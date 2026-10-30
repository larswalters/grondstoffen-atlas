# Routebrief (licht) · kolen — Raspadskaya → Trans-Sib → Nizhny Tagil (Rusland)

**stroom-id:** `kolen-raspadskaya-ntmk` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** Kuzbass-cokeskool (concentraat) uit de Raspadskaya-wasserij bij Mezhdurechensk per spoor over het Kuzbass-net en de
Trans-Sib via Omsk, Ishim en Tyumen naar Yekaterinburg en vandaar noordwaarts naar het EVRAZ NTMK-werk in Nizhny Tagil — een Russische
binnenlandse mijn → staalfabriek-keten (Siberië → Oeral), zonder zee. Het NTMK-eindpunt is **aannemelijk: één bron** (zie §7).
**Welke as van het verhaal:** de eerste westwaartse Kuzbass-corridor en de eerste Russische binnenlandse cokeskoolas: Raspadskaya (EVRAZ, ~93 %)
is de grootste cokeskoolmijn van Rusland [1][3][10] en voedt onder meer de EVRAZ-fabriek in Nizhny Tagil [4][5]. **Jaarvolume:** Raspadskaya totaal
18,5 Mt kolen gedolven en 13,8 Mt verkocht in 2025 [5]; wasserijcapaciteit 15 Mt concentraat/j [2]; **aandeel naar NTMK niet gevonden**.
Peiljaar 2025, eenheid Mt kolen per jaar.

## 1 · Ketenkaart
```
Raspadskaya-wasserij/laadspoor `kolen-raspadskaya-laad` ──(b1 spoor · Mezhdurechensk-station → Kuzbass-net → Trans-Sib tot Omsk · 1.138,0 km)──►
Omsk (via) ──(b2 spoor · Trans-Sib · 279,8 km)──► Ishim (via) ──(b3 spoor · Trans-Sib · 287,9 km)──► Tyumen (via)
──(b4 spoor · Trans-Sib · 319,3 km)──► Yekaterinburg (via) ──(b5 spoor · noordtak · 154,4 km)──► NTMK `kolen-ntmk-aflaad` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-raspadskaya-laad` → Omsk | Mezhdurechensk-station (zuid) → Novokuznetsk-richting → Kuzbass-net → Novosibirsk-zuidelijke omleiding → Trans-Sib; **aannemelijk: één bron** (NTMK-afname) | hemelsbreed 960 km, geen spoorkm; gemeten 1.138,0 | maak_spoorbeen_raw (`rusland-siberie`) | nee |
| b2 | A | spoor | Omsk → Ishim | Trans-Sib hoofdlijn | 281 [8]; gemeten 279,8 (−0,4 %) | toets_spoorroute (`-raw`) | nee |
| b3 | A | spoor | Ishim → Tyumen | Trans-Sib hoofdlijn | 287 [8]; gemeten 287,9 (+0,3 %) | toets_spoorroute (`-raw`) | nee |
| b4 | A | spoor | Tyumen → Yekaterinburg | Trans-Sib hoofdlijn | 328 [8]; gemeten 319,3 (−2,7 %) | toets_spoorroute (`-raw`) | nee |
| b5 | A | spoor | Yekaterinburg → `kolen-ntmk-aflaad` | Yekaterinburg–Nizhny Tagil-lijn (noord) | hemelsbreed 124 km, geen spoorkm; gemeten 154,4 | toets_spoorroute (`-raw`) | nee |

