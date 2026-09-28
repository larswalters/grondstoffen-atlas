# Routebrief (licht) · goud — Van → Via → Naar (land)

**stroom-id:** `goud-loulo-ticino` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** doré-goud van het Loulo-Gounkoto-mijncomplex (Barrick, West-Mali) per truck naar de
vrachtterminal van Bamako-Sénou (BKO), per beveiligde vrachtvlucht (grootcirkel) naar de vrachtterminal
van Zürich Airport (ZRH), en per truck over de Gotthard-as naar de Valcambi-raffinaderij in Balerna (Ticino).
**Welke as van het verhaal:** West-Afrika (Mali) → Zwitserland (Ticino) — de Barrick-doré-as. Loulo-Gounkoto
2026-guidance **260.000–290.000 oz** (≈8,1–9,0 t Au, 80%-Barrick-aandeel) [1], fors lager dan de 2023/24-piek
(500–540 koz) door de productiestop tijdens het Mali-conflict; het conflict is sinds eind 2025 geschikt (§7).

## 1 · Ketenkaart
```
Loulo-Gounkoto-mijncomplex `au-loulo-mijn`
  ──(b1 truck · Kéniéba–Kita–Bamako-corridor · ~380–420 km)──►
Bamako-Sénou vrachtterminal (BKO) `au-bamako-vrachtterminal`
  ──(b2 lucht · vlucht BKO → ZRH, grootcirkel, aannemelijk · ~4.180 km hemelsbreed)──►
Zürich Airport vrachtterminal (ZRH) `au-zrh-vrachtterminal` (hergebruikt uit pgm-springs-zurich.md)
  ──(b3 truck · A2/Gotthard-as via Bellinzona–Lugano–Chiasso · ~200 km)──►
Valcambi-raffinaderij, Balerna `au-ref-valcambi` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Loulo-Gounkoto-mijncomplex → Bamako-Sénou vrachtterminal | mijnweg → Kéniéba → Kita → Bamako (kruist de Dakar-Bamako Millennium Highway 6 km N van de Gounkoto-pit) [2][ontwerp] | ≈380 [ontwerp]; hemelsbreed 380,5 [berekend] | maak_stroombeen_weg | nee — doorgaande weg tot de terminal; korte stukjes airside op het vliegveldterrein evt. stippel bij het bakken |
| b2 | B | lucht | Bamako (BKO) → Zürich (ZRH) | vrachtvlucht BKO → ZRH (grootcirkel) | ≈4.180 hemelsbreed [berekend] | maak_luchtbeen | nee — doorgetrokken (aannemelijk: geen bron noemt déze specifieke vlucht; West-Afrikaanse doré-export vliegt structureel naar Zwitserse raffinaderijen, industriestandaard — zie §7 voor de BKO-vs-mijnvliegveld-keuze) |
| b3 | C | truck | Zürich vrachtterminal (ZRH) → Valcambi, Balerna | A2 Gotthard-as via Bellinzona–Lugano–Chiasso | ≈200 [ontwerp]; hemelsbreed 184,1 [berekend] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-loulo-mijn` | mijn / laadplek | Loulo-Gounkoto-mijncomplex, verwerkingsinstallatie (Barrick) | 13.0868, -11.4118 | [2][3][osm] | bron-gelegd (z15 gezien: gebouwencluster + tankpark/indikker direct Z van de Loulo-pit, met een zonnepanelenveld ten ZO — het Barrick-hybride-energiepark bij Loulo; OSM-landuse "Mine d'Or de Loulo" 300 m N) |
| `au-bamako-vrachtterminal` | overslag / lucht | Bamako-Sénou Int'l (BKO), terreincluster W van de startbaan | 12.5353, -7.9488 | [osm] | bron-gelegd, terminalgebouw op pandniveau **onzeker** (z14 gezien: terminal- en loodsencluster direct W van de baan; welk gebouw specifiek vrachtafhandeling doet is op deze resolutie niet te onderscheiden van de naastgelegen (militaire) faciliteiten — zie §7) |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform (hergebruikt uit `pgm-springs-zurich.md`, golf 3) | 47.4647, 8.5492 | [pgm-brief] | bron-gelegd (z14 gezien in de PGM-brief: vrachtplatform met vrachttoestellen naast een rechthoekig loodsgebouw, O van de hoofdterminal) |
| `au-ref-valcambi` | losplek / raffinaderij | Valcambi SA, Via Passeggiata 3, Zona Industriale Pian Faloppia, Balerna | 45.8385, 9.0051 | [4][osm] | bron-gelegd (z15 gezien: industrieel gebouwencomplex met zonnepanelendak, direct N van de spoorbundel Balerna-Chiasso; OSM-building "Valcambi SA" op hetzelfde pand) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kéniéba (RN-verbindingsweg) | -11.2322, 12.8407 | dichtstbijzijnde stad op de Dakar-Bamako-corridor bij het mijncomplex; sluit een zuidelijkere route via Senegal uit |
| b1 | 2 | Kita (corridorknoop) | -9.4890, 13.0408 | de corridor buigt hier oostwaarts naar Bamako; sluit de noordelijkere Kayes-omweg uit |
| b3 | 1 | Bellinzona (A2-Gotthard) | 9.0206, 46.1921 | de A2 passeert hier na de Gotthard-tunnel op weg naar het zuiden |
| b3 | 2 | Lugano (A2-corridor) | 8.9512, 46.0038 | doorgaande A2 tussen Bellinzona en Chiasso |
| b3 | 3 | Chiasso (grens, A2/A2-aansluiting Balerna) | 9.0290, 45.8355 | laatste punt vóór de afslag naar Balerna/Valcambi, sluit een andere grensovergang uit |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Valcambi (Balerna) | Valcambi SA (Rajesh Exports) | doré/ruw goud → LBMA-baren | 's werelds grootste goudraffinaderij, cap. ≈ 2.000 t/j (v1-register) | [4][v1] |

