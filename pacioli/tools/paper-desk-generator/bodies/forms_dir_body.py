# =====================================================================
# TAX & PAYROLL REGISTRATION FORMS DIRECTORY BODY  (data: bodies/forms_dir_data.json)
# python3 -I build.py bodies/forms_dir_body.py > ../../tax-forms-directory-paper.html
# =====================================================================
import os, json, html as _html
AMPSEMI = AMP + 'amp;'
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), 'forms_dir_data.json')))
FED = D['federal'][:6]            # the 7th scraped row is the "Select a state..." intro paragraph
ICON['pin'] = '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"></path><circle cx="12" cy="10" r="2.5"></circle>'
ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'
P = 'tf'

def esc(t):
    return _html.escape(_html.unescape(t), quote=False).replace('QUARTERLY', 'Quarterly')

def keep_tags(t):
    return re.sub(r'&', AMPSEMI, t)   # copy may contain <em>/<strong>; only & needs escaping (data was unescaped)

def link_html(it):
    if it['href']:
        return '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (_html.escape(it['href'], quote=True), esc(it['text']))
    return esc(it['text'])

def row(u, it):
    note = not it['href']
    t = tx(u + 't', 'p', link_html(it), None, cls='gb-text tf-link' + (' tf-note' if note else ''))
    d = sh(u + 'd', DOT)
    return el(u, 'div', None, [d, t], cls='gb-element tf-row')

# one global rule set for every row (a block's css attribute is emitted page-wide), keeps the file small
LINK_CSS = ('.tf-row{align-items:flex-start;column-gap:0.75rem;display:flex}'
            '.tf-row .gb-shape{color:var(--paper-accent);display:block;flex-shrink:0;margin-top:0.5em}'
            '.tf-row .gb-shape svg{height:7px;width:7px}'
            '.tf-link{font-family:var(--paper-font-body);font-size:0.9375rem;line-height:1.6;margin:0;color:var(--paper-muted)}'
            '.tf-note{font-style:italic}'
            '.tf-row:has(.tf-note) .gb-shape{color:var(--paper-line)}'
            '.tf-link a{color:var(--paper-ink);font-weight:600;text-decoration:underline;text-decoration-color:var(--paper-accent);text-underline-offset:3px}'
            '.tf-link a:hover{color:var(--paper-accent)}')

hero = section(P + 'hero', BASE, [
    doodle(P + 'hero_doc', 'doc', '34px', '44px', '12', {'top': '-4px', 'right': '10%'}, ACC),
    doodle(P + 'hero_clip', 'clip', '30px', '44px', '-14', {'bottom': '-2px', 'left': '9%'}, INK),
    doodle(P + 'hero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    el(P + 'herowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                               'maxWidth': '46rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow(P + 'heroeye', 'Resources'),
        tx(P + 'h1', 'h1', 'Tax ' + AMPSEMI + ' Payroll <em>Registration Forms</em> Directory',
           {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
            'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css(P + 'h1') + LINK_CSS),
        para(P + 'herop', keep_tags(D['intro']), size='1.125rem', mb='0', extra={'maxWidth': '40rem'}),
    ]),
], pad=100, extra_bg=DOTGRID)

fed_card = el(P + 'fedcard', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                                     'padding': '1.75rem 2rem', 'display': 'flex', 'flexDirection': 'column', 'rowGap': '0.8rem',
                                     'transform': 'rotate(-0.2deg)'},
              [row('tffed%d' % (i + 1), it) for i, it in enumerate(FED)])
federal = section(P + 'fedsec', SURF, [
    doodle(P + 'fed_pencil', 'pencil', '30px', '42px', '-10', {'top': '14px', 'right': '6%'}, INK),
    eyebrow(P + 'fedeye', 'Federal'),
    h2(P + 'fedh2', 'Federal Forms', mb='2rem'),
    el(P + 'fedwrap', 'div', {'maxWidth': '48rem'}, [fed_card]),
], pad=72, dashed=True)

acc_items = []
for n, st in enumerate(D['states'], 1):
    slug = re.sub(r'[^a-z0-9]+', '-', st['name'].lower()).strip('-')
    kids = [row('tfs%dr%d' % (n, i + 1), it) for i, it in enumerate(st['items'])]
    acc_items.append(acc_item(n, slug, 'pin', esc(st['name']), kids))
accordion = blk('generateblocks-pro/accordion', {'uniqueId': uid('tfaccordion'), 'tagName': 'div'},
                '<div class="gb-accordion">', '\n\n'.join(acc_items), '</div>')
states = section(P + 'statesec', BASE, [
    doodle(P + 'st_map', 'pin', '34px', '40px', '10', {'top': '14px', 'right': '7%'}, ACC),
    eyebrow(P + 'steye', 'State ' + AMPSEMI + ' Territory'),
    h2(P + 'sth2', 'State Forms', mb='0.75rem'),
    para(P + 'stp', keep_tags(D['select']), mb='2.5rem'),
    el(P + 'stwrap', 'div', {'maxWidth': '56rem'}, [accordion]),
], pad=72, extra_bg=GRIDPAPER)

sys.stdout.write('\n\n'.join([hero, federal, states]) + '\n')
