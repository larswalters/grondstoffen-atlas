# Routebrief (licht) · zilver — Tara Mines (Navan, Ierland) → Dublin Port → Kokkola (Finland)

**stroom-id:** `zilver-tara-kokkola` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** zinkconcentraat van Boliden Tara Mines (Navan) per **truck** (M3 → M50 → Dublin Port Tunnel; het Navan–Drogheda-spoor ligt stil) naar Alexandra Basin West in Dublin Port, per **zeeschip** door Noordzee/Skagerrak/Oostzee/Botnische Golf naar Port of Kokkola, 1,3 km van de Boliden-zinksmelter die sinds 2014 zilver uit het concentraat terugwint; keten stopt bij Kokkola.
**Welke as van het verhaal:** *Ierse zinkmijn → Finse zilverterugwinner.* Tara maalde 1,4 Mt erts in 2025 [3]; capaciteit ~400 kt zink- en ~50 kt loodconcentraat/j (Boliden) [9], Wikipedia noemt 200 kt/40 kt [1]. Boliden Kokkola won **20 t Ag** in 2025 [2]. Zilverinhoud van Tara-concentraat en het Tara-aandeel in Kokkola zijn niet gepubliceerd (Wikipedia: concentraat gaat naar Kokkola, Odda en andere smelters [1]): **aannemelijk, één bron**.

## 1 · Ketenkaart
```
Tara Mines `ag-tara-mijn` ──(b1 truck · M3 → N3 → M50 → Port Tunnel · 62,6 km gemeten, hemelsbreed 47)──► Dublin Port, Alexandra Basin West `ag-dublin-kade`
  ──(b2 zee · haven-aanloop 8,5 km + MARNET ~3.236 km + haven-aanloop Kokkola 25,4 km, aannemelijk)──► Port of Kokkola `ag-kokkola-kade`
  ═══ knoop 1,3 km (geen been): Boliden Kokkola zinksmelter `ag-kokkola-smelter` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ag-tara-mijn` → `ag-dublin-kade` | R147 Navan → M3 → N3 → M50 (noord) → Dublin Port Tunnel → havenwegen; **aannemelijk, spoor buiten dienst, ertsvervoer per weg** [4] | hemelsbreed 47 km, geen wegkm; gemeten 62,6 km (indicatie, +33% op hemelsbreed) | profiel `zilver-tara-kokkola-tara-dublin` in `maak_stroombeen_weg.py` (extract ierland, al gescand) | nee |
| b2a | B | zee | `ag-dublin-kade` → zeeknoop 7778 (53.3221,-6.1189) | Liffeymonding → Dublin Bay | 8,5 km (maak_havenaanloop, gemeten) | kade ligt 7,5 km van de zeeknoop (> 5 km) | ja: aanloop, stippel |
| b2b | B | zee | `ag-dublin-kade` → `ag-kokkola-kade` | Ierse Zee, noord om Schotland of Kanaal, Skagerrak, Kattegat, Deense Straten, Oostzee, Botnische Golf (router kiest) | ~3.236 (MARNET-meting uit de toets, geen bron) | MARNET kade → kade | nee |
| b2c | B | zee | zeeknoop 8821 (64.0369,22.7535) → `ag-kokkola-kade` | Kvarken-scherenkust | 25,4 | **letterlijke kopie** `kobalt-kcc-kokkola-aanloop-kokkola.geojson` (functie `bak_kobalt_kcc_kokkola`) | ja: aanloop, stippel |
| — | C | — | `ag-kokkola-kade` → `ag-kokkola-smelter` | havenweg Kokkola Industrial Park, 1,3 km | 1,3 | geen eigen been (< 2 km, lichte werkwijze); marker | n.v.t. |

