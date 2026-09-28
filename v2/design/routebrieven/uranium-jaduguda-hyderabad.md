# Routebrief (licht) · uranium — Jaduguda → Hyderabad (India)

**stroom-id:** `uranium-jaduguda-hyderabad` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** Uraanerts/geel-koek van de Jaduguda-mijn (UCIL, Jharkhand) per **truck** zuidwaarts door
Jharkhand–Odisha–Chhattisgarh–Telangana naar de Nuclear Fuel Complex (NFC) bij Kapra/ECIL, Hyderabad — India's
eigen binnenlandse splijtstofroute, **zonder verrijking** (natuurlijk UO2 voor de PHWR-vloot).
**Welke as van het verhaal:** *India als winningsland op de bol — de tweede "geen-verrijking"-uitzondering naast
Canada's CANDU.* Jaduguda levert "tot 25%" van de grondstof voor India's reactoren [1]; NFC Hyderabad heeft een
capaciteit van 250 t UO2/jaar, uitbreiding naar 600 t/jaar gepland [2].

## 1 · Ketenkaart
```
Jaduguda-mijn+molen `u-jaduguda-mine` ──(b1 truck · Jharkhand–Odisha–Chhattisgarh–Telangana ·
   1.339 km OSRM-wegroute)──► ECIL X-Roads-kruising, Kapra, Hyderabad `u-nfc-hyderabad-stop`
   — net-uiteinde bij NFC (exacte fabriekspoort niet gevonden, zie §6/§7)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `u-jaduguda-mine` → `u-nfc-hyderabad-stop` | Jharkhand (West Singhbhum) → Odisha (Deogarh–Bolangir) → Chhattisgarh (Bastar/Jagdalpur) → Telangana (Hanamkonda–Bhongir) → Hyderabad/ECIL, enige doorgaande zuidwaartse hoofdroute | 1.339 [webcheck, OSRM-routering over het reële OSM-wegennet]; Wikipedia noemt indicatief ~1.200 km [1] | maak_stroombeen_weg (extract india) | nee — doorgetrokken hoofdwegen; géén stippel naar NFC zelf (geen tweede coördinaat gevonden, zie §7) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-jaduguda-mine` | mijn / molen (laadplek, geel-koek) | Jaduguda-mijn (UCIL), Purbi Singhbhum, Jharkhand | 22.6533, 86.3466 | [1][sat] | bron-gelegd (z15 gezien: industrieel mijncomplex met een zichtbaar tailings-bekken pal ten westen — Wikipedia-geohack van de mijnpagina zelf, niet het dorp) |
| `u-nfc-hyderabad-stop` | net-uiteinde bij de fabriek (stoppunt, géén poort) | ECIL X-Roads-kruising, Kapra, Hyderabad — ~1 km van NFC's noordpoort | 17.4733, 78.5708 | [4][6][sat] | bron-gelegd (z16 gezien: reële grote wegkruising met meerdere invalswegen; NFC's eigen locatiepagina noemt deze kruising expliciet als de referentie voor de noordpoort [6]) |

## 4 · Via-punten (corridorkeuzes op de doorgaande route, reisvolgorde)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Hat Gamharia-corridor, West Singhbhum, Jharkhand | 22.2267, 85.7356 | eerste doorgaande zuidwaartse routekeuze uit de Jaduguda-regio richting de Odisha-grens |
| b1 | 2 | Deogarh, Odisha | 21.5093, 84.7219 | grote plaatsknoop op de doorgaande binnenlandroute door Noord-Odisha |
| b1 | 3 | Bolangir, Odisha | 20.7050, 83.4864 | pint het binnenlandtracé vast tegenover een mogelijke kustroute via Vizag |
| b1 | 4 | Jagdalpur (Bastar), Chhattisgarh | 19.0708, 82.0573 | staatsgrensovergang Odisha→Chhattisgarh, grote stad op de doorgaande verbinding |
| b1 | 5 | Hanamkonda/Warangal, Telangana | 18.0352, 79.5854 | staatsgrensovergang Chhattisgarh→Telangana, grootste stad op het traject |
| b1 | 6 | Bhongir, Telangana | 17.5113, 78.9003 | laatste doorgaande knoop vóór Hyderabad, waar de route de stad binnenkomt richting ECIL/Kapra |

