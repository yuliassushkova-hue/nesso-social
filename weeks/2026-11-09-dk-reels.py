"""The Danish account's 21 Reels, 9 to 15 November: the Italian Reels of 2 November
(weeks/2026-11-02-reels.py), translated, on the same footage, music and times. 08:00 and 20:00 a chat
story, 13:00 a warm interior film with words one at a time.

Footage: Pexels License, ids are https://www.pexels.com/video/<id>/. Viewing steps and limits are the
app's own Danish text, nesso.fit/da/tjekliste-fremvisning (read 2026-11-01). Kroner figures are the
live Danish calculator, nesso.fit/da/omkostninger-ved-boligkoeb, on 3.000.000 kr. with its defaults
(5 % own payment, realkreditlån 2.400.000 kr., banklån 450.000 kr.), run 2026-11-01: skøde 19.850 kr.,
pantebrev realkredit 31.825 kr., pantebrev bank 7.525 kr., i alt 59.200 kr.; withdrawal within
6 hverdage at 1 % = 30.000 kr. The debt-factor line is Finanstilsynet's, quoted on the same page.

Replaced, because the Italian fact is Italian law or Italian money:
- Mon 20:00 "quanto-paghi" (€13.528 of Italian taxes) -> the Danish registration fees on 3 mio. kr.
- Wed 20:00 "registro" (registro on the cadastral value) -> the fee on the deed, 19.850 kr.
- Fri 08:00 "notaio" -> the buyer's adviser or lawyer, whose price no rule sets (live page).
- Fri 13:00 "chiavi": same film, the words now name Danish costs (tinglysning, lån, ydelse).
- Fri 20:00 "iva" (agency VAT) -> the 6-day right to withdraw from a home purchase.
- Sun 20:00 "mutuo" (PIES, Banca d'Italia) -> the debt factor, as Finanstilsynet frames it.
- Sun 13:00 "quartiere": "dieci città italiane" -> the five Danish cities the app covers.
"""

P = "~/Documents/GitHub/nesso-assets/pexels/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-da/"
CH = "ig-dk"
LINK = "Prøv Nesso · link i bio"
TAG_VISIT = "#boligjagt #fremvisning #førstebolig #lejebolig #boligkøb"
TAG_COST = "#boligkøb #førstebolig #boliglån #realkredit #bolig"
TAG_SELL = "#sælgbolig #boligsalg #boligstyling #indretning #bolig"
TAG_LIVE = "#københavn #aarhus #nyiby #flytning #boligjagt"
ORANGE_AV, VIOLET_AV, INK_AV = (249, 115, 22), (90, 62, 192), (52, 33, 111)


def at(day, time):
    return f"2026-11-{day:02d}T{time}+01:00"


def chat(day, time, slug, hook_clip, who, role, color, hook, thread, headline, sub, phone, caption):
    """hook: the first message, floating over real footage. thread: (from, text or clip-photo, typing)."""
    msgs, t = [{"at": 0.0, "from": "them", "text": hook}], 0.9
    for frm, content, typing in thread:
        t += typing
        m = {"at": round(t, 2), "from": frm, "typing": typing}
        if isinstance(content, dict):
            m["photo"] = content
        else:
            m["text"] = content
        msgs.append(m)
        t += 1.15 if frm == "them" else 1.0
    chat_secs = round(t + 0.6, 2)
    return {"id": f"dk-r-{slug}", "type": "reel", "channel": CH, "at": at(day, time), "slug": f"reel-{slug}",
            "scenes": [
                {"kind": "photo", "secs": 2.1, "clip": {"file": P + hook_clip[0] + ".mp4", "start": hook_clip[1]},
                 "who": who, "color": color, "bubble": hook},
                {"kind": "chat", "secs": chat_secs, "who": who, "role": role, "color": color, "messages": msgs},
                {"kind": "headline", "secs": 2.6, "text": headline, "sub": sub, "phone": M + phone},
                {"kind": "end", "secs": 2.0, "line": "Før du skriver under.", "cta": LINK},
            ], "caption": caption}


