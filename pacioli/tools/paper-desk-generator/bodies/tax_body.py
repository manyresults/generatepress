
# =====================================================================
# TAX & COMPLIANCE PAGE BODY (uses the Paper Desk helpers above)
# =====================================================================
AMPSEMI = AMP + 'amp;'

# ---- 1. HERO (dot grid, base)
hero_inner = el('cuherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                                      'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
    eyebrow('cuheroeye', 'Federal, State, and Local Tax Services'),
    tx('cuheroh1', 'h1', 'Comprehensive Tax Services for <em>Businesses</em>',
       {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
        'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('cuheroh1')),
    para('cuherop', 'Sales and use tax, federal, state, and local filings, new business formation, and essential as-needed tax forms — stay compliant with expert guidance, without the burden of in-house tax staffing.',
         size='1.125rem', mb='2rem', extra={'maxWidth': '38rem'}),
    btn('cuherobtn', 'Request a Consultation', '/contact'),
])
hero = section('cuhero', BASE, [
    doodle('cuhero_receipt', 'receipt', '40px', '48px', '-8', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('cuhero_calc', 'calc', '34px', '44px', '12', {'bottom': '-4px', 'left': '9%'}, INK),
    doodle('cuhero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    hero_inner,
], pad=100, extra_bg=DOTGRID)

# ---- 2. PAIN POINTS (dark ink)
pains = [
    "You're not sure whether you have sales tax nexus in every state you sell into",
    'Federal, state, and local filing deadlines are scattered across a dozen different calendars',
    "You're starting a new business and don't know whether to form an LLC, S-corp, or C-corp",
    "IRS or state notices show up and you don't have a plan for responding",
    'Forms like the EIN application, S-corp election, or Power of Attorney feel like a maze',
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
        tx('cupainclose', 'p', "That's where proactive, end-to-end tax guidance makes the difference.",
           {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3rem', 'lineHeight': '1.5', 'color': HI, 'margin': '0 0 1.75rem'}),
        btn('cupainbtn', 'Request a Consultation', '/contact', 'light'),
    ]),
])

# ---- 3. HOW PACIOLI HELPS (surface, dashed borders)
cards_data = [
    ('receipt', 'Sales tax', 'Sales ' + AMPSEMI + ' Use Tax', 'Nexus analysis, taxability determinations, filing, and exemption certificate management across every state you operate in.', '#sales', '-0.6'),
    ('stack', 'Income tax', 'Federal, State ' + AMPSEMI + ' Local Filings', 'Income/franchise tax compliance, audit support, credits and incentives, and a tax calendar that keeps every deadline covered.', '#federal', '0.5'),
    ('briefcase', 'New business', 'New Business Formation', 'EIN setup, entity selection, name/trademark screening, and state and local registrations — from idea to compliant operation.', '#business-formation', '-0.4'),
    ('doc', 'IRS forms', 'As-Needed IRS Forms', 'S-corp elections, Powers of Attorney, reporting agent authorizations, and EFTPS enrollment, prepared and filed correctly the first time.', '#tax-forms', '0.6'),
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
    para('cuhelpintro', 'Pacioli delivers comprehensive, end-to-end tax services that help you stay compliant, minimize risk, and optimize cash flow, combining deep technical expertise with scalable processes and proactive guidance.',
         mb='2.75rem', extra={'maxWidth': '46rem'}),
    cards_grid,
], dashed=True)

# ---- 4. FREE TAX REVIEW (grid paper, base)
assess_items = ['A review of your current filing obligations across federal, state, and local jurisdictions',
                'A nexus check to flag states where you may have unrecognized exposure',
                'A clear recommendation — no fluff, no pressure',
                'A compliance calendar scoped to your business and industry']
note = el('cunote', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                            'padding': '2rem', 'transform': 'rotate(1.5deg)', 'position': 'relative',
                            'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
    doodle('cunote_clip', 'clip', '30px', '48px', '12', {'top': '-22px', 'right': '24px'}, ACC, hide_mobile=False),
    tx('cunotehd', 'span', 'What the review covers', {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC}),
    col('cunotelist', [dot_row('cunote%d' % (i + 1), t, size='1rem', text_color=INK) for i, t in enumerate(assess_items)], gap='0.85rem'),
])
assess_left = el('cuassessleft', 'div', None, [
    eyebrow('cuassesseye', 'Get Started'),
    h2('cuassessh2', 'Start With a Free Tax Review'),
    para('cuassessp', 'This is the obvious first step, not a sales pitch — a clear-eyed look at where your books stand today.', mb='2rem'),
    btn('cuassessbtn', 'Hire Your Team', '/contact'),
], cls='gb-element')
assess = section('cuassesssec', BASE, [
    doodle('cuassess_pencil', 'pencil', '30px', '42px', '-10', {'bottom': '10px', 'left': '4%'}, INK),
    el('cuassessgrid', 'div', {'alignItems': 'center', 'columnGap': '4rem', 'display': 'grid', 'gridTemplateColumns': '1.1fr 1fr',
                               'rowGap': '2.5rem', '@media (max-width:900px)': {'gridTemplateColumns': '1fr'}},
       [assess_left, note]),
], extra_bg=GRIDPAPER)

