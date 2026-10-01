"""Turn Printify white-background mockups into charcoal-ground product shots.

The white studio ground becomes #0d0d0d (the tone of the existing "-dark"
product images), the soft drop shadow is kept as a slightly darker tone,
and the frame is padded to 4:5 (2048x2560) per IMAGERY_SPEC_2026-09-23.md.

Usage: python3 tools/mockup_to_charcoal.py IN_DIR OUT_DIR
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

GROUND = np.array([13, 13, 13], dtype=float)
OUT_W, OUT_H = 2048, 2560


def convert(src: Path) -> Image.Image:
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

    # Shadow keeps its relative depth: pure white -> GROUND, grey -> darker.
    shade = np.clip(lum / 255.0, 0, 1)[..., None]
    ground_rgb = GROUND * (0.55 + 0.45 * shade)
    out = alpha * ground_rgb + (1 - alpha) * a
    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

    canvas = Image.new("RGB", (OUT_W, OUT_H), tuple(int(c) for c in GROUND))
    img = img.resize((OUT_W, round(h * OUT_W / w)), Image.LANCZOS)
    canvas.paste(img, (0, (OUT_H - img.height) // 2))
    return canvas


if __name__ == "__main__":
    src_dir, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in sorted(src_dir.glob("*.jpg")):
        convert(f).save(out_dir / f.name, quality=90)
        print(f.name)
