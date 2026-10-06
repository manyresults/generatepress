# =====================================================================
# SOLUTIONS PAGE BODY -- rebuilt from the live page markup (user paste), with copy fixes.
# python3 -I build.py bodies/solutions_body.py > ../../solutions-page-paper.html
# =====================================================================
AMPSEMI = AMP + 'amp;'
AP, DASH = AMP + '#8217;', AMP + '#8212;'

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

def head(u, eyebrow_text, title):
    return el(u, 'div', {'textAlign': 'center', 'maxWidth': '42rem', 'marginLeft': 'auto', 'marginRight': 'auto', 'marginBottom': '2.75rem'},
              [eye(u + '_eye', eyebrow_text, True), h2c(u + '_h2', title, True)])

def pp(u, text, size='1.0625rem', mt='0', mb='0', mw=None):
    st = {'color': MUTED, 'fontSize': size, 'lineHeight': '1.6', 'marginBottom': mb, 'marginTop': mt}
    if mw:
        st['maxWidth'] = mw
    return tx(u, 'p', text, st)

def link_el(u, href, text, style_extra=None, btn=False):
    st = {'display': 'inline-flex', 'alignItems': 'center', 'columnGap': '0.5em', 'color': ACC, 'fontFamily': BODY, 'fontWeight': '600',
          'fontSize': '0.9375rem', 'textDecoration': 'none', 'svg': {'width': '1em', 'height': '1em'},
          '&:is(:hover, :focus) svg': {'transform': 'translate3d(3px, 0px, 0px)'}}
    return el(u, 'a', st, [tx(u + 't', 'span', text), sh(u + 's', ARROW, {'display': 'inline-flex', 'svg': {'width': '1em', 'height': '1em'}})],
              hattrs={'href': href})

def icon_badge(u, svg_html, size=48, iw='1.25rem', bg=HI, mb='1rem', inline=True):
    st = {'alignItems': 'center', 'backgroundColor': bg, 'border': CARD_BD, 'borderRadius': '50%', 'display': 'inline-flex' if inline else 'flex',
          'height': '%dpx' % size, 'justifyContent': 'center', 'width': '%dpx' % size}
    if mb:
        st['marginBottom'] = mb
    if not inline:
        st['flexShrink'] = '0'
    return el(u + 'w', 'div', st, [sh(u, svg_html, {'color': INK, 'display': 'inline-flex', 'svg': {'width': iw, 'height': iw}})])

def s24(inner, sw='1.5'):
    return svg(inner, sw=sw)

# ---------- 1. HERO ----------
hero = section('solhero', BASE, [
    doodle('solhero_bc', 'briefcase', '48px', '48px', '-8', {'top': '-6px', 'right': '10%'}, ACC),
    doodle('solhero_plane', 'plane', '52px', '52px', '10', {'bottom': '-6px', 'left': '10%'}, INK),
    doodle('solhero_star', 'star', '24px', '24px', '0', {'right': '6%', 'bottom': '10px'}),
    el('solhero_wrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto', 'maxWidth': '44rem', 'textAlign': 'center'}, [
        eye('solhero_eye', 'Remote In-House Accounting Solutions', True),
        tx('solhero_h1', 'h1', 'Solutions', {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
                                             'letterSpacing': '-0.02em', 'lineHeight': '1.1', 'marginTop': '0.25rem', 'marginBottom': '1.25rem', 'textAlign': 'center'}),
        tx('solhero_lead', 'p', 'Pacioli Finance delivers controller-level support at affordable pricing ' + DASH + ' a flexible, outsourced accounting department for established businesses that have outgrown DIY bookkeeping but aren' + AP + 't ready to build a full internal finance team. We combine accuracy, compliance, and strategic insight across four core solution areas, plus a dedicated clean-up track for businesses starting from messy books.',
           {'color': MUTED, 'fontFamily': BODY, 'fontSize': '1.125rem', 'lineHeight': '1.6', 'marginTop': '0', 'marginBottom': '2rem', 'maxWidth': '38rem', 'textAlign': 'center'}),
        btn('solhero_cta', 'Request a Consultation', '/contact/'),
        tx('solhero_note', 'p', 'Flexible hourly pricing ' + DASH + ' no unnecessary packages.',
           {'color': MUTED, 'fontFamily': BODY, 'fontSize': '0.875rem', 'marginTop': '0.75rem', 'marginBottom': '0', 'textAlign': 'center'}),
    ]),
], pad=80, extra_bg=dict(DOTGRID, paddingTop='100px'))

