"""Four Danish carousels, 17 to 23 November 2026, each ending on the Black Friday offer and on what is
coming to Nesso (founder, 2026-11-16). Made for the Danish account only: new photos that no Nesso
account has posted, after the research in nesso_mobile/reports/Danish company Instagram tactics.md
found the copied Reels kept @nesso_danmark out of recommendations.

Figures, and where each one is from:
- m² prices: Finans Danmark, Boligmarkedsstatistikken, tabel BM011, the realised price per m² of
  ejerlejligheder in 2. kvartal 2026, as published for Nesso's postcode map
  (data.nesso.fit/area/<city>/202612/postcode-money.json, read 2026-11-16): 1800-1999 Frederiksberg C
  92.161 kr., 8000 Aarhus C 53.148 kr., 5000 Odense C 27.235 kr., 9000 Aalborg 22.685 kr.,
  2200 København N 83.515 kr. Frederiksberg C is 4,06 times Aalborg.
- costs on 3 mio. kr.: the live Danish calculator (nesso.fit/da/omkostninger-ved-boligkoeb): skøde
  19.850 kr., pantebrev realkredit 31.825 kr., pantebrev bank 7.525 kr., 59.200 kr. in all.
- viewing steps: the live checklist (nesso.fit/da/tjekliste-fremvisning), word for word.
- seller cards: Prepare's Danish text as a Danish reader sees it (nesso_mobile src/content/prepare/items.ts).
- the offer: two months of Full (49 kr. a month) for an account made in the app by 1 December
  (nesso_mobile src/lib/welcome-gift.ts, src/content/welcome-gift.ts). The Android app is in Google Play;
  the iPhone app is not out, so the slide says so.

Photos: Pexels License, ~/Documents/GitHub/nesso-assets/pexels-photos/ (2026-11-03/ and 2026-11-16/).
Carousels published through the API carry no music: Instagram adds music to a carousel only in the app.
"""

P = "~/Documents/GitHub/nesso-assets/pexels-photos/"
A = P + "2026-11-03/"
B = P + "2026-11-16/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-da/"
HINT = "Swipe  →"
SW = 1080


def at(day):
    return f"2026-11-{day:02d}T18:00+01:00"


def coming(x):
    """What is coming to Nesso (founder, 2026-11-16)."""
    return [
        {"x": x + 96, "y": 190, "lines": [("Snart i Nesso", "orange", 64)]},
        {"x": x + 96, "y": 360, "lines": [("Flyt møblerne.", "white", 72), ("Prøv en ny vægfarve.", "white", 72),
                                          ("Se det i dit eget rum,", "violet", 72), ("i 3D.", "violet", 72)]},
    ]


def black_friday(x):
    """The offer, the last slide of every carousel."""
    return [
        {"x": x + 96, "y": 130, "lines": [("BLACK FRIDAY", "orange", 64)]},
        {"x": x + 96, "y": 290, "lines": [("2 måneder", "white", 120), ("med Full, gratis", "violet", 84)]},
        {"x": x + 96, "y": 660, "lines": [("Hent appen, og opret en konto", "white", 46), ("senest 1. december.", "white", 46),
                                          ("En værdi af 98 kr. Intet kort.", "white", 46)]},
        {"x": x + 96, "y": 990, "lines": [("Link i bio  →", "orange", 60), ("Android nu, iPhone på vej", "white", 40)]},
    ]


def mark(x):
    return {"x": x + 540, "y": 1195, "height": 110, "word": "white"}


def answer(x, price, place):
    return {"x": x + 96, "y": 150, "lines": [(price, "violet", 150), (f"pr. m², {place}", "white", 52)]}


def question(x, place):
    return {"x": x + 96, "y": 860, "lines": [(place, "white", 84), ("Dit gæt?", "violet", 60)]}


