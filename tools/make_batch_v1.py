#!/usr/bin/env python3
"""FAEBRIQ batch v1: 10 terminal-style DTG graphics for BLACK garments.

Canvas 4500x5400 @ 300 DPI, fully transparent background. Each design is drawn
at 2x (9000x10800) as one alpha mask per ink colour, then every mask is
Lanczos-downsampled to 1x and composited. That is the "2x pass": supersampled
edges, no upscaling of a raster, no dark fringe on the anti-aliased pixels.

Palette (black garments only): white #FFFFFF, slate #8E9AAF, terracotta #D96B43.
Type: JetBrains Mono (Google Fonts, OFL).

    python3 tools/make_batch_v1.py --fonts <dir with JBM-*.ttf> \
        --out assets/print-art/faebriq_batch_v1 [--mirror /workspace/scratch/faebriq_batch_v1]
"""
import argparse
import json
import os
import shutil

from PIL import Image, ImageDraw, ImageFont

W, H, DPI, SS = 4500, 5400, 300, 2
INK = {"w": "#FFFFFF", "s": "#8E9AAF", "t": "#D96B43"}
WEIGHT = {"r": "JBM-Regular.ttf", "b": "JBM-Bold.ttf", "x": "JBM-ExtraBold.ttf"}

# Each line: (relative size, weight, [(text, ink), ...]). "CURSOR" draws a
# terracotta block cursor. None = spacer (relative height).
DESIGNS = [
    dict(slug="commit-amend", slogan="$ git commit --amend // identity in active refactor",
         placement="Front Center",
         keywords=["queer developer shirt", "git commit tee", "identity as code", "trans in tech", "refactor shirt"],
         lines=[(1.0, "x", [("$ ", "s"), ("git commit", "w")]),
                (1.0, "x", [("  --amend", "t"), ("CURSOR", "t")]),
                (0.35, None, None),
                (0.42, "r", [("// identity in active refactor", "s")])]),
    dict(slug="checkout-me", slogan="$ git checkout -b me / Switched to a new branch 'me'",
         placement="Left Chest",
         keywords=["git branch shirt", "coming out tee", "queer coder", "lgbtq programmer gift", "minimal dev tee"],
         lines=[(1.0, "x", [("$ ", "s"), ("git checkout -b ", "w"), ("me", "t")]),
                (0.30, None, None),
                (0.50, "r", [("Switched to a new branch 'me'", "s")])]),
    dict(slug="wontfix-1969", slogan="#1969 just be straight / closed as WONTFIX",
         placement="Front Center",
         keywords=["stonewall 1969 shirt", "wontfix tee", "gay developer shirt", "github issue humor", "queer pride subtle"],
         lines=[(0.55, "b", [("issue ", "s"), ("#1969", "t")]),
                (0.20, None, None),
                (0.80, "x", [("\"just be straight\"", "w")]),
                (0.40, None, None),
                (1.20, "x", [("WONTFIX", "t")]),
                (0.20, None, None),
                (0.45, "r", [("closed. not planned. ever.", "s")])]),
    dict(slug="no-closet", slogan="$ cd /closet / No such file or directory",
         placement="Front Center",
         keywords=["out and proud tee", "bash humor shirt", "queer tech worker", "linux terminal shirt", "no closet"],
         lines=[(1.0, "x", [("$ ", "s"), ("cd /closet", "w")]),
                (0.35, None, None),
                (0.55, "b", [("bash: cd: /closet:", "t")]),
                (0.55, "b", [("No such file or directory", "t")])]),
    dict(slug="deprecated", slogan="npm WARN deprecated heteronormativity@1.0.0: no longer maintained",
         placement="Front Center",
         keywords=["npm warn shirt", "javascript dev tee", "queer web developer", "deprecated humor", "lgbtq coder gift"],
         lines=[(0.55, "b", [("npm ", "s"), ("WARN ", "t"), ("deprecated", "s")]),
                (0.25, None, None),
                (1.0, "x", [("heteronormativity", "w")]),
                (1.0, "x", [("@1.0.0", "w")]),
                (0.30, None, None),
                (0.55, "r", [("no longer maintained.", "s")])]),
    dict(slug="breaking-change", slogan="v2.0.0 / BREAKING CHANGE: came out. not a phase. a major release.",
         placement="Front Center",
         keywords=["semver shirt", "not a phase tee", "coming out gift", "software engineer queer", "release notes shirt"],
         lines=[(2.0, "x", [("v2.0.0", "w")]),
                (0.25, None, None),
                (0.55, "b", [("BREAKING CHANGE: ", "t"), ("came out.", "w")]),
                (0.30, None, None),
                (0.45, "r", [("not a phase. a major release.", "s")])]),
    dict(slug="kept-mine", slogan="CONFLICT (identity): merge conflict / resolved: kept mine.",
         placement="Front Center",
         keywords=["merge conflict shirt", "git humor tee", "nonbinary coder", "queer self love tee", "developer identity"],
         lines=[(0.55, "b", [("CONFLICT ", "t"), ("(identity):", "s")]),
                (0.55, "b", [("merge conflict in self.md", "s")]),
                (0.35, None, None),
                (1.0, "x", [("resolved:", "w")]),
                (1.0, "x", [("kept ", "w"), ("mine.", "t")])]),
    dict(slug="no-sudo", slogan="$ sudo be gay / permission not required",
         placement="Left Chest",
         keywords=["sudo shirt", "linux gay tee", "sysadmin queer", "unapologetic pride", "terminal humor"],
         lines=[(1.0, "x", [("$ ", "s"), ("sudo ", "t"), ("be gay", "w")]),
                (0.30, None, None),
                (0.48, "r", [("sudo: permission not required", "s")])]),
    dict(slug="identity-diff", slogan="--- a/expectations +++ b/me / - straight - quiet + queer + loud",
         placement="Front Center",
         keywords=["git diff shirt", "code review tee", "queer engineer", "loud and queer", "pull request humor"],
         lines=[(0.50, "b", [("--- a/expectations", "s")]),
                (0.50, "b", [("+++ b/me", "s")]),
                (0.30, None, None),
                (1.0, "x", [("- straight", "t")]),
                (1.0, "x", [("- quiet", "t")]),
                (1.0, "x", [("+ queer", "w")]),
                (1.0, "x", [("+ loud", "w")])]),
    dict(slug="runtime-pronouns", slogan="export PRONOUNS=they/them # set at runtime. not hardcoded.",
         placement="Left Chest",
         keywords=["pronoun shirt", "they them tee", "nonbinary developer", "env variable humor", "trans coder gift"],
         lines=[(0.50, "b", [("$ export", "s")]),
                (1.0, "x", [("PRONOUNS=", "w"), ("they/them", "t")]),
                (0.30, None, None),
                (0.46, "r", [("# set at runtime. not hardcoded.", "s")])]),
]

