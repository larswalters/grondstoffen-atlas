# Routebrief (licht) · Koper · Mirador → Fertisa → Tongling (Ecuador)

**stroom-id:** `koper-mirador-tongling` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** koperconcentraat uit de Mirador-mijn (Ecuacorriente, Zamora-Chinchipe; eigenaar CRCC-Tongguan = Tongling Nonferrous + China Railway Construction) per **truck** via Gualaquiza, Sígsig, Cuenca en de Cajas naar de privéterminal **Fertisa** in Guayaquil, per **zeeschip** over de Stille Oceaan naar de Yangtze-monding en per **binnenvaart** (gedeeld been) naar de kade van Tongling — de eigenaar-smelter (aannemelijk: één bron voor de bestemming, zie §6).
**Welke as van het verhaal:** *Ecuador als nieuw koperland, Chinees bezit van mijn tot smelter.* Volume: eerste lading jan 2020 = 22.000 t concentraat (Expreso 15-1-2020); jan–okt 2023 483,9 kt concentraat geëxporteerd (Expreso 12-11-2023; ≈ 580 kt concentraat/jaar bij lineaire extrapolatie; Cu-inhoud niet gebrond). Plan 2008 (30.000 t erts/dag): 137 Mlb ≈ 62 kt Cu/jaar (Wikipedia) — de mijn maalt nu 60.000 t/dag, dus het plangetal is een ondergrens, geen actueel cijfer.

## 1 · Ketenkaart
```
Mirador-concentrator `cu-mirador-laad` ──(b1 truck · E45 → E594 → Cuenca → E582 Cajas → E25 → E40 · 392,8 km geometrie)──►
Fertisa-kade, Guayaquil `cu-fertisa-kade` ──(b2a haven-aanloop, stippel, 93,2 km)──► zeeknoop 5155 ──(b2 zee · 16.704,6 km)──►
Yangtze-monding `cu-shanghai-kade` ──(b3 binnenvaart · 516,5 km · LETTERLIJKE KOPIE koper-collahuasi-tongling)──►
Tongling-kade `cu-tongling-kade` (smelter TNMG, aannemelijk via eigenaar) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Mirador-concentrator → Fertisa | E45 Gualaquiza → E594 Sígsig/Gualaceo → Cuenca → E582 Cajas → E25 Troncal de la Costa → E40 | hemelsbreed 217 km, geen wegkm; nieuwsbron 220 mijl ≈ 354 km [3]; OSRM-indicatie 379 km [9]; gemeten geometrie 392,8 km (+10,9% op 354, +3,6% op OSRM) | maak_stroombeen_weg (extract ecuador) | nee |
| b2a | B | zee | Fertisa-kade → zeeknoop 5155 (-2.3600,-80.0093) | Río Guayas / Golf van Guayaquil | 93,2 km over water (kade ligt 16,3 km hemelsbreed van de knoop; > 5 km) | maak_havenaanloop | **ja: haven-aanloop (MARNET reikt niet tot de kade)** |
| b2 | B | zee | zeeknoop 5155 → Yangtze-monding (31.51,121.4187) | Stille Oceaan, Oost-Chinese Zee (geen Malakka, geen Panama) | 16.704,6 km (MARNET; reis 38 dagen volgens [2]) | MARNET | nee |
| b3 | C | binnenvaart | Yangtze-monding → Tongling-kade | Yangtze, oostgeul | 516,5 km gemeten | LETTERLIJKE KOPIE `rivierbeen-yangtze-tongling-gedeeld.geojson` (zie koper-collahuasi-tongling b3) | nee |

Totaal testbake 17.707 km (392,8 + 93,2 + 16.704,6 + 516,5); naad zee→rivier 1,8 km, geen naad > 5 km.
Aannemelijk-vlag: bestemming Tongling = één bron (Expreso noemt Tongling bij de eerste lading; eigenaar TNMG) — staat in de beennaam b2, niet in de lijnstijl.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-mirador-laad` | concentrator / laadplek | Mirador-concentrator (Ecuacorriente), El Pangui | -3.5650, -78.4545 | [1][6] | bron-gelegd (z15 gezien: langgerekt complex met molengebouw met blauw dak, indikker, stockpiles en kampgebouwen ca. 2,5 km WNW van de put; Wikipedia-coördinaat -3.578/-78.436 ligt zelf in de open put, z14 gezien, en is daarom GEEN laadanker) |
| `cu-fertisa-kade` | overslag truck → zee | Terminal Portuaria Fertisa, Guayaquil | -2.2543, -79.9082 | [2][4] | bron-gelegd (z15 gezien: ommuurd terrein met loodsen en blauwe daken aan de oostoever van de Guayas-geul, in een stedelijke wijk) |
| `cu-shanghai-kade` | Yangtze-monding (marker) | Shanghai/Luojing — HERGEBRUIK letterlijk uit koper-collahuasi-tongling | 31.42704, 121.47618 | [10] | bron-gelegd (bestaand anker) |
| `cu-tongling-kade` | losplek / smelter | Tongling Nonferrous (TNMG), kade — HERGEBRUIK letterlijk uit koper-collahuasi-tongling | 30.98656, 117.7718 | [10] | bron-gelegd (bestaand anker); afnemer aannemelijk (één bron, via eigenaar) |

