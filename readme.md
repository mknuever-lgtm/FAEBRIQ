# FÆBRIQ — Design System

**Queer tech-nomad merch. Dark editorial aesthetic.**
Silver serif wordmark, rainbow circuit accent. Tagline: *Code it. Serve it.*

FÆBRIQ is a print-on-demand merch brand (tees, stickers, laptop sleeves) sold through a **Shopify storefront**. The audience is queer tech professionals and digital nomads. The flagship product is the *"Please Hold, I'm Rebranding My Identity"* premium tee. The aesthetic target: **high-end fashion brand meets terminal UI** — flat, sharp, editorial, never cringe, never hype.

---

## Sources provided
- Brand assets (wordmark, favicon, hero banner, social, flagship phrase print + SVG) — copied into `assets/`.
- Product mockups (tee on model, flatlay, laptop sleeve, stickers) — copied into `assets/`.
- `uploads/etsy_flagship.pdf` — Etsy listing draft for the flagship tee (voice/copy reference).
- `uploads/concept_to_ca0.pdf` — 7-day brand launch playbook (strategy context).
- Misc business-plan docs and tutorials (CampGPT, Shopify POD) — peripheral, not brand-defining.

> The wordmark is set in **Instrument Serif** (confirmed in the listing draft). Body type and mono are design-system choices documented below.

---

## CONTENT FUNDAMENTALS

**Voice:** dry, direct, slightly cheeky. Deadpan technical wit. The joke is always underplayed — the reader feels smart for getting it, the brand never winks too hard.

**Person:** Speaks to *you* ("Engineered for the tech-nomad"), refers to itself rarely and in the first person only inside product copy that role-plays the wearer ("Please hold, I'm rebranding my identity").

**Casing:** Sentence case for prose. **Mono UPPERCASE with wide tracking** for labels, nav, buttons, SKUs, kickers. Display headings in serif, sentence case.

**Punctuation:** Short sentences. Periods as rhythm. *Code it. Serve it.* The full stop is a brand device — it makes statements land flat and final.

**Emoji:** None. Ever. No exclamation-mark hype, no rocket ships, no "game-changing." Enthusiasm is shown through precision, not punctuation.

**Lexicon:** Borrow from the terminal and version control — *deploy, commit, ship, serve, v2.0, protocol, identity, rebrand*. Use them straight, never as a stretched pun.

**Examples**
- ✅ "Deploying Identity v2.0" · "Code it. Serve it." · "Engineered for the modern tech-nomad." · "Please hold, I'm rebranding my identity."
- ❌ "Unleash your inner coder!! 🚀" · "Best. Tee. Ever." · "You won't BELIEVE this drop" · "game-changing queer-owned synergy"

---

## VISUAL FOUNDATIONS

**Backgrounds.** The void: flat `#0d0d0d`, edge to edge. No gradients, anywhere, ever. Depth is built from **value steps** (`#0d0d0d` → `#141414` → `#1c1c1c`), not blur or shadow. Imagery is full-bleed and moody — server-room low-key lighting, cool-to-neutral cast, subtle grain. Product mockups sit in dim editorial environments, never on bright white.

**Color.** Silver `#C0C0C0` is the brand (wordmark, primary buttons). A single terminal blue `#4A9EFF` is the only accent — links, focus, the one important action. The **rainbow circuit** (coral → amber → yellow → green → blue → purple) is a *graphic signature*, used as the pride bar — six equal blocks — or as a thin branching trace. **Never as a background wash, never as a gradient sweep behind content.** No bright whites; the lightest text is `#E8E8E8`.

**Type.** Display & wordmark: **Instrument Serif**, silver, tracked `+0.06em` — editorial, high-fashion. Body & UI: **Archivo**, neutral grotesque. Labels & terminal flavor: **JetBrains Mono**, uppercase, wide tracking. Headlines set tight (`line-height ~1.05`); body comfortable (`1.5`).

**Spacing.** 4px base scale. Generous editorial whitespace — let the void breathe. Section rhythm uses `--space-7`/`--space-8` (48–64px).

**Corners.** Sharp. Square by default. `2px` is the maximum softening on interactive chrome. **Never pills, never friendly rounding.**

**Borders.** 1px hairlines do the structural work: `#2a2a2a` default, `#383838` on hover/emphasis. Cards are a hairline border over a `#141414` fill.

**Shadows.** Essentially none. One subtle drop (`--shadow-pop`) for menus/modals only. Elevation is communicated by value and border, not blur. The only "glow" is a tight terminal-blue focus ring.

**Cards.** Flat fill, hairline border, square corners, no shadow. Optional 2px circuit accent along the top edge for featured items. Hover brightens the border — nothing moves.

**Animation.** Restrained. Fades and small position shifts, 120–400ms, standard/ease-out curves. **No bounce, no spring, no overshoot.** Product images do a subtle 1.03 zoom + opacity lift on hover; that's the most playful it gets.

**Hover states.** Links/text → silver highlight `#D8D8D8`. Buttons → lighter silver / brightened accent. Cards → brighter border. **Press** → 1px downward nudge, no color flip.

**Transparency & blur.** Used sparingly — a faint accent wash (`--fae-accent-ghost`) behind selected states. No frosted-glass everywhere; blur is not a brand motif.

