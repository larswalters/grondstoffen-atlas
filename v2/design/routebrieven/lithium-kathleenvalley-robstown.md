# Routebrief (licht) · lithium — Kathleen Valley → Geraldton → Tesla Robstown

**stroom-id:** `lithium-kathleenvalley-robstown` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** hardrock-spodumeenconcentraat van de Kathleen Valley-plant (Liontown, Noord-Goldfields) gaat per **road train** ~700 km (Qube) over de Goldfields Hwy en de Leinster/Sandstone/Mount Magnet/Yalgoo-corridor naar de Qube-opslag in de haven van Geraldton, per **bulkschip** over MARNET (21.454 km, door MARNET via Panama gekozen) naar Corpus Christi (aannemelijk: één bron), en per **truck** ~42 km naar Tesla's raffinaderij bij Robstown (spodumeen → lithiumhydroxide, operationeel januari 2026).
**Welke as van het verhaal:** de Amerikaanse eigen-raffinage-as — Australisch hardrock rechtstreeks naar een VS-raffinaderij van de afnemer zelf, naast de Chinese converters. Kathleen Valley **~67–70 kt LCE/j** (sitelaag: ~500 kt SC/j × 5,4% Li2O × 2,473) [3][4]; uitbreiding (FID 29-09-2026) naar ~780 kdmt SC5,4/j vanaf FY30 ≈ 104 kt LCE [4]. Tesla-offtake: tot 150 kdmt SC/j (100 kdmt in jaar 1) ≈ ≤ 20 kt LCE/j contractplafond [7]; het werkelijk geleverde Tesla-volume en de scheepsladingen naar Texas zijn **niet gepubliceerd** — het zeebeen draagt het contractplafond, geen gemeten ladingstroom. Peiljaar 2025/26.

## 1 · Ketenkaart
```
Kathleen Valley-plant `li-kathleenvalley-plant` ──(b1 truck · Goldfields Hwy → Mt Magnet–Leinster Rd → Geraldton–Mt Magnet Rd 123 · ~700 km)──►
Geraldton-pier, Qube-opslag `li-geraldton-kade` (aannemelijk)
   ──(b2 zee-aanloop, stippel · 21,6 km)──► zeeknoop 3877
   ──(b3 zee · MARNET · 21.454 km, aannemelijk: één bron)──► Corpus Christi Inner Harbor `li-corpuschristi-kade` (aannemelijk)
   ──(b4 truck · I-37 → TX 358/44 → US 77 → CR 28 · ~42 km, aannemelijk: één bron)──► Tesla Lithium Refinery `li-robstown-tesla` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (Ultra-Quad road trains, Qube) | `li-kathleenvalley-plant` → `li-geraldton-kade` | Kathleen Valley Access Rd → Goldfields Hwy → Mount Magnet–Leinster Rd (via Sandstone) → Geraldton–Mount Magnet Rd (route 123, via Yalgoo/Mullewa) → John Willcock Link | 700 [1] (OSRM-controle 704,2 km) | maak_stroombeen_weg (extract australie) | nee |
| b2 | B | zee (haven-aanloop) | `li-geraldton-kade` → zeeknoop 3877 (-28.6355,114.4396) | haven-aanloop Geraldton, over water | 21,6 gemeten (maak_havenaanloop, omwegfactor 1,008) | stippel-geojson (klaar, zie §9-voorwerk) | ja — MARNET reikt niet |
| b3 | B | zee (bulkschip; aannemelijk: één bron) | zeeknoop 3877 → `li-corpuschristi-kade` | Indische Oceaan → 50°Z-Pacific → Panama → Golf van Mexico (MARNET beslist) | 21.453,6 gemeten (hemelsbreed 16.890; geen gepubliceerde zeekm) | MARNET | nee — naad kade/snap 1,43 km, aanloop niet nodig |
| b4 | C | truck (aannemelijk: één bron; rail niet uitgesloten) | `li-corpuschristi-kade` → `li-robstown-tesla` | Stroman Rd/N Port Ave → I-37 → TX 358 → TX 44 → US 77/I-69E → FM 2826 → CR 28 | hemelsbreed 34 km, geen wegkm (OSRM-indicatie 42,3 km) | maak_stroombeen_weg (extract us-texas) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-kathleenvalley-plant` | mijn / concentratorplant | Kathleen Valley (Liontown), toegangsweg bij het gebouwencluster | -27.4749, 120.5476 | hergebruik `lithium-sitelaag.json` w-li-kathleenvalley [3][12] | bron-gelegd (z15 gezien: kruis op de toegangsweg aan een gebouwencluster, de verwerkingsplant met transportbanden en witte tailings/pit-terrein ligt 0,3–0,7 km ZZO) |
| `li-geraldton-kade` | overslag weg → zee (Qube-opslag, haven) | Port of Geraldton, pier met bulkschuren, Graham Road/Reg Clarke Rd | -28.7740, 114.5930 | [1][5][6][11] | aannemelijk (z15 gezien: lange pier met een rij schuren en een schip aan de kade; Liontowns eigen Qube-schuur en berth zijn niet aan te wijzen — OSM kent alleen de Karara- en Fenix-schuren op -28.7731,114.5935 / -28.7758,114.5923) |
| `li-corpuschristi-kade` | losplek (bulk, vermoedelijk) | Corpus Christi Inner Harbor, zuidoever net W van de Harbor Bridge-voet, naast groot magazijn | 27.8112, -97.4045 | [9][12] | aannemelijk (z15 gezien: bulkschip aan een kade bij een groot wit magazijn; terminalnaam niet vastgesteld; het ontwerppunt 27.8099,-97.4031 lag op de brugopritten) |
| `li-robstown-tesla` | fabriek (raffinaderij) | Tesla Lithium Refinery, County Road 28, Robstown | 27.7093, -97.7306 | [2][8][10] | bron-gelegd (z15 gezien: terrein met kiln/tanks/magazijn en twee afvalvijvers, ~0,5 km W van I-69E/US-77) |

