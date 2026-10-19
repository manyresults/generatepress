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
    return shape(WAVE,{"color":"#000000","left":"0","overflowX":"hidden","overflowY":"hidden","pointerEvents":"none","position":"absolute","right":"0","top":"0","display":"block","lineHeight":"0","transform":"scale(1,-1)","svg":{"color":color,"display":"block","fill":"currentColor","height":"3rem","width":"100%"}},p=p)
def bar(p,center=True,mb="2.5rem"):
    st={"display":"flex","marginBottom":mb,"color":"var(--global-color-8)","svg":{"fill":"currentColor","height":"4px","width":"4.5rem"}}
    if center: st["justifyContent"]="center"
    return shape(BAR,st,p=p)
def section(p,inner,bg,extra=None,div=None,top_pad=None,anchor=None):
    st={"position":"relative","overflow":"hidden"}
    st.update(bg if isinstance(bg,dict) else {"backgroundColor":bg})
    if div: st["paddingTop"]="calc(7rem + 2rem)"
    if extra: st.update(extra)
    inn=el(inner,{"marginLeft":"auto","marginRight":"auto","maxWidth":"var(--gb-container-width)","position":"relative","zIndex":"1"},p=p,gc=["gbp-section__inner"])
    return el((divider(div,p)+'\n' if div else '')+inn,st,tag='section',p=p,gc=["gbp-section"],align=True,ha=({"id":anchor} if anchor else None))
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
