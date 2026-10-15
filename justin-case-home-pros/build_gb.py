import base64, json, re
def uri(f): return 'data:image/webp;base64,'+base64.b64encode(open('images/'+f,'rb').read()).decode()
LOGO,HERO,ABOUT=uri('jchp-logo.webp'),uri('jchp-hero.webp'),uri('jchp-about.webp')
n=[0]
def uid():
    n[0]+=1; return f"jc{n[0]:03d}"
def kebab(k): return re.sub(r'([A-Z])',lambda m:'-'+m.group(1).lower(),k)
def css_for(cls,styles):
    base=[];extra=[];media=[]
    for k,v in styles.items():
        if k.startswith('@media'): media.append((k,v))
        elif k.startswith('&'): extra.append((k[1:],v))
        else: base.append(f"{kebab(k)}:{v}")
    out=f".{cls}{{{';'.join(base)}}}" if base else ""
    for suf,v in extra: out+=f".{cls}{suf}{{{';'.join(f'{kebab(a)}:{b}' for a,b in v.items())}}}"
    for k,v in media:
        inner=css_for(cls,v)
        out+=f"{k}{{{inner}}}"
    return out
def attrs(d):
    s=json.dumps(d,separators=(',',':'),ensure_ascii=False)
    return s.replace('--','\\u002d\\u002d').replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
def el(tag,styles,children,full=False,html_attrs=None,extra_cls=""):
    i=uid();cls=f"gb-element-{i}"
    a={"uniqueId":i,"tagName":tag,"styles":styles,"css":css_for(cls,styles)}
    if html_attrs: a["htmlAttributes"]=html_attrs
    if full: a["align"]="full"
    a["className"]="gb-element"+(" alignfull" if full else "")+(" "+extra_cls if extra_cls else "")
    ha="".join(f' {k}="{v}"' for k,v in (html_attrs or {}).items())
    return (f'<!-- wp:generateblocks/element {attrs(a)} -->\n<{tag} class="{cls} {a["className"]}"{ha}>\n'+"\n".join(children)+f'\n</{tag}>\n<!-- /wp:generateblocks/element -->')
def tx(tag,styles,content,html_attrs=None):
    i=uid();cls=f"gb-text-{i}"
    a={"uniqueId":i,"tagName":tag,"styles":styles,"css":css_for(cls,styles)}
    if html_attrs: a["htmlAttributes"]=html_attrs
    a["className"]="gb-text"
    ha="".join(f' {k}="{v}"' for k,v in (html_attrs or {}).items())
    return (f'<!-- wp:generateblocks/text {attrs(a)} -->\n<{tag} class="gb-text {cls}"{ha}>{content}</{tag}>\n<!-- /wp:generateblocks/text -->')
def img(src,alt,cls):
    return (f'<!-- wp:image {{"sizeSlug":"full","linkDestination":"none","className":"{cls}"}} -->\n<figure class="wp-block-image size-full {cls}"><img src="{src}" alt="{alt}"/></figure>\n<!-- /wp:image -->')

TEAL="var(--accent)";AMB="var(--accent-2)";CREAM="#f8f1e0";INK="#163b38";DARK="#123b38"
OSW="'Oswald','Arial Narrow',Arial,sans-serif"
SCR="font-family:'Yellowtail','Brush Script MT',cursive;font-weight:400;text-transform:none;letter-spacing:0"
def script(t,color="#d78b20"): return f'<span style="{SCR};font-size:1.25em;color:{color}">{t}</span>'
def wrap(children,extra=None,maxw="1160px"):
    s={"marginLeft":"auto","marginRight":"auto","maxWidth":maxw,"width":"100%"}
    if extra: s.update(extra)
    return el("div",s,children)
def eyebrow(t,color=TEAL):
    return tx("p",{"color":color,"fontSize":"0.78rem","fontWeight":"800","letterSpacing":"0.22em","marginBottom":"0.9rem","textTransform":"uppercase"},t)
def h2(t,color=TEAL):
    return tx("h2",{"color":color,"fontFamily":OSW,"fontSize":"clamp(2rem,5.5vw,3.3rem)","fontWeight":"700","lineHeight":"1.05","marginBottom":"1.2rem","textTransform":"uppercase"},t)
def para(t,color="inherit",extra=None):
    s={"color":color,"fontSize":"1.05rem","lineHeight":"1.6","marginBottom":"1.1rem"}
    if extra: s.update(extra)
    return tx("p",s,t)
