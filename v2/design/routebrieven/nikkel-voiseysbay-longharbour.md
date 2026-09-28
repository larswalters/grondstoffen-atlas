# Routebrief (licht) · nikkel — Voisey's Bay (Labrador) → Long Harbour (Newfoundland)

**stroom-id:** `nikkel-voiseysbay-longharbour` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** sulfideconcentraat van de ondergrondse Voisey's Bay-mijn (Vale Base Metals, Noord-Labrador)
per **truck** over sitewegen naar Vale's eigen ladingskade aan Anaktalak Bay, per **zeeschip** langs de
Labradorkust en door de Golf/Straat van Saint-Laurent naar Long Harbour (Placentia Bay, Newfoundland), en de
laatste ~1,6 km over eigen terrein naar de hydromet-raffinaderij — Vale's tweede, volledig eigen Atlantisch-
Canadese class-1-as (los van de Sudbury→Kristiansand-keten).
**Welke as van het verhaal:** Vale's eigen Labrador→Newfoundland-binnenketen, géén derde partij en geen
zichtbaar prijsrisico in de keten zelf. Ontwerpcapaciteit **45 kt Ni/j** concentraat (Voisey's Bay, volledige
ramp-up verwacht H2 2026) tegen een **Long Harbour-nameplate van 50 kt Ni/j**; werkelijke 2025-productie ligt
daar nog onder — Long Harbour (eigen bron) leverde in Q4 2025 **7,4 kt Ni**, op jaarbasis geannualiseerd
≈ **29,6 kt Ni/j** tijdens de ramp-up [9][10]. Zeevaart is bovendien seizoensgebonden (Vale's winterprogramma
22 jan–6 apr, eigen ijstracks) — zie §6.

