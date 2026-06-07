import React from "react";

/**
 * FÆBRIQ Badge — small mono status/marker chip.
 * Tones: default, accent, new, sold, plus the six circuit colors via `tone`.
 */
export function Badge({ children, tone = "default", dot = false, style = {}, ...rest }) {
  const tones = {
    default: { color: "var(--text-muted)", border: "var(--border-strong)" },
    accent: { color: "var(--fae-accent)", border: "var(--fae-accent)" },
    new: { color: "var(--fae-circuit-green)", border: "var(--fae-circuit-green)" },
    sold: { color: "var(--fae-circuit-coral)", border: "var(--fae-circuit-coral)" },
    coral: { color: "var(--fae-circuit-coral)", border: "var(--fae-circuit-coral)" },
    amber: { color: "var(--fae-circuit-amber)", border: "var(--fae-circuit-amber)" },
    yellow: { color: "var(--fae-circuit-yellow)", border: "var(--fae-circuit-yellow)" },
    green: { color: "var(--fae-circuit-green)", border: "var(--fae-circuit-green)" },
    blue: { color: "var(--fae-circuit-blue)", border: "var(--fae-circuit-blue)" },
    purple: { color: "var(--fae-circuit-purple)", border: "var(--fae-circuit-purple)" },
  };
  const t = tones[tone] || tones.default;

  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "6px",
        fontFamily: "var(--font-mono)",
        fontSize: "10px",
        fontWeight: 500,
        letterSpacing: "0.14em",
        textTransform: "uppercase",
        lineHeight: 1,
        whiteSpace: "nowrap",
        padding: "5px 9px",
        color: t.color,
        border: `1px solid ${t.border}`,
        background: "transparent",
        borderRadius: "var(--radius-sm)",
        ...style,
      }}
      {...rest}
    >
      {dot && (
        <span
          style={{
            width: "5px",
            height: "5px",
            borderRadius: "50%",
            background: t.color,
            flex: "0 0 auto",
          }}
        />
      )}
      {children}
    </span>
  );
}
