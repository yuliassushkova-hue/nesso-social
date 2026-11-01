"""The Danish account's four carousels, 9 to 15 November: the Italian seamless carousels of
2 November (weeks/2026-11-02-carousels.py), translated, on the same photos and the same layout. Only
the opening sentence and one phone cross a cut; the last slide ends on "Prøv Nesso" with the logo on
the photo.

Costs use the live Danish calculator's own example, the one on the phone (nesso.fit/da/
omkostninger-ved-boligkoeb, run 2026-11-01): 3.000.000 kr., 5 % own payment, realkreditlån 2.400.000 kr.,
banklån 450.000 kr. Skøde 19.850 kr., pantebrev realkredit 31.825 kr., pantebrev bank 7.525 kr.:
59.200 kr. over the price. The loan facts are on the same page: realkredit up to 80 % of the value,
at least 5 % own payment, Finanstilsynet's debt-factor line, withdrawal within 6 hverdage at 1 %.
The myths are the Prepare sources (nesso_mobile CLAUDE.md §8ap).
Photos: Pexels License, ~/Documents/GitHub/nesso-assets/pexels-photos/<id>.jpg. The same photos as the
Italian week, except the three with euro notes in them (30139520, 16600134, 29034871): a Danish cost post
showing €200 beside a kroner figure reads as wrong, so those slots take money-free photos from the set.

Replaced: "costi" (Italian taxes on €250.000) by the Danish fees on 3 mio. kr.; "mutuo" (the PIES and
Banca d'Italia's mortgage rights) by the Danish loan facts above. "visita" and "miti" are translated.
"""

F = "~/Documents/GitHub/nesso-assets/pexels-photos/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-da/"
HINT = "Swipe  →"


def at(day):
    return f"2026-11-{day:02d}T18:00+01:00"


def end(x, first, second):
    """The last slide: the thought, the call, the logo on the photo."""
    return [
        {"x": x + 96, "y": 150, "lines": [(first, "white", 84), (second, "violet", 76)]},
        {"x": x + 96, "y": 700, "lines": [("Prøv Nesso  →", "orange", 84), ("link i bio", "white", 52)]},
    ]


