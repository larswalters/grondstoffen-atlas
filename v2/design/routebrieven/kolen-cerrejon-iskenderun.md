# Routebrief (licht) · kolen — Cerrejón → Puerto Bolívar → Isken Sugözü, Golf van Iskenderun (Colombia → Turkije)

**stroom-id:** `kolen-cerrejon-iskenderun` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) ·
**status:** gebakken
**Keten in één zin:** energiekool uit de Cerrejón-dagbouw (La Guajira) gaat per eigen normaalspoor 150 km naar
Puerto Bolívar, per capesize over de Atlantische Oceaan en de Straat van Gibraltar naar de Golf van Iskenderun
(~10.900 km) en komt daar via het drijvend overslagstation en de kolensteiger bij de Isken Sugözü-centrale aan land.
**Welke as van het verhaal:** Colombiaanse kolen naar Turkije — de tweede zeestraat naast Rotterdam. **Aannemelijk: één
bron voor de bestemming**: GEM zegt dat de ~3 Mt/j die het overslagstation lost "mainly" uit Colombia en Zuid-Afrika komt,
zonder mijnnaam; Cerrejón is de aanname (grootste Colombiaanse exporteur, 100% via Puerto Bolívar [3]). Volume: ~3 Mt/j gelost
(GEM [1]); Cerrejón 19,2 Mt in 2024 (kolen-sitelaag); Colombia → Turkije 6,57 Mt in 2024 (AXSMarine via Breakwave [5]). Aandeel
Cerrejón in de Sugözü-aanvoer is niet gepubliceerd. Eenheid: Mt kolen per jaar.

