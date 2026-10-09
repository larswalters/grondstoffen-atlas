// stroomlijn.js — HET LIJNMATERIAAL van de stromenbundel: één LineMaterial
// (Three r185, brede lijnen in schermpixels) dat per been weet of het aan
// staat, welke lijnstijl het draagt en welke kleur het heeft — zonder een
// object per been. (Golf 1 van de visuele fase, 2026-10-08, LAR-617; ontwerp
// in v2/design/atlas-product-golf1.md §3.2–3.3.)
//
// WAAROM. ?v=131 tekende elk been als eigen object: 494 LineSegments + 225
// gestippelde Line + 986 Line2 = ~1.700 lijnobjecten, 12,7 M driehoeken, en
// een telefoon haalde 9–14 fps. Alle benen van alle stromen gaan nu in één
// LineSegments2 per LOD-niveau. Wat per been verschilt (aan/uit, stijl, kleur)
// staat in twee INFORMATIETEXTUREN van 1024 × 1 die de vertex-shader uitleest
// op de beenindex: een klik op een stroom herschrijft een paar texels (één
// upload van 4 KB), er wordt niets herbouwd en het aantal draw calls beweegt
// niet.
//
// ⚠️ DE PATCHES HANGEN AAN DE GLSL VAN r185 (gepind in de importmap). Elke
// patch zoekt een letterlijk anker in de shadertekst van LineMaterial en
// `maakLijnMateriaal` asserteert dat elk anker PRECIES ÉÉN keer voorkomt —
// anders throw, luid, niet stil een shader zonder patronen. Wie Three bumpt
// ziet het bij het laden. Terugvalplan: de shader forken naar dit bestand.
//
// ⚠️ customProgramCacheKey: in r185 is de default `onBeforeCompile.toString()`,
// waardoor twee materialen met dezelfde functietekst stil één programma delen.
// Hier is er maar één materiaal-klasse, maar de sleutel staat expliciet.
//
// De horizon blijft een CLIPPING PLANE (GLOBE.klemOpHorizon, depthTest uit):
// LineMaterial draagt de clipping-chunks en de oude draad-en-kometenlaag
// bewees sinds ?v=116 dat dat op Line2 werkt. Een eigen horizontoets in de
// shader is een vastgelegde mislukking (globe.js, 2026-07-22).
//
// Breedtes staan in CSS-PIXELS: `resolution` krijgt de css-maat van het
// canvas, zodat `linewidth` css-px is. Vóór golf 1 stond de draad op 1,7
// DEVICE-px = 0,85 css-px op een telefoon, dunner dan de exacte lijn eronder.

import * as THREE from "three";
import { LineMaterial } from "three/addons/lines/LineMaterial.js";
import { LineSegmentsGeometry } from "three/addons/lines/LineSegmentsGeometry.js";
import { LineSegments2 } from "three/addons/lines/LineSegments2.js";
import { LIJNSTIJL } from "./stroomstijl.js?v=134";

export const TEX_BREEDTE = 1024;    // benen per textuur; de baker faalt luid boven dit getal
export const VLAG_AAN = 1;          // bit 0: de HUD heeft dit been aan
export const VLAG_FIJN = 2;         // bit 1: het fijn-object tekent dit been nu

// Welke rol een lijnobject speelt t.o.v. de FIJN-vlag (uniform `lodRol`):
//   0 basis  → tekent AAN && !FIJN   (L0/L1)
//   1 fijn   → tekent AAN &&  FIJN   (het fijn-object)
//   2 altijd → tekent AAN            (lucht, hemelsbreed-modi)
export const ROL_BASIS = 0, ROL_FIJN = 1, ROL_ALTIJD = 2;