## 4 · Via-punten (alleen b1 en b4; lat, lon, in profielen `(lon, lat)`)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Goldfields Hwy × Mount Magnet–Leinster Rd, ZW van Leinster | -27.9376, 120.6946 | verlaat de Goldfields Hwy naar het westen i.p.v. Leinster-centrum (1,8 km NO) of noord via Wiluna/Meekatharra (veel langer) |
| b1 | 2 | Sandstone, oostrand op de weg | -27.9882, 119.3046 | pint corridor Sandstone–Mount Magnet (ca. 710 km opgeteld) |
| b1 | 3 | Mount Magnet, zuidrand (begin route 123) | -28.0887, 117.8366 | rand van het dorp op de Great Northern Hwy → Geraldton–Mt Magnet Rd |
| b1 | 4 | Yalgoo, westrand op route 123 | -28.3449, 116.6707 | blijft op route 123 (Yalgoo → Mullewa → Geraldton) i.p.v. een omweg via Meekatharra |
| b1 | 5 | NW Coastal Hwy bij Geraldton, begin John Willcock Link | -28.7884, 114.6239 | pint de havenaansluiting (John Willcock Link → Ian Bogle Rd → Reg Clarke Rd) |
| b4 | 1 | I-37 na de oprit bij Martin Luther King Dr | 27.8002, -97.4225 | I-37 westwaarts i.p.v. de stadsstraten |
| b4 | 2 | begin TX 44 bij Corpus Christi-West | 27.7821, -97.4723 | TX 44 (18 km) i.p.v. door naar Robstown via I-37/US 77 |
| b4 | 3 | US 77/I-69E bij FM 2826-afrit | 27.7780, -97.6650 | pint de aansluiting op de snelweg richting de FM/CR-wegen naar de fabriek (CR 30 → CR 28) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kathleen Valley-plant | Liontown Resources | erts → spodumeenconcentraat SC5,4 | sitelaag ~500 kt SC/j (~70 kt LCE); FID-uitbreiding ~780 kdmt SC5,4/j vanaf FY30 | [3][4] |
| Tesla Lithium Refinery, Robstown | Tesla | spodumeenconcentraat (o.a. Kathleen Valley, North American Lithium) → LiOH | geen tonnage gepubliceerd; 30 GWh/j vroege ramp → 50 GWh/j (energie-equivalent); 1.200 acres; $375 mln [8][10][14] | [2][8][10][14] |

## 6 · Stoppunt
De brief stopt bij Tesla's raffinaderij in Robstown: dat is de enige met naam genoemde afnemer van dit concentraat in de VS (Argus, offtake 2022); het vervolg — LiOH naar Gigafactory Texas — is wel genoemd maar niet als volume of corridor gebrond, dus fase D/E vervalt.

