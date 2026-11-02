"""Week of 9 November 2026, the Danish account (ig-dk): the Stories at 09:30, 15:30 and 21:30.
The Italian week of 2 November (weeks/2026-11-02.py), translated, at the same times (Copenhagen
and Rome are both +01:00 in November). Rendered by tools/render.py into posts/.

Every viewing step is the app's own Danish text from nesso.fit/da/tjekliste-fremvisning (read
2026-11-01, 81 checks in 12 categories). Every kroner figure is from the live Danish calculator,
nesso.fit/da/omkostninger-ved-boligkoeb, run on 3.000.000 kr. with its own defaults on 2026-11-01:
skøde 19.850 kr., pantebrev for realkreditlånet (2.400.000 kr.) 31.825 kr., pantebrev for banklånet
(450.000 kr.) 7.525 kr., i alt 59.200 kr.; fortrydelse within 6 hverdage, 1 % = 30.000 kr.

What changed from the Italian week, and why:
- 15:30 Mon (registro on the cadastral value) and Fri (agency VAT) are Italian taxes: replaced by
  the Danish registration fee on the deed and the 6-day right to withdraw, both from the live page.
- 15:30 Sun (the notary's fee) has no Danish notary: replaced by the buyer's adviser or lawyer, whose
  price the live page says is agreed with them.
- 21:30 "tomorrow at 8" cards announce the Danish 08:00 Reel that actually comes next. The Italian
  cards announced the old check Reels (sheet of paper, draughts, ...) that the chat stories replaced.
"""

MOCK = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-da/"
CH = "ig-dk"


def at(day, time):
    return f"2026-11-{day - 6:02d}T{time}+01:00"  # moved to 3-9 Nov (founder, 2026-11-02)


def screen_story(day, slug, mock):
    return {"id": f"dk-s-screen-{slug}", "type": "story", "channel": CH, "at": at(day, "09:30"),
            "slug": f"historie-skaerm-{slug}", "screen": MOCK + mock}


def card_story(day, time, slug, theme, card, series=None):
    return {"id": f"dk-s-{slug}", "type": "story", "channel": CH, "at": at(day, time),
            "slug": f"historie-{slug}", "theme": theme, "series": series, "card": card}


def tomorrow(day, slug, text):
    return card_story(day, "21:30", f"i-morgen-{slug}", "violet",
                      {"kind": "fact", "label": "I MORGEN KL. 8", "text": text, "sub": "Før du skriver under, ét tjek om dagen."})


ITEMS = [
    # ---------------------------------------------------------------- Monday 9
    screen_story(9, "indenfor", "06-indenfor-property-check.png"),
    card_story(9, "15:30", "fakta-skoede", "orange",
               {"kind": "fact", "label": "VIDSTE DU?", "text": "At tinglyse skødet koster 1.850 kr. plus *0,6 %* af prisen.",
                "sub": "På en bolig til 3 mio. kr.: 19.850 kr.", "source": "Tinglysningsafgiftsloven § 4"}),
    tomorrow(9, "stille", "»Meget stille kvarter.« *Åbn vinduet,* og mål."),

    # ---------------------------------------------------------------- Tuesday 10
    screen_story(10, "stoej", "07-maal-stoej-vindue.png"),
    card_story(10, "15:30", "fakta-kaffe", "orange",
               {"kind": "fact", "label": "FØR DU SÆLGER", "text": "Hæver kaffeduft prisen? *Ingen undersøgelse* viser det.",
                "sub": "Duften løfter humøret i butikker. På boliger er det ikke målt."}),
    tomorrow(10, "to-og-to", "Én bolig, *to fremvisninger.*"),

    # ---------------------------------------------------------------- Wednesday 11
    screen_story(11, "gulv", "08-maal-gulv.png"),
    card_story(11, "15:30", "fakta-ingen-penge", "violet",
               {"kind": "fact", "label": "ÉN REGEL", "text": "Ingen penge, før du har set boligen *selv.*",
                "sub": "Hverken for at leje eller for at købe."}),
    tomorrow(11, "fugt", "Hvor gemmer *fugten* sig?"),

    # ---------------------------------------------------------------- Thursday 12
    screen_story(12, "quiz", "02b-quiz-sticker.png"),
    card_story(12, "15:30", "fakta-forbered", "violet",
               {"kind": "fact", "label": "FØR DU SÆLGER", "text": "Hvad hæver prisen ifølge forskningen?",
                "sub": "Energimærke, lys, ro, en terrasse. I Nesso under Forbered."}),
    tomorrow(12, "advokat", "Hvad koster en *boligadvokat?*"),

    # ---------------------------------------------------------------- Friday 13
    screen_story(13, "investering", "03-investering.png"),
    card_story(13, "15:30", "fakta-fortrydelse", "orange",
               {"kind": "fact", "label": "VIDSTE DU?", "text": "Du kan fortryde et boligkøb inden for *6 hverdage.*",
                "sub": "Det koster 1 % af købesummen: 30.000 kr. på 3 mio.", "source": "LBK nr. 1123/2015"}),
    tomorrow(13, "tryk", "Er der *tryk* i bruseren?"),

    # ---------------------------------------------------------------- Saturday 14
    screen_story(14, "forbered", "05-forbered.png"),
    card_story(14, "15:30", "fakta-lys", "orange",
               {"kind": "fact", "label": "VED FREMVISNINGEN", "text": "Mål lyset ved *bagvæggen,* ikke i vindueskarmen.",
                "sub": "Det er der, du kommer til at læse og arbejde."}),
    tomorrow(14, "billeder", "Var stuen virkelig *så stor?*"),

    # ---------------------------------------------------------------- Sunday 15
    screen_story(15, "bo", "02-bo-kort.png"),
    card_story(15, "15:30", "fakta-raadgiver", "violet",
               {"kind": "fact", "label": "FØR DU SKRIVER UNDER", "text": "Bed rådgiveren om et *skriftligt tilbud.*",
                "sub": "Ingen regel fastsætter prisen."}),
    card_story(15, "21:30", "tjekliste", "violet",
               {"kind": "cta", "text": "81 tjek til den næste fremvisning.", "button": "Link i bio"}, series="Før du skriver under"),
]
