# =====================================================================
# HOME PAGE BODY -- rebuilt from the live markup (user paste).
# Requests: (1) In-House Advantage icons -> orange line-icon badges, (2) paper planes get a dashed flight trail.
# python3 -I build.py bodies/home_body.py > ../../homepage-paper.html
# =====================================================================
AMPSEMI = AMP + 'amp;'
DASH = AMP + '#8212;'
LINK = lambda p: 'https://danj19.sg-host.com' + p     # links kept exactly as in the live page (see notes)

# plane + dashed trail: plane on the right of a 64x24 box, trail curving in from the lower left
PLANE_TRAIL = ('<svg viewBox="0 0 64 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               '<path d="M2 21C12 22 16 10 27 14S42 19 49 13" stroke-width="1.3" stroke-dasharray="1.5 3.2" opacity="0.75"></path>'
               '<g transform="translate(40 0)" stroke-width="1.8"><path d="M3 11L21 3l-7 18-3-8zM11 13L21 3"></path></g></svg>')
def plane_trail(u, h, rot, pos, color):
    w = round(h * 64 / 24)
    st = {'display': 'inline-flex', 'position': 'absolute', 'svg': {'width': '%dpx' % w, 'height': '%dpx' % h},
          'transform': 'rotate(%sdeg)' % rot, 'pointerEvents': 'none', '@media (max-width:1100px)': {'display': 'none'}}
    st.update(pos)
    st['color'] = color
    return sh(u, PLANE_TRAIL, st)

def eye(u, text, center=False):
    st = {'fontFamily': HAND, 'fontSize': '1.3rem', 'color': ACC, 'fontWeight': '700', 'display': 'block' if center else 'inline-block',
          'transform': 'rotate(-1.5deg)', 'marginBottom': '0.5rem'}
    if center:
        st['textAlign'] = 'center'
    return tx(u, 'span', text, st)

def h2c(u, text, center=False):
    st = {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': 'clamp(1.75rem,3.2vw,2.25rem)', 'color': INK, 'letterSpacing': '-0.015em',
          'lineHeight': '1.2', 'margin': '0'}
    if center:
        st['textAlign'] = 'center'
    return tx(u, 'h2', text, st)

def pp(u, text, size='1.0625rem', mt='0', mb='0', lh='1.6', center=False, mw=None):
    st = {'color': MUTED, 'fontFamily': BODY, 'fontSize': size, 'lineHeight': lh, 'marginBottom': mb, 'marginTop': mt}
    if center:
        st['textAlign'] = 'center'
    if mw:
        st['maxWidth'] = mw
    return tx(u, 'p', text, st)

def head(u, e, t, lead=None):
    kids = [eye(u + '_eye', e, True), h2c(u + '_h2', t, True)]
    if lead:
        kids.append(pp(u + '_lead', lead, mt='0.75rem', center=True))
    return el(u, 'div', {'textAlign': 'center', 'maxWidth': '42rem', 'marginLeft': 'auto', 'marginRight': 'auto', 'marginBottom': '2.75rem'}, kids)

def link_el(u, href, text):
    st = {'display': 'inline-flex', 'alignItems': 'center', 'columnGap': '0.5em', 'color': ACC, 'fontFamily': BODY, 'fontWeight': '600', 'fontSize': '0.9375rem',
          'textDecoration': 'none', 'svg': {'width': '1em', 'height': '1em'}, '&:is(:hover, :focus) svg': {'transform': 'translate3d(3px, 0px, 0px)'}}
    return el(u, 'a', st, [tx(u + 't', 'span', text), sh(u + 's', ARROW, {'display': 'inline-flex', 'svg': {'width': '1em', 'height': '1em'}})], hattrs={'href': href})

def white_badge(u, svg_html, size, iw, color, mb='1rem', bg='#fff', inline=False):
    st = {'alignItems': 'center', 'backgroundColor': bg, 'border': CARD_BD, 'borderRadius': '50%', 'display': 'inline-flex' if inline else 'flex',
          'height': '%dpx' % size, 'justifyContent': 'center', 'width': '%dpx' % size}
    if mb:
        st['marginBottom'] = mb
    else:
        st['flexShrink'] = '0'
    return el(u + 'w', 'div', st, [sh(u, svg_html, {'color': color, 'display': 'inline-flex', 'svg': {'width': iw, 'height': iw}})])

