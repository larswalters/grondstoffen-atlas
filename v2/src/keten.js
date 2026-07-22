// keten.js — HET KOPPELEN: de vier netten aan elkaar via aangewezen
// knooppunten, en de keten-router die eroverheen zoekt.
//
// Ontwerp: `v2/design/overslag-ontwerp.md` (LAR-518). De drie dragende regels,
// elk met een gemeten doodsoorzaak van het alternatief:
//
//  1. **Een overslag is GEEN edge.** Nul-kost-edges op de kandidaat-havens
//     braken twee invarianten meteen (R'dam→Shanghai 19.610 → 19.604,
//     Duluth→R'dam 8.031 → 7.998). Een overstap is een TOESTANDSSPRONG: een
//     been eindigt, een nieuw been begint, +1 laag.
//  2. **De modaliteit van een punt is AANGEWEZEN, niet gemeten.** Geen enkele
//     afstandsdrempel kan havens classificeren — Manaus is een échte
//     oceaanhaven op 1.084 km zee-snap, Duisburg wordt door geen zeeschip
//     aangelopen op 152 km. Het interval is leeg. Dus: `knooppunten.json`.
//  3. **Lexicografisch: minste overslagen wint, daarbinnen minste km.** Dát is
//     het structurele slot op de Donau-ring: R'dam→Shanghai slaagt met 0
//     overslagen over zee, en een keten dwars door Europa (2 overslagen) wordt
//     nóóit in kilometers vergeleken — er is geen getal om verkeerd te kiezen.
//
// Een been mengt nooit netten: elke knoop hoort bij precies één groep
// (zee · binnen · spoor · weg) en een edge tussen twee groepen bestaat niet.
// Dat is een constructie-eigenschap, geen guard die je moet vertrouwen.

import { gcKmLL, schipGrenzen, edgePast } from "./router.js?v=056";

export const GROEP = { zee: 0, binnen: 1, spoor: 2, weg: 3 };
export const GROEP_NAAM = ["zee", "binnen", "spoor", "weg"];
export const GROEP_VERVOER = {
  zee: "zeeschip",
  binnen: "binnenschip",
  spoor: "trein",
  weg: "vrachtwagen",
};

// --------------------------------------------------------------------------
// koppelen
// --------------------------------------------------------------------------

/**
 * Koppelt marnet + landnet + het aangewezen register tot één zoekruimte.
 *
 * ⚠️ De OFFSET tussen de twee knoopruimtes wordt hier berekend en nergens
 * gebakken: `landnet.bin` heeft bewust lokale knoop-ids (anders snapt elke
 * haven op een spoorknoop, zie landnet.js), en een gebakken offset zou stil
 * verlopen bij een rebake van één van beide netten.
 *
 * @param {object} o.marnet    resultaat van laadMarnet()
 * @param {object} o.landnet   resultaat van laadLandnet(), of null
 * @param {number} o.zeeKnopen aantal zeeknopen in marnet (uit ports.json)
 * @param {object} o.register  knooppunten.json
 */
