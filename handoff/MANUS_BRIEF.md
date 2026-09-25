# FÆBRIQ: browser tasks for Manus

Paste this whole file into Manus as the task brief.

---

## Who you are working for

FÆBRIQ is a queer-coded dark-tech merch brand. Shopify store at **faebriq.com**
(admin: `ufyytt-er.myshopify.com`), fulfilled by **Printify**. Solo operator.
Currency USD, ships to the US and Canada only, free shipping is built into the
listed prices.

You have browser access to the Shopify admin and to Printify. That is why these
four jobs are yours: they all need a logged-in browser session, and the API
integration that did the rest of the work cannot reach them.

---

## Hard rules. Do not break these.

1. **Never sync or publish from Printify to Shopify.** A Printify publish
   overwrites the Shopify product descriptions, which currently hold hand
   written copy and hand built size guides. This would destroy days of work.
   If Printify offers to "publish" or "sync" a product, decline.
2. **Do not change any price, product handle, product title, SEO title or SEO
   description.** Not one. They are set deliberately.
3. **Do not publish, unpublish or duplicate any theme.** Work inside the theme
   that is already live: `faebriqtheme-launch-fix`.
4. **Do not touch the size guides** in the tee, crewneck and hoodie
   descriptions. They were just added and they are correct.
5. **Never write the word "embroidery" or "embroidered" anywhere.** The cap is
   OTTO 18-253 printed DTF. Embroidery is unverified.
6. **No em dashes and no en dashes anywhere.** Not in copy, not in code, not in
   your own notes back to me. Use a comma, a full stop, or the word "to" for
   ranges. This is a standing brand rule and the site was just cleaned of them.
7. **No purchases without showing me the checkout screen first** and waiting for
   a yes.
8. If a step does not match what is described here, **stop and report it**
   instead of improvising. Do not guess.

---

## Task 1. Replace three legal policies

Shopify admin: **Settings, then Policies.**

For each of the three below, open the policy, switch the editor to HTML view
(the `<>` button in the toolbar), select all the existing content, delete it,
paste the replacement exactly as given, and save.

**Leave the Privacy policy alone.** It has already been checked and needs no
change.

### Why each one is being replaced

- **Refund policy**: the current text tells customers twice to consult a size
  guide, then refuses size related refunds on that basis. Until today no size
  guide existed. That is a live chargeback risk.
- **Shipping policy**: the current text says shipping is calculated at checkout
  and that there is a free shipping threshold. Neither is true. Shipping is free
  to the US and Canada with no minimum, baked into the listed price.
- **Terms of service**: contains em dashes and a claim about PayPal that could
  not be verified.

### Refund policy, replacement HTML

```html
<p><br></p>
<hr>
<p>At <strong>FÆBRIQ</strong>, every item is made to order through our print-on-demand partners. Each piece is produced specifically for you once you order, so we can't accept returns or refunds for a change of mind, or for a size that turned out wrong. This does not affect your statutory rights where they apply.</p>
<p><strong>Not sure about sizing?</strong> Check the size guide on the product page where one is shown. If you are between sizes, or the piece you want doesn't have a chart yet, email <a href="mailto:support@faebriq.com">support@faebriq.com</a> before you order and we will send you the measurements. We would rather answer a question than process a problem.</p>
<p><strong>1. Damaged, defective, or misprinted items</strong></p>
<p>We stand behind the quality of our products. If your order arrives damaged, defective, or with a printing error, we will replace it or refund it at no cost to you.</p>
<p>To be eligible, contact us at support@faebriq.com within 30 days of delivery and include:</p>
<ul>
<li>Your order number</li>
<li>A clear photograph of the damaged, defective, or misprinted item</li>
<li>A description of the issue</li>
</ul>
<p>Once your claim is approved we will arrange a free replacement or a full refund to your original payment method. In most cases you will not be asked to return the faulty item.</p>
<p><strong>2. Wrong item received</strong></p>
<p>If you receive something different from what you ordered, whether that is the wrong design, size, or product, contact us at support@faebriq.com within 30 days of delivery with your order number and a photo. We will send the correct item at no extra charge.</p>
<p><strong>3. What we cannot refund</strong></p>
<ul>
<li>Change of mind or buyer's remorse</li>
<li>Incorrect size ordered. Message us before you buy if you are unsure and we will help</li>
<li>Items damaged through normal wear, improper washing, or misuse</li>
<li>Claims made more than 30 days after delivery</li>
</ul>
<p><strong>4. Lost or stuck shipments</strong></p>
<p>If tracking shows your order as lost in transit, or it runs well past the estimated delivery window, get in touch. See our Shipping Policy for the details. We will work with our fulfillment partners to sort it out.</p>
<p><strong>5. Refund processing</strong></p>
<p>Approved refunds go back to your original payment method. Allow up to 10 business days for the refund to appear, depending on your bank or card issuer.</p>
<p><strong>6. Order changes and cancellations</strong></p>
<p>Items go into production quickly, so we can only change or cancel an order within 24 hours of purchase. Email support@faebriq.com as soon as you can. Once production starts, changes are no longer possible.</p>
<p><strong>7. Contact us</strong></p>
<p>support@faebriq.com</p>
<hr>
<p><br></p>
```

