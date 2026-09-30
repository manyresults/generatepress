#!/usr/bin/env python3
"""Generate GenerateBlocks markup for Beer-A-Rama "<Brand> in Levittown, PA" pages.

Outputs:
  <slug>.html                     brand page (embeds the synced location pattern)
  beerarama-location-block.html   synced pattern: map + hours + CTA + LiquorStore schema

Usage: python3 build_brand_page.py
Edit BRAND at the bottom (or load brands from CSV later) to add more pages.
"""
import json
import re

PHONE_DISPLAY = "215-946-3480"
PHONE_TEL = "+215-946-3480"
DIRECTIONS = "https://www.google.com/maps/dir/?api=1&destination=Beer-A-Rama+Levittown+PA"
HUB_URL = "https://beerarama.com/beer-distributor-in-levittown-pa/"
MAP_EMBED = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3049.880897538602!2d-74.82160414883126"
             "!3d40.14493667929643!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c1505481c93eb3"
             "%3A0xd77cbeedbf653b90!2sBeer-A-Rama!5e0!3m2!1sen!2sus!4v1599666576957!5m2!1sen!2sus")
HOURS = [("Sunday", "10AM – 5PM"), ("Monday – Thursday", "9AM – 8PM"), ("Friday – Saturday", "9AM – 9PM")]

ICONS = {
    "people": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle r="4" cy="7" cx="9"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>',
    "snow": '<line y2="21" x2="12" y1="3" x1="12"></line><line y2="16.5" x2="19.8" y1="7.5" x1="4.2"></line><line y2="7.5" x2="19.8" y1="16.5" x1="4.2"></line>',
    "drop": '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line y2="6" x2="21" y1="6" x1="3"></line><path d="M16 10a4 4 0 0 1-8 0"></path>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle r="3" cy="10" cx="12"></circle>',
    "clock": '<circle r="10" cy="12" cx="12"></circle><polyline points="12 6 12 12 16 14"></polyline>',
}


class Ids:
    def __init__(self, prefix):
        self.prefix, self.n = prefix, 0

    def next(self):
        self.n += 1
        return f"{self.prefix}{self.n:02d}"


def kebab(k):
    return re.sub(r"([A-Z])", lambda m: "-" + m.group(1).lower(), k)


def decls(d):
    return ";".join(f"{kebab(k)}:{v}" for k, v in d.items() if not isinstance(v, dict))


def make_css(cls, styles):
    out = [f".{cls}{{{decls(styles)}}}"]
    for k, v in styles.items():
        if not isinstance(v, dict):
            continue
        if k.startswith("@"):
            out.append(f"{k}{{.{cls}{{{decls(v)}}}}}")
        elif k.startswith("&"):
            out.append(f".{cls}{k[1:]}{{{decls(v)}}}")
        else:
            out.append(f".{cls} {k}{{{decls(v)}}}")
    return "".join(out)


def jdump(o):
    s = json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    return (s.replace("--", "\\u002d\\u002d").replace("&", "\\u0026")
             .replace("<", "\\u003c").replace(">", "\\u003e"))


def attrs_html(h):
    return "".join(f' {k}="{v.replace("&", "&amp;")}"' for k, v in h.items())


