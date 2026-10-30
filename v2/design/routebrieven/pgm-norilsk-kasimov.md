# Routebrief (licht) · PGM — Norilsk → Sheremetyevo (SVO) → Prioksky-raffinaderij, Kasimov (Rusland)

**stroom-id:** `pgm-norilsk-kasimov` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** PGM-concentraat van de Nadezhda-smelter (Nornickel Polar Division, Norilsk) per **spoor** over het
geïsoleerde Norilsk-industrienet naar het vrachtplatform van Alykel (NSK), per **vrachtvlucht** (grootcirkel, aannemelijk)
naar Sheremetyevo-Cargo (SVO) en per **truck** via MKAD en het Egorjevskoje shosse (ex-R105) naar de Prioksky-raffinaderij (AO PZCM)
in Kasimov — toll-raffinage tot Pt/Pd-baar **(stoppunt)**.
**Welke as van het verhaal:** de tweede toll-raffinaderij van Nornickel, in Midden-Rusland (nieuwe regio). Groep Nornickel 2024:
Pd ≈ 2,75–2,8 Moz + Pt 667 koz ≈ **106–108 t 2E/jaar** (koz ÷ 32,15; eenheid 2E = Pt+Pd) [6] — **bovengrens**: de verdeling over
Krastsvetmet, Prioksky en Uralintekh is niet gepubliceerd [1][2]. Ter schaal: PZCM raffineerde in 2009 in totaal 0,4 t Pt + 0,5 t Pd
(en 30 t goud, 117 t zilver) [3] — het werkelijke aandeel is dus waarschijnlijk een fractie.

## 1 · Ketenkaart
```
Nadezhda-smelter `pgm-nadezhda-fabriek` ──(b1 spoor · Norilsk Railway, geïsoleerd net · 27,3 km + 6,2 km stippel — KOPIE)──►
Alykel-vrachtplatform `pgm-alykel-vrachtterminal` (NSK)
  ──(b2 lucht · vlucht NSK → SVO, grootcirkel, aannemelijk · 2.834,4 km)──►
Sheremetyevo-Cargo `pgm-svo-cargo` (SVO) ──(b3 truck · MKAD → Egorjevskoje shosse → R124 · hemelsbreed 274 km, geen wegkm)──►
Prioksky-raffinaderij `pgm-prioksky-raffinaderij`, Kasimov ── stoppunt (Pt/Pd-baren, Good Delivery)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Nadezhda → Alykel | Norilsk Railway; **letterlijke kopie** van `pgm-norilsk-krasnojarsk` b1 | 27,3 gemeten [8] | kopie geojson (zie §9-aanwijzing) | nee |
| b1b | A | spoor | laatste net → Alykel-platform | **letterlijke kopie** van de stippel in `pgm-norilsk-krasnojarsk` | 6,2 [8] | kopie `--stippel` | **ja** — net reikt niet tot het platform |
| b2 | B | lucht | Alykel (NSK) → SVO | vlucht NSK → SVO (vrachtvlucht, grootcirkel); **aannemelijk: één bron** (Norilsk bereikbaar per Jenisej, NZR en lucht [1]; geen weg/doorgaand spoor) | 2.834,4 grootcirkel (berekend) | `maak_luchtbeen.py` (klaar) | nee — doorgetrokken |
| b3a | C | truck | SVO-Cargo → openbare weg | airside last mile (platform privéterrein) | 0,28 | `--stippel` | **ja** — airside |
| b3 | C | truck | openbare weg bij SVO → Prioksky | MKAD (noord → zuidoost) → Egorjevskoje shosse (Ljoebertsy, Egorjevsk-ontwijking, Spas-Klepiki–Toema = R132) → R125/R124 over de Oka bij Kasimov [5] | **hemelsbreed 274 km, geen wegkm**; ref. Moskou–Kasimov 263 km [3]; eigen OSM-graafmeting ≈ 320–326 km (indicatie, geen norm) [10] | `maak_stroombeen_weg` via `wegscan_puur.py` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-nadezhda-fabriek` | smelter (kop spoor) | Nadezhda Metallurgical Plant, Norilsk | 69.3275, 87.9521 | **hergebruikt**: `pgm-norilsk-krasnojarsk.md` [1][12] | bron-gelegd (daar z15 gezien: complex met rookpluim, spoorbundel W) — niet opnieuw gelegd |
| `pgm-alykel-vrachtterminal` | vrachtplatform (kop lucht) | Alykel Airport (NSK) | 69.3252, 87.3290 | **hergebruikt**: `pgm-norilsk-krasnojarsk.md` [12] | **onzeker** (geen apart vrachtplatform te onderscheiden; Alykel is eigendom van Nornickel [8]) |
| `pgm-svo-cargo` | vrachtterminal (losplek lucht) | Sheremetyevo-Cargo, Moskou | 55.9696, 37.4362 | **hergebruikt** `dia-svo-cargo`: `diamant-lomonosov-moskou.md` / `diamant-mirny-mumbai.md` [12] | bron-gelegd; hier opnieuw gezien (z15): vrachthal met platform ten zuiden van de banen, openbare weg ~0,3 km ZO |
| `pgm-prioksky-raffinaderij` | raffinaderij (losplek) | Prioksky Plant of Non-Ferrous Metals (AO PZCM), mkr. Prioksky, Kasimov | 54.9099, 41.3579 | [3][4][9]; OSM landuse industrial "Prioksky Plant" (haalbaarheidstoets) | bron-gelegd (z14+z16 gezien: twee omheinde terreinen met lange hallen en tanks in bos, 4,5 km ZW van Kasimov-centrum 54.9397, 41.3952, N–S-weg langs de westrand; woonwijk Prioksky 1,5 km NNW sluit aan bij [4]) |

