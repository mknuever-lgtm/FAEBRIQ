The storefront's core merch tile — image well over a display title and mono price row, used across collection grids.

```jsx
<ProductCard
  image="assets/mockup-tee-model.png"
  meta="TEE · 6.5 OZ"
  title="Deploying Identity v2.0"
  price="$35"
  badge="New Drop"
  badgeTone="new"
  onClick={openProduct}
/>
```

- Image sits in a 4:5 well at 92% opacity, lifts to full + slight zoom on hover.
- Border brightens and a mono "VIEW →" appears on hover.
- Title uses Instrument Serif; price + meta use mono. Composes `<Badge>`.
