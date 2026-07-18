// lane_widths.js — bake-stap ná bake_searoutes.py: berekent per corridorpunt
// hoeveel zijwaartse ruimte (km) er tot land is en schrijft dat als sparse
// `wp: {monsterindex: km}` terug in data/_searoutes.js — een APART profiel op
// booglengte, los van de getekende punten (zie de ontkoppeling hieronder).
//
// Waarom: flows.js waaiert elke stroom uit over 7 parallelle vaarbanen
// (config.lanes: spacing 0.012 × ±3 = tot ~95 km uit het midden). De oude A*
// maskeerde dat met ~130 km geforceerd water rond knelpunten; MARNET scheert
// écht langs de kust — bij de Tsugaru-straat (~20 km) en de Seto-binnenzee
// gingen de buitenbanen dwars over Japan. makeRouteCurve klemt de baan-offset
// nu af op deze gebakken breedte; open oceaan (geen w) blijft ongewijzigd.
//
// Idempotent: bestaande w-velden worden vervangen. Pipeline:
//   bake_searoutes.py  ->  node tools/lane_widths.js  ->  node tools/check_corridors.js
//
// Gebruik:  node tools/lane_widths.js

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.join(__dirname, "..");
const SR_PATH = path.join(ROOT, "data/_searoutes.js");

const ctx = { console };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(ROOT, "geo-data.js"), "utf8") +
  ";globalThis.__LP=LAND_POLYS;", ctx);
const LAND = ctx.__LP;

// --- zelfde land-test als check_corridors.js (Natural Earth 50m, meren = gaten)
function inRing(lon, lat, ring) {
  let inside = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const xi = ring[i][0], yi = ring[i][1];
    const xj = ring[j][0], yj = ring[j][1];
    if (((yi > lat) !== (yj > lat)) &&
        (lon < (xj - xi) * (lat - yi) / (yj - yi) + xi)) inside = !inside;
  }
  return inside;
}
const polys = LAND.map((p) => {
  const outer = p[0];
  let minX = 999, maxX = -999, minY = 999, maxY = -999;
  outer.forEach(([x, y]) => {
    if (x < minX) minX = x; if (x > maxX) maxX = x;
    if (y < minY) minY = y; if (y > maxY) maxY = y;
  });
  return { rings: p, minX, maxX, minY, maxY };
});
function isLand(lat, lon) {
  lon = ((lon + 180) % 360 + 360) % 360 - 180;
  for (const p of polys) {
    if (lon < p.minX || lon > p.maxX || lat < p.minY || lat > p.maxY) continue;
    if (inRing(lon, lat, p.rings[0])) {
      for (let r = 1; r < p.rings.length; r++) {
        if (inRing(lon, lat, p.rings[r])) return false;
      }
      return true;
    }
  }
  return false;
}

// maximale baan-offset die flows.js ooit vraagt: 3 × 0.012 op bolstraal 2.4
// = 0.036/2.4 × 6371 ≈ 96 km. Ruimer dan dat hoeven we niet te meten.
const CAP_KM = 96;
const STEP_KM = 2;  // meetstap; clearance = laatste stap die nog water was
const DIRS = 16;    // stralen rondom (elke 22,5°) — vangt eilandjes uit élke hoek
const SAMPLE_KM = 20;  // rasterafstand van het klem-profiel (los van de geometrie)
const PIN_KM = 40;     // een pinch pint z'n buren binnen deze afstand

// vrije ruimte = afstand tot het dichtstbijzijnde land in WELKE richting dan ook.
// Loodrecht meten miste eilanden die schuin voor de baan liggen (Seto-binnenzee);
// omnidirectioneel is conservatief en robuust: in een zeestraat = halve breedte,
// op open zee bij een eilandengroep = de afstand tot het eiland.
function clearanceKm(pts, i) {
  const p = pts[i];
  const cosLat = Math.max(0.05, Math.cos(p[0] * Math.PI / 180));
  let best = CAP_KM;
  for (let a = 0; a < DIRS; a++) {
    const ang = (a / DIRS) * 2 * Math.PI;
    const dLat = Math.cos(ang), dLon = Math.sin(ang) / cosLat;
    for (let d = STEP_KM; d <= best; d += STEP_KM) {
      const lat = p[0] + dLat * (d / 111.2);
      const lon = p[1] + dLon * (d / 111.2);
      if (isLand(lat, lon)) { if (d - STEP_KM < best) best = d - STEP_KM; break; }
    }
  }
  return best;
}

