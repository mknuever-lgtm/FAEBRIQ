import React from "react";
import { Badge } from "../../core/Badge/Badge.jsx";

/**
 * FÆBRIQ ProductCard — storefront merch tile.
 * Flat image well, mono SKU/price row, hairline border that lifts on hover.
 */
export function ProductCard({
  image,
  title,
  price,
  meta,
  badge = null,
  badgeTone = "new",
  onClick,
  style = {},
  ...rest
}) {
  const [hover, setHover] = React.useState(false);

  return (
    <div
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      onClick={onClick}
      style={{
        display: "flex",
        flexDirection: "column",
        background: "var(--surface-card)",
        border: `1px solid ${hover ? "var(--border-strong)" : "var(--border-hairline)"}`,
        cursor: onClick ? "pointer" : "default",
        transition: "border-color var(--dur-base) var(--ease-standard)",
        ...style,
      }}
      {...rest}
    >
      <div
        style={{
          position: "relative",
          aspectRatio: "4 / 5",
          overflow: "hidden",
          background: "var(--bg-sunken)",
          borderBottom: "1px solid var(--border-hairline)",
        }}
      >
        {image && (
          <img
            src={image}
            alt={title}
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              display: "block",
              transition: "transform var(--dur-slow) var(--ease-out), opacity var(--dur-base) var(--ease-standard)",
              transform: hover ? "scale(1.03)" : "scale(1)",
              opacity: hover ? 1 : 0.92,
            }}
          />
        )}
        {badge && (
          <div style={{ position: "absolute", top: "12px", left: "12px" }}>
            <Badge tone={badgeTone} dot={badgeTone === "new"}>{badge}</Badge>
          </div>
        )}
      </div>

      <div style={{ padding: "16px 16px 18px", display: "flex", flexDirection: "column", gap: "10px" }}>
        {meta && (
          <span
            style={{
              fontFamily: "var(--font-mono)",
              fontSize: "10px",
              letterSpacing: "0.14em",
              textTransform: "uppercase",
              color: "var(--text-faint)",
            }}
          >
            {meta}
          </span>
        )}
        <h3
          style={{
            fontFamily: "var(--font-display)",
            fontSize: "22px",
            lineHeight: 1.1,
            color: "var(--text-heading)",
            letterSpacing: "var(--ls-tight)",
            margin: 0,
          }}
        >
          {title}
        </h3>
        <div
          style={{
            display: "flex",
            alignItems: "baseline",
            justifyContent: "space-between",
            marginTop: "2px",
          }}
        >
          <span
            style={{
              fontFamily: "var(--font-mono)",
              fontSize: "14px",
              color: hover ? "var(--fae-accent)" : "var(--text-body)",
              transition: "color var(--dur-base) var(--ease-standard)",
            }}
          >
            {price}
          </span>
          <span
            style={{
              fontFamily: "var(--font-mono)",
              fontSize: "11px",
              letterSpacing: "0.1em",
              color: "var(--text-faint)",
              opacity: hover ? 1 : 0,
              transition: "opacity var(--dur-base) var(--ease-standard)",
            }}
          >
            VIEW →
          </span>
        </div>
      </div>
    </div>
  );
}
