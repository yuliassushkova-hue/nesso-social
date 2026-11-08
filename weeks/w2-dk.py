"""@nesso_danmark, Tuesday 10 November: weeks/2026-11-09.py translated, on the same footage, music and
times. Monday 9 is already queued from the first Danish week.

Every step and limit is the app's own Danish text, nesso.fit/da/tjekliste-fremvisning, read on
8 November. App screens: nesso_mobile docs/marketing/mockups-da. Footage: Pexels License. Music: Mixkit.

Replaced, because the Italian fact is Italian or the Danish checklist has no such check:
- 15:30 "superficie commerciale" (an Italian listing convention) -> the ventilation test.
- 21:30 teaser "caldaia" (no boiler check in the Danish list) -> when the windows were changed.
"""

P = "~/Documents/GitHub/nesso-assets/pexels/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-da/"
LINK = "Prøv Nesso · link i bio"
TAGS = "#boligjagt #fremvisning #førstebolig #lejebolig #boligkøb"
VIOLET_AV, INK_AV = (90, 62, 192), (52, 33, 111)
QUESTION_CHAT = "Er det sket for dig? Fortæl det i kommentarerne 👇"
QUESTION_FILM = "Hvad ser du først på i en bolig? Fortæl det i kommentarerne 👇"
SAVE = "Gem den til næste fremvisning 📌\nSend den til en, der leder efter bolig."


def at(day, time):
    return f"2026-11-{day:02d}T{time}+01:00"


def caption(body, is_chat):
    return f"{body}\n\nPrøv Nesso: link i bio.\n\n{QUESTION_CHAT if is_chat else QUESTION_FILM}\n{SAVE}\n\n{TAGS}"


def chat(day, time, slug, hook_clip, who, role, color, hook, thread, headline, sub, phone, body, size=None):
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
    return {"id": f"dk-r-{slug}", "type": "reel", "channel": "ig-dk", "at": at(day, time), "slug": f"reel-{slug}",
            "scenes": [
                {"kind": "photo", "secs": 2.1, "clip": {"file": P + hook_clip[0] + ".mp4", "start": hook_clip[1]},
                 "who": who, "color": color, "bubble": hook},
                {"kind": "chat", "secs": round(t + 0.6, 2), "who": who, "role": role, "color": color, "messages": msgs},
                head,
                {"kind": "end", "secs": 2.0, "line": "Før du skriver under.", "cta": LINK},
            ], "caption": caption(body, True)}


def film(day, slug, shots, body, end):
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
    return {"id": f"dk-r-{slug}", "type": "reel", "channel": "ig-dk", "at": at(day, "13:00"), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": clips, "cards": cards, "caption": caption(body, False),
            "music": "music-beautiful-dream", "music_gain": 0.6, "music_start": 3.0}


def card(day, time, slug, theme, label, text, sub):
    return {"id": f"dk-s-{slug}", "type": "story", "channel": "ig-dk", "at": at(day, time), "slug": f"historie-{slug}",
            "theme": theme, "series": None, "card": {"kind": "fact", "label": label, "text": text, "sub": sub}}


ITEMS = [
    chat(10, "08:00", "revne", ("7817149", 0.5), "Ejer", "Annonce", INK_AV, "Det er bare lidt sætning 🙂",
         [("me", "Må jeg tage et billede med en mønt?", 0.0), ("them", "Med en mønt? 😅", 0.8), ("me", "Så kan jeg se, hvor bred den er.", 0.0)],
         "Tag billedet\nmed en mønt.", "Om den betyder noget, må en fagmand se på.", "06-indenfor-property-check.png",
         "»Det er bare sætning.« Måske. Tag et billede alligevel.\n\nForfra, med en mønt eller et kort ved siden af, og markér, hvor den begynder og ender. Nesso lægger billedet ved siden af din egen notits. Om en revne betyder noget, er et spørgsmål til en, der kan se bygningen."),
    {"id": "dk-s-screen-hjem", "type": "story", "channel": "ig-dk", "at": at(10, "09:30"),
     "slug": "historie-skaerm-hjem", "screen": M + "01-hjem.png"},
    card(10, "12:30", "raad-kontakter", "orange", "VED FREMVISNINGEN", "Tryk på *hver* kontakt.",
         "Notér dem, der ikke gør noget."),
    film(10, "regninger", [
        ("7597965", 0.5, 1.3, "I januar", None), ("7646371", 0.5, 1.0, "*hvad*", None),
        ("4554455", 0.5, 1.3, "koster den?", None), ("7646403", 0.5, 1.2, "Bed om", None),
        ("31679132", 0.5, 1.2, "12 måneders", None), ("4569531", 0.5, 1.4, "*regninger.*", None),
        ("7647439", 0.5, 2.6, "Og bygningens\n*fællesudgifter.*", "06-indenfor-property-check.png"),
    ], "En bolig set i november fortæller ikke, hvad den koster at varme op i januar.\n\nBed ved fremvisningen om tolv måneders energiregninger og bygningens opgørelse over fællesudgifter. Det er en andens tolv måneder, med deres termostat og deres vaner. Dine bliver anderledes, men januartallet fortæller stadig, hvordan bygningen er.",
       end="7817154"),
    card(10, "15:30", "raad-ventilation", "violet", "VED FREMVISNINGEN", "Hold silkepapir mod *ventilationsristen.*",
         "Det viser, om luften bevæger sig lige nu. Ikke hvor meget."),
    chat(10, "20:00", "daekning", ("5697829", 0.5), "Sofie", "Kollega", VIOLET_AV, "Hjemmearbejde fra soveværelset? 💻",
         [("me", "Håber der er dækning 🤞", 0.0), ("them", "Prøvede du det ikke til fremvisningen?", 0.8), ("me", "…nej 😬", 0.0)],
         "Test dækningen.\nRum for rum.", "Stil dig, hvor du ville arbejde, og mål.", "06-indenfor-property-check.png",
         "Det første, man spørger om, når man skal arbejde fra det bagerste værelse. Ingen annonce svarer på det.\n\nVed fremvisningen: stil dig, hvor du ville arbejde, mål, flyt dig et andet sted hen og mål igen. Det er det, din telefon nåede den eftermiddag. En anden udbyder kan være helt anderledes i samme rum.", size=116),
    card(10, "21:30", "imorgen-vinduer", "violet", "I MORGEN KL. 8", "Hvornår blev *vinduerne* skiftet? Spørg efter fakturaen.",
         "Før du skriver under, ét tjek om dagen."),
]
