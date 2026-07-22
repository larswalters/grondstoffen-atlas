// router.js — de routeerfuncties van het zeenet, ZONDER three.js.
//
// Bewust een eigen module: deze functies stonden in `marnet.js`, maar die
// importeert three en kan dus alleen in een browser draaien. Sinds er een
// headless toets is (`v2/tools/toets_routes.mjs`) moet de test de ÉCHTE router
// kunnen aanroepen in plaats van een kopie — een tweede implementatie van een
// A* is precies het soort ding dat een half jaar later stilletjes uit de pas
// loopt. `marnet.js` her-exporteert alles hieronder, dus voor de browser
// verandert er niets.

const R_AARDE = 6371;

export function gcKm(net, i, j) {
  const d = net.knoopXYZ[i * 3] * net.knoopXYZ[j * 3]
    + net.knoopXYZ[i * 3 + 1] * net.knoopXYZ[j * 3 + 1]
    + net.knoopXYZ[i * 3 + 2] * net.knoopXYZ[j * 3 + 2];
  return R_AARDE * Math.acos(Math.max(-1, Math.min(1, d)));
}

/** Grootcirkel-afstand tussen twee lon/lat-paren, in km. */
export function gcKmLL(lon1, lat1, lon2, lat2) {
  const r = Math.PI / 180;
  const d = Math.sin(lat1 * r) * Math.sin(lat2 * r) +
    Math.cos(lat1 * r) * Math.cos(lat2 * r) * Math.cos((lon2 - lon1) * r);
  return R_AARDE * Math.acos(Math.max(-1, Math.min(1, d)));
}

/** Dichtstbijzijnde netwerk-knoop bij een lon/lat (voor klik-op-de-kaart). */
export function dichtstbijzijndeKnoop(net, lon, lat) {
  const lo = lon * (Math.PI / 180), la = lat * (Math.PI / 180);
  const vx = Math.cos(la) * Math.cos(lo), vy = Math.sin(la), vz = Math.cos(la) * Math.sin(lo);
  let beste = -1, besteDot = -2;
  for (let i = 0; i < net.knoopLon.length; i++) {
    const d = net.knoopXYZ[i * 3] * vx + net.knoopXYZ[i * 3 + 1] * vy + net.knoopXYZ[i * 3 + 2] * vz;
    if (d > besteDot) { besteDot = d; beste = i; }
  }
  return beste;
}

/**
 * Welke binnenvaartsystemen zijn vanaf `knoop` bereikbaar ZONDER over zee te
 * gaan? Dat is precies de verzameling die een schip nodig kán hebben om een
 * binnenhaven te bereiken — al het andere binnenwater is voor die reis een
 * sluipweg.
 */
export function binnenSystemenBij(net, knoop) {
  const binnen = new Set();
  for (const [label, v] of Object.entries(net.vaarwegen || {})) {
    if (!v.zeevaart) binnen.add(label);
  }
  const gezien = new Uint8Array(net.knoopLon.length);
  const gevonden = new Set();
  const stapel = [knoop];
  gezien[knoop] = 1;
  while (stapel.length) {
    const u = stapel.pop();
    for (let a = net.adjStart[u]; a < net.adjStart[u + 1]; a++) {
      const label = net.edgeLabel[net.adjEdge[a]];
      if (label === null || !binnen.has(label)) continue;
      gevonden.add(label);
      const b = net.adjKnoop[a];
      if (!gezien[b]) { gezien[b] = 1; stapel.push(b); }
    }
  }
  return gevonden;
}

/**
 * Routeer zoals een schip echt vaart (LAR-494, op Lars' regel: *"als een route
 * naar een zeehaven gaat, dan gaat de zeeboot ineens via rivieren of sluizen —
 * dat is niet natuurlijk"*).
 *
 * Twee trappen:
 *  1. Probeer het als ZEESCHIP: alle binnenvaartsystemen dicht. Lukt dat, dan
 *     is het een zeereis en is er niets aan de hand — Rotterdam→Shanghai gaat
 *     dan weer om via Gibraltar i.p.v. door de Rijn.
 *  2. Lukt het niet, dan ligt minstens één uiteinde in het binnenland. Sta dan
 *     alleen de systemen toe die vanaf die uiteinden **zonder zee** bereikbaar
 *     zijn. Dat is de sleutel: de Europese en de Chinese binnenwaternetten zijn
 *     losse componenten, dus een reis naar Wuhan mag de Yangtze gebruiken maar
 *     niet de Rijn-Donau-corridor als sluipweg naar de Zwarte Zee.
 *
 * `opties.schip` (LAR-514) reist via de spread mee naar BEIDE trappen — dat
 * hoort ook: een te groot schip moet zowel op de zeeroute als op de
 * binnenvaartroute op dezelfde poorten stuklopen.
 */
