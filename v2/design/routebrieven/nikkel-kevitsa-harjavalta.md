# Routebrief (licht) · Nikkel — Kevitsa → Ajos (Kemi) → Harjavalta (Finland)

**stroom-id:** `nikkel-kevitsa-harjavalta` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** nikkel(-koper)concentraat van Boliden's Kevitsa-mijn (Sodankylä, Lapland) gaat per **truck** (Vt4/E75 via Rovaniemi en Tervola, ~306 km) naar de haven Ajos in Kemi en van daar per **spoor** (Oulu – Ylivieska – Kokkola – Seinäjoki – Parkano – Tampere – Kokemäki) naar Boliden's Harjavalta-smelter, de enige nikkelsmelter van West-Europa; stoppunt = de smelter. **Aannemelijk: één bron voor de bestemming** (zie §7).
**Welke as van het verhaal:** Europees nikkelconcentraat, mijn → smelter binnen één land. Peiljaar **2025**: **11.628 t Ni** in nikkelconcentraat (plus 2.065 t Cu in datzelfde concentraat; kopervolume in het koperconcentraat 20.663 t) [1] = **11,6 kt Ni/j**, eenheid kt Ni-in-concentraat (kopconcentraat gaat niet mee). Dat is een bovengrens voor deze lijn: Boliden verdeelt het niet over Harjavalta en Rönnskär [2]. Ter vergelijking: Harjavalta 34 kt Ni (2025) [3], dus Kevitsa kan hooguit ~1/3 daarvan zijn (eigen rekensom, indicatie).

## 1 · Ketenkaart
```
Kevitsa-concentrator `ni-kevitsa-concentrator` ──(b1 truck · Vt4/E75 · ~306 km [VR: "lähes 300"])──► Ajos, Kemi `ni-ajos-kade` (pakhuis)
──(b2 spoor · Kemi–Oulu–Ylivieska · 240 km)──► (b3 spoor · Ylivieska–Kokkola–Seinäjoki · 210 km)──► (b4 spoor · Seinäjoki–Parkano · 90 km)
──(b5 spoor · Parkano–Tampere–Kokemäki–Harjavalta · 174 km)──► Boliden Harjavalta-smelter `ni-harjavalta-smelter` ── stoppunt
```

