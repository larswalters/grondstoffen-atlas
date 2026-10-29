# Routebrief (licht) · zilver — Kidd Creek (Timmins) → Horne (Rouyn-Noranda) → CCR Montréal-Est (Canada)

**stroom-id:** `zilver-kidd-montrealest` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** zilverhoudend kopererts uit de Kidd Creek Mine per **eigen ertsspoor** (27 km) naar de Kidd Met-concentrator, het
concentraat (aannemelijk: één bron, historisch) per **spoor** (Ontario Northland via Matheson en Kirkland Lake) naar de Horne-smelter in
Rouyn-Noranda, de koperanodes (340 kg, Glencore: "rail car or truck") per **spoor** (CN) naar de Canadian Copper Refinery (CCR) in
Montréal-Est, waar uit het anodeslijk de **zilveringots >99,99%** komt. Geen zee, geen weg, geen vlucht.
**Welke as van het verhaal:** *Oost-Canada: zilver als bijproduct van koper* — Kidd levert ca. **47 t Ag/j** (1,5 Moz in 2024, 1 Moz = 31,1 t) [1];
Horne verwerkte 1927-2017 samen 847 Moz Ag (≈ 26.350 t) [9]. Het Kidd-aandeel in Horne/CCR en de CCR-zilveroutput zijn niet gepubliceerd.

## 1 · Ketenkaart
```
Kidd Mine `ag-kidd-mijn` ──(b1 spoor · eigen ertsspoor, erts · 28,8 km gemeten, 27 gepubliceerd)──► Kidd Met-concentrator `ag-kidd-concentrator`
  ──(b2 spoor · ONR Porquis–Matheson–Kirkland Lake–Noranda · 221,6 km, aannemelijk: één bron)──► Horne-smelter `ag-horne-smelter`
  ──(b3 spoor · CN Abitibi/La Tuque–Joliette → Montréal-Est · 845,6 km, anodes)──► CCR `ag-ccr` ── stoppunt (zilveringot)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ag-kidd-mijn` → `ag-kidd-concentrator` | eigen ertsspoor Kidd Creek → Kidd Met; erts, geen concentraat [1] | 27 gepubliceerd [1]; router 28,8 (+6,7%); hemelsbreed 26,6 | toets_spoorroute | nee (OSM kent het spoor; snap 0,07/0,15 km) |
