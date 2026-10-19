import sys; sys.path.insert(0,'.')
from lib import *
OUT='./'
def red(t): return f'<span style="color:var(--global-color-8)">{t}</span>'
def circ(paths,col,p,size="1.9rem",sw="3",ic="0.95rem"):
    svg=f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
    return el(shape(svg,{"color":WHITE,"display":"inline-flex","svg":{"fill":"none","height":ic,"stroke":"currentColor","width":ic}},p=p),{"backgroundColor":col,**{f"border{c}Radius":"100%" for c in ("TopLeft","TopRight","BottomLeft","BottomRight")},"display":"inline-flex","alignItems":"center","justifyContent":"center","width":size,"height":size,"flexShrink":"0","marginTop":"0.1rem"},p=p)
CHECK='<polyline points="20 6 9 17 4 12"/>'; X='<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>'
def chip(t,p):
    return tx(t,'span',{"display":"inline-block","backgroundColor":"rgba(255,255,255,0.1)","color":WHITE,"fontWeight":"600","fontSize":"0.9375rem","borderTopWidth":"1px","borderRightWidth":"1px","borderBottomWidth":"1px","borderLeftWidth":"1px","borderTopStyle":"solid","borderRightStyle":"solid","borderBottomStyle":"solid","borderLeftStyle":"solid","borderTopColor":"rgba(255,255,255,0.35)","borderRightColor":"rgba(255,255,255,0.35)","borderBottomColor":"rgba(255,255,255,0.35)","borderLeftColor":"rgba(255,255,255,0.35)","borderTopLeftRadius":"9999px","borderTopRightRadius":"9999px","borderBottomLeftRadius":"9999px","borderBottomRightRadius":"9999px","paddingTop":"0.4rem","paddingRight":"1rem","paddingBottom":"0.4rem","paddingLeft":"1rem"},p=p)
parts=[]
# 1 HERO
eyebrow=tx('Free · 30 minutes · Fridays','span',{"display":"inline-block","backgroundColor":RED,"color":WHITE,"fontSize":"0.8125rem","fontWeight":"700","textTransform":"uppercase","letterSpacing":"0.14em","borderTopLeftRadius":"9999px","borderTopRightRadius":"9999px","borderBottomLeftRadius":"9999px","borderBottomRightRadius":"9999px","paddingTop":"0.45rem","paddingRight":"1.25rem","paddingBottom":"0.45rem","paddingLeft":"1.25rem","marginBottom":"1.5rem"},p='hero')
left=el(eyebrow+'\n'+tx('Book your <span style="color:var(--base)">Focus Session</span>','h1',{"color":WHITE,"fontSize":"clamp(2.5rem, 5vw, 4rem)","lineHeight":"1.08","marginBottom":"0.75rem"},p='hero')+'\n'+bar('hero',False,"1.5rem")+'\n'+
 tx('In 30 minutes, we’ll find the one process worth fixing first. If I can help, I’ll tell you how. If I can’t, I’ll tell you that too.','p',{"color":WHITE,"fontSize":"1.375rem","lineHeight":"1.5","marginBottom":"2rem"},p='hero')+'\n'+
 el('\n'.join(chip(c,'hero') for c in ("Free","No obligation","30 minutes","Fridays")),{"display":"flex","flexWrap":"wrap","columnGap":"0.6rem","rowGap":"0.6rem"},p='hero'),p='hero')
embed='''<!-- wp:html -->
<div id="calendar-embed" style="min-height:34rem">
<!-- PASTE THE HIGHLEVEL CALENDAR EMBED CODE HERE (30-minute Focus Session). Replace this whole comment. -->
</div>
<!-- /wp:html -->'''
card=el(embed,{"backgroundColor":WHITE,**R12,"borderTopWidth":"6px","borderTopStyle":"solid","borderTopColor":RED,"boxShadow":"0 24px 56px rgba(0,0,0,0.35)",**pad("1.5rem"),"scrollMarginTop":"6rem"},p='hero',ha={"id":"calendar"})
hero_bg={"backgroundColor":NAVY,"backgroundImage":"radial-gradient(circle at 8% 15%, rgba(12,105,128,0.7) 0, transparent 45%), radial-gradient(circle at 95% 90%, rgba(196,57,29,0.35) 0, transparent 40%)"}
parts.append(section('hero',el(left+'\n'+card,{"display":"grid","gridTemplateColumns":"minmax(0, 0.9fr) minmax(0, 1.1fr)","columnGap":"3.5rem","rowGap":"2.5rem","alignItems":"start",M1024:{"gridTemplateColumns":"1fr"}},p='hero'),hero_bg,extra={"paddingBottom":"8rem"}))
# 2 WHAT WE'LL COVER
steps=[("1","What changed.","What’s growing, and where it’s starting to strain.",TEAL),("2","Where it breaks.","We’ll walk through a recent time something went wrong: who felt it and what it cost.",RED),("3","The one process to fix first.","Named out loud, with what “fixed” would look like.",NAVY),("4","Your next step.","Map It, the 3P Reset, or simply an idea you can use on Monday. No pressure either way.",TEAL)]
def row(n,t,b,col):
    num=el(tx(n,'span',{"color":WHITE,"fontFamily":"Lora, serif","fontWeight":"700","fontSize":"1.75rem","lineHeight":"1"},p='cov'),{"backgroundColor":col,"width":"4rem","height":"4rem","display":"flex","alignItems":"center","justifyContent":"center","flexShrink":"0",**{f"border{c}Radius":"100%" for c in ("TopLeft","TopRight","BottomLeft","BottomRight")},"boxShadow":"0 4px 10px rgba(0,0,0,0.15)",M767:{"width":"3rem","height":"3rem"}},p='cov')
    return el(num+'\n'+tx(f'<strong>{t}</strong> {b}','p',{"margin":"0","fontSize":"1.1875rem","lineHeight":"1.55"},p='cov'),{"display":"flex","columnGap":"1.5rem","alignItems":"center","backgroundColor":OFF,**R12,"borderLeftWidth":"6px","borderLeftStyle":"solid","borderLeftColor":col,"boxShadow":"0 4px 12px rgba(0,0,0,0.07)",**pad("1.5rem"),M767:{"columnGap":"1rem",**pad("1.25rem")},**LIFT},p='cov')
