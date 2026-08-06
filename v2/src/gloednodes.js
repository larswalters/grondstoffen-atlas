// gloednodes.js — de uitgezochte knopen als ADDITIEVE GLOED (M26 / LAR-490).
//
// Dit is de dichtbij-helft van het LOD-ontwerp: klopt de gloed als je op één
// complex staat en er zes echte faciliteiten naast elkaar liggen? De veraf-helft
// (wat tientallen fabrieken en overslagpunten sámen doen) komt vanzelf zodra er
// meer grondstoffen op dezelfde plekken uitkomen.
//
// ⚠️ DE WERELD-HOTSPOT IS GEEN APART OBJECT. Dat is de kern van de ontwerpbrief:
// er wordt níets geaggregeerd getekend. Alleen de SITES krijgen een glow-bol; de
// complex- en regioknopen in gloednodes-koper.json zijn er voor labels, interactie
// en flow-aggregatie en worden hier bewust overgeslagen. Dat twaalf fabrieken bij
// Tongling op wereldniveau één heldere vlek worden moet ONTSTAAN uit de optelling,
// niet uit een knoop die we zelf hebben voorgekookt. Ziet het er van veraf goed
// uit, dan klopt het mechanisme; moeten we alsnog een hotspot-object tekenen, dan
// klopt de brief niet — en dát is wat deze laag toetst.
//
// HET MECHANISME. De glow-radius schaalt mee met de kijkafstand via dezelfde
// hybride regel die de brief voor lijndikte kiest: een echte wereldmaat (meters,
// op capaciteit) MET een pixel-minimum. Dichtbij wint de wereldmaat → elke
// faciliteit een eigen scherpe bol. Veraf zakt die onder het minimum → alle
// sites worden even groot, buren van 3 km vallen op dezelfde pixels en tellen
// additief op. Het is dus één formule die twee gedragingen geeft; er zit geen
// zoomdrempel of crossfade in, en daarom kan er per constructie geen pop-in zijn.
//
// Zonder pixel-minimum zou een fabriek van 2 km op wereldhoogte kleiner dan een
// pixel worden en simpelweg verdwijnen — dan is er niets om op te tellen en kan
// de hotspot niet ontstaan. Dat minimum ÍS het mechanisme, geen ondergrens tegen
// onzichtbaarheid.
//
// Tekendiscipline zoals de andere vectorlagen: depthTest uit + renderOrder boven
// de tegels. De horizon wordt hier NIET met een clippingPlane gedaan maar door de
// puntgrootte op 0 te zetten — bij 36 punten is dat CPU-werk verwaarloosbaar, en
// het scheelt de clipping-chunks die een eigen ShaderMaterial anders nodig heeft.

import * as THREE from "three";

// Grondstofkleuren, gelijk aan data/<grondstof>.js in de v1-atlas — de gloed
// hoort dezelfde taal te spreken als de rest van de atlas.
const KLEUR = {
  koper: [0xC8 / 255, 0x7D / 255, 0x4A / 255],
  lithium: [0x4F / 255, 0xD1 / 255, 0xC5 / 255],
};
const KLEUR_ONBEKEND = [0.75, 0.75, 0.75];

// Afstemknoppen. Bewust hier en niet in CONFIG: dit is een pilotlaag en deze drie
// getallen zijn precies wat je tijdens het kijken wilt kunnen draaien.
export const AFSTEMMING = {
  kmPerWortelGewicht: 0.30, // straal in km = dit × √gewicht (g=100 → 3,0 km)
  minPx: 34.0,              // pixel-minimum: hieronder wint het scherm van de wereld
  sterkte: 0.30,            // per schil BEWUST zwak — de optelling maakt hem fel
  koepelHoogte: 2.6,        // koepelhoogte = dit × de wereldstraal van de site
};

