# Routebrief (licht) · olie — Forties Unity (Noordzee) → Cruden Bay → Kinneil → Hound Point (Verenigd Koninkrijk)

**stroom-id:** `olie-fortiesunity-houndpoint` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) ·
**status:** gebakken
**Keten in één zin:** Ruwe olie van het Forties-systeem (≈85 Noordzeevelden) gaat per **36-inch-leiding** (Ineos Forties Pipeline
System) vanaf het onbemande riserplatform Forties Unity 162 km onderzees naar Cruden Bay, 213 km onshore (Angus, Fife) naar de
Kinneil-stabilisatie bij Grangemouth en 23 km langs de zuidoever van de Forth via de Dalmeny-tankpark naar de laadsteiger Hound Point;
daar eindigt het bewijs.
**Welke as van het verhaal:** *de Britse Noordzee-slagader* — FPS draagt ruwweg 30% van de Britse olie [1]; Forties Blend is de grootste
component van de Dated Brent-benchmark [5]. Volume: gemiddelde doorvoer **445 kb/d** (peiljaar 2016, Ineos/OGJ [2][3]); capaciteit
575–610 kb/d [2][3]; recenter ~300 kb/d aan laadvolume (artikel over 2021–22, geen doorvoer) [5]; een actueel 2024/25-cijfer is niet gevonden.

## 1 · Ketenkaart
```
Forties Unity riserplatform `ol-fps-unity` (offshore, 57.7205/0.7520)
   ──(b1 leiding · Forties-pijpleiding onderzees, OSM 161,9 km / gepubliceerd 169 · doorgetrokken)──►
Cruden Bay (landfall 57.3969/-1.8582; booster-station `ol-fps-crudenbay`)
   ──(b2 leiding · Ineos FPS onshore 36", via Netherley, Brechin, Balbeggie · OSM 213,5 km / gepubliceerd 209 · 8 naden recht)──►
Kinneil Terminal `ol-fps-kinneil` (Grangemouth)
   ──(b3 leiding · FPS langs de Forth · 23,1 km)──► Dalmeny-tankpark `ol-fps-dalmeny` ──► Hound Point-steiger `ol-fps-houndpoint` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Forties Unity → landfall Cruden Bay | Forties pipeline (Apache/Ineos), onderzees; OSM-ways 903798450 + 174743471 | 169 [2][3]; OSM 161,9 (−4,2%) [8] | OSM-pipeline, één component, geen naad | nee |
| b2 | A | leiding | landfall Cruden Bay → Kinneil Terminal | Ineos FPS onshore, 36" (OSM `operator=Ineos FPS`, ways in §4); pompstations Netherley, Brechin, Balbeggie [1] | 209 [2][3]; OSM 213,5 incl. 12,8 km rechte naden (+2,2%) [8] | OSM-pipeline, gestikt met 8 rechte stukken (2,2 / 2,4 / 2,5 / 4,6 km e.a.) | nee — naden zijn ontbrekende OSM-ways van een bestaande ondergrondse leiding, geen net-gat |
| b3 | A/B | leiding | Kinneil → Dalmeny-tankpark → Hound Point | Ineos FPS, zuidoever Forth; ways 868045319, 868045318, 689506386, 689503549 | OSM 23,1 (22,7 + 0,35 naden); geen gepubliceerde km | OSM-pipeline | nee |

Geen zeebeen, geen afnemer, geen last-mile: de leiding is de hele keten. Hound Point-steiger = laadpunt voor tankers (twee zee-eilandkades tot
350.000 DWT [4]); een bestemming per lading is niet gebrond, dus geen zeebeen en geen haven-aanloop.
Kinneil-keerpunt: de leiding loopt 3,7 km westwaarts voorbij Kinneil-Kerse naar het complex en 8,6 km terug oostwaarts (echte route: ways
1449717146 en 868045319); `toets_knikken` kan hier een omkering (~150°) of terugloop melden, bedoeld.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-fps-unity` | kop: riserplatform (offshore) | Forties Unity (Ineos noemt hem onbemand [2]) | 57.7205, 0.7520 | [6][8] | aannemelijk (OSM-leidingbegin, 16 km west van het Forties-veld 57.7167/1.0167 [6] zoals "further west"; Esri heeft offshore geen beeld, `…-unity.png` grijs) |
| `ol-fps-crudenbay` | overslag/booster langs de leiding (landfall + booster) | Cruden Bay Booster Station (FPS) | 57.3849, -1.8896 | [1][8][9] | bron-gelegd (z15 gezien: omheinde compound met pompgebouwen en tankjes in akkerland, ±2,4 km van de kust; OSM-onshoreleiding begint hier) |
| `ol-fps-kinneil` | overslag: stabilisatie/terminal | Kinneil Terminal (Ineos), Grangemouth | 56.0040, -3.6640 | [2][7][8] | bron-gelegd (z15 gezien: groot proces- en tankcomplex, 4 tanks, ten oosten van de Avon; kruis op de zuidrand van het terrein waar de OSM-leidingen samenkomen) |
| `ol-fps-dalmeny` | opslag voor export | Dalmeny-tankpark (Ineos), South Queensferry | 55.9765, -3.3684 | [2][4][9] | bron-gelegd (z15 gezien: 9 tanks met drijvend dak in een omwald terrein; OSM-leiding 0,2 km ernaast) |
| `ol-fps-houndpoint` | einde: laadsteiger (stoppunt) | Hound Point-terminal (Ineos) | 56.0059, -3.3591 | [4][8] | bron-gelegd (z15 gezien: lange steiger met twee laadplatforms ±0,7 km uit de zuidoever; kruis op de steiger, OSM-leidingeind 0,22 km westelijker op dezelfde steiger) |

