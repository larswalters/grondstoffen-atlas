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

import { createGlobe, CONFIG } from "./globe.js?v=118";
import { laadVectorWereld } from "./world.js?v=070";
import { createTileLayer } from "./tiles.js?v=070";
import { laadHavens } from "./marnet.js?v=077";
import { bouwHavenLaag, zetHavenGrootte, koppelHavenLabel } from "./havens.js?v=070";
import { laadLandnet } from "./landnet.js?v=070";
import { laadAisnet } from "./aisnet.js?v=084";
import { laadAisgloed } from "./aisgloed.js?v=086";
import { laadAisTracks } from "./aistracks.js?v=090";
import { laadAnkercheck } from "./ankercheck.js?v=098";
import { laadStroombundel } from "./stroombundel.js?v=133";
import { GRONDSTOF_KLEUR, LIJNSTIJL } from "./stroomstijl.js?v=133";

const GLOBE = createGlobe(document.getElementById("canvasWrap"));

// ⚠️ ALLE VECTORLAGEN OP DE SCHIL VAN DE DIEPSTE TEGELS, niet op `radius`.
// Zie de toelichting bij CONFIG.vectorLift in globe.js: de detailtegels liggen
// 130 m boven `radius`, en een lijn eronder verschuift schuin bekeken zichtbaar.
// Eén constante voor alle lagen, zodat ze onderling per constructie niet uit
// elkaar kunnen lopen.
const VECTOR_R = CONFIG.radius * CONFIG.vectorLift;

// --- modus en versies (golf 1 van de visuele fase, 2026-10-08) -------------
// ✅ BESLUIT LARS (2026-10-08): de pagina opent als ATLAS — kleur per grondstof,
// ondergrond donker, gloed en kometen aan, spoornet uit en niet geladen. Dit
// vervangt het besluit van 2026-08-07 ("modaliteitsweergave als default"): dat
// was de bewezen stand van het ROUTEWERK met vijf stromen; met 182 stromen is
// de atlas het product en het routewerk de bouwmodus. `?modus=bouw` opent het
// routewerk (modaliteit · vol · spoornet geladen · witte precisiestippen).
// De oude per-stroom-lagen (exacte lijn, draad + kometen en gloedknopen per
// stroom, tot ?v=131) en hun pariteitspad `?laag=los` zijn in stap 4 van
// golf 1 verwijderd: de bundel is het enige pad.
const PARAMS = new URLSearchParams(location.search);
const MODUS = PARAMS.get("modus") === "bouw" ? "bouw" : "atlas";
const CODE_VERSIE = "133";
// ⚠️ De BUNDEL-versie staat los van de code-versie (zoals landnet "102"): bump
// alleen na `bash v2/tools/bak_stromen.sh bundel`, anders downloadt elke
// bezoeker bit-identieke bins opnieuw.
const BUNDEL_VERSIE = "132";
const TELEFOON = window.innerWidth <= 640;

// --- welke lagen meedoen ---------------------------------------------------
// Op verzoek van Lars (2026-08-07) staan vier lagen uit en zijn hun HUD-knoppen
// weg: ze concurreerden met het beeld dat nu beoordeeld wordt (de AIS-drukte
// legt een brede witte band over precies de rivieren waar de stromen lopen).
//
// ⚠️ Bewust een vlag en geen verwijderde code. Deze lagen zijn geen dood hout:
// de havens zijn de aanhechtpunten voor het nieuwe waternet, de AIS-tracks zijn
// het bronmateriaal voor de graaf-stap (LAR-530) en de vectorwereld is volgens
// de projectafspraak de WAARHEID waartegen routering rekent — alleen het TÓNEN
// ervan staat hier uit. Weghalen zou die rollen stilzwijgend opzeggen.
const TOON = {
  kustlijn: false,
  havens: false,
  aisgloed: false,
  aistracks: false,
};

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

if (TOON.kustlijn) laadVectorWereld(VECTOR_R, GLOBE.klemOpHorizon)
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

if (TOON.havens) laadHavens()
  .then((havens) => {
    HAVENS = havens;
    HAVENLAAG = bouwHavenLaag(havens, VECTOR_R);
    GLOBE.globeGroup.add(HAVENLAAG.punten);
    koppelHavenLabel(GLOBE, HAVENLAAG, HAVENLAAG.getoond, document.getElementById("havenLabel"));
    window.HAVENLAAG = HAVENLAAG;   // diagnose-handvat
    window.HAVENS = havens;
    const hs = HAVENLAAG.stats;
    console.log(
      `[atlas v2] havens: ${hs.havens.toLocaleString("nl")} getoond van ${hs.bron.toLocaleString("nl")} · ` +
      `${hs.verborgen.toLocaleString("nl")} verborgen (>${hs.aanWaterKm} km van kust/meer/rivier)`
    );
    const havenNoot = document.getElementById("havenNoot");   // niet meer in de HUD sinds golf 1
    if (havenNoot) havenNoot.textContent =
      `${hs.havens.toLocaleString("nl")} van ${hs.bron.toLocaleString("nl")} getoond — ` +
      `${hs.verborgen.toLocaleString("nl")} liggen >${hs.aanWaterKm} km van kust, meer of rivier`;
    zetAttrib();
  })
  .catch((e) => console.error("[atlas v2] havens niet geladen:", e));

