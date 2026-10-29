# Routebrief (licht) · Koper · Motheo → Trans-Kalahari → Walvis Bay (Namibië)

**stroom-id:** `koper-motheo-walvisbay` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** koperconcentraat van de Sandfire Motheo-mijn (Ghanzi, Botswana) per **truck** over de Trans-Kalahari-corridor (A3/A2 → grens Mamuno/Buitepos → Namibische B6 → Windhoek → B1 → B2) naar de **Walvis Bay-kade**, voor verscheping naar smelters wereldwijd. Eén truckbeen; stoppunt bij de kade.
**Welke as van het verhaal:** Kalahari Copper Belt → Atlantische kust. FY25 (juli 2024–juni 2025): **52,3 kt Cu in concentraat** (172.059 t concentraat uit 5,52 Mt erts), peiljaar FY25 [2]. Het aandeel dat via Walvis Bay gaat is niet gekwantificeerd; Sandfire en Mmegi noemen Walvis Bay als exportroute [1][3].

## 1 · Ketenkaart
Motheo-mijn `cu-motheo-laad` ──(b1 truck · Ghanzi-zuid → Mamuno/Buitepos → Gobabis → Windhoek → Okahandja → Karibib · hemelsbreed 825 km, geen wegkm)──► Walvis Bay-kade `cu-walvisbay-kade` ── stoppunt (geen gedocumenteerde afnemer)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-motheo-laad` → `cu-walvisbay-kade` | A3/A2 (Botswana) → grens Mamuno/Buitepos → B6 (Gobabis, Windhoek) → B1 → B2 (Okahandja, Karibib, Walvis Bay); Trans-Kalahari-corridor [4][5] | hemelsbreed 825 km, geen wegkm; de ±15%-toets is indicatie. Indicatie uit gepubliceerde sectielengtes: Walvis Bay–Okahandja 325 + Okahandja–Windhoek 70 + Windhoek–Buitepos 315 = 710 km Namibië [4]; Buitepos–A3-knoop 165 km, die knoop ligt 45 km ZW van Ghanzi [5]. Wegtest (toets): 1.013,6 km, geen bron | maak_stroombeen_weg (nieuw profiel, extracts botswana + namibie) | nee |

Geen zeebeen, geen haven-aanloop, geen afnemer: de brief stopt bij de kade (§6). Geen last-mile-been: het anker staat op de verwerkingsinstallatie. Karibib → Walvis Bay (ca. 218 km, B2) valt geometrisch samen met het slot van `koper-sentinel-walvisbay` b2 en `kobalt-mutanda-walvisbay` b4; dit been is één eigen profiel (bindend), geen kopie, het kadeanker is hergebruikt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-motheo-laad` | mijn / laadplek | Motheo Copper Mine, verwerkingsinstallatie (Sandfire) | -21.3325, 22.3049 | [1][6][8] | **bron-gelegd** (z15 gezien: verwerkingsinstallatie met gebouwencluster, stapels en tailings-dam direct ten zuiden; de open pits (T3/A4) liggen NO, de grote opslagvijver ZO; zie [8]) |
| `cu-walvisbay-kade` | overslag / kade (stoppunt) | Walvis Bay-containerterminal, gereclameerd havenhoofd | -22.9500, 14.4860 | [9] | **bron-gelegd, hergebruikt letterlijk** uit `koper-sentinel-walvisbay.md` §3 (z15/z17: containerstapels en portaalkranen op het havenhoofd); de exacte kopererts-kade is niet gebrond, zie §7 |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Gegeven (lon, lat) in het profiel; hier lat, lon. Eerste en laatste punt zijn de ankers.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ghanzi-zuid (A3/A2-knoop) | -22.0140, 21.5380 | zonder dit punt vindt het wegtool geen pad (de knoop ligt 45 km buiten een venster van 40 km); sluit de A3 noordwaarts naar Maun uit, kiest de A2 westwaarts [5] |
| b1 | 2 | Grens Mamuno (Botswana) / Buitepos (Namibië) | -22.2808, 20.0053 | enige grensovergang van de Trans-Kalahari; Namibische kant -22.2812, 19.9977 [4][5] |
| b1 | 3 | Gobabis (B6) | -22.4493, 18.9674 | pint de B6 naar Windhoek; sluit de zuidelijke Botswana-routes (A2 via Kang, naar Gauteng) uit [4] |
| b1 | 4 | Okahandja (B1/B2) | -21.9858, 16.9114 | knoop waar de corridor de B1 verlaat voor de B2; sluit de B1 noordwaarts (Otjiwarongo) uit [4] |
| b1 | 5 | Karibib (B2) | -21.9371, 15.8795 | pint de B2 via Usakos; sluit de weg via de kust (Swakopmund) vanuit het noorden uit [4] |

