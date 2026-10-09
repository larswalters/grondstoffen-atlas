# Routebrief (licht) · gas — Saih Rawl (PDO, Oman) → Qalhat (Oman LNG, Sur)

**stroom-id:** `gas-saihrawl-qalhat` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** Behandeld gas van de Saih Rawl-centrale verwerkingsfabriek (PDO, centraal Oman) gaat door één ondergrondse
48-inch-leiding van ca. 352 km (OSM-way 589407065, 351,7 km) dwars door de woestijn naar de Oman LNG-fabriek in Qalhat bij Sur, waar
het wordt vloeibaar gemaakt aan de Golf van Oman (buiten Hormuz). De tekening stopt bij de fabriek: een een-been-pijp.
**Welke as van het verhaal:** *Reserve-as "LNG buiten Hormuz"* — Omans LNG verlaat de kust van Qalhat aan de Golf van Oman en hoeft
de Straat van Hormuz niet te passeren, in tegenstelling tot Qatar/VAE-LNG. Volume: de leiding heeft een capaciteit van 12 bcm/j [1];
de fabriek produceerde 11,5 Mtpa LNG in 2023 (≈ 15,6 bcm/j, factor 1,36) [3]; ontwerpcapaciteit fabriek 10,4 Mtpa (≈ 14,1 bcm/j) [1].
De doorzet van deze ene leiding is niet gepubliceerd; gewicht in de gloed = leidingcapaciteit 12 bcm/j, met de fabriek (sitelaag
`w-omanlng`, 14,6) als bovengrens. Het verschil leiding 12 ↔ productie 15,6 bcm/j wijst erop dat de fabriek niet uitsluitend uit deze ene
leiding wordt gevoed (open punt, §7).

## 1 · Ketenkaart
```
Saih Rawl-gasverwerking (PDO, centraal Oman) `gas-saihrawl-plant`
  ──(b1 leiding · 48" ondergrondse gasleiding, OSM-way 589407065 · 351,7 km OSM / 352 PDO / 360 Wikipedia, doorgetrokken)──►
Oman LNG, Qalhat bij Sur `gas-qalhat-omanlng` (OSM-eind 1,3 km ZUIDELIJK van het fabrieksanker, binnen de 2 km-regel) — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-saihrawl-plant` → `gas-qalhat-omanlng` | PDO-gasleiding Saih Rawl–Qalhat, 48", OSM-way 589407065 (man_made=pipeline, substance=gas, usage=transmission, location=underground) | 352 [2], 360 [1]; gemeten OSM **351,7** (−0,1% / −2,3%) | vooraf gestikt geojson (FeatureCollection, 345 punten; grootste segment 11,9 km, geen kartering-gat) | nee |

