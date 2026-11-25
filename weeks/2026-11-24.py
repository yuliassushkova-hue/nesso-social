"""@nesso_italia, Tuesday 24 November 2026 onward.

Black Friday is the app's welcome gift (nesso_mobile `src/lib/welcome-gift.ts`, live since 16 November):
an account made from the app's gift sheet by 1 December 23:59 Rome gets Full for 2 months, no card, and
goes back to Free on its own. The app is on Android; the iPhone app is not out yet. The words here follow
the sheet's own Italian copy (`src/content/welcome-gift.ts`). Value: Full €6,99 a month × 2 = €13,98.

Music: Meta Sound Collection, Reels Sound pick, one track per Reel.
"""
import runpy
from pathlib import Path

HERE = Path(__file__).parent
BASE = runpy.run_path(str(HERE / "2026-11-09.py"))
at = BASE["at"]
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"
LINK = "Scarica l'app · link in bio"
TAGS = "#blackfriday #comprarecasa #cercocasa #visitacasa #primacasa"

BF_BODY = (
    "BLACK FRIDAY: scarica l'app Nesso e crea un account entro il 1° dicembre. Ricevi il piano Full per 2 mesi, "
    "un valore di €13,98. Nulla da pagare, nessuna carta richiesta. Allo scadere dei 2 mesi torna da solo a Free.\n\n"
    "L'app c'è per Android, quella per iPhone è in arrivo. Il link è in bio.\n\n"
    "Con Full hai tutti i controlli per la visita, le mappe dei quartieri e i costi di acquisto riga per riga.\n\n"
    "Chi conosci che sta cercando casa? Taggalo nei commenti 👇\n"
    "Mandalo a chi sta per firmare.\n\n" + TAGS
)

ITEMS = [
    {"id": "r-black-friday-1", "type": "reel", "channel": "ig-it", "at": at(24, "20:00"), "slug": "reel-black-friday",
     "theme": "black", "progress": False, "music": "ready-for-action", "music_gain": 0.6,
     "cards": [
         {"kind": "fact", "secs": 2.6, "label": "BLACK FRIDAY", "text": "2 mesi di Full, *gratis.*",
          "sub": "Per i nuovi account creati dall'app Nesso.", "size": 116},
         {"kind": "big", "secs": 2.4, "over": "Un valore di", "text": "€13,98", "sub": "Nulla da pagare. Nessuna carta."},
         {"kind": "hook", "secs": 2.8, "text": "Scarica l'app.", "sub": "Android ora. iPhone in arrivo.",
          "phone": M + "01-home.png", "phone_height": 900, "phone_top": 1000},
         {"kind": "fact", "secs": 2.6, "label": "FINO AL", "text": "1° dicembre", "size": 124,
          "sub": "Alle 23:59, ora italiana. Dopo 2 mesi torna da solo a Free."},
         {"kind": "brand", "secs": 2.2, "sub": LINK},
     ],
     "caption": BF_BODY},
    {"id": "s-black-friday-24", "type": "story", "channel": "ig-it", "at": at(24, "21:30"), "slug": "storia-black-friday",
     "theme": "black", "series": None,
     "card": {"kind": "cta", "text": "Black Friday: *2 mesi di Full* gratis, dall'app.", "button": "Link in bio"}},
]

# ---------------------------------------------------------------- the rubrics, Wednesday 25 onward
W17 = runpy.run_path(str(HERE / "2026-11-17.py"))
card, ask, words, serie, caption = W17["card"], W17["ask"], W17["words"], W17["serie"], W17["caption"]
ORANGE = (249, 115, 22)
S = "~/Documents/GitHub/nesso-assets/stills/"
SAVE = "Salvalo per la prossima visita 📌\nMandalo a chi sta cercando casa."
FILM_TAGS = "#cercocasa #film #casedeifilm #visitacasa #consiglicasa"


