# Routebrief (licht) · goud — Canadian Malartic-mijn (Québec) → Royal Canadian Mint (Ottawa)

**stroom-id:** `goud-malartic-ottawa` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** goudbaren/doré van de Canadian Malartic-mijn (Agnico Eagle, Abitibi-Témiscamingue,
Québec) per **truck** over Route 117 → Route 105 → Autoroute 5, ~480 km zuidwaarts door de Réserve
faunique La Vérendrye en de Outaouais naar de eigen raffinaderij van de Royal Canadian Mint in Ottawa
(320 Sussex Drive) — één binnenlands wegtransport, geen zee-, spoor- of luchtbeen.
**Welke as van het verhaal:** *Canadese binnenlandse raffinage-as* — een van de grootste Canadese
goudmijnen levert rechtstreeks aan de nationale muntslag-/bullion-raffinaderij, zonder tussenkomst van
een Zwitserse of andere buitenlandse raffinaderij. Canadian Malartic produceerde 603.955 oz (≈18,8 t)
goud in 2023 en 655.654 oz (≈20,4 t) in 2024 (Agnico Eagle, jaarverslag FY2024 [2]); de Mint noemt
zichzelf een raffinaderij van "gold from various mines in Canada" en staat sinds 1919 op de LBMA Good
Delivery-lijst [4][6], maar geeft geen gepubliceerd tonnage- of marktaandeelcijfer voor Canadese
mijnproductie specifiek (open punt, §7).

## 1 · Ketenkaart
```
Canadian Malartic-mijn `au-malartic-mijn` ──(b1 truck · Route 117 → Route 105 → Autoroute 5 ·
   ~480 km, 7 via-punten)──► Royal Canadian Mint `au-rcm-ottawa` (320 Sussex Drive, Ottawa)
   ═══ verwerkingsknoop: RCM-raffinaderij (doré/baren → 99,99–99,999% goud, LBMA/COMEX good delivery) ═══
   ── stoppunt (geen bron voor een vervolgzending naar muntslag of exportmarkt per lading)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `au-malartic-mijn` → `au-rcm-ottawa` | Route 117 (Val-d'Or → Réserve La Vérendrye → Grand-Remous) → Route 105 (Kazabazua → Low → Wakefield) → Autoroute 5 (Chelsea/Gatineau) → Macdonald-Cartier Bridge → Sussex Drive | ≈480 [ontwerp-schatting; via-puntensom hemelsbreed 398,0 km, +21% voor bochten is plausibel voor deze route — geen gepubliceerde route-km gevonden, zie §7] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-malartic-mijn` | mijn (laadplek doré/baren) | Canadian Malartic Mine (Agnico Eagle), Malartic, Québec | 48.1176, -78.0942 | [1][2][8] | bron-gelegd (z15 gezien: open pit + tailings/verwerkingsterrein van de mijn; punt ligt op een toegangsweg tussen tailingsbekken en de mijngebouwen aan de NO-rand van het complex, mijngebouwen zichtbaar ~48,131/-78,093) |
| `au-rcm-ottawa` | raffinaderij/muntslag (losplek) | Royal Canadian Mint, 320 Sussex Drive, Ottawa | 45.4315, -75.6993 | [4][5][6][7][8] | bron-gelegd (z15 gezien: gebouwencomplex direct aan de Ottawa-rivier, tegenover de Alexandra Bridge en het National Gallery-terrein; adres 320 Sussex Drive bevestigd door OSM) |

