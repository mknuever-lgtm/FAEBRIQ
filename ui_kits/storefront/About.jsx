import React from "react";
import { CircuitRule } from "../../components/core/CircuitRule/CircuitRule.jsx";
import { Badge } from "../../components/core/Badge/Badge.jsx";

/**
 * About section — editorial brand statement over the void, two columns.
 */
export function About() {
  return (
    <section style={{ padding: "80px 56px", borderTop: "1px solid var(--border-hairline)", background: "var(--bg-sunken)" }}>
      <div style={{ display: "grid", gridTemplateColumns: "0.8fr 1.2fr", gap: "64px", alignItems: "start", maxWidth: "1100px", margin: "0 auto" }}>
        <div>
          <span className="fae-overline" style={{ display: "block", marginBottom: "16px" }}>// about</span>
          <CircuitRule width={180} />
        </div>
        <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
          <h2 style={{ fontFamily: "var(--font-display)", fontSize: "44px", lineHeight: 1.08, color: "var(--text-heading)", margin: 0 }}>
            Merch for people who ship at 2am from a co-working space in Lisbon.
          </h2>
          <p style={{ fontFamily: "var(--font-body)", fontSize: "17px", lineHeight: 1.7, color: "var(--text-muted)", margin: 0, maxWidth: "58ch" }}>
            FÆBRIQ makes wearable statements for queer tech professionals and digital nomads — the ones who build their identity the same way they build software: iteratively, deliberately, and on their own terms.
          </p>
          <p style={{ fontFamily: "var(--font-body)", fontSize: "17px", lineHeight: 1.7, color: "var(--text-muted)", margin: 0, maxWidth: "58ch" }}>
            Dark editorial design. Premium heavyweight cotton. No hype, no neon, no cringe. Just a quiet message that the right people will read instantly.
          </p>
          <div style={{ display: "flex", gap: "10px", marginTop: "8px" }}>
            <Badge tone="green">Queer-owned</Badge>
            <Badge tone="blue">Print-on-demand</Badge>
            <Badge tone="amber">Ships US &amp; Canada</Badge>
          </div>
        </div>
      </div>
    </section>
  );
}
