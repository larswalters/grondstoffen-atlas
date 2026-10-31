# Routebrief (licht) · Zilver · Van Motheo → Trans-Kalahari → Walvis Bay (Namibië)

**stroom-id:** `zilver-motheo-walvisbay` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** koper-zilverconcentraat van de Sandfire Motheo-mijn (Ghanzi, Botswana; zilver als bijproduct in het koperconcentraat) per **truck** over de Trans-Kalahari-corridor (A3/A2 → grens Mamuno/Buitepos → Namibische B6 → Windhoek → B1 → B2) naar de **Walvis Bay-kade**, voor verscheping naar smelters wereldwijd. Eén truckbeen; stoppunt bij de kade.
**Welke as van het verhaal:** Kalahari Copper Belt → Atlantische kust, nieuw voor zilver in Afrika. FY25 (juli 2024 tot juni 2025): **2,0 Moz Ag contained ≈ 62 t Ag/j** (FY24 1,2 Moz ≈ 37 t; FY26-guidance 2,1–2,3 Moz ≈ 65–72 t), contained en niet payable [1]. Het aandeel dat via Walvis Bay gaat is niet gekwantificeerd. De keten is dezelfde weg als `koper-motheo-walvisbay`; alleen de grondstof is nieuw.

## 1 · Ketenkaart
Motheo-installatie `ag-motheo-laad` ──(b1 truck · Ghanzi-zuid → Mamuno/Buitepos → Gobabis → Windhoek → Okahandja → Karibib · hemelsbreed 825 km, geen wegkm; letterlijke kopie van koper-motheo-walvisbay b1)──► Walvis Bay-kade `ag-walvisbay-kade` ── stoppunt (geen gedocumenteerde afnemer)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ag-motheo-laad` → `ag-walvisbay-kade` | A3/A2 (Botswana) → grens Mamuno/Buitepos → B6 (Gobabis, Windhoek) → B1 → B2 (Okahandja, Karibib, Walvis Bay); Trans-Kalahari-corridor [4][5] | hemelsbreed 825 km, geen wegkm; de ±15%-toets is indicatie. Namibië-indicatie uit Wikipedia-sectielengtes 325 + 70 + 315 = 710 km [4]; Buitepos → A3-knoop 165 km [5]. Gemeten OSM-lengte van de kopie: 1.014,3 km [8] | **letterlijke kopie** van `v2/build-cache/ais/graaf/koper-motheo-walvisbay-weg-motheo-walvisbay.geojson` (profiel `koper-motheo-walvisbay-motheo-walvisbay` in maak_stroombeen_weg.py, extracts botswana + namibie); geen nieuw profiel | nee |

Geen zeebeen, geen haven-aanloop, geen afnemer: de brief stopt bij de kade (§6). De Walvis Bay-kade ligt 12,9 km van MARNET-zeeknoop 8084; dat is alleen relevant bij een toekomstig zeebeen (dan haven-aanloop, > 5 km) en hier niet nodig. Geen last-mile-been: het mijnanker staat op de verwerkingsinstallatie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-motheo-laad` | mijn / laadplek | Motheo Copper Mine, verwerkingsinstallatie (Sandfire) | -21.3325, 22.3049 | [2][6][8] | **bron-gelegd, hergebruikt letterlijk** uit `koper-motheo-walvisbay.md` §3 (`cu-motheo-laad`). Z15 opnieuw gezien (`sat-zilver-motheo-walvisbay-ag-motheo-laad.png`): het kruis ligt op het gebouwencluster van de verwerkingsinstallatie met erts- en concentraatstapels, de open pits liggen NO en de grote tailings-/opslagbekkens ZO |
| `ag-walvisbay-kade` | overslag / kade (stoppunt) | Walvis Bay-containerterminal, gereclameerd havenhoofd | -22.9500, 14.4860 | [9] | **bron-gelegd, hergebruikt letterlijk** uit `koper-sentinel-walvisbay.md` §3 (`cu-walvisbay-kade`). Z15 opnieuw gezien (`sat-zilver-motheo-walvisbay-ag-walvisbay-kade.png`): het kruis ligt op het havenhoofd met containerstapels en kranen; de exacte kade voor concentraat is niet gebrond, zie §7 |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Letterlijk uit `koper-motheo-walvisbay.md` §4; het geojson is al gebakken, dus de punten zijn ter controle. Lat, lon; eerste en laatste punt zijn de ankers.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ghanzi-zuid (A3/A2-knoop) | -22.0140, 21.5380 | zonder dit punt vindt het wegtool geen pad (de knoop ligt 45 km buiten een venster van 40 km); sluit de A3 noordwaarts naar Maun uit, kiest de A2 westwaarts [5] |
| b1 | 2 | Grens Mamuno (Botswana) / Buitepos (Namibië) | -22.2808, 20.0053 | enige grensovergang van de Trans-Kalahari [4][5] |
| b1 | 3 | Gobabis (B6) | -22.4493, 18.9674 | pint de B6 naar Windhoek; sluit de zuidelijke Botswana-routes uit [4] |
| b1 | 4 | Okahandja (B1/B2) | -21.9858, 16.9114 | knoop waar de corridor de B1 verlaat voor de B2; sluit de B1 noordwaarts uit [4] |
| b1 | 5 | Karibib (B2) | -21.9371, 15.8795 | pint de B2 via Usakos; sluit de weg via de kust (Swakopmund) uit [4] |

