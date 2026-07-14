// searoute.js — ECHTE ROUTES OVER ZEE ÉN OVER LAND.
//
// Tot nu toe trokken we rechte great-circle-lijnen tussen handmatig geprikte
// punten. Die lopen vrolijk dwars over Java of dwars over de Oostzee. Deze laag
// zoekt het pad zélf: A* over een land/zee-raster van de wereld.
//
// TWEE KAARTEN, ÉÉN RASTER
//   SeaRoute  — water begaanbaar, land onbegaanbaar. Voor schepen.
//   LandRoute — land begaanbaar, water onbegaanbaar. Voor trein, weg, pijpleiding.
//
// HOE HET RASTER ONTSTAAT
//   1. De landpolygonen uit geo-data.js worden op een canvas getekend
//      (0.25° per cel = 1440×720 cellen). Zwart = land, wit = water.
//   2. ZEE: rond elk knelpunt uit _chokepoints.js wordt water GEFORCEERD. Nodig,
//      want de Straat van Lombok is ~35 km breed en een rastercel ~28 km — zo'n
//      straat slibt dicht en dan vaart A* om heel Indonesië heen. Ook Suez en
//      Panama bestaan alleen dankzij deze stap: een kanaal is te smal voor welk
//      wereldraster dan ook.
//   3. LAND: het spiegelbeeld. Bij bruggen en tunnels (LAND_LINKS) wordt LAND
//      geforceerd, anders zou een trein van Bitterfeld naar Skellefteå om de
//      hele Oostzee heen moeten via Polen, de Baltische staten en Finland.
//   4. Cellen aan de rand krijgen een boete: schepen varen niet rakelings langs
//      de kust, en treinen rijden niet het liefst over het strand.
//
// PRESTATIE: elk pad wordt één keer berekend en gecached. Veel stromen delen
// bovendien dezelfde stukken (Lombok → Makassar → Zuid-Chinese Zee), dus die
// worden maar één keer gezocht.