## 6 · Stoppunt
De brief stopt bij Valcambi: fase D (afnemer van de geraffineerde baren) is niet gebrond — Valcambi levert aan
een brede, niet-herleidbare afname (kluizen/hubs wereldwijd); geen bron koppelt déze Mali-doré aan één
specifieke vervolgbestemming. Fase E vervalt.

## 7 · Open punten
- **BINDEND VERWERKT (haalbaarheidstoets):** jaarvolume vervangen door de Barrick-guidance 2026
  (260.000–290.000 oz ≈ 8,1–9,0 t Au, 80%-aandeel) [1] i.p.v. het verouderde 2023/24-cijfer (500–540 koz).
- **BINDEND VERWERKT (haalbaarheidstoets):** het Mali-Barrick-conflict is **geschikt**, geen actueel
  blokkerend risico meer — schikking nov 2025 (Barrick betaalt US$ 253 mln aan de staat, aanklachten
  vervallen, beslag en operationele controle terug 18-12-2025 [5]; sommige bronnen noemen een breder
  pakket rond ~US$ 430 mln), 10-jaars mijnvergunning verlengd 13-02-2026 [6], nieuwe CAO met de vakbonden
  21-09-2026, geplande stakingen afgeblazen [7]. Het volume is desondanks **fors lager** dan pre-conflict
  door de productiestop tijdens 2025.
- **BINDEND BESLIST (mijnvliegveld vs. Bamako-Sénou, §2 van de haalbaarheidstoets):** géén bron gevonden
  die een normale doré-exportvlucht rechtstreeks vanaf het Loulo-mijnvliegveld bevestigt. De enige
  gedocumenteerde vluchten vanaf het mijncomplex zijn de **tijdelijke militaire helikopter-beslagvluchten**
  van juli 2025 tijdens het conflict (goud naar een staatsbank in Bamako) [8][9] — dat is geen
  exportroute maar een geschil-episode, inmiddels afgesloten. Gekozen: vertrek via de reguliere
  **Bamako-Sénou vrachtterminal**, bereikt per truck over de bestaande weginfrastructuur. Geen bron
  bevestigt de vlucht BKO→ZRH voor déze specifieke lading; de vliegverbinding blijft daarom "aannemelijk"
  (West-Afrikaanse doré-export naar Zwitserse raffinaderijen is industriestandaard, zie ook de
  `pgm-springs-zurich.md`-brief in dezelfde golf).
