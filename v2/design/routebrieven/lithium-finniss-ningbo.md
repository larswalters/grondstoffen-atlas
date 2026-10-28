# Routebrief (licht) · lithium — Finniss → Darwin → Zhangjiagang (Australië → China)

**stroom-id:** `lithium-finniss-ningbo` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat (SC) en DMS-fines van de Finniss-mijn (Core Lithium, Cox Peninsula, NT) gaan per **truck** ~88 km over verharde weg (Cox Peninsula Road → Finn Road → Channel Island Road → Berrimah Road) naar East Arm Wharf in Darwin Port, per **bulkcarrier** ~5.400 km door Banda-zee, Makassar, Zuid-Chinese Zee en Taiwanstraat naar de Yangtze-monding en over de Yangtze naar de kade van Zhangjiagang. **Afwijking van het ontwerp:** het ontwerp noemde Ningbo; dat is nergens gebronnd. De enige met naam genoemde aanlandhaven van Finniss-concentraat is Zhangjiagang (Silver Lady, juli 2023, voor Sichuan Yahua) [4]. Eindpunt is dus Zhangjiagang, *aannemelijk: één bron*; het id blijft staan.
**Welke as van het verhaal:** de kortste Australische keten naar China: mijn 88 km van de diepwaterhaven, geen spoor. FY2024 (peiljaar) **95,0 kt SC** [1] ≈ **13 kt LCE/j** (95,0 kt × 5,5 % Li2O × 2,473, eigen omrekening); 2023-leveringen 18,5 kt SC aan Yahua (13,1 kt in de Silver Lady) [4]. De mijn lag sinds 2024 stil (care and maintenance), is sinds mei 2026 herstart (Grants-dagbouw); eerste uitvoer juni 2026 = 20 kt fines + 5 kt stockpile-SC via Darwin [2][3]; eerste nieuwe SC-lading gepland Q4 2026 [5]. De brief tekent de route, niet een gemeten 2026-stroom.

## 1 · Ketenkaart
```
Finniss-mijn/plant `li-finniss-mijn` ──(b1 truck · Cox Peninsula Rd → Finn Rd → Channel Island Rd → Berrimah Rd · 88 km)──► East Arm Wharf `li-eastarm-kade`
   ──(b2 stippel · haven-aanloop East Arm → MARNET-zeeknoop 2572 · ~37 km)──► (-12.2, 130.8)
   ──(b3 zee · Banda-zee → Makassar → ZCZ → Taiwanstraat · 5.425,9 km, MARNET; bestemming aannemelijk: één bron)──► Yangtze-monding `li-yangtze-monding`
   ──(b4 stippel 8,6 · b5 Yangtze 135,2 km · b6 stippel 0,6 — letterlijke kopie lithium-bikita-zhangjiagang)──► Zhangjiagang-kade `li-zjg-kade` ⏹ stoppunt
   └── niet getekend: Sichuan Yahua (Suining) / Ganfeng als afnemers; Glencore-stockpile (5,1 kt, feb 2026) met onbekende bestemming
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (road train/kipper) | `li-finniss-mijn` → `li-eastarm-kade` | mijnweg → Cox Peninsula Road → Finn Road → Jenkins Rd → Channel Island Rd → Berrimah Rd → East Arm Port Rd | 88 (Core, sealed road [2][3]); OSRM 80,5 [6] | maak_stroombeen_weg (extract australie, vensterKm 40) | nee; mogelijk korte "eigen terrein"-stippel op de wharf |
| b2 | B | zee (stippel) | `li-eastarm-kade` → MARNET-zeeknoop 2572 (-12.2000, 130.8000) | Darwin-haven → Beagle Gulf | 36,9 (gemeten, maak_havenaanloop) | maak_havenaanloop.py (timeout 300; bij exit 124 rechte stippel) | ja — net reikt niet (kade 33,5 km van de zeeknoop) |
| b3 | B | zee (bulkcarrier) | (-12.2000, 130.8000) → Yangtze-routeerpunt (31.4074, 121.4848) | Banda-zee, Makassar, Zuid-Chinese Zee, Taiwanstraat | 5.425,9 (MARNET, nagemeten 2026-10-28) | MARNET | nee — *aannemelijk: één bron* in de beennaam |
| b4 | B | zee (stippel) | 31.51, 121.4187 → 31.4512, 121.4769 | — | 8,6 | letterlijke kopie `bak_lithium_bikita_zhangjiagang` (stippel overgang zeenet → bulklaag) | ja — net reikt niet |
| b5 | B | binnenvaart (zelfde schip) | Yangtze-monding → Zhangjiagang | Yangtze, zuidgeul | 135,2 (gebakken) | letterlijke kopie `$BEEN/rivierbeen-yangtze-zhangjiagang.geojson` | nee |
| b6 | B | binnenvaart (stippel) | 31.9733, 120.4202 → `li-zjg-kade` | — | 0,6 | letterlijke kopie aanloop-stippel | ja — anker ≠ routeerpunt |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-finniss-mijn` | mijn / plant | Finniss Lithium Operation (Core Lithium), Cox Peninsula | -12.6712, 130.7747 | [1][7][8] | bron-gelegd (z14/z15 gezien: één afgebakend mijncomplex met een pit, een gevulde oude pit, vier tailings-/waterbekkens en procesgebouwen aan de noordrand, grindweg naar het oosten; punt ligt op het complex tussen de pits, de DMS-plant staat ~1 km noordelijker) |
| `li-eastarm-kade` | overslag truck → zee | East Arm Wharf, Darwin Port (NT Government / Landbridge) | -12.4904, 130.8812 | [2][7][9] | aannemelijk (z15 gezien: pier met containerstack en loodsen, dwarskade en wegtoegang; Core noemt "Darwin Port", de specifieke ligplaats voor concentraat is niet gebrond) |
| `li-yangtze-monding` | overgang zee → rivier | Yangtze-monding | 31.4074, 121.4848 | bestaand (routeerpunt uit lithium-bikita-zhangjiagang) | hergebruik |
| `li-zjg-kade` | losplek (stoppunt) | Zhangjiagang — kade Zhangjiagang Port Group | 31.96800, 120.42050 | bestaand anker (lithium-greenbushes-zhangjiagang, lithium-bikita-zhangjiagang) | hergebruik; bestemming *aannemelijk: één bron* [4] |

