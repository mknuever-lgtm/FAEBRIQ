import * as React from "react";

/**
 * Sharp, editorial button with terminal-mono label.
 *
 * @startingPoint section="Core" subtitle="Primary / accent / secondary / ghost — sharp mono button" viewport="700x220"
 */
export interface ButtonProps {
  children: React.ReactNode;
  /** Visual style. @default "primary" */
  variant?: "primary" | "accent" | "secondary" | "ghost";
  /** @default "md" */
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  /** Element rendered before the label */
  iconLeft?: React.ReactNode;
  /** Element rendered after the label */
  iconRight?: React.ReactNode;
  type?: "button" | "submit" | "reset";
  onClick?: (e: React.MouseEvent<HTMLButtonElement>) => void;
  style?: React.CSSProperties;
}

export function Button(props: ButtonProps): JSX.Element;