class Builder:
    def __init__(self, prefix):
        self.ids = Ids(prefix)

    def el(self, styles, children="", tag="div", align=False, html_attrs=None):
        uid = self.ids.next()
        cls = f"gb-element-{uid}"
        a = {"uniqueId": uid, "tagName": tag, "styles": styles, "css": make_css(cls, styles)}
        if align:
            a["align"] = "full"
        if html_attrs:
            a["htmlAttributes"] = html_attrs
        a["className"] = "gb-element alignfull" if align else "gb-element"
        c = f"{cls} gb-element" + (" alignfull" if align else "")
        return (f"<!-- wp:generateblocks/element {jdump(a)} -->\n<{tag}{attrs_html(html_attrs or {})} class=\"{c}\">"
                f"{children}</{tag}>\n<!-- /wp:generateblocks/element -->\n\n")

    def text(self, tag, styles, content, html_attrs=None):
        uid = self.ids.next()
        cls = f"gb-text-{uid}"
        a = {"uniqueId": uid, "tagName": tag, "styles": styles, "css": make_css(cls, styles)}
        if html_attrs:
            a["htmlAttributes"] = html_attrs
        a["className"] = "gb-text"
        return (f"<!-- wp:generateblocks/text {jdump(a)} -->\n<{tag} class=\"gb-text {cls} gb-text\""
                f"{attrs_html(html_attrs or {})}>{content}</{tag}>\n<!-- /wp:generateblocks/text -->\n\n")

    def shape(self, icon, size, color="#ffffff"):
        uid = self.ids.next()
        cls = f"gb-shape-{uid}"
        styles = {"color": color, "display": "inline-flex", "svg": {"height": size, "width": size}}
        a = {"uniqueId": uid, "styles": styles, "css": make_css(cls, styles)}
        svg = ('<svg aria-hidden="true" stroke-linejoin="round" stroke-linecap="round" stroke-width="2" '
               f'stroke="currentColor" fill="none" viewBox="0 0 24 24">{ICONS[icon]}</svg>')
        return (f"<!-- wp:generateblocks/shape {jdump(a)} -->\n<span class=\"gb-shape {cls}\">{svg}</span>\n"
                "<!-- /wp:generateblocks/shape -->\n\n")

    # ---- shared style snippets -------------------------------------------------
    @staticmethod
    def section(bg, extra=None):
        s = {"backgroundColor": bg, "paddingTop": "5rem", "paddingBottom": "5rem",
             "paddingLeft": "1.5rem", "paddingRight": "1.5rem",
             "@media (max-width:767px)": {"paddingTop": "3rem", "paddingBottom": "3rem"}}
        s.update(extra or {})
        return s

    CONTAINER = {"marginLeft": "auto", "marginRight": "auto", "maxWidth": "var(--gb-container-width)"}
    ACCENT_BG = {
        "backgroundColor": "var(--accent)",
        "backgroundImage": "radial-gradient(rgba(255,255,255,0.16) 2px, transparent 2px), linear-gradient(135deg, var(--accent), var(--accent-2))",
        "backgroundSize": "22px 22px, 100% 100%",
    }

    def eyebrow(self, t, center=True):
        s = {"color": "var(--accent)", "fontWeight": "700", "letterSpacing": "0.08em",
             "marginBottom": "0.75rem", "textTransform": "uppercase"}
        if center:
            s["textAlign"] = "center"
        return self.text("p", s, t)

    def h2(self, t, center=True):
        s = {"color": "var(--contrast)", "fontWeight": "800", "marginBottom": "1rem"}
        if center:
            s["textAlign"] = "center"
        return self.text("h2", s, t)

    def lead(self, t, mb="3rem", mw="680px"):
        return self.text("p", {"color": "var(--contrast)", "marginBottom": mb, "marginLeft": "auto",
                               "marginRight": "auto", "maxWidth": mw, "textAlign": "center"}, t)

    def pill(self, label, href, kind="solid", target=False, mb=None):
        if kind == "solid":
            s = {"backgroundColor": "var(--accent)", "borderRadius": "9999px", "color": "#ffffff",
                 "display": "inline-block", "fontWeight": "700", "padding": "0.85rem 2rem",
                 "textDecoration": "none", "transition": "background-color 0.2s ease",
                 "&:hover": {"backgroundColor": "var(--accent-2)"}}
        elif kind == "outline":
            s = {"backgroundColor": "transparent", "color": "var(--accent)", "display": "inline-block",
                 "fontWeight": "700", "textDecoration": "none", "transition": "all 0.2s ease",
                 "border": "2px solid var(--accent)", "borderRadius": "9999px", "padding": "0.75rem 1.85rem",
                 "&:hover": {"backgroundColor": "var(--accent)", "color": "#ffffff"}}
        elif kind == "white":
            s = {"backgroundColor": "#ffffff", "borderRadius": "9999px", "color": "var(--accent)",
                 "display": "inline-block", "fontWeight": "700", "padding": "0.9rem 2.25rem",
                 "textDecoration": "none", "transition": "transform 0.2s ease",
                 "&:hover": {"transform": "translateY(-2px)"}}
        else:  # white outline
            s = {"backgroundColor": "transparent", "color": "#ffffff", "display": "inline-block",
                 "fontWeight": "700", "textDecoration": "none", "transition": "all 0.2s ease",
                 "border": "2px solid #ffffff", "borderRadius": "9999px", "padding": "0.8rem 2.1rem",
                 "&:hover": {"backgroundColor": "#ffffff", "color": "var(--accent)"}}
        h = {"href": href}
        if target:
            h.update({"target": "_blank", "rel": "noopener"})
        return self.text("a", s, label, h)

    def card(self, inner, top_border=True):
        s = {"backgroundColor": "var(--base-2)", "borderRadius": "18px",
             "boxShadow": "0 8px 24px rgba(0,0,0,0.07)", "display": "flex", "flexDirection": "column",
             "padding": "2rem 1.75rem", "textAlign": "center",
             "transition": "transform 0.2s ease, box-shadow 0.2s ease",
             "&:hover": {"boxShadow": "0 16px 36px rgba(0,0,0,0.12)", "transform": "translateY(-4px)"}}
        if top_border:
            s["borderTop"] = "4px solid var(--accent)"
        return self.el(s, inner)

    def grid(self, cols, inner, gap="2rem", mobile="1fr", bp="900px"):
        return self.el({"columnGap": gap, "display": "grid", "gridTemplateColumns": f"repeat({cols},minmax(0,1fr))",
                        "rowGap": gap, f"@media (max-width:{bp})": {"gridTemplateColumns": mobile}}, inner)


