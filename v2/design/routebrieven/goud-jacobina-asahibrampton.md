# Routebrief (licht) · Goud — Jacobina (Pan American Silver, Bahia) → Salvador → Toronto Pearson → Asahi Refining Canada (Brampton)

**stroom-id:** `goud-jacobina-asahibrampton` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** doré van het Jacobina-complex gaat (aannemelijk) per truck over BR-324 en BA-526 naar de vrachtloods van Salvador (SSA), per vrachtvlucht (grootcirkel) naar de vrachtterminal van Toronto Pearson (YYZ) en per truck over Dixie Road en Steeles Avenue naar Asahi Refining Canada (130 Glidden Road, Brampton).
**Welke as van het verhaal:** Braziliaans mijndoré naar een Canadese raffinaderij onder contract. Jacobina produceerde in 2025 190,5 koz = **5,9 t Au/j** (190,5 ÷ 32,15) [1][2]; guidance 2026 181–191 koz (haalbaarheidstoets). Alleen het contract is gebronnd; **weg en vlucht zijn aannemelijk, geen bron voor het vervoer**.

## 1 · Ketenkaart
```
Jacobina-plant (Pan American Silver) `au-jacobina-plant`
  ──(b1 truck · BR-324 → BA-526 · 345,4 wegkm OSRM, 340 gepubliceerd [1])──► weg Rua Eng. José Afonso Teixeira (-12.9152, -38.3278)
  ──(b2 stippel · 0,19 km · last mile)──► SSA-vrachtloods `au-ssa-vrachtterminal`
  ──(b3 lucht · vlucht SSA → YYZ, grootcirkel, aannemelijk · 7.557 km)──► YYZ-vrachtterminal `au-yyz-vrachtterminal`
  ──(b4 stippel · 0,08 km · last mile, airside)──► openbare weg W van de loodsen (43.6786, -79.6345)
  ──(b5 truck · Britannia Rd E → Courtneypark → Dixie Rd → Steeles Ave E → Glidden Rd · 13,0 km OSRM)──► Asahi Refining Canada `au-asahi-brampton` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Jacobina-plant → weg bij SSA-vrachtloods | BR-324 (Jacobina, Capim Grosso, Feira de Santana, Simões Filho) → BA-526 (Estrada CIA Aeroporto); aannemelijk: geen bron voor het vervoer | **340 gepubliceerd** [1] (Salvador "340 km SSE van het complex"); OSRM 345,4 (+1,6%) [7]; hemelsbreed 301 | maak_stroombeen_weg (extract brazilie) | nee |
| b2 | A | truck | weg → SSA-vrachtloods | eigen terrein, last mile | 0,19 [berekend] | `--stippel` | **ja** — "last mile (geen net op deze korrel)" |
| b3 | B | lucht | SSA → YYZ | vlucht SSA → YYZ, grootcirkel; aannemelijk: geen bron voor de vlucht (tussenlanding GRU of MIA mogelijk) | **7.557,1** grootcirkel, 304 punten (`maak_luchtbeen`) | maak_luchtbeen, reeds gemaakt: `goud-jacobina-asahibrampton-lucht-ssa-yyz.geojson` | nee — doorgetrokken |
| b4 | C | truck | YYZ-platform → openbare weg (43.6786, -79.6345) | eigen terrein, airside | 0,08 [berekend] | `--stippel` (patroon goud-guyana-ottawa) | ja |
| b5 | C | truck | YYZ landside → Asahi Brampton | Britannia Rd E → Courtneypark Dr E → Dixie Rd → Steeles Ave E → West Dr → Glidden Rd; aannemelijk (pand onzeker) | **hemelsbreed 7,1 km, geen gepubliceerde wegkm**; OSRM 13,0 [7] | maak_stroombeen_weg (extract canada) | nee |

De mijn ligt 10 km van de stad Jacobina [1]; de keten start bij de plant, niet bij een mijnopening. Dat de doré überhaupt via Salvador en per lucht gaat is een aanname: de AIF zegt alleen dat de doré "naar de raffinaderij wordt vervoerd" [1].

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-jacobina-plant` | mijn / verwerking | Jacobina-verwerkingsplant (Pan American Silver), Bahia | -11.2575, -40.5195 | [1][2][4] | bron-gelegd (z16 gezien: plantgebouwen met transportbanden en stapels, aan de mijnweg; tailingsdam NW en stuwmeer ZW; OSRM snapt op 51 m). Wikidata-mijnpunt -11.2578, -40.5250 ligt 0,5 km W, in het mijndistrict |
| `au-ssa-vrachtterminal` | overslag truck → lucht | Salvador International (SSA), Terminal de Logística de Carga | -12.9140, -38.3291 | [5] | bron-gelegd (z16 gezien: groot loodsgebouw op de vrachtapron ZO van de passagiersapron, tussen platform en duinen; OSM-way 897713278 "Terminal de Logística de Carga" op 5 m). Het ontwerpanker -12.9086, -38.3225 lag op de baan en is niet gebruikt |
| `au-yyz-vrachtterminal` | overslag lucht → truck | Toronto Pearson cargo-apron (Cargo 1/2/3, Britannia Rd E) | 43.6785, -79.6335 | [10] | **letterlijk hergebruikt** uit `goud-guyana-ottawa.md` (daar bron-gelegd); eigen blik z16: apron met wijdrompvrachttoestellen tussen drie lange loodsen |
| `au-asahi-brampton` | raffinaderij, stoppunt | Asahi Refining Canada, 130 Glidden Road, Brampton | 43.6907, -79.7196 | [3][6] | **aannemelijk, pand onzeker** (z16/z17 gezien: industrieterrein langs Hwy 410; het OSM-adrespunt, node 1126612341, ligt op de hoek van Glidden Rd en het groenstrookje, ~100 m van de dichtstbijzijnde panden; postcode in OSM L6W 3K7, Asahi noemt L6W 3M8) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; lat, lon; punten uit de OSRM-geometrie, dus op OSM-weg)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | BR-324, ZO van Jacobina (ca 20 km) | -11.2090, -40.4529 | pint de BR-324 bij het verlaten van Jacobina, buiten het centrum |
| b1 | 2 | BR-324, tussen Capim Grosso en Riachão do Jacuípe | -11.4727, -39.7863 | doorgaande BR-324, Capim Grosso-centrum niet nodig |
| b1 | 3 | BR-324, ca 160 km | -11.8211, -39.3706 | midden van de corridor, sluit zijwegen via Ipirá uit |
| b1 | 4 | BR-324, ten N van Feira de Santana | -12.0051, -39.0632 | pint de BR-324 vóór de stad |
| b1 | 5 | BR-324, ZO van Feira de Santana (contorno) | -12.3093, -38.8867 | laat de stadsdoorsnijding aan de BR-324 volgen, niet de stad zelf |
| b1 | 6 | BR-324, ca 285 km (Simões Filho-zone) | -12.5302, -38.6028 | doorgaande BR-324 richting Salvador |
| b1 | 7 | knoop BR-324 / BA-526 (Estrada CIA Aeroporto) | -12.8206, -38.4085 | hier gaat de route van de BR-324 op de BA-526 naar het vliegveld; beperkt de keuze tot de luchthaventoegang |
| b5 | 1 | Britannia Rd E / Courtneypark Dr E | 43.6660, -79.6315 | verlaat de airside-ringweg via de eerste openbare weg |
| b5 | 2 | Courtneypark Dr E / Dixie Rd | 43.6636, -79.6581 | kiest Dixie Road noordwaarts (niet Hwy 407/410) |
| b5 | 3 | Dixie Rd / Steeles Ave E | 43.6952, -79.7011 | pint Steeles Ave E westwaarts |
| b5 | 4 | West Dr | 43.6907, -79.7062 | naar Glidden Rd en het eindanker |
Eindanker b1 = weg (-12.9152, -38.3278), niet het SSA-anker (airside/terreinweg). Eindanker b5 = Asahi (OSRM snapt op Glidden Road op 9 m).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Jacobina-plant | Pan American Silver | erts (8.400 t/d) → doré | 190,5 koz goud in 2025 | [1][2] |
| Asahi Refining Canada, Brampton | Asahi Holdings (Japan) | doré → London Good Delivery-baren | niet gepubliceerd | [1][3] |

