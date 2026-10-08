// stroomstijl.js — ÉÉN bron van waarheid voor hoe een stroom eruitziet:
// welke kleur hij krijgt en welke vorm zijn lijn heeft.
//
// WAAROM DIT BESTAAT. `stroomroute.js` (de exacte lijn) en `stroomleven.js`
// (draad + kometen) hadden allebei hun eigen kopie van de kleurtabel, met in de
// tweede letterlijk de opmerking "zelfde kleuren als stroomroute.js". Twee
// kopieën van een legenda lopen vroeg of laat uit elkaar, en dit project heeft
// die klasse al twee keer betaald ("de legenda loog" bij ACES-tone-mapping, en
// de generator↔uitvoer-drift bij `cu-guixi-spoor`). Nu leest één tabel.
//
// ── DE TWEE ASSEN ──────────────────────────────────────────────────────────
//
// ✅ BESLUIT LARS (2026-08-07): de atlas kleurt op GRONDSTOF, het routewerk op
// MODALITEIT. Dat zijn twee verschillende vragen aan hetzelfde beeld:
//
//   · kleur = MODALITEIT → "waar houdt de zee op en begint de barge?" Dat is de
//     vraag tijdens het bouwen en controleren van een route, en die weergave is
//     bewezen (v=111, vijf stromen). Blijft ongewijzigd de default.
//   · kleur = GRONDSTOF → "waar gaat het koper heen?" Dat is de vraag die de
//     ATLAS beantwoordt: drie koperstromen horen dan één kleur te zijn, ook al
//     lopen ze over vier verschillende netten.
//
// Dit is precies wat de ontwerpbrief al voorschreef (`design/lod-ontwerpbrief.md`,
// tabel "de visuele taal": *kleur = grondstof · lijnstijl = modaliteit*). De
// modaliteitskleur was dus nooit de eindvorm, hij was het gereedschap waarmee de
// routes zijn gelegd.
//
// ⚠️ WAT DE MODALITEIT DRAAGT ZODRA KLEUR NAAR DE GRONDSTOF GAAT: de stippel-
// conventie blijft (werkwijze §7 — gestippeld = hier reikt het net niet) en de
// overslagmarkers blijven staan, dus je ziet nog steeds wáár de drager wisselt.
// Wat je niet meer ziet is welke drager het is. De brief wil dat op termijn in
// de lijnSTIJL leggen (streeppatroon/dikte per modaliteit); dat is bewust nog
// niet gebouwd — eerst kijken of de grondstofkleur op de bol doet wat hij moet.
//
// ── DE LIJNVORM ────────────────────────────────────────────────────────────
//
// Vier standen, want Lars wilde de drie hemelsbreed-varianten naast elkaar zien
// in plaats van er één vooraf te kiezen:
//
//   route          de gemeten geometrie — elke meter is ergens op verantwoord
//   recht-plat     grootcirkel kop→staart, strak op dezelfde schil
//   recht-boog     grootcirkel kop→staart, opgetild (hoogte ∝ afstand, v1-look)
//   recht-zeeboog  grootcirkel, opgetild op zee, plat op land en rivier
//
// ⚠️ DIT ONDERGRAAFT HET BESLUIT VAN 2026-08-07 NIET ("de lijnen blijven op de
// grond"). Dat besluit gaat over de ECHTE routes: die mogen niet de lucht in,
// want M23–M28 ging er juist over ze op de gemeten geul/het gemeten spoor te
// krijgen. Een hemelsbreed-lijn dóét die claim per definitie niet — hij zegt
// alleen "van hier naar daar". Het optillen is daar zelfs eerlijker: het maakt
// zichtbaar dat je naar een schematische verbinding kijkt en niet naar een
// zeeschip dat over de Andes vaart.

