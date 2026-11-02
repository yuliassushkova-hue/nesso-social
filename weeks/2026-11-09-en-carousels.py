"""The English account's four carousels, 9 to 15 November: the Italian seamless carousels of 2 to 8
November (weeks/2026-11-02-carousels.py) translated one to one, same photos, phones and layout.
Only the opening sentence and one phone stand across a cut; the last slide ends on "Try Nesso"
with the logo straight on the photo.

Costs use the app's own example, the one on the phone: €250,000 from a private seller, first home,
no rendita entered, agency at 3%, mortgage of €175,000. Registration tax €5,000, mortgage and
cadastral taxes €50 + €50, agency €7,500 + €1,650 VAT, mortgage tax €437.50: €14,687.50 over the price.
The mortgage rights are Banca d'Italia's, "Il mutuo ipotecario in parole semplici" (2026).
The myths are the Prepare sources (nesso_mobile CLAUDE.md §8ap).
Photos: Pexels License, ~/Documents/GitHub/nesso-assets/pexels-photos/<id>.jpg.
"""

F = "~/Documents/GitHub/nesso-assets/pexels-photos/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-en/"


def at(day):
    return f"2026-11-{day:02d}T18:00+01:00"


def end(x, first, second):
    """The last slide: the thought, the call, the logo on the photo."""
    return [
        {"x": x + 96, "y": 150, "lines": [(first, "white", 84), (second, "violet", 76)]},
        {"x": x + 96, "y": 700, "lines": [("Try Nesso  →", "orange", 84), ("link in bio", "white", 52)]},
    ]


