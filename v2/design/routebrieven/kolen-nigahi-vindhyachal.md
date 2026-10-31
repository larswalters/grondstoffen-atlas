# Routebrief (licht) · kolen — Nigahi → Vindhyachal (India)

**stroom-id:** `kolen-nigahi-vindhyachal` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** thermische kolen (subbitumineus, Singrauli-kolenveld) uit de dagbouw Nigahi (Northern Coalfields Ltd, Coal India) gaan per **spoor** over het
captive MGR-net (merry-go-round) van NTPC naar de kolenaflaad van NTPC Vindhyachal STPS (4.760 MW, Singrauli); daarna een korte stippel (eigen terrein) naar de
ketelhuizen. Stoppunt: de kool wordt daar verstookt. Meerdere bronnen koppelen Nigahi aan Vindhyachal, geen noemt de laadsiding of het tracé: **aannemelijk**.
**Welke as van het verhaal:** *India-binnenland, mine-mouth-kool naar de zwaarste centrale-site zonder zee.* Nigahi **21,56 Mt ROM (2024)**, 22,5 Mt (2023) [1];
het MGR-net van NTPC Vindhyachal vervoert Nigahi + Dudhichua samen **±60.000 t/dag** (ongedateerd, ≈ 21,9 Mt/j) [4]. Aandeel Nigahi in de centrale niet gepubliceerd
(sitelaag Vindhyachal 17,1 Mt/j, afgeleid, fase I-III [10]).

## 1 · Ketenkaart
```
Nigahi-laadlus `kolen-nigahi-laadlus` (zuidrand pit, einde pit-CHP-band)
   ──(b1 spoor · NTPC/NCL-MGR, OSM-spurs · 9,8 km router, geen gepubliceerde spoorkm)──► Vindhyachal-kolenaflaad `kolen-vindhyachal-aflaad`
   ──(b2 leiding/band · eigen terrein · ~1,0 km, stippel)──► NTPC Vindhyachal STPS `w-vindhyachal` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-nigahi-laadlus` → `kolen-vindhyachal-aflaad` (aannemelijk: één bron voor de koppeling) | NTPC/NCL-MGR (captive rail, OSM `railway=rail service=spur usage=industrial`) | **hemelsbreed 7,3 km, geen spoorkm gepubliceerd**; router 9,8 km (51 punten, 0 omkeringen); MGR-"loop length" Nigahi 19,6 km [4] = 2 x 9,8 (rondrit, indicatie) | toets_spoorroute (1-op-1-net, één run, geen via) | nee |
