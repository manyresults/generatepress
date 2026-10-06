# Paper Desk page generator (handoff)

Generates paste-ready GenerateBlocks / GenerateBlocks Pro block markup for the Pacioli site,
styled with the "Paper Desk" tokens (`tok.css`, pasted once into WP Additional CSS).

## Use
    python3 -I build.py bodies/np_body.py > industry-non-profit.html
    python3 -I validate.py industry-non-profit.html     # block JSON, nesting, html balance, dup ids, tokens
`bodies/np_body.py` is the template for an industry page (hero card, dark pain section, 4 cards,
free-review note card, trust, promise, 2 quotes, closing CTA). Other bodies: tax, audit, payroll, hub.
The Clean-Up Bookkeeping page body is the tail of `helpers_source.py` (after the `# 1. HERO` banner).

## House rules (client requirements)
- Never say "owner" for Pacioli's owner. CMA line: "Overseen by a Certified Management Accountant (CMA)."
- No client-count figures ("16-20 active clients"). Use: "the same ... process we give every client relationship we take on."
- No revenue range ($2.5M-$5M) anywhere. Do not call clients "small businesses"; say established businesses / nationwide.
- No large raster images or big icons in heroes/feature grids: small icon badges only. Corner doodles hide below 1100px.
- Keep the page's own copy, links and anchors; fix duplicate anchors/typos and mention them.
- Escape like WordPress does: `&` -> `&` in block JSON, `&amp;` in text (helpers do this; use `AMPSEMI`).

## Workflow gotchas
- COPYING FROM CHAT CORRUPTS BLOCK COMMENTS. Always paste into WP from GitHub "Copy raw file", into the
  Code Editor, and Update without switching to the visual editor first ("Attempt recovery" rewrites blocks).
- GB Pro accordion: item/toggle/toggle-icon/content structure is copied from the original markup (see `acc_item`).
- Rendering check: Playwright + /opt/pw-browsers/chromium; inject tok.css (strip the @import) + every block's `css`.

## Status (branch claude/elegant-clarke-f7jlo6)
Done: Clean-Up Bookkeeping, Tax & Compliance, Internal Audit, Payroll, Industries hub, Non-Profit.
Remaining: Education, Legal, Professional Services, Real Estate, Technology (sources are on
origin/claude/epic-cori-y5x8wi: pacioli/industry-*.html).
