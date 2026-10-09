# Routebrief (licht) · zilver — Cuajone → Ilo-smelter → Ilo-raffinaderij (Peru)

**stroom-id:** `zilver-cuajone-ilo` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** koperconcentraat (met zilver als bijproduct) uit de Cuajone-concentrator van Southern Copper gaat per eigen SCC-industriespoor (1435 mm, enkelspoor) naar de Ilo-smelter aan de kust, de anodes gaan (aannemelijk per spoor) naar de raffinaderij met edelmetaalfabriek in hetzelfde Ilo-complex, waar uit de anodeslijk geraffineerd zilver komt; de lijn stopt op die fabriek.
**Welke as van het verhaal:** *Zuid-Peru, een zilverknoop zonder zilvermijn* — het zilver komt uit koperanodes van Toquepala en Cuajone samen en staat nergens per mijn. Jaarvolume: **130,5 t Ag/j geraffineerd in Ilo (2025; 126,6 in 2024; 109,7 in 2023)** [1][2]. Dat is het Ilo-totaal, niet het Cuajone-aandeel; Cuajone is de kleinere voeder (concentrator 90 kt erts/dag tegen 2 × 60 kt/dag bij Toquepala [2]). Het been vanaf Toquepala staat al op de bol als koper-keten `koper-toquepala-ilo` (zie §2).

## 1 · Ketenkaart
```
Cuajone-concentrator `ag-cuajone-conc` ──(b1 spoor · SCC-industriespoor via Toquepala-lijn · ~214 km)──►
Ilo-smelter `ag-ilo-smelter` ──(b2 spoor, aannemelijk · ~8 km)──►
Ilo-raffinaderij + edelmetaalfabriek `ag-ilo-raffinaderij` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Cuajone-concentrator → Ilo-smelter | SCC-industriespoor Cuajone–Toquepala (spur, grotendeels tunnel) en Toquepala–Ilo (1435 mm, 214 km lijn, 27 km tunnels) [2][3] | router 214,0; gepubliceerd 214 voor de héle lijn incl. de Toquepala-tak [1][2], Wikipedia Toquepala–Ilo 187 + tak ≈ 27–30 [3] — indicatie, ±15% geldt (0%) | toets_spoorroute (BAKE_SUFFIX=-raw, extract peru, --hoofd-km=100), één run, geen via-punt | nee |
| b2 | B | spoor | Ilo-smelter → Ilo-raffinaderij en edelmetaalfabriek | zelfde lijn: b1 passeert de raffinaderij 0,55 km westelijk en eindigt in de smelter, b2 rijdt dat laatste stuk terug (**aannemelijk: één bron — alleen "zelfde faciliteit", vervoerswijze niet gebrond**) | router 8,3; hemelsbreed 8,9 tussen de 10-K-punten [1]; geen gepubliceerde km | toets_spoorroute, zelfde vlaggen | nee |

**Gedeeld met een bestaande stroom:** vanaf het knooppunt -17.2632,-70.6464 (34 km van Cuajone) tot de smelter, 183,2 km, is de geometrie punt-voor-punt gelijk aan `spoorroute-koper-toquepala-ilo-a.geojson` (1040 gelijke punten; zelfde net, zelfde staart). Geen tweede versie getekend.

**Waarom de 10-K-afstanden hier niet gelden:** "121 km van Toquepala, 147 km van Cuajone" [1] zijn wegafstanden (10-K: bereikbaar per highway), geen spoorkm; het spoor is hemelsbreed 79,6 km maar 214 km lang (omwegfactor 2,7, bergspoor naar zeeniveau). Toetsen tegen 147 geeft vals alarm (+46%).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-cuajone-conc` | laadplek (concentrator, kop b1) | Cuajone-concentrator (Southern Copper, Torata, Moquegua) | -17.0640, -70.7690 | [1][2][sat] | bron-gelegd (z16 gezien: maalhal met drie grote indikkers, koepelopslag en rangeerterrein aan de zuidkant; OSM-spoor 0,12 km; het 10-K-projectcentroïde -17.0522,-70.7417 is geen anker: 3,1 km oostelijker op stortgebieden, 0,85 km van het net) |
| `ag-ilo-smelter` | losplek concentraat (smelter, staart b1, kop b2) | Fundición de Ilo (SCC), hergebruikt letterlijk uit `koper-toquepala-ilo.md` | -17.5050, -71.3590 | [1][osm][koper-brief] | aannemelijk (z15 gezien: kustcomplex met smeltgebouwen, tankpark en een 500 m-zuurpier; spoor loopt eroverheen, snap 0,08 km; het 10-K-punt -17.4987,-71.3601 ligt 0,8 km noordelijker op de smeltloodsen van hetzelfde complex, snap 0,78 km) |
| `ag-ilo-raffinaderij` | raffinaderij + edelmetaalfabriek (staart b2, stoppunt) | Ilo-raffinaderij met edelmetaalfabriek (SCC, Pacocha) | -17.5788, -71.3531 | [1][sat] | aannemelijk (z15 gezien: gebouwenreeks langs spoor en kustweg; oostelijke helft onder wolk, dus niet te verifiëren; 10-K-coördinaat 17°34.728'S 71°21.188'W; snap 0,55 km) |

