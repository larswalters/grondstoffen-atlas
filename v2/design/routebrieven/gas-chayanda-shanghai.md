# Routebrief (licht) · gas — Chayandinskoye-gasveld (Jakoetië, Rusland) → Nantong/Oost-China (China)

**stroom-id:** `gas-chayanda-shanghai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) · **status:** gebakken
**Keten in één zin:** Oost-Siberisch pijpleidinggas uit het Chajanda-veld dat via de trunkleiding **"Сила Сибири" (Power of Siberia)** dwars door Jakoetië/Amoergebied naar de Chinees-Russische grens bij Blagovesjtsjensk/Heihe loopt, de Amoer onderdoor kruist (dubbele tunnel, 2019) en als **中俄东线天然气管道 (China–Rusland Oostelijke Lijn)** verder zuidwaarts door Noordoost- en Oost-China tot in de Jangtse-delta bij Nantong loopt.
**Welke as van het verhaal:** *Rusland's oostwaartse pivot* — de eerste grote pijpleidingas die de verloren Europese afzet gedeeltelijk vervangt. **38 bcm/jaar** — ontwerpcapaciteit (61 bcm/j totaal, 38 bcm/j contractueel naar China) bereikt december 2024, in 2025 daadwerkelijk geleverd (Interfax/Hellenic Shipping News, peiljaar 2025; dit sessie niet zelf herladen — 404 op de directe hellenic-link, cijfer overgenomen uit de opdracht). Eerste volledige-leiding gas-keten zonder zee-leg.

## 1 · Ketenkaart
```
Chajanda-gasveld `gas-chayanda-veld` (Jakoetië, Rusland)
   ──(b1 leiding · "Сила Сибири"-trunk · 2.168,2 km, OSM-gemeten)──►
RU-grensstation `gas-ru-grensstation` (Amoeroever, ~20 km NW van Blagovesjtsjensk)
   ──(b2 leiding · Amoer-onderdoorgang, dubbele tunnel 2019 · ~3,2 km, stippel — geen OSM-way over de rivier)──►
CN-grensstation `gas-cn-grensstation` (Amoeroever, ~20 km NW van Heihe)
   ──(b3 leiding · 中俄东线, via Changchun–Shenyang–Qinhuangdao/Tianjin–Linyi–Lianyungang · ~1.104 km benoemd OSM-gemeten
       tegen ±5.111 km gepubliceerd hele Chinese traject)──►
