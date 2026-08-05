# Bugs & risks — Grondstoffen Atlas
*Last updated: 2026-08-05 (nieuw: zoomplafond bij Guixi, productconflict Beilun, been-ids ontbreken)*

## ⚠️ OPEN 2026-08-05 (laatst, 2e sessie) — koper: drie punten die niet dicht zijn

1. **De kathode-expeditie op het 贵冶-complex is niet gevonden — en dat is een ZOOMPLAFOND, geen
   zoekprobleem.** Esri heeft bij Guixi geen z19 (`Map data not yet available`, drie agents
   onafhankelijk); via Wayback is uitgesloten dat het aan de opnamedatum ligt, en geen enkele bron
   koppelt 电解车间 of 成品库 aan een gebouw. Gevolg: de kop van been 5 is een substituut en er
   staat een bewust **procesgat van 0,584 km**. Vervolgweg: een niet-Esri-bron (Sentinel-2,
   Tianditu-token, of een bedrijfspublicatie met plattegrond).
2. **PRODUCTCONFLICT BIJ BEILUN — container of bulk?** Wat op 北仑港站 satelliet-gelegd is, is een
   **container**emplacement (78万TEU, vier rail-mounted portaalkranen, containerwagons), terwijl
   ladder L3 van de routebrief zegt: *concentraat, natte bulk in open wagons*. Twee onafhankelijke
   agents zagen hetzelfde beeld. `cu-beilun-laadspoor` is dus **geografisch waterdicht en
   inhoudelijk voorwaardelijk**. Dit is een vraag aan de brief, niet aan de satelliet — beslis hem
   vóórdat fase C herschreven wordt.
3. **Twee tegenstrijdige kandidaten voor het terreincentrum van 铜材公司.** Het registerpunt ligt
   tússen twee aangrenzende blokken; welk blok de walsdraadfabriek is, is op z18 niet te beslissen.
   Voor de lijn maakt het niet uit (het aansluitpunt op de hoofdas is gelegd), voor een
   registerknoop wel — daarom is er bewust géén node in `data/copper.js` bijgekomen.

## ⚠️ OPEN 2026-08-05 — structureel, raakt alle vijf de stromen

- **Been-ids ontbreken in álle vijf gebakken stromen** terwijl werkwijze §2 ze eist
  (`<stroom-id>-b<n>`) en `hecht_marnet route` er geen vlag voor heeft. De brieven dragen ze wel,
  de uitvoer niet — dus is een been in het gebakken bestand niet terug te vinden in zijn brief.
- **"Been eindigt op zijn routeerpunt en niet op zijn anker" is niet Beilun-specifiek.** Gemeten
  gaten die op dezelfde behandeling wachten: `collahuasi-tongling` **1.818 m** en
  `lithium-greenbushes-zhangjiagang` **4.933 m**.
- **De bak-recepten van drie stromen staan nog steeds nergens** (`collahuasi-tongling`,
  `lobito-duisburg`, `lithium`). ⚠️ Herbak ze niet zonder eerst de huidige uitvoer te bewaren.

## ⚠️ OPEN 2026-08-05 (eerder) — drie terugloopjes in de grafietketen

Van de 25 omkeringen zijn er **3 een echte terugloop** (de lijn legt dezelfde weg terug):

| plek | verhouding | status |
|---|---|---|
| Napoleon Ave, start bargebeen | 10,2 | **bestond al** vóór deze ronde |
| tweede punt in het bargebeen | ≥ 2,2 | nieuw |
| North Little Rock, I-30 → I-40 | 3,0 | nieuw |

De overige 22 zijn **werkelijkheid** en horen niet gerepareerd te worden. Gebruik
`toets_knikken.py` en kijk naar de terugloop-kolom, niet naar het omkeringen-totaal.

## ⚠️ GEFIXT 2026-08-05 — de meetlat stond te streng, en dat leek een regressie

Na het herbakken sprongen de omkeringen **12 → 28**. Dat las als een regressie en had bijna tot
het terugdraaien van goed werk geleid. De maat ontbrak: `toets_knikken.py` was geijkt op **spoor**,
waar een trein fysiek niet kan omkeren, dus daar is elke hoek ≥ 150° per definitie verzonnen
geometrie. Op weg en water niet — een klaverbladlus, een sluispassage en een duwstel dat in een
doodlopend zijkanaal omdraait zijn echte 180°-bochten.

**Fix:** de verhouding pad ÷ hemelsbreed over een venster van ±8 punten. Terugloop blijft ter
plaatse (3,0 en 10,2), een echte bocht komt ergens uit (1,1–2,0). Uitslag: 25 omkeringen waarvan
**3 terugloop** — en de vier oudere stromen hebben er **nul**, dus ook de "12" waar we weken naar
keken waren grotendeels echte bochten.

⚠️ **Zoek dezelfde klasse elders:** elke toets die op één modaliteit is geijkt en ongewijzigd op
een andere draait, kan systematisch vals alarm geven.

## ⚠️ RISICO 2026-08-05 — generator↔uitvoer-drift, derde verschijning

Het wegbeen `stroombeen-balama-nacala.geojson` op schijf stond op **502,7 km**; opnieuw bakken
geeft **497,9**. Oorzaak: `snoei_keerlussen` kwam er op 30-07 bij voor de lithiumbrief en raakt
dit been ook. Het bestand op schijf was dus **niet meer wat zijn eigen generator produceert**.

Getoetst door het oude gereedschap terug te zetten en opnieuw te bakken — zelfde nieuwe uitkomst,
dus de drift is **pre-existent** en niet door de eindklassen-wijziging veroorzaakt.

⚠️ **De vier andere stromen dragen dit risico nog steeds**: hun recept staat nergens vastgelegd,
dus niemand kan controleren of hun gebakken bestand nog matcht met het gereedschap van vandaag.
Herbak ze niet zonder eerst de huidige uitvoer te bewaren.

## ⚠️ LET OP 2026-08-05 — agent-rapporten kunnen vals alarm bevatten

Een onderzoeksrapport meldde dat **pyosmium op deze machine geblokkeerd** zou zijn door
applicatiebeleid, wat `fetch_landnet.py`, `fetch_service_lastmile.py` en `toets_ankers.py` zou
breken. Zelf nagelopen: de module importeert en laadt gewoon. Het was een beperking van de
omgeving waarin de agents draaiden, niet van de machine. **Loop een gemelde infrastructuurstoring
zelf na vóór je hem doorgeeft of ernaar handelt.**

## ⚠️ GEFIXT 2026-07-30 (laatst) — `maak_aansluitingen.py` kon alleen draaien door een projectregel te overtreden

De generator las `marnet.bin`/`marnet.json` uit **`v2/data/`** — precies waar ze sinds de
schone-bol-bake van 24-07 **niet mogen staan**, want de bol mag het waternet niet laden.
`hecht_marnet.py` schrijft dat in zijn eigen bestandskop en levert daarom een `--marnet`-vlag
die naar `v2/build-cache/marnet-preais` wijst. De regeneratie van 28-07 kan dus alleen met een
tijdelijke kopie in `v2/data/` zijn gedaan.

**Waarom dit erger is dan een ontbrekend pad:** het is één laag boven de `cu-guixi-spoor`-drift
van 741 m. Daar liep de *data* uit de pas met haar generator; hier liep het **gereedschap** uit
de pas met de architectuur — en het lek werd pas zichtbaar op het moment dat iemand hem twee
sessies later weer nodig had. Een tool die alleen draait als je een projectregel overtreedt is
kapot, ook als hij toevallig het goede antwoord gaf.

**Fix:** dezelfde `--marnet`-vlag als `hecht_marnet.py`, default `v2/build-cache/marnet-preais`,
plus een leesbare fout mét het herstelcommando (`git show pre-ais-net:v2/data/marnet.json > …`).

⚠️ **Zoek dezelfde klasse elders:** elk gereedschap dat na de schone-bol-bake nog een pad in
`v2/data/` hardcodeert naar een verwijderd bestand faalt pas bij gebruik, niet bij de bake.

## ⚠️ RISICO 2026-07-30 — een gegenereerd bestand kan ouder zijn dan zijn invoer

`aansluitingen.json` was van 28-07, het landnet van 29-07 (junctie-fix + 10 m-simplify). Bij de
regeneratie veranderde daardoor één snap: `coal-bolivar-kade` spoor **0,67 → 0,28 km**. Geen bug
— het `gemeten`-blok is per ontwerp een **rapport** — maar wel een val bij het lezen: een
snap-getal uit een gegenereerd bestand hoort bij het netstadium van zijn generatiemoment, niet
bij het huidige. Noem bij een snap-vergelijking dus altijd de bake-datum, net zoals de werkregel
van 28-07 dat voor lengtemetingen eist (gereedschap + beide eindpunten + netstadium).

## ⚠️ GEFIXT 2026-07-30 — een hardgecodeerd profiel gaf een LEGE uitvoer zonder foutmelding
`maak_stroombeen_weg.py` stond hardgecodeerd op Balama→Nacala **inclusief de extract-lijst**
(`["mozambique"]`). De eerste lithiumrun scande dus Mozambique en meldde keurig "0 km, geen
wegen in het venster" — geen exception, geen exitcode, alleen een leeg been. Nu profiel-gestuurd
(`PROFIELEN` + `--profiel`) met `extracts = CORRIDOR["extracts"]`. **Klasse:** een generator die
op de verkeerde invoer draait en dat als een geldig-maar-leeg resultaat rapporteert.

## ⚠️ GEFIXT 2026-07-30 — de lengtetoets liep vóór de keerlus-snoei
Gemeld 88,1 km op een lijn die 82,9 km is: de 5 km die de router heen-en-weer reed telde mee.
De snoei staat nu vóór de toets en `rap["km"]` wordt herberekend op de gesnoeide punten.
**Klasse:** dezelfde als de `toets_spoorroute.mjs`-fout van 28-07 — meet het eindproduct, niet
je meetlat.

## ⚠️ GEFIXT 2026-07-30 — 89 minuten scanwerk weggegooid door een print naar stdout
De China-OSM-scan crashte op `UnicodeEncodeError: 'charmap' codec` (Windows-console = cp1252)
bij het eerste Chinese teken, ná 89 minuten werk; alle treffers waren weg. `vind_osm.py`
schrijft resultaten nu naar een bestand met expliciete `utf-8` en print alleen een
ASCII-samenvatting. **Risico blijft** voor elk script dat niet-ASCII naar de console schrijft.

## ⚠️ OPEN 2026-07-30 — Shed 8-8 (Bunbury) is met Esri niet te leggen
De loods is jonger dan élke Esri-capture: de nieuwste Wayback-release (2026-06-30, van 195) is
identiek aan de live laag. Dit is een **nieuwe faalmodus van de satellietpass**: niet "verkeerd
gezocht" maar "de opname is ouder dan de infrastructuur". Vraagt Sentinel-2 of een
havenplattegrond. Zelfde risico geldt voor elk recent gebouwd anker.

## ⚠️ OPEN 2026-07-30 — twee Chinese fabrieksankers ontbreken, benen 5–8 daarom niet getekend
东新路 5 号 (Tianqi, Zhangjiagang) en 锡梅路 167 号 (LG Chem–Huayou, Wuxi) staan niet in OSM; een
volledige scan over de china-extract vond ze niet (de LG-cluster in Nanjing wél). De lithiumketen
stopt daarom op de kade van Zhangjiagang. Bewuste keuze, geen bug — maar wel een open eind.

## ⚠️ OPEN 2026-07-29 — de bak-commando's van de vier stromen zijn nergens vastgelegd
`hecht_marnet route` is been-gestuurd (`--been` / `--stippel` / `--been-geojson` /
`--marker`), maar wélke vlaggen er per stroom zijn gebruikt leeft uitsluitend in een
shell-historie. Wie een stroom wil herbakken moet het commando reconstrueren uit de
routebrief en het gebakken JSON. Dezelfde klasse als de generator-drift van
`cu-guixi-spoor` (741 m): een gegenereerd artefact waarvan het recept niet is vastgelegd
loopt stil uit de pas. Vastleggen als scriptje naast de routebrieven vóór de volgende
herbake.

## ⚠️ OPEN 2026-07-29 — 12 omkeringen over de vier stromen, waarvan 11 buiten het spoor
`toets_knikken.py` telt ze in de **gebakken** stromen. Na de 1-op-1-omzetting staat het
spoorbeen Beilun→Guixi op **1** (28.3429/117.1975 — tweede spoor 6–16 m naast de
hoofdlijn over 5,3 km). De overige **11 zitten in zee-, rivier- en truckbenen** en komen
dus uit heel andere bronnen (MARNET, AIS-tracks, wegcorridors): 180° op het
grafiet-truckbeen bij −14.9147/40.2954, vier op het zeebeen Southwest Pass → New
Orleans, twee op het Rijnbeen. Eigen ronde per bron; niet met de spoorfix mee te nemen.

## ⚠️ RISICO 2026-07-29 — de oude machinerie staat nog naast de nieuwe
`dedup_parallel`, de heal-passes en `vind_omweg_connectoren` bestaan alléén om schade te
repareren die de oude volgorde (simplify vóór knopen) aanrichtte. Zolang `hecht_marnet`
nog op zijn eigen graaf routeert en alleen het losse spoorbeen op 1-op-1 draait, staan
er **twee netten met verschillende topologie** naast elkaar. Niet schrappen vóór de
baker zelf op 1-op-1 draait — maar ook niet vergeten dat ze er staan.

## ⚠️ OPEN 2026-07-29 — Cerrejón in de Schwelgern-cokesblend is niet gedocumenteerd
Uit de fase D/E-research van de kolen-brief (A–E-omzetting): de gedocumenteerde
Cerrejón→Duitsland-stroom is **krachtwerkkool** (RWE/STEAG/EnBW, ±31% importaandeel);
geen enkele bron legt Cerrejón-kool expliciet in de cokesblend van de Kokerei
Schwelgern. De keten pier→kokerei→hoogovens→OSW 1 klopt fysiek (één tk-terrein), maar
de grondstof-koppeling voor dít been is een open punt (§5 van de brief). Uitzoeken vóór
de Cerrejón→Ruhr-stroom op de bol gebakken wordt — anders tekent de atlas een stroom
waarvan het laatste been niet bij deze mijn hoort.

## ✅ OPGELOST 2026-07-28 (laatst) — vier dingen die Lars op de bol zag
Alle vier eerst gemeten, toen pas gefixt. Ze horen bij elkaar want ze verklaren waarom
een lijn "er net naast" of "onmogelijk" oogt terwijl de route klopt.

1. **Bochten die een trein niet kan maken.** De Dijkstra in `toets_spoorroute.mjs` kende
   geen draaikosten, dus omkeren was gratis: het pad reed een aftakking op en meteen
   terug als dat meters scheelde. Gemeten op Beilun→Guixi: 7 knikken ≥60°, waarvan vijf
   keerpunten van 158-176° met boogstralen van **27, 35, 80, 159 en 554 m**. Nu routeert
   hij over GERICHTE edge-toestanden met een bochtstraf (`--keerstraf`, default 25 km).
   ⚠️ **De hoek alleen volstond niet:** een knik van 77° met segmenten van 15 en 993 m
   heeft op het gemiddelde een boogstraal van 400 m (lijkt echt) maar op de KORTSTE kant
   10 m (een wissel-spike). Sinds de kortste kant telt: 7 → **3** knikken, en die drie
   zijn omkeringen op precies de plekken waar een trein kopmaakt (Ningbo Oost, Guixi
   station, het doodlopende fabrieksspoor — die laatste overleeft ook een straf van
   120 km). Route 550,5 → **553,7 km** tegen ~556 km in de brief.