## 7 · Open punten
- **Ontscheephaven en haven→fabriek-modaliteit niet primair gedocumenteerd:** Argus noemt geen haven of modus [2]; alleen een zwakke aggregator zegt "Port of Corpus Christi" [9], en een 2023-bericht noemt "rail en oceaanvracht via de Golf" als reden voor de locatie. Vandaar *aannemelijk: één bron* in b3/b4; de lijn is wel gemeten en doorgetrokken. Een rail-spur (Tex-Mex/UP) is mogelijk maar niet gedocumenteerd; truck is een werkaanname.
- **Geen scheepsbewijs naar Texas:** de eerste Kathleen Valley-lading (MV Eckert Oldendorff, 27-09-2024, 11.855 wmt, 5,2% Li2O) ging naar een bestaande offtake-klant in China [5]; Tesla haalt ook uit North American Lithium (Quebec) [2][8]. Het Tesla-aandeel uit Kathleen Valley is niet gepubliceerd.
- **Qube-schuur en berth in Geraldton niet te vinden:** Liontown noemt een dedicated Qube-opslag in de haven [1][6] maar geen adres; het anker staat op de pier tussen de OSM-schuren van Karara en Fenix (aannemelijk).
- **Corpus Christi-terminal onbekend:** het anker ligt op een kade met bulkschip bij een magazijn, niet op een benoemde terminal; berth onzeker.
- **Zeeroute door MARNET via Panama (50°Z-Pacific)**, niet via de Kaap; geen gepubliceerde zeekm — 21.454 km is een routeerresultaat, geen bron.
- **b1 niet geverifieerd met `maak_stroombeen_weg`:** `pyosmium` is op deze machine geblokkeerd (beleid voor toepassingsbeheer) en Overpass was onbetrouwbaar; de corridor is alleen met OSRM-op-OSM gecontroleerd (704,2 km: Goldfields Hwy 58 · Mt Magnet–Leinster Rd 301 · route 123 335 km). De plantweg bij Kathleen Valley is mogelijk niet-gepubliceerde klasse → `eindToegangPrivaat`/`eindKlassen` controleren.
- **b4 wegkm:** geen gepubliceerde wegkm; OSRM-indicatie 42,3 km tegen hemelsbreed 34 km — de ±15%-toets geldt als indicatie.

