// stroomroute.js — de stroom-preview: één echte grondstofstroom als keten
// op de bol (M28), sinds het versie-2-contract ROUTEBRIEF-gestuurd.
//
// De benen komen uit data/stroomroute-pilot.json (versie 2), en dát bestand
// volgt de routebrief v2/design/routebrieven/grafiet-balama-vidalia.md:
// de keten begint bij de Balama-MIJN met een truckbeen van echte
// weggeometrie (N380/N1, via de M25-wegcorridor-machinerie — doorgetrokken),
// dan een gestippelde haven-aanloop bij Nacala, zeeschip Nacala → New
// Orleans (de Kaap-route, zoals de echte stroom vaart), containerbarge via
// Port Allen (IRMT) → Port of Vidalia (rivier-mijl 359), en een last mile
// per truck naar de Syrah-fabriek. Het spoorbeen is geschrapt — er ligt
// geen spoor in Concordia Parish. De laag tekent wat de benen zeggen: per
// been "modaliteit" (kleur), "naam", en optioneel "stippel": true. Stippel
// is puur de stijl voor "schematische verbinding" — élke modaliteit kan
// gestippeld zijn (de haven-aanloop is gestippeld zee-blauw, de last mile
// gestippeld truck-amber). MARNET zelf staat niet op de bol — wat je hier
// ziet is de GEROUTETE stroom, niet het net waarover gerouteerd is.
//
// ⚠️ TRUCK = AMBER (0xffb04d), niet meer wit: een witte doorgetrokken
//   weglijn is in Mozambique niet te onderscheiden van het witte
//   landnet-spoor — de Nacala-spoorcorridor loopt vlak bij de N380/N1.
//   Amber is vrij nu het spoorbeen uit deze stroom is.
//
// ⚠️ KLEUR = MODALITEIT — bewust anders dan aistracks (daar is kleur richting).
//   Het punt van deze laag is de OVERGANG tussen de netten zichtbaar maken:
//   waar de zee ophoudt en de barge begint, en waar de kade de weg wordt —
//   dat zijn precies de overslagpunten waar de hele keten om draait. Binnen
//   één stroom is richting geen signaal (alle lading reist dezelfde kant op),
//   dus die as is vrij en de modaliteit mag hem dragen.
//
// Verder exact de tekendiscipline van aistracks.js: één lijnobject per been
// (LineSegments doorgetrokken, THREE.Line gestippeld), klemOpHorizon op het
// materiaal, frustumCulled uit. De overslag-/eindpunten als THREE.Points in
// schermpixels (de LAR-480-les).
//
// ⚠️ Twee keuzes die uit de eerste CDP-verificatie kwamen, niet uit de spec —
//   ze blijven gelden:
//   * renderOrder 7,5 — BOVEN het landnet (7). Een been dat een landnet-lijn
//     volgt was op 6,7 onzichtbaar precies waar het loopt, omdat het witte
//     landnet eroverheen tekende.
//   * toneMapped uit — door ACES bleekten de kleuren naar bijna wit,
//     waardoor de legenda loog. Zonder tone mapping ís de getekende kleur
//     de legenda-kleur.

import * as THREE from "three";

// Kleur per modaliteit. Spoor blijft in de tabel voor latere stromen — de
// laag tekent gewoon wat de benen zeggen; de grafietstroom heeft geen
// spoorbeen meer (zie de routebrief).
const KLEUR = {
  zee: 0x5aa7ff,          // MARNET-zeebeen (zeeschip) + gestippelde haven-aanloop
  binnenvaart: 0x35e0c0,  // echte AIS-tracks (barge)
  truck: 0xffb04d,        // weg-been (echte geometrie) + last mile — amber, zie de kop
  spoor: 0xffb04d,        // landnet (geen been in deze stroom; botst met truck —
                          // geef spoor een eigen kleur zodra een stroom weer een
                          // spoorbeen krijgt)
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

function maakBeen(been, radius, kleur, klemOpHorizon) {
  const punten = been.punten || [];
  if (punten.length < 2) return null;   // een been zonder lijnstuk: niets tekenen

  if (been.stippel) {
    // Stippel-been = schematische verbinding (haven-aanloop, last mile),
    // gestippeld getekend als THREE.Line (doorlopende lijn met 2+ punten,
    // géén LineSegments). dash/gap zijn geijkt op de bolschaal: straal 2,4
    // → een been van ~1 km is ~0,0004 scene-eenheden, dus dash/gap ruim
    // daaronder zodat er meerdere streepjes op passen.
    const pos = new Float32Array(punten.length * 3);
    for (let i = 0; i < punten.length; i++) {
      // Punten zijn [lon, lat] (GeoJSON-volgorde) — zie het datacontract.
      opBol(punten[i][0], punten[i][1], radius, pos, i * 3);
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const mat = new THREE.LineDashedMaterial({
      color: kleur, transparent: true, opacity: 0.95,
      dashSize: 0.00008, gapSize: 0.00005,
      toneMapped: false,     // legenda-kleur = getekende kleur (zie de kop)
    });
    klemOpHorizon(mat);
    const lijn = new THREE.Line(geo, mat);
    // ⚠️ Verplicht bij LineDashedMaterial: zonder computeLineDistances()
    // tekent een dashed lijn gewoon doorgetrokken.
    lijn.computeLineDistances();
    lijn.renderOrder = 7.5;  // boven het landnet (7) — zie de kop
    lijn.frustumCulled = false;
    return lijn;
  }

  const n = punten.length - 1;
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
      been, radius,
      KLEUR[been.modaliteit] ?? 0xffffff, klemOpHorizon
    );
    if (seg) {
      seg.name = `stroomroute-${been.modaliteit}`;
      groep.add(seg);
    }
    benen.push({
      modaliteit: been.modaliteit,
      naam: been.naam,
      stippel: !!been.stippel,
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
