# Routebrief (licht) · Uranium — Urenco USA (Eunice, New Mexico) → Framatome Richland Fuel Fabrication (Washington)

**stroom-id:** `uranium-eunice-richland` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) ·
**status:** gebakken
**Keten in één zin:** verrijkt UF6 (productcilinders) van Urenco USA, Eunice (Lea County, New Mexico), per **truck**
(Roswell → Albuquerque I-40 → US-191 door de Navajo Nation en Utah → Moab → Spanish Fork I-15 → Boise I-84 →
Pendleton) naar de Framatome-splijtstoffabriek aan Horn Rapids Road, Richland (Washington) — stoppunt.
**Welke as van het verhaal:** de Amerikaanse Westkust-splijtstoflijn: de enige Amerikaanse verrijker levert aan de
enige splijtstoffabriek in het noordwesten, een truckreis van ~3 dagen [1]. Jaarvolume: Urenco USA levert gemiddeld
~300 productcilinders per jaar in totaal (Urenco, peiljaar 2022) [1]; sitelaag ~5.850 t U feed-equivalent/j
(schatting) [9]. Geen route-specifiek tonnage; indicatie-bovengrens ≈ 300 × ~1,5 t U ≈ 450 t U/j (eigen rekensom,
algemene 30B-specificatie, niet uit een routebron).

## 1 · Ketenkaart
```
Urenco USA / NEF `u-eunice-verrijking` ──(b1 D truck, aannemelijk: één bron · Roswell → Albuquerque (I-40) →
Chinle (US-191) → Bluff → Moab → Spanish Fork (I-15) → Boise (I-84) → Pendleton · OSRM ~2.650 km, geen wegkm)──►
Framatome Richland `u-richland-fabricage` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Urenco USA (Eunice) → Framatome Richland | NM-176/US-62 → Hobbs → Roswell (US-70/285) → I-40 West (Albuquerque, Gallup) → US-191 (Chinle, Bluff, Moab) → US-6/I-15 (Spanish Fork) → I-84 (Boise, Pendleton) → Tri-Cities | OSRM-indicatie circa 2.650 km over de gekozen via-punten, geen wegkm (hemelsbreed 2.074 km) [8]; Urenco: vertrek 20 mei, aankomst 23 mei 2022 [1] | maak_stroombeen_weg | nee — *aannemelijk: één bron, corridor niet gepubliceerd* |

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-eunice-verrijking` | verrijking (kop) | Urenco USA / National Enrichment Facility, Eunice | 32.4356, -103.0796 | [7][10] | bron-gelegd — letterlijk hergebruikt uit `uranium-eunice-columbia` (z15 gezien: cascadecomplex met hallen, bufferbekkens, omheining, "nuclear alley"); NM-176-aanloop 0,66 km |
| `u-richland-fabricage` | splijtstoffabricage (staart, stoppunt) | Framatome Richland Fuel Fabrication Facility, 2101 Horn Rapids Road, Richland | 46.3485, -119.3025 | [4][5][9] | bron-gelegd (z15/z16 gezien: omheind fabriekscomplex met hallen, wagenparkeerterrein en bufferplekken, ~260 m ten zuiden van Horn Rapids Road; identiteit via het adrespunt 2101 Horn Rapids Road 46.3510, -119.2964 dat 0,5 km oostelijker op de weg naast een klein gebouw ligt) |