## 4 · Via-punten (alleen b1; lat, lon uit de OSM-gebaseerde OSRM-route [6], door het wegprofiel op de doorgaande weg te projecteren)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | mijnweg × Cox Peninsula Road | -12.6611, 130.7811 | verlaat het mijnterrein op de enige verharde uitvoerweg, oost i.p.v. westwaarts de Cox Peninsula in |
| b1 | 2 | Cox Peninsula Rd × Finn Road | -12.7039, 131.0093 | pint de 37 km oostwaarts i.p.v. een omweg over de Stuart Highway en Palmerston |
| b1 | 3 | Finn Rd × Jenkins Road | -12.6123, 131.0092 | pint de noordwaartse tak van Finn Road naar het Darwin-stadsnet |
| b1 | 4 | Jenkins Rd × Channel Island Road | -12.5774, 130.9650 | pint de aansluiting op Channel Island Road (Berrimah-industrie), niet op de Stuart Hwy door Palmerston |
| b1 | 5 | Berrimah Road (ZW-richting havenroute) | -12.4612, 130.9253 | pint Berrimah Road naar East Arm Port i.p.v. een stadsroute via Winnellie |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Finniss DMS-plant | Core Lithium | erts → SC5 spodumeenconcentraat + DMS-fines | FY2024 95,0 kt SC ≈ 13 kt LCE; 2026 Grants-erts 780-790 kt → 130-140 kt SC5 [3]; BP33 ondergronds vanaf mid-2027 | [1][3] |

## 6 · Stoppunt
De brief stopt op de kade van Zhangjiagang: dat is de enige gedocumenteerde aanlandhaven van Finniss-concentraat (Silver Lady, 2023, voor Sichuan Yahua) [4]; de Yahua-fabriek (Suining, Sichuan) ligt niet bij de haven en geen bron legt een landcorridor, dus fase D en E vervallen.

