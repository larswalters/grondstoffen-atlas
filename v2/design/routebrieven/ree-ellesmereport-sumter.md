# Routebrief (licht) · Zeldzame aardmetalen — Less Common Metals Ellesmere Port → Felixstowe → Charleston → eVAC Sumter (VS)

**stroom-id:** `ree-ellesmereport-sumter` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · Less Common Metals Ellesmere Port → Felixstowe → Charleston → eVAC Sumter (VS) (NdFeB-flakes, aannemelijk: beide havens zijn aannames)
**Keten in één zin:** NdFeB-legeringsflakes (HS 7206.90) van Less Common Metals (LCM, Ellesmere Port, VK) gaan per **truck** (M56, M6, A14) naar de containerhaven van Felixstowe, per containerschip over de Noord-Atlantische Oceaan naar Charleston (Leatherman Terminal) en per **truck** (I-26, I-95, US-521) naar de nieuwe magneetfabriek van e-VAC Magnetics in Sumter (SC). Stoppunt aan de fabriekspoort.
**Welke as van het verhaal:** VK als herkomst: Britse legering voor de eerste grote Amerikaanse sintermagneetfabriek. Volume: **onbekend als jaarcijfer**; ImportGenius toont twee zendingen flakes, 12,8 t (06-08-2026) en 5,2 t (29-06-2026), samen **0,018 kt NdFeB-legering** [1][2]. Ter vergelijking: eVAC Sumter 2,0 kt NdFeB-magneten per jaar nameplate, pad naar 12 kt [4].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** geen haven staat op de flake-B/Ls; Felixstowe en Charleston blijven, maar *aannemelijk: één bron / aanname* staat in de beennamen van b1, b2 en b3 en in §7. Titel noemt Felixstowe en Charleston. Eindpunt zoals het id belooft (Sumter).

## 1 · Ketenkaart
```
LCM-legeringsfabriek `ree-lcm-ellesmere` (Ellesmere Port)
  ──(b1 truck · M56 → M6 → A14 · hemelsbreed 324 km, OSRM 414,6 km, aannemelijk)──► Felixstowe, Trinity Terminal `ree-felixstowe-trinity`
  ──(b2 zee · Noordzee, Kanaal, Noord-Atlantische Oceaan · 6.932,2 km, aannemelijk)──► Charleston, Leatherman Terminal `ree-charleston-kade`
  ──(b3 truck · I-26 → I-95 → US-521 · hemelsbreed 118 km, OSRM 158,6 km)──► e-VAC Magnetics Sumter `ree-evac-sumter` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-lcm-ellesmere` → `ree-felixstowe-trinity` | M56, M6, A14 (Cheshire, West Midlands, Cambridgeshire, Suffolk) | hemelsbreed 324 km, geen wegkm; OSRM 414,6 km (indicatie, ontwerp 412,6) [11] | maak_stroombeen_weg (extract groot-brittannie) | nee — *aannemelijk: één bron* (haven) |
| b2 | B | zee | `ree-felixstowe-trinity` → `ree-charleston-kade` | Noordzee, Engels Kanaal, Noord-Atlantische Oceaan | 6.932,2 (eigen MARNET-meting [13]; snap Felixstowe 4,70 km, Charleston 1,67 km) | MARNET | aanloop: nee (4,7 km is onder de 5 km-grens) |
| b3 | D | truck | `ree-charleston-kade` → `ree-evac-sumter` | I-26, I-95, US-521 (SC) | hemelsbreed 118 km, geen wegkm; OSRM 158,6 km (indicatie) [11] | maak_stroombeen_weg (extract us-south-carolina) | nee |

