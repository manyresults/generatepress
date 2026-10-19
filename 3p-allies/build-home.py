import json,re,itertools
n=itertools.count(1)
def uid(p): return f"{p}{next(n):03d}"
def kebab(k): return re.sub(r'([A-Z])',lambda m:'-'+m.group(1).lower(),k)
def css(sel,st):
    base=';'.join(f"{kebab(k)}:{v}" for k,v in sorted(st.items()) if not isinstance(v,dict) and k!='svg')
    out=f".{sel}{{{base}}}" if base else ''
    if 'svg' in st:
        out+=f".{sel} svg{{"+';'.join(f"{kebab(k)}:{v}" for k,v in sorted(st['svg'].items()))+"}"
    for k,v in st.items():
        if k.startswith('@media'):
            out+=f"{k.replace(':',': ',1).replace('(max-width: ','(max-width: ')}{{.{sel}{{"+';'.join(f"{kebab(a)}:{b}" for a,b in sorted(v.items()))+"}}"
    for k,v in st.items():
        if k.startswith('&'):
            out+=f".{sel}{k[1:]}{{"+';'.join(f"{kebab(a)}:{b}" for a,b in sorted(v.items()))+"}"
    return out
def attrs(d):
    s=json.dumps(d,separators=(',',':'),ensure_ascii=False)
    return s.replace('--','\\u002d\\u002d').replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
def block(kind,tag,content,st=None,gc=None,ha=None,extra_cls='',prefix='x',html_attr=None,align=False,inner_attr=''):
    i=uid(prefix); st=st or {}
    cls={'element':'gb-element','text':'gb-text'}[kind]
    sel=f"{cls}-{i}"
    a={"uniqueId":i,"tagName":tag}
    if st: a["styles"]=st; a["css"]=css(sel,st)
    if gc: a["globalClasses"]=gc
    if ha: a["htmlAttributes"]=ha
    if align: a["align"]="full"
    a["className"]=cls+(" alignfull" if align else "")
    classes=f"{sel} {cls}"+(" alignfull" if align else "")+(" "+" ".join(gc) if gc else "")
    hattr=''.join(f' {k}="{v}"' for k,v in (ha or {}).items())
    open_=f'<!-- wp:generateblocks/{kind} {attrs(a)} -->\n<{tag} class="{classes}"{hattr}>'
    if kind=='element':
        return f'{open_}\n{content}\n</{tag}>\n<!-- /wp:generateblocks/element -->'
    return f'{open_}{content}</{tag}>\n<!-- /wp:generateblocks/text -->'
def el(content,st=None,tag='div',p='el',**k): return block('element',tag,content,st,prefix=p,**k)
def tx(content,tag='p',st=None,p='tx',**k): return block('text',tag,content,st,prefix=p,**k)
def shape(svg,st,p='sh'):
    i=uid(p); sel=f"gb-shape-{i}"
    a={"uniqueId":i,"html":svg,"styles":st,"css":css(sel,st)}
    return f'<!-- wp:generateblocks/shape {attrs(a)} -->\n<span class="gb-shape {sel}">{svg}</span>\n<!-- /wp:generateblocks/shape -->'
def img(url,alt,wid,st=''):
    return f'<!-- wp:image {{"id":{wid},"sizeSlug":"full","linkDestination":"none"}} -->\n<figure class="wp-block-image size-full"><img src="{url}" alt="{alt}" class="wp-image-{wid}" style="{st}"/></figure>\n<!-- /wp:image -->'

WAVE='<svg viewBox="0 0 400 27" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><path d="M400 27H0v-.5h342.71c2.46 0 4.89-.57 7.1-1.66L400 0v27Z"></path></svg>'
BAR='<svg viewBox="0 0 36.7 3" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0h36.7v3H0z"></path></svg>'
def divider(color,p):
    return shape(WAVE,{"color":"#000000","left":"0","overflowX":"hidden","overflowY":"hidden","pointerEvents":"none","position":"absolute","right":"0","top":"0","transform":"scale(1,-1)","svg":{"color":color,"fill":"currentColor","height":"3rem","width":"100%"}},p=p)
def bar(p,center=True,mb="2.5rem"):
    st={"display":"flex","marginBottom":mb,"color":"var(--global-color-8)","svg":{"fill":"currentColor","height":"4px","width":"4.5rem"}}
    if center: st["justifyContent"]="center"
    return shape(BAR,st,p=p)