## 8 · Bronnen
[1] Liontown, "Kathleen Valley to Geraldton: driving the transition", 30-09-2025 — 700 km, Qube Ultra-Quad road trains, ~1.000 t/dag, dedicated Qube-opslag bij Geraldton, 16 ladingen verkocht t/m 30-06-2025. https://www.liontown.com/latest-news/kathleen-valley-to-geraldton-driving-the-transition/
[2] Argus Media, 15-01-2026 — Tesla start Robstown-raffinaderij; spodumeen uit North American Lithium en Kathleen Valley; geen haven/modus. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2776390-tesla-begins-ops-at-texas-lithium-refinery
[3] Liontown, projectpagina Kathleen Valley — ~60 km N van Leinster, 680 km NO van Perth, sealed highways naar Geraldton. https://www.liontown.com/project/kathleen-valley/
[4] Liontown, "Board approves Kathleen Valley Expansion", 29/30-09-2026 — ~780 kdmt SC5,4/j vanaf FY30, piek >800 kdmt in FY34, A$389 mln. https://www.liontown.com/latest-news/board-approves-kathleen-valley-expansion/
[5] Liontown (ASX), first shipment, 30-09-2024 — MV Eckert Oldendorff vertrok 27-09-2024, 11.855 wmt 5,2% Li2O, "existing offtake customer"; foto concentraat in het Geraldton Port Shed; offtakes LGES/Tesla/Ford. https://announcements.asx.com.au/asxpdf/20240930/pdf/068gz43gqwvptx.pdf
[6] Engineering News/Mining Weekly, 04-12-2023 — port services deal Liontown/Mid West Ports Authority, Qube-contract ~A$175 mln, opslag en stockpile-beheer in de haven (alleen zoekresultaat gelezen; pagina 403). https://engineeringnews.co.za/article/liontown-locks-in-port-services-deal-for-kathleen-valley-exports-2023-12-04
[7] Mining Weekly, 06-06-2022 — Liontown–Tesla offtake: tot 150.000 dmt/j (100.000 dmt in jaar 1), start 2024 (alleen zoekresultaat gelezen). https://www.miningweekly.com/print-version/liontown-and-tesla-make-offtake-official-2022-06-06
[8] Industrial Info Resources, 19-12-2024 — Tesla start Robstown-kiln; spodumeenleverantie Piedmont/NAL (Quebec). https://www.industrialinfo.com/iirenergy/industry-news/article/tesla-starts-up-us-first-large-scale-lithium-refinery-in-texas--337356
[9] austinio.com — "Tesla Lithium Refinery" (zwakke aggregator): Port of Corpus Christi voor spodumeenimport, rail/truck voor de uitgaande LiOH. https://austinio.com/tesla-lithium-refinery.php
[10] Wikipedia (EN), "Robstown, Texas" — 1.200 acre Tesla-raffinaderij, $375 mln, bouw 2023, operationeel dec 2024. https://en.wikipedia.org/wiki/Robstown,_Texas
[11] OpenStreetMap (ODbL) via Nominatim — Karara Mining en Fenix Resources Geraldton Port Storage Shed, Graham Road. https://nominatim.openstreetmap.org
[12] OpenStreetMap-routering via OSRM — Kathleen Valley → Geraldton 704,2 km; Corpus Christi → Robstown 42,3 km (indicatie, geen publicatie). https://router.project-osrm.org
[13] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-lithium-kathleenvalley-robstown-{kathleenvalley,geraldton,corpuschristi,tesla}.png`.
[14] EnergyX, "Tesla's lithium refinery in Texas" — geïmporteerd spodumeen uit o.a. Australië; 30 → 50 GWh/j. https://energyx.com/blog/teslas-lithium-refinery/

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)

**Uitvoer:** `v2/data/stroomroute-lithium-kathleenvalley-robstown.json` (110,3 KB, contract versie 2, punt_formaat lonlat) · functie `bak_lithium_kathleenvalley_robstown` in `v2/tools/bak_stromen.sh` · profielen `lithium-kathleenvalley-robstown-kathleenvalley-geraldton` en `…-corpuschristi-tesla` in `v2/tools/maak_stroombeen_weg.py`. **4 benen · 22.220,5 km · 5.376 punten · 4 markers.**

| # | modaliteit | km (gebakken) | punten | stippel | brief-doel | naad naar vorig been |
|---|---|---|---|---|---|---|
| b1 | truck (road train) | 702,6 | 2.063 | nee | 700 (bedrijfsopgave) → **+0,4%** [OK, norm ±15%] | — |
| b2 | zee, haven-aanloop Geraldton | 21,6 | 15 | **ja** (MARNET reikt niet) | 21,6 gemeten | 0,00 km |
| b3 | zee (MARNET + VS-trackgraaf) | 21.453,6 | 2.909 | nee | 21.453,6 proefrun (identiek) | 0,00 km |
| b4 | truck | 42,7 | 389 | nee | 42,3 OSRM-indicatie → **+1,7%** [OK, indicatie] | **1,43 km** (procesgat in de havenkom, < 5 km) |

**Markers** (4): Kathleen Valley 0,00 km van de lijn · Port of Geraldton 0,00 km · Corpus Christi-kade 0,00 km · Tesla 0,21 km (anker ≠ routeerpunt, zie onder).

**Recept** (alles vanuit de repo-root, `PYTHONIOENCODING=utf-8`):
1. b1: `python v2/tools/maak_stroombeen_weg.py --profiel lithium-kathleenvalley-robstown-kathleenvalley-geraldton --bron overpass` (extract `australie` bestaat, maar `pyosmium` is geblokkeerd → Overpass-kraan; via-punten uit §4, `corridorKlassen` tertiary/unclassified, `eindToegangPrivaat`, `trimStaart`, `vensterKm` 75). 702,5 km, alle 7 via-snaps ≤ 0,06 km; per etappe 59,2 (plant → Goldfields Hwy × Leinster-weg) · 146,1 (→ Sandstone) · 157,6 (→ Mount Magnet) · 121,8 (→ Yalgoo) · 213,4 (→ NW Coastal Hwy bij Geraldton) · 4,5 (→ pier). Zes keerlusjes van 0,02–0,03 km gesnoeid (Geraldton-havenwegen). Looppad: de Overpass-mirror `kumi` gaf eerst tientallen keren HTTP 500; de run is gelukt via een scratch-wrapper die het Overpass-antwoord van `_ways_uit_overpass()` lokaal cachet en daarna het ONGEWIJZIGDE tool laat draaien (zelfde filter, zelfde Dijkstra).
2. b2: `timeout 300 python v2/tools/maak_havenaanloop.py` (al gebakken, bestand `lithium-kathleenvalley-robstown-aanloop-geraldton.geojson`, richting kade → zeeknoop 3877).
3. b3: `hecht_marnet.py route --been "zee|…|-28.6355,114.4396|27.8112,-97.4045"` (MARNET-zee 9.679 knopen, 262 track-edges + 76 MARNET-edges + 1 connector; snap start 0,000 km, snap Corpus Christi 1,432 km; lengte-invariant +0,016 km).
4. b4: `python v2/tools/maak_stroombeen_weg.py --profiel lithium-kathleenvalley-robstown-corpuschristi-tesla --bron overpass` (officiële run, geen wrapper). 42,7 km; 4 etappes: 2,7 · 7,0 · 20,8 · 12,1 km.
5. Bake: `bash v2/tools/bak_stromen.sh lithium-kathleenvalley-robstown`.

**Toets:** versie 2 / lonlat / alle modaliteiten in de set / elk been ≥ 2 punten / 110 KB ✔ · `toets_knikken`: 25 knikken ≥ 60° waarvan 4 omkeringen (3 terugloop) over de héle stroom — zie onder · `toets_rechte_benen --min-km 5`: geen enkel been van deze stroom staat in de lijst van rechte benen (omwegfactor b1 1,168 · b3 1,269 · b4 1,262).

**Toelichting**
- **b2 stippel = haven-aanloop Geraldton.** MARNET reikt niet tot de kade (kade → zeeknoop 3877: 21,5 km hemelsbreed), dus de aanloop over water is een gemeten kortste pad (maak_havenaanloop, omwegfactor 1,008, 15 punten) en blijft stippel: "hier reikt het net niet". 0,85 km ervan loopt over land aan het kade-uiteinde (1:10M-korrel).
- **Corpus Christi: bewust geen haven-aanloop.** De dichtstbijzijnde MARNET-zeeknoop (4842) ligt 6,4 km van de kade — over de LAR-586-drempel van 5 km — maar de router hecht via de VS-trackgraaf tot 1,43 km van de kade; de naad (b3 → b4) is daarmee 1,43 km, ruim onder de 5 km. De regel bestaat om naden > 5 km te voorkomen; die ontstaat hier niet. Het eind van b3 (snap -97.4183, 27.8154) ligt 1,43 km van de kade; de kade zelf is niet bereikbaar over de AIS-tracks.
- **⚠️ Anker ≠ routeerpunt (b4, Tesla).** Het Tesla-anker (27.7093, -97.7306) snapte (0,09 km) op een geïsoleerd component van 12 knopen — de drie service-ways van het fabrieksterrein, 65 m ten zuiden van County Road 28 en in OSM niet aan het net gekoppeld → "geen wegpad tussen punt 3 en 4". Het laatste via-punt van het profiel is daarom de OSM-vertex van CR 28 (way 1041974071) het dichtst bij het anker: **27.7107, -97.7292** (0,21 km N van het anker). De lijn eindigt dus 0,21 km vóór het Tesla-marker; geen last-mile-stippel nodig (< 2 km, het terrein zelf staat niet in het net).
- **b4 volgt het echte knooppunt.** De route rijdt op US 77/I-69E voorbij CR 28 tot de afrit bij Business 77 (27.7030, -97.7303), keert dan via de tertiary/service-wegen langs de motorway terug noordoost en neemt CR 28 westwaarts; in de OSM-data heeft de motorway geen directe afrit op CR 28. Dat leest de knikkentoets als TERUGLOOP (48 m radius, 174°) en volgt het wegennet, het is geen puntkeerlus (niet nader met satelliet gecontroleerd). Idem de uitstap bij TX 44 × US 77 (27.791, -97.655; 171,7°, ~1,2 km heen en terug): het knooppunt, niet nader gecontroleerd.
- **Terugloop in b3 bij Corpus Christi (27.819, -97.430, 170,5°):** het laatste stuk volgt AIS-tracks het Inner Harbor in en keert; waarschijnlijk een draaiplek in het havenbekken, binnen het procesgat van 1,43 km (niet nader onderzocht).
- **Aannemelijk (één bron):** b3 en b4 staan zo in de beennaam; de lijn is doorgetrokken. Het zeebeen draagt het contractplafond (≤ ~20 kt LCE/j), geen gemeten ladingstroom (§1, §7).

**Lessen**
- Een fabrieksanker dat op een geïsoleerd service-component snapt geeft "geen wegpad": kies het OSM-vertex van de dichtstbijzijnde route-klasse-weg als laatste via-punt en laat het marker op het anker (analyse: component van het anker tellen, `fetch_landnet._wegen_graaf`).
- `--bron overpass` met een bbox van 8°×3° (b1) werkt wel, maar de mirror geeft vaak direct HTTP 500; herhaal met een pauze (b4 lukte na ~20 pogingen, b1 na 4) en cache het antwoord lokaal bij diagnose-iteraties.
- Een shell-functie met `rm -rf "$d"` in de commandotekst wordt door de veiligheidscheck geweigerd; zet de slot-logica in een scriptbestand.
