#!/usr/bin/env python3
"""Generate the Clean-Up Bookkeeping page in the Paper Desk style (GenerateBlocks markup)."""
import json, re, sys

BS = chr(92)
AMP = chr(38)

def kebab(k):
    return re.sub(r'([A-Z])', lambda m: '-' + m.group(1).lower(), k)

def decls(d):
    return ';'.join('%s:%s' % (kebab(k), v) for k, v in d.items() if not isinstance(v, dict))

def make_css(sel, styles, extra=''):
    base = {k: v for k, v in styles.items() if not isinstance(v, dict)}
    out = ''
    if base:
        out += '.%s{%s}' % (sel, decls(base))
    for k, v in styles.items():
        if isinstance(v, dict) and k == 'svg':
            out += '.%s svg{%s}' % (sel, decls(v))
    for k, v in styles.items():
        if isinstance(v, dict) and k.startswith('&'):
            out += '.%s%s{%s}' % (sel, k[1:], decls(v))
    for k, v in styles.items():
        if isinstance(v, dict) and k.startswith('@media'):
            out += '%s{.%s{%s}}' % (k, sel, decls(v))
    return out + extra

USED = []

def attrs_json(a):
    s = json.dumps(a, ensure_ascii=False)
    return s.replace(AMP, BS + 'u0026').replace('<', BS + 'u003c').replace('>', BS + 'u003e')

def blk(name, a, html_open, inner, html_close):
    """wp block with open/close comments."""
    return '<!-- wp:%s %s -->\n%s%s%s\n<!-- /wp:%s -->' % (name, attrs_json(a), html_open, inner, html_close, name)

def uid(u):
    assert u not in USED, 'duplicate uniqueId ' + u
    USED.append(u)
    return u

def el(u, tag, styles=None, children=(), gclasses=None, hattrs=None, cls='gb-element', extra_css=''):
    uid(u)
    a = {'uniqueId': u, 'tagName': tag}
    if styles:
        a['styles'] = styles
        a['css'] = make_css('gb-element-' + u, styles, extra_css)
    if gclasses:
        a['globalClasses'] = gclasses
    if hattrs:
        a['htmlAttributes'] = hattrs
    if cls:
        a['className'] = cls
    classes = ' '.join((gclasses or []) + ['gb-element-' + u] + ([cls] if cls else []))
    attr_html = ''.join(' %s="%s"' % (k, v) for k, v in (hattrs or {}).items())
    return blk('generateblocks/element', a, '<%s class="%s"%s>' % (tag, classes, attr_html),
               '\n\n'.join(children), '</%s>' % tag)

def tx(u, tag, content, styles=None, hattrs=None, extra_css='', cls='gb-text'):
    uid(u)
    a = {'uniqueId': u, 'tagName': tag}
    if styles:
        a['styles'] = styles
        a['css'] = make_css('gb-text-' + u, styles, extra_css)
    if hattrs:
        a['htmlAttributes'] = hattrs
    if cls:
        a['className'] = cls
    attr_html = ''.join(' %s="%s"' % (k, v) for k, v in (hattrs or {}).items())
    extra_cls = ''.join(' ' + c for c in (cls or '').split() if c != 'gb-text')
    return blk('generateblocks/text', a, '<%s class="gb-text gb-text-%s%s"%s>' % (tag, u, extra_cls, attr_html),
               content, '</%s>' % tag)

def sh(u, svg, styles=None):
    uid(u)
    a = {'uniqueId': u}
    if styles:
        a['styles'] = styles
        a['css'] = make_css('gb-shape-' + u, styles)
    return blk('generateblocks/shape', a, '<span class="gb-shape gb-shape-%s">' % u, svg, '</span>')

# ---------- tokens ----------
INK, MUTED, BASE, SURF, LINE, ACC, HI = ('var(--paper-ink)', 'var(--paper-muted)', 'var(--paper-base)',
    'var(--paper-surface)', 'var(--paper-line)', 'var(--paper-accent)', 'var(--paper-hi)')
HEAD, BODY, HAND = 'var(--paper-font-head)', 'var(--paper-font-body)', 'var(--paper-font-hand)'
CARD_SH = '4px 4px 0 rgba(34, 48, 77, 0.9)'
CARD_BD = '1.5px solid #22304d'