def section(p,inner,bg,extra=None,div=None,top_pad=None):
    st={"position":"relative","overflow":"hidden"}
    st.update(bg if isinstance(bg,dict) else {"backgroundColor":bg})
    if extra: st.update(extra)
    if div: st["paddingTop"]="calc(7rem + 2rem)"
    inn=el(inner,{"marginLeft":"auto","marginRight":"auto","maxWidth":"var(--gb-container-width)","position":"relative","zIndex":"1"},p=p,gc=["gbp-section__inner"])
    return el((divider(div,p)+'\n' if div else '')+inn,st,tag='section',p=p,gc=["gbp-section"],align=True)
RED="var(--global-color-8)"; NAVY="var(--contrast)"; TEAL="var(--accent)"; CREAM="var(--base)"; WHITE="var(--base-4)"; OFF="var(--base-3)"
M1024="@media (max-width:1024px)"; M767="@media (max-width:767px)"
LIFT={"transition":"transform 0.25s ease, box-shadow 0.25s ease","&:hover":{"transform":"translateY(-6px)","boxShadow":"0 16px 32px rgba(10,31,68,0.18)"}}
R12={f"border{c}Radius":"12px" for c in ("TopLeft","TopRight","BottomLeft","BottomRight")}
def pad(v): return {"paddingTop":v,"paddingRight":v,"paddingBottom":v,"paddingLeft":v}
def btn(label,href,p,bg=RED,color=WHITE,hover=NAVY):
    bd={f"border{s}{w}":v for s in ("Top","Right","Bottom","Left") for w,v in (("Width","3px"),("Style","solid"),("Color",bg))}
    return tx(label,'a',{"display":"inline-flex","alignItems":"center","backgroundColor":bg,"color":color,"fontWeight":"700","borderTopLeftRadius":"9999px","borderTopRightRadius":"9999px","borderBottomLeftRadius":"9999px","borderBottomRightRadius":"9999px","paddingTop":"0.875rem","paddingRight":"1.9rem","paddingBottom":"0.875rem","paddingLeft":"1.9rem","textDecoration":"none","transition":"transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease",**bd,"&:is(:hover, :focus)":{"backgroundColor":hover,"borderColor":hover,"color":WHITE,"transform":"translateY(-3px)","boxShadow":"0 10px 20px rgba(0,0,0,0.25)"}},p=p,ha={"href":href})
def link(label,href,p,color):
    return tx(label,'a',{"color":color,"fontWeight":"700","textDecoration":"underline","textUnderlineOffset":"4px","&:is(:hover, :focus)":{"color":RED}},p=p,ha={"href":href})
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
def icon(paths,p):
    svg=f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
    return el(shape(svg,{"color":WHITE,"display":"inline-flex","svg":{"fill":"none","height":"1.6rem","stroke":"currentColor","width":"1.6rem"}},p=p),{"backgroundColor":TEAL,"borderTopLeftRadius":"100%","borderTopRightRadius":"100%","borderBottomLeftRadius":"100%","borderBottomRightRadius":"100%","display":"inline-flex","alignItems":"center","justifyContent":"center","width":"3.25rem","height":"3.25rem","marginBottom":"1.25rem","flexShrink":"0"},p=p)
parts=[]
# 1 HERO — card over photo
IMG="https://3p-allies.com/wp-content/uploads/2025/04/SMall-Office.jpg"
hero_bg={"backgroundColor":CREAM,
 "backgroundImage":f"linear-gradient(90deg, rgba(255,255,255,0.1) 0%, rgba(0,0,0,0.3) 100%), url({IMG})",
 "backgroundPosition":"0 0, bottom right","backgroundRepeat":"no-repeat, no-repeat","backgroundSize":"100% 100%, min(1160px, 100%) auto","backgroundAttachment":"scroll, fixed",
 M1024:{"backgroundAttachment":"scroll, scroll"},M767:{"backgroundSize":"100% 100%, 170% auto"}}