Satellietbeelden: `v2/build-cache/satcheck/sat-koper-mirador-tongling-{mijn,concentrator,fertisa}.png`.

## 4 · Via-punten (alleen b1; elk punt snapt in de test op ≤ 0,07 km van een weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | E45/E594-aftakking, Gualaquiza | -3.4377, -78.6178 | keuze E594 naar Sígsig i.p.v. de Loja-route (zie §7) |
| b1 | 2 | E594 zuid van Sígsig | -3.2180, -78.7379 | houdt de lijn op de E594 en uit de zijtakken van Sígsig |
| b1 | 3 | E594 noord van Gualaceo | -2.8707, -78.7708 | laatste punt vóór de aansluiting op Cuenca; ligt buiten het stadscentrum |
| b1 | 4 | E582 west van Cuenca | -2.8679, -79.0862 | pint de Cajas-weg (E582) i.p.v. Cuenca-centrum (het ontwerp noemde -2.90,-79.00 = stadscentrum: bewust niet gebruikt) |
| b1 | 5 | E582 Cajas-pas | -2.7900, -79.2000 | keuze Cajas (E582) boven de omweg via Azogues |
| b1 | 6 | E25 Troncal de la Costa, Naranjal | -2.5565, -79.5539 | bevestigt de afdaling naar de kust |
| b1 | 7 | Puente Unidad Nacional (E40) | -2.1638, -79.8470 | pint de Guayas-oversteek; daarna naar Fertisa via de Av. 25 de Julio |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mirador-concentrator | Ecuacorriente (CRCC-Tongguan) | erts (open pit) → Cu-concentraat | 60.000 t erts/dag; Mirador 2 (140.000 t/dag) is gepland vanaf 2026-2028 | [5] |
| Fertisa-terminal | Fertisa (privé) | truck → zeeschip (bulk) | opslag tot 50.000 t; kanaaldiepte beperkt de schepen | [4] |
| TNMG-smelter, Tongling | Tongling Nonferrous | concentraat → anode → kathode | zie koper-collahuasi-tongling (金冠 + 金新) | [10] |

## 6 · Stoppunt
De brief stopt bij de kade van Tongling: Expreso noemt Tongling als bestemming van de eerste lading en TNMG is mede-eigenaar van de mijn, maar geen bron legt vast dat deze ladingen aan de kade van het TNMG-complex zelf lossen (aannemelijk, één bron); fase D/E vervallen (geen gedocumenteerde afnemer van de kathode).

