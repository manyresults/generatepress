import sys; sys.path.insert(0,'.')
from lib import *
OUT='./'
U='https://3p-allies.com/wp-content/uploads/'
def red(t): return f'<span style="color:var(--global-color-8)">{t}</span>'
def pill(label,p,light=True):
    return tx(label,'span',{"display":"inline-block","backgroundColor":"rgba(255,255,255,0.1)" if light else WHITE,"color":WHITE if light else NAVY,"fontWeight":"600","fontSize":"0.9375rem","borderTopWidth":"1px","borderRightWidth":"1px","borderBottomWidth":"1px","borderLeftWidth":"1px","borderTopStyle":"solid","borderRightStyle":"solid","borderBottomStyle":"solid","borderLeftStyle":"solid","borderTopColor":"rgba(255,255,255,0.35)","borderRightColor":"rgba(255,255,255,0.35)","borderBottomColor":"rgba(255,255,255,0.35)","borderLeftColor":"rgba(255,255,255,0.35)","borderTopLeftRadius":"9999px","borderTopRightRadius":"9999px","borderBottomLeftRadius":"9999px","borderBottomRightRadius":"9999px","paddingTop":"0.4rem","paddingRight":"1rem","paddingBottom":"0.4rem","paddingLeft":"1rem"},p=p)
DOWN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:1.1rem;height:1.1rem;margin-left:0.6rem"><path d="M12 5v14M5 12l7 7 7-7"/></svg>'
parts=[]
# 1 HERO
eyebrow=tx('Free · 5 minutes','span',{"display":"inline-block","backgroundColor":RED,"color":WHITE,"fontSize":"0.8125rem","fontWeight":"700","textTransform":"uppercase","letterSpacing":"0.14em","borderTopLeftRadius":"9999px","borderTopRightRadius":"9999px","borderBottomLeftRadius":"9999px","borderBottomRightRadius":"9999px","paddingTop":"0.45rem","paddingRight":"1.25rem","paddingBottom":"0.45rem","paddingLeft":"1.25rem","marginBottom":"1.5rem"},p='hero')
areas=el('\n'.join(pill(a,'hero') for a in ("Repetitive work","Handoffs","Triggers and visibility","Documentation","Tools")),{"display":"flex","flexWrap":"wrap","justifyContent":"center","columnGap":"0.6rem","rowGap":"0.6rem","marginTop":"2.25rem"},p='hero')
startbtn=tx(f'Start the Scorecard{DOWN}','a',{"display":"inline-flex","alignItems":"center","backgroundColor":RED,"color":WHITE,"fontWeight":"700","fontSize":"1.125rem","borderTopWidth":"3px","borderRightWidth":"3px","borderBottomWidth":"3px","borderLeftWidth":"3px","borderTopStyle":"solid","borderRightStyle":"solid","borderBottomStyle":"solid","borderLeftStyle":"solid","borderTopColor":RED,"borderRightColor":RED,"borderBottomColor":RED,"borderLeftColor":RED,"borderTopLeftRadius":"9999px","borderTopRightRadius":"9999px","borderBottomLeftRadius":"9999px","borderBottomRightRadius":"9999px","paddingTop":"1rem","paddingRight":"2.25rem","paddingBottom":"1rem","paddingLeft":"2.25rem","textDecoration":"none","transition":"transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease","&:is(:hover, :focus)":{"backgroundColor":TEAL,"borderColor":TEAL,"color":WHITE,"transform":"translateY(-3px)","boxShadow":"0 10px 20px rgba(0,0,0,0.25)"}},p='hero',ha={"href":"#scorecard"})
hero=el(eyebrow+'\n'+tx('How much is growth straining <span style="color:var(--base)">your operations?</span>','h1',{"color":WHITE,"fontSize":"clamp(2.25rem, 5vw, 3.75rem)","lineHeight":"1.1","marginBottom":"0.75rem"},p='hero')+'\n'+bar('hero',True,"1.5rem")+'\n'+tx('Ten quick statements. An instant score, and your biggest crack.','p',{"color":WHITE,"fontSize":"1.375rem","marginBottom":"2rem"},p='hero')+'\n'+startbtn+'\n'+areas,{"textAlign":"center","maxWidth":"820px","marginLeft":"auto","marginRight":"auto"},p='hero')
hero_bg={"backgroundColor":NAVY,"backgroundImage":"radial-gradient(circle at 8% 15%, rgba(12,105,128,0.7) 0, transparent 45%), radial-gradient(circle at 95% 90%, rgba(196,57,29,0.35) 0, transparent 40%)"}
parts.append(section('hero',hero,hero_bg,extra={"paddingTop":"6rem","paddingBottom":"8rem"}))
# 2 EMBED
embed_html='''<!-- wp:html -->
<div id="scorecard-embed" style="min-height:28rem">
<!-- PASTE THE HIGHLEVEL SCORECARD EMBED CODE HERE (replace this whole comment). The quiz, capture step and results screen are all inside the embed. -->
</div>
<!-- /wp:html -->'''
card=el(embed_html,{"backgroundColor":WHITE,**R12,"borderTopWidth":"6px","borderTopStyle":"solid","borderTopColor":RED,"boxShadow":"0 24px 56px rgba(10,31,68,0.22)",**pad("2.5rem"),M767:pad("1.25rem"),"maxWidth":"860px","marginLeft":"auto","marginRight":"auto","transform":"translateY(-5rem)","marginBottom":"-5rem","scrollMarginTop":"6rem"},p='emb',ha={"id":"scorecard"})
parts.append(section('emb',card,CREAM,extra={"paddingTop":"0","paddingBottom":"6rem","overflow":"visible","zIndex":"2"}))
# 3 WHAT YOU'LL GET
def gcard(num,title,body,col,ic):
    n=tx(num,'span',{"position":"absolute","top":"0.5rem","right":"1.25rem","fontFamily":"Lora, serif","fontSize":"6.5rem","fontWeight":"700","lineHeight":"1","color":col,"opacity":"0.12","pointerEvents":"none"},p='get')
    svg=f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ic}</svg>'
    circ=el(shape(svg,{"color":WHITE,"display":"inline-flex","svg":{"fill":"none","height":"1.6rem","stroke":"currentColor","width":"1.6rem"}},p='get'),{"backgroundColor":col,"borderTopLeftRadius":"100%","borderTopRightRadius":"100%","borderBottomLeftRadius":"100%","borderBottomRightRadius":"100%","display":"inline-flex","alignItems":"center","justifyContent":"center","width":"3.25rem","height":"3.25rem","marginBottom":"1.25rem"},p='get')
    return el(n+'\n'+circ+'\n'+tx(f'<strong>{title}</strong> {body}','p',{"margin":"0","position":"relative","fontSize":"1.125rem","lineHeight":"1.55"},p='get'),{"backgroundColor":OFF,"position":"relative","overflow":"hidden",**R12,"borderTopWidth":"6px","borderTopStyle":"solid","borderTopColor":col,"boxShadow":"0 4px 12px rgba(0,0,0,0.07)",**pad("2rem"),**LIFT},p='get')
