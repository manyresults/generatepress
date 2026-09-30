"""Brand content for build_brand_page.py.

Each brand is built from shared templates (store facts, hours, ID law, hero/where-to-buy copy) plus
brand-specific copy. Anything in [[ ... ]] is unverified and must be filled or removed before publishing.
"""

SITE = "https://beerarama.com"
PHONE = "215-946-3480"
HOURS_ANSWER = "Sunday 10AM–5PM, Monday–Thursday 9AM–8PM, Friday–Saturday 9AM–9PM. Holiday hours may differ."
TRENDS = ("[[GOOGLE_TRENDS_INSIGHT: 1-2 sentences from trends.google.com for the Philadelphia area, past 5 years, "
          "e.g. when \"{name}\" searches peak.]] Popular searches: [[RELATED_QUERY_1]], [[RELATED_QUERY_2]], [[RELATED_QUERY_3]].")
PRICING = "[[PRICE, or \"Stop in or call " + PHONE + " for today's price\"]]"


def make(name, slug, kind, packages, *, hook, scene, about, specs, history, pairings, occasions,
         spec_answer, schema_desc, faqs_extra, related, verify, formats=None, keg_q=None, keg_a=None):
    beer = kind == "Beer"
    packs = "cases, packs and kegs" if beer else "cases and packs"
    faqs = [
        (f"Where can I buy {name} in Levittown, PA?",
         "Beer-A-Rama, across from the Levittown Town Center at Route 13 &amp; Levittown Pkwy. We've served Lower Bucks County since 1968."),
        (f"Does Beer-A-Rama sell {name} by the case?" if beer else f"What {name} packs does Beer-A-Rama carry?",
         (f"Yes. [[CONFIRM: cases, 24-packs, 30-packs available]]. Call {PHONE} and we'll tell you what's cold and in stock."
          if beer else f"[[CONFIRM: 6-packs, 12-packs, variety packs, cases carried]]. Call {PHONE} and we'll tell you what's cold and in stock.")),
        (f"How many calories and how much alcohol are in {name}?", spec_answer),
        *faqs_extra,
        (keg_q or (f"Do you sell {name} kegs in Levittown?" if beer else f"Do you carry {name} variety packs?"),
         keg_a or (f"[[CONFIRM {name} keg sizes in stock]] We also carry taps and CO² for parties. See our "
                   f"<a href=\"{SITE}/kegs/\">keg page</a> or call {PHONE}." if beer else
                   f"[[CONFIRM variety packs in stock]] Call {PHONE} and we'll tell you what's cold and ready.")),
        ("Do I need ID to buy beer at Beer-A-Rama?",
         "Yes. You must be 21 or older and show valid ID to buy beer in Pennsylvania."),
        ("What are your Levittown store hours?", HOURS_ANSWER),
    ]
    return {
        "prefix": slug.replace("-", "")[:4],
        "slug": slug, "url": f"{SITE}/brands/{slug}/", "name": name, "type": kind, "packages": packages,
        "schema_brand": {"Miller Lite": "Miller", "Coors Light": "Coors"}.get(name, name),
        "schema_desc": schema_desc,
        "seo": {
            "title": f"{name} in Levittown, PA | {'Cases & Kegs' if beer else 'Cases & Packs'} | Beer-A-Rama",
            "desc": f"Buy {name} in Levittown, PA at Beer-A-Rama. Cold {'cases, packs and kegs' if beer else 'cases and packs'} at low prices, "
                    "across from Levittown Town Center. Family owned since 1968.",
            "alt": f"{name} available at Beer-A-Rama in Levittown, PA",
        },
        "hero_lead": f"Looking for {name} in Levittown? Beer-A-Rama is Lower Bucks County's Low Price Leader, proudly serving "
                     f"Levittown since 1968 — and {name} is {hook}.",
        "hero_body": f"Whether you're {scene}, our family-owned team will get you cold {name} at prices that beat the big chains. "
                     f"Ask about {name} {packs}, chilled to 37°F daily.",
        "about": about, "specs": specs, "history": history, "pairings": pairings,
        "buy_lead": f"Beer-A-Rama is a Levittown beer distributor, so you can buy {name} by the case instead of paying "
                    "convenience-store prices for singles.",
        "formats": formats or f"[[CONFIRM_AND_LIST: {', '.join(packages)} carried]]",
        "pricing": PRICING, "trends": TRENDS.format(name=name),
        "kegs_line": (f"Planning a bigger party? Ask about {name} kegs, taps and CO² rentals, or call {PHONE} and we'll help you pick the right size."
                      if beer else
                      f"Stocking up for a party? Ask about {name} cases and packs, or call {PHONE} and we'll help you plan how much to grab."),
        "occasions": occasions,
        "where": (f"Beer-A-Rama is across from the Levittown Town Center at Route 13 and Levittown Pkwy, an easy stop from anywhere in "
                  f"Levittown. Stop in for cold {name}, or call {PHONE} to check what's in the cooler before you come."),
        "faqs": faqs, "related": [(n, f"{SITE}/brands/{s}/") for n, s in related],
        "related_heading": "Other Beers in Levittown, PA" if beer else "Other RTDs in Levittown, PA",
        "verify": verify,
    }


