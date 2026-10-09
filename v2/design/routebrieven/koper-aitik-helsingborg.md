# Routebrief (licht) · Koper · Aitik → Rönnskär → Helsingborg (Zweden)

**stroom-id:** `koper-aitik-helsingborg` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** koperconcentraat van de Aitik-mijn (Boliden, Gällivare) gaat per **truck** naar de eigen spoorterminal op het mijnterrein en per **spoor** (Green Cargo "Aitik shuttle", ~395 km) naar de Rönnskär-smelter bij Skelleftehamn; de kathode gaat per **spoor** (Green Cargo "Copper shuttle", ~1.410 km) naar Helsingborg en vandaar per schip naar eindklanten; stoppunt = de containerterminal in Helsingborg. **Aannemelijk: één bron voor de bestemming** (been b2, zie §7).
**Welke as van het verhaal:** Noord-Europees binnenlands spoorpatroon, mijn → smelter → exporthaven binnen één land, zonder zeebeen. Peiljaar **2024: ~61 kt Cu in concentraat per jaar**, afgeleid uit 40.840 kt erts × 0,17 % Cu × 88,3 % recovery [2]; eenheid kt Cu/jaar, zoals de koper-sitelaag (`w-aitik` capaciteit_kt 61).

## 1 · Ketenkaart
```
Aitik-spoorterminal `cu-aitik-terminal` ──(b1 spoor · Malmbanan → Boden → Norra stambanan → Skelleftehamnsbanan · 394,5 km [ABB: ~400])──►
Rönnskär-smelter `cu-ronnskar-smelter` ──(b2 spoor · Botniabanan → Ostkustbanan → Bergslagen → Södra stambanan → Skåne · 1.411,6 km, aannemelijk)──►
Helsingborg, containerterminal `cu-helsingborg-terminal` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `cu-aitik-terminal` → `cu-ronnskar-smelter` | Malmbanan (Aitik–Murjek–Boden) · Norra stambanan (Boden–Älvsbyn–Bastuträsk) · Skelleftehamnsbanan | gepubliceerd ~400 km [3]; gemeten 394,5 (−1,4 %); hemelsbreed 268,3 | `toets_spoorroute` | nee |
| b2 | C | spoor | `cu-ronnskar-smelter` → `cu-helsingborg-terminal` | Bastuträsk–Vännäs · Botniabanan via Umeå, Örnsköldsvik, Kramfors · Sundsvall–Hudiksvall–Gävle · Gävle–Frövi–Hallsberg · Mjölby–Nässjö–Alvesta–Hässleholm–Åstorp | geen spoorkm gepubliceerd; gemeten 1.411,6; hemelsbreed 1.068,1 (verhouding 1,32) | `toets_spoorroute`, één run | nee |

Géén zeebeen en géén last-mile-been: de Aitik-terminal ligt op het mijnterrein (het concentraat gaat per truck van de concentrator naar die terminal [2]) en de Helsingborg-terminal ligt 0,4 km van het hoofdnet. Naad b1→b2: beide benen snappen op dezelfde hoofdnet-knoop 3556549 (0,38 km van het anker), dus 0,00 km. De ±15 %-toets slaagt voor b1 (−1,4 %); voor b2 is hij alleen indicatie (geen gepubliceerde spoorlengte).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-aitik-terminal` | spoorterminal (kop b1) | Aitik, spoorterminal op het mijnterrein | 67.0751, 20.7754 | [2][4] | bron-gelegd (z15 gezien: emplacement met meerdere parallelle sporen en een grote hal aan de zuidrand van het mijnmeer; spoor komt uit het zuidwesten, het punt ligt op het westelijke emplacementseinde). Het sitelaag-punt `w-aitik` (67.0667, 20.9500, Wikipedia) is het midden van de put en ligt 7,6 km oostelijker: geen anker. |
| `cu-ronnskar-smelter` | smelter (staart b1, kop b2) | Boliden Rönnskär, Skelleftehamn | 64.6704, 21.2699 | [5][11] | bron-gelegd, **letterlijk hergebruikt** uit `zilver-garpenberg-ronnskar` (`ag-ronnskar-kade`; z15: smeltercomplex met schoorstenen en kade, OSM `landuse=industrial` 0 m); spoor-snap 0,38 km |
| `cu-helsingborg-terminal` | losplek / exporthaven (staart b2) | Port of Helsingborg, containerterminal | 56.0310, 12.6930 | [1][6][10] | aannemelijk (z14/z15 gezien: kade met containerstapels en een schip aan de kade, spoorlijnen langs de haven; geen bron noemt de terminal, het dichtstbijzijnde haven-spoor snapt op 0,43 km) |