# ---------- svgs (24x24 stroke icons) ----------
def svg(inner, fill='none', stroke='currentColor', sw='1.8', extra=''):
    return ('<svg viewBox="0 0 24 24" fill="%s" stroke="%s" stroke-width="%s" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true"%s>%s</svg>' % (fill, stroke, sw, extra, inner))

ICON = {
    'plane': '<path d="M3 11L21 3l-7 18-3-8zM11 13L21 3"></path>',
    'clip': '<path d="M16 8L7 18a3.5 3.5 0 0 0 5 5l10-11a6 6 0 0 0-8.5-8.5L4 14a8.5 8.5 0 0 0 12 12l7-7"></path>',
    'briefcase': '<rect x="3" y="7" width="18" height="12" rx="2"></rect><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="3" y1="12" x2="21" y2="12"></line>',
    'calc': '<rect x="5" y="2" width="14" height="20" rx="2"></rect><rect x="8" y="5" width="8" height="4"></rect><path d="M8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01M16 17h.01"></path>',
    'pencil': '<path d="M4 20l1-5L16 4l4 4L9 19zM14 6l4 4"></path>',
    'coffee': '<path d="M5 8h11v6a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5zM16 10h2a2 2 0 0 1 0 4h-2M8 3v2M12 3v2"></path>',
    'receipt': '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2zM9 8h6M9 12h6M9 16h4"></path>',
    'doc': '<path d="M7 3h8l4 4v14H7zM15 3v4h4M10 12h6M10 16h6"></path>',
    'ledger': '<path d="M4 5c3-1 6-1 8 1 2-2 5-2 8-1v14c-3-1-6-1-8 1-2-2-5-2-8-1zM12 6v14"></path>',
    'alert': '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v6M12 16.5h.01"></path>',
    'search': '<circle cx="11" cy="11" r="7"></circle><path d="M21 21l-4.3-4.3"></path>',
    'swap': '<path d="M7 7h13l-3-3M17 17H4l3 3"></path>',
    'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM8.5 12l2.5 2.5L16 9.5"></path>',
    'trend': '<path d="M3 17l6-6 4 4 8-8M15 7h6v6"></path>',
    'refresh': '<path d="M21 12a9 9 0 1 1-3-6.7M21 4v5h-5"></path>',
    'calendar': '<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M16 3v4M8 3v4M3 11h18"></path>',
    'stack': '<path d="M12 3l9 4.5-9 4.5-9-4.5zM3 12l9 4.5 9-4.5M3 16.5L12 21l9-4.5"></path>',
    'steps': '<path d="M9 6h11M9 12h11M9 18h11M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"></path>',
    'clock': '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path>',
    'users': '<circle cx="9" cy="8" r="3.5"></circle><path d="M2.5 20c.5-4 3-6 6.5-6s6 2 6.5 6M16 5a3.5 3.5 0 0 1 0 6.5M18 14c2 .7 3.3 2.5 3.5 6"></path>',
    'target': '<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="4.5"></circle><path d="M12 12h.01"></path>',
    'chat': '<path d="M4 5h16v11H9l-5 4z"></path>',
    'handshake': '<path d="M3 12l4-4 5 2 5-2 4 4-8 8zM9 14l2 2"></path>',
    'scale': '<path d="M12 4v16M5 20h14M4 8h16M4 8l-2 6a3 3 0 0 0 6 0zM20 8l-2 6a3 3 0 0 0 6 0z"></path>',
}
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line>'
         '<polyline points="13 6 19 12 13 18"></polyline></svg>')
STAR = svg('<path d="M12 2l2 7 7 1-6 4 2 8-5-4-5 4 2-8-6-4 7-1z"></path>', fill=HI, stroke=INK)
DOT = '<svg viewBox="0 0 8 8" aria-hidden="true"><circle cx="4" cy="4" r="4" fill="currentColor"></circle></svg>'

def doodle(u, kind, w, h, rot, pos, color=None, hide_mobile=True):
    st = {'display': 'inline-flex', 'position': 'absolute', 'svg': {'width': w, 'height': h},
          'transform': 'rotate(%sdeg)' % rot, 'pointerEvents': 'none'}
    if hide_mobile:
        st['@media (max-width:1100px)'] = {'display': 'none'}
    st.update(pos)
    if color:
        st['color'] = color
    inner = STAR if kind == 'star' else svg(ICON[kind])
    return sh(u, inner, st)