BEER_PACKS = ["6 Pack", "12 Pack", "Case", "Keg"]
RTD_PACKS = ["6 Pack", "12 Pack", "Case"]

MILLER_LITE = make(
    "Miller Lite", "miller-lite", "Beer", BEER_PACKS,
    hook="one of the beers our neighbors ask for most",
    scene="grabbing a case for the weekend, stocking up for a Levittown backyard cookout, or heading to a tailgate",
    about="Whether it's the end of the workday or a few minutes to kickoff, it's always Miller Time. As the original light beer, this fine pilsner revolutionized the beer business. With a body that won't fill you up and flavor that stands the test of time, it's just as satisfying today as it was when it changed the landscape of American beer.",
    specs=[("Style", "American Light Lager"), ("ABV", "4.2%"), ("Calories", "96 per 12 oz"), ("Brewed In", "Milwaukee, WI")],
    history="Miller Lite went national in 1975, and its \"Great Taste, Less Filling\" slogan helped turn light beer into a household category. Today it's brewed by Molson Coors and is still one of the most popular beers in America — and one of the most requested at our Levittown store.",
    pairings="Miller Lite's crisp, easy-drinking profile goes with pizza, wings, burgers, hot dogs, soft pretzels and chips. For best flavor, serve it ice cold — we chill everything to 37°F daily, so it's ready the moment you walk out the door.",
    occasions=[("Eagles Sundays", "Grab a case before kickoff and keep the cooler full for the whole game."),
               ("Phillies Nights", "Cold Miller Lite for the backyard, the patio or the watch party."),
               ("Cookouts &amp; Graduations", "Stock up for the crowd, then add chips, pretzels and dips from our snack aisle."),
               ("Shore Weekends", "Load up the cooler on your way out of Levittown for a Jersey Shore weekend.")],
    spec_answer="A 12 oz Miller Lite has 96 calories, 3.2 g of carbs and 4.2% ABV.",
    schema_desc="Miller Lite, the original light beer: an American light lager with 96 calories, 3.2 g carbs and 4.2% ABV, sold at Beer-A-Rama in Levittown, PA.",
    faqs_extra=[
        ("How many cans are in a case of Miller Lite?", "A standard case of Miller Lite cans is 24 cans. [[CONFIRM pack sizes carried]]"),
        ("What's the difference between Miller Lite and Miller High Life?",
         "Miller Lite is a light lager with 96 calories and 4.2% ABV. Miller High Life, Miller's original \"Champagne of Beers,\" is a fuller-bodied pilsner with 141 calories and 4.6% ABV."),
    ],
    related=[("Bud Light", "bud-light"), ("Coors Light", "coors-light"), ("Yuengling", "yuengling")],
    formats="Ask about Miller Lite 6-packs, 12-packs, cases and kegs. [[CONFIRM exact pack sizes and cans vs. bottles]]",
    verify="Miller Lite history (1975 national launch, Molson Coors owner); High Life stats (141 cal, 4.6% ABV); 24-can case; exact pack sizes.",
)

