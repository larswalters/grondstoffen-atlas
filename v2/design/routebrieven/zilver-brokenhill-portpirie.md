# Zilver · Van → Via → Naar (land)

**stroom-id:** `zilver-brokenhill-portpirie` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) · **status:** gebakken
**Keten in één zin:** lood-zink-zilverconcentraat van de Rasp-mijn (Broken Hill, NSW, sinds okt. 2024 Broken Hill Mines/Coolabah Metals) per **spoor** over de Crystal Brook–Broken Hill-lijn (ARTC) naar Crystal Brook, dan per **spoor** over de Bowmans Rail-vrachtlijn naar de Nyrstar-loodsmelter in Port Pirie (Zuid-Australië), die onder meer geraffineerd zilver produceert — bewust **stoppunt** bij de smelter, geen fase D/E.
**Welke as van het verhaal:** Australiës historische Broken Hill-lijnbreuk-ertslichaam (lood/zink/zilver) naar 's werelds grootste loodsmelter (Nyrstar Port Pirie). Prioriteit 4, M31 golf 5.

## 1 · Ketenkaart
```
Rasp-mijn/plant `ag-brokenhill-mijn` ──(b1 spoor · Crystal Brook–Broken Hill-lijn (ARTC) · 394,2 km [1])──►
   Crystal Brook-knooppunt `ag-crystal-brook-knoop` ──(b2 spoor · Bowmans Rail-vrachtlijn naar de metaalfabriek · hemelsbreed ~27,5 km, geen spoorkm gepubliceerd [3])──►
   Nyrstar Port Pirie-smelter `ag-portpirie-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ag-brokenhill-mijn` → `ag-crystal-brook-knoop` | Crystal Brook–Broken Hill railway line (ARTC-net, ex-Silverton Tramway-tracé, standaardspoor sinds 1970) | 394,2 [2] — ⚠️ Wikipedia noemt de hele lijn 371 km [1]; discrepantie ~23 km/6% niet opgelost binnen budget, zie §7 | toets_spoorroute (`BAKE_SUFFIX=-raw`, extract `australie`) | nee |
| b2 | A | spoor | `ag-crystal-brook-knoop` → `ag-portpirie-smelter` | Bowmans Rail-vrachtlijn Crystal Brook → Port Pirie ("a freight line continues to operate into Port Pirie, feeding the metals plant with raw materials from Broken Hill" [3]) | hemelsbreed ~27,5 km, geen wegkm/spoorkm gepubliceerd binnen budget [3][8] | toets_spoorroute (`BAKE_SUFFIX=-raw`, extract `australie`) | nee |

Geen last-mile-been mijn→spoor: de Rasp-verwerkingsfabriek voert het gefilterde concentraat "trucked less than a kilometre to the Rasp rail siding" [7] — ruim onder de 2 km-drempel voor een aparte stippel, dus het spoorbeen begint op het site-anker.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-brokenhill-mijn` | mijn/verwerkingsfabriek (kop van b1) | Broken Hill Mine (Rasp-mijn, Broken Hill Mines/Coolabah Metals sinds okt. 2024; voorheen Toho Zinc-groep) | -31.9486, 141.4852 | [4][6][7][9] | bron-gelegd (z15 gezien: kantoor/toegang aan Argent Street op het kruispunt; ca. 300–400 m zuidelijker een industrieel mijncomplex met gebouwen, wit uitgegraven terrein en donkere tailingsvijvers — het `w-broken-hill`-anker uit `v2/design/zilver-sitelaag.json`, letterlijk hergebruikt) |
| `ag-crystal-brook-knoop` | spoorknooppunt (splitsing ARTC-hoofdlijn → Bowmans Rail-vrachtlijn) | Crystal Brook, spoorzone rond Railway Terrace | -33.3497, 138.2020 | [1][3][10] | aannemelijk (straatnaam "Railway Terrace" uit OSM als aanwijzing voor de spoorzone; geen exact wisselpunt bevestigd binnen budget — geen satellietblik, want geen overslag maar een spoor-spoor-splitsing binnen dezelfde modaliteit) |
| `ag-portpirie-smelter` | losplek / smelter (staart, stoppunt) | Nyrstar Port Pirie-smelter | -33.1684, 138.0095 | [3][5][11] | bron-gelegd (z15 gezien: groot industrieel complex met hallen, stockpiles en spoorsporen direct aan de kade/rivierarm van de Spencer Gulf) |