export function zoekRouteRealistisch(net, van, naar, opties = {}) {
  const basis = opties.vermijd ?? ["northwest"];
  const zee = zoekRoute(net, van, naar, { ...opties, vermijd: [...basis, "binnenvaart"] });
  if (zee) return { route: zee, modus: "zeeschip" };

  const toegestaan = new Set([
    ...binnenSystemenBij(net, van), ...binnenSystemenBij(net, naar),
  ]);
  const dicht = [];
  for (const [label, v] of Object.entries(net.vaarwegen || {})) {
    if (!v.zeevaart && !toegestaan.has(label)) dicht.push(label);
  }
  const binnen = zoekRoute(net, van, naar, { ...opties, vermijd: [...basis, ...dicht] });
  return binnen ? { route: binnen, modus: "binnenvaart" } : null;
}

/**
 * Vertaalt `opties.schip` naar de vier grenzen in DECIMETER waarop de router
 * filtert. Geeft `null` als er geen schip is opgegeven — en dan gaat er ook
 * geen enkele edge dicht (LAR-514, acceptatiepunt 2).
 *
 * ⚠️ Het draagprincipe zit hier: een edge-maat van 0 betekent ONBEKEND, en
 * onbekend is GEEN grens. Zou 0 als "past niet" gelden, dan sloot elke
 * ongemeten edge stilzwijgend af — en dat is onvindbaar, want je ziet alleen
 * dat een route niet bestaat, niet waaróm.
 */
export function schipGrenzen(schip) {
  if (!schip) return null;
  const dm = (v) => (typeof v === "number" && v > 0 ? Math.round(v * 10) : 0);
  const g = {
    diepgang: dm(schip.diepgang),
    breedte: dm(schip.breedte),
    lengte: dm(schip.lengte),
    hoogte: dm(schip.hoogte),
  };
  return (g.diepgang || g.breedte || g.lengte || g.hoogte) ? g : null;
}

/** Past dit schip door deze edge? Onbekende maat aan één van beide kanten = ja. */
export function edgePast(net, e, g) {
  return !(
    (g.diepgang && net.edgeDiepgang[e] && net.edgeDiepgang[e] < g.diepgang) ||
    (g.breedte && net.edgeBreedte[e] && net.edgeBreedte[e] < g.breedte) ||
    (g.lengte && net.edgeLengte[e] && net.edgeLengte[e] < g.lengte) ||
    (g.hoogte && net.edgeHoogte[e] && net.edgeHoogte[e] < g.hoogte)
  );
}

/**
 * A* van knoop naar knoop. Geeft { edges, knopen, km } of null.
 * De heuristiek (grootcirkel-afstand) is toelaatbaar: geen pad is korter dan
 * de grootcirkel, dus het gevonden pad is exact het kortste over de graaf —
 * ook mét straf, want een straf maakt paden alleen maar duurder.
 *
 * opties.vermijd — passage-labels die dicht zijn. Default ["northwest"]:
 *   exact searoute's eigen default (restrictions=[northwest]) — de
 *   Noordwest-Passage is geometrisch vaak het kortst naar Azië maar geen
 *   commerciële route. Voor M21 (knelpunt-simulator) is dit meteen het
 *   mechanisme: "Suez dicht" = "suez" aan deze lijst toevoegen.
 * opties.arctisFactor — kostfactor voor edges die geheel boven de poolcirkel
 *   liggen (default 1 = uit; zet bv. 2 om de Noordelijke Zeeroute alleen te
 *   laten winnen als er geen redelijk alternatief is).
 */