export function koppelNetten({ marnet, landnet, zeeKnopen, register }) {
  const t0 = (typeof performance !== "undefined" ? performance.now() : Date.now());
  const nMar = marnet.knoopLon.length;
  const nLand = landnet ? landnet.knoopLon.length : 0;
  const nKnopen = nMar + nLand;
  if (!(zeeKnopen > 0 && zeeKnopen <= nMar)) {
    throw new Error(`keten: zeeKnopen (${zeeKnopen}) klopt niet met marnet (${nMar} knopen)`);
  }

  // Groep per landnet-knoop uit de modus van zijn edges. Spoor en weg delen één
  // knoopruimte; raakt een knoop beide, dan is dat GEEN naad maar een
  // toevalligheid van de bake — we tellen ze en laten de edge ertussen niet
  // bestaan (een leg kan er dus nooit doorheen glippen).
  const landGroep = new Uint8Array(nLand);
  let gemengd = 0;
  if (landnet) {
    for (let e = 0; e < landnet.edgeA.length; e++) {
      const g = landnet.edgeModus[e] === 2 ? GROEP.weg : GROEP.spoor;
      for (const k of [landnet.edgeA[e], landnet.edgeB[e]]) {
        if (landGroep[k] === 0) landGroep[k] = g + 1;          // +1: 0 = nog leeg
        else if (landGroep[k] - 1 !== g) gemengd++;
      }
    }
  }

  const groepVan = (u) => {
    if (u < nMar) return u < zeeKnopen ? GROEP.zee : GROEP.binnen;
    const g = landGroep[u - nMar];
    return g ? g - 1 : GROEP.spoor;
  };

  // --- het register snappen -------------------------------------------------
  // De machine meet, de redacteur oordeelt: elke aanhechting krijgt een
  // gemeten snap-afstand mee. Géén drempel — een punt dat niet klopt verraadt
  // zich in dat getal (het Mountain-Pass-patroon uit de wegcorridors).
  const punten = [];
  const gezienId = new Set();
  const vragen = { marnet: [], landnet: [] };

  for (const p of register.punten || []) {
    if (gezienId.has(p.id)) throw new Error(`keten: dubbele knooppunt-id "${p.id}"`);
    gezienId.add(p.id);
    const punt = { id: p.id, naam: p.naam, locode: p.locode || null,
                   bij: p.bij || null, aanhechting: {}, overslag: [] };
    for (const [modus, ll] of Object.entries(p.aanhechting || {})) {
      if (!(modus in GROEP)) throw new Error(`keten: onbekende modaliteit "${modus}" bij ${p.id}`);
      if (!Array.isArray(ll) || ll.length !== 2 || !isFinite(ll[0]) || !isFinite(ll[1])) {
        throw new Error(`keten: onbruikbare coördinaat bij ${p.id}/${modus}`);
      }
      const gcode = GROEP[modus];
      const opLand = gcode === GROEP.spoor || gcode === GROEP.weg;
      if (opLand && !landnet) continue;   // landnet niet gebakken → geen landaanhechting
      punt.aanhechting[modus] = { lon: ll[0], lat: ll[1], knoop: -1, km: Infinity };
      vragen[opLand ? "landnet" : "marnet"].push({ punt, modus, gcode, lon: ll[0], lat: ll[1] });
    }
    punt.overslag = (p.overslag || []).filter(
      ([a, b]) => punt.aanhechting[a] && punt.aanhechting[b]
    );
    punten.push(punt);
  }

  // Eén pass per net over alle knopen; per knoop alleen de vragen van dezelfde
  // groep. Goedkoper dan per vraag het hele net aflopen en exact even nauwkeurig.
  snapVragen(marnet, 0, (k) => (k < zeeKnopen ? GROEP.zee : GROEP.binnen), vragen.marnet);
  if (landnet) snapVragen(landnet, nMar, (k) => (landGroep[k] ? landGroep[k] - 1 : GROEP.spoor), vragen.landnet);

  for (const lijst of [vragen.marnet, vragen.landnet]) {
    for (const v of lijst) {
      const a = v.punt.aanhechting[v.modus];
      if (a.knoop < 0) {
        // Hard falen, nooit stil overslaan: een aangewezen punt dat nergens op
        // snapt is een redactiefout die zichtbaar moet worden.
        throw new Error(`keten: "${v.punt.id}" vindt geen ${v.modus}-knoop`);
      }
    }
  }

  // --- de overstappen -------------------------------------------------------
  // Eén per richting, over een EXPLICIET knopenpaar uit de entry zelf. Nooit
  // "een aangewezen haven raakt deze knoop": 3.962 havens delen 1.854 zeeknopen
  // en knoop 6811 draagt er 22, van Antwerpen tot Straatsburg — dat zou een
  // gratis teleport voor alle 22 zijn.
  const overstappen = [];
  const bijKnoop = new Map();          // knoop → indices in overstappen
  for (const p of punten) {
    for (const [a, b] of p.overslag) {
      for (const [van, naar] of [[a, b], [b, a]]) {
        const A = p.aanhechting[van], B = p.aanhechting[naar];
        const idx = overstappen.length;
        overstappen.push({
          punt: p.id, naam: p.naam, van, naar,
          knoopA: A.knoop, knoopB: B.knoop,
          // De fysieke sprongafstand telt mee in de kilometers — een overslag
          // is geen wormgat. Rotterdam kade→emplacement is ~3 km en dat hoort
          // in het antwoord.
          km: gcKmLL(A.lon, A.lat, B.lon, B.lat),
        });
        if (!bijKnoop.has(A.knoop)) bijKnoop.set(A.knoop, []);
        bijKnoop.get(A.knoop).push(idx);
      }
    }
  }

  const opLocode = new Map();
  for (const p of punten) if (p.locode) opLocode.set(p.locode, p);

  const t1 = (typeof performance !== "undefined" ? performance.now() : Date.now());
  return {
    marnet, landnet, zeeKnopen,
    nMar, nLand, nKnopen, offsetLand: nMar,
    groepVan, landGroep,
    punten, overstappen, bijKnoop, opLocode,
    stats: {
      knopen: nKnopen,
      punten: punten.length,
      overstappen: overstappen.length / 2,
      gemengdeLandknopen: gemengd,
      ergsteSnapKm: punten.reduce((m, p) => Math.max(m,
        ...Object.values(p.aanhechting).map((a) => a.km)), 0),
      msKoppelen: Math.round(t1 - t0),
    },
  };
}

