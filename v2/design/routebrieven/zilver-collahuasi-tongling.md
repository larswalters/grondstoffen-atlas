# Zilver · Collahuasi → Patache → Tongling (Chili → China)

**stroom-id:** `zilver-collahuasi-tongling` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** zilver in het kopersulfide-concentraat van Collahuasi (Glencore 44%, Anglo American 44%),
per eigen **slurryleiding** (192,4 km gekarteerd + 0,9 km stippel) naar Puerto Patache, daar gefilterd en per **bulkcarrier** (Stille Oceaan,
rechtstreeks, geen hub) naar de Yangtze-monding, per **binnenvaart** door de oostgeul naar de kade van de TNMG-smelter in Tongling, waar het zilver als
bijproduct (goud/zilver) in de edelmetaalstroom van de smelter terechtkomt (**aannemelijk: één bron** voor de afname, zie §7). Geometrie = letterlijke kopie van benen 1-5 van `koper-collahuasi-tongling`.
**Welke as van het verhaal:** Chileens koperconcentraat met zilver door een gekarteerde slurryleiding naar een Chinese Yangtze-smelter.
Volume: Collahuasi **2.281 koz Ag in concentraat in 2025 (Glencore-aandeel 44%) = 70,9 t; 100%-basis ca. 161 t Ag/j** (peiljaar 2025; 2024: 3.657 koz = 113,8 t, 100% ca. 259 t) [1];
H1 2026: 858 koz (26,7 t, 44%) [2]. Aandeel naar Tongling niet gepubliceerd.

## 1 · Ketenkaart
```
Collahuasi, pompstation kop leiding `ag-collahuasi-pomp`
  ──(b1 leiding · slurry, OSM-tracé 192,4 km · b2 laatste 0,9 km stippel)──►
  Puerto Patache, indikkers/filter → laadsteiger `ag-patache-kade`
  ──(b3 haven-aanloop 77,9 stip · b4 zee 18.511,6 MARNET, aannemelijk: één bron)──►
  Yangtze-monding `ag-yangtze-monding`
  ──(b5 binnenvaart · Yangtze, oostgeul · 516,5)──► TNMG-smelterkade, Tongling `ag-tongling-kade`  ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | pompstation → eind OSM-kartering | slurryleiding Collahuasi-Patache (14 OSM-ways `substance=slurry`) | 192,4 gemeten (±200 gepubliceerd, -3,8%) [3] | `leidingbeen-collahuasi-patache.geojson` (kopie koper b1) | nee |
| b2 | A | leiding | eind kartering → Patache-pier | laatste 736 m, terminalvlak | 0,9 | stippel, kopie koper b2 | ja: kartering houdt op |
| b3 | B | zee | Patache-pier → MARNET-zeeknoop (-20.2313, -70.6311) | haven-aanloop Patache | 77,9 | stippel, kopie koper b3 | ja: MARNET reikt hier niet |
| b4 | B | zee | zeeknoop → Yangtze-monding (31.5100, 121.4187) | Stille Oceaan, rechtstreeks | 18.511,6 [3] | MARNET (kopie koper b4) | nee |
| b5 | C | binnenvaart | Yangtze-monding → Tongling-kade | Yangtze, oostgeul | 516,5 [3] | `rivierbeen-yangtze-tongling-gedeeld.geojson` (kopie koper b5) | nee |
Totaal **19.299,3 km**, 5 benen. Geen been 6-7 van de koperbrief (kathode-trucks, foliefabriek): zilver verlaat de smelter niet als kathode (§6). Haven-aanloop b3 staat er verplicht: 77,9 km > 5 km.

## 3 · Ankers (één per site en per overslag; alle vier hergebruikt letterlijk uit `koper-collahuasi-tongling`)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-collahuasi-pomp` | mijn, kop b1 | Collahuasi, pompstation kop slurryleiding | -20.97783, -68.64395 | [3][sat] | bron-gelegd (z15 gezien: klein pompcomplex met drie donkere bekkens en een gebouw, tegen de mijninstallaties; Rosario-put 1,6 km zuidoost; hergebruik koper `cu-collahuasi-laad`) |
| `ag-patache-kade` | overslag leiding → zee | Puerto Patache, kop laadsteiger | -20.80270, -70.19890 | [3][sat] | bron-gelegd (z15 gezien: filter-/opslagterminal met overdekte stockpiles, smalle steiger NW de zee in, anker aan de kop; noordelijker tweede pier met schip is de kolenterminal; hergebruik `cu-patache-kade`) |
| `ag-yangtze-monding` | overgang zee → rivier | Shanghai/Luojing, Yangtze-monding | 31.42704, 121.47618 | [3][sat] | bron-gelegd (z14 gezien: pier aan de monding naast de staalwerf Luojing, schepen op de rede; hergebruik) |
| `ag-tongling-kade` | afnemer / losplek | TNMG-smelter Tongling, kade oostgeul | 30.98656, 117.77180 | [3][4][sat] | aannemelijk: één bron (z15 gezien: kade met bargeschepen en kolen-/ertsvelden direct aan de oostoever, smelter-/industrieterrein erachter; hergebruik `cu-tongling-kade`) |

