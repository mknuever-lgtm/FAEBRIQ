"""Sticker product photos from the print files: each die-cut sticker on a
black #070707 card with a thin light inner border (the live sticker-shot look),
then placed on the charcoal sweep by tools/card_on_sweep.py. Also builds the
Full Drop sheet card (all 5 phrase stickers, same layout as the old sheet).

Run from the repo root: python3 tools/sticker_card_shots.py
"""
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, "tools")
from card_on_sweep import place

SRC = "assets/print-art/2026-10-07-sticker-singles/sticker-{}-print.png"
OUT = "assets/mockups/2026-10-10-sweep/"
CARD_W, CARD_H = 1640, 1180  # matches the live single-sticker card (x 204-1843, y 660-1839)
INK, LINE = (7, 7, 7), (205, 205, 205)


def card(w, h):
    c = Image.new("RGB", (w, h), INK)
    m = round(w * 0.055)
    ImageDraw.Draw(c).rectangle([m, m, w - m, h - m], outline=LINE, width=3)
    return c


def fit(img, box_w, box_h):
    k = min(box_w / img.width, box_h / img.height)
    return img.resize((round(img.width * k), round(img.height * k)), Image.LANCZOS)


def single(name):
    c = card(CARD_W, CARD_H)
    s = fit(Image.open(SRC.format(name)).convert("RGBA"), CARD_W * 0.74, CARD_H * 0.56)
    c.paste(s, ((CARD_W - s.width) // 2, (CARD_H - s.height) // 2), s)
    tmp = f"/tmp/card-{name}.png"
    c.save(tmp)
    place(tmp, f"{OUT}sticker-{name}-A.jpg")


def sheet():
    w, h = 1640, 1093  # 3:2 sheet card, same as the old Full Drop
    c = card(w, h)
    m = round(w * 0.055)
    iw, ih = w - 2 * m, h - 2 * m
    slots = {  # name: (centre x, centre y, max w, max h) as fractions of the inner area
        "deploying": (0.27, 0.19, 0.44, 0.28), "not-a-bug": (0.75, 0.19, 0.40, 0.28),
        "404": (0.5, 0.50, 0.56, 0.30),
        "please-hold": (0.27, 0.81, 0.44, 0.26), "code-it": (0.75, 0.81, 0.34, 0.30),
    }
    for n, (fx, fy, fw, fh) in slots.items():
        s = fit(Image.open(SRC.format(n)).convert("RGBA"), iw * fw, ih * fh)
        c.paste(s, (round(m + iw * fx - s.width / 2), round(m + ih * fy - s.height / 2)), s)
    c.save("/tmp/card-sheet.png")
    place("/tmp/card-sheet.png", f"{OUT}sticker-sheet-full-drop-B.jpg")


if __name__ == "__main__":
    for n in ["404", "code-it", "deploying", "not-a-bug", "please-hold"]:
        single(n)
    sheet()