def line(inner, sw='1.5'):
    return svg(inner, sw=sw)

# ---------- 1. HERO ----------
chips = [('QuickBooks Certified', 'Every accountant a Pro Advisor', '1.2',
          '<circle r="5.5" cy="8.5" cx="12"></circle><path d="M8 13.5 6.5 21l5.5-3 5.5 3-1.5-7.5"></path>'),
         ('CMA-Led Team', 'A named senior accountant on every client', '-1',
          '<circle r="4" cy="7.5" cx="12"></circle><path d="M4.5 21c0-4.2 3.4-7.5 7.5-7.5"></path><path d="M14 17.5l3 3 4.5-5"></path>'),
         ('Flexible Hourly Pricing', 'No unnecessary packages', '0.6',
          '<circle r="9" cy="12" cx="12"></circle><path d="M12 7v10M15 9.5c-.5-1-1.7-1.5-3-1.5-1.6 0-3 .8-3 2s1.4 1.7 3 2 3 .8 3 2-1.4 2-3 2c-1.3 0-2.5-.5-3-1.5"></path>')]
chip_els = []
for i, (t, d, rot, ico) in enumerate(chips):
    u = 'phchip%d' % i
    chip_els.append(el(u, 'div', {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.1rem 1.25rem', 'display': 'flex',
                                  'alignItems': 'center', 'columnGap': '0.9rem', 'transform': 'rotate(%sdeg)' % rot}, [
        el(u + 'icw', 'div', {'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'width': '42px', 'height': '42px', 'flexShrink': '0'}, [
            sh(u + 'ic', line(ico), {'display': 'inline-flex', 'color': ACC, 'svg': {'width': '1.5rem', 'height': '1.5rem'}})]),
        el(u + 'txt', 'div', None, [tx(u + 't', 'p', t, {'margin': '0', 'fontWeight': '700', 'fontSize': '0.9375rem', 'color': INK, 'fontFamily': BODY}),
                                    tx(u + 'd', 'p', d, {'margin': '0', 'marginTop': '2px', 'fontSize': '0.8125rem', 'color': MUTED})])]))
