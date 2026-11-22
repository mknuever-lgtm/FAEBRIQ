"""Tee product shots from the approved reference photo: removes the reference print and
places a real print file (assets/print-art/*-light-4500.png) at Printify size.

Usage: python3 tools/flat_from_reference.py REF ART OUT WIDTH_FRAC [TOP_Y] [--closeup]
WIDTH_FRAC = design width / body width, from the product's Printify scale,
calibrated so Off The Clock matches the reference (0.431).
TOP_Y = design top in reference pixels (1400x1750). Default 573, the approved
reference print top (Maurice, 2026-11-19: keep every tee at the photo position).
--closeup = 2048x2560 close-up framing the whole print (about 62% of the width);
the print is placed at close-up resolution from the 4500px file, so it stays sharp.
"""
import sys

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

# reference geometry, measured on the 1400x1750 reference
REF_W, REF_H = 1400, 1750
COLLAR, ARMPIT, BODY_L, BODY_R = 435, 737, 319, 1083
BACK_COLLAR_TOP = 306
OLD = (536, 573, 865, 649)        # reference print bbox
DONOR = 140                       # clean fabric this far below the reference print
OUT_W, OUT_H = 2048, 2560


def render(ref_path, art_path, width_frac, top_y=573.0, closeup=False):
    art = Image.open(art_path).convert("RGBA")
    art = art.crop(art.getchannel("A").getbbox())
    body_w_ref = BODY_R - BODY_L
    dw_ref = body_w_ref * width_frac
    dh_ref = dw_ref * art.height / art.width
    cx_ref = (BODY_L + BODY_R) / 2

    if closeup:   # window around the print, 4:5, print ~62% of width, centre at 45% height
        ww = max(dw_ref / 0.62, 600)
        wh = ww * OUT_H / OUT_W
        x0 = cx_ref - ww / 2
        y0 = top_y + dh_ref / 2 - wh * 0.45
    else:
        x0, y0, ww, wh = 0, 0, REF_W, REF_H
    S = OUT_W / ww

    # crop with room below for the donor fabric, then scale to output resolution
    ref = Image.open(ref_path).convert("RGB")
    extra = min(DONOR + 60, REF_H - (y0 + wh)) if closeup else 0
    box = (round(x0), round(y0), round(x0 + ww), round(y0 + wh + max(extra, 0)))
    crop = ref.crop(box)
    a = np.asarray(crop.resize((OUT_W, round(crop.height * S)), Image.LANCZOS)).astype(float)
    T = lambda x, y: ((x - box[0]) * S, (y - box[1]) * S)

    # 1. remove the reference print: mask its ink, fill with fabric from below it
    L = a @ [.299, .587, .114]
    sat = a.max(2) - a.min(2)
    (ox0, oy0), (ox1, oy1) = T(OLD[0], OLD[1]), T(OLD[2], OLD[3])
    pad = round(8 * S)
    m = np.zeros(L.shape, bool)
    m[max(0, round(oy0) - pad):round(oy1) + pad, max(0, round(ox0) - pad):round(ox1) + pad] = True
    ink = ndimage.binary_dilation(m & ((L > 45) | (sat > 25)), iterations=max(4, round(4 * S)))
    feather = ndimage.gaussian_filter(ink.astype(float), 2 * S)[..., None]
    donor = np.roll(a, -round(DONOR * S), axis=0)
    a = a * (1 - feather) + donor * feather
    a = a[:OUT_H] if closeup else a

    # 2. place the real print file at Printify size
    dw = round(dw_ref * S)
    dh = round(art.height * dw / art.width)
    art = art.resize((dw, dh), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.35 * S))
    p = np.asarray(art).astype(float)
    rgb, al = np.minimum(p[..., :3], 238), p[..., 3:] / 255 * 0.96   # ink, not screen white
    pcx, py = T(cx_ref, top_y)
    px, py = round(pcx - dw / 2), round(py)
    under = a[py:py + dh, px:px + dw]
    tex = under.mean(2, keepdims=True)
    tex = (tex / tex.mean()) ** 0.35                                  # fabric shows through
    a[py:py + dh, px:px + dw] = under * (1 - al) + rgb * tex * al

    if S > 1.6:   # upscaled fabric reads soft: add fine grain
        a += np.random.default_rng(3).normal(0, 1.4, a.shape[:2])[..., None]

    info = (f"design {dw}x{dh}px; width {width_frac:.1%} of body; zoom {S:.2f}x vs reference")
    if not closeup:
        info += (f"; centre frac {((py + dh / 2) / S - COLLAR) / (ARMPIT - COLLAR):.2f} (front seam"
                 f" to armpit); top gap {(top_y - COLLAR) / body_w_ref:.1%} of body from front seam,"
                 f" {(top_y - BACK_COLLAR_TOP) / body_w_ref:.1%} from top of back collar")
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)), info


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    ref_path, art_path, out = args[:3]
    wf = float(args[3])
    top = float(args[4]) if len(args) > 4 else 573.0
    im, info = render(ref_path, art_path, wf, top, closeup="--closeup" in sys.argv)
    im.save(out, quality=93)
    print(info)