Satellietbeelden (Esri z14/z15, `v2/build-cache/satcheck/`): `sat-koper-aitik-helsingborg-aitik-z14.png`, `…-aitik-z15.png`, `…-haven-z14.png`, `…-haven-z15.png`; Rönnskär: `sat-koper-aitik-helsingborg-ronnskar.png` en het beeld van de Garpenberg-brief.

## 4 · Via-punten
**Geen via-punten, per bindende haalbaarheidstoets:** elk been is één run zonder via, 0 omkeringen (keerstraf 25 km). De corridorkeuzes liggen vast door de ankers; ter controle (niet als via te gebruiken) passeert b2 deze plaatsen, afstand lijn–plaats en ketenkm vanaf Rönnskär:
| plaats | lat, lon | afstand | ketenkm |
|---|---|---|---|
| Bastuträsk | 64.7700, 20.0200 | 1,1 km | 65 |
| Vännäs | 63.9100, 19.7500 | 1,0 km | 173 |
| Umeå | 63.8250, 20.2600 | 0,7 km | 204 |
| Örnsköldsvik | 63.2900, 18.7200 | 0,8 km | 318 |
| Kramfors | 62.9300, 17.7800 | 0,2 km | 405 |
| Sundsvall | 62.3900, 17.3000 | 0,2 km | 510 |
| Gävle | 60.6700, 17.1500 | 1,4 km | 729 |
| Frövi | 59.4600, 15.3800 | 0,7 km | 928 |
| Hallsberg | 59.0650, 15.1100 | 0,2 km | 980 |
| Nässjö | 57.6500, 14.7000 | 0,1 km | 1.165 |
| Hässleholm | 56.1600, 13.7600 | 0,3 km | 1.349 |
Niet geraakt: Stockholm 134,6 km ernaast, Ånge 82 km, Långsele 35 km, Borlänge 56 km. b1 passeert Murjek (0,4 km, ketenkm 77), Boden (0,4 km, 161), Älvsbyn (0,0 km, 205), Bastuträsk (1,7 km, 333) en Skellefteå (0,5 km, 379).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Aitik-concentrator + terminal | Boliden | erts → Cu-concentraat (met Au/Ag), per truck naar de terminal, per trein weg; ~500 t concentraat/dag per trein (2010) | 40.840 kt erts, ~61 kt Cu (2024); vergunning 45 Mt erts/jaar | [2][3] |
| Rönnskär-smelter | Boliden | Cu- en Pb-concentraat (eigen + extern) → Cu-kathode, edelmetalen | 266 kt kathode (2025) | [5] |
| Helsingborg-haven | Port of Helsingborg; Dalshult stuwt de containers voor Boliden | kathode per trein → container/schip, overzee | ~40 containers/week (2024); shuttle Rönnskär–Helsingborg sinds 1993 | [1][6] |

## 6 · Stoppunt
De brief stopt in de containerterminal van Helsingborg: de bronnen zeggen alleen dat de kathode daar "onward to various end-customers" wordt verscheept [1], geen bron noemt schip, lijn of afnemer, dus geen fase D en geen zeebeen.

## 7 · Open punten
- **Aannemelijk, één bron voor de bestemming:** alleen het Green Cargo-bericht van 13 maart 2017 [1] noemt de "Copper shuttle" Rönnskär → Helsingborg; de haven bevestigt in 2024 een shuttle sinds 1993 en ~40 containers/week voor Boliden [6], maar noemt de terminal niet en noemt geen kathode.
- **Terminal in Helsingborg niet bevestigd:** het anker is de containerterminal (stapels, schip aan de kade); of Dalshult daar of op een andere kade stuwt is niet gevonden.
- **Corridor Vännäs → Sundsvall:** de router kiest Botniabanan via Umeå, niet de Norra stambanan via Långsele en Ånge uit het ketenontwerp; Green Cargo's werkelijke route is niet gepubliceerd. Gemeten 1.411,6 km, hemelsbreed 1.068 km, geen gepubliceerde spoorkm: de ±15 %-toets is alleen indicatie.
- **Boliden R&R 2024 [2] noemt Rönnskär "about 350 km" van Aitik** (ABB/EMJ 2010 [3]: ~400 km); de gemeten 394,5 km sluit op ABB aan, de 350 km lijkt een ruwe schatting.
- **Volume leg C onbekend:** de 266 kt kathode is het smelterstotaal, geen aandeel Aitik of Helsingborg; Rönnskär had na de brand van 2023 een lagere kathodeproductie (zoekresultaten, niet zelf gelezen: ~150 kt in 2026, 350 kt in 2027).
- Sitelaag-punt `w-aitik` (67.0667, 20.95) is het putmidden, geen terminal: centraal beslissen of het sitelaag-anker verhuist (niet mijn bestand).