// --- het landnet (M25) -----------------------------------------------------
// ⚠️ "102" is de BAKE-versie, niet de codeversie. Die twee zijn bewust
// losgekoppeld: het landnet is bij de AIS-ombouw niet opnieuw gebakken, en
// meebumpen met de code dwingt elke bezoeker ~5 MB opnieuw te downloaden voor
// een bit-identiek bestand. Bump deze alleen bij een echte bake.
//
// ⚠️ LUI SINDS GOLF 1 (2026-10-08): in de atlas wordt het spoornet NIET
// geladen en niet getoond — het is routeer-gereedschap ("ligt het spoorbeen op
// het net?"), en op de donkere bol las het cyaan/witte web als een vijftiende
// grondstof die niet in de legenda staat. Het was ook de grootste enkele
// post (10 MB, 7,5 MB over de lijn). In de bouwmodus (`?modus=bouw`) laadt het
// meteen; anders pas bij de eerste "aan" — het haalAisTracks()-patroon. Code,
// bestand en knop blijven (uitgezette lagen gaan achter een vlag, niet weg).
let LANDNET = null;
let landnetAan = MODUS === "bouw";
let landnetBezig = null;

function haalLandnet() {
  if (landnetBezig) return landnetBezig;
  const noot = document.getElementById("landNoot");
  if (noot) noot.textContent = "laden… (10 MB, eenmalig)";
  landnetBezig = laadLandnet(VECTOR_R, "102", GLOBE.klemOpHorizon)
    .then((ln) => {
      LANDNET = ln;
      ln.lijnen.visible = landnetAan;
      GLOBE.globeGroup.add(ln.lijnen);
      window.LANDNET = ln;
      const s = ln.stats;
      console.log(
        `[atlas v2] landnet: ${s.netwerkKm.toLocaleString("nl")} km · ` +
        `${s.knopen.toLocaleString("nl")} knopen · ${s.edges.toLocaleString("nl")} edges · ` +
        `${s.punten.toLocaleString("nl")} punten · ${s.labels} labels · ` +
        `${s.kbOverdracht} KB · laden ${s.msLaden} ms, verwerken ${s.msVerwerken} ms`
      );
      if (noot) {
        noot.textContent =
          `${Math.round(s.netwerkKm).toLocaleString("nl")} km spoor · ` +
          `${s.edges.toLocaleString("nl")} edges · ${s.labels} labels`;
      }
      return ln;
    })
    .catch((e) => {
      landnetBezig = null;
      if (noot) noot.textContent = "niet geladen (nog niet gebakken?)";
      console.warn("[atlas v2] landnet niet geladen (nog niet gebakken?):", e.message);
    });
  return landnetBezig;
}
if (landnetAan) haalLandnet();

// --- het AIS-waternet (M27, pilot) -----------------------------------------
// De eerste zichtbare stap van de ombouw: vaargeulen afgeleid uit World Bank
// AIS-density (bake_aisnet.py), vier testvensters — Tongling · Nederland ·
// Patache · Shanghai. Kijk-laag; standaard UIT (besluit Lars 2026-07-25) en
// sinds golf 1 (2026-10-08) ook pas geladen bij de eerste "aan".
let AISNET = null;
let aisnetAan = false;
let aisnetBezig = null;

function haalAisnet() {
  if (aisnetBezig) return aisnetBezig;
  aisnetBezig = laadAisnet(VECTOR_R, "085", GLOBE.klemOpHorizon)
    .then((an) => {
      AISNET = an;
      an.lijnen.visible = aisnetAan;
      GLOBE.globeGroup.add(an.lijnen);
      window.AISNET = an;
      const s = an.stats;
      console.log(
        `[atlas v2] aisnet: ${s.lijnen.toLocaleString("nl")} lijnen · ` +
        `${s.segmenten.toLocaleString("nl")} segmenten · ${s.kbOverdracht} KB · ` +
        `laden ${s.msLaden} ms, verwerken ${s.msVerwerken} ms`
      );
      const noot = document.getElementById("aisNoot");
      if (noot) {
        noot.textContent =
          `pilot: ${Object.keys(an.vensters).join(" · ")} — ` +
          `${s.lijnen.toLocaleString("nl")} geullijnen uit AIS-density`;
      }
      return an;
    })
    .catch((e) => { aisnetBezig = null; console.warn("[atlas v2] aisnet niet geladen (nog niet gebakken?):", e.message); });
  return aisnetBezig;
}

