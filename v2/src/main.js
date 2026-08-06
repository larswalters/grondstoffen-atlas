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

import { createGlobe, CONFIG } from "./globe.js?v=100";
import { laadVectorWereld } from "./world.js?v=070";
import { createTileLayer } from "./tiles.js?v=070";
import { laadHavens } from "./marnet.js?v=077";
import { bouwHavenLaag, zetHavenGrootte, koppelHavenLabel } from "./havens.js?v=070";
import { laadLandnet } from "./landnet.js?v=070";
import { laadAisnet } from "./aisnet.js?v=084";
import { laadAisgloed } from "./aisgloed.js?v=086";
import { laadAisPings, ververs as ververspings, zetPingGrootte } from "./aispings.js?v=087";
import { laadAisTracks } from "./aistracks.js?v=090";
import { laadStroomroute } from "./stroomroute.js?v=102";
import { laadAnkercheck } from "./ankercheck.js?v=098";
import { laadGloednodes } from "./gloednodes.js?v=113";
import { laadStroomleven } from "./stroomleven.js?v=113";

const GLOBE = createGlobe(document.getElementById("canvasWrap"));

// ⚠️ ALLE VECTORLAGEN OP DE SCHIL VAN DE DIEPSTE TEGELS, niet op `radius`.
// Zie de toelichting bij CONFIG.vectorLift in globe.js: de detailtegels liggen
// 130 m boven `radius`, en een lijn eronder verschuift schuin bekeken zichtbaar.
// Eén constante voor alle lagen, zodat ze onderling per constructie niet uit
// elkaar kunnen lopen.
const VECTOR_R = CONFIG.radius * CONFIG.vectorLift;

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

laadVectorWereld(VECTOR_R, GLOBE.klemOpHorizon)
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
laadLandnet(VECTOR_R, "102", GLOBE.klemOpHorizon)
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

// --- het AIS-waternet (M27, pilot) -----------------------------------------
// De eerste zichtbare stap van de ombouw: vaargeulen afgeleid uit World Bank
// AIS-density (bake_aisnet.py), vier testvensters — Tongling · Nederland ·
// Patache · Shanghai. Kijk-laag: eerst moet de lijn in de echte geul liggen,
// dan pas wordt dit een graaf met knopen en haven-aanhechting.
let AISNET = null;
laadAisnet(VECTOR_R, "085", GLOBE.klemOpHorizon)
  .then((an) => {
    AISNET = an;
    // standaard UIT (besluit Lars 2026-07-25): het beeld komt van de gloed-
    // laag; de lijnen blijven als graaf-zaad achter hun eigen HUD-knop.
    an.lijnen.visible = false;
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
  })
  .catch((e) => console.warn("[atlas v2] aisnet niet geladen (nog niet gebakken?):", e.message));

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

// --- de stroom-preview: grafiet Balama → VS (M28) ---------------------------
// De eerste echte grondstofstroom end-to-end op de bol, routebrief-gestuurd
// (v2/design/routebrieven/grafiet-balama-vidalia.md): truck Balama → Nacala
// (echte N380/N1-weggeometrie) → gestippelde haven-aanloop → zeeschip
// Kaap-route → barge via Port Allen → Port of Vidalia (mijl 359) → last mile
// per truck. Kleur = modaliteit, zodat de overgang tussen de netten
// zichtbaar is; gestippeld = schematische verbinding. Klein bestand
// (< 300 KB), dus eager zoals het landnet — niet het lazy aistracks-patroon.
// ⚠️ VIER STROMEN sinds 2026-07-28, elk met een eigen bestand, een eigen groep
// en een eigen knop. Ze delen bewust één kleurtabel (kleur = MODALITEIT, niet
// grondstof): het punt van deze laag is de overgang tussen de netten laten
// zien, en die overgang moet in elke stroom hetzelfde lezen. Welke stroom je
// ziet zeg je met de knoppen, niet met de kleur.
const STROMEN = [
  { sleutel: "grafiet", bestand: "stroomroute-pilot.json", aan: true },
  { sleutel: "cu-eg", bestand: "stroomroute-koper-escondida-guixi.json", aan: true },
  { sleutel: "cu-ct", bestand: "stroomroute-koper-collahuasi-tongling.json", aan: true },
  { sleutel: "cu-ld", bestand: "stroomroute-koper-lobito-duisburg.json", aan: true },
  // ⚠️ Deze stroom eindigt bewust in de vaargeul vóór Zhangjiagang en niet bij
  // de fabriek: de losplek en de twee Chinese fabrieksankers staan nog open in
  // de routebrief (§5). Liever een been dat ophoudt waar het bewijs ophoudt dan
  // een lijn naar een plausibel-maar-ongelegd punt (de Waalhaven-klasse).
  { sleutel: "li-gz", bestand: "stroomroute-lithium-greenbushes-zhangjiagang.json", aan: true },
];
const STROOMROUTES = new Map();
let STROOMROUTE = null;              // de eerste, als diagnose-handvat

