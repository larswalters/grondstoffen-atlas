# Kolen · Buchanan-mijn (Virginia) → Lambert's Point, Norfolk (Virginia)

**stroom-id:** `kolen-pocahontas-norfolk` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** cokeskool (metallurgische kolen) uit de ondergrondse Buchanan-mijn (Coronado Global
Resources, Pocahontas-cokeskoolvelden, Buchanan County, zuidwest-Virginia) per Norfolk Southern-spoor
rechtstreeks naar Lambert's Point Coal Terminal Pier 6 in Norfolk — de historische spoorlijn (Norfolk &
Western) die letterlijk om deze kolenstroom werd aangelegd, en de eerste Atlantische kolen-exportkade op de bol.
**Welke as van het verhaal:** reserve-as golf 3 (M31), VS-Appalachen → eerste Atlantische kolenexportkade.
Buchanan + het zustercomplex Logan (WV) samen 5,3 Mt saleable production in 2025 (Coronado 10-K FY2025 [2],
niet Buchanan-alleen — §7); Lambert's Point Pier 6 heeft 48 Mt/j exportcapaciteit voor alle NS-aangeleverde
mijnen samen, niet Buchanan-specifiek [1].

## 1 · Ketenkaart
```
Buchanan-mijn (Coronado, Buchanan County VA) `kolen-buchanan-laad`
   ──(b1 spoor · Norfolk Southern-hoofdlijn door de Pocahontas-cokeskoolvelden · ~504 km hemelsbreed)──►
Lambert's Point Coal Terminal Pier 6, Norfolk `kolen-lambertspoint-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-buchanan-laad` → `kolen-lambertspoint-kade` | Norfolk Southern-hoofdlijn (historisch Norfolk & Western) door de Pocahontas-cokeskoolvelden [2][4] | hemelsbreed 503,8 km, geen gepubliceerde spoorkm | toets_spoorroute (`BAKE_SUFFIX=-raw`; extracts us-virginia + us-west-virginia) | nee |

Geen via-punten: geen bron noemt de exacte corridor (Bluefield-omweg, wisselplaatsen); de router zoekt de
kortste weg over het 1-op-1-spoornet tussen de twee ankers (§7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-buchanan-laad` | mijn / laadspoor | Buchanan Mine (Coronado Global Resources), Buchanan County, Virginia | 37.1625, -81.9876 | [2][3][5][6] | bron-gelegd (z15 gezien: gebouwencluster en toegangsweg in een smalle bergvallei, direct naast een zichtbaar donker terrasvormig kolenverwerkings-/afvalbekken — coördinaat komt vrijwel exact overeen met het OSM-vlak-centroïde `Buchanan Mine #1`, 3 m verschil — zie `sat-kolen-pocahontas-norfolk-buchanan.png`) |
| `kolen-lambertspoint-kade` | overslag spoor → zeeschip (losplek/exportterminal) | Lambert's Point Coal Terminal Pier 6 (Norfolk Southern), Norfolk, Virginia | 36.87468, -76.32348 | [1][2][6] | bron-gelegd (z15 gezien: waaiervormig spoor-rangeerterrein met tientallen parallelle sporen dat samenkomt op een pier het water in, duidelijk gescheiden van de containerterminals ten oosten en het olieterminal ten westen — coördinaat is het Wikipedia-geohack-punt, exact op het rangeerterrein, ~250 m landinwaarts van de pierkop — zie `sat-kolen-pocahontas-norfolk-lambertspoint.png`) |