// --- echte scheepstracks (M28, vijf bronnen) -------------------------------
// De bol-toets van de track-aanpak: gevaren lijnen van individuele schepen uit
// vijf AIS-archieven, op- en afvaart elk hun kleur. Kijk-laag; de graaf-stap
// (LAR-530) rekent op de volledige tracksets in build-cache.
//
// ⚠️ LAAT LADEN, EN DAT IS GEEN OPTIMALISATIE. Dit is met afstand het zwaarste
// databestand van de atlas (39,5 MB, ~14 MB over de lijn). Eager ophalen liet
// élke bezoeker die download betalen voor een laag die standaard UIT staat en
// die de meesten nooit aanzetten. Nu wordt hij pas gehaald bij de eerste "aan".
let AISTRACKS = null;
let aistracksAan = false;
let aistracksBezig = null;

function haalAisTracks() {
  // De laag was al lui (39,5 MB, pas bij de eerste "aan"); nu staat hij ook uit.
  if (!TOON.aistracks) return Promise.resolve(null);
  if (aistracksBezig) return aistracksBezig;
  const noot = document.getElementById("tracksNoot");
  if (noot) noot.textContent = "laden… (39,5 MB, eenmalig)";
  aistracksBezig = laadAisTracks(VECTOR_R, "090", GLOBE.klemOpHorizon)
    .then((at) => {
      AISTRACKS = at;
      at.groep.visible = aistracksAan;
      GLOBE.globeGroup.add(at.groep);
      window.AISTRACKS = at;
      const s = at.stats;
      console.log(
        `[atlas v2] aistracks: ${s.lijnen.toLocaleString("nl")} lijnen · ` +
        `${s.segmenten.toLocaleString("nl")} segmenten · ${s.kbOverdracht} KB · ` +
        `laden ${s.msLaden} ms, verwerken ${s.msVerwerken} ms · ` +
        s.perBron.map((b) => `${b.sleutel} ${b.lijnen}/${b.segmenten}`).join(" · ")
      );
      // De noot telt; de bronvermelding zelf staat statisch in index.html en in
      // de attributiebalk — een licentie-eis hoort niet af te hangen van of een
      // laag toevallig al geladen is.
      if (noot) {
        // ⚠️ Lijnen ≠ doorvaarten: de valse-lassen-knip in de bake splitst een
        // track in meer lijnen (AMSA: 2.043 gekozen tracks → 2.272 lijnen). De
        // noot telt daarom allebei, anders lijkt de tabel van de bake fout.
        const gekozen = (at.bronnen || []).reduce((n, b) => n + b.gekozen, 0);
        noot.textContent =
          s.perBron.map((b) => `${b.sleutel} ${b.lijnen.toLocaleString("nl")}`).join(" · ") +
          ` — ${s.lijnen.toLocaleString("nl")} lijnen` +
          (gekozen ? ` uit ${gekozen.toLocaleString("nl")} doorvaarten` : "") +
          ` · ${s.segmenten.toLocaleString("nl")} segmenten, dekkingsselectie`;
      }
      zetAttrib();
      return at;
    })
    .catch((e) => {
      aistracksBezig = null;   // volgende "aan" mag het opnieuw proberen
      if (noot) noot.textContent = "niet geladen (nog niet gebakken?)";
      console.warn("[atlas v2] aistracks niet geladen (nog niet gebakken?):", e.message);
    });
  return aistracksBezig;
}

// --- de stromen: de bundel (golf 1 van de visuele fase, 2026-10-08) --------
// Alle 182 gemeten ketens komen uit ÉÉN afgeleid bundelbestand (stromen.json +
// stromen-basis.bin, gebakken door v2/tools/bak_stroombundel.py uit het
// register v2/data/stromen-register.json en de stroomroute-*.json, die de
// bron van waarheid blijven) en staan op de bol als een handvol objecten —
// zie v2/src/stroombundel.js en v2/design/atlas-product-golf1.md.
//
// ⚠️ HET REGISTER WOONT NIET MEER HIER. Het STROMEN-blok van 182 regels is
// verhuisd naar stromen-register.json (mét de golf-historie als `noot`); dat
// bestand is de enige bron voor deze HUD, de bundel én de baker. Registreren
// blijft een besluit (2026-09-28: een keten die volledig stippel is wordt niet
// geregistreerd) — de baker faalt luid op een bestand dat nergens staat.
let ATLAS = null;                    // de bundel-laag
let REGISTER = null;

// De twee weergave-assen (zie src/stroomstijl.js). Default = de atlas; de
// bouwmodus zet ze op de bewezen stand van het routewerk (?v=111).
let kleurModus = MODUS === "bouw" ? "modaliteit" : "grondstof";
let lijnModus = "route";             // "route" | "recht-plat" | "recht-boog" | "recht-zeeboog"
let gloedAan = true;                 // stand van de gn-knop
let bewegingAan = true;              // stand van de bw-knop

const STROOM_LABEL = {
  zee: "zeeschip", binnenvaart: "binnenschip", truck: "truck",
  spoor: "trein", leiding: "leiding", lucht: "vliegtuig",
};
const hexVan = (k) => "#" + k.toString(16).padStart(6, "0");

function stroomRegel(benen) {
  // Benen met dezelfde modaliteit tellen op tot één regel — een zeebeen dat op
  // een via-punt uit de routebrief gesplitst is, blijft één zeeschip.
  const per = new Map();
  for (const b of benen) {
    const k = STROOM_LABEL[b.modaliteit] || b.naam || b.modaliteit;
    per.set(k, (per.get(k) || 0) + (b.km || 0));
  }
  return [...per].map(([k, km]) => `${k} ${Math.round(km).toLocaleString("nl")} km`).join(" · ");
}

