2026-08-27 — Updated selected equal-visual-cap apparel masters and proof evidence — applies founder-selected fixed-Circuit production system.
2026-08-27 — Generated five transparent 2400 px / 300 dpi sticker masters and validation manifest under assets/print-art/sticker-final-system-2026-08-27/.
Why: Apply the approved sticker lockup system for the SPOKE kiss-cut sticker line; no Shopify or Printify publish/sync performed.
2026-08-30 Centered content-page body text via scoped .fae-page--centered class in faebriq.css; applied to templates/page.liquid + page.contact.liquid on draft theme faebriqtheme-launch-fix. Why: About and other content pages were left-aligned.
2026-08-30 Added brand/social/ 1200x630 og:image card (SVG outlines + editable SVG + PNG). Why: Shopify social sharing image was unset.
2026-08-30 Audited hero 'Shop the Drop' CTA; no fix applied pending confirmation of target collection handle.
2026-09-05 Added AUDIT_2026-09-05.md — independent read-only pre-traffic audit of Shopify, live theme and design-system repo.
Why: verify launch readiness before driving social traffic; four blockers found, no store/Printify changes made.
Note: themes are inverted vs CLAUDE.md — faebriqtheme-launch-fix is MAIN (live); do not publish the -review theme.
2026-09-08 Added SOCIAL_LAUNCH_NOTES.md — reminder to link the Shop app from social profiles once the website is live.
Why: Shop app has a Follow button and in-app checkout, and renders product data only, so it is unaffected by theme work.
Note: gated on fixing product imagery first — Shop app is a pure image grid with no copy to compensate.
2026-09-08 Corrected design-decisions.md from a physical Error 404 tee sample; flagged its pride hex as unresolved.
Why: its tee description (massive 404, small italic phrase) is falsified by the sample, and its hex set exists in no other file.
Also reverted the draft theme's circuit-rule.liquid to the brand-kit palette this session had overwritten on that file's authority.
2026-09-10 Flagged design-decisions.md as sourced from a now-superseded physical sample; founder reports the design changed since 2026-09-08.
Why: prevent the 2026-09-08 sample's hex/layout claims from being read as a live spec by a future session.

2026-09-08 Regenerated 4 apparel print masters (bug/code-it/deploying-identity/off-the-clock) via tools/make_print_file.py.
Why: 2026-08-27's "equal-visual-cap" pass had silently overwritten make_print_file.py's tuned small-line2 lockup; line2 is punchline/payload and reads deadpan only when smaller, per make_print_file.py's own l2_w=0.4710 spec.
Note: sticker-final-system-2026-08-27/manifest.json now describes a superseded state for these 4 slugs; not touched. No Printify/Shopify sync performed.

2026-09-09 Fixed "It's Not a Bug. It's Me." line-2 sizing on both the sticker (final-system) and apparel-4500 masters, via new --l2-w override in tools/make_print_file.py; regenerated sticker-final-system manifest.json.
Why: default l2_w=0.4710 gave this phrase a ~0.98 size ratio (no visible hierarchy) because line2 has just over half of line1's character count — mathematically inherent to the width-fit formula, not a corruption; PR #17's restoration used the same default and did not fix it. --l2-w is opt-in per call; all other designs verified byte-identical.
Note: no Printify/Shopify sync performed.

