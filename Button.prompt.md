Sharp, mono-labelled button — use for every call to action, from "Add to cart" to nav actions.

```jsx
<Button variant="primary" onClick={checkout}>Add to cart — $35</Button>
<Button variant="accent" size="lg">Deploy</Button>
<Button variant="secondary">View collection</Button>
<Button variant="ghost" size="sm">Size guide</Button>
```

- **primary** = silver fill on black (default, highest emphasis).
- **accent** = terminal blue, reserve for the single most important action on a view.
- **secondary** = hairline outline, the workhorse.
- **ghost** = text only, for low-emphasis / tertiary actions.
- Labels are auto-uppercased and mono-tracked — write them in normal case.
- Supports `iconLeft` / `iconRight`, `size` (sm/md/lg), and `disabled`.
