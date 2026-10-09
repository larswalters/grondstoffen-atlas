# Routebrief (licht) · gas — Agua Dulce (Texas) → Brownsville → Tuxpan (Mexico)

**stroom-id:** `gas-aguadulce-tuxpan` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** Pijpgas uit het Agua Dulce-knooppunt (Nueces County, Texas) gaat via Valley Crossing Pipeline (Enbridge, 168 mijl,
ca. 270 km) langs twee compressiestations naar de kust bij Brownsville en de offshore-aansluiting, loopt dan als 42-inch Sur de Texas-Tuxpan
(TC Energy 60% / IEnova-Sempra 40%, 770 km gepubliceerd) onder de Golf van Mexico en de Tamiahua-lagune naar een meet-/compressiestation bij Tuxpan (Veracruz).
**Welke as van het verhaal:** *VS-gas naar de Mexicaanse elektriciteitsmarkt* — de grootste Zuid-Texas-exportroute. Volume: capaciteit 2,6 bcf/d ≈ 26,9 bcm/j,
25-jarig CFE-transportcontract, in bedrijf sept. 2019 [2][5]; werkelijke doorzet niet gevonden. Context: VS-pijpexport naar Mexico 6,4 bcf/d (≈ 66 bcm/j) in 2024, piek 7,5 bcf/d mei 2025 [1].

