# FAEBRIQ imagery spec, locked 2026/09/23

Decisions by Maurice. Decision board: https://claude.ai/artifact/9zSaBXjVRRWu1AV1kVHdtA

## Locked rules
- **Ratio:** 4:5 for every product image. Make new shots at 2048x2560. The existing 1664x2080 shots stay.
- **Hero:** a clean studio product shot, with the print readable at thumbnail size (about 170px wide).
- **Gallery:** exactly 4 shots per product, in the slot order below.
- **Ground:** the brand's near-black (#0f0e0c family). Dark studio surfaces, dark scenes.
- **Lockup:** serif caps (Instrument Serif), line 2 smaller than line 1, a flat six-block rainbow stripe underneath. Source: the current masters in `assets/print-art/*-light-4500.png`, which match the "75% (current)" variant.
- **Stickers:** FÆBRIQ small, centered under the stripe. Required on every sticker. All 5 files in `assets/print-art/sticker-final-system-2026-08-27/` already have it (checked 2026/09/23).
- **Brand spelling:** FÆBRIQ, with the Æ ligature, every time. The old repo mockups (`assets/mockup-*.png`, `FAEBRIQ_*_Mockup*.png`, `model-*-new.png`, `model-flatlay-new.png`) show a garbled wordmark, the circuit logo on slogan products, or an off-brand font. Never use them as a reference or as a product image.
- **404 design (canonical, set 2026/09/23):** a big "404" on top, "STRAIGHT NOT FOUND" on one line underneath, then the flat stripe (plus FÆBRIQ on stickers). Reference: `assets/print-art/reference/404-canonical-reference-2026-09-23.webp`. Print files: `assets/print-art/404-straight-not-found-v3-light-4500.png` (apparel, tote) and `assets/print-art/sticker-final-system-2026-08-27/404-straight-not-found-v3-sticker-light-2400.png` (sticker), made with `tools/make_404_v3.py`. The "ERROR 404 / STRAIGHT NOT / FOUND" files are retired.
- **Never:** embroidery claims, em or en dashes, the condensed bold sans (seen in `model-tee-new.png` and `model-flatlay-new.png`), or the old "big 404 + italic line" design.

## Slot system
| Slot | Job | Apparel | Cap | Tote | Single sticker | Sticker sheet |
|---|---|---|---|---|---|---|
| 1 Hero | Sells in the thumbnail | Studio flat or ghost, print centered | Studio 3/4 front | Studio front, flat | Flat on dark studio surface | Full sheet flat |
| 2 On-model | Fit and scale on a body | Model, 3/4 | Worn, 3/4 | On shoulder | On a laptop lid | On a laptop, some applied |
| 3 Context | Size and real-life use | Lifestyle scene | Side view with strap | Carried at a market | In hand, next to a coin | In hand, for scale |
| 4 Macro | Proves print quality | Print and stripe close-up | Front print close-up | Print and strap close-up | Kiss-cut edge close-up | Macro of the designs |

## Status per live product
| Product | Slots done | To do |
|---|---|---|
| Deploying Identity Crewneck | 1, 2, 3, 4 | Visual check that the print matches the lockup |
| Off The Clock Hoodie | 1, 2, 3, 4 | Visual check that the print matches the lockup |
| Not A Bug, Code It, Please Hold, Deploying stickers | 1, 2, 4 (reordered 2026/09/23: flat is now first) | Slot 3 (in hand). Check that FÆBRIQ shows on the rendered sticker |
| Sticker Sheet | 1, 2, 4 (flat moved first 2026/09/23; spare detail shot sits at 3) | Slot 3 (in hand), which then replaces the spare |
| 404 Sticker | none usable (square 1200px Printify) | Check against the canonical 404, swap to v3 if different, then all 4 slots in the sticker system |
| 404 Tee | none usable (square) | Check against the canonical 404, swap to v3 if different, then all 4 slots |
| 404 Tote | none usable (square) | Check against the canonical 404, swap to v3 if different, then all 4 slots |
| Code It Tee | none usable (square) | Check the print lockup, then all 4 slots |
| Circuit Cap, Low Profile | none usable (square) | All 4 slots (logo product: the circuit wordmark stays on the cap) |

## Theme dependency (done 2026/09/23, on the unpublished theme)
The 4:5 card and mobile gallery ratio is set in `faebriqtheme-launch-fix` (UNPUBLISHED), inside `assets/faebriq.css` only:
- `.fae-card__image` is now `aspect-ratio: 4/5;`
- The mobile media query has `.fae-product .fae-gallery__main { aspect-ratio: 4 / 5; }`, which overrides the `1 / 1` rule in `templates/product.liquid` without editing that file.

