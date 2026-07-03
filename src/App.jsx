import React from "react";
import { SiteHeader } from "../components/storefront/SiteHeader/SiteHeader.jsx";
import { Hero } from "../ui_kits/storefront/Hero.jsx";
import { CollectionGrid } from "../ui_kits/storefront/CollectionGrid.jsx";
import { ProductDetail } from "../ui_kits/storefront/ProductDetail.jsx";
import { About } from "../ui_kits/storefront/About.jsx";
import { SiteFooter } from "../ui_kits/storefront/SiteFooter.jsx";

export default function App() {
  const [product, setProduct] = React.useState(null);

  return (
    <div style={{ maxWidth: "1240px", margin: "0 auto", background: "var(--bg-page)" }}>
      <SiteHeader
        announcement="Made to order · ships from Canada"
        cartCount={0}
        onNav={() => setProduct(null)}
      />
      {product ? (
        <ProductDetail product={product} onBack={() => setProduct(null)} />
      ) : (
        <>
          <Hero onShop={() => document.getElementById("catalog")?.scrollIntoView({ behavior: "smooth" })} />
          <div id="catalog">
            <CollectionGrid onOpen={setProduct} />
          </div>
          <About />
        </>
      )}
      <SiteFooter />
    </div>
  );
}