def film(day, slug, shots, caption):
    """shots: (clip id, start, secs, words, phone or None). *word* is italic."""
    clips, cards = [], []
    for clip, start, secs, words, phone in shots:
        clips.append({"file": f"{P}{clip}.mp4", "start": start, "secs": secs})
        card = {"kind": "serif", "text": words, "secs": secs}
        if "\n" in words or len(words) > 12:
            card["size"] = 124
        if phone:
            card.update({"phone": M + phone, "phone_top": 400, "phone_height": 1480, "phone_tilt": -3, "phone_dx": 0,
                         "size": 96, "text_top": True, "text_y": 0})
            card["text"] = words.replace("\n", " ")
        cards.append(card)
    clips.append({"file": P + "40187579.mp4", "start": 0.5, "secs": 2.3})
    cards.append({"kind": "brand", "sub": "Før du skriver under · link i bio", "secs": 2.3})
    music = "music-beautiful-dream" if day % 2 == 1 else "music-classical-vibes"
    return {"id": f"dk-r-{slug}", "type": "reel", "channel": CH, "at": at(day, "13:00"), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": clips, "cards": cards, "caption": caption,
            "music": music, "music_gain": 0.6, "music_start": 3.0}


def frame(clip, start=1.0):
    return {"file": P + clip + ".mp4", "start": start}


