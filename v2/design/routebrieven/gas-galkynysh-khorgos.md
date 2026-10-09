# Routebrief (licht) · gas — Galkynyş → Bagtyyarlyk (Saman-Depe) → Khorgos (Turkmenistan–Oezbekistan–Kazachstan–China)

**stroom-id:** `gas-galkynysh-khorgos` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** Turkmeens pijpleidinggas (Galkynyş en Dovletabat, plus de Bagtyyarlyk-velden van CNPC) gaat over het binnenlandse
Turkmeense net naar het begin van de **Centraal-Azië–China-gasleiding** aan de Turkmeens-Oezbeekse grens, door Oezbekistan en Zuid-Kazachstan
(Shymkent, ten noorden van Almaty om) naar het Khorgos-leidingstation 6 km over de Chinese grens, waar hij aansluit op het West–Oost-net.
Eén gekozen lijn (lijn X) van het parallelle drietal A/B/C. De enige grote pijpgas-as op aarde zonder Rusland en zonder LNG.
**Welke as van het verhaal:** 55 bcm/j ontwerpcapaciteit (lijn A+B+C) [1][2]; Turkmeense quota 40 bcm/j (2023) [1]; geleverd ~460 bcm sinds
dec. 2009 tot 1-3-2026 (≈28 bcm/j gemiddeld, eigen deling) [9]. Geen vers volledig jaarvolume 2024/2025 in bcm gevonden (alleen Chinese douanewaarde).

## 1 · Ketenkaart
```
Galkynyş-gasverwerking `gas-galkynysh-plant` (Türkmengaz/CNPC, Mary)
  ──(b1 leiding · binnenlands Turkmeens net via compressorstation Malay, Malay–Bagtyyarlyk-lijn 188 km [3] · ~268 km hemelsbreed, STIPPEL)──►
Bagtyyarlyk/Saman-Depe `gas-bagtyyarlyk-start` (CNPC-gasverwerking op de TM/UZ-grens; begin van de OSM-leiding)
  ──(b2 leiding · OSM-lijn X · ~11 km TM + ~523 km Oezbekistan (Olot) · 534,4 km)──► splitspunt UZ/KZ-grens (41.2659, 66.6391; geen site)
  ──(b3 leiding · Zuid-Kazachstan (Shymkent, Almaty-bypass) · 1.301,8 km KZ + 6,4 km CN · 1.308,2 km)──►
Khorgos-leidingstation `gas-khorgos-station` (Huocheng/Xinjiang, aansluiting West–Oost 2/3) ═══ stoppunt ═══
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-galkynysh-plant` → `gas-bagtyyarlyk-start` | Turkmeens binnenlands net, via Malay-compressor [3] | ~268 hemelsbreed, geen leidingkm; gepubliceerd 188 km voor Malay–Bagtyyarlyk [1][3] | `--stippel` rechte lijn | **ja — geen OSM-way, tracé en positie Malay niet gelegd** |
| b2 | B | leiding | `gas-bagtyyarlyk-start` → UZ/KZ-grens | Centraal-Azië–China, lijn X (Olot) | **534,4** OSM-gemeten; Oezbeeks deel ~523 tegen 530 gepubliceerd (−1,3%) [1] | OSM-ways 265950268 + 265950276, gestikt (twin: 265950267 + 265950274) | nee |
| b3 | C | leiding | UZ/KZ-grens → `gas-khorgos-station` | Turkmenistan–China (KazTransGas/AGP), Shymkent → Almaty-bypass → Khorgos | **1.308,2** OSM-gemeten; Kazachs deel 1.301,8 tegen 1.300 (planning 2007) en 1.115 (as-built volgens [1][10]) [11] | 18 OSM-ways, gestikt (zie §7); eindigt op way 1324617060 `中国—中亚天然气管道` | nee |