# ---------- 2. ABOUT SPLIT ----------
about = section('solabt', SURF, [
    doodle('solabt_pencil', 'pencil', '26px', '38px', '16', {'bottom': '24px', 'left': '10%'}, ACC),
    el('solabt_split', 'div', {'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'columnGap': '4rem', 'alignItems': 'start',
                               '@media (max-width:900px)': {'gridTemplateColumns': '1fr', 'rowGap': '1.5rem'}}, [
        el('solabt_c1', 'div', None, [eye('solabt_eye', 'Your business. Your numbers. Your accounting department.'),
                                      h2c('solabt_h2', 'What Accounting Solutions Does Pacioli Finance Offer?')]),
        el('solabt_c2', 'div', {'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
            tx('solabt_p1', 'p', 'Pacioli Finance offers four core solutions ' + DASH + ' Bookkeeping, Payroll, Tax ' + AMPSEMI + ' Compliance, and Internal Audit ' + DASH + ' plus Clean-Up Bookkeeping for businesses that need their historical books corrected before ongoing support begins. Every engagement is billed on a flexible hourly model with a monthly minimum that scales with your needs, so you only pay for the support your business actually requires.',
               {'color': MUTED, 'fontSize': '1.0625rem', 'lineHeight': '1.6', 'margin': '0'}),
            tx('solabt_p2', 'p', 'We serve established businesses nationwide, with priority focus on technology, legal and professional services, education, real estate, and select manufacturing companies. This is not wealth management and not a CPA-only tax shop ' + DASH + ' Pacioli' + AP + 's differentiator is ongoing management accounting and controller-level oversight, not just historical bookkeeping.',
               {'color': MUTED, 'fontSize': '1.0625rem', 'lineHeight': '1.6', 'margin': '0'}),
        ]),
    ]),
], dashed=True, hattrs={'id': 'about'})

# ---------- 3. SOLUTIONS GRID ----------
ICO_WALLET = s24('<path d="M3 7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v1H3z"></path><rect x="3" y="8" width="18" height="12" rx="2"></rect><circle cx="16.5" cy="14" r="1.5"></circle>')
ICO_TAX = s24('<path d="M7 2h7l4 4v16H7z"></path><polyline points="14 2 14 6 18 6"></polyline><line x1="9.5" y1="13" x2="14.5" y2="18"></line><circle cx="10" cy="13" r="0.8"></circle><circle cx="14" cy="17" r="0.8"></circle>')
ICO_AUDIT = s24('<circle cx="10.5" cy="10.5" r="6.5"></circle><line x1="15.5" y1="15.5" x2="21" y2="21"></line>')
ICO_BOOK = s24('<path d="M3 7a2 2 0 0 1 2-2h12v16H6a2 2 0 0 0-2 2zM4 19V5M8 7h6"></path>')
ICO_CLEAN = ('<svg viewBox="0 0 448 512" fill="currentColor" aria-hidden="true"><path d="M448 360V24c0-13.3-10.7-24-24-24H96C43 0 0 43 0 96v320c0 53 43 96 96 96h328c13.3 0 24-10.7 24-24v-16c0-7.5-3.5-14.3-8.9-18.7-4.2-15.4-4.2-59.3 0-74.7 5.4-4.3 8.9-11.1 8.9-18.6zM128 134c0-3.3 2.7-6 6-6h212c3.3 0 6 2.7 6 6v20c0 3.3-2.7 6-6 6H134c-3.3 0-6-2.7-6-6v-20zm0 64c0-3.3 2.7-6 6-6h212c3.3 0 6 2.7 6 6v20c0 3.3-2.7 6-6 6H134c-3.3 0-6-2.7-6-6v-20zm253.4 250H96c-17.7 0-32-14.3-32-32 0-17.6 14.4-32 32-32h285.4c-1.9 17.1-1.9 46.9 0 64z"></path></svg>')
SOL = [('Payroll', 'Your In-House Payroll Department, Fully Outsourced', '/solutions/payroll/', ICO_WALLET, '-0.5'),
       ('Tax ' + AMPSEMI + ' Compliance', 'Federal, State, and Local Tax Services', '/solutions/tax-compliance/', ICO_TAX, '0.5'),
       ('Internal Audit', 'Risk, Controls ' + AMPSEMI + ' Governance for Your Business', '/solutions/internal-audit/', ICO_AUDIT, '-0.4'),
       ('Bookkeeping', 'Professional Bookkeeping ' + AMPSEMI + ' Financial Operations', '/solutions/bookkeeping/', ICO_BOOK, '0.4')]
