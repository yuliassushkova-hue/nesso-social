"""@nesso_global, Wednesday 11 to Sunday 15 November: weeks/2026-11-11.py translated one to one, on the
same footage, music and times. Italian facts and € figures stay, an Italian term is explained once.

Every step and limit is the app's own text, nesso.fit/it/checklist-visita-casa, read on 9 November.
App screens: nesso_mobile docs/marketing/mockups-en. Footage and photos: Pexels License. Music: Mixkit.
"""
import copy
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "tools"))
import render  # noqa: E402

BASE = runpy.run_path(str(HERE / "w2-en.py"))
IT = runpy.run_path(str(HERE / "2026-11-11.py"))
chat, film, card, tomorrow, at = BASE["chat"], BASE["film"], BASE["card"], BASE["tomorrow"], BASE["at"]
ORANGE_AV, VIOLET_AV, INK_AV = BASE["ORANGE_AV"], BASE["VIOLET_AV"], BASE["INK_AV"]
_, SAVE, TAGS = BASE["FILM"]["visit"]
D = "06-dentro-property-check.png"
N = "07-misura-rumore-finestra.png"


def ask(day, slug, theme, text, sub):
    return card(day, "09:30", f"ask-{slug}", theme, "ASK AT THE VIEWING", text, sub)



