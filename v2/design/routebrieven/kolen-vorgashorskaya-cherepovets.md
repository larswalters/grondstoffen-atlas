# Routebrief (licht) · kolen — Vorgashorskaya → Pechora-lijn → Cherepovets (Rusland)

**stroom-id:** `kolen-vorgashorskaya-cherepovets` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** cokeskoolconcentraat van de Vorgashorskaya-wasserij bij Vorkuta (Vorkutaugol, Pechora-bekken, Komi, ver boven de poolcirkel) gaat in één treinreis van ~1.880 km over de Pechora-lijn (Inta, Ukhta, Mikun, Kotlas) en de Noordelijke Spoorweg (Konosha, Vologda) naar het kolenpark van de Severstal-cokesfabriek in Cherepovets (Vologda) — Russisch binnenland, geen zee. Afname door Cherepovets is **aannemelijk: één bron** (Severstal-offtake, zie §7).
**Welke as van het verhaal:** de Arctische cokeskoolas naar Noordwest-Russisch staal: Vorkutaugol is het Europese-Rusland-bekken dat sinds 2022 in handen van Russkaya Energiya is, maar met een offtake-contract Severstal blijft beleveren [2][3]. **Jaarvolume (peiljaar 2026, Mt kolen/j):** Vorkutaugol → Severstal 280 kt/mnd (≈ 3,4 Mt/j) tot april 2026, 180 kt/mnd (≈ 2,2 Mt/j) vanaf mei 2026, contract tot 30-04-2027 [3]; Vorgashorskaya zelf 3,18 Mt verkoopbaar in 2022 (schatting) [1]; **aandeel van deze mijn in de Cherepovets-levering niet gepubliceerd**.

## 1 · Ketenkaart
```
Vorgashorskaya-wasserij/laadspoor `kolen-vorgashorskaya-laad` (Vorkuta, Komi)
  ──(b1 spoor · mijnsiding → Inta → Ukhta → Mikun → Kotlas → Konosha → Vologda → Cherepovets · router 1.879,9 km, hemelsbreed 1.575)──►
Severstal-cokesfabriek, kolenpark `kolen-cherepovets-kolenpark` (Cherepovets) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-vorgashorskaya-laad` → `kolen-cherepovets-kolenpark` | Pechora-lijn Vorkuta–Inta–Ukhta–Mikun–Kotlas, dan Konosha–Vologda (**Konosha → Vologda-nadering ~184 km = dezelfde OSM-lijn als ree-lovozero-solikamsk b2**, eigen run, 0,0 km verschil), dan Vologda–Cherepovets; **aannemelijk: één bron** (Severstal-offtake) | **hemelsbreed 1.575 km, geen gepubliceerde spoorkm voor het geheel**; router 1.879,9 (bake telt ~1.889 over de punten) | toets_spoorroute (`BAKE_SUFFIX=-raw`, extract rusland-noordwest), één run zonder via-punten | nee |

**Toetsen op deelstukken** (b1 heeft zelf geen totaal-km, dus de ±15 %-toets is een indicatie):
- **Konosha → Kotlas:** gemeten 362,8 km tegen **367 km** (ru-Wikipedia, Pechora-spoorweg, Sevdvinlag-aanleg 1940-42) [5] = **−1,1 %**.
- **Vologda → Cherepovets:** gemeten 111,7 km tegen 126 km (ru-Wikipedia, stad-tot-stad-afstand, geen spoorkm) [6] = −11 %, indicatie.
- **Corridor-treffers** (afstand lijn tot het ontwerp-via-punt): Inta 0,9 km · Ukhta 0,5 · Mikun 0,3 · Kotlas 0,4 · Konosha 1,3 · Vologda 0,5; Pechora 0,8 en Sosnogorsk 0,7 km. 0 bochten ≥ 60° (keerstraf 25), 2 OSM-zigzagpunten gesnoeid. Snap kop 0,38 km, snap staart 0,18 km: geen naden, geen last-mile-been.
- **Het ontwerp-station Vorkuta (67.4700, 64.0280) en "mijn → station 55 km" kloppen niet:** de vrije route verlaat de mijn zuidwaarts naar Inta en blijft 12,9 km van dat stadspunt; geen via-punt in Vorkuta.

## 3 · Ankers (één per site; geen overslag onderweg)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-vorgashorskaya-laad` | wasserij / laadspoor (laadplek) | Vorgashorskaya-mijn en -wasserij, Vorkuta, Komi | 67.5930, 63.6244 | GEM-mijnpunt 67.5953, 63.6160 [1] ligt 0,45 km van het spoor op kaal dagbouwterrein; OSM-gebouw «Воргашорская» 67.5925, 63.6323 [7] | bron-gelegd (z16 gezien: wasserij met kolentoren en transportbanden, kolenstapels en een brede spoorbundel die er dwars doorheen loopt; het GEM-punt ligt 0,5 km ten NW van de wasserij; router snapt op 0,38 km) |
| `kolen-cherepovets-kolenpark` | losplek / kolenpark Severstal-cokesfabriek | Severstal Cherepovets, kolenpark van de cokesbatterijen, westzijde van het werk | 59.1214, 37.8267 | werken-centroïde OSM 59.13815, 37.85392 [7] (3,2 km NO); ligging kolenpark uit de satelliet | **aannemelijk** (z16 gezien: twee lange cokesbatterij-gebouwen met kolentoren en blustoren met stoompluim, ten oosten ervan een groot zwart kolenpark met banden en wagon-ontvangst langs een spoorbundel; geen bron noemt dit punt, wel dat Severstal hier cokeskool afneemt) |

