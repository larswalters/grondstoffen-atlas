# Routebrief (licht) · nikkel — Matsusaka (Japan) → Cardiff → Clydach (Wales)

**stroom-id:** `nikkel-matsusaka-clydach` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** Vale-nikkeloxide (NOS/Tonimet) van de Matsusaka-fabriek (Mie, Japan) gaat per **zeeschip** via
Malakka, Suez en Biskaje naar de haven van **Cardiff**, per **truck** over de A4232 en de M4 naar de Vale Clydach
Nickel Refinery (Swansea Valley), waar de carbonyl-raffinage er pellets en poeder van maakt — verwerker naar
verwerker, Azië naar Europa. Stoppunt bij de raffinaderij.
**Welke as van het verhaal:** de interne Vale-lus tussen twee verwerkers: Japanse oxide-sinter als feed voor de enige
Britse nikkelraffinaderij. Clydach produceerde 31.328 t Ni in 2023 (31.000 t in 2022) [1][2]; nominale capaciteit
40.000 t/j [3]; Matsusaka maakt ~60 kt/j NOS+Tonimet [4]. Het Matsusaka-aandeel in de Clydach-feed is niet gebronnen
(de andere feed is Sudbury-oxide) — eenheid kt Ni/j.

## 1 · Ketenkaart
```
Matsusaka-fabriek `ni-matsusaka-kade` ──(b1 zee · haven-aanloop, stippel · ~12 km)──► MARNET-zeeknoop 5767
   ──(b2 zee · MARNET · Malakka → Bab-el-Mandeb → Suez → Gibraltar → Biskaje → Bristolkanaal · ~20.360 km)──►
   MARNET-zeeknoop 4161 ──(b3 zee · 1,3 km hemelsbreed, geen aanloop nodig)──► Cardiff-kade `ni-cardiff-kade`
   ──(b4 truck · A4232 → M4 → A4067 → B4291 · ~74 km)──► Clydach Nickel Refinery `ni-clydach-refinery` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ni-matsusaka-kade` → zeeknoop 5767 | haven-aanloop, kade 11,87 km van de knoop; KOPIE van `nikkel-sorowako-matsuzaka` b4 (omgekeerd) | 12,05 (gemeten, aanloop-bake golf 2) | letterlijke kopie `nikkel-sorowako-matsuzaka-aanloop-matsusaka.geojson`, puntvolgorde omgekeerd | ja — net reikt niet |
| b2 | B | zee | zeeknoop 5767 → zeeknoop 4161 | Malakka, Bab-el-Mandeb, Suez, Gibraltar, Biskaje, Bristolkanaal (MARNET-testrun, geen Kaap) | 20.361 (testrun, indicatief; ontwerp 19–20 mille) [12] | MARNET (`--been` zee, zeeknoop → zeeknoop) | nee |
| b3 | B | zee | zeeknoop 4161 → `ni-cardiff-kade` | kade ligt 1,3 km van de zeeknoop (<5 km): geen aanloop vereist | 1,3 hemelsbreed | — (naad, ruim binnen de 5 km-norm) | nee |
| b4 | C | truck | `ni-cardiff-kade` → `ni-clydach-refinery` | A4232 (Butetown Link) → M4 J33–J45 → A4067 → B4291 | 74 (Vale: 148 km retour) [1]; OSRM-controle 74,3 [10] | maak_stroombeen_weg, extract `groot-brittannie` | nee |