- **Bamako-Sénou-terminalanker is site-niveau, niet pand-niveau** — het satellietbeeld op z14 laat een
  gebouwencluster zien direct W van de baan, maar welk pand specifiek de vrachtafhandeling doet (er ligt
  ook een militaire basis vlak N ervan, OSM "Wagner-basis") is niet te onderscheiden op deze resolutie.
- **Via-punten b1 zijn indicatief** (bekende steden op de corridor, niet zelf OSM-wegvertex-geverifieerd
  binnen het webbudget) — de bak-agent routeert over het OSM-wegnet, dus de exacte ligging volgt uit die
  routering; corridor "N24 Kayes-regio" uit het ontwerp is niet bevestigd als de gereden route (Kéniéba–
  Kita lijkt de kortere/directere weg te zijn, consistent met de opgegeven ~380 km).
- **Fase D vervalt bewust** — geen bron koppelt deze specifieke Mali-doré aan een geïdentificeerde
  vervolgbestemming ná Valcambi.

## 8 · Bronnen
[1] Ecofin Agency, 2026 — "Barrick Confirms Gold Production Restart at Mali's Loulo-Gounkoto Mine in 2026": 2026-guidance 260.000–290.000 oz (80%-aandeel). https://www.ecofinagency.com/news-industry/0602-52638-barrick-confirms-gold-production-restart-at-mali-s-loulo-gounkoto-mine-in-2026
[2] Mining Technology, "Loulo-Gounkoto Gold Mine Complex, Mali" — "Dakar to Bamako Millennium highway crosses the Loulo-Gounkoto haul road, 6km north of the Gounkoto pit". https://www.mining-technology.com/projects/loulo-gounkoto-gold-mali/
[3] Barrick Mining Corporation, Operations — Loulo-Gounkoto. https://www.barrick.com/English/operations/loulo-gounkoto/default.aspx
[4] Wikipedia, "Valcambi" — precious-metals refiner, Balerna, Switzerland, onderdeel van Rajesh Exports. https://en.wikipedia.org/wiki/Valcambi
[5] Afronomicslaw, 2026 — "Barrick Mining Corporation v. Republic of Mali: The Loulo–Gounkoto Mining Complex ICSID Dispute Settled": schikking nov 2025, US$ 253 mln, controle terug 18-12-2025. https://www.afronomicslaw.org/category/analysis/barrick-mining-corporation-v-republic-mali-loulo-gounkoto-mining-complex-icsid
[6] Yahoo Finance / Ecofin, 2026 — Barrick-Mali dispute settlement en Loulo-vergunningverlenging (10 jaar, 13-02-2026). https://finance.yahoo.com/news/barrick-mining-tsx-abx-mali-011752200.html
[7] Investing.com (Bloomberg), 2026-09 — "Barrick Mining reaches agreement with Mali unions, planned strikes off". https://www.investing.com/news/stock-market-news/barrick-mining-reaches-agreement-with-mali-unions-planned-strikes-off-4918992
[8] The Globe and Mail, 2025-07 — "Mali has begun flying gold out of Barrick's Loulo-Gounkoto complex by helicopter" (conflict-episode, geen normale exportroute). https://www.theglobeandmail.com/business/article-malis-government-begins-seizing-gold-stocks-at-barrick-site-memo-says/
[9] Mining.com, 2025-07 — "Barrick hit again as Mali helicopters take off with $117M in gold" (idem, conflict-episode). https://www.mining.com/barrick-hit-again-as-mali-helicopters-flee-with-117m-in-gold/
[osm] OpenStreetMap (ODbL) via Photon/Nominatim — Bamako-Sénou-aerodrome -7,948765/12,5353304 · Mine d'Or de Loulo -11,411801/13,0868356 · Gounkoto Gold Mine -11,3910877/12,8746327 · Valcambi SA building 9,0050553/45,8384957 · Kéniéba -11,232153/12,8407105 · Kita -9,4889798/13,0408383 · Bellinzona 9,0205888/46,1920538 · Lugano 8,9512275/46,0038007 · Chiasso 9,0290169/45,8355209. https://www.openstreetmap.org
[pgm-brief] `v2/design/routebrieven/pgm-springs-zurich.md` (M31 golf 3, zelfde sessie) — hergebruikt anker `pgm-zrh-vrachtterminal` (47,4647/8,5492), zelf satelliet-gelegd in die brief.
[v1] `data/goud.js` — au-ref-valcambi capaciteit ≈ 2.000 t/j; World Gold Council/USGS/LBMA/Metals Focus (zie `design/goud.md`).
Satellietblik: `v2/build-cache/satcheck/sat-goud-loulo-ticino-loulomill.png`, `sat-goud-loulo-ticino-gounkoto.png`,
`sat-goud-loulo-ticino-bamakosenou.png`, `sat-goud-loulo-ticino-valcambi.png` (Esri z14–z15, 2026-09-28).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `goud-loulo-ticino` · **bestand:** `v2/data/stroomroute-goud-loulo-ticino.json` (247,9 KB) ·
**recept:** `bak_goud_loulo_ticino()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh goud-loulo-ticino`).

