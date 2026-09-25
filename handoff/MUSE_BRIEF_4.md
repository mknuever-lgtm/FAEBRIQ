# FÆBRIQ: product images on the new print system (Muse, continuing from Manus)

Paste this whole file into Muse. Written 2026/09/25.

## Where things stand
Manus ran out of credits. It delivered no images and saved nothing in Printify. Start the images from zero. **Printify is your job too**, through your Printify connector. Code It Tee may have had its artwork deleted by Manus, so check it first. You have no Shopify connector, and Shopify isn't your job: Claude does it.

**Order:** Tier 2 images, then Printify, then Tier 3 images.

## Budget rules
- Do only what this brief lists, in tier order.
- No exploring. No Shopify. No storefront browsing.
- Max 2 attempts per image, then keep the best and flag it.
- Never redo finished work.
- If budget runs low, stop, commit what you have, and write the report.

## Inputs
- Repo `mknuever-lgtm/FAEBRIQ`, branch `claude/hopeful-goldberg-a40dkh`, folder `assets/print-art/system-2026-09-25/`. These are the only print files allowed. Never edit their text or proportions.
- Preview of every design: `contact-sheet-on-black.jpg`.

| Shopify handle | Product (all blanks black) | Print file |
|---|---|---|
| `404-straight-not-found-tee` | heavy cotton tee | `404-straight-not-found-apparel-4500.png` |
| `code-it-serve-it-tee` | heavy cotton tee | `code-it-serve-it-apparel-4500.png` |
| `off-the-clock-still-iconic-hoodie` | heavyweight hoodie | `off-the-clock-still-iconic-apparel-4500.png` |
| `deploying-identity-v2-crewneck` | heavyweight crewneck | `deploying-identity-v2-apparel-4500.png` |
| `404-straight-not-found-tote` | canvas tote | `404-tote-4500.png` (same lockup as the 404 sticker, FÆBRIQ under the stripe) |
| `faebriq-baseball-cap-pride-rainbow-low-profile-hat` | low-profile unstructured cap, fabric strap | `logo-faebriq-1p35.png` |
| `404-straight-not-found-sticker` | kiss-cut sticker | `404-straight-not-found-sticker-2400.png` |
| `its-not-a-bug-its-me-sticker` | kiss-cut sticker | `its-not-a-bug-its-me-sticker-2400.png` |
| `code-it-serve-it-sticker` | kiss-cut sticker | `code-it-serve-it-sticker-2400.png` |
| `please-hold-sticker` | kiss-cut sticker | `please-hold-rebranding-identity-sticker-2400.png` |
| `deploying-identity-v2-sticker` | kiss-cut sticker | `deploying-identity-v2-sticker-2400.png` |
| `faebriq-sticker-sheet-full-drop` | sticker sheet | `sticker-sheet-2400x3600.png` |

Tees, hoodie and crewneck also carry `wordmark-faebriq-sleeve.png` (FÆBRIQ alone, no stripe) about 3 in wide at the **bottom of the left sleeve**, **horizontal**: it reads left to right across the sleeve, level when the arm hangs down, about 1 in above the sleeve hem (tees) or the cuff (hoodie, crewneck). Show it where the angle allows.

## Tiers (work in the table's order)
- **Tier 2 (first):** slot 1 and slot 2 for all 12 products. That's 24 images.
- **Printify (second):** see the section below.
- **Tier 3 (last, only if budget remains):** slots 3 and 4, in the same order.

| Slot | Apparel / tote / cap | Stickers | Sheet |
|---|---|---|---|
| 1 Studio | Flat or resting on matte near-black, print centered. Cap at 3/4 front | Flat on a dark textured surface | Flat |
| 2 On-model | Worn or carried, 3/4 view | On a black laptop lid | In a hand |
| 3 Context | Late-night street or market. Cap from the side, strap visible | In a hand next to a US quarter | On a laptop, a few applied |
| 4 Macro | Close-up of the print on the fabric | Kiss-cut edge | Two designs close up |

Look for every image:
- 4:5 portrait, 2048x2560.
- Near-black world (#0f0e0c). Soft directional light, premium dark fashion editorial.
- Never white or light, never clutter.
- Models are stylish, confident, queer-coded and charismatic. No bored catalogue pose.

## Method: composite the exact file, then make it physical
Generate the scene with the product blank but no print, then composite the exact print file. That guarantees correct text. Last round the composites looked **pasted on**. Fix that this time:
1. **Perspective:** match the print to the garment's angle and the cap's crown curve.
2. **Displacement:** warp the print along the fabric's folds, using the scene's own luminance as the displacement map.
3. **Shading:** multiply the scene's light and shadow over the print, so folds and shadows cross the ink. Keep the white slightly below pure white in shadow.
4. **Focus:** match the scene's sharpness and grain. No halo, no hard cut edge.
5. **Scale:** chest print about 10 in wide on tees, 11 in on the hoodie and crewneck. Tote 10 in. Cap 3.5 to 4 in. Sleeve logo 3 in.

## Reject and redo if any of these apply
1. The text differs from the file, or FÆBRIQ loses its **Æ**.
2. The stripe is in the wrong order (red must be on the left, purple on the right), a gradient, or narrower than the text.
3. It shows stitching or embroidery texture.
4. The print is a flat rectangle on a curve, ignores folds or perspective, has a halo, or the product floats in the air.
5. The background is white or light, or the room is cluttered.
6. The blank isn't black, or it's the wrong garment (knit, wool). Hands or bodies are malformed.

## Printify (via your connector)
1. **Read first, change nothing yet.** Fetch all 12 products and record, for each one: print area positions (front, left sleeve and so on) with their sizes in inches, current artwork, and cost per variant if exposed.
2. **One approval.** Send Maurice a single table: product, position, file, target width, sleeve yes/no, cost now. Maurice approves once. Then run all 12 without asking again. Ask only if something differs from the approved table.
3. **Upload by URL**, never from a device: `https://raw.githubusercontent.com/mknuever-lgtm/FAEBRIQ/claude/hopeful-goldberg-a40dkh/assets/print-art/system-2026-09-25/` + file name.
4. **Placement:** scale = target width / print area width.
   - Chest: 10 in on tees, 11 in on the hoodie and crewneck. Centered, top edge about 0.5 in below the top of the print area.
   - Tote: 10 in, centered.
   - Cap: 3.5 to 4 in, centered.
   - Stickers and sheet: fill the area.
   - Left sleeve: `wordmark-faebriq-sleeve.png` at 3 in, **horizontal** (no rotation), placed at the bottom of the sleeve print area, about 1 in above the hem or cuff. **Only if the product already has a sleeve position.** Never change blueprint or provider. If the sleeve area is too narrow for 3 in horizontal, use the largest width that fits and note it.
5. **Publish** with title, description, tags and images/mockups set to **false**. Variants only. No price may change.
6. Record in `Final_report.md`: done per product, sleeve added or not offered, cost before and after, and the sticker sheet's print area size.

## Delivery
- New branch `muse/imagery-2026-09-25`, folder `assets/product-images/2026-09-25/`.
- Files `{handle}-slot{N}.jpg`, 2048x2560, JPG quality 92.
- `Final_report.md` in the same folder: one row per product with slots done, flags per image, and anything skipped.
- Don't push to any other branch. Don't touch Shopify. Claude uploads the images to Shopify after checking.

## Hard rules
- No purchases.
- No store, theme, price or variant changes. No creating or deleting Printify products.
- No print files from outside `system-2026-09-25/`.
- No em or en dashes in any text you write.