### Shipping policy, replacement HTML

```html
<p><br></p>
<hr>
<p><strong>FÆBRIQ</strong> ships to the United States and Canada. Every item is made to order through our print-on-demand partners, so your total delivery time is two things added together: production time, then shipping time.</p>
<p><strong>1. Production time</strong></p>
<p>Each item is printed and prepared for you after you order. Typical production time is 2 to 7 business days before your order ships. During busy periods such as holidays, sales and new drops, it can run a little longer.</p>
<p><strong>2. Shipping time</strong></p>
<p>Once your order leaves our fulfillment partner, estimated transit times are:</p>
<ul>
<li>United States: 4 to 8 business days</li>
<li>Canada: 7 to 14 business days</li>
</ul>
<p>These are estimates, not guarantees. Total delivery time is production time plus shipping time. We currently ship only within the United States and Canada.</p>
<p><strong>3. Shipping costs</strong></p>
<p><strong>Shipping is free to the United States and Canada.</strong> There is no minimum and no threshold to hit. The cost is already built into the price you see on the product page, so the number at checkout is the number you pay.</p>
<p><strong>4. Order tracking</strong></p>
<p>Once your order ships you will get a confirmation email with tracking. Allow 24 to 48 hours for tracking to start updating after dispatch.</p>
<p><strong>5. Customs, duties and taxes</strong></p>
<p>Orders shipped to Canada may be subject to import duties, taxes and customs fees charged by Canadian authorities. These are the responsibility of the recipient and are not included in the product price. FÆBRIQ has no control over these fees and cannot predict what they will be.</p>
<p><strong>6. Incorrect address</strong></p>
<p>Please check your shipping address at checkout. We are not responsible for orders sent to an address that was entered incorrectly. If you spot a mistake, email support@faebriq.com within 24 hours of ordering and we will do what we can before production starts.</p>
<p><strong>7. Lost, delayed, or stuck shipments</strong></p>
<p>If tracking has not updated for a long stretch, or your order runs well past the estimated window, email support@faebriq.com with your order number. We will work with our fulfillment and shipping partners to locate the package or arrange a replacement where appropriate. See our Refund Policy.</p>
<p><strong>8. Contact us</strong></p>
<p>support@faebriq.com</p>
<hr>
<p><br></p>
```

### Terms of service, replacement HTML

```html
<p><br></p>
<hr>
<p>Welcome to <strong>FÆBRIQ</strong>. These Terms of Service ("Terms") govern your access to and use of our website faebriq.com and any related media (collectively, the "Site"), and your purchase of products from us. By accessing the Site or placing an order, you agree to be bound by these Terms. If you do not agree, please do not use the Site.</p>
<p><strong>1. Eligibility</strong></p>
<p>You must be at least 18 years old, or the age of majority in your jurisdiction, to make a purchase. By using the Site you represent that you meet this requirement.</p>
<p><strong>2. Products and print-on-demand</strong></p>
<p>All FÆBRIQ products are made to order through third-party print-on-demand partners. Each item is produced specifically for you after you place your order. Because of the nature of print-on-demand production:</p>
<ul>
<li>Slight variations in colour, print placement, and fabric may occur between items and from what is shown on screen.</li>
<li>Product images are representative. Actual items may differ slightly.</li>
<li>We reserve the right to limit quantities, discontinue products, or refuse any order at our discretion.</li>
</ul>
<p><strong>3. Pricing and payment</strong></p>
<p>All prices are listed in the currency shown at checkout and are subject to change without notice. Payment is processed securely through Shopify's checkout. You agree to provide current, complete, and accurate purchase and account information. We are not responsible for any additional bank, card, or currency-conversion fees charged by your provider.</p>
<p><strong>4. Orders and acceptance</strong></p>
<p>Your receipt of an order confirmation does not constitute our acceptance of your order. We reserve the right to accept or decline any order, and to cancel orders due to suspected fraud, pricing errors, or product unavailability. If we cancel an order after payment, you will receive a full refund.</p>
<p><strong>5. Shipping and delivery</strong></p>
<p>Shipping times and costs are described in our Shipping Policy. As a print-on-demand business, total delivery time includes both production and transit. We are not liable for delays caused by carriers, customs, or events outside our control.</p>
<p><strong>6. Returns and refunds</strong></p>
<p>Returns and refunds are governed by our Refund Policy. Because items are made to order, we generally do not accept returns except for damaged, defective, misprinted, or incorrect items.</p>
<p><strong>7. Intellectual property</strong></p>
<p>All content on the Site, including designs, logos, text, graphics, and the FÆBRIQ name and marks, is the property of FÆBRIQ or its licensors and is protected by intellectual property laws. You may not reproduce, distribute, or create derivative works from our content without prior written permission.</p>
<p><strong>8. User conduct</strong></p>
<p>You agree not to use the Site for any unlawful purpose, to infringe our or others' intellectual property, to transmit harmful code, or to interfere with the Site's operation or security.</p>
<p><strong>9. Disclaimer of warranties</strong></p>
<p>The Site and all products are provided on an "as is" and "as available" basis without warranties of any kind, express or implied, except as required by applicable law.</p>
<p><strong>10. Limitation of liability</strong></p>
<p>To the fullest extent permitted by law, FÆBRIQ shall not be liable for any indirect, incidental, special, or consequential damages arising from your use of the Site or products. Our total liability for any claim shall not exceed the amount you paid for the product giving rise to the claim.</p>
<p><strong>11. Changes to these Terms</strong></p>
<p>We may update these Terms at any time. Changes take effect when posted to the Site. Your continued use of the Site after changes constitutes acceptance of the revised Terms.</p>
<p><strong>12. Contact us</strong></p>
<p>support@faebriq.com</p>
<hr>
<p><br></p>
```