## 4 · Via-punten (b1 — op de doorgaande weg; alle geprojecteerd met `projecteer_viapunten.py`, afstand tot de ruwe gok vermeld)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Roswell-noord, US-70/US-285 | 33.4396, -104.5232 | Roswell-bypass: pint de Hobbs–Roswell-keuze (630 m geprojecteerd) tegen een Carlsbad/Artesia-omweg |
| b1 | 2 | Albuquerque, I-40 West | 35.0838, -106.7508 | I-40 westelijk van de Rio Grande: keuze tegen US-550/Farmington (1,7 km geprojecteerd) |
| b1 | 3 | Chinle, US-191 | 36.1572, -109.5830 | pint US-191 door de Navajo Nation (Chambers–Chinle) tegen US-491/Shiprock en Kayenta (3,1 km geprojecteerd) |
| b1 | 4 | Bluff (UT), US-191 | 37.2831, -109.5519 | houdt de route op US-191 noordwaarts i.p.v. via US-160/US-163 (62 m) |
| b1 | 5 | Moab, US-191 | 38.5566, -109.5404 | enige doorgaande weg Bluff → Moab; pint de US-191/US-6-oversteek naar Wasatch Front (2,0 km) |
| b1 | 6 | Spanish Fork, I-15/US-6 | 40.1129, -111.6714 | I-15-knooppunt waar de Utah-route de Wasatch Front bereikt, vóór Ogden/I-84 (1,9 km) |
| b1 | 7 | Boise, I-84 | 43.5720, -116.2285 | I-84 door de Treasure Valley, pint de Idaho-corridor tegen I-80/US-93 (249 m) |
| b1 | 8 | Pendleton, I-84 | 45.6635, -118.7575 | laatste hoofdknoop vóór Tri-Cities (US-730/US-395 Umatilla–Kennewick); keuze I-84 boven I-82 (929 m) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Framatome Richland Fuel Fabrication Facility | Framatome | verrijkt UF6 → splijtstof (UO2-poeder, pellets, assemblages) | niet gevonden (~700 medewerkers, stad Richland, 2021) | [3][4] |

## 6 · Stoppunt
De brief stopt bij de splijtstoffabriek Richland: Urenco noemt alleen "a fuel production facility in Richland" [1]; Framatome
is de enige splijtstoffabricage daar [4], dus fase E (reactor/utility) vervalt — geen bron noemt een vervolgbestemming.

## 7 · Open punten
- **Corridor niet gepubliceerd:** Urenco noemt alleen vertrek/aankomst (20 → 23 mei 2022, ~3 dagen) en de plaats Richland [1]. De West-corridor over Albuquerque, US-191 en I-84 is het voorstel van de haalbaarheidstoets: een Las Vegas-route is 3.186 km (te lang voor 3 dagen), de gekozen route ~2.650 km; vrije OSRM-route 2.528 km (via Farmington/Cortez) is bewust niet gevolgd. Aannemelijk, niet bron-gelegd.
- **Bedrijfsnaam niet in de bron:** Urenco schrijft "fuel production facility in Richland" zonder Framatome; eindpunt volgt uit het enige splijtstofbedrijf in Richland [4]. Framatome-site niet opnieuw geraadpleegd (de URL gaf 404).
- **Jaartonnage route-specifiek ontbreekt** (zie kop); fabriekscapaciteit Framatome Richland niet gevonden; geen sitelaagregel `w-framatome-richland` in `uranium-sitelaag.json` — kandidaat voor centrale toevoeging (niet zelf aangepast).
- **Eunice-anker snapt op een geïsoleerd service-lusje** (`way/905682611`): service uitsluiten uit eindKlassen (profiel eunice-columbia, bak-noot).
- **Richland-adrespunt** 46.3510, -119.2964 ligt naast een klein gebouw; het fabrieksterrein ligt 0,5 km westelijker (z16). Eindtoegang tot het omheinde terrein is privaat: `eindToegangPrivaat` + `trimStaart`.
- Overlap: alleen de eerste ~0,7 km uit Eunice (NM-176) met `uranium-eunice-columbia` en `uranium-metropolis-eunice`; geen gedeeld been.

