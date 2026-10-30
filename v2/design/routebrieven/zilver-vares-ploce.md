# Routebrief (licht) · zilver — Rupice-mijn → Vareš-fabriek → Ploče (Bosnië / Kroatië)

**stroom-id:** `zilver-vares-ploce` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Erts van de ondergrondse Rupice-mijn (Dundee Precious Metals, ex Adriatic Metals) per **truck** (~24,5 km) naar de Vareš-verwerkingsfabriek op het oude Veovaca-terrein; het Pb-Ag-concentraat gaat per **spoor** (Podlugovi, Sarajevo, Konjic, Mostar, Čapljina, ~224 km) naar Luka Ploče. **Stoppunt** Ploče: geen bron noemt de smelter per lading.
**Welke as van het verhaal:** *Balkan-concentraat naar de Adriatische kust* — jaarvolume Ag: **geen bedrijfscijfer gevonden**; indicatie ~110–130 t Ag/j uit een DPM-guidance van 3,5–4,1 Moz Ag (zoekresultaat 2026, jaar en dekking niet bevestigd [11]); harde ondergrens uit de bron: Q3 2024 63.100 t erts × 289 g/t = **18,2 t Ag in één kwartaal** (ramp-up, ertsinhoud, geen productie) [2]. Nameplate 65 kt Pb-Ag-concentraat + 90 kt Zn-concentraat uit 800 kt erts [1].

## 1 · Ketenkaart
```
Rupice-mijn `ag-rupice-mijn` ──(b1 truck · weg Rupice–Vareš · ~24,5 km (bron), router 19,8)──► Vareš-fabriek `ag-vares-fabriek`
  ──(b2 spoor · Vareš–Podlugovi · 24,5 km (Wikipedia), router 23,6, aannemelijk: één bron voor de modaliteit)──► Podlugovi-aansluiting
  ──(b3 spoor · Sarajevo, Konjic, Jablanica, Mostar, Čapljina, Metković · router 200,2)──► Luka Ploče `ag-ploce-haven` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Rupice-mijn → Vareš-fabriek | weg Rupice–Vareš (onverhard begin, dan R444-kant) | **24,5** (smallcaps, mining-technology) [2][3]; hemelsbreed 8,8; router 19,8 (−19%) | maak_stroombeen_weg (extract bosnie) | nee (anker-aanloop 0,64 km in de lijn) |
| b2 | A | spoor | Vareš-fabriek → Podlugovi | Podlugovi–Breza–Vareš | **24,5** (Wikipedia, historische lijn) [7]; router 23,6 (−3,7%) | maak_spoorbeen_raw --extract bosnie | nee |
| b3 | A | spoor | Podlugovi → Ploče | Sarajevo–Konjic–Mostar–Čapljina–Metković | geen gepubliceerd totaal; OSM-router **200,2** (hemelsbreed 121,8) | toets_spoorroute (BAKE_SUFFIX=-raw) | nee |
b2+b3 = 223,8 km tegen "circa 228" uit het ontwerp (−1,8%). Geen zeebeen: geen bron noemt een bestemming voorbij Ploče. Geen haven-aanloop nodig (geen MARNET-leg).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-rupice-mijn` | mijn (laad) | Rupice-mijn (DPM Vareš-project) | 44.1986, 18.2326 | [3][10] OSM-punt uit het ontwerp | bron-gelegd (z15 gezien: ontgonnen terrein met pads, gebouwen en een terrasvormig mijnfront in dicht bos; het kruis ligt op het pad) |
| `ag-vares-fabriek` | verwerkingsfabriek + spoorkop | Vareš-verwerkingsfabriek op het Veovaca-terrein | 44.1522, 18.3214 | [3] "brownfield site van de oude Veovaca-fabriek"; OSM-spooreinde | aannemelijk (z15 gezien: loodsen en een lange hal ~150 m NO van het kruis, naast de Veovaca-pit met water, spoor- en weginfra; geen bron noemt een coördinaat) |
| `ag-ploce-haven` | overslag (haven) | Luka Ploče, spoorbundel bij de stortgoed-/stukgoedkades | 43.0479, 17.4336 | [4][9] OSM-spoor, Nominatim | aannemelijk (z15 gezien: spoorbundel naast loodsen en kolenhopen; geen bron noemt het concentraatberth, dus onzeker als kade) |
Niet gebruikt: Luka Ploče-way 147755633 (43.0399, 17.4325) ligt op de olietanks, geen concentraatplek. Spoorstation Ploče 43.0484, 17.4340 (OSM) ligt 0,06 km van het routeeruiteinde.

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Weg noord van Rupice | 44.2132, 18.2566 | de route draait eerst noord en dan oost; pint de bedrijfs-/boswegcorridor, zonder dit punt zijn er sluipwegen |
| b1 | 2 | Weg ten zuiden van Vareš, vóór het centrum | 44.1927, 18.3197 | pint de toegang tot Vareš aan de noordwestkant, geen routering door het centrum |
| b1 | 3 | R444 noordelijk van Vareš-stad | 44.1732, 18.3239 | doorgaande weg langs de stad naar het Veovaca-terrein |
| b2 | — | geen (enkele lijn, 23,6 km, geen keuze) | | |
| b3 | — | knoop Podlugovi als aansluiting (kop 43.9718, 18.2516); geen via nodig: Sarajevo-westzijde Rajlovac 43.8499, 18.3199, Hadžići 43.8357, 18.2180, Konjic 43.6567, 17.9598, Jablanica 43.6559, 17.7659, Mostar 43.3469, 17.8144, Čapljina 43.1158, 17.7006, Metković 43.0577, 17.6528 | | alle punten liggen op de gerouteerde lijn (≤ 0,1 km); zonder via loopt de router dezelfde lijn, controle op de bake-uitvoer |
Profiel staat al in `maak_stroombeen_weg.py`: `zilver-vares-ploce-rupice-fabriek` (extracts bosnie, vensterKm 40, corridorKlassen tertiary + unclassified, trimStaart, gepubliceerdKm 24,5).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Vareš-verwerkingsfabriek | DPM Metals (Dundee Precious Metals; kocht Adriatic Metals 3 sep 2025) | erts → Pb-Ag- en Zn-concentraat | 800 kt erts/j → 65 kt Pb-Ag + 90 kt Zn-concentraat; nameplate later 1,3 Mtpa | [1][2][6] |
| Luka Ploče | Port of Ploče | concentraat per spoor → zee (smelters in België, Noorwegen, Zweden, Spanje, Italië, niet per lading) | n.v.t. | [1][4] |