⚠️ Coördinaten van de zes via-punten zijn punten **op de OSRM-gerouteerde weg zelf** (reëel OSM-wegennet, geen
schatting), elk via Nominatim-reverse-geocoding herkend bij de genoemde plaats (binnen enkele km). Geen los
gepubliceerd bewijs per NH-nummer binnen het webbudget — de wegscan (`maak_stroombeen_weg.py`) bepaalt het
definitieve tracé en kan een vergelijkbare maar niet identieke route kiezen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Jaduguda-mijn+molen | UCIL (Uranium Corporation of India Ltd, DAE) | uraanerts → geel-koek (U3O8) | geen tU/jaar-cijfer gevonden; "tot 25% van India's reactorbrandstof" | [1] |
| Nuclear Fuel Complex, Hyderabad | DAE | geel-koek (U3O8) → natuurlijk UO2-splijtstofbundels (PHWR) | 250 t UO2/jaar (huidig) ≈ ~212 tU/jaar (×0,848); uitbreiding gepland naar 600 t/jaar ≈ ~509 tU/jaar | [2] |

## 6 · Stoppunt
De as bedoelt NFC Hyderabad als eindpunt (splijtstoffabricage, geen verrijking). De **getekende lijn** stopt
echter bij de ECIL X-Roads-kruising: geen enkele geocodingsroute (Wikipedia-infobox, Wikidata, Nominatim,
Photon, Overpass) leverde een site-coördinaat voor NFC zelf op, en NFC's eigen locatiepagina geeft alleen
richting (noordpoort ~1 km van deze kruising, zuidpoort naar Mallapur/HB Colony/Moula-Ali/Tarnaka) — geen adres
of coördinaat. Conform de bindende aanpassing van de haalbaarheidstoets: dit is geen afwijzing van de as, wel
een kortere lijn dan het ontwerp tekent; er wordt geen tweede coördinaat verzonnen, dus geen aparte
last-mile-stippel naar de poort.

## 7 · Open punten
- **NFC Hyderabad heeft geen vindbare site-coördinaat**, opnieuw bevestigd: Wikipedia-pagina "Nuclear Fuel
  Complex" heeft geen `{{coord}}`-infobox [2]; Wikidata Q7067950 draagt geen P625-coördinaatclaim [3];
  Nominatim/Photon geven 0 hits op "Nuclear Fuel Complex Hyderabad" / "Kancha Imarat"; twee Overpass-mirrors
  geven 0 elementen op naam-regex `nuclear|atomic|NFC` en 0 `landuse=industrial`-vlak met een passende naam in
  de ECIL/Kapra-bbox. Enige aanwijzing: een OSM-adrespunt "DAE Colony, Ward 2 Dr A S Rao Nagar, Kapra mandal"
  vlak bij de ECIL X-Roads-kruising [5] — een woonwijk voor DAE-personeel, geen fabrieksanker.
- **Jaduguda-jaarvolume in tU/jaar niet gevonden** — alleen het kwalitatieve "tot 25%" [1]; geen bron met een
  harde ton-opgave binnen budget.
- **Jaduguda's operationele status niet hard bevestigd voor 2024/2025** — de Wikipedia-intro is verouderd
  (spreekt nog van opschorting 2014/herstart 2017) [1]; volgens de meegeleverde haalbaarheidstoets wijst een
  aparte webcheck op een nieuwe ertslaag binnen de bestaande lease (2024) en arbeidsonrust bij UCIL (2025) —
  geen aanwijzing voor sluiting, maar ook geen hard actueel productiecijfer. Status hier: aannemelijk
  operationeel.
- **Afwijking t.o.v. het ontwerp:** het ontwerp noemt de corridor "zuidwaarts door Odisha/Telangana"; de
  gemeten OSRM-route kruist ook **Chhattisgarh** (Bastar/Jagdalpur) — een correctie op basis van echte
  wegrouting, geen tegenspraak van de as.
