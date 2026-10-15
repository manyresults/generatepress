import base64
def uri(f): return 'data:image/webp;base64,'+base64.b64encode(open('images/'+f,'rb').read()).decode()
LOGO,HERO,ABOUT=uri('jchp-logo.webp'),uri('jchp-hero.webp'),uri('jchp-about.webp')
css="""
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Yellowtail&display=swap');
.jchp-page{--teal:#1f4e4a;--teal-d:#123b38;--amber:#e8a33d;--amber-d:#b8791d;--cream:#f8f1e0;--cream-2:#fffaf0;--ink:#163b38;--line:#d9cdb8;position:relative;left:50%;width:100vw;margin-left:-50vw;color:var(--ink);font-size:17px;line-height:1.6;overflow-x:clip;font-family:'Mona Sans',system-ui,-apple-system,Arial,sans-serif;background:var(--cream)}
.jchp-page *,.jchp-page *::before,.jchp-page *::after{box-sizing:border-box}
.jchp-page h1,.jchp-page h2,.jchp-page h3{font-family:'Oswald','Arial Narrow',Arial,sans-serif;text-transform:uppercase;font-weight:700;letter-spacing:.01em;line-height:1.05;margin:0 0 .5em;color:var(--teal)}
.jchp-page p{margin:0 0 1em}
.jchp-page a{text-decoration:none}
.jchp-page img{max-width:100%;height:auto;display:block}
.jchp-page .wrap{width:min(1160px,100% - 2.5rem);margin-inline:auto}
.jchp-page .script{font-family:'Yellowtail','Brush Script MT',cursive;font-weight:400;text-transform:none;letter-spacing:0}
.jchp-page .eyebrow{font-size:.78rem;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--teal);margin:0 0 .9rem}
.jchp-page .btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;background:var(--amber);color:#173d39;border:0;border-radius:999px;padding:.95rem 1.7rem;font-weight:800;font-size:.95rem;text-transform:uppercase;letter-spacing:.07em;cursor:pointer;box-shadow:0 3px 0 var(--amber-d);transition:transform .18s,box-shadow .18s;font-family:inherit}
.jchp-page .btn:hover{transform:translateY(-2px);box-shadow:0 5px 0 var(--amber-d);color:#173d39}
.jchp-page .spark{color:var(--amber);font-size:2.4rem;line-height:1}
/* header */
.jchp-header{background:var(--cream);border-bottom:3px solid var(--teal);position:sticky;top:0;z-index:50}
.jchp-header .wrap{display:flex;align-items:center;justify-content:space-between;gap:1rem 2rem;flex-wrap:wrap;padding:.6rem 0}
.jchp-header .logo img{width:210px}
.jchp-nav{display:flex;gap:1.6rem;font-weight:700;font-size:.95rem}
.jchp-nav a{color:var(--ink);padding:.3rem 0;border-bottom:3px solid transparent}
.jchp-nav a:hover{border-color:var(--amber)}
.jchp-header .btn{padding:.75rem 1.3rem;font-size:.85rem}
/* hero */
.jchp-hero{position:relative;overflow:hidden;padding:3rem 0 4rem;min-height:min(86vh,820px);display:flex;align-items:center}
.jchp-hero .wrap{display:grid;gap:2rem;align-items:center;grid-template-columns:1fr}
.jchp-launch{display:inline-block;background:var(--teal);color:var(--cream);font-family:'Oswald',sans-serif;text-transform:uppercase;letter-spacing:.12em;padding:.4rem 1rem;border-radius:6px;font-size:.9rem;margin-bottom:1.2rem}
.jchp-hero h1{font-size:clamp(2.7rem,8.5vw,5.2rem);margin-bottom:.35em}
.jchp-hero h1 em{display:block;font-style:normal;color:#d78b20}
.jchp-hero .lead{font-size:1.2rem;max-width:33rem;color:#2c4a46}
.jchp-trust{display:flex;flex-wrap:wrap;gap:.6rem 1.8rem;margin:1.8rem 0 0;padding:0;list-style:none;font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.jchp-trust li{border-left:3px solid var(--amber);padding-left:.7rem}
.jchp-hero .art{position:relative}
.jchp-hero .art img{width:100%;border-radius:40% 40% 18px 18px / 30% 30% 18px 18px}
/* sections */
.jchp-sec{padding:4.5rem 0}
.jchp-dark{background:var(--teal);color:var(--cream)}
.jchp-dark h2,.jchp-dark h3{color:var(--cream)}
.jchp-dark .eyebrow{color:var(--amber)}
.jchp-page h2{font-size:clamp(2rem,5.5vw,3.3rem)}
.jchp-page h2 .script{color:#d78b20;font-size:1.25em}
.jchp-dark h2 .script{color:var(--amber)}
.jchp-about .wrap{display:grid;gap:2.5rem;align-items:center}
.jchp-about img{border-radius:18px;border:4px solid var(--teal);width:100%}
/* services */
.jchp-services{display:grid;gap:1.5rem 1rem;grid-template-columns:repeat(2,1fr);margin:2.5rem 0 0;padding:0;list-style:none}
.jchp-services li{text-align:center}
.jchp-services .ico{width:92px;height:92px;margin:0 auto .9rem;border-radius:50%;background:var(--cream);border:4px solid var(--amber);display:grid;place-items:center;font-size:2.6rem}
.jchp-services h3{font-size:1.15rem;margin-bottom:.3em}
.jchp-services p{font-size:.92rem;opacity:.9;margin:0}
.jchp-close{margin:3rem 0 0;font-weight:800;font-size:1.15rem;text-align:center;color:var(--amber)}
/* features */
.jchp-feat{display:grid;gap:1.2rem;margin-top:2.5rem}
.jchp-card{background:var(--cream-2);border:2px solid var(--line);border-radius:18px;padding:1.8rem;box-shadow:5px 5px 0 rgba(20,59,55,.14)}
.jchp-card .ico{font-size:2.4rem;display:block;margin-bottom:.5rem}
.jchp-card{color:var(--ink)}
.jchp-dark .jchp-card h3,.jchp-card h3{font-size:1.3rem;color:var(--teal)}
.jchp-dark .jchp-card p{color:var(--ink)}
.jchp-card p{margin:0;font-size:.98rem}
/* signup */
.jchp-signup{background:var(--amber);padding:4.5rem 0;color:var(--teal)}
.jchp-signup .wrap{display:grid;gap:2.5rem;align-items:start}
.jchp-signup h2,.jchp-signup .eyebrow{color:var(--teal)}
.jchp-signup h2 .script{color:var(--teal);font-size:1.2em}
.jchp-form{background:var(--cream-2);border:3px solid var(--teal);border-radius:20px;padding:1.8rem;box-shadow:6px 6px 0 var(--teal-d)}
.jchp-form label{display:block;font-weight:700;font-size:.9rem;margin-bottom:1rem;color:var(--ink)}
.jchp-form input[type=text],.jchp-form input[type=email],.jchp-form input[type=tel]{display:block;width:100%;margin-top:.35rem;padding:.8rem 1rem;border:2px solid var(--line);border-radius:10px;font-size:1rem;background:#fff;color:var(--ink)}
.jchp-form .check{display:flex;gap:.6rem;align-items:flex-start;font-weight:600}
.jchp-form .check input{margin-top:.35rem;flex:none}
.jchp-form small{display:block;color:#4a5f5b;font-size:.8rem;line-height:1.5;margin:.3rem 0 1rem}
.jchp-form .check small{display:inline}
.jchp-form .btn{width:100%;background:var(--teal);color:var(--cream);box-shadow:0 3px 0 #0c302d}
.jchp-form .btn:hover{color:var(--cream)}
/* footer */
.jchp-foot{background:var(--teal-d);color:var(--cream);text-align:center;padding:2rem 1rem;font-size:.9rem}
.jchp-foot p{margin:0 0 .4em}
.jchp-foot a{color:var(--cream);text-decoration:underline;text-decoration-color:var(--amber);text-underline-offset:4px;margin:0 .6rem}
@media(max-width:699px){.jchp-nav{order:3;width:100%;justify-content:space-between;gap:.5rem;font-size:.88rem}.jchp-header .logo img{width:150px}.jchp-hero .art{order:-1;max-width:420px;margin-inline:auto}}
@media(min-width:700px){.jchp-services{grid-template-columns:repeat(3,1fr)}.jchp-feat{grid-template-columns:repeat(3,1fr)}}
@media(min-width:900px){.jchp-hero .wrap{grid-template-columns:1.05fr .95fr;gap:3rem}.jchp-about .wrap{grid-template-columns:1fr 1fr;gap:4rem}.jchp-signup .wrap{grid-template-columns:1fr 1fr;gap:4rem}.jchp-services{grid-template-columns:repeat(5,1fr)}}
"""
css="\n".join(l for l in css.splitlines() if l.strip())
body=f"""<div class="jchp-page">
<header class="jchp-header"><div class="wrap"><a class="logo" href="#home" aria-label="Justin Case Home Pros"><img src="{LOGO}" alt="Justin Case Home Pros logo" width="375" height="180"></a><nav class="jchp-nav" aria-label="Page sections"><a href="#home">Home</a><a href="#about">About</a><a href="#features">Features</a><a href="#signup">Sign Up</a></nav><a class="btn" href="#signup">Get Early Access</a></div></header>
<section id="home" class="jchp-hero"><div class="wrap"><div><span class="jchp-launch">Launching January 1, 2027</span><h1>Something Dependable <em>Is Coming to Lower Bucks County.</em></h1><p class="lead">Justin Case Home Pros — backed by 30 years of hands-on experience. Launching January 1, 2027.</p><a class="btn" href="#signup">Get Early Access →</a><ul class="jchp-trust"><li>30 years experience</li><li>Licensed &amp; insured</li><li>Locally owned</li></ul></div><div class="art"><img src="{HERO}" alt="Justin Case Home Pros toolbox mascot in front of a home" width="499" height="465"></div></div></section>
<section id="about" class="jchp-sec jchp-about"><div class="wrap"><div><p class="eyebrow">About</p><h2>30 Years of Experience. <span class="script">One Trusted Name.</span></h2><p>Justin Case Home Pros is almost here — and we're bringing three decades of real, hands-on home repair experience with us.</p><p>Our team has spent 30 years combined fixing, installing, and maintaining homes across the region. Now we're bringing that same craftsmanship, honesty, and local trust directly to Lower Bucks County homeowners.</p><p>We're not a franchise and we're not a call center. We're local pros who show up, do it right, and stand behind every job — and we're putting the finishing touches on our new home online.</p></div><div><img src="{ABOUT}" alt="Justin Case Home Pros team" width="540" height="263"></div></div></section>
<section id="features" class="jchp-sec jchp-dark"><div class="wrap"><p class="eyebrow">Features</p><h2>Why Homeowners Will <span class="script">Trust Us.</span></h2><div class="jchp-feat"><article class="jchp-card"><span class="ico">🔧</span><h3>Decades of Hands-On Expertise</h3><p>Thirty years in the field means we've seen it, fixed it, and done it right — from quick repairs to full installations. There's no learning curve here, just real experience on every job.</p></article><article class="jchp-card"><span class="ico">✅</span><h3>Licensed, Insured &amp; Locally Trusted</h3><p>Justin Case Home Pros is a PA-registered home improvement contractor (HICPA # [HICPA #]), fully insured, and based right here in Lower Bucks County — not an out-of-town crew.</p></article><article class="jchp-card"><span class="ico">💵</span><h3>Honest Pricing, Guaranteed Results</h3><p>No hidden fees, no upsells — just clear pricing and work backed by our satisfaction guarantee. If it's not right, we'll make it right.</p></article></div></div></section>
<section id="services" class="jchp-sec"><div class="wrap"><p class="eyebrow">What We Do</p><h2>Handyman Services <span class="script">for Real Life.</span></h2><p>When we launch, Justin Case Home Pros will cover the full range of home repair needs across Lower Bucks County:</p><ul class="jchp-services" style="color:var(--ink)"><li><div class="ico" style="background:var(--teal)">🔌</div><h3>Installation</h3><p>TVs, smart home devices, lighting, fixtures, cabinetry, and more</p></li><li><div class="ico" style="background:var(--teal)">🔨</div><h3>Repair</h3><p>Drywall, doors, decks, fences, plumbing fixtures, and trim</p></li><li><div class="ico" style="background:var(--teal)">🖌️</div><h3>Maintenance</h3><p>Gutter cleaning, touch-up painting, seasonal prep and holiday lights</p></li><li><div class="ico" style="background:var(--teal)">🔑</div><h3>Make Ready</h3><p>Move-in/move-out prep, punch lists, and listing-ready touch-ups</p></li><li><div class="ico" style="background:var(--teal)">🏠</div><h3>Roof Repair</h3><p>Leak patching, shingle replacement, and gutter inspections</p></li></ul><p class="jchp-close" style="color:var(--teal)">One call, text, or form submission covers it all — no matter how long your honey-do list is.</p></div></section>
<section id="signup" class="jchp-signup"><div class="wrap"><div><p class="eyebrow">Sign Up</p><h2>Got a Honey-Do List? <span class="script">So Do We — Get On The List Now!</span></h2><p>Every home has one — that running list of little jobs just waiting for the right pros to show up. Justin Case Home Pros is building our own list too, and we want you on it first.</p><p>Sign up now and we'll let you know the moment we open for business in Lower Bucks County — plus you'll get early access to launch-day specials and [MEMBERSHIP NAME] founding-member pricing, so your honey-do list doesn't stand a chance.</p></div><!-- PLACEHOLDER FORM: replace this form with your Gravity Forms shortcode/block --><form class="jchp-form" action="#" method="post" onsubmit="return false"><label>Full Name<input type="text" name="full_name" autocomplete="name" required></label><label>Email Address<input type="email" name="email" autocomplete="email" required></label><label>Mobile Phone (optional)<input type="tel" name="phone" autocomplete="tel"></label><label>Service Address / Zip Code (optional — helps us prioritize service areas)<input type="text" name="zip" autocomplete="postal-code"></label><label class="check"><input type="checkbox" name="optin" checked><span>Yes, notify me when Justin Case Home Pros launches and send me early-access offers. <small>(Optional; can opt out anytime.)</small></span></label><small>By submitting this form, you agree to Justin Case Home Pros' <a href="/terms-and-conditions/">Terms of Service</a> and <a href="/privacy-policy/">Privacy Policy</a>. Message and data rates may apply.</small><button class="btn" type="submit">Notify Me at Launch</button></form></div></section>
<footer class="jchp-foot"><p>Justin Case Home Pros — Lower Bucks County, PA. Launching 2027.</p><p><a href="/privacy-policy/">Privacy Policy</a><a href="/terms-and-conditions/">Terms and Conditions</a></p></footer>
</div>"""
out=f"""<!--
  Justin Case Home Pros — Coming 2027 pre-launch one-pager (v2: single Custom HTML block, no nested group blocks)
  Slug: /  (static front page)
  SEO Title: Justin Case Home Pros | Coming 2027 to Lower Bucks County, PA
  Meta Description: Justin Case Home Pros is bringing 30 years of combined home repair experience to Lower Bucks County. Launching 2027 — join the list for early access and launch-day specials.
  Placeholders to replace: [HICPA #], [MEMBERSHIP NAME], and the form. Images are embedded; swap for Media Library files in images/ if preferred.
-->
<!-- wp:html -->
<style>
.home .site-header,.home .site-footer,.home .entry-header{{display:none}}
.home .site-content,.home .inside-article,.home .entry-content{{padding:0!important;margin:0!important;max-width:none!important}}
.home .site.grid-container{{max-width:none}}
html{{scroll-behavior:smooth;scroll-padding-top:90px}}
{css}
</style>
{body}
<!-- /wp:html -->
"""
open('homepage.html','w').write(out)
