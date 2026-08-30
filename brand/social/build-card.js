const op = require('opentype.js');
const fs = require('fs');

const W = 1200, H = 630;
const TEXT = 'FÆBRIQ';
const TRACKING_EM = 0.06;          // matches .fae-header__wordmark letter-spacing
const TARGET_INK_W = 660;          // wordmark ink width on the 1200px canvas
const BAR_H = 12;                  // slim, but legible at social preview sizes
const GAP = 44;                    // lowest ink (Q tail) -> bar top
const STRIPES = ['#E8272A','#F47F20','#F9D426','#2AAA42','#1D5BBE','#7B3FAA'];

const font = op.parse(fs.readFileSync('InstrumentSerif-Regular.ttf').buffer);

// Lay out glyphs at a reference size, applying tracking manually.
function layout(size) {
  const track = size * TRACKING_EM;
  // Per-char mapping: bypasses GSUB shaping (unsupported ccmp lookup in this
  // font build) and is safe here — six plain capitals, Æ is a single codepoint.
  const glyphs = [...TEXT].map(c => font.charToGlyph(c));
  let x = 0;
  const out = [];
  glyphs.forEach((g, i) => {
    out.push({ g, x });
    x += (g.advanceWidth / font.unitsPerEm) * size;
    if (i < glyphs.length - 1) {
      let kern = 0;
      try { kern = font.getKerningValue(g, glyphs[i + 1]) || 0; } catch (e) {}
      x += (kern / font.unitsPerEm) * size + track;
    }
  });
  return { items: out, advanceWidth: x - track };
}

// Union ink bbox of the laid-out string at a given size.
function inkBox(size) {
  const { items } = layout(size);
  let x1 = Infinity, y1 = Infinity, x2 = -Infinity, y2 = -Infinity;
  for (const { g, x } of items) {
    const p = g.getPath(x, 0, size);
    const b = p.getBoundingBox();
    if (b.x1 === 0 && b.x2 === 0 && b.y1 === 0 && b.y2 === 0) continue; // space
    x1 = Math.min(x1, b.x1); y1 = Math.min(y1, b.y1);
    x2 = Math.max(x2, b.x2); y2 = Math.max(y2, b.y2);
  }
  return { x1, y1, x2, y2, w: x2 - x1, h: y2 - y1 };
}

// Solve font size so ink width == TARGET_INK_W
const REF = 400;
const refBox = inkBox(REF);
const SIZE = REF * (TARGET_INK_W / refBox.w);
const box = inkBox(SIZE);

// Cap-band height (ignore Q's descending tail) for honest vertical centring
const capBox = (() => {
  const { items } = layout(SIZE);
  let y1 = Infinity, y2 = -Infinity;
  for (const { g, x } of items) {
    if (g.name === 'Q') continue;
    const b = g.getPath(x, 0, SIZE).getBoundingBox();
    y1 = Math.min(y1, b.y1); y2 = Math.max(y2, b.y2);
  }
  return { y1, y2, h: y2 - y1 };
})();

// Block = full ink band + gap + bar, centred vertically on the canvas.
// Measured from the full ink box (not the cap band) so the Q's descending tail
// keeps real clearance above the bar instead of grazing it.
const blockH = box.h + GAP + BAR_H;
const blockTop = (H - blockH) / 2;
const baselineY = blockTop - box.y1;             // box.y1 is negative (above baseline)
const barY = +(blockTop + box.h + GAP).toFixed(2);
const barX = +((W - TARGET_INK_W) / 2).toFixed(2);
const originX = (W - box.w) / 2 - box.x1;        // centre on ink, not on advance width

// Build path data
const { items } = layout(SIZE);
const pathData = items
  .map(({ g, x }) => g.getPath(originX + x, baselineY, SIZE).toPathData(2))
  .filter(d => d && d !== 'Z' && d.length > 2)
  .join(' ');

const stripeW = TARGET_INK_W / 6;
const bars = STRIPES.map((c, i) =>
  `  <rect x="${+(barX + i * stripeW).toFixed(2)}" y="${barY}" width="${+stripeW.toFixed(2)}" height="${BAR_H}" fill="${c}"/>`
).join('\n');

const head = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="FÆBRIQ">
  <title>FÆBRIQ</title>
  <rect width="${W}" height="${H}" fill="#FFFFFF"/>`;

// Variant 1 — outlined paths (self-contained, font-independent)
fs.writeFileSync('faebriq-og-card.svg',
`${head}
  <!-- Wordmark: Instrument Serif, converted to outlines -->
  <path d="${pathData}" fill="#000000"/>
  <!-- Pride Circuit bar: six flush stripes, hard edges, no gradient -->
${bars}
</svg>
`);

// Variant 2 — live text (editable source)
fs.writeFileSync('faebriq-og-card-text.svg',
`${head}
  <!-- Editable source. Renders in Instrument Serif where available, Georgia otherwise. -->
  <text x="${W / 2}" y="${baselineY.toFixed(2)}" fill="#000000" text-anchor="middle"
        font-family="Instrument Serif, Georgia, serif"
        font-size="${SIZE.toFixed(2)}" letter-spacing="${(SIZE * TRACKING_EM).toFixed(2)}"
        >${TEXT}</text>
  <!-- Pride Circuit bar: six flush stripes, hard edges, no gradient -->
${bars}
</svg>
`);

console.log('font size      :', SIZE.toFixed(2));
console.log('ink bbox w x h :', box.w.toFixed(1), 'x', box.h.toFixed(1));
console.log('cap band h     :', capBox.h.toFixed(1));
console.log('baseline y     :', baselineY.toFixed(1));
console.log('bar            : x', barX, 'y', barY.toFixed(1), 'w', TARGET_INK_W, 'h', BAR_H);
console.log('stripe width   :', stripeW.toFixed(2));
console.log('path data chars:', pathData.length);
