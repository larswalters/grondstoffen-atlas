# Routebrief (licht) · Grafiet · Van → Via → Naar (land)

**stroom-id:** `grafiet-vittangi-lulea` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) ·
**status:** gebakken
**Keten in één zin:** natuurlijk vlokgrafiet van de geplande Talga-mijn Nunasvaara South (Södra) bij Vittangi
(Kiruna kommun) per **truck** over de kortste OSM-weg (Vittangi → Tärendö → Överkalix → Råneå) naar het
terrein van Talga's Talnode-anodefabriek op Hertsöfältet in Luleå, Zweden. Eén landbeen; stoppunt de fabriek.
**Welke as van het verhaal:** de volledig Europese mijn-tot-anode-keten van Talga (CRMA-draadje) — **pre-FID,
actueel 0 kt/j**. Plan: gem. **100 kt/j natuurlijk grafiet** (ertsgewicht of concentraat onduidelijk) [1],
tegenover **~25 kt/j grafiet uit ≤120 kt erts/j** [3] en 19,5 kt/j Talnode-C-anode [6]; peiljaar 2025-2026.
Bruikbaar als correctie op het onbevestigde Skaland-voedingsverhaal (`grafiet-skaland-lulea`, §7).

## 1 · Ketenkaart
```
Nunasvaara South-mijn `gr-vittangi-mijn` ──(b1 truck · 395/394/392/98 + E10/E4 · ~307 km gebakken,
hemelsbreed 241 km, geen wegkm, transportwijze niet gebronde aanname)──► Talnode-kavel Hertsön
`gr-lulea-talnode` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-vittangi-mijn` → `gr-lulea-talnode` | mijnweg → Vittangi → Tärendö → Överkalix → Råneå → Luleå (wegen 395, 394, 392, 98, BD 835/867, E10/E4; niet via Kiruna/Gällivare/Boden) | hemelsbreed 241 km, geen wegkm; eigen OSM-scan 306,7 km (indicatie, geen norm) | maak_stroombeen_weg (profiel `grafiet-vittangi-lulea-nunasvaara-hertson`, extract `zweden`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-vittangi-mijn` | mijn / concentrator | Talga Nunasvaara South (Södra), ~10 km W van Vittangi, bij de Hosiojärvi | 67.7047, 21.4094 | [3] (sv.wikipedia-coördinaat; ontwerppunt 67.7250 lag 2,4 km noordelijker in bos) | **aannemelijk** (z15 gezien: ontgraven/kaal gravelvlak van ~150 m in naaldbos, grindwegen langs oost- en zuidzijde, meer NW; geen installaties; mijn niet gebouwd) |
| `gr-lulea-talnode` | losplek / anodefabriek | Talga Talnode, Hertsöfältet, Luleå Industripark (kavel ~10 ha, van de gemeente gekocht) | 65.5670, 22.2840 | [2][4][7]; kandidaat uit gegrade kavels | **onzeker** (z16 gezien: rechthoekige gegrade bedrijfskavels met grindwegen NW van de weg, een grondwerk-/grindbedrijf W ervan, onderstation en loods ZO; welke kavel Talnode is staat in geen bron; NIET 65.58,22.15 = marina) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | — | geen | — | Bewust geen via-punten (haalbaarheidstoets): Kiruna 67.8496/20.3062 en Gällivare 67.3/20.25 forceren een omweg (Gällivare lag 30 km mis); de vrije kortste weg gaat via Tärendö/Överkalix/Råneå. Uitvoer: route passeert Vittangi 1,2 km, Tärendö 1,0, Överkalix 1,1, Råneå 0,4 km; Kiruna 49, Boden 23, Gällivare 68 km ernaast |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nunasvaara South (mijn + concentrator, gepland) | Talga Group | erts → grafietconcentraat | plan 100 kt/j [1] of ~25 kt/j uit 120 kt erts [3][6]; **actueel 0** | [1][3][6] |
| Talnode-fabriek, Luleå (gepland) + EVA-pilot | Talga Group | concentraat → Talnode-C anode | 19,5 kt/j anode (plan) [6]; EVA 50 t/j draait sinds 2022 op proefmijnvoorraad | [2][6] |

## 6 · Stoppunt
De brief stopt bij de Talnode-kavel: dat is de enige door één bron genoemde afnemer van Vittangi-grafiet; wat
daarna met het anodemateriaal gebeurt (naar EU-gigafabrieken) heeft geen locatie in de bronnen. Fase D/E vervallen.

## 7 · Open punten
- **Transportwijze mijn → Luleå staat in geen Talga-bron** [1][2][6]; truck is een aanname (Malmbanan/spoor niet onderzocht). **Corridor niet bronbepaald:** de E10-route via Gällivare en Boden is langer en niet gekozen.
- **Pre-FID:** concessie en milieuvergunning 2024 van kracht [1][3], besluit nog niet genomen; Talnode-FID niet genoemd op de Talga-pagina [2]. Jaarvolume actueel 0.
- **Volume-discrepantie:** Talga 100 kt/j natuurlijk grafiet [1] vs sv.wikipedia ~25 kt/j uit 120 kt erts [3]; eenheid (ertsgewicht of concentraat) onduidelijk.
- **Talnode-kavel niet gevonden:** Hertsöfältet (10 ha) staat in zoekresultaten [7], geen coördinaat; kandidaat 65.5670, 22.2840 is een gegrade kavel (onzeker). OSM kent geen Talga-object (Photon: alleen plaats Hertsön 65.5867, 22.2498).
- **Raakt `grafiet-skaland-lulea`:** die brief heeft `gr-lulea-talnode` op 65.58, 22.15 (marina), ~6 km van dit anker; hier niet aangepast, centraal beslissen. Talga's eigen pagina noemt alleen Vittangi als voeding.
- **Mijnpunt `w-talga-lulea` in de sitelaag** is de marina-coördinaat; een mijnpunt Nunasvaara ontbreekt daar (niet aangepast).
- Eerste 4,6 km vanaf de mijn en laatste 7,5 km naar de kavel gaan over kleine wegklassen (unclassified/residential/service); de kavelweg is niet bevestigd.

## 8 · Bronnen
[1] Talga Group, Vittangi-pagina, 2026 — Nunasvaara South, gem. 100.000 t/j hoogwaardig natuurlijk grafiet; concessie goedgekeurd, milieuvergunning van kracht. https://www.talgagroup.com/our-operations/vittangi/
[2] Talga Group, Luleå-pagina — Luleå Industrial Park, EVA 50 t/j sinds 2022 op Vittangi-proefmijnerts, raffinaderij nog te bouwen. https://www.talgagroup.com/our-operations/lulea/
[3] sv.wikipedia, Nunasvaara Södra — 67,70472 / 21,40944, 10 km W van Vittangi, ≤120.000 t erts → ~25.000 t grafiet/j, besluit nog niet genomen. https://sv.wikipedia.org/wiki/Nunasvaara_S%C3%B6dra
[4] sv.wikipedia, Talga Group — fabriek op Hertsön, grondvoorbereiding sept 2023. https://sv.wikipedia.org/wiki/Talga_Group
[5] sv.wikipedia, Vittangi — 67,677 / 21,645, E45 door het dorp. https://sv.wikipedia.org/wiki/Vittangi
[6] EIB/rightsindevelopment, Talga Anode Production (EIB-20220643) — mijn 120 kt erts/j, Luleå 19,5 kt/j Talnode-C. https://ewsdata.rightsindevelopment.org/projects/20220643-talga-anode-production/
[7] Zoekresultaat (Kallanish, batteryindustry.net) — 10 ha kavel Hertsöfältet, Luleå Industrial Park, van de gemeente gekocht; bouwvergunning maart 2023. https://api.kallanish.com/en/news/power-materials/market-reports/article-details/talga-group-buys-land-for-its-anode-refinery-in-sweden
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-grafiet-vittangi-lulea-mijn.png`, `-hertson16.png`, `-talnode-hertson.png`.
[9] Photon (OSM) — plaats Hertsön 65,5867 / 22,2498; Geofabrik-extract zweden, eigen wegscan 306,7 km.
[10] v1-register `data/graphite.js` (`gr-ref-sweden`, 65.58/22.15) en `v2/design/grafiet-sitelaag.json` (`w-talga-lulea`).

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)

