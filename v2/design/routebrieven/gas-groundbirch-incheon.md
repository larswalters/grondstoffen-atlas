# Routebrief (licht) · gas — Groundbirch (Montney, Canada) → Tongyeong (KOGAS, Zuid-Korea) via Coastal GasLink en LNG Canada

**stroom-id:** `gas-groundbirch-incheon` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken (2026-10-09)
**⚠️ Het id belooft Incheon, het eindpunt is Tongyeong.** De eerste LNG Canada-lading (GasLog Glasgow, vertrek
30-06-2025) werd eerst als Incheon-bound gemeld [5], maar kwam volgens scheepsdata aan in Tongyeong [4]; de
haalbaarheidstoets (bindend) legt het eindpunt daarom bij de KOGAS-terminal Tongyeong. Id en bestand blijven
staan (opdracht); de Incheon-aanloop van `gas-corpuschristi-incheon` (b3) vervalt als kopie, want verkeerde terminal.
**Keten in één zin:** Montney-gas gaat via de Coastal GasLink-pijpleiding (670 km, TC Energy, over Rockies en
Coast Mountains) van Groundbirch naar de LNG Canada-fabriek bij Kitimat, wordt daar vloeibaar, laadt aan de pier
in de Douglas Channel en vaart per **LNG-tanker** over de Noord-Pacific (Aleoeten, Tsugaru, Straat van Korea)
naar de KOGAS-regasterminal Tongyeong. **Aannemelijk:** één bron voor de ontvanger (scheepsdata, 1e lading).
**Welke as van het verhaal:** *Canada → Azië zonder Panama: Montney-gas als eerste LNG-export van de Canadese
westkust.* LNG Canada 14 Mtpa (2 treinen; trein 2 sinds nov 2025; Wikipedia, peil 2026) ≈ 19,0 bcm/j; Coastal
GasLink 2,1 bcf/d ≈ 21,7 bcm/j initiële capaciteit [1][2]. Het Tongyeong-aandeel is niet gebrond.

