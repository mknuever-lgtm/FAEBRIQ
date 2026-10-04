"""Turn Printify white-background mockups into charcoal-ground product shots.

The white studio ground becomes a charcoal studio sweep (Maurice's pick,
2026-10-04, option 3): #19191B at the corners rising to about #2E2E30 in an
oval glow behind the product, so a black garment keeps its silhouette and the
edges melt into the page. The soft drop shadow is kept as a darker tone, and
the frame is 4:5 (2048x2560) per IMAGERY_SPEC_2026-09-23.md.
--flat restores the old flat #0d0d0d ground.

Usage: python3 tools/mockup_to_charcoal.py IN_DIR OUT_DIR [--flat]
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

GROUND = np.array([13, 13, 13], dtype=float)
EDGE = np.array([25, 25, 27], dtype=float)
CENTER = np.array([46, 46, 48], dtype=float)
OUT_W, OUT_H = 2048, 2560


def sweep(flat=False):
    """Canvas-sized ground: flat #0d0d0d, or the oval charcoal glow."""
    if flat:
        return np.broadcast_to(GROUND, (OUT_H, OUT_W, 3)).astype(float)
    y, x = np.mgrid[0:OUT_H, 0:OUT_W].astype(float)
    r = np.hypot((x - OUT_W / 2) / (0.62 * OUT_W), (y - OUT_H * 0.48) / (0.55 * OUT_H))
    t = np.clip(1 - r ** 2, 0, 1)[..., None]
    g = EDGE + (CENTER - EDGE) * t
    # Fine grain so the gradient does not band once Shopify recompresses it.
    g += np.random.default_rng(7).normal(0, 0.8, (OUT_H, OUT_W, 1))
    return g


def convert(src: Path, flat=False) -> Image.Image:
    a = np.asarray(Image.open(src).convert("RGB")).astype(float)
    h, w, _ = a.shape
    lum = a @ [0.299, 0.587, 0.114]
    sat = a.max(2) - a.min(2)

    # Candidate ground: light and unsaturated (white plus its grey shadow).
    cand = (lum > 150) & (sat < 30)
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
            keep[i] = big or edge_white or pocket
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
    band = g[top:top + nh]
    # Shadow keeps its relative depth: pure white -> ground, grey -> darker.
    band[:] = alpha_c * band * (0.55 + 0.45 * shade_c) + (1 - alpha_c) * src_c
    return Image.fromarray(np.clip(g, 0, 255).astype(np.uint8))


if __name__ == "__main__":
    src_dir, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    flat = "--flat" in sys.argv
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in sorted(src_dir.glob("*.jpg")):
        convert(f, flat).save(out_dir / f.name, quality=92)
        print(f.name)