## 4 · Via-punten
Geen — b1 is één doorlopend, met naam benoemd spoortracé (Crystal Brook–Broken Hill railway line) zonder gedocumenteerde corridorkeuze binnen budget; b2 is een kort feederspoor zonder alternatieve route. De splitsing tussen b1 en b2 valt samen met het knooppunt-anker in §3.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Rasp-verwerkingsfabriek (Broken Hill) | Broken Hill Mines/Coolabah Metals | erts (Rasp + Pinnacles) → lood-zilver- en zinkconcentraat (maal/flotatie/filtratie) | plant 750.000 t/j (droog erts); mijnbouwsnelheid ~30.000 t/maand bij 100% oppervlaktetrucking [7] | [6][7] |
| Nyrstar Port Pirie-smelter | Nyrstar | lood-zilverconcentraat → geraffineerd lood, zilver, koper, zuur, goud | geen vers gepubliceerd jaarcijfer binnen budget; "een van 's werelds grootste loodsmelters" [3][5] | [3][5] |

## 6 · Stoppunt
De brief stopt bij de Nyrstar-smelter in Port Pirie: dat is de fabriek die het lood-zilverconcentraat raffineert tot metaal (incl. zilver), en geen bron binnen budget noemt een specifieke vervolgzending van het geraffineerde zilver naar een LME-entrepot of beurs.

## 7 · Open punten
- **Geen vers Ag-jaarcijfer** voor de huidige Rasp-mijn/Broken Hill Mine gevonden binnen budget (bevestigt het open punt uit het ontwerp) — wel een JORC-reserve van 10,1 Mt @ 49 g/t Ag [6][7], geen gepubliceerde jaarlijkse Ag-productie of -verkoop.
- **Geen vers Ag-jaarcijfer** voor de Nyrstar Port Pirie-smelter gevonden binnen budget; Wikipedia noemt alleen dat de smelter "refined silver" produceert, zonder tonnage/peiljaar [3].
- **km-discrepantie b1**: het ontwerp geeft 394,2 km (stations-afstandstabel), Wikipedia geeft de hele Crystal Brook–Broken Hill-lijn als 371 km [1] — 6% verschil, niet verklaard binnen budget (mogelijk sluit 394,2 km het stuk mijn→Broken Hill-emplacement in). Aan de spoorrouter overgelaten om de werkelijke lengte te meten.
- **Huidige operator bevestigd, ontwerp-aanname deels achterhaald**: het ontwerp noemde "Perilya/CBH Resources-lijn" als te bevestigen operator; websearch wijst uit dat de Rasp-mijn sinds okt. 2024 eigendom is van **Broken Hill Mines / Coolabah Metals** (ASX:BHM sinds juli 2025), niet Perilya — Perilya (Zhongjin Lingnan) exploiteert een aparte, oudere Broken Hill-operatie. Welke van de twee de huidige `w-broken-hill`-anker vertegenwoordigt is niet met zekerheid vastgesteld (OSM-tag "Northern Operations" wijst mogelijk eerder naar Perilya dan naar Rasp) — zwakker punt in dit ontwerp.
- **b2-lengte is een hemelsbreed-schatting** (~27,5 km tussen het Crystal Brook-knooppunt en de smelter); geen gepubliceerde spoor- of wegkilometer gevonden binnen budget.
- **Crystal Brook-knooppunt is aannemelijk, niet satelliet bevestigd** als exact wisselpunt (geen overslag, dus geen sat_check-ronde volgens de kaart; alleen straatnaam-evidentie).

