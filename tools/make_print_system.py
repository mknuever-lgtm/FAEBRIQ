"""FÆBRIQ print system, 2026/09/25. One lockup for every product.

Maurice's rules:
  - Inter SemiBold on every design.
  - Line 2 is 55 to 90% of line 1's font size, judged per design.
  - Rainbow stripe: six flat blocks, 1.35x the widest text line.
  - FÆBRIQ wordmark under the stripe on stickers and the tote only.
  - Tees, hoodie, crewneck: no wordmark in the chest print; the FÆBRIQ
    logo (wordmark over a 1.35x stripe, same as the cap) goes on the sleeve.

    python3 tools/make_print_system.py
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_print_file import CIRCUIT, INK_LIGHT, font_path  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "print-art", "system-2026-09-25")

STRIPE_RATIO = 1.35   # stripe width / widest text line
# Line 2 font size / line 1 font size is set per design in DESIGNS, judged
# by eye within 0.55 to 0.90 (Maurice, 2026/09/25).
# Stripe height follows the type, not the stripe width, so the bar reads the
# same weight under big and small type. Clamped to a sane band of the width.
STRIPE_H = 0.14       # stripe height / line 1 cap height
STRIPE_H_MIN, STRIPE_H_MAX = 0.013, 0.028   # of stripe width
TRACK = -0.02         # letter spacing, x font size (editorial tightening)
# Sticker-only line 2 overrides where the apparel ratio prints too small at
# sticker size.
STICKER_L2 = {"please-hold-rebranding-identity": 0.62}
MARK_W = 0.20         # wordmark width / stripe width
# Vertical gaps, as a multiple of the cap height of the element above.
GAP_L1_L2 = 0.55
GAP_L2_BAR = 0.60
GAP_BAR_MARK = 0.75   # x the wordmark's own cap height
MARGIN = 0.045        # canvas margin / canvas width

DESIGNS = {
    # 404 stays the hero: a lower ratio grows the 404 against the fixed stripe.
    "404-straight-not-found": ("404", "STRAIGHT NOT FOUND", 0.55),
    "code-it-serve-it": ("CODE IT.", "SERVE IT.", 0.85),
    "off-the-clock-still-iconic": ("OFF THE CLOCK.", "STILL ICONIC.", 0.72),
    "deploying-identity-v2": ("DEPLOYING", "IDENTITY V2.0", 0.75),
    "its-not-a-bug-its-me": ("IT’S NOT A BUG.", "IT’S ME.", 0.80),
    "please-hold-rebranding-identity": ("PLEASE HOLD,", "I’M REBRANDING MY IDENTITY", 0.58),
}
SHEET = ["404-straight-not-found", "its-not-a-bug-its-me", "code-it-serve-it",
         "please-hold-rebranding-identity", "deploying-identity-v2"]

INTER = font_path("Inter", "600", "Inter-SemiBold.ttf")
WHITE = tuple(int(INK_LIGHT["text"][i:i + 2], 16) for i in (1, 3, 5))


def font(size):
    return ImageFont.truetype(INTER, max(1, int(round(size))))


def cap_h(f):
    b = f.getbbox("H", anchor="ls")
    return b[3] - b[1]


def line_mask(f, text):
    """Tracked line as an L mask cropped to its ink, plus the baseline's y
    offset inside the mask. Glyph by glyph so TRACK applies; measuring the
    real ink (not font.getbbox, which pads to the advance) keeps the 1.35x
    stripe exact on lines ending in a period or comma."""
    track = TRACK * f.size
    xs, x = [], 0.0
    for ch in text:
        xs.append(x)
        x += f.getlength(ch) + track
    asc, desc = f.getmetrics()
    m = Image.new("L", (int(x + f.size) + 8, asc + desc + 8), 0)
    d = ImageDraw.Draw(m)
    for ch, cx in zip(text, xs):
        d.text((4 + cx, 4 + asc), ch, font=f, anchor="ls", fill=255)
    box = m.getbbox()
    return m.crop(box), 4 + asc - box[1]


def ink_w(f, text):
    return line_mask(f, text)[0].width


def layout(lines, wordmark, s, l2):
    """Measure every element at line-1 font size s. Returns rows and stripe width."""
    fonts = [font(s)] + ([font(s * l2)] if len(lines) > 1 else [])
    widest = max(ink_w(f, t) for f, t in zip(fonts, lines))
    sw = widest * STRIPE_RATIO
    fm = None
    if wordmark:
        fm = font(s)  # refit to MARK_W of the stripe width
        fm = font(s * (MARK_W * sw) / ink_w(fm, "FÆBRIQ"))
    return fonts, fm, sw


def lockup(lines, wordmark, width, l2=None):
    """Transparent RGBA lockup whose stripe spans the canvas minus margins."""
    target = width * (1 - 2 * MARGIN)
    fonts, fm, sw = layout(lines, wordmark, 1000, l2)
    s = 1000 * target / sw
    fonts, fm, sw = layout(lines, wordmark, s, l2)

    pad = width * MARGIN
    y = pad
    rows = []  # (text, font, baseline)
    for i, (f, t) in enumerate(zip(fonts, lines)):
        y += cap_h(f)
        rows.append((t, f, y))
        # Descenders (Q, comma) sit below the baseline; gaps are measured
        # from the baseline so every design keeps the same rhythm.
        y += (GAP_L1_L2 if i < len(lines) - 1 else GAP_L2_BAR) * cap_h(f)
    bar_h = round(min(max(STRIPE_H * cap_h(fonts[0]), STRIPE_H_MIN * sw), STRIPE_H_MAX * sw))
    bar_y = y
    y += bar_h
    if fm:
        y += GAP_BAR_MARK * cap_h(fm) + cap_h(fm)
        rows.append(("FÆBRIQ", fm, y))
    last = line_mask(rows[-1][1], rows[-1][0])
    bottom = y + max(0, last[0].height - last[1])
    H = int(round(bottom + pad))

    im = Image.new("RGBA", (width, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx = width / 2
    for t, f, base in rows:
        m, base_off = line_mask(f, t)
        ink = Image.new("RGBA", m.size, WHITE + (255,))
        ink.putalpha(m)
        im.alpha_composite(ink, (int(round(cx - m.width / 2)), int(round(base - base_off))))
    x0, seg = cx - sw / 2, sw / 6
    for i, c in enumerate(CIRCUIT):
        d.rectangle([round(x0 + i * seg), round(bar_y), round(x0 + (i + 1) * seg) - 1,
                     round(bar_y + bar_h) - 1], fill=c)
    return im, dict(line1_px=fonts[0].size, line2_px=fonts[1].size if len(fonts) > 1 else None,
                    stripe_over_widest=round(sw / max(ink_w(f, t) for f, t in zip(fonts, lines)), 3))


def save(im, name, meta, product, text, manifest):
    path = os.path.join(OUT, name)
    im.save(path, "PNG", dpi=(300, 300))
    manifest.append(dict(file=os.path.relpath(path, ROOT), product=product, text=text,
                         size=list(im.size), **meta))
    return im


def sticker_sheet(stickers):
    """8 x 12 in at 300 dpi: 2 columns, the fifth design centered on the last row."""
    W, H, m = 2400, 3600, 120
    cw = (W - 3 * m) // 2
    sheet = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cells = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 2)]
    rh = (H - 4 * m) // 3
    for key, (c, r) in zip(SHEET, cells):
        im = stickers[key]
        k = min(cw / im.width, rh / im.height)
        im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
        x = int(m + c * (cw + m) + (cw - im.width) / 2)
        y = int(m + r * (rh + m) + (rh - im.height) / 2)
        sheet.alpha_composite(im, (x, y))
    return sheet


def contact(entries):
    bg = (15, 14, 12)
    thumbs = []
    for im in entries:
        k = 900 / im.width
        thumbs.append(im.resize((900, max(1, int(im.height * k))), Image.LANCZOS))
    cols, gap = 3, 80
    rows = [thumbs[i:i + cols] for i in range(0, len(thumbs), cols)]
    H = gap + sum(max(t.height for t in r) + gap for r in rows)
    sheet = Image.new("RGB", (cols * 900 + (cols + 1) * gap, H), bg)
    y = gap
    for r in rows:
        for i, t in enumerate(r):
            sheet.paste(t, (gap + i * (900 + gap), y), t)
        y += max(t.height for t in r) + gap
    return sheet


def main():
    os.makedirs(OUT, exist_ok=True)
    manifest, preview, stickers = [], [], {}
    for key, (*lines, l2) in DESIGNS.items():
        im, meta = lockup(lines, False, 4500, l2)
        preview.append(save(im, f"{key}-apparel-4500.png", meta, "apparel", lines, manifest))
    for key, (*lines, l2) in DESIGNS.items():
        im, meta = lockup(lines, True, 2400, STICKER_L2.get(key, l2))
        stickers[key] = save(im, f"{key}-sticker-2400.png", meta, "sticker", lines, manifest)
        preview.append(im)
    *lines, l2 = DESIGNS["404-straight-not-found"]
    im, meta = lockup(lines, True, 4500, l2)
    preview.append(save(im, "404-tote-4500.png", meta, "tote", lines, manifest))
    # Logo: wordmark as line 1, stripe underneath. Cap front and apparel sleeve.
    im, meta = lockup(("FÆBRIQ",), False, 3600)
    preview.append(save(im, "logo-faebriq-1p35.png", meta, "cap front + sleeve", ["FÆBRIQ"], manifest))
    # Sleeve: FÆBRIQ alone, no stripe (the chest print already carries it,
    # and at 3 in the stripe would print as a 1.5 mm thread).
    f = font(1000)
    f = font(1000 * 3000 / ink_w(f, "FÆBRIQ"))
    m, _ = line_mask(f, "FÆBRIQ")
    pad = 60
    im = Image.new("RGBA", (m.width + 2 * pad, m.height + 2 * pad), (0, 0, 0, 0))
    ink = Image.new("RGBA", m.size, WHITE + (255,))
    ink.putalpha(m)
    im.alpha_composite(ink, (pad, pad))
    preview.append(save(im, "wordmark-faebriq-sleeve.png", {}, "apparel sleeve", ["FÆBRIQ"], manifest))
    sheet = sticker_sheet(stickers)
    save(sheet, "sticker-sheet-2400x3600.png", {}, "sticker sheet", SHEET, manifest)
    preview.append(sheet)

    contact(preview).save(os.path.join(OUT, "contact-sheet-on-black.jpg"), quality=88)
    with open(os.path.join(OUT, "manifest.json"), "w") as fh:
        json.dump(dict(system="FÆBRIQ print system", date="2026-09-25", font="Inter SemiBold",
                       stripe_over_widest_line=STRIPE_RATIO,
                       outputs=manifest), fh, indent=2, ensure_ascii=False)
    for e in manifest:
        print(e["file"], e["size"], e.get("stripe_over_widest"))


if __name__ == "__main__":
    main()