# ---------- shared pieces ----------
def section(u, bg, kids, pad=80, extra_bg=None, hattrs=None, dashed=False):
    st = {'position': 'relative', 'overflow': 'hidden', 'paddingTop': '%spx' % pad, 'paddingBottom': '%spx' % pad,
          '@media (max-width:767px)': {'paddingTop': '48px', 'paddingBottom': '48px'}, 'backgroundColor': bg}
    if extra_bg:
        st.update(extra_bg)
    if dashed:
        st['borderTop'] = '1.5px dashed ' + LINE
        st['borderBottom'] = '1.5px dashed ' + LINE
    inner = el(u + 'in', 'div', {'maxWidth': '1180px', 'marginLeft': 'auto', 'marginRight': 'auto',
                                  'paddingLeft': '24px', 'paddingRight': '24px', 'position': 'relative'},
               kids, gclasses=['gbp-section__inner'])
    return el(u, 'section', st, [inner], gclasses=['gbp-section', 'pacioli-paper'], hattrs=hattrs,
              cls='gb-element alignfull')

DOTGRID = {'backgroundImage': 'radial-gradient(rgba(34, 48, 77, 0.07) 1px, transparent 1px)', 'backgroundSize': '22px 22px'}
GRIDPAPER = {'backgroundImage': 'linear-gradient(rgba(34, 48, 77, 0.055) 1px, transparent 1px),linear-gradient(90deg, rgba(34, 48, 77, 0.055) 1px, transparent 1px)',
             'backgroundSize': '26px 26px, 26px 26px'}
LINED = {'backgroundImage': 'repeating-linear-gradient(transparent 0, transparent 31px, rgba(93, 101, 121, 0.16) 31px, rgba(93, 101, 121, 0.16) 32px)'}

def eyebrow(u, text, color=ACC, align=None):
    st = {'fontFamily': HAND, 'fontSize': '1.45rem', 'color': color, 'fontWeight': '700',
          'display': 'inline-block', 'transform': 'rotate(-1.5deg)', 'marginBottom': '0.5rem'}
    return tx(u, 'span', text, st)

def h2(u, text, color=INK, mb='1rem', extra_css=''):
    st = {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': 'clamp(1.75rem,3.2vw,2.25rem)', 'color': color,
          'letterSpacing': '-0.015em', 'lineHeight': '1.2', 'margin': '0 0 %s' % mb}
    return tx(u, 'h2', text, st, extra_css=extra_css)

def hi_css(u):
    return '.gb-text-%s em{font-style:normal;background:linear-gradient(transparent 62%%,var(--paper-hi) 62%% 92%%,transparent 92%%);padding:0 4px}' % u

def para(u, text, color=MUTED, size='1.0625rem', mb='1.5rem', extra=None):
    st = {'fontFamily': BODY, 'color': color, 'fontSize': size, 'lineHeight': '1.6', 'margin': '0 0 %s' % mb}
    if extra:
        st.update(extra)
    return tx(u, 'p', text, st)

def btn(u, text, href, kind='primary'):
    st = {'display': 'inline-flex', 'alignItems': 'center', 'justifyContent': 'center', 'columnGap': '0.5em',
          'fontFamily': BODY, 'fontWeight': '600', 'fontSize': '1rem', 'textDecoration': 'none',
          'paddingTop': '0.85rem', 'paddingBottom': '0.85rem', 'paddingLeft': '1.5rem', 'paddingRight': '1.5rem',
          'borderRadius': '10px', 'transition': 'transform 0.15s ease, box-shadow 0.15s ease'}
    if kind == 'primary':
        st.update({'backgroundColor': INK, 'color': BASE, 'border': '2px solid var(--paper-ink)', 'boxShadow': '3px 3px 0 var(--paper-ink)',
                   '&:is(:hover, :focus)': {'transform': 'translate(-1px, -1px)', 'boxShadow': '5px 5px 0 var(--paper-ink)'}})
    elif kind == 'light':  # on accent / dark backgrounds
        st.update({'backgroundColor': BASE, 'color': INK, 'border': '2px solid var(--paper-ink)', 'boxShadow': '3px 3px 0 var(--paper-ink)',
                   '&:is(:hover, :focus)': {'transform': 'translate(-1px, -1px)', 'boxShadow': '5px 5px 0 var(--paper-ink)'}})
    else:  # ghost on dark
        st.update({'backgroundColor': 'transparent', 'color': '#ffffff', 'border': '2px solid #ffffff',
                   '&:is(:hover, :focus)': {'backgroundColor': 'rgba(255, 255, 255, 0.14)'}})
    return tx(u, 'a', text, st, hattrs={'href': href})

