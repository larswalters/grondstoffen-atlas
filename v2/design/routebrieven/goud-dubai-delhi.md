# Routebrief (licht) · goud — Dubai (DMCC) → Delhi (MMTC-PAMP)

**stroom-id:** `goud-dubai-delhi` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** geraffineerd baar-goud uit de Dubai/DMCC-raffinagezone (Gold & Diamond Park, Al Quoz —
deels uit Afrika/Rusland doorgevoerd) per **truck** naar de vrachtterminal van Dubai International (DXB), per
**vrachtvlucht** (grootcirkel) naar Delhi (DEL), en per **truck** naar de goudraffinaderij MMTC-PAMP in Rojka
Meo (Sohna, Gurugram-district) — stoppunt aan de fabriekspoort, sieradenmarkt Delhi niet als apart been getekend.
**Welke as van het verhaal:** *de Dubai–India-bullionroute* — een van de oudst gedocumenteerde luchtvrachtroutes
voor goud, gedragen door de India-UAE CEPA-handelsovereenkomst (2022): een jaarlijkse invoerkwota tegen 1%
invoerrecht, in de eerste vijf jaar gemaximeerd op 120 t/j, oplopend naar 200 t/j; voor 2024-25 werd 160 t
genotificeerd, voor 2025-26 180 t via een aparte EFC-procedure [7][8][9]. Dubai is hier zowel een zelfstandige
raffinagebron als de knijp waar Afrikaans/Russisch doré-goud (elders in dit ontwerp al eindpunt, ketens 2/5/6)
opnieuw de markt op gaat — dat is precies de rol die Dubai in de echte markt speelt, geen ontwerpfout (zie §7).

