// marnet.js — het MARNET-vaarlanen-netwerk als laag op de bol, plus routering.
//
// DIT IS DE KERN VAN M23 (LAR-483). Het netwerk is bij het bakken ÉÉN KEER
// verzoend met dezelfde 1:10M-vectorwereld die op het scherm staat: lange
// koorden zijn langs de grootcirkel verdicht, edges die land sneden zijn
// omgelegd, en bevaarbaar binnenwater (Suez, Mississippi, Seaway, Wolga-Don,
// Paraná, …) is als aparte soort geflagd. Routeren = A* over deze graaf —
// haven→haven, zonder per-paar reparaties. Knelpunt blokkeren wordt later
// (M21): edge eruit → herrouteren.
//
// Formaat (gebakken door tools/bake_marnet.py, zelfde varint-idee als world):
//   marnet.json  { schaal, knopen, edges, punten, passages, … }
//   marnet.bin   blok 1: knopen (delta-lon/lat, zigzag-varint)
//                blok 2: per edge a, b (delta t.o.v. vorige edge), lengte
//                        (0,1 km), soort (0=zee, 1=binnenwater), aantal punten
//                blok 3: per edge de geometrie als delta's; punt 1 = knoop a

import * as THREE from "three";

const KLEUR_ZEE = new THREE.Color(0x2f9bdd);
const KLEUR_BINNEN = new THREE.Color(0xd9a441);

/** Zelfde zigzag-varint-idee als world.js (bewust gekopieerd: een import van
 *  world.js?v=… zou de module dubbel laden zodra de versies uiteenlopen).
 *  Zonder bit-operatoren: die knippen op 32 bits, terwijl vermenigvuldigen
 *  tot 2^53 exact blijft — en alle deltas hier passen daar ruim in. */
function maakLezer(bytes) {
  let p = 0;
  return {
    volgende() {
      let res = 0;
      let factor = 1;
      while (true) {
        const b = bytes[p++];
        res += (b & 0x7f) * factor;
        if ((b & 0x80) === 0) break;
        factor *= 128;
      }
      // zigzag terugdraaien: even = positief, oneven = negatief
      const half = Math.floor(res / 2);
      return res % 2 === 0 ? half : -half - 1;
    },
  };
}

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js / v1's latLonToVec3 — zie de
  // waarschuwing in de project-CLAUDE.md: een 90°-fout oogt onderling perfect
  // maar ligt los van de bol.
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const cosLat = Math.cos(lat);
  uit[o + 0] = r * cosLat * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * cosLat * Math.sin(lon);
}

/**
 * Laadt het netwerk en bouwt er één LineSegments van (één draw call; kleur
 * per soort via vertex colors) + de graaf waar de router over rekent.
 */
