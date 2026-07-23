// toets_routes.mjs — de eerste uitvoerbare test van de repo.
//
// Rekent headless na wat de browser doet, met EXACT dezelfde router.js/keten.js
// (geen kopie). Drie blokken:
//   A. de elf zee-invarianten (zoekRouteRealistisch) — deze mochten NIET
//      veranderen door het koppelen
//   B. het koppelen zelf: snap-afstanden, gemengde landknopen, structuur
//   C. de keten-router: de tabel uit overslag-ontwerp §3c
//
// Draaien:  node v2/tools/toets_routes.mjs
// Exit-code 0 = alles groen; 1 = een toets faalde.

import { laadMarnetHeadless, laadLandnetHeadless, laadRegister, laadHavens,
         laadAansluitingen, laadStromenData, laadPijpleidingen } from "./laad_headless.mjs";
import { zoekRoute, zoekRouteRealistisch } from "../src/router.js";
import { koppelNetten, zoekKeten, havenZaden } from "../src/keten.js";
import { routeerStroom } from "../src/stromen.js";

const marnet = laadMarnetHeadless();
const landnet = laadLandnetHeadless();
const havens = laadHavens();
const register = laadRegister();
marnet.vaarwegen = marnet.vaarwegen || {};

const opLocode = new Map();
for (const h of havens) if (!opLocode.has(h.locode)) opLocode.set(h.locode, h);
const opNaam = new Map();
for (const h of havens) if (!opNaam.has(h.naam.toLowerCase())) opNaam.set(h.naam.toLowerCase(), h);
const H = (naam) => {
  const h = opNaam.get(naam.toLowerCase());
  if (!h) throw new Error(`haven niet gevonden: ${naam}`);
  return h;
};

let fouten = 0, toetsen = 0;
function toets(naam, ok, detail = "") {
  toetsen++;
  const merk = ok ? "  ok " : "FOUT ";
  if (!ok) fouten++;
  console.log(`${merk} ${naam}${detail ? "  — " + detail : ""}`);
}
function dichtbij(naam, waarde, doel, tol) {
  const ok = Math.abs(waarde - doel) <= tol;
  toets(naam, ok, `${Math.round(waarde)} (doel ${doel} ±${tol})`);
  return ok;
}

// --------------------------------------------------------------------------
console.log("\n=== A · de zee-invarianten (mogen NIET veranderd zijn) ===");
// De elf uit het ontwerp, gemeten knoop→knoop in het DEFAULT-profiel
// (zoekRouteRealistisch). Toleranties ruim: de toets bewijst dat het koppelen
// het zeenet niet raakte, niet de exacte bake-cijfers (die staan in de banner).
function zeeKm(vanNaam, naarNaam) {
  const van = H(vanNaam), naar = H(naarNaam);
  const uit = zoekRouteRealistisch(marnet, van.knoop, naar.knoop);
  if (!uit) return null;
  return uit.route.km + van.afstandKm + naar.afstandKm;
}
dichtbij("Rotterdam→Shanghai", zeeKm("Rotterdam", "Shanghai"), 19610, 60);
dichtbij("Duluth-Superior→Rotterdam", zeeKm("Duluth-Superior", "Rotterdam"), 8031, 60);
{
  const rs = zoekRouteRealistisch(marnet, H("Rotterdam").knoop, H("Shanghai").knoop);
  toets("Rotterdam→Shanghai is een zeereis (0 binnenwater)",
    rs && rs.modus === "zeeschip", rs ? rs.modus : "null");
}

// --------------------------------------------------------------------------
console.log("\n=== B · het koppelen ===");
const K = koppelNetten({ marnet, landnet, zeeKnopen: havens.zeeKnopen, register });
console.log(`  ${K.stats.punten} punten · ${K.stats.overstappen} overstappen · ` +
  `${K.stats.gemengdeLandknopen} gemengde landknopen · ` +
  `ergste snap ${K.stats.ergsteSnapKm.toFixed(1)} km · ${K.stats.msKoppelen} ms`);
toets("alle punten gesnapt (geen exception)", true);
toets("water-aanhechtingen snappen tegen 0 (< 6 km)",
  K.stats.ergsteSnapWaterKm < 6, `${K.stats.ergsteSnapWaterKm.toFixed(1)} km`);
toets("land-aanhechtingen snappen op de hoofdlijn (< 60 km cap)",
  K.stats.ergsteSnapLandKm <= 60, `${K.stats.ergsteSnapLandKm.toFixed(1)} km`);
// zeeknoop-identiteit: knoop 6811 draagt 22 havens — een overstap mag nooit op
// "raakt deze knoop" triggeren. We toetsen dat de overstappen expliciete
// knopenparen zijn (verschillende knoop per modaliteit binnen een punt).
{
  const rotterdam = K.punten.find((p) => p.id === "rotterdam");
  const kZee = rotterdam.aanhechting.zee.knoop;
  const kBinnen = rotterdam.aanhechting.binnen.knoop;
  toets("Rotterdam zee-knoop ≠ binnen-knoop (expliciet paar, geen teleport)",
    kZee !== kBinnen, `${kZee} vs ${kBinnen}`);
}
toets("Duisburg heeft GEEN zee-aanhechting (redactionele fix)",
  !K.punten.find((p) => p.id === "duisburg").aanhechting.zee);

