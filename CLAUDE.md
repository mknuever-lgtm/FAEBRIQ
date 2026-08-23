# FÆBRIQ — Project Guide

## 1. Project identity

FÆBRIQ is a Shopify print-on-demand brand under MK Global Horizons, run by Maurice Knuever (Toronto). Niche: queer + tech/dev community. Provider: Printify, with Monster Digital preferred as the print/apparel supplier.

## 2. Production requirement

Printify requires transparent PNG print files at ~4500px. Source design files currently in this repo are 820x420 JPG previews with solid backgrounds — these need re-export (transparent PNG, ~4500px) before they can sync to Printify.

## 3. Known open bugs — check before touching related products

- **Shipping claims contradict each other in 5 places** (found 2026-08-23, all still open). "US delivery only" is hardcoded in `templates/index.json`, `sections/hero.liquid` (schema default) and `templates/product.liquid:100` (every product page); the rendered About page says "shipped worldwide"; the Shipping Policy says US + Canada. Product descriptions also promise "ships in 5–7 business days", faster than the policy's own production + transit math. Canada is live and gets free shipping — the theme copy is what's wrong.
- **Duplicate shipping rates**: US and Canada zones each have two active rates both named "FREE SHIPPING", one at $0.01 (unconditional) and one at $0.00. Delete the $0.01 rate in each.
- **Sticker delivery profiles still ship to the EU** — SPOKE Custom Products (5 single stickers) and Printed Simply (sticker sheet). Zone deletion is impossible via the Admin API; must be done in Shopify Admin.
- **Latent**: the Shopify About page *body* promises "a named share of Pride Circuit proceeds goes to an LGBTQ+ org" — a commitment that was explicitly deferred until there's revenue. It is currently invisible because `templates/page.about.liquid` is fully static and never renders `page.content`. It goes live the instant anyone makes that template render the page body.

Resolved (2026-08-23): **orphan White variant** — both active tees are Black-only S–5XL; White survives only on an archived product, invisible to customers. **Wrong-design mug** — deleted entirely; only two empty (0-variant) Monster Digital mug delivery profiles remain as harmless residue.

Resolved (2026-08-19): "cross-copied SEO titles" — checked `seo.title` on all 12 active products via GraphQL, all unique, no cross-copying on the live catalog. The real (minor, non-live) issue was 3 archived products with mismatched `seo.title` values from old copy/paste — invisible to customers, low priority if ever revisited.

Note the recurring pattern in all three resolved bugs: the defect survives only on **archived** products. Always filter by `status:active` before concluding a catalog bug is live.

## 4. Brand voice

Load `faebriq-brand-kit/SKILL.md` (and its `references/` files) before writing any FÆBRIQ copy, generating images, or making design decisions — it covers voice, visual identity, color/type tokens, and sample copy. Also check this repo's design system files (`components/`, guideline cards, tokens) for implementation-level detail. Don't invent style choices that conflict with what's already documented here.

## 5. Memory logging

Any time you learn something new about this project's state, structure, conventions, or gotchas while working — a bug you find, a decision Maurice makes, a pattern in the codebase, a workflow quirk — append it to `MEMORY.md` with today's date. Keep entries short and factual. Don't repeat what's already in this file.

## 6. Session start

At the start of every session, read `MEMORY.md` in full before doing anything else.
