# Routebrief (licht) · gas — Kıyıköy (TurkStream-terminal) → Strandzha 2 → Provadia → Zaječar → Horgoš → Kiskundorozsma (Hongarije)

**stroom-id:** `gas-kiyikoy-kiskundorozsma` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** Russisch pijpgas dat via TurkStream bij de BOTAŞ-terminal Kıyıköy aan land komt, over het Turkse net (Kara Kısmı-2) naar de Bulgaarse grens bij Strandzha 2/Malkoçlar gaat, door Bulgarije (Bulgartransgaz, via Provadia en Rasovo) en Servië (Gastrans) loopt en bij de FGSZ-aansluiting Kiskundorozsma in Hongarije het Hongaarse net binnenkomt — de **Balkan Stream**, na de Oekraïne-transitstop (1-1-2025) de enige directe pijpgasroute van Rusland naar de EU.
**Welke as van het verhaal:** *Russisch pijpgas naar de EU na Oekraïne.* **18,1 bcm/j** naar Europa in 2025 (Interfax [4], ENTSOG volgens TASS [5]; S&P telt 16,8 bcm [6]); jan–sep 2026 13,2 bcm (+1,4%, ~79% van de capaciteit) [5]. Ontwerpcapaciteit Europese lijn 15,75 bcm/j [1]. Wat Kiskundorozsma binnenkomt is een deel daarvan: Servië→Hongarije mag tot 8,5 bcm/j [8], Hongarije ontving ≈7 bcm in 2025 (indicatie, zie §7).

## 1 · Ketenkaart
```
TurkStream-ontvangstterminal `gas-kiyikoy-ontvangstterminal` (BOTAŞ, Kıyıköy/Vize, Kırklareli)
  ──(b1 leiding · Kara Kısmı-2 · 141,4 km OSM)──► grens TR/BG bij Strandzha 2 (42,0604; 27,0285; geen site, geen marker)
  ──(b2 leiding · Bulgartransgaz via Provadia en Rasovo · 646,3 km OSM; Provadia→grens 474,3 tegen 474 gepubliceerd)──► grens BG/RS bij Zaječar (43,8405; 22,3748)
  ──(b3 leiding · Gastrans · 400,1 km OSM)──► grens RS/HU bij Horgoš (46,1744; 20,0115)
  ──(b4 leiding · MOL/FGSZ DN1200 · 14,9 km OSM, 15 gepubliceerd)──► `gas-kiskundorozsma-station` (FGSZ, Hongarije) ═══ stoppunt ═══
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | leiding | `gas-kiyikoy-ontvangstterminal` → Strandzha 2 | TurkStream Kara Kısmı-2 (BOTAŞ), OSM way 753501458 | **141,4** OSM; gepubliceerde lengte niet gevonden | OSM-way, letterlijk | nee |
| b2 | C | leiding | Strandzha 2 → grens BG/RS | Bulgartransgaz: Strandzha 2 → Provadia (172,2 km OSM, **geen gepubliceerde lengte**) en Provadia → grens (474,3 OSM tegen **474** [1][3], +0,1%) | **646,3** OSM | 10 OSM-ways, letterlijk gestikt (§4) | nee |
| b3 | C | leiding | grens BG/RS → grens RS/HU | Gastrans (Srbijagas), OSM way 753600807 | **400,1** OSM; ~403 volgens het ontwerp, **niet geverifieerd** | OSM-way, letterlijk | nee |
| b4 | C | leiding | grens RS/HU → `gas-kiskundorozsma-station` | FGSZ/MOL DN1200, OSM way 654525019 | **14,9** OSM tegen **15** [1][8] (−0,7%) | OSM-way, letterlijk (omgekeerd) | nee |

Totaal **1.202,7 km** OSM, volledig doorgetrokken. Provadia→Kiskundorozsma 889,3 km tegen **880** voor het Balkan Stream-traject [2] (+1,1%). Het ontwerp telde 1.030 km "gepubliceerd" = som zonder Strandzha–Provadia; die som is niet de maat voor b2. Geen stippel: er ontbreekt geen stuk OSM.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-kiyikoy-ontvangstterminal` | ontvangstterminal (laadplek) | Türk Akımı Doğalgaz Alım Terminali (BOTAŞ), Kıyıköy/Vize | 41.6500, 28.0752 | [12] letterlijk uit `gas-anapa-kiyikoy`; OSM-way 753501458 begint 0,2 km ervandaan | bron-gelegd (z15 gezien in de brief gas-anapa-kiyikoy: groot omheind industrieterrein in bos net landinwaarts van de kust) |
| `gas-kiskundorozsma-station` | meetstation/entry (stoppunt) | FGSZ Kiskundorozsma, Hongarije | 46.2962, 20.0352 | [8][10][11] | bron-gelegd (z15 gezien: klein omheind terrein met leidingarmatuur precies op het kruis, in akkerland; groter omheind compound 250 m ZW; way 654525019 begint op dit punt en de FGSZ-lijnen 679567605, 753664200 en BRUA 220422601 vertrekken hier) |

