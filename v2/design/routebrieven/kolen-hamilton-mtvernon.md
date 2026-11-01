# Kolen · Hamilton Mine No. 1 (Illinois) → Mt. Vernon Transfer Terminal (Indiana, VS)

**stroom-id:** `kolen-hamilton-mtvernon` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** thermische kolen uit de ondergrondse Hamilton Mine No. 1 (Hamilton County Coal, Alliance Resource Partners, Dahlgren, Illinois) per Evansville Western Railway (EVWR)
via McLeansboro, Enfield en Carmi naar de Mt. Vernon Transfer Terminal aan de Ohio in Mt. Vernon, Indiana, waar de kool op barges gaat. Eén spoorbeen van ca. 84 km, geen
binnenvaartbeen (geen bron noemt de barge-bestemming), geen zee, geen weg, geen fase D/E.
**Welke as van het verhaal:** Illinois-bekken naar de Ohio: mijn aan het EVWR-net, rail-barge-overslag. Hamilton 5,87 Mt ROM in 2025 (GEM [1]), ARLP noemt 6,5 Mst [2]; terminal 8 Mst/j capaciteit en
in 2025 ca. 1,6 Mst geladen voor Gibson County Coal en Hamilton samen (ARLP [2], EVWR [3]). **Eenheid: Mt kolen per jaar.** Aandeel van Hamilton in de terminal niet apart gepubliceerd. Aannemelijk: één bron voor de koppeling.

## 1 · Ketenkaart
```
Hamilton Mine No. 1 (Dahlgren, IL) `kolen-hamilton-laad`
   ──(b1 spoor · EVWR via McLeansboro, Enfield, Carmi · ~84 km)──► Mt. Vernon Transfer Terminal (IN) `kolen-mtvernon-kade` ── stoppunt (barge, bestemming onbekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-hamilton-laad` → `kolen-mtvernon-kade` | EVWR (ex-L&N St. Louis Subdivision) via McLeansboro, Enfield, Carmi; route-uitkomst | hemelsbreed 70 km, geen gepubliceerde spoorkm; proef 83,6 | toets_spoorroute (BAKE_SUFFIX=-raw) | nee (snap 0,81 en 0,18 km) |

