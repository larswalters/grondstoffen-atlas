# Routebrief (licht) · Koper · Asarel-Medet → II-37 → Aurubis Pirdop (Bulgarije)

**stroom-id:** `koper-asarel-pirdop` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** koperconcentraat (ca. 25% Cu) van de Asarel-Medet-concentrator bij Panagyurishte gaat per **truck** over de private Asarel-mijnweg, de II-37 en de I-6 naar de **Aurubis-smelter en -raffinaderij in Pirdop** (grootste smelter van Zuidoost-Europa); één truckbeen, stoppunt bij de smelter. Aannemelijk: één bron voor de relatie, modaliteit en jaar niet gebronnen.
**Welke as van het verhaal:** Balkan, Bulgaars concentraat naar de lokale smelter. Asarel-Medet: ca. 200 kt concentraat met 25% Cu = **ca. 50 kt Cu per jaar** (Wikipedia, peiljaar niet genoemd) [1]; het deel dat naar Pirdop gaat is niet gekwantificeerd ("verkocht wereldwijd, onder meer aan Pirdop"). Pirdop: ca. 300 kt geraffineerd koper per jaar capaciteit [2] (Aurubis zelf: tot 240 kt kathode per jaar [4]).

## 1 · Ketenkaart
Asarel-concentrator `cu-asarel-laad` ──(b1 truck · Asarel-mijnweg → II-37 → I-6 · hemelsbreed 20 km, geen wegkm · wegtest 32,8 km · aannemelijk)──► Aurubis Pirdop `cu-pirdop-smelter` ── stoppunt (anodes naar Olen alleen als 2005-bron, geen modaliteit)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-asarel-laad` → `cu-pirdop-smelter` | Asarel-mijnweg (OSM way 178849344, tertiary, access=private) → II-37 (Panagyurski kolonii → Zlatitsa) → I-6 (Zlatitsa → Pirdop) [9][10] | hemelsbreed 20 km, geen wegkm; Wikipedia noemt "ca. 25 km" Panagyurishte → Pirdop, geen wegkm [1]. Indicatie: OSRM 31,8 km (toets [13]); wegtest 32,8 km (+2,6%, geen bron, dus indicatie) | maak_stroombeen_weg (profiel `koper-asarel-pirdop-asarel-pirdop`, extract bulgarije) | nee |

Geen zeebeen, geen haven-aanloop, geen last-mile-been: beide ankers liggen op de site; plant → weg 0,08 km, weg → smelter 0,01 km. De openbare route zonder de private mijnweg gaat via Panagyurishte en is 47 km (niet getekend).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-asarel-laad` | mijn / laadplek concentraat | Asarel-Medet, verwerkingsfabriek (11 km NW van Panagyurishte) | 42.5419, 24.1517 | Wikipedia [1]; OSM-relatie 1322295 geeft 42.5519, 24.0993 midden in het tailingsbekken en is dus fout [11] | **bron-gelegd** (z14/z15 gezien: gebouwencluster van de fabriek met flotatiehallen, de grote Asarel-dagbouw direct west ervan, slingerende mijnweg naar het noorden) [12] |
| `cu-pirdop-smelter` | smelter / losplek | Aurubis Bulgaria, smelter en raffinaderij, Industrial Zone, 2070 Pirdop | 42.7200, 24.1590 | haalbaarheidstoets [13]; OSM-landuse way 94761524 (bbox 42.7105–42.7219, 24.1532–24.1760; centroïde 42.7170, 24.1643, 0,5 km ZO, zelfde complex) [11]; adres [3] | **bron-gelegd** (z14/z15 gezien: smeltercomplex met hallen, schoorsteenschaduw (325 m, [2]), stapel bij het kruis, slakken- en bezinkbekken oost) [12] |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Eerste en laatste punt van het profiel zijn de ankers. Alle snaps 0,00–0,08 km.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Asarel-mijnweg, Sredna Gora-flank | 42.5819, 24.1629 | pint de private mijnweg naar het noorden tegen de openbare weg via Panagyurishte (+15 km); de mijnweg staat in OSM als `access=private` en wordt met `eindToegangPrivaat` toegelaten [10] |
| b1 | 2 | II-37 NW van de aansluiting van de mijnweg | 42.6258, 24.1654 | op de doorgaande II-37 (ref 37) richting Zlatitsa, ná de aansluiting van de mijnweg; houdt de lijn op de hoofdweg [9] |
| b1 | 3 | II-37 ten zuiden van Zlatitsa | 42.6875, 24.1298 | pint II-37 → I-6 tegen de snelle sluiproute door de woonstraten van Pirdop (unclassified/residential, vrijwel even lang, 31,9 km) [9] |
| b1 | 4 | I-6 tussen Zlatitsa en Pirdop | 42.7087, 24.1457 | op de I-6 (ref 6) zuid van het complex; pint de aanrit naar de smelter vanaf de hoofdweg [2] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Asarel-concentrator | Asarel-Medet AD | erts → koperconcentraat 25% Cu (ook molybdeen, goud, zilver); eindproducten concentraat en kathode | 13 Mt erts/j, ca. 200 kt concentraat/j (ca. 50 kt Cu) | [1][7] |
| Aurubis Bulgaria, Pirdop | Aurubis AG | concentraten → anodes (>99,5%) en kathode (>99,95%), zwavelzuur | concentraten tot 1.529.745 t/j; kathoderaffinage tot 240 kt/j (Aurubis, 2026); ca. 300 kt kathode/j en 830 kt zuur (Wikipedia) | [2][4] |