*Ankerkeuze.* Hergebruik: geen bestaand anker in het VK (geen stroom ligt hier). Hound Point = Wikipedia-punt [4]; Dalmeny en Cruden Bay-booster
= OSM-landuse (`W7917141`, `W217393975`). Kinneil: Wikipedia kent geen coördinaat; de OSM-FPS-ways eindigen/keren bij 56.0040/-3.6640 en dat
valt op het complex. De ontwerptoets noemde ook "Kinneil-Grangemouth 3,7 km west": klopt, het complex ligt aan de westkant van de lus.

## 4 · Via-punten
Niet van toepassing: drie leidingbenen uit OSM-ways, geen corridorkeuze. Ways b1: 903798450 (131,9 km), 174743471 (30,1 km). Ways b2 (in
reisvolgorde): 1079030566, 995752750 (102,5 km), 1080555747 (55,9 km), 1418120450, 1418120452, 1050623035 (15,0 km), 1449978876 (13,4 km),
1449978877 (4,8 km, onder de Forth), 1449717146 (3,7 km). Ways b3: 868045319 (8,6 km), 868045318, 689506386 (8,2 km), 689503549 (3,5 km).
**Naden b2 (rechte stukken, hemelsbreed, ondergronds):** landfall→1079030566 0,58 · →995752750 0,24 · →1080555747 0,12 · →1418120450 2,15 ·
→1418120452 2,37 · →1050623035 4,63 · →1449978876 2,48 · eind 1449717146→868045319 0,25 km; b3-naden 0,01 en 0,34 km. Alle < 5 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Forties Unity / FPS-offshore | Ineos (sinds 2017; voorheen BP) | olie van ≈85 velden → 36"-leiding | 575–610 kb/d; 445 kb/d (2016) | [1][2][3] |
| Kinneil Terminal | Ineos | onstabiele ruwe olie + condensaat (St Fergus) → gestabiliseerd; naar Grangemouth of Dalmeny | stabilisatie >1 mln vaten/d ontworpen | [1][7] |
| Dalmeny-tankpark + Hound Point | Ineos | opslag → tankerlading | twee berths tot 350.000 DWT | [2][4] |

## 6 · Stoppunt
De brief stopt op Hound Point: de bron geeft de steiger als exportpunt van de Forties-olie, maar geen bron koppelt een lading aan een
afnemer of haven (de Grangemouth-raffinaderij is een tweede uitgang en hoort niet tot deze lijn). Geen zeebeen: een bestemming verzinnen is verboden.