## 2 · Benen
Alle vijf benen zijn **letterlijke kopieën** van het geojson van `pgm-kevitsa-harjavalta` (zelfde bestanden in `v2/build-cache/ais/graaf/`, zelfde functieregels; de weg en het spoor zijn niet grondstofspecifiek). Gedeeld met andere nikkel-stromen: Ylivieska–Kokkola (86 km) met `nikkel-sotkamo-kokkola`, eindpunt Harjavalta met `nikkel-monchegorsk-harjavalta` (daar het Nornickel-anker 61.3188,22.1225, hier het Boliden-anker).
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-kevitsa-concentrator` → `ni-ajos-kade` | mijnweg → Vt4/E75 (Sodankyläntie, Valtatie 4, Nelostie) → Kemi → Ajos | ~300 wegkm (VR Linked 2018) [6]; gemeten 306,6 (+2,2%) | KOPIE geojson `pgm-kevitsa-harjavalta-weg-kevitsa-ajos` | nee |
| b2 | B | spoor | `ni-ajos-kade` → Ylivieska | Kemi–Oulu · Pohjanmaan rata | geen spoorkm gepubliceerd; gemeten 240,4 | KOPIE `spoorroute-pgm-kevitsa-harjavalta-ajos-ylivieska` | nee |
| b3 | B | spoor | Ylivieska → Seinäjoki | Pohjanmaan rata via Kokkola | gemeten 210,1 | KOPIE `…-ylivieska-seinajoki` | nee |
| b4 | C | spoor | Seinäjoki → Parkano | Seinäjoki–Tampere-lijn | gemeten 89,6 | KOPIE `…-seinajoki-parkano` | nee |
| b5 | C | spoor | Parkano → `ni-harjavalta-smelter` | Seinäjoki–Tampere-lijn naar Tampere, dan Tampere–Pori-lijn naar Kokemäki/Harjavalta | gemeten 174,2 | KOPIE `…-parkano-harjavalta` | nee |
Totaal **1.020,9 km** (weg 306,6 + spoor 714,3; hemelsbreed spoor 497,8 km). De spoorlengte is nergens gepubliceerd: de ±15%-toets is alleen indicatie; het wegbeen valt binnen de norm. Geen zeebeen (geen Rönnskär), geen fase D/E, geen last-mile-been.

## 3 · Ankers (één per site en per overslag) — alle drie hergebruikt letterlijk uit `pgm-kevitsa-harjavalta` (daar satellietblik z15/z16)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-kevitsa-concentrator` | mijn + concentrator (kop) | Boliden Kevitsa, Sodankylä | 67.6945, 26.9334 | [2][9][10] | bron-gelegd (z15: concentratorhallen met silo/koepel aan de zuidoostrand van de pit, tailingbekken ervoor; Wikipedia-punt 67.6940,26.9280 lag 0,22 km westelijker op bijgebouwen) |
| `ni-ajos-kade` | overslag truck → spoor | Port of Kemi, Ajos, kade/pakhuiszone | 65.6650, 24.5210 | [6][10] | bron-gelegd (z15: pier met pakhuizen en kranen, spoorlijnen lopen vanuit het noordoosten het terrein in). Welk pakhuis het concentraatpakhuis is, is niet aan te wijzen |
| `ni-harjavalta-smelter` | losplek spoor / smelter (staart) | Boliden Harjavalta, Teollisuuskatu 1 | 61.3175, 22.1182 | [3][10] | bron-gelegd (z16: rangeerspoor met wagons langs de smelter-/opslaghallen). Het Nornickel-raffinaderij-anker ligt in hetzelfde complex (0,3 km), de perceelgrens is niet gezien |
Kevitsa en Harjavalta staan niet in `nikkel-sitelaag.json` (alleen `w-harjavalta-nornickel`/`w-harjavalta-boliden`, de laatste 0,46 km oostelijker aan de rand): centraal toevoegen als site (Kevitsa 67.6945,26.9334 · Harjavalta Boliden 61.3175,22.1182).

## 4 · Via-punten (alleen waar een corridorkeuze bestaat; allemaal op de doorgaande weg/lijn, letterlijk uit de PGM-brief)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Rovaniemi — Vt4 noord van het centrum | 66.5425, 25.8179 | pint Vt4/E75 (Sodankyläntie) in plaats van een zijweg |
| b1 | 2 | Tervola — Nelostie | 66.0869, 24.7729 | houdt de route op Vt4/E75 Rovaniemi–Kemi |
| b2/b3 | 3 | Ylivieska — op de Pohjanmaan rata | 64.0405, 24.4824 | pint Oulu → Ylivieska → Kokkola tegen een oostelijke sluipweg (spoor-snap 64.0392,24.4784) |
| b3/b4 | 4 | Seinäjoki — noord van het station | 62.7745, 22.8873 | splitst de lange Kokkola–Seinäjoki-run; spoorknoop |
| b4/b5 | 5 | Parkano — op de Seinäjoki–Tampere-lijn | 61.9857, 23.1425 | de corridorkeuze zelf: via Parkano (88,7 km, verhouding 1,00) en niet via Haapamäki |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kevitsa | Boliden | erts (10.155 kt gemalen 2025) → apart Ni-concentraat (11.628 t Ni, 2.065 t Cu, 481 t Co, Pt/Pd) en Cu-concentraat (20.663 t Cu) | ontwerp 9,9 Mtpa | [1][2] |
| Ajos (Port of Kemi) | Kemin Satama / Baltic Bulk | concentraat per truck → pakhuis → trein (2×/week in 2018) | niet gepubliceerd; 12–13 trucks/dag in 2021 | [6][7][8] |
| Harjavalta | Boliden | Ni-Cu-concentraat → nikkelmatte (één stap), koper, Au, Ag, zwavelzuur | 2025: 162 kt Cu, 34 kt Ni | [3][4][5] |

