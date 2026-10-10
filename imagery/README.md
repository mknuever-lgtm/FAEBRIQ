# FÆBRIQ Product Imagery

Date pulled: 2026/10/10

## Sources

- **Printify**: Shop ID 27682186 (Shopify FÆBRIQ), 25 products, 202 images
- **Shopify**: FÆBRIQ store, 23 products, 23 images (featured/primary image per product)

## Contents

- `MANIFEST.csv`: One row per image (225 total) with source, product title, product handle,
  Printify product ID, Shopify product ID, image ID, position, dimensions, file size,
  SHA-256, full source URL, and local filename.
- `shopify/`: The 23 Shopify product images as actual files.
- Printify images are NOT committed (202 files, ~92MB). Use the `source_url` column
  in the manifest to fetch them. Note: Printify image URLs require a browser
  User-Agent header; plain curl/wget without one returns 403.

## Notes

- All 225 images downloaded successfully. Zero failures.
- Printify `images.printify.com` mockup URLs include `camera_label` query params
  (front, back, context-1, lifestyle-1, etc.) preserved in the manifest.
- Shopify URLs are CDN links with version params (`?v=...`).
- Product statuses at pull time are NOT in the manifest; check Shopify/Printify live
  for current active/draft/archived state.
