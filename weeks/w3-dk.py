"""@nesso_danmark, Wednesday 11 to Sunday 15 November: weeks/2026-11-11.py translated, on the same
footage and times.

Every step and limit is the app's own Danish text, nesso.fit/da/tjekliste-fremvisning, read on
9 November. Costs: the live Danish calculator's example, as in weeks/2026-11-09-dk-carousels.py.
App screens: nesso_mobile docs/marketing/mockups-da. Footage and photos: Pexels License. Music: Mixkit.

Replaced, because the Italian fact is Italian or the Danish checklist words it differently:
- 08:00 Wed "caldaia" -> when the windows were changed, as Tuesday's teaser promised.
- Wed and Sun asks and "verbali" -> the owners' association: its plan, minutes and accounts.
- 85 m²: no "superficie commerciale", only the check's own general limit.
- Sat 09:30 "age of the building" (not in the Danish list) -> the reports on the home.
- Sat 12:30 vent test (used on Tuesday) -> stand still and listen.
Carousels: the tram photo and the end photo had been used or read as Italy, so two photos changed.
"""
import copy
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "tools"))
import render  # noqa: E402

BASE = runpy.run_path(str(HERE / "w2-dk.py"))
IT = runpy.run_path(str(HERE / "2026-11-11.py"))
chat, film, card, at = BASE["chat"], BASE["film"], BASE["card"], BASE["at"]
VIOLET_AV, INK_AV = BASE["VIOLET_AV"], BASE["INK_AV"]
ORANGE_AV = (249, 115, 22)
SAVE, TAGS = BASE["SAVE"], BASE["TAGS"]
D = "06-indenfor-property-check.png"
N = "07-maal-stoej-vindue.png"
MOCKS = {"06-dentro-property-check.png": D, "07-misura-rumore-finestra.png": N, "04-costi.png": "04-omkostninger.png",
         "02-vivi-mappa.png": "02-bo-kort.png"}


def ask(day, slug, theme, text, sub):
    return card(day, "09:30", f"spoerg-{slug}", theme, "SPØRG VED FREMVISNINGEN", text, sub)


def tomorrow(day, slug, text):
    return card(day, "21:30", f"imorgen-{slug}", "violet", "I MORGEN KL. 8", text, "Før du skriver under, ét tjek om dagen.")



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


def relabel(spec, blocks, photos=None):
    """The Italian layout with these words. A block's colours and sizes stay unless a line is (text, size)."""
    out = copy.deepcopy(spec)
    assert len(blocks) == len(out["blocks"])
    out["hint_text"] = "Swipe  →"
    for block, new in zip(out["blocks"], blocks):
        old = block["lines"]
        block["lines"] = [(t if isinstance(t, str) else t[0], old[min(i, len(old) - 1)][1],
                           old[min(i, len(old) - 1)][2] if isinstance(t, str) else t[1]) for i, t in enumerate(new)]
        fit(block)
    for phone in out["phones"]:
        name = phone["mock"].rsplit("/", 1)[1]
        phone["mock"] = phone["mock"].replace("mockups-it", "mockups-da").replace(name, MOCKS[name])
    for photo in out["photos"]:
        for old_id, new_id in (photos or {}).items():
            photo["file"] = photo["file"].replace(old_id, new_id)
    return out


