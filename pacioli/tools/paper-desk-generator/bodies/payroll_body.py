
# =====================================================================
# PAYROLL PAGE BODY (uses the Paper Desk helpers above)
# =====================================================================
AMPSEMI = AMP + 'amp;'
ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'
ICON['globe'] = '<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"></path>'

def btn_outline(u, text, href):
    st = {'display': 'inline-flex', 'alignItems': 'center', 'justifyContent': 'center', 'fontFamily': BODY, 'fontWeight': '600',
          'fontSize': '1rem', 'textDecoration': 'none', 'paddingTop': '0.85rem', 'paddingBottom': '0.85rem',
          'paddingLeft': '1.5rem', 'paddingRight': '1.5rem', 'borderRadius': '10px', 'backgroundColor': 'transparent',
          'color': INK, 'border': '2px solid var(--paper-ink)', 'transition': 'transform 0.15s ease, box-shadow 0.15s ease',
          '&:is(:hover, :focus)': {'backgroundColor': HI, 'transform': 'translate(-1px, -1px)', 'boxShadow': '3px 3px 0 var(--paper-ink)'}}
    return tx(u, 'a', text, st, hattrs={'href': href})

def btn_row(u, kids):
    return el(u, 'div', {'alignItems': 'center', 'columnGap': '1rem', 'display': 'flex', 'flexWrap': 'wrap', 'rowGap': '0.75rem',
                         '@media (max-width:600px)': {'flexDirection': 'column', 'alignItems': 'flex-start'}}, kids)