## 4 · Via-punten
Geen — zie §2 (geen gepubliceerde corridorkeuze om te pinnen; één doorgaande NS-spoorcorridor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lambert's Point Pier 6 | Norfolk Southern | cokeskool (spoor) → bulklading (zeeschip) | 48 Mt/j exportcapaciteit (alle NS-aangeleverde mijnen, niet Buchanan-specifiek); grootste kolenlaadfaciliteit van het noordelijk halfrond | [1][2] |

Geen bewerking: kolen wordt bij Lambert's Point ongewassen overgeslagen van trein naar schip, geen
raffinage-/verwerkingsstap.

## 6 · Stoppunt
De brief stopt bij de Lambert's Point-kade: geen bron noemt een specifieke overzeese eindkoper of -haven per
lading — de Coronado-10-K zegt alleen "for export customers" in algemene zin, conform de v1-claim
(Europa/India/Brazilië-staal) uit het eigen ontwerp-item.

## 7 · Open punten
- **Buchanan verscheept óók via CNX Marine Terminal**, niet uitsluitend via Lambert's Point: de Coronado
  10-K FY2025 noemt beide kades naast elkaar ("transports Buchanan's coal to Lamberts Point Coal Terminal
  Pier 6 and to CNX Marine Terminal for export customers"). Dit been toont bewust alleen de Lambert's
  Point-tak (het ontwerp-item vroeg specifiek om deze keten); het CNX-aandeel is niet gekwantificeerd.
- **Geen Buchanan-specifiek productiecijfer gevonden**: de 5,3 Mt in §"welke as" is Buchanan + Logan (WV)
  samen (Coronado 10-K FY2025); geen bron splitst dat per mijn.
- **Producentverwarring vermeden, niet opgelost voor de hele regio**: Alpha Metallurgical Resources (grootste
  VS-cokeskoolproducent) verscheept het merendeel van zijn productie via zijn 65%-belang in Dominion Terminal
  Associates, Newport News (CSX) — een andere kade/spoorwegmaatschappij dan Lambert's Point/Norfolk Southern
  [7]. Deze keten kiest bewust Coronado/Buchanan, wiens eigen 10-K de NS→Lambert's Point-koppeling expliciet
  noemt.
- **Geen exacte spoorcorridor (via-punten)**: geen bron geeft de wisselplaats(en) tussen Buchanan County en
  Norfolk (bv. via Bluefield, WV); de bak-agent laat de 1-op-1-router de kortste weg vinden en meldt of dat
  plausibel is (geen omweg naar een ver gelegen netcomponent).
- **Geen zeebeen getekend**: geen bron noemt een specifieke koper of haven voor déze mijn-tot-kade-as, alleen
  de regionale v1-claim (Europa/India/Brazilië-staal) uit het ontwerp-item.

## 8 · Bronnen
[1] Wikipedia, "Lambert's Point" — coördinaten 36.87468,-76.32348; "a large coal exporting facility"; Norfolk
Southern Pier 6 = grootste kolenlaadfaciliteit van het noordelijk halfrond, 48 Mt/j exportcapaciteit.
https://en.wikipedia.org/wiki/Lambert%27s_Point
[2] Coronado Global Resources Inc., Form 10-K FY2025 (SEC EDGAR, gearchiveerd 2026) — "The surface facilities
at Buchanan are located along a Norfolk Southern rail line... Norfolk Southern transports coal from the
Buchanan mine complex either to domestic customers or to Lamberts Point Coal Terminal Pier... for overseas
shipment" (oudere jaargang) / FY2025: "The Norfolk Southern railroad transports Buchanan's coal to Lamberts
Point Coal Terminal Pier 6 and to CNX Marine Terminal for export customers"; Buchanan+Logan 5,3 MMt saleable
production 2025; 100%-eigendom Coronado. https://www.sec.gov/Archives/edgar/data/0001770561/000156276226000024/c561202510K.htm
[3] OpenStreetMap/Nominatim (ODbL) — "Buchanan Mine #1", industrieterrein-vlak, Buchanan County, Virginia,
centroïde 37.1625332,-81.9875942. https://www.openstreetmap.org
[4] Wikipedia, "Norfolk Southern Railway" — Class I-spoorwegmaatschappij, gevormd 1982 uit fusie Norfolk &
Western Railway + Southern Railway; kolen historisch de grootste vrachtstroom.
https://en.wikipedia.org/wiki/Norfolk_Southern_Railway
[5] Area Development, "Australia-Based Coronado Global Resources Expands Buchanan-Tazewell County, Virginia,
Operations" (2022-08-26) — Buchanan = grootste metallurgische-kolenmijn van Virginia, ondergronds
langwand-mijn, productie sinds 1983, langwand sinds 1987, ~600 werknemers.
https://www.areadevelopment.com/newsitems/8-26-2022/coronado-global-resources-buchanan-tazewell-county-virginia.shtml
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15) —
`v2/build-cache/satcheck/sat-kolen-pocahontas-norfolk-buchanan.png`,
`v2/build-cache/satcheck/sat-kolen-pocahontas-norfolk-lambertspoint.png`.
[7] Alpha Metallurgical Resources, "Contact Us"/bedrijfspagina Dominion Terminal Associates — "exports most
of its production through its 65% ownership interest in Dominion Terminal Associates, an export terminal
located in Newport News, Virginia"; DTA-capaciteit ~22 Mt/j (2017). https://www.dominionterminal.com/about-us/
[8] v2/design/kolen.md (v1-ontwerp, §3a "coal-us-appalachia" + havennode Hampton Roads/Norfolk) — interne
ontwerpnotitie, geen site-niveau bron voor déze specifieke mijn-tot-kade-as.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Eén been (spoor), 790,7 km · 2.961 punten · 2 markers · `v2/data/stroomroute-kolen-pocahontas-norfolk.json`
(55,2 KB).**

| # | modaliteit | km | punten | naad | toelichting |
|---|---|---|---|---|---|
| 1 | spoor (stippel) | 9,0 | 2 | 0,00 km | Buchanan-mijn-anker → snappunt op het 1-op-1-spoornet — laadspoor/mijnaansluiting niet in OSM gekarteerd (§ toelichting stippels) |
| 2 | spoor | 781,7 | 2.959 | 0,00 km | Norfolk Southern-hoofdlijn Buchanan-mijn → Lambert's Point Pier 6 |

**Recept:** `bash v2/tools/bak_stromen.sh kolen-pocahontas-norfolk` (functie `bak_kolen_pocahontas_norfolk`,
`v2/tools/bak_stromen.sh`). Geometrie van been 2 komt uit
`BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=37.1625,-81.9876 --naar=36.87468,-76.32348
--naam=kolen-pocahontas-norfolk-buchanan-lambertspoint --hoofd-km=1000 --max-snap=60` (console bevestigde
"3260717 spoor-edges" → `-raw`/1-op-1-net actief). Geen wegbeen, geen profiel in `maak_stroombeen_weg.py`
nodig.

**Toelichting per stippel:** het spoornet snapt bij de Buchanan-mijn pas op **9,01 km** van het anker
(37,1625/−81,9876 → 37,2432/−81,9784) — het eigen laadspoor/mijnaansluiting van de mijn is niet in OSM
gekarteerd (analoog aan het NARM-precedent uit de gillette-brief, en het Chuquicamata-emplacementpatroon:
zie ook `koper-chuqui-tongling` been 1, exact dezelfde 9,0 km-klasse). Korte rechte stippel
"laadspoor/mijnaansluiting (geen net op deze korrel)", niet doorgetekend tot in de mijninstallatie zelf.
Bij Lambert's Point snapt het net op **0,13 km** van het anker — geen stippel nodig, doorgetrokken tot de
kade.

**Km-toets:** geen gepubliceerde spoorkm om tegen te toetsen (§2 van de brief); hemelsbreed 503,8 km tegen
gemeten 781,7 km (verhouding route/grootcirkel **1,54**) — de ±15%-toets geldt hier expliciet als indicatie,
niet als norm. De verhouding is geografisch plausibel: het pad blijft binnen Virginia/West-Virginia
(lon −82,18…−76,27, lat 36,72…37,55) en volgt de bergachtige Appalachen-corridor van de historische Norfolk &
Western-hoofdlijn — geen omweg naar een ver gelegen netcomponent (geen Cerrejón-Cuba-klasse). De brief
noemde zelf al dat de route mogelijk kort door West Virginia loopt (bv. via Bluefield) — dat is hier
bevestigd en normaal.

**`toets_knikken.py`:** 0 knikken ≥ 60°, 0 omkeringen, 0 terugloop over het spoorbeen (781,7 km / 2.959 pt).

**`toets_rechte_benen.py --min-km 5`:** het stippelbeen (9,0 km, omwegfactor 0,999) valt binnen de
verwachte klasse "elk been met omwegfactor 1,000 hoort een stippel te zijn" — geen bevinding. Het spoorbeen
heeft een reële omwegfactor en wordt niet als kaarsrecht gevlagd.

**Formaat-toets:** `json.load` slaagt, `versie == 2`, `punt_formaat == "lonlat"`, beide benen modaliteit
`spoor` (in de toegestane set), elk been ≥ 2 punten, bestand 55,2 KB (ruim onder de norm).

**Lessen:** het NARM/Chuquicamata-precedent (spoor-emplacement niet in OSM gekarteerd → korte stippel bij
~9 km snap) herhaalt zich hier vrijwel identiek op een heel andere as (VS-Appalachen i.p.v. Chili) — een
aanwijzing dat mijn-eigen laadsporen structureel buiten het 1-op-1-net vallen, niet een toevalstreffer.
Open punten uit de brief (CNX Marine Terminal als tweede afvoerroute, geen Buchanan-specifiek productiecijfer,
geen exacte spoorcorridor via Bluefield, geen zeebeen) blijven bewust open — geen bron beantwoordt ze voor
déze as.
