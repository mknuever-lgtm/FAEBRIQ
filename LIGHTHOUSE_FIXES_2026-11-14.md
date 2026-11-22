# Lighthouse fixes, 2026/11/14

Apply in Shopify admin: Online Store > Themes > faebriqtheme-launch-fix (Current theme) > ... > Edit code.
Every "Find" block below was checked against the live theme on 2026/11/14. Edits go public on Save.
Do them in this order (fonts first, since edits 1 and 2 belong together).

---

## Edit 1 of 5: `layout/theme.liquid` (load fonts early)

Find:

```
  {{ 'faebriq.css' | asset_url | stylesheet_tag }}
```

Replace with:

```
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@600&family=Archivo:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap">
  {{ 'faebriq.css' | asset_url | stylesheet_tag }}
```

Save.

## Edit 2 of 5: `assets/faebriq.css` (remove the slow font import)

Find (line 5):

```
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@600&family=Archivo:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
```

Replace with:

```
/* Google Fonts load from layout/theme.liquid <head> (preconnect + link), not @import: an @import waits for this file first. */
```

Save.

## Edit 3 of 5: `snippets/product-card.liquid` (stop cards competing with the hero image)

Find:

```
        sizes="(min-width: 990px) 33vw, (min-width: 750px) 50vw, 100vw"
```

Replace with:

```
        sizes="(min-width: 769px) 33vw, (min-width: 481px) 50vw, 100vw"
```

Then find:

```
        {% if card_id <= 3 %}loading="eager" fetchpriority="high"{% else %}loading="lazy"{% endif %}
```

Replace with:

```
        {%- comment -%} FAEBRIQ 2026-11-14: on the homepage the hero image is the LCP; cards sit below it and must not compete for bandwidth. {%- endcomment -%}
        {% if card_id <= 3 and template.name != 'index' %}loading="eager" fetchpriority="high"{% else %}loading="lazy"{% endif %}
```

Save.

## Edit 4 of 5: `snippets/cart-drawer.liquid` (closed drawer can't be tabbed into)

Find (line 2):

```
<div id="fae-cart-drawer" class="fae-cart-drawer" aria-hidden="true">
```

Replace with:

```
<div id="fae-cart-drawer" class="fae-cart-drawer" aria-hidden="true" inert>
```

Save. Do edit 5 straight after, or the cart drawer won't open.

## Edit 5 of 5: `assets/fae-cart.js` (open/close toggles inert and focus)

Find:

```
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
```

Replace with:

```
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
```

Save.

---

## Check after saving (2 minutes, phone is fine)

1. Homepage loads, fonts look the same as before.
2. Tap Cart: drawer opens. Tap X: it closes. Add a product: drawer opens with it.
3. Collection page: product images still show.

## Undo

Each file in the code editor has "Older versions" at the top: pick the version before today's save.
