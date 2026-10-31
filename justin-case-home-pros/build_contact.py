from brand import *
gb_helpers.n[0]=500
STAR='<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 256 256"><path d="M240 128a15.79 15.79 0 0 1-10.5 15l-63.44 23.07L143 229.5a16 16 0 0 1-30 0l-23.06-63.44L26.5 143a16 16 0 0 1 0-30l63.44-23.06L113 26.5a16 16 0 0 1 30 0l23.07 63.44L229.5 113a15.79 15.79 0 0 1 10.5 15"></path></svg>'
def li(t):
    return tx("li",{"listStyleType":"none","display":"flex","alignItems":"flex-start","columnGap":"0.5em",".gb-shape svg":{"width":".9em","height":".9em","fill":"currentColor","color":ORG,"marginTop":"4px"},"color":CREAM},
              f'<span class="gb-shape">{STAR}</span><span class="gb-text">{t}</span>')
def clink(t,href):
    return tx("a",{"color":CREAM,"fontWeight":"700","textDecoration":"underline","textDecorationColor":ORG,"textUnderlineOffset":"4px","&:hover":{"color":ORG}},t,{"href":href})
bul=el("ul",{"display":"flex","flexDirection":"column","rowGap":"8px","listStyleType":"none","margin":"0","padding":"0"},
  [li(t) for t in ("Serving Lower Bucks County, PA","30 years of combined hands-on experience","Licensed, insured &amp; locally owned","Honest pricing, guaranteed results","Installation, repair, maintenance, make ready &amp; roof repair","Early access to launch-day specials")])
details=el("div",{"marginTop":"2rem","display":"flex","flexDirection":"column","rowGap":"0.4rem"},[
  tx("p",{"color":CREAM,"marginBottom":"0","fontWeight":"800","textTransform":"uppercase","letterSpacing":"0.08em","fontSize":"0.85rem"},"Justin Case Home Pros LLC"),
  tx("p",{"color":CREAM,"marginBottom":"0"},"186 Levittown Parkway Unit 1, Levittown PA 19054"),
  el("div",{"display":"flex","flexWrap":"wrap","columnGap":"1.5rem","rowGap":"0.4rem"},[clink("215-935-4524","tel:2159354524"),clink("info@justincasehomepros.com","mailto:info@justincasehomepros.com")])])
content=el("div",{},[
  tx("h1",{"color":CREAM},"Let's Get Your "+hl("List Started")),
  tx("p",{"color":CREAM},"Justin Case Home Pros is launching January 1, 2027 in Lower Bucks County. Tell us about your honey-do list and we'll be in touch."),
  tx("p",{"color":CREAM},"Send a message, call, or text — one contact covers it all, no matter how long your list is."),
  bul,details])
inner=el("div",{"maxWidth":"calc( var(--gb-container-width) / 2 + 32px )","marginLeft":"auto","@media (max-width:1024px)":{"maxWidth":"100%","paddingRight":"2rem","paddingLeft":"2rem"},"paddingRight":"6rem","paddingTop":"6rem","paddingBottom":"6rem"},[content])
left=el("div",{"display":"flex","justifyContent":"flex-end","alignItems":"center","flexGrow":"1","flexShrink":"1","flexBasis":"50%","backgroundColor":TEAL},[inner])
form_col=el("div",{"display":"flex","flexGrow":"1","flexShrink":"1","flexBasis":"50%","backgroundColor":CREAM,"paddingLeft":"5rem","paddingRight":"5rem","paddingTop":"6rem","paddingBottom":"6rem","@media (max-width:1024px)":{"paddingLeft":"2rem","paddingRight":"2rem","paddingTop":"4rem","paddingBottom":"4rem"},"flexDirection":"column","justifyContent":"center"},[
  tx("h2",{"color":TEAL},"Send Us a Message"),
  tx("p",{"color":INK},"Fill out the form and we'll get back to you. Message and data rates may apply."),
  el("div",{"backgroundColor":TINT,"border":f"3px solid {TEAL}","borderRadius":"24px","boxShadow":f"6px 6px 0 {ORG}","padding":"1.2rem"},[
    """<!-- wp:html -->
<iframe src="https://api.manyresults.com/widget/form/7UdAeBIF9M5iTJulQCte" style="width:100%;height:1129px;border:none;border-radius:3px" id="inline-7UdAeBIF9M5iTJulQCte" data-layout="{'id':'INLINE'}" data-trigger-type="alwaysShow" data-trigger-value="" data-activation-type="alwaysActivated" data-activation-value="" data-deactivation-type="neverDeactivate" data-deactivation-value="" data-form-name="Contact Us" data-height="1129" data-layout-iframe-id="inline-7UdAeBIF9M5iTJulQCte" data-form-id="7UdAeBIF9M5iTJulQCte" data-cookie-consent="true" data-cookie-consent-provider="auto" title="Contact Us"></iframe>
<script src="https://api.manyresults.com/js/form_embed.js"></script>
<!-- /wp:html -->"""])])
row=el("div",{"display":"flex","@media (max-width:1024px)":{"display":"block"},"minHeight":"100vh"},[left,form_col],extra_cls="jchp-contact")
style="<!-- wp:html -->\n<style>\n"+STYLE_COMMON+f'''
.jchp-contact h1,.jchp-contact h2{{font-family:{FONT};font-weight:700;line-height:1.1}}
.jchp-contact h1{{font-size:clamp(2.4rem,6vw,4rem)}}
.jchp-contact h2{{font-size:clamp(1.8rem,4vw,2.6rem)}}
</style>
<!-- /wp:html -->'''
head='''<!--
  Justin Case Home Pros — Contact page (GenerateBlocks markup) — Atomic Age brand direction
  Slug: /contact
  SEO Title: Contact Justin Case Home Pros | Lower Bucks County, PA
  Meta Description: Contact Justin Case Home Pros in Levittown, PA. Call 215-935-4524 or send a message — launching January 1, 2027.
  Form: Many Results 'Contact Us' embed (form id 7UdAeBIF9M5iTJulQCte).
-->
'''
open('contact.html','w').write(head+style+"\n\n"+header([("Home","/"),("About","/#about"),("Features","/#features"),("Contact","/contact/")],"/#signup")+"\n\n"+row+"\n\n"+footer()+"\n")
