# Routebrief (licht) · uranium — Ulba (Oskemen, Kazachstan) → Alashankou (grens China)

**stroom-id:** `uranium-oskemen-alashankou` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Titel (bol):** Uranium · Ulba-FA (Oskemen) → Aktogay → Alashankou (grensovergang China)
**Keten in één zin:** kernsplijtstof (fabrieksvers fuel assemblies, AFA 3G, uit laag verrijkt uranium) van de fabriek Ulba-FA (JV Ulba/Kazatomprom 51% en CGNPC-URC 49%) op het Ulba-terrein in Oskemen per **spoor** (één rit, alleen spoor) via Ayagoz naar het knooppunt Aktogay, dan over de Dostyk-lijn naar de grens Dostyk–Alashankou — stoppunt.
**Welke as van het verhaal:** *Kazachs gereed splijtstof naar China.* Ulba-FA levert sinds december 2022 per spoor aan CGN-centrales; ontwerpcapaciteit **200 t U/j**, bereikt 2024/25 (WNA; Kazatomprom 6-1-2025); 20 leveringen tot aug 2026 = 1.448 assemblies, >660 t U naar zes Chinese centrales [1][2][4]. Reserve-as naast de mijnstromen (Inkai/Kharasan): hier gaat het eindproduct, niet het erts.

## 1 · Ketenkaart
```
Ulba-FA/UMP-terrein `u-ulba-fabriek` ──(b1 spoor · Oskemen → Ayagoz → Aktogay · 529,3 km gemeten, hemelsbreed 391 km, geen gepubliceerde spoorkm,
   aannemelijk: één bron — bron noemt spoor naar China, niet de route)──►
Aktogay-knooppunt `u-aktogay-knoop` ──(b2 spoor · Aktogay → Dostyk · 332,3 km · LETTERLIJKE KOPIE kharasan b7)──►
Dostyk-grens ──(b3 spoor · Dostyk → Alashankou · 17,6 km · LETTERLIJKE KOPIE kharasan b8, aannemelijk: één bron voor de grensovergang)──►
Alashankou-station `u-alashankou-station` ── stoppunt (Chinese centrales liggen ver daarna, geen route gedocumenteerd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | spoor | Ulba-fabriek → Aktogay-knooppunt | Oskemen → Ayagoz (±1 km langs de route) → Aktogay; NIET via Semey (route ligt er 104 km vandaan) | geen gepubliceerd [eigen run: 529,3 km over 266 edges; grootcirkel 391,4 km, verhouding 1,35] | toets_spoorroute (BAKE_SUFFIX=-raw), één run zonder via-punten | nee — *aannemelijk: één bron* [3][4] |
| b2 | D | spoor | Aktogay → Dostyk | Aktogay–Dostyk-lijn (Turksib-tak naar de grens) | 332,3 [kopie] | LETTERLIJKE KOPIE `spoorroute-uranium-kharasan-alashankou-aktogay-dostyk.geojson` | nee |
| b3 | D | spoor | Dostyk → Alashankou-station | grensovergang, bogiewissel 1520→1435 mm | 17,6 [kopie] | LETTERLIJKE KOPIE `spoorroute-uranium-kharasan-alashankou-dostyk-alashankou.geojson` | nee — *aannemelijk: één bron* |
Totaal ±879,2 km. Gedeeld met `uranium-kharasan-alashankou`: b2+b3 (349,9 km = 40%); b1 is nieuw.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-ulba-fabriek` | fabriek/laadplek (kop van b1, marker) | Ulba Metallurgical Plant, hier ook Ulba-FA, Oskemen | 49.9861, 82.6286 | [5][6][sat] | bron-gelegd (z15 gezien: het kruis ligt binnen een compact industrieperceel met rijen gebouwen en rangeersporen; OSM-way 260065021 draagt de naam en valt binnen 20 m samen met het punt. Het perceel is op beeld niet te scheiden van het naastgelegen Kazzinc-complex ten westen, de naam komt dus alleen van OSM) |
| `u-aktogay-knoop` | splitspunt b1/b2 (geen marker) | Aktogay, spoorknoop richting Dostyk | 46.9549, 79.9281 | [11] hergebruik kharasan | hergebruikt letterlijk uit `uranium-kharasan-alashankou` (daar een benaderd punt; ligt ±17 km oost van het station, de router keert op het knooppunt 46.971, 79.693) |
| `u-alashankou-station` | stoppunt, marker | Alashankou-spoorstation, Xinjiang | 45.1703, 82.5705 | [8][11] hergebruik kharasan | bron-gelegd (daar: z15 emplacement met rangeeryard en loodsen); kopie eindigt 335,8 m van het anker (anker ≠ routeerpunt) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | haalbaarheidstoets: één run zonder via-punten; de vrije route volgt Ayagoz en is korter (529 km) dan de ontwerp-corridor via Semey (±760 km). Geen corridorkeuze die een via-punt rechtvaardigt |
| b1/b2 | 1 | Aktogay (naad, geen via) | 46.9549, 79.9281 | begin van de kopie; het eindpunt van b1 is exact het beginpunt van kharasan b7 (naad 0 m) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ulba-FA (fabricage assemblies) | Ulba-FA LLP: UMP/Kazatomprom 51%, CGNPC-URC 49% | laag verrijkt UO2-poeder/pellets → fuel assemblies AFA 3G | 200 t U/j ontwerp, bereikt 2024/25 | [1][2][3] |

