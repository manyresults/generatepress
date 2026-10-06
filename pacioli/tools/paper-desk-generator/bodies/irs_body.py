# =====================================================================
# IRS FORMS & PUBLICATIONS BODY  (list data in bodies/irs_data.json, copied from the old page)
# python3 -I build.py bodies/irs_body.py > ../../irs-forms-publications-paper.html
# =====================================================================
import os, json
AMPSEMI = AMP + 'amp;'
DATA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), 'irs_data.json')))
FIXES = [('>Schedule K-1 (Form 1120)</a>: Schedule K-1 (Form 1120)', '>Schedule K-1 (Form 1120-S)</a>: Schedule K-1 (Form 1120-S)'),
         ('QUARTERLY', 'Quarterly')]  # 1120 K-1 links to the 1120-S PDF; 941-X label was all caps
ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'
P = 'irs'

def fix(t):
    for a, b in FIXES:
        t = t.replace(a, b)
    return t

def core_list(items):
    li = ''.join('<!-- wp:list-item -->\n<li>%s</li>\n<!-- /wp:list-item -->\n\n' % fix(i) for i in items).rstrip('\n')
    return ('<!-- wp:list {"className":"pd-list"} -->\n<ul class="wp-block-list pd-list">' + li + '</ul>\n<!-- /wp:list -->')

LIST_CSS = ('.gb-element-%(u)s .pd-list{list-style:none;margin:0;padding:0;columns:2 22rem;column-gap:2.5rem;font-family:var(--paper-font-body);font-size:0.9375rem;line-height:1.5}'
            '.gb-element-%(u)s .pd-list li{break-inside:avoid;position:relative;padding:0 0 0.8rem 1.1rem;margin:0;color:var(--paper-muted)}'
            '.gb-element-%(u)s .pd-list li::before{content:"";position:absolute;left:0;top:0.55em;width:7px;height:7px;border-radius:50%%;background:var(--paper-accent)}'
            '.gb-element-%(u)s .pd-list a{color:var(--paper-ink);font-weight:700;text-decoration:underline;text-decoration-color:var(--paper-accent);text-underline-offset:3px}'
            '.gb-element-%(u)s .pd-list a:hover{color:var(--paper-accent)}')

def list_card(u, title, icon, tag, items, rot):
    card = el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                         'padding': '1.75rem 2rem', 'transform': 'rotate(%sdeg)' % rot, 'position': 'relative'},
              [], extra_css=LIST_CSS % {'u': u})
    head = el(u + 'top', 'div', {'alignItems': 'center', 'columnGap': '0.75rem', 'display': 'flex', 'marginBottom': '1.25rem'}, [
        badge(u + 'bd', icon),
        tx(u + 'h3', 'h3', title, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.5rem', 'color': INK, 'letterSpacing': '-0.015em', 'margin': '0'}),
        tx(u + 'tag', 'span', tag, {'fontFamily': HAND, 'fontSize': '1.25rem', 'fontWeight': '700', 'color': ACC, 'marginLeft': 'auto'}),
    ])
    # splice the core list block in before the card's closing tag
    return card.replace('</div>', head + '\n\n' + core_list(items) + '\n</div>', 1) if False else _splice(card, head, items)

def _splice(card, head, items):
    i = card.rindex('<!-- /wp:generateblocks/element -->')
    j = card.rindex('</div>', 0, i)
    return card[:j] + head + '\n\n' + core_list(items) + '\n' + card[j:]

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
        eyebrow(P + 'heroeye', 'Reference Library'),
        tx(P + 'h1', 'h1', 'IRS Forms ' + AMPSEMI + ' <em>Publications</em>',
           {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
            'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css(P + 'h1')),
        para(P + 'herop', 'A reference library of the IRS publications and forms we point clients to most ' + AMP + '#8212; all hosted directly on IRS.gov.',
             size='1.125rem', mb='2rem', extra={'maxWidth': '40rem'}),
        hero_card,
    ]),
], pad=100, extra_bg=DOTGRID)

note = el(P + 'note', 'div', {'backgroundColor': 'rgba(242, 198, 51, 0.18)', 'border': '1.5px dashed ' + LINE, 'borderRadius': '12px',
                              'padding': '1.25rem 1.5rem', 'display': 'flex', 'flexDirection': 'column', 'rowGap': '0.5rem'}, [
    tx(P + 'notelink', 'a', 'Get Adobe Acrobat Reader',
       {'fontFamily': BODY, 'fontWeight': '700', 'fontSize': '1rem', 'color': ACC, 'textDecoration': 'underline'},
       hattrs={'href': 'https://get.adobe.com/reader/'}),
    para(P + 'notetxt', 'The publications and forms below are PDF files hosted on the IRS website and require Adobe Acrobat Reader to view.',
         size='0.9375rem', mb='0'),
])
listing = section(P + 'listsec', SURF, [
    doodle(P + 'list_pencil', 'pencil', '30px', '42px', '-10', {'top': '14px', 'right': '4%'}, INK),
    el(P + 'listwrap', 'div', {'display': 'flex', 'flexDirection': 'column', 'rowGap': '2rem', 'position': 'relative'}, [
        note,
        list_card(P + 'pubs', 'IRS Publications', 'doc', '%d publications' % len(DATA['pubs']), DATA['pubs'], '-0.2'),
        list_card(P + 'forms', 'Forms', 'ledger', '%d forms' % len(DATA['forms']), DATA['forms'], '0.2'),
    ]),
], pad=72, extra_bg=GRIDPAPER)

cta = section(P + 'ctasec', ACC, [
    doodle(P + 'cta_plane', 'plane', '52px', '52px', '10', {'top': '10px', 'left': '8%'}, '#ffffff'),
    doodle(P + 'cta_star', 'star', '30px', '30px', '-6', {'bottom': '12px', 'right': '9%'}),
    el(P + 'ctawrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                              'maxWidth': '36rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow(P + 'ctaeye', "Still Can" + AMP + "#8217;t Find It?", HI),
        h2(P + 'ctah2', 'We' + AMP + '#8217;ll track down the right form for you.', '#ffffff', mb='1.75rem'),
        btn(P + 'ctabtn', 'Request a Consultation', '/contact/', 'light'),
    ]),
], pad=72, hattrs={'id': 'contact'})
sys.stdout.write('\n\n'.join([hero, listing, cta]) + '\n')
