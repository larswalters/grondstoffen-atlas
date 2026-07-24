// main.js — start v2 op en koppelt de HUD aan de lagen.
// Bewust dun: alle logica hoort in de lagen, niet hier.
//
// ⚠️ DE AIS-OMBOUW (2026-07-24, besluit Lars): het volledige waternet (marnet:
// zee + binnenvaart) is van de bol en uit de bake verwijderd — we bouwen het
// natte net opnieuw, corridor-first, uit World Bank AIS-density ("Global
// Shipping Traffic Density", Data Catalog 0037580). Brief = ankers, AIS = geul.
// De laatste stand mét het oude waternet staat op tag `pre-ais-net` (branch
// `backup/pre-ais-net`, ?v=082): daar leven ook de route-test, de keten-router
// (keten.js), de stromenlaag en toets_routes 30/30 — die komen terug zodra het
// AIS-net ze kan dragen. Havens, knooppunten en aansluitingen blijven bestaan
// als AANHECHTPUNTEN voor het nieuwe net.

import { createGlobe, CONFIG } from "./globe.js?v=070";
import { laadVectorWereld } from "./world.js?v=070";
import { createTileLayer } from "./tiles.js?v=070";
import { laadHavens } from "./marnet.js?v=077";
import { bouwHavenLaag, zetHavenGrootte, koppelHavenLabel } from "./havens.js?v=070";
import { laadLandnet } from "./landnet.js?v=070";

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

laadVectorWereld(CONFIG.radius, GLOBE.klemOpHorizon)
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

// --- de havens -------------------------------------------------------------
// De havens blijven op de bol: zij zijn de aanhechtpunten waar het nieuwe
// AIS-net straks op moet landen. ⚠️ Hun kleuren (zee/rivier-raak) komen nog uit
// de OUDE bake (ports.json ?v=077) — dat is bewust: de meting blijft leesbaar
// tot het AIS-net een nieuwe aanhechting levert.
let HAVENS = null;
let HAVENLAAG = null;

laadHavens()
  .then((havens) => {
    HAVENS = havens;
    HAVENLAAG = bouwHavenLaag(havens, CONFIG.radius);
    GLOBE.globeGroup.add(HAVENLAAG.punten);
    koppelHavenLabel(GLOBE, HAVENLAAG, HAVENLAAG.getoond, document.getElementById("havenLabel"));
    window.HAVENLAAG = HAVENLAAG;   // diagnose-handvat
    window.HAVENS = havens;
    const hs = HAVENLAAG.stats;
    console.log(
      `[atlas v2] havens: ${hs.havens.toLocaleString("nl")} getoond van ${hs.bron.toLocaleString("nl")} · ` +
      `${hs.verborgen.toLocaleString("nl")} verborgen (>${hs.aanWaterKm} km van kust/meer/rivier)`
    );
    document.getElementById("havenNoot").textContent =
      `${hs.havens.toLocaleString("nl")} van ${hs.bron.toLocaleString("nl")} getoond — ` +
      `${hs.verborgen.toLocaleString("nl")} liggen >${hs.aanWaterKm} km van kust, meer of rivier`;
    zetAttrib();
  })
  .catch((e) => console.error("[atlas v2] havens niet geladen:", e));