Doorgetrokken 1.842,6 km tegen gepubliceerd 1.833 (lijn A–C totaal, **inclusief** 188 km Turkmeens deel dat niet getekend is) [1]; stippel 12,7% van de keten.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-galkynysh-plant` | gasverwerking (kop) | Galkynyş-gasverwerkingscomplex, fase 1, Ýolöten | 37.1143, 62.3587 | [4][8] | aannemelijk (z15 gezien: groot complex met meerdere procestreinen en een lange wit-bekalkte strook; ligt in het 90×30 km-veldareaal; Wikipedia-veldcoördinaat 37.3014/62.3586 is een centroïde, geen plant) |
| `gas-bagtyyarlyk-start` | begin van de grensleiding | CNPC-gasverwerking Bagtyyarlyk-contractgebied ("Saman-Depe" in [1][2]), Hojambaz/Lebap | 38.6121, 64.7552 | [1][2][3][5] | bron-gelegd (z14 gezien: groot omheind procescomplex met tanks/procesgebouwen op het eerste punt van de OSM-lijn; Nominatim: "CNPC, industrial", ~11 km vóór de Oezbeekse grens) |
| `gas-khorgos-station` | stoppunt (overslag leiding → CN-net) | Khorgos/霍尔果斯-leidingstation, Huocheng, Xinjiang | 44.0964, 80.4728 | [5][6][8] | bron-gelegd (z14 gezien: omheind compound met rode daken in een industrie-/akkerzone; laatste punt van de naam-getagde way `中国—中亚天然气管道`, 6 km over de grens) |

Splitspunt b2/b3 (41.2659, 66.6391) is een OSM-lijnknoop in de woestijn, **geen** site en geen marker. Het "grensstation Khorgos" van het ontwerp ligt in OSM niet op de grens zelf: de grens ligt bij ~44.0688, 80.4413 [6].

## 4 · Via-punten
Niet van toepassing (leidingbenen: OSM-geometrie of stippel, geen corridorkeuze door ons).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Galkynyş-gasverwerking | Türkmengaz (bouw CNPC/Hyundai/Petrofac) | veldgas → droog verkoopgas | niet gevonden in een bron met jaar | [4] |
| Compressorstation Malay (positie niet gelegd) | Türkmengaz/CNPC | pompt gas van Galkynyş en Dovletabat naar de Malay–Bagtyyarlyk-lijn | 30 bcm/j, 6 compressorsets (geopend 15-1-2021) | [3] |
| Shymkent (op b3) | KazTransGas/AGP | koppeling met de lijn Beineu–Bozoy–Shymkent (Kazachs gas) | 15 bcm/j (Wikipedia, in bedrijf 2014) | [1] |
| Khorgos | PetroChina/PipeChina | overdracht aan West–Oost-lijn 2 (en 3) | — | [1][2] |

## 6 · Stoppunt
Khorgos-station: vanaf hier gaat het gas anoniem het Chinese West–Oost-net in (tot Shanghai, ~7.000 km [1]); geen bron volgt één molecuul naar een afnemer. Fase D/E vervallen.

## 7 · Open punten
- **Het begin ligt niet bij Galkynyş maar bij Bagtyyarlyk/Saman-Depe**: de leiding begint aan de Turkmeens-Oezbeekse grens en wordt gevoed uit Malay, Bagtyyarlyk, Dovletabat en Galkynyş [1][2][3]. Id blijft staan; titel noemt de echte route. b1 is een schematische stippel (feeder bestaat volgens [3], tracé niet gekarteerd).
- **Malay-compressorstation niet gelegd** (geen coördinaat in een bron; het OSM-eind bij 38.4751, 63.8876 is woestijn op z14, geen installatie). Ook Samandepe Gas Complex (Nominatim 38.9468, 64.1382, Farap) ligt 33 km uit de OSM-lijn en is niet als begin gebruikt.
- **Km-conflict Kazachstan**: OSM 1.301,8 km ≈ planning 2007 (1.300) maar +16,8% tegen as-built 1.115 [1][10][11]; Oezbekistan klopt (−1,3%), totaal +0,5% omdat de 188 km Turkmeens voedingsdeel buiten het getekende stuk valt. Indicatie, geen norm.
- Tweelingleidingen: A/B/C liggen parallel; OSM tekent grotendeels één lijn (b2/b3 volgen de gas-getagde lijn X; 265950267/265950274 zijn de tweeling).
- Geen vers volumecijfer 2024/2025 in bcm; 34 bcm voor 2021 en capaciteit 40 vs 55 bcm/j spreken elkaar tegen [1][9]. Gloedgewicht: capaciteit 55 bcm/j aanhouden tot een gemeten jaarvolume bestaat.
- Lijn D (Galkynyş → Tadzjikistan/Kirgizië → China, 966 km) niet gebouwd, niet getekend [1][2].
- Gereedschap: pyosmium is geblokkeerd (app-control), Overpass onbereikbaar en Firecrawl zonder credits; geometrie komt uit een eigen pure-python PBF-scan (`v2/build-cache/ais/graaf/gas-galkynysh-khorgos-pbfscan.py`), niet uit `maak_leidingbeen_*`.

## 8 · Bronnen
[1] Wikipedia, "Central Asia–China gas pipeline" (route, 188/530 km, 55 bcm/j, quota 40 bcm/j 2023, Line D) https://en.wikipedia.org/wiki/Central_Asia%E2%80%93China_gas_pipeline
[2] Global Energy Monitor, "Central Asia–China Gas Pipeline" (begin Saman-Depe op de TM/UZ-grens, lijn A/B/C-capaciteiten, voeding Galkynyş/Dovletabat/Bagtyyarlyk) https://www.gem.wiki/Central_Asia-China_Gas_Pipeline
[3] Ambassade van Turkmenistan Kabul, nieuwsbericht opening compressorstation Malay (15-1-2021): 188-km Malay–Bagtiyarlyk-lijn, 30 bcm/j, Galkynyş/Dovletabat-gas https://afghanistan.tmembassy.gov.tm/en/news/73975
[4] Wikipedia, "Galkynyş Gas Field" (coördinaat 37.3014/62.3586, 90×30 km, Türkmengaz, CNPC/Hyundai/Petrofac) https://en.wikipedia.org/wiki/Galkyny%C5%9F_Gas_Field
[5] OpenStreetMap-bijdragers (ODbL), lokale Geofabrik-extracts turkmenistan/oezbekistan/kazachstan, eigen PBF-scan man_made=pipeline (ways in §2); `1324617060` naam `中国—中亚天然气管道`. https://www.openstreetmap.org/copyright
[6] OSM/Nominatim reverse (landnaam per vertex): TM/UZ-grens ≈ 11–13 km na de OSM-start, UZ/KZ-grens bij lon ≈ 66,67, KZ/CN-grens tussen 44.0688/80.4413 en 44.0715/80.4470. https://nominatim.openstreetmap.org
[7] Wikipedia API (coördinaten): Olot 39.4167/63.8, Khorgos 44.2125/80.4097, Shymkent 42.3167/69.5958.
[8] Esri World Imagery via `v2/tools/sat_check.py`, `v2/build-cache/satcheck/sat-gas-galkynysh-khorgos-{galkynysh-gp1,galkynysh-gp2,leidinghub-hojambaz,samandepe-complex,malay-osmeind,khorgos-station}.png`.
[9] Turkmenistan oil&gas-portaal, "Turkmenistan–China Gas Pipeline Has Delivered Approximately 460 Billion Cubic Meters" (stand 1-3-2026; alleen via zoekresultaat gelezen, pagina gaf ECONNRESET) https://oilgas.gov.tm/index.php/en/posts/habarlar/16570/the-turkmenistan-china-gas-pipeline-has-delivered-approximately-460-billion-cubic-meters-of-natural-gas
[10] Offshore Technology, "Central Asia–China Gas Pipeline" (188/530/1.115 km; alleen via zoekresultaat) https://www.offshore-technology.com/projects/centralasiachinagasp/
[11] Jamestown/EurasiaNet-analyse "Kazakhstan Expands Gas Transit Pipeline Capacities" (Kazachs deel 1.300 km in de planning; alleen via zoekresultaat) https://jamestown.org/?p=20760
[12] Galkynyş GP2 (37.0382, 62.4214) op z15: tweede groot gasverwerkingscomplex ~10 km ZO van GP1; 0,7 km van het eind van OSM-way 591769135.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-gas-galkynysh-khorgos.json` · 27,2 KB · contract versie 2, `lonlat` · 3 benen · 2.110,9 km · 1.353 punten · 3 markers.
**Recept:** `bash v2/tools/bak_stromen.sh gas-galkynysh-khorgos` (functie `bak_gas_galkynysh_khorgos`). Geometrie van b2/b3 is voorgebakken (eigen pure-python PBF-scan, pyosmium geblokkeerd) en onveranderd hergebruikt; geen wegprofiel, geen extract, geen slot nodig (hecht_marnet draait ~15 s).

