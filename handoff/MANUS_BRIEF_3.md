# FÆBRIQ: rebuild every product on the new print system, then take the store live

Paste this whole file into Manus as the task brief. Written 2026/09/25.

**Do not stop until every active product is correct, beautiful and live on faebriq.com.** When something blocks you, work around it, try the next route, and log it. Only the hard rules at the bottom may stop you. If one of those blocks you, finish every other product first, then report.

---

## 0. Accounts and files

- **Printify:** log in with **m.knuever@mkglobalhorizons.com**, using email and password. **Not "Continue with Google".** The Google login opens an empty account.
- **Shopify admin:** faebriq.com. The store sells in USD and ships to the US and Canada only.
- **Print files:** GitHub, repo `mknuever-lgtm/FAEBRIQ`, branch `claude/hopeful-goldberg-a40dkh`, folder `assets/print-art/system-2026-09-25/`. Raw download base:
  `https://raw.githubusercontent.com/mknuever-lgtm/FAEBRIQ/claude/hopeful-goldberg-a40dkh/assets/print-art/system-2026-09-25/`
  Append the file name. Preview everything at once: `contact-sheet-on-black.jpg`.

### The new print system (applies to every product)
- Font: Inter SemiBold, white.
- Line 2 is 58 to 85% the size of line 1, set per design. Never resize or rebalance the files.
- A flat six-block rainbow pride stripe sits under the text: red, orange, yellow, green, blue, purple, left to right. It is exactly 1.35x as wide as the widest text line.
- **FÆBRIQ wordmark under the stripe:** stickers and tote only.
- **Tees, hoodie, crewneck:** no wordmark in the chest print. The FÆBRIQ logo goes on the left sleeve.
- Never use any older print file (Bodoni serif, "ERROR 404", italic lines, `cap-wordmark-slim/structured`, anything in `assets/print-art/` outside `system-2026-09-25/`).

## 1. Before you touch anything: snapshot

In Shopify admin, record for every active product: title, price of every variant, the full description, status. Save it as your baseline. You will compare against it at the end.

## 2. Printify: apply the files

For each product below: open it in Printify, **Edit design**, remove the old artwork, upload the new file, place it, **Save**. Don't publish yet.

| Shopify product | Print location: file |
|---|---|
| FÆBRIQ '404: Straight Not Found' Tee | Front: `404-straight-not-found-apparel-4500.png`. Left sleeve: `logo-faebriq-1p35.png` |
| FÆBRIQ 'Code It. Serve It.' Tee | Front: `code-it-serve-it-apparel-4500.png`. Left sleeve: `logo-faebriq-1p35.png` |
| FÆBRIQ 'Deploying Identity v2.0' Heavyweight Crewneck | Front: `deploying-identity-v2-apparel-4500.png`. Left sleeve: `logo-faebriq-1p35.png` |
| FÆBRIQ 'Off The Clock. Still Iconic.' Heavyweight Hoodie | Front: `off-the-clock-still-iconic-apparel-4500.png`. Left sleeve: `logo-faebriq-1p35.png` |
| FÆBRIQ '404: Straight Not Found' Cotton Tote | Front: `404-tote-4500.png` |
| FÆBRIQ Circuit Cap, Low Profile (Black) | Front: `logo-faebriq-1p35.png` |
| FÆBRIQ '404: Straight Not Found' Sticker | `404-straight-not-found-sticker-2400.png` |
| FÆBRIQ "It's Not A Bug. It's Me." Sticker | `its-not-a-bug-its-me-sticker-2400.png` |
| FÆBRIQ 'Code It. Serve It.' Sticker | `code-it-serve-it-sticker-2400.png` |
| FÆBRIQ 'Please Hold, I'm Rebranding My Identity' Sticker | `please-hold-rebranding-identity-sticker-2400.png` |
| FÆBRIQ 'Deploying Identity v2.0' Sticker | `deploying-identity-v2-sticker-2400.png` |
| FÆBRIQ Sticker Sheet: The Full Drop | `sticker-sheet-2400x3600.png`. If Printify's sheet template has its own slots, place the 5 single sticker files instead, one per slot, same order |

Placement:
- **Chest (tees, crewneck, hoodie):** centered horizontally, top of the art about 3 in below the collar. About 10 in wide on tees, 11 in on the crewneck and hoodie.
- **Sleeve logo:** left sleeve, centered, about 3 in wide. **If a product's provider has no sleeve location, don't switch providers.** Note it in the report and carry on.
- **Tote:** centered, about 10 in wide.
- **Cap:** centered on the front panel, 3.5 to 4 in wide. It's a DTF print. Never write "embroidered" or "embroidery" anywhere.
- **Stickers:** fill the sticker, keep Printify's kiss-cut border.

**Cost check:** a sleeve print can raise Printify's cost. Record the old and new cost for every product. **Don't change any retail price.**

