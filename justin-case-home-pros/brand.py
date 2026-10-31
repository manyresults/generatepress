from gb_helpers import *
import gb_helpers
TEAL="#164E53";ORG="#E66F36";CREAM="#FFF2D5";INK="#293638";TINT="#FFF8E8"
FONT="'Fredoka','Nunito','Arial Rounded MT Bold',system-ui,sans-serif"
def hl(t,on_dark=False):
    return f'<span style="background:linear-gradient(transparent 82%,{ORG} 82%);padding:0 .08em">{t}</span>'
EMBLEM=svguri(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="{TEAL}"/><ellipse cx="32" cy="35" rx="28" ry="9" fill="none" stroke="{ORG}" stroke-width="2.6" transform="rotate(-22 32 32)"/><path d="M15 36 32 21l17 15v13H15z" fill="{CREAM}"/><rect x="28" y="39" width="8" height="10" rx="1" fill="{ORG}"/><path d="M48 8l2.2 5.3L55.5 15.5l-5.3 2.2L48 23l-2.2-5.3L40.5 15.5l5.3-2.2z" fill="{ORG}"/></svg>''')
HERO=svguri(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 480"><circle cx="270" cy="240" r="215" fill="{TEAL}"/><ellipse cx="260" cy="250" rx="250" ry="78" fill="none" stroke="{ORG}" stroke-width="7" transform="rotate(-24 260 250)"/><path d="M110 270 270 130l160 140v140H110z" fill="{CREAM}"/><path d="M92 276 270 116l178 160" fill="none" stroke="{ORG}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/><rect x="350" y="120" width="30" height="62" fill="{ORG}"/><rect x="232" y="318" width="76" height="92" rx="8" fill="{TEAL}"/><circle cx="292" cy="366" r="6" fill="{CREAM}"/><rect x="140" y="296" width="62" height="62" rx="8" fill="{TEAL}"/><rect x="338" y="296" width="62" height="62" rx="8" fill="{TEAL}"/><path d="M170 296v62M140 327h62M368 296v62M338 327h62" stroke="{CREAM}" stroke-width="5"/><path d="M80 80l9 22 22 9-22 9-9 22-9-22-22-9 22-9z" fill="{ORG}"/><path d="M450 60l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="{CREAM}"/><path d="M470 360l5 11 11 5-11 5-5 11-5-11-11-5 11-5z" fill="{ORG}"/><circle cx="60" cy="380" r="9" fill="{ORG}"/><circle cx="500" cy="200" r="6" fill="{TEAL}"/></svg>''')
ABOUT=svguri(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 330"><rect width="540" height="330" rx="24" fill="{TEAL}"/><circle cx="270" cy="165" r="120" fill="{CREAM}"/><ellipse cx="270" cy="170" rx="250" ry="62" fill="none" stroke="{ORG}" stroke-width="6" transform="rotate(-14 270 170)"/><path d="M200 190 270 128l70 62v50H200z" fill="{TEAL}"/><rect x="254" y="200" width="32" height="40" rx="4" fill="{ORG}"/><path d="M62 56l8 19 19 8-19 8-8 19-8-19-19-8 19-8z" fill="{ORG}"/><path d="M470 250l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="{CREAM}"/><circle cx="480" cy="70" r="8" fill="{ORG}"/></svg>''')
def logo_link(href):
    mark=tx("span",{"display":"block","lineHeight":"0"},"")
    return el("a",{"alignItems":"center","columnGap":"0.7rem","display":"flex","textDecoration":"none"},[
        img(EMBLEM,"","jchp-emblem"),
        el("div",{"display":"flex","flexDirection":"column"},[
            tx("span",{"color":TEAL,"fontFamily":FONT,"fontSize":"1.6rem","fontWeight":"700","lineHeight":"1"},"Justin Case"),
            tx("span",{"color":ORG,"fontFamily":FONT,"fontSize":"0.72rem","fontWeight":"600","letterSpacing":"0.28em","marginTop":"0.25rem","textTransform":"uppercase"},"Home Pros")])],
        html_attrs={"href":href,"aria-label":"Justin Case Home Pros"})
def wrap(children,extra=None,maxw="1160px"):
    s={"marginLeft":"auto","marginRight":"auto","maxWidth":maxw,"width":"100%"}
    if extra: s.update(extra)
    return el("div",s,children)
def eyebrow(t,color=TEAL):
    return tx("p",{"color":color,"fontSize":"0.8rem","fontWeight":"800","letterSpacing":"0.2em","marginBottom":"0.9rem","textTransform":"uppercase"},"✦ "+t)
def h2(t,color=TEAL):
    return tx("h2",{"color":color,"fontFamily":FONT,"fontSize":"clamp(2rem,5.5vw,3.3rem)","fontWeight":"700","lineHeight":"1.1","marginBottom":"1.2rem"},t)
def para(t,color=INK,extra=None):
    s={"color":color,"fontSize":"1.05rem","lineHeight":"1.6","marginBottom":"1.1rem"}
    if extra: s.update(extra)
    return tx("p",s,t)
def button(t,href,bg=ORG,color=INK,shadow="#a8441b",small=False):
    s={"alignItems":"center","backgroundColor":bg,"borderRadius":"999px","boxShadow":f"0 3px 0 {shadow}","color":color,"display":"inline-flex","fontFamily":FONT,"fontSize":"0.95rem" if small else "1.05rem","fontWeight":"600","justifyContent":"center","padding":"0.7rem 1.3rem" if small else "0.9rem 1.8rem","textDecoration":"none","transition":"transform .18s,box-shadow .18s","whiteSpace":"nowrap",
       "&:hover":{"transform":"translateY(-2px)","boxShadow":f"0 5px 0 {shadow}","color":color}}
    return tx("a",s,t,{"href":href})
def section(children,bg,pad="4.5rem",anchor=None,extra=None):
    s={"backgroundColor":bg,"paddingTop":pad,"paddingBottom":pad,"paddingLeft":"1.25rem","paddingRight":"1.25rem"}
    if extra: s.update(extra)
    return el("section",s,children,full=True,html_attrs={"id":anchor} if anchor else None)
def grid(cols,children,gap="2.5rem",tablet=None,mobile=None,extra=None):
    s={"alignItems":"center","display":"grid","gridTemplateColumns":cols,"columnGap":gap,"rowGap":gap}
    if tablet: s["@media (max-width:1024px)"]={"gridTemplateColumns":tablet}
    if mobile: s["@media (max-width:600px)"]={"gridTemplateColumns":mobile}
    if extra: s.update(extra)
    return el("div",s,children)
navlink=lambda t,h: tx("a",{"color":INK,"fontSize":"1rem","fontWeight":"700","textDecoration":"none","&:hover":{"color":ORG}},t,{"href":h})
flink=lambda t,h: tx("a",{"color":CREAM,"textDecoration":"underline","textUnderlineOffset":"4px","textDecorationColor":ORG},t,{"href":h})
STYLE_COMMON='''@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap');
.home .site-content,.home .inside-article,.home .entry-content{padding:0!important;margin:0!important;max-width:none!important}
html{scroll-behavior:smooth;scroll-padding-top:90px}
.jchp-emblem{margin:0}.jchp-emblem img{width:58px;height:58px;display:block}
.jchp-hero-img,.jchp-about-img{margin:0}
.jchp-hero-img img,.jchp-about-img img{width:100%;height:auto;display:block}
.jchp-about-img img{border-radius:24px}'''
def header(nav_items,cta_href):
    nav=el("nav",{"columnGap":"1.8rem","display":"flex","@media (max-width:700px)":{"order":"3","width":"100%","justifyContent":"space-between","columnGap":"0.5rem"}},[navlink(t,h) for t,h in nav_items],html_attrs={"aria-label":"Primary"})
    return el("header",{"backgroundColor":CREAM,"borderBottom":f"3px solid {TEAL}","paddingLeft":"1.25rem","paddingRight":"1.25rem","paddingTop":"0.6rem","paddingBottom":"0.6rem","position":"sticky","top":"0","zIndex":"50"},
      [wrap([logo_link("/" if cta_href.startswith("/#") else "#home"),nav,button("Get Early Access",cta_href,small=True)],{"alignItems":"center","columnGap":"2rem","display":"flex","flexWrap":"wrap","justifyContent":"space-between","rowGap":"0.6rem"})],full=True)
def footer():
    return el("footer",{"backgroundColor":INK,"color":CREAM,"fontSize":"0.9rem","paddingTop":"2rem","paddingBottom":"2rem","paddingLeft":"1.25rem","paddingRight":"1.25rem","textAlign":"center"},[
      tx("p",{"color":CREAM,"marginBottom":"0.4rem"},"Justin Case Home Pros — Lower Bucks County, PA. Launching 2027."),
      el("div",{"columnGap":"1.2rem","display":"flex","justifyContent":"center"},[flink("Privacy Policy","/privacy-policy/"),flink("Terms and Conditions","/terms-and-conditions/")])],full=True)
