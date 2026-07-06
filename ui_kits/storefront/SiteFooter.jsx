import React from "react";
import { Input } from "../../components/core/Input/Input.jsx";
import { Button } from "../../components/core/Button/Button.jsx";
import { CircuitRule } from "../../components/core/CircuitRule/CircuitRule.jsx";

/**
 * Storefront footer — wordmark, link columns, newsletter, circuit cap.
 */
export function SiteFooter() {
  const cols = [
    { h: "Shop", items: ["Tees", "Hoodies", "Stickers", "Accessories"] },
    { h: "Brand", items: ["About", "Journal", "Sustainability", "Sizing"] },
    { h: "Support", items: ["Shipping", "Returns", "Contact", "FAQ"] },
  ];
  return (
    <footer style={{ borderTop: "1px solid var(--border-hairline)", padding: "56px 56px 32px" }}>
      <CircuitRule width="100%" style={{ marginBottom: "40px" }} />
      <div style={{ display: "grid", gridTemplateColumns: "1.4fr 1fr 1fr 1fr 1.4fr", gap: "40px" }}>
        <div>
          <div style={{ fontFamily: "var(--font-display)", fontSize: "30px", letterSpacing: "0.06em", color: "var(--fae-silver)", marginBottom: "12px" }}>FÆBRIQ</div>
          <div style={{ fontFamily: "var(--font-display)", fontStyle: "italic", fontSize: "16px", color: "var(--text-muted)" }}>Code it. Serve it.</div>
        </div>
        {cols.map((c) => (
          <div key={c.h}>
            <div className="fae-overline" style={{ marginBottom: "16px" }}>{c.h}</div>
            <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
              {c.items.map((i) => (
                <a key={i} href="#" style={{ fontFamily: "var(--font-body)", fontSize: "14px", color: "var(--text-muted)" }}>{i}</a>
              ))}
            </div>
          </div>
        ))}
        <div>
          <div className="fae-overline" style={{ marginBottom: "16px" }}>The dispatch</div>
          <p style={{ fontFamily: "var(--font-body)", fontSize: "13px", color: "var(--text-faint)", margin: "0 0 14px", lineHeight: 1.5 }}>Drop alerts. No spam. Unsubscribe anytime.</p>
          <div style={{ display: "flex", gap: "8px" }}>
            <Input placeholder="you@domain.dev" style={{ flex: 1 }} />
            <Button variant="accent">Join</Button>
          </div>
        </div>
      </div>
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: "48px", paddingTop: "20px", borderTop: "1px solid var(--border-hairline)" }}>
        <span style={{ fontFamily: "var(--font-mono)", fontSize: "10px", letterSpacing: "0.1em", color: "var(--text-faint)" }}>© 2026 FÆBRIQ · QUEER-OWNED · PRINTED ON DEMAND</span>
        <span style={{ fontFamily: "var(--font-mono)", fontSize: "10px", letterSpacing: "0.1em", color: "var(--text-faint)" }}>BUILT FOR THE NOMADS</span>
      </div>
    </footer>
  );
}
