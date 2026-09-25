# FÆBRIQ: product images on the new print system (Muse, continuing from Manus)

Paste into Muse. Written 2026/09/25, revised 2026/09/25.

## Where things stand
Manus ran out of credits: no images, nothing saved in Printify. Start the images from zero. **Printify is now Muse's job**, via the Printify connector. Check the Code It Tee first: Manus deleted its old design but never uploaded the new file.

## Order of work
1. Tier 2 images: slots 1-2, all 12 products (24 images).
2. Printify: all 12 swaps, Maurice approves first.
3. Tier 3: slots 3-4, only if budget remains. Printify matters more for sales.

## Budget rules
- Do only what this brief lists, in the order above. No exploring, no Shopify, no storefront browsing.
- Max 2 attempts per image, then keep the best and flag it.
- Never redo finished work.
- If budget runs low, stop, commit, and write the report.

## Inputs
- Repo `mknuever-lgtm/FAEBRIQ`, branch `claude/hopeful-goldberg-a40dkh`, folder `assets/print-art/system-2026-09-25/`. These are the only print files allowed. Do not alter them.
- Preview of every design: `contact-sheet-on-black.jpg`.

| Shopify handle | Product (all blanks black) | Print file |
|---|---|---|
| `404-straight-not-found-tee` | heavy cotton tee | `404-straight-not-found-apparel-4500.png` |
| `code-it-serve-it-tee` | heavy cotton tee | `code-it-serve-it-apparel-4500.png` |
| `off-the-clock-still-iconic-hoodie` | heavyweight hoodie | `off-the-clock-still-iconic-apparel-4500.png` |
| `deploying-identity-v2-crewneck` | heavyweight crewneck | `deploying-identity-v2-apparel-4500.png` |
| `404-straight-not-found-tote` | canvas tote | `404-tote-4500.png` |
| `faebriq-baseball-cap-pride-rainbow-low-profile-hat` | low-profile unstructured cap, fabric strap | `logo-faebriq-1p35.png` |
| `404-straight-not-found-sticker` | kiss-cut sticker | `404-straight-not-found-sticker-2400.png` |
| `its-not-a-bug-its-me-sticker` | kiss-cut sticker | `its-not-a-bug-its-me-sticker-2400.png` |
| `code-it-serve-it-sticker` | kiss-cut sticker | `code-it-serve-it-sticker-2400.png` |
| `please-hold-sticker` | kiss-cut sticker | `please-hold-rebranding-identity-sticker-2400.png` |
| `deploying-identity-v2-sticker` | kiss-cut sticker | `deploying-identity-v2-sticker-2400.png` |
| `faebriq-sticker-sheet-full-drop` | sticker sheet | `sticker-sheet-2400x3600.png` |

Tees, hoodie and crewneck also carry `logo-faebriq-1p35.png` (about 3 in) on the **left sleeve**, shown where the angle allows.

## Tiers
- **Tier 2:** slots 1-2, all 12 products (24 images).
- **Tier 3:** slots 3-4, only if budget remains.

| Slot | Apparel / tote / cap | Stickers | Sheet |
|---|---|---|---|
| 1 Studio | Flat, centered. Cap 3/4 front | Dark texture, flat | Flat |
| 2 On-model | Worn or carried, 3/4 view | Black laptop lid | In a hand |
| 3 Context | Night street or market. Cap side, strap seen | Hand, US quarter for scale | On laptop, some applied |
| 4 Macro | Print close-up on fabric | Kiss-cut edge | Two designs close up |

Look: 4:5 portrait, 2048x2560, near-black world (#0f0e0c), soft directional light, dark fashion editorial. Never white, light, or cluttered. Models stylish, confident, queer-coded, charismatic, never a bored catalogue pose.

## Method: composite the exact file, then make it physical
Shoot the scene with the product blank, then composite the exact print file. Last round looked pasted on, fix it:
1. **Perspective:** fit the print to the garment angle and cap crown curve.
2. **Displacement:** warp along the folds, using scene luminance as the displacement map.
3. **Shading:** multiply scene light and shadow over the print, so folds cross the ink. White stays just below pure white in shadow.
4. **Focus:** match scene sharpness and grain. No halo, no hard cut edge.
5. **Scale:** chest 10 in (tees), 11 in (hoodie, crewneck). Tote 10 in. Cap 3.5 to 4 in. Sleeve 3 in.

## Reject and redo if any of these apply
1. Text differs from the file, or FÆBRIQ loses its **Æ**.
2. Stripe order wrong (red left, purple right), a gradient, or narrower than the text.
3. Stitching or embroidery texture.
4. Print is a flat rectangle on a curve, ignores folds or perspective, has a halo, or floats.
5. White or light background, or clutter.
6. Blank isn't black, wrong garment, or malformed hands or bodies.

## Printify (via connector)
- **One approval, not twelve.** Read all 12 products, then send Maurice one table: product, print area and position, file, width in inches, sleeve yes/no, current and new cost if exposed. He approves once, then you execute. Ask only on deviations.
- **Upload by URL**, not from the device. Base plus file name:
  `https://raw.githubusercontent.com/mknuever-lgtm/FAEBRIQ/claude/hopeful-goldberg-a40dkh/assets/print-art/system-2026-09-25/`
  This avoids the file chooser failure.
- **Placement:** read each product's real print area size and position names from the connector. Scale = target width / print area width. Targets: chest 10 in (tees), 11 in (hoodie, crewneck), tote 10 in, cap 3.5 to 4 in, sleeve 3 in. Stickers fill their area. Chest art centered, top edge 0.5 in below the print area top.
- **Sleeve:** only if the product already has a sleeve position. Never change blueprint or provider.
- **Publish** with title, description, tags and images/mockups false. Push variants only. Prices unchanged.
- **Record** the sticker sheet print area size and cost before and after in `Final_report.md`.

## Delivery
- New branch `muse/imagery-2026-09-25`, folder `assets/product-images/2026-09-25/`.
- Files `{handle}-slot{N}.jpg`, 2048x2560, JPG quality 92.
- `Final_report.md` in the same folder: one row per product (slots done, flags, skipped), plus sticker sheet area size and Printify costs.
- Don't push to any other branch. No Shopify.

## Hard rules
- No purchases. No Shopify. No store, theme, price or product changes.
- No creating or deleting Printify products. No price or variant edits.
- No print files from outside `system-2026-09-25/`. No em or en dashes in any text you write.
