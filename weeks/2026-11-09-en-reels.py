"""The English account's 21 Reels, 9 to 15 November: the Italian week of 2 to 8 November
(weeks/2026-11-02-reels.py) translated one to one, same footage, music, times and structure.
08:00 and 20:00 a chat story, 13:00 a warm interior film with words one at a time in the serif.

The audience is English speakers moving to or buying in Italy, so the Italian facts and € figures
stay as they are; an Italian term is explained the first time a post uses it. Footage: Pexels
License, ids are https://www.pexels.com/video/<id>/. Facts: costs from nesso.fit/it/costi-acquisto-casa
(the €300,000 example: €13,528 before notary, bank and insurance; registration tax €1,848 on a
rendita of €800; agency €9,000 + €1,980 VAT), viewing checks from nesso.fit/it/checklist-visita-casa,
the mortgage rights from Banca d'Italia's guide. App screens: nesso_mobile docs/marketing/mockups-en.
"""

P = "~/Documents/GitHub/nesso-assets/pexels/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-en/"
LINK = "Try Nesso · link in bio"
TAG_VISIT = "#movingtoitaly #househunting #livinginitaly #expatsinitaly #italianrealestate"
TAG_COST = "#italianproperty #italianrealestate #movingtoitaly #expatsinitaly #househunting"
TAG_SELL = "#homestaging #italianrealestate #italianproperty #livinginitaly #movingtoitaly"
TAG_LIVE = "#movingtoitaly #expatsinitaly #livinginitaly #expatlife #lifeinitaly"
ORANGE_AV, VIOLET_AV, INK_AV = (249, 115, 22), (90, 62, 192), (52, 33, 111)


