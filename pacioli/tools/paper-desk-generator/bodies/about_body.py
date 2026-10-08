# =====================================================================
# ABOUT PAGE BODY -- rebuilt from the live page markup (user paste), with copy fixes.
# python3 -I build.py bodies/about_body.py > ../../about-page-paper.html
# =====================================================================
AMPSEMI = AMP + 'amp;'
LQ, RQ, AP = '“', '”', '’'

def eye(u, text, center=False, color=ACC):
    st = {'fontFamily': HAND, 'fontSize': '1.3rem', 'color': color, 'fontWeight': '700',
          'display': 'block' if center else 'inline-block', 'transform': 'rotate(-1.5deg)', 'marginBottom': '0.5rem'}
    if center:
        st['textAlign'] = 'center'
    return tx(u, 'span', text, st)

def h2c(u, text, center=False, color=INK, mb='0', mt=None):
    st = {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': 'clamp(1.75rem,3.2vw,2.25rem)', 'color': color,
          'letterSpacing': '-0.015em', 'lineHeight': '1.2', 'margin': '0'}
    if mb != '0':
        st['marginBottom'] = mb
    if center:
        st['textAlign'] = 'center'
    return tx(u, 'h2', text, st)

def p(u, text, color=MUTED, size='1.0625rem', mt='0', mb='0', mw=None, lh='1.6'):
    st = {'color': color, 'fontFamily': BODY, 'fontSize': size, 'lineHeight': lh, 'marginTop': mt, 'marginBottom': mb}
    if mw:
        st['maxWidth'] = mw
    return tx(u, 'p', text, st)

def h3(u, text, size='1.375rem', mb='0.75rem', ink=True):
    return tx(u, 'h3', text, {'color': INK, 'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': size, 'letterSpacing': '-0.01em',
                              'marginBottom': mb, 'marginTop': '0'})

def center_wrap(u, mw, kids, extra=None):
    st = {'maxWidth': mw, 'marginLeft': 'auto', 'marginRight': 'auto', 'textAlign': 'center'}
    if extra:
        st.update(extra)
    return el(u, 'div', st, kids)

def dot_item(u, html_text):
    return el(u, 'div', {'alignItems': 'flex-start', 'columnGap': '0.75rem', 'display': 'flex'}, [
        sh(u + 'dot', DOT, {'color': ACC, 'display': 'block', 'flexShrink': '0', 'marginTop': '0.5rem', 'svg': {'height': '7px', 'width': '7px'}}),
        tx(u + 'tx', 'p', html_text, {'color': MUTED, 'fontSize': '0.9375rem', 'lineHeight': '1.6', 'margin': '0'})])

def card_icon_svg(inner, vb='0 0 512 512', sw='24'):
    return ('<svg stroke-linejoin="round" stroke-linecap="round" stroke-width="%s" stroke="currentColor" fill="none" viewBox="%s" '
            'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">%s</svg>' % (sw, vb, inner))

ICON['phone'] = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path>'
ICON['calendar'] = '<rect x="3.5" y="5" width="17" height="15" rx="2"></rect><path d="M3.5 10h17M8 3v4M16 3v4"></path>'
PLANE_TRAIL = ('<svg aria-hidden="true" viewBox="0 0 64 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M2 21C12 22 16 10 27 14S42 19 49 13" stroke-width="1.3" stroke-dasharray="1.5 3.2" opacity="0.75"></path>'
    '<g transform="translate(40 0)" stroke-width="1.8"><path d="M3 11L21 3l-7 18-3-8zM11 13L21 3"></path></g></svg>')
CHECK = svg('<path d="M5 12l5 5 9-10"></path>', sw='2')

