#!/usr/bin/env node
/**
 * Regenerate _ds_bundle.js from the real component sources.
 *
 * The FÆBRIQ design system has no npm package and no dist/, so the
 * design-sync converter can't run here. This is the repo's own deterministic
 * equivalent: every module in MODULES is Babel-transformed from its .jsx
 * source and emitted into the format-3 IIFE bundle the claude.ai/design
 * self-check reads.
 *
 * Run it whenever a component or ui_kit source changes:
 *   npm run build:ds-bundle
 *
 * Output format (must stay stable — the app's self-check parses the header):
 *   /* @ds-bundle: {...} *\/            header with sourceHashes
 *   (() => { ... })();                  one try/catch IIFE per module
 *   __ds_ns.<Name> = __ds_scope.<Name>; component exports on the namespace
 */
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { transformSync } from "@babel/core";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const GLOBAL_NAME = JSON.parse(
  readFileSync(resolve(ROOT, ".design-sync/config.json"), "utf8"),
).globalName;

/** bundlePath (what the header and error paths report) -> source file on disk. */
const MODULES = [
  ["components/core/Badge.jsx", "components/core/Badge/Badge.jsx", "component"],
  ["components/core/Button.jsx", "components/core/Button/Button.jsx", "component"],
  ["components/core/Card.jsx", "components/core/Card/Card.jsx", "component"],
  ["components/core/CircuitRule.jsx", "components/core/CircuitRule/CircuitRule.jsx", "component"],
  ["components/core/Input.jsx", "components/core/Input/Input.jsx", "component"],
  ["components/storefront/ProductCard.jsx", "components/storefront/ProductCard/ProductCard.jsx", "component"],
  ["components/storefront/SiteHeader.jsx", "components/storefront/SiteHeader/SiteHeader.jsx", "component"],
  ["ui_kits/storefront/About.jsx", "ui_kits/storefront/About.jsx", "screen"],
  ["ui_kits/storefront/CollectionGrid.jsx", "ui_kits/storefront/CollectionGrid.jsx", "screen"],
  ["ui_kits/storefront/Hero.jsx", "ui_kits/storefront/Hero.jsx", "screen"],
  ["ui_kits/storefront/ProductDetail.jsx", "ui_kits/storefront/ProductDetail.jsx", "screen"],
  ["ui_kits/storefront/SiteFooter.jsx", "ui_kits/storefront/SiteFooter.jsx", "screen"],
];

/**
 * Strips the ESM imports, rewrites design-system references, and unwraps the
 * single named export. Components reach siblings through `__ds_scope` (they
 * run in bundle order); screens destructure from the window namespace at
 * render time, so they can use components declared after them.
 */
function dsModulePlugin({ types: t }, { kind }) {
  return {
    visitor: {
      Program(path, state) {
        const dsNames = [];
        const dsRefs = [];
        for (const stmt of path.get("body")) {
          if (!stmt.isImportDeclaration()) continue;
          if (stmt.node.source.value !== "react") {
            for (const spec of stmt.node.specifiers) {
              const name = spec.local.name;
              dsNames.push(name);
              // Collect references while the import binding still exists.
              const binding = path.scope.getBinding(name);
              for (const ref of binding ? binding.referencePaths : []) {
                dsRefs.push([name, ref]);
              }
            }
          }
          stmt.remove();
        }
        state.dsNames = dsNames;
        if (kind === "component") {
          for (const [name, ref] of dsRefs) {
            ref.replaceWith(
              ref.isJSXIdentifier()
                ? t.jsxMemberExpression(
                    t.jsxIdentifier("__ds_scope"),
                    t.jsxIdentifier(name),
                  )
                : t.memberExpression(t.identifier("__ds_scope"), t.identifier(name)),
            );
          }
        }
      },
      ExportNamedDeclaration(path, state) {
        const decl = path.node.declaration;
        if (!decl) return;
        if (kind === "screen" && state.dsNames.length && t.isFunctionDeclaration(decl)) {
          decl.body.body.unshift(
            t.variableDeclaration("const", [
              t.variableDeclarator(
                t.objectPattern(
                  state.dsNames.map((n) =>
                    t.objectProperty(t.identifier(n), t.identifier(n), false, true),
                  ),
                ),
                t.memberExpression(t.identifier("window"), t.identifier(GLOBAL_NAME)),
              ),
            ]),
          );
        }
        path.replaceWith(decl);
      },
    },
  };
}

const sourceHashes = {};
const components = [];
const blocks = [];

for (const [bundlePath, srcPath, kind] of MODULES) {
  const src = readFileSync(resolve(ROOT, srcPath), "utf8");
  sourceHashes[bundlePath] = createHash("sha256").update(src).digest("hex").slice(0, 12);

  const name = bundlePath.split("/").pop().replace(/\.jsx$/, "");
  if (kind === "component") components.push({ name, sourcePath: bundlePath });

  const { code } = transformSync(src, {
    filename: srcPath,
    babelrc: false,
    configFile: false,
    presets: [["@babel/preset-react", { runtime: "classic" }]],
    plugins: [[dsModulePlugin, { kind }]],
  });

  const expose =
    kind === "component"
      ? `Object.assign(__ds_scope, { ${name} });`
      : `window.${name} = ${name};`;

  blocks.push(
    `// ${bundlePath}\ntry { (() => {\n${code}\n${expose}\n})(); } catch (e) { ` +
      `__ds_ns.__errors.push({ path: ${JSON.stringify(bundlePath)}, ` +
      `error: String((e && e.message) || e) }); }`,
  );
}

const header = {
  format: 3,
  namespace: GLOBAL_NAME,
  components,
  sourceHashes,
  inlinedExternals: [],
  unexposedExports: [],
};

const out = [
  `/* @ds-bundle: ${JSON.stringify(header)} */`,
  "",
  "(() => {",
  "",
  `const __ds_ns = (window.${GLOBAL_NAME} = window.${GLOBAL_NAME} || {});`,
  "",
  "const __ds_scope = {};",
  "",
  "(__ds_ns.__errors = __ds_ns.__errors || []);",
  "",
  ...blocks.flatMap((b) => [b, ""]),
  ...components.flatMap((c) => [`__ds_ns.${c.name} = __ds_scope.${c.name};`, ""]),
  "})();",
  "",
].join("\n");

writeFileSync(resolve(ROOT, "_ds_bundle.js"), out);
console.log(
  `_ds_bundle.js: ${components.length} components, ${MODULES.length - components.length} screens`,
);