const STROOM_LABEL = {
  zee: "zeeschip", binnenvaart: "binnenschip", truck: "truck",
  spoor: "trein", leiding: "leiding",
};

function stroomRegel(s) {
  // Benen met dezelfde modaliteit tellen op tot één regel — een zeebeen dat op
  // een via-punt uit de routebrief gesplitst is, blijft één zeeschip.
  const per = new Map();
  for (const b of s.benen) {
    const k = STROOM_LABEL[b.modaliteit] || b.naam || b.modaliteit;
    per.set(k, (per.get(k) || 0) + b.km);
  }
  return [...per].map(([k, km]) =>
    `${k} ${Math.round(km).toLocaleString("nl")} km`).join(" · ");
}

function toonStroomNoot() {
  const noot = document.getElementById("stroomNoot");
  if (!noot) return;
  const regels = [];
  for (const { sleutel } of STROMEN) {
    const s = STROOMROUTES.get(sleutel);
    if (s && s.groep.visible) regels.push(`${s.titel} — ${stroomRegel(s)}`);
  }
  noot.textContent = regels.length ? regels.join("\n") : "geen stroom aan";
}

for (const def of STROMEN) {
  laadStroomroute(VECTOR_R, "111", GLOBE.klemOpHorizon, def.bestand)
    .then((s) => {
      s.groep.visible = def.aan;
      STROOMROUTES.set(def.sleutel, s);
      STROOMROUTE = STROOMROUTE || s;
      GLOBE.globeGroup.add(s.groep);
      window.STROOMROUTES = STROOMROUTES;   // diagnose-handvat
      console.log(`[atlas v2] stroom ${def.sleutel}: ${s.titel} · ${stroomRegel(s)}`);
      toonStroomNoot();
    })
    .catch((e) => console.warn(
      `[atlas v2] stroom ${def.sleutel} niet geladen (nog niet gebakken?):`, e.message));
}