## 7 · Open punten
- **Haven alleen via 2019-2020-bronnen:** Fertisa is gedocumenteerd voor de eerste lading (jan 2020) [2][4]; voor 2023 is geen haven gevonden. Een andere bron noemde een lading uit Puerto Bolívar (mrt 2020, niet terug te vinden); Puerto Bolívar komt in de brief alleen uit een planzin van Wikipedia [7] en is niet getekend.
- **Wegcorridor:** het ontwerp kiest Cuenca/Cajas. Primicias (31-10-2019) noemt 616 km via E40/E45 over El Pangui, Zamora en Loja als de toen opengestelde route; de Cuenca-route was toen onbegaanbaar [3]. Welke route nu de gewone is, is onbekend. De 354 km (220 mijl) komt uit de haalbaarheidstoets (nieuwsbron) en is niet teruggevonden in de gelezen artikelen.
- **Volume:** 483,9 kt is concentraat, niet Cu; het Cu-gehalte is niet gebrond (geen omrekening gemaakt). De 94 kt concentraat/jaar uit Primicias 2020 past niet bij de 2023-export; beide staan hier zoals gebrond.
- **Mijnstop:** Wikipedia meldt productiestop juni 2022; Expreso meldt export in 2023 — de mijn draait; november 2024 stond ze 19 dagen stil door stroomuitval [8].
- Last mile: geen aparte stukken; beide uiteinden liggen op 0,07 km (plant) en 0,20 km (kade) van het wegnet.

## 8 · Bronnen
[1] Wikipedia, "Mirador mine" (eigenaar CRCC-Tongguan, eerste export jan 2020, stop juni 2022, plan 2008, 137 Mlb Cu). https://en.wikipedia.org/wiki/Mirador_mine
[2] Expreso, 15-1-2020: 22.000 t, BBC Valparaíso, Fertisa, 38 dagen naar Tongling. https://www.expreso.ec/actualidad/economia/exportacion-cobre-inicia-22-000-toneladas-3395.html
[3] Primicias, 31-10-2019: route E40/E45 via El Pangui, Zamora, Loja (616 km), Cuenca-route nog niet begaanbaar, 28 t per trailer, Fertisa. https://primicias.ec/noticias/economia/cobre-mirador-exportara-puerto-guayaquil
[4] Primicias, jan 2020: Fertisa privépoort, opslag 50.000 t, 60.000 t Cu/jaar vergund, kanaaldiepte. https://primicias.ec/noticias/economia/por-el-puerto-de-fertisa-saldran-22-000-toneladas-de-cobre
[5] Expreso, 12-11-2023: 483,9 kt concentraat jan–okt 2023 (478,1 kt in 2022), 60.000 t/dag, Mirador 2. https://www.expreso.ec/actualidad/economia/mina-mirador-elevara-produccion-133-2028-179140.html
[6] Esri World Imagery via `v2/tools/sat_check.py` (z14-z15): `v2/build-cache/satcheck/sat-koper-mirador-tongling-*.png`.
[7] Wikipedia, "Corriente Resources" (planzin Puerto Bolívar, 250 mijl). https://en.wikipedia.org/wiki/Corriente_Resources
[8] Primicias, 6-11-2024: stroomuitval, 19 dagen stil, vrachtwagenvloot. https://primicias.ec/economia/cortes-luz-mirador-mina-ecuador-reinicia-operacion-parada-82740
[9] OSRM (router.project-osrm.org): Mirador → Fertisa 379 km via E45, E594, Cuenca, E582, E25, E40 (indicatie, geen wegkm).
[10] `v2/design/routebrieven/koper-collahuasi-tongling.md` (ankers Tongling-kade en Shanghai/Luojing, gedeeld binnenvaartbeen).
[11] El Oriente, jan 2020: Fertisa-terminal zuid-Guayaquil, BBC Valparaíso, 22.000 t. https://www.eloriente.com/articulo/concentrado-de-cobre-ecuatoriano-ya-se-exporta-al-granel/13741

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
`v2/data/stroomroute-koper-mirador-tongling.json` (280 KB, versie 2, lonlat): 4 benen, **17.707,1 km**, 14.168 punten, 4 markers. Recept: `bak_koper_mirador_tongling()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh koper-mirador-tongling`).

