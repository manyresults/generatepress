
# =====================================================================
# NON-PROFIT INDUSTRY PAGE BODY (uses the Paper Desk helpers above)
# =====================================================================
AMPSEMI = AMP + 'amp;'
ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'
ICON['heart'] = '<path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"></path>'

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
    eyebrow('cuheroeye', 'Non-Profit'),
    tx('cuheroh1', 'h1', 'Compliance-Ready Books for <em>Mission-Driven</em> Organizations',
       {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
        'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('cuheroh1')),
    para('cuherop', 'For non-profits and mission-driven organizations that need audit-ready financials and clean grant reporting — without diverting staff time and focus away from the mission. Controller-level oversight, QuickBooks Online Certified, scaled to your budget.',
         size='1.125rem', mb='2rem', extra={'maxWidth': '40rem'}),
    contact_card,
])
hero = section('cuhero', BASE, [
    doodle('cuhero_heart', 'heart', '40px', '40px', '-8', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('cuhero_doc', 'doc', '34px', '44px', '12', {'bottom': '-4px', 'left': '9%'}, INK),
    doodle('cuhero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    hero_inner,
], pad=100, extra_bg=DOTGRID)

# ---- 2. PAIN POINTS (dark ink)
pains = [
    "Grant reporting deadlines pile up and fund restrictions aren't tracked cleanly",
    'Board members ask for financials that take days to pull together',
    'One person handles the books, with no real segregation of duties',
    'Form 990 season turns into a scramble every year',
    "Donor records and program expenses live in separate systems that don't reconcile",
]
pain_rows = [dot_row('cupain%d' % (i + 1), t, color=HI, size='1.125rem', text_color=BASE, mt='0.3em', icon='alert')
             for i, t in enumerate(pains)]
pain_list = col('cupainlist', pain_rows, gap='0.9rem', extra={'textAlign': 'left', 'maxWidth': '38rem', 'margin': '0 auto 2rem'})
pain = section('cupainsec', INK, [
    doodle('cupain_coffee', 'coffee', '40px', '40px', '8', {'top': '8px', 'right': '8%'}, HI),
    doodle('cupain_receipt', 'receipt', '38px', '44px', '-10', {'bottom': '10px', 'left': '7%'}, ACC),
    el('cupainwrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                             'maxWidth': '40rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('cupaineye', 'Common Pain Points', HI),
        h2('cupainh2', 'Sound Familiar?', BASE, mb='1.75rem'),
        pain_list,
        tx('cupainclose', 'p', "That's where a structured, nonprofit-aware approach makes the difference.",
           {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3rem', 'lineHeight': '1.5', 'color': HI, 'margin': '0'}),
    ]),
])

# ---- 3. HOW PACIOLI HELPS (surface, dashed borders; 4 cards, no links)
cards_data = [
    ('stack', 'Funds', 'Fund Accounting ' + AMPSEMI + ' Grant Tracking', 'Restricted vs. unrestricted funds tracked cleanly, so every grant reports exactly where it needs to.', '-0.6'),
    ('trend', 'Board', 'Board-Ready Financial Reporting', 'Clear statements of financial position and activities, ready whenever the board needs them.', '0.5'),
    ('doc', 'Form 990', 'Form 990 Preparation Support', 'Books organized and reconciled ahead of filing season, so nothing is a last-minute scramble.', '-0.4'),
    ('shield', 'Controls', 'Internal Controls for Small Teams', 'Segregated duties built around lean nonprofit staffing, reducing risk without adding headcount.', '0.6'),
]
card_els = []
for i, (ic, tag, title, desc, rot) in enumerate(cards_data, 1):
    u = 'cuhelp%d' % i
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
cards_grid = el('cuhelpgrid', 'div', {'display': 'grid', 'gridTemplateColumns': 'repeat(4,minmax(0,1fr))', 'columnGap': '1.75rem', 'rowGap': '2rem',
                                      '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                                      '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, card_els)
helps = section('cuhelpsec', SURF, [
    doodle('cuhelp_clip', 'clip', '30px', '44px', '18', {'top': '10px', 'right': '6%'}, INK),
    eyebrow('cuhelpeye', 'The Approach'),
    h2('cuhelph2', 'How Pacioli Helps', mb='0.75rem'),
    para('cuhelpintro', 'Pacioli provides a pool of finance and accounting experts who understand fund accounting, grant restrictions, and board reporting — so your team can stay focused on the mission, not the ledger.',
         mb='2.75rem', extra={'maxWidth': '46rem'}),
    cards_grid,
], dashed=True)

# ---- 4. FREE NON-PROFIT BOOKS REVIEW (grid paper, base)
assess_items = ['A review of your current fund accounting setup and grant tracking',
                'Identification of gaps before your next audit or Form 990 filing',
                'A clear recommendation — no fluff, no pressure',
                'A roadmap for outsourced support scoped to your budget']
note = el('cunote', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                            'padding': '2rem', 'transform': 'rotate(1.5deg)', 'position': 'relative',
                            'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
    doodle('cunote_clip', 'clip', '30px', '48px', '12', {'top': '-22px', 'right': '24px'}, ACC, hide_mobile=False),
    tx('cunotehd', 'span', 'What the review covers', {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC}),
    col('cunotelist', [dot_row('cunote%d' % (i + 1), t, size='1rem', text_color=INK) for i, t in enumerate(assess_items)], gap='0.85rem'),
])
assess_left = el('cuassessleft', 'div', None, [
    eyebrow('cuassesseye', 'Get Started'),
    h2('cuassessh2', 'Start With a Free Non-Profit Books Review'),
    para('cuassessp', 'This is the obvious first step, not a sales pitch. <strong>Hire Your Team</strong> to get started.', mb='2rem'),
    btn('cuassessbtn', 'Request a Consultation', '/contact/'),
], cls='gb-element')
assess = section('cuassesssec', BASE, [
    doodle('cuassess_pencil', 'pencil', '30px', '42px', '-10', {'bottom': '10px', 'right': '3%'}, INK),
    el('cuassessgrid', 'div', {'alignItems': 'center', 'columnGap': '4rem', 'display': 'grid', 'gridTemplateColumns': '1.1fr 1fr',
                               'rowGap': '2.5rem', '@media (max-width:900px)': {'gridTemplateColumns': '1fr'}},
       [assess_left, note]),
], extra_bg=GRIDPAPER)

# ---- 5. WHY NON-PROFITS TRUST PACIOLI (lined paper, surface)
trust_data = [('heart', 'Mission-Friendly Rates', 'Comfortable working near pro bono or reduced rates for mission-driven organizations'),
              ('refresh', 'A Structured Process', 'The same structured, separation-of-duties process we give every client relationship we take on'),
              ('users', 'Controller-Level Oversight', 'Controller-level oversight from a Certified Management Accountant (CMA)')]
trust_items = []
for i, (ic, t, d) in enumerate(trust_data, 1):
    u = 'cutrust%d' % i
    trust_items.append(el(u, 'div', {'columnGap': '1rem', 'display': 'flex'}, [
        badge(u + 'bd', ic, size=56, icon_size='1.6rem'),
        el(u + 'txt', 'div', None, [
            tx(u + 'h3', 'h3', t, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.125rem', 'color': INK, 'margin': '0 0 0.3rem'}),
            para(u + 'p', d, size='0.9375rem', mb='0', extra={'lineHeight': '1.5'}),
        ]),
    ]))
trust = section('cutrustsec', SURF, [
    doodle('cutrust_star', 'star', '30px', '30px', '8', {'top': '14px', 'right': '7%'}),
    eyebrow('cutrusteye', 'The Track Record'),
    h2('cutrusth2', 'Why Non-Profits Trust Pacioli', mb='2.5rem'),
    el('cutrustgrid', 'div', {'columnGap': '2.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '2rem',
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
    u = 'cuprom%d' % i
    val_els.append(el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px',
                                 'boxShadow': '3px 3px 0 rgba(34, 48, 77, 0.9)', 'padding': '1.25rem 1.5rem',
                                 'transform': 'rotate(%sdeg)' % ('-0.4' if i % 2 else '0.4')}, [
        tx(u + 'h3', 'h3', t, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.125rem', 'color': ACC, 'margin': '0 0 0.35rem'}),
        para(u + 'p', d, size='0.9375rem', mb='0', extra={'lineHeight': '1.5'}),
    ]))
promise = section('cupromsec', BASE, [
    doodle('cuprom_brief', 'briefcase', '44px', '44px', '-8', {'top': '8px', 'left': '6%'}, INK),
    doodle('cuprom_doc', 'doc', '34px', '44px', '12', {'top': '12px', 'right': '7%'}, ACC),
    el('cupromhead', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto 3rem',
                             'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('cupromeye', 'Our Promise to You'),
        h2('cupromh2', 'Your Business. Your Numbers. <em>Your Accounting Department.</em>', mb='1.25rem', extra_css=hi_css('cupromh2')),
        para('cuprompara', "We don't believe you should have to build a large internal accounting department to receive professional accounting support. Our role can expand or contract as your organization changes.", mb='0'),
    ]),
    el('cupromgrid', 'div', {'columnGap': '1.75rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '1.75rem',
                             '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                             '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, val_els),
], extra_bg=DOTGRID)

# ---- 7. TESTIMONIALS (surface, dashed)
quotes = [('We have been working with them for several years and could not be happier to have Pacioli as a partner… Pacioli has taken over nearly all of our financial needs.', 'Joseph A.', 'Middle Tree', '-0.6'),
          ('I highly recommend working with Pacioli Finance. If you are not working with them, you are missing out. This is my bookkeeping service for life!', 'Donna G.', 'Language Exploration Enrichment', '0.6')]
q_els = []
for i, (q, nm, org, rot) in enumerate(quotes, 1):
    u = 'cuquote%d' % i
    q_els.append(el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                               'padding': '2rem', 'transform': 'rotate(%sdeg)' % rot}, [
        tx(u + 'mark', 'p', '“', {'fontFamily': HEAD, 'fontSize': '3rem', 'lineHeight': '0.6', 'color': ACC, 'margin': '0 0 0.75rem', 'fontWeight': '700'}),
        tx(u + 'q', 'p', q, {'fontFamily': HEAD, 'fontSize': '1.1875rem', 'fontStyle': 'italic', 'lineHeight': '1.5', 'color': INK, 'margin': '0 0 1.25rem'}),
        tx(u + 'nm', 'p', nm, {'fontFamily': BODY, 'fontSize': '0.9375rem', 'fontWeight': '700', 'color': INK, 'margin': '0'}),
        tx(u + 'org', 'p', org, {'fontFamily': BODY, 'fontSize': '0.875rem', 'color': MUTED, 'margin': '0'}),
    ]))
testi = section('cutestsec', SURF, [
    doodle('cutest_star', 'star', '30px', '30px', '-8', {'top': '14px', 'right': '7%'}),
    eyebrow('cutesteye', 'Client Feedback'),
    h2('cutesth2', 'What Clients Say', mb='2.5rem'),
    el('cutestgrid', 'div', {'columnGap': '2.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '2rem',
                             '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, q_els),
], pad=72, dashed=True)

# ---- 8. CLOSING CTA (solid accent)
cta = section('cuctasec', ACC, [
    doodle('cucta_plane', 'plane', '52px', '52px', '10', {'top': '10px', 'left': '8%'}, '#ffffff'),
    doodle('cucta_star', 'star', '30px', '30px', '-6', {'bottom': '12px', 'right': '9%'}),
    el('cuctawrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                            'maxWidth': '36rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('cuctaeye', "Let's Talk", HI),
        h2('cuctah2', 'Ready to hand off the books to a team that gets your mission?', '#ffffff', mb='1.75rem'),
        btn('cuctabtn', 'Request a Consultation', '/contact/', 'light'),
    ]),
], pad=72, hattrs={'id': 'contact'})

page = '\n\n'.join([hero, pain, helps, assess, trust, testi, cta]) + '\n'  # "Our Promise to You" removed from industry pages (hub keeps its own)
sys.stdout.write(page)
