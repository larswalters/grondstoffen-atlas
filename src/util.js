// util.js — kleine hulpjes die overal gebruikt worden.

function latLonToVec3(lat, lon, radius) {
  const phi = (90 - lat) * (Math.PI / 180);
  const theta = (lon + 180) * (Math.PI / 180);
  return new THREE.Vector3(
    -radius * Math.sin(phi) * Math.cos(theta),
    radius * Math.cos(phi),
    radius * Math.sin(phi) * Math.sin(theta)
  );
}

function clamp01(x) { return Math.min(1, Math.max(0, x)); }

// Sferische interpolatie tussen twee EENHEIDSvectoren.
// Dit is de kern van de nieuwe bogen: elk tussenpunt ligt op de bol,
// dus de route kan nooit meer door de aarde zakken (de oude Bézier deed dat wél
// bij lange routes — het controlepunt trok het midden van de boog naar binnen).
function slerpUnit(a, b, t) {
  const dot = Math.min(1, Math.max(-1, a.dot(b)));
  const omega = Math.acos(dot);
  if (omega < 1e-6) return a.clone();
  const so = Math.sin(omega);
  return a.clone().multiplyScalar(Math.sin((1 - t) * omega) / so)
    .add(b.clone().multiplyScalar(Math.sin(t * omega) / so));
}

// Route over het boloppervlak langs een reeks punten [{lat,lon}, ...].
// Tussen opeenvolgende punten wordt de great circle gevolgd (kortste pad).
//
// Twee profielen (opts.flat):
//   flat = false  -> BOOG: hoogte(t) = lift * sin(pi * t). Nul aan de uiteinden,
//                    max in het midden. Voor de "hemelsbreed"-weergave.
//   flat = true   -> ROUTE: constante hoogte vlak boven het oppervlak, met
//                    alleen een zachte opbolling aan de uiteinden zodat de
//                    lijn niet in de markers verdwijnt. Voor de "varen"-weergave.
//
// opts.lane    = ZIJWAARTSE VERSCHUIVING (vaarbaan).
// opts.anchors = indices in `latlons` waar de banen weer SAMEN moeten komen:
//                havens en zeestraten. Daar gaat immers iedereen door dezelfde
//                poort. Tussen twee ankers waaieren de banen uit, bij een anker
//                knijpen ze samen — precies wat je op zee ook ziet: een bundel
//                die zich vernauwt in de straat.
//
// Geeft { curve, totalAngle } terug: totalAngle = routelengte in radialen.
function makeRouteCurve(latlons, radius, lift, opts) {
  const flat = !!(opts && opts.flat);
  const lane = (opts && opts.lane) || 0;
  const anchorIdx = (opts && opts.anchors) || null;
  const units = latlons.map((p) => latLonToVec3(p.lat, p.lon, 1));

  // lengte (in radialen) per segment, voor een gelijkmatige parametrisatie
  const segAngles = [];
  let totalAngle = 0;
  for (let i = 0; i < units.length - 1; i++) {
    const d = Math.min(1, Math.max(-1, units[i].dot(units[i + 1])));
    const w = Math.max(1e-6, Math.acos(d));
    segAngles.push(w);
    totalAngle += w;
  }

  // waar in de route (0..1) ligt elk invoerpunt? nodig om de ankers te plaatsen
  const pointT = [0];
  let acc = 0;
  for (let i = 0; i < segAngles.length; i++) {
    acc += segAngles[i];
    pointT.push(acc / totalAngle);
  }

  const anchorTs = [0];
  if (anchorIdx) {
    anchorIdx.forEach((i) => {
      const t = pointT[i];
      if (t > 0.002 && t < 0.998) anchorTs.push(t);
    });
  }
  anchorTs.push(1);
  anchorTs.sort((a, b) => a - b);

  // hoe ver zit deze baan uit het midden op moment t? nul bij elk anker.
  function laneShape(t) {
    let seg = 0;
    while (seg < anchorTs.length - 2 && t > anchorTs[seg + 1]) seg++;
    const ta = anchorTs[seg];
    const tb = anchorTs[seg + 1];
    if (tb - ta < 1e-6) return 0;
    const local = (t - ta) / (tb - ta);
    return Math.pow(Math.sin(Math.PI * local), 0.6);
  }

  // korte routes -> lage boog, lange routes -> volle boog (afgetopt)
  const spanFactor = flat ? 1 : (0.22 + 0.78 * clamp01(totalAngle / 2.1));
  const effLift = lift * spanFactor;
  const base = CONFIG.markers.lift / radius; // zelfde hoogte als de markers

  const SAMPLES = Math.max(48, Math.min(260, Math.round(totalAngle * 85)));

  // ADAPTIEVE bemonstering: zelfde gemiddelde dichtheid als voorheen, maar
  // élk invoerpunt blijft behouden. De gebakken MARNET-paden (M18) zijn dicht
  // bij kusten en dun op open zee; de oude uniforme bemonstering (1 punt per
  // ~75 km bij lange routes) sloeg de dichte kustpunten over, waarna de
  // spline dwars over schiereilanden sneed. De oude A* maskeerde dat met
  // ~130 km geforceerd water rond knelpunten — MARNET scheert echt langs de
  // kust en verdraagt geen overgeslagen punten.
  const stepRad = totalAngle / SAMPLES;
  const centre = []; // { v: eenheidsvector, t: 0..1 langs de route }
  let accAngle = 0;
  for (let i = 0; i < units.length - 1; i++) {
    const n = Math.max(1, Math.ceil(segAngles[i] / stepRad));
    for (let k = 0; k < n; k++) {
      const v = k === 0 ? units[i] : slerpUnit(units[i], units[i + 1], k / n);
      centre.push({ v, t: (accAngle + segAngles[i] * (k / n)) / totalAngle });
    }
    accAngle += segAngles[i];
  }
  centre.push({ v: units[units.length - 1], t: 1 });

  const pts = [];
  const tangent = new THREE.Vector3();
  const side = new THREE.Vector3();

  for (let s = 0; s < centre.length; s++) {
    const tGlobal = centre[s].t;
    const v = centre[s].v.clone();

    let h;
    if (flat) {
      const ease = Math.min(1, Math.min(tGlobal, 1 - tGlobal) / 0.08);
      h = base + effLift * (0.35 + 0.65 * ease);
    } else {
      h = base + Math.sin(Math.PI * tGlobal) * effLift;
    }

    const p = v.clone().multiplyScalar(radius * (1 + h));

    if (lane) {
      const a = centre[Math.max(0, s - 1)].v;
      const b = centre[Math.min(centre.length - 1, s + 1)].v;
      tangent.subVectors(b, a).normalize();
      side.crossVectors(v, tangent).normalize();
      p.addScaledVector(side, lane * laneShape(tGlobal));
    }

    pts.push(p);
  }

  return { curve: new THREE.CatmullRomCurve3(pts), totalAngle };
}

