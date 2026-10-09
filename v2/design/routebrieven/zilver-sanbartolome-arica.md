# Zilver · San Bartolomé → Tambo Quemado → Arica (Bolivia/Chili)

**stroom-id:** `zilver-sanbartolome-arica` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken
**Keten in één zin:** zilverdoré (geen concentraat) van de San Bartolomé-fabriek van Empresa Minera Manquiri
(Andean Precious Metals, Cerro Rico, Potosí) per **truck** over Ruta 1 → Patacamaya → Ruta 4 (Tambo Quemado) →
Chileense Ruta 11 naar de kade van Puerto de Arica — **aannemelijk: één bron** (zie §6/§7), stoppunt op de kade.
**Welke as van het verhaal:** Boliviaanse reserve-uitgang naar de Pacific, historisch de Arica–La Paz-corridor.
Volume ≈ 140 t Ag/j (4,5 Moz Ag in 2025, [5]; de bron scheidt Ag niet strikt van AgEq, gemiddeld ~5 Moz AgEq/j
sinds 2008 [1] = ~155 t); zie §7.

## 1 · Ketenkaart
```
San Bartolomé-fabriek `ag-sanbartolome-planta` ──(b1 truck · Ruta 1 → Patacamaya → Ruta 4 → Tambo Quemado →
Ruta 11 CH · ~845 km, aannemelijk: één bron)──► kade Puerto de Arica `ag-arica-kade` ── stoppunt
```
Bindende aanpassing van de haalbaarheidstoets: **truck, niet spoor** (Arica–La Paz-spoor: personenverkeer sinds
1996 stil, "trucks carry most of the cargo" [6]); geen tweede been, het ontwerp-spoorbeen Charaña→Arica vervalt.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | San Bartolomé-fabriek → kade Puerto de Arica (aannemelijk: één bron) | RN1/F1 Potosí–Oruro → RN1 Oruro–Patacamaya → RN4/F4 Patacamaya–Tambo Quemado → Ruta 11 CH → Arica | ~845: 319 + 131 [7] + 189 [8] + 192,25 [9] + ~14 Arica-aanloop (niet gepubliceerd) | maak_stroombeen_weg (extracts bolivia, chili) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-sanbartolome-planta` | mijnfabriek / laadplek (doré) | Manquiri San Bartolomé-plant, ZO-zijde Cerro Rico, W van Hwy 1 (F1), 0,42 km van RN1 | -19.6323, -65.7431 | [1][4][12] | bron-gelegd (z17 gezien: ronde leach-/verdikkingstanks, molen- en laboratoriumgebouwen en leidingen W van de N-Z-snelweg, tailingsdam ZO op z15; OSM-landuse "Empresa Minera Manquiri" omsluit het punt) |
| `ag-arica-kade` | overslag truck → (zee) | Puerto de Arica, mole met containerberth (apron tussen schuur en containerschip) | -18.4725, -70.3285 | [10][12] | bron-gelegd (z17 gezien: mole met containerschip aan de oostzijde, containerstapels en bulkhopen op de apron; welke berth het doré-/lading-gedeelte is niet aanwijsbaar) |

## 4 · Via-punten (b1 — alleen corridorkeuzes)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Patacamaya, rotonde RN4/RN1 (F4, way/102537742) | -17.2304, -67.9173 | de keuze Ruta 1 naar La Paz/Desaguadero vs **Ruta 4 naar Arica**; dwingt ook de verharde route boven de kortere RN31 Oruro–La Joya–Totora–Curahuara (La Joya–Totora in OSM "compacted") [11] |
| b1 | 2 | RN4 Tambo Quemado–Curahuara de Carangas (way/375233725) | -17.8648, -68.5781 | bevestigt dat de lijn op de F4 blijft en niet via F31 "Cruce RN4" afsnijdt |
| b1 | 3 | grens Chungará–Tambo Quemado, F4 "Frontera Chile–Tambo Quemado" (way/1482019241) | -18.2851, -69.0722 | grensovergang naar Arica vs Pisiga/Colchane naar Iquique; ≤0,1 km van de passcoördinaat uit [10] |
| b1 | 4 | Ruta 11 CH ten zuiden van Putre (way/825340814) | -18.2044, -69.5549 | Chileense Ruta 11 (de enige weg naar de kust), ~1 km buiten Putre, niet in het centrum [9][11] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| San Bartolomé-plant (eigen doré) | Empresa Minera Manquiri / Andean Precious Metals | oxide-erts (FDF-fines, derden: Tollojchi, Alta Vista, Paca) → zilverdoré (<1% goud) | 1,8 Mt/j ontwerp, 4.800 t/d [1][4] | [1][4] |

## 6 · Stoppunt
De brief stopt op de kade van Puerto de Arica: het doré wordt FOB mijn aan een internationale raffinaderij verkocht
en "naar Canada" verscheept, maar de bronnen (PFS 2023/24) noemen noch de vervoerswijze noch de haven noch de
raffinaderij [4]; Arica is alleen als aanvoerhaven van de fabriek gedocumenteerd [4], dus deze uitvoerlijn is een
spiegel daarvan (aannemelijk: één bron). Fase B (zee) en C (raffinage) vervallen: geen gedocumenteerd traject.

## 7 · Open punten
- **Het doré kan ook per vlucht gaan** (La Paz/Santa Cruz/Sucre); geen bron noemt de vervoerswijze. De lijn tekent de
  corridor Potosí–Arica waarvoor de weg bewezen bestaat ("all-weather roads naar Arica en Iquique" [4]), niet een claim
  over deze lading.
- **Arica vs Iquique:** PFS Figure 18-1 labelt "Port Facility Iquique, Chile"; tekst noemt Arica voor aanvoer en beide
  havens voor de weg [4]. Iquique (via Pisiga/Colchane) niet getekend. Welke berth/terminal in Arica: niet gevonden.
- **Spoor:** Wikipedia meldt dat het goederenvervoer op de Arica–La Paz-lijn in mei 2021 hervat is [6], de toets vond dat
  niet; spoor blijft buiten beeld (bindend), maar Charaña/Visviri is dus geen dood spoor..
- **RN31-snelweg Oruro–La Joya–Totora–Curahuara** is in OSM korter dan RN1+RN4 over Patacamaya, maar deels
  "compacted" (La Joya–Totora); verharding niet bevestigd, dus niet gekozen (via-punt 1).
- **km:** 639 (Bolivia, RN1/RN4-ruta-kilometrering Wikipedia) + 192,25 (Chili) = 831 gepubliceerd, zonder plant-aansluiting
  (~0,4 km) en Arica-stadsdeel Villa Frontera → kade (niet gepubliceerd, hemelsbreed ~5 km). Totaal ±15% rond 845.
- **Volume:** 4,5 Moz Ag komt uit een samenvatting van de Q4-2025-call [5]; eigen persbericht geeft GEq (53.854 oz AuEq).
  Productie is deels toll-erts (3e partijen); geen exportcijfer naar Arica.
- **Sitelaag mist San Bartolomé:** `zilver-sitelaag.json` heeft geen record (alleen San Cristóbal); niet gewijzigd.
- **Plant→F1:** 0,42 km tertiaire/privéweg; Arica-kade: poortlogica (TPA) mogelijk `access=private` (eindToegangPrivaat).

## 8 · Bronnen
[1] Andean Precious Metals, San Bartolomé — silver doré, 1,8 Mt/j ontwerp, ~5 Moz AgEq/j sinds 2008. https://andeanpm.com/san-bartolome/
[2] Wikipedia, "San Bartolomé mine" — Cerro Rico/Potosí, Coeur → AG-Mining → APM. https://en.wikipedia.org/wiki/San_Bartolom%C3%A9_mine
[3] Wikipedia, "Empresa Minera Manquiri" — zilver- én tinmijn, Cerro Rico, 99,96% Ag. https://en.wikipedia.org/wiki/Empresa_Minera_Manquiri
[4] SRK/Andean, PFS Technical Report San Bartolomé (2023/24): §5 (Hwy 5, Hwy 1), §18 (Hwy 1 ten zuiden van Potosí, plant W
    van Hwy 1, supplies via Arica, Arica/Iquique-wegen), §19 (doré FOB naar raffinaderij, Canada). https://wp-andeanpm-2023.s3.ca-central-1.amazonaws.com/media/2024/02/28203753/San-Bartolome-PFS-Report-FINAL.pdf
[5] Yahoo Finance, "Andean Precious Metals Q4 Earnings Call Highlights" — 4,5 Moz Ag 2025, 53.854 oz AuEq. https://finance.yahoo.com/markets/stocks/articles/andean-precious-metals-q4-earnings-151736297.html
[6] Wikipedia, "Arica–La Paz railway" — 440 km, passenger 1996 gestopt, trucks dragen de lading, vracht hervat mei 2021. https://en.wikipedia.org/wiki/Arica%E2%80%93La_Paz_railway
[7] Wikipedia (es), "Ruta 1 (Bolivia)" — km Patacamaya 193 / Oruro 324 / Potosí 643. https://es.wikipedia.org/wiki/Ruta_1_(Bolivia)
[8] Wikipedia (es), "Ruta 4 (Bolivia)" — Tambo Quemado km 0, Curahuara 93, Patacamaya 189. https://es.wikipedia.org/wiki/Ruta_4_(Bolivia)
[9] Wikipedia, "Chile Route 11" — 192,25 km Villa Frontera → Chungará–Tambo Quemado. https://en.wikipedia.org/wiki/Chile_Route_11
[10] Wikipedia, "Chungará–Tambo Quemado" — pas -18,2847/-69,0714, La Paz → Arica. https://en.wikipedia.org/wiki/Chungar%C3%A1%E2%80%93Tambo_Quemado
[11] OpenStreetMap/Overpass (ODbL, 2026-10-09) — F1, F4, F31, Ruta 11 CH; way-id's in §4. https://overpass.kumi.systems
[12] OSM/Nominatim — "Empresa Minera Manquiri" (-19,6311/-65,7418, bbox -19,6356…-19,6267/-65,7467…-65,7330); "Puerto de Arica" (-18,4738/-70,3195).
[13] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-zilver-sanbartolome-arica-planta.png`,
    `…-planta2.png` (z17), `…-arica.png`, `…-kade.png` (z17).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
