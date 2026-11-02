"""The fourth Story a day, 12:30 Rome, 9 to 15 November: the Italian 12:30 tips of 2 to 8 November
(weeks/2026-11-02-stories-1230.py) in English. From nesso.fit/it/checklist-visita-casa and
nesso.fit/it/costi-acquisto-casa."""

TIPS = [
    (9, "orange", "AT THE VIEWING", "Open the *window.*", "30 seconds open, 30 shut. The difference is what counts."),
    (10, "violet", "AT THE VIEWING", "Look under the *sink.*", "Torch on, run a finger along every joint."),
    (11, "orange", "DID YOU KNOW?", "The registration tax can start from the *cadastral value.*", "First home, private seller, buying as a private person."),
    (12, "violet", "AS A COUPLE", "Do the viewing *as two.*", "Each on your own. Then compare."),
    (13, "orange", "BEFORE THE MORTGAGE", "Ask several banks for the *PIES.*", "The sheet with every cost, free, before you're bound. Compare the APR (TAEG)."),
    (14, "violet", "AT THE VIEWING", "Two *taps* at once.", "Kitchen and shower on: watch the kitchen flow."),
    (15, "orange", "AT THE VIEWING", "Photos make rooms *look bigger.*", "Measure the room: length, width, height."),
]

ITEMS = [
    {"id": f"en-s-tip-{day}", "type": "story", "channel": "ig-en", "at": f"2026-11-{day - 7:02d}T12:30+01:00",
     "slug": f"story-tip-{day}", "theme": theme,
     "card": {"kind": "fact", "label": label, "text": text, "sub": sub}}
    for day, theme, label, text, sub in TIPS
]
