# Routebrief (licht) · Zeldzame aardmetalen · KSM Metals Cheongju → Busan → Long Beach → Noveon San Marcos (Zuid-Korea → Verenigde Staten)

**stroom-id:** `ree-cheongju-sanmarcos` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** NdPr-/NdFeB-legering van KSM Metals (= ASM/Energy Fuels' Korean Metals Plant, Cheongju) gaat per truck (Jungbu Naeryuk) naar Busan New Port, per containerschip over de Stille Oceaan naar Long Beach en per truck (SR-91 → I-10 → I-35) naar Noveon Magnetics in San Marcos, Texas. Aannemelijk: B/L noemt Busan en LA/Long Beach, geen terminal, geen modaliteit.
**Welke as van het verhaal:** de niet-Chinese legeringsschakel naar een VS-magneetmaker. Volume: 9 containers, 78,9 t PrNdFeB-legering t/m 2026-06-27, geen jaarcijfer [1]; KMP-capaciteit 1,3 kt NdFeB-legering/j, uitbreiding naar 3,6 kt/j (kt legering, geen REO; peiljaar 2026) [5]; Noveon-afspraak 100 t (mei 2023) [3].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** titel/beennaam "aannemelijk: B/L noemt Busan en LA/Long Beach"; kop-anker onzeker; Busan-aanloop = omgekeerde kopie van kobalt-huayou-gunsan; Long Beach-aanloop = kopie ree-yunsheng-longbeach; km hemelsbreed, geen wegkm. Eindpunt = id (Noveon San Marcos).

## 1 · Ketenkaart
```
KSM Metals / KMP Cheongju `ree-ksm-fabriek` ──(b1 truck · Jungbu 35 → Gyeongbu 1 → 30 → Jungbu Naeryuk 45 → Changwon → Busan · hemelsbreed 222 km)──►
Busan New Port `ree-busan-kade` ──(b2a haven-aanloop, STIPPEL · 10,8 km)──► zeeknoop 5621 ──(b2 zee · MARNET · 9.880 km)──► zeeknoop 4488
──(b3 haven-aanloop, STIPPEL · 8,5 km)──► Long Beach-kade `ree-longbeach-kade` ──(b4 truck · SR-91 → I-10 → I-35 · hemelsbreed 1.960 km)──►
Noveon San Marcos `ree-noveon-fabriek` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (aannemelijk: B/L noemt alleen Busan) | `ree-ksm-fabriek` → `ree-busan-kade` | Jungbu Expwy 35 → Gyeongbu 1 → Seosan-Yeongdeok 30 → Jungbu Naeryuk 45 → Changwon → Jinhae Sanup-ro → Sinhang | hemelsbreed 222 km, geen wegkm (OSRM 279 km is OSM-afgeleid, indicatie) [9] | maak_stroombeen_weg (extract zuid-korea) | nee |
| b2a | B | zee (haven-aanloop) | `ree-busan-kade` → zeeknoop 5621 (35.0485, 128.7268) | Busan New Port-aanloop (kade 10,1 km van de knoop > 5 km, LAR-586) | 10,8 (kopie, omgekeerd) [10] | stippel-geojson | **ja** — MARNET reikt niet tot de kade |
| b2 | B | zee (aannemelijk: B/L noemt Busan en LA/Long Beach) | zeeknoop 5621 → zeeknoop 4488 (33.7039, -118.1945) | Korea-straat → noordelijke Stille Oceaan | 9.879,5 (MARNET-proef 2026-10-30, 61 edges, naden 0); grootcirkel kade-kade 9.663 [13] | MARNET | nee |
| b3 | B | zee (haven-aanloop) | zeeknoop 4488 → `ree-longbeach-kade` | Long Beach-havenbekken (kade 6,47 km > 5 km) | 8,5 (kopie ree-yunsheng-longbeach) [11] | stippel-geojson | **ja** — MARNET reikt niet tot de kade |
| b4 | D | truck (aannemelijk: modaliteit niet gebronnd) | `ree-longbeach-kade` → `ree-noveon-fabriek` | SR-91 → CA-60 → I-10 (Blythe, Phoenix, Tucson, El Paso, Junction) → Loop 1604 → I-35 | hemelsbreed 1.960 km, geen wegkm (OSRM 2.249 km is OSM-afgeleid, indicatie) [9] | maak_stroombeen_weg (us-california, us-arizona, us-new-mexico, us-texas) | nee |

Beennaam b2: "… (aannemelijk: B/L noemt Busan en LA/Long Beach, geen terminal)". Geen luchtbeen: geen bron zegt dat de legering vliegt; de B/L toont containers (HMM Turquoise, Saturn Maritime) [1]. b3 is een LETTERLIJKE KOPIE van `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (zeeknoop → kade, zelfde richting; ook gebruikt in bak_ree_ganzhou_fremont).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-ksm-fabriek` | legeringsfabriek (kop b1) | KSM Metals Co Ltd / Korean Metals Plant, 83 Gwahaksaneop 4-ro, Oksan-myeon, Cheongju | 36.7009, 127.4147 | [1][8] B/L-adres, Nominatim wegnode 과학산업4로 (huisnr. niet te geocoderen) | **onzeker** (z15/z16 gezien: dicht industrieterrein met hallen en een grote parkeervlakte; plantgebouw niet aanwijsbaar; ASM/Segye plaatsen KMP in Ochang-eup, B/L in Oksan-myeon [3][6]) |
| `ree-busan-kade` | overslag truck → zee | Busan New Port, containerterminal | 35.0731, 128.8338 | hergebruikt letterlijk uit `kobalt-huayou-gunsan.md` §3 (`co-busan-newport`) [10] | bron-gelegd daar (z15: containerstapels, portaalkranen); terminal voor deze lading niet gebronnd |
| `ree-longbeach-kade` | overslag zee → truck | containerkade Long Beach, westkade oostelijk havenbekken | 33.7600, -118.2132 | hergebruikt letterlijk uit `ree-yunsheng-longbeach.md` §3 [11] | aannemelijk (portaalkranen, containerstapels; terminal onbekend; LA of Long Beach niet beslist) |
| `ree-noveon-fabriek` | losplek / magneetfabriek | Noveon Magnetics, 1550 Clovis R. Barker Rd, San Marcos TX | 29.8413, -97.9554 | hergebruikt letterlijk uit `ree-larochelle-sanmarcos.md` §3 [12]; adres [2] | aannemelijk (straatniveau, pand niet te onderscheiden) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Alle punten zijn wegvertices uit een OSRM-route [9] (lat, lon), op snelweg/doorgaande weg, niet in een stadscentrum; te converteren naar (lon, lat) in het profiel.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Seosan-Yeongdeok 30, oost van Cheongju | 36.5228, 127.5311 | pint 35 → 1 → 30 oostwaarts i.p.v. de Gyeongbu zuidwaarts naar Daejeon |
| b1 | 2 | knooppunt 30/45, Sangju-zone | 36.3586, 128.2365 | pint de overstap op Jungbu Naeryuk 45 |
| b1 | 3 | Jungbu Naeryuk 45 (Gimcheon-Goryeong) | 36.0244, 128.2675 | houdt de route west van Daegu, niet via de Gyeongbu-stad |
| b1 | 4 | Jungbu Naeryuk 45 (Changnyeong-zone) | 35.4901, 128.5107 | idem, zuidelijk deel |
| b1 | 5 | Changwon-zone, 30/1004 | 35.2836, 128.5102 | pint Changwon i.p.v. Gimhae/Busan-stad |
| b1 | 6 | Jinhae Sanup-ro, naar Gadeok | 35.1590, 128.7150 | pint de aanvoer naar Busan New Port (Sinhang) |
| b4 | 1 | SR-91 Riverside Fwy (Anaheim Hills) | 33.8688, -117.7300 | pint SR-91/CA-60 naar I-10 i.p.v. I-10 door downtown LA |
| b4 | 2 | I-10 bij Blythe | 33.6478, -114.3233 | pint I-10 door de Colorado-woestijn (geen I-8) |
| b4 | 3 | I-10 Tonopah, west van Phoenix | 33.5542, -113.2575 | pint I-10 langs Phoenix (niet I-8 zuid) |
| b4 | 4 | I-10 Benson | 31.9651, -110.2650 | pint I-10 oostwaarts na Tucson |
| b4 | 5 | I-10 Deming | 32.2457, -107.1539 | pint I-10 door New Mexico (Las Cruces-corridor) |
| b4 | 6 | I-10 El Paso, oost | 31.7886, -106.5193 | pint de grensstad-passage op I-10 |
| b4 | 7 | I-10 Sonora | 30.6198, -100.8208 | pint I-10 door Zuid-Texas (niet I-20 via Midland) |
| b4 | 8 | Loop 1604 San Antonio, west | 29.5916, -98.5919 | pint de bypass naar I-35 buiten het centrum |
Gebruik als refs b1 ["35","1","30","45"], b4 ["I 10","I 35"]; venster 40 km (75 als de scan faalt). De Daegu-variant (Gyeongbu) is niet getekend.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Korean Metals Plant (KSM Metals/KSMM), Cheongju | ASM, sinds 2026-08-28 Energy Fuels | oxiden/metaal → NdPr-metaal en NdFeB-strip-cast-legering (Dy/Tb eerste verkopen) | 1,3 kt NdFeB-legering/j, naar 3,6 kt/j (kt legering) | [3][4][5] |
| Noveon Magnetics, San Marcos | Noveon | NdFeB-legering → gesinterde magneten | niet gepubliceerd | [2][12] |

## 6 · Stoppunt
Bij Noveon San Marcos: de enige afnemer in de bronnen [1][2][3]; Noveon is zelf het eindschakel-adres (fase E vervalt, geen gedocumenteerde klant erna).

## 7 · Open punten
- **KSM Metals = KMP is een afleiding** uit [5] (naamgelijkstelling), ASM noemt exploitant KSMM en Noveon als klant [3]; alleen een gratis ImportGenius-samenvatting, geen volledig record.
- **Kop-anker onzeker:** straatniveau Gwahaksaneop 4-ro (B/L: Oksan-myeon; ASM/Segye: Ochang-eup, Ochang Foreign Investment Zone); huisnummer 83 niet geocodeerd, plantgebouw niet gezien [6][8].
- **Busan als laadkade en truck Cheongju-Busan zijn niet gebronnd** (B/L noemt alleen Busan); Gyeongbu via Daegu is een gelijkwaardig alternatief.
- **Long Beach of Los Angeles:** KSM-record noemt Long Beach als top-VS-haven, het Noveon-record alleen één LA-voorbeeld; geen terminal [1][2]. Truck Long Beach → San Marcos is aanname (dray).
- **Km:** geen gepubliceerde wegkm; de ±15%-toets is een indicatie (OSRM 279 en 2.249 km, OSM-afgeleid).
- **Volume:** 9 containers/78,9 t is een steekproef t/m 2026-06-27, geen jaarcijfer.

## 8 · Bronnen
[1] ImportGenius, KSM Metals Co Ltd: 83 Gwahaksaneop 4ro Oksan-myeon, 9 containers, 78.913 kg PrNdFeB, Busan → LA/Long Beach, laatst 2026-06-27, enige importeur Noveon. https://www.importgenius.com/suppliers/ksm-metals-co-ltd
[2] ImportGenius, Noveon Magnetics: 1550 Clovis Barker Rd, KSM Metals als leverancier, havens o.a. Pusan, LA (voorbeeld). https://www.importgenius.com/importers/noveon-magnetics-inc
[3] ASM, KMP-geschiedenis: Ochang Foreign Investment Zone, exploitant KSMM, opening mei 2022, Noveon 100 t (mei 2023). https://asm-au.com/metals/korean-metals-plant/kmp-history/
[4] ASM, Energy Fuels-overname geïmplementeerd 2026-08-28. https://www.asm-au.com/
[5] Investornews, 2026-09: KMP 1,3 kt/j NdFeB-legering, 3,6 kt/j gepland; KSMM = KSM Metals = KMP. https://investornews.com/critical-minerals-rare-earths/rare-earth-metal-and-alloy-capability-outside-of-china-in-september-2026/
[6] Segye Ilbo, 2022-05-12: KSM Metals, Ochang-eup, 5.200 t/j gepland. https://www.segye.com/newsView/20220512519661
[7] Australian Manufacturing, 2021-03-10: MoU Ochang Foreign Investment Zone. https://www.australianmanufacturing.com.au/asm-to-build-its-first-metals-plant-in-south-koreas-ochang-foreign-investment-zone/
[8] OSM Nominatim, 과학산업4로, Oksan-myeon 36.70096, 127.41472. https://nominatim.openstreetmap.org/
[9] OSRM demo-router (OSM-afgeleid, indicatie), eigen meting 2026-10-30: Cheongju → Busan 279 km, Long Beach → San Marcos 2.249 km. https://router.project-osrm.org/
[10] `v2/design/routebrieven/kobalt-huayou-gunsan.md` §3 en §9: Busan-anker, zeeknoop 5621, aanloop 10,85 km.
[11] `v2/design/routebrieven/ree-yunsheng-longbeach.md` §3/§9: Long Beach-anker, zeeknoop 4488, aanloop 8,5 km.
[12] `v2/design/routebrieven/ree-larochelle-sanmarcos.md` §3: Noveon-anker.
[13] MARNET `hecht_marnet.py route`, eigen proef 2026-10-30: Busan 5621 → Long Beach 4488 = 9.879,5 km.
Satellietblik: `v2/build-cache/satcheck/sat-ree-cheongju-sanmarcos-ksm-z15.png` en `…-ksm-z16.png` (Esri, 2026-10-30).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
Bestand `v2/data/stroomroute-ree-cheongju-sanmarcos.json` (369,5 KB, versie 2, lonlat), functie `bak_ree_cheongju_sanmarcos` in `bak_stromen.sh`, profielen `ree-cheongju-sanmarcos-ksm-busan` en `ree-cheongju-sanmarcos-longbeach-sanmarcos` in `maak_stroombeen_weg.py`. Totaal 12.456,2 km, 5 benen, 4 markers, alle naden 0,000 km. Eindpunt = id (Noveon San Marcos), geen afwijking van het ontwerp.

| # | modaliteit | km gebakken | bron / norm | stippel | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 279,4 | geen wegkm; OSRM 279 (indicatie), +0,1% | nee | nieuw profiel, extract zuid-korea, 7 via-punten incl. ankers |
| b2a | zee | 10,8 | gemeten (kopie) | ja: MARNET reikt niet tot de kade (10,1 km van knoop 5621) | OMGEKEERDE LETTERLIJKE KOPIE kobalt-huayou-gunsan-aanloop-busan, eigen prefix `ree-cheongju-sanmarcos-aanloop-busan.geojson` |
| b2 | zee | 9.879,5 | MARNET-proef 9.879,5 | nee | MARNET knoop 5621 naar 4488, snaps 0,000 km |
| b3 | zee | 8,5 | gebakken 8,5 | ja: handgelegd, kade 6,47 km van knoop 4488 | LETTERLIJKE KOPIE `ree-yunsheng-longbeach-aanloop-longbeach.geojson` (knoop naar kade) |
| b4 | truck | 2.278,0 | geen wegkm; OSRM 2.249 (indicatie), +1,3% | nee | nieuw profiel, extracts us-california, us-arizona, us-new-mexico, us-texas, 8 via-punten incl. ankers |

**Markers:** alle vier op de lijn (0,000 km). Geen last-mile-benen, geen lucht/leiding/spoor.

**Recept b1.** `wegscan_puur.py` (zuid-korea, 152 s scan). Via (lon, lat) = de zes brief-punten plus beide ankers, refs 35, 1, 30, 45, venster 40 km. Segmenten 30,1 + 70,6 + 40,1 + 69,9 + 25,3 + 26,7 + 16,7 km; alle snaps 0,00-0,08 km. Eerste mijl 1,91 km, laatste mijl 0,14 km over kleine klassen.

**Recept b4.** `wegscan_puur.py` (4 extracts, ~15 min scan, venster 75 km). Segmenten 51,6 + 359,5 + 100,4 + 374,3 + 325,7 + 100,8 + 600,8 + 269,5 + 97,8 km, alle snaps <= 0,27 km, route I-10 en niet I-20.
- **Venster verruimd (⚠):** met vensterKm 40 faalde de scan met "geen wegpad tussen punt 6 en 7" (El Paso oost - Sonora): I-10 bij Van Horn/Sierra Blanca ligt 42-44 km van de rechte lijn tussen de twee via-punten. Venster naar 75 (brief §4 noemde dat als terugval), via-punten ongewijzigd. Dat kostte een tweede volledige scan (~15 min).
- Eerste mijl 0,99 km, laatste mijl 1,15 km over kleine klassen; 14 keerlussen gesnoeid (o.a. El Paso 1,71 km, Loop 1604 0,94 km).

**Toets.** Contract ok (versie 2, lonlat, modaliteiten zee en truck, elk been >= 2 punten). Geen naad > 0,000 km. `toets_rechte_benen`: geen regel voor deze stroom. `toets_knikken`: 0 terugloop; b1 heeft 3 echte scherpe bochten (173,5 en 171,2 graden bij 36.3661,128.2382, 169 graden bij 36.5621,127.4315; knooppunt 30/45 Sangju-zone resp. Jungbu 35/Gyeongbu, rijbaanomkering op een knooppunt) plus spikes van 5-30 m op kruispunten; b4 spikes op afritten bij Long Beach en San Marcos.

**Bevindingen.** (1) Bestand 369,5 KB, boven de richtlijn van ~300 KB: b4 heeft 13.744 punten (345 KB geojson). Niet herbakken, centraal noteren. (2) Geen gepubliceerde wegkm: de +-15%-toets (b1 237-321, b4 1.912-2.586) is een indicatie op OSM-afgeleide OSRM-lengtes. (3) Kop-anker onzeker (Oksan-myeon tegenover Ochang-eup), plantgebouw niet gezien; de lijn begint op het geocodeerde wegpunt 0,03 km ervan.

**Lessen.** (1) Bij een lang wegbeen met via-punten > 500 km uit elkaar op een snelweg die uitbuigt: check vooraf of de rechte lijn tussen twee via-punten binnen vensterKm van de snelweg blijft (hier El Paso-Sonora, 44 km), anders 75 meteen. De scan-cache hangt aan het venster. (2) Een omgekeerde kopie van een aanloop-geojson (kade naar zeeknoop) is een eenvoudige python-regel op `coordinates[::-1]` met eigen prefix; de naad met het zeebeen is dan 0,000 km.
