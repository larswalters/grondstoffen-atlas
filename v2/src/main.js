// main.js — start v2 op en koppelt de HUD aan de lagen.
// Bewust dun: alle logica hoort in de lagen, niet hier.

import * as THREE from "three";
import { createGlobe, CONFIG } from "./globe.js?v=070";
import { laadVectorWereld } from "./world.js?v=070";
import { createTileLayer } from "./tiles.js?v=070";
import { laadMarnet, laadHavens, zoekRoute, zoekRouteRealistisch, bouwRouteLijn }
  from "./marnet.js?v=077";
import { bouwHavenLaag, zetHavenGrootte, koppelHavenLabel } from "./havens.js?v=070";
import { laadLandnet } from "./landnet.js?v=070";
import { koppelNetten, zoekKeten, havenZaden, puntZaden, GROEP_NAAM } from "./keten.js?v=070";
import { laadStromen, routeerStroom } from "./stromen.js?v=070";
import { bouwStroomLaag, zetMerkGrootte } from "./stroomlaag.js?v=070";

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

// --- het MARNET-netwerk ----------------------------------------------------
// De vaarlanen, éénmalig verzoend met de vectorwereld hierboven (LAR-483).
// Routeren = A* over deze graaf; de route-test hieronder bewijst dat.

let NET = null;
let HAVENS = null;
let HAVENLAAG = null;
let netStats = null;
let routeLijn = null;

Promise.all([laadMarnet(CONFIG.radius, GLOBE.klemOpHorizon), laadHavens()])
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
    probeerKoppel();
  })
  .catch((e) => console.error("[atlas v2] marnet niet geladen:", e));

// --- het landnet (M25) -----------------------------------------------------
// ⚠️ "058" is de BAKE-versie, niet de codeversie. Die twee zijn bewust
// losgekoppeld: marnet/landnet/ports/knooppunten zijn sinds ?v=070 niet
// opnieuw gebakken, en ze meebumpen met de code dwingt elke bezoeker ~14 MB
// opnieuw te downloaden voor bit-identieke bestanden. Bump deze alleen bij
// een echte bake — dat is precies wat de cache-busting-discipline bedoelt.
// Spoor (en straks weg) als VIERDE net, in een eigen bestand met eigen knoop-ids.
// Bewust nog niet gekoppeld aan de router: eerst neerleggen, dan verbinden via
// aangewezen knooppunten — Lars' volgorde. Een ontbrekend bestand is geen fout
// maar "nog niet gebakken": de rest van de atlas moet gewoon doorladen.
let LANDNET = null;
laadLandnet(CONFIG.radius, "072", GLOBE.klemOpHorizon)
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
    probeerKoppel();
  })
  .catch((e) => console.warn("[atlas v2] landnet niet geladen (nog niet gebakken?):", e.message));

// --- HET KOPPELEN: de vier netten aan elkaar (LAR-518) ---------------------
// Zodra marnet, havens én het landnet er zijn, koppelen we ze via het
// aangewezen register `knooppunten.json` tot één zoekruimte. De keten-router
// (zoekKeten) zoekt hier overheen: route = keten van benen met een overstap op
// een aangewezen knooppunt. Bewust ná het laden en niet gebakken: de offset
// tussen de knoopruimtes wordt hier berekend en zou stil verlopen bij een
// rebake van één van beide netten.
let K = null;
let REGISTER = null;
fetch("data/knooppunten.json?v=070")
  .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`HTTP ${r.status}`))))
  .then((reg) => { REGISTER = reg; probeerKoppel(); })
  .catch((e) => console.warn("[atlas v2] knooppunten.json niet geladen:", e.message));

