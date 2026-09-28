# Routebrief (licht) · diamant — Mumbai → New York (land)

**stroom-id:** `diamant-mumbai-newyork` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** gepolijste diamant van de Bharat Diamond Bourse (Bandra-Kurla Complex, Mumbai) gaat per truck naar het Sahar/CSMIA-vrachtcomplex, vliegt als vrachtvlucht (grootcirkel) naar de vrachtterminal van JFK Airport, en gaat per truck naar de 47th Street Diamond Exchange in Manhattan — de grootste eindmarkt-arc van de hele kaart (VS-verlovingsringmarkt, ~50% wereldvraag).
**Welke as van het verhaal:** *India → VS: de grootste polished-eindstroom* — ~18 Mct/j gepolijste diamant [design/diamant.md §4d], mode air (gepolijste steen reist standaard per beveiligde luchtvracht, nooit per zee). Risico: de VS-verlovingsringmarkt is het front van de lab-grown-ontwrichting — dalende natuurlijke-diamantprijzen sinds ~2022 ondergraven het volume van juist déze as structureel, los van elk logistiek risico [ontwerp].

## 1 · Ketenkaart
```
Bharat Diamond Bourse `dia-bdb` ──(b1 truck · BKC-connector/Airport Road · ~3,9 km hemelsbreed)──►
Sahar/CSMIA Air Cargo Complex (BOM) `dia-bom-cargo` ──(b2 lucht · vlucht BOM → JFK, grootcirkel · ~12.530 km)──►
JFK South Cargo Area (JFK) `dia-jfk-cargo` ──(b3 truck · Van Wyck Expwy → Kew Gardens Interchange → Queens-Midtown Tunnel · ~19,2 km hemelsbreed)──►
47th Street Diamond Exchange, Manhattan `dia-ny-47th` ── stoppunt
```
`dia-bdb` en `dia-bom-cargo` zijn de bestaande Mumbai-ankers uit `diamant-mirny-mumbai.md` (deze golf) — hergebruikt, niet opnieuw gelegd.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Bharat Diamond Bourse (BKC) → Sahar/CSMIA Air Cargo Complex | Airport Road / Western Express Highway-connector, binnen Mumbai (<15 km, geen corridorkeuze) | ~10 [ontwerp]; hemelsbreed 3,9 (berekend) | maak_stroombeen_weg | nee |
| b2 | B | lucht | Sahar/CSMIA Air Cargo Complex (BOM) → JFK South Cargo Area (JFK) | vlucht BOM → JFK, grootcirkel | 12.530,2 (berekend, grootcirkel); ontwerp ~12.600 | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | JFK South Cargo Area → 47th Street Diamond Exchange, Manhattan | Van Wyck Expressway (I-678) → Kew Gardens Interchange → Long Island Expressway → Queens-Midtown Tunnel → Manhattan | ~25 [ontwerp]; hemelsbreed 19,2 (berekend) | maak_stroombeen_weg | nee |

