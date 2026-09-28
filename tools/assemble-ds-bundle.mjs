#!/usr/bin/env node
/**
 * Assemble the design-sync upload bundle from this repo's nested layout.
 *
 * The repo IS the design system — there is no npm package or dist/ for the
 * design-sync converter to chew on, so this script is the converter's
 * deterministic stand-in. It copies the shipped layout into ./ds-bundle and
 * makes the preview cards self-contained:
 *
 *   - React + ReactDOM UMD are vendored into _vendor/ (the repo's own pinned
 *     versions), replacing the unpkg.com <script> tags. Cards must render with
 *     no network: a CDN the preview environment can't reach is a blank card.
 *   - Inline <script type="text/babel"> blocks are compiled ahead of time, so
 *     no 3MB Babel runtime has to ship or run in the card.
 *
 * The repo's own .html sources keep their CDN tags and stay directly openable;
 * only the bundle copies are rewritten.
 *
 *   node tools/assemble-ds-bundle.mjs [outDir]     # default ./ds-bundle
 */
import { createHash } from "node:crypto";
import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { transformSync } from "@babel/core";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const OUT = resolve(ROOT, process.argv[2] || "ds-bundle");

if (OUT === ROOT) throw new Error("refusing to assemble into the repo root");
rmSync(OUT, { recursive: true, force: true });
mkdirSync(OUT, { recursive: true });

/** Directories copied wholesale. */
for (const dir of ["components", "tokens", "guidelines", "ui_kits"]) {
  cpSync(join(ROOT, dir), join(OUT, dir), { recursive: true });
}

/** Root files. assets/ ships flat — print-art/ is production art, not design-system material. */
cpSync(join(ROOT, "styles.css"), join(OUT, "styles.css"));
cpSync(join(ROOT, "_ds_bundle.js"), join(OUT, "_ds_bundle.js"));
cpSync(join(ROOT, "readme.md"), join(OUT, "README.md"));
cpSync(join(ROOT, "SKILL.md"), join(OUT, "SKILL.md"));
writeFileSync(join(OUT, "_ds_needs_recompile"), '{"by":"design-sync-cli"}');

mkdirSync(join(OUT, "assets"), { recursive: true });
for (const name of readdirSync(join(ROOT, "assets"))) {
  const src = join(ROOT, "assets", name);
  if (statSync(src).isFile()) cpSync(src, join(OUT, "assets", name));
}

/** _vendor/ — the React the cards actually run against, pinned by package.json. */
const VENDOR = [
  ["react.js", "react/umd/react.production.min.js"],
  ["react-dom.js", "react-dom/umd/react-dom.production.min.js"],
];
mkdirSync(join(OUT, "_vendor"), { recursive: true });
for (const [name, modPath] of VENDOR) {
  cpSync(join(ROOT, "node_modules", modPath), join(OUT, "_vendor", name));
}

const CDN_TAG = /^[ \t]*<script src="https:\/\/unpkg\.com\/[^"]*"[^>]*><\/script>\n/gm;
const JSX_SRC_TAG = /^[ \t]*<script type="text\/babel" src="[^"]*"><\/script>\n/gm;
const INLINE_BABEL = /<script type="text\/babel">([\s\S]*?)<\/script>/g;

function htmlFiles(dir) {
  const out = [];
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) out.push(...htmlFiles(p));
    else if (name.endsWith(".html")) out.push(p);
  }
  return out;
}

let cards = 0;
for (const file of htmlFiles(OUT)) {
  let html = readFileSync(file, "utf8");
  if (!html.includes("text/babel")) continue;

  // "../" per directory between the card and the bundle root.
  const up = "../".repeat(relative(OUT, dirname(file)).split("/").length);
  const vendorTags = VENDOR.map(([name]) => `  <script src="${up}_vendor/${name}"></script>\n`).join("");

  let replacedCdn = false;
  html = html
    .replace(CDN_TAG, () => (replacedCdn ? "" : ((replacedCdn = true), vendorTags)))
    // Redundant in the bundle: _ds_bundle.js already exposes these on window.
    .replace(JSX_SRC_TAG, "")
    .replace(INLINE_BABEL, (_, code) => {
      const { code: js } = transformSync(code, {
        filename: file,
        babelrc: false,
        configFile: false,
        presets: [["@babel/preset-react", { runtime: "classic" }]],
      });
      return `<script>\n${js}\n</script>`;
    });

  if (!replacedCdn) throw new Error(`${relative(OUT, file)}: no CDN script tags to replace`);
  writeFileSync(file, html);
  cards++;
}

const leftover = htmlFiles(OUT).filter((f) => readFileSync(f, "utf8").includes("unpkg.com"));
if (leftover.length) throw new Error(`unpkg refs survived in: ${leftover.map((f) => relative(OUT, f))}`);

/** Components, in the shape the design-sync hashing helpers expect. */
const header = JSON.parse(
  /^\/\* @ds-bundle: (.*) \*\//
    .exec(readFileSync(join(OUT, "_ds_bundle.js"), "utf8").split("\n", 1)[0])[1]
    .replace(/\*\\\//g, "*/"),
);
const components = header.components.map((c) => ({
  name: c.name,
  group: c.sourcePath.split("/")[1],
}));

writeFileSync(
  join(OUT, ".ds-build-meta.json"),
  JSON.stringify(
    {
      namespace: header.namespace,
      source: "faebriq-design-system@repo",
      shape: "package",
      provider: null,
      componentCount: components.length,
      skippedStoryIds: [],
      runtimeFontPrefixes: [],
    },
    null,
    2,
  ) + "\n",
);

/**
 * _ds_sync.json — the verification anchor the next sync diffs against.
 * Computed with design-sync's own hashing lib so the numbers mean exactly
 * what the consumer thinks they mean; skipped (honestly) when the skill's
 * scripts aren't staged. `sourceKeys` is deliberately omitted: this repo has
 * no authored .tsx previews for it to key on, and omitting it makes changed
 * artifacts re-verify rather than falsely carrying a grade forward.
 */
const LIB = resolve(ROOT, ".ds-sync/lib/sync-hashes.mjs");
if (!existsSync(LIB)) {
  console.log("  _ds_sync.json skipped — .ds-sync/lib not staged; next sync re-verifies everything");
} else {
  const { KEY_RECIPE, auxShaFor, renderHashFor, scriptsShaFor, styleShaFor } = await import(LIB);
  writeFileSync(
    join(OUT, "_ds_sync.json"),
    JSON.stringify(
      {
        shape: "package",
        styleSha: styleShaFor(OUT, { includeBundleBody: true }),
        renderHashes: Object.fromEntries(
          components.map((c) => [c.name, renderHashFor(OUT, c)]),
        ),
        keyRecipe: KEY_RECIPE,
        scriptsSha: scriptsShaFor(),
        sourceHashes: header.sourceHashes,
        auxSha: auxShaFor(OUT),
        bundleSha12: createHash("sha256")
          .update(readFileSync(join(OUT, "_ds_bundle.js")))
          .digest("hex")
          .slice(0, 12),
      },
      null,
      2,
    ) + "\n",
  );
  console.log(`  _ds_sync.json: ${components.length} render hashes (verification anchor)`);
}

console.log(`ds-bundle: ${cards} cards vendored + precompiled → ${relative(ROOT, OUT)}/`);
