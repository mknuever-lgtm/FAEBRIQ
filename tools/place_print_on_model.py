"""Place a real FÆBRIQ front print on a BLANK garment photo (AI-made photos
garble text, so the photo is generated blank and the print added here).

Print centre goes to FRAC of the way from collar seam to armpit (CLAUDE.md
lock: 0.65, mid rib cage). Width = WIDTH_FRAC of the garment's chest width
(armpit to armpit), ~0.45 for a 10 in print on a size L. The fabric's own
light and folds are carried into the ink so it reads printed, not pasted.

ARMPIT_Y = underarm crease where the inner arm leaves the torso, NOT the
shoulder/sleeve seam (see PRINT_PLACEMENT_SPEC.md, How to measure).

Usage: python3 tools/place_print_on_model.py PHOTO PRINT_PNG OUT
       COLLAR_Y ARMPIT_Y CHEST_X0 CHEST_X1 [FRAC=0.65] [WIDTH_FRAC=0.45]
       [STRING_WINDOWS e.g. 590-660,800-870 (hoodie drawstrings, kept on top)]
"""
import sys

import numpy as np

STRING_W = 28
from PIL import Image, ImageFilter


def string_mask(base, windows, y0, y1, width):
    """Track hanging drawstrings (knit texture = high local detail) inside the
    given x windows, so they can be laid back OVER the print like on a real
    hoodie. Returns a soft 0..1 mask."""
    lum = base.mean(2)
    blur = np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.GaussianBlur(4))).astype(float)
    detail = np.abs(lum - blur)
    m = np.zeros(lum.shape)
    for wx0, wx1 in windows:
        prev = None
        for y in range(y0, y1):
            row = np.convolve(detail[y, wx0:wx1], np.ones(width) / width, mode="same")
            c = wx0 + int(np.argmax(row))
            if prev is not None and abs(c - prev) > 3:
                c = prev + (3 if c > prev else -3)  # strings hang smoothly
            prev = c
            m[y, c - width // 2:c + width // 2 + 1] = 1
    return np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))).astype(float)[..., None] / 255


def place(photo, art, out, collar, armpit, cx0, cx1, frac=0.65, wfrac=0.45, strings=None):
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
    orig = base.copy()
    base[y:y + a.height, x:x + a.width] = region * (1 - alpha) + rgb * alpha
    if strings:  # [(x0, x1), ...] windows, string width ~ STRING_W px
        sm = string_mask(orig, strings, y - 10, y + a.height + 10, STRING_W)
        base = base * (1 - sm) + orig * sm
    Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).save(out, quality=93)
    print(f"{out}: print {a.width}x{a.height} at ({x},{y})")


if __name__ == "__main__":
    p = sys.argv
    place(p[1], p[2], p[3], int(p[4]), int(p[5]), int(p[6]), int(p[7]),
          float(p[8]) if len(p) > 8 else 0.65, float(p[9]) if len(p) > 9 else 0.45,
          [tuple(map(int, w.split("-"))) for w in p[10].split(",")] if len(p) > 10 else None)
