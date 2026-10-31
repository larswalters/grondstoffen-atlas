# Routebrief (licht) · Goud — Borborema (Aura Minerals, Rio Grande do Norte) → Natal (NAT) → Toronto Pearson (YYZ) → Asahi Refining Canada (Brampton)

**stroom-id:** `goud-borborema-asahibrampton` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** doré van de Borborema-plant (Currais Novos) gaat (aannemelijk) per truck over BR-226 en BR-304 naar de vrachtloods van Natal-São Gonçalo do Amarante (NAT), per vrachtvlucht (grootcirkel) naar de vrachtterminal van Toronto Pearson (YYZ) en per truck naar Asahi Refining Canada (130 Glidden Road, Brampton). **Het eind (b4, b5) is gedeeld met `goud-jacobina-asahibrampton`.**
**Welke as van het verhaal:** tweede Braziliaanse doré-speler bij Asahi Canada. Nominaal **2,2 t Au/j**: 72.240 oz/j ÷ 32,15 [1 par. 22.5]; 2025 was opstart (ramp-up maart, commerciële productie sept 2025): 28.573 GEO = 0,9 t [2]. Alleen het contract is gebronnd; **weg en vlucht zijn aannemelijk, geen bron voor het vervoer**.

## 1 · Ketenkaart
```
Borborema-plant (Aura Minerals) `au-borborema-plant`
  ──(b1 truck · BR-226 → BR-304 → Rodovia Humberto Pessoa → Av. Dr. Ruy Pereira dos Santos · OSRM 148,8 wegkm, hemelsbreed 113,6, geen wegkm)──► weg bij NAT-vrachtloods (-5.7634, -35.3668)
  ──(b2 stippel · 0,11 km · last mile, airside)──► NAT-vrachtloods `au-nat-vrachtterminal`
  ──(b3 lucht · vlucht NAT → YYZ, grootcirkel, aannemelijk · 7.062,8 km)──► YYZ-vrachtterminal `au-yyz-vrachtterminal`
  ──(b4 stippel · 0,08 km · airside, KOPIE jacobina b4)──► openbare weg W van de loodsen (43.6786, -79.6345)
  ──(b5 truck · Britannia Rd E → Dixie Rd → Steeles Ave E → Glidden Rd · 12,9 km, KOPIE jacobina b5)──► Asahi Refining Canada `au-asahi-brampton` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Borborema-plant → weg bij NAT-vrachtloods | BR-226 (Currais Novos, Santa Cruz, Tangará) → BR-304 → Rodovia Humberto Pessoa → Av. Dr. Ruy Pereira dos Santos; aannemelijk: contract gebronnd, vervoer niet | **geen gepubliceerde wegkm naar NAT**; hemelsbreed 113,6 km, geen wegkm; OSRM 148,8 [5]; TRS noemt 172 km tot Natal-STAD (ander eindpunt) [1]: indicatie, geen norm | maak_stroombeen_weg (extract brazilie) | nee |
| b2 | A | truck | weg → NAT-vrachtloods | eigen terrein, airside, last mile | 0,11 [berekend] | `--stippel` | **ja** — "last mile (geen net op deze korrel)" |
| b3 | B | lucht | NAT → YYZ | vlucht NAT → YYZ, grootcirkel; aannemelijk: geen bron voor de vlucht, tussenlanding mogelijk (geen lijndienst NAT–YYZ) | **7.062,8** grootcirkel, 284 punten (`maak_luchtbeen`, reeds gemaakt) | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | YYZ-platform → openbare weg (43.6786, -79.6345) | eigen terrein, airside | 0,08 [berekend] | `--stippel`, **letterlijke kopie** van `goud-jacobina-asahibrampton` b4 | ja |
| b5 | C | truck | YYZ landside → Asahi Brampton | Britannia Rd E → Courtneypark Dr E → Dixie Rd → Steeles Ave E → West Dr → Glidden Rd; aannemelijk (pand onzeker) | **hemelsbreed 7,1 km, geen gepubliceerde wegkm**; gebakken 12,9 (OSRM 13,0) [7] | **letterlijke kopie** van het geojson van `goud-jacobina-asahibrampton` b5 | nee |

De plant ligt 26-30 km van Currais Novos (20-F 26 km, TRS 30 km) [1][2]; de keten start bij de plant, niet bij de pit. Dat de doré via NAT en per lucht gaat is een aanname: TRS zegt alleen dat de doré onder contract door Asahi Refining Canada wordt geraffineerd en dat Auramet de marketing doet [1]. Een webzoek (Aura, Borborema, Natal, doré-vervoer) leverde niets op.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-borborema-plant` | mijn / verwerking | Borborema-plant (Aura Minerals), Currais Novos, RN | -6.2030, -36.2945 | [1][2][8] | bron-gelegd (z14 + z16 gezien: verwerkingsinstallatie met ronde tanks en gebouwen direct W van de pit, tailings- en afvalhopen ernaast, 0,8 km zandweg naar BR-226 in het Z; OSRM snapt op 88 m). TRS-centrum -6.205, -36.285 ligt 1 km ZO in de pit; het UTM-punt uit de 20-F (9.314.875,56 N / 800.289,00 E, zone 24 S, omgerekend -6.1914, -36.2866) ligt 1,4 km NNO op bos/stuwmeer en is niet gebruikt |
| `au-nat-vrachtterminal` | overslag truck → lucht | Natal / São Gonçalo do Amarante (NAT), Terminal de Cargas | -5.7643, -35.3671 | [3][4][8] | bron-gelegd, pand onzeker (z16 gezien: klein loodscluster met platform ZO van de passagiersterminal, aan de platformrand; OSM-way 286146198 "Terminal de Cargas" is een extrapolatie van een plattegrond, dus pandniveau niet vast) |
| `au-yyz-vrachtterminal` | overslag lucht → truck | Toronto Pearson cargo-apron (Cargo 1/2/3, Britannia Rd E) | 43.6785, -79.6335 | [7] | **letterlijk hergebruikt** uit `goud-jacobina-asahibrampton.md` (daar uit `goud-guyana-ottawa.md`, bron-gelegd) |
| `au-asahi-brampton` | raffinaderij, stoppunt | Asahi Refining Canada, 130 Glidden Road, Brampton | 43.6907, -79.7196 | [1][6][7] | **letterlijk hergebruikt** uit `goud-jacobina-asahibrampton.md`: aannemelijk, pand onzeker (OSM-adrespunt) |

