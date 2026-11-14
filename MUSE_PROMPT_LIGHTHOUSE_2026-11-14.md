You are editing the live Shopify theme for faebriq.com. Make exactly the 6 code changes below, then verify and report. Nothing else.

RULES
- Theme: "faebriqtheme-launch-fix" (role MAIN, theme ID 189810704451). Edit no other theme. Do not publish, duplicate or delete any theme.
- Change only the text shown. No other files, settings, products, prices, discounts, shipping or copy.
- Each "FIND" must match exactly once. If it doesn't, stop, change nothing in that file, and tell me what you found instead.
- If you can't edit theme code, say so and stop. Don't approximate.

CHANGE 1: layout/theme.liquid
FIND:
  {{ 'faebriq.css' | asset_url | stylesheet_tag }}
REPLACE WITH:
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@600&family=Archivo:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap">
  {{ 'faebriq.css' | asset_url | stylesheet_tag }}

CHANGE 2: assets/faebriq.css (line 5). Do this in the same session as change 1.
FIND:
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@600&family=Archivo:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
REPLACE WITH:
/* Google Fonts load from layout/theme.liquid <head> (preconnect + link), not @import: an @import waits for this file first. */

CHANGE 3: snippets/product-card.liquid
FIND:
        sizes="(min-width: 990px) 33vw, (min-width: 750px) 50vw, 100vw"
REPLACE WITH:
        sizes="(min-width: 769px) 33vw, (min-width: 481px) 50vw, 100vw"

CHANGE 4: snippets/product-card.liquid
FIND:
        {% if card_id <= 3 %}loading="eager" fetchpriority="high"{% else %}loading="lazy"{% endif %}
REPLACE WITH:
        {%- comment -%} FAEBRIQ 2026-11-14: on the homepage the hero image is the LCP; cards sit below it and must not compete for bandwidth. {%- endcomment -%}
        {% if card_id <= 3 and template.name != 'index' %}loading="eager" fetchpriority="high"{% else %}loading="lazy"{% endif %}

CHANGE 5: snippets/cart-drawer.liquid (line 2). Changes 5 and 6 go together, or the cart drawer stops opening.
FIND:
<div id="fae-cart-drawer" class="fae-cart-drawer" aria-hidden="true">
REPLACE WITH:
<div id="fae-cart-drawer" class="fae-cart-drawer" aria-hidden="true" inert>

CHANGE 6: assets/fae-cart.js
FIND:
  function openDrawer() {
    drawer.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }
  function closeDrawer() {
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }
REPLACE WITH:
  // Closed drawer is inert: hidden from screen readers AND unreachable by Tab.
  var lastFocus = null;
  function openDrawer() {
    lastFocus = document.activeElement;
    drawer.removeAttribute('inert');
    drawer.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    var closeBtn = drawer.querySelector('.fae-cart-drawer__close');
    if (closeBtn) closeBtn.focus();
  }
  function closeDrawer() {
    if (!drawer.classList.contains('is-open')) return;
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    drawer.setAttribute('inert', '');
    document.body.style.overflow = '';
    if (lastFocus && document.contains(lastFocus)) lastFocus.focus();
  }

VERIFY (after saving)
1. Homepage loads; fonts look unchanged.
2. Cart button opens the drawer; X and Escape close it; adding a product opens it with the item.
3. A collection page still shows product images.
If any check fails, restore that file's previous version from the code editor's "Older versions" and tell me.

CHECK ONLY, DO NOT CHANGE
The cart drawer tells sticker-only carts "You're $X away from FREE shipping" up to $50 USD. In Settings > Shipping and delivery, look at the "Stickers (SPOKE)" profile: does any rate make sticker orders of $50 or more ship free? Report yes or no and list the rates. Don't edit anything there.

REPORT
List each change as done or skipped (with reason), each verify step as pass or fail, and the shipping answer. No other commentary.