De benen b2–b4 dragen in de naam "(aannemelijk: Cardiff als aanvoerhaven uit één bron)"; geen naad boven 5 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-matsusaka-kade` | fabriek + losplek (herbruikt letterlijk uit `nikkel-sorowako-matsuzaka` §3) | Vale Base Metals / Tokyo Nickel Co. — Matsusaka (NOS/Tonimet), Mie | 34.6050, 136.5520 | [4][14] | aannemelijk (z15 opnieuw gezien: groot industrieterrein op een landtong tussen twee riviertakken met kademuur; perceel niet door een bron bevestigd) |
| `ni-cardiff-kade` | overslag zee → truck | Port of Cardiff (ABP), Roath Dock, oostoever van het loodsenblok | 51.4595, -3.1551 | [1][7] | onzeker (z16 gezien: doorlopende kade met transitloodsen aan Roath Dock; Vale noemt alleen "Cardiff", geen kade of dok) |
| `ni-clydach-refinery` | raffinaderij (site-anker) | Vale Clydach Nickel Refinery, Ynys-Penllwch Road, Clydach (Swansea) | 51.6956, -3.8892 | [6][1] | bron-gelegd (z15 gezien: aaneengesloten raffinaderijcomplex met hoge installaties, loodsen en tanks aan de rand van Clydach; punt = 51°41'44"N 3°53'21"W uit het Vale-rapport, ligt aan de noordrand bij de toegangsweg) |

## 4 · Via-punten (alleen b4; punten op de doorgaande weg, niet in een centrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b4 | 1 | A4232 Butetown/Grangetown Link | 51.4740, -3.2285 | pint de uitrit uit de dokken op de A4232 (Cardiff Bay Link) in plaats van de stad in [9][10] |
| b4 | 2 | A4232, vlak voor M4 J33 | 51.5014, -3.3022 | houdt de route op de A4232 tot aan J33, niet via de A48 [9] |
| b4 | 3 | M4 tussen J34 en J35 | 51.5109, -3.4258 | pint de M4 (en niet de A48/A473) [10] |
| b4 | 4 | M4 bij J36 Sarn | 51.5337, -3.5567 | midden-M4 op de mainline (geen afrit) [10] |
| b4 | 5 | M4 Port Talbot (net ten zuiden van J40) | 51.5882, -3.7682 | houdt de route op het M4-viaduct i.p.v. de A48 door Port Talbot [10] |
| b4 | 6 | A4067 Ffordd Cwm Tawe, ten noorden van J45 | 51.6856, -3.9056 | laatste corridorkeuze: af op J45 Ynysforgan en de A4067 op naar Clydach, niet via J44 en de A48 [9][6] |
Refs voor het profiel: A4232, M4, A4067, B4291. Gecontroleerd met een OSRM-run (OSM-data) door alle zes punten: 74,3 km, gelijk aan de directe route [10].

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Matsusaka | Vale Base Metals (Vale 87,2 %, Sumitomo rest) | PTVI-matte → nikkeloxide-sinter (NOS) + Tonimet; "levert aan Clydach" | ~60 kt/j intermediair (30 kt Ni finished) | [3][4] |
| Clydach Nickel Refinery | Vale (100 %) | nikkeloxide uit Sudbury en Matsusaka → carbonyl-nikkel (poeder, pellets, >99,9 %) | 40 kt/j nominaal; 31,3 kt Ni in 2023 | [1][2][3] |

## 6 · Stoppunt
De brief stopt bij Clydach: de pellets en het poeder gaan volgens Vale naar 280+ klanten in 30+ landen, zonder
afnemer per lading — geen fase D.

## 7 · Open punten
- **Cardiff als aanvoerhaven is afgeleid**: Vale noemt een elektrische truck met "feed material" Cardiff → Clydach (148 km retour) [1], zonder product of herkomst. Matsusaka-oxide of Sudbury-oxide, en of Cardiff de enige haven is, staat nergens. Daarom "aannemelijk: één bron" in de beennaam.
- **De kade in Cardiff is onzeker**: `ni-cardiff-kade` ligt aan Roath Dock (transitloodsen); Queen Alexandra Dock (oostelijk) is even goed mogelijk. Geen bron noemt een dok.
- **Geen bron voor de zeereis** (rederij, route, containers of bulk): MARNET kiest Suez; de lengte 20.361 km is een testrun, geen gepubliceerde waarde.
- **Zeeknoop 4161 ligt in de afgedamde Cardiff Bay** (ligt 1,3 km van de kade, binnen de 5 km-norm). De sluisroute naar het dok is niet getekend; een haven-aanloop bij de baker is optioneel.
- **Matsusaka-aandeel in de Clydach-feed niet gebronnen**; Vale noemt alleen "Sudbury en Matsusaka" [3][4][5]. De 6-K van 2010 meldt dat een deel van de Sorowako-matte direct naar Clydach is verlegd [13] — andere keten, niet getekend.
- `ni-matsusaka-kade` blijft aannemelijk (zie de brief van Sorowako → Matsuzaka §7).
- Clydach en Matsusaka ontbreken in `nikkel-sitelaag.json` (centraal bijwerken).

## 8 · Bronnen
[1] Vale, "Transforming the future – Vale in Wales, U.K." (2023): Clydach 31.000 t Ni in 2022; elektrische truck Cardiff → Clydach, 148 km retour. https://vale.com/documents/d/guest/transforming-the-future-vale-in-wales-u-k
[2] Vale Base Metals, "Clydach 2023 >> 2024": 31.328 t Ni in 2023, 100 % van het Britse geraffineerde nikkel. https://vale.com/documents/d/guest/clydach-wales
[3] Vale, Form 20-F 2021 (tabel Lines of Business): Clydach verwerkt nikkeloxide "supplied from our Sudbury and Matsusaka operations", nominaal 40.000 t/j; Matsusaka 60.000 t/j intermediair en levert aan "refineries in the UK, and Canada". https://www.sec.gov/Archives/edgar/data/917851/000110465922046078/vale-20211231x20f.htm
[4] Vale Base Metals, Matsusaka: NOS en Tonimet, ~60 kt/j, levert aan "VBM's Clydach Refinery in the UK". https://valebasemetals.com/our-operations/matsusaka/
[5] Vale, Form 6-K 2018: dezelfde zin over Clydach (Sudbury en Matsusaka). https://www.sec.gov/Archives/edgar/data/917851/000110465918036665/a18-14554_16k.htm
[6] Vale, Technical Report Summary Ontario Operations (Form 6-K, 2023-04-03): Clydach Refinery 51°41'44"N 3°53'21"W, toegang via Hebron Road/B4603 en Ynyspenllwch Road/B4291. https://www.sec.gov/Archives/edgar/data/917851/000129281423001493/vale20230403_6k.htm
[7] Wikipedia, "Cardiff Docks": Roath Dock, Queen Alexandra Dock, containers en dry bulk, 51.4653 -3.1538. https://en.wikipedia.org/wiki/Cardiff_Docks
[8] Wikipedia, "Clydach, Swansea": dorp bij de M4, 9,7 km NO van Swansea. https://en.wikipedia.org/wiki/Clydach,_Swansea
[9] OpenStreetMap (ODbL) via Overpass-spiegel maps.mail.ru: M4-aansluitingen J33–J45, A4232-segmenten (Butetown Link, Southern Way), A4067/B4291. https://www.openstreetmap.org
[10] OSRM-demoserver (OSM-routering): Cardiff-kade → Clydach 74,3 km via A4232, M4, A4067, B4291. https://router.project-osrm.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16): `v2/build-cache/satcheck/sat-nikkel-matsusaka-clydach-{clydach,cardiff-docks,cardiff-qad,cardiff-qad-west,matsusaka}.png`.
[12] `hecht_marnet.py route` testrun (scratchpad, niet gebakken): zeeknoop 5767 → 4161 = 20.361 km over 137 MARNET-edges, via Malakka, Suez, Gibraltar.
[13] Vale, Form 6-K 2010 (Q4 2009): deel van de Sorowako-feed naar Matsuzaka verlegd naar Clydach. https://www.sec.gov/Archives/edgar/data/917851/000095012310011268/c96033e6vk.htm
[14] Brief `nikkel-sorowako-matsuzaka.md` §3/§9: anker en aanloop-geojson Matsusaka.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
Bestand `v2/data/stroomroute-nikkel-matsusaka-clydach.json` (65,2 KB, versie 2, lonlat) · functie `bak_nikkel_matsusaka_clydach` in `bak_stromen.sh` · profiel `nikkel-matsusaka-clydach-cardiff-clydach` in `maak_stroombeen_weg.py` · **4 benen · 20.451,7 km · 3.520 punten · 3 markers**.

| # | modaliteit | km | naad naar vorig been | geometrie |
|---|---|---|---|---|
| 1 | zee, **stippel** (haven-aanloop Matsusaka) | 12,1 | 0 | letterlijke kopie van `nikkel-sorowako-matsuzaka-aanloop-matsusaka.geojson`, puntvolgorde omgekeerd (kade 34,6050 / 136,5520 naar zeeknoop 5767) |
| 2 | zee (aannemelijk: één bron) | 20.361,2 | 0,00 | MARNET zeeknoop 5767 naar 4161, 137 edges, via Malakka, Bab-el-Mandeb, Suez, Gibraltar; hemelsbreed 9.660 km |
| 3 | truck, **stippel** (last mile) | 0,3 | 1,25 | rechte lijn kade naar eerste wegvertex; b3 uit de brief (zeeknoop 4161 naar kade, 1,3 km) is een naad en geen eigen been |
| 4 | truck (aannemelijk: één bron) | 78,1 | 0,00 | `maak_stroombeen_weg` via `wegscan_puur.py`, extract groot-brittannie |

**Recept:** `bash v2/tools/bak_stromen.sh nikkel-matsusaka-clydach`. Aanloop-geojson en wegbeen staan in `v2/build-cache/ais/graaf/` met prefix `nikkel-matsusaka-clydach-`; wegscan 8 tot 11 minuten voor groot-brittannie (14,3 mln nodes in het venster), tweede run uit de cache.

**Toets:** wegbeen 78,0 km tegen gepubliceerd 74 (Vale 148 km retour) = **+5,4% (OK)**; OSRM gaf 74,3. Zes via-punten pakten allemaal binnen 0,06 km. Grootste naad 1,25 km (zee-eindknoop naar de last-mile-stippel), ruim onder 5 km. Markers liggen 0,0 km van hun lijn. `toets_knikken.py`: truck 10 knikken, 1 omkering (156 graden bij 51,5100 / -3,3591 = de aansluiting A4232 naar M4 J33, echte scherpe bocht, geen terugloop), de overige knikken zijn korte afrit-pieken (R 2 tot 29 m). `toets_rechte_benen.py --min-km 5`: geen rechte benen in deze stroom (alleen de gewenste stippels).

**Toelichting per stippel:**
- *b1 haven-aanloop Matsusaka:* de kade ligt 11,87 km van de MARNET-zeeknoop; zonder aanloop een naad van 11,9 km (LAR-586). Kopie van de Sorowako-stroom, geen tweede versie.
- *b3 last mile Cardiff:* het kade-anker (51,4595 / -3,1551) snapt in de OSM-data op een los dock-component van twee service-ways. De dichtstbijzijnde vertex van het doorgaande net ligt op 0,26 km (51,460161 / -3,158666, een echte OSM-vertex) en is de eerste via van het wegprofiel. Het stukje anker naar die vertex is een stippel (dock-interne wegen niet doorverbonden), geen verzonnen lijn.

**Bevindingen / open (aanvullend op §7):**
- Zeeknoop 4161 ligt in de afgedamde Cardiff Bay; de gemeten zeelijn eindigt daar en niet in het dok. De 1,25 km tot de kade is bewust naad (binnen de norm) en geen aanloop.
- b2 20.361 km is een router-uitkomst zonder gepubliceerde waarde; er is geen bron voor de zeereis, route of vervoerder.
- Cardiff-kade blijft onzeker (Roath Dock, Queen Alexandra Dock even goed mogelijk); de last mile en het wegbeen beginnen op een vertex 0,26 km daarvandaan.
- A4232 deelbeen 2 is 10,0 km tegen ~6 km hemelsbreed (de A4232 maakt een lus langs Culverhouse Cross): geen omweg door een via-punt, de totale lengtetoets klopt.
- Clydach en Matsusaka ontbreken in `nikkel-sitelaag.json` (centraal bijwerken).

**Lessen (gereedschap):**
- `maak_stroombeen_weg.py` en andere gedeelde bestanden worden door meerdere agenten tegelijk bewerkt: een read-modify-write met Python overschreef mijn eigen via-wijziging (en de scan-cache bleef bij dezelfde hash). Gebruik de Edit-tool voor één kleine gerichte edit en controleer met grep dat hij er na afloop nog staat.
- Een kade-anker kan op een los dock-component van enkele service-ways snappen (geen wegpad tussen punt 0 en 1): zoek de dichtstbijzijnde vertex van het grootste component en maak dat de eerste via, met een korte stippel naar het anker.
