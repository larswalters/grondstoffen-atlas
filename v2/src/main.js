// main.js — start v2 op en koppelt de HUD aan de lagen.
// Bewust dun: alle logica hoort in de lagen, niet hier.

import { createGlobe, CONFIG } from "./globe.js?v=042";
import { laadVectorWereld } from "./world.js?v=042";
import { createTileLayer } from "./tiles.js?v=042";
import { laadMarnet, laadHavens, zoekRoute, zoekRouteRealistisch, bouwRouteLijn }
  from "./marnet.js?v=042";
import { bouwHavenLaag, zetHavenGrootte, koppelHavenLabel } from "./havens.js?v=042";

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
let HAVENLAAG = null;
let netStats = null;
let routeLijn = null;

Promise.all([laadMarnet(CONFIG.radius), laadHavens()])
  .then(([net, havens]) => {
    NET = net;
    HAVENS = havens;
    netStats = net.stats;
    GLOBE.globeGroup.add(net.lijnen);

    // --- de havens als zichtbare laag (LAR-518) ---------------------------
    // Bewust hier en niet in een eigen Promise: het is dezelfde array die de
    // route-test gebruikt, dus er is per constructie één bron voor de havens.
    HAVENLAAG = bouwHavenLaag(havens, CONFIG.radius);
    GLOBE.globeGroup.add(HAVENLAAG.punten);
    // De route-test biedt alleen havens aan die aan water liggen: een punt dat
    // geen enkel net raakt kan per definitie geen route dragen, en dan is
    // "geen pad" een verwarrend antwoord op een vraag die niet gesteld had
    // moeten kunnen worden.
    vulHavenLijst(HAVENLAAG.getoond);
    // `HAVENLAAG.getoond` en niet `havens`: de laag tekent alleen wat aan water
    // ligt, en het label moet per constructie dezelfde lijst gebruiken.
    koppelHavenLabel(GLOBE, HAVENLAAG, HAVENLAAG.getoond, document.getElementById("havenLabel"));
    window.HAVENLAAG = HAVENLAAG;   // diagnose-handvat, net als MARNET/HAVENS
    const hs = HAVENLAAG.stats;
    console.log(
      `[atlas v2] havens: ${hs.havens.toLocaleString("nl")} getoond van ${hs.bron.toLocaleString("nl")} · ` +
      `${hs.verborgen.toLocaleString("nl")} verborgen (>${hs.aanWaterKm} km van kust/meer/rivier) · ` +
      `zee+rivier ${hs.beide.toLocaleString("nl")} · alleen zee ${hs.zee.toLocaleString("nl")} · ` +
      `alleen rivier ${hs.rivier.toLocaleString("nl")} · geen net <${hs.raaktKm} km ${hs.los.toLocaleString("nl")}`
    );
    document.getElementById("havenNoot").textContent =
      `${hs.havens.toLocaleString("nl")} van ${hs.bron.toLocaleString("nl")} getoond — ` +
      `${hs.verborgen.toLocaleString("nl")} liggen >${hs.aanWaterKm} km van kust, meer of rivier`;

    console.log(
      `[atlas v2] marnet: ${net.stats.knopen.toLocaleString("nl")} knopen · ` +
      `${net.stats.edges.toLocaleString("nl")} edges · ${net.stats.punten.toLocaleString("nl")} punten · ` +
      `${net.stats.kbOverdracht} KB · laden ${net.stats.msLaden} ms, verwerken ${net.stats.msVerwerken} ms · ` +
      `${havens.length.toLocaleString("nl")} havens`
    );
    window.MARNET = net;       // diagnose-handvat, net als GLOBE/TEGELS
    window.HAVENS = havens;    // idem — de acceptatietests van LAR-486 rijden hierop
    window.zoekRoute = zoekRoute;
    // De acceptatie van LAR-514 meet in het DEFAULT-profiel, en dat is
    // zoekRouteRealistisch — niet zoekRoute. Zonder dit handvat kan een
    // headless test alleen het permissieve profiel meten, en dat geeft bewust
    // andere getallen (R'dam→Constanța 3.291 i.p.v. 6.285 over zee).
    window.zoekRouteRealistisch = zoekRouteRealistisch;
    zetAttrib();               // vaarweg-data draagt een eigen bronvermelding (ODbL)
  })
  .catch((e) => console.error("[atlas v2] marnet niet geladen:", e));

