/* @ds-bundle: {"format":3,"namespace":"FBRIQDesignSystem_0e5da2","components":[{"name":"Badge","sourcePath":"components/core/Badge.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Card","sourcePath":"components/core/Card.jsx"},{"name":"CircuitRule","sourcePath":"components/core/CircuitRule.jsx"},{"name":"Input","sourcePath":"components/core/Input.jsx"},{"name":"ProductCard","sourcePath":"components/storefront/ProductCard.jsx"},{"name":"SiteHeader","sourcePath":"components/storefront/SiteHeader.jsx"}],"sourceHashes":{"components/core/Badge.jsx":"611d20d07f12","components/core/Button.jsx":"299357e98b38","components/core/Card.jsx":"aef5b741760c","components/core/CircuitRule.jsx":"7a67a359ee58","components/core/Input.jsx":"3ae3e83a64d6","components/storefront/ProductCard.jsx":"4f1061f20c1f","components/storefront/SiteHeader.jsx":"1e25ded8af4f","ui_kits/storefront/About.jsx":"726f45c20f02","ui_kits/storefront/CollectionGrid.jsx":"f083bec11956","ui_kits/storefront/Hero.jsx":"38513b823eef","ui_kits/storefront/ProductDetail.jsx":"92b1c1b7cdf4","ui_kits/storefront/SiteFooter.jsx":"7e1e86b8035e"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.FBRIQDesignSystem_0e5da2 = window.FBRIQDesignSystem_0e5da2 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/core/Badge.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * FÆBRIQ Badge — small mono status/marker chip.
 * Tones: default, accent, new, sold, plus the six circuit colors via `tone`.
 */
function Badge({
  children,
  tone = "default",
  dot = false,
  style = {},
  ...rest
}) {
  const tones = {
    default: {
      color: "var(--text-muted)",
      border: "var(--border-strong)"
    },
    accent: {
      color: "var(--fae-accent)",
      border: "var(--fae-accent)"
    },
    new: {
      color: "var(--fae-circuit-green)",
      border: "var(--fae-circuit-green)"
    },
    sold: {
      color: "var(--fae-circuit-coral)",
      border: "var(--fae-circuit-coral)"
    },
    coral: {
      color: "var(--fae-circuit-coral)",
      border: "var(--fae-circuit-coral)"
    },
    amber: {
      color: "var(--fae-circuit-amber)",
      border: "var(--fae-circuit-amber)"
    },
    yellow: {
      color: "var(--fae-circuit-yellow)",
      border: "var(--fae-circuit-yellow)"
    },
    green: {
      color: "var(--fae-circuit-green)",
      border: "var(--fae-circuit-green)"
    },
    blue: {
      color: "var(--fae-circuit-blue)",
      border: "var(--fae-circuit-blue)"
    },
    purple: {
      color: "var(--fae-circuit-purple)",
      border: "var(--fae-circuit-purple)"
    }
  };
  const t = tones[tone] || tones.default;
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
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
      ...style
    }
  }, rest), dot && /*#__PURE__*/React.createElement("span", {
    style: {
      width: "5px",
      height: "5px",
      borderRadius: "50%",
      background: t.color,
      flex: "0 0 auto"
    }
  }), children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Badge.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * FÆBRIQ Button — sharp, editorial, terminal-flavored.
 * Variants: primary (silver fill), accent (terminal blue), secondary (hairline), ghost (text).
 */
