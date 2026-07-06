import * as React from "react";

/** Flat editorial surface — hairline border, square corners, no shadow. */
export interface CardProps {
  children: React.ReactNode;
  /** Add the six-color circuit accent along the top edge. @default false */
  accent?: boolean;
  /** Brighten the border on hover (for clickable cards). @default false */
  interactive?: boolean;
  /** CSS padding. @default "var(--space-5)" */
  padding?: string | number;
  style?: React.CSSProperties;
}

export function Card(props: CardProps): JSX.Element;
