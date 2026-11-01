"""Approved by the founder on 2026-11-01 for the week of 9 November: the first two posts of the
"Perché Nesso" pillar (CREATIVE.md §7). Move them into that week's batch file: the Reel as a chat
item (with sound), the carousel at a free 18:00 slot. Paths are absolute so the samples render as is."""
P = "/Users/juliasushkova/Documents/GitHub/nesso-assets/pexels/"
M = "/Users/juliasushkova/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"
REEL = {"scenes": [
    {"kind": "photo", "secs": 2.1, "clip": {"file": P + "7710747.mp4", "start": 0.5}, "who": "Sara", "color": (249, 115, 22),
     "bubble": "Chiedilo all'AI se la casa è rumorosa 🤖"},
    {"kind": "chat", "secs": 5.4, "who": "Sara", "role": "Amica", "color": (249, 115, 22), "messages": [
        {"at": 0.0, "from": "them", "text": "Chiedilo all'AI se la casa è rumorosa 🤖"},
        {"at": 1.2, "from": "me", "text": "L'ho chiesto 🙃"},
        {"at": 2.6, "from": "them", "text": "E?", "typing": 0.5},
        {"at": 4.0, "from": "me", "text": "Ha detto «dipende» 😅"},
    ]},
    {"kind": "headline", "secs": 2.8, "text": "L'AI non è nella stanza.\nIl tuo telefono sì.",
     "sub": "Nesso misura rumore, pavimento e sole, in visita.", "phone": M + "07-misura-rumore-finestra.png", "size": 104},
    {"kind": "end", "secs": 2.0, "line": "Prima di firmare.", "cta": "Prova Nesso · link in bio"},
]}
CAROUSEL = {"series": "Perché Nesso", "theme": "orange", "slides": [
    {"text": "Chiedi a un chatbot se la casa è *rumorosa.*", "sub": "Non lo sa. Non è lì.", "photo": M + "07-misura-rumore-finestra.png"},
    {"over": "Un chatbot legge.", "big": "Nesso misura.", "big_size": 150, "text": "Rumore a finestra aperta e chiusa, pendenza del pavimento, sole sopra il palazzo di fronte.", "sub": "Col telefono, durante la visita."},
    {"over": "In Italia", "big": "10 città", "big_size": 170, "text": "Quartieri letti con dati pubblicati: OMI, ISTAT, OpenStreetMap.", "sub": "I minuti a piedi si contano sulle strade vere, non in linea d'aria."},
    {"over": "Le spese", "big": "Ogni riga", "big_size": 160, "text": "con la sua legge accanto.", "sub": "Registro, ipotecaria e catastale, IVA, imposta sul mutuo: DPR 131/1986, D.Lgs. 23/2011, L. 266/2005."},
    {"over": "Onestà", "big": "Ogni controllo", "big_size": 130, "text": "dice cosa non può stabilire.", "sub": "Un telefono non è un fonometro. Lo diciamo prima noi."},
    {"over": "In due", "big": "Alla cieca", "big_size": 150, "text": "Fate la stessa visita senza vedere le risposte dell'altro.", "sub": "Poi una pagina sola: dove siete d'accordo e dove no."},
    {"text": "Una seconda opinione, prima di firmare.", "sub": "Ci paga solo chi cerca casa.", "button": "Link in bio"},
]}
