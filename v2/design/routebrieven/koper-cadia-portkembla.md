# Routebrief (licht) · koper — Cadia-flotatieplant → Blayney → Port Kembla (Australië)

**stroom-id:** `koper-cadia-portkembla` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Titel:** Koper · Cadia-flotatieplant → Blayney (ontwatering) → No. 6 Jetty Port Kembla (Australië)
**Keten in één zin:** goud-koperconcentraat van Newmont Cadia Valley Operations (bij Orange, NSW) gaat als slurry per eigen leiding (~35 km) naar de ontwateringsfabriek bij Blayney, daarna per **spoor** (Main Western Line, Blue Mountains, Sydney-goederennet, Illawarra-lijn, ~364 km gemeten) naar No. 6 Jetty in Port Kembla (Hyrock/Port Kembla Gateway); stoppunt = de kade, geen zeebeen.
**Welke as van het verhaal:** *Australische kop-goud-keten buiten Queensland en Zuid-Australie*: Cadia 82 kt Cu in 2025 (87 kt in 2024), Newmont Q4 2025 Operating Statistics [1]; contained koper in concentraat, indicatie voor de lading.

## 1 · Ketenkaart
```
Cadia-flotatieplant `cu-cadia-plant` --(b1 leiding · eigen slurryleiding · ~35 km gepubliceerd, hemelsbreed 25,2 km · STIPPEL, geen OSM-way)-->
Blayney `cu-blayney-station` --(b2 spoor · Main Western Line → Illawarra-lijn · 363,8 km gemeten, hemelsbreed 185 km, geen spoorkm)-->
No. 6 Jetty Port Kembla `cu-portkembla-kade`  [stoppunt, geen zeebeen]
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Cadia-flotatieplant → Blayney | eigen slurryleiding Cadia–Blayney ("piped to a dewatering plant at nearby Blayney") [2][3] | ~35 gepubliceerd (oud, onemine/Mining Technology via zoekresultaat) [4]; hemelsbreed 25,2 | `--stippel "leiding|…"` | **ja**: geen OSM-way (pbf-scan australie: alleen APA-gasleiding en een 9 m-stukje) |
| b2 | A | spoor | Blayney → No. 6 Jetty Port Kembla | Main Western Line (Blayney, Bathurst, Lithgow, Penrith) → Sydney-goederennet (Strathfield, Sydenham) → Illawarra-lijn (Wollongong) → Port Kembla [5][6] | **hemelsbreed 185 km, geen spoorkm**; gemeten 363,8 | toets_spoorroute (BAKE_SUFFIX=-raw), één run, geen via | nee |

Beennaam b2: `trein Blayney → No. 6 Jetty Port Kembla (aannemelijk: één bron, Main Western Line en Illawarra-lijn)`.
Router b2 (BAKE_SUFFIX=-raw, 3.260.717 spoor-edges, hoofd-km 100, max-snap 10): 363,8 km over 821 edges, snap 0,31 km (Blayney) en 0,44 km (kade), 0 bochten >= 60 graden, verhouding 1,97 op de grootcirkel; passeert Bathurst (0,85 km), Lithgow (0,23), Penrith (0,10), Sydenham (0,73), Wollongong (0,38), Strathfield (2,33). Verhouding 1,97 is echt: de lijn omzeilt de Blue Mountains via Sydney. Geojson: `v2/build-cache/ais/graaf/spoorroute-koper-cadia-portkembla-blayney-portkembla.geojson`.
Geen zeebeen: de MARNET-zeeknoop ligt bij Sydney (8992, -33,8541/151,2116) op 74,0 km; niet gebruikt omdat de keten bij de kade stopt (anders >5 km haven-aanloop vereist). Geen afnemer genoemd.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-cadia-plant` | mijn + flotatieplant (kop b1) | Cadia concentrator, Cadia Valley Operations (Newmont) | -33.4673, 148.9925 | Wikipedia mijncoördinaat -33,467/148,993 [3]; Photon "Cadia Valley Operations" -33,4755/149,0052 ligt 1,3 km verder midden in Cadia East, niet gebruikt | bron-gelegd (z15 gezien: groot grijs plantcomplex met kolommen en bassins onder de open Cadia Hill-put met turkoois meer; nog 3 km Cadia East-terrassen zuidwaarts) |
| `cu-blayney-station` | overslag leiding → spoor (staart b1, kop b2) | Blayney station (Main Western Line) | -33.5275, 149.2541 | ontwerp + haalbaarheidstoets; spoorrun snapt 0,31 km | **onzeker voor de plant**: station, niet de filterfabriek |
| `cu-portkembla-kade` | kade/losplek (staart b2, stoppunt) | No. 6 Jetty, Port Kembla Gateway (Hyrock) | -34.4685, 150.9027 | Spantech-project Hyrock [7]; haalbaarheidstoets | bron-gelegd (z15 gezien: schip langszij de steiger in de Outer Harbour, vlak ten zuiden van de kolenterminal; spoorrun snapt 0,44 km) |