**4 benen · 4.926,0 km · 12.922 punten · 4 markers** — alle DOORGETROKKEN op één na (het korte last-mile-
stukje bij ZRH, zie hieronder):

| # | fase | modaliteit | km | naad met vorig been | stippel? |
|---|---|---|---|---|---|
| b1 | A | truck | 479,9 | — (start) | nee |
| b2 | B | lucht | 4.176,8 | 0,000 km | nee (doorgetrokken; "grootcirkel" in de beennaam) |
| b3 | B/C | truck | 0,9 | 0,000 km | **ja** — ZRH-vrachtplatform last mile |
| b4 | C | truck | 268,4 | 0,000 km | nee |

**Luchtbeen (§2 "Lucht" van de bakhandleiding, letterlijk gevolgd):**
- b2 BKO → ZRH: `maak_luchtbeen.py`, grootcirkel **4.176,8 km** — sluit vrijwel exact aan op de brief-schatting
  (≈4.180 km hemelsbreed). Aannemelijk (geen bron bevestigt déze specifieke lading; West-Afrikaanse doré-export
  naar Zwitserse raffinaderijen is industriestandaard, brief §7); geen tussenlanding gebrond → één directe
  vlucht. Géén km-toets (grootcirkel = de km per definitie); `toets_rechte_benen.py` slaat het terecht over.

