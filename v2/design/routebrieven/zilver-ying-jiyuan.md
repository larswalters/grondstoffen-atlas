# Zilver · Silvercorp Ying → Luoyang → Yuguang Gold and Lead, Jiyuan (China)

**stroom-id:** `zilver-ying-jiyuan` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** zilver in het lood-zilverconcentraat van Silvercorp's Ying-molens (Luoning, Henan) gaat per **truck** over Yi-Gu-weg/S249, G3615, Luoyang en de Gele Rivier-brug bij Mengjin (S240) naar de loodsmelter Henan Yuguang Gold and Lead in Jiyuan; de keten stopt daar (**aannemelijk: één bron** voor de bestemming, zie §7).
**Welke as van het verhaal:** *China als mijnland: de grootste Chinese primaire zilvermijn voedt een Chinese loodsmelter.* Volume: Silvercorp FY2026 (jaar tot 31-03-2026) 6,803 Moz Ag = ca. 212 t Ag/j, waarvan **Ying 6,345 Moz = ca. 197 t Ag/j** (1 Moz = 31,1 t) [1]; het deel dat Yuguang bereikt is niet gepubliceerd. Peiljaar 2025/26.

## 1 · Ketenkaart
```
Ying-molencomplex (Plant 1 Xiayu + Plant 2 Zhuangtou) `ag-ying-molen`  (onzeker→aannemelijk)
  ──(b1 truck · Yi-Gu-weg/S249 → G3615 Luoning → Luoyang → Mengjin/S240 · OSRM 188 indicatie, gemeten 189,9 · aannemelijk: één bron)──►
Henan Yuguang Gold and Lead, Kejing, Jiyuan `ag-yuguang-smelter`  ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Ying-molen → Yuguang Gold and Lead, Jiyuan | Yi-Gu-weg/S249 → G3615 → Luoyang → S240 (aannemelijk: één bron) | **hemelsbreed 150 km, geen wegkm**; OSRM-routelengte 188 km (indicatie, geen bedrijfsopgave); TR 2022: Luoning 56 km verhard, smelters "binnen 210 km straal" [2]; bake 189,9 km weg | `maak_stroombeen_weg.py`, profiel `zilver-ying-jiyuan-molen-yuguang` | nee (zie §7 voor de 1,6 km-stub aan de molen) |
Totaal ca. 191,9 km (189,9 weg + 1,6 stub bij de molen + 0,5 stub bij de smelter), 1 been. Geen fase B-E: geen zee, spoor of leiding.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-ying-molen` | mijn/molen (kop b1) | Silvercorp Ying-molencomplex (Plant 1 Xiayu + Plant 2 Zhuangtou), Luoning | 34.2374, 111.3324 | [2][3][sat] | **aannemelijk** (z15/z16 gezien: molencomplex met blauwe daken en erts-silo's, twee afzinkvijvers 0,6-1,1 km ZO/N, betonweg zuidwaarts; ligt 2,7 km NO van het Xiayu-stadscentroïde, TR zegt "ca. 3 km NO van Xiayu"; geen bron geeft een coördinaat; het eerdere toets-kandidaatpunt 34.2418,111.3295 bleek bos, 0,5 km ernaast) |
| `ag-yuguang-smelter` | smelter (staart b1) | Henan Yuguang Gold and Lead (豫光金铅), Kejing, Jiyuan | 35.1375, 112.5575 | [4][5][sat] | **bron-gelegd** (z15 gezien: groot industrieterrein met fabriekshallen en tegen de zuidrand spoorbundels; OSM landuse=industrial, name 豫光金铅, way 684183239, bbox 35.1317-35.1433 / 112.5525-112.5627, Nominatim 35.1378,112.5580) |

## 4 · Via-punten (alleen b1, corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | S249 ten NO van de molen | 34.3289, 111.4470 | pint de uitgang uit het molendal naar Luoning over de S249; snap 0,0 km |
| b1 | 2 | G3615 bij Luoning | 34.3958, 111.7150 | de doorgaande weg Luoning → Luoyang (G3615), vóór de bergen; ref G3615 |
| b1 | 3 | doorgaande weg N van Luoyang | 34.7146, 112.4364 | Luo-oversteek aan de rand van Luoyang, bewust niet in het stadscentrum (34.66, 112.45) |
| b1 | 4 | S240 bij de Gele Rivier-brug (Mengjin) | 34.9297, 112.5197 | kiest Mengjin boven Xiaolangdi voor de Gele Rivier-oversteek; ref S240 |
Extracts: `china` (Geofabrik, 1,6 GB). Refs (zachte voorkeur): S249, G3615, S240. Vlaggen `eindToegangPrivaat` en `trimStaart` aan, `vensterKm` 40.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ying-molens (Plant 1 Xiayu, Plant 2 Zhuangtou) | Silvercorp | erts → lood-zilver- en zinkconcentraat | 4.000 tpd ontwerp; FY2026 1.475.512 t erts, 6,803 Moz Ag (Ying 6,345) | [1][2][3] |
| Yuguang Gold and Lead, Jiyuan | Henan Yuguang Gold & Lead | loodconcentraat → lood, zilver (edelmetaal) | "grootste zilverproducent van China" (zh.wikipedia); geen tonnage gevonden | [2][6][7] |

## 6 · Stoppunt
Stopt bij de Yuguang-smelter: zilver verlaat Jiyuan als edelmetaalproduct zonder gedocumenteerde volgende locatie, dus fase D/E vervallen. De onzekerheid ("aannemelijk: één bron") staat in de beennaam en hier, niet in de lijnstijl.

## 7 · Open punten
- **Bestemming één bron:** alleen TR 2022 §19.3 noemt Yuguang Gold and Lead als loodafnemer, naast Jiyuan Wanyang, Jiyuan Jinli, Lingbao Xinling en Anyang Minshan [2]; het FY2026-document zegt alleen "smelters in Henan en Shaanxi" [1]. Hoeveel van de 197 t Ag Yuguang bereikt staat nergens. Yuguang Zinc (zinkconcentraat) is een ander bedrijf en niet getekend.
- **Molenanker aannemelijk:** geen coördinaat in een bron of in OSM (Nominatim en china-pbf-scan leeg); de plek volgt uit de TR-afstandsbeschrijving plus het enige molencomplex op de satelliet. Of Plant 1 en 2 (binnen 2 km van elkaar) beide op dit terrein staan is niet apart gezien.
- **Wegkm niet gebrond:** 188 km is een OSRM-lengte, geen bedrijfsopgave; de ±15%-toets (189,9 km gemeten, +1%) is een indicatie, geen norm. Welke brug (Mengjin of Xiaolangdi) de vrachtwagens echt nemen is niet gebrond.
- **Stub aan de molen:** de molen snapt 1,57 km van de dichtstbijzijnde OSM-weg (de 2 km betonweg naar de Yi-Gu-weg uit TR §18.4 staat niet in OSM); het stuk is een rechte stub binnen de 2 km-regel en geen stippel. Aan de smelterkant 0,46 km stub.
- **Sitelaag:** Silvercorp Ying ontbreekt in `zilver-sitelaag.json`; centraal bijwerken (Ying 197 t Ag/j, `ag-ying-molen`).

## 8 · Bronnen
[1] Silvercorp, 40-F FY2026, exhibit 99.1 (Ying 6,345 Moz Ag, groep 6,803 Moz; concentraten naar smelters in Henan en Shaanxi), 2026-06-30: https://www.sec.gov/Archives/edgar/data/1340677/000110465926079021/svm-20260331xex99d1.htm
[2] AMC, NI 43-101 Technical Report Update Ying (2022): Luoning 56 km verhard, molens ca. 3 km NO van Xiayu, concentraten per truck binnen 210 km, smelterlijst §19.3: https://www.sec.gov/Archives/edgar/data/1340677/000117625622000187/exhibit99-17.htm
[3] Silvercorp, Ying Mining District (6,3 Moz Ag FY2026, 4.000 tpd, verkoop aan lokale smelters): https://silvercorpmetals.com/operations/ying-mining-district/
[4] OSM, way 684183239 (landuse industrial, 豫光金铅, Kejing, Jiyuan) via Nominatim: https://nominatim.openstreetmap.org/lookup?osm_ids=W684183239&format=json
[5] OSM, relation 14117968 (下峪镇/Xiayu, centroïde 34.2192,111.3131) via Nominatim: https://nominatim.openstreetmap.org/search?q=Xiayu+Luoning&format=json
[6] zh.wikipedia, 济源市 (豫光金铅: grootste loodsmelter, grootste zilverproducent van China): https://zh.wikipedia.org/wiki/济源市
[7] Wikipedia, Lead poisoning in China (China's largest smelter plant, Yuguang Gold and Lead): https://en.wikipedia.org/wiki/Lead_poisoning_in_China
[sat] Esri World Imagery via `v2/tools/sat_check.py`, z15/z16, 2026-10-30: `v2/build-cache/satcheck/sat-zilver-ying-jiyuan-molen.png`, `-molen2.png`, `-yuguang.png`

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
Bestand `v2/data/stroomroute-zilver-ying-jiyuan.json` (34,3 KB, contract versie 2, lonlat), functie `bak_zilver_ying_jiyuan` in `v2/tools/bak_stromen.sh`, profiel `zilver-ying-jiyuan-molen-yuguang` in `maak_stroombeen_weg.py`.

| been | modaliteit | km gemeten | km brief | stippel |
|---|---|---|---|---|
| b1 | truck, Ying-molen naar Yuguang Gold and Lead, Jiyuan (aannemelijk: een bron) | 191,9 (189,9 weg + 1,6 stub molen + 0,5 stub smelter) | hemelsbreed 150, OSRM 188 (geen wegkm): +2% op OSRM, indicatie | nee |

Totaal 191,9 km, 1 been, 1.657 punten, 2 markers (ag-ying-molen, ag-yuguang-smelter), beide op 0,0 km van de lijn. Geen naden (1 been).
**Recept:** wegscan via `wegscan_puur.py --profiel zilver-ying-jiyuan-molen-yuguang` (extract china, vensterKm 40, refs S249/G3615/S240, eindToegangPrivaat en trimStaart aan, 4 via-punten), geojson in `build-cache/ais/graaf/zilver-ying-jiyuan-weg-molen-yuguang.geojson`, daarna `bash v2/tools/bak_stromen.sh zilver-ying-jiyuan` (tweede bake bevestigde 191,9 km).
**Toelichting:** geen stippel, haven-aanloop, vlucht, leiding of kopie. De molen snapt 1,57 km van de OSM-weg: rechte stub binnen de 2 km-regel (betonweg uit TR par 18.4 staat niet in OSM); smelterkant 0,46 km stub. `toets_knikken`: 13 knikken >= 60 gr (OSM-aansluitingen en op- en afritten), 0 omkeringen, 0 terugloop. De km-toets is geen norm: 188 km is een OSRM-lengte, geen bedrijfsopgave.
**Lessen:** (1) bij een molen zonder broncoördinaat blijft het anker aannemelijk en de stub kort; (2) via-punten buiten Luoyang en Mengjin op de doorgaande weg gaven geen omweg; (3) Silvercorp Ying ontbreekt in `zilver-sitelaag.json` (centraal bijwerken).
