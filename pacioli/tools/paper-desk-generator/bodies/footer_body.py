# =====================================================================
# SITE FOOTER BODY  (Paper Desk, dark ink)
# python3 -I build.py bodies/footer_body.py > ../../footer-paper.html
# =====================================================================
AMPSEMI = AMP + 'amp;'
P = 'ft'
CREAM = 'rgba(250, 246, 236, 0.72)'

def flink(u, text, href):
    return tx(u, 'a', text, {'fontFamily': BODY, 'fontSize': '0.9375rem', 'color': CREAM, 'textDecoration': 'none', 'lineHeight': '1.4',
                             'transition': 'color 0.15s ease',
                             '&:is(:hover, :focus)': {'color': HI}}, hattrs={'href': href})

def fcol(u, title, links):
    return el(u, 'div', None, [
        tx(u + 'h', 'p', title, {'fontFamily': HAND, 'fontSize': '1.5rem', 'fontWeight': '700', 'color': HI, 'margin': '0 0 0.9rem', 'lineHeight': '1'}),
        col(u + 'l', [flink('%sl%d' % (u, i + 1), t, h) for i, (t, h) in enumerate(links)], gap='0.7rem', extra={'alignItems': 'flex-start'}),
    ])

brand = el(P + 'brand', 'div', None, [
    tx(P + 'logo', 'a', '<strong>Pacioli</strong> Finance',
       {'fontFamily': HEAD, 'fontSize': '1.75rem', 'fontWeight': '400', 'color': BASE, 'textDecoration': 'none', 'display': 'inline-block',
        'marginBottom': '1rem', 'letterSpacing': '-0.01em'}, hattrs={'href': '/'}),
    tx(P + 'tag', 'p', 'Remote in-house accounting, payroll, and tax compliance for established businesses ' + AMP + '#8212; a full team for a fraction of the cost of one hire.',
       {'fontFamily': BODY, 'fontSize': '0.9375rem', 'lineHeight': '1.6', 'color': CREAM, 'margin': '0', 'maxWidth': '22rem'}),
])

cols = [
    brand,
    fcol(P + 'sol', 'Solutions', [('All Solutions', '/solutions/'), ('Bookkeeping', '/solutions/bookkeeping/'),
                                   ('Clean-Up Bookkeeping', '/solutions/clean-up-bookkeeping/'),
                                   ('Tax ' + AMPSEMI + ' Compliance', '/solutions/tax-compliance/'),
                                   ('Internal Audit', '/solutions/internal-audit/'), ('Payroll', '/solutions/payroll/')]),
    fcol(P + 'co', 'Company', [('About', '/about/'), ('FAQ', '/faq/'), ('Reviews', '/reviews/'), ('Contact', '/contact/')]),
    fcol(P + 'res', 'Resources', [('Resource Library', '/resources/'), ('Payroll ' + AMPSEMI + ' Tax Forms', '/resources/payroll-tax-forms/'),
                                  ('Request a Consultation', '/contact/')]),
]
grid = el(P + 'grid', 'div', {'display': 'grid', 'gridTemplateColumns': '1.4fr 1fr 1fr 1fr', 'columnGap': '3rem', 'rowGap': '2.5rem',
                              'paddingBottom': '3rem', '@media (max-width:900px)': {'gridTemplateColumns': '1fr 1fr'},
                              '@media (max-width:560px)': {'gridTemplateColumns': '1fr'}}, cols)
bar = el(P + 'bar', 'div', {'alignItems': 'center', 'borderTop': '1.5px dashed rgba(250, 246, 236, 0.28)', 'columnGap': '2rem', 'display': 'flex',
                            'flexWrap': 'wrap', 'justifyContent': 'space-between', 'paddingTop': '1.5rem', 'paddingBottom': '1.75rem', 'rowGap': '0.75rem'}, [
    tx(P + 'copy', 'p', AMP + '#169; 2026 Pacioli Finance. All rights reserved.',
       {'fontFamily': BODY, 'fontSize': '0.875rem', 'color': 'rgba(250, 246, 236, 0.6)', 'margin': '0'}),
    el(P + 'legal', 'div', {'columnGap': '1.5rem', 'display': 'flex'}, [
        tx(P + 'priv', 'a', 'Privacy Policy', {'fontFamily': BODY, 'fontSize': '0.875rem', 'color': 'rgba(250, 246, 236, 0.6)', 'textDecoration': 'none',
                                              '&:is(:hover, :focus)': {'color': HI}}, hattrs={'href': '/privacy-policy/'}),
        tx(P + 'terms', 'a', 'Terms of Use', {'fontFamily': BODY, 'fontSize': '0.875rem', 'color': 'rgba(250, 246, 236, 0.6)', 'textDecoration': 'none',
                                             '&:is(:hover, :focus)': {'color': HI}}, hattrs={'href': '/terms-of-use/'}),
    ]),
])
footer = section(P + 'sec', INK, [
    doodle(P + '_plane', 'plane', '40px', '40px', '-10', {'bottom': '14px', 'left': '48%'}, 'rgba(250, 246, 236, 0.35)'),
    grid, bar,
], pad=72)
sys.stdout.write(footer + '\n')