Station Vorkuta, Inta, Ukhta, Mikun, Kotlas, Konosha en Vologda zijn **geen ankers**: de route loopt erdoorheen (controle, §2).

## 4 · Via-punten
Geen. Eén vrije run kop → staart (`BAKE_SUFFIX=-raw`, keerstraf 25) volgt de Pechora-lijn en de Noordelijke Spoorweg (haalbaarheidstoets + eigen controle); de Vorkuta-lijn heeft geen reële corridorkeuze tot Kotlas, en van Kotlas naar Konosha en Vologda kiest de vrije route zelf de hoofdlijn. Een via-punt in Vorkuta of Vologda zou alleen een omweg kosten.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Vorgashorskaya (mijn + wasserij) | Vorkutaugol (Russkaya Energiya, sinds april 2022) | ruwe kool → cokesconcentraat | 3,18 Mt verkoopbaar (2022, schatting); capaciteit 2,1 Mt/j volgens GEM (tegenstrijdig met 2022-cijfer, niet uitgezocht) | [1][2] |
| Severstal Cherepovets | Severstal | cokeskool → cokes → ruwijzer/staal | niet gevonden | [6][7] |

## 6 · Stoppunt
De brief stopt op het kolenpark van de Severstal-cokesfabriek: de cokes gaat binnen één werkterrein verder (cokesbatterij → hoogoven), zonder openbaar net en zonder bron voor een volgende locatie. Fase D vervalt (geen aparte fabriek buiten het werk), E vervalt.

## 7 · Open punten
- **Geen bron noemt Vorgashorskaya letterlijk als leverancier van Cherepovets.** Bekend: Vorkutaugol levert aan Severstal en blijft dat doen onder een offtake-contract na de verkoop (29-04-2022) [2]; Severstal is de hoofdafnemer [3]. Een zoekresultaat (metal-expo 2018, niet opgehaald: site onbereikbaar) meldt dat concentraat van Vorgashorskaya (1Zh/GZhO) in Cherepovets wordt gebruikt; Wood Mackenzie (via de haalbaarheidstoets, pagina niet opgehaald) zegt dat de output grotendeels naar Cherepovets gaat. Daarom beennaam **aannemelijk: één bron**.
- **Aandeel van deze mijn in de levering aan Cherepovets niet gepubliceerd** (Vorkutaugol heeft meerdere mijnen); de 3,4 en 2,2 Mt/j gelden voor Vorkutaugol als geheel.
- **Volume daalt en contract loopt af:** 280 → 180 kt/mnd vanaf mei 2026, contract tot 30-04-2027, goedkopere Kuzbass-kool vervangt Vorkuta [3]. De lijn is dus kwetsbaar; niet getekend als uitgefaseerd.
- **Kolenpark Cherepovets is afgeleid uit de satelliet** (cokesbatterijen met kolenpark); de werken-centroïde ligt 3,2 km ernaast en de ontvangsthal van Severstal is niet bron-aangewezen. Ook niet uitgesloten: dat een deel via een andere ontvangst loopt.
- **Spoorkm niet gepubliceerd** voor het geheel; alleen Konosha–Kotlas (367 km) [5] en Vologda–Cherepovets (126 km, stad-tot-stad) [6] zijn ruwe controles.
- **Geen tweede corridor getest** (bv. via Kirov): de vrije kortste route over het raw-1-op-1-net volgt Kotlas–Konosha.
- **Mijnsiding niet bron-gelegd:** het GEM-punt ligt op kaal terrein; het laadspoor is uit de satelliet afgeleid (spoorbundel door het wasserij-complex). OSM-gebouw «Воргашорская» ligt 0,4 km ten oosten van het anker, in hetzelfde emplacement.
- **Sancties/transportquota 2026** niet gecontroleerd; Vorkutaugol meldt een crisis en staatsteun [3].