function Button({
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
    sm: {
      padding: "7px 14px",
      fontSize: "11px"
    },
    md: {
      padding: "11px 22px",
      fontSize: "12px"
    },
    lg: {
      padding: "15px 30px",
      fontSize: "13px"
    }
  };
  const variants = {
    primary: {
      background: "var(--fae-silver)",
      color: "var(--fae-black)",
      border: "1px solid var(--fae-silver)"
    },
    accent: {
      background: "var(--fae-accent)",
      color: "var(--fae-black)",
      border: "1px solid var(--fae-accent)"
    },
    secondary: {
      background: "transparent",
      color: "var(--text-body)",
      border: "1px solid var(--border-strong)"
    },
    ghost: {
      background: "transparent",
      color: "var(--text-muted)",
      border: "1px solid transparent"
    }
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
    ...style
  };
  const hover = {
    primary: {
      background: "var(--fae-silver-hi)",
      borderColor: "var(--fae-silver-hi)"
    },
    accent: {
      background: "var(--fae-accent)",
      filter: "brightness(1.12)"
    },
    secondary: {
      borderColor: "var(--fae-silver-lo)",
      color: "var(--fae-silver-hi)"
    },
    ghost: {
      color: "var(--fae-silver-hi)"
    }
  };
  const onEnter = e => {
    if (disabled) return;
    Object.assign(e.currentTarget.style, hover[variant]);
  };
  const onLeave = e => {
    if (disabled) return;
    Object.assign(e.currentTarget.style, variants[variant], {
      filter: "none",
      transform: "none"
    });
  };
  const onDown = e => {
    if (!disabled) e.currentTarget.style.transform = "translateY(1px)";
  };
  const onUp = e => {
    if (!disabled) e.currentTarget.style.transform = "none";
  };
  return /*#__PURE__*/React.createElement("button", _extends({
    type: type,
    disabled: disabled,
    onClick: onClick,
    style: base,
    onMouseEnter: onEnter,
    onMouseLeave: onLeave,
    onMouseDown: onDown,
    onMouseUp: onUp
  }, rest), iconLeft, children, iconRight);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Card.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * FÆBRIQ Card — flat editorial surface with a hairline border.
 * No rounding, no drop shadow. Optional circuit top-edge accent.
 */
function Card({
  children,
  accent = false,
  interactive = false,
  padding = "var(--space-5)",
  style = {},
  ...rest
}) {
  const [hover, setHover] = React.useState(false);
  return /*#__PURE__*/React.createElement("div", _extends({
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      position: "relative",
      background: "var(--surface-card)",
      border: `1px solid ${hover && interactive ? "var(--border-strong)" : "var(--border-hairline)"}`,
      borderRadius: "var(--radius-sm)",
      padding,
      transition: "border-color var(--dur-base) var(--ease-standard)",
      cursor: interactive ? "pointer" : "default",
      ...style
    }
  }, rest), accent && /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      top: 0,
      left: 0,
      right: 0,
      height: "2px",
      background: "linear-gradient(90deg, var(--fae-circuit-coral), var(--fae-circuit-amber), var(--fae-circuit-yellow), var(--fae-circuit-green), var(--fae-circuit-blue), var(--fae-circuit-purple))"
    }
  }), children);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Card.jsx", error: String((e && e.message) || e) }); }

// components/core/CircuitRule.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const CIRCUIT = ["var(--fae-circuit-coral)", "var(--fae-circuit-amber)", "var(--fae-circuit-yellow)", "var(--fae-circuit-green)", "var(--fae-circuit-blue)", "var(--fae-circuit-purple)"];

/**
 * FÆBRIQ CircuitRule — the signature divider.
 * Six rainbow hairlines stacked with optional hollow terminal nodes.
 * The brand's load-bearing graphic device.
 */
function CircuitRule({
  nodes = true,
  gap = 5,
  width = "100%",
  align = "left",
  style = {},
  ...rest
}) {
  const lines = CIRCUIT.length;
  const height = (lines - 1) * gap + (nodes ? 6 : 1);
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      position: "relative",
      width,
      height: `${height}px`,
      marginLeft: align === "right" ? "auto" : 0,
      ...style
    }
  }, rest), CIRCUIT.map((c, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    style: {
      position: "absolute",
      top: `${i * gap + (nodes ? 3 : 0)}px`,
      left: nodes ? "6px" : 0,
      right: 0,
      height: "1px",
      background: c
    }
  })), nodes && CIRCUIT.map((c, i) => /*#__PURE__*/React.createElement("span", {
    key: `n${i}`,
    style: {
      position: "absolute",
      top: `${i * gap}px`,
      left: 0,
      width: "5px",
      height: "5px",
      borderRadius: "50%",
      border: `1px solid ${c}`,
      background: "var(--bg-page)"
    }
  })));
}
Object.assign(__ds_scope, { CircuitRule });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/CircuitRule.jsx", error: String((e && e.message) || e) }); }