function snapVragen(net, offset, groepVanLokaal, vragen) {
  if (!vragen.length) return;
  const perGroep = new Map();
  for (const v of vragen) {
    const q = {
      v,
      x: Math.cos(v.lat * Math.PI / 180) * Math.cos(v.lon * Math.PI / 180),
      y: Math.sin(v.lat * Math.PI / 180),
      z: Math.cos(v.lat * Math.PI / 180) * Math.sin(v.lon * Math.PI / 180),
      besteDot: -2, besteK: -1,
    };
    if (!perGroep.has(v.gcode)) perGroep.set(v.gcode, []);
    perGroep.get(v.gcode).push(q);
  }
  const n = net.knoopLon.length;
  for (let k = 0; k < n; k++) {
    const lijst = perGroep.get(groepVanLokaal(k));
    if (!lijst) continue;
    const nx = net.knoopXYZ[k * 3], ny = net.knoopXYZ[k * 3 + 1], nz = net.knoopXYZ[k * 3 + 2];
    for (const q of lijst) {
      const d = nx * q.x + ny * q.y + nz * q.z;
      if (d > q.besteDot) { q.besteDot = d; q.besteK = k; }
    }
  }
  for (const lijst of perGroep.values()) {
    for (const q of lijst) {
      if (q.besteK < 0) continue;
      const a = q.v.punt.aanhechting[q.v.modus];
      a.knoop = q.besteK + offset;
      a.km = 6371 * Math.acos(Math.max(-1, Math.min(1, q.besteDot)));
      // ⚠️ marnet.js draait de x/z-afspraak om bij het tekenen (z = −sin lon),
      // maar knoopXYZ gebruikt +sin — hier dus consequent knoopXYZ.
      a.knoopLon = net.knoopLon[q.besteK];
      a.knoopLat = net.knoopLat[q.besteK];
    }
  }
}

// --------------------------------------------------------------------------
// de keten-router
// --------------------------------------------------------------------------