def wp_group_cta(b):
    """Return the standard 'Come See Us' accent CTA section."""
    inner = (
        b.text("h2", {"color": "#ffffff", "fontWeight": "800", "marginBottom": "1rem"}, "Come See Us in Levittown")
        + b.text("p", {"color": "#ffffff", "fontSize": "1.1rem", "marginBottom": "0.5rem", "marginLeft": "auto",
                       "marginRight": "auto", "maxWidth": "640px"},
                 "Across from the Levittown Town Center at Route 13 &amp; Levittown Pkwy. Stop in for cold beer, "
                 "fair prices, and a huge selection — or order your keg ahead.")
        + b.text("p", {"color": "#ffffff", "fontSize": "1.6rem", "fontWeight": "800", "marginBottom": "2rem",
                       "marginTop": "1rem"}, PHONE_DISPLAY)
        + b.el({"columnGap": "1rem", "display": "flex", "flexWrap": "wrap", "justifyContent": "center", "rowGap": "1rem"},
               b.pill("Get Directions", DIRECTIONS, "white", True) + b.pill("Call Us", f"tel:{PHONE_TEL}", "whiteoutline"))
    )
    wrap = b.el({**b.CONTAINER, "position": "relative", "textAlign": "center", "zIndex": "1"}, inner)
    s = {**b.ACCENT_BG, "overflow": "hidden", "padding": "5.5rem 1.5rem 5rem 1.5rem", "position": "relative",
         "@media (max-width:767px)": {"paddingBottom": "3.5rem", "paddingTop": "4rem"}}
    return b.el(s, wrap, tag="section", align=True)


PATTERN_REF = 2106  # synced "Beer-A-Rama Levittown Location" pattern on the live site


def plain(html):
    """Strip tags/entities for schema text."""
    return re.sub(r"<[^>]+>", "", html).replace("&amp;", "&")


