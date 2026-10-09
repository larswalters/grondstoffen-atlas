// gloed.js — het GLOED-MECHANISME, sinds golf 1 van de visuele fase als ÉÉN
// object voor alle knopen samen (2026-10-08, LAR-617), en sinds golf 2
// (2026-10-09) herontworpen als LICHTPUNT MET KOEPEL na Lars' telefoontest.
//
// Waarom dit bestaat: de oude gloedknopenlaag (tot ?v=131) bouwde de koepel-
// gloed voor de 36 uitgezochte kopersites, en op 2026-08-07 vroeg Lars om ook
// de belangrijke punten van een stroom (mijn · overslag · fabriek) zo te laten
// oplichten —
// *"die witte ballen met cirkel erom moeten eigenlijk de gloedbron worden … zowel
// stroom, gloed als die belangrijke punten moeten die gloeihotspots worden."*
// Dat is één mechanisme met twee bronnen, dus het mechanisme hoort hier.
//
// ⚠️ EN HET IS OOK EEN INHOUDELIJK PUNT, GEEN OPRUIMING. De ontwerpbrief zegt dat
// de wereld-hotspot moet **ONTSTAAN** uit de optelling van losse glows. Met de
// stroomknopen erbij lichten Balama, Nacala, Vidalia, Greenbushes, Lobito en
// Duisburg óók op, en telt de gloed op waar een stroom door een complex loopt.
//
// HET MECHANISME (sinds de oude gloedknopenlaag, en dat is gebleven): de maat
// schaalt mee met de kijkafstand via een hybride regel — een echte wereldmaat
// (de faciliteit, uit het gewicht) MET een pixel-minimum. Dichtbij wint de
// wereldmaat → elke faciliteit een eigen lichtje. Veraf zakt die onder het
// minimum → alle knopen worden even groot, buren vallen op dezelfde pixels en
// tellen additief op. Eén formule, twee gedragingen, geen zoomdrempel en dus
// per constructie geen pop-in. Zonder pixel-minimum zou een fabriek van 1 km op
// wereldhoogte kleiner dan een pixel worden en verdwijnen — dat minimum ÍS het
// mechanisme, geen ondergrens tegen onzichtbaarheid.
//
// ⚠️ WAT ER IN GOLF 1 VERANDERDE WAS ALLEEN DE IMPLEMENTATIE. ?v=131 had per
// bron een eigen groep van vijf Points (182 stromen + 14 sitelagen = 1.164
// objecten in atlasmodus). Sindsdien liggen alle schillen van ALLE knopen als
// vertex-reeksen in één Points (additief is commutatief, dus de tekenvolgorde
// binnen de koepel draagt niets); de per-frame maat blijft in JS (gemeten
// < 0,3 ms voor alle knopen — de winst zat nooit in die lus maar in de
// objecten). De camera komt binnen in GROEP-LOKALE ruimte (de bol draait, de
// camera staat vast), dus er is geen localToWorld per punt. Sinds stap 4 van
// golf 1 is dit de enige aanroepvorm.
//
// ═══ WAT ER IN GOLF 2 VERANDERDE, EN WAAROM (2026-10-09) ═══════════════════════
// Lars testte ?v=132 op zijn telefoon (Honor, pixelRatio 2): alles werkt, maar
// de gloedspots "zien er nog niet helemaal nice uit". Hij koos drie symptomen
// uit screenshots, en elk had een aanwijsbare oorzaak in DEZE laag:
//
//   1. "VAGE VLEKKEN" op wereldhoogte — geen helder lichtpunt met een kern.
//      · Vijf even gecentreerde gaussen van afnemende breedte tellen van bovenaf
//        op tot één gladde bult: er was geen kern die eruit sprong.
//      · De kleur ging LINEAIR het scherm op. `THREE.Color.setHex` zet sRGB om
//        naar lineair (ColorManagement staat aan in r185), maar deze
//        ShaderMaterial schreef gl_FragColor zonder `<colorspace_fragment>`.
//        Koper ff8a30 werd zo (255, 65, 8): roodbruin op een donkere bol; groen en
//        blauw zakten het verst weg. De LIJN (LineMaterial) zet wél om — de
//        legenda loog dus, voor de derde keer in dit project (na ACES en blending).
//      · Bij d = 1 werd de halo hard afgekapt op ~5 % van de piek: een vaag randje.
//   2. "WAAS BIJ INZOOMEN" — Tongling op 14 km: één oranje sluier over het halve
//      scherm in plaats van een lichtje per fabriek.
//      · De wereldstraal was 0,30·√gewicht, en het gewicht staat PER GRONDSTOF in
//        een andere eenheid: koper tot 10,8 km, uranium tot 36,7 km. Dat is een
//        district, geen fabriek. (De helderheid werd wél per grondstof
//        genormaliseerd, de straal niet.)
//      · Groei zonder plafond en met constante piek: het licht groeide mee met de
//        oppervlakte (~1.700 device-px per sprite op 14 km, geklemd door de GPU).
//      · De koepel was 2,6 × die straal hoog — tot ~28 km (koper) en ~95 km
//        (uranium): op 14 km kijkhoogte staken schillen BOVEN de camera uit.
//   3. "WEG OP MIDDENHOOGTE" — rond 2.500 km bijna onzichtbaar.
//      · "sterkte 0,30 per schil, bewust zwak — de optelling maakt hem fel": een
//        GEÏSOLEERDE knoop werd dus per ontwerp nooit fel, en op 2.500 km staan er
//        nog maar ~12 in beeld, vrijwel allemaal los. Piek 0,17–0,60, lineair.
//      · Het pixel-minimum (34) stond in DEVICE-px: op pixelRatio 2 is dat 17
//        css-px, en de wereldmaat kwam er half zo groot uit als bedoeld. Het
//        ontwerp was op een DPR-1-desktop afgestemd; de telefoon kreeg een kwart
//        van de lichtenergie.
//
// DE NIEUWE VORM: elke knoop is een LICHTPUNT (een kern: de lamp) met daaromheen
// een HALO in koepelvorm (het optelwerk). Per symptoom:
//   1 → De kern is een eigen sprite met een smalle, zachte gauss (halfwaarde-
//       breedte 3,5–5,3 css-px) op 0,50–0,70 in de ECHTE lijnkleur
//       (`<colorspace_fragment>`); de halo loopt als (1−d²)² met helling 0 naar
//       nul — geen rand, geen ring. Een cluster telt op tot een witheet midden
//       met een gekleurde krans: de hotspot ONTSTAAT nog steeds uit de optelling.
//   2 → De wereldstraal is per grondstof genormaliseerd naar de maat van een
//       FABRIEK (0,30–0,90 km, via q zoals de helderheid al was). Zodra de
//       wereldmaat het pixel-minimum overstijgt WAAIERT de halo uit: hij wordt
//       groter maar zijn piek zakt (∝ (minimum/maat)^0,75), en zijn diameter
//       heeft een plafond (160 css-px). De kern neemt het vrijgekomen licht over,
//       zodat het lichtje in het midden overal even helder blijft. De koepel tilt
//       in SCHERMMAAT (hoogte = de straal van de halo zoals je hem ziet) en kan
//       de camera daardoor op geen enkele hoogte meer raken.
//   3 → De zichtbaarheid zit in de KERN van de knoop zelf, niet in de optelling:
//       een losse knoop heeft op elke hoogte in zijn midden 0,70–1,00 van zijn
//       eigen kleur. Alle maten staan in CSS-px en worden met de pixelRatio
//       vermenigvuldigd, dus telefoon en desktop zien hetzelfde.
//
// ⚠️ PIEK PER KNOOP ≤ 1, EN DAT IS GEEN SMAAK. Kern + halo in het midden van één
// losse knoop haalt hooguit 1,0 (kernPiek + haloPiek bij q = 1). Additief in een
// 8-bit sRGB-buffer klemt per KANAAL; boven 1 verschuift de TINT in plaats van
// dat het wit wordt — koper ×1,42 = #ffc444 ligt op 0,06 van goud, kobalt ×2 is
// grafiet. Dat is de legenda-klasse. ⚠️ En twee knopen op dezelfde pixels ZIJN
// één knoop ×2: daarom tellen gelijk-gekleurde knopen die op het scherm
// samenvallen niet in licht maar in gewicht op — (a), (b) en (c) hieronder.
//
// ⚠️ EEN STROOMKNOOP TELT NIET DUBBEL MET ZIJN EIGEN SITE — in twee lagen.
// Een stroomknoop (marker) is het routeeranker van een site: hij ligt exact op
// een registersite of op de marker van een andere stroom (Ningbo ×6, Valcambi
// ×5, de Tongling-kade ×4), of een paar km verderop op de laadplek ervan (Oyu
// Tolgoi: de concentrator op 4,45 km). Met een felle kern telden site en marker
// op tot boven 1 per kanaal, en dan VERSCHUIFT DE TINT: de koperen Oyu Tolgoi
// werd op 2.500 km (255, 222, 77) — goud (gemeten in de lokale atlas, alleen de
// gloed op zwart). Met (b) is hij daar (240, 129, 44) = 0,94 × ff8a30. Daarom:
//   (a) Samenvallen (bouwtijd). Een knoop met `samenvallen: true` gaat op in het
//       dichtstbijzijnde lichtpunt van dezelfde kleur binnen `samenvalKm`
//       (250 m: dezelfde plek). Dat lichtpunt brandt zolang één lid aan staat,
//       met de grootste q van de leden die aan staan. Op de data van ?v=132
//       gaan zo 208 van de 1.101 knopen op in een ander lichtpunt (893 over).
//   (b) Overdragen op het scherm (per frame, continu). Een marker-lichtpunt met
//       een SITE van dezelfde kleur binnen `partnerKm` (10 km: dezelfde
//       faciliteit) dooft uit zolang die twee op het scherm over elkaar liggen
//       (scheiding < `scheidPx`), en de site neemt dan zijn q over (de grootste
//       van de twee). Zoom je in tot ze uit elkaar liggen, dan krijgt de marker
//       zijn eigen lichtje terug — de lijn eindigt op de concentrator en daar
//       brandt het dan ook. Een functie van de pixelscheiding, dus geen drempel.
//   (c) Site ↔ site, op het scherm (per frame, continu) — sinds de review van
//       golf 2. Twee registersites van dezelfde kleur op een paar km (Mutanda–
//       Deziwa 1,5 km, Chuquicamata mijn + smelter 1,1 km, Morowali, Tricastin
//       en QCLNG/GLNG op dezelfde coördinaat) telden hun LICHT op, en dat
//       klemde al bij twee sites: kobalt ×1,8 leest als grafiet, koper ×1,4 als
//       goud — gemeten in de lokale ?v=133, 55 siteparen binnen 2 km. Daarom
//       draagt een site aan de dichtstbijzijnde GROTERE site van dezelfde kleur
//       binnen `siteKm` over, met dezelfde pixelscheiding als (b), maar nu tellen
//       de CAPACITEITEN op: q = √(q₁² + q₂²) = √(Σg/gmax), tot 1. Liggen ze op het
//       scherm uiteen, dan heeft elk weer een eigen lichtje.
// Dit zijn GEEN aggregaat-objecten en de hotspot ONTSTAAT nog steeds uit de
// optelling: (a) en (b) halen één faciliteit die twee keer telde terug naar
// één, en (c) telt naburige installaties op in het gewicht in plaats van in het
// geklemde licht. Sites die verder uiteen liggen (Tongling, Guixi, de Bushveld)
// tellen op het scherm gewoon additief op tot een witheet midden met een
// gekleurde krans — dat "uitgebrand wit" heeft Lars geaccepteerd. ⚠️ Waar zo'n
// cluster op wereld- of middenhoogte toch door een andere legendakleur loopt,
// helpt alleen een HDR-doel met een tintbehoudende resolve (rgb/max(1,max)) —
// een extra pass en fill-rate op de telefoon, dus een apart besluit.
//
// ⚠️ VERBERGEN GEBEURT BUITEN HET CLIPVOLUME, NIET MET PUNTGROOTTE 0. GLES noemt
// gl_PointSize ≤ 0 ongedefinieerd; gemeten in Chrome (ANGLE/D3D11) tekenen 0,
// 0,3 en −5 allemaal één pixel op VOLLE middenwaarde, en met depthTest:false ook
// voor knopen ACHTER de bol. Met een felle kern zou elke verborgen knoop een
// scherpe stip worden. De vertex-shader zet een knoop met grootte 0 daarom op
// z/w = 2 (geklipt, 0 pixels). De horizontoets zelf blijft de CPU-toets — een
// eigen ShaderMaterial zou anders de clipping-chunks nodig hebben, en die toets
// is gratis. ⚠️ De precisiestippen van de bouwmodus (stroombundel.js) verbergen
// nog met grootte 0 en hebben dezelfde fout; bewust buiten deze golf gelaten.

