# Studio Green Capital — sito web

Sito istituzionale di Studio Green Capital SRL (consulenza energetica strategica per le imprese).
Sostituisce la landing page fatta con Gamma su studiogreencapital.it.

Cartella di lavoro: `Desktop\lavoro\Studio Green Capital\` — accanto a `Logo\`, che contiene il materiale di brand originale.

## Identità visiva (dal materiale ufficiale in `..\Logo\`)
- **Logo**: `Studio_Green_Capital_Logo_Ufficiale_bassa.png`. Da questo sono derivati, in `assets/img/`:
  `logo.webp` (a colori), `logo-chiaro.webp` (monocromatico crema, per fondi scuri),
  `simbolo.webp` / `simbolo-chiaro.webp` (solo l'emblema, usato nell'intestazione), `og.png` (anteprima social).
- **Payoff**: *Energy, Land, People*.
- **Colori**: verde scuro `#03352A`, verde lime `#B2CF49` (l'arco del logo), verde oliva `#4F6228` (testi della carta intestata).
- **Carattere**: Open Sans (lo stesso della carta intestata), ospitato in locale in `assets/fonts/`.
- **Dati**: C.F. e P.IVA 04755500164 · REA MI-2807171 · Via Mauro Macchi, 8 — 20124 Milano (MI) · PEC green-capital-srl@pec.it

## Com'è fatto
- `build.py` contiene **tutti i testi** e genera i file `index.html` (home + 12 pagine interne + 404, sitemap, robots).
- `assets/site.css` e `assets/site.js` sono stile e comportamenti comuni (menu, animazioni, modulo contatti).
- `logo/` sono gli script Python usati per le prime proposte di marchio: materiale di lavoro, non pubblicato.

## Pagine
Home · Chi siamo · Servizi (+ 5 schede: Supply & Procurement, PPA, Produzione & Autoconsumo, Efficienza, Welfare energetico) · Metodo · Risultati · Contatti · Privacy · Cookie

## Come si aggiorna
1. Modifica il testo in `build.py` (o un'immagine in `assets/`).
2. Esegui `python build.py` (rigenera tutte le pagine).
3. Commit e push su `main`: GitHub Pages pubblica da solo (workflow `.github/workflows/pages.yml`).

Anteprima locale: il sito è generato per l'indirizzo `/studiogreencapital/`, quindi va servita la cartella **padre** e aperto `http://localhost:PORTA/studiogreencapital/`.

## Passare al dominio studiogreencapital.it
1. In `build.py` mettere `BASE = ""` e `SITE_URL = "https://www.studiogreencapital.it"`, poi `python build.py`.
2. Creare un file `CNAME` nella radice con dentro `www.studiogreencapital.it`.
3. Nel pannello del dominio (di Roberto) impostare i record DNS:
   - `www` → CNAME → `sagardelledonne.github.io`
   - radice (`@`) → A → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
4. Su GitHub: Settings → Pages → Custom domain → `www.studiogreencapital.it` → spuntare "Enforce HTTPS".

## Da confermare
- **Email ordinaria**: nel sito c'è `info@studiogreencapital.it` come segnaposto (in `build.py` e `assets/site.js`). Sul materiale ufficiale compare solo la PEC.
- `greencapital.srl` sulla carta intestata: sembra un profilo social, non è stato inserito perché non è chiaro quale.