## 6 · Stoppunt
Stop in Luka Ploče: de bron noemt alleen de smelterlanden (BE, NO, SE, ES, IT) en afnemers zonder lading-koppeling; geen fase D/E, geen zeebeen.

## 7 · Open punten
- **Modaliteit na de storm.** Storm okt 2024 beschadigde de lijn bij Jablanica en concentraat ging tijdelijk per truck naar Ploče [2][5]; een zoekresultaat meldt herstel "binnenkort" en commerciële productie op 10 aug 2026 [11], maar volledige spoorhervatting is niet bevestigd. Daarom de beennaam "aannemelijk: één bron".
- **Railhead 6 km.** Een bron zegt dat concentraat eerst 6 km naar een Vareš-railhead rijdt [3]; de OSM-spoorlijn eindigt bij het Veovaca-terrein zelf. Mogelijk een korte truckrit die niet is getekend.
- **Fabrieksanker** is aannemelijk, geen bedrijfscoördinaat (Veovaca-terrein, hallen naast de pit).
- **Truck-km.** Router 19,8 km tegen 24,5 km bron (−19%, buiten ±15%): de bedrijfsweg is deels privé of niet als weg gekarteerd. Niet bijgeschoven. 24,5 km is ook de lengte van de oude Podlugovi–Vareš-spoorlijn [7]; verwarring in de bronnen is niet uit te sluiten.
- **Ploče-kade onbepaald:** geen bron noemt het concentraatberth.
- **Jaarvolume Ag** niet gepubliceerd; guidance 3,5–4,1 Moz is zoekresultaat, niet zelf geopend [11].
- **Spoorkm b3:** 200,2 km is een router-indicatie (geen gepubliceerd totaal). De loodblootstellingszaak 2026 rond Vareš [6] raakt de keten niet.
- Sitelaag mist Rupice, Vareš en Ploče: centraal toevoegen (44.1986, 18.2326 · 44.1522, 18.3214 · 43.0479, 17.4336).