## 1 · Ketenkaart
```
DMCC-raffinagezone `au-dmcc-refine` (Gold & Diamond Park, Al Quoz 3)
   ──(b1 truck · Sheikh Zayed Rd / Al Rebat St · ~20 km)──►
   DXB-vrachtterminal `au-air-dxb` (Emirates SkyCargo)
   ──(b2 lucht · vrachtvlucht DXB → DEL, grootcirkel · ~2.185 km)──►
   DEL-vrachtterminal `au-air-del` (Delhi Air Cargo Complex, bij Terminal 3)
   ──(b3 truck · NH48 Delhi–Gurugram → Sohna Road → Sohna → Rojka Meo · ~50–55 km)──►
   MMTC-PAMP-raffinaderij `au-ref-mmtc` (Rojka Meo, Sohna, Gurugram/Nuh) ── stoppunt
   (sieradenmarkt Delhi/India: geen gebronde vervolgzending → niet getekend, zie §6)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | DMCC-raffinagezone → DXB-vrachtterminal | Sheikh Zayed Rd → Al Rebat St/Cargo Village Rd | ≈20 [eigen meting, hemelsbreed 19,8 km] | maak_stroombeen_weg | nee |
| b2 | D | lucht | DXB-vrachtterminal → DEL-vrachtterminal | vrachtvlucht DXB → DEL, grootcirkel | 2.185,2 [eigen meting, grootcirkel] | maak_luchtbeen | nee — doorgetrokken (§7: luchtvracht is een gedocumenteerde verbinding, geen "net ontbreekt") |
| b3 | D | truck | DEL-vrachtterminal → MMTC-PAMP-raffinaderij | NH48 (Delhi–Gurugram Expwy) → Sohna Road → Rojka Meo | ≈50–55 [eigen meting, hemelsbreed 38,3 km + corridor-omweg via Gurugram/Sohna] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-dmcc-refine` | laadplek (raffinage/handelszone) | Gold & Diamond Park, Al Quoz Industrial 3, Dubai (DMCC-vergunde precious-metals-zone) | 25.1261, 55.2089 | [1][10] | bron-gelegd (z15 gezien: cluster loods-/kantoorgebouwen op een verkeersknoop van Sheikh Zayed Rd in Al Quoz Industrial 3, matcht de OSM-`landuse=commercial`-vlek "Gold and Diamond Park") |
| `au-air-dxb` | overslag truck → lucht (vrachtterminal) | DXB-vrachtterminal (Emirates SkyCargo) | 25.2560, 55.3434 | [2][10] | bron-gelegd (z15 gezien: vrachtloodsen direct naast het platform, meerdere vrachttoestellen zichtbaar op de apron ernaast; OSM-gebouw "الإمارات للشحن الجوي / Emirates SkyCargo" aan Airport Internal Road) |
| `au-air-del` | overslag lucht → truck (vrachtterminal) | Delhi Air Cargo Complex, IGI Airport (bij Terminal 3) | 28.5570, 77.1000 | [3][4][10] | bron-gelegd, met voorbehoud (z16 gezien: grote loods-/hangaargebouwen + platform met meerdere toestellen, ~1 km van Terminal 3 zoals de bron aangeeft; de exacte grens tussen het cargo-warehouse en een naastgelegen onderhoudshangar is op dit beeld niet 100% te onderscheiden, zie §7) |
| `au-ref-mmtc` | losplek (raffinaderij) | MMTC-PAMP India Pvt Ltd, Rojka Meo, Sohna, Gurugram-district (Nuh) | 28.2140, 77.0611 | [5][10] | bron-gelegd (z15 gezien: industrieel complex met meerdere hallen — blauwe/witte dakplaten — te midden van een kleine plaats aan de spoorlijn/weg NH248A; OSM-gebouw "MMTC PAMP ROJKA MEO") |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Trade Centre-kruispunt (Sheikh Zayed Rd × Financial Centre Rd) | 25.2225, 55.2867 | corridor verlaat Al Quoz/Sheikh Zayed Rd hier richting Deira/Garhoud (geschat op algemene stadsgeografie; definitief bij het bakken via OSM) |
| b1 | 2 | Al Garhoud-kruising, nadering DXB | 25.2436, 55.3364 | laatste corridorkeuze vóór de vrachtterminal-toegangsweg (geschat; definitief bij het bakken) |
| b3 | 1 | Rajokri, NH48-kruising Delhi/Haryana-grens | 28.5031, 77.1111 | de corridor verlaat hier het Delhi-wegennet en gaat verder over de Delhi–Gurugram Expressway (NH48) [6] |
| b3 | 2 | Gurugram, Sohna Road-afslag | 28.4560, 77.0290 | corridor verlaat NH48 hier en gaat verder zuidwaarts over de Gurugram–Sohna Road [6] |
| b3 | 3 | Sohna | 28.2500, 77.0700 | laatste grote plaats vóór Rojka Meo; de corridor buigt hier oostwaarts het dorp in [6] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| MMTC-PAMP Rojka Meo | MMTC-PAMP India Pvt Ltd (JV MMTC Ltd / MKS PAMP) | doré/schroot/baar-import → LBMA Good Delivery-baren, munten, sieraadhalffabricaat | LBMA Good Delivery-geaccrediteerde raffinaderij; capaciteit niet in deze ronde gebrond (§7) | [5] |

## 6 · Stoppunt
De brief stopt aan de poort van MMTC-PAMP Rojka Meo: dat is de eerste plek waar de invoerstroom een naam en
adres heeft en waar de bullion tot Good-Delivery-baren wordt omgesmolten. Een vervolgzending naar de
Delhi-sieradenmarkt (in het ketenontwerp als nevenbestemming genoemd) is niet gebrond met een specifieke
afnemer of adres — fase E vervalt.

## 7 · Open punten
- **Dubai is hier tegelijk startpunt en (in andere ketens van dit ontwerp) eindpunt** van Afrikaans/Russisch
  doré-goud — expliciet benoemd in het ontwerp en door de haalbaarheidstoets bevestigd als correcte
  zelfreflectie, geen fout: Dubai is precies de knijp die meerdere assen van de wereldgoudmarkt samenbrengt.