/** Groeiende binaire heap — groeit i.p.v. stil over de rand te schrijven. */
function maakHeap(capaciteit) {
  let f = new Float64Array(capaciteit);
  let k = new Int32Array(capaciteit);
  let n = 0;
  return {
    get lengte() { return n; },
    push(fv, kv) {
      if (n >= k.length) {
        const nf = new Float64Array(k.length * 2); nf.set(f); f = nf;
        const nk = new Int32Array(k.length * 2); nk.set(k); k = nk;
      }
      let i = n++;
      while (i > 0) {
        const p = (i - 1) >> 1;
        if (f[p] <= fv) break;
        f[i] = f[p]; k[i] = k[p];
        i = p;
      }
      f[i] = fv; k[i] = kv;
    },
    pop() {
      const top = k[0];
      const fv = f[--n], kv = k[n];
      let i = 0;
      while (true) {
        const l = i * 2 + 1, r = l + 1;
        let kl = i;
        if (l < n && f[l] < (kl === i ? fv : f[kl])) kl = l;
        if (r < n && f[r] < (kl === i ? fv : f[kl])) kl = r;
        if (kl === i) break;
        f[i] = f[kl]; k[i] = k[kl];
        i = kl;
      }
      f[i] = fv; k[i] = kv;
      return top;
    },
  };
}

/**
 * Eén laag: multi-source Dijkstra over de gekoppelde graaf, waarbij een been
 * per constructie binnen één groep blijft.
 *
 * Multi-source is hier gratis (alle zaden in dezelfde heap) — dat is precies
 * waarom dit ontwerp geen paren-probleem heeft: de kosten hangen niet af van
 * de lengte van de aangewezen lijst.
 *
 * ⚠️ Zaadkosten tellen mee in `g`. Gemeten noodzakelijk: zonder de aanloop in
 * de kosten wint een onzinroute naar een knoop 304 km naast Cincinnati.
 */
function laagDijkstra(K, zaden, filter) {
  const { marnet, landnet, nMar, nKnopen } = K;
  const g = new Float64Array(nKnopen).fill(Infinity);
  const prevE = new Int32Array(nKnopen).fill(-1);
  const prevK = new Int32Array(nKnopen).fill(-1);
  const dicht = new Uint8Array(nKnopen);
  const zaadInfo = new Map();
  const heap = maakHeap(Math.max(1024, zaden.length * 4));

  for (const z of zaden) {
    if (z.km < g[z.knoop]) {
      g[z.knoop] = z.km;
      zaadInfo.set(z.knoop, z.info);
      heap.push(z.km, z.knoop);
    }
  }

  let bezocht = 0;
  while (heap.lengte > 0) {
    const u = heap.pop();
    if (dicht[u]) continue;
    dicht[u] = 1;
    bezocht++;
    const opLand = u >= nMar;
    const net = opLand ? landnet : marnet;
    if (!net) continue;
    const lu = opLand ? u - nMar : u;
    const groepU = K.groepVan(u);
    for (let a = net.adjStart[lu]; a < net.adjStart[lu + 1]; a++) {
      const lb = net.adjKnoop[a];
      const buur = opLand ? lb + nMar : lb;
      if (dicht[buur]) continue;
      // Een been mengt nooit netten (constructie-eigenschap, geen guard).
      if (K.groepVan(buur) !== groepU) continue;
      const e = net.adjEdge[a];
      if (!filter(opLand, e, groepU)) continue;
      const ng = g[u] + net.edgeKm[e];
      if (ng < g[buur]) {
        g[buur] = ng;
        prevE[buur] = e;
        prevK[buur] = u;
        heap.push(ng, buur);
      }
    }
  }
  return { g, prevE, prevK, zaadInfo, bezocht };
}