# ---- 1. HERO (dot grid, base)
contact_card = el('cuherocard', 'div', {'alignItems': 'center', 'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px',
                                        'boxShadow': CARD_SH, 'columnGap': '1.125rem', 'display': 'inline-flex', 'padding': '1.25rem 1.75rem',
                                        'transform': 'rotate(-0.8deg)', 'textAlign': 'left',
                                        '@media (max-width:600px)': {'flexDirection': 'column', 'textAlign': 'center', 'rowGap': '0.75rem'}}, [
    badge('cuherocardbd', 'phone', size=52, icon_size='1.4rem'),
    el('cuherocardtxt', 'div', None, [
        tx('cuherocardhd', 'p', 'Run Payroll With Confidence',
           {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC, 'margin': '0 0 0.5rem', 'lineHeight': '1'}),
        btn('cuherobtn', 'Request a Consultation', '/contact'),
    ]),
])
hero_inner = el('cuherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                                      'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
    eyebrow('cuheroeye', 'Payroll ' + AMPSEMI + ' Compliance Services'),
    tx('cuheroh1', 'h1', 'Your In-House Payroll Department, Now <em>Fully Outsourced</em>',
       {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
        'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('cuheroh1')),
    para('cuherop', 'Secure, scalable, multi-state payroll processing, tax filings, benefits, and compliance — with the same rigor as an internal department, aligned with your business cadence anywhere in the United States.',
         size='1.125rem', mb='2rem', extra={'maxWidth': '38rem'}),
    contact_card,
])
hero = section('cuhero', BASE, [
    doodle('cuhero_calc', 'calc', '36px', '44px', '-8', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('cuhero_receipt', 'receipt', '34px', '42px', '12', {'bottom': '-4px', 'left': '9%'}, INK),
    doodle('cuhero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    hero_inner,
], pad=100, extra_bg=DOTGRID)

# ---- 2. PAIN POINTS (dark ink)
pains = [
    'Payroll runs are stressful because one missed timesheet or bonus throws off the whole cycle',
    'You’re not confident your multi-state tax withholdings and filings are correct',
    'Benefit deductions, garnishments, and W-2/1099 season feel like a scramble every year',
    'No one has reviewed your payroll internal controls or access permissions in years',
    'Employee questions about pay and deductions eat up time you don’t have',
]
pain_rows = [dot_row('cupain%d' % (i + 1), t, color=HI, size='1.125rem', text_color=BASE, mt='0.3em', icon='alert')
             for i, t in enumerate(pains)]
pain_list = col('cupainlist', pain_rows, gap='0.9rem', extra={'textAlign': 'left', 'maxWidth': '38rem', 'margin': '0 auto 2rem'})
pain = section('cupainsec', INK, [
    doodle('cupain_coffee', 'coffee', '40px', '40px', '8', {'top': '8px', 'right': '8%'}, HI),
    doodle('cupain_doc', 'doc', '34px', '44px', '-10', {'bottom': '10px', 'left': '7%'}, ACC),
    el('cupainwrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                             'maxWidth': '40rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('cupaineye', 'Common Pain Points', HI),
        h2('cupainh2', 'Sound Familiar?', BASE, mb='1.75rem'),
        pain_list,
        tx('cupainclose', 'p', 'That’s where a dedicated, compliance-first payroll team makes the difference.',
           {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3rem', 'lineHeight': '1.5', 'color': HI, 'margin': '0'}),
    ]),
])

# ---- 3. HOW PACIOLI HELPS (surface, dashed borders)
cards_data = [
    ('calc', 'Processing', 'Payroll Processing', 'Accurate, on-time payroll cycles — timesheets, gross-to-net calculations, direct deposits, and general ledger reconciliation.', '#payroll-processing', '-0.6'),
    ('receipt', 'Tax', 'Year-End ' + AMPSEMI + ' Tax Reporting', 'Federal, state, and local withholding, periodic filings (941s, UI taxes), and accurate W-2s/1099s.', '#tax-reporting', '0.5'),
    ('users', 'Benefits', 'Benefits ' + AMPSEMI + ' Deductions Management', 'Enrollments, contributions, and garnishments handled accurately and on schedule.', '#benefits', '-0.4'),
    ('shield', 'Audit', 'Audit Readiness', 'Segregation of duties, documented policies, and regular reconciliations that hold up under audit.', '#audit-readiness', '0.6'),
]
card_els = []
for i, (ic, tag, title, desc, href, rot) in enumerate(cards_data, 1):
    u = 'cuhelp%d' % i
    link = el(u + 'link', 'a', {'display': 'inline-flex', 'alignItems': 'center', 'columnGap': '0.5em', 'color': ACC,
                                'fontFamily': BODY, 'fontWeight': '600', 'fontSize': '0.9375rem', 'textDecoration': 'none',
                                'marginTop': 'auto', 'svg': {'width': '1em', 'height': '1em'},
                                '&:is(:hover, :focus) svg': {'transform': 'translate3d(3px, 0px, 0px)'}},
              [tx(u + 'lt', 'span', 'Learn more'), sh(u + 'ls', ARROW, {'display': 'inline-flex', 'transition': 'transform 0.15s ease'})],
              hattrs={'href': href})
    card = el(u, 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                         'padding': '1.5rem', 'display': 'flex', 'flexDirection': 'column', 'rowGap': '0.6rem',
                         'transform': 'rotate(%sdeg)' % rot}, [
        el(u + 'top', 'div', {'alignItems': 'center', 'columnGap': '0.75rem', 'display': 'flex', 'marginBottom': '0.4rem'}, [
            badge(u + 'bd', ic),
            tx(u + 'step', 'span', tag, {'fontFamily': HAND, 'fontSize': '1.35rem', 'fontWeight': '700', 'color': ACC}),
        ]),
        tx(u + 'h3', 'h3', title, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.25rem', 'color': INK,
                                   'letterSpacing': '-0.015em', 'margin': '0', 'lineHeight': '1.25', 'textWrap': 'balance'}),
        para(u + 'p', desc, size='0.9375rem', mb='0.75rem', extra={'lineHeight': '1.55'}),
        link,
    ])
    card_els.append(card)
cards_grid = el('cuhelpgrid', 'div', {'display': 'grid', 'gridTemplateColumns': 'repeat(4,minmax(0,1fr))', 'columnGap': '1.75rem', 'rowGap': '2rem',
                                      '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                                      '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, card_els)
helps = section('cuhelpsec', SURF, [
    doodle('cuhelp_clip', 'clip', '30px', '44px', '18', {'top': '10px', 'right': '6%'}, INK),
    eyebrow('cuhelpeye', 'The Approach'),
    h2('cuhelph2', 'How Pacioli Helps', mb='0.75rem'),
    para('cuhelpintro', 'Pacioli handles multi-state payroll processing, tax filings, benefits, and compliance with the same rigor as an internal payroll department.',
         mb='2.75rem', extra={'maxWidth': '46rem'}),
    cards_grid,
], dashed=True)

# ---- 4. FREE PAYROLL REVIEW (grid paper, base)
assess_items = ['A review of your current payroll process, filings, and internal controls',
                'Identification of compliance gaps across the states where you operate',
                'A clear recommendation — no fluff, no pressure',
                'A transition plan scoped to your budget and pay cycle']
note = el('cunote', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                            'padding': '2rem', 'transform': 'rotate(1.5deg)', 'position': 'relative',
                            'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
    doodle('cunote_clip', 'clip', '30px', '48px', '12', {'top': '-22px', 'right': '24px'}, ACC, hide_mobile=False),
    tx('cunotehd', 'span', 'What the review covers', {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC}),
    col('cunotelist', [dot_row('cunote%d' % (i + 1), t, size='1rem', text_color=INK) for i, t in enumerate(assess_items)], gap='0.85rem'),
])
assess_left = el('cuassessleft', 'div', None, [
    eyebrow('cuassesseye', 'Get Started'),
    h2('cuassessh2', 'Start With a Free Payroll Review'),
    para('cuassessp', 'This is the obvious first step, not a sales pitch — a clear-eyed look at how your payroll is run today, before anything changes.', mb='2rem'),
    btn_row('cuassessbtns', [btn('cuassessbtn', 'Request a Consultation', '/contact'),
                             btn_outline('cuassessbtn2', 'See What’s Included', '#service-breakdown')]),
], cls='gb-element')
assess = section('cuassesssec', BASE, [
    doodle('cuassess_pencil', 'pencil', '30px', '42px', '-10', {'bottom': '10px', 'left': '4%'}, INK),
    el('cuassessgrid', 'div', {'alignItems': 'center', 'columnGap': '4rem', 'display': 'grid', 'gridTemplateColumns': '1.1fr 1fr',
                               'rowGap': '2.5rem', '@media (max-width:900px)': {'gridTemplateColumns': '1fr'}},
       [assess_left, note]),
], extra_bg=GRIDPAPER)

# ---- 5. TRUST (lined paper, surface)
trust_data = [('globe', 'Nationwide Coverage', 'Payroll professionals staying current with multi-state tax rules and wage laws wherever you operate.'),
              ('shield', 'Consistent Controls', 'The same segregation-of-duties discipline applied across all of Pacioli’s accounting services.'),
              ('trend', 'Built to Scale', 'A flexible model that scales with new hires, new states, new benefit plans, and seasonal spikes.')]
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
    h2('cutrusth2', 'Why Businesses Trust Pacioli', mb='2.5rem'),
    el('cutrustgrid', 'div', {'columnGap': '2.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '2rem',
                              '@media (max-width:1024px)': {'gridTemplateColumns': '1fr'}}, trust_items),
], pad=72, extra_bg=LINED)