def build_location_pattern():
    b = Builder("loc")
    hours_rows = ""
    for i, (day, hrs) in enumerate(HOURS):
        row = {"alignItems": "center", "display": "flex", "justifyContent": "space-between",
               "paddingBottom": "0.75rem", "paddingTop": "0.75rem"}
        if i < len(HOURS) - 1:
            row["borderBottom"] = "1px solid rgba(255,255,255,0.25)"
        hours_rows += b.el(row, b.text("span", {"color": "#ffffff", "fontWeight": "700"}, day)
                           + b.text("span", {"color": "#ffffff"}, hrs))

    left = (
        b.el({"alignItems": "center", "columnGap": "0.6rem", "color": "var(--accent)", "display": "flex",
              "marginBottom": "1rem"},
             b.shape("pin", "1.5rem", "var(--accent)") + b.text("h2", {"color": "var(--contrast)", "fontWeight": "800", "marginBottom": "0"}, "Visit Beer-A-Rama in Levittown, PA"))
        + f'<!-- wp:html -->\n<iframe src="{MAP_EMBED}" width="100%" height="380" style="border:0;border-radius:16px;" '
          'allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" '
          'title="Map of Beer-A-Rama in Levittown, PA"></iframe>\n<!-- /wp:html -->\n\n'
    )
    right = b.el(
        {**b.ACCENT_BG, "backgroundSize": "20px 20px, 100% 100%", "borderRadius": "18px",
         "boxShadow": "0 12px 30px rgba(0,0,0,0.12)", "color": "#ffffff", "display": "flex",
         "flexDirection": "column", "justifyContent": "center", "padding": "2.5rem 2.25rem"},
        b.el({"alignItems": "center", "columnGap": "0.6rem", "display": "flex", "marginBottom": "1.5rem"},
             b.shape("clock", "1.5rem") + b.text("h2", {"color": "#ffffff", "fontWeight": "800", "marginBottom": "0"}, "Store Hours"))
        + hours_rows
        + b.text("p", {"color": "#ffffff", "fontSize": "0.85rem", "fontStyle": "italic", "marginBottom": "0",
                       "marginTop": "1.25rem", "opacity": "0.9"}, "**Holiday hours may differ"))
    cols = b.el({"alignItems": "stretch", "columnGap": "2.5rem", "display": "grid", "gridTemplateColumns": "1.2fr 0.8fr",
                 "rowGap": "2rem", "@media (max-width:900px)": {"gridTemplateColumns": "1fr"}},
                b.el({}, left) + right)
    intro = b.text("p", {"color": "var(--contrast)", "fontWeight": "700", "marginBottom": "2.5rem", "marginLeft": "auto",
                         "marginRight": "auto", "maxWidth": "760px", "textAlign": "center"},
                   "Beer-A-Rama is conveniently located across from the Levittown Town Center at Route 13 and Levittown Pkwy.")
    loc = b.el(b.section("var(--base-2)"), b.el(b.CONTAINER, intro + cols), tag="section", align=True,
               html_attrs={"id": "visit-levittown"})

    schema = {
        "@context": "https://schema.org", "@type": "LiquorStore", "@id": "https://beerarama.com/#store",
        "name": "Beer-A-Rama", "url": "https://beerarama.com/", "telephone": "+12159463480", "foundingDate": "1968",
        "address": {"@type": "PostalAddress", "streetAddress": "[[STREET_ADDRESS]]", "addressLocality": "Levittown",
                    "addressRegion": "PA", "postalCode": "[[ZIP]]", "addressCountry": "US"},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Sunday"], "opens": "10:00", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "09:00", "closes": "20:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Friday", "Saturday"], "opens": "09:00", "closes": "21:00"},
        ],
        "areaServed": "Levittown, PA",
        "priceRange": "$",
        "geo": {"@type": "GeoCoordinates", "latitude": 40.14493667929643, "longitude": -74.82160414883126},
        "hasMap": "https://www.google.com/maps/search/?api=1&query=Beer-A-Rama+Levittown+PA",
        "sameAs": ["https://www.instagram.com/beerarama/"],
    }
    schema_html = ('<!-- wp:html -->\n<script type="application/ld+json">\n'
                   + json.dumps(schema, indent=2, ensure_ascii=False) + "\n</script>\n<!-- /wp:html -->\n")
    header = ("<!--\n  SYNCED PATTERN: \"Beer-A-Rama Levittown Location\"\n"
              "  Editor: paste into a page, select all top-level blocks > Options > Create pattern > Synced.\n"
              "  Note its ID (wp_block post ID) and set it in each brand page's {\"ref\":ID}.\n"
              "  Only place address / hours / phone / map / LiquorStore schema live.\n"
              "  Fill [[STREET_ADDRESS]] and [[ZIP]] in the schema at the bottom.\n-->\n\n")
    return header + loc + wp_group_cta(b) + schema_html


