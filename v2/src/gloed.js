// gloed.js — het GLOED-MECHANISME, sinds golf 1 van de visuele fase als ÉÉN
// object voor alle knopen samen (2026-10-08, LAR-617).
//
// Waarom dit bestaat: de oude gloedknopenlaag (tot ?v=131) bouwde de koepel-
// gloed voor de 36 uitgezochte kopersites, en op 2026-08-07 vroeg Lars om ook
// de belangrijke punten van een stroom (mijn · overslag · fabriek) zo te laten
// oplichten —
// *"die witte ballen met cirkel erom moeten eigenlijk de gloedbron worden … zowel
// stroom, gloed als die belangrijke punten moeten die gloeihotspots worden."*
// Dat is één mechanisme met twee bronnen, dus het mechanisme hoort hier.
//
// ⚠️ EN HET IS OOK EEN INHOUDELIJK PUNT, GEEN OPRUIMING. De ontwerpbrief zegt dat
// de wereld-hotspot moet **ONTSTAAN** uit de optelling van losse glows. Met de
// stroomknopen erbij lichten Balama, Nacala, Vidalia, Greenbushes, Lobito en
// Duisburg óók op, en telt de gloed op waar een stroom door een complex loopt.
//
// HET MECHANISME (ongewijzigd en bewezen in de oude gloedknopenlaag): de
// glow-radius schaalt mee met de kijkafstand via een hybride regel — een echte
// wereldmaat (meters, uit het gewicht) MET een pixel-minimum. Dichtbij wint de
// wereldmaat → elke faciliteit een eigen scherpe bol. Veraf zakt die onder het
// minimum → alle knopen worden even groot, buren van 3 km vallen op dezelfde
// pixels en tellen additief op. Eén formule, twee gedragingen, geen zoomdrempel
// en dus per constructie geen pop-in. Zonder pixel-minimum zou een fabriek van
// 2 km op wereldhoogte kleiner dan een pixel worden en verdwijnen — dat minimum
// ÍS het mechanisme, geen ondergrens tegen onzichtbaarheid.
//
// ⚠️ WAT ER IN GOLF 1 VERANDERDE IS ALLEEN DE IMPLEMENTATIE. ?v=131 had per
// bron een eigen groep van vijf Points (182 stromen + 14 sitelagen = 1.164
// objecten in atlasmodus). Nu liggen de vijf schillen van ALLE knopen als
// vertex-reeksen in één Points (additief is commutatief, dus de tekenvolgorde
// binnen de koepel draagt niets). AFSTEMMING, SCHILLEN en de shader zijn
// letterlijk hetzelfde; de per-frame maat blijft in JS (gemeten < 0,3 ms voor
// alle knopen — de winst zat nooit in die lus maar in de objecten). De camera
// komt binnen in GROEP-LOKALE ruimte (de bol draait, de camera staat vast), dus
// er is geen localToWorld per punt meer. Sinds stap 4 van golf 1 is dit de
// enige aanroepvorm: de oude per-stroom-lagen en hun compatibiliteitstak zijn weg.
//
// ⚠️ HORIZON VIA GROOTTE 0, NIET VIA EEN CLIPPINGPLANE — een eigen ShaderMaterial
// zou anders de clipping-chunks nodig hebben, en de CPU-toets is gratis.

import * as THREE from "three";

export const AARDSTRAAL_KM = 6371;

// Afstemknoppen, gedeeld door beide bronnen zodat een stroomknoop en een
// registersite met hetzelfde gewicht ook even groot zijn.
export const AFSTEMMING = {
  minPx: 34.0,          // pixel-minimum: hieronder wint het scherm van de wereld
  sterkte: 0.30,        // per schil BEWUST zwak — de optelling maakt hem fel
  koepelHoogte: 2.6,    // koepelhoogte = dit × de wereldstraal van de knoop
};

// ✅ BESLUIT LARS (2026-08-06): de gloed is een KOEPEL met hoogte, geen platte
// schijf. Elke schil is dezelfde puntenwolk, opgetild en smaller gemaakt volgens
// een halve bol (breedte = √(1−u²)); additief opgeteld leest dat als één volume
// dat boven het terrein uitsteekt.
//
// ⚠️ DIT IS GEEN OMKERING VAN BESLUIT 2 UIT DE ONTWERPBRIEF ("glow-bollen, géén
// hoogte-pilaren" = capaciteit-als-hoogte). Hier draagt de hoogte geen betekenis:
// de koepel is even hoog als hij breed is, capaciteit blijft in de grootte.
//
// [u = fractie van de koepelhoogte, breedtefactor, helderheidsfactor]
export const SCHILLEN = [
  [0.00, 1.00, 0.62],
  [0.34, 0.94, 0.34],
  [0.62, 0.78, 0.22],
  [0.84, 0.54, 0.14],
  [0.96, 0.28, 0.08],
];

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

/** Bouw de gloedlaag als één Points.
 *
 * @param knopen  [{lon, lat, straalKm, kleur (0xRRGGBB), helder (0..1)}]
 * @param radius  de schil waarop de laag ligt (CONFIG.vectorLift-schil)
 * @param renderOrder
 * @returns {groep, punten, update(camLocaal, perEenheid), zetAan(i, aan),
 *           zetKleur(i, hex), aantal}
 *
 * `update` wil de camera in de LOKALE ruimte van de groep waarin deze laag
 * hangt (globeGroup): één inverse matrix per frame bij de aanroeper, geen
 * localToWorld per punt. `perEenheid` = pixels per scene-eenheid op afstand 1
 * (h / (2·tan(fov/2)), met h = css-hoogte — zoals de oude gloedknopenlaag hem
 * altijd gaf).
 */