**Stippel (b3, ZRH-vrachtplatform last mile):** het `au-zrh-vrachtterminal`-anker zelf (47,4647/8,5492) snapt
op een geïsoleerde airside-apron-way zonder aansluiting op het openbare net — **twee mislukte pogingen** op de
weg-scan gaven "geen wegpad tussen punt 0 en 1", ook mét `eindToegangPrivaat: True`. Exact dezelfde bevinding
als het analoge been in `goud-yanacocha-ticino-valcambi.md` (zelfde ZRH-anker, zelfde golf) — dat profiel gaf
de oplossing: het wegprofiel start op het dichtstbijzijnde punt van het openbare net (47,472087/8,554523), en
de bake sluit het airside-stukje af met een rechte stippel van **0,914 km** ("eigen verbinding, niet
geroutet"). Geen haven-aanloop nodig (geen zeebeen in deze keten).

**Toelichting per truckbeen (haalbaarheidstoets §5/§6 van de bakhandleiding — beide BUITEN de ±15%-norm,
bevindingen, niet dichtgetrokken):**
- b1 (Loulo-mijn → Bamako-Sénou vrachtterminal): profiel `goud-loulo-ticino-loulo-bamako` (extract mali),
  gebakken **479,9 km** tegen het ~380 km-ontwerpcijfer = **+26,2%**. De brief noemt de via-punten Kéniéba/Kita
  zelf als "indicatief, niet OSM-wegvertex-geverifieerd binnen het webbudget" (§7) — het echte OSM-wegnet
  (Kéniéba–Kita–Bamako) loopt kennelijk verder om dan de hemelsbrede via-som suggereert; geen betrouwbare
  alternatieve gepubliceerde wegreferentie om tegen te toetsen.
- b4 (Zürich Airport vrachtplatform → Valcambi, Balerna): profiel `goud-loulo-ticino-zrh-valcambi` (extract
  zwitserland, via A4 Zug–Luzern → A2/Gotthard-as Bellinzona–Lugano–Chiasso), gebakken **268,4 km** tegen het
  ~200 km-ontwerpcijfer = **+34,2%**. De via-punten volgen de A4/A2-Gotthard-as letterlijk (verplichte
  corridor, geen keuzevrijheid); het OSM-wegnet incl. klaverbladlussen bij Zug/Luzern/Bellinzona (110
  keerlussen gesnoeid, 282,3 → 268,4 km) maakt de rit fors langer dan de hemelsbrede schatting. Geen
  betrouwbare alternatieve gepubliceerde wegreferentie.

**Ankers, status ongewijzigd t.o.v. §3:** `au-loulo-mijn` en `au-ref-valcambi` blijven **bron-gelegd**;
`au-bamako-vrachtterminal` blijft **bron-gelegd, pand onzeker** (terreincluster, niet het specifieke
vrachtgebouw); `au-zrh-vrachtterminal` blijft **bron-gelegd (hergebruikt uit pgm-springs-zurich.md)** — de
airside-onbereikbaarheid van dit punt (zie de b3-stippel hierboven) is een wegnet-eigenschap, geen twijfel over
het anker zelf.

**Toets (bakhandleiding §5):**
- Naden tussen alle vier de benen: **0,000 km** (elk been sluit exact aan op het vorige).
- `toets_knikken.py --bestand`: b1 16 spikes (alle <60 m straal, straatniveau-zigzag) · b2 0 knikken (recht per
  constructie) · b4 18 knikken waarvan **2 "omkeringen" ≥150°, beide geclassificeerd als "scherpe bocht, echt"**
  (v-ratio 1,9–2,0, ronde bochten bij een klaverbladlus/afrit) — **0 terugloop** (de enige klasse die
  gerepareerd hoort te worden). Geen reparatie nodig.
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de uitslag (het luchtbeen wordt terecht
  overgeslagen; geen truckbeen heeft omwegfactor 1,000).
- Markers: alle 4 op **0,000 km** van hun lijn (elk marker-anker is het leg-eindpunt zelf).
- `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteiten ⊂ {truck, lucht}, elk been ≥ 2 punten,
  bestand 247,9 KB (ruim onder ~300 KB).

**Gereedschapslessen:**
- Het §2-lucht-recept (`maak_luchtbeen.py` → `--been-geojson "lucht|vlucht <IATA> → <IATA> …"`) werkte zonder
  aanpassing; de berekende grootcirkel-km (4.176,8) kwam vrijwel exact overeen met de brief-schatting
  (≈4.180 km) — goede kruiscontrole. Licht (milliseconden), geen slot nodig.
- **Hetzelfde ZRH-vrachtplatform-anker (47,4647/8,5492) faalt twee keer op rij** op een weg-scan die er
  rechtstreeks vanaf vertrekt — ook met `eindToegangPrivaat: True` en met de A4-verplichte-tussenpunten
  (Zug/Luzern) erbij. Dit is inmiddels de **tweede** keer in dezelfde golf (na `goud-yanacocha-ticino-valcambi`)
  dat dit exacte punt op een geïsoleerde airside-apron-way blijkt te snappen — een structureel kenmerk van dit
  anker, geen incident. **Werkregel voor een volgende bake die dit ZRH-anker gebruikt:** start het wegprofiel
  meteen op het openbare-net-punt (47,472087/8,554523) en voeg de 0,914 km airside-stippel toe in de
  bak-functie, in plaats van de twee mislukte pogingen te herhalen.
- Beide weg-slot-scans liepen na de fix in één poging goed door; geen extracts ontbraken (mali en zwitserland
  stonden al op schijf). De eerste (kortere) weg-scan-poging op mali (zonder `eindToegangPrivaat`) lukte meteen
  goed — dat probleem zat uitsluitend bij het Zwitserse ZRH-anker.
- Gedeelde-bestand-hygiëne: het gedeelde `v2/build-cache/…/scratchpad/slots/`-mechanisme had een cleanup-bug in
  mijn eigen eerste commando's (`rmdir` vóór het verwijderen van het `sinds`-bestand, dus de `rmdir` faalde
  stil en liet een lege, permanent geblokkeerde slot-map achter voor de hele gedeelde pool). Zelf hersteld
  (twee stuk geraakte lege slot-mappen opgeruimd) en de volgorde in latere commando's omgedraaid (`rm sinds`
  vóór `rmdir`) — een risico voor andere parallelle agenten die hetzelfde patroon kopiëren.
