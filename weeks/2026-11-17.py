"""@nesso_italia, Tuesday 17 to Sunday 22 November 2026.

Wednesday to Friday are the 26 posts Meta blocked on 12–15 November, moved five days on (PR #21).
This file fills the slots left: Tuesday morning, Saturday and Sunday.

New this week (founder, 16 November): Reels must not look alike, every Reel has its own music, and the
music is Meta Sound Collection's "Reels Sound" pick, sorted by popularity (cleared for Meta apps only, so
the YouTube copies need other music). One Reel a day carries a voice-over the founder recorded in
ElevenLabs; its captions follow the voice (tools/voice_timing.py).

Every step and limit is the app's own text from nesso.fit/it/checklist-visita-casa, read on 16 November.
Footage: Pexels License. Music: Meta Sound Collection. Voices: ElevenLabs, the founder's account.
"""
import json
import runpy
from pathlib import Path

HERE = Path(__file__).parent
BASE = runpy.run_path(str(HERE / "2026-11-09.py"))
chat, card, tomorrow, at, caption = BASE["chat"], BASE["card"], BASE["tomorrow"], BASE["at"], BASE["caption"]
ORANGE_AV, VIOLET_AV, INK_AV = BASE["ORANGE_AV"], BASE["VIOLET_AV"], BASE["INK_AV"]
P = "~/Documents/GitHub/nesso-assets/pexels/"
VOICE = Path("~/Documents/GitHub/nesso-assets/voice").expanduser()
LINK = "Prova Nesso · link in bio"


def ask(day, slug, theme, text, sub):
    return card(day, "09:30", f"domanda-{slug}", theme, "CHIEDI IN VISITA", text, sub)


def tune(item, music, gain=0.22, start=0.0):
    """Each Reel its own track."""
    item.update({"music": music, "music_gain": gain, "music_start": start})
    return item


def voiced(day, time, slug, voice, clips, end, music, body, cat="visit", style="white", y=1180):
    """A voice-over Reel: footage, one caption per spoken sentence, timed to the recording.
    clips: one (clip id, start) per sentence of voice/<voice>.json. end: (clip id, start) under the logo."""
    timing = json.loads((VOICE / f"{voice}.json").read_text(encoding="utf-8"))
    lead = 0.4
    lines = timing["lines"]
    assert len(clips) == len(lines), (slug, len(clips), len(lines))
    cards, shots = [], []
    for i, ((a, b, words), (clip, start)) in enumerate(zip(lines, clips)):
        secs = round((b - a) + (lead if i == 0 else 0) + (0.6 if i == len(lines) - 1 else 0), 2)
        shots.append({"file": f"{P}{clip}.mp4", "start": start, "secs": secs})
        cards.append({"kind": "caption", "secs": secs, "y": y, "align": "center",
                      "blocks": [{"text": words, "size": 70, "style": style}]})
    shots.append({"file": f"{P}{end[0]}.mp4", "start": end[1], "secs": 2.4})
    cards.append({"kind": "brand", "sub": LINK, "secs": 2.4})
    return {"id": f"r-{slug}", "type": "reel", "channel": "ig-it", "at": at(day, time), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": shots, "cards": cards, "caption": caption(body, cat, False),
            "voice": voice, "voice_at": lead, "music": music, "music_gain": 0.12}