| b2 | C | spoor | `ag-kidd-concentrator` → `ag-horne-smelter` | ONR Kidd-aftakking Porquis Jct → Matheson → Swastika/Kirkland Lake → Noranda (Nipissing Central) [8] — aannemelijk: één bron voor de bestemming | geen gepubliceerde km; router 221,6 (hemelsbreed 156,0; ratio 1,42) = indicatie | toets_spoorroute (vrije Dijkstra, 0 omkeringen) | nee (snap 0,15/0,30 km) |
| b3 | D | spoor | `ag-horne-smelter` → `ag-ccr` | Rouyn-Noranda → Senneterre → La Tuque/Hervey Jct → Joliette → Montréal-Est (CN); Glencore: "rail car or truck" [4][5] | geen gepubliceerde km; router 845,6 (hemelsbreed 509,8; ratio 1,66) = indicatie | toets_spoorroute (vrije Dijkstra) | nee (snap 0,30/0,18 km) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-kidd-mijn` | mijn / kop ertsspoor | Kidd Creek Mine, schachtcomplex, Timmins (ON) | 48.6900, -81.3722 | [1][3][15] | bron-gelegd (z15 gezien: hijsgebouwen/kopgestellen en transportbanden naast de open pit, spoorsnap 0,07 km). Wikipedia-punt 48.6889,-81.3653 ligt in de pit-rand; OSM-"Kidd Mine" 48.6719,-81.3611 ligt in bos, verworpen |
| `ag-kidd-concentrator` | concentrator (erts → Cu-/Zn-concentraat), overslag naar ONR | Kidd Metallurgical Site, 10050 Hwy 101 E | 48.5500, -81.0792 | [2][16] | bron-gelegd (z15 gezien: grote concentratorhal met emplacement, droogstoven, tailings en spoorbundel; smelter gesloten 2010) |
| `ag-horne-smelter` | smelter (concentraat → anodes) | Fonderie Horne (Glencore), Rouyn-Noranda | 48.2533, -79.0136 | [4][9][10][15] | bron-gelegd (z15 gezien: smeltercomplex met schoorstenen, rangeerspoor, slakkenberg aan het meer; Wikipedia 48.25328,-79.01358, OSM 48.2523,-79.0132) |
| `ag-ccr` | raffinaderij (anodes → kathode, zilveringot) | Canadian Copper Refinery (CCR), Montréal-Est | 45.6172, -73.5171 | [5][6][7][15] | **onzeker** (z15/z16 gezien: industrieterrein met goederenwagons op een emplacement, grote witte loods en twee zwartgedakte hallen; OSM-adresnode 10000 rue Sherbrooke Est; geen bron koppelt dit adres aan CCR, tankhouse niet herkend) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | — | geen | — | enkel spoor, 22 edges, 0 bochten |
| b2 | — | geen via nodig | — | vrije Dijkstra kiest de ONR-lijn en niet Cochrane–CN (~370 km). Dekkingspunten (geen via): Porquis Jct 48.6997, -80.7850 · Matheson 48.5340, -80.4672 · Kirkland Lake-oost 48.1514, -79.9335 |
| b3 | — | geen via nodig | — | Dekkingspunten: Senneterre 48.3811, -77.2299 · Hervey Jct 47.6475, -72.9520 · Joliette 46.0214, -73.4524. ⚠️ OMKERING 179,1° bij 45.6412, -73.5656 (boogstraal 138 m, kopmaak) vlak voor CCR; via 45.6484, -73.5452 blijft hij. Met keerstraf 300 geen oplossing (omkering bij Taschereau 45.4688, -73.6814, 887 km) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kidd Creek Mine + Kidd Met | Discovery Silver (sinds juni 2026; Glencore tot dan) | erts → Cu-/Zn-concentraat; 1,5 Moz Ag (2024) | ≈ 47 t Ag/j | [1][2] |
| Horne-smelter | Glencore Canada | Cu-concentraat + e-schroot → anodes 99,1% | 740 kt concentraat/j, 640 kt zwavelzuur/j; 210 kt Cu+edelmetaal/j | [4][9] |
| CCR | Glencore Canada | anodes + eigen/vreemd anodeslijk → kathode, doré, zilveringot >99,99%, goud, Pt/Pd | 325 kt Cu+edelmetaal/j | [5][6][7] |

## 6 · Stoppunt
De brief stopt bij de CCR-zilveringot (>99,99%): geen bron noemt een afnemer of vervolgzending (LBMA-kluis, munt of fabriek) van CCR-zilver.

## 7 · Open punten
- **Kidd → Horne is niet actueel gebrond:** alleen historisch (15 jaar vóór de eigen smelter, 1967-82) en via Wood Mackenzie (na sluiting 2010 naar "Horne and CCR") [11][13]; Wikipedia zegt "naar Québec". Glencore noemt geen herkomst. Kidd is sinds juni 2026 van Discovery, afname niet gecontroleerd.
- **Modaliteit Kidd → Horne** (spoor versus truck Hwy 101/Rte 101) is niet gepubliceerd; getekend is spoor omdat ONR Timmins–Rouyn bestaat [8] (aannemelijk). Horne → CCR: Glencore zegt "rail car or truck"; spoor getekend.
- **CCR-terrein niet bevestigd** (zie §3, onzeker); het ontwerpcoördinaat 45.6147, -73.5085 (10000 rue Notre-Dame Est) is een olietankenpark en is verworpen. Glencore noemt geen adres.
- **Zilver in het concentraat niet gemeten:** de 47 t Ag/j is mijnproductie; deel naar Horne/CCR, zink-/loodconcentraat en tailingsverlies onbekend.
- **845,6 km is router-lengte, geen gepubliceerde spoorkm;** de ±15%-toets geldt alleen als indicatie. Omkering voor CCR niet dichtgetrokken (bevinding).
- Horne-anodes van andere herkomst (e-schroot 15%, andere concentraten) zijn niet te scheiden van Kidd.

## 8 · Bronnen
[1] Discovery Silver, Kidd Operations — 27 km erts per spoor, 1,5 Moz Ag 2024. https://www.dsvmining.com/English/operations/kidd-operations/default.aspx
[2] Wikipedia, "Kidd Metallurgical Site" — 48°33′N 81°04′45″W, 27 km ZO van de mijn, smelter gesloten 2010. https://en.wikipedia.org/wiki/Kidd_Metallurgical_Site
[3] Wikipedia, "Kidd Creek Mine" — 48.68889, -81.36528; concentraat naar Québec. https://en.wikipedia.org/wiki/Kidd_Creek_Mine
[4] Glencore Canada, Horne "Du concentré au produit fini" — anodes 340 kg per "rail car or truck" naar CCR. http://www.glencore.ca/en/horne/ce-que-nous-faisons/du-concentre-au-produit-fini
[5] Glencore Canada, CCR "Du concentré au produit fini" — doré uit anodeslijk, zilveringot >99,99%. http://www.glencore.ca/en/ccr/ce-que-nous-faisons/du-concentre-au-produit-fini
[6] Glencore Canada, CCR "Nos opérations" — scheidingsfabrieken zilver/goud. https://www.glencore.ca/en/ccr/ce-que-nous-faisons/nos-operations
[7] Glencore Canada, "Filière métallurgique cuivre du Québec" — CCR 325 kt, Horne + CCR geïntegreerd. https://glencore.ca/en/ccr/qui-nous-sommes/filiere-metallurgique-cuivre-du-quebec
[8] Wikipedia, "Ontario Northland Railway" — Porquis–Kidd Creek-spoor, Swastika–Kirkland Lake–Rouyn-Noranda (Nipissing Central). https://en.wikipedia.org/wiki/Ontario_Northland_Railway
[9] Wikipedia FR, "Fonderie Horne" — 847 Moz Ag 1927-2017; anodes per trein of camion naar CCR. https://fr.wikipedia.org/wiki/Fonderie_Horne
[10] Wikipedia, "Horne Smelter" — 48.25328, -79.01358. https://en.wikipedia.org/wiki/Horne_Smelter
[11] Wood Mackenzie, Kidd Creek zink-/kopermijn — na 2010 verwerking bij "Horne and CCR". https://woodmac.com/reports/metals-kidd-creek-zinc-mine-16141226
[12] Wood Mackenzie, Montreal East copper refinery — "road, rail and sea links". https://woodmac.com/reports/metals-montreal-east-copper-refinery-16416201
[13] Northern Miner / Community Stories, Horne-smelter — Kidd-concentraat 15 jaar naar Horne, CCR raffineert (zoekresultaat 2026-10-29, artikel achter betaalmuur). https://www.northernminer.com/news/falconbridge-in-timmins-kidd-creek-milling-and-beyond/1000135827/
[14] OneMine, "Operations at CCR" (1960) — CCR bij spoor en snelweg, verwerkt Noranda-koper. https://onemine.org/documents/operations-at-canadian-copper-refiners-limited
[15] OpenStreetMap (Nominatim/Overpass, ODbL) — Kidd Mine, Fonderie Horne, adresnodes 10000 Sherbrooke/Notre-Dame Est. https://www.openstreetmap.org
[16] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-zilver-kidd-montrealest-{mijn15,met,horne,ccr,ccr16,ccrwide}.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Bestand:** `v2/data/stroomroute-zilver-kidd-montrealest.json` (50,5 KB, versie 2, lonlat) · **titel:** Zilver Kidd Creek Horne CCR · functie `bak_zilver_kidd_montrealest` in `bak_stromen.sh`.
**Recept:** drie runs `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (`--hoofd-km=300 --max-snap=30`, 1-op-1-net, geen via-punten) naar `spoorroute-zilver-kidd-montrealest-{mijn-met,met-horne,horne-ccr}.geojson`, daarna `hecht_marnet.py route` met drie `--been-geojson spoor` en vier `--marker`. Geen zee, haven-aanloop, stippel, weg, lucht of kopie.