// Is een stroom aan, en welke benen heeft hij — uit de bundel (vóór die
// geladen is: nog niet geladen). Eén plek, zodat de HUD niet twee waarheden kent.
function stroomStand(sleutel) {
  if (ATLAS) {
    const info = ATLAS.stroomInfo(sleutel);
    return info ? { geladen: true, aan: ATLAS.isAan(sleutel), benen: info.benen } : { geladen: false };
  }
  return { geladen: false };
}
function zetStroomAan(sleutel, aan) {
  if (ATLAS) ATLAS.zetStroom(sleutel, aan);
}

// --- de HUD-groepen per grondstof (2026-09-26, sinds golf 1 gegenereerd) ---
// Eén <details class="srGroep" data-gs=…> per grondstof, met een .srBtn per
// stroom (data-sr = sleutel), gegenereerd uit het register in #stroomGroepen.
// De telling (aan/geladen) en de "alles"-knop in de summary werken zoals
// voorheen; op een telefoon starten de groepen dichtgeklapt (zelfde grens als
// de HUD zelf, zie hudToggle verderop).
function bouwStroomGroepen(register) {
  const houder = document.getElementById("stroomGroepen");
  if (!houder) return;
  houder.textContent = "";
  const smal = window.innerWidth <= 640;
  const grondstoffen = [...new Set(register.stromen.map((s) => s.grondstof))];
  for (const gs of grondstoffen) {
    const stromen = register.stromen.filter((s) => s.grondstof === gs);
    const groep = document.createElement("details");
    groep.className = "srGroep";
    groep.dataset.gs = gs;
    groep.open = !smal;
    const summary = document.createElement("summary");
    const bol = document.createElement("i");
    bol.className = "gsBol";
    const k = GRONDSTOF_KLEUR[gs];
    if (k !== undefined) { bol.style.background = hexVan(k); bol.style.boxShadow = `0 0 6px ${hexVan(k)}`; }
    const naam = document.createElement("span");
    naam.className = "gsNaam";
    naam.textContent = gs;
    const tel = document.createElement("span");
    tel.className = "gsTel";
    tel.textContent = `${stromen.length}`;
    const alles = document.createElement("button");
    alles.type = "button";
    alles.className = "gsBtn is-on";
    alles.dataset.gs = gs;
    alles.textContent = "alles";
    summary.append(bol, naam, tel, alles);
    groep.append(summary);
    for (let i = 0; i < stromen.length; i += 2) {
      const rij = document.createElement("div");
      rij.className = "btnRow";
      for (const s of stromen.slice(i, i + 2)) {
        const b = document.createElement("button");
        b.className = "srBtn" + (s.aan === false ? "" : " is-on");
        b.dataset.sr = s.sleutel;
        b.textContent = s.label || s.sleutel;
        if (s.noot) b.title = s.noot;
        rij.append(b);
      }
      groep.append(rij);
    }
    houder.append(groep);
  }
  // De chipstrip in de kop: één chip per grondstof (zichtbaar als het paneel
  // is ingeklapt — op een telefoon de hoofdbediening).
  const strip = document.getElementById("chipStrip");
  if (strip) {
    strip.textContent = "";
    for (const gs of grondstoffen) {
      const chip = document.createElement("button");
      chip.type = "button";
      chip.className = "gsChip is-on";
      chip.dataset.gs = gs;
      const bol = document.createElement("i");
      const k = GRONDSTOF_KLEUR[gs];
      if (k !== undefined) { bol.style.background = hexVan(k); bol.style.boxShadow = `0 0 6px ${hexVan(k)}`; }
      chip.append(bol, gs);
      strip.append(chip);
    }
  }
}

function werkGroepenBij() {
  if (!REGISTER) return;
  for (const chip of document.querySelectorAll(".gsChip")) {
    const defs = REGISTER.stromen.filter((d) => d.grondstof === chip.dataset.gs);
    chip.classList.toggle("is-on", defs.some((d) => { const st = stroomStand(d.sleutel); return st.geladen && st.aan; }));
  }
  for (const groep of document.querySelectorAll(".srGroep")) {
    const gs = groep.dataset.gs;
    const defs = REGISTER.stromen.filter((d) => d.grondstof === gs);
    const standen = defs.map((d) => stroomStand(d.sleutel)).filter((s) => s.geladen);
    const aan = standen.filter((s) => s.aan).length;
    const tel = groep.querySelector(".gsTel");
    if (tel) tel.textContent = `${aan}/${standen.length}`;
    const knop = groep.querySelector(".gsBtn");
    if (knop) knop.classList.toggle("is-on", standen.length > 0 && aan === standen.length);
  }
  for (const knop of document.querySelectorAll(".srBtn")) {
    const st = stroomStand(knop.dataset.sr);
    knop.classList.toggle("is-on", !!(st.geladen && st.aan));
  }
}