# ---- 5. TRUST (lined paper, surface)
trust_data = [('shield', 'QuickBooks Certified', 'All Pacioli accountants are QuickBooks Online Certified Pro Advisors.'),
              ('refresh', 'A Structured Process', 'The same separation-of-duties process we give every client relationship we take on.'),
              ('users', 'Controller-Level Oversight', 'Overseen by an owner with a CMA (Certified Management Accountant) credential.')]
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

# ---- 6. MID CTA (solid accent)
mid = section('cumidsec', ACC, [
    doodle('cumid_plane', 'plane', '52px', '52px', '10', {'top': '10px', 'left': '8%'}, '#ffffff'),
    doodle('cumid_star', 'star', '30px', '30px', '-6', {'bottom': '12px', 'right': '9%'}),
    el('cumidwrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                            'maxWidth': '40rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('cumideye', "Curious What's Included?", HI),
        h2('cumidh2', 'See exactly what tax ' + AMPSEMI + ' compliance look like in practice.', '#ffffff', mb='1.75rem'),
        el('cumidbtns', 'div', {'alignItems': 'center', 'columnGap': '1rem', 'display': 'flex', 'justifyContent': 'center',
                                '@media (max-width:767px)': {'flexDirection': 'column', 'rowGap': '1rem'}}, [
            btn('cumidbtn1', 'Request a Consultation', '/contact', 'light'),
            btn('cumidbtn2', 'See the Full Service Breakdown', '#service-breakdown', 'ghost'),
        ]),
    ]),
], pad=72)

# ---- 7. PROMISE (dot grid, base)
vals = [('target', 'Clarity', 'Organized, understandable, useful financial information.'),
        ('scale', 'Accuracy', 'Accounting processes designed to maintain reliable records.'),
        ('chat', 'Communication', 'Real people, not just software and reports.'),
        ('shield', 'Accountability', 'A team that owns the work within scope.'),
        ('handshake', 'Collaboration', 'We work with you and your other advisors.'),
        ('trend', 'Scalability', 'Services that change as your business grows, not a fixed package.')]
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
        para('cuprompara', "We don't believe you should have to build a large internal accounting department to receive professional accounting support. Our role can expand or contract as your business changes.", mb='2rem'),
        btn('cuprombtn', 'Request a Consultation', '/contact'),
    ]),
    tx('cupromsub', 'h3', 'What You Can Expect From Us', {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.375rem', 'color': INK,
                                                          'margin': '0 0 1.5rem', 'position': 'relative'}),
    el('cupromgrid', 'div', {'columnGap': '1.75rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '1.75rem',
                             '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                             '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, val_els),
], extra_bg=DOTGRID)

# ---- 8. FULL SERVICE BREAKDOWN (GB Pro accordion, 6 items)
sales = ['Sales taxability determinations — evaluate what products/services are taxable in each state and locality',
         'Nexus and economic nexus analysis — assess where you have tax obligations based on sales activity, thresholds, and marketplace facilitators',
         'Sales tax compliance and filing — prepare and file monthly, quarterly, or annual returns',
         'Exemption certificate management — track, verify, and maintain certificates to reduce risk',
         'Refunds and credits management — identify overpayments and maximize eligible credits',
         'State and Local Tax (SALT) planning — proactive planning to minimize SALT exposure']