gets=[("01","An instant score","across five areas where growth usually breaks things first.",TEAL,'<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>'),
("02","Your biggest crack,","named in an email breakdown by section.",RED,'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>'),
("03","A clear next step,","whether that’s a small fix you can make yourself or a free Focus Session.",NAVY,'<path d="M5 12h14M13 6l6 6-6 6"/>')]
cards=el('\n'.join(gcard(*g) for g in gets),{"display":"grid","gridTemplateColumns":"repeat(3, minmax(0, 1fr))","columnGap":"2rem","rowGap":"2rem","alignItems":"stretch",M1024:{"gridTemplateColumns":"1fr"}},p='get')
parts.append(section('get',tx('What you’ll get','h2',{"textAlign":"center","marginBottom":"0.75rem"},p='get',gc=["gbp-section__headline"])+'\n'+bar('get')+'\n'+cards,WHITE,div=CREAM))
# 4 TRUST LINE
face=imgid=f'<!-- wp:image {{"id":43734,"sizeSlug":"full","linkDestination":"none"}} -->\n<figure class="wp-block-image size-full"><img src="{U}2025/04/heather-shafter-headshot.png" alt="Heather Shafter" class="wp-image-43734" style="margin:0;width:6rem;height:6rem;border-radius:100%;object-fit:cover;object-position:top;display:block;border:4px solid var(--global-color-8);background:var(--base-4)"/></figure>\n<!-- /wp:image -->'
trust=el(el(face,{"display":"flex","justifyContent":"center","marginBottom":"1.25rem"},p='tru')+'\n'+tx('Created by <strong>Heather Shafter</strong>, 3P Allies — an operations leader who’s spent two decades helping mission-driven organizations run as well as they mean to.','p',{"fontFamily":"Lora, serif","fontSize":"1.375rem","lineHeight":"1.5","margin":"0",M767:{"fontSize":"1.1875rem"}},p='tru'),{"textAlign":"center","maxWidth":"720px","marginLeft":"auto","marginRight":"auto"},p='tru')
parts.append(section('tru',trust,CREAM,div=WHITE,extra={"paddingBottom":"5rem"}))
open(OUT+'05-scorecard.html','w').write('\n\n'.join(parts)+'\n')
