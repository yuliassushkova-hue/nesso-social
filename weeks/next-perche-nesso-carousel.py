"""Perché Nesso, seamless carousel for the week of 9 November (founder feedback 2026-11-01:
only the opening sentence and the phone cross a cut, no "Gratis", logo at the end without a plate).
The first, third and fourth photos changed on 9 November: the earlier ones had been on @nesso_italia.
Render: tools/panorama.py render_panorama(SPEC, out_dir)."""
F = "~/Documents/GitHub/nesso-assets/pexels-photos/"
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"
SPEC = {"slides": 7, "photos": [
    {"file": F + "8082324.jpg", "x": 0, "focus": 0.5},
    {"file": F + "16240690.jpg", "x": 1700, "focus": 0.5},
    {"file": F + "7511695.jpg", "x": 3400, "focus": 0.5},
    {"file": F + "6890395.jpg", "x": 5100, "focus": 0.5},
    {"file": F + "36729696.jpg", "x": 6800, "focus": 0.15},
  ],
  "blocks": [
    # 1 → 2: the opening sentence is the one that runs across the cut.
    {"x": 96, "y": 170, "lines": [("Hai chiesto all'AI", "white", 100)]},
    {"x": 470, "y": 330, "lines": [("se la casa è silenziosa?", "white", 100)], "cross": True},
    # 2
    {"x": 1176, "y": 620, "lines": [("Risposta: «dipende».", "violet", 78)]},
    {"x": 1176, "y": 930, "lines": [("Hai firmato.", "white", 84), ("E alle 6 passa il tram.", "violet", 72)]},
    # 3, then the phone across the cut to 4
    {"x": 2256, "y": 170, "lines": [("L'AI non era lì.", "white", 100)]},
    # 4
    {"x": 3540, "y": 170, "lines": [("Il tuo telefono sì.", "violet", 76)]},
    {"x": 3540, "y": 420, "lines": [("Aperta, poi chiusa.", "white", 70), ("30 secondi.", "white", 70)]},
    {"x": 3540, "y": 760, "lines": [("Ecco quanto rumore", "violet", 66), ("entra davvero.", "violet", 66)]},
    # 5
    {"x": 4416, "y": 180, "lines": [("E i soldi?", "white", 120)]},
    {"x": 4416, "y": 470, "lines": [("€250.000", "white", 84), ("nell'annuncio.", "white", 84)]},
    {"x": 4416, "y": 790, "lines": [("€264.687,50 alla fine.", "violet", 80), ("prima di notaio e banca", "white", 52)]},
    # 6
    {"x": 5496, "y": 150, "lines": [("Nesso fa il conto,", "white", 84), ("riga per riga.", "violet", 84)]},
    # 7
    {"x": 6576, "y": 150, "lines": [("Prima di firmare,", "white", 84), ("chiedi a chi c'era:", "white", 84), ("il tuo telefono.", "violet", 84)]},
    {"x": 6576, "y": 760, "lines": [("Prova Nesso  →", "orange", 84), ("link in bio", "white", 52)]},
  ],
  "phones": [
    {"mock": M + "07-misura-rumore-finestra.png", "x": 3240, "y": 300, "height": 1000, "tilt": -4},
    {"mock": M + "04-costi.png", "x": 5940, "y": 430, "height": 900, "tilt": 4},
  ],
  "mark": {"x": 7020, "y": 1110, "height": 150, "word": "white"},
}
