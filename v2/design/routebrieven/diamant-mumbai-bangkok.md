# Routebrief (licht) · Diamant · Mumbai (BDB) → BOM → Bangkok (BKK) → Bangkok Diamond & Precious Stones Exchange, Jewelry Trade Center (Thailand)

**stroom-id:** `diamant-mumbai-bangkok` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** gepolijste diamant van de Bharat Diamond Bourse (BKC, Mumbai) gaat per truck naar het Sahar/CSMIA-vrachtcomplex (BOM), vliegt als aannemelijke vrachtvlucht (grootcirkel) naar de Free Zone-vrachtterminal van Suvarnabhumi (BKK) en rijdt over Bangkok-Chonburi Motorway en Si Rat Expressway naar het Jewelry Trade Center aan Silom Road, de zetel van de Bangkok Diamond & Precious Stones Exchange (BDPSE; één bron).
**Welke as van het verhaal:** *Zuidoost-Azië: Indiaas gepolijst naar Bangkok.* Geen Mct-cijfer. Thailand importeerde in 2023 voor USD 1,77 mld aan HS 7102 (diamant, ook ruw), waarvan India USD 1,15 mld (65%) op Thailands opgave [1]; de Indiase opgave is USD 512 mln (2,82%) en het verschil is niet verklaard [ontwerp]. Eenheid Mct/j: **volume onbekend**; de waarde per karaat verschilt sterk en is niet gebrond. Risico: Thailand is vooral een kleursteenhub [8] en voert USD 1,33 mld uit, 47% naar Hongkong [1]: Bangkok kan deels doorvoer zijn.

## 1 · Ketenkaart
```
Bharat Diamond Bourse `dia-bdb` ──(b1 truck · BKC-connector/Airport Road · 8,4 km · LETTERLIJKE KOPIE diamant-mumbai-newyork b1)──►
CSMIA Air Cargo Complex `dia-bom-cargo` ──(b2 lucht · vlucht BOM → BKK, grootcirkel · 3.030,4 km · aannemelijk: handelsstroom gebrond, vlucht niet)──►
Suvarnabhumi Free Zone-vrachtterminal `dia-bkk-cargo` ──(b3 truck · Bangkok-Chonburi Motorway → Si Rat Expressway · ~33,5 km gebakken, hemelsbreed 24,9)──►
Jewelry Trade Center / BDPSE, Silom Road `dia-jtc-silom` ── stoppunt
```
`dia-bdb` en `dia-bom-cargo` zijn bestaande ankers (letterlijk uit `diamant-mumbai-shanghai.md`, oorspronkelijk `diamant-mumbai-newyork.md` en `diamant-mirny-mumbai.md`).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | BDB → CSMIA Air Cargo Complex | BKC-connector / Airport Road (kopie `diamant-mumbai-newyork` b1) | 8,4 gebakken in die stroom; hemelsbreed 3,9, geen wegkm | kopie `diamant-mumbai-newyork-weg-bdb-bomcargo.geojson` | nee |
| b2 | B | lucht | BOM-vrachtterminal → BKK-vrachtterminal | vlucht BOM → BKK, grootcirkel (aannemelijk: handelsstroom gebrond, vlucht niet) | 3.030,4 berekend op de twee ankers (ontwerp: ca. 3.030) | maak_luchtbeen | nee, doorgetrokken |
| b3 | C | truck | BKK Free Zone-vrachtterminal → Jewelry Trade Center | Suvarnabhumi-vrachtweg → Rom Klao → Bangkok-Chonburi Motorway (7) → Si Rat Expressway → afrit Silom | hemelsbreed 24,9 km, geen wegkm; OSRM-demo 33,7 (indicatie, geen bron); bake 33,5 | maak_stroombeen_weg (profiel `diamant-mumbai-bangkok-bkk-silom`) | nee |

