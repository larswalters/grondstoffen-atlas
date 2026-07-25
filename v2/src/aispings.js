// aispings.js — de ruwe AIS-pings als debuglaag op de bol (M28, LAR-535).
//
// WAAROM DIT EEN EIGEN LAAG IS. Het tracknet wordt opgebouwd uit pings die op
// de VPS binnendruppelen, en zonder venster op die stroom is DEKKING niet te
// beoordelen: een leeg stuk rivier ziet er in de graaf precies zo uit als een
// stuk waar toevallig geen station staat. Deze laag maakt dat verschil
// zichtbaar terwijl je kijkt — je ziet de corridors zich week na week vullen,
// en je kunt de pings naast de satellietfoto en naast de graaf leggen.
//
// PUUR WEERGAVE. Deze punten spelen geen enkele rol in de routering; de echte
// tracks worden gebouwd in de verwerkingsstap (LAR-530).
//
// ⚠️ PAGES IS STATISCH, dus de bol kan niet in de JSONL op de VPS kijken. Een
// timer op de VPS (ais_pings_publiceren.py) dunt de laatste 24 uur uit tot een
// compact bestand en nginx+Traefik serveren het achter HTTPS met CORS. Zie
// v2/design/ais-collector-vps.md.
//
// KLEUR ZEGT TWEE DINGEN TEGELIJK:
//   varend (SOG >= 0,5 kn)  wit -> cyaan -> donkerblauw naarmate de ping ouder
//                           is: verse doorvaarten springen eruit, oude blijven
//                           als spoor liggen. Dit is het geul-materiaal.
//   stilliggend             warm oranje, geen tijdsverloop: dit zijn de
//                           ligplaatsen, en die zijn juist interessant als
//                           PLEK (het worden de terminal-nodes in LAR-531).

import * as THREE from "three";

// Het endpoint op de VPS (Traefik -> nginx op localhost:8088). Overschrijfbaar
// met ?pings=<url> zodat je een lokaal bestand of een tweede omgeving kunt
// testen zonder de code aan te raken.
const STANDAARD_URL = "https://ais.187.124.169.172.nip.io/pings.json";

const VERS = new THREE.Color(0xffffff);
const MIDDEL = new THREE.Color(0x35d6f5);
const OUD = new THREE.Color(0x1b3f8f);
const LIGPLAATS = new THREE.Color(0xff8a3d);

const PX_VERAF = 1.4;
const PX_DICHTBIJ = 3.6;

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/havens.js — zie de waarschuwing in de
  // project-CLAUDE.md: een 90°-fout oogt onderling perfect maar ligt los van de bol.
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const cosLat = Math.cos(lat);
  uit[o + 0] = r * cosLat * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * cosLat * Math.sin(lon);
}

/** Zachte stip zonder externe asset — zelfde truc als havens.js. */
function maakStip() {
  const n = 32;
  const c = document.createElement("canvas");
  c.width = c.height = n;
  const g = c.getContext("2d");
  const grad = g.createRadialGradient(n / 2, n / 2, 0, n / 2, n / 2, n / 2);
  grad.addColorStop(0.0, "rgba(255,255,255,1)");
  grad.addColorStop(0.45, "rgba(255,255,255,0.9)");
  grad.addColorStop(1.0, "rgba(255,255,255,0)");
  g.fillStyle = grad;
  g.beginPath();
  g.arc(n / 2, n / 2, n / 2, 0, Math.PI * 2);
  g.fill();
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}

function kleurVoor(minutenGeleden, varend, uren, doel) {
  if (!varend) return doel.copy(LIGPLAATS);
  // t loopt van 0 (zojuist) naar 1 (aan het eind van het venster).
  const t = Math.max(0, Math.min(1, minutenGeleden / (uren * 60)));
  return t < 0.5
    ? doel.copy(VERS).lerp(MIDDEL, t * 2)
    : doel.copy(MIDDEL).lerp(OUD, (t - 0.5) * 2);
}

