# -*- coding: utf-8 -*-
"""Genera il simbolo di Studio Green Capital: la S in due tratti dello schizzo, ridisegnata
con curve continue (tangente e curvatura continue in ogni punto).

Ogni tratto = barra dritta + "baffo". Il baffo è una spirale di Eulero a tratti (curvatura
lineare a tratti, vedi baffo.py) ottimizzata sui punti misurati sullo schizzo.
Il secondo tratto è il primo ruotato di 180° attorno al centro.

Uso:  python logo/gen.py   -> scrive logo/*.svg, logo/_symbols.html e le proporzioni
"""
import math, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import baffo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "logo")
STROKE = 7
G = 20            # distanza fra le due barre (asse-asse)
BAR = 76          # lunghezza delle barre

# ----------------------------------------------------------------- S
def s_strokes(targets=None):
    """Ritorna i due tratti della S (liste di punti), centrati nell'origine."""
    if targets:
        baffo.TARGET.update(targets)
    pts, params = baffo.baffo_points()
    # tratto alto: barra da (+BAR/2, -G/2) a (-BAR/2, -G/2), poi il baffo dal capo sinistro
    x0 = -BAR / 2
    top = [(BAR / 2, -G / 2), (x0, -G / 2)] + [(x0 + px, -G / 2 + py) for px, py in pts]
    bottom = [(-px, -py) for px, py in top]
    return top, bottom, params

# ----------------------------------------------------------------- G e C
def integrate(start, th0, knots_s, knots_k, n=1500):
    L = knots_s[-1]
    s = (np.arange(n) + 0.5) * L / n
    k = np.interp(s, knots_s, knots_k)
    ds = L / n
    th = th0 + np.cumsum(k) * ds
    x = start[0] + np.cumsum(np.cos(th)) * ds
    y = start[1] + np.cumsum(np.sin(th)) * ds
    return [(float(a), float(b)) for a, b in zip(x, y)]

def letter_c(R=54, a0=-50, a1=50):
    """Arco di cerchio aperto a destra, da a0 a a1 gradi passando da sinistra."""
    pts = []
    n = 400
    for i in range(n + 1):
        phi = math.radians(a0 - (360 - (a1 - a0)) * i / n)
        pts.append((R * math.cos(phi), R * math.sin(phi)))
    return pts

def letter_g(R=54, a0=-50, corner_r=9, bar_end=-8):
    """Come la C, ma l'arco prosegue fino a destra, gira in dentro con un raccordo
    morbido e diventa la barra orizzontale (stesso principio delle barre della S)."""
    arc_deg = 360 - 50 - 3                       # dall'alto a destra fino a poco sotto l'orizzontale a destra
    L_arc = R * math.radians(arc_deg)
    # profilo di curvatura del raccordo: da -1/R sale a -1/corner_r e torna a 0.
    # L'area sotto il profilo deve valere 90°: L/4 * (1/R + 2/corner_r) = pi/2
    L_corner = (math.pi / 2) * 4 / (1 / R + 2 / corner_r)
    end_x = R * math.cos(math.radians(3))
    L_bar = end_x - bar_end - corner_r * 0.9
    ks = np.array([0, L_arc * 0.97, L_arc, L_arc + L_corner * 0.5, L_arc + L_corner, L_arc + L_corner + L_bar])
    kk = np.array([-1 / R, -1 / R, -1 / R, -1 / corner_r, 0, 0])   # negativa = antiorario sullo schermo
    start = (R * math.cos(math.radians(a0)), R * math.sin(math.radians(a0)))
    th0 = math.radians(a0) - math.pi / 2         # tangente antioraria
    return integrate(start, th0, ks, kk)

# ----------------------------------------------------------------- utilità svg
def path_d(pts):
    return "M%.2f %.2f" % pts[0] + "".join(" L%.2f %.2f" % p for p in pts[1:])

def bbox(*strokes):
    xs = [p[0] for s in strokes for p in s]; ys = [p[1] for s in strokes for p in s]
    return min(xs), min(ys), max(xs), max(ys)

def svg(strokes, color="#B08A45", pad=8, w=None, extra=""):
    x0, y0, x1, y1 = bbox(*strokes)
    vb = "%.1f %.1f %.1f %.1f" % (x0 - pad, y0 - pad, (x1 - x0) + 2 * pad, (y1 - y0) + 2 * pad)
    attr = ' width="%d"' % w if w else ""
    paths = "".join('<path d="%s"/>' % path_d(s) for s in strokes)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s"%s%s><g fill="none" stroke="%s" stroke-width="%d" stroke-linecap="round" stroke-linejoin="round">%s</g></svg>'
            % (vb, attr, extra, color, STROKE, paths))

def symbol(sid, strokes, pad=8):
    x0, y0, x1, y1 = bbox(*strokes)
    vb = "%.1f %.1f %.1f %.1f" % (x0 - pad, y0 - pad, (x1 - x0) + 2 * pad, (y1 - y0) + 2 * pad)
    paths = "".join('<path class="stroke" d="%s"/>' % path_d(s) for s in strokes)
    ratio = ((x1 - x0) + 2 * pad) / ((y1 - y0) + 2 * pad)
    return '<symbol id="%s" viewBox="%s">%s</symbol>' % (sid, vb, paths), ratio, (x0, y0, x1, y1)

def main():
    os.makedirs(OUT, exist_ok=True)
    top, bottom, params = s_strokes()
    top_c, bottom_c, _ = s_strokes(dict(apex=(40.0, -40.0), trough=(98.0, -4.0), end=(138.0, -12.0), minx=-6.0))
    g = letter_g(); c = letter_c()

    # monogramma: S compatta + G + C, allineati verticalmente sul centro
    sx0, _, sx1, _ = bbox(top_c, bottom_c)
    gap = 26
    gx = sx1 + gap + 54
    cx = gx + 54 + gap + 54
    mono = [top_c, bottom_c, [(x + gx, y) for x, y in g], [(x + cx, y) for x, y in c]]

    files = {
        "s": [top, bottom], "s-compatta": [top_c, bottom_c],
        "g": [g], "c": [c], "sgc": mono,
    }
    syms, ratios = [], {}
    for name, strokes in files.items():
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(svg(strokes))
        s, r, bb = symbol(name, strokes)
        syms.append(s); ratios[name] = r
        print("%-11s %6.1f x %5.1f  rapporto %.3f" % (name, bb[2] - bb[0], bb[3] - bb[1], r))
    # simboli separati per la versione bicolore (barre / baffi)
    bars = [[top[0], top[1]], [bottom[0], bottom[1]]]
    baffi = [top[1:], bottom[1:]]
    x0, y0, x1, y1 = bbox(top, bottom)
    vb = "%.1f %.1f %.1f %.1f" % (x0 - 8, y0 - 8, (x1 - x0) + 16, (y1 - y0) + 16)
    syms.append('<symbol id="s-barre" viewBox="%s">%s</symbol>' % (vb, "".join('<path class="stroke" d="%s"/>' % path_d(s) for s in bars)))
    syms.append('<symbol id="s-baffi" viewBox="%s">%s</symbol>' % (vb, "".join('<path class="stroke" d="%s"/>' % path_d(s) for s in baffi)))
    with open(os.path.join(OUT, "_symbols.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(syms))
    with open(os.path.join(OUT, "_ratios.txt"), "w") as f:
        for k, v in ratios.items():
            f.write("%s %.4f\n" % (k, v))
    print("parametri baffo:", np.round(params, 4))

if __name__ == "__main__":
    main()