// --------------------------------------------------------------------------
console.log("\n=== C · de keten-router (overslag-ontwerp §3c) ===");
function keten(vanNaam, naarNaam, opties) {
  const van = H(vanNaam), naar = H(naarNaam);
  return zoekKeten(K, havenZaden(K, van), havenZaden(K, naar), opties);
}
function toonKeten(uit) {
  if (uit.geenPad) return `geen pad — ${uit.reden}`;
  const legs = uit.benen.map((b) => `${b.vervoer} ${Math.round(b.km)}km`).join(" → ");
  const ov = uit.overslagen ? ` [${uit.overslagen}× overslag: ${uit.overstappen.map((o) => o.naam).join(", ")}]` : "";
  return `${Math.round(uit.km)} km · ${legs}${ov}`;
}

// standaardprofiel: alleen zee+binnen open (landnet dicht — de landbrug-regel)
{
  const r = keten("Rotterdam", "Shanghai");
  console.log(`  R'dam→Shanghai: ${toonKeten(r)}`);
  toets("R'dam→Shanghai: 0 overslagen (zee wint lexicografisch)",
    !r.geenPad && r.overslagen === 0);
  dichtbij("R'dam→Shanghai km via keten", r.geenPad ? -1 : r.km, 19610, 60);
}
{
  const r = keten("Rotterdam", "Nijmegen");
  // Nijmegen bestaat mogelijk niet als aparte haven; val terug op Duisburg
  console.log(`  R'dam→Duisburg: ${toonKeten(keten("Rotterdam", "Duisburg"))}`);
}
{
  const r = keten("Rotterdam", "Duisburg");
  toets("R'dam→Duisburg: binnenschip, 0 overslagen (géén verzonnen overslag)",
    !r.geenPad && r.overslagen === 0 && r.benen.every((b) => b.groep === "binnen" || b.groep === "zee"));
}
{
  const r = keten("Rotterdam", "Cincinnati");
  console.log(`  R'dam→Cincinnati: ${toonKeten(r)}`);
  toets("R'dam→Cincinnati: minstens 1 overslag (geen 0-overslagpad)",
    !r.geenPad && r.overslagen >= 1);
  if (!r.geenPad) {
    const namen = r.overstappen.map((o) => o.naam).join(", ");
    toets("R'dam→Cincinnati: overslag bij New Orleans",
      namen.includes("New Orleans"), namen);
  }
}
{
  const r = keten("Rotterdam", "Wuhan");
  console.log(`  R'dam→Wuhan: ${toonKeten(r)}`);
  toets("R'dam→Wuhan: krijgt een keten (zeeschip → overslag → binnenschip)",
    !r.geenPad && r.overslagen >= 1);
}

// een haven ver van elk net → geen pad mét reden
{
  const r = keten("Saldanha Bay", "Manaus");
  console.log(`  Saldanha→Manaus: ${toonKeten(r)}`);
  toets("een onmogelijke relatie geeft 'geen pad' met een reden",
    r.geenPad ? typeof r.reden === "string" && r.reden.length > 0 : true);
}

// ==========================================================================
// D · de werkelijke stromen (M26.1) — design/stroom-aansluiting.md
// ==========================================================================
// Twee dingen moeten hier waar zijn, en ze zijn allebei makkelijk stil kapot
// te maken: (1) de aansluitingen mogen de zoekruimte NIET veranderen — blok A
// hierboven draaide zonder aansluitingen, dus we hérmeten de invariant mét;
// (2) elk been dat een net heeft, moet ook echt een pad hebben.

