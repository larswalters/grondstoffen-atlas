# Gas · Bovanenkovo → Ukhta → Gryazovets → Moskouse gasring KGMO (Rusland)

**stroom-id:** `gas-bovanenkovo-moskou` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Pijpleidinggas van het Gazprom-veld Bovanenkovo (Yamal) over de Noordelijke Corridor (Bovanenkovo-Ukhta, onder de Baydaratskaya-baai door, daarna Ukhta-Gryazovets) en de leiding Gryazovets-KGMO naar de aansluiting op de Moskouse gasring (KGMO) in de Moskou-oblast; drie doorgetrokken OSM-leidingbenen, geen zee, geen stippel.
**Welke as van het verhaal:** Het Russische hart: Yamal-gas naar de grootste binnenlandse afzetmarkt. Bovanenkovo heeft 115 bcm/j nominale capaciteit en produceerde 99 bcm in 2020 [1][6]; dit is capaciteit/productie van het veld, GEEN gemeten stroom naar Moskou (Gazprom publiceert geen verdeling).

## 1 · Ketenkaart
```
Bovanenkovo `gas-bovanenkovo-veld` ──(b1 leiding · Bovanenkovo-Ukhta, 9 compressorstations · 1.120,2 km OSM)──►
Ukhta `gas-ukhta-knoop` ──(b2 leiding · Ukhta-Torzhok 1 tot Gryazovets · 965,4 km OSM)──►
Gryazovets `gas-gryazovets-knoop` ──(b3 leiding · Gryazovets-KGMO DN1220 · 409,8 km OSM, naad 0,25 km)──►
KGMO-ringknoop `gas-kgmo-knoop` (Moskou-oblast) ══ stoppunt (ringknoop, geen afnemer) ══
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Bovanenkovo → Ukhta | Бованенково — Ухта (lijn 1; Baydaratskaya-onderdoorgang 71 km, 4 strengen) | 1.120,2 [eigen OSM-meting, 18 ways] tegen 1.100 [1][2] / 1.200 [4] (+1,8% / −6,7%) | OSM-pipeline, FeatureCollection | nee |
| b2 | B | leiding | Ukhta → Gryazovets | Ухта — Торжок 1 (Ухта — Грязовец) | 965,4 [eigen OSM-meting, 7 ways] tegen circa 970 Ukhta-Torzhok-naamlengte [4] (−0,5%) | OSM-pipeline | nee |
| b3 | C | leiding | Gryazovets → KGMO-knoop | Грязовец — КГМО (5 ways, DN1220) | 409,8 [eigen OSM-meting] tegen 412 [ontwerp]; GEM noemt 498 [8] | OSM-pipeline | nee (naad b2→b3 0,25 km, parallelle strengen op het station) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-bovanenkovo-veld` | veld / kop leiding | Bovanenkovo-gasveld, begin OSM-lijn (Gazprom) | 70.3193, 68.2650 | [1][6][10][11] | aannemelijk (z14 gezien: bundel parallelle pijpen door de toendra met een weg; het gasbehandelingscomplex ligt ~1,3 km west; het Wikipedia-veldpunt 70.2/68.4 is een centroide en niet gebruikt) |
| `gas-ukhta-knoop` | tussenknoop (compressor/hub Ukhta) | Ukhta, einde Бованенково — Ухта | 63.6703, 53.7242 | [4][10][11] | aannemelijk (z14 gezien: groot grijs grindterrein met schakelinstallatie naast de rivier, compressorterreinen 1-2 km zuidwest; geen naam gezien) |
| `gas-gryazovets-knoop` | tussenknoop (hub Gryazovets) | Gryazovets, einde Ухта — Торжок 1 | 58.7627, 40.2219 | [5][7][10][11] | aannemelijk (z14 gezien: compressorstation ~0,6 km west, leidingstrook met meerdere strengen; geen naam gezien) |
| `gas-kgmo-knoop` | stoppunt / ringaansluiting | KGMO-knoop, Gryazovets-KGMO ontmoet КГМО 2 (ring) | 56.3201, 37.4423 | [8][10][11] | bron-gelegd (z14 gezien: leidingstrook door bos, klein station ~0,65 km noord; OSM-lijnen Грязовец — КГМО, КГМО 2 en een перемычка eindigen op dit punt, 0,01 km) |