Recept: `bash v2/tools/bak_stromen.sh zilver-sanbartolome-arica` (functie `bak_zilver_sanbartolome_arica`) → `v2/data/stroomroute-zilver-sanbartolome-arica.json`
(258,7 KB, versie 2, lonlat, 2 benen, 12.128 punten, 2 markers). Geometrie: profiel `zilver-sanbartolome-arica-planta-kade` in `maak_stroombeen_weg.py`.

| # | modaliteit | been | km | naad | stippel |
|---|---|---|---|---|---|
| 1 | truck | San Bartolomé → Tambo Quemado → Arica (Ruta 1 → RN4 → Ruta 11 CH; aannemelijk: één bron) | 842,8 | — | nee |
| 2 | truck | Arica havenweg → kade Puerto de Arica (last mile, geen net op deze korrel) | 0,6 | 0,000 | **ja** |

Totaal 843,4 km. Markers: San Bartolomé-fabriek (0,0 km van de lijn) en Puerto de Arica kade (0,0 km; de stippel eindigt erop).
**Lengtetoets:** 842,7 km tegen ~845 = **−0,3%** (OK). Per segment: fabriek → Patacamaya 452,2 (brief 319+131 = 450) · Patacamaya → RN4 Curahuara 112,0 ·
→ grens Chungará 76,0 (samen 188 tegen 189 [Wikipedia es Ruta 4]) · → Putre-zuid 66,4 · → Arica 136,4 (Ruta 11 CH 192,25 + Arica-aanloop). Alle via-punten snapten ≤ 0,11 km.
Naden 0,000 km; geen zee, dus geen haven-aanloop en geen MARNET-zeeknoop in deze stroom.

