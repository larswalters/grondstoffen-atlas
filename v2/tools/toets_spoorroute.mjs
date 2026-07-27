// toets_spoorroute.mjs — punt-naar-punt over het SPOORNET: snap, Dijkstra, GeoJSON.
//
// Waarom dit tool bestaat: het landnet (v2/data/landnet.bin) draagt spoor én weg
// door elkaar, en er was nog geen los gereedschap om een concreet spoor-been
// (fabriek → fabriek) na te rekenen én de gevolgde lijn op de kaart te leggen.
// Dit tool doet precies dat, headless, met twee projectlessen ingebakken:
//
//   1. SNAP OP HET HOOFDNET (spoor-component >= 1.000 km), niet op de
//      dichtstbijzijnde knoop hoe dan ook — anders snap je op een los
//      rangeersporentje en geeft álles "geen pad" (de LAR-518-les; zelfde
//      drempel als koppelNetten en toets_spoor_aansluiting.mjs). De absolute
//      dichtste spoorknoop wordt wél gerapporteerd, zodat zichtbaar is wanneer
//      de hoofdnet-eis een dichtere stub overslaat.
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
// Uitvoer: kernregels op de console + de gevolgde lijn als GeoJSON in
//   v2/build-cache/ais/graaf/spoorroute-<naam>.geojson

import { writeFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { laadLandnetHeadless } from "./laad_headless.mjs";

const V2 = dirname(dirname(fileURLToPath(import.meta.url)));
const UITMAP = join(V2, "build-cache", "ais", "graaf");
const STRAAL = 2.4;          // bolstraal van `posities` (afspraak z = -sin lon)
const HOOFD_KM = 1000;       // hoofdnet-drempel, zie toets_spoor_aansluiting.mjs
const AARDE_KM = 6371;

// --- CLI ---
const args = {};
for (const a of process.argv.slice(2)) {
  const m = a.match(/^--([^=]+)=(.*)$/);
  if (m) args[m[1]] = m[2];
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
  };
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

// --- Dijkstra over spoor-edges op edgeKm ---
function dijkstra(bron, doel) {
  const dist = new Float64Array(n).fill(Infinity);
  const prevEdge = new Int32Array(n).fill(-1);
  const prevKnoop = new Int32Array(n).fill(-1);
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
  dist[bron] = 0; push(bron, 0);
  while (hK.length) {
    const [k, d] = pop();
    if (d > dist[k]) continue;
    if (k === doel) break;
    for (let i = adjStart[k]; i < adjStart[k + 1]; i++) {
      const e = adjEdge[i];
      if (edgeModus[e] === 2) continue;         // spoor-only
      const buur = adjKnoop[i], nd = d + edgeKm[e];
      if (nd < dist[buur]) { dist[buur] = nd; prevEdge[buur] = e; prevKnoop[buur] = k; push(buur, nd); }
    }
  }
  return { dist, prevEdge, prevKnoop };
}
const { dist, prevEdge, prevKnoop } = dijkstra(snapVan.knoop, snapNaar.knoop);

if (!Number.isFinite(dist[snapNaar.knoop])) {
  const rv = find(snapVan.knoop), rn = find(snapNaar.knoop);
  console.log(`GEEN PAD: van-component ${Math.round(compKm.get(rv) || 0).toLocaleString("nl-NL")} km ` +
    `(root ${rv}) · naar-component ${Math.round(compKm.get(rn) || 0).toLocaleString("nl-NL")} km ` +
    `(root ${rn}) — ${rv === rn ? "ZELFDE component (onverwacht!)" : "verschillende componenten"}`);
  process.exit(2);
}

// --- pad terugbouwen + lijngeometrie in de looprichting ---
const pad = [];                                 // { e, van } in volgorde bron→doel
for (let k = snapNaar.knoop; k !== snapVan.knoop; k = prevKnoop[k])
  pad.push({ e: prevEdge[k], van: prevKnoop[k] });
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

// --- sanity: route-km tegen de grootcirkel tussen de twee ruwe punten ---
const routeKm = dist[snapNaar.knoop];
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