## 6 · Stoppunt
Alashankou: het is de gedeelde grensovergang van de mijnstroom, en beide bronnen noemen alleen "per spoor naar China"; de ontvangende centrales (o.a. Yangjiang, Fangchenggang, Ningde, Ling Ao, Hongyanhe, Daya Bay) liggen 3.000+ km voorbij en geen bron noemt de Chinese route. Fase E vervalt.

## 7 · Open punten
- **Route en grensovergang zijn niet bronvast**: [3][4] zeggen "per spoor naar China", niet via welke grens. Dostyk–Alashankou is de aannemelijke overgang (geen ander bronpunt); het alternatief Altynkol–Khorgos is niet getoetst.
- **Geen gepubliceerde spoorkm Oskemen–Dostyk gevonden** (één WebSearch, geen treffer); b1 heeft alleen de eigen run en de grootcirkel. De ±15%-toets is dus een indicatie, geen norm.
- **Router-omkering bij Aktogay**: de run kent een omkering (174 graden) bij 46.971, 79.693 en daarna 17 km verder oost naar het anker; dezelfde klasse als de TERUGLOOP-clusters van kharasan b6/b7. Bevinding voor §9, niet dichttrekken.
- **Twee omkeringen vlak bij Ulba** (49.996, 82.620 en 49.9925, 82.6075): raakpunt op het fabrieksemplacement, snap 0,32 km; bak-agent let op de eerste 2 km.
- Per rit de lading en het aantal containers staat in [3] (34 containers, 68 assemblies); dat is een voorbeeld, geen jaarvolume.
- **Ulba ontbreekt in de uranium-sitelaag**: centraal toevoegen (fabricage 200 t U/j, hier eenheid t U/j).
- Zelfde Oskemen-anker als keten 3 (Oskemen als herkomst); bij dubbeling het anker letterlijk delen.

## 8 · Bronnen
[1] World Nuclear Association, "Uranium and Nuclear Power in Kazakhstan" — Ulba-FA (JV, 51/49), 200 t U/j assemblies voor CGN, ontwerpcapaciteit bereikt 2024, open nov. 2021. https://world-nuclear.org/information-library/country-profiles/countries-g-n/kazakhstan
[2] Wikipedia, "Kazatomprom" — Ulba-FA sinds 2021, 200 t laag verrijkt uranium als splijtstof per jaar bereikt (Kazatomprom 6-1-2025). https://en.wikipedia.org/wiki/Kazatomprom
[3] World Nuclear News, 8-12-2022, "First fuel from Ulba-FA fuel delivered to customer" — 34 containers per spoor, door CGNPC aanvaard. https://world-nuclear-news.org/articles/first-fuel-from-ulba-fa-fuel-delivered-to-customer
[4] Ulba, 14-8-2026, "A journey of thousands of kilometers" — 20e levering, route "Ust-Kamenogorsk – PRC", zes centrales, 1.448 assemblies (>660 t U); geen grensovergang genoemd. https://ulba.kz/en/news/417/a-journey-of-thousands-of-kilometers
[5] Wikipedia, "Ulba Metallurgical Plant" en "Oskemen" — Kazatomprom 90%, IAEA LEU-bank sinds 2017; geen coördinaat. https://en.wikipedia.org/wiki/Ulba_Metallurgical_Plant
[6] OSM/Nominatim (ODbL), way 260065021 "Үлбі металлургиялық зауыты", Babkina Melnitsa, Oskemen: 49.98608, 82.62857. https://nominatim.openstreetmap.org
[7] Kitco/Kazatomprom, 7-12-2022, eerste levering splijtstof aan China (68 assemblies, 34 containers). https://www.kitco.com/news/article/2022-12-07/kazatomprom-reports-first-delivery-nuclear-fuel-kazakhstan-chinese-nuclear
[8] Wikipedia, "Dostyk" (45.2533, 82.4844) en "Alashankou" — grensstation, bogiewissel. https://en.wikipedia.org/wiki/Dostyk
[9] Wikipedia, "Ayagoz" (47.9667, 80.4333) — op de Turksib-lijn; route komt er binnen 1,0 km langs. https://en.wikipedia.org/wiki/Ayagoz
[10] Haalbaarheidstoets 2026-10-09 (eigen run `toets_spoorroute`, 529,3 km) — `v2/build-cache/ais/graaf/spoorroute-uranium-oskemen-alashankou-ulba-aktogay.geojson`.
[11] Routebrief `uranium-kharasan-alashankou.md` (gebakken 2026-09-28) — Aktogay, Dostyk en Alashankou, benen b7/b8.
[sat] Esri World Imagery via `v2/tools/sat_check.py` z15 — `v2/build-cache/satcheck/sat-uranium-oskemen-alashankou-ulba.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh uranium-oskemen-alashankou` (functie `bak_uranium_oskemen_alashankou`) → `v2/data/stroomroute-uranium-oskemen-alashankou.json` (25,0 KB, versie 2, lonlat). Drie spoorbenen, 881,5 km, 1.379 punten, 2 markers, 0 stippels, geen zee, geen haven-aanloop, geen via-punten, geen wegscan. Alle drie `--been-geojson`, doorgetrokken.