BUD_LIGHT = make(
    "Bud Light", "bud-light", "Beer", BEER_PACKS,
    hook="an easy pick for any Levittown get-together",
    scene="grabbing a case for game day, stocking up for a Levittown graduation party, or loading the cooler for a tailgate",
    about="Crisp, clean and easy to drink, Bud Light is a light lager brewed by Anheuser-Busch with a subtle hint of hop aroma and a delicate malt sweetness. It's built to be shared — the kind of beer that's always on hand when friends, family and football are involved.",
    specs=[("Style", "American Light Lager"), ("ABV", "4.2%"), ("Calories", "110 per 12 oz"), ("Brewed By", "Anheuser-Busch")],
    history="Bud Light debuted in 1982 from Anheuser-Busch of St. Louis and has been one of the best-known light beers in America ever since. Its light, refreshing profile made it a fixture at tailgates, cookouts and sports bars across the country — including right here in Levittown.",
    pairings="Bud Light's clean, refreshing finish pairs with classic party food: wings, nachos, burgers, pizza and hot dogs. Serve it ice cold — we chill every cooler to 37°F daily, so it's ready to go the moment you leave the store.",
    occasions=[("Game Day Tailgates", "Load up on Bud Light before kickoff and keep the cooler stocked all afternoon."),
               ("Graduation Parties", "Cases and packs to cover a backyard full of family and friends."),
               ("Backyard Cookouts", "An easy, crowd-pleasing light beer to go with the grill."),
               ("Shore Weekends", "Pick up cold cases on your way out of Levittown for the Jersey Shore.")],
    spec_answer="A 12 oz Bud Light has 110 calories, 6.6 g of carbs and 4.2% ABV.",
    schema_desc="Bud Light, Anheuser-Busch's American light lager with 110 calories and 4.2% ABV, sold at Beer-A-Rama in Levittown, PA.",
    faqs_extra=[
        ("What's the difference between Bud Light and Budweiser?",
         "Bud Light is a light lager with 110 calories and 4.2% ABV. Budweiser, Anheuser-Busch's flagship American lager, is fuller-bodied with 145 calories and 5% ABV."),
        ("How many cans are in a case of Bud Light?", "A standard case of Bud Light cans is 24 cans. [[CONFIRM pack sizes carried]]"),
    ],
    related=[("Miller Lite", "miller-lite"), ("Coors Light", "coors-light"), ("Yuengling", "yuengling")],
    verify="Bud Light 1982 debut; 110 cal / 6.6g carbs / 4.2% ABV; Budweiser 145 cal / 5% ABV; 24-can case; pack sizes and kegs carried.",
)

