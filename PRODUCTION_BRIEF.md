# FÆBRIQ Vol. 1 — Production Brief

Every SKU · which file · print method · placement · price · what's still needed.

Rainbow (confirmed, do not change): `#E8272A #F47F20 #F9D426 #2AAA42 #1D5BBE #7B3FAA`, segmented bands (6 equal blocks, gaps), never a gradient.

Fonts (confirmed, all-serif as of v6): **Instrument Serif** for every tagline, no exceptions — including "Deploying Identity v2.0," which previously used mono. A small **mono** "FÆBRIQ" kicker sits under every design. **Bold blocky** (not serif) stays on caps only — a fine serif blurs in embroidery thread at that scale; the cap uses the wordmark, not a tagline, so this doesn't conflict.

## 1. Catalog at a glance

Every tagline below ships in **two color variants** — Black-on-White (for lighter garments) and White-on-Black (for black garments, the default). Pick per garment color at Printify upload time.

| Product | Tagline | File (white-on-black) | File (black-on-white) | Method | Price |
|---|---|---|---|---|---|
| Tee — HERO | 404: Straight Not Found | `404-straight-not-found-white-on-black.jpg` | `404-straight-not-found-black-on-white.jpg` | DTG | CA$42 |
| Tee | It's Not A Bug. It's Me. | `its-not-a-bug-its-me-white-on-black.jpg` | `its-not-a-bug-its-me-black-on-white.jpg` | DTG | CA$42 |
| Tee | Code It. Serve It. | `code-it-serve-it-white-on-black.jpg` | `code-it-serve-it-black-on-white.jpg` | DTG | CA$42 |
| Hoodie | Deploying Identity v2.0 | `deploying-identity-v2-white-on-black.jpg` | `deploying-identity-v2-black-on-white.jpg` | DTG | CA$78 |
| Hoodie | Off The Clock. Still Iconic. | `off-the-clock-still-iconic-white-on-black.jpg` | `off-the-clock-still-iconic-black-on-white.jpg` | DTG | CA$78 |
| Tote / Tee (new SKU — see §5a) | GAGGED | `gagged-white-on-black.jpg` | `gagged-black-on-white.jpg` | DTG | TBD |
| Tote / Tee (new SKU — see §5a) | SERVED. | `served-white-on-black.jpg` | `served-black-on-white.jpg` | DTG | TBD |
| Tote | Please Hold, I'm Rebranding My Identity | `please-hold-rebranding-identity-white-on-black.jpg` | `please-hold-rebranding-identity-black-on-white.jpg` | DTG | TBD |
| Mug (replaces Silver Wordmark art) | Please Hold, I'm Rebranding My Identity | `assets/mug-please-hold.png` (own file, mug-wrap-safe crop) | — | Sublimation wrap | CA$16.99 / CA$19.99 (11oz/15oz, unchanged) |
| Cap — slim dad cap | FÆBRIQ wordmark | `assets/print-art/cap-wordmark-slim.png` | — | Embroidery | CA$34 |
| Cap — structured/5-panel | FÆBRIQ wordmark | `assets/print-art/cap-wordmark-structured.png` | — | Embroidery | CA$34 |
| Sticker | 404: Straight Not Found | `404-straight-not-found-white-on-black.jpg` | — | Kiss-cut vinyl | CA$5 |

All tagline files live in `assets/print-art/`. The cap and mug files are separate, purpose-built assets (not part of the two-color set) — see §4 and §5.

## 2. Standalone listing images (no photography needed)

Pure-typographic "Phrase" type images per the design handoff's 5-image spec (Hero/Detail/Phrase/Lifestyle/Collection) — 1080×1080, black-void `#0d0d0d` background, ready to use as a listing image directly:

- `assets/phrase-404.png` — for the 404 tee listing
- `assets/phrase-deploying-identity.png` — for the Deploying Identity hoodie listing

These predate the v6 all-serif rule and still use mono for "Deploying Identity" — cosmetic inconsistency only, not urgent to fix, but regenerate to match if convenient. More can be generated the same way (HTML + Playwright render) for any tagline — no external tool needed, ask for one.

## 3. Tees & hoodies — DTG settings

