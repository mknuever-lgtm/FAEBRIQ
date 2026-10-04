2026-08-27 — Updated selected equal-visual-cap apparel masters and proof evidence — applies founder-selected fixed-Circuit production system.
2026-08-27 — Generated five transparent 2400 px / 300 dpi sticker masters and validation manifest under assets/print-art/sticker-final-system-2026-08-27/.
Why: Apply the approved sticker lockup system for the SPOKE kiss-cut sticker line; no Shopify or Printify publish/sync performed.
2026-08-30 Centered content-page body text via scoped .fae-page--centered class in faebriq.css; applied to templates/page.liquid + page.contact.liquid on draft theme faebriqtheme-launch-fix. Why: About and other content pages were left-aligned.
2026-08-30 Added brand/social/ 1200x630 og:image card (SVG outlines + editable SVG + PNG). Why: Shopify social sharing image was unset.
2026-08-30 Audited hero 'Shop the Drop' CTA; no fix applied pending confirmation of target collection handle.
2026-09-05 Added AUDIT_2026-09-05.md — independent read-only pre-traffic audit of Shopify, live theme and design-system repo.
Why: verify launch readiness before driving social traffic; four blockers found, no store/Printify changes made.
Note (corrected 2026-09-29, verified in Shopify): this note was wrong. faebriqtheme-launch-2026-08-06-review is MAIN (live); faebriqtheme-launch-fix is UNPUBLISHED. Themes match CLAUDE.md. Do not publish either without an explicit instruction.
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

