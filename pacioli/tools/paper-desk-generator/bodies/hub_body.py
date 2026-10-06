
# =====================================================================
# INDUSTRIES HUB BODY (uses the Paper Desk helpers above)
# =====================================================================
AMPSEMI = AMP + 'amp;'
ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'
ICON['heart'] = '<path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"></path>'
ICON['building'] = '<rect x="5" y="3" width="14" height="18" rx="1"></rect><path d="M9 7h.01M13 7h.01M9 11h.01M13 11h.01M9 15h.01M13 15h.01M10 21v-3h4v3"></path>'
ICON['code'] = '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"></path>'

# ---- 1. HERO (dot grid, base)
contact_card = el('cuherocard', 'div', {'alignItems': 'center', 'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px',
                                        'boxShadow': CARD_SH, 'columnGap': '1.125rem', 'display': 'inline-flex', 'padding': '1.25rem 1.75rem',
                                        'transform': 'rotate(-0.8deg)', 'textAlign': 'left',
                                        '@media (max-width:600px)': {'flexDirection': 'column', 'textAlign': 'center', 'rowGap': '0.75rem'}}, [
    badge('cuherocardbd', 'phone', size=52, icon_size='1.4rem'),
    el('cuherocardtxt', 'div', None, [
        tx('cuherocardhd', 'p', 'Hire Your Team',
           {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC, 'margin': '0 0 0.5rem', 'lineHeight': '1'}),
        btn('cuherobtn', 'Request a Consultation', '/contact/'),
    ]),
])
hero_inner = el('cuherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                                      'maxWidth': '46rem', 'textAlign': 'center', 'position': 'relative'}, [
    eyebrow('cuheroeye', 'Who We Work With'),
    tx('cuheroh1', 'h1', 'Industries <em>We Serve</em>',
       {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
        'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('cuheroh1')),
    para('cuherop', 'Pacioli Finance serves established businesses nationwide — with priority focus on non-profit, education, real estate, technology, legal, and professional services, plus select light-manufacturing businesses. Every industry brings its own reporting quirks, compliance rules, and cash-flow patterns, and we tailor our controller-level support to match.',
         size='1.125rem', mb='2rem', extra={'maxWidth': '42rem'}),
    contact_card,
])
hero = section('cuhero', BASE, [
    doodle('cuhero_building', 'building', '38px', '46px', '-8', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('cuhero_briefcase', 'briefcase', '40px', '40px', '12', {'bottom': '-4px', 'left': '9%'}, INK),
    doodle('cuhero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    hero_inner,
], pad=100, extra_bg=DOTGRID)

# ---- 2. INDUSTRY CARD GRID (grid paper, base)
inds = [
    ('heart', 'Non-Profit', 'Compliance-ready books for mission-driven organizations', '/industries/non-profit/', '-0.6'),
    ('ledger', 'Education', 'Accounting support for schools, programs ' + AMPSEMI + ' ed-focused businesses', '/industries/education/', '0.5'),
    ('briefcase', 'Professional Services', 'Accounting for consulting, marketing ' + AMPSEMI + ' professional services firms', '/industries/professional-services/', '-0.4'),
    ('building', 'Real Estate', 'Accounting for investors, property managers ' + AMPSEMI + ' real estate businesses', '/industries/real-estate/', '0.6'),
    ('code', 'Technology', 'Accounting for SaaS, software ' + AMPSEMI + ' tech-enabled businesses', '/industries/technology/', '-0.5'),
    ('scale', 'Legal', 'Accounting for law firms ' + AMPSEMI + ' professional service practices', '/industries/legal/', '0.4'),
]
ind_els = []
for i, (ic, name, desc, href, rot) in enumerate(inds, 1):
    u = 'cuind%d' % i
    ind_els.append(el(u, 'a', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                               'display': 'flex', 'flexDirection': 'column', 'padding': '1.75rem', 'textDecoration': 'none',
                               'rowGap': '0.6rem', 'transform': 'rotate(%sdeg)' % rot,
                               'transition': 'transform 0.15s ease, box-shadow 0.15s ease',
                               '&:is(:hover, :focus)': {'transform': 'translate(-2px, -2px) rotate(0deg)', 'boxShadow': '7px 7px 0 rgba(34, 48, 77, 0.9)'}}, [
        el(u + 'bdw', 'div', {'marginBottom': '0.4rem'}, [badge(u + 'bd', ic, size=52, icon_size='1.5rem')]),
        tx(u + 'h3', 'h3', name, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.375rem', 'color': INK,
                                  'letterSpacing': '-0.015em', 'margin': '0', 'lineHeight': '1.2'}),
        para(u + 'p', desc, size='0.9375rem', mb='1rem', extra={'lineHeight': '1.55', 'flexGrow': '1'}),
        el(u + 'ft', 'div', {'alignItems': 'center', 'color': ACC, 'columnGap': '0.5em', 'display': 'flex', 'fontFamily': BODY,
                             'fontSize': '0.9375rem', 'fontWeight': '600', 'svg': {'height': '1em', 'width': '1em'}},
           [tx(u + 'ftt', 'span', 'Learn more'), sh(u + 'fts', ARROW, {'display': 'inline-flex'})]),
    ], hattrs={'href': href}))
ind_grid = el('cuindgrid', 'div', {'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'columnGap': '2rem', 'rowGap': '2.25rem',
                                   '@media (max-width:900px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                                   '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, ind_els)
grid = section('cuindsec', BASE, [
    doodle('cuind_clip', 'clip', '30px', '44px', '18', {'top': '10px', 'right': '6%'}, INK),
    ind_grid,
], pad=72, extra_bg=GRIDPAPER)

# ---- 3. WHY INDUSTRY EXPERTISE MATTERS (surface, dashed)
vals = [('doc', 'Clarity', 'Financial information that is organized, understandable, and useful'),
        ('trend', 'Accuracy', 'Accounting processes designed to maintain reliable financial records'),
        ('chat', 'Communication', 'Real people who talk with you and your team, not just software and reports'),
        ('shield', 'Accountability', "A team that takes ownership of the work within your engagement's scope"),
        ('users', 'Collaboration', 'We work with you, your employees, and your other professional advisors'),
        ('stack', 'Scalability', 'Services that change as your business grows, rather than forcing you into a fixed package')]
val_els = []
for i, (ic, t, d) in enumerate(vals, 1):
    u = 'cuwhy%d' % i
    val_els.append(el(u, 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'textAlign': 'center'}, [
        el(u + 'bdw', 'div', {'marginBottom': '0.875rem'}, [badge(u + 'bd', ic, size=64, icon_size='1.6rem')]),
        tx(u + 'h3', 'h3', t, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.1875rem', 'color': INK, 'margin': '0 0 0.375rem'}),
        para(u + 'p', d, size='0.9375rem', mb='0', extra={'lineHeight': '1.5', 'maxWidth': '18rem'}),
    ]))
why = section('cuwhysec', SURF, [
    doodle('cuwhy_pencil', 'pencil', '28px', '40px', '16', {'top': '12px', 'right': '7%'}, ACC),
    el('cuwhyhead', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto 2.75rem',
                            'maxWidth': '42rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('cuwhyeye', 'What to Expect'),
        h2('cuwhyh2', 'Why Industry Expertise Matters', mb='0.75rem'),
        para('cuwhyintro', 'Across every industry we serve, clients can expect:', mb='0'),
    ]),
    el('cuwhygrid', 'div', {'columnGap': '2rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '2.5rem',
                            '@media (max-width:900px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                            '@media (max-width:560px)': {'gridTemplateColumns': '1fr'}}, val_els),
], dashed=True)

# ---- 4. FAQ (dot grid, base)
faqs = [('Does Pacioli Finance only work with businesses in these six industries?',
         'These are our priority industries, but we work with any established business, anywhere in the United States, that needs controller-level accounting support.', '-0.4'),
        ('Do you charge differently by industry?',
         'No. Pacioli uses one flexible hourly model with a monthly minimum that scales with your needs, regardless of industry.', '0.4'),
        ('Can you support a business that spans more than one of these industries?',
         "Yes. Many clients don't fit neatly into one category, and our engagements are scoped around your actual needs, not a fixed package.", '-0.3')]
faq_els = []
for i, (q, a, rot) in enumerate(faqs, 1):
    u = 'cufaq%d' % i
    faq_els.append(el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                                 'padding': '1.5rem 1.75rem', 'transform': 'rotate(%sdeg)' % rot}, [
        tx(u + 'q', 'h3', q, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.1875rem', 'color': INK, 'margin': '0 0 0.5rem', 'lineHeight': '1.3'}),
        para(u + 'a', a, size='1rem', mb='0', extra={'lineHeight': '1.6'}),
    ]))
faq = section('cufaqsec', BASE, [
    doodle('cufaq_coffee', 'coffee', '38px', '38px', '8', {'top': '14px', 'left': '7%'}, ACC),
    el('cufaqwrap', 'div', {'margin': '0 auto', 'maxWidth': '44rem', 'position': 'relative'}, [
        el('cufaqhead', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'marginBottom': '2.5rem', 'textAlign': 'center'}, [
            eyebrow('cufaqeye', 'Good to Know'),
            h2('cufaqh2', 'Frequently Asked Questions', mb='0'),
        ]),
        col('cufaqlist', faq_els, gap='1.75rem'),
    ]),
], extra_bg=DOTGRID)

# ---- 5. CLOSING CTA (solid accent)
cta = section('cuctasec', ACC, [
    doodle('cucta_plane', 'plane', '52px', '52px', '10', {'top': '10px', 'left': '8%'}, '#ffffff'),
    doodle('cucta_star', 'star', '30px', '30px', '-6', {'bottom': '12px', 'right': '9%'}),
    el('cuctawrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                            'maxWidth': '36rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('cuctaeye', "Let's Talk", HI),
        h2('cuctah2', "Not sure which industry fits? Let's talk about your business.", '#ffffff', mb='1.75rem'),
        btn('cuctabtn', 'Request a Consultation', '/contact/', 'light'),
    ]),
], pad=72, hattrs={'id': 'contact'})

page = '\n\n'.join([hero, grid, why, faq, cta]) + '\n'
sys.stdout.write(page)
