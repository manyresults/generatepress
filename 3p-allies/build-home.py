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
def section(p,inner,bg,extra=None,padding=None):
    st={"backgroundColor":bg,"position":"relative"}
    if extra: st.update(extra)
    return el(el(inner,{"marginLeft":"auto","marginRight":"auto","maxWidth":"var(--gb-container-width)","position":"relative","zIndex":"1"},p=p,gc=["gbp-section__inner"]),st,tag='section',p=p,gc=["gbp-section"],align=True,ha=None)
RED="var(--global-color-8)"; NAVY="var(--contrast)"; TEAL="var(--accent)"; CREAM="var(--base)"; WHITE="var(--base-4)"
def btn(label,href,p,bg=RED,color=WHITE):
    return tx(label,'a',{"display":"inline-flex","backgroundColor":bg,"color":color,"borderTopWidth":"1px","borderRightWidth":"1px","borderBottomWidth":"1px","borderLeftWidth":"1px","borderTopStyle":"solid","borderRightStyle":"solid","borderBottomStyle":"solid","borderLeftStyle":"solid","borderTopColor":bg,"borderRightColor":bg,"borderBottomColor":bg,"borderLeftColor":bg,"fontWeight":"700","paddingTop":"0.875rem","paddingRight":"1.75rem","paddingBottom":"0.875rem","paddingLeft":"1.75rem","textDecoration":"none","&:is(:hover, :focus)":{"backgroundColor":TEAL,"borderColor":TEAL,"color":WHITE}},p=p,ha={"href":href})
def link(label,href,p,color):
    return tx(label,'a',{"color":color,"fontWeight":"700","textDecoration":"underline","textUnderlineOffset":"4px","&:is(:hover, :focus)":{"color":RED}},p=p,ha={"href":href})
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
M1024="@media (max-width:1024px)"; M767="@media (max-width:767px)"
parts=[]
# 1 HERO
eyebrow=tx('Purpose <span style="color:var(--global-color-8)">+</span> Process <span style="color:var(--global-color-8)">=</span> Progress','p',{"fontFamily":"Lora, serif","fontSize":"1.25rem","fontWeight":"600","color":CREAM,"marginBottom":"1rem"},p='hero')
h1=tx('Growth is the stress test. We fix what cracks.','h1',{"color":WHITE,"marginBottom":"1.5rem"},p='hero')
lead=tx('Hands-on process improvement for growing, mission-driven organizations — built with your team, and I stay until it sticks.','p',{"color":WHITE,"fontSize":"1.25rem","marginBottom":"2rem"},p='hero')
ctas=el(btn('Take the 5-Minute Growing Pains Scorecard','/scorecard/','hero')+'\n'+link('See how the 3P Reset works →','/our-process/','hero',WHITE),{"display":"flex","flexWrap":"wrap","alignItems":"center","columnGap":"2rem","rowGap":"1.25rem"},p='hero')
photo=el(img('https://3p-allies.com/wp-content/uploads/2025/11/Home-page-edited.webp','Heather working beside a team',44247,'width:100%;height:auto;border-radius:12px;display:block'),{"display":"flex","justifyContent":"center"},p='hero')
grid=el(el(eyebrow+'\n'+h1+'\n'+lead+'\n'+ctas,p='hero')+'\n'+photo,{"display":"grid","gridTemplateColumns":"repeat(2, minmax(0, 1fr))","columnGap":"4rem","rowGap":"3rem","alignItems":"center",M1024:{"gridTemplateColumns":"1fr"}},p='hero')
parts.append(section('hero',grid,NAVY))
# 2 SOUND FAMILIAR
quotes=["We're growing, and it's breaking our current processes.","I can't see what's overdue until it's late.","We keep asking each other, 'Are you doing it or am I?'","We bought the software. Nobody uses it.","Every new hire learns by osmosis."]
card=lambda q,i=0: el(tx('“'+q+'”','p',{"fontFamily":"Lora, serif","fontSize":"1.25rem","fontWeight":"600","lineHeight":"1.4","margin":"0"},p='fam'),{"backgroundColor":WHITE,"borderTopWidth":"4px","borderTopStyle":"solid","borderTopColor":TEAL,"borderTopLeftRadius":"12px","borderTopRightRadius":"12px","borderBottomLeftRadius":"12px","borderBottomRightRadius":"12px","boxShadow":"0 4px 12px rgba(0,0,0,0.08)","paddingTop":"1.75rem","paddingRight":"1.75rem","paddingBottom":"1.75rem","paddingLeft":"1.75rem","gridColumn":("2 / span 2" if i==3 else "4 / span 2" if i==4 else "span 2"),M1024:{"gridColumn":"span 1"}},p='fam')
cards=[card(q,i) for i,q in enumerate(quotes)]
# 3+2 layout: 6-col grid, each card spans 2; last two offset
cardsEl=el('\n'.join(cards),{"display":"grid","gridTemplateColumns":"repeat(6, minmax(0, 1fr))","columnGap":"1.5rem","rowGap":"1.5rem","marginBottom":"3rem",M1024:{"gridTemplateColumns":"repeat(2, minmax(0, 1fr))"},M767:{"gridTemplateColumns":"1fr"}},p='fam')
inner=tx('Sound familiar?','h2',{"textAlign":"center","marginBottom":"2.5rem"},p='fam',gc=["gbp-section__headline"])+'\n'+cardsEl+'\n'+tx('Those aren’t people problems. They’re process problems — and they’re fixable.','p',{"textAlign":"center","fontFamily":"Lora, serif","fontSize":"1.75rem","fontWeight":"700","lineHeight":"1.3","maxWidth":"780px","marginLeft":"auto","marginRight":"auto",M767:{"fontSize":"1.375rem"}},p='fam')
parts.append(section('fam',inner,CREAM))
# 4 METHOD
steps=[("Purpose","We name the pain and what it’s costing you, then I interview the people doing the work."),("Process","We co-design the new way of working with your team. I document it, set up the tools and build the triggers so nobody has to remember."),("Progress","I train the team, we go live, and I check back 30 days later to make sure it held.")]
def mcard(t,b): return el(tx(t,'h3',{"color":TEAL,"marginBottom":"0.75rem"},p='meth')+'\n'+tx(b,'p',{"margin":"0"},p='meth'),{"backgroundColor":"var(--base-3)","borderTopLeftRadius":"12px","borderTopRightRadius":"12px","borderBottomLeftRadius":"12px","borderBottomRightRadius":"12px","paddingTop":"2rem","paddingRight":"2rem","paddingBottom":"2rem","paddingLeft":"2rem","height":"100%"},p='meth')
def arrow(): return el(shape(ARROW,{"color":RED,"display":"inline-flex","svg":{"fill":"none","height":"2.5rem","width":"2.5rem"}},p='meth'),{"display":"flex","alignItems":"center","justifyContent":"center",M1024:{"display":"none"}},p='meth')
row=[]
for i,(t,b) in enumerate(steps):
    row.append(mcard(t,b))
    if i<2: row.append(arrow())
