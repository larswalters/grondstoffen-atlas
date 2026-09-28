# Routebrief (licht) · goud — Mendrisio (Argor-Heraeus) → Malpensa → Mumbai (India)

**stroom-id:** `goud-argor-mumbai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** Argor-Heraeus (Mendrisio, Ticino) raffineert goud tot baren, die per **truck** (A2/A9) naar de vrachtterminal van Milaan-Malpensa (MXP) gaan, per **vrachtvlucht** (grootcirkel MXP → BOM) naar Mumbai vliegen, en van de BOM-vrachtterminal per **truck** naar de groothandelsmarkt Zaveri Bazaar rijden — de eerste luchtketen van de atlas (M31 golf 3).
**Welke as van het verhaal:** Zwitserland → India (raffinaat → sieradenmarkt). India is 's werelds grootste sieradenmarkt en haalt het overgrote deel van zijn goudinvoer per luchtvracht binnen; Zwitserland is historisch India's grootste bronland voor geraffineerd goud [1][2][3][4]. India importeerde in 2025 ≈640 t goud (~$45 mrd) [4]; Zwitserland levert daarvan ≈40 % ≈ 256 t/j [4], tegen 700–800 t/j totaal en >25–30 % Zwitsers aandeel in 2023–24 [1][2] — Argor-Heraeus is één van de vier grote Zwitserse raffinaderijen (naast Valcambi, PAMP, Metalor) die samen dat aandeel dragen; deze brief modelleert Zwitserland → Mumbai via de grootste van de vier.

## 1 · Ketenkaart
```
Argor-Heraeus, Mendrisio `au-ref-argor` ──(b1 truck · A2(CH)/A9-A8(IT) · ≈70 km)──► Malpensa-vrachtterminal `au-air-mxp` (MXP)
   ──(b2 lucht · vrachtvlucht MXP → BOM, grootcirkel · 6.508,5 km gemeten)──► Mumbai (BOM)-vrachtterminal `au-air-bom`
   ──(b3 truck · Western Express Hwy → S.V. Road/Dr. Annie Besant Rd · ≈25 km)──► Zaveri Bazaar `au-mkt-zaveri` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Argor-Heraeus → Malpensa-vrachtterminal | A2 (CH) → grens Chiasso → A9/A8 (IT) | ≈70 [ontwerp]; hemelsbreed-som via-punten 64,1 | maak_stroombeen_weg | nee |
