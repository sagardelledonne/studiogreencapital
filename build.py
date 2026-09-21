# -*- coding: utf-8 -*-
"""Genera il sito di Studio Green Capital (HTML statico) a partire dai testi qui sotto.
Uso:  python build.py     -> scrive index.html e le cartelle delle pagine interne.
Pubblicazione: commit + push su main (GitHub Pages fa il resto).
Con il dominio proprio (studiogreencapital.it) mettere BASE = "" e rigenerare.
"""
import os, re

BASE = "/studiogreencapital"          # prefisso degli indirizzi su GitHub Pages; "" con il dominio proprio
SITE_URL = "https://sagardelledonne.github.io" + BASE
IMG = BASE + "/assets/img"
CONTACT_EMAIL = "info@studiogreencapital.it"
ROOT = os.path.dirname(os.path.abspath(__file__))
import time
V = "?v=%d" % int(time.time())

# ------------------------------------------------------------------ icone svg
ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-down" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 12.5l2.6 2.5L16 9.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-no" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M9 9l6 6M15 9l-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></symbol>
<symbol id="i-contract" viewBox="0 0 24 24"><path d="M7 3h7l5 5v13H7z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M14 3v5h5M10 13h6M10 17h6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol>
<symbol id="i-ppa" viewBox="0 0 24 24"><path d="M4 17l5-6 4 4 7-9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 21h16" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol>
<symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></symbol>
<symbol id="i-leaf" viewBox="0 0 24 24"><path d="M5 19c0-8 5-14 15-14-1 9-6 14-15 14z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M5 19c3-5 7-9 12-11" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol>
<symbol id="i-people" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3 20c0-3.5 2.7-6 6-6s6 2.5 6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="17" cy="9" r="2.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M16 14.5c2.8 0 5 2 5 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol>
<symbol id="i-chat" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></symbol>
</defs></svg>"""

MARK = """<svg class="mark" viewBox="0 0 40 40" aria-hidden="true"><rect x="1" y="1" width="38" height="38" rx="11" fill="none" stroke="currentColor" stroke-opacity=".35" stroke-width="1.2"/><path d="M11 29c0-9 6.5-16 18-16-1 10-7.5 16-18 16z" fill="#B08A45"/><path d="M11 29c3.5-5.5 8-10 13.5-12.5" fill="none" stroke="#0A1B14" stroke-width="1.4" stroke-linecap="round" stroke-opacity=".8"/></svg>"""

def ico(name):
    return '<svg aria-hidden="true"><use href="#%s"/></svg>' % name

def arrow():
    return ico("i-arrow")

# ------------------------------------------------------------------ servizi (usati in menu, home, pagina servizi e pagine singole)
SERVICES = [
    dict(slug="supply-procurement", n="01", title="Supply &amp; Procurement", short="Contratti e strategia di acquisto", icon="i-contract", img="firma",
         teaser="Struttura contrattuale, momento di acquisto, negoziazione. Il prezzo dell’energia è una decisione, non una fortuna.",
         lede="Il contratto di fornitura è la prima leva sul costo dell’energia, e quasi sempre la meno governata. Lo trasformiamo in una scelta consapevole: quale struttura, quando fissare, con chi.",
         problem="La maggior parte delle imprese rinnova la fornitura a ridosso della scadenza, confrontando due o tre offerte su un prezzo che nel frattempo è già cambiato. Il contratto resta una casella da spuntare, con clausole poco lette e un’esposizione al mercato che nessuno ha scelto davvero.",
         answer="Trattiamo l’acquisto dell’energia come una decisione finanziaria. Analizziamo il profilo di prelievo, costruiamo la struttura contrattuale più adatta (fisso, indicizzato, a tranche, mix), scegliamo il momento in base al mercato e gestiamo la gara tra i fornitori. Voi firmate un contratto che avete capito e voluto.",
         do=["Analisi del profilo di consumo e della struttura di costo attuale", "Definizione della strategia: prodotto, orizzonte, quota fissata", "Gara tra fornitori qualificati e negoziazione delle clausole", "Presidio delle finestre di fissazione del prezzo durante l’anno", "Verifica delle fatture e recupero di eventuali errori"],
         get=[("Prezzo migliore", "Condizioni ottenute confrontando il mercato nel momento giusto, non solo a scadenza."), ("Rischio scelto", "Un’esposizione alla volatilità decisa a tavolino, coerente con i vostri margini."), ("Zero sorprese", "Clausole chiare, fatture controllate, nessun costo nascosto.")],
         who="Imprese con una spesa energetica significativa — indicativamente da 200.000 € l’anno — che oggi gestiscono la fornitura in modo reattivo."),
    dict(slug="ppa", n="02", title="PPA — Power Purchase Agreement", short="Accordi pluriennali con produttori rinnovabili", icon="i-ppa", img="fiume",
         teaser="Un prezzo stabile per anni, energia rinnovabile certificata, rischio sotto controllo. Senza costruire nulla.",
         lede="Un PPA è un contratto pluriennale con cui un’impresa acquista energia direttamente da un produttore rinnovabile, a un prezzo concordato. È lo strumento più efficace per proteggersi dalla volatilità: se è strutturato bene.",
         problem="I PPA sono contratti complessi: durata, profilo di consegna, garanzie, indicizzazioni, clausole di uscita. Firmarne uno sbagliato significa bloccare per dieci anni una condizione sfavorevole. Per questo molte imprese vi rinunciano, restando esposte al mercato.",
         answer="Vi affianchiamo dall’analisi di fattibilità alla firma: quanta energia coprire con un PPA, con quale profilo, a quale prezzo obiettivo. Selezioniamo le controparti, strutturiamo l’accordo e negoziamo ogni clausola nel vostro interesse. Il risultato è un contratto che regge nel tempo, non solo sulla carta.",
         do=["Analisi del fabbisogno e della quota ottimale da coprire con PPA", "Selezione dei produttori e delle strutture contrattuali (fisico, virtuale, sleeved)", "Modellazione degli scenari di prezzo e del rischio residuo", "Negoziazione di prezzo, durata, garanzie e clausole di flessibilità", "Integrazione del PPA con la strategia di approvvigionamento complessiva"],
         get=[("Prezzo prevedibile", "Una quota rilevante della spesa energetica fissata per anni, fuori dalla volatilità."), ("Energia certificata", "Garanzie d’origine e tracciabilità per obiettivi ESG e reportistica."), ("Nessun capitale immobilizzato", "I benefici della produzione rinnovabile senza costruire né gestire impianti.")],
         who="Imprese e gruppi con consumi rilevanti e continuativi — dai 5 GWh l’anno — che vogliono stabilizzare il costo energetico su un orizzonte pluriennale."),
    dict(slug="produzione-autoconsumo", n="03", title="Produzione &amp; Autoconsumo", short="Fotovoltaico e soluzioni termiche", icon="i-sun", img="fotovoltaico",
         teaser="Impianti dimensionati sul profilo reale di consumo e valutati come investimento, non come acquisto.",
         lede="Produrre parte della propria energia è la forma più diretta di indipendenza. Ma un impianto è un investimento ventennale: va progettato sui numeri dell’azienda, non sul preventivo dell’installatore.",
         problem="Il mercato del fotovoltaico industriale è fatto di offerte “chiavi in mano” costruite per vendere potenza, non per massimizzare il ritorno. Sovradimensionamenti, autoconsumo sovrastimato, incentivi promessi e non verificati: il rischio è un investimento che rende meno del previsto.",
         answer="Partiamo dal profilo orario di consumo e costruiamo il caso economico: potenza ottimale, quota di autoconsumo reale, costo dell’energia prodotta, tempo di rientro. Valutiamo le formule (acquisto, leasing, PPA on-site, comunità energetiche), gestiamo la gara tra installatori qualificati e seguiamo la realizzazione. Siamo dalla vostra parte del tavolo.",
         do=["Studio di fattibilità tecnico-economico basato sui dati reali di consumo", "Dimensionamento ottimale e valutazione di accumulo e soluzioni termiche", "Analisi delle formule di finanziamento e degli incentivi disponibili", "Gara tra installatori e verifica indipendente delle offerte", "Supervisione di realizzazione, collaudo e prestazioni nel tempo"],
         get=[("Energia a costo più basso", "L’energia autoprodotta costa meno di quella acquistata: per vent’anni."), ("Investimento verificato", "Un piano economico realistico, costruito prima di firmare qualsiasi contratto."), ("Indipendenza", "Meno esposizione al mercato, più controllo sul proprio costo industriale.")],
         who="Imprese con superfici disponibili (coperture, aree, parcheggi) e consumi diurni significativi; realtà che stanno già valutando offerte di installatori."),
    dict(slug="efficienza-energetica", n="04", title="Efficienza Energetica", short="Consumare meno, prima di pagare meno", icon="i-leaf", img="bosco",
         teaser="Audit, interventi mirati e ottimizzazione dei processi energivori. Il kilowattora più economico è quello che non si consuma.",
         lede="Prima di negoziare il prezzo dell’energia, vale la pena chiedersi quanta se ne stia usando senza bisogno. L’efficienza è la leva meno visibile e spesso quella con il ritorno più rapido.",
         problem="Molte imprese non sanno davvero dove va la loro energia: quali reparti, quali macchine, in quali orari. Senza questa mappa gli interventi di efficienza restano sporadici, guidati dai fornitori di tecnologia più che da una priorità economica.",
         answer="Costruiamo la mappa dei consumi, individuiamo gli sprechi e ordiniamo gli interventi per ritorno economico: dai più semplici (orari, regolazioni, manutenzione) ai più strutturali (motori, aria compressa, illuminazione, recupero termico). Verifichiamo gli incentivi disponibili e misuriamo i risultati.",
         do=["Diagnosi energetica e monitoraggio dei consumi per centro di costo", "Individuazione e valutazione economica degli interventi", "Piano di intervento ordinato per priorità e tempo di rientro", "Accesso agli incentivi e agli strumenti di finanziamento", "Misura e verifica dei risparmi ottenuti"],
         get=[("Consumi ridotti", "Meno energia acquistata, in modo strutturale e misurabile."), ("Priorità chiare", "Un piano di interventi ordinato per ritorno economico, non per catalogo."), ("Risparmi documentati", "Risultati misurati e certificabili, utili anche per i bilanci di sostenibilità.")],
         who="Realtà produttive e logistiche con processi energivori; imprese soggette a diagnosi energetica obbligatoria che vogliono trasformarla in valore."),
    dict(slug="welfare-energetico", n="05", title="Welfare Energetico", short="Convenzioni energetiche per i dipendenti", icon="i-people", img="germoglio",
         teaser="Condizioni di fornitura vantaggiose per le famiglie dei collaboratori: un benefit concreto, a costo zero per l’azienda.",
         lede="L’energia pesa anche sui bilanci familiari dei vostri collaboratori. Con il welfare energetico l’impresa mette a disposizione delle persone la stessa competenza che usa per sé.",
         problem="Le famiglie affrontano il mercato dell’energia da sole, tra offerte poco trasparenti e prezzi che cambiano di continuo. Un’azienda che vuole offrire benefit concreti spesso non ha uno strumento semplice per intervenire su questa voce di spesa.",
         answer="Strutturiamo convenzioni dedicate ai dipendenti con fornitori selezionati, a condizioni negoziate collettivamente, e curiamo la comunicazione interna e l’assistenza nell’attivazione. L’azienda non sostiene costi né oneri amministrativi; le persone risparmiano su una spesa che sentono ogni mese.",
         do=["Selezione dei fornitori e negoziazione delle condizioni dedicate", "Materiali di comunicazione interna e sportello informativo", "Assistenza ai dipendenti nell’attivazione e nel passaggio", "Monitoraggio periodico della convenzione e rinegoziazione"],
         get=[("Benefit tangibile", "Un vantaggio economico che le persone vedono in bolletta ogni mese."), ("Zero costi", "Nessun esborso né carico amministrativo per l’azienda."), ("Coerenza", "Un segnale concreto di attenzione alle persone e al tema dell’energia.")],
         who="Imprese di ogni dimensione che vogliono arricchire il piano welfare con un benefit semplice da attivare e apprezzato."),
]
def surl(s): return BASE + "/servizi/" + s["slug"] + "/"

# ------------------------------------------------------------------ navigazione
NAV = [
    ("Chi siamo", BASE + "/chi-siamo/", []),
    ("Servizi", BASE + "/servizi/", [(s["title"], surl(s), s["short"]) for s in SERVICES]),
    ("Metodo", BASE + "/metodo/", []),
    ("Risultati", BASE + "/risultati/", []),
    ("Contatti", BASE + "/contatti/", []),
]

def brand(tag="a"):
    return '<%s class="brand" href="%s/" aria-label="Studio Green Capital — home">%s<span><b>Studio Green Capital</b><small>Strategic Energy Advisory</small></span></%s>' % (tag, BASE, MARK, tag)

def header(path):
    items = []
    for label, href, sub in NAV:
        cur = ' aria-current="page"' if path == href or (sub and path.startswith(href)) else ""
        if sub:
            dd = "".join('<a href="%s">%s<span>%s</span></a>' % (h, l, d) for l, h, d in sub)
            items.append('<div><a href="%s"%s>%s %s</a><div class="dd">%s</div></div>' % (href, cur, label, ico("i-down"), dd))
        else:
            items.append('<div><a href="%s"%s>%s</a></div>' % (href, cur, label))
    mob = []
    for label, href, sub in NAV:
        mob.append('<a href="%s">%s %s</a>' % (href, label, arrow()))
        if sub:
            mob.append('<div class="sub">' + "".join('<a href="%s">%s</a>' % (h, l) for l, h, d in sub) + '</div>')
    return """
