# Routebrief (licht) · PGM — Columbus → I-90 / I-76 → West Deptford (Verenigde Staten)

**stroom-id:** `pgm-columbus-westdeptford` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** PGM-rijke filter cake (Pd+Pt, 2E; ook Rh) per **truck** van het Columbus Metallurgical Complex
(Sibanye-Stillwater, Montana) over I-90, de Chicago-bypass (I-294), de Indiana Toll Road en Ohio Turnpike (I-80/90),
I-76 (Pennsylvania Turnpike) en US-322 naar de Johnson Matthey-raffinaderij, 2001 Nolte Drive, West Deptford (New Jersey) —
**stoppunt**; bestemming **aannemelijk: één bron voor de locatie** (zie §7).
**Welke as van het verhaal:** de Amerikaanse mijnproductie wordt toll-geraffineerd door één externe raffinadeur [3][4].
Volume: Stillwater + East Boulder samen 425.842 oz Pd+Pt returnable in 2024 en 427.273 oz in 2023 (TRS tabel 7) ≈ **13,2 t 2E/j**
(koz ÷ 32,15) [3]; plan 2025–2027 ~270 koz 2E/j ≈ 8,4 t [3]. Recycling-voeding (autokatalysatoren) komt erbovenop, niet gekwantificeerd.

## 1 · Ketenkaart
```
Columbus Metallurgical Complex `pgm-columbus-smelter` (smelter + base metal refinery → PGM filter cake)
  ──(b1 truck · I-90 → I-294 → I-80/90 → I-76 → US-322 · hemelsbreed 2.831 km, geen wegkm; OSRM 3.273–3.376 km)──►
JM West Deptford `pgm-westdeptford-jm` (PGM-raffinaderij, aannemelijk: één bron voor de locatie) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `pgm-columbus-smelter` → `pgm-westdeptford-jm` | I-90 (Billings, Sheridan, Rapid City, Sioux Falls, Albert Lea, La Crosse, Madison) → I-294 Tri-State Tollway (Chicago-bypass) → I-80/94 → Indiana Toll Road → Ohio Turnpike (I-80/90) → I-76 Ohio Turnpike → Pennsylvania Turnpike → PA-100/US-202/US-322 → Commodore Barry Bridge → Nolte Drive; aannemelijk: één bron voor de bestemming [1][3] | **hemelsbreed 2.831 km, geen wegkm**; OSRM 3.273 km (vrij: US-212 door MT/SD) en **3.376 km over de via-punten (I-90)** (eigen runs, indicatie); ±15%-toets (2.782–3.764) is indicatie | maak_stroombeen_weg — nieuw profiel (10 extracts, zie §4) | nee — beide uiteinden aan het wegnet (OSRM-snap 0 m) |

Beennaam: `Columbus Metallurgical Complex → JM West Deptford (I-90 → I-294 → I-80/90 → I-76 → US-322) (aannemelijk: één bron)`.
Geen zee-, spoor-, lucht- of leidingbeen. Geen last-mile-been: Nolte Drive ligt aan de openbare weg.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-columbus-smelter` | smelter + base metal refinery (laadplek, kop) | Columbus Metallurgical Complex (Sibanye-Stillwater), Columbus | 45.6330, -109.2400 | **letterlijk hergebruikt uit `pgm-stillwater-columbus` §3** [3] | bron-gelegd (daar z15; hier z15 opnieuw gezien: industrieterrein met gebouwen langs de spoorlijn, ten noorden van de landingsbaan, oostrand Columbus, I-90 ten noorden ervan) |
| `pgm-westdeptford-jm` | PGM-raffinaderij (losplek, staart) | Johnson Matthey, 2001 Nolte Drive, West Deptford NJ 08066 | 39.8180, -75.2067 | adres uit [1] §1.6 en [4]; OSM-adrespunt [8]; routeerbaar (OSRM-snap 0 m op Nolte Drive) | bron-gelegd (z15 gezien: kleine industriële bebouwing met lichte daken aan Nolte Drive, bos en Mantua Creek-moeras westelijk, tankenpark 400 m zuidoost; welk gebouw JM is, is niet aan te wijzen) |