BDB verzorgt zelf dagelijks beveiligd transport van de Diamond Plaza Custom Clearance Centre (DPCCC, in de bourse) naar het Sahar Air Cargo Complex [11] — dat bevestigt b1 als een reguliere, dagelijkse beveiligde truckrit en geen ad-hoc rit.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-bdb` | beursgebouw / vertrekpunt | Bharat Diamond Bourse, G Block, Bandra-Kurla Complex, Mumbai | 19.0641, 72.8646 | [10][11] (hergebruikt uit `diamant-mirny-mumbai.md`) | bron-gelegd (hergebruikt anker, deze golf al satelliet-gelegd) |
| `dia-bom-cargo` | vrachtterminal / vertrek luchtvracht | Sahar / CSMIA Air Cargo Complex, Mumbai | 19.0994, 72.8673 | [9][11] (hergebruikt uit `diamant-mirny-mumbai.md`) | bron-gelegd (hergebruikt anker, deze golf al satelliet-gelegd) |
| `dia-jfk-cargo` | vrachtterminal / aankomst luchtvracht | JFK South Cargo Area (Cargo Plaza/South Cargo Road), Queens, New York | 40.6587, -73.7952 | [1][7] | bron-gelegd (z16 gezien: rij vrachtloodsen/hangaars langs een taxibaan met meerdere geparkeerde wide-body vrachttoestellen op het apron, direct aan South Cargo Road/Cargo Plaza — de zuidelijke vrachtzone van JFK) |
| `dia-ny-47th` | beurs-/handelsgebouw / eindpunt | 47th Street Diamond Exchange, 1196 Avenue of the Americas, Diamond District, Manhattan | 40.7578, -73.9817 | [2][6][8] | bron-gelegd (z15 gezien: dicht stedelijk bouwblok in de Diamond District op West 47th Street tussen 5th en 6th Avenue, geen eigen terrein te onderscheiden — typisch voor een handelsdistrict) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Van Wyck Expressway, nabij JFK | 40.6504, -73.8051 | de corridor verlaat de vrachtzone hier op de enige doorgaande snelweg noordwaarts naar Manhattan (OSM way) |
| b3 | 2 | Van Wyck Expressway, ter hoogte van Kew Gardens | 40.7033, -73.8166 | doorgaand stuk Van Wyck vóór de knoop met Grand Central Parkway/LIE (OSM way) |
| b3 | 3 | Kew Gardens Interchange | 40.7165, -73.8279 | de vaste knoop waar Van Wyck Expwy overgaat in Long Island Expressway richting de Queens-Midtown Tunnel (OSM-POI) |
| b3 | 4 | Queens-Midtown Tunnel, Queens-portaal (Long Island City) | 40.7418, -73.9522 | enige zinnige tunnelcorridor van Queens naar Midtown Manhattan voor vrachtverkeer (OSM way) |
| b3 | 5 | Queens-Midtown Tunnel, Manhattan-portaal (Tudor City) | 40.7463, -73.9719 | uitgang van de tunnel, vanwaar de corridor het Manhattan-stratenpatroon naar 47th Street ingaat (OSM way) |

b1 heeft geen via-punten: een stadsverbinding <4 km binnen Mumbai zonder aanwijsbare corridorkeuze (zelfde patroon als b1/b4 in `diamant-mirny-mumbai.md`); de weg-tool routeert zelf over het lokale net.

## 5 · Verwerkingsknopen
*(geen — deze keten kent geen smelter/raffinaderij/slijperij. Het slijpen/polijsten (~90-95% van de wereld in Surat, ~230 km zuidelijk van Mumbai) valt buiten deze keten: de Bharat Diamond Bourse is een beurs-/exportgebouw voor reeds gepolijste steen, en de 47th Street Diamond Exchange is een handelsgebouw, geen bewerkingslocatie.)*

## 6 · Stoppunt
De brief stopt bij de 47th Street Diamond Exchange: dat is precies het eindpunt uit het ketenontwerp (VS-verlovingsringmarkt-front) en de haalbaarheidstoets meldt "geen aanpassing" voor beide uiteinden — geen bron koppelt déze specifieke stroom aan een vervolgbestemming (bv. een individuele juwelier of retailketen); fase D vervalt.

## 7 · Open punten
- **Geen gepubliceerde vluchtlengte gevonden**: BOM→JFK is een berekende grootcirkel (12.530,2 km); er bestaat geen gekarteerd luchtwegennet en de werkelijke vluchtroute (met eventuele tussenlanding bij bv. Europa) kan langer zijn. Geen bron noemt een tussenlanding voor déze specifieke stroom → één directe vlucht aangenomen, zoals de bakhandleiding voorschrijft.
- **Aandeel van déze specifieke as (Mumbai→New York) binnen het totale ~18 Mct/j India→VS-volume niet apart gebrond** — het cijfer uit `design/diamant.md` §4d is de totale India→VS-arc, niet per vertrek-/aankomstluchthaven uitgesplitst (BDB/Mumbai verwerkt wel 98% van de Indiase diamantexport [11], dus het aandeel via Mumbai is zeer aannemelijk dominant).
- **JFK-vrachtgebouw op zone-niveau gelegd, niet op het specifieke pand van een beveiligde koerier** (bv. Malca-Amit/Brink's): de South Cargo Area is satelliet-bevestigd als vrachtzone met geparkeerde vrachttoestellen, maar welk pand specifiek diamant afhandelt is niet gebrond binnen het webbudget.
- **b3-via-punten zijn OSM-corridorpunten, niet zelf satelliet-gelegd** (geen overslag, geen ander bewijs nodig dan de doorgaande snelweg/tunnelcorridor); Van Wyck Expwy → Kew Gardens → Queens-Midtown Tunnel is de enige zinnige route van JFK naar Midtown Manhattan, dus het risico op een verkeerd wegprofiel is laag.
- **Lab-grown-ontwrichting is een risico voor het VOLUME van deze as, niet voor de route zelf** (zie boven) — buiten scope van deze lichte brief, wel genoemd in de "welke as"-tekst zoals het ontwerp vraagt.

## 8 · Bronnen
[1] Wikipedia — "John F. Kennedy International Airport" (IATA: JFK; 40.63972/-73.77889; Queens, New York City). https://en.wikipedia.org/wiki/John_F._Kennedy_International_Airport
[2] Wikipedia — "Diamond District, Manhattan" (West 47th Street tussen 5th en 6th Avenue). https://en.wikipedia.org/wiki/Diamond_District,_Manhattan
[3] design/diamant.md §4d (project-brief, intern) — "India → VS: de grootste eindstroom (~50% van de wereldvraag)", 18 Mct/j, mode air; gepolijste diamant reist standaard per beveiligde luchtvracht, nooit per zee.
[4] Ketenontwerp (JSON, golf 3) — `diamant-mumbai-newyork`, prioriteit 11, jaarvolume ~18 Mct/j gepolijst.
[5] Haalbaarheidstoets (JSON, golf 3) — `diamant-mumbai-newyork`: haalbaar, geen aanpassing, beide uiteinden hebben al het juiste laatste-been-patroon.
[6] OpenStreetMap (ODbL) via Photon — landuse-polygoon "Diamond District", centroïde 40.75737/-73.98026; "47th Street Diamond Exchange" (amenity=marketplace, 1196 Avenue of the Americas), 40.75785/-73.98166. https://www.openstreetmap.org
[7] OpenStreetMap (ODbL) via Photon — bus-stop-knopen "Cargo Plaza & Central Cargo Road" (40.65875/-73.79520), "South Cargo Road & Cargo Plaza"; kantoren "British Airways Cargo"/"Iberia Cargo"/"WFS Cargo"/"Nippon Cargo Airlines" op JFK Access Road, South Cargo Area. https://www.openstreetmap.org
[8] OpenStreetMap (ODbL) via Photon — via-punten Van Wyck Expressway (40.65045/-73.80509 · 40.70335/-73.81664), Kew Gardens Interchange (40.71652/-73.82794), Queens-Midtown Tunnel Queens-portaal (40.74185/-73.95221) en Manhattan-portaal (40.74625/-73.97187). https://www.openstreetmap.org
[9] `diamant-mirny-mumbai.md` (deze golf, M31 golf 3) — anker `dia-bom-cargo` (CSMIA Air Cargo Complex, Sahar, Mumbai), satelliet-gelegd op z15.
[10] `diamant-mirny-mumbai.md` (deze golf, M31 golf 3) — anker `dia-bdb` (Bharat Diamond Bourse, G Block, BKC), satelliet-gelegd op z15.
[11] BDB India (Bharat Diamond Bourse), "About Us" — BDB handelt 98% van de Indiase diamantexport; alle export via de Precious Cargo Customs Clearance Centre (PCCCC) in de bourse; BDB onderhoudt een sterke kamer bij zowel de Diamond Plaza Custom Clearance Centre (DPCCC) als het Sahar International Air-Cargo Complex, en verzorgt dagelijks beveiligd transport tussen beide. https://bdbindia.org/about/
[12] GJEPC (Gem & Jewellery Export Promotion Council, India) — India Diamond Week wordt gehouden bij de Diamond Dealers Club, 50 W 47th St, New York; ~30% van de Indiase edelsteen-/sieradenexport gaat naar de VS, ruwweg de helft daarvan in gepolijste diamant. https://gjepc.org/india-diamond-week.php
[13] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16, live) — `v2/build-cache/satcheck/sat-diamant-mumbai-newyork-jfk-cargo.png`, `-jfk-cargo-z16.png`, `-47th-street.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `diamant-mumbai-newyork` · **bestand:** `v2/data/stroomroute-diamant-mumbai-newyork.json` (31,9 KB) ·
**recept:** `bak_diamant_mumbai_newyork()` in `v2/tools/bak_stromen.sh` · **profielen:**
`diamant-mumbai-newyork-bdb-bomcargo` en `diamant-mumbai-newyork-jfk-47th` in `v2/tools/maak_stroombeen_weg.py`
(`PROFIELEN`) · **draai:** `bash v2/tools/bak_stromen.sh diamant-mumbai-newyork`.

