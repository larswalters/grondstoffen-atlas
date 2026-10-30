# Routebrief (licht) · kolen — Syferfontein-mijn → Secunda-kolenontvangst (Zuid-Afrika)

**stroom-id:** `kolen-syferfontein-secunda` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Steenkool van de Syferfontein-mijn (Sasol Mining, Secunda-complex, Mpumalanga) gaat over een **overlandband** (OSM `man_made=goods_conveyor`, 4 ways, 30,7 km gestikt) naar de kolenontvangst van **Sasol Synfuels Secunda** (Secunda CTL) — mine-mouth, geen weg, spoor of zee. Stoppunt: de kolenstapel aan de bandingang, want de gasificatie in Secunda zet de kool om in synthetisch brandstof.
**Welke as van het verhaal:** *Kolen als synfuel-grondstof: Sasol Mining naar Secunda CTL* — Syferfontein **8,4 Mt kolen ROM in 2025**, 7,9 Mt in 2024 (GEM Global Coal Mine Tracker [1], via de haalbaarheidstoets; GEM-pagina zelf niet te openen, 403). Secunda totaal ca. 37,3 Mt per jaar uit vier mijnen (Wikipedia [4], zonder jaartal). Eenheid Mt kolen per jaar.

## 1 · Ketenkaart
```
Syferfontein-schachtkop `kolen-syferfontein-schachtkop`
   ──(b1 leiding/band · Sasol-overlandband Syferfontein → Secunda · OSM 30,7 km, geen gepubliceerde lengte)──►
Secunda-kolenontvangst `kolen-secunda-kolenontvangst` ⏹ stoppunt (CTL-hoofdcomplex 2,1 km N, binnen het Sasol-terrein)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (band) | `kolen-syferfontein-schachtkop` → `kolen-secunda-kolenontvangst` | Sasol-overlandband Syferfontein → Secunda (aannemelijk: één bron voor de koppeling mijn–band), OSM-ways 1102903145 (1,92 km, geen naam) + 500048980 (0,20 km) + 499912256 (3,63 km, naam Conveyor Belt) + 499912259 (24,67 km vanaf knoop 5928522691, `content=coal`, naam Conveyor Belt) | **geen gepubliceerde lengte**; OSM gestikt **30,69 km** (ways 30,42 + twee naden 0,17 en 0,11 km, recht dichtgetrokken); hemelsbreed 20,45 km; een onverifieerd, ongedateerd document noemt "42 km" [8]: indicatie, de ±15 %-toets geldt niet als norm | `--been-geojson "leiding\|…"` — vooraf gestikt FeatureCollection (1 LineString, 68 punten) `v2/build-cache/ais/graaf/kolen-syferfontein-secunda-leiding-band.geojson` (al aangemaakt, patroon kolen-grootegeluk-medupi) | nee — doorgetrokken (OSM heeft de band; de naden zijn 0,1–0,2 km) |

Bewust niet getekend: de tweede feeder (way 1102903138, 12,2 km, voegt bij knoop 10092391797 in de hoofdband) en de andere banden van andere mijnen naar hetzelfde punt (27 km West, 21 km NW) — andere mijnen, eigen ketens. De 2,6 km stippel naar het GEM-punt uit het ontwerp vervalt (bindende toets): de band begint op de schachtkop.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-syferfontein-schachtkop` | mijn / schachtkop (kop van b1) | Syferfontein-schachtkop, beginpunt OSM-way 1102903145 | -26.3912, 29.2054 | [1][5][6] | aannemelijk (z15 gezien: headgear en laadcomplex op de kruisplek met een bandlijn die naar het oosten wegloopt; band-mijn-koppeling is één bron: GEM zegt dat de mijn in 1989 is opgezet om Secunda te voeden [1]) |
| `kolen-secunda-kolenontvangst` | losplek / kolenstapel Secunda (staart van b1) | Secunda-kolenontvangst, eindpunt OSM-way 499912259 | -26.5722, 29.1693 | [3][5][6] | bron-gelegd (z15 gezien: grote donkere kolenstapel met bandlijnen, direct ten zuiden van het CTL-procescomplex met koeltorens) |