2. **Een been van twee punten liep dwars door de aarde.** Twee punten worden in 3D een
   rechte KOORDE, en over 153 km duikt die **0,46 km onder het oppervlak** — daarom zag
   Lars geen leiding bij Escondida. `stroomroute.js` verdicht benen nu langs de
   grootcirkel (5 km): 2 → 32 punten, zakking 460 → **0 m**.
3. **130 m parallax.** De tegels liggen niet op `radius`: basisschil 1,0 · middenring
   1,00001 · **detailpatch 1,00002** (tiles.js). Je keek dus naar beeld 130 m bóven de
   vectorlijnen, en schuin bekeken projecteert dat als zijdelingse verschuiving — recht
   van boven niet zichtbaar. Alle vectorlagen staan nu op `CONFIG.vectorLift`, exact de
   schil van de diepste tegels.
4. **De Lobito-stroom begon aan de kust** terwijl het koper uit de Copperbelt komt.
   Spoorbeen Kamoa-Kakula → Lobito erbij: **1.688,8 km** tegen de operator-waarde
   ~1.750 km (−3,5%), plus 12,6 km gestippelde aanvoer mijn→railhead.

## ⚠️ OPEN — het tracé van de Escondida-leiding staat niet in OSM
Gemeten, niet aangenomen: **0 ways met `substance=slurry`**, en een Dijkstra over
**1.319 weg-ways in een corridor van 8 km** vindt géén doorlopend pad terwijl beide
uiteinden op 50 m snappen. Wel 13,9 km óngetagde pipeline aan de Coloso-kant
(way/1530915724 + way/1530915728) — kandidaat, maar zonder substance-tag geen bewijs.
Het been blijft dus gestippeld mét de reden in het label. Wie het exact wil: satelliet-
tracen zoals de Tongling-oostgeul (~166 km handwerk). ⚠️ Bij **Collahuasi** is dit géén
probleem: die leiding ligt al exact op 192,4 km echte OSM-geometrie.

## ✅ OPGELOST 2026-07-28 (laatst) — de zeven goedgekeurde ankercorrecties zijn DOORGEVOERD
Systematisch, niet incidenteel: over vier stromen stond **10 van de 16** laadplek-/
overslag-/losplek-ankers verkeerd, van **42 m tot 4,5 km**. Lars keurde alle zeven
voorstellen goed op 2026-07-28 en ze staan nu in de data.

**Waar:** de zes koper-ankers in `v2/tools/maak_aansluitingen.py` (de redactionele
lijst = bron van waarheid) → daaruit `v2/data/aansluitingen.json` opnieuw gegenereerd
mét verse snap-metingen; `gr-port-neworleans` in `data/graphite.js`; de grafietketen
herbakken (`hecht_marnet.py route` → `v2/data/stroomroute-pilot.json`), live `?v=098`.

**Onafhankelijke bevestiging uit de snap-meting** (die is niet gestuurd door het oog
dat de kade aanwees): Waalhaven zee **1,79 → 0,70 km**, binnen 0,40 → **0,20**, spoor
1,1 → **0,0** · Guixi spoor 0,1 → **0,0** · Beilun zee 2,4 → **1,3**.

⚠️ **Eén meting werd slechter, en dat hoort hier te staan:** Beilun's SPOOR-snap ging
van 0,2 naar **1,3 km**. Logisch — de berth ligt in het water, het havenspoor eindigt
bij het ertsveld — maar het laat zien dat één aansluiting niet tegelijk ligplaats én
laadspoor kan zijn. Gaat dat knellen, dan hoort er een tweede aansluiting te komen
(werkwijze §3.4: de last mile is een eigen been), geen compromis-coördinaat ertussenin.

⚠️ **Drift gevonden en hersteld tijdens het doorvoeren:** `cu-guixi-spoor` stond in
`aansluitingen.json` op de satelliet-bevestigde ertslosbundel (117,226/28,3271, commit
`73cf5d2`) maar in de GENERATOR nog op het oude polygoon-middelpunt
(117,2257/28,3338) — 741 m ernaast. Een regeneratie zou het goede punt stil hebben
teruggedraaid. De generator is nu de waarheid. **Les: als een gegenereerd bestand met
de hand wordt bijgewerkt, loopt de generator stil uit de pas — controleer bij elke
regeneratie eerst het verschil generator↔uitvoer.**

De doorgevoerde paren, voor de historie:

| anker | stond op | staat nu op |
|---|---|---|
| `cu-escondida-laad` | -69,07169 / -24,27004 (ín de open put) | **-69,0600 / -24,2620** (concentrator + indikkers) |
| `cu-coloso-kade` | -70,46332 / -23,76015 (kustweg bij het dorp) | **-70,4652 / -23,7569** (kop laadsteiger) |
| `cu-beilun-kade` | 121,87573 / 29,92742 (transportband aan land) | **121,8830 / 29,9364** (losberth met ertslossers) |
| `cu-patache-kade` | -70,19773 / -20,80503 (wal) | **-70,1989 / -20,8027** (ligplaats) |
| `cu-rotterdam-kade` | 4,39341 / 51,89369 (dijk bij Heijplaat) | **4,4585 / 51,8935** (RHB-kade, Waalhaven Noordzijde 4) |
| `cu-duisburg-kade` | 6,7559 / 51,45187 (in het bekken) | **6,7565 / 51,4518** (kade met stukgoedstapels) |
| `gr-port-neworleans` | -90,1105 / 29,9165 (landzijde vóór het rangeerterrein) | **-90,1120 / 29,9123** (containerkade) |

⚠️ **Napoleon Ave schoof 490 m en dát is de zee→barge-overslag** — daarom is de keten
herbakken. Gemeten gevolg: het zeeschip-been Southwest Pass → New Orleans 193,2 →
**191,1 km**, de barge-start verhuist mee (beide benen delen exact hetzelfde punt), en
de overslagmarker ligt nu **56 m** van het geroutete overslagpunt in de vaargeul in
plaats van ~490 m. De keten als geheel 18.072,3 → **18.070,3 km**. Het routeerpunt zelf
schuift maar 154 m, want een schip vaart in de geul en niet tegen de kade — dat verschil
tussen ANKER en ROUTEERPUNT hoort men te kennen vóór men zich verbaast over "maar 154 m".

## ⚠️ OPEN — drie ligplaatsen niet aanwijsbaar op de beschikbare tegels
**Lobito** · **Port Allen (IRMT)** · **Port of Vidalia**. Staan als enige nog in
`v2/data/ankercheck.json` (HUD-sectie "Open ligplaatsen (3)"); de dertien afgehandelde
punten zijn eruit gehaald, want een rode stip op een gecorrigeerd punt liegt.

**De productvraag is 2026-07-28 wél beantwoord voor alle drie** — wat ontbreekt is
uitsluitend de meter kade:
* **Lobito** — product = koperkathode; terminal = de mineralenterminal van Porto do
  Lobito onder de 30-jarige LAR-concessie (Trafigura/Mota-Engil/Vecturis), eerste schip
  12-07-2024 (MV Lindsaylou, 40.500 t zwavel, ingaand). De eerste VS-lading vertrok
  22-08-2024 op de **MSC SAMU — een containerschip**, dus kathode gaat gecontaineriseerd
  weg. Geen bron noemt een kadenummer; Angola heeft nul havens met varend AIS-verkeer,
  dus ook de trackdata kan hier niets aanwijzen. **Dit blijft vermoedelijk open.**
* **Port Allen** — container-op-barge = **SEACOR AMH** op de **Inland Rivers Marine
  Terminal** van de Port of Greater Baton Rouge: 84 acre aan een bargekanaal langs de
  GIWW, **200 ft bargekade**, 9 acre containeryard, ro/ro-ramp, spooraansluiting.
* **Vidalia** — de haven ligt aan LA-131, mijl 359 AHP, 12 ft; de **bestaande** fase is
  een cargo ramp voor aggregaat + een t-dock met transportband voor droge bulk.
  ⚠️ **Spanning:** deze stroom is containervormig, en een t-dock met transportband lost
  geen containers. Vraag aan de brief, niet aan de satelliet.

**Volgende stap voor Port Allen en Vidalia is NIET opnieuw inzoomen** maar het
dok-bewijs uit de AIS-trackuiteinden — beide liggen binnen de bbox van de track-graaf,
en die toets vond bij de Syrah-kade al 55 eindigende tracks.

## ✅ OPGELOST 2026-07-28 (laat) — de "883 km" van het spoorbeen Beilun→Guixi was een verkeerde conclusie
De brief stelde dat de atlas dit been op 883 km mat tegen ~628 km volgens de bronnen, en
dus op een verkeerde corridor lag. **Hermeten met `toets_spoorroute.mjs`: 550,5 km** over
143 edges (verhouding 1,13 op de grootcirkel), identiek met de oude én de satelliet-
gelegde ankers omdat beide op dezelfde hoofdnet-knoop snappen. De tweezijdige toets van
werkwijze §4 slaagt volledig. De 883 km komt uit de heal-ronde van 2026-07-24, op een
ouder netstadium en tussen andere punten. **Les: noem bij een lengtemeting altijd het
gereedschap, de twee eindpunten en het netstadium — anders wordt een oud getal een nieuwe
conclusie.**

## ✅ OPGELOST 2026-07-28 (laatst) — de ankercheck-laag is teruggebracht tot de drie open punten
`v2/data/ankercheck.json` bevat nog uitsluitend Lobito, Port Allen en Vidalia; de HUD
heet "Open ligplaatsen (3)". `v2/src/ankercheck.js` blijft ongewijzigd staan — het
rood→groen-mechanisme met het witte verplaatsingslijntje werkt nog en is meteen bruikbaar
zodra er voor die drie een voorstel ligt. Het gelabelde proefwerk van de beoordelingsronde
(16 punten mét oordeel en verplaatsing) staat bevroren in
`v2/design/ankercheck-2026-07-28.json` en is de testverzameling van `toets_ankers.py`.

## ✅ OPGELOST 2026-07-28 — de vier grafiet-centroïdes (incl. de New Orleans-kade)
De routebrief grafiet-balama-vidalia leverde de echte coördinaten: Balama-plant
(-13.310/38.660, lag 13 km te ver west) · Nacala-kade (-14.531/40.652) ·
**New Orleans → Napoleon Avenue Container Terminal (29.9165/-90.1105)** — het punt
dat hieronder open stond · Syrah-fabriek (31.5466/-91.4887; het oude 31.57/-91.42
was het Terral-fleeting-punt, blijft in `PUNTEN` als AIS-toetsreferentie). Flow
rail→road (er is géén spoor in Concordia Parish), volumes naar EA-regime. Commit
`56402f1`.

## ⚠️ OPEN — `regressie`-snap heeft geen limiet, dus een VOOR-pad kan misleiden
`snap_halte` snapt naar de dichtstbijzijnde halte hoe ver ook: bij de stroomtests gaf
"VOOR" (alleen track-graaf) formeel een pad vanuit Nacala en Newcastle — na een snap van
**14.390 resp. 26.881 km** naar de VS-corridor. De gerapporteerde snap-afstand ontmaskert
het, maar wie alleen "pad gevonden" leest trekt de verkeerde conclusie. Cosmetisch, geen
routeringsfout (NA-routes zijn correct). **Fix-kandidaat:** een snap-maximum of expliciete
"snap > X km = betekenisloos"-waarschuwing in de uitvoer.

## ⚠️ OPEN — marktcentroïden zijn te grof voor snap-eisen (zelfde klasse als New Orleans)
`gr-mkt-us` (battery belt) snapt op 11,65 km — het is een regio-centroïde (TN/KY), geen
fabriek of laadspoor. Zelfde klasse als de New Orleans-stadscentroïde hieronder. Voor
stroom-rendering is dat oké (markt = gebied), voor snap-acceptatie-eisen niet.

## ✅ OPGELOST 2026-07-27 — het knip-lek: de snelheidsguard was scale-blind
`bouw_tracks.py` kende het dubbel-MMSI-geval wél (de header noemt het) maar
`MAX_KNOPEN=40` toetst **km/uur**, en over een lang datagat wordt élke afstand
plausibel. **2.214 valse lassen** over vier bronnen (VS 1.529 / 107.801 km · DK 610 /
45.486 · NO 15 / 1.018 · collector 60 / 2.826 — steeds ~0,4% van de km), en **alle**
glipten onder de 40-knoopgrens door. Ergste geval: punt [29] in San Francisco, punt [30]
in Providence Rhode Island — **4.392 km in 61 uur = 38,9 kn**, net onder de grens.
Waarom dit ertoe deed: een rechte koorde van 189 km waar de rivier 250 km meandert is
precies de sluipweg die een kortste-pad-router kiest.
**Fix:** na-conditie op de uitvoer (`knip_op_gaten`), niet een extra tak in de
knip-logica — een track mag geen segment bevatten dat én een gat > `KNIP_MIN` én een
afstand > `GAT_MAX_KM` overbrugt. Twee toetsen samen, want elk apart is onschuldig: een
sluispassage van 66 min legt 0,04 km af. Alle vier de sets herbouwd → **0**, korte stops
blijven (VS 275.361 → 275.157), twee runs byte-identiek. Oude sets in
`build-cache/ais/tracks-voor-knipfix/`.

## ⚠️ OPEN — de New Orleans-coördinaat is een stadscentroïde, geen kade
`gr-port-neworleans` in `data/graphite.js` staat op 29,95 / −90,07. Daar komt **geen
enkele** van de 510.752 VS-tracks binnen 0,5 km (749 binnen 1 km, 3.459 binnen 3 km),
dus de acceptatie-eis "snap ≤ 0,5 km" is op dat punt onhaalbaar voor élke graaf op deze
data — de graaf haalt 0,726 km, wat de best mogelijke waarde is. Vidalia haalt wél 0,400
km. Dit is dezelfde klasse als de eerder gevonden `data/*.js`-datafouten (Antofagasta
i.p.v. Patache, Yangshan i.p.v. een rivierkade): te grofkorrelig voor straatniveau.
**Fix:** de echte loskade van het Balama-vlok opzoeken en de coördinaat vervangen.

## ⚠️ RISICO — de tracks-laag groeit hard in de git-history
`v2/data/aistracks-pilot.json` ging van 21,4 → **39,5 MB** (13,9 MB gz) door de vijf
bronnen, en groeit met elke bron erbij. De laag is lazy en default uit, dus de gewone
paginalaadtijd verandert niet, maar dit is inmiddels de tweede 20 MB+ blob in de
history. Voor de **pings**-laag is in M28 bewust voor een VPS-endpoint gekozen om precies
dit te vermijden (*"geen databestanden in de git-history"*); die afweging geldt hier op
enig moment ook. Alternatieven: puntenbudget omlaag, of dezelfde endpoint-route.

## ⚠️ OPEN — laag 1 (hele-track-match) is dun voor lange reizen
119 tracks eindigen binnen 3 km van de Syrah-kade en 133 beginnen er, maar slechts **5**
dekken de héle reis New Orleans→Vidalia (2 binnen 3 km snap aan beide einden). Oorzaak
is by design: `bouw_tracks.py` knipt zodra een schip écht aanlegt, dus een meerdaagse
duwvaart met tussenstops valt in losse tracks uiteen. Voor langere ketens wordt dit
dunner. Geen bug — maar het is de reden dat laag 2 (de graaf) nodig blijft, en het is
het getal om in de gaten te houden als er stromen bijkomen.

## ⚠️ BEVESTIGD — het Wesel-gat is structureel (2026-07-26, hermeten)
Het voorbehoud hieronder ("berust op 1,2 uur data") is opgeheven. Hermeten op **12,5 uur**,
elk bericht geteld per 0,1° lengtegraad binnen de rijn-corridor:

| lon | berichten | MMSI | uurvakken met data |
|---|---|---|---|
| 6,3 | 509 | 119 | 12 |
| 6,4 | 81 | 44 | 12 |
| **6,5** | **0** | **0** | **0** |
| **6,6** | **5** | **2** | **1** |
| 6,7 | 14.118 | 197 | 12 |

