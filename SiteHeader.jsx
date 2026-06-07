import React from "react";

/**
 * FÆBRIQ SiteHeader — storefront top nav.
 * Silver serif wordmark, mono nav links, cart count, circuit underline.
 */
export function SiteHeader({
  links = ["Shop", "Collections", "About", "Journal"],
  active = "Shop",
  cartCount = 0,
  onNav,
  announcement = null,
  style = {},
  ...rest
}) {
  return (
    <header style={{ position: "relative", background: "var(--bg-page)", ...style }} {...rest}>
      {announcement && (
        <div
          style={{
            borderBottom: "1px solid var(--border-hairline)",
            textAlign: "center",
            padding: "8px 16px",
            fontFamily: "var(--font-mono)",
            fontSize: "11px",
            letterSpacing: "0.1em",
            textTransform: "uppercase",
            color: "var(--text-muted)",
          }}
        >
          {announcement}
        </div>
      )}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          height: "var(--header-h)",
          padding: "0 var(--space-6)",
          borderBottom: "1px solid var(--border-hairline)",
        }}
      >
        <a
          href="#"
          onClick={(e) => { e.preventDefault(); onNav && onNav("home"); }}
          style={{
            fontFamily: "var(--font-display)",
            fontSize: "26px",
            letterSpacing: "0.06em",
            color: "var(--fae-silver)",
            lineHeight: 1,
          }}
        >
          FÆBRIQ
        </a>

        <nav style={{ display: "flex", gap: "var(--space-6)" }}>
          {links.map((l) => (
            <a
              key={l}
              href="#"
              onClick={(e) => { e.preventDefault(); onNav && onNav(l); }}
              style={{
                fontFamily: "var(--font-mono)",
                fontSize: "12px",
                letterSpacing: "0.1em",
                textTransform: "uppercase",
                color: active === l ? "var(--text-body)" : "var(--text-muted)",
                position: "relative",
                paddingBottom: "4px",
                transition: "color var(--dur-fast) var(--ease-standard)",
              }}
              onMouseEnter={(e) => (e.currentTarget.style.color = "var(--fae-silver-hi)")}
              onMouseLeave={(e) => (e.currentTarget.style.color = active === l ? "var(--text-body)" : "var(--text-muted)")}
            >
              {l}
              {active === l && (
                <span
                  style={{
                    position: "absolute",
                    left: 0,
                    right: 0,
                    bottom: 0,
                    height: "1px",
                    background: "var(--fae-accent)",
                  }}
                />
              )}
            </a>
          ))}
        </nav>

        <div style={{ display: "flex", alignItems: "center", gap: "var(--space-4)" }}>
          <a
            href="#"
            onClick={(e) => { e.preventDefault(); onNav && onNav("search"); }}
            style={{ fontFamily: "var(--font-mono)", fontSize: "12px", letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--text-muted)" }}
          >
            Search
          </a>
          <a
            href="#"
            onClick={(e) => { e.preventDefault(); onNav && onNav("cart"); }}
            style={{ fontFamily: "var(--font-mono)", fontSize: "12px", letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--text-body)", display: "inline-flex", gap: "6px" }}
          >
            Cart
            <span style={{ color: cartCount ? "var(--fae-accent)" : "var(--text-faint)" }}>[{cartCount}]</span>
          </a>
        </div>
      </div>
    </header>
  );
}
