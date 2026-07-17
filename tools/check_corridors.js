// check_corridors.js — kwaliteitscontrole op de gebakken corridors in
// data/_searoutes.js: (1) snijdt een segment land? (2) zitten er hairpins /
// scherpe bochten in? Gebruikt dezelfde landpolygonen als de kaart zelf
// (geo-data.js, Natural Earth 50m, meren als gaten).
//
// Gebruik:  node tools/check_corridors.js [drempel-bocht-graden=120]

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.join(__dirname, "..");
const ctx = { console };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(ROOT, "geo-data.js"), "utf8") +
  ";globalThis.__LP=LAND_POLYS;", ctx);
vm.runInContext(fs.readFileSync(path.join(ROOT, "data/_searoutes.js"), "utf8") +
  ";globalThis.__SR=SEAROUTES;", ctx);
const LAND = ctx.__LP;
const SEAROUTES = ctx.__SR;

// ray-casting point-in-ring
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
// bounding boxes vooraf (anders is dit O(alles))
const polys = LAND.map((p) => {
  const outer = p[0];
  let minX = 999, maxX = -999, minY = 999, maxY = -999;
  outer.forEach(([x, y]) => {
    if (x < minX) minX = x; if (x > maxX) maxX = x;
    if (y < minY) minY = y; if (y > maxY) maxY = y;
  });
  return { rings: p, minX, maxX, minY, maxY };
});
// kanalen zijn land in Natural Earth maar horen bij de route
const CANALS = [[9.0, -79.6], [30.5, 32.3]]; // Panama, Suez
function nearCanal(lat, lon) {
  return CANALS.some(([cla, clo]) => Math.abs(lat - cla) < 1.2 && Math.abs(lon - clo) < 1.2);
}
function isLand(lat, lon) {
  lon = ((lon + 180) % 360 + 360) % 360 - 180;
  if (nearCanal(lat, lon)) return false;
  for (const p of polys) {
    if (lon < p.minX || lon > p.maxX || lat < p.minY || lat > p.maxY) continue;
    if (inRing(lon, lat, p.rings[0])) {
      for (let r = 1; r < p.rings.length; r++) {
        if (inRing(lon, lat, p.rings[r])) return false; // in een meer-gat
      }
      return true;
    }
  }
  return false;
}

const R = 6371;
function gcKm(a, b) {
  const la1 = a[0] * Math.PI / 180, la2 = b[0] * Math.PI / 180;
  const dla = (b[0] - a[0]) * Math.PI / 180, dlo = (b[1] - a[1]) * Math.PI / 180;
  const h = Math.sin(dla / 2) ** 2 + Math.cos(la1) * Math.cos(la2) * Math.sin(dlo / 2) ** 2;
  return 2 * R * Math.asin(Math.min(1, Math.sqrt(h)));
}
function bearing(a, b) {
  const la1 = a[0] * Math.PI / 180, la2 = b[0] * Math.PI / 180;
  const dlo = (b[1] - a[1]) * Math.PI / 180;
  return Math.atan2(Math.sin(dlo) * Math.cos(la2),
    Math.cos(la1) * Math.sin(la2) - Math.sin(la1) * Math.cos(la2) * Math.cos(dlo)) * 180 / Math.PI;
}

const TURN_LIMIT = +(process.argv[2] || 120);
const STEP_KM = 12;      // bemonsteringsafstand op een segment
const PORT_SKIP_KM = 25; // begin/eind raken per definitie de kust (haven)

let anyIssue = false;
for (const [key, e] of Object.entries(SEAROUTES)) {
  const pts = e.pts;
  const name = (fs.readFileSync(path.join(ROOT, "data/_searoutes.js"), "utf8")
    .split("\n").find((l) => l.includes(key)) || "").match(/\/\/ (.*)$/);
  const label = name ? name[1] : key;

  // 1) landkruisingen — segmentsgewijs lineair in lat/lon bemonsterd (zo tekent
  //    de atlas het ook: de curve interpoleert de punten, niet de grote cirkel)
  const hits = [];
  let fromStart = 0;
  const total = pts.reduce((s, p, i) => i ? s + gcKm(pts[i - 1], p) : 0, 0);
  for (let i = 0; i < pts.length - 1; i++) {
    const a = pts[i], b = pts[i + 1];
    const segKm = gcKm(a, b);
    const n = Math.max(1, Math.ceil(segKm / STEP_KM));
    for (let k = 1; k < n; k++) {
      const t = k / n;
      const dist = fromStart + segKm * t;
      if (dist < PORT_SKIP_KM || dist > total - PORT_SKIP_KM) continue;
      const lat = a[0] + (b[0] - a[0]) * t;
      let dl = b[1] - a[1];
      if (dl > 180) dl -= 360; if (dl < -180) dl += 360;
      const lon = a[1] + dl * t;
      if (isLand(lat, lon)) {
        hits.push({ seg: i, lat: +lat.toFixed(2), lon: +lon.toFixed(2), segKm: Math.round(segKm) });
        break; // één hit per segment is genoeg
      }
    }
    fromStart += segKm;
  }

  // 2) scherpe bochten (hairpins)
  const turns = [];
  for (let i = 1; i < pts.length - 1; i++) {
    let d = Math.abs(bearing(pts[i - 1], pts[i]) - bearing(pts[i], pts[i + 1]));
    if (d > 180) d = 360 - d;
    if (d > TURN_LIMIT) turns.push({ i, hoek: Math.round(d), lat: pts[i][0], lon: pts[i][1] });
  }

  if (hits.length || turns.length) {
    anyIssue = true;
    console.log(`\n${label}`);
    hits.forEach((h) => console.log(`  LAND  segment ${h.seg} (${h.segKm} km) raakt land bij ${h.lat}, ${h.lon}`));
    turns.forEach((t) => console.log(`  BOCHT ${t.hoek}° bij ${t.lat}, ${t.lon} (punt ${t.i})`));
  }
}
if (!anyIssue) console.log("alle corridors schoon (geen landkruisingen, geen bochten > " + TURN_LIMIT + "°)");