eyebrow=tx('Purpose <span style="color:var(--global-color-8)">+</span> Process <span style="color:var(--global-color-8)">=</span> Progress','p',{"fontFamily":"Lora, serif","fontSize":"1.5rem","fontWeight":"700","color":TEAL,"marginBottom":"0.75rem",M767:{"fontSize":"1.125rem"}},p='hero')
h1=tx('Growth is the stress test. <span style="color:var(--global-color-8);display:block">We fix what cracks.</span>','h1',{"fontSize":"clamp(2.25rem, 4.4vw, 3.75rem)","lineHeight":"1.08","marginBottom":"1rem"},p='hero')
lead=tx('Hands-on process improvement for growing, mission-driven organizations — built with your team, and I stay until it sticks.','p',{"fontSize":"1.25rem","marginBottom":"1.75rem",M767:{"fontSize":"1.0625rem"}},p='hero')
ctas=el(btn('Take the 5-Minute Growing Pains Scorecard','/scorecard/','hero')+'\n'+link('See how the 3P Reset works →','/our-process/','hero',TEAL),{"display":"flex","flexWrap":"wrap","alignItems":"center","columnGap":"2rem","rowGap":"1.25rem"},p='hero')
card_st={"backgroundColor":OFF,"display":"inline-flex","flexDirection":"column","alignItems":"flex-start","position":"relative","width":"58%","marginLeft":"-20px",
 "paddingTop":"3.25rem","paddingRight":"3.25rem","paddingBottom":"3rem","paddingLeft":"2.25rem","borderRightWidth":"4px","borderRightStyle":"solid","borderRightColor":RED,"borderTopRightRadius":"10px","borderBottomRightRadius":"10px","boxShadow":"0 20px 40px rgba(10,31,68,0.25)",
 M1024:{"width":"78%","paddingRight":"2.5rem"},M767:{"width":"100%","marginLeft":"0","paddingTop":"2rem","paddingRight":"1.5rem","paddingBottom":"2rem","paddingLeft":"1.5rem"}}
parts.append(section('hero',el(eyebrow+'\n'+h1+'\n'+bar('hero',False,"1.25rem")+'\n'+lead+'\n'+ctas,card_st,p='hero'),hero_bg))
# 2 SOUND FAMILIAR
quotes=[("We're growing, and it's breaking our current processes.",'<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'),
("I can't see what's overdue until it's late.",'<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>'),
("We keep asking each other, 'Are you doing it or am I?'",'<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'),
("We bought the software. Nobody uses it.",'<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>'),
("Every new hire learns by osmosis.",'<path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/>')]
def card(q,ic,i):
    st={"backgroundColor":WHITE,"borderTopWidth":"5px","borderTopStyle":"solid","borderTopColor":TEAL,**R12,"boxShadow":"0 4px 12px rgba(0,0,0,0.08)",**pad("1.75rem"),"display":"flex","flexDirection":"column","alignItems":"flex-start",
        "gridColumn":("2 / span 2" if i==3 else "4 / span 2" if i==4 else "span 2"),M1024:{"gridColumn":"span 1"},**LIFT}
    return el(icon(ic,'fam')+'\n'+tx('“'+q+'”','p',{"fontFamily":"Lora, serif","fontSize":"1.25rem","fontWeight":"600","lineHeight":"1.4","margin":"0"},p='fam'),st,p='fam')
cardsEl=el('\n'.join(card(q,ic,i) for i,(q,ic) in enumerate(quotes)),{"display":"grid","gridTemplateColumns":"repeat(6, minmax(0, 1fr))","columnGap":"1.5rem","rowGap":"1.5rem","marginBottom":"3.5rem",M1024:{"gridTemplateColumns":"repeat(2, minmax(0, 1fr))"},M767:{"gridTemplateColumns":"1fr"}},p='fam')
closing=el(tx('Those aren’t people problems. <span style="color:var(--global-color-8)">They’re process problems</span> — and they’re fixable.','p',{"textAlign":"center","fontFamily":"Lora, serif","fontSize":"2rem","fontWeight":"700","lineHeight":"1.3","margin":"0",M767:{"fontSize":"1.5rem"}},p='fam'),{"maxWidth":"820px","marginLeft":"auto","marginRight":"auto"},p='fam')
inner=tx('Sound familiar?','h2',{"textAlign":"center","marginBottom":"0.75rem"},p='fam',gc=["gbp-section__headline"])+'\n'+bar('fam')+'\n'+cardsEl+'\n'+closing
parts.append(section('fam',inner,CREAM,div=OFF))
# 3 METHOD
steps=[("01","Purpose","We name the pain and what it’s costing you, then I interview the people doing the work.",TEAL),("02","Process","We co-design the new way of working with your team. I document it, set up the tools and build the triggers so nobody has to remember.",RED),("03","Progress","I train the team, we go live, and I check back 30 days later to make sure it held.",NAVY)]
def mcard(num,t,b,col):
    st={"backgroundColor":OFF,"position":"relative","overflow":"hidden","height":"100%",**R12,"borderTopWidth":"6px","borderTopStyle":"solid","borderTopColor":col,"boxShadow":"0 4px 12px rgba(0,0,0,0.06)","paddingTop":"3rem","paddingRight":"2rem","paddingBottom":"2.25rem","paddingLeft":"2rem",**LIFT}
    n=tx(num,'span',{"position":"absolute","top":"0.5rem","right":"1.25rem","fontFamily":"Lora, serif","fontSize":"6.5rem","fontWeight":"700","lineHeight":"1","color":col,"opacity":"0.12","pointerEvents":"none"},p='meth')
    return el(n+'\n'+tx(t,'h3',{"color":col,"marginBottom":"0.75rem","position":"relative"},p='meth')+'\n'+tx(b,'p',{"margin":"0","position":"relative"},p='meth'),st,p='meth')
