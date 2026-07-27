// stroomroute.js — de eerste stroom-preview: één echte grondstofstroom als
// keten over drie netten (M28).
//
// Tekent de gebakken route van de grafietstroom Balama → VS battery belt uit
// data/stroomroute-pilot.json: het zeebeen over MARNET (de Kaap-route, zoals
// de echte stroom vaart), het binnenvaartbeen over échte Mississippi-AIS-tracks
// (New Orleans-delta → Vidalia) en het spoorbeen over het landnet (Vidalia →
// battery belt TN/KY). MARNET zelf staat niet op de bol — wat je hier ziet is
// de GEROUTETE stroom, niet het net waarover gerouteerd is.
//
// ⚠️ KLEUR = MODALITEIT — bewust anders dan aistracks (daar is kleur richting).
//   Het punt van deze laag is de OVERGANG tussen de netten zichtbaar maken:
//   waar de zee ophoudt en de barge begint, en waar de kade het spoor wordt —
//   dat zijn precies de overslagpunten waar de hele keten om draait. Binnen
//   één stroom is richting geen signaal (alle lading reist dezelfde kant op),
//   dus die as is vrij en de modaliteit mag hem dragen.
//
// Verder exact de tekendiscipline van aistracks.js: één LineSegments per been,
// klemOpHorizon op het materiaal, frustumCulled uit. De vier overslag-/eind-
// punten als THREE.Points in schermpixels (de LAR-480-les).
//
// ⚠️ Twee keuzes die uit de eerste CDP-verificatie kwamen, niet uit de spec:
//   * renderOrder 7,5 — BOVEN het landnet (7). Het spoorbeen volgt per
//     definitie exact een landnet-lijn; op 6,7 tekende het witte landnet er
//     dus overheen en was het been onzichtbaar precies waar het loopt.
//   * toneMapped uit — door ACES bleekten alle drie de kleuren naar bijna
//     wit, waardoor de legenda loog. Zonder tone mapping ís de getekende
//     kleur de legenda-kleur.

import * as THREE from "three";

// Kleur per modaliteit — dezelfde drie netten als de keten-tests van 2026-07-27.
const KLEUR = {
  zee: 0x5aa7ff,          // MARNET-zeebeen
  binnenvaart: 0x35e0c0,  // echte AIS-tracks (barge)
  spoor: 0xffb04d,        // landnet
};

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/aistracks.js (z = −sin lon).
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  uit[o + 0] = r * c * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * c * Math.sin(lon);
}

function maakBeen(punten, radius, kleur, klemOpHorizon) {
  const n = punten.length - 1;
  if (n < 1) return null;   // een been zonder lijnstuk: niets tekenen
  const pos = new Float32Array(n * 6);
  let o = 0;
  for (let i = 0; i < n; i++) {
    // Punten zijn [lon, lat] (GeoJSON-volgorde) — zie het datacontract.
    opBol(punten[i][0], punten[i][1], radius, pos, o);
    opBol(punten[i + 1][0], punten[i + 1][1], radius, pos, o + 3);
    o += 6;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.LineBasicMaterial({
    color: kleur, transparent: true, opacity: 0.95,
    toneMapped: false,       // legenda-kleur = getekende kleur (zie de kop)
  });
  klemOpHorizon(mat);
  const seg = new THREE.LineSegments(geo, mat);
  seg.renderOrder = 7.5;   // boven het landnet (7) — zie de kop
  seg.frustumCulled = false;
  return seg;
}

function maakMarkers(markers, radius, klemOpHorizon) {
  if (!markers.length) return null;
  const pos = new Float32Array(markers.length * 3);
  for (let i = 0; i < markers.length; i++) {
    opBol(markers[i].lon, markers[i].lat, radius, pos, i * 3);
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 7,
    sizeAttenuation: false,   // grootte in PIXELS (de LAR-480/marker-les)
    transparent: true,
    opacity: 0.95,
    toneMapped: false,
  });
  klemOpHorizon(mat);
  const points = new THREE.Points(geo, mat);
  points.renderOrder = 7.6;   // net boven de benen
  points.frustumCulled = false;
  return points;
}

export async function laadStroomroute(radius, versie, klemOpHorizon) {
  const r = await fetch(`data/stroomroute-pilot.json?v=${versie}`);
  if (!r.ok) throw new Error(`stroomroute-pilot.json: HTTP ${r.status}`);
  const d = await r.json();

  const groep = new THREE.Group();
  groep.name = "stroomroute";

  const benen = [];
  for (const been of d.benen || []) {
    const seg = maakBeen(
      been.punten || [], radius,
      KLEUR[been.modaliteit] ?? 0xffffff, klemOpHorizon
    );
    if (seg) {
      seg.name = `stroomroute-${been.modaliteit}`;
      groep.add(seg);
    }
    benen.push({
      modaliteit: been.modaliteit,
      km: been.km,
      punten: (been.punten || []).length,
    });
  }

  const markerLaag = maakMarkers(d.markers || [], radius, klemOpHorizon);
  if (markerLaag) groep.add(markerLaag);

  return {
    groep,
    benen,                                        // stats per been
    markers: (d.markers || []).map((m) => m.naam),
    titel: d.titel,
  };
}