| b2 | C | leiding (band) | `kolen-vindhyachal-aflaad` → `w-vindhyachal` | eigen terrein NTPC (kolenaflaad, banden, ketelhuizen) | hemelsbreed ~1,0 km | `--stippel "leiding|…"` | **ja** — eigen terrein, net reikt niet ("last mile, geen net op deze korrel") |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-nigahi-laadlus` | mijn / laadsiding | Nigahi OCP, spoorlus op de zuidrand van de pit | 24.1171, 82.5974 | router-snap (0,00 km) [1][4][11] | aannemelijk (z15/z16 gezien: pitrand met CHP-gebouwen en een transportband die uitkomt bij de spoorlijn; GEM-pit 24.1350, 82.5994 ligt 2,0 km noordelijker midden in de pit, niet op spoor) |
| `kolen-vindhyachal-aflaad` | overslag / aflaad | Vindhyachal, kolenaflaad-/stockyard-spoorlus NW van de ketelhuizen | 24.1050, 82.6694 | router-snap, eindvertex van b1 [11] | aannemelijk (z15 gezien: zwarte kolenstapels, banden en rangeerlussen aan de NW-kant van de centrale; geen bron noemt de aflaadlus) |
| `w-vindhyachal` | afnemer, stoppunt | NTPC Vindhyachal STPS, Waidhan, Singrauli | 24.0972, 82.6736 | HERGEBRUIK letterlijk uit `v2/design/kolen-sitelaag.json` (w-vindhyachal; Wikipedia 24°05'50"N 82°40'25"E) [2]; GEM geeft 24.0983, 82.6719 (0,2 km) [3] | bron-gelegd (z15 gezien: ketelhuizen, schoorstenen met rookpluim, kolenparken en banden) |

## 4 · Via-punten
Geen. De proef met het site-anker 24.0972,82.6736 als doel gaf 27,6 km (3,4x hemelsbreed, 1 omkering van 170 graden): de router loopt dan twee keer om de
ballonlussen van de aflaad heen. Eindigen op de aflaadlus geeft 9,8 km, 0 omkeringen; zie §7.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nigahi OCP | Northern Coalfields Ltd (Coal India) | dagbouw → pit-CHP → silo → MGR-trein | 21,56 Mt ROM (2024); uitbreiding 18,75 naar 21 Mtpa vergund; silo 3.000 t | [1][4][12] |
| NTPC-MGR | NTPC Vindhyachal | 10 dieselloc, 5 rakes (47 wagons), loop Nigahi 19,6 km, 18 rakes/dag | ±60.000 t/dag (Nigahi + Dudhichua) | [4] |
| Vindhyachal STPS | NTPC | kolen → elektriciteit (ketelhuis) | 4.760 MW (13 eenheden) | [2][3] |

## 6 · Stoppunt
Het ketelhuis van Vindhyachal: een centrale zet kolen in één stap om in stroom — geen fase D/E. Eén gemeten spoorbeen plus een stippel over eigen terrein.

## 7 · Open punten
- **Koppeling in woorden, niet in tracé:** Wikipedia en GEM leggen Nigahi bij Vindhyachal [2][3][1]; een NTPC-slideshow (ongedateerd) [4] en een nieuwsbericht van 2019 [5] noemen Nigahi + Dudhichua als MGR-voeders.
  Geen bron geeft de laadsiding, het tracé of het tonnage Nigahi → Vindhyachal. b1 is daarom een router-tracé over OSM-spurs: **aannemelijk**.
- **Haalbaarheidstoets overgenomen, aanpassing bewust gewijzigd:** de toets raadde `naar = 24.0972,82.6736` aan (27,6 km, 1 omkering, ballonlussen dubbel). Gekozen: eindigen op de
  aflaad-eindvertex 24.1050,82.6694 (9,8 km, 0 omkeringen) en de laatste ~1,0 km als stippel. De 19,6 km "loop length" [4] is een rondrit en ondersteunt 9,8 km enkel. Alternatief 27,6 km staat in de bak-aanwijzingen.
- **GEM-pit staat niet op spoor** (24.1350, 82.5994); laadlus 24.1171, 82.5974 is de dichtstbijzijnde spoorknoop (snap 0,00 km). Een silo/CHP op de pitrand (24.1220-24.1265, 82.5915) is niet als anker gelegd.
- **Sitelaag mist Nigahi:** `kolen-sitelaag.json` heeft w-vindhyachal maar geen Nigahi-mijn; centraal aan te vullen (GEM 24.1350, 82.5994, 21,56 Mt ROM 2024, status bron-gelegd; niet vers op satelliet gelegd).
- **Geen 2026-gegevens** over MGR of FSA; het FSA NCL-Vindhyachal [6] is van 2019, de slideshow ongedateerd.
- **km-toets alleen indicatief** (geen gepubliceerde spoorkm): 7,3 km hemelsbreed, router 9,8 km.

## 8 · Bronnen
[1] Global Energy Monitor, Nigahi Coal Mine — 24.1350, 82.5994; NCL; ROM 22,5 Mt (2023), 21,56 Mt (2024); gekoppeld aan Vindhyachal. https://www.gem.wiki/Nigahi_Coal_Mine
[2] Wikipedia (EN), Vindhyachal Thermal Power Station — 24°05'50"N 82°40'25"E; NTPC; 4.760/4.783 MW; kolen uit de Nigahi-mijnen. https://en.wikipedia.org/wiki/Vindhyachal_Thermal_Power_Station
[3] Global Energy Monitor, Vindhyachal power station — 24.0983, 82.6719; 13 eenheden, 4.760 MW; coal source "domestic". https://www.gem.wiki/Vindhyachal_power_station
[4] Slideshare, CHP equipment and interlocks (NTPC Vindhyachal, ongedateerd) — MGR: 10 diesellocs, 5 rakes, loop length 19,6/25 km (Nigahi/DCH), 18 rakes/dag, ±60.000 t/dag, silo 3.000/4.000 t. https://www.slideshare.net/slideshow/chp-equipment-s-interlocks-complete-ppt/278959471
[5] PSU Watch, NTPC CMD bezoekt NCL-mijn Nigahi (12 jan 2019) — Vindhyachal volledig gevoed door NCL (Nigahi + Dudhichua), 26 dagen voorraad. https://psuwatch.com/latestnews/ntpc-cmd-visits-ncl-coal-mine-seeks-support-for-upcoming-power-stations
[6] Daily Pioneer, NTPC seeks more NCL coal under flexi scheme (2019) — NCL heeft FSA met Vindhyachal (pagina bij controle 404; inhoud via zoekresultaat). https://www.dailypioneer.com/2019/business/ntpc-seeks-more-ncl-coal-under-flexi-scheme.html
[7] PSU Connect, NCL supplies sufficient coal to the power houses (30 aug 2017) — NCL leverde boven contract aan NTPC-centrales incl. Vindhyachal. https://www.psuconnect.in/psu-news/ncl-supplies-sufficient-coal-to-the-power-houses
[8] India Environment Portal / Business Standard (23 sep 2012), Energy giants CIL, NTPC spar again — NCL MGR-afname via NTPC-captive rail. https://indiaenvironmentportal.org.in/news-clippings/energy-giants-cil-ntpc-spar-again
[9] OpenStreetMap (ODbL), india-latest.osm.pbf — spoor-spurs `usage=industrial` rond Singrauli, via het 1-op-1-net (`toets_spoorroute.mjs`, 3.260.717 edges). https://www.openstreetmap.org
[10] `v2/design/kolen-sitelaag.json` — w-vindhyachal: 24.09722, 82.67361; 17,1 Mt/j (fase I-III, afgeleid), status aannemelijk.
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15-z16): `v2/build-cache/satcheck/sat-kolen-nigahi-vindhyachal-laadlus.png`, `-centrale.png`, `-aflaadlus.png`, `-silo.png`.
[12] GEM Nigahi Coal Mine, bronnenlijst — milieuvergunning uitbreiding Nigahi 18,75 → 21 Mtpa. https://www.gem.wiki/Nigahi_Coal_Mine

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Recept:** functie `bak_kolen_nigahi_vindhyachal` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh kolen-nigahi-vindhyachal`) -> `v2/data/stroomroute-kolen-nigahi-vindhyachal.json` (2,0 KB, versie 2, lonlat). b1 hergebruikt de bestaande router-uitvoer `spoorroute-kolen-nigahi-vindhyachal-nigahi-vindhyachal.geojson` (`BAKE_SUFFIX=-raw toets_spoorroute.mjs`, hoofd-km 100, max-snap 10, geen via; 3.260.717 spoor-edges). Geen profiel in `maak_stroombeen_weg.py`.

