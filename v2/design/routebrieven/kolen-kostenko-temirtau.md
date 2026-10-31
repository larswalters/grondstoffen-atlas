# Routebrief (licht) · kolen — Kostenko-mijn → Karaganda Metallurgical Plant (Kazachstan)

**stroom-id:** `kolen-kostenko-temirtau` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) · **status:** gebakken
**Keten in één zin:** Kazachse cokeskool (bitumineus, metallurgisch) uit de ondergrondse Kostenko-mijn bij Karaganda (Qarmet) per spoor over het
Kazachse net naar het eigen staalwerk Karaganda Metallurgical Plant in Temirtau — één binnenlands spoorbeen, geen zee. De koppeling mijn → werk is
**aannemelijk: één bron** (GEM [1]).
**Welke as van het verhaal:** reserve-as 'Kazachse cokeskool naar het eigen staalwerk': Qarmet (voorheen ArcelorMittal Temirtau) is vertikaal geïntegreerd
(kolen-, ijzererts- en staalafdeling) [4]; de mijn is door GEM als leverancier van het Temirtau-staalwerk aangemerkt [1]. **Jaarvolume:** 0,5 Mt ROM-kolen in 2023
(brandjaar), 1,7 Mt in 2017 [1]; eenheid Mt kolen per jaar. Aandeel naar Temirtau niet gevonden.

## 1 · Ketenkaart
```
Kostenko-mijn `kolen-kostenko-laad` ──(b1 spoor · Karaganda-net → noordoostelijke boog → Temirtau · 42,9 km)──►
Karaganda Metallurgical Plant `kolen-kmz-aflaad` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-kostenko-laad` → `kolen-kmz-aflaad` | Kostenko-emplacement → Karaganda-knoop → lijn Karaganda–Temirtau (Kazachse spoornet); **aannemelijk: één bron** (GEM [1]) | hemelsbreed 21,6 km, geen spoorkm gepubliceerd; gemeten 42,9 (verhouding 1,99) | toets_spoorroute (`BAKE_SUFFIX=-raw`), 1 run, geen via-punt | nee |