Geen gepubliceerde spoorlengte: de ±15%-toets geldt als indicatie, niet als norm (verhouding spoor/hemelsbreed 1,19). De beennaam draagt "(aannemelijk: één bron)". Het router-pad raakt McLeansboro 0,3 km,
Enfield 0,4, Carmi 0,6 en Mt. Vernon IN 0,7 km; 0 bochten >= 60 graden; vrije route zonder via-punten, het enige alternatief (Howell Yard Evansville) is geen eindpunt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-hamilton-laad` | mijn / laadstation | Hamilton Mine No. 1 (Hamilton County Coal), Dahlgren, Hamilton County | 38.1702, -88.6014 | [1][3] | bron-gelegd (z15 gezien: mijnkantoor en bedrijfsgebouwen, slibbekken direct zuid, bereidingsinstallatie met kolenstapel en transportband ~2 km westelijker, spoorlus ZW; router snapt op 0,81 km) |
| `kolen-mtvernon-kade` | overslag spoor → barge | Mt. Vernon Transfer Terminal (Alliance), 3300 Bluff Road, Ohio, Mt. Vernon IN | 37.9245, -87.8627 | [2][3][5] | bron-gelegd (z15 gezien: zwart kolenpark in een omsloten spoorlus, transportband naar een bargedok aan de Ohio; router snapt op 0,18 km) |

Het OSM-straatpunt van Bluff Road (37.9275, -87.8753) ligt bij het Southwind Maritime Center en een sojafabriek, 1,2 km westelijker, en is geen anker.

## 4 · Via-punten (alleen spoorbenen met een corridorkeuze)
Geen: één vrije run zonder via-punten levert 83,6 km met 0 bochten; er bestaat geen corridorkeuze (geen concurrerende tak naar de terminal) die een pin vraagt.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Hamilton Mine No. 1 | Hamilton County Coal LLC, ARLP | steenkool → gewassen thermische kolen | 5,87 Mt ROM in 2025 (4,7 tot 6,3 Mt 2017-2024) | [1][2] |
| Mt. Vernon Transfer Terminal | Alliance Resource Partners (huurt het terrein) | trein (105-wagon unit trains) → grondopslag of barge | 8 Mst/j; ca. 1,6 Mst geladen 2025 (alle klanten) | [2][3][4] |

## 6 · Stoppunt
De brief stopt bij de bargekade van de terminal: geen bron noemt voor deze kolen een barge-bestemming of afnemer, dus geen binnenvaartbeen en geen fase D/E.

## 7 · Open punten
- **Koppeling mijn-terminal:** één bron (ARLP [2]: terminal laadde voor klanten van Gibson County Coal en Hamilton, 1,6 Mst in 2025); EVWR [3] noemt de mijn en de terminal los en legt geen verband. Hamilton-aandeel niet gepubliceerd.
- **Barge-bestemming:** onbekend (Ohio stroomop of -af), dus geen binnenvaartbeen.
- **Spoorkm:** geen gepubliceerde lengte; proef 83,6 km, hemelsbreed 70 km.
- **Mijnaansluiting:** snap 0,81 km; het laadspoor (bereidingsinstallatie en spoorlus) ligt aan de westzijde; bron voor de exacte laadlus niet gevonden.
- **Hamilton ROM 5,87 Mt (GEM) tegen 6,5 Mst (ARLP):** verschil is eenheid (short ton), GEM-bronpagina noemt tegelijk 2010 en 2014 als openingsjaar.
- **Route langs Evansville:** de EVWR-hoofdlijn loopt verder naar Howell Yard (CSX); niet getekend, de terminal ligt vóór die yard.
- **Sitelaag en v1:** Hamilton ontbreekt in `kolen-sitelaag.json`, `data/coal.js` en `design/kolen.md` hebben geen Illinois-stroom; centrale beslissing.

## 8 · Bronnen
[1] Global Energy Monitor, Hamilton Mine No. 1: Hamilton County Coal LLC, 38.1702261/-88.6013872, ROM 2025 5,87 Mt; 2017 6,1; 2023 5,6; 2024 4,8. https://www.gem.wiki/Hamilton_Mine_No._1
[2] Alliance Resource Partners, Coal Operations: Hamilton 6,5 Mst 2025; Mt. Vernon Transfer Terminal 8 Mst capaciteit, ca. 1,6 Mst geladen voor Gibson County Coal en Hamilton, bediend per EVWR en truck. https://www.arlp.com/our-businesses/coal-operations/
[3] Evansville Western Railway, Coal Facilities: Mt. Vernon Transfer Terminal, 3300 Bluff Road, 105-wagon unit trains, 8 Mt/j; Hamilton Mine #1 rail-bediend door EVWR. https://evwr.com/coal-facilities/
[4] Wikipedia, Evansville Western Railway: 124,5 mijl ex-L&N lijn Howell Yard Evansville tot Okawville, Savatran-aftakking bij Delafield (McLeansboro), interchange CSX, BNSF, UP, NS. https://en.wikipedia.org/wiki/Evansville_Western_Railway
[5] Ports of Indiana, Mt. Vernon 1 (terminallijst, via zoeksamenvatting, niet geopend). https://www.portsofindiana.com/wp-content/uploads/Mt.-Vernon-1.pdf
[6] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-kolen-hamilton-mtvernon-mijn.png` (z15), `…-terminal.png` (z15).
[7] Eigen routerrun `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=38.1702,-88.6014" "--naar=37.9245,-87.8627" --naam=kolen-hamilton-mtvernon-mijn-terminal --hoofd-km=100 --max-snap=60` (3.260.717 spoor-edges): 83,6 km, 56 edges, snap 0,81 en 0,18 km, 0 bochten >= 60 graden, 180 punten.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Recept:** `bash v2/tools/bak_stromen.sh kolen-hamilton-mtvernon` (functie `bak_kolen_hamilton_mtvernon`) schrijft `v2/data/stroomroute-kolen-hamilton-mtvernon.json` (4,1 KB, contract versie 2, lonlat).
Het been is vooraf gerund met `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=38.1702,-88.6014" "--naar=37.9245,-87.8627" --naam=kolen-hamilton-mtvernon-mijn-terminal --hoofd-km=100 --max-snap=60` (niet opnieuw gerund).

| # | modaliteit | km | punten | stippel | naam |
|---|---|---|---|---|---|
| 1 | spoor | 83,7 | 180 | nee | trein Hamilton Mine No. 1 → Mt. Vernon Transfer Terminal (EVWR via McLeansboro, Enfield, Carmi; aannemelijk: één bron) |

Totaal 83,7 km, 2 markers (`kolen-hamilton-laad`, `kolen-mtvernon-kade`).

**Toets (handleiding §5):** geen gepubliceerde spoorkm, dus indicatie: 83,7 km tegen hemelsbreed 70 (verhouding 1,19) en proef 83,6. Eén been, dus geen naad. Marker kolen-mtvernon-kade ligt 0,17 km van de lijn;
marker kolen-hamilton-laad ligt 0,65 km van de lijn (iets boven de 0,5 km-norm: het anker is het mijnterrein, de router snapt op het dichtstbijzijnde spoor, 0,81 km; geen last-mile-stippel omdat < 2 km).
`toets_knikken.py`: 0 knikken, 0 omkeringen. `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom. JSON: versie 2, lonlat, modaliteit spoor, 180 punten.
Geen stippel, haven-aanloop, vlucht, leiding of kopie in deze stroom.

**Lessen:** (1) de gebakken lijn is 0,1 km langer dan de proef (83,7 tegen 83,6): afronding van de gestikte geometrie; (2) de lijn begint op 38.1685,-88.6104, ca. 0,65 km van het mijnanker, de westzijde waar het laadspoor ligt;
(3) Hamilton ontbreekt in kolen-sitelaag.json: centrale beslissing; (4) registerregel centraal: sleutel kolen-hm, bestand stroomroute-kolen-hamilton-mtvernon.json.
