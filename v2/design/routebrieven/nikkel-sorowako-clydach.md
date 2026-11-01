# Routebrief (licht) · nikkel — Sorowako (Indonesië) → Balantang → Cardiff → Clydach (Wales)

**stroom-id:** `nikkel-sorowako-clydach` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) ·
**status:** gebakken
**Keten in één zin:** nikkel-matte van PT Vale Indonesia (Sorowako, Zuid-Sulawesi) gaat per **eigen mijnweg** naar de
Balantang-kade bij Malili, per **zeeschip** via de Soenda-straat, de Indische Oceaan, Bab-el-Mandeb, Suez, Gibraltar en
Biskaje naar **Cardiff** en per **truck** (A4232, M4, A4067, B4291) naar de Vale Clydach Nickel Refinery (Swansea Valley).
Stoppunt bij de raffinaderij. **Aannemelijk: één bron voor de directe lus** (zie §7).
**Welke as van het verhaal:** de Vale-eigen lus tussen twee verwerkers: Indonesische matte als feed voor de enige Britse
nikkelraffinaderij. Herkomst: in 4Q09 werd (tijdelijk, na de stakingen in Canada) een deel van de Sorowako-feed die naar
Matsuzaka ging naar Clydach verlegd [1]; Vale Base Metals zegt nu dat Clydach nikkeloxide uit Canada en Indonesië verwerkt [2].
Volume: Sorowako 70.728 t nikkel in matte (2023) als bovengrens [5], aandeel naar Clydach niet gepubliceerd; Clydach
31,3 kt Ni (2023) [4] — eenheid kt Ni per jaar.

## 1 · Ketenkaart
```
Sorowako-plant `ni-sorowako-plant` ──(b1 truck · Jalan Poros Malili-Soroako · ~60 km, indicatief)──► Balantang-kade `ni-balantang-kade`
   ──(b2 zee · haven-aanloop, stippel · 90,4 km gemeten pad, kade 87 km van de knoop)──► MARNET-zeeknoop 6080
   ──(b3 zee · MARNET · Soenda-straat → Indische Oceaan → Bab-el-Mandeb → Suez → Gibraltar → Biskaje · 17.483 km)──►
   MARNET-zeeknoop 4161 (Cardiff Bay) ──(naad 1,3 km, geen aanloop)──► Cardiff-kade `ni-cardiff-kade`
   ──(b4 truck, last mile stippel 0,3 km + A4232 → M4 → A4067 → B4291 · 74 km)──► Clydach-raffinaderij `ni-clydach-refinery` ⏹
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-sorowako-plant` → `ni-balantang-kade` | Jalan Poros Malili-Soroako (OSM-way 549291588); KOPIE van `nikkel-sorowako-matsuzaka` b1 | hemelsbreed 34 km, geen wegkm; gebakken kopie 60,5 [6] | letterlijke kopie `nikkel-sorowako-matsuzaka-weg-sorowako-balantang.geojson` | nee |
| b2 | B | zee | `ni-balantang-kade` → zeeknoop 6080 | haven-aanloop; kade 86,95 km van de knoop; KOPIE van `nikkel-sorowako-matsuzaka` b2 | 90,4 (gemeten pad) [6] | letterlijke kopie `nikkel-sorowako-matsuzaka-aanloop-balantang.geojson` | ja — net reikt niet |
| b3 | B | zee | zeeknoop 6080 → zeeknoop 4161 | Java-zee, Soenda-straat, Indische Oceaan, Rode Zee, Suez, Gibraltar, Biskaje, Bristolkanaal (geen Malakka) | 17.482,9 (MARNET-test, 107 edges, geen gepubliceerde waarde) [9] | MARNET (`--been` zee, knoop → knoop) | nee |
| b4a | C | truck | `ni-cardiff-kade` → eerste wegvertex | last mile; dock-interne wegen los van het net; KOPIE van `nikkel-matsusaka-clydach` b3 | 0,3 | `--stippel` 51.4595,-3.1551 → 51.460161,-3.158666 | ja — geen net op deze korrel |
| b4 | C | truck | wegvertex → `ni-clydach-refinery` | A4232 → M4 J33–J45 → A4067 → B4291; KOPIE van `nikkel-matsusaka-clydach` b4 | 74 (Vale: 148 km retour) [8]; OSRM 74,3; gebakken kopie 78,1 [7] | letterlijke kopie `nikkel-matsusaka-clydach-weg-cardiff-clydach.geojson` | nee |

