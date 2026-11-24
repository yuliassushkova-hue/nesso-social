"""@nesso_italia, Tuesday 24 November 2026 onward.

Black Friday is the app's welcome gift (nesso_mobile `src/lib/welcome-gift.ts`, live since 16 November):
an account made from the app's gift sheet by 1 December 23:59 Rome gets Full for 2 months, no card, and
goes back to Free on its own. The app is on Android; the iPhone app is not out yet. The words here follow
the sheet's own Italian copy (`src/content/welcome-gift.ts`). Value: Full €6,99 a month × 2 = €13,98.

Music: Meta Sound Collection, Reels Sound pick, one track per Reel.
"""
import runpy
from pathlib import Path

HERE = Path(__file__).parent
BASE = runpy.run_path(str(HERE / "2026-11-09.py"))
at = BASE["at"]
M = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"
LINK = "Scarica l'app · link in bio"
TAGS = "#blackfriday #comprarecasa #cercocasa #visitacasa #primacasa"

BF_BODY = (
    "BLACK FRIDAY: scarica l'app Nesso e crea un account entro il 1° dicembre. Ricevi il piano Full per 2 mesi, "
    "un valore di €13,98. Nulla da pagare, nessuna carta richiesta. Allo scadere dei 2 mesi torna da solo a Free.\n\n"
    "L'app c'è per Android, quella per iPhone è in arrivo. Il link è in bio.\n\n"
    "Con Full hai tutti i controlli per la visita, le mappe dei quartieri e i costi di acquisto riga per riga.\n\n"
    "Chi conosci che sta cercando casa? Taggalo nei commenti 👇\n"
    "Mandalo a chi sta per firmare.\n\n" + TAGS
)

ITEMS = [
    {"id": "r-black-friday-1", "type": "reel", "channel": "ig-it", "at": at(24, "20:00"), "slug": "reel-black-friday",
     "theme": "black", "progress": False, "music": "ready-for-action", "music_gain": 0.6,
     "cards": [
         {"kind": "fact", "secs": 2.6, "label": "BLACK FRIDAY", "text": "2 mesi di Full, *gratis.*",
          "sub": "Per i nuovi account creati dall'app Nesso.", "size": 116},
         {"kind": "big", "secs": 2.4, "over": "Un valore di", "text": "€13,98", "sub": "Nulla da pagare. Nessuna carta."},
         {"kind": "hook", "secs": 2.8, "text": "Scarica l'app.", "sub": "Android ora. iPhone in arrivo.",
          "phone": M + "01-home.png", "phone_height": 900, "phone_top": 1000},
         {"kind": "fact", "secs": 2.6, "label": "FINO AL", "text": "1° dicembre", "size": 124,
          "sub": "Alle 23:59, ora italiana. Dopo 2 mesi torna da solo a Free."},
         {"kind": "brand", "secs": 2.2, "sub": LINK},
     ],
     "caption": BF_BODY},
    {"id": "s-black-friday-24", "type": "story", "channel": "ig-it", "at": at(24, "21:30"), "slug": "storia-black-friday",
     "theme": "black", "series": None,
     "card": {"kind": "cta", "text": "Black Friday: *2 mesi di Full* gratis, dall'app.", "button": "Link in bio"}},
]
