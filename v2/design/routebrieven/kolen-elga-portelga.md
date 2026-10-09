# Routebrief (licht) · kolen — Elga → Pacific Railway → Port Elga (Rusland)

**stroom-id:** `kolen-elga-portelga` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** cokeskool uit de Elga-mijn (Elgaugol/A-Property, Jakoetië) per spoor over de private Tikhookeanskaya
(Pacific) Railway, ~530 km, naar de nieuwe kolenterminal Port Elga
aan de Zee van Okhotsk (Kaap Manorsky, Khabarovsk-kraj); spoor eindigt in OSM ~3,4 km vóór de terminal, geen zeebeen.
**Welke as van het verhaal:** as 5 — Russische cokeskool naar de Pacific, via een **eigen exportcorridor buiten RZD's
BAM/Trans-Sib** om. Elga leverde 35,1 Mt in 2025 (28,6 Mt in 2024), waarvan 26 Mt verscheept en slechts 7 Mt via de
Pacific Railway; het grootste deel ging nog via de Ulak-lijn en BAM naar Vanino [1][2]. Nominale capaciteit lijn en
terminal 30 Mt/j (tweede spoor in aanbouw sinds 04-2025 voor 50 Mt) [2][3].

## 1 · Ketenkaart
```
Elga-mijn `kolen-elga-mijn` ──(b1 spoor · Pacific Railway, privé · ~528 km)──► spoor-einde (OSM, 55.1232/135.6511)
   ──(b2 stippel · last mile, geen net op deze korrel · ~3,4 km)──► Port Elga `kolen-portelga-kade` ⏹ stoppunt
   └── vertakking (niet getekend): grootste volume gaat via Ulak–Elga (321 km) → BAM → Vanino; en zeebestemmingen
       zijn niet gebronde (geen loshaven genoemd) → geen zeebeen
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-elga-mijn` → spoor-einde bij Port Elga | Tikhookeanskaya (Pacific) Railway, geopend 2025/2026 [2][3] | 531 gepubliceerd (GEM/Wikipedia), ~530 (sxcoal) [2][3][5]; gemeten 528,5 (−0,5%) | toets_spoorroute (`BAKE_SUFFIX=-raw`), 1 run, geen via-punt; bestand `spoorroute-kolen-elga-portelga-elga-portelga.geojson` (191 edges, 1.994 punten, 0 bochten, snap kop 0,73 / staart 0,45 km) | nee |
| b2 | A | spoor (last mile) | spoor-einde → `kolen-portelga-kade` | OSM-spoor houdt op in een weide W van de riviermond; terminal ligt O van de monding op de kaap | hemelsbreed ~3,4 (geen wegkm) | stippel `55.1232,135.6511 → 55.1167,135.7021` | ja — "last mile (geen net op deze korrel)" |