function bouwGeometrie(doc, radius) {
  const uren = doc.uren || 24;
  let n = 0;
  for (const schip of doc.schepen) n += schip.length - 1;  // [0] = mmsi

  const posities = new Float32Array(n * 3);
  const kleuren = new Float32Array(n * 3);
  const tmp = new THREE.Color();
  let i = 0;
  let varend = 0;
  let jongste = Infinity;

  for (const schip of doc.schepen) {
    for (let k = 1; k < schip.length; k++) {
      const [latE5, lonE5, min, isVarend] = schip[k];
      opBol(lonE5 / 1e5, latE5 / 1e5, radius, posities, i * 3);
      kleurVoor(min, isVarend, uren, tmp);
      kleuren[i * 3 + 0] = tmp.r;
      kleuren[i * 3 + 1] = tmp.g;
      kleuren[i * 3 + 2] = tmp.b;
      if (isVarend) varend++;
      if (min < jongste) jongste = min;
      i++;
    }
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(posities, 3));
  geo.setAttribute("color", new THREE.BufferAttribute(kleuren, 3));
  return { geo, punten: n, varend, jongste };
}

/**
 * Haalt het pings-bestand op en bouwt de laag. Faalt zacht: is de VPS even weg,
 * dan hoort de rest van de atlas daar niets van te merken — dit is een
 * debuglaag, geen dragende laag.
 */
export async function laadAisPings(radius, url = null) {
  const t0 = performance.now();
  const params = new URLSearchParams(location.search);
  const bron = url || params.get("pings") || STANDAARD_URL;
  // Per minuut een verse sleutel: nginx zet max-age=60, dus dit sluit aan op de
  // cache in plaats van hem elke keer te omzeilen.
  const r = await fetch(`${bron}?t=${Math.floor(Date.now() / 60000)}`);
  if (!r.ok) throw new Error(`pings.json: HTTP ${r.status}`);
  const doc = await r.json();
  const tLaden = performance.now();

  const { geo, punten, varend, jongste } = bouwGeometrie(doc, radius);

  const mat = new THREE.PointsMaterial({
    size: PX_VERAF,
    sizeAttenuation: false,   // grootte in PIXELS (de LAR-480/marker-les)
    map: maakStip(),
    vertexColors: true,
    transparent: true,
    alphaTest: 0.2,
    depthWrite: false,
    // depthTest AAN, net als de havens: pings aan de achterkant van de bol
    // horen achter de aarde te verdwijnen.
  });

  const points = new THREE.Points(geo, mat);
  points.renderOrder = 5.5;   // net boven de havens (5), onder de gloed (6,3)
  points.frustumCulled = false;
  points.visible = false;     // debuglaag: standaard uit

  return {
    punten: points,
    doc,
    bron,
    stats: {
      punten,
      varend,
      stil: punten - varend,
      schepen: doc.schepen.length,
      jongsteMin: Number.isFinite(jongste) ? jongste : null,
      korrelMin: doc.korrel_min,
      uren: doc.uren,
      gemaakt: doc.gemaakt,
      msLaden: Math.round(tLaden - t0),
      msVerwerken: Math.round(performance.now() - tLaden),
    },
  };
}

/**
 * Vervangt de geometrie door een verse ophaal, zonder de laag opnieuw aan de
 * scene te hangen (zo blijft de aan/uit-stand en de tick-lus intact).
 */
export async function ververs(laag, radius) {
  const r = await fetch(`${laag.bron}?t=${Math.floor(Date.now() / 60000)}`);
  if (!r.ok) throw new Error(`pings.json: HTTP ${r.status}`);
  const doc = await r.json();
  const { geo, punten, varend, jongste } = bouwGeometrie(doc, radius);
  laag.punten.geometry.dispose();
  laag.punten.geometry = geo;
  laag.doc = doc;
  Object.assign(laag.stats, {
    punten,
    varend,
    stil: punten - varend,
    schepen: doc.schepen.length,
    jongsteMin: Number.isFinite(jongste) ? jongste : null,
    korrelMin: doc.korrel_min,
    gemaakt: doc.gemaakt,
  });
  return laag;
}

/** Puntgrootte op de kijkhoogte — zelfde wet en dezelfde pixelRatio-val als havens.js. */
export function zetPingGrootte(laag, altitudeKm, pixelRatio) {
  const t = Math.max(0, Math.min(1,
    (Math.log10(Math.max(1, altitudeKm)) - 1) / (Math.log10(8000) - 1)));
  laag.punten.material.size = (PX_DICHTBIJ - t * (PX_DICHTBIJ - PX_VERAF)) * pixelRatio;
}