# ---- 6. PROMISE (dot grid, base)
vals = [('target', 'Clarity', 'Organized, understandable payroll reporting.'),
        ('scale', 'Accuracy', 'Reliable calculations and filings every cycle.'),
        ('chat', 'Communication', 'Real people who answer employee and owner questions.'),
        ('shield', 'Accountability', 'A team that owns the work within scope.'),
        ('handshake', 'Collaboration', 'We work with your HR team and other advisors.'),
        ('trend', 'Scalability', 'Payroll support that grows with headcount and footprint.')]
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
        para('cuprompara', 'Outsourcing payroll converts fixed in-house costs into scalable, transparent fees — giving you a full payroll team without the overhead of salaries, benefits, and training.', mb='2rem'),
        btn_row('cuprombtns', [btn('cuprombtn', 'Request a Consultation', '/contact'),
                                btn_outline('cuprombtn2', 'More About Pacioli', '/#about')]),
    ]),
    tx('cupromsub', 'h3', 'What You Can Expect From Us', {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.375rem', 'color': INK,
                                                          'margin': '0 0 1.5rem', 'position': 'relative'}),
    el('cupromgrid', 'div', {'columnGap': '1.75rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '1.75rem',
                             '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                             '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, val_els),
], extra_bg=DOTGRID)

