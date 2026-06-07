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
 * Six rainbow hairlines stacked with optional hollow terminal nodes.
 * The brand's load-bearing graphic device.
 */
export function CircuitRule({ nodes = true, gap = 5, width = "100%", align = "left", style = {}, ...rest }) {
  const lines = CIRCUIT.length;
  const height = (lines - 1) * gap + (nodes ? 6 : 1);

  return (
    <div
      style={{
        position: "relative",
        width,
        height: `${height}px`,
        marginLeft: align === "right" ? "auto" : 0,
        ...style,
      }}
      {...rest}
    >
      {CIRCUIT.map((c, i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            top: `${i * gap + (nodes ? 3 : 0)}px`,
            left: nodes ? "6px" : 0,
            right: 0,
            height: "1px",
            background: c,
          }}
        />
      ))}
      {nodes &&
        CIRCUIT.map((c, i) => (
          <span
            key={`n${i}`}
            style={{
              position: "absolute",
              top: `${i * gap}px`,
              left: 0,
              width: "5px",
              height: "5px",
              borderRadius: "50%",
              border: `1px solid ${c}`,
              background: "var(--bg-page)",
            }}
          />
        ))}
    </div>
  );
}