The Slim Cap is archived. Leave it alone.

## 3. Product images: 4 per product

Every product gets exactly 4 images, in this order. All are **4:5 portrait, 2048x2560**, photographic, and set in the store's world: near-black (#0f0e0c family), moody and premium, like a dark fashion editorial. **Never white, never light grey, never a cluttered room.**

| Slot | Apparel | Tote | Cap | Single sticker | Sticker sheet |
|---|---|---|---|---|---|
| 1 Studio (required) | Flat lay or ghost on matte near-black, print centered and sharp | Front, flat, on near-black | 3/4 front, resting on a near-black surface | Flat on a dark textured surface | Full sheet flat |
| 2 On-model (required) | Model, 3/4 view, dark editorial light | On one shoulder | Worn, 3/4 view | Applied to a black laptop lid | On a laptop, a few applied |
| 3 Context | Lifestyle: late-night street, dev desk, queer art market | Carried through an evening market | Side view, brim and strap closure | In hand next to a US quarter | In hand for scale |
| 4 Macro | Print and stripe close-up on the fabric | Print and strap seam | Front print close-up | Kiss-cut edge close-up | Close-up of 2 designs |

**How to generate:** attach the product's exact print file to every prompt as the reference. Prompt template:
`Photographic product image, 4:5 portrait. {slot description}. The attached artwork is printed on the {black heavy cotton tee / heavyweight crewneck / heavyweight hoodie / black canvas tote / black low-profile cap / kiss-cut vinyl sticker} exactly as supplied: white Inter SemiBold text, a flat six-block rainbow stripe underneath (red, orange, yellow, green, blue, purple from left to right). The print follows the fabric's curve and folds and sits in the weave. Near-black background (#0f0e0c), soft directional light, premium dark editorial mood. No other text or logos.`
Apparel slots 1 and 2 should also show the small FÆBRIQ logo on the left sleeve where the angle allows.

Models: varied, stylish, confident, queer-coded, at ease. Charisma, not a bored catalogue pose.

### Reject list. Check every image against all of it before using it. Regenerate on any hit.
1. The print text differs from the file in any way: spelling, a missing **Æ** (FAEBRIQ, FABRIQ and FÆBRlQ are all fails), extra words, a changed line break.
2. Wrong stripe order (it must be red on the left, purple on the right), a gradient instead of 6 flat blocks, or a stripe narrower than the text.
3. Any stitch, thread or embroidery texture. These are prints.
4. The print looks pasted on: a perfectly flat rectangle on a curved cap or folded fabric, ignoring seams, or with a glow or hard halo.
5. The product floats in mid-air, or its shape is impossible (buckles that don't exist, melted hands, extra fingers).
6. A white or light background, or visible domestic clutter.
7. The wrong garment: knit or wool instead of cotton, the wrong colour (every blank is black).
8. A wordmark on the apparel chest print (the sleeve only), or a missing wordmark on stickers and the tote.
9. Blurry print, or print that can't be read at thumbnail size in slot 1.

If a slot keeps failing after 3 honest tries, use the strongest compliant image for that slot and flag it in the report. **Slots 1 and 2 may never be skipped.**

## 4. Publish from Printify, safely

Printify's Publish overwrites Shopify edits. Before you press it on each product:
1. Open the publish settings and **uncheck Title, Description, Tags, and Mockups/Images**. Leave only what's needed to push the design and variants.
2. If Printify's retail price differs from the Shopify price in your snapshot, set Printify's price to the snapshot price first.
3. Publish.

## 5. Shopify: images and final check

For each product in Shopify admin:
1. Delete **all** old images: Printify mockups, the 2026-09-24 set, everything.
2. Upload your 4 new images in slot order.
3. Alt text on every image: plain words, no dashes of any kind, no "embroider". Mention "rainbow pride stripe". Pattern:
   `FÆBRIQ {product} in black with the white "{text}" print and rainbow pride stripe, {slot: studio flat lay / worn by a model / at a late-night market / print close-up}`
4. Compare the title, every variant price, the description and the status to your snapshot. Fix any drift back to the snapshot.

Then open faebriq.com in a private window and check the home page, the collection page and every product page on desktop and phone width. Every product must show its 4 new images, and nothing may show an old design.

## 6. Hard rules. These may stop you.

- **No purchases and no sample orders.** If one seems necessary, stop and ask Maurice, showing the checkout screen.
- **Don't publish, edit or switch Shopify themes.** Claude handles the theme.
- **Don't create products, delete products, change prices, change handles or SEO, or edit collections.**
- **Don't use any print file outside `system-2026-09-25/`.**

## 7. Final report (required)

One table, one row per product: Printify saved (yes/no), sleeve logo added (yes/no/not offered), old cost, new cost, published (yes/no), 4 images live (yes/no), flagged slots, and any snapshot drift fixed. Then list every workaround you used and anything left open. Push nothing to GitHub.