- **Blank:** heavyweight black (or white/light, if using a Black-on-White variant) tee / fleece hoodie — match the CA$42/$78 positioning, not the cheapest blank.
- **Print method:** DTG — renders the six-color band + fine serif text cleanly on either garment color. Not screen-print (too many colors).
- **Placement:** front, centered, ~26–28cm wide.
- **Color variant:** use White-on-Black for black garments, Black-on-White for light garments — don't mix (white text is invisible on a white tee).
- **Colors:** confirm the Printify preview shows the exact ROYGBIV band values above.

## 4. Caps — two silhouettes, unaffected by this revision

**Final direction:** wordmark cap, segmented band above "FÆBRIQ" — matches the reference photo that sold the founder on execution quality, built with the confirmed segmented band instead of a gradient line. GAGGED/SERVED were considered for the cap specifically and dropped — the wordmark reads cleaner to strangers who don't yet know the brand, and keeps the cap visually consistent with the rest of the line.

- **Slim/unstructured dad cap** (primary) — soft low crown, curved brim. Use `cap-wordmark-slim.png`.
- **Structured/5-panel** (secondary) — bigger front real estate. Use `cap-wordmark-structured.png`.
- Both use the embroidery-safe band (thicker segments, wider gaps than the tagline print files) — no further tweaking needed before ordering.

## 5. Mug & tote

- **Mug:** `assets/mug-please-hold.png` is sized for a mug-wrap-safe centered layout (avoid handle-adjacent edges). Needs a sublimation/wrap print method in Printify.
  **Confirmed: replaces the existing "Silver Wordmark" mug art**, not a new SKU. This product is **Printify-linked** (`printify_custom.printify_product_id = 6a14e7a6cb8516b5720c68fb` on `gid://shopify/Product/7681278017603`). **The image MUST be swapped in Printify, not uploaded directly to Shopify** — Printify's periodic sync back to Shopify will overwrite any image set manually there. Keep the existing price points (CA$16.99 / CA$19.99, 11oz/15oz) unless a reprice is wanted; consider renaming the listing to drop "Silver Wordmark" once the art changes.
  This same rule applies to every other SKU in this brief: all are Printify-fulfilled, so **every image swap in §1 goes through Printify**, never a direct Shopify image upload.
