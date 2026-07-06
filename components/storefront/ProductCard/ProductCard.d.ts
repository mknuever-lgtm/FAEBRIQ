import * as React from "react";

/**
 * Storefront merch tile — image well, display title, mono price/meta.
 *
 * @startingPoint section="Storefront" subtitle="Product tile with image, title, price, badge" viewport="360x460"
 */
export interface ProductCardProps {
  /** Product image URL */
  image: string;
  title: string;
  /** Price string, e.g. "$35" */
  price: string;
  /** Mono overline, e.g. "TEE · 6.5 OZ" */
  meta?: string;
  /** Corner badge label, e.g. "New Drop" */
  badge?: string;
  /** Badge color tone. @default "new" */
  badgeTone?: "default" | "accent" | "new" | "sold" | "coral" | "amber" | "yellow" | "green" | "blue" | "purple";
  onClick?: (e: React.MouseEvent<HTMLDivElement>) => void;
  style?: React.CSSProperties;
}

export function ProductCard(props: ProductCardProps): JSX.Element;