## 1 · Ketenkaart
```
Groundbirch (CGL-kop, NGTL-aansluiting) `gas-groundbirch-kop`   (fase A Montney-velden vervalt: diffuus)
   ──(b1 leiding · Coastal GasLink, OSM-way, omgekeerd · 662 km)──► LNG Canada-plant `gas-lngcanada-plant`
   ──(b2 leiding, stippel · plant → pier, pijprek op eigen terrein · 3,6 km)──► LNG Canada-kade `gas-lngcanada-kade`
   ──(b3 zee, haven-aanloop, stippel · Douglas Channel → zeeknoop 7837 · 197,6 km)──► zeeknoop 7837 (Hecate)
   ──(b4 zee · Principe Channel, Noord-Pacific, Tsugaru, Straat van Korea · 8.468 km, MARNET)──► zeeknoop 5620
   ──(b5 zee, haven-aanloop, stippel · Tongyeong · 12,4 km)──► Tongyeong LNG-terminal `gas-tongyeong-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-groundbirch-kop` → `gas-lngcanada-plant` | Coastal GasLink Pipeline (OSM-way 1062392714, wikidata Q85753148, `man_made=pipeline`, `substance=gas`, ondergronds) | 662,4 gemeten (OSM-API, 1.017 punten) tegen 670 gepubliceerd [2] = −1,1% | OSM-pijpleiding: geojson klaar (§9-voorbereiding), way loopt in OSM Kitimat → Groundbirch en is **omgekeerd** | nee |
| b2 | B | leiding | `gas-lngcanada-plant` → `gas-lngcanada-kade` | pijprek/trestle plant → pier op eigen terrein (op z14 zichtbaar) | 3,6 hemelsbreed, geen bron | `--stippel "leiding|…"` | ja — eigen terrein, geen OSM-way (naad < 5 km, maar de LNG-leiding is niet gekarteerd) |
| b3 | B | zee | `gas-lngcanada-kade` → zeeknoop 7837 (54.1683, -130.3373) | haven-aanloop Douglas Channel → Wright Sound → Principe Channel → Browning Entrance | 197,6 gemeten (180 punten, 0,00 km over land, omwegfactor 1,80); kade 109,6 hemelsbreed van de zeeknoop (> 5 km én > 25 km max-snap) | `maak_havenaanloop.py` (geojson klaar, 4m47 onder timeout 900) | ja — MARNET reikt niet in de fjord |
| b4 | B | zee | zeeknoop 7837 → zeeknoop 5620 (35.0317, 128.5297) | Principe Channel → Noord-Pacific (Aleoeten) → Tsugaru → Straat van Korea; geen Panama, Hormuz, Malakka | 8.468,0 gemeten (MARNET, 63 edges, 880 punten, 2026-10-09); geen gepubliceerde lengte (ontwerp: eigen schatting ~8.000–8.600) | MARNET | nee |
| b5 | B | zee | zeeknoop 5620 → `gas-tongyeong-kade` | haven-aanloop, Tongyeong-baai | 12,4 gemeten (hemelsbreed 12,3; > 5 km) | `maak_havenaanloop.py` (geojson klaar) | ja |

Fase A (Montney-velden → Groundbirch) **vervalt**: diffuus veld- en verzamelnet (Montney), geen enkelvoudig anker.
Fase C (Tongyeong-regas → KOGAS-net) wordt niet getekend: de terminal is het punt waar LNG weer pijpleidinggas wordt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-groundbirch-kop` | kop leiding (NGTL-aansluiting) | Coastal GasLink-begin, Groundbirch, Peace River Regional District BC | 55.7963, -120.8956 | [2][3][8] | bron-gelegd (z15 gezien: groot geëgaliseerd stationsterrein met compressorgebouwen en uitgaande leidingstroken in bos/akkerland; OSM-uiteinde ligt op de zuidwesthoek. De naam "Groundbirch" komt uit het ketenontwerp, niet uit [2]) |
| `gas-lngcanada-plant` | overslag leiding → fabriek (plant-aansluiting) | LNG Canada-liquefactieplant, Kitimat | 54.0276, -128.6818 | [1][3][8] | bron-gelegd (z15 gezien: omheind LNG-complex met trains, opslagtanks en pijprek aan de Kitimat-rivier; het OSM-leidinguiteinde ligt aan de noordrand van het hek) |
| `gas-lngcanada-kade` | overslag fabriek → tanker (laadkade, routeerpunt in de Douglas Channel) | LNG Canada marine terminal, Kitimat | 53.9950, -128.6830 | [1][8] | bron-gelegd (z14/z16 gezien: pier met pijprek en laadplatform bij 53.9980, -128.6835; kadepunt ligt in open water 0,3 km zuidelijker in het bekken, ook gebruikt als start van de aanloop; beeld lijkt ouder dan de afwerking van de berth) |
| `gas-tongyeong-kade` | overslag zee → leiding (regas, LNG-jetty) | KOGAS Tongyeong LNG-terminal (한국가스공사 통영 LNG기지) | 34.9495, 128.4395 | [4][6][7][8] | bron-gelegd (z15 gezien: ~12 bolvormige LNG-opslagtanks aan de kust, lange trestle naar een jetty-kop met laadplatform; OSM-terrein way 942737946 centroïde 34.9472, 128.4205 [7]) |

## 4 · Via-punten
Niet van toepassing: b1 volgt één OSM-way, b4 wordt door MARNET gerouteerd, b2/b3/b5 zijn stippels.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LNG Canada, Kitimat | Shell 40%, Petronas 25%, PetroChina 15%, Mitsubishi 15%, KOGAS 5% | pijpleidinggas (Coastal GasLink) → LNG | 14 Mtpa (2 treinen) ≈ 19,0 bcm/j; 1e lading 30-06-2025, trein 2 nov 2025, 50 ladingen op 23-02-2026 | [1] |
| Coastal GasLink | TC Energy (65% AIMCo/KKR sinds 2020) | Montney-gas (NGTL) → plant | 2,1 bcf/d ≈ 21,7 bcm/j, uitbreidbaar naar ~5 bcf/d | [2] |
| Tongyeong LNG-terminal | KOGAS | LNG → pijpleidinggas | niet gebrond | [4][6][7] |

## 6 · Stoppunt
De brief stopt bij de KOGAS-terminal Tongyeong: daar wordt de lading pijpleidinggas voor het Koreaanse net en geen bron volgt hem verder (D/E vervallen).

