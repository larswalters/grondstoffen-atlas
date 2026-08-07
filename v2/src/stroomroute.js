// stroomroute.js — de stroom-preview: één echte grondstofstroom als keten
// op de bol (M28), sinds het versie-2-contract ROUTEBRIEF-gestuurd.
//
// De benen komen uit data/stroomroute-*.json (versie 2), en die bestanden
// volgen de routebrieven in v2/design/routebrieven/. De laag tekent wat de
// benen zeggen: per been "modaliteit", "naam", en optioneel "stippel": true.
// Stippel is puur de stijl voor "schematische verbinding" — élke modaliteit kan
// gestippeld zijn (de haven-aanloop is gestippeld zee-blauw, de last mile
// gestippeld truck-amber). MARNET zelf staat niet op de bol — wat je hier ziet
// is de GEROUTETE stroom, niet het net waarover gerouteerd is.
//
// ⚠️ KLEUR EN LIJNVORM ZIJN SINDS 2026-08-07 SCHAKELBAAR en wonen in
//   `stroomstijl.js`. Lees daar waarom: kort samengevat is kleur=modaliteit de
//   vraag van de ROUTEBOUW ("waar houdt de zee op?") en kleur=grondstof de vraag
//   van de ATLAS ("waar gaat het koper heen?"), en de lijnvorm laat je kiezen
//   tussen de gemeten route en drie hemelsbreed-varianten. De defaults zijn
//   bewust de bewezen stand van ?v=111: modaliteit + gemeten route.
//
// Verder exact de tekendiscipline van aistracks.js: één lijnobject per been
// (LineSegments doorgetrokken, THREE.Line gestippeld), klemOpHorizon op het
// materiaal, frustumCulled uit.
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
import { kleurVan, beenPunten, grondstofVan, GRONDSTOF_KLEUR } from "./stroomstijl.js?v=117";

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
 *
 * ⚠️ Alleen nodig in `route`-modus: de hemelsbreed-punten uit `beenPunten()`
 * liggen al op de grootcirkel en dragen hun eigen hoogtefactor.
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
                  Math.atan2(z, Math.hypot(x, y)) * 180 / Math.PI, 1]);
      }
    }
    uit.push([punten[i][0], punten[i][1], 1]);
  }
  return uit;
}

/** De punten van een been als [lon, lat, straalfactor], klaar om te tekenen. */
function puntenVoor(been, lijnModus) {
  const p = beenPunten(been, lijnModus);
  return lijnModus === "route" ? verdicht(p) : p;
}

