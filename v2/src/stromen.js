// stromen.js — DE WERKELIJKE STROMEN op de bol (M26.1).
//
// Dit is bewust NIET de simulator. De flows-data in `data/*.js` kent de keten al
// (`via:`) én de modus per been (`mode:`), en het overslag-ontwerp heeft dat
// expliciet als uitgangspunt genomen (§5.2):
//
//   "De atlas hoeft de modal split niet te raden — de flows-data draagt al
//    `mode` per been. De simulator routeert bekende stromen langs hun opgegeven
//    ketens; hij verzint geen vervoerskeuze."
//
// Dus: een stroom is een RIJ AANSLUITINGEN (laadplek → kade → kade → losplek) en
// per been zoeken we op precies één net. De overslag is daarmee geen zoekactie
// meer maar een FEIT — twee opeenvolgende benen liggen op verschillende netten,
// op dezelfde plek. `zoekKeten` blijft ongemoeid voor de vrije haven→haven-vraag.
//
// Ontwerp: `v2/design/stroom-aansluiting.md`.

import { zoekKeten, aansluitingZaden, GROEP_VERVOER } from "./keten.js?v=066";

// --------------------------------------------------------------------------
// laden
// --------------------------------------------------------------------------

export async function laadStromen(versie = "065") {
  const [aansluitingen, stromen, pijpleidingen] = await Promise.all([
    haal(`data/aansluitingen.json?v=${versie}`),
    haal(`data/stromen-pilot.json?v=${versie}`),
    // De slurry-leidingen zijn TEKENGEOMETRIE, geen net (zelfde rolverdeling als
    // de bulklaag, LAR-515). Ontbreken ze, dan valt het been terug op de rechte
    // lijn — de atlas hoort daar niet op te stranden.
    haal(`data/pijpleidingen.json?v=${versie}`).catch(() => null),
  ]);
  return { aansluitingen, stromen, pijpleidingen };
}

async function haal(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`${url}: HTTP ${r.status}`);
  return r.json();
}

// --------------------------------------------------------------------------
// routeren
// --------------------------------------------------------------------------

/**
 * Routeert één stroom been voor been over de gekoppelde netten.
 *
 * Elk been krijgt precies één net mee en `maxOverstap: 0`: binnen een been mag
 * niets van modaliteit wisselen. Dat is geen guard die we moeten vertrouwen maar
 * een constructie-eigenschap van de graaf (er bestaat geen edge tussen twee
 * groepen) — de optie maakt het alleen expliciet.
 *
 * Een been zónder net (`net: null`) is een EERLIJK GAT: een pijpleiding, een
 * transportband, een corridor die de atlas nog niet als net kent. Dat wordt een
 * rechte lijn mét reden — niet stiekem over de weg gerouteerd, want dan teken je
 * een vrachtwagen waar een pijp ligt.
 */
