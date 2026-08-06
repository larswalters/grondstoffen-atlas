// stroomleven.js — de stromen laten LEVEN: een lichtgevende koker boven de
// gemeten lijn, plus deeltjes die er als schepen overheen bewegen (M26/LAR-490).
//
// ✅ BESLUIT LARS (2026-08-06): de lijnen blijven op de grond. V1's bogen vlogen
// 22% van de bolstraal de lucht in en dat was mooi, maar geografisch verzonnen;
// v2 heeft er M23–M28 over gedaan om ze op de échte zeeroute, het échte spoor en
// de échte weg te krijgen. Het 3D-gevoel komt daarom NIET uit het optillen van de
// route, maar uit een gloed-koker ERBOVEN plus beweging. Elke meter blijft kloppen.
//
// ⚠️ DEZE LAAG RAAKT `stroomroute.js` NIET AAN. Die tekent de dunne, exacte lijn
// in de modaliteitskleur en is bewezen (v=111, vijf stromen, 0 console-fouten);
// wat hier bijkomt ligt eromheen. Zou de koker de lijn vervangen, dan zou een
// visuele bijstelling stilzwijgend de legenda-kleur en de gemeten geometrie
// kunnen verschuiven — precies de klasse fouten die dit project al twee keer
// heeft opgelost ("de legenda loog", generator↔uitvoer-drift).
//
// DE KOKER is opgebouwd uit een paar schillen op oplopende hoogte met aflopende
// breedte en helderheid. Additief opgeteld leest dat als één volume dat boven de
// route hangt. Geen enkele schil draagt betekenis: de betekenis zit in de dunne
// lijn eronder. De breedte staat in PIXELS (LineMaterial met worldUnits=false),
// want een lijn van echte meters is op wereldhoogte onzichtbaar en op straat-
// niveau een muur — dat is dezelfde hybride regel die de ontwerpbrief voor
// lijndikte kiest en die `gloednodes.js` voor de gloed gebruikt.
//
// DE DEELTJES zijn niet decoratief. Hun snelheid komt per modaliteit uit een
// realistische reissnelheid, en hun onderlinge afstand uit de beenlengte, zodat
// een zeebeen van 19.000 km er zichtbaar langer over doet dan een truckbeen van
// 8 km. Dat is het v1-principe uit `voyages.js` (afvaarten volgen uit volume,
// reisduur uit lengte), hier in de eenvoudigste vorm die op de gebakken stromen
// past — de volumes per been zitten nog niet in `stroomroute-*.json`.
//
// ⚠️ Wat hier NIET gebeurt: een deeltje is GEEN schip en het aantal zegt niets
// over vrachtvolume. Zodra het losse metadatabestand naast stroomroute-*.json er
// is (met volume per been) hoort dit die getallen te lezen; tot dan is de
// beweging waar en het aantal een keuze.

import * as THREE from "three";
import { Line2 } from "three/addons/lines/Line2.js";
import { LineGeometry } from "three/addons/lines/LineGeometry.js";
import { LineMaterial } from "three/addons/lines/LineMaterial.js";

// Zelfde kleuren als stroomroute.js — kleur is MODALITEIT, niet grondstof.
const KLEUR = {
  zee: 0x5aa7ff,
  binnenvaart: 0x35e0c0,
  truck: 0xffb04d,
  spoor: 0xff7ab8,
  leiding: 0x9b8cff,
};

// Reissnelheid per modaliteit in km/dag — grof maar realistisch, en het gaat om
// de VERHOUDING: een zeeschip doet er zichtbaar langer over dan een trein.
const KM_PER_DAG = {
  zee: 700,
  binnenvaart: 250,
  spoor: 500,
  truck: 600,
  leiding: 2000,   // continu proces, leest als een gestage stroom
};

// De schillen van de koker: [hoogte in km boven de route, breedte in px, helderheid]
const SCHILLEN = [
  [0.0, 9.0, 0.16],
  [1.6, 6.5, 0.13],
  [3.4, 4.0, 0.10],
];

const AARDSTRAAL_KM = 6371;

export const AFSTEMMING = {
  deeltjesPerBeen: 3,      // hoeveel deeltjes tegelijk over één been
  deeltjeMinPx: 4.0,
  deeltjeMaxPx: 13.0,
  tempo: 1.0,              // 1 = één dag reistijd per seconde
};

