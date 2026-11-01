"""Week of 2 November 2026, @nesso_italia. Rendered by tools/render.py into posts/.

Every step and every "cosa non stabilisce" line is the app's own text from
nesso.fit/it/checklist-visita-casa (read 2026-11-01). Every euro figure is from
nesso.fit/it/costi-acquisto-casa and its rules (DPR 131/1986, D.Lgs. 23/2011, L. 266/2005,
DPR 633/1972, DPR 601/1973); the €300.000 example was recomputed by hand. The myths are the app's
own Prepare cards (PREPARE_MYTHS) with their sources.

Times are Rome (+01:00). Reels at 08:00, 13:00, 20:00; carousels at 18:00 on Mon, Wed, Fri, Sun;
stories at 09:30, 15:30, 21:30.
"""

MOCK = "~/Documents/GitHub/nesso_mobile/docs/marketing/mockups-it/"
VID = "~/Documents/GitHub/nesso_mobile/docs/marketing/videos-it/"
TAGS_VISIT = "#cercocasa #visitacasa #comprarecasa #affittocasa #casa"
TAGS_COST = "#comprarecasa #primacasa #mutuo #casa #Milano"
TAGS_SELL = "#vendocasa #venderecasa #homestaging #casa #immobiliare"
LINK = "Gli altri controlli per la visita, gratis e senza registrazione: link in bio."


def at(day, time):
    return f"2026-11-{day:02d}T{time}+01:00"


def check(n, day, slug, theme, hook, sub, steps, limit, intro):
    cards = [{"kind": "hook", "text": hook, "sub": sub, "secs": 2.6}]
    cards += [{"kind": "step", "n": i, "text": s, "secs": 2.8} for i, s in enumerate(steps, 1)]
    cards += [
        {"kind": "note", "text": limit, "secs": 3.4, "theme": "night"},
        {"kind": "cta", "text": "82 controlli per la visita. *Gratis.*", "secs": 2.6, "theme": "orange"},
    ]
    numbered = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    caption = f"{intro}\n\n{numbered}\n\nIl limite del controllo: {limit}\n\n{LINK}\n\n{TAGS_VISIT}"
    return {"id": f"r-check-{n:02d}", "type": "reel", "channel": "ig-it", "at": at(day, "08:00"),
            "slug": f"controllo-{slug}", "theme": theme, "series": f"Prima di firmare · {n:02d}",
            "cards": cards, "caption": caption}


def myth(n, day, slug, theme, hook, claim, answer, source, intro):
    cards = [
        {"kind": "hook", "text": hook, "sub": "Cosa dice la ricerca.", "secs": 2.6},
        {"kind": "answer", "text": answer, "source": f"Fonte: {source}", "secs": 5.0, "theme": "night"},
        {"kind": "cta", "text": "Cosa cambia il prezzo e cosa no: *nell'app.*", "secs": 2.6, "theme": "violet"},
    ]
    caption = f"{intro}\n\n«{claim}»\n{answer}\n\nFonte: {source}.\n\nIn Nesso, la sezione Prepara mette in fila cosa la ricerca ha misurato sul prezzo e cosa cambia solo la visita. Link in bio.\n\n{TAGS_SELL}"
    return {"id": f"r-myth-{n:02d}", "type": "reel", "channel": "ig-it", "at": at(day, "13:00"),
            "slug": f"mito-{slug}", "theme": "orange", "series": f"Mito o no · {n:02d}",
            "cards": cards, "caption": caption}


def video(day, time, slug, name, caption):
    return {"id": f"r-app-{slug}", "type": "reel", "channel": "ig-it", "at": at(day, time),
            "slug": f"app-{slug}", "video": VID + name, "caption": caption}


def screen_story(day, slug, mock):
    return {"id": f"s-screen-{slug}", "type": "story", "channel": "ig-it", "at": at(day, "09:30"),
            "slug": f"storia-schermo-{slug}", "screen": MOCK + mock}