function toonStroomNoot() {
  const noot = document.getElementById("stroomNoot");
  if (noot && REGISTER) {
    // Eén regel per GRONDSTOF (stromen die aan staan + hun km opgeteld).
    const per = new Map();
    for (const def of REGISTER.stromen) {
      const st = stroomStand(def.sleutel);
      if (!st.geladen || !st.aan) continue;
      const t = per.get(def.grondstof) || { n: 0, km: 0 };
      t.n += 1;
      t.km += st.benen.reduce((som, b) => som + (b.km || 0), 0);
      per.set(def.grondstof, t);
    }
    const regels = [...per].map(([gs, t]) =>
      `${gs}: ${t.n} ${t.n === 1 ? "stroom" : "stromen"} · ${Math.round(t.km).toLocaleString("nl")} km`);
    noot.textContent = regels.length ? regels.join("\n") : "geen stroom aan";
  }
  werkGroepenBij();
}

// #stroomLegendaGrondstof: één regel per grondstof uit het register, kleur uit
// GRONDSTOF_KLEUR — niet hard-coded in de html.
function bouwGrondstofLegenda(register) {
  const el = document.getElementById("stroomLegendaGrondstof");
  if (!el) return;
  const noot = el.querySelector(".legNoot");
  for (const gs of [...new Set(register.stromen.map((d) => d.grondstof))]) {
    const k = GRONDSTOF_KLEUR[gs];
    const span = document.createElement("span");
    const bol = document.createElement("i");
    bol.style.background = k === undefined ? "#bfbfbf" : hexVan(k);
    span.append(bol, gs);
    el.insertBefore(span, noot);
  }
}

// De lijnstijl-legenda (kleur = grondstof, LIJN = transport): staaltjes als
// inline-SVG uit de LIJNSTIJL-tabel van stroomstijl.js — niet met de hand
// getekend, zodat legenda en shader dezelfde tabel lezen.
function bouwLijnstijlLegenda() {
  const el = document.getElementById("lijnstijlLegenda");
  if (!el) return;
  el.textContent = "";
  const NS = "http://www.w3.org/2000/svg";
  const volgorde = [0, 1, 2, 3, 4, 5, 7];
  const label = { zee: "zeeschip", binnenvaart: "binnenschip", truck: "truck (weg)", spoor: "trein (spoor)",
                  leiding: "leiding", lucht: "vliegtuig (boog)", stippel: "gestippeld = hier reikt het net niet" };
  const lijn = (svg, x1, x2, bw, alfa) => {
    const l = document.createElementNS(NS, "line");
    l.setAttribute("x1", x1); l.setAttribute("x2", x2); l.setAttribute("y1", 5); l.setAttribute("y2", 5);
    l.setAttribute("stroke", "currentColor"); l.setAttribute("stroke-width", bw); l.setAttribute("stroke-opacity", alfa);
    svg.append(l);
  };
  for (const i of volgorde) {
    const s = LIJNSTIJL[i];
    const span = document.createElement("span");
    const svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", "0 0 60 10");
    svg.setAttribute("width", "60"); svg.setAttribute("height", "10");
    svg.classList.add("lsStaal");
    const bw = Math.max(1, s.breedte * 1.5);
    if (s.periode > 0) {
      for (let x = 0; x < 60; x += s.periode) {
        lijn(svg, x, Math.min(60, x + s.aan), bw, s.alfaAan);
        if (s.alfaUit > 0) lijn(svg, Math.min(60, x + s.aan), Math.min(60, x + s.periode), bw, s.alfaUit);
      }
    } else {
      lijn(svg, 0, 60, bw, s.kernFractie < 1 ? 0.8 : 1);
    }
    span.append(svg, label[s.naam] || s.naam);
    el.append(span);
  }
}

// Eén knop per stroom (data-sr = sleutel uit het register) — een schakelaar
// per stroom, want met 182 stromen op de bol is "welke wil ik nu zien" de
// vraag. De "alles"-knop in de summary schakelt alle stromen van die grondstof
// (staan ze allemaal aan dan uit, anders aan). preventDefault +
// stopPropagation, anders klapt de <details> mee.
function koppelStroomKnoppen() {
  for (const knop of document.querySelectorAll(".srBtn")) {
    knop.addEventListener("click", () => {
      const st = stroomStand(knop.dataset.sr);
      if (!st.geladen) return;
      zetStroomAan(knop.dataset.sr, !st.aan);
      toonStroomNoot();
    });
  }
  for (const knop of document.querySelectorAll(".gsBtn")) {
    knop.addEventListener("click", (ev) => {
      ev.preventDefault();
      ev.stopPropagation();
      const gs = knop.dataset.gs;
      const defs = REGISTER.stromen.filter((d) => d.grondstof === gs);
      const standen = defs.map((d) => [d.sleutel, stroomStand(d.sleutel)]).filter(([, s]) => s.geladen);
      if (!standen.length) return;
      const nieuw = !standen.every(([, s]) => s.aan);
      if (ATLAS) ATLAS.zetGrondstof(gs, nieuw);
      toonStroomNoot();
    });
  }
  // De chip: staat er íets van de grondstof aan, dan alles uit; anders alles aan.
  for (const chip of document.querySelectorAll(".gsChip")) {
    chip.addEventListener("click", () => {
      const gs = chip.dataset.gs;
      const defs = REGISTER.stromen.filter((d) => d.grondstof === gs);
      const standen = defs.map((d) => [d.sleutel, stroomStand(d.sleutel)]).filter(([, s]) => s.geladen);
      if (!standen.length) return;
      const nieuw = !standen.some(([, s]) => s.aan);
      if (ATLAS) ATLAS.zetGrondstof(gs, nieuw);
      toonStroomNoot();
    });
  }
}

