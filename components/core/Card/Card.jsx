import React from "react";

/**
 * FÆBRIQ Card — flat editorial surface with a hairline border.
 * No rounding, no drop shadow. Optional circuit top-edge accent.
 */
export function Card({ children, accent = false, interactive = false, padding = "var(--space-5)", style = {}, ...rest }) {
  const [hover, setHover] = React.useState(false);

  return (
    <div
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        position: "relative",
        background: "var(--surface-card)",
        border: `1px solid ${hover && interactive ? "var(--border-strong)" : "var(--border-hairline)"}`,
        borderRadius: "var(--radius-sm)",
        padding,
        transition: "border-color var(--dur-base) var(--ease-standard)",
        cursor: interactive ? "pointer" : "default",
        ...style,
      }}
      {...rest}
    >
      {accent && (
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            height: "2px",
            background:
              "linear-gradient(90deg, var(--fae-circuit-coral), var(--fae-circuit-amber), var(--fae-circuit-yellow), var(--fae-circuit-green), var(--fae-circuit-blue), var(--fae-circuit-purple))",
          }}
        />
      )}
      {children}
    </div>
  );
}
