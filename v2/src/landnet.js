// landnet.js — het LANDNET (spoor, straks weg) als eigen laag op de bol.
//
// M25 / [LAR-491]. Waarom een eigen module en een eigen bestand naast
// `marnet.bin`: de haven-bake slicet de knopenlijst van marnet hard in tweeën op
// `zeeKnopen` en telt élke knoop daarboven als water. Spoor ligt in élke haven
// dichter bij dan de dichtstbijzijnde zeeknoop, dus landknopen in diezelfde
// lijst zouden betekenen dat elke haven op een spoorknoop snapt. Het landnet
// leeft daarom in `landnet.bin` met LOKALE knoop-ids; de koppeling aan de
// andere netten gebeurt straks via aangewezen knooppunten, niet via een edge.
//
// Formaat is letterlijk dat van marnet.bin (drie varint-blokken) zodat dezelfde
// lezer werkt — zie bake_landnet.py voor de schrijfkant.

import * as THREE from "three";

// Spoor: koel staalgroen. Bewust NIET gedempt — de bulklaag-les van [LAR-515]
// kostte een ronde doordat een subtiele kleur op de satellietskin onzichtbaar
// bleek. Hogesnelheid en breedspoor krijgen een eigen tint zodat het net leesbaar
// blijft zonder een tweede laag: de kleur is een EIGENSCHAP van de lijn.
const KLEUR_SPOOR = new THREE.Color(0x5fe8c8);
const KLEUR_SPOOR_HS = new THREE.Color(0xa6f0ff);   // hogesnelheid
const KLEUR_BREED = new THREE.Color(0xffb877);      // 1520 mm (Rusland/CIS)
const KLEUR_SMAL = new THREE.Color(0xc9a6ff);       // < 1435 mm
const KLEUR_WEG = new THREE.Color(0xff9d3d);

/** Zelfde zigzag-varint-lezer als marnet.js — bewust gekopieerd en niet
 *  geïmporteerd: een import van marnet.js?v=… laadt die module dubbel zodra de
 *  twee versienummers uiteenlopen. Zonder bit-operatoren, want die knippen op
 *  32 bits terwijl vermenigvuldigen tot 2^53 exact blijft. */
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
      const half = Math.floor(res / 2);
      return res % 2 === 0 ? half : -half - 1;
    },
  };
}

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/marnet.js — een 90°-fout oogt
  // onderling perfect maar ligt los van de bol.
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const cosLat = Math.cos(lat);
  uit[o + 0] = r * cosLat * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * cosLat * Math.sin(lon);
}

function kleurVoor(label) {
  if (label.startsWith("weg")) return KLEUR_WEG;
  if (label.endsWith("-hs")) return KLEUR_SPOOR_HS;
  const m = /-(\d+)(?:\+|-|$)/.exec(label);
  const gauge = m ? parseInt(m[1], 10) : 0;
  if (gauge >= 1520) return KLEUR_BREED;
  if (gauge && gauge < 1435) return KLEUR_SMAL;
  return KLEUR_SPOOR;
}

/**
 * Laadt landnet.bin/json en bouwt er één LineSegments van — één draw call voor
 * het hele landnet, kleur per lijn via vertex colors.
 */
export async function laadLandnet(radius, versie = "052", klemOpHorizon = null) {
  const t0 = performance.now();
  const [meta, buffer] = await Promise.all([
    fetch(`data/landnet.json?v=${versie}`).then((r) => {
      if (!r.ok) throw new Error(`landnet.json: HTTP ${r.status}`);
      return r.json();
    }),
    fetch(`data/landnet.bin?v=${versie}`).then((r) => {
      if (!r.ok) throw new Error(`landnet.bin: HTTP ${r.status}`);
      return r.arrayBuffer();
    }),
  ]);
  const tGeladen = performance.now();

  const lezer = maakLezer(new Uint8Array(buffer));
  const schaal = meta.schaal;
  const nKnopen = meta.knopen;
  const nEdges = meta.edges;
  const nPunten = meta.punten;

  // --- blok 1: knopen -------------------------------------------------------
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

  // --- blok 2: edges --------------------------------------------------------
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
      if (lezer.volgende() === 1) {
        lezer.volgende(); lezer.volgende(); lezer.volgende(); lezer.volgende();
      }
    }
  }

  // Label per edge uit de ranges in landnet.json — géén string per edge in het
  // bestand: dat kost bij ~160k edges megabytes JSON voor nul extra informatie.
  const edgeKleur = new Array(nEdges);
  for (const l of meta.labels || []) {
    const k = kleurVoor(l.naam);
    for (let e = l.edgeVan; e < l.edgeTot && e < nEdges; e++) edgeKleur[e] = k;
  }

  // --- blok 3: geometrie ----------------------------------------------------
  const posities = new Float32Array(nPunten * 3);
  const kleuren = new Float32Array(nPunten * 3);
  let nSegmenten = 0;
  for (let i = 0; i < nEdges; i++) nSegmenten += geomN[i] - 1;
  const indices = new Uint32Array(nSegmenten * 2);
  {
    let pi = 0, ii = 0;
    for (let e = 0; e < nEdges; e++) {
      const kleur = edgeKleur[e] || KLEUR_SPOOR;
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
    opacity: 0.75,
    depthWrite: false,
  });
  if (klemOpHorizon) klemOpHorizon(mat);
  const lijnen = new THREE.LineSegments(geo, mat);
  // ⚠️ BOVEN DE TEGELS (die staan op 1 · 2 · 3) EN MET DE HORIZONTOETS, anders dekt de
  // bol deze laag volledig af zodra de tegels geladen zijn — gemeten: 0 pixels.
  // Zie `klemOpHorizon` in globe.js voor het waarom.
  lijnen.renderOrder = 7;      // tegels 1-3 · kust 6 · zeenet 6,5 · landnet 7 · route 8 · havens 9
  lijnen.frustumCulled = false;

  const kmPerSoort = {};
  for (const l of meta.labels || []) {
    kmPerSoort[l.modus] = (kmPerSoort[l.modus] || 0) + (l.km || 0);
  }

  return {
    lijnen,
    meta,
    stats: {
      knopen: nKnopen,
      edges: nEdges,
      punten: nPunten,
      labels: (meta.labels || []).length,
      netwerkKm: meta.netwerkKm,
      kmPerSoort,
      kbOverdracht: Math.round(buffer.byteLength / 1024),
      msLaden: Math.round(tGeladen - t0),
      msVerwerken: Math.round(performance.now() - tGeladen),
    },
  };
}
