# FÆBRIQ — Project Guide

## 1. Project identity

FÆBRIQ is a Shopify print-on-demand brand under MK Global Horizons, run by Maurice Knuever (Toronto). Niche: queer + tech/dev community. Provider: Printify, with Monster Digital preferred as the print/apparel supplier.

## 2. Production requirement

Printify requires transparent PNG print files at ~4500px. Source design files currently in this repo are 820x420 JPG previews with solid backgrounds — these need re-export (transparent PNG, ~4500px) before they can sync to Printify.

## 3. Known open bugs — check before touching related products

- **Latent**: the Shopify About page *body* promises "a named share of Pride Circuit proceeds goes to an LGBTQ+ org" — a commitment that was explicitly deferred until there's revenue. It is currently invisible because `templates/page.about.liquid` is fully static and never renders `page.content`. It goes live the instant anyone makes that template render the page body.
- **Product descriptions promise "ships in 5–7 business days"** on all 12 active products — faster than the Shipping Policy's own production + transit math (2–7 production + 4–8 US transit = 6–15 days). Needs Maurice to pick the real number, then a single copy pass across all descriptions. Not yet fixed anywhere (theme or descriptions).
- **Store-level `shipsToCountries` still lists ~237 countries** — cosmetic only, not a checkout risk (see Resolved note below), but worth a cleanup pass eventually: 9 delivery profiles with 0 product variants (orphaned Monster Digital mug/hoodie/kids-clothes/Fulfill Engine/Printify-Hats profiles) still carry broad EU/AU/Rest-of-World zone definitions. Zone *removal* isn't supported by the Admin API (confirmed via schema introspection); would need Shopify Admin, or deleting the whole empty profile if that mutation is available.

Resolved (2026-08-24, re-verified live via GraphQL): **duplicate FREE SHIPPING rates** — General profile's US+CA zone now has exactly one active $0.00 rate, no $0.01 duplicate. **Sticker delivery profiles shipping to the EU** — SPOKE Custom Products and Printed Simply now both show a single "United States & Canada" zone only, one $0.00 rate each, no EU/worldwide zones. **Markets configuration** — confirmed already correct: primary market is United States only, a separate active Canada market has Canada only, no other active markets exist. This matches Shopify's documented two-part checkout-country rule (active market + shipping zone with an available rate) exactly, cross-checked against a Manus research pass sourced to Shopify's own Help Center docs. None of these needed further action — whether Maurice fixed them directly in Admin or a provider app re-synced isn't confirmed, only that the live state is now correct.

Resolved (2026-08-23, per theme audit): **shipping-copy contradiction across 5 surfaces** — hero, product-page template, and About page all corrected to "Free shipping to the US & Canada" on `faebriqtheme-launch-fix` (verified byte-for-byte after the `themeFilesUpsert`). Not yet live — still pending Maurice publishing that theme (see MEMORY.md).

Resolved (2026-08-23): **orphan White variant** — both active tees are Black-only S–5XL; White survives only on an archived product, invisible to customers. **Wrong-design mug** — deleted entirely; only two empty (0-variant) Monster Digital mug delivery profiles remain as harmless residue.

Resolved (2026-08-19): "cross-copied SEO titles" — checked `seo.title` on all 12 active products via GraphQL, all unique, no cross-copying on the live catalog. The real (minor, non-live) issue was 3 archived products with mismatched `seo.title` values from old copy/paste — invisible to customers, low priority if ever revisited.

Note the recurring pattern in most resolved bugs: the defect either survives only on **archived** products, or was fixed by Maurice/a provider sync between audit passes without an explicit handoff note. Always re-verify live state via GraphQL before reporting a bug as open — don't trust a prior session's snapshot.

## 4. Brand voice

Load `faebriq-brand-kit/SKILL.md` (and its `references/` files) before writing any FÆBRIQ copy, generating images, or making design decisions — it covers voice, visual identity, color/type tokens, and sample copy. Also check this repo's design system files (`components/`, guideline cards, tokens) for implementation-level detail. Don't invent style choices that conflict with what's already documented here.

## 5. Memory logging

Any time you learn something new about this project's state, structure, conventions, or gotchas while working — a bug you find, a decision Maurice makes, a pattern in the codebase, a workflow quirk — append it to `MEMORY.md` with today's date. Keep entries short and factual. Don't repeat what's already in this file.

## 6. Session start

At the start of every session, read `MEMORY.md` in full before doing anything else.
