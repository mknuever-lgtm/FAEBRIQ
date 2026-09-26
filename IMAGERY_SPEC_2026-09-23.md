# FAEBRIQ imagery spec, locked 2026/09/23

Decisions by Maurice. Decision board: https://claude.ai/artifact/9zSaBXjVRRWu1AV1kVHdtA

## Locked rules
- **Ratio:** 4:5 for every product image. Make new shots at 2048x2560. The existing 1664x2080 shots stay.
- **Hero:** a clean studio product shot, with the print readable at thumbnail size (about 170px wide).
- **Gallery:** exactly 4 shots per product, in the slot order below.
- **Ground:** the brand's near-black (#0f0e0c family). Dark studio surfaces, dark scenes.
- **Print system (reverted 2026/09/25, supersedes the same-day Inter experiment):** Bodoni Moda, white, for every apparel and tote tagline design. The bar is thin and near-continuous (hairline gaps between the 6 blocks), about 1.03x the widest text line, not the flat 1.35x no-gap bar from the 2026/09/25 Inter experiment.
- **White-vinyl sticker correction, approved 2026/09/26:** The five single sticker masters and the sticker sheet use near-black `#0B0B0D` lettering and FÆBRIQ wordmarks on transparent backgrounds, so the standard white SPOKE kiss-cut substrate supplies the white field. Keep the six-color Pride Circuit bar unchanged. This is a color-only correction. Do not resize, re-space, redraw, or add a black background.
- **Line spacing, IMPORTANT: `tools/make_print_file.py`'s formula is stale, do not regenerate from it.** The committed masters (`404-straight-not-found-v3-light-4500.png`, `code-it-serve-it-light-4500.png`, `off-the-clock-still-iconic-light-4500.png`, `deploying-identity-v2-light-4500.png`) hold hand-pixel-shifted final art from the founder's 2026/09/10 review. Their gaps are NOT reproducible by calling `make_print_file.py` fresh: its `GAP_L1_L2_OF_L1_SIZE` / `GAP_L2_BAR_OF_L2_SIZE` constants were never updated after the 09/10 pixel-shift pass, so a fresh build gives noticeably wider gaps than the shipped files. Current rule on the 4 shared-lockup masters, measured on the pixels: gap1-to-2 = gap2-to-bar = 0.25 x line-1's cap height, on all four. A further tightening pass (Off The Clock's top gap, Code It's top and bottom gaps) is in review as of 2026/09/25, not yet applied to the committed files, candidates pending the founder's pick. **Any future spacing change must be a pixel-shift on the existing master (crop the gap, shift the content below it up, same canvas size), never a re-render**, or it silently discards this approved state (the exact failure the 2026/08/27 "equal-visual-cap" incident already caused once, CHANGELOG 2026-09-08).
- **Logo font, deliberately different from the tagline font:** the FÆBRIQ wordmark (cap front, apparel sleeve) stays in Inter SemiBold, not Bodoni. This isn't drift, it's the original documented rule (PRODUCTION_BRIEF §0): a fine serif blurs at small mark scale, so the wordmark uses a blocky sans while every tagline stays serif. Files unchanged: `logo-faebriq-1p35.png` (cap, wordmark over the stripe) and `wordmark-faebriq-sleeve.png` (sleeve, wordmark alone, no stripe).
- **Wordmark on tagline prints:** FÆBRIQ under the stripe on stickers and the tote only, in Bodoni Moda (matches the sticker system already in place). Tees, hoodie and crewneck carry no wordmark on the chest.
- **Brand spelling:** FÆBRIQ, with the Æ ligature, every time. The old repo mockups (`assets/mockup-*.png`, `FAEBRIQ_*_Mockup*.png`, `model-*-new.png`, `model-flatlay-new.png`) show a garbled wordmark, the circuit logo on slogan products, or an off-brand font. Never use them as a reference or as a product image.
- **Retired 2026/09/25 (same day, superseded by the revert above):** the Inter tagline/sticker/tote/sheet files in `assets/print-art/system-2026-09-25/` and every image Muse generated against them. The logo files in that folder (`logo-faebriq-1p35.png`, `wordmark-faebriq-sleeve.png`) are NOT retired, they're still current.
- **Canonical files, apparel/tote/sticker taglines:** `assets/print-art/404-straight-not-found-v3-light-4500.png` (tee/hoodie/crewneck chest use the matching design of these 4: 404, `code-it-serve-it-light-4500.png`, `off-the-clock-still-iconic-light-4500.png`, `deploying-identity-v2-light-4500.png`), `assets/print-art/404-straight-not-found-v3-tote-4500.png` (tote, new 2026/09/25, same lockup as the sticker), `assets/print-art/sticker-final-system-2026-08-27/*.png` (5 stickers), `assets/print-art/sticker-sheet-serif-2400x3600.png` (sheet, new 2026/09/25).
- **Never:** embroidery claims, em or en dashes.

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
- Slot 1: `Studio product photo of a single white kiss-cut vinyl sticker, flat on a dark textured surface. The attached design in near-black with the six-block rainbow stripe and the small FÆBRIQ wordmark underneath, fully legible, slight gloss.`
- Slot 2: `The attached kiss-cut sticker applied to the lid of a black laptop, centered, soft desk light.`
- Slot 3: `A hand holding the attached kiss-cut sticker next to a US quarter for scale, dark background, sticker sharp and legible including the FÆBRIQ wordmark.`
- Slot 4: `Macro of the kiss-cut sticker edge showing the white border and cut line, design partly in frame, dark surface.`

**Sticker Sheet** slot 3: `A hand holding the FÆBRIQ sticker sheet with five typographic designs, dark background, all designs legible, for scale.`
