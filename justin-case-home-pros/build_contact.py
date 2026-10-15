import sys,io,contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from build_gb import *
import build_gb
build_gb.n[0]=500
STAR='<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 256 256"><path d="M240 128a15.79 15.79 0 0 1-10.5 15l-63.44 23.07L143 229.5a16 16 0 0 1-30 0l-23.06-63.44L26.5 143a16 16 0 0 1 0-30l63.44-23.06L113 26.5a16 16 0 0 1 30 0l23.07 63.44L229.5 113a15.79 15.79 0 0 1 10.5 15"></path></svg>'
BASE3="var(--base-3)"
def li(t):
    return tx("li",{"listStyleType":"none","display":"flex","alignItems":"flex-start","columnGap":"0.5em",".gb-shape svg":{"width":".9em","height":".9em","fill":"currentColor","color":"var(--accent-2)","marginTop":"4px"},"color":BASE3},
              f'<span class="gb-shape">{STAR}</span><span class="gb-text">{t}</span>')
def clink(t,href):
    return tx("a",{"color":BASE3,"fontWeight":"700","textDecoration":"underline","textDecorationColor":"var(--accent-2)","textUnderlineOffset":"4px","&:hover":{"color":"var(--accent-2)"}},t,{"href":href})
bul=el("ul",{"display":"flex","flexDirection":"column","rowGap":"8px","listStyleType":"none","margin":"0","padding":"0"},
  [li(t) for t in ("Serving Lower Bucks County, PA","30 years of combined hands-on experience","Licensed, insured &amp; locally owned","Honest pricing, guaranteed results","Installation, repair, maintenance, make ready &amp; roof repair","Early access to launch-day specials")])
details=el("div",{"marginTop":"2rem","display":"flex","flexDirection":"column","rowGap":"0.4rem"},[
  tx("p",{"color":BASE3,"marginBottom":"0","fontWeight":"800","textTransform":"uppercase","letterSpacing":"0.08em","fontSize":"0.85rem"},"Justin Case Home Pros LLC"),
  tx("p",{"color":BASE3,"marginBottom":"0"},"186 Levittown Parkway Unit 1, Levittown PA 19054"),
  el("div",{"display":"flex","flexWrap":"wrap","columnGap":"1.5rem","rowGap":"0.4rem"},[clink("215-935-4524","tel:2159354524"),clink("info@justincasehomepros.com","mailto:info@justincasehomepros.com")])])
content=el("div",{},[
  tx("h1",{"color":BASE3},"Let's Get Your List Started"),
  tx("p",{"color":BASE3},"Justin Case Home Pros is launching January 1, 2027 in Lower Bucks County. Tell us about your honey-do list and we'll be in touch."),
  tx("p",{"color":BASE3},"Send a message, call, or text — one contact covers it all, no matter how long your list is."),
  bul,details])
inner=el("div",{"maxWidth":"calc( var(--gb-container-width) / 2 + 32px )","marginLeft":"auto","@media (max-width:1024px)":{"maxWidth":"100%","paddingRight":"2rem","paddingLeft":"2rem"},"paddingRight":"6rem","paddingTop":"6rem","paddingBottom":"6rem"},[content])
left=el("div",{"display":"flex","justifyContent":"flex-end","alignItems":"center","flexGrow":"1","flexShrink":"1","flexBasis":"50%","backgroundColor":"var(--accent)"},[inner])
form_col=el("div",{"display":"flex","flexGrow":"1","flexShrink":"1","flexBasis":"50%","backgroundColor":"var(--base-2)","paddingLeft":"5rem","paddingRight":"5rem","paddingTop":"6rem","paddingBottom":"6rem","@media (max-width:1024px)":{"paddingLeft":"2rem","paddingRight":"2rem","paddingTop":"4rem","paddingBottom":"4rem"},"flexDirection":"column","justifyContent":"center"},[
  tx("h2",{"color":"var(--accent)"},"Send Us a Message"),
  tx("p",{"color":"#2c4a46"},"Fill out the form and we'll get back to you. Message and data rates may apply."),
  el("div",{"backgroundColor":"#fffaf0","border":"3px solid var(--accent)","borderRadius":"20px","boxShadow":"6px 6px 0 #123b38","padding":"1.8rem"},[
    '<!-- wp:shortcode -->\n[gravityforms id="1" title="false" description="false"]\n<!-- /wp:shortcode -->'])])
section_row=el("div",{"display":"flex","@media (max-width:1024px)":{"display":"block"},"minHeight":"100vh","borderBottomWidth":"1px","borderBottomStyle":"solid","borderBottomColor":"var(--base)"},[left,form_col],extra_cls="jchp-contact")
style='''<!-- wp:html -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&display=swap');
.page-id-contact .inside-article,.jchp-contact-page .inside-article{padding:0!important}
.jchp-contact h1,.jchp-contact h2{font-family:'Oswald','Arial Narrow',Arial,sans-serif;text-transform:uppercase;font-weight:700;line-height:1.05}
.jchp-contact h1{font-size:clamp(2.4rem,6vw,4rem)}
.jchp-contact h2{font-size:clamp(1.8rem,4vw,2.6rem)}
.jchp-logo-img img{width:210px;height:auto;display:block}
.jchp-logo-img{margin:0}
</style>
<!-- /wp:html -->'''
logo=el("a",{"display":"block"},[img(LOGO,"Justin Case Home Pros logo","jchp-logo-img")],html_attrs={"href":"/","aria-label":"Justin Case Home Pros"})
nav=el("nav",{"columnGap":"1.6rem","display":"flex","@media (max-width:700px)":{"order":"3","width":"100%","justifyContent":"space-between","columnGap":"0.5rem"}},
  [navlink("Home","/"),navlink("About","/#about"),navlink("Features","/#features"),navlink("Contact","/contact/")],html_attrs={"aria-label":"Primary"})
header=el("header",{"backgroundColor":CREAM,"borderBottom":"3px solid var(--accent)","paddingLeft":"1.25rem","paddingRight":"1.25rem","paddingTop":"0.6rem","paddingBottom":"0.6rem","position":"sticky","top":"0","zIndex":"50"},
  [wrap([logo,nav,button("Get Early Access","/#signup",small=True)],{"alignItems":"center","columnGap":"2rem","display":"flex","flexWrap":"wrap","justifyContent":"space-between","rowGap":"0.6rem"})],full=True)
foot=el("footer",{"backgroundColor":DARK,"color":CREAM,"fontSize":"0.9rem","paddingTop":"2rem","paddingBottom":"2rem","paddingLeft":"1.25rem","paddingRight":"1.25rem","textAlign":"center"},[
  tx("p",{"color":CREAM,"marginBottom":"0.4rem"},"Justin Case Home Pros — Lower Bucks County, PA. Launching 2027."),
  el("div",{"columnGap":"1.2rem","display":"flex","justifyContent":"center"},[flink("Privacy Policy","/privacy-policy/"),flink("Terms and Conditions","/terms-and-conditions/")])],full=True)
full=el("div",{},[header,section_row,foot],full=True)
head='''<!--
  Justin Case Home Pros — Contact page (GenerateBlocks markup)
  Slug: /contact
  SEO Title: Contact Justin Case Home Pros | Lower Bucks County, PA
  Meta Description: Contact Justin Case Home Pros in Levittown, PA. Call 215-935-4524 or send a message — launching January 1, 2027.
  Form: uses your existing Gravity Forms form 1 via shortcode — change the id if you want a different form.
-->
'''
open('contact.html','w').write(head+style+"\n\n"+header+"\n\n"+section_row+"\n\n"+foot+"\n")
