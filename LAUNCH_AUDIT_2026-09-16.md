# FÆBRIQ — Pre-Launch Deep Dive

**Date:** 2026/09/16
**Audit target:** `faebriqtheme-launch-fix` (theme ID `145284005955`, role UNPUBLISHED)
**Currency:** USD throughout (store currency)
**Verdict:** Ship it. The theme is in better shape than anyone gave it credit for. Three things block the social push, and only one of them is a build task.

---

## 0. Access — read this before trusting any section below

**I could not load a single rendered page.** Not faebriq.com, not the preview link, not the myshopify domain.

This session's network egress policy denies both hosts at the CONNECT layer:

```
ufyytt-er.myshopify.com:443 — CONNECT tunnel failed, 403 (policy denial)
faebriq.com:443            — CONNECT tunnel failed, 403 (policy denial)
```

Tested three ways: `curl`, the WebFetch tool, and a second attempt after the preview-link instruction. All denied. **A theme preview link cannot fix this** — the preview lives on the same blocked domain, so asking you for one would have wasted your time. That's why I didn't ask.

**What I did instead:** read the launch-fix theme's actual source, file by file, through the Shopify Admin API. For a code-level audit this is *better* than a preview — I'm reading the real Liquid, not inferring from rendered HTML. I read all 27 files' names and sizes, and the full contents of `layout/theme.liquid`, `snippets/meta-tags.liquid`, `templates/product.liquid`, `templates/index.json`, `sections/featured-collection.liquid`, `sections/footer.liquid`, `snippets/product-card.liquid`, `snippets/sticker-addon.liquid`, `assets/faebriq.css`, and `assets/faebriq-fixes.css`. I also pulled the live catalogue, variants, prices, image dimensions, delivery profiles, markets, orders, discounts, pages and menus.

**Checks I could NOT perform, and am not guessing at:**

| Check | Status |
|---|---|
| Real Core Web Vitals / Lighthouse | **Not done** — needs a live render |
| Visual layout, spacing, visual hierarchy | **Not done** — code-level only |
| Actual mobile rendering on a device | **Not done** — I read the media queries, that's all |
| Rendered color contrast | **Computed from hex values**, not sampled from pixels |
| Live checkout flow / Shop Pay behavior | **Not done** |
| Whether JSON-LD passes Google's Rich Results Test | **Not done** — I validated the template logic, not a live URL |
| Anything inside Printify's admin | **No access.** Flagged everywhere it matters |

Everything stated as fact below came from source code or the Shopify Admin API on 2026/09/16. Where I'm reasoning rather than observing, I say so.

---

## 1. Three corrections to the brief

Your prompt got three details wrong. Two are harmless, one changes a priority.

**1.1 — The empty delivery profiles are not "two Monster Digital mug profiles."**
There are **14 delivery profiles**. Twelve have **zero variants assigned**. Of those twelve, roughly eight carry Australia / EU / Rest-of-World zones — not just the two mug profiles, but also Monster Digital hoodie/sweatshirt, Monster Digital t-shirt (×2), Fulfill Engine bags (×2), Printify Choice Hats, Duplium Hats, and Printed Simply.

**Your conclusion still holds: zero customer impact.** Belt and braces, actually —

- No product is attached to any of them (0 variants each), and
- **Markets are restricted to United States and Canada only.** Both enabled, US primary. Nothing else exists as a sellable region.

So a customer in Berlin cannot reach those zones through any path. The only two profiles carrying products are:

| Profile | Variants | Zone | Rate |
|---|---|---|---|
| General profile (default) | 61 | United States & Canada | FREE SHIPPING |
| Standard: SPOKE Custom Products, Paper products | 7 | United States & Canada | FREE SHIPPING |

The SPOKE profile holds 7 variants of the Error 404 sticker. Same zone, same free rate, so no customer-visible inconsistency. **US/Canada-only is correctly enforced at every layer.** Confirmed, not a limitation to fix. Cleanup is cosmetic Printify hygiene, nothing more.

**1.2 — No product has "15-20+ near-duplicate images."**
Verified image counts across the whole catalogue: **3 to 4 images per active product.** The only outlier is the *archived* Circuit Cap at 8. Whatever gallery bloat existed has already been cleaned up. The sticker photography critique stands on quality, not on volume — don't spend time culling images that aren't there.

**1.3 — Do not say "embroidery."**
Your prompt describes fulfillment as "DTF/embroidery." Per `CLAUDE.md`, embroidery is **UNVERIFIED** and must never be claimed anywhere. Current state:

- ✅ The **active** cap (`Circuit Cap, Low Profile`) description makes no print-method claim. Clean.
- ⚠️ The **archived** cap's image alt text says *"front embroidery"* and *"macro detail of white wordmark embroidery."* It's archived so it's not public — but if that product is ever un-archived it ships a false claim. Fix the alt text or leave it archived.

---

## 2. Competitive landscape