Nantong-eindpunt `gas-nantong-eindpunt` (Jangtse-noordoever, China) ═══ stoppunt ═══
   (laatste ~70-75 km hemelsbreed naar het Shanghai-stadsnet: geen anker gevonden, niet getekend — zie §6/§7)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-chayanda-veld` → `gas-ru-grensstation` | "Сила Сибири" (Jakoetië → Amoergebied) | **2.168,2** [eigen pyosmium-scan, 14 ways aaneengeschakeld — zie §7 t.o.v. "±3.000 km algemeen bekend"] | OSM-pipeline (letterlijke way-keten, zie §9-bakaanwijzing) | nee |
| b2 | B | leiding | `gas-ru-grensstation` → `gas-cn-grensstation` | Amoer-onderdoorgang (dubbele tunnel, gereed 2019) | ~3,2 [eigen meting tussen de twee OSM-way-uiteinden; hemelsbreed, geen leidingkm] | rechte lijn tussen twee OSM-eindpunten | **ja — geen doorlopende OSM-way over de rivier; fysiek wel gedocumenteerd (tunnel 2019)** |
| b3 | C | leiding | `gas-cn-grensstation` → `gas-nantong-eindpunt` | 中俄东线天然气管道, via Changchun–Shenyang–Qinhuangdao/Tianjin–Linyi–Lianyungang | **~1.104** benoemd OSM-gemeten (25 ways/clusters) tegen **±5.111** [PipeChina, hele Chinese traject, opgave uit de opdracht] | OSM-pipeline (way-stitch, bake-werk — clusters, geen doorlopende naam over de hele afstand, zie §7/§9) | nee op de benoemde clusters; tussenstukken zonder naam-tag worden bij het bakken mogelijk korte stippels (Kårstø-Dornum-patroon) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-chayanda-veld` | veld / gasbehandeling | Chajanda-gasveld, centrale gasbehandelingsinstallatie (Gazprom) | 60.3545, 111.7086 | [1][8] | bron-gelegd (z15 gezien: groot industrieterrein met tientallen procesinstallaties, tankparken en fakkels midden in de taiga, exact op het Wikipedia-coördinaat — komt overeen met "one comprehensive gas treatment unit" [1]; OSM-pijpleiding begint 2,7 km hiervandaan) |
| `gas-ru-grensstation` | grensovergang / leidingstation (RU-zijde) | naamloos compressor-/afsluiterstation aan de Amoer, Amoergebied | 50.3116, 127.3921 | [3][8][9] | bron-gelegd (z15 gezien: omheind stationsterrein met gebouwen, aangesloten op een brede ontboste leidingstrook die noordwaarts de taiga in loopt — dit is het laatste OSM-way-punt van de "Сила Сибири"-keten; ligt ~20 km ten noordwesten van Blagovesjtsjensk zelf, niet op de stadscentroïde) |
| `gas-cn-grensstation` | grensovergang / leidingstation (CN-zijde) | naamloos leidingstation aan de Amoeroever tegenover Blagovesjtsjensk, Heilongjiang | 50.2926, 127.3573 | [3][8][9] | bron-gelegd (z15 gezien: klein stationsterrein direct aan de rivieroever met toegangsweg, exact op het eerste OSM-way-punt van "中俄东线天然气管道"; ligt ~20 km ten noordwesten van Heihe zelf) |
| `gas-nantong-eindpunt` | stoppunt / invoedingspunt oostelijk gasnet | laatste benoemde leidingpunt "中俄东线", Nantong-gebied (Jangtse-noordoever), Jiangsu | 31.7231, 121.0591 | [3][8] | bron-gelegd (z16 gezien: klein ommuurd leiding-/afsluiterterrein met een duidelijke ontboste strook die zuidoostwaarts de velden in loopt, richting de rivier — laatste punt van de benoemde OSM-way-cluster) |

Geen van deze vier ankers is elders in de sitelaag/andere gas-brieven al gelegd (pijpleidingstations, geen LNG-terminals) — geen hergebruik van bestaande punten mogelijk.

## 4 · Via-punten
Geen — alle drie de leidingbenen volgen de exacte OSM-pijpleidinggeometrie (`man_made=pipeline`); een leidingtracé kent geen corridorkeuze zoals een weg of spoorlijn.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Chajanda-gasveld, centrale gasbehandeling | Gazprom | putgas → droog pijpleidinggas (+ heliumscheiding, apart naar Belogorsk) | max. 25 bcm/j gasproductie (ontwerp) | [1] |
| RU/CN-grensstations + 9 compressorstations onderweg (Chajandinskaja 577 MW, Atamanskaja 128 MW, 7 overige 481 MW) | Gazprom / PipeChina | drukverhoging, geen productwijziging | totaal 1.200 MW | [4][6] |

## 6 · Stoppunt
De brief stopt bij `gas-nantong-eindpunt`, het laatste punt waar de OSM-benoemde "中俄东线"-keten eindigt (Jangtse-noordoever bij Nantong). Het feitelijke invoedingspunt van het Shanghai-stadsgasnet ligt hemelsbreed nog ~70-75 km verder (geen eigen wegkm — geen doorlopende naam-tag of gepubliceerd eindpunt gevonden deze sessie); conform de regel "geen coördinaat verzinnen" wordt dat laatste stuk **niet** als aparte stippel getekend zonder een echt eindanker. Fase D/E vervallen: geen bron noemt een specifieke Shanghainese fabriek/afnemer met naam en adres voor déze leidingtak.