## 8 · Bronnen
[1] Mining Technology, "Adriatic to commission Bosnia silver" — 65 kt Pb-Ag + 90 kt Zn uit 800 kt erts, spoor via Sarajevo naar Ploče. https://www.mining-technology.com/newsletters/adriatic-to-commission-bosnia-silver
[2] Smallcaps, "Adriatic Metals more than doubles ore milled" — Q3 2024 63.100 t op 289 g/t Ag, storm okt 2024, concentraat per truck. https://smallcaps.com.au/article/adriatic-metals-more-doubles-ore-milled-vares-silver-operation
[3] Mining Technology, Vareš silver project — Veovaca-terrein, ertstransport 24,5 km, railhead 6 km, Ploče. https://www.mining-technology.com/projects/vares-silver-project-bosnia-and-herzegovina/
[4] Fox-Davies/Adriatic Metals, eerste concentraatlading naar Ploče, herbouwde spoorlijn (zoekresultaat). https://ukim.foxrobinson.com/?p=73280
[5] MoneyAM, concentraat per truck naar Ploče als tijdelijke oplossing (zoekresultaat, niet geopend). https://old.moneyam.com/action/news/showArticle?id=7344621
[6] Wikipedia, Vareš — Adriatic/DPM-overname 2025, loodblootstelling 2026. https://en.wikipedia.org/wiki/Vare%C5%A1
[7] Wikipedia, Narrow-gauge railways in Bosnia and Herzegovina — Podlugovi–Breza–Vareš 24,5 km. https://en.wikipedia.org/wiki/Narrow-gauge_railways_in_Bosnia_and_Herzegovina
[8] Wikipedia, Rail transport in Bosnia and Herzegovina (Narentabahn Metković–Čapljina–Mostar). https://en.wikipedia.org/wiki/Rail_transport_in_Bosnia_and_Herzegovina
[9] OpenStreetMap/Nominatim: Luka Ploče way 147755633 (43.0399, 17.4325), station Ploče 43.0484, 17.4340.
[10] Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-zilver-vares-ploce-rupice.png`, `-fabriek.png`, `-ploce-station.png`, `-lukaploce.png`, `-vares-station.png`.
[11] Engineering News (403 bij WebFetch) en WebSearch-samenvatting 2026-10-30: commerciële productie 10 aug 2026, guidance 3,5–4,1 Moz Ag. https://www.engineeringnews.co.za/article/vare-silver-project-bosnia-and-herzegovina-update-2026-09-04
[12] Geometrie-toetsen 2026-10-30: wegscan_puur (profiel zilver-vares-ploce-rupice-fabriek, 19,8 km), maak_spoorbeen_raw (23,6 km, 0 omkeringen), toets_spoorroute (200,2 km, 620 edges, verhouding 1,64, 0 bochten ≥60°, snaps 0,24/0,06 km).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Resultaat:** `v2/data/stroomroute-zilver-vares-ploce.json` (47,1 KB, versie 2, lonlat), **248,1 km**, 3 benen, 3 markers. Recept: `bash v2/tools/bak_stromen.sh zilver-vares-ploce` (functie `bak_zilver_vares_ploce`, profiel `zilver-vares-ploce-rupice-fabriek`).

| # | modaliteit | km | naad | tegen brief | bestand (build-cache/ais/graaf) |
|---|---|---|---|---|---|
| b1 | truck Rupice-mijn → Vareš-fabriek | 19,8 | 0 | bron 24,5: **-19%** (buiten ±15%, bevinding) | zilver-vares-ploce-weg-rupice-fabriek.geojson |
| b2 | spoor Vareš-fabriek → Podlugovi | 23,6 | 0,006 km | Wikipedia 24,5: -3,7% | zilver-vares-ploce-spoor-vares-podlugovi.geojson |
| b3 | spoor Podlugovi → Luka Ploče | 204,7 (router 200,2) | 0,032 km | geen gepubliceerd totaal; b2+b3 = 228,3 tegen "circa 228" ontwerp | spoorroute-zilver-vares-ploce-podlugovi-ploce.geojson |

**Markers:** `ag-rupice-mijn` (bron-gelegd), `ag-vares-fabriek` (aannemelijk), `ag-ploce-haven` (aannemelijk); alle drie 0,00 km van hun lijn. Naden max 0,03 km.
**Stippels, haven-aanloop, vlucht, leiding, kopie:** geen. Geen zeebeen: stoppunt Ploče, geen MARNET-leg.
**Toets:** `json.load` ok, modaliteiten {truck, spoor}, elk been ≥ 460 punten; `toets_rechte_benen` geen treffer; `toets_knikken` b2 en b3 0 knikken en 0 omkeringen; b1 25 knikken ≥ 60 gr (spikes met straal 6–25 m op de boswegcorridor/serpentines), 0 omkeringen ≥ 150 gr en 0 terugloop, dus echte haarspeldbochten, geen reparatie nodig.
**Bevindingen:**
- b1 router 19,8 km tegen 24,5 km bron (-19%): de bedrijfsweg is deels privé of niet gekarteerd (anker-aanloop 0,64 km aan de mijnkant). Niet bijgeschoven. 24,5 km is ook de lengte van de oude spoorlijn Podlugovi–Vareš [7]; de bron kan verwisseld zijn.
- b3: lijnlengte uit de punten (204,7) ligt 2% boven de router-som (200,2); beide zijn indicatie, er is geen gepubliceerde kilometer.
- Modaliteit na de storm van okt 2024 (spoor of truck) niet bevestigd: "aannemelijk: één bron" in de beennamen b2 en b3.
- Railhead 6 km van de fabriek [3] niet getekend; OSM-spoor eindigt bij het Veovaca-terrein.
**Lessen:** een via-punt-corridor met drie punten volstond voor de boswegen; geen bijschuiven nodig. Spoorbenen eindigden op dezelfde coördinaat als de ankers (naad < 0,05 km), dus geen last-mile-stippel. Sitelaag mist Rupice, Vareš en Ploče (centraal).
