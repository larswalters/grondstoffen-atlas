# Routebrief (licht) · Goud · Van → Via → Naar (land)

**stroom-id:** `goud-nevada-saltlakecity` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** doré-goud (ongeraffineerd, uit autoclaaf/roaster) per **truck** over I-80 van het Goldstrike-complex
(Nevada Gold Mines, Carlin Trend, Barrick 61,5 %/Newmont 38,5 %) naar Asahi Refining USA in Salt Lake City — bewust
zónder luchtvracht, want geen bron noemt die modaliteit voor dit korte, goed gedocumenteerde landtraject.
**Welke as van het verhaal:** *Noord-Amerika (VS) — Nevada → Salt Lake City* — de grootste goudproducerende
mijnencomplex ter wereld levert doré rechtstreeks over de weg aan de belangrijkste Noord-Amerikaanse doré-raffinaderij,
zonder tussenstop, zonder zee, zonder grens.

## 1 · Ketenkaart
```
Goldstrike-complex `au-nevada-mijn` ──(b1 truck · I-80 via Carlin·Elko·Wells·West Wendover·Knolls·Lake Point · ≈450 km)──►
   Asahi Refining USA, Salt Lake City `au-saltlakecity-asahi` ── stoppunt (raffinage tot baar; geen fase E)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Goldstrike-complex (Nevada Gold Mines) → Asahi Refining, Salt Lake City | I-80 (via mijnweg NV-766 → Carlin → Elko → Wells → West Wendover → Knolls → Lake Point) | ≈450 [11]+optelling, ontwerp noemde ≈550 (zie §7) | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-nevada-mijn` | mijn / verwerking (kop) | Goldstrike-complex, Betze-Post open pit + autoclaaf-/roaster-verwerking (Nevada Gold Mines, Carlin Trend) | 40.98160, -116.37890 | [1][2][7][10] | bron-gelegd (z15 gezien: grote open pit met afgetrapte terrassen, direct ten noorden een cluster verwerkingsgebouwen met tanks/schoorstenen — autoclaaf-/roastercomplex — en een tailings-vlak NO) |
| `au-saltlakecity-asahi` | raffinaderij (stoppunt) | Asahi Refining USA, Inc. — 4601 West 2100 South, Salt Lake City UT 84120 | 40.72471, -112.00077 | [3][4][5][6][10] | bron-gelegd (z15 gezien: één industrieel gebouw met eigen parkeerterrein en laaddock, direct zuidelijk van 2100 South, tussen grotere distributiehallen — adres komt exact overeen met het OSM-huisnummer) |

## 4 · Via-punten (b1 — 6, op de doorgaande I-80-corridor)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Carlin, NV | 40.71310, -116.10710 | hier sluit de mijnweg (NV-766/Boone Springs Road, ~30 km vanaf Goldstrike) aan op I-80 — enige corridorkeuze op dit stuk [9] |
| b1 | 2 | Elko, NV | 40.83889, -115.74028 | I-80/US-93-knooppunt, regionale mijnbouwstad; hier zou een alternatief via US-93 zuidwaarts kunnen (niet gebruikt) [9] |
| b1 | 3 | Wells, NV | 41.12000, -114.96722 | I-80/US-93-splitsing (US-93 noordwaarts naar Idaho); doorgaande I-80 blijft de gekozen corridor [9] |
| b1 | 4 | West Wendover, NV | 40.74097, -114.07517 | staatsgrens Nevada/Utah, I-80; casino-/tankstop-cluster pint het corridorpunt op de grens [9] |
| b1 | 5 | Knolls, UT | 40.72299, -113.28971 | I-80-afrit aan de rand van de Bonneville Salt Flats — het enige aangrijppunt op dit lege stuk [9] |
| b1 | 6 | Lake Point, UT | 40.68078, -112.26300 | I-80 langs de zuidoever van de Great Salt Lake, waar de corridor de Salt Lake Valley in buigt richting I-15 [9] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Asahi Refining USA, Salt Lake City | Asahi Holdings (Japan) | doré (goud + zilver, ruw) → good-delivery goud-/zilverbaren | onbekend (t/j niet gevonden binnen het webbudget) | [3][4][5] |

## 6 · Stoppunt
De brief stopt aan de poort van Asahi Refining USA in Salt Lake City: de raffinaderij levert baren aan de
groothandel/COMEX-keten, maar geen bron noemt een specifieke afnemersfabriek of -markt voor dít Nevada-doré na
raffinage — fase E vervalt (ontwerp bevestigt: "bewust geen vlucht" en geeft geen fase D/E-bestemming).