## 5 · Verwerkingsknopen
Geen: de Motheo-installatie (5,6 Mtpa, flotatie, 100% Sandfire [2]) is het begin van de keten. Het zilver gaat als bijproduct mee in het koperconcentraat (172.059 t concentraat in FY25 [1]) en blijft concentraat tot de kade.

## 6 · Stoppunt
De brief stopt bij de Walvis Bay-kade: Sandfire noemt alleen "smelters wereldwijd" en geen benoemde afnemer of bestemmingshaven [2]. Fase D en E vervallen.

## 7 · Open punten
- **Wegkilometers niet gebronnen:** hemelsbreed 825 km (berekend tussen de twee ankers), geen wegkm; de 710 km-som voor Namibië is een optelling van Wikipedia-sectielengtes [4]. De gemeten 1.014,3 km is een OSM-lengte, geen bedrijfsopgave; de ±15%-toets is indicatie.
- **Zilver is contained, niet payable:** 2,0 Moz is de inhoud in concentraat [1]; wat een smelter uitbetaalt is lager en niet gepubliceerd.
- **Jaarvolume Walvis Bay-deel:** niet gekwantificeerd. Mmegi (2023) zegt "primarily through Walvis Bay", spotmarkt, geen offtake-contract [3]; Sandfire meldde vijf verscheepte ladingen in Q4 FY25 [1].
- **Afnemer/bestemmingshaven en exacte kade:** niet gevonden; kopererts-kade (container of bulk) niet gebrond, anker is het containerterminal-havenhoofd.
- **Windhoek:** de router passeert de stad zonder via-punt; een bypass is niet geverifieerd (kopie van koper-motheo-walvisbay).
- **Dubbeling met `koper-motheo-walvisbay`:** geometrie identiek, andere grondstof. Geaccepteerd precedent (kobalt-raglan-sudbury). Geen overlap met `zilver-matsa-huelva` (andere Sandfire-mijn, 3,1 Moz Ag [1]).
- **Motheo-mijnpoort:** niet gekarteerd; de kopie heeft één keerpunt bij de plantstub (-21.32258, 22.30769).

