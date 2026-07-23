// stroomlaag.js — het TEKENEN van de gerouteerde stromen (M26.1).
//
// Bewust losgemaakt van `stromen.js`, om precies dezelfde reden waarom
// `router.js` van three is losgetrokken: het routeren moet headless
// narekenbaar zijn (`v2/tools/toets_routes.mjs`), en zodra er ergens in die
// keten `import "three"` staat kan node het niet meer laden. Rekenen hier,
// tekenen daar — de grens loopt bij THREE.
//
// Ontwerp: `v2/design/stroom-aansluiting.md`.

import * as THREE from "three";
import { gcKmLL } from "./router.js?v=070";

// Elke stroom draagt de kleur van zijn grondstof (data/*.js `flowColor`). De
// MODALITEIT zit niet in de kleur maar in de lijnstijl — anders kun je twee
// grondstoffen in dezelfde havenmond niet uit elkaar houden, en dat is precies
// wat deze laag moet laten zien.
// ⚠️ HIER ZAT DE FOUT VAN DE EERSTE VERSIE, EN HET IS ÉÉN FOUT MET DRIE
// GEZICHTEN: maten als vaste fractie van de bolstraal. Op wereldhoogte
// onzichtbaar, op straatniveau catastrofaal.
//
//   * de lift stond op 1,0006–1,0016 × straal = **3,8 tot 10,2 km boven het
//     oppervlak**. Vanuit de ruimte zie je daar niets van; op 3 km hoogte
//     kijk je schuin tegen een lijn aan die kilometers boven de kade hangt en
//     zie je hem dus op de verkeerde plek. (Lars: "zweeft te hoog waardoor je
//     ze op de verkeerde plek ziet onder bepaalde hoek of hoogte.")
//   * de markers hadden een straal van 0,003 × straal = **19,1 km**, mét
//     depthTest:false — op straatniveau een ondoorzichtige bol over het hele
//     scherm.
//
// De les staat al in dit project (`zetHavenGrootte`): wat je op élke hoogte
// wilt zien hoort in SCHERMRUIMTE geschaald te worden, niet in wereldruimte.
// De lift laten we over aan de altitude-evenredige schaling in main.js — exact
// zoals de kustlijn, het zeenet en het landnet het al doen.
//
// Wat blijft is een MINIEME onderlinge volgorde-offset zodat twee stromen die
// dezelfde vaarweg delen niet in elkaar flikkeren. 2e-6 × straal = 12 m: genoeg
// om de tie te breken, te klein om ooit parallax te geven.
const NET_OFFSET = { zee: 0, binnen: 1, spoor: 2, weg: 3, geenNet: 4 };
const OFFSET_STAP = 2e-6;

// Straal van de marker in SCHERMRUIMTE: hij hoort er op 8.000 km en op 3 km
// even groot uit te zien. De hoek die een bol van straal r op afstand d opspant
// is r/d, dus r moet meelopen met de kijkhoogte.
// Gehalveerd na Lars' blik op z17: op straatniveau moet het merk de kade
// AANWIJZEN, niet afdekken — je wilt de pier eronder kunnen zien liggen.
const MERK_HOEK = { laadplek: 0.005, overslag: 0.0065, losplek: 0.005 };
const MERK_MIN_KM = 0.02;      // nooit kleiner dan 20 m — anders verdwijnt hij
const MERK_MAX_KM = 60;        // nooit groter dan 60 km — anders dekt hij af