sol_cards = []
for i, (t, d, href, ico, rot) in enumerate(SOL):
    u = 'solg%d' % i
    sol_cards.append(el(u, 'div', {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.625rem',
                                   'transform': 'rotate(%sdeg)' % rot}, [
        icon_badge(u + 'ic', ico), tx(u + 't', 'h3', t, {'color': INK, 'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3125rem', 'letterSpacing': '-0.01em', 'marginBottom': '0.25rem', 'marginTop': '0'}),
        pp(u + 'd', d, size='0.9375rem', mb='1rem'), link_el(u + 'link', href, 'Learn more')]))
cleanup = el('solg4', 'div', {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.75rem 2rem', 'marginTop': '0', 'gridColumn': '1 / -1',
                              'alignItems': 'center', 'columnGap': '1.5rem', 'display': 'grid', 'gridTemplateColumns': 'auto 1fr auto', 'transform': 'rotate(-0.3deg)',
                              '@media (max-width:767px)': {'gridTemplateColumns': '1fr', 'rowGap': '1.25rem', 'textAlign': 'left'}}, [
    icon_badge('solg4ic', ICO_CLEAN, size=56, iw='1.375rem', mb=None, inline=False),
    el('solg4txt', 'div', None, [tx('solg4t', 'h3', 'Clean-Up Bookkeeping', {'color': INK, 'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3125rem', 'letterSpacing': '-0.01em', 'marginBottom': '0.25rem', 'marginTop': '0'}),
                                 pp('solg4d', 'Transform Messy Ledgers into Audit-Ready Financials', size='0.9375rem')]),
    el('solg4lw', 'a', {'alignItems': 'center', 'backgroundColor': INK, 'border': '2px solid var(--paper-ink)', 'borderRadius': '8px', 'color': BASE, 'columnGap': '0.5em',
                        'display': 'inline-flex', 'fontSize': '0.9375rem', 'fontWeight': '600', 'padding': '0.625rem 1rem', 'whiteSpace': 'nowrap',
                        '&:is(:hover, :focus)': {'transform': 'translate(-1px, -1px)', 'boxShadow': '3px 3px 0 var(--paper-ink)'}},
       [tx('solg4lwt', 'span', 'Learn more'), sh('solg4lws', ARROW, {'display': 'inline-flex', 'svg': {'width': '1em', 'height': '1em'}})],
       hattrs={'href': '/solutions/clean-up-bookkeeping/'}),
])
grid = section('solgrid', BASE, [
    doodle('solgrid_clip', 'clip', '38px', '54px', '14', {'top': '24px', 'right': '4%'}, INK),
    head('solgrid_head', 'Full-Service Coverage', 'Explore Our Solutions'),
    el('solgrid_grid', 'div', {'columnGap': '1.5rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '1.5rem',
                               '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, sol_cards + [cleanup]),
], extra_bg=GRIDPAPER, hattrs={'id': 'solutions'})

# ---------- 4. PROMISE ----------
PR = [('Clarity', 'Financial information that is organized, understandable, and useful.'),
      ('Accuracy', 'Accounting processes designed to maintain reliable financial records.'),
      ('Communication', 'Real people who communicate with you and your team, not just software and reports.'),
      ('Accountability', 'A team that takes ownership of the accounting work within the scope of your engagement.'),
      ('Collaboration', 'We work with you, your employees, and your other professional advisors when appropriate.'),
      ('Scalability', 'Services that can change as your business grows, rather than forcing your business into a fixed package.')]
prom_cells = [el('solprom%d' % i, 'div', None, [
    tx('solprom%dt' % i, 'h3', t, {'color': ACC, 'fontSize': '1.0625rem', 'fontWeight': '700', 'marginBottom': '0.375rem', 'marginTop': '0'}),
    pp('solprom%dd' % i, d, size='0.9375rem')]) for i, (t, d) in enumerate(PR)]
prom = section('solprom', SURF, [
    doodle('solprom_star', 'star', '24px', '24px', '0', {'top': '24px', 'right': '6%'}),
    eye('solprom_tag', 'Our Promise to You'),
    h2c('solprom_h2', 'Why Choose Pacioli Finance?'),
    pp('solprom_lead', 'Across every solution area, clients can expect:', mt='1.25rem', mb='3rem', mw='46rem'),
    el('solprom_grid', 'div', {'columnGap': '2rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '1.75rem', 'marginBottom': '3.5rem',
                               '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                               '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, prom_cells),
    tx('solprom_close', 'p', 'Industries we serve: Non-Profit, Education, Real Estate, Technology, Legal, Professional Services, and select light-manufacturing businesses.',
       {'color': ACC, 'fontFamily': HEAD, 'fontSize': '1.125rem', 'fontWeight': '600', 'lineHeight': '1.5', 'marginBottom': '0', 'marginTop': '0'}),
], dashed=True, hattrs={'id': 'promise'})

# ---------- 5. FAQ (custom accordion, no badge) ----------
FAQ = [('Does Pacioli Finance offer bundled pricing or fixed packages?', 'No. Pacioli uses a flexible hourly model with a monthly minimum that scales with your needs ' + DASH + ' no unnecessary packages, no surprises.'),
       ('Is Pacioli Finance a wealth management or investment firm?', 'No. Despite the name, Pacioli Finance is not wealth management and not a CPA-only tax shop ' + DASH + ' we provide ongoing management accounting and controller-level support.'),
       ('Can Pacioli Finance help if my books are already a mess?', 'Yes. Clean-Up Bookkeeping is designed exactly for this ' + DASH + ' see that page for our process, deliverables, and typical 4' + AMP + '#8211;8 week timeline.'),
       ('Does Pacioli Finance support multi-state businesses?', 'Yes. Our Payroll and Tax ' + AMPSEMI + ' Compliance teams handle multi-state payroll tax filings, nexus analysis, and state/local registrations across the United States.'),
       ('What accounting software does Pacioli Finance use?', 'Pacioli leverages QuickBooks Online to deliver bookkeeping, financial analysis, and budgeting tailored to your business.')]
def faq_item(n, q, a):
    p_ = 'faq%d' % n
    item_st = {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '10px', 'boxShadow': CARD_SH, 'marginBottom': '1rem'}
    item_a = {'uniqueId': uid(p_ + 'item'), 'tagName': 'div', 'styles': item_st, 'css': make_css('gb-accordion__item-' + p_ + 'item', item_st)}
    tog_st = {'alignItems': 'center', 'color': INK, 'columnGap': '1rem', 'cursor': 'pointer', 'display': 'flex', 'justifyContent': 'space-between', 'padding': '1.25rem 1.5rem',
              '&:is(:hover, :focus)': {'color': ACC},
              '&:is(.gb-block-is-current, .gb-block-is-current:hover, .gb-block-is-current:focus)': {'color': ACC}}
    tog_a = {'uniqueId': uid(p_ + 'tog'), 'tagName': 'div', 'styles': tog_st, 'css': make_css('gb-accordion__toggle-' + p_ + 'tog', tog_st),
             'htmlAttributes': {'id': 'gb-accordion-toggle-' + p_ + 'tog'}}
    ic_st = {'alignItems': 'center', 'color': ACC, 'display': 'flex', 'flexShrink': '0', 'justifyContent': 'center', 'svg': {'height': '1.125em', 'width': '1.125em'}}
    ic_a = {'uniqueId': uid(p_ + 'ic'), 'tagName': 'span', 'styles': ic_st, 'css': make_css('gb-accordion__toggle-icon-' + p_ + 'ic', ic_st)}
    ic_inner = ('<span class="gb-accordion__toggle-icon-open"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>'
                '<span class="gb-accordion__toggle-icon-close"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>')
    toggle_icon = blk('generateblocks-pro/accordion-toggle-icon', ic_a, '<span class="gb-accordion__toggle-icon gb-accordion__toggle-icon-%sic">' % p_, ic_inner, '</span>')
    title = tx(p_ + 'q', 'h3', q, {'fontFamily': HEAD, 'fontSize': '1.1875rem', 'fontWeight': '400', 'lineHeight': '1.4', 'marginBottom': '0'})
    toggle = blk('generateblocks-pro/accordion-toggle', tog_a, '<div class="gb-accordion__toggle gb-accordion__toggle-%stog" id="gb-accordion-toggle-%stog">' % (p_, p_),
                 '\n\n'.join([title, toggle_icon]), '</div>')
    body = el(p_ + 'body', 'div', {'padding': '0 1.5rem 1.375rem'}, [pp(p_ + 'a', a, size='1rem')], cls=None)
    cont_a = {'uniqueId': uid(p_ + 'cont'), 'tagName': 'div', 'htmlAttributes': {'id': 'gb-accordion-content-' + p_ + 'cont'}}
    content = blk('generateblocks-pro/accordion-content', cont_a, '<div class="gb-accordion__content" id="gb-accordion-content-%scont">' % p_, body, '</div>')
    return blk('generateblocks-pro/accordion-item', item_a, '<div class="gb-accordion__item gb-accordion__item-%sitem">' % p_, toggle + '\n\n' + content, '</div>')
faq_acc = blk('generateblocks-pro/accordion', {'uniqueId': uid('faqAccordion'), 'tagName': 'div'}, '<div class="gb-accordion">',
              '\n\n'.join(faq_item(i + 1, q, a) for i, (q, a) in enumerate(FAQ)), '</div>')
faq = section('solfaq', BASE, [
    doodle('solfaq_coffee', 'coffee', '30px', '30px', '10', {'right': '7%', 'bottom': '14px'}, ACC),
    el('solfaq_wrap', 'div', {'margin': '0 auto', 'maxWidth': '46rem'}, [
        tx('solfaq_tag', 'p', 'FREQUENTLY ASKED QUESTIONS', {'color': ACC, 'fontSize': '0.875rem', 'fontWeight': '600', 'letterSpacing': '0.06em', 'marginBottom': '1.5rem',
                                                           'marginTop': '0', 'textAlign': 'center', 'textTransform': 'uppercase'}),
        faq_acc]),
], extra_bg={'backgroundImage': 'linear-gradient(rgba(34, 48, 77, 0.075) 1px, transparent 1px)', 'backgroundSize': '100% 29px'})

# ---------- 6. TRUST ----------
TR = [('QuickBooks Certified', 'Every Pacioli accountant is a QuickBooks Online Certified Pro Advisor.', '-0.5',
       '<circle cx="12" cy="8.5" r="5.5"></circle><path d="M8 13.5 6.5 21l5.5-3 5.5 3-1.5-7.5"></path>'),
      ('CMA-Led Team', 'Overseen by a Certified Management Accountant (CMA), with a senior accountant supervising a team of bookkeepers and admin.', '0.5',
       '<circle cx="12" cy="7.5" r="4"></circle><path d="M4.5 21c0-4.2 3.4-7.5 7.5-7.5"></path><path d="M14 17.5l3 3 4.5-5"></path>'),
      ('A Small, Hands-On Team', 'Gives every client close attention while still handling controller-level work.', '-0.4',
       '<circle cx="8.5" cy="8" r="3"></circle><path d="M2.5 20c0-3.6 2.7-6.5 6-6.5s6 2.9 6 6.5"></path><circle cx="16.5" cy="9" r="2.3"></circle><path d="M15 13.2c2.8.5 5 3 5 6.3"></path>'),
      ('Priority Industries', 'Technology, legal and professional services, education, real estate, and select manufacturing.', '0.4',
       '<rect x="3.5" y="9" width="6" height="12"></rect><rect x="13.5" y="4" width="7" height="17"></rect><line x1="6" y1="12" x2="8" y2="12"></line><line x1="6" y1="15" x2="8" y2="15"></line><line x1="6" y1="18" x2="8" y2="18"></line><line x1="16" y1="7" x2="18" y2="7"></line><line x1="16" y1="10" x2="18" y2="10"></line><line x1="16" y1="13" x2="18" y2="13"></line><line x1="16" y1="16" x2="18" y2="16"></line>')]
tr_cards = []
for i, (t, d, rot, ico) in enumerate(TR):
    u = 'soltr%d' % i
    tr_cards.append(el(u, 'div', {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'padding': '1.375rem', 'columnGap': '1rem',
                                  'display': 'flex', 'transform': 'rotate(%sdeg)' % rot}, [
        icon_badge(u + 'ic', s24(ico), size=44, iw='1.1875rem', bg=BASE, mb=None, inline=False),
        el(u + 'txt', 'div', None, [tx(u + 't', 'h3', t, {'color': INK, 'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.0625rem', 'marginBottom': '0.25rem', 'marginTop': '0'}),
                                    pp(u + 'd', d, size='0.9375rem')])]))
trust = section('soltrust', SURF, [
    doodle('soltrust_receipt', 'receipt', '28px', '42px', '-12', {'top': '12px', 'left': '6%'}, ACC),
    head('soltrust_head', 'The Track Record', 'Why Businesses Trust Pacioli'),
    el('soltrust_grid', 'div', {'columnGap': '2rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(2,minmax(0,1fr))', 'rowGap': '1.75rem',
                                '@media (max-width:767px)': {'gridTemplateColumns': '1fr'}}, tr_cards),
], dashed=True, hattrs={'id': 'why-us'})

# ---------- 7. INSIGHTS (query loop) ----------
loop_item = blk('generateblocks/loop-item', {'uniqueId': uid('solins_item'), 'tagName': 'div',
                'styles': {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'overflow': 'hidden'},
                'css': '.gb-loop-item-solins_item{background-color:#fff;border:1.5px solid var(--paper-ink);border-radius:12px;box-shadow:4px 4px 0 rgba(34, 48, 77, 0.9);overflow:hidden}'},
                '<div class="gb-loop-item gb-loop-item-solins_item">', '\n\n'.join([
    blk('generateblocks/media', {'uniqueId': uid('solins_img'), 'tagName': 'img',
                                 'styles': {'height': 'auto', 'maxWidth': '100%', 'objectFit': 'cover', 'width': '100%', 'aspectRatio': '16 / 10'},
                                 'css': '.gb-media-solins_img{aspect-ratio:16/10;height:auto;max-width:100%;object-fit:cover;width:100%}',
                                 'htmlAttributes': {'src': '{{featured_image key:url|size:medium_large}}'}},
        '<img class="gb-media-solins_img" src="{{featured_image key:url|size:medium_large}}"/>', '', ''),
    el('solins_body', 'div', {'padding': '1.25rem'}, [
        tx('solins_title', 'h3', '{{post_title}}', {'fontFamily': HEAD, 'fontSize': '1.125rem', 'fontWeight': '600', 'color': INK, 'margin': '0 0 0.75rem'}),
        link_el('solins_link', '{{post_permalink}}', 'View Article')])]), '</div>')
looper = blk('generateblocks/looper', {'uniqueId': uid('solins_looper'), 'tagName': 'div',
             'styles': {'display': 'grid', 'gridTemplateColumns': 'repeat(3, minmax(0, 1fr))', 'columnGap': '2rem', 'rowGap': '2rem', '@media (max-width:1024px)': {'gridTemplateColumns': '1fr'}},
             'css': '.gb-looper-solins_looper{column-gap:2rem;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));row-gap:2rem}@media (max-width:1024px){.gb-looper-solins_looper{grid-template-columns:1fr}}'},
             '<div class="gb-looper-solins_looper">', loop_item, '</div>')
query = blk('generateblocks/query', {'uniqueId': uid('solins_query'), 'tagName': 'div', 'query': {'post_type': ['post'], 'posts_per_page': '3'}}, '<div>', looper, '</div>')
ins = section('solins', BASE, [
    doodle('solins_pencil', 'pencil', '24px', '36px', '14', {'bottom': '14px', 'left': '6%'}, ACC),
    head('solins_head', 'Practical Guidance for Running the Numbers Well', 'From Pacioli Insights'),
    query,
], extra_bg=DOTGRID)

sys.stdout.write('\n\n'.join([hero, about, grid, prom, faq, trust, '<!-- wp:block {"ref":51469} /-->', ins, '<!-- wp:block {"ref":51507} /-->']) + '\n')
