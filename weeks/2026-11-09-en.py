"""Week of 9 November 2026, the English account: the Stories of the Italian week of 2 November
(weeks/2026-11-02.py) translated one to one, same times and colours. Rendered by tools/render.py.

Every figure is the Italian week's own: costs from nesso.fit/it/costi-acquisto-casa and its rules
(DPR 131/1986, D.Lgs. 23/2011, L. 266/2005, DPR 633/1972, DPR 601/1973), the myths from the app's
Prepare cards. Times are Rome (+01:00): app screens at 09:30, a fact at 15:30, tomorrow's check at 21:30.
"""

MOCK = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-en/"


def at(day, time):
    return f"2026-11-{day:02d}T{time}+01:00"


def screen_story(day, slug, mock):
    return {"id": f"en-s-screen-{slug}", "type": "story", "channel": "ig-en", "at": at(day, "09:30"),
            "slug": f"story-screen-{slug}", "screen": MOCK + mock}


def card_story(day, time, slug, theme, card, series=None):
    return {"id": f"en-s-{slug}", "type": "story", "channel": "ig-en", "at": at(day, time),
            "slug": f"story-{slug}", "theme": theme, "series": series, "card": card}


def tomorrow(day, slug, text):
    return card_story(day, "21:30", f"tomorrow-{slug}", "violet",
                      {"kind": "fact", "label": "TOMORROW AT 8", "text": text, "sub": "Before you sign, one check a day."})


ITEMS = [
    # ---------------------------------------------------------------- Monday 9
    screen_story(9, "inside", "06-dentro-property-check.png"),
    card_story(9, "15:30", "fact-registration-tax", "orange",
               {"kind": "fact", "label": "DID YOU KNOW?", "text": "Buy from a private seller and the registration tax can start from the *cadastral value*, not the price.",
                "sub": "First home, cadastral income (rendita) €800: €1,848 instead of €6,000 on €300,000.", "source": "DPR 131/1986 · L. 266/2005"}),
    tomorrow(9, "paper", "Does the window really close? You need a *sheet of paper*."),

    # ---------------------------------------------------------------- Tuesday 10
    screen_story(10, "noise", "07-misura-rumore-finestra.png"),
    card_story(10, "15:30", "fact-coffee", "orange",
               {"kind": "fact", "label": "BEFORE YOU SELL", "text": "Does coffee in the oven raise the price? *No study* shows it.", "sub": "Scent lifts the mood in shops. Nobody has measured it on homes."}),
    tomorrow(10, "draughts", "Is there a draught? Feel it with the *back of your hand*."),

    # ---------------------------------------------------------------- Wednesday 11
    screen_story(11, "floor", "08-misura-pavimento.png"),
    card_story(11, "15:30", "fact-deposit", "violet",
               {"kind": "fact", "label": "ONE RULE", "text": "No deposit before you've seen the flat *in person*.", "sub": "Not for a rental, not for a purchase."}),
    tomorrow(11, "damp", "Where does damp hide? *Three places* to look."),

    # ---------------------------------------------------------------- Thursday 12
    screen_story(12, "quiz", "02b-quiz-sticker.png"),
    card_story(12, "15:30", "fact-staging", "violet",
               {"kind": "fact", "label": "BEFORE YOU SELL", "text": "What raises the price, according to research?", "sub": "Energy class, light, quiet, a terrace. In Nesso, under Prepare."}),
    tomorrow(12, "pressure", "Does the water come out strong? Open *two taps* at once."),

    # ---------------------------------------------------------------- Friday 13
    screen_story(13, "investment", "03-investimento-mappa.png"),
    card_story(13, "15:30", "fact-vat", "orange",
               {"kind": "fact", "label": "DID YOU KNOW?", "text": "An Italian agency's fee carries VAT at *22%*.", "sub": "At 3% on €300,000: €9,000 plus €1,980."}),
    tomorrow(13, "light", "How much light reaches the *back* of the room?"),

    # ---------------------------------------------------------------- Saturday 14
    screen_story(14, "prepare", "05-prepara.png"),
    card_story(14, "15:30", "fact-light", "orange",
               {"kind": "fact", "label": "AT THE VIEWING", "text": "Measure the light on the *back wall*, not on the windowsill.", "sub": "That's where you'll read and work."}),
    tomorrow(14, "sink", "Have you ever opened the cupboard *under the sink*?"),

    # ---------------------------------------------------------------- Sunday 15
    screen_story(15, "live", "02-vivi-mappa.png"),
    card_story(15, "15:30", "fact-notary", "violet",
               {"kind": "fact", "label": "BEFORE THE PRELIMINARE", "text": "Ask the notary for a *written quote*.", "sub": "In Italy no national rule sets the fee."}),
    card_story(15, "21:30", "checklist", "violet",
               {"kind": "cta", "text": "82 checks for your next viewing.", "button": "Link in bio"}, series="Before you sign"),
]