## 4 · Via-punten (alleen b1; lat, lon; punten uit de OSRM-geometrie, 1-6 m van de OSM-weg, dus op de doorgaande weg)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | BR-226, ca 20 km ten O van de plant | -6.1962, -36.1484 | pint de BR-226 oostwaarts, buiten Currais Novos |
| b1 | 2 | BR-226, ca 50 km, voorbij Santa Cruz | -6.2584, -35.9191 | punt ligt ten O van de stad: laat de lijn de BR-226-omleiding volgen, niet het centrum (-6.2294, -36.0206) |
| b1 | 3 | BR-226, ca 80 km, voorbij Tangará | -6.1122, -35.7141 | idem voor Tangará (centrum -6.196, -35.751) |
| b1 | 4 | BR-226, ca 100 km | -5.9900, -35.5952 | houdt de lijn op de BR-226 en weg van zijwegen naar de zuidelijke route naar Natal-stad |
| b1 | 5 | knoop BR-226 / BR-304 | -5.8910, -35.4937 | de keuze: BR-304 noordoostwaarts naar de Natal-omleiding, niet de BR-226 door het stadscentrum van Natal |
| b1 | 6 | BR-304 / Rodovia Humberto Pessoa | -5.8684, -35.3727 | pint het oversteekpunt naar de noordelijke ontsluiting van de luchthaven |
| b1 | 7 | Rodovia Humberto Pessoa, noordwaarts | -5.7950, -35.3597 | naar Av. Dr. Ruy Pereira dos Santos (toegangsweg luchthaven) |
Eindanker b1 = weg (-5.7634, -35.3668), niet het NAT-anker (airside). OSRM snapt dit punt op 1 m op een weg die [9] als tertiary kent; de laatste ca 0,4 km zijn naamloze servicewegen.
Wegprofiel voor de bak: sleutel `goud-borborema-asahibrampton-plant-nat`, extract `brazilie`, refs `BR-226` en `BR-304`, `gepubliceerdKm` 172 met bronnoot "TRS: 172 km tot Natal-stad, indicatie", venster 40 km. De eerste 0,8 km vanaf de plant is een zandweg (waarschijnlijk `highway=track`, komt de scanner niet door): lukt de snap niet, laat b1 dan op de BR-226 (ca -6.2097, -36.2954) beginnen en zet een `--stippel` "last mile (geen net op deze korrel)" van het plantanker.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Borborema-plant | Aura Minerals | erts (2 Mt/j) → doré | 72.240 oz Au/j nominaal | [1] par. 22.5 |
| Asahi Refining Canada, Brampton | Asahi Holdings (Japan) | doré → London Good Delivery-baren | niet gepubliceerd | [1][6] |

