# Routebrief (licht) · grafiet — Kilbourne (Balmat, New York) → Anniston Army Depot (Alabama, VS)

**stroom-id:** `grafiet-kilbourne-anniston` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** natuurlijk vlokgrafiet-concentraat van het Kilbourne-project in het Empire State Mines-complex (Titan Mining, bij Gouverneur, St. Lawrence County NY) gaat per **truck** (werkaanname) over US-11 en I-81 Zuid, I-40/I-75 en I-59 naar de geplande Kilbourne Graphite Purification Plant op ~97 acre Army-terrein bij Anniston Army Depot (Alabama). Eén been, geen zee. Geen RHI Magnesita-tak (geen fabriek genoemd).
**Welke as van het verhaal:** *de VS-eigen keten van mijn tot gezuiverd grafiet, op militair terrein.* Titan is "first end-to-end producer of natural flake graphite in 70 years" [1]. **Jaarvolume naar Anniston: 0 kt grafiet/j** — de fabriek bestaat niet (term sheet 2026-10-07, geen definitieve lease [1]). Bron-site: demonstratiefabriek ~1,2 kt/j concentraat (ontwerp tot 2,5 kt/j), doel ~40 kt/j concentraat en waardeproduct vanaf bouw 2027 [3]. Eenheid kt grafiet/j, peiljaar 2026.

## 1 · Ketenkaart
```
ESM-complex, Balmat `gr-kilbourne-esm` ──(b1 truck · NY-812 → US-11 → I-81 Z → I-40 → I-75 → I-24 → I-59 → US-431 · hemelsbreed 1.492 km, geen wegkm · aannemelijk: term sheet niet definitief)──►
   Anniston Army Depot, hoofdterrein `gr-anniston-depot` (kavel Parcel 1 niet gelokaliseerd) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (werkaanname; Titan noemt geen vervoer) | `gr-kilbourne-esm` → `gr-anniston-depot` | NY-812/NY-58 → US-11 → I-81 Z (Syracuse, Binghamton, Scranton, Harrisburg, Hagerstown, Roanoke) → I-81/I-40 → I-75 Chattanooga → I-24 → I-59 (Fort Payne, Gadsden) → US-431 → Bynum Road | hemelsbreed 1.492 km, geen wegkm; indicatie: OSM-extracts 1.850 km, OSRM-demo 1.827 km [10] (zelfde bron als de scan, geen toets) | maak_stroombeen_weg (profiel `grafiet-kilbourne-anniston-esm-anniston`) | nee — *aannemelijk: term sheet niet definitief, feed Kilbourne niet expliciet* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-kilbourne-esm` | mijn + concentrator + demofabriek (laadplek) | Empire State Mines, Balmat/West Fowler (Titan) — industriecomplex met verwerkingsgebouw langs de Balmat-weg | 44.2565, -75.3985 | [3][6][7][10][11] | aannemelijk (z15 gezien: wit gebouwencomplex met grindwegen en stort aan Pumphouse Road, west van NY-812; niet bevestigd als concentrator; OSM-knoop "No 1 Mine and Mill" 44.2660/-75.3870 ligt in een ondergelopen dagbouwput en is verworpen) |
| `gr-anniston-depot` | losplek, depot-hoofdterrein (kavel nog niet gelegd) | Anniston Army Depot, Bynum — loodsen en rangeerspoor | 33.6245, -85.9700 | [1][2][8][9][11] | onzeker (z15 gezien: rijen magazijnloodsen en depotwegen aan Bynum Road; de ~97 acre voor de fabriek is nergens gepubliceerd, dus een depotpunt en geen fabrieksanker) |

