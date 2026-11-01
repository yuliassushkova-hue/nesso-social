"""The week's 21 Reels, 2 to 8 November, in the founder's two chosen styles, mixed:
08:00 and 20:00 a chat story (after Airbnb Italia's "Non preoccuparti."), 13:00 a warm interior
film with words one at a time in the landing page's serif (after the Victorian-home Reel).

Footage: Pexels License, ids are https://www.pexels.com/video/<id>/. Facts: costs from
nesso.fit/it/costi-acquisto-casa (the €300.000 example recomputed: €13.528 before notary, bank and
insurance; registro €1.848 on rendita €800; agency €9.000 + €1.980 IVA), viewing checks from
nesso.fit/it/checklist-visita-casa, the mortgage rights from the same costs page.
"""

P = "~/Documents/GitHub/nesso-assets/pexels/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"
LINK = "Prova Nesso · link in bio"
TAG_VISIT = "#cercocasa #visitacasa #comprarecasa #affittocasa #casa"
TAG_COST = "#comprarecasa #primacasa #mutuo #casa #Milano"
TAG_SELL = "#vendocasa #venderecasa #homestaging #casa #immobiliare"
TAG_LIVE = "#trasferimento #Milano #Torino #quartiere #cercocasa"
ORANGE_AV, VIOLET_AV, INK_AV = (249, 115, 22), (90, 62, 192), (52, 33, 111)


def at(day, time):
    return f"2026-11-{day:02d}T{time}+01:00"