def fit(block):
    """Shrink a line only as far as it needs to stay inside its slide (tools/panorama.py refuses otherwise)."""
    limit = (block["x"] // 1080 + 1) * 1080 - 60 - block["x"]
    if block.get("cross"):
        return
    lines = []
    for text, style, size in block["lines"]:
        while render.font(size, 800).getlength(text) + 2 * round(size * 0.3) > limit:
            size -= 2
        lines.append((text, style, size))
    block["lines"] = lines


def relabel(spec, blocks):
    """The Italian layout and photos with these words. A block's colours and sizes stay unless a line is (text, size)."""
    out = copy.deepcopy(spec)
    assert len(blocks) == len(out["blocks"])
    out["hint_text"] = "Swipe  →"
    for block, new in zip(out["blocks"], blocks):
        old = block["lines"]
        block["lines"] = [(t if isinstance(t, str) else t[0], old[min(i, len(old) - 1)][1],
                           old[min(i, len(old) - 1)][2] if isinstance(t, str) else t[1]) for i, t in enumerate(new)]
        fit(block)
    for phone in out["phones"]:
        phone["mock"] = phone["mock"].replace("mockups-it", "mockups-en")
    return out


CTA = ["Try Nesso  →", "link in bio"]
PERCHE = relabel(IT["PERCHE"], [
    ["You asked AI"], ["if the flat is quiet?"], ["Its answer: \"it depends\"."],
    ["You signed.", ("And at 6 the tram goes by.", 62)], ["AI wasn't there."], ["Your phone was."],
    ["Open, then shut.", "30 seconds."], ["That's how much noise", "really gets in."],
    ["And the money?"], ["€250,000", "in the listing."], [("€264,687.50 in the end.", 76), "before notary and bank"],
    ["Nesso does the sums,", "line by line."], ["Before you sign,", "ask whoever was there:", "your phone."], CTA,
])
ASK = relabel(IT["CHIEDI"], [
    [("You're no engineer.", 92)], [("But you can ask.", 104)],
    ["The bills", "Ask for 12 months.", "And the building's", "accounts."],
    ["The boiler", "When was it", "installed?", "Ask for the logbook."],
    ["The works", "Voted or planned?"], [("The last two sets", 66), ("of assembly minutes.", 66)],
    ["The windows", "When were they", "changed? All of them?"], ["If it matters,", "ask for the invoice."],
    ["Every answer,", "kept as an answer."], CTA,
])
STREET = relabel(IT["STRADA"], [
    ["You've seen the flat."], ["And the street?"],
    [("The supermarket", 84), "How many minutes on foot?", "On real streets,", "not as the crow flies."],
    [("Schools, parks, transport", 68), "You choose", "what matters."], ["Your neighbourhood", "on the map."],
    ["10 cities", "Published data,", "area by area."], ["After dark?"],
    ["A map can't tell you.", "Go back after dark", "and walk", "the block."],
    ["Choose the flat.", "And the street."], CTA,
])


def carousel(day, slug, spec, caption):
    return {"id": f"en-k-{slug}", "type": "carousel", "channel": "ig-en", "at": at(day, "18:00"),
            "slug": f"carousel-{slug}", "panorama": spec, "caption": caption}


ITEMS = [
    # ---------------------------------------------------------------- Wednesday 11
    chat(11, "08:00", "boiler", ("7647325", 0.5), "Marco", "Agency", VIOLET_AV, "The boiler's almost new 👌",
         [("me", "What year is it?", 0.0), ("them", "Recent, I think 🙂", 0.8), ("me", "Can I see the logbook?", 0.0)],
         "Recent how?\nAsk for the logbook.", "How it's doing is for a heating engineer.", D,
         "\"Recent, I think.\" A date from memory is only as good as the memory.\n\nAsk when the boiler was installed and ask to see its logbook (the libretto). The limit: that gets you a date and a logbook. How the boiler is doing is a question for a heating engineer."),
    ask(11, "works", "orange", "What works are *voted* or planned?", "Ask for the last two sets of assembly minutes."),
    card(11, "12:30", "tip-radiators", "violet", "AT THE VIEWING", "Touch *every* radiator, top and bottom.",
         "Ten minutes after the heating goes on."),
    film(11, "opposite", [
        ("7330179", 0.5, 1.3, "Look out.", None), ("8517524", 0.5, 1.2, "What's", None),
        ("16668271", 0.5, 1.3, "*opposite?*", None), ("3109518", 0.5, 1.2, "Up.", None),
        ("38916207", 0.5, 1.2, "Down.", None), ("6000765", 0.5, 1.4, "From every *window.*", None),
        ("36377024", 0.5, 2.6, "Note\n*what's there.*", D),
    ], "Look out of every window: up, down and straight across. Note what's there and Nesso keeps it in your record.\n\nThe limit: it's what's there today. A clear plot opposite is, two years on, a building.",
       end="6798984"),
    card(11, "15:30", "fact-gap", "orange", "DID YOU KNOW?", "A gap under the door is often *deliberate.*",
         "It can be a ventilation gap rather than a defect."),
    carousel(11, "why-nesso", PERCHE,
             "A chatbot tells you \"it depends\". It has never been inside that flat. Swipe.\n\n"
             "Noise is measured in the room, with the window open and then shut. Costs are worked out on the price: €250,000 from a private seller, first home, agency at 3%, mortgage of €175,000. "
             "That's €14,687.50 on top of the price, before notary and bank. It's a calculation on national rules, not advice.\n\n"
             "Try Nesso: link in bio.\n\n"
             "Have you ever asked a chatbot for advice on a home? Tell us in the comments 👇\n"
             f"{SAVE}\n\n{TAGS}"),
    chat(11, "20:00", "paint", ("7817155", 0.5), "Owner", "Listing", INK_AV, "I've just repainted everything ✨",
         [("me", "Why that wall in particular?", 0.0), ("them", "Just to freshen it up 🙂", 0.9), ("me", "I'll make a note.", 0.0)],
         "Fresh paint?\nAsk why.", "An answer stays an answer.", D,
         "Most repairs are ordinary upkeep. The reason is the part you can't see, so ask for it.\n\nStand in front of the new paint or plaster and ask why it was repaired. Nesso keeps what you're told as an answer from someone with an interest, not as a fact."),
    tomorrow(11, "minutes", "Low charges today. And the works *already voted?*"),

    # ---------------------------------------------------------------- Thursday 12
    chat(12, "08:00", "minutes", ("4752623", 0.5), "Giulia", "Agency", VIOLET_AV, "Building charges are really low 💸",
         [("me", "And the works already voted?", 0.0), ("them", "Not that I know of… 🤔", 0.9), ("me", "Can I read the last two minutes?", 0.0)],
         "Low charges, today.\nAnd tomorrow?", "Voted works are in the minutes.", D,
         "Today's charges don't tell you what the building has already decided.\n\nAsk what works are voted or planned and ask for the last two sets of assembly minutes (the verbali). The limit: a spoken answer is as complete as the person giving it. The minutes are the document, so read them.",
         cat="cost"),
    ask(12, "windows", "violet", "When were the *windows* changed?", "All of them? If it matters, ask if there's an invoice."),
    card(12, "12:30", "tip-windows", "orange", "AT THE VIEWING", "Open *every* window. Shut it with the handle.",
         "Note the ones that stick or won't lock."),
    film(12, "neighbour", [
        ("7646797", 0.5, 1.2, "Meet", None), ("7646491", 0.5, 1.3, "a *neighbour?*", None),
        ("16668197", 0.5, 1.3, "One question.", None), ("6247901", 0.5, 1.5, "\"What's it like here,", None),
        ("8061106", 0.5, 1.5, "even at *night?*\"", None),
        ("8814190", 0.5, 2.6, "Note\n*what they said.*", D),
    ], "If you meet a neighbour, ask one question: what's it like living here, even at night?\n\nNesso keeps it as what they said. The limit: it's one person's experience, and they may have a reason of their own.",
       end="7646762"),
    card(12, "15:30", "fact-meter", "violet", "DID YOU KNOW?", "A phone *isn't* a sound level meter.",
         "It compares rooms measured the same way. Not a legal limit."),
    chat(12, "20:00", "lift", ("7578478", 0.5), "Paolo", "Owner", INK_AV, "The lift is silent, I swear 🤫",
         [("me", "Can I measure it?", 0.0), ("them", "Measure… the lift? 😅", 0.9), ("me", "From the bedroom. While someone uses it.", 0.0)],
         "30 seconds of silence.\nThen the lift.", "Your phone compares the two.", N,
         "Measure the bedroom in silence for 30 seconds. Then measure again while someone uses the lift.\n\nThe limit: it's a few minutes of a quiet afternoon. In a block of flats the lift works hardest in the two hours you weren't there.",
         size=104),
    tomorrow(12, "knock", "Knock on the wall. *Then on another.*"),

    # ---------------------------------------------------------------- Friday 13
    chat(13, "08:00", "knock", ("7817153", 0.5), "Sara", "Agency", ORANGE_AV, "Thick walls, you can't hear a thing 🧱",
         [("me", "Can I knock?", 0.0), ("them", "Knock? 😅", 0.8), ("me", "Here and on a solid wall.", 0.0)],
         "Knock here.\nThen on a solid wall.", "Pitch and volume. Not the material.", N,
         "Hold your phone a hand's width from the wall, knock on one spot and repeat on a solid wall. Then compare.\n\nThe limit: you get a pitch and a volume, not a material. Plaster on brick and plasterboard can sound the same, and the phone hears the room too.",
         size=104),
    ask(13, "insurance", "orange", "Has there been an *insurance claim?*", "It's an answer. The insurance file is where you can check it."),
    card(13, "12:30", "tip-door", "violet", "AT THE VIEWING", "Hall light off. *Shut the front door.*",
         "Landing light on: look for light around the edges."),
    film(13, "radiators", [
        ("7646363", 0.5, 1.2, "Ask them", None), ("7646363", 4.0, 1.2, "to turn on", None),
        ("6446329", 0.5, 1.5, "the *heating.*", None), ("7681165", 0.5, 1.3, "Ten minutes.", None),
        ("8482308", 0.5, 1.2, "Then touch.", None), ("12910157", 0.5, 1.3, "Top and *bottom.*", None),
        ("8926989", 0.5, 2.6, "Every\n*radiator.*", D),
    ], "Ask them to turn on the heating. Wait ten minutes and touch the top and bottom of every radiator.\n\nThe limit: it's one radiator on one afternoon. It says nothing about the boiler, the system's pressure, or what it costs to heat this home in January.",
       end="8293116"),
    card(13, "15:30", "fact-wall", "orange", "DID YOU KNOW?", "A flat wall can hide *as much as* a wavy one.",
         "A torch shows the surface, not what's behind it."),
    carousel(13, "ask", ASK,
             "You don't need to be an engineer to ask the right questions. Swipe.\n\n"
             "Twelve months of bills and the building's accounts. The boiler's date and its logbook. Works voted or planned, with the last two sets of minutes. When the windows were changed. "
             "Nesso reminds you of these at the viewing, and each answer stays recorded as the answer of whoever gave it.\n\n"
             "Try Nesso: link in bio.\n\n"
             "What do you always ask at a viewing? Tell us in the comments 👇\n"
             f"{SAVE}\n\n{TAGS}"),
    chat(13, "20:00", "agent", ("8555713", 0.5), "Sara", "Friend", ORANGE_AV, "The agent says it's perfect for us 🥰",
         [("me", "He knows the flat", 0.0), ("them", "So?", 0.6), ("me", "We know us 😄", 0.0)],
         "The agent knows the flat.\nYou know you.", "Pick what matters. Nesso picks the checks.", "01-home.png",
         "The agent knows a lot about the flat. Whether you're a light sleeper, you know.\n\nIn Nesso you choose what matters to you, like quiet, light or costs, and the viewing is built around it. At the end you have a record of what you checked and what's still open.",
         size=100),
    tomorrow(13, "sqm", "85 square metres. *Which ones?*"),

    # ---------------------------------------------------------------- Saturday 14
    chat(14, "08:00", "sqm", ("7347759", 0.5), "Marco", "Agency", VIOLET_AV, "85 square metres, well laid out 📐",
         [("me", "Commercial or walkable?", 0.0), ("them", "Commercial, of course 🙂", 0.9), ("me", "So walls and cellar too?", 0.0)],
         "85 square metres.\nWhich ones?", "Ask which figure was used.", D,
         "Italian listings quote different surfaces. The commercial surface (superficie commerciale) legitimately includes the walls, the balconies and the cellar.\n\nEnter the listing's figure in Nesso and it sits next to the one you measured. The limit: it's the difference between an estimate and a statement, and it doesn't prove anyone said anything false."),
    ask(14, "building", "violet", "What year was the *building* built?", "Look at the façade and the stairs, then ask."),
    card(14, "12:30", "tip-vent", "orange", "AT THE VIEWING", "A strip of tissue on the *vent.*",
         "Let go of the bottom end: does it stick or fall?"),
    film(14, "sofa", [
        ("4553192", 0.5, 1.3, "Will the *sofa*", None), ("4554442", 0.5, 1.1, "fit?", None),
        ("7033604", 0.5, 1.2, "Measure", None), ("4554461", 0.5, 1.2, "the doors.", None),
        ("4553192", 4.0, 1.3, "The *narrowest.*", None),
        ("4554461", 4.0, 2.6, "With a scan\n*or a tape.*", D),
    ], "Will the sofa fit? Measure the narrowest doors before you sign, with Nesso's scan or with a tape.\n\nThe limit: the scan measures the opening in the frame, to within a centimetre or two. With the door open, the leaf and hinges take a few more.",
       end="7817162"),
    card(14, "15:30", "fact-stain", "violet", "DID YOU KNOW?", "A stain can be *old and dry.*",
         "And a wall with nothing to see can still be wet."),
    chat(14, "20:00", "heel", ("7624028", 0.5), "Owner", "Listing", INK_AV, "New parquet, perfect 🪵",
         [("me", "Can I walk across stamping my heel?", 0.0), ("them", "…be my guest? 😅", 0.9), ("me", "To feel if it gives.", 0.0)],
         "Stamp your heel.\nFeel if it gives.", "In the middle and by the walls.", "08-misura-pavimento.png",
         "Walk across the room stamping your heel. Try by the walls and in the middle: feel if the floor bounces or gives.\n\nThe limit: it's your own impression. It doesn't measure what the floor will hold, and you can't conclude anything about load from it."),
    tomorrow(14, "hood", "The hood is on. *But where does the air go?*"),

    # ---------------------------------------------------------------- Sunday 15
    chat(15, "08:00", "hood", ("4554454", 0.5), "Chiara", "Friend", VIOLET_AV, "New kitchen, super strong hood 🍳",
         [("me", "And where does the air go?", 0.0), ("them", "Outside… I think 🤔", 0.9), ("me", "I'll ask.", 0.0)],
         "Hood on.\nWhere does the air go?", "A tissue shows if it pulls. Ask the rest.", D,
         "Hold a tissue to the hood at each speed. Look at the duct above it. Then ask where the air goes.\n\nThe limit: the paper shows the fan is pulling. Only the answer tells you where the air ends up, and that's a claim by whoever answers.",
         size=104),
    ask(15, "disputes", "orange", "Any *disputes* in the building?", "Or unpaid charges? Ask for the last two sets of minutes."),
    card(15, "12:30", "tip-joins", "violet", "AT THE VIEWING", "Run your foot over *every join* between two floors.",
         "Note every step, gap or ridge."),
    film(15, "upstairs", [
        ("8558458", 0.5, 1.2, "Upstairs,", None), ("8558458", 3.0, 1.2, "*who's there?*", None),
        ("7507813", 0.5, 1.4, "Phone in the bedroom.", None), ("7507813", 3.0, 1.3, "Door shut.", None),
        ("8558458", 6.0, 1.5, "30 seconds\nof *silence.*", None),
        ("13556489", 0.5, 2.6, "Then listen\n*yourself.*", N),
    ], "Put your phone in the bedroom, shut the door and stay silent for 30 seconds. Then listen yourself for another 30.\n\nThe limit: Nesso measures how far the loudest second rose above the rest. It doesn't say what made the noise, and thirty seconds catch whatever happened at that moment.",
       end="7579472"),
    card(15, "15:30", "fact-fusebox", "orange", "DID YOU KNOW?", "You *don't open* the fuse box.",
         "Photograph it shut. The rest is an electrician's job."),
    carousel(15, "street", STREET,
             "You see the flat at one viewing. You live on the street every day. Swipe.\n\n"
             "In Nesso the neighbourhoods of 10 Italian cities are read from published data: the tax agency's OMI property quotations, ISTAT and OpenStreetMap. Minutes on foot are counted on real streets. "
             "The evening is something only you can see: go back after dark and walk the block.\n\n"
             "Try Nesso: link in bio.\n\n"
             "What do you want within five minutes of home? Tell us in the comments 👇\n"
             f"{SAVE}\n\n#movingtoitaly #househunting #livinginitaly #expatsinitaly #italianrealestate"),
    chat(15, "20:00", "flush", ("5418696", 0.5), "Paolo", "Owner", INK_AV, "New bathroom, everything's new 🚿",
         [("me", "Can I flush the toilet?", 0.0), ("them", "Excuse me? 😅", 0.8), ("me", "With a timer.", 0.0)],
         "Flush it.\nStart the timer.", "Then listen 30 seconds for running water.", D,
         "Flush, start the timer and stop it when the cistern stops filling. Then listen for 30 seconds for running water.\n\nThe limit: if it keeps running, the valve is letting water through. Which part it is, and how to fix it, is a question for a plumber."),
    {"id": "en-s-checklist-15", "type": "story", "channel": "ig-en", "at": at(15, "21:30"), "slug": "story-checklist-viewing",
     "theme": "violet", "series": None,
     "card": {"kind": "cta", "text": "Viewing tomorrow? *82 checks* are waiting.", "button": "Link in bio"}},
]
