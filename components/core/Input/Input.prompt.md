Sharp text field — mono uppercase label, sunken well, terminal-blue focus ring.

```jsx
<Input label="Email" type="email" placeholder="you@domain.dev" />
<Input label="Discount" prefix="$" hint="Optional" />
<Input label="Handle" invalid hint="Already taken" />
```

- Label is mono-tracked uppercase; write it in normal case.
- Focus glows terminal blue; `invalid` switches the border/hint to coral.
- Use `prefix` for currency or @ handles.