def arrow(): return el(shape(ARROW,{"color":RED,"display":"inline-flex","svg":{"fill":"none","height":"2.5rem","width":"2.5rem"}},p='meth'),{"display":"flex","alignItems":"center","justifyContent":"center",M1024:{"display":"none"}},p='meth')
row=[]
for i,(nm,t,b,c) in enumerate(steps):
    row.append(mcard(nm,t,b,c))
    if i<2: row.append(arrow())
rowEl=el('\n'.join(row),{"display":"grid","gridTemplateColumns":"1fr auto 1fr auto 1fr","columnGap":"1.25rem","alignItems":"stretch",M1024:{"gridTemplateColumns":"1fr","rowGap":"1.5rem"}},p='meth')
inner=tx('Purpose <span style="color:var(--global-color-8)">+</span> Process <span style="color:var(--global-color-8)">=</span> Progress','h2',{"textAlign":"center","marginBottom":"0.75rem"},p='meth',gc=["gbp-section__headline"])+'\n'+bar('meth',True,"1.5rem")+'\n'+tx('Every engagement follows the same three steps. Your team helps design the fix, which is why it gets used.','p',{"textAlign":"center","maxWidth":"680px","marginLeft":"auto","marginRight":"auto","marginBottom":"3rem"},p='meth',gc=["gbp-section__text"])+'\n'+rowEl
parts.append(section('meth',inner,WHITE,div=CREAM))
# 4 RESET
badge=el(tx('Founding rate','p',{"textTransform":"uppercase","letterSpacing":"0.15em","fontSize":"0.8125rem","fontWeight":"700","color":RED,"margin":"0"},p='rst')+'\n'+tx('$2,500','p',{"fontFamily":"Lora, serif","fontSize":"3.5rem","fontWeight":"700","lineHeight":"1.05","color":NAVY,"margin":"0"},p='rst')+'\n'+tx('for my first three clients <span style="opacity:0.75">(standard $3,500)</span>','p',{"fontSize":"1rem","color":NAVY,"margin":"0"},p='rst'),
 {"backgroundColor":CREAM,"display":"inline-flex","flexDirection":"column","alignItems":"center","rowGap":"0.25rem",**R12,"borderTopWidth":"3px","borderRightWidth":"3px","borderBottomWidth":"3px","borderLeftWidth":"3px","borderTopStyle":"dashed","borderRightStyle":"dashed","borderBottomStyle":"dashed","borderLeftStyle":"dashed","borderTopColor":RED,"borderRightColor":RED,"borderBottomColor":RED,"borderLeftColor":RED,"paddingTop":"1.5rem","paddingRight":"2.5rem","paddingBottom":"1.5rem","paddingLeft":"2.5rem","marginBottom":"2.25rem","boxShadow":"0 14px 30px rgba(0,0,0,0.3)"},p='rst')
inner=el(tx('One broken process, fixed and adopted in six Friday sessions.','h2',{"color":WHITE,"marginBottom":"0.75rem"},p='rst')+'\n'+bar('rst',True,"1.5rem")+'\n'+tx('The 3P Reset takes the one process causing the most pain and rebuilds it with your team: clear owners, clear handoffs, a task board everyone can see, and training so it sticks.','p',{"color":WHITE,"fontSize":"1.1875rem","marginBottom":"2.25rem"},p='rst')+'\n'+badge+'\n'+el(btn('See how the 3P Reset works','/our-process/','rst'),{"display":"flex","justifyContent":"center"},p='rst'),{"textAlign":"center","maxWidth":"780px","marginLeft":"auto","marginRight":"auto"},p='rst')
rst_bg={"backgroundImage":"linear-gradient(180deg, var(--contrast) 0%, var(--accent) 100%)","backgroundColor":NAVY}
parts.append(section('rst',inner,rst_bg,div=WHITE))
# 5 TESTIMONIALS
def tcard(q):
    qm=tx('“','span',{"position":"absolute","top":"-0.5rem","left":"1.25rem","fontFamily":"Lora, serif","fontSize":"7rem","fontWeight":"700","lineHeight":"1","color":RED,"opacity":"0.9","pointerEvents":"none"},p='tst')
    return el(qm+'\n'+tx(q,'p',{"fontFamily":"Lora, serif","fontSize":"1.25rem","lineHeight":"1.55","margin":"0","position":"relative"},p='tst'),{"backgroundColor":WHITE,"position":"relative",**R12,"boxShadow":"0 4px 12px rgba(0,0,0,0.08)","paddingTop":"4.5rem","paddingRight":"2rem","paddingBottom":"2rem","paddingLeft":"2rem","borderLeftWidth":"5px","borderLeftStyle":"solid","borderLeftColor":TEAL,**LIFT},p='tst')
