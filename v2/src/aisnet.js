// aisnet.js — het AIS-waternet (M27) als zichtbare laag op de bol.
//
// Tekent de polylijnen uit data/aisnet-pilot.json: vaargeulen afgeleid uit de
// World Bank/IMF "Global Shipping Traffic Density" (0037580, laag Commercial,
// CC-BY 4.0) door bake_aisnet.py. Dit is de KIJK-laag van de ombouw — geen
// graaf, geen router: eerst moet Lars kunnen zien dat de lijnen in de echte
// geul liggen (Tongling, Nederland), pas daarna komen knopen/edges/aanhechting.
//
// Zelfde tekendiscipline als de andere vectorlagen (2026-07-22): één
// LineSegments = één draw call, depthTest uit + horizonklem via klemOpHorizon,
// renderOrder boven de tegels.

import * as THREE from "three";

const KLEUR = 0x49b6ff;   // zeeblauw — dezelfde familie als het oude zeenet

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/havens.js (z = −sin lon) — zie de
  // waarschuwing in de project-CLAUDE.md: een 90°-fout oogt onderling perfect.
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  uit[o + 0] = r * c * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * c * Math.sin(lon);
}

export async function laadAisnet(radius, versie, klemOpHorizon) {
  const t0 = performance.now();
  const r = await fetch(`data/aisnet-pilot.json?v=${versie}`);
  if (!r.ok) throw new Error(`aisnet-pilot.json: HTTP ${r.status}`);
  const d = await r.json();
  const tLaden = performance.now();

  // elke polylijn wordt segmentparen in één buffer: [p0,p1, p1,p2, ...]
  let nSegmenten = 0;
  for (const l of d.lijnen) nSegmenten += l.punten.length - 1;
  const pos = new Float32Array(nSegmenten * 6);
  let o = 0;
  for (const l of d.lijnen) {
    for (let i = 0; i < l.punten.length - 1; i++) {
      opBol(l.punten[i][0], l.punten[i][1], radius, pos, o);
      opBol(l.punten[i + 1][0], l.punten[i + 1][1], radius, pos, o + 3);
      o += 6;
    }
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.LineBasicMaterial({
    color: KLEUR, transparent: true, opacity: 0.9,
  });
  klemOpHorizon(mat);
  const lijnen = new THREE.LineSegments(geo, mat);
  lijnen.renderOrder = 6.5;   // kust 6 · aisnet 6,5 · landnet 7 — water boven land
  lijnen.frustumCulled = false;

  return {
    lijnen,
    vensters: d.vensters,
    stats: {
      lijnen: d.lijnen.length,
      segmenten: nSegmenten,
      kbOverdracht: Math.round((r.headers.get("content-length") || 0) / 1024) ||
        Math.round(JSON.stringify(d).length / 1024),
      msLaden: Math.round(tLaden - t0),
      msVerwerken: Math.round(performance.now() - tLaden),
    },
  };
}
