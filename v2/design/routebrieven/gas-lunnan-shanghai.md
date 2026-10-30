# Routebrief (licht) · gas — Lunnan (Tarim-bekken) → Korla → Turpan → Jiuquan-aansluiting (China, West–Oost-lijn I, gemeten deel)

**stroom-id:** `gas-lunnan-shanghai` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Tarim-aardgas gaat vanaf het beginstation bij Lunnan (Xinjiang) over de **West–Oost-gasleiding, lijn I (西气东输一线)** langs Korla en Turpan en door de Gobi naar Liuyuan, Yumen en de Jiuquan-aansluiting (Gansu). Daar eindigt het OSM-bewijs: het vervolg tot Shanghai (Baihe) staat in OSM alleen als schematische "approximate continuation" en wordt niet getekend.
**Welke as van het verhaal:** Tarim-gas naar de Jangtse-delta, het oorspronkelijke West–Oost-project. **12 bcm/j ontwerpcapaciteit (2004), opgewaardeerd naar 17 bcm/j** [1][2][3]. Capaciteit, geen gemeten doorzet: een jaarvolume voor lijn I alleen is niet gevonden (systeem West–Oost > 100 bcm/j in 2021 [2], dat is alle lijnen samen).
**Titel-afwijking:** het id belooft Shanghai, de lijn eindigt bij Jiuquan (39.6300, 98.4340). Gemeten 1.323,5 km van 4.000 km (Lunnan–Shanghai [1]).

## 1 · Ketenkaart
```
Lunnan-beginstation `gas-lunnan-start` (Tarim Oilfield, Luntai; OSM-leidingbegin)
  ──(b1 leiding · OSM way 1324962088 · 139,6 km)──► Korla-naad west (41.8528, 85.7544)
  ──(b2 leiding · OSM-gat bij Korla · 40,5 km hemelsbreed, STIPPEL)──► (41.7753, 86.2325)
  ──(b3 leiding · OSM ways 1448355433 + 1450151225 + 1450151228 · 172,9 km)──► Turpan-naad west (42.0582, 88.0893)
  ──(b4 leiding · OSM-gat Turpan-bekken · 16,4 km hemelsbreed, STIPPEL)──► (42.1430, 88.2515)
  ──(b5 leiding · OSM way 185011116 + 331022098 + 631355360 + 631355359 + 314999413 + 314999415 · 954,0 km, via Hami-zuid, Liuyuan, Yumen)──►
Jiuquan-knoop `gas-jiuquan-knoop` (39.6300, 98.4340) ═══ stoppunt (einde OSM-bewijs) ═══   [Shanghai niet getekend]
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-lunnan-start` → Korla-naad west | 西气东输一线, Lunnan–Korla | **139,6** OSM-gemeten; geen gepubliceerde leidingkm voor dit stuk | `leiding` pre-gestikt (way 1324962088) | nee |
| b2 | B | leiding | Korla-naad west → Korla-naad oost | idem (OSM-gat) | 40,5 hemelsbreed, geen leidingkm | `--stippel` rechte lijn | **ja — geen OSM-way tussen de twee uiteinden (Korla)** |
| b3 | B | leiding | Korla-naad oost → Turpan-naad west | 西气东输一线, Korla–Turpan-bekken | **172,9** OSM-gemeten | `leiding` pre-gestikt | nee |
| b4 | B | leiding | Turpan-naad west → Turpan-naad oost | idem (OSM-gat) | 16,4 hemelsbreed, geen leidingkm | `--stippel` rechte lijn | **ja — geen OSM-way tussen de twee uiteinden** |
| b5 | B | leiding | Turpan-naad oost → `gas-jiuquan-knoop` | 西气东输一线, Hami-zuid, Liuyuan, Yumen, Jiuquan | **954,0** OSM-gemeten (1 naad 0,3 km bij 41.656, 94.479 rechtgetrokken); geen gepubliceerde leidingkm | `leiding` pre-gestikt | nee |