2026-09-25 Design-sync re-sync to claude.ai/design. Added tools/build-ds-bundle.mjs + tools/assemble-ds-bundle.mjs (npm run ds:bundle) so _ds_bundle.js is generated from the real component sources instead of hand-maintained, and bundle previews vendor React locally instead of loading it from unpkg.
Why: the shipped bundle still contained the superseded CircuitRule (stacked hairlines, not the confirmed segmented pride bar), and every preview card rendered blank wherever the CDN was unreachable.
Also corrected: the ROYGBIV sweep had missed circuit blue (#4A9EFF -> #1D5BBE) in color-circuit/brand-logos/circuit.svg, .fae-circuit-rule and CircuitRule docs still described the old style, ui_kits storefront images used Vite-absolute paths, and two cards still said "free worldwide shipping".

2026-09-27 CLAUDE.md catalog line and SOCIAL_LAUNCH_POSTS tote price corrected to match Shopify: tote is $34 (was listed $42), 3 of 6 sticker listings are still Draft.
Why: synced repo, Notion HQ and To-Do tracker against live Shopify data.

2026-09-27 Added ETSY.md placeholder codifying channel rules for a not-yet-live Etsy shop (brand facts carry over, catalog/SEO can differ per channel, same hard gates).
Why: same brand new channel is coming, future sessions should not improvise brand or gate decisions when it goes live.

2026-09-28 Read-only Shopify Admin verification session, no repo or store changes made. Confirmed live About/Contact pages and theme.liquid all say "United States and Canada" consistently (no meta-description conflict found); shop country is Canada (no false US-presence claim); 241 sessions and 0 orders in the last 30 days; no Etsy app installed in Shopify.
Why: Maurice asked to verify open questions from a prior store status check before deciding next steps.
2026-09-29 Shopify cleanup after Printify publish: restored locked prices (tees $34/36/37, crewneck $62, hoodie $68, stickers $4/5/6), archived duplicate Error 404 tee and Liberty tote, rewrote Off The Clock and Please Hold tee copy/tags/SEO (Embroidery tag removed), fixed Not A Bug title, added alt text to 24 apparel images, filled both collections.
Why: the Printify publish had overwritten Shopify prices, images and copy. Old 4:5 crewneck/hoodie/sticker shots were deleted by that publish, not recoverable from Shopify Files.
2026-09-30 Restored the 404 tee (reactivated product 10274729820227: locked prices, brand copy, tags, SEO, alt, All Products) and fixed Not A Bug tee SEO. Why: the original 404 listing had been repurposed into the Not A Bug tee, leaving no 404 tee live.
2026-10-01 Tees keep the sleeve FÆBRIQ wordmark (wordmark-faebriq-sleeve.png): CLAUDE.md apparel rule updated, sleeve line added to the 404 and Code It tee descriptions in Shopify. Why: Maurice chose to keep the sleeve mark found in Printify; front prints still carry no wordmark.
2026-10-01 Added assets/print-art/please-hold-rebranding-identity-light-4500.png (Bodoni, line2 at 80%, bar spans the wider line2); make_print_file.py now shrinks line1 instead of line2 when line2 overflows. Why: the Printify Please Hold tee used the retired Inter print and no Bodoni apparel master existed; the old fallback broke the 75-85% rule.
2026-10-01 Locked the apparel bar rule as-is in CLAUDE.md: full print width on every tee front, no resizing. Why: Maurice chose least rework; measured bar/text ratio already varies 1.02 to 1.30 across the six tee masters.
2026-10-01 Added handoff/MANUS_BRIEF_FONTS_2026-10-01.md: Manus prompt to swap the Please Hold and Deploying tee fronts to the Bodoni masters (mockups-only publish) and report fonts on crewneck, caps, sticker sheet. Why: make tee fonts consistent without more redesign.
2026-10-01 Sticker sheet: deleted the three 11x8.5 variants in Shopify (6x4 White/Transparent $11.99, Holographic $13.99 remain); 11x8.5 also unticked in Printify by Maurice. Why: the 11x8.5 sheet has four print areas and only one carried art.
2026-10-01 Please Hold and Deploying tees now serif in Shopify; set both to $34/36/37, gave Deploying tee FÆBRIQ title, copy, tags (Embroidery etc. removed), SEO, alt text; both added to All Products. Why: finish the font fix and match the other tee listings.
2026-10-01 Not A Bug tee: FÆBRIQ title, house-format copy with size guide and sleeve line, tags, $34/36/37, alt text, All Products. Also restored $34/36/37 on 404 and Code It tees, $62 on crewneck, and alt text on all three. Why: a 06:11 UTC Printify sync reset prices, tags and alt text again.
2026-10-01 Repriced to the cheapest level with reasonable profit (Printify unit cost + est. shipping + 2.9%+$0.30): tees $30/32/33/34, crewneck $42/44/45, hoodie $54/56/58, cap $32; tote stays $34; stickers unchanged pending real Printify sticker shipping. Why: Maurice wants prices people will pay to get first sales.
2026-10-01 One price for all sizes: tees $30, crewneck $42, hoodie $54 (2XL+ lowered to base). Why: Maurice/Sarah, size-based upcharges upset customers; rule added to CLAUDE.md.
2026-10-01 Stickers get a flat shipping rate ($4.99 US / $7.99 CA, profile set up via handoff/MANUS_BRIEF_STICKER_SHIPPING_2026-10-01.md); free-shipping copy narrowed to apparel/cap/tote in launch-fix theme (announcement, trust row, hero note, product template), About page, sticker descriptions, CLAUDE.md. Why: SPOKE sticker shipping (~CAD 13 to Canada) made every sticker-only order a loss.
2026-10-01 Canada sticker rate $7.99 -> $9.99 (repo, launch-fix product template, About page, 6 sticker descriptions, Manus brief); 404 Cotton Tote set to Draft. Why: SPOKE ships to Canada at ~USD 9.54, and Fulfill Engine shows the AS Colour tote at 0 variants in stock.
2026-10-01 Moved 62 apparel variants (6 tees, crewneck, hoodie) from Printify-created paid shipping profiles into the free General profile, plus 1 stray sticker variant into Stickers (SPOKE). Why: checkout was charging shipping on "free shipping" apparel. Muse brief for policy + meta + checkout check.
2026-10-01 Added the Printify location to the "Stickers (SPOKE)" shipping profile (Manus created it with only 164 Finch Ave E). Why: stock lives at Printify, so stickers had no shipping origin and showed Sold out on the storefront.
2026-10-01 Sticker descriptions (5 singles): size bullet now lists 2" and notes 2" is transparent-only (Deploying has both). Why: copy said 3"/4"/6" but every sticker sells a 2".
2026-10-01 Tote switched to the Liberty canvas tote (product 10274729852995): unarchived, house title/copy/tags/SEO/alt, $34, All Products, free General shipping profile, handle 404-straight-not-found-tote. AS Colour tote stays Draft, handle now -as-colour. Why: Fulfill Engine shows 0 stock; Liberty costs $9.67 vs $20.44. Manus brief for per-product Printify shipping costs.

2026-10-01: added assets/mockups/2026-10-01/ (27 Printify mockups + REPORT.md from Manus).
2026-10-01: Shopify: added 15 new-angle mockups (tee collar+folded x6, hoodie collar+folded, crewneck folded) with alt text; skipped fronts/cap/tote as duplicates of existing images.
2026-10-01: Shopify apparel+tote galleries rebuilt on charcoal (#0d0d0d, 4:5) via tools/mockup_to_charcoal.py; all white-ground and duplicate images deleted; 09-24 on-model shots back as slot 2 on 404 and Code It tees. Why: Maurice, no white backgrounds, no filler.
2026-10-01: Added 404-straight-not-found-tote-4500.png (tools/make_404_tote.py, sticker lockup with sans FÆBRIQ) and handoff/MANUS_BRIEF_TOTE_PRINT_SWAP_2026-10-01.md. Why: live tote prints a serif FÆBRIQ and a full-width bar.
2026-10-01: Re-composited correct prints (serif phrase, six-block bar, sans FÆBRIQ) onto existing dark model photos via tools/composite_print.py; 7 on-model shots live as slot 2 (4 tees, hoodie, crewneck, cap; cap alternate view removed). 2 tote shots held in assets/product-images/2026-10-01-model/ until the Printify swap. Why: Maurice, model pictures, dark aesthetic.
2026-10-01: Fixed old-print specks on the Off The Clock tee model shot (re-healed, re-uploaded). Added handoff/MANUS_BRIEF_MODEL_PHOTOS_2026-10-01.md: 10 multiracial models, blank garments, for compositing with true perspective. Why: Maurice wants a multiracial cast and prints that sit on the fabric.
2026-10-03: Tote brief now points to 404-straight-not-found-v3-tote-light-4500.png (phrase-width bar + sans FÆBRIQ, rule set 2026-10-01 on hero-fixes branch); removed my short-bar tote file and its 2 model composites. Why: they broke the 404 bar exception.
2026-10-04: Shopify: FÆ stickers moved to Stickers (SPOKE) profile; FÆ collection filled (5); em dashes removed (FÆ sheet title, Sticker Add-Ons, All Products, launch-fix announcement); launch-fix FÆ row subtitle + $3.99 price note.
2026-10-04: Product galleries re-rendered on the charcoal studio sweep (option 3) via tools/mockup_to_charcoal.py, 25 images replaced; close-ups cropped to 4:5.
2026-10-04: CLAUDE.md + IMAGERY_SPEC merged with hero-fixes branch (404 bar exception, launch-fix-only theme rule) plus FÆ catalog, photo ground, post-publish shipping-profile rule.