Geen hergebruik mogelijk: geen bestaande brief legt een Russisch binnenlands gasanker (Sabetta-LNG is een ander terrein).

## 4 · Via-punten
Niet van toepassing: leiding volgt de OSM-geometrie; geen corridorkeuze door ons.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Bovanenkovo-veld | Gazprom | putgas → droog pijpleidinggas | 115 bcm/j nominaal, 99 bcm in 2020 (peiljaar 2020); GEM 59 bcm 2023 zonder primaire bron | [1][6][3] |
| Bovanenkovo-Ukhta (9 compressorstations) | Gazprom | drukverhoging | ontwerp 140 bcm/j [2]; Wikipedia 115 bcm/j | [2][1] |
| Ukhta-Torzhok 1/2/3 | Gazprom Transgaz Ukhta | transport | 45 bcm/j per lijn [haalbaarheidstoets, NS Energy]; upgrade Ukhta-Gryazovets goedgekeurd 2025 | [9] |
| Gryazovets-KGMO | Gazprom Transgaz Moskva | transport naar de ring | DN1220; GEM 90 bcm/j (projectie) | [8] |

## 6 · Stoppunt
De brief stopt bij de KGMO-ringknoop: een knoop in het Moskouse gasnet, geen gedocumenteerde afnemer; fase D/E vervallen, en er is geen bron voor de verdeling over Moskou.

## 7 · Open punten
- **Moskou-aandeel onbekend**: Gazprom publiceert geen verdeling; de lijn toont het fysieke pad, niet dat Bovanenkovo-gas hier aankomt (gas in de ring is gemengd).
- **Parallelle lijnen**: Bovanenkovo-Ukhta heeft twee lijnen, Ukhta-Torzhok drie; getekend is lijn 1 per naam; een pad tussen lijnen is bewust uitgesloten.
- **Naad b2→b3 0,25 km** bij Gryazovets: de strengen delen geen OSM-nodes; geen stippel, gewoon een naad.
- **Lengte b3**: eigen meting 409,8 km tegen 412 [ontwerp] en 498 [8]; waarschijnlijk een andere eindpuntdefinitie bij GEM.
- **Volume 2023**: 59 bcm [3] zonder primaire bron, niet gebruikt; productie sinds 2023 geclassificeerd.
- **Anker Bovanenkovo** = begin van de OSM-lijn, niet het plant-hart; het gasbehandelingscomplex ligt ~1,3 km west (onder de 2 km-regel, geen eigen anker of last-mile-been).
- GEM-pagina's [3][8][9] gaven 403: cijfers komen uit zoekresultaten en de haalbaarheidstoets, niet zelf geopend.