def badge(u, icon, size=48, icon_size='1.4rem'):
    st = {'alignItems': 'center', 'backgroundColor': HI, 'border': CARD_BD, 'borderRadius': '50%',
          'boxShadow': '2px 2px 0 var(--paper-ink)', 'display': 'flex', 'flexShrink': '0',
          'height': '%spx' % size, 'justifyContent': 'center', 'width': '%spx' % size, 'color': INK}
    return el(u, 'div', st, [sh(u + 's', svg(ICON[icon]), {'display': 'inline-flex', 'color': INK,
                                                           'svg': {'height': icon_size, 'width': icon_size}})])

def dot_row(u, text, color=ACC, size='0.9375rem', text_color=MUTED, mt='0.42rem', icon=None):
    glyph = svg(ICON[icon]) if icon else DOT
    shape = sh(u + 'd', glyph, {'color': color, 'display': 'block', 'flexShrink': '0', 'marginTop': mt,
                                'svg': {'height': '7px', 'width': '7px'} if not icon else {'height': '1.1em', 'width': '1.1em'}})
    t = tx(u + 't', 'p', text, {'fontFamily': BODY, 'color': text_color, 'fontSize': size, 'lineHeight': '1.6', 'margin': '0'})
    return el(u, 'div', {'alignItems': 'flex-start', 'columnGap': '0.75rem', 'display': 'flex'}, [shape, t])

def col(u, kids, gap='0.75rem', extra=None):
    st = {'display': 'flex', 'flexDirection': 'column', 'rowGap': gap}
    if extra:
        st.update(extra)
    return el(u, 'div', st, kids)

# =====================================================================
# 1. HERO  (dot grid, base)
# =====================================================================
hero_inner = el('cuherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                                      'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
    eyebrow('cuheroeye', 'Clean-Up Bookkeeping'),
    tx('cuheroh1', 'h1', 'Transform Messy Ledgers into <em>Audit-Ready</em> Financials',
       {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
        'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('cuheroh1')),
    para('cuherop', "Eliminate tax-season stress and gain clear, accurate, and actionable insight into your company's bottom line.",
         size='1.125rem', mb='2rem', extra={'maxWidth': '38rem'}),
    btn('cuherobtn', 'Request a Consultation', '/contact'),
])
hero = section('cuhero', BASE, [
    doodle('cuhero_ledger', 'ledger', '48px', '48px', '-8', {'top': '-6px', 'right': '10%'}, ACC),
    doodle('cuhero_pencil', 'pencil', '34px', '44px', '14', {'bottom': '-4px', 'left': '9%'}, INK),
    doodle('cuhero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    hero_inner,
], pad=100, extra_bg=DOTGRID)

# =====================================================================
# 2. PAIN POINTS  (dark ink)
# =====================================================================
pains = [
    "Your books haven't been reconciled in months (or longer) and you're not sure what's actually accurate",
    "Tax season fills you with dread because you don't trust the numbers you'd be filing from",
    'A bookkeeping mistake was discovered and now everything downstream is in question',
    'Intercompany accounts, fixed assets, or payroll data are out of sync with the general ledger',
    'You want to move to ongoing management accounting support but need clean books first',
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
        tx('cupainclose', 'p', "That's where a focused, methodical clean-up engagement makes the difference.",
           {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.3rem', 'lineHeight': '1.5', 'color': HI, 'margin': '0'}),
    ]),
])

# =====================================================================
# 3. HOW PACIOLI HELPS  (surface, dashed borders)
# =====================================================================
cards_data = [
    ('search', 'Step 1', 'Discovery ' + AMP + 'amp; Data Collection', 'Gather historical books, charts of accounts, reconciliations, and trial balances before touching a single entry.', '#core-services', '-0.6'),
    ('swap', 'Step 2', 'Reconciliation Sprint', 'Methodically reconcile every General Ledger account against backups and source documents.', '#process', '0.5'),
    ('pencil', 'Step 3', 'Corrective Entries', 'Apply accurate, well-documented journal entries — no shortcuts, no guesswork.', '#deliverables', '-0.4'),
    ('shield', 'Step 4', 'Quality Review ' + AMP + 'amp; Sign-Off', 'A final pre-close review with a detailed findings report before you take the books forward.', '#timeline', '0.6'),
]
card_els = []
for i, (ic, step, title, desc, href, rot) in enumerate(cards_data, 1):
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
            tx(u + 'step', 'span', step, {'fontFamily': HAND, 'fontSize': '1.35rem', 'fontWeight': '700', 'color': ACC}),
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
    para('cuhelpintro', 'Our team audits, reconciles, and rebuilds your books so you can run your business with reliable numbers and real-time visibility — restoring accuracy, clarity, and confidence to your financials.',
         mb='2.75rem', extra={'maxWidth': '46rem'}),
    cards_grid,
], dashed=True)

