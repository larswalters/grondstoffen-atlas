# Routebrief (licht) · Zilver · Aitik → Rönnskär (Zweden)

**stroom-id:** `zilver-aitik-ronnskar` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) ·
**status:** gebakken
**Keten in één zin:** koper-goud-zilverconcentraat van de Aitik-mijn (Boliden, Gällivare) gaat per **truck** van de concentrator naar de eigen spoorterminal op het mijnterrein (geen eigen been) en per **spoor** (Green Cargo "Aitik shuttle", Malmbanan, Norra stambanan, Skelleftehamnsbanan, ~400 km) naar de Rönnskär-smelter bij Skelleftehamn; stoppunt = de smelter.
**Welke as van het verhaal:** zilver als bijproduct van Europa's grootste kopermijn, Arctisch Zweden naar de edelmetaal-smelter van Boliden. Peiljaar **2024: ≈ 21 t Ag/j in het concentraat** (40,8 Mt erts × 0,7 g/t = 28,6 t Ag in erts × 75% recovery; eigen berekening uit [1]); eenheid t Ag/j. Zilver is slechts 2% van de Aitik-omzet [1].

## 1 · Ketenkaart
```
Aitik-spoorterminal `ag-aitik-terminal` ──(b1 spoor · Malmbanan → Boden → Norra stambanan → Skelleftehamnsbanan · 397 km gemeten; ~400 [3], "ongeveer 350" [1])──►
Rönnskär-smelter `ag-ronnskar-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ag-aitik-terminal` → `ag-ronnskar-smelter` | Malmbanan (Aitik–Murjek–Boden) · Norra stambanan (Boden–Älvsbyn–Bastuträsk) · Skelleftehamnsbanan; Green Cargo Aitik shuttle [2] | gepubliceerd ~400 km [3], "about 350 km" [1]; gemeten 397,3 (−0,7% op [3], +13,5% op [1]); hemelsbreed 268,3 | **letterlijke kopie** van `spoorroute-koper-aitik-helsingborg-aitik-ronnskar.geojson` (b1 van `koper-aitik-helsingborg`, `toets_spoorroute`, 1-op-1-net) | nee |

Geen zeebeen (smelter ligt 1,5 km van zeeknoop 8833, maar dit been eindigt op het spoor), geen last-mile-been, geen leiding, geen lucht. De Aitik-terminal ligt op het mijnterrein: de truck van concentrator naar terminal [1] is geen apart been. De ±15%-toets slaagt op de bedrijfsopgave van 400 km [3]; tegen de ruwe "about 350 km" van [1] (+13,5%) ook nog net, en die 350 lijkt een afgeronde schatting (ABB, zelfde corridor: 400).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-aitik-terminal` | spoorterminal (kop b1) | Aitik, spoorterminal op het mijnterrein (Boliden) | 67.0751, 20.7754 | [1][3][4] | bron-gelegd, **letterlijk hergebruikt** uit `koper-aitik-helsingborg` (`cu-aitik-terminal`). Eigen z15-blik (`sat-zilver-aitik-ronnskar-aitik.png`): emplacement met parallelle sporen en een grote hal langs de zuidrand van het mijnmeer, spoor komt uit het zuidwesten, het punt ligt op het westelijke emplacementseinde. |
| `ag-ronnskar-smelter` | smelter / losplek (staart b1, stoppunt) | Boliden Rönnskär, Skelleftehamn | 64.6704, 21.2699 | [2][5] | bron-gelegd, **letterlijk hergebruikt** uit `zilver-garpenberg-ronnskar` (`ag-ronnskar-kade`) en `koper-aitik-helsingborg`. Eigen z15-blik (`sat-zilver-aitik-ronnskar-smelter.png`): smeltercomplex met schoorstenen, tankenpark en opslag op het schiereiland, spoor loopt het terrein in; het punt ligt aan de noordkant van het complex bij de spoorinvoer. Spoor-snap 0,38 km. |