## 4 · Via-punten
Geen. Het SCC-net is één enkelsporig boomnet (component 252 km): tussen kop en staart bestaat geen corridorkeuze. Een via-punt bij Toquepala was zelfs schadelijk: via de concentrator-knoop 225,7 km tegen 214,0 direct (haalbaarheidstoets). Router: 4 bochten ≥ 60° (85–141 m straal) rond Toquepala passen bij een bergspoor met keerbochten; geen omkeringen ≥ 150°.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Cuajone-concentrator | Southern Copper | erts → Cu-concentraat (+ Mo-concentraat) per spoor | 90 kt erts/dag | [2] |
| Ilo-smelter | Southern Copper | concentraat Toquepala + Cuajone → anodes 99,7% Cu + zwavelzuur | 1.376 kt concentraat/j nominaal; 2025 1.040,7 kt gesmolten (2024 1.230,9) | [1][2] |
| Ilo-raffinaderij + edelmetaalfabriek | Southern Copper | anodes → kathode 99,998% + anodeslijk → geraffineerd Ag, Au, Se | kathode 294,8 kt/j nominaal (2025 244,2); **Ag 130,5 t, Au 225,9 kg, Se 53,3 t (2025)** | [1][2] |

## 6 · Stoppunt
De brief stopt op de Ilo-raffinaderij met edelmetaalfabriek: het 10-K noemt de productie van geraffineerd zilver maar geen afnemer, geen kade, geen schip en geen overzeese bestemming van het zilver — fase D vervalt, fase E vervalt.

## 7 · Open punten
- **Het Cuajone-aandeel in het zilver is niet gebrond.** Het 10-K geeft zilver alleen per bedrijf en als Ilo-totaal; de anodeslijk komt uit Toquepala- én Cuajone-concentraat. Toquepala is de grotere voeder (zie de koper-keten); de lijn laat dus het pad van één van de twee toevoerstromen zien, geen zilverhoeveelheid per mijn.
- **Modaliteit smelter → raffinaderij niet gebrond** (10-K: "refinery as part of the same facility", 9 km uit elkaar). Spoor is aanname uit de aanwezigheid van het SCC-net; kan evengoed een intern wegtransport zijn.
- **Het 10-K-projectcentroïde van Cuajone is geen concentratorpunt** (3,1 km ernaast, midden in stortgebieden; het ontwerp meldt bovendien een kopieerfout tussen Toquepala en Cuajone); daarom is de concentrator satelliet-gelegd en niet uit het 10-K overgenomen.
- **Raffinaderij gedeeltelijk onder wolk** op de Esri-opname; ligging op coördinaat + OSM-spoor, niet op het gebouw bevestigd.
- Productie 2025 lager dan 2024 (smelter −15,5%, kathode −15,2%) terwijl het zilver +3,1% steeg [1]; oorzaak niet onderzocht.
- Sitelaag zilver kent Ilo, Cuajone en Toquepala niet; koper-sitelaag heeft `w-ilo` (-17.505, -71.359 = dit smelter-anker), `w-cuajone` (put, -17.0463, -70.7071) en `w-toquepala`. Centraal gelijktrekken.

