// stadslichten.js — DE STADSLICHTEN (Black Marble) als additieve laag op de
// gedimde bol (golf 2 van de visuele fase, 2026-10-27, LAR-618).
//
// Waarom dit bestaat: besluit 6 van v2/design/lod-ontwerpbrief.md (night-side:
// stromen aan → satelliet gedimd + stadslichten) en de meting van 2026-08-07 dat
// additief licht op een felle daglichtfoto niets heeft om tegen af te steken.
// Sinds `?v=119` dimt de atlasmodus de ondergrond; de "aderen" van de
// referentiebeelden — de bewoonde wereld als fijn lichtnet onder de
// grondstofstromen — ontbraken nog. Op de gedimde bol deed het witte landnet
// dat werk half; dit is de echte laag.
//
// DE BRON. NASA's Black Marble 2016 (publiek domein) was het doel, maar
// eoimages.gsfc.nasa.gov is vanaf deze machine niet bereikbaar (verbinding
// gereset, ook buiten de sandbox) en Wikimedia Commons heeft er alleen een
// 1920×1080-versie van. Gebruikt: de 8k-nachtkaart van Solar System Scope
// (CC BY 4.0, "based on NASA elevation and imagery data" — de Black Marble),
// 8192×4096, hier als JPEG q78: 8k 1,14 MB · 4k 0,34 MB. 98,9 % van de
// pixels is < 32/255: additief opgeteld voegt de donkere rest nauwelijks iets
// toe, dus geen masker nodig. ⚠️ CC BY = naamsvermelding verplicht → de
// attributiebalk (main.js zetAttrib) noemt de laag zolang hij zichtbaar is.
//
// HET MECHANISME. Een tweede bol met dezelfde SphereGeometry-afbeelding als de
// dagkaart (lon 0 op +X — de lat/lon→3D van M22), een haartje boven het
// oppervlak op `lift` (= CONFIG.vectorLift, de schil van de diepste tegels),
// MeshBasicMaterial met AdditiveBlending, toneMapped UIT (de belichting dimt
// alleen de ondergrond; de lichten horen juist te blijven staan, net als de
// gloed en de kometen), en klemOpHorizon (dieptetest uit, achterkant weg —
// dezelfde behandeling als elke vectorlaag, zie globe.js). renderOrder 4:
// boven de tegels (1–3), onder kustlijn/landnet/stromen (6+).
//
// ⚠️ ZOOMBAND. De textuur is 3–5 km per pixel; onder ~150 km kijkhoogte
// worden steden wazige vlekken over scherpe Esri-tegels. Daarom dooft de laag
// glad uit tussen `uitTussenKm` (volle sterkte erboven, nul eronder) — op
// straatniveau zijn de tegels zelf de stadslichten (verlichte wegen, daken).
// Geen drempel, dus geen pop.

import * as THREE from "three";

export const AFSTEMMING = {
  /** vermenigvuldiger op de textuur (additief): 1 = zoals de bron */
  sterkte: 0.85,
  /** [onder, boven] kijkhoogte in km waartussen de laag uitdooft bij inzoomen */
  uitTussenKm: [60, 350],
};

/**
 * @param opts.radius         bolstraal in scene-eenheden
 * @param opts.lift           schaal boven de bol (CONFIG.vectorLift)
 * @param opts.versie         cache-buster voor de textuur
 * @param opts.telefoon       4k i.p.v. 8k
 * @param opts.klemOpHorizon  GLOBE.klemOpHorizon
 * @param opts.renderer       voor anisotropie
 */
export function laadStadslichten(opts) {
  const { radius, lift = 1.00002, versie, klemOpHorizon, renderer } = opts;
  const bestand = opts.telefoon ? "stadslichten-4k.jpg" : "stadslichten-8k.jpg";
  const t0 = performance.now();

  const mat = new THREE.MeshBasicMaterial({
    map: null,
    color: new THREE.Color(AFSTEMMING.sterkte, AFSTEMMING.sterkte, AFSTEMMING.sterkte),
    blending: THREE.AdditiveBlending,
    transparent: true,
    depthWrite: false,
    toneMapped: false,
    side: THREE.FrontSide,
    opacity: 1,
  });
  klemOpHorizon(mat);

  const geo = new THREE.SphereGeometry(radius * lift, 96, 96);
  const mesh = new THREE.Mesh(geo, mat);
  mesh.renderOrder = 4;
  mesh.frustumCulled = false;
  mesh.name = "stadslichten";
  mesh.visible = false;              // tot de textuur binnen is

  let aan = true;
  let geladen = false;
  const klaar = new Promise((resolve, reject) => {
    new THREE.TextureLoader().load(
      `data/${bestand}?v=${versie}`,
      (tex) => {
        tex.colorSpace = THREE.SRGBColorSpace;
        tex.anisotropy = renderer ? renderer.capabilities.getMaxAnisotropy() : 1;
        tex.minFilter = THREE.LinearMipmapLinearFilter;
        mat.map = tex;
        mat.needsUpdate = true;
        geladen = true;
        mesh.visible = aan;
        resolve({ bestand, ms: Math.round(performance.now() - t0), breedte: tex.image.width, hoogte: tex.image.height });
      },
      undefined,
      (e) => reject(new Error(`${bestand}: ${e && e.message ? e.message : "laden mislukt"}`))
    );
  });

  return {
    mesh, klaar, afstemming: AFSTEMMING,
    get aan() { return aan; },
    zetAan(waarde) { aan = !!waarde; mesh.visible = aan && geladen; },
    /** per frame: uitdoven bij inzoomen (glad, geen drempel) */
    update(hoogteKm) {
      if (!mesh.visible) return;
      const [a, b] = AFSTEMMING.uitTussenKm;
      const t = Math.max(0, Math.min(1, (hoogteKm - a) / Math.max(1e-6, b - a)));
      const s = AFSTEMMING.sterkte * t * t * (3 - 2 * t);
      mat.color.setRGB(s, s, s);
    },
    attributie: "Stadslichten: Solar System Scope (CC BY 4.0), naar NASA Black Marble",
  };
}