// ✅ BESLUIT LARS (2026-08-06): de gloed wordt een KOEPEL met hoogte, geen platte
// schijf. Elke schil is dezelfde puntenwolk, opgetild en smaller gemaakt volgens
// een halve bol (breedte = √(1−u²)); additief opgeteld leest dat als één volume
// dat boven het terrein uitsteekt.
//
// ⚠️ DIT IS GEEN OMKERING VAN BESLUIT 2 UIT DE ONTWERPBRIEF. Dat besluit zegt
// "glow-bollen, géén hoogte-pilaren" en gaat over CAPACITEIT-ALS-HOOGTE — een
// staaf waarvan je de lengte moet aflezen. Hier draagt de hoogte geen betekenis:
// de koepel is even hoog als hij breed is, dus capaciteit blijft in de grootte
// zitten en de hoogte is puur volume. Wie hem later tóch op volume laat groeien,
// heeft besluit 2 wél omgedraaid en hoort dat op te schrijven.
//
// [u = fractie van de koepelhoogte, breedtefactor, helderheidsfactor]
const SCHILLEN = [
  [0.00, 1.00, 0.62],
  [0.34, 0.94, 0.34],
  [0.62, 0.78, 0.22],
  [0.84, 0.54, 0.14],
  [0.96, 0.28, 0.08],
];

const AARDSTRAAL_KM = 6371;

function opBol(lonDeg, latDeg, r) {
  // Exact dezelfde afspraak als world.js/aisgloed.js (z = −sin lon).
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  return [r * c * Math.cos(lon), r * Math.sin(lat), -r * c * Math.sin(lon)];
}

const VERT = `
attribute float grootte;
attribute float helder;
attribute vec3 kleur;
varying float vHelder;
varying vec3 vKleur;
void main() {
  vHelder = helder;
  vKleur = kleur;
  vec4 mv = modelViewMatrix * vec4(position, 1.0);
  gl_Position = projectionMatrix * mv;
  gl_PointSize = grootte;
}
`;

// Kern + halo, allebei gaussisch. De halo is breed en zwak (die doet het
// optelwerk tussen buren), de kern smal en fel (die maakt één faciliteit
// herkenbaar zodra je er bovenop staat).
const FRAG = `
precision highp float;
varying float vHelder;
varying vec3 vKleur;
void main() {
  vec2 p = gl_PointCoord - vec2(0.5);
  float d = length(p) * 2.0;
  if (d > 1.0) discard;
  float halo = exp(-2.2 * d * d);
  float kern = exp(-18.0 * d * d);
  float i = (halo * 0.62 + kern * 0.8) * vHelder;
  gl_FragColor = vec4(vKleur, i);
}
`;