## 7 · Open punten
- **Ningbo is niet gebronnd** (ontwerp), afnemers wisselen: Yahua en Ganfeng (offtake Ganfeng 2025 beëindigd), 2026-voorraad naar Glencore met onbekende bestemming; Zhangjiagang is *aannemelijk: één bron*.
- **Status mijn:** herstart sinds mei 2026 [2], maar het eerste nieuwe SC-schip wordt pas Q4 2026 verwacht [5]; de stroom is route, geen gemeten 2026-volume. Bron [5] is alleen als zoeksamenvatting gelezen (403 bij fetch).
- **Wegkm:** 88 km is de Core-opgave; het gebakken wegbeen moet daar binnen ±15% (75-101 km) van blijven; OSRM geeft 80,5 km. De Stuart-Highway-variant is niet getekend.
- **Ligplaats East Arm:** geen bron noemt de ligplaats voor concentraat; East Arm Wharf is aannemelijk omdat Darwin Port daar zijn multi-user-kade heeft.
- **Mijn-anker** staat op OSM-landuse, site-niveau gezien op satelliet; de DMS-plant ligt ~1 km noordelijker en is niet apart gelegd.
- **Haven-aanloop:** de bak duurde 270 s van 300 s timeout; bij exit 124 een rechte stippel -12.4904,130.8812 → -12.2,130.8.

## 8 · Bronnen
[1] Wikipedia — Finniss Lithium Project: 12°42′47″S 130°47′20″E, 95.020 dmt SC FY2024, eerste lading mei 2023 Port Darwin. https://en.wikipedia.org/wiki/Finniss_Lithium_Project
[2] Yahoo Finance, 26-02-2026 — verkoop 5,1 kt stockpile aan Glencore via Darwin Port, project 88 km van Darwin Port over verharde weg. https://finance.yahoo.com/news/core-lithium-sell-finniss-stockpile-154514579.html
[3] Core Lithium ASX 22-06-2026 (via Webull) — eerste export 20 kt fines + 5 kt SC via Darwin Port, "88km by sealed road", Grants 130-140 kt SC5, BP33 mid-2027. https://bulletin.webull.com/qbd/announcement/20260622/499501714/783ae4f4f15a52f594f70b5015961e45.pdf
[4] Core Lithium / Mining Magazine, juli 2023 — 13.100 t SC, Silver Lady, vanuit Darwin Port naar Zhangjiagang voor Sichuan Yahua (balans van 18.500 t). https://miningmagazine.com.au/13000t-spodumene-shipment-setting-sail/ (403 bij fetch; search-samenvatting) · https://www.pv-magazine-australia.com/2023/01/09/first-ore-shipment-sails-from-nt-lithium-mine-to-china
[5] Mining Weekly, 18-09-2026 — eerste SC geproduceerd, eerste lading Q4 2026 gepland. https://www.miningweekly.com/article/finniss-lithium-restart-project-australia-update-2026-09-18 · NT Independent, 20-05-2026 — mijnbouw hervat. https://ntindependent.com.au/core-lithium-restarts-mining-at-finniss-project/
[6] OSRM (OSM-routing, router.project-osrm.org), 2026-10-28 — mijn → East Arm 80,5 km: Cox Peninsula Rd 36,6 · Finn Rd 10,0 · Jenkins Rd 6,4 · Channel Island Rd 6,7 · Elrundie Ave 5,1 · Kirkland/Wishart/Berrimah Rd · East Arm Port.
[7] OpenStreetMap (ODbL) via Nominatim, 2026-10-28 — way 1431682885 "Finniss Lithium mine" -12.6712, 130.7747 · way 1204565197 "East Arm Wharf" -12.4904, 130.8812.
[8] Esri World Imagery via `v2/tools/sat_check.py` (live, 2026-10-28): `v2/build-cache/satcheck/sat-lithium-finniss-ningbo-finniss-z14.png`, `…-finniss-z15.png`.
[9] Esri World Imagery: `v2/build-cache/satcheck/sat-lithium-finniss-ningbo-eastarm-z15.png`.
[10] MARNET (`v2/build-cache/marnet-preais`) — zeeknoop 2572 (-12.2000, 130.8000) op 33,5 km van East Arm; route -12.2,130.8 → 31.4074,121.4848 = 5.425,9 km, snap 0,0 / 13,0 km (2026-10-28).
[11] Letterlijke kopie Zhangjiagang-staart: `v2/design/routebrieven/lithium-bikita-zhangjiagang.md` §2 b3-b5 en `bak_lithium_bikita_zhangjiagang` in `v2/tools/bak_stromen.sh`.

## 9 · Gebakken

