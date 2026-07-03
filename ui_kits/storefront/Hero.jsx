import React from "react";
import { Button } from "../../components/core/Button/Button.jsx";
import { CircuitRule } from "../../components/core/CircuitRule/CircuitRule.jsx";
import { Badge } from "../../components/core/Badge/Badge.jsx";

/**
 * Storefront hero — full-bleed flagship statement over the void.
 * Wordmark-scale serif headline, circuit rule, mono CTA row.
 */
export function Hero({ onShop }) {
  return (
    <section style={{ position: "relative", borderBottom: "1px solid var(--border-hairline)" }}>
      <div style={{ display: "grid", gridTemplateColumns: "1.1fr 0.9fr", minHeight: "560px" }}>
        {/* Left — statement */}
        <div style={{ display: "flex", flexDirection: "column", justifyContent: "center", padding: "64px 56px", gap: "28px" }}>
          <Badge tone="new" dot>New Drop · Vol. 1</Badge>
          <h1 style={{ fontFamily: "var(--font-display)", fontSize: "68px", lineHeight: 1.02, letterSpacing: "-0.01em", color: "var(--text-heading)", margin: 0, maxWidth: "12ch" }}>
            Please hold,<br />I'm rebranding<br /><span style={{ color: "var(--fae-silver)" }}>my identity.</span>
          </h1>
          <CircuitRule width={300} />
          <p style={{ fontFamily: "var(--font-body)", fontSize: "17px", color: "var(--text-muted)", maxWidth: "44ch", lineHeight: 1.6, margin: 0 }}>
            Engineered for the modern tech-nomad. High-contrast aesthetics, a quiet message. Code it. Serve it.
          </p>
          <div style={{ display: "flex", gap: "14px", marginTop: "4px" }}>
            <Button variant="primary" size="lg" onClick={onShop}>Shop the drop</Button>
            <Button variant="ghost" size="lg">The flagship →</Button>
          </div>
        </div>
        {/* Right — image well */}
        <div style={{ position: "relative", background: "var(--bg-sunken)", borderLeft: "1px solid var(--border-hairline)", overflow: "hidden" }}>
          <img src="/model-hoodie-new.png" alt="FÆBRIQ Code It, Serve It. tee on model" style={{ width: "100%", height: "100%", objectFit: "cover", opacity: 0.96 }} />
          <div style={{ position: "absolute", bottom: "20px", left: "20px", fontFamily: "var(--font-mono)", fontSize: "10px", letterSpacing: "0.14em", textTransform: "uppercase", color: "var(--text-faint)" }}>
            FAE-TEE-001 · Premium cotton · S–XL
          </div>
        </div>
      </div>
    </section>
  );
}