## 5 · Verwerkingsknopen
Geen: de Motheo-installatie (5,6 Mtpa, conventioneel breken, malen en flotatie, 100% Sandfire [1]) is het begin van de keten; concentraat blijft concentraat tot de kade.

## 6 · Stoppunt
De brief stopt bij de Walvis Bay-kade: Sandfire noemt alleen "smelters wereldwijd" en geen benoemde afnemer of bestemmingshaven [1]. Fase D en E vervallen.

## 7 · Open punten
- **Wegkilometers niet gebronnen:** hemelsbreed 825 km, geen wegkm; de 710 km-som voor Namibië is optelling van Wikipedia-sectielengtes [4]. Motheo → Ghanzi-zuid heeft geen gepubliceerde lengte.
- **Windhoek:** de router passeert Windhoek op 0,4 km van het centrum; een bypass is niet geverifieerd en er staat bewust geen via-punt in de stad (golf 3/4: via-punten in steden kostten 25-40 km omweg).
- **Jaarvolume Walvis Bay-deel:** niet gekwantificeerd; 52,3 kt Cu is de totale FY25-inhoud in concentraat [2]. Mmegi (2023): "primarily through Walvis Bay", spotmarkt, geen offtake-contract genoemd [3].
- **Afnemer/bestemmingshaven:** niet gevonden; stoppunt is de kade.
- **Exacte kade in Walvis Bay:** container- of bulkterminal voor concentraat niet gebrond (erfenis van `koper-sentinel-walvisbay`).
- **Motheo-anker:** OSM-landuse (way 1425739599), op z15 op de installatie gezien; mijnpoort en toegangsweg tot het net niet gekarteerd (plantstub: één keerpunt in de wegtest).
- **Overlap:** laatste ca. 218 km (Karibib → Walvis Bay) deelt geometrie met twee bestaande stromen, bewust niet herhaald als kopie.

## 8 · Bronnen
[1] Sandfire, "Motheo Copper Operations" (Ghanzi District, 5,6 Mtpa, concentraat per truck naar Walvis Bay), https://www.sandfire.com.au/operations/motheo
[2] Sandfire, June 2025 Quarterly Report, ASX 2025-07-29 (Motheo FY25: 172.059 t concentraat, 52.284 t contained Cu, 58,3 kt CuEq, 5,52 Mt verwerkt), https://announcements.asx.com.au/asxpdf/20250729/pdf/06m7fv5blfhp03.pdf
[3] Mmegi, "First production emerges from newest copper mine", 2023-05-19 (export "primarily through Walvis Bay"), https://mmegi.bw/business/first-production-emerges-from-newest-copper-mine/news
[4] Wikipedia, "Trans-Kalahari Corridor" (B2 35+290 km, A1 70 km, B6 315 km), https://en.wikipedia.org/wiki/Trans-Kalahari_Corridor
[5] Wikipedia, "A2 road (Botswana)" (Buitepos 165 km tot A3-knoop, 45 km ZW van Ghanzi), https://en.wikipedia.org/wiki/A2_road_(Botswana)
[6] OpenStreetMap/Nominatim, way 1425739599 "Motheo Copper Mine" (landuse=industrial; -21.3324863, 22.3049363), https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&osmid=1425739599
[7] Wikipedia, "Ghanzi" (ligging, paved road naar Gaborone), https://en.wikipedia.org/wiki/Ghanzi
[8] Satellietblik `v2/tools/sat_check.py`, Esri World Imagery z14 en z15, 2026-10-29: `sat-koper-motheo-walvisbay-cu-motheo-laad.png` (z14), `sat-koper-motheo-walvisbay-cu-motheo-laad15.png` (z15), in `v2/build-cache/satcheck/`
[9] `koper-sentinel-walvisbay.md` §3 (kadeanker) + satellietbeelden `sat-koper-sentinel-walvisbay-cu-walvisbay-*.png`
[10] Haalbaarheidstoets `koper-motheo-walvisbay` (2026-10-29): bindend een profiel, via-punten, vensterKm 75, wegtest 1.013,6 km, snaps maximaal 0,42 km

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)

