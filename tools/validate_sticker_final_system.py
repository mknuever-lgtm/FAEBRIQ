from pathlib import Path
import json
from PIL import Image

root = Path(__file__).resolve().parents[1]
folder = root / "assets" / "print-art" / "sticker-final-system-2026-08-27"
expected = {
    "deploying-identity-v2-sticker-light-2400.png": ("DEPLOYING", "IDENTITY V2.0"),
    "please-hold-rebranding-identity-sticker-light-2400.png": ("PLEASE HOLD", "I'M REBRANDING MY IDENTITY"),
    "code-it-serve-it-sticker-light-2400.png": ("CODE IT.", "SERVE IT."),
    "error-404-straight-not-found-sticker-light-2400.png": ("ERROR 404", "STRAIGHT NOT", "FOUND"),
    "its-not-a-bug-its-me-sticker-light-2400.png": ("IT'S NOT A BUG.", "IT'S ME."),
}
required_circuit = {(232, 39, 42), (244, 127, 32), (249, 212, 38), (42, 170, 66), (29, 91, 190), (123, 63, 170)}
results = []
for name, text in expected.items():
    path = folder / name
    if not path.exists():
        raise SystemExit(f"missing: {path}")
    with Image.open(path) as im:
        colors = set(im.convert("RGBA").getdata())
        rgb_colors = {(r, g, b) for r, g, b, a in colors if a > 0}
        alpha = im.getchannel("A")
        bbox = alpha.getbbox()
        row = {
            "file": str(path.relative_to(root)),
            "text": list(text),
            "width_px": im.width,
            "height_px": im.height,
            "mode": im.mode,
            "dpi": im.info.get("dpi"),
            "transparent_background": (0, 0, 0, 0) in colors,
            "alpha_bbox": bbox,
            "circuit_colors_present": sorted(required_circuit.intersection(rgb_colors)),
            "pass": im.size[0] == 2400 and im.mode == "RGBA" and im.info.get("dpi", (0, 0))[0] >= 299 and len(required_circuit.intersection(rgb_colors)) == 6,
        }
        if not row["pass"]:
            raise SystemExit(json.dumps(row, indent=2))
        results.append(row)
manifest = {
    "system": "FÆBRIQ sticker final system",
    "date": "2026-08-27",
    "product": "sticker",
    "provider": "SPOKE kiss-cut",
    "ink": "light",
    "resolution": "2400 px wide, RGBA, 300 dpi",
    "rules": {
        "wordmark_included": True,
        "pride_circuit_stripes": 6,
        "transparent_background": True,
        "no_store_publish_or_sync": True,
    },
    "outputs": results,
}
manifest_path = folder / "manifest.json"
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(manifest, indent=2, ensure_ascii=False))