// --- het landnet (M25) -----------------------------------------------------
// ⚠️ "082" is de BAKE-versie, niet de codeversie. Die twee zijn bewust
// losgekoppeld: het landnet is bij de AIS-ombouw niet opnieuw gebakken, en
// meebumpen met de code dwingt elke bezoeker ~5 MB opnieuw te downloaden voor
// een bit-identiek bestand. Bump deze alleen bij een echte bake.
let LANDNET = null;
laadLandnet(CONFIG.radius, "082", GLOBE.klemOpHorizon)
  .then((ln) => {
    LANDNET = ln;
    GLOBE.globeGroup.add(ln.lijnen);
    window.LANDNET = ln;
    const s = ln.stats;
    console.log(
      `[atlas v2] landnet: ${s.netwerkKm.toLocaleString("nl")} km · ` +
      `${s.knopen.toLocaleString("nl")} knopen · ${s.edges.toLocaleString("nl")} edges · ` +
      `${s.punten.toLocaleString("nl")} punten · ${s.labels} labels · ` +
      `${s.kbOverdracht} KB · laden ${s.msLaden} ms, verwerken ${s.msVerwerken} ms`
    );
    const noot = document.getElementById("landNoot");
    if (noot) {
      noot.textContent =
        `${Math.round(s.netwerkKm).toLocaleString("nl")} km spoor · ` +
        `${s.edges.toLocaleString("nl")} edges · ${s.labels} labels`;
    }
  })
  .catch((e) => console.warn("[atlas v2] landnet niet geladen (nog niet gebakken?):", e.message));

// De vectorlagen liggen precies OP de bol. Om te voorkomen dat ze half in het
// oppervlak verdwijnen, tillen we ze elke frame een klein beetje op — evenredig
// met de kijkhoogte. Elke laag z'n eigen plank: kustlijn onder, landnet erboven,
// de havens bovenop.
GLOBE.onTick(() => {
  const alt = GLOBE.getAltitude();
  if (kustlijn) {
    const op = Math.max(CONFIG.radius * 2e-6, alt * 0.004);
    kustlijn.scale.setScalar(1 + op / CONFIG.radius);
  }
  if (LANDNET) {
    const op = Math.max(CONFIG.radius * 2.5e-6, alt * 0.0045);
    LANDNET.lijnen.scale.setScalar(1 + op / CONFIG.radius);
  }
  if (HAVENLAAG) {
    // Bovenop alles: een haven mag nooit onder een lijn verdwijnen.
    const op = Math.max(CONFIG.radius * 5e-6, alt * 0.007);
    HAVENLAAG.punten.scale.setScalar(1 + op / CONFIG.radius);
    zetHavenGrootte(HAVENLAAG, GLOBE.getAltitudeKm(), GLOBE.renderer.getPixelRatio());
  }
});

// --- HUD -------------------------------------------------------------------

// Menu in-/uitklappen. Op een telefoon dekt het volledige paneel de bol af, dus
// starten we daar INGEKLAPT — de kop blijft staan, één tik opent de rest. Op een
// breed scherm staat het gewoon open.
const hudEl = document.getElementById("hud");
const hudToggle = document.getElementById("hudToggle");
if (window.innerWidth <= 640) hudEl.classList.add("is-collapsed");
hudToggle.addEventListener("click", () => hudEl.classList.toggle("is-collapsed"));

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
wireButtons(".lnBtn", "ln", (mode) => {
  if (LANDNET) LANDNET.lijnen.visible = (mode === "aan");
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

// De tegel-attributie hangt aan de gekozen ondergrond; de haven-attributie aan
// de geladen data. De vaarweg-vermelding (ODbL) is met het waternet mee weg en
// komt terug zodra het AIS-net OSM- of World Bank-data draagt.
function zetAttrib() {
  const delen = [];
  if (TEGELS.isAan()) delen.push(TEGELS.attributie());
  // WPI-verrijking op de havens (LAR-518): publiek domein, bron wel noemen.
  if (HAVENS && HAVENS.some((h) => h.wpiAfstandKm >= 0)) {
    delen.push("Havens: NGA World Port Index (publiek domein)");
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
  if (t.mislukt) tekst += `\n${t.mislukt} tegels mislukt`;
  statsEl.textContent = tekst;
});

// Handvat voor diagnose vanuit de console/devtools. Dit project wordt veel
// visueel geverifieerd; zonder globals is er anders geen enkele manier om de
// scene van buitenaf te bevragen (ES-modules hebben geen window-scope).
window.GLOBE = GLOBE;
window.TEGELS = TEGELS;

console.log("[atlas v2] three r185 · ACES · tegels tot z19 · schone bol — AIS-waternet in opbouw (oud waternet: tag pre-ais-net)");
