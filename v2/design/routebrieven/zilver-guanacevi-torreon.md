# Routebrief (licht) · Zilver · Guanaceví-molen (Durango) → Santa María del Oro / San Bernardo / Mapimí → Met-Mex Peñoles Torreón (Mexico)

**stroom-id:** `zilver-guanacevi-torreon` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) ·
**status:** gebakken
**Keten in één zin:** zilverdoré van de Guanaceví-molen (Endeavour Silver, Durango) per **truck** (aannemelijk: modaliteit en tracé niet
gebrond; hemelsbreed 255 km, geen wegkm; gemeten 380,6 km) over de staatswegen Santa María del Oro–Ciénega de Escobar, El Mirador–San
Bernardo en El Palmito–Mapimí naar de Met-Mex Peñoles-raffinaderij in Torreón — **stoppunt** (de raffinaderij is de bestemming; geen D/E).
**Welke as van het verhaal:** *een junior zilvermijn naar de grootste zilverraffinaderij* — jaarvolume **≈ 122 t Ag/j** (3.915.077 oz Ag
geproduceerd in 2025 ÷ 32.150,7 oz/t; Endeavour-productiepersbericht 8 jan 2026 [2]); mijncijfer, geen afleiding.

## 1 · Ketenkaart
```
Guanaceví-molen `ag-guanacevi-molen` ──(b1 truck · Ciénega de Escobar → Indé/San Bernardo → Mapimí → Jiménez–Torreón ·
   hemelsbreed 255 km, geen wegkm · gemeten 380,6 km · aannemelijk: modaliteit niet gebrond)──►
   Met-Mex Peñoles-raffinaderij `ag-penoles-torreon` (Torreón, Coahuila) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | Guanaceví-molen → Met-Mex Torreón (aannemelijk: één bron voor de bestemming, modaliteit niet gebrond) | Carretera Santa María del Oro–Ciénega de Escobar → Carretera El Mirador–San Bernardo (Indé) → Carretera El Palmito–Mapimí → Carretera Jiménez–Torreón [7] | hemelsbreed 255 km, geen wegkm (geen bedrijfs-/overheidsopgave; de ±15%-toets is indicatie) · gemeten 380,6 km | maak_stroombeen_weg (extract mexico, vensterKm 200) | nee — bestemming gebrond [1][9], lijn gemeten en doorgetrokken |

Alternatieve corridor (niet getekend): de officiële toegang tot Guanaceví loopt via Durango (MEX 45 → MEX 23 via Santiago Papasquiaro en
Tepehuanes, ca. 260 km [4]); Durango → Torreón komt daar nog bovenop. De gemeten corridor is de kortste weg in OSM, geen bron zegt welke route
het pantser-/doré-vervoer rijdt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-guanacevi-molen` | molen / doré-laad | Guanaceví-molen (Merrill-Crowe, 1.300 tpd) | 25.9209, -105.9539 | [5][8][10] | bron-gelegd (z16 gezien: gebouwen van de plant naast getrapte tailings-terrassen, 1,2 km ten zuiden van het dorp; het projectcentrum uit het technisch rapport 25.9131, -105.9722 [5] ligt 2,0 km WZW in bos en is geen laadplek) |
| `ag-penoles-torreon` | raffinaderij (los, stoppunt) | Met-Mex Peñoles-raffinaderij, Torreón | 25.5278, -103.4417 | [3][11] | bron-gelegd — hergebruik letterlijk uit `zilver-fresnillo-torreon` en `w-ref-penoles` (zilver-sitelaag); z15 opnieuw gezien: aaneengesloten industrieel complex met tanks en een donkere bezinkvijver op het spoor, ZW van het stadscentrum |

## 4 · Via-punten (b1 — de truckweg heeft een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Carretera Santa María del Oro–Ciénega de Escobar (bij La Cofradía) | 25.630, -105.712 | kiest de zuidoost-uitgang uit Guanaceví boven de Tepehuanes-route naar Durango; 0,02 km snap op de weg [7] |
| b1 | 2 | Carretera El Mirador–San Bernardo, entronque (Indé) | 26.098, -105.202 | kiest de noordoost-boog over Indé/San Bernardo naar de Chihuahuaanse vlakte, niet terug naar Durango; 0,01 km snap [7] |
| b1 | 3 | Carretera El Palmito–Mapimí | 25.873, -104.108 | pint de ingang van de La Laguna-vlakte vóór Mapimí; 0,06 km snap [7] |

