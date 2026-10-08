// stroomkometen.js — de KOMETEN over alle stromen als één Points (golf 1 van
// de visuele fase, 2026-10-08, LAR-617). Gelicht uit stroomleven.js, waar de
// komeet op 2026-08-07 ontstond.
//
// DE LES VAN 2026-08-07, DIE HIER ONGEWIJZIGD GELDT: de lijn geeft geen licht —
// hij is dun, scherp en rustig — en al het licht zit in KOMETEN die eroverheen
// bewegen. De lijn zegt WÁÁR de route ligt, de komeet zegt DÁT er iets overheen
// gaat en HOE SNEL. Een komeet is een KOP (bijna wit, zodat hij tegen élke
// lijnkleur afsteekt — een punt in de lijnkleur is op zijn eigen lijn per
// definitie onzichtbaar) met een staart die terugzakt naar de lijnkleur.
// NORMALE blending: additief telt het deeltje op bij de lijn eronder en dan
// wordt het juist op de drukste plekken onzichtbaar.
//
// De snelheid komt per modaliteit uit een realistische reissnelheid, de
// staartlengte is een FRACTIE van de beenlengte (een zeebeen van 19.000 km en
// een truckbeen van 8 km horen dezelfde vorm te krijgen). Een deeltje is GEEN
// schip en het aantal zegt niets over vrachtvolume; zodra het metadatabestand
// volume per been draagt hoort het aantal daaruit te komen.
//
// WAT GOLF 1 VERANDERDE: één Points voor alle 493 dragers i.p.v. 182 objecten
// en 182 onTick-callbacks; de baan loopt over de GETEKENDE geometrie (fijn
// waar fijn getekend wordt, anders L1), geparametriseerd in ORIGINELE
// cumulatieve km zodat een LOD-wissel geen sprong geeft en de komeet op lokale
// hoogte óp zijn lijn ligt; en drie skip-regels die het beeld niet raken: een
// been dat uit staat, waarvan de kop achter de horizon ligt of dat kleiner dan
// SKIP_PX projecteert, krijgt grootte 0 en slaat de baanberekening over.
// K = 2 kometen per been op desktop, 1 op een telefoon (AFSTEMMING, zodat
// Lars het in één regel terugdraait).

import * as THREE from "three";

// Reissnelheid per modaliteit in km/dag — grof maar realistisch, en het gaat om
// de VERHOUDING: een zeeschip doet er zichtbaar langer over dan een trein.
export const KM_PER_DAG = {
  zee: 700,
  binnenvaart: 250,
  spoor: 500,
  truck: 600,
  leiding: 2000,   // continu proces, leest als een gestage stroom
  lucht: 8000,     // uren waar een schip weken doet; ruim één seconde JNB → Antwerpen
};

export const AFSTEMMING = {
  kometenPerBeenDesktop: 2,
  kometenPerBeenTelefoon: 1,
  staartPunten: 14,        // lengte van de staart in punten
  staartDeelVanBeen: 0.055, // staartlengte als fractie van de beenlengte
  kopMinPx: 6.0,
  kopMaxPx: 17.0,
  tempo: 1.0,              // 1 = één dag reistijd per seconde
  skipPx: 16,              // een been kleiner dan dit op het scherm krijgt geen komeet
};

const VERT = `
attribute float grootte;
attribute float alfa;
attribute vec3 kleur;
varying vec3 vKleur;
varying float vAlfa;
void main() {
  vKleur = kleur;
  vAlfa = alfa;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  gl_PointSize = grootte;
}
`;
// Een HARDE kern (bijna verzadigde schijf tot 45% van de straal) met een korte
// halo eromheen, zodat een deeltje een objectje is en geen wolkje.
const FRAG = `
precision highp float;
varying vec3 vKleur;
varying float vAlfa;
void main() {
  vec2 p = gl_PointCoord - vec2(0.5);
  float d = length(p) * 2.0;
  if (d > 1.0) discard;
  float kern = 1.0 - smoothstep(0.42, 0.62, d);
  float halo = exp(-4.5 * d * d) * 0.45;
  gl_FragColor = vec4(vKleur, clamp(kern + halo, 0.0, 1.0) * vAlfa);
}
`;

/**
 * @param dragers  [{been (globale beenindex), modaliteit}] — de benen die een
 *                 komeet krijgen (niet-stippel). De banen komen later via
 *                 `zetBaan`, zodra de geometrie van dat been bekend is.
 * @param radius   de schil waarop de lijnen liggen
 * @param isAan    (beenIndex) → bool, uit de BeenInfo van de bundel
 * @param telefoon kiest K
 */