Satellietbeelden: `v2/build-cache/satcheck/sat-pgm-columbus-westdeptford-jm.png`, `…-columbus.png` (z15, Esri).

## 4 · Via-punten (b1 — negen, allemaal óp de interstate; (lat, lon) hier, in het profiel (lon, lat); OSRM-routegeometrie, ligging op de weg 0–6 m)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | I-90 bij Sheridan (WY), noordwest van de stad | 44.8460, -106.9851 | houdt I-90 door Wyoming (vrij kiest OSRM US-212/US-14 door MT/SD) |
| b1 | 2 | I-90 oost van Rapid City (SD) | 44.1180, -103.0017 | I-90 door South Dakota, niet US-212 noordelijk |
| b1 | 3 | I-90 oost van Sioux Falls (SD) | 43.6092, -96.6478 | I-90 naar Minnesota (niet I-94 via Bismarck/Fargo) |
| b1 | 4 | I-39/I-90/I-94 bij Madison (WI), Beltline | 43.0397, -89.2744 | I-90 door Wisconsin, niet I-94 via Minneapolis |
| b1 | 5 | I-294 Tri-State Tollway, west van Chicago | 41.8579, -87.9197 | pint de Chicago-bypass (I-294/Borman), niet I-90 door de Loop (Kennedy); buiten het centrum |
| b1 | 6 | Indiana Toll Road (I-80/90) | 41.6665, -86.7306 | I-80/90 door Indiana, niet I-94 door Michigan |
| b1 | 7 | I-76 Ohio Turnpike-aftakking (bij Youngstown) | 41.1135, -80.8409 | I-76 naar de PA Turnpike, niet I-80 door Pennsylvania (alternatief: I-80 → I-81 → …) |
| b1 | 8 | PA Turnpike (I-76), Harrisburg-oost | 40.2151, -76.7818 | houdt de PA Turnpike naar het zuidoosten, niet I-81/I-78 |
| b1 | 9 | US-322 bij de Commodore Barry Bridge | 39.8423, -75.3849 | Delaware-oversteek: Commodore Barry (niet Walt Whitman/Ben Franklin via Philadelphia-centrum, niet Delaware Memorial) |

Chicago: geen via-punt in de stad. Geofabrik-extracts: us-montana, us-wyoming, us-south-dakota, us-minnesota, us-wisconsin, us-illinois, us-indiana, us-ohio, us-pennsylvania, us-new-jersey (us-delaware niet nodig).
Bak-agent: snap per via-punt toetsen (≤ 5 km, liefst < 100 m); `vensterKm` 100 (lang been met grote omwegen tussen via-punten).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Columbus Metallurgical Complex | Sibanye-Stillwater | Stillwater/East Boulder-concentraat + recycling → PGM-rijke filter cake (final BMR-product) | BMR 1.300 lb matte/uur; VS-mijnen 425.842 oz 2E (2024) | [3] |
| JM West Deptford | Johnson Matthey | filter cake (verzegelde emmers, ≤ 8 loten per zending) → raffinaat (Pt/Pd/Rh, sponge ≥ 99,95%) naar de rekening van Sibanye / JM | grootste raffinaderij voor rijke PGM-stromen (>5%) in Noord-Amerika, in bedrijf sinds 1983 (presentatie 2012) | [1][3][5] |

## 6 · Stoppunt
De brief stopt bij de poort van JM West Deptford: de raffinaadmetalen worden overgedragen op de rekening van de afnemer en gaan niet fysiek naar een gedocumenteerde volgende locatie [3]. Fase D/E vervallen.

