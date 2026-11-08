"""@nesso_global, Monday 9 and Tuesday 10 November: weeks/2026-11-09.py translated one to one, on the
same footage, music and times. The audience is English speakers moving to or buying in Italy, so the
Italian facts and € figures stay as they are and an Italian term is explained the first time.

Every step and limit is the app's own text, nesso.fit/it/checklist-visita-casa, read on 8 November.
App screens: nesso_mobile docs/marketing/mockups-en. Footage: Pexels License. Music: Mixkit.
"""

P = "~/Documents/GitHub/nesso-assets/pexels/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-en/"
LINK = "Try Nesso · link in bio"
ORANGE_AV, VIOLET_AV, INK_AV = (249, 115, 22), (90, 62, 192), (52, 33, 111)

QUESTION_CHAT = "Has this happened to you? Tell us in the comments 👇"
FILM = {
    "visit": ("What do you look at first in a home? Tell us in the comments 👇",
              "Save this for your next viewing 📌\nSend it to someone who's flat-hunting.",
              "#movingtoitaly #househunting #livinginitaly #expatsinitaly #italianrealestate"),
    "cost": ("Which cost surprised you most? Tell us in the comments 👇",
             "Save this before you sign 📌\nSend it to someone who's buying a home.",
             "#italianproperty #italianrealestate #movingtoitaly #expatsinitaly #househunting"),
}


def at(day, time):
    return f"2026-11-{day:02d}T{time}+01:00"