De naad zeeknoop 4161 → Cardiff-kade is 1,3 km (binnen de 5 km-norm) en geen eigen been; na b3 is de naad naar de last-mile-stippel 1,25 km.
Beenbenamingen b3 en b4 dragen "(aannemelijk: één bron)"; b1 en b2 zijn gewone gemeten benen.

## 3 · Ankers (één per site en per overslag; alle vier hergebruikt letterlijk)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-sorowako-plant` | mijn + smelter (site-anker) | PT Vale Indonesia — Sorowako, aan Danau Matano | -2.5203, 121.3575 | brief `nikkel-sorowako-matsuzaka` §3 [6] | bron-gelegd (overgenomen: mijnstad, open-pit en smelter als één complex; het smelterperceel zelf niet apart geïsoleerd) |
| `ni-balantang-kade` | overslag weg → zee | Pelabuhan Balantang, Desa Balantang, Kec. Malili | -2.6428, 121.0732 | brief `nikkel-sorowako-matsuzaka` §3 [6] | bron-gelegd (overgenomen: z18 kade met stockpiles en loodsen) |
| `ni-cardiff-kade` | overslag zee → weg | Port of Cardiff (ABP), Roath Dock | 51.4595, -3.1551 | brief `nikkel-matsusaka-clydach` §3 [7] | onzeker (overgenomen: kade met transitloodsen; Queen Alexandra Dock even goed mogelijk) |
| `ni-clydach-refinery` | raffinaderij (site-anker) | Vale Clydach Nickel Refinery, Ynys-Penllwch Road, Clydach | 51.6956, -3.8892 | brief `nikkel-matsusaka-clydach` §3 [7][10] | bron-gelegd (overgenomen: raffinaderijcomplex met hoge installaties en tanks) |

Geen nieuw anker en dus geen nieuwe satellietblik: de vier punten zijn al op Esri z15–z18 gezien in de twee moederbrieven.
Let op: sitelaag `w-sorowako-vale` (-2.568, 121.3785) ligt ~5,8 km zuidoostelijk van `ni-sorowako-plant` (centraal beoordelen).

## 4 · Via-punten (alleen landbenen met een corridorkeuze; alle kopie)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1–4 | Asuli · Wasuponda · Balambano · Malili (doorgaande weg, niet het centrum) | -2.5964,121.3244 · -2.5971,121.2583 · -2.6607,121.2516 · -2.6191,121.1163 | houden de route op de Jalan Poros Malili-Soroako [6] |
| b4 | 1 | A4232 Butetown/Grangetown Link | 51.4740, -3.2285 | uit de dokken de A4232 op, niet de stad in [7] |
| b4 | 2 | A4232 vlak voor M4 J33 | 51.5014, -3.3022 | A4232 tot J33, niet de A48 [7] |
| b4 | 3 | M4 tussen J34 en J35 | 51.5109, -3.4258 | pint de M4 [7] |
| b4 | 4 | M4 bij J36 Sarn | 51.5337, -3.5567 | mainline [7] |
| b4 | 5 | M4 Port Talbot (net ten zuiden van J40) | 51.5882, -3.7682 | M4-viaduct i.p.v. A48 [7] |
| b4 | 6 | A4067 Ffordd Cwm Tawe, ten noorden van J45 | 51.6856, -3.9056 | af op J45 en de A4067 op, niet via J44/A48 [7] |
Geofabrik-regio's: b1 `indonesie`, b4 `groot-brittannie` (beide aanwezig; er wordt niets opnieuw gerouteerd, alleen gekopieerd).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sorowako-smelter | PT Vale Indonesia (Vale/SMM/MIND ID) | lateriet-erts → nikkel-matte | 70.728 t nikkel in matte 2023, 13,45 Mt erts | [5] |
| Clydach Nickel Refinery | Vale Base Metals | nikkeloxide uit Canada en Indonesië → carbonyl-nikkel (poeder, pellets, 99,9 %) | 40 kt/j nominaal; 31,3 kt Ni in 2023 | [2][3][4] |

## 6 · Stoppunt
De brief stopt bij Clydach: de pellets en het poeder gaan naar 280+ klanten in 30+ landen zonder afnemer per lading — geen fase D.