## 7 · Open punten
- **Chajanda→RU-grens (b1) is 2.168,2 km OSM-gemeten** tegen "±3.000 km algemeen bekend" (Gazprom, ongemeten schatting uit de opdracht) — de gemeten waarde dekt de volledige, aaneengesloten keten van veld tot grensstation (14 ways, geen gat), dus vertrouwd als de betere waarde; het verschil kan zitten in de bredere "Power of Siberia"-definitie die ook het Chabarovsk/Vladivostok-deel meerekent (buiten deze China-export-tak).
- **b2 (Amoer-onderdoorgang) is een stippel van ~3,2 km** ondanks een fysiek gedocumenteerde dubbele tunnel (2019): geen OSM-way over/onder de rivier gevonden binnen het webbudget. Geen probleem voor de haalbaarheid — kort stuk, rest van de keten doorgetrokken.
- **Fase C (中俄东线) is grotendeels wél in OSM aanwezig maar in losse clusters** (25 ways / ~1.104 km rond Changchun, Shenyang, Qinhuangdao/Tianjin, Linyi, Lianyungang en Nantong) tegen ±5.111 km voor het hele Chinese traject — de tussenliggende stukken zonder naam-tag zijn dit sessie niet stuk voor stuk gevolgd (webbudget); bij het bakken kunnen die tussenstukken kortere stippels worden, zoals bij `gas-karsto-dornum`. Dat is acceptabel zolang de benoemde clusters (het gros van de kilometers) doorgetrokken blijven.
- **Laatste ~70-75 km Nantong → Shanghai-stadsnet niet getekend** — geen anker gevonden (zie §6).
- **Jaarvolumebron (38 bcm/j, peiljaar 2025)** komt uit de opdracht (Interfax/Hellenic Shipping News); de directe Hellenic-link gaf deze sessie een 404, dus niet zelf herladen — wel intern consistent met Wikipedia (61 bcm/j totale capaciteit, 38 bcm/j contractueel naar China, volledig gerealiseerd december 2024).

## 8 · Bronnen
[1] Wikipedia (EN) — "Chayanda field": coördinaat 60,3545/111,7086; ontwerp-gasproductie tot 25 bcm/j; helium naar Belogorsk; gas via Power of Siberia. https://en.wikipedia.org/wiki/Chayanda_field
[2] Wikipedia (EN) — "Power of Siberia": totale lengte 3.968 km bij volledige voltooiing, 9 compressorstations (1.200 MW totaal, Chajandinskaja 577 MW/Atamanskaja 128 MW/7×481 MW), Amoer-tunnels door China Petroleum Pipeline gereed maart 2019, volledig Chinese traject afgerond december 2024, 61 bcm/j totale capaciteit / 38 bcm/j contractueel naar China. https://en.wikipedia.org/wiki/Power_of_Siberia
[3] OpenStreetMap / Geofabrik — lokale extracts `rusland-verrehoosten-latest.osm.pbf` + `china-latest.osm.pbf`, eigen pyosmium-tagscan (`man_made=pipeline`, `substance=gas`): Rusland 14 ways "Сила Сибири" (2.168,2 km, aaneengeschakeld van 111,7117/60,3576 tot 127,3921/50,3116); China 25 ways/clusters "中俄东线天然气管道" + 1 aftakking 长岭-长春支线 (1.104,1 km, van 127,3573/50,2926 tot in de Nantong-cluster rond 121,06-121,18/31,72-31,93). Geen Overpass gebruikt (webbudget). https://www.openstreetmap.org/copyright
[4] Global Energy Monitor (gem.wiki) — "Power of Siberia Gas Pipeline" (uit de opdracht, dit sessie niet herladen — geen firecrawl-credits). https://www.gem.wiki/Power_of_Siberia_Gas_Pipeline
[5] Interfax — jaarvolume 38 bcm/j, peiljaar 2025 (uit de opdracht, niet herladen). https://interfax.com/newsroom/top-stories/105979/
[6] Hellenic Shipping News — jaarvolume 38 bcm/j, peiljaar 2025 (uit de opdracht; directe link gaf deze sessie 404, zie §7). https://www.hellenicshippingnews.com/russias-gazprom-supplied-38-bcm-of-gas-to-china-via-power-of-siberia-pipeline-in-2025/
[7] Wikipedia geosearch-API — bevestiging plaatsnamen nabij de Chinese eindclusters (Haimen/Nantong-omgeving, Changshu Power Station, "Soviet aircraft carrier Minsk"/Nantong). https://en.wikipedia.org/w/api.php?action=query&list=geosearch
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15-z16) — `v2/build-cache/satcheck/sat-gas-chayanda-shanghai-chayanda-veld.png`, `…-ru-grens.png`, `…-cn-grens.png`, `…-nantong-eind.png`.
[9] Lokale afstandsberekening (haversine) tussen de OSM-way-eindpunten voor b2, geen internet nodig.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Functie:** `bak_gas_chayanda_shanghai()` in `v2/tools/bak_stromen.sh` · **register:** `{ sleutel: "gas-cs", bestand: "stroomroute-gas-chayanda-shanghai.json", grondstof: "gas", aan: true }` (centraal werk).

