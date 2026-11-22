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
  baked into prices for apparel, cap and tote. Stickers + sheets ship via the
  "Stickers and Sheets" shipping profile: $4.99 US / $9.99 CA under $50,
  free at $50 and over (verified in Shopify 2026-11-22; the SPOKE profile
  holds only the Archived "Kiss-Cut Stickers"). Never write "free shipping
  on everything".
- Live catalog (repriced in Shopify 2026-10-01; tees raised $30 to $32 on
  2026-10-06 after Printify costs showed large-size Canada tees losing
  money at $30): 6 tees (404, Code It, Deploying, Not A Bug, Off The Clock,
  Please Hold) $32; crewneck $42; hoodie $54; cap $32; ONE price for every size,
  never charge more for bigger sizes (Maurice, 2026-10-01); 404 tote $34
  (AS Colour, handle 404-straight-not-found-tote-as-colour) is DRAFTED since
  2026-11-14, out of stock: relist only when Printify shows stock; the
  Liberty canvas tote (handle 404-straight-not-found-tote) is ARCHIVED
  (verified in Shopify 2026-11-22); 5 single stickers
  $4 to $6 and sticker sheet $11.99 to $13.99 (6x4 only) (3 active, 3 Draft);
  FÆ mascot stickers (added 2026-10-03, collection `fae`): 4 kiss-cut
  $3.99 to $7.99 and FÆ Sticker Sheet: Four Poses $12.99 to $19.99.
  FÆ Doll Kiss-Cut Sticker is LIVE on purpose (Maurice kept it live
  2026-11-17; $4.99 to $5.99). The FÆ "Mascot Poses" sheet is Archived.
  A Printify publish resets Shopify prices, images and copy, and drops new
  variants into Printify-made shipping profiles: move sticker variants into
  "Stickers and Sheets" and apparel into "General profile" after every publish.
- Front-print height LOCKED (Maurice, 2026-10-10): print centre at mid rib
  cage, 0.65 of the way from collar seam to armpit (chest-logo / pendant
  height). Applies to every on-model photo and any placement check.
  Approved references: assets/mockups/2026-10-10-on-model/. Tool:
  tools/move_print_on_model.py and tools/place_print_on_model.py (default 0.65). Spec: PRINT_PLACEMENT_SPEC.md.
  MEASURE IT RIGHT: armpit = the underarm crease where the inner arm leaves
  the torso, NOT the shoulder or sleeve seam (on dropped-shoulder hoodies
  that seam sits far higher and puts the print too high). Collar = front
  neckline seam (hoodie: bottom of the hood V).
- FÆ = the locked promoter mascot (Notion: FÆBRIQ Content OS). Apparel is
  the hero, FÆ presents.
- Product photos (Maurice, 2026-11-18, replaces the 2026-11-17 grey 81
  and 2026-10-04 charcoal rules): real studio look, the garment lying on a
  dark grey table under one lamp. Table ~42 at the corners, a soft lamp
  halo around the garment (hot spot ~140 behind it), a soft contact shadow
  under the hem, faint table grain, 4:5 at 2048x2560. Made with
  tools/mockup_to_charcoal.py (old filename kept). A flat gradient with no
  visible lamp is a bug, not the look. Never white
  or light backgrounds. Model shots: straight-on (no 3/4 turn), print
  centred, hoodie drawstrings tied clear of the print. Gallery order:
  front, on-model, close-up, folded; 4:5 only, no banner crops in galleries.
  Close-up = the full front print (tool flag --print-closeup on the front
  flat), never Printify's collar close-up that cuts the slogan off.
  Alt text describes the image as it is, never the target spec.
- Image record (Maurice, 2026-10-15): every Shopify image upload is saved
  to imagery/shopify/ with a row in imagery/MANIFEST.csv the same day
  (product, Shopify image ID, gallery position, SHA-256). Replaced or
  deleted images get their row updated, not left stale.
- Fulfillment: Printify. Stickers = SPOKE kiss-cut. Tote = AS Colour 1001 via Fulfill Engine (Draft since 2026-11-14, out of stock); Liberty canvas tote 15x16 is Archived (verified in Shopify 2026-11-22)
  Cap = OTTO 18-253 via Printify Choice, DTF. Embroidery verified not
  applicable (2026-11-19): Duplium offers DTF only for this blank; never
  claim embroidery anywhere.
- Themes: `faebriqtheme-launch-fix` = LIVE (MAIN, verified in Shopify
  2026-11-03): any edit to it is public at once.
  `faebriqtheme-launch-2026-08-06-review` = unpublished. Never publish themes
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
- Printify→Shopify publishes are allowed (Maurice, 2026-11-19) only with
  this checklist, because a publish can overwrite Shopify edits:
  1. Before: snapshot from Shopify the title, description, SEO title and
     description, handle, tags, product type, collections, every variant
     price, gallery order, alt text and the on-model images.
  2. In the publish dialog, publish only what the task needs (e.g. mockups);
     untick title, description, prices, tags and shipping where possible.
  3. After: every size at the one locked price (tees $32), copy/SEO/handle
     match the snapshot, variants back in "General profile" (stickers in
     "Stickers and Sheets"), gallery order and on-model images restored, alt
     text redone. Any price drop must still clear the profit rule below.
- No Printify artwork, file, placement or scale changes (swaps, re-uploads,
  moves) without Maurice's explicit OK in that session (Maurice, 2026-10-10:
  earlier sessions swapped his apparel files without asking).
- No new products, price changes, SEO/handle changes, or collection edits
  beyond the scoped task.
- Every order must clear a profit, even 70 cents (Maurice, 2026-10-07).
  Never create a discount code, sale price, bundle or shipping change that
  can push any size or destination (incl. Canada, largest sizes) below
  Printify cost + shipping + payment fees. Check Printify costs first
  (2026-10-06 table: tees $16.48 to $20.34, Canada shipping $9.69).