Doorgetrokken **1.266,6 km**, stippel **56,9 km** (4,3%), totaal 1.323,5 km; hemelsbreed start–einde 1.217 km (omwegfactor 1,04). De ±15%-toets heeft hier geen gepubliceerde deellengte: alleen indicatie (4.000 km totaal [1], 4.200 km in andere bron [3]).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-lunnan-start` | kop leiding / beginstation | Lunnan-beginstation West–Oost-lijn I (轮南, Luntai, Bayingolin) | 41.4648, 84.2141 | [2][6][7][8] | aannemelijk (z15 gezien: eerste punt van de OSM-leiding ligt aan de rand van een laagbouwcompound met rode daken, 0,9 km ten zuiden van een groot tankpark/verwerkingscomplex; station zelf niet los herkenbaar) |
| `gas-jiuquan-knoop` | stoppunt / einde OSM-bewijs | OSM-leidingknoop bij Jiuquan, Gansu | 39.6300, 98.4340 | [6][8] | onzeker (z14 en z16 gezien: open woestijn tussen kassen/zoutpannen en de rijksweg, geen station; hier begint de schematische way 578805788) |

Verworpen: het ontwerpanker 41.4734, 84.2515 is een tussenpunt op de leiding (bij z15 kale woestijn, 3,3 km oostelijk van het begin). Stadscentroïde Lunnan (41.4810, 84.2531 [7]) is geen anker.

## 4 · Via-punten
Niet van toepassing (leiding: OSM-geometrie of stippel, geen corridorkeuze door ons). Geen markers op de naden (geen sites).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lunnan (Tarim-gasaanvoer, beginstation) | PetroChina/Tarim Oilfield | gas uit Kuqa–Tabei-velden (Kela-2, Dina-2 e.a.) → lijn I | 12 bcm/j ontwerp, 17 bcm/j na opwaardering | [1][2][3] |
| Compressorstations onderweg (22 volgens ontwerp, posities niet gelegd) | PetroChina West–East Gas Pipeline Co | drukverhoging | 35 stations in totaal, 22 compressie [2] | [2] |
| Jiuquan-aansluiting | idem | onbekend (geen site gezien) | — | [8] |

## 6 · Stoppunt
`gas-jiuquan-knoop`: hier eindigt het OSM-bewijs. Het vervolg (Shandan, Zhongwei, Xi'an, Zhengzhou, Nanjing, Shanghai/Baihe) is in OSM alleen één schematische way van 2.378 km met segmenten tot 380 km (tag "approximate continuation"); die tekenen we niet (haalbaarheidstoets). Fase D/E vervallen: geen bron noemt één fabriek of afnemer.

## 7 · Open punten
- **Het eindpunt Shanghai/Baihe is niet getekend**; id blijft staan, titel noemt Jiuquan. Eindanker `gas-jiuquan-knoop` is een kaartknoop zonder zichtbare site (onzeker).
- **Naden:** Korla 40,5 km en Turpan-bekken 16,4 km zijn OSM-gaten (stippel, rechte lijn, geen leidingkm). Bij Hami ligt een naad van 0,3 km (rechtgetrokken in de geometrie).
- **Parallelle lijnen:** 西气东输 dekt lijn I tot en met IV; naast ways 1324962088 en 185011116 liggen 二线轮吐支干线 (1324962089, 1448355434, 1448355428) en lijn IV (四线). Gekozen zijn uitsluitend ways met naam 西气东输一线 en de naamloze 西气东输-ways tussen Liuyuan en Jiuquan; of die fysiek lijn I zijn, is niet onafhankelijk bevestigd.
- **Schematische stukken:** ways 314999413 (12,5 km, tag "approximate route"; één segment van 8,2 km) en lange rechte segmenten van 10-15 km in way 185011116 (Gobi, 91-94 °O) en 1448355433 (87,4-87,7 °O). Km-indicatie, geen norm.
- Geen gemeten doorzet voor lijn I alleen; 12 bcm/j is ontwerp (2004), 17 bcm/j opwaardering (2005-2009, bronnen verschillen) [2][3]. Gloedgewicht: 17 bcm/j aanhouden tot een gemeten cijfer bestaat.
- Lengtebronnen 4.000 km [1][2] en 4.200 km [3] spreken elkaar tegen; gemeten stuk niet te toetsen tegen een gepubliceerde deellengte.
- Compressorstations en afsluiters zijn niet gelegd (geen coördinaat in een bron).
- Gereedschap: pyosmium geblokkeerd, Overpass en Firecrawl niet gebruikt; geometrie uit een eigen pure-python PBF-scan van `china-latest.osm.pbf` (alleen `substance=gas`).

## 8 · Bronnen
[1] Wikipedia, "West–East Gas Pipeline" (Lunnan–Shanghai ~4.000 km, 12 bcm/j, upgrade 17 bcm/j, Tarim-bron) https://en.wikipedia.org/wiki/West%E2%80%93East_Gas_Pipeline
[2] Wikipedia (zh), "西气东输" (route Lunnan, Korla, Turpan, Shanshan, Hami, Liuyuan, Yumen, Jiuquan; 4.000 km; 35 stations; 120 naar 170 亿 m3 na 2005; >1.000 亿 m3 systeem 2021) https://zh.wikipedia.org/wiki/%E8%A5%BF%E6%B0%94%E4%B8%9C%E8%BE%93
[3] Offshore Technology, "West-East Gas Pipeline" (17 bcm/j na opwaardering 2009, bevoorrading Tarim) https://www.offshore-technology.com/projects/west-east/
[4] Global Energy Monitor, "West-East Gas Pipeline 1" (alleen via zoekresultaat; pagina gaf 403) https://gem.wiki/West-East_Gas_Pipeline_1
[5] Natural Gas World, "China's West-East pipeline has supplied 18.7 bcm of gas to Ningxia" (alleen cumulatief Ningxia, geen lijn I-volume) https://naturalgasworld.com/chinas-west-east-pipeline-has-supplied-18.7-bcm-of-gas-to-ningxia-till-date-19000
[6] OpenStreetMap-bijdragers (ODbL), Geofabrik `china-latest.osm.pbf`, eigen PBF-scan `man_made=pipeline substance=gas`: `v2/build-cache/ais/graaf/gas-lunnan-shanghai-pbfscan-china.json`, stiksel `gas-lunnan-shanghai-stitch.py` https://www.openstreetmap.org/copyright
[7] OSM/Nominatim: 轮南镇 centroïde 41.4810, 84.2531 https://nominatim.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-gas-lunnan-shanghai-{lunnan-station,lunnan-osmstart,jiuquan-knoop,jiuquan-eind}.png`.
[9] Yicai Global, "China's fourth West-East gas pipeline comes fully online" (lijn IV, context; niet herlezen) https://www.yicaiglobal.com/news/chinas-fourth-west-east-gas-pipeline-comes-fully-online-boosting-capacity

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Bestand:** `v2/data/stroomroute-gas-lunnan-shanghai.json` (21,1 KB, versie 2, lonlat) · functie `bak_gas_lunnan_shanghai` in `v2/tools/bak_stromen.sh` · geen wegprofiel, geen extract, geen zee/spoor/vlucht/aanloop/kopie. Titel: "Gas · Lunnan (Tarim) → Korla → Turpan → Jiuquan-knoop (West-Oost-lijn I, China)" (id belooft Shanghai, lijn eindigt bij Jiuquan).