## 8 · Bronnen
[1] Southern Copper Corp., Annual Report / Form 10-K FY2025 — Ilo-tabel: geraffineerd zilver 130,5 / 126,6 / 109,7 (000 kg, 2025/2024/2023), goud 225,9 kg, selenium 53,3 t, kathode 244,2 kt; smelter 1.040,7 kt; Ilo 17 km N van Ilo, 121 km van Toquepala, 147 km van Cuajone (wegafstanden); coördinaten smelter/raffinaderij; spoor 214 km. https://www.sec.gov/Archives/edgar/data/1001838/000110465926044985/scco-20251231xars.pdf (10-K zelf: https://www.sec.gov/Archives/edgar/data/1001838/000110465926021492/scco-20251231x10k.htm)
[2] Southern Copper Corp., Form 10-K FY2024 — Cuajone (concentrator 90.000 t/dag, projectcentroïde 17°3,130'S 70°44,499'W, spurspoor Toquepala–Cuajone), Toquepala (2 × 60.000 t/dag), Ilo (smelter, raffinaderij, anodeslijk naar de edelmetaalfabriek, industriespoor 214 km 1435 mm, 257 km incl. emplacementen, 27 km tunnels, 5,7 Mt/j). https://minedocs.com/28/Southern-Copper-Form-10-K-2024.pdf
[3] Wikipedia, "Rail transport in Peru" — SPCC-spoor Toquepala–Ilo 187 km, 1959, later aftakking grotendeels in tunnel naar Cuajone. https://en.wikipedia.org/wiki/Rail_transport_in_Peru
[4] Wikipedia, "Cuajone mine" — put -17,043/-70,711, geopend 1976, blokkade van de spoorlijn door gemeenschappen 2022. https://en.wikipedia.org/wiki/Cuajone_mine
[5] Railway Gazette, "Southern Peru" — 215 km, 1435 mm, Ilo–Toquepala–Cuajone. https://railwaygazette.com/data/southern-peru/53346.article
[6] Wikipedia, "Toquepala mine" — SPCC, Ilo-smelter geopend 1960. https://en.wikipedia.org/wiki/Toquepala_mine
[osm] OpenStreetMap (ODbL) via Nominatim — "Fundición de Cobre de Ilo - Southern Peru" -17,5049908/-71,3590378; spoornet via `v2/build-cache/raw1op1/peru.geojson` (way 788654xxx/788670xxx bij de concentrator).
[koper-brief] `v2/design/routebrieven/koper-toquepala-ilo.md` (M31 golf 8) — smelteranker `cu-ilo-smelter`, zelfde staart en spoorrouter-run.
[sat] Esri World Imagery via sat_check.py — `v2/build-cache/satcheck/sat-zilver-cuajone-ilo-cuajone-conc16.png`, `-cuajone-conc.png`, `-cuajone-put.png`, `-cuajone-railhead.png`, `-cuajone-sw.png`, `-cuajone-z14.png`, `-smelter.png`, `-raffinaderij.png` (z14–z16, 2026-10-09).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-zilver-cuajone-ilo.json` (versie 2, lonlat, 22,4 KB) · functie `bak_zilver_cuajone_ilo` in `v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh zilver-cuajone-ilo`.

| been | modaliteit | km | punten | opmerking |
|---|---|---|---|---|
| b1 Cuajone-concentrator → Ilo-smelter | spoor, doorgetrokken | 214,0 | 1081 | brief 214 (10-K): 0,0% afwijking; snaps 0,12 / 0,08 km |
| b2 Ilo-smelter → Ilo-raffinaderij en edelmetaalfabriek | spoor, doorgetrokken (aannemelijk: modaliteit niet gebrond) | 8,2 | 28 | router 8,3 in de brief, hemelsbreed 8,9 |

Totaal 222,2 km, 3 markers (concentrator, smelter, raffinaderij), 0 naden, geen stippel, geen zee, geen haven-aanloop, geen vlucht, geen last-mile-been.

**Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` b1 van -17.0640,-70.7690 naar -17.5050,-71.3590 (`--naam=zilver-cuajone-ilo-a --hoofd-km=100 --max-snap=60`, geen via-punt) en b2 van de smelter naar -17.5788,-71.3531 (`--naam=zilver-cuajone-ilo-b`); beide als `--been-geojson "spoor|…"` in `hecht_marnet.py route`.

**Toets:** km b1 tegen 214 goed. Geen naad. Markers 0,12 / 0,08 / 0,55 km van hun lijn (de raffinaderij ligt 0,55 km van het spoor, in de brief als snap genoemd). `toets_knikken.py`: 4 knikken >= 60 gr, 0 omkeringen, 0 terugloop; alle vier zijn bergspoor-haarspeldbochten (straal 72-87 m) rond -17.27,-70.66..-70.73, geen geometriefout. `toets_rechte_benen.py --min-km 5`: geen recht been. json.load: versie 2, punt_formaat lonlat, modaliteit spoor.

**Gedeeld:** vanaf -17.2632,-70.6464 tot de smelter is b1 punt-voor-punt gelijk aan `spoorroute-koper-toquepala-ilo-a.geojson` (183,2 km); geen tweede versie getekend.

**Lessen:** (1) een via-punt bij Toquepala gaf 225,7 km tegen 214,0 direct: in een boomnet zonder corridorkeuze geen via-punt. (2) 10-K-afstanden 121/147 km zijn wegkm, geen spoorkm. (3) Centraal: sleutel `ag-cu` of vrije variant controleren; sitelaag zilver kent Ilo, Cuajone en Toquepala niet.
