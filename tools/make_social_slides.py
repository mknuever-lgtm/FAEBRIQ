# Renders the Instagram launch carousels (posts 1 and 2 of SOCIAL_LAUNCH_POSTS_2026-09-23.md)
# as 1080x1350 (4:5) PNGs. Run from the repo root: python3 tools/make_social_slides.py
import os, sys
sys.path.insert(0, 'tools')
import make_print_file as m
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, PAD = 1080, 1350, 96
BG, TEXT, DIM = '#0f0e0c', '#e0e0e0', '#9a9a9a'
OUT = 'assets/social/launch-2026-09'
SERIF = m.font_path('Instrument Serif', None, 'InstrumentSerif-Regular.ttf')
ITAL = m.font_path('Instrument Serif:ital', None, 'InstrumentSerif-Italic.ttf')
MONO = m.font_path('IBM Plex Mono', None, 'IBMPlexMono-Regular.ttf')
LOCKUP = 'assets/print-art/off-the-clock-still-iconic-light-4500.png'


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, width):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= width or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + [cur]


def stripe(im, x, y, w, h):
    d = ImageDraw.Draw(im)
    gap = max(2, round(w * m.SRC['gap_frac']))
    bw = (w - 5 * gap) / 6
    for i, c in enumerate(m.CIRCUIT):
        x0 = x + i * (bw + gap)
        d.rectangle([round(x0), y, round(x0 + bw) - 1, y + h - 1], fill=c)


