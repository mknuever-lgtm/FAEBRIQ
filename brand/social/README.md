# FÆBRIQ social sharing card (og:image)

1200×630. White ground, black Instrument Serif wordmark, Pride Circuit bar below.

| File | Purpose |
|---|---|
| `faebriq-og-card.png` | **Upload this.** Admin → Online Store → Preferences → Social sharing image. |
| `faebriq-og-card.svg` | Production source. Wordmark converted to outlines — no font dependency. |
| `faebriq-og-card-text.svg` | Editable source. Live `<text>`; needs Instrument Serif to render as designed. |
| `build-card.js` | Regenerates all three. Requires `opentype.js` + the Instrument Serif TTF. |

Stripe hexes are the canonical Pride Circuit values, matching
`snippets/circuit-rule.liquid` and `tokens/colors.css`:
`#E8272A #F47F20 #F9D426 #2AAA42 #1D5BBE #7B3FAA` — flush, hard-edged, no gradient.

The TTF is fetched at build time only and is not vendored or referenced by the theme.
