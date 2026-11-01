# Routebrief (licht) · Olie · Superior Terminal → Line 5 → Sarnia (Wisconsin → Michigan → Ontario)

**stroom-id:** `olie-superior-sarnia` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) ·
**status:** gebakken
**Keten in één zin:** Synthetische, zoete en lichte zure crude (West-Canada) **plus NGL** (geen zuivere ruwe olie) per **pijpleiding** (Enbridge **Line 5**, 30 inch, 1953)
van de Superior Terminal (Wisconsin) via het Upper Peninsula, Rapid River, de Straits of Mackinac (onderzees), Bay City en Marysville
naar het tankenpark op de oostoever van de St. Clair bij Sarnia (Ontario).
**Welke as van het verhaal:** Line 5 = de noordelijke Great Lakes-slagader naast Line 6 (`olie-hardisty-superior` eindigt bij dezelfde terminal; geen gedeelde km).
Jaarvolume: **540 kb/d** capaciteit (Wikipedia [1], peiljaar 2013, +50 kb/d uitbreiding); **werkelijke doorvoer niet gebrond**; lading synthetische, zoete en lichte zure crude plus NGL [1].

## 1 · Ketenkaart
```
Superior Terminal `ol-superior-terminal` (Wisconsin)
  ──(stippel 1,1 km · Superior Terminal-terrein, buis daar niet gekarteerd)──► OSM-leidingkop 46.6862,-92.0494
  ──(b1 leiding · Enbridge Line 5 · 1.022,9 km OSM (645 mijl = 1.038 km [1]); Rapid River, Mackinac, Bay City, Marysville)──►
Sarnia-tankenpark `ol-sarnia-terminal` (Ontario, oostoever St. Clair) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Superior Terminal → Sarnia-tankenpark | Enbridge Line 5 (Lakehead), ruwe olie + NGL | 645 mijl = 1.038 km [1][2]; OSM-gestikt **1.022,9 km (-1,5%)** + 1,1 km stippel kop | OSM-pipeline, 30 ways (`maak_leidingbeen_olie_superior_sarnia.py`) | alleen kop 1,1 km (terrein) |

Aannemelijk-status: geen. Route, eindplaats en lading staan bij meerdere bronnen gelijk [1][2][4][5][6]; alleen het volume en de eindafnemer zijn niet gebrond (§7).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-superior-terminal` | kop / breakout-terminal | Enbridge Superior Terminal (Wisconsin) | 46.6895, -92.0635 | letterlijk uit `olie-hardisty-superior.md` §3 [9]; Superior = begin Line 5 en 6 [1][2] | bron-gelegd (z15 hier nogmaals: tankenpark met tientallen ronde tanks in gewalde vakken, raffinaderij 0,5-1 km westelijk; punt op de rand van een tankvak) |
| `ol-sarnia-terminal` | eind van Line 5 / stoppunt | Sarnia-tankenpark, oostoever St. Clair (Ontario) | 42.9087, -82.4508 | laatste OSM-node van Line 5 (way 627763507) [7] + Esri z15 [8]; Line 5 eindigt bij Sarnia, tanks voor doorpomping naar Line 7 [1] | bron-gelegd (z15 gezien: tankenpark met tientallen tanks langs de oever, procesinstallatie direct zuidelijk; OSM-landuse eromheen heet "Shell Corunna Refinery" [11]; punt 5 m van het lijn-eind) |

Niet gebruikt: Nominatim "Enbridge Sarnia Terminal" 42.9498, -82.3725 (Modeland Road, 8 km NO; geen gekarteerde Line 5-aansluiting, §7); stadscentra.
Kop: het OSM-leidingbegin ligt 1,14 km oostelijker (46.6862, -92.0494, z15: moeras/bos tegen de oostrand van het tankenpark) dan het anker; geen OSM-way ertussen, dus **stippel "Superior Terminal-terrein"**.

## 4 · Via-punten
*Geen corridorkeuze: een pijpleiding volgt een aangelegde buis, de gestikte lijn is OSM-geometrie. Controle (afstand lijn tot plaats): Rapid River 1,7 km · McGulpin Point (Mackinac) 0,6 km · Marysville 0,5 km; Bay City 5,4 km (de lijn loopt om Saginaw Bay heen [1], klopt).*