## 8 · Bronnen
[1] Global Energy Monitor, Vorgashorskaya Coal Mine — 67.5953177, 63.6160208; Vorkutaugol 100 %; 3,18 Mt (2022, schatting). https://www.gem.wiki/Vorgashorskaya_Coal_Mine
[2] Interfax, 2022-04-29 — Severstal sluit verkoop Vorkutaugol aan Russkaya Energiya af (15 mld roebel); langlopend offtake-contract garandeert Severstal-levering. https://interfax.com/newsroom/top-stories/78816/
[3] The Barents Observer, 2026-04-30 — Vorkutaugol in crisis; Severstal hoofdafnemer; 280 → 180 kt/mnd vanaf mei 2026; contract tot 30-04-2027. https://www.thebarentsobserver.com/news/vorkuta-coal-company-reports-severe-crisisnbsp/449739
[4] Wood Mackenzie, Vorkutaugol coal mines (asset report) — via de haalbaarheidstoets; pagina door mij niet opgehaald (404). https://www.woodmac.com/reports/coal-vorkutaugol-coal-mines-16489076
[5] ru-Wikipedia, Печорская железная дорога — lijn Konosha–Kotlas 367 km (Sevdvinlag, eerste trein Kotlas 7-3-1942); beheer Kotlas. https://ru.wikipedia.org/wiki/Печорская_железная_дорога
[6] ru-Wikipedia, Череповец — 124 km west van Vologda, afstand 126 km; ChMK/Severstal grootste werkgever. https://ru.wikipedia.org/wiki/Череповец
[7] OpenStreetMap-bijdragers via Nominatim — Череповецкий металлургический комбинат «Северсталь» (man_made=works) 59.13815, 37.85392; building «Воргашорская» 67.59250, 63.63227; Воргашор (plaats) 67.58119, 63.78373 (ODbL). https://www.openstreetmap.org/copyright
[8] en-Wikipedia (MediaWiki API `prop=coordinates`), Vorkuta — stadspunt 67.5, 64.0333; Pechora-kolenbekken. https://en.wikipedia.org/wiki/Vorkuta
[9] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-kolen-vorgashorskaya-cherepovets-{mijn,laad,severstal,kokerij,kolen-zuid,vorkuta-stn}.png`.
[10] Eigen metingen `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`, 3.260.717 spoor-edges), uitvoer `v2/build-cache/ais/graaf/spoorroute-kolen-vorgashorskaya-cherepovets-vorkuta-cherepovets.geojson` (1.879,9 km, 1.202 edges, 3.346 punten).
[11] Routebrief `ree-lovozero-solikamsk` (§4) en `v2/build-cache/ais/graaf/spoorroute-ree-lovozero-solikamsk-b2-r3-obozerskaya-vologda.geojson` — Konosha → Vologda-nadering 0,0 km verschil.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-kolen-vorgashorskaya-cherepovets.json` (58,9 KB, versie 2, punt_formaat lonlat) · **functie:** `bak_kolen_vorgashorskaya_cherepovets` in `v2/tools/bak_stromen.sh` · **titel:** Kolen · Vorgashorskaya (Vorkuta) → Pechora-lijn → Severstal Cherepovets.

| # | modaliteit | been | km gebakken | km brief | naad | stippel |
|---|---|---|---|---|---|---|
| b1 | spoor | trein Vorgashorskaya-laadspoor naar Cherepovets-kolenpark (aannemelijk: een bron) | 1.889,3 (router 1.879,9) | geen spoorkm; hemelsbreed 1.575 | n.v.t. | nee, doorgetrokken |

Totaal 1.889,3 km · 3.346 punten · 2 markers (`kolen-vorgashorskaya-laad` bron-gelegd 67.5930,63.6244; `kolen-cherepovets-kolenpark` aannemelijk 59.1214,37.8267). Markers liggen 0,38 km resp. 0,18 km van de lijn (de router-snap uit §2); er zijn geen naden.

**Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=67.5930,63.6244 --naar=59.1214,37.8267 --naam=kolen-vorgashorskaya-cherepovets-vorkuta-cherepovets` (zonder via-punten, 3.260.717 spoor-edges, extract rusland-noordwest) levert `spoorroute-kolen-vorgashorskaya-cherepovets-vorkuta-cherepovets.geojson` in `v2/build-cache/ais/graaf/`; die staat letterlijk als `--been-geojson "spoor|…"` in de functie. Geen profiel, zee, haven-aanloop, kopie, lucht of leiding.

**Toets:** de bake-lengte over de punten (1.889,3 km) ligt 0,5% boven de routerlengte; de brief geeft geen spoorkm voor het geheel, dus de ±15%-norm is een indicatie (Konosha–Kotlas −1,1%, Vologda–Cherepovets −11%, zie §2). `toets_knikken.py`: 0 knikken, 0 omkeringen. Geen naad, 58,9 KB, één modaliteit (spoor), alle punten in lon,lat.

**Lessen:** een enkele spoorrun zonder via-punten is genoeg waar de Pechora-lijn geen corridorkeuze heeft; de bake-regel van een vooraf gebakken spoorgeojson hertelt de km over de punten (1.889,3 tegen 1.879,9), een verschil van 0,5%. Open punten uit §7 gelden onverkort: geen bron noemt Vorgashorskaya letterlijk als leverancier, het kolenpark is uit de satelliet afgeleid, het volume daalt (280 naar 180 kt/mnd vanaf mei 2026) en het contract loopt tot 30-04-2027.