export async function laadMarnet(radius) {
  const t0 = performance.now();

  // ?v= mee op de data: zelfde cache-busting-discipline als de scripts —
  // verandert de bake, dan bumpt de versie en kan geen cache blijven hangen.
  const [meta, buffer] = await Promise.all([
    fetch("data/marnet.json?v=011").then((r) => {
      if (!r.ok) throw new Error(`marnet.json: HTTP ${r.status}`);
      return r.json();
    }),
    fetch("data/marnet.bin?v=011").then((r) => {
      if (!r.ok) throw new Error(`marnet.bin: HTTP ${r.status}`);
      return r.arrayBuffer();
    }),
  ]);
  const tGeladen = performance.now();

  const lezer = maakLezer(new Uint8Array(buffer));
  const schaal = meta.schaal;
  const nKnopen = meta.knopen;
  const nEdges = meta.edges;
  const nPunten = meta.punten;

  // --- blok 1: knopen ------------------------------------------------------
  const knoopLon = new Float64Array(nKnopen);
  const knoopLat = new Float64Array(nKnopen);
  {
    let x = 0, y = 0;
    for (let i = 0; i < nKnopen; i++) {
      x += lezer.volgende();
      y += lezer.volgende();
      knoopLon[i] = x / schaal;
      knoopLat[i] = y / schaal;
    }
  }

  // --- blok 2: edges -------------------------------------------------------
  const edgeA = new Uint32Array(nEdges);
  const edgeB = new Uint32Array(nEdges);
  const edgeKm = new Float32Array(nEdges);
  const edgeSoort = new Uint8Array(nEdges);
  const geomN = new Uint32Array(nEdges);
  {
    let a = 0, b = 0;
    for (let i = 0; i < nEdges; i++) {
      a += lezer.volgende();
      b += lezer.volgende();
      edgeA[i] = a;
      edgeB[i] = b;
      edgeKm[i] = lezer.volgende() / 10;
      edgeSoort[i] = lezer.volgende();
      geomN[i] = lezer.volgende();
    }
  }

  // --- blok 3: geometrie ---------------------------------------------------
  const posities = new Float32Array(nPunten * 3);
  const kleuren = new Float32Array(nPunten * 3);
  const geomStart = new Uint32Array(nEdges);
  let nSegmenten = 0;
  for (let i = 0; i < nEdges; i++) nSegmenten += geomN[i] - 1;
  const indices = new Uint32Array(nSegmenten * 2);

  {
    let pi = 0, ii = 0;
    for (let e = 0; e < nEdges; e++) {
      geomStart[e] = pi;
      const kleur = edgeSoort[e] === 1 ? KLEUR_BINNEN : KLEUR_ZEE;
      let x = Math.round(knoopLon[edgeA[e]] * schaal);
      let y = Math.round(knoopLat[edgeA[e]] * schaal);
      for (let k = 0; k < geomN[e]; k++) {
        if (k > 0) {
          x += lezer.volgende();
          y += lezer.volgende();
          indices[ii++] = pi - 1;
          indices[ii++] = pi;
        }
        opBol(x / schaal, y / schaal, radius, posities, pi * 3);
        kleuren[pi * 3 + 0] = kleur.r;
        kleuren[pi * 3 + 1] = kleur.g;
        kleuren[pi * 3 + 2] = kleur.b;
        pi++;
      }
    }
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(posities, 3));
  geo.setAttribute("color", new THREE.BufferAttribute(kleuren, 3));
  geo.setIndex(new THREE.BufferAttribute(indices, 1));

  const mat = new THREE.LineBasicMaterial({
    vertexColors: true,
    transparent: true,
    opacity: 0.55,
  });
  const lijnen = new THREE.LineSegments(geo, mat);
  lijnen.renderOrder = 3; // boven de kustlijn (2)

  // --- graaf (CSR-adjacency) ----------------------------------------------
  const graad = new Uint32Array(nKnopen + 1);
  for (let e = 0; e < nEdges; e++) {
    graad[edgeA[e] + 1]++;
    graad[edgeB[e] + 1]++;
  }
  for (let i = 0; i < nKnopen; i++) graad[i + 1] += graad[i];
  const adjEdge = new Uint32Array(nEdges * 2);
  const adjKnoop = new Uint32Array(nEdges * 2);
  {
    const kop = graad.slice(0, nKnopen);
    for (let e = 0; e < nEdges; e++) {
      const a = edgeA[e], b = edgeB[e];
      adjEdge[kop[a]] = e; adjKnoop[kop[a]++] = b;
      adjEdge[kop[b]] = e; adjKnoop[kop[b]++] = a;
    }
  }

  // eenheidsvectoren per knoop voor de A*-heuristiek (grootcirkel via dot)
  const knoopXYZ = new Float64Array(nKnopen * 3);
  for (let i = 0; i < nKnopen; i++) {
    const lon = knoopLon[i] * (Math.PI / 180);
    const lat = knoopLat[i] * (Math.PI / 180);
    knoopXYZ[i * 3 + 0] = Math.cos(lat) * Math.cos(lon);
    knoopXYZ[i * 3 + 1] = Math.sin(lat);
    knoopXYZ[i * 3 + 2] = Math.cos(lat) * Math.sin(lon);
  }

  // passage-label per edge (schaars: alleen zeestraten/kanalen zijn gelabeld)
  const edgeLabel = new Array(nEdges).fill(null);
  for (const [ei, label] of Object.entries(meta.passages || {})) {
    edgeLabel[Number(ei)] = label;
  }

  const t1 = performance.now();

  return {
    lijnen,
    schaal,
    knoopLon, knoopLat, knoopXYZ,
    edgeA, edgeB, edgeKm, edgeSoort, edgeLabel,
    geomStart, geomN, posities,
    adjStart: graad, adjEdge, adjKnoop,
    passages: meta.passages || {},
    stats: {
      knopen: nKnopen,
      edges: nEdges,
      punten: nPunten,
      netwerkKm: meta.netwerkKm,
      kbOverdracht: Math.round((buffer.byteLength + JSON.stringify(meta).length) / 1024),
      msLaden: Math.round(tGeladen - t0),
      msVerwerken: Math.round(t1 - tGeladen),
    },
  };
}

