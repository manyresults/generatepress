# Fix-It Buddy — design system notes

Source: `generatepress-settings.json` (GeneratePress export) + the Basement Remodeling page block markup.

## Global colors (use as `var(--slug)`)
| slug | hex | typical use |
|---|---|---|
| contrast | #08090a | body text, text on yellow buttons |
| contrast-2 | #06132e | headings, links |
| contrast-3 | #092347 | link hover, step-number chips |
| base / base-2 / base-3 | #e6effa / #F2F7Fa / #ffffff | tints, cards, white |
| accent / accent-2 / accent-3 | #07377a / #094a9e / #0d64d6 | blue sections |
| global-color-10 | #F2BE1F | primary CTA (yellow) |
| global-color-11 | #193156 | icon color in feature cards |
| global-color-12 | #DB3A3D | CTA hover (red) |
| background-color | #f7f7f7 | alternating section background |

## Type
Headings Montserrat 700; body Inter 1.125rem / 1.5em. Container width 1200 (`--gb-container-width`). Hide-title is on.

## Page pattern (GenerateBlocks v2 `generateblocks/element` + `text`)
1. Hero — 2 col (copy+bullets+CTAs+rating card | image + service card); bg `--background-color`
2. Pain points — "You may be dealing with:" stacked cards, tag icon, closing callout (bg `--base-2`), CTA
3. Process — numbered 5-step cards + 4 benefit cards (icon, title, text), CTA
4. Quote — `--accent` bg, copy+checklist left, white form card right (`#quote`, Gravity Forms id 4)
5. Trust — "Why people choose" 2x2 icon cards
6. Service area — town pill links, "don't see your town" line, CTA
7. Reviews — `[trustindex no-registration=google]`
8. FAQ — GenerateBlocks Pro accordion
9. Final CTA — fixed-bg image with 51% black overlay, outlined button

Section padding: 100px desktop / 70px 20px tablet / 50px 20px mobile.
Phone: (856) 644-3030 (`tel:+1856443030`). Buttons: 30px radius, 15px 30px padding, 16px/600.
