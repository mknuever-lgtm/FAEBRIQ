#!/usr/bin/env python3
"""Generate print-ready FÆBRIQ tagline art: transparent PNG at DTG resolution.

Lockup rules, from the founder handoff (2026-08-20) and confirmed against the
apparel print files in it:

  apparel  ->  phrase + pride-circuit bar.   NO FÆBRIQ wordmark.
  sticker  ->  phrase + bar + FÆBRIQ wordmark.

The wordmark is a sticker/cap element only — the apparel print files in the
handoff ("Code It. Serve It. - White (Print)", "Off The Clock...") carry no
wordmark at all.

Bar geometry follows the *sticker* model deliberately: thin (height ~1.6% of bar
width) with hairline gaps. The handoff's apparel files use a bar ~3x thicker
(5.0%) with no gaps; the founder's call is that this reads too heavy, so the thin
bar is standard everywhere now.

Type is Bodoni Moda. Colour stays on the settled tokens in `tokens/colors.css`
(muted circuit set), NOT the handoff's pure pride-flag hex — the handoff governs
type and geometry, the tokens govern colour.

    python3 tools/make_print_file.py --line1 "STRAIGHT NOT" --line2 FOUND \
        --label "ERROR 404" --product apparel \
        --out assets/print-art/404-straight-not-found-light-4500.png

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

# Lockup proportions measured from the reference sticker, normalised to
# phrase-line-1 width (L), origin at the top of the label.
SRC = dict(
    label_h=0.0429, label_y=0.0000,
    l1_w=1.0000, l1_y=0.0818,
    l2_w=0.4710, l2_y=0.2708,
    bar_w=1.0326, bar_y=0.4519, bar_h=0.01615,   # bar_h is a fraction of bar_w
    mark_w=0.1446, mark_y=0.5218,
    stripe_frac=0.16333,   # stripe width as a fraction of bar width
    gap_frac=0.00369,      # gap width as a fraction of bar width
)

# Printify's own published DTG guideline: 2pt minimum line thickness.
# https://help.printify.com/hc/en-us/articles/43890557264529
MIN_STROKE_MM = 0.706
OUTPUT_DPI = 300  # fixed regardless of --width; do not scale DILATE_RADIUS_PX
                  # against --width, only against a DPI change.

# Bodoni Moda is a Didone: at any size that fits a garment print, its serif
# *feet* run thinner than its round-letter hairlines (measured 2026-08-20 on
# the actual rendered glyphs, not a proxy). Scaling the whole design up can't
# fix this — reaching MIN_STROKE_MM by scale alone would require a ~42in wide
# print for "STRAIGHT NOT" at this lockup's proportions. The fix is a small
# uniform ink-growth pass on each glyph's alpha mask (see _reinforce below):
# it thickens a 3px hairline by the same 4px that a 40px stem barely notices,
# so it targets exactly the failure mode without visibly changing the type.
# Verified: 3px (0.254mm) hairline -> 11px (0.931mm) after MaxFilter(9),
# comfortably above the 0.706mm minimum; visual diff at design scale is
# negligible (see scratchpad/dilation_compare.png, 2026-08-20).
DILATE_RADIUS_PX = 4

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


def _fit(ImageFont, path, text, target, by):
    """Binary-search the font size whose rendered width/height matches target."""
    lo, hi = 4.0, 6000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        f = ImageFont.truetype(path, max(1, int(round(mid))))
        bb = f.getbbox(text)
        got = f.getlength(text) if by == "w" else (bb[3] - bb[1])
        lo, hi = (mid, hi) if got < target else (lo, mid)
    return ImageFont.truetype(path, max(1, int(round(lo))))


def _draw_reinforced(canvas, cx, y, text, font, fill):
    """Draw text as a standalone alpha mask, dilate it by DILATE_RADIUS_PX so no
    stroke (in particular a Didone serif foot) falls under MIN_STROKE_MM, then
    composite it at constant fill colour. See DILATE_RADIUS_PX docstring."""
    from PIL import Image, ImageDraw, ImageFilter

    bb = font.getbbox(text)
    pad = DILATE_RADIUS_PX + 2
    w, h = bb[2] - bb[0] + 2 * pad, bb[3] - bb[1] + 2 * pad
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).text((pad - bb[0], pad - bb[1]), text, font=font, fill=255)
    mask = mask.filter(ImageFilter.MaxFilter(2 * DILATE_RADIUS_PX + 1))

    layer = Image.new("RGBA", mask.size, (*fill, 255))
    layer.putalpha(mask)
    canvas.alpha_composite(layer, (int(round(cx - w / 2)), int(round(y - pad))))


# Gaps between line1->line2 and line2->bar, measured off the approved 404
# reference ("STRAIGHT NOT" / "FOUND") as a multiple of the PRECEDING line's
# own fitted font size — not a fixed fraction of canvas width like the old
# l1_y/l2_y/bar_y constants were. A fixed-fraction gap looks wildly different
# depending on word count, since _fit shrinks or grows the font to hit a
# target width: "CODE IT." renders much bigger than "OFF THE CLOCK." at the
# same width fraction, so the same absolute gap reads as cramped on one and
# oversized on the other. Scaling the gap by the actual rendered font size
# keeps the visual rhythm constant across every tagline automatically —
# derived once from make_print_file.py's own font-fit output, not eyeballed.
GAP_L1_L2_OF_L1_SIZE = 1.4668
GAP_L2_BAR_OF_L2_SIZE = 1.3758


def build(line1, line2, out, label=None, width=4500, margin_frac=0.045,
          ink="light", product="apparel", l2_y=None):
    from PIL import Image, ImageFont

    serif = font_path("Bodoni Moda", None, "BodoniModa-Regular.ttf")
    ink_hex = INK_LIGHT if ink == "light" else INK_DARK
    col = {k: tuple(int(v.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)) for k, v in ink_hex.items()}
    wordmark = product == "sticker"
    src = dict(SRC)

    # The bar is the widest element, so it sets the usable width.
    L = width * (1 - 2 * margin_frac) / src["bar_w"]
    f_l1 = _fit(ImageFont, serif, line1, src["l1_w"] * L, "w")
    f_l2 = _fit(ImageFont, serif, line2, src["l2_w"] * L, "w")
    # Label is fitted by cap height, not width, so it stays a consistent size
    # regardless of how long the label text is ("404" vs "ERROR 404").
    f_lab = _fit(ImageFont, serif, label, src["label_h"] * L, "h") if label else None
    f_mark = _fit(ImageFont, serif, "FÆBRIQ", src["mark_w"] * L, "w") if wordmark else None

    # l1_y is a fixed anchor (unaffected by text length); l2_y and bar_y are
    # derived from the actual rendered font sizes so spacing self-adjusts per
    # tagline. --l2-y still allows a manual override of the line1->line2 gap
    # specifically, but bar_y always follows line2's own size from there.
    src["l2_y"] = l2_y if l2_y is not None else src["l1_y"] + GAP_L1_L2_OF_L1_SIZE * f_l1.size / L
    src["bar_y"] = src["l2_y"] + GAP_L2_BAR_OF_L2_SIZE * f_l2.size / L
    src["mark_y"] = src["bar_y"] + (SRC["mark_y"] - SRC["bar_y"])

    bar_h = src["bar_h"] * src["bar_w"] * L
    content_h = (src["mark_y"] * L + f_mark.getbbox("FÆBRIQ")[3] - f_mark.getbbox("FÆBRIQ")[1]
                 if wordmark else src["bar_y"] * L + bar_h)
    pad = width * margin_frac
    top = pad if label else pad - src["l1_y"] * L
    height = int(round(content_h + 2 * pad - (0 if label else src["l1_y"] * L)))
    im = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    cx = width / 2

    def line(y_key, text, font, fill):
        _draw_reinforced(im, cx, top + src[y_key] * L, text, font, fill)

    if label:
        line("label_y", label, f_lab, col["label"])
    line("l1_y", line1, f_l1, col["text"])
    line("l2_y", line2, f_l2, col["text"])

    # pride-circuit bar: thin, near-continuous, marginally wider than the phrase.
    # A solid rectangle at 300dpi is always far above MIN_STROKE_MM (~5.7mm
    # tall even at this "thin" spec), so it needs no reinforcement pass.
    from PIL import ImageDraw
    d = ImageDraw.Draw(im)
    bar_w = src["bar_w"] * L
    sw, gap = src["stripe_frac"] * bar_w, src["gap_frac"] * bar_w
    bx, by = cx - bar_w / 2, top + src["bar_y"] * L
    for i, c in enumerate(CIRCUIT):
        x0 = bx + i * (sw + gap)
        d.rectangle([x0, by, x0 + sw, by + bar_h], fill=c)

    if wordmark:
        line("mark_y", "FÆBRIQ", f_mark, col["mark"])

    im.save(out, "PNG", dpi=(300, 300))
    return im.size


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--line1", required=True)
    p.add_argument("--line2", required=True)
    p.add_argument("--label", help='small serif label above the phrase, e.g. "ERROR 404"')
    p.add_argument("--out", required=True)
    p.add_argument("--width", type=int, default=4500)
    p.add_argument("--product", choices=["apparel", "sticker"], default="apparel",
                   help="apparel omits the FÆBRIQ wordmark; sticker includes it")
    p.add_argument("--ink", choices=["light", "dark"], default="light",
                   help="light = for dark garments (default); dark = for light garments")
    p.add_argument("--l2-y", type=float, default=None,
                   help="manual override for line-2's vertical position (fraction of L). "
                        "By default this is computed automatically from line-1's rendered "
                        "font size so spacing self-adjusts per tagline — only pass this to "
                        "force a specific position.")
    a = p.parse_args()
    w, h = build(a.line1, a.line2, a.out, label=a.label, width=a.width,
                 ink=a.ink, product=a.product, l2_y=a.l2_y)
    print(f"wrote {a.out}  {w}x{h}  RGBA 300dpi  ink={a.ink}  product={a.product}")
