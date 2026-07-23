// laad_headless.mjs — leest marnet.bin/landnet.bin in Node tot dezelfde
// net-objecten die de browser bouwt, MAAR zonder three.js: alleen de
// graaf-velden waarop de router en de keten-router rekenen. Zo draait de
// headless toets exact dezelfde code als de browser (router.js/keten.js).
//
// ⚠️ Bewust GEEN kopie van de bit-lezer met three erin: het formaat is één-op-
// één dat van marnet.js/landnet.js, en als het uiteenloopt faalt de toets luid
// (verkeerde knopen → geen route), niet stil.

import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const DATA = join(dirname(fileURLToPath(import.meta.url)), "..", "data");

// De bake schrijft desgewenst naar een suffix (`--suffix=-t`) zodat een nieuwe
// set náást de live set komt te staan en byte-vergeleken kan worden vóór hij
// live gaat. Zonder deze haak kon de headless toets die -t-set niet lezen —
// dan toets je dus altijd de set die er al stond, en dat is precies andersom.
// Gebruik: BAKE_SUFFIX=-t node v2/tools/toets_routes.mjs
// Terugval op de live naam als de suffix-set dat bestand niet heeft: een
// marnet-bake schrijft `marnet-t`/`ports-t` maar raakt `landnet` niet, en dan
// hoort de toets het landnet gewoon te lezen in plaats van te struikelen.
const S = process.env.BAKE_SUFFIX || "";
const bestand = (naam, ext) => {
  const metSuffix = join(DATA, `${naam}${S}.${ext}`);
  return S && existsSync(metSuffix) ? metSuffix : join(DATA, `${naam}.${ext}`);
};

function maakLezer(bytes) {
  let p = 0;
  return {
    volgende() {
      let res = 0, factor = 1;
      while (true) {
        const b = bytes[p++];
        res += (b & 0x7f) * factor;
        if ((b & 0x80) === 0) break;
        factor *= 128;
      }
      const half = Math.floor(res / 2);
      return res % 2 === 0 ? half : -half - 1;
    },
  };
}

function eenheidsXYZ(knoopLon, knoopLat) {
  const n = knoopLon.length;
  const xyz = new Float64Array(n * 3);
  for (let i = 0; i < n; i++) {
    const lon = knoopLon[i] * (Math.PI / 180);
    const lat = knoopLat[i] * (Math.PI / 180);
    xyz[i * 3] = Math.cos(lat) * Math.cos(lon);
    xyz[i * 3 + 1] = Math.sin(lat);
    xyz[i * 3 + 2] = Math.cos(lat) * Math.sin(lon);
  }
  return xyz;
}

function bouwGraaf(nKnopen, nEdges, edgeA, edgeB) {
  const graad = new Uint32Array(nKnopen + 1);
  for (let e = 0; e < nEdges; e++) { graad[edgeA[e] + 1]++; graad[edgeB[e] + 1]++; }
  for (let i = 0; i < nKnopen; i++) graad[i + 1] += graad[i];
  const adjEdge = new Uint32Array(nEdges * 2);
  const adjKnoop = new Uint32Array(nEdges * 2);
  const kop = graad.slice(0, nKnopen);
  for (let e = 0; e < nEdges; e++) {
    const a = edgeA[e], b = edgeB[e];
    adjEdge[kop[a]] = e; adjKnoop[kop[a]++] = b;
    adjEdge[kop[b]] = e; adjKnoop[kop[b]++] = a;
  }
  return { adjStart: graad, adjEdge, adjKnoop };
}

/**
 * Het derde blok van de bin: de LIJNGEOMETRIE per edge (delta-varint, eerste
 * vertex = knoop A). Headless las dit blok eerst niet — en dan meet de toets
 * iets anders dan de browser, precies wat dit bestand moet voorkomen: het
 * snoeien op dichtste nadering (M26.1) gebeurt op vertex-niveau, niet op
 * knoopniveau. `posities` is XYZ op de bolstraal, dezelfde afspraak als
 * marnet.js (z = -sin lon).
 */
function leesGeometrie(lezer, schaal, nEdges, geomN, edgeA, knoopLon, knoopLat, radius) {
  let nPunten = 0;
  for (let i = 0; i < nEdges; i++) nPunten += geomN[i];
  const geomStart = new Uint32Array(nEdges);
  const posities = new Float64Array(nPunten * 3);
  let pi = 0;
  for (let e = 0; e < nEdges; e++) {
    geomStart[e] = pi;
    let x = Math.round(knoopLon[edgeA[e]] * schaal);
    let y = Math.round(knoopLat[edgeA[e]] * schaal);
    for (let k = 0; k < geomN[e]; k++) {
      if (k > 0) { x += lezer.volgende(); y += lezer.volgende(); }
      const lon = (x / schaal) * Math.PI / 180, lat = (y / schaal) * Math.PI / 180;
      const c = Math.cos(lat);
      posities[pi * 3] = radius * c * Math.cos(lon);
      posities[pi * 3 + 1] = radius * Math.sin(lat);
      posities[pi * 3 + 2] = -radius * c * Math.sin(lon);
      pi++;
    }
  }
  return { geomStart, posities };
}

