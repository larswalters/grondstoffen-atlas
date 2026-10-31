# Routebrief (licht) · olie — Vohburg (Duitsland) → IKL via Rozvadov → Nelahozeves bij Praag (Tsjechië)

**stroom-id:** `olie-vohburg-nelahozeves` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** Ruwe olie per **leiding** — de Ingolstadt–Kralupy–Litvínov-leiding (IKL, 28 inch, MERO) — van de MERO-kopstation in het Bayernoil-terrein bij
Vohburg an der Donau (Beieren) via de grens bij Rozvadov naar het MERO-tankenpark Nelahozeves bij Praag; 322,4 km OSM-som in één been, zonder zee.
**Welke as van het verhaal:** *Tsjechië zonder Druzhba* — de TAL-olie uit Triëst kruist bij Vohburg over op de IKL en is sinds april 2025 de enige aanvoer naar de Tsjechische
raffinaderijen [3][4]. **Volume:** mei 2025 bijna 660 kt in één maand (record, 586 kt in 2012) = ca. **156 kb/d** (7,33 vat/t, eigen omrekening) [3]; jaargemiddelde 2024 **3,8 Mt =
ca. 76 kb/d** (58% van de Tsjechische import, de rest Druzhba) [2]. Capaciteit IKL 11 Mt/j; TAL-PLUS maakt tot 8 Mt/j voor Tsjechië mogelijk [2][4][5]. Geen jaarcijfer 2025 gevonden (§7).

## 1 · Ketenkaart
```
MERO-kopstation Vohburg (in Bayernoil-terrein) `ol-vohburg-ikl` ──(b1 leiding · IKL 28" · Vohburg → Beierse Woud → grens Rozvadov (km 157,5) → Nelahozeves ·
   347 km gepubliceerd, 322,4 km OSM, naden 0 m)──► MERO-tankenpark Nelahozeves `ol-nelahozeves-mero` ── stoppunt
```
Geen zeebeen (geen bron voor de herkomst van de lading). Aftakking van TAL naar Vohburg valt buiten de keten (zie §7).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | MERO-kop Vohburg → MERO-tankenpark Nelahozeves | Ingolstadt–Kralupy–Litvínov-leiding / Mitteleuropäische Rohölleitung (MERO) / ropovod IKL | 347 [1][2]; OSM 322,4 (-7,1%) [6] | 3 OSM-ways, `man_made=pipeline substance=oil`, `maak_leidingbeen_olie_vohburg_nelahozeves.py` | nee |

