# Session handoff — Pacioli Finance "Paper Desk" rebuild

**Repo:** manyresults/generatepress · **Branch:** `claude/elegant-clarke-f7jlo6` (all work pushed; last commit `4c76d94`)
**Other branch (NOT merged, on purpose):** `claude/epic-cori-y5x8wi`. It was merged once and the merge was reverted at the
user's request. It still holds the old source files the checklist/hub generators read from
(`tax-checklist-<slug>.html`, `tax-checklists-hub.html`), the old page versions, `paper-desk-tokens.css`, the component kit,
the header/overlay/nav files and `services-template.html`. Don't merge it unless asked.
**User's work log:** Notion page "Grace site additions" (a running to-do + a "Paper Desk rebuild: log" section at the bottom).
In-repo notes: `pacioli/WORK_LOG.md`.

## Goal
Rebuild the Pacioli Finance WordPress site (GeneratePress + GenerateBlocks Pro) page by page as paste-ready block markup
for WP's Code Editor, in the "Paper Desk" style (cream paper, hard offset shadows, hand-drawn doodles, small icon badges).
Tokens (`--paper-*`) are pasted ONCE into Appearance > Customize > Additional CSS.

## Done (all in `pacioli/`, each a `-paper` file unless noted)
| Area | Files |
|---|---|
| Services | services-cleanup-bookkeeping.html, services-tax-compliance.html, services-internal-audit.html, services-payroll.html |
| Industries | industries-hub-paper, industry-{non-profit,education,legal,professional-services,real-estate,technology}-paper (7 sections, NO "Our Promise to You") |
| Tax resources | tax-checklists-hub-paper, tax-checklist-{1040-schedule-c,1065,1120,1120-s,990-ez,990}-paper, irs-forms-publications-paper, tax-forms-directory-paper |
| Site-wide | footer-paper, cta-block-paper-trail (reusable CTA, ref 51507, plane has a dotted trail) |
| Core pages | about-page-paper, solutions-page-paper, homepage-paper, thank-you-page-paper |
| Snippet | about-tape-corners-snippet.html (superseded: tape is already in about-page-paper) |

About, Solutions and Home were rebuilt from the user's LIVE markup (pasted in chat), with copy fixes. If the user pastes newer
live code again, rebuild from THAT, not from the generator bodies (the live pages have been hand-edited since).

## Not done / left alone
- Header bar (`site-header.html`) and the 4 dropdown overlay panels: restyling intentionally skipped (they work; user fixed them in the editor).
- `services-template.html` (not requested). `services-bookkeeping.html` (7-item Full Service Breakdown page) was never redone.
- `testimonials-block-paper` (ref 51469) unchanged.
- CTA sections of the earlier generated pages (4 services pages, 5 industry pages, checklists, thank-you, etc.) still use the OLD plain plane.
  Only Professional Services (and the CTA pattern file) use the standard plane. Regenerate the others if asked (`cta_plane()`).
- Nothing was verified in real WordPress; everything was validated and rendered in headless Chromium only.

## Live-site fixes the user made in the editor (no repo change needed)
- Industries panel: "Trade" renamed to "Professional Services".
- Mega menu: "Book a Call" pill set to Justify Self: End; Contact/Resources panels had been switched from "mega menu" to "standard" type
  (fixed by switching back); panels unparented; Width Mode: Full Width fixed the mobile layout.
- Header: Navigation block (Site Header > Navigation > logo, menu toggle, menu container) has Max Width 1400 (global) with no centering.
  Fix given: set Navigation Margin Left/Right to auto. Client reported header pinned left on wide screens. Not yet confirmed fixed.
- Mobile menu: bottom two buttons (Upload Portal, Book a Call) need a flex wrapper, Justify Content center, on the tablet breakpoint. Not yet confirmed.

## Open items for the user
- Ask Dan and Amanda about the home page solutions boxes and whether Payroll should be centered (in the Notion to-do).
- Re-check the About page icons (Notion to-do). The paper-clip path was fixed repo-wide (old one was cut off at the bottom of its 24x24
  box); live pages built earlier still show the old clip until re-pasted.
- Industry pages were built from repo copies, not the live site: skim copy against live.
- Home page still has some old-plane CTAs via reusable block 51507 until `cta-block-paper-trail.html` is pasted into it.
- Staging links (`danj19.sg-host.com`) remain only in `cta-block-paper-trail.html` and the thank-you page's calendar URLs; Dan said links auto-change at launch.

## Generator (`pacioli/tools/paper-desk-generator/`)
- `python3 -I build.py bodies/<page>_body.py > ../../<out>.html`; for checklists: `CL=<slug> python3 -I build.py bodies/checklist_body.py`.
  **Never redirect straight onto the final file** when a build could fail: a failed build truncates it (this pushed six empty files once).
  Build to the scratchpad first, validate, then copy.
- `python3 -I validate.py <out>.html` must say `errors 0` (block JSON, wp: nesting, HTML balance, duplicate ids, raw `&`, `--paper-*` tokens).
- `shot.py` renders with headless Chromium (`pip install playwright` once; do NOT run `playwright install`; Chromium is at /opt/pw-browsers/chromium;
  set PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1). Layout check only; it can't run GB Pro accordions or query loops.
- Bodies: np, education, legal, professional-services, real-estate, technology, hub, tax, audit, payroll, checklist_body, checklists_hub_body,
  irs_body (+irs_data.json), forms_dir_body (+forms_dir_data.json), footer_body, about_body, solutions_body, home_body, thankyou_body.
  Clean-Up Bookkeeping's body is the tail of `helpers_source.py`.
- Helpers: `section, eyebrow, h2, para, btn, badge, dot_row, col, doodle, acc_item, tx/el/sh/blk, cta_plane`. Use `AMPSEMI` for `&amp;`; never type a raw `&` in JSON.
  `tx(..., cls='gb-text extra')` now writes extra classes into the HTML class attribute.
- GB editor gotcha: the editor REGENERATES CSS from block settings. Use only GB-style settings (plain properties inside `@media`, `svg` at the top level of
  `styles`). Nested `svg` inside `@media` made the editor drop a shape's styling. Size shapes via the block `width`, SVG at `width:100%`.

## CLIENT RULES (apply to every page)
- Never say "owner" for Pacioli's owner. CMA line: "Overseen by a Certified Management Accountant (CMA)" / "Controller-level oversight from…".
  No Souderton, PA location.
- No client-count figures. No revenue range ($2.5M-$5M) anywhere; not "small businesses": "established businesses", nationwide.
- No large raster images/big icons in heroes or feature grids (small icon badges only). Corner doodles hide < 1100px.
- Keep the page's own copy, links and anchors; fix typos and say so.
- Trade is now Professional Services (`/industries/professional-services/`).
- Hero/CTA buttons go to `/contact/` (relative). Thank-you page keeps its Google Calendar booking links.
- Industry pages: NO "Our Promise to You" section (client removed it; only the Industries hub keeps one).
- Every new bottom-of-page CTA uses `cta_plane()`: plane with dotted trail, svg 64x24, width and height 100px, hides < 1100px.

## HOW TO PASTE (this caused most of the "bugs")
1. Open the file on GitHub -> **Copy raw file**. NEVER copy from the chat or a file viewer: it strips `<!-- wp:... -->` block comments and the page renders unstyled.
2. WP page -> three-dot menu -> **Code editor** -> Cmd+A -> paste -> **Update** straight from the Code Editor (not the visual editor: "Attempt recovery" rewrites blocks).
3. Hard-refresh the live page (stale cache caused false "bugs").
4. WP rewrites `--` to `--` on save; that's normal.