Het sitelaag-punt `w-aitik` (zilversitelaag kent geen Aitik; koperlaag: putmidden 67.0667, 20.9500) is 7,6 km van de terminal en dus geen anker.

## 4 · Via-punten
**Geen via-punten, conform de bindende haalbaarheidstoets:** b1 is een kopie van een run zonder via, 0 bochten ≥ 60°, 0 omkeringen. Controle-plaatsen op b1 (afstand lijn-plaats, ketenkm vanaf Aitik): Murjek 0,4 km (77), Boden 0,4 km (161), Älvsbyn 0,0 km (205), Bastuträsk 1,7 km (333), Skellefteå 0,5 km (379). Bron: brief `koper-aitik-helsingborg` §4.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Aitik-concentrator + terminal | Boliden | erts (0,7 g/t Ag) → Cu-concentraat met Au/Ag; per truck naar de terminal, per trein weg (~500 t concentraat/dag, 2010) | 40,8 Mt erts in 2024; ≈ 21 t Ag in concentraat; Ag-recovery ~75% | [1][3] |
| Rönnskär-smelter | Boliden | Cu- en Pb-concentraat (eigen + extern) + e-waste → Cu-kathode, Ag, Au | 2025: 266 kt kathode, **191 t Ag**, 5 t Au | [5] |

## 6 · Stoppunt
De brief stopt bij de Rönnskär-smelter: geen bron noemt een afnemer of fabriek voor het Aitik-zilver na de raffinage, dus fase D vervalt en er is geen fase E. (Het zilver verlaat Rönnskär als edelmetaal-product; de kathode-shuttle naar Helsingborg is koper en hoort bij `koper-aitik-helsingborg`.)

## 7 · Open punten
- **Gedeeld been, geen nieuwe geometrie:** b1 is 100% gelijk aan b1 van `koper-aitik-helsingborg`; nieuw is alleen de grondstof (zilver) en de ketenas. Centraal beslissen of dit als eigen stroom op de bol komt (dubbele lijn op dezelfde rails).
- **Zilvervolume is een afleiding:** [1] geeft 0,7 g/t Ag in het jaarkop (2024) en ~75% Ag-recovery, geen concentraat-zilvertonnage. Het concentrator-grade uit de reconciliatietabel van [1] is 0,8 g/t (→ ≈ 24 t); 21 t is de conservatieve keuze. Peiljaar 2025 (39,2 Mt erts [4]) geeft geen graad.
- **Rönnskär-zilver is niet uit te splitsen per herkomst:** de 191 t Ag (2025) is smelterstotaal incl. e-waste en andere mijnen (o.a. Garpenberg, `zilver-garpenberg-ronnskar`); het Aitik-aandeel (≈ 21 t) is een schatting, geen gemeten stroom.
- **Eindanker gedeeld** met `zilver-garpenberg-ronnskar` (zelfde marker 64.6704, 21.2699); de zilversitelaag heeft `w-ref-ronnskar` maar geen Aitik-site. Centraal beslissen of er een zilversite Aitik bij moet (niet mijn bestand).
- **Corridor niet door Green Cargo gepubliceerd:** de route Malmbanan → Boden → Norra stambanan is de gemeten kortste treinpad; de exacte treinweg staat nergens beschreven.

