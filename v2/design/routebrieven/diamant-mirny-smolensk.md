# Routebrief (licht) · diamant — Mirny → Moskou → Smolensk (Rusland)

**stroom-id:** `diamant-mirny-smolensk` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** Ruwe diamant uit het Mir-cluster (Alrosa, Jakoetië) gaat per truck van mijn/sorteercentrum naar Mirny Airport (MJZ), vliegt als vrachtvlucht (grootcirkel) naar Sheremetyevo-Cargo (SVO, Moskou) en gaat per truck via de MKAD en de M-1 (E30) naar Kristall (Alrosa) in Smolensk, de eigen slijperij — de binnenlandse, sanctie-beladen beneficiation (aannemelijk: één bron voor de levering).
**Welke as van het verhaal:** *Alrosa-ruw naar de eigen Russische slijperij.* Kristall verwerkt ruim 200.000 ct ruw per jaar, >90% van de Alrosa-aanvoer [3]; Alrosa nam het in 2019 over [1][3] en OFAC zette het op 23 aug 2024 op de SDN-lijst [2]. Volume **0,2 Mct/j** (Kristall-totaal, peiljaar 2019/2024; het Mirny-aandeel is niet uitgesplitst). Waarde per karaat: gepolijst, hoog. Alrosa totaal ca. 35 Mct/j (KPCS, `design/diamant.md`).

## BINDENDE aanpassing (haalbaarheidstoets)
b1 en b2 zijn LETTERLIJKE KOPIEËN van `diamant-mirny-mumbai` (naad SVO 0 km). Nieuw is alleen het wegbeen SVO → Kristall via MKAD en M-1, extract `rusland-centraal`, vensterKm 75, via-punten alleen op ring en M-1. Aannemelijk, niet bron-gelegd: geen bron noemt de SVO-overslag. De ±15%-toets is indicatie (geen wegkm gepubliceerd).

## 1 · Ketenkaart
```
Alrosa Mir-mijn/sorteercentrum, Mirny `dia-mirny-mijn` ──(b1 truck · stadsweg Mirny · 3,6 km, KOPIE)──►
Mirny Airport (MJZ) `dia-mirny-mjz` ──(b2 lucht · vlucht MJZ → SVO, grootcirkel · 4.150,4 km, KOPIE)──►
Sheremetyevo-Cargo (SVO) `dia-svo-cargo` ──(b3 truck · MKAD → M-1/E30 · 411,7 km gemeten, aannemelijk)──►
Kristall (Alrosa), Smolensk `dia-smolensk-kristall` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Mir-mijn → Mirny Airport (MJZ) | stadsweg Mirny (geen corridorkeuze); LETTERLIJKE KOPIE `diamant-mirny-mumbai` b1 | 3,6 getekend, hemelsbreed ~2,2, geen wegkm | kopie geojson `diamant-mirny-mumbai-weg-mijn-mjz` | nee |
| b2 | B | lucht | MJZ → Sheremetyevo-Cargo (SVO) | vlucht MJZ → SVO (vrachtvlucht, grootcirkel); LETTERLIJKE KOPIE `diamant-mirny-mumbai` b2 | 4.150,4 (berekend, grootcirkel) | kopie geojson `diamant-mirny-mumbai-lucht-mjz-svo` | nee — doorgetrokken |
| b3 | D | truck | SVO-Cargo → Kristall, Smolensk | MKAD (NW-boog) → M-1/E30 via Vjazma-rondweg, Safonovo, Jartsevo → Smolensk-noord → stadswegen; aannemelijk: één bron | hemelsbreed 362 km, geen wegkm; gemeten 411,7 [9] (indicatie ca. 400) | maak_stroombeen_weg (nieuw profiel) | nee |

Fase C vervalt (geen overslag buiten de lucht-truck-wissel in SVO); E vervalt. Kristall slijpt zelf en levert gepolijst/juwelen uit (geen bron voor een vervolgbeen).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-mirny-mijn` | mijn / laadplek | Mir-mijn / Alrosa-complex, Mirny (**hergebruikt**) | 62.5258, 113.9842 | `diamant-mirny-mumbai.md` [6] | bron-gelegd (overgenomen, niet opnieuw gelegd) |
| `dia-mirny-mjz` | vrachtterminal / vertrek | Mirny Airport (MJZ) (**hergebruikt**) | 62.5344, 114.0222 | [6] | bron-gelegd (overgenomen) |
| `dia-svo-cargo` | vrachtterminal / overslag lucht → truck | Sheremetyevo-Cargo, Moskou (**hergebruikt**) | 55.9696, 37.4362 | [6] | bron-gelegd (overgenomen); wegnet op 0,19 km (OSM-service-wegen), geen airside-stippel nodig |
| `dia-smolensk-kristall` | slijperij / bestemming | Kristall (Alrosa), ul. Shkadova, Smolensk | 54.7731, 32.0989 | [1][7][8] | bron-gelegd (z15 gezien: groot industrieel dakcomplex op het punt, in een industriezone ten zuidoosten van het centrum; `diamant-mirny-smolensk-kristall`). Levering aannemelijk |

