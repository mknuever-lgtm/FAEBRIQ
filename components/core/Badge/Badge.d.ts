import * as React from "react";

/** Small mono status/marker chip — outlined, sharp. */
export interface BadgeProps {
  children: React.ReactNode;
  /** Color tone. @default "default" */
  tone?: "default" | "accent" | "new" | "sold" | "coral" | "amber" | "yellow" | "green" | "blue" | "purple";
  /** Show a leading status dot. @default false */
  dot?: boolean;
  style?: React.CSSProperties;
}

export function Badge(props: BadgeProps): JSX.Element;
