# FÆBRIQ — Shopify Admin Audit

**Date:** 2026/09/16
**Scope:** The admin surface the theme audit did not cover — store settings, sales channels, policies, payments, inventory, apps, analytics.
**Method:** Read-only, via the Shopify Admin API. No setting, product, theme or Printify change was made.
**Companion doc:** `LAUNCH_AUDIT_2026-09-16.md` (theme + competitive research)

**Short version:** you were right to push. Six new findings, two of which are more serious than anything in the first audit. One of them is a legal exposure, and one of them proves the blank homepage has already cost you money.

---

## 1. The number that changes the story

You've been describing this store as having "one sale." Shopify's own records disagree, and the funnel is worse than "no traffic yet."

| Metric | Value |
|---|---|
| Sessions (last 365 days) | **464** |
| Online store visitors | 446 |
| Sessions with cart additions | **2** |
| Sessions that reached checkout | **2** |
| Sessions that completed checkout | **0** |
| Orders (all statuses) | **0** |
| Conversion rate | **0.0%** |

Traffic by month: 7 (May), **220 (June)**, 51 (July), 107 (August), 79 (September so far).

**Two things follow from this.**

**The "one sale" is not in Shopify.** Zero orders, queried with `status:any`. Either it was a test order that was deleted, it happened on another channel, or the memory is wrong. Worth reconciling before you use it as a baseline for anything — including your bookkeeping.

**462 of 464 visitors never added anything to a cart.** A cart-add rate of **0.43%** against a typical 7–10% is not a copywriting problem or a pricing problem. It is roughly twentyfold below normal. It is exactly what you would expect from a store whose homepage renders `Select a collection in the theme editor to show the catalog here.` — which is what the published theme has been serving this entire time.

So the fixed theme isn't a nice-to-have that might help future traffic. There is already evidence that real people arrived, found no products, and left.

**One honest caveat.** The device split is **424 desktop / 38 mobile / 2 other**. Consumer retail traffic is normally mobile-majority, so a 91% desktop share suggests a large share of these 464 sessions were you, previews, and bots rather than genuine shoppers. I cannot separate them from here. Read the 0.43% as directional, not as a clean consumer benchmark. The **0 orders** figure, however, is exact.

---

## 2. Two contradictions inside your own policies

Your Refund, Shipping and Terms policies are **custom-written and genuinely good** — POD-aware, specific, well-structured. The Privacy policy is Shopify's standard template, correctly customised with your name, `support@faebriq.com` and your address. This is better than most stores at this stage. Two problems, though, and the first is serious.

### 2.1 🔴 The Refund policy denies refunds based on a size guide that does not exist

The Refund policy says, twice:

> "Please review our **size guides** carefully before purchasing."

> Non-returnable: "Incorrect size ordered (**please consult our size guide** before purchasing)"

**There is no size guide anywhere on the site.** Not in the live theme, not in the fixed theme, not in any product description, not on any page.

You are selling S–5XL, refusing refunds for wrong sizing, and justifying that refusal by pointing at a document you don't publish. In a category where sizing causes 50–70% of returns, that is a chargeback magnet and a consumer-protection problem, not just a UX gap.

This moves the size guide from "should fix soon" in the first audit to **launch blocker**. Either publish the measurements or rewrite the refund policy. Publishing the measurements is the better answer and roughly the same amount of work.
→ **Maurice supplies** measurements from Printify. **Then:** dev task.

### 2.2 🟠 The Shipping policy contradicts how you actually charge for shipping

The Shipping policy says:

> "Shipping costs are **calculated at checkout** based on your destination and order. Any promotional **free-shipping thresholds** will be shown on the Site."

Neither is true. Verified in the delivery profiles: every product sits on a US & Canada zone with a **FREE SHIPPING** rate at $0.00, and free shipping is baked into every listed price. There is no threshold and nothing is calculated.

Meanwhile the About page says *"Free shipping, priced into every listing,"* the fixed PDP says *"Free shipping to the US & Canada,"* and the hero says *"Free shipping to the US & Canada."* So your policy page is the one surface telling customers something different, and it's the surface a cautious buyer checks before paying.
→ **Pure copy fix.** Rewrite section 3. Ten minutes.

### 2.3 Smaller policy notes

- **Both the Refund policy and the Terms promise PayPal** ("Shopify Payments or PayPal"). I can confirm Shopify Payments with Shop Pay, Apple Pay and Google Pay wallets are active, but I **could not verify PayPal is actually enabled**. If it isn't, two policies are promising a payment method you don't offer. Check Settings → Payments.
- **Production time still disagrees with itself:** policies and the Contact page say **2–7 business days**; every product description and the PDP delivery block say **5–7**. Flagged in the first audit, repeating because it's now in three places.
- **Your home address is published.** The Privacy policy carries `164 Finch Ave E, North York, ON, M2N 4R9, CA`, and that's also your only Shopify location. Legally normal and usually required — but you're a solo operator putting a residential address on a public queer-brand website. Worth a conscious decision rather than a default. A registered agent or a mailbox service is the usual workaround.
→ **Maurice decides.**