## 4 · Via-punten (b1 — corridorkeuzes op Route 117 → Route 105 → Autoroute 5)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Route 117 bij Louvicourt (oostzijde Val-d'Or) | 48.0657, -77.3779 | de corridor verlaat Malartic oostwaarts richting Val-d'Or en zet zich daar op de doorgaande Route 117 zuidwaarts voort (OSM way, `highway=trunk`) |
| b1 | 2 | Route 117 door de Réserve faunique La Vérendrye | 47.3300, -77.1100 | enige doorgaande weg door het ~13.000 km² reservaat; pint de corridor op het midden van het ~250 km lange rechte trajectdeel tussen Val-d'Or en Grand-Remous |
| b1 | 3 | Grand-Remous — knooppunt Route 117 / Route 105 | 46.6192, -75.9158 | hier eindigt Route 117 zuidwaarts en zet de corridor zich voort op Route 105 richting Maniwaki/Gatineau — de enige corridorsplitsing op deze reis |
| b1 | 4 | Route 105 bij Kazabazua | 45.9074, -76.0226 | pint Route 105 op het rechte stuk tussen Grand-Remous/Maniwaki en Gatineau, op de doorgaande rijbaan (OSM way `highway=primary`) |
| b1 | 5 | Route 105 bij Low | 45.8117, -75.9526 | tweede pin-punt op dezelfde doorgaande Route 105, dichter bij de Autoroute 5-aansluiting |
| b1 | 6 | Wakefield — noordelijk eindpunt Autoroute 5 / aansluiting Route 105 | 45.6400, -75.9293 | hier voegt Route 105 zich bij Autoroute 5 (Exit 28, korte samenloop) — de corridor wisselt van tweebaans regionale weg naar snelweg |
| b1 | 7 | Macdonald-Cartier Bridge (grens Québec/Ontario, Gatineau–Ottawa) | 45.4370, -75.7030 | de enige oeversteek van de Ottawa-rivier op deze route; Autoroute 5 eindigt hier volgens Wikipedia expliciet "at the Ontario-Quebec border on the MacDonald-Cartier Bridge" [10] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Royal Canadian Mint-raffinaderij (Ottawa) | Royal Canadian Mint (Crown corporation) | doré/baren van Canadese mijnen → 99,5 / 99,99 / 99,999% goud (LBMA/COMEX good delivery-baren + grein) | geen gepubliceerd jaarvolume gevonden voor goud specifiek; raffinaderij operationeel sinds 1911, LBMA Good Delivery-lijst sinds 1919 | [4][5][6][7] |

## 6 · Stoppunt
De brief stopt bij de RCM-raffinaderij in Ottawa: dat is zowel het `naar_site` van het ketenontwerp als
de plek waar het goud van doré/baren naar good-delivery-kwaliteit wordt omgezet. Geen bron documenteert
een specifieke vervolgzending (muntslag-halffabricaat, exportbaar of een andere afnemer) per lading, dus
fase D vervalt en fase E is niet van toepassing.

## 7 · Open punten
- **Geen gepubliceerde route-km gevonden** voor Malartic→Ottawa over de weg — de 480 km in het
  ketenontwerp is een schatting; de som van de zeven via-punten hemelsbreed komt op 398,0 km, wat met
  ~21% bochtopslag (plausibel voor een traject met een ~250 km ongebogen rechte reservaat-doorsteek plus
  twee regionale wegen) in dezelfde orde ligt. De bake-toets (±15% t.o.v. de brief-tabel) moet dit
  bevestigen.
- **RCM's aandeel in de Canadese mijnproductie is niet gebrond met een tonnage- of percentagecijfer.**
  De Mint noemt zichzelf een raffinaderij van "gold from various mines in Canada" [4][5] en staat sinds
  1919 op de LBMA Good Delivery-lijst [6], maar geen geraadpleegde bron geeft een concreet jaarvolume of
  marktaandeel voor Canadese mijngoud specifiek — het ontwerp noemt dit zelf al "RCM eigen opgave,
  ≈veelvoud van de eigen muntslag-behoefte", een kwalitatieve, niet-gekwantificeerde claim.
- **Geen bron koppelt Canadian Malartic specifiek aan de RCM-raffinaderij** (géén offtake-vermelding
  gevonden) — de keten steunt op de generieke claim dat de RCM "gold from various mines in Canada"
  raffineert [4][5] plus het feit dat Canadian Malartic een van de grootste Canadese goudmijnen is;
  bevestigd in de haalbaarheidstoets als "haalbaar, geen blokkerende aanpassing".
- **Geen luchtvracht voor dit traject** — bevestigd door de haalbaarheidstoets: truck-only over een
  korte/middellange binnenlandse afstand, consistent met de eigen aanname van het ketenontwerp.
  §2 "Lucht" van de bakhandleiding is hier niet van toepassing.