Aan weerszijden twaalf uur onafgebroken verkeer, ertussen twee lege bins — **geen
steekproefartefact maar een eigenschap van het stationsnetwerk**. De pilot-corridor
(Rotterdam-Rijnmonding → Duisburg) krijgt hier dus een gedocumenteerd gat van ~55 km. Conform
de werkregel wordt het **niet** gerepareerd met geleende geometrie: dekking kan opportunistisch
aangroeien, dus geleend werk is weggegooid werk zodra er één ontvanger bijkomt.

## ⚠️ RISICO OPGELOST, NIEUW RISICO ERVOOR TERUG — schijf bij het wereldabonnement (2026-07-26)
Sinds 14:08 UTC draait de collector op een wereldabonnement. **Ruw zou dat ~8,5 GB/dag zijn
tegen ~22 GB vrij** = schrijfstop binnen twee dagen; daarom schrijft hij nu direct gegzipt
(~1 GB/dag, ~20 dagen marge) en **weigert `--wereld` zonder `--live-gz`**.
⚠️ **Blijvend risico:** de harde ondergrens van 2 GB stopt alléén het schrijven — de stream
loopt door, dus een volle schijf valt niet op in de data maar alleen in `journalctl`.
`haal_ais_data.py --opruimen` is daarmee onderhoud geworden, geen luxe.

## ⚠️ GEGEVEN — wat NOOIT uit tracks gebouwd gaat worden (2026-07-26, wereldwijd gemeten)
Van de 3.963 havens heeft er **1.169 (29,5%) varend verkeer**. **Nul** havens met varend
verkeer in: **Chili (47 havens) · Peru (28) · VAE (22) · Egypte (18) · Nigeria (18) ·
Roemenië (16) · Angola (12) · Iran (12) · Saoedi-Arabië (11) · Filipijnen (58) · Vietnam (21) ·
Tanzania (8)**. Dat raakt het koperbeen (Collahuasi/Escondida → Patache/Antofagasta),
**Hormuz**, **Lobito**, **Constanța** en **Suez** — die corridors blijven op MARNET + het
density-raster aangewezen; daar valt geen track te leggen.
⚠️ **Nuance bij de meting:** één uur. "0 in dit uur" bewijst geen afwezigheid van dekking bij
een haven met weinig bewegingen; wat wél binnenkwam is hard bewijs van aanwezigheid. Voor de
extreme gevallen (Zuid-Azië + Golf samen 163 berichten in een uur) is toeval uitgesloten.

## ⚠️ GEGEVEN — ook de Chinese KUST heeft geen aisstream-dekking (2026-07-26)
Aanvulling op de China-notitie hieronder, en het weerlegt het idee om de Chinese kust erbij
te nemen voor betere MARNET-aansluitingen. **Bewezen met een positieve controle in dezelfde
subscriptie:** Busan **220** en Tokio-baai **71** berichten in 3 minuten, tegen **Shanghai 0**
en **Ningbo-Beilun 0**. Geen box-limiet, geen subscriptiefout. De stippen die op de
aisstream-dekkingskaart bij China lijken te staan zijn Korea, Japan en Taiwan.
**Werkregel:** concludeer "geen dekking" nooit uit een uitblijvend signaal alleen — stuur
altijd een venster mee waar het aantoonbaar wél moet stromen.

Andere nulmetingen uit dezelfde ronde: **onder-Mississippi (New Orleans–Memphis) 0** (de
binnenlandse VS-stippen zitten op de Meren, niet op de rivieren) en **donau-onder 0**.
Gibraltar 2/min en Panama 1/min zijn praktisch niets — dekking is sterk bij walstations nabij
druk vaarwater en zwak op open zee (bereik 40–80 km). Volledige tabel in
`v2/design/ais-collector-vps.md`.

## ⚠️ VOORLOPIG GEMETEN — dekkingsgat op de Rijn bij Wesel (2026-07-25, bevestigen)
Door Lars gezien op de nieuwe pings-debuglaag en nagemeten in `pings.json`: tussen
**lon 6,37 en 6,75** komt geen enkele ping binnen, terwijl het aan weerszijden druk is
(6,15–6,30 Emmerich: 215 pings · **6,35–6,65 Wesel: 0** · 6,70–6,85 Duisburg: 637, in
hetzelfde tijdvenster). Laatste ping stroomopwaarts 51,754 N / 6,366 O (voorbij Rees),
eerstvolgende 51,400 N / 6,745 O (Duisburg-Rheinhausen): **47 km hemelsbreed, ~55 km
langs de rivier** — de Rijn langs Xanten, Wesel en Rheinberg. De collector-box loopt door
tot 7,0 O / 51,15 N, dus dit is géén venster-rand maar een ontbrekende ontvanger.

⚠️ **Voorbehoud:** de meting besloeg pas **1,2 uur** data (collector startte 20:23 UTC).
Een schip doet 2–3 uur over dat traject, dus één rustig uur kan strikt genomen toeval
zijn — de drukke flanken maken dat onwaarschijnlijk. **Hermeten zodra er een volle dag
ligt**, en dan hard vastleggen of doorhalen.

Waarom het uitmaakt: dit stuk ligt op het Rijnbeen van de kolen-routebrief (EMO →
Schwelgern). Duisburg zelf is goed gedekt, dus de track-graaf krijgt hier een gat van
~55 km. Oplosrichting: density-raster als fallback voor dít segment, of de OSM-geometrie
lenen — dezelfde rolverdeling als bij de Yangtze.

## ⚠️ GEGEVEN — aisstream heeft geen dekking landinwaarts in China (2026-07-25)
De stationskaart van aisstream (open/vrijwillig netwerk) is dicht op Europa incl. het Duitse
binnenland, de VS-kust **plus** Grote Meren en het Mississippi/Ohio-binnenland, Japan/Korea/
Zuidoost-Azië en de Australische kust — maar China heeft **alleen kustpunten**. Een station
reikt 40–80 km; Tongling ligt ±400 km landinwaarts. Gemeten: 0 berichten in 3 minuten tegen
293/min voor Rotterdam. Dit is geen storing en geen bug, maar de harde grens van M28: **de
Yangtze krijgt geen eigen tracks** en houdt het World Bank density-raster als fallback
(`bake_aisnet.py`, kop gemarkeerd). Het tongling-venster blijft in de collector staan zodat
het antwoord doorlopend geverifieerd wordt in plaats van uit één momentopname te komen.
Praktisch gevolg: het Tongling-handwerk (`data/vaarwegen-handmatig.geojson`, de satelliet-
gelegde oostgeul) blijft nodig — juist daar waar tracks het overbodig zouden maken.

## ⚠️ RISICO — VPS-schijf: 22,8 GB vrij van 96 GB (2026-07-25)
De collector schrijft ~234 MB/dag ruw per Rijnmond-formaat venster. Ondervangen: afgesloten
dagen worden automatisch gegzipt (~10×) en onder **2 GB vrij** stopt de collector met
schrijven (stream + health lopen door) in plaats van de schijf vol te laten lopen. Bij het
toevoegen van drukke vensters (Shanghai-mond, VS-binnenwateren) eerst een dag meten. Hermes,
Traefik en form4app delen deze schijf.

## ⏳ OPEN — reboot-overleving collector niet live bevestigd (2026-07-25)
`ais-collector.service` is `enabled` met `Restart=always`, en crash- én verbindingsherstel zijn
echt getest (`kill -9`, `ss -K`). Een echte reboot is **niet** gedaan omdat Hermes, Traefik en
form4app op dezelfde VPS draaien. Bevestigen bij de eerstvolgende geplande reboot.

## ⚠️ GEGEVEN — het World Bank AIS-raster heeft artefacten (2026-07-25)
Geulen staan er vaak in als 1-cels draden met uniforme waarden (oostgeul Tongling:
17,8M/cel) mét losse exacte-nul-cellen erin, soms hele nul-rijen — tegelnaden in de
World Bank-verwerking (de zwarte band bij Shanghai op de screenshots is er ook een).
Drijf-/ankerzones dragen dezelfde ~3M-waarden als corridors maar als speckle (p50 van
de bezette cellen: 2 berichten). Elke toekomstige stap op dit raster (de graaf-stap!)
moet hiermee rekenen: waarde-drempels onderscheiden geul niet van ankervlek — geometrie
(doorlopende draad vs spikkels) wel. Het rug-recept in `bake_aisnet.py` is hierop geijkt.

## ⚠️ OPEN — Rijnbeen kolenstroom vaart via het Beerkanaal (routebrief-vondst 2026-07-24)
De gerouteerde corridor (`?v=071`: EMO→Beerkanaal→Hartelkanaal→Oude Maas→Rijn, 254 km) wijkt aan
de havenkant af van de werkelijke duwvaartroute: het duwstel verlaat de Mississippihaven
**oostwaarts** en gaat bij de **Suurhoffbrug direct het Hartelkanaal in** (open verbinding sinds
de doorsteek van de Beerdam, eind 1997; het Beerkanaal is de zeevaart-kant). Operator-opgave
240 km vs 254 gerouteerd. Fix = het been via-punt→via-punt langs de brief routeren; eindpunt
hoort op de Schwelgern-haveningang, Rijn-km 790,20 (51.512, 6.723). Bron + puntenlijst:
`v2/design/routebrieven/kolen-cerrejon-ruhr.md` (§Toets tegen de huidige atlas).

## ✅ OPGELOST 2026-07-24 — industrieel last-mile-spoor niet aangesloten (live ?v=072)
De sidings die een smelter/terminal aan de hoofdlijn knopen waren losse stubs, omdat het M25-filter
álle `service=`-rail dropt. Additieve pass (`fetch_service_lastmile.py`) + transitieve vertex-heal
in `bake_landnet` + drop-onverbonden. Tongling/Beilun/Guixi/Duisburg hechten nu. Twee regressies
onderweg gevangen (beide Cerrejón→Bolívar): (1) een edge-split gaf de tweede helft van een
gesplitste hoofdlijn het spoor-heal-label → de drop wierp dat legitieme stuk weg → van edge-split
terug naar vertex-connectoren; (2) de drop liet **wees-knopen** achter → Bolívar snapte op een
0-graads wees i.p.v. de 158 km-kolenlijn → wees-knopen compacteren na de drop. Pas dáárna 30/30.

## ⚠️ OPEN — 22 grove AFGEKNIPT-sites (bredere uitrol)
`toets_spoor_aansluiting.mjs` vindt 22 industriële nodes met een gemapte-maar-losse siding
(Fresnillo, Kalgoorlie, Norilsk, Hunan-Ag…). Dat zijn de grove `data/*.js`-coördinaten (vaak
stad-centroïdes), niet de aangewezen aansluitingen — de last-mile-pass raakt ze pas als hun
precieze coördinaat + extract in `PUNT_EXTRACT` staan. Geen bug in de pass; bewust nog niet uitgerold.

## ✅ OPGELOST 2026-07-24 — vier netbreuken in één ronde (de pijplijn knipte ze zelf)
Raw-experiment bewees vooraf: de bron was op elk breukpunt al verbonden, óók onder het
service-filter. Drie fixes: (1) de heal VERLENGT een uiteinde i.p.v. het te verplaatsen —
verplaatsen trok samenvallende tweeling-eindpunten los en tier-2 snapte ze terug (de
EMO-flip-flop: zelfde 15 m-naad zes rondes gelegd en losgetrokken); (2) de haven-riviersnap
verkiest relatief een doorgaand component (absolute drempel verworpen: teleporteerde
Whitby/Rostock 58 km); (3) dedup-connectiviteitsguard `herstel_verbindingen` — niets wegvouwen
dat ≥2 componenten verbond, terug via het kortste stukkenpad (wereld: 1.185 stukken / 3.468 km,
0,3%). Daarmee opgelost: **EMO→Rijn** (kolen 0 gaten) · **Manaus→Amazone** (Saldanha→Manaus
routeert) · **Beilun↔Guixi** (trein 883 km) · **EU-spoor** (Antwerpen↔Duisburg één component).
⚠️ Gemeten en verworpen (niet opnieuw proberen): DEDUP_SNIPPER_KM 0,30→0,15 alléén — grootste
component kromp er zelfs van (4.135 → 3.531 km op BE+NL+NRW).

## ⚠️ OPEN 2026-07-23 (avond) — de gebakken hoofd-Yangtze is te grof bij de Tongling-noordpunt
De Chang-Jiang-middellijn (OSM way 226556520) heeft tussen lat 31,042 en 31,074 één **rechte
segment van ~16 km** dat de echte riviercurve om de eilandnoordpunt niet volgt (springt van
lon 117,74 naar 117,90). Gevolg: een fijn (167 m) afgeleide oostgeul-lijn kan er niet binnen
heal-afstand (250 m) aan aansluiten, want de gebakken lijn ligt kilometers naast het echte
water. Daarom is de Tongling-oostgeul nu **handmatig** afgeleid en bewust **alleen aan de
noordkant** aangesloten (met óók de zuidkant koos de router de westgeul + zuidjunctie en
maakte een lus om het hele eiland). **Structurele fix (Lars, volgende sessie):** een
riviernet-heal op dit gevlochten stuk (LAR-520-familie) die de hoofdgeul en de zijgeulen aan
beide eilandpunten verbindt — dan vervalt `data/vaarwegen-handmatig.geojson`.

## ✅ OPGELOST 2026-07-23 (avond) — de Yangtze was onderbroken in de graaf (snij_bulk knipte doormidden)
`snij_bulk()` in `bake_marnet.py` sluit dubbele OSM-geometrie uit door alles binnen 250 m van
de verhalende MARNET-laag weg te knippen. Bedoeld om een zijrivier zijn **kop of staart** af te
nemen, maar hij knipte ook **middenin** — en dan valt de rivier in de graaf uit elkaar terwijl
hij op het scherm doorloopt. Op de Yangtze vielen vijf stukken (2,1–5,9 km) weg precies waar de
M23-`yangtze`-zone ernaast ligt; die zone heeft knoop-ids ónder `zeeKnopen` (groep **zee**), dus
een binnenvaartbeen kon er niet op → Shanghai→Tongling maakte een lus tot lat 32,84 (Grote
Kanaal), 616 km. Fix: alleen kop en staart mogen weg (die verbreken per definitie geen
verbinding; een middengat altijd), interne `dicht`-vertices blijven staan. Been 616 → **540 km**;
wereldwijd **59 lijnen / ~282 km** heel gehouden; zee-invarianten onveranderd.

## ✅ OPGELOST 2026-07-23 (avond) — overslag-markers verdwenen zodra de tegels laadden
Het merk (een bolletje op de kade) was het enige object van `stroomlaag.js` zónder
`transparent:true`. Three tekent de opaque pass vóór de transparante; de invadende tegels
(transparant, vaden in met opacity 0→1) schilderden er daarna overheen. `renderOrder` en
`depthTest:false` ordenen alleen bínnen een pass en konden er niets tegen doen. Fix: vlag
toegevoegd (zelfde pass als de lijnen) + marker-maat gehalveerd zodat het de kade aanwijst
i.p.v. afdekt. (Lars: *"ik heb ze in sommige beelden wel heel kort gezien"* = precies dit
symptoom.)

## ✅ OPGELOST 2026-07-24 (dedup-guard, zie boven) - Beilun-havenspoor ligt los van het Chinese hoofdnet
De spoor-aansluiting van de ertsterminal Beilun (`cu-beilun-kade`) snapt op een component van
**1.823 km**; Jiangxi Copper/Guixi zit op het Chinese hoofdnet van **402.762 km**. Daardoor geeft
`cu-escondida-guixi` "geen pad" op het treinbeen. Zelfde soort breuk als het EU-spoor hieronder;
een cross-component-heal op `landnet.bin` kan beide dekken. De router meldt het nu zelf met getal
(`verklaarGeenPad()` in `stromen.js`), dus dit is diagnosticeerbaar in plaats van stil.