def chat(day, time, slug, hook_clip, who, role, color, hook, thread, headline, sub, phone, caption):
    """hook: the first message, floating over real footage. thread: (from, text or clip-photo, typing)."""
    # the hook message opens the thread too, already there when the chat appears
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
    return {"id": f"r-{slug}", "type": "reel", "channel": "ig-it", "at": at(day, time), "slug": f"reel-{slug}",
            "scenes": [
                {"kind": "photo", "secs": 2.1, "clip": {"file": P + hook_clip[0] + ".mp4", "start": hook_clip[1]},
                 "who": who, "color": color, "bubble": hook},
                {"kind": "chat", "secs": chat_secs, "who": who, "role": role, "color": color, "messages": msgs},
                {"kind": "headline", "secs": 2.6, "text": headline, "sub": sub, "phone": M + phone},
                {"kind": "end", "secs": 2.0, "line": "Prima di firmare.", "cta": LINK},
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
            # the app takes the screen: big and centred, the words in one line above it
            card.update({"phone": M + phone, "phone_top": 400, "phone_height": 1480, "phone_tilt": -3, "phone_dx": 0,
                         "size": 96, "text_top": True, "text_y": 0})
            card["text"] = words.replace("\n", " ")
        cards.append(card)
    clips.append({"file": P + "40187579.mp4", "start": 0.5, "secs": 2.3})
    cards.append({"kind": "brand", "sub": "Prima di firmare · link in bio", "secs": 2.3})
    # soft piano under every warm film, the two tracks taking turns day by day
    music = "music-beautiful-dream" if day % 2 == 0 else "music-classical-vibes"
    return {"id": f"r-{slug}", "type": "reel", "channel": "ig-it", "at": at(day, "13:00"), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": clips, "cards": cards, "caption": caption,
            "music": music, "music_gain": 0.6, "music_start": 3.0}


def frame(clip, start=1.0):
    return {"file": P + clip + ".mp4", "start": start}


ITEMS = [
    # ---------------------------------------------------------------- Monday 2
    chat(2, "08:00", "luce", ("5853208", 0.5), "Marco", "Agenzia", VIOLET_AV, "La casa è luminosissima ☀️",
         [("them", frame("30744460"), 0.0), ("them", "Sole tutto il giorno ☀️", 0.6),
          ("me", "Anche in fondo alla stanza?", 0.0), ("them", "Eh… quasi 😅", 0.9)],
         "Fidati.\nMa misura.", "La luce in fondo alla stanza, in visita.", "06-dentro-property-check.png",
         "«Luminosissima.» Vicino alla finestra lo sono tutte.\n\nIn visita spegni le luci e guarda la parete di fondo: è lì che leggerai e lavorerai. Nella checklist di Nesso c'è come farlo, e cosa quel controllo non può dirti.\n\nProva Nesso: link in bio.\n\n" + TAG_VISIT),
    film(2, "guarda-davvero", [
        ("6798992", 0.3, 1.0, "Prima", None), ("6798992", 1.3, 1.1, "di *firmare,*", None),
        ("29513615", 0.5, 1.4, "guarda", None), ("40134358", 0.5, 1.6, "*davvero.*", None),
        ("36300251", 0.5, 1.2, "La luce.", None), ("31960017", 0.5, 1.2, "Il silenzio.", None),
        ("6323324", 0.5, 1.2, "Gli angoli.", None),
        ("30912265", 0.5, 2.6, "82 controlli\nper la *visita.*", "06-dentro-property-check.png"),
    ], "Una visita dura venti minuti. La casa, anni.\n\nLa luce in fondo alla stanza, il rumore a finestra aperta, gli angoli dietro i mobili: 82 controlli per la visita, molti col telefono.\n\nProva Nesso: link in bio.\n\n" + TAG_VISIT),
    chat(2, "20:00", "quanto-paghi", ("13441354", 0.5), "Giulia", "Amica", ORANGE_AV, "Allora, quanto la paghi? 🏠",
         [("me", "300 mila 🙂", 0.0), ("them", "E registro, agenzia, IVA, mutuo?", 0.7), ("me", "…😳", 0.0)],
         "€13.528 in più.", "Su €300.000, prima di notaio e banca.", "04-costi.png",
         "Il prezzo dell'annuncio non è quello che paghi.\n\nEsempio con le regole nazionali: €300.000 da un privato, prima casa, rendita catastale €800, agenzia al 3%, mutuo di €240.000. Registro €1.848, ipotecaria e catastale €100, agenzia €10.980 con IVA, imposta sul mutuo €600: €13.528, prima di notaio, banca e assicurazione.\n\nFai il conto sul tuo prezzo, gratis: link in bio. È un calcolo sulle regole nazionali, non una consulenza.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Tuesday 3
    chat(3, "08:00", "tranquilla", ("5835540", 0.5), "Marco", "Agenzia", VIOLET_AV, "Zona tranquillissima 🤫",
         [("me", "Anche con la finestra aperta?", 0.0), ("them", "Beh… il tram passa alle 6 🚋", 0.9)],
         "Aprila.\nE misura.", "30 secondi aperta, 30 chiusa.", "07-misura-rumore-finestra.png",
         "Alla visita la finestra è quasi sempre chiusa. Aprila.\n\n30 secondi a finestra aperta, 30 a finestra chiusa, telefono fermo nello stesso punto: Nesso confronta le due misure. La cifra assoluta cambia da telefono a telefono, la differenza no.\n\nProva Nesso: link in bio.\n\n" + TAG_VISIT),
    film(3, "silenzio", [
        ("31960017", 0.5, 1.2, "Casa", None), ("40134358", 0.8, 1.2, "è dove", None),
        ("30912265", 0.5, 1.3, "il *silenzio*", None), ("6263194", 0.5, 1.5, "ti aspetta.", None),
        ("29532417", 0.3, 1.3, "Ascoltalo", None), ("36300251", 0.5, 1.3, "*prima.*", None),
        ("6323324", 0.5, 2.6, "Il rumore,\nmisurato in *visita.*", "07-misura-rumore-finestra.png"),
    ], "Il rumore è il motivo più comune per cui si lascia una casa presto, ed è l'unica cosa che nessun annuncio dichiara.\n\nIn visita: telefono a metà stanza, 30 secondi a finestra aperta e 30 chiusa. Nesso confronta le due misure.\n\nLink in bio.\n\n" + TAG_VISIT),
    chat(3, "20:00", "caparra", ("7710747", 0.5), "Proprietario", "Annuncio", INK_AV, "Per bloccarla mi mandi 1.000€? 🙏",
         [("me", "Prima posso vederla?", 0.0), ("them", "Sono all'estero 😕", 0.8), ("me", "Allora no.", 0.0)],
         "Prima la visita.", "Nessuna caparra prima di aver visto la casa di persona.", "06-dentro-property-check.png",
         "Una regola sui soldi: nessuna caparra prima di aver visto la casa di persona. Né per un affitto, né per un acquisto.\n\nE quando la vedi, hai 82 controlli in tasca. Prova Nesso: link in bio.\n\n" + TAG_VISIT),

    # ---------------------------------------------------------------- Wednesday 4
    chat(4, "08:00", "in-due", ("8555712", 0.5), "Luca", "Fidanzato", ORANGE_AV, "Ti è piaciuta la casa? 😍",
         [("me", "Sì! Ma hai sentito il vicino?", 0.0), ("them", "Quale vicino? 😅", 0.8)],
         "Una casa.\nDue visite.", "Fatela in due, ognuno per conto suo. Poi confrontate.", "06-dentro-property-check.png",
         "Uno ha visto la luce, l'altra ha sentito il vicino.\n\nCon Nesso fate la stessa visita in due, senza vedere le risposte dell'altro. Poi una pagina sola vi mostra dove siete d'accordo e dove no.\n\nLink in bio.\n\n" + TAG_VISIT),
    film(4, "luce-mattino", [
        ("31960017", 0.5, 1.2, "La luce", None), ("29513615", 0.8, 1.3, "del *mattino*", None),
        ("40134358", 0.5, 1.3, "vale più", None), ("36300251", 0.5, 1.5, "di una *foto.*", None),
        ("29681899", 0.5, 1.4, "Guardala", None), ("6798992", 1.0, 1.2, "*dal vivo.*", None),
        ("30912265", 0.5, 2.6, "In fondo\nalla *stanza.*", "06-dentro-property-check.png"),
    ], "Le foto dell'annuncio si scattano col sole migliore e l'obiettivo più largo.\n\nIn visita spegni le luci e guarda la parete di fondo, non il davanzale. Nesso ti dice come, e cosa quel controllo non può stabilire.\n\nLink in bio.\n\n" + TAG_VISIT),
    chat(4, "20:00", "registro", ("6964001", 0.5), "Sara", "Amica", ORANGE_AV, "Il registro è il 9% del prezzo, vero? 😱",
         [("me", "Prima casa da un privato: 2%", 0.0), ("me", "E spesso sul valore catastale", 0.0), ("them", "Cioè? 🤔", 0.7)],
         "€1.848,\nnon €6.000.", "Prima casa, rendita €800, casa da €300.000.", "04-costi.png",
         "Se compri da un privato come persona fisica, il registro sulla prima casa è il 2% della base imponibile (il 9% sulle altre), e la base può essere il valore catastale: rendita × 1,05 × 110. Si chiede in atto.\n\nCon una rendita di €800: €1.848 invece di €6.000 su un prezzo di €300.000.\n\nIl calcolo con la tua rendita, gratis: link in bio. DPR 131/1986, L. 266/2005. È un calcolo, non una consulenza.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Thursday 5
    chat(5, "08:00", "mamma", ("7464106", 0.5), "Mamma", "", (226, 124, 176), "Hai guardato dietro l'armadio? 👀",
         [("me", "Perché?", 0.0), ("them", "La muffa si nasconde lì.", 0.8), ("them", "Fidati 😌", 0.5)],
         "Ha ragione\nla mamma.", "Base dei muri, angoli, dietro i mobili.", "06-dentro-property-check.png",
         "L'umidità raramente è al centro della parete. Sta in basso, negli angoli e dove i mobili coprono il muro.\n\nIn visita: cammina lungo la base dei muri esterni, guarda dietro i mobili e negli angoli, cerca macchie, bolle o vernice che si stacca. Il limite: una macchia può essere vecchia e asciutta, e un muro pulito può essere bagnato.\n\nLink in bio.\n\n" + TAG_VISIT),
    film(5, "angoli", [
        ("6323324", 0.5, 1.3, "Ogni *angolo*", None), ("29532417", 0.3, 1.3, "racconta", None),
        ("40187579", 0.5, 1.4, "qualcosa.", None), ("36300251", 0.5, 1.3, "Il pavimento.", None),
        ("31960017", 0.5, 1.3, "Le finestre.", None), ("6263194", 0.5, 1.3, "L'*acqua.*", None),
        ("30912265", 0.5, 2.6, "82 controlli\nper *ascoltarli.*", "06-dentro-property-check.png"),
    ], "Pavimento, finestre, acqua, muri, rumore, luce.\n\nOgni controllo della checklist di Nesso dice come farlo in pochi passi, con cosa si fa e cosa non stabilisce. Molti col telefono.\n\nProva Nesso: link in bio.\n\n" + TAG_VISIT),
    chat(5, "20:00", "nuova-citta", ("9141848", 0.5), "Chiara", "Collega", VIOLET_AV, "Benvenuta a Milano! 🎉",
         [("them", "Dove cerchi casa?", 0.6), ("me", "Non conosco nessun quartiere 😅", 0.0)],
         "5 domande.\nIl tuo quartiere.", "Scopri che abitante sei.", "02b-quiz-sticker.png",
         "Ti trasferisci per lavoro e la città non la conosci.\n\nCinque domande e Nesso ti dice che abitante sei, con il tuo sticker, e quale quartiere ti somiglia. I quartieri sono letti con dati pubblicati: negozi, parchi, scuole, minuti a piedi.\n\nProva Nesso: link in bio.\n\n" + TAG_LIVE),

    # ---------------------------------------------------------------- Friday 6
    chat(6, "08:00", "notaio", ("8814707", 0.5), "Paolo", "Amico", ORANGE_AV, "E il notaio quanto costa? 🤔",
         [("me", "Dipende 🤷‍♀️", 0.0), ("them", "Da cosa??", 0.6)],
         "Nessuna legge\nlo fissa.", "Chiedi un preventivo scritto. A più di un notaio.", "04-costi.png",
         "Quanto costa il notaio? Nessuna norma nazionale fissa il suo onorario, quindi un numero unico non esiste.\n\nChiedi un preventivo scritto prima del preliminare, e chiedilo a più di un notaio. Imposte, agenzia e imposta sul mutuo invece hanno regole precise: le calcola Nesso, gratis.\n\nLink in bio.\n\n" + TAG_COST),
    film(6, "chiavi", [
        ("6798992", 0.3, 1.2, "Prima", None), ("29513615", 0.5, 1.3, "delle *chiavi,*", None),
        ("6323324", 0.5, 1.4, "i numeri.", None), ("30912265", 0.8, 1.3, "Imposte.", None),
        ("36300251", 0.5, 1.2, "Agenzia.", None), ("29532417", 0.3, 1.2, "*Mutuo.*", None),
        ("6263194", 0.5, 2.6, "Tutto, sul tuo\n*prezzo.*", "04-costi.png"),
    ], "Prima delle chiavi, i numeri.\n\nRegistro, ipotecaria e catastale, agenzia con l'IVA, imposta sul mutuo: il calcolatore di Nesso fa il conto sul tuo prezzo, con la norma accanto a ogni riga. Notaio, banca e assicurazione a parte: servono preventivi scritti.\n\nProva Nesso: link in bio.\n\n" + TAG_COST),
    chat(6, "20:00", "iva", ("7646611", 0.5), "Marco", "Agenzia", VIOLET_AV, "La provvigione è il 3% 🙂",
         [("me", "IVA compresa?", 0.0), ("them", "…no 😬", 0.9)],
         "+22% di IVA.", "Su €300.000: €10.980, non €9.000.", "04-costi.png",
         "La provvigione dell'agenzia ha l'IVA al 22%. Al 3% su €300.000: €9.000 più €1.980.\n\nSulla prima casa puoi detrarre dall'IRPEF il 19% della provvigione, fino a €1.000, nell'anno in cui la paghi.\n\nIl calcolo con la tua percentuale, gratis: link in bio. È un calcolo, non una consulenza.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Saturday 7
    chat(7, "08:00", "doccia", ("8563625", 0.5), "Elena", "Coinquilina", ORANGE_AV, "C'è pressione in doccia? 🚿",
         [("me", "Non ho provato 🙈", 0.0), ("them", "Prova con la cucina aperta 😏", 0.8)],
         "Due rubinetti\ninsieme.", "Un controllo, un minuto, in visita.", "06-dentro-property-check.png",
         "Con un rubinetto solo quasi tutte le case sembrano a posto.\n\nApri del tutto il rubinetto della cucina, accendi anche la doccia e guarda il getto in cucina. Il limite: la pressione cambia nell'arco della giornata e da un piano all'altro.\n\nGli altri controlli per la visita, gratis: link in bio.\n\n" + TAG_VISIT),
    film(7, "vendi", [
        ("40187579", 0.5, 1.3, "Vendi *casa?*", None), ("40134358", 0.5, 1.3, "Cosa conta", None),
        ("36300251", 0.5, 1.4, "*davvero,*", None), ("6323324", 0.5, 1.4, "secondo", None),
        ("30912265", 0.5, 1.3, "la *ricerca.*", None),
        ("31960017", 0.5, 2.6, "E cosa cambia\nsolo la *visita.*", "05-prepara.png"),
    ], "Vendi o affitti casa? Prepara è la parte di Nesso per chi la mostra.\n\nOgni consiglio dice se la ricerca lo ha visto nel prezzo, se rende visibile un valore che c'è già o se cambia solo la visita. Il profumo di caffè, per dire, non ha studi che lo leghino al prezzo.\n\nLink in bio.\n\n" + TAG_SELL),
    chat(7, "20:00", "sole", ("6799015", 0.5), "Marco", "Agenzia", VIOLET_AV, "Esposizione sud! ☀️",
         [("me", "E il palazzo di fronte?", 0.0), ("them", "…è alto 🫣", 0.9)],
         "Conta le ore\ndi sole.", "Anche a dicembre, col palazzo di fronte.", "06-dentro-property-check.png",
         "Il sole lo decide anche il palazzo di fronte.\n\nIn Nesso punti il telefono sul bordo del tetto di fronte e l'app calcola le ore di sole sopra quel tetto, oggi e al solstizio d'inverno. Il limite: vede un tetto solo, non un albero o un balcone.\n\nLink in bio.\n\n" + TAG_VISIT),

    # ---------------------------------------------------------------- Sunday 8
    chat(8, "08:00", "foto", ("4553290", 0.5), "Sara", "Amica", ORANGE_AV, "Hai visto le foto? Enorme! 📸",
         [("them", frame("29681899"), 0.0), ("me", "Dal vivo è la metà 🙃", 0.0)],
         "Le foto\ningrandiscono.", "Misura la stanza in visita.", "06-dentro-property-check.png",
         "Le foto degli annunci si scattano dall'angolo, con l'obiettivo più largo che c'è.\n\nIn visita misura tu: lunghezza, larghezza e altezza di ogni stanza. La checklist di Nesso ti dice cosa misurare e come.\n\nProva Nesso: link in bio.\n\n" + TAG_VISIT),
    film(8, "quartiere", [
        ("40134358", 0.5, 1.3, "Il *quartiere*", None), ("29681899", 0.5, 1.3, "giusto", None),
        ("6263194", 0.5, 1.4, "cambia", None), ("29513615", 0.5, 1.5, "*tutto.*", None),
        ("30912265", 0.5, 2.6, "Il tuo,\nin 5 *domande.*", "02b-quiz-sticker.png"),
    ], "Il caffè sotto casa, il parco, la scuola, quanti minuti a piedi.\n\nCinque domande e Nesso ti dice che abitante sei e quale quartiere ti somiglia, con dati pubblicati. Dieci città italiane.\n\nProva Nesso: link in bio.\n\n" + TAG_LIVE),
    chat(8, "20:00", "mutuo", ("8293126", 0.5), "Banca", "Consulente", INK_AV, "Ecco la nostra offerta! ✨",
         [("me", "Mi manda anche il PIES?", 0.0), ("them", "Certo, è gratuito 📄", 0.8)],
         "Confronta\nil TAEG.", "Chiedi il PIES a più banche, prima di firmare.", "04-costi.png",
         "Prima di un mutuo per la casa, la banca ti deve il PIES: gratuito e personalizzato, prima che tu sia vincolato. Chiedilo a più banche e confronta il TAEG.\n\nHai almeno sette giorni per valutare un'offerta vincolante, puoi portare il mutuo a un'altra banca senza costi e chiuderlo prima senza penali.\n\nRata, imposte e spese nel calcolatore di Nesso, gratis: link in bio.\nFonte: Banca d'Italia, Il mutuo ipotecario in parole semplici (2026).\n\n" + TAG_COST),
]


# ---------------------------------------------------------------- captions that travel
# Every caption: the hook line first (what shows before "more"), the body, then a call to save,
# share and comment (the three signals Instagram weighs most), the link, and five hashtags
# (Instagram counts five at most since December 2025, so they are chosen, not piled up).
CTA = {
    "visit": ("Salvalo per la prossima visita 📌\nMandalo a chi sta cercando casa.",
              "#cercocasa #visitacasa #comprarecasa #affitto #consiglicasa"),
    "cost": ("Salvalo prima di firmare 📌\nMandalo a chi sta comprando casa.",
             "#comprarecasa #primacasa #mutuo #notaio #consiglicasa"),
    "sell": ("Salvalo se vendi o affitti casa 📌\nMandalo a chi sta preparando la sua.",
             "#vendocasa #venderecasa #homestaging #immobiliare #consiglicasa"),
    "live": ("Salvalo se ti trasferisci 📌\nMandalo a chi cerca casa in una nuova città.",
             "#trasferimento #nuovacitta #quartiere #cercocasa #Milano"),
}
QUESTION_CHAT = "Ti è mai successo? Raccontalo nei commenti 👇"
QUESTION_FILM = {
    "visit": "Tu cosa guardi per primo in una casa? Scrivilo nei commenti 👇",
    "cost": "Quale spesa ti ha sorpreso di più? Scrivilo nei commenti 👇",
    "sell": "Quale consiglio hai sentito più spesso? Scrivilo nei commenti 👇",
    "live": "In che città cerchi casa? Scrivilo nei commenti 👇",
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