**Uitvoer:** `v2/data/stroomroute-grafiet-vittangi-lulea.json` (93,4 KB, versie 2, lonlat) · functie `bak_grafiet_vittangi_lulea` in `v2/tools/bak_stromen.sh` · profiel `grafiet-vittangi-lulea-nunasvaara-hertson` in `v2/tools/maak_stroombeen_weg.py` · tussenuitvoer `v2/build-cache/ais/graaf/grafiet-vittangi-lulea-weg-nunasvaara-hertson.geojson`.

| # | modaliteit | been | km gemeten | km brief | naad | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | Nunasvaara South (Vittangi) → Talnode Hertsön, kortste weg via Tärendö–Överkalix–Råneå | **306,7** (4795 punten) | hemelsbreed 241, geen wegkm | n.v.t. | nee |

Totaal 306,7 km, 1 been, 2 markers (beide 0,0 km van de lijn). Geen zee, spoor, leiding, lucht, haven-aanloop of kopie.

**Recept:** `python v2/tools/wegscan_puur.py --profiel grafiet-vittangi-lulea-nunasvaara-hertson` (extract `zweden`, geen via-punten, `vensterKm` 75, snaps 0,06 km bij de mijn en 0,16 km bij de kavel) en daarna `bash v2/tools/bak_stromen.sh grafiet-vittangi-lulea`.

**Toets:** de ±15%-toets is hier geen norm (geen gepubliceerde wegkm); omwegfactor 306,7/241 = 1,27, gebruikelijk voor het dunne Noord-Zweedse net. `toets_knikken.py`: 17 knikken ≥ 60 gr (rijdbare bochten, spikes van 3 tot 20 m), 0 omkeringen, 0 terugloop. json.load slaagt, modaliteit truck, ≥ 2 punten, bestand 93 KB.

**Lessen / bevindingen:**
- De route volgt de vrije kortste weg en passeert Vittangi 1,2 km, Tärendö 1,0, Överkalix 1,1 en Råneå 0,4 km; Kiruna ligt 49, Boden 23 en Gällivare 68 km ernaast. Een via-punt in Kiruna of Gällivare gaf een omweg (Gällivare 30 km mis), dus bewust weggelaten.
- Eerste 4,6 km vanaf de mijn en laatste 7,5 km naar de kavel gaan over kleine wegklassen; de kavelweg is niet bevestigd.
- Ankers: mijn aannemelijk (sv.wikipedia-coördinaat, z15 ontgraven plek), Talnode-kavel onzeker (Hertsöfältet; kavel niet gevonden). Transportwijze truck is een niet-gebronde aanname.
- Niet aangepast, centraal beslissen: `grafiet-skaland-lulea` heeft `gr-lulea-talnode` op de marina (65,58 / 22,15), ~6 km van dit anker; sitelaag `w-talga-lulea` staat op die marina en mist een mijnpunt Nunasvaara.
- Het eerdere profielcommentaar noemde 321,2 km en Junosuando (haalbaarheidsscan); gecorrigeerd naar de gebakken 306,7 km.