## 6 · Stoppunt
De brief stopt bij de Harjavalta-smelter: Boliden noemt Kevitsa als toeleverancier [3][4][5], maar geen bron zegt waar de nikkelmatte daarna heen gaat — geen fase D getekend.

## 7 · Open punten
- **Aannemelijk, één bron:** Boliden noemt voor Kevitsa-concentraten Harjavalta én Rönnskär zonder verdeling [2][5]; dat juist het Ni-concentraat naar Harjavalta rijdt, staat nergens expliciet. Harjavalta is de enige Ni-smelter van de groep ("nickel feed base load for our Harjavalta smelter", 2016 [4]), maar de VR-bronnen [6][7][8] zeggen alleen "rikaste" en niet welk concentraat.
- **Volume:** 11,6 kt Ni is het totaal van het Ni-concentraat, niet het deel dat per trein naar Harjavalta gaat; geen volume per smelter of route gepubliceerd.
- **Spoorlengte** onbekend: 714,3 km is gemeten op OSM; geen bron om tegen te toetsen.
- **Twee omkeringen uit de OSM-topologie, zo gelaten:** Kemi (65.7318,24.5802, Ajos-aftakking) en Tampere (61.4951,23.7740, Lielahti: de route rijdt ~0,8 km het station in en terug).
- **Kevitsa-sluiting:** Boliden's rapport noemt een sluitingsplan, update vóór september 2027 [1]; peiljaar 2025 geldt, de lijn kan uitdoven.
- **Ajos-pakhuis** en de **perceelgrens Boliden/Nornickel** in Harjavalta niet aangewezen. Geen Ni-gehalte van het concentraat uit een eigen gelezen bron.
- **Rönnskär-zeebeen** (Ajos → Rönnskär, `ag-ronnskar-kade` 64.6704,21.2699) is mogelijk, niet getekend: geen volume of schip gevonden.