def caption(body, cat, is_chat):
    question, save, tags = FILM[cat]
    return f"{body}\n\nTry Nesso: link in bio.\n\n{QUESTION_CHAT if is_chat else question}\n{save}\n\n{tags}"


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
    return {"id": f"en-r-{slug}", "type": "reel", "channel": "ig-en", "at": at(day, time), "slug": f"reel-{slug}",
            "scenes": [
                {"kind": "photo", "secs": 2.1, "clip": {"file": P + hook_clip[0] + ".mp4", "start": hook_clip[1]},
                 "who": who, "color": color, "bubble": hook},
                {"kind": "chat", "secs": round(t + 0.6, 2), "who": who, "role": role, "color": color, "messages": msgs},
                head,
                {"kind": "end", "secs": 2.0, "line": "Before you sign.", "cta": LINK},
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
    return {"id": f"en-r-{slug}", "type": "reel", "channel": "ig-en", "at": at(day, "13:00"), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": clips, "cards": cards, "caption": caption(body, cat, False),
            "music": music, "music_gain": 0.6, "music_start": 3.0}


def screen(day, slug, mock):
    return {"id": f"en-s-screen-{slug}", "type": "story", "channel": "ig-en", "at": at(day, "09:30"),
            "slug": f"story-screen-{slug}", "screen": M + mock}


def card(day, time, slug, theme, label, text, sub):
    return {"id": f"en-s-{slug}", "type": "story", "channel": "ig-en", "at": at(day, time), "slug": f"story-{slug}",
            "theme": theme, "series": None, "card": {"kind": "fact", "label": label, "text": text, "sub": sub}}


def tomorrow(day, slug, text):
    return card(day, "21:30", f"tomorrow-{slug}", "violet", "TOMORROW AT 8", text, "Before you sign, one check a day.")


ITEMS = [
    # ---------------------------------------------------------------- Monday 9
    chat(9, "08:00", "it-depends", ("6808082", 0.5), "Sara", "Friend", ORANGE_AV, "Ask AI if the flat is noisy 🤖",
         [("me", "I did 🙃", 0.0), ("them", "And?", 0.5), ("me", "It said \"it depends\" 😅", 0.0)],
         "AI isn't in the room.\nYour phone is.", "Nesso measures noise, floors and sun at the viewing.",
         "07-misura-rumore-finestra.png",
         "\"It depends.\" That's the answer you get from anything that hasn't seen the flat.\n\nHow much noise comes in, how far the floor slopes, when the sun arrives: you measure those in the room, at the viewing, with your phone. Nesso guides you and also tells you what each measurement can't establish.",
         size=104),
    screen(9, "costs", "04-costi.png"),
    card(9, "12:30", "tip-torch", "violet", "AT THE VIEWING", "Run a *torch* along the wall.",
         "Phone flat against the wall: where it's been patched, the shadow shows."),
    film(9, "after-dark", [
        ("34626564", 0.5, 1.2, "Go back", None), ("34626564", 1.8, 1.2, "*after dark.*", None),
        ("37557759", 0.5, 1.5, "The same street,", None), ("34626564", 6.0, 1.5, "a different *light.*", None),
        ("7578792", 0.5, 1.2, "The people.", None), ("37557759", 4.0, 1.2, "The *parking.*", None),
        ("37557759", 8.0, 2.6, "Walk\n*the block.*", "02-vivi-mappa.png"),
    ], "By day, with someone showing you round, every street looks the same.\n\nGo back after dark and walk the block: note the light, the people, the parking. Nesso keeps it in your record as your own observation. It's one evening, and it isn't a judgement on the area or on the people who live there.",
       end="30939183"),
    card(9, "15:30", "fact-deduction", "orange", "DID YOU KNOW?", "On the home you'll live in, you can deduct *19%* of the agent's fee.",
         "From IRPEF (Italian income tax), on at most €1,000 of fee, in the year you pay it."),
    chat(9, "20:00", "paper", ("7646370", 0.5), "Marco", "Agency", VIOLET_AV, "New windows, great insulation ✨",
         [("me", "Can I do the paper test?", 0.0), ("them", "The… paper? 😅", 0.9)],
         "One sheet of paper.\nOne minute.", "Where it slides out, the frame isn't pressing.", "06-dentro-property-check.png",
         "New windows, they say. Test them.\n\nShut a sheet of paper in the window and pull it out: top, bottom and both sides. Where it slides out easily, the frame isn't pressing. The limit: it's a comparison of four points, done by hand, and it says nothing about the glass.\n\nIt's one of Nesso's 82 viewing checks."),
    tomorrow(9, "crack", "Photograph a crack with a *coin.*"),

    # ---------------------------------------------------------------- Tuesday 10
    chat(10, "08:00", "crack", ("7817149", 0.5), "Owner", "Listing", INK_AV, "It's just a bit of settling 🙂",
         [("me", "Can I photograph it with a coin?", 0.0), ("them", "With a coin? 😅", 0.8), ("me", "So I can see how wide it is.", 0.0)],
         "Photograph it\nwith a coin.", "Whether it matters is for a technician.", "06-dentro-property-check.png",
         "\"It's just settling.\" Maybe. Photograph it anyway.\n\nHead-on, with a coin or a card in the shot, and mark where it starts and ends. Nesso keeps the photo next to your note. Whether a crack matters is a question for someone who can see the building."),
    screen(10, "home", "01-home.png"),
    card(10, "12:30", "tip-switches", "orange", "AT THE VIEWING", "Press *every* switch.",
         "Note the ones that do nothing."),
    film(10, "bills", [
        ("7597965", 0.5, 1.3, "In January", None), ("7646371", 0.5, 1.0, "*what*", None),
        ("4554455", 0.5, 1.3, "will you pay?", None), ("7646403", 0.5, 1.2, "Ask for", None),
        ("31679132", 0.5, 1.2, "12 months", None), ("4569531", 0.5, 1.4, "of *bills.*", None),
        ("7647439", 0.5, 2.6, "And the building's\n*accounts.*", "06-dentro-property-check.png"),
    ], "A flat seen in November doesn't tell you what it costs to heat in January.\n\nAt the viewing, ask for twelve months of bills and the building's accounts (the rendiconto condominiale). They're twelve months of someone else's, with their thermostat and their habits. Yours will be different, but the January figure tells you how the building is made.",
       end="7817154", cat="cost"),
    card(10, "15:30", "fact-surface", "violet", "DID YOU KNOW?", "The *commercial surface* (superficie commerciale) includes the walls.",
         "And the balconies and the cellar. Ask which figure was used."),
    chat(10, "20:00", "signal", ("5697829", 0.5), "Chiara", "Colleague", VIOLET_AV, "Working from the bedroom? 💻",
         [("me", "Hope there's signal 🤞", 0.0), ("them", "You didn't try it at the viewing?", 0.8), ("me", "…no 😬", 0.0)],
         "Test the signal.\nRoom by room.", "Stand where you'd work and measure.", "06-dentro-property-check.png",
         "The first thing anyone asks if they'll work from the back bedroom. No listing answers it.\n\nAt the viewing, stand where you'd work, measure, move to a second spot and measure again. The limit: it's what your phone reached that afternoon. Another network can behave differently.", size=116),
    tomorrow(10, "boiler", "How old is the *boiler*? Ask for the logbook."),
]