OSM-ways in reisvolgorde (gedeelde nodes 7550120391 en 1686438757, naden 0 m): **338003961** (157,5 km, Duitse deel, eindigt op de grens bij 49.6545,12.5292) · **814022703** (132,9 km,
Tsjechië, `ref=MERO`, `location=underground`) · **578939177** (32,1 km, `name:cs=Ropovod IKL`, eindigt in Nelahozeves). Duits deel 157,5 km tegen 178 gepubliceerd (-11%), Tsjechisch
164,9 tegen 169 (-2,4%) [2][6]. Eén been, dus geen naad tussen benen; geen fase B/C/D/E: de pijp eindigt in het tankenpark.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-vohburg-ikl` | kop van de leiding (MERO-kopstation + tankenpark) | MERO-kopstation in het Bayernoil-terrein Vohburg — OSM-beginknoop van way 338003961 | 48.7709, 11.6022 | [1][2][6][7] | bron-gelegd (z15 gezien: uitgestrekt tankpark van het Bayernoil-complex met tientallen tanks aan de noordrand van de raffinaderij, naast de Donau; het punt ligt in een tankgroep; MERO's 4 eigen tanks zijn niet afzonderlijk aan te wijzen) |
| `ol-nelahozeves-mero` | eind van de leiding (Centrale Tankenpark Nelahozeves) | MERO-tankenpark Nelahozeves — OSM-eindknoop van way 578939177 | 50.2887, 14.2967 | [1][2][6][7] | bron-gelegd (z15 gezien: ommuurd tankenpark met ca. 15 grote cilindrische tanks op een plateau boven de Moldau-vallei bij Nelahozeves; punt op het pijpenstraatje tussen twee tankgroepen) |

Sitelaag `olie-sitelaag.json` heeft geen Vohburg- of Nelahozeves-site; geen hergebruik. `ol-vohburg-ikl` ligt 9,7 km (hemelsbreed) van `ol-ingolstadt-tal` (Lenting) uit
`olie-trieste-ingolstadt`: geen letterlijk gedeeld been, **naad tussen de twee stromen 9,7 km** (de TAL-aftakking Lenting → Vohburg is niet gekarteerd en niet getekend).

## 4 · Via-punten (leiding: geen corridorkeuze; één info-knoop, geen via-punt)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | way-overgang 338003961 → 814022703 (grens Beieren/Tsjechië bij Rozvadov) | 49.6545, 12.5292 | gedeelde node 7550120391 op 157,5 km; alleen ter controle, geen via-punt |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| MERO-tankenpark Vohburg a.d. Donau | MERO Germany AG (dochter MERO ČR) | TAL-aftakking → opslag 4 tanks 200.000 m3 → IKL | IKL 11 Mt/j; piek mei 2025 660 kt/maand | [1][2][3] |
| Centrale Tankenpark Nelahozeves | MERO ČR a.s. (100% Min. van Financiën) | IKL + Druzhba → opslag 17 tanks 1.675.000 m3 → Kralupy en Litvínov (Orlen Unipetrol) | 1.675.000 m3 | [2][3][5] |

## 6 · Stoppunt
De brief stopt in het MERO-tankenpark Nelahozeves: de IKL eindigt daar; de olie gaat vandaar over aparte Tsjechische leidingen naar de raffinaderijen Kralupy en Litvínov, die niet in OSM-pijpleiding-geometrie zijn vastgelegd en hier niet worden verzonnen.

## 7 · Open punten
- **Volume 2025/26:** geen jaarcijfer; 156 kb/d is één maand (mei 2025), 76 kb/d is 2024. Tot 8 Mt/j (ca. 160 kb/d) is een planningsmaximum, geen meting [4][5].
- **Duits deel 157,5 km (OSM) tegen 178 gepubliceerd (-11%):** onverklaard (andere meetpunten of een stuk dat OSM niet kent); totaal -7,1% blijft binnen ±15%. Echte leidinglengte, dus een echte norm.
- **TAL-link Lenting → Vohburg (9,7 km hemelsbreed)** niet gekarteerd; de keten begint bij de IKL-kop, niet bij het TAL-tankenpark.
- **Vohburg-anker** ligt in het Bayernoil-terrein (OSM-landuse 29122362 draagt zelf een fixme dat de MERO-kopstation erin ligt); precieze tankgroep niet vastgesteld.
- **Herkomst van de olie** (TAL-lading uit Triëst) niet gebronnen; geen zeebeen.

## 8 · Bronnen
[1] Wikipedia, "Ingolstadt–Kralupy–Litvínov pipeline" — 347 km (178 DE / 169 CZ), 28 inch, Vohburg → Nelahozeves, capaciteit ~10 Mt/j. https://en.wikipedia.org/wiki/Ingolstadt%E2%80%93Kralupy%E2%80%93Litv%C3%ADnov_pipeline
[2] MERO ČR, "Proměny infrastruktury v Česku a Evropě 2025" (april 2025) — IKL 347 km, 178/169 km, 11 Mt/j, 2024: 3,8 Mt (58%), Nelahozeves 17 tanks 1,675 Mm3, Vohburg-tankoviště. https://mero.cz/wp-content/uploads/2025/04/mero-promeny-infrastruktury-v-cesku-a-evrope-data-cisla-a-souvislosti-2025.pdf
[3] MERO ČR, persbericht 4 aug 2025 — IKL mei 2025 bijna 660 kt (record), 4 maanden uitsluitend westelijke route, Vohburg 200.000 m3. https://mero.cz/wp-content/uploads/2025/08/2025-08-04-tz-ctyri-mesice-s-tal-plus-ropovodem-ikl-priteka-do-ceska-rekordni-mnozstvi-ropy.pdf
[4] MERO ČR, persbericht 14 jan 2025 — TAL-PLUS, tot 8 Mt/j via TAL en IKL. https://mero.cz/wp-content/uploads/2025/01/2025-01-14-tz-cesko-je-technicky-pripravene-na-odstrizeni-od-ruske-ropy-projekt-tal-plus-se-posouva-do-konecne-faze.pdf
[5] oEnergetice.cz, "Czech state-owned MERO and Orlen Unipetrol sign new oil transport contract" (jan 2025) — tot 8 Mt/j westelijk, 2023: 7,4 Mt, 58% Druzhba. https://oenergetice.cz/en/oil/czech-state-owned-mero-and-orlen-unipetrol-sign-new-oil-transport-contract
[6] OpenStreetMap-API (ODbL), ways 338003961, 814022703, 578939177 (`man_made=pipeline substance=oil name=Mitteleuropäische Rohölleitung operator=MERO Germany AG`) en landuse 29122362 (Bayernoil Raffinerie Vohburg, fixme MERO-kop). https://api.openstreetmap.org/api/0.6/ways.json?ways=338003961,814022703,578939177,29122362
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-olie-vohburg-nelahozeves-vohburg.png`, `sat-olie-vohburg-nelahozeves-nelahozeves.png`.
[8] oEnergetice.cz, "Provozovator ropovodu Mero loni zvysil cisty zisk" (mei 2023) — 2022: 7,4 Mt naar Tsjechische raffinaderijen, 56% Rusland. https://oenergetice.cz/ropa/provozovatel-ropovodu-mero-loni-zvysil-cisty-zisk-o-desetinu-na-7883-mil-kc

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-olie-vohburg-nelahozeves.json` (11,0 KB, versie 2, lonlat) · **functie:** `bak_olie_vohburg_nelahozeves` in `v2/tools/bak_stromen.sh` · **register:** `olie-vn` (centraal).
**Recept:** `python v2/tools/maak_leidingbeen_olie_vohburg_nelahozeves.py --schrijf` (3 OSM-ways op gedeelde nodes gestikt, FeatureCollection met 1 LineString) -> `hecht_marnet.py route` met één `--been-geojson "leiding|..."` en twee markers; geen zee, geen aanloop, geen stippel, geen wegscan, geen profiel.

| # | modaliteit | km gemeten | brief | afwijking | punten | naad |
|---|---|---|---|---|---|---|
| b1 | leiding (doorgetrokken) | 322,4 | 347 gepubliceerd (178 DE + 169 CZ) | -7,1% (binnen +-15%, echte leidinglengte = echte norm) | 521 | n.v.t. (1 been) |

Totaal 322,4 km · 521 punten · 2 markers: `ol-vohburg-ikl` 5 m en `ol-nelahozeves-mero` 4 m van de lijn.
**Toetsen:** `toets_knikken.py` 21 knikken >= 60 graden, 0 omkeringen, 0 terugloop (OSM-leiding met bochten en spikes in de bronnodes, echte gekarteerde geometrie); `toets_rechte_benen.py` markeert dit been niet.
**Toelichting leiding:** doorgetrokken, want OSM kent de IKL volledig (`man_made=pipeline substance=oil`, operator MERO); ondergronds, dus de kartering is de enige geometrie. Geen stippel: er is geen gat in het net.
**Bevindingen:** (1) Duits deel -11% tegen gepubliceerd, onverklaard; totaal blijft binnen de norm. (2) Naad 9,7 km met `olie-trieste-ingolstadt` (TAL-link Lenting -> Vohburg niet gekarteerd), bewust niet getekend. (3) Sitelaag `olie-sitelaag.json` heeft geen Vohburg- of Nelahozeves-site: centraal eventueel toevoegen.
**Lessen:** een kant-en-klaar leidingbeen-geojson (FeatureCollection) bakt in één commando; geen zwaar rekenwerk nodig buiten het zwaar-slot voor de hecht_marnet-run.
