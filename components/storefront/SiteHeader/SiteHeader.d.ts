import * as React from "react";

/**
 * Storefront top navigation — wordmark, mono links, cart count.
 *
 * @startingPoint section="Storefront" subtitle="Site header with wordmark, nav, cart" viewport="1240x120"
 */
export interface SiteHeaderProps {
  /** Nav link labels. @default ["Shop","Collections","About","Journal"] */
  links?: string[];
  /** Currently active link label. @default "Shop" */
  active?: string;
  /** Number shown in the cart pill. @default 0 */
  cartCount?: number;
  /** Optional announcement bar text above the nav */
  announcement?: React.ReactNode;
  /** Fired with the clicked label (or "home"/"cart"/"search") */
  onNav?: (target: string) => void;
  style?: React.CSSProperties;
}

export function SiteHeader(props: SiteHeaderProps): JSX.Element;