// De losse bulklaag (LAR-515) is hier weg sinds het binnenwater ÉÉN net met de
// graaf werd: die 374.342 km zitten nu in NET zelf, met de maten per lijn.
// `marnet-bulk.json` wordt niet meer gebakken, dus de fetch gaf bij elke load
// een 404 en de HUD-knop schakelde een laag die niet bestond. `laadBulk()` blijft
// in marnet.js staan voor het geval de tekenlaag ooit terugkomt.

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
  if (HAVENLAAG) {
    // Bovenop alles: een haven mag nooit onder een lijn verdwijnen.
    const op = Math.max(CONFIG.radius * 5e-6, alt * 0.007);
    HAVENLAAG.punten.scale.setScalar(1 + op / CONFIG.radius);
    zetHavenGrootte(HAVENLAAG, GLOBE.getAltitudeKm(), GLOBE.renderer.getPixelRatio());
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
  let route = null;
  let modus = "";
  const schip = SCHEEPSKLASSEN[klasseEl.value] || null;
  const opties = schip ? { schip } : {};
  if (SCHIP === "alles") {
    route = zoekRoute(NET, van.knoop, naar.knoop, opties);
  } else {
    const uit = zoekRouteRealistisch(NET, van.knoop, naar.knoop, opties);
    if (uit) { route = uit.route; modus = uit.modus; }
  }
  const ms = performance.now() - t0;
  if (!route) {
    // Bij een maatfilter is "geen pad" meestal geen bug maar het antwoord —
    // zeg er dus bij wélk schip niet paste, anders lijkt het een storing.
    infoEl.textContent = schip
      ? `geen pad voor klasse ${klasseEl.value} (${havenLabel(van)} → ${havenLabel(naar)}) — te groot voor een poort onderweg`
      : `geen pad gevonden (${havenLabel(van)} → ${havenLabel(naar)})`;
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
    (modus ? `${modus} · ` : "") +
    `${route.edges.length} edges · ${ms.toFixed(0)} ms` +
    (schip ? ` · klasse ${klasseEl.value}` : "") +
    (binnen ? ` · ${binnen} binnenwater` : "") +
    (aanloop > 20 ? ` · aanloop ${Math.round(aanloop)} km` : "") +
    (passages.length ? `<br>via ${passages.join(" · ")}` : "");
  window.ROUTE = route; // diagnose
}

// Default = "echt" (LAR-494, op Lars' regel): eerst als zeeschip proberen, en
// alleen als een uiteinde in het binnenland ligt de binnenvaartsystemen
// openzetten die vanaf dát uiteinde bereikbaar zijn. "alles" laat het oude
// permissieve gedrag zien — handig om de Rijn-Donau-corridor te inspecteren,
// maar dan vaart er dus een zeeschip door sluizen van klasse Vb.
let SCHIP = "echt";

// Scheepsklassen voor het maatfilter (LAR-514). Dezelfde CEMT-presets als de
// baker gebruikt (ECMT Res. 92/2, 1992) — daar staan ze als bron van waarheid,
// hier alleen om een schip mee te BESCHRIJVEN. Doorvaarthoogte staat er bewust
// niet in: die volgt niet uit de klasse (de tabel geeft alternatieven waaruit
// de beheerder kiest), dus een waarde hier zou een verzinsel zijn.
const SCHEEPSKLASSEN = {
  IV:  { lengte: 85,  breedte: 9.5,  diepgang: 2.80 },
  Va:  { lengte: 110, breedte: 11.4, diepgang: 4.50 },
  Vb:  { lengte: 185, breedte: 11.4, diepgang: 4.50 },
  VIb: { lengte: 195, breedte: 22.8, diepgang: 4.50 },
  VIc: { lengte: 280, breedte: 22.8, diepgang: 4.00 },
  VII: { lengte: 285, breedte: 34.2, diepgang: 4.50 },
  // VS-duwkonvooi — GEEN CEMT-klasse, en dat is precies het punt: op de Ohio en
  // de Mississippi vaart geen Europees schip maar een Amerikaanse duwbak.
  // Standaard jumbo hopper barge = 195 x 35 ft, 9 ft diepgang bij ~1.500 ton.
  // Een cut van 3 breed x 3 lang is wat één schutting op een 600x110 ft-kolk
  // neemt: 3 x 35 = 105 ft (32,0 m) en 3 x 195 = 585 ft (178,3 m).
  //
  // ⚠️ Let op hoe exact dat past — de Amerikaanse vloot is OP de sluis
  // ontworpen. Dat is meteen een onafhankelijke bevestiging van de kolkmaten
  // die uit USACE kwamen: de vaarweg-maten en de scheeps-maten passen als
  // sleutel op slot. Zonder deze klasse sloot de Ohio voor élk schip in de
  // HUD, want zelfs CEMT-klasse IV steekt 2,80 m tegen de 2,7432 m die USACE
  // toestaat — fysiek juist, maar het beschreef een schip dat daar nooit vaart.
  "VS-tow": { lengte: 178.3, breedte: 32.0, diepgang: 2.7432 },
};
const klasseEl = document.getElementById("schipKlasse");
klasseEl.addEventListener("change", () => {
  if (vanEl.value && naarEl.value) toonRoute();
});

for (const b of document.querySelectorAll(".schipBtn")) {
  b.addEventListener("click", () => {
    SCHIP = b.dataset.schip;
    for (const o of document.querySelectorAll(".schipBtn")) o.classList.toggle("is-on", o === b);
    if (vanEl.value && naarEl.value) toonRoute();
  });
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
wireButtons(".hvBtn", "hv", (mode) => {
  if (HAVENLAAG) HAVENLAAG.punten.visible = (mode === "aan");
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
  zetAttrib();
});

document.getElementById("zoomIn").addEventListener("click", () => GLOBE.zoomBy(1 / 1.35));
document.getElementById("zoomOut").addEventListener("click", () => GLOBE.zoomBy(1.35));

// De tegel-attributie hangt aan de gekozen ondergrond; de vaarweg-attributie
// aan de gelaadde data (M24: OSM-middellijnen = ODbL, verplicht — óók als de
// ondergrond op "egaal" staat en er geen tegels in beeld zijn).
function zetAttrib() {
  const delen = [];
  if (TEGELS.isAan()) delen.push(TEGELS.attributie());
  const bronnen = NET ? Object.values(NET.vaarwegen || {}).map((v) => (v.bron || "").toLowerCase()) : [];
  if (bronnen.some((b) => b.includes("osm") || b.includes("openstreetmap"))) {
    delen.push("Vaarwegen: © OpenStreetMap-bijdragers (ODbL)");
  } else if (bronnen.some((b) => b.includes("unece"))) {
    delen.push("Vaarwegen: UNECE Blue Book");
  }
  document.getElementById("attrib").textContent = delen.join(" · ");
}
zetAttrib();

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
