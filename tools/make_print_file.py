#!/usr/bin/env python3
"""Generate print-ready FÆBRIQ tagline art: transparent PNG at DTG resolution.

Geometry and typography follow the founder-supplied reference lockup
("404 Straight Not Found - Sticker.png", 2026-08-20 handoff): Playfair Display
throughout — phrase, label, and FÆBRIQ kicker — over a thin, near-continuous
pride-circuit bar slightly wider than the phrase.

Colour stays on the settled tokens in `tokens/colors.css` (muted circuit set),
NOT the reference's pure pride-flag hex. Decision: the handoff governs type and
geometry, the tokens govern colour.

    python3 tools/make_print_file.py --line1 "STRAIGHT NOT" --line2 FOUND \
        --label 404 --out assets/print-art/404-straight-not-found-light-4500.png

The legacy 820x420 JPGs in assets/print-art/ are previews only — too small, and
their opaque #0D0D0D field prints as a dark box on the garment.
"""
import argparse
import os
import re
import sys
import urllib.request

# Settled brand tokens — tokens/colors.css
CIRCUIT = ["#E8272A", "#F47F20", "#F9D426", "#2AAA42", "#1D5BBE", "#7B3FAA"]
# label uses --fae-text-dim, which also matches the reference's #999999
INK_LIGHT = {"text": "#E8E8E8", "label": "#9A9A9A", "mark": "#C0C0C0"}
INK_DARK = {"text": "#0D0D0D", "label": "#9A9A9A", "mark": "#5F5F5F"}

# Lockup proportions measured from the reference, normalised to phrase-line-1
# width (L) with the origin at the top of the label.
SRC = dict(
    label_w=0.0985, label_y=0.0000,
    l1_w=1.0000, l1_y=0.0818,
    l2_w=0.4710, l2_y=0.2708,
    bar_w=1.0326, bar_y=0.4519, bar_h=0.01615,   # bar_h is a fraction of bar_w
    mark_w=0.1446, mark_y=0.5218,
    total_h=0.5592,
    stripe_frac=0.16333,   # stripe width as a fraction of bar width
    gap_frac=0.00369,      # gap width as a fraction of bar width
)
FONT_CSS = "https://fonts.googleapis.com/css?family={}"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".fontcache")


def font_path(family, weight, filename):
    """Fetch a Google Font TTF into the local cache (OFL; safe to redistribute)."""
    os.makedirs(CACHE, exist_ok=True)
    dest = os.path.join(CACHE, filename)
    if os.path.exists(dest):
        return dest
    q = family.replace(" ", "+") + (f":{weight}" if weight else "")
    req = urllib.request.Request(FONT_CSS.format(q), headers={"User-Agent": "Mozilla/4.0"})
    css = urllib.request.urlopen(req, timeout=30).read().decode()
    urls = re.findall(r"url\((https://[^)]+\.ttf)\)", css)
    if not urls:
        sys.exit(f"could not resolve a TTF for {family} {weight}")
    urllib.request.urlretrieve(urls[0], dest)
    return dest


def fit(ImageFont, path, text, target_w):
    """Binary-search the font size whose rendered width matches target_w."""
    lo, hi = 4.0, 6000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        f = ImageFont.truetype(path, max(1, int(round(mid))))
        lo, hi = (mid, hi) if f.getlength(text) < target_w else (lo, mid)
    return ImageFont.truetype(path, max(1, int(round(lo))))


def build(line1, line2, out, label=None, width=4500, margin_frac=0.045, ink="light"):
    from PIL import Image, ImageDraw, ImageFont

    serif = font_path("Playfair Display", None, "PlayfairDisplay-Regular.ttf")
    col = INK_LIGHT if ink == "light" else INK_DARK

    # The bar is the widest element, so it sets the usable width.
    L = width * (1 - 2 * margin_frac) / SRC["bar_w"]
    f_l1 = fit(ImageFont, serif, line1, SRC["l1_w"] * L)
    f_l2 = fit(ImageFont, serif, line2, SRC["l2_w"] * L)
    f_mark = fit(ImageFont, serif, "FÆBRIQ", SRC["mark_w"] * L)
    f_lab = fit(ImageFont, serif, label, SRC["label_w"] * L) if label else None

    pad = width * margin_frac
    top = pad if label else pad - SRC["l1_y"] * L
    height = int(round(SRC["total_h"] * L + 2 * pad - (0 if label else SRC["l1_y"] * L)))
    im = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx = width / 2

    def line(y_key, text, font, fill):
        bb = font.getbbox(text)
        d.text((cx - (bb[2] + bb[0]) / 2, top + SRC[y_key] * L - bb[1]), text,
               font=font, fill=fill)

    if label:
        line("label_y", label, f_lab, col["label"])
    line("l1_y", line1, f_l1, col["text"])
    line("l2_y", line2, f_l2, col["text"])

    # pride-circuit bar: thin, near-continuous, marginally wider than the phrase
    bar_w = SRC["bar_w"] * L
    sw, gap = SRC["stripe_frac"] * bar_w, SRC["gap_frac"] * bar_w
    bh = SRC["bar_h"] * bar_w
    bx, by = cx - bar_w / 2, top + SRC["bar_y"] * L
    for i, c in enumerate(CIRCUIT):
        x0 = bx + i * (sw + gap)
        d.rectangle([x0, by, x0 + sw, by + bh], fill=c)

    line("mark_y", "FÆBRIQ", f_mark, col["mark"])
    im.save(out, "PNG", dpi=(300, 300))
    return im.size


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--line1", required=True)
    p.add_argument("--line2", required=True)
    p.add_argument("--label", help="small serif label above the phrase, e.g. 404")
    p.add_argument("--out", required=True)
    p.add_argument("--width", type=int, default=4500)
    p.add_argument("--ink", choices=["light", "dark"], default="light",
                   help="light = for dark garments (default); dark = for light garments")
    a = p.parse_args()
    w, h = build(a.line1, a.line2, a.out, label=a.label, width=a.width, ink=a.ink)
    print(f"wrote {a.out}  {w}x{h}  RGBA 300dpi  ink={a.ink}")
