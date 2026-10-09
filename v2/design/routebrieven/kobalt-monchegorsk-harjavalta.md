# Routebrief (licht) · kobalt — Monchegorsk (Kola MMC) → Vainikkala → Harjavalta (Finland)

**stroom-id:** `kobalt-monchegorsk-harjavalta` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** Ni-Co-matte/tussenproduct van Severonickel (Kola MMC / Nornickel, Monchegorsk) per **spoor** over de Oktoberspoorweg (Olenegorsk – Kandalaksha – Petrozavodsk – Volkhov – Mga – Vyborg) naar de Finse grens bij **Vainikkala**, dan over het Finse net (Kouvola – Lahti – Riihimäki – Tampere – Pori-lijn) naar Norilsk Nickel Harjavalta Oy, dat uit dat materiaal o.a. **kobaltsulfaat** maakt. **Aannemelijk: één bron, Ni-Co-matte, kobaltaandeel niet gemeten** — er is geen bron die zegt dat kobalt of kobaltsulfaat zelf per spoor reist.
**Welke as van het verhaal:** *het sanctie-gat, kobaltkant.* Harjavalta maakt kobaltsulfaat uit het Russische feedmateriaal (≈94% van de feed, 2021 [1]); product sinds 2014 [5]. Volume: **~1,8 kt Co/j in sulfaat** bij Harjavalta (Interfax, nov 2022; productie of capaciteit niet gespecificeerd) [2]. Bovengrens uit Russische feed ≈ **1,7 kt Co/j** (1,8 × 94%; eigen optelling, twee verschillende peiljaren, geen meting van het kobaltaandeel per lading). Los daarvan: Kola MMC's eigen kobaltmetaalwerkplaats, 3,0 kt Co/j capaciteit sinds dec 2025 [6], is een ander circuit (zie `kobalt-norilsk-monchegorsk`). **De geometrie is een letterlijke kopie van `nikkel-monchegorsk-harjavalta`**: zelfde lading, zelfde lijn, andere grondstofkleur (visueel dubbel, bindend besluit toets).

## 1 · Ketenkaart
```
Kola MMC `co-monchegorsk-kola` ──(b1 spoor · Monchegorsk→Olenegorsk→Kandalaksha→Petrozavodsk-lijn · 956,6 km, kopmaak Olenegorsk)──► via 1 Petrozavodsk-lijn
   ──(b2 spoor · Murmansk-lijn Svir→Volkhov · 277,4 km)──► via 2 Volkhov-knoop ──(b3 spoor · Mga → SPb-omleiding → Vyborg · 281,8 km)──► `co-vainikkala-grens`
   ──(b4 spoor · Finse net Kouvola–Lahti–Riihimäki–Tampere–Pori · 432,5 km)──► Harjavalta-raffinaderij `co-harjavalta-raffinaderij` ⏹ stoppunt
```
Sluit aan op `kobalt-norilsk-monchegorsk` (die eindigt in Monchegorsk): Norilsk-matte → Moermansk → Monchegorsk → Harjavalta is dan één doorlopend verhaal.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | spoor | Kola MMC → via 1 Petrozavodsk-lijn | Oktoberspoorweg Monchegorsk–Olenegorsk–Apatity–Kandalaksha–Belomorsk–Segezha–Petrozavodsk | 956,6 gebakken (router 949,9); geen gepubliceerde spoor-km [9] | **kopie** nikkel b1: `spoorroute-nikkel-monchegorsk-harjavalta-b1-monchegorsk-petrozavodsk.geojson` | nee |
| b2 | C | spoor | via 1 → via 2 Volkhov-knoop | Murmansk-lijn Petrozavodsk–Svir–Volkhov | 277,4 gebakken [9] | **kopie** nikkel b2: `…-b2-petrozavodsk-volkhov.geojson` | nee |
| b3 | C | spoor | via 2 → Vainikkala-grensknoop | Volkhov–Mga–SPb-omleiding–Vyborg–Buslovskaya | 281,8 gebakken [9] | **kopie** nikkel b3: `…-b3-volkhov-vainikkala.geojson` | nee |
| b4 | C | spoor | Vainikkala → Harjavalta-raffinaderij | Vainikkala–Luumäki–Kouvola–Lahti–Riihimäki–Tampere–Pori-lijn, Kokemäki | 432,5 gebakken [9] | **kopie** nikkel b4: `…-b4-vainikkala-harjavalta.geojson` | nee |
Totaal **1.948,3 km**, hemelsbreed Monchegorsk–Harjavalta **891 km, geen spoorkm** — de ±15%-toets is alleen een indicatie. Sanity: Kirov Railway SPb–Murmansk 1.448 km [8], Monchegorsk ligt 145 km ten zuiden van Murmansk [8]; Monchegorsk–Volkhov (1.234,0) valt daar logisch in. Alle vier de geojsons zijn FeatureCollections in `v2/build-cache/ais/graaf/` (3.147/692/560/1.438 punten), uiteinden delen één netknoop (naden 0,000 km volgens de nikkelbak [9]). Geen stippel, geen haven-aanloop, geen last-mile: de net-snaps liggen op 0,23 km (Kola) en 0,19 km (Harjavalta).
**Beennamen (bindend):** elke naam draagt `(aannemelijk: één bron, Ni-Co-matte, kobaltaandeel niet gemeten)` én `kopie van nikkel-monchegorsk-harjavalta bN`.