**Totaal: 13 benen, alle modaliteit leiding, 4.619,5 km · 3.019 punten · 4 markers · bestand 64,1 KB.**

| # | been | km | punten | type |
|---|---|---|---|---|
| 1 | Сила Сибири, Chajanda-veld → RU-grensstation | 2.153,8 | 1.285 | doorgetrokken |
| 2 | Amoer-onderdoorgang (stippel) | 3,3 | 2 | stippel |
| 3 | 中俄东线, cluster CN-grens → Changchun | 571,7 | 559 | doorgetrokken |
| 4 | tussenstuk Changchun → Changchun-Shenyang | 141,7 | 2 | stippel |
| 5 | 中俄东线, cluster Changchun → Shenyang | 140,7 | 145 | doorgetrokken |
| 6 | tussenstuk Shenyang-omgeving | 85,0 | 2 | stippel |
| 7 | 中俄东线, cluster Shenyang-omgeving | 27,1 | 37 | doorgetrokken |
| 8 | tussenstuk Shenyang → Qinhuangdao/Tangshan | 317,4 | 2 | stippel |
| 9 | 中俄东线, cluster Qinhuangdao/Tangshan | 160,8 | 433 | doorgetrokken |
| 10 | tussenstuk Qinhuangdao/Tangshan → Linyi/Rizhao | 524,4 | 2 | stippel |
| 11 | 中俄东线, cluster Linyi/Rizhao | 136,8 | 461 | doorgetrokken |
| 12 | tussenstuk Linyi/Rizhao → Nantong | 331,4 | 2 | stippel |
| 13 | 中俄东线, cluster Nantong-eindpunt (eindigt op het stoppunt) | 25,4 | 87 | doorgetrokken |

Doorgetrokken totaal 3.216,2 km (69,6%) · stippel totaal 1.403,3 km (30,4%) — **niet** de Bingham-Garfield-klasse (100% stippel), de keten blijft haalbaar. Alle vier markers ≤ 0,383 km van hun lijn (RU-grens/CN-grens/Nantong exact op 0,000–0,007 km); alle naden tussen opeenvolgende benen ≤ 0,006 km (ver onder de 5 km-norm). `toets_knikken.py`: 134 knikken ≥ 60°, waarvan 1 omkering ≥ 150° en **0 terugloop** (dus niets te repareren). `toets_rechte_benen.py --min-km 5`: alleen de 5 stippelbenen komen op omwegfactor 1,000 naar boven — precies zoals het hoort, geen doorgetrokken been is verdacht recht. JSON-contract: versie 2, `punt_formaat` lonlat, modaliteit uitsluitend `leiding`, elk been ≥ 2 punten.