export function bouwStroomLaag(gerouteerd, { marnet, landnet, radius, klemOpHorizon,
                                             stroomIndex = 0 }) {
  const groep = new THREE.Group();
  const kleur = new THREE.Color(gerouteerd.stroom.kleur || "#ffe066");
  // Onderlinge volgorde-offset in de orde van tientallen meters — zie de
  // toelichting bij NET_OFFSET. Niet meer dan dat: de echte lift komt van de
  // altitude-evenredige schaling in main.js.
  const laagje = (net) => radius * (1 + ((NET_OFFSET[net] ?? 0) + stroomIndex * 5) * OFFSET_STAP);

  for (const been of gerouteerd.benen) {
    if (been.status === "ok") {
      const net = been.net === "spoor" || been.net === "weg" ? landnet : marnet;
      groep.add(routeLijn(net, been.route, laagje(been.net), kleur, klemOpHorizon));
      // De last mile aan beide kanten: kade → het punt waar het been écht
      // begint/eindigt. ⚠️ Dat is NIET de gesnapte knoop uit de aansluiting:
      // het been is gesnoeid op de dichtste nadering van de LIJN, dus we lezen
      // de uiteinden uit het snoeiresultaat. Naar de oude knoop tekenen brengt
      // de overvaar-lus visueel gewoon weer terug.
      const kn = been.route.knopen;
      const eindpunten = [
        [been.van, been.vanLL || [net.knoopLon[kn[0]], net.knoopLat[kn[0]]]],
        [been.naar, been.naarLL
          || [net.knoopLon[kn[kn.length - 1]], net.knoopLat[kn[kn.length - 1]]]],
      ];
      for (const [a, ll] of eindpunten) {
        if (!(gcKmLL(a.lon, a.lat, ll[0], ll[1]) > 0.01)) continue;
        groep.add(lastMile(a, ll[0], ll[1], laagje(been.net), kleur, klemOpHorizon));
      }
    } else if (been.status === "eigen" && been.punten) {
      // EIGEN VERBINDING met echte geometrie: doorgetrokken, want we weten waar
      // hij ligt. Wel dunner/doffer dan een gerouteerd been, zodat je ziet dat
      // hij niet over een gedeeld net loopt.
      const p = been.punten;
      groep.add(eigenLijn(p, laagje("geenNet"), kleur, klemOpHorizon));
      // ⚠️ DE GEKARTEERDE LIJN HOEFT NIET TOT DE AANSLUITING TE LOPEN. Bij
      // Patache houdt OSM's slurry-kartering 736 m vóór het terminalvlak op: het
      // laatste stuk, waar de leiding uitmondt en wordt overgepompt, staat niet
      // in de kaart (gemeten: 5 OSM-objecten binnen 1,8 km, geen tank of works).
      // Dat restje tekenen we GESTIPPELD — we weten dát hij doorloopt, niet
      // precies waar. Zelfde afspraak als overal: gestippeld = geraden.
      for (const [a, ll] of [[been.van, p[0]], [been.naar, p[p.length - 1]]]) {
        if (!(gcKmLL(a.lon, a.lat, ll[0], ll[1]) > 0.05)) continue;
        groep.add(lastMile(a, ll[0], ll[1], laagje("geenNet"), kleur, klemOpHorizon));
      }
    } else if ((been.status === "onbekend" || been.status === "geenNet")
               && been.van && been.naar) {
      // ONBEKEND: gestippeld, want dit is een rechte lijn tussen twee punten en
      // geen bewering over de route. De stijl zegt nu één ding — gestippeld =
      // we weten het niet.
      groep.add(gatLijn(been.van, been.naar, laagje("geenNet"), kleur, klemOpHorizon));
    }
  }

  // De aansluitingen zelf: een bolletje op de kade. Dit is het punt dat op z17
  // óp de juiste kade moet liggen — de acceptatietoets van deze hele laag.
  // De straal wordt elke frame bijgesteld door zetMerkGrootte().
  const merken = [];
  for (const a of aansluitingenVan(gerouteerd)) {
    const m = merk(a, radius, kleur, a.rol);
    merken.push(m);
    groep.add(m);
  }
  groep.userData.merken = merken;
  groep.userData.radius = radius;
  return groep;
}

/**
 * Houdt de markers even groot in BEELD, op elke hoogte.
 *
 * Zonder dit staat er op straatniveau een ondoorzichtige bol van 19 km over de
 * hele kade — precies de fout die deze laag in de eerste versie onbruikbaar
 * maakte. Zelfde principe als `zetHavenGrootte()` in havens.js, alleen werkt
 * die met puntgrootte in pixels en deze met een bolstraal in wereldruimte:
 * de opgespannen hoek r/d is constant als r meeloopt met de kijkhoogte.
 */
