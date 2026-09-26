#!/usr/bin/env python3
"""Rebuild FÆBRIQ sticker typography at a consistent 1.25x cap-height hierarchy.

Approved 2026-09-26:
- Individual sticker line 1 cap height is 1.25x line 2 cap height.
- Use Bodoni Moda, near-black #0B0B0D, the six original Pride Circuit colours,
  and the FÆBRIQ wordmark.
- Preserve 2400 px-wide, transparent print masters at 300 DPI.
- Individual files are subsequently passed through add_connected_kiss_cut_path.py.
- The full-drop sheet uses these same raw lockups but remains rectangular.

This is the authoritative source for the current individual sticker type hierarchy.
It intentionally supersedes the stale Inter-only make_print_system.py for the
five sticker outputs listed below. It does not change apparel, tote, or cap art.
"""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from make_print_file import CIRCUIT, _draw_reinforced, _fit, font_path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/print-art/sticker-final-system-2026-08-27"
WIDTH = 2400
DPI = (300, 300)
NEAR_BLACK = (11, 11, 13)
TARGET_CAP_RATIO = 1.25
MARGIN = 108
BAR_RATIO_TO_WIDEST = 1.0326
BAR_HEIGHT_RATIO = 0.01615
STRIPE_FRACTION = 0.16333
GAP_FRACTION = 0.00369
WORDMARK_RATIO_TO_BAR = 0.1400
GAP_TOP_TO_BOTTOM = 0.20
GAP_BOTTOM_TO_BAR = 0.20
GAP_BAR_TO_WORDMARK = 1.10

DESIGNS = (
    ("404-straight-not-found-v3-sticker-light-2400.png", "404", "STRAIGHT NOT FOUND"),
    ("code-it-serve-it-sticker-light-2400.png", "CODE IT.", "SERVE IT."),
    ("deploying-identity-v2-sticker-light-2400.png", "DEPLOYING", "IDENTITY V2.0"),
    ("its-not-a-bug-its-me-sticker-light-2400.png", "IT'S NOT A BUG.", "IT'S ME."),
    ("please-hold-rebranding-identity-sticker-light-2400.png", "PLEASE HOLD", "I'M REBRANDING MY IDENTITY"),
)


def visible_width(font: ImageFont.FreeTypeFont, text: str) -> int:
    box = font.getbbox(text)
    return int(box[2] - box[0])


def visible_height(font: ImageFont.FreeTypeFont, text: str) -> int:
    box = font.getbbox(text)
    return int(box[3] - box[1])


def cap_height(font: ImageFont.FreeTypeFont) -> int:
    box = font.getbbox("H")
    return int(box[3] - box[1])


def font_for_cap(path: str, target_cap_height: float) -> ImageFont.FreeTypeFont:
    lo, hi = 4, 6000
    while lo < hi:
        mid = (lo + hi) // 2
        candidate = ImageFont.truetype(path, mid)
        if cap_height(candidate) < target_cap_height:
            lo = mid + 1
        else:
            hi = mid
    return ImageFont.truetype(path, lo)


def font_pair(path: str, line1: str, line2: str) -> tuple[ImageFont.FreeTypeFont, ImageFont.FreeTypeFont]:
    """Largest fitting pair whose actual Bodoni H cap heights target 1.25x."""
    usable = (WIDTH - 2 * MARGIN) / BAR_RATIO_TO_WIDEST
    best: tuple[ImageFont.FreeTypeFont, ImageFont.FreeTypeFont] | None = None
    best_ratio_error: float | None = None
    for bottom_size in range(4, 3000):
        bottom = ImageFont.truetype(path, bottom_size)
        target_top_cap = cap_height(bottom) * TARGET_CAP_RATIO
        top = font_for_cap(path, target_top_cap)
        ratio = cap_height(top) / cap_height(bottom)
        if max(visible_width(top, line1), visible_width(bottom, line2)) > usable:
            break
        ratio_error = abs(ratio - TARGET_CAP_RATIO)
        # Favour the largest line 2 that fits. Within it, take the closest ratio.
        if best is None or bottom_size > best[1].size or (bottom_size == best[1].size and ratio_error < (best_ratio_error or 999)):
            best, best_ratio_error = (top, bottom), ratio_error
    if best is None:
        raise RuntimeError(f"No valid 1.25x font pair for {line1!r} / {line2!r}")
    return best


