# Routebrief (licht) · Grafiet · cylib Dormagen → Rotterdam → Vianode Herøya (Duitsland → Noorwegen)

**stroom-id:** `grafiet-dormagen-heroya` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** grafietconcentraat uit cylib's batterijrecycling in Chempark Dormagen (NRW) gaat per **binnenvaartschip** de Rijn af naar Rotterdam (Waalhaven, RHB), per **zeeschip** door de Noordzee en het Skagerrak naar de Langesundsfjord en de kade bij Herøya Industripark (Porsgrunn), en vandaar naar Vianode's Via ONE op hetzelfde terrein. **Aannemelijk: één bron voor de hele relatie** (MoU, zie §7); stoppunt = Via ONE.
**Welke as van het verhaal:** de Europese recyclinglus van batterijgrafiet, Duitsland → Noorwegen. Jaarvolume: **0 kt grafiet/j gedocumenteerd** (peiljaar 2026; MoU van 2-6-2026 noemt geen tonnage [1]). Ter vergelijking: cylib-Dormagen 30 kt batterijen/j nameplate, start gepland 2026 [3]; Via ONE ~2 kt/j (sitelaag [9]).

## 1 · Ketenkaart
```
cylib-plot, Chempark Dormagen (plot niet gepubliceerd) ··(binnen het park, geen been)··
Chempark-Rijnkade `gr-dormagen-kade` ──(b1-b3 binnenvaart · Rijn · 290,7 km gemeten)──► Rotterdam RHB `gr-rotterdam-rhb`
──(b4 zee · MARNET · 927,3 km)──► zeeknoop 4530 (Langesundsfjord) ──(b5 zee · haven-aanloop, stippel, 11,1 km, kopie)──►
Herøya-kade `gr-heroya-kade` ··(0,6 km, binnen het terrein, geen been)·· Vianode Via ONE `gr-vianode-heroya` ⏹
```