// components/core/Input.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * FÆBRIQ Input — sharp field with mono label and terminal-blue focus.
 */
function Input({
  label,
  hint,
  prefix = null,
  type = "text",
  invalid = false,
  id,
  style = {},
  ...rest
}) {
  const [focus, setFocus] = React.useState(false);
  const inputId = id || (label ? `fae-${label.toLowerCase().replace(/\s+/g, "-")}` : undefined);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "8px",
      ...style
    }
  }, label && /*#__PURE__*/React.createElement("label", {
    htmlFor: inputId,
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "10px",
      letterSpacing: "0.14em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, label), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      background: "var(--bg-sunken)",
      border: `1px solid ${invalid ? "var(--fae-danger)" : focus ? "var(--fae-accent)" : "var(--border-hairline)"}`,
      borderRadius: "var(--radius-sm)",
      boxShadow: focus && !invalid ? "0 0 0 1px var(--fae-accent)" : "none",
      transition: "border-color var(--dur-fast) var(--ease-standard), box-shadow var(--dur-fast) var(--ease-standard)"
    }
  }, prefix && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "13px",
      color: "var(--text-faint)",
      padding: "0 0 0 12px"
    }
  }, prefix), /*#__PURE__*/React.createElement("input", _extends({
    id: inputId,
    type: type,
    onFocus: () => setFocus(true),
    onBlur: () => setFocus(false),
    style: {
      flex: 1,
      background: "transparent",
      border: "none",
      outline: "none",
      color: "var(--text-body)",
      fontFamily: "var(--font-body)",
      fontSize: "14px",
      padding: "11px 12px",
      letterSpacing: "var(--ls-tight)"
    }
  }, rest))), hint && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "10px",
      color: invalid ? "var(--fae-danger)" : "var(--text-faint)"
    }
  }, hint));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Input.jsx", error: String((e && e.message) || e) }); }

// components/storefront/ProductCard.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * FÆBRIQ ProductCard — storefront merch tile.
 * Flat image well, mono SKU/price row, hairline border that lifts on hover.
 */