CTA = ["Prøv Nesso  →", "link i bio"]
PERCHE = relabel(IT["PERCHE"], [
    ["Har du spurgt AI'en,"], [("om boligen er stille?", 96)], ["Svar: »det kommer an på«."],
    ["Du skrev under.", ("Kl. 6 starter trafikken.", 62)], ["AI'en var der ikke."], ["Din telefon var."],
    ["Åben, så lukket.", "30 sekunder."], ["Så meget støj", "kommer ind."],
    ["Og pengene?"], [("3.000.000 kr.", 80), ("i annoncen.", 80)], [("3.059.200 kr. til sidst.", 74), ("før rådgiver og forsikring", 46)],
    ["Nesso regner det ud,", "linje for linje."], [("Før du skriver under,", 74), ("spørg den, der var der:", 74), "din telefon."], CTA,
], {"16240690": "29546067", "36729696": "5998120"})
PERCHE["mark"]["word"] = "ink"
SPOERG = relabel(IT["CHIEDI"], [
    [("Du er ikke fagmand.", 92)], [("Men du kan spørge.", 104)],
    ["Regningerne", "Bed om 12 måneder.", "Og bygningens", "fællesudgifter."],
    ["Varmen", "Hvad varmer boligen?", "Hvornår blev den", "serviceret?"],
    ["Foreningen", "Hvad er planlagt?"], [("Vedligeholdelsesplan", 66), ("og referater.", 66)],
    ["Vinduerne", "Hvornår blev de", "skiftet? Alle sammen?"], [("Hvis det betyder noget,", 54), ("spørg efter fakturaen.", 54)],
    ["Hvert svar,", "noteret som et svar."], CTA,
])
GADEN = relabel(IT["STRADA"], [
    ["Du har set boligen."], ["Og gaden?"],
    [("Supermarkedet", 86), "Hvor mange minutter?", "Ad rigtige gader,", "ikke i luftlinje."],
    [("Skoler, parker, transport", 66), "Du vælger,", "hvad der tæller."], ["Dit kvarter", "på kortet."],
    ["5 byer", ("Offentliggjorte data,", 58), ("område for område.", 58)], [("Og om aftenen?", 92)],
    [("Et kort ved det ikke.", 70), ("Kom igen efter mørke", 58), "og gå rundt", "om karréen."],
    ["Vælg boligen.", "Og gaden."], CTA,
], {"37382515": "35657824", "30726119": "34916291"})


def carousel(day, slug, spec, caption):
    return {"id": f"dk-k-{slug}", "type": "carousel", "channel": "ig-dk", "at": at(day, "18:00"),
            "slug": f"karrusel-{slug}", "panorama": spec, "caption": caption}


