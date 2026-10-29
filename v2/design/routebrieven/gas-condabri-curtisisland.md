# Routebrief (licht) · gas — APLNG-hoofdleiding (Surat Basin) → Curtis Island (Australië)

**stroom-id:** `gas-condabri-curtisisland` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) ·
**status:** gebakken
**Keten in één zin:** Coal-seam-gas uit het Surat/Bowen-bekken (Queensland) gaat door de ondergrondse APLNG-hoofdleiding (42 inch, 8 OSM-ways,
365,1 km) van een onbenoemd beginstation bij de Woleebee Lateral noordnoordoostwaarts naar de Australia Pacific LNG-fabriek op Curtis Island bij
Gladstone, onder The Narrows door. De tekening stopt bij de fabriek: een een-been-pijp (reserve-as, Oost-Australië).
**Welke as van het verhaal:** *Reserve-as "LNG uit Oost-Australië"* — steenkoolgas dat via één leiding de kust bereikt en daar vloeibaar wordt.
Volume: LNG-fabriek 9,0 Mtpa = 12,2 bcm/j (sitelaag `w-aplng`, B9; 2 treinen van 4,5 Mtpa [5]); peiljaar boekjaar jul 2023–jun 2024: APLNG-productie
ca. 690 PJ (≈ 18 bcm, incl. ca. 142 PJ binnenlands; eigen optelling van kwartaalcijfers [8]), dus meer dan alleen de LNG-keten. Leidingcapaciteit
1.479 MMcf/d ≈ 15 bcm/j (GEM-omrekening, geen eigen bcm-cijfer) [3]. Gewicht in de gloed: 12,2 bcm/j (fabriek) is de bovengrens van deze ene leiding.

## 1 · Ketenkaart
```
APLNG-hoofdleiding, beginstation (launcher) bij de Woleebee Lateral, Surat Basin `gas-aplng-hoofdstation`
  ──(b1 leiding · APLNG-hoofdleiding 42", 8 OSM-ways, doorgetrokken · 365,1 km OSM / 364,97 AEMC / 360 McConnell Dowell)──►
Australia Pacific LNG, Curtis Island `gas-aplng-curtisisland` (OSM-eind 0,6 km van het fabrieksanker, binnen het hek) — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-aplng-hoofdstation` → `gas-aplng-curtisisland` | APLNG Mainline 1050 mm, operator APLNG, man_made=pipeline, substance=gas, usage=transmission, ondergronds; incl. The Narrows-kruising | 364,97 [1], 360 [4]; gemeten OSM **365,1** (+0,04% / +1,4%) | vooraf gestikt geojson (FeatureCollection, 522 punten; grootste segment 5,9 km, naden 0 m) | nee |