COORS_LIGHT = make(
    "Coors Light", "coors-light", "Beer", BEER_PACKS,
    hook="a cold, easy choice for any Levittown get-together",
    scene="grabbing a case for the weekend, stocking up for a Levittown cookout, or heading out for a day on the water",
    about="Brewed with pure Rocky Mountain water, Coors Light is a smooth, refreshing light lager known as \"The Silver Bullet.\" Its clean, crisp taste and ultra-cold refreshment make it a go-to for anyone who likes their beer as cold as possible.",
    specs=[("Style", "American Light Lager"), ("ABV", "4.2%"), ("Calories", "102 per 12 oz"), ("Origin", "Golden, CO")],
    history="Coors Light launched in 1978 from the Coors brewery in Golden, Colorado, and its Rocky Mountain branding has made it one of the most recognizable light beers in the country. Today it's brewed by Molson Coors and sold coast to coast.",
    pairings="Coors Light's clean, crisp profile goes with grilled chicken, tacos, burgers, wings and chips. Serve it ice cold — we chill everything to 37°F daily, so the mountains on the can will be blue by the time you get home.",
    occasions=[("Eagles Sundays", "Stock the cooler with Coors Light before kickoff and keep it ice cold all game."),
               ("Days on the Water", "Cold cases for boating, fishing and the Delaware River."),
               ("Backyard Cookouts", "A crisp, easy-drinking light beer to go with whatever's on the grill."),
               ("Shore Weekends", "Load up on your way out of Levittown for a Jersey Shore weekend.")],
    spec_answer="A 12 oz Coors Light has 102 calories, 5 g of carbs and 4.2% ABV.",
    schema_desc="Coors Light, the Rocky Mountain American light lager with 102 calories and 4.2% ABV, sold at Beer-A-Rama in Levittown, PA.",
    faqs_extra=[
        ("Why do the mountains on the Coors Light can turn blue?",
         "They're cold-activated. The mountains on a Coors Light can turn blue when the beer is cold — and we chill everything at Beer-A-Rama to 37°F daily."),
        ("How many cans are in a case of Coors Light?", "A standard case of Coors Light cans is 24 cans. [[CONFIRM pack sizes carried]]"),
    ],
    related=[("Miller Lite", "miller-lite"), ("Bud Light", "bud-light"), ("Yuengling", "yuengling")],
    verify="Coors Light 1978 launch, Golden CO, Molson Coors; 102 cal / 5g carbs / 4.2% ABV; cold-activated mountain description; 24-can case; pack sizes and kegs carried.",
)

YUENGLING = make(
    "Yuengling", "yuengling", "Beer", BEER_PACKS,
    hook="a Pennsylvania original",
    scene="grabbing a case of the hometown favorite, stocking up for a Levittown cookout, or bringing something local to a party",
    about="Yuengling Traditional Lager is Pennsylvania's own — an amber lager with a smooth, slightly sweet malt character and a balanced finish. Brewed in Pottsville, PA by America's oldest brewery, it's a true local favorite across the Delaware Valley.",
    specs=[("Style", "Amber Lager"), ("ABV", "[[4.5% — VERIFY]]"), ("Calories", "[[140 per 12 oz — VERIFY]]"), ("Brewed In", "Pottsville, PA")],
    history="D.G. Yuengling &amp; Son has been brewing in Pottsville, Pennsylvania since 1829, which makes it America's oldest brewing company. Yuengling Traditional Lager is its flagship, and it's a Pennsylvania staple at cookouts, tailgates and corner bars alike.",
    pairings="Yuengling's amber malt character pairs with burgers, pizza, soft pretzels, pulled pork and cheesesteaks. Serve it ice cold — we chill everything to 37°F daily, so it's ready the moment you walk out the door.",
    occasions=[("Eagles Sundays", "A Pennsylvania beer for a Philadelphia game day. Grab a case before kickoff."),
               ("Phillies Nights", "Cold Yuengling for the patio, the porch and the watch party."),
               ("Cookouts &amp; Reunions", "A crowd-pleasing local lager for family get-togethers."),
               ("Bringing Something Local", "Bringing a host a six-pack? You can't go wrong with a Pennsylvania original.")],
    spec_answer="[[VERIFY: Yuengling Traditional Lager ABV and calories per 12 oz — confirm at yuengling.com before publishing.]]",
    schema_desc="Yuengling Traditional Lager, the amber lager from Pottsville, Pennsylvania's D.G. Yuengling & Son, America's oldest brewery, sold at Beer-A-Rama in Levittown, PA.",
    faqs_extra=[
        ("Is Yuengling brewed in Pennsylvania?",
         "Yes. Yuengling has been brewed in Pottsville, Pennsylvania since 1829, making it America's oldest brewing company."),
        ("What kind of beer is Yuengling Traditional Lager?",
         "It's an amber lager — smooth, slightly sweet and easy to drink, with a balanced finish. It's Yuengling's flagship beer."),
    ],
    related=[("Miller Lite", "miller-lite"), ("Bud Light", "bud-light"), ("Coors Light", "coors-light")],
    verify="Yuengling 1829 founding / America's oldest brewery / Pottsville; Traditional Lager ABV, calories and carbs (specs left as placeholders); pack sizes and kegs carried (and whether you carry Yuengling Light or other varieties).",
)