import * as THREE from "three";

export const AARDSTRAAL_KM = 6371;

// Afstemknoppen, gedeeld door beide bronnen zodat een stroomknoop en een
// registersite met dezelfde q ook even groot en even fel zijn. Alles in css-px
// (de update vermenigvuldigt met de pixelRatio). Een paar [a, b] betekent
// a + b·q, met q ∈ [0, 1] het per grondstof genormaliseerde gewicht.
// Live bijstellen kan in de console: `ATLAS.gloed.afstemming.<knop> = …` werkt
// vanaf het volgende frame (de update leest AFSTEMMING per frame); alleen
// SCHILLEN, samenvalKm, partnerKm en siteKm gelden bij het bouwen.
export const AFSTEMMING = {
  // ── de faciliteit in de wereld
  wereldKm: [0.30, 0.60],    // straal 0,30–0,90 km: de maat van een fabriek, geen district
  // ── de kern (de lamp) — een eigen sprite
  kernPx: [12, 6],           // sprite-diameter op het minimum (halfwaardebreedte ≈ 0,29 × dit)
  kernWereld: 0.25,          // dichtbij groeit de kern mee: 0,25 × de wereldmaat …
  kernMaxPx: 30,             // … tot hooguit dit (halfwaardebreedte ≈ 8,8 css-px)
  kernPiek: [0.50, 0.20],    // ⚠️ kernPiek + haloPiek ≤ 1 bij elke q — zie de kop
  kernUitdoofPx: 300,        // boven deze wereldmaat (css) dimt de kern ∝ 1/maat: op straat-
                             // niveau is de satellietfoto de inhoud (1 km hoogte → ~1/7)
  // ── de halo (de koepel, het optelwerk)
  haloPx: [22, 14],          // diameter op het minimum: 22–36 css = op 9.000 km 180–295 km
  haloMaxPx: 160,            // plafond van de diameter — de waasgarantie
  haloPiek: [0.20, 0.10],    // piek van de hele koepel van boven gezien, op het minimum
  uitwaaier: 0.75,           // γ: piek ∝ (minimum / wereldmaat)^γ zodra de wereld wint.
                             // 0 = constante piek = de waas van ?v=132; 2 = strikt
                             // energiebehoud, dan verdwijnt de eigen glow per fabriek
  koepel: 1.0,               // koepelhoogte = dit × de straal van de halo (schermmaat)
  // ── randen en budget
  horizonBand: 0.03,         // over de laatste 3 % (in cos) vóór de horizon dooft een knoop uit
  kegelBand: 0.03,           // zachte rand van de kijkkegel in de budgettelling
  budget: 2.5,               // totale halo-oppervlakte ≤ dit × de framebuffer (fill-rate Honor)
  // ── dubbeltelling (zie de kop)
  samenvalKm: 0.25,          // (a) stroomknoop gaat op in een gelijk-gekleurd punt binnen dit
  partnerKm: 10,             // (b) stroomknoop draagt over aan een gelijk-gekleurde site binnen dit …
  scheidPx: [6, 24],         // … zolang ze op het scherm minder dan [6 → 24] css-px uiteen liggen
  siteKm: 2,                 // (c) site draagt over aan een gelijk-gekleurde, grotere site binnen dit
};