BASE = 400  # px at 2x for relative size 1.0, before fit-to-width scaling
MAX_W = 0.86  # block width as share of canvas
TOP = 0.07  # block top offset as share of canvas height
LEAD = 1.18  # line height multiplier


def layout(d, fonts_dir, scale):
    fonts, rows = {}, []
    for size, wt, segs in d["lines"]:
        px = int(BASE * size * scale)
        if segs is None:
            rows.append((px, None, None))
            continue
        key = (wt, px)
        if key not in fonts:
            fonts[key] = ImageFont.truetype(os.path.join(fonts_dir, WEIGHT[wt]), px)
        rows.append((px, fonts[key], segs))
    return rows


def row_width(font, segs):
    w = 0
    for text, _ in segs:
        w += int(font.size * 0.62) if text == "CURSOR" else font.getlength(text)
    return w


def render(d, fonts_dir):
    W2, H2 = W * SS, H * SS
    rows = layout(d, fonts_dir, 1.0)
    widest = max(row_width(f, s) for _, f, s in rows if f)
    rows = layout(d, fonts_dir, (W2 * MAX_W) / widest)
    widest = max(row_width(f, s) for _, f, s in rows if f)
    masks = {k: Image.new("L", (W2, H2), 0) for k in INK}
    draws = {k: ImageDraw.Draw(m) for k, m in masks.items()}
    x0, y = (W2 - widest) / 2, H2 * TOP
    for px, font, segs in rows:
        if font is None:
            y += px
            continue
        asc, _ = font.getmetrics()
        x = x0
        for text, ink in segs:
            if text == "CURSOR":
                cw = font.size * 0.62
                draws[ink].rectangle([x + font.size * 0.08, y + asc * 0.08, x + cw, y + asc * 1.02], fill=255)
                x += cw
            else:
                draws[ink].text((x, y), text, font=font, fill=255)
                x += font.getlength(text)
        y += px * LEAD
    assert y < H2 * 0.95, f"{d['slug']} overflows canvas"
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for k, m in masks.items():
        layer = Image.new("RGBA", (W, H), INK[k])
        layer.putalpha(m.resize((W, H), Image.LANCZOS))
        out = Image.alpha_composite(out, layer)
    return out


def left_chest(img):
    """Tight crop with 4% pad so Printify's chest area isn't mostly empty canvas."""
    x0, y0, x1, y1 = img.getchannel("A").getbbox()
    pad = int(max(x1 - x0, y1 - y0) * 0.04)
    return img.crop((x0 - pad, y0 - pad, x1 + pad, y1 + pad))


def preview(files, out):
    th = 540
    tw = int(th * W / H)
    sheet = Image.new("RGB", (tw * 5, th * 2), "#0f0e0c")
    for i, f in enumerate(files):
        im = Image.open(f).resize((tw, th), Image.LANCZOS)
        sheet.paste(im, ((i % 5) * tw, (i // 5) * th), im)
    sheet.save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--mirror")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    manifest, files = [], []
    for i, d in enumerate(DESIGNS, 1):
        name = f"faebriq_design_{i:02d}_{d['slug']}.png"
        path = os.path.join(a.out, name)
        img = render(d, a.fonts)
        img.save(path, dpi=(DPI, DPI), optimize=True)
        files.append(path)
        entry = dict(design_id=f"FAEBRIQ-B1-{i:02d}", file=name, slogan=d["slogan"],
                     micro_niche_keywords=d["keywords"], printify_placement=d["placement"],
                     canvas_px=[W, H], dpi=DPI, background="transparent",
                     inks=sorted({INK[s[1]] for _, _, segs in d["lines"] if segs for s in segs}),
                     garment="black only")
        if d["placement"] == "Left Chest":
            lc = name.replace(".png", "_leftchest.png")
            left_chest(img).save(os.path.join(a.out, lc), dpi=(DPI, DPI), optimize=True)
            entry["left_chest_file"] = lc
        manifest.append(entry)
    with open(os.path.join(a.out, "manifest.json"), "w") as fh:
        json.dump({"batch": "faebriq_batch_v1", "palette": INK, "font": "JetBrains Mono (OFL)",
                   "designs": manifest}, fh, indent=2, ensure_ascii=False)
    preview(files, os.path.join(a.out, "_preview_on_black.png"))
    if a.mirror:
        shutil.copytree(a.out, a.mirror, dirs_exist_ok=True)


if __name__ == "__main__":
    main()