| # | modaliteit | km | naad naar volgend been | been |
|---|---|---|---|---|
| 1 | truck | 392,8 | 0,000 | Mirador-concentrator → Gualaquiza → Sigsig → Cuenca → Cajas → Naranjal → Fertisa (9.703 punten) |
| 2 | zee, **stippel** | 93,2 | 0,000 | haven-aanloop Fertisa → zeeknoop 5155 (schematisch, over water; `maak_havenaanloop`, gelukt) |
| 3 | zee | 16.704,6 | 1,818 | zeeknoop 5155 (-2.3600,-80.0093) → Yangtze-monding (MARNET) |
| 4 | binnenvaart | 516,5 | - | LETTERLIJKE KOPIE `rivierbeen-yangtze-tongling-gedeeld.geojson` |

- **Recept b1:** profiel `koper-mirador-tongling-mirador-fertisa` in `maak_stroombeen_weg.py` (9 punten, refs E45 E594 E582 E25 E40 E35, extract ecuador, venster 60, `trimStaart`), gescand met `wegscan_puur.py`; alle snaps <= 0,2 km, 52 keerlussen gesnoeid (392,7 → 392,5 km wegdeel; getekend 392,8). Het tussenbestand uit de testrun is met het profiel opnieuw gedraaid: zelfde km.
- **Wegkm-toets (bevinding):** brief 354 km (220 mijl, nieuwsbron, niet teruggevonden in de bron); gemeten 392,8 = **+10,9% op 354**, +3,6% op OSRM 379. Buiten de +-15%-norm valt het niet, maar boven de +-10% van het wegtool; de 354 is een nieuwsbronschatting, geen gemeten wegkm. Geen via-punt bijgeschoven.
- **Markers:** Mirador 0,000 km en Fertisa 0,000 km van de lijn; Tongling-kade 0,397 km (bestaand gedeeld anker); Shanghai/Luojing 4,449 km (bestaand gedeeld anker, Yangtze-monding-conventie: zeebeen eindigt op 31.51,121.4187). Naad zee → rivier 1,818 km (< 5 km, procesgat in de monding).
- **Haven-aanloop:** de kade ligt 16,3 km (hemelsbreed) van zeeknoop 5155, dus een aanloop van 93,2 km over water (75 punten); 3,2 km daarvan ligt volgens de 1:10M-kust over land (schematisch, 1:10M kent de Guayas-geul niet) en blijft daarom stippel.
- **Toetsen:** `toets_knikken.py`: truck 45 knikken, 2 omkeringen (beide echte scherpe bocht, v 1,4 en 1,5: Gualaceo -2.8446,-78.8834 en bij de mijn -3.5348,-78.5328; 0 terugloop), de rest spikes van OSM-zigzags (<= 34 m radius); `toets_rechte_benen.py --min-km 5`: geen rechte been in deze stroom. Contract: versie 2, punt_formaat lonlat, modaliteiten {truck, zee, binnenvaart}, elk been >= 2 punten.
- **Aannemelijk:** bestemming Tongling (één bron plus eigenaarschap) staat in de beennaam van b3; geen lijnstijl.
- **Lessen:** (1) het wegprofiel stond niet in `maak_stroombeen_weg.py` (alleen een testwrapper in de scratchpad); nu vast opgenomen, zodat de tweede run uit de cache komt. (2) De aanloop-geojson uit de testrun is rechtstreeks hergebruikt (geen tweede `maak_havenaanloop`-run).