function ProductCard({
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
  return /*#__PURE__*/React.createElement("div", _extends({
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    onClick: onClick,
    style: {
      display: "flex",
      flexDirection: "column",
      background: "var(--surface-card)",
      border: `1px solid ${hover ? "var(--border-strong)" : "var(--border-hairline)"}`,
      cursor: onClick ? "pointer" : "default",
      transition: "border-color var(--dur-base) var(--ease-standard)",
      ...style
    }
  }, rest), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "4 / 5",
      overflow: "hidden",
      background: "var(--bg-sunken)",
      borderBottom: "1px solid var(--border-hairline)"
    }
  }, image && /*#__PURE__*/React.createElement("img", {
    src: image,
    alt: title,
    style: {
      width: "100%",
      height: "100%",
      objectFit: "cover",
      display: "block",
      transition: "transform var(--dur-slow) var(--ease-out), opacity var(--dur-base) var(--ease-standard)",
      transform: hover ? "scale(1.03)" : "scale(1)",
      opacity: hover ? 1 : 0.92
    }
  }), badge && /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      top: "12px",
      left: "12px"
    }
  }, /*#__PURE__*/React.createElement(__ds_scope.Badge, {
    tone: badgeTone,
    dot: badgeTone === "new"
  }, badge))), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: "16px 16px 18px",
      display: "flex",
      flexDirection: "column",
      gap: "10px"
    }
  }, meta && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "10px",
      letterSpacing: "0.14em",
      textTransform: "uppercase",
      color: "var(--text-faint)"
    }
  }, meta), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "22px",
      lineHeight: 1.1,
      color: "var(--text-heading)",
      letterSpacing: "var(--ls-tight)",
      margin: 0
    }
  }, title), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "baseline",
      justifyContent: "space-between",
      marginTop: "2px"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "14px",
      color: hover ? "var(--fae-accent)" : "var(--text-body)",
      transition: "color var(--dur-base) var(--ease-standard)"
    }
  }, price), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "11px",
      letterSpacing: "0.1em",
      color: "var(--text-faint)",
      opacity: hover ? 1 : 0,
      transition: "opacity var(--dur-base) var(--ease-standard)"
    }
  }, "VIEW \u2192"))));
}
Object.assign(__ds_scope, { ProductCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/storefront/ProductCard.jsx", error: String((e && e.message) || e) }); }

// components/storefront/SiteHeader.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * FÆBRIQ SiteHeader — storefront top nav.
 * Silver serif wordmark, mono nav links, cart count, circuit underline.
 */
function SiteHeader({
  links = ["Shop", "Collections", "About", "Journal"],
  active = "Shop",
  cartCount = 0,
  onNav,
  announcement = null,
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("header", _extends({
    style: {
      position: "relative",
      background: "var(--bg-page)",
      ...style
    }
  }, rest), announcement && /*#__PURE__*/React.createElement("div", {
    style: {
      borderBottom: "1px solid var(--border-hairline)",
      textAlign: "center",
      padding: "8px 16px",
      fontFamily: "var(--font-mono)",
      fontSize: "11px",
      letterSpacing: "0.1em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, announcement), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      height: "var(--header-h)",
      padding: "0 var(--space-6)",
      borderBottom: "1px solid var(--border-hairline)"
    }
  }, /*#__PURE__*/React.createElement("a", {
    href: "#",
    onClick: e => {
      e.preventDefault();
      onNav && onNav("home");
    },
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "26px",
      letterSpacing: "0.06em",
      color: "var(--fae-silver)",
      lineHeight: 1
    }
  }, "F\xC6BRIQ"), /*#__PURE__*/React.createElement("nav", {
    style: {
      display: "flex",
      gap: "var(--space-6)"
    }
  }, links.map(l => /*#__PURE__*/React.createElement("a", {
    key: l,
    href: "#",
    onClick: e => {
      e.preventDefault();
      onNav && onNav(l);
    },
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "12px",
      letterSpacing: "0.1em",
      textTransform: "uppercase",
      color: active === l ? "var(--text-body)" : "var(--text-muted)",
      position: "relative",
      paddingBottom: "4px",
      transition: "color var(--dur-fast) var(--ease-standard)"
    },
    onMouseEnter: e => e.currentTarget.style.color = "var(--fae-silver-hi)",
    onMouseLeave: e => e.currentTarget.style.color = active === l ? "var(--text-body)" : "var(--text-muted)"
  }, l, active === l && /*#__PURE__*/React.createElement("span", {
    style: {
      position: "absolute",
      left: 0,
      right: 0,
      bottom: 0,
      height: "1px",
      background: "var(--fae-accent)"
    }
  })))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: "var(--space-4)"
    }
  }, /*#__PURE__*/React.createElement("a", {
    href: "#",
    onClick: e => {
      e.preventDefault();
      onNav && onNav("search");
    },
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "12px",
      letterSpacing: "0.1em",
      textTransform: "uppercase",
      color: "var(--text-muted)"
    }
  }, "Search"), /*#__PURE__*/React.createElement("a", {
    href: "#",
    onClick: e => {
      e.preventDefault();
      onNav && onNav("cart");
    },
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "12px",
      letterSpacing: "0.1em",
      textTransform: "uppercase",
      color: "var(--text-body)",
      display: "inline-flex",
      gap: "6px"
    }
  }, "Cart", /*#__PURE__*/React.createElement("span", {
    style: {
      color: cartCount ? "var(--fae-accent)" : "var(--text-faint)"
    }
  }, "[", cartCount, "]")))));
}
Object.assign(__ds_scope, { SiteHeader });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/storefront/SiteHeader.jsx", error: String((e && e.message) || e) }); }

