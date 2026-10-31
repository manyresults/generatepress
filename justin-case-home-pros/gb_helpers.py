import base64, json, re
def svguri(s): return 'data:image/svg+xml;base64,'+base64.b64encode(s.encode()).decode()
n=[0]
def uid():
    n[0]+=1; return f"jc{n[0]:03d}"
def kebab(k): return re.sub(r'([A-Z])',lambda m:'-'+m.group(1).lower(),k)
def css_for(cls,styles):
    base=[];extra=[];media=[]
    for k,v in styles.items():
        if k.startswith('@media'): media.append((k,v))
        elif k.startswith('&'): extra.append((k[1:],v))
        elif k.startswith('.'): extra.append((' '+k,v))
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

