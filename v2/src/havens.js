// havens.js — de searoute-havens als zichtbare laag op de bol.
//
// WAAROM DIT EEN EIGEN LAAG IS. Tot nu toe waren havens onzichtbaar: ze stonden
// alleen in ports.json als snap-doel voor de route-test. Vanaf [LAR-518] zijn ze
// het onderwerp zelf, want een haven is de plek waar MODALITEITEN samenkomen —
// zee, binnenwater, en in M25 ook spoor en weg. Lars' regel bij dit issue:
//
//   "als de criteria voor overslagplek 1 zeeroute en 1 binnenwaterroute [zijn]
//    die elkaar raakt, dan missen we de binnenvaart naar spoor of vrachtwagens"
//
// Een overslagpunt is dus niet "waar twee waternetten elkaar toevallig raken"
// maar een AANGEWEZEN haven. Daarom moeten ze eerst op de kaart staan: pas als
// je ze ziet, kun je aanwijzen welke een overslaghaven is.
//
// RENDERING. Eén THREE.Points = één draw call voor bijna 4.000 havens. De stip
// is een gegenereerde sprite (geen extern bestand): lichte kern met een donkere
// rand, zodat een haven leesbaar blijft op zowel de satellietskin als de
// donkere oceaan. Dat is de les van [LAR-480] — zichtbaarheid is CONTRAST, niet
// grootte; groter maken hielp daar juist niet.

import * as THREE from "three";

// Kleur = WELKE NETTEN DEZE HAVEN RAAKT. Bewust naast de bestaande lijnkleuren
// (zee 0x2f9bdd · binnenwater 0xd9a441 · route 0xffe066), zodat een haven nooit
// voor een lijn aangezien wordt.
//
// De mintgroene punten zijn de KANDIDATEN voor de aangewezen overslaghavens:
// havens die zowel het zeenet als het riviernet raken. Kandidaten, niet de
// lijst zelf — Lars' regel bij [LAR-518] is dat "beide netten raken" als
// criterium de overslag binnenvaart -> spoor/vrachtwagen mist, dus de echte
// lijst wordt aangewezen. Deze kleur laat alleen zien waar je kúnt aanwijzen.
const KLEUR_BEIDE  = new THREE.Color(0x4fe3b0);  // zee + rivier — kandidaat
const KLEUR_ZEE    = new THREE.Color(0xfff4e2);  // alleen zeenet
const KLEUR_RIVIER = new THREE.Color(0xd9a441);  // alleen riviernet (= binnenhaven)
const KLEUR_LOS    = new THREE.Color(0x6a7484);  // geen van beide in de buurt

// ⚠️ Wanneer "raakt" een haven een net? MARNET is een GROVE graaf — de mediane
// zee-snap is 31 km — dus een strakke drempel meet vooral de knoopdichtheid van
// MARNET en niet of er een haven ligt. Op 5 km raken 100 havens beide netten,
// op 25 km zijn het er 572; dat verschil is meetresolutie, geen aardrijkskunde.
// 25 km is hier dus een LEESHULP voor het oog, geen besluit: de echte
// aanhechtingsafstanden staan ongewijzigd per haven in ports.json.
const RAAKT_KM = 25;

// Grootte in CSS-pixels, los van de zoom (een haven is een plek, geen gebied —
// meeschalen met de bol zou hem op wereldniveau onzichtbaar maken en op 1 km
// hoogte een vlek). Van ver klein zodat de kustlijnen niet dichtslibben.
const PX_DICHTBIJ = 9.0;
const PX_VERAF = 3.5;

/** Ronde stip met donkere rand — één keer gegenereerd, gedeeld door alle punten. */
function maakStip() {
  const n = 64;
  const c = document.createElement("canvas");
  c.width = c.height = n;
  const g = c.getContext("2d");
  const m = n / 2;

  // donkere halo eerst: die geeft de stip een rand op élke ondergrond
  g.beginPath();
  g.arc(m, m, n * 0.42, 0, Math.PI * 2);
  g.fillStyle = "rgba(8,12,18,0.80)";
  g.fill();

  // lichte kern erbovenop
  g.beginPath();
  g.arc(m, m, n * 0.26, 0, Math.PI * 2);
  g.fillStyle = "rgba(255,255,255,1)";
  g.fill();

  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.minFilter = THREE.LinearFilter;   // geen mipmaps: de stip is al klein
  tex.generateMipmaps = false;
  return tex;
}

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/marnet.js — zie de waarschuwing in de
  // project-CLAUDE.md: een 90°-fout oogt onderling perfect maar ligt los van de bol.
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const cosLat = Math.cos(lat);
  uit[o + 0] = r * cosLat * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * cosLat * Math.sin(lon);
}

/**
 * Bouwt de havenlaag uit de al geladen havenlijst (géén tweede fetch — de
 * route-test in main.js gebruikt exact dezelfde array, en twee bronnen voor
 * dezelfde havens is precies hoe ze uit de pas gaan lopen).
 *
 * De kleur staat als attribuut PER PUNT klaar, niet als materiaal-kleur. Dat is
 * met opzet: zodra de aangewezen overslaghavens er zijn, krijgen die een eigen
 * kleur zonder dat er één regel geometrie verandert.
 */
