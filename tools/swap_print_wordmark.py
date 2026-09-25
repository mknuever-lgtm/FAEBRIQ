# Swaps the small FÆBRIQ signature mark on the sticker/cap print files from the old
# serif render to the approved sans wordmark (Maurice, 2026-09-23; see CLAUDE.md and
# IMAGERY_SPEC_2026-09-23.md). Touches ONLY the mark glyph pixels: the phrase lines,
# label and pride-circuit bar on each sticker are hand pixel-shifted (see CHANGELOG
# 2026-09-09 merge-resolution note) and are left completely untouched here.
#
# Run from the repo root: python3 tools/swap_print_wordmark.py
import glob
import sys
sys.path.insert(0, 'tools')
import make_print_file as m
import numpy as np
from PIL import Image

REF = 'assets/print-art/reference/wordmark-reference-2026-09-23.jpg'
STICKERS = sorted(glob.glob('assets/print-art/sticker-final-system-2026-08-27/*sticker-light-2400.png'))
MARK_HEX = m.INK_LIGHT['mark']  # #C0C0C0 -- unchanged: only the typeface changes, not the tone


def wordmark_mask(width, color):
    """The approved sans wordmark cut from Maurice's reference, as a solid-color RGBA at `width`."""
    ref = np.array(Image.open(REF).convert('L')).astype(float)
    top, bottom, left, right = 570, 800, 490, 1516  # crop box for the middle (approved) wordmark
    a = np.clip((ref[top:bottom, left:right] - 16) / (232 - 16), 0, 1) * 255
    cols = np.where((a > 40).any(0))[0]
    a = a[:, cols[0]:cols[-1] + 1]
    im = Image.new('RGBA', a.shape[::-1], color)
    im.putalpha(Image.fromarray(a.astype('uint8')))
    k = width / im.width
    return im.resize((width, round(im.height * k)), Image.LANCZOS)


def find_mark_band(alpha):
    """The FÆBRIQ mark is the lowest contiguous alpha band in the file (label/lines/bar sit above it)."""
    rows = np.where((alpha > 20).any(1))[0]
    bands, start = [], rows[0]
    for p, q in zip(rows, rows[1:]):
        if q - p > 1:
            bands.append((start, p + 1)); start = q
    bands.append((start, rows[-1] + 1))
    lo, hi = bands[-1]
    cols = np.where((alpha[lo:hi] > 20).any(0))[0]
    return lo, hi, cols[0], cols[1] + 1 if False else cols[-1] + 1


def swap_sticker(path):
    im = Image.open(path).convert('RGBA')
    a = np.array(im.getchannel('A'))
    lo, hi, x0, x1 = find_mark_band(a)
    hex_ = MARK_HEX.lstrip('#')
    color = tuple(int(hex_[i:i + 2], 16) for i in (0, 2, 4)) + (255,)
    mark = wordmark_mask(x1 - x0, color)
    out = np.array(im)
    out[lo:hi, x0:x1] = 0  # erase the old serif mark, exactly its own band -- nothing else touches
    out_im = Image.fromarray(out, 'RGBA')
    y = lo + (hi - lo - mark.height) // 2
    out_im.paste(mark, (x0, y), mark)
    out_im.save(path, 'PNG', dpi=(300, 300))
    print('swapped mark on', path, f'-> {x1 - x0}x{mark.height} at y={y}')


def rebuild_cap(path, width):
    """Cap wordmark files carry no phrase -- pure logo lockup, so rebuild fully as
    sans wordmark + six-block bar at 1.35x the wordmark width (CLAUDE.md, 2026-09-24)."""
    hex_ = MARK_HEX.lstrip('#')
    text_color = tuple(int(hex_[i:i + 2], 16) for i in (0, 2, 4)) + (255,)
    wm = wordmark_mask(width, text_color)
    bar_w, bar_h, gap = round(width * 1.35), round(width * 0.045), round(width * 0.006)
    pad = round(width * 0.12)
    canvas_w = max(wm.width, bar_w) + 2 * pad
    canvas_h = wm.height + bar_h + round(width * 0.09) + 2 * pad
    im = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
    cx = canvas_w // 2
    im.paste(wm, (cx - wm.width // 2, pad), wm)
    by = pad + wm.height + round(width * 0.09)
    bx = cx - bar_w // 2
    from PIL import ImageDraw
    d = ImageDraw.Draw(im)
    for i, c in enumerate(m.CIRCUIT):
        d.rectangle([bx + round(i * bar_w / 6), by, bx + round((i + 1) * bar_w / 6) - 1, by + bar_h - 1], fill=c)
    im.save(path, 'PNG', dpi=(300, 300))
    print('rebuilt', path, im.size)


def main():
    for f in STICKERS:
        swap_sticker(f)
    # Print-resolution rebuild (300dpi, ~10in wide) -- the committed files were 500x200
    # placeholder scale, far below DTG/DTF print resolution.
    rebuild_cap('assets/print-art/cap-wordmark-slim.png', 3000)
    rebuild_cap('assets/print-art/cap-wordmark-structured.png', 3000)


if __name__ == '__main__':
    main()
