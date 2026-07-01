Storefront top navigation — silver wordmark left, mono nav center, cart right, optional announcement bar.

```jsx
<SiteHeader
  active="Shop"
  cartCount={2}
  announcement="Free worldwide shipping over $80 · Code it. Serve it."
  onNav={(t) => goto(t)}
/>
```

- Wordmark is Instrument Serif at +0.06em; nav links are mono uppercase.
- Active link gets a terminal-blue 1px underline.
- Cart count turns accent-blue when non-zero.