- **Modaliteit en globale afstand (~1.200 km, truck)** zijn direct bevestigd door de Jaduguda-Wikipedia-pagina
  zelf [1] — geen extra check nodig. De gemeten OSRM-wegkm (1.339 km) wijkt +11,6% af van die indicatieve
  1.200 km; dat is geen bedrijfs-/overheidscijfer voor dit exacte traject, dus de ±15%-toets geldt hier als
  indicatie, niet als norm.
- **Geen zeebeen, geen spoorbeen**: dit is een zuiver binnenlandse truckketen — India's eerste winningsland op
  de bol, en samen met Canada's CANDU de tweede "geen-verrijking"-uitzondering, zoals het ontwerp claimt.

## 8 · Bronnen
[1] Wikipedia, "Jaduguda uranium mine" — coördinaat 22.653273,86.346639 (paginakop, niet het dorp), "up to 25%"
van India's reactorbrandstof, modaliteit truck + "over 1,200 kilometres (750 mi) away" naar NFC Hyderabad.
https://en.wikipedia.org/wiki/Jaduguda_uranium_mine
[2] Wikipedia, "Nuclear Fuel Complex" — opgericht 1971, DAE, 250 t UO2/jaar huidige capaciteit, uitbreiding naar
600 t/jaar gepland, geen coördinaat in de infobox. https://en.wikipedia.org/wiki/Nuclear_Fuel_Complex
[3] Wikidata, item Q7067950 ("Nuclear Fuel Complex") — geen P625-coördinaatclaim aanwezig.
https://www.wikidata.org/wiki/Q7067950
[4] Wikipedia, "ECIL X Roads" — coördinaat 17.47333,78.57083, reële wegkruising, genoemd naar de nabijgelegen
ECIL-fabriek. https://en.wikipedia.org/wiki/ECIL_X_Roads
[5] OpenStreetMap via Nominatim — adrespunt "DAE Colony, Ward 2 Dr A S Rao Nagar, Kapra mandal, Hyderabad,
500062" vlak bij ECIL X-Roads; 0 hits op directe NFC-naamzoekopdrachten. https://nominatim.openstreetmap.org
[6] NFC (Department of Atomic Energy), officiële locatiepagina — noordpoort ~1 km van de ECIL X-Roads-bushalte,
zuidpoort naar Mallapur/HB Colony/Moula-Ali/Tarnaka; geen adres/coördinaat gegeven; toegang strikt op
uitnodiging. https://www.nfc.gov.in/location-and-visit-to-nfc.html
[7] NFC, officiële contactpagina — postadres "ECIL Post Office, Hyderabad – 500 062, Telangana".
https://www.nfc.gov.in/contacts.html
[8] OSRM (Project OSRM demo-server) — real-road routering Jaduguda-mijn → ECIL X-Roads over het OpenStreetMap-
wegennet: 1.339,0 km. http://router.project-osrm.org
[webcheck] Haalbaarheidstoets van dit ontwerp (meegeleverd document, niet apart herbevestigd binnen deze brief):
mijn-coördinaat 22.6533,86.3466 (dezelfde bronsoort als w-cnnc-lanzhou in de sitelaag) + het 2024/2025-webcheck
op Jaduguda's operationele status.
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15–z17) —
`v2/build-cache/satcheck/sat-uranium-jaduguda-hyderabad-jaduguda-mine.png`,
`sat-uranium-jaduguda-hyderabad-ecil-xroads.png`,
`sat-uranium-jaduguda-hyderabad-nfc-wide.png`, `-nfc-z16.png`, `-nfc-candidate.png` (verkenning van het
NFC-gebied, geen anker opgeleverd — zie §7).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Recept:** `bash v2/tools/bak_stromen.sh uranium-jaduguda-hyderabad` (functie `bak_uranium_jaduguda_hyderabad` in
`v2/tools/bak_stromen.sh`); geometrie via `python v2/tools/maak_stroombeen_weg.py --profiel
uranium-jaduguda-hyderabad-jaduguda-hyderabad --bron geofabrik` (profiel in `v2/tools/maak_stroombeen_weg.py`,
extract `india`). Eén rechttoe-rechtaan volledige scan met alle 6 via-punten in één profiel — geen sub-runs
nodig, de scan haalde het in één keer.

