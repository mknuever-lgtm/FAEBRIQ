# FÆBRIQ Vol. 1 — Production Brief

Every SKU · which file · print method · placement · price · what's still needed.

Rainbow (confirmed, do not change): `#E8272A #F47F20 #F9D426 #2AAA42 #1D5BBE #7B3FAA`, segmented bands (6 equal blocks, gaps), never a gradient.

Fonts (confirmed): **Instrument Serif** for statement pieces (Code It Serve It, It's Not A Bug, Off The Clock, Please Hold, mug/phrase headlines). **Mono** for Deploying Identity v2.0 and the 404 terminal subline/code. **Bold blocky** (not serif) on caps — a fine serif blurs in embroidery thread at that scale.

## 1. Catalog at a glance

| Product | Tagline | Font | File | Method | Price |
|---|---|---|---|---|---|
| Tee — HERO | 404: Straight Not Found | Bold number + mono | `assets/print-art/tee-404-straight-not-found.png` | DTG | CA$42 |
| Tee | It's Not A Bug. It's Me. | Instrument Serif | `assets/print-art/tee-its-not-a-bug.png` | DTG | CA$42 |
| Tee | Code It. Serve It. | Instrument Serif | `assets/print-art/tee-code-it-serve-it.png` | DTG | CA$42 |
| Hoodie | Deploying Identity v2.0 | Mono | `assets/print-art/hoodie-deploying-identity.png` | DTG | CA$78 |
| Hoodie | Off The Clock. Still Iconic. | Instrument Serif | `assets/print-art/hoodie-off-the-clock.png` | DTG | CA$78 |
| Tote | Please Hold, I'm Rebranding My Identity | Instrument Serif | `assets/print-art/tote-please-hold.png` | DTG | TBD |
| Mug (replaces Silver Wordmark art) | Please Hold, I'm Rebranding My Identity | Instrument Serif | `assets/mug-please-hold.png` | Sublimation wrap | CA$16.99 / CA$19.99 (11oz/15oz, unchanged) |
| Cap — slim dad cap | GAGGED | Bold blocky | `assets/print-art/cap-gagged-slim.png` | Embroidery | CA$34 |
| Cap — slim dad cap | SERVED. | Bold blocky | `assets/print-art/cap-served-slim.png` | Embroidery | CA$34 |
| Cap — structured/5-panel | GAGGED | Bold blocky | `assets/print-art/cap-gagged-structured.png` | Embroidery | CA$34 |
| Cap — structured/5-panel | SERVED. | Bold blocky | `assets/print-art/cap-served-structured.png` | Embroidery | CA$34 |
| Sticker | 404: Straight Not Found | Bold number + mono | `assets/print-art/tee-404-straight-not-found.png` | Kiss-cut vinyl | CA$5 |

## 2. Standalone listing images (no photography needed)

Pure-typographic "Phrase" type images per the design handoff's 5-image spec (Hero/Detail/Phrase/Lifestyle/Collection) — 1080×1080, black-void `#0d0d0d` background, ready to use as a listing image directly:

- `assets/phrase-404.png` — for the 404 tee listing
- `assets/phrase-deploying-identity.png` — for the Deploying Identity hoodie listing

More can be generated the same way (HTML + Playwright render) for any tagline — no external tool needed, ask for one.

## 3. Tees & hoodies — DTG settings

- **Blank:** heavyweight black tee / fleece hoodie — match the CA$42/$78 positioning, not the cheapest blank.
- **Print method:** DTG — renders the six-color band + fine serif/mono text cleanly on black. Not screen-print (too many colors).
- **Placement:** front, centered, ~26–28cm wide. The 404 hero art is left-aligned by design — place as a large left-chest-to-center block, ~28–30cm wide, so the big `404` and the terminal subline both read.
- **Colors:** confirm the Printify preview shows the exact ROYGBIV band values above.

## 4. Caps — two silhouettes, both done

- **Slim/unstructured dad cap** (primary) — soft low crown, curved brim. Use the `-slim` files (smaller, discreet front hit).
- **Structured/5-panel** (secondary) — bigger front real estate. Use the `-structured` files (larger, bolder front hit).
- Both already use the embroidery-safe band (thicker segments, wider gaps than the print files) — no further tweaking needed before ordering.
- Brand tie-in: front carries the one word only; tuck "Code It. Serve It." tiny on the back/strap if desired.

## 5. Mug & tote — new this revision

- **Mug:** `assets/mug-please-hold.png` is sized for a mug-wrap-safe centered layout (avoid handle-adjacent edges). Needs a sublimation/wrap print method in Printify.
  **Confirmed: replaces the existing "Silver Wordmark" mug art**, not a new SKU. This product is **Printify-linked** (`printify_custom.printify_product_id = 6a14e7a6cb8516b5720c68fb` on `gid://shopify/Product/7681278017603`) — its own Shopify description already reads "Please Hold, I'm Rebranding My Identity," so the copy update happened but the art didn't. **The image MUST be swapped in Printify, not uploaded directly to Shopify** — Printify's periodic sync back to Shopify will overwrite any image set manually there. Keep the existing price points (CA$16.99 / CA$19.99, 11oz/15oz) unless a reprice is wanted — consider renaming the listing to drop "Silver Wordmark" once the art changes, since that name describes the old design.
  This same rule applies to every other SKU in this brief: all are Printify-fulfilled, so **every image swap in §1 goes through Printify**, never a direct Shopify image upload.
- **Tote:** `assets/print-art/tote-please-hold.png` — same art, larger canvas tote-tile size. DTG or screen-print depending on the blank.

## 6. Stickers

- Kiss-cut vinyl, ~7–8cm wide. `tee-404-straight-not-found.png` works as-is — the terminal-error styling is made for a laptop lid. Consider a sticker sheet later (error-code deep cuts: 418 Teapot, 500 Serving Error, etc.).

## 7. Exact click-path in Printify

1. Catalog → pick the blank.
2. Start designing → upload the matching file from §1.
3. Position & size per §3–6. Check the print preview for band color + text sharpness.
4. Select variants — tees/hoodies: S–XL, black only. Cap: one size per silhouette. Sticker/mug/tote: one size.
5. Set price per §1. Printify shows the margin.
6. Publish to Shopify — lands as a draft with Printify's auto-mockup.
7. In Shopify, swap in the Placeit on-model hero image (§8), then set the product Active.

## 8. Elite photos — Placeit pass (after Printify)

Printify's auto-mockups get every listing sellable but look generic. For the dark-editorial "designer" look:

1. Upload the same files to Placeit/Smartmockups.
2. Composite onto dark, on-model/lifestyle templates (matches the mockups already validated).
3. Download and set as product image #1 (hero) in Shopify.

Follow the brand rules: black void background, cool grade, on-model is non-negotiable, 5 images per listing when time allows (Hero/Detail/Phrase/Lifestyle/Collection — see §2 for the Phrase images already done).

## 9. Still outside this repo / needs the founder's action

- Printify upload, variant setup, and pricing (no Printify API access in this session)
- Placeit/Smartmockups compositing (no API access in this session)
- Second cap silhouette's on-model product photo (art is done; photo is not)
- Full 5-image sets (Hero/Detail/Lifestyle/Collection) for every SKU beyond the two Phrase images above

## 10. Shopify copy cleanup (done directly in Shopify, safe — no Printify conflict)

Found and fixed live on 2026-07-05: four product descriptions still contained internal placeholder/dev text visible to customers.

- **Deploying Identity Hoodie** (`.../7707663302723`) — removed `[DRAFT, final hoodie print art pending]`
- **Code It, Serve It. Hoodie** (`.../7707663335491`) — removed the same placeholder; also swapped "glitch-rainbow" language for "pride-circuit spine" to match the confirmed segmented-band aesthetic (not a gradient/glitch effect)
- **Please Hold Tee** (`.../7707664187459`) — removed `[DRAFT, final tee print art pending]`; "subway line rainbow" → "pride-circuit spine" for the same reason
- **Circuit Cap** (`.../7707664973891`) — removed `[DRAFT, final embroidery art pending]` **and** an internal sourcing note ("Confirm Printify/Monster Digital blank before launch. First unit doubles as founder's personal cap..."); rewrote the front-design description from "AE ligature wordmark" (superseded) to **GAGGED** in bold block type, matching the confirmed cap decision — no brand wordmark on the front, punchline leads

These were description/copy edits only (title, descriptionHtml) — no images touched, consistent with §9's rule that images must go through Printify.

---
v4 — Shopify copy cleanup: stripped customer-visible dev placeholders from 4 listings, corrected cap description to match the confirmed GAGGED design (see §10). v3 — mug confirmed as a replacement for the existing Silver Wordmark SKU, not a new product (see §5). v2 superseded the chat-only brief: font corrected to Instrument Serif for statement pieces (was mono/plain-sans in earlier drafts), mug + Phrase images added.
