/* ============================================================
   FÆBRIQ — cart drawer + AJAX cart (Shopify AJAX Cart API)
   No dependencies. Progressive enhancement over /cart.liquid.
   ============================================================ */
(function () {
  var drawer   = document.getElementById('fae-cart-drawer');
  var body     = document.getElementById('fae-cart-drawer-body');
  var countEls = [document.getElementById('fae-cart-count'), document.getElementById('fae-cart-drawer-count')];
  var subtotal = document.getElementById('fae-cart-drawer-subtotal');
  if (!drawer) return;

  function money(cents) {
    return (window.Shopify && Shopify.formatMoney)
      ? Shopify.formatMoney(cents, window.fae_money_format || '${{amount}}')
      : '$' + (cents / 100).toFixed(2);
  }

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

  function renderCart(cart) {
    countEls.forEach(function (el) {
      if (!el) return;
      el.textContent = cart.item_count > 0 ? '(' + cart.item_count + ')' : '';
    });
    if (subtotal) subtotal.textContent = money(cart.total_price);

    if (!cart.items.length) {
      body.innerHTML = '<p class="fae-cart-drawer__empty">Cart is empty.</p>';
      return;
    }

    body.innerHTML = cart.items.map(function (item) {
      var variantLine = (item.variant_title && item.variant_title !== 'Default Title')
        ? '<p class="fae-cart-drawer__item-variant">' + item.variant_title + '</p>' : '';
      return (
        '<div class="fae-cart-drawer__item" data-key="' + item.key + '">' +
          '<a href="' + item.url + '"><img src="' + (item.image || '') + '&width=160" alt="' + item.title.replace(/"/g, '&quot;') + '"></a>' +
          '<div>' +
            '<a href="' + item.url + '" class="fae-cart-drawer__item-title" style="text-decoration:none;">' + item.product_title + '</a>' +
            variantLine +
            '<div class="fae-cart-drawer__item-qty">' +
              '<button type="button" class="fae-cart-drawer__qty-btn" data-qty-change="-1" data-key="' + item.key + '">&minus;</button>' +
              '<span>' + item.quantity + '</span>' +
              '<button type="button" class="fae-cart-drawer__qty-btn" data-qty-change="1" data-key="' + item.key + '">+</button>' +
            '</div>' +
            '<button type="button" class="fae-cart-drawer__item-remove" data-qty-set="0" data-key="' + item.key + '">Remove</button>' +
          '</div>' +
          '<div class="fae-cart-drawer__item-price">' + money(item.final_line_price) + '</div>' +
        '</div>'
      );
    }).join('');
  }

  function fetchCart() {
    fetch('/cart.js').then(function (r) { return r.json(); }).then(renderCart);
  }

  function changeQty(key, quantity) {
    fetch('/cart/change.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: key, quantity: quantity })
    }).then(function (r) { return r.json(); }).then(renderCart);
  }

  // Open/close
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-cart-toggle]')) {
      e.preventDefault();
      openDrawer();
      fetchCart();
    } else if (e.target.closest('[data-cart-close]')) {
      closeDrawer();
    } else if (e.target.closest('[data-qty-change]')) {
      var btn = e.target.closest('[data-qty-change]');
      var row = btn.closest('.fae-cart-drawer__item');
      var current = parseInt(row.querySelector('span').textContent, 10) || 0;
      var delta = parseInt(btn.dataset.qtyChange, 10);
      changeQty(btn.dataset.key, Math.max(0, current + delta));
    } else if (e.target.closest('[data-qty-set]')) {
      var rbtn = e.target.closest('[data-qty-set]');
      changeQty(rbtn.dataset.key, parseInt(rbtn.dataset.qtySet, 10));
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeDrawer();
  });

  // Intercept product-form submits -> AJAX add, then open drawer
  document.addEventListener('submit', function (e) {
    var form = e.target.closest('#fae-product-form');
    if (!form) return;
    e.preventDefault();
    var formData = new FormData(form);
    fetch('/cart/add.js', { method: 'POST', body: formData })
      .then(function (r) { return r.json(); })
      .then(function () {
        fetchCart();
        openDrawer();
      })
      .catch(function () { form.submit(); }); // graceful fallback
  });

  // Initial count sync on load
  fetchCart();
})();