COSTS = {"slides": 7, "hint_text": "Swipe  →", "photos": [
    {"file": F + "4307963.jpg", "x": 0, "focus": 0.5},
    {"file": F + "30139520.jpg", "x": 1700, "focus": 0.4},
    {"file": F + "16600134.jpg", "x": 3400, "focus": 0.5},
    {"file": F + "29034871.jpg", "x": 5100, "focus": 0.6},
    {"file": F + "7579192.jpg", "x": 6700, "focus": 0.3},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Found it: €250,000.", "white", 70)]},
    {"x": 420, "y": 330, "lines": [("But what do you really pay?", "violet", 96)], "cross": True},
    {"x": 1176, "y": 720, "lines": [("Purchase taxes", "white", 70), ("€5,100", "violet", 150), ("buying from a private seller", "white", 50)]},
    {"x": 2256, "y": 170, "lines": [("Agency at 3%", "white", 70), ("€9,150", "violet", 150), ("with VAT at 22%", "white", 50)]},
    {"x": 3540, "y": 170, "lines": [("Mortgage tax", "white", 64), ("€437.50", "violet", 130), ("on a €175,000 loan", "white", 50)]},
    {"x": 4416, "y": 560, "lines": [("On top of the price:", "white", 76), ("€14,687.50", "violet", 130), ("first home, private seller", "white", 50)]},
    {"x": 5496, "y": 150, "lines": [("And the notary?", "white", 96)]},
    {"x": 5496, "y": 420, "lines": [("No law sets", "violet", 80), ("the fee.", "violet", 80)]},
    {"x": 5496, "y": 800, "lines": [("Ask several notaries", "white", 64), ("for a written quote.", "white", 64)]},
    *end(6480, "Run the numbers", "on your price."),
  ],
  "phones": [{"mock": M + "04-costi.png", "x": 3240, "y": 330, "height": 980, "tilt": -4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

VIEWING = {"slides": 8, "hint_text": "Swipe  →", "photos": [
    {"file": F + "19916712.jpg", "x": 0, "focus": 0.5},
    {"file": F + "12932887.jpg", "x": 1400, "focus": 0.35},
    {"file": F + "6077368.jpg", "x": 2800, "focus": 0.5},
    {"file": F + "8092188.jpg", "x": 4300, "focus": 0.4},
    {"file": F + "4010280.jpg", "x": 5900, "focus": 0.5},
    {"file": F + "4307929.jpg", "x": 7300, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("A 20-minute viewing.", "white", 80)]},
    {"x": 470, "y": 340, "lines": [("A 25-year mortgage.", "violet", 104)], "cross": True},
    {"x": 1176, "y": 680, "lines": [("Noise", "violet", 110), ("Window open, then shut.", "white", 58), ("30 seconds each.", "white", 58)]},
    {"x": 2256, "y": 170, "lines": [("Light", "violet", 110), ("On the back wall,", "white", 60), ("not the windowsill.", "white", 60)]},
    {"x": 3336, "y": 170, "lines": [("Floor", "violet", 100), ("Phone on the floor.", "white", 60), ("Read, turn it, read.", "white", 60)]},
    {"x": 4620, "y": 170, "lines": [("Damp", "violet", 100), ("Look low down,", "white", 60), ("in the corners,", "white", 60), ("behind furniture.", "white", 60)]},
    {"x": 5496, "y": 640, "lines": [("Water", "violet", 110), ("Kitchen and shower", "white", 60), ("on together.", "white", 60), ("Watch the flow.", "white", 60)]},
    {"x": 6576, "y": 170, "lines": [("Under the sink", "violet", 96), ("Torch on:", "white", 60), ("a finger on every joint.", "white", 60)]},
    *end(7560, "82 checks", "for your viewing."),
  ],
  "phones": [{"mock": M + "08-misura-pavimento.png", "x": 4320, "y": 400, "height": 920, "tilt": -4}],
  "mark": {"x": 8100, "y": 1110, "height": 150, "word": "white"},
}

MYTHS = {"slides": 7, "hint_text": "Swipe  →", "photos": [
    {"file": F + "8482895.jpg", "x": 0, "focus": 0.35},
    {"file": F + "19916712.jpg", "x": 1500, "focus": 0.5},
    {"file": F + "8092188.jpg", "x": 3200, "focus": 0.45},
    {"file": F + "6077368.jpg", "x": 4900, "focus": 0.5},
    {"file": F + "7579192.jpg", "x": 6400, "focus": 0.3},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("Selling a home?", "white", 104)]},
    {"x": 330, "y": 360, "lines": [("\"Make coffee before the viewing.\"", "violet", 76)], "cross": True},
    {"x": 1176, "y": 720, "lines": [("A higher price?", "white", 64), ("No study", "violet", 84), ("shows it.", "violet", 84)]},
    {"x": 2256, "y": 170, "lines": [("\"Put classical", "white", 68), ("music on.\"", "white", 68)]},
    {"x": 2256, "y": 700, "lines": [("In shops it helps a little.", "white", 56), ("On offers for a home:", "white", 56), ("no evidence.", "violet", 90)]},
    {"x": 3336, "y": 170, "lines": [("\"Empty it,", "white", 76), ("it looks bigger.\"", "white", 76)]},
    {"x": 3336, "y": 700, "lines": [("With furniture it looked", "white", 54), ("a little smaller.", "white", 58), ("In virtual reality:", "white", 58), ("no difference.", "violet", 76)]},
    {"x": 4416, "y": 170, "lines": [("\"Home staging", "white", 70), ("raises the price.\"", "white", 70)]},
    {"x": 4416, "y": 640, "lines": [("In the experiment", "white", 56), ("the home looked", "white", 56), ("more liveable.", "white", 56), ("The estimated value", "violet", 60), ("stayed the same.", "violet", 64)]},
    {"x": 5720, "y": 170, "lines": [("What counts,", "white", 84), ("according to studies:", "white", 62)]},
    {"x": 5720, "y": 560, "lines": [("energy class,", "violet", 62), ("light, quiet,", "violet", 62), ("a terrace.", "violet", 62)]},
    *end(6480, "Prepare your home", "with the evidence."),
  ],
  "phones": [{"mock": M + "05-prepara.png", "x": 5400, "y": 400, "height": 920, "tilt": 4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

MORTGAGE = {"slides": 7, "hint_text": "Swipe  →", "photos": [
    {"file": F + "7579211.jpg", "x": 0, "focus": 0.5},
    {"file": F + "16600134.jpg", "x": 1700, "focus": 0.5},
    {"file": F + "29034871.jpg", "x": 3400, "focus": 0.6},
    {"file": F + "8368754.jpg", "x": 5100, "focus": 0.6},
    {"file": F + "4307929.jpg", "x": 6600, "focus": 0.5},
  ],
  "blocks": [
    {"x": 96, "y": 170, "lines": [("At the bank for a mortgage.", "white", 64)]},
    {"x": 380, "y": 330, "lines": [("Know what they owe you?", "violet", 96)], "cross": True},
    {"x": 1176, "y": 680, "lines": [("The PIES", "violet", 120), ("a sheet with every cost", "white", 58), ("of your mortgage.", "white", 60), ("Free, before you sign.", "white", 60)]},
    {"x": 2256, "y": 170, "lines": [("7 days", "violet", 130), ("at least, to think over", "white", 60), ("the final offer.", "white", 60)]},
    {"x": 3540, "y": 170, "lines": [("Switch banks", "violet", 76), ("whenever you like,", "white", 60), ("no cost, no penalty.", "white", 60)]},
    {"x": 4416, "y": 640, "lines": [("Pay it off early", "violet", 90), ("in full or in part,", "white", 60), ("no penalty.", "white", 60), ("If the loan is for a home.", "white", 50)]},
    {"x": 5496, "y": 170, "lines": [("Ask several banks", "white", 76), ("for the PIES.", "white", 76)]},
    {"x": 5496, "y": 640, "lines": [("Compare the APR:", "violet", 76), ("the mortgage's total", "white", 60), ("cost, as a %.", "white", 60)]},
    *end(6480, "Instalment and costs", "on your price."),
  ],
  "phones": [{"mock": M + "04-costi.png", "x": 3240, "y": 330, "height": 980, "tilt": -4}],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}

CAPTIONS = {
    "costs": ("Buying your first home in Italy: what do you pay on top of the price? Swipe.\n\n"
              "The example is the app's own: €250,000 from a private seller, first home, agency at 3%, a €175,000 mortgage. "
              "Taxes €5,100, agency €9,150 with VAT, tax on the mortgage €437.50: €14,687.50 on top of the price. "
              "Add the rendita catastale (the official rental value on the land registry) and the registration tax (imposta di registro) usually goes down.\n\n"
              "Notary, bank and insurance come apart: no law sets them, so you need written quotes.\n\n"
              "Try Nesso: link in bio. It's a calculation under Italy's national rules, not advice.\n"
              "Sources: DPR 131/1986, D.Lgs. 23/2011, DPR 633/1972, DPR 601/1973.\n\n"
              "Which cost surprised you most? Tell us in the comments 👇\n"
              "Save it before you sign 📌\nSend it to someone buying in Italy.\n\n"
              "#italianproperty #italianrealestate #movingtoitaly #expatsinitaly #househunting"),
    "viewing": ("A viewing lasts twenty minutes. The mortgage, twenty-five years. Swipe.\n\n"
                "Noise, light, floor, damp, water, under the sink: six checks you do at the viewing, many with your phone in your hand. "
                "Nesso's checklist has 82, and each one also says what it can't establish.\n\n"
                "And one rule about money: no deposit (caparra) before you've seen the flat in person.\n\n"
                "Try Nesso: link in bio.\n\n"
                "What do you look at first in a flat? Tell us in the comments 👇\n"
                "Save it for your next viewing 📌\nSend it to someone who's flat hunting.\n\n"
                "#movingtoitaly #househunting #livinginitaly #expatsinitaly #italianrealestate"),
    "myths": ("Coffee, music, home staging, empty rooms: we looked for the studies behind the most repeated tips for selling a home. Swipe.\n\n"
              "Coffee: a meta-analysis of 55 papers on ambient scent in shops and hotels. Music: 32 studies in shops. "
              "Home staging: the experiment by Lane, Seiler and Seiler. Empty rooms: one test on a model and one in virtual reality.\n\n"
              "In Nesso, Prepare sorts the tips into three groups: what research has seen in the price, what makes visible a value that's already there, and what only changes the viewing.\n\n"
              "Try Nesso: link in bio.\n\n"
              "Which tip have you heard most often? Tell us in the comments 👇\n"
              "Save it if you're selling or letting 📌\nSend it to someone getting their place ready.\n\n"
              "#homestaging #italianrealestate #italianproperty #livinginitaly #movingtoitaly"),
    "mortgage": ("Before you sign for a home loan in Italy: what the bank owes you. Swipe.\n\n"
                 "The PIES, the bank's sheet with every cost of the mortgage, free and made for you, before you're bound. At least 7 days to weigh the binding offer. "
                 "Moving the mortgage to another bank (portabilità) at no cost and with no penalty. Paying it off early, in full or in part, with no penalty.\n\n"
                 "Ask several banks for the PIES and compare the TAEG, the Italian APR. Instalment, taxes and costs on your price are in Nesso's calculator.\n\n"
                 "Try Nesso: link in bio.\nSource: Banca d'Italia, Il mutuo ipotecario in parole semplici (2026).\n\n"
                 "Have you asked for the PIES yet? Tell us in the comments 👇\n"
                 "Save it before you go to the bank 📌\nSend it to someone about to apply for a mortgage.\n\n"
                 "#italianproperty #movingtoitaly #expatsinitaly #italianrealestate #mortgage"),
}

ITEMS = [
    {"id": f"en-k-0{i}", "type": "carousel", "channel": "ig-en", "at": at(day), "slug": f"carousel-{name}",
     "panorama": spec, "caption": CAPTIONS[name]}
    for i, (day, name, spec) in enumerate([(9, "costs", COSTS), (11, "viewing", VIEWING), (13, "myths", MYTHS), (15, "mortgage", MORTGAGE)], 1)
]