## 7 · Open punten
- **Actueel volume ontbreekt:** doorvoer 2016 = 445 kb/d [2]; een Upstream-bericht noemt tijdelijk 330 kb/d bij een Unity-stilstand (ongedateerd, niet gebruikt) [10]; 2024/25 niet gevonden.
- **Offshore beginpunt aannemelijk, één bron:** OSM-leidingknoop 57.7205/0.7520 (Nexen-lijnen sluiten er aan); platformnaam niet in OSM, geen satellietbeeld.
- **Offshore-lengte** 161,9 km (OSM) tegen 169 km gepubliceerd: −4,2%, mogelijk omdat de gepubliceerde lengte bij Unity zelf begint of de leiding gladgestreken is.
- **Naden in OSM:** 8 rechte stukken (12,8 km) in b2 en 0,35 km in b3; de leiding zelf loopt waarschijnlijk iets anders tussen de uiteinden.
- **Kinneil-anker:** coördinaat afgeleid van OSM-ways + beeld, geen Wikipedia-punt; Esri toont het complex, niet de naam. Grangemouth-raffinaderij (2025 gesloten, niet zelf gecontroleerd) ligt aan de overkant van de Avon.
- **Afnemers van Forties Blend** (Noordwest-Europa, Azië) niet gebrond: geen fase C.
- Er bestaan ook oudere/nabije lijnen (32" afgedankt [1], NGL-way 1458748251, Falkirk-Grangemouth FGOP) die bewust niet zijn gebruikt.

## 8 · Bronnen
[1] Wikipedia, "Forties pipeline system" — 169 km 36", Cruden Bay, Kinneil, pompstations Netherley/Brechin/Balbeggie, 575 kb/d, ≈30% VK-olie, 85 velden. https://en.wikipedia.org/wiki/Forties_pipeline_system
[2] INEOS, "completes the acquisition of the North Sea Forties Pipeline System and Kinneil Terminal from BP" — Unity onbemand, 169 km + 209 km, Dalmeny, Hound Point, 610 kb/d, 445 kb/d (2016). https://www.ineos.com/sites/grangemouth/news/ineos-completes-the-acquisition-of-the-north-sea-forties-pipeline-system-and-kinneil-terminal-from-bp/
[3] Oil & Gas Journal (6-4-2017), "Ineos to buy BP's Forties pipeline, Kinneil terminal for $250 million" — 575 kb/d, 169 + 209 km, 445 kb/d (2016). https://www.ogj.com/pipelines-transportation/article/17289849/ineos-to-buy-bps-forties-pipeline-kinneil-terminal-for-250-million
[4] Wikipedia, "Hound Point" — 56.0059/−3.3591, twee berths 350.000 DWT, Dalmeny-tankpark. https://en.wikipedia.org/wiki/Hound_Point
[5] Hellenic Shipping News — Forties-doorvoer −21% in 2021, ~300 kb/d aan laadvolumes, Forties Blend grootste bijdrage aan Dated Brent. https://www.hellenicshippingnews.com/?p=930859
[6] Wikipedia, "Forties oil field" — veld 57.7167/1.0167; Unity "further west", BP-bezit; productie piek 1979. https://en.wikipedia.org/wiki/Forties_oil_field
[7] Scottish Places, "Kinneil Terminal" — Kerse of Kinneil, aan de overkant van de Avon van de raffinaderij; stabilisatie; 90 medewerkers. https://www.scottish-places.info/features/featurefirst18052.html
[8] OpenStreetMap (ODbL), eigen PBF-scan 2026-10-31 van `groot-brittannie-latest.osm.pbf`: 22 oil-ways (Ineos FPS / Forties pipeline), bruggen/naden gemeten; begin 57.72049/0.75203, eind 56.00567/−3.36258.
[9] OpenStreetMap via Photon-zoekopdracht: `W217393975` (Cruden Bay Booster Station, 57.3849/−1.8896), `W7917141` (Dalmeny Tank Farm, 55.9765/−3.3684). https://photon.komoot.io
[10] Upstream, "Unity shutdown hits Forties" (ongedateerd zoekresultaat). https://www.upstreamonline.com/online/unity-shutdown-hits-forties/1-1-1073697
[11] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-olie-fortiesunity-houndpoint-{houndpoint,dalmeny,crudenbay,kinneil-z15,kinneil-z16,unity}.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
`bash v2/tools/bak_stromen.sh olie-fortiesunity-houndpoint` → `v2/data/stroomroute-olie-fortiesunity-houndpoint.json` (17,0 KB, versie 2, lonlat,
3 benen, 797 punten, 5 markers). Recept: functie `bak_olie_fortiesunity_houndpoint` in `v2/tools/bak_stromen.sh`; geometrie uit
`v2/tools/maak_leidingbeen_olie_fortiesunity_houndpoint.py --schrijf` (pure-Python-PBF-lezer, ways bij id uit §4, `groot-brittannie-latest.osm.pbf`,
~2,5 min scan na het wachten op een slot) → `build-cache/ais/graaf/olie-fortiesunity-houndpoint-leiding-b{1,2,3}.geojson`. Geen wegprofiel, geen zee, geen extra extract.

| # | modaliteit | km gebakken | km brief | afwijking | punten | stippel |
|---|---|---|---|---|---|---|
| b1 | leiding | 161,9 | 169 gepubliceerd (OSM 161,9) | -4,2% | 33 | nee |
| b2 | leiding | 213,5 | 209 gepubliceerd (OSM 213,5) | +2,2% | 654 | nee |
| b3 | leiding | 23,1 | geen (OSM 23,1) | n.v.t. | 110 | nee |
Totaal 398,5 km. Naden tussen de benen 0,00 km (b1 eindigt op het landfall waar b2 begint; b2 eindigt waar b3 begint). Binnen b2 zitten 8 rechte
stukken van samen 12,8 km (0,58 / 0,24 / 0,12 / 2,15 / 2,37 / 4,63 / 2,48 / 0,25 km), binnen b3 twee van samen 0,35 km: ontbrekende OSM-ways van een
bestaande ondergrondse leiding, allemaal < 5 km, dus geen stippel en geen bevinding.

**Toelichting.** Doorgetrokken leiding, geen stippel, geen vlucht, geen haven-aanloop, geen kopie van een andere stroom. De km zijn die van de
OSM-ways (geen wegkm). Het script reproduceert de drie door de briefagent vooraf geschreven geojsons: zelfde puntverzameling, alleen 1-2 dubbele
beginpunten minder (33/654/110 tegen 34/656/112 punten), km identiek.
**Markers** (5, alle ankers uit §3): Forties Unity 0,001 km van de lijn, Cruden Bay-booster 0,01, Kinneil 0,003, Dalmeny-tankpark 0,25 en Hound
Point-steiger 0,22 km (laatste twee: anker op het terrein/de steiger, leidingeinde ernaast, binnen de 0,5 km-norm).
**Toets.** `toets_knikken`: 5 knikken >= 60 gr, 0 omkeringen, 0 terugloop; het in §2 verwachte keerpunt bij Kinneil is dus niet als omkering gemeld. Twee knikken in b3 zijn spikes in de OSM-vertices bij
Dalmeny (55.9763,-3.3724; R 72 m) en bij 55.9896,-3.6077 (R 16 m), drie in b2 (Cruden Bay-booster 57.3837,-1.8844; Aberdeenshire 57.19,-2.23);
leidingvertices, geen routeerfout. `toets_rechte_benen --min-km 5`: de stroom staat er niet in (geen been met omwegfactor 1,000).
`json.load` ok: versie 2, punt_formaat lonlat, modaliteit overal `leiding`, elk been >= 2 punten, 17,0 KB.
**Open (uit §7, ongewijzigd):** actueel volume 2024/25 niet gevonden (peiljaar 2016); Forties Unity-kop aannemelijk, één bron, offshore geen beeld;
offshore OSM 161,9 tegen 169 gepubliceerd; afnemers van Forties Blend niet gebrond (geen fase C); Kinneil-anker afgeleid van OSM plus beeld.
**Lessen.** (1) Een leiding bij way-id lezen is sneller dan een naam-filter: eerst alleen de ids van de node-blokken decoderen (lat/lon pas bij een
treffer) scheelt veel bij een 2 GB-extract; totaal 13,4 min, waarvan 11 min wachten op een weg-slot (de scan zelf 2,4 min). (2) De bake zelf (hecht_marnet route met
alleen --been-geojson) laadt het zeenet en de track-graaf en kost een halve minuut; er wordt niets gerouteerd.
