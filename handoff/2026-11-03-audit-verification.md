# Pre-launch audit: verification pass (2026/11/03)

Checks the latest external audit against live Shopify (Admin API), Gmail and this repo.
faebriq.com itself was not reachable from the session, so storefront text was read from the live theme files.

## Must fix before unpausing

| # | Finding | Evidence | Status |
|---|---|---|---|
| 1 | Homepage hero says "Vol. 1 · Now Live" while the plan is "Pause and Build" | Live theme `templates/index.json` | Repo mirror changed to "Vol. 1 · Opening soon". Live theme NOT yet changed. |
| 2 | About page: "FÆBRIQ is built by queer technologists, supporting community initiatives year-round." Solo founder, no initiative named | Shopify page `about` | Open. Proposed: "FÆBRIQ is built by one queer developer in Toronto. Year-round. Not Q2." |
| 3 | Sticker Add-Ons says "The 5 single sticker designs"; collection holds 3 | Collection `stickers-add-ons` | Open. Proposed: "Single kiss-cut stickers, 3x3, 4x4 or 6x6." |
| 4 | Sender email: store email is support@faebriq.com; Shopify "Verify your email address" mail arrived | Shopify shop info, Gmail | Maurice: click the verify link. |

## Worth doing, not urgent

- All Products says "The full FÆBRIQ catalog" but holds 11 of 18 active products.
- Tee blank: all 6 tee pages say 100% cotton, 180 g/m2, tubular knit, no side seams (Gildan 5000 spec, not Bella+Canvas 3001). Confirm one tee blueprint in Printify to close the conflict.
- Margins: repo cost table matches. Worst-case tee (USD 32.00 less USD 20.34 item and USD 9.69 Canada shipping) is USD 1.97 before fees, USD 0.74 after 2.9% + USD 0.30, USD 0.55 after 3.5% + USD 0.30. The audit labelled USD 0.74 "before fees": wrong label, same conclusion.

## Audit points that need no action

- Cap copy never claims embroidery; a DTF note is optional.
- Drafts: 3 text-sticker drafts plus 2 parked FÆ drafts (2026/10/23) plus the AS Colour tote draft. All already Draft.
- Sessions: now 771 all-time, 6 cart adds, 7 checkouts, 0 orders (the audit's 489 is stale).
- The audit prompt lists the tote as AS Colour 1001; the live tote is Liberty canvas (since 2026/10/01).

## New, not in the audit

- Shopify contact-information policy shows a phone number and a North York street address publicly. Check it is not a home address.
- Live theme is `faebriqtheme-launch-fix` (MAIN). CLAUDE.md said the review theme was live; corrected.
- Shipping policy promises "Additional regions, including Europe, are coming soon." No plan backs it.
- Homepage copy calls FÆ "He".