async function startStromen() {
  const r = await fetch(`data/stromen-register.json?v=${CODE_VERSIE}`);
  if (!r.ok) throw new Error(`stromen-register.json: HTTP ${r.status}`);
  REGISTER = await r.json();
  window.REGISTER = REGISTER;
  bouwStroomGroepen(REGISTER);
  bouwGrondstofLegenda(REGISTER);
  bouwLijnstijlLegenda();
  koppelStroomKnoppen();
  const sub = document.getElementById("hudSub");
  const nGs = new Set(REGISTER.stromen.map((s) => s.grondstof)).size;
  if (sub) sub.textContent = `${REGISTER.stromen.length} stromen · ${nGs} grondstoffen · kleur = grondstof, lijn = transport`;

  ATLAS = await laadStroombundel({
    radius: VECTOR_R, codeVersie: CODE_VERSIE, bundelVersie: BUNDEL_VERSIE,
    klemOpHorizon: GLOBE.klemOpHorizon, camera: GLOBE.camera, renderer: GLOBE.renderer,
    globeGroup: GLOBE.globeGroup, getAltitudeKm: GLOBE.getAltitudeKm, telefoon: TELEFOON,
    kleurModus, lijnModus, gloedAan,
  });
  GLOBE.globeGroup.add(ATLAS.groep);
  // Een klik tijdens het laden (≈ 0,5 s) mag niet verloren gaan: de stand van
  // nu toepassen, niet die van het moment van aanroepen (review 2026-10-08).
  ATLAS.zetKleurModus(kleurModus);
  ATLAS.zetLijnModus(lijnModus);
  ATLAS.zetGloed(gloedAan);
  ATLAS.zetBeweging(bewegingAan);
  GLOBE.onTick((dt) => ATLAS.update(dt));
  window.ATLAS = ATLAS;                 // diagnose- en meethandvat (meet_atlas.mjs)
  const st = ATLAS.stats;
  console.log(
    `[atlas v2] stromenbundel ${BUNDEL_VERSIE}: ${st.stromen} stromen · ${st.benen} benen (${st.stippel} stippel) · ` +
    `${st.markers} knopen · ${st.sites} sites · L0 ${st.segmentenL0.toLocaleString("nl")} / L1 ${st.segmentenL1.toLocaleString("nl")} / ` +
    `lucht ${st.segmentenLucht.toLocaleString("nl")} segmenten · ${st.kometen.kometen} kometen (K ${st.kometen.K}) · ` +
    `laden ${st.msLaden} ms, decoderen ${st.msDecoderen} ms`
  );
  toonStroomNoot();
}

startStromen().catch((e) => {
  console.error("[atlas v2] stromen niet geladen:", e);
  const noot = document.getElementById("stroomNoot");
  if (noot) noot.textContent = `stromen niet geladen: ${e.message}`;
});