// ✅ BESLUIT LARS (2026-08-06): de gloed is een KOEPEL met hoogte, geen platte
// schijf. Elke schil is dezelfde knoop, opgetild en smaller gemaakt volgens een
// halve bol (breedte = √(1−u²)); additief opgeteld leest dat als één volume dat
// boven het terrein uitsteekt.
//
// ⚠️ DIT IS GEEN OMKERING VAN BESLUIT 2 UIT DE ONTWERPBRIEF ("glow-bollen, géén
// hoogte-pilaren" = capaciteit-als-hoogte). Hier draagt de hoogte geen betekenis:
// de koepel is een halve bol over de halo (hoogte = halostraal bij koepel 1,0),
// capaciteit blijft in grootte en helderheid.
//
// ⚠️ GOLF 2: DE HOOGTE IS NU SCHERMMAAT EN BEGRENSD. Was 2,6 × de wereldstraal
// (tot 95 km — boven de camera op 14 km). Nu tilt de vertex-shader elke schil
// met u × koepel × (de halostraal in device-px), omgerekend naar wereldlengte op
// déze diepte: de koepeltop ligt op ≤ 0,83·80/1099 ≈ 6 % van de kijkafstand
// (telefoon staand; liggend ~13 %), op elke hoogte, zonder drempel. Recht van
// boven projecteert de verticaal op nul (concentrisch); naar de rand van het beeld
// en bij de horizon rijst de koepel op. Drie schillen in plaats van vijf: het
// koepelbeeld blijft en de fill-rate zakt (Σ breedte² 2,86 → 2,07).
//
// [u = fractie van de koepelhoogte, breedtefactor √(1−u²), aandeel in de halopiek]
export const SCHILLEN = [
  [0.00, 1.000, 0.52],
  [0.50, 0.866, 0.30],
  [0.83, 0.558, 0.18],
];

