// gloed.js — het GLOED-MECHANISME, losgemaakt van zijn eerste gebruiker.
//
// Waarom dit bestaat: `gloednodes.js` bouwde de koepel-gloed voor de 36
// uitgezochte kopersites, en op 2026-08-07 vroeg Lars om ook de belangrijke
// punten van een stroom (mijn · overslag · fabriek) zo te laten oplichten —
// *"die witte ballen met cirkel erom moeten eigenlijk de gloedbron worden … zowel
// stroom, gloed als die belangrijke punten moeten die gloeihotspots worden."*
// Dat is één mechanisme met twee bronnen, dus het mechanisme hoort hier en niet
// in een van de twee.
//
// ⚠️ EN HET IS OOK EEN INHOUDELIJK PUNT, GEEN OPRUIMING. De ontwerpbrief zegt dat
// de wereld-hotspot moet **ONTSTAAN** uit de optelling van losse glows. Zolang
// alleen `gloednodes-koper.json` gloeide, kon dat alleen in China gebeuren — daar
// staan de enige uitgezochte sites. Met de stroomknopen erbij lichten Balama,
// Nacala, Vidalia, Greenbushes, Lobito en Duisburg óók op, en telt de gloed op
// waar een stroom door een complex loopt. Dat is de eerste keer dat de
// optel-claim buiten één land te toetsen is.
//
// HET MECHANISME (ongewijzigd overgenomen uit gloednodes.js, waar het is bewezen):
// de glow-radius schaalt mee met de kijkafstand via een hybride regel — een echte
// wereldmaat (meters, uit het gewicht) MET een pixel-minimum. Dichtbij wint de
// wereldmaat → elke faciliteit een eigen scherpe bol. Veraf zakt die onder het
// minimum → alle knopen worden even groot, buren van 3 km vallen op dezelfde
// pixels en tellen additief op. Eén formule, twee gedragingen, geen zoomdrempel
// en dus per constructie geen pop-in.
//
// Zonder pixel-minimum zou een fabriek van 2 km op wereldhoogte kleiner dan een
// pixel worden en simpelweg verdwijnen — dan is er niets om op te tellen en kan
// de hotspot niet ontstaan. Dat minimum ÍS het mechanisme, geen ondergrens tegen
// onzichtbaarheid.
//
// ⚠️ HORIZON VIA GROOTTE 0, NIET VIA EEN CLIPPINGPLANE — een eigen ShaderMaterial
// zou anders de clipping-chunks nodig hebben, en bij enkele tientallen punten is
// de CPU-toets gratis.

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
// ⚠️ DIT IS GEEN OMKERING VAN BESLUIT 2 UIT DE ONTWERPBRIEF. Dat besluit zegt
// "glow-bollen, géén hoogte-pilaren" en gaat over CAPACITEIT-ALS-HOOGTE — een
// staaf waarvan je de lengte moet aflezen. Hier draagt de hoogte geen betekenis:
// de koepel is even hoog als hij breed is, dus capaciteit blijft in de grootte
// zitten en de hoogte is puur volume. Wie hem later tóch op volume laat groeien,
// heeft besluit 2 wél omgedraaid en hoort dat op te schrijven.
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

/** Bouw een gloedlaag.
 *
 * @param knopen  [{lon, lat, straalKm, kleur (0xRRGGBB), helder (0..1)}]
 * @param radius  de schil waarop de laag ligt (CONFIG.vectorLift-schil)
 * @param camera/renderer  nodig voor de per-frame pixelmaat
 * @param renderOrder  basis; elke schil telt er 0,001 bij op
 * @returns {groep, update, zetKleur, aantal}
 */
export function bouwGloed(knopen, radius, camera, renderer, renderOrder = 7.6) {
  const n = knopen.length;
  const groep = new THREE.Group();
  if (!n) return { groep, update() {}, zetKleur() {}, aantal: 0 };

  const straal = new Float32Array(n);
  const kleur = new Float32Array(n * 3);
  const c = new THREE.Color();

  knopen.forEach((k, i) => {
    straal[i] = (k.straalKm / AARDSTRAAL_KM) * radius;
    c.setHex(k.kleur);
    kleur[i * 3] = c.r; kleur[i * 3 + 1] = c.g; kleur[i * 3 + 2] = c.b;
  });

  const schillen = [];   // {pos, grootte, attrGrootte, attrKleur, breedte}

  SCHILLEN.forEach(([u, breedteF, helderF], si) => {
    const pos = new Float32Array(n * 3);
    const helder = new Float32Array(n);
    const grootte = new Float32Array(n);
    const kl = kleur.slice();   // elke schil een eigen buffer, zodat zetKleur werkt

    for (let i = 0; i < n; i++) {
      // De schil ligt op u × koepelhoogte boven het oppervlak.
      const hoogte = AFSTEMMING.koepelHoogte * straal[i] * u;
      const [x, y, z] = opBol(knopen[i].lon, knopen[i].lat, radius + hoogte);
      pos[i * 3] = x; pos[i * 3 + 1] = y; pos[i * 3 + 2] = z;
      helder[i] = (knopen[i].helder ?? 1) * helderF * AFSTEMMING.sterkte;
    }

    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const attrKleur = new THREE.BufferAttribute(kl, 3);
    geo.setAttribute("kleur", attrKleur);
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
    punten.renderOrder = renderOrder + si * 0.001;
    punten.frustumCulled = false;   // wij bepalen zichtbaarheid zelf, per punt
    groep.add(punten);
    schillen.push({ pos, grootte, attrGrootte, attrKleur, breedte: breedteF });
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

  /** Alle knopen in één keer omkleuren (voor de kleurmodus-schakelaar). */
  function zetKleur(hex) {
    c.setHex(hex);
    for (const sch of schillen) {
      const a = sch.attrKleur.array;
      for (let i = 0; i < n; i++) {
        a[i * 3] = c.r; a[i * 3 + 1] = c.g; a[i * 3 + 2] = c.b;
      }
      sch.attrKleur.needsUpdate = true;
    }
  }

  return { groep, update, zetKleur, aantal: n };
}