| b2 | D | lucht (vrachtvlucht) | Malpensa (MXP) → Mumbai (BOM), beide vrachtterminal | grootcirkel | 6.508,5 (gemeten, `maak_luchtbeen.py`, terminal-tot-terminal) | maak_luchtbeen | nee — doorgetrokken (net-per-definitie tussen twee gelegde terminals) |
| b3 | D | truck | BOM-vrachtterminal → Zaveri Bazaar | Western Express Highway → S.V. Road → Dr. Annie Besant Road | ≈25 [ontwerp]; hemelsbreed-som via-punten 22,2 | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-ref-argor` | raffinaderij (kop) | Argor-Heraeus SA, Mendrisio (Ticino) | 45.8749, 8.9818 | [7][10] | bron-gelegd (z15 gezien: gebouwencomplex met hallen tussen spoorlijn en A2, industrieterrein Mendrisio–Salorino; OSM-bedrijfsnode 14 m van het complex) — hergebruikt/verfijnd t.o.v. v1 `au-ref-argor` (45.87,8.98) |
| `au-air-mxp` | vrachtterminal (overslag truck→lucht) | Milano Malpensa Cargo, Cargo City Sud | 45.6142, 8.7186 | [8][10] | bron-gelegd (z15 gezien: vrachtloodsen + platform met vrachttoestellen op de apron, Cargo City Sud, direct naast de brandweerpost van de luchthaven) |
| `au-air-bom` | vrachtterminal (overslag lucht→truck) | Mumbai Air Cargo Complex, Sahar (CSMIA) | 19.0954, 72.8660 | [6][9][10] | bron-gelegd (z15 gezien: vrachtplatform met toestellen west van de passagiersterminal, tussen de twee banen; OSM `aeroway=terminal` "Cargo Terminal" 5 m van het punt) — hergebruikt/verfijnd t.o.v. v1 `au-air-bom` (19.09,72.87, luchthavencentroïde) |
| `au-mkt-zaveri` | groothandelsmarkt (stoppunt) | Zaveri Bazaar, Mumbai | 18.9518, 72.8307 | [5][9] | aannemelijk (z15 gezien: dichte historische marktwijk bij Kalbadevi/Bhuleshwar, geen los gebouw te onderscheiden — zie §7) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Chiasso — grenspost CH/IT | 45.8333, 9.0333 | overgang A2 (Zwitserland) → Italiaans net, verplicht knooppunt [10] |
| b1 | 2 | San Fermo della Battaglia (Como-tunnels A9) | 45.8084, 9.0486 | de A9 (Autostrada dei Laghi) passeert Como ondergronds hier; enige doorgaande route naar het zuiden [10] |
| b1 | 3 | Fino Mornasco | 45.7429, 9.0476 | A9 blijft de enige corridor tot het A8-knooppunt [10] |
| b1 | 4 | Lainate — A9/A8-knooppunt | 45.5632, 9.0317 | corridorkeuze: hier splitst de route van A9 (naar Milaan) af naar A8 (naar de meren/Malpensa) — `highway=motorway_junction` [9] |
| b1 | 5 | Busto Arsizio (A8) | 45.6119, 8.8518 | A8 blijft de doorgaande route noordwestwaarts [10] |
| b1 | 6 | Cardano al Campo (A8-afslag Malpensa) | 45.6457, 8.7725 | hier verlaat de corridor de A8 naar de luchthaven-toegangsweg [10] |
| b3 | 1 | Vile Parle (Western Express Highway) | 19.0999, 72.8440 | enige doorgaande zuidwaartse corridor vanaf de luchthaven [9] |
| b3 | 2 | Bandra West | 19.0583, 72.8303 | WEH gaat hier over in S.V. Road, de doorgaande route naar het zuiden [9] |
| b3 | 3 | Mahim | 19.0423, 72.8398 | S.V. Road/Lady Jamshedji Road blijft de kustcorridor volgen [9] |
| b3 | 4 | Worli (Dr. Annie Besant Road) | 19.0308, 72.8157 | corridorkeuze: verder via Annie Besant Road/Lower Parel i.p.v. de tolweg Bandra-Worli Sea Link [9] |
| b3 | 5 | Crawford Market | 18.9473, 72.8345 | laatste doorgaande punt vóór de nauwe marktstraten van Kalbadevi/Zaveri Bazaar [9] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Argor-Heraeus, Mendrisio | Argor-Heraeus SA | doré/schroot/mijngoud → LBMA-good-delivery baren | cap. ≈1.000 t/j (v1-cijfer, niet dit golf herbrond) | [7] |

## 6 · Stoppunt
De brief stopt bij Zaveri Bazaar: het is de door het ontwerp aangewezen grootste losse sieradenmarkt van India en de groothandelsschakel waar bewerkt goud de detailhandel/sieradensector ingaat; een specifieke juwelier of beursgebouw is niet aan te wijzen (§7), dus fase E (eindsieraad) vervalt.

## 7 · Open punten
- **Zaveri Bazaar is een marktwijk, geen los gebouw**: de coördinaat is het eigen Wikipedia-punt van de bazaar (niet een stads- of landcentroïde), maar op z15 zijn geen aparte marktgebouwen te onderscheiden in de dichte bebouwing — status *aannemelijk*, geen scherper anker gevonden.
- **Mumbai/Zaveri Bazaar als eindpunt is een bewuste vereenvoudiging** (haalbaarheidstoets, bindend): een deel van de Zwitserse import gaat ook via Delhi/MMTC-PAMP (Manesar) of Ahmedabad — hier wordt bewust de grootste losse markt getekend.
- **Geen tussenlanding gebrond** voor de vlucht MXP→BOM (geen bron noemt een hub) → één directe vlucht getekend, conform bakhandleiding §2.
- **Volume is Zwitserland-breed, niet Argor-specifiek**: geen bron isoleert het aandeel van Argor-Heraeus in de ≈256 t/j Zwitsers-Indiase stroom; de vier grote Ticino-raffinaderijen (Valcambi/PAMP/Argor/Metalor) delen die markt.
- Gepubliceerde wegkilometers voor b1/b3 zijn ramingen uit het ketenontwerp, geen officiële bron; de hemelsbreed-som van de via-punten (64,1 resp. 22,2 km) ligt eronder, zoals verwacht voor een geschatte wegafstand.
- Malpensa-vrachtterminal en Mendrisio liggen beide binnen Zwitserland/Italië-extract; geen leidingnet/spoor relevant voor dit been.

## 8 · Bronnen
[1] World Gold Council, Gold Demand by Country (India-vraagrapportages, jaarcijfers). https://www.gold.org/goldhub/data/gold-demand-by-country
[2] Argor-Heraeus SA, bedrijfswebsite. https://www.argor.com/
[3] Reserve Bank of India. https://www.rbi.org.in/
[4] tradeint.com, "India imports gold from which countries in Q1/2026?" — India-import 2025 ≈640 t (~$45 mrd), Zwitserland ≈40% van de import. https://tradeint.com/insights/india-imports-gold-from-which-countries/
[5] Wikipedia, "Zaveri Bazaar" — jewellery market, coördinaat 18.951808/72.830697. https://en.wikipedia.org/wiki/Zaveri_Bazaar
[6] Wikipedia, "Chhatrapati Shivaji Maharaj International Airport" — coördinaat 19.08861/72.86806. https://en.wikipedia.org/wiki/Chhatrapati_Shivaji_Maharaj_International_Airport
[7] Wikipedia/MediaWiki-coordinates, "Milan Malpensa Airport" — coördinaat 45.63/8.72306. https://en.wikipedia.org/wiki/Milan_Malpensa_Airport
[8] OpenStreetMap (ODbL) via Nominatim — "Argor-Heraeus SA", office=company, 45.8748809/8.9818097. https://www.openstreetmap.org
[9] OpenStreetMap (ODbL) via Photon — "Milano Malpensa Cargo" warehouse Cargo City Sud (45.6141746/8.7185941); "Cargo Terminal" aeroway=terminal Sahar Village Mumbai (19.09544/72.86600); Lainate motorway_junction A8/A9 (45.5632/9.0317); Crawford Market amenity=marketplace (18.9473/72.8345); Vile Parle/Bandra West/Mahim/Worli-Rajiv Gandhi Sea Link plaatsnodes. https://photon.komoot.io
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-goud-argor-mumbai-argor.png`, `sat-goud-argor-mumbai-malpensa.png`, `sat-goud-argor-mumbai-bomcargo.png`, `sat-goud-argor-mumbai-zaveri.png`; via-punten uit dezelfde Photon-bevraging als [9].
[11] World Gold Council, "India gold market update: Import tightening" (2026-05) — kwartaalimport 175–236 t, ≈8% van de Indiase merchandise-import 2025. https://www.gold.org/goldhub/gold-focus/2026/05/india-gold-market-update-import-tightening
[12] Kimberley Process / LBMA-lijst (Good Delivery-raffinaderijen, context Argor-Heraeus-status) — geraadpleegd, geen aanvullend cijfer gebruikt. https://www.lbma.org.uk/


## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `goud-argor-mumbai`** → `v2/data/stroomroute-goud-argor-mumbai.json` — 4 benen,
**6.611,0 km**, 2.686 punten, 4 markers. truck 76,0 + lucht 6.508,5 + truck 0,1 (stippel) +
truck 26,4 = 6.611,0 km. Recept: `bak_stromen.sh` (functie `bak_goud_argor_mumbai`).
Bestandsgrootte **51,6 KB** (binnen het normale bereik van de corpus).

**b1 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel `goud-argor-mumbai-argor-mxp`,
extracts `zwitserland`+`italie`):** Argor-Heraeus, Mendrisio → Chiasso-grens → San Fermo della
Battaglia (Como-tunnels A9) → Fino Mornasco → Lainate (A9/A8-knooppunt) → Busto Arsizio →
Cardano al Campo → Milaan-Malpensa (MXP) vrachtterminal, over A2 (CH) → A9/A8 (IT). **75,9-76,0 km
tegen ~70 km (ontwerpschatting, geen officiële wegbeheerder-lengte gevonden voor een
grensoverschrijdend CH→IT-traject) = +8,4%, binnen ±15%.** Anker-verbindingen 0,02 km
(plant → weg) en 0,09 km (weg → kade), beide onder de 0,5 km-norm — geen stippel nodig. 235
keerlussen gesnoeid (79,5 → 75,9 km wegkilometers, dubbel gereden stukken op de Alpenwegen).

**b2 (lucht, doorgetrokken, `maak_luchtbeen.py`):** grootcirkel Milaan-Malpensa (MXP) →
Mumbai (BOM), **6.508,5 km, 262 punten** — exact de eerder in de brief gemeten waarde. Geen
km-toets (een luchtbeen ís de grootcirkel per constructie). Doorgetrokken, geen stippel — lucht
is per regel nooit gestippeld. Geen tussenlanding gebrond (brief §7) → één directe vlucht.

