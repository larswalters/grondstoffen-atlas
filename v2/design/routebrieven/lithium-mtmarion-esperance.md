# Routebrief (licht) · Lithium — Mt Marion → Port of Esperance (Australië)

**stroom-id:** `lithium-mtmarion-esperance` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat (typisch 5 % en 3,5 % Li2O) van de Mt Marion-mijn (MinRes / Ganfeng 50:50) gaat per road train
~347 km over de Coolgardie–Esperance Highway (NH94 → NH1, Harbour Road-bypass) naar de schuur van het Port of Esperance en via een gesloten
bandcircuit naar de shiploader van Berth 3. **De lijn eindigt bij die kade:** geen bron noemt de Chinese aanlandhaven, dus er is geen zeebeen.
**Welke as van het verhaal:** *de derde Westaustralische lithium-exporthaven naast Bunbury en Port Hedland* — Goldfields-hardrock dat niet
naar de westkust maar over de Goldfields-zuidroute naar de zuidkust gaat. Volume: **~75 kt LCE/j** (70–80; 500–600 kt SC/j), peiljaar 2025
[8]; DMS-installatiecapaciteit ~500 kt SC/j [1]. Heel Esperance voert >900 kt spodumeen per jaar uit (alle exporteurs) [5].

## 1 · Ketenkaart
```
Mt Marion-mijn `li-mtmarion-mijn` ──(b1 truck · mijnweg → NH94 (Coolgardie-Esperance Hwy) → Norseman → NH1 → Harbour Rd · 347 km OSRM,
370 km Wikipedia-hele-highway)──► Port of Esperance, Berth 3 `li-esperance-kade` ⏹ stoppunt (geen gedocumenteerde aanlandhaven)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (concentraat, road train) | `li-mtmarion-mijn` → `li-esperance-kade` | Mt Marion-mijnweg (tertiary, ~5 km) → Coolgardie–Esperance Hwy: NH94 (ref 94) Widgiemooltha–Norseman, NH1 (ref 1) Norseman–Salmon Gums–Gibson → Harbour Rd (bypass) → havenweg (Harbour Rd, service) | **geen gepubliceerde Mt Marion→kade-km.** Referentie: de highway is **370 km** (Coolgardie→Esperance, Wikipedia [2]; het stuk Coolgardie→mijnafslag valt eraf, de mijnweg komt erbij). OSRM **347,2 km** (348,5 via Harbour Rd) [9]; **hemelsbreed 313,8 km, geen wegkm**. ±15 % op 370 = 315–425: indicatie, geen norm. DWER: "approximately 4 hours" [4] | maak_stroombeen_weg (extract australie) | nee |

*Geen haven-aanloop en geen zeebeen: het ontwerp had er twee (kade→zeeknoop 2478 70,7 km; zeeknoop → Yangtze-monding), beide vervallen op de
bindende haalbaarheidstoets — zonder bron voor de aanlandhaven is een aanloop van 70 km zonder zee erachter een losse stippel in open water.*

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-mtmarion-mijn` | mijn / concentrator | Mt Marion (MinRes / Ganfeng 50:50), 70 km zuid van Kalgoorlie | -31.0750, 121.4480 | **hergebruik letterlijk** `w-li-mtmarion` uit `lithium-sitelaag.json` [8]; eigen z15-blik [11] | **bron-gelegd** (z15 gezien: kruis op de haul road tussen plantbebouwing/tanks en tailingsdam in het westen en de open dagbouwputten oost — binnen het mijnterrein, ~0,6 km van het procesblok) |
| `li-esperance-kade` | overslag / kade | Port of Esperance, Berth 3 (dolphin-berth met shiploader) | -33.8711, 121.9024 | Southern Ports: Berth 3 = "Iron ore and spodumene", loader aan de ijzererts-circuit [3]; DWER 2018: Mt Marion Shed 4 → "enclosed circuit to the Berth 3 shiploader" [4]; eigen z17-blik [11] | **bron-gelegd** (z17 = fijnste Esri-niveau, z18 "Map data not yet available": een pier met transportbandtrestle en witte shiploaderboom aan het hoofd, bandcircuit over het havenplateau; de enige dolphin-pier van de haven) |
| routeerpunt (geen anker) | einde wegbeen | havenweg bij de wortel van de Berth 3-pier | -33.8726, 121.9026 | OSM-service-way "Harbour Road" (way 375759203), 0,17 km van de kade [10] | de jetty zelf is geen weg: bij een kale snap eindigt het been hier |

*Shed 4 (het ontvangstschuur, volgens [4] naast Shed 5) is niet apart gelegd: welke van de grote schuren op het oostelijke havenplateau het is staat nergens — zie §7.*