def guess(day, time, slug, rounds, music, body):
    """Quiz Reel on stills: for each round the photo with the question, then the answer."""
    clips, cards = [], []
    for photo, focus, question, answer, note in rounds:
        clips.append({"file": S + photo, "focus": focus, "secs": 2.8})
        cards.append({"kind": "caption", "secs": 2.8, "y": 260, "align": "center",
                      "blocks": [{"text": "DI CHE FILM È QUESTA CASA?", "style": "orange", "size": 56}, {"text": question, "style": "white", "size": 64}]})
        clips.append({"file": S + photo, "focus": focus, "secs": 2.0, "out": True})
        cards.append({"kind": "caption", "secs": 2.0, "y": 1180, "align": "center",
                      "blocks": [{"text": answer, "style": "violet", "size": 76}, {"text": note, "style": "white", "size": 52}]})
    clips.append({"file": S + rounds[0][0], "focus": rounds[0][1], "secs": 2.4})
    cards.append({"kind": "brand", "sub": "Prova Nesso · link in bio", "secs": 2.4})
    return {"id": f"r-{slug}", "type": "reel", "channel": "ig-it", "at": at(day, time), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": clips, "cards": cards, "caption": body,
            "music": music, "music_gain": 0.55}


HOME_ALONE = {"title": "La casa di Kevin", "show": "Mamma, ho perso l'aereo · Winnetka, Illinois",
              "cover": S + "commons-home-alone-house-01-9807303934-.jpg", "cover_focus": 0.55,
              "cover_credit": "Foto: Ben Schumin, CC BY-SA 2.0",
              "slides": [
                  {"photo": S + "commons-home-alone-house-2026.jpg", "head": "COSA CI PIACE", "credit": "Foto: Kidfly182, CC BY 4.0",
                   "lines": ["Mattoni rossi, tre piani e un giardino davanti.", "Camere per tutta la famiglia. E per i cugini.", "Una via tranquilla, piena di alberi."]},
                  {"photo": S + "commons-home-alone-house-01-9807303934-.jpg", "focus": 0.3, "head": "COSA CONTROLLEREMMO", "chip": ORANGE, "credit": "Foto: Ben Schumin, CC BY-SA 2.0",
                   "lines": ["La caldaia in cantina fa paura a Kevin.", "Tu chiedi quando è stata installata e chiedi il libretto.", "Come sta, lo dice un termotecnico."]},
                  {"photo": S + "commons-home-alone-house-2026.jpg", "focus": 0.75, "head": "A NATALE", "credit": "Foto: Kidfly182, CC BY 4.0",
                   "lines": ["Chiedi di accendere il riscaldamento.", "Dopo dieci minuti tocca ogni termosifone, in alto e in basso.", "Apri ogni finestra e richiudila: chiude a chiave?"]},
              ],
              "ask": "La lasceresti a un bambino di 8 anni?", "ask_sub": "Noi prima chiederemmo il libretto della caldaia."}

BIG_BANG = {"title": "L'appartamento 4A", "show": "The Big Bang Theory · Pasadena",
            "cover": S + "commons-the-big-bang-theory-apartment-4a-6163979146-.jpg", "cover_focus": 0.5,
            "cover_credit": "Foto: NASA Blueshift, CC BY 2.0",
            "slides": [
                {"photo": S + "commons-the-big-bang-theory-apartment-4a-6196882054-.jpg", "head": "COSA CI PIACE", "credit": "Foto: Chester, CC BY 2.0",
                 "lines": ["Soggiorno grande, cucina a vista.", "Due camere: due coinquilini, ognuno con la sua porta.", "La vicina proprio di fronte, sul pianerottolo."]},
                {"photo": S + "commons-the-big-bang-theory-hallway-6196388577-.jpg", "head": "COSA CONTROLLEREMMO", "chip": ORANGE, "credit": "Foto: Chester, CC BY 2.0",
                 "lines": ["L'ascensore è rotto per quasi tutta la serie: si sale a piedi.", "Chiedi se i lavori sono votati e leggi gli ultimi due verbali.", "Il divano passa per le scale? Misura prima."]},
                {"photo": S + "commons-the-big-bang-theory-apartment-4a-6163979146-.jpg", "focus": 0.3, "head": "E IL RUMORE?", "credit": "Foto: NASA Blueshift, CC BY 2.0",
                 "lines": ["La porta d'ingresso dà sul pianerottolo.", "Misura 30 secondi con la porta aperta, poi 30 con la porta chiusa.", "Il telefono confronta le due misure."]},
            ],
            "ask": "Quarto piano senza ascensore: firmeresti?", "ask_sub": "Sheldon sì. E tu?"}

