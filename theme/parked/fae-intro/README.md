# Parked: FÆ intro section (2026/10/02)

Not used on the live site. The live home page uses the `meet-fae` section
instead. Kept here as an alternative FÆ block. Source: branch
claude/faebriq-hero-fixes-02dw1g.

Files:
- fae-intro.liquid: the section (schema name "FÆ intro", has an image picker).
- fae-front.webp: its default image (front render, 1000x1640).

To try it: copy fae-intro.liquid into the theme's sections/ and
fae-front.webp into assets/, add "fae-intro" to templates/index.json
(sections and order), and preview it in the theme editor. It uses classes
and variables that already exist in faebriq.css (fae-container, fae-hero__cta,
--fae-text, --fae-text-dim, --fae-line-700). Never publish a theme without
Maurice's explicit OK.
