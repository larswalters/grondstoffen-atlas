# Routebrief (licht) · Goud · MKS PAMP (Ticino) → Zürich → Shanghai Pudong → SGE-kluiszone (China)

**stroom-id:** `goud-pamp-shanghai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** LBMA-erkend baar-goud van de MKS PAMP-raffinaderij in Castel San Pietro (Ticino) per
**truck** (A2/Gotthard) naar de vrachtterminal van Zürich Airport (ZRH), per **vrachtvlucht** (grootcirkel)
naar de vrachtterminal van Shanghai Pudong (PVG), en per **truck** binnenstedelijk naar de
Lujiazui-financiële-wijk in Pudong — waar het internationale bord van de Shanghai Gold Exchange (SGE) en zijn
door Bank of Communications beheerde kluis zitten.
**Welke as van het verhaal:** Zwitserland (Ticino-raffinage) → China (SGE-kluizen, grootste netto-importeur
van fysiek goud) — China importeert al jaren overwegend geraffineerd baar-goud per luchtvracht, en de
Zwitserse raffinagesector is de grootste externe leverancier van LBMA-erkend baar-goud aan China (WGC/SGE-
importvergunningendata) [1][2].

## 1 · Ketenkaart
```
MKS PAMP-raffinaderij `au-pamp-raffinaderij`
  ──(b1 truck · A2 Ticino → Zürich, via Gotthard · ~198 km hemelsbreed via de punten)──►
Zürich Airport vrachtterminal `au-zrh-vrachtterminal`
  ──(b2 lucht · vlucht ZRH → PVG, grootcirkel · ~9.032 km)──►
Shanghai Pudong vrachtterminal `au-pvg-vrachtterminal`
  ──(b3 truck · binnenstedelijk Pudong · ~31 km, aannemelijk)──►
SGE-kluiszone Lujiazui (Bank of Communications) `au-sge-kluiszone` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | MKS PAMP → Zürich Airport vrachtterminal | A2 (Mendrisio–Bellinzona–Gotthard–Erstfeld) → A2/A4 (Rotkreuz–Zug–Zürich) | ~200 [ontwerp], ~198 hemelsbreed via de punten | maak_stroombeen_weg | nee |
| b2 | D | lucht | Zürich (ZRH) → Shanghai Pudong (PVG) | vrachtvlucht ZRH → PVG, grootcirkel | ~9.032 (berekend op de twee vrachtterminal-ankers) | maak_luchtbeen | nee — doorgetrokken (bakhandleiding §2) |
| b3 | D | truck | Shanghai Pudong vrachtterminal → SGE-kluiszone Lujiazui | binnenstedelijk (S1/A20-corridor) | ~31 [berekend] tegen ~35 [ontwerp] | maak_stroombeen_weg | nee — doorgetrokken (aannemelijk: kluis-exacte pand niet gepubliceerd, zie §7) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-pamp-raffinaderij` | raffinaderij / vertrekpunt | MKS PAMP SA, succursale Ticino — Via alle Zocche 1, 6874 Castel San Pietro | 45.8546, 9.0025 | [3][4][7] | bron-gelegd (z16–z17 gezien: industrieel complex met proceshallen, dakinstallaties/tanks en een apart gebouw met zonnepanelendak op het adres uit het handelsregister, Tognano-wijk van Castel San Pietro) |
| `au-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform | 47.4647, 8.5492 | [5] | bron-gelegd — hergebruikt van `pgm-springs-zurich` (deze golf): vrachtplatform met vrachttoestellen naast een rechthoekig loodsgebouw, direct O van de hoofdterminal |
| `au-pvg-vrachtterminal` | overslag / lucht | Shanghai Pudong International Airport — vrachtplatform/-loodsen | 31.1335, 121.8025 | [6] | bron-gelegd — hergebruikt van `pgm-rustenburg-shanghai` (deze golf): verhard platform met tientallen geparkeerde wijdrompvrachttoestellen naast lange vrachtloodsen, zuid van de passagiersterminals |
| `au-sge-kluiszone` | losplek / kluis | Lujiazui financiële wijk, Pudong (Yincheng-corridor) — SGE International Board-kantoren + Bank of Communications-hoofdkantoor, exploitant van het SGEI-kluissysteem | 31.2355, 121.5008 | [1][8][9] | **onzeker** (zone-niveau: het SGEI-kluiscomplex zelf, capaciteit 1.000 t, wordt door geen bron met een straatadres genoemd — gangbare geheimhouding bij baar-goudkluizen, ook bij Zürich/Loomis in `pgm-springs-zurich` deze golf; het gebied rond Yincheng Road, waar zowel de SGEI-kantoren als de hoofdkantoortoren van de beherende bank staan, is satelliet-gezien een dichtbebouwde financiële wijk aan de Huangpu-oever) |

