/**
 * Product detail — image well + buy column, sticky to the drop.
 */
function ProductDetail({ product, onBack, onAdd }) {
  const { Button, Badge, CircuitRule } = window.FBRIQDesignSystem_0e5da2;
  const p = product || { image: "../../assets/mockup-tee-model.png", meta: "TEE · 6.5 OZ", title: "Deploying Identity v2.0", price: "$35", badge: "New Drop", badgeTone: "new" };
  const [size, setSize] = React.useState("M");
  const sizes = ["XS", "S", "M", "L", "XL", "2XL", "3XL"];

  return (
    <section style={{ padding: "40px 56px 80px" }}>
      <button onClick={onBack} style={{ background: "none", border: "none", cursor: "pointer", fontFamily: "var(--font-mono)", fontSize: "11px", letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--text-muted)", marginBottom: "28px", padding: 0 }}>
        ← Back to catalog
      </button>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "48px", alignItems: "start" }}>
        {/* Image */}
        <div style={{ position: "relative", aspectRatio: "4/5", background: "var(--bg-sunken)", border: "1px solid var(--border-hairline)", overflow: "hidden" }}>
          <img src={p.image} alt={p.title} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
          {p.badge && <div style={{ position: "absolute", top: "16px", left: "16px" }}><Badge tone={p.badgeTone} dot={p.badgeTone === "new"}>{p.badge}</Badge></div>}
        </div>
        {/* Buy column */}
        <div style={{ display: "flex", flexDirection: "column", gap: "22px", paddingTop: "8px" }}>
          <span className="fae-overline">{p.meta}</span>
          <h1 style={{ fontFamily: "var(--font-display)", fontSize: "48px", lineHeight: 1.05, color: "var(--text-heading)", margin: 0 }}>{p.title}</h1>
          <CircuitRule width={220} />
          <div style={{ fontFamily: "var(--font-mono)", fontSize: "22px", color: "var(--text-body)" }}>{p.price}</div>
          <p style={{ fontFamily: "var(--font-body)", fontSize: "15px", lineHeight: 1.7, color: "var(--text-muted)", margin: 0, maxWidth: "46ch" }}>
            Premium heavyweight cotton, 6.5oz. Soft hand-feel, structured drape. Screen-quality DTG print that survives the laundromat in any timezone.
          </p>

          <div>
            <span className="fae-overline" style={{ display: "block", marginBottom: "10px" }}>Size</span>
            <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
              {sizes.map((s) => (
                <button
                  key={s}
                  onClick={() => setSize(s)}
                  style={{
                    width: "46px", height: "46px", cursor: "pointer",
                    background: size === s ? "var(--fae-silver)" : "transparent",
                    color: size === s ? "var(--fae-black)" : "var(--text-muted)",
                    border: `1px solid ${size === s ? "var(--fae-silver)" : "var(--border-strong)"}`,
                    fontFamily: "var(--font-mono)", fontSize: "12px",
                  }}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>

          <div style={{ display: "flex", gap: "12px", marginTop: "6px" }}>
            <Button variant="primary" size="lg" style={{ flex: 1 }} onClick={() => onAdd && onAdd(p)}>Add to cart — {p.price}</Button>
            <Button variant="secondary" size="lg">♥</Button>
          </div>
          <div style={{ fontFamily: "var(--font-mono)", fontSize: "11px", color: "var(--text-faint)", letterSpacing: "0.06em" }}>
            // free US &amp; Canada shipping over $80 · 30-day returns
          </div>
        </div>
      </div>
    </section>
  );
}
window.ProductDetail = ProductDetail;
