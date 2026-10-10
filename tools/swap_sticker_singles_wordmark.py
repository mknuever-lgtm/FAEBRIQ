# Swaps the serif FÆBRIQ mark on the 5 live phrase sticker singles (black ink on
# a white die-cut, cut from the sheets on 2026-10-07) for the approved sans
# wordmark, then rebuilds each on-black preview (print file padded 100px onto
# #070707). Only the mark's own box is repainted: phrase, bar and die-cut stay.
#
# Run from the repo root: python3 tools/swap_sticker_singles_wordmark.py
import sys
sys.path.insert(0, 'tools')
import make_print_file as m
import numpy as np
from PIL import Image

DIR = 'assets/print-art/2026-10-07-sticker-singles'
NAMES = ['404', 'code-it', 'deploying', 'not-a-bug', 'please-hold']


def swap(name):
    path = f'{DIR}/sticker-{name}-print.png'
    im = Image.open(path).convert('RGBA')
    a = np.array(im).astype(int)
    rgb, op = a[..., :3], a[..., 3] > 200
    sat = rgb.max(2) - rgb.min(2)
    bar_bottom = np.where(((sat > 80) & op).sum(1) > 200)[0].max()
    # The mark is the only dark ink below the pride-circuit bar.
    dark = (rgb.mean(2) < 110) & op
    dark[:bar_bottom + 1] = False
    ys, xs = np.where(dark)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    ink = tuple(int(v) for v in np.median(rgb[dark], 0)) + (255,)
    # Cap height from the left 40% of the mark (F, Æ, B: no descenders), so the
    # Q tail is ignored; >= 3 ink pixels per row skips stray specks.
    cap = np.where(dark[:, x0:x0 + (x1 - x0) * 4 // 10].sum(1) >= 3)[0]
    cap_h = cap.max() - cap.min() + 1
    pad = 6
    box = (slice(y0 - pad, y1 + pad), slice(x0 - pad, x1 + pad))
    light = op[box] & (rgb[box].mean(2) >= 110)
    paper = tuple(int(v) for v in np.median(rgb[box][light], 0))
    out = np.array(im)
    sub = out[box]
    sub[op[box], :3] = paper  # erase the serif mark to the sticker's own white
    wm = m.wordmark_mask(1000, ink)
    wm = m.wordmark_mask(round(1000 * cap_h / wm.height), ink)
    res = Image.fromarray(out, 'RGBA')
    cx = (x0 + x1) / 2
    res.alpha_composite(wm, (round(cx - wm.width / 2), int(cap.min())))
    res.save(path, 'PNG', dpi=(300, 300))
    ob = Image.new('RGBA', (res.width + 200, res.height + 200), (7, 7, 7, 255))
    ob.alpha_composite(res, (100, 100))
    ob.convert('RGB').save(f'{DIR}/on-black/sticker-{name}-on-black.png')
    print(f'{name}: serif {x1 - x0}x{y1 - y0} -> sans {wm.width}x{wm.height}, ink {ink[:3]}, paper {paper}')


for n in NAMES:
    swap(n)