federal = ['Federal income tax compliance — accurate accounting method and entity-level treatment',
           'Tax provision and ASC 740 support — quarterly/annual provision calculations and disclosures',
           'Tax planning and strategy — R' + AMPSEMI + 'D credits, deductions, and timing strategies',
           'IRS audit support and representation', 'Tax reform and legislative updates',
           'Federal estimated tax payments — quarterly vouchers']
state = ['State income/franchise tax compliance, apportionment and allocation analysis',
         'State nexus and apportionment studies (three-factor, single-factor methods)',
         'State tax credits and incentives', 'State tax audits and appeals',
         'State tax calendar and remittance management across states']
local = ['Local sales/use tax compliance for city or municipal levels',
         'Local income/business taxes, including gross receipts and city-specific filings',
         'Local tax registration and permit management', 'Local audit support and rate monitoring']
formation = ['EIN Setup — prepare and submit your federal Employer Identification Number application, then deliver a post-issuance onboarding checklist for payroll and tax setup',
             'Entity Selection ' + AMPSEMI + ' Structuring — evaluate LLC, S-corp, C-corp, partnership, and nonprofit options; deliverable includes a recommended entity type, governance outline, and a 90–180 day formation plan',
             'Name Availability ' + AMPSEMI + ' Trademark Screening — federal/state/local name search, preliminary trademark clearance, and domain/SEO considerations',
             'State and Local Business Registrations — Secretary of State filings, local licenses, zoning approvals, industry permits, plus a renewal/compliance calendar']
forms_intro = 'Common IRS authorization and election forms we help clients prepare, file, and maintain:'
forms = ['Form 2553 — Election by a Small Business Corporation (S-corp election for pass-through taxation)',
         'Form 2848 — Power of Attorney and Declaration of Representative (authorizes a practitioner to represent you before the IRS)',
         'Form 8655 — Reporting Agent Authorization (authorizes a third-party agent to file certain returns on your behalf)',
         'Form 8821 — Tax Information Authorization (grants information access without representation authority)',
         'Form 9779 — EFTPS Business Enrollment (electronic federal tax payment setup)',
         'Form 9783T — Third Party Authorization (limited-scope access for a trusted advisor, varies by tax authority)']

items = [
    acc_item(1, 'sales', 'receipt', 'Sales and Use Tax', [dot_row('cus%d' % (i + 1), t) for i, t in enumerate(sales)]),
    acc_item(2, 'federal', 'doc', 'Federal Tax Filings', [dot_row('cuf%d' % (i + 1), t) for i, t in enumerate(federal)]),
    acc_item(3, 'state', 'stack', 'State Tax Filings', [dot_row('cust%d' % (i + 1), t) for i, t in enumerate(state)]),
    acc_item(4, 'local', 'ledger', 'Local Tax Filings', [dot_row('cul%d' % (i + 1), t) for i, t in enumerate(local)]),
    acc_item(5, 'business-formation', 'briefcase', 'New Business Formation Services', [dot_row('cub%d' % (i + 1), t) for i, t in enumerate(formation)]),
    acc_item(6, 'tax-forms', 'clip', 'As-Needed Business Tax Forms',
             [plain_row('cufi', forms_intro)] + [dot_row('cuff%d' % (i + 1), t) for i, t in enumerate(forms)]),
]
accordion = blk('generateblocks-pro/accordion', {'uniqueId': uid('cuaccordion'), 'tagName': 'div'},
                '<div class="gb-accordion">', '\n\n'.join(items), '</div>')
breakdown = section('cubreaksec', SURF, [
    doodle('cubreak_pencil', 'pencil', '28px', '40px', '16', {'top': '12px', 'right': '7%'}, ACC),
    eyebrow('cubreakeye', 'Scope of Work'),
    h2('cubreakh2', 'Full Service Breakdown', mb='2.5rem'),
    accordion,
], dashed=True, hattrs={'id': 'service-breakdown'})

refs = '<!-- wp:block {"ref":51469} /-->\n\n<!-- wp:block {"ref":51507} /-->'
page = '\n\n'.join([hero, pain, helps, assess, trust, mid, promise, breakdown, refs]) + '\n'
sys.stdout.write(page)