<header class="top" id="top"><div class="wrap">
  %s
  <nav class="nav" aria-label="Principale">%s</nav>
  <div class="top-cta">
    <a class="btn btn-brass" href="%s/contatti/">Richiedi una valutazione</a>
    <button class="burger" id="burger" aria-label="Apri il menu" aria-expanded="false" aria-controls="menu">%s</button>
  </div>
</div></header>
<div class="menu" id="menu" aria-label="Menu">
  <div class="mhead">%s<button class="close" id="menuClose" aria-label="Chiudi il menu">%s</button></div>
  <nav>%s</nav>
  <p class="mfoot">Studio Green Capital SRL · Strategic Energy Advisory<br><a href="mailto:%s">%s</a></p>
</div>
""" % (brand(), "".join(items), BASE, ico("i-menu"), brand("span"), ico("i-x"), "".join(mob), CONTACT_EMAIL, CONTACT_EMAIL)

def footer():
    srv = "".join('<a href="%s">%s</a>' % (surl(s), s["title"]) for s in SERVICES)
    return """
<footer class="foot"><div class="wrap">
  <div class="cols">
    <div>%s<p>Società di consulenza energetica indipendente per imprese e realtà industriali. Contratti, approvvigionamento, produzione propria: un solo interlocutore, remunerato sui risultati.</p></div>
    <div><h4>Studio</h4><nav><a href="%(b)s/chi-siamo/">Chi siamo</a><a href="%(b)s/metodo/">Il metodo</a><a href="%(b)s/risultati/">Risultati</a><a href="%(b)s/contatti/">Contatti</a></nav></div>
    <div><h4>Servizi</h4><nav>%(s)s</nav></div>
    <div><h4>Contatti</h4><nav><a href="mailto:%(m)s">%(m)s</a><a href="%(b)s/contatti/">Richiedi una valutazione</a></nav></div>
  </div>
  <div class="legal">
    <span>© <span id="year">2026</span> Studio Green Capital SRL · Tutti i diritti riservati</span>
    <nav><a href="%(b)s/privacy/">Privacy</a><a href="%(b)s/cookie/">Cookie</a></nav>
  </div>