| # | modaliteit | km gebakken | km brief | afwijking | naad | opm |
|---|---|---|---|---|---|---|
| 1 | spoor Kidd-mijn → Kidd Met | 29,0 (router 28,8) | 27 gepubliceerd | +7,4% | 0 | binnen ±15% |
| 2 | spoor Kidd Met → Horne | 222,5 (router 221,6) | geen | indicatie | 0,0 | aannemelijk: één bron |
| 3 | spoor Horne → CCR | 849,1 (router 845,6) | geen | indicatie | 0,0 | 1 omkering |
Totaal 1.100,6 km · 2.694 punten · 4 markers (0,07 / 0,15 / 0,30 / 0,18 km van de lijn).

**Toelichting.** Geen stippel: alle drie de benen zijn gemeten en doorgetrokken. Modaliteit b2 (spoor) staat als aannemelijk (één bron, historisch) in de beennaam, niet in de lijnstijl. De km van b2 en b3 zijn router-lengte, geen gepubliceerde spoorkm. De kilometers in het json zijn de geometrielengte en liggen 0,2 tot 0,4% boven de routerlengte van de spoorrouter.
**Bevindingen.** (1) `toets_knikken`: 1 omkering van 179,1 graden bij 45.6412,-73.5656, kopmaak vlak voor CCR, niet te vermijden en niet dichtgetrokken (keerstraf 300 geeft een omkering bij Taschereau, 887 km). (2) CCR-terrein onzeker (OSM-adresnode niet aan CCR gekoppeld), marker staat op het onzekere terreinpunt. (3) Kidd naar Horne alleen historisch gebrond. (4) Geen afnemer van CCR-zilver, stoppunt bij de ingot.
**Lessen.** De drie spoorruns uit de briefschrijffase waren volledig en identiek bruikbaar; het bakken kostte één hecht-marnet-run van 19 s. Spoor-only ketens zonder via-punten zijn het snelste type.