Omsk → Yekaterinburg: 887,0 km tegen 896 km uit tabel [8] (km 2.712 → 1.816) = **−1,0 %**, binnen ±15 %. Totaal gemeten 2.179,4 km tegen
hemelsbreed 1.797 km (verhouding 1,21); geen gepubliceerde spoorlengte voor Mezhdurechensk → Omsk, dus daar is de toets een indicatie.
Naden 0–4 m. Alle vijf de runs 0 bochten ≥ 60° (b1: 0 omkeringen ≥ 150°).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-raspadskaya-laad` | wasserij / laadspoor | Raspadskaya-wasserij met bandverlading op het spoor, Raspadsky bij Mezhdurechensk, Kemerovo | 53.7770, 88.0990 | [2] noemt wasserij → Mezhdurechensk-station; GEM-mijnpunt [1] ligt 1,3 km NW | aannemelijk (z16 gezien: grote wasserij met kolenstapels en banden die over een spoorbundel eindigen; het mijnpunt zelf is bosrijk mijnterrein zonder spoor; router snapt op 184 m) |
| `kolen-mezhdurechensk-station` | formatiestation (overslag, route loopt erdoorheen) | station Mezhdurechensk (RZD), Kemerovo | 53.6949, 88.0316 | [6] ru-Wikipedia; [2] noemt het station | bron-gelegd (z15 gezien: breed meersporig emplacement langs de stad; lijn ligt 50 m ernaast) |
| `kolen-ntmk-aflaad` | losplek / staalfabriek | EVRAZ NTMK (Nizhny Tagil Iron and Steel Works), Tagilstroevsky-district, Sverdlovsk | 57.9304, 60.0355 | [7] OSM landuse "EVRAZ NTMK"; [9][10] eigenaar EVRAZ | bron-gelegd (z15 gezien: groot walserij-/hoogoven-/cokescomplex met stoompluimen en een spoorbundel noordelijk; lijn snapt op 130 m; de cokeskoolontvangst zelf niet aangewezen) |

## 4 · Via-punten (alleen waar een corridorkeuze bestaat; alle op de doorgaande lijn, snap ≤ 0,03 km)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1/b2 | 1 | Omsk-Passazhirsky | 54.9396, 73.3860 | pint de Trans-Sib bij Omsk; zonder via-punten kiest een vrije route Petropavlovsk/Kurgan door Kazachstan (2.162,6 km bij de haalbaarheidstoets) |
| b2/b3 | 2 | Ishim, op de hoofdlijn 3 km oost van het station | 56.1097, 69.5179 | houdt de route op de Russische hoofdlijn; het stationspunt 56.1109, 69.5114 gaf een 172°-omkering van 0,6 km (zijspoor), dit punt 0 |
| b3/b4 | 3 | Tyumen | 57.1450, 65.5225 | pint de Tyumen-doorgang (geen Kazachse tak) |
| b4/b5 | 4 | Yekaterinburg-Passazhirsky | 56.8596, 60.6049 | pint de Trans-Sib-aankomst vóór de afslag noordwaarts naar Nizhny Tagil |

**Afwijking van het ontwerp:** het ontworpen via-punt Novosibirsk (55.0288, 82.9227) is bewust weggelaten. Een route via dat punt kost ~23 km
extra (1.145 tegen 1.122 km tot Omsk) met een 170°-omkering op het stationsknooppunt; de vrije route passeert Novosibirsk 8,2 km zuidelijker
over de omleiding, 0 bochten. Er bestaat daar geen corridorkeuze (alle Kazachse sluipwegen liggen ten westen van Omsk).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Raspadskaya-wasserij | Raspadskaya Coal Company (EVRAZ 82–93 %) | ruwe kool → cokesconcentraat | 15 Mt concentraat/j (3 circuits); 2019 negen maanden 10,1 Mt ruw → 6,2 Mt concentraat | [2][10] |
| EVRAZ NTMK | EVRAZ | cokeskool → cokes → ruwijzer/staal (rails, wielen) | niet gevonden | [7][9] |

## 6 · Stoppunt
De brief stopt op het NTMK-terrein: de cokeskoolontvangst binnen het werk is niet aangewezen, en geen bron noemt een volgende locatie van de
lading. Fase D (cokesbatterij → hoogoven) en E vervallen: één terrein, geen openbaar net.

## 7 · Open punten
- **Afname NTMK is aannemelijk, niet bevestigd voor 2024–26:** Fastmarkets (14-05-2010) noemt NTMK sterk afhankelijk van Raspadskaya [4]; GEM noemt NTMK
  naast NLMK en MMK als afnemer [1]; Kommersant (2026) noemt alleen "EVRAZ-ondernemingen" zonder fabriek of volume [5]. Geen leveringsvolume gevonden.
- **Kuzbass-corridor aannemelijk, niet bevestigd:** het pad (Mezhdurechensk → Novokuznetsk-richting → Belovo → Novosibirsk-omleiding) is het kortste
  OSM-pad; er is geen bron voor de railtraversal.
- **Wasserij-coördinaat afgeleid:** geen bron geeft de laadplek; positie uit de satelliet (wasserij + bandverlading op het spoor, 1,3 km van het GEM-mijnpunt).
- **Treinen vormen bij Mezhdurechensk-station** (bron [2]): de route gaat er niet apart langs, het station ligt ~9 km zuidelijk van de wasserij op de lijn.
- **Geen spoorkm gepubliceerd** voor b1 en b5; Omsk → Yekaterinburg wel (tabel [8]).
- **Recente volumes sancties/vervoersquota niet gecontroleerd;** wasserijcijfers 2019 zijn ouder dan het peiljaar.
- **GEM-mijnpunt** 53.7841, 88.0824 (en Wikipedia 53.7836, 88.0828) ligt in bos 1,3 km van de lijn: niet als anker gebruikt (mijn is ondergronds, banden naar de wasserij).

## 8 · Bronnen
[1] Global Energy Monitor, Raspadskaya coal mining complex — 53.784142, 88.082391; EVRAZ 82 %; leveringen aan NLMK, MMK, NTMK. https://www.gem.wiki/Raspadskaya_coal_mining_complex
[2] NS Energy, Raspadskaya Coal Mine (30-01-2020) — wasserij 15 Mt concentraat/j; Tomusinsk Handling → station Mezhdurechensk; 12,7 Mt (2018); 9M 2019 10,1/6,2 Mt. https://www.nsenergybusiness.com/?p=245365
[3] AIST, EVRAZ takes indirect controlling interest in Raspadskaya (2012) — EVRAZ grootste klant, 82 %. https://www.aist.org/evraz-takes-indirect-controlling-interest-in-coking-coal-producer
[4] Fastmarkets, "Concern mounts after Raspadskaya blast" (14-05-2010) — NTMK sterk afhankelijk van Raspadskaya. https://fastmarkets.com/?p=13340
[5] Kommersant, Raspadskaya 2025 (02-03-2026) — 18,5 Mt productie, 13,8 Mt verkoop (+7 %), groei Azië en EVRAZ-ondernemingen. https://www.kommersant.ru/doc/8478278
[6] Wikipedia (ru, MediaWiki API `prop=coordinates`), станция Междуреченск — 53.694889, 88.031639. https://ru.wikipedia.org/wiki/Междуреченск_(станция)
[7] OpenStreetMap-bijdragers via Nominatim — landuse industrial "АО «ЕВРАЗ НТМК»" 57.9304368, 60.0355420 (ODbL). https://www.openstreetmap.org/copyright
[8] Wikipedia, Trans-Siberian Railway, routetabel — km vanaf Moskou: Yekaterinburg 1.816 · Tyumen 2.144 · Ishim 2.431 · Omsk 2.712 · Novosibirsk 3.335. https://en.wikipedia.org/wiki/Trans-Siberian_Railway
[9] Wikipedia, Nizhny Tagil — Yekaterinburg 130 km (hemelsbreed) zuidwaarts; EVRAZ-eigendom van NTMK. https://en.wikipedia.org/wiki/Nizhny_Tagil
[10] Wikipedia, Raspadskaya (company) — EVRAZ 82 %, groepsstructuur met wasserij en Tomusinskoye Cargo Handling. https://en.wikipedia.org/wiki/Raspadskaya_(company)
[11] Wikipedia, Raspadskaya coal mine (MediaWiki API) — 53.78361, 88.08278. https://en.wikipedia.org/wiki/Raspadskaya_coal_mine
[12] Eigen metingen `maak_spoorbeen_raw.py` (rusland-siberie) en `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`), uitvoer `v2/build-cache/ais/graaf/kolen-raspadskaya-ntmk-spoor-raspadskaya-omsk.geojson` en `spoorroute-kolen-raspadskaya-ntmk-{omsk-ishim,ishim-tyumen,tyumen-yekaterinburg,yekaterinburg-ntmk}.geojson`.
[13] Esri World Imagery via `sat_check.py` — `v2/build-cache/satcheck/sat-kolen-raspadskaya-ntmk-{raspadskaya-mijn,raspadskaya-laadstation,mezhdurechensk-station,ntmk}.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Recept:** `bash v2/tools/bak_stromen.sh kolen-raspadskaya-ntmk` (functie `bak_kolen_raspadskaya_ntmk`) over vooraf gebakken lijnen: b1 `maak_spoorbeen_raw.py --extract rusland-siberie`
(ruwe OSM-ways), b2–b5 `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs`; geen profiel in `maak_stroombeen_weg.py`, geen zee, stippel, haven-aanloop, kopie, lucht of leiding.
Uitvoer `v2/data/stroomroute-kolen-raspadskaya-ntmk.json` (166,6 KB, versie 2, lonlat, 8.732 punten).