// ── Grondstofkleuren ───────────────────────────────────────────────────────
//
// ✅ KEUZE LARS (2026-08-07): fellere atlas-varianten van de v1-families, niet
// de v1-waarden zelf. Reden is meetbaar en niet esthetisch: v1 kleurt MARKERS op
// een lichte kaart, hier zijn het lichtgevende lijnen op satelliet in het donker.
// Grafietgrijs (#78828F) is als glowlijn vrijwel onzichtbaar, en lithium-teal
// (#4FD1C5) valt samen met het binnenvaart-turkoois dat er in modaliteitsmodus
// naast ligt. De families blijven herkenbaar: koper warm, lithium violet.
//
// ⚠️ `gloednodes.js` leest deze tabel óók — gloed en lijn van dezelfde grondstof
// horen per definitie dezelfde kleur te hebben. Verander hier, en de gloed gaat
// mee. Dat is de bedoeling.
//
// In gebruik vandaag: koper · lithium · grafiet. De rest staat er vooruit, in
// dezelfde families als `data/<grondstof>.js` in de v1-atlas.
export const GRONDSTOF_KLEUR = {
  koper: 0xff8a30,        // v1 #C87D4A brons → feloranje
  lithium: 0xc06bff,      // v1 #4FD1C5 teal → violet (de brief zegt "lithium paars")
  grafiet: 0x7fd8ff,      // v1 #78828F grijs → ijsblauw; grijs gloeit niet
  kobalt: 0x3d6dff,
  nikkel: 0x2fd08a,
  goud: 0xffd24a,
  zilver: 0xe6f2ff,
  uranium: 0x8bff5a,
  "rare-earths": 0xe8ff3d,
  // `ree` = dezelfde kleur als "rare-earths": de stroom-id's heten
  // `ree-<van>-<naar>` en grondstofVan() splitst op het EERSTE streepje, dus
  // "rare-earths" zou als id-prefix nooit matchen. De prefix is de sleutel die
  // lijn, komeet en gloed opzoeken; de regel hierboven blijft voor de v1-naam.
  ree: 0xe8ff3d,
  pgm: 0xc0e0ff,
  olie: 0xff4d4d,
  gas: 0x5ce1e6,
  diamant: 0xa8f0ff,
  kolen: 0xd94f2b,
};

// ── Modaliteitskleuren ─────────────────────────────────────────────────────
// Ongewijzigd overgenomen uit stroomroute.js — dit is de bewezen legenda van de
// routebouw-weergave en er is geen reden hem aan te raken.
export const MODALITEIT_KLEUR = {
  zee: 0x5aa7ff,          // MARNET-zeebeen + gestippelde haven-aanloop
  binnenvaart: 0x35e0c0,  // AIS-tracks (barge) of riviergeometrie uit de bulklaag
  truck: 0xffb04d,        // weg-been + last mile
  spoor: 0xff7ab8,        // landnet — eigen kleur sinds 2026-07-28
  leiding: 0x9b8cff,      // slurryleiding: een eigen verbinding, geen net
  // Sinds 2026-09-28 (M31 golf 3): goud, PGM en diamant vliegen. Limoengeel is
  // de enige vrije familie naast blauw/turkoois/amber/roze/paars.
  lucht: 0xd6ff5a,
};

const ONBEKEND = 0xffffff;
const gemeld = new Set();