</div></footer>
""".replace("%s", brand(), 1) % {"b": BASE, "s": srv, "m": CONTACT_EMAIL}

# ------------------------------------------------------------------ pagina
def page(path, title, desc, body, light=False):
    """path: indirizzo (es. '/chi-siamo/'). Scrive index.html nella cartella corrispondente."""
    full = BASE + path
    canon = SITE_URL + path
    og_img = SITE_URL + "/assets/img/bosco.webp"
    cls = ' class="on-light"' if light else ""
    html = """<!DOCTYPE html>
<html lang="it"%s>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta property="og:type" content="website"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:image" content="%s"><meta property="og:locale" content="it_IT">
<meta name="theme-color" content="#0F2A1F">
<link rel="icon" href="%s/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="%s/assets/fonts/fraunces-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="%s/assets/fonts/manrope-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="%s/assets/fonts/fonts.css">
<link rel="stylesheet" href="%s/assets/site.css%s">
</head>
<body>
%s
%s
<main id="main">
%s
</main>
%s
<script src="%s/assets/site.js%s" defer></script>
</body>
</html>
""" % (cls, title, desc, canon, title, desc, og_img, BASE, BASE, BASE, BASE, BASE, V, ICONS, header(full), body, footer(), BASE, V)
    out = os.path.join(ROOT, *[p for p in path.split("/") if p])
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return path

# ------------------------------------------------------------------ componenti
def phero(eyebrow, h1, lede, crumbs=None, img=None):
    c = ""
    if crumbs:
        c = '<div class="crumbs">' + " / ".join('<a href="%s">%s</a>' % (h, l) if h else "<span>%s</span>" % l for l, h in crumbs) + "</div>"
    im = '<img class="bgimg" src="%s/%s.webp" alt="" loading="eager">' % (IMG, img) if img else ""
    return """<section class="phero dark%s">%s<div class="wrap">%s<p class="eyebrow rv in">%s</p><h1 class="rv in">%s</h1><p class="lede rv in rv-d1">%s</p></div></section>""" % (" has-img" if img else "", im, c, eyebrow, h1, lede)

def cta_band(h2, p, btn="Richiedi una valutazione", img="germoglio", second=None):
    s = '<a class="btn btn-ghost" href="%s">%s %s</a>' % (second[1], second[0], arrow()) if second else ""
    return """<section class="cta-band"><img src="%s/%s.webp" alt="" loading="lazy"><div class="wrap"><p class="eyebrow rv">Iniziamo</p><h2 class="rv">%s</h2><p class="lede rv rv-d1">%s</p><div class="actions rv rv-d2"><a class="btn btn-brass" href="%s/contatti/">%s %s</a>%s</div></div></section>""" % (IMG, img, h2, p, BASE, btn, arrow(), s)

def service_cards(with_cta=True):
    cards = []
    for i, s in enumerate(SERVICES):
        cards.append('<a class="card rv rv-d%d" href="%s"><span class="ico">%s</span><span class="n">%s</span><h3>%s</h3><p>%s</p><span class="link">Approfondisci %s</span></a>' % (i % 3 + 1, surl(s), ico(s["icon"]), s["n"], s["title"], s["teaser"], arrow()))
    if with_cta:
        cards.append('<a class="card cta rv rv-d3" href="%s/contatti/"><span class="ico">%s</span><h3>Non sapete da dove partire?</h3><p>Iniziamo da un’analisi preliminare del vostro profilo energetico: riservata, senza impegno, con numeri concreti.</p><span class="link">Richiedi una valutazione %s</span></a>' % (BASE, ico("i-chat"), arrow()))
    return '<div class="grid3">%s</div>' % "".join(cards)

STEPS = [
    ("Analizziamo", "Consumi, contratti, profilo orario, esposizione al mercato. Costruiamo la mappa energetica dell’impresa: un punto di partenza misurabile."),
    ("Strutturiamo", "Definiamo la strategia: quali leve, in che ordine, con quali obiettivi. Un piano con i numeri, non un elenco di buone intenzioni."),
    ("Eseguiamo", "Negoziamo, strutturiamo i contratti, seguiamo la realizzazione degli interventi. Al vostro fianco davanti a fornitori e controparti."),
    ("Presidiamo", "Monitoriamo i risultati e aggiorniamo la strategia quando il mercato cambia. L’energia si governa nel tempo, non una volta sola."),
]
def steps(light=False):
    return '<div class="steps%s">%s</div>' % (" light" if light else "", "".join('<div class="step rv rv-d%d"><span class="dot">0%d</span><h3>%s</h3><p>%s</p></div>' % (i + 1, i + 1, t, d) for i, (t, d) in enumerate(STEPS)))

def checks(items, x=False):
    return '<ul class="checks%s">%s</ul>' % (" x" if x else "", "".join('<li>%s<span>%s</span></li>' % (ico("i-no" if x else "i-check"), t) for t in items))

def pun_chart():
    """Grafico del prezzo medio annuo dell’elettricità in Italia (PUN, €/MWh)."""
    data = [(2016, 43), (2017, 54), (2018, 61), (2019, 52), (2020, 39), (2021, 125), (2022, 304), (2023, 127), (2024, 108), (2025, 110)]
    W, H, L, R, T, B = 900, 380, 56, 24, 30, 46
    ymax = 350
    def x(i): return L + i * (W - L - R) / (len(data) - 1)
    def y(v): return T + (H - T - B) * (1 - v / ymax)
    pts = [(x(i), y(v)) for i, (_, v) in enumerate(data)]
    path = "M" + " L".join("%.1f %.1f" % p for p in pts)
    area = path + " L%.1f %.1f L%.1f %.1f Z" % (pts[-1][0], y(0), pts[0][0], y(0))
    grid = "".join('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f"/><text class="lbl" x="%d" y="%.1f" text-anchor="end">%d</text>' % (L, W - R, y(v), y(v), L - 10, y(v) + 4, v) for v in range(0, ymax + 1, 50))
    xl = "".join('<text class="lbl" x="%.1f" y="%d" text-anchor="middle">%d</text>' % (x(i), H - 14, yr) for i, (yr, _) in enumerate(data))
    dots = "".join('<circle class="pt%s" cx="%.1f" cy="%.1f" r="%d"/>' % (" peak" if v == 304 else "", px, py, 6 if v == 304 else 4) for (px, py), (_, v) in zip(pts, data))
    vals = "".join('<text class="val" x="%.1f" y="%.1f" text-anchor="middle">%d</text>' % (px, py - 12, v) for (px, py), (_, v) in zip(pts, data) if v in (39, 304, 110))
    call = '<text class="call" x="%.1f" y="%.1f" text-anchor="end">×8 in ventiquattro mesi</text>' % (pts[6][0] - 16, pts[6][1] + 6)
    return """<svg class="chart" viewBox="0 0 %d %d" role="img" aria-label="Prezzo medio annuo dell’energia elettrica in Italia dal 2016 al 2025: da 39 euro al megawattora nel 2020 a 304 nel 2022">
<defs><linearGradient id="gArea" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#2E7A5A" stop-opacity=".28"/><stop offset="1" stop-color="#2E7A5A" stop-opacity="0"/></linearGradient></defs>
<g class="grid">%s</g>%s<path class="area" d="%s"/><path class="line" d="%s"/>%s%s%s</svg>""" % (W, H, grid, xl, area, path, dots, vals, call)

# ================================================================== HOME
def home():
    b = []
    b.append("""