**Verify:** open faebriq.com, click through to each of Refund, Shipping and
Terms in the footer, and confirm the new text is live, centred, and dark themed
like the rest of the site. If a policy page renders unstyled on a white
background, say so.

---

## Task 2. Two text replacements in the theme code

Shopify admin: **Online Store, Themes, `faebriqtheme-launch-fix`, then the three
dot menu, Edit code.**

Open `templates/product.liquid`. It is about 11.5 KB and contains the variant
switching and add to cart JavaScript. **Change only the two strings below.**
Touch nothing else in that file. Breaking it breaks checkout on every product.

Find:

```
Made to order &mdash; printed after you order it, not before
```

Replace with:

```
Made to order. Printed after you order it, not before
```

Find:

```
Production 5&ndash;7 business days, then shipping
```

Replace with:

```
Production 5 to 7 business days, then shipping
```

Save.

**Verify:** open any product page on faebriq.com, scroll to the "Delivery and
returns" block, and confirm both lines now read as plain text with no dash
characters. Then add any product to the cart and confirm the cart drawer opens
and shows the item. If add to cart fails, revert the file immediately using the
theme editor's version history and tell me.

---

## Task 3. Establish which sticker artwork is actually wrong

This is an investigation, not a fix. **Do not unpublish or delete anything.**

There is an unverified claim that three sticker designs print incorrectly.
Nobody has produced evidence. Your job is to settle it with evidence or report
that you cannot.

In **Printify**, open each of the six sticker products in turn. For each one:

1. Open the actual **print file** or design file, the artwork that goes to the
   printer. Not the mockup preview. The mockup is a composite and will not show
   the fault.
2. Look for: cut off edges, the design not centred in the print area, wrong
   canvas size, a transparent background where a white one is expected or the
   reverse, low resolution, or the pride bar rendering with the wrong number of
   stripes or wrong colours.
3. Screenshot anything that looks wrong.

The six sticker listings are:

- "It's Not A Bug. It's Me." Sticker
- "Code It. Serve It." Sticker
- "Error 404: Straight Not Found" Sticker
- "Please Hold, I'm Rebranding My Identity" Sticker
- "Deploying Identity v2.0" Sticker
- Sticker Sheet: The Full Drop

**Report back per sticker**: name, whether the print file looks correct, and if
not, exactly what is wrong, with the screenshot. If all six look fine in
Printify, say that plainly. "Cannot tell from Printify alone" is an acceptable
and useful answer. Do not guess which three are broken in order to produce three.

---

## Task 4. Confirm the homepage is rendering

Open **faebriq.com** in a fresh browser tab, logged out or in a private window.

Confirm all five, and screenshot the full page at desktop width and again at
phone width:

1. A narrow bar across the very top reading "Free shipping to the US & Canada"
   and "Made to order, printed after you buy".
2. A hero with the FÆBRIQ wordmark and text on the left, and a product image on
   the right with a small badge reading "The Flagship", a product title and a
   price under it.
3. A row of four short facts below the hero: free shipping, made to order, 2 to
   7 days to print, misprints covered.
4. A section titled "The Drop" showing **six** product cards, with a "View all
   All Products" button under it.
5. Click that button and confirm it loads a collection page with all 12
   products, not a 404.

If the "The Drop" section instead shows the words "Select a collection in the
theme editor", stop and report it. That means a fix applied earlier did not
hold.

---

## How to report back

One message, in this order:

1. **Task 1**: which policies you replaced, and what the live pages look like.
2. **Task 2**: both strings changed yes or no, and whether add to cart still
   works.
3. **Task 3**: the six sticker verdicts, with screenshots of anything wrong.
4. **Task 4**: the five homepage checks, with both screenshots.
5. **Anything you could not do, and why.** Do not paper over a blocked step.

Remember rule 6: no em dashes or en dashes in your report either.
