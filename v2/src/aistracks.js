// aistracks.js — echte scheepstracks als kijk-laag op de bol (M28).
//
// Tekent de track-selectie uit data/aistracks-pilot.json: gevaren lijnen van
// individuele schepen uit VIJF bronnen (MarineCadastre/NOAA · DMA/Denemarken ·
// Kystdatahuset/Noorwegen · AMSA/Australië · de eigen aisstream-collector).
// Dit is de bol-toets van de track-aanpak: ligt één doorvaart als één vloeiende
// lijn ín de geul op satelliet, en zie je op- en afvaart als eigen banen?
//
// ⚠️ KLEUR = RICHTING, NIET BRON — dat is een besluit, geen verzuim.
//   1. De laag bestaat om de vraag hierboven te beantwoorden. Richting is de
//      eigenschap die getoetst wordt; de bron is dat niet.
//   2. De bronnen zijn geografisch bijna disjunct (VS-binnenwater/kust · DK en
//      de Oostzee · NO-fjorden · Australië/Tasman · de collector in NW-Europa).
//      Kleuren op bron verft dus vooral hele wérelddelen over — informatie die
//      je al van de kaart afleest — en kost het enige signaal dat de laag draagt.
//   3. Vijf kleuren op 0,55 doorzichtigheid boven satelliet wordt een brij. Zelfs
//      met twéé kleuren lopen drukke gebieden (Deense straten, Mississippi-delta)
//      al naar wit dicht; dat is een reden om er niet nóg drie bij te doen.
// De bron is daarmee niet weg. Elke lijn draagt zijn `bron`-sleutel en de laag
// bouwt PER BRON een eigen subgroep (elk met een op- en een afvaartmesh). Zo is
// een bron los aan/uit te zetten zonder rebake — `AISTRACKS.zetBron("au", false)`
// vanuit de console is het verschil tussen "is dat een valse las?" en "dat is
// AMSA's korrel van 21 km". De tellingen per bron staan in de HUD-noot, de
// licenties statisch in index.html (AMSA is CC BY-NC 3.0 AU: naamsvermelding
// én niet-commercieel).
//
// Twee kleuren, verder exact de tekendiscipline van aisnet.js: depthTest uit +
// horizonklem, renderOrder boven de tegels, frustumCulled uit.

import * as THREE from "three";

const KLEUR_OP = 0xffd166;   // opvaart — amber
const KLEUR_AF = 0x7fe8ff;   // afvaart — ijsblauw

function opBol(lonDeg, latDeg, r, uit, o) {
  // Exact dezelfde afspraak als world.js/aisnet.js (z = −sin lon).
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  uit[o + 0] = r * c * Math.cos(lon);
  uit[o + 1] = r * Math.sin(lat);
  uit[o + 2] = -r * c * Math.sin(lon);
}

function maakSegmenten(lijnen, radius, kleur, klemOpHorizon) {
  let n = 0;
  for (const l of lijnen) n += l.punten.length - 1;
  if (!n) return null;   // een bron zonder lijnen in deze richting: niets tekenen
  const pos = new Float32Array(n * 6);
  let o = 0;
  for (const l of lijnen) {
    for (let i = 0; i < l.punten.length - 1; i++) {
      opBol(l.punten[i][0], l.punten[i][1], radius, pos, o);
      opBol(l.punten[i + 1][0], l.punten[i + 1][1], radius, pos, o + 3);
      o += 6;
    }
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.LineBasicMaterial({
    color: kleur, transparent: true, opacity: 0.55,
  });
  klemOpHorizon(mat);
  const seg = new THREE.LineSegments(geo, mat);
  seg.renderOrder = 6.6;   // net boven aisnet (6,5), onder landnet (7)
  seg.frustumCulled = false;
  return { seg, segmenten: n };
}

export async function laadAisTracks(radius, versie, klemOpHorizon) {
  const t0 = performance.now();
  const r = await fetch(`data/aistracks-pilot.json?v=${versie}`);
  if (!r.ok) throw new Error(`aistracks-pilot.json: HTTP ${r.status}`);
  const d = await r.json();
  const tLaden = performance.now();

  // Sorteren op bron × richting. De volgorde van `d.bronnen` bepaalt de
  // tekenvolgorde, zodat de bak beslist wie bovenop ligt en niet de toevallige
  // volgorde van de lijnenlijst.
  const sleutels = (d.bronnen || []).map((b) => b.sleutel);
  const perBron = new Map();
  const pak = (s) => {
    if (!perBron.has(s)) perBron.set(s, { op: [], af: [] });
    return perBron.get(s);
  };
  for (const s of sleutels) pak(s);
  for (const l of d.lijnen) {
    pak(l.bron || "onbekend")[l.richting === "op" ? "op" : "af"].push(l);
  }

  const groep = new THREE.Group();
  const bronGroepen = new Map();
  const perBronStats = [];
  let segmenten = 0;
  let lijnen = 0;
  for (const [sleutel, sets] of perBron) {
    const g = new THREE.Group();
    g.name = `aistracks-${sleutel}`;
    let sSeg = 0;
    for (const [richting, kleur] of [["op", KLEUR_OP], ["af", KLEUR_AF]]) {
      const m = maakSegmenten(sets[richting], radius, kleur, klemOpHorizon);
      if (!m) continue;
      g.add(m.seg);
      sSeg += m.segmenten;
    }
    if (!g.children.length) continue;
    groep.add(g);
    bronGroepen.set(sleutel, g);
    segmenten += sSeg;
    lijnen += sets.op.length + sets.af.length;
    perBronStats.push({
      sleutel, lijnen: sets.op.length + sets.af.length,
      op: sets.op.length, af: sets.af.length, segmenten: sSeg,
    });
  }

  return {
    groep,
    bronGroepen,
    bronnen: d.bronnen || null,
    attributie: d.bron,
    // Diagnose-handvat: één bron los aan/uit, zonder rebake en zonder herladen.
    zetBron: (sleutel, aan) => {
      const g = bronGroepen.get(sleutel);
      if (g) g.visible = aan !== false;
      return !!g;
    },
    stats: {
      lijnen,
      segmenten,
      perBron: perBronStats,
      kbOverdracht: Math.round((r.headers.get("content-length") || 0) / 1024) ||
        Math.round(JSON.stringify(d).length / 1024),
      msLaden: Math.round(tLaden - t0),
      msVerwerken: Math.round(performance.now() - tLaden),
    },
  };
}