def button(t,href,bg=AMB,color="#173d39",shadow="#b8791d",small=False,full=False):
    s={"alignItems":"center","backgroundColor":bg,"borderRadius":"999px","boxShadow":f"0 3px 0 {shadow}","color":color,"display":"inline-flex","fontSize":"0.85rem" if small else "0.95rem","fontWeight":"800","justifyContent":"center","letterSpacing":"0.07em","padding":"0.75rem 1.3rem" if small else "0.95rem 1.7rem","textDecoration":"none","textTransform":"uppercase","transition":"transform .18s,box-shadow .18s","whiteSpace":"nowrap",
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

blocks=[]
# style block
blocks.append('''<!-- wp:html -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Yellowtail&display=swap');
.home .site-content,.home .inside-article,.home .entry-content{padding:0!important;margin:0!important;max-width:none!important}
html{scroll-behavior:smooth;scroll-padding-top:90px}
.jchp-logo-img img{width:210px;height:auto;display:block}
.jchp-hero-img img{width:100%;height:auto;display:block;border-radius:40% 40% 18px 18px / 30% 30% 18px 18px}
.jchp-about-img img{width:100%;height:auto;display:block;border-radius:18px;border:4px solid var(--accent)}
.jchp-hero-img,.jchp-about-img,.jchp-logo-img{margin:0}
.jchp-form{background:#fffaf0;border:3px solid #1f4d4a;border-radius:20px;padding:1.8rem;box-shadow:6px 6px 0 #123b38;font-size:1rem}
.jchp-form label{display:block;font-weight:700;font-size:.9rem;margin-bottom:1rem;color:#163b38}
.jchp-form input[type=text],.jchp-form input[type=email],.jchp-form input[type=tel]{display:block;width:100%;margin-top:.35rem;padding:.8rem 1rem;border:2px solid #d9cdb8;border-radius:10px;font-size:1rem;background:#fff;color:#163b38}
.jchp-form .check{display:flex;gap:.6rem;align-items:flex-start;font-weight:600}
.jchp-form .check input{margin-top:.35rem;flex:none}
.jchp-form small{display:block;color:#4a5f5b;font-size:.8rem;line-height:1.5;margin:.3rem 0 1rem}
.jchp-form .check small{display:inline}
.jchp-form button{width:100%;background:#1f4d4a;color:#f8f1e0;border:0;border-radius:999px;padding:1rem 1.5rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;font-size:1rem;cursor:pointer;box-shadow:0 3px 0 #0c302d}
.jchp-form a{color:#1f4d4a;text-decoration:underline}
</style>
<!-- /wp:html -->''')

# header
logo=el("a",{"display":"block"},[img(LOGO,"Justin Case Home Pros logo","jchp-logo-img")],html_attrs={"href":"#home","aria-label":"Justin Case Home Pros"})
navlink=lambda t,h: tx("a",{"color":INK,"fontSize":"0.95rem","fontWeight":"700","textDecoration":"none","&:hover":{"color":"#b8791d"}},t,{"href":h})
nav=el("nav",{"columnGap":"1.6rem","display":"flex","@media (max-width:700px)":{"order":"3","width":"100%","justifyContent":"space-between","columnGap":"0.5rem"}},
       [navlink("Home","#home"),navlink("About","#about"),navlink("Features","#features"),navlink("Sign Up","#signup")],html_attrs={"aria-label":"Page sections"})
header=el("header",{"backgroundColor":CREAM,"borderBottom":"3px solid var(--accent)","paddingLeft":"1.25rem","paddingRight":"1.25rem","paddingTop":"0.6rem","paddingBottom":"0.6rem","position":"sticky","top":"0","zIndex":"50"},
  [wrap([logo,nav,button("Get Early Access","#signup",small=True)],{"alignItems":"center","columnGap":"2rem","display":"flex","flexWrap":"wrap","justifyContent":"space-between","rowGap":"0.6rem"})],full=True)
blocks.append(header)

# hero
trust=el("div",{"columnGap":"1.8rem","display":"flex","flexWrap":"wrap","marginTop":"1.8rem","rowGap":"0.6rem"},
  [tx("p",{"borderLeft":"3px solid var(--accent-2)","fontSize":"0.78rem","fontWeight":"800","letterSpacing":"0.08em","marginBottom":"0","paddingLeft":"0.7rem","textTransform":"uppercase"},t) for t in ("30 years experience","Licensed &amp; insured","Locally owned")])
hero_left=el("div",{},[
  tx("p",{"backgroundColor":TEAL,"borderRadius":"6px","color":CREAM,"display":"inline-block","fontFamily":OSW,"fontSize":"0.9rem","letterSpacing":"0.12em","marginBottom":"1.2rem","padding":"0.4rem 1rem","textTransform":"uppercase"},"Launching January 1, 2027"),
  tx("h1",{"color":TEAL,"fontFamily":OSW,"fontSize":"clamp(2.7rem,8.5vw,5.2rem)","fontWeight":"700","lineHeight":"1.02","marginBottom":"1.2rem","textTransform":"uppercase"},'Something Dependable <span style="display:block;color:#d78b20">Is Coming to Lower Bucks County.</span>'),
  para("Justin Case Home Pros — backed by 30 years of hands-on experience. Launching January 1, 2027.","#2c4a46",{"fontSize":"1.2rem","maxWidth":"33rem","marginBottom":"1.6rem"}),
  button("Get Early Access →","#signup"),trust])
hero_art=el("div",{"@media (max-width:1024px)":{"maxWidth":"460px","marginLeft":"auto","marginRight":"auto"}},[img(HERO,"Justin Case Home Pros toolbox mascot in front of a home","jchp-hero-img")])
blocks.append(section([wrap([grid("1.05fr 0.95fr",[hero_left,hero_art],"3rem","1fr")])],CREAM,pad="3.5rem",anchor="home",extra={"minHeight":"min(86vh,820px)","display":"flex","alignItems":"center","overflow":"hidden"}))

# about
about_text=el("div",{},[eyebrow("About"),h2("30 Years of Experience. "+script("One Trusted Name.")),
  para("Justin Case Home Pros is almost here — and we're bringing three decades of real, hands-on home repair experience with us."),
  para("Our team has spent 30 years combined fixing, installing, and maintaining homes across the region. Now we're bringing that same craftsmanship, honesty, and local trust directly to Lower Bucks County homeowners."),
  para("We're not a franchise and we're not a call center. We're local pros who show up, do it right, and stand behind every job — and we're putting the finishing touches on our new home online.")])
blocks.append(section([wrap([grid("1fr 1fr",[about_text,el("div",{},[img(ABOUT,"Justin Case Home Pros team","jchp-about-img")])],"4rem","1fr")])],CREAM,anchor="about"))

# features
def card(icon,title,body):
    return el("div",{"backgroundColor":"#fffaf0","border":"2px solid #d9cdb8","borderRadius":"18px","boxShadow":"5px 5px 0 rgba(20,59,55,.14)","padding":"1.8rem"},[
      tx("span",{"display":"block","fontSize":"2.4rem","marginBottom":"0.5rem"},icon),
      tx("h3",{"color":TEAL,"fontFamily":OSW,"fontSize":"1.3rem","fontWeight":"700","lineHeight":"1.1","marginBottom":"0.6rem","textTransform":"uppercase"},title),
      tx("p",{"color":INK,"fontSize":"0.98rem","lineHeight":"1.6","marginBottom":"0"},body)])
feats=grid("repeat(3,minmax(0,1fr))",[
  card("🔧","Decades of Hands-On Expertise","Thirty years in the field means we've seen it, fixed it, and done it right — from quick repairs to full installations. There's no learning curve here, just real experience on every job."),
  card("✅","Licensed, Insured &amp; Locally Trusted","Justin Case Home Pros is a PA-registered home improvement contractor (HICPA # [HICPA #]), fully insured, and based right here in Lower Bucks County — not an out-of-town crew."),
  card("💵","Honest Pricing, Guaranteed Results","No hidden fees, no upsells — just clear pricing and work backed by our satisfaction guarantee. If it's not right, we'll make it right.")],
  "1.2rem","1fr",extra={"alignItems":"stretch","marginTop":"2.5rem"})
blocks.append(section([wrap([eyebrow("Features",AMB),h2("Why Homeowners Will "+script("Trust Us.",AMB),CREAM),feats])],TEAL,anchor="features"))

# services
def svc(icon,title,body):
    return el("div",{"textAlign":"center"},[
      el("div",{"alignItems":"center","backgroundColor":TEAL,"border":"4px solid var(--accent-2)","borderRadius":"50%","display":"flex","height":"92px","justifyContent":"center","marginBottom":"0.9rem","marginLeft":"auto","marginRight":"auto","width":"92px"},[tx("span",{"fontSize":"2.6rem","lineHeight":"1"},icon)]),
      tx("h3",{"color":TEAL,"fontFamily":OSW,"fontSize":"1.15rem","fontWeight":"700","marginBottom":"0.3rem","textTransform":"uppercase"},title),
      tx("p",{"color":INK,"fontSize":"0.92rem","lineHeight":"1.5","marginBottom":"0"},body)])
svcs=el("div",{"columnGap":"1rem","display":"grid","gridTemplateColumns":"repeat(5,minmax(0,1fr))","marginTop":"2.5rem","rowGap":"2rem","@media (max-width:1024px)":{"gridTemplateColumns":"repeat(3,minmax(0,1fr))"},"@media (max-width:600px)":{"gridTemplateColumns":"repeat(2,minmax(0,1fr))"}},[
  svc("🔌","Installation","TVs, smart home devices, lighting, fixtures, cabinetry, and more"),
  svc("🔨","Repair","Drywall, doors, decks, fences, plumbing fixtures, and trim"),
  svc("🖌️","Maintenance","Gutter cleaning, touch-up painting, seasonal prep and holiday lights"),
  svc("🔑","Make Ready","Move-in/move-out prep, punch lists, and listing-ready touch-ups"),
  svc("🏠","Roof Repair","Leak patching, shingle replacement, and gutter inspections")])
blocks.append(section([wrap([eyebrow("What We Do"),h2("Handyman Services "+script("for Real Life.")),
  para("When we launch, Justin Case Home Pros will cover the full range of home repair needs across Lower Bucks County:",INK),svcs,
  tx("p",{"color":TEAL,"fontSize":"1.15rem","fontWeight":"800","marginBottom":"0","marginTop":"3rem","textAlign":"center"},"One call, text, or form submission covers it all — no matter how long your honey-do list is.")])],CREAM,anchor="services"))

# signup
form='''<!-- wp:html -->
<!-- PLACEHOLDER FORM: replace this block with your Gravity Forms block/shortcode -->
<form class="jchp-form" action="#" method="post" onsubmit="return false"><label>Full Name<input type="text" name="full_name" autocomplete="name" required></label><label>Email Address<input type="email" name="email" autocomplete="email" required></label><label>Mobile Phone (optional)<input type="tel" name="phone" autocomplete="tel"></label><label>Service Address / Zip Code (optional — helps us prioritize service areas)<input type="text" name="zip" autocomplete="postal-code"></label><label class="check"><input type="checkbox" name="optin" checked><span>Yes, notify me when Justin Case Home Pros launches and send me early-access offers. <small>(Optional; can opt out anytime.)</small></span></label><small>By submitting this form, you agree to Justin Case Home Pros' <a href="/terms-and-conditions/">Terms of Service</a> and <a href="/privacy-policy/">Privacy Policy</a>. Message and data rates may apply.</small><button type="submit">Notify Me at Launch</button></form>
<!-- /wp:html -->'''
sign_text=el("div",{},[eyebrow("Sign Up"),h2("Got a Honey-Do List? "+script("So Do We — Get On The List Now!",TEAL)),
  para("Every home has one — that running list of little jobs just waiting for the right pros to show up. Justin Case Home Pros is building our own list too, and we want you on it first.",TEAL),
  para("Sign up now and we'll let you know the moment we open for business in Lower Bucks County — plus you'll get early access to launch-day specials and [MEMBERSHIP NAME] founding-member pricing, so your honey-do list doesn't stand a chance.",TEAL)])
blocks.append(section([wrap([grid("1fr 1fr",[sign_text,el("div",{},[form])],"4rem","1fr",extra={"alignItems":"start"})])],AMB,anchor="signup"))

# footer
flink=lambda t,h: tx("a",{"color":CREAM,"textDecoration":"underline","textUnderlineOffset":"4px","textDecorationColor":"var(--accent-2)"},t,{"href":h})
blocks.append(el("footer",{"backgroundColor":DARK,"color":CREAM,"fontSize":"0.9rem","paddingTop":"2rem","paddingBottom":"2rem","paddingLeft":"1.25rem","paddingRight":"1.25rem","textAlign":"center"},[
  tx("p",{"color":CREAM,"marginBottom":"0.4rem"},"Justin Case Home Pros — Lower Bucks County, PA. Launching 2027."),
  el("div",{"columnGap":"1.2rem","display":"flex","justifyContent":"center"},[flink("Privacy Policy","/privacy-policy/"),flink("Terms and Conditions","/terms-and-conditions/")])],full=True))

head='''<!--
  Justin Case Home Pros — Coming 2027 pre-launch one-pager (GenerateBlocks / GeneratePress block markup)
  Slug: /  (static front page)
  SEO Title: Justin Case Home Pros | Coming 2027 to Lower Bucks County, PA
  Meta Description: Justin Case Home Pros is bringing 30 years of combined home repair experience to Lower Bucks County. Launching 2027 — join the list for early access and launch-day specials.
  Paste into the block editor Code editor. Placeholders: [HICPA #], [MEMBERSHIP NAME], the form block. Images are embedded; use Replace in the editor to swap in Media Library files.
-->
'''
open('homepage-generateblocks.html','w').write(head+"\n\n".join(blocks)+"\n")