## 8 · Bronnen
[1] Wikipedia, "Yamal project": Bovanenkovo 4,9 tcm, 99 bcm in 2020, capaciteit 115 bcm/j, pijp Bovanenkovo-Ukhta 1.100 km. https://en.wikipedia.org/wiki/Yamal_project
[2] Offshore Technology, "Bovanenkovo-Ukhta Gas Trunkline System": 1.100 km, ontwerp 140 bcm/j, 1.420 mm, 9 compressorstations, Baydaratskaya 71 km. https://www.offshore-technology.com/projects/bovanenkovoukhta-gas-trunkline-system/
[3] Global Energy Monitor, "Bovanenkovskoye (Gazprom)": 59 bcm 2023 (uit de opdracht, niet zelf geopend). https://www.gem.wiki/Bovanenkovskoye_(Gazprom)_Oil_and_Gas_Asset_(Yamalo-Nenets_Autonomous_Okrug,_Russia)
[4] Wikipedia, "Yamal-Europe pipeline": secties Bovanenkovo-Ukhta 1.200 km en Ukhta-Torzhok 970 km. https://en.wikipedia.org/wiki/Yamal%E2%80%93Europe_pipeline
[5] Wikipedia, "Northern Lights (pipeline)": Vuktyl-Ukhta-Gryazovets-Torzhok, Gazprom-eigendom. https://en.wikipedia.org/wiki/Northern_Lights_(pipeline)
[6] Wikipedia, "Bovanenkovo gas field": ontdekt 1972, productie sinds 2012, 99 bcm in 2020 van 115 bcm; veldcoordinaat 70.2/68.4. https://en.wikipedia.org/wiki/Bovanenkovo_gas_field
[7] Wikipedia, "Gryazovets-Vyborg gas pipeline": Gryazovets als beginpunt van de noordwesttak. https://en.wikipedia.org/wiki/Gryazovets%E2%80%93Vyborg_gas_pipeline
[8] Global Energy Monitor, "Gryazovets-Ring of the Moscow Region Gas Pipeline": 498 km, 1.200 mm, 90 bcm/j (projectie), via zoekresultaat. https://www.gem.wiki/Gryazovets-Ring_of_the_Moscow_Region_Gas_Pipeline
[9] Global Energy Monitor, "Northern Lights Gas Pipeline": upgrade Ukhta-Gryazovets goedgekeurd april 2025 (uit de haalbaarheidstoets). https://www.gem.wiki/Northern_Lights_Gas_Pipeline
[10] OpenStreetMap/Geofabrik, extracts rusland-oeral, -noordwest, -centraal: man_made=pipeline, namen Бованенково — Ухта, Ухта — Торжок (Ухта — Грязовец), Грязовец — КГМО; 30 ways, totaal 2.495,6 km; tool `v2/tools/maak_leidingbeen_gas_bovanenkovo_moskou.py`. https://www.openstreetmap.org/copyright
[11] Esri World Imagery via `v2/tools/sat_check.py` (z14): `v2/build-cache/satcheck/sat-gas-bovanenkovo-moskou-{bovanenkovo,ukhta,gryazovets,kgmo}.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

**Stroom `gas-bovanenkovo-moskou`** → `v2/data/stroomroute-gas-bovanenkovo-moskou.json` · 3 benen (alle leiding, doorgetrokken), **2.495,4 km**, 3.625 punten, 4 markers, 71,2 KB. Recept: `bak_stromen.sh` (functie `bak_gas_bovanenkovo_moskou`), geometrie `v2/tools/maak_leidingbeen_gas_bovanenkovo_moskou.py` (drie FeatureCollections in `v2/build-cache/ais/graaf/`, prefix `gas-bovanenkovo-moskou-leiding-`).

**b1 leiding Bovanenkovo → Ukhta:** 18 OSM-ways, 1.120,2 km, 1.161 punten, tegen 1.100 [1][2] (+1,8%) en 1.200 [4] (-6,7%). OSM-leidinglengte, geen wegkm.
**b2 leiding Ukhta → Gryazovets:** 7 ways, 965,4 km, 1.567 punten, tegen circa 970 (-0,5%).
**b3 leiding Gryazovets → KGMO:** 5 ways, 409,8 km, 897 punten, tegen 412 ontwerp (-0,5%); GEM noemt 498 (waarschijnlijk andere eindpuntdefinitie).

**Geen stippel, geen haven-aanloop, geen zeebeen, geen via-punten, geen kopie.** Elk been is een vooraf gestikte OSM-pipeline (`--been-geojson "leiding|..."`), volledig gedekt: geen gat, dus geen schematische stippel.

**Naden:** b1 naar b2 0,000 km, b2 naar b3 0,247 km (parallelle strengen bij Gryazovets delen geen OSM-nodes); beide ver onder 5 km, geen stippel. **Markers:** veld 0,003 km, Ukhta 0,004 km, Gryazovets 0,002 km, KGMO 0,006 km van de lijn.

**Toets:** `toets_knikken.py` 80 knikken >= 60 graden (54 op b1, 26 op b2, 0 op b3), 0 omkeringen >= 150 graden, 0 terugloop; de knikken zijn krappe bochten en spikes in de OSM-pijplijnbron. `toets_rechte_benen.py --min-km 5`: geen rechte benen voor deze stroom. json geldig: versie 2, punt_formaat lonlat, modaliteit alleen `leiding`, elk been >= 2 punten.

**Open (zie §7):** Moskou-aandeel onbekend (fysiek pad, geen bewezen stroom); alleen lijn 1 per naam getekend; Bovanenkovo-anker is het begin van de OSM-lijn (plant ~1,3 km west).

**Gereedschapslessen:** (1) een tussentijdse `bash -n`/dispatch-fout op `bak_stromen.sh` tijdens de bake kwam door een gelijktijdige edit van een andere agent aan hetzelfde bestand; de bake zelf was al geslaagd en een tweede `bash -n` was schoon. (2) Meerdere OSM-pipelinelijnen met dezelfde naam delen geen nodes: de naad tussen twee gestikte benen blijft dan ~0,25 km, wat prima binnen de 5 km-norm valt.
