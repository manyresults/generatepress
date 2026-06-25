# Block Library

Reusable GenerateBlocks patterns from the 3P Allies / ManyResults sites. Copy-paste into new pages and update uniqueIds, text, links, and images.

---

## Table of Contents

1. [Hero – Gradient Background with Split Layout](#hero--gradient-background-with-split-layout)
2. [Section Banner – Overlay Text Card](#section-banner--overlay-text-card)
3. [Tagline with Underline](#tagline-with-underline)
4. [Tagline with Star Icon](#tagline-with-star-icon)
5. [Shadow Card with Icon](#shadow-card-with-icon)
6. [Icon Grid – 2x2 with Circle Icons](#icon-grid--2x2-with-circle-icons)
7. [CTA Button – Pill Style with Arrow](#cta-button--pill-style-with-arrow)
8. [CTA Button – Shadow/Offset Style](#cta-button--shadowoffset-style)
9. [Split Layout – Image Left, Text Right](#split-layout--image-left-text-right)
10. [Split Layout – Text Left, Image Right](#split-layout--text-left-image-right)
11. [Reusable Block Reference (Divider/Separator)](#reusable-block-reference)
12. [Horizontal Divider Line Icon](#horizontal-divider-line-icon)

---

## Hero – Gradient Background with Split Layout

Full-width hero with gradient overlay, background image, left text column, and right image/content column. Used on the home page and Movement Blueprint.

```html
<!-- wp:generateblocks/container {"uniqueId":"HERO-OUTER","gradient":true,"gradientDirection":299,"gradientColorOne":"var(--global-color-8)","gradientColorTwo":"var(--global-color-8)","bgImage":{"id":"","image":{"url":"YOUR-BG-IMAGE-URL","height":600,"width":1050,"orientation":"landscape"}},"bgOptions":{"selector":"pseudo-element","opacity":0.45,"overlay":false,"position":"center bottom","size":"cover","repeat":"no-repeat","attachment":""},"isDynamic":true,"blockVersion":4,"position":"relative","overflowX":"hidden","overflowY":"hidden","sizing":{"height":"","maxWidth":""},"spacing":{"marginTop":""}} -->
<!-- wp:generateblocks/container {"uniqueId":"HERO-INNER","isDynamic":true,"blockVersion":4,"display":"flex","flexDirectionMobile":"column","columnGap":"80px","columnGapTablet":"40px","rowGapMobile":"60px","position":"relative","sizing":{"maxWidth":"","heightTablet":"","height":""},"useGlobalMaxWidth":true,"spacing":{"paddingTop":"100px","paddingRight":"40px","paddingBottom":"100px","paddingLeft":"40px","marginRight":"auto","marginLeft":"auto","paddingTopTablet":"80px","paddingBottomTablet":"80px","paddingRightMobile":"30px","paddingLeftMobile":"30px"}} -->
<!-- wp:generateblocks/container {"uniqueId":"HERO-TEXT","isDynamic":true,"blockVersion":4,"position":"relative","sizing":{"width":"50%","widthMobile":"100%","height":"100%","maxWidth":"","heightTablet":""}} -->

<!-- INSERT: Tagline (h6), Headline (h1), Divider, Description (p), CTA Button -->

<!-- /wp:generateblocks/container -->

<!-- wp:generateblocks/container {"uniqueId":"HERO-IMG","bgImage":null,"bgOptions":{"selector":"element","opacity":1,"overlay":false,"position":"top center","size":"cover","repeat":"no-repeat","attachment":""},"removeVerticalGapMobile":true,"isDynamic":true,"blockVersion":4,"display":"flex","flexDirection":"column","sizing":{"width":"50%","widthMobile":"100%","minHeight":"","minHeightTablet":"","minHeightMobile":"300px","height":"","maxWidth":"","heightTablet":""},"borders":{"borderTopLeftRadius":"10px","borderTopRightRadius":"10px","borderBottomLeftRadius":"10px","borderBottomRightRadius":"10px"},"className":"box-shadow"} -->
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","className":"is-style-default"} -->
<figure class="wp-block-image size-large is-style-default"><img src="YOUR-IMAGE-URL" alt="YOUR-ALT-TEXT"/></figure>
<!-- /wp:image -->
<!-- /wp:generateblocks/container -->
<!-- /wp:generateblocks/container -->
<!-- /wp:generateblocks/container -->
```

---

## Section Banner – Overlay Text Card

Dark background with fixed image, offset text card with right border accent. Used for "The Journey Ahead" and "4-Step Plan" intros.

```html
<!-- wp:generateblocks/container {"uniqueId":"BANNER-OUTER","gradientDirection":90,"gradientColorOne":"rgba(255, 255, 255, 0.1)","gradientColorOneOpacity":1,"gradientColorStopOne":0,"gradientColorTwo":"rgba(0, 0, 0, 0.30)","bgImage":{"id":"","image":{"url":"YOUR-BG-IMAGE-URL","height":829,"width":1207,"orientation":"landscape"}},"bgOptions":{"selector":"pseudo-element","opacity":0.84,"overlay":false,"position":"bottom right","size":"1160px","repeat":"no-repeat","attachment":"fixed"},"isDynamic":true,"blockVersion":4,"position":"relative","overflowX":"hidden","overflowY":"hidden","sizing":{"height":"","maxWidth":""}} -->
<!-- wp:generateblocks/container {"uniqueId":"BANNER-INNER","isDynamic":true,"blockVersion":4,"sizing":{"maxWidth":""},"useGlobalMaxWidth":true,"spacing":{"paddingTop":"120px","paddingRight":"20px","paddingBottom":"120px","paddingLeft":"20px","marginRight":"auto","marginLeft":"auto","paddingTopMobile":"80px","paddingRightMobile":"20px","paddingBottomMobile":"120px","paddingLeftMobile":"20px"}} -->
<!-- wp:generateblocks/container {"uniqueId":"BANNER-CARD","backgroundColor":"var(--base-3)","gradientColorOneOpacity":1,"gradientColorStopOne":40,"gradientColorTwoOpacity":1,"gradientColorStopTwo":40,"isDynamic":true,"blockVersion":4,"display":"inline-flex","flexDirection":"column","alignItems":"flex-start","position":"relative","sizing":{"width":"75%","widthTablet":"75%","widthMobile":"100%","height":"","maxWidth":""},"spacing":{"paddingTop":"50px","paddingRight":"50px","paddingBottom":"30px","paddingLeft":"20px","marginLeft":"-20px","paddingTopTablet":"40px","paddingRightTablet":"40px","paddingBottomTablet":"20px","paddingLeftTablet":"40px","paddingTopMobile":"30px","paddingRightMobile":"30px","paddingBottomMobile":"10px","paddingLeftMobile":"30px"},"borders":{"borderRightWidth":"3px","borderRightStyle":"solid","borderRightColor":"var(--global-color-8)","borderTopRightRadius":"10px","borderBottomRightRadius":"10px"}} -->

<!-- INSERT: Headline (h1), Divider, Description (p) -->

<!-- /wp:generateblocks/container -->
<!-- /wp:generateblocks/container -->
<!-- /wp:generateblocks/container -->
```

---

## Tagline with Underline

Uppercase tagline with bottom border accent. Used to label sections.

```html
<!-- wp:generateblocks/headline {"uniqueId":"TAGLINE","element":"p","blockVersion":3,"display":"inline-flex","alignItems":"center","columnGap":"0.5em","sizing":{"width":""},"typography":{"fontSize":"18px","fontWeight":"700","textTransform":"uppercase"},"spacing":{"paddingBottom":"6px","marginBottom":"16px"},"borders":{"borderBottomWidth":"2px","borderBottomStyle":"solid","borderTopRightRadius":"4px","borderBottomRightRadius":"4px","borderBottomLeftRadius":"4px","borderTopLeftRadius":"4px"},"textColor":"var(--accent)"} -->
<p class="gb-headline gb-headline-TAGLINE gb-headline-text">YOUR TAGLINE TEXT</p>
<!-- /wp:generateblocks/headline -->
```

---

## Tagline with Star Icon

Same as above but with a star icon before the text.

```html
<!-- wp:generateblocks/headline {"uniqueId":"TAGLINE-STAR","element":"p","blockVersion":3,"display":"inline-flex","alignItems":"center","columnGap":"0.5em","sizing":{"width":""},"typography":{"fontSize":"18px","fontWeight":"700","textTransform":"uppercase"},"spacing":{"paddingBottom":"6px","marginBottom":"16px"},"borders":{"borderBottomWidth":"2px","borderBottomStyle":"solid","borderTopRightRadius":"4px","borderBottomRightRadius":"4px","borderBottomLeftRadius":"4px","borderTopLeftRadius":"4px"},"textColor":"var(--accent)","hasIcon":true,"iconStyles":{"width":"1em","height":"1em","paddingRight":"0.8em"}} -->
<p class="gb-headline gb-headline-TAGLINE-STAR"><span class="gb-icon"><svg aria-hidden="true" role="img" height="1em" width="1em" viewBox="0 0 576 512" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"></path></svg></span><span class="gb-headline-text">YOUR TAGLINE TEXT</span></p>
<!-- /wp:generateblocks/headline -->
```

---

## Shadow Card with Icon

Rounded card with icon badge, heading, and description. Used for SACRED elements, journey steps, etc.

```html
<!-- wp:generateblocks/container {"uniqueId":"CARD","backgroundColor":"var(--base-3)","isDynamic":true,"blockVersion":4,"display":"flex","flexDirectionMobile":"column","alignItems":"flex-start","alignItemsMobile":"center","columnGap":"20px","flexGrowTablet":1,"flexShrinkTablet":1,"sizing":{"widthTablet":"45%","widthMobile":"100%"},"spacing":{"paddingTop":"20px","paddingLeft":"20px","paddingRight":"20px","paddingBottom":"20px","paddingLeftMobile":"10px","paddingRightMobile":"10px"},"borders":{"borderTopLeftRadius":"10px","borderTopRightRadius":"10px","borderBottomLeftRadius":"10px","borderBottomRightRadius":"10px"},"className":"shadow"} -->
<!-- wp:generateblocks/headline {"uniqueId":"CARD-ICON","element":"div","blockVersion":3,"display":"flex","alignItems":"center","columnGap":"0.5em","spacing":{"paddingTop":"10px","paddingLeft":"10px","paddingRight":"10px","paddingBottom":"10px"},"borders":{"borderTopLeftRadius":"10px","borderTopRightRadius":"10px","borderBottomLeftRadius":"10px","borderBottomRightRadius":"10px"},"backgroundColor":"var(--base-2)","hasIcon":true,"iconColor":"var(--base)","removeText":true,"iconStyles":{"height":"2.5em","width":"2.5em"}} -->
<div class="gb-headline gb-headline-CARD-ICON"><span class="gb-icon">
<!-- INSERT YOUR SVG ICON HERE -->
</span></div>
<!-- /wp:generateblocks/headline -->

<!-- wp:generateblocks/container {"uniqueId":"CARD-TEXT","isDynamic":true,"blockVersion":4} -->
<!-- wp:generateblocks/headline {"uniqueId":"CARD-H","element":"h4","blockVersion":3,"typography":{"fontWeight":"600","textAlignMobile":"center"},"spacing":{"marginBottom":"10px"}} -->
<h4 class="gb-headline gb-headline-CARD-H gb-headline-text"><strong>YOUR HEADING</strong></h4>
<!-- /wp:generateblocks/headline -->

<!-- wp:generateblocks/headline {"uniqueId":"CARD-P","element":"p","blockVersion":3,"spacing":{"marginBottom":"0px"}} -->
<p class="gb-headline gb-headline-CARD-P gb-headline-text">YOUR DESCRIPTION TEXT</p>
<!-- /wp:generateblocks/headline -->
<!-- /wp:generateblocks/container -->
<!-- /wp:generateblocks/container -->
```

---

## Icon Grid – 2x2 with Circle Icons

Four items in a 2x2 grid, each with a circular accent icon. Used for "Why Work Together?" sections.

```html
<!-- wp:generateblocks/container {"uniqueId":"GRID-WRAP","backgroundColor":"var(--base)","isDynamic":true,"blockVersion":4,"spacing":{"paddingTop":"30px","paddingRight":"30px","paddingBottom":"30px","paddingLeft":"30px","paddingRightMobile":"20px","paddingLeftMobile":"20px"},"borders":{"borderTopRightRadius":"8px","borderBottomRightRadius":"8px","borderBottomLeftRadius":"8px","borderTopLeftRadius":"8px"}} -->
<!-- wp:generateblocks/grid {"uniqueId":"GRID","columns":4,"horizontalGap":40,"verticalGap":60,"isDynamic":true,"blockVersion":3} -->

<!-- REPEAT THIS BLOCK 4x, changing uniqueIds, icon SVG, heading, and text: -->
<!-- wp:generateblocks/container {"uniqueId":"GRID-ITEM-1","isGrid":true,"gridId":"GRID","isDynamic":true,"blockVersion":4,"display":"flex","alignItems":"flex-start","columnGap":"15px","sizing":{"width":"50%","widthMobile":"100%","widthTablet":"100%"},"borders":{"borderBottomWidth":"0px","borderBottomStyle":"solid"}} -->
<!-- wp:generateblocks/headline {"uniqueId":"GRID-ITEM-1-ICON","element":"div","blockVersion":3,"display":"flex","alignItems":"center","columnGap":"0.5em","spacing":{"paddingTop":"15px","paddingRight":"15px","paddingBottom":"15px","paddingLeft":"15px"},"borders":{"borderTopRightRadius":"50%","borderBottomRightRadius":"50%","borderBottomLeftRadius":"50%","borderTopLeftRadius":"50%"},"backgroundColor":"var(--accent-2)","hasIcon":true,"iconColor":"var(--accent)","removeText":true,"iconStyles":{"width":"1.4em","height":"1.4em","paddingRight":"0.5em"}} -->
<div class="gb-headline gb-headline-GRID-ITEM-1-ICON"><span class="gb-icon">
<!-- YOUR SVG ICON -->
</span></div>
<!-- /wp:generateblocks/headline -->

<!-- wp:generateblocks/container {"uniqueId":"GRID-ITEM-1-TEXT","isDynamic":true,"blockVersion":4} -->
<!-- wp:generateblocks/headline {"uniqueId":"GRID-ITEM-1-H","element":"h3","blockVersion":3,"typography":{"fontSize":"20px","textTransform":"capitalize","fontSizeMobile":"19px"},"spacing":{"marginBottom":"10px"}} -->
<h3 class="gb-headline gb-headline-GRID-ITEM-1-H gb-headline-text">YOUR HEADING</h3>
<!-- /wp:generateblocks/headline -->

<!-- wp:generateblocks/headline {"uniqueId":"GRID-ITEM-1-P","element":"p","blockVersion":3,"spacing":{"marginBottom":"0px"}} -->
<p class="gb-headline gb-headline-GRID-ITEM-1-P gb-headline-text">YOUR DESCRIPTION</p>
<!-- /wp:generateblocks/headline -->
<!-- /wp:generateblocks/container -->
<!-- /wp:generateblocks/container -->

<!-- /wp:generateblocks/grid -->
<!-- /wp:generateblocks/container -->
```

---

## CTA Button – Pill Style with Arrow

Rounded pill button with right arrow icon. Used in hero and CTA sections.

```html
<!-- wp:generateblocks/button {"uniqueId":"CTA-PILL","hasUrl":true,"target":false,"blockVersion":4,"display":"inline-flex","alignItems":"center","justifyContent":"center","typography":{"fontFamily":"Niramit","fontWeight":"700","textAlign":"center"},"fontFamilyFallback":"sans-serif","googleFontVariants":"200, 200italic, 300, 300italic, regular, italic, 500, 500italic, 600, 600italic, 700, 700italic","spacing":{"paddingTop":"14px","paddingRight":"30px","paddingBottom":"14px","paddingLeft":"30px","marginTop":"40px"},"borders":{"borderTopRightRadius":"9999px","borderBottomRightRadius":"9999px","borderBottomLeftRadius":"9999px","borderTopLeftRadius":"9999px"},"backgroundColor":"var(--contrast)","backgroundColorHover":"var(--accent)","textColor":"var(--base-4)","textColorHover":"var(--base-4)","hasIcon":true,"iconLocation":"right","iconPaddingRight":"","iconStyles":{"width":"1em","height":"1em","paddingLeft":"1em"},"className":"smooth-scroll"} -->
<a class="gb-button gb-button-CTA-PILL smooth-scroll" href="YOUR-URL"><span class="gb-button-text">YOUR BUTTON TEXT</span><span class="gb-icon"><svg viewBox="0 0 16 16" class="bi bi-arrow-right" height="16" width="16" xmlns="http://www.w3.org/2000/svg">   <path d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"></path> </svg></span></a>
<!-- /wp:generateblocks/button -->
```

---

## CTA Button – Shadow/Offset Style

Button with border and shadow offset effect. Used in about sections and takeaways.

```html
<!-- wp:generateblocks/container {"uniqueId":"BTN-WRAP","backgroundColor":"var(--contrast-2)","isDynamic":true,"blockVersion":4,"variantRole":"button-container","display":"inline-block","spacing":{"marginTop":"20px"},"borders":{"borderTopRightRadius":"8px","borderBottomRightRadius":"8px","borderBottomLeftRadius":"8px","borderTopLeftRadius":"8px"}} -->
<!-- wp:generateblocks/button {"uniqueId":"BTN","hasUrl":true,"blockVersion":4,"display":"inline-flex","typography":{"fontWeight":"700","textTransform":"uppercase"},"spacing":{"paddingTop":"12px","paddingRight":"34px","paddingBottom":"12px","paddingLeft":"34px","marginTop":"-4px","marginRight":"3px","marginBottom":"4px","marginLeft":"-3px"},"borders":{"borderTopWidth":"2px","borderTopStyle":"solid","borderTopColor":"var(--contrast-2)","borderRightWidth":"2px","borderRightStyle":"solid","borderRightColor":"var(--contrast-2)","borderBottomWidth":"2px","borderBottomStyle":"solid","borderBottomColor":"var(--contrast-2)","borderLeftWidth":"2px","borderLeftStyle":"solid","borderLeftColor":"var(--contrast-2)","borderTopRightRadius":"8px","borderBottomRightRadius":"8px","borderBottomLeftRadius":"8px","borderTopLeftRadius":"8px"},"backgroundColor":"var(--base-2)","backgroundColorHover":"var(--base)","textColor":"var(--base)","textColorHover":"var(--base-2)"} -->
<a class="gb-button gb-button-BTN gb-button-text" href="YOUR-URL">YOUR BUTTON TEXT</a>
<!-- /wp:generateblocks/button -->
<!-- /wp:generateblocks/container -->
```

---

## Split Layout – Image Left, Text Right

Two-column layout with image on the left, text content on the right. Used for about/bio sections.

```html
<!-- wp:generateblocks/container {"uniqueId":"SPLIT-LR","isDynamic":true,"blockVersion":4,"display":"flex","flexDirectionMobile":"column","columnGap":"40px","rowGapMobile":"60px","position":"relative","zindex":1,"useGlobalMaxWidth":true,"spacing":{"paddingTop":"80px","paddingRight":"40px","paddingBottom":"80px","paddingLeft":"40px","marginRight":"auto","marginLeft":"auto","paddingTopMobile":"60px","paddingRightMobile":"20px","paddingBottomMobile":"60px","paddingLeftMobile":"20px"}} -->
<!-- wp:generateblocks/container {"uniqueId":"SPLIT-LR-IMG","isDynamic":true,"blockVersion":4,"sizing":{"width":"50%","widthTablet":"","widthMobile":"100%"}} -->
<!-- wp:generateblocks/image {"uniqueId":"SPLIT-LR-PHOTO","sizeSlug":"full","height":"600px","objectFit":"contain","blockVersion":2} -->
<figure class="gb-block-image gb-block-image-SPLIT-LR-PHOTO"><img class="gb-image gb-image-SPLIT-LR-PHOTO" src="YOUR-IMAGE-URL" alt="YOUR-ALT-TEXT"/></figure>
<!-- /wp:generateblocks/image -->
<!-- /wp:generateblocks/container -->

<!-- wp:generateblocks/container {"uniqueId":"SPLIT-LR-TEXT","isDynamic":true,"blockVersion":4,"sizing":{"width":"50%","widthTablet":"","widthMobile":"100%"}} -->

<!-- INSERT: Tagline, Headline, Paragraphs, CTA Button -->

<!-- /wp:generateblocks/container -->
<!-- /wp:generateblocks/container -->
```

---

## Split Layout – Text Left, Image Right

Same as above but text on left, image on right. Used for takeaways sections.

```html
<!-- wp:generateblocks/container {"uniqueId":"SPLIT-RL","isDynamic":true,"blockVersion":4,"display":"flex","flexDirectionMobile":"column","columnGap":"40px","rowGapMobile":"60px","position":"relative","zindex":1,"useGlobalMaxWidth":true,"spacing":{"paddingTop":"80px","paddingRight":"40px","paddingBottom":"80px","paddingLeft":"40px","marginRight":"auto","marginLeft":"auto","paddingTopMobile":"60px","paddingRightMobile":"20px","paddingBottomMobile":"60px","paddingLeftMobile":"20px"}} -->
<!-- wp:generateblocks/container {"uniqueId":"SPLIT-RL-TEXT","isDynamic":true,"blockVersion":4,"sizing":{"width":"60%","widthTablet":"","widthMobile":"100%"}} -->

<!-- INSERT: Tagline, Headline, Paragraphs, List, CTA Button -->

<!-- /wp:generateblocks/container -->

<!-- wp:generateblocks/container {"uniqueId":"SPLIT-RL-IMG","isDynamic":true,"blockVersion":4,"sizing":{"widthTablet":"","width":"40%","widthMobile":"100%"}} -->
<!-- wp:generateblocks/image {"uniqueId":"SPLIT-RL-PHOTO","sizeSlug":"full","objectFit":"contain","blockVersion":2} -->
<figure class="gb-block-image gb-block-image-SPLIT-RL-PHOTO"><img class="gb-image gb-image-SPLIT-RL-PHOTO" src="YOUR-IMAGE-URL" alt="YOUR-ALT-TEXT"/></figure>
<!-- /wp:generateblocks/image -->
<!-- /wp:generateblocks/container -->
<!-- /wp:generateblocks/container -->
```

---

## Reusable Block Reference

Inserts a reusable block (e.g., divider/separator). Block ID 43859 is the current site divider.

```html
<!-- wp:block {"ref":43859} /-->
```

---

## Horizontal Divider Line Icon

Small horizontal line used as a visual separator within text sections.

```html
<!-- wp:generateblocks/headline {"uniqueId":"DIVIDER","element":"div","blockVersion":3,"display":"flex","flexDirection":"column","typography":{"fontSize":"20px"},"spacing":{"marginBottom":"10px"},"hasIcon":true,"iconColor":"var(--global-color-8)","iconLocation":"above","iconPaddingRight":"","removeText":true,"iconStyles":{"width":"1.4em","height":"1.4em","paddingBottom":"0.5em"}} -->
<div class="gb-headline gb-headline-DIVIDER"><span class="gb-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36.7 3"><path d="M0 0h36.7v3H0z"></path></svg></span></div>
<!-- /wp:generateblocks/headline -->
```

---

## Icon Library

Common SVG icons used across the site. Reference by name when building cards.

| Name | Usage | SVG |
|------|-------|-----|
| **Star** | Taglines, awards | `<svg viewBox="0 0 576 512"><path fill="currentColor" d="M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z"></path></svg>` |
| **People Group** | Affiliation, community | `<svg viewBox="0 0 640 512"><path d="M184 88C184 118.9..."></path></svg>` (full SVG in card examples) |
| **Bullseye** | Goals, targeting | `<svg viewBox="0 0 16 16" class="bi bi-bullseye" fill="currentColor"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"></path><path d="M8 13A5 5 0 1 1 8 3a5 5 0 0 1 0 10zm0 1A6 6 0 1 0 8 2a6 6 0 0 0 0 12z"></path><path d="M8 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm0 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"></path><path d="M9.5 8a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"></path></svg>` |
| **Award/Badge** | Success, credentials | `<svg viewBox="0 0 384 512"><path fill="currentColor" d="M97.12 362.63..."></path></svg>` (full SVG in card examples) |
| **Map** | Collaboration, planning | `<svg viewBox="0 0 576 512"><path d="M565.6 36.2..."></path></svg>` (full SVG in card examples) |
| **Arrows Move** | Action, movement | `<svg viewBox="0 0 16 16" class="bi bi-arrows-move" fill="currentColor"><path d="M7.646.146a.5.5 0 0 1 .708 0l2 2..." fill-rule="evenodd"></path></svg>` |
| **Clipboard Search** | Research, assessment | `<svg stroke-linejoin="round" stroke-linecap="round" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">...</svg>` (full SVG in card examples) |
| **Arrow Right** | CTA buttons | `<svg viewBox="0 0 16 16" class="bi bi-arrow-right"><path d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"></path></svg>` |
| **Rocket** | Launch, initiative | `<svg viewBox="0 0 256 256"><path d="M96.6,177a7.9..."></path><path d="M227.6,41.8..."></path></svg>` (full SVG in card examples) |
| **Layout/Grid** | Planning, structure | `<svg fill="none" viewBox="0 0 48 48"><rect stroke-linejoin="round" stroke-linecap="round" stroke-width="1" stroke="#333" rx="3" height="36" width="36" y="6" x="6"></rect>...</svg>` (full SVG in card examples) |

---

## CSS Custom Properties Reference

These are the theme color variables used throughout:

| Variable | Purpose |
|----------|---------|
| `--base` | Primary dark text/fills |
| `--base-2` | Secondary background |
| `--base-3` | Card/light backgrounds |
| `--base-4` | Lightest text (on dark bg) |
| `--accent` | Primary accent color |
| `--accent-2` | Light accent (icon circles) |
| `--contrast` | Dark contrast text |
| `--contrast-2` | Dark contrast backgrounds |
| `--contrast-3` | Border/subtle contrast |
| `--global-color-8` | Brand gradient color |
| `--gb-container-width` | Max container width |
