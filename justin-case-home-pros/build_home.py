from brand import *
blocks=[]
blocks.append("<!-- wp:html -->\n<style>\n"+STYLE_COMMON+f'''
.jchp-form{{background:{TINT};border:3px solid {CREAM};border-radius:24px;padding:1.8rem;font-size:1rem;box-shadow:6px 6px 0 {ORG}}}
.jchp-form label{{display:block;font-weight:700;font-size:.9rem;margin-bottom:1rem;color:{INK}}}
.jchp-form input[type=text],.jchp-form input[type=email],.jchp-form input[type=tel]{{display:block;width:100%;margin-top:.35rem;padding:.8rem 1rem;border:2px solid {TEAL};border-radius:12px;font-size:1rem;background:#fff;color:{INK}}}
.jchp-form .check{{display:flex;gap:.6rem;align-items:flex-start;font-weight:600}}
.jchp-form .check input{{margin-top:.35rem;flex:none}}
.jchp-form small{{display:block;color:{INK};font-size:.8rem;line-height:1.5;margin:.3rem 0 1rem}}
.jchp-form .check small{{display:inline}}
.jchp-form button{{width:100%;background:{ORG};color:{INK};border:0;border-radius:999px;padding:1rem 1.5rem;font-weight:600;font-family:'Fredoka',sans-serif;font-size:1.1rem;cursor:pointer;box-shadow:0 3px 0 #a8441b}}
.jchp-form a{{color:{TEAL};text-decoration:underline}}
</style>
<!-- /wp:html -->''')
blocks.append(header([("Home","#home"),("About","#about"),("Features","#features"),("Sign Up","#signup")],"#signup"))

trust=el("div",{"columnGap":"1.8rem","display":"flex","flexWrap":"wrap","marginTop":"1.8rem","rowGap":"0.6rem"},
  [tx("p",{"borderLeft":f"4px solid {ORG}","color":INK,"fontSize":"0.85rem","fontWeight":"800","letterSpacing":"0.06em","marginBottom":"0","paddingLeft":"0.7rem","textTransform":"uppercase"},t) for t in ("30 years experience","Licensed &amp; insured","Locally owned")])
hero_left=el("div",{},[
  tx("p",{"backgroundColor":TEAL,"borderRadius":"999px","color":CREAM,"display":"inline-block","fontFamily":FONT,"fontSize":"1rem","fontWeight":"500","marginBottom":"1.2rem","padding":"0.35rem 1.1rem"},"✦ Launching January 1, 2027"),
  tx("h1",{"color":TEAL,"fontFamily":FONT,"fontSize":"clamp(2.7rem,7.5vw,4.8rem)","fontWeight":"700","lineHeight":"1.05","marginBottom":"1.2rem"},"Something Dependable Is Coming to "+hl("Lower Bucks County.")),
  para("Justin Case Home Pros — backed by 30 years of hands-on experience. Launching January 1, 2027.",INK,{"fontSize":"1.2rem","maxWidth":"33rem","marginBottom":"1.6rem"}),
  button("Get Early Access →","#signup"),trust])
hero_art=el("div",{"@media (max-width:1024px)":{"maxWidth":"460px","marginLeft":"auto","marginRight":"auto"}},[img(HERO,"Illustration of a home with an orbit line and starbursts","jchp-hero-img")])
blocks.append(section([wrap([grid("1.05fr 0.95fr",[hero_left,hero_art],"3rem","1fr")])],CREAM,pad="3.5rem",anchor="home",extra={"minHeight":"min(86vh,820px)","display":"flex","alignItems":"center","overflow":"hidden"}))

about_text=el("div",{},[eyebrow("About"),h2("30 Years of Experience. "+hl("One Trusted Name.")),
  para("Justin Case Home Pros is almost here — and we're bringing three decades of real, hands-on home repair experience with us."),
  para("Our team has spent 30 years combined fixing, installing, and maintaining homes across the region. Now we're bringing that same craftsmanship, honesty, and local trust directly to Lower Bucks County homeowners."),
  para("We're not a franchise and we're not a call center. We're local pros who show up, do it right, and stand behind every job — and we're putting the finishing touches on our new home online.")])
blocks.append(section([wrap([grid("1fr 1fr",[about_text,el("div",{},[img(ABOUT,"","jchp-about-img")])],"4rem","1fr")])],CREAM,anchor="about"))

def card(icon,title,body):
    return el("div",{"backgroundColor":TINT,"border":f"3px solid {ORG}","borderRadius":"24px","padding":"1.8rem"},[
      tx("span",{"display":"block","fontSize":"2.4rem","marginBottom":"0.5rem"},icon),
      tx("h3",{"color":TEAL,"fontFamily":FONT,"fontSize":"1.4rem","fontWeight":"600","lineHeight":"1.15","marginBottom":"0.6rem"},title),
      tx("p",{"color":INK,"fontSize":"0.98rem","lineHeight":"1.6","marginBottom":"0"},body)])
feats=grid("repeat(3,minmax(0,1fr))",[
  card("🔧","Decades of Hands-On Expertise","Thirty years in the field means we've seen it, fixed it, and done it right — from quick repairs to full installations. There's no learning curve here, just real experience on every job."),
  card("✅","Licensed, Insured &amp; Locally Trusted","Justin Case Home Pros is a PA-registered home improvement contractor (HICPA # [HICPA #]), fully insured, and based right here in Lower Bucks County — not an out-of-town crew."),
  card("💵","Honest Pricing, Guaranteed Results","No hidden fees, no upsells — just clear pricing and work backed by our satisfaction guarantee. If it's not right, we'll make it right.")],
  "1.2rem","1fr",extra={"alignItems":"stretch","marginTop":"2.5rem"})