Kandidaat nieuwe CVO-ontwateringsfabriek (2016, oost van Blayney [8][9]): -33,5322, 149,2698 (witte hallen langs de spoorlijn op z15, 1,55 km ten ZO van het station); niet door een bron gelegd, dus **onzeker** en niet als anker gebruikt: hij ligt < 2 km van het station (geen last-mile-been). De oude fabriek (Maria Street, Blayney) is gesloten [8].
Hergebruik: geen bestaand anker (Cadia, Blayney en No. 6 Jetty staan niet in andere brieven; Dendrobium-anker -34,4647/150,8929 is BlueScope, niet gebruikt).

## 4 · Via-punten
Geen. Eén directe spoorrun (geen corridorkeuze die de router niet zelf goed neemt; alle sleutelplaatsen binnen 2,4 km, zie §2). Geen wegbeen, geen last mile.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Cadia concentrator + Mo-plant | Newmont (100%, sinds nov 2023) | erts → Cu-Au-concentraat (+ Mo-concentraat als bijproduct) | 82 kt Cu en 385 koz Au in 2025 | [1][2] |
| CVO-ontwateringsfabriek Blayney | Newmont | slurry → gefilterd concentraat, treinbelading | niet gevonden | [8][9] |
| No. 6 Jetty + 40 kt concentraatloods | Hyrock / Port Kembla Gateway | spoor → schip (Cadia, Northparkes) | 40 kt opslag (2006) | [7] |

## 6 · Stoppunt
De brief stopt bij No. 6 Jetty in Port Kembla: de bron noemt de kade als exportpunt voor Cadia-concentraat, maar geen bron noemt een afnemer, smelter of bestemming (fase B/C/D vervallen).

## 7 · Open punten
- **Jaarvolume:** 82 kt Cu in 2025 [1]. De Newmont-operatiepagina toont "Copper 11 Kt (Q2 2026)", vermoedelijk een kwartaalcijfer, niet gebruikt.
- **Blayney-anker = station, niet de filterfabriek:** coördinaat van de nieuwe CVO-fabriek niet gevonden; kandidaat -33,5322/149,2698 alleen op beeld, onzeker.
- **Leiding:** ~35 km gepubliceerd (oude bron, vermoedelijk nog geldig na de nieuwe fabriek van 2016, niet bevestigd) tegen 25,2 km hemelsbreed; geen OSM-way (pbf-scan australie, geen slurry, haalbaarheidstoets), dus b1 volledig stippel (25 van 389 km = 6,5% van de keten). Mo-plant haalt concentraat uit de leiding vóór Blayney en stuurt het terug [10]; niet getekend.
- **No. 6 Jetty:** de Spantech-bron is uit 2006 en noemt Cadia als Newcrest; of Cadia nu nog via Hyrock/No. 6 Jetty gaat is niet bevestigd, wel is de kade bron-gelegd met schip langszij.
- **Spoorkm niet gepubliceerd:** Wikipedia geeft geen km Blayney–Port Kembla; de +-15%-toets is een indicatie tegen hemelsbreed 185 km (verhouding 1,97 door Blue Mountains/Sydney).
- **Afnemer/smelter** niet genoemd; geen zeebeen, geen fase D.
- **Overlap:** laatste ~10 km (Illawarra-lijn, Coniston → Port Kembla) ligt op dezelfde rails als `kolen-dendrobium-portkembla` b1 (ander eindpunt), eigen run.
- **Id vs eindpunt:** id `…-portkembla` = werkelijk eindpunt (No. 6 Jetty, Port Kembla); geen afwijking.