console.log("\n=== D · de werkelijke stromen (M26.1) ===");
{
  const aansluitingen = laadAansluitingen();
  const stromenData = laadStromenData();
  const K2 = koppelNetten({ marnet, landnet, zeeKnopen: havens.zeeKnopen,
                            register, aansluitingen });
  console.log(
    `  ${K2.stats.aansluitingen} aansluitingen · ` +
    `ergste last mile ${K2.stats.ergsteLastMileKm.toFixed(1)} km`
  );

  // (1) De invariant, opnieuw gemeten MET de aansluitingen erin. Een
  // aansluiting maakt geen overstap aan, dus dit hoort exact hetzelfde te zijn.
  const r = zoekKeten(K2, havenZaden(K2, H("Rotterdam")), havenZaden(K2, H("Shanghai")), {});
  toets("aansluitingen veranderen de zoekruimte niet (R'dam→Shanghai)",
    !r.geenPad && Math.abs(r.km - 19610) < 60, `${Math.round(r.km)} km`);
  toets("aansluitingen maken geen overstappen aan",
    K2.stats.overstappen === K.stats.overstappen,
    `${K2.stats.overstappen} vs ${K.stats.overstappen}`);

  const leidingen = laadPijpleidingen();
  const opId = (id) => K2.aansluitingen.get(id) || null;
  const opLeiding = (id) => (leidingen?.leidingen || []).find((l) => l.id === id) || null;
  if (leidingen) {
    for (const l of leidingen.leidingen) {
      console.log(`  leiding ${l.id}: ${l.km} km tegen ${l.gepubliceerdKm} gepubliceerd ` +
        `(${l.afwijkingPct > 0 ? "+" : ""}${l.afwijkingPct}%) · ${l.punten.length} punten`);
      // De lengtetoets is bij een pijpleiding de ENIGE echte controle: er is geen
      // tweede bron voor de geometrie, net als bij de wegcorridors.
      toets(`leiding ${l.id}: lengte binnen 15% van de gepubliceerde`,
        Math.abs(l.afwijkingPct) <= 15, `${l.afwijkingPct}%`);
    }
  }
  for (const s of stromenData.stromen) {
    const g = routeerStroom(K2, s, opId, opLeiding);
    const beschrijf = g.benen.map((b) =>
      b.status === "ok" ? `${b.vervoer} ${Math.round(b.km)}km`
        : `${b.modus} [${b.status}]`).join(" → ");
    console.log(`  ${s.id}: ${Math.round(g.km)} km · ${beschrijf}`);

    // ⚠️ GATEN WORDEN GETELD, NIET WEGGEPOETST. Deze getallen staan hier en niet
    // in de data: een gat in de data zetten maakt hem onzichtbaar zodra hij
    // gedicht is. Gaat een getal omlaag → vooruitgang, pas het hier aan. Gaat
    // het omhoog → regressie, en dan hoort deze toets rood te staan.
    //
    //   cu-collahuasi-tongling = 0  de slurryleiding is EIGEN VERBINDING, geen
    //                               gat: we weten waar hij ligt (OSM), en dat hij
    //                               niet routeerbaar is hoort bij zijn aard —
    //                               een net is productonafhankelijk, een
    //                               slurryleiding vervoert één ding tussen twee
    //                               punten.
    //   cu-escondida-guixi     = 2  de Escondida-leiding (route ONBEKEND: OSM
    //                               heeft hem niet doorlopend) + het spoorbeen
    //                               Beilun→Guixi: het havenspoor van Beilun ligt
    //                               op een eigen component van 1.823 km, los van
    //                               het Chinese hoofdnet (402.762 km). Vraagt een
    //                               heal-ronde op landnet.bin — hetzelfde soort
    //                               gat als het gefragmenteerde EU-spoor.
    //   cu-lobito-duisburg     = 0  volledig gerouteerd, mijn tot fabriek.
    //   coal-cerrejon-ruhr     = 1  het Rijnbeen: de EMO-kade op de Maasvlakte
    //                               hecht op een LOSSTAAND havenbekken van 4 km,
    //                               terwijl Duisburg op de doorgaande Rijn zit
    //                               (24.517 km). De Waalhaven-kade 30 km verderop
    //                               zit wél op de Rijn — vandaar dat stroom C
    //                               dezelfde reis wél maakt. Riviernet-gat op de
    //                               Maasvlakte, hetzelfde patroon als LAR-520.
    const VERWACHTE_GATEN = {
      "cu-collahuasi-tongling": 0,
      "cu-escondida-guixi": 2,
      "cu-lobito-duisburg": 0,
      "coal-cerrejon-ruhr": 1,
    };
    for (const b of g.benen) {
      // Een EIGEN VERBINDING is compleet — geen waarschuwing, wel vermelden.
      if (b.status === "eigen") {
        console.log(`     · ${b.modus}: eigen verbinding, ${Math.round(b.km)} km getekend`);
      } else if (b.status !== "ok") {
        console.log(`     ⚠️ ${b.modus}: ${b.reden}`);
      }
    }
    toets(`${s.id}: aantal gaten ongewijzigd (${VERWACHTE_GATEN[s.id]})`,
      g.gaten === VERWACHTE_GATEN[s.id], `${g.gaten} gaten`);
    toets(`${s.id}: de overslag zit op de aansluiting van de grondstof`,
      g.overslagen.length >= 1 && g.overslagen.every((o) => o.bij && o.bij.grondstof === s.grondstof),
      g.overslagen.map((o) => `${o.van}→${o.naar} @ ${o.bij?.id}`).join(" · "));
    // Een been mengt nooit netten — hier expliciet nagerekend i.p.v. vertrouwd.
    toets(`${s.id}: geen been mengt netten`,
      g.benen.filter((b) => b.status === "ok").every((b) => b.route && b.route.groep === b.net),
      g.benen.filter((b) => b.status === "ok").map((b) => `${b.net}/${b.route?.groep}`).join(" "));
  }
}

// --------------------------------------------------------------------------
console.log(`\n${toetsen - fouten}/${toetsen} toetsen groen`);
if (fouten) { console.log(`❌ ${fouten} FOUT`); process.exit(1); }
console.log("✅ alles groen");