POTTER = {"title": "4 Privet Drive", "show": "Harry Potter · Little Whinging, Surrey",
          "cover": S + "commons-privet-drive-warner-bros-studios-london-the-making-of-harry-potter-12.jpg", "cover_focus": 0.5,
          "cover_credit": "Foto: Ank Kumar, CC BY-SA 4.0",
          "slides": [
              {"photo": S + "commons-4-privet-drive-little-whinging-surrey-geograph-3264264.jpg", "head": "COSA CI PIACE", "credit": "Foto: Richard Croft, CC BY-SA 2.0",
               "lines": ["Villetta con garage e giardino davanti.", "Una strada tranquilla, tutte le case uguali.", "Il vialetto per due macchine."]},
              {"photo": S + "commons-cupboard-under-the-stairs-2025-.jpg", "focus": 0.45, "head": "IL SOTTOSCALA", "chip": ORANGE, "credit": "Foto: S. Perquin, CC BY-SA 4.0",
               "lines": ["Harry ci dorme per dieci anni.", "In Italia una camera singola deve avere almeno 9 m² e 2,70 m di altezza.", "Il sottoscala non è una camera (DM 5 luglio 1975)."]},
              {"photo": S + "commons-privet-drive-warner-bros-studios-london-the-making-of-harry-potter-03.jpg", "focus": 0.5, "head": "IN VISITA", "credit": "Foto: Ank Kumar, CC BY-SA 4.0",
               "lines": ["Ti mostrano una stanza in più?", "Chiedi se è nella planimetria come camera.", "E misura l'altezza del soffitto."]},
          ],
          "ask": "Dormiresti nel sottoscala?", "ask_sub": "Anche solo una notte."}

ITEMS += [
    # ---------------------------------------------------------------- Wednesday 25
    guess(25, "08:00", "indovina-il-film", [
        ("commons-home-alone-house-2026-001.jpg", 0.5, "Una famiglia parte per Parigi. Uno resta qui.", "Mamma, ho perso l'aereo", "Winnetka, Illinois"),
        ("commons-privet-drive-warner-bros-studios-london-the-making-of-harry-potter-11.jpg", 0.5, "Un ragazzo dorme nel sottoscala.", "Harry Potter", "4 Privet Drive"),
        ("commons-the-big-bang-theory-apartment-4a-5029599593-.jpg", 0.5, "L'ascensore qui non funziona mai.", "The Big Bang Theory", "Appartamento 4A, Pasadena"),
    ], "style-check",
        "Tre case, tre film. Quante ne hai indovinate? Scrivi il punteggio nei commenti 👇\n\n"
        "Questa settimana su Nesso le guardiamo come in una visita: cosa ci piace e cosa controlleremmo. Mercoledì la casa di Kevin, venerdì l'appartamento 4A, domenica 4 Privet Drive.\n\n"
        + SAVE + "\n\nFoto: Kidfly182 (CC BY 4.0), Ank Kumar (CC BY-SA 4.0), NASA Blueshift (CC BY 2.0), Wikimedia Commons.\n\n" + FILM_TAGS),
    ask(25, "caldaia", "orange", "Quando è stata installata *la caldaia?*", "Chiedi anche il libretto."),
    card(25, "12:30", "consiglio-finestre-chiave", "violet", "IN VISITA", "Apri ogni finestra. *Chiude a chiave?*",
         "Segna quelle che si incastrano."),
    card(25, "15:30", "fatto-sottoscala", "orange", "LO SAPEVI?", "Una camera singola deve avere *almeno 9 m².*",
         "E un'altezza di 2,70 m. DM 5 luglio 1975."),
    serie(25, "18:00", "casa-di-kevin", HOME_ALONE,
          "La casa di Mamma, ho perso l'aereo esiste davvero: è a Winnetka, vicino a Chicago. Mattoni rossi, tre piani, una via piena di alberi. Scorri.\n\n"
          "Cosa controlleremmo prima di Natale: la caldaia in cantina, quella che fa paura a Kevin. Chiedi quando è stata installata e chiedi il libretto. "
          "Poi accendi il riscaldamento e tocca ogni termosifone dopo dieci minuti.\n\n"
          "La lasceresti a un bambino di 8 anni? Scrivilo nei commenti 👇\n" + SAVE +
          "\n\nFoto: Ben Schumin (CC BY-SA 2.0), Kidfly182 (CC BY 4.0), Wikimedia Commons.\n\n" + FILM_TAGS),
    card(25, "21:30", "domani-black-friday", "violet", "BLACK FRIDAY", "2 mesi di Full, *gratis.* Fino al 1° dicembre.",
         "Crea l'account dall'app Nesso. Link in bio."),

    # ---------------------------------------------------------------- Friday 27
    serie(27, "18:00", "appartamento-4a", BIG_BANG,
          "L'appartamento 4A di The Big Bang Theory: soggiorno grande, due camere, la vicina di fronte. E un ascensore rotto per quasi tutta la serie. Scorri.\n\n"
          "Cosa controlleremmo: se i lavori all'ascensore sono votati, negli ultimi due verbali di assemblea. E il rumore dal pianerottolo: 30 secondi con la porta aperta, 30 con la porta chiusa.\n\n"
          "Quarto piano senza ascensore: firmeresti? Scrivilo nei commenti 👇\n" + SAVE +
          "\n\nFoto del set agli studi Warner Bros: NASA Blueshift, Chester (CC BY 2.0), Wikimedia Commons.\n\n" + FILM_TAGS),

    # ---------------------------------------------------------------- Sunday 29
    serie(29, "18:00", "privet-drive", POTTER,
          "4 Privet Drive: villetta con garage, giardino curatissimo, una strada di case tutte uguali. E un sottoscala dove Harry dorme per dieci anni. Scorri.\n\n"
          "In Italia una camera singola deve avere almeno 9 m² e un soffitto di 2,70 m (DM 5 luglio 1975). Se in visita ti mostrano una stanza in più, chiedi se è nella planimetria come camera.\n\n"
          "Dormiresti nel sottoscala? Scrivilo nei commenti 👇\n" + SAVE +
          "\n\nFoto: Ank Kumar, S. Perquin (CC BY-SA 4.0), Richard Croft (CC BY-SA 2.0), Wikimedia Commons.\n\n" + FILM_TAGS),
]