| # | modaliteit | been | km gebakken | brief | naad |
|---|---|---|---|---|---|
| b1 | spoor | Ulba-fabriek → Aktogay (via Ayagoz, niet via Semey; aannemelijk: één bron) | 531,6 | 529,3 gemeten, 391,4 hemelsbreed, geen gepubliceerde spoorkm | – |
| b2 | spoor | Aktogay → Dostyk, LETTERLIJKE KOPIE kharasan b7 | 332,3 | 332,3 | 0 m |
| b3 | spoor | Dostyk → Alashankou-station, LETTERLIJKE KOPIE kharasan b8 | 17,6 | 17,6 | 0 m |

Totaal 881,5 km (brief verwachtte ±879; het verschil zit in de bake-meting van b1: 531,6 tegen 529,3 uit de toets, andere afstandsformule). Markers: `u-ulba-fabriek` (49.9861, 82.6286; 0,33 km van de lijn, begin b1 op 49.9865, 82.6241 = router-snap) en `u-alashankou-station` (45.1703, 82.5705; 0,34 km van de lijn, anker ≠ routeerpunt). Geen markers voor Aktogay en Dostyk (naden, geen overslag).

**Toelichting:** b1 is de bestaande haalbaarheidsrun (`spoorroute-uranium-oskemen-alashankou-ulba-aktogay.geojson`, BAKE_SUFFIX=-raw, 3.260.717 spoor-edges, zonder via-punten) en is hier hergebruikt, niet opnieuw gedraaid. b2 en b3 verwijzen naar hetzelfde geojson als `uranium-kharasan-alashankou`; de beennaam vermeldt de kopie. Geen stippel: de keten loopt van fabriek tot station zonder gat; "aannemelijk: één bron" staat in de beennaam van b1/b3, niet in de lijnstijl.

**Toets:** geen naad > 0 m tussen de benen; b1 heeft geen gepubliceerde spoorkm, dus 531,6 tegen hemelsbreed 391,4 (factor 1,36) is indicatie, geen norm; b2/b3 identiek aan de kopie. `toets_rechte_benen --min-km 5`: geen enkel been van deze stroom gemeld. `toets_knikken`: 7 omkeringen ≥ 150 gr, 3 gemarkeerd als TERUGLOOP (b1 bij 49.9925, 82.6075 op het Ulba-emplacement; b2 bij 46.9635, 79.6897 vlak bij Aktogay; b3 bij 45.2682, 82.4693 vlak bij Dostyk). De Aktogay-omkering (174 gr, 46.9713, 79.6932) en de twee Ulba-omkeringen zijn router-gedrag op knooppunten en emplacementen en zijn niet dichtgetrokken; b2/b3 zijn een kopie en worden hier niet aangepast.

**Lessen:** (1) een stroom die uit vooraf gebakken spoorbenen bestaat kost in de bake slechts ±17 s: de haalbaarheidsrun uit de brief is direct het been. (2) De omkering bij Aktogay zit zowel aan het eind van b1 als aan het begin van b2: het gedeelde knooppunt Aktogay ligt ±17 km ten oosten van het station en is een benaderd punt (kharasan §4). (3) De oorspronkelijke ontwerp-corridor via Semey (±760 km) is door de router verworpen ten gunste van Ayagoz (529 km): de brief had hem terecht niet als via-punt vastgelegd.