// --- open ligplaatsen: wat er van de anker-check over is --------------------
// De beoordelingsronde van 2026-07-28 is afgerond: zeven correcties zijn
// goedgekeurd en doorgevoerd, zes punten doorstonden de check. Die dertien zijn
// uit `ankercheck.json` gehaald — een rode stip op een al gecorrigeerd punt
// liegt. Wat blijft zijn de DRIE waar de ligplaats niet aanwijsbaar was
// (Lobito · Port Allen · Vidalia); voor alle drie is de productvraag wél
// beantwoord, alleen de kade nog niet. Het rood/groen-mechanisme blijft staan,
// zodat een voorstel voor die drie meteen te beoordelen is.
// Elke knop vliegt naar het punt: op een telefoon is dat de enige werkbare
// manier om zo'n plek op straatniveau na te lopen.
// ⚠️ LUI SINDS GOLF 1 (2026-10-08): standaard uit en pas geladen bij de eerste
// "aan" — het is een beoordelingslaag voor het routewerk, geen atlasbeeld.
let ANKERCHECK = null;
let ankercheckAan = false;
let ankercheckBezig = null;
function haalAnkercheck() {
  if (ankercheckBezig) return ankercheckBezig;
  ankercheckBezig = laadAnkercheck(VECTOR_R, "098", GLOBE.klemOpHorizon)
  .then((a) => {
    ANKERCHECK = a;
    a.groep.visible = ankercheckAan;
    GLOBE.globeGroup.add(a.groep);
    window.ANKERCHECK = a;           // diagnose-handvat
    const lijst = document.getElementById("ankerLijst");
    if (lijst) {
      for (const anker of a.ankers) {
        const knop = document.createElement("button");
        const merk = anker.status === "goed" ? "✓"
          : anker.status === "ongecontroleerd" ? "?"
          : anker.afstandM >= 1000 ? `${(anker.afstandM / 1000).toFixed(1).replace(".", ",")} km`
          : anker.afstandM > 0 ? `${anker.afstandM} m`
          : "✕";
        knop.textContent = `${anker.naam} · ${merk}`;
        knop.className = `ankerKnop is-${anker.status}`;
        knop.title = anker.wat;
        // Vlieg naar het NIEUWE punt waar dat bestaat — dan valt het oude punt
        // vanzelf in beeld ernaast; andersom kan het voorstel buiten beeld
        // vallen bij de grote correcties (Escondida 1,5 km).
        const doel = anker.nieuw || anker.oud;
        knop.addEventListener("click", () => GLOBE.vliegNaar(doel[0], doel[1], 2));
        lijst.appendChild(knop);
      }
    }
    const open = a.ankers.filter((x) => x.status === "onbepaald" && !x.nieuw).length;
    const noot = document.getElementById("ankerNoot");
    if (noot) {
      noot.textContent = open === a.ankers.length
        ? `${open} ligplaats${open === 1 ? "" : "en"} nog niet aanwijsbaar — `
          + `operator en terminal zijn bekend, de kade niet`
        : `${open} van ${a.ankers.length} nog open; de rest heeft een voorstel`;
    }
    console.log(`[atlas v2] ankercheck: ${a.titel} · ${open}/${a.ankers.length} open`);
    return a;
  })
  .catch((e) => { ankercheckBezig = null; console.warn("[atlas v2] ankercheck niet geladen:", e.message); });
  return ankercheckBezig;
}

// --- de AIS-drukte als gloed (M27) -----------------------------------------
// Het dichtheidsveld zélf op de bol (besluit Lars 2026-07-25): de blauwe
// gloed van zes jaar scheepvaart, additief per pilotvenster — dít is het
// beeld; de lijnen hierboven zijn het graaf-zaad.
let AISGLOED = null;
if (TOON.aisgloed) laadAisgloed(VECTOR_R, "086", GLOBE.klemOpHorizon)
  .then((g) => {
    AISGLOED = g;
    GLOBE.globeGroup.add(g.groep);
    window.AISGLOED = g;
    const s = g.stats;
    console.log(
      `[atlas v2] aisgloed: ${s.vensters} vensters · ` +
      `laden ${s.msLaden} ms, verwerken ${s.msVerwerken} ms`
    );
    const noot = document.getElementById("gloedNoot");
    if (noot) {
      noot.textContent =
        `drukte 2015–2021 als gloed: ${Object.keys(g.vensters).join(" · ")}`;
    }
  })
  .catch((e) => console.warn("[atlas v2] aisgloed niet geladen (nog niet gebakken?):", e.message));

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
  if (AISNET) {
    // Boven het landnet: waar spoor en water samenkomen hoort water te winnen.
    const op = Math.max(CONFIG.radius * 3e-6, alt * 0.005);
    AISNET.lijnen.scale.setScalar(1 + op / CONFIG.radius);
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
  landnetAan = (mode === "aan");
  if (LANDNET) LANDNET.lijnen.visible = landnetAan;
  else if (landnetAan) haalLandnet();           // eerste keer: nu pas ophalen (10 MB)
});
wireButtons(".anBtn", "an", (mode) => {
  aisnetAan = (mode === "aan");
  if (AISNET) AISNET.lijnen.visible = aisnetAan;
  else if (aisnetAan) haalAisnet();
});
wireButtons(".atBtn", "at", (mode) => {
  aistracksAan = (mode === "aan");
  if (AISTRACKS) {
    AISTRACKS.groep.visible = aistracksAan;
    zetAttrib();                            // bronvermelding volgt de laag
  } else if (aistracksAan) {
    haalAisTracks();                        // eerste keer: nu pas ophalen
  }
});
// Kleur van de stromen: per transport (routewerk) ↔ per grondstof (atlas).
// De bundel kleurt lijn en komeet van een been in één pas (pasKleurToe in
// stroombundel.js), dus die hebben per constructie dezelfde kleur.
wireButtons(".skBtn", "sk", (modus) => {
  kleurModus = modus;
  if (ATLAS) ATLAS.zetKleurModus(modus);
  toonStroomNoot();
  const modLeg = document.getElementById("stroomLegenda");
  const grLeg = document.getElementById("stroomLegendaGrondstof");
  if (modLeg) modLeg.hidden = (modus === "grondstof");
  if (grLeg) grLeg.hidden = (modus !== "grondstof");
  // De atlasmodus zet de ondergrond mee op donker en het routewerk weer op vol.
  // ⚠️ Bewust GEEN verborgen gedrag: de knoprij hieronder springt zichtbaar
  // mee, en je kunt hem daarna los bijstellen. Zonder deze koppeling zie je bij
  // het omschakelen de gloedhotspots niet — additief licht heeft op een felle
  // daglichtfoto niets om tegen af te steken, en dat is de reden dat de
  // ontwerpbrief night-side een VOORWAARDE noemt en geen schoonheidsvraag.
  zetOndergrondDim(modus === "grondstof" ? "donker" : "vol");
});