ITEMS = [
    # ---------------------------------------------------------------- Tuesday 17
    tune(chat(17, "08:00", "segnale", ("6391723", 0.5), "Giulia", "Agenzia", VIOLET_AV, "Fibra ovunque, prende benissimo 📶",
              [("me", "Anche in camera, in fondo?", 0.0), ("them", "Ovunque, giuro 🙂", 0.8), ("me", "Faccio una prova col telefono.", 0.0)],
              "Lavori dalla camera?\nProva lì.", "Stanza per stanza, col tuo telefono.", "06-dentro-property-check.png",
              "«Prende ovunque.» Se lavorerai dalla camera in fondo, è lì che conta.\n\nMettiti dove lavoreresti e misura. Poi spostati in un secondo punto e misura di nuovo. Il limite: è quello che il tuo telefono ha preso quel pomeriggio, sulla sua rete. Un altro operatore può comportarsi in modo del tutto diverso nella stessa stanza."),
         "wishlist-calling"),
    ask(17, "bollette", "orange", "Mi mostri *12 mesi* di bollette?", "E il rendiconto condominiale. Gennaio dice com'è fatto l'edificio."),
    card(17, "12:30", "consiglio-tacche", "violet", "IN VISITA", "Entra in ogni stanza. *Guarda le tacche.*",
         "Prima la camera, poi il bagno."),
    voiced(17, "13:00", "un-minuto", "it-1",
           [("6639956", 0.5), ("4153809", 1.0), ("8862328", 0.5), ("7034335", 0.5), ("10308537", 0.5), ("7198960", 0.5), ("13554476", 0.5)],
           ("6639956", 6.0), "romantic",
           "Prima di dire sì a una casa, prenditi un minuto. A metà stanza, finestre chiuse, in silenzio.\n\nIl limite: un minuto di un pomeriggio non racconta la notte. Però è il controllo che costa meno di tutta la visita, e puoi rifarlo quante volte vuoi."),
]

S = "~/Documents/GitHub/nesso-assets/stills/"
ORANGE = (249, 115, 22)
SAVE = "Salvalo per la prossima visita 📌\nMandalo a chi sta cercando casa."


def words(day, time, slug, shots, end, music, body, cat="visit"):
    """A Reel of footage and captions without a voice: shots are (clip, start, secs, [(text, style, size)])."""
    clips, cards = [], []
    for clip, start, secs, blocks in shots:
        clips.append({"file": f"{P}{clip}.mp4", "start": start, "secs": secs})
        cards.append({"kind": "caption", "secs": secs, "y": 640, "align": "center",
                      "blocks": [{"text": t, "style": s, "size": z} for t, s, z in blocks]})
    clips.append({"file": f"{P}{end[0]}.mp4", "start": end[1], "secs": 2.4})
    cards.append({"kind": "brand", "sub": LINK, "secs": 2.4})
    return {"id": f"r-{slug}", "type": "reel", "channel": "ig-it", "at": at(day, time), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": clips, "cards": cards, "caption": caption(body, cat, False),
            "music": music, "music_gain": 0.5}


def serie(day, time, slug, spec, body):
    return {"id": f"k-{slug}", "type": "carousel", "channel": "ig-it", "at": at(day, time), "slug": f"carosello-{slug}",
            "review": spec, "caption": body}


FRIENDS = {"title": "La casa di Monica", "show": "Friends · Greenwich Village, New York",
           "cover": S + "friends-finale.jpg", "cover_credit": "Friends, NBC / Warner Bros.",
           "slides": [
               {"photo": S + "friends-living.jpg", "head": "COSA CI PIACE", "credit": "Friends, NBC / Warner Bros.",
                "lines": ["La cucina è aperta sul soggiorno: si cucina e si parla.", "Finestre grandi, tanta luce.", "Due camere: c'è posto per una coinquilina."]},
               {"photo": S + "friends-window.jpg", "head": "COSA CONTROLLEREMMO", "chip": ORANGE, "credit": "Friends, NBC / Warner Bros.",
                "lines": ["Chi c'è di fronte? Qui, il vicino nudo.", "Tu vedi lui. E lui vede te.", "In visita affacciati da ogni finestra: in alto, in basso, di fronte."]},
               {"photo": S + "friends-balcony.jpg", "head": "IL TRUCCO DELL'AFFITTO", "credit": "Friends, NBC / Warner Bros.",
                "lines": ["Era la casa della nonna, con l'affitto bloccato.", "Monica la subaffittava senza dirlo a nessuno.", "Quando una casa costa troppo poco, chiedi perché."]},
           ],
           "ask": "E tu, ci vivresti?", "ask_sub": "Con il vicino di fronte, intendo."}