GAET = {"slides": 9, "hint_text": HINT, "photos": [
    {"file": B + "11627141.jpg", "x": 0, "focus": 0.5},
    {"file": B + "11801511.jpg", "x": 1400, "focus": 0.5},
    {"file": B + "8404920.jpg", "x": 2500, "focus": 0.5},
    {"file": B + "14872654.jpg", "x": 3600, "focus": 0.45},
    {"file": B + "29144713.jpg", "x": 4700, "focus": 0.5},
    {"file": B + "35926276.jpg", "x": 6100, "focus": 0.4},
    {"file": B + "19866401.jpg", "x": 7500, "focus": 0.4},
    {"file": P + "36767137.jpg", "x": 8640, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 150, "lines": [("Gæt m²-prisen", "white", 110), ("Ejerlejligheder, solgt i", "white", 48),
                                  ("2. kvartal 2026", "white", 48)]},
    {"x": 96, "y": 860, "lines": [("Frederiksberg C", "white", 84), ("Dit gæt?", "violet", 60)]},
    answer(SW, "92.161 kr.", "Frederiksberg C"), question(SW, "8000 Aarhus C"),
    answer(2 * SW, "53.148 kr.", "Aarhus C"), question(2 * SW, "5000 Odense C"),
    answer(3 * SW, "27.235 kr.", "Odense C"), question(3 * SW, "9000 Aalborg"),
    answer(4 * SW, "22.685 kr.", "Aalborg"), question(4 * SW, "2200 København N"),
    answer(5 * SW, "83.515 kr.", "København N"),
    {"x": 5 * SW + 96, "y": 800, "lines": [("Frederiksberg C:", "white", 64), ("over 4 gange", "violet", 96),
                                           ("prisen i Aalborg.", "white", 64)]},
    {"x": 6 * SW + 96, "y": 130, "lines": [("Se dit postnummer", "white", 76), ("på kortet i Nesso.", "violet", 76)]},
    {"x": 6 * SW + 96, "y": 1250, "lines": [("Kilde: Finans Danmark, tabel BM011", "white", 32)]},
    *coming(7 * SW),
    *black_friday(8 * SW),
  ],
  "phones": [{"mock": M + "03-investering.png", "x": 6 * SW + 540, "y": 400, "height": 820, "tilt": -4}],
  "mark": mark(8 * SW),
}

OVENI = {"slides": 7, "hint_text": HINT, "photos": [
    {"file": A + "7647387.jpg", "x": 0, "focus": 0.55},
    {"file": B + "35617573.jpg", "x": 1300, "focus": 0.5},
    {"file": A + "7534561.jpg", "x": 2400, "focus": 0.5},
    {"file": A + "6312358.jpg", "x": 3500, "focus": 0.5},
    {"file": P + "5998120.jpg", "x": 5300, "focus": 0.5},
    {"file": B + "36722460.jpg", "x": 6480, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 150, "lines": [("Bolig til 3 mio. kr.?", "white", 88)]},
    {"x": 300, "y": 330, "lines": [("Det koster oveni.", "violet", 110)], "cross": True},
    {"x": SW + 96, "y": 700, "lines": [("Tinglysning af skødet", "white", 60), ("19.850 kr.", "violet", 150),
                                       ("1.850 kr. plus 0,6 % af prisen", "white", 46)]},
    {"x": 2 * SW + 96, "y": 150, "lines": [("Pantebrev, realkredit", "white", 60), ("31.825 kr.", "violet", 150),
                                           ("for et lån på 2,4 mio. kr.", "white", 46)]},
    {"x": 3 * SW + 96, "y": 700, "lines": [("Pantebrev, banklån", "white", 60), ("7.525 kr.", "violet", 150),
                                           ("for et lån på 450.000 kr.", "white", 46)]},
    {"x": 4 * SW + 96, "y": 120, "lines": [("I alt oveni:", "white", 72), ("59.200 kr.", "violet", 130)]},
    {"x": 4 * SW + 96, "y": 1230, "lines": [("Kun statens afgifter. Rådgiver og forsikring kommer til.", "white", 30)]},
    *coming(5 * SW),
    *black_friday(6 * SW),
  ],
  "phones": [{"mock": M + "04-omkostninger.png", "x": 4 * SW + 640, "y": 440, "height": 760, "tilt": -4}],
  "mark": mark(6 * SW),
}