function opBol(lonDeg, latDeg, r) {
  // Exact dezelfde afspraak als world.js/aisgloed.js (z = −sin lon).
  const lon = lonDeg * (Math.PI / 180);
  const lat = latDeg * (Math.PI / 180);
  const c = Math.cos(lat);
  return [r * c * Math.cos(lon), r * Math.sin(lat), -r * c * Math.sin(lon)];
}

// position = het GRONDPUNT voor de kern én alle schillen; de koepel tilt hier,
// zodat er per frame geen posities heen en weer hoeven (alleen `maat`).
// ⚠️ De bol ligt om de oorsprong van deze groep (globeGroup, alleen rotatie),
// dus "omhoog" = de richting van het bolmiddelpunt naar het punt, in view-ruimte.
// ⚠️ Schermrand: GLES gooit een punt weg zodra zijn MIDDELPUNT buiten beeld valt
// (per driver verschillend). Daarom dooft een sprite uit over zijn eigen straal
// vóór de rand, in plaats van daar als halve schijf te verdwijnen.
const VERT = `
uniform float uPxPerEenheid;  // device-px per scene-eenheid op afstand 1 (perEenheid · pixelRatio)
uniform float uKoepel;        // AFSTEMMING.koepel
uniform vec2 uViewport;       // framebuffer in device-px
attribute vec2 maat;          // x = puntgrootte (device-px, 0 = verborgen), y = piekalfa
attribute vec2 stijl;         // x = u / breedte (0 voor de kern), y = 1 kern · 0 halo
attribute vec3 kleur;         // LINEAIR (THREE.Color.setHex) — terug naar sRGB in de fragment-shader
varying vec3 vKleur;
varying float vAmp;
varying float vVorm;
void main() {
  if (maat.x < 0.5) {
    gl_Position = vec4(0.0, 0.0, 2.0, 1.0);   // buiten het clipvolume → 0 pixels
    gl_PointSize = 1.0;
    vKleur = vec3(0.0); vAmp = 0.0; vVorm = 0.0;
    return;
  }
  vec4 mv = modelViewMatrix * vec4(position, 1.0);
  vec3 omhoog = normalize(mv.xyz - modelViewMatrix[3].xyz);
  // lift in device-px = u · koepel · halostraal; maat.x / breedte = basisdiameter
  float liftPx = uKoepel * stijl.x * maat.x * 0.5;
  mv.xyz += omhoog * (liftPx * (-mv.z) / uPxPerEenheid);
  gl_Position = projectionMatrix * mv;
  gl_PointSize = maat.x;
  vec2 ndc = gl_Position.xy / gl_Position.w;
  vec2 rand = (1.0 - abs(ndc)) * 0.5 * uViewport;
  float randF = clamp(min(rand.x, rand.y) / max(0.5 * maat.x, 1.0), 0.0, 1.0);
  vKleur = kleur;
  vAmp = maat.y * randF;
  vVorm = stijl.y;
}
`;

// Twee vormen in één shader. KERN: smalle gauss die op de spriterand exact 0 is
// (halfwaardebreedte 0,29 × de sprite). HALO: (1−d²)², komt met helling 0 op nul
// — geen afgekapte rand en geen ringen meer (?v=132 kapte op 5 % van de piek af).
// Opgeteld over buren is de halo een kerndichtheidsschatting: de hotspot ONTSTAAT.
// ⚠️ <colorspace_fragment> zet de lineaire kleur terug naar het uitvoerformaat
// vóór het additief mengen — exact het pad van de lijn (LineMaterial), dus gloed,
// komeet en lijn hebben per constructie dezelfde tint. En het blijft kloppen als
// er ooit naar een lineair render target getekend wordt (selectieve bloom).
// Bewust GEEN <tonemapping_fragment>: de belichtingsknop raakt alleen de ondergrond.
const FRAG = `
precision highp float;
varying vec3 vKleur;
varying float vAmp;
varying float vVorm;
void main() {
  vec2 p = gl_PointCoord * 2.0 - 1.0;
  float d2 = dot(p, p);
  if (d2 >= 1.0) discard;
  float w = 1.0 - d2;
  float vorm = vVorm > 0.5 ? exp(-7.0 * d2) * w : w * w;
  gl_FragColor = vec4(vKleur, vAmp * vorm);
  #include <colorspace_fragment>
}
`;

