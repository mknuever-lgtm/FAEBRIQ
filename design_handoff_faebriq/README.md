# Handoff: FÆBRIQ Design System
**Version:** 0.1 · **Date:** June 2026
**Fidelity:** High-fidelity — implement pixel-precisely using the tokens and specs below.

---

## Overview

FÆBRIQ is a queer tech-nomad print-on-demand merch brand (tees, hoodies, stickers, sleeves) sold via Shopify. This handoff covers the full design system: tokens, core components, storefront UI kit, brand rules, and asset inventory.

The HTML/JSX files in this bundle are **design references**, not production code. Your task is to **recreate these designs in the target codebase** (React + Shopify Hydrogen, or equivalent) using its established patterns — or, if no environment exists yet, Vite + React + plain CSS custom properties is the closest match to this system.

---

## Brand in one line

> **Flat. Sharp. Silver. Quiet.**
> Dark editorial aesthetic — void black canvas, silver Instrument Serif wordmark, one canonical rainbow circuit as the graphic signature. Voice: dry, deadpan, terminal wit. Tagline: *Code it. Serve it.*

---

## Tech stack (recommended)

| Layer | Choice |
|---|---|
| Framework | React 18 (Vite or Hydrogen) |
| Styling | CSS custom properties (tokens) — **no Tailwind, no CSS-in-JS** |
| Icons | [Lucide](https://lucide.dev) — `1.5px` stroke, never filled |
| Fonts | Google Fonts (see below) |
| Components | JSX files in `components/` |

---

## Fonts — load order matters

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Archivo:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet" />
```

| Role | Family | Usage |
|---|---|---|
| Display / wordmark | Instrument Serif 400 | Silver, tracked `+0.06em`. Headlines, brand name. |
| Body / UI | Archivo 300–700 | All prose, nav, buttons. |
| Labels / terminal flavor | JetBrains Mono 400–700 | Kickers, overlines, prices, SKUs, code. Uppercase, wide tracking. |

---

## Design tokens (CSS custom properties)

Link `styles.css` first — it imports everything in `tokens/`.

### Colors

```css
/* THE VOID */
--fae-black:        #0d0d0d;  /* primary background */
--fae-ink-900:      #0a0a0a;  /* wells / insets */
--fae-ink-800:      #141414;  /* card surfaces */
--fae-ink-700:      #1c1c1c;  /* elevated / hover surface */
--fae-line-700:     #2a2a2a;  /* default border / hairline */
--fae-line-600:     #383838;  /* stronger border / hover border */

/* SILVER — the wordmark */
--fae-silver:       #c0c0c0;
--fae-silver-hi:    #d8d8d8;  /* highlight */
--fae-silver-lo:    #8a8a8a;  /* shadow / muted */

/* TEXT ON DARK */
--fae-text:         #e8e8e8;  /* body */
--fae-text-dim:     #9a9a9a;  /* secondary */
--fae-text-faint:   #5f5f5f;  /* captions / disabled */

/* ACCENT — terminal blue (the ONE accent) */
--fae-accent:       #4a9eff;
--fae-accent-dim:   #3a7fcc;  /* pressed */
--fae-accent-ghost: rgba(74,158,255,0.12);

/* RAINBOW CIRCUIT (the graphic signature — never fills, never BGs) */
/* ⭐ CONFIRMED PALETTE — locked June 2026, Option 3 (Segmented bands) */
--fae-circuit-coral:  #E8272A;  /* red    */
--fae-circuit-amber:  #F47F20;  /* orange */
--fae-circuit-yellow: #F9D426;  /* yellow */
--fae-circuit-green:  #2AAA42;  /* green  */
--fae-circuit-blue:   #1D5BBE;  /* blue   */
--fae-circuit-purple: #7B3FAA;  /* purple */

/* SEMANTIC ALIASES (use these in components) */
--bg-page:          var(--fae-black);
--surface-card:     var(--fae-ink-800);
--surface-raised:   var(--fae-ink-700);
--border-hairline:  var(--fae-line-700);
--border-strong:    var(--fae-line-600);
--text-display:     var(--fae-silver);
--text-body:        var(--fae-text);
--text-muted:       var(--fae-text-dim);
--text-faint:       var(--fae-text-faint);
--link:             var(--fae-accent);
--focus-ring:       var(--fae-accent);
```

### Typography scale

```css
--fs-2xs:  0.6875rem;  /* 11px — circuit labels */
--fs-xs:   0.75rem;    /* 12px — captions */
--fs-sm:   0.875rem;   /* 14px — secondary body */
--fs-md:   1rem;       /* 16px — body */
--fs-lg:   1.125rem;   /* 18px — lead */
--fs-xl:   1.5rem;     /* 24px — small heading */
--fs-2xl:  2rem;       /* 32px — heading */
--fs-3xl:  2.75rem;    /* 44px — display sm */
--fs-4xl:  4rem;       /* 64px — display */
--fs-5xl:  6rem;       /* 96px — hero wordmark */
--fs-6xl:  8.5rem;     /* 136px — billboard */

/* Letter spacing */
--ls-wide:    0.04em;
--ls-wider:   0.12em;   /* overlines, taglines */
--ls-widest:  0.28em;   /* CODE IT. SERVE IT. lockup */
```

### Spacing (4px base)

```css
--space-1:  4px;   --space-2:  8px;   --space-3: 12px;
--space-4: 16px;   --space-5: 24px;   --space-6: 32px;
--space-7: 48px;   --space-8: 64px;   --space-9: 96px;
--space-10:128px;
```

### Borders & radius

```css
--radius-none: 0;     /* default — square is the brand */
--radius-sm:   2px;   /* absolute maximum rounding (interactive chrome only) */
--border-1: 1px solid var(--border-hairline);
--border-2: 1px solid var(--border-strong);
```

---

## Components

All components are in `components/`. Load the compiled bundle:
```html
<script src="_ds_bundle.js"></script>
```
Then access via:
```js
const { Button, Badge, Card, CircuitRule, Input, ProductCard, SiteHeader }
  = window.FBRIQDesignSystem_0e5da2;
```

### Button

```ts
interface ButtonProps {
  variant?: "primary" | "accent" | "secondary" | "ghost"; // default: "primary"
  size?:    "sm" | "md" | "lg";                           // default: "md"
  disabled?: boolean;
  iconLeft?:  ReactNode;
  iconRight?: ReactNode;
  onClick?: (e) => void;
}
```

- **primary** — silver fill `#c0c0c0`, black text, JetBrains Mono uppercase
- **accent** — `#4a9eff` fill, black text
- **secondary** — transparent fill, `--border-hairline` border, silver text
- **ghost** — no border, silver text, slight hover fill
- **All variants:** square corners (max 2px), no shadow, 1px border

### Badge

```ts
interface BadgeProps {
  tone?: "default"|"accent"|"new"|"sold"|"coral"|"amber"|"yellow"|"green"|"blue"|"purple";
  dot?: boolean; // leading status dot
}
```

Mono uppercase chip. `--fs-2xs` (11px). Outlined style, hairline border, 0px radius.

### Card

```ts
interface CardProps {
  accent?:      boolean; // six-color circuit hairline along the top edge
  interactive?: boolean; // hover brightens border
  padding?:     string;  // default: var(--space-5)
}
```

`--surface-card` fill, `--border-hairline` border, zero radius, no shadow. Hover: border brightens to `--border-strong`.

### CircuitRule

Renders the six-stripe rainbow circuit divider (inline SVG, 6 horizontal traces, terminal pads). Use at section breaks. Never substitute with a CSS gradient.

```tsx
<CircuitRule width={400} /> // width in px, height auto-sized
```

### Input

Standard text input. `--bg-sunken` fill, `--border-hairline` border. Focus: `--fae-accent` ring. JetBrains Mono label above. Zero radius.

### ProductCard

```ts
interface ProductCardProps {
  image: string;  // product image URL
  title: string;
  price: string;  // e.g. "$35"
  meta?:  string; // mono overline, e.g. "TEE · 6.5 OZ"
  badge?: string; // corner label, e.g. "New Drop"
  badgeTone?: BadgeTone;
  onClick?: (e) => void;
}
```

Image well (square, `overflow:hidden`, no radius), Instrument Serif title, mono price. Hover: image scales 1.03, border brightens. `--surface-card` background.

### SiteHeader

```ts
interface SiteHeaderProps {
  links?:        string[]; // default: ["Shop","Collections","About","Journal"]
  active?:       string;   // default: "Shop"
  cartCount?:    number;   // default: 0
  announcement?: ReactNode;
  onNav?: (target: string) => void;
}
```

Fixed 72px header. Hairline bottom border. Left: FÆBRIQ wordmark (Instrument Serif, silver). Right: JetBrains Mono nav links (uppercase, `--ls-wider`), search glyph, cart count chip.

---

## The circuit rule: ONE mark, never redrawn

**Confirmed style (June 2026): Option 3 — Segmented bands.** Six equal solid-color blocks with a small gap between each. This renders faithfully at all sizes including embroidery and small print.

```html
<!-- Standard circuit rule implementation -->
<div style="display:flex; gap:3px; width:100%; height:4px;">
  <span style="flex:1; background:#E8272A;"></span>
  <span style="flex:1; background:#F47F20;"></span>
  <span style="flex:1; background:#F9D426;"></span>
  <span style="flex:1; background:#2AAA42;"></span>
  <span style="flex:1; background:#1D5BBE;"></span>
  <span style="flex:1; background:#7B3FAA;"></span>
</div>
```

**Rules:**
- Six equal segments, `gap: 3–4px`, height `3–5px` depending on context.
- On every product: present as a divider, underline, edge band, or corner trace.
- In UI: use `<CircuitRule>` for section breaks only.
- Never use as a fill or background color.
- Never substitute with a smooth CSS gradient.
- The logo lockup = `FÆBRIQ` wordmark **above** the circuit rule — one integrated mark.

The `assets/circuit.svg` (circuit trace with nodes) is a legacy reference asset — do NOT use it for new implementations. Use the segmented bands CSS above.

---

## Logo lockup implementation

```html
<div style="position:relative; display:inline-block; width:300px;">
  <img src="assets/circuit.svg" style="width:100%; display:block;" />
  <span style="
    position:absolute; top:50%; left:50%;
    transform:translate(-50%,-50%);
    font-family:'Instrument Serif',serif;
    font-size:36px; letter-spacing:0.06em;
    color:#c0c0c0; white-space:nowrap;
    margin-top:0.15em;
  ">FÆBRIQ</span>
</div>
```

The `margin-top:0.15em` compensates for the Instrument Serif cap-height offset so the text visually centers on the trace (not the em-box midpoint).

---

## Storefront UI kit

Pre-built page sections in `ui_kits/storefront/`:

| File | Section |
|---|---|
| `Hero.jsx` | Full-bleed hero with wordmark lockup, tagline, CTA |
| `CollectionGrid.jsx` | 3-col product grid with `<ProductCard>` tiles |
| `ProductDetail.jsx` | PDP — image, title, price, size selector, add-to-cart |
| `About.jsx` | Brand statement + founder text |
| `SiteFooter.jsx` | Footer with wordmark, nav links, mono copyright |
| `index.html` | Full storefront preview (all sections, no router) |

---

## Assets inventory

All in `assets/`:

| File | Use |
|---|---|
| `circuit.svg` | ⭐ canonical brand circuit — the one mark |
| `wordmark.png` | Wordmark PNG (4500×1500) |
| `logo-stacked.png` | Stacked lockup |
| `favicon.png` | 512px favicon |
| `hero-banner.png` | Hero full-bleed (2560×1024) |
| `flagship-phrase.png` / `.svg` | "Please Hold, I'm Rebranding My Identity" phrase print |
| `mockup-tee-model.png` | ~~Old tee mockup — name misspelled, do not use~~ |
| `mockup-tee-flat.png` | ~~Old flat mockup — name misspelled, do not use~~ |
| `mockup-flatlay.png` | ~~Old flatlay — name misspelled, do not use~~ |

**Current product photography (June 2026 — use these):**

| File | Product | Use |
|---|---|---|
| `uploads/lifestyle_model-bf26297c.png` | Unisex Tee — "Code it. Serve it." | Hero, lifestyle |
| `uploads/lifestyle_model (1)-c0be1b62.png` | Dad Cap — FÆBRIQ embroidered | Detail, portrait |
| `uploads/lifestyle_model (2)-86e63f14.png` | Pullover Hoodie — "Deploying Identity V2.0" | Lifestyle, full bleed |
| `uploads/Flat-layMockup-d0017eb3.png` | Collection flatlay | Collection overview |
| `uploads/A single high-resolution...dfe9a456.png` | Product lineup (wide) | Brand/press use |

---

## Voice & copy rules

- **Sentence case** for prose. **MONO UPPERCASE wide tracking** for labels, kickers, nav.
- **No emoji. No exclamation marks.** Full stops are a brand device.
- **Vocabulary:** terminal/version-control lexicon — *deploy, commit, ship, serve, v2.0, protocol, rebrand.*
- **Never:** "game-changing", hype language, rocket emojis, "best. tee. ever."
- Buttons say: *Shop now.* / *Add to cart.* / *Deploy. →* — not *BUY NOW!!!*

---

## Layout rules

- Max content width: **1240px**, centered
- Header: **72px fixed**, hairline bottom border
- Base grid: 4px. Section vertical rhythm: `--space-7`/`--space-8` (48–64px)
- Gutters: generous — let the void breathe
- **No gradients. No box-shadow (except `--shadow-pop` for modals only). No border-radius > 2px.**
- Hover state: border brightens or text goes to `--fae-silver-hi`. **Nothing moves except product image 1.03 scale.**

---

## Files in this package

```
design_handoff_faebriq/
├── README.md                  ← this file
├── styles.css                 ← token entry point
├── tokens/
│   ├── colors.css
│   ├── typography.css
│   ├── spacing.css
│   ├── fonts.css
│   └── base.css
├── assets/
│   ├── circuit.svg            ← THE canonical brand mark
│   ├── wordmark.png
│   └── … (all mockups)
├── components/
│   ├── core/                  ← Button, Badge, Card, Input, CircuitRule
│   └── storefront/            ← ProductCard, SiteHeader
├── ui_kits/storefront/        ← full page sections
└── faebriq-mockups/
    └── FÆBRIQ Mockup Sheet.html  ← product mockup reference
```

## Shopify product image system (June 2026)

Each product listing requires **5 images** at 1080×1080px. The composition system:

| # | Type | Layout | Photo needed |
|---|---|---|---|
| 1 | **Hero** | Split — photo 65% left, info panel 35% right (wordmark, product name, price) | Yes — main model shot |
| 2 | **Detail** | Full bleed photo, top kicker + circuit rule, bottom scrim with name/price | Yes — close-up/portrait |
| 3 | **Phrase** | Pure typographic — phrase large in Instrument Serif, circuit rule below, FÆBRIQ mono | No |
| 4 | **Lifestyle** | Full bleed with dark gradient overlay, product name + price bottom | Yes — lifestyle/environment |
| 5 | **Collection** | Photo top 68%, info panel bottom (price grid, circuit rule) | Yes — flatlay |

Reference implementation: `export/src/FAEBRIQ Shopify Images.html`

**Brand consistency across all product images:**
- Always: black void (`#0d0d0d`) for info panels, circuit rule (segmented bands) strip, FÆBRIQ wordmark
- Always: Instrument Serif for product names, JetBrains Mono for kickers/prices/SKUs
- Always: hairline borders (`#1c1c1c`), silver text (`#c0c0c0`), no gradients in panels

---

*When in doubt: flat, sharp, silver, quiet.*
