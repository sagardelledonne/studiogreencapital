# -*- coding: utf-8 -*-
"""Scrive proposte-logo/index.html usando i simboli generati da gen.py.
Uso: python logo/gen.py && python logo/pagina.py
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SYMS = open(os.path.join(HERE, "_symbols.html"), encoding="utf-8").read()
R = dict((l.split()[0], float(l.split()[1])) for l in open(os.path.join(HERE, "_ratios.txt")))
R["s-barre"] = R["s-baffi"] = R["s"]

def use(sid, w, cls=""):
    h = w / R[sid]
    return '<svg class="%s" width="%d" height="%d"><use href="#%s"/></svg>' % (cls, w, round(h), sid)

def use_h(sid, h, cls=""):
    return use(sid, round(h * R[sid]), cls)

def tile(cls, inner, label=""):
    return '<div class="tile %s">%s%s</div>' % (cls, ('<small>%s</small>' % label) if label else "", inner)

def lock(sid, w, name_size="2.1rem"):
    return '<div class="lock">%s<div><div class="name" style="font-size:%s">Studio Green Capital</div><div class="sub">Strategic Energy Advisory</div></div></div>' % (use(sid, w), name_size)

def stack(sid, w, sub="Strategic Energy Advisory", name='Studio Green<br>Capital'):
    return '<div class="stack">%s<div class="name">%s</div><div class="sub">%s</div></div>' % (use(sid, w).replace('class=""', 'class="" style="margin:0 auto"'), name, sub)

page = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Proposte logo — Studio Green Capital</title>
<link rel="stylesheet" href="../assets/fonts/fonts.css">
<style>
:root{--g950:#0A1B14;--g900:#0F2A1F;--g700:#1D4D39;--g500:#2E7A5A;--cream:#F4F1EA;--paper:#FBF9F4;--ink:#121C17;--muted:#66756C;--brass:#B08A45;--brass2:#D6B97E;--line:rgba(18,28,23,.12)}
*{box-sizing:border-box}
body{margin:0;font-family:Manrope,system-ui,sans-serif;background:var(--cream);color:var(--ink);line-height:1.55}
.wrap{width:min(1180px,100% - 40px);margin:0 auto;padding:56px 0 96px}
h1{font-family:Fraunces,Georgia,serif;font-weight:400;font-size:clamp(2rem,4vw,3rem);margin:0 0 8px;letter-spacing:-.01em}
h2{font-family:Fraunces,Georgia,serif;font-weight:400;font-size:1.6rem;margin:64px 0 6px}
.eyebrow{font-size:.75rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--brass);margin:0 0 8px}
p.note{color:var(--muted);max-width:72ch;margin:0 0 22px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.tile{border-radius:20px;padding:40px;display:flex;align-items:center;justify-content:center;min-height:260px;border:1px solid var(--line);position:relative;overflow:hidden}
.tile.dark{background:var(--g900);color:#fff}
.tile.darker{background:var(--g950);color:#fff}
.tile.light{background:var(--paper);color:var(--g900)}
.tile.cream{background:var(--cream);color:var(--g900)}
.tile small{position:absolute;left:18px;top:14px;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;opacity:.5;font-weight:700}
svg{display:block;max-width:100%;height:auto}
.stroke{fill:none;stroke:currentColor;stroke-width:7;stroke-linecap:round;stroke-linejoin:round}
.brass{color:var(--brass)}.brass2{color:var(--brass2)}.white{color:#fff}.green{color:var(--g900)}
.lock{display:flex;align-items:center;gap:26px}
.lock .name{font-family:Fraunces,Georgia,serif;line-height:1;letter-spacing:-.01em;font-weight:400;white-space:nowrap}
.lock .sub{font-size:.68rem;letter-spacing:.24em;text-transform:uppercase;font-weight:700;margin-top:9px;opacity:.75}
.stack{text-align:center}
.stack .name{font-family:Fraunces,Georgia,serif;font-size:1.9rem;line-height:1.05;margin-top:22px;letter-spacing:-.01em}
.stack .sub{font-size:.66rem;letter-spacing:.26em;text-transform:uppercase;font-weight:700;margin-top:10px;opacity:.75}
.row3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.tile.sm{min-height:200px;padding:28px}
.chip{display:grid;place-items:center;border-radius:22px}
.tiny{display:flex;gap:26px;align-items:center;flex-wrap:wrap;justify-content:center}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:18px;align-items:stretch}
.cmp img{width:100%;height:100%;object-fit:cover;border-radius:20px;border:1px solid var(--line)}
.legend{display:flex;gap:18px;flex-wrap:wrap;font-size:.85rem;color:var(--muted);margin-top:14px}
.legend span::before{content:"";display:inline-block;width:14px;height:4px;border-radius:2px;background:var(--c);margin-right:6px;vertical-align:middle}
@media (max-width:760px){.grid,.row3,.cmp{grid-template-columns:1fr}.tile{min-height:200px;padding:28px}.lock{flex-direction:column;text-align:center;gap:16px}.lock .name{font-size:1.5rem!important}}
</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
__SYMS__
</defs></svg>

<div class="wrap">
  <p class="eyebrow">Studio Green Capital</p>
  <h1>Proposte per il logo — seconda versione</h1>
  <p class="note">La S resta in due tratti, come nel tuo disegno. Ogni tratto è ora una curva unica e continua: una barra dritta che si raccorda al “baffo”, e il baffo è costruito come una <em>spirale di Eulero a tratti</em> (la curva usata per tracciare strade e binari: la curvatura cambia in modo graduale, mai a scatti). I parametri sono stati calcolati perché la curva passi per i punti misurati sul tuo schizzo: apice del giro, conca, estremo del baffo.</p>

  <h2>Dallo schizzo al vettoriale</h2>
  <div class="cmp">
    <img src="schizzo.webp" alt="Lo schizzo a penna">
    __CMP__
  </div>

  <h2>1 · Il simbolo</h2>
  <p class="note">Il secondo tratto è il primo ruotato di 180°: la S è perfettamente simmetrica rispetto al centro.</p>
  <div class="grid">
    __T1__
  </div>

  <h2>2 · Simbolo + nome, in orizzontale</h2>
  <div class="grid">
    __T2__
  </div>

  <h2>3 · Simbolo + nome, in verticale</h2>
  <div class="grid">
    __T3__
  </div>

  <h2>4 · Il monogramma SGC</h2>
  <p class="note">La S con i baffi più corti (stessa costruzione, punti obiettivo più vicini), poi G e C con lo stesso tratto. La G finisce con una barra orizzontale come quelle della S, raccordata all’arco con la stessa curva morbida.</p>
  <div class="grid">
    __T4__
  </div>

  <h2>5 · Icona</h2>
  <div class="row3">
    __T5__
  </div>
  <div class="tile light" style="margin-top:18px;min-height:0;padding:28px"><small>a dimensioni reali</small>
    <div class="tiny">__TINY__</div>
  </div>

  <h2>Come starebbe nell’intestazione</h2>
  <div class="tile darker" style="justify-content:flex-start;min-height:0;padding:20px 30px;border-radius:14px">
    <div class="lock" style="gap:14px">__HEAD__<div><div class="name" style="font-size:1.25rem;font-weight:500">Studio Green Capital</div><div class="sub" style="font-size:.58rem;margin-top:3px;letter-spacing:.2em">Strategic Energy Advisory</div></div></div>
    <div style="margin-left:auto;display:flex;gap:26px;font-size:.9rem;font-weight:600;opacity:.85"><span>Chi siamo</span><span>Servizi</span><span>Metodo</span><span>Risultati</span><span>Contatti</span></div>
  </div>
</div>
</body>
</html>
"""