// ui_kits/storefront/About.jsx
try { (() => {
/**
 * About section — editorial brand statement over the void, two columns.
 */
function About() {
  const {
    CircuitRule,
    Badge
  } = window.FBRIQDesignSystem_0e5da2;
  return /*#__PURE__*/React.createElement("section", {
    style: {
      padding: "80px 56px",
      borderTop: "1px solid var(--border-hairline)",
      background: "var(--bg-sunken)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "0.8fr 1.2fr",
      gap: "64px",
      alignItems: "start",
      maxWidth: "1100px",
      margin: "0 auto"
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("span", {
    className: "fae-overline",
    style: {
      display: "block",
      marginBottom: "16px"
    }
  }, "// about"), /*#__PURE__*/React.createElement(CircuitRule, {
    width: 180
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "24px"
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "44px",
      lineHeight: 1.08,
      color: "var(--text-heading)",
      margin: 0
    }
  }, "Merch for people who ship at 2am from a co-working space in Lisbon."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "17px",
      lineHeight: 1.7,
      color: "var(--text-muted)",
      margin: 0,
      maxWidth: "58ch"
    }
  }, "F\xC6BRIQ makes wearable statements for queer tech professionals and digital nomads \u2014 the ones who build their identity the same way they build software: iteratively, deliberately, and on their own terms."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "17px",
      lineHeight: 1.7,
      color: "var(--text-muted)",
      margin: 0,
      maxWidth: "58ch"
    }
  }, "Dark editorial design. Premium heavyweight cotton. No hype, no neon, no cringe. Just a quiet message that the right people will read instantly."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "10px",
      marginTop: "8px"
    }
  }, /*#__PURE__*/React.createElement(Badge, {
    tone: "green"
  }, "Queer-owned"), /*#__PURE__*/React.createElement(Badge, {
    tone: "blue"
  }, "Print-on-demand"), /*#__PURE__*/React.createElement(Badge, {
    tone: "amber"
  }, "Ships US & Canada")))));
}
window.About = About;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/storefront/About.jsx", error: String((e && e.message) || e) }); }

// ui_kits/storefront/CollectionGrid.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const PRODUCTS = [{
  id: "p1",
  image: "../../assets/mockup-tee-model.png",
  meta: "TEE · 6.5 OZ",
  title: "Deploying Identity v2.0",
  price: "$35",
  badge: "New Drop",
  badgeTone: "new"
}, {
  id: "p2",
  image: "../../assets/mockup-sleeve.png",
  meta: "SLEEVE · 13\"",
  title: "Carry Protocol",
  price: "$42",
  badge: "Limited",
  badgeTone: "purple"
}, {
  id: "p3",
  image: "../../assets/mockup-stickers.png",
  meta: "STICKER PACK · ×6",
  title: "Commit Messages",
  price: "$12",
  badge: null
}, {
  id: "p4",
  image: "../../assets/mockup-flatlay.png",
  meta: "TEE · 6.5 OZ",
  title: "Serve It Black",
  price: "$35",
  badge: null
}, {
  id: "p5",
  image: "../../assets/mockup-tee-flat.png",
  meta: "TEE · 6.5 OZ",
  title: "Rebrand In Progress",
  price: "$35",
  badge: "Sold Out",
  badgeTone: "sold"
}, {
  id: "p6",
  image: "../../assets/mockup-sleeve-desk.png",
  meta: "SLEEVE · 15\"",
  title: "Nomad Edition",
  price: "$46",
  badge: null
}];

/**
 * Collection grid — filter rail + 3-up product grid.
 */