Geen letterlijke kopie: Felixstowe → Charleston heeft geen eerder been. Het Charleston-anker is hergebruikt uit `lithium-hombremuerto-bessemercity` (kade-uiteinde van een ander been). Fase C bestaat niet; fase D is gebronnen: de B/L noemt e-VAC als consignee [1].

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-lcm-ellesmere` | legeringsfabriek (laadplek) | Less Common Metals, North Road, Ellesmere Port | 53.3055, -2.9334 | [7][10] OSM-fabriek (Nominatim 53.30546, -2.93337) | bron-gelegd (z15 gezien: wit-gedekte industriehal in een hallencluster aan de Mersey-oever, direct ZW van een tankenpark; ligt 53 m van een weg) |
| `ree-felixstowe-trinity` | overslag land → zee (containerterminal) | Trinity Terminal, Port of Felixstowe | 51.9639, 1.2926 | [12] ontwerp | bron-gelegd (z15 gezien: containerstapels en portaalkranen op de kade langs de Orwell-monding; punt ligt ca. 190 m achter de kadekant, site-niveau; 15 m van de weg) |
| `ree-charleston-kade` | overslag zee → land (containerkade) | Hugh K. Leatherman Terminal, North Charleston | 32.8392, -79.9352 | hergebruik letterlijk uit `lithium-hombremuerto-bessemercity.md` §3 (`li-charleston-kade`) | bron-gelegd (z15 hier opnieuw gezien: containerstapels, portaalkranen en schip aan de oostkade; 29 m van de weg) |
| `ree-evac-sumter` | fabriek (losplek, stoppunt) | e-VAC Magnetics, 840 Masatosagawa Dr, Sumter SC (Pocotaligo Industrial Park) | 33.8551, -80.3163 | [1][5] adres + ArcGIS-geocode (Nominatim kent het adres niet) | aannemelijk (z15 gezien: grote witte hallen met parkeerterrein en een waterzuiveringsbekken ten Z, deels onder wolk; 94 m van de weg) |

Zeeknopen: Felixstowe snapt op MARNET-knoop 4306 (51.9217, 1.2966, 4,70 km); Charleston op knoop 9371 (32.8542, -79.9358, 1,67 km). Dat zijn knopen, geen ankers.

## 4 · Via-punten (alleen landbenen met een corridorkeuze; profiel-coördinaten zijn (lon, lat))
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | M56/M6-corridor ten Z van Warrington | 53.3468, -2.4967 | pint de M56 → M6 zuidwaarts i.p.v. M62 → M1 (OSRM nearest 0,2 m; OSRM-route M56 21 km daarna M6) |
| b1 | 2 | M6 aan de noordrand van de West Midlands (Walsall) | 52.5614, -1.9835 | pint de M6 door de West Midlands i.p.v. M6 Toll of M1 (OSRM nearest 1,5 m) |
| b1 | 3 | M6/A14-overgang bij Catthorpe | 52.4025, -1.1697 | pint de overstap van M6 op A14 oostwaarts i.p.v. M1/M45 (OSRM nearest 0,2 m) |
| b1 | 4 | A14 ten NW van Cambridge (Girton-regio) | 52.2408, 0.0575 | pint de A14 Cambridge-bypass i.p.v. A428/M11 of door de stad (OSRM ref A14, nearest 3 m) |
| b3 | 1 | I-95, regio Santee | 33.3243, -80.5436 | pint de route via I-26 → I-95 noordwaarts i.p.v. de kust of US-17 (OSRM nearest 2,5 m) |
| b3 | 2 | US-521 ten Z van Sumter | 33.7381, -80.2075 | pint de laatste kilometers op US-521 vanuit het zuiden, buiten het centrum van Sumter (OSRM nearest 0,3 m) |
Alle punten liggen buiten stadscentra. Gewenste refs: b1 `["M56", "M6", "A14"]`, b3 `["I-26", "I-95", "US-521"]`. Eerste en laatste via zijn de ankers; first/last mile via kleine klassen (de ankers liggen 15-94 m van een weg).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LCM Ellesmere Port | Less Common Metals (USA Rare Earth, overname goedgekeurd) | REE-metaal → NdFeB strip-cast flakes | 2.500 t/j alle metalen en legeringen (10-K); ca. 1.400 t/j strip-cast NdFeB-legering (oude opgave, twee ovens van 600 kg) | [7][8][9] |
| e-VAC Magnetics Sumter | VAC (Ara Partners, sinds 2026 overnamebod Energy Fuels) | NdFeB-legering → sintermagneetblokken | 2.000 t magneten per jaar, pad naar 12.000 t | [4][5][6][15] |

## 6 · Stoppunt
Fabriekspoort van e-VAC in Sumter: de B/L noemt de fabriek als consignee [1]; wat er met de magneetblokken daarna gebeurt valt buiten deze keten (fase E vervalt).

## 7 · Open punten
- **Beide havens zijn aannames.** De twee flake-B/Ls (06-08 en 29-06-2026) noemen geen haven [1][2]. Felixstowe staat alleen op een LCM-B/L voor een mezzanineplatform (master MEDURE870957, place of receipt Newton-le-Willows, aan de M6) [3]; dezelfde master staat op de LCM-pagina met Antwerpen en aankomst Norfolk [2], dus bronnen spreken elkaar tegen. Charleston is een van LCM-s vijf Amerikaanse topHavens [2], gekozen op nabijheid; e-VAC-s eigen B/L (Vacuumschmelze) loopt via New York. Reserve: Seaforth (26 km van LCM, MARNET 6.586 km) als VK-haven.
- **Geen jaarvolume.** Twee zendingen (0,018 kt legering) zijn geen jaarcijfer; de eVAC-nameplate is magneetoutput, geen flake-invoer. Niet geextrapoleerd.
- **Sumter-punt is een adres-geocode**, plant nog niet bevestigd op satelliet (wolk over het midden); LCM-adres Unit 2 Hooton Park niet bevestigd: OSM geeft North Road, Overpool (CH65 1BL), 0,9 km van Hooton Park Circuit.
- **Wegkilometers zijn indicaties**: b1 en b3 hebben alleen hemelsbreed en OSRM, geen operator- of overheidsopgave; de ±15%-toets is een indicatie.
- **Felixstowe-anker staat 190 m achter de kadekant** (site-niveau, Trinity Terminal; Landguard niet onderzocht).
- Capaciteit LCM 1.400 t/j is een oud artikel; 10-K noemt 2.500 t/j voor alle producten.

## 8 · Bronnen
[1] ImportGenius, E-Vac Magnetics LLC — 840 Masatosagawa Dr, Sumter SC 29153; B/L ECUWMANCHS07747, LCM, NdFeB-flakes, 40 drums, 12.805 kg, aankomst 06-08-2026. https://www.importgenius.com/importers/e-vac-magnetics-llc
[2] ImportGenius, Less Common Metals Ltd — top US-havens Newark, New York, Chester, Charleston, Norfolk; flakes-B/L 29-06-2026 HS 7206.90.00 5.226 kg (4 pallets); sample-B/L Antwerpen. https://www.importgenius.com/suppliers/less-common-metals-ltd
[3] ImportGenius, USA Rare Earth Inc — B/L SAIJKXMJ00005940, master MEDURE870957, foreign port Felixstowe, receipt Newton-le-Willows. https://www.importgenius.com/importers/usa-rare-earth-inc
[4] metal-powder.tech, "eVAC ships first rare-earth magnets from South Carolina facility" — 2.000 t NdFeB/j, pad naar 12.000 t/j (via zoekresultaat; pagina gaf 403). https://www.metal-powder.tech/evac-ships-first-rare-earth-magnets-from-south-carolina-facility/
[5] Fastmarkets, "E-Vac to build rare earth magnet plant in South Carolina" — 85 acres, Pocotaligo Industrial Park, Sumter County. https://fastmarkets.com/insights/e-vac-to-build-rare-earth-magnet-plant-in-south-carolina
[6] VAC Newsroom, e-VAC tax credit US$112 mln — groundbreaking maart 2024, oplevering najaar 2025. https://vacuumschmelze.com/Newsroom/e-vac-magnetics-receives-historic-1119-million-qualifying-advanced-energy-project-tax-credit-for-construction-of-first-us-manufacturing-facility-in-south-carolina-n2641
[7] USA Rare Earth, 10-K FY2025 — LCM ca. 2.500 MTPA, strip-cast flakes voor sintermagneten. https://www.sec.gov/Archives/edgar/data/1970622/000197062226000021/usar-20251231.htm
[8] Less Common Metals, "Metal and alloy production in the Western World" — strip casting, twee ovens van 600 kg, ca. 1.400 tpa (oude opgave). https://lesscommonmetals.com/metal-and-alloy-production-in-the-western-world-a-supply-chain-alternative/
[9] metal-powder.tech, "USA Rare Earth cleared to acquire Less Common Metals". https://www.metal-powder.tech/?p=284480
[10] OpenStreetMap (ODbL) via Nominatim — Less Common Metals, North Road, CH65 1BL 53.3054566, -2.9333669. https://nominatim.openstreetmap.org
[11] OSRM (router.project-osrm.org) — b1 met vier via-punten 414,6 km; b3 158,6 km; alle via-punten op de weg binnen 3 m, ankers 15-94 m van een weg.
[12] Wikipedia, "Port of Felixstowe" — grootste containerhaven van het VK, 51.955, 1.31. https://en.wikipedia.org/wiki/Port_of_Felixstowe
[13] Eigen MARNET-dry-run (`hecht_marnet.py route`, scratch): Felixstowe → Charleston 6.932,2 km, 93 MARNET-edges, snaps 4,70 en 1,67 km.
[14] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-ree-ellesmereport-sumter-{lcm,felixstowe,evac,leatherman}.png` (z15, 2026-10-30).
[15] `v2/design/ree-sitelaag.json` — w-vac-hanau: VAC-VS-site Sumter 2.000 t/j nu, pad naar 12.000 t/j; Energy Fuels-overnamebod juni 2026.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Resultaat:** `v2/data/stroomroute-ree-ellesmereport-sumter.json` (120 KB, versie 2, lonlat) · 3 benen · **7.502,5 km** · 6.186 punten · 4 markers (alle 0,0 km van hun lijn). Functie `bak_ree_ellesmereport_sumter` in `v2/tools/bak_stromen.sh`; profielen `ree-ellesmereport-sumter-lcm-felixstowe` en `-charleston-sumter` in `maak_stroombeen_weg.py`.