const glad = (x) => (x <= 0 ? 0 : x >= 1 ? 1 : x * x * (3 - 2 * x));

/** Bouw de gloedlaag als één Points.
 *
 * @param knopen  [{lon, lat, q (0..1, genormaliseerd per grondstof), kleur (0xRRGGBB),
 *                 samenvallen? (stroomknoop: mag opgaan in een gelijk-gekleurd punt)}]
 *                — q bepaalt zowel de wereldmaat als de helderheid (AFSTEMMING)
 * @param radius  de schil waarop de laag ligt (CONFIG.vectorLift-schil)
 * @param renderOrder
 * @returns {groep, punten, update(camLocaal, perEenheid, scherm), zetAan(i, aan),
 *           zetKleur(i, hex), commitKleur(), afstemming, aantal, fysiek, paren, siteparen}
 *
 * `update` wil de camera in de LOKALE ruimte van de groep waarin deze laag
 * hangt (globeGroup): één inverse matrix per frame bij de aanroeper, geen
 * localToWorld per punt. `perEenheid` = CSS-px per scene-eenheid op afstand 1
 * (h / (2·tan(fov/2)), met h = css-hoogte). `scherm` = {dpr, breedte, hoogte
 * (css), bufferB, bufferH (device-px), maxPunt} en is VERPLICHT: zonder de
 * pixelRatio komt de fout van ?v=132 terug (maten half zo groot op een telefoon).
 * De camera kijkt altijd naar het bolmiddelpunt (globe.js); daar leunt de
 * kijkkegel van het budget op.
 *
 * `aantal` = het aantal invoerknopen (de indexruimte van zetAan/zetKleur);
 * `fysiek` = het aantal lichtpunten na het samenvallen (a); `paren` = het aantal
 * stroomknoop-lichtpunten met een site om aan over te dragen (b).
 */
