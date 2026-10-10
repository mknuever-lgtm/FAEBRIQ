# FÆBRIQ front-print placement spec (2026-10-10)

Why: Maurice, 2026-10-10: every apparel front print sits too high, right under
the collar. Placement lives in Printify (x, y, scale per product), not in the
print files, so the files stay as they are (bar lock of 2026-10-01 respected).

## Spec (measured on the design itself: phrase + bar, bar = full design width)

| Garment | Printed width | Top edge below collar seam | Horizontal |
|---|---|---|---|
| Tee (all 6) | 10 in | 3 in | centred |
| Crewneck | 10 in | 3 in | centred |
| Hoodie | 10 in | 3.5 in (clear of the drawstring knot zone) | centred |

One placement serves every size (Printify applies it to all variants), so it is
set for size L. Small sizes read slightly larger and lower, 4XL/5XL slightly
smaller and higher: normal for one-file POD.

Resulting heights at 10 in wide: Code It 3.88 in, 404 v3 2.75 in, Deploying
2.53 in, Not A Bug 2.50 in, Off The Clock 2.30 in, Please Hold: measure.

## Sources (accessed 2026-10-10)
- Printify: top edge about 3 in below the collar ("three fingers"), centred:
  https://printify.com/blog/t-shirt-design-placement-guide/ ,
  https://printify.com/knowledge-hub/print-placement-tips-for-profit/
- Printful: 3 to 4 in below the collar, adjust by size:
  https://www.printful.com/ca/blog/t-shirt-design-placement-guide
- Kittl: standard adult front, top 3 to 3.5 in below collar:
  https://www.kittl.com/blogs/placement-t-shirt-design-size-chart-pod/
- 4OVER4 / Vistaprint: full-front width 10 to 12 in; slogan / minimal
  centre-chest 6 to 10 in:
  https://v2.4over4.com/guide/t-shirt-print-size-guide-how-big-should-your-design-be ,
  https://www.vistaprint.com/hub/t-shirt-design-placement-guide
- Hoodie 3.5 in: no source gives a hood-seam figure (Inference).

10 in sits where the slogan range (6 to 10) meets the full-front range (10 to
12): these lockups are wide and short, so smaller makes the line-2 text tiny.

## How to apply
1. Pull per product: blueprint, provider, front placeholder width/height px,
   and the provider's print-area top offset below the collar (Unknown until
   pulled; check the provider's print-area guide).
2. `python3 tools/printify_placement.py products.json` gives x, y, scale.
3. Set those in Printify, SAVE, do NOT publish (publish resets Shopify).
4. Verify on the re-rendered size-L front mockup with the check ratios the tool
   prints (tee: design width ~45% of body width, collar gap ~14%).
5. Re-shoot Shopify front, on-model and close-up images afterwards.

## Status 2026-10-10: do NOT apply yet
Measured on the Printify front mockups (Shopify front images, made from the
Printify mockups with geometry kept): collar-to-design-top gap is 0.45 to 0.54x
the design width on the tees and crewneck, 0.36x on the hoodie. The spec ratio
is 0.30 (tee) and 0.35 (hoodie). So Printify already prints at or BELOW the
spec; the "too high" look comes from the generated on-model and close-up
photos. Ground truth before any change: tape-measure collar seam to print top
on a physical tee. Muse's current values (provider 29, blueprint 6 tees /
49 crewneck / 77 hoodie): tee y 0.13 to 0.17, scale 0.66 to 0.80.
