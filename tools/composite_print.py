#!/usr/bin/env python3
"""
Composite a real FAEBRIQ print master onto a garment photo so it reads as ink
on cloth instead of a sticker.

The generated model shots have good lighting and drape but their prints are
fake: wrong artwork, gradient bar instead of the six-block pride bar, razor
edges, and uniform brightness across a chest that is half in shadow. This
script removes the fake print and lays the real 4500px master back down with:

  heal        the fake print is detected as pixels brighter than the local
              fabric, then filled with the fabric's own low-frequency
              luminance plus grain sampled from clean cloth nearby
  warp        the master is perspective-mapped into a quad on the chest
  displace    the garment's own blurred luminance gradient pushes the print
              pixels around, so edges ride the folds
  shade       the print is multiplied by the garment's normalised luminance,
              so it falls into shadow exactly where the cloth does
  weave       a small amount of the fabric's high-frequency texture is added
              back over the ink, and the edges get sub-pixel softening

Usage:
  python3 tools/composite_print.py --garment assets/model-tee-new.png \
      --print assets/print-art/code-it-serve-it-light-4500.png \
      --quad 288,252,428,246,430,316,290,322 \
      --out assets/model-tee-composite.png [--debug]
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent


def parse_quad(s):
    v = [float(x) for x in s.split(",")]
    if len(v) != 8:
        raise ValueError("quad needs 8 comma-separated numbers: tlx,tly,trx,try,brx,bry,blx,bly")
    return [(v[0], v[1]), (v[2], v[3]), (v[4], v[5]), (v[6], v[7])]


def luminance(rgb):
    return rgb[..., 0] * 0.2126 + rgb[..., 1] * 0.7152 + rgb[..., 2] * 0.0722


def blur(a, radius):
    """Gaussian blur a float array in 0..1 via PIL, shape preserved."""
    squeeze = a.ndim == 3 and a.shape[2] == 1
    src = a[..., 0] if squeeze else a
    im = Image.fromarray((np.clip(src, 0, 1) * 255).astype(np.uint8))
    out = np.asarray(im.filter(ImageFilter.GaussianBlur(radius)), dtype=np.float32) / 255.0
    return out[..., None] if squeeze else out


def heal_existing_print(rgb, roi, threshold, grow, feather):
    """
    Remove the baked-in fake print inside roi.

    The garment is near-black and smoothly lit, so anything notably brighter
    than the local fabric is print. Replace it with the region's own
    low-frequency luminance (which carries the real lighting) plus grain
    lifted from clean fabric in the same region, so the patch keeps the
    photo's noise floor instead of going plastic-smooth.
    """
    x0, y0, x1, y1 = roi
    patch = rgb[y0:y1, x0:x1]
    lum = luminance(patch)

    # Detect on the high-pass, not on raw brightness. Print is small bright
    # detail; the lighting across a chest is a broad gradient. Thresholding
    # raw luminance makes the cut depend on how lit the garment happens to
    # be, which flagged the whole lit side of the darker hoodie shot.
    highpass = lum - blur(lum, 6)
    scale = 1.4826 * np.median(np.abs(highpass - np.median(highpass))) + 1e-6

    # Black cloth is neutral, so anything carrying real chroma is ink even
    # when it is too dark to trip the luminance test (the old gradient bar).
    chroma = patch.max(axis=-1) - patch.min(axis=-1)
    chroma_hp = chroma - blur(chroma, 6)
    chroma_scale = 1.4826 * np.median(np.abs(chroma_hp - np.median(chroma_hp))) + 1e-6

    mask = ((highpass > threshold * scale) | (chroma_hp > 3.0 * chroma_scale)).astype(np.float32)
    mask = np.clip(blur(mask, grow) * 3.0, 0, 1)

    # Rebuild the cloth under the print by fitting a smooth quadratic surface
    # to the clean fabric pixels, per channel. A blur-and-divide fill leaves
    # blotches wherever the mask is dense; a fitted surface cannot, because it
    # only ever sees fabric and is smooth by construction.
    ph, pw = mask.shape
    yy, xx = np.mgrid[0:ph, 0:pw].astype(np.float32)
    xn, yn = xx / max(pw - 1, 1) - 0.5, yy / max(ph - 1, 1) - 0.5
    basis = np.stack([np.ones_like(xn), xn, yn, xn * xn, xn * yn, yn * yn], axis=-1)
    clean_sel = mask < 0.05
    filled = np.zeros_like(patch)
    if clean_sel.sum() > 32:
        A = basis[clean_sel]
        for c in range(3):
            coef, *_ = np.linalg.lstsq(A, patch[clean_sel][:, c], rcond=None)
            filled[..., c] = basis @ coef
    else:
        filled[:] = patch.mean(axis=(0, 1))

    # Grain from the darkest (cleanest) third of the region.
    clean = patch[lum < np.percentile(lum, 33)]
    grain_sigma = float(clean.std()) if clean.size else 0.004
    rng = np.random.default_rng(7)
    grain = rng.normal(0.0, grain_sigma * 0.9, filled.shape).astype(np.float32)

    patched = patch * (1 - mask)[..., None] + (filled + grain) * mask[..., None]

    # Feather the ROI border, otherwise the patched rectangle reads as a
    # faint tonal box against the surrounding cloth.
    fh, fw = mask.shape
    edge = np.ones((fh, fw), dtype=np.float32)
    edge[:1, :] = edge[-1:, :] = edge[:, :1] = edge[:, -1:] = 0.0
    edge = blur(edge, feather)
    out = rgb.copy()
    out[y0:y1, x0:x1] = patch * (1 - edge)[..., None] + patched * edge[..., None]
    return np.clip(out, 0, 1), mask


def warp_into_quad(art, quad, size):
    """Perspective-map the art image so its corners land on quad."""
    w, h = size
    src = [(0, 0), (art.width, 0), (art.width, art.height), (0, art.height)]
    # PIL wants the inverse map: destination -> source.
    a = []
    b = []
    for (dx, dy), (sx, sy) in zip(quad, src):
        a.append([dx, dy, 1, 0, 0, 0, -sx * dx, -sx * dy])
        b.append(sx)
        a.append([0, 0, 0, dx, dy, 1, -sy * dx, -sy * dy])
        b.append(sy)
    coeffs = np.linalg.solve(np.array(a, dtype=np.float64), np.array(b, dtype=np.float64))
    return art.transform((w, h), Image.PERSPECTIVE, coeffs, Image.BICUBIC)


def displace(layer, field, amount):
    """Push layer's pixels along the gradient of field, by up to `amount` px."""
    gy, gx = np.gradient(field)
    scale = amount / (max(float(np.abs(gx).max()), float(np.abs(gy).max())) + 1e-6)
    h, w = field.shape
    yy, xx = np.mgrid[0:h, 0:w]
    sx = np.clip(xx + gx * scale, 0, w - 1)
    sy = np.clip(yy + gy * scale, 0, h - 1)
    x0, y0 = np.floor(sx).astype(int), np.floor(sy).astype(int)
    x1, y1 = np.minimum(x0 + 1, w - 1), np.minimum(y0 + 1, h - 1)
    fx, fy = (sx - x0)[..., None], (sy - y0)[..., None]
    top = layer[y0, x0] * (1 - fx) + layer[y0, x1] * fx
    bot = layer[y1, x0] * (1 - fx) + layer[y1, x1] * fx
    return top * (1 - fy) + bot * fy


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--garment", required=True)
    ap.add_argument("--print", dest="art", required=True)
    ap.add_argument("--quad", required=True, help="tlx,tly,trx,try,brx,bry,blx,bly")
    ap.add_argument("--out", required=True)
    ap.add_argument("--roi", default=None, help="x0,y0,x1,y1 heal box; defaults to the quad's bbox padded")
    ap.add_argument("--heal-also", action="append", default=[],
                    help="extra x0,y0,x1,y1 box to clean but not print on; repeatable "
                         "(the cap's brim swoosh, for instance)")
    ap.add_argument("--heal-threshold", type=float, default=4.0, help="high-pass sigmas above cloth noise that count as print")
    ap.add_argument("--heal-grow", type=float, default=2.5)
    ap.add_argument("--feather", type=float, default=3.0, help="heal-box edge feather, px; keep the roi wider than this")
    ap.add_argument("--opacity", type=float, default=0.93)
    ap.add_argument("--displace", type=float, default=0.7, help="max fold displacement, px")
    ap.add_argument("--supersample", type=float, default=3.0, help="art px per output px before warping")
    ap.add_argument("--shade", type=float, default=0.85, help="0 = flat ink, 1 = fully lit by the cloth")
    ap.add_argument("--weave", type=float, default=0.35, help="how much fabric texture shows through the ink")
    ap.add_argument("--softness", type=float, default=0.6, help="edge blur, px")
    ap.add_argument("--debug", action="store_true", help="also write a _debug.png with the quad drawn")
    args = ap.parse_args()

    garment = Image.open(ROOT / args.garment).convert("RGB")
    rgb = np.asarray(garment, dtype=np.float32) / 255.0
    W, H = garment.size
    quad = parse_quad(args.quad)

    xs = [p[0] for p in quad]
    ys = [p[1] for p in quad]
    if args.roi:
        roi = tuple(int(v) for v in args.roi.split(","))
    else:
        pad = 14
        roi = (max(0, int(min(xs)) - pad), max(0, int(min(ys)) - pad),
               min(W, int(max(xs)) + pad), min(H, int(max(ys)) + pad))

    healed, _ = heal_existing_print(rgb, roi, args.heal_threshold, args.heal_grow, args.feather)
    for box in args.heal_also:
        extra = tuple(int(v) for v in box.split(","))
        healed, _ = heal_existing_print(healed, extra, args.heal_threshold, args.heal_grow, args.feather)

    art = Image.open(ROOT / args.art).convert("RGBA")
    quad_w = max(abs(quad[1][0] - quad[0][0]), abs(quad[2][0] - quad[3][0]))
    target = max(1, int(quad_w * args.supersample))
    if art.width > target:
        art = art.resize((target, max(1, round(art.height * target / art.width))), Image.LANCZOS)
    warped = np.asarray(warp_into_quad(art, quad, (W, H)), dtype=np.float32) / 255.0
    ink, alpha = warped[..., :3], warped[..., 3]

    lum = luminance(healed)
    folds = blur(lum, 2.2)
    ink = displace(ink, folds, args.displace)
    alpha = displace(alpha[..., None], folds, args.displace)[..., 0]

    # Shade the ink by how lit the cloth under it is. Reference is the bright
    # end of the print area, so the lit side stays at full strength and the
    # shadowed side drops away with the fabric.
    inside = alpha > 0.15
    if inside.any():
        ref = float(np.percentile(folds[inside], 88)) + 1e-6
        shading = np.clip(folds / ref, 0.0, 1.25)
        shading = 1.0 - args.shade + args.shade * shading
    else:
        shading = np.ones_like(folds)
    ink = ink * shading[..., None]

    # Let the weave and its noise come back through the ink.
    texture = lum - folds
    ink = np.clip(ink + texture[..., None] * args.weave, 0, 1)

    if args.softness > 0:
        alpha = blur(alpha[..., None], args.softness)[..., 0]
    a = np.clip(alpha * args.opacity, 0, 1)[..., None]

    out = np.clip(healed * (1 - a) + ink * a, 0, 1)
    img = Image.fromarray((out * 255).astype(np.uint8))
    outp = ROOT / args.out
    outp.parent.mkdir(parents=True, exist_ok=True)
    img.save(outp)
    print(f"wrote {args.out}  (quad {quad}, heal roi {roi})")

    if args.debug:
        from PIL import ImageDraw
        dbg = img.copy()
        d = ImageDraw.Draw(dbg)
        d.polygon(quad, outline=(0, 255, 255))
        d.rectangle(roi, outline=(255, 0, 255))
        p = outp.with_name(outp.stem + "_debug.png")
        dbg.save(p)
        print(f"wrote {p}")


if __name__ == "__main__":
    main()
