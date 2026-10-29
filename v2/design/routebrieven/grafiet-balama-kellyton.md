# Routebrief (licht) · Grafiet · Balama → Nacala → New Orleans → Kellyton (Alabama, VS)

**stroom-id:** `grafiet-balama-kellyton` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** natuurlijk vlokgrafiet (concentraat van Syrah) gaat per **truck** over de N380/N1 van de Balama-plant naar de containerterminal van Nacala, per **zeeschip** om de Kaap naar de Napoleon Avenue Container Terminal in New Orleans (haven aannemelijk: geen bron), en per **truck** over I-10, I-65 (Mobile, Montgomery), US-231 en AL-9 naar de Westwater-fabriek bij Kellyton (Coosa County, Alabama) — de derde Amerikaanse verwerker naast Vidalia en Novonix. Eén nieuw landbeen; de trunk Balama–Nacala–New Orleans is een letterlijke kopie.
**Welke as van het verhaal:** *de VS-eigen anodeketen krijgt een derde inlandcorridor, Zuidoost-VS.* **Jaarvolume: 0 kt grafiet/j in 2025** — de plant is in aanbouw, in 2025 alleen kwalificatiemonsters (> 1 t CSPG); Phase I ontwerp 26,5 kt product/j (12,5 kt CSPG + 14 kt SG-fines) [1]. Concentraatvolume uit Balama onbekend. Eenheid kt grafiet/j, peiljaar 2025.

## 1 · Ketenkaart
```
Balama-plant `gr-balama-plant` ──(b1 truck · N380 → Metoro → N1 → Namialo → N12 · 497,9 km — LETTERLIJKE KOPIE bak_grafiet been 1)──► Nacala containerterminal `gr-nacala-kade`
   ──(aanloop Nacala · 152,1 km stippel over water — LETTERLIJKE KOPIE aanloop-nacala.geojson)──► zeeknoop 2148 (-15.0, 41.7)
   ──(b2 zee · Mozambikaanse Straat → Kaap → Zuid-Atlantisch → Golf van Mexico · ca. 17.160 km MARNET — LETTERLIJKE KOPIE bak_grafiet, aannemelijk: haven niet gebrond)──► Napoleon Ave `gr-port-neworleans`
   ──(b3 truck · I-10 → I-65 (Mobile, Montgomery) → US-231 → AL-9 → Kellyton · 583,8 km tool, hemelsbreed 514 km, geen wegkm)──► Westwater Kellyton Graphite Plant `gr-kellyton-plant` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-balama-plant` → `gr-nacala-kade` | N380 → Metoro → N1 → Namialo → N12 | 497,9 gebakken [9] | **kopie** `$BEEN/stroombeen-balama-nacala.geojson` (bak_grafiet been 1 = grafiet-balama-laixi b1) | nee |
| — | A | zee (aanloop) | `gr-nacala-kade` → zeeknoop 2148 | Baai van Nacala | 152,1 [9] | **kopie** `$BEEN/aanloop-nacala.geojson` | ja — MARNET reikt niet (122 km) |
| b2 | B | zee | zeeknoop 2148 → `gr-port-neworleans` (via Southwest Pass) | Indische Oceaan → Kaap → Zuid-Atlantisch → Golf van Mexico → Mississippi-monding | ca. 17.160 gebakken; geen gepubliceerde km [9] | **kopie** van de twee `--been "zee\|…"`-regels in `bak_grafiet` (Nacala → SWP, SWP → New Orleans) | nee — *aannemelijk: één bron voor de bestemming, haven niet gebrond* |
| b3 | C | truck (werkaanname) | `gr-port-neworleans` → `gr-kellyton-plant` | I-10 oost → I-65 N (Mobile, Evergreen, Montgomery) → US-231 Wetumpka → AL-9 (Jacksons Gap) → AL-115 → Kellyton | hemelsbreed 514 km, geen wegkm; tool 583,8; OSRM 586,8 [6] | maak_stroombeen_weg (profiel `grafiet-balama-kellyton-nola-kellyton`, extracts us-louisiana, us-mississippi, us-alabama) | nee — *aannemelijk: Syrah levert, haven en vervoer niet gebrond*; slotstuk 0,32 km rechte ankerverbinding |