OSM-ways van b1, in volgorde: 1358316289 (40,7 km) · 1358316292 (55,7) · 1358316293 (78,7) · 1358316296 (78,8) · 1358316287 (0,0; bovengronds stukje) ·
1358316299 (7,1) · 1356547330 (14,1) · 618217684 (90,1; Narrows + eiland). Alle acht: operator APLNG, diameter 1066 mm waar getagd.
De 530 km uit [3][5][7] is het hele APLNG-systeem (hoofdleiding + Condabri Lateral 76 km + Woleebee Lateral 87 km): geen maat voor b1. Niet getekend: de
parallelle leidingen naar Gladstone van APA (way 618217685) en Santos/GLNG (618217686), en de Woleebee Lateral (way 1358319559, 88 km, ander been).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-aplng-hoofdstation` | beginstation hoofdleiding (kop) | APLNG launcher-station, Surat Basin (naam niet bevestigd) | -26.3199, 150.1948 | [9][4] | bron-gelegd (z15+z16 gezien: klein omheind station met grindplatforms, leidingstrook en toegangsweg, midden in weiland/bos; OSM-begin ligt op het station; naam onzeker) |
| `gas-aplng-curtisisland` | LNG-fabriek (staart, stoppunt) | Australia Pacific LNG, Curtis Island | -23.7554, 151.1896 | [11][5] | bron-gelegd (z15 gezien: noordelijk van de drie complexen op het eiland, processtreinen en pijpenrek binnen het hek; hergebruik van sitelaag `w-aplng`) |

Hergebruik: `gas-aplng-curtisisland` is letterlijk sitelaag-punt `w-aplng` (-23.7554, 151.1896) uit `gas-sitelaag.json`; het OSM-eind (-23.7514, 151.1937, z16 gezien:
ontvangstkant aan de noordrand van het complex bij een schakelstation) ligt 0,6 km ernaast en is geen eigen anker.
Het beginstation is geen bronnaam: McConnell Dowell noemt het "launcher station at Condabri" [4], maar Condabri North/South (-26.67 / -26.93) liggen 39+ km zuidelijker.

## 4 · Via-punten
Niet van toepassing: leiding = OSM-ways, geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| APLNG-velden en gasverwerking (Condabri, Southern, Woleebee, Western) | Origin (operator) namens Australia Pacific LNG | steenkoolgas → hoofdleiding | ca. 690 PJ/j productie (FY2023-24) | [5][8] |
| Australia Pacific LNG, Curtis Island | APLNG (ConocoPhillips 47,5 / Origin 27,5 / Sinopec 25 % [3]; oorspronkelijk 37,5/37,5/25 [5][6]) | gas → LNG | 2 treinen, 9,0 Mtpa (12,2 bcm/j) | [5][6] |

## 6 · Stoppunt
De tekening stopt bij de LNG-fabriek op Curtis Island: de afnemer per lading is niet te volgen (Sinopec 7,6 en Kansai 1 Mtpa zijn contractvolumes [6], geen terminal
per cargo), dus geen zeebeen; fase D/E vervallen. De keten is daarmee een bewuste een-been-pijp. Verhaal in één zin: het gas van het Surat-bekken verlaat de
binnenlanden door één 42-inch-pijp en wordt aan de kust van Gladstone LNG.

## 7 · Open punten
- **Naam van het beginstation onbekend.** Geen bron legt coördinaten bij "Condabri launcher"; de OSM-ways beginnen onbenoemd bij -26,3199, 150,1948 (naast de Woleebee Lateral). Titel noemt Condabri niet.
- **Lengte-vergelijking:** 365,1 (OSM) komt overeen met de AEMC-hoofdleiding 364,97 [1] en McConnell Dowell 360 [4]; de gepubliceerde 530 km [3][5][7] betreft het hele netwerk met laterals (apart been, hier niet getekend).
- **Peiljaar-volume is een eigen optelling** (519 PJ jul–mrt + 175 PJ apr–jun) uit kwartaalcijfers [8]; een Mt-LNG-cijfer per kalenderjaar is niet gevonden. Binnenlands deel (ca. 142 PJ) loopt niet allemaal door deze leiding.
- **Afnemerterminal per lading ongedocumenteerd** (Sinopec, Kansai, andere): geen LNG-been.
- **Aandeelhoudersverdeling:** GEM geeft 47,5/27,5/25 % [3], oudere bronnen 37,5/37,5/25 % [5][6]; niet relevant voor de geometrie.
- **Binnen het hek:** de laatste 0,6 km tot het fabrieksanker is niet gekarteerd; geen stippel (< 2 km). Narrows-kruising zit als ondergrondse OSM-way in b1.

## 8 · Bronnen
[1] AEMC, Gas pipeline register "QLD: APLNG Mainline" — 364,97 km, Narrows Crossing 3 secties ca. 11 km, gereed 2014 (inhoud uit zoekresultaat; pagina geeft 403 bij ophalen). https://www.aemc.gov.au/energy-system/gas/gas-pipeline-register/qld-aplng-mainline
[2] AEMC, Gas scheme register "QLD: Australia Pacific LNG Gladstone Pipeline" — ca. 365 km, 1050 mm, velden bij Wandoan, aansluitingen Condabri/Woleebee Lateral en Wandoan Interconnect (zoekresultaat). https://www.aemc.gov.au/energy-rules/national-gas-rules/gas-scheme-register/qld-australia-pacific-lng-gladstone-pipeline
[3] Global Energy Monitor wiki, "APLNG Pipeline" — 530 km netwerk, 42 inch, Condabri Lateral 76 km, Woleebee Lateral 87 km, 1.478,59 MMcf/d, eigenaren, start 2015. https://www.gem.wiki/APLNG_Pipeline
[4] McConnell Dowell, "APLNG Pipeline" — hoofdleiding 360 km 42", launcher-station bij Condabri tot ontvangststation Curtis Island, 4 afsluiterstations, middenlijn-scraperstation. https://www.mcconnelldowell.com/projects/aplng-pipeline
[5] Offshore Technology, "Australia Pacific LNG, Queensland" — 530 km hoofdleiding, ontwikkelgebieden Condabri/Southern/Woleebee/Western, 2 treinen 4,5 Mtpa, leiding in bedrijf feb 2015, eerste LNG dec 2015, eerste lading jan 2016. https://www.offshore-technology.com/projects/australia-pacific-lng-queensland/
[6] Oil & Gas Journal, 10 okt 2016, "Australia Pacific LNG second train brought on stream" — Sinopec 7,6 Mtpa, Kansai 1 Mtpa, aandeelhouders 37,5/37,5/25 %. https://www.ogj.com/pipelines-transportation/article/17250845/australia-pacific-lng-second-train-brought-on-stream
[7] World Coal, 11 dec 2015, "APLNG begins LNG production on Curtis Island" — start LNG-productie, 530 km leiding. https://www.worldcoal.com/cbm/11122015/APLNG-begins-LNG-production-on-Curtis-Island-3274/
[8] Argus Media, "APLNG gas output rebounds in 2023-24: Origin" (en kwartaalcijfers 176/175 PJ, binnenlands 142 PJ; zoekresultaat). https://www.argusmedia.com/en/news-and-insights/latest-market-news/2593066-aplng-gas-output-rebounds-in-2023-24-origin
[9] OpenStreetMap (ODbL), ways 1358316289, 1358316292, 1358316293, 1358316296, 1358316287, 1358316299, 1356547330, 618217684 (man_made=pipeline, operator APLNG), gelezen uit de Geofabrik australie-pbf; stikscript `v2/tools/maak_leidingbeen_gas_condabri_curtisisland.py`. https://www.openstreetmap.org/way/618217684
[10] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-gas-condabri-curtisisland-start.png`, `-start-z16.png`, `-plant.png`, `-eind.png`.
[11] Sitelaag `v2/design/gas-sitelaag.json`, id `w-aplng` (Wikidata Q30972398; z15-blik door deze brief); Wikipedia "List of LNG terminals" (9,0 Mtpa).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
**Bestand:** `v2/data/stroomroute-gas-condabri-curtisisland.json` (11,7 KB, versie 2, lonlat) · **functie:** `bak_gas_condabri_curtisisland()` in `v2/tools/bak_stromen.sh` · **recept:** `bash v2/tools/bak_stromen.sh gas-condabri-curtisisland`.
**Titel:** Gas · APLNG-hoofdleiding (Surat Basin) → Curtis Island (Australië). Eindpunt klopt met het id (Curtis Island); het beginpunt is het launcher-station bij de Woleebee Lateral, niet Condabri.

