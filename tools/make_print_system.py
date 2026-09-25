"""FÆBRIQ print system, 2026/09/25. One lockup for every product.

Maurice's rules:
  - Inter SemiBold on every design.
  - Line 2 is 75% of line 1's font size.
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
L2_SIZE = 0.75        # line 2 font size / line 1 font size
STRIPE_H = 0.018      # stripe height / stripe width
MARK_W = 0.20         # wordmark width / stripe width
# Vertical gaps, as a multiple of the cap height of the element above.
GAP_L1_L2 = 0.55
GAP_L2_BAR = 0.60
GAP_BAR_MARK = 0.75   # x the wordmark's own cap height
MARGIN = 0.045        # canvas margin / canvas width

DESIGNS = {
    "404-straight-not-found": ("404", "STRAIGHT NOT FOUND"),
    "code-it-serve-it": ("CODE IT.", "SERVE IT."),
    "off-the-clock-still-iconic": ("OFF THE CLOCK.", "STILL ICONIC."),
    "deploying-identity-v2": ("DEPLOYING", "IDENTITY V2.0"),
    "its-not-a-bug-its-me": ("IT’S NOT A BUG.", "IT’S ME."),
    "please-hold-rebranding-identity": ("PLEASE HOLD,", "I’M REBRANDING MY IDENTITY"),
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


def ink_box(f, text):
    """True ink box relative to the baseline anchor. font.getbbox pads the
    right edge to the advance width, which throws the 1.35x stripe off by
    a few percent on lines ending in a period or comma."""
    b = f.getbbox(text, anchor="ls")
    m = Image.new("L", (b[2] - b[0] + 4, b[3] - b[1] + 4), 0)
    ImageDraw.Draw(m).text((2 - b[0], 2 - b[1]), text, font=f, anchor="ls", fill=255)
    x0, y0, x1, y1 = m.getbbox()
    return x0 - 2 + b[0], y0 - 2 + b[1], x1 - 2 + b[0], y1 - 2 + b[1]


def ink_w(f, text):
    b = ink_box(f, text)
    return b[2] - b[0]


def layout(lines, wordmark, s):
    """Measure every element at line-1 font size s. Returns rows and stripe width."""
    fonts = [font(s), font(s * L2_SIZE)][:len(lines)]
    widest = max(ink_w(f, t) for f, t in zip(fonts, lines))
    sw = widest * STRIPE_RATIO
    fm = None
    if wordmark:
        fm = font(s)  # refit to MARK_W of the stripe width
        fm = font(s * (MARK_W * sw) / ink_w(fm, "FÆBRIQ"))
    return fonts, fm, sw


def lockup(lines, wordmark, width):
    """Transparent RGBA lockup whose stripe spans the canvas minus margins."""
    target = width * (1 - 2 * MARGIN)
    fonts, fm, sw = layout(lines, wordmark, 1000)
    s = 1000 * target / sw
    fonts, fm, sw = layout(lines, wordmark, s)

    pad = width * MARGIN
    y = pad
    rows = []  # (text, font, baseline)
    for i, (f, t) in enumerate(zip(fonts, lines)):
        y += cap_h(f)
        rows.append((t, f, y))
        # Descenders (Q, comma) sit below the baseline; gaps are measured
        # from the baseline so every design keeps the same rhythm.
        y += (GAP_L1_L2 if i < len(lines) - 1 else GAP_L2_BAR) * cap_h(f)
    bar_y, bar_h = y, round(sw * STRIPE_H)
    y += bar_h
    if fm:
        y += GAP_BAR_MARK * cap_h(fm) + cap_h(fm)
        rows.append(("FÆBRIQ", fm, y))
    bottom = y + max(0, max(f.getbbox(t, anchor="ls")[3] for t, f, _ in rows[-1:]))
    H = int(round(bottom + pad))

    im = Image.new("RGBA", (width, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx = width / 2
    for t, f, base in rows:
        b = ink_box(f, t)
        d.text((cx - (b[0] + b[2]) / 2, base), t, font=f, anchor="ls", fill=WHITE + (255,))
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
    for key, lines in DESIGNS.items():
        im, meta = lockup(lines, False, 4500)
        preview.append(save(im, f"{key}-apparel-4500.png", meta, "apparel", lines, manifest))
    for key, lines in DESIGNS.items():
        im, meta = lockup(lines, True, 2400)
        stickers[key] = save(im, f"{key}-sticker-2400.png", meta, "sticker", lines, manifest)
        preview.append(im)
    im, meta = lockup(DESIGNS["404-straight-not-found"], True, 4500)
    preview.append(save(im, "404-tote-4500.png", meta, "tote",
                        DESIGNS["404-straight-not-found"], manifest))
    # Logo: wordmark as line 1, stripe underneath. Cap front and apparel sleeve.
    im, meta = lockup(("FÆBRIQ",), False, 3600)
    preview.append(save(im, "logo-faebriq-1p35.png", meta, "cap front + sleeve", ["FÆBRIQ"], manifest))
    sheet = sticker_sheet(stickers)
    save(sheet, "sticker-sheet-2400x3600.png", {}, "sticker sheet", SHEET, manifest)
    preview.append(sheet)

    contact(preview).save(os.path.join(OUT, "contact-sheet-on-black.jpg"), quality=88)
    with open(os.path.join(OUT, "manifest.json"), "w") as fh:
        json.dump(dict(system="FÆBRIQ print system", date="2026-09-25", font="Inter SemiBold",
                       stripe_over_widest_line=STRIPE_RATIO, line2_size=L2_SIZE,
                       outputs=manifest), fh, indent=2, ensure_ascii=False)
    for e in manifest:
        print(e["file"], e["size"], e.get("stripe_over_widest"))


if __name__ == "__main__":
    main()