# =====================================================================
# 4. FREE ASSESSMENT  (grid paper, base)
# =====================================================================
assess_items = ['A review of your chart of accounts, reconciliations, and trial balances',
                'An honest look at how far out of balance things really are',
                'A clear recommendation — no fluff, no pressure',
                'A typical 4–8 week clean-up timeline scoped to your volume']
note = el('cunote', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH,
                            'padding': '2rem', 'transform': 'rotate(1.5deg)', 'position': 'relative',
                            'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem'}, [
    doodle('cunote_clip', 'clip', '30px', '48px', '12', {'top': '-22px', 'right': '24px'}, ACC, hide_mobile=False),
    tx('cunotehd', 'span', 'What the assessment covers', {'fontFamily': HAND, 'fontSize': '1.6rem', 'fontWeight': '700', 'color': ACC}),
    col('cunotelist', [dot_row('cunote%d' % (i + 1), t, size='1rem', text_color=INK) for i, t in enumerate(assess_items)], gap='0.85rem'),
])
assess_left = el('cuassessleft', 'div', None, [
    eyebrow('cuassesseye', 'Get Started'),
    h2('cuassessh2', 'Start With a Free Books Assessment'),
    para('cuassessp', 'This is the obvious first step, not a sales pitch — a clear-eyed look at where your books stand today.', mb='2rem'),
    btn('cuassessbtn', 'Hire Your Team', '/contact'),
], cls='gb-element')
assess = section('cuassesssec', BASE, [
    doodle('cuassess_calc', 'calc', '36px', '44px', '-10', {'top': '14px', 'left': '4%'}, INK),
    el('cuassessgrid', 'div', {'alignItems': 'center', 'columnGap': '4rem', 'display': 'grid', 'gridTemplateColumns': '1.1fr 1fr',
                               'rowGap': '2.5rem', '@media (max-width:900px)': {'gridTemplateColumns': '1fr'}},
       [assess_left, note]),
], extra_bg=GRIDPAPER)

# =====================================================================
# 5. TRUST  (lined paper, surface)
# =====================================================================
trust_data = [('trend', 'Path to Ongoing Support', 'Clean-up is often the entry point that converts into an ongoing accounting-department relationship'),
              ('refresh', 'Repeatable Process', 'A repeatable, four-step process (discovery, reconciliation, correction, sign-off) refined across dozens of engagements'),
              ('calendar', 'Ongoing Maintenance', "SLA options for ongoing monthly clean-ups or quarterly re-cleans, so the mess doesn't come back")]
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

# =====================================================================
# 6. MID CTA  (solid accent)
# =====================================================================
mid = section('cumidsec', ACC, [
    doodle('cumid_plane', 'plane', '52px', '52px', '10', {'top': '10px', 'left': '8%'}, '#ffffff'),
    doodle('cumid_star', 'star', '30px', '30px', '-6', {'bottom': '12px', 'right': '9%'}),
    el('cumidwrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                            'maxWidth': '40rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('cumideye', "Curious What's Included?", HI),
        h2('cumidh2', 'See exactly what clean-up bookkeeping looks like in practice.', '#ffffff', mb='1.75rem'),
        el('cumidbtns', 'div', {'alignItems': 'center', 'columnGap': '1rem', 'display': 'flex', 'justifyContent': 'center',
                                '@media (max-width:767px)': {'flexDirection': 'column', 'rowGap': '1rem'}}, [
            btn('cumidbtn1', 'Request a Consultation', '/contact', 'light'),
            btn('cumidbtn2', 'See the Full Service Breakdown', '#service-breakdown', 'ghost'),
        ]),
    ]),
], pad=72)