## 1 · Ketenkaart
```
Cerrejón-laadlus `kolen-cerrejon-laadlus` ──(b1 spoor · Vía Ferroviaria Albania–Puerto Bolívar · 150,6 km)──►
Puerto Bolívar `kolen-bolivar-kade` ──(b2 zee · Caribische Zee–Atlantische Oceaan–Gibraltar–Middellandse Zee · 10.932 km
router + haven-aanlopen 42,1 en 13,0 km)──► Isken Sugözü-kolensteiger `kolen-isken-sugozu-steiger` ── STOPPUNT
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | laadlus → Puerto Bolívar-pierlus | Vía Ferroviaria Albania–Puerto Bolívar — **letterlijke kopie van kolen-cerrejon-ruhr b1** | 150 operator [3]; 150,6 gemeten | kopie `spoorroute-kolen-cerrejon-ruhr-b1.geojson` | nee |
| b1b | A | spoor | laatste km Puerto Bolívar | — kopie stippel uit `bak_kolen_cerrejon_ruhr` | 0,3 | stippel 12.2391,-71.9739 → 12.23912,-71.97693 | ja — OSM-gat bij de pier |
| b2a | B | zee | kade Puerto Bolívar → zeeknoop 8957 | haven-aanloop — **letterlijke kopie** `kolen-cerrejon-ruhr-aanloop-bolivar.geojson` | 42,1 (kade 36,4 km van de zeeknoop) | maak_havenaanloop (bestaand) | ja — geen AIS/MARNET tot de kade |
| b2 | B | zee | zeeknoop 12.4470,-72.2363 → zeeknoop 3786 (36.8913,36.0022) | Atlantische Oceaan, Gibraltar (router passeert op 4 km), Middellandse Zee — aannemelijk: één bron | 10.932,4 gemeten; geen gepubliceerde lengte (ontwerp: ~10.500 schatting, +4%) | MARNET | nee |
| b2b | B | zee | zeeknoop 3786 → Sugözü-steiger | haven-aanloop Isken Sugözü, over water | 13,0 (kade 11,9 km van de zeeknoop; hemelsbreed 11,9) | `maak_havenaanloop.py` — **al gebakken** `kolen-cerrejon-iskenderun-aanloop-sugozu.geojson` | ja — MARNET reikt niet tot de kade |

Geen weg, leiding, binnenvaart of lucht. Geen last mile: het been eindigt op de steiger; de band naar de centrale (1,0 km) en het
drijvend station zelf worden niet getekend. Controle: scratch-bake (3 benen + 2 aanlopen) = 11.138,4 km, 1.324 punten, geen naad > 0,5 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-cerrejon-laadlus` | mijn / laadplek | Cerrejón-laadlus (keerlus + silo's) | 11.1260, -72.6350 | **hergebruikt letterlijk** uit `kolen-cerrejon-ruhr.md` §10 (daar z15 gezien) [2] | bron-gelegd |
| `kolen-bolivar-kade` | overslag spoor → zee | Puerto Bolívar-terminal | 12.2391, -71.9770 | **hergebruikt letterlijk** uit `kolen-cerrejon-ruhr.md` §10 (daar z15 gezien) [2] | bron-gelegd |
| `kolen-isken-sugozu-steiger` | overslag zee → land / stoppunt | Isken Sugözü-kolensteiger (bandsteiger met dolfijnen-kade, Golf van Iskenderun) | 36.8333, 35.8904 | [1][4][sat] | **aannemelijk** (z17 gezien: ca. 1 km lange bandsteiger vanaf de centrale naar het oosten, dan een rij dolfijnen 150 m naar het zuiden; dit is de kade; het drijvend station is op de tegel niet te zien) |
| `kolen-isken-sugozu-centrale` | afnemer (niet getekend) | Isken Sugözü-centrale, 2 × 605 MW | 36.8350, 35.8791 | GEM [1] (Wikipedia 36.835, 35.880) | bron-gelegd (z15: centrale met kolenstapels en 800.000 t-opslag; 1,0 km van de steiger) |

Beelden: `v2/build-cache/satcheck/sat-kolen-cerrejon-iskenderun-sugozu-steiger.png` (z15), `…-sugozu-pier-mid.png` (z17), `…-sugozu-pier-zw.png` (z17, de
zuidwestelijke werfhaven met sleepboten en een golfbreker: niet de kolenkade). De lange pier NO van de steiger (36.8343, 35.9065) hoort bij een
ander terrein (zandopslag), niet bij de centrale. De ketenontwerp-coördinaat 36.8337, 35.8925 lag 150 m open water oostelijk van de steiger en is
niet overgenomen.

## 4 · Via-punten
Geen. b1 volgt het gekopieerde spoor, b2 is MARNET (router), b2a/b2b zijn haven-aanlopen. Er bestaat geen eigen landbeen met een corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Drijvend overslagstation, Golf van Iskenderun | İSKEN Enerji (OYAK 100% sinds okt. 2025; daarvoor STEAG 51%) | zeeschip → lichters/band → steiger | ~3 Mt/j gelost | [1][4] |
| Isken Sugözü-centrale | idem | kolen → elektriciteit, 1.210 MW (GEM; Wikipedia 1.320 MW) | 800.000 t kolenopslag | [1] |

## 6 · Stoppunt
De brief stopt bij de kolensteiger van de centrale: dat is de enige gedocumenteerde ontvanger (één bron), en het eindgebruik (elektriciteit)
is geen goederenstroom. Fase D vervalt; fase E vervalt. Het overslagstation is niet apart getekend (niet gezien, geen coördinaat).

## 7 · Open punten
- **Herkomst Colombia niet mijn-specifiek.** GEM noemt Colombia en Zuid-Afrika zonder mijnnaam; Cerrejón is een aanname. Argus: Colombia ~73% van
  de Turkse centrale-import in 2020 [6]; Turkije nam in 2024 6,57 Mt Colombiaanse kolen [5]. Een Cerrejón-specifiek aandeel bij Sugözü ontbreekt.
- **Oldendorff-pagina (reloader Turkije, 2015) is 404**; het drijvend station is op satelliet niet zichtbaar. Alleen de steiger is gelegd.
- **Zeelengte niet gepubliceerd**; 10.932 km is de MARNET-meting, de ~10.500 uit het ontwerp is een schatting. Oost-Middellandse Zee-lijn
  (Kreta 101 km, Cyprus 99 km) niet nader getoetst.
- **Beide haven-aanlopen zijn schematisch** (Puerto Bolívar 36,4 km, Sugözü 11,9 km tot de zeeknoop; de laatste heeft 0,15 km land aan de uiteinden).
- Het spoorbeen deelt 151 km met `kolen-cerrejon-ruhr` (letterlijke kopie, ~1,4% van de ketenkm).
- Cerrejón-productie 2025/2026 is lager (Glencore-beperking 5-10 Mt); het volume bij Sugözü kan lager liggen dan de 3 Mt van GEM (oude 2015-bron).

## 8 · Bronnen
[1] Global Energy Monitor, "Isken Sugozu power station" — 36.83502, 35.879104; 2 × 605 MW; ~3 Mt/j "mainly from vessels arriving from Colombia and South Africa" via drijvend station; band naar 800.000 t opslag; eigenaar OYAK. https://www.gem.wiki/Isken_Sugozu_power_station
[2] `v2/design/routebrieven/kolen-cerrejon-ruhr.md` §10 + `bak_kolen_cerrejon_ruhr` — ankers laadlus en Puerto Bolívar, spoor 150,6 km, aanloop 42,1 km.
[3] GEM, "Puerto Bolivar coal export terminal" — alle Cerrejón-kolen gaan via Puerto Bolívar (via zoekresultaat); Cerrejón 22,0 Mt (2023), 19,2 Mt (2024). https://gem.wiki/Puerto_Bolivar_coal_export_terminal
[4] Wikipedia, "İsken Sugözü power station" — 1320 MW, in bedrijf sinds 2003, 36.835, 35.88; HEAL-verwijzing Iskenderun Bay. https://en.wikipedia.org/wiki/%C4%B0sken_Sug%C3%B6z%C3%BC_power_station · en Power Engineering, "Iskenderun dedication a joint Turkish German celebration" (alleen via zoekresultaat: transshipper in de baai, lichters naar de centrale-steiger; pagina gaf 403). https://www.power-eng.com/renewables/hydropower/iskenderun-dedication-a-joint-turkish-german-celebration/
[5] Breakwave Advisors (AXSMarine), "Colombia Cerrejon to cut coal output" (2025-04-14) — Colombia 2024: Zuid-Korea 10, China 6,65, Turkije 6,57 Mt van 56,96 Mt. https://www.breakwaveadvisors.com/insights/2025/4/14/colombia-cerrejon-to-cut-coal-output
[6] Argus Media, "Turkey softens coal import restrictions" (2021-10-21) — Colombië ~73% en Rusland ~19% van de Turkse centrale-import in 2020. https://argusmedia.com/ja/news-and-insights/latest-market-news/2265933-turkey-softens-coal-import-restrictions
[7] GEM, "Isken Sugozu Coal Terminal" — herkomst Colombia en Zuid-Afrika, eigenaar İSKEN; geen coördinaat. https://www.gem.wiki/Isken_Sugozu_Coal_Terminal
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15 en z17, 2026-10-29), bestanden met prefix `kolen-cerrejon-iskenderun-sugozu-`.
[mar] MARNET (`hecht_marnet.py route`), scratch-bake 2026-10-29: zeeknoop 3786 op 36.8913, 36.0022; zee 10.932,4 km, passeert Gibraltar op 4,3 km.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
**Bestand:** `v2/data/stroomroute-kolen-cerrejon-iskenderun.json` (25,2 KB, versie 2, lonlat) · titel *Kolen · Cerrejon naar Iskenderun (Turkije)* · functie `bak_kolen_cerrejon_iskenderun` in `v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh kolen-cerrejon-iskenderun`.
Geen profiel, geen extract, geen via-punten (geen eigen weg-, leiding- of luchtbeen).