## 7 · Open punten
- **Locatie is afgeleid:** de TRS 2025 noemt Johnson Matthey als ontvanger van de filter cake, maar geen locatie [3]; de 20-F noemt alleen "a third-party refiner". Het adres 2001 Nolte Drive komt uit het 2014-contract (looptijd t/m 2018) [1] en een JM-certificaat uit 2023 [4]; het persbericht 2021 verlengt de leveringsovereenkomsten zonder plaats [2]. Daarom **aannemelijk: één bron voor de bestemming**; JM heeft ook Royston (UK), maar het VS-contract is aan de VS-vestiging gebonden.
- **Modaliteit niet expliciet:** het contract noemt "carrier's receipt" en "sealed in pails" [1], geen truck of spoor; truck is afgeleid (kleine massa, verpakt per emmer). Express/koerier of een spoor-omlading is niet uitgesloten.
- **Km zijn geen wegkm:** hemelsbreed 2.831 km; OSRM 3.273 km (vrije route US-212) en 3.376 km over de via-punten; geen operator- of overheidsopgave voor dit traject. Gepubliceerd-getal in het profiel: 3.273 (haalbaarheidstoets), verwachting bak ~3.350–3.450 km.
- **Volume:** het ontwerpcijfer 14–15 t (460–490 koz) is niet teruggevonden; de TRS geeft 425.842 oz (2024) en 427.273 oz (2023) Pd+Pt returnable [3]. Het aandeel dat naar West Deptford gaat is niet los gepubliceerd; recycling komt erbij. Een secundaire bron voor 308.617 oz 3E in 2025 is niet geverifieerd.
- **USITC pub 5671** (noot 55: JM als toll-raffinadeur) is niet te openen (HTTP 403 vanaf deze machine) en alleen overgenomen uit het ontwerp, niet zelf gelezen.
- **Exacte ontvangstplek** op het JM-terrein niet aan te wijzen op deze korrel.

