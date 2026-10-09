# Routebrief (licht) · gas — Rio Grande (Bolivia) → Corumbá → Canoas (Bolivia–Brazilië)

**stroom-id:** `gas-riogrande-canoas` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Boliviaans pijpleidinggas verlaat het Rio Grande-station bij Santa Cruz, gaat door de GASBOL (Gas TransBoliviano, 32 inch) naar het grensstation bij Corumbá, loopt als TBG-leiding door Mato Grosso do Sul en São Paulo (splitsing Campinas/Paulínia) en via Curitiba en Florianópolis naar het afleverpunt Canoas bij Porto Alegre. Eén doorlopende OSM-leiding, geen zee, weg of spoor.
**Welke as van het verhaal:** de langste gasleiding van Zuid-Amerika, **11 bcm/j capaciteit** (Wikipedia GASBOL [1]; TBG 30 mln m3/d ≈ 11 bcm/j [9]). Actuele doorzet veel lager: **13,02 mln m3/d naar Brazilië in juli 2025** (≈ 4,8 bcm/j geannualiseerd, één maand, Correo del Sur [6]).

## 1 · Ketenkaart
```
Rio Grande-station `gas-riogrande-station` (GTB/YPFB, bij Santa Cruz) ──(b1 leiding · GASBOL Bolivië · 554,5 km)──►
grens Corumbá/Puerto Suárez (-19.1080, -57.8231; splitspunt, geen site) ──(b2 leiding · TBG stage 1 via Campo Grande · 1.260,8 km)──►
splitspunt Campinas/Paulínia (-22.7292, -47.1251; Guararema-tak 151 km blijft buiten beeld) ──(b3 leiding · TBG stage 2 via Curitiba, Florianópolis · 1.167,4 km)──►
afleverpunt Canoas `gas-canoas-station` (Rio Grande do Sul) ═══ stoppunt ═══
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-riogrande-station` → grens Corumbá | Gasoducto Bolivia-Brasil (GTB), OSM 1446052042 + 272116041 | **554,5** OSM tegen 557 gepubliceerd [2][3] (−0,4%) | OSM-leiding, voorgebakken geojson | nee |
| b2 | B | leiding | grens Corumbá → Campinas/Paulínia | Bolivia-Brazil Gas Pipeline (TBG stage 1), 18 OSM-ways | **1.260,8** OSM tegen ~1.267 [1][2] (stage 1 = 1.418 incl. 151 km Guararema-tak; −0,5%) | idem | nee |
| b3 | B | leiding | Campinas/Paulínia → `gas-canoas-station` | TBG stage 2, 40 OSM-ways (269260061 … 390992750) | **1.167,4** OSM tegen 1.165 [1] (+0,2%) | idem | nee |

Totaal 2.982,8 km doorgetrokken tegen 2.989 gepubliceerd (557 + 1.418 − 151 + 1.165). Geen stippel, geen gat: 60 OSM-ways sluiten op 1 m. Fase A (Boliviaanse velden/GASYRG) en D/E vervallen: geen bron noemt één fabriek of centrale als afnemer van deze stroom (het gas gaat naar distributiebedrijven, centrales en industrie langs de lijn [2]).