/** De twee informatietexturen + hun schrijvers. Eén exemplaar per bundel. */
export class BeenInfo {
  constructor(aantal) {
    if (aantal > TEX_BREEDTE) {
      throw new Error(`stroomlijn: ${aantal} benen > ${TEX_BREEDTE} — vergroot TEX_BREEDTE (en MAX_BENEN in bak_stroombundel.py)`);
    }
    this.aantal = aantal;
    // RGBA8: R = vlaggen · G = stijlindex · B = breedtefactor × 100 · A ongebruikt
    this.info = new Uint8Array(TEX_BREEDTE * 4);
    for (let i = 0; i < TEX_BREEDTE; i++) this.info[i * 4 + 2] = 100;
    this.infoTex = new THREE.DataTexture(this.info, TEX_BREEDTE, 1, THREE.RGBAFormat, THREE.UnsignedByteType);
    // RGBA32F: lineaire rgb van de lijnkleur (uit THREE.Color.setHex, dus al
    // sRGB → lineair, net als material.color bij LineBasicMaterial)
    this.kleur = new Float32Array(TEX_BREEDTE * 4);
    this.kleurTex = new THREE.DataTexture(this.kleur, TEX_BREEDTE, 1, THREE.RGBAFormat, THREE.FloatType);
    for (const t of [this.infoTex, this.kleurTex]) {
      t.magFilter = THREE.NearestFilter;
      t.minFilter = THREE.NearestFilter;
      t.generateMipmaps = false;
      t.wrapS = t.wrapT = THREE.ClampToEdgeWrapping;
      t.needsUpdate = true;
    }
    this._c = new THREE.Color();
    this.infoVuil = false;
    this.kleurVuil = false;
  }
  isAan(i)  { return (this.info[i * 4] & VLAG_AAN) !== 0; }
  isFijn(i) { return (this.info[i * 4] & VLAG_FIJN) !== 0; }
  stijl(i)  { return this.info[i * 4 + 1]; }
  _zetVlag(i, vlag, aan) {
    const o = i * 4;
    const nieuw = aan ? (this.info[o] | vlag) : (this.info[o] & ~vlag);
    if (nieuw !== this.info[o]) { this.info[o] = nieuw; this.infoVuil = true; }
  }
  zetAan(i, aan)   { this._zetVlag(i, VLAG_AAN, aan); }
  zetFijn(i, fijn) { this._zetVlag(i, VLAG_FIJN, fijn); }
  zetStijl(i, idx) {
    if (this.info[i * 4 + 1] !== idx) { this.info[i * 4 + 1] = idx; this.infoVuil = true; }
  }
  /** Breedtefactor (1,0 = de tabelbreedte); de haak voor dikte = volume (golf 2). */
  zetBreedteF(i, f) {
    const b = Math.max(0, Math.min(255, Math.round(f * 100)));
    if (this.info[i * 4 + 2] !== b) { this.info[i * 4 + 2] = b; this.infoVuil = true; }
  }
  zetKleur(i, hex) {
    this._c.setHex(hex);
    const o = i * 4;
    this.kleur[o] = this._c.r; this.kleur[o + 1] = this._c.g; this.kleur[o + 2] = this._c.b; this.kleur[o + 3] = 1;
    this.kleurVuil = true;
  }
  /** Eén upload per frame hooguit — roep dit aan het eind van een reeks wijzigingen aan. */
  commit() {
    if (this.infoVuil)  { this.infoTex.needsUpdate = true;  this.infoVuil = false; }
    if (this.kleurVuil) { this.kleurTex.needsUpdate = true; this.kleurVuil = false; }
  }
}

