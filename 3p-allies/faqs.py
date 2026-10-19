import sys,re,json; sys.path.insert(0,'.')
from lib import *
OUT='./'
def red(t): return f'<span style="color:var(--global-color-8)">{t}</span>'
def icon_circ(paths,p):
    svg=f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
    return el(shape(svg,{"color":WHITE,"display":"inline-flex","svg":{"fill":"none","height":"1.6rem","stroke":"currentColor","width":"1.6rem"}},p=p),{"backgroundColor":TEAL,"borderTopLeftRadius":"100%","borderTopRightRadius":"100%","borderBottomLeftRadius":"100%","borderBottomRightRadius":"100%","display":"inline-flex","alignItems":"center","justifyContent":"center","width":"3.5rem","height":"3.5rem","marginBottom":"1.25rem"},p=p)
def L(href,t): return f'<a href="{href}">{t}</a>'
groups=[
 ("who","Who I work with",'<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',WHITE,CREAM,[
  ("What kinds of organizations do you work with?","Growing, values-driven organizations: nonprofits, social enterprises and mission-driven businesses, usually with 10–75 staff. I don’t work with manufacturing. The common thread is that the work has outgrown the way it gets done."),
  ("Do you only work with nonprofits?","No. Values-aligned for-profit businesses are a great fit too. What matters is that you take care of your people and your community, and that growth is straining your processes."),
  ("How do I know if we’re ready?",f"Usually something just changed: new funding or a new contract, fast hiring, a key person leaving, a handoff that went badly, or software nobody is using. If any of those sound familiar, take the {L('/scorecard/','Growing Pains Scorecard')} — it takes five minutes."),
  ("Who on our team should reach out?","The executive director, founder, COO or operations lead — whoever feels responsible for how the work gets done.")]),
 ("how","How it works",'<polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/>',CREAM,WHITE,[
  ("What is the 3P Reset?",f"A fixed-scope engagement to fix one broken process. Over six 2-hour Friday sessions, I interview your team, co-design the new process with them, set up the tools, write the SOPs, train everyone, and go live. Then I check back 30 days later. {L('/our-process/','See the full process →')}"),
  ("Why one process at a time?","Because it gets done. Fixing one process well builds the habits — clear owners, visible work, written steps — that make the next fix easier."),
  ("How much of my team’s time does it take?","About 45 minutes per person for interviews, plus 2–4 people in a few working sessions. I do the documentation and setup between sessions."),
  ("Will you tell us what software to buy?","Only if you need it. Most organizations already own tools that would work if they were set up and adopted. If you need something new, I’ll recommend it and help configure it."),
  ("What if we need automation?","I work with a trusted automation partner for deeper builds. I coordinate the work; the build is quoted separately."),
  ("Why only Fridays?","Fridays are my dedicated 3P Allies day. You get my full attention, not a junior team, and I take one client at a time."),
  ("Do you work remotely?","Yes. I’m based in Philadelphia and work in person locally and remotely anywhere.")]),
 ("pricing","Pricing",'<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',WHITE,CREAM,[
  ("How much does it cost?","LIST"),
  ("What’s the difference between the Reset and the Partnership?","The Reset fixes the process and checks it at 30 days. The Partnership adds 90 days of support after launch: monthly check-ins, SOP updates as things change, and training for 1–2 people on your team to keep owning and improving the process."),
  ("What if the new process doesn’t stick?","If your team isn’t running it at the 30-day check, I add up to two more sessions at no charge until it is."),
  ("What’s Map It for?","It’s for leaders who feel the strain but aren’t sure which process to fix first. One working session gives you a map of how work happens today and the fixes ranked by impact.")]),
 ("start","Getting started",'<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',CREAM,WHITE,[
  ("What happens when I take the Scorecard?","You’ll see your score right away, and I’ll email you a breakdown by section that names your biggest crack. You’ll also get an invitation to a free Focus Session."),
  ("What happens in a Focus Session?","In 30 minutes, we find the one process worth fixing first. If I can help, I’ll tell you how. If I can’t, I’ll tell you that too — and you’ll leave with at least one idea you can use on Monday."),
  ("How soon can we start?","I take one engagement at a time, so start dates depend on my calendar. Book a Focus Session and I’ll tell you the next available Friday.")])]
PRICES=[("Growing Pains Scorecard:","free"),("Focus Session:","free, 30 minutes"),("Map It:","$750, credited toward the 3P Reset if you start within 30 days"),("The 3P Reset:","$2,500 founding rate for my first three clients, then $3,500"),("3P Partnership:","$4,500 — the Reset plus 90 days of support")]
def answer(a):
    if a=="LIST":
        items=''.join(f'<!-- wp:list-item -->\n<li><strong>{b}</strong> {t}</li>\n<!-- /wp:list-item -->\n' for b,t in PRICES)
        return f'<!-- wp:list -->\n<ul class="wp-block-list">\n{items}</ul>\n<!-- /wp:list -->'
    return f'<!-- wp:paragraph -->\n<p>{a}</p>\n<!-- /wp:paragraph -->'
def faq(q,a,p):
    d=f'<!-- wp:details -->\n<details class="wp-block-details"><summary>{q}</summary>\n{answer(a)}</details>\n<!-- /wp:details -->'
    return el(d,{"backgroundColor":WHITE if False else OFF,**R12,"borderLeftWidth":"5px","borderLeftStyle":"solid","borderLeftColor":TEAL,"boxShadow":"0 4px 12px rgba(0,0,0,0.07)","paddingTop":"1.25rem","paddingRight":"1.75rem","paddingBottom":"1.25rem","paddingLeft":"1.75rem","transition":"box-shadow 0.25s ease, transform 0.25s ease",
     "& summary":{"cursor":"pointer","fontFamily":"Lora, serif","fontSize":"1.25rem","fontWeight":"700","lineHeight":"1.35"},"& summary:hover":{"color":TEAL},"& details[open] summary":{"color":TEAL,"marginBottom":"0.75rem"},"& summary::marker":{"color":RED},
     "& p":{"margin":"0"},"& ul":{"margin":"0","paddingLeft":"1.25rem"},"& li":{"marginBottom":"0.5rem"},"& a":{"color":TEAL,"fontWeight":"700"},"& a:hover":{"color":RED},"&:hover":{"boxShadow":"0 10px 24px rgba(10,31,68,0.15)","transform":"translateY(-3px)"}},p=p)