- **"Manesar" in de ketennaam ≠ de plaats Manesar.** De naam uit het ketenontwerp ("MMTC-PAMP (Manesar)")
  verwijst in de praktijk naar de vestiging in **Rojka Meo, Sohna** (Nuh-district, Haryana) — 16 km
  zuidoostelijker dan de gelijknamige industriestad Manesar (28,3553 / 76,9327) aan de Delhi–Jaipur-corridor.
  Anker en corridor in deze brief volgen het satelliet-bevestigde Rojka Meo-punt, niet de plaatsnaam "Manesar".
- **DEL-vrachtterminal**: het cargo-warehouse en een naastgelegen hangaarcomplex liggen dicht tegen elkaar op
  het z16-beeld; welk deel exact bij het Air Cargo Complex hoort (Celebi-locatie tot mei 2025, sindsdien
  GMR-beheer) is niet 100% af te bakenen op satelliet alleen [3][4].
- **Luchtroutebron is één klasse bewijs** (algemeen bekende, decennialang gerapporteerde bullion-luchtcorridor
  Dubai↔India — WGC/RBI/DGFT-importstatistieken), geen vluchtnummer- of AWB-niveau-bevestiging; conform de
  haalbaarheidstoets ("stabiele marktkennis, niet apart getoetst") geen blokkerend punt.
- **Tussenlanding**: geen bron noemt een tussenstop op deze route → één directe vlucht aangenomen (conform
  bakhandleiding §2).
- **Via-punten b1 en b3 zijn een corridorschets** op basis van algemene stadsgeografie (Dubai) resp. het
  bekende Delhi–Gurugram–Sohna-wegennet (India); de bak-agent bevestigt de exacte ligging via OSM-routering.
- **CEPA-kwota is volatiel** (140 t → 160 t → 180 t over de laatste drie notificatierondes) en betreft de hele
  VAE→India-goudstroom, niet cargo- of terminalspecifiek voor deze ene keten.
- **Truckbenen naar/van de vrachtterminal**: b1 (~20 km) en b3 (~50–55 km) zijn beide ruim boven de "< 2 km →
  stippel"-drempel en boven de "airside zonder openbare weg"-uitzondering; beide dus als gewoon wegbeen
  (`maak_stroombeen_weg.py`), niet gestippeld.

