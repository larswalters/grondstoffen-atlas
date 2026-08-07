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
// ⚠️ HET MECHANISME ZELF STAAT SINDS 2026-08-07 IN `gloed.js`, want er is een
// tweede bron bijgekomen: de belangrijke punten van elke stroom (mijn · overslag ·
// fabriek) gloeien nu ook, op verzoek van Lars. Deze module is daarmee nog maar
// één ding: de vertaling van `gloednodes-koper.json` naar gloedknopen.

import { bouwGloed, AFSTEMMING as GLOED_AFSTEMMING } from "./gloed.js?v=118";
import { GRONDSTOF_KLEUR } from "./stroomstijl.js?v=118";

// Grondstofkleuren komen uit `stroomstijl.js` — de gloed hoort dezelfde taal te
// spreken als de lijn die er vertrekt.
//
// ⚠️ STOND HIER EERST ALS EIGEN KOPIE (de v1-waarden #C87D4A / #4FD1C5). Sinds
// 2026-08-07 kleuren ook de stroomlijnen op grondstof, en twee tabellen die
// hetzelfde horen te zeggen lopen uit elkaar — dus leest deze laag de gedeelde
// tabel. Een gloedkoepel en de lijn die eruit vertrekt hebben nu per constructie
// dezelfde kleur.
const KLEUR_ONBEKEND = 0xbfbfbf;

// Afstemknoppen die alleen over DEZE bron gaan. De gedeelde knoppen (pixel-
// minimum, sterkte, koepelhoogte) staan in `gloed.js`, zodat een stroomknoop en
// een registersite met hetzelfde gewicht ook even groot zijn.
export const AFSTEMMING = {
  kmPerWortelGewicht: 0.30, // straal in km = dit × √gewicht (g=100 → 3,0 km)
  get minPx() { return GLOED_AFSTEMMING.minPx; },
  get sterkte() { return GLOED_AFSTEMMING.sterkte; },
  get koepelHoogte() { return GLOED_AFSTEMMING.koepelHoogte; },
};

export async function laadGloednodes(radius, versie, camera, renderer) {
  const t0 = performance.now();
  const r = await fetch(`data/gloednodes-koper.json?v=${versie}`);
  if (!r.ok) throw new Error(`gloednodes-koper.json: HTTP ${r.status}`);
  const doc = await r.json();
  const tLaden = performance.now();

  // ⚠️ Alleen sites. Zie de kop: complex/regio zijn labels, geen glow-objecten.
  const sites = doc.knopen.filter((k) => k.level === "site");
  if (!sites.length) throw new Error("gloednodes: geen sites in het bestand");

  const maxGewicht = Math.max(...sites.map((s) => s.gewicht || 1));

  const knopen = sites.map((s) => {
    const g = Math.max(1, s.gewicht || 1);
    return {
      lon: s.lon,
      lat: s.lat,
      straalKm: AFSTEMMING.kmPerWortelGewicht * Math.sqrt(g),
      kleur: GRONDSTOF_KLEUR[(s.grondstof || [])[0]] ?? KLEUR_ONBEKEND,
      // Capaciteit is het gewicht in de optelling (besluit 2 uit de brief): hij
      // stuurt zowel de wereldmaat hierboven als de helderheid. Zonder dat tweede
      // zouden op wereldhoogte — waar iedereen op het pixel-minimum zit — alleen
      // AANTALLEN nog tellen en zou een smelter van 1,2 Mt/j even zwaar wegen als
      // een staalbouwer ernaast.
      helder: 0.28 + 0.72 * Math.sqrt(g / maxGewicht),
    };
  });

  const gloed = bouwGloed(knopen, radius, camera, renderer, 7.6);

  return {
    groep: gloed.groep,
    update: gloed.update,
    sites,
    stats: {
      sites: knopen.length,
      schillen: gloed.groep.children.length,
      complexen: doc.knopen.filter((k) => k.level === "complex").length,
      msLaden: Math.round(tLaden - t0),
      msVerwerken: Math.round(performance.now() - tLaden),
    },
  };
}
