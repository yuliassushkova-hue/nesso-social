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
