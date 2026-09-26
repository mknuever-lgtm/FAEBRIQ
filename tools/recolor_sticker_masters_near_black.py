#!/usr/bin/env python3
"""Recolor FÆBRIQ locked sticker lettering for white vinyl without moving pixels.

Approved change, 2026-09-26:
- White/neutral lettering and FÆBRIQ wordmarks become #0B0B0D.
- The six-color Pride Circuit bar, alpha channel, dimensions, DPI, and geometry stay unchanged.
- Standard white vinyl remains the physical background; it is not printed into the PNG.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
NEAR_BLACK = (11, 11, 13)
FILES = [
    ROOT / "assets/print-art/sticker-final-system-2026-08-27/404-straight-not-found-v3-sticker-light-2400.png",
    ROOT / "assets/print-art/sticker-final-system-2026-08-27/code-it-serve-it-sticker-light-2400.png",
    ROOT / "assets/print-art/sticker-final-system-2026-08-27/deploying-identity-v2-sticker-light-2400.png",
    ROOT / "assets/print-art/sticker-final-system-2026-08-27/its-not-a-bug-its-me-sticker-light-2400.png",
    ROOT / "assets/print-art/sticker-final-system-2026-08-27/please-hold-rebranding-identity-sticker-light-2400.png",
    ROOT / "assets/print-art/sticker-sheet-serif-2400x3600.png",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_neutral_light(r: int, g: int, b: int, a: int) -> bool:
    """Match only anti-aliased white or neutral lettering, never the rainbow bar."""
    return a > 0 and min(r, g, b) >= 96 and max(r, g, b) - min(r, g, b) <= 5


def recolor(path: Path) -> tuple[int, str, str]:
    before = sha256(path)
    with Image.open(path) as src:
        dpi = src.info.get("dpi", (300, 300))
        original = src.convert("RGBA")
    original_alpha = original.getchannel("A").tobytes()
    pixels = list(original.getdata())
    transformed = [
        (*NEAR_BLACK, a) if is_neutral_light(r, g, b, a) else (r, g, b, a)
        for r, g, b, a in pixels
    ]
    changed = sum(a != b for a, b in zip(pixels, transformed))
    output = Image.new("RGBA", original.size)
    output.putdata(transformed)
    if output.getchannel("A").tobytes() != original_alpha:
        raise RuntimeError(f"alpha changed for {path}")
    output.save(path, format="PNG", dpi=dpi, optimize=True)
    with Image.open(path) as check:
        if check.size != original.size or check.mode != "RGBA":
            raise RuntimeError(f"geometry changed for {path}")
        if check.getchannel("A").tobytes() != original_alpha:
            raise RuntimeError(f"alpha changed after save for {path}")
    return changed, before, sha256(path)


def main() -> None:
    for path in FILES:
        changed, before, after = recolor(path)
        print(f"{path.relative_to(ROOT)}\tchanged={changed}\tbefore={before}\tafter={after}")


if __name__ == "__main__":
    main()
