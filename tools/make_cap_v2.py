"""Cap print file v2: flat six-block stripe on top, FÆBRIQ in sans caps below.

Layout measured off Maurice's approved cap render (2026/09/24): stripe is
~2.55x the wordmark width, wordmark cap height ~1/7 of its width. Printed
DTF, so the stripe is solid blocks with no gaps and no gradient.
"""
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_print_file import CIRCUIT, INK_LIGHT, _fit, font_path  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "print-art")

W, H = 3600, 1500          # 12 x 5 in at 300 dpi; Printify scales it down
STRIPE_W = 3240            # 90% of canvas width
STRIPE_H = 60              # 1:54, about 2 mm tall at a 4.5 in print width
WORD_W = STRIPE_W / 2.55
GAP = 150                  # stripe bottom to wordmark cap top


def hex_rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def build():
    from PIL import ImageFont

    sans = font_path("Inter", "600", "Inter-SemiBold.ttf")
    font = _fit(ImageFont, sans, "FÆBRIQ", WORD_W, "w")
    bb = font.getbbox("FÆBRIQ")
    word_h = bb[3] - bb[1]

    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    top = (H - (STRIPE_H + GAP + word_h)) // 2
    x0 = (W - STRIPE_W) // 2
    seg = STRIPE_W / 6
    for i, c in enumerate(CIRCUIT):
        d.rectangle([round(x0 + i * seg), top, round(x0 + (i + 1) * seg) - 1,
                     top + STRIPE_H - 1], fill=hex_rgb(c) + (255,))

    ty = top + STRIPE_H + GAP
    tw = font.getlength("FÆBRIQ")
    d.text(((W - tw) / 2 - bb[0], ty - bb[1]), "FÆBRIQ", font=font,
           fill=hex_rgb(INK_LIGHT["text"]) + (255,))

    # Trim to the artwork plus a small margin so Printify's placement box
    # scales the design, not empty canvas.
    l, t, r, b = im.getbbox()
    pad = 60
    im = im.crop((l - pad, t - pad, r + pad, b + pad))
    W2, H2 = im.size

    png = os.path.join(OUT, "cap-wordmark-v2-print.png")
    im.save(png, dpi=(300, 300))

    preview = Image.new("RGB", (W2 + 400, H2 + 400), (15, 14, 12))
    preview.paste(im, (200, 200), im)
    preview.save(os.path.join(OUT, "cap-wordmark-v2-preview-on-black.jpg"), quality=92)
    print(png)


if __name__ == "__main__":
    build()