I could not open any competitor's site (same egress block), so this is built from search-result evidence and published brand material, not first-hand PDP teardowns. Everything below is a real, currently-operating brand. Where I don't have a detail, I've left it out rather than invented it.

### The dev-humor lane — your closest commercial comparables

**Techmerch.io** — developer t-shirts, sweatshirts, hoodies. Tech in-jokes for people who get them immediately, explicitly positioned against "generic *I code* shirts and overpriced merch."
- **Price:** $25–$42
- **Shipping:** free from **3 shirts**
- **Social proof:** Trustpilot presence; reports of good print quality and better-than-promo fabric
- **Trust:** 30-day hassle-free returns; fulfils EU/US/UK with stated delivery estimates; customers report fit matching the size guide
- **Borrow:** the free-shipping-at-3 threshold, and publishing delivery estimates up front
- **Avoid:** nothing much — this is the benchmark

**Code Culture (codeculture.store)** — "indie apparel brand turning dev jokes into premium streetwear." Terminal jokes, language logos, stack-trace humor.
- **Price:** premium positioning, unstated band; **240gsm** fabric called out explicitly
- **Sizing:** unisex **S–3XL on every design**, with a written fit description ("true to size, runs slightly relaxed through the body")
- **Shipping:** free on **3+ shirts**; worldwide from US and EU facilities, 5–10 days domestic / 10–15 international
- **Returns:** POD-honest — no returns for sizing or buyer's remorse, but free reprints on defects within 30 days with photo + order number, plus an EU 14-day cooling-off
- **Content:** runs a blog for SEO (e.g. a "Top 8 Code.Clothing Alternatives" comparison post) that ranks against competitor brand searches
- **Borrow:** ⭐ **the written fit description and the gsm spec.** This is the single cheapest thing on this page and you already half-do it. Also the honest POD returns policy — it pre-empts the top objection instead of hiding it
- **Avoid:** their Trustpilot shows unanswered support email and slow shipments. You're a one-person shop; unanswered email is your biggest reputational risk too

### The queer-apparel lane — your brand and audience comparables

**Awarewolf Apparel (awarewolfapparel.com)** — founded 2015 by Landon Reed, trans-owned, "queer streetwear with punk attitude." Shirts like "Queer is punk," "Bury all the gender roles."
- **Range:** the widest accessory ladder of anyone here — hats, keychains, flags, blankets, stickers, patches, pins, plus swim shorts, packing briefs, tees, jackets
- **Social:** **45,000+ Instagram, 25,000+ TikTok.** This is the audience you're competing with for attention
- **Borrow:** ⭐ **the accessory ladder.** Low-price impulse SKUs (pins, patches, keychains) do the customer-acquisition work while apparel does the margin. You have stickers at $4 — that's the same idea, under-extended
- **Avoid:** their loudness is the opposite of your positioning. Don't chase it

**Ash + Chess (ashandchess.com)** — queer/trans couple Ashley Molesso and Chessie Needham, Kingston NY. Greeting cards, art prints, screen-printed tees, accessories. Messages like "trans people belong here!"
- **Proof strategy:** brand collaborations as social proof — Target, Skittles, Nooworks, Belletrist — plus published authors (*Queer Tarot: An Inclusive Deck & Guidebook*)
- **Borrow:** ⭐ **founder-as-proof.** They sell the people, not just the product. You have a genuinely good story (queer developer in Toronto, builds by day, serves identity by night) and it's currently buried at the bottom of the About page
- **Avoid:** their bright illustrated style is the aesthetic opposite of yours. Don't soften your dark-tech look toward it

**Stuzo Clothing** — founded 2010 by Stoney Michelli and Uzo Ejikeme. Gender-free clothing with explicit emphasis on the BIPOC queer community. Celebrity co-signs (Ruby Rose, Tiffany Haddish, Jada Pinkett Smith, Spike Lee).
- **Borrow:** a sharply-named point of view beyond "queer" generally. Yours is "queer *and* technical" — lean harder on the second half
- **Avoid:** celebrity seeding isn't reachable at your stage

**The Phluid Project (thephluidproject.com)** — founded 2018, queer-owned, gender-free apparel and accessories, built on "community, activism, and education."
- **Borrow:** the education/community content pillar. Your voice can carry this without being worthy about it
- **Avoid:** breadth. They carry far more SKUs than a solo operator should

**Otherwild** — founded 2012, queer-owned, ethics-forward (fair wages and labor practices stated up front), curated goods from many makers alongside apparel. Entry price around $15.
- **Borrow:** ⭐ **stating your ethics as spec, not sentiment.** Your About page already does this well with "A named share of Pride Circuit proceeds goes to an LGBTQ+ org. Year-round. Not Q2." That line is excellent and it is currently invisible to anyone who doesn't click About
- **Avoid:** multi-maker curation — not your model

**Kirrin Finch** — Laura Moffat and Kelly Sanders Moffat. Size-inclusive, menswear-inspired tailoring for female and nonbinary bodies. Founded on a fit problem the founders personally had.
- **Borrow:** ⭐ **fit as the entire brand promise.** They exist because sizing was broken. You sell S–5XL with *no measurements published at all*. That's the gap, and this brand is the proof it matters

