""""Bolig fra serien": three Danish carousels after the Italian "Casa da serie" ones (weeks/2026-11-17.py,
founder, 2026-11-16), drawn with the same tool (tools/review.py).

The Danish set swaps Montalbano for a Danish series: Huset på Christianshavn (DR, 1970-1977), whose
tenants live in Amagergade 7 with the pet shop on the ground floor and the pub Rottehullet across
the street (da.wikipedia.org/wiki/Huset_på_Christianshavn, read 2026-11-16). Friends and Emily in
Paris stay, on different pictures from the Italian posts so neither account repeats the other's
images: Friends on free photos of the real building (90 Bedford Street) and its street, since the
one unused still in the folder is a colouring-book page; Emily on other Commons photos of Place de
l'Estrapade.

Photos: Wikimedia Commons, ~/Documents/GitHub/nesso-assets/stills/dk/ with SOURCES.md (author,
licence, link). Every photo is credited on its slide and in the caption.
"""

S = "~/Documents/GitHub/nesso-assets/stills/dk/"
ORANGE = (249, 115, 22)  # render.ORANGE


def at(day, time):
    return f"2026-11-{day:02d}T{time}+01:00"


COMMON = {"label": "BOLIG FRA SERIEN", "hint_text": "Swipe  →", "cta": "Prøv Nesso  →", "cta_sub": "link i bio"}

HUSET = {**COMMON, "title": "Huset på Christianshavn", "show": "DR, 1970-77 · Amagergade, København",
         "cover": S + "commons-amagergade-no-7.jpg", "cover_focus": 0.45, "cover_credit": "Foto: Leif Jørgensen, CC BY-SA 4.0",
         "slides": [
             {"photo": S + "commons-amagergade-2020-01.jpg", "head": "DET KAN VI LIDE", "credit": "Foto: Leif Jørgensen, CC BY-SA 4.0",
              "lines": ["En smal gade med brosten på Christianshavn.", "Kanalen et par minutter væk.", "Et helt hus af naboer, der kender hinanden."]},
             {"photo": S + "commons-rottehullet.jpg", "head": "DET VILLE VI TJEKKE", "chip": ORANGE, "credit": "Foto: Mathiaskh, CC BY-SA 3.0",
              "lines": ["I serien ligger værtshuset Rottehullet lige overfor.", "Kom tilbage en fredag aften.", "Mål støjen med telefonen: vinduet åbent, så lukket."]},
             {"photo": S + "commons-amagergade-alley-15911969565.jpg", "head": "BUTIK I STUEN", "credit": "Foto: Tony Webster, CC BY 2.0",
              "lines": ["Nederst har dyrehandler Clausen sin butik.", "Spørg, hvad der ligger i stuen og i kælderen.", "Lyd og lugt fra en butik kan nå op ad trappen."]},
         ],
         "ask": "Ville du bo overfor Rottehullet?", "ask_sub": "Eller hellere over dyrehandleren?"}

MONICA = {**COMMON, "title": "Monicas lejlighed", "show": "Venner · Greenwich Village, New York",
          "cover": S + "commons-90-bedford-street.jpg", "cover_focus": 0.5, "cover_credit": "Foto: EarthLuau, public domain",
          "slides": [
              {"photo": S + "commons-grove-street-img-9019.jpg", "head": "DET KAN VI LIDE", "credit": "Foto: Gryffindor, CC BY-SA 3.0",
               "lines": ["Køkkenet er åbent mod stuen.", "Store vinduer og masser af lys.", "To værelser: plads til en bofælle."]},
              {"photo": S + "commons-new-york-city-greenwich-village-fire-escapes.jpg", "head": "DET VILLE VI TJEKKE", "chip": ORANGE,
               "credit": "Foto: Marc-Lautenbacher, CC BY-SA 4.0",
               "lines": ["Hvem bor overfor? Her: den nøgne nabo.", "Du ser ham. Og han ser dig.", "Kig ud af hvert vindue til fremvisningen: op, ned og ligeud."]},
              {"photo": S + "commons-nyc-greenwich-village-gay-street.jpg", "head": "HUSLEJE-TRICKET", "credit": "Foto: Jean-Christophe Benoist, CC BY 3.0",
               "lines": ["Det var bedstemors lejlighed, med en lav husleje.", "Monica fremlejede den uden at sige det.", "Er en lejlighed for billig, så spørg hvorfor. Og hvem der står på kontrakten."]},
          ],
          "ask": "Ville du bo der?", "ask_sub": "Med naboen overfor, altså."}

