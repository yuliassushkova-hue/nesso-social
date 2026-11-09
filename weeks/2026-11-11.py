"""@nesso_italia, Wednesday 11 to Sunday 15 November 2026. Same formats and helpers as weeks/2026-11-09.py.

Every step and every limit is the app's own text from nesso.fit/it/checklist-visita-casa, read on
9 November. The Perché Nesso claims are the ones in CREATIVE.md §7.

No clip or photo here has been on @nesso_italia before (founder, 8 November); each clip is in one post.
The 09:30 story is a question card this week, because every app screen has already been a story.

Footage and photos: Pexels License, downloaded 9 November. Sounds and music: Mixkit.
"""
import runpy
from pathlib import Path

HERE = Path(__file__).parent
BASE = runpy.run_path(str(HERE / "2026-11-09.py"))
chat, film, card, tomorrow, at = BASE["chat"], BASE["film"], BASE["card"], BASE["tomorrow"], BASE["at"]
ORANGE_AV, VIOLET_AV, INK_AV = BASE["ORANGE_AV"], BASE["VIOLET_AV"], BASE["INK_AV"]
PERCHE = runpy.run_path(str(HERE / "next-perche-nesso-carousel.py"))["SPEC"]

F = "~/Documents/GitHub/nesso-assets/pexels-photos/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"
SAVE = "Salvalo prima di firmare 📌\nMandalo a chi sta cercando casa."
TAGS = "#comprarecasa #cercocasa #visitacasa #primacasa #consiglicasa"


def ask(day, slug, theme, text, sub):
    """The 09:30 story: one question to put at the viewing."""
    return {**card(day, "09:30", f"domanda-{slug}", theme, "CHIEDI IN VISITA", text, sub)}


def end(x, first, second):
    """The last slide: the thought, the call, the logo on the photo."""
    return [
        {"x": x + 96, "y": 150, "lines": [(first, "white", 84), (second, "violet", 76)]},
        {"x": x + 96, "y": 700, "lines": [("Prova Nesso  →", "orange", 84), ("link in bio", "white", 52)]},
    ]