## 1 · Ketenkaart
```
Agua Dulce Compressor Station 1 `gas-aguadulce-cs1` (bij het Agua Dulce-knooppunt, Valley Crossing-begin)
  ──(b1 leiding · Valley Crossing via station 26.0565,-97.5143 → CS2 · hemelsbreed 242,5 km, STIPPEL: niet in OSM)──►
Compressor Station 2 Brownsville `gas-valleycrossing-cs2` ──► offshore-begin Sur de Texas-Tuxpan 25.9683,-97.0115 (zee, geen marker)
  ──(b2 leiding · Sur de Texas-Tuxpan 42" onderzees · 739,9 km OSM, doorgetrokken)──►
Tuxpan-meetstation `gas-tuxpan-aansluiting` — stoppunt (begin Tuxpan-Tula-systeem, CFE)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-aguadulce-cs1` → offshore-begin 25.9683,-97.0115 (via station, CS2) | Valley Crossing Pipeline, Enbridge, 42"/48" | hemelsbreed 242,5 km, geen wegkm; gepubliceerd 168 mijl ≈ 270 km [5], 177 mijl ≈ 285 km [3] | 3 × `--stippel` | ja: Valley Crossing staat niet in OSM (alleen CS1, CS2 en één station-polygoon) [7][8] |
| b2 | A | leiding | offshore-begin → `gas-tuxpan-aansluiting` | Sur de Texas-Tuxpan Gas Pipeline: OSM-ways 921735480 + 1279403582 + 1279403585 (substance gas, 42") | 770 [2][4] (800 [4], 497 mijl ≈ 800 [5]); OSM **739,9** = −3,9% | vooraf gestikt geojson (`maak_leidingbeen_gas_aguadulce_tuxpan.py`, FeatureCollection, patroon raslaffan_taweelah) | nee |

OSM-ways, met de OSM-API op 2026-10-09 opgehaald: 921735480 = 171 pt, 467,0 km, 25.9683,-97.0115 → 22.5503,-97.9070 (underwater, grootste segment 19,4 km = rechte zeebodemligging) ·
1279403582 = 131 pt, 242,8 km, → 21.2351,-97.4644 (underwater; loopt onder de Tamiahua-lagune, aanlanding aan de westoever) · 1279403585 = 78 pt, 30,1 km, → 20.9868,-97.3808 (underground).
Naden 22 m en 28 m: de tool legt ze aan elkaar. Zijarm **1279403584** (Naranjos, 30,7 km, 21.2349,-97.4646 → 21.4651,-97.6101) weglaten: andere bestemming, geen bron.
Totaal getekend 982,4 km tegen ca. 1.040 km gepubliceerd (270 + 770), −5,5% (indicatie, geen wegkm); stippel 242,5 km = 25% van de lengte.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-aguadulce-cs1` | begin Valley Crossing (compressor, header) | Valley Crossing Pipeline Compressor Station 1 = "Agua Dulce Compressor Station" | 27.7486, -97.8143 | [6][8] | bron-gelegd (z17 gezien: ommuurd compressorterrein met acht compressortreinen in een rij en een transformatorveld, direct noord van FM 2826 en 1,1 km oost van de kruising met FM 666; TCEQ noemt 0,7 mijl (1,1 km) oost van die kruising; OSM-way 921735488 bbox-midden) |
| `gas-valleycrossing-station` | via-punt stippel (geen marker) | OSM-polygoon "Valley Crossing Pipeline", Cameron County | 26.0565, -97.5143 | [8] | onzeker (z15 gezien: akker met een rechte lichte strook van 1 km, geen faciliteit zichtbaar; alleen een OSM-naamlabel) |
| `gas-valleycrossing-cs2` | compressor, laatste Texas-station | Valley Crossing Pipeline Compressor Station 2, Brownsville | 25.9903, -97.3584 | [7][8] | bron-gelegd (z17 gezien: omheind compressorterrein met vijf treinhuizen en leidingmanifolds op een zandvlakte ten noorden van het Brownsville-havenkanaal) |
| `gas-sdt-begin` | begin OSM-leiding op zee (geen marker) | begin way 921735480, ca. 12 km oost van de Rio Grande-monding | 25.9683, -97.0115 | [7] | aannemelijk (open zee, geen satellietblik mogelijk; valt samen met "grens/aansluiting op zee" in TC Energy-materiaal) |
| `gas-tuxpan-aansluiting` | staart, stoppunt | einde way 1279403585, Tuxpan | 20.9868, -97.3808 | [2][7] | bron-gelegd (z17 gezien: ommuurd gasstation met leidingwerk en gebouwen, tweede klein terrein 200 m zuidelijk; dat dit het Tuxpan-Tula-begin is staat alleen in het ontwerp) |

Hergebruik: geen. Het OSM-label "Agua Dulce Natural Gas Hub" (27.7522, -97.8428, node 10009350751) is een plaatsnaam in een akker: niet gebruikt als anker. De aanlanding 21.2350, -97.4645 is geen site en krijgt geen marker.

## 4 · Via-punten
Niet van toepassing: beide benen zijn leiding (stippel of OSM-way), geen corridorkeuze zoals bij weg of spoor.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Agua Dulce CS1 + header | Valley Crossing Pipeline LLC (Enbridge, voorheen Spectra) | Agua Dulce-gas → Valley Crossing 42"/48" | 2,6 bcf/d ≈ 26,9 bcm/j (header 5 bcf/d) | [3][5][6] |
| Tuxpan-meetstation | Infraestructura Marina del Golfo (TC Energy 60% / IEnova-Sempra 40%) | Sur de Texas-Tuxpan → Tuxpan-Tula en CFE-net | 2,6 bcf/d ≈ 26,9 bcm/j | [2][4][5] |

## 6 · Stoppunt
De brief stopt bij het meetstation in Tuxpan: daarna is het gas CFE-netgas voor centrales in Tamaulipas en Veracruz, en geen bron koppelt de stroom aan één centrale of één molecuul aan één afnemer. Fase D (centrale) vervalt, fase E vervalt. Het Southeast Gateway-vervolg (420 km offshore, 2021 aangekondigd [2]) is geen onderdeel van deze stroom.

## 7 · Open punten
- **Valley Crossing is geen Sempra-leiding maar van Enbridge** [3][5]; Sempra zit alleen via IEnova in de Mexicaanse helft (40%). Het ontwerp noemt het ten onrechte Sempra-leiding.
- **Het startanker uit het ontwerp (hub-label 27.7522, -97.8428) is vervangen** door CS1, 2,8 km oostelijk (27.7486, -97.8143): daar staat aantoonbaar compressie, het label ligt in een akker. De header zelf is niet gevonden, CS1 is de dichtstbijzijnde bewezen faciliteit.
- **Tracé Valley Crossing onbekend:** de stippel loopt rechtlijnig CS1 → station → CS2 → offshore-begin; het echte tracé (Kenedy/Willacy/Cameron County) is niet gekarteerd. Het station 26.0565, -97.5143 is onzeker; ontbreekt het op de route, dan is b1 8 km korter. Gepubliceerd 168 mijl (270 km) tegen 242,5 km hemelsbreed.
- **Offshore-begin niet bevestigd als grensaansluiting:** 25.9683, -97.0115 is het OSM-wayeinde; de FERC-grenssectie (1.000 ft) zit volgens [3][5] in Texaanse wateren, de exacte positie niet gevonden.
- **Gepubliceerde lengte Sur de Texas-Tuxpan wisselt** (770 [2][4], 800 [4], 497 mijl [5]); OSM 739,9 km (−3,9% tegen 770).
- **Aanlanding in de Tamiahua-lagune en Naranjos-arm** zijn alleen OSM-geometrie; het Tuxpan-Tula-aansluitpunt en de CFE-afname per centrale zijn niet door een bron gedekt.
- **Geen meting van de doorzet** op deze leiding; 26,9 bcm/j is capaciteit, geen flow. Sitelaag mist alle drie de sites; gloedgewicht uit deze brief ca. 26,9 bcm/j per site, centraal aan te vullen.
- Een tweede compressorterrein 800 m noord van CS1 en één bij 27.754, -97.822 (andere eigenaar, niet Valley Crossing) staan op hetzelfde beeld: niet gebruikt.

## 8 · Bronnen
[1] EIA, "Today in Energy", 20 okt. 2025 — VS-pijpexport naar Mexico 6,4 bcf/d (2024), piek 7,5 bcf/d mei 2025; Sur de Texas-Tuxpan voert gas vanaf Agua Dulce. https://www.eia.gov/todayinenergy/detail.php?id=66404
[2] Global Energy Monitor wiki, "Gasoducto Sur de Texas-Tuxpan" — 770 km, 42", 2,6 bcf/d, TC Energy 60% / IEnova 40%, in bedrijf sept. 2019, Southeast Gateway. https://www.gem.wiki/Gasoducto_Sur_de_Texas-Tuxpan
[3] Global Energy Monitor wiki, "Valley Crossing Pipeline" — Enbridge, 177 mijl, 42"/48", 2,6 bcf/d, Agua Dulce → grens in de Golf, 1.000 ft FERC-grenssectie. https://www.gem.wiki/Nueces_to_Brownsville_Pipeline
[4] TC Energy, "Sur de Texas-Tuxpan Pipeline" — 770/800 km, 2,6 bcf/d, Brownsville → Tuxpan. https://www.tcenergy.com/operations/natural-gas/sur-de-texas-tuxpan-pipeline/
[5] Oil & Gas Journal, "TransCanada-IEnova JV to build 2.6-bcfd Texas-Mexico pipelines" — Valley Crossing 168 mijl Agua Dulce hub → Brownsville, Sur de Texas-Tuxpan 497 mijl 42", CFE 25 jaar. https://www.ogj.com/pipelines-transportation/article/17250275/transcanadaienova-jv-to-build-26bcfd-texasmexico-pipelines
[6] TCEQ, Agreed Order Docket 2024-0247-AIR-E, Valley Crossing Pipeline LLC — "Agua Dulce Compressor Station", 0,7 mijl oost van FM 666/FM 2826, Banquete, Nueces County. https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2024/2024-0247-air-e.pdf
[7] OpenStreetMap (ODbL), ways 921735480, 1279403582, 1279403585 (man_made=pipeline, Sur de Texas-Tuxpan Gas Pipeline), 1279403584 (Naranjos-arm), opgehaald via de OSM-API 2026-10-09; Texas-extract gescand: geen Valley Crossing-pijpway. https://www.openstreetmap.org/way/921735480
[8] OpenStreetMap (ODbL), ways 921735488 "Valley Crossing Pipeline - Compressor Station 1" en 921735489 "… Station 2" (operator Valley Crossing Pipeline, LLC), node 10009350751 "Agua Dulce Natural Gas Hub", polygoon "Valley Crossing Pipeline" (Photon). https://www.openstreetmap.org/way/921735488
[9] Pipeline & Gas Journal, "Valley Crossing pipeline goes in service to Mexico", apr. 2019 — 168 mijl, Agua Dulce → leiding in Mexico. https://pgjonline.com/magazine/2019/april-2019-vol-246-no-4/global-news/valley-crossing-pipeline-goes-in-service-to-mexico
[10] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-aguadulce-tuxpan-cs1-z17.png`, `-aguadulce-cs.png`, `-cs2-z17.png`, `-cs2.png`, `-station.png`, `-tuxpan-z17.png`, `-tuxpan.png`, `-landing.png`, `-hub.png`.
## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)

**Bestand:** `v2/data/stroomroute-gas-aguadulce-tuxpan.json` (9,4 KB, contract versie 2, lonlat) · functie `bak_gas_aguadulce_tuxpan()` in `v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh gas-aguadulce-tuxpan` · titel "Gas · Agua Dulce (Texas) → Brownsville → Tuxpan (Mexico), Valley Crossing + Sur de Texas-Tuxpan".

| # | modaliteit | been | km | stippel | toets |
|---|---|---|---|---|---|
| 1 | leiding | Valley Crossing CS1 → station 26.0565,-97.5143 | 190,5 | ja | hemelsbreed, geen wegkm |
| 2 | leiding | station → CS2 Brownsville | 17,2 | ja | hemelsbreed |
| 3 | leiding | CS2 → offshore-begin 25.9683,-97.0115 | 34,8 | ja | hemelsbreed, kruist kuststrook |
| 4 | leiding | Sur de Texas-Tuxpan 42 inch (OSM-ways 921735480 + 1279403582 + 1279403585) | 739,9 | nee | -3,9% tegen 770 |

Totaal **982,4 km**, 386 punten, 3 markers (CS1, CS2, Tuxpan-meetstation). Stippel 242,5 km = 25%. Totaal -5,5% tegen ca. 1.040 km gepubliceerd (indicatie: b1 is hemelsbreed).
Naden: 0,000 / 0,000 / 0,000 km (b3 → b4 0,007 km). Markers 0,000 / 0,000 / 0,002 km van hun lijn.

**Recept.** b4 vooraf gestikt met het nieuwe `v2/tools/maak_leidingbeen_gas_aguadulce_tuxpan.py` (OSM-API, drie ways in die volgorde, oriëntatie op het dichtstbijzijnde uiteinde, naden 22 m en 28 m, FeatureCollection met 380 punten) → `v2/build-cache/ais/graaf/gas-aguadulce-tuxpan-leiding-sdt.geojson`; Naranjos-arm 1279403584 weggelaten. b1-b3 drie `--stippel "leiding|…"`. Geen zee, weg, spoor, haven-aanloop, via-punten of kopieën; geen zwaar rekenwerk buiten de bake (18 s).

**Stippels (reden).** b1-b3: Valley Crossing staat niet in OSM (alleen CS1, CS2 en een stationlabel), dus rechte lijnen tussen de drie bewezen/onzekere punten, "geen net op deze korrel" in de beennaam. Het echte tracé door Kenedy/Willacy/Cameron County is niet gekarteerd; het station 26.0565,-97.5143 is onzeker (b1 is zonder dat station 8 km korter). b3 kruist de kuststrook schematisch.

**Leiding.** b4 is doorgetrokken omdat OSM de leiding heeft (man_made=pipeline, 42 inch, substance gas); het onderzeese deel ligt als rechte zeebodemsegmenten (grootste 19,4 km). "aannemelijk: één bron" staat in de beennaam, niet in de lijnstijl.

**Toetsbevindingen.** `toets_knikken.py`: 3 knikken ≥ 60° in b4 (22.55043,-97.90682 148° R 12 m; 21.23508,-97.46440 90°; 21.23484,-97.46449 89°), alle OSM-geometrie bij de way-naad en de Tamiahua-aanlanding, 0 omkeringen, 0 terugloop; geen ingreep. `toets_rechte_benen.py`: alleen de drie stippels (omwegfactor 1,000 = stippel met reden, in orde). Afwijking van het ontwerp: geen; het stroom-id noemt Tuxpan en de lijn eindigt daar.

**Open.** Zie §7; daarbij bevestigt de bake dat de sitelaag de drie sites mist (gloedgewicht ca. 26,9 bcm/j per site, centraal aan te vullen) en dat de markers CS1/CS2/Tuxpan een gloedhotspot zonder gewicht zijn totdat dat gebeurt.

**Lessen.** Voor een onderzeese OSM-leiding volstaat een stik-script met oriëntatie op het dichtstbijzijnde uiteinde; de naden (22 en 28 m) vallen ruim binnen de 5 km. Een leidingketen die voor een kwart uit stippel bestaat is hier acceptabel, omdat het onderzeese hoofdstuk (75%) doorgetrokken is en de stippel de landzijde is waar OSM de Valley Crossing niet kent.
