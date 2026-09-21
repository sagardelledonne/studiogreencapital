# Studio Green Capital — sito web

Sito istituzionale di Studio Green Capital SRL (consulenza energetica strategica per le imprese).
Sostituisce la landing page fatta con Gamma su studiogreencapital.it.

## Com'è fatto
- `build.py` contiene **tutti i testi** delle pagine e genera i file `index.html` (home + 12 pagine interne + 404, sitemap, robots).
- `assets/site.css` e `assets/site.js` sono stile e comportamenti comuni (menu, animazioni, modulo contatti).
- `assets/fonts/` i caratteri Fraunces e Manrope ospitati in locale (niente richieste a Google, ok per la privacy).
- `assets/img/` le foto in WebP.

## Pagine
Home · Chi siamo · Servizi (+ 5 schede: Supply & Procurement, PPA, Produzione & Autoconsumo, Efficienza, Welfare energetico) · Metodo · Risultati · Contatti · Privacy · Cookie

## Come si aggiorna
1. Modifica il testo in `build.py` (o un'immagine in `assets/`).
2. Esegui `python build.py` (rigenera tutte le pagine).
3. Commit e push su `main`: GitHub Pages pubblica da solo (workflow `.github/workflows/pages.yml`).

## Passare al dominio studiogreencapital.it
1. In `build.py` mettere `BASE = ""` e `SITE_URL = "https://www.studiogreencapital.it"`, poi `python build.py`.
2. Creare un file `CNAME` nella radice con dentro `www.studiogreencapital.it`.
3. Nel pannello del dominio (di Roberto) impostare i record DNS:
   - `www` → CNAME → `sagardelledonne.github.io`
   - radice (`@`) → A → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
4. Su GitHub: Settings → Pages → Custom domain → `www.studiogreencapital.it` → spuntare "Enforce HTTPS".

## Da completare
- Email di contatto: ora `info@studiogreencapital.it` (in `build.py` e `assets/site.js`); verificare che esista.
- P.IVA e sede legale nelle pagine Privacy/Cookie (segnaposto `[da inserire]`).
- Logo definitivo (ora un marchio SVG provvisorio in `build.py`, `MARK`).