## 4 · Via-punten (b3, reisvolgorde, lat, lon, vertices OP de doorgaande weg, snap ≤ 0,01 km behalve #5)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 0 | openbare weg bij SVO-Cargo (46Н-13926) | 55.9679, 37.4395 | eerste openbare weg; einde airside-stippel (geen via, begin van het been) |
| b3 | 1 | MKAD noord | 55.9076, 37.5973 | kiest de MKAD i.p.v. de kortste lijn dwars door Moskou-centrum (31 km, niet voor vracht) of de A-107 |
| b3 | 2 | MKAD zuidoost, afslag Ljoebertsy | 55.7047, 37.8331 | verlaat de MKAD waar het Egorjevskoje shosse (Oktjabrski prospekt) begint |
| b3 | 3 | Egorjevskoje shosse bij Malakhovka | 55.6606, 37.9715 | pint dit shosse en sluit de M5/Novoryazanskoje uit |
| b3 | 4 | Egorjevsk-ontwijking (R105) | 55.3880, 39.0822 | de ontwijking (sinds jaren 80), niet door Egorjevsk-stad [5] |
| b3 | 5 | R132 tussen Spas-Klepiki en Toema | 55.1417, 40.3473 | pint de Klepikovskaja-corridor (R132-deel is R105-route [5]); snap 0,9 km van mijn kandidaat, vertex gebruikt |
| b3 | 6 | R105/61К-001 vóór de Oka-brug | 54.9730, 41.3215 | pint de oversteek bij Kasimov, vóór het knooppunt met de R125 |
| b3 | 7 | R124 bij Kasimov | 54.9183, 41.3525 | laatste stuk naar Prioksky, buiten het stadscentrum (54.9397, 41.3952) |

Alternatief (niet gekozen, niet gemeten): M7 → Vladimir → Gus-Khrustalny → Moeroem → R125; veel langer en niet de bronroute. De ontwerp-corridor "R125 Ryazan–Kasimov" bestaat niet [5].

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nadezhda-smelter, Norilsk | Nornickel Polar Division | concentraat → matte/PGM-concentraat (de PGM-concentraatwerkplaats zit volgens [1] bij Nadezhda én de Kopersmelter) | groepscijfer 2E ≈ 106–108 t/j | [1][6] |
| Prioksky Plant (AO PZCM), Kasimov | staat (PZCM) | PGM-concentraat (toll, Nornickel) → Pt/Pd-baren; vooral goud/zilver-affinage | Au 30 t, Ag 117 t, Pt 0,4 t, Pd 0,5 t (2009) | [2][3][7] |

## 6 · Stoppunt
Prioksky: één bron noemt Prioksky als toll-raffinaderij van Nornickel-PGM [1][2]; geen bron noemt een volgende, benoemde afnemer. Fase D/E vervallen.