- **Alternatieve bestemming Detour Lake → RCM** bestaat als plausibele tweede keten voor dezelfde
  raffinaderij (al erkend in het ketenontwerp) — niet getekend, want dit is een aparte keten met een
  andere mijn.
- **Via-punt 2 (Réserve faunique La Vérendrye) is een geschat middenpunt**, geen OSM-wegvertex — het
  reservaat heeft op deze schaal maar één doorgaande weg (Route 117), dus een corridorkeuze in de zin
  van §4 bestaat hier strikt genomen niet; het punt dient alleen om de ~250 km rechte doorsteek te pinnen
  tegen een sluipweg-artefact in de wegscanner.
- **Mijnanker ligt op de toegangsweg tussen tailingsbekken en mijngebouwen**, niet exact op een
  laad-/expeditiepunt van goudbaren — Agnico Eagle publiceert geen exacte locatie van de
  doré-expeditie binnen het mijnterrein; site-niveau volstaat voor de lichte werkwijze.

## 8 · Bronnen
[1] Wikipedia, "Canadian Malartic Mine" — ligging 25 km ten westen van Val-d'Or, Québec; eigendom Agnico Eagle Mines (100% sinds de Yamana-transactie 2023). https://en.wikipedia.org/wiki/Canadian_Malartic_Mine
[2] Agnico Eagle Mines Ltd, Form 40-F FY2024 (SEC-archief) — Canadian Malartic-productie 655.654 oz goud in 2024 (+8,6% t.o.v. 603.955 oz in 2023, door de stijging van Agnico Eagle's aandeel van 50% naar 100% via de Yamana-transactie). https://www.sec.gov/Archives/edgar/data/2809/000110465925017551/aem-20241231xex99d3.htm
[3] Agnico Eagle Mines, corporate site (operaties-overzicht Canadian Malartic Complex, Abitibi-Témiscamingue, Québec). https://www.agnicoeagle.com/
[4] Royal Canadian Mint, "Storage and Refinery" — raffinaderij op locatie sinds 1911, refined "gold from various mines in Canada", refining tot 99,5/99,99/99,999% zuiverheid. https://www.mint.ca/en/storage-and-refinery
[5] Royal Canadian Mint, "Precious Metals Refining" — segregated refining voor goud van diverse Canadese mijnen. https://www.mint.ca/en/storage-and-refinery/precious-metals-refining
[6] Royal Canadian Mint, "Refinery" — LBMA Good Delivery-status sinds 1919, London Bullion Market Association-erkenning voor goud en zilver. https://www.mint.ca/en/storage-and-refinery/refinery
[7] Wikipedia, "Royal Canadian Mint" — Crown corporation, hoofdvestiging Ottawa (320 Sussex Drive), munt- en baarslagproductie, eigen raffinaderij. https://en.wikipedia.org/wiki/Royal_Canadian_Mint
[8] OpenStreetMap (ODbL) via Nominatim — "Mine Canadian Malartic" (quarry-relatie, 48.11762/-78.09416) · "Royal Canadian Mint, 320 Sussex Drive, Ottawa" (office/government, 45.43145/-75.69926). https://www.openstreetmap.org
[9] Wikipedia, "Quebec Route 117" — Trans Canada Highway Northern Route, Montréal → Abitibi-Témiscamingue → Ontario-grens, enige directe route tussen Zuid-Québec en Abitibi-Témiscamingue. https://en.wikipedia.org/wiki/Quebec_Route_117
[10] Wikipedia, "Autoroute 5 (Quebec)" — begint aan de Ontario-Québec-grens op de Macdonald-Cartier Bridge (Ottawa), loopt 33,8 km noordwaarts via Gatineau/Chelsea tot Wakefield waar Route 105 verdergaat. https://en.wikipedia.org/wiki/Autoroute_5_(Quebec)
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-goud-malartic-ottawa-mijn.png`, `sat-goud-malartic-ottawa-mint.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `goud-malartic-ottawa`** → `v2/data/stroomroute-goud-malartic-ottawa.json` — 1 been,
**451,8 km**, 5.459 punten, 2 markers. truck 451,8 km (doorgetrokken, geen stippel). Recept:
`bak_stromen.sh` (functie `bak_goud_malartic_ottawa`). Bestandsgrootte **111,4 KB**.

**b1 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel
`goud-malartic-ottawa-malartic-ottawa`, extract `canada`):** Route 117 → Route 105 → Autoroute 5,
langs alle zeven brief-via-punten in reisvolgorde — **451,8 km over 5.459 punten** (na het snoeien
van 59 keerlussen, ruw 453,1 → 451,6 km wegdeel + 0,08 km ankerstuk plant→weg + 0,05 km
ankerstuk weg→kade). Tegen de ontwerp-schatting van 480 km (brief §2/§7, zelf al aangemerkt als
niet-gepubliceerd) is dat **−5,9%, binnen ±15% [OK]** — al staat die toets tegen een schatting,
geen harde bron. Beide ankers snappen nagenoeg op de lijn (0,08 km mijn, 0,05 km kade); geen
via-punt is bijgeschoven om het getal te halen.

