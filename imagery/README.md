# FÆBRIQ Product Imagery

Date pulled: 2026/10/10 (v2 manifest: 2026/10/10)

## Sources

- **Printify**: Shop ID 27682186 (Shopify FÆBRIQ), 25 products, 202 images
- **Shopify**: FÆBRIQ store, 23 products, 58 media items (all gallery images, not just featured)

## Contents

- `MANIFEST.csv`: One row per image (260 total: 202 Printify + 58 Shopify) with source,
  product title, product handle, Printify product ID, Shopify product ID,
  Printify-to-Shopify handle link, Shopify status, image ID, position, dimensions,
  file size, SHA-256, full source URL, and local filename.
- `shopify/`: The 23 Shopify featured product images as actual files.
  (Gallery images beyond the featured image are URL-only in the manifest.)
- Printify images are NOT committed (202 files, ~92MB). Use the `source_url` column
  in the manifest to fetch them. Note: Printify image URLs require a browser
  User-Agent header; plain curl/wget without one returns 403.

## Product count note (25 vs 21)

Printify shows 25 products but only 21 distinct titles. Five products share the
identical title "Kiss-Cut Stickers" (different product IDs for the 404, Not-A-Bug,
Deploying, Code-It, and Please-Hold designs). The manifest has one row per image,
so all 25 products are represented across the 202 Printify rows.

## Known gaps

- Printify product-to-Shopify handle links are filled where confidently matched
  (FÆ stickers by title, phrase stickers by known product IDs from 2026/10/07).
  Unmatched rows have an empty `shopify_handle_link`.
- The "FÆ Doll Kiss-Cut Sticker", "FÆ Sticker Sheet: Mascot Poses",
  "Minimal Phrase Sticker Sheets", generic "Kiss-Cut Stickers" (20 variants),
  and duplicate caps have no obvious Shopify match. Likely orphans or drafts.
- Only Shopify featured images are committed as files. Gallery positions 2+
  are URL-only.

## Failures

Zero download failures on 2026/10/10. All 202 Printify + 23 Shopify featured
images downloaded successfully.
