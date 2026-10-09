# Routebrief (licht) · Goud — Guyana Gold Board (Georgetown) → Toronto Pearson → Royal Canadian Mint (Canada)

**stroom-id:** `goud-guyana-ottawa` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** door de Guyana Gold Board gekocht goud gaat per truck over de East Bank Road naar het platform van Cheddi Jagan Intl (GEO), per vrachtvlucht (grootcirkel, aannemelijk) naar de vrachtterminal van Toronto Pearson (YYZ) en per truck over Hwy 401, 416 en 417 naar de Royal Canadian Mint (320 Sussex Drive, Ottawa).
**Welke as van het verhaal:** staatsinkoop in Guyana naar Canadese raffinage. Guyana voerde in 2023 437 koz uit (**13,6 t Au/j**; 432 koz aangegeven = 13,4 t) [1]; 2025: 484.321 oz aangegeven (15,1 t) [6]. Canada nam in 2023 ca 12,5% (≈1,7 t, indicatie), de VAE ca 81% [11]: een **minderheidsstroom**; het RCM-aandeel zelf is niet gebronnd. Mijn is niet de start (Aurora/Zijin niet gelokaliseerd).

## 1 · Ketenkaart
```
Guyana Gold Board, GGMC-terrein, Georgetown `au-ggb-georgetown`
  ──(b1 truck · East Bank Road → Airport Road · 40,4 wegkm [7], 41 [5])──► rotonde Airport Road, CJIA
  ──(b2 stippel · 0,3 km · last mile, airside)──► GEO-vrachtplatform `au-geo-vrachtplatform`
  ──(b3 lucht · vlucht GEO → YYZ, grootcirkel, aannemelijk · 4.630 km)──► Toronto Pearson vrachtterminal `au-yyz-vrachtterminal`
  ──(b4 stippel · 0,09 km · last mile, airside)──► openbare weg (parkeerzone W van de loodsen)
  ──(b5 truck · Hwy 401 → 416 → 417 · 468 wegkm [7])──► Royal Canadian Mint `au-rcm-ottawa` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | GGB → rotonde Airport Road (6.5036, -58.2569) | East Bank Road (primary, naam; geen ref) → Airport Road | **40,4 wegkm** (OSRM [7]); 41 (Wikipedia [5]); hemelsbreed 35,5 | maak_stroombeen_weg (extract guyana) | nee |
| b2 | A | truck | rotonde → GEO-vrachtplatform | eigen terrein, airside | 0,29 [berekend] | `--stippel` | **ja** — apron zonder wegpad |
| b3 | B | lucht | GEO → YYZ | vrachtvlucht GEO → YYZ, grootcirkel | **4.630,1** (`maak_luchtbeen`, 187 punten) | maak_luchtbeen, reeds gemaakt: `goud-guyana-ottawa-lucht-geo-yyz.geojson` | nee — **aannemelijk: één bron voor de bestemming, geen bron voor de vlucht** |
| b4 | C | truck | YYZ-platform → openbare weg (43.6786, -79.6345) | eigen terrein, airside (way access=no) | 0,09 [berekend] | `--stippel` (laat vervallen als het wegprofiel vanaf het anker lukt) | ja |
| b5 | C | truck | YYZ landside → RCM | Hwy 401 → Hwy 416 (Johnstown–Ottawa) → Hwy 417 → Sussex Drive | **468,0 wegkm** (OSRM [7]); hemelsbreed 367,6; via-som 440,6 | maak_stroombeen_weg (extract canada) | nee |

De vlucht gaat bewust naar **YYZ** en niet naar Ottawa (YOW): vanaf GEO is Toronto de Canada-verbinding (Caribbean Airlines; Air Transat seizoen [5]); een vlucht GEO → YOW bestaat niet. Werkelijk transport kan ook via de Caribische hub of een koerier lopen: één directe vlucht aangenomen.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-ggb-georgetown` | koper / laadplek | Guyana Gold Board, GGMC Compound, Upper Brickdam St, Georgetown | 6.8052, -58.1527 | [1][8] | bron-gelegd (z16 gezien: stedelijk blok met blauwdakig gebouwtje, kruis op het GGMC-terrein; OSM-gebouw "Guyana Gold Board" way 346311630 op 12 m; OSRM snapt op Brickdam Street) |
| `au-geo-vrachtplatform` | overslag truck → lucht | Cheddi Jagan Intl (GEO), apron ZW van de terminal | 6.5025, -58.2545 | [8][9] | **aannemelijk, pand onzeker** (z16 gezien: tarmac naast de terminal met blauwe daken; geen herkenbare vrachtloods en geen bron die de vrachtfaciliteit noemt; OSM-aerodrome-centroïde 6.4982,-58.2559 ligt op de baan en is niet gebruikt) |
| `au-yyz-vrachtterminal` | overslag lucht → truck | Toronto Pearson cargo-apron (Cargo 1/2/3, Infield Tunnel Rd / Britannia Rd E) | 43.6785, -79.6335 | [8][9] | bron-gelegd (z15+z16 gezien: apron tussen drie lange vrachtloodsen met wide-body vrachttoestellen; OSM-gebouwen "Air Canada Cargo (Cargo 1)", "Cargo 2", "Cargo 3"). **Nieuw anker, nog niet in een andere brief** |
| `au-rcm-ottawa` | losplek / raffinaderij | Royal Canadian Mint, 320 Sussex Drive, Ottawa | 45.4315, -75.6993 | [10] | **letterlijk hergebruikt** uit `goud-malartic-ottawa.md` (daar bron-gelegd, z15); eigen scan: Sussex Drive-way op 60 m |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; lat, lon; refs in [9], eigen PBF-scan)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | East Bank Road (primary, way 1271753110) | 6.7705, -58.1758 | verlaat Georgetown op de doorgaande East Bank Road (primary, naam) |
| b1 | 2 | East Bank Road (primary, way 436770595) | 6.7209, -58.1922 | pint de oostoever-corridor |
| b1 | 3 | East Bank Road (primary, way 4680228) | 6.6302, -58.2019 | idem |
| b1 | 4 | East Bank Road (primary, way 295668125) | 6.5473, -58.2342 | laatste primary-stuk; sluit de Soesdyke-Linden Highway uit |
| b1 | 5 | splitsing East Bank Road / Airport Road (tertiary) | 6.5120, -58.2679 | enige toegang tot het terminalgebied; einde op rotonde 6.5036, -58.2569 |
| b5 | 1 | Hwy 401, Scarborough | 43.7723, -79.2946 | pint de 401 door Toronto (sluit de tolweg 407 uit) |
| b5 | 2 | Hwy 401, Oshawa | 43.8710, -78.8971 | op de 401, ca 5 km ten zuiden van de 407 (ETR) |
| b5 | 3 | Hwy 401, Belleville–Trenton | 44.1921, -77.3984 | midden van de 401-as |
| b5 | 4 | Hwy 401, Kingston | 44.2692, -76.4989 | idem |
| b5 | 5 | Hwy 416, zuideinde bij Johnstown (motorway) | 44.7499, -75.4899 | knooppunt 401/416, **niet in Toronto of Ottawa-centrum** |
| b5 | 6 | Hwy 416, midden | 44.8216, -75.5185 | op de doorgaande 416 |
| b5 | 7 | knooppunt 416/417 (Nepean, Hwy 417) | 45.3428, -75.8164 | hier gaat de route op de 417 oostwaarts naar het centrum |
Eindanker b5 = RCM (Sussex Drive-way op 60 m); geen via in het stadscentrum.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Royal Canadian Mint, raffinaderij Ottawa | Royal Canadian Mint (kroonbedrijf) | doré/baren → 99,99-goud, LBMA | geen gepubliceerd volume per bron; v1 ≈ 200 t/j nameplate (`data/goud.js`) | [10][v1] |