Naad b2 → b3 ≈ 0 (zelfde anker Napoleon Ave 29.9123, -90.1120; het weg-profiel begint er op 0,03 km). Haven-aanloop New Orleans: zeeknoop 6185 ligt 9,3 km van de kade (> 5 km), maar de MARNET-route SWP → kade eindigt op de kade zelf (bak_grafiet, marker 56 m van het routeerpunt); geen extra aanloop, zoals in de kopie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-balama-plant` | mijn / laadplek | Balama-plant (Syrah) | -13.3100, 38.6600 | hergebruik `grafiet-balama-vidalia.md` / `grafiet-balama-laixi.md`; sitelaag `w-balama` | bron-gelegd — hergebruik (z14 gezien in eerdere brieven: procesfabriek met bezinkvijvers) |
| `gr-nacala-kade` | overslag truck → zee | Porto de Nacala — containerterminal oostoever | -14.5383, 40.6673 | hergebruik `grafiet-balama-laixi.md` | bron-gelegd — hergebruik |
| `gr-port-neworleans` | losplek zee / overslag zee → truck | Napoleon Avenue Container Terminal, New Orleans | 29.9123, -90.1120 | hergebruik `grafiet-balama-vidalia.md` (satelliet-gelegd z16) | bron-gelegd — hergebruik; als haven voor Westwater **aannemelijk** (geen bron) |
| `gr-kellyton-plant` | verwerkingsknoop / fabriek (eindpunt) | Westwater Kellyton Graphite Plant, Lake Martin Regional Industrial Park, adres 349 McClellan Industrial Drive | 32.9625, -86.0390 | [1][4][7] naam/park/adres; coördinaat zelf van satelliet [8], niet in een bron of in OSM | **aannemelijk** (z15/z16 gezien: nieuw fabriekscomplex met vier grote hallen op kale grond, ronde berm en bluspoel, toegangsweg van US-280 ~1,6 km noordwaarts; het grijsgedakte complex 1 km noordelijker is een ouder, afgebouwd bedrijf en verworpen als Westwater; adres niet te geocoderen) |

## 4 · Via-punten (alleen b3; b1 en b2 zijn kopieën)
Alle punten uit de OSRM-stappen en door de wegscan binnen 0,01 km op de benoemde weg gesnapt; geen enkel punt in een stadscentrum.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | I-10 Louisiana oost | 30.2375, -89.7679 | I-10 oost langs Slidell i.p.v. de I-59/I-55-route via Hattiesburg (ontwerp-corridor, 653 km tegen 587 km) |
| b3 | 2 | I-10 Mississippi kust | 30.4455, -88.7294 | I-10 langs de kust naar Mobile i.p.v. de I-59-route |
| b3 | 3 | I-65 noord van Mobile | 30.9071, -87.9845 | I-65 noord i.p.v. US-43/US-45 |
| b3 | 4 | I-65 bij Evergreen | 31.4665, -86.9578 | I-65 doorrijden naar Montgomery |
| b3 | 5 | I-65 Montgomery | 32.2536, -86.3649 | I-65 buiten het stadscentrum, afslag naar US-231 |
| b3 | 6 | US-231 bij Wetumpka | 32.5458, -86.1907 | US-231/AL-9 noord naar Alexander-City-zone i.p.v. door naar Birmingham/Sylacauga |
| b3 | 7 | AL-9 bij Jacksons Gap | 32.7547, -86.1004 | AL-9 noord (de tool koos zonder dit punt een omweg van 50 km via Sylacauga, 636,6 km) |
| b3 | 8 | AL-9 / AL-115-splitsing | 32.9344, -86.0613 | AL-115 naar Kellyton i.p.v. AL-9 naar Alexander City |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kellyton Graphite Plant (Phase I, in aanbouw sinds Q4 2021) | Westwater Resources / Alabama Graphite Products | vlokconcentraat → gecoat sferisch gezuiverd grafiet (CSPG) + SG-fines | 26,5 kt/j (12,5 CSPG + 14 SG-fines); Phase II ~106 kt/j; ~70 acre | [1] |
| Balama (context) | Syrah Resources | vlokconcentraat | 67 kt geproduceerd 2025 | [9] |

## 6 · Stoppunt
De brief stopt bij de Kellyton-fabriek: de plant produceert nog niet, en de afnemers (SK On, Hiller Carbon) zijn zonder fabriek of adres genoemd [1][2] — fase D en E vervallen.

## 7 · Open punten
- **Kellyton-coördinaat is niet bronbaar:** geen bron noemt een coördinaat; adres 349 McClellan Industrial Drive staat niet in Nominatim/Photon/OSM (OSM kent alleen McClellan Road op 32.972, -86.042). Anker gelegd op het nieuwe hallencomplex (z16), aannemelijk. Fabriek niet in OSM.
- **Toegangsweg onbekend:** het wegbeen eindigt via AL-115 en lokale wegen 0,32 km west van het anker (rechte ankerverbinding); de echte plantweg vanaf US-280 (~1,6 km) staat niet in OSM.
- **Syrah → Westwater is gebrond, Balama → Kellyton niet:** Syrah en Westwater sloten in aug 2023 een bindende offtake (titel Balama) [5]; de 10-K noemt alleen "supply contract with Syrah", geen herkomst, haven of volume [1]. Concentraat kan via Mobile of Savannah komen.
- **Haven New Orleans is aanname** (kopie van de Vidalia-keten); de gekopieerde trunk is ca. 96 % van de km.
- **Geen gepubliceerde wegkm:** de ±15%-toets is een indicatie tegen OSRM (586,8 km, tool 583,8 = -0,5 %). Modaliteit truck is werkaanname; spoor niet uitgesloten.
- **Volume nul:** plant in aanbouw (kosten 128,2 mln van 245 mln eind 2025, vertraagd) [1]; concentraatvolume onbekend; contract met FCA US beëindigd 2025 [1].
- **Backup-feedstock:** de 10-K noemt een niet-FEOC backup-leverancier zonder naam of land [1] — niet getekend.

## 8 · Bronnen
[1] Westwater Resources, Form 10-K FY2025 (SEC): koopt vlokconcentraat onder contract met Syrah; ~70 acre bij Kellyton; Phase I 26,5 kt/j; bouw sinds Q4 2021; SK On, Hiller Carbon, FCA US (beëindigd). https://www.sec.gov/Archives/edgar/data/839470/000110465926032111/wwr-20251231x10k.htm
[2] NS Energy, offtake Hiller Carbon voor 100 % van de fines (~14 kt/j) van Kellyton. https://www.nsenergybusiness.com/news/westwater-resources-announces-off-take-agreement-for-sale-of-100-of-fines-graphite-production-from-its-kellyton-plant/
[3] S&P Global Autotech Insight: Westwater en SK On (niet zelf geopend, via ontwerp). https://autotechinsight.spglobal.com/news/5274256/westwater-resources-signs-first-off-take-agreement-to-supply-graphite-to-sk-on-in-the-us
[4] Westwater/Business Wire, 2022-04-19, ground-breaking: plant in het Lake Martin Regional Industrial Park langs US-280, Coosa County, 349 McClellan Industrial Drive (via zoekresultaat; pagina gaf 403). https://www.businesswire.com/news/home/20220419006039/en/Westwater-Resources-and-Alabama-Graphite-Products-Break-Ground-on-Kellyton-Processing-Plant/
[5] Kallanish, 2023-08-03: Syrah tekent bindende offtake voor Balama-grafiet met Graphex en Westwater (via zoekresultaat; pagina 404) · Africa Energy 2023-08-14: twee nieuwe offtakes met Amerikaanse AAM-verwerkers, geen namen of volumes. https://api.kallanish.com/en/news/power-materials/market-reports/article-details/syrah-inks-new-offtake-agreements-for-its-balama-natural-graphite-0823 · https://www.africa-energy.com/news-centre/article/new-balama-graphite-offtake-deals-pvstorage-plant-complete
[6] OSRM-demoserver (OSM), 2026-10-29: New Orleans → anker 586,8 km via I-10, I-65, AL-152, US-231, AL-9, AL-115; stappen = via-punten §4. https://router.project-osrm.org/
[7] OpenStreetMap via Overpass, 2026-10-29: McClellan Road (way 7400224), AL-115 (7400868), US-280 (827660907); Nominatim/Photon vinden het adres niet. https://overpass-api.de/
[8] Esri World Imagery via `v2/tools/sat_check.py` (live, 2026-10-29): `v2/build-cache/satcheck/sat-grafiet-balama-kellyton-kellyton-a.png`, `-kellyton-b.png`, `-kellyton-z14.png`, `-kellyton-z16.png`.
[9] Atlas: `grafiet-balama-vidalia.md`, `grafiet-balama-laixi.md` (ankers, N380/N1, kopieën), `bak_grafiet` in `v2/tools/bak_stromen.sh`; Syrah Annual Report 2025 (via laixi-brief [1]): Balama 67 kt geproduceerd. https://www.datocms-assets.com/65260/1774572803-syr_2025_annual_report.pdf
[10] Geofabrik us-louisiana, us-mississippi, us-alabama (ODbL), wegscan `v2/build-cache/ais/graaf/grafiet-balama-kellyton-wegscan.log`: 583,8 km, 4.921 punten, snaps ≤ 0,01 km.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Resultaat:** `v2/data/stroomroute-grafiet-balama-kellyton.json` (216,5 KB, versie 2, lonlat) · 5 benen · 18.273,9 km · 10.792 punten · 4 markers. Bakken: `bash v2/tools/bak_stromen.sh grafiet-balama-kellyton` (functie `bak_grafiet_balama_kellyton`).

| # | modaliteit | km | punten | naad naar vorig been | stippel |
|---|---|---|---|---|---|
| b1 | truck Balama → Nacala (kopie) | 497,9 | 3.174 | — | nee |
| aanloop | zee Nacala-kade → zeeknoop 2148 (kopie) | 152,1 | 113 | 0,00 km | ja (MARNET reikt niet) |
| b2a | zee Nacala → Southwest Pass (kopie) | 16.849,0 | 1.853 | 0,00 km | nee |
| b2b | zee Southwest Pass → Napoleon Ave (kopie) | 191,1 | 731 | 0,00 km | nee |
| b3 | truck New Orleans → Kellyton | 583,8 | 4.921 | 0,06 km | nee |

**Recept.** b1, aanloop en b2 zijn letterlijke kopieën uit `bak_grafiet`: de vier beenpunten zijn punt voor punt gelijk aan de eerste vier benen van `stroomroute-pilot.json` (grafiet-balama-vs), dus geen tweede scan en geen tweede routering. b3 is het enige nieuwe been: profiel `grafiet-balama-kellyton-nola-kellyton`, wegscan via `wegscan_puur.py` op us-louisiana, us-mississippi en us-alabama (log `grafiet-balama-kellyton-wegscan.log`), 8 via-punten uit §4, refs I-10, I-65, US-231, AL-9, AL-115, `trimStaart`. Alle snaps ≤ 0,01 km; plant → weg 0,03 km, weg → anker 0,32 km (rechte ankerverbinding).

**Toets.**
- b3 583,8 km tegen OSRM 586,8 = -0,5 %; hemelsbreed 514 km. Er is geen gepubliceerde wegkm, dus de ±15%-toets is een indicatie (binnen de norm), geen norm.
- Naden: max 0,06 km (b2b → b3); geen naad > 5 km. De zee-snap van het eerste zeebeen is 0,000 km (de aanloop eindigt op de zeeknoop zelf).
- Markers: alle vier op 0,0 km van de lijn.
- `toets_knikken.py`: 5 omkeringen, 0 terugloop; b3 heeft 0 omkeringen. De omkeringen zitten in de gekopieerde benen (b1: 1, b2b: 4, spikes bij de Mississippi-monding en de Napoleon-kade) en zijn niet aangeraakt.
- `toets_rechte_benen.py --min-km 5`: geen regel voor deze stroom; de aanloop Nacala is een gekarteerd 113-puntsbeen, geen rechte lijn.
- json.load slaagt, versie 2, punt_formaat lonlat, modaliteiten {truck, zee}, elk been ≥ 2 punten, 216,5 KB.

**Stippel.** Alleen de haven-aanloop Nacala (152,1 km over water, MARNET reikt niet; gekopieerd uit `bak_grafiet`). Het slotstuk van b3 (0,32 km rechte ankerverbinding) zit in het doorgetrokken wegbeen, omdat de plantweg niet in OSM staat en korter is dan 2 km: geen aparte last-mile-stippel getekend.

**Afwijkingen van het ontwerp.** Geen. Het stroom-id noemt het werkelijke eindpunt (Kellyton). Haven New Orleans is een aanname (geen bron), modaliteit truck is werkaanname; dat staat in de beennamen en in §7.

**Lessen.**
- Een stroom met 96 % kopie van een bestaande trunk bakt in seconden; de enige echte kost was de wegscan.
- Via-punt AL-9 bij Jacksons Gap voorkomt de omweg van 50 km via Sylacauga (636,6 km zonder, 583,8 km met).
- Het Kellyton-anker is een satellietblik zonder bron-coördinaat en blijft aannemelijk; de lijn eindigt 0,32 km voor het anker over rechte ankerverbinding, niet erover heen.