# ---------------------------------------------------------------- the daily Reels, Wednesday 25 onward
chat, film, tune = BASE["chat"], BASE["film"], W17["tune"]
ORANGE_AV, VIOLET_AV, INK_AV = BASE["ORANGE_AV"], BASE["VIOLET_AV"], BASE["INK_AV"]
N = "07-misura-rumore-finestra.png"
D = "06-dentro-property-check.png"


def serif(day, slug, shots, body, end, music, gain=0.6):
    item = film(day, slug, shots, body, end)
    item.update({"music": music, "music_gain": gain, "music_start": 0.0})
    return item


ITEMS += [
    serif(25, "dicembre", [
        ("35449771", 0.5, 1.3, "Visiti casa", None), ("6273843", 0.5, 1.2, "a *dicembre?*", None),
        ("34967956", 0.5, 1.4, "Chiedi di accendere", None), ("3201320", 0.5, 1.3, "il *riscaldamento.*", None),
        ("29538916", 0.5, 1.5, "Dieci minuti.\nPoi tocca.", None),
        ("6273843", 4.0, 2.6, "Ogni\n*termosifone.*", D),
    ], "A dicembre una visita dice cose che d'estate non dice. Chiedi di accendere il riscaldamento, aspetta dieci minuti e tocca la parte alta e bassa di ogni termosifone.\n\n"
       "Il limite: è un radiatore in un pomeriggio. Non dice niente sulla caldaia, sulla pressione dell'impianto, né su quanto costa scaldare questa casa a gennaio.",
       "34963013", "this-can-t-be-possible"),
    tune(chat(25, "20:00", "tubi", ("5614823", 0.5), "Paolo", "Proprietario", INK_AV, "Impianto rifatto, silenziosissimo 🔇",
              [("me", "Posso aprire l'acqua e chiuderla forte?", 0.0), ("them", "Forte? 😅", 0.8), ("me", "Per sentire i tubi.", 0.0)],
              "Apri. Chiudi forte.\nAscolta i tubi.", "Il telefono misura di quanto sale il rumore.", N,
              "Misura il bagno in silenzio per 20 secondi. Poi apri il rubinetto per 15 secondi e chiudilo forte, e stai in silenzio mentre il telefono ascolta.\n\n"
              "Il limite: Nesso misura di quanto il secondo più alto si è alzato sopra la stanza. Non dice cosa l'ha causato: quella è una domanda da idraulico.",
              size=104), "waves"),
]