## 6 · Stoppunt
De brief stopt bij de RCM-raffinaderij: dat is het gegeven eindpunt; geen bron noemt een vervolgzending per lading. Fase D en E vervallen.

## 7 · Open punten
- **BINDEND (toets) verwerkt:** vlucht naar YYZ, niet YOW; b5 468 wegkm (OSRM) met hemelsbreed 367,6 letterlijk; via-punten op de 401 en op 401/416 bij Johnstown; b1 41 km; GEO-platform airside → korte stippel; Canada als ca 12,5% van de export; afnemer aannemelijk.
- **Afnemer RCM rust op weinig:** Wikipedia (2012-cijfers, ongedateerd) zegt dat al het Guyanese goud via de GGB naar de RCM gaat [2]; dpi.gov.gy 2017 noemt de RCM "refining partner" van de GGB [3] (de ">30 jaar" uit de toets heb ik daar niet teruggevonden); in 2021 schorste de RCM de aanvoer van één grote exporteur (El Dorado) via de GGB [4] en die schorsing is niet gedocumenteerd opgeheven. Export gaat nu overwegend naar de VAE [11]. Valt de afnemer-check om: stop op GEO.
- **Geen bron voor de vlucht of een vrachtdienst GEO → YYZ** met goud; gouduitvoer verliep ook op andere wegen (smokkel op CJIA is wel gemeld [12]). Geen mijn als start; het RCM-aandeel van de 13,6 t is onbekend.
- **GEO-vrachtplatform:** geen bron voor de locatie van de vracht-apron; anker is een apron-punt naast de terminal (onzeker). Het wegbeen eindigt op de rotonde en de stippel (0,29 km) draagt het ontbrekende stuk.
- **YYZ landside:** vanaf het anker (airside, service access=no) naar de openbare weg loopt de eerste route via Britannia Road East (unclassified, access=yes); het eerste tertiary-punt ligt 2,0–2,5 km verder (Courtneypark Dr E). Het wegprofiel start daarom op 43.6786, -79.6345; knip de 0,09 km-stippel als het anker zelf snapt.
- **Hwy 401/416-hoek:** de scan toont de 401 tot Johnstown (lon -75,55); de 416 begint bij 44.749, -75.490. De eerste bake moet bevestigen dat de 416 doorloopt naar de 417 (ways 1307485798 en 485841695 zijn motorway, ref 416).
- Fly Jamaica (toets, Wikipedia) is in mijn fetch niet teruggevonden; actueel GEO-YYZ: Caribbean Airlines en Air Transat (seizoen) [5].