# ---------- 1. HERO (story) ----------
hero = section('abhero', SURF, [
    center_wrap('abhero_wrap', '44rem', [
        eye('abhero_eye', 'Get to Know Pacioli Finance', center=True),
        tx('abhero_h1', 'h1', 'Who Is Pacioli Finance? <strong>Outsourced Accounting, Handled Clearly and Correctly</strong>',
           {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.1rem,4.2vw,2.9rem)', 'color': INK, 'letterSpacing': '-0.02em',
            'lineHeight': '1.2', 'marginTop': '0.25rem', 'marginBottom': '1.25rem', 'textAlign': 'center'}),
        tx('abhero_p1', 'p', 'For established businesses who need controller-level oversight without building a full internal accounting department.',
           {'color': INK, 'fontFamily': BODY, 'fontSize': '1.125rem', 'lineHeight': '1.6', 'maxWidth': '38rem', 'margin': '0 auto 1rem auto'}),
        tx('abhero_p2', 'p', 'Bookkeeping, management accounting, tax support, and payroll compliance oversight ' + AMP + '#8212; from a flexible remote team, scaled to your budget.',
           {'color': MUTED, 'fontFamily': BODY, 'fontSize': '1rem', 'lineHeight': '1.6', 'maxWidth': '38rem', 'margin': '0 auto 2rem auto'}),
        btn('abhero_cta', 'Request a Consultation', '/contact/'),
    ]),
], pad=80, hattrs={'id': 'story'}, extra_bg={'paddingTop': '100px', 'borderBottom': '1.5px dashed ' + LINE})

# ---------- 2. PAIN POINTS ----------
pains = ['You' + AP + 've outgrown DIY bookkeeping, but a full-time in-house hire or a big CPA firm feels like overkill',
         'A bookkeeping mistake got discovered and now you need it cleaned up before you can trust your numbers again',
         'You' + AP + 're applying for a line of credit or loan and need clean, lender-ready books to improve your odds',
         'Your business doesn' + AP + 't need wealth management ' + AMP + '#8212; it needs someone watching the day-to-day numbers',
         'You want management-level insight, not just a bookkeeper who records history']
pain_rows = [el('abpain_i%d' % i, 'div', {'alignItems': 'flex-start', 'columnGap': '0.6rem', 'display': 'flex'}, [
    sh('abpain_i%ds' % i, CHECK, {'color': INK, 'display': 'block', 'flexShrink': '0', 'marginTop': '0.2em', 'svg': {'width': '1.1em', 'height': '1.1em'}}),
    tx('abpain_i%dt' % i, 'span', t, {'color': INK, 'fontSize': '1.0625rem', 'lineHeight': '1.5'})]) for i, t in enumerate(pains)]
TAPE = ('<svg aria-hidden="true" viewBox="0 0 64 22"><rect x="0.5" y="0.5" width="63" height="21" fill="rgba(255, 255, 255, 0.62)" stroke="rgba(34, 48, 77, 0.28)" stroke-width="1"></rect>'
        '<path d="M12 0.5v21M52 0.5v21" stroke="rgba(34, 48, 77, 0.07)" stroke-width="1"></path></svg>')