// ── Lijnstijl per modaliteit (golf 1 van de visuele fase, 2026-10-08) ──────
//
// De ontwerpbrief zegt *kleur = grondstof · lijnstijl = modaliteit*. Zodra de
// kleur naar de grondstof gaat moet de modaliteit dus in de VORM, en wel in
// SCHERMpixels (wat op elke hoogte zichtbaar moet zijn schaalt in schermruimte).
// Eén tabel voedt de shader van stroomlijn.js én de legenda in de HUD, zodat
// legenda en beeld niet uit elkaar kunnen lopen ("de legenda loog"-klasse).
//
// Vorm van een patroon: binnen een periode van `periode` px zijn de eerste
// `aan` px op alfa `alfaAan`, de rest op `alfaUit`. Patronen moduleren ALLEEN
// alfa, nooit de tint (×1,35 maakt zilver/pgm/diamant wit, en wit is
// "onbekend"), en de breedte nooit langs de lengte (de ronde eindkappen van
// LineMaterial zouden op elke vertex een knobbel zetten). Een dwarsprofiel
// (`kernFractie` < 1) dempt de randen van de lijn tot `randAlfa` ("berm").
//
// ⚠️ ALLEEN STIPPEL HEEFT ECHTE GATEN (alfaUit 0). Elk modaliteitspatroon houdt
// alfa ≥ 0,45, zodat gestippeld op geen enkele hoogte iets anders kan betekenen
// dan "hier reikt het net niet" (werkwijze §7). Stijl 6 (onbekend) is de luide
// klasse: magenta en gestreept, zodat een vergeten modaliteit nooit stil
// meeloopt. Index 0–5 = MODALITEITEN, 6 = onbekend, 7 = stippel.
//
// ⚠️ De stippel van vóór golf 1 (LineDashedMaterial, dash 0,00008 scene-
// eenheden ≈ 0,21 km) was op wereldhoogte aantoonbaar een vlakke lijn: op
// 9.000 km is 1 css-px ≈ 8 km. Met 3 px aan / 5 px uit is hij op élke hoogte
// gestippeld.
export const MODALITEITEN = ["zee", "binnenvaart", "truck", "spoor", "leiding", "lucht"];
export const STIJL_ONBEKEND = 6;
export const STIJL_STIPPEL = 7;
export const LIJNSTIJL = [
  { naam: "zee",         breedte: 1.8, periode: 0,  aan: 0, alfaAan: 1.0,  alfaUit: 1.0,  kernFractie: 1.0, randAlfa: 1.0 },
  { naam: "binnenvaart", breedte: 1.3, periode: 0,  aan: 0, alfaAan: 1.0,  alfaUit: 1.0,  kernFractie: 1.0, randAlfa: 1.0 },
  { naam: "truck",       breedte: 2.0, periode: 0,  aan: 0, alfaAan: 1.0,  alfaUit: 1.0,  kernFractie: 0.6, randAlfa: 0.45 },
  { naam: "spoor",       breedte: 1.6, periode: 8,  aan: 6, alfaAan: 1.0,  alfaUit: 0.45, kernFractie: 1.0, randAlfa: 1.0 },
  { naam: "leiding",     breedte: 1.6, periode: 12, aan: 9, alfaAan: 0.6,  alfaUit: 1.0,  kernFractie: 1.0, randAlfa: 1.0 },
  { naam: "lucht",       breedte: 1.0, periode: 0,  aan: 0, alfaAan: 1.0,  alfaUit: 1.0,  kernFractie: 1.0, randAlfa: 1.0 },
  { naam: "onbekend",    breedte: 1.6, periode: 6,  aan: 3, alfaAan: 1.0,  alfaUit: 0.0,  kernFractie: 1.0, randAlfa: 1.0 },
  { naam: "stippel",     breedte: 1.1, periode: 8,  aan: 3, alfaAan: 0.85, alfaUit: 0.0,  kernFractie: 1.0, randAlfa: 1.0 },
];

/** Stijlindex van een been: 7 voor stippel, anders de modaliteit; onbekend = 6
 *  mét de luide waarschuwing (één keer per sleutel). */
export function stijlIndex(modaliteit, stippel) {
  if (stippel) return STIJL_STIPPEL;
  const i = MODALITEITEN.indexOf(modaliteit);
  if (i < 0) { meld(`modaliteit "${modaliteit}" (lijnstijl)`); return STIJL_ONBEKEND; }
  return i;
}