/**
 * `zoekKeten(K, bronnen, doelen, opties)` — een route als KETEN van benen, met
 * een overstap op een aangewezen knooppunt.
 *
 * bronnen/doelen: [{ knoop, km, naam }] — `km` is de aanloop (haven → knoop),
 * die eerlijk meetelt. Meerdere zaden per uiteinde is normaal: een zeehaven met
 * een rivieraanhechting levert er twee, en de goedkoopste wint vanzelf.
 *
 * opties:
 *   netten       — welke groepen open staan (default ["zee","binnen"]; het
 *                  standaardprofiel SLUIT het landnet, want een zuivere
 *                  spoorroute heeft 0 overslagen en zou lexicografisch van zee
 *                  winnen — 7 van de 11 invarianten kantelen dan naar een trein.
 *                  De modus per been komt in de simulator uit de flows-data.)
 *   maxOverstap  — default 2 ("3 schepen, niet 1")
 *   vermijd      — passage-labels (default ["northwest"], = searoute's default)
 *   schipZee / schipBinnen — maten per been, niet één schip over de hele reis
 */
export function zoekKeten(K, bronnen, doelen, opties = {}) {
  const t0 = (typeof performance !== "undefined" ? performance.now() : Date.now());
  const netten = new Set(opties.netten ?? ["zee", "binnen"]);
  const maxOverstap = opties.maxOverstap ?? 2;
  const vermijd = new Set(opties.vermijd ?? ["northwest"]);
  const grenzenZee = schipGrenzen(opties.schipZee);
  const grenzenBinnen = schipGrenzen(opties.schipBinnen);

  const filter = (opLand, e, groepU) => {
    if (opLand) return true;                       // landnet draagt geen maten
    const label = K.marnet.edgeLabel[e];
    if (label !== null && vermijd.has(label)) return false;
    const grenzen = groepU === GROEP.zee ? grenzenZee : grenzenBinnen;
    if (grenzen && !edgePast(K.marnet, e, grenzen)) return false;
    return true;
  };

  const open = (knoop) => netten.has(GROEP_NAAM[K.groepVan(knoop)]);
  const bronOpen = bronnen.filter((b) => b.knoop >= 0 && open(b.knoop));
  const doelOpen = doelen.filter((d) => d.knoop >= 0 && open(d.knoop));
  if (!bronOpen.length || !doelOpen.length) {
    return geenPad(
      !bronOpen.length
        ? "het vertrekpunt heeft geen aanhechting op een open net"
        : "de bestemming heeft geen aanhechting op een open net",
      { bronnen, doelen, netten: [...netten] }
    );
  }

  let zaden = bronOpen.map((b) => ({
    knoop: b.knoop, km: b.km,
    info: { type: "start", naam: b.naam || "", groep: GROEP_NAAM[K.groepVan(b.knoop)], aanloopKm: b.km },
  }));
  const lagen = [];

  for (let L = 0; L <= maxOverstap; L++) {
    const laag = laagDijkstra(K, zaden, filter);
    lagen.push(laag);

    let beste = null;
    for (const d of doelOpen) {
      const g = laag.g[d.knoop];
      if (!isFinite(g)) continue;
      const totaal = g + d.km;
      if (!beste || totaal < beste.totaal) beste = { totaal, doel: d };
    }
    if (beste) {
      const uit = bouwKeten(K, lagen, L, beste.doel);
      uit.km = beste.totaal;
      uit.overslagen = L;
      uit.ms = Math.round((typeof performance !== "undefined" ? performance.now() : Date.now()) - t0);
      uit.bezocht = lagen.reduce((s, l) => s + l.bezocht, 0);
      return uit;
    }
    if (L === maxOverstap) break;

    // Zaden voor de volgende laag: elke aangewezen overstap waarvan de A-kant
    // in deze laag bereikbaar is.
    const volgende = new Map();
    for (const [knoopA, idxs] of K.bijKnoop) {
      const gA = laag.g[knoopA];
      if (!isFinite(gA)) continue;
      for (const i of idxs) {
        const o = K.overstappen[i];
        if (!netten.has(o.van) || !netten.has(o.naar)) continue;
        const kost = gA + o.km;
        const oud = volgende.get(o.knoopB);
        if (!oud || kost < oud.km) {
          volgende.set(o.knoopB, {
            knoop: o.knoopB, km: kost,
            info: { type: "overslag", punt: o.punt, naam: o.naam, van: o.van,
                    naar: o.naar, vanKnoop: knoopA, sprongKm: o.km },
          });
        }
      }
    }
    zaden = [...volgende.values()];
    if (!zaden.length) break;
  }

  // --- geen pad: zeg waaróm (besluit 6 uit het ontwerp) ---------------------
  let reden = "de netten zijn hier niet verbonden — geen aangewezen overslagpunt op de route";
  if (grenzenZee || grenzenBinnen) {
    const zonderMaat = zoekKeten(K, bronnen, doelen,
      { ...opties, schipZee: null, schipBinnen: null });
    if (!zonderMaat.geenPad) {
      reden = "de maat past niet: er is wél een keten, maar niet voor dit schip";
    }
  }
  if (lagen.length > maxOverstap) {
    reden = `meer dan ${maxOverstap} overslagen nodig`;
  }
  return geenPad(reden, {
    netten: [...netten],
    bronGroepen: [...new Set(bronOpen.map((b) => GROEP_NAAM[K.groepVan(b.knoop)]))],
    doelGroepen: [...new Set(doelOpen.map((d) => GROEP_NAAM[K.groepVan(d.knoop)]))],
    ms: Math.round((typeof performance !== "undefined" ? performance.now() : Date.now()) - t0),
  });
}