**Toelichting stippel (b2).** De vier OSM-`service`-ways van Puerto de Arica (10 knopen rond -18,475/-70,326) hangen niet aan het openbare wegnet; de dichtstbijzijnde
verbonden weg (way 297201779) ligt 0,64 km van het kade-anker. Met `eindToegangPrivaat` bleef "geen wegpad tussen punt 4 en 5" staan, dus het wegprofiel eindigt op die
verbonden knoop (-18,47735/-70,32514) en een rechte stippel van 0,645 km (< 2 km) sluit af op het kade-anker — "hier reikt het net niet", geen last-mile-been.

**Bevindingen / lessen**
- `pyosmium` is geblokkeerd (beleid voor toepassingsbeheer): de wegscan liep via `--bron overpass` (213.826 ways uit één bbox-query; kumi gaf 1 op ~8 pogingen 200,
  overpass-api.de reset de verbinding). De ruwe uitslag is bewaard in een scratchpad-cache zodat profielwijzigingen niet opnieuw hoefden te downloaden; de bake zelf is
  deterministisch over die set. Een tweede bake met een verse Overpass-set kan door kartering van de dag marginaal afwijken.
- `toets_knikken`: 21 knikken, 1 omkering (152° bij de Patacamaya-rotonde, 7 m, "scherpe bocht, echt": Ruta 1 naar La Paz vs RN4 naar Arica — de brief-keuze), 0 terugloop;
  de overige 20 zijn OSM-spikes van 1–41 m in stadsdoorsneden (Potosí, Oruro-uitvalswegen) en bij de Putre-zijtak.
- `toets_rechte_benen`: geen verdacht recht gemeten been van deze stroom (de stippel is bewust recht).
- Het doré-volume/vervoerswijze blijft aannemelijk met één bron; zie §7. Kade-berth niet aanwijsbaar, dus het kade-anker is het mole-niveau van Puerto de Arica.
- Sitelaag (niet gewijzigd): `zilver-sitelaag.json` mist San Bartolomé; voorstel record `w-sanbartolome`, rol "mijn (primair, eigen doré)", -19,6323/-65,7431, ~140 t Ag/j
  aannemelijk (Andean/Yahoo), coord_bron OSM-landuse Manquiri + satelliet z17.
- Latere fase B: haven-aanloop Arica → MARNET-zeeknoop 490 (-18,90000/-71,00000, 85,2 km) is dan verplicht (> 5 km); de kade-aansluiting moet dan opnieuw vanaf de mole worden bezien.