## 3 · Ankers (één per site en per overslag; alle letterlijk hergebruikt)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-monchegorsk-kola` | laad-/startpunt | Severonickel (Kola MMC), Monchegorsk | 67.9195, 32.8320 | [9][10], z15 eigen blik 2026-10-09 | bron-gelegd (kruis ligt aan de noordrand van het complex bij de spoorbundel; tanks links ervan, hallen en schoorstenen zuidelijk, groot emplacement oost) |
| `co-vainikkala-grens` | grensovergang | Vainikkala-grensknoop (gedeelde node finland- en rusland-noordwest-net) | 60.8596, 28.3208 | [9] (Wikipedia-dorp 60.8661, 28.2997 ligt 1,4 km verderop [8]) | bron-gelegd (z15: kruis op de dubbelsporige hoofdlijn ten zuidoosten van het Vainikkala-rangeerterrein; één Esri-tegel ontbreekt noordelijk, niet bij het anker) |
| `co-harjavalta-raffinaderij` | losplek/raffinaderij | Norilsk Nickel Harjavalta Oy, Teollisuuskatu 1 | 61.3188, 22.1225 | [5][9], z15 eigen blik 2026-10-09 | bron-gelegd (kruis in het hallen-/ketelblok van het raffinaderijcomplex, tankpark noord, goederenspoor zuidwest, Kokemäenjoki oost) |
Het kobalt-sitelaag heeft geen Harjavalta- of Kola-MMC-site (alleen `w-norilsk` draagt de 3 kt Kola-capaciteit op de Norilsk-centroïde); sitelagen niet aangeraakt, zie §7.

## 4 · Via-punten (alleen b1–b3; geen corridorkeuze in Finland)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1/b2 | 1 | Petrozavodsk-lijn (station op de hoofdlijn, snap 0,30 km) | 61.7723, 34.3751 | een vrije Dijkstra kiest de verkeerde grens (Vartius/Kajaani, 1.589 km); dwingt de Murmansk-lijn af [9] |
| b2/b3 | 2 | Volkhov-knoop (hoofdlijn-junctie, snap 0,00 km) | 59.9217, 32.3074 | houdt de route op de Oktoberspoorweg i.p.v. de Sortavala-sluipweg (63 km korter, via Vyborg-Sortavala) [9] |
| b3/b4 | 3 | Vainikkala-grensknoop | 60.8596, 28.3208 | grensovergang; naadpunt van b3/b4 |
Geen nieuwe via-punten en geen scan: alles is overgenomen uit de gebakken nikkelstroom. Nooit via-punten bij Sint-Petersburg (de route loopt al over de omleiding).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Severonickel, Monchegorsk | Nornickel (Kola MMC) | converter-matte → Ni-Co-matte/tussenproduct in containers | 145 kt Ni/j raffinage (zie nikkel-norilsk-monchegorsk) | [9] |
| Harjavalta | Norilsk Nickel Harjavalta Oy | matte/feed (~94% Russisch, 2021) → nikkelkathode, -zouten, **kobaltsulfaat en -oplossingen**, koperkoek | 65 kt Ni/j nu (>100 kt aangekondigd 2021, niet bevestigd), ~1,8 kt Co/j in sulfaat, ~20 kt Cu in koperkoek (2022) | [1][2][3][5] |

## 6 · Stoppunt
Harjavalta: kobaltsulfaat is het eindproduct; Nornickel noemt als afnemer batterijtoepassingen in het algemeen [12], Global Witness alleen Umicore als koper van "beperkte volumes nikkel- en kobaltproducten" [1] — geen afnemer per lading, dus fase D vervalt en E ook.