## 7 · Open punten
- **De bestemming is het zwakke punt (aannemelijk, één bron).** Energy Intelligence meldde 01-07-2025 "Incheon" [5]; LNG Prime ziet GasLog Glasgow op 18-07-2025 in Tongyeong "according to shipping data" [4]. Geen bron noemt de koper; KOGAS is 5%-aandeelhouder, geen bewezen afnemer. Dat Tongyeong KOGAS-terminal is staat in [6][7]. Mitsubishi, Toho Gas en Tokyo Gas hebben contracten: Japan is de hoofdbestemming van LNG Canada; dit is de Koreaanse lane.
- **Geen Tongyeong-volume** (aandeel van de 14 Mtpa naar Zuid-Korea onbekend); capaciteit is plantniveau.
- **Kade-routeerpunt ligt in water, laadplatform 0,3 km noordelijker (53.9980, -128.6835)** — niet gezien welke berth; z16-beeld ouder dan de afwerking. Plant → kade is een stippel (pijprek niet in OSM).
- **Groundbirch-naam niet in [2]**; het OSM-uiteinde ligt wel op een groot compressor-/meetstation.
- **Montney-velden (fase A) niet getekend.**
- **Overlap:** het zeebeen b4 ligt volgens de toets voor ~89% binnen 10 km van `gas-corpuschristi-incheon` (zelfde Noord-Pacifische lane); nieuw zijn CGL (662 km), de Douglas/Principe Channel-aanloop (197,6 km), de bron en de Tongyeong-ontvanger. Geen letterlijke kopie, de lijnen vallen vanzelf samen.
- **Geen gepubliceerde kilometers voor b3/b4/b5**: de ±15%-toets geldt alleen b1 (−1,1%).

## 8 · Bronnen
[1] Wikipedia, "LNG Canada" (peil 2026-10-09; aandeelhouders, 14 Mtpa, trein 2 nov 2025, 50 ladingen 23-02-2026). https://en.wikipedia.org/wiki/LNG_Canada
[2] Wikipedia, "Coastal GasLink pipeline" (670 km, 2,1 bcf/d, TC Energy, in dienst nov 2024). https://en.wikipedia.org/wiki/Coastal_GasLink_pipeline
[3] OpenStreetMap-bijdragers (ODbL) — way 1062392714 (v7, 2026-02-08), `name=Coastal GasLink Pipline`, `wikidata=Q85753148`; 1.017 punten, 662,4 km; via OSM-API 2026-10-09. https://www.openstreetmap.org/way/1062392714
[4] LNG Prime, 18-07-2025, "South Korea gets first LNG Canada cargo" (GasLog Glasgow "arrived in Tongyeong"; rest achter betaalmuur). https://lngprime.com/asia/south-korea-gets-first-lng-canada-cargo/157381
[5] Energy Intelligence, 01-07-2025, "First LNG Canada Cargo Begins Journey to South Korea" (naar Incheon-terminal). https://www.energyintel.com/00000197-c775-d376-a1df-cff514910000
[6] Wikipedia, "List of LNG terminals" (Tongyeong, KOGAS; "citation needed"). https://en.wikipedia.org/wiki/List_of_LNG_terminals
[7] OSM/Photon (ODbL) — industrial "한국가스공사 통영 LNG기지", way 942737946, centroïde 34.9472, 128.4205. https://photon.komoot.io
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live, 2026-10-09): `v2/build-cache/satcheck/sat-gas-groundbirch-incheon-{groundbirch,plant,kade,kade-z14,kade-z16,tongyeong-kade,tongyeong-overzicht}.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Recept:** `bash v2/tools/bak_stromen.sh gas-groundbirch-incheon` (functie `bak_gas_groundbirch_incheon`, 13 s) → `v2/data/stroomroute-gas-groundbirch-incheon.json` (43,9 KB, versie 2, `lonlat`, 5 benen, 2.088 punten, 4 markers). Titel: "Gas · Groundbirch → Tongyeong" (het id zegt Incheon, het eindpunt is Tongyeong; id blijft staan). Geen profiel in `maak_stroombeen_weg.py`, geen extract, geen via-punt, geen luchtbeen, geen letterlijke kopie. De drie tussenbestanden `v2/build-cache/ais/graaf/gas-groundbirch-incheon-{leiding-cgl,aanloop-kitimat,aanloop-tongyeong}.geojson` waren al klaar en zijn niet opnieuw gedraaid.

| # | modaliteit | km | naad | doorgetrokken/stippel | been |
|---|---|---|---|---|---|
| 1 | leiding | 662,4 | 0,00 | doorgetrokken | Coastal GasLink (OSM-way 1062392714, omgekeerd) Groundbirch → Kitimat; 1.017 punten |
| 2 | leiding | 3,6 | 0,00 | stippel | LNG-overslagleiding plant → pier (eigen terrein, geen OSM-way) |
| 3 | zee | 197,6 | 0,00 | stippel | haven-aanloop Kitimat/Douglas Channel → zeeknoop 7837; 180 punten |
| 4 | zee | 8.468,0 | 0,00 | doorgetrokken | LNG-tanker zeeknoop 7837 → 5620 (MARNET, 63 edges, 880 punten, snap 0,000 km); "aannemelijk: één bron" in de beennaam |
| 5 | zee | 12,4 | 0,00 | stippel | haven-aanloop Tongyeong zeeknoop 5620 → kade; 9 punten |

Totaal **9.344,0 km** (brief verwachtte ca. 9.346). Markers: Groundbirch (Coastal GasLink-kop) 0,004 km van de lijn · LNG Canada-plant 0,000 · LNG Canada-kade 0,000 · Tongyeong LNG-terminal (KOGAS, aannemelijk) 0,000.

**Toets (§5):** alleen b1 heeft een gepubliceerde km: 662,4 tegen 670 = −1,1% (binnen ±15%). b4 heeft geen gepubliceerde km (8.468,0 gemeten; ontwerpschatting 8.000–8.600). Alle naden 0,00 km (geen naad > 5 km). `toets_knikken.py`: 0 omkeringen, 0 terugloop; de 51 krappe bochten ≥ 60° zitten in het CGL-tracé (OSM-geometrie door bergterrein) en in MARNET-passen (Aleoeten, Tsugaru, Straat van Korea). `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom (de enige rechte benen zijn b2 van 3,6 km en de aanloop-stippels, allemaal met reden). `json.load` slaagt, versie 2, modaliteiten ⊂ {zee, leiding}, elk been ≥ 2 punten.