| # | modaliteit | km gebakken | km brief | afwijking | naad vorig been | opmerking |
|---|---|---|---|---|---|---|
| b1 | truck | 412,8 | OSRM 414,6 (indicatie, geen wegkm) | -0,4% | 0,00 | M56, M6, A14; lengtetoets 412,6 tegen 414 = -0,3% [OK] |
| b2 | zee | 6.932,2 | MARNET 6.932,2 | 0,0% | 4,70 | kade naar kade, 93 MARNET-edges, geen haven-aanloop |
| b3 | truck | 157,5 | OSRM 158,6 (indicatie, geen wegkm) | -0,7% | 1,67 | I-26, I-95, US-521; lengtetoets 157,4 tegen 159 = -1,0% [OK] |

**Recept.** b1: wegscan_puur.py, extract groot-brittannie (12 min), 4 via-punten uit §4 plus de twee ankers, refs M56 M6 A14. b3: extract us-south-carolina (1 min), via I-95 Santee en US-521, refs I-26 I-95 US-521. b2: `--been zee 51.9639,1.2926 -> 32.8392,-79.9352`. Geen stippel, geen aanloop, geen lucht, geen kopie. Alle drie de benen doorgetrokken; "aannemelijk: één bron" staat in de beennamen (beide havens), niet in de lijnstijl.

