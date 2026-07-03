import * as React from "react";

/** The signature six-color circuit divider — segmented bands (confirmed style, June 2026). */
export interface CircuitRuleProps {
  /** Gap between the six segments, px. @default 4 */
  gap?: number;
  /** Bar height, px. @default 4 */
  height?: number;
  /** CSS width. @default "100%" */
  width?: string | number;
  /** Push to the right edge of its container. @default "left" */
  align?: "left" | "right";
  style?: React.CSSProperties;
}

export function CircuitRule(props: CircuitRuleProps): JSX.Element;