<section class="hero">
  <div class="bg"><img src="%(i)s/bosco.webp" alt="" fetchpriority="high"></div><div class="veil"></div>
  <div class="wrap">
    <div>
      <p class="eyebrow rv in">Strategic Energy Advisory</p>
      <h1 class="rv in">L’energia non si subisce. <em>Si governa.</em></h1>
      <p class="lede rv in rv-d1">Affianchiamo imprese e gruppi industriali nelle decisioni che determinano il costo dell’energia: contratti, approvvigionamento, produzione propria. Un solo interlocutore, indipendente, remunerato sui risultati.</p>
      <div class="actions rv in rv-d2"><a class="btn btn-brass" href="%(b)s/contatti/">Richiedi una valutazione %(a)s</a><a class="btn btn-ghost" href="%(b)s/metodo/">Come lavoriamo</a></div>
    </div>
    <aside class="rv in rv-d3"><strong>Advisor, non fornitori.</strong>Nessun prodotto da vendere, nessuna provvigione dai fornitori. Il nostro interesse coincide con il vostro: un costo dell’energia più basso e più prevedibile.</aside>
  </div>
  <div class="scroll-hint" aria-hidden="true"></div>
</section>""" % {"i": IMG, "b": BASE, "a": arrow()})

    b.append("""
<section class="sec manifesto light"><div class="wrap">
  <div class="num rv" aria-hidden="true">01</div>
  <p class="quote rv rv-d1">Ogni impresa ha un commercialista e un consulente legale. <em>Quasi nessuna ha un partner per l’energia</em> — eppure è tra le prime voci di costo, e la più esposta al mercato.</p>
</div></section>""")

    b.append("""
<section class="stats"><div class="wrap">
  <div class="stat rv"><b data-count="25" data-prefix="10–" data-suffix="%">10–25%</b><p>di riduzione strutturale del costo energetico ottenibile con una strategia integrata</p></div>
  <div class="stat rv rv-d1"><b data-count="8" data-prefix="×">×8</b><p>la variazione del prezzo dell’elettricità in Italia in ventiquattro mesi, tra il 2020 e il 2022</p></div>
  <div class="stat rv rv-d2"><b data-count="75" data-suffix="%">75%</b><p>della bolletta dipende da materia prima e margine del fornitore: la parte su cui si può intervenire</p></div>
  <div class="stat rv rv-d3"><b>0</b><p>prodotti da vendere. Siamo advisor indipendenti, non fornitori né installatori</p></div>
</div></section>""")

    b.append("""
<section class="sec light"><div class="wrap">
  <div class="head rv"><p class="eyebrow">Cosa facciamo</p><h2>Un unico partner per l’intera <em>strategia energetica</em></h2><p class="lede">Dall’acquisto dell’energia alla produzione in proprio: interveniamo su ogni leva che determina il costo, il rischio e la prevedibilità della spesa.</p></div>
  %s
</div></section>""" % service_cards())

    b.append("""
<section class="sec dark"><div class="wrap">
  <div class="head rv"><p class="eyebrow">Il metodo</p><h2>Quattro fasi. Un processo che <em>non finisce con la firma.</em></h2></div>
  %s
  <p class="rv" style="margin-top:56px"><a class="link" href="%s/metodo/">Il metodo nel dettaglio %s</a></p>
</div></section>""" % (steps(), BASE, arrow()))

    b.append("""
<section class="sec light"><div class="wrap">
  <div class="split wide-r">
    <div class="sticky rv"><p class="eyebrow">Il contesto</p><h2>La volatilità non è un incidente. <em>È la normalità</em> del mercato.</h2><p class="lede" style="margin-top:20px">Prezzo medio annuo dell’energia elettrica all’ingrosso in Italia. Chi compra senza una strategia paga queste oscillazioni per intero, e le scopre in fattura.</p></div>
    <div class="rv rv-d1">
      <div class="chart-wrap">%s<p class="source">PUN, media annua in €/MWh, valori arrotondati. Fonte: GME.</p></div>
      <div class="callout"><b>1,3 mln €</b><p>Per un’impresa che consuma 5 GWh l’anno, la differenza tra il prezzo del 2020 e quello del 2022 ha significato oltre 1,3 milioni di euro di costo aggiuntivo in dodici mesi. Senza aver cambiato nulla nel modo di produrre.</p></div>
    </div>
  </div>
</div></section>""" % pun_chart())

    b.append("""
<section class="sec paper light"><div class="wrap">
  <div class="split">
    <div class="sticky rv"><p class="eyebrow">Perché Studio Green Capital</p><h2>Non un broker. Non un installatore. <em>Un partner.</em></h2><p class="lede" style="margin-top:20px">Chi vende energia o impianti ha un interesse nel farvi comprare. Noi abbiamo un interesse solo: che il vostro costo scenda e resti sotto controllo.</p></div>
    <ol class="nlist rv rv-d1">
      <li><div><h3>Indipendenza</h3><p>Nessun legame con fornitori, trader o installatori. Raccomandiamo ciò che conviene a voi, non ciò che conviene a qualcun altro.</p></div></li>
      <li><div><h3>Allineamento</h3><p>La nostra remunerazione è legata ai risultati che generiamo. Se il vostro costo non scende, non abbiamo fatto il nostro lavoro.</p></div></li>
      <li><div><h3>Rigore</h3><p>Ogni raccomandazione parte dai dati: profili di consumo, curve di prezzo, scenari. Niente sensazioni, solo numeri verificabili.</p></div></li>
      <li><div><h3>Continuità</h3><p>Non consegniamo un report per poi sparire. Restiamo al vostro fianco nel tempo, perché il mercato non si ferma.</p></div></li>
    </ol>
  </div>
</div></section>""")

    b.append("""
<section class="sec light"><div class="wrap">
  <div class="case rv">
    <div class="img"><img src="%(i)s/fotovoltaico.webp" alt="Impianto fotovoltaico industriale visto dall’alto" loading="lazy"></div>
    <div class="body">
      <p class="eyebrow">Risultati</p>
      <h3>Manifatturiero, Nord Italia. <em>3,8 GWh l’anno.</em></h3>
      <p>Nuova strategia di acquisto, contratti rinegoziati, copertura del rischio prezzo e un impianto fotovoltaico da 1 MWp in autoconsumo. Un intervento su più leve, coordinato da un solo interlocutore.</p>
      <div class="kpis"><div class="kpi"><b>−15%%</b><span>costo unitario dell’energia</span></div><div class="kpi"><b>−55%%</b><span>spesa energetica complessiva</span></div><div class="kpi"><b>1 MWp</b><span>fotovoltaico in autoconsumo</span></div></div>
      <a class="link" href="%(b)s/risultati/">Leggi il caso %(a)s</a>
    </div>
  </div>
</div></section>""" % {"i": IMG, "b": BASE, "a": arrow()})

    b.append(cta_band("Quanto pesa l’energia sui vostri margini? <em>Scopriamolo insieme.</em>",
                      "Un’analisi preliminare, riservata e senza impegno: bastano le ultime bollette e un’ora del vostro tempo per capire quanto valore c’è da recuperare.",
                      second=("Come lavoriamo", BASE + "/metodo/")))
    return "".join(b)

# ================================================================== CHI SIAMO
def chi_siamo():
    b = [phero("Chi siamo", "Uno studio, <em>non un fornitore.</em>",
               "Studio Green Capital è una società di consulenza energetica indipendente, spin-off italiano di InSSIDe World Inc. Nasce da un’idea precisa: portare nelle imprese lo stesso rigore che si dedica alla finanza e al diritto, applicato all’energia.",
               crumbs=[("Home", BASE + "/"), ("Chi siamo", None)], img="fiume")]
    b.append("""
