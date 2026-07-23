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

import { zoekKeten, aansluitingZaden, GROEP_VERVOER } from "./keten.js?v=059";

// --------------------------------------------------------------------------
// laden
// --------------------------------------------------------------------------

export async function laadStromen(versie = "059") {
  const [aansluitingen, stromen] = await Promise.all([
    haal(`data/aansluitingen.json?v=${versie}`),
    haal(`data/stromen-pilot.json?v=${versie}`),
  ]);
  return { aansluitingen, stromen };
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
export function routeerStroom(K, stroom, aansluitingOp) {
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
      const km = gcKmLL(van.lon, van.lat, naar.lon, naar.lat);
      benen.push({ ...b, status: "geenNet", van, naar, km,
                   reden: b.reden || "deze modaliteit is nog geen net in de atlas" });
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
    benen.push({
      ...b, status: "ok", van, naar,
      km: uit.km, route: been,
      vervoer: b.modus || GROEP_VERVOER[b.net] || b.net,
      // De last mile is het stuk kade → netknoop, aan beide kanten. Apart
      // bijgehouden omdat het precies het getal is dat zegt waar het net ophoudt.
      lastMileKm: (van.aanhechting[b.net]?.km ?? 0) + (naar.aanhechting[b.net]?.km ?? 0),
    });
    totaalKm += uit.km;
  }

  return { stroom, benen, km: totaalKm, gaten,
           overslagen: telOverslagen(benen) };
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
  const opLand = been.net === "spoor" || been.net === "weg";
  if (!opLand || !K.landComp || !K.landComp.length) return null;
  const kA = van.aanhechting[been.net]?.knoop;
  const kB = naar.aanhechting[been.net]?.knoop;
  if (!(kA >= K.nMar) || !(kB >= K.nMar)) return null;
  const cA = K.landComp[kA - K.nMar], cB = K.landComp[kB - K.nMar];
  if (cA === cB) return null;                    // andere oorzaak — niet raden
  const km = (k) => Math.round(K.landCompKm[k - K.nMar]).toLocaleString("nl");
  return `de twee aansluitingen liggen op verschillende ${been.net}-componenten ` +
         `(${km(kA)} km bij "${van.naam.split(" — ")[0]}" vs ${km(kB)} km bij ` +
         `"${naar.naam.split(" — ")[0]}") — een gat in de bake, geen routeerfout`;
}

/** Een overslag = twee opeenvolgende benen op verschillende netten. */
function telOverslagen(benen) {
  const punten = [];
  for (let i = 1; i < benen.length; i++) {
    const a = benen[i - 1], b = benen[i];
    if (!a.net || !b.net || a.net === b.net) continue;
    punten.push({ bij: b.van, van: a.net, naar: b.net });
  }
  return punten;
}

function gcKmLL(lon1, lat1, lon2, lat2) {
  const r = Math.PI / 180;
  const d = Math.sin(lat1 * r) * Math.sin(lat2 * r) +
    Math.cos(lat1 * r) * Math.cos(lat2 * r) * Math.cos((lon2 - lon1) * r);
  return 6371 * Math.acos(Math.max(-1, Math.min(1, d)));
}

