"""Cap print file v3: FÆBRIQ in sans caps on top, flat six-block stripe UNDER it.

Maurice's call (2026/09/24): wordmark font from the approved cap render
(Inter SemiBold, same as v2), stripe underneath like the rest of the brand,
and the stripe at least as wide as the word. One file per stripe ratio so
the widths can be compared side by side.
"""
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_print_file import CIRCUIT, INK_LIGHT, _fit, font_path  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "print-art")

WORD_W = 2400              # wordmark width in px, 8 in at 300 dpi before scaling
RATIOS = (1.1, 1.35, 1.7)  # stripe width as a multiple of the wordmark width
BAR_H = 0.024              # stripe height as a fraction of the WORD width
GAP = 0.40                 # wordmark baseline to stripe top, x cap height
PAD = 60


def hex_rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def build(ratio, font):
    bb = font.getbbox("FÆBRIQ")
    tw, th = font.getlength("FÆBRIQ"), bb[3] - bb[1]
    sw, sh = round(WORD_W * ratio), round(WORD_W * BAR_H)
    gap = round(th * GAP)

    W, H = sw + 2 * PAD, th + gap + sh + 2 * PAD
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.text(((W - tw) / 2 - bb[0], PAD - bb[1]), "FÆBRIQ", font=font,
           fill=hex_rgb(INK_LIGHT["text"]) + (255,))

    y0, x0, seg = PAD + th + gap, PAD, sw / 6
    for i, c in enumerate(CIRCUIT):
        d.rectangle([round(x0 + i * seg), y0, round(x0 + (i + 1) * seg) - 1,
                     y0 + sh - 1], fill=hex_rgb(c) + (255,))

    tag = f"{ratio:.2f}".replace(".", "p")
    path = os.path.join(OUT, f"cap-wordmark-v3-stripe-{tag}x.png")
    im.save(path, dpi=(300, 300))
    return path, im


def main():
    from PIL import ImageFont

    font = _fit(ImageFont, font_path("Inter", "600", "Inter-SemiBold.ttf"),
                "FÆBRIQ", WORD_W, "w")
    built = [build(r, font) for r in RATIOS]

    # Comparison sheet on the site black, same wordmark size in each row.
    cw = max(im.width for _, im in built) + 400
    rows = [im for _, im in built]
    sheet = Image.new("RGB", (cw, sum(im.height + 200 for im in rows) + 200), (15, 14, 12))
    y = 200
    for im in rows:
        sheet.paste(im, ((cw - im.width) // 2, y), im)
        y += im.height + 200
    sheet.save(os.path.join(OUT, "cap-wordmark-v3-compare-on-black.jpg"), quality=90)
    for p, _ in built:
        print(p)


if __name__ == "__main__":
    main()