2026-09-10 Tightened line1->line2 gap ~18% (pixel-shift, no re-render) on all 5 apparel masters + 4 matching sticker masters in assets/print-art/. Why: founder feedback that the gap read too wide on "It's Not A Bug. It's Me."; confirmed not a one-off outlier so applied to all shared-lockup designs.
2026-09-10 Per-design line2 size pass, applied to the gap-tightened baseline (not stacked): It's Not A Bug -> line2 at 85% (apparel+sticker); Code It./Deploying/Off The Clock/404 -> line2 at 75%. Why: founder judged It's Not A Bug's longer line1 needed less shrink than the shorter-phrase designs to read balanced.
Note (merge resolution, PR #19 vs PR #18): this pixel-shift pass and the 2026-09-08/09-09 make_print_file.py regeneration above both touched the same 5 files independently. Resolved in favor of this pass for all 5 (founder-reviewed, side-by-side) — the committed art now reflects the pixel-shift + per-design-scale result, not the --l2-w/small-line2 regeneration. make_print_file.py's --l2-w flag and l2_w spec are kept for future regenerations; sticker-final-system-2026-08-27/manifest.json re-validated against the final files via tools/validate_sticker_final_system.py.

2026-09-16 Added CLAUDE.md clarification that dry/deadpan brand voice is a delivery style, not low-energy/monotone.
Why: Riverside AI-avatar tone draft was written as a flat, no-energy "technician" persona under a literal reading of "dry, deadpan" — founder correctly called it boring/unsellable; locking in the correct interpretation so it isn't regenerated wrong next session.

2026-09-16 Added LAUNCH_AUDIT_2026-09-16.md — competitive research + source-level audit of faebriqtheme-launch-fix (theme 145284005955), catalogue, delivery profiles, markets, orders and discounts.
Why: final go/no-go before social traffic; live site could not be rendered (egress policy blocks faebriq.com and ufyytt-er.myshopify.com), so every check was done against theme source via the Shopify Admin API.
Note: no store, theme or Printify changes made. Headline finding — the MAIN theme is faebriqtheme-launch-2026-08-06-review and carries none of the fixes; publishing launch-fix is the one action gating launch.

2026-09-16 Added SHOPIFY_ADMIN_AUDIT_2026-09-16.md — read-only review of the admin surface the theme audit missed: sales channels, policies, payments, inventory, installed apps, analytics.
Why: founder challenged whether the first audit was complete; it was theme-only. Six new findings, two launch-blocking.
Note: no store/theme/Printify changes. Key items — Refund policy denies size refunds citing a non-existent size guide; 464 sessions have produced 2 cart adds and 0 orders; three AI agents hold write_themes.

2026-09-16 Site review pass: rewrote all 12 product descriptions + SEO fields, Contact and About page bodies (dashes removed, sticker copy de-duplicated); added theme/templates/policy.liquid, unified About page type, stripped dashes from contact template; staged corrected Refund/Shipping/Terms policies in handoff/.
Why: founder review of the live site flagged em dashes sitewide, mixed fonts on About, uncentred policy pages, and AI-sounding copy.
Note: policies and live-theme files could not be written via the connector (read-only legal scope; MAIN theme writes blocked), so both are staged in handoff/ for manual paste. Privacy policy verified dash-free, no change needed.

2026-09-16 Applied 7 template/layout fixes directly to faebriqtheme-launch-fix (new policy.liquid; About type unified; dashes removed from theme.liquid title, hero price line, index.json, collection.liquid sort, contact strings).
Why: founder review flagged mixed fonts on About, uncentred policy pages and em dashes sitewide; theme had flipped back to unpublished so connector writes were permitted.
Note: themes swapped again at 11:01:43Z (review became MAIN). Connector cannot publish or unpublish, so an external actor did it; three AI apps hold write_themes. product.liquid left for manual edit (2 entities) to avoid retyping its cart JS.

2026-09-16 Added handoff/homepage-options.html: side-by-side mockup of two homepage hero layouts (A typographic, B split with product shot), plus the competitor-research figures behind the call.
Why: founder asked to see both options before choosing a homepage structure that features products above the fold.
Note: published as an artifact for viewing. Product tiles are CSS, not real renders, so the comparison stays about layout.

2026-09-16 Built Option B homepage into faebriqtheme-launch-fix: split hero (wordmark beside a product shot, product picked via theme setting), new sitewide announcement bar, new trust row, curated 6-product grid; mirrored the 7 files into theme/.
Why: founder chose Option B from the two hero mockups; competitor research put a product, free shipping and trust facts above the fold.
Note: trimming the grid to 6 broke the catalog section's count ("12 products" over 6 cards) and its filter rail (filtering a 12-type rail over 6 cards emptied the grid), so both are now conditional on the grid holding the full collection. Also removed the last en dash, in its A-Z sort option.

2026-09-17 Published the All Products collection to the Online Store sales channel. It was published to zero channels.
Why: the homepage catalog section rendered its "select a collection" placeholder and /collections/all-products was unreachable, because an unpublished collection resolves to nil on the storefront even though the Admin API returns it normally.
Note: Online Store only. Shop, TikTok, POS and Manus left as they were, since those are separate distribution decisions.

2026-09-17 Added handoff/MANUS_BRIEF.md: a self-contained browser task brief covering the three policy replacements, the two product.liquid string edits, a sticker artwork investigation, and a homepage render check.
Why: the remaining launch items all need a logged-in browser session, which the Shopify connector cannot provide. Manus can.
Note: the three policy bodies are embedded in full so the brief needs no repo access, and the standing brand rules (no Printify sync, no price or handle changes, no theme publishing, no embroidery claim, no dashes) are stated as hard constraints.

2026-09-17 Added handoff/MANUS_BRIEF_2.md for a second Manus account: policies, the two product.liquid strings, and the sticker investigation, reordered by value and capped by time.
Why: the first run drained its credits on Shopify admin routes that never rendered, and completed none of the three.
Note: drops the homepage checks the first run already confirmed, routes around the SPA stall with deep links and a legacy-host fallback, sets hard attempt caps, and makes Task B conditional on the theme still being published.

2026-09-17 Applied the two product.liquid dash replacements directly to faebriqtheme-launch-fix (Made to order line, Production 5 to 7 line), byte-verified. Mirrored into theme/.
Why: last of the sitewide dash cleanup, held back earlier because the connector cannot write to a live theme and the file carries the cart JS.
Note: theme was unpublished by the founder for this edit; publish to see it live. No other line in the file touched.

2026-09-19 Added an Output style section to CLAUDE.md: no em dashes or en dashes in any output, hyphens still allowed.
Why: the founder wants the existing store-copy dash ban applied to chat replies and reports too, not just shipped strings.
Note: rule text only. No existing dashes elsewhere in the repo were touched.

2026-09-22 Removed all 13 em and en dashes from the four policy drafts in legal/ (ranges now read "2 to 7", parenthetical dashes rewritten as commas or full stops).
Why: the Output style rule merged in PR #22 bans dashes in store copy, and the earlier sitewide cleanup covered theme strings only, never legal/.
Note: wording is otherwise untouched and the drafts already carried their Last Updated lines. The four live Shopify policies still need a manual paste: the connector lacks write_legal_policies.

2026-09-22 Added POST_LAUNCH_TOOLS.md, logging Triple Whale and Postscript as later-stage growth tools to revisit once the store has traffic.
Why: keep post-launch tooling ideas somewhere durable without drifting MEMORY.md (current-state only) or misfiling under SOCIAL_LAUNCH_NOTES.md (social-channel-specific).

2026-09-22 Added IMAGE_INVENTORY_2026-09-22.md, built from the media on the live Shopify store (13 products, 52 images, 3 systems).
Why: to scope the imagery launch blocker before any art gets redone.

2026-09-22 Rewrote alt text on 35 live Shopify images: em dashes out, "embroidery" removed from the archived Slim Cap, circuit wording unified as "six-color rainbow pride stripe".
Why: no em dashes in store copy, never claim embroidery, and alt text now uses terms people search. Imagery decision board: https://claude.ai/artifact/9zSaBXjVRRWu1AV1kVHdtA

2026-09-23 Locked the imagery spec (IMAGERY_SPEC_2026-09-23.md: 4:5, studio hero, 4 fixed slots, serif lockup, FAEBRIQ under the stripe on stickers) and moved the flat studio shot to first on the 4 single stickers and the Sticker Sheet (live).
Why: these are Maurice's picks from the decision board. Theme card ratio NOT changed, because launch-fix is now the live theme and the tool cannot write to it.

2026-09-23 Set product cards and mobile product gallery to 4:5 in faebriqtheme-launch-fix (unpublished), faebriq.css only, uploaded and checksum-verified.
Why: the 4:5 imagery spec letterboxes inside square cards.

2026-09-23 Spec and decision board: added the FAEBRIQ spelling rule and banned the old repo mockups (garbled wordmark, wrong 404 art). The board slot examples now use the real print files.
Why: Maurice caught the misspelled brand and the wrong 404 design on the board.

2026-09-23 Set the canonical 404 design from Maurice's reference (big 404, one-line STRAIGHT NOT FOUND, stripe). Added the v3 print files (apparel 4500, sticker 2400 with FAEBRIQ), tools/make_404_v3.py and the reference image. Retired the ERROR 404 files in the spec.
Why: the repo 404 masters did not match the approved design.

2026-09-23 Added SOCIAL_LAUNCH_POSTS_2026-09-23.md: 9 Instagram launch posts (grid order, readiness per imagery spec) and 2 LinkedIn founder posts.
Why: store is open, Maurice asked for the first social posts.

2026-09-23 Rendered IG launch posts 1 and 2 as 10 slides (1080x1350) in assets/social/launch-2026-09, built by tools/make_social_slides.py.
Why: Maurice asked for the text carousels as ready-to-post images.

2026-09-23 Added an approved social bio copy entry to SOCIAL_LAUNCH_NOTES.md (Instagram/X/Threads/Bluesky and TikTok bios, plus an implementation note).
Why: founder-approved copy for a future manual account setup, logged so it isn't lost before accounts exist.

2026-09-23 Set the wordmark: sans FÆBRIQ (reference saved in assets/print-art/reference), bar at 1.35x wordmark width. Applied to IG post 1 slide 1, rule added to IMAGERY_SPEC.
Why: Maurice picked the middle version from three options.

2026-09-24 Updated CLAUDE.md stable facts: wordmark is sans FÆBRIQ with a 1.35x bar, not Instrument Serif. Product phrase lockups keep Instrument Serif.
Why: matches the 2026-09-23 wordmark decision, so future sessions do not follow the stale rule.

2026-09-24 Swapped the serif FAEBRIQ signature mark for the approved sans wordmark on all 6 sticker print files (phrase lines and bar untouched, hand-tuned pixel positions preserved) and fully rebuilt the two cap wordmark files at print resolution (3000px, was 500x200 placeholder scale) via new tools/swap_print_wordmark.py.
Why: match the 2026-09-23 wordmark decision; cap files also carried no real print resolution before.

2026-09-25 Fixed two print-lockup rules per Maurice: line1 is 100%, line2 is 75-85% of line1 (LINE2_RATIO_DEFAULT=0.80, replaces the old width-fit l2_w mechanism which sometimes gave near-zero size difference); the bar next to a printed wordmark is 1.35x that wordmark width (BAR_TO_MARK_RATIO), not the old ~7x phrase-width bar. Regenerated the 5 live stickers and the 404 v3 print files in tools/make_print_file.py and tools/make_404_v3.py, re-swapped the sans mark, corrected CLAUDE.md (product prints use Bodoni Moda, not Instrument Serif) and IMAGERY_SPEC.
Why: Maurice flagged the shipped stickers as wrong on both counts.

2026-09-23 Added faebriq_batch_v1: 10 transparent 4500x5400 terminal-style tee graphics for black garments (tools/make_batch_v1.py, manifest.json, left-chest crops) plus ETSY_LISTING_01_2026-09-23.md.
Why: Maurice asked for a 10-design batch and a corrected Etsy metadata package for listing #1.

2026-09-23 Added ETSY_LISTING_02_2026-09-23.md: corrected Etsy package for listing #2 (clean build).
Why: supplied package had 2 over-length tags and unverified fabric claims.

2026-09-23 Added faebriq_batch_v2: 2 designs (chown-identity, npm-liberation) via make_batch_v1.py --batch v2.
Why: Maurice approved the two strongest picks from the external concept list.
