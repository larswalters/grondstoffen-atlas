// extract_corridors.js — verzamelt de unieke zee-corridors (haven→haven) uit de
// grondstof-data, PRECIES zoals flows.js ze straks routeert: stops = from + via + to,
// en elk opeenvolgend paar zee-punten is een corridor.
//
// MARNET-BESLIST-PRINCIPE (besluit Lars 2026-07-17, design/zeeroutes.md §8):
// wp-*-punten in via-ketens worden GENEGEERD — zee-corridors zijn kaal haven→haven;
// searoute bepaalt zelf langs welke knelpunten de route loopt. Aanloophavens
// (port-nodes in via) blijven wél echte tussenstops.
//
// Gebruik:  node tools/extract_corridors.js [grondstof-id ...]
//           (geen argumenten = alle grondstoffen)
// Output:   JSON op stdout: [{ key, a:{lat,lon,id}, b:{lat,lon,id}, uses, resources }]

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.join(__dirname, "..");
const wanted = process.argv.slice(2);

// data-laag laden zoals de browser dat doet (volgorde: chokepoints, registry, rest)
const ctx = { CONFIG: {}, console };
vm.createContext(ctx);
let src =
  fs.readFileSync(path.join(ROOT, "data/_chokepoints.js"), "utf8") + "\n" +
  fs.readFileSync(path.join(ROOT, "data/_registry.js"), "utf8") + "\n";
for (const f of fs.readdirSync(path.join(ROOT, "data"))) {
  if (f.endsWith(".js") && !f.startsWith("_")) {
    src += fs.readFileSync(path.join(ROOT, "data", f), "utf8") + "\n";
  }
}
src += ";globalThis.__WP=WAYPOINTS;globalThis.__R=RESOURCES;";
vm.runInContext(src, ctx);
const WP = ctx.__WP;
const RESOURCES = ctx.__R;

// replica van flows.js isSeaPoint
function isSeaPoint(p) {
  if (p.kind === "grensovergang") return false;
  return p.type === "port" || p.coastal === true ||
    (p.id && String(p.id).startsWith("wp-"));
}

// zelfde sleutelformaat als flows.js straks: 3 decimalen, paar gesorteerd
const fmt = (p) => `${(+p.lat).toFixed(3)},${(+p.lon).toFixed(3)}`;
const keyOf = (a, b) => [fmt(a), fmt(b)].sort().join("|");

const corridors = new Map();
for (const res of RESOURCES) {
  if (wanted.length && !wanted.includes(res.id)) continue;
  const byId = {};
  (res.nodes || []).forEach((n) => (byId[n.id] = n));
  for (const flow of res.flows || []) {
    if ((flow.mode || "ship") !== "ship") continue;
    const from = byId[flow.from], to = byId[flow.to];
    if (!from || !to) continue;
    const stops = [from];
    (flow.via || []).forEach((id) => {
      if (String(id).startsWith("wp-")) return; // MARNET beslist — geen route-dwang
      const p = byId[id] || WP[id];
      if (p) stops.push(p);
    });
    stops.push(to);
    for (let i = 0; i < stops.length - 1; i++) {
      const a = stops[i], b = stops[i + 1];
      if (!isSeaPoint(a) || !isSeaPoint(b)) continue;
      const key = keyOf(a, b);
      if (!corridors.has(key)) {
        corridors.set(key, {
          key,
          a: { lat: +a.lat, lon: +a.lon, id: a.id },
          b: { lat: +b.lat, lon: +b.lon, id: b.id },
          uses: 0,
          resources: new Set(),
        });
      }
      const c = corridors.get(key);
      c.uses++;
      c.resources.add(res.id);
    }
  }
}

const out = [...corridors.values()]
  .sort((x, y) => (x.key < y.key ? -1 : 1)) // determinisme
  .map((c) => ({ ...c, resources: [...c.resources].sort() }));
process.stdout.write(JSON.stringify(out, null, 1));