**dfrntpigeon** — Portland; designs created by marginalised youth through New Avenues for Youth, mentored by professional designers. Tees, buttons, stickers.
- **Borrow:** a concrete, named beneficiary. "A named share" in your About copy is a promise with a blank in it. Fill in the name

### 2.1 — Positioning verdict

**Is the "queer tech-nomad" niche distinct enough? Yes — genuinely.**

This isn't flattery. When I searched for brands combining queer identity *and* programmer humor, the result was explicit: strong brands exist in each lane separately, and **no single store combines queer + tech + developer humor**. The queer lane (Awarewolf, Ash + Chess, Stuzo, Otherwild, Phluid, Kirrin Finch) sells identity. The dev lane (Techmerch, Code Culture) sells in-group humor to a mostly-straight-coded audience. The intersection is open.

That's a defensible wedge, and it's narrow enough that you can own the search terms cheaply.

**Is the pride-circuit bar ownable? Yes. Keep it exactly as it is.**

Six hard-edged blocks, no gradient, no noise. Every other brand in this space defaults to a smooth rainbow gradient. Hard-edged segments read as a *circuit* or a *progress bar* — which is the whole joke, and it's legible at 16px where a wordmark isn't. It's already carried consistently across the header, footer, cards, PDP, favicon and print art. This is the strongest single asset the brand has. **Do not let anyone redesign it.**

**Does the humor land? Yes, but it's carrying more weight than it should.**

Your copy is drier and more understated than both comparables. Awarewolf shouts ("Queer is punk"). Code Culture goes broad (stack-trace gags). You do deadpan: *"Not a defect. A feature nobody requested."* / *"Straight not found. The lookup failed and nobody is filing a bug report."*

That restraint is a real differentiator — it reads as confident rather than needy. **But deadpan raises the bar on visual execution**, because the joke doesn't do the selling by itself. A loud brand survives mediocre photography; a dry one doesn't. This is exactly why the sticker imagery problem is a bigger deal for *you* than it would be for Awarewolf.

**Pricing verdict: correct. Don't touch it.**

| | FÆBRIQ | Category |
|---|---|---|
| Tee | $34 (2XL $36, 3XL+ $37) | Techmerch $25–$42 |
| Crewneck | $62 | — |
| Hoodie | $68 | — |
| Sticker | $4–$6 | — |
| Sticker sheet | $11.99–$13.99 | — |

2026 POD economics: DTG blanks run $8–$12; Printify all-in per shirt is $11.39–$18.49 on the free plan, $9.91–$15.89 on Premium ($39/mo, raised from $29 on 2026/02/17). Benchmark margin is 40%, with premium niche brands reaching 50%+.

At $34 with free shipping baked in, you're sitting around **47–59% gross margin** depending on plan and blank. That's premium-niche territory and it's where you want to be. **Cutting price would undermine the positioning without meaningfully moving volume.** The $4 sticker as a trial-price entry point is exactly right.

**The one pricing structure you're missing:** both Techmerch and Code Culture gate free shipping at **3+ shirts**. You give free shipping at quantity 1. That's more generous — and it means **you have no reason for anyone to add a second item.** You've spent your only AOV lever before the customer arrives. See §5.

---

## 3. Storefront audit — `faebriqtheme-launch-fix`

### 3.1 What's genuinely done and good

Credit where it's due. This theme is in far better shape than the brief implied, and several things were fixed that nobody listed:

