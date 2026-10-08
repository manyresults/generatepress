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
Done: Clean-Up Bookkeeping, Tax & Compliance, Internal Audit, Payroll, Industries hub, Non-Profit,
Education, Legal, Professional Services, Real Estate, Technology (bodies/<slug>_body.py ->
pacioli/industry-<slug>-paper.html). All five validate with 0 errors; rendered in headless Chromium at 1280px and 390px
with no horizontal overflow. Not yet pasted into or checked in real WordPress.
Remaining: none of the planned industry pages.

Tax checklists (added): bodies/checklists_hub_body.py -> pacioli/tax-checklists-hub-paper.html;
bodies/checklist_body.py (CL=<slug>, reads copy from pacioli/tax-checklist-<slug>.html) ->
pacioli/tax-checklist-<slug>-paper.html for 1040-schedule-c, 1065, 1120-s, 1120, 990-ez, 990.
Note: the epic-branch merge was reverted; the checklist sources (tax-checklist-<slug>.html, tax-checklists-hub.html) live on claude/epic-cori-y5x8wi only.
IRS Forms & Publications: bodies/irs_body.py + bodies/irs_data.json (list data bundled) -> pacioli/irs-forms-publications-paper.html
Tax & Payroll Registration Forms Directory: bodies/forms_dir_body.py + bodies/forms_dir_data.json -> pacioli/tax-forms-directory-paper.html (helpers: tx() now emits extra cls into the html class attr)
Footer: bodies/footer_body.py -> pacioli/footer-paper.html (copy changes: established businesses, /contact/, Clean-Up Bookkeeping + Internal Audit added to Solutions)
About page: bodies/about_body.py (rebuilt from live markup) -> pacioli/about-page-paper.html (copy fixes: no small businesses/owner/Souderton, /contact/ links, consultation image -> small badge)
Solutions page: bodies/solutions_body.py (rebuilt from live markup) -> pacioli/solutions-page-paper.html
Thank-you page: bodies/thankyou_body.py -> pacioli/thank-you-page-paper.html (booking links/iframe unchanged: Google Calendar)
Home page: bodies/home_body.py (rebuilt from live markup; In-House Advantage icons -> orange line badges; hero plane has a dashed flight trail) -> pacioli/homepage-paper.html. pacioli/cta-block-paper-trail.html = reusable CTA block (ref 51507) with the trailed plane.

CONVENTION - CTA airplane: every new bottom-of-page CTA uses `cta_plane(...)` (helpers_source.py): the plane with the dotted trail
(viewBox 0 0 64 24, dasharray 1.5 3.2), set to width 100px and height 100px, hidden below 1100px. Do not use the plain plane doodle in CTAs.
Existing pages built earlier still have the old plain plane in their CTA sections until regenerated.
