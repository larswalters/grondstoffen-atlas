# Routebrief (licht) · gas — Rockies-gas via Opal Hub (Wyoming) → Ruby Pipeline → Malin (Oregon)

**stroom-id:** `gas-opal-malin` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) ·
**status:** gebakken
**Keten in één zin:** Rockies-gas (Opal-plant, Lincoln County WY) gaat via de Ruby Pipeline (42 inch, Tallgrass sinds 2023) over Noord-Utah, Noord-Nevada en Zuid-Oregon naar het Malin-knooppunt (Klamath County OR), waar GTN en PG&E aansluiten; getekend: 52,7 km stippel (OSM-gat) plus 1.025,7 km OSM-leiding.
**Welke as van het verhaal:** *Rockies-gas naar de Pacifische kust*, een pijp die na faillissement (2022) half leeg loopt. Volume: capaciteit 1,5 bcf/d ≈ 15,5 bcm/j (eigen omrekening) [1][5]; bezetting ca. 50% (2026, Wikipedia, geen primaire bron) ≈ 7-8 bcm/j indicatief; peiljaar 2014: ca. 1,0 bcf/d ≈ 10 bcm/j (afgeleid: 0,08 bcf/d = 8% van de Ruby-flow) [2]. Geen gemeten jaarcijfer gevonden.

## 1 · Ketenkaart
```
Opal-plant `gas-opal-plant` 41.7772,-110.3440 (Lincoln County WY; verwerkingscomplex 1,7 km WNW van het dorp Opal)
  ··(b1 leiding · STIPPEL 52,7 km hemelsbreed · Ruby-begin niet in OSM)··►
OSM-begin Ruby `gas-ruby-begin` 41.5727,-110.9166 (Uinta County WY; rand van een gasfaciliteit)
  ──(b2 leiding · Ruby Pipeline 42" · OSM name=Ruby Pipeline, 31 ways · 1.025,7 km, doorgetrokken)──►
Malin `gas-malin-einde` 41.9969,-121.3566 (Klamath County OR; Ruby-einde, meterstation) — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | leiding | `gas-opal-plant` → `gas-ruby-begin` | Ruby Pipeline, oostelijk beginstuk (Opal → eerste gekarteerde punt) | hemelsbreed 52,7 km, geen leidingkm | 1 × `--stippel` | ja: leiding niet in OSM (reden: kartering ontbreekt) |
| b2 | C | leiding | `gas-ruby-begin` → `gas-malin-einde` | Ruby Pipeline, 42" (Utah Box Elder, Nevada Humboldt/Elko, Oregon Klamath) | **1.025,7 OSM**; gepubliceerd 683 mijl = 1.099 km [1][5] = −6,7%; b1+b2 = 1.078,4 km = −1,9% | vooraf gestikt geojson (`maak_leidingbeen_gas_opal_malin.py`, FeatureCollection, 4.785 punten) | nee |

OSM-ways b2 (OSM-API, oost → west; allemaal underground, name=Ruby Pipeline, substance gas; 42 in waar getagd): 371667159 · 371848659 · 371848655 · 371848653 · 371848658 · 371848657 · 371848656 · 371667163 · 371667165 · 371667169 · 371667167 · 371667166 · 371667170 · 371667171 · 371667173 · 371667175 · 371667176 · 371668066 · 371668067 · 371668068 · 371668069 · 371668070 · 371668071 · 371668072 · 371668073 · 371845634 · 948043134 · 946203791 · 946177658 · 946170581 · 209036621 (176 km, eindigt bij Malin). Naden 0-73 m, geen naad > 5 km.
**Weglaten:** de ca. 80 stationsstukjes (overground/indoor, 0,01-0,07 km, bij de compressorstations 41.4466,-118.2751 · 41.1252,-117.1094 · 41.2435,-115.7955 · 41.4182,-114.5107 · 41.7614,-113.1086 en bij Malin) en way 382912693 (1,1 km, zijtak zonder substance, 41.5075,-111.1751). Selecteren op de 31 ids, niet op naam alleen.
Niet gebruikt: naamloze overground-way 207894029 (33,5 km, naast het ontbrekende stuk): koppeling aan Ruby onbevestigd, dus geen deel van b1.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-opal-plant` | begin: gasverwerking en hub | Williams Opal-plant, Lincoln County WY | 41.7772, -110.3440 | [2][3][6] | aannemelijk (z16 gezien: omheind verwerkingscomplex met procestorens, tanks en gebouwen op een vlakte, 1,7 km WNW van het dorp Opal (OSM-plaatsnode 41.7691,-110.3260); geen bron geeft een coördinaat van de plant, de plaatsing volgt uit "Lincoln County, ca. 15 mijl oostelijk van Kemmerer" [3]) |
| `gas-ruby-begin` | begin gekarteerde leiding (geen site) | OSM-leidingbegin Ruby, Uinta County WY | 41.5727, -110.9166 | [4][6] | aannemelijk (z15 gezien: de lijn begint aan de westrand van een omheind gascomplex met leidingbundel en vijvers; wat voor installatie is niet bevestigd) |
| `gas-malin-einde` | eind Ruby, aansluiting GTN/PG&E (stoppunt) | Malin-meterstation, Klamath County OR | 41.9969, -121.3566 | [4][6][7] | bron-gelegd (z15 gezien: klein omheind erf met witte opslag/gebouwtjes op akkerland naast een landweg, ca. 140 m WNW van het OSM-leidingeinde; OSM kartert er de stationsstukjes) |

