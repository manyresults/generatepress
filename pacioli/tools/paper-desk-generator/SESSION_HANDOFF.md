# Session handoff — Pacioli Finance "Paper Desk" rebuild

**Repo:** manyresults/generatepress · **This work:** branch `claude/elegant-clarke-f7jlo6`
**Earlier work (separate branch, NOT merged):** `claude/epic-cori-y5x8wi` — has `paper-desk-tokens.css`,
the component kit, and the first Paper Desk pages. The two branches have not been merged; decide which
branch to consolidate on before adding more files (the generator's `tok.css` is a copy of the tokens file).

## Goal
Rebuild the Pacioli Finance WordPress site (GeneratePress + GenerateBlocks Pro) page by page as paste-ready
block markup for WP's Code Editor, in the "Paper Desk" style (cream paper, hard offset shadows, hand-drawn
doodles, small icon badges). Tokens (`--paper-*`) are pasted ONCE into Appearance > Customize > Additional CSS.

## Done on this branch (all in `pacioli/`)
| Page | File |
|---|---|
| Clean-Up Bookkeeping | services-cleanup-bookkeeping.html |
| Tax & Compliance | services-tax-compliance.html |
| Internal Audit | services-internal-audit.html |
| Payroll | services-payroll.html |
| Industries hub | industries-hub-paper.html |
| Non-Profit, Education, Legal, Professional Services, Real Estate, Technology | industry-<name>-paper.html |

Earlier (epic branch, confirmed working by the user): homepage-v2, about-page, contact-page, faqs,
reviews-page, industry-professional-services, solutions-page, resources-hub, plus reusable blocks
cta-block-paper (ref 51507) and testimonials-block-paper (ref 51469).

## Not yet redone in Paper Desk (sources on the epic branch, old visual style)
services-bookkeeping.html (the 7-item "Full Service Breakdown" bookkeeping page — NOT broken, see below),
tax-checklists-hub + 6 tax-checklist-*.html pages, tax-forms-directory, irs-forms-publications,
thank-you-page, site-header, footer, mega-menu-site-nav + overlay-*.html (nav got only rename/centering fixes),
services-template. Ask the user which to do next and in what order.

## Generator (`pacioli/tools/paper-desk-generator/`)
- `python3 -I build.py bodies/<page>_body.py > ../../<out>.html` assembles shared helpers + a page body and runs it.
- `python3 -I validate.py <out>.html` (run inside the generator dir; reads `tok.css`) checks block JSON, wp: nesting,
  HTML balance, duplicate uniqueIds, raw `&`, undefined `--paper-*` tokens. Must say `errors 0`.
- `shot.py` renders with headless Chromium (Playwright; do NOT run `playwright install`, Chromium is at
  /opt/pw-browsers/chromium; set PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1). It injects tok.css (strip the `@import` with
  `re.sub(r'@import url\([^)]*\);','',css)`) plus every block's `css` attribute. It is a layout check only.
- `bodies/np_body.py` = template for an industry page; other bodies: tax, audit, payroll, hub, education, legal,
  professional-services, real-estate, technology. Clean-Up Bookkeeping's body is the tail of `helpers_source.py`.
- Helpers: `section, eyebrow, h2, para, btn(kind=primary|light|ghost), badge, dot_row, col, doodle, acc_item (GB Pro accordion)`.
  Use `AMPSEMI` for `&amp;`. Never type a raw `&` into block JSON.

## CLIENT RULES (apply to every page)
- Never say "owner" for Pacioli's owner. CMA line: "Controller-level oversight from / Overseen by a Certified Management Accountant (CMA)".
- No client-count figures ("16-20 active client relationships") -> "the same ... process we give every client relationship we take on".
- No revenue range ($2.5M-$5M) anywhere; don't call clients "small businesses" — "established businesses", nationwide.
  (Ideal client is $2.5-5M but smaller clients are welcome; don't rule them out in copy.)
- No large raster images/big icons in heroes or feature grids (small icon badges only). Corner doodles hide < 1100px.
- Keep the page's own copy, links and anchors; fix duplicate anchors/typos and say so.
- Trade was renamed Professional Services (`/industries/professional-services/`).
- Hero/CTA buttons go to `/contact/`.

## HOW TO PASTE (this caused most of the "bugs")
1. Open the file on GitHub -> **Copy raw file**. NEVER copy from the chat or a file viewer: it silently strips
   `<!-- wp:... -->` block comments and the page renders as unstyled raw HTML (giant icons, no cards, no accordion).
2. WP page -> three-dot menu -> **Code editor** -> Cmd+A -> paste -> **Update** straight from the Code Editor.
   Don't switch to the visual editor first: "Attempt recovery" rewrites blocks.
3. Hard-refresh the live page. The original Bookkeeping "bug" was a bad copy plus stale cache, not the markup.
4. WP rewrites `--` to `--` on save; that's normal.

## Open items / decisions for the user
- Consolidate the two branches (which one is canonical?). Output files here use a `-paper` suffix so they don't
  overwrite the older files on the epic branch.
- Other pages on the epic branch still contain the $2.5M-$5M range / "small businesses" (about-page, homepage-v2,
  solutions-page, faqs, old industries-hub). The user said they fixed these on the live site already.
- Industry pages were built from the repo's copies, not the live site — user should skim copy against live.
- Everything was validated structurally and rendered in headless Chromium only; nothing is verified in real WordPress.