| # | modaliteit | been | km (gebakken) | km (brief) | afwijking | stippel |
|---|---|---|---|---|---|---|
| b1 | spoor | Raspadskaya-laadspoor → Omsk (Kuzbass-net, Novosibirsk-omleiding, Trans-Sib) | 1.138,0 | 1.138,0 (hemelsbreed 960, geen spoorkm) | indicatie | nee |
| b2 | spoor | Omsk → Ishim | 281,3 | 281 (Wikipedia-tabel) | +0,1 % | nee |
| b3 | spoor | Ishim → Tyumen | 289,5 | 287 | +0,9 % | nee |
| b4 | spoor | Tyumen → Yekaterinburg | 323,5 | 328 | −1,4 % | nee |
| b5 | spoor | Yekaterinburg → EVRAZ NTMK | 158,4 | 154,4 (hemelsbreed 124, geen spoorkm) | indicatie | nee |

Totaal 2.190,7 km, 5 benen, 0 stippel. Omsk → Yekaterinburg 894,3 km tegen 896 km (tabel [8]) = −0,2 %. De bake telt km over de punten (haversine), de routerkm in de kop van §2 liggen tot 1,3 % lager.
**Naden** 0,000–0,004 km (max 4 m). **Markers (3)** — Raspadskaya-laad 0,18 km van de lijn, Mezhdurechensk-station 0,05 km, NTMK 0,13 km: alle ≤ 0,5 km.
**Toetsen:** `toets_knikken.py` 0 knikken ≥ 60° en 0 omkeringen ≥ 150°; `toets_rechte_benen.py --min-km 5` meldt geen been van deze stroom; json.load goed, versie 2, punt_formaat lonlat, alleen modaliteit `spoor`, elk been ≥ 239 punten, 166,6 KB.
**Toelichting:** geen stippel, geen haven-aanloop, geen vlucht, geen leiding. Het NTMK-eindpunt (Nizhny Tagil) komt overeen met het stroom-id; geen afwijking van het ontwerp in het eindpunt.
**Lessen:** (1) b1 over ruwe OSM-ways zonder bladsnoei gaf 0 omkeringen; (2) het ontworpen via-punt Novosibirsk bleef weg (+23 km, 170°-omkering); (3) het Ishim-via-punt 3 km oost van het station i.p.v. het stationspunt (172°-omkering van een zijspoor);
(4) b1 en b5 hebben geen gepubliceerde spoorkm, de ±15 %-toets is daar een indicatie; (5) wasserij-anker afgeleid uit de satelliet (aannemelijk), NTMK-afname aannemelijk (één bron, niet bevestigd 2024–26).