**3 benen · 12.563,9 km · 1.536 punten · 4 markers · 0 naden.**

| # | modaliteit | km | naad | toelichting |
|---|---|---|---|---|
| b1 | truck | 8,4 | — | Bharat Diamond Bourse → Sahar/CSMIA Air Cargo Complex |
| b2 | lucht | 12.530,2 | 0,00 km | vlucht BOM → JFK, grootcirkel, doorgetrokken |
| b3 | truck | 25,3 | 0,00 km | JFK South Cargo Area → 47th Street Diamond Exchange |

**Luchtbeen (b2):** gebouwd met `maak_luchtbeen.py` volgens bakhandleiding-licht.md §2 "Lucht" — grootcirkel tussen
de twee satelliet-gelegde vrachtterminals `dia-bom-cargo` en `dia-jfk-cargo`, 12.530,2 km, **exact** de
ontwerpschatting uit §2/§8 van deze brief. Geen bron noemt een tussenlanding voor déze specifieke vlucht → één
directe vlucht aangenomen (open punt, zie §7 hierboven). Doorgetrokken, geen stippel: een vlucht tussen twee
gelegde vrachtterminals is geen gat in het net.

**Stippels:** geen. Beide truckbenen zijn volledig doorgetrokken — de anker-verbindingen (plant→weg, weg→kade) zijn
allebei ≤ 0,06 km en liggen op de openbare weg (geen airside/privéterrein-uitzondering nodig).