- **Tote:** use `please-hold-rebranding-identity-*.jpg` as the primary tote design (matches the zip's original naming — this set was delivered specifically for tote text/color adjustment). GAGGED and SERVED are also candidates for tote (see §5a).

### 5a. GAGGED / SERVED — new SKUs, not yet priced or listed

Per the founder: these are tee/tote designs now, **not** the cap (cap direction is settled — see §4). They don't map to any existing Shopify product yet. Open decisions before these go into Printify:
- Which product(s) — tee only, tote only, or both?
- Pricing — tee would likely be CA$42 (matching the other tees), tote TBD alongside the Please Hold tote.
- New Shopify listing needed for each (title, description, tags) — none exists today.

## 6. Stickers

- Kiss-cut vinyl, ~7–8cm wide. `404-straight-not-found-white-on-black.jpg` works as-is — the terminal-error styling is made for a laptop lid. Consider a sticker sheet later (error-code deep cuts: 418 Teapot, 500 Serving Error, etc.), and possibly GAGGED/SERVED as small sticker call-outs too.

## 7. Exact click-path in Printify

1. Catalog → pick the blank (confirm garment color to pick the matching White-on-Black or Black-on-White file).
2. Start designing → upload the matching file from §1.
3. Position & size per §3–6. Check the print preview for band color + text sharpness.
4. Select variants — tees/hoodies: S–XL. Cap: one size per silhouette. Sticker/mug/tote: one size.
5. Set price per §1 (or decide new pricing for GAGGED/SERVED, §5a).
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
- GAGGED/SERVED product/pricing decisions (§5a)
- Regenerating the two Phrase images (§2) to match the v6 all-serif rule (cosmetic, low priority)

## 10. Shopify copy cleanup (done directly in Shopify, safe — no Printify conflict)

Found and fixed live on 2026-07-05: four product descriptions still contained internal placeholder/dev text visible to customers.

- **Deploying Identity Hoodie** (`.../7707663302723`) — removed `[DRAFT, final hoodie print art pending]`
- **Code It, Serve It. Hoodie** (`.../7707663335491`) — removed the same placeholder; also swapped "glitch-rainbow" language for "pride-circuit spine" to match the confirmed segmented-band aesthetic (not a gradient/glitch effect)
- **Please Hold Tee** (`.../7707664187459`) — removed `[DRAFT, final tee print art pending]`; "subway line rainbow" → "pride-circuit spine" for the same reason
- **Circuit Cap** (`.../7707664973891`) — removed `[DRAFT, final embroidery art pending]` **and** an internal sourcing note. Description went through two revisions before landing on the final direction: **FÆBRIQ wordmark + segmented band** (see §4).

## 11. Shopify catalog synced to v6 tagline map (2026-07-07)

Text-only updates (title/description), no images/SKUs touched — those stay Printify's job per §5:

- **Hoodie #2** (`.../7707663335491`) renamed from "Code It, Serve It." → **"Off The Clock. Still Iconic."** to match its brief slot.
- **Tee** (`.../7707664187459`) repurposed from "Please Hold" → **"Code It. Serve It."** — this listing had no real photo/SKU yet, so relabeling was safe. (The other tee, "Deploying Identity v2.0" `.../7682131034179`, already has real Printify art/SKUs and was **left untouched** — it doesn't match any tee slot in the v6 table, since "Deploying Identity v2.0" is hoodie-only there. Renaming it would mismatch title against its live photo. Needs a founder decision: keep it as a bonus tee SKU, or retire once "It's Not A Bug" / "404" tees exist.)
- **Totes** — consolidated 2 → 1. `.../7707665104963` renamed to **"Please Hold, I'm Rebranding My Identity" Tote** and its stale `[DRAFT]` copy cleaned up; the redundant "Deploying Identity v2.0" tote (zero content) was deleted.
- **Mug** (`.../7681278017603`) renamed from "Silver Wordmark" → **"Please Hold, I'm Rebranding My Identity"**, description updated. Art swap is still a Printify task per §5.
- **Stickers** — the 3 existing tagline stickers (Deploying Identity, Please Hold, Code It Serve It) were **left untouched** for the same reason as the tee above: they already have real Printify-linked art matching their current titles. The brief's "404: Straight Not Found" sticker is a separate, not-yet-created listing.
- **Sticker bundle** (`.../7682175238211`) renamed to "Sticker Bundle — The Full Drop", restructured with a **Bundle Size** option: 3-Pack ($11, existing) and new 5-Pack ($16 — best per-sticker price, ships today using 2 duplicate designs until 404/GAGGED/SERVED stickers exist). All 3 single-sticker listings' copy updated to position stickers as an apparel add-on.
- Duplicate cap listing ("Technical Cap V1.0") and the stray "General Clothes example products" collection were deleted earlier in this pass — no real content in either.

These were description/copy edits only (title, descriptionHtml) — no images touched, consistent with §9's rule that images must go through Printify.

---
v6 — **Adopted the founder-supplied 16-file print-art set as canonical**, replacing the old single-color-direction files. Every tagline now ships in both Black-on-White and White-on-Black. Dropped the mono exception for "Deploying Identity v2.0" — all taglines now use Instrument Serif uniformly. Added GAGGED and SERVED as new (unpriced, unlisted) tee/tote candidates — see §5a. Old files removed from the working tree: `tee-404-straight-not-found.png`, `tee-its-not-a-bug.png`, `tee-code-it-serve-it.png`, `hoodie-deploying-identity.png`, `hoodie-off-the-clock.png`, `tote-please-hold.png`, `cap-gagged-*.png`, `cap-served-*.png` (still in git history).

v5 — Cap direction finalized: wordmark + segmented band, replacing GAGGED/SERVED for the cap specifically (see §4, §10). v4 — Shopify copy cleanup: stripped customer-visible dev placeholders from 4 listings. v3 — mug confirmed as a replacement for the existing Silver Wordmark SKU, not a new product. v2 superseded the chat-only brief: font corrected to Instrument Serif for statement pieces, mug + Phrase images added.
