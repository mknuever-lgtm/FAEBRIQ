---
name: faebriq-design
description: Use this skill to generate well-branded interfaces and assets for FÆBRIQ, either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.
If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.
If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## FÆBRIQ in one breath
Queer tech-nomad merch. Dark editorial. Silver serif wordmark (`#C0C0C0`, Instrument Serif), rainbow circuit accent, single terminal-blue accent (`#4A9EFF`) on the void (`#0d0d0d`). Tagline: *Code it. Serve it.* Voice: dry, direct, slightly cheeky. No gradients, no emoji, no rounded friendly corners, no bright whites. Flat. Sharp. Editorial.

## Files
- `styles.css` — link this; it imports all tokens + fonts.
- `readme.md` — full guide (content fundamentals, visual foundations, iconography).
- `tokens/` — color/type/spacing/font CSS custom properties.
- `assets/` — wordmark, favicon, logos, product mockups.
- `components/` — React primitives (Button, Badge, Card, Input, CircuitRule, ProductCard, SiteHeader).
- `ui_kits/storefront/` — full Shopify storefront recreation.
- `guidelines/` — foundation specimen cards.