export function routeerStroom(K, stroom, aansluitingOp, leidingOp = null) {
  const benen = [];
  let totaalKm = 0;
  let gaten = 0;

  for (const b of stroom.benen) {
    const van = aansluitingOp(b.van);
    const naar = aansluitingOp(b.naar);
    if (!van || !naar) {
      benen.push({ ...b, status: "onbekend",
                   reden: `aansluiting ${!van ? b.van : b.naar} bestaat niet` });
      gaten++;
      continue;
    }

    if (!b.net) {
      // ⚠️ EEN EIGEN VERBINDING IS GEEN GAT — Lars' onderscheid, en het is het
      // juiste: een weg, spoor of vaarweg is PRODUCTONAFHANKELIJK (iedereen mag
      // erover, dus loont het om er een graaf van te maken waar je overheen kunt
      // zoeken en omheen kunt routeren). Een slurryleiding is dat niet: daar gaat
      // precies één ding doorheen, van één mijn naar één kade. Als net levert hij
      // niets op, want er is geen andere lading die hem zou kunnen gebruiken.
      //
      // Dus zodra we de geometrie hébben, is dit been COMPLEET. Niet-routeerbaar
      // zijn is hier geen tekortkoming maar de aard van het ding. Een gat is
      // "de atlas mist een net dat er hoort te zijn" — het havenspoor van Beilun,
      // want spoor is wél productonafhankelijk en zou moeten aansluiten.
      const leiding = b.geometrie && leidingOp ? leidingOp(b.geometrie) : null;
      if (leiding) {
        benen.push({ ...b, status: "eigen", van, naar, km: leiding.km,
                     punten: leiding.punten, leiding,
                     vervoer: b.modus || "eigen verbinding" });
        totaalKm += leiding.km;
        continue;
      }
      // Zonder geometrie weten we niet waar het loopt — en DAT is het gat.
      const km = gcKmLL(van.lon, van.lat, naar.lon, naar.lat);
      benen.push({ ...b, status: "onbekend", van, naar, km, punten: null, leiding: null,
                   reden: b.reden || "we weten niet waar deze verbinding loopt" });
      totaalKm += km;
      gaten++;
      continue;
    }

    const uit = zoekKeten(
      K,
      aansluitingZaden(K, van, [b.net]),
      aansluitingZaden(K, naar, [b.net]),
      { netten: [b.net], maxOverstap: 0,
        ...(b.schip ? { schipZee: b.schip, schipBinnen: b.schip } : {}) }
    );

    if (uit.geenPad) {
      benen.push({ ...b, status: "geenPad", van, naar,
                   reden: verklaarGeenPad(K, b, van, naar) || uit.reden });
      gaten++;
      continue;
    }

    // maxOverstap 0 ⇒ precies één been terug. Assert i.p.v. aanname: als dit
    // ooit meer wordt, is er een overstap binnen een been geslopen en dan klopt
    // het hele modus-label niet meer.
    if (uit.benen.length !== 1) {
      throw new Error(`stromen: been ${b.van}→${b.naar} gaf ${uit.benen.length} deelbenen`);
    }
    const been = uit.benen[0];
    // ⚠️ SNOEIEN OP DE DICHTSTE NADERING. Een been eindigt op de dichtstbijzijnde
    // KNOOP, en knopen liggen op kruisingen en verder elke ~10 km — dus de
    // laatste knoop ligt geregeld vóórbij de terminal. Ongesnoeid vaart het
    // schip de haven voorbij en komt via de last mile terug (Lars: "anders vaart
    // de boot ervoorbij en dan terug naar de overslaghaven").
    //
    // Dit is dezelfde val die `landnet-aanhecht.json` al een keer opleverde: een
    // knoop-afstand meet niet waar de LIJN het dichtst langs komt. Snoeien lost
    // dat op zonder rebake — we knippen het been af op het punt van dichtste
    // nadering en laten de last mile daar beginnen.
    const net = b.net === "spoor" || b.net === "weg" ? K.landnet : K.marnet;
    const gesnoeid = snoeiUiteinden(net, been, van, naar);
    benen.push({
      ...b, status: "ok", van, naar,
      km: uit.km - gesnoeid.wegKm, route: been, gesnoeidKm: gesnoeid.wegKm,
      vervoer: b.modus || GROEP_VERVOER[b.net] || b.net,
      // De last mile is het stuk kade → het punt waar het been nu écht begint
      // en eindigt (ná het snoeien), aan beide kanten. Apart bijgehouden omdat
      // het precies het getal is dat zegt waar het net ophoudt.
      lastMileKm: gesnoeid.lastMileKm,
      // waar het been ná het snoeien écht begint en eindigt — de last mile
      // wordt hiernaartoe getekend, niet naar de oude knoop
      vanLL: gesnoeid.vanLL, naarLL: gesnoeid.naarLL,
    });
    totaalKm += uit.km - gesnoeid.wegKm;
  }

  return { stroom, benen, km: totaalKm, gaten,
           overslagen: telOverslagen(benen) };
}