**Layout.** Max content width `1240px`. Fixed 72px header with a hairline bottom border. Generous gutters. Asymmetry and editorial grids over centered symmetry where possible.

---

## BUILDING WITH THE SYSTEM

**Load two things.** Link `styles.css` — it is the whole styling closure (fonts, colour, type, spacing, element defaults). Then load `_ds_bundle.js`, which assigns every component to the global `window.FBRIQDesignSystem_0e5da2`.

**There is no provider and no theme context.** Nothing needs wrapping. Every token is a plain CSS custom property on `:root`, so a component is styled the moment `styles.css` is on the page — and unstyled, in browser defaults, the moment it isn't.

**Style your own layout glue with the tokens, not with invented values.** There is no utility-class framework here: reach for `var(--bg-page)`, `var(--bg-sunken)`, `var(--text-body)`, `var(--text-faint)`, `var(--border-hairline)`, `var(--font-display)`, `var(--font-body)`, `var(--font-mono)` and the `--space-*` scale, plus the `.fae-wordmark` / `.fae-overline` / `.fae-tagline` / `.fae-circuit-rule` primitives. Never hardcode a hex that a token already names.

**Where the truth lives.** Per component: `components/<group>/<Name>/<Name>.d.ts` is the prop contract and `<Name>.prompt.md` is the usage note — read those before composing. The stylesheets in `tokens/` are the authoritative token list; `guidelines/` holds the specimen cards.

```jsx
const { SiteHeader, ProductCard, CircuitRule, Button } = window.FBRIQDesignSystem_0e5da2;

<div style={{ maxWidth: "1240px", margin: "0 auto", background: "var(--bg-page)" }}>
  <SiteHeader active="Shop" cartCount={0} announcement="Free US & Canada shipping over $80 · Code it. Serve it." />
  <section style={{ padding: "var(--space-8) var(--space-7)" }}>
    <div className="fae-overline">The catalog</div>
    <h2 style={{ font: "400 34px/1.05 var(--font-display)", color: "var(--text-display)", margin: "0 0 20px" }}>
      Everything in the drop
    </h2>
    <CircuitRule />
    <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "var(--space-5)", marginTop: "var(--space-6)" }}>
      <ProductCard image="assets/model-tee-new.png" meta="TEE" title="Code It, Serve It." price="CA$42" />
    </div>
    <Button variant="primary">Shop the drop</Button>
  </section>
</div>
```

---

## ICONOGRAPHY

FÆBRIQ is **icon-light by design** — the terminal aesthetic favors text and typographic glyphs over decorative icons.

- **No emoji. No icon font baked into the brand.** Where a wordless control is unavoidable, prefer mono typographic glyphs: `→` (forward/CTA), `[0]` (cart count), `$` (prompt), `//` (comment/aside), `✕` (close/negation).
- The **rainbow circuit** is the one true brand graphic. The canonical mark is **`assets/circuit.svg`** — a single horizontal rainbow trace (coral → purple) with filled terminal pads and hollow ring nodes branching off. Use that SVG at hero/lockup scale; use `<CircuitRule>` / `.fae-circuit-rule` as the pride bar — six equal blocks in one row — for section breaks and hero caps. `<CircuitRule>` takes `height`, `gap`, `width` and `align`; `.fae-circuit-rule` is the gapless CSS twin. Never hand-draw a substitute.
- When UI genuinely needs line icons (e.g. a storefront search/cart/menu), use **[Lucide](https://lucide.dev)** from CDN — its thin, sharp, geometric stroke matches the terminal vibe. *(Substitution flagged: no icon set was provided in the brand assets; Lucide is the closest match. Swap if the brand later adopts a set.)*
  ```html
  <script src="https://unpkg.com/lucide@latest"></script>
  ```
  Render at `1.5px`–`2px` stroke, in `--text-muted` or `--text-body`, never filled.
- Logos & marks live in `assets/` — never redraw them.

---

## Index / manifest

**Root**
- `styles.css` — global entry point (imports only). Consumers link this.
- `README.md` — this guide.
- `SKILL.md` — Agent Skills wrapper for downloadable use.

**`tokens/`** — `fonts.css`, `colors.css`, `typography.css`, `spacing.css`, `base.css` (element defaults + `.fae-wordmark` / `.fae-overline` / `.fae-tagline` / `.fae-circuit-rule` primitives).

**`assets/`** — `wordmark.png`, `favicon.png`, `logo-stacked.png`, `hero-banner.png`, `circuit.svg`, `flagship-phrase.png` + `.svg`, the current on-model shots (`model-tee-new`, `model-hoodie-new`, `model-cap-new`, `model-flatlay-new`) and the earlier product mockups (`mockup-tee-model`, `mockup-tee-flat`, `mockup-flatlay`, `mockup-sleeve`, `mockup-sleeve-desk`, `mockup-stickers`).

**`components/`**
- `core/` — `Button`, `Badge`, `Card`, `Input`, `CircuitRule`
- `storefront/` — `ProductCard`, `SiteHeader`

**`ui_kits/`**
- `storefront/` — Shopify storefront recreation (home / hero, collection grid, product detail, about).

**`guidelines/`** — foundation specimen cards (Colors, Type, Spacing, Brand) shown in the Design System tab.

---

*Maintained as a living system. When in doubt: flat, sharp, silver, quiet.*
