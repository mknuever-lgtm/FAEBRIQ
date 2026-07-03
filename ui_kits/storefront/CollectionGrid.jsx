import React from "react";
import { ProductCard } from "../../components/storefront/ProductCard/ProductCard.jsx";
import { CircuitRule } from "../../components/core/CircuitRule/CircuitRule.jsx";

const PRODUCTS = [
  { id: "p1", image: "/model-tee-new.png", meta: "HOODIE", title: "Deploying Identity v2.0", price: "CA$78", badge: "New Drop", badgeTone: "new" },
  { id: "p2", image: "/model-hoodie-new.png", meta: "TEE", title: "Code It, Serve It.", price: "CA$42", badge: null },
  { id: "p3", image: "/model-cap-new.png", meta: "CAP", title: "Circuit Cap", price: "CA$34", badge: null },
];

/** Collection overview tile — not a priced product, links out to the full catalog. */
const COLLECTION_TILE = { image: "/model-flatlay-new.png", label: "Shop the full collection" };

/**
 * Collection grid — filter rail + product grid.
 */
export function CollectionGrid({ onOpen }) {
  const [filter, setFilter] = React.useState("All");
  const filters = ["All", "Tees", "Hoodies", "Accessories"];

  return (
    <section style={{ padding: "64px 56px" }}>
      <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", marginBottom: "12px" }}>
        <div>
          <span className="fae-overline" style={{ display: "block", marginBottom: "12px" }}>The Catalog</span>
          <h2 style={{ fontFamily: "var(--font-display)", fontSize: "40px", color: "var(--text-heading)", margin: 0 }}>Everything in the drop</h2>
        </div>
        <div style={{ display: "flex", gap: "20px" }}>
          {filters.map((f) => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              style={{
                background: "none", border: "none", cursor: "pointer", padding: "0 0 4px",
                fontFamily: "var(--font-mono)", fontSize: "12px", letterSpacing: "0.1em", textTransform: "uppercase",
                color: filter === f ? "var(--text-body)" : "var(--text-faint)",
                borderBottom: filter === f ? "1px solid var(--fae-accent)" : "1px solid transparent",
              }}
            >
              {f}
            </button>
          ))}
        </div>
      </div>
      <CircuitRule width="100%" style={{ margin: "0 0 32px" }} />
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "24px" }}>
        {PRODUCTS.map((p) => (
          <ProductCard key={p.id} {...p} onClick={() => onOpen && onOpen(p)} />
        ))}
        <div
          style={{
            position: "relative",
            aspectRatio: "4 / 5",
            overflow: "hidden",
            border: "1px solid var(--border-hairline)",
            cursor: "pointer",
          }}
        >
          <img
            src={COLLECTION_TILE.image}
            alt={COLLECTION_TILE.label}
            style={{ width: "100%", height: "100%", objectFit: "cover", opacity: 0.85 }}
          />
          <div
            style={{
              position: "absolute",
              inset: 0,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              background: "rgba(13,13,13,0.55)",
            }}
          >
            <span
              style={{
                fontFamily: "var(--font-mono)",
                fontSize: "12px",
                letterSpacing: "0.14em",
                textTransform: "uppercase",
                color: "var(--fae-silver-hi)",
                border: "1px solid var(--fae-silver)",
                padding: "10px 18px",
              }}
            >
              {COLLECTION_TILE.label} →
            </span>
          </div>
        </div>
      </div>
    </section>
  );
}