| # | modaliteit | km gemeten | km brief | naad | stippel | been |
|---|---|---|---|---|---|---|
| 1 | spoor | 150,6 | 150 operator / 150,6 | 0 | nee | letterlijke kopie `spoorroute-kolen-cerrejon-ruhr-b1.geojson` (94 punten) |
| 2 | spoor | 0,3 | 0,3 | 0,00 | ja, OSM-gat bij de pier | kopie van de pierstippel uit `bak_kolen_cerrejon_ruhr` |
| 3 | zee | 42,1 | 42,1 | 0,00 | ja, MARNET reikt niet tot de kade | letterlijke kopie `kolen-cerrejon-ruhr-aanloop-bolivar.geojson` (60 punten) |
| 4 | zee | 10.932,4 | geen; schatting ~10.500 (+4,1%) | 0,00 | nee | MARNET, 91 edges, zeeknoop 12.4470,-72.2363 naar zeeknoop 3786 (36.8913,36.0022), 1.145 punten |
| 5 | zee | 13,0 | 13,0 | 0,00 | ja, MARNET reikt niet tot de kade | `kolen-cerrejon-iskenderun-aanloop-sugozu.geojson` (23 punten), zeeknoop naar steiger |

Totaal **11.138,4 km**, 1.324 punten, 3 markers; grootste naad 0,00 km. Markers: laadlus 0,45 km van de lijn (hergebruikt anker, de lijn begint op 11.1275,-72.6312 zoals bij kolen-cerrejon-ruhr), Puerto Bolivar-terminal en Sugozu-steiger 0,00 km.
Toetsen: `toets_knikken.py` 0 knikken, 0 omkeringen; `toets_rechte_benen.py --min-km 5` meldt deze stroom niet; json.load goed, modaliteiten {spoor, zee}, elk been >= 2 punten.