def card_story(day, time, slug, theme, card, series=None):
    return {"id": f"s-{slug}", "type": "story", "channel": "ig-it", "at": at(day, time),
            "slug": f"storia-{slug}", "theme": theme, "series": series, "card": card}


def tomorrow(day, slug, theme, text):
    return card_story(day, "21:30", f"domani-{slug}", "violet",
                      {"kind": "fact", "label": "DOMANI ALLE 8", "text": text, "sub": "Prima di firmare, un controllo al giorno."})


ITEMS = [
    # ---------------------------------------------------------------- Monday 2
    check(1, 2, "luce-radente", "orange",
          "Questo muro è stato *rifatto*?", "Te lo dice la torcia del telefono.",
          ["Accendi la torcia.", "Tieni il telefono piatto sul muro, obiettivo lungo la parete.", "Fai scorrere il fascio da un angolo all'altro."],
          "Non dice cosa c'è dietro il muro. Un muro piano può nascondere quanto uno ondulato.",
          "Con la luce della stanza i muri sembrano tutti uguali. Con la luce radente no: dove una parete è stata stuccata o rifatta, l'ombra lo fa vedere."),
    {"id": "r-cost-01", "type": "reel", "channel": "ig-it", "at": at(2, "13:00"), "slug": "costi-300mila",
     "theme": "orange", "series": "Quanto costa · 01", "cards": [
        {"kind": "hook", "text": "Casa da €300.000.\nQuanto paghi *davvero*?", "sub": "Prima casa, da un privato.", "secs": 2.6},
        {"kind": "big", "over": "Imposta di registro (rendita €800)", "text": "€1.848", "sub": "2% sul valore catastale, non sul prezzo.", "secs": 3.0},
        {"kind": "big", "over": "Ipotecaria e catastale", "text": "€100", "sub": "€50 ciascuna.", "secs": 2.2},
        {"kind": "big", "over": "Agenzia al 3%", "text": "€10.980", "sub": "€9.000 più IVA al 22%.", "secs": 2.8},
        {"kind": "big", "over": "Imposta sul mutuo di €240.000", "text": "€600", "sub": "0,25% sulla prima casa.", "secs": 2.6},
        {"kind": "big", "over": "In più del prezzo", "text": "€13.528", "sub": "E mancano notaio, banca e assicurazione.", "secs": 3.4},
        {"kind": "cta", "text": "Fai il conto sul tuo prezzo.", "button": "Calcolatore gratis · link in bio", "secs": 2.8},
     ],
     "caption": "Il prezzo dell'annuncio non è quello che paghi.\n\nEsempio con le regole nazionali: €300.000 da un privato, prima casa, rendita catastale €800, agenzia al 3%, mutuo di €240.000.\nRegistro €1.848, ipotecaria e catastale €100, agenzia €10.980, imposta sul mutuo €600.\nTotale €13.528, prima di notaio, banca e assicurazione.\n\nIl calcolo sul tuo prezzo, gratis e senza registrazione: link in bio.\nÈ un calcolo sulle regole nazionali, non una consulenza: il notaio conferma ogni riga.\n\n" + TAGS_COST},
    video(2, "20:00", "rumore", "rumore.mp4",
          "Alla visita la finestra è quasi sempre chiusa. Aprila.\n\n30 secondi a finestra aperta, 30 a finestra chiusa, telefono fermo nello stesso punto. Conta la differenza tra le due: la cifra assoluta dipende dal telefono, la differenza no.\n\nNesso fa la misura e ti dice anche cosa non può stabilire: non è un fonometro tarato. Link in bio.\n\n#cercocasa #affittomilano #visitacasa #casa #Milano"),
    screen_story(2, "dentro", "06-dentro-property-check.png"),
    card_story(2, "15:30", "fatto-registro", "orange",
               {"kind": "fact", "label": "LO SAPEVI?", "text": "Se compri da un privato, l'imposta di registro può partire dal *valore catastale*, non dal prezzo.",
                "sub": "Con una rendita di €800 sulla prima casa: €1.848 invece di €6.000 su €300.000.", "source": "DPR 131/1986 · L. 266/2005"}),
    tomorrow(2, "foglio", "violet", "La finestra chiude davvero? Serve un *foglio di carta*."),

    # ---------------------------------------------------------------- Tuesday 3
    check(2, 3, "foglio", "violet",
          "La finestra chiude *davvero*?", "Serve un foglio di carta.",
          ["Chiudi un foglio di carta nella finestra.", "Tiralo fuori: sopra, sotto, ai due lati.", "Segna dove scivola via facilmente."],
          "Dice dove l'anta non preme. Niente sul vetro.",
          "La guarnizione di una finestra si controlla in un minuto, con un foglio di carta."),
    myth(1, 3, "caffe", "orange",
         "Il profumo di caffè fa *vendere* casa a più?",
         "Il profumo di caffè fa vendere a più.",
         "Il profumo migliora l'umore nei negozi. Nessuno studio mostra un prezzo più alto per una casa.",
         "meta-analisi di 55 articoli sul profumo d'ambiente in negozi e hotel",
         "Lo dicono tutti, lo consigliano molti. Abbiamo cercato le prove."),
    video(3, "20:00", "costi", "costi.mp4",
          "Imposte, agenzia e mutuo oltre al prezzo, in una schermata sola.\n\nScrivi il prezzo, scegli se compri da un privato o da un costruttore, aggiungi la rendita catastale: Nesso fa il conto voce per voce con la norma accanto. Il notaio non lo calcoliamo: nessuna legge fissa il suo onorario.\n\nGratis, link in bio.\n\n" + TAGS_COST),
    screen_story(3, "rumore", "07-misura-rumore-finestra.png"),
    card_story(3, "15:30", "fatto-caffe", "orange",
               {"kind": "fact", "label": "PRIMA DI VENDERE", "text": "Il caffè in forno alza il prezzo? *Nessuno studio* lo mostra.", "sub": "Il profumo migliora l'umore nei negozi. Sulle case non è stato misurato."}),
    tomorrow(3, "spifferi", "violet", "C'è uno spiffero? Lo senti con il *dorso della mano*."),

    # ---------------------------------------------------------------- Wednesday 4
    check(3, 4, "spifferi", "violet",
          "C'è uno *spiffero*?", "Lo senti con il dorso della mano.",
          ["Chiudi la finestra.", "Passa il dorso della mano lungo il telaio.", "Senti se c'è aria che si muove."],
          "Vale per il vento di quel giorno. Una giornata ferma nasconde uno spiffero.",
          "Una finestra chiusa può far passare aria lungo il telaio. Si sente con la mano, su ogni finestra."),
    {"id": "r-cost-02", "type": "reel", "channel": "ig-it", "at": at(4, "13:00"), "slug": "costi-registro",
     "theme": "orange", "series": "Quanto costa · 02", "cards": [
        {"kind": "hook", "text": "Il registro si paga *sul prezzo*?", "sub": "Se compri da un privato, spesso no.", "secs": 2.6},
        {"kind": "fact", "label": "PRIMA CASA, DA UN PRIVATO", "text": "2% della base imponibile.", "sub": "Mai meno di €1.000.", "secs": 2.8},
        {"kind": "fact", "label": "SE COMPRI COME PERSONA FISICA", "text": "La base può essere il *valore catastale*.", "sub": "Rendita × 1,05 × 110 sulla prima casa. Si chiede in atto.", "secs": 3.6},
        {"kind": "big", "over": "Rendita €800, casa da €300.000", "text": "€1.848", "sub": "invece di €6.000.", "secs": 3.0},
        {"kind": "note", "label": "Da sapere", "text": "Nell'atto si dichiara comunque il prezzo intero. Il notaio conferma ogni riga.", "secs": 3.2},
        {"kind": "cta", "text": "Fai il conto con la tua rendita.", "button": "Link in bio", "secs": 2.6},
     ],
     "caption": "Il registro su una prima casa comprata da un privato è il 2% della base imponibile, mai meno di €1.000. E la base, se compri come persona fisica, può essere il valore catastale: rendita × 1,05 × 110.\n\nCon una rendita di €800: €1.848 invece di €6.000 su un prezzo di €300.000.\n\nLa rendita la trovi nella visura catastale. Il calcolo con la tua è gratis: link in bio.\nDPR 131/1986, L. 266/2005. È un calcolo, non una consulenza.\n\n" + TAGS_COST},
    video(4, "20:00", "pavimento", "pavimento.mp4",
          "Il pavimento è in piano? Appoggia il telefono a terra a metà stanza, leggi, giralo di mezzo giro e leggi di nuovo. Nesso toglie l'errore del telefono e ti dà la pendenza.\n\nCosa non ti dice: cosa c'è sotto. Gli edifici vecchi sono raramente in piano, e una pendenza da sola non è un accertamento.\n\nLink in bio.\n\n" + TAGS_VISIT),
    screen_story(4, "pavimento", "08-misura-pavimento.png"),
    card_story(4, "15:30", "fatto-caparra", "violet",
               {"kind": "fact", "label": "UNA REGOLA SOLA", "text": "Nessuna caparra prima di aver visto la casa *di persona*.", "sub": "Né per un affitto, né per un acquisto."}),
    tomorrow(4, "umidita", "violet", "Dove si nasconde l'umidità? *Tre posti* da guardare."),

    # ---------------------------------------------------------------- Thursday 5
    check(4, 5, "umidita", "violet",
          "Dove si nasconde l'*umidità*?", "Tre posti da guardare.",
          ["Cammina lungo la base dei muri esterni.", "Guarda dietro i mobili e negli angoli.", "Cerca macchie, bolle o vernice che si stacca."],
          "Una macchia può essere vecchia e asciutta. Un muro pulito può essere bagnato.",
          "L'umidità raramente è al centro della parete. Sta in basso, negli angoli e dove i mobili coprono il muro."),
    myth(2, 5, "staging", "violet",
         "L'home staging *alza* il prezzo?",
         "L'home staging alza il prezzo.",
         "Nell'esperimento che abbiamo trovato l'allestimento cambiava quanto la casa sembrava vivibile ai proprietari, non quanto dicevano valesse.",
         "Lane, Seiler e Seiler, l'effetto dell'allestimento sulla domanda di case",
         "L'home staging è un mestiere vero. Quello che abbiamo cercato è se alza il prezzo."),
    video(5, "20:00", "quiz", "quiz.mp4",
          "Cinque domande e Nesso ti dice che abitante sei, con il tuo sticker, e quale quartiere ti somiglia di più nella tua città.\n\nI quartieri sono letti con dati pubblicati: negozi, parchi, scuole, minuti a piedi. Gratis, link in bio.\n\n#quartiere #Milano #Torino #cercocasa #casa"),
    screen_story(5, "quiz", "02b-quiz-sticker.png"),
    card_story(5, "15:30", "fatto-staging", "violet",
               {"kind": "fact", "label": "PRIMA DI VENDERE", "text": "Cosa alza il prezzo, secondo la ricerca?", "sub": "Classe energetica, luce, silenzio, un terrazzo. In Nesso, sezione Prepara."}),
    tomorrow(5, "pressione", "violet", "L'acqua arriva con forza? Apri *due rubinetti* insieme."),

    # ---------------------------------------------------------------- Friday 6
    check(5, 6, "pressione", "violet",
          "L'acqua arriva *con forza*?", "Apri due rubinetti insieme.",
          ["Apri del tutto il rubinetto della cucina.", "Accendi anche la doccia.", "Guarda il getto in cucina."],
          "La pressione cambia nell'arco della giornata e da un piano all'altro.",
          "Con un rubinetto solo quasi tutte le case sembrano a posto. Il problema si vede quando l'acqua serve in due punti."),
    {"id": "r-cost-03", "type": "reel", "channel": "ig-it", "at": at(6, "13:00"), "slug": "costi-agenzia",
     "theme": "orange", "series": "Quanto costa · 03", "cards": [
        {"kind": "hook", "text": "La provvigione dell'agenzia ha *l'IVA*?", "secs": 2.4},
        {"kind": "fact", "text": "Sì, al 22%.", "sub": "La provvigione di solito è dal 2% al 4% per ciascuna parte, secondo la provincia. Si concorda nell'incarico.", "secs": 3.6},
        {"kind": "big", "over": "Su €300.000, al 3%", "text": "€10.980", "sub": "€9.000 più €1.980 di IVA.", "secs": 3.0},
        {"kind": "fact", "label": "PRIMA CASA", "text": "Puoi detrarre dall'IRPEF il 19% della provvigione, fino a €1.000.", "sub": "Nell'anno in cui la paghi.", "secs": 3.6},
        {"kind": "cta", "text": "Tutte le voci, sul tuo prezzo.", "button": "Link in bio", "secs": 2.6},
     ],
     "caption": "La provvigione dell'agenzia ha l'IVA al 22%. Su una casa da €300.000 con provvigione al 3%: €9.000 più €1.980.\n\nSulla prima casa puoi detrarre dall'IRPEF il 19% della provvigione, fino a €1.000, nell'anno in cui la paghi.\n\nIl calcolo con la tua percentuale: link in bio. DPR 633/1972, DPR 917/1986. È un calcolo, non una consulenza.\n\n" + TAGS_COST},
    video(6, "20:00", "mappa", "mappa.mp4",
          "Prima della casa, il quartiere. Nesso mostra i quartieri della tua città con dati pubblicati: minuti a piedi da scuola, negozi e parco, e una personalità per ogni zona.\n\nDieci città italiane. Le personalità dei quartieri sono gratis. Link in bio.\n\n#quartiere #Milano #Roma #Torino #cercocasa"),
    screen_story(6, "investimento", "03-investimento-mappa.png"),
    card_story(6, "15:30", "fatto-iva", "orange",
               {"kind": "fact", "label": "LO SAPEVI?", "text": "La provvigione dell'agenzia ha l'IVA al *22%*.", "sub": "Al 3% su €300.000: €9.000 più €1.980."}),
    tomorrow(6, "luce", "orange", "Quanta luce arriva *in fondo* alla stanza?"),

    # ---------------------------------------------------------------- Saturday 7
    check(6, 7, "luce", "orange",
          "Quanta luce arriva *in fondo* alla stanza?", "Tre letture, un minuto.",
          ["Spegni le luci della stanza.", "Leggi sul davanzale, a metà stanza e sulla parete di fondo.", "Tieni il telefono in piano, schermo in su."],
          "Dipende dal cielo di quel minuto. Una nuvola che passa la dimezza.",
          "Vicino alla finestra ogni stanza è luminosa. La parete di fondo è dove metterai la scrivania."),
    myth(3, 7, "musica", "violet",
         "La musica classica fa *offrire* di più?",
         "La musica classica fa offrire di più.",
         "La musica influenza un po' chi fa acquisti. Nessuno studio sulle case ha trovato offerte più alte.",
         "meta-analisi di 32 studi nei negozi sulla musica di sottofondo",
         "Il consiglio arriva dai negozi. Nelle case nessuno l'ha misurato."),
    video(7, "20:00", "prepara", "prepara.mp4",
          "Vendi o affitti casa? Prepara è la parte di Nesso per chi la mostra: ogni consiglio dice se la ricerca lo ha visto nel prezzo o se cambia solo la visita.\n\nRispondi a ogni carta e vedi cosa fare per primo. Link in bio.\n\n" + TAGS_SELL),
    screen_story(7, "prepara", "05-prepara.png"),
    card_story(7, "15:30", "fatto-luce", "orange",
               {"kind": "fact", "label": "IN VISITA", "text": "Misura la luce sulla *parete di fondo*, non sul davanzale.", "sub": "È lì che leggerai e lavorerai."}),
    tomorrow(7, "lavello", "violet", "Hai mai aperto il mobile *sotto il lavello*?"),

    # ---------------------------------------------------------------- Sunday 8
    check(7, 8, "lavello", "violet",
          "Hai aperto il mobile *sotto il lavello*?", "Trenta secondi, una torcia.",
          ["Apri il mobile sotto ogni lavello.", "Torcia accesa, guarda ogni giunzione.", "Passa un dito lungo ognuna."],
          "Trova la traccia di acqua passata. Non dice se perde ancora.",
          "In visita nessuno apre i mobili. È lì che una perdita lascia il segno."),
    myth(4, 8, "stanza-vuota", "orange",
         "Una stanza vuota sembra *più grande*?",
         "Una stanza vuota sembra sempre più grande.",
         "I mobili facevano sembrare le stanze un po' più piccole in un test, e nessuna differenza in VR.",
         "arredamento e spazio percepito, in un modello e in VR",
         "Svuotare tutto prima delle foto? La ricerca dice qualcosa di più preciso."),
    {"id": "r-cost-04", "type": "reel", "channel": "ig-it", "at": at(8, "20:00"), "slug": "costi-notaio",
     "theme": "violet", "series": "Quanto costa · 04", "cards": [
        {"kind": "hook", "text": "Quanto costa *il notaio*?", "secs": 2.2},
        {"kind": "fact", "text": "Nessuna norma nazionale fissa il suo onorario.", "sub": "Per questo non te lo calcoliamo.", "secs": 3.0},
        {"kind": "fact", "label": "COSA FARE", "text": "Chiedi un preventivo scritto prima del preliminare.", "sub": "A più di un notaio.", "secs": 3.0},
        {"kind": "fact", "label": "VALE ANCHE PER", "text": "Istruttoria e perizia della banca, e l'assicurazione del mutuo.", "sub": "Sono nel PIES, che la banca ti deve dare gratis.", "secs": 3.6},
        {"kind": "cta", "text": "Il resto delle spese lo calcoliamo noi.", "button": "Link in bio", "secs": 2.6},
     ],
     "caption": "Quanto costa il notaio? Nessuna norma nazionale fissa il suo onorario, quindi un numero unico non esiste. Chiedi un preventivo scritto prima del preliminare, e chiedilo a più di un notaio.\n\nImposte, agenzia e imposta sul mutuo invece hanno regole precise: le calcola Nesso, gratis. Link in bio.\n\n" + TAGS_COST},
    screen_story(8, "vivi", "02-vivi-mappa.png"),
    card_story(8, "15:30", "fatto-notaio", "violet",
               {"kind": "fact", "label": "PRIMA DEL PRELIMINARE", "text": "Chiedi al notaio un *preventivo scritto*.", "sub": "Nessuna norma nazionale fissa il suo onorario."}),
    card_story(8, "21:30", "checklist", "violet",
               {"kind": "cta", "text": "82 controlli per la prossima visita.", "button": "Link in bio"}, series="Prima di firmare"),
]

# Cost Reels: orange, with the total and the ending on violet so the last seconds change colour.
for _item in ITEMS:
    if _item["id"].startswith("r-cost-"):
        _item["cards"][-1]["theme"] = "violet"
        if _item["cards"][-2]["kind"] == "big":
            _item["cards"][-2]["theme"] = "night"
