# Routebrief (licht) · olie — Kome/Doba (Tsjaad) → Tsjaad–Kameroen-pijpleiding → Kome Kribi 1 FSO (Kribi, Kameroen)

**stroom-id:** `olie-doba-kribi` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** Doba-blend ruwe olie uit de Doba-velden (Zuid-Tsjaad) vanaf het Kome-verwerkingsstation, per **leiding**
(TOTCO in Tsjaad, COTCO in Kameroen; 30", ~1.070 km, via Belabo naar de kust bij Kribi), door een onderzeese buis naar de
drijvende opslag/laadinstallatie Kome Kribi 1 (FSO) voor de kust van Kribi. De keten stopt bij de FSO.
**Welke as van het verhaal:** *de enige landinwaartse olie-uitvoer van Centraal-Afrika* — Tsjaad heeft geen kust en exporteert
bijna alles door één leiding naar het Kameroense Kribi. Volume ~134 kb/d (jan-apr 2026: 16,1 Mbbl in 120 dagen, eigen
berekening uit [1][4]; peiljaar 2026); naamcapaciteit 225-250 kb/d [3][6]; Kameroen int ~$1,32/vat transitvergoeding [1].

## 1 · Ketenkaart
```
Kome-verwerkingsstation `ol-doba-kome` (Doba-velden, Zuid-Tsjaad) ──(b1 leiding · Tsjaad–Kameroen-leiding,
   via Belabo, Yaoundé-oost en Kribi-kust · 1.077 km OSM-pad / ~1.070 gepubliceerd, doorgetrokken, 0 stippel)──►
   Kribi-kust 2.9081, 9.9008 ──(onderzeese buis ~9,7 km, deel van b1)──► OSM-einde buis / FSO-zijde `ol-kribi-fso`
   (Kome Kribi 1, ~11 km uit de kust) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Kome/Doba → Kribi-kust → OSM-einde onderzeese buis (FSO-zijde) | Tsjaad–Kameroen-pijpleiding (TOTCO/COTCO), "Oil Pipeline Chad to Kribi" | 1.070 (Wikipedia [2], Tchadinfos [4]); 1.080 (Business in Cameroon [1]); eigen OSM-som 1.077,0 = +0,7% / −0,3% [5] | OSM-ways 926239436 (742,0 km, extract tsjaad) + 199342881 (325,3 km, kameroen) + 257189942 (9,7 km, onderzees, kameroen), stikken op 0 m, één LineString | nee — volledig doorgetrokken |

Aannemelijk-opmerking: alleen het eindpunt (FSO-zijde) is aannemelijk, niet gezien (zie §3). Geen tweede been: het ketenontwerp had
een stippel b2 van ~3 km naar de FSO; de bindende toets schrapte die (eindpunt = OSM-einde buis).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-doba-kome` | kop van de leiding / verwerkingsstation (CPF) | Kome-CPF (Doba-velden, Zuid-Tsjaad) | 8.5304, 16.7958 | [5] OSM-startpunt way 926239436; [2][4] | bron-gelegd (z15 gezien: ommuurd terrein met tanks en procesinstallaties; het punt ligt op de zuidrand van het hek, kampementen en een landingsbaan ~1,5 km ONO) |
| `ol-kribi-fso` | einde: onderzeese buis richting SPM/FSO Kome Kribi 1 | OSM-einde onderzeese buis, FSO-zijde | 2.9260, 9.8149 | [5] OSM-einde way 257189942; [3][7] | aannemelijk (z14 gezien: open zee, niets zichtbaar — Esri toont geen schepen of boeien; FSO volgens Wikipedia 2.9019, 9.7931 [2], 3,6 km WZW, volgens MarineLink 2.9225, 9.8015 [7], 1,5 km W; alle drie binnen 4 km) |

Niet als anker gelegd: de landing aan de Kribi-kust (2.9081, 9.9008, z15: smalle kuststrook met dorpsbebouwing, geen terminal zichtbaar; pure waygrens,
geen overslag) en het vermelde "Kribi onshore processing facility" [7] (positie niet gevonden — §7).

## 4 · Via-punten (b1 is een gestikte OSM-lijn: geen routering; punten dienen als controle op de waygrenzen en op de corridor)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Belabo (leiding op 1,7 km, ketenkm 593) | 4.9272, 13.3145 | controle dat de gestikte lijn de corridor volgt [5] |
| b1 | 2 | waygrens 926239436 → 199342881 (grens Tsjaad-extract/Kameroen-extract-keten, ketenkm 742) | 4.5030, 12.0650 | exacte stikplek op 0 m, beide ways delen deze node [5] |
| b1 | 3 | passage Yaoundé-oost (op 12 km, ketenkm 841) | 3.9328, 11.4320 | controle [5] |
| b1 | 4 | kustovergang land → onderzees (waygrens 199342881 → 257189942, ketenkm 1.067) | 2.9081, 9.9008 | exacte stikplek op 0 m [5] |

Uitsluiten (dubbele mapping, parallelle ways die de som tot ~1.750 km opblazen): **197953902** (178,1 km, TOTCO, 8.5364,16.7892 → 7.5655,15.5376),
**198082553** (275,0 km, COTCO, 7.5655,15.5376 → 5.8886,13.8295), **1189390159** (219,2 km, 3.8829,11.3902 → 2.9081,9.9008), ook **198081296** (27,7 km, naamloos, Kome-omgeving) en 667015827 / 319544257 (losse stukken bij Belabo).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kome-CPF (Doba-velden) | veldoperator Doba (Exxon-erfenis; hier niet verder gebrond) | olie + water uit de velden → ruwe olie voor de leiding | niet gebrond | [2] |
| Kome Kribi 1 FSO + SPM | KMT JV / COTCO; Savannah Energy ~31% indirect | leiding-olie → opslag (~2,2-2,5 Mbbl) → VLCC-lading | leiding 225-250 kb/d; laden 40-50 kb/uur | [3][6][7] |

## 6 · Stoppunt
De brief stopt bij de FSO/SPM voor Kribi: de lading wordt daar op tankers geladen, en geen bron koppelt een lading of afnemer aan één
raffinaderij. Fase D en E vervallen; ook geen zeebeen, omdat er geen bestemming gedocumenteerd is.

## 7 · Open punten
- **FSO-positie alleen Wikipedia [2] en MarineLink [7]**; de OSM-buis eindigt 3,6 km oostelijker dan Wikipedia, 1,5 km dan MarineLink. De lijn eindigt waar het bewijs (OSM) eindigt; de SPM-jacket is een objectief klein doel dat Esri-satelliet niet toont.
- **Kribi onshore faciliteit** (genoemd in [7]) niet gelokaliseerd; de OSM-leiding loopt door tot de kust zonder terminal-object.
- **Geen vervolg na Kribi** — geen bron noemt een afnemer of bestemming van de lading; geen zeebeen getekend.
- **Passage Moundou en Ebolowa uit het ketenontwerp**: de gestikte lijn ligt ~52 km ZO van Moundou en ~51 km NNW van Ebolowa; de leiding gaat dus niet "door" die steden. Alleen Belabo (1,7 km) en Kribi (1,8 km) liggen aan de lijn.
- **Volume ~134 kb/d is eigen berekening** (16,1 Mbbl / 120 dagen) [1][4]; Savannah noemt 124 kb/d voor 2022 [3] (zoekresultaat). Capaciteit 225 (ketenontwerp) tegen 250 kb/d (Savannah-snippet [3]).
- **Lengte-verschillen in bronnen** (1.070 / 1.080 / 903+~170): de OSM-som 1.077,0 km valt binnen ±1% van alle drie.
- **Onderzees stuk (9,7 km)** is OSM-gemapt, geen tweede bron voor de exacte route in zee.
- De v1-checklist (`data/oil.js`, `design/olie.md`) en de olie-sitelaag bevatten geen Doba/Kribi-site: er is geen site-coördinaat om te hergebruiken.

## 8 · Bronnen
[1] Business in Cameroon, 03-06-2026 — 16,1 Mbbl jan-apr 2026, leiding 1.080 km, transitvergoeding $1,321/vat. https://www.businessincameroon.com/energy/0306-16269-chad-cameroon-pipeline-delivers-more-revenue-to-cameroon-as-oil-flows-rise
[2] Wikipedia, "Chad–Cameroon Petroleum Development and Pipeline Project" — 1.070 km (~890 km in Kameroen), TOTCO/COTCO, FSO ~18 km uit de kust op 2°54'7"N 9°47'35"E. https://en.wikipedia.org/wiki/Chad%E2%80%93Cameroon_Petroleum_Development_and_Pipeline_Project
[3] Savannah Energy — 31,06% indirect belang in het Cameroon Export Transportation System en de Kome Kribi 1 FSO; 30", 903 km Kameroense deel, nameplate 250 kb/d, FSO-opslag ~2,2-2,5 Mbbl, doorvoer 124 kb/d in 2022 (belang bevestigd op de pagina; leiding- en FSO-cijfers uit een zoekresultaat, niet op de pagina zelf gecontroleerd). https://www.savannah-energy.com/?p=9584
[4] Tchadinfos, 28-05-2026 — 16,10 Mbbl transit jan-apr 2026, >1.070 km waarvan 890 km in Kameroen, eind bij het offshore-terminal Kome-Kribi 1. https://tchadinfos.com/2026/05/28/pipeline-tchad-cameroun-122-milliards-fcfa-de-droits-de-transit-percus-par-le-cameroun-pour-les-4-premiers-mois-de-2026/
[5] OpenStreetMap (ODbL), lokale Geofabrik-extracts tsjaad + kameroen, eigen pyosmium-scan 2026-10-09: ways 926239436, 199342881, 257189942 (`man_made=pipeline`, `substance=oil`, operator COTCO) stikken op 0,0 m; som 1.077,0 km, 687 punten; ook de uit te sluiten parallelle ways. https://www.openstreetmap.org
[6] IFC-projectfiche Chad-Cameroon Petroleum Development and Pipeline Project (alleen als zoekresultaat gezien, niet geopend; capaciteit 225 kb/d komt uit het ketenontwerp).  https://disclosures.ifc.org/project-detail/SPI/4338/chad-cameroon-petroleum-development-and-pipeline-project
[7] MarineLink Ports, "Kome Kribi I" — 2.922543, 9.801545, ~11 km offshore, SPM-boei en FSO, VLCC-geschikt, KMT JV. https://ports.marinelink.com/ports/port/kome-kribi-i
[8] Esri World Imagery via `v2/tools/sat_check.py` — `sat-olie-doba-kribi-kome-cpf.png` (z15), `sat-olie-doba-kribi-kribi-landing.png` (z15), `sat-olie-doba-kribi-osm-eind.png` en `sat-olie-doba-kribi-fso-wiki.png` (z14, open zee).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-olie-doba-kribi.json` (13,5 KB, versie 2, lonlat) · **functie:** `bak_olie_doba_kribi()` in `v2/tools/bak_stromen.sh` · **titel:** Olie · Doba (Tsjaad) → Tsjaad–Kameroen-leiding → Kribi (Kome Kribi 1, Kameroen).

| # | modaliteit | been | km gemeten | brief | afwijking | naad | stippel |
|---|---|---|---|---|---|---|---|
| b1 | leiding | Kome-CPF → Belabo → Yaoundé-oost → Kribi-kust → onderzeese buis (3 OSM-ways) | 1.077,0 (687 punten) | 1.070 / 1.080 | +0,7% / −0,3% | n.v.t. (eerste been) | nee, volledig doorgetrokken |

Totaal 1.077,0 km, 2 markers (`ol-doba-kome` 8.5304,16.7958 · `ol-kribi-fso` 2.9260,9.8149), geen zee, geen haven-aanloop, geen MARNET.

**Recept.** `python v2/tools/maak_leidingbeen_olie_doba_kribi.py --schrijf` (nieuw script naar het patroon kirkuk_ceyhan, maar met de pure-Python pbf-lezer uit `wegscan_puur.py` omdat pyosmium geblokkeerd is): ways 926239436 (extract tsjaad, 377 nodes), 199342881 (309) en 257189942 (3, onderzees) op id gepakt, in deze volgorde gestikt; de naden zijn 0,0 m, de richting klopt (kop 0,00 km van het Kome-anker), de dubbele ways 197953902, 198082553, 1189390159 en 198081296 zijn niet gebruikt. Daarna `bash v2/tools/bak_stromen.sh olie-doba-kribi` (zwaar-slot). Uitvoer: `v2/build-cache/ais/graaf/olie-doba-kribi-leiding-chad-cameroon.geojson` (FeatureCollection, 1 LineString). Het script reproduceert de brief exact: 1.077,0 km en 687 punten.

**Toelichting.** Doorgetrokken omdat OSM de leiding volledig heeft (`man_made=pipeline`, `substance=oil`, operator COTCO), ook het onderzeese stuk van 9,7 km; daar is geen tweede bron voor. Het eindpunt is het OSM-einde van de buis; de FSO zelf ligt 1,5 (MarineLink) tot 3,6 km (Wikipedia) verderop en is niet gebakken: "aannemelijk" staat in de beennaam en in de markernaam, niet in de lijnstijl. Geen via-punten gebruikt (gestikte lijn, geen routering); de controlepunten uit §4 (waygrens 4.5030,12.0650 en kustovergang 2.9081,9.9008) liggen op de lijn (binnen 0,01 km).

**Toets.** Km binnen ±1% van beide gepubliceerde cijfers; geen naden (één been); json.load OK, versie 2, punt_formaat lonlat, modaliteit leiding, 687 punten, 13,5 KB; `toets_knikken.py`: 3 knikken 60–67 graden (R 332–792 m, op Belabo-Yaoundé-flanken), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py --min-km 5` markeert dit been niet. Markers liggen per constructie op het begin- en eindpunt van de lijn (0 m).

**Lessen.** (1) Een nieuw leidingscript hoeft pyosmium niet: `wegscan_puur.py` biedt `blobs/prim/fields/np_sint`; twee passen (ways op id, dan alleen de nodes van die ways via `np.isin`) kosten 75 s voor 134+223 MB pbf. (2) Het script is herbruikbaar voor elke OSM-leiding op way-id. (3) Open punten uit §7 blijven staan: FSO-positie, Kribi onshore faciliteit, geen bestemming/zeebeen.