const R_AARDE = 6371;

function gcKm(net, i, j) {
  const d = net.knoopXYZ[i * 3] * net.knoopXYZ[j * 3]
    + net.knoopXYZ[i * 3 + 1] * net.knoopXYZ[j * 3 + 1]
    + net.knoopXYZ[i * 3 + 2] * net.knoopXYZ[j * 3 + 2];
  return R_AARDE * Math.acos(Math.max(-1, Math.min(1, d)));
}

/** Dichtstbijzijnde netwerk-knoop bij een lon/lat (voor klik-op-de-kaart). */
export function dichtstbijzijndeKnoop(net, lon, lat) {
  const lo = lon * (Math.PI / 180), la = lat * (Math.PI / 180);
  const vx = Math.cos(la) * Math.cos(lo), vy = Math.sin(la), vz = Math.cos(la) * Math.sin(lo);
  let beste = -1, besteDot = -2;
  for (let i = 0; i < net.knoopLon.length; i++) {
    const d = net.knoopXYZ[i * 3] * vx + net.knoopXYZ[i * 3 + 1] * vy + net.knoopXYZ[i * 3 + 2] * vz;
    if (d > besteDot) { besteDot = d; beste = i; }
  }
  return beste;
}

/**
 * A* van knoop naar knoop. Geeft { edges, knopen, km } of null.
 * De heuristiek (grootcirkel-afstand) is toelaatbaar: geen pad is korter dan
 * de grootcirkel, dus het gevonden pad is exact het kortste over de graaf —
 * ook mét straf, want een straf maakt paden alleen maar duurder.
 *
 * opties.vermijd — passage-labels die dicht zijn. Default ["northwest"]:
 *   exact searoute's eigen default (restrictions=[northwest]) — de
 *   Noordwest-Passage is geometrisch vaak het kortst naar Azië maar geen
 *   commerciële route. Voor M21 (knelpunt-simulator) is dit meteen het
 *   mechanisme: "Suez dicht" = "suez" aan deze lijst toevoegen.
 * opties.arctisFactor — kostfactor voor edges die geheel boven de poolcirkel
 *   liggen (default 1 = uit; zet bv. 2 om de Noordelijke Zeeroute alleen te
 *   laten winnen als er geen redelijk alternatief is).
 */