ITEMS = [
    # ---------------------------------------------------------------- Monday 9
    chat(9, "08:00", "lys", ("5853208", 0.5), "Mikkel", "Mægler", VIOLET_AV, "Lejligheden er virkelig lys ☀️",
         [("them", frame("30744460"), 0.0), ("them", "Sol hele dagen ☀️", 0.6),
          ("me", "Også bagerst i stuen?", 0.0), ("them", "Øh… næsten 😅", 0.9)],
         "Stol på det.\nMen mål det.", "Lyset ved bagvæggen, ved fremvisningen.", "06-indenfor-property-check.png",
         "»Virkelig lys.« Tæt på vinduet er alle lejligheder det.\n\nVed fremvisningen slukker du lyset og ser på bagvæggen: det er der, du kommer til at læse og arbejde. I Nessos tjekliste står der, hvordan du gør, og hvad tjekket ikke kan fortælle dig.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    film(9, "se-ordentligt", [
        ("6798992", 0.3, 1.0, "Før", None), ("6798992", 1.3, 1.1, "du *skriver under,*", None),
        ("29513615", 0.5, 1.4, "så", None), ("40134358", 0.5, 1.6, "*ordentligt efter.*", None),
        ("36300251", 0.5, 1.2, "Lyset.", None), ("31960017", 0.5, 1.2, "Stilheden.", None),
        ("6323324", 0.5, 1.2, "Hjørnerne.", None),
        ("30912265", 0.5, 2.6, "81 tjek til\n*fremvisningen.*", "06-indenfor-property-check.png"),
    ], "En fremvisning tager tyve minutter. I boligen bor du i årevis.\n\nLyset bagest i rummet, støjen med vinduet åbent, hjørnerne bag møblerne: 81 tjek til fremvisningen, mange med telefonen.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    chat(9, "20:00", "hvad-koster-den", ("13441354", 0.5), "Sofie", "Veninde", ORANGE_AV, "Nå, hvad skal du give for den? 🏠",
         [("me", "3 millioner 🙂", 0.0), ("them", "Og tinglysning af skøde og lån?", 0.7), ("me", "…😳", 0.0)],
         "59.200 kr.\noveni.", "Statens afgifter på en bolig til 3 mio. kr.", "04-omkostninger.png",
         "Prisen i annoncen er ikke alt, du betaler.\n\nEksempel fra Nessos beregner: en ejerbolig til 3.000.000 kr., et realkreditlån på 2.400.000 kr. og et banklån på 450.000 kr. Tinglysning af skødet 19.850 kr., af pantebrevet for realkreditlånet 31.825 kr. og af pantebrevet for banklånet 7.525 kr. I alt 59.200 kr., før rådgiver, ejerskifteforsikring og lånenes egne gebyrer.\n\nRegn det ud på din egen pris: Prøv Nesso, link i bio. Det er en beregning efter de gældende satser, ikke rådgivning.\nKilde: tinglysningsafgiftsloven, satserne fra 1. januar 2026.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Tuesday 10
    chat(10, "08:00", "stille", ("5835540", 0.5), "Mikkel", "Mægler", VIOLET_AV, "Meget stille kvarter 🤫",
         [("me", "Også med vinduet åbent?", 0.0), ("them", "Tja… toget kører forbi fra kl. 5 🚆", 0.9)],
         "Åbn det.\nOg mål.", "30 sekunder åbent, 30 lukket.", "07-maal-stoej-vindue.png",
         "Ved fremvisningen er vinduet næsten altid lukket. Åbn det.\n\n30 sekunder med vinduet åbent, 30 med det lukket, telefonen samme sted: Nesso sammenligner de to målinger. Selve tallet skifter fra telefon til telefon, forskellen gør ikke.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    film(10, "stilhed", [
        ("31960017", 0.5, 1.2, "Hjem", None), ("40134358", 0.8, 1.2, "er der,", None),
        ("30912265", 0.5, 1.3, "hvor *stilheden*", None), ("6263194", 0.5, 1.5, "venter.", None),
        ("29532417", 0.3, 1.3, "Lyt", None), ("36300251", 0.5, 1.3, "*først.*", None),
        ("6323324", 0.5, 2.6, "Støjen, *målt på stedet.*", "07-maal-stoej-vindue.png"),
    ], "Støj er den hyppigste grund til, at en lejer flytter tidligt, og det eneste, ingen annonce fortæller om.\n\nVed fremvisningen: telefonen midt i rummet, 30 sekunder med vinduet åbent og 30 med det lukket. Nesso sammenligner de to målinger.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    chat(10, "20:00", "ingen-penge", ("7710747", 0.5), "Udlejer", "Annonce", INK_AV, "Overfør depositum, så er den din 🙏",
         [("me", "Kan jeg se den først?", 0.0), ("them", "Jeg er i udlandet 😕", 0.8), ("me", "Så nej.", 0.0)],
         "Først\nfremvisningen.", "Ingen penge, før du har set boligen selv.", "06-indenfor-property-check.png",
         "En regel om penge: ingen penge, før du har set boligen med egne øjne. Hverken for at leje eller for at købe.\n\nOg når du ser den, har du 81 tjek i lommen. Prøv Nesso: link i bio.\n\n" + TAG_VISIT),

    # ---------------------------------------------------------------- Wednesday 11
    chat(11, "08:00", "to-og-to", ("8555712", 0.5), "Jonas", "Kæreste", ORANGE_AV, "Kunne du lide lejligheden? 😍",
         [("me", "Ja! Men hørte du naboen?", 0.0), ("them", "Hvilken nabo? 😅", 0.8)],
         "Én bolig.\nTo fremvisninger.", "Gå den igennem hver for sig. Sammenlign bagefter.", "06-indenfor-property-check.png",
         "Den ene så lyset, den anden hørte naboen.\n\nMed Nesso går I den samme fremvisning igennem hver for sig, uden at se den andens svar. Bagefter viser én side, hvor I er enige, og hvor I ikke er.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    film(11, "morgenlys", [
        ("31960017", 0.5, 1.2, "Lyset", None), ("29513615", 0.8, 1.3, "om *morgenen*", None),
        ("40134358", 0.5, 1.3, "siger mere", None), ("36300251", 0.5, 1.5, "end et *foto.*", None),
        ("29681899", 0.5, 1.4, "Se det", None), ("6798992", 1.0, 1.2, "*selv.*", None),
        ("30912265", 0.5, 2.6, "Bagest\ni *rummet.*", "06-indenfor-property-check.png"),
    ], "Billederne i annoncen er taget i det bedste sollys og med den bredeste vinkel.\n\nVed fremvisningen slukker du lyset og ser på bagvæggen, ikke på vindueskarmen. Nesso viser dig hvordan, og hvad tjekket ikke kan fastslå.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    chat(11, "20:00", "skoede", ("6964001", 0.5), "Emma", "Veninde", ORANGE_AV, "Hvad koster det at tinglyse skødet? 🤔",
         [("me", "1.850 kr. plus 0,6 % af prisen", 0.0), ("them", "Af 3 millioner? 😳", 0.7)],
         "19.850 kr.\nfor skødet.", "En ejerbolig til 3 mio. kr.", "04-omkostninger.png",
         "Når du køber en ejerbolig, tinglyser du skødet. Afgiften er 1.850 kr. plus 0,6 % af købesummen, og procentdelen rundes op til hele 100 kr.\n\nPå en bolig til 3.000.000 kr. er det 19.850 kr. Hvert lån får desuden sit eget pantebrev med sin egen afgift.\n\nRegn det ud med din pris: Prøv Nesso, link i bio.\nKilde: tinglysningsafgiftsloven § 4. Det er en beregning, ikke rådgivning.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Thursday 12
    chat(12, "08:00", "mor", ("7464106", 0.5), "Mor", "", (226, 124, 176), "Har du kigget bag skabet? 👀",
         [("me", "Hvorfor?", 0.0), ("them", "Skimmel gemmer sig der.", 0.8), ("them", "Tro mig 😌", 0.5)],
         "Mor har\nret.", "Foden af væggene, hjørnerne, bag møblerne.", "06-indenfor-property-check.png",
         "Fugt sidder sjældent midt på væggen. Den sidder forneden, i hjørnerne og der, hvor møblerne dækker væggen.\n\nVed fremvisningen: gå langs foden af ydervæggene, kig bag møbler og ind i hjørnerne, og led efter pletter, bobler eller afskallet maling. Grænsen: en plet kan være gammel og tør, og en væg, hvor der intet er at se, kan stadig være våd.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    film(12, "hjoerner", [
        ("6323324", 0.5, 1.3, "Hvert *hjørne*", None), ("29532417", 0.3, 1.3, "fortæller", None),
        ("40187579", 0.5, 1.4, "noget.", None), ("36300251", 0.5, 1.3, "Gulvet.", None),
        ("31960017", 0.5, 1.3, "Vinduerne.", None), ("6263194", 0.5, 1.3, "*Vandet.*", None),
        ("30912265", 0.5, 2.6, "81 tjek, så du\nhører *efter.*", "06-indenfor-property-check.png"),
    ], "Gulv, vinduer, vand, vægge, støj, lys.\n\nHvert tjek i Nessos tjekliste siger i få trin, hvordan du gør det, hvad det tjekkes med, og hvad det ikke fastslår. Mange klarer du med telefonen.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    chat(12, "20:00", "ny-by", ("9141848", 0.5), "Ida", "Kollega", VIOLET_AV, "Velkommen til København! 🎉",
         [("them", "Hvor leder du efter bolig?", 0.6), ("me", "Jeg kender ikke et eneste kvarter 😅", 0.0)],
         "5 spørgsmål.\nDit kvarter.", "Find ud af, hvilken slags beboer du er.", "02b-quiz-sticker.png",
         "Du flytter for jobbets skyld og kender ikke byen.\n\nFem spørgsmål, og Nesso fortæller dig, hvilken slags beboer du er, med dit eget klistermærke, og hvilket kvarter der ligner dig mest. Kvartererne er læst ud fra offentlige data: butikker, parker, skoler, minutter til fods.\n\nPrøv Nesso: link i bio.\n\n" + TAG_LIVE),

    # ---------------------------------------------------------------- Friday 13
    chat(13, "08:00", "advokat", ("8814707", 0.5), "Mads", "Ven", ORANGE_AV, "Hvad koster en boligadvokat? 🤔",
         [("me", "Det kommer an på 🤷‍♀️", 0.0), ("them", "På hvad??", 0.6)],
         "Ingen regel\nsætter prisen.", "Bed om et skriftligt tilbud. Fra flere end én.", "04-omkostninger.png",
         "Hvad koster en rådgiver eller advokat til boligkøbet? Ingen regel sætter et tal på det: prisen aftaler du med dem.\n\nBed om et skriftligt tilbud, før du skriver under, og spørg flere end én. Tinglysningen har derimod faste satser, og dem regner Nesso ud.\n\nPrøv Nesso: link i bio.\n\n" + TAG_COST),
    film(13, "noegler", [
        ("6798992", 0.3, 1.2, "Før", None), ("29513615", 0.5, 1.3, "*nøglerne,*", None),
        ("6323324", 0.5, 1.4, "tallene.", None), ("30912265", 0.8, 1.3, "Tinglysning.", None),
        ("36300251", 0.5, 1.2, "Lånet.", None), ("29532417", 0.3, 1.2, "*Ydelsen.*", None),
        ("6263194", 0.5, 2.6, "Det hele, på\ndin *pris.*", "04-omkostninger.png"),
    ], "Før nøglerne, tallene.\n\nTinglysning af skøde og pantebreve, og hvad lånene koster om måneden: Nessos beregner regner det ud på din pris med loven ved siden af. Rådgiver, ejerskifteforsikring og bankens gebyrer står der uden tal, fordi ingen regel fastsætter dem.\n\nPrøv Nesso: link i bio.\n\n" + TAG_COST),
    chat(13, "20:00", "fortrydelse", ("7646611", 0.5), "Sofie", "Veninde", ORANGE_AV, "Har I skrevet under? 🥂",
         [("me", "Ja… og nu er jeg i tvivl 😬", 0.0), ("them", "Du kan fortryde i 6 hverdage", 0.9)],
         "6 hverdage\ntil at fortryde.", "Det koster 1 % af prisen: 30.000 kr. på 3 mio.", "04-omkostninger.png",
         "Køber du en bolig, kan du som udgangspunkt fortryde inden for 6 hverdage. Det koster 1 % af købesummen, som du betaler til sælger: 30.000 kr. på en bolig til 3.000.000 kr.\n\nDet koster kun noget, hvis du bruger det. Nessos beregner viser beløbet på din pris.\n\nPrøv Nesso: link i bio.\nKilde: lov om forbrugerbeskyttelse ved erhvervelse af fast ejendom (LBK nr. 1123/2015). Det er en beregning, ikke rådgivning.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Saturday 14
    chat(14, "08:00", "bruser", ("8563625", 0.5), "Freja", "Bofælle", ORANGE_AV, "Er der tryk i bruseren? 🚿",
         [("me", "Har ikke prøvet 🙈", 0.0), ("them", "Prøv med køkkenhanen åben 😏", 0.8)],
         "To haner\npå én gang.", "Ét tjek, ét minut, ved fremvisningen.", "06-indenfor-property-check.png",
         "Med kun én hane åben ser næsten alle boliger fine ud.\n\nÅbn køkkenhanen helt, tænd også for bruseren, og se på strålen i køkkenet. Grænsen: vandtrykket skifter hen over dagen og fra etage til etage.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    film(14, "saelger", [
        ("40187579", 0.5, 1.3, "Sælger du *bolig?*", None), ("40134358", 0.5, 1.3, "Hvad tæller", None),
        ("36300251", 0.5, 1.4, "*virkelig,*", None), ("6323324", 0.5, 1.4, "ifølge", None),
        ("30912265", 0.5, 1.3, "*forskningen?*", None),
        ("31960017", 0.5, 2.6, "Og hvad der *ikke* tæller.", "05-forbered.png"),
    ], "Skal du sælge eller udleje? Forbered er den del af Nesso, der er til den, der viser boligen frem.\n\nHvert råd siger, om forskningen har set det i prisen, om det hjælper værdien med at blive set, eller om det kun ændrer fremvisningen. Kaffeduft har for eksempel ingen undersøgelse, der knytter den til prisen.\n\nPrøv Nesso: link i bio.\n\n" + TAG_SELL),
    chat(14, "20:00", "sol", ("6799015", 0.5), "Mikkel", "Mægler", VIOLET_AV, "Sydvendt! ☀️",
         [("me", "Og bygningen overfor?", 0.0), ("them", "…den er høj 🫣", 0.9)],
         "Tæl timerne\nmed sol.", "Også i december, med huset overfor.", "06-indenfor-property-check.png",
         "Solen afhænger også af bygningen overfor.\n\nI Nesso retter du telefonen mod tagkanten overfor, og appen regner timerne med sol over det tag ud, i dag og ved vintersolhverv. Grænsen: den ser ét tag, ikke et træ eller en altan.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),

    # ---------------------------------------------------------------- Sunday 15
    chat(15, "08:00", "billeder", ("4553290", 0.5), "Sofie", "Veninde", ORANGE_AV, "Har du set billederne? Kæmpestor! 📸",
         [("them", frame("29681899"), 0.0), ("me", "I virkeligheden er den det halve 🙃", 0.0)],
         "Billederne\nforstørrer.", "Mål rummet ved fremvisningen.", "06-indenfor-property-check.png",
         "Billederne i boligannoncer tages fra hjørnet med den bredeste vinkel, der findes.\n\nVed fremvisningen måler du selv: længde, bredde og højde i hvert rum. Nessos tjekliste siger, hvad du skal måle, og hvordan.\n\nPrøv Nesso: link i bio.\n\n" + TAG_VISIT),
    film(15, "kvarter", [
        ("40134358", 0.5, 1.3, "Det rigtige", None), ("29681899", 0.5, 1.3, "*kvarter*", None),
        ("6263194", 0.5, 1.4, "ændrer", None), ("29513615", 0.5, 1.5, "*alt.*", None),
        ("30912265", 0.5, 2.6, "Dit, på\n5 *spørgsmål.*", "02b-quiz-sticker.png"),
    ], "Caféen nede på gaden, parken, skolen, hvor mange minutter til fods.\n\nFem spørgsmål, og Nesso fortæller dig, hvilken slags beboer du er, og hvilket kvarter der ligner dig, ud fra offentlige data. Fem danske byer: København, Aarhus, Odense, Aalborg og Esbjerg.\n\nPrøv Nesso: link i bio.\n\n" + TAG_LIVE),
    chat(15, "20:00", "gaeldsfaktor", ("8293126", 0.5), "Banken", "Rådgiver", INK_AV, "Her er vores lånetilbud! ✨",
         [("me", "Hvad er min gældsfaktor?", 0.0), ("them", "Din gæld delt med din indkomst 📄", 0.8)],
         "Over 4\ner højt.", "Finanstilsynets udgangspunkt for gældsfaktoren.", "04-omkostninger.png",
         "Din gældsfaktor er din samlede gæld delt med husstandens indkomst før skat. Finanstilsynet anser som udgangspunkt en gældsfaktor på mere end fire som høj.\n\nDet er et udgangspunkt, banken bruger sammen med resten af din økonomi, og det siger ikke, om du kan eller bør låne. Nessos beregner viser din gældsfaktor ud fra lånene og din indkomst.\n\nPrøv Nesso: link i bio.\nKilde: Finanstilsynets vejledning nr. 9458 af 1. juni 2023.\n\n" + TAG_COST),
]


