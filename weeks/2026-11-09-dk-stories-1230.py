"""The fourth Story a day on the Danish account, 12:30, 9 to 15 November: the Italian 12:30 tips
(weeks/2026-11-02-stories-1230.py), translated. Steps from nesso.fit/da/tjekliste-fremvisning,
the fee from nesso.fit/da/omkostninger-ved-boligkoeb.

Replaced: Wednesday's Italian tip (registro on the cadastral value) by the Danish fee on each
mortgage deed; Friday's (ask several banks for the PIES) by the checklist's own ask for the energy
label and the other reports, because the PIES is an Italian bank form.
"""

TIPS = [
    (9, "orange", "VED FREMVISNINGEN", "Åbn *vinduet.*", "30 sekunder åbent, 30 lukket. Se på forskellen."),
    (10, "violet", "VED FREMVISNINGEN", "Kig under *vasken.*", "Lommelygten tændt, en finger langs hver samling."),
    (11, "orange", "VIDSTE DU?", "Hvert lån får sit eget *pantebrev.*", "Det koster 1.825 kr. plus 1,25 % af lånet at tinglyse."),
    (12, "violet", "TO OG TO", "Gå fremvisningen igennem *hver for sig.*", "Sammenlign bagefter."),
    (13, "orange", "FØR DU KØBER", "Bed om *energimærket.*", "Og spørg, hvilke andre rapporter der findes."),
    (14, "violet", "VED FREMVISNINGEN", "To *haner* på én gang.", "Køkken og bruser åbne: se på strålen i køkkenet."),
    (15, "orange", "VED FREMVISNINGEN", "Billederne *forstørrer.*", "Mål rummet: længde, bredde, højde."),
]

ITEMS = [
    {"id": f"dk-s-tip-{day}", "type": "story", "channel": "ig-dk", "at": f"2026-11-{day - 6:02d}T12:30+01:00",
     "slug": f"historie-raad-{day}", "theme": theme,
     "card": {"kind": "fact", "label": label, "text": text, "sub": sub}}
    for day, theme, label, text, sub in TIPS
]