function CollectionGrid({
  onOpen
}) {
  const {
    ProductCard,
    CircuitRule
  } = window.FBRIQDesignSystem_0e5da2;
  const [filter, setFilter] = React.useState("All");
  const filters = ["All", "Tees", "Sleeves", "Stickers"];
  return /*#__PURE__*/React.createElement("section", {
    style: {
      padding: "64px 56px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "flex-end",
      justifyContent: "space-between",
      marginBottom: "12px"
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("span", {
    className: "fae-overline",
    style: {
      display: "block",
      marginBottom: "12px"
    }
  }, "The Catalog"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "40px",
      color: "var(--text-heading)",
      margin: 0
    }
  }, "Everything in the drop")), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "20px"
    }
  }, filters.map(f => /*#__PURE__*/React.createElement("button", {
    key: f,
    onClick: () => setFilter(f),
    style: {
      background: "none",
      border: "none",
      cursor: "pointer",
      padding: "0 0 4px",
      fontFamily: "var(--font-mono)",
      fontSize: "12px",
      letterSpacing: "0.1em",
      textTransform: "uppercase",
      color: filter === f ? "var(--text-body)" : "var(--text-faint)",
      borderBottom: filter === f ? "1px solid var(--fae-accent)" : "1px solid transparent"
    }
  }, f)))), /*#__PURE__*/React.createElement(CircuitRule, {
    width: "100%",
    nodes: false,
    style: {
      margin: "0 0 32px"
    }
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(3, 1fr)",
      gap: "24px"
    }
  }, PRODUCTS.map(p => /*#__PURE__*/React.createElement(ProductCard, _extends({
    key: p.id
  }, p, {
    onClick: () => onOpen && onOpen(p)
  })))));
}
window.CollectionGrid = CollectionGrid;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/storefront/CollectionGrid.jsx", error: String((e && e.message) || e) }); }

// ui_kits/storefront/Hero.jsx
try { (() => {
/**
 * Storefront hero — full-bleed flagship statement over the void.
 * Wordmark-scale serif headline, circuit rule, mono CTA row.
 */
function Hero({
  onShop
}) {
  const {
    Button,
    CircuitRule,
    Badge
  } = window.FBRIQDesignSystem_0e5da2;
  return /*#__PURE__*/React.createElement("section", {
    style: {
      position: "relative",
      borderBottom: "1px solid var(--border-hairline)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1.1fr 0.9fr",
      minHeight: "560px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      padding: "64px 56px",
      gap: "28px"
    }
  }, /*#__PURE__*/React.createElement(Badge, {
    tone: "new",
    dot: true
  }, "New Drop \xB7 Collection 02"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "68px",
      lineHeight: 1.02,
      letterSpacing: "-0.01em",
      color: "var(--text-heading)",
      margin: 0,
      maxWidth: "12ch"
    }
  }, "Please hold,", /*#__PURE__*/React.createElement("br", null), "I'm rebranding", /*#__PURE__*/React.createElement("br", null), /*#__PURE__*/React.createElement("span", {
    style: {
      color: "var(--fae-silver)"
    }
  }, "my identity.")), /*#__PURE__*/React.createElement(CircuitRule, {
    width: 300
  }), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "17px",
      color: "var(--text-muted)",
      maxWidth: "44ch",
      lineHeight: 1.6,
      margin: 0
    }
  }, "Engineered for the modern tech-nomad. High-contrast aesthetics, a quiet message. Code it. Serve it."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "14px",
      marginTop: "4px"
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "primary",
    size: "lg",
    onClick: onShop
  }, "Shop the drop"), /*#__PURE__*/React.createElement(Button, {
    variant: "ghost",
    size: "lg"
  }, "The flagship \u2192"))), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      background: "var(--bg-sunken)",
      borderLeft: "1px solid var(--border-hairline)",
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/mockup-tee-model.png",
    alt: "F\xC6BRIQ flagship tee on model",
    style: {
      width: "100%",
      height: "100%",
      objectFit: "cover",
      opacity: 0.96
    }
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      bottom: "20px",
      left: "20px",
      fontFamily: "var(--font-mono)",
      fontSize: "10px",
      letterSpacing: "0.14em",
      textTransform: "uppercase",
      color: "var(--text-faint)"
    }
  }, "FAE-TEE-001 \xB7 6.5oz \xB7 XS\u20133XL"))));
}
window.Hero = Hero;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/storefront/Hero.jsx", error: String((e && e.message) || e) }); }