## 8 · Bronnen
[1] Wikipedia, "Crystal Brook–Broken Hill railway line" — 371 km, ARTC-net, standaardspoor sinds jan. 1970, ex-Silverton Tramway-tracé via Cockburn (1888), bypass Oodla Wirra. https://en.wikipedia.org/wiki/Crystal_Brook%E2%80%93Broken_Hill_railway_line
[2] Ketenontwerp (M31 golf 5, zie brief-invoer) — 394,2 km Broken Hill→Crystal Brook uit de stations-afstandstabel op dezelfde Wikipedia-pagina [1].
[3] Wikipedia, "Port Pirie" — "a freight line continues to operate into Port Pirie, feeding the metals plant with raw materials from Broken Hill... managed by Bowmans Rail"; smelter door Nyrstar sinds 2007, produceert lood/zilver/koper/zuur/goud. https://en.wikipedia.org/wiki/Port_Pirie
[4] Wikipedia, "Broken Hill ore deposit" — geschiedenis van de vondst (Charles Rasp, 1883), 538 miljoen oz zilver gewonnen t/m 1946. https://en.wikipedia.org/wiki/Broken_Hill_ore_deposit
[5] Wikipedia, "Broken Hill railway line" (NSW-zijde, achtergrond) — Sydney-Perth-corridor, standaardisatie Broken Hill–Port Pirie in 1970. https://en.wikipedia.org/wiki/Broken_Hill_railway_line
[6] Broken Hill Mines, "Rasp Mine" projectpagina — huidige exploitant, plantcapaciteit 750.000 tpa, JORC-reserve 10,1 Mt @ 5,7% Zn/3,2% Pb/49 g/t Ag (jan. 2024), concentraat-logistiek naar Port Pirie/Port Adelaide. https://brokenhillmines.com/projects/rasp-mine
[7] Idem [6] — detail: gefilterd concentraat "trucked less than a kilometre to the Rasp rail siding"; loodconcentraat per spoor naar Port Pirie-smelter, zinkconcentraat per spoor naar Port Adelaide.
[8] Nyrstar, "Nyrstar Port Pirie" operations-pagina — locatie Upper Spencer Gulf, 230 km noord van Adelaide, >130 jaar in bedrijf, top submerged lance/hoogovens/loodraffinage, afvoer per weg en spoor via eigen havenfaciliteit. https://www.nyrstar.com/operations/metals-processing/nyrstar-port-pirie
[9] Websearch-synthese (Australian Mining, Mining Weekly, Stockhead, Kalkine, Small Caps, sept. 2024–2026) — Broken Hill Mines (voorheen Coolabah Metals, ASX:BHM sinds juli 2025) rondde de overname van de Rasp-mijn af in okt. 2024; Perilya (Zhongjin Lingnan) exploiteert een afzonderlijke, oudere Broken Hill-operatie. https://www.australianmining.com.au/new-joint-venture-consolidates-broken-hill-mines/ · https://www.miningweekly.com/article/coolabah-to-unite-broken-hill-assets-paving-path-to-production-2024-09-17 · https://stockhead.com.au/resources/good-grasp-an-iconic-broken-hill-asset-is-returning-to-the-asx/
[10] OpenStreetMap/Photon (ODbL) — "Railway Terrace", Crystal Brook, SA, als indicatie van de spoorzone/het historische station. https://www.openstreetmap.org
[11] OpenStreetMap/Nominatim (ODbL) — "Broken Hill Mine : Northern Operations" (office=company, Argent Street) en "Nyrstar Port Pirie" (landuse=industrial). https://www.openstreetmap.org
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-zilver-brokenhill-portpirie-mijn.png`, `sat-zilver-brokenhill-portpirie-smelter.png`.

## 9 · Bakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Twee spoorbenen, 400,5 km totaal, 562 punten, 3 markers.** Geen zee/weg — de keten stopt
bij de smelter (§6). `v2/data/stroomroute-zilver-brokenhill-portpirie.json` (12,0 KB).

| # | modaliteit | km gebakken | km brief | toets | recept |
|---|---|---|---|---|---|
| b1 | spoor | 371,4 | 394,2 (stations-tabel) / ~371 (Wikipedia, hele lijn) | −5,8% tegen de brief-tabel, −0,1% tegen Wikipedia | `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=-31.9486,141.4852 --naar=-33.3497,138.2020 --naam=zilver-brokenhill-portpirie-brokenhill-crystalbrook` |
| b2 | spoor | 29,1 | hemelsbreed ~27,5, geen wegkm/spoorkm | +5,8% tegen de hemelsbreed-schatting (indicatie, geen ±15%-norm — brief zegt dat expliciet) | `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=-33.3497,138.2020 --naar=-33.1684,138.0095 --naam=zilver-brokenhill-portpirie-crystalbrook-portpirie` |

**Toelichting b1-discrepantie:** de brief vlagt zelf al een mogelijk verschil tussen de
394,2 km uit de stations-afstandstabel en Wikipedia's 371 km voor de hele
Crystal Brook–Broken Hill-lijn (§7, bron [1][2]). De spoorrouter (1-op-1-OSM-net,
`BAKE_SUFFIX=-raw`, extract `australie`) meet **371,4 km** — nagenoeg identiek aan
Wikipedia's 371 km (+0,1%) en 5,8% onder de brief-tabel. Dit bevestigt het eigen open
punt van het ontwerp (de stations-tabel omvat mogelijk een extra stuk mijn→emplacement
dat de doorlopende lijnlengte niet meetelt) en is een **bevinding, geen fout van deze
bake** — verhouding route/grootcirkel 1,07, 0 knikken ≥ 60°, 0 omkeringen.

**Toelichting b2:** kort feederspoor (Bowmans Rail) zonder gepubliceerde deellengte.
Gemeten 29,1 km tegen een hemelsbreed-schatting van ~27,5 km — de brief stelt expliciet
dat de ±15%-toets hier niet als norm geldt, alleen als indicatie. Verhouding route/
grootcirkel 1,06, 0 knikken, 0 omkeringen.

**Geen stippels, geen haven-aanloop, geen luchtbeen, geen leidingbeen** — twee
doorgetrokken, gemeten spoorbenen. Geen last-mile-been mijn→spoor (bron [7]: concentraat
"trucked less than a kilometre to the Rasp rail siding", ruim onder de 2 km-drempel);
b1 begint direct op het site-anker `ag-brokenhill-mijn`. Geen via-punten (§4: b1 is één
doorlopend benoemd tracé zonder gedocumenteerde corridorkeuze; b2 is een kort feederspoor).

**Markers:** alle drie ≤ 0,5 km van hun lijn (`ag-brokenhill-mijn` 267 m, `ag-crystal-brook-knoop`
53 m, `ag-portpirie-smelter` 393 m) — anker ≠ exact routeerpunt, binnen de norm.
`toets_knikken.py` en `toets_rechte_benen.py`: 0 knikken, 0 omkeringen, geen been in de
rechte-lijn-verdachtenlijst (beide benen hebben een omwegfactor > 1,00, dus geen stippel-
kandidaat). Naden tussen b1 en b2: 0,00 km (identiek knooppunt).

**Lessen:**
- De km-discrepantie die de brief zelf al vlagde (stations-tabel vs. Wikipedia) is door de
  meting **opgelost in het voordeel van Wikipedia** — een voorbeeld waarbij "aan de
  spoorrouter overlaten" (brief-aanwijzing) letterlijk werkte: de meting weegt zwaarder dan
  een niet-gespecificeerde bron-tabel.
- Openstaande punten uit de brief (§7) blijven onopgelost binnen dit bak-budget: geen vers
  Ag-jaarcijfer voor Rasp-mijn of Port Pirie-smelter, en welke van Broken Hill Mines/Coolabah
  Metals versus Perilya het bestaande `w-broken-hill`-anker in de sitelaag het beste
  representeert — dat is een redactievraag voor de orkestrator, geen bak-taak.