Hergebruik: **geen** bestaand anker (de kolen-sitelaag kent Syferfontein/Secunda niet). Controlepunten, geen ankers: GEM-punt Syferfontein -26.4098, 29.2011 ligt 2,1 km ZZW van de schachtkop (z14 gezien: klein bebouwd complex aan de westrand van het mijngebied, geen schacht); Secunda CTL Wikipedia -26.5537, 29.1658 (2,1 km N van de bandingang); buurmarker `gas-secunda-leidingeinde` -26.5516, 29.1933 (stroom gas-temane-secunda, 3,3 km ONO, ander product, niet gebruikt).
Beelden: `v2/build-cache/satcheck/sat-kolen-syferfontein-secunda-schachtkop.png`, `-bandeinde.png`, `-gem.png`, `-ctl.png` [6].

## 4 · Via-punten
Geen: een band volgt één gekarteerd OSM-pad, er is geen corridorkeuze. Geen weg-, spoor- of zeebeen, dus geen extracts, geen haven-aanloop, geen MARNET, geen vlucht, geen letterlijke kopie. (De eigen PBF-scan van de bakker hoeft niet: het geojson is al gestikt uit de OSM-API.)

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Syferfontein colliery (ondergronds) | Sasol Mining (Sasol) | ROM-kool → band | 8,4 Mt ROM (2025), 7,9 Mt (2024) | [1] |
| Secunda CTL (Sasol Synfuels; Sasol II en III) | Sasol | steenkool → synthetische ruwe olie (Fischer-Tropsch) | 160.000 vaten per dag; kooltoevoer Secunda ca. 37,3 Mt per jaar uit vier mijnen (zonder jaartal) | [3][4] |

## 6 · Stoppunt
De brief stopt bij de kolenontvangst: Secunda CTL zet de kool in één stap om in synthetische brandstof binnen één terrein; fase D valt weg (geen bron die een afnemer buiten het terrein voor deze kool noemt), E vervalt. Een last-mile-been binnen het Sasol-terrein (2,1 km naar het CTL-punt) wordt niet getekend.

## 7 · Open punten
- **Koppeling mijn–band:** OSM-tags zeggen niet welke mijn de band voedt. Aannemelijk via de schachtkop-way 1102903145 (bandkop 0,2 km van de hoofdband) en [1]; Wikipedia Secunda noemt Syferfontein niet bij de vier kernmijnen, Wikipedia Sasol wel als Secunda-mijn [2][4]. Eén bron, dus aannemelijk.
- **Bandlengte:** geen gepubliceerde waarde; OSM 30,7 km (twee naden 0,17 en 0,11 km recht), een ongedateerd document noemt 42 km [8] zonder tracé: niet verzoend.
- **Geen `man_made=pipeline`:** de band staat als `goods_conveyor` (twee ways met `content=coal`, `covered=yes`); als doorgetrokken leiding getekend op besluit van de haalbaarheidstoets (patroon kolen-grootegeluk-medupi).
- **Volume:** 8,4 Mt (2025) is ROM van de mijn, geen gemeten levering over deze band; GEM-pagina niet zelf kunnen lezen (403), cijfers via de haalbaarheidstoets en een zoeksamenvatting (2021: ca. 9,3 Mt, 2023: 7,6 Mt; GEM-historie 2017: 10,9 Mt).
- **Sitelaag:** `kolen-sitelaag.json` heeft geen Syferfontein of Secunda; centraal aanvullen (door mij niet gewijzigd). GEM-punt ligt 2,1 km van de schachtkop, niet satelliet-gelegd als mijn.
- **Kort been** (31 km): dun volume en weinig verhaal op de bol; de andere Secunda-mijnen (Bosjesspruit, Brandspruit, Middelbult, Twistdraai, Impumelelo, Shondoni) bewust niet getekend.

