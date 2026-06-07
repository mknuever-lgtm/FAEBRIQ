Outlined mono chip for status and markers — "New Drop", "Sold Out", "Collection 02".

```jsx
<Badge tone="new" dot>New Drop</Badge>
<Badge tone="sold">Sold Out</Badge>
<Badge>6.5 oz</Badge>
```

- Always outlined, never filled — keeps the surface flat.
- `tone` accepts semantic names (default/accent/new/sold) or any of the six circuit colors.
- `dot` adds a small status indicator. Keep labels to 1–3 words.