EMILY = {**COMMON, "title": "Emilys lejlighed", "show": "Emily in Paris · Place de l'Estrapade, Paris",
         "cover": S + "commons-place-de-l-estrapade-paris-5e-2.jpg", "cover_focus": 0.5, "cover_credit": "Foto: Celette, CC BY-SA 4.0",
         "slides": [
             {"photo": S + "commons-fontaine-de-l-estrapade.jpg", "head": "DET KAN VI LIDE", "credit": "Foto: Moonik, CC BY-SA 3.0",
              "lines": ["En lille plads med træer lige udenfor.", "En restaurant lige overfor.", "Panthéon ligger om hjørnet."]},
             {"photo": S + "commons-p1250557-paris-v-place-estrapade-bis-rwk.jpg", "head": "5. SAL? TÆL SELV", "chip": ORANGE, "credit": "Foto: Mbzt, CC BY-SA 3.0",
              "lines": ["Emily tæller etager på amerikansk og ender ved naboens dør.", "I Paris, som i Danmark, tæller stuen ikke med.", "Spørg til etagen, og tæl selv til fremvisningen."]},
             {"photo": S + "commons-p1250563-paris-v-place-estrapade-bis-rwk.jpg", "head": "FØR FLYTTEDAGEN", "credit": "Foto: Mbzt, CC BY-SA 3.0",
              "lines": ["Smal trappe? Mål den smalleste dør.", "Kan sofaen komme op? Godt at vide, før du skriver under."]},
         ],
         "ask": "Tagetage i Paris eller toværelses med elevator?", "ask_sub": "Vælg i kommentarerne."}

SAVE = "Gem den til næste fremvisning 📌\nSend den til en, der leder efter bolig."


def serie(day, time, slug, spec, body):
    return {"id": f"dk-serie-{slug}", "type": "carousel", "channel": "ig-dk", "at": at(day, time), "slug": f"karrusel-{slug}",
            "review": spec, "caption": body}


ITEMS = [
    serie(20, "18:00", "huset-paa-christianshavn", HUSET,
          "Huset på Christianshavn: beboerne i Amagergade 7, dyrehandleren i stuen og værtshuset Rottehullet lige overfor. Swipe.\n\n"
          "Et værtshus overfor er hyggeligt en tirsdag eftermiddag. Kom tilbage en fredag aften, og mål støjen med telefonen, med vinduet åbent og lukket. "
          "Og spørg, hvad der ligger i stuen og i kælderen.\n\n"
          "Ville du bo overfor Rottehullet? Skriv det i kommentarerne 👇\n" + SAVE +
          "\n\nFotos: Leif Jørgensen (CC BY-SA 4.0), Mathiaskh (CC BY-SA 3.0), Tony Webster (CC BY 2.0), Wikimedia Commons.\n\n"
          "#christianshavn #dr #tvserier #boligjagt #fremvisning"),
    serie(22, "18:00", "monicas-lejlighed", MONICA,
          "Monicas lejlighed i Venner: åbent køkken, store vinduer, to værelser i Greenwich Village. Og en nabo overfor, der aldrig trækker gardinet for. Swipe.\n\n"
          "Det var bedstemors lejlighed med en lav husleje, og Monica fremlejede den uden at sige det. Er en lejlighed for billig, så spørg hvorfor, og hvem der står på kontrakten.\n\n"
          "Ville du bo der, med den nabo? Skriv det i kommentarerne 👇\n" + SAVE +
          "\n\nFotos: EarthLuau (public domain), Gryffindor (CC BY-SA 3.0), Marc-Lautenbacher (CC BY-SA 4.0), Jean-Christophe Benoist (CC BY 3.0), Wikimedia Commons.\n\n"
          "#venner #friends #tvserier #lejebolig #boligjagt"),
    serie(24, "18:00", "emilys-lejlighed", EMILY,
          "Emilys lejlighed i Emily in Paris ligger på en rigtig plads: Place de l'Estrapade. Træer, en restaurant overfor og en etage, der bliver talt forkert. Swipe.\n\n"
          "Emily tæller etagerne på amerikansk og banker på hos naboen. I Paris, som i Danmark, tæller stuen ikke med: spørg til etagen, og tæl selv til fremvisningen.\n\n"
          "Tagetage i Paris eller toværelses med elevator? Skriv det i kommentarerne 👇\n" + SAVE +
          "\n\nFotos: Celette (CC BY-SA 4.0), Moonik (CC BY-SA 3.0), Mbzt (CC BY-SA 3.0), Wikimedia Commons.\n\n"
          "#emilyinparis #tvserier #boligdrøm #fremvisning #boligjagt"),
]
