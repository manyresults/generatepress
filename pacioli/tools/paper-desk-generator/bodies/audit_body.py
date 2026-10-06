
# =====================================================================
# INTERNAL AUDIT PAGE BODY (uses the Paper Desk helpers above)
# =====================================================================
AMPSEMI = AMP + 'amp;'

# ---- 1. HERO (dot grid, base)
hero_inner = el('cuherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                                      'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
    eyebrow('cuheroeye', 'Internal Audit'),
    tx('cuheroh1', 'h1', 'Risk, Controls ' + AMPSEMI + ' <em>Governance</em> for Your Business',
       {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
        'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('cuheroh1')),
    para('cuherop', 'Premium internal audit services that strengthen risk management, controls, and compliance — execution, continuous monitoring, and collaborative, hands-on remediation within the finance function.',
         size='1.125rem', mb='2rem', extra={'maxWidth': '38rem'}),
    btn('cuherobtn', 'Request a Consultation', '/contact'),
])
hero = section('cuhero', BASE, [
    doodle('cuhero_shield', 'shield', '44px', '44px', '-8', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('cuhero_search', 'search', '38px', '38px', '12', {'bottom': '-4px', 'left': '9%'}, INK),
    doodle('cuhero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    hero_inner,
], pad=100, extra_bg=DOTGRID)

# ---- 2. PAIN POINTS (dark ink)
pains = [
    'Journal entries get posted with no second set of eyes reviewing them',
    'Segregation of duties across AP, AR, and payroll is more theory than practice',
    'Your external auditors keep flagging the same control gaps year after year',
    "You suspect there's process waste or fraud risk somewhere, but no one has time to look",
    "Board or investors are asking for governance and controls you don't currently have documented",
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
        tx('cupainclose', 'p', "That's where a dedicated, hands-on internal audit function makes the difference.",
           {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3rem', 'lineHeight': '1.5', 'color': HI, 'margin': '0 0 1.75rem'}),
        btn('cupainbtn', 'Request a Consultation', '/contact', 'light'),
    ]),
])

# ---- 3. HOW PACIOLI HELPS (surface, dashed borders)
cards_data = [
    ('ledger', 'Reporting', 'Reporting ' + AMPSEMI + ' Journal Entry Review', 'Regular checks on financial statements, management reports, and high-risk journal entries.', '#reporting', '-0.6'),
    ('shield', 'Controls', 'Internal Controls Testing', 'Walkthroughs, control questionnaires, and targeted testing of segregation of duties across revenue, cash, payroll, AP, and AR.', '#internal-controls', '0.5'),
    ('scale', 'Compliance', 'Compliance ' + AMPSEMI + ' Regulatory Readiness', 'Documentation kept audit-ready so external audits are never a scramble.', '#compliance', '-0.4'),
    ('search', 'Fraud risk', 'Process Improvement ' + AMPSEMI + ' Fraud Risk', 'End-to-end process mapping, automation opportunities, and fraud risk indicators built into daily operations.', '#process-improvement', '0.6'),
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
    para('cuhelpintro', 'Our team blends accounting expertise, process control proficiency, and risk advisory to deliver practical findings, actionable remediation, and board-ready reporting — available as co-sourced support, project-based audits, or a fully outsourced internal audit function.',
         mb='2.75rem', extra={'maxWidth': '46rem'}),
    cards_grid,
], dashed=True)

# ---- 4. FREE CONTROLS REVIEW (grid paper, base)
assess_items = ['A walkthrough of your current controls across revenue, cash, payroll, AP, and AR',
                'Identification of segregation-of-duties gaps and fraud risk indicators',
                'A clear recommendation — no fluff, no pressure',
                'A remediation plan tailored to your industry and growth trajectory']
note = el('cunote', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                            'padding': '2rem', 'transform': 'rotate(1.5deg)', 'position': 'relative',
                            'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
    doodle('cunote_clip', 'clip', '30px', '48px', '12', {'top': '-22px', 'right': '24px'}, ACC, hide_mobile=False),
    tx('cunotehd', 'span', 'What the review covers', {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC}),
    col('cunotelist', [dot_row('cunote%d' % (i + 1), t, size='1rem', text_color=INK) for i, t in enumerate(assess_items)], gap='0.85rem'),
])
assess_left = el('cuassessleft', 'div', None, [
    eyebrow('cuassesseye', 'Get Started'),
    h2('cuassessh2', 'Start With a Free Controls Review', mb='2rem'),
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
              ('users', 'Controller-Level Oversight', 'Overseen by a Certified Management Accountant (CMA).')]
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
        h2('cumidh2', 'See exactly what an internal audit looks like in practice.', '#ffffff', mb='1.75rem'),
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
def roles_row(u, roles):
    return tx(u, 'p', '<strong>Roles covered:</strong> ' + roles,
              {'fontFamily': BODY, 'color': MUTED, 'fontSize': '0.8125rem', 'lineHeight': '1.5', 'margin': '0.5rem 0 0',
               'paddingTop': '1rem', 'borderTop': '1px dashed ' + LINE})

acc = [
    ('reporting', 'ledger', 'Financial and Management Reporting Review',
     'Regularly assess the accuracy and timeliness of internal financial statements, management reports, and KPIs; validate consistency with GL data, policy, and accounting standards.',
     'Internal Auditor, Financial Reporting Analyst, Management Accountant, Senior Accountant, Accounting Manager, Financial Controller'),
    ('journal-entries', 'pencil', 'Journal Entry Review and Authorization',
     'Monitor, review, and approve high-risk or high-value journal entries; detect unusual or out-of-cycle entries and ensure proper documentation.',
     'Internal Auditor, GL Accountant, Senior Accountant, Accounting Manager, Financial Controller'),
    ('internal-controls', 'shield', 'Internal Controls Design and Testing',
     'Evaluate control design and operating effectiveness across revenue, cash, payroll, AP, and AR, including walkthroughs, control questionnaires, and targeted testing of segregation of duties and approval workflows.',
     'Internal Auditor, Internal Controls Analyst, SOX/Controls Specialist, Risk ' + AMPSEMI + ' Controls Manager, Audit Manager'),
    ('compliance', 'scale', 'Compliance and Regulatory Readiness (Finance)',
     'Ensure adherence to applicable finance and reporting laws/regulations, and maintain audit-ready documentation for external auditors.',
     'Compliance Analyst, Internal Auditor, Regulatory Reporting Specialist, Compliance Manager, Financial Controller'),
    ('process-improvement', 'refresh', 'Process Efficiency and Continuous Improvement',
     'Map and optimize end-to-end finance processes (procure-to-pay, order-to-cash, revenue cycles, close), identify automation opportunities, and implement small-scale improvements with minimal disruption.',
     'Process Improvement Analyst, Business Process Analyst, Internal Auditor, Finance Transformation Manager, Financial Controller'),
    ('fraud-risk', 'search', 'Fraud Risk Awareness and Early Detection',
     'Implement fraud risk indicators — vendor due diligence checks, expense report reviews, unusual spending patterns — and encourage a control-conscious culture.',
     'Fraud Risk Analyst, Internal Auditor, Forensic Accountant, Compliance Officer, Risk Manager'),
]
items = []
for n, (anchor, icon, title, body, roles) in enumerate(acc, 1):
    items.append(acc_item(n, anchor, icon, title,
                          [dot_row('cuai%d' % n, body), roles_row('cuar%d' % n, roles)]))
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
