"""The week's four carousels, 2 to 8 November, redone seamless (founder, 2026-11-01): one long
picture cut into slides, only the opening sentence and one phone across a cut, plain words, real
photos, and the last slide ends on "Prova Nesso" with the logo straight on the photo.

Costs use the app's own example, the one on the phone: €250.000 from a private seller, first home,
no rendita entered, agency at 3%, mortgage of €175.000. Registro €5.000, ipotecaria and catastale
€50 + €50, agency €7.500 + €1.650 VAT, mortgage tax €437,50: €14.687,50 over the price.
The mortgage rights are Banca d'Italia's, "Il mutuo ipotecario in parole semplici" (2026).
The myths are the Prepara sources (nesso_mobile CLAUDE.md §8ap).
Photos: Pexels License, ~/Documents/GitHub/nesso-assets/pexels-photos/<id>.jpg.
"""

F = "~/Documents/GitHub/nesso-assets/pexels-photos/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"


def at(day):
    return f"2026-11-{day:02d}T18:00+01:00"


def end(x, first, second):
    """The last slide: the thought, the call, the logo on the photo."""
    return [
        {"x": x + 96, "y": 150, "lines": [(first, "white", 84), (second, "violet", 76)]},
        {"x": x + 96, "y": 700, "lines": [("Prova Nesso  →", "orange", 84), ("link in bio", "white", 52)]},
    ]


