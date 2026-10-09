// stroombundel.js — DE STROMENBUNDEL op de bol: alle 182 gemeten ketens uit
// één afgeleid bundelbestand, met twee gebakken LOD-niveaus en een lui geladen
// fijn-niveau, getekend als een handvol objecten. (Golf 1 van de visuele fase,
// 2026-10-08, LAR-617; ontwerp in v2/design/atlas-product-golf1.md.)
//
// Vervangt het trio van tot ?v=131: de oude exacte-lijnlaag (lijn per been),
// de oude draad-en-kometenlaag (draad + kometen per been) en de gloedknopen-lus
// in main.js. Die drie leefden nog achter `?laag=los` als pariteitsreferentie
// en zijn in stap 4 van golf 1 verwijderd.
//
// WAAROM (gemeten, ?v=131): 382 verzoeken / 51,7 MB (elk stroombestand twee
// keer gefetcht), ~2.300 objecten en 12,7 M driehoeken, telefoon 9–14 fps. De
// oorzaak zat niet in de hoeveelheid data maar in de VORM: één object per been
// per laag, en 813.000 truckpunten op meters-korrel die op wereldhoogte een
// paar honderd pixels beslaan.
//
// WAT ER NU STAAT (alles aan, atlasmodus):
//   lijnen-L0 / lijnen-L1   één LineSegments2 per niveau, alle grondbenen van
//                           alle stromen, stippel inbegrepen (precies één
//                           zichtbaar; de keuze volgt uit kijkhoogte en
//                           schermhoogte, niet uit vaste kilometers)
//   lijnen-fijn             één LineSegments2 met vooraf gealloceerde buffer,
//                           gevuld uit de benen IN BEELD op volle resolutie
//                           (de fijne bundel per grondstof wordt lui gehaald en
//                           blijft resident — alles samen is 3,2 MB)
//   lijnen-lucht            de 38 luchtbenen als boog uit beenPunten(), in elke
//                           lijnmodus (een vlucht ligt echt in de lucht)
//   lijnen-<hemelsbreed>    lui, alleen in die lijnmodus
//   kometen · gloed · precisiestippen   elk één Points
// Aan/uit per stroom, kleurmodus en LOD-rol lopen via de informatietexturen
// van stroomlijn.js: een klik herschrijft texels, er wordt niets herbouwd.
//
// WAT ONGEWIJZIGD IS (de besluiten van Lars): de gemeten routes blijven op de
// grond (alleen lucht en de drie hemelsbreed-modi boogen), stippel betekent
// uitsluitend "hier reikt het net niet" en krijgt geen kometen, kleur =
// grondstof in de atlas en = modaliteit in het routewerk (stroomstijl.js is
// de enige bron), de gloed telt additief op met het pixel-minimum als
// mechanisme, de komeet is bijna wit met een staart als fractie van het been.
//
// ⚠️ DE BAKE-VERSIE (`bundelVersie`) STAAT LOS VAN DE CODE-`?v=`: bump hem alleen
// bij een echte herbundel (bak_stromen.sh bundel), zoals landnet "102".

import * as THREE from "three";
import {
  kleurVan, beenPunten, GRONDSTOF_KLEUR, stijlIndex, LIJNMODI,
} from "./stroomstijl.js?v=132";
import {
  BeenInfo, maakLijnMateriaal, zetLijnSchaal, zetKmPerPx, zetPatronenAan, maakSegmentGeometrie, bouwLijn,
  ROL_BASIS, ROL_FIJN, ROL_ALTIJD,
} from "./stroomlijn.js?v=132";
import { bouwGloed } from "./gloed.js?v=132";
import { bouwKometen } from "./stroomkometen.js?v=132";

const AARDSTRAAL_KM = 6371;
const D2R = Math.PI / 180;

/** Hoeveel segmenten het fijn-object hooguit tegelijk tekent. Bij < 260 km
 *  hoogte is het venster hooguit ~200 × 100 km → hooguit enkele tienduizenden
 *  segmenten; past het niet, dan blijven de overige benen op L1 en zegt de
 *  console dat luid. 200.000 × 6 floats = 4,8 MB posities. */
export const FIJN_MAX = 200000;

/** De LOD-regel: een niveau is toelaatbaar zolang zijn tolerantie ≤ 1 css-px.
 *  kmPerCssPx = 2·h·tan(fov/2) / H — dus uit kijkhoogte én schermhoogte, nooit
 *  als vaste kilometers in de code (een telefoon van 844 css-px wisselt dan op
 *  een andere hoogte dan een desktop van 1000, en dat hoort zo). */
export const LOD = {
  L0TolKm: 3.0,          // uit de bake (stromen.json → niveaus.L0.tolKm)
  L1TolKm: 0.2,
  hysterese: 1.2,        // terug naar grover pas boven 1,2 × de grens: geen flikkeren
  prefetchFactor: 1.5,   // fijne bundels alvast halen vlak boven de L1/fijn-grens
  herzienMs: 250,        // hoe vaak de benen-in-beeld opnieuw bepaald worden
  marge: 1.15,           // venster 15 % ruimer dan het scherm
};