---

## 3. Sales channels — two real problems

Five channels are installed: **Online Store, Point of Sale, Shop, Manus, TikTok**.

### 3.1 🟠 Nothing is published to the Shop channel

Checked product by product. All 12 active products: `Online Store: true`, `TikTok: true`, **`Shop: false`**, `Point of Sale: false`.

The repo's own `SOCIAL_LAUNCH_NOTES.md` plans to link the Shop app from your social profiles once the site is live — for the Follow button and in-app checkout. **As configured, anyone following that link lands on an empty store.**

Publishing to Shop is a checkbox per product. But note the same file's gate: the Shop app is a pure image grid with no copy to compensate, so it's the harshest possible showcase for the sticker photography. Do the imagery first, then publish to Shop.
→ **Maurice decides** the sequencing; the publish itself is trivial.

### 3.2 🟠 Everything is already live on TikTok

All 12 products are published to the TikTok channel right now. That includes the three sticker SKUs with the known defective pride-bar artwork.

You told me you're *about* to start posting to social. Your catalogue is already listed on the one channel where a product page can be surfaced without you posting anything.
→ **Maurice decides:** either unpublish the three defective stickers from TikTok too, or fix the artwork. Same decision as the first audit, wider blast radius than assumed.

### 3.3 A correction to my own first audit

I called the 12 empty Printify delivery profiles "purely cosmetic." That was too generous.

`shop.shipsToCountries` returns **roughly 200 country codes** — AD, AE, AF, AL, AM, AO, AR, AU, AT, BE, BR, DE, FR, GB, JP, and on and on. That field is derived from shipping zones across *all* delivery profiles, including the empty Printify ones.

Your actual selling surface is still correctly locked down — Markets contain only United States and Canada, and every product sits on a US/CA-only profile. A German customer cannot check out. **But** `shipsToCountries` is a shop-level field that apps and sales channels read, and you have channels installed (TikTok, Shop, Microsoft Copilot) that may use it to describe where you ship.

So cleaning up those profiles is not tidiness. It stops your store advertising ~200 countries it will not ship to.
→ **Maurice, in Printify/Shopify admin.** Delete the 12 profiles with zero variants.

---

## 4. 🟠 Admin security — three AI agents can rewrite your store

Six apps are installed. Four hold broad write access:

| App | Notable scopes |
|---|---|
| **Printify** | `write_products`, `write_publications`, `write_shipping`, `write_script_tags` |
| **Shopify Claude Connector** | `write_themes`, `write_products`, `write_markets`, `write_discounts`, `write_orders` |
| **Shopify Perplexity MCP App** | `write_themes`, `write_products`, `write_markets`, `write_discounts`, `write_orders`, `write_checkouts` |
| **Zapier** | `write_orders`, `write_products`, `write_content`, `write_inventory`, `write_draft_orders` |