function opBol(lonDeg, latDeg, r) {
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  return [r * c * Math.cos(lon), r * Math.sin(lat), -r * c * Math.sin(lon)];
}

// Grootcirkelafstand in km — voor de booglengte waarop de deeltjes lopen.
function gcKm(a, b) {
  const R = 6371, t = Math.PI / 180;
  const dLat = (b[1] - a[1]) * t, dLon = (b[0] - a[0]) * t;
  const s = Math.sin(dLat / 2) ** 2 +
    Math.cos(a[1] * t) * Math.cos(b[1] * t) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.min(1, Math.sqrt(s)));
}

const VERT_D = `
attribute float grootte;
attribute vec3 kleur;
varying vec3 vKleur;
void main() {
  vKleur = kleur;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  gl_PointSize = grootte;
}
`;
const FRAG_D = `
precision highp float;
varying vec3 vKleur;
void main() {
  vec2 p = gl_PointCoord - vec2(0.5);
  float d = length(p) * 2.0;
  if (d > 1.0) discard;
  float kern = exp(-9.0 * d * d);
  gl_FragColor = vec4(vKleur, kern);
}
`;

export async function laadStroomleven(radius, versie, klemOpHorizon, bestand,
                                      renderer, camera) {
  const r = await fetch(`data/${bestand}?v=${versie}`);
  if (!r.ok) throw new Error(`${bestand}: HTTP ${r.status}`);
  const doc = await r.json();

  const groep = new THREE.Group();
  const materialen = [];   // LineMaterials, die willen de vensterresolutie weten
  const banen = [];        // per been: punten in 3D + cumulatieve km

  for (const been of doc.benen || []) {
    const punten = been.punten || [];
    if (punten.length < 2) continue;
    const kleur = KLEUR[been.modaliteit] ?? 0xffffff;

    // ⚠️ Stippel-benen krijgen GEEN koker en GEEN deeltjes. Gestippeld betekent
    // in dit project "hier reikt het net niet" (werkwijze §7); daar een stroom
    // overheen laten lopen zou een verbinding suggereren die we juist als
    // ontbrekend hebben vastgesteld.
    if (been.stippel) continue;

    const plat = [];
    for (const p of punten) {
      const [x, y, z] = opBol(p[0], p[1], radius);
      plat.push(x, y, z);
    }

    for (const [hoogteKm, breedte, helder] of SCHILLEN) {
      const rr = radius * (1 + hoogteKm / AARDSTRAAL_KM);
      const pos = [];
      for (const p of punten) {
        const [x, y, z] = opBol(p[0], p[1], rr);
        pos.push(x, y, z);
      }
      const geo = new LineGeometry();
      geo.setPositions(pos);
      const mat = new LineMaterial({
        color: kleur,
        linewidth: breedte,          // pixels (worldUnits blijft false)
        transparent: true,
        opacity: helder,
        blending: THREE.AdditiveBlending,
        depthTest: false,
        depthWrite: false,
        toneMapped: false,
      });
      // ⚠️ klemOpHorizon zet clippingPlanes; LineMaterial erft van
      // ShaderMaterial en ondersteunt die, dus de achterkant van de bol valt
      // net als bij de andere lagen weg.
      klemOpHorizon(mat);
      const lijn = new Line2(geo, mat);
      lijn.renderOrder = 7.45;   // NET onder stroomroute.js (7,5): de koker
                                 // ligt eromheen, de exacte lijn blijft bovenop
      lijn.frustumCulled = false;
      materialen.push(mat);
      groep.add(lijn);
    }

    // booglengte voor de deeltjes
    const cum = [0];
    for (let i = 1; i < punten.length; i++) {
      cum.push(cum[i - 1] + gcKm(punten[i - 1], punten[i]));
    }
    const totaal = cum[cum.length - 1];
    if (totaal > 0) {
      banen.push({
        plat, cum, totaal, kleur: new THREE.Color(kleur),
        kmPerDag: KM_PER_DAG[been.modaliteit] ?? 500,
      });
    }
  }

  // --- de deeltjes -----------------------------------------------------------
  const perBeen = AFSTEMMING.deeltjesPerBeen;
  const n = banen.length * perBeen;
  const dPos = new Float32Array(Math.max(1, n) * 3);
  const dKleur = new Float32Array(Math.max(1, n) * 3);
  const dGrootte = new Float32Array(Math.max(1, n));
  const fase = new Float32Array(Math.max(1, n));

  banen.forEach((b, bi) => {
    for (let k = 0; k < perBeen; k++) {
      const i = bi * perBeen + k;
      fase[i] = k / perBeen;                 // gelijkmatig over het been verdeeld
      dKleur[i * 3] = b.kleur.r;
      dKleur[i * 3 + 1] = b.kleur.g;
      dKleur[i * 3 + 2] = b.kleur.b;
      dGrootte[i] = AFSTEMMING.deeltjeMinPx;
    }
  });

  const dGeo = new THREE.BufferGeometry();
  const attrPos = new THREE.BufferAttribute(dPos, 3);
  attrPos.setUsage(THREE.DynamicDrawUsage);
  const attrGr = new THREE.BufferAttribute(dGrootte, 1);
  attrGr.setUsage(THREE.DynamicDrawUsage);
  dGeo.setAttribute("position", attrPos);
  dGeo.setAttribute("kleur", new THREE.BufferAttribute(dKleur, 3));
  dGeo.setAttribute("grootte", attrGr);

  const dMat = new THREE.ShaderMaterial({
    vertexShader: VERT_D, fragmentShader: FRAG_D,
    blending: THREE.AdditiveBlending, transparent: true,
    depthTest: false, depthWrite: false,
  });
  const deeltjes = new THREE.Points(dGeo, dMat);
  deeltjes.renderOrder = 7.55;   // net boven de lijn, zodat een "schip" leesbaar
                                 // over zijn eigen route beweegt
  deeltjes.frustumCulled = false;
  groep.add(deeltjes);

  // positie op de baan bij fractie f (0..1) langs de ECHTE booglengte, zodat
  // een deeltje niet versnelt waar de punten dichter liggen — dezelfde reden
  // waarom v1 `getPointAt` (booglengte) gebruikt in plaats van de curve-parameter
  const tmp = new THREE.Vector3();
  function opBaan(b, f, uit, o) {
    const doel = f * b.totaal;
    let lo = 0, hi = b.cum.length - 1;
    while (lo + 1 < hi) {
      const mid = (lo + hi) >> 1;
      if (b.cum[mid] <= doel) lo = mid; else hi = mid;
    }
    const span = b.cum[hi] - b.cum[lo];
    const t = span > 0 ? (doel - b.cum[lo]) / span : 0;
    for (let a = 0; a < 3; a++) {
      uit[o + a] = b.plat[lo * 3 + a] * (1 - t) + b.plat[hi * 3 + a] * t;
    }
  }

  const camRicht = new THREE.Vector3();
  let tijd = 0;

  function update(dtSec) {
    if (!groep.visible || !banen.length) return;
    tijd += (dtSec || 0.016) * AFSTEMMING.tempo;

    const d = camera.position.length();
    const horizon = d > radius ? radius / d : 1;
    camRicht.copy(camera.position).normalize();
    const h = renderer.domElement.height / (renderer.getPixelRatio() || 1);
    const perEenheid = h / (2 * Math.tan((camera.fov * Math.PI) / 360));

    banen.forEach((b, bi) => {
      // reisduur in dagen = lengte / snelheid; tempo 1 = één dag per seconde
      const duur = b.totaal / b.kmPerDag;
      for (let k = 0; k < perBeen; k++) {
        const i = bi * perBeen + k;
        const f = (fase[i] + tijd / duur) % 1;
        opBaan(b, f, dPos, i * 3);

        tmp.set(dPos[i * 3], dPos[i * 3 + 1], dPos[i * 3 + 2]);
        groep.localToWorld(tmp);
        if (tmp.dot(camRicht) / radius < horizon) { dGrootte[i] = 0; continue; }
        const afst = tmp.distanceTo(camera.position);
        // dichterbij groter, met een plafond zodat een deeltje op straatniveau
        // geen scherm vullende vlek wordt
        const px = (0.35 * perEenheid) / Math.max(1e-6, afst) * 0.01;
        dGrootte[i] = Math.min(AFSTEMMING.deeltjeMaxPx,
                               Math.max(AFSTEMMING.deeltjeMinPx, px));
      }
    });
    attrPos.needsUpdate = true;
    attrGr.needsUpdate = true;
  }

  function zetResolutie(w, hh) {
    for (const m of materialen) m.resolution.set(w, hh);
  }
  zetResolutie(renderer.domElement.width, renderer.domElement.height);

  return {
    groep, update, zetResolutie,
    stats: { benen: banen.length, schillen: materialen.length, deeltjes: n },
  };
}