# =====================================================================
# 7. PROMISE  (dot grid, base)
# =====================================================================
vals = [('target', 'Clarity', 'A detailed findings report you can actually understand.'),
        ('scale', 'Accuracy', 'Every account reconciled against source documents.'),
        ('chat', 'Communication', 'Real people explaining what was wrong and what was fixed.'),
        ('shield', 'Accountability', 'A team that owns the clean-up within scope.'),
        ('handshake', 'Collaboration', 'We work with your team and other advisors during discovery.'),
        ('trend', 'Scalability', 'A one-time clean-up or an ongoing SLA — whatever you need next.')]
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
        para('cuprompara', 'We restore accuracy so you can make decisions with confidence — real people rebuilding your books, not just software running reports.', mb='2rem'),
        btn('cuprombtn', 'Request a Consultation', '/contact'),
    ]),
    tx('cupromsub', 'h3', 'What You Can Expect From Us', {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.375rem', 'color': INK,
                                                          'margin': '0 0 1.5rem', 'position': 'relative'}),
    el('cupromgrid', 'div', {'columnGap': '1.75rem', 'display': 'grid', 'gridTemplateColumns': 'repeat(3,minmax(0,1fr))', 'rowGap': '1.75rem',
                             '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2,minmax(0,1fr))'},
                             '@media (max-width:600px)': {'gridTemplateColumns': '1fr'}}, val_els),
], extra_bg=DOTGRID)