**Stippels en aanlopen.** b4 is doorgetrokken (gemeten MARNET-pad, Gibraltar op ~4 km). b3 en b5 zijn de twee haven-aanlopen: Puerto Bolivar 36,4 km en Sugozu 11,9 km van hun zeeknoop, beide schematisch over water en daarom stippel. b1b (pierstukje) is een OSM-gat.
**Aannemelijk: een bron.** Bestemming Turkije en Colombia als herkomst staan op GEM; Cerrejon als mijn is de aanname. Dat staat in de beennaam van de zeevaart en in de markernaam van de steiger, niet in de lijnstijl.

**Recept.** Eigen functie `bak_kolen_cerrejon_iskenderun` (model `bak_kolen_cerrejon_ruhr`): `--been-geojson spoor` (kopie) + `--stippel spoor` + `--stippel-geojson zee` (kopie aanloop Bolivar) + `--been zee` 12.44700,-72.23630 naar 36.89130,36.00220 + `--stippel-geojson zee` (aanloop Sugozu) + 3 markers. Graaf rijn-default `$GRAAF`, MARNET marnet-preais, NE build-cache.

**Lessen.**
- De "al gebakken" aanloop `kolen-cerrejon-iskenderun-aanloop-sugozu.geojson` stond kade naar zeeknoop; in reisvolgorde (zee, dan aanloop) gaf dat een naad van 11,85 km. Eigen bestand omgekeerd (coordinaten gespiegeld, zeeknoop naar steiger) en herbakken: naad 0,00. Een aanloop aan het EINDE van de keten moet zeeknoop naar kade lopen, een aanloop aan het begin kade naar zeeknoop.
- Het drijvend overslagstation is niet getekend (niet gezien, geen coordinaat); de lijn eindigt bij de steiger, de band naar de centrale (1,0 km) en de centrale zelf zijn niet getekend.
- Volume 3 Mt/j (GEM, 2015-opgave) en Cerrejon-aandeel blijven onbekend (zie §7).