MONTALBANO = {"title": "La casa di Montalbano", "show": "Il commissario Montalbano · Punta Secca (RG)",
              "cover": S + "commons-punta-secca-e-casa-di-montalbano---panoramio.jpg", "cover_focus": 0.75,
              "cover_credit": "Foto: jean-michel gobet, CC BY-SA 3.0",
              "slides": [
                  {"photo": S + "commons-tramonto-sulla-spiaggia-di-punta-secca.jpg", "head": "COSA CI PIACE", "credit": "Foto: SaraaaCreaaa, CC0",
                   "lines": ["La terrazza sulla spiaggia.", "Il mare a dieci passi dalla porta.", "Il caffè davanti al tramonto."]},
                  {"photo": S + "commons-il-mare-di-montalbano---panoramio.jpg", "head": "COSA CONTROLLEREMMO", "chip": ORANGE, "credit": "Foto: giomodica, CC BY 3.0",
                   "lines": ["Sale e umidità: cammina lungo la base dei muri esterni.", "Cerca macchie, bolle o vernice che si stacca.", "Una macchia può essere vecchia e asciutta. Chiedi."]},
                  {"photo": S + "commons-la-spiaggia-del-commissario-di-notte.jpg", "head": "E D'ESTATE?", "credit": "Foto: Maocchio, CC BY-SA 4.0",
                   "lines": ["La spiaggia sotto casa è di tutti.", "Torna di sera, e in un altro giorno della settimana.", "Due visite sono due momenti. Meglio di uno."]},
              ],
              "ask": "Ci vivresti tutto l'anno?", "ask_sub": "Anche a gennaio, col vento."}

EMILY = {"title": "La casa di Emily", "show": "Emily in Paris · Place de l'Estrapade, Parigi",
         "cover": S + "commons-1-place-de-lestrapade.jpg", "cover_focus": 0.4, "cover_credit": "Foto: VVVCFFrance, CC BY-SA 4.0",
         "slides": [
             {"photo": S + "commons-place-de-lestrapade--paris-5e.jpg", "head": "COSA CI PIACE", "credit": "Foto: Celette, CC BY-SA 4.0",
              "lines": ["Una piazzetta con gli alberi sotto casa.", "Un ristorante proprio di fronte.", "Il Pantheon a due passi."]},
             {"photo": S + "commons-place-de-lestrapade-2.jpg", "head": "QUINTO PIANO? CONTA BENE", "chip": ORANGE, "credit": "Foto: LPLT, CC BY-SA 3.0",
              "lines": ["Emily conta i piani all'americana e finisce alla porta del vicino.", "A Parigi, come in Italia, il piano terra non si conta.", "In visita chiedi il piano e contalo da te."]},
             {"photo": S + "commons-1-place-de-lestrapade.jpg", "focus": 0.6, "head": "PRIMA DEL TRASLOCO", "credit": "Foto: VVVCFFrance, CC BY-SA 4.0",
              "lines": ["Scale strette? Misura le porte più strette.", "Il divano passa? Meglio saperlo prima di firmare."]},
         ],
         "ask": "Mansarda a Parigi o bilocale con ascensore?", "ask_sub": "Scegli nei commenti."}

FILM_TAGS = "#cercocasa #serietv #casedeifilm #visitacasa #consiglicasa"

