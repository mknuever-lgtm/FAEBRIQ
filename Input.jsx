import React from "react";

/**
 * FÆBRIQ Input — sharp field with mono label and terminal-blue focus.
 */
export function Input({ label, hint, prefix = null, type = "text", invalid = false, id, style = {}, ...rest }) {
  const [focus, setFocus] = React.useState(false);
  const inputId = id || (label ? `fae-${label.toLowerCase().replace(/\s+/g, "-")}` : undefined);

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "8px", ...style }}>
      {label && (
        <label
          htmlFor={inputId}
          style={{
            fontFamily: "var(--font-mono)",
            fontSize: "10px",
            letterSpacing: "0.14em",
            textTransform: "uppercase",
            color: "var(--text-muted)",
          }}
        >
          {label}
        </label>
      )}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          background: "var(--bg-sunken)",
          border: `1px solid ${invalid ? "var(--fae-danger)" : focus ? "var(--fae-accent)" : "var(--border-hairline)"}`,
          borderRadius: "var(--radius-sm)",
          boxShadow: focus && !invalid ? "0 0 0 1px var(--fae-accent)" : "none",
          transition: "border-color var(--dur-fast) var(--ease-standard), box-shadow var(--dur-fast) var(--ease-standard)",
        }}
      >
        {prefix && (
          <span
            style={{
              fontFamily: "var(--font-mono)",
              fontSize: "13px",
              color: "var(--text-faint)",
              padding: "0 0 0 12px",
            }}
          >
            {prefix}
          </span>
        )}
        <input
          id={inputId}
          type={type}
          onFocus={() => setFocus(true)}
          onBlur={() => setFocus(false)}
          style={{
            flex: 1,
            background: "transparent",
            border: "none",
            outline: "none",
            color: "var(--text-body)",
            fontFamily: "var(--font-body)",
            fontSize: "14px",
            padding: "11px 12px",
            letterSpacing: "var(--ls-tight)",
          }}
          {...rest}
        />
      </div>
      {hint && (
        <span
          style={{
            fontFamily: "var(--font-mono)",
            fontSize: "10px",
            color: invalid ? "var(--fae-danger)" : "var(--text-faint)",
          }}
        >
          {hint}
        </span>
      )}
    </div>
  );
}
