
# =====================================================================
# REAL ESTATE INDUSTRY PAGE BODY (uses the Paper Desk helpers above)
# =====================================================================
AMPSEMI = AMP + 'amp;'
ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'
ICON['heart'] = '<path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"></path>'

# ---- 1. HERO (dot grid, base)
contact_card = el('reherocard', 'div', {'alignItems': 'center', 'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px',
                                        'boxShadow': CARD_SH, 'columnGap': '1.125rem', 'display': 'inline-flex', 'padding': '1.25rem 1.75rem',
                                        'transform': 'rotate(-0.8deg)', 'textAlign': 'left',
                                        '@media (max-width:600px)': {'flexDirection': 'column', 'textAlign': 'center', 'rowGap': '0.75rem'}}, [
    badge('reherocardbd', 'phone', size=52, icon_size='1.4rem'),
    el('reherocardtxt', 'div', None, [
        tx('reherocardhd', 'p', 'Hire Your Team',
           {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC, 'margin': '0 0 0.5rem', 'lineHeight': '1'}),
        btn('reherobtn', 'Request a Consultation', '/contact/'),
    ]),
])
hero_inner = el('reherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                                      'maxWidth': '46rem', 'textAlign': 'center', 'position': 'relative'}, [
    eyebrow('reheroeye', "Real Estate"),
    tx('reheroh1', 'h1', "Accounting for Investors, Property Managers " + AMPSEMI + " <em>Real Estate Businesses</em>",
       {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
        'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('reheroh1')),
    para('reherop', "For real estate investors, property managers, and brokerages that need clean, entity-by-entity books and lender-ready financials — without hiring a full internal accounting department. Controller-level oversight, QuickBooks Online Certified, scaled to your budget.",
         size='1.125rem', mb='2rem', extra={'maxWidth': '40rem'}),
    contact_card,
])
hero = section('rehero', BASE, [
    doodle('rehero_heart', 'ledger', '40px', '40px', '-8', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('rehero_doc', 'doc', '34px', '44px', '12', {'bottom': '-4px', 'left': '9%'}, INK),
    doodle('rehero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    hero_inner,
], pad=100, extra_bg=DOTGRID)

# ---- 2. PAIN POINTS (dark ink)
pains = [
    "Multiple properties or entities are tracked in one messy spreadsheet or QuickBooks file",
    "Rent roll and actual bank deposits don't match up",
    "CapEx vs. repair expenses get miscategorized, throwing off depreciation",
    "Books aren't clean enough to hand to a lender when it's time to refinance or acquire",
    "Property-level P" + AMPSEMI + "Ls are impossible to pull on demand",
]
pain_rows = [dot_row('repain%d' % (i + 1), t, color=HI, size='1.125rem', text_color=BASE, mt='0.3em', icon='alert')
             for i, t in enumerate(pains)]
pain_list = col('repainlist', pain_rows, gap='0.9rem', extra={'textAlign': 'left', 'maxWidth': '38rem', 'margin': '0 auto 2rem'})
pain = section('repainsec', INK, [
    doodle('repain_coffee', 'coffee', '40px', '40px', '8', {'top': '8px', 'right': '8%'}, HI),
    doodle('repain_receipt', 'receipt', '38px', '44px', '-10', {'bottom': '10px', 'left': '7%'}, ACC),
    el('repainwrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                             'maxWidth': '40rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('repaineye', 'Common Pain Points', HI),
        h2('repainh2', 'Sound Familiar?', BASE, mb='1.75rem'),
        pain_list,
        tx('repainclose', 'p', "That's where a structured, entity-aware approach makes the difference.",
           {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3rem', 'lineHeight': '1.5', 'color': HI, 'margin': '0'}),
    ]),
])

# ---- 3. HOW PACIOLI HELPS (surface, dashed borders; 4 cards, no links)
cards_data = [
    ('stack', "Entities", "Entity " + AMPSEMI + " Property-Level Accounting", "Each property or entity tracked separately, so P" + AMPSEMI + "Ls are accurate and ready on demand.", '-0.6'),
    ('receipt', "Rent Roll", "Rent Roll Reconciliation", "Rent roll reconciled to actual bank deposits every month, so nothing slips through.", '0.5'),
    ('calc', "CapEx", "CapEx " + AMPSEMI + " Depreciation Tracking", "Capital improvements and depreciation tracked correctly for accurate tax treatment.", '-0.4'),
    ('handshake', "Lenders", "Lender-Ready Financials", "Books maintained clean and current, so financing applications move faster.", '0.6'),
]
card_els = []
for i, (ic, tag, title, desc, rot) in enumerate(cards_data, 1):
    u = 'rehelp%d' % i
    card_els.append(el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                                  'padding': '1.5rem', 'display': 'flex', 'flexDirection': 'column', 'rowGap': '0.6rem',
                                  'transform': 'rotate(%sdeg)' % rot}, [
        el(u + 'top', 'div', {'alignItems': 'center', 'columnGap': '0.75rem', 'display': 'flex', 'marginBottom': '0.4rem'}, [
            badge(u + 'bd', ic),
            tx(u + 'step', 'span', tag, {'fontFamily': HAND, 'fontSize': '1.35rem', 'fontWeight': '700', 'color': ACC}),
        ]),
        tx(u + 'h3', 'h3', title, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.25rem', 'color': INK,
                                   'letterSpacing': '-0.015em', 'margin': '0', 'lineHeight': '1.25', 'textWrap': 'balance'}),
        para(u + 'p', desc, size='0.9375rem', mb='0', extra={'lineHeight': '1.55'}),
    ]))
cards_grid = el('rehelpgrid', 'div', {'display': 'grid', 'gridTemplateColumns': 'repeat(4,minmax(0,1fr))', 'columnGap': '1.75rem', 'rowGap': '2rem',
                                      '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                                      '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, card_els)
helps = section('rehelpsec', SURF, [
    doodle('rehelp_clip', 'clip', '30px', '44px', '18', {'top': '10px', 'right': '6%'}, INK),
    eyebrow('rehelpeye', 'The Approach'),
    h2('rehelph2', 'How Pacioli Helps', mb='0.75rem'),
    para('rehelpintro', "Pacioli provides a pool of finance and accounting experts dedicated to keeping every property and entity clean, reconciled, and ready to report on — whenever you need it.",
         mb='2.75rem', extra={'maxWidth': '46rem'}),
    cards_grid,
], dashed=True)

# ---- 4. FREE NON-PROFIT BOOKS REVIEW (grid paper, base)
assess_items = [
    "A review of your current entity structure, rent roll, and reconciliation process",
    "Identification of gaps before your next refinance or acquisition",
    "A clear recommendation — no fluff, no pressure",
    "A roadmap for outsourced support scoped to your budget",
]
note = el('renote', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                            'padding': '2rem', 'transform': 'rotate(1.5deg)', 'position': 'relative',
                            'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
    doodle('renote_clip', 'clip', '30px', '48px', '12', {'top': '-22px', 'right': '24px'}, ACC, hide_mobile=False),
    tx('renotehd', 'span', 'What the review covers', {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC}),
    col('renotelist', [dot_row('renote%d' % (i + 1), t, size='1rem', text_color=INK) for i, t in enumerate(assess_items)], gap='0.85rem'),
])
assess_left = el('reassessleft', 'div', None, [
    eyebrow('reassesseye', 'Get Started'),
    h2('reassessh2', "Start With a Free Portfolio Books Review"),
    para('reassessp', 'This is the obvious first step, not a sales pitch. <strong>Hire Your Team</strong> to get started.', mb='2rem'),
    btn('reassessbtn', 'Request a Consultation', '/contact/'),
], cls='gb-element')
assess = section('reassesssec', BASE, [
    doodle('reassess_pencil', 'pencil', '30px', '42px', '-10', {'bottom': '10px', 'right': '3%'}, INK),
    el('reassessgrid', 'div', {'alignItems': 'center', 'columnGap': '4rem', 'display': 'grid', 'gridTemplateColumns': '1.1fr 1fr',
                               'rowGap': '2.5rem', '@media (max-width:900px)': {'gridTemplateColumns': '1fr'}},
       [assess_left, note]),
], extra_bg=GRIDPAPER)

# ---- 5. WHY NON-PROFITS TRUST PACIOLI (lined paper, surface)
trust_data = [
    ('target', "A Priority Industry", "Real estate is one of Pacioli's priority industries, alongside technology, legal, and education"),
    ('refresh', "A Structured Process", "The same structured, separation-of-duties process we give every client relationship we take on"),
    ('users', "Controller-Level Oversight", "Controller-level oversight from a Certified Management Accountant (CMA)"),
]
trust_items = []
for i, (ic, t, d) in enumerate(trust_data, 1):
    u = 'retrust%d' % i
    trust_items.append(el(u, 'div', {'columnGap': '1rem', 'display': 'flex'}, [
        badge(u + 'bd', ic, size=56, icon_size='1.6rem'),
        el(u + 'txt', 'div', None, [
            tx(u + 'h3', 'h3', t, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.125rem', 'color': INK, 'margin': '0 0 0.3rem'}),
            para(u + 'p', d, size='0.9375rem', mb='0', extra={'lineHeight': '1.5'}),
        ]),
    ]))
trust = section('retrustsec', SURF, [
    doodle('retrust_star', 'star', '30px', '30px', '8', {'top': '14px', 'right': '7%'}),
    eyebrow('retrusteye', 'The Track Record'),
    h2('retrusth2', "Why Real Estate Businesses Trust Pacioli", mb='2.5rem'),
    el('retrustgrid', 'div', {'columnGap': '2.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '2rem',
                              '@media (max-width:1024px)': {'gridTemplateColumns': '1fr'}}, trust_items),
], pad=72, extra_bg=LINED)

# ---- 6. PROMISE (dot grid, base)
vals = [('doc', 'Clarity', 'Financial information that is organized, understandable, and useful'),
        ('trend', 'Accuracy', 'Accounting processes designed to maintain reliable financial records'),
        ('chat', 'Communication', 'Real people who talk with you and your team, not just software and reports'),
        ('shield', 'Accountability', "A team that takes ownership of the work within your engagement's scope"),
        ('users', 'Collaboration', 'We work with you, your employees, and your other professional advisors'),
        ('stack', 'Scalability', 'Services that change as your business grows, rather than forcing you into a fixed package')]
val_els = []
for i, (ic, t, d) in enumerate(vals, 1):
    u = 'reprom%d' % i
    val_els.append(el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px',
                                 'boxShadow': '3px 3px 0 rgba(34, 48, 77, 0.9)', 'padding': '1.25rem 1.5rem',
                                 'transform': 'rotate(%sdeg)' % ('-0.4' if i % 2 else '0.4')}, [
        tx(u + 'h3', 'h3', t, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.125rem', 'color': ACC, 'margin': '0 0 0.35rem'}),
        para(u + 'p', d, size='0.9375rem', mb='0', extra={'lineHeight': '1.5'}),
    ]))
promise = section('repromsec', BASE, [
    doodle('reprom_brief', 'briefcase', '44px', '44px', '-8', {'top': '8px', 'left': '6%'}, INK),
    doodle('reprom_doc', 'doc', '34px', '44px', '12', {'top': '12px', 'right': '7%'}, ACC),
    el('repromhead', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto 3rem',
                             'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('repromeye', 'Our Promise to You'),
        h2('repromh2', 'Your Business. Your Numbers. <em>Your Accounting Department.</em>', mb='1.25rem', extra_css=hi_css('repromh2')),
        para('reprompara', "We don't believe you should have to build a large internal accounting department to receive professional accounting support. Our role can expand or contract as your portfolio changes.", mb='0'),
    ]),
    el('repromgrid', 'div', {'columnGap': '1.75rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '1.75rem',
                             '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                             '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, val_els),
], extra_bg=DOTGRID)

# ---- 7. TESTIMONIALS (surface, dashed)
quotes = [('We have been working with them for several years and could not be happier to have Pacioli as a partner… Pacioli has taken over nearly all of our financial needs.', 'Joseph A.', 'Middle Tree', '-0.6'),
          ('I highly recommend working with Pacioli Finance. If you are not working with them, you are missing out. This is my bookkeeping service for life!', 'Donna G.', 'Language Exploration Enrichment', '0.6')]
q_els = []
for i, (q, nm, org, rot) in enumerate(quotes, 1):
    u = 'requote%d' % i
    q_els.append(el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                               'padding': '2rem', 'transform': 'rotate(%sdeg)' % rot}, [
        tx(u + 'mark', 'p', '“', {'fontFamily': HEAD, 'fontSize': '3rem', 'lineHeight': '0.6', 'color': ACC, 'margin': '0 0 0.75rem', 'fontWeight': '700'}),
        tx(u + 'q', 'p', q, {'fontFamily': HEAD, 'fontSize': '1.1875rem', 'fontStyle': 'italic', 'lineHeight': '1.5', 'color': INK, 'margin': '0 0 1.25rem'}),
        tx(u + 'nm', 'p', nm, {'fontFamily': BODY, 'fontSize': '0.9375rem', 'fontWeight': '700', 'color': INK, 'margin': '0'}),
        tx(u + 'org', 'p', org, {'fontFamily': BODY, 'fontSize': '0.875rem', 'color': MUTED, 'margin': '0'}),
    ]))
testi = section('retestsec', SURF, [
    doodle('retest_star', 'star', '30px', '30px', '-8', {'top': '14px', 'right': '7%'}),
    eyebrow('retesteye', 'Client Feedback'),
    h2('retesth2', 'What Clients Say', mb='2.5rem'),
    el('retestgrid', 'div', {'columnGap': '2.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '2rem',
                             '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, q_els),
], pad=72, dashed=True)

# ---- 8. CLOSING CTA (solid accent)
cta = section('rectasec', ACC, [
    doodle('recta_plane', 'plane', '52px', '52px', '10', {'top': '10px', 'left': '8%'}, '#ffffff'),
    doodle('recta_star', 'star', '30px', '30px', '-6', {'bottom': '12px', 'right': '9%'}),
    el('rectawrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                            'maxWidth': '36rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('rectaeye', "Let's Talk", HI),
        h2('rectah2', "Ready for books a lender won't blink at?", '#ffffff', mb='1.75rem'),
        btn('rectabtn', 'Request a Consultation', '/contact/', 'light'),
    ]),
], pad=72, hattrs={'id': 'contact'})

page = '\n\n'.join([hero, pain, helps, assess, trust, promise, testi, cta]) + '\n'
sys.stdout.write(page)