## 7 · Open punten
- **Vervoerswijze Norilsk → Moskou ongebrond:** [1] noemt alleen Jenisej, NZR en lucht voor Norilsk; een directe vlucht NSK → SVO is een aanname (isolatie). Aannemelijk, in de beennaam.
- **Aandeel Prioksky onbekend:** het groepscijfer is een bovengrens; PZCM is vooral een goud/zilver-affinaderij (2009: 0,9 t Pt+Pd) [3].
- **PGM-concentraatplant:** [1] noemt Nadezhda én het Kopersmelter; Nadezhda-anker is hergebruik, de Koperfabriek is niet gelegd. Een zoekresultaat meldt dat Nornickel kopersliem-verwerking naar Montsjegorsk verplaatst (juli 2026, alleen snippet) [9] — niet geverifieerd.
- **Sanctiecontext:** LPPM schorste Krastsvetmet en PZCM in 2022 (Good Delivery) [7] — raakt de afzet, niet de fysieke route.
- **Wegkm niet gebrond:** 263 km Moskou–Kasimov (Wikipedia) is vanaf het centrum; OSRM 358 uit de toets is onbetrouwbaar (kan door Moskou). Geen gepubliceerdKm invullen (`None`), meting 320–326 km is een indicatie.
- **Jaarverslag 2025** (haalbaarheidstoets: Krasnoyarsk Transport Division, Pd 2.725 + Pt 667 koz) kon ik niet openen (PDF > 10 MB); 667 koz Pt vond ik als 2024-cijfer [6].
- **Alykel-vrachtplatform onzeker** (zie §3); b1b-stippel 6,2 km komt uit de gekopieerde stroom.