Het way-begin (21.3722, 56.7200) ligt binnen de omheining van de Saih Rawl-fabriek (z16: oostrand, bij de pijpenbundel); het way-eind
(22.6482, 59.4069) ligt 0,6 km ten zuiden van het fabrieksterrein bij een omheind ontvangstcompound en 1,3 km van het fabrieksanker: geen eigen been
(< 2 km). Een tweede leiding vanaf hetzelfde begin, OSM-way 565166565 (395 km, naar Sohar, 24.4543, 56.6200), is **niet** deze stroom en wordt niet getekend.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-saihrawl-plant` | gasfabriek (kop) | Saih Rawl Central Processing Plant (PDO) | 21.3722, 56.7200 | [2][4] | bron-gelegd (z15+z16 gezien: omheind procescomplex met rijen processtreinen en pijpenbundels midden in het woestijn-olieveld, putlocaties en wegenspinsel eromheen; het OSM-begin ligt op de oostrand van het complex) |
| `gas-qalhat-omanlng` | LNG-fabriek (staart, stoppunt) | Oman LNG, Qalhat bij Sur | 22.6599, 59.4057 | [1][5] | bron-gelegd (z15+z16 gezien: omheind LNG-complex aan de kust met twee grote bolvormige tanks, processtreinen en een lange laadsteiger naar zee; hergebruik van sitelaag `w-omanlng`, bron-gelegd door dit z16-blik) |

Hergebruik: `gas-qalhat-omanlng` is letterlijk het sitelaag-punt `w-omanlng` (22.6599, 59.4057) uit `gas-sitelaag.json`; wiki-punt 22.6611, 59.4053 [1] ligt 0,15 km ernaast.
Het OSM-eind van de leiding (22.6482, 59.4069) is **geen** anker (alleen het lijneinde).

## 4 · Via-punten
Niet van toepassing: leiding = OSM-way, geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Saih Rawl-verwerkingsfabriek | PDO (Petroleum Development Oman, overheid) | veldgas (Barik, Saih Nihayda, Saih Rawl) → behandeld exportgas | leiding 12 bcm/j | [1][2] |
| Oman LNG, Qalhat | Oman LNG LLC (overheid 51%, Shell 30%, TotalEnergies 5,54%, KOGAS 5%, Mitsubishi/Mitsui 2,77% elk, Partex 2%, Itochu 0,92%) | gas → LNG | 10,4 Mtpa nameplate; 11,5 Mtpa productie 2023; 3 treinen | [1][3] |

## 6 · Stoppunt
De tekening stopt bij de Oman LNG-fabriek in Qalhat: de afnemer per cargo is niet te volgen (afnemers wisselen per contract en Oman LNG
verkoopt FOB aan terminals buiten onze brief), dus geen LNG-been; fase D/E vervallen. De keten is daarmee een bewuste een-been-pijp.
Verhaal in één zin: "LNG buiten Hormuz" begint hier, bij het laden aan de Golf van Oman.

## 7 · Open punten
- **Afnemer per cargo onbekend.** Het KOGAS-contract (4,1 Mtpa, 25 jaar) en Osaka Gas (0,7 Mtpa) liepen eind 2024 af; vanaf 2025 nieuwe termijncontracten
  met o.a. Shell (tot 1,6 Mtpa), JERA (0,8), Itochu (0,8), Mitsui (0,75), TotalEnergies (0,8), Unipec (1,0, 4 jaar), BOTAS (1,0) [3][6]; of die per terminal
  bevestigd zijn is niet gevonden, dus geen LNG-been.
- **Volume leiding ↔ fabriek:** 12 bcm/j [1] tegen 15,6 bcm/j LNG-productie (2023) [3]: de fabriek krijgt kennelijk ook gas via andere PDO-/netverbindingen; welke is niet gevonden.
- **Way-eind 1,3 km van het fabrieksanker** (OSM yahoo lowres-bron): de laatste kilometer binnen het terrein is niet gekarteerd; geen stippel (< 2 km).
- **Way-identificatie** berust op begin (Saih Rawl-fabriek) + eind (Qalhat) + lengte 351,7 tegen 352 [2] en 360 [1]; geen naam- of diameter-tag in OSM (alleen substance=gas, usage=transmission).
- **Geen peiljaar-cijfer voor de doorzet van de leiding;** 12 bcm/j is capaciteit, niet doorzet.

## 8 · Bronnen
[1] Wikipedia, "Oman LNG" — Qalhat bij Sur, 3 treinen 10,4 Mtpa, 360 km 48"-leiding vanaf Saih Rowl, 12 bcm/j, aandeelhouders, coördinaat 22°39′40″N 59°24′19″E. https://en.wikipedia.org/wiki/Oman_LNG
[2] Wikipedia, "Petroleum Development Oman" — Saih Rawl-verwerkingsfabriek + 352 km-leiding naar Qalhat, opgedragen november 1999. https://en.wikipedia.org/wiki/Petroleum_Development_Oman
[3] LNG Prime, "Oman LNG to boost capacity with new train", 29 juli 2024 — 11,5 Mtpa productie in 2023, 173 cargo's, termijncontracten 2025–2034, nieuwe trein 3,8 Mtpa tegen 2029. https://lngprime.com/lng-terminals/oman-lng-to-boost-capacity-with-new-train/118488
[4] OpenStreetMap (ODbL), way 589407065 (man_made=pipeline, substance=gas, usage=transmission, location=underground), 345 punten, 351,7 km; opgehaald via de OSM-API op 2026-10-09. https://www.openstreetmap.org/way/589407065
[5] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-gas-saihrawl-qalhat-saihrawl-start.png`, `-saihrawl-z16.png`, `-qalhat.png`, `-qalhat-z16.png`.
[6] Oman Observer, "Oman LNG eyes expansion of Qalhat plant capacity to 12 million tonnes per year", 8 mei 2023 — capaciteit 11,5 → 12 Mtpa, offtake-overeenkomsten (TotalEnergies, PTTEP e.a.) vanaf 2025. https://www.omanobserver.om/article/1136826/business/energy/oman-lng-eyes-expansion-of-qalhat-plant-capacity-to-12-million-tonnes-per-year
[7] Natural Gas World, "Oman LNG pens supply deals with three Japanese companies" — Itochu/JERA 0,8 en Mitsui 0,75 Mtpa vanaf 2025. https://naturalgasworld.com/oman-lng-pens-supply-deals-with-three-japanese-companies-102879
[8] OpenStreetMap (ODbL), way 565166565 (leiding Saih Rawl–Sohar, 394,8 km) — als niet-deze-stroom uitgesloten. https://www.openstreetmap.org/way/565166565
[9] Esri World Imagery-tegels (z15/z16) zelf bekeken op 2026-10-09; sitelaag `v2/design/gas-sitelaag.json` (id `w-omanlng`).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)