def lockup(width, lit):
    """Off The Clock print art scaled to width. lit: set of parts at full ink (1, 2, 'stripe');
    the rest drop to 18% so the slide points at one part of the system."""
    art = Image.open(LOCKUP).convert('RGBA')
    a = np.array(art.getchannel('A'))
    rows = np.where((a > 20).any(1))[0]
    bands, start = [], rows[0]
    for p, q in zip(rows, rows[1:]):
        if q - p > 1:
            bands.append((start, p + 1)); start = q
    bands.append((start, rows[-1] + 1))
    cuts = [0, (bands[0][1] + bands[1][0]) // 2, (bands[1][1] + bands[2][0]) // 2, a.shape[0]]
    alpha = a.astype(float)
    for part, lo, hi in zip((1, 2, 'stripe'), cuts, cuts[1:]):
        if part not in lit:
            alpha[lo:hi] *= 0.18
    art.putalpha(Image.fromarray(alpha.astype('uint8')))
    cols = np.where((a > 20).any(0))[0]
    art = art.crop((cols[0], bands[0][0], cols[-1] + 1, bands[-1][1]))
    return art.resize((width, round(art.height * width / art.width)), Image.LANCZOS)


def slide(blocks, n, total, label, last=False):
    """blocks: list of ('text', font_path, size, color, text) | ('gap', px) | ('stripe', w, h) | ('img', Image)."""
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    mono = font(MONO, 24)
    d.text((PAD, PAD - 30), label, font=mono, fill=DIM)
    num = f'{n:02d} / {total:02d}'
    d.text((W - PAD - d.textlength(num, font=mono), PAD - 30), num, font=mono, fill=DIM)
    d.text((PAD, H - PAD), 'faebriq.com', font=mono, fill=DIM)
    if not last:
        d.text((W - PAD - d.textlength('swipe ->', font=mono), H - PAD), 'swipe ->', font=mono, fill=DIM)

    items, total_h = [], 0
    for b in blocks:
        if b[0] == 'text':
            _, path, size, color, text = b
            f = font(path, size)
            lh = round(size * 1.12)
            for line in wrap(d, text, f, W - 2 * PAD):
                items.append(('line', f, color, line, lh)); total_h += lh
        elif b[0] == 'gap':
            items.append(b); total_h += b[1]
        elif b[0] == 'stripe':
            items.append(b); total_h += b[2]
        elif b[0] == 'img':
            items.append(b); total_h += b[1].height
    y = (H - total_h) // 2
    for it in items:
        if it[0] == 'line':
            _, f, color, line, lh = it
            asc = f.getmetrics()[0]
            d.text((PAD, y + (lh - f.size) // 2 + f.size - asc), line, font=f, fill=color)
            y += lh
        elif it[0] == 'gap':
            y += it[1]
        elif it[0] == 'stripe':
            stripe(im, PAD, y, it[1], it[2]); y += it[2]
        elif it[0] == 'img':
            im.paste(it[1], (PAD, y), it[1]); y += it[1].height
    return im


def centered_wordmark(n, total):
    im = slide([], n, total, '> boot sequence')
    d = ImageDraw.Draw(im)
    f = font(SERIF, 230)
    tw = d.textlength('FÆBRIQ', font=f)
    x, y = (W - tw) / 2, 470
    d.text((x, y), 'FÆBRIQ', font=f, fill=TEXT)
    sy = y + 300
    stripe(im, round(x), sy, round(tw), max(8, round(tw * m.SRC['bar_h'])))
    fi = font(ITAL, 76)
    sub = 'System online.'
    d.text(((W - d.textlength(sub, font=fi)) / 2, sy + 70), sub, font=fi, fill=TEXT)
    return im


def main():
    os.makedirs(OUT, exist_ok=True)
    cw = W - 2 * PAD
    post1 = [
        centered_wordmark(1, 5),
        slide([('text', SERIF, 92, TEXT, 'Queer-coded apparel for people who work in tech'),
               ('gap', 28),
               ('text', ITAL, 92, TEXT, 'and live out loud at a reasonable volume.')], 2, 5, '> boot sequence'),
        slide([('text', SERIF, 104, TEXT, 'One stripe per piece.'),
               ('gap', 56), ('stripe', 560, 14), ('gap', 72),
               ('text', SERIF, 56, DIM, 'Most people read it as design.'),
               ('gap', 16),
               ('text', ITAL, 56, TEXT, 'The right people read it as something else.')], 3, 5, '> boot sequence'),
        slide([('text', SERIF, 104, TEXT, 'Ships US + Canada.'),
               ('gap', 40),
               ('text', ITAL, 72, TEXT, 'Shipping is already in the price.'),
               ('gap', 56),
               ('text', MONO, 30, DIM, '0 surprise fees at checkout. 0 bugs.')], 4, 5, '> boot sequence'),
        slide([('text', SERIF, 140, TEXT, 'faebriq.com'),
               ('gap', 40), ('stripe', 560, 14), ('gap', 48),
               ('text', ITAL, 72, TEXT, 'link in bio')], 5, 5, '> boot sequence', last=True),
    ]
    post2 = [
        slide([('text', SERIF, 128, TEXT, 'HOW TO READ'),
               ('text', SERIF, 128, TEXT, 'THIS BRAND'),
               ('gap', 40),
               ('text', ITAL, 72, DIM, 'a field guide')], 1, 5, '> field guide'),
        slide([('text', MONO, 30, DIM, 'LINE 1 / THE STATEMENT'), ('gap', 48),
               ('img', lockup(cw, {1})), ('gap', 72),
               ('text', SERIF, 76, TEXT, 'Serif caps.'),
               ('text', ITAL, 76, TEXT, 'Says the thing.')], 2, 5, '> field guide'),
        slide([('text', MONO, 30, DIM, 'LINE 2 / THE FOOTNOTE'), ('gap', 48),
               ('img', lockup(cw, {2})), ('gap', 72),
               ('text', SERIF, 76, TEXT, 'Smaller.'),
               ('text', ITAL, 76, TEXT, 'Where the joke lives.')], 3, 5, '> field guide'),
        slide([('text', MONO, 30, DIM, 'THE STRIPE'), ('gap', 48),
               ('img', lockup(cw, {'stripe'})), ('gap', 72),
               ('text', SERIF, 64, TEXT, 'Six blocks, flat.'), ('gap', 20),
               ('text', SERIF, 64, DIM, 'To your manager: a nice detail.'),
               ('text', ITAL, 64, TEXT, 'To us: a handshake.')], 4, 5, '> field guide'),
        slide([('img', lockup(cw, {1, 2, 'stripe'})), ('gap', 96),
               ('text', SERIF, 84, TEXT, 'Nobody has to'),
               ('text', SERIF, 84, TEXT, 'explain anything.'),
               ('gap', 16),
               ('text', ITAL, 84, TEXT, "That's the feature.")], 5, 5, '> field guide', last=True),
    ]
    for p, slides in ((1, post1), (2, post2)):
        for i, im in enumerate(slides, 1):
            im.save(f'{OUT}/post{p}-slide{i}.png')
    print('wrote', len(post1) + len(post2), 'slides to', OUT)


if __name__ == '__main__':
    main()