/**
 * Knipt aan beide uiteinden het stuk weg dat vóórbij de aansluiting ligt.
 *
 * ⚠️ Werkt op VERTEX-niveau, en dat is het hele punt. Op knoopniveau doet deze
 * functie per definitie NIETS: het uiteinde van een been ís al de knoop die het
 * dichtst bij de kade ligt (daar is op gezaaid). De overvaar-lus zit dus niet
 * tussen de knopen maar erbínnen — in de lijngeometrie die knopen van ~10 km
 * uit elkaar overspant. Gemeten in Shanghai: dichtstbijzijnde knoop 10,7 km,
 * dichtste nadering van de lijn 4,5 km.
 *
 * De nóg fijnere variant (de edge openknippen op een nieuwe vertex, zoals
 * `hecht_aan_keten()` in de baker doet) hoort in de bake thuis, niet hier.
 *
 * Muteert `been` (knipVan/knipNaar/km) en geeft terug hoeveel km eraf ging, wat
 * de last mile daarna is, en waar het been nu begint en eindigt.
 */
function snoeiUiteinden(net, been, van, naar) {
  const pts = beenPunten(net, been);
  if (pts.n < 2) return { wegKm: 0, lastMileKm: 0 };

  // Dichtste nadering, per vertex, in XYZ — geen trigonometrie per punt nodig:
  // op de eenheidsbol is de grootste dot de kleinste hoek.
  const dichtste = (a) => {
    const la = a.lat * Math.PI / 180, lo = a.lon * Math.PI / 180, c = Math.cos(la);
    const ax = c * Math.cos(lo), ay = Math.sin(la), az = c * Math.sin(lo);
    let besteI = 0, besteDot = -Infinity;
    for (let i = 0; i < pts.n; i++) {
      // ⚠️ posities gebruiken z = −sin(lon) (tekenafspraak van marnet.js),
      // knoopXYZ +sin. Hier dus het teken omdraaien, anders spiegelt de meting
      // over de meridiaan en snoei je aan de verkeerde kant.
      const d = pts.x[i] * ax + pts.y[i] * ay + (-pts.z[i]) * az;
      if (d > besteDot) { besteDot = d; besteI = i; }
    }
    // ⚠️ De posities liggen op de BOLSTRAAL (2,4), niet op de eenheidsbol. De
    // vergelijking hierboven is daar ongevoelig voor (alles schaalt mee), maar
    // de hoek niet: zonder normaliseren klemt acos op 1 en meldt elke last mile
    // 0,0 km. Precies het soort stille meetfout dat dit project vaker heeft
    // gezien — de keuze klopte, het getal niet.
    return { i: besteI, km: 6371 * Math.acos(Math.max(-1, Math.min(1, besteDot / pts.straal))) };
  };

  const start = dichtste(van);
  const eind = dichtste(naar);
  if (!(start.i < eind.i)) return { wegKm: 0, lastMileKm: start.km + eind.km };

  const voor = pts.kmTot[pts.n - 1];
  been.knipVan = start.i;
  been.knipNaar = eind.i;
  been.km = pts.kmTot[eind.i] - pts.kmTot[start.i];
  return { wegKm: Math.max(0, voor - been.km), lastMileKm: start.km + eind.km,
           vanLL: pts.ll(start.i), naarLL: pts.ll(eind.i) };
}

/**
 * De volledige getekende polylijn van een been, in dezelfde volgorde als
 * `routeLijn()` hem opbouwt, plus de cumulatieve kilometers.
 *
 * Bewust op VERTEX-niveau en niet op knoopniveau: knopen liggen op kruisingen
 * en verder elke ~10 km, dus de dichtstbijzijnde KNOOP is bijna nooit het punt
 * waar de vaarweg het dichtst langs de kade komt. Dat verschil is exact de
 * meetfout die dit project al eens maakte op `landnet-aanhecht.json` — en het
 * is hier zichtbaar als een schip dat de haven voorbijvaart en terugkomt.
 */