## 6 · Stoppunt
De brief stopt bij Asahi Refining Canada: de TRS noemt Asahi alleen als raffinage-contractpartij en geen bron noemt een vervolgzending. Fase D en E vervallen.

## 7 · Open punten
- **BINDEND (toets) verwerkt:** mijnanker op het ontginningscomplex ZW van het TRS-centrum (-6.2030, -36.2945, gezien); OSRM 148 wegkm naar NAT, hemelsbreed geen wegkm; vlucht NAT-YYZ 7.062,8 km; b4/b5 letterlijke kopie van Jacobina; beennaam "aannemelijk: contract gebronnd, vervoer niet"; eind gedeeld met Jacobina.
- **Geen bron voor het vervoer:** weg naar NAT, de vlucht (geen lijndienst NAT-YYZ, tussenlanding of een andere luchthaven, bv. Recife of Fortaleza, is niet uit te sluiten) en zelfs de luchtmodaliteit zijn aannames; Aura noemt alleen het contract.
- **Klant in de 20-F:** de 20-F noemt voor het segment Borborema "Asahi Refining Inc." en Metalor [2]; de TRS noemt Asahi Refining Canada [1]. Welk deel naar Brampton gaat is niet gepubliceerd; Metalor is niet getekend.
- **Volume:** 72.240 oz/j is de ontwerpwaarde uit de TRS-formule (2 Mt x 1,22 g/t x 92,1%); 2025 gaf 28.573 GEO (opstart) [2]; 2026-productie niet gecontroleerd.
- **NAT-pand onzeker:** de OSM-way is een extrapolatie, het vrachtloods op pandniveau niet vast. Het UTM-punt uit de 20-F ligt 1,4 km van het gezien complex; de plant is gelegd op de beelden, niet op dat punt.
- **Wegkm b1/b5:** geen gepubliceerde wegkm; 148,8 (OSRM) en 12,9 zijn indicaties, de ±15%-toets is geen norm. 172 km (TRS) geldt voor Natal-stad.
- **Brazilië-scan:** de brazilie-extract is een reus-scan (ca 7 min); eerste bake moet bevestigen dat de lijn bij Santa Cruz en Tangará niet door het centrum buigt.
- **Lage novelty:** eindbenen en bestemming identiek aan Jacobina en Orcopampa; alleen b1, b2 en de vlucht NAT-YYZ zijn nieuwe lijn.