## 3 · Ankers
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-riogrande-station` | begin leiding (Rio Grande Measurement Station) | Rio Grande-station, GTB, Santa Cruz | -18.1928, -62.9012 | [3][8] | bron-gelegd (z16 gezien: omheind stationsterrein met rijen kleine gebouwen en leidingwerk op het OSM-lijnbegin; groter procescomplex ~0,6 km westelijker) |
| `gas-canoas-station` | afleverpunt, stoppunt (einde TBG-leiding) | Canoas-afleverstation, TBG, Rio Grande do Sul | -29.8763, -51.1473 | [8] | bron-gelegd (z16 gezien: klein omheind terrein met installaties tussen industrie en woonwijk, einde van OSM-way 390992750; ligt 1,4 km oost van de REFAP-tanks, niet op het raffinaderijterrein) |

Grens Corumbá (-19.1080, -57.8231) en Campinas (-22.7292, -47.1251) zijn OSM-lijnknopen waar de benen splitsen, geen sites en geen markers. Grenspunt z15: kleine open plek met één gebouw in bos op de lijn, het station is niet apart herkenbaar.

## 4 · Via-punten
Niet van toepassing: leidingbenen volgen OSM-geometrie, er is geen corridorkeuze door ons.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Rio Grande Measurement Station | GTB / YPFB | veldgas (o.a. via GASYRG Yacuiba–Río Grande) → export | niet gevonden | [3][7] |
| Mutún/Corumbá-overdracht | GTB → TBG | custody-overdracht grens | niet gevonden | [3] |
| Campinas/Paulínia | TBG | stage 1 → tak Guararema (151 km, niet getekend) + stage 2 | — | [1][2] |
| TBG-leiding (totaal) | TBG | Corumbá → Canoas, 2.593 km Brazilië | 30 mln m3/d (+5,2 entry) | [2][9] |

## 6 · Stoppunt
Canoas (Rio Grande do Sul), het zuidelijke leidingeinde van TBG: dit is de gevraagde eindpunt van de leiding. Daarna verdeelt het gas zich anoniem over regionale distributie en industrie; geen bron volgt één stroom naar een fabriek.

## 7 · Open punten
- **Actueel volume ontbreekt als jaarcijfer.** 13,02 mln m3/d (juli 2025, één maand) is het enige 2025-getal [6]; het contract is vaak gewijzigd (max 30 → 20 mln m3/d sinds 6-3-2020 [2], addendum dec 2023 [7]). Gloedgewicht = capaciteit 11 bcm/j tot een gemeten jaarvolume bestaat.
- **Ontwerpclaim "verlenging einde 2025" niet bevestigd:** het Energy Intelligence-artikel is van 29-12-2019 (tijdelijke verlenging vóór 31-12-2019) [4]. Petrobras 20-F 2025 noemt uitloop naar mei 2028 of aug 2029 via take-or-pay (alleen via zoekresultaat) [7].
- **Begin ligt bij het Rio Grande-station, niet bij de velden.** GASYRG (Yacuiba–Río Grande, 432 km, OSM-way 188651805) voedt het station; OSM mist het deel daartussen, dus niet getekend.
- **Argentijns gas in transit:** sinds april 2025 loopt ca. 4,5 mln m3/d Argentijns gas door Bolivië naar Brazilië [6]; de leiding draagt dus niet uitsluitend Boliviaans gas.
- **Canoas-eind ≠ REFAP:** het ontwerp noemde het anker "bij REFAP"; de leiding eindigt 1,4 km oostelijk (REFAP-centroïde -29.8725, -51.1610 [10]). Eindpunt is het OSM-lijneinde, niet het raffinaderijterrein.
- Uitgesloten (niet in de keten): Cuiabá-lateraal (OSM 206276689, 250295341), Guararema-tak (219839781). Compressorstations niet gelegd (positie niet gevonden).
- Tooling: pyosmium geblokkeerd, geen Overpass; geometrie via pure-python PBF-scan op `bolivia` en `brazilie` (`v2/build-cache/ais/graaf/gas-riogrande-canoas-stitch.py`).

## 8 · Bronnen
[1] Wikipedia, "GASBOL": 3.150 km, stage 1 1.418 km tot Guararema, stage 2 1.165 km Campinas–Canoas, max 11 bcm/j. https://en.wikipedia.org/wiki/GASBOL
[2] Wikipedia (PT), "Gasoduto Bolívia-Brasil": 557 km Bolivië (GTB) + 2.593 km Brazilië (TBG), Trecho Norte/Sul, akkoord 6-3-2020 (max 20 mln m3/d). https://pt.wikipedia.org/wiki/Gasoduto_Bol%C3%ADvia-Brasil
[3] Gas TransBoliviano (GTB): 557 km, begin Río Grande Measurement Station, eind Mutún Measurement Station aan de grens. https://www.gastransboliviano.com.bo/
[4] Energy Intelligence, "Bolivia, Brazil Reach Temporary Gas Deal", 29-12-2019. https://www.energyintel.com/0000017b-a7d9-de4c-a17b-e7db8e4e0000
[5] Eixos, "Bolívia quer diversificar clientes de gás natural no Brasil", 13-12-2022 (addendum 2022, deadline 2024 → 2025). https://eixos.com.br/bolivia-quer-diversificar-clientes-de-gas-natural-no-brasil/
[6] Correo del Sur, 19-8-2025: juli 2025 export Brazilië 13,02 MMmcd; Argentijns transitgas 4,5 mln m3/d (alleen via zoekresultaat gelezen). https://correodelsur.com/economia/20250819/produccion-de-gas-natural-alcanza-su-segundo-pico-maximo-del-ano.html
[7] Petrobras Form 20-F FY2025 (addendum 11 en 12, uitloop contract; alleen via zoekresultaat). https://www.sec.gov/Archives/edgar/data/1119639/000129281426002168/pbrform20f_2025.htm
[8] OpenStreetMap-bijdragers (ODbL), Geofabrik `bolivia` en `brazilie`, eigen PBF-scan man_made=pipeline; Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-gas-riogrande-canoas-{riogrande-start-z16,canoas-eind-z16,grens-corumba}.png`.
[9] Eixos, TBG-capaciteit 30 mln m3/d + 5,2 entry (alleen via zoekresultaat). https://eixos.com.br/gas-natural/como-a-tbg-pretende-aumentar-a-capacidade-do-gasbol-ate-2024/
[10] Wikipedia (PT), "Refinaria Alberto Pasqualini": coördinaat REFAP. https://pt.wikipedia.org/wiki/Refinaria_Alberto_Pasqualini

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh gas-riogrande-canoas` (functie `bak_gas_riogrande_canoas`, LF). Drie `--been-geojson "leiding|…"` in volgorde b1, b2, b3 naar de voorgebakken FeatureCollections `v2/build-cache/ais/graaf/gas-riogrande-canoas-leiding-{riogrande-corumba,corumba-campinas,campinas-canoas}.geojson` (gemaakt door `gas-riogrande-canoas-stitch.py` uit de PBF-scans van Geofabrik `bolivia` en `brazilie`, pure-Python, 60 OSM-ways). Twee `--marker` (de ankers uit §3), geen marker op Corumbá of Campinas. Geen extracts, weg, spoor, zee, haven-aanloop, stippel, kopie of vlucht. Uitvoer: `v2/data/stroomroute-gas-riogrande-canoas.json`, 149,6 KB, versie 2, punt_formaat lonlat.

| been | modaliteit | km gebakken | km brief | afwijking | punten | naad naar vorige |
|---|---|---|---|---|---|---|
| b1 Rio Grande-station → grens Corumbá | leiding | 554,5 | 554,5 OSM (557 gepubliceerd) | 0,0% (−0,4% tegen gepubliceerd) | 323 | — |
| b2 grens Corumbá → Campinas/Paulínia | leiding | 1.260,8 | 1.260,8 OSM (~1.267) | 0,0% (−0,5%) | 1.459 | 0,0 km |
| b3 Campinas/Paulínia → Canoas | leiding | 1.167,4 | 1.167,4 OSM (1.165) | 0,0% (+0,2%) | 5.207 | 0,0 km |

Totaal 2.982,7 km (2.982,8 in de brief, afronding), 6.989 punten, 3 benen, geen stippel. De ±15%-toets is hier vanzelf gehaald: de bake kopieert de OSM-geometrie, de vergelijking met de gepubliceerde lengte (557 + 1.418 − 151 + 1.165 = 2.989 km) is de echte toets en geeft −0,2%.

**Toets (handleiding §5):** naden alle 0,0 km (max 0,0 km). Markers: Rio Grande-station 0,006 km en Canoas 0,004 km van de lijn. `toets_knikken.py`: 77 knikken ≥ 60° op 2.982 km, 0 omkeringen, 0 terugloop. De knikken zijn spikes van 40–280 m straal in de OSM-leidinggeometrie (Serra do Mar bij Curitiba, het lijnbegin in het stationsterrein en de knoop bij Corumbá), geen keerpunt. `toets_rechte_benen.py --min-km 5 --alles`: geen van de drie benen heeft omwegfactor 1,000 (1,018 · 1,067 · 1,312). json.load slaagt, modaliteit alleen `leiding`, elk been ≥ 323 punten.

**Toelichting:**
- **Leiding, geen stippel:** OSM heeft de hele GASBOL als `man_made=pipeline`, 60 ways die op 1 m sluiten. Een gemeten been is doorgetrokken; er is geen gat, dus geen stippel en geen offshore- of ontbrekend stuk.
- **Splitspunten:** Corumbá en Campinas zijn lijnknopen op de OSM-geometrie, geen sites. Bij Campinas verlaat de Guararema-tak (151 km) de hoofdlijn; die is bewust niet getekend.
- **Lange segmenten:** de leiding is in OSM op sommige stukken grof gekarteerd, het langste segment is 44,8 km (b2) en 35,5 km (b1). Dat is bronresolutie, geen router die een rechte lijn trekt; de lengte klopt met de gepubliceerde.
- **Stoppunt Canoas:** het OSM-lijneinde ligt 1,4 km oost van REFAP, niet op het raffinaderijterrein (brief §7).
- **Registerregel (centraal, niet door de bak-agent gewijzigd):** sleutel `gas-rg` (xy = Rio Grande, Canoas; niet in de bezette lijst `gas-sr … gas-gt`; `gas-rc` blijft bezet), bestand `stroomroute-gas-riogrande-canoas.json`, grondstof `gas`, label `Rio Grande → Canoas (Bolivia → Brazilië)`, aan `true`.

**Lessen:** (1) een voorgebakken FeatureCollection per been is het goedkoopste recept voor een doorlopende OSM-leiding: de hecht_marnet-route kostte 17 s en hoeft niets te routeren. (2) Het stroom-id noemt Canoas en de lijn eindigt daar; er is geen afwijking tussen id en eindpunt. (3) De 77 knikken moeten niet als fout gelezen worden: toets_knikken is geijkt op spoor, en een pijpleiding in heuvelland heeft echte scherpe hoeken en kleine verspringingen op OSM-way-naden.
