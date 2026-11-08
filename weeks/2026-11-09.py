"""@nesso_italia, week of 9 November 2026. Monday and Tuesday first, the rest of the week follows.

Every step and every limit is the app's own text from nesso.fit/it/checklist-visita-casa, read on
8 November. The €250.000 example is the costs screen on the phone (see weeks/2026-11-02-carousels.py).
Perché Nesso is the pillar in CREATIVE.md §7: the two posts here are the ones the founder approved
on 1 November (weeks/next-perche-nesso.py and -carousel.py).

Rome times. Reels 08:00, 13:00, 20:00. Stories 09:30, 12:30, 15:30, 21:30. Carousels 18:00.
Footage and photos: Pexels License. Sounds and music: Mixkit.
"""
import runpy
from pathlib import Path

P = "~/Documents/GitHub/nesso-assets/pexels/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"
LINK = "Prova Nesso · link in bio"
ORANGE_AV, VIOLET_AV, INK_AV = (249, 115, 22), (90, 62, 192), (52, 33, 111)

QUESTION_CHAT = "Ti è mai successo? Raccontalo nei commenti 👇"
FILM = {
    "visit": ("Tu cosa guardi per primo in una casa? Scrivilo nei commenti 👇",
              "Salvalo per la prossima visita 📌\nMandalo a chi sta cercando casa.",
              "#cercocasa #visitacasa #comprarecasa #affitto #consiglicasa"),
    "cost": ("Quale spesa ti ha sorpreso di più? Scrivilo nei commenti 👇",
             "Salvalo prima di firmare 📌\nMandalo a chi sta comprando casa.",
             "#comprarecasa #primacasa #mutuo #notaio #consiglicasa"),
}


def at(day, time):
    return f"2026-11-{day:02d}T{time}+01:00"


def caption(body, cat, is_chat):
    question, save, tags = FILM[cat]
    return f"{body}\n\nProva Nesso: link in bio.\n\n{QUESTION_CHAT if is_chat else question}\n{save}\n\n{tags}"


def chat(day, time, slug, hook_clip, who, role, color, hook, thread, headline, sub, phone, body, cat="visit", size=None):
    """hook: the first message, floating over real footage. thread: (from, text, typing)."""
    msgs, t = [{"at": 0.0, "from": "them", "text": hook}], 0.9
    for frm, text, typing in thread:
        t += typing
        msgs.append({"at": round(t, 2), "from": frm, "typing": typing, "text": text})
        t += 1.15 if frm == "them" else 1.0
    head = {"kind": "headline", "secs": 2.6, "text": headline, "sub": sub, "phone": M + phone,
            "phone_height": 1300, "text_y": 230}
    if size:
        head["size"] = size
    return {"id": f"r-{slug}", "type": "reel", "channel": "ig-it", "at": at(day, time), "slug": f"reel-{slug}",
            "scenes": [
                {"kind": "photo", "secs": 2.1, "clip": {"file": P + hook_clip[0] + ".mp4", "start": hook_clip[1]},
                 "who": who, "color": color, "bubble": hook},
                {"kind": "chat", "secs": round(t + 0.6, 2), "who": who, "role": role, "color": color, "messages": msgs},
                head,
                {"kind": "end", "secs": 2.0, "line": "Prima di firmare.", "cta": LINK},
            ], "caption": caption(body, cat, True)}


def film(day, slug, shots, body, end, cat="visit"):
    """shots: (clip id, start, secs, words, phone or None). *word* is italic. end: the clip under the logo."""
    clips, cards = [], []
    for clip, start, secs, words, phone in shots:
        clips.append({"file": f"{P}{clip}.mp4", "start": start, "secs": secs})
        card = {"kind": "serif", "text": words, "secs": secs}
        if "\n" in words or len(words) > 12:
            card["size"] = 124
        if phone:
            card.update({"phone": M + phone, "phone_top": 400, "phone_height": 1480, "phone_tilt": -3, "phone_dx": 0,
                         "size": 96, "text_top": True, "text_y": 0, "text": words.replace("\n", " ")})
        cards.append(card)
    clips.append({"file": P + end + ".mp4", "start": 0.5, "secs": 2.3})
    cards.append({"kind": "brand", "sub": LINK, "secs": 2.3})
    music = "music-beautiful-dream" if day % 2 == 0 else "music-classical-vibes"
    return {"id": f"r-{slug}", "type": "reel", "channel": "ig-it", "at": at(day, "13:00"), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": clips, "cards": cards, "caption": caption(body, cat, False),
            "music": music, "music_gain": 0.6, "music_start": 3.0}