# ---------------------------------------------------------------- captions that travel
# Every caption: the hook line first, the body, the link, then a question, save and share, and five
# hashtags (Instagram counts five at most since December 2025).
CTA = {
    "visit": ("Gem den til næste fremvisning 📌\nSend den til en, der leder efter bolig.", TAG_VISIT),
    "cost": ("Gem den, før du skriver under 📌\nSend den til en, der skal købe bolig.", TAG_COST),
    "sell": ("Gem den, hvis du sælger eller udlejer 📌\nSend den til en, der gør sin bolig klar.", TAG_SELL),
    "live": ("Gem den, hvis du skal flytte 📌\nSend den til en, der leder efter bolig i en ny by.", TAG_LIVE),
}
QUESTION_CHAT = "Er det sket for dig? Fortæl det i kommentarerne 👇"
QUESTION_FILM = {
    "visit": "Hvad kigger du først efter i en bolig? Skriv det i kommentarerne 👇",
    "cost": "Hvilken udgift overraskede dig mest? Skriv det i kommentarerne 👇",
    "sell": "Hvilket råd har du hørt oftest? Skriv det i kommentarerne 👇",
    "live": "Hvilken by leder du efter bolig i? Skriv det i kommentarerne 👇",
}


def _category(caption):
    tags = caption.strip().splitlines()[-1]
    if tags == TAG_COST:
        return "cost"
    if tags == TAG_SELL:
        return "sell"
    if tags == TAG_LIVE:
        return "live"
    return "visit"


for _item in ITEMS:
    cat = _category(_item["caption"])
    body = "\n".join(_item["caption"].strip().splitlines()[:-1]).strip()
    question = QUESTION_CHAT if "scenes" in _item else QUESTION_FILM[cat]
    save, tags = CTA[cat]
    _item["caption"] = f"{body}\n\n{question}\n{save}\n\n{tags}"
