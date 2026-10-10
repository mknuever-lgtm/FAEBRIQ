"""Move the front print down on a generated on-model photo to where Printify
actually prints it (and optionally shrink it). Finds the print by its rainbow
bar, erases it (OpenCV inpaint), re-adds the same print pixels lower.
Target: print CENTRE at FRAC of the way from collar to armpit (default 0.65,
mid rib cage: where a chest logo or pendant sits, Maurice 2026-10-10).
Not for hoodies: drawstrings hide parts of the print and the gaps travel.

ARMPIT_Y = underarm crease where the inner arm leaves the torso, NOT the
shoulder/sleeve seam (see PRINT_PLACEMENT_SPEC.md, How to measure).

Usage: python3 tools/move_print_on_model.py IN OUT COLLAR_Y ARMPIT_Y [FRAC] [SHRINK]
"""
import sys, numpy as np, cv2
from PIL import Image
src, out, collar, armpit = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
frac = float(sys.argv[5]) if len(sys.argv) > 5 else 0.65
shrink = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
img = cv2.imread(src).astype(np.float32)
lum = img.mean(2); sat = img.max(2) - img.min(2)
# anchor on the rainbow bar: the only strongly saturated horizontal run
R, G, B = img[..., 2], img[..., 1], img[..., 0]
blue = (B > R + 40) & (B > G + 15) & (B > 90)
red = (R > G + 60) & (R > B + 50) & (R > 120)
rows = np.where((blue.sum(1) > 10) & (red.sum(1) > 10))[0]
rows = rows[(rows > collar) & (rows < armpit + 200)]
bar0, bar1 = rows.min(), rows.max()
bcols = np.where(((blue | red)[bar0:bar1 + 1]).sum(0) > 0)[0]
bx0, bx1 = bcols.min(), bcols.max()
bw = bx1 - bx0
y0, y1 = int(bar0 - 0.5 * bw), bar1 + 10
x0, x1 = bx0 - 15, bx1 + 15
box = np.zeros_like(lum, bool); box[y0:y1, x0:x1] = True
ink = ((lum > 70) | (sat > 60)) & box
ys, xs = np.where(ink)
y0 = ys.min() - 10
mask = np.zeros(lum.shape, np.uint8); mask[ink] = 255
mask[bar0 - 4:bar1 + 6, bx0 - 40:bx1 + 60] = 255  # whole old bar, faint tips included
reg = np.zeros_like(box); reg[y0:y1, x0 - 40:x1 + 60] = True
mask[((lum > 45) | (sat > 45)) & reg] = 255     # faint anti-aliased residue
x0, x1 = x0 - 40, x1 + 60
mask = cv2.dilate(mask, np.ones((7, 7), np.uint8))
clean = cv2.inpaint(img.astype(np.uint8), mask, 9, cv2.INPAINT_TELEA).astype(np.float32)
layer = np.clip(img - clean, 0, 255)[y0:y1, x0:x1]
# frac positions the print's vertical CENTRE (Maurice 2026-10-10: mid rib
# cage, where a chest logo / pendant sits, ~0.65 of collar-to-armpit)
target_mid = collar + frac * (armpit - collar)
dy = int(round(target_mid - (ys.min() + bar1) / 2))
res = clean.copy()
if shrink != 1.0:
    h, w = layer.shape[:2]
    nw, nh = int(w * shrink), int(h * shrink)
    layer = cv2.resize(layer, (nw, nh), interpolation=cv2.INTER_AREA)
    x0 = x0 + (w - nw) // 2; x1 = x0 + nw; y1 = y0 + nh
res[y0 + dy:y1 + dy, x0:x1] = np.clip(res[y0 + dy:y1 + dy, x0:x1] + layer, 0, 255)
cv2.imwrite(out, res.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 93])
print(f'print box y {ys.min()}-{ys.max()} x {x0}-{x1}, moved down {dy}px')
