# Storefront UI Kit

Recreation of the **FÆBRIQ Shopify storefront** — the single product surface for the brand.

`index.html` is an interactive click-through: home (hero → collection grid → about → footer), click any product to open its detail page, pick a size, and "Add to cart" increments the header cart count.

## Screens / sections
- `Hero.jsx` — full-bleed flagship statement, serif headline, circuit rule, CTA row + model image well.
- `CollectionGrid.jsx` — filterable 3-up product grid built from `<ProductCard>`.
- `ProductDetail.jsx` — image well + buy column with size picker and add-to-cart.
- `About.jsx` — editorial two-column brand statement.
- `SiteFooter.jsx` — wordmark, link columns, newsletter, circuit cap.
- Header is the shared `<SiteHeader>` component.

## Notes
- Composes the design-system components (`SiteHeader`, `ProductCard`, `Button`, `Badge`, `Input`, `CircuitRule`) via `window.FBRIQDesignSystem_0e5da2` — does **not** re-implement them.
- Product imagery uses the real mockups in `assets/`. All copy follows the brand voice (dry, flat, mono labels, no emoji).
- This is a cosmetic recreation, not production Shopify Liquid.