## 6 · Stoppunt
De brief stopt bij de smelter van Pirdop: dat is de enige in een bron benoemde afnemer van dit concentraat [1]. Fase D vervalt: wel noemt een 2005-bron dat ongeveer de helft van de anodes naar Olen (België) ging [8], maar zonder modaliteit en zonder actueel jaar tekenen we dat niet; fase E vervalt.

## 7 · Open punten
- **Modaliteit niet gebronnen:** Wikipedia zegt alleen dat concentraat "onder meer aan Pirdop" wordt verkocht [1]. Aurubis noemt 2026 wel twee vrachtwagenweegbruggen aan de centrale ingang (ca. 200 vrachtwagens per dag, alle goederen) en een robotbemonstering voor "ontvangen concentraten" [4]; dat maakt truck aannemelijk, maar bewijst Asarel niet.
- **Private mijnweg:** de directe weg (9 km tussen plant en II-37, OSM `access=private`) is een aanname dat het eigen bedrijfsvervoer deze gebruikt; zonder die weg is de route 47 km via Panagyurishte.
- **Jaartal en aandeel:** 200 kt concentraat/j zonder peiljaar [1]; het deel naar Pirdop onbekend. Aurubis-CEO Trean (2012): Aurubis Bulgaria koopt al het beschikbare lokale concentraat (Elatsite en Asarel), samenvatting uit een zoekresultaat, pagina gaf 403 en is niet zelf gelezen [5]; 2018: lokale productie dekt ca. een derde van de capaciteit [6].
- **Capaciteit Pirdop:** 300 kt [2] tegen 240 kt kathode [4] (en 240 kt anode + 60 kt kathode in 2005 [8]): bronnen verschillen, de brief gebruikt geen enkel getal als stroomvolume.
- **Geen wegkm gepubliceerd:** hemelsbreed 20 km; de ±15%-toets is een indicatie (wegtest 32,8 km, OSRM 31,8 km).
- **Anode naar Olen (België):** alleen in een 2005-bron [8]; geen modaliteit, geen actueel jaar: niet getekend.