def screen(day, slug, mock):
    return {"id": f"s-screen-{slug}", "type": "story", "channel": "ig-it", "at": at(day, "09:30"),
            "slug": f"storia-schermo-{slug}", "screen": M + mock}


def card(day, time, slug, theme, label, text, sub):
    return {"id": f"s-{slug}", "type": "story", "channel": "ig-it", "at": at(day, time), "slug": f"storia-{slug}",
            "theme": theme, "series": None, "card": {"kind": "fact", "label": label, "text": text, "sub": sub}}


def tomorrow(day, slug, text):
    return card(day, "21:30", f"domani-{slug}", "violet", "DOMANI ALLE 8", text, "Prima di firmare, un controllo al giorno.")


PERCHE = runpy.run_path(str(Path(__file__).parent / "next-perche-nesso-carousel.py"))["SPEC"]

ITEMS = [
    # ---------------------------------------------------------------- Monday 9
    chat(9, "08:00", "dipende", ("6808082", 0.5), "Sara", "Amica", ORANGE_AV, "Chiedilo all'AI se la casa è rumorosa 🤖",
         [("me", "L'ho chiesto 🙃", 0.0), ("them", "E?", 0.5), ("me", "Ha detto «dipende» 😅", 0.0)],
         "L'AI non è nella stanza.\nIl tuo telefono sì.", "Nesso misura rumore, pavimento e sole, in visita.",
         "07-misura-rumore-finestra.png",
         "«Dipende.» È quello che risponde chi non ha visto la casa.\n\nQuanto rumore entra, quanto pende il pavimento, quando arriva il sole: si misura lì, in visita, col telefono. Nesso ti guida e ti dice anche cosa quella misura non può stabilire.",
         size=104),
    screen(9, "costi", "04-costi.png"),
    card(9, "12:30", "consiglio-torcia", "violet", "IN VISITA", "Fai scorrere la *torcia* sul muro.",
         "Telefono piatto sulla parete: dove è stata rifatta, l'ombra si vede."),
    film(9, "di-sera", [
        ("34626564", 0.5, 1.2, "Torna", None), ("34626564", 1.8, 1.2, "*di sera.*", None),
        ("37557759", 0.5, 1.5, "La stessa strada,", None), ("34626564", 6.0, 1.5, "un'altra *luce.*", None),
        ("7578792", 0.5, 1.2, "Le persone.", None), ("37557759", 4.0, 1.2, "I *parcheggi.*", None),
        ("37557759", 8.0, 2.6, "Fai il giro\n*dell'isolato.*", "02-vivi-mappa.png"),
    ], "Di giorno, con chi ti mostra la casa, ogni strada sembra la stessa.\n\nTorna dopo il buio e fai il giro dell'isolato: segna luce, persone, parcheggi. Nesso lo tiene nel tuo registro come una tua osservazione. Vale una sera sola, e non è un giudizio sulla zona o su chi ci vive.",
       end="30939183"),
    card(9, "15:30", "fatto-detrazione", "orange", "LO SAPEVI?", "Sulla casa dove vai a vivere puoi detrarre il *19%* della provvigione.",
         "Dall'IRPEF, su massimo €1.000 di provvigione, nell'anno in cui la paghi."),
    {"id": "k-perche", "type": "carousel", "channel": "ig-it", "at": at(9, "18:00"), "slug": "carosello-perche-nesso",
     "panorama": PERCHE,
     "caption": "Un chatbot ti dice «dipende». In quella casa non è mai entrato. Scorri.\n\n"
                "Il rumore si misura nella stanza, con la finestra aperta e poi chiusa. Le spese si contano sul prezzo: €250.000 da un privato, prima casa, agenzia al 3%, mutuo di €175.000. "
                "Sono €14.687,50 in più del prezzo, prima di notaio e banca. È un calcolo sulle regole nazionali, non una consulenza.\n\n"
                "Prova Nesso: link in bio.\n\n"
                "Hai mai chiesto a un chatbot un consiglio sulla casa? Scrivilo nei commenti 👇\n"
                "Salvalo prima di firmare 📌\nMandalo a chi sta cercando casa.\n\n"
                "#comprarecasa #cercocasa #visitacasa #primacasa #consiglicasa"},
    chat(9, "20:00", "foglio", ("7646370", 0.5), "Marco", "Agenzia", VIOLET_AV, "Infissi nuovi, isolano benissimo ✨",
         [("me", "Posso fare la prova del foglio?", 0.0), ("them", "Del… foglio? 😅", 0.9)],
         "Un foglio di carta.\nUn minuto.", "Dove scivola via, l'anta non preme.", "06-dentro-property-check.png",
         "Infissi nuovi, dicono. Provali.\n\nChiudi un foglio di carta nella finestra e tiralo fuori: sopra, sotto, ai due lati. Dove scivola via facilmente, l'anta non preme. Il limite: è un confronto fra quattro punti, fatto a mano, e non dice niente sul vetro.\n\nÈ uno degli 82 controlli di Nesso per la visita."),
    tomorrow(9, "crepa", "Una crepa si fotografa con una *moneta.*"),

    # ---------------------------------------------------------------- Tuesday 10
    chat(10, "08:00", "crepa", ("7817149", 0.5), "Proprietario", "Annuncio", INK_AV, "È solo un po' di assestamento 🙂",
         [("me", "Posso fotografarla con una moneta?", 0.0), ("them", "Con una moneta? 😅", 0.8), ("me", "Così vedo quanto è larga.", 0.0)],
         "Fotografala\ncon una moneta.", "Se conta o no, lo dice un tecnico.", "06-dentro-property-check.png",
         "«È solo assestamento.» Può darsi. Fotografala lo stesso.\n\nDi fronte, con una moneta o una tessera nella foto, e segna dove inizia e dove finisce. Nesso tiene la foto accanto alla tua nota. Se una crepa conti o no è una domanda per chi può vedere l'edificio."),
    screen(10, "home", "01-home.png"),
    card(10, "12:30", "consiglio-interruttori", "orange", "IN VISITA", "Premi *ogni* interruttore.",
         "Segna quelli che non fanno niente."),
    film(10, "bollette", [
        ("7597965", 0.5, 1.3, "A gennaio", None), ("7646371", 0.5, 1.0, "*quanto*", None),
        ("4554455", 0.5, 1.3, "la paghi?", None), ("7646403", 0.5, 1.2, "Chiedi", None),
        ("31679132", 0.5, 1.2, "12 mesi", None), ("4569531", 0.5, 1.4, "di *bollette.*", None),
        ("7647439", 0.5, 2.6, "E il rendiconto\n*condominiale.*", "06-dentro-property-check.png"),
    ], "Una casa vista a novembre non dice quanto costa scaldarla a gennaio.\n\nIn visita chiedi dodici mesi di bollette e il rendiconto condominiale. Sono dodici mesi di qualcun altro, col suo termostato e le sue abitudini: i tuoi saranno diversi, ma la cifra di gennaio dice com'è fatto l'edificio.",
       end="7817154", cat="cost"),
    card(10, "15:30", "fatto-superficie", "violet", "LO SAPEVI?", "La *superficie commerciale* comprende anche i muri.",
         "E i balconi e la cantina. Chiedi quale cifra è stata usata."),
    chat(10, "20:00", "campo", ("5697829", 0.5), "Chiara", "Collega", VIOLET_AV, "Smart working dalla camera? 💻",
         [("me", "Spero ci sia campo 🤞", 0.0), ("them", "Non l'hai provato in visita?", 0.8), ("me", "…no 😬", 0.0)],
         "Prova il campo.\nStanza per stanza.", "Mettiti dove lavoreresti e misura.", "06-dentro-property-check.png",
         "La domanda che fa per prima chi lavora dalla camera in fondo. Nessun annuncio risponde.\n\nIn visita mettiti dove lavoreresti, misura, spostati in un secondo punto e misura di nuovo. Il limite: è quello che il tuo telefono ha raggiunto quel pomeriggio. Un altro operatore può comportarsi in modo diverso.", size=116),
    tomorrow(10, "caldaia", "Quanti anni ha la *caldaia*? Chiedi il libretto."),
]

# The carousel goes out once its photos are ones @nesso_italia has not shown (founder, 8 November).
ITEMS = [item for item in ITEMS if item["id"] != "k-perche"]