CHIEDI = {"slides": 7, "photos": [
    {"file": F + "7641868.jpg", "x": 0, "focus": 0.5},
    {"file": F + "7641932.jpg", "x": 1700, "focus": 0.5},
    {"file": F + "36935416.jpg", "x": 3300, "focus": 0.6},
    {"file": F + "4246220.jpg", "x": 4900, "focus": 0.5},
    {"file": F + "8112184.jpg", "x": 6500, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Non sei un tecnico.", "white", 92)]},
    {"x": 500, "y": 340, "lines": [("Ma sai fare domande.", "violet", 104)], "cross": True},
    {"x": 1176, "y": 640, "lines": [("Le bollette", "violet", 96), ("Chiedi 12 mesi.", "white", 64), ("E il rendiconto", "white", 64), ("condominiale.", "white", 64)]},
    {"x": 2256, "y": 170, "lines": [("La caldaia", "violet", 96), ("Quando è stata", "white", 64), ("installata?", "white", 64), ("Chiedi il libretto.", "white", 64)]},
    {"x": 3336, "y": 170, "lines": [("I lavori", "violet", 96), ("Votati o previsti?", "white", 64)]},
    {"x": 4416, "y": 170, "lines": [("Gli ultimi due", "white", 70), ("verbali di assemblea.", "violet", 70)]},
    {"x": 5496, "y": 170, "lines": [("Le finestre", "violet", 96), ("Quando sono state", "white", 64), ("cambiate? Tutte?", "white", 64)]},
    {"x": 5496, "y": 800, "lines": [("Se conta,", "white", 60), ("chiedi la fattura.", "white", 60)]},
    *end(6480, "Ogni risposta,", "segnata come risposta."),
  ],
  "phones": [{"mock": M + "06-dentro-property-check.png", "x": 3960, "y": 380, "height": 940, "tilt": -4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "ink"},
}

STRADA = {"slides": 7, "photos": [
    {"file": F + "33486969.jpg", "x": 0, "focus": 0.5},
    {"file": F + "37382515.jpg", "x": 1700, "focus": 0.5},
    {"file": F + "30726119.jpg", "x": 3300, "focus": 0.5},
    {"file": F + "20508442.jpg", "x": 4900, "focus": 0.5},
    {"file": F + "5380028.jpg", "x": 6500, "focus": 0.4},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Hai visto la casa.", "white", 100)]},
    {"x": 620, "y": 340, "lines": [("E la strada?", "violet", 130)], "cross": True},
    {"x": 1176, "y": 680, "lines": [("Il supermercato", "violet", 90), ("Quanti minuti a piedi?", "white", 62), ("Sulle strade vere,", "white", 62), ("non in linea d'aria.", "white", 62)]},
    {"x": 2256, "y": 170, "lines": [("Scuole, parchi, mezzi", "violet", 78), ("Scegli tu", "white", 66), ("cosa conta.", "white", 66)]},
    {"x": 3336, "y": 170, "lines": [("Il tuo quartiere", "white", 76), ("sulla mappa.", "violet", 76)]},
    {"x": 4416, "y": 170, "lines": [("10 città", "violet", 150), ("Dati pubblicati,", "white", 62), ("zona per zona.", "white", 62)]},
    {"x": 5496, "y": 170, "lines": [("E di sera?", "white", 110)]},
    {"x": 5496, "y": 460, "lines": [("Una mappa non lo sa.", "violet", 72), ("Torna dopo il buio", "white", 62), ("e fai il giro", "white", 62), ("dell'isolato.", "white", 62)]},
    *end(6480, "Scegli la casa.", "E anche la strada."),
  ],
  "phones": [{"mock": M + "02-vivi-mappa.png", "x": 3960, "y": 380, "height": 940, "tilt": 4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

D = "06-dentro-property-check.png"
N = "07-misura-rumore-finestra.png"

ITEMS = [
    # ---------------------------------------------------------------- Wednesday 11
    chat(11, "08:00", "caldaia", ("7647325", 0.5), "Marco", "Agenzia", VIOLET_AV, "Caldaia quasi nuova 👌",
         [("me", "Di che anno è?", 0.0), ("them", "Recente, credo 🙂", 0.8), ("me", "Posso vedere il libretto?", 0.0)],
         "Recente quanto?\nChiedi il libretto.", "Come sta, lo dice un termotecnico.", D,
         "«Recente, credo.» Una data detta a memoria vale quanto chi la ricorda.\n\nChiedi quando è stata installata la caldaia e chiedi di vedere il libretto. Il limite: così hai una data e un libretto. Come sta l'apparecchio è una domanda da termotecnico."),
    ask(11, "lavori", "orange", "Quali lavori sono *votati* o previsti?", "Chiedi gli ultimi due verbali di assemblea."),
    card(11, "12:30", "consiglio-termosifoni", "violet", "IN VISITA", "Tocca *ogni* termosifone, in alto e in basso.",
         "Dieci minuti dopo aver acceso il riscaldamento."),
    film(11, "di-fronte", [
        ("7330179", 0.5, 1.3, "Affacciati.", None), ("8517524", 0.5, 1.2, "Cosa c'è", None),
        ("16668271", 0.5, 1.3, "*di fronte?*", None), ("3109518", 0.5, 1.2, "In alto.", None),
        ("38916207", 0.5, 1.2, "In basso.", None), ("6000765", 0.5, 1.4, "Da ogni *finestra.*", None),
        ("36377024", 0.5, 2.6, "Segna\n*cosa c'è.*", D),
    ], "Guarda fuori da ogni finestra: in alto, in basso e di fronte. Segna cosa c'è, Nesso lo tiene nel tuo registro.\n\nIl limite: è quello che c'è oggi. Un'area sgombra di fronte, fra due anni, è un edificio.",
       end="6798984"),
    card(11, "15:30", "fatto-fessura", "orange", "LO SAPEVI?", "Una fessura sotto la porta spesso è *voluta.*",
         "Può essere un'intercapedine di ventilazione, non un difetto."),
    {"id": "k-perche", "type": "carousel", "channel": "ig-it", "at": at(11, "18:00"), "slug": "carosello-perche-nesso",
     "panorama": PERCHE,
     "caption": "Un chatbot ti dice «dipende». In quella casa non è mai entrato. Scorri.\n\n"
                "Il rumore si misura nella stanza, con la finestra aperta e poi chiusa. Le spese si contano sul prezzo: €250.000 da un privato, prima casa, agenzia al 3%, mutuo di €175.000. "
                "Sono €14.687,50 in più del prezzo, prima di notaio e banca. È un calcolo sulle regole nazionali, non una consulenza.\n\n"
                "Prova Nesso: link in bio.\n\n"
                "Hai mai chiesto a un chatbot un consiglio sulla casa? Scrivilo nei commenti 👇\n"
                f"{SAVE}\n\n{TAGS}"},
    chat(11, "20:00", "vernice", ("7817155", 0.5), "Proprietario", "Annuncio", INK_AV, "Ho appena imbiancato tutto ✨",
         [("me", "Perché proprio quella parete?", 0.0), ("them", "Così, per rinfrescare 🙂", 0.9), ("me", "Me lo segno.", 0.0)],
         "Vernice fresca?\nChiedi perché.", "Una risposta resta una risposta.", D,
         "Quasi tutti gli interventi sono ordinaria manutenzione. Il motivo è la parte che non puoi vedere, quindi chiedilo.\n\nMettiti davanti alla vernice o all'intonaco nuovo e chiedi perché è stato riparato. Nesso segna quello che ti dicono come risposta di chi ha un interesse, non come fatto."),
    tomorrow(11, "verbali", "Spese basse oggi. E i *lavori già votati?*"),

    # ---------------------------------------------------------------- Thursday 12
    chat(12, "08:00", "verbali", ("4752623", 0.5), "Giulia", "Agenzia", VIOLET_AV, "Spese condominiali bassissime 💸",
         [("me", "E i lavori già votati?", 0.0), ("them", "Non mi risulta… 🤔", 0.9), ("me", "Posso leggere gli ultimi due verbali?", 0.0)],
         "Spese basse, oggi.\nE domani?", "I lavori votati stanno nei verbali.", D,
         "Le spese di oggi non dicono cosa ha già deciso il condominio.\n\nChiedi quali lavori sono votati o previsti e chiedi gli ultimi due verbali di assemblea. Il limite: una risposta a voce è completa quanto chi te la dà. I verbali sono il documento, leggili.",
         cat="cost"),
    ask(12, "finestre", "violet", "Quando sono state cambiate le *finestre?*", "Tutte? Se conta, chiedi se esiste una fattura."),
    card(12, "12:30", "consiglio-finestre", "orange", "IN VISITA", "Apri *ogni* finestra. Richiudila con la maniglia.",
         "Segna quelle che si incastrano o non chiudono a chiave."),
    film(12, "vicino", [
        ("7646797", 0.5, 1.2, "Incontri", None), ("7646491", 0.5, 1.3, "un *vicino?*", None),
        ("16668197", 0.5, 1.3, "Una domanda.", None), ("6247901", 0.5, 1.5, "«Com'è abitare qui,", None),
        ("8061106", 0.5, 1.5, "anche di *notte?*»", None),
        ("8814190", 0.5, 2.6, "Segna\n*cosa ha detto.*", D),
    ], "Se incontri un vicino, fai una domanda: com'è abitare qui, anche di notte?\n\nNesso la tiene come quello che ha detto. Il limite: è l'esperienza di una persona sola, che può avere un motivo suo.",
       end="7646762"),
    card(12, "15:30", "fatto-fonometro", "violet", "LO SAPEVI?", "Un telefono *non è* un fonometro.",
         "Confronta stanze misurate allo stesso modo. Con una soglia di legge, no."),
    chat(12, "20:00", "ascensore", ("7578478", 0.5), "Paolo", "Proprietario", INK_AV, "Ascensore silenziosissimo, giuro 🤫",
         [("me", "Posso misurare?", 0.0), ("them", "Misurare… l'ascensore? 😅", 0.9), ("me", "Dalla camera. Mentre qualcuno lo usa.", 0.0)],
         "30 secondi di silenzio.\nPoi l'ascensore.", "Il telefono confronta le due misure.", N,
         "Misura la camera in silenzio per 30 secondi. Poi misura di nuovo mentre qualcuno usa l'ascensore.\n\nIl limite: sono pochi minuti di un pomeriggio tranquillo. In un condominio l'ascensore lavora di più nelle due ore in cui non c'eri.",
         size=104),
    tomorrow(12, "bussa", "Bussa sul muro. *Poi su un altro.*"),

    # ---------------------------------------------------------------- Friday 13
    chat(13, "08:00", "bussa", ("7817153", 0.5), "Sara", "Agenzia", ORANGE_AV, "Muri spessi, non si sente niente 🧱",
         [("me", "Posso bussare?", 0.0), ("them", "Bussare? 😅", 0.8), ("me", "Qui e su un muro pieno.", 0.0)],
         "Bussa qui.\nPoi su un muro pieno.", "Altezza e volume. Il materiale no.", N,
         "Tieni il telefono a una spanna dal muro, batti un punto con le nocche e ripeti su un muro pieno. Poi confronta.\n\nIl limite: senti un'altezza e un volume, non un materiale. Intonaco su mattone e cartongesso possono suonare uguali, e il telefono sente anche la stanza.",
         size=104),
    ask(13, "sinistro", "orange", "C'è stato un *sinistro* con l'assicurazione?", "Una risposta. Nel fascicolo diventa verificabile."),
    card(13, "12:30", "consiglio-porta", "violet", "IN VISITA", "Luce dell'ingresso spenta. *Chiudi la porta.*",
         "Luce del pianerottolo accesa: cerca la luce lungo i bordi."),
    film(13, "termosifoni", [
        ("7646363", 0.5, 1.2, "Chiedi", None), ("7646363", 4.0, 1.2, "di accendere", None),
        ("6446329", 0.5, 1.5, "il *riscaldamento.*", None), ("7681165", 0.5, 1.3, "Dieci minuti.", None),
        ("8482308", 0.5, 1.2, "Poi tocca.", None), ("12910157", 0.5, 1.3, "Alto e *basso.*", None),
        ("8926989", 0.5, 2.6, "Ogni\n*termosifone.*", D),
    ], "Chiedi di accendere il riscaldamento. Aspetta dieci minuti e tocca la parte alta e bassa di ogni termosifone.\n\nIl limite: è un radiatore in un pomeriggio. Non dice niente sulla caldaia, sulla pressione dell'impianto, né su quanto costa scaldare questa casa a gennaio.",
       end="8293116"),
    card(13, "15:30", "fatto-muro", "orange", "LO SAPEVI?", "Un muro piano può nascondere *quanto uno ondulato.*",
         "La torcia mostra la superficie, non cosa c'è dietro."),
    {"id": "k-chiedi", "type": "carousel", "channel": "ig-it", "at": at(13, "18:00"), "slug": "carosello-chiedi",
     "panorama": CHIEDI,
     "caption": "Non serve essere un tecnico per fare le domande giuste. Scorri.\n\n"
                "Dodici mesi di bollette e il rendiconto condominiale. La data della caldaia e il libretto. I lavori votati o previsti, con gli ultimi due verbali. Quando sono state cambiate le finestre. "
                "Sono domande che Nesso ti ricorda in visita, e ogni risposta resta segnata come risposta di chi te l'ha data.\n\n"
                "Prova Nesso: link in bio.\n\n"
                "Tu cosa chiedi sempre in una visita? Scrivilo nei commenti 👇\n"
                f"{SAVE}\n\n{TAGS}"},
    chat(13, "20:00", "agente", ("8555713", 0.5), "Sara", "Amica", ORANGE_AV, "L'agente dice che è perfetta per noi 🥰",
         [("me", "Lui conosce la casa", 0.0), ("them", "E quindi?", 0.6), ("me", "Noi conosciamo noi 😄", 0.0)],
         "L'agente conosce la casa.\nTu conosci te.", "Scegli cosa conta. Nesso sceglie i controlli.", "01-home.png",
         "L'agente sa molte cose della casa. Se dormi col sonno leggero, lo sai tu.\n\nIn Nesso scegli cosa conta per te, come silenzio, luce o spese, e la visita si costruisce su quello. Alla fine hai un registro di cosa hai controllato e cosa resta aperto.",
         size=100),
    tomorrow(13, "metri", "85 metri quadri. *Quali?*"),

    # ---------------------------------------------------------------- Saturday 14
    chat(14, "08:00", "metri", ("7347759", 0.5), "Marco", "Agenzia", VIOLET_AV, "85 metri quadri, ben distribuiti 📐",
         [("me", "Commerciali o calpestabili?", 0.0), ("them", "Commerciali, certo 🙂", 0.9), ("me", "Quindi anche muri e cantina?", 0.0)],
         "85 metri quadri.\nQuali?", "Chiedi quale cifra è stata usata.", D,
         "Gli annunci italiani citano superfici diverse. La superficie commerciale comprende legittimamente i muri, i balconi e la cantina.\n\nScrivi in Nesso la superficie dell'annuncio: la affianca a quella che hai misurato. Il limite: è la differenza fra una stima e una dichiarazione, e non prova che qualcuno abbia dichiarato il falso."),
    ask(14, "edificio", "violet", "In che anno è stato costruito *l'edificio?*", "Guarda facciata e scala, poi chiedi."),
    card(14, "12:30", "consiglio-griglia", "orange", "IN VISITA", "Una striscia di fazzoletto sulla *griglia.*",
         "Lascia andare l'estremità inferiore: resta attaccata o cade?"),
    film(14, "divano", [
        ("4553192", 0.5, 1.3, "Il *divano*", None), ("4554442", 0.5, 1.1, "passa?", None),
        ("7033604", 0.5, 1.2, "Misura", None), ("4554461", 0.5, 1.2, "le porte", None),
        ("4553192", 4.0, 1.3, "più *strette.*", None),
        ("4554461", 4.0, 2.6, "Con la scansione\n*o con un metro.*", D),
    ], "Il divano passa? Misura le porte più strette prima di firmare, con la scansione di Nesso o con un metro.\n\nIl limite: la scansione misura il vano nello stipite, con uno o due centimetri di scarto. Con la porta aperta, l'anta e le cerniere se ne prendono qualche centimetro.",
       end="7817162"),
    card(14, "15:30", "fatto-macchia", "violet", "LO SAPEVI?", "Una macchia può essere *vecchia e asciutta.*",
         "E un muro su cui non c'è niente da vedere può comunque essere bagnato."),
    chat(14, "20:00", "tallone", ("7624028", 0.5), "Proprietario", "Annuncio", INK_AV, "Parquet rifatto, perfetto 🪵",
         [("me", "Posso attraversare la stanza battendo il tallone?", 0.0), ("them", "…prego? 😅", 0.9), ("me", "Per sentire se cede.", 0.0)],
         "Batti il tallone.\nSenti se cede.", "Al centro e vicino ai muri.", "08-misura-pavimento.png",
         "Attraversa la stanza battendo forte il tallone. Prova vicino ai muri e al centro: senti se il pavimento rimbalza o cede.\n\nIl limite: è un'impressione tua. Non misura quanto il pavimento reggerà, e da qui non si può concludere niente sulla portata."),
    tomorrow(14, "cappa", "La cappa aspira. *Ma dove va l'aria?*"),

    # ---------------------------------------------------------------- Sunday 15
    chat(15, "08:00", "cappa", ("4554454", 0.5), "Chiara", "Amica", VIOLET_AV, "Cucina nuova, cappa potentissima 🍳",
         [("me", "E l'aria dove va?", 0.0), ("them", "Fuori… credo 🤔", 0.9), ("me", "Chiedo.", 0.0)],
         "Cappa accesa.\nDove va l'aria?", "Un fazzoletto mostra se tira. Il resto chiedilo.", D,
         "Tieni un fazzoletto sulla cappa, a ogni velocità. Guarda il condotto sopra. Poi chiedi dove va l'aria.\n\nIl limite: la carta mostra che la ventola sta tirando. Dove finisce l'aria lo sai solo dalla risposta, ed è un'affermazione di chi risponde."),
    ask(15, "cause", "orange", "Ci sono *cause in corso* nel condominio?", "E morosità? Chiedi gli ultimi due verbali."),
    card(15, "12:30", "consiglio-giunzioni", "violet", "IN VISITA", "Passa il piede su *ogni giunzione* fra due pavimenti.",
         "Segna ogni gradino, spazio o rialzo."),
    film(15, "di-sopra", [
        ("8558458", 0.5, 1.2, "Di sopra", None), ("8558458", 3.0, 1.2, "*chi c'è?*", None),
        ("7507813", 0.5, 1.4, "Telefono in camera.", None), ("7507813", 3.0, 1.3, "Porta chiusa.", None),
        ("8558458", 6.0, 1.5, "30 secondi\nin *silenzio.*", None),
        ("13556489", 0.5, 2.6, "Poi ascolta\n*tu.*", N),
    ], "Posa il telefono in camera da letto, chiudi la porta e stai in silenzio per 30 secondi. Poi ascolta tu stesso altri 30 secondi.\n\nIl limite: Nesso misura di quanto il secondo più alto si è alzato sopra il resto. Non dice cosa ha fatto il rumore, e trenta secondi prendono quello che capitava in quel momento.",
       end="7579472"),
    card(15, "15:30", "fatto-quadro", "orange", "LO SAPEVI?", "Il quadro elettrico *non si apre.*",
         "Fotografalo chiuso. Il resto è lavoro da elettricista."),
    {"id": "k-strada", "type": "carousel", "channel": "ig-it", "at": at(15, "18:00"), "slug": "carosello-strada",
     "panorama": STRADA,
     "caption": "La casa la vedi in una visita. La strada la vivi tutti i giorni. Scorri.\n\n"
                "In Nesso i quartieri di 10 città italiane si leggono con dati pubblicati: Agenzia delle Entrate (OMI), ISTAT, OpenStreetMap. I minuti a piedi si contano sulle strade vere. "
                "La sera invece la vedi solo tu: torna dopo il buio e fai il giro dell'isolato.\n\n"
                "Prova Nesso: link in bio.\n\n"
                "Cosa vuoi trovare a cinque minuti da casa? Scrivilo nei commenti 👇\n"
                f"{SAVE}\n\n#comprarecasa #cercocasa #quartiere #primacasa #consiglicasa"},
    chat(15, "20:00", "sciacquone", ("5418696", 0.5), "Paolo", "Proprietario", INK_AV, "Bagno rifatto, tutto nuovo 🚿",
         [("me", "Posso tirare lo sciacquone?", 0.0), ("them", "Come, scusi? 😅", 0.8), ("me", "Col timer.", 0.0)],
         "Tira lo sciacquone.\nAvvia il timer.", "Poi ascolta 30 secondi se scorre acqua.", D,
         "Tira lo sciacquone, avvia il timer e fermalo quando la cassetta smette di riempirsi. Poi ascolta per 30 secondi se scorre acqua.\n\nIl limite: se continua a scorrere, il gruppo di carico lascia passare acqua. Quale pezzo sia, e come si ripara, è una domanda da idraulico."),
    {"id": "s-checklist-15", "type": "story", "channel": "ig-it", "at": at(15, "21:30"), "slug": "storia-checklist-visita",
     "theme": "violet", "series": None,
     "card": {"kind": "cta", "text": "Domani hai una visita? *82 controlli* ti aspettano.", "button": "Link in bio"}},
]
