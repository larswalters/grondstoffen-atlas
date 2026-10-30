# Routebrief (licht) · gas — Komotini (Griekenland) → Stara Zagora (Bulgarije) — Interconnector Griekenland-Bulgarije (IGB)

**stroom-id:** `gas-komotini-starazagora` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) ·
**status:** gebakken
**Keten in één zin:** Gas uit de Zuidelijke Gascorridor (Azerbeidzjaans Shah Deniz-gas via TAP, daarnaast LNG uit Griekse terminals) takt bij Komotini
af van het Griekse net en TAP en gaat door één doorlopende DN800-leiding (Thracie, Bulgaarse grens, Zuid-Bulgarije)
naar het Bulgartransgaz-meetstation bij Stara Zagora; sinds Bulgarije in 2022 Gazprom verloor is dit de zuidelijke toevoer.
**Welke as van het verhaal:** Zuidelijke Gascorridor naar Zuidoost-Europa — 3 bcm/j capaciteit (uitbreiding naar 5 bcm/j vergund, fase 1) [1][2][5];
werkelijke doorzet 2025 ca. 1 bcm/j (6,74 TWh in jan-aug 2025 [4], eigen omrekening) en ruim 40% van de Bulgaarse winter- en 60% van de zomervraag [3].

## 1 · Ketenkaart
```
TAP/DESFA-net bij Komotini ──► `gas-komotini-igb-begin` (IGB-begin, meetstation)
   ──(b1 leiding · IGB: Komotini → Bulgaarse grens (way 919860052 + 1076969894, 81,1 km OSM) → ICGB-way 826478838 (100,9 km) · 182,0 km OSM)──►
`gas-starazagora-igb-eind` (Bulgartransgaz-meetstation) — stoppunt (daarna Bulgaars net en Trans-Balkan-leidingen, niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | leiding | `gas-komotini-igb-begin` → `gas-starazagora-igb-eind` | IGB / ICGB, DN800 (813 mm): Komotini → Bulgaarse grens → Stara Zagora | 182,6 gepubliceerd (31 GR + 151 BG) [2] → OSM 182,0 (-0,3%) | OSM-ways `man_made=pipeline`, substance=gas: 919860052 (31,0 km) omgedraaid, 1076969894 (50,1 km) omgedraaid, 826478838 `name=ICGB` (100,9 km), exact aaneengesloten (knopen 41.2756,25.4405 en 41.6293,25.4263), gestikt tot één FeatureCollection | nee |

Beennaam voor de bake: *Interconnector Griekenland-Bulgarije (IGB) Komotini naar Stara Zagora (Griekenland, Bulgarije; aannemelijk: één bron)*.
Correctie op het ketenontwerp: het Griekse deel is WEL gekarteerd (geen stippel, geen losse Griekse leg). De twee zuidelijke ways zijn onbenoemd en dragen
`construction=yes`, `source=sentinel imagery 20210301` (verouderde bouwtag; de leiding draait sinds 1 okt 2022 [2]) — de geometrie is dezelfde leiding en
de som (182,0 km) valt samen met de gepubliceerde 182 km, dus doorgetrokken.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-komotini-igb-begin` | leiding-kop / meetstation (aansluiting TAP/DESFA) | IGB-begin, Komotini (Grieks Thracie) | 41.0621, 25.4864 | [2][4][6][7] | aannemelijk (z15 gezien: zuidrand van het industrieterrein Komotini bij een gascentrale met twee ronde tanks en schakelstation; 0,7 km west een tweede ommuurd platform, waarschijnlijk het TAP-station; welke installatie het IGB-meetstation is, is niet aan te wijzen) |
| `gas-starazagora-igb-eind` | leiding-staart / meetstation (aansluiting Bulgartransgaz) | IGB-einde, Stara Zagora (Bulgarije) | 42.3625, 25.7029 | [2][5][6][7] | aannemelijk (z15 gezien: open akkerland, een klein ommuurd platform met toegangspad ~0,3 km ZZW van het punt, dorp ~0,7 km noord; consistent met een klein meetstation) |

Hergebruik: geen. De sitelaag (`gas-sitelaag.json`) en eerdere brieven kennen Komotini en Stara Zagora niet; TAP-eind Kipoi (`gas-kipoi-melendugno`) ligt ~70 km oost
en is niet hergebruikt. Beide ankers zijn de OSM-leidinguiteinden: kop 0,00 km, staart 0,00 km van de lijn, geen last-mile (platform < 0,5 km).
Beelden: `v2/build-cache/satcheck/sat-gas-komotini-starazagora-komotini.png`, `sat-gas-komotini-starazagora-starazagora.png` [8].