COSTI = {"slides": 7, "photos": [
    {"file": F + "4307963.jpg", "x": 0, "focus": 0.5},
    {"file": F + "30139520.jpg", "x": 1700, "focus": 0.4},
    {"file": F + "16600134.jpg", "x": 3400, "focus": 0.5},
    {"file": F + "29034871.jpg", "x": 5100, "focus": 0.6},
    {"file": F + "7579192.jpg", "x": 6700, "focus": 0.3},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Casa trovata: €250.000.", "white", 70)]},
    {"x": 420, "y": 330, "lines": [("Ma quanto paghi davvero?", "violet", 100)], "cross": True},
    {"x": 1176, "y": 720, "lines": [("Tasse d'acquisto", "white", 70), ("€5.100", "violet", 150), ("se compri da un privato", "white", 50)]},
    {"x": 2256, "y": 170, "lines": [("Agenzia al 3%", "white", 70), ("€9.150", "violet", 150), ("con l'IVA al 22%", "white", 50)]},
    {"x": 3540, "y": 170, "lines": [("Tassa sul mutuo", "white", 64), ("€437,50", "violet", 130), ("su €175.000 di prestito", "white", 50)]},
    {"x": 4416, "y": 560, "lines": [("In più del prezzo:", "white", 84), ("€14.687,50", "violet", 130), ("prima casa, da un privato", "white", 50)]},
    {"x": 5496, "y": 150, "lines": [("E il notaio?", "white", 110)]},
    {"x": 5496, "y": 420, "lines": [("Nessuna legge", "violet", 80), ("fissa il suo prezzo.", "violet", 80)]},
    {"x": 5496, "y": 800, "lines": [("Chiedi un preventivo", "white", 64), ("scritto, a più notai.", "white", 64)]},
    *end(6480, "Fai il conto", "sul tuo prezzo."),
  ],
  "phones": [{"mock": M + "04-costi.png", "x": 3240, "y": 330, "height": 980, "tilt": -4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

VISITA = {"slides": 8, "photos": [
    {"file": F + "19916712.jpg", "x": 0, "focus": 0.5},
    {"file": F + "12932887.jpg", "x": 1400, "focus": 0.35},
    {"file": F + "6077368.jpg", "x": 2800, "focus": 0.5},
    {"file": F + "8092188.jpg", "x": 4300, "focus": 0.4},
    {"file": F + "4010280.jpg", "x": 5900, "focus": 0.5},
    {"file": F + "4307929.jpg", "x": 7300, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("20 minuti di visita.", "white", 96)]},
    {"x": 470, "y": 340, "lines": [("25 anni di mutuo.", "violet", 110)], "cross": True},
    {"x": 1176, "y": 680, "lines": [("Rumore", "violet", 110), ("Finestra aperta, poi chiusa.", "white", 58), ("30 secondi ciascuna.", "white", 58)]},
    {"x": 2256, "y": 170, "lines": [("Luce", "violet", 110), ("Sulla parete di fondo,", "white", 60), ("non sul davanzale.", "white", 60)]},
    {"x": 3336, "y": 170, "lines": [("Pavimento", "violet", 100), ("Telefono a terra.", "white", 60), ("Leggi, giralo, rileggi.", "white", 60)]},
    {"x": 4620, "y": 170, "lines": [("Umidità", "violet", 100), ("Guarda in basso,", "white", 60), ("negli angoli,", "white", 60), ("dietro i mobili.", "white", 60)]},
    {"x": 5496, "y": 640, "lines": [("Acqua", "violet", 110), ("Apri cucina e doccia", "white", 60), ("insieme.", "white", 60), ("Guarda il getto.", "white", 60)]},
    {"x": 6576, "y": 170, "lines": [("Sotto il lavello", "violet", 96), ("Torcia accesa:", "white", 60), ("un dito su ogni raccordo.", "white", 60)]},
    *end(7560, "82 controlli", "per la tua visita."),
  ],
  "phones": [{"mock": M + "08-misura-pavimento.png", "x": 4320, "y": 400, "height": 920, "tilt": -4}],
  "mark": {"x": 8100, "y": 1110, "height": 150, "word": "white"},
}

MITI = {"slides": 7, "photos": [
    {"file": F + "8482895.jpg", "x": 0, "focus": 0.35},
    {"file": F + "19916712.jpg", "x": 1500, "focus": 0.5},
    {"file": F + "8092188.jpg", "x": 3200, "focus": 0.45},
    {"file": F + "6077368.jpg", "x": 4900, "focus": 0.5},
    {"file": F + "7579192.jpg", "x": 6400, "focus": 0.3},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Vendi casa?", "white", 110)]},
    {"x": 330, "y": 360, "lines": [("«Fai il caffè prima della visita.»", "violet", 80)], "cross": True},
    {"x": 1176, "y": 720, "lines": [("Un prezzo più alto?", "white", 64), ("Nessuno studio", "violet", 84), ("lo mostra.", "violet", 84)]},
    {"x": 2256, "y": 170, "lines": [("«Metti musica classica.»", "white", 68)]},
    {"x": 2256, "y": 700, "lines": [("Nei negozi aiuta un po'.", "white", 60), ("Sulle offerte per una casa:", "white", 60), ("nessuna prova.", "violet", 90)]},
    {"x": 3336, "y": 170, "lines": [("«Svuotala,", "white", 76), ("sembra più grande.»", "white", 76)]},
    {"x": 3336, "y": 700, "lines": [("Con i mobili sembrava", "white", 58), ("un po' più piccola.", "white", 58), ("In realtà virtuale:", "white", 58), ("nessuna differenza.", "violet", 76)]},
    {"x": 4416, "y": 170, "lines": [("«L'home staging", "white", 70), ("alza il prezzo.»", "white", 70)]},
    {"x": 4416, "y": 640, "lines": [("Nell'esperimento", "white", 56), ("la casa sembrava", "white", 56), ("più vivibile.", "white", 56), ("Il valore stimato", "violet", 64), ("restava quello.", "violet", 64)]},
    {"x": 5720, "y": 170, "lines": [("Cosa conta,", "white", 84), ("secondo gli studi:", "white", 70)]},
    {"x": 5720, "y": 560, "lines": [("classe energetica,", "violet", 62), ("luce, silenzio,", "violet", 62), ("un terrazzo.", "violet", 62)]},
    *end(6480, "Prepara la casa", "con le prove."),
  ],
  "phones": [{"mock": M + "05-prepara.png", "x": 5400, "y": 400, "height": 920, "tilt": 4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

MUTUO = {"slides": 7, "photos": [
    {"file": F + "7579211.jpg", "x": 0, "focus": 0.5},
    {"file": F + "16600134.jpg", "x": 1700, "focus": 0.5},
    {"file": F + "29034871.jpg", "x": 3400, "focus": 0.6},
    {"file": F + "8368754.jpg", "x": 5100, "focus": 0.6},
    {"file": F + "4307929.jpg", "x": 6600, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("In banca per il mutuo.", "white", 78)]},
    {"x": 380, "y": 330, "lines": [("Sai cosa ti devono dare?", "violet", 96)], "cross": True},
    {"x": 1176, "y": 680, "lines": [("Il PIES", "violet", 120), ("un foglio con tutti", "white", 60), ("i costi del tuo mutuo.", "white", 60), ("Gratis, prima di firmare.", "white", 60)]},
    {"x": 2256, "y": 170, "lines": [("7 giorni", "violet", 130), ("almeno, per pensarci", "white", 60), ("sull'offerta finale.", "white", 60)]},
    {"x": 3540, "y": 170, "lines": [("Cambiare banca", "violet", 76), ("quando vuoi,", "white", 60), ("senza costi né penali.", "white", 60)]},
    {"x": 4416, "y": 640, "lines": [("Chiudere prima", "violet", 96), ("tutto o in parte,", "white", 60), ("senza penali.", "white", 60), ("Se il mutuo è per la casa.", "white", 50)]},
    {"x": 5496, "y": 170, "lines": [("Chiedi il PIES", "white", 84), ("a più banche.", "white", 84)]},
    {"x": 5496, "y": 640, "lines": [("Confronta il TAEG:", "violet", 76), ("il costo totale", "white", 60), ("del mutuo, in %.", "white", 60)]},
    *end(6480, "Rata e spese", "sul tuo prezzo."),
  ],
  "phones": [{"mock": M + "04-costi.png", "x": 3240, "y": 330, "height": 980, "tilt": -4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

CAPTIONS = {
    "costi": ("Comprare la prima casa: quanto si paga oltre al prezzo? Scorri.\n\n"
              "L'esempio è quello dell'app: €250.000 da un privato, prima casa, agenzia al 3%, mutuo di €175.000. "
              "Tasse €5.100, agenzia €9.150 con l'IVA, tassa sul mutuo €437,50: €14.687,50 in più del prezzo. "
              "Se indichi la rendita catastale, il registro di solito scende.\n\n"
              "Notaio, banca e assicurazione a parte: nessuna legge li fissa, servono preventivi scritti.\n\n"
              "Prova Nesso: link in bio. È un calcolo sulle regole nazionali, non una consulenza.\n"
              "Fonti: DPR 131/1986, D.Lgs. 23/2011, DPR 633/1972, DPR 601/1973.\n\n"
              "Quale spesa ti ha sorpreso di più? Scrivilo nei commenti 👇\n"
              "Salvalo prima di firmare 📌\nMandalo a chi sta comprando casa.\n\n"
              "#comprarecasa #primacasa #mutuo #notaio #consiglicasa"),
    "visita": ("Una visita dura venti minuti. Il mutuo, venticinque anni. Scorri.\n\n"
               "Rumore, luce, pavimento, umidità, acqua, sotto il lavello: sei controlli che fai in visita, molti col telefono in mano. "
               "Nella checklist di Nesso sono 82, e ognuno dice anche cosa non può stabilire.\n\n"
               "E una regola sui soldi: nessuna caparra prima di aver visto la casa di persona.\n\n"
               "Prova Nesso: link in bio.\n\n"
               "Tu cosa guardi per primo in una casa? Scrivilo nei commenti 👇\n"
               "Salvalo per la prossima visita 📌\nMandalo a chi sta cercando casa.\n\n"
               "#cercocasa #visitacasa #comprarecasa #affitto #consiglicasa"),
    "miti": ("Caffè, musica, home staging, stanze vuote: abbiamo cercato gli studi dietro i consigli più ripetuti per vendere casa. Scorri.\n\n"
             "Caffè: una meta-analisi di 55 articoli sul profumo d'ambiente, nei negozi e negli hotel. Musica: 32 studi nei negozi. "
             "Home staging: l'esperimento di Lane, Seiler e Seiler. Stanze vuote: un test su un modello e uno in realtà virtuale.\n\n"
             "In Nesso, Prepara divide i consigli in tre gruppi: cosa la ricerca ha visto nel prezzo, cosa rende visibile un valore che c'è già, cosa cambia solo la visita.\n\n"
             "Prova Nesso: link in bio.\n\n"
             "Quale consiglio hai sentito più spesso? Scrivilo nei commenti 👇\n"
             "Salvalo se vendi o affitti casa 📌\nMandalo a chi sta preparando la sua.\n\n"
             "#vendocasa #venderecasa #homestaging #immobiliare #consiglicasa"),
    "mutuo": ("Prima di firmare un mutuo per la casa: cosa ti deve la banca. Scorri.\n\n"
              "Il PIES, gratuito e personalizzato, prima che tu sia vincolato. Almeno 7 giorni per valutare l'offerta vincolante. "
              "La portabilità verso un'altra banca, senza costi né penali. L'estinzione anticipata, tutta o in parte, senza penali.\n\n"
              "Chiedi il PIES a più banche e confronta il TAEG. Rata, imposte e spese sul tuo prezzo sono nel calcolatore di Nesso.\n\n"
              "Prova Nesso: link in bio.\nFonte: Banca d'Italia, Il mutuo ipotecario in parole semplici (2026).\n\n"
              "Hai già chiesto il PIES? Scrivilo nei commenti 👇\n"
              "Salvalo prima di andare in filiale 📌\nMandalo a chi sta per chiedere un mutuo.\n\n"
              "#mutuo #primacasa #comprarecasa #casa #banca"),
}

ITEMS = [
    {"id": f"k-0{i}", "type": "carousel", "channel": "ig-it", "at": at(day), "slug": f"carosello-{name}",
     "panorama": spec, "caption": CAPTIONS[name]}
    for i, (day, name, spec) in enumerate([(2, "costi", COSTI), (4, "visita", VISITA), (6, "miti", MITI), (8, "mutuo", MUTUO)], 1)
]