## 1 · Ketenkaart
```
Voisey's Bay-mijn `ni-voiseysbay-mijn` ──(b1 truck · sitewegen, stippel, ~9-13 km)──►
Voisey's Bay-kade `ni-voiseysbay-kade` (Anaktalak Bay / Edward's Cove-cluster)
   ──(b2 zee · haven-aanloop + MARNET · Labradorkust → Straat Belle Isle/Golf v. Saint-Laurent → Placentia Bay
       · ~1.700 km indicatief, seizoensijs)──►
Long Harbour-kade `ni-longharbour-kade` ──(b3 truck · eigen terrein/conveyor, stippel, ~1,6 km)──►
Long Harbour Processing Plant `ni-longharbour-fabriek` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-voiseysbay-mijn` → `ni-voiseysbay-kade` | sitewegen, geen openbaar net | ~9-13 [satellietblik, wegvolgend geschat; niet gepubliceerd] | stippel — eigen terrein | ja |
| b2 | B | zee | `ni-voiseysbay-kade` → `ni-longharbour-kade` | Labradorkust → Straat Belle Isle/Golf v. Saint-Laurent → Placentia Bay, seizoensgebonden ijsvaart | ~1.700 [ontwerp, indicatief kustvolgend; niet gemeten] | MARNET + haven-aanloop **aan beide zijden** (§6, LAR-586) | aanloop: ja/ja |
| b3 | C | truck | `ni-longharbour-kade` → `ni-longharbour-fabriek` | eigen terrein/transportband, geen openbaar net | ~1,6 [satellietblik, geschat] | stippel — eigen terrein | ja |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-voiseysbay-mijn` | mijn/concentrator | Voisey's Bay Mine (Vale Base Metals) | 56.3347, -62.1031 | [5][11], hergebruikt uit `w-voiseys-bay-vale` | bron-gelegd (z14 gezien: open pit/ondergrondse mijncomplex, concentrator, tailingsvlakken, landingsstrip) |
| `ni-voiseysbay-kade` | laadplek/overslag (kandidaat Edward's Cove-cluster) | sitefaciliteit Anaktalak Bay | 56.4115, -62.0800 | [7][11] | aannemelijk (z17 gezien: brandstoftankenpark + opslag-/equipmentterrein aan getijdenwater, via de siteweg met de mijn verbonden; het exacte ertsladingsdok is op dit beeld niet apart te onderscheiden — zie §7) |
| `ni-longharbour-kade` | overslag zee → land (wharf) | Long Harbour-kade (Vale) | 47.4230, -53.8230 | [6][8][11] | bron-gelegd (z17 gezien: kade met laadconveyor-overkapping, bulkopslagloods, bezinkbekken en een gemeerd schip — dit is de wharf, niet de stadscentroïde) |
| `ni-longharbour-fabriek` | raffinaderij (hydromet) | Long Harbour Processing Plant (Vale) | 47.4101, -53.8133 | [6][8][11] | bron-gelegd (z16 gezien: het volledige procescomplex — hoofdgebouwen, tanks, bezinkbekkens — ~1,6 km zuid van de kade, exact zoals de EIS het beschrijft) |

## 4 · Via-punten
Geen — beide truckbenen zijn sitewegen zonder corridorkeuze (§ werkwijze); het zeebeen is haven → haven.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Long Harbour Processing Plant | Vale Base Metals | Ni-sulfideconcentraat (Voisey's Bay) → afgewerkt nikkel (+ Cu, Co als bijproduct) | nameplate 50 kt Ni/j + 20 kt Cu/j + 2,6 kt Co/j; werkelijk Q4 2025 7,4 kt Ni (≈29,6 kt/j geannualiseerd, ramp-up) | [1][2][3][9][10] |

## 6 · Stoppunt
De brief stopt bij de Long Harbour Processing Plant: dit is het eindproduct (afgewerkt nikkel) en geen bron
documenteert een vervolgzending per lading naar een LME-entrepot of derde afnemer — fase D vervalt, precies
zoals bij de Sudbury→Kristiansand-keten geen fase na de raffinaderij is getekend.
**Seizoensijs (tekstuele kanttekening, geen blokkade voor het tekenen):** Vale vaart de Labradorkust-route onder
een eigen winterprogramma (22 jan–6 apr, ijs-versterkte schepen + eigen ijstracks). De gebakken zeelijn volgt de
standaard zomercorridor via MARNET; het winter-ijstrack wordt hiermee niet gemodelleerd.

## 7 · Open punten
- **Exacte ertsladingskade (Edward's Cove) niet met zekerheid vastgesteld.** heritage.nf.ca bevestigt de naam en
  ligging ("Edward's Cove, Anaktalak Bay, ~11 km noordelijk van de mijn") [7], maar Nominatim/Photon en de
  Wikipedia-API geven geen bruikbaar coördinaat voor dat specifieke punt. Deze sessie vond via satellietblik één
  sitefaciliteit (tankenpark + opslagterrein) op de kust van dezelfde inlet, ~8,6 km hemelsbreed (wegvolgend
  vermoedelijk 9-13 km) noord/noordnoordoost van de mijn, wegverbonden met de mijn — vermoedelijk onderdeel van
  hetzelfde havencomplex, maar het aparte, dieper-water ladingsdok voor de ertscarrier kon niet worden
  onderscheiden binnen het beeldbudget. `ni-voiseysbay-kade` blijft daarom *aannemelijk*, niet *bron-gelegd*.
- **Fase-A-kilometrage is een schatting, geen meting.** Het oorspronkelijke ketenontwerp noemde "<2 km
  (site-intern)"; de satellietblik laat zien dat de afstand mijn → kust-faciliteit ruim groter is (hemelsbreed
  ~8,6 km) — een afwijking van het ontwerp die de bak-agent met een echte wegmeting moet vervangen.
  zeebeen (b2): MARNET-zeeknopen 645 (57.8113, -60.6748) en 762 (47.7000, -52.5000) liggen beide zeer ver van de
  kades (haalbaarheidstoets: 185,5 km resp. 98,6 km tegen mijn-/stadscentroïdes) — met de hier gelegde kade-
  ankers moet de bak-agent de dichtstbijzijnde zeeknoop opnieuw opzoeken (`hecht_marnet.marnet_zee`), maar een
  haven-aanloop aan **beide** zijden is hoe dan ook nodig (LAR-586, > 5 km-regel).
- **Winter-ijsvaart niet gemodelleerd** (zie §6) — de gebakken lijn is de zomercorridor.
- **Jaarvolume is een ontwerpcapaciteit** (45 kt Ni/j, volledig pas H2 2026); de brief gebruikt daarnaast de
  gepubliceerde Q4-2025 werkelijke productie als correctie, maar een volledig productiejaar tegen nameplate
  ontbreekt nog.

## 8 · Bronnen
[1] Vale Base Metals, "Voisey's Bay" — operationele beschrijving, ontwerpcapaciteit. https://valebasemetals.com/our-operations/voiseys-bay/
[2] Vale Base Metals, "Long Harbour" — hydromet-raffinage, nameplate. https://valebasemetals.com/our-operations/long-harbour/
[3] PR Newswire / Vale Base Metals, 3 dec. 2024 — "Vale Base Metals Complete Voisey's Bay Transition to Underground Mining" (Mine Expansion Project, Reid Brook/Eastern Deeps). https://www.prnewswire.com/news-releases/vale-base-metals-complete-voiseys-bay-transition-to-underground-mining-302320350.html
[4] Wood Mackenzie, "Voisey's Bay Nickel Operation" (achter betaalmuur, ontwerpbron in het ketenontwerp). https://www.woodmac.com/reports/metals-voiseys-bay-nickel-operation-15926753/
[5] Wikipedia, "Voisey's Bay Mine" — coördinaat 56°20'5"N 62°6'11"W, ~35 km ZW van Nain. https://en.wikipedia.org/wiki/Voisey%27s_Bay_Mine
[6] Wikipedia, "Long Harbour Nickel Processing Plant" — coördinaat 47°25'27"N 53°49'0"W, wharf "near the port of Long Harbour", hoofdplant ~2 km zuid van de kade. https://en.wikipedia.org/wiki/Long_Harbour_Nickel_Processing_Plant
[7] Heritage NL, "The Voisey's Bay Mine" — ladingskade Edward's Cove, Anaktalak Bay, ~11 km noordelijk van de mijn. https://www.heritage.nf.ca/articles/economy/voiseys-bay.php
[8] Government of Newfoundland and Labrador, ECCC project 1243 — "Commercial Nickel Processing Plant, Long Harbour, Placentia Bay" (EIS-project). https://www.gov.nl.ca/eccc/projects/project-1243/
[9] MINING.com, "Canada's Sudbury, Voisey's Bay expansions boost Vale nickel, copper output" — Q4 2025 Long Harbour 7,4 kt Ni, FY2025 Vale-totaal 177 kt Ni. https://www.mining.com/canadas-sudbury-voiseys-bay-expansions-boost-vale-nickel-copper-output/
[10] Vale S.A., Form 6-K FY2025-kwartaalcijfers (SEC EDGAR). https://www.sec.gov/Archives/edgar/data/917851/000129281426000189/vale20260127_6k.htm
[11] Esri World Imagery via `v2/tools/sat_check.py` (z14-z17) — `v2/build-cache/satcheck/sat-nikkel-voiseysbay-longharbour-{mijn,cluster,tanks,kade,plant,fabriek}.png`; OpenStreetMap/Nominatim + Photon voor de zoekpogingen naar Edward's Cove en de Long Harbour-kade (geen bruikbaar resultaat, zie §7).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `nikkel-voiseysbay-longharbour`** → `v2/data/stroomroute-nikkel-voiseysbay-longharbour.json` —
5 benen, 1.871,5 km, 433 punten, 4 markers. truck (stippel) 8,7 km · zee (stippel) 177,3 km ·
zee 1.378,9 km · zee (stippel-geojson) 305,0 km · truck (stippel) 1,6 km. Recept: `bak_stromen.sh`
(functie `bak_nikkel_voiseysbay_longharbour`).

Toelichting per been:
- **b1 (truck, stippel)** — Voisey's Bay sitewegen mijn → kade, 8,657 km hemelsbreed (de rechte
  stippel komt automatisch op de brief-schatting van ~8,6 km uit; geen wegprofiel gebouwd, zoals de
  bak-aanwijzing voorschreef — afgelegen gebied, geen OSM-corridor te verwachten).
- **b2a (zee, haven-aanloop Voisey's Bay, RECHTE STIPPEL)** — de kade ligt 177,3 km van de
  dichtstbijzijnde MARNET-zeeknoop (645, 57,8113/-60,6748) — ver boven zowel de 5 km-norm
  (bakhandleiding §2, LAR-586) als de 25 km-max-snap zelf. `maak_havenaanloop.py` liep vast op
  `timeout 300` op **alle acht trappen** (exit 124) — geen tweede poging, conform §2: rechte
  stippel met de reden in de beennaam.
- **b2b (zee, midden)** — MARNET-router zeeknoop 645 → zeeknoop 762, 1.378,9 km over 142 punten,
  langs de Labradorkust/Straat Belle Isle/Golf van Saint-Laurent/Placentia Bay — precies de
  standaard zomercorridor uit de brief. Geen via-punten (haven → haven, geen corridorkeuze).
- **b2c (zee, haven-aanloop Long Harbour, GESLAAGD → stippel-geojson)** — de kade ligt 103,9 km
  van zeeknoop 762 (47,7000/-52,5000). `maak_havenaanloop.py` slaagde op de derde trap (cel
  0,005° gebufferd, minste land midden op de lijn) — 305,0 km over 285 punten, **0,00 km over
  land** (ook 0,00 km aan het kade-uiteinde). De geschreven geojson liep van kade → zeeknoop (de
  volgorde waarin `--van`/`--naar` zijn meegegeven); voor de reisvolgorde (aankomst uit zee) is de
  puntenlijst na de bake-run eenmalig omgekeerd naar zeeknoop → kade.
- **b3 (truck, stippel)** — Long Harbour eigen terrein/conveyor kade → fabriek, 1,609 km (brief-
  schatting ~1,6 km).

Naden tussen alle opeenvolgende benen: **0,000 km** (elk been sluit exact aan op het vorige
eindpunt — de haven-aanlopen zijn op dezelfde zeeknoop-coördinaten geknipt als het middenzeebeen).
Totaal b2 (aanloop + midden + aanloop): 177,3 + 1.378,9 + 305,0 = **1.861,2 km** tegen de
indicatieve ~1.700 km uit de brief (§1, kustvolgend, niet gemeten) = **+9,5%** — binnen de ±15%-
orde ondanks dat de brief zelf geen harde norm eist ("indicatief"). Fase D/E vervalt (brief §6,
stoppunt = Long Harbour Processing Plant, geen vervolgzending gedocumenteerd). Seizoensijs (Vale's
winterprogramma) is niet gemodelleerd — bewust de standaard zomercorridor (brief §6).

Toets: `toets_knikken.py` geeft **2 knikken ≥60°** (beide krappe bochten op het middenzeebeen,
82,7° bij 50,00000/-54,60000 en 72,9° bij 49,60000/-52,50000 — normale MARNET-routebochten langs de
kust), **0 omkeringen ≥150°, 0 terugloop** — geen reparatie nodig. `toets_rechte_benen.py --min-km 5`
plaatst de vier stippel-/aanloopbenen correct in de "al gestippeld"-categorie (8,7 · 177,3 · 305,0
km, omwegfactoren 1,00–2,93) en het middenzeebeen (1.378,9 km, omwegfactor 1,103) krijgt geen
vlag — het is een echt geroute pad, geen verdachte rechte lijn. Json geldig: versie 2,
punt_formaat lonlat, alle modaliteiten in {truck, zee}, elk been ≥ 2 punten, bestand 9,1 KB.
Markers liggen alle op 0,000 km van hun been (elk anker is letterlijk het been-eindpunt).

**Open punt voor deze sessie (uit de bak-aanwijzing):** of `ni-voiseysbay-kade` (tankenpark/
opslagterrein) inderdaad hetzelfde complex is als het Edward's Cove-ladingsdok, of dat er verderop
in dezelfde inlet een apart, dieper-water dok bestaat dat deze sessie niet kon onderscheiden —
onveranderd overgenomen uit §7, niet opgelost door het bakken.

**Gereedschapslessen:**
- Twee kade-ankers in dezelfde keten kunnen totaal verschillend uitpakken bij `maak_havenaanloop.py`
  ondanks vergelijkbare afstand tot hun zeeknoop (177 km vs. 104 km): de Labradorkust rond Voisey's
  Bay is zo fijnkorrelig/fjordachtig dat alle acht trappen vastliepen binnen de 300 s-timeout,
  terwijl de Newfoundland-kust bij Long Harbour op de derde trap al een schone oplossing gaf. Geen
  patroon om op te vertrouwen — elke kade moet apart geprobeerd worden.
- `maak_havenaanloop.py` schrijft de geojson in de `--van`→`--naar`-volgorde die je meegeeft, niet
  in reisvolgorde. Voor een AANKOMST-aanloop (zeeknoop → kade) met `--van <kade> --naar <zeeknoop>`
  (nodig om dezelfde `--naar`-conventie als de vertrek-aanloop te gebruiken) moet de puntenlijst ná
  het schrijven handmatig omgekeerd worden — anders ontstaat een naad van de volledige aanloop-
  lengte tussen het middenzeebeen en de eerste stippel-geojson-regel. `hecht_marnet.py` reverst
  `--stippel-geojson`/`--been-geojson` niet zelf.
- Bij een dubbele haven-aanloop (beide zijden > 5 km, LAR-586) telt de indicatieve brief-km voor
  het HELE zeebeen, niet alleen het MARNET-midden — de plausibiliteitscheck moet aanloop + midden +
  aanloop optellen, anders lijkt het been onterecht buiten de orde te vallen.