rowEl=el('\n'.join(row),{"display":"grid","gridTemplateColumns":"1fr auto 1fr auto 1fr","columnGap":"1.25rem","alignItems":"stretch",M1024:{"gridTemplateColumns":"1fr","rowGap":"1.5rem"}},p='meth')
inner=tx('Purpose + Process = Progress','h2',{"textAlign":"center","marginBottom":"1rem"},p='meth',gc=["gbp-section__headline"])+'\n'+tx('Every engagement follows the same three steps. Your team helps design the fix, which is why it gets used.','p',{"textAlign":"center","maxWidth":"680px","marginLeft":"auto","marginRight":"auto","marginBottom":"3rem"},p='meth',gc=["gbp-section__text"])+'\n'+rowEl
parts.append(section('meth',inner,WHITE))
# 5 RESET
inner=el(tx('One broken process, fixed and adopted in six Friday sessions.','h2',{"color":WHITE,"marginBottom":"1.5rem"},p='rst')+'\n'+tx('The 3P Reset takes the one process causing the most pain and rebuilds it with your team: clear owners, clear handoffs, a task board everyone can see, and training so it sticks.','p',{"color":WHITE,"fontSize":"1.125rem","marginBottom":"2rem"},p='rst')+'\n'+el(tx('<strong>Founding rate: $2,500</strong> for my first three clients (standard $3,500).','p',{"color":NAVY,"fontSize":"1.125rem","margin":"0"},p='rst'),{"backgroundColor":CREAM,"borderTopLeftRadius":"12px","borderTopRightRadius":"12px","borderBottomLeftRadius":"12px","borderBottomRightRadius":"12px","paddingTop":"1.25rem","paddingRight":"1.75rem","paddingBottom":"1.25rem","paddingLeft":"1.75rem","display":"inline-block","marginBottom":"2rem"},p='rst')+'\n'+btn('See how the 3P Reset works','/our-process/','rst'),{"textAlign":"center","maxWidth":"780px","marginLeft":"auto","marginRight":"auto"},p='rst')
parts.append(section('rst',inner,NAVY))
# 6 TESTIMONIALS
def tcard(q,w): return el(tx('“'+q+'”','p',{"fontFamily":"Lora, serif","fontSize":"1.25rem","lineHeight":"1.5","margin":"0"},p='tst'),{"backgroundColor":WHITE,"borderTopLeftRadius":"12px","borderTopRightRadius":"12px","borderBottomLeftRadius":"12px","borderBottomRightRadius":"12px","boxShadow":"0 4px 12px rgba(0,0,0,0.08)","paddingTop":"2rem","paddingRight":"2rem","paddingBottom":"2rem","paddingLeft":"2rem"},p='tst')
tg=el(tcard("Heather is such an amazing person to work with, so efficient, effective, and intelligent.",0)+'\n'+tcard("The vastness and depth of Heather’s knowledge and the clarity of her thoughts become so evident…",0),{"display":"grid","gridTemplateColumns":"repeat(2, minmax(0, 1fr))","columnGap":"2rem","rowGap":"2rem",M767:{"gridTemplateColumns":"1fr"}},p='tst')
inner=tx('What it’s like to work with Heather','h2',{"textAlign":"center","marginBottom":"2.5rem"},p='tst',gc=["gbp-section__headline"])+'\n<!-- TESTIMONIALS: publish only quotes Heather has approved. Replace/add cards by duplicating a card Element. -->\n'+tg
parts.append(section('tst',inner,CREAM))
# 7 MEET HEATHER
pic=el(img('https://3p-allies.com/wp-content/uploads/2025/11/About-me.webp','Heather Shafter at work',44229,'width:100%;height:auto;border-radius:12px;display:block'),p='mt')
txt=el(tx('I’ve built these systems from the inside.','h2',{"marginBottom":"1.5rem"},p='mt',gc=["gbp-section__headline"])+'\n'+tx('I’ve spent more than two decades in nonprofit, government, social services and advocacy work, and I still run operations day to day. I hold a master’s in Adult and Organizational Development, and I’ve sat on the other side of the table: the new hire who doesn’t know what to do, the manager who can’t see what’s overdue, the leader who becomes the bottleneck.','p',{"marginBottom":"1.25rem"},p='mt',gc=["gbp-section__text"])+'\n'+tx('I take one client at a time, and I stay until the new way of working sticks.','p',{"marginBottom":"1.5rem","fontWeight":"700"},p='mt',gc=["gbp-section__text"])+'\n'+link('More about Heather →','/about/','mt',TEAL),p='mt')
parts.append(section('mt',el(pic+'\n'+txt,{"display":"grid","gridTemplateColumns":"repeat(2, minmax(0, 1fr))","columnGap":"4rem","rowGap":"2.5rem","alignItems":"center",M1024:{"gridTemplateColumns":"1fr"}},p='mt'),WHITE))
# 8 FINAL CTA
inner=el(tx('Where is growth straining your operations?','h2',{"color":WHITE,"marginBottom":"1.25rem"},p='cta')+'\n'+tx('Find out in five minutes. Ten quick statements, an instant score and your biggest crack.','p',{"color":WHITE,"fontSize":"1.125rem","marginBottom":"2rem"},p='cta')+'\n'+el(btn('Take the Growing Pains Scorecard','/scorecard/','cta')+'\n'+link('Already know what’s breaking? Book a Focus Session →','/welcome/','cta',WHITE),{"display":"flex","flexDirection":"column","alignItems":"center","rowGap":"1.5rem"},p='cta'),{"textAlign":"center","maxWidth":"720px","marginLeft":"auto","marginRight":"auto"},p='cta')
parts.append(section('cta',inner,NAVY))
open('/tmp/claude-0/-home-user/943bec44-4e22-5eb2-aaee-39ec5ceb70e3/scratchpad/gen/01-home.html','w').write('\n\n'.join(parts)+'\n')
