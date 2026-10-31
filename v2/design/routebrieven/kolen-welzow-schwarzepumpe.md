# Routebrief (licht) · kolen — Tagebau Welzow-Süd (bruinkool) → LEAG-Kohlebahn → Kraftwerk Schwarze Pumpe (Duitsland)

**stroom-id:** `kolen-welzow-schwarzepumpe` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** **bruinkool** (geen steenkool) uit de Lausitzer dagbouw Welzow-Süd (LEAG) gaat vanaf het kolenlager/de treinverlading aan de rand van de put per **werkspoor** (LEAG/ZEB-Kohlebahn) naar het kolenemplacement van Kraftwerk Schwarze Pumpe (LEAG, 2 x 800 MW); de band in de put en de transporten binnen de centrale zijn geen been.
Titel noemt het echte eindpunt (de Kohlebahn-aansluiting op het kolenemplacement, niet de ketels) en dat het bruinkool is: de bol kent nog geen bruinkool, centraal beslissen of dit onder `kolen` mag (zelfde vraag als Hambach).
**Welke as van het verhaal:** *tweede Duitse bruinkoolregio* — de laatste actieve groeve van Brandenburg voedt een centrale op 8 km hemelsbreed. Welzow-Süd **ca. 20 Mt ruwe bruinkool/j (capaciteit, LEAG-brochure 2014)** [1]; Schwarze Pumpe verbruikt bij vollast **36.000 t/dag = ca. 13 Mt/j (afgeleid, peiljaar 2014)** [1], deels uit Nochten; het aandeel Welzow-Süd is niet gepubliceerd. Peiljaar 2014, eenheid Mt kolen per jaar.

## 1 · Ketenkaart
```
Kolenlager + treinverlading Welzow-Süd `kolen-welzow-laad`
   ──(b1 spoor · LEAG/ZEB-Kohlebahn Welzow → Industriepark Schwarze Pumpe · router 12,3 km, hemelsbreed 8,1 km, geen spoorkm)──►
Kohlebahn-aansluiting kolenemplacement Kraftwerk Schwarze Pumpe `kolen-schwarzepumpe-kolenemplacement` ⏹ stoppunt (bunker ca. 1,2 km westelijker op hetzelfde emplacement)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-welzow-laad` → `kolen-schwarzepumpe-kolenemplacement` | LEAG-Kohlebahn (ZEB-werkspoor, OSM `Anschlussbahn Schwarze Pumpe`, operator ZEB, 25 t asdruk) [1][5][7] | **hemelsbreed 8 km, geen spoorkm** (router 12,3 km, verhouding 1,52, 38 edges, 73 punten, 0 bochten >=60 graden; geen gepubliceerde lengte: ±15%-toets is indicatie) | toets_spoorroute (1-op-1-net, geen via) | nee |