// Gewicht van een stroomknoop — EEN HEURISTIEK, GEEN METING (een marker draagt
// alleen naam/lon/lat): uiteinden (de mijn, de eindfabriek) zwaarder dan een
// overslagpunt. Zodra het metadatabestand volume per been draagt hoort dit
// dáár uit te komen. Letterlijk de waarden van de oude exacte-lijnlaag (?v=119).
const KNOOPGLOED = { uiteindeKm: 3.4, uiteindeHelder: 0.90, overslagKm: 2.2, overslagHelder: 0.62 };
// Sites: straal en helderheid uit het gewicht, genormaliseerd PER GRONDSTOF
// (de oude gloedknopenlaag, 2026-09-26): koper verandert niet als er een
// grondstof met grotere getallen bijkomt (kolen in Mt/j).
const SITEGLOED = { kmPerWortelGewicht: 0.30 };
const KLEUR_ONBEKEND = 0xbfbfbf;

// De witte precisiestip van het routewerk (bouwmodus): kern + ring, exact de
// shader van de oude exacte-lijnlaag — een additieve gloed is aan de rand per
// definitie onnauwkeurig, en tijdens het routewerk is de vraag "ligt dit punt
// op de goede kade?".
const VERT_STIP = `
attribute float grootte;
void main() {
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  gl_PointSize = grootte;
}`;
const FRAG_STIP = `
precision highp float;
uniform float alfa;
void main() {
  vec2 p = gl_PointCoord - vec2(0.5);
  float d = length(p) * 2.0;
  if (d > 1.0) discard;
  float kern = 1.0 - smoothstep(0.10, 0.30, d);
  float halo = exp(-3.2 * d * d) * 0.42;
  float ring = smoothstep(0.62, 0.74, d) * (1.0 - smoothstep(0.80, 0.94, d)) * 0.55;
  gl_FragColor = vec4(vec3(1.0), clamp(kern + halo + ring, 0.0, 1.0) * alfa);
}`;
const STIP = { minPx: 9.0, maxPx: 44.0, wereldKm: 26.0 };

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/aistracks.js (z = −sin lon).
  const lon = lonDeg * D2R, lat = latDeg * D2R;
  const c = Math.cos(lat);
  uit[o] = r * c * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * c * Math.sin(lon);
}

function gcKm(a, b) {
  const la1 = a[1] * D2R, la2 = b[1] * D2R, dLo = (b[0] - a[0]) * D2R;
  const s = Math.sin((la2 - la1) / 2) ** 2 + Math.cos(la1) * Math.cos(la2) * Math.sin(dLo / 2) ** 2;
  return 2 * AARDSTRAAL_KM * Math.asin(Math.min(1, Math.sqrt(s)));
}