// Ruimt een THREE.Group volledig op (geometrie + materialen vrijgeven).
function clearGroup(g) {
  while (g.children.length) {
    const c = g.children.pop();
    if (c.children && c.children.length) clearGroup(c);
    if (c.geometry) c.geometry.dispose();
    if (c.material) c.material.dispose();
    if (c.material && c.material.map) c.material.map.dispose();
  }
}

// value -> 0..1, relatief aan de grootste waarde in de lijst
function normalize(value, max) {
  if (!max) return 0.5;
  return Math.min(1, Math.max(0, value / max));
}

function flowColorOf(res) {
  return new THREE.Color(res.flowColor || res.color);
}

// Kleur per KETENSTAP, afgeleid van de grondstofkleur:
//   erts       -> gedempt en donker (het ruwe spul, dicht bij de grond)
//   raffinaat  -> de volle grondstofkleur
//   product    -> licht, bijna wit (het eindproduct)
// Zo kun je in één oogopslag zien wáár in de keten een stroom zit.
function stageColorOf(res, stage) {
  const base = flowColorOf(res);
  if (stage === "erts") {
    const hsl = {};
    base.getHSL(hsl);
    return new THREE.Color().setHSL(hsl.h, hsl.s * 0.62, Math.max(0.22, hsl.l * 0.62));
  }
  if (stage === "product") {
    return base.clone().lerp(new THREE.Color(0xffffff), 0.45);
  }
  return base; // raffinaat / default
}