**Bestand:** `v2/data/stroomroute-koper-motheo-walvisbay.json` (versie 2, lonlat, 116,4 KB, 1 been, 2 markers). **Functie:** `bak_koper_motheo_walvisbay` in `v2/tools/bak_stromen.sh`; **profiel:** `koper-motheo-walvisbay-motheo-walvisbay` in `v2/tools/maak_stroombeen_weg.py` (extracts botswana + namibie, vensterKm 75, geen corridorKlassen of eindToegangPrivaat nodig). **Titel:** Koper · Motheo (Botswana) → Trans-Kalahari → Walvis Bay (Namibië).

| # | modaliteit | been | km gemeten | punten | stippel |
|---|---|---|---|---|---|
| b1 | truck | Motheo-installatie → Ghanzi-zuid → grens Mamuno/Buitepos → Gobabis → Okahandja → Karibib → Walvis Bay-kade (A3/A2 → B6 → B1 → B2) | 1.014,3 | 5.692 | nee, doorgetrokken |

Totaal 1.014,3 km. Naden: geen (één been; lijn begint op Motheo-anker en eindigt op het kadeanker). Markers: `cu-motheo-laad` (-21.3325, 22.3049) en `cu-walvisbay-kade` (-22.9500, 14.4860), beide 0,0 km van de lijn.

**Recept:** één wegscan met `wegscan_puur.py` (13 s scan, 1.013,6 km); segmenten Motheo → Ghanzi-zuid 128,5 · → Mamuno/Buitepos 169,4 · → Gobabis 110,3 · → Okahandja 276,6 · → Karibib 111,0 · → Walvis Bay 217,8 km; snaps 0,00 tot 0,42 km. Daarna `bash v2/tools/bak_stromen.sh koper-motheo-walvisbay` met `--been-geojson "truck|…"` en twee markers.

**Toets.** Geen gepubliceerde wegkm, dus de ±15%-toets is een indicatie: 1.014,3 km tegen hemelsbreed 825 km (omwegfactor 1,23, de Trans-Kalahari-lijn buigt via Ghanzi en Gobabis) en tegen de Namibië-indicatie 710 km uit Wikipedia-sectielengtes: Mamuno/Buitepos → Walvis Bay meet hier 110,3 + 276,6 + 111,0 + 217,8 = 715,7 km (+0,8% t.o.v. 710). Buitepos → A3-knoop meet 169,4 km tegen 165 km uit Wikipedia (+2,7%). `toets_knikken`: 19 knikken, 0 terugloop; de omkering van 161,5 graden ligt op 18 m bij de plantstub van Motheo (-21.32258, 22.30769), de verwachte keerpunt bij de niet-gekarteerde mijnpoort. Overige knikken zijn spikes van enkele tot tientallen meters op kruispunten. `toets_rechte_benen`: geen treffer.

**Lessen / open.**
- De overlap Karibib → Walvis Bay (217,8 km) met `koper-sentinel-walvisbay` b2 en `kobalt-mutanda-walvisbay` b4 is bewust een eigen profiel; de geometrie wijkt daardoor mogelijk op meters af van die stromen.
- Windhoek: er staat geen via-punt in de stad; de router kiest zelf de B1/B6-doorgang. Een bypass is niet geverifieerd.
- Het Walvis Bay-aandeel van het volume, de afnemer en de exacte kopererts-kade zijn niet gebrond (zie §7); de lijn eindigt op het hergebruikte containerterminal-anker.
- Wegkm blijft ongebronnen; de 1.014,3 km is een gemeten OSM-lengte, geen bedrijfsopgave.
- Procesles: `maak_stroombeen_weg.py` heeft gemengde regeleinden (CRLF en LF door elkaar); een parallelle agent kan bij een lees-schrijf-edit mijn profiel wissen (eerste poging verdween). Na de edit altijd met grep controleren.
