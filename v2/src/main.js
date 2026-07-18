// main.js — start v2 op en koppelt de HUD aan de lagen.
// Bewust dun: alle logica hoort in de lagen, niet hier.

import { createGlobe, CONFIG } from "./globe.js?v=013";
import { laadVectorWereld } from "./world.js?v=013";
import { createTileLayer } from "./tiles.js?v=013";
import { laadMarnet, laadHavens, zoekRoute, bouwRouteLijn } from "./marnet.js?v=013";

const GLOBE = createGlobe(document.getElementById("canvasWrap"));

// --- satelliettegels -------------------------------------------------------
// Streamt Esri World Imagery op het detailniveau dat bij je kijkhoogte past —
// dezelfde bron als earth3dmap.com. Dit is de SKIN.
const TEGELS = createTileLayer(GLOBE);
GLOBE.onTick((dt) => TEGELS.tick(dt));

// --- de vectorwereld -------------------------------------------------------
// Dit is de WAARHEID: waar land ophoudt en water begint. De tegels mogen mooi
// zijn, maar routering rekent tegen deze lijnen.

let wereldStats = null;
let kustlijn = null;

laadVectorWereld(CONFIG.radius)
  .then(({ lijnen, stats }) => {
    GLOBE.globeGroup.add(lijnen);
    kustlijn = lijnen;
    wereldStats = stats;
    console.log(
      `[atlas v2] vectorwereld: ${stats.punten.toLocaleString("nl")} punten · ` +
      `${stats.ringen.toLocaleString("nl")} vormen · ${stats.kbOverdracht} KB · ` +
      `laden ${stats.msLaden} ms, verwerken ${stats.msVerwerken} ms`
    );
  })
  .catch((e) => console.error("[atlas v2] vectorwereld niet geladen:", e));

// --- het MARNET-netwerk ----------------------------------------------------
// De vaarlanen, éénmalig verzoend met de vectorwereld hierboven (LAR-483).
// Routeren = A* over deze graaf; de route-test hieronder bewijst dat.

let NET = null;
let HAVENS = null;
let netStats = null;
let routeLijn = null;

Promise.all([laadMarnet(CONFIG.radius), laadHavens()])
  .then(([net, havens]) => {
    NET = net;
    HAVENS = havens;
    netStats = net.stats;
    GLOBE.globeGroup.add(net.lijnen);
    vulHavenLijst(havens);
    console.log(
      `[atlas v2] marnet: ${net.stats.knopen.toLocaleString("nl")} knopen · ` +
      `${net.stats.edges.toLocaleString("nl")} edges · ${net.stats.punten.toLocaleString("nl")} punten · ` +
      `${net.stats.kbOverdracht} KB · laden ${net.stats.msLaden} ms, verwerken ${net.stats.msVerwerken} ms · ` +
      `${havens.length.toLocaleString("nl")} havens`
    );
    window.MARNET = net; // diagnose-handvat, net als GLOBE/TEGELS
  })
  .catch((e) => console.error("[atlas v2] marnet niet geladen:", e));

// De vectorlagen liggen precies OP de bol. Om te voorkomen dat ze half in het
// oppervlak verdwijnen, tillen we ze elke frame een klein beetje op — evenredig
// met de kijkhoogte. Elke laag z'n eigen plank: kustlijn onder, netwerk erboven,
// de gevonden route bovenop.
GLOBE.onTick(() => {
  const alt = GLOBE.getAltitude();
  if (kustlijn) {
    const op = Math.max(CONFIG.radius * 2e-6, alt * 0.004);
    kustlijn.scale.setScalar(1 + op / CONFIG.radius);
  }
  if (NET) {
    const op = Math.max(CONFIG.radius * 3e-6, alt * 0.005);
    NET.lijnen.scale.setScalar(1 + op / CONFIG.radius);
  }
  if (routeLijn) {
    const op = Math.max(CONFIG.radius * 4e-6, alt * 0.006);
    routeLijn.scale.setScalar(1 + op / CONFIG.radius);
  }
});

// --- route testen (haven → haven) ------------------------------------------

const vanEl = document.getElementById("vanHaven");
const naarEl = document.getElementById("naarHaven");
const infoEl = document.getElementById("routeInfo");

function havenLabel(h) {
  return `${h.naam} (${h.land})`;
}

function vulHavenLijst(havens) {
  const lijst = document.getElementById("havenLijst");
  const frag = document.createDocumentFragment();
  for (const h of havens) {
    const opt = document.createElement("option");
    opt.value = havenLabel(h);
    frag.appendChild(opt);
  }
  lijst.appendChild(frag);
}

function vindHaven(tekst) {
  if (!HAVENS || !tekst) return null;
  const t = tekst.trim().toLowerCase();
  return (
    HAVENS.find((h) => havenLabel(h).toLowerCase() === t) ||
    HAVENS.find((h) => h.naam.toLowerCase() === t) ||
    HAVENS.find((h) => h.naam.toLowerCase().startsWith(t)) ||
    null
  );
}

function gcKmLL(lon1, lat1, lon2, lat2) {
  const r = Math.PI / 180;
  const d = Math.sin(lat1 * r) * Math.sin(lat2 * r) +
    Math.cos(lat1 * r) * Math.cos(lat2 * r) * Math.cos((lon2 - lon1) * r);
  return 6371 * Math.acos(Math.max(-1, Math.min(1, d)));
}