## 8 · Bronnen
[1] Nornickel, Norilsk Division (toll-raffinage bij Krastsvetmet, Uralintekh, Prioksky; Jenisej/NSR/lucht; Nadezhda + Kopersmelter). https://nornickel.ru/business/assets/norilsk-division/
[2] Reuters via Yahoo Finance, Nornickel/Bahrein (PGM-concentraat toll-geraffineerd bij Krastsvetmet, Prioksky, Uralintekh). https://finance.yahoo.com/news/russia-nornickel-build-platinum-group-135712119.html
[3] ru.wikipedia, Касимов (PZCM sinds 1991, affinage 2009, R105 Moskou–Kasimov 263 km, 262 km). https://ru.wikipedia.org/wiki/Касимов
[4] ru.wikipedia, Приокский (Касимов) (mkr. Prioksky, rechteroever Oka, ketelhuis 1,5 km). https://ru.wikipedia.org/wiki/Приокский_(Касимов)
[5] ru.wikipedia, Егорьевское шоссе (Moskou–Kasimov, Egorjevsk-ontwijking, R132, R125 bij Kasimov). https://ru.wikipedia.org/wiki/Егорьевское_шоссе
[6] metals-wire, Nornickel 2024/H1-2025 (Pt 667 koz 2024, Pd bijna 2,8 Moz, guidance 2025). https://metals-wire.net/regions/russia-cis/nornickel-cuts-2025-production-guidance-after-first-half-output-declines
[7] ibprom.ru, Приокский завод цветных металлов (Good Delivery Au/Ag/Pt/Pd; zoekfragment, niet geopend) https://ibprom.ru/priokskiy-zavod-cvetnyh-metallov · gmk.center, LPPM-schorsing 2022 (fragment) https://gmk.center/news/londonskij-rynok-platiny-i-palladiya-zablokiroval-rossijskie-zavody/amp/
[8] Novaya Gazeta 2020, Alykel is eigendom van Nornickel (fragment). https://novayagazeta.ru/amp/articles/2020/06/27/86041-aeroport-eto-tozhe-nornikel
[9] AK&M, Nornickel consolideert edelmetaalproductie in Montsjegorsk (fragment, niet geopend). https://www.akm.ru/news/nornikel_konsolidiruet_proizvodstvo_dragmetallov_v_monchegorske/
[10] Eigen meting: Geofabrik `rusland-centraal` (pure-Python pbf-scan, primary+ ways, kortste pad met via-punten) — 317–326 km; indicatie.
[11] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-pgm-norilsk-kasimov-prioksky-z14.png`, `-prioksky-z16.png`, `-svo-z15.png`.
[12] Eigen brieven: `pgm-norilsk-krasnojarsk.md` (Nadezhda, Alykel, b1+stippel), `diamant-lomonosov-moskou.md` (dia-svo-cargo), `goud-loulo-ticino.md` (airside-patroon).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

Bestand `v2/data/stroomroute-pgm-norilsk-kasimov.json` (87,2 KB, contract versie 2, lonlat): 5 benen, **3.189,3 km**, 4 markers.
Recept: `bash v2/tools/bak_stromen.sh pgm-norilsk-kasimov` (functie `bak_pgm_norilsk_kasimov`); wegprofiel `pgm-norilsk-kasimov-svo-prioksky`
in `maak_stroombeen_weg.py`, gescand met `wegscan_puur.py` (extract rusland-centraal, 310 s).

| # | modaliteit | km | naad | stippel | been |
|---|---|---|---|---|---|
| 1 | spoor | 27,3 | 0 | nee | Nadezhda → Alykel, **letterlijke kopie** van pgm-norilsk-krasnojarsk (geojson `spoorroute-pgm-norilsk-krasnojarsk-nadezhda-alykel`) |
| 2 | spoor | 6,2 | 0 | **ja** | laatste zijspoor naar het Alykel-vrachtplatform, **letterlijke kopie** van de stippel van pgm-norilsk-krasnojarsk |
| 3 | lucht | 2.834,4 | 0 | nee | vlucht NSK → SVO, grootcirkel, 115 punten, "aannemelijk: één bron" in de beennaam, doorgetrokken |
| 4 | truck | 0,3 | 0 | **ja** | SVO-Cargo airside last mile naar de openbare weg 46N-13926 (55.9696,37.4362 → 55.9679,37.4395) |
| 5 | truck | 321,1 | 0 | nee | SVO → Prioksky via MKAD, Egorjevskoje shosse, R132, R124 (4.201 punten) |

**Markers (4):** `pgm-nadezhda-fabriek`, `pgm-alykel-vrachtterminal`, `pgm-svo-cargo`, `pgm-prioksky-raffinaderij`. Afstand tot de lijn: Alykel,
SVO en Prioksky 0,0 km; Nadezhda **0,73 km** (het gekopieerde spoorbeen begint op 69.3312,87.9367, de smelter-marker is hergebruikt; > 0,5 km, bevinding, niet bijgeschoven).

**Toelichting**
- **Stippel b1b (spoor, 6,2 km):** het net reikt niet tot het platform; Alykel-anker blijft onzeker (§3). Gekopieerd, niet opnieuw gemeten.
- **Vlucht (b2):** doorgetrokken grootcirkel tussen twee vrachtplatforms; de wijze NSK → SVO is een aanname uit de isolatie van Norilsk, één bron (§7).
- **Stippel b3a (airside, 0,28 km):** SVO-Cargo ligt op privéterrein; de weg begint op de eerste openbare weg. Patroon bak_goud_loulo_ticino.
- **Weg:** geen gepubliceerde wegkm. 321,1 km ligt in de eigen meting van 320-326 km (indicatie, geen ±15%-norm); ter vergelijking Moskou-Kasimov 263 km vanaf het centrum
  en hemelsbreed 274 km. Segmenten (km): 17,5 · 32,1 · 11,8 · 83,0 · 98,8 · 69,2 · 8,1 · 1,0; alle via-snaps ≤ 0,01 km behalve het eindanker (0,15 km, weg → kade). Geen omweg-segment.
- **Geen zee, geen haven-aanloop, geen leiding.** Naden: alle 0,00 km (maximaal 0 km).
- **Toetsen:** `toets_knikken.py` 12 knikken ≥ 60 graden, 1 omkering (170,7 graden bij 55.8816,37.7269, op de MKAD, terugloop 0); `toets_rechte_benen.py`: alleen de bekende spoorstippel van 6,2 km.
- **Id en eindpunt:** het id belooft Kasimov en de lijn eindigt in Kasimov (Prioksky-raffinaderij); geen afwijking.

**Lessen:** (1) de bak-agent hoefde geen via-punt te verplaatsen: de zeven via-punten uit §4 snapten allemaal op de doorgaande weg. (2) Een wegscan op rusland-centraal kost ~310 s
en 60.171 ways in het venster; het resultaat is gecached. (3) Een gekopieerd spoorbeen erft de 0,73 km-afstand tussen smelter-marker en spoorbegin; markers van een gedeeld been horen bij het kopiëren
dezelfde conventie te houden als de bronstroom.
