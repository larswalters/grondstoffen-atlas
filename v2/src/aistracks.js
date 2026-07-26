// aistracks.js — echte scheepstracks als kijk-laag op de bol (M28, VS-pilot).
//
// Tekent de track-selectie uit data/aistracks-pilot.json: gevaren lijnen van
// individuele schepen (MarineCadastre/NOAA — de bron die de VS-binnenrivieren
// dekt waar aisstream niets ontvangt). Dit is de bol-toets van de track-aanpak:
// ligt één doorvaart als één vloeiende lijn ín de geul op satelliet, en zie je
// op- en afvaart als eigen banen?
//
// Twee LineSegments (op- en afvaart elk hun kleur), verder exact de
// tekendiscipline van aisnet.js: depthTest uit + horizonklem, renderOrder
// boven de tegels, frustumCulled uit.

import * as THREE from "three";

const KLEUR_OP = 0xffd166;   // opvaart — amber
const KLEUR_AF = 0x7fe8ff;   // afvaart — ijsblauw

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/aisnet.js (z = −sin lon).
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  uit[o + 0] = r * c * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * c * Math.sin(lon);
}

function maakSegmenten(lijnen, radius, kleur, klemOpHorizon) {
  let n = 0;
  for (const l of lijnen) n += l.punten.length - 1;
  const pos = new Float32Array(n * 6);
  let o = 0;
  for (const l of lijnen) {
    for (let i = 0; i < l.punten.length - 1; i++) {
      opBol(l.punten[i][0], l.punten[i][1], radius, pos, o);
      opBol(l.punten[i + 1][0], l.punten[i + 1][1], radius, pos, o + 3);
      o += 6;
    }
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.LineBasicMaterial({
    color: kleur, transparent: true, opacity: 0.55,
  });
  klemOpHorizon(mat);
  const seg = new THREE.LineSegments(geo, mat);
  seg.renderOrder = 6.6;   // net boven aisnet (6,5), onder landnet (7)
  seg.frustumCulled = false;
  return { seg, segmenten: n };
}

export async function laadAisTracks(radius, versie, klemOpHorizon) {
  const t0 = performance.now();
  const r = await fetch(`data/aistracks-pilot.json?v=${versie}`);
  if (!r.ok) throw new Error(`aistracks-pilot.json: HTTP ${r.status}`);
  const d = await r.json();
  const tLaden = performance.now();

  const op = maakSegmenten(d.lijnen.filter((l) => l.richting === "op"),
                           radius, KLEUR_OP, klemOpHorizon);
  const af = maakSegmenten(d.lijnen.filter((l) => l.richting !== "op"),
                           radius, KLEUR_AF, klemOpHorizon);
  const groep = new THREE.Group();
  groep.add(op.seg, af.seg);

  return {
    groep,
    vensters: d.vensters,
    stats: {
      lijnen: d.lijnen.length,
      segmenten: op.segmenten + af.segmenten,
      kbOverdracht: Math.round((r.headers.get("content-length") || 0) / 1024) ||
        Math.round(JSON.stringify(d).length / 1024),
      msLaden: Math.round(tLaden - t0),
      msVerwerken: Math.round(performance.now() - tLaden),
    },
  };
}
