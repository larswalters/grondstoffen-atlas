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

// Elke stroom draagt de kleur van zijn grondstof (data/*.js `flowColor`). De
// MODALITEIT zit niet in de kleur maar in de lijnstijl — anders kun je twee
// grondstoffen in dezelfde havenmond niet uit elkaar houden, en dat is precies
// wat deze laag moet laten zien.
const LIFT = {
  // Radiale lift per net, in fracties van de straal. Voorkomt z-fighting waar
  // twee benen dezelfde edges delen (dat is geen fout: routes delen letterlijk
  // edges sinds M23 — bundelen is gratis, maar dan moet je ze wel zien liggen).
  zee: 1.0006, binnen: 1.0008, spoor: 1.0010, weg: 1.0012, geenNet: 1.0014,
};
const LAST_MILE_LIFT = 1.0016;

export function bouwStroomLaag(gerouteerd, { marnet, landnet, radius, klemOpHorizon,
                                             stroomIndex = 0 }) {
  const groep = new THREE.Group();
  const kleur = new THREE.Color(gerouteerd.stroom.kleur || "#ffe066");
  // Elke stroom een eigen minieme extra lift, zodat twee grondstoffen die
  // dezelfde vaarweg delen naast elkaar leesbaar blijven i.p.v. te flikkeren.
  const stroomLift = 1 + stroomIndex * 0.00035;

  for (const been of gerouteerd.benen) {
    if (been.status === "ok") {
      const net = been.net === "spoor" || been.net === "weg" ? landnet : marnet;
      groep.add(routeLijn(net, been.route, radius * LIFT[been.net] * stroomLift,
                          kleur, klemOpHorizon));
      // de last mile aan beide kanten: kade → netknoop
      for (const [a, kant] of [[been.van, 0], [been.naar, 1]]) {
        const h = a.aanhechting[been.net];
        if (!h || !(h.km > 0.01)) continue;
        groep.add(lastMile(a, h, radius * LAST_MILE_LIFT * stroomLift, kleur, klemOpHorizon, kant));
      }
    } else if (been.status === "geenNet" && been.van && been.naar) {
      groep.add(gatLijn(been.van, been.naar, radius * LIFT.geenNet * stroomLift,
                        kleur, klemOpHorizon));
    }
  }

  // De aansluitingen zelf: een bolletje op de kade. Dit is het punt dat op z17
  // óp de juiste kade moet liggen — de acceptatietoets van deze hele laag.
  for (const a of aansluitingenVan(gerouteerd)) {
    groep.add(merk(a, radius * LAST_MILE_LIFT * stroomLift, kleur, a.rol));
  }
  return groep;
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
      // De gebakken posities liggen op de bolstraal; radiaal opschalen tilt ze
      // op zonder de vorm te raken.
      pts.push(net.posities[idx * 3], net.posities[idx * 3 + 1], net.posities[idx * 3 + 2]);
    }
    bij = vooruit ? net.edgeB[e] : net.edgeA[e];
  }
  const arr = new Float32Array(pts);
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
function lastMile(aansluiting, h, straal, kleur, klemOpHorizon) {
  const geo = new THREE.BufferGeometry().setFromPoints([
    opBol3(aansluiting.lon, aansluiting.lat, straal),
    opBol3(h.knoopLon ?? h.lon, h.knoopLat ?? h.lat, straal),
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

/** Een been zonder net (pijpleiding, transportband): recht en gestippeld. */
function gatLijn(van, naar, straal, kleur, klemOpHorizon) {
  const pts = [];
  const n = 48;                       // gesampled, anders snijdt hij door de bol
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    pts.push(opBol3(van.lon + (naar.lon - van.lon) * t,
                    van.lat + (naar.lat - van.lat) * t, straal));
  }
  const geo = new THREE.BufferGeometry().setFromPoints(pts);
  const mat = new THREE.LineDashedMaterial({
    color: kleur, transparent: true, opacity: 0.55,
    dashSize: straal * 0.002, gapSize: straal * 0.002,
  });
  klemOpHorizon?.(mat);
  const lijn = new THREE.Line(geo, mat);
  lijn.computeLineDistances();
  lijn.renderOrder = 10;
  lijn.frustumCulled = false;
  return lijn;
}

const ROL_MAAT = { laadplek: 0.0030, overslag: 0.0038, losplek: 0.0030 };

function merk(aansluiting, straal, kleur, rol) {
  const m = new THREE.Mesh(
    new THREE.SphereGeometry(straal * (ROL_MAAT[rol] ?? 0.003), 12, 12),
    new THREE.MeshBasicMaterial({
      color: rol === "overslag" ? 0xffffff : kleur, depthTest: false,
    })
  );
  m.position.copy(opBol3(aansluiting.lon, aansluiting.lat, straal));
  m.renderOrder = 12;
  m.userData.aansluiting = aansluiting;
  return m;
}