**Benen:** 1 — truck, doorgetrokken, **1.295,7 km** / 16.083 punten (`v2/build-cache/ais/graaf/
uranium-jaduguda-hyderabad-weg-jaduguda-hyderabad.geojson`). Geen stippels, geen haven-aanloop, geen leiding/
spoor (zuiver truck, geen zee/spoor in deze keten, conform de brief).

**Markers:** 2 (beide ankers uit §3) — Jaduguda-mijn (UCIL) 22.6533,86.3466 · ECIL X-Roads-kruising, Kapra,
Hyderabad 17.4733,78.5708 (net-uiteinde, GEEN NFC-poort).

**Toets (handleiding §5):**
- Km-toets: 1.295,7 km tegen de gepubliceerde 1.339 km OSRM-wegroute = **−3,2%**, ruim binnen ±15%; ook ruim
  onder Wikipedia's indicatieve "~1.200 km". Beide staan als indicatie, niet als harde norm (brief §7) — de
  wegscan koos zelf een iets ander maar vergelijkbaar tracé over de vier staten.
- Naden: 1 been, dus geen naad te meten (0,00 km per constructie).
- Via-snaps: alle zes 0,00–0,04 km van de gerouteerde weg — geen enkele > 5 km, dus geen wegklasse-correctie
  nodig geweest.
- Markers: beide ankers liggen exact op het eerste/laatste routepunt (0,00 km).
- `toets_knikken.py`: 98 knikken ≥ 60° (kleine OSM-spikes op kruisingen, straal 6–65 m — normaal op een
  wegroute van 1.300 km door vier Indiase staten), waarvan 1 omkering ≥ 150° en **0 terugloop** (de enige
  klasse die gerepareerd hoort te worden). Geen actie nodig.
- `toets_rechte_benen.py --min-km 5`: geen treffer voor deze stroom (geen been met omwegfactor 1,000 — dus
  geen stippel-die-eigenlijk-een-route-is).
- Contract: `versie` 2, `punt_formaat` "lonlat", modaliteit `truck` (geldig), 1 been met 16.083 punten (≥ 2).
- **Bevinding:** bestandsgrootte 311,5 KB, net over de indicatieve "~300 KB" uit de handleiding §5.3 — een
  gevolg van de lengte (1.300+ km, 16.083 punten voor één doorgetrokken wegbeen door vier staten); geen
  actie ondernomen (geen via-punt bijschuiven om een bestandsgrootte-norm te halen, die norm is indicatief).

**Toelichting stippels/aanloop/vlucht/leiding:** geen van toepassing — één doorgetrokken truckbeen, geen zee,
geen spoor, geen leiding, geen lucht.

**Lessen:**
- De zes OSRM/Nominatim-via-punten waren scherp genoeg gelegd (alle snaps ≤ 0,04 km) om de wegscan in één
  keer een geloofwaardig tracé te laten vinden — de voorgestelde sub-runs (Jaduguda→Bolangir enz.) waren niet
  nodig.
- `corridorKlassen: ["tertiary", "unclassified"]` was nodig om ze door de eindKlassen-validatie te krijgen;
  `secondary` hoort niet in `corridorKlassen` omdat het al binnen `WEG_HOUD` (motorway–secondary) valt en dus
  altijd al meedoet — de validatie in `maak_stroombeen_weg.py` (`corridorKlasse … staat niet in eindKlassen`)
  ving die fout meteen af.
- Het net-uiteinde bij NFC (ECIL X-Roads) is bewust de laatste routepunt-anker, geen aparte last-mile-stippel:
  er is geen tweede coördinaat om naartoe te stippelen (brief §6).