## 4 · Via-punten
Niet van toepassing: leidingbenen (OSM-way of stippel), geen corridorkeuze. Geen zee, geen haven-aanloop.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Opal-plant / Opal Hub | Williams | Greater Green River Basin e.a. → Kern River (ca. 50%), Ruby (ca. 40%) in 2014 | 1,5 bcf/d verwerking (5 units), 1,0 bcf/d in gebruik (2014) | [2][3] |
| Ruby Pipeline | Tallgrass (sinds jan. 2023; daarvoor Kinder Morgan/Pembina, Chapter 11 op 31 mrt./1 apr. 2022, verkoop 282,5 mln dollar) | Opal → Malin | 1,5 bcf/d ≈ 15,5 bcm/j; 42"; 683 mijl | [1][5] |

## 6 · Stoppunt
De brief stopt in Malin: Ruby levert er af aan GTN (corridor naar Noord-Californië/Oregon) en PG&E, en daarna is het gas vermengd met ander gas. Geen bron legt dit gas aan een afnemer; fase D en E vervallen.

## 7 · Open punten
- **Eerste 52,7 km (Opal → OSM-begin) niet gekarteerd:** stippel hemelsbreed, geen leidingkm; de werkelijke leiding verlaat Opal niet noodzakelijk in rechte lijn. Dat de Ruby daar loopt volgt uit [1] (Opal → Malin), niet uit OSM.
- **Opal-coördinaat is een satellietkeuze:** de plaatsing tegen "ca. 15 mijl oostelijk van Kemmerer" [3] is grof; twee kleinere installaties (41.782,-110.334 en 41.793,-110.327) zijn niet gebruikt. Of Ruby fysiek op deze plant aansluit of op een naburig knooppunt is niet bevestigd.
- **Bezetting 50% (2026)** staat alleen op Wikipedia [1] zonder primaire bron; geen EIA- of Tallgrass-jaarcijfer gevonden. Het Stratos-datacenter (Box Elder, 2026) is een aankondiging.
- **Faillissementsdatum:** [1] zegt 1 april 2022, RBN [5] zegt 31 maart 2022; verkoop 282,5 mln dollar [5], GEM noemt 290 mln.
- Het OSM-einde ligt ca. 140 m van het gezien erf: de aansluiting GTN/PG&E is niet apart gelegd.

