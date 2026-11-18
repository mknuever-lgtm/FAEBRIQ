"""Turn Printify white-background mockups into studio-table product shots.

The white studio ground becomes a grey studio table under one lamp (Maurice
picked it 2026-11-18, "pool 140 to 42 + shadow"; replaces the 2026-10-04
charcoal sweep): a lamp hot spot (RGB ~140) behind the garment that shows as
a soft light halo around it, falling off to a dark table (~42 at the corners),
faint table grain, and a soft contact shadow under the garment so it reads
as lying on the surface.
The original drop shadow is kept as a darker tone, and the frame is 4:5
(2048x2560) per IMAGERY_SPEC_2026-09-23.md.
--flat gives a flat #515152 ground with no lamp and no contact shadow.
--soft-shadow=LUM sets the ground cutoff (default 85).
The filename stays for compatibility (tools/card_on_sweep.py imports it).

Usage: python3 tools/mockup_to_charcoal.py IN_DIR OUT_DIR [--flat] [--soft-shadow[=LUM]] [--print-closeup]
--print-closeup: feed it front flats (the -A mockups); writes NAME-print.jpg,
a close-up framing the whole front print (replaces Printify's collar close-ups,
which cut the slogan off).
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

GROUND = np.array([81, 81, 82], dtype=float)   # #515152, flat base (--flat)
EDGE = np.array([42, 42, 42], dtype=float)     # table outside the lamp
CENTER = np.array([140, 140, 141], dtype=float)  # lamp hot spot, behind the garment
POOL_R = 1350    # px: lamp pool radius
POOL_POW = 2.2   # falloff steepness; the light hugs the garment as a halo
POOL_CY = 0.46   # pool centre height as a share of the frame
SHADOW = 0.35                 # contact shadow strength under the garment
SCALE = 1.12  # full product shots: garment ~12% bigger in frame (2026-11-18)
OUT_W, OUT_H = 2048, 2560
LUM_T = 85  # ground cutoff. 85 (default since 2026-11-18) also clears the dark
# drop shadow under a cap brim; checked on all 27 mockups in
# assets/mockups/2026-10-01 with no white print lost. --soft-shadow=150
# restores the old cutoff.


def sweep(flat=False):
    """Canvas-sized ground: flat #515152, or the lamp pool on a grey table."""
    if flat:
        return np.broadcast_to(GROUND, (OUT_H, OUT_W, 3)).astype(float)
    y, x = np.mgrid[0:OUT_H, 0:OUT_W].astype(float)
    r = np.hypot(x - OUT_W / 2, (y - OUT_H * POOL_CY) * 0.92) / POOL_R
    t = np.clip(1 - r, 0, 1) ** POOL_POW
    t = ndimage.gaussian_filter(t, 60)[..., None]  # soft edge, no ring
    g = EDGE + (CENTER - EDGE) * t
    # Faint table grain: reads as a surface and stops banding after Shopify
    # recompresses the file.
    grain = ndimage.gaussian_filter(
        np.random.default_rng(7).normal(0, 1, (OUT_H, OUT_W)), 1.5) * 1.6
    return g + grain[..., None]