## 4 · Via-punten (b1 — corridorkeuze op de doorgaande A2/A4)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Bellinzona (A2-knoop) | 46.1954, 9.0297 | hoofdstad Ticino, A2 loopt er doorheen vóór de Gotthard-klim [7] |
| b1 | 2 | Göschenen (noordportaal Gotthard) | 46.6676, 8.5887 | vaste doorgang: de A2/Gotthard-tunnel heeft geen alternatieve corridor voor vrachtverkeer op dit traject [7] |
| b1 | 3 | Erstfeld (Reuss-dal, Uri) | 46.8215, 8.6500 | A2 volgt hier het Reuss-dal noordwaarts, vóór de knoop bij Lucerne [7] |
| b1 | 4 | Rotkreuz (A2/A4-knoop) | 47.1408, 8.4313 | hier verlaat de route de A2 en buigt via de A4 noordoostwaarts naar Zürich [7] |
| b1 | 5 | Zug (A4-corridor) | 47.1681, 8.5169 | doorgaande A4 tussen Rotkreuz en Zürich, geen zijtak [7] |

b3 heeft geen via-punten: het is één doorgaande stedelijke expressway-corridor (S1/A20-type) tussen luchthaven
en financiële wijk zonder een aanwijsbare corridorkeuze binnen het webbudget van deze sessie — de bak-agent
routeert dit rechtstreeks over het OSM-wegennet.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| MKS PAMP-raffinaderij | MKS PAMP SA | doré/schroot/oud goud → LBMA-erkende baren (999,9) | Zwitserse raffinagesector (4 huizen, incl. PAMP) samen ~65-70% van het wereldgoud [1][2] | [1][2][4] |
| SGEI-kluis (Lujiazui) | Bank of Communications (namens SGE) | ingevoerde baren → vrijgave aan SGE-leden/China-markt | 1.000 t opslagcapaciteit | [8][9] |

## 6 · Stoppunt
De brief stopt bij de SGE-kluiszone: dat is het door het ketenontwerp gegeven eindpunt (China-put — geen
gedocumenteerde vervolgbestemming binnen één bron), en fase E (sieraad-/beleggingsverwerking) is niet met
naam en adres gebrond, dus die vervalt.

## 7 · Open punten
- **Geen straatadres voor de SGEI-kluis** — bullion-kluizen publiceren hun locatie doorgaans niet (zelfde
  reden als de Loomis-kluis Kloten in `pgm-springs-zurich`, deze golf); `au-sge-kluiszone` is een
  **zone-anker** (Lujiazui/Yincheng-corridor), geen pand-anker.
- **Geen route-specifiek jaarvolume** — alleen het nationale China-importcijfer (§8), geen Zwitsers
  aandeel-cijfer voor déze as (bevestigd als bekend gat door de haalbaarheidstoets).
- **Vlucht ZRH→PVG niet apart gebrond** — aangenomen als industriestandaard op de gepubliceerde grootcirkel,
  geen carrier/tussenlanding gevonden → één directe vlucht.
- **b1-viapunten zijn Photon-plaatscentra**, niet zelf OSM-/satellietgeverifieerd; de bake-lengtetoets is de
  echte controle op de A2/Gotthard-corridor.
- **PAMP-satellietbeeld is site-niveau**: het complex op Via alle Zocche 1 heeft meerdere gebouwen; welk
  hal-nummer exact raffinage/gieterij is, is op z17 niet te onderscheiden van bijgebouwen.
- **b3 ~31 km berekend vs. ~35 km ontwerp** — marge tussen hemelsbreed-schatting en echte rijroute, niet blokkerend.