pain_card = el('abpain_card', 'div', {'backgroundColor': HI, 'border': CARD_BD, 'borderRadius': '8px', 'boxShadow': '4px 4px 0 var(--paper-ink)',
                                      'padding': '2rem 2.25rem', 'maxWidth': '40rem', 'marginLeft': 'auto', 'marginRight': 'auto', 'marginTop': '2rem',
                                      'transform': 'rotate(-0.5deg)', 'position': 'relative'}, [
    sh('abpain_tape_l', TAPE, {'display': 'inline-flex', 'position': 'absolute', 'svg': {'width': '64px', 'height': '22px'}, 'transform': 'rotate(-38deg)',
                               'pointerEvents': 'none', 'zIndex': '2', 'top': '-10px', 'left': '-18px'}),
    sh('abpain_tape_r', TAPE, {'display': 'inline-flex', 'position': 'absolute', 'svg': {'width': '64px', 'height': '22px'}, 'transform': 'rotate(38deg)',
                               'pointerEvents': 'none', 'zIndex': '2', 'top': '-10px', 'right': '-18px'}),
    col('abpain_list', pain_rows, gap='0.85rem', extra={'textAlign': 'left'}),
])
pain = section('abpain', BASE, [
    center_wrap('abpain_wrap', '40rem', [eye('abpain_eye', 'Is This You?', center=True), h2c('abpain_h2', 'Sound Familiar?', center=True)]),
    pain_card,
    center_wrap('abpain_close', '40rem', [
        tx('abpain_closetext', 'p', 'That' + AP + 's where a real accounting department ' + AMP + '#8212; without the overhead ' + AMP + '#8212; makes the difference.',
           {'color': ACC, 'fontFamily': HEAD, 'fontSize': '1.3125rem', 'fontWeight': '600', 'lineHeight': '1.4', 'marginTop': '0', 'marginBottom': '1.5rem'}),
        btn('abpain_cta', 'Request a Consultation', '/contact/'),
    ], extra={'marginTop': '2.25rem'}),
], extra_bg=DOTGRID, hattrs={'id': 'pain-points'})

# ---------- 3. APPROACH (capabilities) ----------
CAP = [
    ('Budgeting ' + AMPSEMI + ' Forecasting', 'Build realistic operating budgets and look ahead at future revenue and expenses to help you plan for growth, anticipate slow periods, and set financial goals.', '-0.6',
     '<path d="M103 94c70-9 137-8 202 1v318c-67 10-134 10-202 0V94zM129 137h149v68H129zM137 241h34v34h-34zM190 241h34v34h-34zM243 241h34v34h-34zM137 294h34v34h-34zM190 294h34v34h-34zM243 294h34v34h-34zM137 347h34v34h-34zM190 347h87"></path><path d="M353 151c58 0 105 47 105 105s-47 105-105 105-105-47-105-105M353 151v105h105M353 256l-75 74"></path><path stroke-width="14" d="M88 119l15-11M88 149l15-11M88 179l15-10"></path>'),
    ('Financial Analysis ' + AMPSEMI + ' Reporting', 'Instead of just recording history, we interpret the data, spot trends, measure product profitability, and explain where the business is making or losing money.', '0.5',
     '<path d="M78 407h356M105 382V302h58v80M197 382V246h58v136M289 382V183h58v199M381 382V119h53v263"></path><path d="M111 271l83-70 61 31 124-126M349 106h31v32"></path><path stroke-width="14" d="M70 383l14-11M70 353l14-11M70 323l14-11"></path>'),
    ('Cost Management ' + AMPSEMI + ' Control', 'Analyze fixed and variable expenses to find waste, price products correctly, and improve profit margins.', '-0.4',
     '<ellipse ry="28" rx="81" cy="329" cx="177"></ellipse><path d="M96 329v62c4 18 39 29 81 29s77-11 81-29v-62M99 360c15 17 44 25 78 25s63-8 79-25"></path><ellipse ry="23" rx="63" cy="185" cx="355"></ellipse><path d="M292 185v48c4 15 31 24 63 24s59-9 63-24v-48"></path><path d="M223 268c43-71 90-91 145-87M340 144l32 36-43 23M290 294c-42 45-89 57-139 37M171 300l-24 32 36 23"></path><path stroke-width="14" d="M82 337l14-8M82 361l14-8M84 385l14-8"></path>'),
    ('Strategic Advisory ' + AMPSEMI + ' Decision Support', 'Use these insights to decide whether to hire new staff, buy equipment, expand locations, or secure bank loans.', '0.5',
     '<circle r="48" cy="151" cx="167"></circle><path d="M84 355c9-85 41-133 83-133s75 48 84 133M130 225l37 48 37-48M167 273v83"></path><path d="M266 126c53-8 106-6 158 5v224c-52 12-105 13-158 4V126zM290 321V244M328 321V210M366 321V176M404 321V146M287 169c43-6 83-4 120 3"></path><path stroke-width="14" d="M69 296l15-11M72 325l14-10M76 353l14-10"></path>'),
]
cap_cards = []
for i, (t, d, rot, icon) in enumerate(CAP):
    u = 'abcap%d' % i
    cap_cards.append(el(u, 'div', {'backgroundColor': BASE, 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.5rem',
                                   'transform': 'rotate(%sdeg)' % rot}, [
        el(u + 'icw', 'div', {'alignItems': 'center', 'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '50%', 'display': 'flex',
                              'height': '56px', 'justifyContent': 'center', 'marginBottom': '1.125rem', 'width': '56px'}, [
            sh(u + 'ic', card_icon_svg(icon), {'color': ACC, 'display': 'inline-flex', 'svg': {'height': '1.4rem', 'width': '1.4rem'}})]),
        h3(u + 't', t, size='1.1875rem', mb='0.5rem'),
        p(u + 'd', d, size='0.9375rem', lh='1.5'),
    ]))