Alle drie liggen op de doorgaande weg buiten bebouwing (geen stadscentrum); coördinaten van de haalbaarheidstoets, na een Nominatim-controle op wegnaam.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Guanaceví-molen | Endeavour Silver | erts (+ 23% lokale derden-voeding in Q4 2025) → zilverdoré (ca. 93,5% Ag) | 1.300 tpd ontwerp; 2025 gemiddeld 1.104 tpd | [2][5][9] |
| Met-Mex Peñoles-raffinaderij (Torreón) | Industrias Peñoles | doré/precipitaten → good-delivery baren | 118 Moz Ag/j ≈ 3.670 t Ag/j geïnstalleerd; 2025 productie 70.586 koz ≈ 2.195 t | [3] |

## 6 · Stoppunt
De brief stopt bij Met-Mex Peñoles: de AIF noemt alleen "delivered to the Penoles Torreon refinery" [1], de raffinaderij is de eindbestemming van
deze as en geen bron noemt een volgende locatie (geen fase D/E).

## 7 · Open punten
- **Modaliteit en tracé niet gebrond**: de AIF zegt alleen "delivered to" (en foutief "Chihuahua state", Torreón ligt in Coahuila) [1]; geen bron noemt
  pantserwagen, ander wegvervoer of vlucht. De Guanaceví-landingsbaan is 1.000 m onverhard, onderhouden noch geschikt voor vrachtvliegtuigen [4]:
  daarom geen luchtbeen. Het been is een truck-aanname, in de beennaam "aannemelijk".
- **Geen echte wegkilometer**: alleen hemelsbreed 255 km; gemeten 380,6 km (+49% t.o.v. hemelsbreed, omwegfactor 1,49 door de Sierra Madre; ±15%-toets
  hier niet toepasbaar). Het tracé is de kortste OSM-route, niet de bewezen route; via Durango is het ruwweg 260 km + Durango–Torreón.
- **Eenheid**: 122 t Ag/j volgt uit 3.915.077 oz (Guanaceví 2025) en omvat doré uit ook derden-voeding (23% in Q4); AIF-aandeel 56% van de zilveromzet [1].
- Geen wegnummers (ref) per wegdeel gevonden; alleen staatsweg-namen uit OSM [7]; `refs` blijft leeg in het profiel.
- AIF-coördinaat van het projectcentrum (bos) wijkt 2,0 km af van de molen: molen/tailings-ligging is satelliet-gelegd, niet bron-gelegd uit een document.
- Gedeeld stuk met `zilver-fresnillo-torreon` b1: alleen de laatste ca. 1,3 km voor Met-Mex; de weg is een andere aanvoer (Jiménez–Torreón), geen letterlijke kopie.

## 8 · Bronnen
[1] Endeavour Silver, Annual Information Form FY2025 (Form 40-F exhibit 99.1) — "silver doré delivered to the Penoles Torreon refinery, in Chihuahua
    state"; Guanaceví = 56% van de zilveromzet 2025. https://www.sec.gov/Archives/edgar/data/1277866/000106299326001944/exhibit99-1.htm
[2] Endeavour Silver, productiepersbericht 2025 (8 jan 2026) — Guanaceví: 402.992 t, 1.104 tpd, 3.915.077 oz Ag, 13.747 oz Au; Q4 23% lokale
    derden-voeding. https://edrsilver.com/site/assets/files/14623/2026_01_08_2025_production_nr_draft4.pdf
[3] Industrias Peñoles, Metals — Met-Mex lead-silver refinery, 118 Moz Ag/j geïnstalleerd, 2025 productie 70.586 koz, Torreón (Coahuila).
    https://www.penoles.com.mx/en/our-operations/metals.html
[4] Endeavour Silver, NI 43-101 Guanaceví (effectief 31 dec 2020, gepubliceerd jan 2022), §5 — toegang vanaf Durango via MEX 45 en MEX 23, 260 km;
    landingsbaan 1.000 m onverhard. https://www.sec.gov/Archives/edgar/data/1277866/000106299322001253/exhibit99-1.htm
[5] Endeavour AIF FY2025, Guanaceví-sectie — projectcentrum 25°54'47"N 105°58'20"W (25.9131, -105.9722), "3.6 km west of the town"; on-site mill
    Merrill-Crowe 1.300 tpd. (zelfde url als [1], offset 200.000)