<section class="sec light"><div class="wrap"><div class="split">
  <div class="sticky rv"><p class="eyebrow">Da dove veniamo</p><h2>L’energia è diventata una variabile <em>strategica.</em> Le competenze per gestirla, no.</h2></div>
  <div class="prose rv rv-d1">
    <p>Negli ultimi anni il costo dell’energia ha smesso di essere una voce prevedibile del conto economico. Prezzi che si moltiplicano in pochi mesi, contratti sempre più complessi, mercati all’ingrosso che entrano direttamente in fattura: per molte imprese l’energia è passata da costo di gestione a fattore di rischio.</p>
    <p>Eppure, dentro le aziende, chi se ne occupa è quasi sempre qualcuno che fa anche altro. L’ufficio acquisti, l’amministrazione, il titolare. Persone competenti nel loro lavoro, che affrontano un mercato specialistico con gli strumenti di un rinnovo contrattuale qualsiasi. Dall’altra parte del tavolo, invece, siedono professionisti che di energia si occupano tutto il giorno.</p>
    <p>Studio Green Capital nasce per riequilibrare quel tavolo. Portiamo nelle imprese competenze di mercato, contrattualistica e ingegneria energetica, con un modello che non prevede la vendita di nulla: né energia, né impianti, né prodotti finanziari. Solo decisioni migliori, misurate sui risultati.</p>
    <p>Siamo lo spin-off italiano di InSSIDe World Inc., da cui ereditiamo metodo e visione internazionale, applicati alla realtà delle imprese italiane: manifattura, logistica, servizi, gruppi multi-sito.</p>
  </div>
</div></div></section>""")
    b.append("""
<section class="sec dark"><div class="wrap">
  <div class="grid2">
    <div class="panel dark rv"><p class="eyebrow">Visione</p><h3>Diventare il riferimento nella gestione strategica dell’energia per le imprese energivore.</h3><p>Un ruolo attivo nelle decisioni che impattano costi, rischio e marginalità, per contribuire in modo diretto alla competitività delle imprese nel lungo periodo. Vogliamo che “avere un partner energetico” diventi normale quanto avere un commercialista.</p></div>
    <div class="panel dark rv rv-d1"><p class="eyebrow">Missione</p><h3>Ridurre il costo dell’energia, stabilizzarlo nel tempo, proteggere i margini.</h3><p>Interveniamo su analisi dei consumi, strutturazione contrattuale e sviluppo di soluzioni dedicate — dai PPA agli impianti di produzione — con un approccio integrato che combina ottimizzazione dei costi, efficientamento e controllo del rischio.</p></div>
  </div>
</div></section>""")
    b.append("""
<section class="sec light"><div class="wrap"><div class="split">
  <div class="sticky rv"><p class="eyebrow">I principi</p><h2>Quattro regole che <em>non negoziamo.</em></h2></div>
  <ol class="nlist rv rv-d1">
    <li><div><h3>Indipendenza</h3><p>Non riceviamo compensi da fornitori, trader o installatori. Ogni raccomandazione è libera da conflitti di interesse, e lo mettiamo per iscritto.</p></div></li>
    <li><div><h3>Misurabilità</h3><p>Ogni intervento ha un obiettivo numerico definito prima di iniziare e verificato dopo. Se non si può misurare, non lo proponiamo.</p></div></li>
    <li><div><h3>Lungo periodo</h3><p>Le soluzioni che costruiamo devono reggere ai cicli di mercato, non solo alla prossima scadenza contrattuale. Preferiamo un risultato solido a uno spettacolare.</p></div></li>
    <li><div><h3>Riservatezza</h3><p>Lavoriamo su dati sensibili: consumi, costi, contratti, piani industriali. Li trattiamo con la stessa cura di uno studio legale.</p></div></li>
  </ol>
</div></div></section>""")
    b.append("""
<section class="sec paper light"><div class="wrap"><div class="two-col">
  <div class="rv"><p class="eyebrow">Per chiarezza</p><h2>Cosa <em>non</em> facciamo</h2><p class="lede" style="margin-top:20px">È il modo più rapido per capire che tipo di partner siamo.</p></div>
  <div class="rv rv-d1">%s</div>
</div></div></section>""" % checks(["<strong>Non vendiamo energia.</strong> Non siamo un fornitore né un broker: non abbiamo tariffe da piazzare.",
                                     "<strong>Non installiamo impianti.</strong> Progettiamo e verifichiamo, poi mettiamo in gara chi li realizza.",
                                     "<strong>Non incassiamo provvigioni nascoste.</strong> La nostra remunerazione la vedete e la decidete voi con noi.",
                                     "<strong>Non proponiamo soluzioni standard.</strong> Ogni impresa ha un profilo energetico diverso: il piano lo costruiamo su quello."], x=True))
    b.append(cta_band("Parliamo della <em>vostra</em> situazione energetica.", "Un primo confronto riservato per capire se e quanto possiamo essere utili. Senza impegno, senza vendite."))
    return "".join(b)

# ================================================================== SERVIZI
def servizi():
    b = [phero("Servizi", "Ogni leva che decide <em>il costo dell’energia.</em>",
               "Cinque ambiti di intervento, un solo metodo. Li attiviamo in base al profilo dell’impresa, nell’ordine che genera più valore, e li coordiniamo perché lavorino insieme.",
               crumbs=[("Home", BASE + "/"), ("Servizi", None)])]
    rows = []
    for s in SERVICES:
        rows.append("""<div class="row rv"><div class="n">%s</div><div><h3>%s</h3><span class="tag">%s</span></div><div><p>%s</p><p>%s</p><a class="link" href="%s">Approfondisci %s</a></div></div>""" % (s["n"], s["title"], s["short"], s["lede"], s["teaser"], surl(s), arrow()))
    b.append('<section class="sec light"><div class="wrap"><div class="rows">%s</div></div></section>' % "".join(rows))
    b.append("""
<section class="sec dark"><div class="wrap">
  <div class="head rv"><p class="eyebrow">Come si combinano</p><h2>Le leve valgono di più <em>insieme.</em></h2><p class="lede">Un PPA copre una parte del fabbisogno; il fotovoltaico un’altra; il contratto di fornitura gestisce il resto; l’efficienza riduce il totale. Il valore sta nel coordinarle, e nell’avere un solo interlocutore che risponde del risultato complessivo.</p></div>
  %s
</div></section>""" % steps())
    b.append(cta_band("Non sapete quale leva attivare per prima? <em>È il nostro lavoro capirlo.</em>", "L’analisi preliminare serve esattamente a questo: capire dove sta il valore, nel vostro caso specifico, prima di muovere qualsiasi cosa."))
    return "".join(b)

def servizio(s, i):
    prev = SERVICES[i - 1] if i > 0 else None
    nxt = SERVICES[i + 1] if i < len(SERVICES) - 1 else None
    b = [phero("Servizi · %s" % s["n"], s["title"], s["lede"], crumbs=[("Home", BASE + "/"), ("Servizi", BASE + "/servizi/"), (s["title"], None)], img=s["img"])]
    b.append("""
<section class="sec light"><div class="wrap"><div class="two-col">
  <div class="panel rv"><p class="eyebrow">Il problema</p><h3>Com’è oggi, nella maggior parte delle imprese</h3><p>%s</p></div>
  <div class="panel dark rv rv-d1"><p class="eyebrow">La nostra risposta</p><h3>Come lo affrontiamo</h3><p>%s</p></div>
</div></div></section>""" % (s["problem"], s["answer"]))
    b.append("""
<section class="sec paper light"><div class="wrap"><div class="split">
  <div class="sticky rv"><p class="eyebrow">Cosa facciamo</p><h2>Le attività, <em>una per una.</em></h2><p class="lede" style="margin-top:20px">Per chi è pensato: %s</p></div>
  <div class="rv rv-d1">%s</div>
</div></div></section>""" % (s["who"], checks(s["do"])))
    gets = "".join('<div class="panel rv rv-d%d"><p class="eyebrow">Risultato</p><h3>%s</h3><p>%s</p></div>' % (k + 1, t, d) for k, (t, d) in enumerate(s["get"]))
    b.append("""
<section class="sec light"><div class="wrap">
  <div class="head rv"><p class="eyebrow">Cosa ottenete</p><h2>Tre risultati <em>concreti.</em></h2></div>
  <div class="grid3">%s</div>
