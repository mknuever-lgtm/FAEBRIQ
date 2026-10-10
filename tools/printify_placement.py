"""Turn the FÆBRIQ front-print spec (inches) into Printify print_areas values.

Spec (PRINT_PLACEMENT_SPEC.md): design (alpha bbox, bar = full width) centred,
top edge a fixed distance below the collar seam, fixed printed width.

Input: JSON list, one object per product, e.g.
  {"handle": "code-it-serve-it-tee", "garment": "tee",
   "file": "assets/print-art/code-it-serve-it-light-4500.png",
   "placeholder_w_px": 4500, "placeholder_h_px": 5400, "dpi": 300,
   "area_top_below_collar_in": 1.0}
Output: x, y, scale per product (Printify: x/y = image centre as a fraction of
the placeholder, scale = image width / placeholder width -- Inference, verify
on the re-rendered mockup with the check ratios printed below).

Usage: python3 tools/printify_placement.py products.json
"""
import json
import sys

from PIL import Image

SPEC = {  # garment: (design width in, design top below collar seam in)
    "tee": (10.0, 3.0),
    "crewneck": (10.0, 3.0),
    "hoodie": (10.0, 3.5),
}
BODY_W_L = {"tee": 22.0, "crewneck": 24.0, "hoodie": 24.0}  # size L chest width, in (check only)


def place(p):
    width_in, top_in = SPEC[p["garment"]]
    im = Image.open(p["file"])
    fw, fh = im.size
    bx0, by0, bx1, by1 = im.getchannel("A").getbbox()
    dpi = p.get("dpi", 300)
    pw_in, ph_in = p["placeholder_w_px"] / dpi, p["placeholder_h_px"] / dpi
    file_w_in = width_in * fw / (bx1 - bx0)          # whole file, so the design itself hits width_in
    file_h_in = file_w_in * fh / fw
    file_top_in = top_in - p["area_top_below_collar_in"] - by0 / fh * file_h_in
    design_cx = (bx0 + bx1) / 2 / fw                  # keep the design, not the canvas, centred
    x = 0.5 + (0.5 - design_cx) * file_w_in / pw_in
    y = (file_top_in + file_h_in / 2) / ph_in
    scale = file_w_in / pw_in
    body = BODY_W_L[p["garment"]]
    return {"handle": p["handle"], "x": round(x, 4), "y": round(y, 4), "scale": round(scale, 4),
            "printed_in": f'{width_in} x {width_in * (by1 - by0) / (bx1 - bx0):.2f}',
            "check_L_mockup": f"design width {width_in / body:.0%} of body width; "
                              f"collar-to-design gap {top_in / body:.0%} of body width"}


if __name__ == "__main__":
    for p in json.load(open(sys.argv[1])):
        print(json.dumps(place(p)))
