# Handoff: site review fixes, 2026/09/16

Everything in your list, split by whether I could apply it or whether it needs you.

---

## Already applied, live now

These went in through the Shopify API. Nothing for you to do.

**All 12 product descriptions rewritten.** Every em dash and en dash removed. More importantly, the five sticker descriptions all shared one identical sentence (`set over the signature pride-circuit bar. Sized for a laptop lid, a notebook, or [one swapped noun]`). That mail-merge pattern was the single biggest "this was generated" tell on the site. Each sticker now has its own copy.

**All 12 SEO titles and descriptions rewritten.** Dashes removed, phrasing varied.

**One product title changed.** `FÆBRIQ Sticker Sheet — The Full Drop` became `FÆBRIQ Sticker Sheet: The Full Drop`. The handle was not touched, so no links break.

**Contact page and About page bodies rewritten.** Dashes out, tightened.

**Removed the PayPal claim** from copy I rewrote. Two policies promised PayPal and I could not verify it is enabled. If it is, say so and I will put it back.

> Note: the About page you see on the site does **not** come from the Shopify About page record. The copy is hardcoded in `templates/page.about.liquid`. I updated both so they cannot drift apart, but the template is the one that renders.

---

## Needs you: three theme files

The Shopify connector refuses theme file writes to the live theme. These are ready to paste.

Go to **Online Store → Themes → faebriqtheme-launch-fix → Edit code**.

| File | Action | What it fixes |
|---|---|---|
| `templates/policy.liquid` | **Create new** | Privacy, Refund, Shipping and Terms pages. Centred, and styled like the rest of the site instead of Shopify's bare fallback |
| `templates/page.about.liquid` | Replace | The font problem, plus one em dash |
| `templates/page.contact.liquid` | Replace | Two em dashes in hardcoded strings |

Source files are in `theme/faebriqtheme-launch-fix/templates/` in this repo.

### What the font problem actually was

The About page ran four type treatments in one screen. The headline used the display serif, the body used the sans, and then two *near-identical but different* mono styles sat a few hundred pixels apart: the "About" eyebrow at 0.28em letter-spacing, and the Design/Product/Voice headings at 0.12em. Two almost-matching monos read as a mistake, which is what you were seeing.

Fixed by collapsing every label to one class, `fae-section-label`. The page now uses the same three roles as every other page: serif for the headline, sans for running copy, one mono for all labels.

### Why the policy pages were not centred

There was no `templates/policy.liquid`. Without it Shopify renders policies with its own bare fallback, which ignores your theme entirely. That is why Contact looked right and Privacy did not. The new file mirrors `page.liquid` and adds `fae-page--centered`.

---

## Needs you: three policies

The connector has read-only access to legal policies, so I cannot write these. Paste them in **Settings → Policies**, using the `<>` HTML view in the editor.

| Policy | File | Why |
|---|---|---|
| Refund policy | `handoff/policy-refund.html` | **Fixes a real liability.** It told customers twice to consult a size guide that does not exist, then refused size refunds on that basis. Now it points to the guide where one exists and invites an email where one does not |
| Shipping policy | `handoff/policy-shipping.html` | **Fixes a contradiction.** Section 3 said shipping is calculated at checkout and hinted at a free-shipping threshold. Neither is true. Now states plainly that shipping is free to the US and Canada with no minimum |
| Terms of service | `handoff/policy-terms.html` | Two em dashes in section 7, plus the PayPal claim |

**Privacy policy needs no text change.** I checked the full body: it contains zero em dashes and zero en dashes. Once `policy.liquid` is in, it will be centred like the others.

I also dropped "Additional regions, including Europe, are coming soon" from the shipping policy. It is a promise with no date attached. Tell me if you want it back.

---

## The imagery problem

This is the right thing to be worried about, and the plan you floated needs one correction before you spend money on it.

### What is actually wrong, in three separate problems

**1. Three sticker designs print wrong.** Known, root-caused, blocked on source artwork. This is a file problem, not a photography problem. No imagery pipeline fixes it.

**2. The print looks pasted on, not printed into fabric.** This is what you mean by "text placed above, like separate." Printify's mockup generator composites flat artwork onto a garment photo with no displacement map, so the print does not follow the weave, the folds, or the lighting. Your eye reads it as a sticker floating on a photo, because that is literally what it is.

**3. The compositions are flat.** Studio product shot, no scale reference, no context, no human. For stickers this is fatal: a customer cannot see the die-cut edge, cannot judge size, and cannot tell transparent from white, even though you sell both.

### The correction to your plan

**Do not let a generative image model regenerate your print.** Nano Banana, Seedream, Flux Kontext and everything in that class will redraw the artwork. Your entire product is typography and a six-block bar with exact hex values. A generative model will drift the letterforms, soften the bar edges, and invent a seventh stripe. For most brands that is cosmetic. For yours it destroys the product.

The pipeline that works:

- **The garment, the scene, the lighting, the model: generative is fine.** That is what these models are good at.
- **The print itself: composited, never generated.** Take the real PNG from `assets/print-art/` (you already have 4500px masters) and warp it onto the garment with a displacement map so it follows the fabric.

That gives you the realism you are missing without risking the artwork.

### What I would actually do, cheapest first

**Option A, displacement-map mockup tool. Start here.** Placeit, Mockup World, or a Photoshop/Photopea smart-object template. You upload your existing print master, it wraps onto a real photographed garment with real fabric displacement. Pixel-exact print, realistic result, roughly $15 to $30 a month or a one-off template purchase. No AI, no drift. This single change fixes problem 2 across the whole catalogue.

**Option B, for stickers specifically: photograph one real sticker.** Order one sheet, put it on your actual laptop, shoot it on a phone. One honest photo with a visible die-cut edge and something for scale beats any render. It also settles the transparent-versus-white question that no render currently answers. Cost: one sticker order.

**Option C, generative for lifestyle scenes only.** Once A is working, use an image model for the *context* shots: a desk, a café, a hand holding the tote. Then composite the real print in. This is where a separate AI model genuinely earns its place, and it is the last step, not the first.

### On the "separate AI model" question

Yes, worth doing, but scope it to scene generation and product placement, not print rendering. And sequence it third. Option A alone will move your product pages more than a generative pipeline will, and it costs less and cannot corrupt the brand asset.

**What I need from you to go further:** the Printify blank model names for the tee, hoodie and crewneck. With those I can pull the manufacturer's official size charts and finish the size guide, which is still the last open launch blocker.
