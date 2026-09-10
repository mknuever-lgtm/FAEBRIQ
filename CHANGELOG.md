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