export function bouwKometen(dragers, radius, isAan, telefoon, renderOrder = 7.55) {
  const K = telefoon ? AFSTEMMING.kometenPerBeenTelefoon : AFSTEMMING.kometenPerBeenDesktop;
  const T = AFSTEMMING.staartPunten;
  const perKomeet = T + 1;
  const nD = dragers.length;
  const n = Math.max(1, nD * K * perKomeet);

  const dPos = new Float32Array(n * 3);
  const dKleur = new Float32Array(n * 3);
  const dGrootte = new Float32Array(n);
  const dAlfa = new Float32Array(n);
  const fase = new Float32Array(Math.max(1, nD * K));
  const lijnKleur = new Float32Array(nD * 3);      // de lijnkleur per drager (voor kop/staart-menging)
  // baan per drager: plat (xyz), cum (originele km per vertex), totaal (km)
  const banen = dragers.map((d) => ({
    been: d.been, plat: null, cum: null, totaal: 0,
    kmPerDag: KM_PER_DAG[d.modaliteit] ?? 500,
  }));
  const slotVanBeen = new Map();
  dragers.forEach((d, i) => slotVanBeen.set(d.been, i));
  for (let bi = 0; bi < nD; bi++) for (let c = 0; c < K; c++) fase[bi * K + c] = c / K;

  const geo = new THREE.BufferGeometry();
  const attrPos = new THREE.BufferAttribute(dPos, 3); attrPos.setUsage(THREE.DynamicDrawUsage);
  const attrGr = new THREE.BufferAttribute(dGrootte, 1); attrGr.setUsage(THREE.DynamicDrawUsage);
  const attrAlfa = new THREE.BufferAttribute(dAlfa, 1); attrAlfa.setUsage(THREE.DynamicDrawUsage);
  const attrKleur = new THREE.BufferAttribute(dKleur, 3);
  geo.setAttribute("position", attrPos);
  geo.setAttribute("kleur", attrKleur);
  geo.setAttribute("grootte", attrGr);
  geo.setAttribute("alfa", attrAlfa);
  geo.boundingSphere = new THREE.Sphere(new THREE.Vector3(), radius * 2);

  const mat = new THREE.ShaderMaterial({
    vertexShader: VERT, fragmentShader: FRAG,
    blending: THREE.NormalBlending, transparent: true,
    depthTest: false, depthWrite: false,
  });
  const punten = new THREE.Points(geo, mat);
  punten.renderOrder = renderOrder;
  punten.frustumCulled = false;
  punten.name = "kometen";
  const groep = new THREE.Group();
  groep.name = "kometen";
  groep.add(punten);

  const c = new THREE.Color();
  function kleurDrager(bi) {
    const r = lijnKleur[bi * 3], g = lijnKleur[bi * 3 + 1], b = lijnKleur[bi * 3 + 2];
    for (let k = 0; k < K; k++) {
      for (let j = 0; j <= T; j++) {
        const i = (bi * K + k) * perKomeet + j;
        const u = j / T;                       // 0 = kop, 1 = staarteind
        // De KOP is bijna wit; de staart zakt terug naar de lijnkleur, zodat je
        // aan de kleur ziet wát er beweegt.
        const w = (1 - u) * 0.75;
        dKleur[i * 3] = r + (1 - r) * w;
        dKleur[i * 3 + 1] = g + (1 - g) * w;
        dKleur[i * 3 + 2] = b + (1 - b) * w;
      }
    }
  }

  /** De lijnkleur van een been zetten (de bundel roept dit bij elke kleurwissel). */
  function zetKleur(been, hex) {
    const bi = slotVanBeen.get(been);
    if (bi === undefined) return;
    c.setHex(hex);
    lijnKleur[bi * 3] = c.r; lijnKleur[bi * 3 + 1] = c.g; lijnKleur[bi * 3 + 2] = c.b;
    kleurDrager(bi);
  }
  function commitKleur() { attrKleur.needsUpdate = true; }

  /** De baan van een been: `plat` = xyz per vertex (Float32Array), `cum` = de
   *  ORIGINELE cumulatieve km per vertex, zodat L1 en fijn dezelfde fasering
   *  dragen en een wissel geen sprong geeft. */
  function zetBaan(been, plat, cum) {
    const bi = slotVanBeen.get(been);
    if (bi === undefined) return;
    const b = banen[bi];
    b.plat = plat; b.cum = cum; b.totaal = cum.length ? cum[cum.length - 1] : 0;
  }

  // positie op de baan bij km-stand `doel` — binaire zoektocht over cum, zodat
  // een deeltje niet versnelt waar de punten dichter liggen (v1's getPointAt)
  function opBaan(b, doel, uit, o) {
    const cum = b.cum, plat = b.plat;
    let lo = 0, hi = cum.length - 1;
    while (lo + 1 < hi) {
      const mid = (lo + hi) >> 1;
      if (cum[mid] <= doel) lo = mid; else hi = mid;
    }
    const span = cum[hi] - cum[lo];
    const t = span > 0 ? (doel - cum[lo]) / span : 0;
    uit[o] = plat[lo * 3] * (1 - t) + plat[hi * 3] * t;
    uit[o + 1] = plat[lo * 3 + 1] * (1 - t) + plat[hi * 3 + 1] * t;
    uit[o + 2] = plat[lo * 3 + 2] * (1 - t) + plat[hi * 3 + 2] * t;
  }

  const camRicht = new THREE.Vector3();
  let tijd = 0;
  const kop = new Float32Array(3);

  /**
   * @param dt          seconden sinds het vorige frame
   * @param camLocaal   camera in de lokale ruimte van de groep (de bol draait)
   * @param perEenheid  css-px per scene-eenheid op afstand 1
   */
  function update(dt, camLocaal, perEenheid) {
    if (!groep.visible || !nD) return;
    tijd += (dt || 0.016) * AFSTEMMING.tempo;
    const d = camLocaal.length();
    const horizon = d > radius ? radius / d : 1;
    camRicht.copy(camLocaal).normalize();
    const cx = camLocaal.x, cy = camLocaal.y, cz = camLocaal.z;
    const rx = camRicht.x, ry = camRicht.y, rz = camRicht.z;
    const stap = AFSTEMMING.staartDeelVanBeen / T;

    for (let bi = 0; bi < nD; bi++) {
      const b = banen[bi];
      let skip = !b.plat || !(b.totaal > 0) || !isAan(b.been);
      let beenPx = 0;
      if (!skip) {
        // schermgrootte van het been uit zijn uiteinden: te klein → geen komeet
        const n3 = b.plat.length - 3;
        const ax = b.plat[0], ay = b.plat[1], az = b.plat[2];
        const bx = b.plat[n3], by = b.plat[n3 + 1], bz = b.plat[n3 + 2];
        const afstA = Math.max(1e-6, Math.hypot(ax - cx, ay - cy, az - cz));
        beenPx = (Math.hypot(ax - bx, ay - by, az - bz) * perEenheid) / afstA;
        skip = beenPx < AFSTEMMING.skipPx;
      }
      if (skip) {
        for (let k = 0; k < K; k++) for (let j = 0; j <= T; j++) {
          const i = (bi * K + k) * perKomeet + j;
          dGrootte[i] = 0; dAlfa[i] = 0;
        }
        continue;
      }
      // reisduur in dagen = lengte / snelheid; tempo 1 = één dag per seconde
      const duur = b.totaal / b.kmPerDag;
      for (let k = 0; k < K; k++) {
        const f0 = (fase[bi * K + k] + tijd / duur) % 1;
        // horizon-toets op de kop: achter de bol → de hele komeet uit
        opBaan(b, f0 * b.totaal, kop, 0);
        if ((kop[0] * rx + kop[1] * ry + kop[2] * rz) / radius < horizon) {
          for (let j = 0; j <= T; j++) {
            const i = (bi * K + k) * perKomeet + j;
            dGrootte[i] = 0; dAlfa[i] = 0;
          }
          continue;
        }
        const afst = Math.max(1e-6, Math.hypot(kop[0] - cx, kop[1] - cy, kop[2] - cz));
        // dichterbij groter, met een plafond zodat een kop op straatniveau geen
        // schermvullende vlek wordt
        const px = (0.0035 * perEenheid) / afst;
        const kopPx = Math.min(AFSTEMMING.kopMaxPx, Math.max(AFSTEMMING.kopMinPx, px));
        for (let j = 0; j <= T; j++) {
          const i = (bi * K + k) * perKomeet + j;
          const u = j / T;
          const f = f0 - j * stap;
          // Een komeet die net vertrokken is heeft nog geen staart achter zich.
          if (f < 0) { dGrootte[i] = 0; dAlfa[i] = 0; continue; }
          opBaan(b, f * b.totaal, dPos, i * 3);
          dGrootte[i] = kopPx * Math.pow(1 - u, 0.55);
          dAlfa[i] = Math.pow(1 - u, 1.8);
        }
      }
    }
    attrPos.needsUpdate = true;
    attrGr.needsUpdate = true;
    attrAlfa.needsUpdate = true;
  }

  return {
    groep, punten, update, zetBaan, zetKleur, commitKleur,
    stats: { dragers: nD, kometen: nD * K, punten: n, K },
  };
}
