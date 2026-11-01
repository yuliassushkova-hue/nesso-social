"""A fourth Story a day, 12:30 Rome, 2 to 8 November (founder: 4 Stories a day).
One tip each, from nesso.fit/it/checklist-visita-casa and nesso.fit/it/costi-acquisto-casa."""

TIPS = [
    (2, "orange", "IN VISITA", "Apri la *finestra.*", "30 secondi aperta, 30 chiusa. Conta la differenza."),
    (3, "violet", "IN VISITA", "Guarda sotto il *lavello.*", "Torcia accesa, un dito lungo ogni giunzione."),
    (4, "orange", "LO SAPEVI?", "Il registro può partire dal *valore catastale.*", "Prima casa, da un privato, se compri come persona fisica."),
    (5, "violet", "IN DUE", "Fate la visita *in due.*", "Ognuno per conto suo. Poi confrontate."),
    (6, "orange", "PRIMA DEL MUTUO", "Chiedi il *PIES* a più banche.", "È gratuito, prima che tu sia vincolato. Confronta il TAEG."),
    (7, "violet", "IN VISITA", "Due *rubinetti* insieme.", "Cucina e doccia aperte: guarda il getto in cucina."),
    (8, "orange", "IN VISITA", "Le foto *ingrandiscono.*", "Misura la stanza: lunghezza, larghezza, altezza."),
]

ITEMS = [
    {"id": f"s-tip-{day}", "type": "story", "channel": "ig-it", "at": f"2026-11-{day:02d}T12:30+01:00",
     "slug": f"storia-consiglio-{day}", "theme": theme,
     "card": {"kind": "fact", "label": label, "text": text, "sub": sub}}
    for day, theme, label, text, sub in TIPS
]