## 6 · Stoppunt
De brief stopt bij Asahi Refining Canada: de AIF zegt dat de doré daar tot London Good Delivery-baar wordt geraffineerd en daarna op de internationale markt wordt verkocht; geen bron noemt een vervolgzending. Fase D en E vervallen.

## 7 · Open punten
- **BINDEND (toets) verwerkt:** plantanker i.p.v. mijnpunt; SSA-vracht -12.9140, -38.3291 (niet de baan); wegkm 340 gepubliceerd naast OSRM 345,4; vlucht "aannemelijk: geen bron voor het vervoer"; YYZ-anker letterlijk met airside-stippel; Brampton hemelsbreed 7,1 km, geen wegkm.
- **Geen bron voor het vervoer:** de AIF zegt alleen "contract met Asahi Refining Canada" en "doré wordt vervoerd" [1]. Weg naar SSA, de vlucht SSA → YYZ en een directe vlucht zijn aannames; een tussenlanding (GRU, MIA) of een geldtransport per weg/zee is niet uit te sluiten. Webzoek (Pan American, Wood Mackenzie, G Mining) leverde geen vervoerinfo.
- **Brampton-pand onzeker:** adrespunt op een hoek, postcode wijkt af (L6W 3K7 tegenover L6W 3M8); Nominatim vond het postcodepunt L6W 3M8 niet. Asahi heeft ook een site in Salt Lake City; de AIF noemt Asahi Refining Canada.
- **Wegkm b5:** geen gepubliceerde kilometer; 13,0 km OSRM is indicatie, de ±15%-toets is hier geen norm.
- **Brazilië-scan:** de brazilie-extract is een reus-scan; BR-324 in Feira de Santana loopt door de stad (Av. Eduardo Froes da Mota / Av. Luís Eduardo Magalhães); via 5 ligt erachter. Eerste bake moet bevestigen dat de lijn niet door het centrum buigt.
- Guidance 2026 (181–191 koz) komt uit de haalbaarheidstoets, niet zelf teruggevonden.