def convert(src: Path, flat=False) -> Image.Image:
    a = np.asarray(Image.open(src).convert("RGB")).astype(float)
    h, w, _ = a.shape
    lum = a @ [0.299, 0.587, 0.114]
    sat = a.max(2) - a.min(2)

    # Candidate ground: light and unsaturated (white plus its grey shadow).
    cand = (lum > LUM_T) & (sat < 30)
    labels, n = ndimage.label(cand)
    if n:
        area = ndimage.sum(np.ones_like(lum), labels, index=range(1, n + 1))
        mean_l = ndimage.mean(lum, labels, index=range(1, n + 1))
        # Ground = big components, or border-touching ones that are near white.
        # White print strokes are small and sit inside the dark garment.
        edge_ids = set(np.unique(np.concatenate(
            [labels[0], labels[-1], labels[:, 0], labels[:, -1]])))
        keep = np.zeros(n + 1, bool)
        for i in range(1, n + 1):
            big = area[i - 1] > 0.03 * h * w
            edge_white = i in edge_ids and mean_l[i - 1] > 240 and area[i - 1] > 0.002 * h * w
            # Enclosed pure-white pockets (inside tote handles). Printed white
            # on fabric never reads this clean, so it stays.
            pocket = mean_l[i - 1] > 247 and area[i - 1] > 0.002 * h * w
            # Soft grey shadow pockets under a brim or fold: sizeable, never print.
            shadow = area[i - 1] > 0.008 * h * w
            keep[i] = big or edge_white or pocket or shadow
        ground = keep[labels]
    else:
        ground = cand

    # Grow 2px to swallow the anti-aliased halo, then feather.
    ground = ndimage.binary_dilation(ground, iterations=2)
    alpha = ndimage.gaussian_filter(ground.astype(float), 1.2)[..., None]

    # A close-up whose garment runs off the top or bottom edge would show a hard
    # fabric-to-ground line if padded, so crop it to 4:5 instead.
    if min(alpha[0].mean(), alpha[-1].mean()) < 0.7:
        cw = round(h * OUT_W / OUT_H)
        x0 = (w - cw) // 2
        crop = lambda arr: arr[:, x0:x0 + cw]
        a, alpha, lum = crop(a), crop(alpha), crop(lum)
        h, w = a.shape[:2]
    else:
        # Full product shot: zoom in by SCALE so the garment fills more of the
        # frame (thumbnails), by trimming empty ground off the sides. Never
        # trim into the garment: keep at least 40px of ground beside it.
        cols = np.where((alpha[..., 0] < 0.5).any(axis=0))[0]
        if cols.size:
            room = min(cols[0], w - 1 - cols[-1]) - 40
            x0 = int(max(0, min((w - round(w / SCALE)) // 2, room)))
            if x0:
                crop = lambda arr: arr[:, x0:w - x0]
                a, alpha, lum = crop(a), crop(alpha), crop(lum)
                h, w = a.shape[:2]
    # Place source, its ground alpha and its shading on the 4:5 canvas.
    nh = min(round(h * OUT_W / w), OUT_H)
    top = (OUT_H - nh) // 2
    def fit(arr):
        im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
        return np.asarray(im.resize((OUT_W, nh), Image.LANCZOS)).astype(float)
    src_c = fit(a)
    alpha_c = fit(alpha[..., 0] * 255)[..., None] / 255
    shade_c = fit(np.clip(lum, 0, 255))[..., None] / 255

    g = sweep(flat).copy()
    if not flat:
        # Soft contact shadow: the garment blocks the lamp just below itself.
        garment = np.zeros((OUT_H, OUT_W))
        garment[top:top + nh] = 1 - alpha_c[..., 0]
        s = ndimage.shift(ndimage.gaussian_filter(garment, 45), (30, 0), order=1)
        g *= (1 - SHADOW * s)[..., None]
    band = g[top:top + nh]
    # Shadow keeps its relative depth: pure white -> ground, grey -> darker.
    band[:] = alpha_c * band * (0.55 + 0.45 * shade_c) + (1 - alpha_c) * src_c
    return Image.fromarray(np.clip(g, 0, 255).astype(np.uint8))


def print_closeup(src: Path, flat=False) -> Image.Image:
    """Close-up on the front print, cut from a full front flat.

    Printify's own close-ups crop the slogan off, so this frames the whole
    print instead: about 62% of the width, never zoomed past 2x (sharpness).
    """
    im = convert(src, flat)
    a = np.asarray(im).astype(float)
    H, W = a.shape[:2]
    lum = a @ [0.299, 0.587, 0.114]
    mid = np.zeros_like(lum, bool)
    mid[:, int(W * .25):int(W * .75)] = True   # skip the sleeve wordmark
    ys, xs = np.where((lum > 170) & mid)
    if xs.size < 500:
        raise ValueError(f"{src.name}: no front print found")
    x0, x1 = np.percentile(xs, [1, 99])
    y0, y1 = np.percentile(ys, [1, 99])
    ww = max((x1 - x0) / 0.62, W / 2.0)
    wh = ww * H / W
    L = int(np.clip((x0 + x1) / 2 - ww / 2, 0, W - ww))
    T = int(np.clip((y0 + y1) / 2 - wh * 0.45, 0, H - wh))
    return im.crop((L, T, int(L + ww), int(T + wh))).resize((W, H), Image.LANCZOS)


if __name__ == "__main__":
    src_dir, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    flat = "--flat" in sys.argv
    for a in sys.argv:
        if a.startswith("--soft-shadow"):
            LUM_T = float(a.split("=")[1]) if "=" in a else 85
    out_dir.mkdir(parents=True, exist_ok=True)
    closeup = "--print-closeup" in sys.argv
    for f in sorted(src_dir.glob("*.jpg")):
        if closeup:
            name = f.stem + "-print.jpg"
            print_closeup(f, flat).save(out_dir / name, quality=92)
        else:
            name = f.name
            convert(f, flat).save(out_dir / name, quality=92)
        print(name)