// ui_kits/storefront/ProductDetail.jsx
try { (() => {
/**
 * Product detail — image well + buy column, sticky to the drop.
 */
function ProductDetail({
  product,
  onBack,
  onAdd
}) {
  const {
    Button,
    Badge,
    CircuitRule
  } = window.FBRIQDesignSystem_0e5da2;
  const p = product || {
    image: "../../assets/mockup-tee-model.png",
    meta: "TEE · 6.5 OZ",
    title: "Deploying Identity v2.0",
    price: "$35",
    badge: "New Drop",
    badgeTone: "new"
  };
  const [size, setSize] = React.useState("M");
  const sizes = ["XS", "S", "M", "L", "XL", "2XL", "3XL"];
  return /*#__PURE__*/React.createElement("section", {
    style: {
      padding: "40px 56px 80px"
    }
  }, /*#__PURE__*/React.createElement("button", {
    onClick: onBack,
    style: {
      background: "none",
      border: "none",
      cursor: "pointer",
      fontFamily: "var(--font-mono)",
      fontSize: "11px",
      letterSpacing: "0.1em",
      textTransform: "uppercase",
      color: "var(--text-muted)",
      marginBottom: "28px",
      padding: 0
    }
  }, "\u2190 Back to catalog"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "48px",
      alignItems: "start"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: "relative",
      aspectRatio: "4/5",
      background: "var(--bg-sunken)",
      border: "1px solid var(--border-hairline)",
      overflow: "hidden"
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: p.image,
    alt: p.title,
    style: {
      width: "100%",
      height: "100%",
      objectFit: "cover"
    }
  }), p.badge && /*#__PURE__*/React.createElement("div", {
    style: {
      position: "absolute",
      top: "16px",
      left: "16px"
    }
  }, /*#__PURE__*/React.createElement(Badge, {
    tone: p.badgeTone,
    dot: p.badgeTone === "new"
  }, p.badge))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "22px",
      paddingTop: "8px"
    }
  }, /*#__PURE__*/React.createElement("span", {
    className: "fae-overline"
  }, p.meta), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "48px",
      lineHeight: 1.05,
      color: "var(--text-heading)",
      margin: 0
    }
  }, p.title), /*#__PURE__*/React.createElement(CircuitRule, {
    width: 220
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "22px",
      color: "var(--text-body)"
    }
  }, p.price), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "15px",
      lineHeight: 1.7,
      color: "var(--text-muted)",
      margin: 0,
      maxWidth: "46ch"
    }
  }, "Premium heavyweight cotton, 6.5oz. Soft hand-feel, structured drape. Screen-quality DTG print that survives the laundromat in any timezone."), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("span", {
    className: "fae-overline",
    style: {
      display: "block",
      marginBottom: "10px"
    }
  }, "Size"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "8px",
      flexWrap: "wrap"
    }
  }, sizes.map(s => /*#__PURE__*/React.createElement("button", {
    key: s,
    onClick: () => setSize(s),
    style: {
      width: "46px",
      height: "46px",
      cursor: "pointer",
      background: size === s ? "var(--fae-silver)" : "transparent",
      color: size === s ? "var(--fae-black)" : "var(--text-muted)",
      border: `1px solid ${size === s ? "var(--fae-silver)" : "var(--border-strong)"}`,
      fontFamily: "var(--font-mono)",
      fontSize: "12px"
    }
  }, s)))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "12px",
      marginTop: "6px"
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "primary",
    size: "lg",
    style: {
      flex: 1
    },
    onClick: () => onAdd && onAdd(p)
  }, "Add to cart \u2014 ", p.price), /*#__PURE__*/React.createElement(Button, {
    variant: "secondary",
    size: "lg"
  }, "\u2665")), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "11px",
      color: "var(--text-faint)",
      letterSpacing: "0.06em"
    }
  }, "// free US & Canada shipping over $80 \xB7 30-day returns"))));
}
window.ProductDetail = ProductDetail;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/storefront/ProductDetail.jsx", error: String((e && e.message) || e) }); }