Fase C vervalt: beide ankers liggen op het werkspoor zelf (snap kop 0,02 km, staart 0,10 km). Geen zee, weg, leiding, lucht, haven-aanloop of kopie.
Geen fase D (centrale draait op de kool, geen product dat een bron verder volgt), geen E.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-welzow-laad` | mijn / laadplek | Kolenlager en treinverlading Welzow-Süd (LEAG), oostrand van de dagbouw | 51.5479, 14.2551 | [1][2][9] | bron-gelegd (z16 gezien: open lagerterrein met hallen en een laadtoren direct langs het werkspoor, put met bandbruggen west, bos oost; bronnen noemen "Kohlelagerplatz" en "coal loading station" zonder coördinaat). Het kandidaatpunt 51.5548,14.2553 (z15) ligt 0,8 km noordelijker op open spoor zonder verlading en is verlaten; Wikipedia-mijnpunt 51.5881,14.2331 ligt in de put en snapt 4,0 km van het net |
| `kolen-schwarzepumpe-kolenemplacement` | verwerker / losplek | Kohlebahn-aansluiting kolenemplacement Kraftwerk Schwarze Pumpe (LEAG), oostrand centrale | 51.5338, 14.3700 | [1][3][7][9] | aannemelijk (z16 gezien: enkelspoor lijn langs de oostrand van het centraleterrein, 1,2 km oost van de bunker bij het ketelhuis; de ontlaadplek zelf is niet aangewezen). Wikipedia-centralepunt 51.5361,14.3538 ligt bij de ketels en geeft een route van 22,5 km met uit-en-terug |

Hergebruik: geen bestaand anker (geen Lausitz-keten in sitelaag of markers; grep Welzow/Schwarze Pumpe: 0 treffers).

## 4 · Via-punten
Geen (bindend uit de haalbaarheidstoets). De route volgt het werkspoor zonder via: eerst zuidwaarts langs het verladingsterrein (51.540, 14.268), dan oostnoordoost over de Kohlebahn (51.548, 14.304), langs de top bij 51.5537,14.335, zuidwaarts naar de oost-west-lijn onder de centrale (51.5296, 14.34-14.36) en daar het emplacement op [9].
Er bestaat in OSM ook een boog ten noorden van de centrale naar dezelfde aansluiting; de router kiest de zuidelijke aanvoer. Geen corridorkeuze die ver uiteen loopt, dus geen via.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tagebau Welzow-Süd | LEAG | bruinkool → band → kolenlager → trein | ca. 20 Mt/j (2014); winning t/m 2030 volgens de-Wikipedia (2026) | [1][2] |
| Kraftwerk Schwarze Pumpe | LEAG | bruinkool → stroom (+ procesdamp) | 2 x 800 MW; 36.000 t kool/dag bij vollast; stilleggen uiterlijk eind 2038 | [1][3][4] |

## 6 · Stoppunt
De brief stopt bij de Kohlebahn-aansluiting op het kolenemplacement: de bruinkool wordt in de centrale verbrand tot stroom en er is geen volgende fysieke locatie van de lading; het laatste stuk naar de bunker (ca. 1,2 km, eigen terrein) is geen been.

## 7 · Open punten
- **Bruinkool is geen steenkool:** past alleen als de bol `kolen` ruim opvat; anders afkeuren centraal. Het stroom-id blijft staan.
- **Spoorkm niet gepubliceerd:** alleen hemelsbreed 8 km (router 12,3 km); de ±15%-toets is indicatie, geen norm.
- **Uit-en-terug uit de haalbaarheidstoets (omkering 51.4983, 14.3989) is vermeden, niet verklaard:** de voorgestelde eindankers (ketelhuis 51.5339,14.3504 resp. Einfahrt LEAG Kohle 51.5161,14.3717 — een private OSM-weg, geen spoor) geven 21,8 resp. 18,9 km met 2,4-6 km heen-en-weer, waarschijnlijk Kopfmachen of een OSM-koppeling die ontbreekt tussen aansluiting en bunkeremplacement. Daarom is het eindanker de aansluiting op de oostrand; de lijn eindigt waar het bewijs eindigt.
- **Ontlaadplek bij het ketelhuis niet doorgekoppeld in OSM;** het stuk emplacement ernaartoe (ca. 1,2 km) is niet getekend en niet gestippeld (< 2 km, eigen terrein).
- **Volume:** 20 Mt/j is capaciteit (2014), 13 Mt/j is afgeleid uit 36.000 t/dag bij vollast; werkelijke productie en het aandeel Welzow-Süd in Schwarze Pumpe (naast Nochten) zijn niet gepubliceerd gevonden. De dagbouw levert ook aan de Brikettfabrik/Veredlung in het Industriepark [1][2]; of dit emplacement die deelt, is niet gevonden.
- **Einddatum:** de-Wikipedia noemt (begin 2026) winning Welzow-Süd t/m 2030 en sluiting van de centrale uiterlijk 2038; alleen via Wikipedia [2][3].
- **Verladinglocatie** volgt uit satelliet en brochure (kolenlager langs de Kohlebahn), niet uit een coördinaat in een bron.

## 8 · Bronnen
[1] Vattenfall/LEAG, Welzow-Süd / Schwarze Pumpe Energy Site (factsheets, dec. 2014) — ca. 20 Mt/j; "coal loading station"; per trein naar de consumenten; Schwarze Pumpe vooral uit Welzow-Süd en Nochten, 36.000 t/dag. https://www.leag.de/fileadmin/user_upload/pdf-en/fb_standort_welz_pump_2014_engl.pdf
[2] de.wikipedia, Tagebau Welzow-Süd — tot 20 Mt/j, Förderband naar Kohlelagerplatz, daarvandaan per trein naar Schwarze Pumpe (bij piek 35 treinen/dag), winning t/m 2030. https://de.wikipedia.org/wiki/Tagebau_Welzow-S%C3%BCd
[3] de.wikipedia, Kraftwerk Schwarze Pumpe — 2 x 800 MW, kool uit het naburige Welzow-Süd, stilleggen uiterlijk eind 2038. https://de.wikipedia.org/wiki/Kraftwerk_Schwarze_Pumpe
[4] en.wikipedia, Schwarze Pumpe power station — 2 x 800 MW lignite, in dienst 1997/98. https://en.wikipedia.org/wiki/Schwarze_Pumpe_power_station
[5] de.wikipedia, Lausitzer Braunkohlerevier — Zentraler Eisenbahnbetrieb (ZEB), spoornet voor 25 t asdruk. https://de.wikipedia.org/wiki/Lausitzer_Braunkohlerevier
[6] OpenStreetMap, way 35778895 "Einfahrt LEAG Kohle" (highway=tertiary, access=private; geen spoor). https://www.openstreetmap.org/way/35778895
[7] OpenStreetMap-API (bbox 14.335,51.510,14.385,51.545), ways "Anschlussbahn Schwarze Pumpe" (operator ZEB, service=yard, usage=industrial). https://api.openstreetmap.org/api/0.6/map?bbox=14.335,51.510,14.385,51.545
[8] Haalbaarheidstoets keten kolen-welzow-schwarzepumpe (2026-10-31): anker- en routemeting, webcheck de.wikipedia.
[9] Esri World Imagery via `v2/tools/sat_check.py` (2026-10-31) — `v2/build-cache/satcheck/sat-kolen-welzow-schwarzepumpe-laad.png` (z15), `-verlading.png` (z16), `-kw-oost.png` (z16), `-bunker.png` (z16), `-kolenopslag.png`, `-kolenopslag2.png`, `-toets-keer.png`; route-geojson `spoorroute-kolen-welzow-schwarzepumpe-welzow-schwarzepumpe.geojson` (toets_spoorroute, BAKE_SUFFIX=-raw, --hoofd-km=1000).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
- **Bestand:** `v2/data/stroomroute-kolen-welzow-schwarzepumpe.json` (versie 2, lonlat, 1,9 KB) · functie `bak_kolen_welzow_schwarzepumpe` in `v2/tools/bak_stromen.sh` · **totaal 12,6 km, 73 punten, 1 been, 2 markers**.
- **Benen:** b1 spoor 12,6 km, doorgetrokken (geen stippel), LEAG/ZEB-Kohlebahn Welzow-Süd-lager → kolenemplacement-aansluiting. Router-uitvoer 12,3 km; de baker meet de geojson-lijn op 12,6 km (haversine 12,57); verschil is de rekenmethode van de bake, geen tweede route.
- **Km-toets:** brief geeft geen spoorkm (hemelsbreed 8,1 km, geen spoorkm), dus indicatie: verhouding 1,55 op de grootcirkel, in lijn met de eerder gemeten 1,52. Geen naad (één been). Markers 0,02 km (laad) en 0,10 km (losplek) van de lijn.
- **Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=51.5479,14.2551 --naar=51.5338,14.3700 --naam=kolen-welzow-schwarzepumpe-welzow-schwarzepumpe --hoofd-km=1000` (extracts de-brandenburg en de-sachsen) -> geojson `spoorroute-kolen-welzow-schwarzepumpe-welzow-schwarzepumpe.geojson` -> `bash v2/tools/bak_stromen.sh kolen-welzow-schwarzepumpe` (`--been-geojson` spoor, twee `--marker`).
- **Toetsen:** `toets_knikken.py`: 0 knikken, 0 omkeringen, 0 terugloop; `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom.
- **Stippel / aanloop / vlucht / leiding / kopie:** geen. Het stuk emplacement tot het ketelhuis (ca. 1,2 km, eigen terrein, niet doorgekoppeld in OSM) is niet getekend en niet gestippeld (< 2 km).
- **Lessen:** (1) een eindanker op de aansluiting aan de oostrand voorkomt de uit-en-terug van 2,4-6 km die de ketelhuis-ankers gaven; de lijn eindigt waar het bewijs eindigt. (2) De router-km is indicatie bij ontbrekende gepubliceerde spoorkm. (3) Open voor centraal: bruinkool onder `kolen`? Volume (20 Mt/j capaciteit 2014; aandeel Welzow-Süd in Schwarze Pumpe niet gepubliceerd); einde winning 2030 en centrale uiterlijk 2038 alleen via de-Wikipedia.