## ✅ OPGELOST 2026-07-24 (heal verlengt i.p.v. verplaatst, zie boven) - Maasvlakte-riviergat: EMO hing aan een bekken van 4 km
De EMO-kolenkade hecht op een **losstaand havenbekken van 4 km**, terwijl Duisburg op de doorgaande
Rijn (**24.517 km**) ligt -> het Rijnbeen van `coal-cerrejon-ruhr` faalt. Scherp contrast dat de
diagnose bevestigt: de koperkade in de Waalhaven, 30 km verderop, zit wel op de doorgaande Rijn en
maakt dezelfde reis probleemloos. Riviernet-fragmentatie, patroon van [LAR-520].

## OPEN 2026-07-23 - de via-havens in `data/*.js` zijn te grofkorrelig voor straatniveau
Op wereldniveau onzichtbaar, op z17 fout: `cu-collahuasi` vaart via **Antofagasta** terwijl zijn
eigen `note` "Patache/Collahuasi-haven" zegt en Collahuasi daar een eigen terminal heeft;
`cu-port-shanghai` is **Yangshan** - een containerhaven op eilanden voor de kust, niet de rivier;
de Guixi-smelter ligt **3,8 km** van zijn node-coordinaat. De aansluitingenlaag omzeilt dit nu per
stroom, maar de onderliggende data blijft grof.

## OPEN 2026-07-23 - OSM tagt niet wat er op een kade wordt overgeslagen
Bij geen van de gekozen kades in Rotterdam en Duisburg zegt OSM welke lading er omgaat; de
toewijzing leunt op de buren binnen 1 km (ArcelorMittal Staalhandel / Metaalhandel Ketting bij de
Waalhaven; Kokerei Schwelgern + Erzlager bij de Schwelgern-pier). Staat per aansluiting in de
`noot`. Idem bij Patache: de **espesadores** - het echte uitmondingspunt van de slurryleiding,
bevestigd door Collahuasi's eigen video - staan **helemaal niet in OSM** (vijf objecten binnen
1,8 km, geen tank). Daardoor houdt de gekarteerde leiding **736 m voor het terminalvlak** op; dat
restje wordt gestippeld getekend.

## OPGELOST 2026-07-23 - vijf fouten van mij, alle door Lars' visuele controle gevonden
Drie ervan hadden een wortel: **maten als vaste fractie van de bolstraal** (zie `decisions.md`).
1. Markers van **19,1 km** met `depthTest:false` -> op straatniveau een bol over het hele scherm.
   Nu schermgebonden (60 km op wereldhoogte, 30 m op 3 km).
2. Lijnen zwevend op **3,8-10,2 km** -> parallax; je zag ze naast de kade. Vaste lift eruit.
3. Koperkleur onleesbaar op de Atacama (zandkleur op zandkleur) -> pilot in contrastkleuren.
4. **Het schip voer de haven voorbij en kwam terug** - snoeien op knoopniveau doet per definitie
   niets; nu per vertex (Shanghai 10,7 -> 4,5 km).
5. **De pijpleiding begon middenin zichzelf** - zaaien op de dichtstbijzijnde vertex i.p.v. het
   uiteinde; het echte kopeinde lag 3,3 km verderop.
**Niet gereproduceerd:** Lars meldde traagheid ("bijna onbruikbaar"), later vanzelf weg - mogelijk
zijn laptop. Gemeten kostte de hele stromenlaag 0,02-0,04 ms per frame op elke hoogte, ook met een
marker centraal in beeld. De 19 km-bol was de beste kandidaat maar is niet bewezen.

## ✅ OPGELOST 2026-07-24 (dedup-guard, zie boven) — EU-spoor was gefragmenteerd in de M25-bake
Register-punten in Europa liggen op verschillende spoorcomponenten: Antwerpen (comp ~4.813 knopen)
en Duisburg (comp ~2.556) zijn níet verbonden, dus Antwerpen→Duisburg per trein = "geen pad" — óók
mét de hoofdlijn-snap. China (89.296-knoop component) en Zuid-Afrika zijn wél één net, daar werkt
spoor (Shanghai→Chongqing = trein 2.299 km). **Risico:** zodra de stromen over spoor door Europa
moeten, ontbreken die verbindingen. **Fix (later):** een cross-component-heal op `landnet.bin`, de
familie van de riviernet-heal (LAR-520) maar dan voor spoor, met gelijke-spoorwijdte-guard.

## ✅ OPGELOST 2026-07-24 (relatieve doorgaand-component-snap, zie boven) — Manaus→Rotterdam gaf "geen pad"
Sinds de dichtste-net-zaad-fix (geen fictieve verre zee-snap meer) valt Manaus terug op zijn
riviersnap, en die zit vermoedelijk op een Amazone-fragment dat het aangewezen Macapá-punt niet
raakt. Eerlijk "geen pad" i.p.v. een verzonnen route — maar het wijst op een riviernet-gat op de
Amazone dat een heal of een extra aangewezen punt vraagt. Komt boven bij het routeren van de stromen.

## ✅ OPGELOST 2026-07-23 — spoornet leek nergens in gebruik (rangeerspoor-snap)
Register-punten snapten op de dichtstbijzijnde landnet-knoop = meestal een emplacement-stub van een
paar honderd meter, terwijl het doorgaande net km's verderop lag → élke spoorroute "geen pad".
Opgelost met **hoofdlijn-snap** in `koppelNetten` (union-find; component-drempel spoor 1.000 / weg
30 km; cap 60 km, anders terugval + eerlijk "geen pad"). Dit is de val die de `CLAUDE.md` al noemde
bij `landnet-aanhecht.json`: knoop-afstand meet een stub, niet de doorgaande lijn.

## ✅ OPGELOST 2026-07-23 — de route-lijn stopte zomaar in zee (verre zee-snap)
Een niet-aangewezen binnenhaven (Karlsruhe, zee-snap 360 km) kreeg een zee-zaad met een aanloop die
dwars over land liep en niet getekend werd → de lijn leek in zee te stoppen. Opgelost: een niet-
aangewezen haven zaait alleen op zijn dichtste net (`havenZaden`). Aangewezen havens houden hun
dubbele aanhechting.

## ✅ OPGELOST 2026-07-22 — de HELE vectorlaag was onzichtbaar zodra de tegels er lagen

Niet alleen het spoor. Gemeten op 1 km hoogte mét tegels: kustlijn **0** pixels (zonder
dieptetest 20.057), zeenet+riviernet **0** (84.477), landnet **0** (30.509). De dader is de
**bol en alleen de bol** — tegels en atmosfeer schrijven al geen diepte — en hij dekt af terwijl
hij 12,7 km ónder de lijnen ligt. Dat kan alleen doordat `logarithmicDepthBuffer` een mesh zijn
diepte via `gl_FragDepth` laat schrijven en een `LineBasicMaterial` niet.

**Opgelost** met `depthTest: false` + renderOrder boven de tegels (tegels 1–3 · kust 6 ·
zee+rivier 6,5 · landnet 7) en de achterkant afgeknipt met een **`THREE.Plane` op de horizon**.

⚠️ **GEMETEN EN NIET WERKEND — niet opnieuw proberen:**

| poging | resultaat |
| -- | -- |
| de laag optillen (t/m ×1,01 ≈ 150 km) | geen enkele pixel verschil |
| renderOrder ophogen (t/m 4,5) | geen enkele pixel verschil |
| `material.extensions.fragDepth` | geen verschil (WebGL2, dus al core) |
| eigen horizontoets als varying via `onBeforeCompile` | kwam er met **omgekeerd teken** uit; ook na omdraaien klopte het beeld niet |

⚠️ **EN DE MEETVAL DIE DRIE RONDES KOSTTE:** meet zichtbaarheid **nooit boven open water**. De
camera staat standaard op lat 0 / lon 0 — de Golf van Guinee. "0 pixels" betekende daar precies
niets. Meet boven een gebied waar de laag hóórt te liggen (Frankfurt, Nederland, de Copperbelt).
En meet met *"hoeveel pixels veranderen als je de laag uitzet"*, niet met *"hoeveel pixels
hebben de kleur van de laag"* — dat tweede vervaagt over een lichte satellietfoto.

## ⚠️ OPEN — drie wegcorridors zonder pad

Zelfgemeld door de routering, mét coördinaat. Bewust open gelaten op Lars' regel dat gaten bij
het routeren van de stromen bovenkomen.

| corridor | melding | vermoedelijke oorzaak |
| -- | -- | -- |
| `bx-boke-katougouma` | geen wegen in het venster (8 km) | de SMB-haul road staat vermoedelijk niet als `motorway..secondary` in OSM |
| `li-atacama-lanegra` | punt (−68,3089 / −23,6430) >25 km van elke weg | tussenpunt midden in de salar, of wegklasse te laag |
| `ree-mountweld-leonora` | geen wegpad tussen punt 2 en 3 | venster of wegklasse |

## ✅ OPGELOST 2026-07-22 — de simplify knipte het spoornet door

`schrijf_geojson()` draaide Douglas-Peucker (tolerantie 100 m) ná de heal, en brak daarmee een deel
van de naden weer open. Polen, met de bake-regel: 77 componenten / grootste 15.341 km (79%) → 91 /
8.673 km (45%); de twee helften raakten elkaar op 75 plekken, waarvan zes binnen 22 m en één op
**0,7 meter**. Opgelost met `heel_na_simplify()`. Wereldwijd: grootste component 356.682 → 402.845 km.

## ⚠️ OPEN — drie fouten in `data/*.js` die de corridorronde blootlegde

Gevonden doordat elke corridor gedwongen werd een échte plek als anker te hebben. Alle drie zijn
datafouten, geen corridorprobleem — ze horen in de grondstofmodules gerepareerd te worden.

| plek | wat er mis is |
| -- | -- |
| `silver` — Japan (urban mining) → Mitsubishi / Dowa | draagt een lengte van **610,7 km** gemeten tussen een **landcentroïde** en een aggregaat van **twee bedrijven**. Een getal dat niets meet maar op bewijs lijkt; moet op `null`. Eén zo'n getal doet meer schade dan alle ontbrekende lengtes bij elkaar |
| `graphite` — Redwood Materials (Nevada) → Novonix Chattanooga | **de stroom bestaat niet.** Novonix Riverside maakt *synthetisch* grafiet uit petroleum needle coke van Phillips 66 (raffinaderij Lake Charles); Redwood's gepubliceerde anodeproduct is koperfolie, en teruggewonnen grafiet dat niet batterijwaardig is gaat volgens Redwood zelf naar industriële smeermiddelen |
| `silver` — Bingham Canyon → "VS-raffinage (Pacific-Noordwest)" | **modus én bestemming kloppen niet.** Het concentraat gaat 27 km door een **pijpleiding** (slurry) naar de Rio Tinto Kennecott-smelter bij Magna, Utah. De bestemming is bovendien een verzonnen regio-aggregaat |

Daarnaast, kleiner maar dezelfde familie — **dubbelnamen die twee plaatsen in één knoop persen**:
`Barro Alto / Onça Puma` (Goiás vs Pará, ~700 km uit elkaar), `Lake Charles/Seadrift`,
`Arezzo/Vicenza`, `Kwinana / Kemerton` (dat zijn twéé corridors, en de kortere viel weg),
`Zimplats / Unki / Mimosa`, `Mitsubishi / Dowa`.

## ⚠️ OPEN — 89 atlas-plaatsen hangen aan een spoorcomponent <1.000 km

Ná de heal-fix nog steeds. Een deel is **terecht** — Dubai, Jurong (Singapore) en Nieuw-Caledonië
hébben geen noemenswaardig spoor. Maar **New York op een component van 0 km** en **Amsterdam op
87 km** zijn dat niet. Van de 200 roze havens hangen er 28 aan een component <1.000 km.
⚠️ Meet dit tegen de **lijngeometrie**, niet tegen `landnet-aanhecht.json`: dat bestand meet de
afstand tot een **knoop**, en knopen liggen elke 10 km, dus een stub van 1 km lijkt er altijd
dichterbij dan een doorgaande hoofdlijn. Die vertekening kostte in deze sessie een halve diagnose.

## ⚠️ OPEN — `us-new-mexico` ontbreekt in de extract-registry

Nodig voor de corridor Mountain Pass → Fort Worth (I-40 loopt erdoorheen). Ophalen met
`fetch_landnet.py --download` vóór de wegbake. Ook `us-nevada` en `us-colorado` ontbreken.

## ✅ OPGELOST 2026-07-21 — de twee angled confluenties zijn dicht via écht water

De bruggen-walk (`knoop_riviernet.py`) vond bij **Ohio-Cairo** én de **Waal-tak bij Nijmegen**
gewoon verbindende watergeometrie in de bron: Cincinnati↔New Orleans (19.304 km) en
Nijmegen↔Rotterdam↔Duisburg (24.517 km) zijn elk één component. De geplande lengtetoets-naad /
`knooppunten.json`-workaround is vervallen.

## ⚠️ AANGEPAST — route-test geschrapt; router klein en pas bij stap 3 (2026-07-21)

Lars schrapte de route-test als gap-detector (een kortste-pad-router rijdt om een gat heen en
verbergt het) en checkt zelf binnenhaven→binnenhaven zodra de keten-router er is. R'dam→Duisburg
toont nu 420 km / aanloop 153 km — blijft indicatief tot de overslag/keten-router (stap 3) de
haven-aanloop goed afhandelt. Geen `toets_routes.py` bouwen als poort.

## ⚠️ OPEN — 1.903 verbindingsstukken nog visueel te toetsen bij de stromen (2026-07-21)

1.828 bruggen + 75 meer-oversteken liggen erin mét guards, maar de langste (250–300 km: Mamoré,
Irtysj/Lena-omgeving, Povlakte, Binnen-Mongolië) en het GB-kanalennet (553 kleine bruggen) zijn
niet stuk voor stuk beoordeeld. Lars' lakmoesproef: bij het uitwerken van de stromen (M26) blijkt
wat mist of te veel is. Elke brug/oversteek is een eigen lijn met signaal `"brug"`/`"meer"` —
gericht weghalen kan zonder iets anders te raken. Bekende v1-beperking: een walk stopt op de
extractrand, dus tagging-gaten die precies over een landsgrens lopen worden gemist.

## ⚠️ OPEN — LAR-519: onderzochte gabariet-maten moeten op het nieuwe net herlanden

De 7 trajectmaten + zes te splitsen edges + vier bronverificaties uit de gabariet-ronde verwijzen
naar de oude handgemaakte systemen die niet meer als routeerbare entiteit bestaan. Herankeren op
binnenwaternet-edges of bewust sluiten — niet laten hangen als schijn-backlog.

## ⚠️ OPEN — binnenhavens snappen slecht tot de overslag er is (2026-07-20)

Het riviernet is een eigen component en havens snappen alleen op het zeenet, dus elke haven die
landinwaarts ligt valt terug op zijn pre-M24-snap: **Nijmegen 79,1 km**, Amsterdam 15,1 km, havens
>50 km terug van 1.358 naar **1.473**. Ook A'dam→Shanghai staat weer op **19.794** i.p.v. 19.677.

**Dit is geen regressie maar een teruggedraaide verbetering** — die waarden kwamen van het
`noordzeekanaal`-systeem, dat met de andere artisanale ketens is verwijderd. Ze horen terug te
komen zodra de overslag er is; dat is meteen de acceptatietoets van dat werk.

## ⚠️ OPGELOST 2026-07-20 — de Ohio sluit voor élke CEMT-klasse (was [LAR-514])