## 4 · Via-punten (b3, reisvolgorde, alle vertices OP de ring of de M-1, snap 0–0,01 km [9])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | MKAD NW-boog (tussen afrit 67B en 62/63A) | 55.8040, 37.3858 | de ring i.p.v. een route dwars door Moskou (MKAD, ontwerp: "MKAD of A107") |
| b3 | 2 | M-1/MKAD-knoop West-Moskou (begin M-1) | 55.7304, 37.3662 | waar de ring op de M-1 aansluit |
| b3 | 3 | M-1 Vjazma-rondweg | 55.2431, 34.3129 | M-1 loopt ~3,7 km ten noorden van Vjazma [5] i.p.v. door de stad |
| b3 | 4 | M-1 bij Safonovo | 55.1422, 33.2573 | ~4 km ten noorden van Safonovo; Dorogobuzj ligt ~25 km ten zuiden en niet aan de M-1 (ontwerp noemde het wel) |
| b3 | 5 | M-1 bij Jartsevo | 55.0797, 32.7089 | ~2 km van Jartsevo [5] |
| b3 | 6 | M-1 Smolensk-noord (A-132-knoop) | 54.8779, 32.0513 | afslag van de M-1 naar de stad, niet via het centrum |

Segmenten (km): SVO → punt 1 21,2 · → 2 8,8 · → 3 211,3 · → 4 69,4 · → 5 35,7 · → 6 50,0 · → Kristall 15,4 (som 411,8). Gemeten route volgt М-1 over 30–396 km; zonder via-punten gaf de scan dezelfde 411,7 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kristall, Smolensk | Alrosa (100% sinds 2019; SDN sinds 23-08-2024) | ruw → geslepen | >200.000 ct ruw/j | [1][2][3] |

## 6 · Stoppunt
De brief stopt bij Kristall: de slijperij is de gedocumenteerde afnemer van Alrosa-ruw in Rusland en geen bron noemt een afzetbeen van het geslepen product (fase E vervalt).

## 7 · Open punten
- **Geen bron voor de route**: de AFP zegt dat sommige Mirny-stenen per vlucht naar slijpcentra in Moskou en Smolensk gaan [4]; de SVO-overslag en de truck Moskou → Smolensk zijn aanname (een rechtstreekse vlucht naar Smolensk-Severny is niet uitgesloten).
- **Wegkm niet gebrond**: alleen hemelsbreed 362 km; M-1 is 440 km Moskou–Wit-Russische grens [5], geen SVO-Smolensk-lengte.
- **Mirny-aandeel** in Kristalls 0,2 Mct/j niet uitgesplitst; peil is 2019 (>90% Alrosa [3]) en 2024 (>200.000 ct [2]).
- **Kristall ontbreekt in de sitelaag** (centraal toevoegen); de OFAC-lijst (2024) geeft weinig zendingsdata.
- De eerste 0,3 km vanaf het SVO-anker loopt over OSM-service-wegen (snap 0,19 km): precieze poort van het vrachtplatform niet gezien.

## 8 · Bronnen
[1] ru.wikipedia — Кристалл (предприятие, Смоленск): Alrosa 100%, sinds 2019, ul. Shkadova, 54°46′23″N 32°05′56″E. https://ru.wikipedia.org/wiki/Кристалл_(предприятие,_Смоленск)
[2] Rapaport, 2024-08-28 — "US adds Alrosa-owned manufacturer Kristall to sanctions list": >200.000 ct ruw/j, OFAC 23 aug 2024. https://rapaport.com/news/us-adds-alrosa-owned-manufacturer-kristall-to-sanctions-list/
[3] Interfax, 2019-09-19 — Medvedev geeft Alrosa toestemming Kristall te kopen: >200.000 ct/j, >90% van Alrosa. https://www.interfax.ru/business/677056
[4] AFP via Arab News, 2019-07-08 — "Russia digs for diamonds to ensure supremacy in global market" (Mirny-sorteercentrum; "flown to polishing centers in Moscow and Smolensk"). https://www.arabnews.com/business/russia-digs-for-diamonds-to-ensure-supremacy-in-global-market-1522276
[5] en.wikipedia — "M1 highway (Russia)": 440 km, ten noorden van Vjazma, via Safonovo en Jartsevo. https://en.wikipedia.org/wiki/M1_highway_(Russia)
[6] `v2/design/routebrieven/diamant-mirny-mumbai.md` (b1, b2 en de ankers mijn, MJZ, SVO-Cargo).
[7] OpenStreetMap Nominatim: ul. Shkadova, Smolensk op 54.7737, 32.0987 (~50 m van het anker). https://nominatim.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-diamant-mirny-smolensk-kristall.png`.
[9] OSM (ODbL), Geofabrik `rusland-centraal`, eigen PBF-scan (`wegscan_puur.py`, profiel `diamant-mirny-smolensk-svo-kristall`); stadscoördinaten Vjazma/Safonovo/Jartsevo via Photon (komoot). https://download.geofabrik.de/russia/central-fed-district.html

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)

