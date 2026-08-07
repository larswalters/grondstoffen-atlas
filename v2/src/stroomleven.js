// stroomleven.js — de stromen laten LEVEN: een lichtgevende koker boven de
// gemeten lijn, plus deeltjes die er als schepen overheen bewegen (M26/LAR-490).
//
// ✅ BESLUIT LARS (2026-08-06): de lijnen blijven op de grond. V1's bogen vlogen
// 22% van de bolstraal de lucht in en dat was mooi, maar geografisch verzonnen;
// v2 heeft er M23–M28 over gedaan om ze op de échte zeeroute, het échte spoor en
// de échte weg te krijgen. Het 3D-gevoel komt daarom NIET uit het optillen van de
// route, maar uit een gloed-koker ERBOVEN plus beweging. Elke meter blijft kloppen.
//
// ⚠️ DEZE LAAG RAAKT `stroomroute.js` NIET AAN. Die tekent de dunne, exacte lijn
// in de modaliteitskleur en is bewezen (v=111, vijf stromen, 0 console-fouten);
// wat hier bijkomt ligt eromheen. Zou de koker de lijn vervangen, dan zou een
// visuele bijstelling stilzwijgend de legenda-kleur en de gemeten geometrie
// kunnen verschuiven — precies de klasse fouten die dit project al twee keer
// heeft opgelost ("de legenda loog", generator↔uitvoer-drift).
//
// DE KOKER is opgebouwd uit een paar schillen op oplopende hoogte met aflopende
// breedte en helderheid. Additief opgeteld leest dat als één volume dat boven de
// route hangt. Geen enkele schil draagt betekenis: de betekenis zit in de dunne
// lijn eronder. De breedte staat in PIXELS (LineMaterial met worldUnits=false),
// want een lijn van echte meters is op wereldhoogte onzichtbaar en op straat-
// niveau een muur — dat is dezelfde hybride regel die de ontwerpbrief voor
// lijndikte kiest en die `gloednodes.js` voor de gloed gebruikt.
//
// DE DEELTJES zijn niet decoratief. Hun snelheid komt per modaliteit uit een
// realistische reissnelheid, en hun onderlinge afstand uit de beenlengte, zodat
// een zeebeen van 19.000 km er zichtbaar langer over doet dan een truckbeen van
// 8 km. Dat is het v1-principe uit `voyages.js` (afvaarten volgen uit volume,
// reisduur uit lengte), hier in de eenvoudigste vorm die op de gebakken stromen
// past — de volumes per been zitten nog niet in `stroomroute-*.json`.
//
// ⚠️ Wat hier NIET gebeurt: een deeltje is GEEN schip en het aantal zegt niets
// over vrachtvolume. Zodra het losse metadatabestand naast stroomroute-*.json er
// is (met volume per been) hoort dit die getallen te lezen; tot dan is de
// beweging waar en het aantal een keuze.

import * as THREE from "three";
import { Line2 } from "three/addons/lines/Line2.js";
import { LineGeometry } from "three/addons/lines/LineGeometry.js";
import { LineMaterial } from "three/addons/lines/LineMaterial.js";
import { kleurVan, beenPunten } from "./stroomstijl.js?v=118";

// ⚠️ DE KLEURTABEL STOND HIER OOK, EN DAT WAS DE FOUT. Twee kopieën van dezelfde
// legenda (hier en in stroomroute.js) lopen vroeg of laat uit elkaar; sinds
// 2026-08-07 leest deze laag `stroomstijl.js`, samen met de exacte lijn en de
// gloedknopen. Draad en komeet hebben per constructie dezelfde kleur als de
// lijn waar ze op lopen — ook nadat je op grondstofkleur omschakelt.

// Reissnelheid per modaliteit in km/dag — grof maar realistisch, en het gaat om
// de VERHOUDING: een zeeschip doet er zichtbaar langer over dan een trein.
const KM_PER_DAG = {
  zee: 700,
  binnenvaart: 250,
  spoor: 500,
  truck: 600,
  leiding: 2000,   // continu proces, leest als een gestage stroom
};

