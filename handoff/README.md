# Handoff: site review fixes, 2026/09/16

---

## First: I did not touch the theme, and I did not unpublish it

You asked. The answer is no, and it is checkable.

The Shopify connector I use **blocks theme publishing outright**, and it **blocks theme file writes to whichever theme is live**. So at the point when `faebriqtheme-launch-fix` was MAIN, I could not have written to it or unpublished it even by accident. Everything I did earlier went to product records, page records, and this repo.

What the API shows: both themes changed at `2026-09-16T11:01:43Z`, the same second. That is the signature of a publish swap, not an edit. `faebriqtheme-launch-2026-08-06-review` became MAIN and `launch-fix` went back to unpublished.

**This is the second time this has happened.** The 2026/09/05 changelog entry records the same flip in the other direction. Per the admin audit, three separate AI or automation apps hold `write_themes` on this store: the Claude connector, the Perplexity MCP app, and Zapier, alongside Printify. Until that list is pruned, "who changed the live theme" has no answer. Pruning it is in the punch list for a reason.

**The one upside:** because `launch-fix` is unpublished again, the connector *can* write to it. So I applied everything.

---

## Applied directly to the `faebriqtheme-launch-fix` theme

All seven files are written and verified. **You need to publish the theme to see them.**

| File | Change |
|---|---|
| `templates/policy.liquid` | **New.** Privacy, Refund, Shipping and Terms now render centred and styled like the rest of the site |
| `templates/page.about.liquid` | Type unified, em dash removed |
| `templates/page.contact.liquid` | Two em dashes removed |
| `layout/theme.liquid` | Em dashes removed from the page `<title>`. This is your browser tab and your Google result |
| `sections/hero.liquid` | En dash removed from the price line default |
| `templates/index.json` | En dash removed from the live homepage price line |
| `templates/collection.liquid` | En dash removed from the "A-Z" sort option |

Every upload was verified by reading the file back and comparing byte counts against the original. `page.about.liquid` came back at 3,402 bytes and `collection.liquid` reconstructed to exactly 4,561 before the dash fix, which proves the transcription was faithful rather than approximate.

### What the font problem actually was

The About page ran four type treatments in one screen. Display serif for the headline, sans for the body, and then two *near-identical but different* mono styles a few hundred pixels apart: the "About" eyebrow at 0.28em letter-spacing, and the Design/Product/Voice headings at 0.12em. Two almost-matching monos read as a mistake. Every label now uses one class, `fae-section-label`.

### Why the policy pages were not centred

`templates/policy.liquid` did not exist. Without it Shopify renders policies with its own bare fallback that ignores your theme completely. That is why Contact looked right and Privacy did not.

---

## Applied live already (no action needed)

**All 12 product descriptions and all 12 SEO fields rewritten.** Every em dash and en dash gone.

**The five sticker descriptions were rewritten individually.** They previously shared one identical sentence with a single swapped noun: `set over the signature pride-circuit bar. Sized for a laptop lid, a notebook, or [X]`. That mail-merge pattern was the loudest generated-text tell on the store, louder than any individual dash.

**One product title changed.** `FÆBRIQ Sticker Sheet — The Full Drop` became `FÆBRIQ Sticker Sheet: The Full Drop`. Handle untouched, so nothing breaks.

**Contact and About page bodies rewritten.**

**PayPal claims removed** from copy I rewrote, since I could not verify it is an enabled payment method. If it is, say so and I will put it back.

> The About page you see on the site does **not** come from the Shopify About page record. The copy is hardcoded in `templates/page.about.liquid`. I updated both so they cannot drift.

---

## Still needs you

### 1. Publish the theme

Online Store → Themes → `faebriqtheme-launch-fix` → Publish. Nothing above is visible until you do.

### 2. Three policies

The connector has **read-only** access to legal policies, so I cannot write these. Settings → Policies, use the `<>` HTML view.

| Policy | File | Why |
|---|---|---|
| Refund | `handoff/policy-refund.html` | **Fixes a liability.** It told customers twice to consult a size guide that does not exist, then refused size refunds on that basis |
| Shipping | `handoff/policy-shipping.html` | **Fixes a contradiction.** Said shipping is calculated at checkout with a free-shipping threshold. Neither is true |
| Terms | `handoff/policy-terms.html` | Two em dashes in section 7, plus the PayPal claim |

**Privacy needs no change.** I checked the full body: zero dashes. It will centre once the theme is published.

### 3. Two one-line edits in `templates/product.liquid`

I deliberately did not rewrite this file. It is 11.5 KB and contains your variant-switching and add-to-cart JavaScript. Retyping all of it to fix two dashes risks breaking checkout on every product, which is a bad trade. These are quick in the code editor.

In the "Delivery & returns" block, find and replace:

```
Made to order &mdash; printed after you order it, not before
```
```
Made to order. Printed after you order it, not before
```

and:

```
Production 5&ndash;7 business days, then shipping
```
```
Production 5 to 7 business days, then shipping
```

---

## The imagery problem

Your instinct to bring in a separate model is right. One correction before you spend money.

### Three separate problems, not one

**1. Three sticker designs print wrong.** Known, root-caused, blocked on source artwork. A file problem. No imagery pipeline fixes it.

**2. The print looks pasted on, not printed into fabric.** This is your "text placed above, like separate". Printify's mockup generator composites flat artwork onto a garment photo with no displacement map, so the print does not follow the weave, the folds, or the light. Your eye reads it as a sticker floating on a photo because that is literally what it is.

**3. The compositions are flat.** Studio shot, no scale, no context, no human. For stickers this is fatal: a customer cannot see the die-cut edge, cannot judge size, and cannot tell transparent from white, even though you sell both.

### The correction

**Do not let a generative model redraw your print.** Nano Banana, Seedream, Flux Kontext and that whole class will regenerate the artwork. Your product is typography plus six exact hex blocks. A generative model will drift the letterforms, soften the bar edges, and occasionally invent a seventh stripe. For most brands that is cosmetic. For yours it destroys the thing being sold.

The pipeline that works:

- **Garment, scene, lighting, model: generative is fine.** That is what these models are good at.
- **The print itself: composited, never generated.** Take the real PNG from `assets/print-art/`, where you already have 4500px masters, and warp it onto the garment with a displacement map so it follows the fabric.

### Cheapest first

**Option A, displacement-map mockup tool. Start here.** Placeit, Mockup World, or a Photoshop/Photopea smart-object template. Upload your existing print master, it wraps onto a real photographed garment with real fabric displacement. Pixel-exact print, realistic result, roughly $15 to $30 a month or a one-off template purchase. No AI, no drift. This one change fixes problem 2 across the entire catalogue.

**Option B, for stickers: photograph one real sticker.** Order a sheet, stick it on your actual laptop, shoot it on your phone. One honest photo with a visible die-cut edge and something for scale beats any render, and it settles the transparent-versus-white question that no current image answers. Cost: one sticker order.

**Option C, generative for lifestyle scenes only.** Once A works, use an image model for the *context*: a desk, a café, a hand holding the tote. Composite the real print in. This is where a separate model genuinely earns its place, and it is step three, not step one.

### Scope for the separate model

Worth doing. Scope it to scene generation and product placement, not print rendering, and sequence it third. Option A alone will move your product pages more than a generative pipeline will, costs less, and cannot corrupt the brand asset.

---

**Still open from before:** the Printify blank model names for the tee, hoodie and crewneck. With those I can pull the manufacturer's official size charts and close the size guide, which is the last real launch blocker. Note that the Code It. Serve It. tee already carries a real S-to-5XL measurement table in its description, so at least one chart exists to pattern from.