function wisRoute() {
  if (routeLijn) {
    GLOBE.globeGroup.remove(routeLijn);
    routeLijn.traverse?.((o) => o.geometry?.dispose());
    routeLijn = null;
  }
  infoEl.innerHTML = "";
}

function toonRoute() {
  if (!NET || !HAVENS) {
    infoEl.textContent = "netwerk laadt nog…";
    return;
  }
  const van = vindHaven(vanEl.value);
  const naar = vindHaven(naarEl.value);
  if (!van || !naar) {
    infoEl.textContent = "kies twee havens uit de lijst";
    return;
  }
  wisRoute();

  const t0 = performance.now();
  const route = zoekRoute(NET, van.knoop, naar.knoop);
  const ms = performance.now() - t0;
  if (!route) {
    infoEl.textContent = `geen pad gevonden (${havenLabel(van)} → ${havenLabel(naar)})`;
    return;
  }

  // haven → dichtstbijzijnde-knoop-aanlopen als kort recht stuk erbij
  routeLijn = bouwRouteLijn(NET, route, CONFIG.radius,
    [[van.lon, van.lat]], [[naar.lon, naar.lat]]);
  GLOBE.globeGroup.add(routeLijn);

  const aanloop = van.afstandKm + naar.afstandKm;
  const totaal = route.km + aanloop;
  const binnen = route.edges.filter((e) => NET.edgeSoort[e] === 1).length;
  const passages = [...new Set(route.edges.map((e) => NET.edgeLabel[e]).filter(Boolean))];
  infoEl.innerHTML =
    `<b>${Math.round(totaal).toLocaleString("nl")} km</b> · ` +
    `${route.edges.length} edges · ${ms.toFixed(0)} ms` +
    (binnen ? ` · ${binnen} binnenwater` : "") +
    (aanloop > 20 ? ` · aanloop ${Math.round(aanloop)} km` : "") +
    (passages.length ? `<br>via ${passages.join(" · ")}` : "");
  window.ROUTE = route; // diagnose
}

document.getElementById("routeGo").addEventListener("click", toonRoute);
document.getElementById("routeWis").addEventListener("click", wisRoute);
for (const el of [vanEl, naarEl]) {
  el.addEventListener("keydown", (e) => { if (e.key === "Enter") toonRoute(); });
}

// --- HUD -------------------------------------------------------------------

function wireButtons(selector, attr, apply) {
  const btns = [...document.querySelectorAll(selector)];
  for (const btn of btns) {
    btn.addEventListener("click", () => {
      btns.forEach((b) => b.classList.remove("is-on"));
      btn.classList.add("is-on");
      apply(btn.dataset[attr]);
    });
  }
}

wireButtons(".tmBtn", "tm", (mode) => GLOBE.setToneMapping(mode));
wireButtons(".sunBtn", "sun", (mode) => GLOBE.setSun(mode));
wireButtons(".clBtn", "cl", (mode) => {
  if (kustlijn) kustlijn.visible = (mode === "aan");
});
wireButtons(".mnBtn", "mn", (mode) => {
  if (NET) NET.lijnen.visible = (mode === "aan");
});

wireButtons(".bmBtn", "bm", (mode) => {
  if (mode === "egaal") {
    TEGELS.zetAan(false);
    GLOBE.setBasemap("vector");
  } else {
    TEGELS.zetAan(true);
    TEGELS.zetBron(mode);          // "satelliet" of "kaart"
    GLOBE.setBasemap("satelliet"); // ondergrond onder de tegels
  }
  document.getElementById("attrib").textContent = TEGELS.isAan() ? TEGELS.attributie() : "";
});

document.getElementById("zoomIn").addEventListener("click", () => GLOBE.zoomBy(1 / 1.35));
document.getElementById("zoomOut").addEventListener("click", () => GLOBE.zoomBy(1.35));

document.getElementById("attrib").textContent = TEGELS.attributie();

// --- statusregel -----------------------------------------------------------

const statsEl = document.getElementById("stats");
statsEl.style.whiteSpace = "pre-line";

GLOBE.onTick(() => {
  const s = GLOBE.getStats();
  const t = TEGELS.stats();
  const km = GLOBE.getAltitudeKm();
  const hoogte = km >= 10 ? `${Math.round(km).toLocaleString("nl")} km` : `${km.toFixed(1)} km`;

  let tekst =
    `${s.fps} fps · hoogte ${hoogte}\n` +
    `${s.calls} draw calls · tegels z${t.detailZ} (${t.tegelsInBeeld})`;
  if (wereldStats) {
    tekst += `\n${(wereldStats.punten / 1000).toFixed(0)}k vectorpunten · ${wereldStats.kbOverdracht} KB`;
  }
  if (netStats) {
    tekst += `\nmarnet ${(netStats.punten / 1000).toFixed(0)}k punten · ${netStats.kbOverdracht} KB`;
  }
  if (t.mislukt) tekst += `\n${t.mislukt} tegels mislukt`;
  statsEl.textContent = tekst;
});

// Handvat voor diagnose vanuit de console/devtools. Dit project wordt veel
// visueel geverifieerd; zonder globals is er anders geen enkele manier om de
// scene van buitenaf te bevragen (ES-modules hebben geen window-scope).
window.GLOBE = GLOBE;
window.TEGELS = TEGELS;

console.log("[atlas v2] three r185 · ACES · tegels tot z19 · zoom tot ~1 km · marnet-zeeroutes");
