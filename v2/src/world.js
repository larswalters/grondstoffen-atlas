// world.js — de vectorwereld: kustlijnen uit Natural Earth 1:10M, als echte
// lijnen op de bol getekend.
//
// DIT IS DE KERN VAN M22. Een satelliettextuur van 4096px is ~9,8 km per pixel;
// zoom je in tot 1,3 km per schermpixel, dan wordt elke textuurpixel over ~7
// schermpixels uitgesmeerd — dat is de wazigheid. Een lijn heeft geen
// pixelgrootte en blijft dus op ELKE zoom scherp. Wat er hooguit overblijft is
// hoekigheid, en dat is een datakwestie: 1:10M heeft een mediane puntafstand
// van 1,5 km tegen 7,7 km bij het oude 1:50M.
//
// Formaat (gebakken door tools/bake_world.py):
//   world-10m.json  { schaal, punten, ringen, index: [[byteOffset, aantal], ..] }
//   world-10m.bin   per ring: delta-gecodeerde zigzag-varints, lon/lat om en om

import * as THREE from "three";

/** Leest zigzag-varints uit een Uint8Array. */
function maakLezer(bytes) {
  let p = 0;
  return {
    zetPositie(n) { p = n; },
    volgende() {
      let resultaat = 0;
      let schuif = 0;
      while (true) {
        const b = bytes[p++];
        resultaat |= (b & 0x7f) << schuif;
        if ((b & 0x80) === 0) break;
        schuif += 7;
      }
      // zigzag terugdraaien: even = positief, oneven = negatief
      return (resultaat >>> 1) ^ -(resultaat & 1);
    },
  };
}

/**
 * Laadt het wereldmodel en bouwt er één LineSegments van (dus één draw call,
 * hoeveel eilanden er ook zijn).
 *
 * @param {number} radius  straal van de bol
 * @returns {Promise<{lijnen: THREE.LineSegments, stats: object}>}
 */
export async function laadVectorWereld(radius, klemOpHorizon = null) {
  const t0 = performance.now();

  const [meta, buffer] = await Promise.all([
    fetch("data/world-10m.json").then((r) => {
      if (!r.ok) throw new Error(`world-10m.json: HTTP ${r.status}`);
      return r.json();
    }),
    fetch("data/world-10m.bin").then((r) => {
      if (!r.ok) throw new Error(`world-10m.bin: HTTP ${r.status}`);
      return r.arrayBuffer();
    }),
  ]);
  const tGeladen = performance.now();

  const bytes = new Uint8Array(buffer);
  const lezer = maakLezer(bytes);
  const schaal = meta.schaal;

  // Precies OP het oppervlak bouwen. De opheffing boven de bol gebeurt door
  // het hele object te schalen (zie main.js), want die moet meeschalen met de
  // kijkhoogte: een vaste 1.0015 is 9,5 km — onzichtbaar vanuit de ruimte,
  // maar van 1 km hoogte loopt je kustlijn dan een flink eind naast de kust.
  const r = radius;

  const posities = new Float32Array(meta.punten * 3);
  // Elke ring is gesloten: n punten geven n-1 lijnstukken tussen opeenvolgende
  // punten (het laatste punt is gelijk aan het eerste).
  const indices = new Uint32Array((meta.punten - meta.ringen) * 2);

  let pi = 0; // schrijfkop posities (in punten)
  let ii = 0; // schrijfkop indices

  for (const [offset, aantal] of meta.index) {
    lezer.zetPositie(offset);

    let x = 0;
    let y = 0;
    const eersteIndex = pi;

    for (let k = 0; k < aantal; k++) {
      x += lezer.volgende();
      y += lezer.volgende();

      const lon = (x / schaal) * (Math.PI / 180);
      const lat = (y / schaal) * (Math.PI / 180);
      const cosLat = Math.cos(lat);

      // Exact dezelfde afspraak als v1's latLonToVec3 (src/util.js):
      //   phi = 90 - lat, theta = lon + 180
      //   x = -r·sin(phi)·cos(theta)  ->  r·cos(lat)·cos(lon)
      //   z =  r·sin(phi)·sin(theta)  -> -r·cos(lat)·sin(lon)
      // Dit MOET kloppen met twee dingen tegelijk: de UV-afbeelding van
      // THREE.SphereGeometry (lon 0 ligt op +X) en de markers/routes die in
      // M26 uit v1 komen. Een eerdere versie zette lon 0 op +Z — dat is 90°
      // verdraaid: de kustlijnen klopten onderling, maar lagen los van de bol.
      posities[pi * 3 + 0] = r * cosLat * Math.cos(lon);
      posities[pi * 3 + 1] = r * Math.sin(lat);
      posities[pi * 3 + 2] = -r * cosLat * Math.sin(lon);

      if (k > 0) {
        indices[ii++] = eersteIndex + k - 1;
        indices[ii++] = eersteIndex + k;
      }
      pi++;
    }
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(posities, 3));
  geo.setIndex(new THREE.BufferAttribute(indices, 1));

  const mat = new THREE.LineBasicMaterial({
    color: 0xdfe9f5,
    transparent: true,
    opacity: 0.95,
  });

  if (klemOpHorizon) klemOpHorizon(mat);
  const lijnen = new THREE.LineSegments(geo, mat);
  lijnen.renderOrder = 6;   // boven de tegels (1-3); zie klemOpHorizon in globe.js

  const t1 = performance.now();

  return {
    lijnen,
    stats: {
      punten: meta.punten,
      ringen: meta.ringen,
      segmenten: ii / 2,
      kbOverdracht: Math.round((bytes.byteLength + JSON.stringify(meta).length) / 1024),
      msLaden: Math.round(tGeladen - t0),
      msVerwerken: Math.round(t1 - tGeladen),
    },
  };
}
