---
titel: Golf 1 · de atlas als product — bouwplan
datum: 2026-10-08
status: bouwplan, vastgesteld na drie ontwerpvoorstellen (prestaties-eerst · product-eerst · minimale-ingreep-eerst) en zes kritieken; go/no-go per stap op de bol, telefoontest Lars als poort tussen stap 1 en 2
issue: LAR-490 (M26 · LOD / visuele fase)
bouwt voort op: lod-ontwerpbrief.md (2026-07-19), stroomstijl.js (2026-08-07), het gloed-mechanisme (gloed.js, 2026-08-07)
nulmeting: build-cache/meting/v131-default-rapport.json en v131-atlas-rapport.json (meet_atlas.mjs, 2026-10-08)
---

# Golf 1 · de atlas als product — bouwplan (LAR-490)

*Dit document is zelfstandig leesbaar voor wie de code van `v2/` kent. Het kiest per onderwerp één
oplossing, zegt waarom, en noemt wat is afgewezen en waaraan dat stierf. De tien harde besluiten van
Lars (CLAUDE.md / memory/decisions.md) heten hieronder **H1–H10**; geen daarvan wordt omgedraaid.*

> H1 gemeten routes op de grond, alleen lucht en de drie hemelsbreed-modi boogen · H2 stippel = uitsluitend
> "hier reikt het net niet", zichtbaar gestippeld, zonder draad en kometen · H3 kleur = grondstof in de
> atlas, kleur = modaliteit in het routewerk, `stroomstijl.js` enige stijlbron, onbekende sleutel luid ·
> H4 bakken is geen deliverable, extra velden in een los bestand of een reproduceerbaar afgeleid artefact ·
> H5 gloed additief, pixel-minimum als mechanisme, koepel, alleen sites + stroomknopen, geen voorgekookt
> hotspot-object, capaciteit = gewicht · H6 kometen normaal geblend, bijna-witte kop, staart als fractie van
> het been; draad/komeet/gloed dragen per constructie de lijnkleur · H7 uitgezette lagen achter een vlag,
> AIS-bronvermelding blijft · H8 wat op elke hoogte zichtbaar moet zijn schaalt in schermruimte · H9 fouten
> luid, meet het eindproduct met `meet_atlas.mjs` · H10 vectorlagen op `CONFIG.vectorLift`, renderOrder
> stromen 7,4–7,6 boven landnet 7.

## Waarom