**b1 — bevinding t.o.v. de brief:** van de 14 kandidaat-way-id's uit de brief bleken **4 korte parallel-/spurstukken** bij compressorstations te zijn (641327232, 729366004, 1070629087, 1070643676 — elk 4-16 punten, binnen het bereik van de al-doorlopende hoofdgeometrie, geen brugfunctie). Een pyosmium-graaf op endpoint-matching (auto-detectie van oriëntatie per way) bevestigt dat de overige **10 ways een gatloze, aaneengesloten keten** vormen van het veld-anker (naad 2,7 km — binnen de norm) tot het RU-grensstation (exact, 0,000 km): **2.153,8 km**, tegen 2.168,2 km in de brief met alle 14 (−0,7%). Beide liggen ver onder de "±3.000 km algemeen bekend" (Gazprom, ongemeten) — verschil blijft een bevinding, geen via-punt-gesleep (§7 van de brief blijft geldig).

**b2 — ongewijzigd stippel:** 3,3 km, Amoer-onderdoorgang, zoals voorgeschreven.

**b3 — verbetering t.o.v. de brief (bakhandleiding §2, optie a):** vóór het stikken is een **bredere pyosmium-scan zonder naamfilter** gedraaid over de hele China-extract (bbox 118–127,5° / 31–46°N, 1.313 `man_made=pipeline`-ways, 88 met `substance=gas`). Die vond drie extra benoemde "中俄东线"-ways (1328499370, 1328499376, 1328499377) die de losse Qinhuangdao/Tangshan-cluster (1336781081) en de Qinhuangdao-Tianjin-cluster (1450157901/1415123638/1415123639) tot **één doorlopende cluster van 160,8 km** samensmeden (interne naden 0,66–1,22 km, ruim binnen de norm) — een echte meting, geen aanname. Way 1328499381 (`中俄东线天然气管道长岭-长春支线`) is expliciet een zijtak (eigen naam-tag) en **niet meegenomen**; way 1328499383 (2 punten, 2,3–2,8 km van de Changchun-cluster) is een losse afsluiter-stub zonder brugfunctie en evenmin meegenomen. De overige vijf tussenstukken (141,7 · 85,0 · 317,4 · 524,4 · 331,4 km) bleven ook na de bredere scan zonder benoemde OSM-way — verdeeld over vijf losse stippels (geen enkele rechte lijn voor de hele 5.111 km-Chinese trajectlengte), conform het `gas-karsto-dornum`-patroon. Cluster "shenyang-omgeving" en "nantong" zijn omgekeerd t.o.v. hun ruwe OSM-node-volgorde zodat de hele keten Noord → Zuid loopt; de Nantong-cluster eindigt op 0,007 km van het stoppunt-anker.

**Bestanden:** `v2/build-cache/ais/graaf/gas-chayanda-shanghai-leiding-chayanda-rugrens.geojson` + zes `gas-chayanda-shanghai-leiding-cn-*.geojson` (cn-grens-changchun, changchun-shenyang, shenyang-cluster, qinhuangdao-tangshan, linyi-rizhao, nantong). `v2/data/stroomroute-gas-chayanda-shanghai.json` (64,1 KB).

**Lessen:** (1) een brief-gelegde way-lijst is een hypothese, niet een garantie — endpoint-matching op de echte pyosmium-geometrie ontmaskerde 4 van 14 ways als niet-brug-vormende spurs zonder de meting te schaden (de 10 overige vormen zelf al een gatloze keten). (2) de "brede scan zonder naamfilter"-stap uit de bakhandleiding is geen dode letter: ze leverde hier een meetbare verbetering (twee losse clusters → één, +160,8 km doorgetrokken i.p.v. een extra stippel). (3) grote stippels (300-500 km) horen bij een trunkleiding die dwars door duizenden km ongekarteerd binnenland loopt — dat is geen bakfout, het is de eerlijke grens van OSM's dekking op dit tracé; verdelen over vijf losse benen i.p.v. één grote lijn houdt de claim "hier reikt het net niet" lokaal en controleerbaar.