export function zoekRoute(net, van, naar, opties = {}) {
  const vermijd = opties.vermijd ?? ["northwest"];
  const arctisFactor = opties.arctisFactor ?? 1;
  const dichtLabel = new Set(vermijd);
  // Scheepsmaten (LAR-514). Zelfde soort filter als `vermijd` en op dezelfde
  // plek in de lus: een edge valt weg VÓÓR de relaxatie, er komt geen
  // strafmechanisme bij. Daardoor blijft de grootcirkel-heuristiek toelaatbaar
  // en is het gevonden pad nog steeds exact het kortste over wat overblijft.
  const grenzen = schipGrenzen(opties.schip);
  // Groepslabel "binnenvaart" (LAR-494): sluit in één keer élk vaarwegsysteem
  // dat niet zeevaarbaar is. Nodig sinds de Donau-ring, want dat is de EERSTE
  // binnenvaartverbinding die twee zeeën koppelt — daarvoor was elke rivierketen
  // een doodlopende tak en kon een zeeroute er dus nooit korter door worden.
  if (dichtLabel.has("binnenvaart")) {
    for (const [label, v] of Object.entries(net.vaarwegen || {})) {
      if (!v.zeevaart) dichtLabel.add(label);
    }
  }
  const n = net.knoopLon.length;
  const g = new Float64Array(n).fill(Infinity);
  const vorigeEdge = new Int32Array(n).fill(-1);
  const vorigeKnoop = new Int32Array(n).fill(-1);
  const dicht = new Uint8Array(n);

  // binaire heap van [f, knoop] — ruim bemeten: een knoop kan vaker gepusht
  // worden voordat hij dichtgaat (decrease-key via her-push)
  const heapF = new Float64Array(n * 8);
  const heapK = new Int32Array(n * 8);
  let heapN = 0;
  function push(f, k) {
    // ⚠️ Bounds-assert: een typed array negeert een schrijf buiten zijn bereik
    // STIL, dus zonder deze check is overloop geen crash maar een verkeerde
    // route zonder foutmelding (bevinding uit het overslag-panel).
    if (heapN >= heapK.length) throw new Error("router: heap vol");
    let i = heapN++;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (heapF[p] <= f) break;
      heapF[i] = heapF[p]; heapK[i] = heapK[p];
      i = p;
    }
    heapF[i] = f; heapK[i] = k;
  }
  function pop() {
    const topK = heapK[0];
    const f = heapF[--heapN], k = heapK[heapN];
    let i = 0;
    while (true) {
      const l = i * 2 + 1, r = l + 1;
      let kleinste = i;
      if (l < heapN && heapF[l] < (kleinste === i ? f : heapF[kleinste])) kleinste = l;
      if (r < heapN && heapF[r] < (kleinste === i ? f : heapF[kleinste])) kleinste = r;
      if (kleinste === i) break;
      heapF[i] = heapF[kleinste]; heapK[i] = heapK[kleinste];
      i = kleinste;
    }
    heapF[i] = f; heapK[i] = k;
    return topK;
  }

  g[van] = 0;
  push(gcKm(net, van, naar), van);
  while (heapN > 0) {
    const cur = pop();
    if (dicht[cur]) continue;
    dicht[cur] = 1;
    if (cur === naar) break;
    for (let a = net.adjStart[cur]; a < net.adjStart[cur + 1]; a++) {
      const buur = net.adjKnoop[a];
      if (dicht[buur]) continue;
      const e = net.adjEdge[a];
      if (net.edgeLabel[e] !== null && dichtLabel.has(net.edgeLabel[e])) continue;
      if (grenzen && !edgePast(net, e, grenzen)) continue;
      let kost = net.edgeKm[e];
      if (arctisFactor !== 1 &&
          net.knoopLat[net.edgeA[e]] > 66.5 && net.knoopLat[net.edgeB[e]] > 66.5) {
        kost *= arctisFactor;
      }
      const ng = g[cur] + kost;
      if (ng < g[buur]) {
        g[buur] = ng;
        vorigeEdge[buur] = e;
        vorigeKnoop[buur] = cur;
        push(ng + gcKm(net, buur, naar), buur);
      }
    }
  }
  if (!dicht[naar]) return null;

  const edges = [], knopen = [naar];
  let k = naar;
  while (k !== van) {
    edges.push(vorigeEdge[k]);
    k = vorigeKnoop[k];
    knopen.push(k);
  }
  edges.reverse();
  knopen.reverse();
  // km = de échte afstand (g bevat bij een straf ook de strafkilometers)
  let km = 0;
  for (const e of edges) km += net.edgeKm[e];
  return { edges, knopen, km };
}
