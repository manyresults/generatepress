import re,json,sys,collections
from html.parser import HTMLParser
t=open(sys.argv[1]).read()
pat=re.compile(r'<!-- (/?)wp:([a-z0-9\-/]+)\s*(\{.*?\})?\s*(/?)-->',re.S)
errs=[];stack=[]
for m in pat.finditer(t):
    line=t.count('\n',0,m.start())+1
    if m.group(3):
        try: json.loads(m.group(3))
        except Exception as e: errs.append((line,'json',str(e)))
    if m.group(1):
        if not stack or stack[-1][0]!=m.group(2): errs.append((line,'mismatch',m.group(2),stack[-1:]))
        else: stack.pop()
    elif not m.group(4): stack.append((m.group(2),line))
if stack: errs.append(('unclosed',stack[:3]))
VOID={'br','img','hr','input','path','circle','rect','line','polyline','ellipse','use'}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.e=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        else: s.e.append((t,s.st[-2:]))
p=P();p.feed(pat.sub('',t))
if p.st or p.e: errs.append(('html',p.st[:3],p.e[:3]))
ids=re.findall(r'"uniqueId": ?"([^"]+)"',t)
d=[k for k,v in collections.Counter(ids).items() if v>1]
if d: errs.append(('dup ids',d))
if re.search(r'[^;&]&(?!amp;|#)',re.sub(pat,'',t)): errs.append(('raw &',))
for m in pat.finditer(t):
    if m.group(3) and '&' in m.group(3): errs.append(('raw & in json',t.count('\n',0,m.start())+1)); break
bad=set(re.findall(r'var\((--paper-[a-z0-9-]+)',t))-set(re.findall(r'(--paper-[a-z0-9-]+)\s*:',open('tok.css').read()))
if bad: errs.append(('undefined tokens',bad))
print('blocks',len(ids),'errors',len(errs)); [print(e) for e in errs]
