# -*- coding: utf-8 -*-
"""Il 'baffo' della S: la curva che parte dal capo della barra, fa il giro e si stende a onda.

Costruzione: la CURVATURA lungo la curva è una spezzata continua (spirale di Eulero a
tratti, come nel tracciamento di strade e binari). Integrando la curvatura si ottiene
la direzione, integrando la direzione si ottiene la curva: il risultato è continuo con
derivata prima e seconda continue (nessun cambio brusco di direzione né di curvatura).

I valori della curvatura nei nodi vengono ottimizzati perché la curva passi per i punti
misurati sullo schizzo (apice, conca, estremo del baffo) e finisca orizzontale.
"""
import math
import numpy as np
from scipy.optimize import least_squares

# Punti obiettivo misurati sullo schizzo, in unità in cui la distanza fra le barre vale 20.
# Origine = capo sinistro della barra alta; la curva parte verso sinistra (direzione pi).
TARGET = {
    "apex": (44.0, -44.0),     # apice del giro (direzione orizzontale verso destra)
    "trough": (116.0, -4.0),   # conca dopo la discesa (di nuovo orizzontale)
    "end": (180.0, -14.0),     # estremo del baffo (orizzontale)
    "minx": -6.0,              # quanto la curva sporge a sinistra del capo della barra
}

def integrate(knots_s, knots_k, n=1600):
    """Curvatura lineare a tratti definita dai nodi (s, k). Ritorna punti, direzione finale."""
    L = knots_s[-1]
    s = (np.arange(n) + 0.5) * L / n
    k = np.interp(s, knots_s, knots_k)
    ds = L / n
    th = math.pi + np.cumsum(k) * ds
    x = np.cumsum(np.cos(th)) * ds
    y = np.cumsum(np.sin(th)) * ds
    return np.column_stack([x, y]), th[-1], th

def build(params):
    """params -> nodi. Lunghezze dei tratti e valori di curvatura ai nodi interni."""
    Lc, La, Ld, Lt, Lr = params[:5]          # corner, arco, discesa, conca, risalita
    kc, ka, kd, kt, kr = params[5:10]        # curvature ai nodi
    s = [0, Lc * 0.5, Lc, Lc + La, Lc + La + Ld * 0.5, Lc + La + Ld,
         Lc + La + Ld + Lt * 0.5, Lc + La + Ld + Lt, Lc + La + Ld + Lt + Lr * 0.5, Lc + La + Ld + Lt + Lr]
    k = [0, kc, ka, ka, kd, 0, -kt, 0, kr, 0]
    return np.array(s, float), np.array(k, float)

def residuals(params):
    ks, kk = build(params)
    pts, th_end, th = integrate(ks, kk)
    ys = pts[:, 1]
    ai = int(np.argmin(ys)); apex = pts[ai]
    ti = ai + int(np.argmax(ys[ai:])); trough = pts[ti]
    end = pts[-1]
    r = [
        (apex[0] - TARGET["apex"][0]) / 4, (apex[1] - TARGET["apex"][1]) / 4,
        (trough[0] - TARGET["trough"][0]) / 4, (trough[1] - TARGET["trough"][1]) / 4,
        (end[0] - TARGET["end"][0]) / 4, (end[1] - TARGET["end"][1]) / 4,
        (pts[:, 0].min() - TARGET["minx"]) / 3,
        (th_end - 2 * math.pi) * 40,          # deve finire orizzontale (verso destra)
        (th[ai] - 2 * math.pi) * 10,          # all'apice orizzontale
    ]
    return r

def solve():
    x0 = np.array([14, 69, 76, 30, 60, 0.17, 1 / 44, 0.03, 0.02, 0.01])
    lb = np.array([6, 30, 30, 10, 20, 0.02, 0.005, 0.0, 0.0, 0.0])
    ub = np.array([40, 140, 140, 90, 120, 0.6, 0.08, 0.1, 0.1, 0.1])
    res = least_squares(residuals, x0, bounds=(lb, ub), max_nfev=4000)
    return res

def baffo_points(params=None):
    if params is None:
        params = solve().x
    ks, kk = build(params)
    pts, th_end, _ = integrate(ks, kk)
    return [(float(p[0]), float(p[1])) for p in pts], params

if __name__ == "__main__":
    res = solve()
    print("costo", res.cost)
    print("param", np.round(res.x, 4))
    pts, _ = baffo_points(res.x)
    ys = [p[1] for p in pts]; xs = [p[0] for p in pts]
    ai = ys.index(min(ys)); ti = ai + ys[ai:].index(max(ys[ai:]))
    print("apex", [round(v, 1) for v in pts[ai]], "trough", [round(v, 1) for v in pts[ti]], "end", [round(v, 1) for v in pts[-1]], "minx", round(min(xs), 1))
