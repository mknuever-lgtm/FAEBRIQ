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

2026-09-23 Restored the size guide on the live 404 Tee description after the Manus rewrite dropped it (same block as the Code It Tee; same S to 5XL Gildan 5000). Manus copy kept.
Why: the size guide is a conversion must-have and the prompt never told Manus to keep it.

2026-09-23 Live descriptions: Crewneck and Hoodie size tables moved into the same collapsible Size guide the tees use (contents unchanged). Cap "six-colour" changed to "six-color".
Why: consistent product pages and US spelling. The other 9 descriptions were already on-brand and left alone.

2026-09-24 After the Manus image run: moved the new in-hand shot to slot 3 on the 4 single stickers, and deleted the 4 retired square italic-404 images from the 404 Sticker (the in-hand shot is now its only image).
Why: slot order per IMAGERY_SPEC, and no retired design live. The new tee and tote images still need a visual check.
2026-09-24 Added cap print file v2 (assets/print-art/cap-wordmark-v2-print.png, 3360x593 transparent, 300 dpi) and its generator tools/make_cap_v2.py: flat six-block stripe over FÆBRIQ in Inter SemiBold.
Why: the cap design changed after the sample and the repo only had 520px previews; this is the reference file for Muse and for the Printify DTF print.
2026-09-24 Added cap print file v3 (tools/make_cap_v3.py): FÆBRIQ in Inter SemiBold on top, flat stripe underneath, three stripe widths (1.1x, 1.35x, 1.7x the word) plus a comparison sheet.
Why: Maurice wants the render's wordmark font, the stripe under the word like the rest of the brand, and the stripe at least as wide as the word.
2026-09-25 New print system for every product (tools/make_print_system.py, assets/print-art/system-2026-09-25/): Inter SemiBold, line 2 at 75%, stripe 1.35x the widest line, wordmark on stickers and tote only, FÆBRIQ logo on apparel sleeves and cap.
Why: Maurice's call to put every product in one system; older print files and the 2026-09-24 images are retired in IMAGERY_SPEC. Added handoff/MANUS_BRIEF_3.md to rebuild Printify, reshoot 4 images per product and publish.
2026-09-25 Print system: line 2 size now set per design (404 0.60 so the 404 reads bigger, Code It 0.85, Off The Clock 0.72, Deploying 0.75, Not A Bug 0.80, Please Hold 0.58). Why: Maurice asked for a per-design judgment in the 55 to 90% range.
