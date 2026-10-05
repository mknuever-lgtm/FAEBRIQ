"""Error State hero: desktop banner (3000x1250) and stacked mobile/story (1080x1920).

    python3 assets/campaign/awareness-2026-10/render.py

Fonts come from tools/make_print_file.py's Google Fonts cache, and the wordmark
is the approved sans mark cut from the founder reference (wordmark_mask), with
the six-block bar at 1.35x its width.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from make_print_file import font_path, wordmark_mask  # noqa: E402

BG = (15, 14, 12); FG = (224, 224, 224); SHADOW = (10, 9, 8); FAINT = (26, 25, 22)
DIM = (70, 68, 64)        # registration marks, window controls
NOTE = (112, 110, 104)    # edge annotations, ~4:1 on BG
TAG = (168, 166, 160)     # "This is not an error.", ~8:1 on BG
ACC = (123, 63, 170)
CIRCUIT = [(232, 39, 42), (244, 127, 32), (249, 212, 38), (42, 170, 66), (29, 91, 190), (123, 63, 170)]

BOD = font_path('Bodoni Moda', 400, 'BodoniModa-400.ttf')
MONO = font_path('IBM Plex Mono', 400, 'IBMPlexMono-400.ttf')
mono = lambda s: ImageFont.truetype(MONO, s)
bod = lambda s: ImageFont.truetype(BOD, s)


def frame(d, W, H, M, step):
    """Measurement grid and corner registration marks."""
    for x in range(M, W - M + 1, step): d.line([(x, M), (x, H - M)], fill=FAINT, width=1)
    for y in range(M, H - M + 1, step): d.line([(M, y), (W - M, y)], fill=FAINT, width=1)
    k = round(M * 0.25)
    for cx, cy in [(M, M), (W - M, M), (M, H - M), (W - M, H - M)]:
        d.line([(cx - k, cy), (cx + k, cy)], fill=DIM, width=2); d.line([(cx, cy - k), (cx, cy + k)], fill=DIM, width=2)


def runs(d, x, y, parts, font, right=None):
    """Draw [(text, color), ...] in one line; right-align to `right` if given."""
    if right is not None:
        x = right - sum(d.textlength(t, font=font) for t, _ in parts)
    for t, c in parts:
        d.text((x, y), t, font=font, fill=c); x += d.textlength(t, font=font)


def dialog(d, box, L1, chrome, square_left=True, tag=0.305):
    """system_notice.exe window with the phrase lockup, tagline and two buttons."""
    x0, y0, x1, y1 = box
    off = round(chrome * 0.6)
    d.rectangle([x0 + off, y0 + off, x1 + off, y1 + off], fill=SHADOW)
    d.rectangle([x0, y0, x1, y1], fill=BG, outline=FG, width=3)
    bar = round(chrome * 2.5)
    d.line([(x0, y0 + bar), (x1, y0 + bar)], fill=FG, width=3)
    ft = mono(round(chrome * 0.87))
    d.text((x0 + chrome * 1.2, y0 + (bar - chrome) / 2 - 2), 'system_notice.exe', font=ft, fill=FG)
    s = round(chrome * 0.4)
    for i in range(3):
        cx = x1 - chrome * 1.5 - i * chrome * 1.47; cy = y0 + bar / 2
        d.rectangle([cx - s, cy - s, cx + s, cy + s], outline=DIM, width=2)
    pad = chrome * 2
    sq = round(L1 * 0.41)
    if square_left:
        d.rectangle([x0 + pad, y0 + bar + L1 * 0.65, x0 + pad + sq, y0 + bar + L1 * 0.65 + sq], fill=ACC)
        tx, ty = x0 + pad + sq + L1 * 0.36, y0 + bar + L1 * 0.4
    else:
        d.rectangle([x0 + pad, y0 + bar + pad, x0 + pad + sq, y0 + bar + pad + sq], fill=ACC)
        tx, ty = x0 + pad, y0 + bar + pad + sq + L1 * 0.05
    # phrase lockup: line 2 at 80% of line 1
    d.text((tx, ty), 'Unexpected', font=bod(L1), fill=FG)
    d.text((tx, ty + L1 * 1.12), 'identity detected.', font=bod(round(L1 * 0.8)), fill=FG)
    if tag:  # tag=None leaves the answer for a later slide
        d.text((tx, ty + L1 * 1.12 + L1 * 0.8 * 1.5), 'This is not an error.', font=mono(round(L1 * tag)), fill=TAG)
    # buttons, right-aligned
    fb = mono(round(chrome * 1.0)); bh = round(chrome * 2.4); by = y1 - pad - bh
    xr = x1 - pad
    for label, primary in [('Wear it anyway', True), ('Ignore', False)]:
        w = d.textlength(label, font=fb) + chrome * 2.6; xl = xr - w
        if primary:
            d.rectangle([xl, by, xr, by + bh], fill=FG); c = BG
        else:
            d.rectangle([xl, by, xr, by + bh], outline=NOTE, width=2); c = NOTE
        d.text((xl + chrome * 1.3, by + (bh - chrome) / 2 - chrome * 0.2), label, font=fb, fill=c)
        xr = xl - chrome


def lockup(im, d, x, baseline_bar, ww, prompt_size, center=False, prompt='> process running'):
    """Prompt + sans wordmark + 1.35x circuit bar. Bar's left edge sits at x (or centered on x)."""
    bw = ww * 1.35
    bx = x - bw / 2 if center else x
    bh = max(4, round(bw * 0.016))
    wm = wordmark_mask(ww, FG)
    wx = round(bx + (bw - ww) / 2)
    wy = round(baseline_bar - wm.height * 0.55 - wm.height)
    im.paste(wm, (wx, wy), wm)
    cw = bw / 6
    for i, c in enumerate(CIRCUIT):
        d.rectangle([round(bx + i * cw), baseline_bar, round(bx + (i + 1) * cw) - 1, baseline_bar + bh], fill=c)
    # prompt shares the wordmark's left edge
    d.text((wx, wy - prompt_size * 2.4), prompt, font=mono(prompt_size), fill=NOTE)


