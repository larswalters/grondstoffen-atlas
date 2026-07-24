// toets_spoor_aansluiting.mjs — de brede spoor-last-mile-detector.
//
// Lars' hypothese: industrieel siding-spoor naar smelters/mijnen/terminals is
// vaak NIET of LOS gemapt — precies het spoor dat de keten nodig heeft voor de
// last mile. Tongling bewees het (siding op ~2 km, afgeknipt van het hoofdnet).
// Dit toetst het BREED: elke industriële node uit data/*.js + de aansluitingen,
// geclassificeerd tegen het landnet met de projecteigen drempels.
//
//   VERBONDEN   hoofdnet-lijn ≤ 3 km               → last mile klopt
//   AFGEKNIPT   siding ≤ 3 km, maar hoofdnet verder → siding gemapt maar los (Tongling)
//   LANGE SPUR  hoofdnet 3–60 km, geen lokale siding → hoofdlijn-snap over rechte spur
//   GEEN SPOOR  hoofdnet > 60 km                    → geen bruikbaar spoor
//
// "hoofdnet" = component ≥ 1.000 km (koppelNetten's spoor-hoofdlijn-drempel).
// Draaien:  node v2/tools/toets_spoor_aansluiting.mjs

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { laadLandnetHeadless, laadAansluitingen } from "./laad_headless.mjs";

const V2 = dirname(dirname(fileURLToPath(import.meta.url)));
const DATA = join(V2, "..", "data");   // de grondstof-datafiles staan in de repo-root data/

// --- nodes uit alle data/*.js trekken via de REGISTER-shim ---
const RESOURCES = [];
globalThis.REGISTER = (r) => RESOURCES.push(r);
const files = ["copper", "coal", "cobalt", "rare-earths", "graphite", "lithium",
  "nickel", "oil", "silver", "uranium", "gas", "goud", "diamond", "pgm"];
for (const f of files) {
  const src = readFileSync(join(DATA, `${f}.js`), "utf-8");
  new Function("REGISTER", src)(globalThis.REGISTER);
}
const INDUSTRIE = new Set(["mine", "refinery", "port", "market", "recycler", "hub", "smelter"]);
const punten = [];
for (const r of RESOURCES) for (const n of r.nodes || []) {
  if (INDUSTRIE.has(n.type) && Number.isFinite(n.lat) && Number.isFinite(n.lon))
    punten.push({ bron: r.id, id: n.id, naam: n.name, type: n.type, lat: n.lat, lon: n.lon });
}
// de aansluitingen (precieze kade/laadspoor-coördinaten van de pilots)
for (const a of (laadAansluitingen().aansluitingen || [])) {
  const ll = a.modaliteiten ? Object.values(a.modaliteiten)[0] : (a.ll || null);
  const lat = a.lat ?? (ll && ll[1]), lon = a.lon ?? (ll && ll[0]);
  if (Number.isFinite(lat) && Number.isFinite(lon))
    punten.push({ bron: "aansluiting", id: a.id, naam: a.naam, type: "aansluiting", lat, lon });
}

// --- landnet + component-km ---
const L = laadLandnetHeadless();
const { edgeA, edgeB, edgeKm, geomN, geomStart, posities, stats } = L;
const n = stats.knopen, m = stats.edges;
const par = new Int32Array(n).map((_, i) => i);
const find = (x) => { while (par[x] !== x) { par[x] = par[par[x]]; x = par[x]; } return x; };
for (let e = 0; e < m; e++) { const a = find(edgeA[e]), b = find(edgeB[e]); if (a !== b) par[a] = b; }
const compKm = new Map();
for (let e = 0; e < m; e++) { const r = find(edgeA[e]); compKm.set(r, (compKm.get(r) || 0) + edgeKm[e]); }
const HOOFD_KM = 1000;

// vertex-arrays op de eenheidsbol + hoofdnet-vlag per vertex
let nV = 0; for (let e = 0; e < m; e++) nV += geomN[e];
const vx = new Float64Array(nV), vy = new Float64Array(nV), vz = new Float64Array(nV);
const vHoofd = new Uint8Array(nV);
{
  const R = 2.4; let pi = 0;
  for (let e = 0; e < m; e++) {
    const hoofd = (compKm.get(find(edgeA[e])) || 0) >= HOOFD_KM ? 1 : 0;
    for (let k = 0; k < geomN[e]; k++) {
      const i = geomStart[e] + k;
      vx[pi] = posities[i * 3] / R; vy[pi] = posities[i * 3 + 1] / R; vz[pi] = posities[i * 3 + 2] / R;
      vHoofd[pi] = hoofd; pi++;
    }
  }
}
const to3d = (lo, la) => { const r = Math.PI / 180, c = Math.cos(la * r);
  return [c * Math.cos(lo * r), Math.sin(la * r), -c * Math.sin(lo * r)]; };
const kmVan = (dot) => 6371 * Math.acos(Math.max(-1, Math.min(1, dot)));

// per punt: dichtste hoofdnet-lijn en dichtste stub-lijn (dot = cos hoek, monotoon)
for (const p of punten) {
  const [sx, sy, sz] = to3d(p.lon, p.lat);
  let bestHoofd = -2, bestStub = -2;
  for (let i = 0; i < nV; i++) {
    const d = sx * vx[i] + sy * vy[i] + sz * vz[i];
    if (vHoofd[i]) { if (d > bestHoofd) bestHoofd = d; }
    else if (d > bestStub) bestStub = d;
  }
  p.dHoofd = kmVan(bestHoofd);
  p.dStub = kmVan(bestStub);
  if (p.dHoofd <= 3) p.klasse = "VERBONDEN";
  else if (p.dStub <= 3 && p.dHoofd > p.dStub + 2) p.klasse = "AFGEKNIPT";
  else if (p.dHoofd <= 60) p.klasse = "LANGE SPUR";
  else p.klasse = "GEEN SPOOR";
}

// --- rapport ---
const orde = { "AFGEKNIPT": 0, "LANGE SPUR": 1, "GEEN SPOOR": 2, "VERBONDEN": 3 };
punten.sort((a, b) => orde[a.klasse] - orde[b.klasse] || a.dHoofd - b.dHoofd);
const telling = {};
for (const p of punten) telling[p.klasse] = (telling[p.klasse] || 0) + 1;

console.log(`\n=== brede spoor-last-mile-detector · ${punten.length} industriële punten ===\n`);
console.log("verdeling:", Object.entries(telling).map(([k, v]) => `${k} ${v}`).join(" · "), "\n");
console.log("De aandachtspunten (siding gemapt-maar-los of ontbrekende last-mile):\n");
for (const p of punten) {
  if (p.klasse === "VERBONDEN") continue;
  const stub = p.dStub < 1e4 ? `stub ${p.dStub.toFixed(1)}km` : "geen stub";
  console.log(`  ${p.klasse.padEnd(10)} hoofdnet ${p.dHoofd.toFixed(1).padStart(6)}km · ${stub.padStart(12)} · ` +
    `${p.bron}/${p.type} · ${p.naam}`);
}
