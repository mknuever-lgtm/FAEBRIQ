"""Place a real FÆBRIQ front print on a BLANK garment photo (AI-made photos
garble text, so the photo is generated blank and the print added here).

Print centre goes to FRAC of the way from collar seam to armpit (CLAUDE.md
lock: 0.65, mid rib cage). Width = WIDTH_FRAC of the garment's chest width
(armpit to armpit), ~0.45 for a 10 in print on a size L. The fabric's own
light and folds are carried into the ink so it reads printed, not pasted.

Usage: python3 tools/place_print_on_model.py PHOTO PRINT_PNG OUT
       COLLAR_Y ARMPIT_Y CHEST_X0 CHEST_X1 [FRAC=0.65] [WIDTH_FRAC=0.45]
"""
import sys

import numpy as np
from PIL import Image, ImageFilter


def place(photo, art, out, collar, armpit, cx0, cx1, frac=0.65, wfrac=0.45):
    img = Image.open(photo).convert("RGB")
    a = Image.open(art).convert("RGBA")
    a = a.crop(a.getchannel("A").getbbox())
    w = round((cx1 - cx0) * wfrac)
    a = a.resize((w, round(a.height * w / a.width)), Image.LANCZOS)
    x = round((cx0 + cx1) / 2 - a.width / 2)
    y = round(collar + frac * (armpit - collar) - a.height / 2)
    base = np.asarray(img).astype(float)
    region = base[y:y + a.height, x:x + a.width]
    # fabric shading: local luminance relative to its blurred mean, so folds
    # darken/lighten the ink the same way they shade the cloth
    lum = region.mean(2)
    soft = np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.GaussianBlur(25))).astype(float)
    shade = np.clip(1 + (lum - soft) / 60.0, 0.75, 1.15)[..., None]
    ink = np.asarray(a).astype(float)
    rgb = ink[..., :3] * 0.94 * shade          # DTG white sits slightly below pure white
    alpha = np.asarray(a.getchannel("A").filter(ImageFilter.GaussianBlur(0.6))).astype(float)[..., None] / 255 * 0.96
    base[y:y + a.height, x:x + a.width] = region * (1 - alpha) + rgb * alpha
    Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).save(out, quality=93)
    print(f"{out}: print {a.width}x{a.height} at ({x},{y})")


if __name__ == "__main__":
    p = sys.argv
    place(p[1], p[2], p[3], int(p[4]), int(p[5]), int(p[6]), int(p[7]),
          float(p[8]) if len(p) > 8 else 0.65, float(p[9]) if len(p) > 9 else 0.45)