// ── de shader-patches ──────────────────────────────────────────────────────
// Elke patch = [anker, vervanging]. De ankers zijn letterlijke regels uit de
// r185-shader; `patch()` eist precies één treffer.
const PATCHES_VERTEX = [
  ["#include <clipping_planes_pars_vertex>", `#include <clipping_planes_pars_vertex>
    // ── stroomlijn (golf 1): per-been informatie uit de texturen ──
    attribute float instanceBeen;
    attribute float instanceAfstandStart;
    attribute float instanceAfstandEnd;
    uniform sampler2D beenInfo;
    uniform sampler2D beenKleur;
    uniform float texBreedte;
    uniform float lodRol;
    uniform vec4 patroon[8];
    varying vec3 vKleur;
    varying float vStijl;
    varying float vAfstandKm;
    float sVerborgen = 0.0;
    float sBreedte = 1.0;`],
  ["vec4 end = modelViewMatrix * vec4( instanceEnd, 1.0 );", `vec4 end = modelViewMatrix * vec4( instanceEnd, 1.0 );
      // ── stroomlijn: aan/uit, stijl, kleur en de pixelafstand langs de lijn ──
      vec2 texUv = vec2( ( instanceBeen + 0.5 ) / texBreedte, 0.5 );
      vec4 info = texture2D( beenInfo, texUv );
      float vlaggen = floor( info.r * 255.0 + 0.5 );
      float aan = mod( vlaggen, 2.0 );
      float fijn = mod( floor( vlaggen / 2.0 ), 2.0 );
      float zichtbaar = aan;
      if ( lodRol < 0.5 ) { zichtbaar *= ( 1.0 - fijn ); }
      else if ( lodRol < 1.5 ) { zichtbaar *= fijn; }
      sVerborgen = 1.0 - zichtbaar;
      vStijl = floor( info.g * 255.0 + 0.5 );
      float breedteF = floor( info.b * 255.0 + 0.5 ) / 100.0;
      int stijlI = int( min( vStijl, 7.0 ) );
      sBreedte = patroon[ stijlI ].x * breedteF;
      vKleur = texture2D( beenKleur, texUv ).rgb;
      // ⚠️ De afstand langs het been gaat in KILOMETERS naar de fragment-shader;
      // de omrekening naar pixels gebeurt daar met één uniform (km per css-px in
      // het beeldmidden). Een eerdere versie deelde hier de CUMULATIEVE km door
      // de diepte van de vertex — dan drijft en rekt het patroon op een lang
      // been zodra de diepte langs de lijn verandert (review 2026-10-08).
      vAfstandKm = ( position.y < 0.5 ) ? instanceAfstandStart : instanceAfstandEnd;`],
  ["offset *= linewidth;", "offset *= linewidth * sBreedte;"],
  ["gl_Position = clip;", `// ── stroomlijn: een verborgen been degenereert buiten de clipruimte ──
      if ( sVerborgen > 0.5 ) { clip = vec4( 2.0, 2.0, 2.0, 1.0 ); }
      gl_Position = clip;`],
];
const PATCHES_FRAGMENT = [
  ["#include <clipping_planes_pars_fragment>", `#include <clipping_planes_pars_fragment>
    // ── stroomlijn (golf 1): patroon per stijl, kleur per been ──
    uniform vec4 patroon[8];
    uniform vec4 patroon2[8];
    uniform float patronenAan;
    uniform float kmPerCssPx;
    varying vec3 vKleur;
    varying float vStijl;
    varying float vAfstandKm;`],
  ["#include <clipping_planes_fragment>", `#include <clipping_planes_fragment>
      // ── stroomlijn: lengtepatroon (alleen alfa), dwarsprofiel, kleur ──
      int si = int( min( floor( vStijl + 0.5 ), 7.0 ) );
      vec4 pt = patroon[ si ];
      vec4 pt2 = patroon2[ si ];
      float pa = 1.0;
      // stijl 6 (onbekend) en 7 (stippel) dragen hun patroon in élke modus;
      // de modaliteitspatronen alleen als ze aan staan (atlasmodus)
      bool actief = ( pt.y > 0.0 ) && ( patronenAan > 0.5 || si >= 6 );
      if ( actief ) {
        // patroon in schermpixels: km langs het been / (km per css-px in het
        // beeldmidden). Aan de rand van de bol is de periode wat kleiner
        // (perspectief), maar hij drijft nergens.
        float fase = mod( vAfstandKm / max( 1e-6, kmPerCssPx ), pt.y );
        pa = ( fase < pt.z ) ? pt2.x : pt.w;
        if ( pa <= 0.001 ) discard;
      }
      if ( patronenAan > 0.5 && pt2.y < 1.0 && abs( vUv.x ) > pt2.y ) { pa *= pt2.z; }
      alpha *= pa;
      diffuseColor.rgb = ( si == 6 ) ? vec3( 1.0, 0.0, 1.0 ) : vKleur;`],
];

function patch(bron, patches, waar) {
  let tekst = bron;
  for (const [anker, vervanging] of patches) {
    const n = tekst.split(anker).length - 1;
    if (n !== 1) {
      throw new Error(`stroomlijn: anker "${anker.slice(0, 48)}" komt ${n}× voor in de ${waar}-shader van LineMaterial — ` +
                      `Three-versie gewijzigd? (verwacht r185, gepind in de importmap)`);
    }
    tekst = tekst.replace(anker, vervanging);
  }
  return tekst;
}

function patroonUniforms() {
  const a = [], b = [];
  for (let i = 0; i < 8; i++) {
    const s = LIJNSTIJL[i] || LIJNSTIJL[6];
    a.push(new THREE.Vector4(s.breedte, s.periode, s.aan, s.alfaUit));
    b.push(new THREE.Vector4(s.alfaAan, s.kernFractie, s.randAlfa, 0));
  }
  return { a, b };
}

export class StroomLijnMateriaal extends LineMaterial {
  constructor(info, lodRol) {
    super({
      color: 0xffffff, linewidth: 1, transparent: true, opacity: 1,
      depthTest: false, depthWrite: false, toneMapped: false,
      worldUnits: false, dashed: false, vertexColors: false,
    });
    const { a, b } = patroonUniforms();
    this.extraUniforms = {
      beenInfo: { value: info.infoTex }, beenKleur: { value: info.kleurTex },
      texBreedte: { value: TEX_BREEDTE }, lodRol: { value: lodRol },
      kmPerCssPx: { value: 1 },
      patroon: { value: a }, patroon2: { value: b }, patronenAan: { value: 1 },
    };
    Object.assign(this.uniforms, this.extraUniforms);
    this.onBeforeCompile = (shader) => {
      shader.vertexShader = patch(shader.vertexShader, PATCHES_VERTEX, "vertex");
      shader.fragmentShader = patch(shader.fragmentShader, PATCHES_FRAGMENT, "fragment");
      Object.assign(shader.uniforms, this.extraUniforms);
    };
  }
  customProgramCacheKey() { return "stroomlijn-golf1-v1"; }
}

