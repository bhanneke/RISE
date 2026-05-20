// GoatCounter — privacy-friendly, free-for-OSS page analytics.
//
// SETUP (one-time):
//   1. Register a free OSS account at https://www.goatcounter.com/signup
//      (pick a subdomain, e.g. "rise-kb" → https://rise-kb.goatcounter.com).
//   2. Replace the placeholder "RISE_SUBDOMAIN" below with that subdomain.
//   3. Commit & push. GitHub Pages will pick it up on the next build.
//
// After a day or two of traffic, visit your dashboard at
// https://<subdomain>.goatcounter.com/ for per-page view counts.
// To surface "trending" skills inside the site itself, run
// scripts/fetch_goatcounter_stats.py periodically and the build
// pipeline will mark high-traffic skills.

(function () {
  var SUBDOMAIN = "RISE_SUBDOMAIN"; // <-- replace this string
  if (SUBDOMAIN === "RISE_SUBDOMAIN") return; // not configured yet — do nothing
  var s = document.createElement("script");
  s.setAttribute("data-goatcounter", "https://" + SUBDOMAIN + ".goatcounter.com/count");
  s.async = true;
  s.src = "//gc.zgo.at/count.js";
  document.head.appendChild(s);
})();