## 8 · Bronnen
[1] Sandfire, June 2025 Quarterly Report, ASX 2025-07-29: p.5 Motheo contained silver FY24 1,2 Moz, FY25 2,0 Moz, 172.059 t concentraat, "five shipments sailed" in Q4 FY25; p.9 FY25 actual 2,0 Moz Ag [guidance 2,0]; p.10 FY26-guidance 2,1–2,3 Moz Ag, https://announcements.asx.com.au/asxpdf/20250729/pdf/06m7fv5blfhp03.pdf (pdf gelezen, cijfers geverifieerd)
[2] Sandfire, "Motheo Copper Operations": concentraat "containing a silver by-product", per truck naar Walvis Bay voor verscheping naar smelters wereldwijd, https://www.sandfire.com.au/operations/motheo
[3] Mmegi, "First production emerges from newest copper mine", 2023-05-19 (export "primarily through Walvis Bay"), https://mmegi.bw/business/first-production-emerges-from-newest-copper-mine/news
[4] Wikipedia, "Trans-Kalahari Corridor" (B2 35+290 km, A1 70 km, B6 315 km), https://en.wikipedia.org/wiki/Trans-Kalahari_Corridor
[5] Wikipedia, "A2 road (Botswana)" (Buitepos 165 km tot A3-knoop, 45 km ZW van Ghanzi), https://en.wikipedia.org/wiki/A2_road_(Botswana)
[6] OpenStreetMap/Nominatim, way 1425739599 "Motheo Copper Mine" (landuse=industrial), https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&osmid=1425739599
[7] Satellietblik `v2/tools/sat_check.py`, Esri World Imagery z15, 2026-10-31: `sat-zilver-motheo-walvisbay-ag-motheo-laad.png`, `sat-zilver-motheo-walvisbay-ag-walvisbay-kade.png` in `v2/build-cache/satcheck/`
[8] `koper-motheo-walvisbay.md` (§2–§4 en §9: profiel, via-punten, gemeten 1.014,3 km, 5.692 punten, 0 naden; bron-brief van de kopie)
[9] `koper-sentinel-walvisbay.md` §3 (kadeanker Walvis Bay-containerterminal)
[10] Haalbaarheidstoets `zilver-motheo-walvisbay` (2026-10-31): bindend een letterlijke kopie, twee markers, geen zeebeen, hemelsbreed 825 km, volume 62 t Ag contained

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)

**Bestand:** `v2/data/stroomroute-zilver-motheo-walvisbay.json` (versie 2, lonlat, 116,5 KB, 1 been, 2 markers). **Functie:** `bak_zilver_motheo_walvisbay` in `v2/tools/bak_stromen.sh`; geen eigen profiel in maak_stroombeen_weg.py (letterlijke kopie). **Titel:** Zilver · Motheo (Botswana) → Trans-Kalahari → Walvis Bay (Namibië).

| # | modaliteit | been | km gemeten | punten | stippel |
|---|---|---|---|---|---|
| b1 | truck | Motheo-installatie → Ghanzi-zuid → grens Mamuno/Buitepos → Gobabis → Okahandja → Karibib → Walvis Bay-kade (A3/A2 → B6 → B1 → B2); LETTERLIJKE KOPIE koper-motheo-walvisbay b1 | 1.014,3 | 5.692 | nee, doorgetrokken |

Totaal 1.014,3 km, 5.692 punten, 0 naden (één been; begint op -21.3325, 22.3049 en eindigt op -22.9500, 14.4860). Markers: `ag-motheo-laad` en `ag-walvisbay-kade`, beide 0,0 km van de lijn.

**Recept:** geen wegscan, geen slot voor de weg-pool. `bash v2/tools/bak_stromen.sh zilver-motheo-walvisbay` (zwaar-slot) met `--been-geojson "truck|…|$BEEN/koper-motheo-walvisbay-weg-motheo-walvisbay.geojson"` en twee `--marker`. Geen zeebeen, geen haven-aanloop, geen stippel, geen lucht.

**Toets.** Geen gepubliceerde wegkm: hemelsbreed 825 km, geen wegkm; de ±15%-toets is indicatie (1.014,3 km, omwegfactor 1,23; Namibië-deel 715,7 km tegen 710 km uit Wikipedia-sectielengtes). Naden: geen (één doorlopend been; grootste vertexafstand 7,3 km op een recht wegstuk). `toets_knikken`: 19 knikken, 1 omkering (161,5 graden op 18 m bij de plantstub -21.32258, 22.30769, de keerpunt bij de niet-gekarteerde mijnpoort), 0 terugloop. `toets_rechte_benen --min-km 5`: geen treffer voor deze stroom. JSON: versie 2, punt_formaat lonlat, modaliteit truck, 5.692 punten.

**Lessen / open.**
- Gedeelde geometrie met `koper-motheo-walvisbay` (andere grondstof, geaccepteerd precedent); Windhoek zonder via-punt, bypass niet geverifieerd.
- Zilver is contained (2,0 Moz FY25), niet payable; het Walvis Bay-aandeel, de afnemer en de exacte kopererts-kade zijn niet gebrond (zie §7).
- Wegkm blijft ongebronnen; de 1.014,3 km is een gemeten OSM-lengte.