| # | modaliteit | been | km gemeten | km brief | punten | stippel |
|---|---|---|---|---|---|---|
| 1 | leiding | APLNG-hoofdleiding 42 inch Surat Basin naar Curtis Island, ondergronds | 365,1 | 364,97 AEMC / 360 McConnell Dowell | 522 | nee |

Totaal 365,1 km · 1 been · 2 markers · naden: geen (een been). Afwijking t.o.v. AEMC +0,04%, t.o.v. McConnell Dowell +1,4% (binnen de norm, en dit is een echte leidinglengte, geen hemelsbreed).
**Markers:** beginstation 0,002 km van de lijn; Curtis Island 0,607 km (anker is sitelaag-punt `w-aplng`, het OSM-eind ligt binnen het hek: anker is niet gelijk aan routeerpunt, niet gekarteerd, geen stippel omdat < 2 km).
**Toelichting leiding:** doorgetrokken, want OSM heeft alle acht ways (man_made=pipeline, operator APLNG, ondergronds, Narrows-kruising en eilandstuk inbegrepen). Geen offshore- of ontbrekend stuk, dus geen stippel. Geometrie vooraf gestikt door `v2/tools/maak_leidingbeen_gas_condabri_curtisisland.py` (FeatureCollection, `v2/build-cache/ais/graaf/gas-condabri-curtisisland-leiding-aplng.geojson`).
**Niet getekend:** geen zeebeen of haven-aanloop (afnemer per lading ongedocumenteerd, fase D/E vervallen), geen via-punten, geen kopie, geen luchtbeen, geen wegbeen (dus geen profiel in `maak_stroombeen_weg.py`).
**Toets:** `toets_knikken` 6 knikken >= 60 graden (waarvan 3 spikes en 3 krappe bochten op OSM-vertices, het scherpst 90,3 graden), 0 omkeringen, 0 terugloop; echte leiding, een bocht in de pijp is geen spoor-onmogelijkheid. `toets_rechte_benen --min-km 5`: geen melding voor deze stroom. json.load, versie 2, punt_formaat lonlat, modaliteit leiding, 522 punten.
**Lessen:** (1) een-been-pijp met vooraf gestikt geojson bakt in seconden, geen slot-zware route nodig behalve de hecht_marnet-lading (~25 s). (2) Het stroom-id noemt Condabri, de leiding begint 39 km zuidelijker; de titel is daarom neutraal gehouden. (3) De 530 km uit de bronnen is het netwerk met laterals, de hoofdleiding is 365 km.