Gebakken (2026-10-28, lichte werkwijze, M31 golf 10) · `bash v2/tools/bak_stromen.sh lithium-finniss-ningbo` → `v2/data/stroomroute-lithium-finniss-ningbo.json` (42,1 KB, contract versie 2, lonlat).

| # | modaliteit | km | naad | stippel | naam (kort) |
|---|---|---|---|---|---|
| b1 | truck | 80,7 | 0,00 | nee | Finniss-mijn → East Arm Wharf (gemeten weg, 773 punten) |
| b2 | zee | 36,9 | 0,00 | ja | haven-aanloop East Arm (over water, 62 punten) |
| b3 | zee | 5.425,9 | 0,00 | nee | bulkcarrier Darwin → Yangtze-monding (MARNET, bestemming aannemelijk: één bron) |
| b4 | zee | 8,6 | 0,00 | ja | overgang zeenet → Yangtze-bulklaag (letterlijke kopie bikita) |
| b5 | binnenvaart | 135,2 | 0,00 | nee | Yangtze-monding → Zhangjiagang (letterlijke kopie rivierbeen) |
| b6 | binnenvaart | 0,6 | 0,00 | ja | aanloop naar de ligplaats (letterlijke kopie bikita) |

Totaal **5.687,9 km**, 2.090 punten, 4 markers (mijn, East Arm, Yangtze-monding, Zhangjiagang). Geen naad > 0,00 km (alle benen sluiten op elkaar aan); toets_knikken: 0 omkeringen, 0 terugloop (truck 13 knikken in de Berrimah-stadsstraten, zee 4 krappe bochten in de MARNET-route).

**Recept:** profiel `lithium-finniss-ningbo-mijn-eastarm` in `maak_stroombeen_weg.py` (extract australie, vensterKm 40, corridorKlassen tertiary+unclassified, eindToegangPrivaat; scan `wegscan_puur.py` 172 s) · `timeout 300 python v2/tools/maak_havenaanloop.py --van=-12.4904,130.8812 --naar=-12.2,130.8` (slaagde, 36,9 km, 0 km land; negatieve breedte met `=` meegeven) · functie `bak_lithium_finniss_ningbo` in `bak_stromen.sh`.

**Toelichting per been**
- **b1:** 80,7 km tegen 88 km Core-opgave = −8,4% (binnen ±15%); OSRM 80,5. De segmenten 36,6 / 10,2 / 6,4 km komen op de OSRM-lengtes uit; alle zes via-snaps ≤ 0,09 km, dus de via-punten lagen op de doorgaande weg. Eerste 1,7 km over service-wegen (mijnterrein), laatste 6,5 km over service/tertiary/unclassified in Berrimah/East Arm. Stuart-Highway-variant niet getekend.
- **b2 (stippel, haven-aanloop):** kade 33,5 km van zeeknoop 2572, dus aanloop nodig; gebakken 36,9 km over water, omwegfactor 1,10. Stippel betekent hier "het zeenet reikt niet tot de kade".
- **b3:** MARNET zeeknoop 2572 → Yangtze-routeerpunt = 5.425,9 km (snap 0,0 / 13,0 km, gelijk aan de bikita-route); bestemming Zhangjiagang is aannemelijk op één bron en staat in de beennaam, de lijn is doorgetrokken.
- **b4-b6:** letterlijke kopieën van `bak_lithium_bikita_zhangjiagang`; geen tweede versie.

**Markers:** mijn, East Arm en Zhangjiagang liggen 0,000 km van de lijn; de Yangtze-marker (31.42704,121.47618, brief-opgave, hergebruik bikita) ligt 2,69 km van de lijn: anker ≠ routeerpunt, zoals bij de bikita-bake.

**Lessen:** (1) `maak_havenaanloop.py` neemt een negatieve breedte alleen als `--van=-12.4904,130.8812` (met `=`); zonder `=` leest argparse hem als vlag. (2) Een achtergrondrun met `&` aan het eind van het commando overleeft het einde van de shell niet: gebruik run_in_background zonder `&`. (3) De Australië-extract (953 MB) scant in ~3 minuten.

**Onopgelost:** Ningbo niet gebronnd (zie §7); ligplaats East Arm voor concentraat niet gebrond; DMS-plant ~1 km noordelijker niet apart gelegd; 2026-volume niet gemeten.