/** Maak het materiaal voor één lijnobject; `klemOpHorizon` is GLOBE.klemOpHorizon. */
export function maakLijnMateriaal(info, lodRol, klemOpHorizon) {
  const mat = new StroomLijnMateriaal(info, lodRol);
  klemOpHorizon(mat);          // clippingPlanes + depthTest uit — zie de kop
  return mat;
}

/** Schermschaal op een lijst materialen: css-resolutie, zodat `linewidth` css-px is. */
export function zetLijnSchaal(materialen, cssW, cssH) {
  for (const m of materialen) m.resolution.set(cssW, cssH);
}

/** Km per css-pixel in het beeldmidden (uit kijkhoogte, fov en schermhoogte) —
 *  de maat waarmee de fragment-shader het lengtepatroon in pixels legt. Elke
 *  frame zetten: hij verandert bij elke zoom. */
export function zetKmPerPx(materialen, kmPerCssPx) {
  for (const m of materialen) m.extraUniforms.kmPerCssPx.value = kmPerCssPx;
}

export function zetPatronenAan(materialen, aan) {
  for (const m of materialen) m.extraUniforms.patronenAan.value = aan ? 1 : 0;
}

/** Een segmentgeometrie met vooraf gealloceerde buffers (zodat het fijn-object
 *  in-place gevuld kan worden) en de drie per-instantie attributen die de
 *  shader leest. `zetAantal(n)` zet hoeveel segmenten er getekend worden. */
export function maakSegmentGeometrie(maxSegmenten, dynamisch = false) {
  const geo = new LineSegmentsGeometry();
  const pos = new Float32Array(Math.max(1, maxSegmenten) * 6);
  const been = new Float32Array(Math.max(1, maxSegmenten));
  const afstand = new Float32Array(Math.max(1, maxSegmenten) * 2);
  const posBuf = new THREE.InstancedInterleavedBuffer(pos, 6, 1);
  const afsBuf = new THREE.InstancedInterleavedBuffer(afstand, 2, 1);
  const beenAttr = new THREE.InstancedBufferAttribute(been, 1);
  if (dynamisch) {
    posBuf.setUsage(THREE.DynamicDrawUsage);
    afsBuf.setUsage(THREE.DynamicDrawUsage);
    beenAttr.setUsage(THREE.DynamicDrawUsage);
  }
  geo.setAttribute("instanceStart", new THREE.InterleavedBufferAttribute(posBuf, 3, 0));
  geo.setAttribute("instanceEnd", new THREE.InterleavedBufferAttribute(posBuf, 3, 3));
  geo.setAttribute("instanceAfstandStart", new THREE.InterleavedBufferAttribute(afsBuf, 1, 0));
  geo.setAttribute("instanceAfstandEnd", new THREE.InterleavedBufferAttribute(afsBuf, 1, 1));
  geo.setAttribute("instanceBeen", beenAttr);
  geo.instanceCount = 0;
  // ⚠️ Geen computeBoundingSphere over een half gevulde buffer: de lijnen zijn
  // frustumCulled=false (de horizon doet de clip) en een bounding sphere van
  // een lege buffer is NaN → het object wordt nooit getekend.
  geo.boundingSphere = new THREE.Sphere(new THREE.Vector3(), 1e9);
  geo.boundingBox = null;
  return {
    geo, pos, been, afstand, max: maxSegmenten,
    zetAantal(n) {
      geo.instanceCount = n;
    },
    /** Na een in-place vulling: alleen de gebruikte bytes naar de GPU. */
    markeerBijgewerkt(n) {
      for (const [buf, stride] of [[posBuf, 6], [afsBuf, 2]]) {
        buf.clearUpdateRanges();
        buf.addUpdateRange(0, n * stride);
        buf.needsUpdate = true;
      }
      beenAttr.clearUpdateRanges();
      beenAttr.addUpdateRange(0, n);
      beenAttr.needsUpdate = true;
    },
  };
}

/** Eén getekend lijnobject. frustumCulled uit: de horizon-clip doet het werk. */
export function bouwLijn(segGeo, mat, renderOrder, naam) {
  const lijn = new LineSegments2(segGeo.geo, mat);
  lijn.frustumCulled = false;
  lijn.renderOrder = renderOrder;
  lijn.name = naam;
  return lijn;
}