function maakBeen(been, radius, kleur, klemOpHorizon, lijnModus) {
  const punten = puntenVoor(been, lijnModus);
  if (punten.length < 2) return null;   // een been zonder lijnstuk: niets tekenen

  if (been.stippel) {
    // Stippel-been = schematische verbinding (haven-aanloop, last mile),
    // gestippeld getekend als THREE.Line (doorlopende lijn met 2+ punten,
    // géén LineSegments). dash/gap zijn geijkt op de bolschaal: straal 2,4
    // → een been van ~1 km is ~0,0004 scene-eenheden, dus dash/gap ruim
    // daaronder zodat er meerdere streepjes op passen.
    const pos = new Float32Array(punten.length * 3);
    for (let i = 0; i < punten.length; i++) {
      // Punten zijn [lon, lat, straalfactor] — zie het datacontract + stroomstijl.
      opBol(punten[i][0], punten[i][1], radius * punten[i][2], pos, i * 3);
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
    opBol(punten[i][0], punten[i][1], radius * punten[i][2], pos, o);
    opBol(punten[i + 1][0], punten[i + 1][1], radius * punten[i + 1][2], pos, o + 3);
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

// ── De knopen als gloeiende cirkel ─────────────────────────────────────────
//
// De overslag- en eindpunten waren witte stippen van 7 px. Dat is genoeg om een
// punt aan te wijzen tijdens het routewerk, maar het is niet wat de atlas moet
// laten zien: op de referentiebeelden (`design/referenties/`) zijn de knopen
// juist de dragers van het beeld — gloeiende cirkels waar de lijnen samenkomen.
//
// Dit is dezelfde kern/halo-opzet als `gloednodes.js`, en om dezelfde reden:
// een zachte vlek alléén leest als mist (dat kostte op 2026-08-07 drie afgekeurde
// rondes), dus er hoort een felle kern in te zitten die de plek aanwijst.
//
// ⚠️ HORIZON VIA GROOTTE 0, NIET VIA EEN CLIPPINGPLANE — exact het
// gloednodes-argument: een eigen ShaderMaterial zou anders de clipping-chunks
// nodig hebben, en bij een handvol markers is de CPU-toets gratis.
const VERT_M = `
attribute float grootte;
varying vec3 vKleur;
uniform vec3 kleur;
void main() {
  vKleur = kleur;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  gl_PointSize = grootte;
}
`;
const FRAG_M = `
precision highp float;
varying vec3 vKleur;
uniform float alfa;
void main() {
  vec2 p = gl_PointCoord - vec2(0.5);
  float d = length(p) * 2.0;
  if (d > 1.0) discard;
  // ring + kern: de ring maakt er een CIRKEL van (referentiebeeld), de kern
  // houdt de plek exact aanwijsbaar op straatniveau.
  float kern = 1.0 - smoothstep(0.10, 0.30, d);
  float halo = exp(-3.2 * d * d) * 0.42;
  float ring = smoothstep(0.62, 0.74, d) * (1.0 - smoothstep(0.80, 0.94, d)) * 0.55;
  gl_FragColor = vec4(vKleur, clamp(kern + halo + ring, 0.0, 1.0) * alfa);
}
`;

const MARKER = { minPx: 9.0, maxPx: 44.0, wereldKm: 26.0 };

function maakMarkers(markers, radius) {
  if (!markers.length) return null;
  const pos = new Float32Array(markers.length * 3);
  for (let i = 0; i < markers.length; i++) {
    opBol(markers[i].lon, markers[i].lat, radius, pos, i * 3);
  }
  const grootte = new Float32Array(markers.length).fill(MARKER.minPx);
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const attrGr = new THREE.BufferAttribute(grootte, 1);
  attrGr.setUsage(THREE.DynamicDrawUsage);
  geo.setAttribute("grootte", attrGr);

  const mat = new THREE.ShaderMaterial({
    vertexShader: VERT_M, fragmentShader: FRAG_M,
    uniforms: {
      kleur: { value: new THREE.Color(0xffffff) },
      alfa: { value: 0.95 },
    },
    // Normale blending: additief zou de marker juist op de drukste plekken
    // laten opgaan in de lijn eronder — de deeltjes-les van 2026-08-07.
    blending: THREE.NormalBlending, transparent: true,
    depthTest: false, depthWrite: false,
  });
  const punten = new THREE.Points(geo, mat);
  punten.renderOrder = 7.6;   // net boven de benen
  punten.frustumCulled = false;
  return { punten, mat, attrGr, grootte, n: markers.length };
}

export async function laadStroomroute(radius, versie, klemOpHorizon,
                                      bestand = "stroomroute-pilot.json",
                                      camera = null, renderer = null) {
  // ⚠️ Sinds 2026-07-28 draagt deze laag MEER DAN ÉÉN stroom, en daarom is de
  // bestandsnaam een parameter geworden in plaats van vast. Elke stroom is een
  // eigen bestand en een eigen groep, zodat hij los aan/uit kan — precies het
  // patroon van de vijf tracksets in aistracks.js. Eén gedeeld bestand zou de
  // stromen aan elkaar vastklinken en elke nieuwe stroom een herbake van alle
  // andere kosten.
  const r = await fetch(`data/${bestand}?v=${versie}`);
  if (!r.ok) throw new Error(`${bestand}: HTTP ${r.status}`);
  const d = await r.json();

  const stroom = d.stroom || bestand;
  const grondstof = grondstofVan(stroom);

  const groep = new THREE.Group();
  groep.name = `stroomroute-${stroom}`;

  let kleurModus = "modaliteit";
  let lijnModus = "route";

  // ⚠️ NIET FILTEREN op puntenaantal: `maakBeen` geeft zelf null terug bij een
  // been zonder lijnstuk, en de HUD-statistiek (km per modaliteit) hoort over
  // álle benen te lopen — anders zou een been zonder geometrie stil uit de
  // kilometertelling vallen.
  const ruweBenen = d.benen || [];
  let objecten = [];    // parallel aan ruweBenen, null waar niets te tekenen viel

  function bouwLijnen() {
    for (const o of objecten) {
      if (!o) continue;
      groep.remove(o);
      o.geometry.dispose();
      o.material.dispose();
    }
    objecten = ruweBenen.map((been) => {
      const seg = maakBeen(been, radius,
                           kleurVan(been.modaliteit, stroom, kleurModus),
                           klemOpHorizon, lijnModus);
      if (seg) {
        seg.name = `stroomroute-${been.modaliteit}`;
        groep.add(seg);
      }
      return seg;
    });
  }
  bouwLijnen();

  const markerLaag = maakMarkers(d.markers || [], radius);
  if (markerLaag) groep.add(markerLaag.punten);

  function zetMarkerKleur() {
    if (!markerLaag) return;
    // ⚠️ In modaliteitsmodus blijft de marker WIT — dat is de bewezen stand van
    // ?v=111 en de routebouw-weergave is expres onaangeraakt. In de atlasmodus
    // krijgt hij de grondstofkleur, zodat een knoop meteen zegt wélke stroom er
    // samenkomt zonder dat je een lijn hoeft te volgen.
    const k = kleurModus === "grondstof"
      ? (GRONDSTOF_KLEUR[grondstof] ?? 0xffffff)
      : 0xffffff;
    markerLaag.mat.uniforms.kleur.value.setHex(k);
  }
  zetMarkerKleur();

  // Puntgrootte volgt de kijkafstand met een pixel-minimum én -maximum: dichtbij
  // een cirkel óm de site heen (wereldmaat), veraf een leesbare stip die niet
  // verdwijnt. Dezelfde hybride regel als gloednodes.js en de ontwerpbrief.
  const tmp = new THREE.Vector3();
  const camRicht = new THREE.Vector3();
  function update() {
    if (!markerLaag || !groep.visible || !camera || !renderer) return;
    const afstandCam = camera.position.length();
    const horizon = afstandCam > radius ? radius / afstandCam : 1;
    camRicht.copy(camera.position).normalize();
    const h = renderer.domElement.height / (renderer.getPixelRatio() || 1);
    const perEenheid = h / (2 * Math.tan((camera.fov * Math.PI) / 360));
    const wereld = (MARKER.wereldKm / 6371) * radius;
    const pos = markerLaag.punten.geometry.attributes.position.array;
    for (let i = 0; i < markerLaag.n; i++) {
      tmp.set(pos[i * 3], pos[i * 3 + 1], pos[i * 3 + 2]);
      groep.localToWorld(tmp);
      if (tmp.dot(camRicht) / radius < horizon) { markerLaag.grootte[i] = 0; continue; }
      const px = (2 * wereld * perEenheid) / Math.max(1e-6, tmp.distanceTo(camera.position));
      markerLaag.grootte[i] = Math.min(MARKER.maxPx, Math.max(MARKER.minPx, px));
    }
    markerLaag.attrGr.needsUpdate = true;
  }

  return {
    groep,
    update,
    grondstof,
    /** Schakel kleur=modaliteit ↔ kleur=grondstof zonder herladen. */
    zetKleurModus(modus) {
      if (modus === kleurModus) return;
      kleurModus = modus;
      objecten.forEach((o, i) => {
        if (o) o.material.color.setHex(
          kleurVan(ruweBenen[i].modaliteit, stroom, kleurModus));
      });
      zetMarkerKleur();
    },
    /** Schakel tussen de gemeten route en de drie hemelsbreed-varianten. */
    zetLijnModus(modus) {
      if (modus === lijnModus) return;
      lijnModus = modus;
      bouwLijnen();   // de puntentelling verschilt per modus → opnieuw opbouwen
    },
    benen: ruweBenen.map((been) => ({
      modaliteit: been.modaliteit,
      naam: been.naam,
      stippel: !!been.stippel,
      km: been.km,
      punten: (been.punten || []).length,
    })),
    markers: (d.markers || []).map((m) => m.naam),
    titel: d.titel,
    stroom,
    routebrief: d.routebrief || null,
  };
}
