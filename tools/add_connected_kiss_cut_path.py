#!/usr/bin/env python3
"""Add one connected white contour-cut backing behind FÆBRIQ single sticker lockups.

Approved change, 2026-09-26:
- Keep every existing lettering pixel, Pride Circuit bar pixel, geometry, and DPI.
- Add a connected white silhouette behind each full lockup.
- Preserve transparent canvas outside that silhouette.
- Do not apply to sticker-sheet-serif-2400x3600.png: a sheet is intentionally rectangular.
"""
from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "assets/print-art/sticker-final-system-2026-08-27"
# Per-lockup values are the smallest elliptical expansion that creates exactly
# one connected component. At 300 DPI they produce a 0.19 to 0.25 inch white
# cut buffer before Printify scales the source into its selected sticker size.
FILES_AND_BUFFER_PX = {
    "404-straight-not-found-v3-sticker-light-2400.png": 56,
    "code-it-serve-it-sticker-light-2400.png": 76,
    "deploying-identity-v2-sticker-light-2400.png": 56,
    "its-not-a-bug-its-me-sticker-light-2400.png": 56,
    "please-hold-rebranding-identity-sticker-light-2400.png": 56,
}


def connected_components(mask: np.ndarray) -> int:
    return int(cv2.connectedComponents(mask, 8)[0] - 1)


def transform(path: Path, buffer_px: int) -> None:
    with Image.open(path) as src:
        dpi = src.info.get("dpi", (300, 300))
        art = src.convert("RGBA")
    rgba = np.asarray(art).copy()
    original = rgba.copy()
    alpha = original[:, :, 3]
    mask = (alpha > 0).astype(np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * buffer_px + 1, 2 * buffer_px + 1))
    backing_mask = cv2.dilate(mask, kernel)
    if connected_components(backing_mask) != 1:
        raise RuntimeError(f"cut path is not connected: {path.name}")

    # White vinyl silhouette. The transparent canvas outside remains untouched.
    out = np.zeros_like(original)
    out[backing_mask > 0] = (255, 255, 255, 255)
    # Restore every original non-transparent source pixel exactly above it.
    keep = alpha > 0
    out[keep] = original[keep]
    if not np.array_equal(out[keep], original[keep]):
        raise RuntimeError(f"source pixels changed: {path.name}")

    Image.fromarray(out, "RGBA").save(path, format="PNG", dpi=dpi, optimize=True)
    with Image.open(path) as check:
        check_rgba = np.asarray(check.convert("RGBA"))
    if check_rgba.shape != original.shape or not np.array_equal(check_rgba[keep], original[keep]):
        raise RuntimeError(f"saved output failed source-pixel validation: {path.name}")
    if connected_components((check_rgba[:, :, 3] > 0).astype(np.uint8)) != 1:
        raise RuntimeError(f"saved output is not one contour: {path.name}")
    print(f"{path.relative_to(ROOT)}\tbuffer_px={buffer_px}\tcomponents=1")


def main() -> None:
    for filename, buffer_px in FILES_AND_BUFFER_PX.items():
        transform(FOLDER / filename, buffer_px)


if __name__ == "__main__":
    main()
