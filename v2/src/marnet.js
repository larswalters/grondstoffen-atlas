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
//                        (0,1 km), soort (0=zee, 1=binnenwater), aantal punten,
//                        gabarietvlag (0 = geen maten; 1 = er volgen vier
//                        varints: diepgang, breedte, lengte, hoogte in DECIMETER
//                        met 0 = onbekend — LAR-514)
//                blok 3: per edge de geometrie als delta's; punt 1 = knoop a

import * as THREE from "three";

// De routeerfuncties leven sinds 2026-07-23 in `router.js`, zónder three, zodat
// de headless toets (`v2/tools/toets_routes.mjs`) exact dezelfde code draait als
// de browser. Hier alleen her-exporteren: voor iedereen die `marnet.js`
// importeert verandert er niets.
export {
  zoekRoute,
  zoekRouteRealistisch,
  binnenSystemenBij,
  dichtstbijzijndeKnoop,
  gcKmLL,
} from "./router.js?v=063";

const KLEUR_ZEE = new THREE.Color(0x2f9bdd);
const KLEUR_BINNEN = new THREE.Color(0xd9a441);
// Bulklaag (LAR-515): fel rood, hoge opaciteit. Eerst gedempt amber geprobeerd
// (0xa8814a @ 0,35) om de getoetste ketens te laten winnen, maar dat bleek
// in de praktijk vrijwel onzichtbaar — Lars zag de laag niet. Zichtbaarheid
// gaat voor: de bulklaag moet nú opvallen; ontoetsbaarheid blijft geborgd
// doordat hij buiten de routeergraaf staat, niet doordat hij onopvallend is.
const KLEUR_BULK = new THREE.Color(0xff1a1a);
const OPACITEIT_BULK = 0.85;

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
export async function laadMarnet(radius, klemOpHorizon = null) {
  const t0 = performance.now();

  // ?v= mee op de data: zelfde cache-busting-discipline als de scripts —
  // verandert de bake, dan bumpt de versie en kan geen cache blijven hangen.
  const [meta, buffer] = await Promise.all([
    fetch("data/marnet.json?v=058").then((r) => {
      if (!r.ok) throw new Error(`marnet.json: HTTP ${r.status}`);
      return r.json();
    }),
    fetch("data/marnet.bin?v=058").then((r) => {
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
  // Gabariet per edge (LAR-514), in DECIMETER met 0 = onbekend. Uint16 is ruim:
  // de grootste maat die hier ooit in komt is de Poe Lock op 366 m = 3.660 dm.
  // ⚠️ 0 betekent ONBEKEND en dus GEEN GRENS — nooit "past niet".
  const edgeDiepgang = new Uint16Array(nEdges);
  const edgeBreedte = new Uint16Array(nEdges);
  const edgeLengte = new Uint16Array(nEdges);
  const edgeHoogte = new Uint16Array(nEdges);
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
      if (lezer.volgende() === 1) {
        edgeDiepgang[i] = lezer.volgende();
        edgeBreedte[i] = lezer.volgende();
        edgeLengte[i] = lezer.volgende();
        edgeHoogte[i] = lezer.volgende();
      }
    }
  }

  // --- blok 3: geometrie ---------------------------------------------------
  const posities = new Float32Array(nPunten * 3);
  const kleuren = new Float32Array(nPunten * 3);
  const geomStart = new Uint32Array(nEdges);
  let nSegmenten = 0;
  for (let i = 0; i < nEdges; i++) nSegmenten += geomN[i] - 1;
  const indices = new Uint32Array(nSegmenten * 2);

  // Welke edges horen bij het mechanisch gefilterde riviernet? Die krijgen een
  // eigen kleur, want het verschil tussen GETOETST en MECHANISCH moet zichtbaar
  // blijven nu ze in één net zitten. Het is dus geen aparte laag meer maar een
  // eigenschap van de lijn — precies zoals diepgang en breedte dat zijn.
  const isBulk = new Uint8Array(nEdges);
  for (const v of Object.values(meta.vaarwegen || {})) {
    if (v && v.bulk && Array.isArray(v.edges)) {
      for (const ei of v.edges) isBulk[ei] = 1;
    }
  }

  {
    let pi = 0, ii = 0;
    for (let e = 0; e < nEdges; e++) {
      geomStart[e] = pi;
      const kleur = isBulk[e] ? KLEUR_BULK
        : (edgeSoort[e] === 1 ? KLEUR_BINNEN : KLEUR_ZEE);
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
  if (klemOpHorizon) klemOpHorizon(mat);
  const lijnen = new THREE.LineSegments(geo, mat);
  lijnen.renderOrder = 6.5;   // boven de tegels (1-3) en de kustlijn (6)

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
    edgeDiepgang, edgeBreedte, edgeLengte, edgeHoogte,   // dm, 0 = onbekend
    geomStart, geomN, posities,
    adjStart: graad, adjEdge, adjKnoop,
    passages: meta.passages || {},
    vaarwegen: meta.vaarwegen || {},   // M24: {label: {zeevaart, cemt, bron, …}}
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

/**
 * Bulklaag (LAR-515): PUUR TEKENGEOMETRIE, volledig los van laadMarnet()/NET.
 *
 * Bewust geen onderdeel van de routeergraaf — een eerder ontwerp stitchte de
 * bulklaag tot een junction-graaf zoals de verhalende ketens, maar dat gaf op
 * Nederland alleen al 23.189 knopen/edges (méér dan het hele huidige netwerk),
 * want bulkketens zijn extreem kort. Zonder topologie bestaat dat risico niet:
 * dit is een aparte fetch, een apart bestand (marnet-bulk.json), en een aparte
 * THREE.Group per regio. `zoekRoute`/`zoekRouteRealistisch`/`binnenSystemenBij`
 * raken deze data nooit — een bulk-edge kan dus per constructie geen zeeroute
 * bekorten, niet toevallig.
 *
 * Formaat: { regios: { "bulk-eu": { km, bronKm, weggenomenKm, polylines }, … } }
 * — polylines is een array van [lon,lat]-punt-arrays, al door bake_marnet.py's
 * 250 m-uitsluiting gehaald.
 */
export async function laadBulk(radius) {
  const t0 = performance.now();
  const meta = await fetch("data/marnet-bulk.json?v=058").then((r) => {
    if (!r.ok) throw new Error(`marnet-bulk.json: HTTP ${r.status}`);
    return r.json();
  });

  const groep = new THREE.Group();
  groep.name = "marnet-bulk";
  const regioLijnen = {};
  let totaalKm = 0, totaalPunten = 0, totaalLijnen = 0;

  for (const [label, v] of Object.entries(meta.regios || {})) {
    const lijnen = v.polylines || [];
    let nPunten = 0;
    for (const p of lijnen) nPunten += p.length;
    const posities = new Float32Array(nPunten * 3);
    const indices = new Uint32Array(Math.max(0, nPunten - lijnen.length) * 2);
    let pi = 0, ii = 0;
    for (const p of lijnen) {
      for (let k = 0; k < p.length; k++) {
        opBol(p[k][0], p[k][1], radius, posities, pi * 3);
        if (k > 0) { indices[ii++] = pi - 1; indices[ii++] = pi; }
        pi++;
      }
    }

    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(posities, 3));
    geo.setIndex(new THREE.BufferAttribute(indices, 1));
    const mat = new THREE.LineBasicMaterial({
      color: KLEUR_BULK,
      transparent: true,
      opacity: OPACITEIT_BULK,
      depthWrite: false,   // bulk mag een getoetste keten op een kruising nooit overtekenen
    });
    const mesh = new THREE.LineSegments(geo, mat);
    mesh.name = label;
    mesh.renderOrder = 2.5;  // kustlijn 2 · bulk 2,5 · net 3 · route 4
    groep.add(mesh);
    regioLijnen[label] = mesh;
    totaalKm += v.km || 0;
    totaalPunten += nPunten;
    totaalLijnen += lijnen.length;
  }

  const t1 = performance.now();
  return {
    lijnen: groep,
    regioLijnen,
    regios: meta.regios || {},
    stats: {
      regios: Object.keys(meta.regios || {}).length,
      km: Math.round(totaalKm),
      lijnen: totaalLijnen,
      punten: totaalPunten,
      msLaden: Math.round(t1 - t0),
    },
  };
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

/** Laadt de havens (gebakken uit searoute's ports.geojson).
 *
 * Elke haven draagt sinds [LAR-518] TWEE aanhechtingen: `knoop`/`afstandKm` op
 * het zeenet (ongewijzigd — alle bestaande zeeroutes rekenen hierop) en
 * `knoopRivier`/`afstandRivierKm` op het riviernet. Een haven die beide netten
 * raakt is een kandidaat-overslaghaven; welke het wérkelijk worden is een
 * aangewezen lijst, want een overslagpunt is de plek waar modaliteiten
 * samenkomen — inclusief spoor en weg, die in M25 aan dezelfde haven hangen.
 *
 * `knoopRivier === -1` betekent: er is geen riviernet in deze bake. Dat is iets
 * anders dan "ver weg", en die twee moeten uit elkaar te houden blijven.
 */
export async function laadHavens() {
  const r = await fetch("data/ports.json?v=058");
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
      knoopRivier: d.knoopRivier ? d.knoopRivier[i] : -1,
      afstandRivierKm: d.afstandRivierKm ? d.afstandRivierKm[i] : -1,
      // afstand tot kustlijn of meeroever; -1 = niet gemeten in deze bake
      afstandWaterKm: d.afstandWaterKm ? d.afstandWaterKm[i] : -1,
      // NGA World Port Index-verrijking op LOCODE (LAR-518); "" / -1 = geen
      // match. ⚠️ WPI zet massaal "U" (unknown): een leeg veld betekent
      // "onbekend", nooit "geen spoor" of "geen vracht".
      wpiMaat: d.wpiMaat ? d.wpiMaat[i] : "",
      wpiSpoor: d.wpiSpoor ? d.wpiSpoor[i] : "",
      wpiVracht: d.wpiVracht ? d.wpiVracht[i] : "",
      wpiAfstandKm: d.wpiAfstandKm ? d.wpiAfstandKm[i] : -1,
      // "wpi" = positie geschoond naar de haven-georiënteerde WPI-plek;
      // "locode" = nog de oorspronkelijke plaatscentroïde.
      posBron: d.posBron ? d.posBron[i] : "locode",
    });
  }
  havens.zeeKnopen = d.zeeKnopen ?? null;
  return havens;
}