FOER = {"slides": 8, "hint_text": HINT, "photos": [
    {"file": A + "7937326.jpg", "x": 0, "focus": 0.45},
    {"file": A + "7937330.jpg", "x": 1600, "focus": 0.5},
    {"file": A + "8962575.jpg", "x": 3400, "focus": 0.5},
    {"file": A + "6527037.jpg", "x": 4900, "focus": 0.5},
    {"file": A + "5793547.jpg", "x": 6480, "focus": 0.5},
    {"file": B + "18531489.jpg", "x": 7560, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 150, "lines": [("Læg telefonen", "white", 100), ("på gulvet,", "white", 100)]},
    {"x": 360, "y": 470, "lines": [("før du byder.", "violet", 110)], "cross": True},
    {"x": SW + 96, "y": 700, "lines": [("Gulvets hældning", "violet", 84), ("Telefonen midt i rummet,", "white", 46),
                                       ("skærmen opad. Lad den måle.", "white", 46), ("Drej en halv omgang. Mål igen.", "white", 46)]},
    {"x": 2 * SW + 96, "y": 150, "lines": [("Støj", "violet", 96), ("Telefonen midt i rummet.", "white", 46),
                                           ("30 sek. med vinduet åbent,", "white", 46), ("30 sek. lukket.", "white", 46)]},
    {"x": 3 * SW + 96, "y": 700, "lines": [("Dagslys", "violet", 96), ("Sluk lyset i rummet.", "white", 46),
                                           ("Mål ved vindueskarmen,", "white", 46), ("midt i rummet og ved bagvæggen.", "white", 46)]},
    {"x": 4 * SW + 96, "y": 150, "lines": [("Vandtryk", "violet", 96), ("Åbn køkkenhanen helt.", "white", 46),
                                           ("Tænd også for bruseren.", "white", 46), ("Se på strålen i køkkenet.", "white", 46)]},
    {"x": 5 * SW + 96, "y": 120, "lines": [("81 tjek i Nesso.", "white", 76), ("Hvert siger også, hvad", "violet", 50),
                                           ("det ikke fastslår.", "violet", 50)]},
    *coming(6 * SW),
    *black_friday(7 * SW),
  ],
  "phones": [{"mock": M + "08-maal-gulv.png", "x": 5 * SW + 560, "y": 480, "height": 780, "tilt": -4}],
  "mark": mark(7 * SW),
}

SAELGER = {"slides": 8, "hint_text": HINT, "photos": [
    {"file": P + "34916291.jpg", "x": 0, "focus": 0.5},
    {"file": B + "35617573.jpg", "x": 1300, "focus": 0.6},
    {"file": P + "35657824.jpg", "x": 2400, "focus": 0.5},
    {"file": A + "6527037.jpg", "x": 3500, "focus": 0.3},
    {"file": P + "5998120.jpg", "x": 4600, "focus": 0.3},
    {"file": B + "36722460.jpg", "x": 5700, "focus": 0.5},
    {"file": B + "19866401.jpg", "x": 6700, "focus": 0.6},
    {"file": B + "772177.jpg", "x": 7560, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 150, "lines": [("Sælger du", "white", 110), ("din bolig?", "white", 110)]},
    {"x": 380, "y": 560, "lines": [("Før fremvisningen:", "violet", 90)], "cross": True},
    {"x": SW + 96, "y": 740, "lines": [("Energimærke", "violet", 96), ("Bedre mærker blev solgt", "white", 46),
                                       ("dyrere i Danmark.", "white", 46), ("Sæt det forrest i annoncen.", "white", 46)]},
    {"x": 2 * SW + 96, "y": 150, "lines": [("Rene vinduer", "violet", 96), ("Vask dem, indvendigt", "white", 46),
                                           ("og udvendigt.", "white", 46), ("Træk gardinerne fra.", "white", 46)]},
    {"x": 3 * SW + 96, "y": 760, "lines": [("Den lyseste time", "violet", 90), ("Læg fremvisninger,", "white", 46),
                                           ("når solen står ind.", "white", 46)]},
    {"x": 4 * SW + 96, "y": 150, "lines": [("Lav baggrundsstøj", "violet", 88), ("Sluk tv og vaskemaskine.", "white", 46),
                                           ("Luk mod trafikken.", "white", 46)]},
    {"x": 5 * SW + 96, "y": 700, "lines": [("Kaffeduft?", "white", 110), ("Pris: ikke påvist.", "violet", 80)]},
    {"x": 5 * SW + 96, "y": 1230, "lines": [("Kilderne står i Nesso, under Forbered.", "white", 34)]},
    *coming(6 * SW),
    *black_friday(7 * SW),
  ],
  "mark": mark(7 * SW),
}