| # | modaliteit | km (bake) | brief | punten | naad naar vorig | stippel |
|---|---|---|---|---|---|---|
| 1 | leiding Lunnan → Korla | 139,6 | 139,6 OSM | 131 | — | nee |
| 2 | leiding OSM-gat Korla | 40,5 | 40,5 hemelsbreed | 2 | 4 m | ja (geen OSM-way) |
| 3 | leiding Korla → Turpan-bekken | 172,9 | 172,9 OSM | 161 | 2 m | nee |
| 4 | leiding OSM-gat Turpan-bekken | 16,4 | 16,4 hemelsbreed | 2 | 1 m | ja (geen OSM-way) |
| 5 | leiding Turpan → Jiuquan-knoop | 954,0 | 954,0 OSM | 731 | 6 m | nee |

Totaal 1.323,4 km (doorgetrokken 1.266,5 km, stippel 56,9 km = 4,3%), max naad 6 m. Markers: Lunnan-beginstation 7 m van de lijn, Jiuquan-knoop 2 m.

**Recept:** drie voorgestikte FeatureCollections uit de eigen PBF-scan (`gas-lunnan-shanghai-stitch.py`, OSM `man_made=pipeline substance=gas`) als `--been-geojson`, twee rechte `--stippel` over de OSM-gaten, via `hecht_marnet.py route` (geen zee, dus de graaf/MARNET werden alleen geladen). Eén bake, geen herbake.
**Stippels:** Korla (40,5 km) en Turpan-bekken (16,4 km) zijn echte OSM-gaten: schematisch hemelsbreed, geen leidingkm. Doorgetrokken delen zijn OSM-gemeten, niet tegen een gepubliceerde deellengte te toetsen (4.000 km totaal; km-toets is indicatie).
**Toets:** `toets_knikken.py` 14 knikken >= 60 graden (krappe bochten R 160-410 m in de Gobi bij 94,1-94,9 O en 98,0 O, afkomstig uit OSM-geometrie van ways 185011116/331022098), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py`: alleen de twee bewuste stippels. json.load ok, versie 2, lonlat, modaliteit alleen leiding, alle benen >= 2 punten.
**Lessen:** een keten van uitsluitend OSM-leiding met twee korte gaten haalt de haalbaarheidstoets (4,3% stippel) en bakt zonder router of slot-zwaar werk van betekenis; de stippels zitten in de beennaam als "schematisch — OSM-gat". Eindanker Jiuquan blijft onzeker (geen station zichtbaar); Shanghai niet getekend.