**Toelichting en bevindingen.**
- **b1 vroeg `eindToegangPrivaat`.** De eerste scan gaf "geen wegpad tussen punt 4 en 5": de terminalwegen rond het Trinity-anker zijn in OSM access=private en het openbare net eindigt 1,09 km ten westen van het anker. Met `eindToegangPrivaat: True` (rescan, ander cache-hash) loopt de last mile 2,09 km over service/unclassified-wegen tot op 0,09 km van het anker; first mile 1,33 km. Geen via-punt bijgeschoven.
- **Zee-naden onder de 5 km-grens:** 4,70 km bij Felixstowe en 1,67 km bij Charleston. Volgens de bakhandleiding (>5 km = haven-aanloop) geen aanloop; de 4,70 km is wel een naad op de rand van de norm en een procesgat in de haven (zelfde bevinding als §7, laatste punt).
- **b3:** first mile 1,44 km (service/tertiary), last mile 0,94 km (service); zes keerlussen gesnoeid (0,3 km). Eerste via is het Leatherman-anker, snap 0,05 km.
- **Knikken:** `toets_knikken.py` 13 + 2 + 12 knikken >= 60 graden, 0 omkeringen en 0 terugloop; de scherpe hoeken zijn spikes in OSM-terminalgeometrie (Leatherman, Sumter-park), geen routefout.
- **Wegkm zijn OSRM-indicaties** (zie §7): de ±15%-toets is een indicatie; beide wegbenen vallen er ruim binnen.

**Lessen.** Een containerterminal waarvan de interne wegen access=private zijn heeft `eindToegangPrivaat` nodig (cache-hash verandert, dus een rescan van het hele extract: 12 minuten voor groot-brittannie). Meet vóór een scan met de bestaande cache welke wegen rond het anker in de graaf zitten (component-test op gedeelde knopen), dan weet je of het profiel de vlag nodig heeft.