function geenPad(reden, extra = {}) {
  return { geenPad: true, reden, ...extra };
}

/** Loopt de lagen terug en knipt het pad in benen, met de overstappen ertussen. */
function bouwKeten(K, lagen, laagIdx, doel) {
  const benen = [];
  const overstappen = [];
  let L = laagIdx;
  let k = doel.knoop;
  let staart = { naam: doel.naam || "", km: doel.km };

  while (true) {
    const laag = lagen[L];
    const knopen = [k];
    const edges = [];
    while (laag.prevK[k] !== -1) {
      edges.push(laag.prevE[k]);
      k = laag.prevK[k];
      knopen.push(k);
    }
    edges.reverse();
    knopen.reverse();
    const opLand = k >= K.nMar;
    const net = opLand ? K.landnet : K.marnet;
    let km = 0;
    for (const e of edges) km += net.edgeKm[e];
    const info = laag.zaadInfo.get(k);
    benen.unshift({
      groep: GROEP_NAAM[K.groepVan(k)],
      vervoer: GROEP_VERVOER[GROEP_NAAM[K.groepVan(k)]],
      net: opLand ? "landnet" : "marnet",
      // knopen/edges zijn LOKALE ids in dat net — precies wat bouwRouteLijn wil
      knopen: knopen.map((u) => (opLand ? u - K.nMar : u)),
      edges,
      km,
      // wat er vóór dit been aan aanloop of sprong zat
      begin: info,
      eind: staart,
    });
    if (!info || info.type === "start") break;
    overstappen.unshift({
      punt: info.punt, naam: info.naam, van: info.van, naar: info.naar, km: info.sprongKm,
    });
    staart = { naam: `overslag ${info.naam}`, km: 0 };
    L -= 1;
    k = info.vanKnoop;
  }

  const aanloopKm = (benen[0].begin?.aanloopKm || 0) + (doel.km || 0);
  return {
    geenPad: false,
    benen,
    overstappen,
    aanloopKm,
    sprongKm: overstappen.reduce((s, o) => s + o.km, 0),
    netKm: benen.reduce((s, b) => s + b.km, 0),
  };
}