Plus `Digital Products` and `Messaging` (both Shopify's own), and a **Manus** sales-channel publication.

**Three separate AI or automation agents — Claude, Perplexity and Zapier — can write to your products and themes.** Claude and Perplexity can both publish themes.

That is very plausibly how the live theme ended up back on `faebriqtheme-launch-2026-08-06-review` after your 2026/09/05 changelog note recorded `faebriqtheme-launch-fix` as MAIN. I can't prove which agent did it, and I'm not going to guess. But an account where three agents hold `write_themes` is an account where "who changed this?" has no answer, and you've already been burned twice by sessions that reported changes that weren't real.

**Recommendation:** uninstall what you're not actively using. If you aren't running Perplexity against this store, remove it — it currently has the same power over your storefront as I do. Keep Printify (you need it) and keep one AI connector.
→ **Maurice decides.** Settings → Apps and sales channels.

---

## 5. Verified healthy — do not spend time here

Everything below I checked and found correct. Leave it alone.

| Area | State |
|---|---|
| **Storefront password** | **Disabled.** The store is publicly reachable — no hidden gate |
| **Store setup** | `setupRequired: false`. No outstanding Shopify onboarding steps |
| **Product publication** | All 12 active products published to Online Store. The archived cap is correctly published nowhere |
| **Payments** | Shopify Payments active, with Shop Pay, Apple Pay and Google Pay wallets enabled |
| **Inventory policy** | Every variant is `CONTINUE` — the store keeps selling at zero stock, which is the correct and necessary setting for print-on-demand |
| **Sizes** | S, M, L, XL, 2XL, 3XL, 4XL, **5XL** confirmed on the tee. Pricing tiers: $34 (S–XL), $36 (2XL–3XL), $37 (4XL–5XL) |
| **Markets** | United States and Canada only, both enabled, US primary |
| **Delivery on real products** | Both profiles carrying products are US & Canada, FREE SHIPPING |
| **Policies** | All four exist with live URLs. Refund, Shipping and Terms are custom-written and specific |
| **Product metafields** | No definitions at all — clean, no leftover Printify junk |
| **URL redirects** | Two in place, catching dead product handles |
| **Locations** | One active location, correctly configured |
| **Customer accounts** | `OPTIONAL` — right setting for a first launch; not forcing signup |
| **Shop SEO description** | Set and on-voice |

**Correction to the first audit:** I wrote tee pricing as "2XL $36, 3XL+ $37." Exact figures are 2XL **and** 3XL at $36, 4XL **and** 5XL at $37.

---

## 6. Minor findings

- **A blog exists that nothing can render.** There's a blog titled `News` (handle `news`), but neither theme has `templates/blog.liquid` or `templates/article.liquid`. `/blogs/news` would 404. Harmless while nothing links to it — but Code Culture's SEO blog was one of my competitive recommendations, so if you act on that, the templates need building first.
- **Both URL redirects point somewhere semantically wrong.** `/products/deploying-identity-v2-tee` → the *Error 404* tee, and `/products/please-hold-rebranding-tote` → the *Error 404* tote. Someone searching for a Deploying Identity tee lands on a different design. Better than a 404, worse than correct.
- **Design coverage across product types is uneven.** Error 404 exists as tee, tote and sticker. Code It. Serve It. as tee and sticker. Deploying Identity as crewneck and sticker but **no tee**. Off The Clock as hoodie only. Please Hold and It's Not A Bug as **stickers only**. Two of your five statements can only be bought for $4–$6. That caps what a customer who loves that line can spend.
- **Three different contact emails are in play.** Shopify's public-facing `contactEmail` is **`m.knuever@mkglobalhorizons.com`**, every policy says **`support@faebriq.com`**, and the live theme's footer says **`hello@faebriq.com`**. Shopify's own order confirmations and contact surfaces use the first one — so a FÆBRIQ customer gets email from an unrelated business domain. Set the shop contact email to `support@faebriq.com`.
- **Tee weight is recorded as 0.1 kg.** Light for a 180 g/m² garment. No practical effect while shipping is free and flat, but it would matter if you ever enable calculated rates.

---

## 7. Updated punch list — what this audit adds

Merge these into the list in `LAUNCH_AUDIT_2026-09-16.md`.

### 🔴 New launch blockers

| # | Item | Type |
|---|---|---|
| **A** | **Size guide** — promoted from "should fix" to blocker. Your Refund policy denies size-related refunds by pointing at a guide you don't publish. | Maurice supplies measurements → dev |
| **B** | **Fix Shipping policy section 3.** It tells customers shipping is calculated at checkout and hints at a threshold. Both false. | Pure copy fix, 10 min |
| **C** | **Decide on the three defective stickers for TikTok as well as the website.** They are already live on the TikTok channel. | Maurice decides |

### 🟠 New "should fix soon"

| # | Item | Type |
|---|---|---|
| **D** | **Audit installed apps.** Remove any AI/automation connector you aren't using. Three agents currently hold `write_themes`. | Maurice decides |
| **E** | **Delete the 12 empty Printify delivery profiles.** They put ~200 countries into `shipsToCountries`, which installed channels can read. | Maurice, in admin |
| **F** | **Set shop contact email to `support@faebriq.com`.** Order emails currently come from `mkglobalhorizons.com`. | Maurice, 2 min |
| **G** | **Verify PayPal is enabled**, or remove it from the Refund policy and Terms. | Maurice checks |
| **H** | **Decide about the public home address** in the Privacy policy. | Maurice decides |
| **I** | **Publish products to the Shop channel** — after the sticker imagery is fixed, per `SOCIAL_LAUNCH_NOTES.md`. | Maurice decides sequencing |

### 🟡 New later items

| # | Item |
|---|---|
| **J** | Fix the two semantically-wrong URL redirects |
| **K** | Build blog/article templates, or delete the unused `News` blog |
| **L** | Fill the design-coverage gaps — Deploying Identity and Please Hold exist only as low-ticket items |
| **M** | Correct the 0.1 kg tee weight if calculated shipping is ever enabled |

---

## 8. Bottom line

**No, it wasn't all fine.** The first audit stopped at the theme. The admin side had six more findings, and two of them matter more than most of what was in it:

Your **Refund policy refuses size-related refunds on the strength of a size guide you don't publish**. That's the kind of thing that turns a bad fit into a chargeback, and it's live right now.

And **464 sessions have already produced 2 cart additions and 0 orders**. Even discounting heavily for your own traffic and bots, nobody is reaching a cart — which is precisely the symptom of a homepage that renders a theme-editor placeholder instead of twelve products.

Everything structural underneath is sound. Password off, payments live, inventory policy correct for POD, markets locked to US and Canada, policies written and specific, no data junk. This is not a broken store. It is a well-built store serving the wrong theme, with a policy contradiction and a Shopify account that three AI agents can write to.

Publish the fixed theme, publish the size guide, fix one paragraph of the Shipping policy, and prune the apps. Then post.
