# FÆBRIQ Vol. 1 — Production Brief

Every SKU · which file · print method · placement · price · what's still needed.

Rainbow — **colour** (confirmed, do not change): `#E8272A #F47F20 #F9D426 #2AAA42 #1D5BBE #7B3FAA`, never a gradient. **Geometry** (updated 2026-08-20 from the founder handoff): 6 blocks, but a *thin, near-continuous* bar — stripe gaps ≈0.4% of bar width (hairline, not the old chunky gaps), bar height ≈1.6% of bar width, and the bar runs slightly **wider** than the phrase above it (≈1.03×). Founder note: the rainbow read as too thick across the older designs.

Fonts — **superseded 2026-08-20, see below.** ~~(confirmed, all-serif as of v6): **Instrument Serif** for every tagline, no exceptions — including "Deploying Identity v2.0," which previously used mono. A small **mono** "FÆBRIQ" kicker sits under every design.~~

**Print art uses Bodoni Moda throughout** — phrase, the small label (e.g. "ERROR 404"), and the FÆBRIQ wordmark where one appears. No mono anywhere in the print files. Set all tagline text in **CAPS**, matching the handoff.

The 2026-08-20 handoff was set in Playfair Display (identified by shape comparison — 0.905 overlap vs Playfair, 0.384 vs Instrument Serif). Founder chose Bodoni Moda over it: same Didone register, far less ubiquitous.

**Print-safety correction (2026-08-20, later same day):** the first version of this file used an invented 0.33mm minimum-stroke rule of thumb and measured it against an isolated "O" glyph — not the real design. Printify's own published DTG guideline is **2pt (0.706mm) minimum line thickness**, and measured directly on the actual rendered file, the headline and label **failed it** — down to 0.254mm at the serif feet, the thinnest feature of a Didone and not what the "O" check caught. Scaling up doesn't fix it: hitting 0.706mm by size alone would need "STRAIGHT NOT" printed ~42in wide. Fixed instead with a small uniform alpha-dilation pass on each glyph (`DILATE_RADIUS_PX` in the tool) that thickens a 3px hairline the same fixed amount a 40px stem barely notices — targets the actual failure, not a proxy for it. Re-measured on the shipped file: 0.85–1.52mm across every element, all above the real minimum. Visual difference at design scale is negligible.

**Still true: no sample print has been run.** The 0.706mm figure is Printify's general DTG guideline, not a number confirmed for Monster Digital specifically. **Confirm with a physical print before committing the rest of the catalog.**

This reverses the Instrument Serif decision of 2026-08-19 **for print art only** — the website/theme still runs Instrument Serif. Treat that as a deliberate split: Didone on product, Instrument Serif on screen.

### Wordmark rule (confirmed 2026-08-20)

**Apparel and other products carry NO FÆBRIQ wordmark** — phrase + circuit bar, nothing else. The wordmark appears on **stickers and caps only**. Verified against the handoff's own apparel print files (`Code It. Serve It. - White (Print)`, `Off The Clock. Still Iconic. - Black (Print)`): both are phrase + bar with no wordmark. The earlier "a small mono FÆBRIQ kicker sits under every design" line was wrong on both counts. `tools/make_print_file.py --product apparel|sticker` encodes this. **Bold blocky** (not serif) stays on caps only — a fine serif blurs in embroidery thread at that scale; the cap uses the wordmark, not a tagline, so this doesn't conflict.

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

### 1a. The `.jpg` files above are previews, not print files (2026-08-19)

Audited every file in `assets/print-art/`. The 16 tagline JPGs are **820×420 with a solid `#0D0D0D` background**, and their rainbow bar measures `#FE0000 #FF8B00 #FFFF00 #008001 #0000FE #81007F` — the retired pure pride-flag hex, not the palette §0 above marks "confirmed, do not change." They also don't appear to use Instrument Serif. They predate the v6 spec; the spec was always right. Three problems if uploaded as-is:

1. **Too small** — 820px against Printify's ~4500px requirement.
2. **Opaque background** — JPG has no alpha, so the `#0D0D0D` field prints as a visible dark box on the garment instead of ink-on-fabric.
3. **Wrong palette** — contradicts the confirmed circuit colors.

Only `cap-wordmark-slim.png` / `cap-wordmark-structured.png` (on-brand) and `assets/phrase-404.png` (correct palette + type — the reference the rebuild is measured from) were already right.

