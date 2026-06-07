import React from "react";

/**
 * FÆBRIQ Button — sharp, editorial, terminal-flavored.
 * Variants: primary (silver fill), accent (terminal blue), secondary (hairline), ghost (text).
 */
export function Button({
  children,
  variant = "primary",
  size = "md",
  disabled = false,
  iconLeft = null,
  iconRight = null,
  type = "button",
  onClick,
  style = {},
  ...rest
}) {
  const sizes = {
    sm: { padding: "7px 14px", fontSize: "11px" },
    md: { padding: "11px 22px", fontSize: "12px" },
    lg: { padding: "15px 30px", fontSize: "13px" },
  };

  const variants = {
    primary: {
      background: "var(--fae-silver)",
      color: "var(--fae-black)",
      border: "1px solid var(--fae-silver)",
    },
    accent: {
      background: "var(--fae-accent)",
      color: "var(--fae-black)",
      border: "1px solid var(--fae-accent)",
    },
    secondary: {
      background: "transparent",
      color: "var(--text-body)",
      border: "1px solid var(--border-strong)",
    },
    ghost: {
      background: "transparent",
      color: "var(--text-muted)",
      border: "1px solid transparent",
    },
  };

  const base = {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: "8px",
    fontFamily: "var(--font-mono)",
    fontWeight: 500,
    letterSpacing: "0.12em",
    textTransform: "uppercase",
    lineHeight: 1,
    borderRadius: "var(--radius-sm)",
    cursor: disabled ? "not-allowed" : "pointer",
    opacity: disabled ? 0.4 : 1,
    transition: "background var(--dur-fast) var(--ease-standard), color var(--dur-fast) var(--ease-standard), border-color var(--dur-fast) var(--ease-standard), transform var(--dur-fast) var(--ease-standard)",
    whiteSpace: "nowrap",
    ...sizes[size],
    ...variants[variant],
    ...style,
  };

  const hover = {
    primary: { background: "var(--fae-silver-hi)", borderColor: "var(--fae-silver-hi)" },
    accent: { background: "var(--fae-accent)", filter: "brightness(1.12)" },
    secondary: { borderColor: "var(--fae-silver-lo)", color: "var(--fae-silver-hi)" },
    ghost: { color: "var(--fae-silver-hi)" },
  };

  const onEnter = (e) => {
    if (disabled) return;
    Object.assign(e.currentTarget.style, hover[variant]);
  };
  const onLeave = (e) => {
    if (disabled) return;
    Object.assign(e.currentTarget.style, variants[variant], { filter: "none", transform: "none" });
  };
  const onDown = (e) => { if (!disabled) e.currentTarget.style.transform = "translateY(1px)"; };
  const onUp = (e) => { if (!disabled) e.currentTarget.style.transform = "none"; };

  return (
    <button
      type={type}
      disabled={disabled}
      onClick={onClick}
      style={base}
      onMouseEnter={onEnter}
      onMouseLeave={onLeave}
      onMouseDown={onDown}
      onMouseUp={onUp}
      {...rest}
    >
      {iconLeft}
      {children}
      {iconRight}
    </button>
  );
}