## 8 · Bronnen
[1] Boliden, Summary Report Kevitsa — Mineral Resources and Reserves 31-12-2025: Ni-metaal in Ni-concentraat 2025 11.628 t, Cu 20.663 t (Cu-conc.) + 2.065 t (Ni-conc.), Co 481 t, 10.155 kt gemalen, sluitingsplan-update vóór sept. 2027 (zelf gelezen, tabel 7). https://www.boliden.com/4900d3/globalassets/operations/exploration/mineral-resources-and-mineral-reserves-pdf/2025/mineral-resources-and-mineral-reserves-kevitsa-2025-12-31.pdf
[2] Boliden, "Boliden Kevitsa" — nikkel- en koperconcentraten naar de eigen smelters Harjavalta en Rönnskär; 10,2 Mt erts 2025. https://www.boliden.com/operations/mines/boliden-kevitsa
[3] Boliden, "Boliden Harjavalta" — Kevitsa levert concentraten (ook externe mijnen), 2025: 34 kt Ni, 162 kt Cu, Teollisuuskatu 1. https://www.boliden.com/operations/smelters/boliden-harjavalta
[4] Boliden, persbericht 10-3-2016 "Boliden to acquire Kevitsa mine in Finland" — "a nickel feed base load for our Harjavalta smelter". https://investors.boliden.com/sv/node/4123
[5] Boliden, Capital Market Day 2017 (K. Konradsson): "long-term, stable supply of nickel and copper concentrates for Harjavalta and Rönnskär". https://investors.boliden.com/sv/node/4164
[6] VR Logistiikka/Linked, 2018, "Kellontarkkaa rikasteliikennettä Kevitsasta Kemiin" — "lähes 300" km, trein 2×/week naar Harjavalta (concentraatsoort niet genoemd; zelf gelezen). https://logistics.vr.fi/fi/vr-logistiikka/linked/artikkeli/kellontarkkaa-rikasteliikennetta-kevitsasta-kemiin-120420181226/
[7] Yle, 26-4-2021 — ~300.000 t concentraat/j, Ajos → trein → Harjavalta (via PGM-brief, niet opnieuw gelezen). https://yle.fi/a/3-11901777
[8] VR Group, 26-4-2021 — Sodankylä → Harjavalta, 12–13 trucks/dag, 76 t (via PGM-brief). https://www.vrgroup.fi/fi/vrgroup/uutiset/kevitsan-kaivoskuljetusten-tehostamiseksi-loydettiin-uusia-innovaatioita-vr-transpointin-ja-bolidenin-yhteistyo-laajenee-260420210744/
[9] Wikipedia, "Kevitsa mine" — 67.693992, 26.928048 (zoekpunt, niet het anker). https://en.wikipedia.org/wiki/Kevitsa_mine
[10] `v2/design/routebrieven/pgm-kevitsa-harjavalta.md` — ankers, via-punten, satellietblikken (Esri z15/z16, `v2/build-cache/satcheck/sat-pgm-kevitsa-harjavalta-*`), gemeten kilometers van alle vijf benen.
[11] Eigen controle van de vijf geojson (som van haversine-afstanden: 306,6 · 240,4 · 210,1 · 89,6 · 174,2 km; naden 0,00–0,05 km) en de haalbaarheidstoets van de keten.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-nikkel-kevitsa-harjavalta.json` (107,1 KB, versie 2, punt_formaat lonlat) · functie `bak_nikkel_kevitsa_harjavalta` in `v2/tools/bak_stromen.sh` · **totaal 1.020,9 km, 5 benen, 5.640 punten, 3 markers** — precies de verwachting uit de brief.
| # | modaliteit | km | punten | stippel | herkomst |
|---|---|---|---|---|---|
| b1 | truck | 306,6 | 3915 | nee | KOPIE `pgm-kevitsa-harjavalta-weg-kevitsa-ajos.geojson` |
| b2 | spoor | 240,4 | 553 | nee | KOPIE `spoorroute-pgm-kevitsa-harjavalta-ajos-ylivieska` |
| b3 | spoor | 210,1 | 493 | nee | KOPIE `…-ylivieska-seinajoki` |
| b4 | spoor | 89,6 | 119 | nee | KOPIE `…-seinajoki-parkano` |
| b5 | spoor | 174,2 | 560 | nee | KOPIE `…-parkano-harjavalta` |
**Recept:** `bash v2/tools/bak_stromen.sh nikkel-kevitsa-harjavalta` (zwaar-slot). Vijf `--been-geojson`, drie `--marker`; geen eigen wegscan, geen spoorrun, geen zee, aanloop, stippel, lucht of leiding. Functie en LF-controle: 0 CRLF, `bash -n` ok.
**Toets:** km per been gelijk aan de brief (weg +2,2% tegen "lähes 300" VR Linked; spoorkm niet gepubliceerd, dus alleen indicatie). Naden 0,000 / 0,045 / 0,000 / 0,000 km (max 0,05). Markers 0,00 / 0,00 / 0,05 km van hun lijn. `toets_rechte_benen`: geen regel voor deze stroom (geen stippel).
**Knikken (`toets_knikken`):** truck-been 8 spikes van 8–38 m rond de mijn (Sodankylä, mijnweg), geerfd uit de PGM-kopie; spoor b2 één omkering Kemi 65.7318,24.5802 (Ajos-aftakking) en b5 één terugloop Tampere 61.4951,23.7740 (Lielahti, ~0,8 km het station in en terug). Allemaal geerfd, bewust niet gerepareerd (zie §7 en de PGM-brief).
**Aannemelijk, één bron:** in de beennamen b1 en b5 en in de titel; lijnen zijn doorgetrokken.
**Lessen:** een gedeeld been is een letterlijke kopie via `--been-geojson` — geen herbake nodig; kopieen erven ook de knikken van de bron-stroom.
