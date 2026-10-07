#!/usr/bin/env python3
"""Put a Printify mockup on the FAEBRIQ charcoal studio backdrop (option A, 2026-10-01).

Input: a Printify mockup on its light-grey/white studio background (JPG or PNG),
or a PNG that already has transparency. Output: square JPG, product centred at
~75% of the frame, charcoal backdrop with a soft radial spotlight and a contact
shadow, so black garments keep their silhouette on the near-black storefront.

    python3 tools/make_dark_mockup.py in.jpg out.jpg [--size 2048] [--fill 0.75]
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter

BG_EDGE = np.array([24, 24, 23])      # #181817 corners
BG_CENTRE = np.array([46, 46, 44])    # #2E2E2C spotlight centre


def cutout(im):
    """RGBA cutout. Keeps existing alpha; else keys out the light studio background
    by distance from the colour sampled at the image border."""
    im = im.convert("RGBA")
    a = np.array(im).astype(float)
    if (a[..., 3] < 250).mean() > 0.02:
        return im
    rgb = a[..., :3]
    border = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]])
    bg = np.median(border, axis=0)
    # Products here are dark on a light studio sweep, so alpha comes from how much darker a
    # pixel is than the backdrop. Printify's soft floor shadow lands at partial alpha and
    # reads as a natural shadow on the charcoal.
    lum = rgb.mean(-1)
    alpha = np.clip((bg.mean() - lum - 12) / 70, 0, 1)
    # light print areas (white ink) are enclosed by the product: anything not connected to
    # the outer background becomes fully opaque
    from scipy import ndimage
    lab, _ = ndimage.label(alpha < 0.5)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    alpha[~np.isin(lab, list(edge))] = np.maximum(alpha[~np.isin(lab, list(edge))], 1.0)
    alpha = ndimage.gaussian_filter(alpha, 0.5)
    # un-mix the light backdrop out of semi-transparent edge pixels (kills the white halo)
    am = np.clip(alpha, 0.05, 1)[..., None]
    a[..., :3] = np.clip((rgb - (1 - am) * bg) / am, 0, 255)
    a[..., 3] = alpha * 255
    return Image.fromarray(a.astype("uint8"), "RGBA")


def backdrop(size):
    y, x = np.mgrid[0:size, 0:size].astype(float)
    cx, cy = size / 2, size * 0.46
    r = np.sqrt((x - cx) ** 2 + ((y - cy) * 1.1) ** 2) / (size * 0.62)
    t = np.clip(r, 0, 1) ** 1.6
    img = BG_CENTRE * (1 - t[..., None]) + BG_EDGE * t[..., None]
    rng = np.random.default_rng(7)
    img += rng.normal(0, 1.2, img.shape)  # faint grain so it reads as a surface, not a flat fill
    return Image.fromarray(np.clip(img, 0, 255).astype("uint8"), "RGB")


def build(src, out, size=2048, fill=0.75):
    prod = cutout(Image.open(src))
    prod = prod.crop(prod.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox())
    k = fill * size / max(prod.size)
    prod = prod.resize((round(prod.width * k), round(prod.height * k)), Image.LANCZOS)
    canvas = backdrop(size).convert("RGBA")
    x = (size - prod.width) // 2
    y = (size - prod.height) // 2 - round(size * 0.02)
    # contact shadow: flattened ellipse under the product
    sh = Image.new("L", (size, size), 0)
    from PIL import ImageDraw
    sw, shh = prod.width * 0.8, size * 0.035
    sy = y + prod.height - shh * 0.4
    ImageDraw.Draw(sh).ellipse([size / 2 - sw / 2, sy, size / 2 + sw / 2, sy + shh], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(size * 0.018))
    canvas = Image.composite(Image.new("RGBA", (size, size), (8, 8, 8, 255)), canvas, sh)
    canvas.alpha_composite(prod, (x, y))
    canvas.convert("RGB").save(out, "JPEG", quality=92)
    return out


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("src"); p.add_argument("out")
    p.add_argument("--size", type=int, default=2048)
    p.add_argument("--fill", type=float, default=0.75)
    a = p.parse_args()
    print(build(a.src, a.out, a.size, a.fill))
