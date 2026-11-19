"""Front tee flat from the approved reference photo: removes the reference print and
places a real print file (assets/print-art/*-light-4500.png) at Printify size.
Usage: python3 tools/flat_from_reference.py REF ART OUT WIDTH_FRAC [TOP_Y]
WIDTH_FRAC = design width / body width, from the product's Printify scale,
calibrated so Off The Clock matches the reference (0.431).
TOP_Y = design top in reference pixels (1400x1750). Default 573, the approved
reference print top (Maurice, 2026-11-19: keep every tee at the photo position).
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

REF = sys.argv[1]; ART = sys.argv[2]; OUT = sys.argv[3]
WIDTH_FRAC = float(sys.argv[4])   # design width / body width
TOP_Y = float(sys.argv[5]) if len(sys.argv) > 5 else 573.0
# reference geometry, measured on the 1400x1750 reference
COLLAR, ARMPIT, BODY_L, BODY_R = 435, 737, 319, 1083
OLD = (536, 573, 865, 649)        # old print bbox
S = 2048 / 1400

ref = Image.open(REF).convert("RGB").resize((2048, 2560), Image.LANCZOS)
a = np.asarray(ref).astype(float)
L = a @ [.299, .587, .114]; sat = a.max(2) - a.min(2)

# 1. remove the old print: mask its ink, fill with fabric from below it
x0, y0, x1, y1 = [round(v * S) for v in OLD]
box = np.zeros(L.shape, bool); box[y0-12:y1+12, x0-12:x1+12] = True
ink = box & ((L > 45) | (sat > 25))
ink = ndimage.binary_dilation(ink, iterations=6)
feather = ndimage.gaussian_filter(ink.astype(float), 3)[..., None]
shift = round(140 * S)
donor = np.roll(a, -shift, axis=0)            # fabric 140px (ref) lower
a = a * (1 - feather) + donor * feather

# 2. place the real print file at Printify size
art = Image.open(ART).convert("RGBA")
art = art.crop(art.getchannel("A").getbbox())
body_w = (BODY_R - BODY_L) * S
dw = round(body_w * WIDTH_FRAC); dh = round(art.height * dw / art.width)
art = art.resize((dw, dh), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.5))
p = np.asarray(art).astype(float)
rgb, al = p[..., :3], p[..., 3:] / 255
rgb = np.minimum(rgb, 238)                    # ink, not screen white
cx = (BODY_L + BODY_R) / 2 * S
px, py = round(cx - dw / 2), round(TOP_Y * S)
under = a[py:py+dh, px:px+dw]
tex = under.mean(2, keepdims=True); tex = (tex / tex.mean()) ** 0.35   # fabric shows through
al = al * 0.96
a[py:py+dh, px:px+dw] = under * (1 - al) + rgb * tex * al

Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(OUT, quality=93)
print(f"body_w {body_w:.0f}px design {dw}x{dh}px at ({px},{py}); width {dw/body_w:.1%} of body; "
      f"centre frac {((py + dh/2)/S - COLLAR)/(ARMPIT - COLLAR):.2f} (front seam to armpit); "
      f"top gap {(py - COLLAR*S)/body_w:.1%} of body from front seam, "
      f"{(py - 306*S)/body_w:.1%} from top of back collar")