## 8 · Bronnen
[1] Guyana Gold Board, adres GGMC Compound, Upper Brickdam St; 2023: 432 koz aangegeven, 437 koz uitgevoerd. https://ggb.gov.gy/
[2] Wikipedia, "Mining in Guyana" — alle goud verkocht aan de GGB en voor raffinage naar de RCM (ongedateerd; 2012-exportcijfers). https://en.wikipedia.org/wiki/Mining_in_Guyana
[3] DPI Guyana, 2017-07-28, "Team from the Royal Canadian Mint visits Guyana Gold Board" — RCM als "refining partners". https://dpi.gov.gy/team-from-the-royal-canadian-mint-visits-guyana-gold-board-to-assess-the-agencys-oversight-processes/
[4] Stabroek News, 2021-05-31, "Smuggled gold" — RCM schorst intake El Dorado-goud via de GGB. https://stabroeknews.com/2021/05/31/opinion/editorial/smuggled-gold
[5] Wikipedia, "Cheddi Jagan International Airport" — 41 km van Georgetown; Toronto-verbindingen. https://en.wikipedia.org/wiki/Cheddi_Jagan_International_Airport
[6] Kaieteur News, 2026-02-02 — 2025: 484.321 oz aangegeven, exportwaarde US$ 1,6 mld. https://kaieteurnewsonline.com/2026/02/02/gold-export-hit-us1-6b-bauxite-reaches-us144-1m-in-2025/
[7] OSRM publieke demo-router (OSM): GGB → rotonde CJIA 40.355,8 m; YYZ cargo → RCM 467.988,6 m. https://router.project-osrm.org
[8] OpenStreetMap via Photon/Nominatim: GGB way 346311630 (6,8052/-58,1527); aerodrome GEO; Toronto Cargo 1/2/3 (43,6764-43,6793 / -79,6309…-79,6357); RCM Sussex Drive. https://www.openstreetmap.org
[9] Eigen scan van de Geofabrik-PBF's guyana en canada (pure-Python-lezer): wegen, refs en vertexcoördinaten in §4. https://download.geofabrik.de
[10] Royal Canadian Mint, "Storage and refinery". https://www.mint.ca/en/storage-and-refinery
[11] Haalbaarheidstoets goud-guyana-ottawa (orkestrator): OEC-mirror 2023, Canada 12,5% / VAE 81%; niet zelf teruggevonden.
[12] Jamaica Observer, 2024-06-06, gouddouane op CJIA. https://www.jamaicaobserver.com/2024/06/06/three-busted-alleged-smuggling-gold-guyana-airport/
[v1] `data/goud.js`, `design/goud.md` — au-ref-rcm ≈ 200 t/j; au-air-yyz als v1-uitgang Canada.
Satellietblik: `v2/build-cache/satcheck/sat-goud-guyana-ottawa-ggb.png`, `…-geo.png`, `…-geo-terminal.png`, `…-geo-oost.png`, `…-yyz.png`, `…-yyz-cargo.png` (Esri z15–z16, 2026-10-09).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-goud-guyana-ottawa.json` (78,5 KB, versie 2, lonlat) · functie `bak_goud_guyana_ottawa()` in `v2/tools/bak_stromen.sh` · profielen `goud-guyana-ottawa-ggb-geo` en `goud-guyana-ottawa-yyz-rcm` in `maak_stroombeen_weg.py`. **Totaal 5.139,1 km, 5 benen, 4 markers, alle naden 0,000 km.**

| # | modaliteit | km gebakken | km brief | afwijking | stippel |
|---|---|---|---|---|---|
| b1 | truck GGB → rotonde CJIA | 40,1 | 41 (Wikipedia; OSRM 40,4) | -2,3% (OK) | nee |
| b2 | truck last mile GEO-platform | 0,29 | 0,29 | 0 | ja, airside |
| b3 | lucht GEO → YYZ | 4.630,1 | 4.630,1 | 0 | nee, doorgetrokken (aannemelijk) |
| b4 | truck last mile YYZ-platform | 0,08 | 0,09 | afronding | ja, airside |
| b5 | truck YYZ → RCM | 468,5 | 468,0 (OSRM) | +0,1% (OK) | nee |

**Recept.** b1: `wegscan_puur.py --profiel goud-guyana-ottawa-ggb-geo` (extract guyana, venster 20 km, geen refs, 6 segmenten, alle snaps ≤ 0,06 km). b5: `wegscan_puur.py --profiel goud-guyana-ottawa-yyz-rcm` (extract canada, 443 s scan, refs 401/416/417, `corridorKlassen unclassified`, `eindToegangPrivaat`, venster 30 km; 8 segmenten, alle snaps ≤ 0,05 km; 14 keerlussen gesnoeid, 471,3 → 468,4 km). b3: het bestaande `goud-guyana-ottawa-lucht-geo-yyz.geojson` (FeatureCollection, 187 punten). Markers: de vier ankers uit §3. Bake: `bash v2/tools/bak_stromen.sh goud-guyana-ottawa`.

**Toelichting.**
- **b2 en b4 zijn stippels** omdat beide vrachtplatforms airside liggen (geen wegpad): het wegbeen eindigt op de rotonde Airport Road (CJIA) resp. begint op de openbare weg W van de Pearson-loodsen (43.6786, -79.6345); de stippel draagt 0,29 resp. 0,08 km. b4 is NIET vervallen: het anker (airside) snapt niet zelf op een weg.
- **b3 vlucht** is doorgetrokken; "aannemelijk: één bron voor de bestemming, geen bron voor de vlucht" staat in de beennaam. Geen tussenlanding aangenomen.
- Geen haven-aanloop, geen zeebeen, geen kopieën; het RCM-anker is letterlijk uit goud-malartic-ottawa hergebruikt (zelfde coördinaat 45.4315, -75.6993).
- **Hwy 416 → 417 loopt door** (open punt uit §7 bevestigd): de 416 verbindt in de scan zonder omweg met de 417 bij Nepean (segment 67,0 km, snaps 0,00).
- Eerste Britannia Road East-km (6,6 km over kleine klassen) liepen via `corridorKlassen unclassified` en lopen netjes door naar de 401.
- `toets_knikken.py`: 38 knikken, 1 omkering (162 gr bij de rotonde Airport Road, echte rotonde), 0 terugloop. `toets_rechte_benen.py --min-km 5`: geen bevinding voor deze stroom. Markers 0,0 km van hun lijn.

**Lessen.** (1) Het weg-slot slot4 bleek bezet (mkdir faalde, maar de scan liep door en gaf het slot vrij): de scan van Guyana (3 s) heeft geen gevolgen gehad, het slot is hersteld. (2) `maak_stroombeen_weg.py` heeft CRLF-regeleinden, `bak_stromen.sh` LF: bij een scripted edit het anker met `\r\n` zoeken. (3) Het RCM-aandeel van de Guyanese export blijft onbewezen (zie §7).
