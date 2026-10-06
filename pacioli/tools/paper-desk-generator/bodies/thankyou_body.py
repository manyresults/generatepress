# =====================================================================
# THANK-YOU PAGE BODY (copy, links and iframe from pacioli/thank-you-page.html)
# python3 -I build.py bodies/thankyou_body.py > ../../thank-you-page-paper.html
# =====================================================================
AP, DASH = AMP + '#8217;', AMP + '#8212;'
CAL = 'https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ1UqukH_WpQ5M8lguGMZl2Teih1odWVS5Nwb-rZnA-l6r3tU0eZFwoGI4QBGFnfgfI9OV5CVy2D'
EMBED = CAL.replace('/u/0/', '/') + '?gv=true'
ICON['check'] = '<path d="M5 12l5 5 9-10"></path>'

hero = section('tyhero', BASE, [
    doodle('tyhero_star', 'star', '28px', '28px', '8', {'top': '24px', 'right': '14%'}),
    doodle('tyhero_plane', 'plane', '48px', '48px', '10', {'bottom': '24px', 'left': '12%'}, INK),
    el('tyhero_wrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto', 'maxWidth': '38rem',
                              'textAlign': 'center', 'position': 'relative'}, [
        el('tyhero_badge', 'div', {'marginBottom': '1.5rem', 'transform': 'rotate(-4deg)'}, [badge('tyhero_bd', 'check', size=64, icon_size='1.8rem')]),
        tx('tyhero_h1', 'h1', 'Thank <em>You</em>', {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
                                                  'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}, extra_css=hi_css('tyhero_h1')),
        para('tyhero_p', 'Your message has been received. A member of the Pacioli Finance team will follow up within one business day ' + DASH + ' or, if you' + AP + 'd rather not wait, book a time with us right now below.',
             size='1.125rem', mb='0'),
    ]),
], pad=88, extra_bg=DOTGRID)

card = el('tybook_card', 'div', {'backgroundColor': '#ffffff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'margin': '0 auto', 'maxWidth': '52rem',
                                 'overflow': 'hidden', 'padding': '0.75rem'}, [
    '<!-- wp:html -->\n<iframe src="%s" style="border:0" width="100%%" height="600" frameborder="0" title="Book a meeting with Pacioli Finance"></iframe>\n<!-- /wp:html -->' % EMBED])
book = section('tybook', SURF, [
    doodle('tybook_clip', 'clip', '30px', '44px', '14', {'top': '16px', 'right': '7%'}, INK),
    el('tybook_head', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto 2.5rem', 'maxWidth': '36rem', 'textAlign': 'center'}, [
        eyebrow('tybook_eye', 'Skip the Wait'),
        h2('tybook_h2', 'Book a Meeting With Our Team', mb='1rem'),
        para('tybook_p', 'Pick a time that works for you and we' + AP + 'll take it from there ' + DASH + ' no need to wait on an email back and forth.', mb='1.75rem'),
        btn('tybook_btn', 'Book a Meeting', CAL),
    ]),
    card,
    tx('tybook_note', 'p', 'Calendar not loading? <a href="%s" target="_blank" rel="noopener">Open the booking page in a new tab</a>.' % CAL,
       {'color': MUTED, 'fontFamily': BODY, 'fontSize': '0.875rem', 'lineHeight': '1.5', 'marginBottom': '0', 'marginTop': '1.25rem', 'textAlign': 'center'},
       extra_css='.gb-text-tybook_note a{color:var(--paper-accent);font-weight:600;text-decoration:underline;text-underline-offset:3px}'),
], pad=72, extra_bg=GRIDPAPER, dashed=True)

back = section('tyback', BASE, [
    el('tyback_wrap', 'div', {'textAlign': 'center'}, [
        el('tyback_link', 'a', {'alignItems': 'center', 'color': INK, 'columnGap': '0.5em', 'display': 'inline-flex', 'fontFamily': BODY, 'fontSize': '0.9375rem', 'fontWeight': '600',
                                'textDecoration': 'underline', 'textDecorationColor': ACC, 'textUnderlineOffset': '3px',
                                '&:is(:hover, :focus)': {'color': ACC}}, [
            sh('tyback_arrow', svg('<line x1="19" y1="12" x2="5" y2="12"></line><polyline points="11 6 5 12 11 18"></polyline>', sw='2'),
               {'display': 'inline-flex', 'svg': {'height': '1em', 'width': '1em'}}),
            tx('tyback_t', 'span', 'Back to Homepage')], hattrs={'href': '/'}),
    ]),
], pad=40)
sys.stdout.write('\n\n'.join([hero, book, back]) + '\n')