**Stroom:** `diamant-mirny-smolensk` · **bestand:** `v2/data/stroomroute-diamant-mirny-smolensk.json` (60,7 KB) ·
**recept:** `bak_diamant_mirny_smolensk()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh diamant-mirny-smolensk`).

**3 benen · 4.566,0 km · 3.062 punten · 4 markers** — alle benen DOORGETROKKEN, geen stippel, geen zee/haven-aanloop/leiding/spoor.

| # | fase | modaliteit | km | brief | naad met vorig been | stippel? |
|---|---|---|---|---|---|---|
| b1 | A | truck | 3,6 | geen wegkm; 3,6 getekend (KOPIE mirny-mumbai b1) | — (start) | nee |
| b2 | B | lucht | 4.150,4 | 4.150,4 berekend (KOPIE mirny-mumbai b2) | 0,000 km | nee (grootcirkel in de beennaam) |
| b3 | D | truck | 412,0 | geen wegkm; hemelsbreed 362 km (indicatie ~400) | 0,000 km | nee |

**Recept:** b1 en b2 zijn byte-gelijke kopieen van de geojsons van `diamant-mirny-mumbai` (punten identiek aan het bestaande stroombestand). b3 is het
profiel `diamant-mirny-smolensk-svo-kristall` in `maak_stroombeen_weg.py` (extract `rusland-centraal`, vensterKm 75, `wegscan_puur.py`, geojson
`diamant-mirny-smolensk-weg-svo-kristall.geojson`), met 6 via-punten op ring en M-1 (snap <= 5 m): MKAD NW-boog (km 21), M-1/MKAD-knoop (km 30),
Vjazma-rondweg (km 241), Safonovo (km 311), Jartsevo (km 347), Smolensk-noord (km 397), Kristall (km 412). Geen segment met omweg.

**Toets:** naden 0,000 km (max 0); alle 4 markers 0,0 km van hun lijn; modaliteiten {truck, lucht}; versie 2, punt_formaat lonlat; geen
rechte benen > 5 km. Knikken: 39 (b1 8, b3 31), 0 terugloop; de ene omkering (155,6 gr, b1, Mirny) is een echte bocht in het gekopieerde been, de b3-spikes
(max 140 gr bij het Kristall-anker, rest op MKAD-afritten en bij het SVO-anker) zijn korte OSM-stukjes (<= 47 m), geen terugloop.
De +-15%-toets is hier een indicatie: 412,0 km tegen hemelsbreed 362 km (+13,8%) is een normale wegfactor; er is geen gepubliceerde wegkm.

**Afwijkingen van het ontwerp:** Dorogobuzj ligt niet aan de M-1: het via-punt ligt bij Safonovo. De eerste 0,3 km vanaf het SVO-anker loopt over
OSM-service-wegen (snap 0,19 km); geen airside-stippel nodig omdat het anker bij het cargo-gebouw ligt.

**Lessen:** een stroom die twee bestaande benen letterlijk kopieert en maar een nieuw landbeen toevoegt bakt in een paar minuten; de MKAD draagt in OSM geen
ref, dus via-punten op de ring (vertices uit de eigen PBF-scan, snap 0) zijn nodig om de route niet dwars door Moskou te laten lopen.

**Open punten:** geen bron voor SVO-overslag en truck (AFP 2019: sommige Mirny-stenen vliegen naar slijpcentra in Moskou en Smolensk; directe vlucht naar
Smolensk niet uitgesloten); Mirny-aandeel in Kristalls 0,2 Mct/j niet uitgesplitst; Kristall ontbreekt in de sitelaag (centraal toevoegen).