rows=el('\n'.join(row(*s) for s in steps),{"display":"flex","flexDirection":"column","rowGap":"1.25rem","maxWidth":"860px","marginLeft":"auto","marginRight":"auto"},p='cov')
parts.append(section('cov',tx('What we’ll cover','h2',{"textAlign":"center","marginBottom":"0.75rem"},p='cov',gc=["gbp-section__headline"])+'\n'+bar('cov')+'\n'+rows,WHITE,div=NAVY))
# 3 BEFORE WE TALK
call=el(el(circ('<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',TEAL,'bef',"3.5rem","1.75","1.7rem"),{"flexShrink":"0"},p='bef')+'\n'+el(tx('Get more out of the call','h2',{"fontSize":"1.75rem","marginBottom":"0.75rem"},p='bef')+'\n'+tx('Take the <a href="/scorecard/" style="color:var(--accent);font-weight:700">5-minute Growing Pains Scorecard</a> first. I’ll review your results before we meet, so we can skip straight to what matters.','p',{"margin":"0","fontSize":"1.1875rem","lineHeight":"1.6"},p='bef'),p='bef'),
 {"display":"flex","columnGap":"1.75rem","alignItems":"center","backgroundColor":WHITE,"maxWidth":"860px","marginLeft":"auto","marginRight":"auto",**R12,"borderTopWidth":"3px","borderRightWidth":"3px","borderBottomWidth":"3px","borderLeftWidth":"3px","borderTopStyle":"dashed","borderRightStyle":"dashed","borderBottomStyle":"dashed","borderLeftStyle":"dashed","borderTopColor":TEAL,"borderRightColor":TEAL,"borderBottomColor":TEAL,"borderLeftColor":TEAL,**pad("2.25rem"),M767:{"flexDirection":"column","alignItems":"flex-start",**pad("1.5rem")}},p='bef')
parts.append(section('bef',call,CREAM,div=WHITE,extra={"paddingBottom":"6rem"}))
# 4 WHO IT'S FOR
fit=["An executive director, founder, COO or operations lead","At a growing nonprofit or mission-driven business, roughly 10–75 staff","Feeling the strain of growth: dropped handoffs, invisible overdue work, everything routing through you"]
nofit=["Manufacturing or production-line process work","A full-time operations hire or ongoing fractional executive"]
def col(title,items,colr,ic,p):
    return el(tx(title,'h3',{"color":colr,"marginBottom":"1.25rem"},p=p)+'\n'+el('\n'.join(el(circ(ic,colr,p)+'\n'+tx(t,'p',{"margin":"0","fontWeight":"600","lineHeight":"1.45"},p=p),{"display":"flex","columnGap":"0.9rem","alignItems":"flex-start"},p=p) for t in items),{"display":"flex","flexDirection":"column","rowGap":"1rem"},p=p),
      {"backgroundColor":OFF,**R12,"borderTopWidth":"6px","borderTopStyle":"solid","borderTopColor":colr,"boxShadow":"0 4px 12px rgba(0,0,0,0.07)",**pad("2.25rem"),**LIFT},p=p)
cols=el(col('A good fit if you are:',fit,TEAL,CHECK,'who')+'\n'+col('Not a fit if you need:',nofit,RED,X,'who'),{"display":"grid","gridTemplateColumns":"repeat(2, minmax(0, 1fr))","columnGap":"2rem","rowGap":"2rem","alignItems":"stretch",M1024:{"gridTemplateColumns":"1fr"}},p='who')
parts.append(section('who',tx('Who it’s for','h2',{"textAlign":"center","marginBottom":"0.75rem"},p='who',gc=["gbp-section__headline"])+'\n'+bar('who')+'\n'+cols,WHITE,div=CREAM))
# 5 TESTIMONIAL
qm=tx('“','span',{"display":"block","fontFamily":"Lora, serif","fontSize":"7rem","fontWeight":"700","lineHeight":"0.8","color":RED,"marginBottom":"0.5rem"},p='tst')
quote=el(qm+'\n<!-- TESTIMONIAL: swap in one approved quote. Candidate from the live site below. -->\n'+tx('Heather is such an amazing person to work with, so efficient, effective, and intelligent.','p',{"fontFamily":"Lora, serif","fontSize":"1.75rem","lineHeight":"1.45","fontWeight":"600","margin":"0",M767:{"fontSize":"1.375rem"}},p='tst'),{"textAlign":"center","maxWidth":"760px","marginLeft":"auto","marginRight":"auto"},p='tst')
parts.append(section('tst',quote,CREAM,div=WHITE))
# 6 FOOTER NOTE
note=el(tx('Can’t find a time that works? <a href="/contact/" style="color:var(--accent);font-weight:700">Send me a message →</a> and I’ll reply on Friday.','p',{"margin":"0","fontSize":"1.125rem"},p='fn'),{"textAlign":"center"},p='fn')
parts.append(section('fn',note,WHITE,div=CREAM,extra={"paddingTop":"6rem","paddingBottom":"4rem"}))
open(OUT+'06-welcome.html','w').write('\n\n'.join(parts)+'\n')