OMKOSTNINGER = {"slides": 7, "hint_text": HINT, "photos": [
    {"file": F + "4307963.jpg", "x": 0, "focus": 0.5},
    {"file": F + "36729696.jpg", "x": 1700, "focus": 0.5},
    {"file": F + "6077368.jpg", "x": 3400, "focus": 0.5},
    {"file": F + "12932887.jpg", "x": 5100, "focus": 0.35},
    {"file": F + "7579192.jpg", "x": 6700, "focus": 0.3},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Boligen er fundet: 3 mio. kr.", "white", 62)]},
    {"x": 420, "y": 330, "lines": [("Men hvad betaler du egentlig?", "violet", 92)], "cross": True},
    {"x": 1176, "y": 720, "lines": [("Tinglysning af skødet", "white", 64), ("19.850 kr.", "violet", 150), ("1.850 kr. plus 0,6 % af prisen", "white", 50)]},
    {"x": 2256, "y": 170, "lines": [("Pantebrev, realkredit", "white", 64), ("31.825 kr.", "violet", 150), ("for et lån på 2,4 mio. kr.", "white", 50)]},
    {"x": 3540, "y": 170, "lines": [("Pantebrev, banklån", "white", 60), ("7.525 kr.", "violet", 130), ("for et lån på 450.000 kr.", "white", 50)]},
    {"x": 4416, "y": 560, "lines": [("Oven i prisen:", "white", 84), ("59.200 kr.", "violet", 130), ("kun statens afgifter", "white", 50)]},
    {"x": 5496, "y": 150, "lines": [("Og advokaten?", "white", 104)]},
    {"x": 5496, "y": 420, "lines": [("Ingen regel", "violet", 80), ("sætter prisen.", "violet", 80)]},
    {"x": 5496, "y": 800, "lines": [("Bed om et skriftligt", "white", 64), ("tilbud fra flere.", "white", 64)]},
    *end(6480, "Regn det ud", "på din pris."),
  ],
  "phones": [{"mock": M + "04-omkostninger.png", "x": 3240, "y": 330, "height": 980, "tilt": -4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

FREMVISNING = {"slides": 8, "hint_text": HINT, "photos": [
    {"file": F + "19916712.jpg", "x": 0, "focus": 0.5},
    {"file": F + "12932887.jpg", "x": 1400, "focus": 0.35},
    {"file": F + "6077368.jpg", "x": 2800, "focus": 0.5},
    {"file": F + "8092188.jpg", "x": 4300, "focus": 0.4},
    {"file": F + "4010280.jpg", "x": 5900, "focus": 0.5},
    {"file": F + "4307929.jpg", "x": 7300, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 150, "lines": [("Fremvisning:", "white", 96), ("20 minutter.", "white", 96)]},
    {"x": 470, "y": 420, "lines": [("30 år med lån.", "violet", 110)], "cross": True},
    {"x": 1176, "y": 680, "lines": [("Støj", "violet", 110), ("Vinduet åbent, så lukket.", "white", 58), ("30 sekunder hver.", "white", 58)]},
    {"x": 2256, "y": 170, "lines": [("Lys", "violet", 110), ("Ved bagvæggen,", "white", 60), ("ikke i vindueskarmen.", "white", 60)]},
    {"x": 3336, "y": 170, "lines": [("Gulv", "violet", 100), ("Telefonen på gulvet.", "white", 60), ("Mål, drej, mål igen.", "white", 60)]},
    {"x": 4620, "y": 170, "lines": [("Fugt", "violet", 100), ("Kig forneden,", "white", 60), ("i hjørnerne,", "white", 60), ("bag møblerne.", "white", 60)]},
    {"x": 5496, "y": 640, "lines": [("Vand", "violet", 110), ("Åbn køkken og bruser", "white", 60), ("samtidig.", "white", 60), ("Se på strålen.", "white", 60)]},
    {"x": 6576, "y": 170, "lines": [("Under vasken", "violet", 96), ("Lommelygten tændt:", "white", 60), ("en finger på hver samling.", "white", 56)]},
    *end(7560, "81 tjek", "til din fremvisning."),
  ],
  "phones": [{"mock": M + "08-maal-gulv.png", "x": 4320, "y": 400, "height": 920, "tilt": -4}],
  "mark": {"x": 8100, "y": 1110, "height": 150, "word": "white"},
}

MYTER = {"slides": 7, "hint_text": HINT, "photos": [
    {"file": F + "8482895.jpg", "x": 0, "focus": 0.35},
    {"file": F + "19916712.jpg", "x": 1500, "focus": 0.5},
    {"file": F + "8092188.jpg", "x": 3200, "focus": 0.45},
    {"file": F + "6077368.jpg", "x": 4900, "focus": 0.5},
    {"file": F + "7579192.jpg", "x": 6400, "focus": 0.3},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Skal du sælge?", "white", 110)]},
    {"x": 330, "y": 360, "lines": [("»Lav kaffe før fremvisningen.«", "violet", 80)], "cross": True},
    {"x": 1176, "y": 720, "lines": [("En højere pris?", "white", 64), ("Ingen undersøgelse", "violet", 84), ("viser det.", "violet", 84)]},
    {"x": 2256, "y": 170, "lines": [("»Spil klassisk musik.«", "white", 68)]},
    {"x": 2256, "y": 700, "lines": [("I butikker hjælper det lidt.", "white", 56), ("På bud på en bolig:", "white", 60), ("intet bevis.", "violet", 90)]},
    {"x": 3336, "y": 170, "lines": [("»Tøm den, så virker", "white", 70), ("den større.«", "white", 70)]},
    {"x": 3336, "y": 700, "lines": [("Med møbler virkede", "white", 58), ("rummet lidt mindre.", "white", 58), ("I virtual reality:", "white", 58), ("ingen forskel.", "violet", 76)]},
    {"x": 4416, "y": 170, "lines": [("»Boligstyling", "white", 70), ("hæver prisen.«", "white", 70)]},
    {"x": 4416, "y": 640, "lines": [("I forsøget virkede", "white", 56), ("boligen mere", "white", 56), ("beboelig.", "white", 56), ("Den anslåede værdi", "violet", 64), ("var den samme.", "violet", 64)]},
    {"x": 5720, "y": 170, "lines": [("Hvad tæller,", "white", 84), ("ifølge forskningen:", "white", 70)]},
    {"x": 5720, "y": 560, "lines": [("energimærke,", "violet", 62), ("lys, ro,", "violet", 62), ("en terrasse.", "violet", 62)]},
    *end(6480, "Gør boligen klar", "ud fra forskningen."),
  ],
  "phones": [{"mock": M + "05-forbered.png", "x": 5400, "y": 400, "height": 920, "tilt": 4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

LAAN = {"slides": 7, "hint_text": HINT, "photos": [
    {"file": F + "7579211.jpg", "x": 0, "focus": 0.5},
    {"file": F + "36729696.jpg", "x": 1700, "focus": 0.5},
    {"file": F + "4010280.jpg", "x": 3400, "focus": 0.5},
    {"file": F + "8368754.jpg", "x": 5100, "focus": 0.6},
    {"file": F + "4307929.jpg", "x": 6600, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Til møde i banken.", "white", 78)]},
    {"x": 380, "y": 330, "lines": [("Hvad skal du vide først?", "violet", 96)], "cross": True},
    {"x": 1176, "y": 680, "lines": [("80 %", "violet", 120), ("højst, i realkreditlån", "white", 60), ("af boligens værdi.", "white", 60), ("Resten er typisk et banklån.", "white", 52)]},
    {"x": 2256, "y": 170, "lines": [("5 %", "violet", 130), ("betaler du mindst", "white", 60), ("selv i udbetaling.", "white", 60)]},
    {"x": 3540, "y": 170, "lines": [("Gældsfaktor", "violet", 76), ("din gæld delt med", "white", 60), ("din indkomst før skat.", "white", 56)]},
    {"x": 4416, "y": 640, "lines": [("Over 4", "violet", 96), ("er højt, siger", "white", 60), ("Finanstilsynet", "white", 60), ("som udgangspunkt.", "white", 50)]},
    {"x": 5496, "y": 170, "lines": [("Fortryd købet?", "white", 84), ("6 hverdage.", "white", 84)]},
    {"x": 5496, "y": 640, "lines": [("1 % af prisen,", "violet", 76), ("betalt til sælger:", "white", 60), ("30.000 kr. på 3 mio.", "white", 60)]},
    *end(6480, "Ydelse og afgifter", "på din pris."),
  ],
  "phones": [{"mock": M + "04-omkostninger.png", "x": 3240, "y": 330, "height": 980, "tilt": -4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

CAPTIONS = {
    "omkostninger": ("Første bolig: hvad betaler du oven i prisen? Swipe.\n\n"
                     "Eksemplet er fra Nessos beregner: en ejerbolig til 3.000.000 kr., 5 % i udbetaling, et realkreditlån på 2.400.000 kr. og et banklån på 450.000 kr. "
                     "Tinglysning af skødet 19.850 kr., af pantebrevet for realkreditlånet 31.825 kr. og af pantebrevet for banklånet 7.525 kr.: 59.200 kr. oven i prisen.\n\n"
                     "Rådgiver, ejerskifteforsikring og lånenes egne gebyrer kommer oveni. Ingen regel fastsætter dem, så bed om skriftlige tilbud.\n\n"
                     "Prøv Nesso: link i bio. Det er en beregning efter de gældende satser, ikke rådgivning.\n"
                     "Kilde: tinglysningsafgiftsloven (LBK nr. 307/2025 §§ 4 og 5 a), satserne fra 1. januar 2026.\n\n"
                     "Hvilken udgift overraskede dig mest? Skriv det i kommentarerne 👇\n"
                     "Gem den, før du skriver under 📌\nSend den til en, der skal købe bolig.\n\n"
                     "#boligkøb #førstebolig #boliglån #realkredit #bolig"),
    "fremvisning": ("En fremvisning tager tyve minutter. Lånet, tredive år. Swipe.\n\n"
                    "Støj, lys, gulv, fugt, vand, under vasken: seks tjek, du laver ved fremvisningen, mange med telefonen i hånden. "
                    "I Nessos tjekliste er der 81, og hvert af dem siger også, hvad det ikke kan fastslå.\n\n"
                    "Og en regel om penge: ingen penge, før du har set boligen selv.\n\n"
                    "Prøv Nesso: link i bio.\n\n"
                    "Hvad kigger du først efter i en bolig? Skriv det i kommentarerne 👇\n"
                    "Gem den til næste fremvisning 📌\nSend den til en, der leder efter bolig.\n\n"
                    "#boligjagt #fremvisning #førstebolig #lejebolig #boligkøb"),
    "myter": ("Kaffe, musik, boligstyling, tomme rum: vi har ledt efter undersøgelserne bag de råd, man oftest hører, når man skal sælge. Swipe.\n\n"
              "Kaffe: en metaanalyse af 55 artikler om duft i butikker og på hoteller. Musik: 32 undersøgelser i butikker. "
              "Boligstyling: forsøget af Lane, Seiler og Seiler. Tomme rum: en test med en model og en i virtual reality.\n\n"
              "I Nesso deler Forbered rådene i tre grupper: det, forskningen har set i prisen, det, der hjælper en værdi, der allerede er der, med at blive set, og det, der kun ændrer fremvisningen.\n\n"
              "Prøv Nesso: link i bio.\n\n"
              "Hvilket råd har du hørt oftest? Skriv det i kommentarerne 👇\n"
              "Gem den, hvis du sælger eller udlejer 📌\nSend den til en, der gør sin bolig klar.\n\n"
              "#sælgbolig #boligsalg #boligstyling #indretning #bolig"),
    "laan": ("Før du låner til en bolig: det skal du vide. Swipe.\n\n"
             "Realkreditlån på højst 80 % af boligens værdi, mindst 5 % i udbetaling og typisk et banklån til resten. "
             "Din gældsfaktor er din gæld delt med indkomsten før skat, og Finanstilsynet anser som udgangspunkt en gældsfaktor over fire som høj. "
             "Og du kan som udgangspunkt fortryde købet inden for 6 hverdage mod at betale sælger 1 % af købesummen.\n\n"
             "Ydelse, afgifter og gældsfaktor på din pris står i Nessos beregner. Det er en beregning, ikke rådgivning.\n\n"
             "Prøv Nesso: link i bio.\n"
             "Kilder: lov om realkreditlån (LBK nr. 1541/2025), Finanstilsynets vejledning nr. 9458/2023, LBK nr. 1123/2015.\n\n"
             "Har du regnet din gældsfaktor ud? Skriv det i kommentarerne 👇\n"
             "Gem den til mødet i banken 📌\nSend den til en, der skal låne til bolig.\n\n"
             "#boligkøb #førstebolig #boliglån #realkredit #bolig"),
}

ITEMS = [
    {"id": f"dk-k-0{i}", "type": "carousel", "channel": "ig-dk", "at": at(day), "slug": f"karrusel-{name}",
     "panorama": spec, "caption": CAPTIONS[name]}
    for i, (day, name, spec) in enumerate([(9, "omkostninger", OMKOSTNINGER), (11, "fremvisning", FREMVISNING),
                                          (13, "myter", MYTER), (15, "laan", LAAN)], 1)
]