def desktop():
    W, H, M = 3000, 1250, 90
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    frame(d, W, H, M, 60)
    f = mono(24); L = M + 40; R = W - M - 40
    runs(d, L, M - 58, [('SYS/FAEBRIQ  ·  PROC 0x0F0E0C  ·  STATUS: UNEXPECTED', NOTE)], f)
    runs(d, 0, M - 58, [('FAEBRIQ.COM', NOTE)], f, right=R)
    runs(d, L, H - M + 28, [('REF. 404 / 2026  ·  US + CA  ·  ', NOTE), ('FREE SHIPPING', FG)], f)
    runs(d, 0, H - M + 28, [('FIG. 01', NOTE)], f, right=R)
    dialog(d, (1240, 280, 2700, 940), 118, 30)
    lockup(im, d, L, H - M - 110, 560, 26)
    return im


def story():
    W, H, M = 1080, 1920, 60
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    frame(d, W, H, M, 40)
    # keep copy inside the IG/TikTok safe band (~250px top, ~340px bottom)
    f = mono(24); L = M + 30; R = W - M - 30
    runs(d, L, 262, [('STATUS: UNEXPECTED', NOTE)], f)
    runs(d, 0, 262, [('FAEBRIQ.COM', NOTE)], f, right=R)
    dialog(d, (M + 20, 340, W - M - 20, 1050), 118, 28, square_left=False)
    lockup(im, d, W / 2, 1370, 560, 26, center=True)
    runs(d, L, 1480, [('US + CA  ·  ', NOTE), ('FREE SHIPPING', FG)], f)
    runs(d, 0, 1480, [('FIG. 01', NOTE)], f, right=R)
    return im


if __name__ == '__main__':
    desktop().save(os.path.join(HERE, 'hero-error-state-3000x1250.png'), optimize=True)
    story().save(os.path.join(HERE, 'hero-error-state-story-1080x1920.png'), optimize=True)
    print('ok')
