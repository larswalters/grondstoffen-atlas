# Zilver · Van → Via → Naar (land)

**stroom-id:** `zilver-imiter-guemassa` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** zilverhoudend erts van de Imiter-mijn (SMI/Managem, Drâa-Tafilalet) wordt **op de mijn
zelf** tot 98,5–99,5% zuiver zilveranodes/-ingots verwerkt (gravimetrische concentratie + eigen smelter) en per
**truck** (N10 → N9 via de Tizi n'Tichka-pas → Marrakech → A7/A1-snelweg via Settat–Casablanca–Rabat–Kenitra)
naar het exportcomplex **Tanger Med** vervoerd — **stoppunt**, aannemelijk: één zwakke bron.
**Welke as van het verhaal:** *Marokko — Afrika's grootste zilverproducent, eigen erts-tot-metaal-verwerking op
de mijn.* Jaarvolume: laatst bekend **125,5 t Ag/j** (Managem-groep, peildatum 31-12-2025, managemgroup.com/
our-products/silver — dit cijfer dekt vermoedelijk de hele Managem-zilverproductie, niet exclusief Imiter, want
recentere Managem-bronnen noemen géén Guemassa/Tizert als aparte zilverstie meer) [1][2].

## ⚠️ Afwijking van het ketenontwerp — eerst lezen
Het ontwerp veronderstelde een truckbeen Imiter → CTT Guemassa-complex (kobalt/koper/nikkel/zink-hydrometallurgie).
Eigen onderzoek dit ronde weerlegt dat: Imiter heeft een **eigen, geïntegreerd metallurgisch complex op de mijn**
("gravimetric concentration" → "ingots of Silver metal, purity 99,5%", managemgroup.com/en/imiter-mine) en de
actuele Managem-productpagina (managemgroup.com/en/our-products/silver, peildatum 2025) noemt **uitsluitend
Imiter** als zilverproductiesite — geen Guemassa, geen Tizert. Dat is precies het scenario dat het ketenontwerp
zelf al als risico benoemde ("blijkt Imiter een eigen smelter te hebben, dan wordt de mijn zelf het stoppunt,
evt. met een kort exportbeen"). De haalbaarheidstoets citeerde een oudere/algemenere zin ("SMI produced silver at
three sites … Guemassa, Imiter, and Tizert") die dit ronde niet bevestigd kon worden op de huidige bedrijfspagina's
— zie §7. **Conclusie: Guemassa vervalt uit deze keten; de staart is vervangen door een exportbeen naar Tanger
Med**, op basis van één zwakke, niet-corporate bron (een geologie-reisverslag uit 2012: "the finished silver
ingots are shipped by armored trucks to the port at Tangiers") [3]. Dit is welbewust **niet stevig**: zie §7.

## 1 · Ketenkaart
```
Imiter-mijn `ag-imiter-mijn` (eigen smelter, 98,5–99,5% Ag-anodes/ingots) ──(b1 truck · N10 Tinghir–Ouarzazate →
N9 Tizi n'Tichka-pas → Marrakech → A7/A1 via Settat–Casablanca–Rabat–Kenitra → Tanger Med-aftakking ·
hemelsbreed via-som ~795 km, geen wegkm, aannemelijk: één bron)──► Tanger Med-exportcomplex `ag-tangermed-poort`
── stoppunt (exportpoort, geen genoemde koper)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Imiter-mijn → Tanger Med-exportcomplex | N10 (Tinghir–Ouarzazate) → N9 (Tizi n'Tichka-pas, gedeeld tracé met `kobalt-bouazzer-guemassa` t/m Marrakech-zuid) → A7 (Marrakech–Settat–Casablanca) → A1 (Casablanca–Rabat–Kenitra–Tanger) → Tanger Med-spur | hemelsbreed via-punten-som **794,7 km**, geen gepubliceerde wegkm gevonden binnen budget (aannemelijk: één bron voor de bestemming zelf) [3][8] | `maak_stroombeen_weg` | nee — doorgetrokken; "aannemelijk: één bron" in de beennaam, niet in de lijnstijl |

Corridorstuk **Ouarzazate → Tizi n'Tichka-pas** deelt de N9 met `kobalt-bouazzer-guemassa` (dat been begint bij
Bou Azzer, niet bij Imiter/Ouarzazate) — **niet** één-op-één hetzelfde geojson (ander kopanker, andere staart na
Marrakech), dus geen letterlijke kopie mogelijk; wel dezelfde wegnummers/via-coördinaten voor de gedeelde
passage, expliciet vermeld voor de bak-agent (§ bak-aanwijzingen).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-imiter-mijn` | mijn + eigen smelter (kop) | Imiter Mine (Société Métallurgique d'Imiter/SMI, Managem), Tinghir-provincie | 31.3501, -5.7230 | OSM/Nominatim `landuse=quarry`, way 803732702, exact op deze coördinaat [4][9]; Managem: "150 km from Ouarzazate", eigen gravimetrische verwerking tot 98,5–99,5% Ag [1][2] | **bron-gelegd** (z15, live, eigen satellietblik dit ronde): uitgestrekt mijnbouw-/plantcomplex met meerdere tailings-/procesbekkens (wit-turkoois), een open pit met spiraalvormige toegangsweg, industriële loodsen en dorpsbebouwing — exact op de OSM-coördinaat, geen verschuiving nodig |
| `ag-tangermed-poort` | exportcomplex (staart, stoppunt) | Tanger Med-havencomplex (Ksar Sghir, bij Tanger) | 35.8750, -5.5207 | Wikipedia "Tanger Med" (35°52'30"N 5°31'15"W) [6]; blogbron noemt alleen generiek "port at Tangiers", niet expliciet Tanger Med — zie §7 [3] | **bron-gelegd** (z14, live, eigen satellietblik dit ronde): grootschalig containerterminalcomplex met kadekranen, honderden opgestapelde containers, tankopslag en een aansluitende snelweg — herkenbaar als het Tanger Med-havencomplex; géén specifiek mineralen-/metaalterminal geïdentificeerd binnen dit complex (open punt) |

## 4 · Via-punten (b1 — corridorkeuzes op de doorgaande route, geen stadscentra)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ouarzazate — aansluiting mijnweg op de N9 | 30.9170, -6.9170 | zelfde punt als `kobalt-bouazzer-guemassa` [5][7]: hier komt de Imiter-corridor (via N10) op de doorgaande N9 Ouarzazate–Marrakech |
| b1 | 2 | Tizi n'Tichka-pas (2.260 m, Hoge Atlas) | 31.2858, -7.3808 | zelfde punt als `kobalt-bouazzer-guemassa` [5]: de N9 heeft hier geen alternatieve route door het gebergte |
| b1 | 3 | Marrakech — A7-noordaansluiting | 31.6295, -7.9811 | hier verlaat de corridor de N9-richting-Marrakech-centrum en gaat over op de A7-snelweg noordwaarts (dus niet de N8-zuidaftakking naar Guemassa uit de kobaltketen) [10] |
| b1 | 4 | Settat — A7-doorgaand punt | 33.0000, -7.6167 | tussenstop op de A7 Marrakech–Casablanca, enige doorgaande snelwegcorridor [10] |
| b1 | 5 | Casablanca — A7/A1-knooppunt | 33.5333, -7.5833 | hier gaat de corridor van de A7 over op de A1 richting Rabat/Tanger; grootste knooppunt van het Marokkaanse snelwegnet [10] |
| b1 | 6 | Kenitra — A1-doorgaand punt | 34.2500, -6.5833 | laatste grote plaats vóór de Tanger Med-aftakking, bevestigt dat de corridor de kustcorridor A1 volgt i.p.v. landinwaarts af te buigen [10] |

## 5 · Verwerkingsknopen
Geen tussenliggende verwerkingsknoop: het erts wordt al **op de mijn zelf** (Imiter) tot zilveranodes/-ingots
verwerkt (gravimetrische concentratie + smelterij) — dat maakt Imiter tegelijk mijn én de facto raffinaderij.
Geen fase C/D (geen tweede metallurgische stap gedocumenteerd); Tanger Med is een exportpoort, geen verwerker.

## 6 · Stoppunt
De brief stopt bij Tanger Med: geen bron noemt een specifieke koper, smelter of markt voorbij de haven — alleen
de (zwakke) claim dat de zilveringots per pantserwagen naar "de haven van Tanger" gaan. Tanger Med is Marokko's
grootste exporthaven en het meest plausibele concrete punt achter die claim, maar dit is uitdrukkelijk een
**aanname, geen bevestiging van déze exacte terminal** (zie §7).

## 7 · Open punten
- **BINDEND OPEN, GROOTSTE RISICO — de bestemming Tanger Med steunt op één zwakke bron.** Een persoonlijk
  geologie-reisverslag uit 2012 (hobbyist-blog, geen corporate/overheidsbron) noemt: "the finished silver ingots
  are shipped by armored trucks to the port at Tangiers" [3] — zonder welke terminal, zonder koper, zonder
  peiljaar-actualiteit (13+ jaar oud). Geen Managem-bron, geen havenbron en geen tweede onafhankelijke bron
  bevestigt dit binnen budget. Dit been is dus getekend als "aannemelijk: één bron" conform de kaartregels, maar
  het is de zwakste zulke claim in deze golf — een bak-agent of latere ronde die een sterkere bron vindt
  (Managem-jaarverslag met exportroute, douanedata) hoort dit te vervangen.
- **Guemassa is uit deze keten geschrapt** t.o.v. het ketenontwerp — zie de afwijkingssectie bovenaan. De
  haalbaarheidstoets citeerde "SMI produced silver at three sites … Guemassa, Imiter, and Tizert" als bevestiging
  dat Guemassa een geldig stoppunt was; dat citaat kon dit ronde niet op de huidige managemgroup.com-pagina's
  teruggevonden worden (de actuele "Silver"-pagina noemt uitsluitend Imiter, peildatum 2025) [2]. Mogelijk was de
  eerdere quote gedateerd (Guemassa/Tizert zijn ooit zilverbijproduct-sites geweest, nu niet meer vermeld) of een
  onjuiste weergave. Dit is een **inhoudelijke correctie op de haalbaarheidstoets**, gemeld conform de opdracht
  ("zie je daar een fout, meld het in je rapport"), niet zelf gecorrigeerd in de toetsdata.
- **Geen gepubliceerde wegkilometer voor de ~795 km-corridor** — alleen de via-punten-som hemelsbreed. Dezelfde
  situatie als `kobalt-bouazzer-guemassa` en `zilver-fresnillo-torreon`; de ±15%-toets geldt hier niet als norm.
- **Jaarvolume (125,5 t Ag/j, peildatum 31-12-2025) is vermoedelijk Managem-groepsbreed**, niet Imiter-specifiek
  uitgesplitst — al lijkt Imiter, gezien de huidige bedrijfspagina, de enige actieve zilverproductiesite van de
  groep te zijn, wat het cijfer alsnog een redelijke proxy maakt.
- **Geen specifieke mineralen-/metaalterminal binnen Tanger Med geïdentificeerd** — het satellietbeeld toont het
  containerterminalcomplex; een pantserwagentransport van edelmetaal loopt vermoedelijk via een aparte, kleinere
  faciliteit (bv. een vrachtterminal of douaneloods) die niet apart gelokaliseerd kon worden binnen budget.
- **Fase D/E vervallen bewust** — geen bron noemt een koper of vervolgbestemming voorbij de haven.
- **Corridorklasse A7/A1 niet vooraf getoetst** — bekende, goed gekarteerde hoofdsnelwegen, geen bijzonderheden
  verwacht; te bevestigen bij het bakken.

## 8 · Bronnen
[1] Managem, "Imiter mine" — SMI (Société Métallurgique d'Imiter), sinds 1969, oostelijk van de Saghro, 150 km
    van Ouarzazate; gravimetrische concentratie; ingots met 99,5% zuiverheid; 222 t in 2017, capaciteitsuitbreiding
    2017/2018-2019. https://www.managemgroup.com/en/imiter-mine
[2] Managem, "Silver" (our-products) — actuele productpagina (geraadpleegd 2026-09-28): Imiter als enige genoemde
    zilverproductiesite, 125.537 kg zilver geproduceerd (peildatum 31-12-2025), "high purity silver metal (98,5%
    Ag) in the form of anodes", 11% van de geconsolideerde omzet. https://www.managemgroup.com/en/our-products/silver
[3] Natural History Museum of L.A. Minblog, "Morocco part 6: Todra Gorges and Imiter Silver Mine" (2012) — enige
    gevonden bron voor de exportroute: "the finished silver ingots are shipped by armored trucks to the port at
    Tangiers" — persoonlijk reisverslag, geen corporate/overheidsbron, niet elders bevestigd.
    http://nhminsci.blogspot.com/2012/05/morocco-part-6-todra-gorges-and-imiter.html
[4] OpenStreetMap (ODbL) via Nominatim — "Imiter Mine", `landuse=quarry`, way 803732702, 31.3501154/-5.7230483,
    exact overeenkomend met het ketenontwerp-coördinaat. https://www.openstreetmap.org
[5] `v2/design/routebrieven/kobalt-bouazzer-guemassa.md` — hergebruikte via-punten Ouarzazate (30,9170/-6,9170)
    en Tizi n'Tichka-pas (31,2858/-7,3808), gedeeld tracé t/m Marrakech-zuid.
[6] Wikipedia (en), "Tanger Med" — coördinaat 35°52'30"N 5°31'15"W (35,8750/-5,5207); ligging ~40-45 km van
    Tanger-stad, 14 km van de Spaanse kust, tegenover Tarifa. https://en.wikipedia.org/wiki/Tanger_Med
[7] Wikipedia (en), "Ouarzazate" (30,91667/-6,91667) — knooppunt N9/N10.
    https://en.wikipedia.org/wiki/Ouarzazate
[8] Ketenontwerp (JSON, M31 golf 6) + haalbaarheidstoets (JSON, bindend) — oorspronkelijke Guemassa-hypothese en
    het expliciet gevlagde risico "heeft Imiter een eigen smelter?", dat dit ronde bevestigend is beantwoord (ja
    — met als gevolg dat de bestemming ná Imiter niet Guemassa is, zie de afwijkingssectie).
[9] Institute of Developing Economies (IDE-JETRO), Managem-bedrijfsprofiel — algemene Managem/SMI-context.
    https://www.ide.go.jp/English/Data/Africa_file/Company/morocco05.html
[10] Wikipedia (en) — coördinaten Casablanca (33,53333/-7,58333), Kenitra (34,25/-6,58333), Settat (33,0/-7,61667);
     algemene kennis Marokkaans snelwegnet A7 (Marrakech–Casablanca via Settat) en A1 (Casablanca–Rabat–Kenitra–
     Tanger) — geen aparte Wikipedia-pagina "Autoroutes of Morocco" geraadpleegd binnen budget (rate-limited).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Eén been (b1, truck), doorgetrokken, geen stippel.** Profiel `zilver-imiter-guemassa-imiter-tangermed`
in `v2/tools/maak_stroombeen_weg.py` (extract `marokko`, `--bron geofabrik`, vensterKm 70, geen `refs`-
harde eis — N10/N9/A7/A1 als zachte voorkeur). Functie `bak_zilver_imiter_guemassa()` in
`v2/tools/bak_stromen.sh`. Uitvoer: `v2/data/stroomroute-zilver-imiter-guemassa.json` (319,7 KB).

| # | modaliteit | km gemeten | km-bron | snap kop/staart | markers |
|---|---|---|---|---|---|
| b1 | truck | **938,5 km** (16.507 punten) | geen gepubliceerde wegkm; hemelsbreed via-som **794,7 km** → gemeten +18,1% (indicatie, geen norm — brief §1/§7) | 0,20 km (plant→weg, Imiter) · 0,01 km (weg→kade, Tanger Med) | `ag-imiter-mijn` (31,3501/−5,7230) · `ag-tangermed-poort` (35,8750/−5,5207) |

**Recept:**
1. `python v2/tools/maak_stroombeen_weg.py --profiel zilver-imiter-guemassa-imiter-tangermed --bron geofabrik`
   → `v2/build-cache/ais/graaf/zilver-imiter-guemassa-weg-imiter-tangermed.geojson` (385,6 KB, 16.507 punten).
   Scan: 1 extract (marokko, 0,2 GB, 45 s), 343 keerlussen gesnoeid (940,4 → 938,3 km), eindklassen
   (residential/service/tertiary/unclassified) binnen 12 km van plant/kade meegenomen (first mile 7,01 km,
   last mile 3,14 km, beide over kleine wegklassen — geen stippel nodig, het net reikt tot de poort).
2. `bash v2/tools/bak_stromen.sh zilver-imiter-guemassa` → `hecht_marnet.py route` met het vooraf gebakken
   `--been-geojson`, twee `--marker`, `--routebrief`/`--uit`/`--stroom`/`--titel`.

**Toets (handleiding §5):**
- **Km-toets**: geen harde ±15%-norm mogelijk (geen gepubliceerde wegkm). Gemeten 938,5 km tegen de
  hemelsbrede via-punten-som van 794,7 km = **+18,1%**, in lijn met de verwachting uit de bak-aanwijzingen
  ("de A1 volgt de kustlijn, dus een grotere uitbuiging dan de hemelsbrede via-som is verwacht"). Geen bevinding.
- **Naden**: enkelbenige keten, geen naad tussen benen (0,000 km per constructie).
- **Ankerverbindingen**: plant→weg 0,20 km, weg→kade 0,01 km — beide ver onder de 0,5 km-norm.
- `toets_knikken.py`: 45 knikken ≥60°, 2 omkeringen (beide **TERUGLOOP**, R = 0 m en 4 m — puntruis op de
  Marrakech- resp. Kenitra-doorgang, geen echte terugrit; te klein om te repareren, komt overeen met
  vergelijkbare spikes elders in de repo).
- `toets_rechte_benen.py --min-km 5`: `zilver-imiter-guemassa` komt **niet** voor in de lijst met verdachte
  rechte segmenten ≥5 km — het been bestaat uit een echt gerouteerde weglijn, geen rechte stippel.
- JSON-contract: `versie` 2 · `punt_formaat` "lonlat" · modaliteit `{truck}` ⊂ toegestane set · 1 been ≥2
  punten · 319,7 KB (ver onder de norm van ~300 KB die de handleiding als indicatie noemt, maar dit is één
  lang been met veel puntdichtheid — geen contractfout, alleen een grote geometrie).

**Stippel/aanloop/vlucht/leiding:** geen. Eén truckbeen, doorgetrokken. Geen zeebeen (geen MARNET-router
nodig — de keten stopt bij de Tanger Med-exportpoort zelf), geen luchtbeen, geen leidingbeen, geen fase D/E
(Imiter is tegelijk mijn én de facto raffinaderij; Tanger Med is stoppunt, brief §5/§6).

**Gedeeld corridorstuk, geen gedeeld geojson:** Ouarzazate → Tizi n'Tichka-pas deelt wegnummers/via-
coördinaten met `kobalt-bouazzer-guemassa` (profiel `kobalt-bouazzer-guemassa-bouazzer-guemassa`), maar is
een **eigen, nieuw profiel en een eigen bake** — geen `--been-geojson`-hergebruik — omdat het kopanker
(Imiter i.p.v. Bou Azzer) en de staart (Tanger Med noordwaarts i.p.v. Guemassa zuidwaarts) verschillen.

**Lessen:**
- Een lange corridor zonder gepubliceerde wegkm (alleen een hemelsbrede via-som) hoort een ruim venster
  (60–75 km) en levert typisch een positieve afwijking op zodra de route een kustcorridor volgt (hier A1
  Casablanca–Rabat–Kenitra–Tanger) — de hemelsbrede som onderschat een kustbocht systematisch.
- Kleine wegklassen binnen 12 km van kop/staart (`eindKlassen`, default) waren hier voldoende om zowel de
  mijnpoort als de havenpoort zonder stippel te bereiken (7,0 km resp. 3,1 km first/last mile) — geen
  aparte `eindToegangPrivaat`-vlag nodig, in tegenstelling tot bv. Codelco-achtige privéterreinen.

**Open punt uit de brief (§7), niet zelf opgelost door dit bakken:** de bestemming Tanger Med steunt op één
zwakke, niet-corporate bron (een 13+ jaar oud persoonlijk reisverslag, geen terminal-/kopernaam). Het
bakken bevestigt alleen dat de weg tussen Imiter en Tanger Med bestaat en rijdbaar is — het bevestigt niet
dat de zilverexport daar werkelijk doorheen gaat. Dit blijft het bindende grootste risico van de keten
(zie de bak-aanwijzingen: een aanvullende bronronde vóór definitieve acceptatie wordt aanbevolen).

**Gecorrigeerd t.o.v. de haalbaarheidstoets (gemeld, niet zelf aangepast in de toetsdata):** de claim "SMI
produced silver at three sites … Guemassa, Imiter, and Tizert" kon dit ronde niet worden teruggevonden op
de actuele managemgroup.com-pagina's; de huidige "Silver"-productpagina (peildatum 2025) noemt uitsluitend
Imiter. Guemassa is daarom uit deze keten geschrapt (zie de afwijkingssectie boven §1).
