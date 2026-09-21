/* Studio Green Capital — comportamenti comuni */
(function () {
  "use strict";
  var CONTACT_EMAIL = "info@studiogreencapital.it";

  // Header: diventa pieno dopo lo scroll, si nasconde scendendo, riappare salendo
  var top = document.getElementById("top");
  var lastY = 0;
  function onScroll() {
    var y = window.scrollY || 0;
    if (top) {
      top.classList.toggle("solid", y > 40);
      top.classList.toggle("hide", y > 400 && y > lastY + 4);
    }
    lastY = y;
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Menu mobile
  var menu = document.getElementById("menu");
  var burger = document.getElementById("burger");
  var closeBtn = document.getElementById("menuClose");
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (burger) burger.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) closeBtn && closeBtn.focus(); else burger && burger.focus();
  }
  burger && burger.addEventListener("click", function () { setMenu(true); });
  closeBtn && closeBtn.addEventListener("click", function () { setMenu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
  menu && menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });

  // Comparsa degli elementi allo scroll
  var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
    });
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.08 }) : null;
  document.querySelectorAll(".rv").forEach(function (el) { io ? io.observe(el) : el.classList.add("in"); });

  // Numeri che contano
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    var dec = (el.getAttribute("data-dec") || "0") | 0;
    if (reduce || isNaN(target)) { el.firstChild.nodeValue = prefix + target.toFixed(dec).replace(".", ",") + suffix; return; }
    var start = null, dur = 1600;
    function frame(t) {
      if (!start) start = t;
      var p = Math.min(1, (t - start) / dur);
      var e = 1 - Math.pow(1 - p, 3);
      el.firstChild.nodeValue = prefix + (target * e).toFixed(dec).replace(".", ",") + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  var cio = ("IntersectionObserver" in window) ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); } });
  }, { threshold: 0.5 }) : null;
  document.querySelectorAll("[data-count]").forEach(function (el) { cio ? cio.observe(el) : animateCount(el); });

  // Modulo contatti: apre la posta con la richiesta già compilata
  var form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements;
      var NL = "\n";
      var lines = [
        "Richiesta di valutazione energetica dal sito studiogreencapital.it", "",
        "Azienda: " + f.azienda.value,
        "Referente: " + f.nome.value,
        "Email: " + f.email.value,
        "Telefono: " + (f.telefono.value || "-"),
        "Settore: " + (f.settore.value || "-"),
        "Consumo annuo indicativo: " + (f.consumo.value || "-"), "",
        "Messaggio:", f.messaggio.value || "-"
      ];
      var subject = "Richiesta valutazione — " + f.azienda.value;
      window.location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join(NL));
      var sent = document.getElementById("formSent");
      if (sent) sent.textContent = "Si apre il tuo programma di posta con la richiesta già pronta: basta premere Invia. Se non si apre, scrivi direttamente a " + CONTACT_EMAIL + ".";
    });
  }

  // Anno nel footer
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