ITEMS += [
    # ---------------------------------------------------------------- Saturday 21
    words(21, "08:00", "lo-sapevi-soffitto", [
        ("7216715", 0.5, 2.4, [("LO SAPEVI?", "orange", 64), ("Quanto deve essere alto un soffitto?", "white", 78)]),
        ("36933613", 0.5, 2.6, [("2,70 m", "violet", 150), ("in camera, soggiorno e cucina", "white", 62)]),
        ("4155077", 0.5, 2.4, [("2,40 m", "violet", 150), ("in bagno e nei corridoi", "white", 62)]),
        ("8232811", 0.5, 2.6, [("Camera singola: almeno 9 m²", "white", 70), ("Doppia: almeno 14 m²", "white", 70)]),
        ("39226628", 0.5, 2.4, [("Decreto ministeriale", "white", 58), ("5 luglio 1975", "orange", 74)]),
    ], ("40397796", 0.5), "sparks-fly",
        "Un soffitto di una camera, di un soggiorno o di una cucina deve essere alto almeno 2,70 m. Bagni e corridoi almeno 2,40 m. Una camera singola almeno 9 m², una doppia 14 m². Lo dice il decreto ministeriale del 5 luglio 1975.\n\nIn Nesso l'altezza del soffitto si misura con un metro o con la scansione. Il limite: è una stima. Se l'altezza decide se una stanza è abitabile, la cifra che conta è quella nei documenti edilizi."),
    ask(21, "perdita", "violet", "C'è mai stata *una perdita?*", "Se sì: quando, e dove."),
    card(21, "12:30", "consiglio-silicone", "orange", "IN VISITA", "Premi piano *negli angoli* della doccia.",
         "Segna crepe, nero o punti molli."),
    voiced(21, "13:00", "bagno-tre-punti", "it-5",
           [("40397795", 0.5), ("6694013", 0.5), ("4155072", 0.5), ("37296798", 0.5), ("6322926", 0.5), ("29532407", 0.5)],
           ("40397782", 0.5), "beautifully-stranded",
           "In bagno guarda tre punti: il soffitto, la parete della doccia, l'angolo sopra la porta. Cerca macchie, vernice che si stacca o una parete ridipinta da poco.\n\nIl limite: segni compatibili con l'umidità non sono un accertamento di umidità. Ti dicono dove fare domande.",
           style="violet"),
    card(21, "15:30", "fatto-soffitto", "violet", "LO SAPEVI?", "Un soffitto *ridipinto il mese scorso* dice poco.",
         "Uno asciutto in una settimana asciutta dice già meno di quanto sembri."),
    serie(21, "18:00", "casa-di-monica", FRIENDS,
          "La casa di Monica in Friends: cucina aperta, finestre grandi, due camere nel Greenwich Village. E un vicino di fronte che non tira mai le tende. Scorri.\n\n"
          "Era la casa della nonna, con l'affitto bloccato, e Monica la subaffittava senza dirlo. Quando un affitto è troppo basso, chiedi perché.\n\n"
          "Ci vivresti, con quel vicino? Scrivilo nei commenti 👇\n" + SAVE + "\n\nImmagini: Friends, NBC / Warner Bros.\n\n" + FILM_TAGS),
    words(21, "20:00", "vero-o-falso", [
        ("6204980", 0.5, 2.6, [("VERO O FALSO?", "orange", 64), ("La superficie commerciale comprende muri e balconi.", "white", 70)]),
        ("6204980", 3.5, 1.8, [("VERO", "violet", 140), ("Anche la cantina, in parte.", "white", 60)]),
        ("5867579", 0.5, 2.6, [("VERO O FALSO?", "orange", 64), ("Un telefono è un fonometro.", "white", 76)]),
        ("5867579", 3.5, 2.2, [("FALSO", "violet", 140), ("Confronta stanze misurate allo stesso modo.", "white", 60)]),
        ("40955484", 0.5, 2.6, [("VERO O FALSO?", "orange", 64), ("In camera il soffitto può essere alto 2,40 m.", "white", 70)]),
        ("40955484", 3.5, 2.0, [("FALSO", "violet", 140), ("Servono 2,70 m. 2,40 vale per bagni e corridoi.", "white", 58)]),
    ], ("8348130", 0.5), "we-have-a-winner",
        "Tre domande sulla casa. Quante ne hai indovinate?\n\nLa superficie commerciale comprende legittimamente muri, balconi e cantina. Un telefono non è un fonometro tarato: confronta stanze misurate allo stesso modo. E per una camera servono 2,70 m di altezza (DM 5 luglio 1975); 2,40 m valgono per bagni e corridoi."),
    card(21, "21:30", "domani-novita", "violet", "DOMANI ALLE 8", "Una cosa *nuova* in arrivo su Nesso.", "Riguarda i mobili."),

    # ---------------------------------------------------------------- Sunday 22
    voiced(22, "08:00", "prova-i-mobili", "it-3d",
           [("37674127", 0.5), ("36516353", 0.5), ("39122055", 0.5), ("12015692", 0.5)],
           ("6474186", 0.5), "treat-yourself",
           "Presto in Nesso: scansioni la stanza col telefono e provi i mobili prima di comprarli. Incolli il link di un divano e lo vedi nella tua stanza.\n\nArriva presto. Seguici per sapere quando.",
           style="orange"),
    ask(22, "seconda-visita", "orange", "Posso tornare *dopo le 20?*", "Oppure in un giorno feriale."),
    serie(22, "11:00", "casa-di-emily", EMILY,
          "La casa di Emily in Emily in Paris è un edificio vero, in Place de l'Estrapade. Piazzetta con gli alberi, ristorante di fronte. E un piano che si conta male. Scorri.\n\n"
          "Emily sale al «quinto» contando all'americana e bussa alla porta del vicino. A Parigi, come in Italia, il piano terra non si conta: in visita chiedi il piano e contalo da te.\n\n"
          "Mansarda a Parigi o bilocale con ascensore? Scrivilo nei commenti 👇\n" + SAVE +
          "\n\nFoto: VVVCFFrance, Celette (CC BY-SA 4.0), LPLT (CC BY-SA 3.0), Wikimedia Commons.\n\n" + FILM_TAGS),
    card(22, "12:30", "consiglio-angoli", "violet", "IN VISITA", "Dove cambia la pendenza, *leggi i quattro angoli.*",
         "Un quadrato di un metro, telefono sempre orientato allo stesso modo."),
    voiced(22, "13:00", "pavimento-in-piano", "it-6",
           [("40807351", 0.5), ("38413518", 3.0), ("7817161", 0.5), ("6474180", 3.0), ("36516351", 0.5), ("6353472", 0.5)],
           ("36044316", 0.5), "tinsel-and-memories",
           "Il pavimento è in piano? Posa il telefono a faccia in su, a metà stanza, e lascialo leggere. Poi giralo di mezzo giro e leggi di nuovo: così Nesso toglie l'errore del telefono stesso.\n\nIl limite: ti dice qualcosa di quel quadrato di pavimento. Le case vecchie sono raramente in piano, e una pendenza da sola non dimostra niente."),
    card(22, "15:30", "fatto-due-visite", "orange", "LO SAPEVI?", "Due visite sono *due momenti.*",
         "Non un andamento. Ma il doppio di quelle che fa quasi chiunque."),
    serie(22, "18:00", "casa-di-montalbano", MONTALBANO,
          "La casa di Montalbano esiste davvero: è a Punta Secca, sulla spiaggia, con la terrazza sul mare. Scorri.\n\n"
          "Cosa controlleremmo in visita: la base dei muri esterni, per macchie, bolle o vernice che si stacca. E una seconda visita in un altro momento, perché la spiaggia sotto casa d'estate è di tutti.\n\n"
          "Ci vivresti tutto l'anno? Scrivilo nei commenti 👇\n" + SAVE +
          "\n\nFoto: jean-michel gobet (CC BY-SA 3.0), giomodica (CC BY 3.0), Maocchio (CC BY-SA 4.0), SaraaaCreaaa (CC0), Wikimedia Commons.\n\n" + FILM_TAGS),
    chat(22, "20:00", "seconda-visita", ("6016323", 0.5), "Marco", "Agenzia", INK_AV, "Venite alle 11, è l'ora più bella ☀️",
         [("me", "E alle 21?", 0.0), ("them", "Alle 21? 😅", 0.8), ("me", "Voglio sentire la casa di sera.", 0.0)],
         "Le 11 sono belle.\nE le 21?", "Chiedi una seconda visita dopo le 20.", "06-dentro-property-check.png",
         "L'ora della visita la sceglie quasi sempre chi vende. Le 11 sono belle per tutti.\n\nChiedi una seconda visita dopo le 20, oppure in un giorno feriale. Il limite: due visite sono due momenti, non un andamento. Restano comunque il doppio di quelle che fa quasi chiunque."),
    {"id": "s-checklist-22", "type": "story", "channel": "ig-it", "at": at(22, "21:30"), "slug": "storia-82-controlli",
     "theme": "orange", "series": None,
     "card": {"kind": "cta", "text": "Questa settimana hai una visita? *82 controlli* in tasca.", "button": "Link in bio"}},
]
for item in ITEMS:
    if item["slug"] == "reel-seconda-visita":
        tune(item, "80s-synthwave")