def build_brand_page(brand):
    b = Builder(brand["prefix"])
    name = brand["name"]
    page_title = f"{name} in Levittown, PA"

    # 1. Hero (image left in white card, copy right) + breadcrumb
    crumb_style = {"color": "var(--contrast)", "fontSize": "0.9rem", "marginBottom": "1rem", "opacity": "0.8"}
    crumb = b.text("p", crumb_style,
                   f'<a href="https://beerarama.com/">Home</a> › <a href="{HUB_URL}">Beer in Levittown, PA</a> › {name}')
    hero_left = b.el({"alignItems": "center", "backgroundColor": "#ffffff", "borderRadius": "10px", "display": "flex",
                      "flexDirection": "column", "gap": "1.5rem", "paddingTop": "20px", "paddingBottom": "20px",
                      "textAlign": "center"},
                     '<!-- wp:post-featured-image {"sizeSlug":"full"} /-->\n\n')
    hero_right = b.el({}, (
        crumb
        + b.text("h1", {"color": "var(--contrast)", "fontWeight": "800", "lineHeight": "1.1", "marginBottom": "1.25rem"}, page_title)
        + b.text("p", {"color": "var(--contrast)", "fontWeight": "700", "fontSize": "1.15rem", "marginBottom": "1.25rem"}, brand["hero_lead"])
        + b.text("p", {"color": "var(--contrast)", "marginBottom": "2rem"}, brand["hero_body"])
        + b.el({"columnGap": "1rem", "display": "flex", "flexWrap": "wrap", "rowGap": "1rem",
                "@media (max-width:1024px)": {"justifyContent": "center"}},
               b.pill("Get Directions", DIRECTIONS, "solid", True)
               + b.pill("Explore Our Selection", HUB_URL, "outline"))))
    hero_grid = b.el({"alignItems": "center", "columnGap": "4rem", "display": "grid",
                      "gridTemplateColumns": "repeat(2,minmax(0,1fr))", "rowGap": "3rem",
                      "@media (max-width:1024px)": {"gridTemplateColumns": "1fr", "textAlign": "center"}},
                     hero_left + hero_right)
    hero = b.el({"backgroundColor": "var(--base-2)", "backgroundImage": "radial-gradient(rgba(0,0,0,0.05) 2px, transparent 2px)",
                 "backgroundSize": "24px 24px", "overflow": "hidden", "padding": "5rem 1.5rem", "position": "relative",
                 "@media (max-width:767px)": {"paddingTop": "3rem", "paddingBottom": "3rem"}},
                b.el(b.CONTAINER, hero_grid), tag="section", align=True)

    # 2. Trust strip (with heading)
    def trust(icon, t, sub):
        return b.el({"alignItems": "center", "color": "#ffffff", "display": "flex", "flexDirection": "column",
                     "gap": "0.5rem", "textAlign": "center"},
                    b.shape(icon, "2.25rem")
                    + b.text("p", {"color": "#ffffff", "fontSize": "1.25rem", "fontWeight": "800", "marginBottom": "0"}, t)
                    + b.text("p", {"color": "#ffffff", "fontSize": "0.95rem", "marginBottom": "0", "opacity": "0.9"}, sub))
    strip_grid = b.el({"columnGap": "2rem", "display": "grid", "gridTemplateColumns": "repeat(4,minmax(0,1fr))",
                       "position": "relative", "rowGap": "2.5rem", "zIndex": "1",
                       "@media (max-width:900px)": {"gridTemplateColumns": "repeat(2,minmax(0,1fr))"}},
                      trust("people", "Family Owned", "Serving Levittown since 1968")
                      + trust("snow", "Ice Cold", "Chilled to 37°F every day")
                      + trust("drop", "Kegs &amp; Taps", "CO², taps &amp; party rentals")
                      + trust("bag", "Huge Selection", "Beer, seltzer, cider &amp; more"))
    strip_head = b.text("h2", {"color": "#ffffff", "fontWeight": "800", "marginBottom": "2.5rem", "textAlign": "center",
                               "position": "relative", "zIndex": "1"}, "Why Levittown Buys Beer at Beer-A-Rama")
    strip = b.el({**b.ACCENT_BG, "overflow": "hidden", "padding": "4.5rem 1.5rem 4rem 1.5rem", "position": "relative",
                  "@media (max-width:767px)": {"paddingTop": "3.5rem", "paddingBottom": "3rem"}},
                 b.el(b.CONTAINER, strip_head + strip_grid), tag="section", align=True)

    # 3. About the brand: spec cards + history / pairings
    def spec(label, value):
        return b.card(b.text("p", {"color": "var(--accent)", "fontWeight": "700", "letterSpacing": "0.08em",
                                   "marginBottom": "0.5rem", "textTransform": "uppercase", "fontSize": "0.85rem"}, label)
                      + b.text("p", {"color": "var(--contrast)", "fontWeight": "800", "fontSize": "1.5rem", "marginBottom": "0"}, value))

    def panel(title, body):
        return b.el({"backgroundColor": "var(--base-2)", "borderLeft": "4px solid var(--accent)", "borderRadius": "18px",
                     "padding": "1.75rem"},
                    b.text("h3", {"color": "var(--contrast)", "fontWeight": "800", "fontSize": "1.25rem", "marginBottom": "0.5rem"}, title)
                    + b.text("p", {"color": "var(--contrast)", "marginBottom": "0"}, body))
    about_inner = (b.eyebrow(f"About {name}") + b.h2(f"{name}: What Levittown Is Drinking")
                   + b.lead(brand["about"], mb="3rem", mw="760px")
                   + b.grid(4, "".join(spec(k, v) for k, v in brand["specs"]), gap="1.5rem", mobile="repeat(2,minmax(0,1fr))")
                   + b.el({"height": "2.5rem"}, "")
                   + b.grid(2, panel(f"The Story of {name}", brand["history"])
                            + panel(f"What to Drink {name} With", brand["pairings"]), gap="1.5rem", mobile="1fr", bp="767px"))
    about = b.el(b.section("#ffffff"), b.el(b.CONTAINER, about_inner), tag="section", align=True)

    # 4. Buy in Levittown + Trends
    def info_card(title, body, bg="#ffffff"):
        return b.el({"backgroundColor": bg, "borderRadius": "18px", "boxShadow": "0 8px 24px rgba(0,0,0,0.07)",
                     "padding": "1.75rem"},
                    b.text("h3", {"color": "var(--contrast)", "fontWeight": "800", "fontSize": "1.25rem", "marginBottom": "0.5rem"}, title)
                    + b.text("p", {"color": "var(--contrast)", "marginBottom": "0"}, body))
    buy_inner = (b.eyebrow("Stock Up &amp; Save") + b.h2(f"Buy {name} in Levittown, PA")
                 + b.lead(brand["buy_lead"])
                 + b.grid(3, info_card("Cases &amp; Packs", brand["formats"])
                          + info_card("Levittown Pricing", brand["pricing"])
                          + info_card(f"Why Levittown Loves {name}", brand["trends"]), gap="2rem")
                 + b.el({"height": "2rem"}, "")
                 + b.text("p", {"color": "var(--contrast)", "fontWeight": "700", "marginLeft": "auto", "marginRight": "auto",
                                "maxWidth": "760px", "textAlign": "center"}, brand["kegs_line"]))
    buy = b.el(b.section("var(--base-2)"), b.el(b.CONTAINER, buy_inner), tag="section", align=True)

    # 5. Occasions
    def occ(t, body):
        return b.card(b.text("h3", {"color": "var(--contrast)", "fontWeight": "800", "fontSize": "1.2rem", "marginBottom": "0.5rem"}, t)
                      + b.text("p", {"color": "var(--contrast)", "marginBottom": "0"}, body))
    occ_inner = (b.eyebrow("Made for Get-Togethers") + b.h2(f"{name} for Every Levittown Occasion")
                 + b.lead(f"Whatever's on the calendar, a cold case of {name} from Beer-A-Rama has you covered.")
                 + b.grid(4, "".join(occ(t, d) for t, d in brand["occasions"]), gap="1.5rem", mobile="repeat(2,minmax(0,1fr))"))
    occasions = b.el(b.section("#ffffff"), b.el(b.CONTAINER, occ_inner), tag="section", align=True)

    # 6. Reviews (Trustindex widget already used on the homepage)
    reviews = b.el(b.section("var(--base-2)"), b.el({**b.CONTAINER, "textAlign": "center"}, (
        b.eyebrow("Don't Just Take Our Word For It") + b.h2("What Our Neighbors Are Saying")
        + b.el({"alignItems": "center", "backgroundColor": "#ffffff", "border": "3px dashed var(--accent)", "borderRadius": "18px",
                "display": "flex", "flexDirection": "column", "gap": "0.75rem", "justifyContent": "center",
                "minHeight": "220px", "padding": "3rem 2rem"},
               "<!-- wp:html -->\n<script defer async src='https://cdn.trustindex.io/loader.js?052132c8028a96526456c9b815e'></script>\n<!-- /wp:html -->\n\n"))),
        tag="section", align=True)

    # 7. FAQ
    faq_wrap = b.el({"display": "grid", "gap": "1.5rem", "gridTemplateColumns": "repeat(2,minmax(0,1fr))",
                     "@media (max-width:767px)": {"gridTemplateColumns": "1fr"}},
                    "".join(b.el({"backgroundColor": "var(--base-2)", "borderRadius": "18px",
                                  "borderLeft": "4px solid var(--accent)", "padding": "1.75rem"},
                                 b.text("h3", {"color": "var(--contrast)", "fontWeight": "800", "fontSize": "1.2rem", "marginBottom": "0.5rem"}, q)
                                 + b.text("p", {"color": "var(--contrast)", "marginBottom": "0"}, a))
                            for q, a in brand["faqs"]))
    faq = b.el(b.section("#ffffff"),
               b.el(b.CONTAINER, b.eyebrow("Good to Know") + b.h2(f"{name} Levittown FAQs") + faq_wrap),
               tag="section", align=True)

    # 8. Related brands + internal links
    def rel(label, url):
        return b.card(b.text("h3", {"color": "var(--contrast)", "fontWeight": "800", "marginBottom": "0.5rem"}, label)
                      + b.text("p", {"color": "var(--contrast)", "marginBottom": "1.5rem"}, f"See {label} in Levittown, PA.")
                      + b.el({"marginTop": "auto"}, b.pill("Shop " + label, url, "solid")))
    links = b.el({"columnGap": "1rem", "display": "flex", "flexWrap": "wrap", "justifyContent": "center", "marginTop": "3rem",
                  "rowGap": "1rem"},
                 "".join(b.pill(l, u, "outline") for l, u in INTERNAL_LINKS))
    related = b.el(b.section("var(--base-2)"),
                   b.el(b.CONTAINER, b.eyebrow("More Cold Ones") + b.h2(brand["related_heading"])
                        + b.lead("Not sure what to grab? Ask our team, or browse more of what's cold right now.")
                        + b.grid(len(brand["related"]), "".join(rel(n, u) for n, u in brand["related"])) + links),
                   tag="section", align=True)

    # 9. Brand-specific "where to buy" lead-in for the synced location pattern
    where = b.el(b.section("#ffffff", {"paddingBottom": "2rem"}),
                 b.el(b.CONTAINER, b.eyebrow("Find Us") + b.h2(f"Where to Buy {name} in Levittown, PA")
                      + b.lead(brand["where"], mb="0", mw="760px")),
                 tag="section", align=True)

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Product", "name": name, "brand": {"@type": "Brand", "name": brand["schema_brand"]},
             "description": brand["schema_desc"], "image": "[[FEATURED_IMAGE_URL]]", "category": "Beer",
             "offers": {"@type": "Offer", "seller": {"@id": "https://beerarama.com/#store"}, "areaServed": "Levittown, PA"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://beerarama.com/"},
                {"@type": "ListItem", "position": 2, "name": "Beer in Levittown, PA", "item": HUB_URL},
                {"@type": "ListItem", "position": 3, "name": name, "item": brand["url"]}]},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": s}} for q, s in [(q, plain(a)) for q, a in brand["faqs"]]]},
        ],
    }
    schema_html = ('<!-- wp:html -->\n<script type="application/ld+json">\n'
                   + json.dumps(schema, indent=2, ensure_ascii=False) + "\n</script>\n<!-- /wp:html -->\n\n")

    seo = brand["seo"]
    header = (f"<!--\n  {page_title} — brand page (GenerateBlocks). Generated by build_brand_page.py\n\n"
              f"  Title tag:        {seo['title']}\n  Meta description: {seo['desc']}\n  Slug:             {brand['slug']}\n"
              f"  Featured image:   file {brand['slug']}-levittown-pa.png. Alt: \"{seo['alt']}\"\n"
              f"  Taxonomies:       types = {brand['type']}; packages = {', '.join(brand['packages'])}\n\n"
              f"  Location/hours/CTA come from synced pattern ID {PATTERN_REF} (wp:block line at the bottom).\n"
              "  Replace every [[ ... ]] placeholder before publishing. Nothing in [[ ]] is verified.\n"
              f"  VERIFY before publishing: {brand['verify']}\n-->\n\n")
    return (header + hero + strip + about + buy + occasions + reviews + faq + related + where
            + f'<!-- wp:block {{"ref":{PATTERN_REF}}} /-->\n\n' + schema_html)