## 8 · Bronnen
[1] Urenco, "UUSA's 500th product shipment" (2022) — vertrek vrijdag 20 mei vanuit Eunice per long haul truck, aankomst maandag 23 mei bij "a fuel production facility in Richland, Washington"; gemiddeld 300 productcilinders per jaar. https://www.urenco.com/news/uusa/2022/uusas-500th-product-shipment
[2] WISE Uranium Project, Urenco USA enrichment plant — cilinder/UX-30-zendingen, capaciteitsgeschiedenis (3,7 → 5,7+ miljoen SWU/j). https://www.wise-uranium.org/eoples.html
[3] WISE Uranium Project, fuel fabrication/transport — vermeldt Framatome Inc. Richland nuclear fuel plant (TN-B1-transport tot 8% verrijking). https://www.wise-uranium.org/eopusaf.html
[4] Wikipedia, "Richland, Washington" — Framatome als werkgever "creating nuclear fuel" (~700 medewerkers, 2021). https://en.wikipedia.org/wiki/Richland,_Washington
[5] OpenStreetMap/Nominatim (ODbL) — 2101 Horn Rapids Road, Richland, WA 99352 = 46.3510, -119.2964 (way 616212142). https://nominatim.openstreetmap.org
[6] Wikipedia, "U.S. Route 191" — 2.660 km totaal, Navajo Nation, Bluff/Moab in Utah. https://en.wikipedia.org/wiki/U.S._Route_191
[7] Wikipedia, "National Enrichment Facility" — 8 km oost van Eunice, 32.4356, -103.0796. https://en.wikipedia.org/wiki/National_Enrichment_Facility
[8] OSRM demo-router (OSM) — Eunice → via-punten → Richland 2.650 km / 31,6 uur; vrije route 2.528 km. https://router.project-osrm.org
[9] `v2/design/uranium-sitelaag.json` — `w-urenco-eunice` ~9% wereld-SWU, ≈5.850 t U feed-eq/j; Richland ontbreekt.
[10] Eigen brief `v2/design/routebrieven/uranium-eunice-columbia.md` — Eunice-anker, NM-176 en service-lusje.
[11] Esri World Imagery via `sat_check.py` (z15/z16, live) — `v2/build-cache/satcheck/sat-uranium-eunice-richland-richland-z16.png` en `…-z15.png`; Eunice: `sat-uranium-eunice-columbia-eunice-nef.png`.
[12] Geofabrik-extracts (OSM, us-new-mexico, us-arizona, us-utah, us-idaho, us-oregon) via `projecteer_viapunten.py` — doorgaande-rijbaanprojectie van de via-punten.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-uranium-eunice-richland.json` (versie 2, lonlat, 405 KB) · functie `bak_uranium_eunice_richland` in `v2/tools/bak_stromen.sh` · profiel `uranium-eunice-richland-eunice-richland` in `maak_stroombeen_weg.py`.

| # | modaliteit | km | punten | stippel | naad |
|---|---|---|---|---|---|
| b1 | truck | 2.607,6 (wegscan 2.606,5) | 19.008 | nee (doorgetrokken, "aannemelijk: één bron" in de beennaam) | — (enig been) |

- **Km-toets:** brief geeft geen wegkm maar een OSRM-indicatie van ca 2.650 km; gemeten 2.606,5 km = -1,6% (ruim binnen ±15%, als indicatie). Hemelsbreed 2.074 km, omwegfactor 1,26.
- **Markers:** `u-eunice-verrijking` (32.4356, -103.0796) en `u-richland-fabricage` (46.3485, -119.3025), beide 0,0 km van de lijn. Plant → weg-aanloop 0,66 km (NM-176), weg → kade 0,35 km, last mile over tertiary 1,22 km: bevindingen, geen stippel.
- **Recept:** wegscan over zes extracts (us-new-mexico, -arizona, -utah, -idaho, -oregon, -washington), venster 70 km, refs I 40 / US 191 / I 15 / I 84, `eindKlassen` zonder service, `eindToegangPrivaat`, `trimStaart`. 31 keerlussen gesnoeid (2.612,7 → 2.606,8 km).
- **⚠️ Afwijking van de brief:** de eerste scan faalde met "geen wegpad tussen punt 6 en 7" (Spanish Fork → Boise): het 70-km-venster om de rechte lijn ligt in de Grote Zoutmeerwoestijn. Twee via-punten toegevoegd op de doorgaande I-84 (motorway-vertices via `projecteer_viapunten.py`): Tremonton (41.7095, -112.2032) en Burley (42.5688, -113.8008). De stadspunten zelf (Tremonton 41.7118 / Burley 42.5381) lagen op I-84 Business in het centrum en zijn niet gebruikt.
- **Knikken:** `toets_knikken.py` 30 knikken >= 60 graden, 0 omkeringen, 0 terugloop (meest spikes op afritten/knooppunten van 7-250 m). Spanish Fork-via-punt gaf een lus van 5,8 km die door het snoeien is verwijderd.
- **Stippel/aanloop/vlucht/leiding:** geen. Eindpunt = Richland, zoals het id belooft.
- **Lessen:** een via-punt-lijst uit een OSRM-haalbaarheidstoets is niet genoeg voor een venstergraaf bij een route die om een leeg gebied heen buigt (Grote Zoutmeer): zet dan een via-punt op de echte omweg-knoop (hier Tremonton/Burley). `projecteer_viapunten.py --refs` matcht ook "Bus"-routes: kies de motorway-vertex, niet het stadscentrum.