// Zelfde zigzag-varint-lezer als landnet.js — bewust gekopieerd, niet
// geïmporteerd (een import van landnet.js?v=… laadt die module dubbel zodra de
// versienummers uiteenlopen). Zonder bit-operatoren: die knippen op 32 bits.
function maakLezer(bytes, p = 0) {
  return {
    get p() { return p; },
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

/** Decodeer één blok (basis-niveau of fijn-bundel) voor een lijst benen in
 *  bundelvolgorde. `metKm`: het blok draagt per punt een Δkm-kolom (basis);
 *  anders telt de lezer de koordelengte op (fijn). Geeft per been
 *  {xyz, km, kop, staart}. */
function decodeerBlok(bytes, benen, radius, schaal, kmSchaal, metKm) {
  const lezer = maakLezer(bytes);
  const uit = new Array(benen.length);
  const kmPerEenheid = AARDSTRAAL_KM / radius;
  for (let bi = 0; bi < benen.length; bi++) {
    const n = lezer.volgende();
    const xyz = new Float32Array(n * 3);
    const km = new Float32Array(n);
    let qx = 0, qy = 0, qk = 0, lon0 = 0, lat0 = 0, lonN = 0, latN = 0;
    for (let i = 0; i < n; i++) {
      qx += lezer.volgende(); qy += lezer.volgende();
      const lon = qx / schaal, lat = qy / schaal;
      if (i === 0) { lon0 = lon; lat0 = lat; }
      lonN = lon; latN = lat;
      opBol(lon, lat, radius, xyz, i * 3);
      if (metKm) {
        qk += lezer.volgende();
        km[i] = qk / kmSchaal;
      } else if (i > 0) {
        const o = i * 3;
        km[i] = km[i - 1] + Math.hypot(xyz[o] - xyz[o - 3], xyz[o + 1] - xyz[o - 2], xyz[o + 2] - xyz[o - 1]) * kmPerEenheid;
      }
    }
    uit[bi] = { xyz, km, kop: [lon0, lat0], staart: [lonN, latN], n };
  }
  if (lezer.p !== bytes.length) {
    throw new Error(`stroombundel: blok niet volledig gelezen (${lezer.p} van ${bytes.length} bytes) — formaat ≠ bake`);
  }
  return uit;
}

/** Schrijf de segmenten van een puntenreeks in een segmentgeometrie vanaf
 *  segment `s0`; geeft het nieuwe aantal. Afstand = km per vertex. */
function schrijfSegmenten(sg, s0, xyz, km, beenIndex, max) {
  const n = km.length;
  let s = s0;
  for (let i = 0; i + 1 < n && s < max; i++, s++) {
    const o6 = s * 6, o3 = i * 3;
    sg.pos[o6] = xyz[o3]; sg.pos[o6 + 1] = xyz[o3 + 1]; sg.pos[o6 + 2] = xyz[o3 + 2];
    sg.pos[o6 + 3] = xyz[o3 + 3]; sg.pos[o6 + 4] = xyz[o3 + 4]; sg.pos[o6 + 5] = xyz[o3 + 5];
    sg.been[s] = beenIndex;
    sg.afstand[s * 2] = km[i]; sg.afstand[s * 2 + 1] = km[i + 1];
  }
  return s;
}

/** Punten uit beenPunten() ([lon,lat,straalfactor]) → xyz + cumulatieve km. */
function puntenNaarXyz(punten, radius) {
  const xyz = new Float32Array(punten.length * 3);
  const km = new Float32Array(punten.length);
  for (let i = 0; i < punten.length; i++) {
    opBol(punten[i][0], punten[i][1], radius * punten[i][2], xyz, i * 3);
    if (i > 0) km[i] = km[i - 1] + gcKm(punten[i - 1], punten[i]);
  }
  return { xyz, km };
}

/**
 * @param opts.radius        schil van de lijnen (CONFIG.radius × vectorLift)
 * @param opts.codeVersie    ?v= van de code (voor het register)
 * @param opts.bundelVersie  ?v= van de bundel (stromen.json + bins)
 * @param opts.klemOpHorizon GLOBE.klemOpHorizon
 * @param opts.camera / opts.renderer / opts.globeGroup
 * @param opts.getAltitudeKm GLOBE.getAltitudeKm
 * @param opts.telefoon      bool (kometen K)
 * @param opts.kleurModus / opts.lijnModus  startstanden
 * @param opts.bijLaden      callback({geladen, stromen}) voor de HUD
 */
export async function laadStroombundel(opts) {
  const { radius, codeVersie, bundelVersie, klemOpHorizon, camera, renderer, globeGroup, getAltitudeKm } = opts;
  const telefoon = !!opts.telefoon;
  let kleurModus = opts.kleurModus || "grondstof";
  let lijnModus = opts.lijnModus || "route";
  let gloedAan = opts.gloedAan !== false;
  let bewegingAan = opts.bewegingAan !== false;

  const t0 = performance.now();
  const haal = async (bestand, versie, binair) => {
    const r = await fetch(`data/${bestand}?v=${versie}`);
    if (!r.ok) throw new Error(`${bestand}: HTTP ${r.status}`);
    return binair ? new Uint8Array(await r.arrayBuffer()) : r.json();
  };
  const [register, index, basisBytes] = await Promise.all([
    haal("stromen-register.json", codeVersie, false),
    haal("stromen.json", bundelVersie, false),
    haal("stromen-basis.bin", bundelVersie, true),
  ]);
  const tLaden = performance.now();
  if (index.formaat !== 1) throw new Error(`stromen.json: onbekend formaat ${index.formaat}`);
  if (register.stromen.length !== index.stromen.length ||
      register.stromen.some((s, i) => s.sleutel !== index.stromen[i].sleutel)) {
    throw new Error("stromen-register.json en stromen.json lopen uiteen — draai `bash v2/tools/bak_stromen.sh bundel`");
  }
  const { schaal, kmSchaal } = index.codering;
  // De LOD-toleranties komen uit de bundel zelf (de baker schrijft ze in
  // niveaus.*.tolKm); de constanten in LOD zijn alleen de terugval.
  const tolL0 = index.niveaus?.L0?.tolKm ?? LOD.L0TolKm;
  const tolL1 = index.niveaus?.L1?.tolKm ?? LOD.L1TolKm;

  // ── de benen, plat over alle stromen (globale beenindex = textuur-index) ──
  const stromen = index.stromen.map((s, si) => ({
    ...s, registratie: register.stromen[si],
    label: register.stromen[si].label || s.titel || s.sleutel,
  }));
  const benen = [];
  for (const s of stromen) {
    for (const b of s.benen) {
      if (b.i !== benen.length) throw new Error(`stromen.json: beenindex ${b.i} ≠ positie ${benen.length}`);
      benen.push({
        ...b, sleutel: s.sleutel, stroom: s.stroom, grondstof: s.grondstof,
        lucht: b.L0 === null, L0: null, L1: null, fijn: null, baan: "L1",
      });
    }
  }
  const grondBenen = benen.filter((b) => !b.lucht);
  // Een been zonder geometrie én zonder kop/staart kan niets tekenen: overslaan
  // (luid in de console), niet de hele bundel laten vallen op een null.
  const luchtBenen = benen.filter((b) => b.lucht && Array.isArray(b.kopStaart) && b.kopStaart.length === 2);
  for (const b of benen) if (b.lucht && !luchtBenen.includes(b)) console.warn(`[atlas v2] been ${b.i} (${b.sleutel}) heeft geen geometrie en geen kop/staart — overgeslagen`);

  // ── decoderen van de twee basisniveaus ───────────────────────────────────
  for (const naam of ["L0", "L1"]) {
    const nv = index.niveaus[naam];
    const blok = basisBytes.subarray(nv.byteVan, nv.byteTot);
    const dec = decodeerBlok(blok, grondBenen, radius, schaal, kmSchaal, true);
    grondBenen.forEach((b, i) => { b[naam] = dec[i]; });
  }
  for (const b of grondBenen) { b.kop = b.L0.kop; b.staart = b.L0.staart; }
  for (const b of luchtBenen) { b.kop = b.kopStaart[0]; b.staart = b.kopStaart[1]; }
  // de benen die in een hemelsbreed-object horen: alles met een kop en staart
  // behalve lucht — dat heeft zijn eigen object (dezelfde boog in elke modus)
  const hemelsbreedBenen = [...grondBenen, ...[]];
  const tDecode = performance.now();

  // ── de informatietexturen ────────────────────────────────────────────────
  const info = new BeenInfo(benen.length);
  const stroomAan = new Map(stromen.map((s) => [s.sleutel, s.registratie.aan !== false]));
  const stroomVan = new Map(stromen.map((s) => [s.sleutel, s]));
  const benenVanStroom = new Map(stromen.map((s) => [s.sleutel, benen.filter((b) => b.sleutel === s.sleutel)]));
  const grondstoffen = [...new Set(stromen.map((s) => s.grondstof))];
  const stromenVanGrondstof = new Map(grondstoffen.map((g) => [g, stromen.filter((s) => s.grondstof === g)]));
  for (const b of benen) info.zetStijl(b.i, stijlIndex(b.modaliteit, b.stippel));

  // ── de lijnobjecten ──────────────────────────────────────────────────────
  const groep = new THREE.Group();
  groep.name = "stroombundel";
  const matBasis = maakLijnMateriaal(info, ROL_BASIS, klemOpHorizon);
  const matFijn = maakLijnMateriaal(info, ROL_FIJN, klemOpHorizon);
  const matAltijd = maakLijnMateriaal(info, ROL_ALTIJD, klemOpHorizon);
  const materialen = [matBasis, matFijn, matAltijd];

  function bouwNiveau(naam) {
    const nSeg = grondBenen.reduce((s, b) => s + Math.max(0, b[naam].n - 1), 0);
    const sg = maakSegmentGeometrie(nSeg);
    let s = 0;
    for (const b of grondBenen) s = schrijfSegmenten(sg, s, b[naam].xyz, b[naam].km, b.i, nSeg);
    sg.zetAantal(s);
    sg.markeerBijgewerkt(s);
    return { sg, lijn: bouwLijn(sg, matBasis, 7.5, `lijnen-${naam}`), segmenten: s };
  }
  const L0 = bouwNiveau("L0");
  const L1 = bouwNiveau("L1");
  groep.add(L0.lijn, L1.lijn);

  // fijn: één object, vooraf gealloceerd, gevuld uit de benen in beeld
  const fijnSg = maakSegmentGeometrie(FIJN_MAX, true);
  const fijnLijn = bouwLijn(fijnSg, matFijn, 7.5, "lijnen-fijn");
  fijnLijn.visible = false;
  groep.add(fijnLijn);

  // lucht: de 38 bogen uit beenPunten(), in elke lijnmodus (ook "route")
  const luchtBaan = new Map();   // beenindex → {xyz, km}
  const luchtSg = (() => {
    const reeksen = luchtBenen.map((b) => puntenNaarXyz(beenPunten({ punten: b.kopStaart, modaliteit: "lucht" }, "route"), radius));
    const nSeg = reeksen.reduce((s, r) => s + Math.max(0, r.km.length - 1), 0);
    const sg = maakSegmentGeometrie(nSeg);
    let s = 0;
    luchtBenen.forEach((b, i) => {
      luchtBaan.set(b.i, reeksen[i]);
      s = schrijfSegmenten(sg, s, reeksen[i].xyz, reeksen[i].km, b.i, nSeg);
    });
    sg.zetAantal(s); sg.markeerBijgewerkt(s);
    return sg;
  })();
  const luchtLijn = bouwLijn(luchtSg, matAltijd, 7.5, "lijnen-lucht");
  groep.add(luchtLijn);

  // hemelsbreed-modi: lui, één object per modus, alle grondbenen kop → staart
  // (lucht niet: dat staat al in lijnen-lucht, en boogt in elke modus hetzelfde —
  // anders tekent een luchtbeen in deze modi dubbel; review 2026-10-08)
  const hemelsbreed = new Map();  // modus → {lijn, banen: Map(beenindex → {xyz, km})}
  function bouwHemelsbreed(modus) {
    if (hemelsbreed.has(modus)) return hemelsbreed.get(modus);
    const reeksen = hemelsbreedBenen.map((b) => puntenNaarXyz(beenPunten({ punten: [b.kop, b.staart], modaliteit: b.modaliteit }, modus), radius));
    const nSeg = reeksen.reduce((s, r) => s + Math.max(0, r.km.length - 1), 0);
    const sg = maakSegmentGeometrie(nSeg);
    const banen = new Map();
    let s = 0;
    hemelsbreedBenen.forEach((b, i) => { banen.set(b.i, reeksen[i]); s = schrijfSegmenten(sg, s, reeksen[i].xyz, reeksen[i].km, b.i, nSeg); });
    sg.zetAantal(s); sg.markeerBijgewerkt(s);
    const lijn = bouwLijn(sg, matAltijd, 7.5, `lijnen-${modus}`);
    lijn.visible = false;
    groep.add(lijn);
    const h = { lijn, banen };
    hemelsbreed.set(modus, h);
    return h;
  }

  // ── kometen ──────────────────────────────────────────────────────────────
  const dragers = benen.filter((b) => !b.stippel).map((b) => ({ been: b.i, modaliteit: b.modaliteit }));
  const kometen = bouwKometen(dragers, radius, (i) => info.isAan(i), telefoon, 7.55);
  groep.add(kometen.groep);
  function zetBaanRoute(b) {
    // de getekende geometrie: fijn waar fijn getekend wordt, anders L1; lucht zijn boog
    if (b.lucht) { const r = luchtBaan.get(b.i); kometen.zetBaan(b.i, r.xyz, r.km); return; }
    const bron = (b.baan === "fijn" && b.fijn) ? b.fijn : b.L1;
    kometen.zetBaan(b.i, bron.xyz, bron.km);
  }
  function zetAlleBanen() {
    if (lijnModus === "route") { for (const b of benen) zetBaanRoute(b); return; }
    const h = bouwHemelsbreed(lijnModus);
    for (const b of benen) {
      const r = h.banen.get(b.i);
      if (r) kometen.zetBaan(b.i, r.xyz, r.km);
      else zetBaanRoute(b);              // lucht: zijn eigen boog
    }
  }
  zetAlleBanen();

  // ── gloed: sites + stroomknopen in één object ────────────────────────────
  const gloedKnopen = [];
  const siteIdx = new Map(grondstoffen.map((g) => [g, []]));
  const maxGewicht = new Map();
  for (const s of index.sites) maxGewicht.set(s.grondstof, Math.max(maxGewicht.get(s.grondstof) || 1, s.gewicht || 1));
  for (const s of index.sites) {
    const g = Math.max(1, s.gewicht || 1);
    (siteIdx.get(s.grondstof) || siteIdx.set(s.grondstof, []).get(s.grondstof)).push(gloedKnopen.length);
    gloedKnopen.push({
      lon: s.lon, lat: s.lat, straalKm: SITEGLOED.kmPerWortelGewicht * Math.sqrt(g),
      kleur: GRONDSTOF_KLEUR[s.grondstof] ?? KLEUR_ONBEKEND,
      // capaciteit is het gewicht in de optelling: stuurt wereldmaat én helderheid
      helder: 0.28 + 0.72 * Math.sqrt(g / maxGewicht.get(s.grondstof)),
    });
  }
  const knoopIdx = new Map();     // sleutel → [gloedindex]
  const stipPos = [];             // precisiestippen: alle markers
  const stipStroom = [];
  for (const s of stromen) {
    const lijst = [];
    s.markers.forEach((m, mi) => {
      const uiteinde = (mi === 0 || mi === s.markers.length - 1);
      lijst.push(gloedKnopen.length);
      gloedKnopen.push({
        lon: m.lon, lat: m.lat, kleur: GRONDSTOF_KLEUR[s.grondstof] ?? KLEUR_ONBEKEND,
        straalKm: uiteinde ? KNOOPGLOED.uiteindeKm : KNOOPGLOED.overslagKm,
        helder: uiteinde ? KNOOPGLOED.uiteindeHelder : KNOOPGLOED.overslagHelder,
      });
      stipPos.push(m.lon, m.lat);
      stipStroom.push(s.sleutel);
    });
    knoopIdx.set(s.sleutel, lijst);
  }
  const gloed = bouwGloed(gloedKnopen, radius, 7.6);
  groep.add(gloed.groep);

  // ── precisiestippen (bouwmodus) ──────────────────────────────────────────
  const nStip = stipPos.length / 2;
  const stipXyz = new Float32Array(nStip * 3);
  for (let i = 0; i < nStip; i++) opBol(stipPos[i * 2], stipPos[i * 2 + 1], radius, stipXyz, i * 3);
  const stipGrootte = new Float32Array(nStip);
  const stipGeo = new THREE.BufferGeometry();
  stipGeo.setAttribute("position", new THREE.BufferAttribute(stipXyz, 3));
  const stipAttrGr = new THREE.BufferAttribute(stipGrootte, 1);
  stipAttrGr.setUsage(THREE.DynamicDrawUsage);
  stipGeo.setAttribute("grootte", stipAttrGr);
  stipGeo.boundingSphere = new THREE.Sphere(new THREE.Vector3(), radius * 2);
  const stipMat = new THREE.ShaderMaterial({
    vertexShader: VERT_STIP, fragmentShader: FRAG_STIP, uniforms: { alfa: { value: 0.95 } },
    blending: THREE.NormalBlending, transparent: true, depthTest: false, depthWrite: false,
  });
  const stippen = new THREE.Points(stipGeo, stipMat);
  stippen.renderOrder = 7.6;
  stippen.frustumCulled = false;
  stippen.name = "precisiestippen";
  groep.add(stippen);

  // ── toestand → texturen en gloed ─────────────────────────────────────────
  const gsAan = (g) => (stromenVanGrondstof.get(g) || []).some((s) => stroomAan.get(s.sleutel));
  function pasAanToe() {
    const atlas = kleurModus === "grondstof";
    for (const b of benen) info.zetAan(b.i, !!stroomAan.get(b.sleutel));
    for (const g of grondstoffen) {
      const aan = gloedAan && gsAan(g);
      for (const i of siteIdx.get(g) || []) gloed.zetAan(i, aan);
    }
    for (const s of stromen) {
      const aan = gloedAan && atlas && !!stroomAan.get(s.sleutel);
      for (const i of knoopIdx.get(s.sleutel)) gloed.zetAan(i, aan);
    }
    stippen.visible = !atlas;
    info.commit();
  }
  function pasKleurToe() {
    for (const b of benen) {
      const hex = kleurVan(b.modaliteit, b.stroom, kleurModus);
      info.zetKleur(b.i, hex);
      kometen.zetKleur(b.i, hex);
    }
    kometen.commitKleur();
    info.commit();
    zetPatronenAan(materialen, kleurModus === "grondstof");
  }
  pasKleurToe();
  pasAanToe();

  // ── LOD en het fijn-niveau ───────────────────────────────────────────────
  let niveau = 0;                 // 0 = L0 · 1 = L1 · 2 = fijn-geschikt
  const fijnResident = new Map(); // grondstof → "laden" | "klaar" | "mislukt"
  let fijnSleutel = "";           // de set benen in beeld van de laatste vulling
  let fijnSegmenten = 0;
  let fijnOverloopGemeld = false;
  let laatsteHerzien = -1e9;
  let bundelBinnen = false;
  const camLocaal = new THREE.Vector3();
  const inv = new THREE.Matrix4();
  let kmPerCssPx = 1;

  async function haalFijn(gs) {
    if (fijnResident.has(gs)) return;
    fijnResident.set(gs, "laden");
    try {
      const f = index.fijn[gs];
      if (!f) throw new Error(`geen fijne bundel voor ${gs}`);
      const bytes = await haal(f.bestand, bundelVersie, true);
      const lijst = grondBenen.filter((b) => b.grondstof === gs);
      const dec = decodeerBlok(bytes, lijst, radius, schaal, kmSchaal, false);
      lijst.forEach((b, i) => { b.fijn = dec[i]; });
      fijnResident.set(gs, "klaar");
      bundelBinnen = true;
      console.log(`[atlas v2] fijne bundel ${gs}: ${lijst.length} benen · ${f.punten.toLocaleString("nl")} punten · ${Math.round(f.bytes / 1024)} KB`);
    } catch (e) {
      fijnResident.set(gs, "mislukt");
      console.warn(`[atlas v2] fijne bundel ${gs} niet geladen:`, e.message);
    }
  }

  // bbox-toets op een lon/lat-venster; de bbox is in ONTWIKKELDE lon (kan
  // buiten ±180 liggen), dus toets op de drie takken −360/0/+360
  function inBeeld(bbox, lonC, latC, dLon, dLat) {
    if (!bbox) return false;
    if (bbox[3] < latC - dLat || bbox[1] > latC + dLat) return false;
    for (const sh of [-360, 0, 360]) {
      if (bbox[0] + sh <= lonC + dLon && bbox[2] + sh >= lonC - dLon) return true;
    }
    return false;
  }

  function herzieFijn(h, aspect, nu) {
    // het venster rond het punt onder de camera
    const p = camLocaal.clone().normalize();
    const latC = Math.asin(Math.max(-1, Math.min(1, p.y))) / D2R;
    const lonC = Math.atan2(-p.z, p.x) / D2R;
    const halfH = h * Math.tan((camera.fov * D2R) / 2) * LOD.marge;
    const halfW = halfH * aspect;
    const dLat = halfH / 111.195;
    const dLon = Math.min(180, halfW / (111.195 * Math.max(0.05, Math.cos(latC * D2R))));
    const inzicht = grondBenen.filter((b) => inBeeld(b.bbox, lonC, latC, dLon, dLat));
    // bundels halen voor de grondstoffen in beeld (resident, geen LRU)
    for (const g of new Set(inzicht.map((b) => b.grondstof))) haalFijn(g);
    const sleutel = inzicht.map((b) => b.i).join(",");
    if (sleutel === fijnSleutel && !bundelBinnen) return;
    fijnSleutel = sleutel;
    bundelBinnen = false;
    // vullen: alleen benen met residente fijne geometrie; de rest blijft L1
    let s = 0;
    const metFijn = new Set();
    let overloop = false;
    for (const b of inzicht) {
      if (!b.fijn) continue;
      const nodig = b.fijn.n - 1;
      if (s + nodig > FIJN_MAX) { overloop = true; continue; }
      s = schrijfSegmenten(fijnSg, s, b.fijn.xyz, b.fijn.km, b.i, FIJN_MAX);
      metFijn.add(b.i);
    }
    fijnSg.zetAantal(s);
    fijnSg.markeerBijgewerkt(s);
    fijnSegmenten = s;
    if (overloop && !fijnOverloopGemeld) {
      fijnOverloopGemeld = true;
      console.warn(`[atlas v2] fijn-overloop: meer dan ${FIJN_MAX.toLocaleString("nl")} segmenten in beeld — de rest blijft op L1`);
    }
    for (const b of grondBenen) {
      const fijn = metFijn.has(b.i);
      info.zetFijn(b.i, fijn);
      const baan = fijn ? "fijn" : "L1";
      if (baan !== b.baan) { b.baan = baan; if (lijnModus === "route") zetBaanRoute(b); }
    }
    info.commit();
  }

  function wisFijn() {
    if (!fijnSleutel && fijnSegmenten === 0) return;
    fijnSleutel = "";
    fijnSegmenten = 0;
    fijnSg.zetAantal(0);
    for (const b of grondBenen) {
      info.zetFijn(b.i, false);
      if (b.baan !== "L1") { b.baan = "L1"; if (lijnModus === "route") zetBaanRoute(b); }
    }
    info.commit();
  }

  let cssW = 0, cssH = 0;
  function update(dt) {
    if (!groep.visible) return;
    const canvas = renderer.domElement;
    const w = canvas.clientWidth || canvas.width, h = canvas.clientHeight || canvas.height;
    if (w !== cssW || h !== cssH) {
      cssW = w; cssH = h;
      zetLijnSchaal(materialen, cssW, cssH);
    }
    // de bol draait, de camera staat vast: één inverse per frame
    globeGroup.updateMatrix();
    inv.copy(globeGroup.matrix).invert();
    camLocaal.copy(camera.position).applyMatrix4(inv);
    const perEenheid = cssH / (2 * Math.tan((camera.fov * D2R) / 2));

    // LOD-keuze uit kijkhoogte en schermhoogte, met hysterese
    const hoogte = getAltitudeKm();
    kmPerCssPx = (2 * hoogte * Math.tan((camera.fov * D2R) / 2)) / cssH;
    zetKmPerPx(materialen, kmPerCssPx);     // het lengtepatroon in schermpixels
    let nieuw = niveau;
    if (niveau === 0 && kmPerCssPx < tolL0) nieuw = 1;
    if (niveau === 1 && kmPerCssPx >= tolL0 * LOD.hysterese) nieuw = 0;
    if (niveau === 1 && kmPerCssPx < tolL1) nieuw = 2;
    if (niveau === 2 && kmPerCssPx >= tolL1 * LOD.hysterese) nieuw = 1;
    if (niveau === 0 && kmPerCssPx < tolL1) nieuw = 2;
    if (niveau === 2 && kmPerCssPx >= tolL0 * LOD.hysterese) nieuw = 0;
    if (nieuw !== niveau) {
      niveau = nieuw;
      if (niveau < 2) wisFijn();
    }
    const route = lijnModus === "route";
    L0.lijn.visible = route && niveau === 0;
    L1.lijn.visible = route && niveau >= 1;
    fijnLijn.visible = route && niveau === 2;
    const nu = performance.now();
    if (route && (niveau === 2 || kmPerCssPx < tolL1 * LOD.prefetchFactor) && nu - laatsteHerzien > LOD.herzienMs) {
      laatsteHerzien = nu;
      if (niveau === 2) herzieFijn(hoogte, cssW / cssH, nu);
      else {
        // prefetch: de bundels van de grondstoffen in beeld alvast halen
        const p = camLocaal.clone().normalize();
        const latC = Math.asin(Math.max(-1, Math.min(1, p.y))) / D2R, lonC = Math.atan2(-p.z, p.x) / D2R;
        const halfH = hoogte * Math.tan((camera.fov * D2R) / 2) * LOD.marge;
        const dLat = halfH / 111.195, dLon = Math.min(180, (halfH * cssW / cssH) / (111.195 * Math.max(0.05, Math.cos(latC * D2R))));
        for (const b of grondBenen) if (inBeeld(b.bbox, lonC, latC, dLon, dLat)) haalFijn(b.grondstof);
      }
    }

    if (bewegingAan) kometen.update(dt, camLocaal, perEenheid);
    gloed.update(camLocaal, perEenheid);
    if (stippen.visible) {
      const d = camLocaal.length();
      const horizon = d > radius ? radius / d : 1;
      const rx = camLocaal.x / d, ry = camLocaal.y / d, rz = camLocaal.z / d;
      const wereld = (STIP.wereldKm / AARDSTRAAL_KM) * radius;
      for (let i = 0; i < nStip; i++) {
        const o = i * 3, px = stipXyz[o], py = stipXyz[o + 1], pz = stipXyz[o + 2];
        if (!stroomAan.get(stipStroom[i]) || (px * rx + py * ry + pz * rz) / radius < horizon) { stipGrootte[i] = 0; continue; }
        const afst = Math.max(1e-6, Math.hypot(px - camLocaal.x, py - camLocaal.y, pz - camLocaal.z));
        stipGrootte[i] = Math.min(STIP.maxPx, Math.max(STIP.minPx, (2 * wereld * perEenheid) / afst));
      }
      stipAttrGr.needsUpdate = true;
    }
    info.commit();
  }

  // ── de API voor main.js / de HUD ─────────────────────────────────────────
  const api = {
    groep, update, stromen, grondstoffen, benen,
    isAan: (sleutel) => !!stroomAan.get(sleutel),
    isGrondstofAan: (g) => gsAan(g),
    zetStroom(sleutel, aan) {
      if (!stroomAan.has(sleutel)) return false;
      stroomAan.set(sleutel, !!aan);
      pasAanToe();
      return true;
    },
    zetGrondstof(g, aan) {
      for (const s of stromenVanGrondstof.get(g) || []) stroomAan.set(s.sleutel, !!aan);
      pasAanToe();
    },
    zetKleurModus(m) {
      if (m === kleurModus) return;
      kleurModus = m;
      pasKleurToe();
      pasAanToe();
    },
    zetLijnModus(m) {
      if (m === lijnModus || !LIJNMODI.includes(m)) return;
      for (const h of hemelsbreed.values()) h.lijn.visible = false;
      lijnModus = m;
      if (m !== "route") { bouwHemelsbreed(m).lijn.visible = true; wisFijn(); }
      zetAlleBanen();
    },
    zetGloed(aan) { gloedAan = !!aan; pasAanToe(); },
    zetBeweging(aan) { bewegingAan = !!aan; kometen.groep.visible = bewegingAan; },
    get kleurModus() { return kleurModus; },
    get lijnModus() { return lijnModus; },
    /** Voor de HUD: km per modaliteit en de beenlijst van één stroom. */
    stroomInfo(sleutel) {
      const s = stroomVan.get(sleutel);
      return s ? { titel: s.titel, label: s.label, grondstof: s.grondstof, kmPerModaliteit: s.kmPerModaliteit,
                   benen: benenVanStroom.get(sleutel), markers: s.markers.map((m) => m.naam) } : null;
    },
    get stats() {
      return {
        stromen: stromen.length, geladen: stromen.length, benen: benen.length,
        stippel: benen.filter((b) => b.stippel).length, markers: nStip, sites: index.sites.length,
        objecten: [L0.lijn, L1.lijn, fijnLijn, luchtLijn, ...[...hemelsbreed.values()].map((h) => h.lijn)].filter((o) => o.visible).length
                  + (kometen.groep.visible ? 1 : 0) + (gloed.groep.visible ? 1 : 0) + (stippen.visible ? 1 : 0),
        niveau, kmPerCssPx: +kmPerCssPx.toFixed(3), fijnSegmenten,
        segmentenL0: L0.segmenten, segmentenL1: L1.segmenten, segmentenLucht: luchtSg.geo.instanceCount,
        fijnResident: [...fijnResident.entries()].filter(([, v]) => v === "klaar").map(([k]) => k),
        kometen: kometen.stats, gloedKnopen: gloed.aantal,
        msLaden: Math.round(tLaden - t0), msDecoderen: Math.round(tDecode - tLaden),
        bundelVersie, kleurModus, lijnModus,
      };
    },
  };
  return api;
}