## 4 · Via-punten
Geen: alle benen zijn letterlijke kopieën van gebakken geometrie (leiding en rivier: geojson; zee: MARNET). Er is geen wegbeen, geen spoor en geen extract nodig.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Collahuasi-concentrator + Patache-filterplant | Collahuasi (Glencore 44%, Anglo American 44%) | sulfide-Cu-concentraat met Ag → gefilterd concentraat | Ag 2.281 koz (44%) in 2025 | [1][3] |
| TNMG-smelter, Tongling (金冠 + 金新) | Tongling Nonferrous | concentraat → anode/kathode + goud en zilver als bijproduct | 金新: 500 kt/j kopermateriaal "en goud, zilver als bijproduct" | [4] |

## 6 · Stoppunt
Stopt bij de TNMG-smelterkade: de bron noemt voor de smelter alleen goud/zilver als bijproduct, geen edelmetaalraffinage of volgende locatie, en zilver verlaat de smelter niet als kathode; fase D/E vervallen en de koper-benen 6-7 (kathode-trucks, foliefabriek) worden bewust niet gekopieerd.

## 7 · Open punten
- **Collahuasi → Tongling is een aanname:** geen bron koppelt Collahuasi-concentraat aan TNMG. Enige onderlegger: TNMG-analistenrapport (Guosen 2023) dat geimporteerd concentraat bij Nantong lost en per Yangtze naar het bedrijf gaat (overgenomen uit koperbrief D4, niet opnieuw geopend) [5]; zoektocht naar een Collahuasi-TNMG-contract (Chinees zoekwerk) leverde niets. Daarom **aannemelijk: één bron** in titel en beennamen.
- **Ag is "silver in concentrates" (gehalte, geen payable):** Glencore geeft het zilver in concentraat [1][2]; hoeveel de smelter uitbetaalt en terugwint is niet gepubliceerd. TNMG-zilverproductie in ton niet gevonden (alleen "goud, zilver als bijproduct" [4]).
- **Volume-spreiding:** Glencore 2025 (161 t/j, 100%) tegen 2024 (259 t) en GlobalData-schatting 8,65 Moz in 2023 (269 t, secundair) [6]; sitelaag `w-collahuasi-ag` zet 180 t Ag/j op -20.9914, -68.6386 (1,6 km van `ag-collahuasi-pomp`, in de Rosario-put): centraal gelijktrekken.
- **Nantong-losligplaats, espesadores en Patache-terreinsplitsing** blijven open (koperbrief §5.1-5.4); geen coordinaat verzonnen. Naad zee-eind (31.5100, 121.4187) naar riviersbegin is ca. 1,8 km en de marker `ag-yangtze-monding` ligt ca. 4,5 km van de lijn (beide overgenomen uit de koperstroom).
- **Overlap:** geometrie 100% gelijk aan koper-collahuasi-tongling b1-b5; thema Chili-China gedeeld met zilver-escondida-guixi (andere mijn, haven, smelter).