De grens bij Strandzha 2 en de twee overige grenspunten zijn OSM-lijnknopen, geen sites en geen markers. Satellietbeeld op Strandzha 2 (z15, `sat-gas-kiyikoy-kiskundorozsma-strandzha2.png`): ontboste leidingstrook door heuvelland, geen zichtbare installatie op het grenspunt; de omheinde installatie ligt 1,3 km ZO (zie §7).

## 4 · Via-punten
Niet van toepassing: leidingbenen zonder corridorkeuze door ons. De ontwerp-toets eiste via-punten Provadia en Rasovo bij een router; hier zijn de ways **letterlijk** gestikt (geen router, dus geen omweg via Negru Vodă). Stikvolgorde b2 (script `v2/build-cache/ais/graaf/gas-kiyikoy-kiskundorozsma-stitch.py`): 282209866 (omgekeerd, 8,6 km) · 580622006 (omgekeerd, 63,3) · 580622007 (67,8) · 265086899 (0,1) · 754069435 (13,1) · 945610766 (13,9) · 945610765 (0,1) · 754069438 tot vertex 7 (4,8) · 754566651 (272,6) · 859279906 (201,7). Naden: 0,04 km bij Strandzha 2; **0,45 km langs de lijn bij Provadia** (0,02 km loodrecht; knik 93° = de lijn buigt bij het compressorstation naar het westen); verder 0,00. Niet gebruikt: dubbel gemapte 116034497 (BG) en 1098864819 (RS), en 753522859 (tweede lijn).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kıyıköy-terminal | BOTAŞ | offshore TurkStream → Turks net + Malkoçlar | 2 × 15,75 bcm/j | [1] |
| Strandzha 2 (grens TR/BG) | BOTAŞ → Bulgartransgaz | overdracht, reverse mode tot Provadia | ~16 bcm/j [2]; 20 bcm/j [3] | [1][2][3] |
| KS Provadia, KS Rasovo | Bulgartransgaz | compressie op b2 | niet gevonden | [1] |
| Grens BG/RS bij Zaječar → RS/HU bij Horgoš | Srbijagas | doorvoer | 13,88 bcm/j naar Servië [2] | [2] |
| Kiskundorozsma | FGSZ | meetstation + Hongaars net, ook start van de BRUA-lijn naar Roemenië | tot 8,5 bcm/j [8] | [8][10] |

## 6 · Stoppunt
De brief stopt bij het FGSZ-station Kiskundorozsma, het instroompunt van Balkan Stream in het Hongaarse net; daarachter gaat het gas anoniem het Hongaarse en Roemeense (BRUA) net in en volgt geen bron één afnemer. Fase D/E vervallen.