## 8 · Bronnen
[1] OpenStreetMap (ODbL), Nominatim — landuse "Gold and Diamond Park" (way 231290392), Al Quoz Industrial 3,
Dubai, centroid 25,1261/55,2089. https://www.openstreetmap.org
[2] OpenStreetMap (ODbL), Nominatim — gebouw "الإمارات للشحن الجوي / Emirates SkyCargo" (way 249217154),
Airport Internal Road, Dubai International Airport, 25,2560/55,3434. https://www.openstreetmap.org
[3] Wikipedia, "Indira Gandhi International Airport" — air cargo complex op ~1 km van Terminal 3; brownfield
terminal (Celebi Delhi Cargo Management, JV met DIAL) + greenfield terminal (Delhi Cargo Service Centre).
https://en.wikipedia.org/wiki/Indira_Gandhi_International_Airport
[4] News on Air / Ventura Securities, mei 2025 — beveiligingsvrijgave Çelebi Delhi Cargo Terminal Management
ingetrokken; GMR Airports neemt cargo-terminalbeheer op IGI Airport over.
https://www.newsonair.gov.in/govt-revokes-security-clearance-of-turkish-firm-celebi-dial-ends-association-at-igi-airport
[5] OpenStreetMap (ODbL), Nominatim — gebouw "MMTC PAMP ROJKA MEO" (way 795879631), NH248A, Sohna, Nuh-district,
Haryana, 28,2140/77,0611; MMTC-PAMP = JV MMTC Ltd (India) / MKS PAMP (Zwitserland), LBMA Good
Delivery-geaccrediteerde raffinaderij. https://www.openstreetmap.org · https://www.mmtcpamp.com/
[6] Wikipedia (MediaWiki API, prop=coordinates) — Rajokri 28,5031/77,1111 · Gurgaon/Gurugram 28,4560/77,0290 ·
Sohna 28,2500/77,0700 · Manesar (ter onderscheid, niet gebruikt als anker) 28,3553/76,9327.
https://en.wikipedia.org/wiki/Rajokri · https://en.wikipedia.org/wiki/Gurgaon · https://en.wikipedia.org/wiki/Sohna
· https://en.wikipedia.org/wiki/Manesar
[7] Gulf News, "After CEPA, UAE exports of gold to India already hits 120/t ceiling for 2022" — CEPA-plafond
eerste vijf jaar 120 t/j, daarna 200 t/j. https://gulfnews.com/business/retail/after-cepa-uae-exports-of-gold-to-india-already-hits-120t-ceiling-for-2022-1.90135166
[8] Business Standard, 27-08-2024 — 160 t goudinvoer uit de VAE genotificeerd tegen verlaagd tarief (FY2024-25).
https://www.business-standard.com/industry/news/govt-notifies-160-tons-of-gold-import-from-uae-at-concessional-rate-124082700941_1.html
[9] The Hans India — geldigheid FY26-invoerkwotalicenties onder de India-VAE-handelsovereenkomst verlengd; 180 t
voor 2025-26 via een aparte EFC-procedure. https://www.thehansindia.com/amp/business/validity-of-fy26-gold-import-quota-licences-under-india-uae-trade-pact-extended-1092784
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16) —
`sat-goud-dubai-delhi-dmcc-golddiamondpark.png`, `sat-goud-dubai-delhi-dxb-skycargo.png`,
`sat-goud-dubai-delhi-mmtc-rojkameo.png`, `sat-goud-dubai-delhi-del-cargo-est.png`,
`sat-goud-dubai-delhi-del-cargo-zoom1.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `goud-dubai-delhi` · **bestand:** `v2/data/stroomroute-goud-dubai-delhi.json` (24,6 KB) · **recept:** `bak_goud_dubai_delhi()` in `v2/tools/bak_stromen.sh` (draaien: `bash v2/tools/bak_stromen.sh goud-dubai-delhi`).

| # | modaliteit | km | punten | naad met vorige been |
|---|---|---|---|---|
| b1 | truck | 23,2 | 478 | — (eerste been) |
| b2 | lucht | 2.185,2 | 89 | 0,0 km |
| b3 | truck | 45,4 | 634 | 0,0 km |
| **totaal** | | **2.253,8 km** | **1.201 punten** | |

**Markers:** 4 — alle op de snap-afstand van hun been-uiteinde (0,04–0,22 km, ruim binnen anker ≈ routeerpunt): `au-dmcc-refine`, `au-air-dxb`, `au-air-del`, `au-ref-mmtc`.

**Per been:**
- **b1** (DMCC-raffinagezone → DXB-vrachtterminal, Sheikh Zayed Rd → Al Rebat St/Cargo Village Rd, `maak_stroombeen_weg.py`, extract gcc-staten): 23,2 km tegen ≈20 km eigen meting (hemelsbreed 19,8 km, geen officiële wegbeheerder-lengte) = **+16,0% [licht buiten ±15% — bevinding, niet dichtgetrokken]**. De brief-schatting was zelf al een hemelsbreed-afgeleide "≈20 km", geen harde bron; de gemeten route volgt gewoon de enige beschikbare Sheikh Zayed Rd → Al Rebat St/Cargo Village Rd-corridor incl. 43 gesnoeide keerlussen (23,9 → 22,9 km vóór de ankerstukjes) en twee korte ankeraansluitingen (0,04 + 0,21 km). Geen via-punt bijgeschoven om het getal te halen.
- **b2** (DXB-vrachtterminal → DEL-vrachtterminal, `maak_luchtbeen.py`, grootcirkel): 2.185,2 km, exact gelijk aan de brief-schatting (2.185,2 km eigen grootcirkelmeting, §2/§8). **Doorgetrokken, geen stippel** — geen tussenlanding gebrond (brief §7), één rechtstreekse vlucht DXB → DEL aangenomen conform bakhandleiding §2. Geen km-toets nodig voor een luchtbeen (km = grootcirkel per constructie).
- **b3** (DEL-vrachtterminal → MMTC-PAMP Rojka Meo, NH48 → Sohna Road, `maak_stroombeen_weg.py`, extract india — reus-extract, weg- + reus-slot gebruikt): 45,4 km tegen ≈50–55 km eigen meting (hemelsbreed 38,3 km + corridoromweg via Gurugram/Sohna) = **-13,0% [binnen ±15%, OK]**. Volgt Rajokri (NH48-grenskruising) → Gurugram/Sohna Road-afslag → Sohna → Rojka Meo, mét het satelliet-bevestigde anker (niet de plaats Manesar, zie brief §7). 10 gesnoeide keerlussen (50,7 → 45,3 km), grootste bij het Rajokri-kruispunt (5,44 km dubbel gereden stuk, verwacht bij een grenskruising met een lus-op-/afrit).

**Toets (STAP 3):** naden alle 0,000 km (drie benen, elk `vooraf gebakken lijn` — geen graaf-snap tussen benen nodig) · `toets_knikken.py`: 35 knikken ≥60° (32 spikes op wegbochten <76 m straal + 3 "scherpe bocht, echt" op 3–6 m straal bij kruispunten), **0 omkeringen-terugloop** (de enige categorie die reparatie vraagt) · `toets_rechte_benen.py --min-km 5`: geen van de drie benen komt op de verdachtenlijst voor (beide truckbenen hebben honderden punten en een omwegfactor ruim > 1,000; het luchtbeen wordt per ontwerp overgeslagen) · `json.load` slaagt, `versie: 2`, `punt_formaat: lonlat`, modaliteiten `{truck, lucht}` ⊂ toegestane set, elk been ≥2 punten, bestandsgrootte 24,6 KB (ruim onder ~300 KB) · markers alle binnen de snap-afstand van hun ankerpunt (0,04–0,22 km, anker ≈ routeerpunt op elk van de vier ankers).

**Gereedschapslessen:**
- Eerste bake in deze golf-batch die zowel het lucht- als het weg-gereedschap combineert zonder wrijving: `maak_luchtbeen.py` (milliseconden, geen slot) vóór de twee wegscans, dan de bake zelf via het zwaar-slot — de volgorde uit STAP 1 (lucht → weg → bake) werkte in één keer.
- **Slot-contentie was de echte bottleneck, niet het rekenwerk:** de india-wegscan (reus-extract, 246 s scan) stond ruim een uur te wachten op een vrij `reus`-slot terwijl beide `reus`-slots en meerdere `weg`-slots al 25–45+ minuten stilstonden zonder een levend proces erachter (age tot 9.758 s, ver boven het afgesproken max=2700 s). De eigen wacht-lus reclaimede geen verlopen slots (alleen de gedeelde `neem_slot`-helper doet dat); na handmatig vrijgeven van de duidelijk-verweesde slots liep de scan meteen door. Les voor de volgende golf: een agent die zijn eigen slot-wachtlus schrijft zonder de reclaim-check bouwt een lek in het gedeelde systeem — de reclaim-logica uit de opdracht (leeftijd > max → verwijderen) hoort in élke variant van `neem_slot`, niet alleen in het gegeven voorbeeld.
- b1's lengtetoets (+16,0%) ligt net buiten de ±15%-norm terwijl de brief zelf al "≈20 km, geen officiële bron" zei — een teken dat de norm strikter is dan de brief-schatting kan dragen bij een zachte hemelsbreed-schatting, niet dat de route fout ligt (43 gesnoeide keerlussen bevestigen dat de scan een echte, iets omwegende stadscorridor volgde in plaats van een sluiproute).