## 8 · Bronnen
[1] Green Cargo, "Boliden extend its agreement with Green Cargo", 13-3-2017 — Aitik shuttle (Aitik → Rönnskär) en Copper shuttle (Rönnskär → Helsingborg, "shipped onward to various end-customers"), 7 dagen/week (zelf gelezen). https://www.mynewsdesk.com/greencargo/news/boliden-extend-its-agreement-with-green-cargo-227453
[2] Boliden, Summary Report Resources and Reserves 2024, Aitik — 40.840 kt erts, 0,17 % Cu, 88,3 % recovery; concentraat "trucked to an on-site railway terminal and reloaded" naar Rönnskär; mijn 15 km ten oosten van Gällivare (zelf gelezen, tabel 3). https://www.boliden.com/490349/globalassets/operations/exploration/mineral-resources-and-mineral-reserves-pdf/2024/resources-and-reserves-aitik-2024-12-31.pdf
[3] Engineering & Mining Journal / ABB, "Aitik" (okt. 2010) — ~500 t concentraat/dag per trein naar Rönnskär, 400 km, eigen spoorterminal (via zoekresultaat, pdf niet zelf gelezen). https://library.e.abb.com/public/d9044272eb0556b6c12577dc0058115c/Aitik_Engineering%20and%20Mining%20Journal%20October%202010%20A4_lr.pdf
[4] Sweco, "Sweco to streamline ore transports from Aitik" (2006) — nieuwe spoorverbinding en terminal bij Aitik; vroeger per weg naar Gällivare (zelf gelezen). https://www.swecogroup.com/corporate-news/sweco-to-streamline-ore-transports-from-aitik/
[5] Boliden, "Boliden Rönnskär" — 266 kt kathode in 2025, haven en spoor bij de vestiging (zelf gelezen). https://www.boliden.com/operations/smelters/boliden-ronnskar
[6] Port of Helsingborg, "Boliden expands container volume via Helsingborg", 28-8-2024 — shuttle Rönnskär–Helsingborg sinds 1993, ~40 containers/week bij Dalshult (zelf gelezen). https://port.helsingborg.se/?p=14480
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14/z15) — de vier PNG's uit §3.
[11] `v2/design/routebrieven/zilver-garpenberg-ronnskar.md` — Rönnskär-anker 64.6704, 21.2699 (bron-gelegd).
[12] Eigen metingen met `toets_spoorroute.mjs` (1-op-1-net, extract zweden): b1 394,5 km / 502 edges / 0 bochten ≥ 60°; b2 1.411,6 km / 1.977 edges / 0 bochten; snaps 0,00 / 0,38 / 0,43 km; haalbaarheidstoets van de keten (workflow-invoer).

## 9 · Gebakken
**Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)** · `v2/data/stroomroute-koper-aitik-helsingborg.json` (96,3 KB, versie 2, `lonlat`) · recept `bak_koper_aitik_helsingborg()` in `v2/tools/bak_stromen.sh`.

| # | modaliteit | been | km (json) | naad | stippel |
|---|---|---|---|---|---|
| 1 | spoor | Aitik-terminal → Rönnskär-smelter (Aitik shuttle) | 397,3 | – | nee |
| 2 | spoor | Rönnskär → Helsingborg-containerterminal (Copper shuttle, aannemelijk: één bron) | 1.425,9 | 0,00 | nee |

Totaal 1.823,2 km · 5.502 punten · 3 markers (Aitik-terminal 0,00 km van de lijn, Rönnskär 0,38 km, Helsingborg 0,43 km: de spoor-snaps).

**Recept.** Beide benen zijn de vooraf gebakken spoorgeojson uit `v2/build-cache/ais/graaf/` (`spoorroute-koper-aitik-helsingborg-aitik-ronnskar.geojson` en `…-ronnskar-helsingborg.geojson`, `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs`, extract zweden, geen via), als `--been-geojson spoor` in `hecht_marnet.py route`; geen zeebeen, aanloop, stippel, luchtbeen, last-mile, wegprofiel of letterlijke kopie.

**Toets.** b1 397,3 km tegen ABB ~400 km: -0,7 % (norm ±15 % gehaald). b2 1.425,9 km: geen gepubliceerde spoorkm, alleen indicatie (omwegfactor 1,33 tegen hemelsbreed 1.068). Naad b1→b2 0,00 km. `toets_knikken.py`: 0 knikken, 0 omkeringen. `toets_rechte_benen.py`: geen melding voor deze stroom.

**Les / afwijking.** De bake-km (haversine over de punten) ligt 0,7 % (b1) en 1,0 % (b2) boven de 394,5 en 1.411,6 km die de spoorrouter in zijn console geeft (edge-lengte); het json is de bron voor de bol. Titel blijft "Aitik → Rönnskär → Helsingborg": eindpunt klopt met het stroom-id. Open punten: zie §7 (terminal Helsingborg niet bevestigd, corridor Vännäs–Sundsvall via Botniabanan, sitelaag-punt `w-aitik` 7,6 km van de terminal, volume leg C onbekend).