## 4 · Via-punten (alleen b1; alle óp de doorgaande rijbaan, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | I-81 Z van Binghamton | 42.0190, -75.7815 | I-81 door de Southern Tier i.p.v. I-90 Thruway / I-88 |
| b1 | 2 | I-81 Pittston (Wilkes-Barre) | 41.3002, -75.7710 | I-81 i.p.v. de tolweg I-476 (Turnpike NE-extensie) |
| b1 | 3 | I-81 Carlisle (Harrisburg) | 40.1880, -77.1913 | I-81 langs Harrisburg i.p.v. I-78/I-83/I-76 |
| b1 | 4 | I-81 Wytheville | 36.9589, -81.1041 | I-81 Zuid naar Tennessee i.p.v. I-77 naar Charlotte |
| b1 | 5 | I-40 W van Knoxville | 35.9183, -84.0905 | I-40/I-75 Z naar Chattanooga i.p.v. I-40 W naar Nashville |
| b1 | 6 | I-75 Cleveland (TN) | 35.1918, -84.8921 | I-75 naar Chattanooga (Novonix Riverside ligt aan de route, geen stop) |
| b1 | 7 | I-59 Fort Payne | 34.4553, -85.7315 | I-59 Z via Fort Payne i.p.v. I-24 W / I-65 naar Birmingham |
| b1 | 8 | US-431 O van Gadsden | 33.9679, -85.9453 | US-431 Z naar Anniston i.p.v. I-59 door naar Birmingham en I-20 O |

Punten zijn gelezen van de OSRM-demoroute (OSM) op de benoemde weg [10]; geen enkel punt in een stadscentrum.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kilbourne / ESM-demofabriek, Gouverneur | Empire State Mines LLC (Titan Mining) | grafieterts → vlokconcentraat | demo ~1,2 kt/j (ontwerp 2,5); doel ~40 kt/j (PEA dec 2025) | [3] |
| Kilbourne Graphite Purification Plant (gepland), Anniston | Empire State Mines LLC (EUL, term sheet) | concentraat → gezuiverd gemicroniseerd grafiet (PMG), later gecoat bolvormig (CSPG) | niet gepubliceerd; Army heeft ROFO op max 10% | [1][2] |

## 6 · Stoppunt
De brief stopt bij het Anniston-depotterrein: de fabriek is niet gebouwd, en geen bron noemt een afnemer of vervolgbestemming van PMG/CSPG (alleen defense, industrie, energie in algemene termen). RHI Magnesita (voorwaardelijke levering, tot 10%) [4] noemt geen fabriek en wordt niet getekend.

## 7 · Open punten
- **Locatie niet definitief:** het term sheet (2026-10-07) is geen definitieve EUL; in juni 2026 was Pine Bluff Arsenal (AR, ~245 acre) de primaire site en Anniston Parcel 1 secundair; Pine Bluff en Fort Drum (NY) blijven in onderzoek [1][2]. Titan noemt ook een andere New Yorkse site voor nabewerking [3].
- **Kavel Parcel 1 (97 acre) is niet gelegd;** OSM-relatie 14955745 (hele depot, 33.6495/-85.9699 in het bos) is geen anker [8]. Staart blijft depot-hoofdterrein, onzeker; de lijn eindigt aan het depot.
- **Feedkoppeling niet expliciet:** de release noemt geen feedbron of capaciteit voor Anniston, alleen "Kilbourne's domestic natural flake graphite resource" [1].
- **Kop is niet bevestigd als concentrator:** ESM-adres 408 Sylvia Lake Rd (Photon/OSM 44.2628/-75.4089, 1,1 km NW van het anker, kantoor/werkplaats-gebouwen z15) [6][7]; de DEC-melding geeft 44.2475/-75.3972 (1,0 km ZZW) voor de mijn-en-molenlocatie. De demofabriek zelf is nergens gelokaliseerd.
- **Transportwijze werkaanname;** een spoorverbinding (CSX/NS naar Anniston) is niet uitgesloten maar niet gebrond.
- **Volume nul tot de fabriek bestaat** (bouw gepland vanaf 2027 [3]); geen wegkilometer gepubliceerd, de ±15%-toets is een indicatie.
- **Eindtoegang:** de laatste ~1,3 km loopt over depotwegen (Bynum Road, Mac Arthur Avenue, 3rd Street West); toegang militair/privé is niet gecontroleerd.
- **Sitelaag (niet aangeraakt):** kandidaten `w-kilbourne-esm` (mijn, 1,2 kt/j demo) en een depot-site Anniston (onzeker).

