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
             b.shape("pin", "1.5rem", "var(--accent)") + b.text("h2", {"color": "var(--contrast)", "fontWeight": "800", "marginBottom": "0"}, "Our Levittown Location"))
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

    # 1. Hero
    hero_left = (
        b.text("p", {"color": "var(--accent)", "fontWeight": "700", "letterSpacing": "0.08em", "marginBottom": "1rem",
                     "textTransform": "uppercase"}, "Levittown's Beer Distributor Since 1968")
        + b.text("h1", {"color": "var(--contrast)", "fontWeight": "800", "lineHeight": "1.1", "marginBottom": "1.25rem"}, page_title)
        + b.text("p", {"color": "var(--contrast)", "fontWeight": "700", "fontSize": "1.15rem", "marginBottom": "1.25rem"}, brand["hero_lead"])
        + b.text("p", {"color": "var(--contrast)", "marginBottom": "2rem"}, brand["hero_body"])
        + b.el({"columnGap": "1rem", "display": "flex", "flexWrap": "wrap", "rowGap": "1rem",
                "@media (max-width:1024px)": {"justifyContent": "center"}},
               b.pill("Get Directions", DIRECTIONS, "solid", True)
               + b.pill("Explore Our Selection", HUB_URL, "outline"))
    )
    pill = b.el({"alignItems": "center", "backgroundColor": "#ffffff", "borderRadius": "9999px",
                 "boxShadow": "0 10px 25px rgba(0,0,0,0.12)", "columnGap": "1rem", "display": "flex",
                 "padding": "1px 1.5em 1px 0.5px"},
                '<!-- wp:generateblocks/image {"uniqueId":"07022659","mediaId":1597,"sizeSlug":"medium","blockVersion":2} -->\n'
                '<figure class="gb-block-image gb-block-image-07022659"><img class="gb-image gb-image-07022659" '
                'src="https://beerarama.com/wp-content/uploads/2022/11/justin_full_1000-287x300.png" alt="Beer-A-Rama owner"/></figure>\n'
                '<!-- /wp:generateblocks/image -->\n\n'
                + b.text("p", {"color": "var(--contrast)", "fontWeight": "700", "marginBottom": "0"},
                         "Family owned &amp; operated<br>right here in Levittown"))
    hero_right = b.el({"alignItems": "center", "display": "flex", "flexDirection": "column", "gap": "1.5rem"},
                      "<!-- wp:post-featured-image {\"sizeSlug\":\"large\"} /-->\n\n" + pill)
    hero_grid = b.el({"alignItems": "center", "columnGap": "4rem", "display": "grid", "gridTemplateColumns": "1.1fr 0.9fr",
                      "rowGap": "3rem", "@media (max-width:1024px)": {"gridTemplateColumns": "1fr", "textAlign": "center"}},
                     b.el({}, hero_left) + hero_right)
    hero = b.el({"backgroundColor": "var(--base-2)", "backgroundImage": "radial-gradient(rgba(0,0,0,0.05) 2px, transparent 2px)",
                 "backgroundSize": "24px 24px", "overflow": "hidden", "paddingTop": "5rem", "paddingBottom": "5rem",
                 "paddingLeft": "1.5rem", "paddingRight": "1.5rem", "position": "relative",
                 "@media (max-width:767px)": {"paddingTop": "3rem", "paddingBottom": "3rem"}},
                b.el(b.CONTAINER, hero_grid), tag="section", align=True)

    # 2. Trust strip
    def trust(icon, t, sub):
        return b.el({"alignItems": "center", "color": "#ffffff", "display": "flex", "flexDirection": "column",
                     "gap": "0.5rem", "textAlign": "center"},
                    b.shape(icon, "2.25rem")
                    + b.text("p", {"color": "#ffffff", "fontSize": "1.25rem", "fontWeight": "800", "marginBottom": "0"}, t)
                    + b.text("p", {"color": "#ffffff", "fontSize": "0.95rem", "marginBottom": "0", "opacity": "0.9"}, sub))
    strip_grid = b.el({"columnGap": "2rem", "display": "grid", "gridTemplateColumns": "repeat(4,minmax(0,1fr))",
                       **b.CONTAINER, "position": "relative", "rowGap": "2.5rem", "zIndex": "1",
                       "@media (max-width:900px)": {"gridTemplateColumns": "repeat(2,minmax(0,1fr))"}},
                      trust("people", "Family Owned", "Serving Levittown since 1968")
                      + trust("snow", "Ice Cold", "Chilled to 37°F every day")
                      + trust("drop", "Kegs &amp; Taps", "CO², taps &amp; party rentals")
                      + trust("bag", "Huge Selection", "Beer, seltzer, cider &amp; more"))
    strip = b.el({**b.ACCENT_BG, "overflow": "hidden", "padding": "4.5rem 1.5rem 4rem 1.5rem", "position": "relative",
                  "@media (max-width:767px)": {"paddingTop": "3.5rem", "paddingBottom": "3rem"}},
                 strip_grid, tag="section", align=True)

    # 3. About the brand + spec cards
    def spec(label, value):
        return b.card(b.text("p", {"color": "var(--accent)", "fontWeight": "700", "letterSpacing": "0.08em",
                                   "marginBottom": "0.5rem", "textTransform": "uppercase", "fontSize": "0.85rem"}, label)
                      + b.text("p", {"color": "var(--contrast)", "fontWeight": "800", "fontSize": "1.5rem", "marginBottom": "0"}, value))
    about_inner = (b.eyebrow(f"About {name}") + b.h2(f"{name}: What Levittown Is Drinking")
                   + b.lead(brand["about"], mb="3rem", mw="760px")
                   + b.grid(4, "".join(spec(k, v) for k, v in brand["specs"]), gap="1.5rem", mobile="repeat(2,minmax(0,1fr))"))
    about = b.el(b.section("#ffffff"), b.el(b.CONTAINER, about_inner), tag="section", align=True)

    # 4. Buy in Levittown + Trends
    def info_card(title, body):
        return b.el({"backgroundColor": "#ffffff", "borderRadius": "18px", "boxShadow": "0 8px 24px rgba(0,0,0,0.07)",
                     "padding": "1.75rem"},
                    b.text("h3", {"color": "var(--contrast)", "fontWeight": "800", "fontSize": "1.25rem", "marginBottom": "0.5rem"}, title)
                    + b.text("p", {"color": "var(--contrast)", "marginBottom": "0"}, body))
    buy_inner = (b.eyebrow("Stock Up &amp; Save") + b.h2(f"Buy {name} in Levittown, PA")
                 + b.lead(brand["buy_lead"])
                 + b.grid(3, info_card("Cases &amp; Packs", brand["formats"])
                          + info_card("Levittown Pricing", brand["pricing"])
                          + info_card(f"Why Levittown Loves {name}", brand["trends"]), gap="2rem"))
    buy = b.el(b.section("var(--base-2)"), b.el(b.CONTAINER, buy_inner), tag="section", align=True)

    # 5. FAQ
    faq_wrap = b.el({"display": "grid", "gap": "1.5rem", "gridTemplateColumns": "repeat(2,minmax(0,1fr))",
                     "@media (max-width:767px)": {"gridTemplateColumns": "1fr"}},
                    "".join(b.el({"backgroundColor": "var(--base-2)", "borderRadius": "18px",
                                  "borderLeft": "4px solid var(--accent)", "padding": "1.75rem"},
                                 b.text("h3", {"color": "var(--contrast)", "fontWeight": "800", "fontSize": "1.2rem", "marginBottom": "0.5rem"}, q)
                                 + b.text("p", {"color": "var(--contrast)", "marginBottom": "0"}, a))
                            for q, a, _ in brand["faqs"]))
    faq = b.el(b.section("#ffffff"),
               b.el(b.CONTAINER, b.eyebrow("Good to Know") + b.h2(f"{name} Levittown FAQs") + faq_wrap),
               tag="section", align=True)

    # 6. Related brands
    def rel(label, url):
        return b.card(b.text("h3", {"color": "var(--contrast)", "fontWeight": "800", "marginBottom": "0.5rem"}, label)
                      + b.text("p", {"color": "var(--contrast)", "marginBottom": "1.5rem"}, f"See {label} in Levittown, PA.")
                      + b.el({"marginTop": "auto"}, b.pill("Shop " + label, url, "solid")))
    related = b.el(b.section("var(--base-2)"),
                   b.el(b.CONTAINER, b.eyebrow("More Cold Ones") + b.h2("Other Beers in Levittown, PA")
                        + b.lead("Not sure what to grab? Ask our team, or browse more of what's cold right now.")
                        + b.grid(3, "".join(rel(n, u) for n, u in brand["related"]))),
                   tag="section", align=True)

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Product", "name": name, "brand": {"@type": "Brand", "name": brand["schema_brand"]},
             "description": brand["schema_desc"], "image": "[[FEATURED_IMAGE_URL]]", "category": "Beer",
             "offers": {"@type": "Offer", "seller": {"@id": "https://beerarama.com/#store"}, "areaServed": "Levittown, PA"}},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": s}} for q, _, s in brand["faqs"]]},
        ],
    }
    schema_html = ('<!-- wp:html -->\n<script type="application/ld+json">\n'
                   + json.dumps(schema, indent=2, ensure_ascii=False) + "\n</script>\n<!-- /wp:html -->\n\n")

    seo = brand["seo"]
    header = (f"<!--\n  {page_title} — brand page (GenerateBlocks). Generated by build_brand_page.py\n\n"
              f"  Title tag:        {seo['title']}\n  Meta description: {seo['desc']}\n  Slug:             {brand['slug']}\n"
              f"  Featured image:   {brand['name']} pack shot. Alt: \"{seo['alt']}\"\n\n"
              "  Location/hours/CTA come from the synced pattern: set the ref ID on the wp:block line.\n"
              "  Replace every [[ ... ]] placeholder before publishing. Nothing in [[ ]] is verified.\n-->\n\n")
    return header + hero + strip + about + buy + faq + related + '<!-- wp:block {"ref":0} /-->\n\n' + schema_html


