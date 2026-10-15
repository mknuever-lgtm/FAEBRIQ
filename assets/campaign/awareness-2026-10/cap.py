"""Cap product set: cutouts from the white-background mockups, plus carousel slide 02.

    python3 assets/campaign/awareness-2026-10/cap.py

Sources live in product/src (front 1600px native, left/right 2048px). Outputs:
product/cap-{front,left,right}.png (transparent) and social/carousel-03-product-1080x1350.png.
"""
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as ndi

from render import BG, FG, NOTE, TAG, frame, mono, runs
from social import OUT

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'product', 'src')
PROD = os.path.join(HERE, 'product')


def cutout(path):
    """White-background product shot to transparent PNG. Cap is near-black, so the dark
    component is the cap; holes (the print) are filled back in; the soft floor shadow drops out."""
    im = Image.open(path).convert('RGB'); a = np.asarray(im).astype(int)
    dark = a.max(axis=2) < 72
    lab, n = ndi.label(dark)
    keep = lab == (np.argmax(ndi.sum(dark, lab, range(1, n + 1))) + 1)
    keep = ndi.binary_closing(keep, iterations=3)
    # Only the print's own holes get filled back in; enclosed background (under the brim) stays out.
    strong = ((a.min(axis=2) > 200) | ((a.max(axis=2) - a.min(axis=2)) > 90)) & ndi.binary_fill_holes(keep)
    ys, xs = np.where(strong & ~dark)
    box = np.zeros_like(keep)
    if len(ys):
        box[max(ys.min() - 15, 0):ys.max() + 15, max(xs.min() - 15, 0):xs.max() + 15] = True
    holes = ndi.binary_fill_holes(keep) & ~keep
    lab_h, nh = ndi.label(holes)
    for i in range(1, nh + 1):
        comp = lab_h == i
        if (comp & box).sum() > 0.5 * comp.sum():
            keep |= comp
    keep = ndi.binary_erosion(keep, iterations=1)  # shave the white fringe
    alpha = ndi.gaussian_filter(keep.astype(float), 1.0)
    out = np.dstack([a, (alpha * 255).astype(int)]).astype(np.uint8)
    im = Image.fromarray(out, 'RGBA')
    return im.crop(im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox())


def rim_light(cap, strength=0.55, depth=5):
    """Cool edge highlight along the upper silhouette so black reads against near-black."""
    al = np.asarray(cap.getchannel('A')).astype(float) / 255
    edge = np.clip(al - ndi.grey_erosion(al, size=(depth, depth)), 0, 1)
    h = al.shape[0]
    top = np.clip(1 - np.arange(h)[:, None] / (h * 0.65), 0, 1) ** 1.2
    k = edge * top * strength
    rgb = np.asarray(cap.convert('RGB')).astype(float)
    tint = np.array([170, 172, 178], float)
    rgb = rgb + (tint - rgb) * k[..., None]
    return Image.merge('RGBA', [Image.fromarray(rgb[..., i].astype(np.uint8)) for i in range(3)] + [cap.getchannel('A')])


def glow(size, center, radius, color, peak=1.0):
    """Soft radial lift behind the product."""
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - center[0]) ** 2 + (yy - center[1]) ** 2) / radius
    k = np.clip(1 - d, 0, 1) ** 2 * peak
    base = np.array(BG, float); col = np.array(color, float)
    return Image.fromarray((base + (col - base) * k[..., None]).astype(np.uint8), 'RGB')


def s03(front):
    """Product slide: cap hero on a lifted near-black, label, shipping line."""
    f = mono(24); W, H, M = 1080, 1350, 60; L = M + 30; R = W - M - 30
    base = glow((W, H), (W / 2, 520), 640, (84, 83, 80))
    grid = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gdraw = ImageDraw.Draw(grid)
    frame(gdraw, W, H, M, 40)
    base.paste(grid, (0, 0), grid)
    d = ImageDraw.Draw(base)
    runs(d, L, 90, [('STATUS: UNEXPECTED', NOTE)], f)
    runs(d, 0, 90, [('03 / 04', NOTE)], f, right=R)
    cap = rim_light(front)
    tw = 700; cap = cap.resize((tw, round(cap.height * tw / cap.width)), Image.LANCZOS)
    # soft contact shadow
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    cx, cy = W // 2, 225 + cap.height - 20
    sd.ellipse([cx - 270, cy - 18, cx + 270, cy + 42], fill=(0, 0, 0, 190))
    base.paste(sh.filter(ImageFilter.GaussianBlur(26)), (0, 0), sh.filter(ImageFilter.GaussianBlur(26)))
    base.paste(cap, ((W - tw) // 2, 225), cap)
    f3 = mono(32); t = '> new hardware detected'
    d.text(((W - d.textlength(t, font=f3)) / 2, 985), t, font=f3, fill=NOTE)
    ft = mono(54); t = 'FÆBRIQ CAP'
    d.text(((W - d.textlength(t, font=ft)) / 2, 1040), t, font=ft, fill=FG)
    f2 = mono(32); parts = [('US + CA  ·  ', NOTE), ('FREE SHIPPING', FG)]
    x = W / 2 - sum(d.textlength(p, font=f2) for p, _ in parts) / 2
    runs(d, x, 1135, parts, f2)
    return base


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    cuts = {}
    for name in ('front', 'left', 'right'):
        cuts[name] = cutout(os.path.join(SRC, f'cap-{name}.jpg'))
        cuts[name].save(os.path.join(PROD, f'cap-{name}.png'), optimize=True)
    s03(cuts['front']).save(os.path.join(OUT, 'carousel-03-product-1080x1350.png'), optimize=True)
    print('ok')