// Grote-cirkelafstand — zelfde formule als util.js gebruikt voor totalAngle,
// zodat de monster-index aan beide kanten op hetzelfde raster valt.
function segKm(a, b) {
  const toR = (x) => x * Math.PI / 180;
  const dLa = toR(b[0] - a[0]), dLo = toR(b[1] - a[1]);
  const h = Math.sin(dLa / 2) ** 2 +
    Math.cos(toR(a[0])) * Math.cos(toR(b[0])) * Math.sin(dLo / 2) ** 2;
  return 2 * 6371 * Math.asin(Math.min(1, Math.sqrt(h)));
}

// Punt op booglengte-fractie t langs de polyline (lineair binnen een segment).
function pointAtFraction(pts, acc, t) {
  const total = acc[acc.length - 1];
  const d = t * total;
  let lo = 0, hi = acc.length - 1;
  while (lo < hi - 1) {
    const mid = (lo + hi) >> 1;
    if (acc[mid] <= d) lo = mid; else hi = mid;
  }
  const span = acc[hi] - acc[lo] || 1;
  const f = (d - acc[lo]) / span;
  return [pts[lo][0] + (pts[hi][0] - pts[lo][0]) * f,
          pts[lo][1] + (pts[hi][1] - pts[lo][1]) * f];
}

const src = fs.readFileSync(SR_PATH, "utf8").split("\n");
const LINE_RE = /^(\s*)"([^"]+)": \{ pts: (\[.*?\]), (?:wp?: \{[^}]*\}, )?passages: (\[[^\]]*\]) \},(.*)$/;

let corridors = 0, constrained = 0, points = 0, samples = 0;
const out = src.map((line) => {
  const m = line.match(LINE_RE);
  if (!m) return line;
  corridors++;
  const pts = JSON.parse(m[3]);   // geometrie ONGEMOEID — dit is puur meten
  const acc = [0];
  for (let i = 1; i < pts.length; i++) acc.push(acc[i - 1] + segKm(pts[i - 1], pts[i]));
  const totalKm = acc[acc.length - 1];

  // UNIFORM langs de booglengte bemonsteren, elke SAMPLE_KM. Los van waar de
  // getekende punten toevallig liggen: de klem heeft z'n eigen raster.
  const K = Math.max(2, Math.ceil(totalKm / SAMPLE_KM) + 1);
  const probe = [];
  for (let k = 0; k < K; k++) probe.push(pointAtFraction(pts, acc, k / (K - 1)));
  const clr = probe.map((_, i) => clearanceKm(probe, i));

  // running-min: een pinch pint z'n buren binnen ~PIN_KM, zodat de spline niet
  // tússen een smal en een ruim monster over land bult.
  const pinSteps = Math.max(1, Math.round(PIN_KM / SAMPLE_KM));
  const pinned = clr.map((v, i) => {
    let mn = v;
    for (let j = Math.max(0, i - pinSteps); j <= Math.min(K - 1, i + pinSteps); j++) {
      if (clr[j] < mn) mn = clr[j];
    }
    return mn;
  });

  const wp = {};
  for (let i = 0; i < K; i++) if (pinned[i] < CAP_KM) { wp[i] = pinned[i]; points++; }
  const hasW = Object.keys(wp).length > 0;
  if (hasW) constrained++;
  samples += K;
  const wPart = hasW ? `wp: ${JSON.stringify(wp)}, ` : "";
  // pts blijft exact zoals gebakken; wp is een APART profiel op booglengte
  return `${m[1]}"${m[2]}": { pts: ${m[3]}, ${wPart}passages: ${m[4]} },${m[5]}`;
});

// pipeline-notitie in de header, één keer
const HDR = "// _searoutes.js — GEGENEREERD";
const NOTE = "// Baanbreedtes (w) toegevoegd door tools/lane_widths.js — draai die opnieuw ná elke bake.";
const hdrIdx = out.findIndex((l) => l.startsWith(HDR));
if (hdrIdx >= 0 && !out.some((l) => l.startsWith("// Baanbreedtes"))) {
  out.splice(hdrIdx + 1, 0, NOTE);
}

fs.writeFileSync(SR_PATH, out.join("\n"));
console.log(`${corridors} corridors, ${constrained} met een klem-profiel — ${samples} monsters op ${SAMPLE_KM} km, waarvan ${points} < ${CAP_KM} km vrij.`);