## 7 · Open punten
- **Het kobaltaandeel van de lading is niet gemeten.** De treinen dragen Ni-Co-matte; geen bron splitst Co of zegt dat kobaltsulfaat zelf per spoor reist. Global Witness noemt Harjavalta-kobalt alleen als Umicore-inkoop en 290 containers/maand over de grens (alle lading, apr 2024–jan 2025) [1]; Boliden-materiaal is niet te scheiden.
- Het cijfer 1,8 kt Co in sulfaat is van Interfax nov 2022 [2], zonder aanduiding productie/capaciteit; de 94% Russische feed is van 2021 [1]. De bovengrens 1,7 kt is dus een eigen optelling over twee peiljaren, geen meting.
- Een tweede feedbron: Fortum meldt alleen "nickel cobalt sulphate solution" aan Harjavalta te hebben geleverd [1]; dat is niet-Russisch kobalt in dezelfde fabriek, dus niet alle kobaltsulfaat komt uit de matte.
- Interfax zegt dat het Kola-concentraat "usually" vanuit Moermansk per spoor gaat [2]; onze b1 start in Monchegorsk (Moermansk-lading voegt bij Olenegorsk in). Het precieze beginpunt per lading is niet gepubliceerd.
- Actualiteit: Yle (aug 2024) noemt dagelijkse Russische grondstoftreinen bij Vainikkala, EU en Finland sanctioneren Russisch nikkel niet [4]; geen bron uit 2026. Lees als infrastructuur en gedocumenteerd patroon, niet als actuele lading.
- Geen gepubliceerde spoorkilometers voor deze relatie; kopmaak bij Olenegorsk (68.1397, 33.2323) is een echte keerlus van de nikkelbak, geen fout. De kobaltlijn ligt exact op de nikkellijn (visueel dubbel).
- Sitelaag (niet aangeraakt, centraal gelijktrekken): `kobalt-sitelaag.json` heeft geen site Harjavalta (1,8 kt Co/j) en geen site Kola MMC op 67.9195, 32.8320; `w-norilsk` (69.35, 88.20) draagt de 3 kt Kola-capaciteit.
- De Nornickel-productfiche CobaltSulphate.pdf (kobalt uit "primary nickel raw material feed") kon niet geopend worden (404); de zin komt uit een zoekresultaat [12].

## 8 · Bronnen
[1] Global Witness, "Sanctions gap lets Russian-mined nickel flow to Western markets" (2025): 94% Russische feed, 65 kt, 290 containers/maand, Umicore koopt beperkt Ni- en Co-producten, Fortum-sulfaatoplossing (gelezen 2026-10-09). https://globalwitness.org/en/campaigns/transition-minerals/sanctions-gap-lets-russian-mined-nickel-flow-to-western-markets/
[2] Interfax, 17-11-2022, "Nornickel mulls alternatives to supply Finnish plant if shipments from Russia halted": ~65 kt Ni, 20 kt Cu, 1.800 t Co in sulfaat, ~100 kt concentraat van Kola MMC meestal per spoor vanuit Moermansk (gelezen 2026-10-09). https://interfax.com/newsroom/top-stories/85025/
[3] NS Energy, Nornickel Harjavalta expansion (2021): producten "cobalt sulphates and solutions", 65 → 75 → >100 ktpa (gelezen). https://www.nsenergybusiness.com/company-news/nornickel-harjavalta-nickel-refinery-expansion/
[4] Yle, 26-08-2024: Vainikkala hoofdovergang voor Russische grondstoffen, EU/Finland sanctioneren nikkel niet; noemt geen kobalt (gelezen). https://yle.fi/a/74-20106170
[5] Nornickel Harjavalta, "The story of": kobaltsulfaat-productielijn sinds 2014, Teollisuuskatu 1, 29200 Harjavalta (gelezen). https://www.nornickel.fi/en-gb/nornickel-harjavalta/history
[6] Interfax, 08-12-2025: Kola MMC kobaltwerkplaats hersteld, tot 3.000 t Co-metaal/j, 2.500 t vóór de brand van 2022; geen exportvermelding (gelezen). https://interfax.com/newsroom/top-stories/115189/
[7] Interfax, 21-02-2025, kobaltproductie Kola hervat (alleen via `kobalt-norilsk-monchegorsk` [2] en zoekresultaat). https://interfax.com/newsroom/top-stories/109943/
[8] Wikipedia, Vainikkala (60.8661, 28.2997), Kirov Railway (1.448 km), Monchegorsk — overgenomen uit de nikkelbrief [4][7][8], niet opnieuw gelezen.
[9] `v2/design/routebrieven/nikkel-monchegorsk-harjavalta.md` (§2–§4, §9) en `v2/data/stroomroute-nikkel-monchegorsk-harjavalta.json`: alle km, via-punten, snaps en geojson-namen.
[10] `v2/design/routebrieven/kobalt-norilsk-monchegorsk.md` (anker `co-monchegorsk-kola`) en `v2/design/kobalt-sitelaag.json`.
[11] Esri World Imagery via `sat_check.py` z15: `v2/build-cache/satcheck/sat-kobalt-monchegorsk-harjavalta-{monchegorsk-kola-mmc,vainikkala-grens,harjavalta-raffinaderij}.png`.
[12] Zoekresultaat (Nornickel Harjavalta, CobaltSulphate.pdf, zoekmachinesnippet; pdf zelf 404): kobaltsulfaat "separated from primary nickel raw material feed", voor oplaadbare batterijen. https://www.nornickel.fi/uploads/Y77hn2Pj/CobaltSulphate.pdf

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Recept:** `bash v2/tools/bak_stromen.sh kobalt-monchegorsk-harjavalta` (functie `bak_kobalt_monchegorsk_harjavalta`, zwaar-slot, 15 s). Geen scan, geen routerrun, geen extract: vier `--been-geojson`-regels met de bestaande nikkel-geojsons in `v2/build-cache/ais/graaf/` (`spoorroute-nikkel-monchegorsk-harjavalta-b1…b4`), in reisvolgorde, drie `--marker`-regels. Uitvoer `v2/data/stroomroute-kobalt-monchegorsk-harjavalta.json`, 103,2 KB, versie 2, `punt_formaat` lonlat, modaliteit alleen `spoor`.