export function bouwGloed(knopen, radius, renderOrder = 7.6) {
  const n = knopen.length;
  const groep = new THREE.Group();
  groep.name = "gloed";
  if (!n) return { groep, punten: null, update() {}, zetAan() {}, zetKleur() {}, commitKleur() {}, aantal: 0 };

  const S = SCHILLEN.length;
  const straal = new Float32Array(n);
  const aan = new Uint8Array(n).fill(1);
  const pos = new Float32Array(n * S * 3);
  const kleur = new Float32Array(n * S * 3);
  const helder = new Float32Array(n * S);
  const breedte = new Float32Array(n * S);   // breedtefactor van de schil, per vertex
  const grootte = new Float32Array(n * S);
  const c = new THREE.Color();

  knopen.forEach((k, i) => {
    straal[i] = (k.straalKm / AARDSTRAAL_KM) * radius;
    c.setHex(k.kleur);
    SCHILLEN.forEach(([u, breedteF, helderF], si) => {
      const v = si * n + i;                      // schil-major: alle knopen van schil 0, dan schil 1, …
      const hoogte = AFSTEMMING.koepelHoogte * straal[i] * u;
      const [x, y, z] = opBol(k.lon, k.lat, radius + hoogte);
      pos[v * 3] = x; pos[v * 3 + 1] = y; pos[v * 3 + 2] = z;
      kleur[v * 3] = c.r; kleur[v * 3 + 1] = c.g; kleur[v * 3 + 2] = c.b;
      helder[v] = (k.helder ?? 1) * helderF * AFSTEMMING.sterkte;
      breedte[v] = breedteF;
    });
  });

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const attrKleur = new THREE.BufferAttribute(kleur, 3);
  geo.setAttribute("kleur", attrKleur);
  geo.setAttribute("helder", new THREE.BufferAttribute(helder, 1));
  const attrGrootte = new THREE.BufferAttribute(grootte, 1);
  attrGrootte.setUsage(THREE.DynamicDrawUsage);
  geo.setAttribute("grootte", attrGrootte);
  geo.boundingSphere = new THREE.Sphere(new THREE.Vector3(), radius * 2);

  const mat = new THREE.ShaderMaterial({
    vertexShader: VERT, fragmentShader: FRAG,
    blending: THREE.AdditiveBlending, transparent: true,
    depthTest: false, depthWrite: false,
  });
  const punten = new THREE.Points(geo, mat);
  punten.renderOrder = renderOrder;
  punten.frustumCulled = false;      // wij bepalen zichtbaarheid zelf, per punt
  punten.name = "gloed";
  groep.add(punten);

  // --- de per-frame maatregel ------------------------------------------------
  const camRicht = new THREE.Vector3();
  function update(camLocaal, perEenheid) {
    if (!groep.visible) return;
    const d = camLocaal.length();
    if (d <= radius) return;
    // Zichtbaarheidsgrens op een bol: een punt p̂ is zichtbaar vanaf een camera op
    // afstand d als dot(p̂, ĉ) ≥ R/d. Exact, op elke hoogte, zonder drempel.
    const horizon = radius / d;
    camRicht.copy(camLocaal).normalize();
    const cx = camLocaal.x, cy = camLocaal.y, cz = camLocaal.z;
    const rx = camRicht.x, ry = camRicht.y, rz = camRicht.z;
    for (let i = 0; i < n; i++) {
      // horizon- en afstandstoets op de basisschil; de koepel erboven volgt
      const px = pos[i * 3], py = pos[i * 3 + 1], pz = pos[i * 3 + 2];
      const zichtbaar = aan[i] && (px * rx + py * ry + pz * rz) / radius >= horizon;
      if (!zichtbaar) {
        for (let si = 0; si < S; si++) grootte[si * n + i] = 0;
        continue;
      }
      const afstand = Math.max(1e-6, Math.hypot(px - cx, py - cy, pz - cz));
      const wereldPx = (2 * straal[i] * perEenheid) / afstand;
      for (let si = 0; si < S; si++) {
        const v = si * n + i;
        // ⚠️ De breedtefactor hoort ÓÓK op het pixel-minimum te werken, niet
        // alleen op de wereldmaat. Anders wordt de koepel op wereldhoogte een
        // stapel even brede schijven — een pilaar in plaats van een koepel.
        grootte[v] = Math.max(AFSTEMMING.minPx * breedte[v], wereldPx * breedte[v]);
      }
    }
    attrGrootte.needsUpdate = true;
  }

  function zetAan(i, waarde) { aan[i] = waarde ? 1 : 0; }

  /** Eén knoop omkleuren (alle vijf schillen). Roep daarna `commitKleur()` aan. */
  function zetKleur(i, hex) {
    c.setHex(hex);
    for (let si = 0; si < S; si++) {
      const v = si * n + i;
      kleur[v * 3] = c.r; kleur[v * 3 + 1] = c.g; kleur[v * 3 + 2] = c.b;
    }
  }
  function commitKleur() { attrKleur.needsUpdate = true; }

  return { groep, punten, update, zetAan, zetKleur, commitKleur, aantal: n };
}