def at(day, time):
    return f"2026-11-{day - 7:02d}T{time}+01:00"  # moved to 2-8 Nov (founder, 2026-11-02)


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
    return {"id": f"en-r-{slug}", "type": "reel", "channel": "ig-en", "at": at(day, time), "slug": f"reel-{slug}",
            "scenes": [
                {"kind": "photo", "secs": 2.1, "clip": {"file": P + hook_clip[0] + ".mp4", "start": hook_clip[1]},
                 "who": who, "color": color, "bubble": hook},
                {"kind": "chat", "secs": chat_secs, "who": who, "role": role, "color": color, "messages": msgs},
                {"kind": "headline", "secs": 2.6, "text": headline, "sub": sub, "phone": M + phone},
                {"kind": "end", "secs": 2.0, "line": "Before you sign.", "cta": LINK},
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
    cards.append({"kind": "brand", "sub": "Before you sign · link in bio", "secs": 2.3})
    # the same music day by day as the Italian week (2 Nov = 9 Nov, and so on)
    music = "music-beautiful-dream" if (day - 7) % 2 == 0 else "music-classical-vibes"
    return {"id": f"en-r-{slug}", "type": "reel", "channel": "ig-en", "at": at(day, "13:00"), "slug": f"reel-{slug}",
            "theme": "violet", "progress": False, "clips": clips, "cards": cards, "caption": caption,
            "music": music, "music_gain": 0.6, "music_start": 3.0}


def frame(clip, start=1.0):
    return {"file": P + clip + ".mp4", "start": start}


ITEMS = [
    # ---------------------------------------------------------------- Monday 9
    chat(9, "08:00", "light", ("5853208", 0.5), "Marco", "Agent", VIOLET_AV, "The flat is so bright ☀️",
         [("them", frame("30744460"), 0.0), ("them", "Sun all day long ☀️", 0.6),
          ("me", "At the back of the room too?", 0.0), ("them", "Well… almost 😅", 0.9)],
         "Trust him.\nBut measure.", "The light at the back of the room, at the viewing.", "06-dentro-property-check.png",
         "\"So bright.\" Every flat is, next to the window.\n\nAt the viewing, switch the lights off and look at the back wall: that's where you'll read and work. Nesso's checklist shows you how, and what that check can't tell you.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    film(9, "look-properly", [
        ("6798992", 0.3, 1.0, "Before", None), ("6798992", 1.3, 1.1, "you *sign,*", None),
        ("29513615", 0.5, 1.4, "look", None), ("40134358", 0.5, 1.6, "*properly.*", None),
        ("36300251", 0.5, 1.2, "The light.", None), ("31960017", 0.5, 1.2, "The quiet.", None),
        ("6323324", 0.5, 1.2, "The corners.", None),
        ("30912265", 0.5, 2.6, "82 checks\nfor the *viewing.*", "06-dentro-property-check.png"),
    ], "A viewing lasts twenty minutes. The flat, years.\n\nThe light at the back of the room, the noise with the window open, the corners behind the furniture: 82 checks for the viewing, many of them with your phone.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    chat(9, "20:00", "what-you-pay", ("13441354", 0.5), "Giulia", "Friend", ORANGE_AV, "So, how much are you paying? 🏠",
         [("me", "300k 🙂", 0.0), ("them", "And the taxes, agency, VAT, mortgage?", 0.7), ("me", "…😳", 0.0)],
         "€13,528 more.", "On €300,000, before notary and bank.", "04-costi.png",
         "The price in the listing isn't what you pay.\n\nAn example under Italy's national rules: €300,000 from a private seller, first home, a rendita catastale (the official rental value on the land registry) of €800, agency at 3%, a mortgage of €240,000. Registration tax (imposta di registro) €1,848, mortgage and cadastral taxes €100, agency €10,980 with VAT, tax on the mortgage €600: €13,528, before notary, bank and insurance.\n\nRun the numbers on your own price: try Nesso, link in bio. It's a calculation under national rules, not advice.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Tuesday 10
    chat(10, "08:00", "quiet", ("5835540", 0.5), "Marco", "Agent", VIOLET_AV, "Super quiet street 🤫",
         [("me", "With the window open too?", 0.0), ("them", "Well… the tram goes by at 6 🚋", 0.9)],
         "Open it.\nAnd measure.", "30 seconds open, 30 shut.", "07-misura-rumore-finestra.png",
         "At a viewing the window is almost always shut. Open it.\n\n30 seconds with the window open, 30 with it shut, phone still in the same spot: Nesso compares the two. The number on its own changes from phone to phone, the difference doesn't.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    film(10, "silence", [
        ("31960017", 0.5, 1.2, "Home", None), ("40134358", 0.8, 1.2, "is where", None),
        ("30912265", 0.5, 1.3, "the *quiet*", None), ("6263194", 0.5, 1.5, "waits for you.", None),
        ("29532417", 0.3, 1.3, "Listen", None), ("36300251", 0.5, 1.3, "*first.*", None),
        ("6323324", 0.5, 2.6, "Noise, measured\n*in person.*", "07-misura-rumore-finestra.png"),
    ], "Noise is the most common reason people leave a flat early, and it's the one thing no listing mentions.\n\nAt the viewing: phone in the middle of the room, 30 seconds with the window open and 30 with it shut. Nesso compares the two.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    chat(10, "20:00", "deposit", ("7710747", 0.5), "Owner", "Listing", INK_AV, "Send me €1,000 to hold it? 🙏",
         [("me", "Can I see it first?", 0.0), ("them", "I'm abroad 😕", 0.8), ("me", "Then no.", 0.0)],
         "Viewing first.", "No deposit before you've seen the flat in person.", "06-dentro-property-check.png",
         "One rule about money: no deposit (caparra) before you've seen the flat in person. Not for a rental, not for a purchase.\n\nAnd when you do see it, you have 82 checks in your pocket. Try Nesso: link in bio.\n\n" + TAG_VISIT),

    # ---------------------------------------------------------------- Wednesday 11
    chat(11, "08:00", "together", ("8555712", 0.5), "Luca", "Boyfriend", ORANGE_AV, "Did you like the flat? 😍",
         [("me", "Yes! But did you hear the neighbour?", 0.0), ("them", "What neighbour? 😅", 0.8)],
         "One flat.\nTwo viewings.", "Each of you on your own. Then compare.", "06-dentro-property-check.png",
         "One of you saw the light, the other heard the neighbour.\n\nWith Nesso you both do the same viewing without seeing each other's answers. Then one page shows where you agree and where you don't.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    film(11, "morning-light", [
        ("31960017", 0.5, 1.2, "Morning", None), ("29513615", 0.8, 1.3, "*light*", None),
        ("40134358", 0.5, 1.3, "is worth more", None), ("36300251", 0.5, 1.5, "than a *photo.*", None),
        ("29681899", 0.5, 1.4, "See it", None), ("6798992", 1.0, 1.2, "*in person.*", None),
        ("30912265", 0.5, 2.6, "At the back\nof the *room.*", "06-dentro-property-check.png"),
    ], "Listing photos are taken in the best sun with the widest lens.\n\nAt the viewing, switch the lights off and look at the back wall, not the windowsill. Nesso shows you how, and what that check can't establish.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    chat(11, "20:00", "registration-tax", ("6964001", 0.5), "Sara", "Friend", ORANGE_AV, "The tax is 9% of the price, right? 😱",
         [("me", "First home, private seller: 2%", 0.0), ("me", "And often on the cadastral value", 0.0), ("them", "Meaning? 🤔", 0.7)],
         "€1,848,\nnot €6,000.", "First home, rendita €800, a €300,000 flat.", "04-costi.png",
         "Buy from a private seller as a private person, and the registration tax (imposta di registro) on a first home is 2% of the taxable base (9% on other homes). The base can be the cadastral value (valore catastale): the rendita catastale, the official rental value on the land registry, × 1.05 × 110. You ask for it in the deed.\n\nWith a rendita of €800: €1,848 instead of €6,000 on a €300,000 price.\n\nRun it with your own rendita: try Nesso, link in bio. DPR 131/1986, L. 266/2005. It's a calculation, not advice.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Thursday 12
    chat(12, "08:00", "mum", ("7464106", 0.5), "Mum", "", (226, 124, 176), "Did you look behind the wardrobe? 👀",
         [("me", "Why?", 0.0), ("them", "That's where mould hides.", 0.8), ("them", "Trust me 😌", 0.5)],
         "Mum is\nright.", "Base of the walls, corners, behind furniture.", "06-dentro-property-check.png",
         "Damp is rarely in the middle of a wall. It's low down, in the corners and where furniture hides the wall.\n\nAt the viewing: walk along the base of the outside walls, look behind the furniture and in the corners, look for stains, bubbles or peeling paint. The limit: a stain can be old and dry, and a clean wall can be wet.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    film(12, "corners", [
        ("6323324", 0.5, 1.3, "Every *corner*", None), ("29532417", 0.3, 1.3, "tells you", None),
        ("40187579", 0.5, 1.4, "something.", None), ("36300251", 0.5, 1.3, "The floor.", None),
        ("31960017", 0.5, 1.3, "The windows.", None), ("6263194", 0.5, 1.3, "The *water.*", None),
        ("30912265", 0.5, 2.6, "82 checks\nto *hear them.*", "06-dentro-property-check.png"),
    ], "Floor, windows, water, walls, noise, light.\n\nEvery check on Nesso's list tells you how to do it in a few steps, what you need and what it doesn't establish. Many of them with your phone.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    chat(12, "20:00", "new-city", ("9141848", 0.5), "Chiara", "Colleague", VIOLET_AV, "Welcome to Milan! 🎉",
         [("them", "Where are you looking for a flat?", 0.6), ("me", "I don't know any of the districts 😅", 0.0)],
         "5 questions.\nYour district.", "Find out what kind of local you are.", "02b-quiz-sticker.png",
         "You're moving for work and you don't know the city.\n\nFive questions and Nesso tells you what kind of local you are, with your own sticker, and which district suits you. The districts are read from published data: shops, parks, schools, minutes on foot.\n\nTry Nesso: link in bio.\n\n" + TAG_LIVE),

    # ---------------------------------------------------------------- Friday 13
    chat(13, "08:00", "notary", ("8814707", 0.5), "Paolo", "Friend", ORANGE_AV, "And how much is the notary? 🤔",
         [("me", "It depends 🤷‍♀️", 0.0), ("them", "On what??", 0.6)],
         "No law\nsets it.", "Ask for a written quote. From more than one.", "04-costi.png",
         "How much does the notary (notaio) cost? In Italy no national rule sets the fee, so there's no single number.\n\nAsk for a written quote before the preliminary contract (preliminare), and ask more than one notary. Taxes, agency and the tax on the mortgage do follow exact rules: Nesso works them out.\n\nTry Nesso: link in bio.\n\n" + TAG_COST),
    film(13, "keys", [
        ("6798992", 0.3, 1.2, "Before", None), ("29513615", 0.5, 1.3, "the *keys,*", None),
        ("6323324", 0.5, 1.4, "the numbers.", None), ("30912265", 0.8, 1.3, "Taxes.", None),
        ("36300251", 0.5, 1.2, "Agency.", None), ("29532417", 0.3, 1.2, "*Mortgage.*", None),
        ("6263194", 0.5, 2.6, "All of it,\non your *price.*", "04-costi.png"),
    ], "Before the keys, the numbers.\n\nRegistration tax (imposta di registro), mortgage and cadastral taxes, agency with VAT, the tax on the mortgage: Nesso's calculator works it out on your price, with the law next to every line. Notary, bank and insurance come apart: you need written quotes.\n\nTry Nesso: link in bio.\n\n" + TAG_COST),
    chat(13, "20:00", "vat", ("7646611", 0.5), "Marco", "Agent", VIOLET_AV, "Our fee is 3% 🙂",
         [("me", "Including VAT?", 0.0), ("them", "…no 😬", 0.9)],
         "+22% VAT.", "On €300,000: €10,980, not €9,000.", "04-costi.png",
         "An Italian agency's fee carries VAT (IVA) at 22%. At 3% on €300,000: €9,000 plus €1,980.\n\nOn a first home you can deduct 19% of the fee from your income tax (IRPEF), up to €1,000, in the year you pay it.\n\nRun it with your own percentage: try Nesso, link in bio. It's a calculation, not advice.\n\n" + TAG_COST),

    # ---------------------------------------------------------------- Saturday 14
    chat(14, "08:00", "shower", ("8563625", 0.5), "Elena", "Flatmate", ORANGE_AV, "Is the shower pressure OK? 🚿",
         [("me", "I didn't try 🙈", 0.0), ("them", "Try it with the kitchen tap on 😏", 0.8)],
         "Two taps\nat once.", "One check, one minute, at the viewing.", "06-dentro-property-check.png",
         "With one tap running, almost every flat seems fine.\n\nTurn the kitchen tap on full, switch the shower on too and watch the kitchen flow. The limit: pressure changes through the day and from one floor to the next.\n\nThe other checks for the viewing: try Nesso, link in bio.\n\n" + TAG_VISIT),
    film(14, "selling", [
        ("40187579", 0.5, 1.3, "Selling *a home?*", None), ("40134358", 0.5, 1.3, "What really", None),
        ("36300251", 0.5, 1.4, "*counts,*", None), ("6323324", 0.5, 1.4, "according to", None),
        ("30912265", 0.5, 1.3, "the *research.*", None),
        ("31960017", 0.5, 2.6, "And what only\nhelps the *visit.*", "05-prepara.png"),
    ], "Selling or letting your flat? Prepare is the part of Nesso for the person showing it.\n\nEvery tip says whether research has seen it in the price, whether it makes visible a value that's already there, or whether it only changes the viewing. The smell of coffee, for one, has no study linking it to the price.\n\nTry Nesso: link in bio.\n\n" + TAG_SELL),
    chat(14, "20:00", "sun", ("6799015", 0.5), "Marco", "Agent", VIOLET_AV, "South facing! ☀️",
         [("me", "And the building opposite?", 0.0), ("them", "…it's tall 🫣", 0.9)],
         "Count the hours\nof sun.", "In December too, with the building opposite.", "06-dentro-property-check.png",
         "The building opposite decides your sun too.\n\nIn Nesso you aim your phone at the roofline across the street and the app works out the hours of sun above that roof, today and at the winter solstice. The limit: it sees one roof, not a tree or a balcony.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),

    # ---------------------------------------------------------------- Sunday 15
    chat(15, "08:00", "photos", ("4553290", 0.5), "Sara", "Friend", ORANGE_AV, "Seen the photos? It's huge! 📸",
         [("them", frame("29681899"), 0.0), ("me", "In person it's half that 🙃", 0.0)],
         "Photos make\nrooms bigger.", "Measure the room at the viewing.", "06-dentro-property-check.png",
         "Listing photos are taken from the corner, with the widest lens there is.\n\nAt the viewing, measure it yourself: length, width and height of every room. Nesso's checklist tells you what to measure and how.\n\nTry Nesso: link in bio.\n\n" + TAG_VISIT),
    film(15, "neighbourhood", [
        ("40134358", 0.5, 1.3, "The right", None), ("29681899", 0.5, 1.3, "*district*", None),
        ("6263194", 0.5, 1.4, "changes", None), ("29513615", 0.5, 1.5, "*everything.*", None),
        ("30912265", 0.5, 2.6, "Yours,\nin 5 *questions.*", "02b-quiz-sticker.png"),
    ], "The café downstairs, the park, the school, how many minutes on foot.\n\nFive questions and Nesso tells you what kind of local you are and which district suits you, from published data. Ten Italian cities.\n\nTry Nesso: link in bio.\n\n" + TAG_LIVE),
    chat(15, "20:00", "mortgage", ("8293126", 0.5), "Bank", "Adviser", INK_AV, "Here's our offer! ✨",
         [("me", "Will you send me the PIES too?", 0.0), ("them", "Of course, it's free 📄", 0.8)],
         "Compare\nthe APR.", "Ask several banks for the PIES before you sign.", "04-costi.png",
         "Before a home loan in Italy, the bank owes you the PIES, the sheet with every cost of the mortgage: free and made for you, before you're bound. Ask several banks and compare the TAEG, the Italian APR.\n\nYou get at least seven days to weigh a binding offer, you can move the mortgage to another bank at no cost and pay it off early with no penalty.\n\nInstalment, taxes and costs in Nesso's calculator: try Nesso, link in bio.\nSource: Banca d'Italia, Il mutuo ipotecario in parole semplici (2026).\n\n" + TAG_COST),
]


# ---------------------------------------------------------------- captions that travel
# Every caption: the hook line first, the body, then a question, a save and a share line (the
# signals Instagram weighs most), and five hashtags (Instagram counts five at most since December 2025).
CTA = {
    "visit": ("Save it for your next viewing 📌\nSend it to someone who's flat hunting.",
              "#movingtoitaly #househunting #livinginitaly #expatsinitaly #italianrealestate"),
    "cost": ("Save it before you sign 📌\nSend it to someone buying in Italy.",
             "#italianproperty #italianrealestate #movingtoitaly #expatsinitaly #househunting"),
    "sell": ("Save it if you're selling or letting 📌\nSend it to someone getting their place ready.",
             "#homestaging #italianrealestate #italianproperty #livinginitaly #movingtoitaly"),
    "live": ("Save it if you're moving 📌\nSend it to someone looking for a flat in a new city.",
             "#movingtoitaly #expatsinitaly #livinginitaly #expatlife #lifeinitaly"),
}
QUESTION_CHAT = "Has this happened to you? Tell us in the comments 👇"
QUESTION_FILM = {
    "visit": "What do you look at first in a flat? Tell us in the comments 👇",
    "cost": "Which cost surprised you most? Tell us in the comments 👇",
    "sell": "Which tip have you heard most often? Tell us in the comments 👇",
    "live": "Which city are you looking in? Tell us in the comments 👇",
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