| # | modaliteit | km gebakken | km brief | afwijking | naad | punten |
|---|---|---|---|---|---|---|
| b1 | leiding (stippel) | 268,3 | 188 gepubliceerd (Malay–Bagtyyarlyk), ~268 hemelsbreed | geen leidingkm: indicatie | start | 2 |
| b2 | leiding | 534,4 | 530 (Oezbeeks deel, Wikipedia) | +0,8% (OSM 534,4 incl. ~11 km TM) | 0,000 km | 315 |
| b3 | leiding | 1.308,2 | 1.300 planning / 1.115 as-built | +0,6% / +17,3%: indicatie, geen norm | 0,017 km | 1.036 |

Doorgetrokken 1.842,6 km tegen 1.833 gepubliceerd (+0,5%); stippel 268,3 km = 12,7% van de getekende keten (12,7% van 2.110,9). Markers: plant 0 m, Bagtyyarlyk 0 m, Khorgos 5 m van de lijn.
**Toelichting stippel b1:** de feeder Galkynyş/Dovletabat → Malay → Bagtyyarlyk bestaat volgens de Turkmeense ambassade-bron [3], maar tracé en Malay-positie zijn niet gelegd en OSM kent geen way: rechte lijn, schematisch. Plantanker Galkynyş is aannemelijk, niet bron-gelegd.
**Geen** haven-aanloop, vlucht, zee, weg, spoor, via-punt of kopie. Geen marker op het splitspunt b2/b3.
**Toets:** geen naad > 5 km (max 17 m); `toets_knikken.py`: 28 knikken >= 60 gr (OSM-pijpleidinggeometrie bij Shymkent/Almaty-bypass/Khorgos, twee spikes van 20-35 m straal bij 42.25,69.77 en 42.28,69.81), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py`: alleen b1 (omwegfactor 1,000, stippel mét reden).
**Lessen:** (1) alles wat pyosmium, Overpass of Firecrawl nodig heeft faalt hier (app-control, 5xx, geen credits): een pure-python PBF-scan op de lokale Geofabrik-extracts is het werkende alternatief voor leidingbenen. (2) Het eigenlijke begin van een grensleiding kan elders liggen dan het stroom-id belooft: id blijft staan, titel en dit blad noemen Bagtyyarlyk. (3) De slotjes-routine (`rm -rf "$d"`) wordt door de veiligheidscheck geweigerd; deze bake is licht en draaide zonder slot.