// --- de stromen-laag (M26.1) -----------------------------------------------
// De aansluitingen moeten mee de koppeling in (ze worden door dezelfde
// snap-machine gehaald), dus ze horen bij het wachten hieronder. De stromen
// zelf zijn puur data en mogen later komen.
let AANSLUITINGEN = null;
let STROMEN = null;
let LEIDINGEN = null;
let stromenGeladen = false;
laadStromen("070")
  .then(({ aansluitingen, stromen, pijpleidingen }) => {
    AANSLUITINGEN = aansluitingen;
    STROMEN = stromen;
    LEIDINGEN = pijpleidingen;
    stromenGeladen = true;
    probeerKoppel();
  })
  .catch((e) => {
    // Een ontbrekende stromenlaag mag de atlas nooit tegenhouden — de rest van
    // de bol staat er los van.
    console.warn("[atlas v2] stromen niet geladen:", e.message);
    stromenGeladen = true;
    probeerKoppel();
  });

function probeerKoppel() {
  if (K || !NET || !HAVENS || !LANDNET || !REGISTER || !stromenGeladen) return;
  try {
    K = koppelNetten({
      marnet: NET, landnet: LANDNET,
      zeeKnopen: HAVENS.zeeKnopen, register: REGISTER,
      aansluitingen: AANSLUITINGEN,
    });
    window.KETEN = K;
    const s = K.stats;
    console.log(
      `[atlas v2] koppeling: ${s.punten} knooppunten · ${s.overstappen} overstappen · ` +
      `${s.gemengdeLandknopen} gemengde landknopen · ergste snap ${s.ergsteSnapKm.toFixed(1)} km · ` +
      `${s.msKoppelen} ms`
    );
    const noot = document.getElementById("ketenNoot");
    if (noot) {
      noot.textContent =
        `${s.punten} aangewezen knooppunten · ${s.overstappen} overslagen · ` +
        `ergste snap ${s.ergsteSnapKm.toFixed(1)} km`;
    }
    // De aangewezen knooppunten óók in de route-keuze, met ◆ ervoor. Zo kun je
    // een landlocked overslagpunt kiezen en het spoornet echt in gebruik zien.
    const lijst = document.getElementById("havenLijst");
    const frag = document.createDocumentFragment();
    for (const p of K.punten) {
      const opt = document.createElement("option");
      opt.value = knoopLabel(p);
      frag.appendChild(opt);
    }
    lijst.appendChild(frag);

    if (s.aansluitingen) {
      console.log(
        `[atlas v2] aansluitingen: ${s.aansluitingen} · ` +
        `ergste last mile ${s.ergsteLastMileKm.toFixed(1)} km`
      );
      const an = document.getElementById("aanslNoot");
      if (an) {
        an.textContent =
          `${s.aansluitingen} aansluitingen op straatniveau · ` +
          `ergste last mile ${s.ergsteLastMileKm.toFixed(1)} km`;
      }
    }
    bouwStromenHud();
  } catch (e) {
    console.error("[atlas v2] koppelen mislukt:", e);
  }
}

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
  if (LANDNET) {
    // Onder het zeenet: waar spoor en water samenkomen hoort het water te winnen.
    const op = Math.max(CONFIG.radius * 2.5e-6, alt * 0.0045);
    LANDNET.lijnen.scale.setScalar(1 + op / CONFIG.radius);
  }
  if (stroomLaag) {
    // Nog iets hoger dan de route: een stroom loopt vaak óver een route heen en
    // moet dan zichtbaar blijven. ⚠️ Dit is de ENIGE lift die de stromenlaag
    // heeft — evenredig met de kijkhoogte, net als de andere vectorlagen. De
    // vaste lift die hier eerst in stroomlaag.js zat (3,8–10,2 km) gaf op
    // straatniveau parallax: je zag de lijn kilometers naast de kade.
    const op = Math.max(CONFIG.radius * 4.5e-6, alt * 0.0065);
    stroomLaag.scale.setScalar(1 + op / CONFIG.radius);
    for (const g of stroomLaag.children) zetMerkGrootte(g, GLOBE.getAltitudeKm());
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

// Een keten-eindpunt kan een haven zijn óf een aangewezen knooppunt. Knooppunten
// dragen ◆ in de lijst; zo kun je een landlocked overslagpunt (Kasumbalesa,
// Wenen, Duisburg) kiezen en dus een zuivere spoor- of binnenvaartroute zien.
const KNOOP_MERK = "◆ ";
function knoopLabel(p) { return `${KNOOP_MERK}${p.naam}`; }

function vindKetenEindpunt(tekst) {
  if (!tekst) return null;
  const t = tekst.trim().toLowerCase();
  if (K) {
    const zonderMerk = t.startsWith(KNOOP_MERK.trim().toLowerCase())
      ? t.slice(KNOOP_MERK.trim().length).trim() : t;
    const p = K.punten.find((x) => knoopLabel(x).toLowerCase() === t)
      || K.punten.find((x) => x.naam.toLowerCase() === zonderMerk);
    if (p) return { kind: "knoop", punt: p, naam: p.naam };
  }
  const h = vindHaven(tekst);
  return h ? { kind: "haven", haven: h, naam: h.naam } : null;
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
  const schip = SCHEEPSKLASSEN[klasseEl.value] || null;

  // "keten": de multi-modale keten-router over álle vier de netten (LAR-518).
  // Aparte tak, want hij geeft een keten van benen terug i.p.v. één route, en
  // hij accepteert ook de aangewezen knooppunten (Kasumbalesa, Wenen, …) als
  // eindpunt — niet alleen havens. Zo is een zuivere spoorroute te bekijken.
  if (SCHIP === "keten") {
    const a = vindKetenEindpunt(vanEl.value);
    const b = vindKetenEindpunt(naarEl.value);
    if (!a || !b) {
      infoEl.textContent = "kies twee punten uit de lijst (haven of ◆ knooppunt)";
      return;
    }
    wisRoute();
    toonKeten(a, b, schip);
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

// --- de keten-router tekenen (LAR-518) -------------------------------------
// Elk been krijgt de kleur van zijn net, zodat je in één oogopslag ziet waar de
// lading van modaliteit wisselt. De overslagpunten markeren we met een witte
// ring: dát is de plek waar het "3 schepen, niet 1" zichtbaar wordt.
const KETEN_KLEUR = {
  zee: 0x49b6ff, binnen: 0xffc94a, spoor: 0x5fe8c8, weg: 0xff9d3d,
};

function opBol3(lon, lat, r) {
  const a = lon * (Math.PI / 180), b = lat * (Math.PI / 180);
  const c = Math.cos(b);
  return new THREE.Vector3(r * c * Math.cos(a), r * Math.sin(b), -r * c * Math.sin(a));
}

function beenLijn(net, been, radius) {
  const pts = [];
  let bij = been.knopen[0];
  for (const e of been.edges) {
    const start = net.geomStart[e], n = net.geomN[e];
    const vooruit = net.edgeA[e] === bij;
    for (let k = 0; k < n; k++) {
      const idx = vooruit ? start + k : start + (n - 1 - k);
      pts.push(net.posities[idx * 3], net.posities[idx * 3 + 1], net.posities[idx * 3 + 2]);
    }
    bij = vooruit ? net.edgeB[e] : net.edgeA[e];
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(new Float32Array(pts), 3));
  const mat = new THREE.LineBasicMaterial({
    color: KETEN_KLEUR[been.groep] ?? 0xffe066, transparent: true, opacity: 0.97,
  });
  // Zelfde dieptebehandeling als de andere vectorlagen (2026-07-22): zonder
  // depthTest:false + horizonklem verdwijnt de lijn achter de bol zodra de
  // tegels geladen zijn — dan zag Lars een route die er niet leek te zijn.
  GLOBE.klemOpHorizon(mat);
  const lijn = new THREE.Line(geo, mat);
  lijn.renderOrder = 8;   // boven landnet (7)
  lijn.frustumCulled = false;
  return lijn;
}

// Zaden voor een keten-eindpunt: een haven (zee/binnen) of een aangewezen
// knooppunt (alle modaliteiten die het punt draagt, incl. spoor/weg).
function eindpuntZaden(ep) {
  return ep.kind === "knoop" ? puntZaden(K, ep.punt) : havenZaden(K, ep.haven);
}

function toonKeten(van, naar, schip) {
  if (!K) {
    infoEl.textContent = "de netten zijn nog niet gekoppeld…";
    return;
  }
  const t0 = performance.now();
  // Standaardprofiel sluit het landnet (de landbrug-regel): een zuivere
  // spoorroute heeft 0 overslagen en zou lexicografisch van zee winnen. De knop
  // "spoor/weg meenemen" zet het open zodat je het spoornet in gebruik kunt zien.
  const netten = landnetMee
    ? ["zee", "binnen", "spoor", "weg"]
    : ["zee", "binnen"];
  const opties = { netten };
  if (schip) { opties.schipZee = schip; opties.schipBinnen = schip; }
  const uit = zoekKeten(K, eindpuntZaden(van), eindpuntZaden(naar), opties);
  const ms = performance.now() - t0;

  if (uit.geenPad) {
    infoEl.innerHTML =
      `<b>geen keten</b> · ${ms.toFixed(0)} ms<br>` +
      `<span style="opacity:.8">${uit.reden}</span>`;
    return;
  }

  const groep = new THREE.Group();
  const netVan = (been) => (been.net === "landnet" ? LANDNET : NET);
  const knoopPos = (net, kLokaal, lift = 1) =>
    opBol3(net.knoopLon[kLokaal], net.knoopLat[kLokaal], CONFIG.radius * lift);

  for (const been of uit.benen) {
    const net = netVan(been);
    if (!net) continue;
    groep.add(beenLijn(net, been, CONFIG.radius));
  }

  // De overstap zelf: een kort verbindingslijntje tussen het eind van het ene
  // been en het begin van het volgende, plus een witte ring op het overslagpunt.
  // Zonder dat lijntje "mist" de route een stukje bij elke overslag — de twee
  // aanhechtingen liggen een paar km uit elkaar (kade ↔ emplacement/riviermond).
  for (let i = 0; i < uit.overstappen.length; i++) {
    const beenA = uit.benen[i], beenB = uit.benen[i + 1];
    const netA = netVan(beenA), netB = netVan(beenB);
    const kEindA = beenA.knopen[beenA.knopen.length - 1];
    const kStartB = beenB.knopen[0];
    const pA = knoopPos(netA, kEindA, 1.0009);
    const pB = knoopPos(netB, kStartB, 1.0009);

    const cGeo = new THREE.BufferGeometry().setFromPoints([pA, pB]);
    const cMat = new THREE.LineBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.9, depthTest: false });
    const connector = new THREE.Line(cGeo, cMat);
    connector.renderOrder = 8.5;
    groep.add(connector);

    const ring = new THREE.Mesh(
      new THREE.SphereGeometry(CONFIG.radius * 0.004, 12, 12),
      new THREE.MeshBasicMaterial({ color: 0xffffff, depthTest: false })
    );
    ring.position.copy(knoopPos(netA, kEindA, 1.001));
    ring.renderOrder = 9;   // boven de benen
    groep.add(ring);
  }
  routeLijn = groep;
  GLOBE.globeGroup.add(routeLijn);

  const legs = uit.benen
    .map((b) => `${b.vervoer} ${Math.round(b.km).toLocaleString("nl")} km`)
    .join(" → ");
  const overs = uit.overstappen.length
    ? `<br>overslag: ${uit.overstappen.map((o) => o.naam).join(" · ")}`
    : "";
  infoEl.innerHTML =
    `<b>${Math.round(uit.km).toLocaleString("nl")} km</b> · ` +
    `${uit.overslagen}× overslag · ${uit.benen.length} benen · ${ms.toFixed(0)} ms` +
    (schip ? ` · klasse ${klasseEl.value}` : "") +
    `<br>${legs}${overs}` +
    (uit.aanloopKm > 20 ? `<br><span style="opacity:.7">aanloop ${Math.round(uit.aanloopKm)} km</span>` : "");
  window.KETENROUTE = uit;
}

// --- DE WERKELIJKE STROMEN (M26.1) -----------------------------------------
// Geen simulator: de keten staat in de data (data/*.js → stromen-pilot.json) en
// per been zoeken we op precies één net. Wat deze laag toevoegt is POSITIONELE
// WAARHEID — elke stroom komt aan op zijn eigen kade, niet op de generieke
// havenstip. Ontwerp: design/stroom-aansluiting.md.

let stroomLaag = null;              // THREE.Group met alle getoonde stromen
const stroomInfoEl = () => document.getElementById("stroomInfo");

function aansluitingOp(id) { return K?.aansluitingen.get(id) || null; }
// De slurry-leidingen: tekengeometrie voor de benen zonder net.
function leidingOp(id) {
  return (LEIDINGEN?.leidingen || []).find((l) => l.id === id) || null;
}

function bouwStromenHud() {
  const lijst = document.getElementById("stromenLijst");
  if (!lijst || !STROMEN) return;
  lijst.innerHTML = "";
  for (const s of STROMEN.stromen) {
    const rij = document.createElement("button");
    rij.className = "stroomBtn";
    rij.innerHTML =
      `<i style="background:${s.kleur}"></i>` +
      `<span><b>${s.naam.replace(/^.*· /, "")}</b><br>` +
      `<small>${s.kort} · ${s.waarde} ${s.eenheid}</small></span>`;
    rij.addEventListener("click", () => toonStromen([s.id], { vlieg: true }));
    lijst.appendChild(rij);
  }
}

function wisStromen() {
  if (stroomLaag) {
    GLOBE.globeGroup.remove(stroomLaag);
    // ⚠️ alleen lijn-geometrie vrijgeven: de markers delen één bolgeometrie
    // (MERK_GEO in stroomlaag.js). Die weggooien maakt de vólgende klik leeg.
    stroomLaag.traverse?.((o) => {
      if (o.isLine) o.geometry?.dispose?.();
      o.material?.dispose?.();
    });
    stroomLaag = null;
  }
  const el = stroomInfoEl();
  if (el) el.innerHTML = "";
}

function toonStromen(ids, { vlieg = false } = {}) {
  if (!K || !STROMEN) return;
  wisStromen();
  const groep = new THREE.Group();
  const uitkomsten = [];

  let i = 0;
  for (const s of STROMEN.stromen) {
    if (!ids.includes(s.id)) continue;
    const g = routeerStroom(K, s, aansluitingOp, leidingOp);
    uitkomsten.push(g);
    groep.add(bouwStroomLaag(g, {
      marnet: NET, landnet: LANDNET, radius: CONFIG.radius,
      klemOpHorizon: GLOBE.klemOpHorizon, stroomIndex: i++,
    }));
  }
  stroomLaag = groep;
  GLOBE.globeGroup.add(groep);
  window.STROOMROUTE = uitkomsten;      // diagnose-handvat, net als KETENROUTE

  toonStroomInfo(uitkomsten);
  if (vlieg && uitkomsten.length === 1) {
    const o = uitkomsten[0].overslagen[0];
    // Regionaal aanvliegen, niet meteen tot de kade: een duik van 8.500 naar
    // 3 km in één seconde vraagt élk tegelniveau z5..z19 tegelijk op. Vanaf
    // hier klik je de overslagnaam aan om door te zakken.
    if (o) GLOBE.vliegNaar(o.bij.lon, o.bij.lat, 120, 1500);
  }
}

// De informatieregel is hier geen sierraad: hij is de enige plek waar een been
// zónder pad zichzelf kan melden. Een gat stil laten vallen zou precies de
// vergissing zijn die het routeren moest blootleggen.
function toonStroomInfo(uitkomsten) {
  const el = stroomInfoEl();
  if (!el) return;
  const stukken = [];
  for (const g of uitkomsten) {
    const regels = g.benen.map((b) => {
      const naam = `${b.van?.naam || b.van} → ${b.naar?.naam || b.naar}`.replace(/ — [^→]*/g, "");
      if (b.status === "ok") {
        const lm = b.lastMileKm > 1
          ? ` <span style="opacity:.6">(+${Math.round(b.lastMileKm)} km last mile)</span>` : "";
        return `<div>· ${b.vervoer} <b>${Math.round(b.km).toLocaleString("nl")} km</b>${lm}<br>` +
               `<small style="opacity:.65">${naam}</small></div>`;
      }
      if (b.status === "eigen") {
        // Compleet, alleen niet over een gedeeld net — dus geen waarschuwkleur.
        return `<div>· ${b.vervoer} <b>${Math.round(b.km).toLocaleString("nl")} km</b> ` +
               `<span style="opacity:.6">(eigen verbinding)</span><br>` +
               `<small style="opacity:.65">${b.van?.naam || b.van} → ${b.naar?.naam || b.naar}</small></div>`
                 .replace(/ — [^→<]*/g, "");
      }
      if (b.status === "onbekend" || b.status === "geenNet") {
        return `<div style="color:#ffc94a">· ${b.modus} ~${Math.round(b.km).toLocaleString("nl")} km ` +
               `<b>— route onbekend</b><br><small style="opacity:.7">${b.reden}</small></div>`;
      }
      return `<div style="color:#ff8a7a">· ${b.modus || b.net} <b>— ${b.status === "geenPad" ? "geen pad" : b.status}</b>` +
             `<br><small style="opacity:.7">${b.reden || ""}</small></div>`;
    }).join("");

    const oversl = g.overslagen.map((o) =>
      `<a href="#" data-lon="${o.bij.lon}" data-lat="${o.bij.lat}" class="naarKade">` +
      `${o.bij.naam.split(" — ")[0]}</a> <small>(${o.van}→${o.naar})</small>`).join(" · ");

    stukken.push(
      `<div class="stroomKaart" style="border-left-color:${g.stroom.kleur}">` +
      `<b>${Math.round(g.km).toLocaleString("nl")} km</b> · ` +
      `${g.overslagen.length}× overslag` +
      (g.gaten ? ` · <span style="color:#ffc94a">${g.gaten} gat${g.gaten > 1 ? "en" : ""}</span>` : "") +
      `${regels}` +
      (oversl ? `<div style="margin-top:4px">overslag: ${oversl}</div>` : "") +
      `</div>`
    );
  }
  el.innerHTML = stukken.join("");
  // Op de overslagnaam klikken = ernaartoe vliegen tot straatniveau. Dát is de
  // toets van deze laag: ligt de lijn op z17 in het juiste bekken?
  for (const a of el.querySelectorAll("a.naarKade")) {
    a.addEventListener("click", (e) => {
      e.preventDefault();
      GLOBE.vliegNaar(+a.dataset.lon, +a.dataset.lat, 2.5, 1800);
    });
  }
}

document.getElementById("stromenAlle")?.addEventListener("click", () => {
  toonStromen((STROMEN?.stromen || []).map((s) => s.id));
});
document.getElementById("stromenWis")?.addEventListener("click", wisStromen);

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

// Landnet meenemen in de keten (spoor + weg). Default UIT: de landbrug-regel
// (een zuivere spoorroute heeft 0 overslagen en wint anders lexicografisch van
// zee). Aan = je kunt het spoornet in gebruik zien, bv. een landlocked ◆-punt.
let landnetMee = false;
const landnetMeeEl = document.getElementById("landnetMee");
const landnetMeeRij = document.getElementById("landnetMeeRij");
if (landnetMeeEl) {
  landnetMeeEl.addEventListener("change", () => {
    landnetMee = landnetMeeEl.checked;
    if (vanEl.value && naarEl.value && SCHIP === "keten") toonRoute();
  });
}

function toonLandnetKnop() {
  // alleen zinvol in keten-modus
  if (landnetMeeRij) landnetMeeRij.style.display = SCHIP === "keten" ? "" : "none";
}

for (const b of document.querySelectorAll(".schipBtn")) {
  b.addEventListener("click", () => {
    SCHIP = b.dataset.schip;
    for (const o of document.querySelectorAll(".schipBtn")) o.classList.toggle("is-on", o === b);
    toonLandnetKnop();
    if (vanEl.value && naarEl.value) toonRoute();
  });
}
toonLandnetKnop();

document.getElementById("routeGo").addEventListener("click", toonRoute);
document.getElementById("routeWis").addEventListener("click", wisRoute);
for (const el of [vanEl, naarEl]) {
  el.addEventListener("keydown", (e) => { if (e.key === "Enter") toonRoute(); });
}

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
wireButtons(".mnBtn", "mn", (mode) => {
  if (NET) NET.lijnen.visible = (mode === "aan");
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