## 7 · Open punten
- **Eén bron voor de directe lus, en die is oud:** de 6-K van feb 2010 (4Q09) meldt dat een deel van de Sorowako-feed die naar Matsuzaka ging naar Clydach is verlegd, tijdelijk na de stakingen in Canada [1]; het zegt niet in welke vorm (matte of oxide), niet via welke haven en niet voor hoe lang. De huidige VBM-pagina noemt alleen "nikkeloxide uit Canada en Indonesië" [2], zonder Sorowako of Cardiff. De Matsusaka-route (twee bestaande stromen) is de gangbare weg.
- **Cardiff als aanvoerhaven is afgeleid** uit de Vale-elektrische-truck Cardiff → Clydach [8] (zie moederbrief); dok en kade onzeker.
- **Geen aandeel Sorowako → Clydach:** 70.728 t is de bovengrens. Bron [5] noemt "nickel matte" en tegelijk 78 % Ni in de matte; of 70.728 t het nikkelgehalte is of de brutomatte (dan ~55 kt Ni) is niet uitgezocht.
- **Zeereis is een routeruitkomst:** 17.483 km is MARNET (Soenda-straat, Suez), niet een gepubliceerde rederijroute. Het ontwerp noemde Singapore/Malakka; de router kiest de Soenda-straat.
- **Zeeknoop 4161 ligt in de afgedamde Cardiff Bay**, de lijn eindigt daar en niet in het dok (naad 1,25 km, bewust).
- b1 heeft geen gepubliceerde wegkm: de ±15%-toets is een indicatie (kopie van een gebakken lijn van 60,5 km, ketenontwerp ~60).
- Clydach en Sorowako-plant staan als anker/marker, niet als eigen sitelaagrij; Clydach ontbreekt in `nikkel-sitelaag.json` (centraal).