**Haven-aanlopen:** n.v.t. — geen zeebeen in deze keten.

**Lengtetoets:**
- b1 (truck): 8,4 km tegen het ontwerpcijfer ~10 km (geen gepubliceerde bron, alleen hemelsbreed 3,9 km) = **−16,5%**,
  net buiten de ±15%-norm. Bevinding, niet dichtgetrokken: het ontwerpcijfer was zelf nooit gebrond en de weg volgt
  hier gewoon de lokale straten binnen Bandra-Kurla Complex; er is geen aanwijzing dat de router een verkeerde
  corridor koos.
- b2 (lucht): geen km-toets van toepassing (km = grootcirkel per constructie).
- b3 (truck): 25,3 km tegen ~25 km ontwerp = **+1,3%** [OK]. Alle vijf via-punten snappen ≤ 0,02 km op de doorgaande
  corridor (Van Wyck Expressway → Kew Gardens Interchange → Long Island Expressway → Queens-Midtown Tunnel).

**Markers:** alle vier de ankers (`dia-bdb`, `dia-bom-cargo`, `dia-jfk-cargo`, `dia-ny-47th`) liggen op ≤ 0,1 m van
de lijn (anker = routeerpunt op alle vier de sites).

**Overige toetsen:** `toets_knikken.py` vindt op b1 en b3 alleen kleine-straal spikes (4–39 m) uit de OSM-korrel bij
kruispunten (typisch voor stadswegen), waaronder 2 TERUGLOOP-punten op b3 (Kew Gardens Interchange-omgeving en de
JFK-zijde, radius 4–6 m) — micro-zigzags in het brongeometrie-net, geen route-fout; niet gecorrigeerd binnen de
lichte werkwijze. `toets_rechte_benen.py --min-km 5` geeft geen treffer voor deze stroom (het luchtbeen wordt per
constructie overgeslagen, geen enkel doorgetrokken wegbeen is recht). `json.load` slaagt, `versie` 2,
`punt_formaat` `lonlat`, alle drie modaliteiten (`truck`, `lucht`) geldig, elk been ≥ 2 punten.

**Gereedschapslessen:**
- `maak_luchtbeen.py` reproduceert een reeds gepubliceerde ontwerp-grootcirkelschatting tot op 0,0 km nauwkeurig
  wanneer de ankers exact overeenkomen met de briefankers — een bruikbare stille consistentiecheck vóór het bakken.
- Een korte stads-truckcorridor (<4 km, geen via-punten) kan makkelijk buiten de ±15%-norm vallen zonder dat er iets
  mis is: bij zulke korte afstanden is het verschil tussen "hemelsbreed" en "over straten" procentueel groot, ook al
  is de absolute afwijking klein (1,6 km hier).

**Open punten (ongewijzigd t.o.v. §7):** geen gepubliceerde vluchtlengte voor BOM→JFK (grootcirkel als beste
schatting); aandeel van déze specifieke as binnen het India→VS-totaalvolume niet apart gebrond; JFK-vrachtanker op
zone-niveau, niet op het specifieke koerierspand; b3-via-punten zijn OSM-corridorpunten, niet zelf satelliet-gelegd.
