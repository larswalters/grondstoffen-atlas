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
  binnenvaart: 0x35e0c0,  // echte AIS-tracks (barge) óf riviergeometrie uit de bulklaag
  truck: 0xffb04d,        // weg-been (echte geometrie) + last mile — amber, zie de kop
  spoor: 0xff7ab8,        // landnet — EIGEN kleur sinds 2026-07-28. Hij deelde amber
                          // met truck zolang geen enkele stroom een spoorbeen had; de
                          // koperstroom Escondida → Guixi heeft er nu wél een, en twee
                          // modaliteiten in één kleur maakt de legenda onwaar.
  leiding: 0x9b8cff,      // slurryleiding — een EIGEN VERBINDING, geen net (besluit
                          // Lars 2026-07-23). Altijd te onderscheiden van de vier
                          // netten, want dit been kan per definitie niet herrouteren.
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

/** Verdicht een been langs de GROOTCIRKEL zodat het op het oppervlak blijft.
 *
 * ⚠️ WAAROM DIT MOET (gemeten 2026-07-28, op Lars' "ik zie geen leiding bij
 * Escondida"): twee punten worden in 3D verbonden met een RECHTE KOORDE, en een
 * koorde van 153 km duikt in het midden ~0,46 km ónder het boloppervlak. Een
 * schematisch been van twee punten — de slurryleiding, elke haven-aanloop, het
 * Wesel-vak — ligt dus niet op de kaart maar er dwars doorheen, en verdwijnt bij
 * inzoomen precies daar waar je kijkt. Hetzelfde als de tegel-koorde die de bol
 * eronder liet doorprikken (M22), alleen andersom.
 *
 * De stap van 5 km is geijkt op de zakking: over 5 km is die 0,5 m, ruim onder
 * de 130 m waarop de tegels liggen — kleiner verdichten kost punten zonder dat
 * je het ziet.
 */
function verdicht(punten, maxKm = 5) {
  const R = 6371;
  const uit = [punten[0]];
  for (let i = 1; i < punten.length; i++) {
    const [lo1, la1] = punten[i - 1], [lo2, la2] = punten[i];
    const p1 = [la1 * Math.PI / 180, lo1 * Math.PI / 180];
    const p2 = [la2 * Math.PI / 180, lo2 * Math.PI / 180];
    const d = 2 * Math.asin(Math.sqrt(
      Math.sin((p2[0] - p1[0]) / 2) ** 2 +
      Math.cos(p1[0]) * Math.cos(p2[0]) * Math.sin((p2[1] - p1[1]) / 2) ** 2));
    const n = Math.ceil((d * R) / maxKm);
    if (n > 1 && d > 1e-9) {
      for (let k = 1; k < n; k++) {
        const f = k / n;
        const a = Math.sin((1 - f) * d) / Math.sin(d);
        const b = Math.sin(f * d) / Math.sin(d);
        const x = a * Math.cos(p1[0]) * Math.cos(p1[1]) + b * Math.cos(p2[0]) * Math.cos(p2[1]);
        const y = a * Math.cos(p1[0]) * Math.sin(p1[1]) + b * Math.cos(p2[0]) * Math.sin(p2[1]);
        const z = a * Math.sin(p1[0]) + b * Math.sin(p2[0]);
        uit.push([Math.atan2(y, x) * 180 / Math.PI,
                  Math.atan2(z, Math.hypot(x, y)) * 180 / Math.PI]);
      }
    }
    uit.push(punten[i]);
  }
  return uit;
}

function maakBeen(been, radius, kleur, klemOpHorizon) {
  const punten = verdicht(been.punten || []);
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

export async function laadStroomroute(radius, versie, klemOpHorizon,
                                      bestand = "stroomroute-pilot.json") {
  // ⚠️ Sinds 2026-07-28 draagt deze laag MEER DAN ÉÉN stroom, en daarom is de
  // bestandsnaam een parameter geworden in plaats van vast. Elke stroom is een
  // eigen bestand en een eigen groep, zodat hij los aan/uit kan — precies het
  // patroon van de vijf tracksets in aistracks.js. Eén gedeeld bestand zou de
  // stromen aan elkaar vastklinken en elke nieuwe stroom een herbake van alle
  // andere kosten.
  const r = await fetch(`data/${bestand}?v=${versie}`);
  if (!r.ok) throw new Error(`${bestand}: HTTP ${r.status}`);
  const d = await r.json();

  const groep = new THREE.Group();
  groep.name = `stroomroute-${d.stroom || bestand}`;

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
    stroom: d.stroom || bestand,
    routebrief: d.routebrief || null,
  };
}