</div></section>""" % gets)
    pn = '<div class="pn">'
    pn += ('<a class="prev" href="%s"><small>Servizio precedente</small><span>%s</span></a>' % (surl(prev), prev["title"])) if prev else '<a class="prev" href="%s/servizi/"><small>Panoramica</small><span>Tutti i servizi</span></a>' % BASE
    pn += ('<a class="next" href="%s"><small>Servizio successivo</small><span>%s</span></a>' % (surl(nxt), nxt["title"])) if nxt else '<a class="next" href="%s/metodo/"><small>Continua</small><span>Il metodo</span></a>' % BASE
    pn += '</div>'
    b.append('<section class="sec-sm light"><div class="wrap">%s</div></section>' % pn)
    b.append(cta_band("Vale la pena approfondire <em>nel vostro caso?</em>", "Un’analisi preliminare ci dice in poche settimane se questa leva può generare valore per la vostra impresa, e quanto."))
    return "".join(b)

# ================================================================== METODO
def metodo():
    b = [phero("Il metodo", "Un processo, <em>non una consulenza spot.</em>",
               "Quattro fasi che si ripetono nel tempo, perché il mercato dell’energia non sta fermo. Ogni fase produce qualcosa di concreto che resta all’impresa: dati, decisioni, contratti, risultati misurati.",
               crumbs=[("Home", BASE + "/"), ("Metodo", None)], img="germoglio")]
    det = [
        ("Analizziamo", "Costruire la mappa energetica dell’impresa",
         "Raccogliamo dodici mesi di fatture, i contratti in essere, le curve di prelievo orarie e le informazioni sui processi. Ricostruiamo la struttura reale del costo: quanto pesa la materia prima, quanto il trasporto, quanto gli oneri; dove si concentrano i consumi; quanto l’impresa è esposta al mercato e in quali momenti dell’anno.",
         ["Mappa energetica dell’impresa con struttura del costo per componente", "Profilo di consumo e curva di carico commentati", "Stima quantificata delle aree di miglioramento"]),
        ("Strutturiamo", "Trasformare l’analisi in una strategia con i numeri",
         "Sulla base della mappa definiamo quali leve attivare, in che ordine e con quali obiettivi: struttura contrattuale, eventuale PPA, produzione propria, efficienza. Per ogni leva quantifichiamo valore atteso, rischio residuo e tempi. Il piano viene discusso e approvato insieme, prima di muovere qualsiasi cosa.",
         ["Piano energetico con obiettivi, priorità e scenari", "Politica di gestione del rischio prezzo condivisa", "Calendario delle azioni e delle finestre decisionali"]),
        ("Eseguiamo", "Portare a casa i risultati, dalla vostra parte del tavolo",
         "Gestiamo le gare tra fornitori, negoziamo contratti e PPA, seguiamo gli studi di fattibilità e la realizzazione degli impianti, verifichiamo le offerte degli installatori. Voi decidete; noi prepariamo le decisioni e le portiamo a termine, con la competenza di chi fa questo ogni giorno.",
         ["Contratti negoziati e verificati clausola per clausola", "Gare gestite con controparti qualificate", "Supervisione tecnica ed economica degli interventi"]),
        ("Presidiamo", "Governare l’energia nel tempo",
         "Il lavoro non finisce con la firma. Monitoriamo i consumi e i prezzi, controlliamo le fatture, presidiamo le finestre di fissazione, aggiorniamo il piano quando cambiano il mercato o l’impresa. Un report periodico vi dice esattamente dove siete rispetto agli obiettivi.",
         ["Report periodico su costi, consumi e obiettivi", "Controllo delle fatture e gestione delle anomalie", "Revisione della strategia a ogni cambiamento rilevante"]),
    ]
    rows = []
    for i, (t, sub, p, out) in enumerate(det):
        rows.append("""<div class="row rv"><div class="n">0%d</div><div><h3>%s</h3><span class="tag">%s</span></div><div><p>%s</p><h4 style="margin:22px 0 12px">Cosa resta all’impresa</h4>%s</div></div>""" % (i + 1, t, sub, p, checks(out)))
    b.append('<section class="sec light"><div class="wrap"><div class="rows">%s</div></div></section>' % "".join(rows))
    b.append("""
<section class="sec dark"><div class="wrap"><div class="split">
  <div class="sticky rv"><p class="eyebrow">Il modello economico</p><h2>Guadagniamo <em>se guadagnate voi.</em></h2><p class="lede" style="margin-top:20px">Il modo in cui un consulente viene pagato dice tutto sui consigli che darà. Il nostro è costruito per allineare gli interessi.</p></div>
  <ol class="nlist rv rv-d1">
    <li><div><h3>Nessuna provvigione dai fornitori</h3><p>Non riceviamo compensi da chi vende energia o impianti. Se lo facessimo, non potremmo dirvi con onestà qual è l’offerta migliore.</p></div></li>
    <li><div><h3>Remunerazione legata ai risultati</h3><p>Una parte sostanziale del nostro compenso dipende dal valore che generiamo, misurato con criteri definiti insieme prima di iniziare.</p></div></li>
    <li><div><h3>Rapporto continuativo</h3><p>Lavoriamo su mandato pluriennale, perché è nel tempo che la strategia energetica produce i risultati maggiori. Con la libertà, per voi, di interrompere se non siamo all’altezza.</p></div></li>
  </ol>
</div></div></section>""")
    b.append("""
<section class="sec light"><div class="wrap">
  <div class="head rv"><p class="eyebrow">Come si inizia</p><h2>Le prime <em>quattro settimane.</em></h2><p class="lede">Dal primo contatto alla presentazione del piano. Quello che serve da parte vostra è poco: i documenti e qualche ora di confronto.</p></div>
  <div class="tl">
    <div class="rv"><small>Settimana 1</small><h4>Primo confronto</h4><p>Un incontro riservato per capire l’impresa, i consumi, le scadenze. Raccogliamo le fatture degli ultimi dodici mesi e i contratti attivi.</p></div>
    <div class="rv rv-d1"><small>Settimane 2–3</small><h4>Analisi</h4><p>Ricostruiamo la struttura del costo e il profilo di consumo. Se disponibile, analizziamo la curva di carico oraria.</p></div>
    <div class="rv rv-d2"><small>Settimana 4</small><h4>Restituzione</h4><p>Vi presentiamo la mappa energetica e una stima quantificata delle opportunità: dove sta il valore e quanto vale.</p></div>
    <div class="rv rv-d3"><small>Poi</small><h4>Decisione</h4><p>Se i numeri vi convincono, definiamo insieme il mandato. Se no, la mappa resta a voi. Senza impegno.</p></div>
  </div>
</div></section>""")
    b.append(cta_band("Iniziamo dalla <em>prima settimana.</em>", "Un incontro riservato, le ultime bollette, e in un mese sapete quanto valore c’è da recuperare. Il resto lo decidete dopo."))
    return "".join(b)

# ================================================================== RISULTATI
def risultati():
    b = [phero("Risultati", "I numeri prima, <em>le parole dopo.</em>",
               "Ogni mandato ha obiettivi misurabili definiti all’inizio e verificati alla fine. Qui raccontiamo come lavoriamo attraverso un caso concreto, con il consenso del cliente.",
               crumbs=[("Home", BASE + "/"), ("Risultati", None)], img="fotovoltaico")]
    b.append("""