t1 = "".join([
    tile("dark", use("s", 320, "brass"), "ottone su verde"),
    tile("light", use("s", 320, "green"), "verde su carta"),
    tile("darker", use("s", 320, "white"), "bianco su verde scuro"),
    tile("cream", '<div style="position:relative;width:320px">%s<div style="position:absolute;inset:0">%s</div></div>' % (use("s-baffi", 320, "green"), use("s-barre", 320, "brass")), "bicolore: barre in ottone"),
])
t2 = "".join([tile("dark", lock("s", 170)), tile("light", lock("s", 170))])
t3 = "".join([tile("dark", stack("s", 220)), tile("light", stack("s", 220))])
t4 = "".join([
    tile("dark", use("sgc", 440, "brass")),
    tile("light", use("sgc", 440, "green")),
    tile("darker", stack("sgc", 360, name="", sub="Studio Green Capital").replace('<div class="name"></div>', "")),
    tile("cream", stack("s-compatta", 230, name="", sub="SGC · Studio Green Capital").replace('<div class="name"></div>', "")),
])
def chip(bg, sid, w, cls, size=96, radius="22px"):
    return '<div class="chip" style="background:%s;width:%dpx;height:%dpx;border-radius:%s">%s</div>' % (bg, size, size, radius, use(sid, w, cls))
t5 = "".join([
    tile("sm light", chip("var(--g900)", "s", 74, "brass"), "quadrato arrotondato"),
    tile("sm light", chip("var(--g900)", "s", 66, "brass", radius="50%"), "tondo"),
    tile("sm light", chip("var(--brass)", "s", 74, "green"), "ottone pieno"),
])
tiny = "".join([
    chip("var(--g900)", "s", 40, "brass", size=52, radius="13px"),
    chip("var(--g900)", "s", 24, "brass", size=32, radius="8px"),
    use("s", 70, "green"), use("s", 44, "green"), use("sgc", 110, "green"),
])
cmp_ = tile("dark", use("s", 380, "brass"), "vettoriale")
head = use("s", 62, "brass")

html = (page.replace("__SYMS__", SYMS).replace("__CMP__", cmp_).replace("__T1__", t1).replace("__T2__", t2)
        .replace("__T3__", t3).replace("__T4__", t4).replace("__T5__", t5).replace("__TINY__", tiny).replace("__HEAD__", head))
out = os.path.join(ROOT, "proposte-logo", "index.html")
open(out, "w", encoding="utf-8").write(html)
print("scritto", out, len(html) // 1024, "KB")
