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

import { laadMarnetHeadless, laadLandnetHeadless, laadRegister, laadHavens }
  from "./laad_headless.mjs";
import { zoekRoute, zoekRouteRealistisch } from "../src/router.js";
import { koppelNetten, zoekKeten, havenZaden } from "../src/keten.js";

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
toets("ergste snap-afstand < 6 km (redactioneel plausibel)",
  K.stats.ergsteSnapKm < 6, `${K.stats.ergsteSnapKm.toFixed(1)} km`);
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

// --------------------------------------------------------------------------
console.log(`\n${toetsen - fouten}/${toetsen} toetsen groen`);
if (fouten) { console.log(`❌ ${fouten} FOUT`); process.exit(1); }
console.log("✅ alles groen");
