import React from "react";

const CIRCUIT = [
  "var(--fae-circuit-coral)",
  "var(--fae-circuit-amber)",
  "var(--fae-circuit-yellow)",
  "var(--fae-circuit-green)",
  "var(--fae-circuit-blue)",
  "var(--fae-circuit-purple)",
];

/**
 * FÆBRIQ CircuitRule — the signature divider.
 * Confirmed style (June 2026, Option 3): six equal segmented bands
 * in a single row. Renders faithfully at any size, including
 * embroidery and small print — unlike a smooth gradient trace.
 * Never substitute with a CSS gradient.
 */
export function CircuitRule({ gap = 4, height = 4, width = "100%", align = "left", style = {}, ...rest }) {
  return (
    <div
      role="separator"
      style={{
        display: "flex",
        gap: `${gap}px`,
        width,
        height: `${height}px`,
        marginLeft: align === "right" ? "auto" : 0,
        ...style,
      }}
      {...rest}
    >
      {CIRCUIT.map((c, i) => (
        <span key={i} style={{ flex: 1, background: c }} />
      ))}
    </div>
  );
}