Opgelost met de **VS-duwkonvooi**-klasse (3×3 jumbo hoppers, 178,3 × 32,0 m, 2,7432 m diep,
commit `afcabff`): op de Ohio vaart geen Europees schip. ⚠️ Maar daarmee is de fout **omgedraaid,
niet weg**: het model zegt nu dat een Ohio-duwbak vanuit Rotterdam vaart, en dat is even onwaar.
De echte oplossing is de overslag — zie `next-actions.md`.



`ohio` draagt diepgang **2,7432 m** (9 ft), en dat is géén geuldiepte maar een echte scheepsmaat:
USACE HEC schrijft *"navigation by vessels drafting up to nine feet from the downstream sill"* —
de geul zelf is 12 ft. Gevolg: **alle vijf** Europese CEMT-klassen in de HUD steken dieper (klasse
IV al 2,80 m), dus **Cincinnati en Louisville zijn onbereikbaar voor de hele Europese vloot**.

**Dit is fysiek juist, geen bug** — een Europees binnenvaartschip ís dieper dan een Ohio-duwbak.
Maar het maakt het Mississippi/Ohio-net onbruikbaar zodra je in de simulator een scheepsklasse
kiest. **Voorstel:** een klasse *"US barge tow"* (9 ft × 35 ft × 600 ft) aan `SCHEEPSKLASSEN` in
`main.js` toevoegen. Beslissing bij Lars.

## ⚠️ OPEN — zes edges dragen bewust géén gabariet tot ze gesplitst zijn (2026-07-20, [LAR-514])

`mississippi-upper` · `xijiang` · `grand-canal-zuid` · `yangtze` · `yangtze-boven` · `parelrivier`.
Voor alle zes ís er een gevonden maat, maar één gabariet kan het traject niet eerlijk beschrijven
(de 56 ft-kolken op de Upper Mississippi gelden over 10 van 1.728 km; de Xijiang loopt van 7,6 m in
de delta naar 11,5 m). **Risico bij nalaten:** wie de maat tóch invult sluit vrijwel al het verkeer
op die as af — precies de stille afsluiting die het draagprincipe verbiedt. Split-punten staan in
`next-actions.md` punt 2.

## ⚠️ OPEN — vier gabariet-waarden zijn niet hard genoeg (2026-07-20, [LAR-514])

Chicago-breedte (80 ft in 33 CFR 207.420 tegen 50 ft in de USACE WCM van mei 2024 — **die twee
liggen aan wéérszijden van CEMT VIb**, dus de keuze beslist de uitkomst) · Yangon 44 m (bekendmaking
van vóór de brugopening) · de Xijiang-bruggen 旧五斗大桥/旧西樵大桥 (heten "oud", mogelijk gesloopt)
· de 18 m van de 武汉长江大桥. Alle vier **leeg gelaten** — veilig, maar het zijn echte poorten.

> **Les die breder geldt:** elk hoogtecijfer is waardeloos zonder referentievlak, en hoogte werkt
> **ómgekeerd** aan diepgang — voor diepgang is laagwater de harde kant, voor hoogte juist
> hoogwater. Twee datums door elkaar gaf bij de Mississippi niet alleen een verkeerd getal maar de
> verkeerde **constructie**. En: **kabels liggen stelselmatig lager dan bruggen** en werden in drie
> van de vier gevallen vergeten — neem ze standaard mee in een hoogte-inventarisatie.

## ⚠️ OPEN — marnet-bulk.json is ongeoptimaliseerd (2026-07-20, [LAR-515])

38,7 MB raw / ~12,5 MB gzip — groter dan de eerste schatting (~6,2 MB), omdat de scope wereldwijd
werd (349.312 km i.p.v. de eerder geschatte 190.034) en de opslag platte JSON is, geen binaire
varint-codering zoals `marnet.bin`. Werkt nu prima (browser laadt in 624 ms), maar is de voor de
hand liggende volgende optimalisatie zodra dekking niet meer de prioriteit is. Bewust nu uitgesteld
("eerst alles mappen, dan optimaliseren").

## ⚠️ OPEN — LAR-515-acceptatiecriteria nog niet compleet (2026-07-20)

Wat wél gedaan is: `git diff` bewijst dat de routeergraaf onaangeroerd blijft, de 250m-exclusie is
gemeten (max weg ≤250 m, dichtste bewaard ≥250 m — grens klopt), browser laadt foutloos, Lars gaf
zijn visuele go op dichtheid/positie. Wat **niet** gedaan is: de dubbele-geometrie-toets op de
bestaande `vermijd`-knoppen (bewijzen dat elk label nog exact doet wat het deed — bv. `rijn-boven`
dicht moet nog steeds Mainz/Karlsruhe/Kehl onbereikbaar maken), een steekproef van bulksystemen
tegen officiële vaarafstanden, en `toets_usace.py` op de VS-bulk. Dit is fundament, geen afronding.

## ✅ OPGELOST — het aftakmechanisme is nu end-to-end gerouteerd (2026-07-19, [LAR-505])

Wat wél bewezen is: de knip zelf (moederedge 23→24 edges, lengte onveranderd, aansluiting 0,00 km,
uitvoer byte-identiek op de bestaande set). Wat **niet** bewezen is: een route die dwars **door** een
aftakking heen loopt, met echte havens aan weerszijden. Dat kan pas met een echte zijtak en is de
acceptatie van [LAR-505] (Nieuwe Merwede en Amsterdam-Rijnkanaal takken allebei middenin `waal` af).

**Gedekt sinds [LAR-505]:** `maas` hecht als `aftakking:waal` op 0,00 km bij Werkendam, en
**Nijmegen→Luik (353 km)** loopt de Waal af om er middenin af te slaan — een echte route dwars
**door** een aftakking, met searoute-havens aan weerszijden. Ook de `vermijd`-knop werkt per tak:
`maas` dicht → Luik/Born onbereikbaar terwijl R'dam→Nijmegen exact 172 km blijft.

## ✅ OPGELOST — `now.md` liep 14 knopen/edges uit de pas met de code (2026-07-19)

De vault noemde 9.877 knopen / 16.124 edges voor de bake van `45a21eb`, terwijl `marnet.json` op
**9.863 / 16.110** stond. Niets kapot, maar het is precies het soort drift dat een volgende sessie
laat "corrigeren" wat niet stuk is. Gecorrigeerd in `now.md` mét een notitie erbij.
**Les:** neem netwerkcijfers over uit `marnet.json`, niet uit een vorige samenvatting.

## ⚠️ OPEN — doodlopende MARNET-binnenwaterstubs ([LAR-507], 2026-07-19)

Lars zag het op de bol en omcirkelde het; nagemeten en het klopt. **MARNET-knoop 3947**
(4,430 / 51,715) in het Hollandsch Diep heeft **graad 1**: één ongelabelde binnenwater-edge van
16,4 km die nergens op aansluit. Onze `schelde-rijnkanaal`-keten loopt er pal langs maar de
dichtstbijzijnde ketenknoop ligt **7,84 km** verderop.

**Niet cosmetisch:** de haven `Willemstad` snapt erop (2,5 km) en is dus per constructie
onbereikbaar. Netwerkbreed **16 zulke stubs** (van 705 knopen met graad 1).

⚠️ **Twee consequenties, en de tweede is de ergste.** Deze edges dragen géén passage-label, dus
(a) onze nauwkeurige ketens kunnen ernaast liggen zonder routes te dragen (de ARK-situatie — de
Wolga-agent mat dat: Astrachan→Rostov gaat over MARNET in 870 km terwijl onze keten 1.002 meet), en
(b) het groepslabel `binnenvaart` uit [LAR-494] kan ze **niet sluiten**. Daar zit de veiligheidsklep
dus nog niet dicht.

⚠️ Bij een fix voorzichtig zijn met zones waar MARNET de énige geometrie is (Suez, Panama, Seaway):
die moeten open blijven voor zeeschepen — Duluth→R'dam 8.031 hangt eraan. Toets per zone, niet
globaal.

## ⚠️ OPEN — Noord-Duitsland ontbreekt volledig ([LAR-508], 2026-07-19)

Lars: *"er zijn boven in Duitsland toch ook grote industriële gebieden die met rivier aan water
liggen"*. De uitrol dekt de Rijn-Donau-as maar Elbe, Weser, Mittellandkanaal en Nord-Ostsee-Kanal
zitten in geen enkel issue.

Bewijs in de haventoets: **`Bremen` snapt 56,5 km** (de stad ligt 60 km de Weser op), Lübeck 18,2,
Kiel 18,9. Magdeburg/Hannover/Emden staan niet eens in de searoute-lijst omdat het binnenhavens zijn.

⚠️ Het **Kielerkanaal** wordt het eerste systeem met bewust `zeevaart=True` — dat ís een echte
zeevaartroute. Daarmee wordt R'dam→Oostzee terecht korter, maar dat raakt de regressie: bewust
vaststellen, niet stil laten gebeuren.

## ✅ OPGELOST — de routeer-default na de Donau-ring (2026-07-19, [LAR-494])

De Donau-ring maakte het kortste graafpad voor een zeeschip ineens dwars door Europa (18.627
i.p.v. 19.610 km). Lars' regel: *een zeeboot gaat niet ineens via rivieren of sluizen.*

Gefixt met **`zoekRouteRealistisch()`** (nu de default): eerst als zeeschip proberen, en pas als
een uiteinde in het binnenland ligt de binnenvaartsystemen openzetten die vanaf **dát uiteinde
zonder zee bereikbaar** zijn. Alle vastgelegde invarianten kloppen weer onder één default —
inclusief R'dam→Wuhan (20.626), dat met een simpele aan/uit-schakelaar niet te redden was.