WHITE_CLAW = make(
    "White Claw", "white-claw", "RTD", RTD_PACKS,
    hook="the hard seltzer everyone reaches for first",
    scene="stocking the cooler for the beach, planning a Levittown pool party, or grabbing something light for a get-together",
    about="White Claw Hard Seltzer is a crisp, clean, lightly carbonated hard seltzer with a hint of real fruit flavor. Light, refreshing and easy to drink, it's the go-to RTD for pool days, beach trips and backyard parties.",
    specs=[("Type", "Hard Seltzer"), ("ABV", "5%"), ("Calories", "100 per 12 oz"), ("Gluten-Free", "Yes")],
    history="White Claw launched in 2016 and took off in the summer of 2019, turning hard seltzer into one of the biggest categories in the beverage world. Its simple formula — seltzer water, a gluten-free alcohol base and a touch of fruit flavor — is still the standard for RTD seltzers.",
    pairings="White Claw is light and refreshing enough to go with almost anything: grilled chicken, tacos, salads, sushi, chips and fruit. Serve it ice cold — we chill everything to 37°F daily, so it's ready to go.",
    occasions=[("Shore Weekends", "Load the cooler with cold White Claw variety packs on your way to the beach."),
               ("Pool &amp; Patio Days", "Light, refreshing and easy to keep cold all afternoon."),
               ("Summer Cookouts", "A lighter option to sit alongside the beer at any Levittown cookout."),
               ("Parties &amp; Showers", "Variety packs let everyone pick a favorite flavor.")],
    spec_answer="A 12 oz White Claw has 100 calories, 2 g of carbs and 5% ABV.",
    schema_desc="White Claw Hard Seltzer: a gluten-free hard seltzer with 100 calories and 5% ABV, sold at Beer-A-Rama in Levittown, PA.",
    faqs_extra=[
        ("Is White Claw gluten-free?", "Yes. White Claw Hard Seltzer is gluten-free."),
        ("What flavors of White Claw do you carry?",
         "[[CONFIRM flavors in stock, e.g. Mango, Black Cherry, Lime, Ruby Grapefruit, Watermelon]] Call " + PHONE + " and we'll tell you what's cold and ready."),
    ],
    related=[("High Noon", "high-noon"), ("Truly", "truly")],
    verify="White Claw 2016 launch / 2019 boom; 100 cal / 2g carbs / 5% ABV; gluten-free; flavors and pack sizes carried.",
)