## 4 · Via-punten (b1 — corridorkeuzes)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | NH94 net ten zuiden van de mijnafslag (Londonderry) | -31.1524, 121.4230 | pint het opdraaien **zuidwaarts** (Norseman/Esperance) i.p.v. noordwaarts naar Coolgardie/Kalgoorlie; op de trunk, niet op de mijnweg |
| b1 | 2 | NH94 bij Higginsville | -31.7146, 121.6916 | houdt de lijn op de trunk (ref 94) naast de zijwegen naar Kambalda en de parallelle Goldfields-spoorlijn |
| b1 | 3 | NH94 bij Iragul | -32.0445, 121.6797 | laatste punt vóór de NH94/NH1-knoop; buiten Norseman |
| b1 | 4 | NH1 ten zuiden van Norseman (Dundas) | -32.2626, 121.7706 | pint NH1 **zuidwaarts** i.p.v. de Eyre Hwy oostwaarts; buiten het dorp |
| b1 | 5 | NH1 bij Salmon Gums | -33.0703, 121.6815 | houdt de lijn op de doorgaande NH1 i.p.v. landbouwwegen |
| b1 | 6 | NH1 bij Scaddan | -33.4948, 121.7164 | idem, aanloop Esperance |
| b1 | 7 | Harbour Road (bypass, Chadwick) | -33.8462, 121.8866 | **corridorkeuze:** de highway eindigt volgens Wikipedia [2] op een rotonde met Harbour Rd, die als bypass naar de haven loopt; de OSRM-default (347,2 km) rijdt in plaats daarvan door Esperance (Norseman Rd → The Esplanade) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mt Marion DMS-concentrator | MinRes (operator) / Ganfeng 50:50 | erts → spodumeenconcentraat 5 % en 3,5 % Li2O (flotatie-installatie in aanbouw) | ~500 kt SC/j; 500–600 kt SC/j ≈ 70–80 kt LCE | [1][8] |
| Port of Esperance, Shed 4 → Berth 3 | Southern Ports (contract met MinRes' Process Minerals International: 5 jaar + 5 optioneel) | opslag in gesloten schuur → bandcircuit → shiploader | trial: schepen gem. 34.000 t (max 65.000 t), ~elke 27–28 dagen, 500.000 dmt/j [4] | [3][4][5] |

## 6 · Stoppunt
De brief stopt bij de Berth 3-kade: de bronnen noemen de haven, de schuur en de bandroute, maar geen enkele noemt de aanlandhaven of de Chinese afnemer (Ganfeng-converters liggen in het binnenland), dus er is geen zeebeen en fase D/E vervalt.

## 7 · Open punten
- **Chinese aanlandhaven/afnemer niet gedocumenteerd**; Argus noemt geen bestemming [7]. Daarom bewust geen zeebeen en geen aanloop (bindende toets).
- **Shed 4 niet individueel gelegd** — het ontvangstschuur van het wegbeen; waarschijnlijk in het schuurcomplex op het oostelijke plateau, niet vastgesteld.
- **Geen gepubliceerde Mt Marion→kade-km**; 370 km is de hele highway vanaf Coolgardie [2]; 347,2 km is eigen OSRM-routing op dezelfde OSM-bron.
- **Berth 3-gebruik is gedateerd**: de DWER-proef is van 2018 [4]; de berthingpagina [3] (ongedateerd) noemt spodumeen nog bij Berth 3, maar deelt de loader met ijzererts.
- **Mijnweg**: de weg van de plant naar NH94 is OSM-"unclassified"/"tertiary" (~5 km), dus de bake heeft corridorKlassen nodig; plant → weg kan een korte stub geven.
- **v1 nam Geraldton aan als exporthaven** (`data/lithium.md`) [12]; de bronnen hier tonen Esperance — v1 wordt niet aangepast.

## 8 · Bronnen
[1] MinRes, Mt Marion — https://www.mineralresources.com.au/our-business/lithium/mt-marion/ (50:50 JV Ganfeng, DMS ~500 kt SC/j, 5 % en 3,5 % Li2O, per road naar Esperance)
[2] Wikipedia, Coolgardie–Esperance Highway (370 km; NH94/NH1; Harbour Road als bypass naar de haven) — https://en.wikipedia.org/wiki/Coolgardie%E2%80%93Esperance_Highway
[3] Southern Ports, berthing facilities (Berth 3: iron ore and spodumene; dolphin; loader aan de ijzerertscircuit) — https://www.southernports.com.au/trade-with-us/trade-capability/our-services/berthing-facilities
[4] Southern Ports/MRL, DWER trial notification L5099, 19-11-2018 (Shed 4 → Berth 3 shiploader; Coolgardie-Esperance Hwy ~4 u) — gelezen via web.archive.org-kopie van https://www.der.wa.gov.au/images/documents/our-work/licences-and-works-approvals/material-change/L5099_Trial_Not_19112018_.pdf
[5] Shipping Telegraph, Port of Esperance secures long-term export deals (MinRes/PMI, >900 kt spodumeen) — https://shippingtelegraph.com/commodity-news/port-of-esperance-secure-long-term-export-deals/
[6] Southern Ports, Global Lithium exploring Port of Esperance (>4 Mt in vijf jaar, derde exporthaven) — https://www.southernports.com.au/news/global-lithium-exploring-port-of-esperance-opportunities
[7] Argus, Australia's Oct lithium loadings dip after record Sep (32.900 t Esperance) — https://www.argusmedia.com/es/news-and-insights/latest-market-news/2751915-australia-s-oct-lithium-loadings-dip-after-record-sep
[8] `v2/design/lithium-sitelaag.json` — `w-li-mtmarion` (-31.0750, 121.4480; ~140 kt SC/kwartaal begin 2025 → 500–600 kt SC/j ≈ 70–80 kt LCE, [B4] MinRes-kwartaalrapportages)
[9] OSRM (project-osrm.org), Mt Marion → havenweg: 347,17 km (348,46 km via Harbour Rd), opgevraagd 2026-10-09 — http://router.project-osrm.org
[10] OpenStreetMap (ODbL) via Nominatim reverse: NH94/NH1 `trunk`, Harbour Road `secondary`/`service`; mijnweg `unclassified`/`tertiary` — https://nominatim.openstreetmap.org
[11] Esri World Imagery via `sat_check.py` — `v2/build-cache/satcheck/sat-lithium-mtmarion-esperance-mijn-z15.png`, `…-haven-z16.png`, `…-haven-z17.png`, `…-berth3-crop.png`
[12] `data/lithium.js` / `data/lithium.md` — v1 `li-mt-marion` (Geraldton-aanname)
[13] Southern Ports, Port of Esperance (3 berths, 75 ha) — https://www.southernports.com.au/esperance

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Stroom:** `v2/data/stroomroute-lithium-mtmarion-esperance.json` (35,7 KB, versie 2, lonlat) · **totaal 350,4 km** · 1 been · 2 markers · functie `bak_lithium_mtmarion_esperance` (`bash v2/tools/bak_stromen.sh lithium-mtmarion-esperance`).

| # | modaliteit | km | naad | stippel | been |
|---|---|---|---|---|---|
| b1 | truck (doorgetrokken, gemeten) | 350,4 (weggeometrie 349,0 + 1,31 plant→weg + 0,15 weg→kade) | 0 | nee | vrachtwagen (road train) Mt Marion → Port of Esperance Berth 3 (mijnweg, NH94, Norseman, NH1, Harbour Road) |

- **Markers (2):** Mt Marion-mijn (-31.0750, 121.4480) en Port of Esperance Berth 3 (-33.8711, 121.9024); beide 0,0 km van de lijn.
- **Toets:** 350,4 km tegen 370 (hele highway) = -5,3 % en tegen OSRM 347,2 = +0,9 %: binnen ±15 %, maar 370 is geen Mt Marion-kade-km, dus een indicatie (hemelsbreed 313,8 km, omwegfactor 1,117). Geen naad. `toets_knikken`: 9 knikken >= 60 gr, 0 omkeringen, 0 terugloop (alle bij Harbour Road/havenrotondes bij Esperance en de mijnafslag, echte wegbochten). `toets_rechte_benen`: stroom niet gemeld.
- **Recept:** profiel `lithium-mtmarion-esperance-mtmarion-esperance` in `maak_stroombeen_weg.py` (extract australie, vensterKm 50, refs 94 / 1 / Coolgardie-Esperance Highway / Harbour Road, corridorKlassen tertiary+unclassified, trimStaart, eindToegangPrivaat, 7 via-punten uit §4 ongewijzigd, snaps <= 0,01 km behalve plant 1,31 en kade 0,15). Wegscan via `wegscan_puur.py` (pyosmium geblokkeerd, Overpass onbereikbaar), 174 s op de 953 MB pbf; uitvoer `v2/build-cache/ais/graaf/lithium-mtmarion-esperance-weg-mtmarion-esperance.geojson`.
- **Geen stippel, geen aanloop, geen zeebeen:** bewust (zie §2/§6): de Chinese aanlandhaven is niet gebrond.
- **Bevinding mijn-anker:** het anker (hergebruik `w-li-mtmarion`) ligt 1,31 km van het dichtstbijzijnde bereikbare wegnet (de OSM-mijnweg) en de eerste 5,04 km loopt over tertiary/unclassified; de lijn begint met een korte rechte plant→weg-verbinding (< 2 km, dus geen last-mile-been). Het eerste via-punt (Londonderry, op NH94) ligt 10,1 km verder.
- **Les:** een Westaustralisch road-train-been over NH94/NH1 vraagt `corridorKlassen` voor de mijnweg en geen extra via-punten; de Harbour Road-bypass-via bleef nodig (4,7 km vanaf Chadwick). Shed 4 en gebruik van Berth 3 blijven open (§7).