| # | modaliteit | km | punten | naad | stippel |
|---|---|---|---|---|---|
| b1 | spoor, trein Nigahi OCP naar NTPC Vindhyachal (aannemelijk: één bron) | 10,2 | 51 | - | nee, doorgetrokken |
| b2 | leiding, kolenband aflaad naar ketelhuizen (eigen terrein) | 1,0 | 2 | 0,00 km | ja: eigen terrein, geen net op deze korrel |

Totaal 11,2 km, 53 punten, 3 markers (laadlus, aflaad, w-vindhyachal), alle 0,0 km van de lijn. Toetsen: `toets_knikken` 0 knikken en 0 omkeringen; `toets_rechte_benen` geen bevinding voor deze stroom; json laadt, modaliteiten {spoor, leiding}.
**Km:** b1 geometrie 10,2 km tegen router-opgave 9,8 km (+4%, edge-som tegen lijngeometrie) en hemelsbreed 7,3 km; er is geen gepubliceerde spoorkm, dus de +-15%-toets is alleen indicatief. De 19,6 km "loop length" is een rondrit (2 x 9,8).
**Toelichting stippel:** b2 is de laatste ~1,0 km (aflaadlus naar de ketelhuizen) als rechte stippel over eigen NTPC-terrein; OSM kent daar geen `man_made=pipeline` en de band is geen openbaar net. Geen zee, geen haven-aanloop, geen via-punten, geen kopie, geen lucht.
**Lessen / bevindingen:** (1) eindigen op de site-coördinaat gaf 27,6 km met een omkering van 170 graden; eindigen op de aflaad-eindvertex + stippel lost dat op. (2) Laad- en aflaadlus zijn router-snaps (aannemelijk), geen bron-ankers. (3) Sitelaag mist de Nigahi-mijn: centraal aanvullen (GEM 24.1350, 82.5994, 21,56 Mt ROM 2024); die pitcoordinaat ligt 2,0 km van de laadlus. (4) Het stroom-id noemt het werkelijke eindpunt (Vindhyachal); geen afwijking van het ontwerp.
