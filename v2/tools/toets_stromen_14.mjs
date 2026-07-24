// toets_stromen_14.mjs — de sibling-gatendetector (havenniveau).
//
// Lars' werkregel: "we moeten het vooral meemaken waar iets ontbreekt." Dit
// routeert per grondstof ÉÉN echte stroom van een zee-export-haven naar een
// binnenwater-/spoorbestemming, met overslag, en meldt waar het net breekt.
// Bewust op HAVENNIVEAU (bestaande ports.json-havens, geen nieuwe kades): voor
// "zijn er nog meer random gaten?" is straatniveau-precisie niet nodig — je
// wilt alleen weten of de keten doorloopt en waar hij anders breekt.
//
// Een gat = zoekKeten geeft "geen pad", OF de bestemming hangt op een absurde
// rivier-last-mile (sliver/ongekaarteerde geul — de Manaus/Tongling-signatuur).
// Grondstoffen die puur VLIEGEN (goud/diamant/PGM) hebben geen graaf-been en
// kunnen per constructie geen net-gat hebben; die staan als zodanig gemarkeerd.
//
// Draaien:  node v2/tools/toets_stromen_14.mjs

import { existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { laadMarnetHeadless, laadLandnetHeadless, laadHavens,
         laadRegister } from "./laad_headless.mjs";
import { koppelNetten, zoekKeten, havenZaden } from "../src/keten.js";

// ⚠️ GEPARKEERD (2026-07-24, AIS-ombouw): zie de guard-noot in toets_routes.mjs.
if (!existsSync(join(dirname(fileURLToPath(import.meta.url)), "..", "data", "marnet.bin"))) {
  console.log("geparkeerd: geen marnet.bin — waternet verwijderd voor de AIS-ombouw " +
    "(oude stand: git-tag pre-ais-net). Deze toets komt terug op het AIS-net.");
  process.exit(0);
}

const marnet = laadMarnetHeadless();
const landnet = laadLandnetHeadless();
const havens = laadHavens();
const register = laadRegister();
marnet.vaarwegen = marnet.vaarwegen || {};

const opNaam = new Map();
for (const h of havens) if (!opNaam.has(h.naam.toLowerCase())) opNaam.set(h.naam.toLowerCase(), h);
const hv = (naam) => opNaam.get(naam.toLowerCase()) || null;

const K = koppelNetten({ marnet, landnet, zeeKnopen: havens.zeeKnopen, register });

// De 14 teststromen. Per grondstof een echte stroom naar binnenwater/spoor
// (waar de gaten leven). `via` is niet nodig — havenZaden zaait op het net, de
// keten-router zoekt zelf de overslag. `netten` opent spoor waar de bestemming
// per trein bereikt wordt.
const RIVIER = ["zee", "binnen"];
const SPOOR = ["zee", "binnen", "spoor"];
const STROMEN = [
  { g: "copper",      van: "Antofagasta", naar: "Chongqing",   netten: RIVIER, riv: "boven-Yangtze" },
  { g: "coal",        van: "Rotterdam",   naar: "Duisburg",    netten: RIVIER, riv: "Rijn" },
  { g: "cobalt",      van: "Durban",      naar: "Jiujiang",    netten: RIVIER, riv: "Yangtze" },
  { g: "rare-earths", van: "Shanghai",    naar: "Ganzhou",     netten: SPOOR,  riv: "spoor Z-China" },
  { g: "graphite",    van: "Nacala",      naar: "New Orleans", netten: RIVIER, riv: "Mississippi-mond" },
  { g: "lithium",     van: "Antofagasta", naar: "Nanchang",    netten: RIVIER, riv: "Gan-rivier" },
  { g: "nickel",      van: "Rotterdam",   naar: "Duluth-Superior", netten: RIVIER, riv: "Seaway" },
  { g: "oil",         van: "Novorossiysk", naar: "Wuhan",      netten: RIVIER, riv: "Yangtze" },
  { g: "silver",      van: "Callao",      naar: "Memphis",     netten: RIVIER, riv: "Ohio/Mississippi" },
  { g: "uranium",     van: "Vancouver",   naar: "Chongqing",   netten: RIVIER, riv: "boven-Yangtze" },
  { g: "gas",         van: "Rotterdam",   naar: "Budapest",    netten: RIVIER, riv: "Donau" },
  // Luchtvracht — geen graaf-been, geen net-gat mogelijk (great-circle-boog).
  { g: "gold",        lucht: true },
  { g: "diamond",     lucht: true },
  { g: "pgm",         lucht: true },
];

console.log("\n=== sibling-gatendetector · 14 teststromen op havenniveau ===\n");
let gaten = 0, geen = 0, gemist = 0, lucht = 0;

for (const s of STROMEN) {
  if (s.lucht) {
    console.log(`  ✈  ${s.g.padEnd(12)} vliegt — geen net-been, geen gat mogelijk`);
    lucht++;
    continue;
  }
  const van = hv(s.van), naar = hv(s.naar);
  if (!van || !naar) {
    console.log(`  ??  ${s.g.padEnd(12)} haven niet in ports.json: ${!van ? s.van : s.naar}`);
    gemist++;
    continue;
  }
  const r = zoekKeten(K, havenZaden(K, van), havenZaden(K, naar),
    { netten: s.netten, maxOverstap: 3 });
  const lastMile = naar.afstandRivierKm >= 0 ? naar.afstandRivierKm : naar.afstandKm;
  const merk = r.geenPad ? "❌" : (lastMile > 15 ? "⚠️ " : "  ok");
  if (r.geenPad) { gaten++; geen++; }
  else if (lastMile > 15) gaten++;

  const route = r.geenPad ? `GEEN PAD — ${r.reden}`
    : `${Math.round(r.km)} km · ${r.overslagen}× overslag` +
      (r.overstappen?.length ? ` (${r.overstappen.map((o) => o.naam).join(", ")})` : "");
  console.log(`  ${merk} ${s.g.padEnd(12)} ${s.van} → ${s.naar} [${s.riv}]`);
  console.log(`        last-mile ${lastMile.toFixed(1)} km · ${route}`);
}

console.log(`\n${STROMEN.length} stromen · ${lucht} luchtvracht · ${gemist} haven-gemist · ` +
  `${gaten} met gat (${geen}× geen pad)`);