HIGH_NOON = make(
    "High Noon", "high-noon", "RTD", RTD_PACKS,
    hook="a fruit-forward pick for any Levittown get-together",
    scene="stocking the cooler for the beach, planning a Levittown pool party, or grabbing something fruity for a get-together",
    about="High Noon is a sparkling, real-fruit-juice hard seltzer-style drink that comes in bright, refreshing flavors. Light on calories and big on fruit flavor, it's a favorite for summer days, beach weekends and backyard gatherings.",
    specs=[("Type", "Hard Seltzer"), ("ABV", "[[4.5% — VERIFY]]"), ("Calories", "[[100 per 12 oz — VERIFY]]"), ("Made With", "Real Fruit Juice")],
    history="High Noon launched in 2019 from Sun Sips and quickly became one of the most popular RTDs, known for its real fruit juice flavors and its sun-and-seltzer branding. Its fruity, easy-drinking profile has made it a summer staple.",
    pairings="High Noon's fruit-forward flavors go with grilled chicken, tacos, salads, chips and fresh fruit. Serve it ice cold — we chill everything to 37°F daily, so it's party-ready the moment you walk out.",
    occasions=[("Shore Weekends", "A cold variety pack is the ideal beach-day cooler addition."),
               ("Pool &amp; Patio Days", "Fruity, light and easy to keep cold all afternoon."),
               ("Summer Cookouts", "A fruity alternative to go with the beer at any Levittown cookout."),
               ("Parties &amp; Showers", "Bright, colorful flavors that fit right in at a party.")],
    spec_answer="[[VERIFY: High Noon ABV and calories per 12 oz for the version you carry — confirm before publishing.]]",
    schema_desc="High Noon, a sparkling real-fruit-juice hard seltzer-style drink, sold at Beer-A-Rama in Levittown, PA.",
    faqs_extra=[
        ("What is High Noon?",
         "High Noon is a sparkling, real-fruit-juice hard seltzer-style drink that comes in flavors like Peach, Watermelon and Pineapple. [[CONFIRM flavors carried]]"),
        ("What flavors of High Noon do you carry?",
         "[[CONFIRM flavors in stock]] Call " + PHONE + " and we'll tell you what's cold and ready."),
    ],
    related=[("White Claw", "white-claw"), ("Truly", "truly")],
    verify="IMPORTANT: confirm Beer-A-Rama actually sells High Noon. In Pennsylvania, spirits-based drinks are generally sold only at state Fine Wine & Good Spirits stores; beer distributors sell malt beverages. Only publish this page if you carry a malt-based version, and fix the 'what is High Noon' FAQ and specs to match. Also verify 2019 launch, ABV, calories, flavors, pack sizes.",
)

TRULY = make(
    "Truly", "truly", "RTD", RTD_PACKS,
    hook="a fruit-flavored favorite for any Levittown get-together",
    scene="stocking the cooler for the beach, planning a Levittown pool party, or grabbing something fruity for a get-together",
    about="Truly Hard Seltzer is a bright, refreshing seltzer made with real fruit flavors and a clean finish. With low sugar and plenty of flavor, it's a popular choice for summer days, beach weekends and backyard parties.",
    specs=[("Type", "Hard Seltzer"), ("ABV", "5%"), ("Calories", "100 per 12 oz"), ("Made By", "Boston Beer Co.")],
    history="Truly was launched by the Boston Beer Company, the makers of Samuel Adams, in 2016. Built around fruit flavors and variety packs, it helped make hard seltzer one of the biggest RTD categories in America.",
    pairings="Truly's fruity, crisp flavors go with grilled chicken, tacos, salads, chips and fresh fruit. Serve it ice cold — we chill everything to 37°F daily, so it's ready to go the moment you leave the store.",
    occasions=[("Shore Weekends", "Load up on cold Truly variety packs on your way to the beach."),
               ("Pool &amp; Patio Days", "Bright, fruity and refreshing all afternoon."),
               ("Summer Cookouts", "A light, fruity option alongside the beer at any Levittown cookout."),
               ("Parties &amp; Showers", "Variety packs give every guest a flavor to love.")],
    spec_answer="A 12 oz Truly has 100 calories, 2 g of carbs and 5% ABV.",
    schema_desc="Truly Hard Seltzer from the Boston Beer Company: a fruit-flavored hard seltzer with 100 calories and 5% ABV, sold at Beer-A-Rama in Levittown, PA.",
    faqs_extra=[
        ("Who makes Truly Hard Seltzer?", "Truly is made by the Boston Beer Company, the brewer of Samuel Adams."),
        ("What flavors of Truly do you carry?",
         "[[CONFIRM flavors in stock, e.g. Wild Berry, Strawberry Lemonade, Pineapple]] Call " + PHONE + " and we'll tell you what's cold and ready."),
    ],
    related=[("White Claw", "white-claw"), ("High Noon", "high-noon")],
    verify="Truly 2016 launch / Boston Beer Company; 100 cal / 2g carbs / 5% ABV; flavors and pack sizes carried.",
)

BRANDS = [MILLER_LITE, BUD_LIGHT, COORS_LIGHT, YUENGLING, WHITE_CLAW, HIGH_NOON, TRULY]