## 2 · Benen
Alle benen **aannemelijk (MoU, één bron)**; binnenvaart en zee zijn werkaanname, volume nul — dat staat in de beennaam, niet in de lijnstijl.
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | binnenvaart | `gr-dormagen-kade` → Wesel-vak-eind (51.39994, 6.74551) | Rijn, Rhein-km ~711 → Duisburg-Homberg (stroomafwaarts) | Rhein-km Chempark 709,8-711,4 [5]; gemeten 63,0 (59,6 bulklaag + 2 aansluitstukken van 1,3 en 1,0 km) | `maak_rivierbeen.py` (gedaan, bulklaag; AIS-graaf reikt tot 51,0 N, dus niet tot Dormagen) | nee |
| b2 | A | binnenvaart | Wesel-vak-eind → Emmerich-vak (51.75322, 6.36616) | Rijn — **letterlijke kopie** `rivierbeen-wesel.geojson` (grafiet-molo-duisburg b5), omgekeerde richting | 66,6 [8] | `--been-geojson` (`…-rivier-wesel-omgekeerd.geojson`, zelfde 164 punten gespiegeld) | nee |
| b3 | A | binnenvaart | Emmerich-vak (51.754, 6.366) → `gr-rotterdam-rhb` | Rijn en Nieuwe Maas — kopie van b4 grafiet-molo-duisburg, omgekeerde richting | 161,1 [8] | `--been` over AIS-graaf `rijn` | nee |
| b4 | B | zee | `gr-rotterdam-rhb` → zeeknoop 4530 (59.0498, 9.7056) | Nieuwe Waterweg, Noordzee, Skagerrak | gemeten 927,3 (26 track- + 17 MARNET-edges); geen gepubliceerde zeekm; ontwerpindicatie "orde 1.000" | MARNET `--been zee` | nee |
| b5 | B | zee | zeeknoop 4530 → `gr-heroya-kade` | Frierfjord — **letterlijke kopie** b4 van grafiet-harjavalta-heroya (haven-aanloop, 8,8 km hemelsbreed > 5 km) | 11,1 [7] | `--stippel-geojson` `grafiet-harjavalta-heroya-aanloop-heroya.geojson` | ja — "hier reikt het net niet" |
Totaal ~1.229 km (binnenvaart 290,7 + zee 927,3 + 11,1). Geen weg, spoor, leiding, vlucht, fase D/E of last-mile-been. De ±15%-toets voor b1-b3 is een indicatie: Rhein-km-verschil Ruhrort (~780, eigen kennis, niet bevestigd) → Chempark (~710,6) = ~70 km tegen 63,0 gemeten vanaf het Wesel-vak-eind, dat ~6 km onder Ruhrort ligt; b4 heeft geen publicatie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-dormagen-kade` | overslag Rijn (kop) | Chempark Dormagen, Rijn-oever linkeroever, tankerkade ter hoogte van de tanker-steiger (OSM-piers 51.0765-51.0833, 6.850-6.853) | 51.0768, 6.8531 | [4][5] | **aannemelijk** (z17 gezien: tankerkade met een aangemeerd chemietanker en steigers langs de oever aan de rand van het chemiepark met tankparken en spoorbundel; geen container- of bulkkraan zichtbaar, welke kade grafiet zou laden niet aan te wijzen; cylib-plot zelf niet gelegd, zie §7) |
| `gr-rotterdam-rhb` | overslag binnenvaart → zee | RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4 — hergebruikt uit routebrief-licht §1 en grafiet-molo-duisburg | 51.8935, 4.4585 | [8] | bron-gelegd (letterlijk hergebruikt, niet opnieuw gecheckt) |
| `gr-heroya-kade` | overslag zee → terrein | Herøya zuidwestkade (OSM quay way 4153733) — hergebruikt uit grafiet-harjavalta-heroya | 59.1174, 9.6249 | [7] | bron-gelegd (hergebruikt: kade met loodsen aan de westpunt van het schiereiland) |
| `gr-vianode-heroya` | losplek / anodefabriek (staart) | Vianode Via ONE, Herøya Industripark — sitelaag-anker `w-vianode-heroya` | 59.1228, 9.6245 | [9][2] | bron-gelegd (sitelaag, z15: fabriekshal in Herøya Industripark) |
Zeeknoop (router, geen anker): 4530 (59.0498, 9.7056). `gr-cylib-dormagen` (de fabriek zelf) is **bewust niet gelegd**: 22.000 m² plot binnen een park van 360 ha, nergens gepubliceerd. Negatief anker: de container-terminal van UCT in Zons (Rhein-km 726,0-726,5, 15 km stroomafwaarts) is een ander bedrijf [6]; Chemion's CT DOR II (noordwestdeel van het park) noemt geen Rijnaansluiting [6].

## 4 · Via-punten
Geen: alle landbenen ontbreken (binnenvaart over bulklaag, AIS-graaf en kopieën; zee via MARNET). De bulklaag volgt één doorgaande Rijn; er bestaat geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| cylib Dormagen | cylib | batterijen/zwarte massa → lithium-/metaalzouten + grafietconcentraat (cygraph) | 30 kt batterijen/j, start 2026 (andere bron: 2027); geen grafiettonnage | [3][1] |
| Via ONE, Herøya | Vianode | (secundair + synthetisch) grafiet → anodegrafiet | ~2 kt/j nameplate | [9][2] |

## 6 · Stoppunt
De brief stopt bij Via ONE: het MoU noemt geen volgende stap en Vianode's klanten zijn niet gedocumenteerd voor deze stroom. Fase D valt weg (geen bron voor de afnemer van het anodemateriaal), E vervalt.

## 7 · Open punten
- **Alleen een niet-bindend MoU** (2-6-2026) [1]: noemt noch Dormagen, noch Herøya, noch tonnage, vervoerswijze of datum; cylib wordt er alleen met Aachen genoemd [1]. Dormagen = cylib's eerste industriële plant (bouw sinds 9-2024, start 2026 of 2027, nog niet bevestigd draaiend) [3]; of grafiet nu nog uit het Aachen-pilot komt staat niet vast. Dat het naar Via ONE gaat is de enige Vianode-fabriek-aanname (ook in grafiet-harjavalta-heroya). Vianode test op pilotschaal, mogelijk niet op Herøya. Volume 0 kt.
- **Binnenvaart en zee zijn werkaanname**; alternatief truck naar Hirtshals en feeder. Een Herøya-kade voor een containerschip is niet bevestigd (hergebruikte kade).
- **cylib-plot niet gelegd** (in geen enkele bron een adres of coördinaat; een OSM-scan van NRW op "cylib"/bouwterrein is niet afgerond (te traag op de gedeelde machine), de eerdere haven-scan vond alleen de piers). Het kadepunt is een Chempark-tankerkade; de Chempark-haven is een Stromhafen Rhein-km 709,83-711,4 [5], maar niet bekend is welke ligplaats droog/containergoed krijgt.
- **b1** heeft twee aansluitstukken (1,3 en 1,0 km) omdat de bulklaag-knopen 1 km naast de ankers liggen; hemelsbreed, op de rivier.
- **Zee-lengte** 927,3 km is de router, geen gepubliceerde afstand. De Reuters-melding van 30-9-2026 (Vianode zoekt partner of verkoop) is niet gelezen.
- **Webbudget:** 3 van 3 WebSearch gebruikt; Overpass 429, daarom pyosmium op `de-nrw`.

## 8 · Bronnen
[1] Vianode/cylib, MoU 2-6-2026: recycled graphite concentrate uit OLiC, geen site/volume. https://www.vianode.com/news/vianode-and-cylib-are-joining-forces-to-close-the-loop-on-battery-graphite
[2] Vianode, Via ONE Herøya (bron via grafiet-harjavalta-heroya): https://www.heroya-industripark.no/en/companies-and-businesses-in-the-industrial-park/vianode
[3] cylib: eerste industriële plant Chempark Dormagen, 22.000 m², 30 kt/j, start 2026; water-based lithium and graphite recovery. https://www.electrive.com/2024/09/09/cylib-starts-building-battery-recycling-plant-in-germany en https://www.cylib.de/
[4] OSM (Geofabrik `de-nrw`, ODbL): Chempark Dormagen (relation 8370963, 51.0757, 6.8459), piers way 99180769-99184518 e.a. aan de Rijn.
[5] Bezirksregierung Düsseldorf, Festsetzung Hafen Chempark Dormagen (Stromhafen, linkeroever, Rhein-km 709,83-711,38), via zoekresultaat (document niet zelf geopend).
[6] Chemanager, 20-3-2024, Chemion CT DOR II (15.000 m², 1.000 containers, alleen weg genoemd): https://chemanager-online.com/de/news/chemion-bietet-gefahrgutterminal; Amtsblatt Bezirksregierung 2023 Nr. 8 (UCT Zons, Rhein-km 726,0-726,5).
[7] `v2/design/routebrieven/grafiet-harjavalta-heroya.md` (anker Herøya-kade, b4 haven-aanloop 11,1 km, zeeknoop 4530).
[8] `v2/design/routebrieven/grafiet-molo-duisburg.md` (b4-b5: Rijn-vakken 161,1 + 66,6 km; Waalhaven-anker).
[9] `v2/design/grafiet-sitelaag.json`, site `w-vianode-heroya` (59.1228, 9.6245, ~2 kt/j).
[10] Esri via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-grafiet-dormagen-heroya-{chempark,kade,kade2}.png`.
[11] Eigen meting: `maak_rivierbeen.py` (60,6 km bulklaag), `hecht_marnet route` proefbake in de scratchpad (b1-b5 samen 1.229,1 km, naden 0,0-0,4 km).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
Functie `bak_grafiet_dormagen_heroya` in `v2/tools/bak_stromen.sh` (graaf `rijn`), uitvoer `v2/data/stroomroute-grafiet-dormagen-heroya.json` (19,0 KB, versie 2, lonlat). Recept: `bash v2/tools/bak_stromen.sh grafiet-dormagen-heroya`. Totaal **1.229,1 km, 990 punten, 4 markers**; alle naden 0,00-0,07 km.
| # | modaliteit | km | punten | naad | stippel | bron van de geometrie |
|---|---|---|---|---|---|---|
| b1 | binnenvaart | 63,0 | 334 | - | nee | `grafiet-dormagen-heroya-rivier-dormagen-duisburg.geojson` (maak_rivierbeen, bulklaag + 2 aansluitstukken) |
| b2 | binnenvaart | 66,6 | 164 | 0,00 | nee | `grafiet-dormagen-heroya-rivier-wesel-omgekeerd.geojson` (letterlijke kopie rivierbeen-wesel, gespiegeld) |
| b3 | binnenvaart | 161,1 | 321 | 0,07 | nee | `--been` over AIS-graaf `rijn`, Emmerich-vak → Waalhaven (snap 0,04 / 0,11 km) |
| b4 | zee | 927,3 | 148 | 0,00 | nee | MARNET Waalhaven → zeeknoop 4530 (26 track- + 17 MARNET-edges) |
| b5 | zee | 11,1 | 23 | 0,00 | ja | letterlijke kopie b4 grafiet-harjavalta-heroya (haven-aanloop Herøya) |
Markers: Dormagen-kade (0,0 km van de lijn), Rotterdam RHB (0,11 km), Herøya-kade (0,0 km), Via ONE (0,6 km: staartanker binnen het terrein, geen been, zoals de brief zegt).
**Toelichting stippel:** alleen b5 is stippel: MARNET reikt niet tot de Herøya-kade (zeeknoop 4530 ligt 8,8 km hemelsbreed, > 5 km), dus een haven-aanloop, hergebruikt van harjavalta-heroya. "Aannemelijk: één bron (MoU)" staat in de beennamen en markernamen, niet in de lijnstijl. Geen weg, spoor, leiding, vlucht of last-mile-been.
**Toets (§5):** b1 63,0 km tegen indicatie ~70 (-10%, eigen kennis Rhein-km, geen wegkm: indicatie, niet norm); b2 en b3 identiek aan de kopieën uit molo-duisburg (66,6 / 161,1); b4 geen publicatie (router 927,3). Geen naad > 5 km. `toets_knikken`: 15 knikken, 2 omkeringen (Emmerich 175/155 gr, 11 m, de bekende Emmerich-kruising van de kopie), 0 teruglopen; de spikes zijn AIS-tracks (Waalhaven, Nijmegen, Nieuwe Waterweg) en zee bij Hoek van Holland, ongewijzigd t.o.v. de moederstroom. `toets_rechte_benen`: geen treffer voor deze stroom behalve de stippel b5 (bedoeld).
**Lessen:** (1) de functie stond al in `bak_stromen.sh` uit de ontwerpronde; de bak-agent heeft alleen de beennaam b1 gecorrigeerd ("stroomafwaarts", Rhein-km loopt stroomafwaarts op) en herbakken; (2) gedeelde Rijn-benen en de Herøya-aanloop zijn kopieën, geen nieuwe geometrie; (3) de gemeten km's van b2, b3 en b5 zijn dezelfde als bij de bronstromen, dus geen nieuwe ±15%-toets mogelijk behalve b1.
