#!/usr/bin/env python3
"""Build smooth connected white contours for FÆBRIQ individual text stickers.

Approved production rule, 2026-09-26:
- Preserve the existing lettering, Pride Circuit bar, canvas dimensions, and DPI.
- Build one centered, near-symmetrical, solid-white organic contour around each lockup.
- Form the contour from softly overlapping rounded bands, not rectangles, letter outlines, or thin bridges.
- Keep transparency only outside the outer silhouette and retain no interior transparent voids.
- Do not apply to sticker-sheet-serif-2400x3600.png: that product stays rectangular.
"""
from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "assets/print-art/sticker-final-system-2026-08-27"
FILES = (
    "404-straight-not-found-v3-sticker-light-2400.png",
    "code-it-serve-it-sticker-light-2400.png",
    "deploying-identity-v2-sticker-light-2400.png",
    "its-not-a-bug-its-me-sticker-light-2400.png",
    "please-hold-rebranding-identity-sticker-light-2400.png",
)
HORIZONTAL_PAD = 56
VERTICAL_PAD = 64
CORNER_RADIUS = 96


def connected_components(mask: np.ndarray) -> int:
    return int(cv2.connectedComponents(mask, 8)[0] - 1)


def bands(alpha: np.ndarray) -> list[tuple[int, int, int, int]]:
    """Return the four text or bar bands: line 1, line 2, bar, wordmark."""
    active = (alpha > 0).any(axis=1)
    y_runs: list[tuple[int, int]] = []
    start: int | None = None
    for y, value in enumerate(np.append(active, False)):
        if value and start is None:
            start = y
        elif not value and start is not None:
            y_runs.append((start, y - 1))
            start = None
    result: list[tuple[int, int, int, int]] = []
    for top, bottom in y_runs:
        xs = np.where((alpha[top : bottom + 1] > 0).any(axis=0))[0]
        if len(xs):
            result.append((int(xs.min()), top, int(xs.max()), bottom))
    if len(result) != 4:
        raise RuntimeError(f"expected four lockup bands, found {len(result)}")
    return result


def rounded_band_rect(band: tuple[int, int, int, int], width: int, height: int) -> tuple[int, int, int, int]:
    left, top, right, bottom = band
    centre_x = width // 2
    half_width = max(centre_x - left, right - centre_x) + HORIZONTAL_PAD
    return (
        max(0, centre_x - half_width),
        max(0, top - VERTICAL_PAD),
        min(width - 1, centre_x + half_width),
        min(height - 1, bottom + VERTICAL_PAD),
    )


def transform(path: Path) -> None:
    with Image.open(path) as src:
        dpi = src.info.get("dpi", (300, 300))
        art = src.convert("RGBA")
    original = np.asarray(art).copy()
    height, width = original.shape[:2]
    alpha = original[:, :, 3]
    rects = [rounded_band_rect(band, width, height) for band in bands(alpha)]

    # With a 64 px vertical offset every adjacent band overlaps. This creates
    # one gentle, cloud-like carrier without a skinny bridge or square card.
    backing = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(backing)
    for rect in rects:
        draw.rounded_rectangle(rect, radius=CORNER_RADIUS, fill=255)
    backing_mask = (np.asarray(backing) > 0).astype(np.uint8)
    if connected_components(backing_mask) != 1:
        raise RuntimeError(f"cut path is not connected: {path.name}")

    out = np.zeros_like(original)
    out[backing_mask > 0] = (255, 255, 255, 255)
    keep = alpha > 0
    out[keep] = original[keep]
    if not np.array_equal(out[keep], original[keep]):
        raise RuntimeError(f"source pixels changed: {path.name}")
    Image.fromarray(out, "RGBA").save(path, format="PNG", dpi=dpi, optimize=True)

    with Image.open(path) as check:
        check_rgba = np.asarray(check.convert("RGBA"))
    check_mask = (check_rgba[:, :, 3] > 0).astype(np.uint8)
    if check_rgba.shape != original.shape or not np.array_equal(check_rgba[keep], original[keep]):
        raise RuntimeError(f"saved output failed source-pixel validation: {path.name}")
    if connected_components(check_mask) != 1:
        raise RuntimeError(f"saved output is not one contour: {path.name}")
    exterior = check_mask.copy()
    flood_mask = np.zeros((height + 2, width + 2), np.uint8)
    cv2.floodFill(exterior, flood_mask, (0, 0), 1)
    if np.count_nonzero(exterior == 0):
        raise RuntimeError(f"saved output has interior holes: {path.name}")
    print(f"{path.relative_to(ROOT)}\tbands=4\tcomponents=1\tvoids=0")


def main() -> None:
    for filename in FILES:
        transform(FOLDER / filename)


if __name__ == "__main__":
    main()