## 8 · Bronnen
[1] Newmont, Q4 2025 Operating Statistics: Cadia copper 82 kt (2025), 87 kt (2024), gold 385 koz. https://s24.q4cdn.com/382246808/files/doc_earnings/2025/q4/generic/Newmont-Q4-2025-Operating-Statistics_Final.pdf
[2] Newmont, Cadia: concentraat "piped to a dewatering plant at nearby Blayney, then by rail to Port Kembla"; 100% Newmont, Cadia East panel caving. https://operations.newmont.com/australia/cadia
[3] Wikipedia, Cadia-Ridgeway mine (-33,467/148,993; Newmont operator). https://en.wikipedia.org/wiki/Cadia-Ridgeway_mine
[4] Onemine, "Cadia Hill Features The World's Largest Grinding Mill" (concentrator ~35 km van de pijpleiding/ontwatering in Blayney; via zoekresultaat, niet geopend). https://onemine.org/documents/cadia-hill-features-the-world-s-largest-grinding-mill
[5] Wikipedia, Main Western railway line (Bathurst, Blayney, Orange; Blayney-Harden-aftakking). https://en.wikipedia.org/wiki/Main_Western_railway_line
[6] Wikipedia, South Coast railway line (Coniston-aftakking naar Port Kembla, vracht naar Sydney-net). https://en.wikipedia.org/wiki/South_Coast_railway_line,_New_South_Wales
[7] Spantech, Hyrock Port Kembla: Port Kembla Gateway No. 6 Jetty, concentraat Cadia en Northparkes, 40 kt loods (2006). https://www.spantech.com.au/projects/hyrock-port-kembla-copper-concentrate-storage-facility-new-south-wales-pinkenba-370
[8] Central Western Daily, "Cadia facility marked for demolition" (oude Maria Street-fabriek 1998-2016, nieuwe 2016). https://www.centralwesterndaily.com.au/story/6543774/cadia-facility-marked-for-demolition-freeing-up-valuable-water-for-town
[9] Blayney Chronicle, "Cadia East approved" (nieuwe ontwateringsfabriek oost van Blayney, nieuwe leiding, trein naar Port Kembla). https://www.blayneychronicle.com.au/story/1084573/cadia-east-approved
[10] Newcrest, "Holy Moly(bdenum)" (Mo-plant op de leiding, via zoekresultaat). https://newcrest.com/holy-molybdenum
[11] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-koper-cadia-portkembla-cadiaplant.png` (z15), `-blayney15.png` (z15), `-kade.png` (z15), `-blayney.png`, `-cadia.png` (z14).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Bestand:** `v2/data/stroomroute-koper-cadia-portkembla.json` (40,7 KB, versie 2, lonlat) · **recept:** functie `bak_koper_cadia_portkembla` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh koper-cadia-portkembla`) · totaal **396,5 km · 2.054 punten · 3 markers**.

| # | modaliteit | km gebakken | km brief | naad | opmerking |
|---|---|---|---|---|---|
| b1 | leiding (stippel) | 25,2 | ~35 gepubliceerd, hemelsbreed 25,2 | 0 | rechte lijn, 2 punten, geen OSM-way |
| b2 | spoor | 371,3 | gemeten 363,8; geen gepubliceerde spoorkm | 0,31 km (snap Blayney) | vooraf gebakken geojson, 2.052 punten |

**Markers (3):** `cu-cadia-plant` 0,0 km van de lijn · `cu-blayney-station` 0,0 · `cu-portkembla-kade` 0,44 km (spoorsnap, anker ≠ routeerpunt).
**Toets:** geen naad > 5 km; `toets_knikken` 0 knikken, 0 omkeringen; `toets_rechte_benen`: alleen b1 (stippel, 1,001, met reden); modaliteiten {leiding, spoor}; elk been ≥ 2 punten.

**Toelichting stippel (b1):** de slurryleiding Cadia → Blayney is een eigen verbinding zonder net: de pbf-scan van australie vond geen `man_made=pipeline` met slurry. Hele been stippel met reden, 6,5% van de keten. De gepubliceerde ~35 km (oude bron) is langer dan de hemelsbreedte van 25,2 km; de lijn is schematisch recht en claimt geen tracé.
**Toelichting spoor (b2):** de bake telt de km opnieuw op de gestikte lijn (371,3) en dat wijkt +2,1% af van de 363,8 uit de routerrun; de brief geeft geen spoorkm, dus een indicatie, geen norm (verhouding 1,97 op de grootcirkel door de Blue Mountains-omweg via Sydney).
**Geen** zeebeen, haven-aanloop, kopie, vlucht of wegbeen: de keten stopt bij de kade. Stoppunt: geen bron noemt een afnemer of bestemming.

**Lessen:**
- De geojson van de spoorrun was al klaar (`BAKE_SUFFIX=-raw`); de bake was een functie van één stippel en één `--been-geojson`, zonder nieuwe routering.
- Blayney-anker is het station; de CVO-ontwateringsfabriek (kandidaat -33,5322/149,2698) blijft onzeker en ligt < 2 km, dus geen last-mile-been.
- Of Cadia nu nog via Hyrock No. 6 Jetty exporteert is niet bevestigd (bron uit 2006).
- Bijvangst: `bash -n v2/tools/bak_stromen.sh` gaf tijdens de run een syntaxfout bij een andermans functie midden in een edit; na afloop weer schoon.
