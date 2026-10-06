# =====================================================================
# TAX PREP CHECKLIST PAGE BODY  (one body, six pages)
# usage: CL=1065 python3 -I build.py bodies/checklist_body.py > ../../tax-checklist-1065-paper.html
# Copy (title, intro, groups, list items, links) is read straight from the existing
# pacioli/tax-checklist-<slug>.html so nothing is retyped.
# =====================================================================
import os
AMPSEMI = AMP + 'amp;'
SLUG = os.environ['CL']
SRC = open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), '..', '..', '..', 'tax-checklist-%s.html' % SLUG)).read()
P = 'cl' + re.sub(r'[^a-z0-9]', '', SLUG.lower())
ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'

def inner(pattern):
    return re.search(pattern, SRC, re.S).group(1).strip()

eyebrow_txt = re.sub(r'<[^>]+>', '', inner(r'<h5[^>]*>(.*?)</h5>'))
h1_txt = re.sub(r'<[^>]+>', '', inner(r'<h1[^>]*>(.*?)</h1>'))
title_main = h1_txt.replace(' Prep Checklist', '')
intro_txt = inner(r'<h1[^>]*>.*?</h1>.*?<p[^>]*>(.*?)</p>')
# optional note block (Schedule C only): a link + a reminder paragraph
note_m = re.search(r'<a class="gb-element-c\w*notelink[^>]*href="([^"]+)"[^>]*>(.*?)</a>.*?<p[^>]*>(.*?)</p>', SRC, re.S)
# groups: each <h3> followed by its <li> items (h3s inside the hero card or CTA are not present)
groups = []
for m in re.finditer(r'<h3[^>]*>(.*?)</h3>(.*?)(?=<h3|<h5|\Z)', SRC, re.S):
    items = re.findall(r'<li[^>]*>(.*?)</li>', m.group(2), re.S)
    if items:
        groups.append((m.group(1).strip(), [i.strip() for i in items]))
assert groups, SLUG

GROUP_ICON = ['doc', 'users', 'stack', 'ledger', 'briefcase', 'receipt']
LINK_CSS = '.gb-text-%s a{color:var(--paper-accent);text-decoration:underline;text-underline-offset:2px}'

# ---- 1. HERO (dot grid)
hero_card = el(P + 'herocard', 'div', {'alignItems': 'center', 'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px',
                                       'boxShadow': CARD_SH, 'columnGap': '1.125rem', 'display': 'inline-flex', 'padding': '1.25rem 1.75rem',
                                       'transform': 'rotate(-0.8deg)', 'textAlign': 'left',
                                       '@media (max-width:600px)': {'flexDirection': 'column', 'textAlign': 'center', 'rowGap': '0.75rem'}}, [
    badge(P + 'herocardbd', 'phone', size=52, icon_size='1.4rem'),
    el(P + 'herocardtxt', 'div', None, [
        tx(P + 'herocardhd', 'p', 'Not sure what applies to you?',
           {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC, 'margin': '0 0 0.5rem', 'lineHeight': '1'}),
        btn(P + 'herobtn', 'Request a Consultation', '/contact/'),
    ]),
])
hero = section(P + 'hero', BASE, [
    doodle(P + 'hero_doc', 'doc', '34px', '44px', '12', {'top': '-4px', 'right': '10%'}, ACC),
    doodle(P + 'hero_clip', 'clip', '30px', '44px', '-14', {'bottom': '-2px', 'left': '9%'}, INK),
    doodle(P + 'hero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    el(P + 'herowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                               'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow(P + 'heroeye', eyebrow_txt),
        tx(P + 'h1', 'h1', '%s <em>Prep Checklist</em>' % title_main,
           {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
            'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css(P + 'h1')),
        para(P + 'herop', intro_txt, size='1.125rem', mb='2rem', extra={'maxWidth': '40rem'}),
        hero_card,
    ]),
], pad=100, extra_bg=DOTGRID)

# ---- 2. CHECKLIST (grid paper, one card per group)
kids = []
if note_m:
    kids.append(el(P + 'note', 'div', {'backgroundColor': 'rgba(242, 198, 51, 0.18)', 'border': '1.5px dashed ' + LINE, 'borderRadius': '12px',
                                       'padding': '1.25rem 1.5rem', 'display': 'flex', 'flexDirection': 'column', 'rowGap': '0.5rem'}, [
        tx(P + 'notelink', 'a', note_m.group(2).strip(),
           {'fontFamily': BODY, 'fontWeight': '700', 'fontSize': '1rem', 'color': ACC, 'textDecoration': 'underline'},
           hattrs={'href': note_m.group(1)}),
        para(P + 'notetxt', note_m.group(3).strip(), size='0.9375rem', mb='0'),
    ]))
for gi, (title, items) in enumerate(groups, 1):
    g = '%sg%d' % (P, gi)
    rows = []
    for ii, it in enumerate(items, 1):
        u = '%sr%d' % (g, ii)
        rows.append(el(u, 'div', {'alignItems': 'flex-start', 'columnGap': '0.75rem', 'display': 'flex'}, [
            sh(u + 'd', DOT, {'color': ACC, 'display': 'block', 'flexShrink': '0', 'marginTop': '0.5em', 'svg': {'height': '7px', 'width': '7px'}}),
            tx(u + 't', 'p', it, {'fontFamily': BODY, 'color': MUTED, 'fontSize': '0.9375rem', 'lineHeight': '1.6', 'margin': '0'},
               extra_css=LINK_CSS % (u + 't')),
        ]))
    kids.append(el(g, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                              'padding': '1.75rem', 'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem',
                              'transform': 'rotate(%sdeg)' % ('-0.3' if gi % 2 else '0.3')}, [
        el(g + 'top', 'div', {'alignItems': 'center', 'columnGap': '0.75rem', 'display': 'flex', 'marginBottom': '0.25rem'}, [
            badge(g + 'bd', GROUP_ICON[(gi - 1) % len(GROUP_ICON)]),
            tx(g + 'h3', 'h3', title, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.375rem', 'color': INK,
                                       'letterSpacing': '-0.015em', 'margin': '0', 'lineHeight': '1.25'}),
        ]),
        col(g + 'list', rows, gap='0.7rem'),
    ]))
listing = section(P + 'listsec', SURF, [
    doodle(P + 'list_pencil', 'pencil', '30px', '42px', '-10', {'top': '14px', 'right': '5%'}, INK),
    el(P + 'listwrap', 'div', {'display': 'flex', 'flexDirection': 'column', 'rowGap': '2rem', 'margin': '0 auto', 'maxWidth': '48rem',
                               'position': 'relative'}, kids),
], pad=72, extra_bg=GRIDPAPER)

# ---- 3. CLOSING CTA (solid accent)
cta = section(P + 'ctasec', ACC, [
    doodle(P + 'cta_plane', 'plane', '52px', '52px', '10', {'top': '10px', 'left': '8%'}, '#ffffff'),
    doodle(P + 'cta_star', 'star', '30px', '30px', '-6', {'bottom': '12px', 'right': '9%'}),
    el(P + 'ctawrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                              'maxWidth': '36rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow(P + 'ctaeye', 'Ready When You Are', HI),
        h2(P + 'ctah2', 'Have your documents ready? Let' + AMP + '#8217;s get filing.', '#ffffff', mb='1.75rem'),
        btn(P + 'ctabtn', 'Request a Consultation', '/contact/', 'light'),
    ]),
], pad=72, hattrs={'id': 'contact'})

sys.stdout.write('\n\n'.join([hero, listing, cta]) + '\n')
