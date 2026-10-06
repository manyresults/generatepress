
# =====================================================================
# EDUCATION INDUSTRY PAGE BODY (uses the Paper Desk helpers above)
# =====================================================================
AMPSEMI = AMP + 'amp;'
ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'
ICON['heart'] = '<path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"></path>'

# ---- 1. HERO (dot grid, base)
contact_card = el('edherocard', 'div', {'alignItems': 'center', 'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px',
                                        'boxShadow': CARD_SH, 'columnGap': '1.125rem', 'display': 'inline-flex', 'padding': '1.25rem 1.75rem',
                                        'transform': 'rotate(-0.8deg)', 'textAlign': 'left',
                                        '@media (max-width:600px)': {'flexDirection': 'column', 'textAlign': 'center', 'rowGap': '0.75rem'}}, [
    badge('edherocardbd', 'phone', size=52, icon_size='1.4rem'),
    el('edherocardtxt', 'div', None, [
        tx('edherocardhd', 'p', 'Hire Your Team',
           {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC, 'margin': '0 0 0.5rem', 'lineHeight': '1'}),
        btn('edherobtn', 'Request a Consultation', '/contact/'),
    ]),
])
hero_inner = el('edherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                                      'maxWidth': '46rem', 'textAlign': 'center', 'position': 'relative'}, [
    eyebrow('edheroeye', "Education"),
    tx('edheroh1', 'h1', "Accounting Support for Schools, Programs " + AMPSEMI + " <em>Ed-Focused Businesses</em>",
       {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
        'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('edheroh1')),
    para('edherop', "For schools, tutoring companies, and education-focused businesses that need tuition and program revenue tracked correctly — without building an internal finance team. Controller-level oversight, QuickBooks Online Certified, scaled to your budget.",
         size='1.125rem', mb='2rem', extra={'maxWidth': '40rem'}),
    contact_card,
])
hero = section('edhero', BASE, [
    doodle('edhero_heart', 'doc', '40px', '40px', '-8', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('edhero_doc', 'doc', '34px', '44px', '12', {'bottom': '-4px', 'left': '9%'}, INK),
    doodle('edhero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    hero_inner,
], pad=100, extra_bg=DOTGRID)

# ---- 2. PAIN POINTS (dark ink)
pains = [
    "Tuition and program revenue come in through multiple channels that don't reconcile cleanly",
    "Multi-location or multi-program budgets get tracked in scattered spreadsheets",
    "Grant or scholarship funding has restrictions nobody is formally tracking",
    "Month-end close takes weeks because enrollment and revenue data live in separate systems",
    "Leadership can't get a clear read on program-level profitability",
]
pain_rows = [dot_row('edpain%d' % (i + 1), t, color=HI, size='1.125rem', text_color=BASE, mt='0.3em', icon='alert')
             for i, t in enumerate(pains)]
pain_list = col('edpainlist', pain_rows, gap='0.9rem', extra={'textAlign': 'left', 'maxWidth': '38rem', 'margin': '0 auto 2rem'})
pain = section('edpainsec', INK, [
    doodle('edpain_coffee', 'coffee', '40px', '40px', '8', {'top': '8px', 'right': '8%'}, HI),
    doodle('edpain_receipt', 'receipt', '38px', '44px', '-10', {'bottom': '10px', 'left': '7%'}, ACC),
    el('edpainwrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                             'maxWidth': '40rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('edpaineye', 'Common Pain Points', HI),
        h2('edpainh2', 'Sound Familiar?', BASE, mb='1.75rem'),
        pain_list,
        tx('edpainclose', 'p', "That's where a structured, education-aware approach makes the difference.",
           {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3rem', 'lineHeight': '1.5', 'color': HI, 'margin': '0'}),
    ]),
])

# ---- 3. HOW PACIOLI HELPS (surface, dashed borders; 4 cards, no links)
cards_data = [
    ('receipt', "Revenue", "Tuition " + AMPSEMI + " Program Revenue Reconciliation", "Every payment channel reconciled to the general ledger, so revenue is never a guess.", '-0.6'),
    ('calc', "Budgets", "Multi-Program Budgeting", "Budgets built and tracked by program or location, not just company-wide.", '0.5'),
    ('stack', "Funding", "Grant " + AMPSEMI + " Scholarship Fund Tracking", "Restricted funding tracked separately so reporting stays accurate.", '-0.4'),
    ('trend', "Leadership", "Leadership-Ready Reporting", "Clear, program-level financials that leadership and boards can actually use.", '0.6'),
]
card_els = []
for i, (ic, tag, title, desc, rot) in enumerate(cards_data, 1):
    u = 'edhelp%d' % i
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
cards_grid = el('edhelpgrid', 'div', {'display': 'grid', 'gridTemplateColumns': 'repeat(4,minmax(0,1fr))', 'columnGap': '1.75rem', 'rowGap': '2rem',
                                      '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                                      '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, card_els)
helps = section('edhelpsec', SURF, [
    doodle('edhelp_clip', 'clip', '30px', '44px', '18', {'top': '10px', 'right': '6%'}, INK),
    eyebrow('edhelpeye', 'The Approach'),
    h2('edhelph2', 'How Pacioli Helps', mb='0.75rem'),
    para('edhelpintro', "Pacioli provides a pool of finance and accounting experts dedicated to keeping tuition, program, and grant revenue organized and reportable — so leadership always knows where the numbers stand.",
         mb='2.75rem', extra={'maxWidth': '46rem'}),
    cards_grid,
], dashed=True)

# ---- 4. FREE NON-PROFIT BOOKS REVIEW (grid paper, base)
assess_items = [
    "A review of your current revenue tracking, budgeting, and close process",
    "Identification of gaps in program-level or grant reporting",
    "A clear recommendation — no fluff, no pressure",
    "A roadmap for outsourced support scoped to your budget",
]
note = el('ednote', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                            'padding': '2rem', 'transform': 'rotate(1.5deg)', 'position': 'relative',
                            'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
    doodle('ednote_clip', 'clip', '30px', '48px', '12', {'top': '-22px', 'right': '24px'}, ACC, hide_mobile=False),
    tx('ednotehd', 'span', 'What the review covers', {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC}),
    col('ednotelist', [dot_row('ednote%d' % (i + 1), t, size='1rem', text_color=INK) for i, t in enumerate(assess_items)], gap='0.85rem'),
])
assess_left = el('edassessleft', 'div', None, [
    eyebrow('edassesseye', 'Get Started'),
    h2('edassessh2', "Start With a Free Education Books Assessment"),
    para('edassessp', 'This is the obvious first step, not a sales pitch. <strong>Hire Your Team</strong> to get started.', mb='2rem'),
    btn('edassessbtn', 'Request a Consultation', '/contact/'),
], cls='gb-element')
assess = section('edassesssec', BASE, [
    doodle('edassess_pencil', 'pencil', '30px', '42px', '-10', {'bottom': '10px', 'right': '3%'}, INK),
    el('edassessgrid', 'div', {'alignItems': 'center', 'columnGap': '4rem', 'display': 'grid', 'gridTemplateColumns': '1.1fr 1fr',
                               'rowGap': '2.5rem', '@media (max-width:900px)': {'gridTemplateColumns': '1fr'}},
       [assess_left, note]),
], extra_bg=GRIDPAPER)

# ---- 5. WHY NON-PROFITS TRUST PACIOLI (lined paper, surface)
trust_data = [
    ('target', "An Education Focus", "Education is one of the industries Pacioli is most passionate about serving"),
    ('refresh', "A Structured Process", "The same structured, separation-of-duties process we give every client relationship we take on"),
    ('users', "Controller-Level Oversight", "Controller-level oversight from a Certified Management Accountant (CMA)"),
]
trust_items = []
for i, (ic, t, d) in enumerate(trust_data, 1):
    u = 'edtrust%d' % i
    trust_items.append(el(u, 'div', {'columnGap': '1rem', 'display': 'flex'}, [
        badge(u + 'bd', ic, size=56, icon_size='1.6rem'),
        el(u + 'txt', 'div', None, [
            tx(u + 'h3', 'h3', t, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.125rem', 'color': INK, 'margin': '0 0 0.3rem'}),
            para(u + 'p', d, size='0.9375rem', mb='0', extra={'lineHeight': '1.5'}),
        ]),
    ]))
trust = section('edtrustsec', SURF, [
    doodle('edtrust_star', 'star', '30px', '30px', '8', {'top': '14px', 'right': '7%'}),
    eyebrow('edtrusteye', 'The Track Record'),
    h2('edtrusth2', "Why Education Businesses Trust Pacioli", mb='2.5rem'),
    el('edtrustgrid', 'div', {'columnGap': '2.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '2rem',
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
    u = 'edprom%d' % i
    val_els.append(el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px',
                                 'boxShadow': '3px 3px 0 rgba(34, 48, 77, 0.9)', 'padding': '1.25rem 1.5rem',
                                 'transform': 'rotate(%sdeg)' % ('-0.4' if i % 2 else '0.4')}, [
        tx(u + 'h3', 'h3', t, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.125rem', 'color': ACC, 'margin': '0 0 0.35rem'}),
        para(u + 'p', d, size='0.9375rem', mb='0', extra={'lineHeight': '1.5'}),
    ]))
promise = section('edpromsec', BASE, [
    doodle('edprom_brief', 'briefcase', '44px', '44px', '-8', {'top': '8px', 'left': '6%'}, INK),
    doodle('edprom_doc', 'doc', '34px', '44px', '12', {'top': '12px', 'right': '7%'}, ACC),
    el('edpromhead', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto 3rem',
                             'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('edpromeye', 'Our Promise to You'),
        h2('edpromh2', 'Your Business. Your Numbers. <em>Your Accounting Department.</em>', mb='1.25rem', extra_css=hi_css('edpromh2')),
        para('edprompara', "We don't believe you should have to build a large internal accounting department to receive professional accounting support. Our role can expand or contract as your organization changes.", mb='0'),
    ]),
    el('edpromgrid', 'div', {'columnGap': '1.75rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '1.75rem',
                             '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                             '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, val_els),
], extra_bg=DOTGRID)

# ---- 7. TESTIMONIALS (surface, dashed)
quotes = [('We have been working with them for several years and could not be happier to have Pacioli as a partner… Pacioli has taken over nearly all of our financial needs.', 'Joseph A.', 'Middle Tree', '-0.6'),
          ('I highly recommend working with Pacioli Finance. If you are not working with them, you are missing out. This is my bookkeeping service for life!', 'Donna G.', 'Language Exploration Enrichment', '0.6')]
q_els = []
for i, (q, nm, org, rot) in enumerate(quotes, 1):
    u = 'edquote%d' % i
    q_els.append(el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                               'padding': '2rem', 'transform': 'rotate(%sdeg)' % rot}, [
        tx(u + 'mark', 'p', '“', {'fontFamily': HEAD, 'fontSize': '3rem', 'lineHeight': '0.6', 'color': ACC, 'margin': '0 0 0.75rem', 'fontWeight': '700'}),
        tx(u + 'q', 'p', q, {'fontFamily': HEAD, 'fontSize': '1.1875rem', 'fontStyle': 'italic', 'lineHeight': '1.5', 'color': INK, 'margin': '0 0 1.25rem'}),
        tx(u + 'nm', 'p', nm, {'fontFamily': BODY, 'fontSize': '0.9375rem', 'fontWeight': '700', 'color': INK, 'margin': '0'}),
        tx(u + 'org', 'p', org, {'fontFamily': BODY, 'fontSize': '0.875rem', 'color': MUTED, 'margin': '0'}),
    ]))
testi = section('edtestsec', SURF, [
    doodle('edtest_star', 'star', '30px', '30px', '-8', {'top': '14px', 'right': '7%'}),
    eyebrow('edtesteye', 'Client Feedback'),
    h2('edtesth2', 'What Clients Say', mb='2.5rem'),
    el('edtestgrid', 'div', {'columnGap': '2.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '2rem',
                             '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, q_els),
], pad=72, dashed=True)

# ---- 8. CLOSING CTA (solid accent)
cta = section('edctasec', ACC, [
    doodle('edcta_plane', 'plane', '52px', '52px', '10', {'top': '10px', 'left': '8%'}, '#ffffff'),
    doodle('edcta_star', 'star', '30px', '30px', '-6', {'bottom': '12px', 'right': '9%'}),
    el('edctawrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                            'maxWidth': '36rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('edctaeye', "Let's Talk", HI),
        h2('edctah2', "Ready for financials that leadership can actually use?", '#ffffff', mb='1.75rem'),
        btn('edctabtn', 'Request a Consultation', '/contact/', 'light'),
    ]),
], pad=72, hattrs={'id': 'contact'})

page = '\n\n'.join([hero, pain, helps, assess, trust, promise, testi, cta]) + '\n'
sys.stdout.write(page)