## 8 · Bronnen
[1] Pan American Silver, Annual Information Form FY2025: Jacobina 190,5 koz in 2025; Salvador 340 km SSE; "contract in place with Asahi Refining Canada"; doré naar London Good Delivery. https://www.sec.gov/Archives/edgar/data/771992/000077199226000019/aif-2025ye.htm
[2] Pan American Silver, Jacobina: 190,5 koz, 8.400 tpd, doré, 7 zones. https://panamericansilver.com/operations/gold-segment/jacobina/
[3] Asahi Refining, About us: Asahi Refining Canada, 130 Glidden Road, Brampton L6W 3M8. https://www.asahirefining.com/about-us/
[4] Wikidata Q16965377 (Jacobina mine): -11.2577971, -40.5250394. https://www.wikidata.org/wiki/Q16965377
[5] OpenStreetMap via Photon: way 897713278 "TERMINAL DE LOGÍSTICA DE CARGA", Salvador (-12.9140, -38.3291). https://www.openstreetmap.org/way/897713278
[6] OpenStreetMap via Nominatim: 130 Glidden Road, Brampton, node 1126612341 (43.6907, -79.7196), postcode L6W 3K7. https://nominatim.openstreetmap.org
[7] OSRM publieke demo-router (OSM): plant → SSA 345,4 km, YYZ landside → Asahi 13,0 km; snaps 51 m, 192 m, 9 m. https://router.project-osrm.org
[8] Wikipedia, "Jacobina mine": Bahia; eigenaar Yamana Gold (verouderd, nu Pan American). https://en.wikipedia.org/wiki/Jacobina_mine
[9] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-goud-jacobina-asahibrampton-plant.png`, `-mijn`, `-ssa`, `-asahi`, `-asahi-z17`, `-yyz` (z15-z17, 2026-10-31).
[10] `goud-guyana-ottawa.md` — YYZ-vrachtterminal (43.6785, -79.6335) en airside-stippel 43.6785,-79.6335 → 43.6786,-79.6345.
[11] Haalbaarheidstoets goud-jacobina-asahibrampton (orkestrator): guidance 2026, SSA-ankercorrectie, OSRM-cijfers; niet zelf teruggevonden.
[v1] `data/goud.js`: geen Jacobina; au-air-gru als Brazilië-gateway (Paracatu).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
`v2/data/stroomroute-goud-jacobina-asahibrampton.json` · 83,7 KB · versie 2, lonlat · 5 benen · **7.915,3 km** · 3.884 punten · 4 markers · `bash v2/tools/bak_stromen.sh goud-jacobina-asahibrampton` (functie `bak_goud_jacobina_asahibrampton`).

| # | modaliteit | km | naad | recept / toets |
|---|---|---|---|---|
| b1 | truck | 345,0 | 0 | profiel `goud-jacobina-asahibrampton-jacobina-ssa` (extract brazilie, reus-scan, refs BR-324/BA-526, venster 40 km); **344,9 tegen 340 gepubliceerd = +1,4% [OK]**; snaps 0,00-0,05 km; 12 keerlussen gesnoeid (345,1 -> 344,9) |
| b2 | truck, stippel | 0,19 | 0 | `--stippel` last mile SSA (geen net op deze korrel), -12.9152,-38.3278 -> -12.9140,-38.3291 |
| b3 | lucht | 7.557,1 | 0 | `maak_luchtbeen.py`, 304 punten, grootcirkel SSA -> YYZ, doorgetrokken (geen stippel) |
| b4 | truck, stippel | 0,08 | 0 | `--stippel` YYZ-vrachtplatform last mile (airside, patroon goud-guyana-ottawa), 43.6785,-79.6335 -> 43.6786,-79.6345 |
| b5 | truck | 12,9 | 0 | profiel `goud-jacobina-asahibrampton-yyz-asahi` (extract canada, corridorKlassen unclassified, eindToegangPrivaat); router 12,9 tegen OSRM 13,0; **geen wegkm gepubliceerd, hemelsbreed 7,1 km**: indicatie, geen norm; snaps 0,00-0,01 km |

**Markers:** au-jacobina-plant, au-ssa-vrachtterminal, au-yyz-vrachtterminal, au-asahi-brampton, allemaal 0,0 km van hun lijn (anker = lijneinde). Naden alle 0,000 km.

**Stippels:** b2 en b4 zijn de enige. b2 omdat de loods 0,19 km van het eindpunt van de openbare weg ligt (BA-526 loopt niet het terrein op), b4 omdat het YYZ-platform airside ligt. Geen haven-aanloop (geen zee), geen kopie van andermans been.

**Vlucht:** doorgetrokken grootcirkel tussen twee vrachtterminals; aannemelijk, geen bron voor de vlucht of een tussenlanding (GRU, MIA). Dat staat in de beennaam.

**Toetsen:** `toets_knikken.py`: 38 knikken >= 60 graden (10 op b1, 28 op b5, bijna allemaal 60-100 graden stedelijke kruispunten), 1 omkering van 157,5 graden op de ankertip van b1 bij -12.91517,-38.32779 (de lijn stopt op het anker dat 2 m naast de weg ligt), 0 terugloop. `toets_rechte_benen.py --min-km 5` meldt niets voor deze stroom. `json.load` ok, modaliteiten in {truck, lucht}, elk been >= 2 punten.

**Bevindingen / open:** (1) BR-324 bij Feira de Santana: de contorno-via (punt 5) hield de lijn buiten het centrum, segment 44,7 km tegen 39 km hemelsbreed, geen omweg. (2) Brampton-pand blijft onzeker (OSM-adrespunt op de hoek, postcode L6W 3K7 tegenover L6W 3M8). (3) Vervoer weg + vlucht is een aanname. (4) De Brampton-weg b5 wordt door goud-orcopampa-asahibrampton letterlijk gekopieerd uit dit bestand.

**Lessen:** profielen met de reus-extracts brazilie en canada draaien samen in ruim 10 minuten via wegscan_puur.py (canada ca 4 min, brazilie ca 7 min); de via-punten uit de brief (lat,lon) moesten in het profiel naar (lon, lat). De profielen staan direct na de ankerregel NIEUWE PROFIELEN, de functie vlak voor NIEUWE STROOMFUNCTIES; LF gecontroleerd (0 CRLF in beide bestanden).