# ---- 7. TESTIMONIALS (lined paper, base)
quotes = [('I never have to worry about the numbers or invoices or taxes or bookkeeping. I can simply run my business and trust they are keeping everything else in line for my law firm.', 'Virginia W.', 'Viking Law', '-0.6'),
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
testi = section('cutestsec', BASE, [
    doodle('cutest_star', 'star', '30px', '30px', '-8', {'top': '14px', 'right': '7%'}),
    eyebrow('cutesteye', 'Client Feedback'),
    h2('cutesth2', 'What Clients Say', mb='2.5rem'),
    el('cutestgrid', 'div', {'columnGap': '2.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '2rem',
                             '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, q_els),
], pad=72, extra_bg=LINED)

# ---- 8. FULL SERVICE BREAKDOWN (GB Pro accordion, 5 items)
def roles_row(u, roles):
    return tx(u, 'p', '<strong>Roles covered:</strong> ' + roles,
              {'fontFamily': BODY, 'color': MUTED, 'fontSize': '0.8125rem', 'lineHeight': '1.5', 'margin': '0.5rem 0 0',
               'paddingTop': '1rem', 'borderTop': '1px dashed ' + LINE})

def intro_row(u, text):
    return tx(u, 'p', text, {'fontFamily': BODY, 'color': MUTED, 'fontSize': '1rem', 'lineHeight': '1.6', 'margin': '0 0 0.25rem'})

acc = [
    ('payroll-processing', 'calc', 'Payroll Processing',
     'Prepare and run regular payroll cycles accurately and on schedule for every employee.',
     ['Collect, review, and validate timesheets, overtime, bonuses, and commission data',
      'Calculate gross pay, deductions, and net pay',
      'Process payroll, generate pay statements, and issue direct deposits or checks',
      'Enter and adjust data for new hires, terminations, status changes, and retroactive corrections',
      'Reconcile payroll registers with general ledger postings'],
     'Payroll Specialist/Analyst, Payroll Administrator, Senior Payroll Specialist, Payroll Manager'),
    ('tax-reporting', 'receipt', 'Year-End ' + AMPSEMI + ' Tax Reporting',
     'Ensure accurate tax calculations and timely filings at every level of government.',
     ['Withhold federal, state, and local taxes; manage Social Security, Medicare, and unemployment taxes',
      'File periodic payroll tax returns (941s, state and UI taxes)',
      'Generate and distribute year-end forms (W-2s, 1099s)',
      'Track tax rate changes and multi-state nexus requirements'],
     'Payroll Tax Analyst, Tax Compliance Specialist (Payroll), Payroll Manager, Tax Specialist (Corporate Tax liaison)'),
    ('benefits', 'users', 'Benefits ' + AMPSEMI + ' Deductions Management',
     'Pacioli manages enrollments, contributions, and deductions so nothing falls through the cracks each pay cycle.',
     ['Input benefit enrollments, changes, and terminations',
      'Calculate and remit employee and employer benefit deductions and contributions',
      'Track garnishments, child support, and court-ordered withholdings',
      'Maintain up-to-date benefit plan data and integration with providers'],
     'Benefits/Payroll Specialist, Payroll Administrator, HR/Payroll Liaison, Payroll Manager'),
    ('audit-readiness', 'shield', 'Audit Readiness',
     'Pacioli builds and maintains the internal controls that keep your payroll process audit-ready year-round.',
     ['Implement segregation of duties and access controls',
      'Maintain payroll policy documentation',
      'Reconcile payroll liabilities and tax accounts regularly',
      'Prepare for internal and external audits with documented controls'],
     'Internal Controls Specialist (Payroll), Payroll Manager, Compliance Officer'),
    ('employee-inquiries', 'chat', 'Employee Inquiries ' + AMPSEMI + ' Customer Service',
     'Pacioli serves as the first point of contact for payroll-related questions, keeping your team informed and your HR department focused on higher-value work.',
     ['Answer questions on paychecks, deductions, benefits, and tax withholdings',
      'Communicate changes in payroll cycles, tax laws, and policy updates',
      'Escalate complex issues to HR, IT, or legal as needed'],
     'Payroll Specialist/Analyst, Payroll Customer Service Lead, HR/Payroll Liaison'),
]
items = []
for n, (anchor, icon, title, intro, bullets, roles) in enumerate(acc, 1):
    kids = [intro_row('cuaii%d' % n, intro)] + [dot_row('cuab%d_%d' % (n, k + 1), b) for k, b in enumerate(bullets)] + [roles_row('cuar%d' % n, roles)]
    items.append(acc_item(n, anchor, icon, title, kids))
accordion = blk('generateblocks-pro/accordion', {'uniqueId': uid('cuaccordion'), 'tagName': 'div'},
                '<div class="gb-accordion">', '\n\n'.join(items), '</div>')
breakdown = section('cubreaksec', SURF, [
    doodle('cubreak_pencil', 'pencil', '28px', '40px', '16', {'top': '12px', 'right': '7%'}, ACC),
    eyebrow('cubreakeye', 'Scope of Work'),
    h2('cubreakh2', 'Full Service Breakdown', mb='2.5rem'),
    accordion,
], dashed=True, hattrs={'id': 'service-breakdown'})

page = '\n\n'.join([hero, pain, helps, assess, trust, promise, testi, breakdown]) + '\n'
sys.stdout.write(page)