## 8 · Bronnen
[1] Global Energy Monitor, Syferfontein coal mine: Sasol Mining, Secunda; opgezet 1989 voor Sasol Synfuels; ROM 2025 8,4 Mt, 2024 7,9 Mt (via haalbaarheidstoets en WebSearch-samenvatting 2026-10-30; pagina zelf 403). https://www.gem.wiki/Syferfontein_coal_mine
[2] Wikipedia (EN), Sasol: Syferfontein bij Bosjesspruit, Brandspruit, Middelbult, Twistdraai als Secunda-collieries; Sasol Mining ruim 40 Mt per jaar (opgehaald 2026-10-30). https://en.wikipedia.org/wiki/Sasol
[3] Wikipedia (EN), Secunda CTL: grootste kolenvloeibaarmakingsfabriek ter wereld, Sasol II (1980) en III (1984), 160.000 vaten per dag. https://en.wikipedia.org/wiki/Secunda_CTL
[4] Wikipedia (EN), Secunda, South Africa: vier mijnen leveren ca. 37,3 Mt kolen per jaar aan Sasol Synfuels. https://en.wikipedia.org/wiki/Secunda,_South_Africa
[5] OpenStreetMap (ODbL), ways 1102903145, 500048980, 499912256, 499912259 (`man_made=goods_conveyor`, twee met `content=coal`) en 1102903138, via de OSM-API 0.6 opgehaald 2026-10-30. https://www.openstreetmap.org/way/499912259
[6] Esri World Imagery via `v2/tools/sat_check.py` (z14-z15): de vier beelden onder §3.
[7] Sasol Mining, overzichtspagina: zes mijnen, ca. 40 Mt per jaar voor Secunda, Sasolburg en export (alleen via WebSearch-samenvatting; de pagina zelf gaf geen inhoud). https://sasol.com/index.php/what-we-do/energy/sasol-mining
[8] Ongedateerd document (Univ. Wisconsin-bibliotheek, OCR-tekst): conveyor bij Syferfontein, 42 km en 1,2 m breed, voor 20,7 Mt per jaar naar Secunda; onverifieerd. https://search.library.wisc.edu/digital/AM42DNFFQNI2X29B/text/A3C7E6O2MMQATU8C
[9] Eigen brieven: `gas-temane-secunda.md` (buurmarker leidingeinde) en `kolen-grootegeluk-medupi.md` (patroon band als leiding).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Recept:** `bash v2/tools/bak_stromen.sh kolen-syferfontein-secunda` (functie `bak_kolen_syferfontein_secunda`) → `v2/data/stroomroute-kolen-syferfontein-secunda.json` (2,1 KB, versie 2, lonlat).

| # | modaliteit | km (bake) | punten | naam | stippel |
|---|---|---|---|---|---|
| b1 | leiding (band) | 30,7 | 68 | overlandband Syferfontein-schachtkop → Secunda-kolenontvangst (OSM-band; aannemelijk: één bron voor de koppeling mijn-band) | nee, doorgetrokken |

Totaal 30,7 km · 2 markers: `kolen-syferfontein-schachtkop` (-26.3912, 29.2054; 1,0 m van de lijn) en `kolen-secunda-kolenontvangst` (-26.5722, 29.1693; 5,4 m van de lijn).

- **Leiding:** het vooraf gestikte geojson `v2/build-cache/ais/graaf/kolen-syferfontein-secunda-leiding-band.geojson` (FeatureCollection, 1 LineString) is ongewijzigd als `--been-geojson leiding` gebruikt; geen herroutering, geen MARNET-snap, geen extracts, geen haven-aanloop, geen stippel, geen via-punt, geen profiel, geen vlucht, geen kopie. De naden in het stiksel (0,17 en 0,11 km) zijn recht dichtgetrokken, ruim onder de 5 km-norm.
- **Toets:** lengte 30,7 km tegen OSM-stiksel 30,69 km (geen gepubliceerde waarde; het ongedateerde document met 42 km is niet verzoend, dus indicatie en geen +-15%-norm). Eén been, dus geen naad tussen benen. `toets_knikken.py`: 4 knikken >= 60 graden (spikes en een krappe bocht in de OSM-bandgeometrie bij -26.393/29.225, -26.580/29.168, -26.499/29.276, -26.580/29.172), 0 omkeringen, 0 terugloop; een transportband zonder wegfunctie, bewust niet gladgestreken. `toets_rechte_benen.py`: been niet gemeld.
- **Open (ongewijzigd):** koppeling mijn-band slechts één bron; bandlengte 30,7 (OSM) tegen 42 km (document) niet verzoend; band als doorgetrokken leiding op besluit van de haalbaarheidstoets (geen `man_made=pipeline`); volume 8,4 Mt is mijnvolume (ROM), geen gemeten bandlevering; `kolen-sitelaag.json` mist Syferfontein en Secunda (centraal aanvullen); tweede feeder 1102903138 en andere banden naar Secunda niet getekend.
- **Les:** een kort mine-mouth-been met een vooraf gestikt OSM-geojson is één functie van een handvol regels; er was geen slot, scan of extract nodig behalve het zwaar-slot voor de bake zelf.