export function zoekRoute(net, van, naar, opties = {}) {
  const vermijd = opties.vermijd ?? ["northwest"];
  const arctisFactor = opties.arctisFactor ?? 1;
  const dichtLabel = new Set(vermijd);
  const n = net.knoopLon.length;
  const g = new Float64Array(n).fill(Infinity);
  const vorigeEdge = new Int32Array(n).fill(-1);
  const vorigeKnoop = new Int32Array(n).fill(-1);
  const dicht = new Uint8Array(n);

  // binaire heap van [f, knoop] — ruim bemeten: een knoop kan vaker gepusht
  // worden voordat hij dichtgaat (decrease-key via her-push)
  const heapF = new Float64Array(n * 8);
  const heapK = new Int32Array(n * 8);
  let heapN = 0;
  function push(f, k) {
    let i = heapN++;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (heapF[p] <= f) break;
      heapF[i] = heapF[p]; heapK[i] = heapK[p];
      i = p;
    }
    heapF[i] = f; heapK[i] = k;
  }
  function pop() {
    const topK = heapK[0];
    const f = heapF[--heapN], k = heapK[heapN];
    let i = 0;
    while (true) {
      const l = i * 2 + 1, r = l + 1;
      let kleinste = i;
      if (l < heapN && heapF[l] < (kleinste === i ? f : heapF[kleinste])) kleinste = l;
      if (r < heapN && heapF[r] < (kleinste === i ? f : heapF[kleinste])) kleinste = r;
      if (kleinste === i) break;
      heapF[i] = heapF[kleinste]; heapK[i] = heapK[kleinste];
      i = kleinste;
    }
    heapF[i] = f; heapK[i] = k;
    return topK;
  }

  g[van] = 0;
  push(gcKm(net, van, naar), van);
  while (heapN > 0) {
    const cur = pop();
    if (dicht[cur]) continue;
    dicht[cur] = 1;
    if (cur === naar) break;
    for (let a = net.adjStart[cur]; a < net.adjStart[cur + 1]; a++) {
      const buur = net.adjKnoop[a];
      if (dicht[buur]) continue;
      const e = net.adjEdge[a];
      if (net.edgeLabel[e] !== null && dichtLabel.has(net.edgeLabel[e])) continue;
      let kost = net.edgeKm[e];
      if (arctisFactor !== 1 &&
          net.knoopLat[net.edgeA[e]] > 66.5 && net.knoopLat[net.edgeB[e]] > 66.5) {
        kost *= arctisFactor;
      }
      const ng = g[cur] + kost;
      if (ng < g[buur]) {
        g[buur] = ng;
        vorigeEdge[buur] = e;
        vorigeKnoop[buur] = cur;
        push(ng + gcKm(net, buur, naar), buur);
      }
    }
  }
  if (!dicht[naar]) return null;

  const edges = [], knopen = [naar];
  let k = naar;
  while (k !== van) {
    edges.push(vorigeEdge[k]);
    k = vorigeKnoop[k];
    knopen.push(k);
  }
  edges.reverse();
  knopen.reverse();
  // km = de échte afstand (g bevat bij een straf ook de strafkilometers)
  let km = 0;
  for (const e of edges) km += net.edgeKm[e];
  return { edges, knopen, km };
}

/**
 * Bouwt een THREE.Line voor een gevonden route: de geometrie van de edges in
 * de juiste richting achter elkaar. Extra's vooraan/achteraan (haven→knoop)
 * kunnen via voorstuk/nastuk (arrays van [lon, lat]).
 */
export function bouwRouteLijn(net, route, radius, voorstuk = [], nastuk = []) {
  let totaal = voorstuk.length + nastuk.length;
  for (const e of route.edges) totaal += net.geomN[e];
  const pos = new Float32Array(totaal * 3);
  let pi = 0;

  for (const [lon, lat] of voorstuk) {
    opBol(lon, lat, radius, pos, pi * 3); pi++;
  }
  let bij = route.knopen[0];
  for (const e of route.edges) {
    const start = net.geomStart[e], n = net.geomN[e];
    const vooruit = net.edgeA[e] === bij;
    for (let k = 0; k < n; k++) {
      const idx = vooruit ? start + k : start + (n - 1 - k);
      pos[pi * 3] = net.posities[idx * 3];
      pos[pi * 3 + 1] = net.posities[idx * 3 + 1];
      pos[pi * 3 + 2] = net.posities[idx * 3 + 2];
      pi++;
    }
    bij = vooruit ? net.edgeB[e] : net.edgeA[e];
  }
  for (const [lon, lat] of nastuk) {
    opBol(lon, lat, radius, pos, pi * 3); pi++;
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos.subarray(0, pi * 3), 3));
  const lijn = new THREE.Line(geo, new THREE.LineBasicMaterial({
    color: 0xffe066,
    transparent: true,
    opacity: 0.95,
  }));
  lijn.renderOrder = 4;
  return lijn;
}

/** Laadt de havens (gebakken uit searoute's ports.geojson). */
export async function laadHavens() {
  const r = await fetch("data/ports.json?v=011");
  if (!r.ok) throw new Error(`ports.json: HTTP ${r.status}`);
  const d = await r.json();
  const havens = [];
  for (let i = 0; i < d.aantal; i++) {
    havens.push({
      naam: d.namen[i],
      land: d.landen[i],
      locode: d.locodes[i],
      lon: d.ll[i * 2],
      lat: d.ll[i * 2 + 1],
      knoop: d.knoop[i],
      afstandKm: d.afstandKm[i],
    });
  }
  return havens;
}