def raw_lockup(font_path_: str, line1: str, line2: str) -> tuple[Image.Image, dict[str, float | int | str]]:
    top_font, bottom_font = font_pair(font_path_, line1, line2)
    top_cap, bottom_cap = cap_height(top_font), cap_height(bottom_font)
    widest = max(visible_width(top_font, line1), visible_width(bottom_font, line2))
    bar_width = int(round(widest * BAR_RATIO_TO_WIDEST))
    bar_height = max(1, int(round(bar_width * BAR_HEIGHT_RATIO)))
    mark_font = _fit(ImageFont, font_path_, "FÆBRIQ", bar_width * WORDMARK_RATIO_TO_BAR, "w")
    mark_cap = cap_height(mark_font)

    top_y = MARGIN
    bottom_y = top_y + visible_height(top_font, line1) + int(round(top_cap * GAP_TOP_TO_BOTTOM))
    bar_y = bottom_y + visible_height(bottom_font, line2) + int(round(top_cap * GAP_BOTTOM_TO_BAR))
    mark_y = bar_y + bar_height + int(round(mark_cap * GAP_BAR_TO_WORDMARK))
    height = mark_y + visible_height(mark_font, "FÆBRIQ") + MARGIN

    im = Image.new("RGBA", (WIDTH, height), (0, 0, 0, 0))
    centre_x = WIDTH / 2
    _draw_reinforced(im, centre_x, top_y, line1, top_font, NEAR_BLACK)
    _draw_reinforced(im, centre_x, bottom_y, line2, bottom_font, NEAR_BLACK)
    draw = ImageDraw.Draw(im)
    x0 = centre_x - bar_width / 2
    stripe_width, gap = bar_width * STRIPE_FRACTION, bar_width * GAP_FRACTION
    for index, colour in enumerate(CIRCUIT):
        left = round(x0 + index * (stripe_width + gap))
        right = round(left + stripe_width) - 1
        draw.rectangle((left, bar_y, right, bar_y + bar_height - 1), fill=colour)
    _draw_reinforced(im, centre_x, mark_y, "FÆBRIQ", mark_font, NEAR_BLACK)
    return im, {
        "line_1": line1,
        "line_2": line2,
        "top_font_px": top_font.size,
        "bottom_font_px": bottom_font.size,
        "top_cap_px": top_cap,
        "bottom_cap_px": bottom_cap,
        "top_to_bottom_cap_ratio": round(top_cap / bottom_cap, 4),
        "widest_text_px": widest,
        "bar_width_px": bar_width,
        "canvas_width_px": WIDTH,
        "canvas_height_px": height,
    }


def build_sheet(lockups: list[Image.Image]) -> Image.Image:
    """Retain the existing 8 x 12 in rectangular full-drop sheet layout."""
    sheet_width, sheet_height, margin = 2400, 3600, 120
    cell_width = (sheet_width - 3 * margin) // 2
    cell_height = (sheet_height - 4 * margin) // 3
    sheet = Image.new("RGBA", (sheet_width, sheet_height), (0, 0, 0, 0))
    placements = ((0, 0), (1, 0), (0, 1), (1, 1), (0.5, 2))
    for lockup, (column, row) in zip(lockups, placements):
        scale = min(cell_width / lockup.width, cell_height / lockup.height)
        resized = lockup.resize((round(lockup.width * scale), round(lockup.height * scale)), Image.Resampling.LANCZOS)
        x = round(margin + column * (cell_width + margin) + (cell_width - resized.width) / 2)
        y = round(margin + row * (cell_height + margin) + (cell_height - resized.height) / 2)
        sheet.alpha_composite(resized, (x, y))
    return sheet


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    bodoni = font_path("Bodoni Moda", None, "BodoniModa-Regular.ttf")
    metadata: list[dict[str, float | int | str]] = []
    raw_lockups: list[Image.Image] = []
    for filename, line1, line2 in DESIGNS:
        image, record = raw_lockup(bodoni, line1, line2)
        image.save(OUT / filename, "PNG", dpi=DPI)
        record["file"] = str((OUT / filename).relative_to(ROOT))
        metadata.append(record)
        raw_lockups.append(image)
        print(f"{filename}: {record['top_cap_px']}px / {record['bottom_cap_px']}px = {record['top_to_bottom_cap_ratio']}x")
    sheet = build_sheet(raw_lockups)
    sheet.save(ROOT / "assets/print-art/sticker-sheet-serif-2400x3600.png", "PNG", dpi=DPI)
    hierarchy = {
        "date": "2026-09-26",
        "font": "Bodoni Moda Regular",
        "ink": "#0B0B0D",
        "target_top_to_bottom_cap_ratio": TARGET_CAP_RATIO,
        "actual_lockups": metadata,
        "sheet": "Rectangular full-drop sheet regenerated from the same raw hierarchy lockups.",
    }
    (OUT / "hierarchy-1p25.json").write_text(json.dumps(hierarchy, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