ITEMS = [
    # ---------------------------------------------------------------- Wednesday 11
    chat(11, "08:00", "vinduer", ("7647325", 0.5), "Mikkel", "Mægler", VIOLET_AV, "Alle vinduer er nye 👌",
         [("me", "Hvornår blev de skiftet?", 0.0), ("them", "For nogle år siden, tror jeg 🙂", 0.9), ("me", "Alle sammen? Er der en faktura?", 0.0)],
         "Nye hvornår?\nSpørg efter fakturaen.", "En dato fra hukommelsen er kun det.", D,
         "»For nogle år siden, tror jeg.« En dato fra hukommelsen er kun så god som hukommelsen.\n\nSpørg, hvornår vinduerne blev skiftet, og om alle blev skiftet. Hvis det betyder noget, så spørg, om der er en faktura."),
    ask(11, "foreningen", "orange", "Hvad har foreningen *lavet* de seneste ti år?", "Bed om vedligeholdelsesplan og referater."),
    card(11, "12:30", "raad-radiatorer", "violet", "VED FREMVISNINGEN", "Mærk *hver* radiator, øverst og nederst.",
         "Ti minutter efter, at varmen er tændt."),
    film(11, "overfor", [
        ("7330179", 0.5, 1.3, "Kig ud.", None), ("8517524", 0.5, 1.2, "Hvad er", None),
        ("16668271", 0.5, 1.3, "*overfor?*", None), ("3109518", 0.5, 1.2, "Op.", None),
        ("38916207", 0.5, 1.2, "Ned.", None), ("6000765", 0.5, 1.4, "Fra hvert *vindue.*", None),
        ("36377024", 0.5, 2.6, "Notér,\n*hvad der er der.*", D),
    ], "Se ud af hvert vindue: op, ned og på tværs. Notér, hvad der er der, så gemmer Nesso det i din optegnelse.\n\nDet viser, hvad der er der i dag. En ryddet grund over for er en bygning om to år.",
       end="6798984"),
    card(11, "15:30", "fakta-spraekke", "orange", "VIDSTE DU?", "En sprække ved tærsklen er ofte *tilsigtet.*",
         "En udluftningsspalte og ikke en mangel."),
    carousel(11, "hvorfor-nesso", PERCHE,
             "En chatbot siger »det kommer an på«. Den har aldrig været inde i boligen. Swipe.\n\n"
             "Støj måles i rummet, med vinduet åbent og så lukket. Omkostningerne regnes ud på prisen: en ejerbolig til 3.000.000 kr., 5 % i udbetaling, et realkreditlån på 2.400.000 kr. og et banklån på 450.000 kr. "
             "Det er 59.200 kr. oven i prisen, før rådgiver, ejerskifteforsikring og lånenes egne gebyrer. Det er en beregning efter de gældende satser, ikke rådgivning.\n\n"
             "Prøv Nesso: link i bio.\n\n"
             "Har du spurgt en chatbot til råds om en bolig? Skriv det i kommentarerne 👇\n"
             f"{SAVE}\n\n{TAGS}"),
    chat(11, "20:00", "maling", ("7817155", 0.5), "Ejer", "Annonce", INK_AV, "Jeg har lige malet det hele ✨",
         [("me", "Hvorfor lige den væg?", 0.0), ("them", "Bare for at friske op 🙂", 0.9), ("me", "Det noterer jeg.", 0.0)],
         "Frisk maling?\nSpørg hvorfor.", "Et svar er et svar.", D,
         "Stil dig ved den friske maling eller puds, og spørg, hvorfor det blev repareret.\n\nNesso noterer det, du får at vide, som et svar fra en part med egen interesse og ikke som et faktum."),
    tomorrow(11, "planen", "Lave fællesudgifter i dag. *Og planen?*"),

    # ---------------------------------------------------------------- Thursday 12
    chat(12, "08:00", "planen", ("4752623", 0.5), "Sofie", "Mægler", VIOLET_AV, "Meget lave fællesudgifter 💸",
         [("me", "Hvad er der planlagt af arbejder?", 0.0), ("them", "Ikke noget, jeg kender til… 🤔", 0.9), ("me", "Må jeg se planen og referaterne?", 0.0)],
         "Lavt i dag.\nOg i morgen?", "Planen og referaterne viser det.", D,
         "Fællesudgifterne i dag fortæller ikke, hvad foreningen har planlagt.\n\nSpørg, hvad foreningen har lavet de seneste ti år, og bed om vedligeholdelsesplan og referater. Et svar er kun så fuldstændigt som den, der giver det. Planen og referaterne er optegnelsen, så læs dem."),
    ask(12, "varme", "violet", "Hvad *varmer* boligen?", "Hvor gammelt er det, og hvornår blev det serviceret?"),
    card(12, "12:30", "raad-vinduer", "orange", "VED FREMVISNINGEN", "Åbn *hvert* vindue. Luk det med grebet.",
         "Notér, hvilke der sidder fast eller ikke lukker tæt."),
    film(12, "nabo", [
        ("7646797", 0.5, 1.2, "Møder du", None), ("7646491", 0.5, 1.3, "en *nabo?*", None),
        ("16668197", 0.5, 1.3, "Ét spørgsmål.", None), ("6247901", 0.5, 1.5, "»Hvordan er det her,", None),
        ("8061106", 0.5, 1.5, "også om *natten?*«", None),
        ("8814190", 0.5, 2.6, "Notér,\n*hvad der blev sagt.*", D),
    ], "Hvis du møder en nabo, så stil ét spørgsmål: hvordan er det at bo her, også om natten?\n\nNesso gemmer det som det, der blev sagt. Det er én persons oplevelse, og vedkommende kan have sine egne grunde.",
       end="7646762"),
    card(12, "15:30", "fakta-maaler", "violet", "VIDSTE DU?", "En telefon er *ikke* en støjmåler.",
         "Den sammenligner rum, du måler på samme måde. Ikke en lovgrænse."),
    chat(12, "20:00", "elevator", ("7578478", 0.5), "Paul", "Ejer", INK_AV, "Elevatoren er helt lydløs, lover 🤫",
         [("me", "Må jeg måle?", 0.0), ("them", "Måle… elevatoren? 😅", 0.9), ("me", "Fra soveværelset. Mens nogen bruger den.", 0.0)],
         "30 sekunders stilhed.\nSå elevatoren.", "Telefonen sammenligner de to målinger.", N,
         "Mål soveværelset i ro i 30 sekunder. Mål igen, mens nogen bruger elevatoren.\n\nDet er få minutter en stille eftermiddag. Elevatoren i en etageejendom er mest i brug i de to timer, du ikke var der.",
         size=100),
    tomorrow(12, "bank", "Bank på væggen. *Så på en anden.*"),

    # ---------------------------------------------------------------- Friday 13
    chat(13, "08:00", "bank", ("7817153", 0.5), "Sofie", "Mægler", ORANGE_AV, "Tykke vægge, man hører ingenting 🧱",
         [("me", "Må jeg banke på?", 0.0), ("them", "Banke på? 😅", 0.8), ("me", "Her og på en massiv væg.", 0.0)],
         "Bank her.\nSå på en massiv væg.", "Tonehøjde og lydstyrke. Ikke materialet.", N,
         "Hold telefonen en håndsbredde fra væggen, bank med en knoledd på ét sted, og gentag på en massiv væg. Sammenlign.\n\nDu får en tonehøjde og en lydstyrke, ikke et materiale. Puds på mursten og en skillevæg af stolper kan lyde ens, og telefonen hører rummet med.",
         size=100),
    ask(13, "laekage", "orange", "Har der nogensinde været en *lækage?*", "Blev den anmeldt til forsikringen?"),
    card(13, "12:30", "raad-doer", "violet", "VED FREMVISNINGEN", "Sluk lyset i gangen. *Luk entrédøren.*",
         "Lad lyset i opgangen være tændt, og led efter lys langs kanterne."),
    film(13, "radiatorer", [
        ("7646363", 0.5, 1.2, "Bed om", None), ("7646363", 4.0, 1.2, "at få tændt", None),
        ("6446329", 0.5, 1.5, "for *varmen.*", None), ("7681165", 0.5, 1.3, "Ti minutter.", None),
        ("8482308", 0.5, 1.2, "Så mærk.", None), ("12910157", 0.5, 1.3, "Øverst og *nederst.*", None),
        ("8926989", 0.5, 2.6, "Hver\n*radiator.*", D),
    ], "Bed om at få varmen tændt. Vent ti minutter, og mærk øverst og nederst på hver radiator.\n\nDet er én radiator på én eftermiddag. Det siger intet om kedlen, anlæggets tryk eller, hvad det koster at opvarme denne bolig i januar.",
       end="8293116"),
    card(13, "15:30", "fakta-vaeg", "orange", "VIDSTE DU?", "En plan væg kan skjule *lige så meget* som en bølget.",
         "Lommelygten viser overfladen, ikke hvad der er bagved."),
    carousel(13, "spoerg", SPOERG,
             "Du behøver ikke være fagmand for at stille de rigtige spørgsmål. Swipe.\n\n"
             "Tolv måneders energiregninger og bygningens fællesudgifter. Hvad der varmer boligen, og hvornår det blev serviceret. Foreningens vedligeholdelsesplan og referater. Hvornår vinduerne blev skiftet. "
             "Nesso minder dig om dem ved fremvisningen, og hvert svar bliver noteret som svaret fra den, der gav det.\n\n"
             "Prøv Nesso: link i bio.\n\n"
             "Hvad spørger du altid om ved en fremvisning? Skriv det i kommentarerne 👇\n"
             f"{SAVE}\n\n{TAGS}"),
    chat(13, "20:00", "maegler", ("8555713", 0.5), "Sofie", "Veninde", ORANGE_AV, "Mægleren siger, den er perfekt til os 🥰",
         [("me", "Han kender boligen", 0.0), ("them", "Og hvad så?", 0.6), ("me", "Vi kender os selv 😄", 0.0)],
         "Mægleren kender boligen.\nDu kender dig selv.", "Vælg, hvad der tæller. Nesso vælger tjekkene.", "01-hjem.png",
         "Mægleren ved meget om boligen. Om du sover let, ved du selv.\n\nI Nesso vælger du, hvad der betyder noget for dig, for eksempel ro, lys eller udgifter, og fremvisningen bygges op omkring det. Bagefter har du en optegnelse over, hvad du har tjekket, og hvad der stadig er åbent.",
         size=92),
    tomorrow(13, "areal", "85 kvadratmeter. *Hvilke?*"),

    # ---------------------------------------------------------------- Saturday 14
    chat(14, "08:00", "areal", ("7347759", 0.5), "Mikkel", "Mægler", VIOLET_AV, "85 kvadratmeter, godt indrettet 📐",
         [("me", "Hvilket areal er det?", 0.0), ("them", "Det fra annoncen 🙂", 0.9), ("me", "Må jeg måle selv?", 0.0)],
         "85 kvadratmeter.\nHvilke?", "Spørg, hvilket tal der er brugt.", D,
         "Skriv arealet fra annoncen i Nesso, så stiller den det ved siden af din scanning, og spørg, hvilket tal der er brugt.\n\nDet er en forskel mellem et skøn og en oplysning og ikke bevis for, at nogen har fremstillet noget forkert."),
    ask(14, "rapporter", "violet", "Hvilke *rapporter* findes der om boligen?", "Bed om energimærket, og spørg, hvad der ellers er."),
    card(14, "12:30", "raad-lyt", "orange", "VED FREMVISNINGEN", "Stå stille *i ét minut.*",
         "Midt i rummet. Lyt."),
    film(14, "sofaen", [
        ("4553192", 0.5, 1.3, "Kan *sofaen*", None), ("4554442", 0.5, 1.1, "komme ind?", None),
        ("7033604", 0.5, 1.2, "Mål", None), ("4554461", 0.5, 1.2, "de smalleste", None),
        ("4553192", 4.0, 1.3, "*døre.*", None),
        ("4554461", 4.0, 2.6, "Med scanning\n*eller målebånd.*", D),
    ], "Kan sofaen komme ind? Mål de smalleste døre, før du skriver under, med Nessos scanning eller med et målebånd.\n\nScanningen måler åbningen i karmen, med en til to centimeters afvigelse. Med døren åben tager dørbladet og hængslerne et par centimeter af den.",
       end="7817162"),
    card(14, "15:30", "fakta-plet", "violet", "VIDSTE DU?", "En plet kan være *gammel og tør.*",
         "Og en væg, hvor der intet er at se, kan stadig være våd."),
    chat(14, "20:00", "haelen", ("7624028", 0.5), "Ejer", "Annonce", INK_AV, "Nyt parketgulv, perfekt 🪵",
         [("me", "Må jeg gå gennem stuen og træde fast med hælen?", 0.0), ("them", "…værsgo? 😅", 0.9), ("me", "For at mærke, om det giver efter.", 0.0)],
         "Træd fast med hælen.\nMærk, om det giver efter.", "Ved væggene og midt i rummet.", "08-maal-gulv.png",
         "Gå gennem rummet, og træd fast ned med hælen. Prøv ved væggene og midt i rummet: mærk, om gulvet fjedrer eller giver efter.\n\nDet er dit eget indtryk. Det er ikke en måling af, hvad gulvet bærer, og man kan ikke slutte noget om bæreevnen ud fra det.",
         size=92),
    tomorrow(14, "emhaette", "Emhætten trækker. *Men hvor ender luften?*"),

    # ---------------------------------------------------------------- Sunday 15
    chat(15, "08:00", "emhaette", ("4554454", 0.5), "Sofie", "Veninde", VIOLET_AV, "Nyt køkken, super stærk emhætte 🍳",
         [("me", "Og hvor ender luften?", 0.0), ("them", "Udenfor… tror jeg 🤔", 0.9), ("me", "Jeg spørger.", 0.0)],
         "Emhætten kører.\nHvor ender luften?", "Papir viser, om den trækker. Spørg om resten.", D,
         "Hold papir mod emhætten på hver hastighed. Se på kanalen over den. Spørg så, hvor luften ender.\n\nPapiret viser, at ventilatoren trækker. Kun svaret fortæller, hvor luften ender, og det er en påstand fra den, der svarer.",
         size=100),
    ask(15, "regnskab", "orange", "Må jeg se foreningens *regnskab?*", "Bed også om budgettet og eventuelle lån."),
    card(15, "12:30", "raad-overgange", "violet", "VED FREMVISNINGEN", "Før foden over *hver overgang* mellem gulve.",
         "Notér hvert trin, sprække eller opbulning."),
    film(15, "ovenpaa", [
        ("8558458", 0.5, 1.2, "Ovenpå:", None), ("8558458", 3.0, 1.2, "*hvem bor der?*", None),
        ("7507813", 0.5, 1.4, "Telefon i soveværelset.", None), ("7507813", 3.0, 1.3, "Døren lukket.", None),
        ("8558458", 6.0, 1.5, "30 sekunders\n*stilhed.*", None),
        ("13556489", 0.5, 2.6, "Lyt så\n*selv.*", N),
    ], "Læg telefonen i soveværelset, luk døren, og vær stille i 30 sekunder. Lyt så selv i 30 sekunder.\n\nNesso måler, hvor langt det højeste sekund steg over resten. Det siger ikke, hvad der lavede lyden, og tredive sekunder fanger, hvad der tilfældigvis skete.",
       end="7579472"),
    card(15, "15:30", "fakta-eltavle", "orange", "VIDSTE DU?", "El-tavlen *åbner du ikke.*",
         "Tag billede af den lukket. Resten er en elektrikers arbejde."),
    carousel(15, "gaden", GADEN,
             "Boligen ser du til én fremvisning. Gaden bor du på hver dag. Swipe.\n\n"
             "I Nesso kan du se kvartererne i 5 danske byer med offentliggjorte data. Minutterne til fods tælles ad rigtige gader. "
             "Aftenen kan kun du se: kom igen efter mørkets frembrud, og gå rundt om karréen.\n\n"
             "Prøv Nesso: link i bio.\n\n"
             "Hvad vil du have inden for fem minutter fra hoveddøren? Skriv det i kommentarerne 👇\n"
             f"{SAVE}\n\n{TAGS}"),
    chat(15, "20:00", "cisterne", ("5418696", 0.5), "Paul", "Ejer", INK_AV, "Nyt badeværelse, alt er nyt 🚿",
         [("me", "Må jeg trække ud?", 0.0), ("them", "Undskyld? 😅", 0.8), ("me", "Med timer.", 0.0)],
         "Træk ud.\nStart timeren.", "Lyt så 30 sekunder efter rindende vand.", D,
         "Træk ud, start timeren, og stop, når cisternen holder op med at fylde. Lyt så 30 sekunder efter rindende vand.\n\nHvis vandet bliver ved med at løbe, lader ventilen vand slippe igennem. Hvilken del det er, og hvad der skal til for at rette det, er et spørgsmål til en fagperson."),
    {"id": "dk-s-tjekliste-15", "type": "story", "channel": "ig-dk", "at": at(15, "21:30"), "slug": "historie-tjekliste",
     "theme": "violet", "series": None,
     "card": {"kind": "cta", "text": "Fremvisning i morgen? *81 tjek* venter.", "button": "Link i bio"}},
]