function beenPunten(net, been) {
  const xs = [], ys = [], zs = [];
  let bij = been.knopen[0];
  for (const e of been.edges) {
    const start = net.geomStart[e], n = net.geomN[e];
    const vooruit = net.edgeA[e] === bij;
    for (let k = 0; k < n; k++) {
      const idx = vooruit ? start + k : start + (n - 1 - k);
      // opeenvolgende edges delen hun eindvertex — niet dubbel opnemen
      if (k === 0 && xs.length) continue;
      xs.push(net.posities[idx * 3]);
      ys.push(net.posities[idx * 3 + 1]);
      zs.push(net.posities[idx * 3 + 2]);
    }
    bij = vooruit ? net.edgeB[e] : net.edgeA[e];
  }
  const n = xs.length;
  const straal = n ? Math.hypot(xs[0], ys[0], zs[0]) : 1;
  const kmTot = new Float64Array(n);
  for (let i = 1; i < n; i++) {
    const dot = (xs[i] * xs[i - 1] + ys[i] * ys[i - 1] + zs[i] * zs[i - 1]) / (straal * straal);
    kmTot[i] = kmTot[i - 1] + 6371 * Math.acos(Math.max(-1, Math.min(1, dot)));
  }
  return {
    n, x: xs, y: ys, z: zs, kmTot, straal,
    ll: (i) => {
      const r = Math.hypot(xs[i], ys[i], zs[i]);
      return [Math.atan2(-zs[i], xs[i]) * 180 / Math.PI, Math.asin(ys[i] / r) * 180 / Math.PI];
    },
  };
}

/**
 * Waaróm heeft dit been geen pad? Besluit 6 uit het overslag-ontwerp: "geen
 * pad" moet een reden dragen, anders is het niet te onderscheiden van een
 * kapotte feature.
 *
 * Op één net binnen één been is er maar één interessante oorzaak, en die is
 * exact meetbaar: **de twee aansluitingen liggen op verschillende componenten**.
 * De generieke boodschap van `zoekKeten` ("meer dan 0 overslagen nodig") klopt
 * formeel maar zegt niets — hier staat het getal dat wél iets zegt, inclusief
 * de omvang van beide componenten. Een havenspoor van 1.800 km dat losligt van
 * een hoofdnet van 400.000 km is een gat in de bake, geen routeerfout.
 */
function verklaarGeenPad(K, been, van, naar) {
  const kA = van.aanhechting[been.net]?.knoop;
  const kB = naar.aanhechting[been.net]?.knoop;
  if (!(kA >= 0) || !(kB >= 0)) return null;

  // Land en water hebben elk hun eigen componenttabel; de vraag is dezelfde.
  const opLand = been.net === "spoor" || been.net === "weg";
  const comp = opLand ? K.landComp : K.marComp;
  const compKm = opLand ? K.landCompKm : K.marCompKm;
  if (!comp || !comp.length) return null;
  const idx = (k) => (opLand ? k - K.nMar : k);

  const cA = comp[idx(kA)], cB = comp[idx(kB)];
  if (cA === cB) return null;                    // andere oorzaak — niet raden
  const km = (k) => Math.round(compKm[idx(k)]).toLocaleString("nl");
  return `de twee aansluitingen liggen op verschillende ${been.net}-componenten ` +
         `(${km(kA)} km bij "${van.naam.split(" — ")[0]}" vs ${km(kB)} km bij ` +
         `"${naar.naam.split(" — ")[0]}") — een gat in de bake, geen routeerfout`;
}

/** Een overslag = twee opeenvolgende benen op verschillende netten. */
function telOverslagen(benen) {
  // Een been draagt zijn modaliteit: het net waarover het loopt, of "eigen" voor
  // een toegewijde verbinding (pijpleiding). Van leiding naar schip wisselt de
  // lading wel degelijk van vervoermiddel, dus dát is ook een overslag.
  const soort = (b) => (b.status === "eigen" ? b.modus || "eigen" : b.net);
  const punten = [];
  for (let i = 1; i < benen.length; i++) {
    const a = benen[i - 1], b = benen[i];
    const sa = soort(a), sb = soort(b);
    if (!sa || !sb || sa === sb) continue;
    punten.push({ bij: b.van, van: sa, naar: sb });
  }
  return punten;
}

function gcKmLL(lon1, lat1, lon2, lat2) {
  const r = Math.PI / 180;
  const d = Math.sin(lat1 * r) * Math.sin(lat2 * r) +
    Math.cos(lat1 * r) * Math.cos(lat2 * r) * Math.cos((lon2 - lon1) * r);
  return 6371 * Math.acos(Math.max(-1, Math.min(1, d)));
}

