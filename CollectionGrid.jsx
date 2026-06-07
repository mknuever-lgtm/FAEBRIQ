const PRODUCTS = [
  { id: "p1", image: "../../assets/mockup-tee-model.png", meta: "TEE · 6.5 OZ", title: "Deploying Identity v2.0", price: "$35", badge: "New Drop", badgeTone: "new" },
  { id: "p2", image: "../../assets/mockup-sleeve.png", meta: "SLEEVE · 13\"", title: "Carry Protocol", price: "$42", badge: "Limited", badgeTone: "purple" },
  { id: "p3", image: "../../assets/mockup-stickers.png", meta: "STICKER PACK · ×6", title: "Commit Messages", price: "$12", badge: null },
  { id: "p4", image: "../../assets/mockup-flatlay.png", meta: "TEE · 6.5 OZ", title: "Serve It Black", price: "$35", badge: null },
  { id: "p5", image: "../../assets/mockup-tee-flat.png", meta: "TEE · 6.5 OZ", title: "Rebrand In Progress", price: "$35", badge: "Sold Out", badgeTone: "sold" },
  { id: "p6", image: "../../assets/mockup-sleeve-desk.png", meta: "SLEEVE · 15\"", title: "Nomad Edition", price: "$46", badge: null },
];

/**
 * Collection grid — filter rail + 3-up product grid.
 */
function CollectionGrid({ onOpen }) {
  const { ProductCard, CircuitRule } = window.FBRIQDesignSystem_0e5da2;
  const [filter, setFilter] = React.useState("All");
  const filters = ["All", "Tees", "Sleeves", "Stickers"];

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
      <CircuitRule width="100%" nodes={false} style={{ margin: "0 0 32px" }} />
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "24px" }}>
        {PRODUCTS.map((p) => (
          <ProductCard key={p.id} {...p} onClick={() => onOpen && onOpen(p)} />
        ))}
      </div>
    </section>
  );
}
window.CollectionGrid = CollectionGrid;