tg=el(tcard("Heather is such an amazing person to work with, so efficient, effective, and intelligent.")+'\n'+tcard("The vastness and depth of Heather’s knowledge and the clarity of her thoughts become so evident…"),{"display":"grid","gridTemplateColumns":"repeat(2, minmax(0, 1fr))","columnGap":"2rem","rowGap":"2rem",M767:{"gridTemplateColumns":"1fr"}},p='tst')
inner=tx('What it’s like to work with Heather','h2',{"textAlign":"center","marginBottom":"0.75rem"},p='tst',gc=["gbp-section__headline"])+'\n'+bar('tst')+'\n<!-- TESTIMONIALS: publish only quotes Heather has approved. Duplicate a card Element to add more. -->\n'+tg
parts.append(section('tst',inner,CREAM,div=TEAL))
# 6 MEET HEATHER
pic=el(img('https://3p-allies.com/wp-content/uploads/2025/11/About-me.webp','Heather Shafter at work',44229,'width:100%;height:auto;border-radius:12px;display:block;box-shadow:16px 16px 0 var(--accent)'),{"paddingRight":"16px","paddingBottom":"16px"},p='mt')
txt=el(tx('I’ve built these systems <span style="color:var(--global-color-8)">from the inside.</span>','h2',{"marginBottom":"0.75rem"},p='mt',gc=["gbp-section__headline"])+'\n'+bar('mt',False,"1.5rem")+'\n'+tx('I’ve spent more than two decades in nonprofit, government, social services and advocacy work, and I still run operations day to day. I hold a master’s in Adult and Organizational Development, and I’ve sat on the other side of the table: the new hire who doesn’t know what to do, the manager who can’t see what’s overdue, the leader who becomes the bottleneck.','p',{"marginBottom":"1.25rem"},p='mt',gc=["gbp-section__text"])+'\n'+tx('I take one client at a time, and I stay until the new way of working sticks.','p',{"marginBottom":"1.5rem","fontWeight":"700","fontFamily":"Lora, serif","fontSize":"1.375rem"},p='mt')+'\n'+link('More about Heather →','/about/','mt',TEAL),p='mt')
parts.append(section('mt',el(pic+'\n'+txt,{"display":"grid","gridTemplateColumns":"repeat(2, minmax(0, 1fr))","columnGap":"4rem","rowGap":"2.5rem","alignItems":"center",M1024:{"gridTemplateColumns":"1fr"}},p='mt'),WHITE,div=CREAM))
# 7 FINAL CTA
cta_bg={"backgroundColor":NAVY,"backgroundImage":"radial-gradient(circle at 12% 20%, rgba(12,105,128,0.65) 0, transparent 45%), radial-gradient(circle at 88% 85%, rgba(196,57,29,0.4) 0, transparent 40%)"}
inner=el(tx('Where is growth straining your operations?','h2',{"color":WHITE,"marginBottom":"0.75rem"},p='cta')+'\n'+bar('cta',True,"1.5rem")+'\n'+tx('Find out in five minutes. Ten quick statements, an instant score and your biggest crack.','p',{"color":WHITE,"fontSize":"1.1875rem","marginBottom":"2rem"},p='cta')+'\n'+el(btn('Take the Growing Pains Scorecard','/scorecard/','cta',hover=TEAL)+'\n'+link('Already know what’s breaking? Book a Focus Session →','/welcome/','cta',WHITE),{"display":"flex","flexDirection":"column","alignItems":"center","rowGap":"1.5rem"},p='cta'),{"textAlign":"center","maxWidth":"720px","marginLeft":"auto","marginRight":"auto"},p='cta')
parts.append(section('cta',inner,cta_bg,div=WHITE))
open('/tmp/claude-0/-home-user/943bec44-4e22-5eb2-aaee-39ec5ceb70e3/scratchpad/gen/01-home.html','w').write('\n\n'.join(parts)+'\n')