b1 is het bestaande BDB-transport naar Sahar [7]; b2 is een aanname op de handelsstroom (§7). Geen last-mile-stippel op BKK: het anker ligt landside aan een dienstweg en de bake snapt 0,02 km op het wegnet.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-bdb` | beursgebouw / vertrek | Bharat Diamond Bourse, BKC, Mumbai | 19.0641, 72.8646 | letterlijk uit `diamant-mumbai-shanghai.md` | bron-gelegd (hergebruikt) |
| `dia-bom-cargo` | vrachtterminal / vertrek lucht | CSMIA Air Cargo Complex (Sahar), Mumbai | 19.0994, 72.8673 | letterlijk uit `diamant-mumbai-shanghai.md` | bron-gelegd (hergebruikt; beeld zie die brief) |
| `dia-bkk-cargo` | vrachtterminal / aankomst lucht | Suvarnabhumi Free Zone-vrachtcomplex (BKK) | 13.7049, 100.7499 | [5] OSM-vlak "Free Zone" (way 1254572195) | bron-gelegd (z16 gezien, `…-bkk-freezone.png`: kruis op de landside dienstweg langs de oostgevel van een zeer lang wit vrachtterminalgebouw met platform en toestellen aan de westzijde en pakhuizen aan de oostzijde) |
| `dia-jtc-silom` | afnemer / beurs, stoppunt | Jewelry Trade Center (BDPSE), 919/1 Silom Road, Bang Rak | 13.7228, 100.5200 | [2][5] Wikipedia 13.72278/100.52 en OSM-way 342271323 (13.7228, 100.5201) | bron-gelegd (z15 gezien, `…-jtc-silom.png`: kruis in een dicht hoogbouwblok langs de Si Rat-hoogweg; pand niet individueel te onderscheiden); BDPSE-claim **aannemelijk: één bron [3]** |

Verworpen kandidaten BKK: 13.7105, 100.7585 is het Thai Airways Operations Center (OSM-kantoor, geen vrachtterminal); 13.7051, 100.7568 is een Bangkok Airways-pakhuis (OSM-punt). Het oostelijke complex (z16 `…-bkk-cargo-a.png`, loodsen en een rij vrachttoestellen rond 13.705, 100.759) is een tweede vrachtzone, niet gekozen.

## 4 · Via-punten (alleen b3)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Bangkok-Chonburi Motorway (7) ten westen van Rom Klao | 13.7302, 100.7238 | motorway (7) in plaats van stadswegen (Lat Krabang/Ramkhamhaeng) [7] |
| b3 | 2 | Motorway/Si Rat-corridor bij Hua Mak-Lat Phrao | 13.7403, 100.6466 | houdt de hoofdas aan bij de overgang naar de Si Rat Expressway [7] |
| b3 | 3 | Si Rat Expressway centraal-noord | 13.7535, 100.5761 | expressway in plaats van Rama IV / Phetchaburi [7] |
| b3 | 4 | Si Rat Expressway bij Bang Sue/Chatuchak | 13.7709, 100.5334 | noordelijke boog van de expressway, voor de zuidwaartse afrit [7] |
| b3 | 5 | Si Rat Expressway, afrit richting Silom | 13.7263, 100.5175 | laatste punt op de hoogweg, 0,7 km voor het anker; geen punt in het stadscentrum |

Alle vijf liggen op de doorgaande rijbaan (OSRM-demo-routeknooppunten, bake: snap 0,00-0,01 km). Extracts: `thailand`.

## 5 · Verwerkingsknopen
Geen. De BDPSE is een handels- en beursplek, geen bewerkingsplek; het polijsten valt buiten deze keten.

## 6 · Stoppunt
De brief stopt op het Jewelry Trade Center in Silom: één bron noemt de BDPSE daar [3], geen bron noemt een vervolgbestemming van de stenen (Thailand voert door, o.a. naar Hongkong [1]); fase D en E vervallen.

## 7 · Open punten
- **Diamant-specifiek eindpunt is één bron.** Wikipedia (Jewelry Trade Center) noemt het een juwelen-/edelsteencentrum zonder diamant [2]; alleen het Henry Ho-artikel zegt dat de BDPSE in het JTC zit [3]. Dus aannemelijk; BDPSE zelf staat niet in OSM/Photon (geen eigen coördinaat).
- **Vlucht BOM → BKK niet gebrond.** Geen carrier, vluchtnummer of tussenlanding; alleen de handelsstroom [1] en indirecte aanwijzingen: de eerste vracht die op Suvarnabhumi landde kwam uit Mumbai (Lufthansa Cargo, bij de opening van de luchthaven) [4] en een Thai Airways-vrachtzending met gepolijst (BKK → BOM, 2010) [9]; een koerier met 154,81 ct gepolijst op weg van Surat naar Bangkok werd in december 2025 onderschept [11]. Eén directe vlucht is een aanname.
- **Handelsstroom twee opgaven.** Thailand 1,15 mld (65%) tegen India 512 mln (2,82%), verschil niet verklaard; HS 7102 omvat ook ruwe steen en doorvoer; Thailand is vooral kleursteenhub [8].
- **Geen gepubliceerde wegkm voor b1 en b3.** b3 is 33,5 km gebakken tegen 24,9 hemelsbreed (+34%), de OSRM-demo gaf 33,7: de ±15%-toets is indicatie. b1 is een kopie van een stroom met 8,4 km tegen 3,9 hemelsbreed.
- **BKK-anker is het Free Zone-complex als geheel**, niet een bepaald pakhuis (carrier/handler niet gebrond).
- **Geen jaarvolume in Mct/j.**

## 8 · Bronnen
[1] Trendeconomy, Thailand HS 7102 (invoer 2023 USD 1,77 mld, India 1,15 mld = 65%; uitvoer USD 1,33 mld, Hongkong 47%). https://trendeconomy.com/data/h2/Thailand/7102
[2] Wikipedia, "Jewelry Trade Center" (59 verdiepingen, Silom Road gemstone district, 13.72278 N 100.52 E; noemt geen diamant). https://en.wikipedia.org/wiki/Jewelry_Trade_Center
[3] Wikipedia, "Henry Ho (jeweler)" (BDPSE zit in het JTC). https://en.wikipedia.org/wiki/Henry_Ho_(jeweler)
[4] Wikipedia, "Suvarnabhumi Airport" (eerste aankomst Lufthansa Cargo LH8442 uit Mumbai). https://en.wikipedia.org/wiki/Suvarnabhumi_Airport
[5] OpenStreetMap (ODbL) via Photon: Jewelry Trade Center way 342271323 (13.7227691, 100.5201278); Free Zone Suvarnabhumi way 1254572195 (13.7049, 100.7499); Thai Airways Operations Center way 404295669 (13.7105, 100.7585). https://photon.komoot.io
[6] `diamant-mumbai-shanghai.md` en `diamant-mumbai-newyork.md` (ankers BDB/BOM, b1-kopie, grootcirkelpatroon).
[7] OSRM-demoserver (indicatie, geen bron): BKK-anker → JTC 33,7 km, via Suvarnabhumi Rd 2, Rom Klao, Bangkok-Chonburi 7, Si Rat Expressway, Silom. https://router.project-osrm.org
[8] Rapaport, "Why Bangkok Is the Go-To Spot for Colored Stones". https://rapaport.com/magazine-article/why-bangkok-is-the-go-to-spot-for-colored-stones/
[9] Indian Jeweller, 2010, Thai Airways-vrachtzending (goud en ca. 70 gepolijste diamanten) gestolen op Mumbai-luchthaven, route Bangkok → Mumbai. https://indianjeweller.in/Indian-Jewellery-News/1796/index.php
[10] BDB India, "About Us" (beveiligd transport bourse ↔ Sahar). https://bdbindia.org/about/
[11] IDEX, 2025-12-09, douane Surat Airport onderschept 154,81 ct gepolijst voor een vlucht India → Bangkok. https://idexonline.com/FullArticle?Id=50960
[12] Esri World Imagery via `v2/tools/sat_check.py` (live 2026-11-01): `v2/build-cache/satcheck/sat-diamant-mumbai-bangkok-bkk-freezone.png`, `-bkk-cargo.png`, `-bkk-cargo-a.png`, `-bkk-cargo2.png`, `-jtc-silom.png`.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
Bestand `v2/data/stroomroute-diamant-mumbai-bangkok.json` (16,4 KB, contract versie 2, lonlat), functie `bak_diamant_mumbai_bangkok()` in `v2/tools/bak_stromen.sh` (LF, 0 CRLF). Totaal 3.072,4 km, 749 punten, 4 markers (allemaal 0,0 km van hun lijn). Bak enkele seconden: alle drie de benen waren al vooraf gebakken, geen wegscan in deze run.

| # | modaliteit | been | km | punten | naad |
|---|---|---|---|---|---|
| b1 | truck | BDB naar CSMIA Air Cargo Complex (kopie diamant-mumbai-newyork b1) | 8,4 | 227 | 0 |
| b2 | lucht | vlucht BOM naar BKK (grootcirkel, aannemelijk: handelsstroom gebrond, vlucht niet) | 3.030,4 | 123 | 0,0 |
| b3 | truck | BKK Free Zone-vrachtterminal naar Jewelry Trade Center, Silom (Motorway 7, Si Rat Expressway) | 33,6 | 399 | 0,0 |

**Recept.** b1: `--been-geojson` rechtstreeks op `diamant-mumbai-newyork-weg-bdb-bomcargo.geojson` (letterlijke kopie). b2: `maak_luchtbeen.py` BOM `19.0994,72.8673` naar BKK `13.7049,100.7499` naar `diamant-mumbai-bangkok-lucht-bom-bkk.geojson` (FeatureCollection, 123 punten), doorgetrokken. b3: profiel `diamant-mumbai-bangkok-bkk-silom` (extract thailand, vensterKm 25, 5 via-punten uit §4) via `wegscan_puur.py`, geojson `diamant-mumbai-bangkok-weg-bkk-silom.geojson`, snaps 0,00-0,02 km.

**Toets.** b1 is de lengte van de bronstroom (8,4 km tegen hemelsbreed 3,9, geen wegkm: indicatie). b2 heeft per constructie geen km-toets (3.030,4 km grootcirkel zoals verwacht). b3 33,6 km tegen hemelsbreed 24,9 (+35%) en OSRM-demo 33,7 (indicatie, geen bron): de ±15%-toets is hier geen norm, wel in lijn met de routering. Geen naad boven 0,0 km, geen stippel, geen haven-aanloop, geen airside-stippel (het BKK-anker ligt landside, het wegbeen snapt 0,02 km). `toets_knikken.py`: 21 knikken, alle in b1 (BKC/Sahar-stadsnet) en b3 (eerste en laatste 100 m bij de ankers: 8-34 m straal), 0 omkeringen, 0 terugloop; b2 0 knikken.

**Lessen.** (1) BDPSE-claim blijft één bron en het anker is het JTC-gebouw; de bol toont dus een aannemelijk eindpunt, niet een bevestigd diamantpakhuis. (2) Thailand is deels doorvoer naar Hongkong (brief §1/§7): geen vervolgbeen getekend. (3) Registerregel centraal: sleutel `dia-mb` is bezet, gebruik `dia-mbk`; bestand `stroomroute-diamant-mumbai-bangkok.json`.