<section class="sec light"><div class="wrap">
  <p class="eyebrow rv">Caso · Manifatturiero</p>
  <div class="split" style="align-items:stretch">
    <div class="rv">
      <h2>Un’azienda manifatturiera del Nord Italia, <em>3,8 GWh l’anno.</em></h2>
      <dl class="dl" style="margin-top:32px">
        <div><dt>Settore</dt><dd>Manifatturiero, produzione continua</dd></div>
        <div><dt>Localizzazione</dt><dd>Nord Italia</dd></div>
        <div><dt>Consumo annuo</dt><dd>~3,8 GWh</dd></div>
        <div><dt>Spesa energetica iniziale</dt><dd>~950.000 € l’anno</dd></div>
      </dl>
    </div>
    <div class="prose rv rv-d1">
      <h3 style="margin-top:0">La situazione di partenza</h3>
      <p>Contratto di fornitura rinnovato ogni anno a ridosso della scadenza, con prezzo interamente indicizzato al mercato. Nessuna strategia di copertura. Coperture dello stabilimento inutilizzate. Nel 2022 la spesa energetica era più che raddoppiata rispetto a due anni prima, senza alcun cambiamento nella produzione.</p>
      <h3>L’intervento</h3>
      <p>Abbiamo ridefinito da capo la strategia di acquisto: rinegoziazione dei contratti in essere, nuova struttura con una quota di prezzo fissata in finestre pianificate e una copertura del rischio sulla parte restante. In parallelo, studio di fattibilità e realizzazione di un impianto fotovoltaico da 1 MWp in autoconsumo, con gara tra installatori e verifica indipendente delle offerte.</p>
      <h3>Il risultato</h3>
      <p>Costo unitario dell’energia acquistata ridotto del 15%. Grazie all’autoconsumo e alla nuova struttura contrattuale, spesa energetica complessiva ridotta del 55%. Ma soprattutto: una spesa oggi prevedibile, con un’esposizione al mercato scelta e non subita, e un margine operativo protetto anche nei mesi di prezzo alto.</p>
    </div>
  </div>
  <div class="kpis light rv" style="grid-template-columns:repeat(4,1fr);margin-top:56px">
    <div class="kpi"><b>−15%</b><span>costo unitario dell’energia acquistata</span></div>
    <div class="kpi"><b>−55%</b><span>spesa energetica complessiva annua</span></div>
    <div class="kpi"><b>1 MWp</b><span>fotovoltaico in autoconsumo realizzato</span></div>
    <div class="kpi"><b>1</b><span>interlocutore per l’intero progetto</span></div>
  </div>
</div></section>""")
    b.append("""
<section class="sec dark"><div class="wrap"><div class="split">
  <div class="sticky rv"><p class="eyebrow">Cosa misuriamo</p><h2>Gli indicatori che <em>contano davvero.</em></h2><p class="lede" style="margin-top:20px">Il risparmio in bolletta è solo uno dei numeri. Un’impresa che governa l’energia guarda anche agli altri.</p></div>
  <ol class="nlist rv rv-d1">
    <li><div><h3>Costo unitario (€/MWh)</h3><p>Il prezzo pieno dell’energia, tutte le componenti incluse, confrontato con il mercato e con la situazione di partenza.</p></div></li>
    <li><div><h3>Quota di spesa protetta</h3><p>Quanta parte del costo è al riparo dalla volatilità: prezzo fisso, PPA, autoproduzione.</p></div></li>
    <li><div><h3>Prevedibilità</h3><p>Lo scostamento tra spesa prevista a budget e spesa effettiva. Un numero che l’amministrazione apprezza quanto la produzione.</p></div></li>
    <li><div><h3>Impatto sul margine</h3><p>Il risultato finale: quanto la gestione dell’energia ha spostato sul margine operativo dell’impresa.</p></div></li>
  </ol>
</div></div></section>""")
    b.append("""
<section class="sec-sm light"><div class="wrap"><div class="panel rv" style="max-width:820px"><p class="eyebrow">Una nota</p><h3>Perché pubblichiamo pochi casi</h3><p>Lavoriamo su dati sensibili — costi, contratti, piani industriali — e ogni mandato è coperto da riservatezza. Pubblichiamo solo i casi per cui il cliente ha dato il consenso esplicito, in forma anonima. In un incontro riservato possiamo raccontarvi molto di più.</p></div></div></section>""")
    b.append(cta_band("Il prossimo caso potrebbe essere <em>il vostro.</em>", "Iniziamo da un’analisi preliminare: in poche settimane sapete quanto valore c’è da recuperare nella vostra impresa."))
    return "".join(b)

# ================================================================== CONTATTI
def contatti():
    b = [phero("Contatti", "Richiedete una <em>valutazione riservata.</em>",
               "Raccontateci in poche righe la vostra impresa. Vi ricontattiamo per fissare un primo confronto: senza impegno, senza vendite, in totale riservatezza.",
               crumbs=[("Home", BASE + "/"), ("Contatti", None)])]
    b.append("""
<section class="sec light"><div class="wrap"><div class="split">
  <div class="rv">
    <form class="form" id="contactForm" novalidate>
      <div><label for="azienda">Azienda *</label><input id="azienda" name="azienda" type="text" required autocomplete="organization"></div>
      <div><label for="nome">Nome e cognome *</label><input id="nome" name="nome" type="text" required autocomplete="name"></div>
      <div><label for="email">Email *</label><input id="email" name="email" type="email" required autocomplete="email"></div>
      <div><label for="telefono">Telefono</label><input id="telefono" name="telefono" type="tel" autocomplete="tel"></div>
      <div><label for="settore">Settore</label><select id="settore" name="settore"><option value="">Seleziona…</option><option>Manifatturiero</option><option>Alimentare</option><option>Logistica e trasporti</option><option>Chimico / farmaceutico</option><option>Servizi e terziario</option><option>Grande distribuzione</option><option>Altro</option></select></div>
      <div><label for="consumo">Consumo annuo indicativo</label><select id="consumo" name="consumo"><option value="">Seleziona…</option><option>Fino a 1 GWh</option><option>1 – 5 GWh</option><option>5 – 20 GWh</option><option>Oltre 20 GWh</option><option>Non lo so</option></select></div>
      <div class="full"><label for="messaggio">Cosa vi interessa approfondire?</label><textarea id="messaggio" name="messaggio" placeholder="Es. scadenza del contratto, valutazione di un fotovoltaico, interesse per un PPA…"></textarea></div>
      <label class="full consent"><input type="checkbox" required> <span>Ho letto l’<a href="%(b)s/privacy/">informativa sulla privacy</a> e acconsento al trattamento dei dati per essere ricontattato. *</span></label>
      <div class="full"><button class="btn btn-dark" type="submit">Invia la richiesta %(a)s</button></div>
      <p class="full sent" id="formSent" aria-live="polite"></p>
    </form>
  </div>
  <div class="contact-aside rv rv-d1">
    <div class="item"><small>Email</small><a href="mailto:%(m)s">%(m)s</a></div>
    <div class="item"><small>Cosa succede dopo</small><p class="small" style="margin:6px 0 0">Vi rispondiamo entro due giorni lavorativi per fissare un primo confronto. Se ha senso proseguire, raccogliamo le fatture degli ultimi dodici mesi e in circa quattro settimane vi restituiamo la mappa energetica dell’impresa, con una stima del valore recuperabile.</p></div>
    <div class="item"><small>Riservatezza</small><p class="small" style="margin:6px 0 0">Tutto ciò che condividete resta tra noi. Su richiesta firmiamo un accordo di riservatezza prima ancora del primo incontro.</p></div>
    <div class="item"><small>Cosa serve per iniziare</small><p class="small" style="margin:6px 0 0">Le ultime fatture di energia elettrica e gas, i contratti di fornitura attivi e, se disponibile, la curva di carico oraria. Al resto pensiamo noi.</p></div>
  </div>
</div></div></section>""" % {"b": BASE, "a": arrow(), "m": CONTACT_EMAIL})
    return "".join(b)

# ================================================================== LEGALI
LEGAL_NOTE = "<p class=\"small muted\">Titolare del trattamento: Studio Green Capital SRL — [sede legale] — P.IVA [da inserire] — %s</p>" % CONTACT_EMAIL

def privacy():
    b = [phero("Informativa", "Privacy policy", "Informativa sul trattamento dei dati personali ai sensi del Regolamento (UE) 2016/679 (GDPR).", crumbs=[("Home", BASE + "/"), ("Privacy", None)])]
    b.append("""
