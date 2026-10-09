# Kolen · El Descanso (Cesar) → Puerto Drummond, Ciénaga (Colombia)

**stroom-id:** `kolen-eldescanso-puertodrummond` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** thermische steenkool uit de dagbouw El Descanso (Drummond Ltd, Cesar) per Drummond-trein over de
Fenoco-concessielijn ± 210 km naar Puerto Drummond bij Ciénaga (Magdalena), waar de kolen via twee directe schiplaadsystemen op een
pier de zee op gaan — Colombia's tweede exportas na Cerrejón.
**Welke as van het verhaal:** Colombia tweede kolenexportas (Drummond). El Descanso 21,7 Mt ROM per jaar (GEM, peiljaar 2024) [1];
Puerto Drummond exporteerde 30,2 Mt in 2024 en heeft 60 Mt/j capaciteit (alle Drummond-mijnen samen, niet El Descanso alleen) [2][3].

## 1 · Ketenkaart
```
El Descanso (Drummond) `kolen-descanso-laad`
   ──(b1 spoor · mijnaansluiting, geen OSM-spoor · ~6 km stippel)──► spoorstart 9.6530,-73.5095
   ──(b2 spoor · Drummond-/Fenoco-lijn La Loma → Ciénaga · ~210,5 km)──► Puerto Drummond `kolen-puertodrummond-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-descanso-laad` → spoorstart 9.6530,-73.5095 | mijnspoor naar de hoofdlijn | hemelsbreed 5,98 km, geen wegkm | stippel last mile (geen net op deze korrel) | ja |
| b2 | A | spoor | spoorstart → `kolen-puertodrummond-kade` | Drummond-spoor La Loma → Puerto Drummond (Fenoco-concessie) | 210,5 gemeten tegen 192 publ. (+9,6%) [3][4] | toets_spoorroute `--hoofd-km=100` | nee |

Geen zeebeen: geen bron noemt kopers of bestemmingshavens per lading van deze mijn, dus de keten stopt bij de kade (§6).
De 192 km (Wikipedia en Drummond) loopt van La Loma resp. "de mijnprojecten" tot het terminal; het routerpad is langer
omdat het ook het stuk vanaf de spoorstart bij de mijn bevat. Vanaf het emplacement bij 9.552,-73.608 (route-km 18) resteren 192,6 km —
een indicatie dat het pad de gepubliceerde lijn volgt, niet bewezen dat dit La Loma is.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-descanso-laad` | mijn / laadplek | El Descanso (Drummond), Codazzi, Cesar | 9.7051, -73.5232 | [1] (GEM-coördinaat, hergebruikt uit `kolen-sitelaag.json` `w-eldescanso`) | bron-gelegd (z15 gezien: donker kolenstapelvlak met afvoerwegen en een N-Z lopend spoor direct oostelijk, aan de rand van de grote dagbouw — `sat-kolen-eldescanso-puertodrummond-descanso.png`) |
| `kolen-eldescanso-spoorstart` | spoorstart op het 1-op-1-net (routerpunt, geen overslag) | eerste net-knoop van de spoorlijn | 9.6530, -73.5095 | router-snap 5,98 km van het anker (toets_spoorroute) | bron-gelegd (z15 gezien: diagonale spoorbaan met ballastbed die bij de mijnlus aansluit — `sat-kolen-eldescanso-puertodrummond-spoorstart.png`; deels bewolkt) |
| `kolen-puertodrummond-kade` | overslag spoor → zeeschip (exportterminal) | Puerto Drummond, Ciénaga, Magdalena | 11.0565, -74.2200 | [2][3][5] | bron-gelegd (z15 gezien: treinlus om twee kolenstapelovalen, aan zee de wortel van een lange lader-trestle die ± 1,9 km NW de zee in loopt — `sat-kolen-eldescanso-puertodrummond-haven.png`) |

Terminal-anker op de wortel van de pier, niet op de pierkop (GEM geeft ~11.0725,-74.2313, midden in zee). Net-eind (11.0548,-74.2191) ligt 0,21 km van het anker. Een tweede, kleiner kolenterminal ligt ± 2,5 km zuidwestelijk (11.04,-74.24) en is niet dit terminal.

## 4 · Via-punten
Geen: één doorgaande spoorlijn zonder corridorkeuze (Drummond-/Fenoco-lijn; de router volgt hem via Fundación en Ciénaga, 0 bochten ≥ 60°).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Puerto Drummond | Drummond Ltd | kolen (trein) → bulklading (zeeschip, directe lading sinds 2014-03-31) | 60 Mt/j; 2 × 8.000 t/uur; pier voor vier capesizes [2][3] | [2][3] |

Geen bewerking: kolen worden van wagon via kipper (drie wagenkippers) naar band en scheepslader overgeslagen.

## 6 · Stoppunt
De brief stopt bij de kade van Puerto Drummond: geen bron koppelt kolen van El Descanso aan een bestemmingshaven of afnemer.

## 7 · Open punten
- **Sitelaag `w-puerto-drummond` (11.95, -74.3812) is fout**: ligt ± 0,9° noordelijk in zee (breedtefout; coordinaat uit graden/minuten verkeerd omgezet); echte terminal 11.0565, -74.2200. Sitelaag mag centraal gelijkgetrokken worden; hier niet gewijzigd.
- **Mijnspoor niet in OSM**: de router snapt 5,98 km van het mijnanker; het N-Z spoor dat op het beeld zichtbaar is wordt als stippel last mile getekend, niet als gemeten lijn.
- **Gepubliceerde km is niet mijn-specifiek**: 192 km is La Loma/mijnprojecten → haven; mijn → La Loma staat nergens als km.
- **Geen zeebeen**: kopers van Drummond-kolen (Europa, Israël, Turkije e.d.) zijn niet per lading te herleiden.
- **Productie ≠ export**: 21,7 Mt is alleen El Descanso (ROM); 30,2 Mt export is het hele terminal (ook Pribbenow/El Corozo).
- **Satellietbeeld spoorstart deels bewolkt**; de exacte aansluiting mijnlus ↔ hoofdlijn is niet scherp gezien.