/** Welke grondstof hoort bij een stroom-id?
 *
 * De id's zijn `<grondstof>-<bron>-<bestemming>` (`koper-collahuasi-tongling`,
 * `lithium-greenbushes-zhangjiagang`, `grafiet-balama-vs`), dus het eerste
 * segment ís de grondstof.
 *
 * ⚠️ BEWUST AFGELEID EN NIET GEBAKKEN. Er gaat geen `grondstof`-veld in
 * `stroomroute-*.json`, want dat zou vijf herbakes kosten voor één string —
 * precies wat besluit "bakken is geen deliverable" (2026-08-06) uitsluit.
 * Blijkt de afleiding ooit te kort te schieten (twee grondstoffen in één
 * streng), dan hoort dat in het losse metadatabestand naast de stroom, niet in
 * de gebakken geometrie.
 */
export function grondstofVan(stroomId) {
  return String(stroomId || "").split("-")[0];
}

/** Kleur van een been, gegeven de kleurmodus.
 *
 * ⚠️ EEN ONBEKENDE SLEUTEL MOET LUID ZIJN, NIET WIT. Op 2026-08-06 kostte
 * `KLEUR[been.modaliteit] ?? 0xffffff` een teruggedraaide commit: modaliteit
 * `weg` bestond niet (het heet `truck`), het been werd stilzwijgend wit, en wit
 * is in deze atlas geen legenda-kleur maar "onbekend". Daarom hier één keer per
 * onbekende sleutel een waarschuwing.
 */
export function kleurVan(modaliteit, stroomId, kleurModus) {
  if (kleurModus === "grondstof") {
    const g = grondstofVan(stroomId);
    const k = GRONDSTOF_KLEUR[g];
    if (k === undefined) meld(`grondstof "${g}" (stroom ${stroomId})`);
    return k ?? ONBEKEND;
  }
  const k = MODALITEIT_KLEUR[modaliteit];
  if (k === undefined) meld(`modaliteit "${modaliteit}"`);
  return k ?? ONBEKEND;
}

function meld(wat) {
  if (gemeld.has(wat)) return;
  gemeld.add(wat);
  console.warn(`[atlas v2] stroomstijl: onbekende ${wat} → wit getekend`);
}

// ── Lijnvorm ───────────────────────────────────────────────────────────────

export const LIJNMODI = ["route", "recht-plat", "recht-boog", "recht-zeeboog"];

/** Hoe hoog gaat de boog?
 *
 * Op de piek `LIFT_MAX × (hoek / π)` van de bolstraal: een been rond de halve
 * aardbol krijgt de volle lift, een truckbeen van 8 km vrijwel niets. Dat is
 * v1's `arcStyle.lift: 0.22` met dezelfde afhankelijkheid van de afstand — de
 * look die Lars van v1 kende — alleen nu uitsluitend op de hemelsbreed-lijnen.
 */
const LIFT_MAX = 0.22;

/** Krijgt dit been een boog in deze modus? */
function tiltOp(modaliteit, lijnModus) {
  // ⚠️ LUCHT BOOGT IN ÉLKE LIJNMODUS, ook in "onze routes" (M31 golf 3,
  // 2026-09-28). Het besluit "de lijnen blijven op de grond" (2026-08-07) gaat
  // over routes die OP de grond liggen: daar zou optillen de gemeten geul of het
  // gemeten spoor onwaar maken. Een vlucht ligt echt in de lucht, dus hier is de
  // boog de eerlijke weergave en niet de verzonnen. Zelfde reden als in v1 (M6):
  // "goud vliegt écht die boog, voor lithium was hij fout". De hoogte blijft
  // overdreven (een vrachtvliegtuig vliegt op ~11 km); de boog zegt "dit been
  // gaat door de lucht", niet "op deze hoogte".
  if (modaliteit === "lucht") return true;
  if (lijnModus === "recht-boog") return true;
  // Zee is de modaliteit waar een rechte lijn het vaakst over land snijdt, dus
  // daar koopt de boog het meest op.
  if (lijnModus === "recht-zeeboog") return modaliteit === "zee";
  return false;
}