| Area | State |
|---|---|
| **Typography** | ✅ **Instrument Serif.** (The live published theme still loads **Playfair Display** — off-brand. Another reason to publish.) |
| **Social previews** | ✅ `snippets/meta-tags.liquid`: canonical, `og:site_name/type/title/description/url/image` + dimensions + alt, `twitter:card` = `summary_large_image` with graceful fallback to `summary` |
| **Structured data** | ✅ Product JSON-LD with **one `Offer` per variant** (sku, price, currency, availability, url) + Organization JSON-LD on the homepage |
| **Homepage** | ✅ The `collections[section.settings.collection]` bug is fixed — a `collection`-type setting resolves to an object, not a handle, so the old code always rendered the "select a collection" placeholder. Now `section.settings.collection` is used directly |
| **Homepage hero** | ✅ Full settings populated (eyebrow, heading, tagline, subheading, CTA label **and URL**, price note). The live theme's hero settings are empty, so its CTA button doesn't even render |
| **PDP gallery** | ✅ Multi-image gallery with thumbnails, keyboard focus rings, `srcset` + `sizes` + `fetchpriority="high"` on the LCP image |
| **Image cropping** | ✅ `object-fit: contain` — explicitly chosen because the catalogue mixes 1:1 and 4:5 and `cover` cropped both |
| **Accessibility** | ✅ Skip-to-content link, `role="group"` + `aria-labelledby` on variant groups, `aria-pressed` state, `:focus-visible` outlines |
| **Contrast** | ✅ `--fae-text-faint` lifted `#5f5f5f` → `#8a8a8a`. On `#0a0a0a` that's ~5.6:1, clears WCAG AA. Body dim text ~7.0:1, silver on ink ~10.3:1, link blue ~7.2:1. All pass |
| **Mobile PDP** | ✅ The desktop `height: 60vw` letterbox is overridden to `height: auto` under 768px — the old rule sliced the top and bottom off every portrait garment shot |
| **Variant JS** | ✅ Two real bugs fixed: `Shopify.formatMoney` is now guarded (it isn't loaded by this theme, so unguarded it threw and froze the displayed price while the cart charged the new one), and an option combination with no matching variant now blocks instead of silently adding a *different* variant |
| **Printify taxonomy** | ✅ `Paper products` → Stickers, `Bags` → Tote, `Hats` → Cap, `Sweatshirt` → Crewneck. Applied on both the PDP eyebrow and the homepage filter rail |
| **PDP trust** | ✅ "Free shipping to the US & Canada · Printed to order" under the price, plus a Delivery & returns block linking the refund policy |
| **Cross-sell** | ✅ Sticker add-on adds the cheapest *available* variant via AJAX and opens the drawer — no navigation away. Has a busy-guard and an error state |
| **Content pages** | ✅ `templates/page.liquid` + `templates/page.contact.liquid` exist. **The live theme has neither**, and both pages point at templates it lacks — so `/pages/about` and `/pages/contact` are broken on the published site right now |
| **Footer** | ✅ Email capture, Shop/About/Contact, five legal links, support email |
| **Favicon** | ✅ `favicon.svg` — pride-circuit bar, reads at 16px |

**Performance signals from source** (not measured — no live render): the theme is 27 files with no framework, no jQuery, no app embeds. Images are responsive with proper `sizes`. There's a `preconnect` to `cdn.shopify.com`. These are genuinely fast bones. One real problem, see 3.2.8.

### 3.2 What's still missing or wrong

**3.2.1 — No size guide. This is the #1 conversion gap.** 🔴
You sell S–5XL. There is not one measurement anywhere in the theme or in any product description. Meanwhile: fit and sizing cause **50% of apparel returns**, and McKinsey puts **70% of fashion returns** down to sizing. Category return rates run 20–40%.

Worse for you specifically: this is **print-on-demand**, so a sizing return is a total loss — you can't restock it. Code Culture publishes a written fit description *and* gsm. You publish gsm (180 g/m² on the tee — good) but no measurements.
→ **Needs from Maurice:** the measurement table per garment, from Printify's product pages. **Then:** pure dev task to render it.

**3.2.2 — Three sticker SKUs have defective printed artwork.** 🔴
Known, root-caused, blocked on sourcing original files. I'm not re-diagnosing — but I am escalating the **priority**.

Shipping a visibly defective pride bar to a first-wave customer, in a brand whose entire visual identity *is* that bar, is worse than not selling it. Your first 50 customers are the ones who post. A gapped/dotted stripe is exactly the thing that gets screenshotted.
→ **Decision for Maurice, today:** either fix the artwork before the social push, or set those three SKUs to **draft** until it's fixed. Do not push traffic at a product you know prints wrong. Two SKUs plus the sheet is still a viable sticker offer.

**3.2.3 — Sticker photography.** 🟠
Confirmed as flagged: `sticker_*_01_flat` / `_02_laptop_context` / `_03_detail`, three per SKU, 4:5. Not the 15-20 image problem you thought. The real issue is that a flat composition doesn't communicate **die-cut edge, physical scale, or the transparent-vs-white surface choice** — and you sell both surfaces as variants. A customer choosing "Transparent" vs "White" currently has no way to see the difference.
→ **Needs from Maurice:** real Printify mockups, or one real photo of a sticker on a laptop lid with something for scale. **Note:** this is *more* urgent for you than for a louder brand, because deadpan copy doesn't compensate for weak imagery.

**3.2.4 — The 1200×630 social card exists and isn't wired up.** 🟠
`brand/social/faebriq-og-card.png` — verified **1200×630**, white ground, Instrument Serif wordmark, pride-circuit bar. Built 2026/08/30. `meta-tags.liquid` doesn't reference it; it falls back to the first product image.

Two consequences:
- Sharing the **homepage** previews as a photo of the Error 404 tee, not as the brand.
- `twitter:card` is `summary_large_image`, which crops to **1.91:1**. Your product images are 1:1 and 4:5. Every shared product link gets center-cropped, and on the 4:5 shots that cuts the garment.

Also a small precision bug: `og:image:height` is hardcoded to `1200` while width is `1200`. For the seven 4:5 products, `image_url: width: 1200` actually returns **1200×1500**. The declared height is wrong for more than half the catalogue. Most scrapers re-measure, so impact is low — but it's wrong.
→ **Dev task.** Upload the card as a theme asset, use it for non-product pages, and fix the height declaration. ~20 minutes.

**3.2.5 — DEPLOY15 is live and invisible.** 🟠
There is an **active discount code** on the store: `DEPLOY15`, 15% off, "FÆBRIQ Vol. 1 Launch," active since 2026/06/15. It appears **nowhere** on the site. No announcement bar, no popup, no footer note, no PDP mention.

You're about to drive first-ever social traffic at a store carrying an unadvertised launch discount.
→ **Decision for Maurice:** either retire it or surface it. If you surface it, attach it to the email signup (see next).

**3.2.6 — The email signup offers nothing.** 🟠
Footer capture exists and works — `{% form 'customer' %}`, tagged `newsletter`, accessible hidden label, success state. Good build. The offer is *"Get told when the next drop lands."*

Benchmark: popups **with** a discount convert at **2.4%** vs **1.7%** without — a 41% relative lift. Average Shopify popup converts 4.2%; standard discount popups 3–5%. Mobile-designed popups convert 2.2% vs 1.4% desktop-only, and your traffic is about to be overwhelmingly mobile.

You already have the discount sitting unused. Wire DEPLOY15 to the signup and you've built a first-purchase incentive out of parts you already own.
→ **Decision for Maurice** (do you want to give 15%?), **then dev task.**

**3.2.7 — No social links in the footer.** 🟠
You are about to start posting to social for the first time, and there is no path from the site to your accounts. Also no path back — nothing tells a visitor the brand is active anywhere.
→ **Needs from Maurice:** the handles. **Then:** trivial dev task. Do this before the first post, not after.

**3.2.8 — Google Fonts loaded via CSS `@import`.** 🟠
`assets/faebriq.css` line 5:

```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Archivo:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
```

An `@import` inside a stylesheet is **serialised** — the browser must download and parse `faebriq.css` before it even discovers the font request. That's a guaranteed extra round-trip on the critical path, and `theme.liquid` preconnects to `cdn.shopify.com` but **not** to `fonts.googleapis.com` or `fonts.gstatic.com`.

You're also pulling three families and about eleven weight files. Archivo alone requests five weights (300/400/500/600/700); the theme visibly uses far fewer.
→ **Pure dev task.** Move to `<link>` tags in `theme.liquid` with preconnects, and trim Archivo to the weights actually used. This is the highest-leverage performance fix available and it's low-risk.

**3.2.9 — No on-site search.** 🟡
No `templates/search.liquid` in either theme. At 12 products this genuinely does not matter — the homepage catalog has a working client-side type filter (All / Tees / Crewneck / Hoodie / Tote / Cap / Stickers) with sort. **Do not build search before launch.** Revisit past ~30 SKUs.

*Improvement worth noting:* the live theme's footer menu links to `/search`, which would 404. The fix theme's footer doesn't. One more broken link resolved by publishing.

**3.2.10 — `settings_schema.json` is `[]`, but "zero customizer controls" overstates it.** 🟡
Correct: there are no *global* theme settings, so colors/fonts need code edits. But every section carries its own `{% schema %}` — the hero (eyebrow, heading, tagline, subheading, CTA label, CTA URL, price note), the catalog section (title, subtitle, collection, product count, view-all toggle), the header (menu picker), brand-statement. **You can edit all homepage copy in the theme editor without touching code.** That's the 80% case covered.
→ Not a launch blocker. Build global settings when you want to change a color, not before.

**3.2.11 — The grid will look ragged.** 🟡
The `object-fit: contain` fix prevents cropping — correct call — but the cards are `aspect-ratio: 1/1`. So square product shots fill their tile while 4:5 shots letterbox with side gutters. On a 12-product grid, seven are 4:5 and five are 1:1. It'll read as inconsistent.

The real fix isn't CSS, it's source images.
→ **Decision + asset work for Maurice:** re-export mockups at one ratio. **Recommendation: 1:1**, because it matches the majority of your newer Printify-generated shots (2048×2048), matches the Shop app's grid, and avoids the crop entirely. Post-launch.

**3.2.12 — Only two collections exist.** 🟡
`All Products` (12) and `Stickers — Add-Ons` (5). No category landing pages. That's fine for navigation at this size, but it means no URL to rank for "queer developer t-shirt" or "programmer pride hoodie." Given your niche is uncontested (§2.1), that's cheap traffic you're leaving on the table.
→ Post-launch SEO work.

**3.2.13 — Smaller items**

- **Eager-loading on mobile.** `{% if card_id <= 3 %}loading="eager" fetchpriority="high"{% endif %}` — correct on a 3-column desktop grid, but the grid drops to 1 column under 480px, so phones eagerly fetch three images when one is above the fold. Minor over-fetch on exactly the devices that matter most.
- **No quantity selector** on the PDP. Compounds the AOV problem in §5.
- **No cross-sell from sticker PDPs.** `fae_addon_types` is `T-Shirt,Sweatshirt,Hoodie,Bags,Hats` — so a customer on a $4 sticker page sees no route to a $34 tee. That's backwards from a margin standpoint.
- **Accent colour is generic blue** (`#4a9eff`) for links and focus rings, on a brand whose entire palette is six pride colours. Contrast passes (~7.2:1), so this is taste, not a defect. A Maurice call.
- **No `priceValidUntil`** in the Product JSON-LD. Optional; Google may emit a warning.
- **Vendor field is inconsistent** across the catalogue — some products are `Printify`, others `FÆBRIQ`. The theme doesn't render vendor on the PDP, so it's invisible on-site, but it does flow into Shopify's own product feeds and the Shop app. Admin hygiene.
- **No reviews or social proof of any kind.** See §5.

---

## 4. Catalogue and merchandising

**Verified 2026/09/16: 12 active products, 1 archived.**

| Product | Price | Variants | Images | Ratio |
|---|---|---|---|---|
| Error 404: Straight Not Found Tee | $34–$37 | 8 | 4 | 1:1 (2048) |
| Code It. Serve It. Tee | $34–$37 | 8 | 4 | 1:1 (2048) |
| Deploying Identity v2.0 Crewneck | $62 | 6 | 4 | 4:5 (1664×2080) |
| Off The Clock. Still Iconic. Hoodie | $68 | 8 | 4 | 4:5 |
| Error 404 Cotton Tote | $34 | 1 | 4 | 1:1 (2048) |
| Circuit Cap, Low Profile | $34 | 1 | 4 | 1:1 (2048) |
| It's Not A Bug. It's Me. Sticker | $4–$6 | 6 | 3 | 4:5 |
| Code It. Serve It. Sticker | $4–$6 | 6 | 3 | 4:5 |
| Error 404 Sticker | $4–$6 | 8 | 4 | 1:1 (1200) |
| Please Hold Sticker | $4–$6 | 6 | 3 | 4:5 |
| Deploying Identity v2.0 Sticker | $4–$6 | 6 | 3 | 4:5 |
| Sticker Sheet — The Full Drop | $11.99–$13.99 | — | 4 | 4:5 |
| ~~Circuit Cap, Slim Unstructured~~ | ~~$34~~ | 1 | 8 | **ARCHIVED** |

**Image standards.** All images clear 1200px; most are 2048px. Nothing is below spec. The problem is **ratio consistency**, not resolution — see §3.2.11. One outlier: the Error 404 Sticker is 1200×1200 while everything else 1:1 is 2048×2048. Harmless but worth normalising when you redo the sticker shots anyway.

**Two cap products exist.** `Circuit Cap, Slim Unstructured` is ARCHIVED; `Circuit Cap, Low Profile` is ACTIVE at $34. Both $34, both black, near-identical naming. Not customer-visible, but keep the archived one archived or you'll confuse yourself — and it carries the embroidery alt-text problem from §1.3.

**Copy quality: strong. Leave it alone.** Product descriptions are specific and on-voice — *"100% cotton · 180 g/m²"*, *"Reinforced shoulders for a stable shape"*, *"Made to order, printed in the US · ships in 5–7 business days"*. That's the Code Culture spec-forward pattern, already done, without being told to. The About page is genuinely good writing.

**Two copy problems:**

1. **The best line on the site is buried.** *"A named share of Pride Circuit proceeds goes to an LGBTQ+ org. Year-round. Not Q2."* That is your sharpest differentiator against every seasonal-rainbow brand, and it's at the bottom of a page most visitors won't open. It belongs on the homepage and in the footer.
2. **"A named share" doesn't name anything.** Neither the share nor the org. Right now it's a promise with two blanks in it, and a sceptical reader will notice. → **Decision for Maurice:** pick the org, pick the percentage, state both. Or soften the claim.

**SEO titles are solid.** Every product has a hand-written `seo.title` and `seo.description` (e.g. *"Error 404: Straight Not Found Premium Tee | FÆBRIQ"* / *"Premium black tee — Error 404: Straight Not Found with a subtle pride-circuit bar. Made to order, printed in the US."*). Consistent pattern, brand suffix, keyword-bearing, correct length. No work needed.

**Tag taxonomy is sane** — `apparel`/`accessories` + design slug + `dark tech` + `pride circuit` + `queer tech` + `launch vol1` + product type. Consistent across all 13. Fine.

**No duplicates, no orphans, no stray drafts.** Everything active is intentional.

---

## 5. The commercial gap nobody has flagged

Separate from bugs. This is about money.

**You have one sale. Zero orders show in the Shopify Admin API** — I queried with `status:any` and got `count: 0`. If a sale happened, it isn't in this store's order records (test order, deleted, or a different channel). Worth reconciling before you use it as a baseline for anything.

**Three structural problems, all cheap to fix:**

**5.1 — There is no reason to buy two things.**
Free shipping is baked in at quantity 1. No quantity selector. No bundle. No threshold. Your competitors gate free shipping at 3+ shirts specifically *because* it manufactures a reason to add items. You've given away your only AOV lever before the visitor arrives.

The sticker cross-sell is the right instinct and it's well built — but it fires only on apparel pages, adds a $4 item to a $34–$68 order, and offers no incentive to take it.
→ **Cheapest fix that fits your model:** "Add any two stickers, get the third free," or "Free sticker over $50." You keep free shipping as the headline and get a bundle ladder underneath. **Decision for Maurice**, then a small dev task.

**5.2 — Zero social proof, and no mechanism to start collecting it.**
No reviews, no ratings, no UGC, no order count, no "as seen" — nothing. With one sale that's honest, and **fabricating any of it would be worse than having none.** But there's no mechanism in place either, so after 50 orders you'll still have nothing.

At this volume, skip review apps entirely — they cost money and render empty stars, which is worse than silence. Instead: turn on Shopify's built-in post-purchase email, ask for a photo, and repost to social. Your first thirty customers *are* your social proof pipeline.
→ Free. Set up before the first order lands, not after.

**5.3 — No abandoned-cart flow confirmed.**
Shopify Basic includes abandoned checkout emails but they are **off by default**. Benchmarks: a three-email sequence recovers **10–17%** of abandoned carts (5–8% / 3–5% / 2–4%). Cart-abandonment popups average 17.1% conversion.

At your volume this is a handful of orders — but it's free, it's a checkbox, and it compounds.
→ **Check Settings → Notifications → Abandoned checkout.** I can't verify its state through the API. Five minutes.

**5.4 — Social cadence, for the launch itself.**
Benchmarks for a small brand: Instagram feed **3–5/week**, Reels **2–5/week**, TikTok **2–5/week**. Fashion brands average **2.4%** engagement on TikTok with top performers above 8%. Awarewolf — your closest audience comparable — sits at 45k Instagram / 25k TikTok.

The consistent advice across sources: **a schedule you can sustain beats a heavy one you abandon.** Two to three strong posts a week plus replying to everything outperforms daily low-effort posting, and low-effort posts actively hurt reach on Instagram.

For a solo operator: **3/week on one platform** beats 5/week split across two. Given your deadpan copy is text-first and your product is visual-second, TikTok's higher engagement ceiling favours it — but Instagram better suits a static-image, typography-led brand. Pick one, commit for eight weeks.

---

## 6. Printify and fulfilment — what I could and couldn't check

**No Printify access. Nothing below is guessed.**

✅ **Verified through Shopify:** shipping is correctly restricted to US and Canada at *both* layers — market-level (only US and Canada exist and are enabled) and profile-level (both profiles carrying products are US & Canada, free rate). This is enforced at the product level, not just a shop default. **Your US/Canada-only policy is correctly reflected everywhere I can see.**

✅ **Verified customer-facing consistency:**
- About page: *"Ships to the United States and Canada — 2–7 business days to produce, then 4–8 days in transit to the US, 7–14 days to Canada"*
- Contact page: *"We ship to the United States and Canada"* + the same production/transit windows + a 24-hour change/cancel window
- PDP (fix theme): *"Free shipping to the US & Canada · Printed to order"* under the price, plus a Delivery & returns block
- Homepage hero: *"$4–$68 USD · Free shipping to the US & Canada · Printed to order"*

That's consistent across four surfaces. Good.

⚠️ **One inconsistency to resolve:** the About and Contact pages say production is **2–7 business days**. Every product description says **5–7 business days**. The PDP Delivery block says **5–7**. Pick one number.
→ **Decision for Maurice.** Trivial to apply once decided.

❌ **Could not verify** (needs Printify login):
- Whether print-provider-level shipping settings match US/Canada-only *inside Printify* — if a provider there is configured for worldwide, that surfaces the day you enable another market
- Provider turnaround and quality ratings for SPOKE (stickers), Fulfill Engine (tote), and the Printify Choice provider behind the cap
- Whether the cap is DTF or embroidery — **still UNVERIFIED, still must not be claimed**
- Whether the 14 auto-generated profiles regenerate on the next Printify sync

⚠️ **Standing hazard, from `CLAUDE.md`:** Printify→Shopify publishes and syncs **overwrite Shopify edits**. Every hand-written SEO title, description and alt text in §4 is at risk from a single careless sync. Whatever else happens, don't run one.

---

## 7. Pre-launch punch list

Ordered by (impact on a first-time buyer) × (effort), not by severity.

### 🔴 Launch blockers — do these before any social traffic

| # | Item | Type | Effort |
|---|---|---|---|
| 1 | **Publish `faebriqtheme-launch-fix`.** Everything in §3.1 is sitting unpublished. The live site currently has a blank homepage catalog, a hero with no CTA button, broken `/pages/about` and `/pages/contact`, a broken `/search` link, no OG tags, no JSON-LD, no srcset, one image per PDP, Playfair Display instead of Instrument Serif, and a variant bug that displays $34 while charging $36. **One action fixes all of it.** | **Maurice's call** — `CLAUDE.md` forbids me publishing themes without explicit instruction | 2 min |
| 2 | **Decide on the three defective sticker SKUs:** fix the artwork, or set them to draft. Do not drive traffic at a product you know prints wrong — especially not one whose defect is in the brand device itself. | **Maurice decides** | 5 min to draft |
| 3 | **Add a size guide.** S–5XL with no measurements, in a category where sizing drives 50–70% of returns, on a POD model where returns are a total loss. | **Maurice supplies** measurements from Printify → **dev task** | 1–2 hrs total |
| 4 | **Add social links to the footer.** You cannot start posting to social with no route between the site and the accounts. | **Maurice supplies** handles → trivial dev | 15 min |
| 5 | **Resolve DEPLOY15.** An unadvertised 15%-off code is live. Surface it or retire it before traffic arrives. | **Maurice decides** | 10 min |
| 6 | **Turn on abandoned-checkout emails.** Free, off by default, recovers 10–17%. | **Maurice** (Settings → Notifications) | 5 min |

### 🟠 Should fix soon — hurts conversion or credibility, won't sink launch

| # | Item | Type | Effort |
|---|---|---|---|
| 7 | **Wire DEPLOY15 to the email signup.** Discount popups convert 2.4% vs 1.7% without. You own both halves already. | Maurice decides the offer → dev | 30 min |
| 8 | **Use the 1200×630 OG card** for non-product pages; fix the hardcoded `og:image:height`. Asset already exists at `brand/social/faebriq-og-card.png`. | **Pure dev task** | 20 min |
| 9 | **Fix font loading.** Move Google Fonts out of CSS `@import` into `<link>` + preconnect; trim Archivo's five weights. Highest-leverage perf win available. | **Pure dev task** | 30 min |
| 10 | **Reshoot sticker photography** — die-cut edge, scale reference, transparent vs white side by side. Matters more for a deadpan brand than a loud one. | **Maurice supplies** mockups/photos | Varies |
| 11 | **Add a bundle ladder.** "Two stickers, third free" or "free sticker over $50." You currently have no reason for anyone to buy two things. | Maurice decides → dev | 1 hr |
| 12 | **Move the "not Q2" allyship line to the homepage**, and **name the org and the percentage.** Your sharpest differentiator, currently buried and unfilled. | **Maurice decides** (which org, what %) → trivial dev | 20 min |
| 13 | **Reconcile production time:** 2–7 days (About/Contact) vs 5–7 days (all PDPs). | Maurice picks → trivial dev | 10 min |
| 14 | **Set up a post-purchase photo request** and repost customer shots. Your only viable social-proof engine at this volume. | Maurice | 30 min |

### 🟡 Later — polish and roadmap

| # | Item | Type |
|---|---|---|
| 15 | **Normalise all product images to 1:1.** Fixes the ragged grid at the source instead of in CSS. | Maurice supplies re-exports |
| 16 | **Add category collections** (Tees / Sweats / Accessories / Stickers) as SEO landing pages. Your niche is uncontested — cheap traffic. | Dev |
| 17 | **Cross-sell apparel from sticker PDPs.** Currently only apparel→sticker, which is backwards for margin. | Dev |
| 18 | **Clean up the 12 empty Printify delivery profiles.** Zero customer impact; purely tidiness. | Maurice, in Printify |
| 19 | **Normalise the `vendor` field** (`Printify` vs `FÆBRIQ`). Invisible on-site, visible in feeds and the Shop app. | Dev or Maurice |
| 20 | **Fix the archived cap's embroidery alt text**, or leave it archived forever. | Dev |
| 21 | **Build `settings_schema.json`** so colors/fonts are editable without code. Section-level settings already cover homepage copy. | Dev |
| 22 | **Quantity selector** on the PDP. | Dev |
| 23 | **Reconsider the `#4a9eff` link blue** against the six-colour pride palette. Taste, not a defect. | Maurice decides |
| 24 | **On-site search** — revisit past ~30 SKUs. Not before. | Dev |
| 25 | **Extend the accessory ladder** (pins, patches, keychains) — Awarewolf's acquisition model, and your $4 sticker is the same idea under-extended. | Maurice decides |

---

## 8. Bottom line

**The build is ready. The publish hasn't happened.**

The single highest-value action on this entire page takes two minutes and is not a code change: **publish `faebriqtheme-launch-fix`**. Everything the previous session built — social previews, structured data, the gallery, the accessibility work, the homepage fix, the correct typeface, two genuine cart bugs — is finished and sitting in an unpublished theme while the broken version serves customers.

After that, three things gate the social push: the **size guide**, a **decision on the three defective stickers**, and **social links in the footer**. Two of the three need you, not a developer.

Everything else on this list is optimisation. The brand positioning is sound and the niche is genuinely open. The copy is better than most brands at ten times the revenue. The pride-circuit bar is a real asset — don't let anyone touch it.

Don't redesign anything. Publish, measure, and let the first wave of traffic tell you what's actually wrong.
