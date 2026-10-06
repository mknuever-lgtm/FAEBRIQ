# FAEBRIQ — Session Rules

## Prime directive
Act ONLY on direct instructions given in this session. Do NOT resume prior
threads, scan for open items, run audits or verifications, or open pull
requests unless explicitly asked. When the assigned task is done, stop.

## Reads — keep context small
- Do NOT read MEMORY.md, PRODUCTION_BRIEF.md, .design-sync/, or any archive/
  file unless the task explicitly requires history.
- Do NOT read image files, _ds_bundle.js, or _ds_manifest.json unless the
  task is design-sync work.
- If unsure whether something is in scope: ask one short question, then wait.

## Logging
- No PRs for logs. No PRs at all unless requested.
- If a task changes repo state, append at most 3 lines to CHANGELOG.md:
  date, what changed, why. Nothing else.

## Stable facts — trust these, do not re-verify each session
- Brand: queer-coded dark-tech merch. Voice: dry, deadpan, terminal wit.
  Sans FÆBRIQ wordmark (reference: assets/print-art/reference/wordmark-reference-2026-09-23.jpg)
  with a six-block bar at 1.35x its width, on near-black (#0f0e0c bg / #e0e0e0 text).
  Phrase lockups (product prints) keep Bodoni Moda (corrected 2026-09-25;
  an earlier version of this line wrongly said Instrument Serif). Line 1
  is 100% size, line 2 is 75-85% of line 1. Bar is 1.35x the wordmark's
  width wherever the wordmark prints (cap, standalone logo, non-404
  stickers); the apparel front print has no wordmark; its bar runs the full
  print width (~4050-4090px on a 4500px file), whatever the text width.
  Locked 2026-10-01: do not resize apparel bars or regenerate tee prints for
  it. Exception: every 404 file keeps the full phrase-width bar; the 404
  tote and 404 stickers add the sans FÆBRIQ underneath (Maurice,
  2026-10-01; tote file assets/print-art/404-straight-not-found-v3-tote-light-4500.png).
  Tees carry a small FÆBRIQ wordmark on the sleeve
  (wordmark-faebriq-sleeve.png, kept by Maurice 2026-10-01).
  One pride-circuit accent per product.
- Dry/deadpan = delivery style, NOT low-energy, monotone, or flat. Any
  marketing copy, avatar/video persona, or promotional content still needs
  a hook, charisma, confident energy, and comedic timing. Deadpan means the
  joke isn't oversold, not that there's no energy behind it. Rendering this
  as a bored technician reciting specs is a bug — always re-read output for
  "does this sound boring" before treating dry/deadpan instructions as done.
- Store: Shopify, faebriq.com, USD, ships US + Canada only. Free shipping
  baked into prices for apparel, cap and tote. Stickers + sheet ship separately
  (SPOKE) at a flat $4.99 US / $9.99 CA via the "Stickers (SPOKE)" shipping
  profile (2026-10-01). Never write "free shipping on everything".
- Live catalog (repriced in Shopify 2026-10-01, cheapest with reasonable
  profit): 6 tees (404, Code It, Deploying, Not A Bug, Off The Clock, Please
  Hold) $30; crewneck $42; hoodie $54; cap $32; ONE price for every size,
  never charge more for bigger sizes (Maurice, 2026-10-01); 404 tote $34 (Liberty canvas, switched from AS Colour 2026-10-01); 5 single stickers
  $4 to $6 and sticker sheet $11.99 to $13.99 (6x4 only) (3 active, 3 Draft);
  FÆ mascot stickers (added 2026-10-03, collection `fae`): 4 kiss-cut
  $3.99 to $7.99 and FÆ Sticker Sheet: Four Poses $12.99 to $19.99.
  A Printify publish resets Shopify prices, images and copy, and drops new
  variants into Printify-made shipping profiles: move sticker variants into
  "Stickers (SPOKE)" and apparel into "General profile" after every publish.
- FÆ = the locked promoter mascot (Notion: FÆBRIQ Content OS). Apparel is
  the hero, FÆ presents.
- Product photos (Maurice, 2026-10-04): charcoal studio sweep, #19191B
  corners to ~#2E2E30 behind the product, 4:5 at 2048x2560, made with
  tools/mockup_to_charcoal.py. Never white or light backgrounds. Gallery
  order: front, on-model, close-up, folded.
- Fulfillment: Printify. Stickers = SPOKE kiss-cut. Tote = Liberty canvas tote 15x16 (AS Colour 1001 via Fulfill Engine is Draft, out of stock)
  Cap = OTTO 18-253 via Printify Choice, DTF — embroidery
  is UNVERIFIED; never claim embroidery anywhere.
- Themes: `faebriqtheme-launch-fix` = production candidate.
  `faebriqtheme-launch-2026-08-06-review` = LIVE. Never publish themes
  without an explicit instruction. `faebriqtheme-launch-fix` (Shopify id
  145284005955) is the ONLY theme Claude may edit; never write to any other
  theme (Maurice, 2026-10-01).

## Output style
- No em dashes and no en dashes in any output: chat replies, reports,
  briefs, store copy, theme strings, commit messages. Hyphens are fine
  (compounds, ranges, handles). Rewrite with commas, colons, or a full
  stop instead.

## Hard gates
- No purchases or sample orders without checkout-screen confirmation.
- No Printify→Shopify publishes or syncs (they overwrite Shopify edits).
- No new products, price changes, SEO/handle changes, or collection edits
  beyond the scoped task.
- Every order must clear a profit after Printify item + shipping cost and
  payment fees (Maurice, 2026/10/06). No discount code, sale or price cut that
  breaks it. Keep tees out of codes and sales unless the numbers are re-checked
  (thinnest case: biggest-size tee to Canada, about $0.74).