// ui_kits/storefront/SiteFooter.jsx
try { (() => {
/**
 * Storefront footer — wordmark, link columns, newsletter, circuit cap.
 */
function SiteFooter() {
  const {
    Input,
    Button,
    CircuitRule
  } = window.FBRIQDesignSystem_0e5da2;
  const cols = [{
    h: "Shop",
    items: ["Tees", "Sleeves", "Stickers", "Gift cards"]
  }, {
    h: "Brand",
    items: ["About", "Journal", "Sustainability", "Sizing"]
  }, {
    h: "Support",
    items: ["Shipping", "Returns", "Contact", "FAQ"]
  }];
  return /*#__PURE__*/React.createElement("footer", {
    style: {
      borderTop: "1px solid var(--border-hairline)",
      padding: "56px 56px 32px"
    }
  }, /*#__PURE__*/React.createElement(CircuitRule, {
    width: "100%",
    style: {
      marginBottom: "40px"
    }
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1.4fr 1fr 1fr 1fr 1.4fr",
      gap: "40px"
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-display)",
      fontSize: "30px",
      letterSpacing: "0.06em",
      color: "var(--fae-silver)",
      marginBottom: "12px"
    }
  }, "F\xC6BRIQ"), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-display)",
      fontStyle: "italic",
      fontSize: "16px",
      color: "var(--text-muted)"
    }
  }, "Code it. Serve it.")), cols.map(c => /*#__PURE__*/React.createElement("div", {
    key: c.h
  }, /*#__PURE__*/React.createElement("div", {
    className: "fae-overline",
    style: {
      marginBottom: "16px"
    }
  }, c.h), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "10px"
    }
  }, c.items.map(i => /*#__PURE__*/React.createElement("a", {
    key: i,
    href: "#",
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "14px",
      color: "var(--text-muted)"
    }
  }, i))))), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    className: "fae-overline",
    style: {
      marginBottom: "16px"
    }
  }, "The dispatch"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: "var(--font-body)",
      fontSize: "13px",
      color: "var(--text-faint)",
      margin: "0 0 14px",
      lineHeight: 1.5
    }
  }, "Drop alerts. No spam. Unsubscribe anytime."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "8px"
    }
  }, /*#__PURE__*/React.createElement(Input, {
    placeholder: "you@domain.dev",
    style: {
      flex: 1
    }
  }), /*#__PURE__*/React.createElement(Button, {
    variant: "accent"
  }, "Join")))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      justifyContent: "space-between",
      marginTop: "48px",
      paddingTop: "20px",
      borderTop: "1px solid var(--border-hairline)"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "10px",
      letterSpacing: "0.1em",
      color: "var(--text-faint)"
    }
  }, "\xA9 2026 F\xC6BRIQ \xB7 QUEER-OWNED \xB7 PRINTED ON DEMAND"), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "10px",
      letterSpacing: "0.1em",
      color: "var(--text-faint)"
    }
  }, "BUILT FOR THE NOMADS")));
}
window.SiteFooter = SiteFooter;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/storefront/SiteFooter.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.CircuitRule = __ds_scope.CircuitRule;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.ProductCard = __ds_scope.ProductCard;

__ds_ns.SiteHeader = __ds_scope.SiteHeader;

})();