## 4 · Via-punten
Niet van toepassing: één leidingbeen uit aaneengestikte OSM-ways (geen corridorkeuze zoals bij weg/spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Komotini-meetstation | ICGB (IGI Poseidon 50%, Bulgarian Energy Holding 50%) | Grieks net/TAP-gas → IGB | 3 bcm/j; opwaardering (lot 2) loopt | [2][3][5] |
| Stara Zagora-meetstation | ICGB / Bulgartransgaz | IGB → Bulgaars net | 3 bcm/j; opwaardering (lot 1, vergund aug 2025) naar 5 bcm/j | [2][5] |

## 6 · Stoppunt
De brief stopt bij het meetstation Stara Zagora: het invoedingspunt in het Bulgaarse net, waarna het gas anoniem Bulgartransgaz-netgas is (afnemers: Bulgarije,
Noord-Macedonie, Roemenie, Servie, Hongarije, sinds 2024 Slowakije, Moldavie, Oekraine [1]). Stroomopwaarts is niet getekend: TAP/Shah Deniz zie `gas-kipoi-melendugno`.

## 7 · Open punten
- **Geen kalenderjaar-volume van ICGB gevonden:** 34,5 mln MWh sinds de start eind 2022 t/m jun 2025 [3] en 6,74 TWh jan-aug 2025 [4]; omrekening naar ca. 1-1,3 bcm/j (10,5 kWh/m3) is mijn eigen rekensom, calorische waarde onbekend. 3 bcm/j is capaciteit.
- **Herkomst per molecuul:** Azerbeidzjaans via TAP [1][2], maar IGB kan ook LNG uit Griekse terminals doorvoeren (Revithoussa, Alexandroupolis); geen bron voor het aandeel.
- **Meetstations niet aangewezen:** het exacte meetstation-terrein bij Komotini en Stara Zagora is op z15 niet scherp te onderscheiden; ankers zijn de OSM-leidinguiteinden.
- Geen overlap met `gas-kipoi-melendugno` (toets: < 5% binnen 2 km); aansluiting op TAP bij Komotini niet als eigen been getekend.
- Gepubliceerde lengte wisselt per bron (Wikipedia 160-180 km, GEM 182, Europese Commissie 185, ICGB 182,6 [2][3]); OSM-som 182,0 km sluit aan bij ICGB.

## 8 · Bronnen
[1] Wikipedia (EN), "Gas Interconnector Greece-Bulgaria" — operationeel 1 okt 2022, 3-5 bcm/j, Komotini-Stara Zagora, ~30 km GR + ~150 km BG, klanten 2024. https://en.wikipedia.org/wiki/Gas_Interconnector_Greece%E2%80%93Bulgaria
[2] ICGB, "Infrastructure" — 182,6 km (31 GR, 151 BG), DN800, 3 bcm/j, EPC 28-10-2019, COD 1-10-2022. https://www.icgb.eu/infrastructure-operation/infrastructure/
[3] IENE, 07-06-2025, "Greece-Bulgaria gas link now covers over 60% of Bulgaria's summer supply" — >34,5 mln MWh sinds start, 60% zomer / ~40% winter, ~2 mln MWh virtuele reverse flow. https://www.iene.eu/energy-news/greecebulgaria-gas-link-now-covers-over-60-of-bulgarias-summer-supply-p7859.html
[4] Trend.az, 12-09-2025 — IGB aug 2025 888.790,92 MWh; jan-aug 2025 6.737.566,58 MWh richting Bulgarije; aansluiting op TAP bij Komotini. https://www.trend.az/business/energy/4089777.html
[5] Pipeline & Gas Journal, 11-2025, "Greece-Bulgaria interconnector granted expansion permit" — 3 naar 5 bcm/j, lot 1 Stara Zagora-meetstation, lot 2 Komotini-meetstation. https://pgjonline.com/news/2025/august/greece-bulgaria-interconnector-natural-gas-pipeline-granted-expansion-permit
[6] OpenStreetMap-bijdragers (ODbL), via api.openstreetmap.org (2026-10-30) — ways 919860052, 1076969894, 826478838 (name=ICGB, operator ICGB, diameter 813). https://www.openstreetmap.org/way/826478838
[7] Global Energy Monitor wiki, "Gas Interconnector Greece-Bulgaria (IGB)" — 182 km, Azerbeidzjaans gas via TAP, eigenaren IGI Poseidon/BEH. https://www.gem.wiki/Gas_Interconnector_Greece_-_Bulgaria_(IGB)
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15, live, 2026-10-30).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-gas-komotini-starazagora.json` (17,4 KB, versie 2, lonlat) · **1 been · 182,0 km · 866 punten · 2 markers** · naden n.v.t. (één been).
Recept: `bak_gas_komotini_starazagora()` in `v2/tools/bak_stromen.sh`; geometrie via `v2/tools/maak_leidingbeen_gas_komotini_starazagora.py` (OSM-API, ways 919860052 omgedraaid + 1076969894 omgedraaid + 826478838, naden 0 m) → `v2/build-cache/ais/graaf/gas-komotini-starazagora-leiding-igb.geojson` (FeatureCollection met één LineString).
| # | modaliteit | km gemeten | km brief | afwijking | stijl |
|---|---|---|---|---|---|
| b1 | leiding (IGB/ICGB DN800) | 182,0 | 182,6 (ICGB) | -0,3% | doorgetrokken |
Markers: `gas-komotini-igb-begin` (41.0621, 25.4864; 0 m van de lijn) en `gas-starazagora-igb-eind` (42.3625, 25.7029; ca. 10 m van de lijnuiteinde). Beide status aannemelijk (OSM-leidinguiteinden).
**Toelichting:** geen stippel, geen haven-aanloop, geen vlucht, geen via-punten, geen gedeeld been, geen wegscan: het Griekse deel is wel gekarteerd, dus doorgetrokken. Eindpunt = id (Stara Zagora). De twee zuidelijke ways dragen verouderde `construction=yes` (sentinel 2021); de leiding draait sinds 1 okt 2022, geometrie is dezelfde leiding en de som sluit aan op de gepubliceerde 182 km.
**Toetsen:** `toets_knikken.py` 53 knikken >= 60 graden (OSM-pijplijnbochten, krappe bocht/spike), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py` meldt dit been niet; json.load ok, modaliteit leiding, bestand 17,4 KB; `bak_stromen.sh` blijft LF (0 CRLF).
**Lessen:** een lang OSM-leidingbeen met ways in vaste volgorde is in één script te stikken (nybro-patroon, richting per way afgedwongen op het kopanker); een bewust ontbrekende bundel/register-stap blijft centraal.