export async function laadGloednodes(radius, versie, camera, renderer) {
  const t0 = performance.now();
  const r = await fetch(`data/gloednodes-koper.json?v=${versie}`);
  if (!r.ok) throw new Error(`gloednodes-koper.json: HTTP ${r.status}`);
  const doc = await r.json();
  const tLaden = performance.now();

  // ⚠️ Alleen sites. Zie de kop: complex/regio zijn labels, geen glow-objecten.
  const sites = doc.knopen.filter((k) => k.level === "site");
  if (!sites.length) throw new Error("gloednodes: geen sites in het bestand");

  const n = sites.length;
  const maxGewicht = Math.max(...sites.map((s) => s.gewicht || 1));
  // wereldstraal en koepelhoogte per site, in globe-eenheden, uit het gewicht
  const straal = new Float32Array(n);
  const kleur = new Float32Array(n * 3);
  const basisHelder = new Float32Array(n);
  const lonlat = [];

  sites.forEach((s, i) => {
    const g = Math.max(1, s.gewicht || 1);
    const km = AFSTEMMING.kmPerWortelGewicht * Math.sqrt(g);
    straal[i] = (km / AARDSTRAAL_KM) * radius;
    lonlat.push([s.lon, s.lat]);

    // Capaciteit is het gewicht in de optelling (besluit 2 uit de brief): hij
    // stuurt zowel de wereldmaat hierboven als de helderheid. Zonder dat tweede
    // zouden op wereldhoogte — waar iedereen op het pixel-minimum zit — alleen
    // AANTALLEN nog tellen en zou een smelter van 1,2 Mt/j even zwaar wegen als
    // een staalbouwer ernaast.
    basisHelder[i] = 0.28 + 0.72 * Math.sqrt(g / maxGewicht);

    const c = KLEUR[(s.grondstof || [])[0]] || KLEUR_ONBEKEND;
    kleur[i * 3] = c[0]; kleur[i * 3 + 1] = c[1]; kleur[i * 3 + 2] = c[2];
  });

  const groep = new THREE.Group();
  const schillen = [];   // {pos, grootte, attrGrootte, breedte}

  SCHILLEN.forEach(([u, breedteF, helderF], si) => {
    const pos = new Float32Array(n * 3);
    const helder = new Float32Array(n);
    const grootte = new Float32Array(n);

    for (let i = 0; i < n; i++) {
      // De schil ligt op u × koepelhoogte boven het oppervlak.
      const hoogte = AFSTEMMING.koepelHoogte * straal[i] * u;
      const [x, y, z] = opBol(lonlat[i][0], lonlat[i][1], radius + hoogte);
      pos[i * 3] = x; pos[i * 3 + 1] = y; pos[i * 3 + 2] = z;
      helder[i] = basisHelder[i] * helderF * AFSTEMMING.sterkte;
    }

    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    geo.setAttribute("kleur", new THREE.BufferAttribute(kleur, 3));
    geo.setAttribute("helder", new THREE.BufferAttribute(helder, 1));
    const attrGrootte = new THREE.BufferAttribute(grootte, 1);
    attrGrootte.setUsage(THREE.DynamicDrawUsage);
    geo.setAttribute("grootte", attrGrootte);

    const mat = new THREE.ShaderMaterial({
      vertexShader: VERT,
      fragmentShader: FRAG,
      blending: THREE.AdditiveBlending,
      transparent: true,
      depthTest: false,
      depthWrite: false,
    });

    const punten = new THREE.Points(geo, mat);
    // Hoger in de koepel = later tekenen, zodat de top bovenop de basis ligt.
    punten.renderOrder = 7.6 + si * 0.001;
    punten.frustumCulled = false;   // wij bepalen zichtbaarheid zelf, per punt
    groep.add(punten);
    schillen.push({ pos, grootte, attrGrootte, breedte: breedteF });
  });

  // --- de per-frame maatregel ------------------------------------------------
  const wereldPos = new THREE.Vector3();
  const camRicht = new THREE.Vector3();

  function update() {
    if (!groep.visible) return;
    const d = camera.position.length();
    if (d <= radius) return;
    // Zichtbaarheidsgrens op een bol: een punt p̂ is zichtbaar vanaf een camera op
    // afstand d als dot(p̂, ĉ) ≥ R/d. Exact, op elke hoogte, zonder drempel.
    const horizon = radius / d;
    camRicht.copy(camera.position).normalize();

    // pixels per globe-eenheid op afstand 1, uit de projectie
    const h = renderer.domElement.height / (renderer.getPixelRatio() || 1);
    const perEenheid = h / (2 * Math.tan((camera.fov * Math.PI) / 360));

    for (const sch of schillen) {
      for (let i = 0; i < n; i++) {
        wereldPos.set(sch.pos[i * 3], sch.pos[i * 3 + 1], sch.pos[i * 3 + 2]);
        groep.localToWorld(wereldPos);

        if (wereldPos.dot(camRicht) / radius < horizon) {
          sch.grootte[i] = 0;   // achterkant van de bol
          continue;
        }
        const afstand = wereldPos.distanceTo(camera.position);
        const wereldPx = (2 * straal[i] * perEenheid) / Math.max(1e-6, afstand);
        // ⚠️ De breedtefactor hoort ÓÓK op het pixel-minimum te werken, niet
        // alleen op de wereldmaat. Anders wordt de koepel op wereldhoogte een
        // stapel even brede schijven — dus een pilaar in plaats van een koepel,
        // en precies daar zit de meeste kijktijd.
        sch.grootte[i] = Math.max(AFSTEMMING.minPx * sch.breedte,
                                  wereldPx * sch.breedte);
      }
      sch.attrGrootte.needsUpdate = true;
    }
  }

  return {
    groep,
    update,
    sites,
    stats: {
      sites: n,
      schillen: SCHILLEN.length,
      complexen: doc.knopen.filter((k) => k.level === "complex").length,
      msLaden: Math.round(tLaden - t0),
      msVerwerken: Math.round(performance.now() - tLaden),
    },
  };
}