/** Ligt dit been in deze lijnmodus op het oppervlak (straalfactor 1 overal)?
 *  Alleen dan mag een aanroeper het been verdichten zonder de hoogte te
 *  verliezen — `verdicht()` in stroomroute.js zet de straalfactor op 1. */
export function ligtOpGrond(been, lijnModus) {
  return lijnModus === "route" && been.modaliteit !== "lucht";
}

const D2R = Math.PI / 180;

/** Grootcirkel-hoek tussen twee [lon,lat]-punten, in radialen. */
function hoek(a, b) {
  const la1 = a[1] * D2R, la2 = b[1] * D2R;
  const dLa = la2 - la1, dLo = (b[0] - a[0]) * D2R;
  const s = Math.sin(dLa / 2) ** 2 +
    Math.cos(la1) * Math.cos(la2) * Math.sin(dLo / 2) ** 2;
  return 2 * Math.asin(Math.min(1, Math.sqrt(s)));
}

/** De punten van een been in de gevraagde lijnmodus, als [lon, lat, hoogtefactor].
 *
 * De derde waarde is een VERMENIGVULDIGER op de bolstraal (1 = op de schil waar
 * de route ligt). Zo hoeft geen enkele aanroeper te weten óf er een boog is: hij
 * krijgt gewoon punten met een straalfactor erbij.
 *
 * ⚠️ HEMELSBREED = KOP → STAART PER BEEN, niet mijn → eindfabriek in één keer.
 * De benen zijn precies de stukken tussen twee overslagpunten, en die punten
 * dragen de hele keten: waar de drager wisselt is de plek waar de atlas iets te
 * vertellen heeft. Eén boog over de hele keten zou de overslag onzichtbaar
 * maken — dan zie je nog wel dát Chili naar China levert, maar niet meer dát er
 * in Beilun iets van boord gaat.
 */
export function beenPunten(been, lijnModus) {
  const punten = been.punten || [];
  // Een luchtbeen is gebakken als grootcirkel (maak_luchtbeen.py), dus de boog
  // hieronder volgt in "onze routes" exact de gebakken lijn, alleen opgetild.
  if (ligtOpGrond(been, lijnModus) || punten.length < 2) {
    return punten.map((p) => [p[0], p[1], 1]);
  }

  const a = punten[0], b = punten[punten.length - 1];
  const d = hoek(a, b);
  if (!(d > 1e-9)) return punten.map((p) => [p[0], p[1], 1]);

  // Zoveel punten dat de koorde onder de tegel-schil blijft (~130 m) én de boog
  // glad oogt: één punt per ~50 km, met een ondergrens voor korte benen en een
  // plafond zodat een zeebeen van 19.000 km geen 4.000 punten krijgt.
  const km = d * 6371;
  const n = Math.min(512, Math.max(48, Math.ceil(km / 50)));

  const lift = tiltOp(been.modaliteit, lijnModus) ? LIFT_MAX * (d / Math.PI) : 0;

  const la1 = a[1] * D2R, lo1 = a[0] * D2R;
  const la2 = b[1] * D2R, lo2 = b[0] * D2R;
  const sinD = Math.sin(d);
  const uit = [];
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    const f1 = Math.sin((1 - t) * d) / sinD;
    const f2 = Math.sin(t * d) / sinD;
    const x = f1 * Math.cos(la1) * Math.cos(lo1) + f2 * Math.cos(la2) * Math.cos(lo2);
    const y = f1 * Math.cos(la1) * Math.sin(lo1) + f2 * Math.cos(la2) * Math.sin(lo2);
    const z = f1 * Math.sin(la1) + f2 * Math.sin(la2);
    uit.push([
      Math.atan2(y, x) / D2R,
      Math.atan2(z, Math.hypot(x, y)) / D2R,
      1 + lift * Math.sin(Math.PI * t),
    ]);
  }
  return uit;
}