De ±15 %-toets is hier een indicatie, geen norm: er is geen gepubliceerde spoorlengte. Het ontwerp noemde 54 km (raw1op1-diagnose); de bake-router geeft 42,9 km
over 85 edges, snaps 0,18 en 0,28 km, 0 bochten ≥ 60°. De lijn loopt eerst noordoost (via 73.22 O) en komt het werk van het noordoosten in; de hoge verhouding komt door die boog, niet door een terugloop (0 omkeringen).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-kostenko-laad` | mijn / laadplek | Kostenko-mijn (Qarmet), Karaganda, ondergronds | 49.8596, 73.1139 | [1] GEM exact 49.859567, 73.113928; [2] Wikipedia 49.86, 73.115 | bron-gelegd (z15 gezien: oppervlaktecomplex van de mijn met gebouwen, kolenstapel en een spoorbundel direct zuidelijk; de mijn zelf is ondergronds, het punt ligt op het schachtterrein) |
| `kolen-kmz-aflaad` | losplek / staalfabriek | Karaganda Metallurgical Plant (Qarmet), Temirtau | 50.0466, 73.0343 | OSM-landuse (ketenontwerp); [9] ru-Wikipedia 50.0517, 73.0142 ligt 1,5 km WNW in hetzelfde complex | bron-gelegd (z14 en z16 gezien: groot geïntegreerd staalcomplex met walserijen, cokes-/hoogovenzone en spoorbundels; het punt ligt in de oostelijke fabriekszone naast een emplacement, lijn snapt op 0,28 km; de ontvangst van de kool zelf is niet aangewezen) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | — | geen | — | de vrije route (0 bochten ≥ 60°, snaps ≤ 0,28 km) is het kortste OSM-pad tussen twee punten in hetzelfde Kazachse hoofdnet (1,14 mln km); er bestaat geen corridorkeuze of sluipweg over een grens |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kostenko-mijn | Qarmet JSC (100 %) | ondergronds delven → ROM-kool (metallurgisch/bitumineus); 1.282 medewerkers, 1 langwand sinds feb 2024 | 0,5 Mt ROM (2023), 1,7 Mt (2017); 53 kt/maand in juni 2023 (~0,64 Mt/j) | [1][8] |
| Karaganda Metallurgical Plant | Qarmet (staatsdeelneming sinds dec 2023) | kool → cokes → ruwijzer/staal | 3 Mt staal in jan–okt 2024 | [4][9] |

## 6 · Stoppunt
De brief stopt op het KMZ-terrein: geen bron wijst de cokeskoolontvangst of een wasserij op de route aan, en het werk is één terrein zonder openbaar net (fase D/E vervallen).

## 7 · Open punten
- **Koppeling Kostenko → Temirtau-werk: aannemelijk, één bron.** GEM zegt dat de mijn het Temirtau-staalwerk voedt [1] (tabel noemt een staalwerk als hoofdafnemer); geen bron noemt het werk
  of de cokesbatterij expliciet, en Qarmet-kool kan eerst langs een wasserij (niet gecontroleerd; GEM noemt een wasserij in het complex maar niet voor deze mijn).
- **Mijnstatus tegenstrijdig:** na de brand van 28-10-2023 (46 doden [3]) verbood Qarmet op 12-01-2024 de herstart [5]; Qarmet zegt zelf dat de winning in februari 2024 hervatte, met één langwand en
  een tweede gepland voor april 2025 [8]; Mining Data Online meldt 'actief' [7]. Dat de tweede langwand echt draait is niet bevestigd. Een 2025-productiecijfer ontbreekt (Qarmet-kolenafdeling in totaal 7,5 Mt in 2025 volgens een zoekresultaat, niet voor deze mijn).
- **Geen spoorkm gepubliceerd;** de 42,9 km is routerkm, hemelsbreed 21,6 km. Het ontwerpgetal 54 km kwam uit een diagnoserun en is niet gebruikt.
- **Klein volume en kort been:** 0,5 Mt in het brandjaar; de keten is één korte schakel, bewust als reserve gekozen. Beter alternatief is een nog volledig producerende Qarmet-mijn (niet onderzocht).
- Het GEM-mijnpunt is het schachtterrein, niet de ondergrondse winning; geen eigen railaansluiting apart gelegd (de lijn snapt op 0,18 km).
- Het ru-Wikipedia-punt (50.0517, 73.0142) en het OSM-landuse-anker liggen 1,5 km uit elkaar binnen één complex; de KMZ-ontvangst is niet aangewezen.

## 8 · Bronnen
[1] Global Energy Monitor, Kostenko Coal Mine — status operating, Qarmet 100 %, 1,7 Mt ROM (2017), ~2 Mt (2020, raming), 0,5 Mt (2023), langwand 53 kt/maand juni 2023, GEM-coördinaat 49.859567, 73.113928 (exact); levert aan ArcelorMittal Temirtau-staalwerk. https://www.gem.wiki/Kostenko_coal_mine
[2] Wikipedia, Kostenko mine — ondergrondse mijn in Karaganda; 49°51′36″N 73°06′54″E; brand 28-10-2023, 46 doden. https://en.wikipedia.org/wiki/Kostenko_mine
[3] Wikipedia, Kostenko mine disaster — 28-10-2023, methaanexplosie/brand op ~700 m, 46 doden, 18 gewonden; eigenaar ArcelorMittal Temirtau. https://en.wikipedia.org/wiki/Kostenko_mine_disaster
[4] Wikipedia, Qarmet — Temirtau, eigenaar Karaganda Metallurgical Plant (grootste staalwerk van Kazachstan); afdelingen staal, kolen, ijzererts; verkocht aan Qazaqstan Investment Corporation 08-12-2023. https://en.wikipedia.org/wiki/Qarmet
[5] Interfax, 12-01-2024, Qarmet stops production at Kostenko mine until all risks are eliminated — herstart verboden na de brand. https://interfax.com/newsroom/top-stories/98371/
[6] Interfax, Five ArcelorMittal Temirtau coal mines resume operations after fire at Kostenko mine (31-10-2023, alleen titel via zoekresultaat, niet geopend). https://interfax.com/newsroom/top-stories/95985/
[7] Mining Data Online, Kostenko Mine — Qarmet Coal Department, actief, 5 km noord van Karaganda; winning hervat feb 2024, nieuwe langwand 2025; cijfers achter betaalmuur. https://miningdataonline.com/property/1778/Kostenko-Mine.aspx
[8] Qazinform, A year after the Kostenko mine tragedy (10-2024) — 'restored to 100 % operability', winning hervat feb 2024, één langwand, tweede gepland apr 2025, 1.282 medewerkers. https://qazinform.com/news/a-year-after-the-kostenko-mine-tragedy-what-has-been-done-for-industrial-safety-at-qarmet-962d8b
[9] ru-Wikipedia, Карагандинский металлургический комбинат — 50.0517, 73.0142; basis Karaganda-kolen; 3 Mt staal jan–okt 2024. https://ru.wikipedia.org/wiki/Карагандинский_металлургический_комбинат
[10] Wikipedia (MediaWiki API prop=coordinates) — Karaganda 49.8028, 73.1056 · Kostenko mine 49.86, 73.115 · Temirtau 50.05, 72.95. https://en.wikipedia.org/wiki/Temirtau
[11] OpenStreetMap-bijdragers via Nominatim — railway=station Темиртау 50.0788, 72.9271 (ODbL; niet als anker gebruikt). https://www.openstreetmap.org/copyright
[12] Eigen meting `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`), uitvoer `v2/build-cache/ais/graaf/spoorroute-kolen-kostenko-temirtau-kostenko-kmz.geojson` (42,9 km, 85 edges, 152 punten).
[13] Esri World Imagery via `sat_check.py` — `v2/build-cache/satcheck/sat-kolen-kostenko-temirtau-{kostenko-mijn,kmz-werk,kmz-werk-z16}.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Recept:** `bash v2/tools/bak_stromen.sh kolen-kostenko-temirtau` (functie `bak_kolen_kostenko_temirtau`); b1 vooraf gerouteerd met
`BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=49.8596,73.1139 --naar=50.0466,73.0343 --naam=kolen-kostenko-temirtau-kostenko-kmz --hoofd-km=1000`.
Uitvoer: `v2/data/stroomroute-kolen-kostenko-temirtau.json` (3,5 KB), contract versie 2, punt_formaat lonlat.

| # | modaliteit | km | punten | stippel |
|---|---|---|---|---|
| b1 | spoor | 43,7 (router 42,9 + ankerstukjes) | 152 | nee, doorgetrokken |

**Totaal 43,7 km, 152 punten, 2 markers** (Kostenko 0,18 km en KMZ 0,29 km van de lijn). Naden: één been, dus geen naad. `toets_knikken`: 0 knikken, 0 omkeringen.
**Km-toets:** geen gepubliceerde spoorkm; 43,7 is routerkm (hemelsbreed 21,6), dus alleen indicatie. Geen zee, haven-aanloop, stippel, kopie, lucht of leiding.
**Lessen:** (1) de gebakken lijn (43,7) is iets langer dan de routerkm (42,9) omdat hecht_marnet de lijn bij de uiteinden op de eigen punten laat aansluiten; (2) de
verhouding 1,99 komt van de noordoostelijke boog van het Kazachse net, niet van een terugloop; (3) mijnstatus en koppeling blijven de open punten van §7.