MILLER_LITE = {
    "prefix": "ml",
    "slug": "miller-lite-levittown-pa",
    "name": "Miller Lite",
    "schema_brand": "Miller",
    "schema_desc": "Miller Lite, the original light beer: an American light lager with 96 calories, 3.2 g carbs and 4.2% ABV, sold at Beer-A-Rama in Levittown, PA.",
    "seo": {
        "title": "Miller Lite in Levittown, PA | Low Prices at Beer-A-Rama",
        "desc": "Buy Miller Lite in Levittown, PA at Beer-A-Rama, Lower Bucks County's low price leader since 1968. Cases, 12-packs and more. Cold beer, fair prices.",
        "alt": "Miller Lite case available at Beer-A-Rama in Levittown, PA",
    },
    "hero_lead": "Looking for Miller Lite in Levittown? Beer-A-Rama is Lower Bucks County's Low Price Leader, proudly serving Levittown since 1968 — and Miller Lite is one of the beers our neighbors ask for most.",
    "hero_body": "Whether you're grabbing a case for the weekend, stocking up for a Levittown backyard cookout, or heading to a tailgate, our family-owned team will get you cold Miller Lite at prices that beat the big chains.",
    "about": "Whether it's the end of the workday or a few minutes to kickoff, it's always Miller Time. As the original light beer, this fine pilsner revolutionized the beer business. With a body that won't fill you up and flavor that stands the test of time, it's just as satisfying today as it was when it changed the landscape of American beer.",
    "specs": [("Style", "American Light Lager"), ("ABV", "4.2%"), ("Calories", "96 per 12 oz"), ("Brewed In", "Milwaukee, WI")],
    "buy_lead": "Beer-A-Rama is a Levittown beer distributor, so you can buy Miller Lite by the case instead of paying convenience-store prices for singles.",
    "formats": "[[CONFIRM_AND_LIST: e.g. 12-pack, 18-pack, 24-pack and 30-pack cans, bottles, kegs]]",
    "pricing": "[[PRICE, or \"Stop in or call 215-946-3480 for today's price\"]]",
    "trends": "[[GOOGLE_TRENDS_INSIGHT: 1-2 sentences from trends.google.com for the Philadelphia area, past 5 years. e.g. when \"Miller Lite\" searches peak.]] Popular searches: [[RELATED_QUERY_1]], [[RELATED_QUERY_2]], [[RELATED_QUERY_3]].",
    "faqs": [
        ("Where can I buy Miller Lite in Levittown, PA?",
         "Beer-A-Rama, across from the Levittown Town Center at Route 13 &amp; Levittown Pkwy. We've served Lower Bucks County since 1968.",
         "Beer-A-Rama, across from the Levittown Town Center at Route 13 and Levittown Pkwy. We've served Lower Bucks County since 1968."),
        ("Does Beer-A-Rama sell Miller Lite by the case?",
         "Yes. [[CONFIRM: cases, 24-packs, 30-packs available]]. Call 215-946-3480 and we'll tell you what's cold and in stock.",
         "Yes. Call 215-946-3480 to check what Miller Lite cases and packs are cold and in stock."),
        ("How many calories are in a Miller Lite?",
         "A 12 oz Miller Lite has 96 calories, 3.2 g of carbs and 4.2% ABV.",
         "A 12 oz Miller Lite has 96 calories, 3.2 g of carbs and 4.2% ABV."),
        ("What are your Levittown store hours?",
         "Sunday 10AM–5PM, Monday–Thursday 9AM–8PM, Friday–Saturday 9AM–9PM. Holiday hours may differ.",
         "Sunday 10AM-5PM, Monday-Thursday 9AM-8PM, Friday-Saturday 9AM-9PM. Holiday hours may differ."),
    ],
    "related": [("Bud Light", "[[URL_BUD_LIGHT]]"), ("Coors Light", "[[URL_COORS_LIGHT]]"), ("Michelob Ultra", "[[URL_MICHELOB_ULTRA]]")],
}

if __name__ == "__main__":
    open("beerarama-location-block.html", "w").write(build_location_pattern())
    open(MILLER_LITE["slug"] + ".html", "w").write(build_brand_page(MILLER_LITE))
    print("wrote beerarama-location-block.html and", MILLER_LITE["slug"] + ".html")