OFFER = ("BLACK FRIDAY: Hent Nesso-appen, og opret en konto senest 1. december, så får du 2 måneder med Full "
         "gratis, en værdi af 98 kr. Intet kort. Appen findes til Android nu, iPhone er på vej. Link i bio.\n\n"
         "Snart i Nesso: flyt møblerne, prøv en ny vægfarve, og se det i dit eget rum i 3D.")

CAPTIONS = {
    "gaet-m2-prisen": ("Gæt m²-prisen, før du swiper. Hvor tæt kom du?\n\n"
                       "Realiserede priser pr. m² for ejerlejligheder, solgt i 2. kvartal 2026: Frederiksberg C 92.161 kr., "
                       "København N 83.515 kr., Aarhus C 53.148 kr., Odense C 27.235 kr., Aalborg 22.685 kr. "
                       "Dit eget postnummer står på kortet i Nesso.\n"
                       "Kilde: Finans Danmark, Boligmarkedsstatistikken, tabel BM011.\n\n"
                       + OFFER + "\n\n"
                       "Hvilket postnummer skal vi tage næste gang? Skriv det i kommentarerne 👇\n\n"
                       "#boligpriser #kvadratmeterpris #ejerlejlighed #boligkøb #blackfriday"),
    "koster-oveni": ("En bolig til 3 mio. kr. koster mere end 3 mio. kr. Swipe.\n\n"
                     "Eksemplet er fra Nessos beregner: 5 % i udbetaling, et realkreditlån på 2.400.000 kr. og et banklån på 450.000 kr. "
                     "Tinglysning af skødet 19.850 kr., af pantebrevet for realkreditlånet 31.825 kr. og af pantebrevet for banklånet 7.525 kr.: "
                     "59.200 kr. oven i prisen. Rådgiver og ejerskifteforsikring kommer til, så bed om skriftlige tilbud.\n"
                     "Kilde: tinglysningsafgiftsloven, satserne fra 1. januar 2026. En beregning, ikke rådgivning.\n\n"
                     + OFFER + "\n\n"
                     "Gem den, før du skriver under 📌\n\n"
                     "#boligkøb #førstebolig #tinglysning #boliglån #blackfriday"),
    "foer-du-byder": ("Fire ting, du kan måle med telefonen til fremvisningen: gulvets hældning, støj, dagslys og vandtryk. Swipe.\n\n"
                      "Trinene er fra Nessos tjekliste med 81 tjek. Hvert tjek siger også, hvad det ikke kan fastslå.\n\n"
                      + OFFER + "\n\n"
                      "Hvad tjekker du først? Skriv det i kommentarerne 👇\n\n"
                      "#fremvisning #boligjagt #huskøb #førstebolig #blackfriday"),
    "saelger-du": ("Sælger du din bolig? Fire ting før fremvisningen, og én myte. Swipe.\n\n"
                   "Energimærket: bedre mærker blev solgt dyrere i Danmark, og mærket skal stå i annoncen. "
                   "Rene vinduer og gardinerne fra. Fremvisning i den lyseste time. Ingen baggrundsstøj. "
                   "Og kaffeduften: den løfter humøret, men ingen undersøgelse har fundet den i prisen. "
                   "Kilderne står i Nesso under Forbered.\n\n"
                   + OFFER + "\n\n"
                   "Send den til en, der skal sælge 📌\n\n"
                   "#sælgbolig #boligsalg #energimærke #boligstyling #blackfriday"),
}

ITEMS = [
    {"id": f"dk-bf-0{i}", "type": "carousel", "channel": "ig-dk", "at": at(day), "slug": f"karrusel-{name}",
     "panorama": spec, "caption": CAPTIONS[name]}
    for i, (day, name, spec) in enumerate([(17, "gaet-m2-prisen", GAET), (19, "koster-oveni", OVENI),
                                          (21, "foer-du-byder", FOER), (23, "saelger-du", SAELGER)], 1)
]