The live theme is `faebriqtheme-launch-2026-08-06-review`. It shows the change only once launch-fix is published.

## Print file swaps (Maurice, in Printify, manual)
Compare each live 404 product to the canonical reference. If it matches (one-line STRAIGHT NOT FOUND in upright serif caps under a big 404), keep it. If it shows an italic line, or the retired ERROR 404 layout, swap it:
- 404 Tee: `assets/print-art/404-straight-not-found-v3-light-4500.png`
- 404 Tote: `assets/print-art/404-straight-not-found-v3-light-4500.png`
- 404 Sticker: `assets/print-art/sticker-final-system-2026-08-27/404-straight-not-found-v3-sticker-light-2400.png`
- Code It Tee: open it and compare to `code-it-serve-it-light-4500.png`. Swap it if it shows the circuit wordmark instead.

**Do not press Publish in Printify.** It overwrites Shopify edits (titles, alt text, image order). Save the design in Printify only, then upload the new images to Shopify by hand.

Side note: `sticker-validation.json` records the 404 sticker at 2400x1397. The file on disk is 2400x1280. Re-run validation before uploading it.

## Generation prompts
Attach the product's print file as the reference image in every prompt. Replace the `{}` fields.
Output for every shot: 4:5, 2048x2560, photographic, no text other than the print.

**Apparel** (`{garment}` = black heavy cotton unisex tee / heavyweight crewneck / heavyweight hoodie)
- Slot 1: `Studio product photo of a {garment}, laid flat, centered, on a matte near-black surface (#0f0e0c). The attached print is screen-printed in white on the chest with its six-color rainbow stripe, sharp and fully legible. Soft top light, subtle shadow, no props.`
- Slot 2: `Editorial fashion photo, 3/4 view, model wearing a {garment} with the attached white chest print and six-color rainbow stripe clearly visible. Dark urban night setting, cool rim light, confident relaxed pose, print unobstructed.`
- Slot 3: `Lifestyle photo of a person in a {garment} with the attached print, at a {setting: developer workstation / queer art market / late-night street}. Moody low light, print legible, candid.`
- Slot 4: `Macro close-up of the attached white print and flat six-block rainbow stripe on black cotton, showing fabric weave and print edge. Shallow depth of field.`

**404 Tote** (AS Colour 1001, black)
- Slot 1: `Studio product photo of a black cotton canvas tote bag, front, flat, on a matte near-black surface. The attached print in white with the six-color rainbow stripe, centered, fully legible.`
- Slot 2: `Model carrying the black canvas tote on one shoulder, 3/4 view, the attached print facing camera, dark editorial setting.`
- Slot 3: `The black tote carried through an evening art market, print legible, candid, warm string lights against a dark background.`
- Slot 4: `Macro of the white print and six-block rainbow stripe on black canvas, strap seam visible at the frame edge.`

**Circuit Cap, Low Profile** (OTTO 18-253 black, printed DTF, never embroidered)
- Slot 1: `Studio product photo of a black low-profile unstructured baseball cap, 3/4 front, on a matte near-black surface. White FÆBRIQ wordmark with the six-color rainbow stripe printed flat on the front panel.`
- Slot 2: `Model wearing the black low-profile cap, 3/4 view, the front print visible, dark editorial light.`
- Slot 3: `Side view of the black low-profile cap showing the curved brim and the adjustable strap closure, dark studio.`
- Slot 4: `Macro of the printed white wordmark and rainbow stripe on the cap front, showing the flat print surface.`

**Stickers** (`{design}` = sticker print file; FÆBRIQ must be visible under the stripe)
- Slot 1: `Studio product photo of a single kiss-cut vinyl sticker, flat on a dark textured surface. The attached design in white with the six-block rainbow stripe and the small FÆBRIQ wordmark underneath, fully legible, slight gloss.`
- Slot 2: `The attached kiss-cut sticker applied to the lid of a black laptop, centered, soft desk light.`
- Slot 3: `A hand holding the attached kiss-cut sticker next to a US quarter for scale, dark background, sticker sharp and legible including the FÆBRIQ wordmark.`
- Slot 4: `Macro of the kiss-cut sticker edge showing the white border and cut line, design partly in frame, dark surface.`

**Sticker Sheet** slot 3: `A hand holding the FÆBRIQ sticker sheet with five typographic designs, dark background, all designs legible, for scale.`