**Geen haven-aanloop, geen leiding, geen spoor, geen lucht:** deze keten heeft geen zeebeen (brief
§7 bevestigt truck-only), dus bakhandleiding §2 "Lucht" en de haven-aanloop-regel zijn hier niet
van toepassing. Alle zeven via-punten en beide ankers liggen op doorgaande wegen (`highway=trunk`/
`primary`) plus kleine-klasse eindstukken (residential/service/tertiary/unclassified) binnen 12 km
van plant en kade — first mile 7,06 km, last mile 0,80 km, beide binnen de norm; geen stippel nodig.

**Toets naden:** enige been (b1), naad 0,000 km per constructie (eerste been van de keten).

**`toets_knikken.py`:** 19 knikken ≥60° over 451,8 km, **alle 19 geclassificeerd als "spike"**
(radius 2–41 m) en **0 omkeringen ≥150°, 0 terugloop**. De spikes clusteren rond de twee ankers
(Malartic-mijnterrein, RCM-terrein in Ottawa) en rond Wakefield/de Route 105–Autoroute 5-aansluiting
— OSM-wegdetail (kruispunten, keerlussen op klein-klasse toegangswegen) op een schaal die de
lengtetoets niet raakt, geen bevinding die aanpassing vraagt.

**`toets_rechte_benen.py --min-km 5`:** deze stroom staat **niet** in de lijst — het truckbeen volgt
een echte, gebogen wegcorridor (geen omwegfactor 1,000), zoals verwacht voor een doorgetrokken been.

**json geldig:** versie 2, punt_formaat lonlat, modaliteit uitsluitend `truck` (binnen de
toegestane set), het ene been heeft 5.459 punten (≥2), bestand 111,4 KB (< ~300 KB-norm).

**Markers:** beide op de been-eindpunten zelf (au-malartic-mijn, au-rcm-ottawa) — 0,0 m van de lijn
(anker = routeerpunt aan beide kanten).

**Gereedschapslessen:**
- De `canada`-extract stond al lokaal (`v2/build-cache/geofabrik/canada-latest.osm.pbf`, 6,4 GB) en
  scande in 190 s tot 36.826 km ruw over 127.620 ways — geen download nodig, en `canada` bleek als
  reus-extract vlot genoeg voor het gewone weg-slot.
- Het brief-risico op een niet-doorlopende weg door de Réserve faunique La Vérendrye bleek ongegrond:
  `corridor_keten()` volgde de enige doorgaande Route 117 zonder sluipweg-artefact, ook over het
  ~250 km rechte reservaat-stuk waarvoor de brief expliciet een gepind midden-via-punt (47,3300/
  −77,1100) had opgenomen — dat via-punt werkte precies als bedoeld (pin tegen een scanner-omweg,
  geen echte corridorkeuze).
- vensterKm 60 (i.p.v. de default 40) was voldoende voor het hele traject, inclusief het lange
  rechte reservaat-deel; een verdere verruiming naar 75 bleek niet nodig.
- WEBBUDGET niet aangesproken deze bak-ronde (geen WebSearch nodig, alleen bestaand gereedschap en
  de al aanwezige extract).