// ⚠️ EERSTE VERSIE WAS ALLEEN RAND EN GEEN LIJN. Drie zachte additieve schillen
// (9 · 6,5 · 4 px op oplopende hoogte) leverden een wolk op waarin de exacte
// lijn van 1 px volledig verdween — Lars: "dit ziet er wel een beetje vaag uit".
// Additief opgeteld verkleurde het bovendien naar wit, dus ook de modaliteits-
// kleur ging eraan. V1 doet het andersom: een STEVIGE KERN met een subtiele
// gloed eromheen. Vandaar de opzet hieronder — de kern draagt het beeld, de
// halo's zijn duidelijk ondergeschikt en de hoogte zit op één schil in plaats
// van op alle drie (drie hoogtes lezen onder een schuine hoek als drie losse
// linten, en dát is de mist).
//
// ⚠️ TWEEDE CORRECTIE, EN NU AAN DE OPZET IN PLAATS VAN AAN DE GETALLEN. Ook
// mét kern bleef het oordeel "de lijnen zien er uit als één grote gloed": een
// halo van 16 px om een kern van 2,4 px ís een gloed, hoe je hem ook afstemt.
// De denkfout was dat de LIJN het licht moest geven. Nu geeft de lijn geen licht
// meer — hij is dun, scherp en rustig, als een draad op de kaart — en al het
// licht zit in KOMETEN die eroverheen bewegen. Dat scheidt de twee taken die
// door elkaar liepen: de lijn zegt WAAR de route ligt, de kometen zeggen DAT er
// iets over beweegt en hoe snel. Precies de ontkoppeling die dit project in juli
// al eens moest maken tussen vorm, vaarsnelheid en baanklem.
//
// [hoogte in km, breedte in px, opacity, additief?]
const SCHILLEN = [
  [0.0, 3.6, 0.13, true],     // één krappe halo, alleen om de kern lucht te geven
  [0.0, 1.7, 0.88, false],    // DE DRAAD: dun, scherp, volle modaliteitskleur
];

const AARDSTRAAL_KM = 6371;

export const AFSTEMMING = {
  kometenPerBeen: 2,       // hoeveel kometen tegelijk over één been
  staartPunten: 14,        // lengte van de staart in punten
  staartDeelVanBeen: 0.055, // staartlengte als fractie van de beenlengte
  kopMinPx: 6.0,
  kopMaxPx: 17.0,
  tempo: 1.0,              // 1 = één dag reistijd per seconde
};

function opBol(lonDeg, latDeg, r) {
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  return [r * c * Math.cos(lon), r * Math.sin(lat), -r * c * Math.sin(lon)];
}

// Grootcirkelafstand in km — voor de booglengte waarop de deeltjes lopen.
function gcKm(a, b) {
  const R = 6371, t = Math.PI / 180;
  const dLat = (b[1] - a[1]) * t, dLon = (b[0] - a[0]) * t;
  const s = Math.sin(dLat / 2) ** 2 +
    Math.cos(a[1] * t) * Math.cos(b[1] * t) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.min(1, Math.sqrt(s)));
}

const VERT_D = `
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
// ⚠️ Een zachte gaussische vlek gaat op in de gloed van de lijn waar hij op
// loopt — dan zie je wel iets bewegen maar niets afsteken. Daarom een HARDE
// kern (bijna verzadigde schijf tot 45% van de straal) met een korte halo
// eromheen, zodat een deeltje een objectje is en geen wolkje.
const FRAG_D = `
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