## 8 · Bronnen
[1] Vale, Form 6-K (4Q09 productieverslag, 2010): "part of the Sorowako feed to Matsuzaka, in Japan, was reallocated to Clydach, in Wales, UK". https://www.sec.gov/Archives/edgar/data/917851/000095012310011268/c96033e6vk.htm
[2] Vale Base Metals, Clydach: enige Britse nikkelraffinaderij, "refining nickel oxide sourced from VBM operations in Canada and Indonesia". https://valebasemetals.com/our-operations/clydach/
[3] Vale, Form 20-F 2021: Clydach 40.000 t/j nominaal, feed uit Sudbury en Matsusaka. https://www.sec.gov/Archives/edgar/data/917851/000110465922046078/vale-20211231x20f.htm
[4] Vale Base Metals, "Clydach 2023 >> 2024": 31.328 t Ni in 2023. https://vale.com/documents/d/guest/clydach-wales
[5] Wikipedia, "Sorowako mine": 70.728 t nikkel-matte in 2023 (13.452.663 t erts), matte ~78 % Ni. https://en.wikipedia.org/wiki/Sorowako_mine
[6] Brief `nikkel-sorowako-matsuzaka.md` §3/§4/§9: anker- en via-punten Sorowako/Balantang, geojson b1 en aanloop Balantang.
[7] Brief `nikkel-matsusaka-clydach.md` §3/§4/§9: ankers Cardiff/Clydach, zes via-punten, last-mile-stippel, wegbeen.
[8] Vale, "Transforming the future – Vale in Wales, U.K." (2023): elektrische truck Cardiff → Clydach, 148 km retour. https://vale.com/documents/d/guest/transforming-the-future-vale-in-wales-u-k
[9] `hecht_marnet.py route` testrun 2026-11-01: zeeknoop 6080 (-3.3140,120.6714) → 4161 (51.4579,-3.1730) = 17.482,9 km, 107 MARNET-edges, 1.804 punten; passeert Soenda-straat, Bab-el-Mandeb, Suez, Gibraltar, Biskaje, niet Malakka.
[10] Vale, Technical Report Summary Ontario Operations (6-K 2023-04-03): Clydach 51°41'44"N 3°53'21"W. https://www.sec.gov/Archives/edgar/data/917851/000129281423001493/vale20230403_6k.htm

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-nikkel-sorowako-clydach.json` (101,5 KB, contract versie 2, punt_formaat lonlat) · **recept:**
`bak_nikkel_sorowako_clydach` in `v2/tools/bak_stromen.sh` · **totaal 17.712,2 km · 5.248 punten · 4 markers.**
Geen nieuw geojson en geen nieuw wegprofiel: vier van de vijf benen zijn letterlijke kopieën van bestaande stromen, alleen b3 is nieuw gerouteerd.

| # | modaliteit | km gebakken | punten | stijl | herkomst |
|---|---|---|---|---|---|
| b1 | truck | 60,5 | 1.971 | doorgetrokken | kopie `nikkel-sorowako-matsuzaka-weg-sorowako-balantang.geojson` |
| b2 | zee (haven-aanloop Balantang) | 90,4 | 64 | stippel (net reikt niet) | kopie `nikkel-sorowako-matsuzaka-aanloop-balantang.geojson` |
| b3 | zee (MARNET 6080 → 4161) | 17.482,9 | 1.804 | doorgetrokken | nieuw: `--been` knoop → knoop, 107 edges |
| b4a | truck (last mile Cardiff) | 0,26 | 2 | stippel (geen net op deze korrel) | kopie `nikkel-matsusaka-clydach` b3 |
| b4 | truck | 78,1 | 1.407 | doorgetrokken | kopie `nikkel-matsusaka-clydach-weg-cardiff-clydach.geojson` |

**Markers (4, alle op het ankerpunt, 0,0 km van de lijn):** Sorowako (-2.5203, 121.3575), Balantang (-2.6428, 121.0732), Cardiff Roath Dock (51.4595, -3.1551), Clydach (51.6956, -3.8892).

**Toets:**
- b1: gebakken 60,5 km tegen hemelsbreed 34 km, geen wegkm gepubliceerd; de ±15%-toets is een indicatie (ketenontwerp ~60 km, +0,8%).
- b4: 78,1 km tegen gepubliceerd 74 km (Vale, 148 km retour) = +5,5%, binnen ±15%.
- b3: 17.482,9 km is de routeruitkomst, geen gepubliceerde waarde; lengte-invariant +0,156 km (naden). Passeert Soenda-straat, Bab-el-Mandeb, Suez, Gibraltar, Biskaje.
- Naden: b1-b2 0 m, b2-b3 0 m, b3-b4a 1,25 km (zeeknoop 4161 in de afgedamde Cardiff Bay naar de Cardiff-kade), b4a-b4 0 m. Maximum 1,25 km, dus geen naad > 5 km.
- `toets_knikken.py`: b1 18 knikken (1 omkering, geen terugloop), b3 4, b4 10 (1 omkering, geen terugloop); 0 terugloop in totaal, niets te repareren.
- Rechte benen: alleen de last-mile-stippel (0,26 km, 2 punten) is recht en ligt ruim onder de 5 km; de aanloop heeft 64 punten. `toets_rechte_benen.py` scant alleen geregistreerde stromen, dus deze stroom verschijnt pas na centrale registratie.
- JSON: versie 2, punt_formaat lonlat, modaliteiten {zee, truck}, elk been ≥ 2 punten.

**Recept (volgorde = reisvolgorde):** (1) `--been-geojson truck` kopie b1; (2) `--stippel-geojson zee` kopie aanloop Balantang; (3) `--been zee -3.3140,120.6714 → 51.45790,-3.17300`; (4) `--stippel truck` 51.4595,-3.1551 → 51.460161,-3.158666; (5) `--been-geojson truck` kopie Cardiff → Clydach; vier `--marker`.

**Toelichting stippel/aanloop:** b2 is de haven-aanloop Balantang (kade 86,95 km van MARNET-zeeknoop 6080, LAR-586), stippel omdat MARNET daar niet reikt. b4a is de last mile van de Cardiff-kade naar de eerste wegvertex van het doorgaande net (eigen verbinding zonder net). "Aannemelijk: één bron" staat in de beennamen b3 en b4, niet in de lijnstijl: b3 en b4 zijn doorgetrokken.
Geen vlucht, geen leiding, geen spoor, geen binnenvaart; geen extract gedownload; sitelagen, register en bundel niet aangeraakt.

**Lessen:**
- Een keten die alleen uit bestaande geojson-kopieën plus één MARNET-been bestaat bakt in ~20 s en heeft geen wegscan of slot nodig.
- MARNET kiest voor Sorowako → Cardiff de Soenda-straat en Suez (17.483 km), niet Malakka; de zeereis is dus een routeruitkomst en geen rederijbron.
- Open (centraal): sitelaag `w-sorowako-vale` ligt 5,8 km van `ni-sorowako-plant`; Clydach ontbreekt in `nikkel-sitelaag.json`; register- en bundelregistratie volgen centraal.