## 7 · Open punten
- **Mijnkeuze binnen "Carlin/Cortez-trend":** het ontwerp noemt beide trends generiek; deze brief kiest bewust het
  **Goldstrike-complex** (Carlin Trend) als anker omdat het direct aan de I-80-corridor ligt, autoclaaf/roaster/doré-
  productie heeft en satelliet-bevestigd is. De **Cortez-trend** (Pipeline/Crescent Valley, via SR-306 naar I-80 bij
  Beowawe, ~65 km zuidwestelijker) is niet getekend — als Cortez-doré apart vervoerd wordt is dat een tweede,
  aparte keten met een eigen kortere I-80-instap.
- **km-correctie:** het ketenontwerp noemt "≈550 km"; deze brief meet ≈450 km (Elko→Salt Lake City 370 km via I-80
  [11] + Carlin→Elko ≈39 km + mijnweg Goldstrike→Carlin ≈30 km over NV-766). De 550 km lijkt een overschatting;
  de exacte lengte volgt uit `maak_stroombeen_weg.py` bij het bakken.
- **Doorzetcapaciteit Asahi Refining SLC** (t/j doré of baren) niet gevonden binnen het webbudget — alleen het
  adres en de bedrijfsrol zijn bron-gelegd.
- **Klantrelatie Asahi USA ↔ Nevada Gold Mines** niet met naam bevestigd; Asahi's eigen site noemt alleen in
  algemene termen "de grootste mijnbouwbedrijven ter wereld" zonder klantnamen — dit deel van het ontwerp blijft
  **aannemelijk**, niet brongelegd.
- Feasibility-toets bevestigd: `us-nevada-latest.osm.pbf` (122.247.210 bytes) en `us-utah-latest.osm.pbf` staan al
  lokaal in `v2/build-cache/geofabrik/` — geen download nodig vóór het bakken.