parts=[]
# HERO
chips=el('\n'.join(tx(name,'a',{"display":"inline-flex","backgroundColor":WHITE,"color":NAVY,"fontWeight":"700","fontSize":"0.9375rem","borderTopWidth":"2px","borderRightWidth":"2px","borderBottomWidth":"2px","borderLeftWidth":"2px","borderTopStyle":"solid","borderRightStyle":"solid","borderBottomStyle":"solid","borderLeftStyle":"solid","borderTopColor":TEAL,"borderRightColor":TEAL,"borderBottomColor":TEAL,"borderLeftColor":TEAL,"borderTopLeftRadius":"9999px","borderTopRightRadius":"9999px","borderBottomLeftRadius":"9999px","borderBottomRightRadius":"9999px","paddingTop":"0.55rem","paddingRight":"1.15rem","paddingBottom":"0.55rem","paddingLeft":"1.15rem","textDecoration":"none","transition":"transform 0.2s ease, background-color 0.2s ease, color 0.2s ease","&:is(:hover, :focus)":{"backgroundColor":TEAL,"color":WHITE,"transform":"translateY(-3px)"}},p='hero',ha={"href":"#"+gid}) for gid,name,*_ in groups),{"display":"flex","flexWrap":"wrap","justifyContent":"center","columnGap":"0.75rem","rowGap":"0.75rem","marginTop":"2rem"},p='hero')
hero=el(tx('Questions, answered','h1',{"fontSize":"clamp(2.5rem, 5.5vw, 4.25rem)","lineHeight":"1.08","marginBottom":"0.75rem"},p='hero')+'\n'+bar('hero',True,"1.5rem")+'\n'+tx(f'Short answers to what people ask before we start. Don’t see yours? <a href="/contact/" style="color:var(--accent);font-weight:700">Ask me directly →</a>','p',{"fontSize":"1.25rem","lineHeight":"1.6","margin":"0"},p='hero')+'\n'+chips,{"textAlign":"center","maxWidth":"760px","marginLeft":"auto","marginRight":"auto"},p='hero')
hero_bg={"backgroundColor":CREAM,"backgroundImage":"radial-gradient(circle at 92% 10%, rgba(12,105,128,0.18) 0, transparent 40%), radial-gradient(circle at 6% 95%, rgba(196,57,29,0.12) 0, transparent 38%)"}
parts.append(section('hero',hero,hero_bg,extra={"paddingTop":"6rem","paddingBottom":"6rem"}))
# GROUPS
for gid,name,ic,bg,prev,qa in groups:
    left=el(icon_circ(ic,gid)+'\n'+tx(name,'h2',{"marginBottom":"0.75rem"},p=gid,gc=["gbp-section__headline"])+'\n'+bar(gid,False,"0"),{"position":"sticky","top":"8rem","alignSelf":"start",M1024:{"position":"relative","top":"0"}},p=gid)
    right=el('\n'.join(faq(q,a,gid) for q,a in qa),{"display":"flex","flexDirection":"column","rowGap":"1rem"},p=gid)
    parts.append(section(gid,el(left+'\n'+right,{"display":"grid","gridTemplateColumns":"minmax(0, 0.7fr) minmax(0, 1.3fr)","columnGap":"4rem","rowGap":"2rem","alignItems":"start",M1024:{"gridTemplateColumns":"1fr"}},p=gid),bg,div=prev,anchor=gid))
# CTA
cta_bg={"backgroundColor":NAVY,"backgroundImage":"radial-gradient(circle at 12% 20%, rgba(12,105,128,0.65) 0, transparent 45%), radial-gradient(circle at 88% 85%, rgba(196,57,29,0.4) 0, transparent 40%)"}
inner=el(tx('Still deciding?','h2',{"color":WHITE,"marginBottom":"0.75rem"},p='cta')+'\n'+bar('cta',True,"1.5rem")+'\n'+tx('The Scorecard takes five minutes and shows you where to start.','p',{"color":WHITE,"fontSize":"1.1875rem","marginBottom":"2rem"},p='cta')+'\n'+el(btn('Take the Growing Pains Scorecard','/scorecard/','cta',hover=TEAL),{"display":"flex","justifyContent":"center"},p='cta'),{"textAlign":"center","maxWidth":"720px","marginLeft":"auto","marginRight":"auto"},p='cta')
parts.append(section('cta',inner,cta_bg,div=CREAM))
open(OUT+'04-faqs.html','w').write('\n\n'.join(parts)+'\n')
# JSON-LD
def plain(a):
    if a=="LIST": return "Growing Pains Scorecard: free. Focus Session: free, 30 minutes. Map It: $750, credited toward the 3P Reset if you start within 30 days. The 3P Reset: $2,500 founding rate for my first three clients, then $3,500. 3P Partnership: $4,500 — the Reset plus 90 days of support."
    return re.sub(r'<[^>]+>','',a)
ents=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":plain(a)}} for g in groups for q,a in g[5]]
ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":ents}
open(OUT+'04-faqs-schema.html','w').write('<script type="application/ld+json">\n'+json.dumps(ld,ensure_ascii=False,indent=2)+'\n</script>\n')
