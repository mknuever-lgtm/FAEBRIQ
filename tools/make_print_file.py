#!/usr/bin/env python3
"""Generate print-ready FÆBRIQ tagline art: transparent PNG at DTG resolution.

The tagline art in `assets/print-art/` is 820x420 JPG with a solid #0D0D0D
background — fine as a preview, unusable as a Printify print file (too small, and
the opaque background prints as a dark box on the garment). Those files also
still carry the retired pure pride-flag hex rather than the settled muted
circuit palette in `tokens/colors.css`.

This rebuilds the lockup — optional label / two-line phrase / pride-circuit bar /
wordmark — from the live tokens, at 4500px with a real alpha channel.

    python3 tools/make_print_file.py --line1 "Straight Not" --line2 Found \
        --label 404 --out assets/print-art/404-straight-not-found-light-4500.png

Proportions are measured from `assets/phrase-404.png`, which is the one asset
already using the correct palette.
"""
import argparse
import os
import re
import sys
import urllib.request

# Settled brand tokens — tokens/colors.css
CIRCUIT = ["#E8272A", "#F47F20", "#F9D426", "#2AAA42", "#1D5BBE", "#7B3FAA"]
INK_LIGHT = {"text": "#E8E8E8", "faint": "#5F5F5F", "mark": "#C0C0C0"}
INK_DARK = {"text": "#0D0D0D", "faint": "#8A8A8A", "mark": "#5F5F5F"}
TRACK = 0.24  # mono label tracking, em

# Lockup proportions measured from assets/phrase-404.png (1080px canvas)
SRC = dict(
    label_w=78, l1_w=477, l2_w=246, bar_w=420, bar_h=9, mark_w=111,
    label_y=0, l1_y=69, l2_y=171, bar_y=286, mark_y=329, total_h=347,
    stripe_w=61.5, gap=10,
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
    urllib.request.urlretrieve(urls[-1], dest)
    return dest


def tracked_width(font, text, track_px):
    return sum(font.getlength(c) for c in text) + track_px * (len(text) - 1)


def fit(ImageFont, path, text, target_w, tracked=False):
    """Binary-search the font size whose rendered width matches target_w."""
    lo, hi = 4.0, 4000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        f = ImageFont.truetype(path, max(1, int(round(mid))))
        w = tracked_width(f, text, TRACK * mid) if tracked else f.getlength(text)
        lo, hi = (mid, hi) if w < target_w else (lo, mid)
    size = max(1, int(round(lo)))
    return ImageFont.truetype(path, size), size


def build(line1, line2, out, label=None, width=4500, margin_frac=0.045, ink="light"):
    from PIL import Image, ImageDraw, ImageFont

    serif = font_path("Instrument Serif", None, "InstrumentSerif-Regular.ttf")
    mono = font_path("JetBrains Mono", "500", "JetBrainsMono-Medium.ttf")
    col = INK_LIGHT if ink == "light" else INK_DARK

    s = width * (1 - 2 * margin_frac) / SRC["l1_w"]  # source -> output scale
    f_l1, _ = fit(ImageFont, serif, line1, SRC["l1_w"] * s)
    f_l2, _ = fit(ImageFont, serif, line2, SRC["l2_w"] * s)
    f_mark, s_mark = fit(ImageFont, mono, "FÆBRIQ", SRC["mark_w"] * s, tracked=True)
    f_lab, s_lab = fit(ImageFont, mono, label, SRC["label_w"] * s, tracked=True) if label else (None, 0)

    pad = width * margin_frac
    top = pad if label else pad - SRC["l1_y"] * s
    height = int(round(SRC["total_h"] * s + 2 * pad - (0 if label else SRC["l1_y"] * s)))
    im = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx = width / 2

    def plain(y, text, font, fill):
        bb = font.getbbox(text)
        d.text((cx - (bb[2] + bb[0]) / 2, top + y * s - bb[1]), text, font=font, fill=fill)

    def tracked(y, text, font, size, fill):
        x = cx - tracked_width(font, text, TRACK * size) / 2
        yy = top + y * s - font.getbbox(text)[1]
        for ch in text:
            d.text((x, yy), ch, font=font, fill=fill)
            x += font.getlength(ch) + TRACK * size

    if label:
        tracked(SRC["label_y"], label, f_lab, s_lab, col["faint"])
    plain(SRC["l1_y"], line1, f_l1, col["text"])
    plain(SRC["l2_y"], line2, f_l2, col["text"])

    sw, gap = SRC["stripe_w"] * s, SRC["gap"] * s
    bx = cx - (6 * sw + 5 * gap) / 2
    by, bh = top + SRC["bar_y"] * s, SRC["bar_h"] * s
    for i, c in enumerate(CIRCUIT):
        d.rectangle([bx + i * (sw + gap), by, bx + i * (sw + gap) + sw, by + bh], fill=c)

    tracked(SRC["mark_y"], "FÆBRIQ", f_mark, s_mark, col["mark"])
    im.save(out, "PNG", dpi=(300, 300))
    return im.size


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--line1", required=True)
    p.add_argument("--line2", required=True)
    p.add_argument("--label", help="small mono label above the phrase, e.g. 404")
    p.add_argument("--out", required=True)
    p.add_argument("--width", type=int, default=4500)
    p.add_argument("--ink", choices=["light", "dark"], default="light",
                   help="light = for dark garments (default); dark = for light garments")
    a = p.parse_args()
    w, h = build(a.line1, a.line2, a.out, label=a.label, width=a.width, ink=a.ink)
    print(f"wrote {a.out}  {w}x{h}  RGBA 300dpi  ink={a.ink}")