const Routing = (function () {
  const C = CONFIG.searoute;

  const NX = Math.round(360 / C.cellDeg);
  const NY = Math.round(180 / C.cellDeg);

  let seaCost = null;    // Float32Array: Infinity = land
  let landCost = null;   // Float32Array: Infinity = water
  let ready = false;
  const cache = new Map();

  const idx = (x, y) => y * NX + x;
  const wrapX = (x) => ((x % NX) + NX) % NX;
  const lonOf = (x) => (x + 0.5) * C.cellDeg - 180;
  const latOf = (y) => 90 - (y + 0.5) * C.cellDeg;
  const xOf = (lon) => wrapX(Math.floor(((lon + 180) / 360) * NX));
  const yOf = (lat) => Math.max(0, Math.min(NY - 1, Math.floor(((90 - lat) / 180) * NY)));

  function dist(x1, y1, x2, y2) {
    const la1 = latOf(y1) * Math.PI / 180;
    const la2 = latOf(y2) * Math.PI / 180;
    let dLon = Math.abs(lonOf(x1) - lonOf(x2));
    if (dLon > 180) dLon = 360 - dLon;
    const dLat = latOf(y1) - latOf(y2);
    const dx = dLon * Math.cos((la1 + la2) / 2);
    return Math.sqrt(dx * dx + dLat * dLat);
  }

  // schijf van cellen rond een punt op een vaste waarde zetten
  function stamp(grid, lat, lon, radiusDeg, value) {
    const rad = Math.ceil(radiusDeg / C.cellDeg);
    const cx = xOf(lon), cy = yOf(lat);
    for (let dy = -rad; dy <= rad; dy++) {
      for (let dx = -rad; dx <= rad; dx++) {
        if (dx * dx + dy * dy > rad * rad) continue;
        const y = cy + dy;
        if (y < 0 || y >= NY) continue;
        grid[idx(wrapX(cx + dx), y)] = value;
      }
    }
  }

  function build() {
    if (typeof LAND_POLYS === "undefined") {
      console.warn("[routing] geo-data.js niet geladen — routering uitgeschakeld");
      return;
    }
    const t0 = performance.now();

    const cv = document.createElement("canvas");
    cv.width = NX; cv.height = NY;
    const ctx = cv.getContext("2d", { willReadFrequently: true });
    ctx.fillStyle = "#fff";
    ctx.fillRect(0, 0, NX, NY);

    const X = (lon) => ((lon + 180) / 360) * NX;
    const Y = (lat) => ((90 - lat) / 180) * NY;

    ctx.fillStyle = "#000";
    LAND_POLYS.forEach((poly) => {
      ctx.beginPath();
      poly.forEach((ring) => {
        ring.forEach((p, i) => (i ? ctx.lineTo(X(p[0]), Y(p[1])) : ctx.moveTo(X(p[0]), Y(p[1]))));
        ctx.closePath();
      });
      ctx.fill("evenodd");
    });

    const px = ctx.getImageData(0, 0, NX, NY).data;

    // twee kaarten: 1 = land, 0 = water
    const seaLand = new Uint8Array(NX * NY);   // voor de ZEEkaart
    const landLand = new Uint8Array(NX * NY);  // voor de LANDkaart
    for (let i = 0; i < NX * NY; i++) {
      const v = px[i * 4] < 128 ? 1 : 0;
      seaLand[i] = v;
      landLand[i] = v;
    }

    // ZEE: zeestraten en kanalen openhouden. Een waypoint mag een eigen
    // openRadius meegeven: smalle rivieren (Saint-Laurent) wil je met kleine
    // schijfjes openen, anders forceer je per ongeluk water dwars door een
    // landengte heen. Grensovergangen (kind: "grensovergang") zijn juist
    // LANDpunten: die houden de landkaart open in plaats van de zeekaart.
    if (typeof WAYPOINTS !== "undefined") {
      Object.values(WAYPOINTS).forEach((wp) => {
        if (wp.kind !== "grensovergang")
          stamp(seaLand, wp.lat, wp.lon, wp.openRadius || C.openRadiusDeg, 0);
        else
          stamp(landLand, wp.lat, wp.lon, wp.bridgeRadius || C.bridgeRadiusDeg, 1);
      });
    }
    // LAND: bruggen en tunnels laten bestaan
    if (typeof LAND_LINKS !== "undefined") {
      LAND_LINKS.forEach((ll) =>
        stamp(landLand, ll.lat, ll.lon, C.bridgeRadiusDeg, 1));
    }

    seaCost = new Float32Array(NX * NY);
    landCost = new Float32Array(NX * NY);

    for (let y = 0; y < NY; y++) {
      for (let x = 0; x < NX; x++) {
        const i = idx(x, y);

        // ---- zeekaart: water begaanbaar, kustcellen duurder
        if (seaLand[i]) {
          seaCost[i] = Infinity;
        } else {
          let coastal = false;
          for (let dy = -1; dy <= 1 && !coastal; dy++) {
            for (let dx = -1; dx <= 1; dx++) {
              const yy = y + dy;
              if (yy < 0 || yy >= NY) continue;
              if (seaLand[idx(wrapX(x + dx), yy)]) { coastal = true; break; }
            }
          }
          seaCost[i] = coastal ? C.coastPenalty : 1;
        }

        // ---- landkaart: precies andersom
        landCost[i] = landLand[i] ? 1 : Infinity;
      }
    }

    ready = true;
    console.log(`[routing] raster klaar: ${NX}×${NY} in ${Math.round(performance.now() - t0)} ms`);
  }

  // Een haven ligt op de kust en valt dus vaak nét in de verkeerde cel.
  // Schuif hem naar de dichtstbijzijnde begaanbare cel van de juiste kaart.
  function snap(costGrid, lat, lon) {
    const x0 = xOf(lon), y0 = yOf(lat);
    if (isFinite(costGrid[idx(x0, y0)])) return { x: x0, y: y0 };
    for (let r = 1; r <= 14; r++) {
      for (let dy = -r; dy <= r; dy++) {
        for (let dx = -r; dx <= r; dx++) {
          if (Math.max(Math.abs(dx), Math.abs(dy)) !== r) continue;
          const y = y0 + dy;
          if (y < 0 || y >= NY) continue;
          const x = wrapX(x0 + dx);
          if (isFinite(costGrid[idx(x, y)])) return { x, y };
        }
      }
    }
    return null;
  }

  function makeHeap() {
    const a = [];
    return {
      size: () => a.length,
      push(node) {
        a.push(node);
        let i = a.length - 1;
        while (i > 0) {
          const p = (i - 1) >> 1;
          if (a[p].f <= a[i].f) break;
          [a[p], a[i]] = [a[i], a[p]];
          i = p;
        }
      },
      pop() {
        const top = a[0];
        const last = a.pop();
        if (a.length) {
          a[0] = last;
          let i = 0;
          for (;;) {
            const l = 2 * i + 1, r = l + 1;
            let m = i;
            if (l < a.length && a[l].f < a[m].f) m = l;
            if (r < a.length && a[r].f < a[m].f) m = r;
            if (m === i) break;
            [a[m], a[i]] = [a[i], a[m]];
            i = m;
          }
        }
        return top;
      },
    };
  }

  function search(costGrid, a, b, label) {
    const start = snap(costGrid, a.lat, a.lon);
    const goal = snap(costGrid, b.lat, b.lon);
    if (!start || !goal) return null;

    const N = NX * NY;
    const g = new Float32Array(N).fill(Infinity);
    const from = new Int32Array(N).fill(-1);
    const closed = new Uint8Array(N);

    const sI = idx(start.x, start.y);
    const gI = idx(goal.x, goal.y);
    g[sI] = 0;

    const W = C.heuristicWeight;
    const heap = makeHeap();
    heap.push({ i: sI, x: start.x, y: start.y, f: dist(start.x, start.y, goal.x, goal.y) * W });

    let guard = 0;
    let found = sI === gI;

    while (heap.size() && guard++ < C.maxExpansions) {
      const cur = heap.pop();
      if (closed[cur.i]) continue;
      closed[cur.i] = 1;
      if (cur.i === gI) { found = true; break; }

      for (let dy = -1; dy <= 1; dy++) {
        for (let dx = -1; dx <= 1; dx++) {
          if (!dx && !dy) continue;
          const ny = cur.y + dy;
          if (ny < 0 || ny >= NY) continue;
          const nx = wrapX(cur.x + dx);
          const ni = idx(nx, ny);
          const c = costGrid[ni];
          if (!isFinite(c) || closed[ni]) continue;

          const ng = g[cur.i] + dist(cur.x, cur.y, nx, ny) * c;
          if (ng >= g[ni]) continue;
          g[ni] = ng;
          from[ni] = cur.i;
          // gewogen A*: gretiger richting het doel, dus veel minder zoekwerk
          heap.push({ i: ni, x: nx, y: ny, f: ng + dist(nx, ny, goal.x, goal.y) * W });
        }
      }
    }

    if (!found) {
      console.warn(`[routing/${label}] geen route gevonden`,
        `${a.name || a.id || ""} -> ${b.name || b.id || ""}`, `(${guard} stappen)`);
      return null;
    }

    const path = [];
    let i = gI;
    while (i !== -1) {
      const y = Math.floor(i / NX);
      const x = i - y * NX;
      path.push({ lat: latOf(y), lon: lonOf(x) });
      if (i === sI) break;
      i = from[i];
    }
    path.reverse();

    const out = [];
    for (let k = 0; k < path.length; k += C.simplify) out.push(path[k]);
    const last = path[path.length - 1];
    if (out[out.length - 1] !== last) out.push(last);
    return out;
  }

  function cached(kind, grid, a, b) {
    if (!ready) return null;
    const key = `${kind}:${a.lat.toFixed(2)},${a.lon.toFixed(2)}>${b.lat.toFixed(2)},${b.lon.toFixed(2)}`;
    if (cache.has(key)) return cache.get(key);
    const p = search(grid, a, b, kind);
    cache.set(key, p);
    return p;
  }

  return {
    init() { if (C.enabled && !ready) build(); },
    isReady: () => ready,
    sea: (a, b) => cached("zee", seaCost, a, b),
    land: (a, b) => cached("land", landCost, a, b),
  };
})();

// Oude naam blijft werken (flows.js gebruikte SeaRoute)
const SeaRoute = {
  init: () => Routing.init(),
  isReady: () => Routing.isReady(),
  path: (a, b) => Routing.sea(a, b),
};