## 8 · Bronnen
[1] Glencore, Full Year 2025 Production Report, 29-1-2026 (Collahuasi "silver in concentrates" 2.281 koz in 2025 tegen 3.657 koz in 2024; 44% pro-rata aandeel):
https://www.glencore.com/.rest/api/v1/documents/static/a8114247-02e8-4bd8-bc04-81f411ba631c/GLEN_2025-FY-Production-Report.pdf
[2] Glencore, Half-Year Production Report 2026, 29-7-2026 (Collahuasi Ag 858 koz H1 2026 tegen 1.103 koz H1 2025):
https://www.glencore.com/.rest/api/v1/documents/static/e44bf57f-8768-4b27-8a33-39087d02d00a/GLEN_2026-H1ProductionReport.pdf
[3] Routebrief `v2/design/routebrieven/koper-collahuasi-tongling.md` (ankers, benen 1-5, OSM-leiding 192,4 km, Z1/Z2, P1/P2, T1) en `v2/data/stroomroute-koper-collahuasi-tongling.json` (geometrie).
[4] CNR/央广网, 铜陵有色金新铜业铜基新材料项目点火, 26-3-2025 (500 kt/j hoogwaardig kopermateriaal en goud, zilver als bijproduct): https://www.cnr.cn/ah/jhfc/20250326/t20250326_527113743.shtml
[5] Guosen Securities, rapport 铜陵有色 000630.SZ, 22-12-2023, via koperbrief D4: https://pdf.dfcfw.com/pdf/H3_AP202312221614826947_1.pdf
[6] Mining Technology/GlobalData, "five largest silver mines in Chile" (Collahuasi ca. 8,65 Moz in 2023, secundair): https://www.mining-technology.com/marketdata/five-largest-silver-mines-chile/
[sat] Esri World Imagery via `v2/tools/sat_check.py`, z14-z15, 2026-10-31: `v2/build-cache/satcheck/sat-zilver-collahuasi-tongling-{pomp,patache,monding,tongling}.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Functie:** `bak_zilver_collahuasi_tongling` in `v2/tools/bak_stromen.sh` · **uitvoer:** `v2/data/stroomroute-zilver-collahuasi-tongling.json` (115,1 KB, versie 2, lonlat) · **register:** sleutel `ag-cot`.
**Recept:** letterlijke kopie van benen 1-5 van `koper-collahuasi-tongling` (zelfde geojson in `$BEEN`, zelfde stippels, zelfde coordinaten), zonder b6/b7. Geen extract, geen profiel, geen weg/spoor/vlucht, geen via-punten, geen slotgebruik buiten de bake.

| # | modaliteit | km | stippel | naad naar vorige |
|---|---|---|---|---|
| b1 | leiding (OSM-slurryleiding, 1.363 pt) | 192,4 (brief 192,4; ca. 200 gepubliceerd) | nee | - |
| b2 | leiding (laatste 736 m) | 0,9 | ja: kartering houdt op | 0,00 |
| b3 | zee, haven-aanloop Patache | 77,9 | ja: MARNET reikt niet | 0,00 |
| b4 | zee, MARNET Patache-zeeknoop -> Yangtze-monding (1.898 pt) | 18.511,6 | nee | 0,00 |
| b5 | binnenvaart, Yangtze oostgeul (2.674 pt) | 516,5 | nee | 1,82 |
Totaal **19.299,3 km**, 5 benen, 4 markers (`ag-collahuasi-pomp`, `ag-patache-kade`, `ag-yangtze-monding`, `ag-tongling-kade`). Alle km komen exact overeen met de brief en met de koperstroom.

**Toelichting per stippel/aanloop/leiding:**
- b1 doorgetrokken: OSM heeft de slurryleiding (14 ways). 192,4 km tegen ca. 200 gepubliceerd = -3,8%, binnen de norm.
- b2 stippel 0,9 km (de kartering stopt 736 m voor het terminalvlak; hemelsbreed 0,89 km).
- b3 haven-aanloop Patache: kade 77,9 km van de zeeknoop (-20.2313, -70.6311), MARNET reikt niet, rechte stippel zoals koper b3 (geen `maak_havenaanloop.py`-run, kopie).
- b4 MARNET: beide uiteinden snappen op 0,000 km.

**Bevindingen (geerfd van koper, niets verschoven):** naad zee-eind (31.5100, 121.4187) naar riviersbegin (31.5149, 121.4004) = 1,82 km (< 5 km); marker `ag-yangtze-monding` ligt 4,45 km van de dichtstbijzijnde lijnpunt (anker-conventie, niet het routeerpunt); marker `ag-tongling-kade` 0,40 km. `toets_knikken.py`: 12 knikken >= 60 gr, 0 omkeringen en 0 terugloop (de spikes liggen in het OSM-leidingtracé en op de krappe bochten bij Patache, het is echte kartering). `toets_rechte_benen.py --min-km 5`: alleen b3 (stippel, bewust recht).
**Lessen:** (1) een kopie van een koper-recept is in een paar minuten gebakken zodra de geojson in `$BEEN` staan; (2) een parallelle edit van een andere agent aan `bak_stromen.sh` tijdens de bake gaf een bash-melding ("beennaam,: command not found", regel ~15465) uit andermans functie, na het schrijven van mijn json; geen invloed op de uitvoer; (3) Sitelaag `w-collahuasi-ag` (-20.9914, -68.6386) ligt 1,6 km van het pompstation: centraal gelijktrekken (zie §7).