## 8 · Bronnen
[1] Wikipedia, Asarel Medet (13 Mt erts, ca. 200 kt concentraat 25% Cu, verkocht onder meer aan Pirdop, 42.5419 N 24.1517 E), https://en.wikipedia.org/wiki/Asarel_Medet
[2] Wikipedia, Pirdop (smelter en raffinaderij, ca. 300 kt, 830 kt zuur, schoorsteen 325 m, I-6), https://en.wikipedia.org/wiki/Pirdop
[3] Aurubis, Sites (Aurubis Bulgaria, Industrial Zone, 2070 Pirdop; anodes, kathodes, zwavelzuur), https://www.aurubis.com/en/about-us/group/sites
[4] Aurubis Bulgaria AD, investeringsvoorstel (kennisgeving aan RIOSV-Sofia), 2026-01-26 (concentraten tot 1.529.745 t/j, kathoderaffinage tot 240 kt/j, weegbruggen ca. 200 vrachtwagens/dag), https://www.aurubis.com/dam/jcr:7c90b175-1027-4c14-b22d-8e6c151b3421/20250126_UIP_Avtokantar_3.2026-01-26-09-43-36.pdf
[5] Capital.bg, interview Nikola Trean, 2012-03-30 (zoekresultaatsamenvatting; pagina 403), https://www.capital.bg/politika_i_ikonomika/bulgaria/2012/03/30/1798725_nikola_trean_poskupvaneto_na_energiiata_ubiva/
[6] Capital.bg, "Aurubis po patya kam rekordnite prihodi", 2018-11-02 (zoekresultaatsamenvatting), https://www.capital.bg/biznes/kompanii/2018/11/02/3338204_aurubis_po_putia_kum_rekordnite_prihodi/
[7] Wikipedia (bg), Asarel-Medet (eindproducten concentraat en kathode; verkoop 2023 ca. 800 mln lv), https://bg.wikipedia.org/wiki/Асарел-Медет
[8] Wikipedia (bg), Aurubis Bulgaria (2005: 240 kt anode, 60 kt kathode, ca. helft van de anodes naar Olen; tussen Pirdop en Zlatitsa), https://bg.wikipedia.org/wiki/Аурубис_България
[9] Wikipedia, Panagyurishte (II-37, Panagyurski kolonii 15 km noordwaarts), https://en.wikipedia.org/wiki/Panagyurishte
[10] OpenStreetMap API, way 178849344 (tertiary, access=private, 182 knopen, bewerkt 2026-10-04), https://api.openstreetmap.org/api/0.6/way/178849344.json
[11] OpenStreetMap/Nominatim, relatie 1322295 Asarel-Medet (42.5518751, 24.0992890, fout in tailings) en way 94761524 Aurubis Bulgaria (42.7170111, 24.1643466), https://nominatim.openstreetmap.org/
[12] Satellietblik `v2/tools/sat_check.py`, Esri World Imagery z14 en z15, 2026-10-31: `sat-koper-asarel-pirdop-cu-asarel-laad.png`, `…-laad15.png`, `sat-koper-asarel-pirdop-cu-pirdop-smelter.png`, `…-smelter15.png` in `v2/build-cache/satcheck/`
[13] Haalbaarheidstoets `koper-asarel-pirdop` (2026-10-31): OSRM Asarel → Pirdop 31,8 km, aanpassing anker Pirdop 42.7200, 24.1590 (z14 bron-gelegd)
[14] Asarel-Medet, bedrijfssite (alleen bedrijfsbeschrijving; Engelse versie in opbouw), https://www.asarel.com/bg

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Uitvoer:** `v2/data/stroomroute-koper-asarel-pirdop.json` (16,6 KB, contract versie 2, lonlat) · 1 been · 32,9 km · 816 punten · 2 markers · geen stippel, geen naad (één been).

| # | modaliteit | km gemeten | km bron | afwijking | naam |
|---|---|---|---|---|---|
| b1 | truck | 32,9 | geen wegkm (hemelsbreed 20 km; OSRM 31,8 km, wegtest 32,8 km) | +3,5% t.o.v. OSRM, indicatie, geen norm | concentraat Asarel-Medet via private mijnweg, II-37 en I-6 naar Aurubis Pirdop (aannemelijk: één bron) |

**Recept:** `bash v2/tools/bak_stromen.sh koper-asarel-pirdop` (functie `bak_koper_asarel_pirdop`). b1 = vooraf gescande weg: `python v2/tools/wegscan_puur.py --profiel koper-asarel-pirdop-asarel-pirdop` (extract bulgarije, refs 37 en 6, `eindToegangPrivaat`, vensterKm 40) naar `koper-asarel-pirdop-weg-asarel-pirdop.geojson`, als `--been-geojson truck`. Markers: cu-asarel-laad 42.5419,24.1517 en cu-pirdop-smelter 42.7200,24.1590 (beide 0,0 km van de lijn).

**Toelichting:** geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen kopie. Snaps van de wegscan 0,00-0,08 km. De private mijnweg (OSM `access=private`) is een aanname dat bedrijfsvervoer hem gebruikt; zonder hem 47 km via Panagyurishte. Toets: json.load ok, versie 2, punt_formaat lonlat, modaliteit truck, 816 punten. `toets_knikken.py`: 16 knikken >= 60 graden, 0 omkeringen, 0 terugloop (spikes van enkele meters op de serpentijnen van de mijnweg en een paar bochten bij de smelter, geen repareerbare lus). `toets_rechte_benen.py`: been niet genoemd (niet recht).

**Lessen:** (1) een been zonder gepubliceerde wegkm krijgt in de beennaam letterlijk de hemelsbreedte, de OSRM-indicatie staat in deze brief; (2) het profiel en de scan stonden al klaar uit de briefronde, dus bakken was één functie plus één run; (3) de OSM-relatie van Asarel ligt in het tailingsbekken, het Wikipedia-coordinaat is het anker; (4) bash -n op bak_stromen.sh kan kort falen door een gelijktijdige edit van een andere agent, lees opnieuw en herhaal.