export function bouwGloed(knopen, radius, renderOrder = 7.45) {
  const n = knopen.length;
  const groep = new THREE.Group();
  groep.name = "gloed";
  if (!n) return { groep, punten: null, update() {}, zetAan() {}, zetKleur() {}, commitKleur() {}, afstemming: AFSTEMMING, aantal: 0, fysiek: 0, paren: 0 };

  // --- (a) samenvallen: welk invoerknoop-nummer hoort bij welk lichtpunt -----
  // Sites eerst, elk een eigen lichtpunt (nummers 0 … nSitePunten−1); daarna
  // gaat elke stroomknoop op in het dichtstbijzijnde lichtpunt van dezelfde kleur
  // binnen samenvalKm, of wordt zelf een lichtpunt (waar latere stroomknopen weer
  // in op kunnen gaan).
  const fys = new Int32Array(n);
  const fysEenheid = [];              // [x, y, z] op de eenheidsbol
  const fysLeden = [];
  const perKleur = new Map();         // kleur → [lichtpuntnummers]
  function nieuwPunt(i, k, e) {
    const p = fysEenheid.length;
    fysEenheid.push(e);
    fysLeden.push([i]);
    (perKleur.get(k.kleur) || perKleur.set(k.kleur, []).get(k.kleur)).push(p);
    return p;
  }
  function dichtstbij(k, e, maxKm, totPunt) {
    let beste = -1, besteD = maxKm / AARDSTRAAL_KM;   // koorde op de eenheidsbol
    for (const p of perKleur.get(k.kleur) || []) {
      if (p >= totPunt) continue;
      const f = fysEenheid[p];
      const dd = Math.hypot(f[0] - e[0], f[1] - e[1], f[2] - e[2]);
      if (dd <= besteD) { besteD = dd; beste = p; }
    }
    return [beste, besteD];
  }
  knopen.forEach((k, i) => { if (!k.samenvallen) fys[i] = nieuwPunt(i, k, opBol(k.lon, k.lat, 1)); });
  const nSitePunten = fysEenheid.length;
  knopen.forEach((k, i) => {
    if (!k.samenvallen) return;
    const e = opBol(k.lon, k.lat, 1);
    const [beste] = dichtstbij(k, e, AFSTEMMING.samenvalKm, Infinity);
    if (beste < 0) fys[i] = nieuwPunt(i, k, e);
    else { fys[i] = beste; fysLeden[beste].push(i); }
  });
  const m = fysEenheid.length;

  // --- (b) overdragen: een stroomknoop-lichtpunt en zijn site ------------------
  // Alleen lichtpunten zónder site (puur stroomknopen) krijgen een partner, en die
  // partner is altijd een SITE-lichtpunt: zo kan er geen keten of wederzijds
  // uitdoven ontstaan.
  const partner = new Int32Array(m).fill(-1);
  const partnerAfst = new Float32Array(m);   // koorde in scene-eenheden
  const paren = [];
  for (let p = nSitePunten; p < m; p++) {
    const k = knopen[fysLeden[p][0]];
    const [s, koorde] = dichtstbij(k, fysEenheid[p], AFSTEMMING.partnerKm, nSitePunten);
    if (s < 0) continue;
    partner[p] = s;
    partnerAfst[p] = koorde * radius;
    paren.push(p);
  }

  const qIn = new Float32Array(n);
  let qOntbreekt = 0;
  knopen.forEach((k, i) => {
    const q = Number.isFinite(k.q) ? k.q : (qOntbreekt++, 1);
    qIn[i] = Math.min(1, Math.max(0, q));
  });
  if (qOntbreekt) console.warn(`[atlas v2] gloed: ${qOntbreekt} knopen zonder q — als q = 1 getekend`);
  const aanIn = new Uint8Array(n).fill(1);

  // --- (c) overdragen tussen sites van dezelfde kleur ---------------------------
  // Elk site-lichtpunt krijgt als partner het dichtstbijzijnde site-lichtpunt van
  // dezelfde kleur binnen siteKm met een GROTERE rang (q van de site zelf, dan
  // het nummer). Strikt stijgende rang = een boom, nooit een kring; per frame
  // lopen we in oplopende rang, zodat een site eerst ontvangt en dan pas zelf
  // (met wat hij ontving) doorgeeft.
  const rang = new Float32Array(nSitePunten);
  for (let p = 0; p < nSitePunten; p++) rang[p] = qIn[fysLeden[p][0]];
  const groter = (a, b) => rang[a] > rang[b] || (rang[a] === rang[b] && a > b);
  const sitePartner = new Int32Array(nSitePunten).fill(-1);
  const sitePartnerAfst = new Float32Array(nSitePunten);   // koorde in scene-eenheden
  for (let p = 0; p < nSitePunten; p++) {
    const k = knopen[fysLeden[p][0]], e = fysEenheid[p];
    let beste = -1, besteD = AFSTEMMING.siteKm / AARDSTRAAL_KM;
    for (const s of perKleur.get(k.kleur) || []) {
      if (s >= nSitePunten || !groter(s, p)) continue;
      const f = fysEenheid[s];
      const dd = Math.hypot(f[0] - e[0], f[1] - e[1], f[2] - e[2]);
      if (dd <= besteD) { besteD = dd; beste = s; }
    }
    if (beste >= 0) { sitePartner[p] = beste; sitePartnerAfst[p] = besteD * radius; }
  }
  const siteVolgorde = [];
  for (let p = 0; p < nSitePunten; p++) if (sitePartner[p] >= 0) siteVolgorde.push(p);
  siteVolgorde.sort((a, b) => (groter(a, b) ? 1 : groter(b, a) ? -1 : 0));

  // per lichtpunt: aan en q van de leden die aan staan (herbepaald bij zetAan)
  const aanF = new Uint8Array(m);
  const qF = new Float32Array(m);
  const vuilF = new Uint8Array(m).fill(1);
  let vuil = true;

  // --- vertices: [kern × m, schil 0 × m, schil 1 × m, schil 2 × m] ----------
  const S = SCHILLEN.length;
  const V = m * (1 + S);
  const pos0 = new Float32Array(m * 3);
  const pos = new Float32Array(V * 3);
  const kleur = new Float32Array(V * 3);
  const stijl = new Float32Array(V * 2);
  const maat = new Float32Array(V * 2);
  const c = new THREE.Color();
  for (let p = 0; p < m; p++) {
    const k = knopen[fysLeden[p][0]];
    const [x, y, z] = opBol(k.lon, k.lat, radius);
    pos0[p * 3] = x; pos0[p * 3 + 1] = y; pos0[p * 3 + 2] = z;
    c.setHex(k.kleur);
    for (let blok = 0; blok <= S; blok++) {
      const v = blok * m + p;
      pos[v * 3] = x; pos[v * 3 + 1] = y; pos[v * 3 + 2] = z;
      kleur[v * 3] = c.r; kleur[v * 3 + 1] = c.g; kleur[v * 3 + 2] = c.b;
      if (blok === 0) { stijl[v * 2] = 0; stijl[v * 2 + 1] = 1; }
      else { const [u, b] = SCHILLEN[blok - 1]; stijl[v * 2] = u / b; stijl[v * 2 + 1] = 0; }
    }
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const attrKleur = new THREE.BufferAttribute(kleur, 3);
  geo.setAttribute("kleur", attrKleur);
  geo.setAttribute("stijl", new THREE.BufferAttribute(stijl, 2));
  const attrMaat = new THREE.BufferAttribute(maat, 2);
  attrMaat.setUsage(THREE.DynamicDrawUsage);
  geo.setAttribute("maat", attrMaat);
  geo.boundingSphere = new THREE.Sphere(new THREE.Vector3(), radius * 2);

  const mat = new THREE.ShaderMaterial({
    vertexShader: VERT, fragmentShader: FRAG,
    uniforms: {
      uPxPerEenheid: { value: 1 },
      uKoepel: { value: AFSTEMMING.koepel },
      uViewport: { value: new THREE.Vector2(1, 1) },
    },
    blending: THREE.AdditiveBlending, transparent: true,
    depthTest: false, depthWrite: false,
    toneMapped: false,      // expliciet: de belichtingsknop (0,40/0,75/1,6) raakt de gloed nooit
  });
  const punten = new THREE.Points(geo, mat);
  punten.renderOrder = renderOrder;
  punten.frustumCulled = false;      // wij bepalen zichtbaarheid zelf, per punt
  punten.name = "gloed";
  groep.add(punten);

  function herbereken() {
    vuil = false;
    for (let p = 0; p < m; p++) {
      if (!vuilF[p]) continue;
      vuilF[p] = 0;
      let q = -1;
      for (const i of fysLeden[p]) if (aanIn[i] && qIn[i] > q) q = qIn[i];
      aanF[p] = q >= 0 ? 1 : 0;
      qF[p] = q >= 0 ? q : 0;
    }
  }

  // --- de per-frame maatregel ------------------------------------------------
  const BREED = SCHILLEN.map((s) => s[1]);
  const AANDEEL = SCHILLEN.map((s) => s[2]);
  const B2 = BREED.reduce((s, b) => s + b * b, 0);
  const kmNaarScene = radius / AARDSTRAAL_KM;
  const qE = new Float32Array(m);      // q van dit frame (na het overdragen)
  const mW = new Float32Array(m);      // overdraagweging van een stroomknoop (1 = eigen licht)
  const tW = new Float32Array(m);      // wereldmaat (css)
  const tDH = new Float32Array(m);     // halodiameter (css), vóór het budget
  const tG = new Float32Array(m);      // uitwaaierfactor van de halopiek
  const tWeeg = new Float32Array(m);   // horizon × overdragen (0 = verborgen)
  let schermGemeld = false;
  const NOODSCHERM = { dpr: 1, breedte: 1000, hoogte: 1000, bufferB: 1000, bufferH: 1000, maxPunt: 1024 };

  function update(camLocaal, perEenheid, scherm) {
    if (!groep.visible) return;
    if (!scherm || !(scherm.dpr > 0) || !(scherm.hoogte > 0)) {
      if (!schermGemeld) {
        schermGemeld = true;
        console.error("[atlas v2] gloed.update zonder scherm {dpr, breedte, hoogte, bufferB, bufferH, maxPunt} — de gloedmaten kloppen nu niet (zie gloed.js)");
      }
      scherm = NOODSCHERM;
    }
    if (vuil) herbereken();
    const A = AFSTEMMING;            // per frame gelezen: bijstellen in de console werkt meteen
    const dpr = scherm.dpr;
    const maxPx = scherm.maxPunt > 0 ? scherm.maxPunt : 1024;
    const d = camLocaal.length();
    if (d <= radius) return;
    // Zichtbaarheidsgrens op een bol: een punt p̂ is zichtbaar vanaf een camera op
    // afstand d als dot(p̂, ĉ) ≥ R/d. Exact, op elke hoogte, zonder drempel — en
    // sinds golf 2 met een zachte band ervóór, zodat een knoop van 0,7–1,0 niet
    // aan de bolrand aan- en uitknipt.
    const horizon = radius / d;
    const band = A.horizonBand * (1 - horizon);
    const cx = camLocaal.x, cy = camLocaal.y, cz = camLocaal.z;
    const rx = cx / d, ry = cy / d, rz = cz / d;
    // De kijkkegel om de beeldhoeken: tan(fov/2) volgt uit perEenheid zelf.
    const t = scherm.hoogte / (2 * perEenheid);
    const asp = (scherm.breedte || scherm.hoogte) / scherm.hoogte;
    const cosKegel = 1 / Math.sqrt(1 + t * t * (1 + asp * asp));

    // pass 0 — (b) overdragen: liggen een stroomknoop en zijn site op het scherm
    // over elkaar, dan dooft de stroomknoop uit en neemt de site zijn q over.
    for (let p = 0; p < m; p++) { qE[p] = qF[p]; mW[p] = 1; }
    const s0 = A.scheidPx[0], ds = Math.max(1e-6, A.scheidPx[1] - A.scheidPx[0]);
    for (const p of paren) {
      const s = partner[p];
      if (!aanF[p] || !aanF[s]) continue;
      const o = p * 3;
      const afst = Math.max(1e-6, Math.hypot(pos0[o] - cx, pos0[o + 1] - cy, pos0[o + 2] - cz));
      const w = glad(((partnerAfst[p] * perEenheid) / afst - s0) / ds);
      mW[p] = w;
      const q = qF[s] + Math.max(0, qF[p] - qF[s]) * (1 - w);
      if (q > qE[s]) qE[s] = q;
    }
    // (c) site → grotere site van dezelfde kleur: hier tellen de capaciteiten op
    // (√ van de som van de kwadraten = √(Σg/gmax)), want het zijn twee installaties.
    for (const p of siteVolgorde) {
      const s = sitePartner[p];
      if (!aanF[p] || !aanF[s]) continue;
      const o = p * 3;
      const afst = Math.max(1e-6, Math.hypot(pos0[o] - cx, pos0[o + 1] - cy, pos0[o + 2] - cz));
      const w = glad(((sitePartnerAfst[p] * perEenheid) / afst - s0) / ds);
      mW[p] = w;
      qE[s] = Math.min(1, Math.sqrt(qE[s] * qE[s] + (1 - w) * qE[p] * qE[p]));
    }

    // pass 1 — maten, en de totale halo-oppervlakte in beeld (device-px²)
    let opp = 0;
    for (let p = 0; p < m; p++) {
      tWeeg[p] = 0;
      if (!aanF[p] || mW[p] <= 0) continue;
      const o = p * 3, px = pos0[o], py = pos0[o + 1], pz = pos0[o + 2];
      const v = (px * rx + py * ry + pz * rz) / radius;
      if (v <= horizon) continue;
      const weeg = (band > 0 ? glad((v - horizon) / band) : 1) * mW[p];
      const vx = px - cx, vy = py - cy, vz = pz - cz;
      const afst = Math.max(1e-6, Math.hypot(vx, vy, vz));
      const q = qE[p];
      const W = (2 * (A.wereldKm[0] + A.wereldKm[1] * q) * kmNaarScene * perEenheid) / afst;
      const Smin = A.haloPx[0] + A.haloPx[1] * q;
      // ⚠️ De uitwaaierfactor rekent met de ONGEKLEMDE wereldmaat: voorbij het
      // plafond blijft de halo even groot maar wordt hij steeds zwakker, zodat er
      // dichtbij geen sluier van 160 css-px blijft hangen.
      tG[p] = W > Smin ? Math.pow(Smin / W, A.uitwaaier) : 1;
      const DH = Math.min(A.haloMaxPx, W > Smin ? W : Smin);
      tW[p] = W; tDH[p] = DH; tWeeg[p] = weeg;
      const cosZicht = -(vx * rx + vy * ry + vz * rz) / afst;
      const wKegel = glad((cosZicht - (cosKegel - A.kegelBand)) / A.kegelBand);
      const dpx = dpr * DH;
      opp += weeg * wKegel * dpx * dpx * B2;
    }
    // ⚠️ HET BUDGET REKENT MET DE MATEN VAN DIT FRAME, NIET MET DE VORIGE. Een klep
    // die op de vulling ná zichzelf stuurt slingert (σ = 1 → 0,71 → 1 …: flikkeren
    // op halve framerate). En omdat horizon-, overdraag- en kegelweging glad zijn,
    // verandert `opp` continu: geen sprong als één knoop de kegelrand passeert. De
    // klep krimpt alleen de halo's, met gelijke piek (minder licht, geen
    // flikkering); met de data van ?v=132 bijt hij op een telefoon hooguit bij de
    // hele bol op 20.000 km (f ≥ 0,96 in de simulatie) — hij is een vangnet voor
    // als het aantal knopen groeit, geen afstemknop.
    const bufB = scherm.bufferB || scherm.breedte * dpr, bufH = scherm.bufferH || scherm.hoogte * dpr;
    const bud = A.budget * bufB * bufH;
    const f = opp > bud ? Math.sqrt(bud / opp) : 1;

    // pass 2 — schrijven
    for (let p = 0; p < m; p++) {
      const weeg = tWeeg[p];
      if (weeg <= 0) {
        for (let blok = 0; blok <= S; blok++) { const v = blok * m + p; maat[v * 2] = 0; maat[v * 2 + 1] = 0; }
        continue;
      }
      const q = qE[p], W = tW[p], g = tG[p];
      const kernPiek = A.kernPiek[0] + A.kernPiek[1] * q;
      const haloPiek = A.haloPiek[0] + A.haloPiek[1] * q;
      // De kern neemt het licht over dat de uitwaaierende halo in het midden
      // verliest: kern + halo blijft in het midden kernPiek + haloPiek, op elke
      // hoogte — het lichtje is dichtbij even helder als veraf.
      const uitdoof = W > A.kernUitdoofPx ? A.kernUitdoofPx / W : 1;
      const kernAmp = (kernPiek + haloPiek * (1 - g)) * weeg * uitdoof;
      const DK = Math.min(A.kernMaxPx, Math.max(A.kernPx[0] + A.kernPx[1] * q, A.kernWereld * W));
      maat[p * 2] = Math.min(maxPx, DK * dpr);
      maat[p * 2 + 1] = Math.min(1, kernAmp);
      const haloAmp = haloPiek * g * weeg;
      const DH = f * tDH[p] * dpr;
      for (let s = 0; s < S; s++) {
        const v = (s + 1) * m + p;
        maat[v * 2] = Math.min(maxPx, BREED[s] * DH);
        maat[v * 2 + 1] = haloAmp * AANDEEL[s];
      }
    }
    mat.uniforms.uPxPerEenheid.value = perEenheid * dpr;
    mat.uniforms.uKoepel.value = A.koepel;
    mat.uniforms.uViewport.value.set(bufB, bufH);
    attrMaat.needsUpdate = true;
  }

  /** Eén invoerknoop aan/uit. Een lichtpunt brandt zolang één van zijn leden
   *  aan staat, met de grootste q van de leden die aan staan. */
  function zetAan(i, waarde) {
    const a = waarde ? 1 : 0;
    if (aanIn[i] === a) return;
    aanIn[i] = a;
    vuilF[fys[i]] = 1;
    vuil = true;
  }

  /** Eén knoop omkleuren (kern en alle schillen). Roep daarna `commitKleur()` aan.
   *  ⚠️ Een samengevallen lichtpunt heeft één kleur voor al zijn leden — ze
   *  vielen juist samen omdat ze dezelfde kleur hadden; omkleuren van één lid
   *  kleurt het hele lichtpunt. De partner voor het overdragen (b) is bij het
   *  bouwen gekozen op gelijke kleur en wordt hier niet opnieuw bepaald. */
  function zetKleur(i, hex) {
    c.setHex(hex);
    const p = fys[i];
    for (let blok = 0; blok <= S; blok++) {
      const v = blok * m + p;
      kleur[v * 3] = c.r; kleur[v * 3 + 1] = c.g; kleur[v * 3 + 2] = c.b;
    }
  }
  function commitKleur() { attrKleur.needsUpdate = true; }

  return { groep, punten, update, zetAan, zetKleur, commitKleur, afstemming: AFSTEMMING, aantal: n, fysiek: m, paren: paren.length, siteparen: siteVolgorde.length };
}