Zee: geen been. Geen bron noemt een loshaven voor deze lading (afnemers/loshaven niet gebronnen). Haven-aanloop: n.v.t. Beennaam b1 (voorstel): *"trein Elga → Port Elga (Pacific Railway, cokeskool; 2025: 7 Mt van 35,1 Mt)"*.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-elga-mijn` | mijn / laadgebied | Elga-mijn (Elginskiy, Elgaugol/A-Property), Jakoetië — sitelaag `w-elga` | 56.1994, 130.6358 | [1][4][7] | bron-gelegd (z15 gezien: dagbouwmijn met afgravingsbanken en haulwegen, het punt ligt in het mijnveld; laadstation niet te onderscheiden; OSM-spoor 0,73 km noordelijker, geen last-mile-been) |
| `kolen-portelga-kade` | overslag / kolenterminal | Port Elga, Kaap Manorsky, Zee van Okhotsk (Vanino-havengrens) | 55.1167, 135.7021 | [3][6][8] | **aannemelijk** (z14/z15/z16 gezien: kale rotsige kaap met zandpaadjes en wat bouwputten, geen kade, kranen of stapels — opname ouder dan de ingebruikname; twee onafhankelijke bronnen (OSM `landuse=construction` en Wikipedia 55.1146/135.7025) liggen 0,2 km uit elkaar) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | één private lijn, geen corridorkeuze; vrije Dijkstra gaf 528,5 km, −0,5% t.o.v. 531, 0 bochten ≥ 60° |

Geofabrik-extract: `rusland-verrehoosten` (mijn, hele lijn en terminal).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Elga-mijn + verrijking | Elgaugol / Elga Sibanthracite (ELSI), A-Property | dagbouw cokeskool → verhandelbare cokeskool | 35,1 Mt (2025), 28,6 Mt (2024) | [1][4] |
| Port Elga kolenterminal | Port Elga LLC (A-Property) | spoor → zeeschip | 30 Mt/j (uitbreiding naar 50 Mt) | [2][3] |

## 6 · Stoppunt
De brief stopt op de kade van Port Elga: geen bron noemt een loshaven of afnemer voor deze lading, dus geen zeebeen en geen fase D/E.
Er is geen bestemmingstype gebronnen en niets getekend voorbij de kade.

## 7 · Open punten
- Port Elga is op de satelliet nog niet gebouwd (kale kaap); anker is **aannemelijk**, geen kade-geometrie. Ligging bevestigd door twee bronnen (OSM, Wikipedia) maar niet gezien.
- OSM-spoor houdt 3,4 km vóór de terminal op; de b2-stippel is "geen net op deze korrel", niet "onbekend".
- Onduidelijk in de bronnen: GEM noemt eerste schip in 11-2024 én ingebruikname op 2 september 2026 (Eastern Economic Forum); de 7 Mt van 2025 was dus voor of tijdens de ingebruikname. Brief gaat uit van "in gebruik".
- Het grootste deel (~26 Mt van 35,1 Mt verscheept in 2025) loopt via Ulak–BAM naar Vanino; die route is niet getekend (andere keten).
- Mijnpunt is een GEM/Wikipedia-coördinaat in de put, geen laadstation; Elga-laadstation niet apart gelegd.
- Geen bron voor de verdeling tussen thermische en cokeskool in de Pacific-stroom (Elga is overwegend cokeskool).
- Hemelsbreed 3,4 km voor b2: geen echte kilometer.

## 8 · Bronnen
[1] Global Energy Monitor, Elga (Elginskiy) Coal Mine — coördinaat 56.192426, 130.635752; productie 28,6 Mt (2024), 35,1 Mt (2025); Ulak–Elga 321 km; Pacific Railway 531 km. https://www.gem.wiki/Elga_mine
[2] Sxcoal (Interfax), Pacific Railway/Port Elga-nieuws — lijn ca. 530 km, 30 Mtpa, tweede spoor sinds 04-2025 (50 Mtpa), Elga 35,1 Mt (2025), 26 Mt verscheept, 7 Mt via Pacific Railway; ingebruikname 2 sept 2026. https://en.sxcoal.com/news/detail/2095321632872091650
[3] Global Energy Monitor, Port Elga Coal Terminal — Chumikan, Khabarovsk; 30 Mtpa; eigenaar Port Elga LLC (A-Property); eerste schip 11-2024. https://www.gem.wiki/Port_Elga_coal_terminal
[4] Wikipedia (ru), Эльгинское месторождение — coördinaat 56°11′58″N 130°38′09″E; reserves ~2,2 mld t; Ulak–Elga 321 km; Pacific Railway 500 km. https://ru.wikipedia.org/wiki/Эльгинское_месторождение
[5] Wikipedia (en), Elga coal mine — 531 km lijn naar Port Elga, 55°06′52.7″N 135°42′09.0″E; port 30 Mt/j. https://en.wikipedia.org/wiki/Elga_coal_mine
[6] OpenStreetMap, way 1316635669 `landuse=construction` «Порт Эльга» — 55.1167534, 135.7021275 (via Nominatim). https://nominatim.openstreetmap.org/search?q=Порт+Эльга&format=json
[7] Kolen-sitelaag `v2/design/kolen-sitelaag.json` — site `w-elga`, 56.19944/130.63583, 28,6 Mt (TASS 2024).
[8] Wikipedia (en), Albert Avdolyan — Elga-complex en Pacific Railway naar Port Elga bij Kaap Manorsky. https://en.wikipedia.org/wiki/Albert_Avdolyan
[9] Wikipedia (en, MediaWiki API `prop=coordinates`), Chumikan — 54.7000, 135.2833 (oriëntatie). https://en.wikipedia.org/wiki/Chumikan
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14/z15/z16, live) — `v2/build-cache/satcheck/sat-kolen-elga-portelga-{mijn,spoorstart,spoorend,kaap,terminal,terminal-z16}.png`.
[11] Eigen graaf-proef `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`, 3.260.717 spoor-edges): 528,5 km, `spoorroute-kolen-elga-portelga-elga-portelga.geojson`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh kolen-elga-portelga` (functie `bak_kolen_elga_portelga`); b1 vooraf gebakken met `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=56.1994,130.6358 --naar=55.1215,135.6575 --naam=kolen-elga-portelga-elga-portelga` (1-op-1-net, 191 edges, geen via-punt). Uitvoer `v2/data/stroomroute-kolen-elga-portelga.json`, 37,4 KB, versie 2, lonlat.

| # | modaliteit | km | punten | naad | stippel |
|---|---|---|---|---|---|
| b1 | spoor | 529,5 (brief 531, -0,3%; routertool 528,5) | 1.994 | - | nee |
| b2 | spoor (last mile) | 3,3 (hemelsbreed, geen wegkm) | 2 | 0,0 km | ja, "geen net op deze korrel" |

Totaal 532,8 km, 2 markers (Elga-mijn, Port Elga-terminal). Geen zeebeen, geen haven-aanloop, geen leiding, geen luchtbeen, geen gedeeld been.

**Toets:** km b1 binnen ±15% van 531 (-0,3%); naad b1 -> b2 0,0 km; `toets_knikken.py` 0 knikken, 0 omkeringen; `toets_rechte_benen.py` meldt geen Elga-been (de enige rechte lijn is de bedoelde stippel); json.load, versie 2, punt_formaat lonlat, modaliteit alleen spoor, elk been >= 2 punten. Markerafstand tot de lijn: terminal 0,0 km; mijn 0,73 km (anker is het GEM/Wikipedia-mijnpunt in de put, het OSM-spoor begint 0,73 km noordelijker; < 2 km dus geen last-mile-been, anker ongelijk routeerpunt).

**Stippel b2:** rechte lijn spoor-einde (55.1232, 135.6511) -> terminal (55.1167, 135.7021), 3,3 km hemelsbreed; reden: OSM-spoor houdt in een weide W van de riviermond op, de terminal ligt O van de monding op de kaap; de lijn zegt hier reikt het net niet, niet onbekend. Aannemelijk (één bron voor de kade) staat in de beennaam, niet in de lijnstijl.

**Lessen:** (1) toets_spoorroute (528,5) en hecht_marnet (529,5) meten 1 km verschil door de eindpunt-stub; de brief noemt beide. (2) Een privé-industriële lijn (Pacific Railway) staat compleet in het 1-op-1-net tot de riviermond, dus geen via-punten nodig. (3) Het brief-anker van de terminal is aannemelijk: de kaap is op de satelliet nog kaal.
