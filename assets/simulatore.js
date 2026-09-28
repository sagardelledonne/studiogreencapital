/* Simulatore: cosa cambia per un'impresa che ristruttura i contratti e produce in proprio.
   Prezzi di riferimento dalla serie GME (assets/prezzi.js). Ipotesi dichiarate nella pagina. */
(function () {
  "use strict";
  var root = document.getElementById("sim");
  if (!root) return;

  // ipotesi tecniche, dichiarate sotto il simulatore
  var PROD_KWP = 1200;        // kWh prodotti per kWp all'anno, Nord Italia
  var AUTOCONS = 0.75;        // quota di produzione effettivamente autoconsumata
  var COSTO_KWP = 850;        // € per kWp chiavi in mano
  var SCONTO_CONTRATTO = 0.15; // riduzione del costo unitario sull'energia acquistata
  var MQ_PER_KWP = 7;         // superficie di copertura per kWp

  var el = {};
  ["consumo", "spesa", "superficie"].forEach(function (k) { el[k] = document.getElementById("sim-" + k); });

  function n(v) { return Math.round(v).toLocaleString("it-IT"); }
  function eur(v) { return n(v) + " €"; }

  function calcola() {
    var consumo = Math.max(0.1, parseFloat(el.consumo.value) || 1);       // GWh/anno
    var spesa = Math.max(1, parseFloat(el.spesa.value) || 1) * 1000;      // migliaia € -> €
    var mq = Math.max(0, parseFloat(el.superficie.value) || 0);           // m²

    var mwh = consumo * 1000;
    var unitario = spesa / mwh;                                           // €/MWh oggi

    // impianto: limitato dalla superficie e da quanto serve davvero
    var kwpDaTetto = Math.floor(mq / MQ_PER_KWP);
    var kwpUtile = Math.floor(mwh * 1000 * 0.35 / (PROD_KWP * AUTOCONS)); // copre al più ~35% del fabbisogno
    var kwp = Math.max(0, Math.min(kwpDaTetto, kwpUtile));
    var autoprodotto = kwp * PROD_KWP * AUTOCONS / 1000;                  // MWh autoconsumati
    if (autoprodotto > mwh) autoprodotto = mwh;
    var investimento = kwp * COSTO_KWP;

    var acquistato = mwh - autoprodotto;
    var nuovoUnitario = unitario * (1 - SCONTO_CONTRATTO);
    var nuovaSpesa = acquistato * nuovoUnitario;

    var rispContratto = acquistato * unitario * SCONTO_CONTRATTO;
    var rispAutocons = autoprodotto * unitario;
    var rispTot = spesa - nuovaSpesa;
    var pct = spesa > 0 ? rispTot / spesa * 100 : 0;
    var rientro = rispAutocons > 0 ? investimento / rispAutocons : 0;

    var put = function (id, v) { var x = document.getElementById(id); if (x) x.innerHTML = v; };
    put("sim-unitario", n(unitario) + " <small>€/MWh</small>");
    put("sim-nuovo-unitario", n(nuovoUnitario) + " <small>€/MWh</small>");
    put("sim-spesa-oggi", eur(spesa));
    put("sim-spesa-dopo", eur(nuovaSpesa));
    put("sim-risparmio", eur(rispTot));
    put("sim-pct", "−" + pct.toFixed(0) + "%");
    put("sim-kwp", kwp > 0 ? n(kwp) + " <small>kWp</small>" : "—");
    put("sim-investimento", kwp > 0 ? eur(investimento) : "—");
    put("sim-rientro", kwp > 0 && rientro > 0 ? rientro.toFixed(1).replace(".", ",") + " <small>anni</small>" : "—");
    put("sim-da-contratto", eur(rispContratto));
    put("sim-da-autocons", eur(rispAutocons));

    // la barra: quanto pesa ciascuna leva sul risparmio totale
    var q1 = rispTot > 0 ? rispContratto / rispTot * 100 : 0;
    var b1 = document.getElementById("sim-barra-contratto");
    var b2 = document.getElementById("sim-barra-autocons");
    if (b1 && b2) { b1.style.width = q1.toFixed(1) + "%"; b2.style.width = (100 - q1).toFixed(1) + "%"; }
    var lab = document.getElementById("sim-quote");
    if (lab) lab.textContent = kwp > 0
      ? "Il " + q1.toFixed(0) + "% del risparmio viene dalla struttura contrattuale, il " + (100 - q1).toFixed(0) + "% dall’energia che non comprate più."
      : "Con questa superficie non c’è spazio per un impianto: il risparmio viene tutto dalla struttura contrattuale.";
  }

  ["consumo", "spesa", "superficie"].forEach(function (k) {
    if (el[k]) { el[k].addEventListener("input", calcola); el[k].addEventListener("change", calcola); }
  });
  calcola();
})();