## 8 · Bronnen
[1] Stillwater Mining / Johnson Matthey, Master Global Supply Agreement + filter-cake-overeenkomst (SEC ex. 10.2, 2014): Facility 2001 Nolte Drive, West Deptford NJ; 100% van de filter cake; "sealed in pails"; looptijd 2014–2018. https://www.sec.gov/Archives/edgar/data/931948/000093194814000063/swc-09302014x10xqxexhibit102.htm
[2] Johnson Matthey, "Sibanye-Stillwater" (19-3-2021): pgm-supply- en refining-overeenkomsten verlengd, geen locatie. https://matthey.com/news/2021/sibanye-stillwater
[3] Sibanye-Stillwater, US PGM Operations Technical Report Summary (SEC ex. 96.1, effectief 31-12-2024): filter cake "despatched to Johnson Matthey"; concentraat per truck naar Columbus; tabel 7 productie 2023/2024; plan 270 koz/j. https://sec.gov/Archives/edgar/data/1786909/000178690925000015/sswuspgmops2025trs_final.htm
[4] Johnson Matthey, IATF 16949-certificaat 0399614 (heruitgegeven 11-5-2023): 2001 Nolte Drive, West Deptford NJ 08066, "Manufacture of Precious Metal Chemicals". https://matthey.com/documents/161599/415798/4051%20Johnson%20Matthey%20IATF%20Reissue%20052023%20.pdf/25e47c5c-5ab6-c9c7-a857-debdbf7b419a
[5] Johnson Matthey-presentatie 2012 (National Academies): West Deptford grootste rich-metals PGM-raffinaderij in Noord-Amerika, in bedrijf sinds 1983 (alleen als zoekresultaat gezien). https://sites.nationalacademies.org/cs/groups/pgasite/documents/webpage/pga_080355.pdf
[6] Rowan University, projectpagina Johnson Matthey: West Deptford-raffinaderij zuivert Pt/Pd/Rh uit voedingsstromen (zoekresultaat). https://engineering.rowan.edu/programs/chemical/rowanche/projects/matthey.html
[7] Vacatures "Process Engineer, West Deptford Refinery" (Johnson Matthey, 2026): raffinaderij actief (zoekresultaat). https://www.careerbuilder.com/job-details/process-engineer-refinery-west-deptford-nj--a51defba-1b9f-49f7-87f3-e5b8dea5b9de
[8] OpenStreetMap (ODbL): adrespunt 2001 Nolte Drive 39.8180, -75.2067. https://www.openstreetmap.org
[9] OSRM (router.project-osrm.org), eigen runs 2026-10-30: 3.273 km direct, 3.376 km via de negen via-punten; stappen met refs I 90 / I 294 / I 80 / I 76 / US 322. https://router.project-osrm.org
[10] Routebrieven `pgm-stillwater-columbus` en `pgm-eastboulder-columbus` (Columbus-anker, Montana-corridor).
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15): `sat-pgm-columbus-westdeptford-jm.png`, `sat-pgm-columbus-westdeptford-columbus.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

**Bestand:** `v2/data/stroomroute-pgm-columbus-westdeptford.json` (versie 2, `lonlat`, 503,6 KB, 24.553 punten, 2 markers). Functie `bak_pgm_columbus_westdeptford` in `v2/tools/bak_stromen.sh`, profiel `pgm-columbus-westdeptford-columbus-jm` in `v2/tools/maak_stroombeen_weg.py`.

| # | modaliteit | been | km (gemeten) | brief | naad | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | Columbus Metallurgical Complex → JM West Deptford (I-90 → I-294 → I-80/90 → I-76 → US-322) (aannemelijk: één bron) | **3.371,4** | geen wegkm: hemelsbreed 2.831; OSRM 3.273 (vrij) en 3.376 (via-punten) | — | nee |

Totaal 3.371,4 km, één doorgetrokken been, geen naad (enkel been), geen stippel, geen haven-aanloop, geen kopie.

**Recept:** `python v2/tools/wegscan_puur.py --profiel pgm-columbus-westdeptford-columbus-jm` (10 extracts: us-montana … us-new-jersey, 1,6 GB pbf, ruim 10 min; 329.843 ways in het venster, vensterKm 100, `eindToegangPrivaat`), daarna `bash v2/tools/bak_stromen.sh pgm-columbus-westdeptford`. Tussenuitvoer: `v2/build-cache/ais/graaf/pgm-columbus-westdeptford-weg-columbus-jm.geojson` (600,6 KB) en het scanlog `…-wegscan.log`.

**Toets:**
- Lengte 3.371,3 km tegen de toetswaarde 3.273 = +3,0% (OK); tegen OSRM via de via-punten (3.376) −0,1%. De brief geeft geen echte wegkm: dit is een indicatie, geen norm.
- Alle tien via-punt-segmenten snappen op 0,00–0,09 km (≤ 0,09 km); geen via-punt verplaatst of verwijderd, geen omweg. Segmenten 269,5 / 413,8 / 535,2 / 686,6 / 214,4 / 125,6 / 525,1 / 436,0 / 145,7 / 19,8 km.
- Markers op 0,0 km van de lijn; plant → weg 0,09 km, weg → kade 0,01 km; first mile 1,14 km, last mile 0,48 km (kleine klassen, residential/service).
- `toets_knikken.py`: 22 knikken ≥ 60°, waarvan 1 terugloop (22 m, 175°) bij 41.1128,-80.8369, het via-punt bij de Ohio Turnpike-aftakking bij Youngstown (interchange/oprit); de rest zijn spikes van 3–70 m aan de uiteinden en bij knooppunten. Niet gerepareerd (een via-punt bijschuiven om de toets te halen is niet toegestaan); gemeld als bevinding.
- `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom.
- 24 keerlussen gesnoeid (3.371,5 → 3.371,3 km).

**Toelichting.** Geen stippel: beide uiteinden liggen aan het openbare wegnet (OSRM-snap 0 m; JM Nolte Drive, Columbus aan Pike Avenue/I-90). Geen zee-, spoor-, lucht- of leidingbeen. Bestand ruim boven 300 KB (503,6 KB; truckbeen over 3.371 km): centraal te vlaggen. Bestemming blijft aannemelijk (één bron voor het adres, contract 2014 en certificaat 2023); modaliteit truck afgeleid; exacte ontvangstplek op het JM-terrein niet aan te wijzen.

**Lessen.** Een enkel profiel over tien extracts kost een lange scan (us-illinois, -ohio en -pennsylvania elk 320–355 MB) maar de cache maakt een tweede run meteen klaar. Via-punten op de interstate-knooppunten (Madison Beltline, Tri-State Tollway, Indiana Toll Road) hielden de route op I-90/I-294/I-80-90/I-76 zonder omwegen; vrij had OSRM US-212 gekozen (3.273 km).