# =====================================================================
# 8. FULL SERVICE BREAKDOWN  (GenerateBlocks Pro accordion)
# =====================================================================
def acc_item(n, anchor, icon, title, body_kids):
    p = 'cuacc%02d' % n
    item_st = {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '10px', 'boxShadow': CARD_SH, 'marginBottom': '1.25rem'}
    item_a = {'uniqueId': p + 'item', 'tagName': 'div', 'styles': item_st,
              'css': make_css('gb-accordion__item-' + p + 'item', item_st), 'htmlAttributes': {'id': anchor}}
    tog_st = {'alignItems': 'center', 'color': INK, 'columnGap': '1rem', 'cursor': 'pointer', 'display': 'flex',
              'justifyContent': 'space-between', 'padding': '1.5rem 2rem',
              '&:is(:hover, :focus)': {'color': ACC},
              '&:is(.gb-block-is-current, .gb-block-is-current:hover, .gb-block-is-current:focus)': {'color': ACC}}
    tog_a = {'uniqueId': p + 'tog', 'tagName': 'div', 'styles': tog_st,
             'css': make_css('gb-accordion__toggle-' + p + 'tog', tog_st),
             'htmlAttributes': {'id': 'gb-accordion-toggle-' + p + 'tog'}}
    ic_st = {'alignItems': 'center', 'color': ACC, 'display': 'flex', 'flexShrink': '0', 'justifyContent': 'center',
             'svg': {'height': '1.125em', 'width': '1.125em'}}
    ic_a = {'uniqueId': p + 'ic', 'tagName': 'span', 'styles': ic_st, 'css': make_css('gb-accordion__toggle-icon-' + p + 'ic', ic_st)}
    ic_inner = ('<span class="gb-accordion__toggle-icon-open"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                'stroke-width="1.75" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>'
                '<span class="gb-accordion__toggle-icon-close"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                'stroke-width="1.75" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"></line></svg></span>')
    toggle_icon = blk('generateblocks-pro/accordion-toggle-icon', ic_a,
                      '<span class="gb-accordion__toggle-icon gb-accordion__toggle-icon-%sic">' % p, ic_inner, '</span>')
    for x in (p + 'item', p + 'tog', p + 'ic', p + 'cont'):
        uid(x)
    head_badge = badge(p + 'bd', icon, size=44, icon_size='1.3rem')
    head_title = tx(p + 'h3', 'h3', title, {'fontFamily': HEAD, 'fontWeight': '600', 'fontSize': '1.25rem', 'color': INK,
                                            'letterSpacing': '-0.015em', 'flexGrow': '1', 'margin': '0 0 0 1rem'})
    toggle = blk('generateblocks-pro/accordion-toggle', tog_a,
                 '<div class="gb-accordion__toggle gb-accordion__toggle-%stog" id="gb-accordion-toggle-%stog">' % (p, p),
                 '\n\n'.join([head_badge, head_title, toggle_icon]), '</div>')
    body_el = el(p + 'body', 'div', {'padding': '0 2rem 2rem'}, [col(p + 'list', body_kids)], cls=None)
    cont_a = {'uniqueId': p + 'cont', 'tagName': 'div', 'htmlAttributes': {'id': 'gb-accordion-content-' + p + 'cont'}}
    content = blk('generateblocks-pro/accordion-content', cont_a,
                  '<div class="gb-accordion__content" id="gb-accordion-content-%scont">' % p, body_el, '</div>')
    return blk('generateblocks-pro/accordion-item', item_a,
               '<div class="gb-accordion__item gb-accordion__item-%sitem" id="%s">' % (p, anchor),
               toggle + '\n\n' + content, '</div>')

def plain_row(u, text):
    return el(u, 'div', {'alignItems': 'flex-start', 'columnGap': '0.75rem', 'display': 'flex'}, [
        tx(u + 't', 'p', text, {'fontFamily': BODY, 'color': MUTED, 'fontSize': '0.9375rem', 'lineHeight': '1.6', 'margin': '0'})])

core = ['Chart of accounts cleanup and reorganization', 'Bank, credit card, and cash reconciliations',
        'Accounts payable and accounts receivable cleanup', 'Clean-up of intercompany accounts and eliminations',
        'Fixed assets reconciliation and depreciation corrections', 'Payroll and payroll tax data harmonization',
        'Journal entry correction and backdated adjustment entries']
process = ['1. Discovery and data collection — gather historical books, charts of accounts, reconciliations, and trial balances',
           '2. Reconciliation sprint — methodically reconcile every General Ledger account against backups and source documents',
           '3. Corrective entries — apply accurate, well-documented journal entries',
           '4. Quality review and sign-off — final pre-close review with a detailed findings report']
deliv = ['Reconciled historical and current-period General Ledger', 'Updated chart of accounts and cost centers (if needed)',
         'Cleaned AP/AR, vendor/customer data, and master data', 'Reconciled bank statements and cash positions',
         'Monthly closing package with supported journal entries', 'Error-free, auditable financial statements']
timeline_first = 'A full clean-up typically runs 4–8 weeks, depending on volume.'
timeline = ['Interim milestones: data collection → first-pass reconciliations → remediation → final sign-off',
            'SLA options: ongoing monthly clean-ups or quarterly re-cleans to maintain accuracy']

items = [
    acc_item(1, 'core-services', 'stack', 'Core Services', [dot_row('cuc%d' % (i + 1), t) for i, t in enumerate(core)]),
    acc_item(2, 'process', 'steps', 'Process and Approach', [plain_row('cup%d' % (i + 1), t) for i, t in enumerate(process)]),
    acc_item(3, 'deliverables', 'doc', 'Deliverables', [dot_row('cud%d' % (i + 1), t) for i, t in enumerate(deliv)]),
    acc_item(4, 'timeline', 'clock', 'Typical Timeline',
             [plain_row('cut0', timeline_first)] + [dot_row('cut%d' % (i + 1), t) for i, t in enumerate(timeline)]),
]
accordion = blk('generateblocks-pro/accordion', {'uniqueId': uid('cuaccordion'), 'tagName': 'div'},
                '<div class="gb-accordion">', '\n\n'.join(items), '</div>')
breakdown = section('cubreaksec', SURF, [
    doodle('cubreak_pencil', 'pencil', '28px', '40px', '16', {'top': '12px', 'right': '7%'}, ACC),
    eyebrow('cubreakeye', 'Scope of Work'),
    h2('cubreakh2', 'Full Service Breakdown', mb='2.5rem'),
    accordion,
], dashed=True, hattrs={'id': 'service-breakdown'})

# reusable blocks (testimonials + closing CTA) already live on the site
refs = '<!-- wp:block {"ref":51469} /-->\n\n<!-- wp:block {"ref":51507} /-->'

page = '\n\n'.join([hero, pain, helps, assess, trust, mid, promise, breakdown, refs]) + '\n'
page = page.replace(AMP + 'amp;', AMP + 'amp;')  # (entities typed via AMP + 'amp;' are already final)
sys.stdout.write(page)