[6] Wikipedia (en), Guanaceví — dorp 25.932, -105.954. https://en.wikipedia.org/wiki/Guanacev%C3%AD
[7] OpenStreetMap/Nominatim reverse op de via-punten en routepunten (Carretera Santa María del Oro–Ciénega de Escobar; El Mirador–San Bernardo;
    El Palmito–Mapimí; Jiménez–Torreón), 2026-10-31. https://nominatim.openstreetmap.org/
[8] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-zilver-guanacevi-torreon-molen-z16.png`, `…-molen.png` (z15),
    `…-penoles.png` (z15) en `sat-toets-zilver-guanacevi-project.png` (haalbaarheidstoets, bos op het projectcentrum).
[9] Endeavour Silver 6-K 2009 en 40-F 2006 (via zoeksamenvatting, niet zelf gelezen) — doré naar Met-Mex Peñoles Torreón; doré ca. 93,5% Ag.
    https://www.sec.gov/Archives/edgar/data/0001277866/000119907309000571/ex99_1.htm · https://www.sec.gov/Archives/edgar/data/0001277866/000106299306003544/exhibit99-28.htm
[10] Haalbaarheidstoets zilver-guanacevi-torreon (2026-10-31): molen 25.9209, -105.9539 (z16), via-punten, 380,6 km.
[11] `v2/design/routebrieven/zilver-fresnillo-torreon.md` §3 en `v2/design/zilver-sitelaag.json` id `w-ref-penoles` — anker Met-Mex 25.5278, -103.4417.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)

**Resultaat:** `v2/data/stroomroute-zilver-guanacevi-torreon.json` (126,7 KB, versie 2, punt_formaat lonlat) · 1 been · **381,0 km** · 5.895 punten · 5 markers · geen naden (één been).

| # | modaliteit | km | stippel | been |
|---|---|---|---|---|
| b1 | truck | 381,0 (weg 380,6 + aanloop 0,15 en 0,31 km) | nee | zilverdoré Guanaceví-molen → Ciénega de Escobar → Indé/San Bernardo → Mapimí → Met-Mex Peñoles Torreón (aannemelijk: bestemming gebrond, modaliteit en tracé niet) |

**Recept:** profiel `zilver-guanacevi-torreon-guanacevi-torreon` in `maak_stroombeen_weg.py` (extract mexico, vensterKm 200, refs leeg; via-snaps 0,15 / 0,02 / 0,01 / 0,06 / 0,31 km, allemaal OK), gescand met `wegscan_puur.py`, uitvoer `v2/build-cache/ais/graaf/zilver-guanacevi-torreon-weg-guanacevi-torreon.geojson`; functie `bak_zilver_guanacevi_torreon()` in `bak_stromen.sh` (één `--been-geojson truck`, 5 markers: 2 ankers + 3 via-punten, geen stippel). Draaien: `bash v2/tools/bak_stromen.sh zilver-guanacevi-torreon`.

**Toets:** km 381,0 tegen hemelsbreed 255 km (omwegfactor 1,49): de brief geeft geen echte wegkm, dus de ±15%-toets is hier indicatie en geen norm; alle markers 0,00-0,06 km van de lijn; `toets_knikken.py`: 25 knikken >= 60 graden (spikes van 4-35 m, vooral rond de molen en in Torreón), 0 omkeringen, 0 teruglopen; `toets_rechte_benen.py --min-km 5`: de stroom komt niet voor (omwegfactor niet 1,000).

**Geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen letterlijke kopie.** Het eindanker Met-Mex is hergebruikt uit `zilver-fresnillo-torreon`; alleen de laatste ca. 1,3 km voor Met-Mex ligt dicht bij de Fresnillo-aanvoer, maar het is een andere weg (Jiménez–Torreón), dus geen gedeeld been.

**Lessen:** (1) Een tweede run van het profiel was niet nodig; het gevalideerde geojson (5.895 punten) is rechtstreeks gebruikt. (2) De modaliteit en het tracé blijven aannemelijk: de kortste OSM-route is niet de bewezen route; de officiële toegang via Durango (MEX 45/MEX 23) is niet getekend. (3) Geen eindklasse-probleem: de kop (4,3 km kleine klasse `unclassified` bij de molen) en de staart (0,3 km) liggen ruim onder de last-mile-drempel van 2 km.
