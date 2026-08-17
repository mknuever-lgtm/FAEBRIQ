# FÆBRIQ — Project Guide

## 1. Project identity

FÆBRIQ is a Shopify print-on-demand brand under MK Global Horizons, run by Maurice Knuever (Toronto). Niche: queer + tech/dev community. Provider: Printify, with Monster Digital preferred as the print/apparel supplier.

## 2. Production requirement

Printify requires transparent PNG print files at ~4500px. Source design files currently in this repo are 820x420 JPG previews with solid backgrounds — these need re-export (transparent PNG, ~4500px) before they can sync to Printify.

## 3. Known open bugs — check before touching related products

- Orphan White/L variant on the tee product.
- Cross-copied SEO titles on four products (need unique titles per product).
- Mug had the wrong design synced (already approved for deletion — confirm before recreating).

## 4. Brand voice

Load `faebriq-brand-kit/SKILL.md` (and its `references/` files) before writing any FÆBRIQ copy, generating images, or making design decisions — it covers voice, visual identity, color/type tokens, and sample copy. Also check this repo's design system files (`components/`, guideline cards, tokens) for implementation-level detail. Don't invent style choices that conflict with what's already documented here.

## 5. Memory logging

Any time you learn something new about this project's state, structure, conventions, or gotchas while working — a bug you find, a decision Maurice makes, a pattern in the codebase, a workflow quirk — append it to `MEMORY.md` with today's date. Keep entries short and factual. Don't repeat what's already in this file.

## 6. Session start

At the start of every session, read `MEMORY.md` in full before doing anything else.
