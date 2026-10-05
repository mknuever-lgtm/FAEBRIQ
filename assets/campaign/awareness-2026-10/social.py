"""Error State social set: square post (1080x1080) and carousel (1080x1350).

    python3 assets/campaign/awareness-2026-10/social.py

Reuses render.py's palette, dialog and lockup. Carousel slide 02 (product) is
held until the Manus mockups land; files are numbered so it drops straight in.
"""
import os

from PIL import Image, ImageDraw

from render import (BG, FG, NOTE, TAG, ACC, CIRCUIT, mono, bod, frame, runs, dialog,
                    lockup, HERE)

OUT = os.path.join(HERE, 'social')


def canvas(W, H, M, step):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    frame(d, W, H, M, step)
    return im, d


def button(d, x, y, label, chrome, primary=True, right=False):
    f = mono(round(chrome)); w = d.textlength(label, font=f) + chrome * 2.6; h = round(chrome * 2.4)
    xl = x - w if right else x
    if primary:
        d.rectangle([xl, y, xl + w, y + h], fill=FG); c = BG
    else:
        d.rectangle([xl, y, xl + w, y + h], outline=NOTE, width=2); c = NOTE
    d.text((xl + chrome * 1.3, y + (h - chrome) / 2 - chrome * 0.2), label, font=f, fill=c)
    return xl, w, h


def square():
    """Job: stop the scroll. Phrase + wordmark, nothing to read twice."""
    W = H = 1080; M = 60
    im, d = canvas(W, H, M, 40)
    f = mono(24); L = M + 30; R = W - M - 30
    runs(d, L, 90, [('STATUS: UNEXPECTED', NOTE)], f)
    runs(d, 0, 90, [('FAEBRIQ.COM', NOTE)], f, right=R)
    dialog(d, (M + 20, 130, W - M - 20, 722), 100, 26, square_left=False, tag=0.40)
    lockup(im, d, W / 2, 930, 380, 24, center=True)
    runs(d, L, H - M - 56, [('US + CA  ·  ', NOTE), ('FREE SHIPPING', FG)], mono(32))
    runs(d, 0, H - M - 50, [('FIG. 01', NOTE)], f, right=R)
    return im


def slide(n, total):
    f = mono(24); W, H, M = 1080, 1350, 60
    im, d = canvas(W, H, M, 40)
    L = M + 30; R = W - M - 30
    runs(d, L, 90, [('STATUS: UNEXPECTED', NOTE)], f)
    runs(d, 0, 90, [(f'{n:02d} / {total:02d}', NOTE)], f, right=R)
    return im, d, W, H, M, L, R


def s01():
    """Hook: the dialog, with a swipe cue."""
    im, d, W, H, M, L, R = slide(1, 4)
    dialog(d, (M + 20, 190, W - M - 20, 930), 118, 28, square_left=False, tag=0.373)
    lockup(im, d, W / 2, 1200, 400, 24, center=True)
    runs(d, 0, H - M - 56, [('SWIPE  >', FG)], mono(32), right=R)
    return im


def s03():
    """Message: the reframe, in terminal output."""
    im, d, W, H, M, L, R = slide(3, 4)
    d.rectangle([L, 250, L + 56, 306], fill=ACC)
    d.text((L, 360), 'This is', font=bod(150), fill=FG)
    d.text((L, 360 + 150 * 1.12), 'not an error.', font=bod(150), fill=FG)
    y = 800
    for line, c in [('> scan complete', NOTE), ('> identity: confirmed', TAG), ('> status: wearable', FG)]:
        d.text((L, y), line, font=mono(44), fill=c); y += 76
    runs(d, L, H - M - 50, [('FAEBRIQ.COM', NOTE)], mono(24))
    return im


def s04():
    """CTA: wordmark, the one button, shipping."""
    im, d, W, H, M, L, R = slide(4, 4)
    lockup(im, d, W / 2, 700, 560, 26, center=True)
    c = 40; bw = d.textlength('Wear it anyway', font=mono(c)) + c * 2.6
    button(d, W / 2 - bw / 2, 830, 'Wear it anyway', c)
    f = mono(36); t = 'faebriq.com'
    d.text((W / 2 - d.textlength(t, font=f) / 2, 990), t, font=f, fill=TAG)
    f2 = mono(32); parts = [('US + CA  ·  ', NOTE), ('FREE SHIPPING', FG)]
    x = W / 2 - sum(d.textlength(p, font=f2) for p, _ in parts) / 2
    runs(d, x, 1070, parts, f2)
    return im


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    square().save(os.path.join(OUT, 'square-1080x1080.png'), optimize=True)
    for name, fn in [('carousel-01-hook', s01), ('carousel-03-message', s03), ('carousel-04-cta', s04)]:
        fn().save(os.path.join(OUT, f'{name}-1080x1350.png'), optimize=True)
    print('ok')