## 8 · Bronnen
[1] Boliden, Summary Report Resources and Reserves 2024, Aitik (2024-12-31) — 40,8 Mt erts met 0,7 g/t Ag in 2024; Ag 2% van de omzet; recovery ~75% Ag; concentraat per spoor naar Rönnskär, "about 350 km"; concentraat per truck naar de spoorterminal op het terrein (zelf gelezen, p.7 en p.22). https://www.boliden.com/490349/globalassets/operations/exploration/mineral-resources-and-mineral-reserves-pdf/2024/resources-and-reserves-aitik-2024-12-31.pdf
[2] Green Cargo, "Boliden extend its agreement with Green Cargo", 13-3-2017 — Aitik shuttle: kopersconcentraat Aitik (Gällivare) → Rönnskär (Skelleftehamn), 7 dagen per week, enkelvoudige treinen (zelf gelezen). https://www.mynewsdesk.com/greencargo/news/boliden-extend-its-agreement-with-green-cargo-227453
[3] Engineering & Mining Journal / ABB, "Aitik" (okt. 2010) — ~500 t concentraat/dag per spoor naar Rönnskär, 400 km, eigen spoorterminal (zelf gelezen). https://library.e.abb.com/public/d9044272eb0556b6c12577dc0058115c/Aitik_Engineering%20and%20Mining%20Journal%20October%202010%20A4_lr.pdf
[4] Boliden, "Boliden Aitik" (operations) — 2025: 39,2 Mt erts verwerkt tot Cu/Au/Ag-concentraten, open pit, Gällivare (zelf gelezen). https://www.boliden.com/operations/mines/boliden-aitik
[5] Boliden, "Boliden Rönnskär" (operations) — productie 2025: 266 kt Cu-kathode, 191 t Ag, 5 t Au; haven en spoor als vestigingsreden (zelf gelezen). https://www.boliden.com/operations/smelters/boliden-ronnskar
[6] `v2/design/routebrieven/koper-aitik-helsingborg.md` — b1: spoorgeometrie, ankers, metingen (397,3 km, snaps 0,00 / 0,38 km), controle-plaatsen.
[7] `v2/design/routebrieven/zilver-garpenberg-ronnskar.md` — Rönnskär-anker 64.6704, 21.2699 (OSM `landuse=industrial "Rönnskärsverken"` 0 m).
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15, grid 0,01°) — `sat-zilver-aitik-ronnskar-aitik.png`, `sat-zilver-aitik-ronnskar-smelter.png` in `v2/build-cache/satcheck/`.
[9] Haalbaarheidstoets (workflow-invoer, M31 golf 17) — bindend: kopie b1, volume 21 t Ag/j, km-norm.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
Bestand `v2/data/stroomroute-zilver-aitik-ronnskar.json` (20,7 KB, contract versie 2, punt_formaat lonlat), recept `bak_zilver_aitik_ronnskar()` in `v2/tools/bak_stromen.sh`. Titel: Zilver · Aitik → Rönnskär (Zweden, spoor).

| # | modaliteit | been | km | punten | lijnstijl |
|---|---|---|---|---|---|
| b1 | spoor | trein Aitik-terminal → Rönnskär-smelter (Green Cargo Aitik shuttle, Malmbanan en Norra stambanan; letterlijke kopie van koper-aitik-helsingborg b1) | 397,3 | 1154 | doorgetrokken |

Totaal 397,3 km, 1 been, 2 markers (`ag-aitik-terminal` 67.0751, 20.7754 en `ag-ronnskar-smelter` 64.6704, 21.2699).
**Recept:** `--been-geojson spoor` op `$BEEN/spoorroute-koper-aitik-helsingborg-aitik-ronnskar.geojson` (vooraf gebakken lijn, niet opnieuw geroutet). Geen nieuwe tool-run, geen eigen geojson, geen profiel, geen via-punten. Geen stippel, haven-aanloop, vlucht, leiding of weg.
**Toets:** 397,3 km tegen ca. 400 (ABB 2010) = -0,7% (ok; tegen "about 350" van Boliden +13,5%). Geen naden (één been). Markers: terminal 0,00 km van de lijn, smelter 0,38 km. `toets_knikken`: 0 knikken, 0 omkeringen. `toets_rechte_benen --min-km 5`: geen melding voor deze stroom.
**Lessen / bevindingen:** (1) het brief-kopcommentaar van koper-aitik-helsingborg noemt 394,5 km (routeKm in de geojson-properties), de gemeten polylijn is 397,3 km; de bak meldt 397,3. (2) Dubbeling: 100% gelijk aan b1 van koper-aitik-helsingborg, centraal beslissen over een dubbele lijn op de bol. (3) Het zilvervolume (ca. 21 t Ag/j) blijft een afleiding.