export function bouwHavenLaag(havens, radius) {
  const t0 = performance.now();
  const n = havens.length;
  const posities = new Float32Array(n * 3);
  const kleuren = new Float32Array(n * 3);

  const telling = { beide: 0, zee: 0, rivier: 0, los: 0 };
  for (let i = 0; i < n; i++) {
    const h = havens[i];
    opBol(h.lon, h.lat, radius, posities, i * 3);

    const aanZee = h.afstandKm >= 0 && h.afstandKm <= RAAKT_KM;
    // -1 = er is geen riviernet in deze bake. Dat is iets ANDERS dan "ver weg",
    // en het verschil moet zichtbaar blijven: anders leest een bake zonder
    // binnenwater als een wereld waarin geen enkele haven aan een rivier ligt.
    const aanRivier = h.afstandRivierKm >= 0 && h.afstandRivierKm <= RAAKT_KM;

    let k;
    if (aanZee && aanRivier) { k = KLEUR_BEIDE; telling.beide++; }
    else if (aanZee) { k = KLEUR_ZEE; telling.zee++; }
    else if (aanRivier) { k = KLEUR_RIVIER; telling.rivier++; }
    else { k = KLEUR_LOS; telling.los++; }

    kleuren[i * 3 + 0] = k.r;
    kleuren[i * 3 + 1] = k.g;
    kleuren[i * 3 + 2] = k.b;
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(posities, 3));
  geo.setAttribute("color", new THREE.BufferAttribute(kleuren, 3));

  const mat = new THREE.PointsMaterial({
    size: PX_VERAF,
    sizeAttenuation: false,   // grootte in pixels, niet in wereld-eenheden
    map: maakStip(),
    vertexColors: true,
    transparent: true,
    alphaTest: 0.25,          // knipt het transparante vierkant weg
    depthWrite: false,
    // depthTest AAN: havens aan de achterkant van de bol horen erachter te
    // verdwijnen. Zonder dit zie je door de aarde heen.
  });

  const punten = new THREE.Points(geo, mat);
  punten.renderOrder = 5;     // kustlijn 2 · bulk 2,5 · net 3 · route 4 · havens 5
  punten.frustumCulled = false;

  return {
    punten,
    kleurAttr: geo.getAttribute("color"),
    stats: {
      havens: n,
      raaktKm: RAAKT_KM,
      ...telling,
      msBouwen: Math.round(performance.now() - t0),
    },
  };
}

/**
 * Zet de puntgrootte op de kijkhoogte. Los van `bouwHavenLaag` zodat main.js
 * hem in dezelfde tick-lus kan aanroepen als de andere lagen.
 *
 * `pixelRatio` moet mee: Three zet `gl_PointSize` in DEVICE-pixels, dus zonder
 * die factor is een haven op een retina-scherm precies half zo groot.
 */
export function zetHavenGrootte(laag, altitudeKm, pixelRatio) {
  const t = Math.max(0, Math.min(1,
    (Math.log10(Math.max(1, altitudeKm)) - 1) / (Math.log10(8000) - 1)));
  laag.punten.material.size = (PX_DICHTBIJ - t * (PX_DICHTBIJ - PX_VERAF)) * pixelRatio;
}

/**
 * Toont de havennaam zodra de cursor er een raakt. Zelfstandig bedraad zodat
 * main.js dun blijft (en THREE niet hoeft te importeren voor één raycaster).
 *
 * ⚠️ De trefdrempel staat in PIXELS en wordt hier naar wereld-eenheden
 * vertaald, want THREE's Points-raycast rekent in wereld-eenheden. Zonder die
 * omrekening is één vaste drempel op wereldniveau veel te grof en op 1 km
 * hoogte onbruikbaar fijn — exact dezelfde val als bij het slepen (globe.js).
 */
export function koppelHavenLabel(globe, laag, havens, labelEl, drempelPx = 9) {
  const straal = new THREE.Raycaster();
  const ndc = new THREE.Vector2();
  const el = globe.renderer.domElement;
  let sleept = false;
  let vorige = -1;

  const verberg = () => {
    if (vorige !== -1) { labelEl.hidden = true; vorige = -1; }
  };

  // Tijdens het slepen zwerft het label mee over de bol en dat leidt af; bij
  // pointerdown gaat hij uit en pas na loslaten weer aan.
  el.addEventListener("pointerdown", () => { sleept = true; verberg(); });
  window.addEventListener("pointerup", () => { sleept = false; });

  el.addEventListener("pointerleave", verberg);

  el.addEventListener("pointermove", (e) => {
    if (sleept || !laag.punten.visible) { verberg(); return; }
    const r = el.getBoundingClientRect();
    if (!(r.width > 0) || !(r.height > 0)) return;

    ndc.x = ((e.clientX - r.left) / r.width) * 2 - 1;
    ndc.y = -(((e.clientY - r.top) / r.height) * 2 - 1);
    straal.setFromCamera(ndc, globe.camera);

    const perPixel =
      (2 * globe.getAltitude() *
        Math.tan(THREE.MathUtils.degToRad(globe.camera.fov) / 2)) / r.height;
    straal.params.Points.threshold = perPixel * drempelPx;

    const treffers = straal.intersectObject(laag.punten, false);
    const i = treffers.length ? treffers[0].index : -1;
    if (i === -1) { verberg(); return; }

    if (i !== vorige) {
      const h = havens[i];
      // Beide aanhechtingen in het label: dát is waar deze laag over gaat, en
      // zonder de afstanden is een mintgroene stip niet te controleren.
      const rv = h.afstandRivierKm >= 0 ? `${h.afstandRivierKm} km` : "geen riviernet";
      labelEl.innerHTML =
        `${h.naam} <span>· ${h.land}${h.locode ? " · " + h.locode : ""}</span>` +
        `<br><span>zee ${h.afstandKm} km · rivier ${rv}</span>`;
      vorige = i;
    }
    labelEl.hidden = false;
    labelEl.style.left = `${e.clientX - r.left}px`;
    labelEl.style.top = `${e.clientY - r.top}px`;
  });
}