/**
 * Zaden voor een haven: zee- én rivieraanhechting, elk met zijn eigen aanloop.
 *
 * ⚠️ Is de haven een AANGEWEZEN knooppunt, dan tellen alléén de aangewezen
 * modaliteiten — dat is de kern van het ontwerp (§2, besluit 2). Cincinnati
 * heeft een zee-snap op 304 km (de zee komt daar over land, niet over water);
 * zonder deze regel neemt de keten-router die 304 km als een "0-overslag
 * zeereis" en tekent hij een zeeschip in Ohio. Het interval is leeg — geen
 * drempel kan dit classificeren, dus doet de redacteur het: Cincinnati is
 * aangewezen als binnen+spoor, niet zee.
 *
 * Een haven die NIET in het register staat (de duizenden gewone havens) zaait
 * op het net waar hij het DICHTST bij ligt — en alleen dáár. Dat is de fix voor
 * Karlsruhe→elders: Karlsruhe is een Rijnhaven met een zee-snap op 360 km (de
 * zee komt daar over de Rijn, niet dwars over land), en zonder deze regel wint
 * een "zeeschip" dat 360 km landinwaarts begint lexicografisch van de eerlijke
 * rivier→overslag→zee-keten — met een aanloop die niet eens getekend wordt, dus
 * de lijn lijkt zomaar in zee te stoppen.
 *
 * Waarom geen dubbel zaad meer voor een gewone haven: een verre zee-aanloop is
 * geen "duur maar geldig" zaad maar een fysieke onwaarheid (hij kruist land).
 * Een haven die écht op twee netten ligt (kade + riviermond) is precies een
 * overslagkandidaat en hoort dan in het register — daar krijgt hij zijn tweede
 * aanhechting terug, aangewezen in plaats van geraden.
 *
 * ⚠️ GEEN afstandsdrempel: het interval is leeg (Antofagasta is een échte
 * zeehaven op 91 km zee-snap, Duisburg een binnenhaven op 152 km). "Dichtste
 * net" is een RELATIEVE keuze en heeft dat probleem niet — Antofagasta's zee
 * (91) verslaat zijn rivier (304), Karlsruhe's rivier (2) verslaat zijn zee
 * (360). Geen magisch getal.
 */
export function havenZaden(K, haven) {
  const punt = haven.locode ? K.opLocode.get(haven.locode) : null;
  if (punt) {
    const zaden = [];
    for (const [modus, a] of Object.entries(punt.aanhechting)) {
      // alleen zee/binnen dragen een haven-zaad; spoor/weg-zaden komen via
      // puntZaden als het punt zélf het vertrek/doel is
      if ((modus === "zee" || modus === "binnen") && a.knoop >= 0) {
        zaden.push({ knoop: a.knoop, km: a.km, naam: haven.naam });
      }
    }
    if (zaden.length) return zaden;
    // een register-punt zonder zee/binnen (bv. Kasumbalesa) valt hieronder door
  }
  const heeftZee = haven.knoop >= 0 && haven.afstandKm >= 0;
  const heeftRivier = haven.knoopRivier >= 0 && haven.afstandRivierKm >= 0;
  if (heeftZee && heeftRivier) {
    // het dichtste net wint — geen teleport over land naar het andere net
    return haven.afstandKm <= haven.afstandRivierKm
      ? [{ knoop: haven.knoop, km: haven.afstandKm, naam: haven.naam }]
      : [{ knoop: haven.knoopRivier, km: haven.afstandRivierKm, naam: haven.naam }];
  }
  if (heeftZee) return [{ knoop: haven.knoop, km: haven.afstandKm, naam: haven.naam }];
  if (heeftRivier) return [{ knoop: haven.knoopRivier, km: haven.afstandRivierKm, naam: haven.naam }];
  return [];
}

/** Zaden voor een aangewezen knooppunt: elke modaliteit die het punt draagt. */
export function puntZaden(K, punt) {
  return Object.entries(punt.aanhechting).map(([modus, a]) => ({
    knoop: a.knoop, km: a.km, naam: `${punt.naam} (${modus})`,
  }));
}