export function zetMerkGrootte(laag, altitudeKm) {
  const radius = laag.userData?.radius;
  if (!radius) return;
  const perKm = radius / 6371;
  for (const m of laag.userData.merken || []) {
    const hoek = MERK_HOEK[m.userData.rol] ?? 0.010;
    const km = Math.max(MERK_MIN_KM, Math.min(MERK_MAX_KM, altitudeKm * hoek));
    m.scale.setScalar(km * perKm / m.geometry.parameters.radius);
  }
}

function aansluitingenVan(gerouteerd) {
  const uit = new Map();
  for (const b of gerouteerd.benen) {
    for (const a of [b.van, b.naar]) if (a && !uit.has(a.id)) uit.set(a.id, a);
  }
  return [...uit.values()];
}

function opBol3(lon, lat, r) {
  const a = lon * (Math.PI / 180), b = lat * (Math.PI / 180);
  const c = Math.cos(b);
  return new THREE.Vector3(r * c * Math.cos(a), r * Math.sin(b), -r * c * Math.sin(a));
}

/** De gerouteerde polylijn van één been, opgetild tot boven de tegels. */
function routeLijn(net, been, straal, kleur, klemOpHorizon) {
  const pts = [];
  let bij = been.knopen[0];
  for (const e of been.edges) {
    const start = net.geomStart[e], n = net.geomN[e];
    const vooruit = net.edgeA[e] === bij;
    for (let k = 0; k < n; k++) {
      const idx = vooruit ? start + k : start + (n - 1 - k);
      // ⚠️ Opeenvolgende edges DELEN hun eindvertex. Die dubbel opnemen is
      // visueel onzichtbaar maar verschuift de indexering, en dan snijdt het
      // snoeien uit stromen.js op de verkeerde plek. Dezelfde regel als in
      // `beenPunten()` — de twee moeten per constructie dezelfde reeks geven.
      if (k === 0 && pts.length) continue;
      // De gebakken posities liggen op de bolstraal; radiaal opschalen tilt ze
      // op zonder de vorm te raken.
      pts.push(net.posities[idx * 3], net.posities[idx * 3 + 1], net.posities[idx * 3 + 2]);
    }
    bij = vooruit ? net.edgeB[e] : net.edgeA[e];
  }
  // Snoeien op de dichtste nadering: exact hetzelfde stuk dat stromen.js heeft
  // GETELD, anders wijken het getal in de HUD en de lijn op de bol van elkaar af.
  const vanI = been.knipVan ?? 0;
  const naarI = been.knipNaar ?? (pts.length / 3 - 1);
  const arr = new Float32Array(pts.slice(vanI * 3, (naarI + 1) * 3));
  const schaal = straal / straalVan(arr);
  for (let i = 0; i < arr.length; i++) arr[i] *= schaal;

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(arr, 3));
  const mat = new THREE.LineBasicMaterial({ color: kleur, transparent: true, opacity: 0.95 });
  klemOpHorizon?.(mat);
  const lijn = new THREE.Line(geo, mat);
  lijn.renderOrder = 10;          // boven de keten-route (8) en het landnet (7)
  lijn.frustumCulled = false;
  return lijn;
}

/** Straal van het eerste punt — de bake is bolvast, dus één sample volstaat. */
function straalVan(arr) {
  return Math.hypot(arr[0], arr[1], arr[2]) || 1;
}

/**
 * De LAST MILE: kade → netknoop. Bewust een eigen, dunnere lijn en niet stil
 * meegetekend in het been — dit stukje is niet gerouteerd maar rechtgetrokken,
 * en dat verschil hoort zichtbaar te zijn.
 */
function lastMile(aansluiting, lon, lat, straal, kleur, klemOpHorizon) {
  const geo = new THREE.BufferGeometry().setFromPoints([
    opBol3(aansluiting.lon, aansluiting.lat, straal),
    opBol3(lon, lat, straal),
  ]);
  const mat = new THREE.LineDashedMaterial({
    color: kleur, transparent: true, opacity: 0.85,
    dashSize: straal * 0.0004, gapSize: straal * 0.0003,
  });
  klemOpHorizon?.(mat);
  const lijn = new THREE.Line(geo, mat);
  lijn.computeLineDistances();
  lijn.renderOrder = 11;
  lijn.frustumCulled = false;
  return lijn;
}