## 8 · Bronnen
[1] Titan Mining, "Titan Mining and U.S. Army agree to commercial framework", 2026-10-07 — term sheet EUL, ~97 acre Anniston, 50 j + 2×25 j, PMG/CSPG, ROFO 10%, Pine Bluff en Fort Drum in diligence. https://www.titanminingcorp.com/_resources/news/nr-20261007.pdf
[2] Titan Mining, persbericht 2026-06-25 — twee conditionele EUL-awards: Pine Bluff Arsenal (Site B, ~245 acre, primair) en Anniston (Parcel 1). https://www.titanminingcorp.com/_resources/news/2026-06-25-nr-titan.pdf
[3] Titan Mining, Graphite project — demofabriek in het ESM-molencomplex, ~1.200 t/j (ontwerp 2.500), doel ~40.000 t/j, bouw 2027, tweede NY-site overwogen. https://www.titanminingcorp.com/projects/graphite/
[4] Titan Mining, persbericht 2026-08-05 — RHI Magnesita (voorwaardelijke levering, geen fabriek genoemd). https://www.titanminingcorp.com/_resources/news/nr-20260805.pdf
[5] SEC exhibit 99.1 (0001171843-26-006477) en Mining Weekly 2026-10-07 — term sheet, geen feedbron (alleen via de haalbaarheidstoets, niet zelf geopend). https://www.sec.gov/
[6] NY DEC Environmental Notice Bulletin 2022-07-06, "ESM Balmat Mines and Mill" — 408 Sylvia Lake Rd, Gouverneur NY, erts per interne weg naar No. 4 Mill (via zoekresultaat, pagina gaf 403). https://dec.ny.gov/news/environmental-notice-bulletin/2022-07-06/completed-application/esm-balmat-mines-and-mill
[7] OpenStreetMap via Photon, 2026-10-29 — "408 Sylvia Lake Road, West Fowler" 44.2628/-75.4089. https://photon.komoot.io/
[8] OpenStreetMap/Nominatim — relatie 14955745 Anniston Army Depot (militair, bbox 33.610–33.689 / -86.013–-85.911). https://www.openstreetmap.org/relation/14955745
[9] Wikipedia, "Anniston Army Depot" — Bynum, Calhoun County, 10.640 acre sinds 1940. https://en.wikipedia.org/wiki/Anniston_Army_Depot
[10] OSRM-demoserver over OSM, 2026-10-29 — Balmat → depot 1.826,7 km, via NY-812, US-11, I-81, I-40, I-75, I-24, I-59, US-431; via-puntcoördinaten uit deze route. https://router.project-osrm.org/
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-grafiet-kilbourne-anniston-balmat.png`, `sat-grafiet-kilbourne-anniston-depot.png`.
[12] Wikipedia, "Fowler, New York" — gemeente van de ESM-site, 44.2833/-75.4000. https://en.wikipedia.org/wiki/Fowler,_New_York

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Bestand:** `v2/data/stroomroute-grafiet-kilbourne-anniston.json` (577 KB, versie 2, lonlat) · recept `bak_grafiet_kilbourne_anniston()` in `v2/tools/bak_stromen.sh` · profiel `grafiet-kilbourne-anniston-esm-anniston` in `v2/tools/maak_stroombeen_weg.py` · tussenuitvoer `v2/build-cache/ais/graaf/grafiet-kilbourne-anniston-weg-esm-anniston.geojson` (+ `-wegscan.log`).

| # | modaliteit | been | km | punten | naad |
|---|---|---|---|---|---|
| b1 | truck (doorgetrokken) | grafietconcentraat ESM-complex Balmat → Anniston Army Depot (NY-812/US-11 → I-81 Z → I-40 → I-75 → I-59 → US-431; werkaanname truck, aannemelijk: term sheet niet definitief) | 1.836,6 | 28.424 | — (één been) |

Totaal 1.836,6 km, 2 markers (gr-kilbourne-esm en gr-anniston-depot, beide 0,0 km van de lijn).

**Recept.** Eén wegprofiel, 8 Geofabrik-extracts (us-new-york, -pennsylvania, -maryland, -west-virginia, -virginia, -tennessee, -georgia, -alabama), vensterKm 40, `eindToegangPrivaat`, `trimStaart`, refs I-81/I-40/I-75/I-24/I-59/US-431. Wegscan via `wegscan_puur.py` in een weg-slot, ~15 min (Virginia en Pennsylvania zijn de langste). Daarna `bash v2/tools/bak_stromen.sh grafiet-kilbourne-anniston` in een zwaar-slot. Geen zee, geen haven-aanloop, geen stippel, geen kopie.

**Toets.**
- Km: 1.836,6 tegen OSM-indicatie 1.850 (-0,7%) en OSRM 1.827 (+0,5%); hemelsbreed 1.491,8 (omwegfactor 1,23). Er is GEEN gepubliceerde wegkm, dus dit is een indicatie met dezelfde bron (OSM) als de scan, geen onafhankelijke ±15%-toets.
- Segmenten per via-punt (km): Balmat → Binghamton 300,4 · → Pittston 92,4 · → Carlisle 202,4 · → Wytheville 580,3 · → Knoxville-W 303,9 · → Cleveland TN 112,4 · → Fort Payne 130,8 · → Gadsden-O 67,9 · → depot 46,2. Alle via-snaps 0,00 km; geen via-punt verplaatst of bijgeschoven.
- Anker-uiteinden: plant → weg 0,00 km, weg → depot 0,03 km. Eerste mijl 0,24 km (residential/service), laatste ~9,2 km over kleine klassen (residential, service, tertiary, unclassified) door `eindToegangPrivaat`: dat zijn de wegen rond en op het depot; toegang niet gecontroleerd.
- `toets_knikken.py`: 81 knikken >= 60 graden (bijna allemaal 'spike' op 3-30 m straal, afritten en klaverbladen van de Interstates), 2 omkeringen, 0 terugloop. De twee omkeringen (173,5 en 166,1 graden, 41,3123/-75,7582) zijn één afrit-lus van ~0,6 km bij Pittston (I-81/I-476-knoop, punten 5863-5881): de lijn rijdt een lusafrit rond en voegt op dezelfde I-81 weer in. Niet gerepareerd (via-punt Pittston ligt 1,8 km zuidelijker op de rijbaan, snap 0,00); 82 keerlussen waren al door `snoei_keerlussen` verwijderd (1.836,7 -> 1.836,6 km). `toets_rechte_benen.py`: geen rechte stukken.
- json.load, versie 2, punt_formaat lonlat, modaliteit truck, 28.424 punten.
- ⚠️ Bestand 577 KB: boven de ~300 KB-richtlijn omdat het wegbeen 1.837 km op wegpuntdichtheid is; de bundel (`bak_stroombundel.py`) verdunt op L0/L1, het losse json hoeft niet kleiner.

**Wat staat open.** Zie §7: locatie niet definitief (Pine Bluff primair), kavel Parcel 1 niet gelegd (staart = depot-hoofdterrein, onzeker), feedkoppeling niet expliciet, kop niet bevestigd als concentrator, transportwijze truck is werkaanname, depottoegang niet gecontroleerd. Het id noemt het werkelijke eindpunt (Anniston); lijn en titel eindigen daar ook.

**Lessen.** (1) Acht extracts op een venster van 40 km rond 1.800 km snelweg is een run van ~15 min en 690 KB geojson; neem een weg-slot en wacht met een until-lus op `geschreven`. (2) De Interstate-afrittenstructuur geeft veel spikes in `toets_knikken`; filter op omkering en terugloop, niet op het totaal. (3) Via-punten uit de OSRM-demoroute (op de benoemde weg) snapten allemaal op 0,00 km: dat is de manier om een corridor over meerdere staten te pinnen zonder een stadscentrum aan te raken.
