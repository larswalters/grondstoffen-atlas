// lane_widths.js — bake-stap ná bake_searoutes.py: berekent per corridorpunt
// hoeveel zijwaartse ruimte (km) er tot land is en schrijft dat als sparse
// `w: {puntindex: km}` terug in data/_searoutes.js.
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

// VERDICHTEN vóór het meten. bake_searoutes.py vereenvoudigt agressief (trapjes
// uit de land-omleiding weg — dat is puur een VORM-kwestie), maar de baan-klem
// leest de vrije ruimte PER PUNT: in de Seto-binnenzee waren juist die punten de
// rem op de waaier, en na het opruimen bolden de banen weer over Japan
// (8 -> 195 landtreffers). Daarom zetten we hier punten terug — maar alléén waar
// het water nauw is, en exact op de bestaande lijn (het midden van een segment),
// zodat er GEEN nieuwe knik bijkomt. Vorm blijft dus glad, klem krijgt resolutie.
function densifyNarrow(pts, depth = 0) {
  if (depth > 6) return pts;
  const out = [pts[0]];
  let added = false;
  for (let i = 1; i < pts.length; i++) {
    const a = pts[i - 1], b = pts[i];
    const len = segKm(a, b);
    const mid = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
    if (len > 20 && clearanceKm([a, mid, b], 1) < CAP_KM) {
      out.push([+mid[0].toFixed(3), +mid[1].toFixed(3)]);
      added = true;
    }
    out.push(b);
  }
  return added ? densifyNarrow(out, depth + 1) : out;
}

function segKm(a, b) {
  const cosLat = Math.cos((a[0] + b[0]) / 2 * Math.PI / 180);
  const dLat = b[0] - a[0], dLon = (b[1] - a[1]) * cosLat;
  return Math.sqrt(dLat * dLat + dLon * dLon) * 111.2;
}

const src = fs.readFileSync(SR_PATH, "utf8").split("\n");
const LINE_RE = /^(\s*)"([^"]+)": \{ pts: (\[.*?\]), (?:w: \{[^}]*\}, )?passages: (\[[^\]]*\]) \},(.*)$/;

let corridors = 0, constrained = 0, points = 0, densified = 0;
const out = src.map((line) => {
  const m = line.match(LINE_RE);
  if (!m) return line;
  corridors++;
  const pts = densifyNarrow(JSON.parse(m[3]));
  // per-punt vrije ruimte
  const clr = pts.map((_, i) => clearanceKm(pts, i));
  // running-min: een pinch pint z'n buren binnen ~PIN_KM langs de route, zodat
  // de CatmullRom-spline niet tússen een smal en een ruim punt over land bult.
  const PIN_KM = 40;
  const acc = [0];
  for (let i = 1; i < pts.length; i++) acc.push(acc[i - 1] + segKm(pts[i - 1], pts[i]));
  const pinned = clr.map((v, i) => {
    let mn = v;
    for (let j = i - 1; j >= 0 && acc[i] - acc[j] <= PIN_KM; j--) if (clr[j] < mn) mn = clr[j];
    for (let j = i + 1; j < pts.length && acc[j] - acc[i] <= PIN_KM; j++) if (clr[j] < mn) mn = clr[j];
    return mn;
  });
  const w = {};
  for (let i = 0; i < pts.length; i++) {
    if (pinned[i] < CAP_KM) { w[i] = pinned[i]; points++; }
  }
  const hasW = Object.keys(w).length > 0;
  if (hasW) constrained++;
  densified += pts.length - JSON.parse(m[3]).length;
  const wPart = hasW ? `w: ${JSON.stringify(w)}, ` : "";
  // de verdichte polyline gaat MEE terug: de w-indices verwijzen ernaar
  return `${m[1]}"${m[2]}": { pts: ${JSON.stringify(pts)}, ${wPart}passages: ${m[4]} },${m[5]}`;
});

// pipeline-notitie in de header, één keer
const HDR = "// _searoutes.js — GEGENEREERD";
const NOTE = "// Baanbreedtes (w) toegevoegd door tools/lane_widths.js — draai die opnieuw ná elke bake.";
const hdrIdx = out.findIndex((l) => l.startsWith(HDR));
if (hdrIdx >= 0 && !out.some((l) => l.startsWith("// Baanbreedtes"))) {
  out.splice(hdrIdx + 1, 0, NOTE);
}

fs.writeFileSync(SR_PATH, out.join("\n"));
console.log(`${corridors} corridors, ${constrained} met begrensde punten (${points} punten < ${CAP_KM} km vrij, ${densified} verdicht in nauw water).`);
