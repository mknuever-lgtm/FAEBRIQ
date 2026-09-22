# FAEBRIQ image inventory, 2026/09/22

Source: live Shopify Admin GraphQL, every product and every media node, run read-only on 2026/09/22.

## Findings (Fact, live Shopify, 2026/09/22)
13 products: 12 ACTIVE, 1 ARCHIVED. 52 images in total.

Three image systems, confirmed:

| System | Spec | Filenames | Products |
|---|---|---|---|
| A: Printify mockups | 2048x2048 square JPG | numeric `*_2048.jpg` | 404 Tee, Code It Tee, 404 Tote, Circuit Cap Low Profile (4 each) |
| A': Printify, low-res | 1200x1200 square JPG | numeric `*_1200.jpg` | 404 Sticker (4) |
| B: AI studio set | 1664x2080 (4:5) PNG | random 16-char `*.png` | Crewneck, Hoodie (4 each), archived Slim Cap (4 of its 8; the other 4 are system A) |
| C: Sticker set | 1664x2080 (4:5) PNG | `sticker_<name>_01/02/03.png` | Not A Bug, Code It, Please Hold, Deploying Identity stickers (3 each) |
| Mixed | B + C, 1664x2080 and 2048x2560 | both patterns | Sticker Sheet (2 from B, 2 from C) |

Problems:
1. Aspect ratios clash on the grid: 5 active products are square (A), 7 are 4:5 (B and C). This causes the collection inconsistency.
2. 404 Sticker is the odd one out. It is the only sticker in system A, it is 1200px, and it has 4 shots where the other stickers have 3. This matches the "needs square-authored artwork" note.
3. Sticker Sheet mixes two systems and two resolutions within one gallery.
4. Stickers use 3 images and everything else uses 4.
5. Archived Slim Cap alt text says "embroidery" twice. Archived, so it does not show on the storefront, but it breaks the never-claim-embroidery rule. Fix it or delete it before anyone unarchives it.
6. Alt text on all products except the 4 single stickers uses em dashes. That breaks the no-dash rule for store copy.
7. Wording drift in alt text: "Pride Circuit" vs "pride-circuit", "six-stripe" vs "six-colour".

Unknown: which wordmark lockup the A-system mockups use. Printify renders it, so it has to be checked visually against `assets/print-art/`.

Repo sources available (local): `assets/print-art/` (4500px lights, JPG W/B variants, `sticker-final-system-2026-08-27/` at 2400px), `proofs/` (equal-visual-caps proofs), `assets/model-*-new.png`.