cap = section('abcap', SURF, [
    eye('abcap_eye', "How We're Different"),
    h2c('abcap_h2', 'Controller-Level Support At Affordable Pricing'),
    p('abcap_p1', 'Pacioli Finance sits between low-cost DIY bookkeeping and an expensive full-time in-house hire or big CPA firm: real people, real oversight, and management-level insight, billed on a flexible hourly model with a monthly minimum that scales with your needs.',
      color=MUTED, mt='1rem', mb='1rem', mw='46rem'),
    p('abcap_p2', 'This is explicitly not wealth management (a common point of confusion tied to the name) and not a CPA-only tax shop ' + AMP + '#8212; our differentiator is ongoing management accounting and controller-level support, not just historical bookkeeping.',
      color=MUTED, mb='2.5rem', mw='46rem'),
    el('abcap_grid', 'div', {'columnGap': '1.75rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(4,minmax(0,1fr))', 'rowGap': '1.75rem',
                             '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                             '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, cap_cards),
], dashed=True, hattrs={'id': 'approach'})

# ---------- 4. FREE CONSULTATION (small icon badge instead of the large image) ----------
fl = ['A conversation about where your business stands today and where it' + AP + 's headed',
      'An honest read on whether you need clean-up work, ongoing support, or both',
      'A clear recommendation ' + AMP + '#8212; no fluff, no pressure',
      'A flexible hourly plan with a monthly minimum, scoped to your budget']
free_note = el('abfree_note', 'div', {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '2rem',
                                      'transform': 'rotate(1.5deg)', 'position': 'relative', 'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
    doodle('abfree_clip', 'clip', '30px', '48px', '12', {'top': '-22px', 'right': '24px'}, ACC, hide_mobile=False),
    el('abfree_notetop', 'div', {'alignItems': 'center', 'columnGap': '0.75rem', 'display': 'flex'}, [
        badge('abfree_bd', 'calendar', size=52, icon_size='1.4rem'),
        tx('abfree_notehd', 'span', 'What you' + AP + 'll get', {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC})]),
    col('abfree_list', [dot_item('abfree_li%d' % i, t) for i, t in enumerate(fl)], gap='0.85rem'),
])
free = section('abfree', BASE, [
    el('abfree_grid', 'div', {'alignItems': 'center', 'columnGap': '4rem', 'display': 'grid', 'gridTemplateColumns': '1.2fr 1fr', 'rowGap': '2.5rem',
                              '@media (max-width:1024px)': {'gridTemplateColumns': '1fr'}}, [
        el('abfree_left', 'div', None, [
            eye('abfree_eye', 'Get Started'),
            h2c('abfree_h2', 'Start With a Free Consultation'),
            p('abfree_intro', 'This is the obvious first step, not a sales pitch ' + AMP + '#8212; a clear-eyed look at where your business and its books stand today.', mt='1rem', mb='2rem'),
            btn('abfree_cta', 'Request a Consultation', '/contact/'),
        ]),
        free_note,
    ]),
], extra_bg=DOTGRID, hattrs={'id': 'consultation'})

# ---------- 5. NAMESAKE ----------
PORTRAIT = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" aria-labelledby="t d"><title id="t">Pacioli portrait icon</title>'
            '<desc id="d">A simplified Renaissance-style portrait of Luca Pacioli in a hood.</desc>'
            '<g stroke="#22304d" stroke-width="10" stroke-linecap="round" stroke-linejoin="round">'
            '<path fill="#22304d" d="M67 438c27-46 73-64 119-78c22-7 28-22 25-45c-18-19-29-49-31-81c-3-47 6-92 37-124c24-25 64-37 96-25c38 14 60 53 62 99c1 19-1 40 1 63c4 49 27 84 70 96c-20 15-45 23-73 24c31 13 58 34 72 71H67z"></path>'
            '<path fill="#fbf6ea" d="M212 181c13-25 41-40 72-40c30 0 56 14 70 37l-3 67c-2 48-25 91-66 94c-43 3-68-40-71-91l-2-67z"></path>'
            '<path fill="none" d="M205 190c7-49 43-78 86-77c39 1 74 32 76 80M208 188c-18 17-19 45-10 65M367 189c10 29 7 63-3 90"></path>'
            '<path fill="none" d="M231 220c12-9 27-8 38 0M303 220c12-9 26-8 36 1"></path><path fill="none" d="M240 227c7 6 14 6 21 0M311 227c7 6 14 6 21 0"></path>'
            '<path fill="none" d="M286 226c-2 17-2 31-8 42c7 5 14 5 21 0M261 298c15 10 33 10 48-1"></path>'
            '<path fill="#fbf6ea" d="M212 315c15 22 40 36 72 36c31 0 56-14 72-37c3 22 14 38 31 48c-34 18-68 26-103 26c-37 0-71-9-103-27c18-10 28-25 31-46z"></path>'
            '<path fill="none" d="M181 361c32 17 67 27 103 27c36 0 70-9 103-26M217 340l-12 31M351 340l13 31"></path>'
            '<g fill="none" stroke="#fbf6ea" stroke-width="6"><path d="M336 105c-19 6-31 17-37 33M349 116c-19 7-30 18-35 31M361 130c-17 5-28 15-34 29"></path>'
            '<path d="M366 178c-13 17-18 39-17 62M369 196c-8 20-9 42-4 64M364 290c13 28 34 46 63 55"></path>'
            '<path d="M227 123c-25 17-38 43-41 77M191 270c3 20 10 36 22 49"></path><path d="M319 351c19 7 39 10 60 9M343 337c18 9 36 13 56 14"></path></g>'
            '<g fill="none" stroke="#fbf6ea" stroke-width="4"><path d="M343 167l19-12M344 180l22-14M345 194l22-14M348 209l20-13M351 224l17-11"></path>'
            '<path d="M378 291l-18 11M388 301l-20 13M399 312l-20 13M410 324l-18 12"></path><path d="M222 367l-9 12M238 371l-9 13M256 375l-8 13"></path></g></g></svg>')
