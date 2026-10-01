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
  width wherever the wordmark prints (stickers, cap, standalone logo);
  the apparel front print has no wordmark; its bar runs the full print
  width (~4050-4090px on a 4500px file), whatever the text width. Locked
  2026-10-01: do not resize apparel bars or regenerate tee prints for it. Tees carry a small FÆBRIQ wordmark on the sleeve
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
  (SPOKE) at a flat $4.99 US / $7.99 CA via the "Stickers (SPOKE)" shipping
  profile (2026-10-01). Never write "free shipping on everything".
- Live catalog (repriced in Shopify 2026-10-01, cheapest with reasonable
  profit): 6 tees (404, Code It, Deploying, Not A Bug, Off The Clock, Please
  Hold) $30; crewneck $42; hoodie $54; cap $32; ONE price for every size,
  never charge more for bigger sizes (Maurice, 2026-10-01); 404 tote $34; 5 single stickers
  $4 to $6 and sticker sheet $11.99 to $13.99 (6x4 only) (3 active, 3 Draft).
  A Printify publish resets Shopify prices, images and copy.
- Fulfillment: Printify. Stickers = SPOKE kiss-cut. Tote = AS Colour 1001
  (Fulfill Engine). Cap = OTTO 18-253 via Printify Choice, DTF — embroidery
  is UNVERIFIED; never claim embroidery anywhere.
- Themes: `faebriqtheme-launch-fix` = production candidate.
  `faebriqtheme-launch-2026-08-06-review` = LIVE. Never publish themes
  without an explicit instruction.

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