## 8 · Bronnen
[1] Wikipedia, "Goldstrike mine" — coördinaten (40,981583/-116,378964), eigenaar Barrick, cumulatieve productie 44,4 Moz t/m 2018. https://en.wikipedia.org/wiki/Goldstrike_mine
[2] Wikipedia, "Gold mining in Nevada" — overzicht Carlin Trend en Nevada Gold Mines. https://en.wikipedia.org/wiki/Gold_mining_in_Nevada
[3] Asahi Refining, "About Us" — vier wereldwijde raffinaderijlocaties. https://www.asahirefining.com/about-us/
[4] Asahi Refining, "Miners" — algemeen klantenprofiel ("world's largest mining companies", geen namen). https://www.asahirefining.com/miners/
[5] Utah Division of Air Quality, permit DAQE-IN103670032-26 — Asahi Refining USA, Inc., 4601 West 2100 South, Salt Lake City, UT 84120. https://daqpermitting.utah.gov/DocViewer?IntDocID=160312&contentType=application%2Fpdf
[6] Panjiva, "Asahi Refining USA Inc." — bedrijfsadres 4601 West 2100 South, Salt Lake City UT 84120. https://panjiva.com/Asahi-Refining-USA-Inc/38176602
[7] Mining Technology, "Nevada Gold Mines, US" (Carlin) — JV Barrick 61,5 %/Newmont Goldcorp 38,5 %; Carlin-complex reserves 190 Mt @ 3,32 g/t Au = 21 Moz (dec. 2019); productie 2,2 Moz (2019); Betze-Post/Goldstrike genoemd. https://www.mining-technology.com/projects/carlin/
[8] Nevada Gold Mines, bedrijfswebsite. https://www.nevadagoldmines.com/
[9] OpenStreetMap (ODbL) via Nominatim — Carlin/Elko/Wells/West Wendover/Knolls/Lake Point, adrespunt Asahi Refining. https://www.openstreetmap.org
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-goud-nevada-saltlakecity-mijn.png`, `sat-goud-nevada-saltlakecity-asahi.png`.
[11] DistanceCalc, "How far is it from Elko, NV to Salt Lake City, UT" — 230 mijl / 370 km via I-80. https://distancecalc.com/how-far-from-elko-nv-to-salt-lake-city-ut

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `goud-nevada-saltlakecity`** → `v2/data/stroomroute-goud-nevada-saltlakecity.json` — 2 benen, 443,0 km, 2.868 punten,
2 markers: truck 442,9 km · truck (stippel) 0,1 km.
Recept: `bak_stromen.sh` (functie `bak_goud_nevada_saltlakecity`). Toelichting per been:
- **b1 (truck, doorgetrokken):** `maak_stroombeen_weg.py --profiel goud-nevada-saltlakecity-nevada-saltlakecity` (venster 75 km,
  `corridorKlassen: tertiary/unclassified`, extracts `us-nevada`+`us-utah`) → 442,9 km over I-80/NV-766 via Carlin·Elko·Wells·
  West Wendover·Knolls·Lake Point, tegen ≈450 km gepubliceerd (§2/§7 van deze brief) = **−1,6% [OK]**. Het via-punt bij
  Carlin (mijnweg-aansluiting) vroeg het verruimde venster (40 km gaf "geen wegpad tussen punt 0 en 1"; 75 km +
  corridorKlassen loste het op — de mijnweg NV-766 is deels `tertiary`/`unclassified`, niet doorgaand `secondary`).
  `snoei_keerlussen` verwijderde 14 heen-en-weer-uitstapjes (449,3 → 442,8 km vóór afronding), grootste bij Elko
  (3,75 km) — normale OSM-viaductlussen op de I-80/US-93-knoop, geen fout.
- **b2 (truck, stippel — "last mile", <2 km):** de laatste ~100 m bij Asahi Refining. Diagnose (eigen weggraaf-analyse, BFS
  op connected components): het satelliet-gelegde anker `au-saltlakecity-asahi` (laaddock/parkeerlus, 40,72471/-112,00077)
  snapt op een OSM-component van slechts 8 knopen (twee losse `service`-ways, way 742154031 en 742154032) die **niet**
  aan het publieke wegennet hangt — een echte topologiebreuk in OSM, geen te krap scanvenster (het venster van 75 km
  dekt de hele corridor ruimschoots). De dichtstbijzijnde knoop op het hoofdnet ligt 102 m verderop, op South Frontage
  Road (40,725566/-112,000339, bevestigd via Nominatim-reverse-geocode als het adres direct vóór de Asahi-poort). Het
  wegbeen (b1) eindigt daar; de laatste 102 m gaan als rechte stippel met deze reden — precies de "last mile (geen net
  op deze korrel)"-conventie uit de bakhandleiding (§2, <2 km, geen `maak_havenaanloop.py` nodig want geen water).
- Beide markers uit §3 zijn meegenomen (au-nevada-mijn, au-saltlakecity-asahi). Geen lucht (brief §1: bewust geen
  luchtvracht voor dit korte, goed gedocumenteerde landtraject), geen fase D/E (brief §6: geen bron noemt een
  specifieke afnemersfabriek na raffinage bij Asahi SLC — bewust stoppunt bij de raffinaderij).

**Toets-bevindingen:**
- Geen naad > 5 km: been 1→2 naad 0,00 km (South Frontage Road-punt is letterlijk het beginpunt van de stippel).
- `toets_knikken.py`: 32 knikken ≥60° (allemaal `spike`, boogstraal 6–103 m — normale rijstrookwisselingen/kruisingen
  op I-80/NV-766/US-93), **0 omkeringen ≥150°, 0 terugloop** — geen reparatie nodig.
- `toets_rechte_benen.py --min-km 5`: de stroom komt niet in de verdachtenlijst voor — b1 heeft een omwegfactor ruim
  boven 1,000 (echte weggeometrie) en b2 (0,1 km) valt onder de 5 km-drempel van het tool.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteit `truck` (toegestaan), beide benen ≥2 punten,
  bestand 62,1 KB (ruim < 300 KB) — allemaal in orde.
- De ontwerpschatting van ≈550 km (§7 van deze brief) wordt door de bake niet bevestigd; de eigen optelling van deze
  brief (≈450 km) en de gebakken lengte (442,9 km) liggen dicht bij elkaar, dus de brief-correctie op het ontwerp
  klopt.
- Open punt uit §7 ("last mile mijnterrein Goldstrike → openbare weg") blijft onbeantwoord: de Goldstrike-kop snapte
  op b1 op 0,09 km van het anker (binnen de graaf, geen aparte stippel nodig) — geen aanwijzing voor een
  mijnterrein-last-mile aan die kant; alleen de Asahi-kant (b2) bleek een last-mile-geval.

**Gereedschapslessen:**
- Een via-punt op een mijnwegaansluiting kan een groter venster + `corridorKlassen` vragen, ook als de brief zelf geen
  reden geeft om te twijfelen aan de wegklasse — 40 km venster met alleen `WEG_HOUD` (motorway–secondary) gaf hier
  direct "geen wegpad tussen punt 0 en 1" tussen de mijn en Carlin.
- Een satelliet-gelegd anker kan op een OSM-topologiegat landen dat geen verband houdt met de mijnterrein/privéterrein-
  vraag uit de brief: hier is het een geïsoleerde parkeerlus/laaddock-lus (8 knopen) bij een gewone, publiek
  toegankelijke Amerikaanse voorstad-industriestraat — géén "airside" of "privéterrein"-geval, gewoon een OSM-
  karteringsgat op de allerlaatste ~100 m. Een BFS-componentenanalyse op de weggraaf (in plaats van alleen de
  foutmelding "geen wegpad tussen punt X en Y" te accepteren) vond het exacte gat en de exacte afstand (102 m) —
  ruim genoeg voor de <2 km-last-mile-stippelregel, en te kort om als een tweede, apart onderzocht "privéterrein"-
  geval te labelen.