nl = ['<strong>Standardized double-entry systems</strong> ' + AMP + '#8212; accurate recording of transactions, balanced books, and reliable financial statements',
      '<strong>Structured internal controls</strong> ' + AMP + '#8212; segregation of duties and formal ledgers that reduce errors and fraud, enhancing audit readiness',
      '<strong>Transparent financial reporting</strong> ' + AMP + '#8212; clear, GAAP-aligned financial statements that improve decision-making',
      '<strong>Scalable bookkeeping practices</strong> ' + AMP + '#8212; processes that scale for growing businesses, including multi-entity structures',
      '<strong>Educational foundation</strong> ' + AMP + '#8212; we help non-financial leaders understand financial results, budget variances, and cash-flow implications',
      '<strong>Documentation and audit trails</strong> ' + AMP + '#8212; thorough records that streamline internal and external audits',
      '<strong>Integration with technology</strong> ' + AMP + '#8212; timeless principles translated into scalable cloud-based accounting, automated reconciliations, and real-time reporting']
name = section('abname', SURF, [
    eye('abname_eye', 'Our Namesake'),
    el('abname_grid', 'div', {'columnGap': '4rem', 'display': 'grid', 'gridTemplateColumns': '1.4fr 1fr', 'rowGap': '2.5rem', 'marginBottom': '3rem',
                              '@media (max-width:1024px)': {'gridTemplateColumns': '1fr'}}, [
        el('abname_c1', 'div', None, [
            h2c('abname_h2', 'Inspired by Luca Pacioli, the Father of Accounting'),
            p('abname_p', 'In 1494, Luca Pacioli published a foundational section on bookkeeping in his <em>Summa de Arithmetica, Geometria, Proportioni et Proportionalita</em>, detailing the double-entry system ' + AMP + '#8212; debits, credits, ledgers, and trial balances ' + AMP + '#8212; that standardized accounting practices used by merchants and businesses across Europe. He also collaborated with Leonardo da Vinci on mathematical and accounting diagrams, illustrating the era' + AP + 's blend of art, science, and commerce. Our name honors his legacy: accuracy, structure, and financial clarity.',
              mt='1.25rem', lh='1.65'),
        ]),
        el('abname_c2', 'div', None, [
            el('abname_badge', 'div', {'alignItems': 'center', 'backgroundColor': BASE, 'border': CARD_BD, 'borderRadius': '50%', 'display': 'flex', 'height': '56px',
                                       'justifyContent': 'center', 'marginBottom': '1rem', 'width': '56px'}, [
                sh('abname_badgeic', PORTRAIT, {'color': BASE, 'display': 'inline-flex', 'svg': {'fill': 'none', 'stroke': 'currentColor', 'strokeWidth': '1.5', 'width': '1.75rem', 'height': '1.75rem'}})]),
            h3('abname_h3', 'Why ' + LQ + 'Pacioli' + RQ),
            p('abname_p2', 'We took the name because the principle still holds: every entry has two sides, and the truth shows up when they match.', size='1rem', mb='1.25rem'),
            tx('abname_quote', 'p', 'A CMA is trained for the inside of a business: reporting, controls, analysis. A CPA is trained for the outside: attestation and returns. Most owners need both, at different moments.',
               {'backgroundColor': HI, 'color': INK, 'padding': '1.25rem 1.5rem', 'borderRadius': '4px', 'border': CARD_BD, 'boxShadow': '3px 3px 0 var(--paper-ink)',
                'transform': 'rotate(0.6deg)', 'fontFamily': HEAD, 'fontSize': '1.0625rem', 'fontStyle': 'italic', 'margin': '0'}),
        ]),
    ]),
    h3('abname_h3b', 'How We Incorporate Pacioli' + AP + 's Findings to Benefit Your Business', mb='1.5rem'),
    el('abname_list', 'div', {'columnGap': '2rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '1rem',
                              '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, [dot_item('abname_li%d' % i, t) for i, t in enumerate(nl)]),
], dashed=True, hattrs={'id': 'pacioli'})

# ---------- 6. TRUST ----------
TR = [('Led by a CMA', 'Overseen by a Certified Management Accountant (CMA).', '-0.5',
       '<circle cx="12" cy="7.5" r="4"></circle><path d="M4.5 21c0-4.2 3.4-7.5 7.5-7.5"></path><path d="M14 17.5l3 3 4.5-5"></path>'),
      ('A Team of Four', 'A CMA plus a senior accountant supervising two bookkeepers/admin ' + AMP + '#8212; small enough to give every client hands-on attention.', '0.5',
       '<circle cx="8.5" cy="8" r="3"></circle><path d="M2.5 20c0-3.6 2.7-6.5 6-6.5s6 2.9 6 6.5"></path><circle cx="16.5" cy="9" r="2.3"></circle><path d="M15 13.2c2.8.5 5 3 5 6.3"></path>'),
      ('QuickBooks Certified', 'Every accountant is a QuickBooks Online Certified Pro Advisor.', '-0.4',
       '<circle cx="12" cy="8.5" r="5.5"></circle><path d="M8 13.5 6.5 21l5.5-3 5.5 3-1.5-7.5"></path>'),
      ('Priority Industries', 'Technology, legal and professional services, education (a favorite vertical), real estate, and select manufacturing.', '0.4',
       '<rect x="3.5" y="9" width="6" height="12"></rect><rect x="13.5" y="4" width="7" height="17"></rect><line x1="6" y1="12" x2="8" y2="12"></line><line x1="6" y1="15" x2="8" y2="15"></line><line x1="6" y1="18" x2="8" y2="18"></line><line x1="16" y1="7" x2="18" y2="7"></line><line x1="16" y1="10" x2="18" y2="10"></line><line x1="16" y1="13" x2="18" y2="13"></line><line x1="16" y1="16" x2="18" y2="16"></line>')]
tr_cards = []
for i, (t, d, rot, icon) in enumerate(TR):
    u = 'abtrust%d' % i
    tr_cards.append(el(u, 'div', {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.375rem',
                                  'columnGap': '1rem', 'display': 'flex', 'transform': 'rotate(%sdeg)' % rot}, [
        el(u + 'icw', 'div', {'alignItems': 'center', 'backgroundColor': BASE, 'border': CARD_BD, 'borderRadius': '50%', 'display': 'flex', 'flexShrink': '0',
                              'height': '44px', 'justifyContent': 'center', 'width': '44px'}, [
            sh(u + 'ic', card_icon_svg(icon, '0 0 24 24', '1.5'), {'color': ACC, 'display': 'inline-flex', 'svg': {'width': '1.1875rem', 'height': '1.1875rem'}})]),
        el(u + 'txt', 'div', None, [h3(u + 't', t, size='1.0625rem', mb='0.25rem'), p(u + 'd', d, size='0.9375rem', lh='1.5')]),
    ]))
trust = section('abtrust', BASE, [
    el('abtrust_head', 'div', {'maxWidth': '42rem', 'marginBottom': '2.75rem'}, [eye('abtrust_eye', 'The Track Record'), h2c('abtrust_h2', 'Why Businesses Trust Pacioli')]),
    el('abtrust_grid', 'div', {'columnGap': '2rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '1.75rem',
                               '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, tr_cards),
], extra_bg=DOTGRID, hattrs={'id': 'trust'})

# ---------- 7. PROMISE ----------
EXP = [('Clarity', 'Financial information that is organized, understandable, and useful.', '-0.5'),
       ('Accuracy', 'Accounting processes designed to maintain reliable financial records.', '0.5'),
       ('Communication', 'Real people who communicate with you and your team, not just software and reports.', '-0.4'),
       ('Accountability', 'A team that takes ownership of the accounting work within the scope of your engagement.', '0.4'),
       ('Collaboration', 'We work with you, your employees, and your other professional advisors when appropriate.', '-0.3'),
       ('Scalability', 'Services that can change as your business grows, rather than forcing your business into a fixed package.', '0.3')]
exp_cards = [el('abexp%d' % i, 'div', {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '10px', 'boxShadow': '3px 3px 0 rgba(34, 48, 77, 0.9)',
                                       'padding': '1.25rem', 'transform': 'rotate(%sdeg)' % r}, [
    sh('abexp%dic' % i, CHECK, {'color': ACC, 'display': 'inline-flex', 'marginBottom': '0.625rem', 'svg': {'width': '1.1rem', 'height': '1.1rem'}}),
    tx('abexp%dt' % i, 'h3', t, {'color': INK, 'fontSize': '1.0625rem', 'fontWeight': '700', 'marginBottom': '0.375rem', 'marginTop': '0'}),
    p('abexp%dd' % i, d, size='0.9375rem', lh='1.5')]) for i, (t, d, r) in enumerate(EXP)]
ask = ['Provide complete and accurate information', 'Give us timely access to necessary financial systems and records', 'Respond to questions and document requests',
       'Review reports and tax filings', 'Notify us of significant changes to the business', 'Maintain appropriate supporting documentation',
       'Make required tax and business payments on time']
promise = section('abpromise', SURF, [
    eye('abpromise_eye', 'Our Promise to You'),
    h2c('abpromise_h2', 'Your Business. Your Numbers. <strong>Your Accounting Department.</strong>'),
    p('abpromise_p', 'We don' + AP + 't believe you should have to build a large internal accounting department to receive professional accounting support. Our role can expand or contract as your business changes.',
      mt='1.25rem', mb='3rem', mw='46rem'),
    h3('abpromise_h3a', 'What You Can Expect From Us', mb='1.5rem'),
    el('abpromise_grid', 'div', {'columnGap': '1.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '1.5rem', 'marginBottom': '3.5rem',
                                 '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                                 '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, exp_cards),
    h3('abpromise_h3b', 'What We Ask of You'),
    p('abpromise_askintro', 'A successful accounting relationship works both ways. We ask our clients to:', size='1rem', mb='1.5rem'),
    el('abask_list', 'div', {'columnGap': '2rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '0.85rem', 'marginBottom': '2rem',
                             '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, [dot_item('abask_li%d' % i, t) for i, t in enumerate(ask)]),
    tx('abpromise_close', 'p', 'The better the information and communication we receive, the better we can support your business.',
       {'color': ACC, 'fontFamily': HEAD, 'fontSize': '1.1875rem', 'fontWeight': '600', 'lineHeight': '1.5', 'marginBottom': '0', 'marginTop': '0'}),
], dashed=True, hattrs={'id': 'promise'})

# ---------- 8. CLOSING CTA ----------
close = section('abclose', ACC, [
    sh('abclose_plane', PLANE_TRAIL, {'display': 'inline-flex', 'position': 'absolute', 'svg': {'width': '100px', 'height': '100px'}, 'transform': 'rotate(0deg)',
                                      'pointerEvents': 'none', '@media (max-width:1100px)': {'display': 'none'}, 'top': '24px', 'left': '8%', 'color': BASE}),
    sh('abclose_clip', svg('<path d="M7 3h8l4 4v14H7zM15 3v4h4M10 12h6M10 16h6"></path>'),
       {'display': 'inline-flex', 'position': 'absolute', 'svg': {'width': '40px', 'height': '58px'}, 'transform': 'rotate(16deg)', 'pointerEvents': 'none',
        '@media (max-width:1100px)': {'display': 'none'}, 'bottom': '24px', 'right': '10%', 'color': BASE}),
    doodle('abclose_star', 'star', '26px', '26px', '0', {'top': '30px', 'right': '6%'}),
    el('abclose_wrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto', 'maxWidth': '38rem', 'textAlign': 'center',
                               'position': 'relative'}, [
        eye('abclose_eye', "Let's Talk", center=True, color=BASE),
        h2c('abclose_h2', 'You don' + AP + 't necessarily need a full-time accounting department ' + AMP + '#8212; you need the right level of support, at the right time, with people who understand your business.',
            center=True, color=BASE, mb='1.75rem'),
        btn('abclose_cta', 'Request a Consultation', '/contact/', 'light'),
    ]),
])
sys.stdout.write('\n\n'.join([hero, pain, cap, free, name, trust, promise, close]) + '\n')
