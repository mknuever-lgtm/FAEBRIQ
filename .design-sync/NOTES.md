# FAEBRIQ design-sync notes

## Shape of this repo (read this first)

This repo **is** the design system — there is no npm package and no `dist/`,
so the skill's `package-build.mjs` converter cannot run here. The repo carries
its own deterministic equivalent instead:

| Command | What it does |
|---|---|
| `npm run build:ds-bundle` | `tools/build-ds-bundle.mjs` — regenerates `_ds_bundle.js` from the real `.jsx` sources (Babel, classic runtime) into the format-3 IIFE the app's self-check parses. |
| `npm run ds:bundle` | the above, then `tools/assemble-ds-bundle.mjs` — copies the layout into `ds-bundle/`, vendors React into `_vendor/`, precompiles the cards, and writes `.ds-build-meta.json` + `_ds_sync.json`. |

So a re-sync is: `npm install && npm run ds:bundle && node .ds-sync/package-validate.mjs ./ds-bundle`.
`cfg.buildCmd` records this. Do **not** hand-edit `_ds_bundle.js` — it is generated.

`tools/build-ds-bundle.mjs` was verified against the previously-shipped bundle:
7 of 12 modules regenerated **byte-for-byte**, and the 5 that differed were
exactly the 5 sources that had changed. That equality check is the way to
verify any future change to the generator.

## 2026-09-19 re-sync

The first sync (2026-07-01) hand-assembled the layout and hand-maintained
`_ds_bundle.js`. Both of those risks had already materialised by this run:

- **The bundle was stale.** `components/core/CircuitRule/CircuitRule.jsx` had
  been rewritten to the confirmed segmented-bands style, but the bundle still
  shipped the old stacked-hairlines-with-nodes version. Fixed by the generator.
- **The cards could not render offline.** Every preview loaded React, ReactDOM
  and Babel from `unpkg.com`. With the CDN unreachable all 7 previews rendered
  an empty root. The assembler now vendors React + ReactDOM into `_vendor/` and
  precompiles the inline `text/babel` blocks, so no CDN and no 3MB Babel
  runtime ship. The repo's own `.html` sources keep their CDN tags and stay
  directly openable; only the `ds-bundle/` copies are rewritten.

Also fixed in this run:

- `CircuitRule.prompt.md`, its card and its `@dsCard` subtitle still documented
  the removed `nodes` prop and called the mark "hairlines ... never bars".
- `.fae-circuit-rule` (tokens/base.css) was still the old six stacked 1px
  lines. It is now the pride bar — six equal blocks, gapless. `<CircuitRule>`
  is the gapped variant; the README says so.
- The ROYGBIV palette sweep (commit `1b722a5`) missed **blue** in three
  places: `guidelines/color-circuit.card.html`, `assets/circuit.svg` and
  `guidelines/brand-logos.card.html` all still carried `#4A9EFF` (the accent
  blue) while `--fae-circuit-blue` is `#1D5BBE`. Aligned to the token.
- `ui_kits/storefront/*` used Vite-absolute image paths (`/model-tee-new.png`)
  that resolve to the origin root outside the dev server — four broken images
  in the storefront starting-point card. Now `../../assets/...`. The hoodie
  and tee images were also swapped relative to their `meta` labels.
- Two cards still announced "Free worldwide shipping" after the store went
  US + Canada only.
- Nine cards under-declared their `@dsCard viewport` and clipped their own
  content; `ProductCard`'s three tiles were stacking full-width (2869px tall)
  instead of sitting in a row. All measured and corrected.
- `Badge`'s circuit-tone row was missing `purple`.
- `readme.md` (the `readmeHeader`) had no "how to build with this" section —
  it never named the `window.FBRIQDesignSystem_0e5da2` global, that there is
  no provider to wrap in, or gave a build snippet. Added and name-validated
  against the built artifacts.

## Verification state

