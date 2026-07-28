// ankercheck.js — de OPEN LIGPLAATSEN als kijklaag (rest van de anker-check).
//
// Waarom deze laag bestaat: routebrief-werkwijze §2 eist sinds 2026-07-28 dat
// elk laadplek-/overslag-/losplek-punt satelliet-gelegd is vóórdat het een
// anker wordt. Bij de eerste toepassing stond 10 van de 16 fout, van 42 m tot
// 4,5 km. Die uitslag is met woorden slecht over te brengen — vandaar deze
// laag: rood = waar het punt nu staat, groen = waar de satelliet zegt dat het
// hoort, met een lijntje ertussen zodat de verplaatsing afleesbaar is.
//
// ⚠️ STAND 2026-07-28 (later die dag): de zeven goedgekeurde correcties zijn
//   DOORGEVOERD en `data/ankercheck.json` is teruggebracht tot de DRIE punten
//   waar de ligplaats niet aanwijsbaar was (Lobito · Port Allen · Vidalia).
//   Dat is bewust: een rode stip op een al gecorrigeerd punt liegt. De laag
//   zelf blijft ongewijzigd bruikbaar — zodra er voor die drie een voorstel
//   ligt, krijgt het bestand weer `nieuw`-coördinaten en tekent hij vanzelf de
//   rood→groen-paren met het witte lijntje. Weg zodra ze alle drie een kade
//   hebben.
//
// ⚠️ DEZE LAAG WIJZIGT NIETS. Hij leest `ankercheck.json` en tekent; het
//   oordeel en het doorvoeren gebeuren buiten de browser.
//
// Tekendiscipline exact als stroomroute.js: punten als THREE.Points in
// SCHERMpixels (sizeAttenuation uit — de LAR-480-les: wat je op elke hoogte
// moet zien schaalt in schermruimte, niet in wereldruimte), klemOpHorizon op
// elk materiaal, frustumCulled uit, toneMapped uit zodat de legenda-kleur de
// getekende kleur is, en renderOrder boven het landnet.

import * as THREE from "three";

// Rood/groen/blauw/geel — bewust vier duidelijk verschillende tinten; deze
// laag moet leesbaar zijn boven satellietbeeld van woestijn (Atacama), water
// (Lobito, Ruhrort) én stad (Waalhaven, Beilun).
const KLEUR = {
  fout: 0xff3b30,          // staat er nu, en is fout
  onbepaald: 0xff3b30,     // staat er nu en is fout, maar er is nog geen voorstel
  goed: 0x5aa7ff,          // staat er nu en heeft de check doorstaan
  ongecontroleerd: 0xffd23b, // nog niet bekeken
  voorstel: 0x3ddc84,      // het satelliet-gelegde nieuwe punt
};

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/stroomroute.js (z = −sin lon).
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  uit[o + 0] = r * c * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * c * Math.sin(lon);
}

function maakPunten(lijst, radius, kleur, pixels, klemOpHorizon) {
  if (!lijst.length) return null;
  const pos = new Float32Array(lijst.length * 3);
  for (let i = 0; i < lijst.length; i++) {
    opBol(lijst[i][0], lijst[i][1], radius, pos, i * 3);
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.PointsMaterial({
    color: kleur,
    size: pixels,
    sizeAttenuation: false,   // grootte in PIXELS
    transparent: true,
    opacity: 0.95,
    toneMapped: false,
  });
  klemOpHorizon(mat);
  const p = new THREE.Points(geo, mat);
  p.renderOrder = 7.8;        // boven de stroomroute-markers (7,6)
  p.frustumCulled = false;
  return p;
}

/** Dun wit lijntje oud → nieuw: dát maakt de verplaatsing afleesbaar. */
function maakVerbindingen(paren, radius, klemOpHorizon) {
  if (!paren.length) return null;
  const pos = new Float32Array(paren.length * 6);
  let o = 0;
  for (const [oud, nieuw] of paren) {
    opBol(oud[0], oud[1], radius, pos, o);
    opBol(nieuw[0], nieuw[1], radius, pos, o + 3);
    o += 6;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.LineBasicMaterial({
    color: 0xffffff, transparent: true, opacity: 0.7, toneMapped: false,
  });
  klemOpHorizon(mat);
  const seg = new THREE.LineSegments(geo, mat);
  seg.renderOrder = 7.7;
  seg.frustumCulled = false;
  return seg;
}

export async function laadAnkercheck(radius, versie, klemOpHorizon) {
  const r = await fetch(`data/ankercheck.json?v=${versie}`);
  if (!r.ok) throw new Error(`ankercheck.json: HTTP ${r.status}`);
  const d = await r.json();

  const groep = new THREE.Group();
  groep.name = "ankercheck";

  const perStatus = { fout: [], onbepaald: [], goed: [], ongecontroleerd: [] };
  const voorstellen = [];
  const paren = [];
  for (const a of d.ankers || []) {
    (perStatus[a.status] ?? perStatus.fout).push(a.oud);
    if (a.nieuw) {
      voorstellen.push(a.nieuw);
      paren.push([a.oud, a.nieuw]);
    }
  }

  for (const [status, lijst] of Object.entries(perStatus)) {
    // Iets groter dan de stroomroute-markers (7 px): deze punten zijn het
    // onderwerp van de kijkronde, niet de context.
    const p = maakPunten(lijst, radius, KLEUR[status], 9, klemOpHorizon);
    if (p) { p.name = `ankercheck-${status}`; groep.add(p); }
  }
  const v = maakPunten(voorstellen, radius, KLEUR.voorstel, 9, klemOpHorizon);
  if (v) { v.name = "ankercheck-voorstel"; groep.add(v); }
  const lijn = maakVerbindingen(paren, radius, klemOpHorizon);
  if (lijn) { lijn.name = "ankercheck-verplaatsing"; groep.add(lijn); }

  return { groep, ankers: d.ankers || [], titel: d.titel };
}