<section class="sec light"><div class="wrap"><div class="prose">
%s
<h2>1. Titolare del trattamento</h2>
<p>Il titolare del trattamento è Studio Green Capital SRL (di seguito “il Titolare”), contattabile all’indirizzo email indicato sopra.</p>
<h2>2. Dati trattati</h2>
<p><strong>Dati di navigazione.</strong> I sistemi informatici che ospitano questo sito acquisiscono, nel normale funzionamento, alcuni dati tecnici la cui trasmissione è implicita nell’uso di internet (indirizzi IP, tipo di browser, orario della richiesta). Sono utilizzati esclusivamente per garantire il funzionamento e la sicurezza del sito e non sono associati a persone identificate.</p>
<p><strong>Dati forniti volontariamente.</strong> Il modulo di contatto apre il programma di posta dell’utente con un messaggio precompilato: i dati inseriti (azienda, nome, email, telefono, settore, consumi, messaggio) sono trasmessi dall’utente stesso via email e trattati dal Titolare al solo fine di rispondere alla richiesta.</p>
<h2>3. Finalità e base giuridica</h2>
<p>I dati forniti tramite il modulo o via email sono trattati per rispondere alle richieste di informazioni e valutazione (base giuridica: esecuzione di misure precontrattuali su richiesta dell’interessato, art. 6.1.b GDPR) e per adempiere a obblighi di legge (art. 6.1.c). Non svolgiamo attività di marketing automatizzato né profilazione.</p>
<h2>4. Conservazione</h2>
<p>I dati sono conservati per il tempo necessario a gestire la richiesta e, in caso di instaurazione di un rapporto contrattuale, per la durata dello stesso e per i termini di legge successivi.</p>
<h2>5. Destinatari</h2>
<p>I dati possono essere trattati da personale autorizzato del Titolare e da fornitori di servizi tecnici (es. posta elettronica, hosting) nominati responsabili del trattamento. Il sito è ospitato su GitHub Pages (GitHub, Inc.); i trasferimenti extra-UE avvengono sulla base delle garanzie previste dal GDPR. I dati non sono diffusi né ceduti a terzi per finalità commerciali.</p>
<h2>6. Diritti dell’interessato</h2>
<p>In qualsiasi momento è possibile esercitare i diritti previsti dagli artt. 15–22 GDPR (accesso, rettifica, cancellazione, limitazione, opposizione, portabilità) scrivendo all’indirizzo email del Titolare. È inoltre possibile proporre reclamo al Garante per la protezione dei dati personali.</p>
<h2>7. Aggiornamenti</h2>
<p>La presente informativa può essere aggiornata; la versione in vigore è quella pubblicata su questa pagina. Ultimo aggiornamento: settembre 2026.</p>
</div></div></section>""" % LEGAL_NOTE)
    return "".join(b)

def cookie():
    b = [phero("Informativa", "Cookie policy", "Come questo sito utilizza (e soprattutto non utilizza) i cookie.", crumbs=[("Home", BASE + "/"), ("Cookie", None)])]
    b.append("""
<section class="sec light"><div class="wrap"><div class="prose">
%s
<h2>Cosa sono i cookie</h2>
<p>I cookie sono piccoli file di testo che i siti salvano sul dispositivo dell’utente per ricordare informazioni o tracciare la navigazione.</p>
<h2>Cookie utilizzati da questo sito</h2>
<p>Questo sito <strong>non utilizza cookie di profilazione</strong>, né propri né di terze parti, e non integra strumenti di analisi statistica o pubblicitari. I caratteri tipografici sono ospitati direttamente sul sito, senza richieste a servizi esterni.</p>
<p>Il sito può utilizzare esclusivamente eventuali cookie tecnici strettamente necessari al funzionamento della piattaforma di hosting (GitHub Pages), per i quali non è richiesto il consenso ai sensi della normativa vigente.</p>
<h2>Come gestire i cookie</h2>
<p>È comunque possibile bloccare o eliminare i cookie tramite le impostazioni del proprio browser. Le istruzioni sono disponibili nella documentazione di Chrome, Firefox, Safari ed Edge.</p>
<h2>Riferimenti</h2>
<p>Per ogni informazione sul trattamento dei dati personali si rimanda alla <a href="%s/privacy/">Privacy policy</a>. Ultimo aggiornamento: settembre 2026.</p>
</div></div></section>""" % (LEGAL_NOTE, BASE))
    return "".join(b)

def not_found():
    return """<section class="phero dark" style="min-height:70svh;display:flex;align-items:center"><div class="wrap"><p class="eyebrow">Errore 404</p><h1>Questa pagina <em>non esiste.</em></h1><p class="lede">L’indirizzo potrebbe essere cambiato. Ripartite dalla home o dai servizi.</p><div class="hero-actions" style="display:flex;gap:14px;margin-top:32px;flex-wrap:wrap"><a class="btn btn-brass" href="%s/">Torna alla home</a><a class="btn btn-ghost" href="%s/servizi/">I servizi</a></div></div></section>""" % (BASE, BASE)

# ================================================================== generazione
def main():
    pages = []
    pages.append(page("/", "Studio Green Capital — Consulenza energetica strategica per le imprese", "Advisor indipendenti per la gestione strategica dell’energia: contratti, PPA, fotovoltaico e autoconsumo, efficienza. Riduciamo il costo dell’energia e lo rendiamo prevedibile.", home()))
    pages.append(page("/chi-siamo/", "Chi siamo — Studio Green Capital", "Società di consulenza energetica indipendente, spin-off italiano di InSSIDe World Inc. Nessun prodotto da vendere: solo decisioni migliori, misurate sui risultati.", chi_siamo()))
    pages.append(page("/servizi/", "Servizi — Studio Green Capital", "Supply & procurement, PPA, produzione e autoconsumo, efficienza energetica, welfare energetico: ogni leva che decide il costo dell’energia della vostra impresa.", servizi()))
    for i, s in enumerate(SERVICES):
        t = re.sub(r"&amp;", "&", s["title"])
        pages.append(page("/servizi/%s/" % s["slug"], "%s — Studio Green Capital" % t, s["lede"][:155], servizio(s, i)))
    pages.append(page("/metodo/", "Il metodo — Studio Green Capital", "Analizziamo, strutturiamo, eseguiamo, presidiamo: un processo in quattro fasi che non finisce con la firma. Remunerazione legata ai risultati.", metodo()))
    pages.append(page("/risultati/", "Risultati — Studio Green Capital", "Un caso concreto: azienda manifatturiera del Nord Italia, 3,8 GWh l’anno, −15% costo unitario e −55% spesa energetica complessiva.", risultati()))
    pages.append(page("/contatti/", "Contatti — Studio Green Capital", "Richiedete una valutazione riservata e senza impegno della situazione energetica della vostra impresa.", contatti()))
    pages.append(page("/privacy/", "Privacy policy — Studio Green Capital", "Informativa sul trattamento dei dati personali.", privacy(), light=True))
    pages.append(page("/cookie/", "Cookie policy — Studio Green Capital", "Informativa sull’uso dei cookie.", cookie(), light=True))

    # 404 (GitHub Pages la serve da sola)
    html404 = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    body404 = not_found()
    html404 = re.sub(r"<main id=\"main\">.*?</main>", "<main id=\"main\">%s</main>" % body404.replace("\\", "\\\\"), html404, flags=re.S)
    html404 = re.sub(r"<title>.*?</title>", "<title>Pagina non trovata — Studio Green Capital</title>", html404)
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(html404)

    # favicon, sitemap, robots
    open(os.path.join(ROOT, "assets", "favicon.svg"), "w", encoding="utf-8").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="#0F2A1F"/><path d="M11 29c0-9 6.5-16 18-16-1 10-7.5 16-18 16z" fill="#B08A45"/><path d="M11 29c3.5-5.5 8-10 13.5-12.5" fill="none" stroke="#0A1B14" stroke-width="1.4" stroke-linecap="round" stroke-opacity=".8"/></svg>')
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join("  <url><loc>%s%s</loc></url>\n" % (SITE_URL, p) for p in pages) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE_URL)
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    print("Generate %d pagine + 404, sitemap, robots." % len(pages))

if __name__ == "__main__":
    main()