Spoor is bewust **niet** getekend: Navan–Drogheda is buiten dienst door de Dublin Port-werken en Tara rijdt per weg [4]; het 1-op-1-net kent geen spoor rond Navan. Wikipedia noemt het spoor nog [1] (verouderd).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-tara-mijn` | mijn / laadplek | Tara Mines (Boliden), Navan | 53.6553, -6.7150 | [1] Wikipedia-coördinaat, [3] | bron-gelegd (z15 gezien: oppervlaktecomplex met concentrator, opslaghallen, wegenstructuur en turquoise bekkens; kruis ligt op het procescomplex) |
| `ag-dublin-kade` | overslag truck → zee | Dublin Port, Alexandra Basin West, noordkade | 53.3490, -6.2217 | [5] erts-laadsysteem ligt in Alexandra Basin West; [6] oude laadband op een pier in het bekken; eigen satellietblik | **aannemelijk** (z18 gezien: bulkkade met bulkcarrier, mobiele kraan/hopper en loodsen; dat het erts-laadsysteem daar nu staat is niet te onderscheiden — het is verplaatst/gesloopt in ABR) |
| `ag-kokkola-kade` | overslag zee → land | Kokkolan syväsatama (Deep Port), Port of Kokkola | 63.8645, 23.0270 | **hergebruikt letterlijk** uit `kobalt-kcc-kokkola` (`co-kokkola-kade`), ook `nikkel-sotkamo-kokkola` | bron-gelegd (elders: pier met kranen, bulk in hopen) |
| `ag-kokkola-smelter` | verwerkingsknoop (marker) | Boliden Kokkola, zinksmelter, Kokkola Industrial Park | 63.8631, 23.0540 | [2] + OSM-object, genoemd in `kobalt-kcc-kokkola` §3 [7] | bron-gelegd (elders: OSM `man_made=works`, 1,3 km van de kade) |

## 4 · Via-punten (b1, alle op de motorweg, geen stadscentra)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | M3 ten zuiden van Dunshaughlin | 53.4897, -6.5293 | corridorkeuze M3 (motorway) versus de oude R147/N3 |
| b1 | 2 | M3-einde bij Clonee | 53.4090, -6.4279 | overgang M3 → N3 naar de M50 |
| b1 | 3 | M50 noordzijde, J6 → J5 | 53.4014, -6.3198 | kiest de noordelijke M50 (met de klok mee) naar de Port Tunnel |
| b1 | 4 | M50 noordzijde bij Ballymun | 53.4087, -6.2737 | pint M50 versus M1/R132 (Swords Road) |
| b1 | 5 | M50/M1-knoop, afrit Port Tunnel | 53.3993, -6.2366 | tunnelafrit |
| b1 | 6 | Dublin Port Tunnel, zuidmond | 53.3583, -6.2317 | tunnel, havenuitrit East Wall |

Refs `["M3","M50","M1"]`; extract `ierland`; venster 25 km; `eindToegangPrivaat: True` (mijnterrein: service-wegen, snap 0,05 km). Alle snaps ≤ 0,05 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tara Mines (mijn + concentrator), Navan | Boliden | erts → zink-/loodconcentraat (met zilver in het concentraat) | 1,4 Mt erts 2025; ~400 kt Zn-conc./j capaciteit; Ag niet gepubliceerd | [1][3][9] |
| Boliden Kokkola, zinksmelter | Boliden | zinkconcentraat → zink; zilverterugwinning sinds 2014 | 20 t Ag in 2025 (hele smelter) | [2] |

## 6 · Stoppunt
De brief stopt bij Kokkola: het zilverhoudende concentraat wordt daar verwerkt en het zilverconcentraat gaat naar een niet genoemde raffinaderij — geen bron noemt een volgende locatie; fase D/E vervallen.

## 7 · Open punten
- **Zilverinhoud Tara-concentraat en Tara-aandeel in Kokkola niet gepubliceerd** (Boliden-site noemt Tara niet bij Kokkola [2]); de haalbaarheidstoets meldt dat Mining Weekly Tara vooral Odda noemt — niet zelf getoetst. Label: aannemelijk, één bron [1].
- **Spoor buiten dienst** (Meath Chronicle, 2025-02-25 [4]); hervatting na de Dublin Port-werken onbekend. Het wegbeen geldt voor de huidige situatie.
- **Laadplek in Dublin onzeker:** het erts-laadsysteem is binnen Alexandra Basin West verplaatst [5]; afbeelding toont een bulkkade, geen bevestigd ertslaadsysteem; Afloat-bericht over de sloplijst niet zelf gelezen (403).
- **Wegkm niet gepubliceerd:** 62,6 km is een routegeometrie, geen bron; toets +-15% is indicatie.
- **Haven-aanloop Dublin (8,5 km)** snijdt de 1:10M-kust (0,23 km aan de uiteinden): schematisch, stippel, geen bevaren geul.
- Reisroute zee (noord om Schotland of Kanaal) is aan de router; MARNET-km 3.236 komt uit de toets.

## 8 · Bronnen
[1] Wikipedia, "Tara Mines" (coördinaat 53.6553,-6.7150; concentraat via Dublin Port naar Kokkola en Odda). https://en.wikipedia.org/wiki/Tara_Mines
[2] Boliden Kokkola — zilverterugwinning sinds 2014, 20 t Ag in 2025. https://www.boliden.com/operations/smelters/boliden-kokkola
[3] Boliden Tara — 1,4 Mt erts verwerkt in 2025. https://www.boliden.com/operations/mines/boliden-tara
[4] Meath Chronicle, 2025-02-25 — spoor Navan–Drogheda dicht door Dublin Port-werken, Tara per weg. https://www.meathchronicle.ie/?p=119354
[5] An Bord Pleanála, ABR-dossier (r322353) — verplaatsing ore concentrates loading system in Alexandra Basin West. https://www.pleanala.ie/anbordpleanala/media/abp/cases/reports/322/r322353.pdf
[6] Irish Railway Modeller-forum, Dublin Port Alexandra Basin (2019–2020) — ertsband op pier in het bekken (forum, zwakke bron). https://irishrailwaymodeller.com/topic/7419-dublin-port-alexandra-basin/
[7] Interne brief `kobalt-kcc-kokkola.md` — kade, smelter-OSM-object, aanloop Kokkola, zeeknoop 8821.
[8] Interne brief `nikkel-sotkamo-kokkola.md` — kade Kokkola hergebruikt.
[9] Boliden, "Tara zinc mine in Ireland back in full production" — capaciteit ~400 kt/50 kt. https://investors.boliden.com/en/press/bolidens-tara-zinc-mine-ireland-back-full-production-59913
[10] Esri World Imagery via `sat_check.py`: `sat-zilver-tara-kokkola-tara.png`, `-dublin-alex.png`, `-dublin-z16.png`, `-dublin-z17.png`, `-dublin-kade.png`, `-dublin-anker.png`.
[11] Geofabrik Ierland-extract (OSM), pure-Python scan `wegscan_puur.py`; haalbaarheidstoets (intern, 2026-11-01).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
`v2/data/stroomroute-zilver-tara-kokkola.json` (27,5 KB, versie 2, lonlat), 4 benen, 3.332,8 km, 1.387 punten, 4 markers (Tara, Dublin kade, Kokkola kade, Boliden Kokkola). Recept: `bak_zilver_tara_kokkola` in `bak_stromen.sh`.

| # | modaliteit | been | km | stijl |
|---|---|---|---|---|
| b1 | truck | Tara Mines → Dublin Alexandra Basin West (R147/M3/M50/Port Tunnel), letterlijk `zilver-tara-kokkola-weg-tara-dublin.geojson` | 62,6 (brief: hemelsbreed 47, geen wegkm) | doorgetrokken |
| b2a | zee | haven-aanloop Dublin, kade → zeeknoop 7778 | 8,5 | stippel |
| b2b | zee | MARNET Dublin kade → Kokkola kade (snaps 7,45 en 23,36 km) | 3.236,3 (brief ca. 3.236) | doorgetrokken |
| b2c | zee | haven-aanloop Kokkola, zeeknoop 8821 → kade, letterlijke kopie `kobalt-kcc-kokkola-aanloop-kokkola.geojson` | 25,4 | stippel |

**Toets.** Naden alle 0,0 km; markers 0,0 km van hun lijn, behalve Boliden Kokkola (1,33 km, bedoeld: marker zonder been, brief 1,3 km). b1 is +33% op hemelsbreed: indicatie, geen norm. Knikken: geen omkering of terugloop meer; 14 knikken op b1 zijn korte spikes (5 tot 47 m) op ramps en mijnterrein, zee drie krappe bochten (Schotland, Sont, Ierse Zee).
**Toelichting stippel.** Dublin-aanloop 0,23 km over de 1:10M-kust (schematisch, geen bevaren geul). Kokkola-aanloop 25,4 km over de Kvarken-scherenkust.
**Les.** Het gescande b1-geojson had een terugloop van 173,6 gr (stekel van ~50 m op de M50, 53.4052,-6.3126); de twee apexpunten zijn met de hand verwijderd (999 naar 997 punten) en herbakt. Een volgende wegscan van dit profiel zou de stekel opnieuw leveren.
**Open.** Zilverinhoud en Tara-aandeel in Kokkola niet gepubliceerd; spoor stil; Dublin-laadplek aannemelijk.