**Toelichting per stippel/aanloop:**
- **b2 (3,6 km stippel):** het LNG-pijprek plant → pier is niet in OSM gekarteerd; rechte lijn tussen plant (54.0276, −128.6818) en kadepunt (53.9950, −128.6830).
- **b3 (haven-aanloop Kitimat):** de kade ligt 109,6 km hemelsbreed van zeeknoop 7837 (MARNET reikt niet in de fjord); `maak_havenaanloop.py` vond een pad over water van 197,6 km, 0,00 km over land (rechte lijn zou 94,7 km over land gaan). Kadepunt ligt in open water, 0,3 km zuidelijker dan het laadplatform (53.9980, −128.6835).
- **b5 (haven-aanloop Tongyeong):** kade 12,3 km van zeeknoop 5620; aanloop 12,4 km, 9 punten, 0,43 km over land (1:10M-kustgrofheid; de rechte lijn zou 0,98 km over land gaan). ⚠️ Het geojson `-aanloop-tongyeong.geojson` loopt kade → knoop; voor de reisrichting is het omgedraaid opgeslagen als `-aanloop-tongyeong-aankomst.geojson`, dat de functie gebruikt.
- **b1 (leiding):** doorgetrokken omdat OSM de leiding heeft (`man_made=pipeline`, `substance=gas`, ondergronds, wikidata Q85753148); way loopt in OSM Kitimat → Groundbirch en is omgekeerd.
- Geen vlucht, geen weg, geen spoor; geen "aannemelijk"-stippel: de onzekerheid over de bestemming (Tongyeong, één bron) zit in de beennaam van b4 en de markernaam.

**Lessen:** (1) Een voorbereid aanloop-geojson kan tegen de reisrichting in staan (`maak_havenaanloop.py` loopt `--van` kade → `--naar` knoop); bij de aankomstkant omdraaien vóór `--stippel-geojson`, anders is de naad met het zeebeen bij de bake meetbaar fout. (2) Een OSM-leiding die één way is (CGL 1.017 punten) kan via de OSM-API worden opgehaald zonder Canada-extract. (3) Overlap van b4 met `gas-corpuschristi-incheon` (~89% binnen 10 km) is een vanzelf-samenvallende lane en geen kopie. (4) Gloedlaag centraal: LNG Canada (14 Mtpa, 54.0276, −128.6818) en Tongyeong (34.9495, 128.4395; capaciteit niet gebrond) ontbreken in `v2/design/gas-sitelaag.json`.