## 5 · Verwerkingsknopen
*Geen marker: Rapid River (NGL-stripping en terugpersen), Lewiston (US-crude erin) en Marysville (aflevering aan Michigan/Ohio, Sunoco-leiding naar Toledo) zijn pompstations/afleverpunten op de buis, geen overslag naar een andere drager [1]. Volumes per knoop niet gebrond.*

## 6 · Stoppunt
De brief stopt op het tankenpark waar Line 5 in OSM eindigt: Wikipedia noemt Sarnia als eindpunt (leveringen aan Sarnia-raffinaderijen, rest per tank naar Line 7) [1], maar geen bron koppelt déze lading aan één met naam genoemde raffinaderij. Fase C/D/E vervallen.

## 7 · Open punten
- **Lading deels NGL:** Line 5 draagt crude (synthetisch, zoet, licht zuur) én NGL [1][4][6]; het aandeel is niet gebrond, de beennaam zegt "ruwe olie + NGL".
- **Volume niet gebrond:** 540 kb/d is de capaciteit uit 2013 [1], geen jaarlijkse doorvoer. De Enbridge-pagina uit de ontwerpstap gaf bij ophalen HTTP 404.
- **Juridische status 2026 onzeker:** SCOTUS 2026-04-22: de Michigan-zaak over het Mackinac-stuk blijft bij de staatsrechter (procedureel, geen uitspraak over sluiten) [4]; Bad River: uitspraak 2023 eist reroute of sluiting uiterlijk juni 2026, reroute-bouw begon feb. 2026 [5][6]; of de oude buis nog draait na juni 2026 is niet bevestigd. OSM tekent de bestaande lijn, niet de Bad River-reroute. Tunnel onder de Straits niet gebouwd [6].
- **Eind-anker:** de gekarteerde Line 5 eindigt op het tankenpark aan de oever bij Corunna/Sarnia-zuid (binnen OSM-landuse "Shell Corunna Refinery"), niet op de Enbridge-terminal aan de Modeland Road (42.9498, -82.3725; Nominatim) die als Sarnia Terminal bedoeld kan zijn. Of dit tankenpark een Enbridge-terminal is, is niet bewezen; de lijn eindigt waar het bewijs eindigt. Of de Shell-site nog crude raffineert is niet nagezocht.
- **Naden:** 30 ways, alle naden 0,0 km; langste segment 5,8 km = onderzees Mackinac-stuk (OSM tekent het, geen stippel); de St. Clair-oversteek zit in OSM. Eindanker 0,005 km van de lijn.
- **Parallelle strengen:** Mackinac heeft twee 20-inch leidingen [1]; de gestikte lijn volgt way 329360259, de dubbelganger 329360261 (zelfde coördinaten) is weggelaten.