export function laadMarnetHeadless() {
  const meta = JSON.parse(readFileSync(bestand("marnet", "json"), "utf-8"));
  const lezer = maakLezer(readFileSync(bestand("marnet", "bin")));
  const { schaal, knopen: nKnopen, edges: nEdges } = meta;

  const knoopLon = new Float64Array(nKnopen), knoopLat = new Float64Array(nKnopen);
  let x = 0, y = 0;
  for (let i = 0; i < nKnopen; i++) {
    x += lezer.volgende(); y += lezer.volgende();
    knoopLon[i] = x / schaal; knoopLat[i] = y / schaal;
  }

  const edgeA = new Uint32Array(nEdges), edgeB = new Uint32Array(nEdges);
  const edgeKm = new Float32Array(nEdges), edgeSoort = new Uint8Array(nEdges);
  const geomN = new Uint32Array(nEdges);
  const edgeDiepgang = new Uint16Array(nEdges), edgeBreedte = new Uint16Array(nEdges);
  const edgeLengte = new Uint16Array(nEdges), edgeHoogte = new Uint16Array(nEdges);
  let a = 0, b = 0;
  for (let i = 0; i < nEdges; i++) {
    a += lezer.volgende(); b += lezer.volgende();
    edgeA[i] = a; edgeB[i] = b;
    edgeKm[i] = lezer.volgende() / 10;
    edgeSoort[i] = lezer.volgende();
    geomN[i] = lezer.volgende();
    if (lezer.volgende() === 1) {
      edgeDiepgang[i] = lezer.volgende(); edgeBreedte[i] = lezer.volgende();
      edgeLengte[i] = lezer.volgende(); edgeHoogte[i] = lezer.volgende();
    }
  }

  const geo = leesGeometrie(lezer, schaal, nEdges, geomN, edgeA, knoopLon, knoopLat, 2.4);

  const edgeLabel = new Array(nEdges).fill(null);
  for (const [ei, label] of Object.entries(meta.passages || {})) edgeLabel[Number(ei)] = label;

  return {
    ...bouwGraaf(nKnopen, nEdges, edgeA, edgeB),
    knoopLon, knoopLat, knoopXYZ: eenheidsXYZ(knoopLon, knoopLat),
    edgeA, edgeB, edgeKm, edgeSoort, edgeLabel, geomN, ...geo,
    edgeDiepgang, edgeBreedte, edgeLengte, edgeHoogte,
    vaarwegen: meta.vaarwegen || {}, passages: meta.passages || {},
    stats: { knopen: nKnopen, edges: nEdges },
  };
}

export function laadLandnetHeadless() {
  const meta = JSON.parse(readFileSync(bestand("landnet", "json"), "utf-8"));
  const lezer = maakLezer(readFileSync(bestand("landnet", "bin")));
  const { schaal, knopen: nKnopen, edges: nEdges } = meta;

  const knoopLon = new Float64Array(nKnopen), knoopLat = new Float64Array(nKnopen);
  let x = 0, y = 0;
  for (let i = 0; i < nKnopen; i++) {
    x += lezer.volgende(); y += lezer.volgende();
    knoopLon[i] = x / schaal; knoopLat[i] = y / schaal;
  }

  const edgeA = new Uint32Array(nEdges), edgeB = new Uint32Array(nEdges);
  const edgeKm = new Float32Array(nEdges), geomN = new Uint32Array(nEdges);
  let a = 0, b = 0;
  for (let i = 0; i < nEdges; i++) {
    a += lezer.volgende(); b += lezer.volgende();
    edgeA[i] = a; edgeB[i] = b;
    edgeKm[i] = lezer.volgende() / 10;
    lezer.volgende();              // soort
    geomN[i] = lezer.volgende();
    if (lezer.volgende() === 1) { lezer.volgende(); lezer.volgende(); lezer.volgende(); lezer.volgende(); }
  }

  const edgeModus = new Uint8Array(nEdges);
  const edgeLabel = new Array(nEdges).fill(null);
  for (const l of meta.labels || []) {
    const m = l.modus === "weg" ? 2 : 1;
    for (let e = l.edgeVan; e < Math.min(l.edgeTot, nEdges); e++) { edgeModus[e] = m; edgeLabel[e] = l.naam; }
  }

  const geo = leesGeometrie(lezer, schaal, nEdges, geomN, edgeA, knoopLon, knoopLat, 2.4);

  return {
    ...bouwGraaf(nKnopen, nEdges, edgeA, edgeB),
    knoopLon, knoopLat, knoopXYZ: eenheidsXYZ(knoopLon, knoopLat),
    edgeA, edgeB, edgeKm, edgeModus, edgeLabel, geomN, ...geo,
    meta,
    stats: { knopen: nKnopen, edges: nEdges },
  };
}

export function laadRegister() {
  return JSON.parse(readFileSync(join(DATA, "knooppunten.json"), "utf-8"));
}

/** De aansluitingen per grondstof (M26.1) — zie design/stroom-aansluiting.md. */
export function laadAansluitingen() {
  return JSON.parse(readFileSync(join(DATA, "aansluitingen.json"), "utf-8"));
}

/** De slurry-leidingen: tekengeometrie voor de benen zonder net (mag ontbreken). */
export function laadPijpleidingen() {
  try {
    return JSON.parse(readFileSync(join(DATA, "pijpleidingen.json"), "utf-8"));
  } catch {
    return null;
  }
}

/** De pilot-stromen: welke aansluitingen in welke volgorde, modus per been. */
export function laadStromenData() {
  return JSON.parse(readFileSync(join(DATA, "stromen-pilot.json"), "utf-8"));
}

export function laadHavens() {
  const d = JSON.parse(readFileSync(bestand("ports", "json"), "utf-8"));
  const havens = [];
  for (let i = 0; i < d.aantal; i++) {
    havens.push({
      naam: d.namen[i], land: d.landen[i], locode: d.locodes[i],
      lon: d.ll[i * 2], lat: d.ll[i * 2 + 1],
      knoop: d.knoop[i], afstandKm: d.afstandKm[i],
      knoopRivier: d.knoopRivier ? d.knoopRivier[i] : -1,
      afstandRivierKm: d.afstandRivierKm ? d.afstandRivierKm[i] : -1,
    });
  }
  havens.zeeKnopen = d.zeeKnopen ?? null;
  return havens;
}