**Stippel (truck, "last mile", BOM-vrachtterminal → openbare weg):** het satelliet-gelegde
`au-air-bom`-anker (Mumbai Air Cargo Complex, Sahar, 19,0954/72,8660) bleek bij het bakken te
snappen op een **geïsoleerd airside-wegcomponent** — gemeten met een BFS over de india-scan
(dezelfde graaf als `maak_stroombeen_weg.py` gebruikt): componentgrootte **9 knopen** vanaf de
anker-snap tegen **178.739 knopen** op het publieke net, dichtstbijzijnde publieke-netknoop
0,117 km van de anker-snap. Zelfde klasse bevinding als eerder bij `au-zrh-vrachtterminal`
(goud-yanacocha-ticino) en `dia-surat-bourse` (diamant-surat-hongkong): `eindToegangPrivaat`
lost een ACCESS-filter op, geen COMPONENT-scheiding, en hielp hier dus niet. Opgelost zoals de
bakhandleiding §2 Lucht voorschrijft ("last mile … zonder openbare weg → stippel"): b3 is
gescand vanaf het dichtstbijzijnde punt op het openbare wegennet (72,865345/19,096391, **0,13 km**
van het anker, gemeten met dezelfde graaf) en die 0,13 km is hier een korte, gemotiveerde
stippel. **0,130 km, 2 punten.**

**b3 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel `goud-argor-mumbai-bom-zaveri`,
extract `india`):** openbare-wegaansluiting bij BOM → Vile Parle (Western Express Highway) →
Bandra West → Mahim → Worli (Dr. Annie Besant Road) → Crawford Market → Zaveri Bazaar. **26,3-26,4
km tegen ~25 km (ontwerpschatting) = +5,4%, binnen ±15%.** De brief hield rekening met een
mogelijke korte stippel bij Kalbadevi (smalle marktstraten, brief §2/`bak_aanwijzingen`) — bleek
niet nodig: `trimStaart` knipte 1 punt overschiet-en-terug (26,36 → 26,34 km) en de lijn eindigt
gewoon op het `au-mkt-zaveri`-anker (0,01-0,04 km snap). 11 keerlussen gesnoeid
(28,7 → 26,4 km).

**Toets naden:** alle vier overgangen **≤ 0,004 km** — elk been begint vrijwel precies waar het
vorige eindigt (inclusief de stippel), ruim binnen de 5 km-norm.

**`toets_knikken.py`:** b1 (truck) 32 knikken ≥60° waarvan 2 **scherpe bochten, echt** (167,6°
en 167,0°, kleine boogstralen op de Alpencorridor — Como-tunnelzone en de A8-oprit bij Busto
Arsizio) en de rest spikes <45 m (OSM-wegdetail, geen omkeringen die op een verkeerd via-punt
wijzen). b3 (truck) 37 knikken ≥60° waarvan 1 **scherpe bocht, echt** (180,0°, R≈0 m, bij
19,05834/72,83066 — Bandra-Worli-kustweg, een haarspeldbocht op de OSM-geometrie) en de rest
spikes <80 m. Lucht-been: 0 knikken, 0 omkeringen (verwacht, een grootcirkel heeft geen scherpe
bochten). **Totaal 69 knikken ≥60°, 3 omkeringen ≥150°, 0 TERUGLOOP** — niets hoefde
gerepareerd te worden.

**`toets_rechte_benen.py --min-km 5`:** geen enkel been van deze stroom komt naar voren — het
luchtbeen wordt per constructie overgeslagen en geen ander been (≥5 km) heeft een omwegfactor
van 1,000.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, lucht} (binnen
de toegestane set {zee, binnenvaart, truck, spoor, leiding, lucht}), elk been ≥2 punten
(minimum 2, op de stippel en het luchtbeen na alle ver boven de 2), bestandsgrootte 52.883 byte
(51,6 KB).

**Gereedschapslessen:**
- **`eindToegangPrivaat` lost een ACCESS-filter op, geen COMPONENT-scheiding** — de derde keer
  dat een luchthaven-vrachtplatform op een geïsoleerd airside-wegcomponent blijkt te snappen
  (na Zürich in goud-yanacocha-ticino en DREAM City in diamant-surat-hongkong). Een BFS over de
  gescande graaf (component vanaf de ankerknoop vs. de grootste component) onderscheidt dit
  betrouwbaar van een gewone access-tag-uitsluiting vóórdat je `eindToegangPrivaat` probeert.
- **`maak_luchtbeen.py` gaf exact 6.508,5 km** zoals al in de brief opgenomen (proefgedraaid
  vóór deze bake-sessie) — de grootcirkelberekening is deterministisch en reproduceert 1-op-1.
- Beide wegbenen kwamen ruim binnen ±15% uit ondanks dat de gepubliceerde km's zelf
  ontwerpschattingen zijn zonder officiële bron (brief §7) — de via-puntenketens uit de brief
  waren goed gepind op de doorgaande weg (snaps overal ≤0,76 km, meeste ≤0,1 km).