⚠️ **Bij het lezen van oude regressiecijfers:** die horen bij de realistische default. De knop
"alles toestaan" geeft bewust andere getallen (R'dam→Constanța 3.291 i.p.v. 6.285) — noem dus het
profiel erbij.

## ⚠️ De deltahavens van de Donau snappen nog >100 km weg (2026-07-19, [LAR-494])

Sulina **124,8** · Brăila **100,8** · Tulcea **110,9** km. Oorzaak: we komen via het
Donau-Zwarte Zeekanaal binnen (Constanța), niet via de Sulina-arm — MARNET reikt niet tot de
delta. Bewust geaccepteerd binnen LAR-494. Oplossing = de **maritieme Donau** (Cernavodă →
Brăila → Sulina) als aparte tak; kandidaat voor een vervolgissue.

## ⚠️ EEN STITCH-FOUT WIJST NIET ALTIJD NAAR DE KETEN (2026-07-19, [LAR-505])

`RuntimeError: geen doorlopend waterpad tussen de ankers` klinkt als een gat in de ketting, en de
reflex is namen toevoegen. Bij het Albertkanaal hielp dat twee keer wél (`Canal de Monsin`, de vier
`duwvaartsas`-kolken) en de derde keer niet — want de keten wás al heel: **136,3 km van Antwerpen
tot Luik in één component**.

De echte oorzaak zat in het **anker**. `dichtstbij()` pakt de dichtstbijzijnde vertex ongeacht of
die in het hoofdcomponent zit, en `Canal de Monsin` bestaat uit twee stukjes met 130 m ertussen —
het anker landde op het losse fragment van 4 punten. **De melding beschreef het symptoom van het
anker, niet van de ketting.**

**Werkwijze die het uitwees:** de échte stitcher-graaf naspelen (segment-vertices + de
endpoint-hechting binnen `stitch_km`) en dan vragen *welke knopen zijn vanaf `start` bereikbaar* —
antwoord: 4 van de 446. Een eigen benadering met alleen endpoint-koppeling was hier misleidend,
want die verbindt anders dan de stitcher zelf. Bouw de diagnose op de échte graaf.

## ⚠️ METEN IN DE BROWSER-PANE: twee artefacten die me allebei beetnamen (2026-07-19)

Het venster is daar **1×1** en `document.hidden` is true. Gevolg:
1. **rAF staat stil** → `globeGroup.rotation` wordt nooit ververst, dus alles wat de framelus
   schrijft lijkt bevroren. Ook WebGL-screenshots hangen daardoor (bekend sinds M22).
2. **De cameramatrix blijft stale** → `Vector3.project(camera)` geeft onzin tot je expliciet
   `camera.updateMatrixWorld(true)` + `updateProjectionMatrix()` aanroept.

Ik heb op grond van artefact 2 bijna een verkeerde conclusie getrokken over de sleepwet (de
pixelmeting varieerde 309 → 2 terwijl hij constant had moeten zijn). **Betrouwbaar was alleen de
pure rekenkunde** — graden-nu tegen graden-ideaal — en die gaf een schone constante 3,52×.
Les: in deze omgeving alleen dingen meten die niet van een render-tick of matrix-update afhangen.

## ⚠️ RISICO — de CEMT-clause haalt méér binnen dan de whitelist (2026-07-19, [LAR-492] / [LAR-506])

**Bij de Mosel ging dit echt mis** (zie `decisions.md`): de clause haalde de Freycinet-kanalen bij
Nancy binnen (klasse I, 350 t) en die wonnen als kortste pad van de Moezel zelf — 18 km te kort én
de verkeerde vaarweg. Opgelost met `cemt_insluiten=False` op dat systeem.

**Verwacht dit opnieuw** overal waar een klein-gabarit kanaalnet naast de hoofdvaarweg ligt
(Frankrijk, België, Duitsland). De toets die het vangt is **lengte tegen tussenliggende ijkpunten**,
niet de corridor-toets — die vergelijkt de keten met de bron waaruit hij gebakken is.



Een systeem mét een `cemt`-waarde laat álle CEMT-getagde ways in de bbox toe, ook zonder naam-match.
Bij de Rijn was dat nuttig (het vond het Grand Canal d'Alsace), maar het betekent dat de invoer
groter is dan de namenlijst suggereert: 1.246 segmenten voor de Rijn, waaronder het halve
Benelux-kanalennet. De stitcher kiest het kórtste waterpad, dus dat kan in principe een sluiproute
opleveren. Gedekt door de **lengtetoets** (716,1 km tegen 714,7 officieel = +0,2%) en de haventoets,
niet door de corridor-toets — die vergelijkt de keten met de bron waaruit hij gebakken is.
Blijf dus per systeem op lengte controleren, niet alleen op corridor-afstand.

## ⚠️ OPEN / te weten vóór M25 gebouwd wordt (2026-07-19, [LAR-491])

- **Dubbelspoor leest 2× — de lengtetoets werkt niet zonder dedup.** OSM mapt dubbelspoor meestal als
  twéé losse parallelle lijnen (`tracks=2` staat in China op maar 5.406 ways). China meet daardoor
  266.146 km gefilterd tegen 109.767 gepubliceerde route-km (**+142%**). Dat is geen meetfout maar het
  gedrag van de data. Op land is lengte onze énige echte controle, dus **dedup moet er zijn vóór de
  eerste pilot** — anders "faalt" een bake die klopt en jaag je een niet-bestaande bug. Bijkomend: de
  graaf verdubbelt gratis mee met nul routeerwaarde. Myanmar (+7%) en Cambodja (~0%) verbergen dit,
  want die zijn enkelspoor; kies daarom een expliciet enkelsporige lijn als eerste ijkpunt
  (Sishen–Saldanha, 861 km).
- **Weg heeft géén onafhankelijke scheidsrechter.** GRIP4 was de kandidaat en valt af (vier
  tegenstrijdige licentieclaims voor dezelfde data + een onopgeloste klacht dat het ODbL-data als CC-0
  herpubliceert + ~de helft dateert van vóór 2010). Er is niets anders. Gevolg: wegcorridors kunnen
  alleen op gepubliceerde corridorlengtes getoetst worden, en waar die niet bestaan is er geen bewijs.
  Daarom bewust klein houden.
- **De GEM-pijpleidingrepo draagt geen LICENSE-bestand.** `GlobalEnergyMonitor/GOIT-GGIT-pipeline-routes`
  is openbaar en de README is puur operationeel; GEM's tracker-pagina's noemen CC BY 4.0, maar dat staat
  niet op de repo. Prototypen prima; **vastzetten vóór het live gaat**, want de atlas voert ODbL, Esri
  en UNECE wél netjes in de credits.
- **De router kan een niet-operationele spoorlijn kiezen.** Kortste pad over spoor ≠ de route die de
  operator rijdt (spoorbreedte-wissels, eigendom, lijnen die fysiek bestaan maar niet rijden). Dat is de
  geaccepteerde prijs van het complete net; mitigatie is de gelaagdheid (verhalende corridors apart
  gebakken en op lengte gecontroleerd).
- **⚠️ FCAB Antofagasta niet als ijkpunt gebruiken** — gepubliceerde lengtes lopen van 700 km (FCAB's
  eigen duurzaamheidsrapport) via 834 tot 1.152 km voor de doorgaande route. Een spreiding van 65% is
  geen meetlat. Idem Droezjba (4.000–5.500 km, vertakt systeem).

## ⚠️ OPEN / te weten na LAR-487+488 (2026-07-19)

- **De publieke Overpass-mirrors zijn een broos afhankelijkheidspunt.** Tijdens deze sessie gaven ze
  massaal 504's, ook op queries die minuten eerder gewoon slaagden — de fetch is daardoor de traagste
  stap van de pijplijn (~25 min voor 6 systemen), niet de bake (~1 min). Gemitigeerd met retry-rondes,
  snelle failover en een schijf-cache op de query-inhoud (een herstart begint nooit opnieuw), maar bij
  de **wereldwijde uitrol** met tientallen systemen is dit het schaalrisico. Overwegen: chunken van
  grote bboxen, of Geofabrik-extracts als de mirrors structureel tekortschieten.
- **`overpass.osm.jp` heeft een kapot certificaat** (hostname mismatch) — uit de mirrorlijst gehaald.
- **USACE `AMILE`/`BMILE` zijn niet overal gevuld.** Twee links in de Mississippi-corridor staan op
  0.0; sorteren op milepost suggereert dan een gat van 45 mijl terwijl hun geometrie gewoon aanwezig
  is. Wie dat gat gelooft, leest elk OSM-punt in die stretch als uitschieter tegen niets.
- **`exceededTransferLimit` zit bij `f=geojson` genest onder `properties`** (en `properties` is null
  als er niets is afgekapt). Op de top-level sleutel checken geeft **stille truncatie op 2.000
  features**. Native SR van de laag is 4269 (NAD83) → `outSR=4326` expliciet meegeven.
- **OSM en USACE zijn het lokaal oneens over het kanaal** in de oxbow/cutoff-stretch tussen Baton
  Rouge en Arkansas City (lon -91,15..-91,49): 3,8% van de punten >500 m, max 1.889 m. Geen fout van
  ons (de ruwe lijn heeft dezelfde max) en onschadelijk op bolschaal, maar goed om te weten als er
  ooit op meterniveau tegen de VS-geometrie gemeten wordt.
- **`taskkill /IM python.exe` sloopt ook de dev-server van de Browser-pane** — daarna `preview_start`
  opnieuw draaien.

## ⚠️ OPEN na M23 (2026-07-18) — bekend, bewust doorgeschoven naar M24 (= [LAR-485], incl. het ontbrekende Noordzeekanaal)

0. **Ultrawide-restje tegels (geaccepteerd, niet fixen):** na de scherpte-reeks (`990765c`+`61d7388`+`1a724b8`)
   is 1080p/portret helemaal goed (~100 tegels); op een ultrawide 2K zijn de uiterste hoeken nog nét te vinden
   (ring op z−2 i.p.v. vol-scherp) en laadt een verse view 1.300+ tegels (patch ≤900 + ring ≤350 + shell 64) —
   merkbaar maar smooth. **Lars (2026-07-18): "dat is voor nu niet erg, we laten het zo."** Knoppen als het ooit
   tóch moet: `ringMaxTiles`, het budget-plafond (900), de tilesAcross-cap (14), of progressief laden.

1. **2 onopgeloste edges** (origineel behouden, connectiviteit intact): Södertälje-archipel
   `(58.57,17.42)→(58.65,16.32)` (Stockholm-scheren te fijn voor het 0,01°-raster) en één Channel
   Islands-koorde `(33.20,-120.67)→(33.63,-118.12)`. Opruimen bij M24 (zone of fijner raster).
2. **Rivierhaven-stubs:** havens die ver een rivier op liggen (Yangon, Moulmein, …) krijgen hun laatste
   ~30 km als rechte lijn over land — de rivier bestaat niet als water in de NE-polygonen en valt binnen de
   gemeten eindtolerantie. Geen databug; M24 (binnenwater) vervangt stubs door echte riviergeometrie.
3. **Snap-afstand havens:** mediaan 31 km, maar 1.473 van de 3.962 havens snappen >50 km naar de graaf
   (kleine havens ver van een lane). Voor de route-test prima (aanloopstuk zichtbaar + km opgeteld); voor
   M26-flows willen we per grondstof-haven checken of de snap acceptabel is.

## ✅ GEFIXT in M23 (2026-07-18) — twee structurele, gevangen door Lars' eerste route-test

1. **De trans-Pacific was doorgeknipt op de datumgrens.** MARNET heeft **15 knopen dubbel als lon +180 én
   −180** (58+49 punten op ±180): de graaf bleef formeel één component, maar de hoofdlanes eindigden op een
   +180-knoop terwijl het vervolg op −180 begon. Symptoom: Yokohama→LA = 32.000 km via Suez+Panama;
   Antofagasta→Shanghai om Zuid-Afrika. Fix: lon-normalisatie in `bouw_graaf` → 9.111 resp. 18.915 km.
   **Les: bij élke graaf uit geo-data eerst de datumgrens-topologie controleren.**
2. **Kortste graafpad koos de Noordwest-Passage** voor Rotterdam→Shanghai (15,5k km) — geometrisch correct,
   commercieel onzin. Fix: passage-restricties in `zoekRoute`, default `northwest` dicht (= searoute's eigen
   default `restrictions=[northwest]`). Geen arctis-straf nodig gebleken.
3. *(klein)* **cp1252-console crashte op een `→` in een print** ná het schrijven van alle data — de bake
   leek gefaald terwijl alles er stond. `sys.stdout.reconfigure(encoding="utf-8")` in de baker.

## ✅ GEFIXT in M22/v2 (2026-07-18) — vier die je makkelijk opnieuw maakt

1. **Vectorwereld lag 90° verdraaid op de bol.** `world.js` gebruikte `x = cos(lat)·sin(lon)` /
   `z = cos(lat)·cos(lon)` i.p.v. v1's `x = cos(lat)·cos(lon)` / `z = −cos(lat)·sin(lon)`. Kustlijnen klopten
   **onderling** (Sumatra wás Sumatra) maar lagen los van de bol — dat maakt het verraderlijk: de laag ziet er
   op zichzelf perfect uit. Het commentaar beweerde bovendien "zelfde afspraak als v1", wat het niet was.
   **Was dit blijven staan, dan had M26 alle mijnen en routes verkeerd gezet.**
2. **Lege tegels schilderden over de bol tijdens het laden.** Bij het overzetten van `tiles.js` uit v1 ging
   `opacity: 0` + invaden verloren. Tegels worden aangemaakt vóór hun textuur binnen is, dus ze moeten
   onzichtbaar beginnen. Mislukte tegels worden nu opgeruimd i.p.v. als leeg vlak te blijven staan.
   ⚠️ **Correctie:** ik schreef dit eerst op als de verklaring voor Lars' banden en ruitjespatroon. **Dat was
   het niet** — hij zag ze daarna nog steeds. Het was een echte bug, maar een ander symptoom. De werkelijke
   oorzaak staat hieronder onder 4.

4. **De bol prikte door de tegels heen — DIT waren de banden en de poolringen.** Een tegel is een plat
   lapje; tussen de hoekpunten duikt zijn koorde onder het boloppervlak en prikt de bol-textuur eroverheen.
   Vandaar perfect horizontale banden langs de breedtegraden en een ringpatroon precies op de pool, waar de
   Mercator-tegels het grootst zijn. **v1 waarschuwt hier letterlijk voor in `config.js`** en ik heb bij het
   overzetten alle drie de waarden te laag gezet: `shellLift` **1.0000** (v1: 1.0016 — mijn tegels lagen dus
   precies ÓP de bol), `detailLift` 1.0002 (v1: 1.0026), `shellMeshDetail` 16 (v1: 24).
   **v1's oplossing kon niet worden overgenomen:** de tegels optillen naar 1.0016 = 3,8 km, en v2 zoomt tot
   ~1 km hoogte → de camera zou onder de tegellaag uitkomen. Daarom omgekeerd opgelost: **de bol eronder
   zakt** (`setSphereSink`, scale 0,998 ≈ 12,7 km) zodra er tegels overheen liggen, en staat op 1 in "egaal"
   waar de bol zelf het oppervlak is. `shellMeshDetail` wel terug naar v1's 24.
   **Meetmethode die dit ontrafelde** (herbruikbaar): tel welk aandeel schermpixels verandert als je de bol
   eronder verbergt — dat is letterlijk "waar prikt hij doorheen". Voor: **8,50%** (7,80% sterk). Na:
   **0,42%** (0,40% sterk), en die rest zit voorbij 85° breedte waar de tegellaag ophoudt en de bol terecht
   de achtergrond is.
3. **De `index.html` zelf zit in de Pages-cache.** Na de uitlijn-fix gaf mijn verificatie onzin en leek de
   fix niet te werken — de browser had `?v=002` geladen, want de gecachete HTML verwijst naar de oude
   assetversies. **Cache-busting op assets helpt dan niets.** Verifieer met een cache-bustende query op de
   HTML (`?vers=…`) én check `performance.getEntriesByType('resource')` wélke versie geladen is.

## 🔧 OPEN — risico's van de nieuwe tegellaag (2026-07-18)
- **Tegelbudget niet getest op mobiel onder 4G.** Op wifi/desktop: 305 tegels op 1 km hoogte, 0 mislukt.
  Onbekend hoe dat zich houdt op de Honor Magic V5 met een trage verbinding (data + textuurgeheugen).
- **Esri heeft geen beeld boven open oceaan op hoge zoom** → lege/mislukte tegels. Ze worden nu opgeruimd,
  maar je ziet dan de grove shell. Acceptabel; opletten bij het beoordelen van routes ver van de kust.
- **Vector en satelliet zullen het nooit perfect eens zijn** — andere bronnen, en de satelliet is bij de
  shell ~9,8 km/pixel. Bij diep inzoomen loopt de lijn een eindje naast de satellietkust. **Geen bug:** de
  vector is per besluit de waarheid, de satelliet een skin.
- **`v2/build-cache/` staat in `.gitignore`** (ruwe GeoJSON, 11,5 MB). Wie het wereldmodel opnieuw wil bakken
  moet eerst opnieuw downloaden.

## 🔧 OPEN — asymmetrische baan-klem staat halverwege in de werkende boom (2026-07-18)
- **Niet gepusht.** `src/util.js` + `tools/lane_widths.js` + `data/_searoutes.js` zijn dirty.
- **Doel:** links/rechts apart klemmen i.p.v. rondom, zodat één los eiland niet de hele waaier dichtknijpt —
  Lars: *"voor de westkust van Amerika komen de lijnen samen terwijl dat niet hoeft."* Een echte zeestraat
  heeft land aan béide kanten; een eiland aan één kant hoort alleen díe kant te beperken.
- **Stand:** Baja-spreiding hersteld (**143 km**, banen blijven uit elkaar ✅) maar Japan ging **0 → 52**
  treffers, omdat exact haaks peilen eilanden schuin vóór de baan mist. Laatste wijziging (waaier ±60° per
  zijde i.p.v. één straal) is **nog ongemeten**.
- `SIDE_SIGN = 1` is **empirisch bevestigd** (154 vs 1.571 landtreffers bij omdraaien) — niet opnieuw uitzoeken.
- **Beslis eerst of dit nog nodig is** als LAR-483 (netwerk-aanpak) doorgaat — de klem kan van vorm veranderen.

## 🔍 OPEN — Malakka/Singapore-straat: 6 scherpe knikken over (2026-07-18)
- Deels **echt**: de Straat van Malakka en de Singapore-straat maken werkelijk scherpe bochten tussen Sumatra
  en Maleisië. Niet blind gladstrijken — dat zou een wáár detail wegpoetsen.
- Pas beoordelen **ná** LAR-483; het netwerk kan de geometrie daar alsnog veranderen.

## 🔍 OPEN — Valparaíso→Rotterdam scheert langs de Caribische eilandjes (2026-07-18)
- Middellijn zelf (41 treffers bij lane 0), rond Panama/Caribisch gebied. Los van de Japan/Baja-problematiek;
  bestond al vóór de lane-fixes. Kandidaat om mee te nemen in de netwerk-verzoening (LAR-483).

## ✅ OPGELOST (2026-07-18) — trans-Pacific bundel over Japan (stond hier sinds 17 juli)
- **Twee oorzaken, geen van beide de vermoede "stale cache van de curve-fix".**
- **(1) De lane-waaier.** Elke stroom wordt als 7 parallelle vaarbanen getekend (±95 km); die waaier wist niets
  van land, dus bij Tsugaru (~20 km breed) en de Seto-binnenzee gingen de **buitenste** banen over Honshu/Hokkaido.
  **Mijn eigen verificatiefout:** de eerste controle testte alleen de **middelste** baan en verklaarde het
  opgelost. → **Regel: meet altijd over alle 7 banen.**
- **(2) Cache — maar structureel.** `index.html` laadde assets zónder versie terwijl Pages `max-age=600` stuurt;
  Lars zag daardoor **drie fixes lang** de vorige versie. Opgelost met `tools/stamp_assets.js`.
- Stand na de fixes: Japan **0** landtreffers (van 8), wereld 406 → 108.

## ✅ GEFIXT (2026-07-17) — curve-bemonstering sloeg invoerpunten over (`util.js`)
- `makeRouteCurve` bemonsterde uniform (cap 260 = 1 punt/~75 km op trans-Pacific) → de dichte kustpunten van
  MARNET-paden werden overgeslagen → CatmullRom-spline sneed over schiereilanden (Vogelkop), óók toen de data al
  gerepareerd was. Oude A\* maskeerde dit met ~130 km geforceerd water. **Fix: adaptieve bemonstering, elk
  invoerpunt behouden.** Les: **verifieer op de gétekende curve, niet alleen op de polyline-data.**

## ✅ GEFIXT (2026-07-17) — ruwe MARNET-paden: zigzags + landkruisingen (baker)
- Yangtze-monding 140°+105° binnen 50 km (de "rare draai"); Vogelkop-segment 399 km over land; Isla Guadalupe.
- Fix in `tools/bake_searoutes.py`: de-zigzag (alleen als kortsluiting over water) + lokale A\*-omleiding
  (0,1° waterraster, kustbuffer 1 cel) + kanaal-uitzondering Panama/Suez. Checker: `tools/check_corridors.js`.
- Restant (bewust geaccepteerd): haven-uitvaart-bochtjes op punt 1 (110–160°, tientallen km, onder de marker).

## ⚠️ RISICO — GitHub-egress flaky op deze machine (2026-07-17)
- `git push`/`gh`/`curl` naar github.com vallen periodiek weg (Recv failure/TLS timeout), minuten later weer OK.
- Workaround die werkt: **achtergrond-retry-loop** (1 poging/min, max 30) — alle 3 deploys kwamen zo door.

## ✅ GEFIXT (2026-07-17) — LAR-479 tegel-patch werd afgekapt bij inzoomen · commit `297016f`, bevestigd door Lars
- **Symptoom (Lars):** *"het bovenste gedeelte scherp en de onderste wazig … die grens van wazig en scherp beweegt
  mee als ik de wereldbol draai, alsof je echt een sweet spot moet hebben."*
- **Twee samenwerkende oorzaken** (de vorige sessie vond er één; de tweede kwam er bij het fixen bij):
  1. **Budget < één patch.** `updateDetail` vulde rij voor rij van **noord naar zuid** met `budget--` per tegel,
     terwijl een normale patch **42–72** tegels vraagt en `maxTiles` op **40** stond → de zuidelijke rijen kregen
     structureel niets → alleen de shell (`shellMaxZ: 3`, ~20 km/px). De grens bewoog mee omdat de bbox elke update
     rond `viewCentre()` wordt gelegd. **Er was dus geen sweet spot** — je zat altijd in de bug en zag alleen de
     bovenkant ervan. *(De eerdere "camZ 4,0/5,6/6,5 zijn gekapt, de rest niet"-analyse was te optimistisch: door
     oorzaak 2 is vrijwel élke view gekapt.)*
  2. **`detailZoomFor()` miste `cos(lat)`.** Een Mercator-tegel op 60° breedte beslaat de helft van de grond van
     eentje op de evenaar → hoe noordelijker, hoe méér tegels voor dezelfde scherpte. Verspild werk dat het budget
     extra opblies; daarom was Noorwegen **veel** erger dan China.
- **Fix:** `cos(lat)` in `detailZoomFor()` · `maxTiles` 40 → **96** · de patch vult **van het midden naar buiten**
  (sortering op afstand tot `viewCentre`) → het plafond is weer een noodrem i.p.v. een dagelijkse limiet, en bij een
  hit verdwijnen de **buitenste** tegels langs de bolrand i.p.v. de halve onderkant.
- **Bewijs (raycast-grid, 412×915, oude code echt teruggezet via `git stash` op een schone origin):**

  | view | oud (tegels · boven/onder) | nieuw |
  |---|---|---|
  | China camZ 3,6 | 40 (cap) · 100% / 100% | 42 · 100% / 100% |
  | maximale zoom | 40 (cap) · 100% / **50%** | 49 · 100% / 100% |
  | evenaar/Andes | 36 · 100% / 100% | 30 · 100% / 100% |
  | hoge breedte (Noorwegen) | 40 (cap) · **33% / 0%** | 36 · 100% / 100% |

  3 van de 4 oude views zitten **exact op de cap van 40**. Nieuw: 100%/100% op alle 7 views, piek 72 tegels.
- **`shellMaxZ: 3` bewust níét aangeraakt** — de shell is nu nergens meer zichtbaar in beeld, dus de oude
  LAR-394-afweging (meer tegels = zwaarder op mobiel) hoeft niet opnieuw gemaakt.

## 🐛 OPEN (Low) — een mislukte tegel wordt nooit opnieuw geprobeerd (`src/tiles.js`)
- Bijvangst van de LAR-479-analyse, **andere oorzaak, apart defect** — bewust níét meegefixt (scope).
- `ensureTile` doet `if (liveMap.has(id)) return;` en de error-callback alleen `console.warn` → de mesh blijft
  permanent op opacity 0 en herstelt nooit. Op trage/geknepen verbindingen (mobiel, Esri-throttling) een echte kwaal.
- **Nu iets relevanter geworden:** met `maxTiles: 96` kunnen er meer gelijktijdige requests uitstaan dan voorheen.
  Nog niet waargenomen in de praktijk (Lars' bevestiging was schoon), dus geen issue aangemaakt.

## ✅ GEFIXT (2026-07-17) — LAR-481 marker-LOD vuurde averechts · commit `8dda38e`, bevestigd door Lars
- **Symptoom (Lars):** de Norilsk-mijn verschijnt pas bij inzoomen.
- **Dit léék tier-by-design** (staat letterlijk zo in de kop-comment van `markers.js`), maar was het **omgekeerde**:
  `forced` (node hangt aan een zichtbare stroom, uit `usedNodeIds`) overrulet tier volledig, en dat gold voor
  **57 van de 63** koper-nodes; **nul** nodes waren tier 1 zónder stroom. De tier-regel raakte dus **alléén nog de
  6 context-mijnen zónder flows** — mijnen met een eigen smelter ter plekke (Chuquicamata/Calama, KGHM/Głogów,
  Norilsk binnenlands, Aitik, Julong, Cobre Panamá), zelfde klasse als Argyle/Nickel West/Iran.
- **De willekeur:** El Teniente (share 2,1 · tier 2 · stroom) altijd zichtbaar · Norilsk (2,0 · tier 2 · géén stroom)
  pop-in · Los Pelambres (1,6 · tier 2 · stroom) altijd zichtbaar · Chuquicamata (1,6 · tier 2 · géén stroom) pop-in.
  Identieke share, identieke tier, tegengesteld gedrag — zichtbaarheid hing af van of een mijn tóévallig een lijntje
  had. De LOD ontdubbelde niet; hij vuurde alleen op de nodes die dat het minst verdienden.
- **Fix (Lars koos uit 3 opties):** markers verdwijnen niet meer op tier; **`tier` stuurt alleen nog de labels**
  (`labelZoomByTier` + botsingsdetectie) — die houden de kaart werkelijk rustig, niet de bolletjes. `tierZoom`
  (config) + de `forced`/`usedNodeIds`-uitzondering **verwijderd**: het gevaar dat ze afdekten ("een lijn eindigt in
  het niets") kan niet meer optreden. NB-comment op beide plekken.
- **Geverifieerd:** markers-per-zoomstand constant (z 8,0→2,75) · labels blijven gefaseerd (0 → 12 @ z=4 → 29 @
  z=2,75) · **regressie 14 grondstoffen: totale pop-in 0**.
- **Kosten:** uitgezoomd 6 extra bolletjes bij koper. Als dat te druk blijkt → stromen ook tieren, **ná M18**
  (raakt `flows.js` = de pilot-code).

## ✅ GEFIXT (2026-07-17) — draaien was zoom-onafhankelijk (`src/globe-core.js`) · commit `297016f`
- **Symptoom (Lars):** *"als je een stuk bent ingezoomd dan is het draaien super gevoelig."*
- **Oorzaak:** `rotation.y += dx * 0.005` = een vaste hoeveelheid radialen per pixel, ongeacht zoom. Op `minZoom`
  (2,75) zie je ~9× minder wereld, maar draaide een veeg evenveel graden.
- **Fix:** schaalt met de afstand camera→oppervlak (`dragSpeed` + `dragRefZoom` in config), **bewust geankerd op de
  standaardzoom** — Lars klaagde alleen over ingezoomd, en de fysisch "correcte" 1:1-grab zou de standaardzoom 4,4×
  trager maken. Gemeten: 28,65°/100px @ standaard (identiek aan oud) · 3,13° @ volle zoom · ratio **0,109** = exact
  de ratio zichtbare wereld.

## ⚠️ Route-engine: aantoonbaar onrealistisch (2026-07-17) → M18
- **`openRadiusDeg: 1.2`** = ~130 km geforceerd water rond élk knelpunt → A\* vaart dwars over land/eilandjes.
  Hoofdboosdoener achter *"een boot zou daar nooit zo varen"*.
- **8-richtingen-A\*** → trapjes (Golf→Rotterdam = 33 richtingswissels). **Grof raster + gretige heuristiek + géén
  echte vaarlanen** → kaarsrechte runs langs een breedtegraad/meridiaan.
- **`wp-pac-zuid` dwingt een omweg van ~1.090 km af** (Antofagasta→Shanghai +8% vs. grote-cirkel; searoute +2%).
  De `via`-ketens zijn grotendeels handmatige compensatie voor een slechte router.
- **Risico bij M18:** de **vaarbanen-waaier** (`laneShape`, `util.js`) die bij een knelpunt samenknijpt is een
  kernbeeld — die moet ook op gebakken polylines nog kloppen. Subtielste regressie-val. Verder: uranium's Kaspische
  oversteek (ingesloten zee) heeft searoute's netwerk waarschijnlijk niet → expliciet checken.
- **Verificatie-val (kostte de vorige pilot z'n geldigheid):** vergelijk nooit tegen een kale origin→dest A\*-run;
  de atlas routeert altijd langs de `via`-keten.

## M17 · Kolen — geverifieerd headless (2026-07-16)
- Volledig gebouwd + geverifieerd (eigen server poort 8735 = `grondstoffen-atlas-4`): **kolen 111 legs / 0 kapot /
  0 straight / 0 degen / 0 unresolved via** (34 nodes / 33 flows / 6 tensions). Regressie schoon: alle
  op dat moment geladen grondstoffen (12 tijdens de test) op hun bekende baseline; kolen voegt 0 kapot/straight/degen toe.
- **1 route-bug onderweg gevonden + gefixt (zilver-Tacoma→Astoria-echo):** de 2 kapotte legs zaten op `coal-port-vancouver
  → wp-pac-noord`. Empirisch gediagnosticeerd door kandidaat-coördinaten door `Routing.sea` te halen: **Roberts Bank /
  Westshore ligt ingesloten in de Salish Sea** (achter Vancouver Island) en valt dicht in het grove 0,25°-raster
  (robertsbank→open zee = `null`). Verplaatst naar **Ridley Terminal / Prince Rupert** (open kust) — dat is bovendien
  feitelijk dé Canadese cokeskool-exporthaven. Daarna 0 kapot. **Les (herbevestigd):** ingesloten binnenzeeën (Salish Sea,
  Puget Sound, Bohai) sluiten in het grove raster; test een haven-coördinaat door de router vóór je hem vastzet, en kies
  een open-kust-terminal.
- **Risico (parallel werk, sectie J):** deze sessie draaide náást **3** andere (grafiet mid-wrapup, diamant, gas). De
  gedeelde `index.html` kreeg drie script-regels (diamond/coal/gas) in één hunk → alléén de coal-regel gestaged via een
  gerichte `git apply --cached`-patch. `atlas-standalone.html` (gitignored) bevatte tijdens de build ook diamant/gas-data;
  geen probleem want het is een lokaal artefact. **Blijf bij nieuwe grondstoffen selectief stagen (nooit `git add -A`).**

## M14 · Grafiet — geverifieerd headless (2026-07-15)
- Volledig gebouwd + geverifieerd (eigen server poort 8735, `grondstoffen-atlas-4` toegevoegd aan `launch.json`):
  **grafiet 77 legs (57 zee + 20 land) / 0 kapot / 0 straight / 0 warnings** (31 nodes / 26 flows / 6 tensions);
  toggle aan (recycling) = **80 legs** (+3 recycle-flows). Regressie schoon: **0 kapot over álle grondstoffen**.
- **Browser-pane-cache-gotcha (nieuw, belangrijk):** de Browser-pane cachete de oude `graphite.js` (basis 10/3)
  hardnekkig — óók na `location.reload(true)` bleef `getResource('graphite')` de oude data tonen. Dit is een
  **pane-cache, geen codeprobleem**. Workaround die werkte: de verse schijf-data via **synchrone XHR** (`?ts=`-buster)
  ophalen, `window.REGISTER` tijdelijk shadowen om het resource-object te capturen, en de leg-check dáárop draaien
  (repliceert exact de `flows.js`-leglogica: `Routing.sea`/`Routing.land`, `isSeaPoint`, gathering-legs). Voor de
  live render: het verse resource in `RESOURCES` splicen + de grafiet-pill klikken (ATLAS re-render). **Les:** vertrouw
  headless niet op een gewone reload voor verse data-files; fetch+capture of splice-in.
- **1 route-bug onderweg gevonden + gefixt:** `gr-ref-japan → gr-mkt-korea-japan` stond op `mode:"road"`, maar Japan→Korea
  gaat over zee (Straat van Korea) → de landrouter vond geen pad (kapot). Beide punten zijn `coastal` → mode veranderd naar
  `ship` (directe korte zee-hop, géén via). Daarna 0 kapot. **Les (herbevestigd, koper/PGM-echo):** een `road`/`rail`-flow
  tussen twee landen gescheiden door zee is onmogelijk; zulke hops moeten `ship` zijn (beide endpoints `coastal`/`port`).
- **Recycling-toggle hergebruikt met 0 engine-wijziging** (REE/PGM-patroon, 3e datagedreven hergebruik van dít patroon):
  de "recycling"-chip verschijnt automatisch voor grafiet omdat het `layer:"recycle"`-nodes/-flows heeft; toggle uit=23 flows
  (77 legs), aan=26 flows (80 legs). Blurb + 6 tensions renderen, geen console-warnings (geen onbekende via-/node-ids).
- **Co-locatie bewaakt:** grafiet-eigen nodes ~30-45 km uit elkaar gehouden (gr-ref-korea vs gr-mkt-korea-japan ~58 km;
  gr-ref-shandong vs gr-nc-china) → 0 `degDist:0`-arcs (0 degenerate in de check).
- ⚠️ **Visuele bevestiging blijft open (LAR-454)** — WebGL-screenshot lukt niet headless (timeout, zelfde gat als M5–M13).
  Nu triviaal via de live URL: de twee feedstock-stromen die op China convergeren, het Balama→Vidalia-draadje rond de Kaap,
  de ex-China buildout-waaier, de recycling-toggle.
- ✅ **Concurrency (sectie J) schoon:** werktree schoon bij start én vóór commit; grafiet raakt de engine niet
  (0 engine-wijziging) → alléén eigen bestanden gestaged. **Repo-correctie:** de docs zeiden "lokaal-only", maar de repo
  is sinds M13 live op GitHub Pages → deze sessie **wél gepusht** (code + docs).

## M13 · Zilver — geverifieerd headless (2026-07-15)
- Volledig gebouwd + geverifieerd in de draaiende atlas (eigen server poort 8734): **zilver 85 legs / 0 kapot /
  0 straight / 0 warnings** (42 nodes / 37 flows / 6 tensions). Legs-check repliceert exact de `flows.js`-leglogica
  (`Routing.sea`/`Routing.land`, `isSeaPoint`, gathering-legs). Regressie schoon: de andere uitgewerkte grondstoffen
  (kobalt/koper/nikkel/REE/uranium/goud) allemaal 0/0; de bekende baseline (lithium 4× same-cell + grafiet/PGM op "basis")
  ongewijzigd — zilver voegt **0** toe.
- **2 route-bugs onderweg gevonden + gefixt** (empirisch getest vóór de fix, niet gegokt — kandidaat-coördinaten door
  `Routing.sea` gehaald): (1) **VS-raffinage Tacoma → Astoria/Columbia-monding** (47.25/-122.44 → 46.20/-123.90): Puget
  Sound valt in het grove 0,25°-raster dicht → Greens Creek→Tacoma per zee onbereikbaar (0 legs); open Pacific-kust wél (20).
  (2) **China-solar Suzhou-binnenland → Jiangsu-kust Nantong** (31.30/120.60 → 32.00/121.60): het binnenland is per zee
  onbereikbaar → de 2 ship-flows ernaartoe braken; de kustpositie routeert wél (de grote rail-flows werkten al). **Les/risico
  (herbevestigd):** elke ship-endpoint moet op een echt zee-cel liggen; diep-in-baai-steden (Puget Sound) en landinwaartse
  clusters (Jiangsu-solar) falen in het grove raster → verplaats naar de open kust of route via een haven.
- **Exchange-toggle hergebruikt met 0 engine-wijziging** (nikkel-patroon, nu 2e datagedreven hergebruik): de "beursvoorraden"-chip
  verschijnt automatisch voor zilver omdat het exchange-nodes/-flows heeft; toggle uit=34 flows, aan=37; blurb + 6 tensions renderen.
  Geen console-warnings (geen onbekende via-/node-ids).
- **Co-locatie bewaakt:** zilver-eigen nodes rond Shanghai (ref-china/SGE/solar) en Mumbai (markt/haven/recycler) staan ≥1 rastercel
  uit elkaar → geen `degDist:0`-arc.
- ⚠️ **Visuele bevestiging blijft open (LAR-439)** — WebGL-screenshot lukt niet headless (timeout, zelfde gat als M5–M11).
  Op Netlify/mobiel door Lars: de diffuse by-product-mijn-origin (geen winnings-trechter), de convergentie op Peñoles/KGHM/Korea/China,
  de dikke solar-boog SGE→Jiangsu, de India-sieradenstroom, en de kluis-toggle (LBMA/COMEX/SGE) die de aftap toont.
- ⚠️ **Concurrency (sectie J):** een parallelle sessie werkte tegelijk aan uranium's engine-laag op de gedeelde bestanden
  (`config.js`, `src/{flows,main,markers,ui}.js`, `data/uranium.js`, dirty). Zilver raakt de engine niet (0 engine-wijziging) →
  alléén de eigen bestanden gestaged (`data/silver.js` + `design/zilver.md` + `index.html` + `build-standalone.py`); nooit `git add -A`.

## M8 · Zeldzame aardmetalen — geverifieerd headless (2026-07-15)
- Volledig gebouwd + geverifieerd in de draaiende atlas (poort 8732): **rare-earths 90 legs (39 land + 51 zee) / 0 kapot /
  0 straight**. Structuurcheck groen: 41 nodes / 38 flows / 6 tensions, geen dubbele ids, geen onbekende flow-endpoints,
  `grens-ruili` resolvet in de tension. Regressie schoon: globaal 5 kapot = de bekende `degDist:0` lithium(4)+goud(1)-baseline
  (**0 nieuw**); 25 straight = de basis-grondstoffen (nikkel/grafiet/PGM/olie, ongewijzigd).
- **Onderweg gevangen (niet echt kapot):** 5 legs waren aanvankelijk `degDist:0` same-city hops (ref/magneet/recycler in
  dezelfde rastercel: Baotou/Ganzhou/MP/La Rochelle/Fort Worth). Opgelost door die 5 tweede-nodes ~30–45 km binnen dezelfde
  stad te verschuiven → zichtbare korte landroute + teller schoon op 0. **Les/risico:** twee nodes van dezelfde grondstof
  binnen één 0,25°-cel geven een onzichtbare arc; hou co-located functies (scheiding+magneet) minstens een cel uit elkaar.
- **Recycling-toggle** (`layer:"recycle"`) getest: aan → +3 recycle-flows + 3 recycler-nodes; uit → weg; de 4e (MP-recycling,
  `status:"project"`) is extra project-gated (verschijnt alleen met recycling ÉN projecten aan — correct gedrag). cb/beurs-chips
  blijven correct weg bij REE. **Risico-nul t.o.v. koper:** de node-gate op `node.layer==="recycle"` (niet op `type==="recycler"`)
  laat koper's always-on recyclers ongemoeid — geverifieerd dat koper's legs/markers ongewijzigd zijn.
- ⚠️ **Visuele bevestiging blijft open (LAR-421)** — WebGL-canvas laat zich niet volledig headless screenshotten (zelfde gat
  als M5/M6/M7/M9). In de browser-pane wél zichtbaar bevestigd dat de Ganzhou-trechter (met knelpunt-ring), de Myanmar/Vietnam-
  landstromen, de NdFeB-waaier, de Mountain-Pass-Pacific-route en het EU-draadje via Suez renderen. Op Netlify/mobiel te checken
  door Lars: convergeren de scheidings-bogen echt op Zuid-China?, loopt de Dy/Tb-landstroom over Ruili?, is de rondreis VS↔China
  zichtbaar?, waaiert de NdFeB uit naar EV/wind/defensie?, lopen de scheeps-voyages voor REE?

## M9 · Uranium — geverifieerd headless (2026-07-15)
- Uranium volledig gebouwd + geverifieerd in de draaiende atlas (mijn eigen server poort 8743, want 8732 bezet door de
  M8-sessie): **uranium 54 legs / 0 kapot** (20 zee + 34 land, **0 straight** → de nieuwe Kaspische oversteek routeert écht
  over water, geen fallback). Regressie schoon: de 5 overige nulls zijn de bekende `degDist:0` same-city hops uit de
  M5/M6-baseline (lithium 4, goud 1), **niet nieuw**. Structuurcheck groen (geen onbekende node-/via-/tension-ids, geen duplicaten).
- **Nieuwe vaarpunten in `_chokepoints.js`** (`wp-kaspisch-n/-m/-z` + `wp-dardanellen`): alleen uranium verwijst ernaar via
  `via`, dus geen impact op de andere 9 grondstoffen (geverifieerd: hun leg-tellingen ongewijzigd). Risico bij een volgende
  ingesloten-zee-grondstof: dezelfde geforceerd-water-truc, let op contiguïteit (overlappende discs, zie de Saint-Laurent-keten).
- ⚠️ **Visuele bevestiging blijft open (LAR-415)** — WebGL-canvas laat zich niet headless screenshotten (zelfde gat als
  M5/M6). Op Netlify/mobiel te checken: verrijkings-flessenhals (dun ringetje nodes, Rusland dikst)?, de twee Kazachstan-
  routes (Rusland-transit vs. Trans-Kaspische omweg)?, de VVER-lock-in-lijn naar Midden-Europa?, de CANDU-uitzondering?,
  scheeps-voyages voor uranium?
- ✅ **Militaire-kringloop-toggle GEBOUWD (LAR-414 Done, 2026-07-15, commit `6a6d062`)** — de uitgestelde engine-laag afgemaakt
  zodra de gedeelde bestanden schoon waren; het vijfde optionele-laag-patroon (`type:"military"`/`layer:"secondary"`). Headless
  geverifieerd (uranium 60 legs / 0 kapot / 0 straight; toggle +4 nodes/+5 flows; chip alleen bij uranium). Niet meer openstaand.

## M7 · Koper — geverifieerd headless (2026-07-14)
- Koper volledig gebouwd + geverifieerd in de draaiende atlas (poort 8742): **koper 145 zee/land-legs, 0 kapot**;
  regressie **388 legs / 0 kapot** over alle 10 grondstoffen; beursvoorraden-toggle +6 nodes/+7 flows, chip
  "beursvoorraden" verschijnt (CB-chip niet — correct); geen console-errors. Structurele Node-check ook groen
  (geen onbekende ids/via-punten/duplicaten/coördinaatfouten).
- **4 route-bugs onderweg gevonden + gefixt** (route=null over lange afstand → een ship-leg landde op een landinwaarts
  punt): (1) Walvis→VS-markt zonder VS-haven → gereroute naar Rotterdam/Duitsland; (2+3) Japan/Korea-markt landinwaarts
  + Korea→Japan kan niet over land (geen landbrug) → markt kustpunt Nagoya (`coastal:true`) + Onsan→markt naar `ship`;
  (4) beursmagazijnen die per schip beleverd worden → `coastal:true`. **Les/risico:** elke ship-leg moet op een
  kustpunt (`port`/`coastal`/`wp-`) eindigen, anders valt hij op de landkaart terug (of vindt geen pad) — checken bij
  elke nieuwe schip-grondstof.
- ⚠️ **Visuele bevestiging blijft open** — WebGL-canvas laat zich niet headless screenshotten (zelfde gat als M5/M6).
  Op Netlify/mobiel te checken: Andes-concentraatbundel convergeert op de Chinese smelters?, Copperbelt-kathode kruipt
  over land naar de kust (Kasumbalesa)?, beursvoorraden-toggle + koperkleurige spoel-markers?, scheeps-voyages lopen?
- ⚠️ **Concurrency:** een tweede chat werkte deze sessie in dezelfde projectmap aan M8 (zeldzame aardmetalen). Bij
  gedeelde memory/CLAUDE-bestanden chirurgisch bewerken (geen full-file overwrites) om elkaars werk niet te clobberen.

## M6 · Goud — geverifieerd headless (2026-07-14)
- Goud volledig gebouwd + geverifieerd in de draaiende preview: 31 luchtroutes (alle `air`, bogen tillen
  2,5–12,7% op), CB-toggle 31→35 routes + 12 voorraad-nodes, "✈ vluchten"-teller, regressie **371 legs / 0 kapot**
  over alle 10 grondstoffen (lithium/kobalt onaangeraakt). `atlas-standalone.html` laadt schoon.
- ⚠️ **Visuele bevestiging blijft open (LAR-403)** — WebGL-canvas laat zich niet headless screenshotten (zelfde gat
  als M5). Op Netlify/mobiel te checken: Ticino-trechter mooi in beeld?, luchtbogen plausibel (bendten netjes via de
  hubs, geen rare knikken)?, labels/knopen leesbaar?, voyages-vliegtuigjes lopen?
- **Aandachtspunt `atlas-standalone.html`:** gegenereerd artefact (1,4 MB) — overweeg te gitignoren zodat de repo
  niet vervuilt; niet handmatig editen (regenereer via `build-standalone.py`).

## M5-port naar modulaire code — geverifieerd (2026-07-14)
- M5-fixes zitten nu ook in de **modulaire bron van waarheid** (waren alleen in de single-file). Headless
  routeverificatie in de draaiende atlas: **214 legs gerouteerd, 0 kapotte routes**; 3 M5-bugroutes
  geometrisch correct (Antwerpen→Newark + Kaap→Deense Straten via Nauw van Calais, Cuba→Montréal de
  Saint-Laurent op). Eén restfout (kobalt Niihama→Osaka, null-route) gefixt met de **Seto-brug**.
- ⚠️ **Visuele bevestiging blijft open** — preview-screenshot liep vast (WebGL-time-out). Op Netlify/mobiel
  te bekijken (zit al in LAR-403). Dit is de enige rest vóór `globe-oud`/single-file opgeruimd mag worden.

## M5-bugs — OPGELOST + geverifieerd (2026-07-14, aparte CC-sessie) → LAR-393/394/395/396 Done
**Aanpak 395/396** (kobaltroutes Cuba→Canada + Europa→Amerika): Straat van Dover + St. Lawrence als knelpunt
open geforceerd (zelfde patroon als Lombok/Malakka); regressiecheck 0 kapotte routes over alle stromen.
**Aanpak 393/394** (tegelnaad + drempel): shell-laag (hele bol grove tegels) + scherpe detailpatch; blue-marble
prikt nergens meer door. ⚠️ Visueel **niet met screenshot** bevestigd (WebGL-capture liep vast) — numeriek/geometrisch getoetst.
Referentie-symptomen hieronder:
- **LAR-393 (High)** — bol toont **twee verschillende kaarten naast elkaar** bij vaste zoom: de ene helft
  tegellaag (Esri, scherp), de andere basemap-satelliettextuur, met zichtbare naad/overhang. Beeld springt
  vaak van view. Vermoedelijke oorzaak: tegellaag (`tiles.js`, z=6.2) en basemap (`basemap.js`) te
  gescheiden. (Waargenomen op mobiel, 14 juli 2026.)
- **LAR-394 (Medium)** — tegellaag (mooier dan basemap) eerder tonen: drempel `z=6.2` omhoog (~7.5–8),
  evt. standaard actief zodra bol interactief wordt. **Afweging:** eerder tegels = meer tegelverzoeken =
  zwaarder op mobiel.
- **LAR-395 (High)** — kobaltroute **Zuid-Amerika → Noord-Amerika** loopt niet plausibel (knik bij Great
  Lakes/Nova Scotia). Checken: lat/lon omgedraaid of verkeerd teken, haven aan verkeerde kust,
  raster/waypoint. Bestanden: `data/kobalt.js`, `searoute.js`.
- **LAR-396 (High)** — kobaltroute **Europa → Amerika** klopt niet. Transatlantisch is de simpelste route;
  als díé eruitziet als een omweg wijst dat op iets structureels (great-circle vs. rasterpad). Bestand:
  `data/kobalt.js`, `searoute.js`.

## Risico's / aandachtspunten
- **Coördinaatfouten** (lat/lon-swap, verkeerd teken west/oost) zijn een terugkerende bron van verkeerde
  routes. Bij elke nieuwe grondstof checken.
- **Rasterresolutie 0,25°** verliest smalle doorgangen; nieuwe knelpunten moeten expliciet in
  `_chokepoints.js` als water geforceerd worden.
- **Gewogen A\* is niet gegarandeerd optimaal** — bewust ingeruild voor "wel een route vinden". Bij vreemde
  paden eerst hier kijken.
- **Goud-luchtvracht — OPGELOST (M6):** de route-engine was zee/land-A\*; goud kreeg een **3e route-modus**
  (great-circle-boog, `mode:"air"`, buiten het A\*-raster om). Korte hops blijven road/rail. Zie decisions.md.
  Restpunt (niet-blokkerend): het is nu één boog over de via-luchthavens (geen touch-down bij elke hub) en
  voyages gebruikt ship-tempo voor lucht — bewuste v1-vereenvoudiging, later te verfijnen.
- **Mobiele performance:** tegellaag + veel stromen + voyages kunnen zwaar worden; bewaken bij uitbreiding.
- **Modulair vs single-file — OPGELOST:** modulair is nu de bron van waarheid in de projectmap-git-repo, M5-fixes
  geport. Single-file blijft alleen als referentie tot visuele bevestiging.
- **Visuele M5-bevestiging ontbreekt** (screenshot lukt niet in de preview → WebGL-time-out). Bevestig op
  Netlify/mobiel voordat `globe-oud`/single-file definitief weg mag.

## Verholpen (referentie)
- Schaalbug (delen door camerastand i.p.v. afstand tot oppervlak) — opgelost in M2 (`scaleFor()`).
- Lange oceaanroutes vielen terug op rechte lijnen — opgelost met gewogen A\* (M3).
- Zeven Australische stromen als één dikke worm over Lombok — opgelost met vaarbanen (`laneShape`, M3).

## 2026-07-21 · Havenlijst-bron (searoute ports.geojson) — twee OPEN gebreken
De havenpoort filtert alleen "ligt niet aan water" (630 punten). Blijft open: (1) posities zijn
plaatscentroides, geen kades -- een stip landt naast de haven; (2) geen enkel attribuut scheidt
vrachthaven van jachthaven. Beide vragen een betere bron (WPI-verificatie = eerste actie).
Bekend dekkingsgat: Saldanha Bay (ijzererts, ZA) ontbreekt volledig (112 km naar dichtstbijzijnde).

## 2026-07-21 · Uit het vierpanel, geldt netwerkbreed
- De heap in zoekRoute is n*8 slots ZONDER bounds check; overloop = stille no-op op een typed
  array = verkeerde routes zonder foutmelding. Assert toevoegen bij LAR-520/zoekKeten-werk.
- dichtstbijzijndeKnoop() scant lineair zonder netonderscheid -- kaartklik geeft sinds het
  riviernet vaak een rivierknoop. Netfilter nodig.
- meta.passages telt 53.989 entries waarvan 52 echte zeestraten; wie erover itereert toont het
  halve riviernet.

## 2026-07-25 — AIS-pilot: bekende opens
- **Ankervelden/havenbekkens** zijn nog kluwens in de pilot-laag (Shanghai rechts,
  R''dam-bekkens) — filter via convergentiegedrag komt in de graaf-stap.
- **Open zee snipperig** (Patache): diffuus verkeer past niet in het geul-recept;
  eigen recept met bredere gladstrijking nodig.
- **Mini-gaatje in de Tongling-oostgeul** + 2-puntslijnen-fragmentatie (8.467/9.631)
  — beide voor de graaf-stap (healen/consolideren).
- **Meetles:** met het browserpaneel dicht is de drawingBuffer 1×1 én draait rAF niet
  (vliegNaar doet niets) — pixel-metingen dan zinloos; verifieer via console/preview-PNG''s
  of laat Lars live kijken.