De atlas heeft 182 gemeten ketens over 14 grondstoffen, en niemand kan ze op een telefoon bekijken: de
telefoon-emulatie haalt 9–14 fps op élke kijkstand, 182 stromen laden in 14,1 s, en de pagina opent nog
steeds als het **routewerk** (kleur per transport, felle satelliet, wit spoornet, HUD-titel "Atlas v2 ·
fundament / M28"). De atlasmodus bestaat, maar als knop.

De oorzaak is gemeten en zit niet in de hoeveelheid data maar in de **vorm** waarin die op de bol staat:

- elk van de 182 bestanden wordt **twee keer** gefetcht (`stroomroute.js` en `stroomleven.js` lezen hetzelfde
  json) en twee keer geparsed → 382 verzoeken, 51,7 MB lokaal, en een JS-heap van 365–475 MB die vooral uit
  182 × 2 geparsede documenten plus `b.plat`/`b.cum`-arrays bestaat;
- **één object per been per laag**: 494 `LineSegments` + 225 gestippelde `Line` + 986 `Line2` (twee schillen
  per niet-stippel-been) + 436 `Points` (1.164 in atlasmodus: 182 marker-lagen + 182 × 5 gloedschillen + 14 × 5
  site-schillen) → ~2.300 draw calls (~3.000 in atlasmodus). Op CPU ×4 is dat de hele framebegroting;
- **12,7 miljoen driehoeken**, allemaal uit de Line2-schillen: 1.059.266 segmenten × 2 schillen × 6 driehoeken
  = 12,71 M van de 12,73 M gemeten. De GPU tekent op wereldhoogte 813.000 truckpunten op meters-korrel die
  samen een paar honderd pixels beslaan;
- per frame 182 + 182 + 14 `onTick`-callbacks én `zetResolutie` op 986 `LineMaterial`s (main.js:614–617).

De hefboom is daarom: **één afgeleid bundelbestand met ingebakken LOD**, **een handvol samengevoegde
objecten** waarin aan/uit, kleurmodus en lijnmodus via attributen en een textuur blijven werken, en **de atlas
als default**. Alles wat de visuele taal draagt — kleurtabel, gloed-afstemming, komeetgedrag, de vier lijnmodi,
de stippel-conventie — blijft inhoudelijk ongewijzigd; alleen de implementatie wordt één object per laag.

## De nulmeting (?v=131, 2026-10-08) — de referentie

Gemeten met `v2/tools/meet_atlas.mjs` tegen `http://localhost:8732/v2/?v=131`, headless Chrome 154 via CDP,
cache uit, GPU = RX 7900 XTX (óók in de telefoon-emulatie: CPU ×4, 390 × 844 css-px, DPR 3 → canvas 780 × 1688
want `setPixelRatio` capt op 2).

| | desktop 1600 × 1000 | telefoon-emulatie |
|---|---|---|
| data-verzoeken / bytes (lokaal, ongecomprimeerd) | 382 / 51,7 MB (landnet.bin 9,9 MB; elk stroombestand 2×) | idem |
| pagina-load / alle 182 stromen zichtbaar | 3,96 s / **4,23 s** | 6,19 s / **14,09 s** |
| zichtbare objecten (routewerk) | 2.301 = 494 LineSegments · 225 Line · 986 Line2 · 436 Points · 160 Mesh | 2.213 (72 Mesh) |
| zichtbare objecten (atlasmodus) | 3.029 (1.164 Points) | 2.941 |
| vertices / driehoeken | 5,18 M / **12,73 M** | 5,17 M / 12,72 M |
| draw calls (routewerk · atlas) | 2.238–2.324 · 2.966–3.052 | 2.181–2.227 · 2.909–2.955 |
| fps mediaan wereld · continent · regionaal · lokaal | 79 · 84 · 72 · 69 | **11 · 14 · 9 · 9** (atlas 12 · 12 · 12 · 13) |
| JS-heap | 395–475 MB | 365–407 MB |
| console-fouten / excepties | 0 / 0 | 0 / 0 |

De data erachter (eigen telling over de 182 geregistreerde stromen, 2026-10-08): **718 benen · 225 stippel ·
650 markers · 1.063.700 punten · 1.180.043 km**. Per modaliteit: truck 240 benen / 813.353 punten / 83.231 km ·
spoor 138 / 118.499 / 52.933 · zee 202 / 85.502 / 780.679 · binnenvaart 32 / 23.090 / 4.968 · leiding 68 / 13.483 /
15.310 · lucht 38 / 9.773 / 242.922. Twaalf zeebenen kruisen de datumgrens (lon-sprong > 180°). Veertien
`gloednodes-*.json` met 463 knopen waarvan **451** `level = site`. Het 183e bestand op schijf,
`stroomroute-ree-phaxay-namcan.json`, is **bewust niet geregistreerd** (besluit 2026-09-28: een keten die
volledig uit stippel bestaat wordt niet geregistreerd) — de voorstellen die "719 benen / 226 stippel / 652
markers" of "glob == manifest" als acceptatie namen, telden dat bestand mee en zijn daarop gecorrigeerd.

⚠️ **Live is de baseline kleiner dan lokaal.** GitHub Pages comprimeert óók `.bin`: `curl -I` op 2026-10-08
geeft `landnet.bin` 10,13 MB → **7,48 MB** (`Content-Encoding: gzip`), `stroomroute-pilot.json` 672 KB →
196 KB. De werkelijke transfer van ?v=131 is dus ~14 MB, niet 51,7. `meet_atlas` meet per constructie
ongecomprimeerd op localhost; alle bytebudgetten hieronder zijn daarom **ongecomprimeerd lokaal**, met één
slotmeting tegen de Pages-URL (`--url https://larswalters.github.io/grondstoffen-atlas/v2/`).

## Wat golf 1 oplevert

A. De pagina opent als **atlas**: kleur per grondstof, ondergrond donker, gloed en kometen aan; het routewerk
   blijft volledig bereikbaar als **bouwmodus** (`?modus=bouw` en de bouwsectie in de HUD).
B. 182 stromen laden en renderen vlot op een telefoon: ≤ 5 data-verzoeken en ≈ 0,7 MB voor de eerste weergave,
   ≤ 6 stroomobjecten in de scene, ≤ 0,6 M driehoeken op wereld/continent, ≥ 30 fps in de emulatie, alle
   stromen zichtbaar < 3 s in de emulatie, heap ≤ 200 MB.
C. **Lijnstijl per modaliteit** in de atlasmodus, in schermpixels, zonder de stippel-conventie te breken.
D. Een **HUD die als product leest**: titel, per grondstof aan/uit als hoofdbediening, de bouwknoppen in één
   dichtgeklapte bouwsectie, werkend op 375 px.
E. Het **landnet** is in de atlas niet zichtbaar en niet geladen; in de bouwmodus lui achter zijn knop.

Niet in golf 1 (§13): gloedkoepel kern/halo, stadslichten, labels per zoomband, dikte = volume, aantal kometen
uit volume, een gedimde landnet-variant, de gloedmaat in de vertex-shader, een adaptieve pixelRatio-klep.

## Besluiten (golf 1, 2026-10-08)

1. **De atlas is de default.** `kleurModus = "grondstof"`, belichting `donker` (0,40), `lijnModus = "route"`,
   gloed aan, kometen aan, alle 14 grondstoffen en 182 stromen aan, landnet/AIS-waternet/open ligplaatsen uit
   én niet geladen. `?modus=bouw` opent het routewerk (modaliteit · vol · landnet geladen en aan · witte
   precisiestippen). ⚠️ Dit **vervangt** het besluit van 2026-08-07 ("modaliteitsweergave als default, een
   besluit en geen instelling", memory/decisions.md) op keuze van Lars (2026-10-08); dat hoort in decisions.md
   bijgeschreven, anders staan er twee tegenstrijdige besluiten (de les "vervallen waarschuwingen niet
   meeslepen").
2. **Eén afgeleid bundelartefact uit een baker; de bron blijft de bron.** De 183 `stroomroute-*.json` en de 14
   `gloednodes-*.json` worden niet aangeraakt en niet herbakken (H4). `v2/tools/bak_stroombundel.py` schrijft
   `stromen.json` + `stromen-basis.bin` + 14 × `stromen-fijn-<grondstof>.bin`, deterministisch
   (byte-identiek bij herhaling = de regressietoets, zoals `landnet.bin`). **Het register verhuist naar
   `v2/data/stromen-register.json`** en is de enige bron voor `main.js`, de HUD-generatie én de baker. Een
   glob over `v2/data/` is géén register: het expliciete registratiemoment van 2026-09-28 blijft bestaan, en
   een bestand dat in geen van beide lijsten (`stromen` / `uitgesloten`) staat laat de baker **luid falen**.
3. **Drie geometrie-niveaus: twee gebakken LOD-niveaus voor alle stromen samen, plus de volle resolutie per
   grondstof, lui geladen en resident.** L0 (3 km) en L1 (200 m) staan in één `stromen-basis.bin`; de volle
   geometrie staat per grondstof in een eigen `.bin` die pas wordt gehaald als de kijkhoogte eronder komt en
   die daarna **niet meer wordt weggegooid** (geen LRU — bij Rijnmond, Durban, Beilun of Antwerpen komen meer
   dan drie grondstoffen samen, en alles samen is 3,4 MB). De bandgrenzen volgen uit de canvashoogte en de
   fov (één formule, geen vaste kilometers); de wissel is hard, zonder crossfade, want per constructie ≤ 1
   css-px.
4. **Een handvol objecten voor alle stromen samen**: per LOD-niveau één `LineSegments2` (alle benen van alle
   stromen, stippel inbegrepen), één klein `LineSegments2` voor de 38 luchtbenen (boog, runtime zoals nu),
   één `Points` voor alle kometen, één `Points` voor alle gloedkoepels (sites + stroomknopen), één `Points` voor
   de witte precisiestippen (alleen bouwmodus). Per-stroom aan/uit, kleurmodus en lijnmodus werken via een
   **per-been informatietextuur** (1024 × 1) en per-instantie attributen; er wordt bij een klik niets herbouwd.
5. **De horizon blijft een clipping plane** (`GLOBE.klemOpHorizon`, `depthTest: false`). `LineMaterial` bevat
   de clipping-chunks en `stroomleven.js` bewijst sinds ?v=116 dat dat op `Line2` werkt. Een eigen horizontoets
   in de vertex-shader is een vastgelegde mislukking (globe.js: "heeft me twee rondes gekost en werkte niet",
   2026-07-22) en zou bovendien per segment knippen i.p.v. per fragment — op L0 zijn segmenten tot 100 km.
6. **De lijnafstand voor patronen staat per been in kilometers**, uit de bake (basis) of uit de decode (fijn),
   nooit via `computeLineDistances()` over de hele buffer: alle benen samen zijn 1.180.043 km ≈ 445
   scene-eenheden en de float32-korrel daar is ≈ 80 m, op 14 km hoogte ≈ 6 css-px. Per been (max 22.615 km in
   km-eenheden) is de korrel ≈ 2 m.
7. **Lijnstijl per modaliteit = alfa-patroon langs de lengte in schermpixels + breedte per modaliteit + een
   dwarsprofiel**, gerealiseerd in dezelfde draw via `onBeforeCompile` op `LineMaterial`. Patronen moduleren
   **alleen alfa en breedte, nooit de tint** (×1,35 maakt zilver/pgm/diamant wit, en wit is "onbekend"); de
   breedte varieert **per instantie, nooit langs de lengte** (de ronde eindkappen van `LineMaterial` zouden op
   elke vertex een knobbel op de volle breedte zetten). **Alleen stippel heeft echte gaten** (alfa 0); elk
   modaliteitspatroon houdt alfa ≥ 0,45, zodat gestippeld op geen enkele hoogte iets anders kan betekenen dan
   "hier reikt het net niet" (H2). De tabel `LIJNSTIJL` staat in `stroomstijl.js` en voedt shader-uniforms én
   de HUD-legenda (H3).
8. **Breedtes in css-pixels.** `LineMaterial.resolution` krijgt de css-maat van het canvas
   (`clientWidth/clientHeight`), zodat `linewidth` css-px is. Vandaag staat de draad op 1,7 **device**-px =
   0,85 css-px op een telefoon, dunner dan de 1-px exacte lijn eronder — de levenslaag was daar onzichtbaar.
   Dit is een zichtbare wijziging en staat als constante (`BREEDTE_IN_CSS_PX`), zodat hij in één regel terug kan.
9. **De halo-schil vervalt.** De 3,6 px additieve schil op 0,13 had maar één taak ("de kern lucht geven"); op de
   donkere atlas is het verschil niet te zien en hij kostte de helft van de 12,7 M driehoeken. De lijn geeft geen
   licht; het licht zit in kometen en gloed (de les van 2026-08-07). Screenshot-vergelijk in beide standen.
10. **Het gloed-ontwerp verandert niet, alleen de implementatie**: minPx 34, sterkte 0,30, koepelhoogte 2,6, de
    vijf `SCHILLEN`, de knoopgewicht-heuristiek en de normalisatie per grondstof blijven letterlijk (H5). De vijf
    schillen worden vertex-reeksen in één `Points` (additief is commutatief, dus de tekenvolgorde binnen de
    koepel draagt niets). De per-frame maat blijft in **JS**: gemeten kost de lus over alle knopen < 0,3 ms
    desktop (≈ 1 ms op CPU ×4) — de winst zat nooit in die lus maar in de 1.164 objecten. De camera wordt één
    keer per frame naar groep-lokale ruimte getransformeerd (de BOL draait, globe.js:533; de camera staat vast).
11. **Kometen: één `Points`, K = 2 op desktop en K = 1 op een telefoon** (`innerWidth ≤ 640`, als
    `AFSTEMMING`-constante zodat Lars het terug kan draaien), staart 14 punten, 5,5 % van het been, bijna-witte
    kop, normale blending — ongewijzigd (H6). Nieuw zijn drie skip-regels die het beeld niet raken: een been dat
    uit staat, waarvan de kop achter de horizon ligt, of dat kleiner dan 16 px projecteert, krijgt grootte 0 en
    slaat de baanberekening over. De baan loopt over de **getekende** geometrie (fijn waar fijn getekend wordt,
    anders L1), geparametriseerd in **originele cumulatieve km**, zodat een LOD-wissel geen sprong geeft en de
    komeet op lokale hoogte óp zijn lijn ligt (H6: de lijn zegt waar). In de hemelsbreed-modi loopt hij over
    dezelfde `beenPunten()` als de lijn, zoals nu.
12. **Landnet, AIS-waternet en open ligplaatsen worden lui en zitten alleen in de bouwsectie** (het
    `haalAisTracks()`-patroon). Code, bestanden en de AIS-bronvermelding blijven (H7).
13. **De HUD bedient per grondstof**, en een grondstofschakelaar schakelt **stromen én sites** van die grondstof
    (de legenda zegt dat). De bouwknoppen gaan in één `<details id="bouw">`, dicht op elke breedte. Op mobiel
    staat een horizontaal scrollende chipstrip in de ingeklapte kop, zodat je grondstoffen schakelt zonder de
    bol te bedekken.
14. **Vier leverbare stappen**, elk met push, `?v=`-bump, live-link en meting; **de telefoontest van Lars is de
    poort tussen stap 1 en 2**. De oude modules (`stroomroute.js`, `stroomleven.js`, de `gloednodes`-lus) blijven
    in stap 1–3 bereikbaar via `?laag=los` als pariteitsreferentie en gaan in stap 4 in een eigen commit weg.
15. **Meten blijft `meet_atlas.mjs`**, uitgebreid met `--modus atlas|bouw`, een wachtvoorwaarde op de
    manifest-telling en **pixeltoetsen** waar een telling liegt: een via de textuur verborgen instantie wordt nog
    steeds getekend, dus `renderer.info` beweegt niet bij een toggle — de toets telt pixels in de stroomkleur.
16. **De bundelversie is losgekoppeld van de code-`?v=`** (`BUNDEL_VERSIE`, zoals landnet "102"): bump alleen bij
    een echte bake. Werkregel in de kop van `bak_stromen.sh` en §7 van `bakhandleiding-licht.md`: **elke gebakken
    stroom gaat in dezelfde commit door `bak_stromen.sh bundel`**, en `bak_stroombundel.py --check` (sha1 van alle
    bronnen in `stromen.json`) faalt luid bij drift.

## 1 · Dataformaat

### 1.1 Bron (ongewijzigd)

`v2/data/stroomroute-*.json` (versie-2-contract: `stroom`, `titel`, `routebrief`, `benen[{modaliteit, naam,
stippel?, km, punten[[lon,lat],…], vertakt_van?}]`, `markers[{naam, lon, lat}]`) en `v2/data/gloednodes-*.json`
(`knopen[{level, lon, lat, gewicht, grondstof[], …}]`). Beide blijven de bron van waarheid en blijven op Pages
staan (het `?laag=los`-pad leest ze tot stap 4).

### 1.2 `v2/data/stromen-register.json` — het register (nieuw, met de hand onderhouden)

Het `STROMEN`-blok uit `main.js` (182 regels mét hun commentaarhistorie) verhuist hierheen; `main.js` en
`index.html` dragen geen stroomlijst meer.

```json
{
  "versie": 1,
  "stromen": [
    { "sleutel": "cu-eg", "bestand": "stroomroute-koper-escondida-guixi.json", "grondstof": "koper",
      "label": "Escondida → Guixi", "aan": true,
      "noot": "M28; fase E bestaat niet (2026-08-05)" }
  ],
  "uitgesloten": [
    { "bestand": "stroomroute-ree-phaxay-namcan.json",
      "reden": "volledig stippel — niet geregistreerd (besluit 2026-09-28)" }
  ]
}
```

- `sleutel` = de HUD-sleutel (data-sr), `label` = de handgeschreven knoptekst uit `index.html` (val hij weg, dan
  toont de HUD `titel` uit het json — zichtbaar, niet stil), `noot` = de golf-historie uit de html-commentaren.
- `grondstof` staat expliciet (de HUD groepeert erop en het pilotbestand heet niet naar zijn grondstof — de
  bestaande reden uit main.js:235). De baker **asserteert** `grondstofVan(doc.stroom) == grondstof` (vandaag 0
  afwijkingen over 182) zodat een toekomstige stroom met een afwijkende id-prefix niet stil in bundel X met kleur
  Y belandt. De baker kent verder géén kleur- of stijlsleutels — die blijven uitsluitend in `stroomstijl.js` (H3).

### 1.3 `v2/data/stromen.json` — de index (gegenereerd, ≈ 250 KB ongecomprimeerd, ≈ 60 KB over de lijn)

```json
{
  "formaat": 1, "bakVersie": "132", "gebakken": "2026-10-09T…",
  "bron": { "stroomroute-koper-escondida-guixi.json": "sha1…", "gloednodes-koper.json": "sha1…" },
  "totalen": { "stromen": 182, "benen": 718, "stippel": 225, "markers": 650, "sites": 451,
               "puntenL0": 16470, "puntenL1": 86811, "puntenFijn": 1146817 },
  "niveaus": {
    "L0":   { "tolKm": 3.0, "verdichtKm": 100, "bestand": "stromen-basis.bin", "byteVan": 0,      "byteTot": 70000 },
    "L1":   { "tolKm": 0.2, "verdichtKm": 25,  "bestand": "stromen-basis.bin", "byteVan": 70000,  "byteTot": 450000 },
    "fijn": { "tolKm": 0,   "verdichtKm": 5,   "bestand": "stromen-fijn-<grondstof>.bin" }
  },
  "fijn": { "koper": { "bestand": "stromen-fijn-koper.bin", "bytes": 330000, "punten": 112000 } },
  "stromen": [
    { "sleutel": "cu-eg", "stroom": "koper-escondida-guixi", "titel": "…", "routebrief": "…",
      "kmPerModaliteit": { "leiding": 154.2, "zee": 19104.0, "spoor": 565.8 },
      "benen": [
        { "i": 0, "modaliteit": "leiding", "naam": "slurryleiding Escondida → Coloso", "stippel": true,
          "km": 154.2, "vertaktVan": null,
          "bbox": [[-69.1, -24.3, -68.4, -23.6]],
          "L0": [0, 2], "L1": [0, 2], "fijn": [0, 31] }
      ],
      "markers": [ { "naam": "Escondida (concentrator)", "lon": -69.07, "lat": -24.27 } ] }
  ],
  "sites": [ { "grondstof": "koper", "lon": 117.81, "lat": 30.96, "gewicht": 400, "naam": "金冠铜业" } ]
}
```

- `i` is de **globale beenindex** (0…717) — de sleutel in de informatietextuur en in de instantie-attributen. De
  baker faalt luid boven 1024 benen (dan wordt de textuur 2048; één constante).
- `bbox` is een lijst van 1 of 2 dozen over **alle punten** van het been (twee bij een datumgrens-kruising), niet
  alleen de uiteinden: een zeebeen Antofagasta → Beilun of een spoorbeen Guixi → Tongling loopt dwars door een
  lokaal venster zonder dat een uiteinde in beeld is.
- `L0`/`L1`/`fijn` = `[puntVan, nPunten]` binnen het blok van dat niveau. Luchtbenen hebben `"L0": null, "L1":
  null, "fijn": null` en `"kopStaart": [[lon,lat],[lon,lat]]`: hun geometrie komt niet uit de bin maar uit
  `beenPunten()` (boog, H1), precies zoals nu.
- `sites` zijn de `level = site`-knopen uit de 14 gloedbestanden, gestript tot grondstof/lon/lat/gewicht/naam. De
  normalisatie (`helder = 0,28 + 0,72·√(g/max)` per grondstof) en de straal (`0,30·√g` km) blijven **runtime** in
  `gloednodes.js`; de baker levert gewicht, geen afstemming.
- `kmPerModaliteit` voedt de HUD-noot (km per grondstof) zonder geometrie te lezen.

### 1.4 `stromen-basis.bin` en `stromen-fijn-<grondstof>.bin` — de geometrie

Codering = het `landnet.bin`/`world-10m`-patroon (lezer `maakLezer` uit landnet.js, bewust gekopieerd): zigzag-varint
zonder bitoperatoren, lon/lat gekwantiseerd op **1e-5°** (≈ 1 m), **delta per punt** binnen een been (eerste punt
absoluut t.o.v. 0), **lon ontwikkeld** over de datumgrens (continu > 180° waar nodig; `opBol` rekent met sin/cos en
is periodiek, dus de browser hoeft niets terug te vouwen).

Blokindeling per niveau: voor elk been in `stromen.json`-volgorde (sleutelvolgorde van het register, benen in
reisvolgorde) `[nPunten] [Δlon Δlat …]`, en in **basis.bin per punt bovendien `Δkm`** = de **originele** cumulatieve
kilometerstand vanaf het beenbegin, gekwantiseerd op 10 m (zodat L0 en L1 dezelfde fasering dragen als de volle
lijn — besluit 6 en 11). De fijn-bins dragen géén km-kolom: de browser telt bij het decoderen de 3D-koordelengte op
(één pass hypot over de punten, ≈ 10 ms desktop / ≈ 40 ms op CPU ×4), wat op 100 m-korrel gelijk is aan de
grootcirkel-som.

Gemeten op de 182 geregistreerde stromen (2026-10-08, eigen Douglas-Peucker in lokale equirectangulaire projectie
per been, lon ontwikkeld, uiteinden vast):

| niveau | tolerantie · verdichting | punten | bytes (schatting; de baker rapporteert) |
|---|---|---|---|
| ruw (ter referentie) | — | 1.063.700 | 2,99 MB als lon/lat-varint (2,81 B/punt) |
| L0 wereld | DP 3 km · grootcirkel-verdicht 100 km | **16.470** (DP alleen: 9.904) | ≈ 70 KB |
| L1 regio | DP 200 m · verdicht 25 km | **86.811** (DP alleen: 59.222) | ≈ 380 KB |
| fijn | geen DP · verdicht 5 km (grondbenen, zoals `verdicht()` nu) | **1.146.817** | ≈ 3,4 MB over 14 bins, 53–400 KB per grondstof |

De grootcirkel-verdichting van `stroomroute.js` verhuist naar de bake, per niveau met een koorde-zakking die bij de
hoogte past (L0 100 km → 0,2 km zakking, waar 1 css-px ≥ 2,5 km is · L1 25 km → 12 m · fijn 5 km → 0,5 m, de
bestaande ijking van 2026-07-28). Het fijn-niveau is daarmee **punt voor punt wat de bol vandaag tekent**, op de
1 m-kwantisatie na; dat maakt de pixelregressie in bouwmodus eenduidig. Alleen `ligtOpGrond`-benen worden verdicht
(lucht zit niet in de bins).

⚠️ Pages gzipt de bins (gemeten), maar varint blijft: het is 3,4 MB tegen ~6 MB gegzipte JSON, er is geen
`JSON.parse` en geen tussenliggend object per punt, en wie later "voor de snelheid" Float32 kiest verdrievoudigt de
bytes — vastgelegd hier.

### 1.5 Versiebeleid en werkregel

`BUNDEL_VERSIE` in `main.js` (start "132") is de data-versie van `stromen.json` en alle bins, los van de code-`?v=`.
`stromen-register.json` laadt mee op de **code**-versie (hij verandert met elke registratie). `bak_stromen.sh bundel`
roept de baker aan; de kop van dat script en §7 van `bakhandleiding-licht.md` krijgen de regel dat een gebakken
stroom nooit zonder herbundel wordt gecommit. `bak_stroombundel.py --check` herberekent de sha1's uit `stromen.json`
en geeft exit 1 bij drift — de guard tegen de generator↔uitvoer-klasse (cu-guixi-spoor, 741 m).

## 2 · LOD

### 2.1 Algoritme (bake)

Douglas-Peucker per been, iteratief (stapel, geen recursie), in een **lokale equirectangulaire projectie** (schaal
111,195 km/° in lat en `cos(lat_midden)·111,195` in lon), met **ontwikkelde lon** en **vaste uiteinden**. Daarna
grootcirkel-verdichting tot de maximale segmentlengte van het niveau. Een marker blijft ≤ tolerantie van de
vereenvoudigde lijn — dus ≤ 1 css-px op de hoogte waar dat niveau getekend wordt; de anker≠routeerpunt-metingen gaan
over de bron-json's en die veranderen niet. Visvalingam niet: DP zit al in de keten (`bake_landnet.py`) en de
2D-afwijking is wat op het scherm telt. De baker toetst per been dat elk gekozen punt een bronpunt is (geen
coördinaat verzonnen) en dat de km-som van het fijn-niveau binnen 0,1 % van de bron-`km` ligt, en faalt luid bij
een segment > 2× de verdichtingsmaat (de datumgrens-val).

### 2.2 Wanneer welk niveau (browser)

Eén gedeelde keuze per frame in `stroombundel.js`, uit de kijkhoogte `h` (`GLOBE.getAltitudeKm()`), de fov (42°) en
de **css-hoogte** `H` van het canvas:

```
kmPerCssPx = 2 · h · tan(21°) / H = 0,7673 · h / H
L0 toelaatbaar zolang 3,0 km ≤ 1,0 css-px   →  h ≥ 3,91 · H  (H 844: 3.300 km · H 1000: 3.910 km)
L1 toelaatbaar zolang 0,2 km ≤ 1,0 css-px   →  h ≥ 0,261 · H (H 844:   220 km · H 1000:   261 km)
hysterese 20 % (terug naar het grovere niveau pas boven 1,2 × de grens)
fijne bundels prefetchen zodra h < 1,5 × de L1/fijn-grens voor elke grondstof met een been in de zichtkap
```

Op de vier kijkstanden: wereld 9.000 km → L0 (3 km = 0,37 css-px op een telefoon) · continent 3.500 km → telefoon L0
(0,94 px), desktop L1 · regionaal 300 km → L1 (0,73 / 0,87 px) · lokaal 14 km → fijn. De grenzen worden dus nooit
als kilometers in de code gezet — de kritiek dat "2.500/300/30 km" op een telefoon van 1688 device-px zichtbaar
wisselen is zo structureel weg.

### 2.3 Overgang

Harde `visible`-wissel tussen het L0- en het L1-object (zelfde materiaal, zelfde textuur); geen crossfade, want op de
grens is het verschil ≤ 1 css-px en de hysterese voorkomt flikkeren. Het fijn-niveau komt asynchroon: tot de bundel
binnen is blijft L1 staan voor die benen (geen gat). Koorde-zakking kan het 2026-07-28-probleem ("ik zie geen
leiding") niet terugbrengen: `depthTest` staat uit, de zakking per niveau is ≪ de kijkhoogte van dat niveau, en de
horizon-clip speelt pas als de zakking de kijkhoogte nadert.

### 2.4 Het fijn-niveau: één object, gebouwd uit de benen in beeld

Het fijn-object is één `LineSegments2` met een **vooraf gealloceerde** instantiebuffer van `FIJN_MAX = 200.000`
segmenten (4,8 MB posities + 1,6 MB attributen) en `instanceCount` = gebruikt. Elke 250 ms (niet per frame) toetst
`stroombundel.js` de `bbox` van alle 718 benen tegen het zichtvenster (hoekstraal uit de hoogte, 15 % marge); is de
set benen-in-beeld veranderd of is er een bundel binnengekomen, dan worden de segmenten van de benen in beeld
waarvan de bundel resident is **in-place** in de buffer gekopieerd (typed-array `set` van per been bij de decode
klaargezette start/eind-paren; geen allocatie), `needsUpdate` met `addUpdateRange`, en krijgen die benen bit FIJN
in de textuur (§3.2) — het L1-object laat ze dan weg, het fijn-object tekent ze. Past de set niet in `FIJN_MAX`
(bij < 260 km hoogte is het venster hooguit ~200 × 100 km, dus hooguit enkele tienduizenden segmenten), dan blijven
de overige benen op L1 en meldt de console dat **luid** (H9). Zo tekent nooit iets dubbel, is er nooit een object
per stroom, en blijft het driehoekenaantal op lokaal begrensd op 1,2 M in plaats van de 6,9 M die "alle fijne
bundels zichtbaar" zou kosten.

Lijnmodus `route` = {L-actief, fijn, lucht}. De drie hemelsbreed-modi hebben geen LOD nodig: `beenPunten()` geeft
48–512 punten per been (≈ 60–70 k totaal), lui gebouwd als één `LineSegments2` per modus bij de eerste omschakeling,
met dezelfde textuur en hetzelfde materiaal; stippelbenen houden hun stijl, lucht houdt zijn boog (H1 — de vier
modi en hun lift-gedrag per been blijven exact zoals in ?v=117 gemeten).

## 3 · De scene: van 2.300 objecten naar een handvol

### 3.1 Objecten (alles aan, atlasmodus)

| object | aantal | renderOrder | inhoud |
|---|---|---|---|
| `lijnen-L0`, `lijnen-L1` | 2 (1 zichtbaar) | 7,5 | alle 680 niet-lucht-benen van alle stromen, stippel inbegrepen; `LineSegments2` + `StroomLijnMateriaal` |
| `lijnen-fijn` | 1 | 7,5 | benen in beeld op volle resolutie (§2.4) |
| `lijnen-lucht` | 1 | 7,5 | 38 luchtbenen als boog uit `beenPunten()`, ≈ 5–6 k segmenten, in elke lijnmodus |
| `lijnen-<hemelsbreed>` | 0–3, lui | 7,5 | alleen in die lijnmodus zichtbaar |
| `kometen` | 1 | 7,55 | 493 dragers × K × 15 punten, één `Points` |
| `gloed` | 1 | 7,6 | 451 sites + 650 stroomknopen = 1.101 knopen × 5 schillen = 5.505 vertices, additief |
| `precisiestippen` | 1 | 7,6 | 650 markers, alleen bouwmodus (dan is de stroomknoop-gloed uit — "precies één van de twee") |

Telling met alles aan: telefoon ≈ 72–108 tegels + ~5 (bol, atmosfeer, sterren) + ≤ 6 stroomobjecten ≈ **85–120**;
desktop continent ≈ 204 tegels + ~12 ≈ **215–230**. De tegels zijn na deze golf de grootste post en vallen bewust
buiten scope (budget 96, `tiles.js` onaangeraakt).

Driehoeken: L0 16.470 segmenten × 6 ≈ **0,10 M**; L1 86.811 × 6 ≈ **0,52 M**; fijn ≤ 200.000 × 6 = 1,2 M (verwacht
0,1–0,4 M); lucht ≈ 0,03 M; tegels ≈ 0,02 M. Tegen 12,7 M nu.

### 3.2 De informatietexturen — aan/uit, stijl en kleur zonder een object per stroom

Twee `DataTexture`s van 1024 × 1, `NearestFilter`, geen mipmaps, gedeeld door lijnen, kometen (en gelezen door de
HUD-telling):

- **`beenInfo`** (RGBA8), index = globale beenindex `i`:
  `R` = vlaggen (bit 0 **AAN** uit de HUD; bit 1 **FIJN** = het fijn-object tekent dit been nu) ·
  `G` = **stijl** (0 zee · 1 binnenvaart · 2 truck · 3 spoor · 4 leiding · 5 lucht · 6 onbekend · 7 stippel) —
  door de **browser** gezet bij het laden uit `stroomstijl.MODALITEITEN.indexOf(modaliteit)` en `been.stippel`;
  een onbekende modaliteit wordt stijl 6 (magenta, 3/3) én een `console.warn` via `meld()` (H3/H9). De baker kent
  dus geen stijlindex · `B` = breedtefactor × 100 (100 = 1,0; de haak voor dikte = volume uit het metadatabestand,
  golf 2) · `A` = ongebruikt.
- **`beenKleur`** (RGBA, `FloatType`), index `i`: de lijnkleur in lineaire rgb uit `THREE.Color.setHex(kleurVan(
  modaliteit, stroom, kleurModus))`. **Kleurmodus wisselen = 718 texels herschrijven**, één upload van 16 KB; geen
  kleurbuffer per segment (dus ook `USE_COLOR` uit en 24 B per segment minder).

Elk object heeft een uniform `lodRol`: 0 = basis (tekent AAN && !FIJN), 1 = fijn (AAN && FIJN), 2 = lucht en
hemelsbreed (AAN). De vertex-shader degenereert een verborgen instantie (alle acht vertices naar `clip =
vec4(2,2,2,1)`, buiten de clipruimte — niets wordt gerasterd). Kosten van een klik: `.srBtn` zet bit 0 voor de
benen van die stroom, `.gsChip` voor alle benen van de grondstof, één 4 KB-upload. De HUD-telling en
`toonStroomNoot()` lezen de vlaggen (via `ATLAS.isAan(sleutel)`), niet `groep.visible`.

Kometen hebben per vertex een `been`-attribuut en lezen dezelfde twee texturen (uit → grootte 0; kleur = texel met de
witte menging van de kop, `w = (1 − u)·0,75`, zoals nu). De gloed heeft een `aan`-attribuut per vertex (5.505 floats,
herschreven bij een klik) en een `kleur`-attribuut dat `zetKleurModus` herschrijft uit `GRONDSTOF_KLEUR`; sites
blijven in beide modi zichtbaar (zoals `gloednodes.js` nu), stroomknopen alleen in de atlasmodus. Draad, komeet en
gloed dragen zo per constructie de lijnkleur op het moment van omschakelen (H6).

### 3.3 Het lijnmateriaal (`v2/src/stroomlijn.js`)

Eén klasse `StroomLijnMateriaal extends LineMaterial` (r185, gepind in de importmap), `transparent`, `depthWrite
false`, `toneMapped false`, `klemOpHorizon()` erop (besluit 5), `worldUnits false`, `dashed false` (het `USE_DASH`-pad
discardt de eindkappen en kent alleen één `dashScale`; wij doen het patroon zelf), `customProgramCacheKey()`
overschreven met een eigen sleutel (in r185 is de default `this.onBeforeCompile.toString()`, waardoor materialen met
dezelfde functietekst stil één programma delen — hier is er maar één materiaal, maar de val staat opgeschreven).
Per-instantie attributen op de `LineSegmentsGeometry`: `instanceBeen` (float), `instanceAfstandStart/End` (km vanaf
beenbegin, float32). De `onBeforeCompile`-patches hangen aan **vier letterlijke ankers** in de r185-GLSL, en
`stroomlijn.js` asserteert bij het laden dat elk anker precies één keer voorkomt (anders `throw` — luid, niet stil):

| anker (r185) | patch |
|---|---|
| vertex `#include <clipping_planes_pars_vertex>` | declaraties: attributen, `uniform sampler2D beenInfo, beenKleur`, `uniform float perEenheidCss, kmNaarEenheid, lodRol`, `uniform vec4 patroon[8]`, varyings `vAfstandPx, vStijl, vKleur, vDwars` |
| vertex `vUv = uv;` (de niet-`WORLD_UNITS`-tak) | texel-fetch op `(instanceBeen + 0.5) / 1024`; zichtbaarheid uit `lodRol` + vlaggen; `vStijl`, `vKleur`; `float D = max(1e-6, -((position.y < 0.5) ? start : end).z); vAfstandPx = afstandKm · kmNaarEenheid · perEenheidCss / D` (perspectief-gecorrigeerd per vertex, dus het patroon is in het hele beeld pixelconstant op de verkorting langs de lijn na) |
| vertex `offset *= linewidth;` | `offset *= linewidth * patroon[stijl].breedte * breedtefactor;` |
| vertex `gl_Position = clip;` | `if (verborgen) clip = vec4(2.0, 2.0, 2.0, 1.0);` |
| fragment `#include <clipping_planes_fragment>` (blijft staan) | `float pa = patroonAlfa(vAfstandPx, vStijl); if (pa <= 0.0) discard; alpha *= pa * dwarsAlfa(vUv.x, vStijl); diffuseColor.rgb = vKleur;` |

`vUv.x` ∈ [−1, 1] is de dwarscoördinaat (de eindkap-code van r185 gebruikt hem zo), dus het dwarsprofiel geldt ook in
de kappen en kan geen rand-artefact geven. `perEenheidCss = H_css / (2·tan 21°)`, `kmNaarEenheid = radius / 6371`.
`resolution` krijgt de css-maat (besluit 8) en wordt alleen bij een resize gezet (`ResizeObserver`), niet elke tick.

### 3.4 Bediening

- **Per stroom / per grondstof aan-uit**: textuur-bit (§3.2) + gloed-`aan`. Geen rebuild, geen dispose, draw calls
  gelijk.
- **Kleurmodus**: `beenKleur` herschrijven uit `kleurVan` (de enige bron, waarschuwt luid), gloed-`kleur`
  herschrijven, precisiestippen ↔ stroomknoop-gloed wisselen, belichting mee (vol ↔ donker) met zichtbaar
  meespringende knoppen zoals nu, en in bouwmodus staan de modaliteitspatronen **uit** (effen op modaliteitsbreedte,
  stippel wél in pixels — zie §4).
- **Lijnmodus**: `route` toont {L-actief, fijn, lucht}; de drie andere tonen hun eigen object (lui gebouwd) + lucht;
  kometenbanen worden herrekend over dezelfde punten (zoals `stroomleven.js` nu).
- **Gloed aan/uit** (`.gnBtn`) en **beweging aan/uit** (nieuw, kometen-`Points.visible`).

## 4 · Lijnstijl per modaliteit (deliverable C)

Kleur = grondstof, dus de modaliteit moet in de **vorm**, in **schermpixels** (H8), zonder H2 te breken. Eén tabel
`LIJNSTIJL` in `stroomstijl.js` (naast `GRONDSTOF_KLEUR`/`MODALITEIT_KLEUR`; dezelfde `meld()` bij een onbekende
sleutel) voedt de shader-uniform `patroon[8]` én de legenda-SVG in de HUD, zodat legenda en beeld niet uit elkaar
kunnen lopen. Alle maten in css-px.

| stijl | breedte | lengtepatroon (periode: alfa-profiel) | dwarsprofiel | leest als |
|---|---|---|---|---|
| zee | 1,8 | effen (alfa 1,0) | vol | de drager van de atlas (66 % van alle km), de rustigste lijn |
| binnenvaart | 1,3 | effen | vol | smaller water |
| truck | 2,0 | effen | kern 1,2 px alfa 1,0 · rand alfa 0,45 ("berm") | weg met casing; iets zwaarder dan zee, past bij corridors en last mile |
| spoor | 1,6 | periode 8 px: 6 px alfa 1,0 · 2 px alfa 0,45 ("bielzen") | vol | geribbelde draad op wereldhoogte, spoorlijn op regionaal |
| leiding | 1,6 | periode 12 px: 9 px alfa 0,6 · 3 px alfa 1,0 ("pulsen") | vol | een gepompte, gesegmenteerde stroom; nergens een gat |
| lucht | 1,0 | effen | vol | dun, plus de boog die er al is (20,6 % van de km in 38 rechte lijnen — tweede plan) |
| onbekend (6) | 1,6 | periode 6 px: 3 vol · 3 **uit** in magenta | vol | luid, nooit stil (H9) |
| **stippel (7)** | 1,1 | periode 8 px: **3 px aan · 5 px uit** (alfa 0) | vol | **"hier reikt het net niet"**, op de breedte van geen enkele modaliteit, alfa 0,85 |

Regels die dit bij elkaar houden:

- **Alleen stippel heeft gaten.** Elk modaliteitspatroon houdt alfa ≥ 0,45, dus op geen enkele hoogte kan een
  spoor- of leidingdraad "gestippeld" ogen. Stippel overschrijft het modaliteitspatroon volledig; de modaliteit van
  een stippelbeen blijft kenbaar aan de kleur in bouwmodus en aan de beennaam. Stippelbenen krijgen geen kometen
  (dragers = `!stippel`, zoals nu) en er is geen halo meer voor wie dan ook (H2).
- **Patronen moduleren alfa, nooit de tint, en de breedte nooit langs de lengte** (besluit 7). Bekende bijwerking,
  bewust geaccepteerd en in de screenshots te zien: waar twee segmenten elkaar bij een vertex overlappen tellen hun
  eindkappen op (1 − (1 − a)²); bij alfa 0,45 is dat 0,70 over hooguit 2 px, en op L0 liggen vertices ~12 px uit
  elkaar. Daarom staat de basis-alfa van elke modaliteit op 1,0 (ook lucht — 1,0 px dun is al het tweede plan; op
  0,7 zou een boog van 512 punten een kralensnoer worden).
- **De stippel is vandaag onleesbaar, en dat wordt gerepareerd.** `LineDashedMaterial` dasht nu in wereldeenheden
  (dash 0,00008 ≈ 0,21 km, gap 0,13 km); op 9.000 km is 1 css-px 8,2 km, dus de stippel rendert daar als een vlakke
  lijn — de conventie bestond op wereldhoogte feitelijk niet. Met 3/5 px is hij op elke hoogte gestippeld. Toets:
  de continent-screenshot toont ≥ 3 losse streepjes op de Escondida-slurrystippel (nu 0).
- **Bouwmodus (kleur = modaliteit)**: patronen uit, effen op de modaliteitsbreedte, stippel in pixels. ⚠️ Dit is
  **niet** "het routewerk exact zoals het was": drie dingen veranderen bewust — de stippel staat in pixels, de
  3,6 px-halo is weg, de breedte staat in css-px. Alle drie worden met de ?laag=los-vergelijking gemeten (§11.12)
  en niet als "exact" verkocht.
- **Legenda**: zeven inline-SVG-staaltjes (60 × 10 px) die uit `LIJNSTIJL` worden gegenereerd in `main.js` — niet
  met de hand getekend.

Dikte = volume (de brief) komt niet in golf 1: er is geen volume per been. Kanaal `B` van `beenInfo` staat klaar als
breedtefactor, zodat het losse metadatabestand hem later vult zonder shaderwijziging en zonder herbake (H4).

## 5 · Per frame

Wat blijft is wat beweegt; al het geometrische werk is gebakken of eenmalig bij het laden/decoderen.

- **LOD-keuze**: één vergelijking op `getAltitudeKm()` per frame; elke 250 ms de zichtkap-toets over 718 bboxen
  (JS, < 0,2 ms) en alleen bij een wijziging een fijn-rebuild (§2.4).
- **Kometen**: één `update(dt)` i.p.v. 182. JS doet de baanparameter (binaire zoektocht op de km-array van de
  getekende geometrie) en de grootte/alfa per punt zoals nu; de camera wordt één keer per frame naar groep-lokaal
  getransformeerd (één inverse matrix) voor horizon- en afstandstoets. Skip-regels (besluit 11) halen op wereldhoogte
  ruim de helft van de 493 dragers uit de lus. Budget ≤ 2 ms op CPU ×4 (nu ≈ 1,1 ms voor de lus zelf, de rest zat in
  182 callbacks en objecten).
- **Gloed**: één lus over 5.505 vertices (nu 1.164 objecten × hun eigen lus en upload): `max(minPx·breedte,
  2·straal·perEenheid/afstand·breedte)` en de horizontoets `dot(p̂, ĉ) < R/d → 0`, letterlijk de huidige formule,
  camera in groep-lokale ruimte. Eén `needsUpdate` op één attribuut.
- **Precisiestippen**: idem, 650 punten, alleen bouwmodus.
- **Lijnen**: géén per-frame JS. `resolution` op resize; `perEenheidCss` idem.
- **Tegels**: ongewijzigd en na deze golf de dominante kostenpost.

Fill-rate meet de emulatie niet (RX 7900 XTX): 5.505 additieve gloedsprites van ≥ 34 device-px zijn op een telefoon
~2× schermvulling, plus de Line2-quads. Dat is de reden dat de telefoontest van Lars de poort tussen stap 1 en 2 is
en dat `meet_atlas` optioneel een vijfde profiel krijgt via `adb forward tcp:9333 localabstract:chrome_devtools_remote`
(Chrome op de Honor spreekt hetzelfde CDP). Een adaptieve pixelRatio-klep wordt pas overwogen als die meting onder de
30 blijft (§13).

## 6 · Defaults en HUD (deliverable D)

### 6.1 Defaults

`kleurModus "grondstof"` · belichting `donker` (0,40) · `lijnModus "route"` · gloed aan · kometen aan (K 2/1) ·
satelliet aan · landnet **uit en niet geladen** · AIS-waternet uit en niet geladen · open ligplaatsen uit en niet
geladen (de `ankerLijst` wordt gevuld bij het eerste openen van zijn `<details>`) · alle 14 grondstoffen en 182
stromen aan. De `is-on`-klassen in `index.html` schuiven mee (skBtn grondstof, sdBtn donker, lnBtn uit), zodat knop
en stand niet uit elkaar lopen.

Alles aan, geen curated set: de productclaim ís "182 gemeten ketens", en met L0 (16 k punten), dunne lucht en de
komeet-skips blijft de wereldhoogte leesbaar — gloed voorop, draden daarachter. Vindt Lars het na de screenshots te
druk, dan is "batterijketen aan, rest uit" één regel in het register (`aan: false`).

URL-parameters: `?modus=bouw` (modaliteit · vol · landnet laden en aan · precisiestippen · bouwsectie open) voor Lars
en voor `meet_atlas --modus bouw`; `?laag=los` (stap 1–3) laadt de oude per-stroom-modules als pariteitsreferentie.

### 6.2 Indeling (van boven naar beneden)

1. **Kop**: "Grondstoffen Atlas" · ondertitel dynamisch uit het register: "182 stromen · 14 grondstoffen · kleur =
   grondstof, lijn = transport" · ▾ klapt in.
2. **Grondstoffen (hoofdbediening)**: veertien rijen `[kleurbol] naam  aan/geladen [▸]`, gegenereerd uit het
   register (`GRONDSTOF_KLEUR` voor de bol). Tik op de rij (`.gsChip`, ≥ 36 px) = alle stromen **én sites** van die
   grondstof aan/uit; ▸ opent de bestaande `<details class="srGroep" data-gs>` met één `.srBtn` per stroom
   (`label` uit het register), op alle breedtes dichtgeklapt bij start (182 knoppen zijn een bouwgereedschap).
   Bovenaan "alles aan · alles uit". ⚠️ De klassen `.srGroep`/`.srBtn`/`.gsBtn`/`.gsTel`/`.gsBol` blijven bestaan
   (meet_atlas en `werkGroepenBij` hangen eraan); de chips zijn een laag erboven.
3. **Legenda**: "kleur = grondstof · lijn = transport · gloed = site of overslag · komeet = beweging" + de zeven
   SVG-staaltjes uit `LIJNSTIJL` + "gestippeld = hier reikt het net niet".
4. **Vliegknoppen**: wereld · Tongling · Guixi · Rijnmond (ze dienen het product).
5. **`<details id="bouw">` "Bouwmodus · routewerk"**, dicht op elke breedte, in deze volgorde: kleur per transport ↔
   per grondstof (`.skBtn`, met de modaliteitslegenda; zet belichting mee en biedt het landnet aan) · lijnen (de
   vier `.slBtn`) · ondergrond (satelliet/kaart/egaal + vol/gedimd/donker) · spoornet (`.lnBtn`, lui: eerste "aan"
   haalt 10 MB, noot "laden… (10 MB, eenmalig)"; plus een opt-in "gedimd" 0,30 via één `zetDim`-helper) · AIS-waternet
   (`.anBtn`, lui) · open ligplaatsen (`.akBtn`, lui, lijst bij openen) · gloed aan/uit (`.gnBtn`) · beweging
   aan/uit (nieuw) · beeldverwerking (`.tmBtn`) · belichting (`.sunBtn`) · `#stats`.
6. **Bronnen** (altijd zichtbaar, klein, buiten de bouwsectie): de tegel-attributie (`#attrib`) en `#tracksBronnen`
   met de vijf AIS-archieven en de AMSA-regel voluit — de licentie-eis hangt aan de gepubliceerde data (H7).

Weg uit `index.html`: de 182 handgeschreven `.srBtn`'s en 14 groepen (gegenereerd; commentaren → `noot`), de titel
"Atlas v2 · fundament / M28", de dubbele legendablokken (`#stroomLegenda`/`#stroomLegendaGrondstof` worden één
legenda die met de kleurmodus van inhoud wisselt). 40 KB → ≈ 12 KB.

### 6.3 Mobiel (≤ 640 px, getest op 375 px)

Paneel start ingeklapt (al zo), maar de ingeklapte kop krijgt een **horizontaal scrollende chipstrip** (44 px hoog)
met de veertien grondstofchips — tik = aan/uit, chip gedimd als uit — zodat de hoofdbediening bereikbaar is zonder
de bol te bedekken. Uitgeklapt: breedte `calc(100vw − 20px)`, `max-height 60vh`, scroll binnen het paneel;
tap-targets ≥ 36 px; stroomlijsten en bouwsectie dicht; geen `hidden sm:`-constructies; `#stats` verborgen (al zo).
Toets: `document.documentElement.scrollWidth === innerWidth` op 375 px in `meet_atlas`.

## 7 · Het landnet (antwoord op E)

**In de atlasmodus niet zichtbaar en niet geladen; in de bouwmodus beschikbaar achter zijn knop en pas bij de
eerste "aan" (of bij `?modus=bouw`) opgehaald** — exact het `haalAisTracks()`-patroon met één promise en een
noot; `landnet.js`, `landnet.bin` (bake "102") en de knop blijven (H7). Redenen:

1. Het is ook gecomprimeerd de grootste enkele post (7,48 MB over de lijn, 10,13 MB op schijf, 587–975 ms puur
   netwerk, ~2,4 M vertices per frame) — twee keer de hele stromenbundel op volle resolutie, voor een laag die in
   de atlas geen grondstof is.
2. Inhoudelijk is het spoornet routeer-gereedschap ("ligt het spoorbeen op het net?"); in de atlas tekenen de 138
   spoorbenen zelf waar spoor telt. `LANDNET` heeft in `main.js` geen runtime-afnemer behalve weergave en de
   plank-lift (regels 109–134, 753–756); `keten.js` wordt niet geïmporteerd — lui laden breekt niets.
3. Op de donkere bol leest het cyaan/witte net als een vijftiende grondstof die niet in de legenda staat (zie de
   atlas-continent-screenshot: Europa is één turquoise web waar de stromen in verdrinken), vlak bij lithium-paars en
   gas-cyaan. De "aderen"-rol die het op de gedimde bol half vervulde (CLAUDE.md, ?v=119) is een stadslichten-vraag
   en hoort in golf 2.

Als Lars de bol zonder spoornet vóór golf 2 te leeg vindt, is het goedkope tussenpad een door `bak_stroombundel.py`
afgeleide `landnet-L0.bin` (DP 2 km, geschat 0,5–1 MB, opacity 0,2, één draw call) — bewust pas na de screenshots
van stap 1 beslist, niet nu gebouwd. Regressie in bouwmodus: na "aan" identieke `stats` (netwerkKm, knopen, edges,
punten) en renderOrder 7 onder de stromen.

## 8 · Bestanden

| pad | wat |
|---|---|
| `v2/tools/bak_stroombundel.py` | NIEUW. Leest `stromen-register.json` + alle `stroomroute-*.json` + `gloednodes-*.json`; schrijft `stromen.json`, `stromen-basis.bin` (L0 3 km/100 km + L1 200 m/25 km, mét km-kolom), `stromen-fijn-<grondstof>.bin` × 14 (verdicht 5 km). Lon-ontwikkeling, DP in lokale equirect met vaste uiteinden, bbox per been (1–2 dozen), sha1 van alle bronnen. `--check` (drift → exit 1), `--toets` (tellingen, km-som ≤ 0,1 %, segment ≤ 2× verdichting, ≤ 1024 benen, `grondstofVan == register.grondstof`, geen bestand buiten `stromen`/`uitgesloten`). Byte-identiek bij herhaling. |
| `v2/data/stromen-register.json` | NIEUW, met de hand. 182 `stromen` + `uitgesloten`; enige bron voor main.js, HUD en baker. |
| `v2/data/stromen.json` · `stromen-basis.bin` · `stromen-fijn-<gs>.bin` ×14 | NIEUW, gegenereerd (H4), eigen `BUNDEL_VERSIE`. |
| `v2/src/stroombundel.js` | NIEUW, vervangt `stroomroute.js` + `stroomleven.js` + de `gloednodes`-lus. Laadt register + index + basis (één `Promise.all`), decodeert varint naar typed arrays, bouwt de objecten uit §3.1, LOD-keuze met hysterese, fijn-rebuild uit benen in beeld, luie fijne bundels (resident), hemelsbreed-objecten lui, kleurmodus = textuur. API: `zetStroom(sleutel, aan)`, `zetGrondstof(gs, aan)`, `isAan(sleutel)`, `zetKleurModus`, `zetLijnModus`, `zetBeweging`, `update(dt)`, `stats` (`window.ATLAS`). |
| `v2/src/stroomlijn.js` | NIEUW. `StroomLijnMateriaal` (onBeforeCompile-patches op vier ankers met assert, `customProgramCacheKey`), de twee `DataTexture`s en hun schrijvers. |
| `v2/src/stroomkometen.js` | NIEUW (uit `stroomleven.js` gelicht). Eén `Points`; `KM_PER_DAG`, `AFSTEMMING` (K per apparaat), skip-regels, baan op getekende geometrie in originele km. |
| `v2/src/gloed.js` | WIJZIGING. `bouwGloed` legt de 5 schillen in één `Points` (5n vertices, attributen `breedte`, `helder`, `kleur`, `aan`); `zetAan(bereik)`, `zetKleur(bereik, hex)`; horizontoets in groep-lokale ruimte. `AFSTEMMING`, `SCHILLEN`, shader ongewijzigd. |
| `v2/src/gloednodes.js` | WIJZIGING. Leest `sites` uit `stromen.json` (geen eigen fetch); normalisatie per grondstof blijft; levert knopen aan de gedeelde gloed. |
| `v2/src/stroomstijl.js` | WIJZIGING. `MODALITEITEN` (vaste volgorde) + `LIJNSTIJL` (tabel §4) + `meld()` voor onbekende stijl; kleurtabellen ongewijzigd. |
| `v2/src/main.js` | WIJZIGING. Register uit json; defaults atlas; `?modus=bouw`/`?laag=los`; HUD-generatie; landnet/aisnet/ankercheck lui; één `onTick` voor de stromenlaag; `BUNDEL_VERSIE`; `TOON`-vlaggen en AIS-code onaangeraakt. |
| `v2/index.html` · `v2/style.css` | WIJZIGING. Nieuwe HUD-structuur (§6), chipstrip, bouw-details, legenda-container; `?v=132`. |
| `v2/src/landnet.js` | WIJZIGING (klein). `zetDim(opacity)` op het bestaande materiaal. |
| `v2/tools/bak_stromen.sh` · `v2/design/bakhandleiding-licht.md` | WIJZIGING. Subcommando `bundel`; werkregel "bundel in dezelfde commit" + `--check` in de keuring (§7 handleiding). |
| `v2/tools/meet_atlas.mjs` | WIJZIGING. `--modus atlas\|bouw`; wachten op `window.ATLAS.stats.geladen === stats.stromen`; pixeltoets per stroom en per kleurwissel; stippel-streepjestelling op een vast venster; LOD-grens-screenshots (0,9× en 1,1×); 375 px-profiel met `scrollWidth`; `--url` naar Pages als slotmeting. Bestaande metrieken blijven. |
| `memory/decisions.md` · `CLAUDE.md` | WIJZIGING. Default-besluit van 2026-08-07 vervangen door besluit 1 (met datum en reden). |
| `v2/src/stroomroute.js` · `v2/src/stroomleven.js` | BLIJVEN in stap 1–3 achter `?laag=los`; VERWIJDERD in stap 4 in een eigen commit (git-historie bewaart ze). Geen laag verdwijnt, alleen de implementatie. |

## 9 · Afgewezen alternatieven en hun doodsoorzaak

| alternatief | doodsoorzaak |
|---|---|
| Horizontoets in de vertex-shader i.p.v. clippingPlanes (prestaties-voorstel) | Vastgelegde mislukking (globe.js, 2026-07-22, twee rondes); knipt per segment i.p.v. per fragment → rafelige limb op L0-segmenten van 100 km; clippingPlanes werken al op `LineMaterial` (?v=116). |
| `computeLineDistances()` over de hele buffer voor pixel-dashes | Cumulatief over alle instanties: 445 scene-eenheden → float32-korrel ≈ 80 m ≈ 6 css-px op 14 km; faalt precies op de kijkstand waar de toets zit. |
| LRU van 3 resident fijne bundels + endpoint-bbox | Knooppunten met > 3 grondstoffen zouden hoekig op L1 staan naast scherpe buren (200 m ≈ 15 px op 14 km); een endpoint-bbox mist elk lang been dwars door het venster. Alles samen is 3,4 MB → resident, bbox over alle punten. |
| Alle fijne bundels als zichtbare objecten | 1,15 M segmenten × 6 = 6,9 M driehoeken en 9 M vertex-invocaties per frame op lokaal — de GPU-last van vandaag terug via de achterdeur. Daarom één fijn-object uit de benen in beeld. |
| Zichtbaarheidstextuur 256 breed, stromen 0..181 + grondstoffen 200..213 | 18 vrije sleuven bij golven van 10–37 ketens; bij stroom #201 zet een grondstofchip stil een stroom uit. Nu 1024 per **been**, baker faalt luid bij overloop. |
| Eén gedeelde byte voor "aan" over basis- én fijn-object | Eén byte kan niet "uit in regio, aan in fijn" uitdrukken → dubbel tekenen. Bitvlaggen + `lodRol`-uniform. |
| Glob over `v2/data/` als register (product-voorstel) | Haalt het bewuste registratiemoment weg en telt `ree-phaxay-namcan` mee tegen het besluit van 2026-09-28; "glob == manifest == 182" kan nooit kloppen (glob = 183). |
| Register via regex uit `main.js` (minimale-ingreep-voorstel) | Broos bij een herschrijving en met een hard-coded 182 dat elke golf moet meebewegen; json + telling uit het register zelf. |
| Grondstof-veld en stijlindex in de baker (Python-kopie van `stroomstijl.js`) | Tweede kopie van legenda-sleutels in een andere taal — de drift die cu-guixi-spoor al kostte. De baker schrijft strings en asserteert alleen `grondstofVan == register`; de browser zet stijl en kleur. |
| Patronen met tintmodulatie (kleur × 1,35 "lichtstreep", kleur × 0,55 "kader") | Zilver/pgm/diamant worden exact wit = de "onbekend"-kleur; "getekende kleur = legenda-kleur" per pixel sneuvelt. Alleen alfa. |
| Breedtemodulatie langs de lengte (parelsnoer, ladder) | De ronde eindkappen van `LineMaterial` tekenen op elke vertex een knobbel op de volle quad-breedte, los van het patroon. Breedte alleen per instantie. |
| `LineMaterial.dashed` + één `dashScale`-uniform per frame (minimale-ingreep-voorstel) | Alleen in het beeldmidden pixelconstant (centrum→limb ×1,5–2,2); `USE_DASH` discardt de eindkappen. Eigen patroon met per-vertex perspectiefcorrectie. |
| Lucht op alfa 0,7 | Overlappende kappen op 512-punts bogen geven een kralensnoer (0,7 → 0,91 op elke vertex). Alfa 1,0 en 1,0 px dun. |
| Halo als tweede schil of als alfa-profiel in dezelfde draw | De halo droeg geen taak meer sinds "de lijn geeft geen licht"; een extra schil kost de helft van de driehoeken, een alfa-profiel een bredere quad voor 0,13 verschil op een donkere bol. Weg, met screenshot-vergelijk. |
| Gedeelde `LineSegmentsGeometry` per stijlklasse (minimale-ingreep-voorstel) | `LineSegmentsGeometry` is instanced zonder index-selectie; elk object tekent álle instanties → elk segment 2–4× met spoorstrepen over zeebenen. |
| LOD via `geo.setIndex`-wissel op Line2 | Bestaat niet voor instanced geometry; alleen voor de dunne `LineSegments`, die hier juist vervalt. |
| Lazy "L3" = het originele json per stroom (product-voorstel) | Tweede tekenpad (object per stroom, `JSON.parse` van 0,6 MB per stroom op straatniveau) naast de bundel — precies de drift-bron die het voorstel zelf benoemde. Fijn in hetzelfde bin-formaat. |
| Kometen vast op L1 | Tot 200 m ≈ 15 px naast de fijne lijn op 14 km; H6 ("de lijn zegt waar") breekt. Baan op de getekende geometrie, geparametriseerd in originele km. |
| Komeetbudget 400 koppen met zoomband-selectie | Verandert "dát er iets beweegt" op wereldhoogte sterker dan nodig; de skip-regels halen hetzelfde per-frame-werk weg zonder het aantal te wijzigen. K per apparaat is één constante. |
| Gloedmaat en horizon naar de vertex-shader | Niet nodig: de lus is gemeten goedkoop (< 0,3 ms); de camera-ruimte-val (de bol draait) is een extra bron van fouten; golf-2-optie als de Honor-meting erom vraagt. |
| Crossfade tussen LOD-niveaus | Overbodig: ≤ 1 css-px op de grens per constructie; hysterese tegen flikkeren. |
| Visvalingam-Whyatt | DP zit al in de keten (`bake_landnet.py`) en de 2D-afwijking ís het schermcriterium. |
| Float32 in de bins | 3× de bytes (8,5 MB tegen 2,99); Pages gzipt, maar varint blijft kleiner én parsevrij. |
| `vertexcount`-acceptatietoets voor per-stroom aan/uit | Een gedegenereerde instantie wordt nog getekend; `renderer.info` beweegt niet → de toets zou groen zeggen terwijl de shader de vlag negeert ("de legenda loog"). Pixeltoets. |
| Pixelregressie als symmetrische masker-overlap ≥ 95 % | Oude en nieuwe lijn verschillen per constructie in breedte (1,7 device-px + halo vs 1,8 css-px); overlap meet breedte, niet geometrie. Afstandstransformatie (§11.12). |
| Alles in één sessie bouwen | Drie voorstellen, zes kritieken: 2–4 sessies werk. Zonder fasering gaat niets live (de les "lichte variant bij opschalen"). |

## 10 · Risico's

1. **De onBeforeCompile-patches hangen aan de GLSL van r185.** Mitigatie: pin in de importmap (staat), assert op de
   vier ankers bij het laden (luid), `customProgramCacheKey` overschreven; terugvalplan is de shader forken naar
   `stroomlijn.js`.
2. **Schermpixel-patronen kruipen tijdens het zoomen** (patroon in px, lijnlengte in px groeit; verankerd op het
   beenbegin). Geen fix nodig, wel iets dat Lars moet zien; op L0/L1 verspringt de fase níet bij een wissel omdat
   beide niveaus de originele km dragen.
3. **De halo weg en breedte in css-px veranderen het beeld** (ook in bouwmodus). Beide staan als constante en worden
   in beide standen met screenshots vergeleken; Lars' eerdere afkeuringen gingen over te véél licht, niet te dun.
4. **Fill-rate op de Honor** (gloed ≈ 2× schermvulling, Line2-quads) meet de emulatie niet. Daarom de telefoontest
   als poort, optioneel het adb-profiel, en de pixelRatio-klep als reserve in golf 2.
5. **Lon-ontwikkeling en DP over de datumgrens en bij de polen** (12 Pacific-zeebenen, Sabetta): een fout geeft een
   streep om de wereld. De baker toetst elke segmentlengte (≤ 2× verdichting) en faalt luid.
6. **Fijn-rebuild tijdens pannen op lokaal** (set benen-in-beeld wijzigt): in-place kopie van ≤ 200 k segmenten ≈
   10–20 ms op CPU ×4, hooguit elke 250 ms en alleen bij een wijziging; 15 % marge dempt dat. Hapert het zichtbaar,
   dan de rebuild in `requestIdleCallback`.
7. **Twee bewezen modules worden vervangen**; regressierisico in knoopvorm-wissel, km-noot, `vertakt_van`-benen en
   de drie hemelsbreed-modi → pariteits- en 8-standen-toetsen zijn hard en de oude modules gaan pas weg na groen.
8. **K = 1 op de telefoon en de 16-px-skip** veranderen de bewegingsindruk op wereldhoogte — een visuele keuze voor
   Lars, één `AFSTEMMING`-constante.
9. **De HUD-generatie verwijdert 182 handgeschreven knoppen** inclusief hun commentaarhistorie; die verhuist naar
   `noot` in het register, en de baker/HUD tonen `titel` als een `label` ontbreekt (zichtbaar).
10. **Twee tekenpaden (bundel en `?laag=los`) zijn een drift-bron** zolang ze naast elkaar leven → verwijdering in
    stap 4 is ingepland, niet "later".
11. **Pages-cache (max-age 600)**: een herbundel zonder `BUNDEL_VERSIE`-bump is voor bezoekers onzichtbaar → de
    werkregel in `bak_stromen.sh` en `--check` in de keuring; elke stap eindigt met een `?v=`-bump én de live-link
    met dat nummer naar Lars.

## 11 · Acceptatiecriteria (meet_atlas-uitkomsten, tenzij anders vermeld)

Tussen haakjes de nulmeting ?v=131. "Telefoon" = de emulatie (CPU ×4, 390 × 844, DPR 2 effectief); "desktop" =
1600 × 1000. Budgetten zijn ongecomprimeerd lokaal (§nulmeting).

1. **Verzoeken/bytes eerste weergave, `--modus atlas`**: data-verzoeken ≤ 5 — verwacht 3: `stromen-register.json`,
   `stromen.json`, `stromen-basis.bin` (382); data-bytes ≤ 1,5 MB — verwacht ≈ 0,7 MB (51,7 MB). In de lijst
   ontbreken `landnet.bin`, `aisnet-pilot.json`, `ankercheck.json` en elke `stroomroute-*.json`.
2. **Laden**: `msTotAlleStromen` ≤ 3.000 telefoon en ≤ 1.500 desktop (14.094 / 4.226), gewacht op
   `window.ATLAS.stats.geladen === window.ATLAS.stats.stromen === 182`.
3. **Draw calls, alles aan, alle vier kijkstanden**: ≤ 120 telefoon, ≤ 300 desktop (2.181–3.052);
   `window.ATLAS.stats.objecten` ≤ 6.
4. **Driehoeken**: ≤ 0,6 M op wereld en continent, ≤ 1,5 M op regionaal en lokaal (12,7 M).
5. **fps mediaan**: telefoon ≥ 30 op alle vier kijkstanden (9–14); desktop ≥ 60 (69–84).
6. **JS-heap**: ≤ 200 MB op elke kijkstand (365–475); verwacht 120–160.
7. **Fouten**: 0 console-fouten en 0 excepties in 2 kleurmodi × 4 lijnmodi × 2 profielen; één opzettelijk onbekende
   modaliteit in een testbestand geeft wél de `stroomstijl`-waarschuwing en een magenta lijn (de luide klasse).
8. **Pariteit bake** (`bak_stroombundel.py --toets`): `stromen.json` telt 182 stromen · 718 benen · 225 stippel ·
   650 markers · 451 sites; `kmPerModaliteit` opgeteld is per modaliteit gelijk aan de bron (truck 83.231 · spoor
   52.933 · zee 780.679 · binnenvaart 4.968 · leiding 15.310 · lucht 242.922 km); `stroomroute-ree-phaxay-namcan.json`
   staat in `uitgesloten`; tweemaal draaien is byte-identiek; `git diff --stat v2/data/stroomroute-*` is leeg;
   `--check` exit 0 op de commit en exit 1 na een opzettelijk gewijzigd bronbestand.
9. **Bediening (pixeltoetsen)**: alleen stroom X aan → > 0 pixels in zijn kleur binnen zijn been-bbox, X uit → 0,
   draw calls gelijk; grondstofchip uit → 0 pixels in die kleur én 0 gloedpixels op zijn sites; kleurwissel → per
   grondstof exact één kleur op tien steekproefpunten (≤ 12/255 per kanaal van `GRONDSTOF_KLEUR`, in bouwmodus van
   `MODALITEIT_KLEUR`); alle vier lijnmodi renderen met de lift per been van ?v=117 (route/recht-plat 1,000 behalve
   lucht · recht-boog zee ≈ 7,9 %, spoor ≈ 1,42 % · recht-zeeboog alleen zee > 1,000) — gemeten op de nieuwe buffers.
10. **Stippel-leesbaarheid**: continent-screenshot toont ≥ 3 losse streepjes op de Escondida-slurrystippel (0 nu);
    op lokaal dezelfde periode in css-px (8 ± 1).
11. **LOD-wissel**: screenshots op 0,9× en 1,1× van de L0/L1-grens: binnen een 2 px-masker om de lijnhartlijnen
    verschilt ≤ 2 % van de lijnpixels; geen "fijn-overloop"-waarschuwing in de console op de vier kijkstanden.
12. **Pixelregressie bouwmodus, lokaal (Tongling 14 km)**: afstandstransformatie — ≥ 98 % van de lijnpixels van
    `?laag=los` ligt binnen 2 css-px van een lijnpixel van de bundel en omgekeerd (geometrie, niet breedte).
13. **Landnet**: in `--modus atlas` 0 verzoeken naar `landnet.bin`; in `--modus bouw` wél, en de stats na "aan"
    identiek aan ?v=131 (netwerkKm, knopen, edges, punten).
14. **HUD op 375 px** (telefoonprofiel): `scrollWidth === 375`, chipstrip zichtbaar en bedienbaar bij ingeklapt
    paneel, tap-targets ≥ 36 px, `#bouw` dicht, AMSA-regel in de DOM, kop toont "182 stromen · 14 grondstoffen".
15. **Live**: `meet_atlas --url https://larswalters.github.io/grondstoffen-atlas/v2/ --modus atlas` toont
    `stromen-basis.bin?v=<BUNDEL_VERSIE>` met `Content-Encoding: gzip` en dezelfde telling; Lars' telefoontest
    (Honor Magic V5, live-link met `?v=`) meldt `#stats` ≥ 30 fps op de vier kijkstanden — de enige meting die de
    fill-rate echt ziet.

## 12 · Bouwvolgorde met regressietoets per stap

Elke stap eindigt met: meting met `meet_atlas` (beide profielen), push, `?v=`-bump, live-link mét versienummer naar
Lars, wrapup. Geen stap begint vóór de toets van de vorige groen is.

**Stap 0 — register en bundel (geen browserwijziging).** `stromen-register.json` uit het `STROMEN`-blok (met de
noten), `bak_stroombundel.py` (+ `--check`/`--toets`), `bak_stromen.sh bundel`, de bins en `stromen.json` gecommit,
§7 in de bakhandleiding.
*Regressietoets*: §11.8 volledig; de live site is ongewijzigd (?v=131 blijft).

**Stap 1 — de bundel op de bol, atlas als default.** `stroombundel.js`, `stroomlijn.js` (stijl = effen per
modaliteit op de breedtes uit §4 + stippel in pixels; de lengtepatronen nog uit), `stroomkometen.js`, `gloed.js` één
object, `gloednodes.js` uit `stromen.json`, LOD met de formule uit §2.2 en de fijn-rebuild, de twee texturen,
`main.js` met defaults, `BUNDEL_VERSIE`, `?modus=bouw`, `?laag=los`, landnet/aisnet/ankercheck lui, `meet_atlas
--modus`. HUD alleen minimaal (titel, is-on-klassen, bouwsectie als wrapper; de productindeling komt in stap 3).
*Regressietoets*: §11.1–9, 11.12, 11.13; plus 0 fouten in de 8 standen in beide paden (`?laag=los` moet dezelfde
182 stromen en km-regels geven). **Poort: de telefoontest van Lars** (§11.15). Haalt de Honor de 30 niet, dan eerst
diagnose (fill-rate: gloed-sprites, Line2-breedte, tegel-DPR) vóór stap 2 — niet draaien aan afstemming zonder meting.

**Stap 2 — lijnstijl per modaliteit.** `LIJNSTIJL` in `stroomstijl.js`, de lengtepatronen en het truck-dwarsprofiel
in de shader, de legenda-SVG uit de tabel, bouwmodus zonder patronen.
*Regressietoets*: §11.7 en 11.10; screenshots wereld/continent/regionaal/lokaal in beide kleurmodi vergeleken met
stap 1 (alleen de lijntextuur mag verschillen: zelfde geometrie, zelfde kleuren op de steekproefpunten);
patroonperiode gemeten in css-px op lokaal en wereld binnen ± 1 px.

**Stap 3 — de HUD als product.** Generatie uit het register, grondstofrijen/-chips, chipstrip, legenda, bouwsectie,
bronnen-voet, 375 px-CSS; `meet_atlas` wacht op `ATLAS.stats` en krijgt het 375 px-profiel.
*Regressietoets*: §11.14; alle `.srBtn`/`.gsBtn`-handvatten werken (toggle-pixeltoets opnieuw); de km-noot per
grondstof toont dezelfde regels als ?v=131; 0 fouten in de 8 standen.

**Stap 4 — opruimen en vastleggen.** `stroomroute.js`, `stroomleven.js` en `?laag=los` weg in een eigen commit;
`decisions.md` en `CLAUDE.md`: besluit 1 vervangt de default van 2026-08-07, het landnet-besluit, de
bundel-werkregel; slotmeting tegen Pages (§11.15) en de volledige acceptatielijst opnieuw.
*Regressietoets*: §11 integraal; `git grep stroomroute.js v2/src` leeg; `bak_stroombundel.py --check` exit 0.

## 13 · Bewust naar golf 2

- **Gloedkoepel kern/halo** en de afstemming van de koepel op de telefoon (incl. de vraag of `minPx` 34 in device-
  of css-px hoort — vandaag device-px, dus 17 css-px op DPR 2; ongewijzigd gelaten omdat het een zichtbare keuze is).
- **Stadslichten** (Black Marble) als de "aderen" van de referentiebeelden; tot die tijd eventueel `landnet-L0.bin`
  gedimd, pas na de screenshots van stap 1 beslist.
- **Labels per zoomband** en de semantische banden van de ontwerpbrief (het `level`/`parent`-model blijft bestaan).
- **Dikte = volume** en **aantal kometen uit volume**, zodra het losse metadatabestand volume per been draagt; de
  haak (`beenInfo.B`) staat klaar zonder shaderwijziging.
- **Gloedmaat in de vertex-shader** en een **adaptieve pixelRatio-klep** (mediane fps 3 s < 30 → 1,5): alleen als de
  Honor-meting erom vraagt.
- **Tegels**: na deze golf de grootste post (72–204 draw calls, DPR 2-textures); eigen meting en budgetvraag.
- **De bleke grondstofkleuren** (zilver `e6f2ff`, pgm `c0e0ff`, diamant `a8f0ff`, grafiet `7fd8ff`; goud/ree/uranium
  in één geelgroene band) vallen op wereldhoogte met alles aan samen. Dat is een keuze van Lars (2026-08-07) in één
  tabel en wordt niet stil aangepast; wél als beslisvraag met screenshot voorgelegd na stap 2.
- Een vijfde `meet_atlas`-profiel **"honor"** via adb, als de handmatige telefoontest te vaak nodig blijkt.

## Gerelateerd

- `v2/design/lod-ontwerpbrief.md` — de visuele taal en de besluiten van 2026-07-19 waar dit plan de eerste
  productstap van is; `v2/design/referenties/lod-referentie-1-zoomniveaus.png` en `-2-hotspots.png` zijn de doelbeelden.
- `build-cache/meting/v131-default-rapport.json` · `v131-atlas-rapport.json` en de acht screenshots per profiel —
  de nulmeting; `v2/tools/meet_atlas.mjs` — het meetgereedschap.
- `v2/src/stroomstijl.js` (kleur en lijnvorm), `v2/src/gloed.js` (het koepelmechanisme), `v2/src/landnet.js`
  (varint-lezer en het bin-patroon), `v2/tools/bak_stromen.sh` + `v2/design/bakhandleiding-licht.md` (hoe een keten
  gebakken wordt; de bundel wordt stap 7 daarvan).
- Linear: LAR-490 (M26 · LOD); de vier stappen worden sub-issues met dit document als spec.
- memory/decisions.md 2026-08-07 (default modaliteit — **vervangen door besluit 1**), 2026-08-06 (bakken is geen
  deliverable), 2026-09-28 (volledig-stippel wordt niet geregistreerd), 2026-07-22 (horizon via clipping plane).