blocks.append(section([wrap([eyebrow("Features",CREAM),h2("Why Homeowners Will "+hl("Trust Us."),CREAM),feats])],TEAL,anchor="features"))

def svc(icon,title,body):
    return el("div",{"textAlign":"center"},[
      el("div",{"alignItems":"center","backgroundColor":TEAL,"border":f"4px solid {ORG}","borderRadius":"50%","display":"flex","height":"92px","justifyContent":"center","marginBottom":"0.9rem","marginLeft":"auto","marginRight":"auto","width":"92px"},[tx("span",{"fontSize":"2.6rem","lineHeight":"1"},icon)]),
      tx("h3",{"color":TEAL,"fontFamily":FONT,"fontSize":"1.2rem","fontWeight":"600","marginBottom":"0.3rem"},title),
      tx("p",{"color":INK,"fontSize":"0.92rem","lineHeight":"1.5","marginBottom":"0"},body)])
svcs=el("div",{"columnGap":"1rem","display":"grid","gridTemplateColumns":"repeat(5,minmax(0,1fr))","marginTop":"2.5rem","rowGap":"2rem","@media (max-width:1024px)":{"gridTemplateColumns":"repeat(3,minmax(0,1fr))"},"@media (max-width:600px)":{"gridTemplateColumns":"repeat(2,minmax(0,1fr))"}},[
  svc("🔌","Installation","TVs, smart home devices, lighting, fixtures, cabinetry, and more"),
  svc("🔨","Repair","Drywall, doors, decks, fences, plumbing fixtures, and trim"),
  svc("🖌️","Maintenance","Gutter cleaning, touch-up painting, seasonal prep and holiday lights"),
  svc("🔑","Make Ready","Move-in/move-out prep, punch lists, and listing-ready touch-ups"),
  svc("🏠","Roof Repair","Leak patching, shingle replacement, and gutter inspections")])
blocks.append(section([wrap([eyebrow("What We Do"),h2("Handyman Services "+hl("for Real Life.")),
  para("When we launch, Justin Case Home Pros will cover the full range of home repair needs across Lower Bucks County:"),svcs,
  tx("p",{"color":TEAL,"fontFamily":FONT,"fontSize":"1.3rem","fontWeight":"600","marginBottom":"0","marginTop":"3rem","textAlign":"center"},"One call, text, or form submission covers it all — no matter how long your honey-do list is.")])],CREAM,anchor="services"))

form='''<!-- wp:html -->
<!-- PLACEHOLDER FORM: replace this block with your Many Results sign-up form embed -->
<form class="jchp-form" action="#" method="post" onsubmit="return false"><label>Full Name<input type="text" name="full_name" autocomplete="name" required></label><label>Email Address<input type="email" name="email" autocomplete="email" required></label><label>Mobile Phone (optional)<input type="tel" name="phone" autocomplete="tel"></label><label>Service Address / Zip Code (optional — helps us prioritize service areas)<input type="text" name="zip" autocomplete="postal-code"></label><label class="check"><input type="checkbox" name="optin" checked><span>Yes, notify me when Justin Case Home Pros launches and send me early-access offers. <small>(Optional; can opt out anytime.)</small></span></label><small>By submitting this form, you agree to Justin Case Home Pros' <a href="/terms-and-conditions/">Terms of Service</a> and <a href="/privacy-policy/">Privacy Policy</a>. Message and data rates may apply.</small><button type="submit">Notify Me at Launch</button></form>
<!-- /wp:html -->'''
sign_text=el("div",{},[eyebrow("Sign Up",CREAM),h2("Got a Honey-Do List? So Do We — "+hl("Get On The List Now!"),CREAM),
  para("Every home has one — that running list of little jobs just waiting for the right pros to show up. Justin Case Home Pros is building our own list too, and we want you on it first.",CREAM),
  para("Sign up now and we'll let you know the moment we open for business in Lower Bucks County — plus you'll get early access to launch-day specials and [MEMBERSHIP NAME] founding-member pricing, so your honey-do list doesn't stand a chance.",CREAM)])
blocks.append(section([wrap([grid("1fr 1fr",[sign_text,el("div",{},[form])],"4rem","1fr",extra={"alignItems":"start"})])],TEAL,anchor="signup"))
blocks.append(footer())
head='''<!--
  Justin Case Home Pros — Coming 2027 pre-launch one-pager (GenerateBlocks markup) — Atomic Age brand direction
  Slug: /  (static front page)
  SEO Title: Justin Case Home Pros | Coming 2027 to Lower Bucks County, PA
  Meta Description: Justin Case Home Pros is bringing 30 years of combined home repair experience to Lower Bucks County. Launching 2027 — join the list for early access and launch-day specials.
  Palette: Petrol Teal #164E53, Atomic Orange #E66F36, Buttercream #FFF2D5, Ink #293638. Headline font: Fredoka (provisional — brand kit has not fixed final fonts).
  Placeholders: [HICPA #], [MEMBERSHIP NAME], the sign-up form, and the emblem/illustrations (concept artwork, not final logo).
-->
'''
open('homepage-generateblocks.html','w').write(head+"\n\n".join(blocks)+"\n")