- `package-validate.mjs ./ds-bundle` exits 0. Render check 7/7 clean, 0 bad,
  0 thin, 0 variants-identical, 0 floor cards.
- All 24 cards (7 components + 17 guidelines) and the storefront starting
  point were screenshotted at their declared viewports and graded good on the
  absolute rubric: styled with real tokens and brand fonts, complete, plausible.
- `_ds_sync.json` is now uploaded, so the **next** sync has an anchor and can
  skip unchanged components. `sourceKeys` is deliberately omitted (no authored
  `.tsx` previews to key on) — changed artifacts re-verify rather than falsely
  carrying a grade forward.

## Known render warns (expected, not new)

- `[FONT_REMOTE]` for Instrument Serif / Archivo / JetBrains Mono. The fonts
  load from Google Fonts via `@import` in `tokens/fonts.css`; nothing ships in
  `fonts/`. Not a gap.
- `(render-hash recompute skipped — no .stories-map.json)` — expected for an
  off-script layout.
- `guidelines/brand-logos.card.html` (700x2512) and
  `ui_kits/storefront/index.html` (1280x3017) intentionally exceed their
  declared viewports: both are long-form scrolling documents whose declared
  size is the card "cover". Every other card fits exactly.

## Environment gotchas

- Chromium is at `/opt/pw-browsers` (build **1194**) → install
  **playwright@1.56.0**; the latest release pins a different build and fails
  with "Executable doesn't exist".
- Outbound HTTPS goes through an allowlisting proxy. `fonts.googleapis.com` is
  allowed; `unpkg.com` and `cdnjs.cloudflare.com` are **blocked**. Chromium
  does not inherit `HTTPS_PROXY`, so screenshot scripts must pass
  `chromium.launch({ proxy: { server: process.env.HTTPS_PROXY,
  bypass: "<-loopback>" } })` and load cards over `file://` — routing a local
  HTTP server through that proxy returns the proxy's own error page.

## Re-sync risks

- **`tools/build-ds-bundle.mjs` hardcodes the module list.** A new component or
  ui_kit file will silently not be bundled until it is added to `MODULES`.
  Same for `tools/assemble-ds-bundle.mjs`'s copy list.
- **`assets/print-art/` is deliberately excluded** from the bundle (production
  print masters, ~13MB, not design-system material). Only flat `assets/*` ships.
- **The upload never deletes.** The design project also holds `uploads/`,
  `scraps/`, `compressed/`, `export/`, `faebriq-theme/`, `faebriq-mockups/`,
  `design_handoff_faebriq/` and some root `.html` files that this repo does not
  produce — user-uploaded source material the sync does not own. The plan ships
  `deletes: []` on purpose. Two leftovers from the first sync also survive:
  `assets/circuit-fan.svg`, `assets/circuit-simple.svg` and
  `ui_kits/storefront/README.md`. Re-check before ever widening deletes.
- **`cfg.readmeHeader` is inert here.** With no converter there is nothing to
  prepend to — the assembler copies `readme.md` to `README.md` wholesale, so
  `readme.md` *is* the conventions header. The key is kept to record intent.
- **Screen vs print palette diverge.** `tokens/colors.css` (screen) and
  `design-decisions.md` (locked print hexes) are close but not equal, e.g. red
  `#E8272A` vs `#E8271C`, blue `#1D5BBE` vs `#0057A8`. Left as-is — confirm
  with the founder whether that is deliberate gamut mapping or drift.
- **`guidelines/components-storefront-overview.card.html`** still demos the
  older catalogue ($35 tee, $42 sleeve, old mockups). Accurate as a ProductCard
  specimen, stale as a catalogue. Harmless, but worth a pass one day.
- **`guidelines/brand-logos.card.html` loads IBM Plex Mono**, not the brand's
  JetBrains Mono. Deliberate-looking (it ships its own font link and its own
  `:root`), so left alone — but it is an inconsistency in a guidelines card.
