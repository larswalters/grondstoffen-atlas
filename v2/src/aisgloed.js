// aisgloed.js — de AIS-drukte als GLOED op de bol (M27).
//
// Lars' keuze (2026-07-25): niet de geëxtraheerde middellijnen maar het
// dichtheidsveld zélf — de blauwe gloed van zes jaar scheepvaart, zoals de
// verken-PNG's. Tekent per pilotvenster een gebogen quad op de bol met de
// gloed-textuur uit bake_aisgloed.py, ADDITIEF: zwart telt niets op en is
// vanzelf onzichtbaar, de drukte licht op boven donker water én satelliet.
//
// Zelfde tekendiscipline als de andere lagen: depthTest uit + horizonklem
// via klemOpHorizon, renderOrder boven de tegels (6,3 — nét onder de
// aisnet-lijnen op 6,5), transparent zodat hij in de transparante pass rendert
// (de overslag-marker-les van 2026-07-23: opaque tussen invadende tegels
// wordt overschilderd).

import * as THREE from "three";

function opBol(lonDeg, latDeg, r) {
  // Exact dezelfde afspraak als world.js/aisnet.js (z = −sin lon).
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  return [r * c * Math.cos(lon), r * Math.sin(lat), -r * c * Math.sin(lon)];
}

export async function laadAisgloed(radius, versie, klemOpHorizon) {
  const t0 = performance.now();
  const r = await fetch(`data/aisgloed/manifest.json?v=${versie}`);
  if (!r.ok) throw new Error(`aisgloed/manifest.json: HTTP ${r.status}`);
  const d = await r.json();
  const tLaden = performance.now();

  const groep = new THREE.Group();
  const lader = new THREE.TextureLoader();

  await Promise.all(Object.values(d.vensters).map((v) => new Promise((klaar, faal) => {
    lader.load(`data/${v.file}?v=${versie}`, (tex) => {
      tex.colorSpace = THREE.SRGBColorSpace;

      const [w, z, o, n] = v.bbox;
      // gebogen quad: het unit-uv-grid van PlaneGeometry op de bol leggen
      // (~0,05° per segment volgt de kromming ruim binnen een pixel)
      const segLon = Math.min(96, Math.max(8, Math.round((o - w) / 0.05)));
      const segLat = Math.min(96, Math.max(8, Math.round((n - z) / 0.05)));
      const geo = new THREE.PlaneGeometry(1, 1, segLon, segLat);
      const pos = geo.attributes.position;
      const uv = geo.attributes.uv;
      for (let i = 0; i < pos.count; i++) {
        const lon = w + uv.getX(i) * (o - w);
        const lat = z + uv.getY(i) * (n - z);
        const [x, y, zz] = opBol(lon, lat, radius);
        pos.setXYZ(i, x, y, zz);
      }
      geo.computeVertexNormals();

      const mat = new THREE.MeshBasicMaterial({
        map: tex,
        blending: THREE.AdditiveBlending,
        transparent: true,
        depthWrite: false,
        side: THREE.DoubleSide,
      });
      klemOpHorizon(mat);
      const mesh = new THREE.Mesh(geo, mat);
      mesh.renderOrder = 6.3;
      mesh.frustumCulled = false;
      groep.add(mesh);
      klaar();
    }, undefined, faal);
  })));

  return {
    groep,
    vensters: d.vensters,
    stats: {
      vensters: Object.keys(d.vensters).length,
      msLaden: Math.round(tLaden - t0),
      msVerwerken: Math.round(performance.now() - tLaden),
    },
  };
}
