// toets_spoorroute.mjs — punt-naar-punt over het SPOORNET: snap, Dijkstra, GeoJSON.
//
// Waarom dit tool bestaat: het landnet (v2/data/landnet.bin) draagt spoor én weg
// door elkaar, en er was nog geen los gereedschap om een concreet spoor-been
// (fabriek → fabriek) na te rekenen én de gevolgde lijn op de kaart te leggen.
// Dit tool doet precies dat, headless, met twee projectlessen ingebakken:
//
//   1. SNAP OP HET HOOFDNET (spoor-component >= --hoofd-km, default 1.000 km),
//      niet op de dichtstbijzijnde knoop hoe dan ook — anders snap je op een los
//      rangeersporentje en geeft álles "geen pad" (de LAR-518-les; zelfde
//      drempel als koppelNetten en toets_spoor_aansluiting.mjs). De absolute
//      dichtste spoorknoop wordt wél gerapporteerd, zodat zichtbaar is wanneer
//      de hoofdnet-eis een dichtere stub overslaat.
//      ⚠️ MAAR DIE EIS HEEFT EEN BOVENGRENS (--max-snap, default 60 km), en die
//      ontbrak hier terwijl `koppelNetten` hem wél had (MAX_LAND_SNAP_KM, zie
//      v2/src/keten.js). Zonder grens zoekt de eis door tot ze ergens een groot
//      net vindt: bij Cerrejón (mijnspoor op een component van 156 km) landde
//      het uiteinde 1.025 km verderop IN CUBA, en omdat de laadlus én Puerto
//      Bolívar op diezelfde Cubaanse knoop uitkwamen meldde het tool geen "geen
//      pad" maar een gedegenereerd been — plausibel-fout in plaats van
//      luid-fout. Boven de grens valt het punt daarom terug op de
//      dichtstbijzijnde spoorknoop; liggen beide uiteinden dan op hetzelfde
//      kleine component, dan is dát de echte lijn. Ligt er niets, dan komt er
//      eerlijk "geen pad" uit. 106 van de 642 registerknopen hangen onder de
//      1.000 km-drempel, dus dit raakt meer dan één stroom.
//      ⚠️ De absolute drempel zelf is een erfenis: de haven-riviersnap ging op
//      2026-07-24 juist van absoluut naar RELATIEF (doorgaand component, hooguit
//      2x+1 km verder, cap 60) omdat een absolute drempel Whitby/Rostock 58 km
//      wegteleporteerde. Dezelfde klasse; spoor mag die kant ook nog op.
//   2. DE LIJNGEOMETRIE PER EDGE HEEFT EEN RICHTING (eerste vertex = knoop A);
//      wie de edge van B naar A loopt moet de reeks omkeren, anders springt de
//      getekende route op elke knoop heen en weer.
//
// Dijkstra op edgeKm volstaat (251k knopen, geen A* nodig); alleen edges met
// edgeModus !== 2 (spoor) doen mee — in de union-find, de snap én de relaxatie.
// Sanity in de uitvoer: de route-km wordt expliciet tegen de grootcirkel-afstand
// tussen de twee punten gelegd (route korter dan grootcirkel = bug in dit
// script), en bij "geen pad" worden de component-km aan beide kanten
// gerapporteerd (diagnose, geen fix).
//
// Draaien:
//   node v2/tools/toets_spoorroute.mjs "--van=LAT,LON" "--naar=LAT,LON" [--naam=slug]
//                                       [--hoofd-km=1000] [--max-snap=60]
// Uitvoer: kernregels op de console + de gevolgde lijn als GeoJSON in
//   v2/build-cache/ais/graaf/spoorroute-<naam>.geojson

import { writeFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { laadLandnetHeadless } from "./laad_headless.mjs";

const V2 = dirname(dirname(fileURLToPath(import.meta.url)));
const UITMAP = join(V2, "build-cache", "ais", "graaf");
const STRAAL = 2.4;          // bolstraal van `posities` (afspraak z = -sin lon)
const AARDE_KM = 6371;

// --- CLI ---
const args = {};
for (const a of process.argv.slice(2)) {
  const m = a.match(/^--([^=]+)=(.*)$/);
  if (m) args[m[1]] = m[2];
}
// Hoofdnet-drempel en de bovengrens erop. Vlaggen en geen constanten, omdat een
// legitiem nationaal net kleiner kan zijn dan de drempel (Colombia 156 km,
// Peru 854) — dat is geen rangeerstub maar de lijn waar de stroom overheen gaat.
const HOOFD_KM = getal("hoofd-km", 1000);   // zie toets_spoor_aansluiting.mjs
const MAX_SNAP_KM = getal("max-snap", 60);  // = MAX_LAND_SNAP_KM in keten.js
function getal(sleutel, standaard) {
  if (args[sleutel] === undefined) return standaard;
  const v = Number(args[sleutel]);
  if (!Number.isFinite(v) || v < 0) {
    console.error(`--${sleutel} moet een getal >= 0 zijn (kreeg "${args[sleutel]}")`);
    process.exit(1);
  }
  return v;
}
function leesPunt(sleutel) {
  const v = args[sleutel];
  const delen = (v || "").split(",").map(Number);
  if (delen.length !== 2 || delen.some((x) => !Number.isFinite(x))) {
    console.error(`gebruik: node v2/tools/toets_spoorroute.mjs "--van=LAT,LON" "--naar=LAT,LON" [--naam=slug]`);
    process.exit(1);
  }
  return { lat: delen[0], lon: delen[1] };
}
const van = leesPunt("van"), naar = leesPunt("naar");
const naam = (args.naam || `${van.lat}_${van.lon}--${naar.lat}_${naar.lon}`)
  .replace(/[^A-Za-z0-9._-]+/g, "-");

// --- landnet + spoor-componenten (union-find UITSLUITEND over spoor-edges) ---
const L = laadLandnetHeadless();
const { adjStart, adjEdge, adjKnoop, knoopLon, knoopLat,
        edgeA, edgeB, edgeKm, edgeModus, geomN, geomStart, posities, stats } = L;
const n = stats.knopen, m = stats.edges;

const par = new Int32Array(n).map((_, i) => i);
const find = (x) => { while (par[x] !== x) { par[x] = par[par[x]]; x = par[x]; } return x; };
const spoorKnoop = new Uint8Array(n);
let nSpoorEdges = 0, spoorKmTotaal = 0;
for (let e = 0; e < m; e++) {
  if (edgeModus[e] === 2) continue;            // weg doet niet mee
  nSpoorEdges++; spoorKmTotaal += edgeKm[e];
  spoorKnoop[edgeA[e]] = 1; spoorKnoop[edgeB[e]] = 1;
  const a = find(edgeA[e]), b = find(edgeB[e]);
  if (a !== b) par[a] = b;
}
const compKm = new Map();
for (let e = 0; e < m; e++) {
  if (edgeModus[e] === 2) continue;
  const r = find(edgeA[e]);
  compKm.set(r, (compKm.get(r) || 0) + edgeKm[e]);
}
let grootsteKm = 0;
for (const km of compKm.values()) if (km > grootsteKm) grootsteKm = km;

console.log(`\n=== spoorroute · ${naam} ===`);
console.log(`spoornet: ${nSpoorEdges} spoor-edges (${m - nSpoorEdges} weg-edges genegeerd) · ` +
  `${compKm.size} componenten · grootste ${Math.round(grootsteKm).toLocaleString("nl-NL")} km · ` +
  `totaal ${Math.round(spoorKmTotaal).toLocaleString("nl-NL")} spoor-km`);

// --- snap: dichtste hoofdnet-knoop + absolute dichtste spoorknoop ---
// Dot-product op de eenheidsbol is monotoon in de afstand; conventie hier
// z = +cos(lat)·sin(lon), dezelfde als eenheidsXYZ zou geven — zolang punt en
// knoop dezelfde formule gebruiken is het teken van z irrelevant voor de hoek.
const rad = Math.PI / 180;
function eenheids(p) {
  const c = Math.cos(p.lat * rad);
  return [c * Math.cos(p.lon * rad), Math.sin(p.lat * rad), c * Math.sin(p.lon * rad)];
}
const kmUitDot = (d) => AARDE_KM * Math.acos(Math.max(-1, Math.min(1, d)));

function snapSpoor(p, etiket) {
  const [sx, sy, sz] = eenheids(p);
  let hoofdKnoop = -1, hoofdDot = -2, dichtstKnoop = -1, dichtstDot = -2;
  for (let k = 0; k < n; k++) {
    if (!spoorKnoop[k]) continue;
    const c = Math.cos(knoopLat[k] * rad);
    const d = sx * c * Math.cos(knoopLon[k] * rad) + sy * Math.sin(knoopLat[k] * rad)
            + sz * c * Math.sin(knoopLon[k] * rad);
    if (d > dichtstDot) { dichtstDot = d; dichtstKnoop = k; }
    if ((compKm.get(find(k)) || 0) >= HOOFD_KM && d > hoofdDot) { hoofdDot = d; hoofdKnoop = k; }
  }
  const uit = {
    knoop: hoofdKnoop, km: kmUitDot(hoofdDot),
    dichtstKnoop, dichtstKm: kmUitDot(dichtstDot),
    dichtstCompKm: compKm.get(find(dichtstKnoop)) || 0,
    teruggevallen: false,
  };
  // De hoofdnet-eis heeft een BOVENGRENS. Ligt het dichtstbijzijnde grote net
  // verder dan --max-snap, dan is dit geen "stub overslaan" meer maar een
  // teleport: het uiteinde landt op een net waar deze plek fysiek niet aan
  // vastzit. Terugvallen op de dichtstbijzijnde spoorknoop is dan het eerlijke
  // antwoord — zitten beide uiteinden op hetzelfde kleine component, dan ís dat
  // de echte lijn; zit er niets, dan volgt hieronder gewoon "geen pad".
  if (hoofdKnoop < 0 || uit.km > MAX_SNAP_KM) {
    const reden = hoofdKnoop < 0
      ? `geen enkel component >= ${HOOFD_KM.toLocaleString("nl-NL")} km in het net`
      : `dichtstbijzijnde hoofdnet ligt ${uit.km.toFixed(2)} km weg (> --max-snap ${MAX_SNAP_KM})`;
    console.log(`${etiket} (${p.lat}, ${p.lon}): ⚠️ TERUGVAL op de dichtste ` +
      `spoorknoop ${dichtstKnoop} op ${uit.dichtstKm.toFixed(2)} km · component ` +
      `${Math.round(uit.dichtstCompKm).toLocaleString("nl-NL")} km — ${reden}. ` +
      `De hoofdnet-eis wordt hier NIET toegepast; verhoog --max-snap alleen met ` +
      `een reden, want een verre snap tekent een lijn die er niet ligt.`);
    uit.knoop = dichtstKnoop;
    uit.km = uit.dichtstKm;
    uit.teruggevallen = true;
    return uit;
  }
  const overgeslagen = dichtstKnoop !== hoofdKnoop
    ? ` (dichtste spoorknoop ${uit.dichtstKm.toFixed(2)} km op stub-component van ` +
      `${Math.round(uit.dichtstCompKm).toLocaleString("nl-NL")} km — overgeslagen door de hoofdnet-eis)`
    : ``;
  console.log(`${etiket} (${p.lat}, ${p.lon}): snap hoofdnet-knoop ${uit.knoop} op ` +
    `${uit.km.toFixed(2)} km · component ${Math.round(compKm.get(find(uit.knoop)) || 0)
      .toLocaleString("nl-NL")} km${overgeslagen}`);
  return uit;
}
const snapVan = snapSpoor(van, "van "), snapNaar = snapSpoor(naar, "naar");

// ⚠️ BEIDE UITEINDEN OP DEZELFDE KNOOP = GEEN BEEN, EN DAT MOET LUID ZIJN.
// Dit is de faalvorm die de Cerrejón-diagnose zo lang verborg: de ongeremde
// hoofdnet-eis stuurde de laadlus én Puerto Bolívar naar dezelfde knoop 1.000 km
// verderop, waarna Dijkstra netjes een pad van lengte nul vond. Geen "geen pad",
// geen foutmelding — een gedegenereerd been met de echte meting in een terzijde.
// Een route van een knoop naar zichzelf is nooit een geldig antwoord.
if (snapVan.knoop === snapNaar.knoop) {
  console.log(`GEDEGENEREERD: beide uiteinden snappen op knoop ${snapVan.knoop} ` +
    `(van ${snapVan.km.toFixed(2)} km · naar ${snapNaar.km.toFixed(2)} km). ` +
    `Er is geen been tussen een knoop en zichzelf. Meestal betekent dit dat het ` +
    `spoor dat deze twee plekken verbindt niet in het net zit, of dat de ` +
    `snap-afstanden te groot zijn voor de vraag die je stelt.`);
  process.exit(2);
}

// --- richting per edge-uiteinde: waar wijst de rail als je hier wegrijdt? -----
// Nodig voor de bochtstraf hieronder. `uitA[e]` = de peiling waarmee je knoop A
// verlaat langs edge e (uit de EERSTE geometrie-segmenten, niet uit de rechte
// lijn knoop-naar-knoop: een edge van 1,5 km met een bocht erin zou anders een
// richting krijgen die hij nergens heeft). Idem `uitB[e]` vanaf knoop B.
const MIN_SEG_M = 5;    // korter dan dit zegt niets over richting (dubbele vertex)

function peilingUitGeom(e, vanafA) {
  const start = geomStart[e], nV = geomN[e];
  const lees = (j) => {
    const i = start + (vanafA ? j : nV - 1 - j);
    const x = posities[i * 3], y = posities[i * 3 + 1], z = posities[i * 3 + 2];
    return [Math.atan2(-z, x) / rad,
            Math.asin(Math.max(-1, Math.min(1, y / STRAAL))) / rad];
  };
  const [lo0, la0] = lees(0);
  for (let j = 1; j < nV; j++) {
    const [lo1, la1] = lees(j);
    const dx = (lo1 - lo0) * Math.cos((la0 + la1) / 2 * rad) * 111320;
    const dy = (la1 - la0) * 110574;
    const d = Math.hypot(dx, dy);
    if (d >= MIN_SEG_M) return [Math.atan2(dx, dy) / rad, d];
  }
  return [NaN, 0];   // edge zonder bruikbare lengte: geen richting, geen straf
}
const uitA = new Float64Array(edgeKm.length);
const uitB = new Float64Array(edgeKm.length);
const lenA = new Float64Array(edgeKm.length);   // lengte van het eerste segment
const lenB = new Float64Array(edgeKm.length);
for (let e = 0; e < edgeKm.length; e++) {
  if (edgeModus[e] === 2) { uitA[e] = uitB[e] = NaN; continue; }
  [uitA[e], lenA[e]] = peilingUitGeom(e, true);
  [uitB[e], lenB[e]] = peilingUitGeom(e, false);
}
const peilingUit = (e, k) => (edgeA[e] === k ? uitA[e] : uitB[e]);
const segLenUit = (e, k) => (edgeA[e] === k ? lenA[e] : lenB[e]);

// --- de bochtstraf: waarom een kale Dijkstra hier niet volstaat --------------
// ⚠️ GEMETEN, NIET BEDACHT (2026-07-28, op Lars' observatie "de trein maakt 2
// bochten die niet kunnen"). Zonder draaikosten is OMKEREN GRATIS, en dan doet
// het kortste pad precies wat een trein niet kan: het rijdt een aftakking op en
// meteen weer terug als dat een paar meter scheelt, en het zigzagt door de
// wissels van een emplacement. Gemeten op Beilun → Guixi (551 km): zeven
// vertices met een richtingswissel ≥ 60°, waarvan vijf KEERPUNTEN van 158-176°
// met boogstralen van **27, 35, 80, 159 en 554 m**. Een vrachtlijn heeft geen
// boog van 27 meter; dat is geen route maar een graaf-artefact.
//
// De straf is bewust in KILOMETERS uitgedrukt en niet als verbod, want een
// echte kopmaak-beweging bestáát (bij Guixi rangeert de trein aantoonbaar op
// het station). Een verbod zou die route onmogelijk maken en "geen pad" geven;
// een prijs laat hem alleen winnen als er werkelijk geen alternatief is.
//
// De drempels volgen de meetkunde, niet de smaak: bij een boogstraal onder
// ~150 m ontspoort een goederentrein fysiek, en een wissel op een vrije baan
// buigt zelden meer dan ~30° af. Vandaar: tot 45° gratis, daarboven oplopend,
// en een omkering (≥150°) kost het meest.
const KEERSTRAF_KM = Number(
  (process.argv.find((a) => a.startsWith("--keerstraf=")) || "").split("=")[1] || 25);
const BOCHT_STRAF_KM = [
  [150, KEERSTRAF_KM],   // omkering — alleen met kopmaken/rangeren, dus fors
  [110, Math.min(8, KEERSTRAF_KM / 3)],  // scherpe knik = emplacement-zigzag
  [ 75, Math.min(3, KEERSTRAF_KM / 8)],
  [ 45, Math.min(0.6, KEERSTRAF_KM / 40)],
];

// ⚠️ DE HOEK ALLEEN IS NIET GENOEG — de BOOGSTRAAL is het echte criterium, en
// dat verschil is gemeten. Na de eerste ronde bleef bij Guixi een knik over van
// 77° met segmenten van 15 m aan weerszijden: dat is een boogstraal van ~10 m,
// een wissel-spike waar de lijn 15 m uitwijkt en terugkomt. Dezelfde 77° met
// segmenten van 400 m is een boogstraal van 250 m — een krappe maar echte
// aansluitboog. Op de hoek zijn die twee niet te onderscheiden; op de straal
// wel. Vandaar: R = ((L1+L2)/2) / (2·sin(θ/2)), en onder de fysieke ondergrens
// van een goederenboog (~150 m) is het per definitie geen bocht maar een
// artefact.
const MIN_BOOG_M = 150;
const SPIKE_STRAF_KM = 15.0;

function bochtStrafKm(eIn, eUit, k) {
  if (eIn < 0) return 0;                      // eerste stap: geen inkomende richting
  const a = peilingUit(eIn, k), b = peilingUit(eUit, k);
  if (Number.isNaN(a) || Number.isNaN(b)) return 0;
  // Aankomstrichting = tegengesteld aan "wegrijden langs eIn"; de draai is het
  // verschil tussen die aankomstrichting en de nieuwe wegrijrichting.
  const d = Math.abs(((b - a - 180) % 360 + 540) % 360 - 180);
  let straf = 0;
  for (const [grens, s] of BOCHT_STRAF_KM) { if (d >= grens) { straf = s; break; } }
  if (d >= 30 && d < 150) {
    // ⚠️ De KORTSTE van de twee segmenten, niet het gemiddelde. Gemeten bij
    // Guixi: 15 m aan de ene kant en 993 m aan de andere; het gemiddelde geeft
    // dan een boogstraal van 400 m en de spike glipt erdoor, terwijl de lijn in
    // werkelijkheid 15 m opzij stapt en meteen terug. Wat de knik onmogelijk
    // maakt is de KORTE kant — daar moet de trein de hele draai in maken.
    const L = Math.min(segLenUit(eIn, k), segLenUit(eUit, k));
    const R = L / (2 * Math.sin(d / 2 * rad));
    if (R < MIN_BOOG_M) straf = Math.max(straf, SPIKE_STRAF_KM);
  }
  return straf;
}

// --- Dijkstra over GERICHTE EDGE-TOESTANDEN (edge, richting) -----------------
// ⚠️ De toestand moet de edge zijn en niet de knoop: een bochtstraf hangt af
// van waar je VANDAAN komt, en die informatie bestaat niet in een knoop-
// toestand. Kosten: 2 × aantal spooredges toestanden (~519k) — ruim binnen wat
// deze heap aankan, en het is dezelfde truc als de haltes in de track-graaf.
function dijkstra(bron, doel) {
  const nE = edgeKm.length;
  const dist = new Float64Array(2 * nE).fill(Infinity);
  const prevStaat = new Int32Array(2 * nE).fill(-1);
  const staatKm = new Float64Array(2 * nE).fill(Infinity);   // km zónder straf
  const eindKnoop = (s) => ((s & 1) === 0 ? edgeB[s >> 1] : edgeA[s >> 1]);
  const hK = [], hD = [];                       // binaire min-heap met lazy deletes
  const push = (k, d) => {
    let i = hK.length; hK.push(k); hD.push(d);
    while (i > 0) { const p = (i - 1) >> 1; if (hD[p] <= hD[i]) break;
      [hD[p], hD[i]] = [hD[i], hD[p]]; [hK[p], hK[i]] = [hK[i], hK[p]]; i = p; }
  };
  const pop = () => {
    const k = hK[0], d = hD[0], lk = hK.pop(), ld = hD.pop();
    if (hK.length) { hK[0] = lk; hD[0] = ld;
      let i = 0;
      for (;;) { const l = 2 * i + 1, r = l + 1; let kl = i;
        if (l < hK.length && hD[l] < hD[kl]) kl = l;
        if (r < hK.length && hD[r] < hD[kl]) kl = r;
        if (kl === i) break;
        [hD[kl], hD[i]] = [hD[i], hD[kl]]; [hK[kl], hK[i]] = [hK[i], hK[kl]]; i = kl; }
    }
    return [k, d];
  };
  // startzetten: elke spooredge die de bronknoop raakt, in de wegrijrichting
  for (let i = adjStart[bron]; i < adjStart[bron + 1]; i++) {
    const e = adjEdge[i];
    if (edgeModus[e] === 2) continue;
    const s = (edgeA[e] === bron) ? (e << 1) : ((e << 1) | 1);
    if (edgeKm[e] < dist[s]) {
      dist[s] = edgeKm[e]; staatKm[s] = edgeKm[e]; push(s, edgeKm[e]);
    }
  }
  let beste = -1, besteD = Infinity;
  while (hK.length) {
    const [s, d] = pop();
    if (d > dist[s]) continue;
    const k = eindKnoop(s);
    if (k === doel) { if (d < besteD) { besteD = d; beste = s; } break; }
    const eIn = s >> 1;
    for (let i = adjStart[k]; i < adjStart[k + 1]; i++) {
      const e = adjEdge[i];
      if (edgeModus[e] === 2) continue;         // spoor-only
      const s2 = (edgeA[e] === k) ? (e << 1) : ((e << 1) | 1);
      const nd = d + edgeKm[e] + bochtStrafKm(eIn, e, k);
      if (nd < dist[s2]) {
        dist[s2] = nd;
        staatKm[s2] = staatKm[s] + edgeKm[e];
        prevStaat[s2] = s;
        push(s2, nd);
      }
    }
  }
  return { dist, prevStaat, staatKm, beste, besteD, eindKnoop };
}
const { dist, prevStaat, staatKm, beste, eindKnoop } =
  dijkstra(snapVan.knoop, snapNaar.knoop);

if (beste < 0) {
  const rv = find(snapVan.knoop), rn = find(snapNaar.knoop);
  console.log(`GEEN PAD: van-component ${Math.round(compKm.get(rv) || 0).toLocaleString("nl-NL")} km ` +
    `(root ${rv}) · naar-component ${Math.round(compKm.get(rn) || 0).toLocaleString("nl-NL")} km ` +
    `(root ${rn}) — ${rv === rn ? "ZELFDE component (onverwacht!)" : "verschillende componenten"}`);
  process.exit(2);
}

// --- pad terugbouwen + lijngeometrie in de looprichting ---
// De toestand draagt de richting al: even = van A naar B, oneven = van B naar A.
const pad = [];                                 // { e, van } in volgorde bron→doel
for (let s = beste; s >= 0; s = prevStaat[s]) {
  const e = s >> 1;
  pad.push({ e, van: (s & 1) === 0 ? edgeA[e] : edgeB[e] });
}
pad.reverse();

const coords = [];
for (const stap of pad) {
  const e = stap.e, start = geomStart[e], nV = geomN[e];
  const voorwaarts = edgeA[e] === stap.van;     // eerste vertex = knoop A
  for (let j = coords.length ? 1 : 0; j < nV; j++) {   // junctiepunt niet dubbel
    const i = start + (voorwaarts ? j : nV - 1 - j);
    const x = posities[i * 3], y = posities[i * 3 + 1], z = posities[i * 3 + 2];
    const lon = Math.atan2(-z, x) / rad;
    const lat = Math.asin(Math.max(-1, Math.min(1, y / STRAAL))) / rad;
    coords.push([+lon.toFixed(6), +lat.toFixed(6)]);
  }
}

// --- spike-schoonmaak op de GETEKENDE lijn -----------------------------------
// ⚠️ DIT IS EEN ANDER PROBLEEM DAN DE BOCHTSTRAF, en het onderscheid is precies
// waar de grens ligt tussen "routeren" en "tekenen". De bochtstraf kiest tussen
// edges; een knik BINNEN één OSM-way is geen keuze — daar valt niets te
// routeren, die zigzag staat gewoon zo in de bron.
//
// Zichtbaar geworden door de fijnere simplify (2026-07-28): op 100 m tolerantie
// veegde Douglas-Peucker elke uitstulping onder 100 m weg, inclusief OSM's eigen
// fouten; op 10 m blijven ze staan. Gemeten na de herbake: knikken van ~95° met
// een boogstraal van 46 m, midden in een way.
//
// De schoonmaak haalt een punt weg als het ALLEBEI waar is:
//   * de knik is groter dan 60° — geen enkele vrachtboog draait zo scherp, en
//   * het punt steekt minder dan 25 m uit de lijn tussen zijn buren.
// Die twee samen selecteren een spike en laten een echte boog met rust: in een
// dichte boog is de knik per punt maar een paar graden, dus de eerste eis vangt
// hem niet. Wat we verplaatsen is hooguit 25 m, en dat is minder dan de
// tolerantie waarmee de lijn sowieso getekend is.
{
  const offset = (a, b, c) => {
    const sx = Math.cos((a[1] + c[1]) / 2 * rad) * 111.32;
    const ax = a[0] * sx, ay = a[1] * 110.57;
    const bx = b[0] * sx, by = b[1] * 110.57;
    const cx = c[0] * sx, cy = c[1] * 110.57;
    const vx = cx - ax, vy = cy - ay;
    const L2 = vx * vx + vy * vy;
    if (L2 < 1e-12) return Math.hypot(bx - ax, by - ay) * 1000;
    const t = Math.max(0, Math.min(1, ((bx - ax) * vx + (by - ay) * vy) / L2));
    return Math.hypot(bx - ax - t * vx, by - ay - t * vy) * 1000;
  };
  const hoekVan = (a, b, c) => {
    const p = (u, v) => Math.atan2((v[0] - u[0]) * Math.cos((u[1] + v[1]) / 2 * rad),
                                   v[1] - u[1]) / rad;
    return Math.abs(((p(b, c) - p(a, b) + 180) % 360 + 360) % 360 - 180);
  };
  let weg = 0;
  for (let ronde = 0; ronde < 3; ronde++) {
    let veranderd = false;
    for (let i = coords.length - 2; i >= 1; i--) {
      const a = coords[i - 1], b = coords[i], c = coords[i + 1];
      if (hoekVan(a, b, c) > 60 && offset(a, b, c) < 25) {
        coords.splice(i, 1); weg++; veranderd = true;
      }
    }
    if (!veranderd) break;
  }
  if (weg) console.log(`spike-schoonmaak: ${weg} punten weg (knik >60 graden ` +
    `terwijl het punt <25 m uit de lijn steekt — OSM-zigzag, geen bocht)`);
}

// --- wat er NA de straf nog aan scherpe bochten overblijft -------------------
// ⚠️ Dit hoort in de uitvoer en niet in een logbestand: een keerpunt dat de
// straf overleeft is óf een echte kopmaak-beweging (het spoor loopt dood, de
// trein moet terug) óf een rest-artefact — en dat verschil kan alleen een mens
// beoordelen. Wegmoffelen zou de indruk wekken dat het probleem weg is; het
// getal erbij (boogstraal) maakt het beoordeelbaar: onder ~150 m bestaat er
// geen vrachtboog, dus dan is het een omkering en geen bocht.
{
  const bochten = [];
  for (let i = 1; i < coords.length - 1; i++) {
    const a = coords[i - 1], b = coords[i], c = coords[i + 1];
    const seg = (p, q) => {
      const dx = (q[0] - p[0]) * Math.cos((p[1] + q[1]) / 2 * rad) * 111.32;
      const dy = (q[1] - p[1]) * 110.57;
      return [Math.hypot(dx, dy), Math.atan2(dx, dy) / rad];
    };
    const [d1, p1] = seg(a, b), [d2, p2] = seg(b, c);
    if (d1 < 0.005 || d2 < 0.005) continue;
    const hoek = Math.abs(((p2 - p1 + 180) % 360 + 360) % 360 - 180);
    if (hoek < 60) continue;
    const s = Math.sin(hoek / 2 * rad);
    bochten.push({ hoek, straalM: ((d1 + d2) / 2 * 1000) / (2 * s), b });
  }
  bochten.sort((x, y) => y.hoek - x.hoek);
  console.log(`bochten >= 60 graden na de straf (keerstraf ${KEERSTRAF_KM} km): ` +
    `${bochten.length}`);
  for (const q of bochten.slice(0, 6)) {
    console.log(`  ${q.hoek.toFixed(1).padStart(6)} graden · boogstraal ` +
      `~${Math.round(q.straalM).toString().padStart(6)} m · ` +
      `${q.b[1].toFixed(5)},${q.b[0].toFixed(5)} · ` +
      (q.hoek >= 150 ? "OMKERING — alleen echt als hier kopgemaakt wordt"
                     : "scherpe bocht"));
  }
}

// --- sanity: route-km tegen de grootcirkel tussen de twee ruwe punten ---
const routeKm = staatKm[beste];   // ECHTE km — de bochtstraf zit niet in de lengte
const dLat = (naar.lat - van.lat) * rad, dLon = (naar.lon - van.lon) * rad;
const h = Math.sin(dLat / 2) ** 2 +
  Math.cos(van.lat * rad) * Math.cos(naar.lat * rad) * Math.sin(dLon / 2) ** 2;
const grootcirkelKm = 2 * AARDE_KM * Math.asin(Math.sqrt(h));
const sanity = routeKm >= grootcirkelKm
  ? "OK (route >= grootcirkel)"
  : "FOUT — route korter dan de grootcirkel, bug in dit script";

console.log(`route: ${routeKm.toFixed(1)} km over ${pad.length} edges · ` +
  `grootcirkel ${grootcirkelKm.toFixed(1)} km · verhouding ${(routeKm / grootcirkelKm).toFixed(2)} · sanity ${sanity}`);

// --- GeoJSON wegschrijven ---
mkdirSync(UITMAP, { recursive: true });
const geoPad = join(UITMAP, `spoorroute-${naam}.geojson`);
writeFileSync(geoPad, JSON.stringify({
  type: "FeatureCollection",
  features: [{
    type: "Feature",
    properties: {
      naam, routeKm: +routeKm.toFixed(1), edges: pad.length,
      grootcirkelKm: +grootcirkelKm.toFixed(1),
      van, naar,
      snapVanKm: +snapVan.km.toFixed(2), snapNaarKm: +snapNaar.km.toFixed(2),
      vanKnoop: snapVan.knoop, naarKnoop: snapNaar.knoop,
    },
    geometry: { type: "LineString", coordinates: coords },
  }],
}));
console.log(`geojson: ${geoPad} (${coords.length} punten)`);