## 8 · Bronnen
[1] Ketenontwerp golf 3 (orkestrator-invoer) — "China is al jaren de grootste netto-importeur van fysiek
goud (WGC/SGE-importvergunningendata) en importeert vrijwel uitsluitend geraffineerd baar-goud per
luchtvracht via de Shanghai Gold Exchange-kluizen; de Zwitserse raffinagesector is de grootste externe
leverancier van LBMA-erkend baar-goud aan China", incl. jaarvolume "SGE-vault-uitgifte + China netto-import
≈ 500–1.000+ t Au/j in piekjaren (WGC China-vraagrapportages, sterk fluctuerend per jaar)".
[2] World Gold Council, Goldhub — "Gold demand by country" (dataportaal, cijfers per land/kwartaal, geen los
site-specifiek cijfer voor déze as). https://www.gold.org/goldhub/data/gold-demand-by-country
[3] Zefix (Eidgenössisches Handelsregisteramt), opzoeking "MKS PAMP" — MKS PAMP SA, succursale Ticino
(CHE-187.174.186), zetel Castel San Pietro, adres Via alle Zocche 1, 6874 Castel San Pietro.
https://www.zefix.ch (REST-opzoeking `firm/search.json` + `firm/1514109.json`)
[4] Wikipedia, "MKS PAMP" — raffinage- en muntbedrijf in Castel San Pietro, Ticino; handelskantoren in
Genève, New York, Hongkong. https://en.wikipedia.org/wiki/MKS_PAMP
[5] Esri World Imagery via `v2/tools/sat_check.py` (z14) — vrachtplatform ZRH, hergebruikt anker uit
`v2/design/routebrieven/pgm-springs-zurich.md` §3 (deze golf, `v2/build-cache/satcheck/sat-pgm-springs-
zurich-zrh-airport.png`).
[6] Esri World Imagery via `v2/tools/sat_check.py` (z16) — vrachtplatform PVG, hergebruikt anker uit
`v2/design/routebrieven/pgm-rustenburg-shanghai.md` §3 (deze golf, `v2/build-cache/satcheck/sat-pgm-
rustenburg-shanghai-pvg-cargo.png`).
[7] OpenStreetMap-geocoding via Photon/Nominatim + Esri World Imagery via `v2/tools/sat_check.py` (z14–z17) —
Castel San Pietro-dorpscentrum en Via alle Zocche (Photon); Bellinzona/Göschenen/Erstfeld/Rotkreuz/Zug
(Photon-plaatscentra); `v2/build-cache/satcheck/sat-goud-pamp-shanghai-pamp-zocche.png`,
`sat-goud-pamp-shanghai-pamp-zocche-zoom.png`.
[8] BullionStar, "Infrastructure of the Shanghai Gold Exchange" + "The Mechanics of the Shanghai
International Gold Exchange" — SGEI-kluis in de Shanghai Pilot Free Trade Zone, beheerd door Bank of
Communications, capaciteit 1.000 t; SGE heeft daarnaast 61-69 gecertificeerde kluizen in 35-37 Chinese
steden. https://www.bullionstar.com/gold-university/infrastructure-shanghai-gold-exchange ·
https://www.bullionstar.com/gold-university/the-mechanics-of-the-shanghai-international-gold-exchange
[9] Shanghai Gold Exchange (SGE), officiële site — hoofdadres 上海市黄浦区中山南路699号 (699 Zhongshan South
Road, Huangpu); SGEI-kantoren in de Bank of China Tower, 200 Yincheng Road Central, Pudong; SGEI-kluis
geëxploiteerd door Bank of Communications (hoofdkantoor 188 Yincheng Middle Road, Pudong) — geen
gepubliceerd kluisadres. https://www.sge.com.cn/

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3 — centraal afgemaakt)

- **Stroom** `goud-pamp-shanghai` · `v2/data/stroomroute-goud-pamp-shanghai.json` (135 KB) · recept `bak_goud_pamp_shanghai` in `v2/tools/bak_stromen.sh`.
- **Benen:** b1 truck 263,3 km (A2 Gotthard → A14 Luzern–Rotkreuz → A4 Knonaueramt → A1 naar Kloten) · b2 stippel 0,9 km (ZRH-vrachtplatform last mile, airside) · b3 lucht ZRH → PVG 9.032,0 km (grootcirkel) · b4 truck PVG → Lujiazui 39,7 km. **Totaal 9.335,9 km**, 4 markers, naden 0.
- **Waarom centraal:** de bak-agent kreeg binnen zijn sessie alleen het luchtbeen en de twee profielen af; de wegscans wachtten op het gedeelde slot. Afgemaakt door de orkestrator.
- **Twee profielcorrecties:** (1) het ZRH-vrachtplatform ligt airside ("geen wegpad tussen punt 5 en 6", dezelfde bevinding als `goud-loulo-ticino` en `goud-yanacocha-ticino`), dus het wegbeen eindigt op de openbare weg 0,91 km ervandaan en een stippel sluit af; (2) via-punt **Zug verwijderd**. Het lag in de stad, terwijl de A4 Rotkreuz → Zürich door het Knonaueramt loopt. Rotkreuz → Zug kostte 31,2 km voor 6,5 km hemelsbreed; het hele been ging van 266,7 naar 263,3 km.
- **Lengtetoets b1: 263,3 tegen ~200 km = +32%.** Dat is een bevinding, geen fout: de ~200 km in §2 was hemelsbreed. Castel San Pietro → Zürich Airport over de Gotthard is ~250 km over de weg. Er is geen via-punt bijgeschoven.
- **b4:** 39,7 km tegen ~35 km (+12%, binnen ±15%). Het eindanker blijft een zone (onzeker, zie §3/§7).