## 8 · Bronnen
[1] Global Energy Monitor, "El Descanso Coal Mine" — 9.7050912,-73.5231884; Drummond Ltd 100%; 21,7 Mt in 2024. https://www.gem.wiki/El_Descanso_Coal_Mine
[2] Drummond Ltd, "Puerto Drummond" — Ciénaga, Magdalena; 60 Mt/j; 8.000 t/uur per direct-ladersysteem; directe lading sinds 2014-03-31; geopend 1995. https://www.drummondltd.com/nuestras-operaciones/el-puerto/puerto-drummond/
[3] Global Energy Monitor, "Puerto Drummond Coal Terminal" — export 30,185 Mt (2024), 25,147 Mt (2025); 192 km spoor van Pribbenow/El Descanso/El Corozo bij La Loma; ~11.0725,-74.2313. https://www.gem.wiki/Puerto_Drummond_Coal_Terminal
[4] Wikipedia, "Rail transport in Colombia" — sectie La Loma – Puerto Drummond 192 km, kolenvervoer sinds 1991; concessie FENOCO (1999). https://en.wikipedia.org/wiki/Rail_transport_in_Colombia
[5] Drummond Ltd, "Nuestros trenes" — 192 km mijnprojecten → haven, ± 5 uur, 13 treinen van 150 wagons (7.500 t), lijn in concessie bij Fenoco. https://www.drummondltd.com/nuestras-operaciones/el-ferrocarril/nuestros-trenes/
[6] Wikipedia, "Drummond Company" — Pribbenow en El Descanso bij La Loma (Cesar), Colombia's tweede thermische producent; bandtransport Santa Marta–Ciénaga. https://en.wikipedia.org/wiki/Drummond_Company
[7] Matrix Service Co., "Drummond Company Coal Shiploader" — directe lading ± 1.900 m offshore met twee scheepsladers op een nieuwe pier. https://www.matrixservicecompany.com/project/drummond-company-coal-shiploader
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-kolen-eldescanso-puertodrummond-{descanso,haven,spoorstart}.png`.
[9] Router-uitvoer `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=9.7051,-73.5232" "--naar=11.0565,-74.2200" --hoofd-km=100 --max-snap=60`: snap 5,98 km / 0,21 km, 210,5 km over 72 edges, grootcirkel 168,5 km, 0 bochten ≥ 60°.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-kolen-eldescanso-puertodrummond.json` (5,1 KB, contract versie 2) · functie `bak_kolen_eldescanso_puertodrummond` in `v2/tools/bak_stromen.sh` · geen wegprofiel, geen extract-scan.

| # | modaliteit | km | geometrie | stippel | naad |
|---|---|---|---|---|---|
| b1 | spoor | 6,0 | rechte lijn mijnanker 9.7051,-73.5232 → spoorstart 9.6530,-73.5095 | ja: last mile, mijnspoor niet in OSM | — |
| b2 | spoor | 210,8 | `spoorroute-kolen-eldescanso-puertodrummond-eldescanso-puertodrummond.geojson`, 227 punten | nee | 0,00 km |

Totaal 216,8 km · 3 markers (El Descanso 9.7051,-73.5232 · spoorstart 9.6530,-73.5095 als naadmarker · Puerto Drummond 11.0565,-74.2200; laatste ligt 0,21 km van de lijn, anker = pierwortel, net-eind 11.0548,-74.2191).

**Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=9.7051,-73.5232" "--naar=11.0565,-74.2200" "--naam=kolen-eldescanso-puertodrummond-eldescanso-puertodrummond" --hoofd-km=100 --max-snap=60`, daarna `bash v2/tools/bak_stromen.sh kolen-eldescanso-puertodrummond` (stippel vooraf, dan `--been-geojson`). Geen via-punt: één doorgaande lijn.

**Toets (§5):** b2 210,8 km tegen 192 km gepubliceerd = +9,8%, binnen ±15% maar indicatie: de 192 km is La Loma/mijnprojecten → haven, het routerpad bevat ook het stuk vanaf de spoorstart bij de mijn. Naden 0,00 km. `toets_knikken`: 0 knikken, 0 omkeringen. `toets_rechte_benen`: alleen b1 (stippel, omwegfactor 1,003, bedoeld). json.load goed, versie 2, lonlat, modaliteit alleen `spoor`, elk been ≥ 2 punten.

**Stippel b1:** het mijnspoor van El Descanso naar de hoofdlijn staat niet in OSM; de router snapt 5,98 km van het mijnanker. De stippel is hemelsbreed, geen wegkm, en geen mijn-specifieke meting.
**Geen zeebeen, geen haven-aanloop, geen vlucht, geen leiding:** geen bron koppelt kolen van deze mijn aan een bestemmingshaven; stoppunt = kade Puerto Drummond.

**Lessen:** (1) `--hoofd-km=100` en `--max-snap=60` zijn nodig voor Colombia; default 1000 faalt. (2) Sitelaag `w-puerto-drummond` (11.95,-74.3812) staat ~0,9 graad te noordelijk in zee; centraal gelijktrekken naar 11.0565,-74.2200. (3) Productie 21,7 Mt is El Descanso, export 30,2 Mt het hele terminal: de gloed- en lijndikte niet aan elkaar koppelen.