**Bestand:** `v2/data/stroomroute-gas-saihrawl-qalhat.json` (7,3 KB, contract versie 2, lonlat) · **functie:** `bak_gas_saihrawl_qalhat` in `v2/tools/bak_stromen.sh` · **recept:** `bash v2/tools/bak_stromen.sh gas-saihrawl-qalhat` (tussenuitvoer `python v2/tools/maak_leidingbeen_gas_saihrawl_qalhat.py` -> `v2/build-cache/ais/graaf/gas-saihrawl-qalhat-leiding-omangas.geojson`, FeatureCollection, 345 punten).

| # | modaliteit | been | km | naad | stippel |
|---|---|---|---|---|---|
| 1 | leiding | PDO-gasleiding 48 inch (OSM-way 589407065) Saih Rawl -> Qalhat, ondergronds | 351,7 | 0 | nee |

Totaal 351,7 km, 345 punten, 2 markers (`gas-saihrawl-plant` 21.3722, 56.7200 op 0,005 km van de lijn; `gas-qalhat-omanlng` 22.6599, 59.4057 op 1,31 km van het lijn-eind). Geen zee, weg, spoor, lucht, via-punten, haven-aanloop, stippel of gedeeld been.

**Toets:** 351,7 km tegen 352 [2] / 360 [1] = -0,1% / -2,3% (OSM-geometrie, geen wegkm), binnen de +/-15%. Geen naden (een been). Omwegfactor 1,130, dus geen rechte lijn (`toets_rechte_benen` toont het been alleen met `--alles`). `toets_knikken`: 2 knikken (79,9 graden bij 22.6467, 59.4056 en 62,1 graden bij 22.3595, 59.2565), 0 omkeringen, 0 terugloop; de eerste is de laatste aanloop naar het ontvangstcompound. json.load ok, versie 2, punt_formaat lonlat, modaliteit leiding, 345 punten.

**Toelichting leiding:** doorgetrokken omdat OSM de leiding heeft (man_made=pipeline, substance=gas, ondergronds); grootste segment 11,9 km, geen kartering-gat. Identificatie berust op begin (op 5 m van het fabrieksanker), eind en lengte, want de way heeft geen naam- of diameter-tag. Niet way 565166565 (Saih Rawl naar Sohar).

**Marker Qalhat (bevinding, geen fout):** het lijn-eind (22.6482, 59.4069) ligt 1,31 km van het fabrieksanker, het ontvangstcompound 0,6 km ten zuiden van het terrein. Binnen de 2 km-regel (geen last-mile-stippel), dus marker en lijn vallen niet samen: anker is niet het routeerpunt. De marker-toets (<= ~0,5 km) wijkt hier bewust af.

**Lessen:** (1) bij een een-been-leiding vallen km-toets en naden-toets samen in een regel: de gepubliceerde lengte (352) en de OSM-lengte kloppen op -0,1%. (2) Een parallelle bake-agent kan `bak_stromen.sh` bewerken terwijl bash het script nog leest: de bake gaf aan het eind een spurieuze "lling: command not found" (regel 10262, een andermans functie); het resultaat is niet beinvloed (json geschreven, 0 CRLF). (3) Lijn-eind staat vast uit OSM; de laatste 1,3 km binnen het LNG-terrein is niet gekarteerd en niet getekend.