## 8 · Bronnen
[1] Wikipedia, "Ruby Pipeline" — 683 mijl (1.099 km), Opal WY → Malin OR, 1,5 bcf/d, in bedrijf 2011, Chapter 11 2022, ca. 50% bezetting 2026. https://en.wikipedia.org/wiki/Ruby_Pipeline
[2] EIA, Today in Energy, explosie Opal-plant april 2014 — 1,5 bcf/d capaciteit (5 units), 1,0 bcf/d in gebruik, Ruby ca. 40% en Kern River ca. 50% van het Opal-gas, Ruby-flow −0,08 bcf/d (8%). https://www.eia.gov/Todayinenergy/detail.php?id=16091
[3] WyoHistory, "The Opal Hub" — hub en Williams-plant in Lincoln County, ca. 15 mijl oostelijk van Kemmerer, verwerkt gas uit Greater Green River Basin e.a. https://www.wyohistory.org/field-trips/opal-hub
[4] OpenStreetMap (ODbL), 31 ways name=Ruby Pipeline (man_made=pipeline, substance gas), OSM-API 2026-11-01 en Geofabrik-extracts us-wyoming/utah/nevada/oregon/california; way 371667159 (begin) en 209036621 (einde). https://www.openstreetmap.org/way/209036621
[5] RBN Energy, "Ruby, Ruby, Will You Be Mine? Tallgrass Bid Breathes New Purpose into Languishing Ruby Pipeline" — 680-683 mijl, 42", 1,5 bcf/d, Chapter 11 31 mrt. 2022, bod 282,5 mln dollar. https://rbnenergy.com/daily-posts/blog/tallgrass-bid-breathes-new-purpose-languishing-ruby-pipeline ; S&P Global 2022-12: https://www.spglobal.com/market-intelligence/en/news-insights/articles/2022/12/tallgrass-buys-ruby-pipeline-in-bankruptcy-auction-73549118
[6] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-opal-malin-opal.png`, `-opal-z16.png`, `-eerste-ruby.png`, `-malin.png`.
[7] Nominatim (OSM), reverse 2026-11-01: 41.7772,-110.3440 = Lincoln County WY; 41.5727,-110.9166 = Uinta County WY; 41.9969,-121.3566 = Klamath County OR. https://nominatim.openstreetmap.org

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)

**Stroom `gas-opal-malin`** → `v2/data/stroomroute-gas-opal-malin.json` — 2 benen, 1.078,9 km, 3 markers, 102,7 KB. Titel: Gas · Opal Hub (WY) → Ruby Pipeline → Malin (OR, VS).
- b1 leiding STIPPEL 52,7 km (Opal-plant 41.7772,-110.3440 → 41.5727,-110.9166): rechte lijn, Ruby-begin niet in OSM; hemelsbreed, geen leidingkm.
- b2 leiding doorgetrokken 1.026,2 km, 4.785 punten (31 OSM-ways, vooraf gestikt door `maak_leidingbeen_gas_opal_malin.py` naar `v2/build-cache/ais/graaf/gas-opal-malin-leiding-ruby.geojson`) tegen gepubliceerd 1.099 km (-6,6%); b1+b2 = 1.078,9 km (-1,8%). Binnen de ±15%-norm (de gepubliceerde lengte is een echte leidinglengte).
- Naad b1/b2 2,8 m, geen naad > 5 km. Markers: Opal-plant (aannemelijk), Ruby OSM-begin (aannemelijk), Malin-meterstation (bron-gelegd, 4 m van de lijn).
**Recept:** `bash v2/tools/bak_stromen.sh gas-opal-malin` (functie `bak_gas_opal_malin`): `--stippel leiding` + `--been-geojson leiding`; geen zee, weg, lucht, haven-aanloop, via-punten, geen profiel in `maak_stroombeen_weg.py`.
**Toets:** `toets_knikken.py` 31 knikken >= 60 graden, 0 omkeringen, 0 teruglopen: spikes en bochten zitten in de OSM-geometrie van Ruby (stationsomleidingen, 23-624 m radius), niet bijgewerkt (OSM is de bron). `toets_rechte_benen.py`: alleen de stippel b1 is een lang recht stuk (reden: niet gekarteerd).
**Lessen:** een OSM-leiding die in de lijst als FeatureCollection klaarstaat bakt zonder tweede poging; selecteren op way-id (niet op naam) hield stationsstukjes en zijtak buiten de lijn. Eindpunt = id (Malin).
