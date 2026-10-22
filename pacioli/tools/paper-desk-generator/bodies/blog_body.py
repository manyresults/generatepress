# =====================================================================
# BLOG ARCHIVE BODY  (replaces the old GP archive header; keeps {{archive_title}})
# Build (set BLOG_PART to split for the two GP Elements):
#   BLOG_PART=hero python3 -I build.py bodies/blog_body.py > ../../blog-page-hero-paper.html    (Page Hero - Blog)
#   BLOG_PART=loop python3 -I build.py bodies/blog_body.py > ../../blog-loop-template-paper.html (Loop - Blog and Archives)
# =====================================================================
def link_el(u, href, text):
    st = {'display': 'inline-flex', 'alignItems': 'center', 'columnGap': '0.5em', 'color': ACC, 'fontFamily': BODY, 'fontWeight': '600', 'fontSize': '0.9375rem',
          'textDecoration': 'none', 'svg': {'width': '1em', 'height': '1em'}, '&:is(:hover, :focus) svg': {'transform': 'translate3d(3px, 0px, 0px)'}}
    return el(u, 'a', st, [tx(u + 't', 'span', text), sh(u + 's', ARROW, {'display': 'inline-flex', 'svg': {'width': '1em', 'height': '1em'}})], hattrs={'href': href})

hero = section('blghero', BASE, [
    doodle('blghero_doc', 'doc', '34px', '44px', '12', {'top': '-4px', 'right': '10%'}, ACC),
    doodle('blghero_pencil', 'pencil', '30px', '42px', '-10', {'bottom': '-2px', 'left': '9%'}, INK),
    doodle('blghero_star', 'star', '26px', '26px', '0', {'right': '5%', 'bottom': '10px'}),
    el('blgherowrap', 'div', {'alignItems': 'center', 'display': 'flex', 'flexDirection': 'column', 'margin': '0 auto',
                              'maxWidth': '44rem', 'textAlign': 'center', 'position': 'relative'}, [
        eyebrow('blgheroeye', 'Pacioli Insights'),
        tx('blgh1', 'h1', '{{archive_title}}',
           {'fontFamily': HEAD, 'fontWeight': '700', 'fontSize': 'clamp(2.25rem,4.6vw,3.25rem)', 'color': INK,
            'letterSpacing': '-0.015em', 'lineHeight': '1.15', 'margin': '0 0 1.25rem'}),
        para('blgherop', 'Practical guidance on bookkeeping, payroll, and tax compliance from the Pacioli Finance team.',
             size='1.125rem', mb='0', extra={'maxWidth': '38rem'}),
    ]),
], pad=100, extra_bg=DOTGRID)

loop_css = ('.gb-loop-item-blgitem{background-color:#fff;border:1.5px solid var(--paper-ink);border-radius:12px;box-shadow:4px 4px 0 rgba(34, 48, 77, 0.9);'
            'overflow:hidden;display:flex;flex-direction:column;transition:transform 0.15s ease, box-shadow 0.15s ease}'
            '.gb-loop-item-blgitem:hover{transform:translate(-2px, -2px);box-shadow:6px 6px 0 rgba(34, 48, 77, 0.9)}')
loop_item = blk('generateblocks/loop-item', {'uniqueId': uid('blgitem'), 'tagName': 'div',
                'styles': {'backgroundColor': '#fff', 'border': CARD_BD, 'borderRadius': '12px', 'boxShadow': CARD_SH, 'overflow': 'hidden',
                           'display': 'flex', 'flexDirection': 'column', 'transition': 'transform 0.15s ease, box-shadow 0.15s ease',
                           '&:hover': {'transform': 'translate(-2px, -2px)', 'boxShadow': '6px 6px 0 rgba(34, 48, 77, 0.9)'}},
                'css': loop_css},
                '<div class="gb-loop-item gb-loop-item-blgitem">', '\n\n'.join([
    blk('generateblocks/media', {'uniqueId': uid('blgimg'), 'tagName': 'img',
                                 'styles': {'height': 'auto', 'maxWidth': '100%', 'objectFit': 'cover', 'width': '100%', 'aspectRatio': '16 / 10',
                                            'borderBottom': CARD_BD},
                                 'css': '.gb-media-blgimg{aspect-ratio:16/10;height:auto;max-width:100%;object-fit:cover;width:100%;border-bottom:1.5px solid #22304d}',
                                 'htmlAttributes': {'src': '{{featured_image key:url|size:medium_large}}'}},
        '<img class="gb-media-blgimg" src="{{featured_image key:url|size:medium_large}}"/>', '', ''),
    el('blgbody', 'div', {'padding': '1.375rem', 'display': 'flex', 'flexDirection': 'column', 'flexGrow': '1'}, [
        tx('blgdate', 'p', '{{post_date}}', {'fontFamily': HAND, 'fontSize': '1.15rem', 'fontWeight': '700', 'color': ACC, 'margin': '0 0 0.35rem'}),
        tx('blgtitle', 'h3', '{{post_title}}', {'fontFamily': HEAD, 'fontSize': '1.3125rem', 'fontWeight': '600', 'letterSpacing': '-0.01em',
                                                'lineHeight': '1.25', 'color': INK, 'margin': '0 0 0.6rem'}),
        tx('blgexc', 'p', '{{post_excerpt}}', {'fontFamily': BODY, 'fontSize': '0.9375rem', 'lineHeight': '1.55', 'color': MUTED,
                                               'margin': '0 0 1.25rem', 'flexGrow': '1'}),
        link_el('blglink', '{{post_permalink}}', 'Read article')])]), '</div>')
looper_css = ('.gb-looper-blglooper{column-gap:2rem;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));row-gap:2.25rem}'
              '.gb-looper-blglooper>.gb-loop-item:nth-child(odd){rotate:-0.4deg}.gb-looper-blglooper>.gb-loop-item:nth-child(even){rotate:0.4deg}'
              '@media (max-width:1024px){.gb-looper-blglooper{grid-template-columns:repeat(2,minmax(0,1fr))}}'
              '@media (max-width:640px){.gb-looper-blglooper{grid-template-columns:minmax(0,1fr)}}')
looper = blk('generateblocks/looper', {'uniqueId': uid('blglooper'), 'tagName': 'div',
             'styles': {'display': 'grid', 'gridTemplateColumns': 'repeat(3, minmax(0, 1fr))', 'columnGap': '2rem', 'rowGap': '2.25rem',
                        '@media (max-width:1024px)': {'gridTemplateColumns': 'repeat(2, minmax(0, 1fr))'},
                        '@media (max-width:640px)': {'gridTemplateColumns': 'minmax(0, 1fr)'}},
             'css': looper_css},
             '<div class="gb-looper-blglooper">', loop_item, '</div>')
query = blk('generateblocks/query', {'uniqueId': uid('blgquery'), 'tagName': 'div', 'inheritQuery': True,
                                     'query': {'post_type': ['post'], 'posts_per_page': '9'}}, '<div>', looper, '</div>')
posts = section('blgposts', SURF, [
    doodle('blgposts_clip', 'clip', '30px', '44px', '14', {'top': '14px', 'right': '5%'}, INK),
    query,
], pad=72, extra_bg=GRIDPAPER, dashed=True)

import os
PART = os.environ.get('BLOG_PART', 'all')
PARTS = {'hero': [hero], 'loop': [posts, '<!-- wp:block {"ref":51507} /-->'], 'all': [hero, posts, '<!-- wp:block {"ref":51507} /-->']}
sys.stdout.write('\n\n'.join(PARTS[PART]) + '\n')