| # | modaliteit | km | punten | naad naar volgend been | stippel |
|---|---|---|---|---|---|
| b1 | spoor | 956,6 | 3.147 | 0,00 km | nee |
| b2 | spoor | 277,4 | 692 | 0,00 km | nee |
| b3 | spoor | 281,8 | 560 | 0,00 km | nee |
| b4 | spoor | 432,5 | 1.438 | (einde) | nee |
Totaal **1.948,3 km**, 5.837 punten, 3 markers. Alle vier de benen zijn punt voor punt gelijk aan `stroomroute-nikkel-monchegorsk-harjavalta.json` (gecontroleerd). Geen gepubliceerde spoorkm: de ±15%-toets is een indicatie; Monchegorsk–Harjavalta is hemelsbreed 891 km, de omwegfactor 2,19 komt doordat de lijn eerst zuidwaarts naar Volkhov loopt en dan via Vyborg naar de Finse grens, niet uit een sluipweg.
**Markers:** `co-monchegorsk-kola` 0,23 km van de lijn, `co-vainikkala-grens` 0,00 km, `co-harjavalta-raffinaderij` 0,19 km (allemaal binnen de 0,5 km-norm). Ankers letterlijk uit §3; geen nieuwe satellietpass nodig (de drie z15-beelden staan in `v2/build-cache/satcheck/sat-kobalt-monchegorsk-harjavalta-*.png`).
**Toetsen:** naden 0,00 km (max 0,00); `toets_knikken.py`: 1 knik >= 60 graden, een terugloop bij 68.1397, 33.2323 (Olenegorsk), de echte keerlus van de kopmaak die de nikkelbak ook heeft (zie §7), geen fout; `toets_rechte_benen.py --min-km 5`: geen enkel van de vier benen staat in de lijst van rechte benen.
**Stippel / haven-aanloop / vlucht / leiding:** geen. Er is geen zee-, lucht-, leiding- of wegbeen; het net reikt over de hele keten.
**Beennamen:** elke naam draagt `(aannemelijk: een bron, Ni-Co-matte, kobaltaandeel niet gemeten)` en `kopie van nikkel-monchegorsk-harjavalta bN`.
**Lessen:** (1) een letterlijk gedeeld been kost alleen een functie van vier regels en geen enkele rekenrun; de enige beslissing is de beennaam. (2) De kobaltlijn ligt exact op de nikkellijn: op de bol is dat visueel dubbel, wie dat wil oplossen doet dat in de tekenlaag, niet door de geometrie te verschuiven. (3) De sitelaag-punten voor Harjavalta en Kola MMC ontbreken nog in `kobalt-sitelaag.json` (zie §7), centraal gelijktrekken.