## 8 · Bronnen
[1] Wikipedia, "Enbridge Line 5" (API-extract 2026-11-01) — 645 mijl, 30 inch, 540 kb/d (2013), Superior-Sarnia, Rapid River NGL, Mackinac, Marysville, Sarnia/Line 7, Bad River-uitspraak. https://en.wikipedia.org/wiki/Enbridge_Line_5
[2] Wikipedia, "Lakehead System" — Superior = oostelijk eind Lines 1-4/67 en begin Lines 5/6. https://en.wikipedia.org/wiki/Lakehead_System
[3] Enbridge, Line 5-pagina (startpunt van de ontwerpstap; ophalen 2026-11-01 gaf 404, niet gebruikt). https://www.enbridge.com/projects-and-infrastructure/public-awareness/line-5
[4] Michigan Public, 2026-04-22, SCOTUS-uitspraak (zaak blijft in staatsrechtbank; crude en NGL Superior-Sarnia). https://www.michiganpublic.org/environment-climate-change/2026-04-22/supreme-court-rules-for-michigan-in-its-fight-to-shut-down-an-aging-energy-pipeline
[5] Michigan Public, 2026-02-26, Bad River-reroute begonnen (24 feb. 2026). https://www.michiganpublic.org/environment-climate-change/2026-02-26/after-years-of-legal-wrangling-enbridge-begins-rerouting-pipeline-around-wisconsin-reservation
[6] CRS In Focus IN11798, 2026-01-23 — 645 mijl, crude + NGL, stand tunnel en Bad River-reroute. https://www.everycrsreport.com/files/2026-01-23_IN11798_ffb23e4648f28b063324a7556c1deabbddb1685a.html
[7] OpenStreetMap-bijdragers (ODbL), OSM-API per way-id: 30 ways `man_made=pipeline`, `substance=oil`, operator Enbridge, "Enbridge Lakehead Pipeline Line 5" (329777044 … 627763507), 2026-11-01; Overpass (private.coffee): Line 6B way 756293298 bij de oversteek.
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-olie-superior-sarnia-anker.png`, `-kop.png`, `-eind.png` (z15).
[9] Eigen brief `olie-hardisty-superior.md` §3 (anker Superior Terminal).
[10] Nominatim (OSM), zoekterm "Enbridge Sarnia Terminal" -> 42.9498, -82.3725 (alleen als open punt).
[11] OSM-landuse way 614086705 "Shell Corunna Refinery" en 161826997 "Shell Chemicals Sarnia" (Overpass 2026-11-01).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-olie-superior-sarnia.json` (51,0 KB, versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh olie-superior-sarnia` (functie `bak_olie_superior_sarnia`) · geometrie: `v2/build-cache/ais/graaf/olie-superior-sarnia-leiding-line5.geojson` (uit `maak_leidingbeen_olie_superior_sarnia.py`).

| # | modaliteit | km | punten | naad | beschrijving |
|---|---|---|---|---|---|
| 1 | leiding (stippel) | 1,1 | 2 | 0 | Superior Terminal-terrein (schematisch, geen OSM-way) |
| 2 | leiding | 1.022,9 | 2.474 | 0,01 | Enbridge Line 5 (ruwe olie + NGL), Superior naar Sarnia via Mackinac (OSM) |

Totaal 1.024,0 km, 2 markers: `ol-superior-terminal` (0,000 km van de lijn) en `ol-sarnia-terminal` (0,005 km van de lijn).

**Toets:** OSM-km 1.022,9 tegen 1.038 gepubliceerd = -1,5% (norm ±15%, hier OSM-lengte tegen de Wikipedia-leidinglengte van 645 mijl). Geen naad > 5 km (1,1 km kop is de stippel). `toets_rechte_benen.py --min-km 5` meldt dit been niet. `toets_knikken.py`: 4 knikken >= 60 graden, 0 omkeringen, 0 terugloop; drie zijn spikes van 28-49 m bij 45,79-45,84 N / -84,77 W (Mackinac-oversteek, OSM-way-overgang), één krappe bocht van 752 m bij 43,63 N / -83,99 W (Saginaw Bay); geen reparatie nodig. json.load, versie 2, punt_formaat lonlat, modaliteit alleen leiding, elk been >= 2 punten.

**Stippel (kop 1,1 km):** het OSM-leidingbegin ligt 1,14 km oostelijker (46,6862, -92,0494) dan het terminalanker; tussen die twee punten bestaat geen OSM-way (terrein), dus rechte stippel "eigen verbinding zonder net". Het leidingbeen zelf is doorgetrokken.
**Leiding:** 30 OSM-ways (`man_made=pipeline`, `substance=oil`, operator Enbridge) gestikt tot één LineString; alle naden 0,0 km. Het langste segment (5,8 km) is het onderzeese Mackinac-stuk; OSM tekent het, dus geen stippel. Alleen de ene van de twee parallelle 20-inch strengen is gevolgd.
**Geen** haven-aanloop, zeebeen, wegbeen, luchtbeen of gedeeld been: een keten van één leiding.

**Lessen:** (1) een volledig OSM-gedekte leiding is de ideale korte bak: één `--been-geojson` plus één kop-stippel, de tool voegt niets toe. (2) Het eindanker is het OSM-leidingeinde; of het een Enbridge-terminal is blijft open (§7). (3) Registerregel: sleutel `olie-ss`, centraal te registreren.