## 8 · Bronnen
[1] Aura Minerals, Technical Report Summary Borborema Gold Project, 30-03-2026 (exh. 96.2): 172 km tot Natal via BR-226, 30 km van Currais Novos, raffinage onder contract met Asahi Refining Canada, Auramet marketing, 72.240 oz/j. https://www.sec.gov/Archives/edgar/data/1468642/000117184326002127/exh_962.htm
[2] Aura Minerals, 20-F FY2025 (31-03-2026): 26 km van Currais Novos, UTM-coordinaat, ramp-up maart 2025, commerciële productie sept 2025, 28.573 GEO in 2025, klanten Asahi Refining Inc. en Metalor voor Borborema. https://www.sec.gov/Archives/edgar/data/1468642/000117184326002127/f20f_033126.htm
[3] Wikipedia, "Greater Natal International Airport": São Gonçalo do Amarante, 25 km van Natal, coördinaat -5.7689, -35.3664, concessie Zurich Airport Brasil, bedoeld voor passagiers- en vrachtverkeer. https://en.wikipedia.org/wiki/Greater_Natal_International_Airport
[4] OpenStreetMap, way 286146198 "Terminal de Cargas" (aeroway=terminal, extrapolatie). https://www.openstreetmap.org/way/286146198
[5] OSRM publieke demo-router (OSM): plant -6.2030, -36.2945 → -5.7634, -35.3668 = 148,8 km; snaps 88 m en 1 m. https://router.project-osrm.org
[6] Asahi Refining, About us: Asahi Refining Canada, 130 Glidden Road, Brampton. https://www.asahirefining.com/about-us/
[7] `goud-jacobina-asahibrampton.md` (b4, b5, ankers YYZ en Asahi; `bak_goud_jacobina_asahibrampton` in `v2/tools/bak_stromen.sh`).
[8] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-goud-borborema-asahibrampton-mijn.png`, `-mijn-20f`, `-plant`, `-nat` (z14-z16, 2026-10-31).
[9] OpenStreetMap via Nominatim reverse: way 286005773 (tertiary, Maçaranduba, São Gonçalo do Amarante). https://nominatim.openstreetmap.org
[10] Haalbaarheidstoets goud-borborema-asahibrampton (orkestrator): mijnanker, OSRM 148 km, vlucht 7.063 km; niet zelf teruggevonden.
[v1] `data/goud.js`: geen Borborema, geen Natal.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
`v2/data/stroomroute-goud-borborema-asahibrampton.json` · 52,2 KB · versie 2, lonlat · 5 benen · **7.220,7 km** · 2.479 punten · 4 markers · `bash v2/tools/bak_stromen.sh goud-borborema-asahibrampton` (functie `bak_goud_borborema_asahibrampton`).

| # | modaliteit | km | naad | recept / toets |
|---|---|---|---|---|
| b1 | truck | 144,8 | 0 | profiel `goud-borborema-asahibrampton-plant-nat` (extract brazilie, reus-scan, refs BR-226/BR-304, venster 40 km, eindKlassen incl. track); **144,7-144,8 tegen OSRM 148,8 = -2,7% [indicatie]**, tegen TRS 172 (Natal-stad, ander eindpunt) -15,9%; hemelsbreed 113,6, geen wegkm; plant snapt op 0,09 km (eerste 0,81 km unclassified), alle via-snaps 0,00-0,01 km |
| b2 | truck, stippel | 0,11 | 0 | `--stippel` last mile NAT-vrachtloods (geen net op deze korrel), -5.7634,-35.3668 -> -5.7643,-35.3671 |
| b3 | lucht | 7.062,8 | 0 | `maak_luchtbeen.py`, 284 punten, grootcirkel NAT -> YYZ, doorgetrokken (geen stippel) |
| b4 | truck, stippel | 0,08 | 0 | `--stippel` YYZ-vrachtplatform airside, **letterlijke kopie** jacobina b4, 43.6785,-79.6335 -> 43.6786,-79.6345 |
| b5 | truck | 12,9 | 0 | **letterlijke kopie** van het geojson `goud-jacobina-asahibrampton-weg-yyz-asahi.geojson` (310 punten); hemelsbreed 7,1, geen wegkm: indicatie |

**Markers:** au-borborema-plant, au-nat-vrachtterminal, au-yyz-vrachtterminal, au-asahi-brampton, allemaal 0,0 km van hun lijn (anker = lijneinde). Naden alle 0,000 km.

**Stippels:** b2 (loods 0,11 km van de weg) en b4 (YYZ airside). Geen haven-aanloop (geen zee).

**Vlucht:** doorgetrokken grootcirkel tussen twee vrachtterminals; aannemelijk, geen bron voor de vlucht of een tussenlanding. Dat staat in de beennaam.

**Toetsen:** `toets_knikken.py`: 39 knikken >= 60 graden (11 op b1, 28 op de b5-kopie), 1 omkering (167 graden) op b1 bij -5.8684,-35.3750, 0 terugloop. `toets_rechte_benen.py --min-km 5` meldt niets voor deze stroom. `json.load` ok, versie 2, lonlat, modaliteiten in {truck, lucht}, elk been >= 2 punten.

**Bevindingen / open:** (1) Via 6 uit de brief (-5.8684,-35.3727) lag 0,23 km op een zijtak en gaf een keerlus van 0,46 km; verplaatst naar -5.8688,-35.3778 op BR-304 (profiel en functiekop dragen de noot). De lijn houdt daarna toch een keerlus van ca 0,5 km bij -5.8684,-35.3750 (OSM-geometrie van de afslag naar Rodovia Humberto Pessoa, 0 terugloop): laten staan. (2) Geen omweg door Santa Cruz of Tangara (segmenten 30,1 en 29,9 km, hemelsbreed ca 29-30 km). (3) Vervoer weg en vlucht blijft een aanname; NAT-pand onzeker; Brampton-pand onzeker (zie jacobina). (4) De 172 km van de TRS geldt Natal-stad en is geen norm voor dit eindpunt.

**Lessen:** een via-punt dat uit een router-geometrie is overgenomen kan op een dubbelbaans-afslag liggen waar de router terugkeert; controleer na de scan `toets_knikken` op 150+ graden. De reus-scan brazilie duurde ca 9 minuten per run (slotwachttijd komt erbij); een via-wijziging dwingt een volledige herscan. LF gecontroleerd (0 CRLF in bak_stromen.sh en maak_stroombeen_weg.py).