**Founder handoff, 2026-08-20** — a zip of genuinely print-ready transparent PNGs arrived and supersedes the JPGs for the designs it covers: 4500×5400 print files for *Code It. Serve It.* and *Off The Clock. Still Iconic.*, 1664×1664 stickers for five taglines, a sticker-sheet bundle, cap logos and the mug art. **Use those directly.** Note the handoff carries the pure pride-flag hex; colour still follows the tokens above, so anything regenerated here uses the muted set.

There is **no print-res 404 in that handoff** — only the 1664px sticker (≈5.5" at 300dpi, too small for a chest print), which is why the 404 tee art is generated below.

**Print-ready files** (transparent PNG, 4500px, 300dpi, confirmed palette, Playfair Display):

| Tagline | Print file | For |
|---|---|---|
| 404: Straight Not Found | `assets/print-art/404-straight-not-found-light-4500.png` | dark garments (all FÆBRIQ apparel is black) |

Regenerate any tagline with `tools/make_print_file.py`:

```
python3 tools/make_print_file.py --label 404 --line1 "STRAIGHT NOT" --line2 "FOUND" \
    --out assets/print-art/404-straight-not-found-light-4500.png
```

`--ink dark` produces the light-garment variant. The remaining taglines share this same lockup and can be regenerated the same way — not yet done, pending a decision on whether to re-upload art for SKUs already synced to Printify.

**Open:** the live 404 sticker (`404-straight-not-found-sticker`, ACTIVE) was built from the old wrong-palette JPG per §6, so it is currently shipping retired pride-flag colors. Re-uploading its art in Printify is a founder action.

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

## 12. Sticker consolidation — one product page, pick 1-of-5 designs (founder action required)

Founder wants a single sticker product page where the customer picks the design (currently 3, eventually 5: Deploying Identity v2.0, Please Hold, Code It Serve It, plus 404 and one of GAGGED/SERVED once those exist) crossed with the existing Size option.

**Why this can't be done as a Shopify-side merge:** each of the 3 existing sticker listings is a *separate* Printify-linked product (`printify_custom.printify_product_id` is unique per listing — confirmed via metafield). Merging them into one Shopify product would strip the Printify link from 2 of the 3 designs, breaking fulfillment for whichever designs don't keep the surviving link.

**Correct path — rebuild in Printify as one product:**
1. In Printify, start a **new** product on the sticker blank (don't edit the 3 existing ones).
2. Add a custom variant option — call it **"Design"** — alongside the existing **Size** option, with values for however many designs are ready (start with the 3 that already have art).
3. Use Printify's per-variant artwork assignment (select the variant group for each Design value, apply that design's print file) so each Design × Size combination maps to the correct file.
4. Publish → syncs to Shopify as **one new draft product** with a Design + Size variant matrix.
5. Ping the agent (or just say so next session) to delete the 3 legacy single-design sticker listings and update the sticker bundle's copy/links to point at the new consolidated product.

Exact menu labels may vary by Printify's editor version — look for "Variants" and an "apply design to selected variants" style control if "Design" isn't offered as a preset option name.

**Update 2026-07-07:** the 3 legacy single-design sticker listings (Deploying Identity, Please Hold, Code It Serve It) have been **deleted** from Shopify per founder decision. Current sticker lineup is **bundle-only** — "FÆBRIQ Sticker Bundle — The Full Drop" (3-Pack $11 / 5-Pack $16). Founder is still finishing that product in Printify (not yet published). A separate single-sticker product (pick 1-of-N designs) is planned for later, once the founder builds it in Printify the same way (Design × Size variant option).

These were description/copy edits only (title, descriptionHtml) — no images touched, consistent with §9's rule that images must go through Printify.

---
v6 — **Adopted the founder-supplied 16-file print-art set as canonical**, replacing the old single-color-direction files. Every tagline now ships in both Black-on-White and White-on-Black. Dropped the mono exception for "Deploying Identity v2.0" — all taglines now use Instrument Serif uniformly. Added GAGGED and SERVED as new (unpriced, unlisted) tee/tote candidates — see §5a. Old files removed from the working tree: `tee-404-straight-not-found.png`, `tee-its-not-a-bug.png`, `tee-code-it-serve-it.png`, `hoodie-deploying-identity.png`, `hoodie-off-the-clock.png`, `tote-please-hold.png`, `cap-gagged-*.png`, `cap-served-*.png` (still in git history).

v5 — Cap direction finalized: wordmark + segmented band, replacing GAGGED/SERVED for the cap specifically (see §4, §10). v4 — Shopify copy cleanup: stripped customer-visible dev placeholders from 4 listings. v3 — mug confirmed as a replacement for the existing Silver Wordmark SKU, not a new product. v2 superseded the chat-only brief: font corrected to Instrument Serif for statement pieces, mug + Phrase images added.
