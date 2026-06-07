import * as React from "react";

/** The signature six-color circuit divider with optional terminal nodes. */
export interface CircuitRuleProps {
  /** Render hollow terminal nodes at the line origins. @default true */
  nodes?: boolean;
  /** Vertical gap between the six hairlines, px. @default 5 */
  gap?: number;
  /** CSS width. @default "100%" */
  width?: string | number;
  /** Push to the right edge of its container. @default "left" */
  align?: "left" | "right";
  style?: React.CSSProperties;
}

export function CircuitRule(props: CircuitRuleProps): JSX.Element;
