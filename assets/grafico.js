/* Grafico dei prezzi all'ingrosso di energia elettrica e gas — dati mensili GME.
   I dati arrivano da assets/prezzi.js (window.PREZZI), generato da build.py. */
(function () {
  "use strict";
  var D = window.PREZZI;
  var root = document.getElementById("grafico");
  if (!D || !root) return;

  var MESI = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"];
  var NS = "http://www.w3.org/2000/svg";
  var COL = { el: "#0B4130", gas: "#B5791C" };
  // su schermi stretti il grafico diventa più verticale, altrimenti è illeggibile
  var W = 1000, H = 420, ML = 54, MR = 16, MT = 24, MB = 46;
  function misura() {
    var w = root.clientWidth || 1000;
    if (w < 560) { W = 420; H = 460; ML = 46; MT = 20; MB = 42; }
    else if (w < 860) { W = 700; H = 430; ML = 50; MT = 22; MB = 44; }
    else { W = 1000; H = 420; ML = 54; MT = 24; MB = 46; }
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
  }

  var stato = { anni: 10, serie: { el: true, gas: true }, i: null };

  function el(tag, attrs, testo) {
    var n = document.createElementNS(NS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (testo != null) n.textContent = testo;
    return n;
  }
  function etichetta(ym, lunga) {
    var m = MESI[+ym.slice(4) - 1];
    return lunga ? m + " " + ym.slice(0, 4) : m + " ’" + ym.slice(2, 4);
  }
  function euro(v, dec) {
    return v.toLocaleString("it-IT", { minimumFractionDigits: dec == null ? 0 : dec, maximumFractionDigits: dec == null ? 0 : dec });
  }

  function finestra() {
    var n = Math.min(stato.anni * 12, D.mesi.length);
    var da = D.mesi.length - n;
    return {
      mesi: D.mesi.slice(da), el: D.elettricita.slice(da), gas: D.gas.slice(da), da: da
    };
  }

  var svg = el("svg", { viewBox: "0 0 " + W + " " + H, class: "gr-svg", role: "img" });
  svg.setAttribute("aria-label", "Prezzo medio mensile dell’energia elettrica e del gas all’ingrosso in Italia, in euro per megawattora");
  var gGrid = el("g", {}), gSerie = el("g", {}), gHover = el("g", { class: "gr-hover" });
  svg.appendChild(gGrid); svg.appendChild(gSerie); svg.appendChild(gHover);

  function disegna() {
    misura();
    var f = finestra(), n = f.mesi.length;
    var vis = [];
    if (stato.serie.el) vis = vis.concat(f.el);
    if (stato.serie.gas) vis = vis.concat(f.gas);
    if (!vis.length) vis = [0, 100];
    var vmax = Math.max.apply(null, vis);
    var passo = vmax > 400 ? 100 : vmax > 200 ? 50 : vmax > 100 ? 25 : 10;
    var top = Math.ceil(vmax / passo) * passo;

    var x = function (i) { return ML + (n === 1 ? 0 : i * (W - ML - MR) / (n - 1)); };
    var y = function (v) { return MT + (H - MT - MB) * (1 - v / top); };

    // griglia
    gGrid.textContent = "";
    for (var v = 0; v <= top; v += passo) {
      gGrid.appendChild(el("line", { x1: ML, x2: W - MR, y1: y(v), y2: y(v), class: "gr-grid" }));
      gGrid.appendChild(el("text", { x: ML - 10, y: y(v) + 4, class: "gr-lbl", "text-anchor": "end" }, euro(v)));
    }
    // etichette anni: gennaio di ogni anno (o ogni 2 anni se la finestra è lunga)
    var ogni = (W < 560 ? (n > 72 ? 3 : n > 36 ? 2 : 1) : (n > 72 ? 2 : 1)), ultimo = -1;
    for (var i = 0; i < n; i++) {
      var ym = f.mesi[i];
      if (ym.slice(4) !== "01") continue;
      var anno = +ym.slice(0, 4);
      if (ultimo >= 0 && anno - ultimo < ogni) continue;
      ultimo = anno;
      gGrid.appendChild(el("line", { x1: x(i), x2: x(i), y1: MT, y2: H - MB, class: "gr-tick" }));
      gGrid.appendChild(el("text", { x: x(i), y: H - MB + 22, class: "gr-lbl", "text-anchor": "middle" }, anno));
    }
    gGrid.appendChild(el("line", { x1: ML, x2: W - MR, y1: y(0), y2: y(0), class: "gr-axis" }));

    // serie
    gSerie.textContent = "";
    [["gas", f.gas], ["el", f.el]].forEach(function (s) {
      if (!stato.serie[s[0]]) return;
      var d = s[1].map(function (v, i) { return (i ? "L" : "M") + x(i).toFixed(1) + " " + y(v).toFixed(1); }).join(" ");
      var area = d + " L" + x(n - 1).toFixed(1) + " " + y(0) + " L" + x(0).toFixed(1) + " " + y(0) + " Z";
      gSerie.appendChild(el("path", { d: area, class: "gr-area gr-area-" + s[0] }));
      gSerie.appendChild(el("path", { d: d, class: "gr-line gr-line-" + s[0] }));
    });

    // picco assoluto della finestra (sulla serie elettrica, se visibile)
    if (stato.serie.el) {
      var im = f.el.indexOf(Math.max.apply(null, f.el));
      gSerie.appendChild(el("circle", { cx: x(im), cy: y(f.el[im]), r: 4.5, class: "gr-peak" }));
      var ancora = im > n * 0.7 ? "end" : "start";
      gSerie.appendChild(el("text", {
        x: x(im) + (ancora === "end" ? -12 : 12), y: y(f.el[im]) + 5, class: "gr-peak-lbl", "text-anchor": ancora
      }, W < 560 ? euro(f.el[im]) + " €/MWh" : euro(f.el[im]) + " €/MWh · " + etichetta(f.mesi[im], true)));
    }

    disegnaHover(f, x, y);
    aggiornaSintesi(f);
  }

  var tip = document.getElementById("gr-tip");
  function disegnaHover(f, x, y) {
    gHover.textContent = "";
    if (stato.i == null || stato.i >= f.mesi.length) { if (tip) tip.hidden = true; return; }
    var i = stato.i;
    gHover.appendChild(el("line", { x1: x(i), x2: x(i), y1: MT, y2: H - MB, class: "gr-cursor" }));
    if (stato.serie.el) gHover.appendChild(el("circle", { cx: x(i), cy: y(f.el[i]), r: 5, class: "gr-dot gr-dot-el" }));
    if (stato.serie.gas) gHover.appendChild(el("circle", { cx: x(i), cy: y(f.gas[i]), r: 5, class: "gr-dot gr-dot-gas" }));
    if (!tip) return;
    var righe = "";
    if (stato.serie.el) righe += '<span class="gr-k"><i style="background:' + COL.el + '"></i>Elettricità</span><b>' + euro(f.el[i], 2) + " €/MWh</b>";
    if (stato.serie.gas) righe += '<span class="gr-k"><i style="background:' + COL.gas + '"></i>Gas</span><b>' + euro(f.gas[i], 2) + " €/MWh</b>";
    tip.innerHTML = "<strong>" + etichetta(f.mesi[i], true) + "</strong><div class='gr-tip-g'>" + righe + "</div>";
    tip.hidden = false;
    var r = svg.getBoundingClientRect();
    var px = r.left + (x(i) / W) * r.width - svg.parentNode.getBoundingClientRect().left;
    var max = svg.parentNode.clientWidth - tip.offsetWidth - 8;
    tip.style.left = Math.max(8, Math.min(px - tip.offsetWidth / 2, max)) + "px";
  }

  function indiceDaEvento(e) {
    var f = finestra(), r = svg.getBoundingClientRect();
    var cx = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
    var u = (cx / r.width) * W;
    var i = Math.round((u - ML) / ((W - ML - MR) / (f.mesi.length - 1)));
    return Math.max(0, Math.min(f.mesi.length - 1, i));
  }
  function muovi(e) { stato.i = indiceDaEvento(e); var f = finestra(); disegnaHover(f, function (i) { return ML + i * (W - ML - MR) / (f.mesi.length - 1); }, yCorrente(f)); }
  function yCorrente(f) {
    var vis = []; if (stato.serie.el) vis = vis.concat(f.el); if (stato.serie.gas) vis = vis.concat(f.gas);
    var vmax = Math.max.apply(null, vis.length ? vis : [100]);
    var passo = vmax > 400 ? 100 : vmax > 200 ? 50 : vmax > 100 ? 25 : 10;
    var top = Math.ceil(vmax / passo) * passo;
    return function (v) { return MT + (H - MT - MB) * (1 - v / top); };
  }
  svg.addEventListener("mousemove", muovi);
  svg.addEventListener("touchstart", function (e) { muovi(e); }, { passive: true });
  svg.addEventListener("touchmove", function (e) { muovi(e); }, { passive: true });
  svg.addEventListener("mouseleave", function () { stato.i = null; disegna(); });

  /* ---- sintesi sotto il grafico: minimo, massimo, oggi, impatto in bolletta ---- */
  var consumoGWh = 5;
  function aggiornaSintesi(f) {
    var e = f.el, g = f.gas;
    var min = Math.min.apply(null, e), max = Math.max.apply(null, e), oggi = e[e.length - 1];
    var imin = e.indexOf(min), imax = e.indexOf(max);
    var put = function (id, v) { var n = document.getElementById(id); if (n) n.innerHTML = v; };
    put("gr-min", euro(min, 0) + " <small>€/MWh</small>");
    put("gr-min-m", etichetta(f.mesi[imin], true));
    put("gr-max", euro(max, 0) + " <small>€/MWh</small>");
    put("gr-max-m", etichetta(f.mesi[imax], true));
    put("gr-oggi", euro(oggi, 0) + " <small>€/MWh</small>");
    put("gr-oggi-m", etichetta(f.mesi[f.mesi.length - 1], true));
    put("gr-volt", (max / min).toFixed(0) + "<small>×</small>");
    // impatto: differenza fra il mese più caro e il più economico, su un anno di consumo
    var delta = (max - min) * consumoGWh * 1000;
    put("gr-impatto", euro(Math.round(delta / 1000) * 1000, 0) + " €");
    var gmin = Math.min.apply(null, g), gmax = Math.max.apply(null, g);
    put("gr-gas-range", euro(gmin, 0) + "–" + euro(gmax, 0) + " €/MWh");
  }

  /* ---- comandi ---- */
  root.querySelectorAll("[data-anni]").forEach(function (b) {
    b.addEventListener("click", function () {
      stato.anni = +b.dataset.anni; stato.i = null;
      root.querySelectorAll("[data-anni]").forEach(function (o) { o.setAttribute("aria-pressed", o === b); });
      disegna();
    });
  });
  root.querySelectorAll("[data-serie]").forEach(function (b) {
    b.addEventListener("click", function () {
      var k = b.dataset.serie;
      if (stato.serie[k] && !(stato.serie.el && stato.serie.gas)) return;   // almeno una accesa
      stato.serie[k] = !stato.serie[k];
      b.setAttribute("aria-pressed", stato.serie[k]);
      disegna();
    });
  });
  var slider = document.getElementById("gr-consumo");
  if (slider) {
    slider.addEventListener("input", function () {
      consumoGWh = +slider.value;
      var l = document.getElementById("gr-consumo-v");
      if (l) l.textContent = consumoGWh.toLocaleString("it-IT") + " GWh";
      aggiornaSintesi(finestra());
    });
  }

  root.querySelector(".gr-plot").appendChild(svg);
  disegna();
  var tRes;
  window.addEventListener("resize", function () {
    clearTimeout(tRes);
    tRes = setTimeout(function () { stato.i = null; disegna(); }, 150);
  });
})();