hero = section('phhero', BASE, [
    plane_trail('phhero_plane', 84, 10, {'top': '-28px', 'right': '4%'}, ACC),
    el('phhero_grid', 'div', {'display': 'grid', 'gridTemplateColumns': '1.3fr 1fr', 'columnGap': '3.5rem', 'rowGap': '2.5rem', 'alignItems': 'center',
                              '@media (max-width:1024px)': {'gridTemplateColumns': '1fr'}}, [
        el('phhero_left', 'div', None, [
            eye('phhero_eye', 'Remote in-house accounting solutions'),
            tx('phhero_h1', 'h1', '<em>Controller-Level</em> Support at Affordable Pricing',
               {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK, 'letterSpacing': '-0.02em', 'lineHeight': '1.15',
                'marginTop': '0.25rem', 'marginBottom': '1.25rem'}, extra_css=hi_css('phhero_h1')),
            tx('phhero_lead', 'p', 'The leading remote in-house accounting solutions provider with access to department-level services. We help small businesses get real bookkeeping, management accounting, tax support, and payroll compliance oversight ' + DASH + ' without building a full internal finance team.',
               {'color': MUTED, 'fontFamily': BODY, 'fontSize': '1.125rem', 'lineHeight': '1.6', 'marginTop': '0', 'marginBottom': '2rem', 'maxWidth': '34rem'}),
            btn('phhero_cta', 'Request a Consultation', LINK('/contact/')),
            tx('phhero_note', 'p', 'Flexible hourly pricing ' + DASH + ' no unnecessary packages.',
               {'color': MUTED, 'fontFamily': BODY, 'fontSize': '0.875rem', 'marginTop': '0.75rem', 'marginBottom': '0'}),
        ]),
        el('phhero_right', 'div', {'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, chip_els),
    ]),
], pad=80, extra_bg=dict(DOTGRID, paddingTop='110px'))

# ---------- 2. WHO YOU'RE HIRING ----------
who = section('phwho', SURF, [
    el('phwho_split', 'div', {'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'columnGap': '4rem', 'alignItems': 'start',
                              '@media (max-width:900px)': {'gridTemplateColumns': '1fr', 'rowGap': '1.5rem'}}, [
        el('phwho_c1', 'div', None, [eye('phwho_eye', "Who You're Actually Hiring"),
                                      h2c('phwho_h2', 'A CMA-led team, a named senior accountant, and people who actually answer the phone.')]),
        el('phwho_c2', 'div', {'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
            pp('phwho_p1', 'With Pacioli Finance, you get a full, hands-on team.'),
            pp('phwho_p2', 'The whole team is built around management accounting: the reporting, controls, and analysis that run a business day to day.'),
            tx('phwho_link', 'a', "More about the firm and the friar it's named for",
               {'display': 'inline-flex', 'alignItems': 'center', 'backgroundColor': 'transparent', 'color': INK, 'fontFamily': BODY, 'fontWeight': '600', 'fontSize': '0.9375rem',
                'textDecoration': 'none', 'paddingTop': '0.6rem', 'paddingBottom': '0.6rem', 'paddingLeft': '1rem', 'paddingRight': '1rem', 'borderRadius': '8px',
                'border': '2px solid var(--paper-ink)', 'width': 'max-content', '&:is(:hover, :focus)': {'backgroundColor': INK, 'color': BASE}},
               hattrs={'href': LINK('/about/')}),
        ]),
    ]),
], dashed=True, hattrs={'id': 'about'})

# ---------- 3. IN-HOUSE ADVANTAGE (orange line-icon badges, replacing the cross-hatch images) ----------
ADV = [('Full Support', 'Peace of mind with year-round support and proactive check-ins.', '-0.6',
        '<circle cx="8.5" cy="8" r="3"></circle><path d="M2.5 20c0-3.6 2.7-6.5 6-6.5s6 2.9 6 6.5"></path><circle cx="16.5" cy="9" r="2.3"></circle><path d="M15 13.2c2.8.5 5 3 5 6.3"></path>'),
       ('Productivity', 'Maintain full control of the work being done without expanding office space.', '0.6',
        '<path d="M3 17l6-6 4 4 8-8"></path><path d="M15 7h6v6"></path>'),
       ('Compliance', 'Keep your business compliant with the IRS for federal forms and audits.', '-0.4',
        '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"></path><path d="M9 12l2 2 4-4"></path>'),
       ('Savings', 'Reduce hiring, operating, and labor costs versus building an in-house team.', '0.5',
        '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v10M15 9.5c-.5-1-1.7-1.5-3-1.5-1.6 0-3 .8-3 2s1.4 1.7 3 2 3 .8 3 2-1.4 2-3 2c-1.3 0-2.5-.5-3-1.5"></path>')]
adv_cards = []
for i, (t, d, rot, ico) in enumerate(ADV):
    u = 'phadv%d' % i
    adv_cards.append(el(u, 'div', {'backgroundColor': BASE, 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.625rem', 'transform': 'rotate(%sdeg)' % rot}, [
        white_badge(u + 'ic', line(ico), 60, '1.7rem', ACC, mb='1.125rem'),
        tx(u + 't', 'h3', t, {'color': INK, 'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.25rem', 'letterSpacing': '-0.01em', 'marginBottom': '0.5rem', 'marginTop': '0'}),
        pp(u + 'd', d, size='0.9375rem', lh='1.55')]))
adv = section('phadv', SURF, [
    doodle('phadv_receipt', 'receipt', '26px', '40px', '-12', {'top': '14px', 'right': '6%'}, ACC),
    head('phadv_head', 'The In-House Advantage', 'Cost-Effective In-House Support, Custom-Fit to You', 'Enjoy streamlined workflows, processes, and internal controls you thought were only for big business.'),
    el('phadv_grid', 'div', {'display': 'grid', 'gridTemplateColumns': 'repeat(4,minmax(0,1fr))', 'columnGap': '1.75rem', 'rowGap': '1.75rem',
                             '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                             '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, adv_cards),
], dashed=True, hattrs={'id': 'why-us'})

# ---------- 4. SOLUTIONS ----------
CALC = ('<rect rx="2" height="20" width="14" y="2" x="5"></rect><rect rx="0.5" height="4" width="9" y="4.5" x="7.5"></rect>' +
        ''.join('<circle stroke="none" fill="currentColor" r="0.6" cy="%s" cx="%s"></circle>' % (y, x) for y in ('13', '16.5', '20') for x in ('8', '12', '16')))
feat = el('phsol_feat', 'div', {'alignItems': 'center', 'backgroundColor': HI, 'border': CARD_BD, 'borderRadius': '8px', 'boxShadow': '4px 4px 0 var(--paper-ink)', 'columnGap': '1.5rem',
                                'display': 'grid', 'gridTemplateColumns': 'auto 1fr auto', 'marginBottom': '1.75rem', 'padding': '1.75rem 2rem', 'transform': 'rotate(-0.4deg)',
                                '@media (max-width:767px)': {'gridTemplateColumns': '1fr', 'rowGap': '1.25rem', 'textAlign': 'left'}}, [
    white_badge('phsol_feat_ic', line('<rect rx="1.5" height="18" width="16" y="3" x="4"></rect><line y2="21" x2="12" y1="3" x1="12"></line><line y2="8" x2="10" y1="8" x1="7"></line><line y2="8" x2="17" y1="8" x1="14"></line><line y2="12" x2="10" y1="12" x1="7"></line><line y2="12" x2="17" y1="12" x1="14"></line><line y2="16" x2="10" y1="16" x1="7"></line><line y2="16" x2="17" y1="16" x1="14"></line>'), 64, '1.625rem', INK, mb=None),
    el('phsol_feat_txt', 'div', None, [
        tx('phsol_feat_tag', 'p', 'Featured', {'color': INK, 'fontSize': '0.8125rem', 'fontWeight': '700', 'letterSpacing': '0.06em', 'marginBottom': '0.375rem', 'marginTop': '0', 'textTransform': 'uppercase', 'opacity': '0.75'}),
        tx('phsol_feat_h3', 'h3', 'Bookkeeping', {'color': INK, 'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.375rem', 'letterSpacing': '-0.01em', 'marginBottom': '0.25rem', 'marginTop': '0'}),
        tx('phsol_feat_p', 'p', 'Professional Bookkeeping ' + AMPSEMI + ' Financial Operations', {'color': INK, 'fontSize': '0.9375rem', 'marginBottom': '0', 'marginTop': '0', 'opacity': '0.85'})]),
    el('phsol_feat_link', 'a', {'alignItems': 'center', 'backgroundColor': INK, 'border': '2px solid var(--paper-ink)', 'borderRadius': '8px', 'color': BASE, 'columnGap': '0.5em',
                                'display': 'inline-flex', 'fontSize': '0.9375rem', 'fontWeight': '600', 'padding': '0.625rem 1rem', 'whiteSpace': 'nowrap',
                                '&:is(:hover, :focus)': {'transform': 'translate(-1px, -1px)', 'boxShadow': '3px 3px 0 var(--paper-ink)'}},
       [tx('phsol_feat_link_t', 'span', 'Learn more'), sh('phsol_feat_link_s', ARROW, {'display': 'inline-flex', 'svg': {'width': '1em', 'height': '1em'}})],
       hattrs={'href': '/solutions/bookkeeping/'}),
])
CLEAN = '<svg aria-hidden="true" fill="currentColor" viewBox="0 0 448 512"><path d="M448 360V24c0-13.3-10.7-24-24-24H96C43 0 0 43 0 96v320c0 53 43 96 96 96h328c13.3 0 24-10.7 24-24v-16c0-7.5-3.5-14.3-8.9-18.7-4.2-15.4-4.2-59.3 0-74.7 5.4-4.3 8.9-11.1 8.9-18.6zM128 134c0-3.3 2.7-6 6-6h212c3.3 0 6 2.7 6 6v20c0 3.3-2.7 6-6 6H134c-3.3 0-6-2.7-6-6v-20zm0 64c0-3.3 2.7-6 6-6h212c3.3 0 6 2.7 6 6v20c0 3.3-2.7 6-6 6H134c-3.3 0-6-2.7-6-6v-20zm253.4 250H96c-17.7 0-32-14.3-32-32 0-17.6 14.4-32 32-32h285.4c-1.9 17.1-1.9 46.9 0 64z"></path></svg>'
SOL = [('Clean-Up Bookkeeping', 'Transform Messy Ledgers into Audit-Ready Financials', '/solutions/clean-up-bookkeeping/', CLEAN, '1.1rem', '0.5'),
       ('Tax ' + AMPSEMI + ' Compliance', 'Federal, State, and Local Tax Services', '/solutions/tax-compliance/',
        line('<path d="M7 2h7l4 4v16H7z"></path><polyline points="14 2 14 6 18 6"></polyline><line y2="18" x2="14.5" y1="13" x1="9.5"></line><circle r="0.8" cy="13" cx="10"></circle><circle r="0.8" cy="17" cx="14"></circle>'), '1.25rem', '-0.4'),
       ('Internal Audit', 'Risk, Controls ' + AMPSEMI + ' Governance for Your Business', '/solutions/internal-audit/',
        line('<circle r="6.5" cy="10.5" cx="10.5"></circle><line y2="21" x2="21" y1="15.5" x1="15.5"></line>'), '1.25rem', '0.4'),
       ('Payroll', 'Your In-House Payroll Department, Fully Outsourced', '/solutions/payroll/',
        line('<path d="M3 7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v1H3z"></path><rect rx="2" height="12" width="18" y="8" x="3"></rect><circle r="1.5" cy="14" cx="16.5"></circle>'), '1.25rem', '-0.3')]
sol_cards = []
for i, (t, d, href, ico, iw, rot) in enumerate(SOL, 1):
    u = 'phsol%d' % i
    sol_cards.append(el(u, 'div', {'backgroundColor': BASE, 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.625rem', 'transform': 'rotate(%sdeg)' % rot}, [
        white_badge(u + 'ic', ico, 48, iw, ACC, inline=True),
        tx(u + 't', 'h3', t, {'color': INK, 'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3125rem', 'letterSpacing': '-0.01em', 'marginBottom': '0.25rem', 'marginTop': '0'}),
        pp(u + 'd', d, size='0.9375rem', mb='1rem', lh='1.5'), link_el(u + 'link', href, 'Learn more')]))
sol = section('phsol', BASE, [
    doodle('phsol_calc', 'calc', '28px', '28px', '-8', {'bottom': '16px', 'left': '4%'}, ACC) if 'calc' in ICON else '',
    head('phsol_head', 'Full-Service Coverage', 'Explore Our Solutions'),
    feat,
    el('phsol_grid', 'div', {'columnGap': '1.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '1.5rem',
                             '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, sol_cards),
], extra_bg=GRIDPAPER, hattrs={'id': 'solutions'})

# ---------- 5. TRUST ----------
TR = [('QuickBooks Certified', 'Every Pacioli accountant is a QuickBooks Online Certified Pro Advisor.', '-0.5', '<circle r="5.5" cy="8.5" cx="12"></circle><path d="M8 13.5 6.5 21l5.5-3 5.5 3-1.5-7.5"></path>'),
      ('CMA-Led Team', 'Led by a CMA (Certified Management Accountant), with a senior accountant supervising a team of bookkeepers and admin.', '0.5',
       '<circle r="4" cy="7.5" cx="12"></circle><path d="M4.5 21c0-4.2 3.4-7.5 7.5-7.5"></path><path d="M14 17.5l3 3 4.5-5"></path>'),
      ('A Small, Hands-On Team', 'Gives every client close attention while still handling controller-level work.', '-0.4',
       '<circle r="3" cy="8" cx="8.5"></circle><path d="M2.5 20c0-3.6 2.7-6.5 6-6.5s6 2.9 6 6.5"></path><circle r="2.3" cy="9" cx="16.5"></circle><path d="M15 13.2c2.8.5 5 3 5 6.3"></path>'),
      ('Priority Industries', 'Technology, legal and professional services, education, real estate, and non-profits.', '0.4',
       '<rect height="12" width="6" y="9" x="3.5"></rect><rect height="17" width="7" y="4" x="13.5"></rect><line y2="12" x2="8" y1="12" x1="6"></line><line y2="15" x2="8" y1="15" x1="6"></line><line y2="18" x2="8" y1="18" x1="6"></line><line y2="7" x2="18" y1="7" x1="16"></line><line y2="10" x2="18" y1="10" x1="16"></line><line y2="13" x2="18" y1="13" x1="16"></line><line y2="16" x2="18" y1="16" x1="16"></line>')]
tr_cards = []
for i, (t, d, rot, ico) in enumerate(TR):
    u = 'phtrust%d' % i
    tr_cards.append(el(u, 'div', {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.375rem', 'columnGap': '1rem', 'display': 'flex',
                                  'transform': 'rotate(%sdeg)' % rot}, [
        white_badge(u + 'ic', line(ico), 44, '1.1875rem', ACC, mb=None, bg=BASE),
        el(u + 'txt', 'div', None, [tx(u + 't', 'h3', t, {'color': INK, 'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.0625rem', 'marginBottom': '0.25rem', 'marginTop': '0'}),
                                    pp(u + 'd', d, size='0.9375rem', lh='1.5')])]))
trust = section('phtrust', SURF, [
    doodle('phtrust_ledger', 'ledger', '24px', '36px', '-10', {'top': '14px', 'right': '6%'}, INK),
    head('phtrust_head', 'The Track Record', 'Why Businesses Trust Pacioli'),
    el('phtrust_grid', 'div', {'columnGap': '2rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '1.75rem',
                               '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, tr_cards),
], dashed=True)

# ---------- 6. INSIGHTS (query loop) ----------
loop_item = blk('generateblocks/loop-item', {'uniqueId': uid('phins_item'), 'tagName': 'div',
                'styles': {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'overflow': 'hidden'},
                'css': '.gb-loop-item-phins_item{background-color:#fff;border:1.5px solid var(--paper-ink);border-radius:12px;box-shadow:4px 4px 0 rgba(34, 48, 77, 0.9);overflow:hidden}'},
                '<div class="gb-loop-item gb-loop-item-phins_item">', '\n\n'.join([
    blk('generateblocks/media', {'uniqueId': uid('phins_img'), 'tagName': 'img',
                                 'styles': {'height': 'auto', 'maxWidth': '100%', 'objectFit': 'cover', 'width': '100%', 'aspectRatio': '16 / 10'},
                                 'css': '.gb-media-phins_img{aspect-ratio:16/10;height:auto;max-width:100%;object-fit:cover;width:100%}',
                                 'htmlAttributes': {'src': '{{featured_image key:url|size:medium_large}}'}},
        '<img class="gb-media-phins_img" src="{{featured_image key:url|size:medium_large}}"/>', '', ''),
    el('phins_body', 'div', {'padding': '1.25rem'}, [
        tx('phins_title', 'h3', '{{post_title}}', {'fontFamily': HEAD, 'fontSize': '1.125rem', 'fontWeight': '600', 'color': INK, 'margin': '0 0 0.75rem'}),
        link_el('phins_link', '{{post_permalink}}', 'View Article')])]), '</div>')
looper = blk('generateblocks/looper', {'uniqueId': uid('phins_looper'), 'tagName': 'div',
             'styles': {'display': 'grid', 'gridTemplateColumns': 'repeat(3, minmax(0, 1fr))', 'columnGap': '2rem', 'rowGap': '2rem', '@media (max-width:1024px)': {'gridTemplateColumns': '1fr'}},
             'css': '.gb-looper-phins_looper{column-gap:2rem;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));row-gap:2rem}@media (max-width:1024px){.gb-looper-phins_looper{grid-template-columns:1fr}}'},
             '<div class="gb-looper-phins_looper">', loop_item, '</div>')
query = blk('generateblocks/query', {'uniqueId': uid('phins_query'), 'tagName': 'div', 'query': {'post_type': ['post'], 'posts_per_page': '3'}}, '<div>', looper, '</div>')
ins = section('phins', SURF, [
    doodle('phins_coffee', 'coffee', '28px', '28px', '10', {'top': '14px', 'right': '6%'}, ACC),
    head('phins_head', 'Practical Guidance for Running the Numbers Well', 'From Pacioli Insights'),
    query,
], dashed=True)

sys.stdout.write('\n\n'.join([x for x in [hero, who, adv, sol, trust, '<!-- wp:block {"ref":51469} /-->', ins, '<!-- wp:block {"ref":51507} /-->']]) + '\n')
