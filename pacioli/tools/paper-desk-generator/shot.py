import re,json,sys
from playwright.sync_api import sync_playwright
t=open('cleanup.html').read()
css=[]
for m in re.finditer(r'<!-- wp:[a-z0-9\-/]+ (\{.*?\}) -->',t,re.S):
    try: a=json.loads(m.group(1))
    except: continue
    if 'css' in a: css.append(a['css'])
body=re.sub(r'<!--.*?-->','',t,flags=re.S)
tok=re.sub(r'@import url\([^)]*\);','',open('tok.css').read())
html='<!doctype html><meta charset=utf-8><style>*{box-sizing:border-box}body{margin:0;background:#fff}.gbp-section__inner{}%s%s</style>%s'%(tok,'\n'.join(css),body)
open('render.html','w').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    for w,n in ((1280,'desk'),(390,'mob')):
        pg=b.new_page(viewport={'width':w,'height':900}); pg.set_content(html); pg.wait_for_timeout(300)
        pg.screenshot(path='shot_%s.png'%n,full_page=True)
        print(n,pg.evaluate('document.documentElement.scrollWidth'),pg.evaluate('document.documentElement.scrollHeight'))
    b.close()