/**
 * EEN EIGEN VERBINDING: een toegewijde schakel met echte geometrie — de
 * slurryleiding van de mijn naar zijn eigen kade.
 *
 * Doorgetrokken, niet gestippeld. Hij is namelijk niet onzeker: we weten precies
 * waar hij ligt. Wat hem onderscheidt van een gerouteerd been is dat hij niet
 * over een GEDEELD net loopt — een weg of vaarweg is productonafhankelijk, een
 * slurryleiding vervoert precies één ding tussen precies twee punten. Dat
 * verschil zit in de dikte/dofheid, niet in stippels.
 */
function eigenLijn(punten, straal, kleur, klemOpHorizon) {
  const pts = punten.map(([lo, la]) => opBol3(lo, la, straal));
  const geo = new THREE.BufferGeometry().setFromPoints(pts);
  const mat = new THREE.LineBasicMaterial({
    color: kleur, transparent: true, opacity: 0.7,
  });
  klemOpHorizon?.(mat);
  const lijn = new THREE.Line(geo, mat);
  lijn.renderOrder = 10;
  lijn.frustumCulled = false;
  return lijn;
}

/**
 * ONBEKEND: we weten niet waar deze verbinding loopt. Rechte lijn tussen de twee
 * uiteinden, gestippeld — en de stippels zeggen nu precies één ding: dit is
 * geraden, geen route. (Ze betekenden eerder óók "geen net", en dat maakte
 * dezelfde stijl twee dingen tegelijk.)
 */
function gatLijn(van, naar, straal, kleur, klemOpHorizon) {
  const pts = [];
  {
    const n = 48;                     // gesampled, anders snijdt hij door de bol
    for (let i = 0; i <= n; i++) {
      const t = i / n;
      pts.push(opBol3(van.lon + (naar.lon - van.lon) * t,
                      van.lat + (naar.lat - van.lat) * t, straal));
    }
  }
  const geo = new THREE.BufferGeometry().setFromPoints(pts);
  const mat = new THREE.LineDashedMaterial({
    color: kleur, transparent: true, opacity: 0.55,
    dashSize: straal * 0.0004, gapSize: straal * 0.0004,
  });
  klemOpHorizon?.(mat);
  const lijn = new THREE.Line(geo, mat);
  lijn.computeLineDistances();
  lijn.renderOrder = 10;
  lijn.frustumCulled = false;
  return lijn;
}

// Eenheidsbol; de echte maat komt elke frame uit zetMerkGrootte(). Zo staat de
// hoogte-afhankelijkheid op één plek in plaats van in de constructor.
const MERK_GEO = new THREE.SphereGeometry(1, 12, 12);

function merk(aansluiting, straal, kleur, rol) {
  // ⚠️ `transparent: true` IS HIER GEEN COSMETICA — het bepaalt in welke PASS
  // dit merk terechtkomt, en dát is waarom de merken verdwenen zodra de tegels
  // binnen waren (Lars: "ik heb ze in sommige beelden wel heel kort gezien").
  // Three tekent eerst de opaque objecten en daarna pas de transparante; een
  // renderOrder ordent alleen bínnen zijn eigen pass. Het merk was het enige
  // object van deze laag zonder de vlag — alle lijnen hier staan er wél op — dus
  // het werd getekend in de opaque pass en de tegels (transparant, want ze vaden
  // in met opacity 0→1) schilderden er daarna overheen. `depthTest: false` en
  // renderOrder 12 kunnen daar per definitie niets tegen doen.
  const m = new THREE.Mesh(MERK_GEO, new THREE.MeshBasicMaterial({
    color: rol === "overslag" ? 0xffffff : kleur,
    depthTest: false, transparent: true, opacity: 1,
  }));
  m.position.copy(opBol3(aansluiting.lon, aansluiting.lat, straal));
  m.renderOrder = 12;
  m.userData.aansluiting = aansluiting;
  m.userData.rol = rol;
  m.scale.setScalar(straal * 1e-4);   // voorlopig; direct overschreven
  return m;
}