// Ondergrond dimmen. Raakt per constructie alleen de tegels en de bol: de
// lijnen staan op `toneMapped: false` en de gloed/kometen zijn eigen
// ShaderMaterials, en die drie gaan geen van alle door tone mapping.
function zetOndergrondDim(stand) {
  GLOBE.zetBelichting(stand);
  for (const b of document.querySelectorAll(".sdBtn")) {
    b.classList.toggle("is-on", b.dataset.sd === stand);
  }
}
wireButtons(".sdBtn", "sd", (stand) => GLOBE.zetBelichting(stand));

// De startstand van de knoprijen volgt de modus — zichtbaar, niet verborgen.
function zetKnopStand(selector, attr, waarde) {
  for (const b of document.querySelectorAll(selector)) b.classList.toggle("is-on", b.dataset[attr] === waarde);
}
zetKnopStand(".skBtn", "sk", kleurModus);
zetKnopStand(".slBtn", "sl", lijnModus);
zetKnopStand(".lnBtn", "ln", landnetAan ? "aan" : "uit");
zetKnopStand(".akBtn", "ak", "uit");
zetKnopStand(".gnBtn", "gn", "aan");
zetKnopStand(".bwBtn", "bw", "aan");
{
  const modLeg = document.getElementById("stroomLegenda");
  const grLeg = document.getElementById("stroomLegendaGrondstof");
  if (modLeg) modLeg.hidden = (kleurModus === "grondstof");
  if (grLeg) grLeg.hidden = (kleurModus !== "grondstof");
}
zetOndergrondDim(kleurModus === "grondstof" ? "donker" : "vol");
document.body.dataset.modus = MODUS;
{
  // De bouwsectie staat dicht; ?modus=bouw opent hem (het routewerk wil zijn knoppen zien).
  const bouw = document.getElementById("bouw");
  if (bouw) bouw.open = (MODUS === "bouw");
}

// Lijnvorm: de gemeten route of één van de drie hemelsbreed-varianten.
wireButtons(".slBtn", "sl", (modus) => {
  lijnModus = modus;
  if (ATLAS) ATLAS.zetLijnModus(modus);
});

wireButtons(".akBtn", "ak", (mode) => {
  ankercheckAan = (mode === "aan");
  if (ANKERCHECK) ANKERCHECK.groep.visible = ankercheckAan;
  else if (ankercheckAan) haalAnkercheck();
});
wireButtons(".glBtn", "gl", (mode) => {
  if (AISGLOED) AISGLOED.groep.visible = (mode === "aan");
});
wireButtons(".gnBtn", "gn", (mode) => {
  gloedAan = (mode === "aan");
  if (ATLAS) ATLAS.zetGloed(gloedAan);
});
// Beweging (de kometen) aan/uit — nieuw in golf 1; de lijnen blijven staan.
wireButtons(".bwBtn", "bw", (mode) => {
  bewegingAan = (mode === "aan");
  if (ATLAS) ATLAS.zetBeweging(bewegingAan);
});
document.querySelectorAll(".gnGa").forEach((knop) => {
  knop.addEventListener("click", () => {
    GLOBE.vliegNaar(+knop.dataset.lon, +knop.dataset.lat, +knop.dataset.km);
  });
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
  // De vijf AIS-archieven, zodra hun lijnen op de bol staan. ⚠️ AMSA is
  // CC BY-NC 3.0 AU — naamsvermelding ÉN niet-commercieel gebruik; dat is de
  // strengste eis van de vijf en die staat daarom voluit, niet als afkorting.
  if (AISTRACKS && AISTRACKS.groep.visible) {
    delen.push(
      "AIS-tracks: MarineCadastre NOAA/USACE (publiek domein) · " +
      "DMA Denemarken · Kystdatahuset/Kystverket (NLOD) · " +
      "© AMSA (CC BY-NC 3.0 AU, niet-commercieel) · eigen aisstream-collector"
    );
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
  if (ATLAS) {
    const a = ATLAS.stats;
    tekst += `\nstromen ${a.stromen} · ${["L0", "L1", "fijn"][a.niveau]} · ${a.objecten} objecten` +
      (a.fijnSegmenten ? ` · fijn ${a.fijnSegmenten.toLocaleString("nl")} seg` : "");
  }
  statsEl.textContent = tekst;
});

// Handvat voor diagnose vanuit de console/devtools. Dit project wordt veel
// visueel geverifieerd; zonder globals is er anders geen enkele manier om de
// scene van buitenaf te bevragen (ES-modules hebben geen window-scope).
window.GLOBE = GLOBE;
window.TEGELS = TEGELS;

console.log(`[atlas v2] three r185 · ACES · tegels tot z19 · modus ${MODUS} (stromenbundel ${BUNDEL_VERSIE})`);
