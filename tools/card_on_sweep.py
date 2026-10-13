"""Place a flat dark product card (sticker or sticker sheet on black) on the
charcoal studio sweep, framed like the live single-sticker shots: card 1640px
wide (x 204 to 1843 on the 2048x2560 frame), centred, soft drop shadow.

Usage: python3 tools/card_on_sweep.py IN OUT
"""
import sys

import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, "tools")
from mockup_to_charcoal import OUT_H, OUT_W, sweep

CARD_W = 1640


def place(src, out):
    card = Image.open(src).convert("RGB")
    card = card.resize((CARD_W, round(card.height * CARD_W / card.width)), Image.LANCZOS)
    g = Image.fromarray(np.clip(sweep(), 0, 255).astype(np.uint8))
    x, y = (OUT_W - card.width) // 2, (OUT_H - card.height) // 2
    # Soft shadow: a blurred dark plate offset slightly down, multiplied in.
    sh = Image.new("L", (OUT_W, OUT_H), 0)
    sh.paste(150, (x + 10, y + 28, x + card.width + 10, y + card.height + 28))
    sh = sh.filter(ImageFilter.GaussianBlur(36))
    a = np.asarray(g).astype(float) * (1 - np.asarray(sh)[..., None] / 255 * 0.6)
    g = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    g.paste(card, (x, y))
    g.save(out, quality=92)
    print(out, g.size)


if __name__ == "__main__":
    place(sys.argv[1], sys.argv[2])