INTERNAL_LINKS = [
    ("All Beer in Levittown", HUB_URL),
    ("Kegs & Supplies", "https://beerarama.com/kegs/"),
    ("Adult Slushies", "https://beerarama.com/hard-slushies-levittown-pa/"),
]


def build_wxr(brands, pages):
    """WordPress import file (Tools > Import > WordPress): one draft `brands` post per brand."""
    import datetime
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def cdata(t):
        return "<![CDATA[" + t.replace("]]>", "]]]]><![CDATA[>") + "]]>"

    def slugify(t):
        return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

    def meta(k, v):
        return f"<wp:postmeta><wp:meta_key>{cdata(k)}</wp:meta_key><wp:meta_value>{cdata(v)}</wp:meta_value></wp:postmeta>\n"
    items = ""
    for n, brand in enumerate(brands):
        pid = 9001 + n
        terms = f'<category domain="types" nicename="{slugify(brand["type"])}">{cdata(brand["type"])}</category>\n'
        terms += "".join(f'<category domain="packages" nicename="{slugify(p)}">{cdata(p)}</category>\n' for p in brand["packages"])
        seo = brand["seo"]
        items += (
            f"<item>\n<title>{cdata(brand['name'])}</title>\n<link>{brand['url']}</link>\n<pubDate>{now}</pubDate>\n"
            f"<dc:creator>{cdata('info@manyresults.com')}</dc:creator>\n"
            f'<guid isPermaLink="false">https://beerarama.com/?post_type=brands&#038;p={pid}</guid>\n<description></description>\n'
            f"<content:encoded>{cdata(pages[brand['slug']])}</content:encoded>\n<excerpt:encoded>{cdata('')}</excerpt:encoded>\n"
            f"<wp:post_id>{pid}</wp:post_id>\n<wp:post_date>{cdata(now)}</wp:post_date>\n<wp:post_date_gmt>{cdata(now)}</wp:post_date_gmt>\n"
            f"<wp:post_modified>{cdata(now)}</wp:post_modified>\n<wp:post_modified_gmt>{cdata(now)}</wp:post_modified_gmt>\n"
            f"<wp:comment_status>{cdata('closed')}</wp:comment_status>\n<wp:ping_status>{cdata('closed')}</wp:ping_status>\n"
            f"<wp:post_name>{cdata(brand['slug'])}</wp:post_name>\n<wp:status>{cdata('draft')}</wp:status>\n"
            "<wp:post_parent>0</wp:post_parent>\n<wp:menu_order>0</wp:menu_order>\n"
            f"<wp:post_type>{cdata('brands')}</wp:post_type>\n<wp:post_password>{cdata('')}</wp:post_password>\n<wp:is_sticky>0</wp:is_sticky>\n"
            + terms
            + meta("rank_math_title", seo["title"]) + meta("rank_math_description", seo["desc"])
            + meta("rank_math_focus_keyword", f"{brand['name'].lower()} levittown pa")
            + meta("_generate-sidebar-layout-meta", "no-sidebar") + meta("_generate-full-width-content", "true")
            + meta("_generate-disable-headline", "true") + meta("_generate-disable-post-image", "true")
            + meta("_generateblocks_reusable_blocks", f'a:1:{{i:0;i:{PATTERN_REF};}}')
            + "</item>\n")
    return ('<?xml version="1.0" encoding="UTF-8" ?>\n<rss version="2.0" xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" '
            'xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/">\n<channel>\n'
            "<title>Beer-A-Rama</title>\n<link>https://beerarama.com</link>\n<language>en-US</language>\n"
            "<wp:wxr_version>1.2</wp:wxr_version>\n<wp:base_site_url>https://beerarama.com</wp:base_site_url>\n"
            "<wp:base_blog_url>https://beerarama.com</wp:base_blog_url>\n"
            '<wp:author><wp:author_id>3</wp:author_id><wp:author_login><![CDATA[info@manyresults.com]]></wp:author_login>'
            '<wp:author_email><![CDATA[info@manyresults.com]]></wp:author_email></wp:author>\n'
            + items + "</channel>\n</rss>\n")


if __name__ == "__main__":
    import os
    from brands import BRANDS
    os.makedirs("pages", exist_ok=True)
    os.makedirs("import", exist_ok=True)
    open("beerarama-location-block.html", "w").write(build_location_pattern())
    pages = {}
    for brand in BRANDS:
        pages[brand["slug"]] = build_brand_page(brand)
        open(f"pages/{brand['slug']}.html", "w").write(pages[brand["slug"]])
    # Miller Lite already exists on the site (post 2103); import only the new brands.
    new = [b for b in BRANDS if b["slug"] != "miller-lite"]
    open("import/brands-import.xml", "w").write(build_wxr(new, pages))
    print("wrote", len(BRANDS), "pages + location pattern + import/brands-import.xml for", [b["name"] for b in new])
