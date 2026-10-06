import os
# =====================================================================
# TAX PREP CHECKLISTS HUB BODY  (cards read from pacioli/tax-checklists-hub.html)
# =====================================================================
AMPSEMI = AMP + 'amp;'
SRC = open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), '..', '..', '..', 'tax-checklists-hub.html')).read() 
P = 'hub'
for m in [0]: pass
cards_src = re.findall(r'<a class="gb-element-c\d+ gb-element" href="([^"]+)">.*?<h3[^>]*>(.*?)</h3>.*?<p[^>]*>(.*?)</p>', SRC, re.S)
assert len(cards_src) == 7, len(cards_src)
intro_txt = re.search(r'<h1[^>]*>.*?</h1>.*?<p[^>]*>(.*?)</p>', SRC, re.S).group(1).strip()
fix = lambda t: re.sub(r'&(?!#?\w+;)', AMPSEMI, t.strip())
ICONS = ['briefcase', 'handshake', 'ledger', 'stack', 'scale', 'doc', 'receipt']

hero = section('hubhero', BASE, [
    doodle('hubhero_doc', 'doc', '34px', '44px', '12', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('hubhero_clip', 'clip', '30px', '44px', '-14', {'bottom': '-2px', 'left': '9%'}, INK),
    doodle('hubhero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    el('hubherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                              'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('hubheroeye', 'Resources'),
        tx('hubh1', 'h1', 'Tax Prep <em>Checklists</em>',
           {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
            'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('hubh1')),
        para('hubherop', intro_txt, size='1.125rem', mb='0', extra={'maxWidth': '38rem'}),
    ]),
], pad=100, extra_bg=DOTGRID)

card_els = []
for i, (href, title, desc) in enumerate(cards_src, 1):
    u = 'hubc%d' % i
    card_els.append(el(u, 'a', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                                'display': 'flex', 'flexDirection': 'column', 'padding': '1.5rem', 'textDecoration': 'none',
                                'transform': 'rotate(%sdeg)' % ('-0.5' if i % 2 else '0.5'),
                                'transition': 'transform 0.15s ease, box-shadow 0.15s ease',
                                '&:is(:hover, :focus)': {'transform': 'translate(-2px, -2px) rotate(0deg)', 'boxShadow': '6px 6px 0 rgba(34, 48, 77, 0.9)'}},
                       [
        el(u + 'top', 'div', {'marginBottom': '1rem'}, [badge(u + 'bd', ICONS[i - 1])]),
        tx(u + 'h3', 'h3', fix(title), {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.375rem', 'color': INK,
                                       'letterSpacing': '-0.015em', 'margin': '0 0 0.4rem', 'lineHeight': '1.25'}),
        para(u + 'p', fix(desc), size='0.9375rem', mb='1.25rem', extra={'lineHeight': '1.5', 'flexGrow': '1'}),
        el(u + 'ft', 'div', {'alignItems': 'center', 'color': ACC, 'columnGap': '0.4em', 'display': 'flex', 'fontFamily': BODY,
                             'fontSize': '0.9375rem', 'fontWeight': '700'}, [
            tx(u + 'ftt', 'span', 'View checklist'),
            sh(u + 'fts', ARROW, {'display': 'inline-flex', 'svg': {'height': '1em', 'width': '1em'}}),
        ]),
    ], hattrs={'href': href}))
listing = section('hublistsec', SURF, [
    doodle('hublist_pencil', 'pencil', '30px', '42px', '-10', {'top': '14px', 'right': '5%'}, INK),
    el('hubgrid', 'div', {'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'columnGap': '1.75rem', 'rowGap': '2rem',
                          '@media (max-width:900px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                          '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, card_els),
], pad=72, extra_bg=GRIDPAPER)

sys.stdout.write('\n\n'.join([hero, listing]) + '\n')