## 7 · Open punten
- **Km-bron b1 en Strandzha–Provadia ontbreekt**: geen gepubliceerde lengte; 141,4 resp. 172,2 km zijn alleen OSM. b2 totaal 646,3 tegen de 474 van [1] geldt alleen voor Provadia→grens; GEM [3] noemt 474 km voor de héle Bulgaarse sectie, wat niet klopt met de ligging van Provadia (indicatie, geen norm).
- **b3 ~403 km niet geverifieerd**: het enige gepubliceerde totaal is 880 km voor Balkan Stream [2].
- **Volumes**: ENTSOG/TASS-bron geopend via zoekresultaat (de TASS-pagina's gaven ECONNRESET); alleen Interfax [4] is gelezen. De 18,1 bcm is de héle Europese lijn; het aandeel naar Servië/Hongarije is niet gevonden. Hongarije ≈7 bcm in 2025 komt uit een zoekresultaat, bron niet geopend.
- **Malkoçlar-station niet gemarkeerd**: een omheinde installatie staat op z15 op ca. 42.0535, 27.040 (BOTAŞ-way 580622005 eindigt op 42.0518, 27.0392), 1,3 km buiten de lijn; als marker zou hij buiten de ±0,5 km-norm vallen. Niet gebruikt.
- **Dubbele lijnen**: Turkije en Bulgarije hebben een tweede lijn (282209866 naast 753522859, 0,40 km uiteen bij Strandzha 2); gekozen is de lijn met node-exacte aansluiting op 580622006.
- **EU-uitfasering** van Russisch pijpgas (verbod onder langlopende contracten uiterlijk 1-11-2027, volgens de haalbaarheidstoets) hier niet geverifieerd.
- Tooling: pyosmium geblokkeerd; geometrie komt uit een eigen pure-Python PBF-scan (kopie van `gas-galkynysh-khorgos-pbfscan.py`).

## 8 · Bronnen
[1] Wikipedia — TurkStream (474 km Provadia→grens, Zaječar, Horgoš, Hongarije 15 km, 2 × 15,75 bcm/j). https://en.wikipedia.org/wiki/TurkStream
[2] Wikipedia — Balkan Stream (880 km, ~16 bcm/j uit Turkije, 13,88 bcm/j naar Servië, in bedrijf 2021). https://en.wikipedia.org/wiki/Balkan_Stream
[3] Global Energy Monitor — Balkan Stream gas pipeline (474 km, 20 bcm/j, in bedrijf dec 2020). https://www.gem.wiki/Balkan_Stream_gas_pipeline
[4] Interfax, 1-4-2026 — 18,1 bcm naar Europa en 7,6 bcm naar Turkije in 2025. https://interfax.com/newsroom/top-stories/116906/
[5] TASS (ENTSOG) — 18,1 bcm in 2025 (+8,3%); jan–sep 2026 13,2 bcm (+1,4%, 79%); gelezen via zoekresultaat. https://tass.com/economy/2067605 · https://tass.com/economy/2195565
[6] S&P Global, feb 2026 — 16,8 bcm in 2025 (zoekresultaat). https://www.spglobal.com/energy/en/news-research/latest-news/natural-gas/020226-russian-gas-flows-to-europe-via-turkstream-remain-at-sustained-high-in-jan
[7] Capital.bg, 12-11-2025 — Bulgaarse sectie bijna 100% transit naar Servië/Hongarije (zoekresultaat). https://www.capital.bg/en/energy/2025/11/12/4851531_uncertainty_grows_over_turkstreams_future_amid_new_eu/
[8] FGSZ — tienjarenplan 2020 (grens SRB-HU→Kiskundorozsma 15 km DN1200 + meetstation; Servië→Hongarije 8,5 bcm/j), gelezen via zoekresultaat. https://fgsz.hu/file/documents/1/1743/2020_07_09_ten_year_network_development_plan.pdf
[9] Budapest Business Journal — Hongaarse en Servische sectie aaneengelast bij Horgoš (2021). https://bbj.hu/economy/energy/energy-trade/sections-of-serbian-hungarian-gas-pipeline-joined
[10] OpenStreetMap via Geofabrik-extracts bulgarije, servie, hongarije (19-7-2026), eigen PBF-scan, `man_made=pipeline` met `substance=gas`: ways uit §2/§4. https://www.openstreetmap.org/copyright
[11] Esri World Imagery via `v2/tools/sat_check.py` z15: `v2/build-cache/satcheck/sat-gas-kiyikoy-kiskundorozsma-kiskundorozsma.png`, `…-strandzha2.png`.
[12] Routebrief `gas-anapa-kiyikoy.md` — anker Kıyıköy-terminal (41.6500, 28.0752) letterlijk.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`v2/data/stroomroute-gas-kiyikoy-kiskundorozsma.json` (versie 2, lonlat, 34,6 KB) via `bash v2/tools/bak_stromen.sh gas-kiyikoy-kiskundorozsma` (functie `bak_gas_kiyikoy_kiskundorozsma`). Totaal **1.202,7 km**, 1.728 punten, 2 markers, geen stippel.

| # | modaliteit | km gebakken | punten | brief | naad naar vorige |
|---|---|---|---|---|---|
| b1 | leiding | 141,4 | 257 | geen publicatie | — |
| b2 | leiding | 646,3 | 777 | Provadia→grens 474,3 tegen 474; Strandzha–Provadia geen publicatie | 0,04 km |
| b3 | leiding | 400,1 | 650 | ca. 403, niet geverifieerd | 0,00 km |
| b4 | leiding | 14,9 | 44 | 15 | 0,00 km |

**Recept.** Geen router, geen via-punten, geen zee, geen haven-aanloop: de vier benen zijn als FeatureCollection (LineString) door `v2/build-cache/ais/graaf/gas-kiyikoy-kiskundorozsma-stitch.py` uit de OSM-scans (bulgarije, servie, hongarije, turkije) gestikt en staan in `v2/build-cache/ais/graaf/gas-kiyikoy-kiskundorozsma-leiding-<van>-<naar>.geojson`; de functie hangt ze met `--been-geojson "leiding|…"` in reisvolgorde aan elkaar. Markers: Kıyıköy-terminal 41.6500,28.0752 (0,19 km van de lijn) en Kiskundorozsma-station 46.2962,20.0352 (0,00 km). Geen letterlijke kopie van een andere stroom.

**Toets.** Naden max 0,04 km (de 0,45 km langs de lijn bij Provadia zit binnen b2). Km: b2 en b4 binnen de norm van de enige echte publicaties (Provadia→grens +0,1%, b4 −0,7%); b1, Strandzha–Provadia en b3 zijn alleen OSM (indicatie, geen norm). `toets_knikken.py`: 58 knikken ≥ 60° (b1 3, b2 44, b3 11, b4 0), 0 omkeringen en 0 terugloop; het zijn OSM-spikes en krappe bochten in de leidingstikkerij, geen routerfout. `toets_rechte_benen.py`: geen melding voor deze stroom. `json.load` ok, alle modaliteiten `leiding`, elk been ≥ 2 punten.

**Toelichting.** Geen stippel: er ontbreekt geen stuk OSM. Geen aanloop en geen vlucht. Het id noemt Kiskundorozsma en het eindpunt is Kiskundorozsma. Kıyıköy-anker hergebruikt uit `gas-anapa-kiyikoy`; Malkoçlar-station niet gemarkeerd (1,3 km buiten de lijn).

**Lessen.** (1) Een gestikte OSM-leiding hoeft niet langs de router: vooraf gebakken FeatureCollections en een functie zonder via-punten volstaan en geven 0,04 km naad. (2) Zodra een brief maar één gepubliceerde lengte kent (Provadia→grens), is de ±15%-toets voor de rest een indicatie. (3) De 58 knikken in b2/b3 zijn OSM-spikes (R 44–500 m); ze vragen geen herbakken.