// --- de stromen laten leven (M26 / LAR-490) --------------------------------
// Koker + bewegende deeltjes NAAST stroomroute.js, niet erdoorheen: die laag is
// bewezen en tekent de exacte lijn in de legenda-kleur. Zie de kop van
// stroomleven.js voor waarom de lijn op de grond blijft.
const STROOMLEVEN = new Map();
for (const def of STROMEN) {
  laadStroomleven(VECTOR_R, "113", GLOBE.klemOpHorizon, def.bestand,
                  GLOBE.renderer, GLOBE.camera)
    .then((l) => {
      l.groep.visible = def.aan;
      STROOMLEVEN.set(def.sleutel, l);
      GLOBE.globeGroup.add(l.groep);
      GLOBE.onTick((dt) => l.update(dt));
      window.STROOMLEVEN = STROOMLEVEN;   // diagnose-handvat
      console.log(
        `[atlas v2] stroomleven ${def.sleutel}: ${l.stats.benen} benen · ` +
        `${l.stats.schillen} kokerschillen · ${l.stats.deeltjes} deeltjes`
      );
    })
    .catch((e) => console.warn(
      `[atlas v2] stroomleven ${def.sleutel} niet geladen:`, e.message));
}
// LineMaterial rekent in pixels en moet de vensterafmeting kennen; bijhouden in
// de tick is goedkoper dan een resize-listener die de kaart moet kennen.
GLOBE.onTick(() => {
  const c = GLOBE.renderer.domElement;
  for (const l of STROOMLEVEN.values()) l.zetResolutie(c.width, c.height);
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
let ANKERCHECK = null;
laadAnkercheck(VECTOR_R, "098", GLOBE.klemOpHorizon)
  .then((a) => {
    ANKERCHECK = a;
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
  })
  .catch((e) => console.warn("[atlas v2] ankercheck niet geladen:", e.message));

// --- de AIS-drukte als gloed (M27) -----------------------------------------
// Het dichtheidsveld zélf op de bol (besluit Lars 2026-07-25): de blauwe
// gloed van zes jaar scheepvaart, additief per pilotvenster — dít is het
// beeld; de lijnen hierboven zijn het graaf-zaad.
let AISGLOED = null;
laadAisgloed(VECTOR_R, "086", GLOBE.klemOpHorizon)
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

// --- de uitgezochte knopen als gloed (M26 / LAR-490) -----------------------
// De dichtbij-helft van het LOD-ontwerp. Alleen SITES lichten op; dat Tongling
// en Guixi op wereldhoogte één vlek worden hoort te ONTSTAAN uit de optelling.
// Zie de kop van gloednodes.js — als hier alsnog een hotspot-object nodig blijkt,
// klopt de ontwerpbrief niet.
let GLOEDNODES = null;
laadGloednodes(VECTOR_R, "112", GLOBE.camera, GLOBE.renderer)
  .then((g) => {
    GLOEDNODES = g;
    GLOBE.globeGroup.add(g.groep);
    window.GLOEDNODES = g;
    GLOBE.onTick(() => g.update());
    console.log(
      `[atlas v2] gloednodes: ${g.stats.sites} sites (${g.stats.complexen} complexen ` +
      `bewust niet getekend) · laden ${g.stats.msLaden} ms`
    );
    const noot = document.getElementById("gloedNodeNoot");
    if (noot) {
      noot.textContent =
        `${g.stats.sites} uitgezochte kopersites · Tongling en Guixi`;
    }
  })
  .catch((e) => console.warn("[atlas v2] gloednodes niet geladen:", e.message));

// --- de ruwe AIS-pings als debuglaag (M28, LAR-535) ------------------------
// Het venster op wat de collector op de VPS binnenkrijgt. Hiermee beoordeel je
// DEKKING terwijl je kijkt: een leeg stuk rivier in de graaf kan "geen schepen"
// óf "geen ontvanger" betekenen, en alleen deze laag laat het verschil zien.
// Puur weergave — de echte tracks worden gebouwd in LAR-530.
let AISPINGS = null;
function toonPingNoot() {
  const noot = document.getElementById("pingNoot");
  if (!noot || !AISPINGS) return;
  const s = AISPINGS.stats;
  const vers = s.jongsteMin === null ? "—"
    : s.jongsteMin < 60 ? `${s.jongsteMin} min`
    : `${Math.round(s.jongsteMin / 60)} u`;
  noot.textContent =
    `${s.punten.toLocaleString("nl")} pings · ${s.schepen.toLocaleString("nl")} schepen · ` +
    `laatste ${vers} geleden · ${s.uren} u venster, korrel ${s.korrelMin} min`;
}
laadAisPings(VECTOR_R)
  .then((p) => {
    AISPINGS = p;
    GLOBE.globeGroup.add(p.punten);
    window.AISPINGS = p;
    const s = p.stats;
    console.log(
      `[atlas v2] aispings: ${s.punten.toLocaleString("nl")} punten · ` +
      `${s.schepen.toLocaleString("nl")} schepen (${s.varend.toLocaleString("nl")} varend) · ` +
      `laden ${s.msLaden} ms, verwerken ${s.msVerwerken} ms`
    );
    toonPingNoot();
  })
  // Zacht falen: de VPS is geen dragende afhankelijkheid van de atlas.
  .catch((e) => {
    console.warn("[atlas v2] aispings niet geladen (VPS bereikbaar?):", e.message);
    const noot = document.getElementById("pingNoot");
    if (noot) noot.textContent = "geen verbinding met de collector op de VPS";
  });

// De publisher op de VPS draait elk kwartier; ververs alleen zolang de laag
// zichtbaar is, zodat een dichtgeklapte HUD geen verkeer veroorzaakt.
setInterval(() => {
  if (!AISPINGS || !AISPINGS.punten.visible) return;
  ververspings(AISPINGS, VECTOR_R)
    .then(toonPingNoot)
    .catch((e) => console.warn("[atlas v2] aispings verversen mislukt:", e.message));
}, 5 * 60 * 1000);

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
  if (AISPINGS && AISPINGS.punten.visible) {
    // Zelfde plank als het AIS-net: dit is water-materiaal, geen haven.
    const op = Math.max(CONFIG.radius * 3.5e-6, alt * 0.0055);
    AISPINGS.punten.scale.setScalar(1 + op / CONFIG.radius);
    zetPingGrootte(AISPINGS, GLOBE.getAltitudeKm(), GLOBE.renderer.getPixelRatio());
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
wireButtons(".anBtn", "an", (mode) => {
  if (AISNET) AISNET.lijnen.visible = (mode === "aan");
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
// Eén knop per stroom (data-sr = de sleutel uit STROMEN) — geen aan/uit-paar
// maar een schakelaar per stroom, want met vier stromen tegelijk op de bol is
// "welke wil ik nu zien" de vraag, niet "laag aan of uit".
for (const knop of document.querySelectorAll(".srBtn")) {
  knop.addEventListener("click", () => {
    const sleutel = knop.dataset.sr;
    const s = STROOMROUTES.get(sleutel);
    if (!s) return;
    s.groep.visible = !s.groep.visible;
    // De levenslaag hoort bij dezelfde stroom en volgt dus dezelfde knop —
    // anders blijven er koker en deeltjes zweven boven een lijn die weg is.
    const l = STROOMLEVEN.get(sleutel);
    if (l) l.groep.visible = s.groep.visible;
    knop.classList.toggle("is-on", s.groep.visible);
    toonStroomNoot();
  });
}
wireButtons(".akBtn", "ak", (mode) => {
  if (ANKERCHECK) ANKERCHECK.groep.visible = (mode === "aan");
});
wireButtons(".glBtn", "gl", (mode) => {
  if (AISGLOED) AISGLOED.groep.visible = (mode === "aan");
});
wireButtons(".gnBtn", "gn", (mode) => {
  if (GLOEDNODES) GLOEDNODES.groep.visible = (mode === "aan");
});
document.querySelectorAll(".gnGa").forEach((knop) => {
  knop.addEventListener("click", () => {
    GLOBE.vliegNaar(+knop.dataset.lon, +knop.dataset.lat, +knop.dataset.km);
  });
});
wireButtons(".apBtn", "ap", (mode) => {
  if (!AISPINGS) return;
  AISPINGS.punten.visible = (mode === "aan");
  // Bij aanzetten meteen de verste stand ophalen: de laag kan uren uit hebben
  // gestaan en dan is de zichtbare data ouder dan het venster suggereert.
  if (mode === "aan") {
    ververspings(AISPINGS, VECTOR_R)
      .then(toonPingNoot)
      .catch(() => {});
  }
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
  statsEl.textContent = tekst;
});

// Handvat voor diagnose vanuit de console/devtools. Dit project wordt veel
// visueel geverifieerd; zonder globals is er anders geen enkele manier om de
// scene van buitenaf te bevragen (ES-modules hebben geen window-scope).
window.GLOBE = GLOBE;
window.TEGELS = TEGELS;

console.log("[atlas v2] three r185 · ACES · tegels tot z19 · schone bol — AIS-waternet in opbouw (oud waternet: tag pre-ais-net)");