export async function laadStroomleven(radius, versie, klemOpHorizon, bestand,
                                      renderer, camera) {
  const r = await fetch(`data/${bestand}?v=${versie}`);
  if (!r.ok) throw new Error(`${bestand}: HTTP ${r.status}`);
  const doc = await r.json();

  const stroom = doc.stroom || bestand;
  const groep = new THREE.Group();
  let materialen = [];     // LineMaterials, die willen de vensterresolutie weten
  let lijnen = [];         // Line2-objecten, om te kunnen herbouwen
  let kleurModus = "modaliteit";
  let lijnModus = "route";

  // ⚠️ Stippel-benen krijgen GEEN draad en GEEN kometen. Gestippeld betekent in
  // dit project "hier reikt het net niet" (werkwijze §7); daar een stroom
  // overheen laten lopen zou een verbinding suggereren die we juist als
  // ontbrekend hebben vastgesteld.
  //
  // De set benen ligt VAST over alle lijnmodi. Dat is geen detail: de
  // komeet-buffers worden één keer op deze telling gealloceerd, dus als een
  // andere lijnvorm er stilzwijgend eentje bij of af zou halen, zouden kop en
  // staart in elkaars geheugen gaan schrijven.
  const dragers = (doc.benen || []).filter(
    (b) => !b.stippel && (b.punten || []).length >= 2);
  const banen = dragers.map((been) => ({
    been,
    plat: [], cum: [0], totaal: 0,
    kleur: new THREE.Color(0xffffff),
    kmPerDag: KM_PER_DAG[been.modaliteit] ?? 500,
  }));

  function bouwLijnen() {
    for (const l of lijnen) {
      groep.remove(l);
      l.geometry.dispose();
      l.material.dispose();
    }
    lijnen = []; materialen = [];

    banen.forEach((b) => {
      const punten = beenPunten(b.been, lijnModus);
      const kleur = kleurVan(b.been.modaliteit, stroom, kleurModus);
      b.kleur.setHex(kleur);

      b.plat = [];
      for (const p of punten) {
        const [x, y, z] = opBol(p[0], p[1], radius * p[2]);
        b.plat.push(x, y, z);
      }

      SCHILLEN.forEach(([hoogteKm, breedte, helder, additief], si) => {
        const pos = [];
        for (const p of punten) {
          // De straalfactor uit stroomstijl (de boog) vermenigvuldigt met de
          // schil-hoogte; in route-modus is die factor 1 en verandert er niets.
          const rr = radius * p[2] * (1 + hoogteKm / AARDSTRAAL_KM);
          const [x, y, z] = opBol(p[0], p[1], rr);
          pos.push(x, y, z);
        }
        const geo = new LineGeometry();
        geo.setPositions(pos);
        const mat = new LineMaterial({
          color: kleur,
          linewidth: breedte,          // pixels (worldUnits blijft false)
          transparent: true,
          opacity: helder,
          blending: additief ? THREE.AdditiveBlending : THREE.NormalBlending,
          depthTest: false,
          depthWrite: false,
          toneMapped: false,           // legenda-kleur = getekende kleur
        });
        // ⚠️ klemOpHorizon zet clippingPlanes; LineMaterial erft van
        // ShaderMaterial en ondersteunt die, dus de achterkant van de bol valt
        // net als bij de andere lagen weg.
        klemOpHorizon(mat);
        const lijn = new Line2(geo, mat);
        // Halo's van buiten naar binnen, de kern als laatste — anders schildert
        // een additieve halo over de kern heen en is de scherpte weer weg.
        lijn.renderOrder = 7.41 + si * 0.01;
        lijn.frustumCulled = false;
        materialen.push(mat);
        lijnen.push(lijn);
        groep.add(lijn);
      });

      // booglengte voor de deeltjes — over dezelfde punten als de lijn, zodat
      // een komeet per constructie op zijn eigen draad blijft lopen
      b.cum = [0];
      for (let i = 1; i < punten.length; i++) {
        b.cum.push(b.cum[i - 1] + gcKm(punten[i - 1], punten[i]));
      }
      b.totaal = b.cum[b.cum.length - 1];
    });
  }
  bouwLijnen();

  // --- de kometen ------------------------------------------------------------
  // Elke komeet is een KOP plus een staart van punten die achter hem aan sleept.
  // De staartlengte is een fractie van de BEENLENGTE, niet een vast aantal km:
  // een zeebeen van 19.000 km en een truckbeen van 8 km horen dezelfde vorm te
  // krijgen, en een vaste km-staart is op het ene onzichtbaar en op het andere
  // onmogelijk.
  const K = AFSTEMMING.kometenPerBeen;
  const T = AFSTEMMING.staartPunten;
  const perKomeet = T + 1;
  const n = banen.length * K * perKomeet;
  const dPos = new Float32Array(Math.max(1, n) * 3);
  const dKleur = new Float32Array(Math.max(1, n) * 3);
  const dGrootte = new Float32Array(Math.max(1, n));
  const dAlfa = new Float32Array(Math.max(1, n));
  const fase = new Float32Array(Math.max(1, banen.length * K));

  banen.forEach((b, bi) => {
    for (let c = 0; c < K; c++) fase[bi * K + c] = c / K;  // gelijkmatig verdeeld
  });

  // De kleur van kop en staart hangt aan de lijnkleur, dus dit draait opnieuw
  // zodra je van modaliteit naar grondstof schakelt.
  function kleurKometen() {
    banen.forEach((b, bi) => {
      for (let c = 0; c < K; c++) {
        for (let j = 0; j <= T; j++) {
          const i = (bi * K + c) * perKomeet + j;
          const u = j / T;                     // 0 = kop, 1 = staarteind
          // De KOP is bijna wit — die moet afsteken tegen élke lijnkleur, en een
          // punt in exact de lijnkleur is op zijn eigen lijn per definitie
          // onzichtbaar. De staart zakt terug naar de lijnkleur, zodat je aan de
          // kleur ziet wát er beweegt.
          const w = (1 - u) * 0.75;
          dKleur[i * 3] = b.kleur.r + (1 - b.kleur.r) * w;
          dKleur[i * 3 + 1] = b.kleur.g + (1 - b.kleur.g) * w;
          dKleur[i * 3 + 2] = b.kleur.b + (1 - b.kleur.b) * w;
        }
      }
    });
  }
  kleurKometen();

  const dGeo = new THREE.BufferGeometry();
  const attrPos = new THREE.BufferAttribute(dPos, 3);
  attrPos.setUsage(THREE.DynamicDrawUsage);
  const attrGr = new THREE.BufferAttribute(dGrootte, 1);
  attrGr.setUsage(THREE.DynamicDrawUsage);
  const attrAlfa = new THREE.BufferAttribute(dAlfa, 1);
  attrAlfa.setUsage(THREE.DynamicDrawUsage);
  const attrKleur = new THREE.BufferAttribute(dKleur, 3);
  dGeo.setAttribute("position", attrPos);
  dGeo.setAttribute("kleur", attrKleur);
  dGeo.setAttribute("grootte", attrGr);
  dGeo.setAttribute("alfa", attrAlfa);

  const dMat = new THREE.ShaderMaterial({
    vertexShader: VERT_D, fragmentShader: FRAG_D,
    // ⚠️ NORMALE blending, geen additieve. Additief telt het deeltje op bij de
    // lijn eronder en dan wordt het juist op de drukste plekken onzichtbaar —
    // precies waar je het wilt zien. Normaal dekt het af en blijft het een
    // objectje dat over de lijn schuift.
    blending: THREE.NormalBlending, transparent: true,
    depthTest: false, depthWrite: false,
  });
  const deeltjes = new THREE.Points(dGeo, dMat);
  deeltjes.renderOrder = 7.55;   // net boven de lijn, zodat een "schip" leesbaar
                                 // over zijn eigen route beweegt
  deeltjes.frustumCulled = false;
  groep.add(deeltjes);

  // positie op de baan bij fractie f (0..1) langs de ECHTE booglengte, zodat
  // een deeltje niet versnelt waar de punten dichter liggen — dezelfde reden
  // waarom v1 `getPointAt` (booglengte) gebruikt in plaats van de curve-parameter
  const tmp = new THREE.Vector3();
  function opBaan(b, f, uit, o) {
    const doel = f * b.totaal;
    let lo = 0, hi = b.cum.length - 1;
    while (lo + 1 < hi) {
      const mid = (lo + hi) >> 1;
      if (b.cum[mid] <= doel) lo = mid; else hi = mid;
    }
    const span = b.cum[hi] - b.cum[lo];
    const t = span > 0 ? (doel - b.cum[lo]) / span : 0;
    for (let a = 0; a < 3; a++) {
      uit[o + a] = b.plat[lo * 3 + a] * (1 - t) + b.plat[hi * 3 + a] * t;
    }
  }

  const camRicht = new THREE.Vector3();
  let tijd = 0;

  function update(dtSec) {
    if (!groep.visible || !banen.length) return;
    tijd += (dtSec || 0.016) * AFSTEMMING.tempo;

    const d = camera.position.length();
    const horizon = d > radius ? radius / d : 1;
    camRicht.copy(camera.position).normalize();
    const h = renderer.domElement.height / (renderer.getPixelRatio() || 1);
    const perEenheid = h / (2 * Math.tan((camera.fov * Math.PI) / 360));

    const stap = AFSTEMMING.staartDeelVanBeen / T;

    banen.forEach((b, bi) => {
      // Een been zonder lengte (kop en staart vallen in hemelsbreed samen) heeft
      // geen baan om over te lopen — dan alle punten op grootte 0 en door.
      if (!(b.totaal > 0)) {
        for (let c = 0; c < K; c++) {
          for (let j = 0; j <= T; j++) {
            const i = (bi * K + c) * perKomeet + j;
            dGrootte[i] = 0; dAlfa[i] = 0;
          }
        }
        return;
      }
      // reisduur in dagen = lengte / snelheid; tempo 1 = één dag per seconde
      const duur = b.totaal / b.kmPerDag;
      for (let c = 0; c < K; c++) {
        const kop = (fase[bi * K + c] + tijd / duur) % 1;
        for (let j = 0; j <= T; j++) {
          const i = (bi * K + c) * perKomeet + j;
          const u = j / T;
          const f = kop - j * stap;
          // Een komeet die net vertrokken is heeft nog geen staart achter zich;
          // die om laten lopen naar het eind van het been zou een tweede,
          // richtingloze sliert opleveren.
          if (f < 0) { dGrootte[i] = 0; dAlfa[i] = 0; continue; }

          opBaan(b, f, dPos, i * 3);
          tmp.set(dPos[i * 3], dPos[i * 3 + 1], dPos[i * 3 + 2]);
          groep.localToWorld(tmp);
          if (tmp.dot(camRicht) / radius < horizon) {
            dGrootte[i] = 0; dAlfa[i] = 0; continue;
          }
          const afst = tmp.distanceTo(camera.position);
          // dichterbij groter, met een plafond zodat een kop op straatniveau
          // geen schermvullende vlek wordt
          const px = (0.0035 * perEenheid) / Math.max(1e-6, afst);
          const kopPx = Math.min(AFSTEMMING.kopMaxPx,
                                 Math.max(AFSTEMMING.kopMinPx, px));
          dGrootte[i] = kopPx * Math.pow(1 - u, 0.55);
          dAlfa[i] = Math.pow(1 - u, 1.8);
        }
      }
    });
    attrPos.needsUpdate = true;
    attrGr.needsUpdate = true;
    attrAlfa.needsUpdate = true;
  }

  function zetResolutie(w, hh) {
    for (const m of materialen) m.resolution.set(w, hh);
  }
  zetResolutie(renderer.domElement.width, renderer.domElement.height);

  return {
    groep, update, zetResolutie,
    /** Schakel kleur=modaliteit ↔ kleur=grondstof zonder herladen. */
    zetKleurModus(modus) {
      if (modus === kleurModus) return;
      kleurModus = modus;
      banen.forEach((b) => {
        b.kleur.setHex(kleurVan(b.been.modaliteit, stroom, kleurModus));
      });
      // De schillen dragen de kleur op hun materiaal en staan per been op rij:
      // SCHILLEN.length materialen achter elkaar, in dezelfde volgorde als banen.
      banen.forEach((b, bi) => {
        for (let si = 0; si < SCHILLEN.length; si++) {
          materialen[bi * SCHILLEN.length + si].color.copy(b.kleur);
        }
      });
      kleurKometen();
      attrKleur.needsUpdate = true;
    },
    /** Schakel tussen de gemeten route en de drie hemelsbreed-varianten. */
    zetLijnModus(modus) {
      if (modus === lijnModus) return;
      lijnModus = modus;
      bouwLijnen();              // nieuwe geometrie voor draad én komeetbaan
      kleurKometen();
      attrKleur.needsUpdate = true;
      zetResolutie(renderer.domElement.width, renderer.domElement.height);
    },
    stats: {
      benen: banen.length, schillen: materialen.length,
      kometen: banen.length * K, staartpunten: n,
    },
  };
}
