# Next actions — Grondstoffen Atlas
*Last updated: 2026-08-06 (laatst: guards + Tongling fase D, `?v=111`)*

## 🔴 NIEUW 2026-08-06 (laatst) — na de guards en Tongling fase D

> ⚠️ **VERVALLEN PUNTEN UIT DE LIJST HIERONDER, per besluit van Lars (2026-08-06):**
> punt 4 (been-ids → *"eén vlag, vijf herbakes"*) en punt 6 (de bak-recepten van de drie
> resterende stromen) zijn **geschrapt**. Bakken is geen deliverable meer — *"de ene bak maakt
> de andere weer invalid"*. Moeten been-ids/fase/volume er later tóch komen voor de visuals, dan
> in een **los metadatabestand** naast `stroomroute-*.json`, niet via een herbake.

1. **Lobito fase D als tijdgeboxte bronronde (halve dag).** Eén bronvondst scheidt "twee
   varianten in de brief" van "getekend been"; het anker (51.82811, 6.26387) ligt er, in
   z19-gebied. Komt de bron niet: **laat hem als twee expliciete varianten staan en teken hem
   niet** — dat is de correcte uitkomst, geen mislukking.

2. **Las Bambas → Matarani kan nu pas.** De spoordrempel was de blokkade (het tool leverde daar
   een gedegenereerd been); die is gefixt. Hergebruikt fase C/D/E van Tongling → de eerste echte
   §1b-samenvloeiing in koper, dus lage marginale kosten.

3. **De LG-perceelvraag in Nanjing** (lithium) — productvraag, geen meetkunde. 750 m tussen drie
   kandidaten, groter dan elk procesgat dat die keten bewust laat staan.

4. **De kathode-expeditie (Tongling én Guixi) en het folie-losdock vragen een NIET-Esri-bron.**
   Vijf bevestigde zoomplafond-plekken nu — dit is een eigenschap van Esri boven Chinees
   binnenland, geen incident. Kandidaten: Amap/Baidu met sleutel (⚠️ GCJ-02-conversie), een
   Tianditu-token (CGCS2000 ≈ WGS-84, geen datumval), of een 总平面布置图 uit een EIA-bijlage.
   Het folie-EIA noemt **twee poorten** (翠湖二路 zuid, 泰山大道 oost) — goedkoopste gerichte stap.

5. **⚠️ `pyosmium` deblokkeren** — Windows-beleid voor toepassingsbeheer, iets voor Lars. Zolang
   het geblokkeerd is draait het Geofabrik-pad niet en zijn regressies op de vier bestaande
   wegprofielen niet te meten.

6. **Overweeg de spoordrempel relatief te maken**, zoals de haven-riviersnap op 2026-07-24 al is
   geworden (doorgaand component, hooguit 2×+1 km verder, cap 60). De cap voorkomt nu de teleport,
   maar 106 van 642 registerknopen heten nog steeds "geen hoofdnet".

7. **Corrigeer de bron-noot van `cu-tongling-kade`** in `maak_aansluitingen.py` — hij noemt de
   ijzerfabriek 铜冠冶化 als "de smelter erachter". De kade zelf klopt en blijft staan.

8. **`toets_corridor.py` bestaat nog steeds niet.** Vierde ronde op rij ad hoc geschreven.

## 🔴 NIEUW 2026-08-05 (laatst, 2e sessie) — na de koper-fase-D-ronde

1. **De tweede complete keten wordt NIET koper — kies lithium.** Koper Escondida→Guixi kan de
   A–E-belofte niet waarmaken: fase D is 613 m en fase E heeft geen gedocumenteerde afnemer.
   **Lithium benen 5–8** is de enige stroom die het wél kan: gedeblokkeerd sinds beide Chinese
   fabrieksankers gevonden zijn (Tianqi Jiangsu 32.01218/120.45771 · LG-Huayou Wuxi
   31.523573/120.475895), allemaal wegbenen, en de keten eindigt in **Tesla Giga Shanghai** —
   een echte eindfabriek, zoals Lucid bij grafiet. ⚠️ Besluit ligt bij Lars; hij is er in deze
   sessie niet aan toegekomen.

2. **De kathode-expeditie bij Guixi vraagt een NIET-Esri-bron.** Dit is een **zoomplafond**
   (Esri heeft daar geen z19), geen opnamedatum en geen zoekprobleem — Wayback heeft dat
   uitgesloten. Kandidaten: Sentinel-2, een eigen Tianditu-token (CGCS2000 ≈ WGS-84, dus geen
   datumval), of een bedrijfspublicatie met plattegrond. Zolang hij ontbreekt blijft het
   procesgat van 0,584 km staan — en dat hoort zo.

3. **Beslis het productconflict bij Beilun: container of bulk?** Het satelliet-gelegde laadspoor
   is een containeremplacement (78万TEU), de brief zegt "natte bulk in open wagons". Een vraag
   aan de brief, niet aan de satelliet — beslis hem vóórdat fase C herschreven wordt.

4. **Been-ids ontbreken in álle vijf gebakken stromen** terwijl werkwijze §2 ze eist
   (`<stroom-id>-b<n>`) en `hecht_marnet route` er geen vlag voor heeft. Daardoor is een been in
   het gebakken bestand niet terug te vinden in zijn eigen brief. Eén vlag, vijf herbakes.

5. **Dezelfde routeerpunt-behandeling voor de twee andere stromen.** "Been eindigt op zijn
   routeerpunt en niet op zijn anker" is niet Beilun-specifiek: gemeten gaten
   `collahuasi-tongling` **1.818 m** en `lithium-greenbushes-zhangjiagang` **4.933 m**.

6. **De bak-recepten van de resterende DRIE stromen** (`collahuasi-tongling`, `lobito-duisburg`,
   `lithium`) staan nog steeds nergens. Koper is nu dicht; grafiet was het al.
   ⚠️ Herbak ze niet zonder eerst de huidige uitvoer te bewaren.

7. **`toets_corridor.py` bestaat nog steeds niet** (zie de grafietlijst hieronder). De dekkings-
   en verklikkertoets is deze ronde opnieuw ad hoc geschreven — nu wél met `knip_osm_been.py`
   als precedent dat gereedschap in `v2/tools/` hoort.

## 🔴 2026-08-05 (eerder) — na de eerste complete keten

1. **Vraag Lars' check uit.** Zijn oordeel op `?v=106` was *"ziet er goed uit denk ik"* — mild,
   geen enthousiaste go zoals bij eerdere rondes. Vóór de volgende stroom is het de moeite waard
   te weten wat hij mist; anders bouwen we drie stromen in een vorm die hem maar half bevalt.

2. **De drie terugloopjes.** Napoleon Ave (bestond al, verhouding 10,2) · één in het bargebeen ·
   North Little Rock I-30 → I-40 (3,0). Gebruik `toets_knikken.py` en kijk naar de
   terugloop-kolom — de andere 22 omkeringen zijn werkelijkheid en mogen blijven.

3. **De pilotset bevestigen** (`v2/design/pilotronde-analyse.md`): grafiet · kolen · koper ·
   diamant. Grafiet is af; de volgorde daarna is koper (goedkoopst: 3 ankers, 1 kort been) →
   kolen → diamant.
   ⚠️ **Kolen vraagt éérst een halve dag bronwerk, vóór de eerste satellietpass:** geen bron legt
   Cerrejón-kool in de cokesblend van Schwelgern; de gedocumenteerde stroom naar Duitsland is
   krachtwerkkool. Je kunt de keten technisch perfect afmaken en tóch de verkeerde streng hebben
   getekend. Valt de aanname, vervang dan de **kop** en niet de staart — Bowen Basin → Hay Point
   staat al in het register en het Duitse eind draagt alle interessante overslagen.
   ⚠️ **Diamant vraagt gereedschap vóór het eerste been:** luchtvracht als modaliteit (~1 dag;
   kleur + label + een baker die een grootcirkel verdicht — `verdicht()` bestaat al). Dat
   ontsluit daarna goud en PGM in één klap.

4. **De bak-recepten van de vier andere stromen reconstrueren** (koper ×3, lithium) en toevoegen
   aan `v2/tools/bak_stromen.sh`. ⚠️ Herbak ze **niet** zonder eerst de huidige uitvoer te
   bewaren: bij grafiet bleek het wegbeen op schijf niet meer te zijn wat zijn generator maakt.

5. **Lithium benen 5–8 bakken** — gedeblokkeerd nu beide Chinese fabrieksankers er zijn
   (Tianqi Jiangsu 32.01218 / 120.45771 · LG-Huayou Wuxi 31.523573 / 120.475895). Allemaal
   wegbenen, dus de 1-op-1-spoorbaker is hier niet nodig. Daarna is lithium de tweede stroom die
   A–E waarmaakt.

6. **`toets_corridor.py` bestaat niet meer** — hij leefde in een scratchpad en is verdwenen,
   precies de klasse fout die `sat_check.py` naar `v2/tools/` bracht. De dekkings- en
   verklikkertoets is deze ronde ad hoc geschreven; zet hem als repo-tool neer, met een
   puntenlijst + verbodsstralen als invoer, zodat hij deze keer blijft bestaan.

7. **Niet gevonden, en dat blijft zo tot er een andere bron is:** het uitgaande AAM-laaddock bij
   Syrah (probeer de LDEQ-luchtvergunning met plot plan) en beide docks bij Panasonic De Soto
   (wacht op een opname van ná juli 2025 — dit is de Shed 8-8-klasse, geen zoekprobleem).

## ✅ AFGEROND 2026-08-05 — §6b variant 1 (uitgevoerd, commit `48afcf4`)

**Punt 4 van de afwerklijst was géén coördinaatfout maar een eenheden-botsing.** De "110" van de
brief is 110 kt spodumeen**concentraat** (≈17 kt LCE), de `value: 110` in `data/lithium.js` is kt
**LCE** — factor 7,7, dus de gelijke getallen waren toeval. De atlas mist **twee knopen**, geen
andere `via`. **Lars koos variant 1**; het volledige recept mét onderbouwing staat in §6b van
`v2/design/routebrieven/lithium-greenbushes-zhangjiagang.md`. Vier wijzigingen in
`data/lithium.js`, allemaal register-laag (**geen `?v=`-bump**, niets in de browser te toetsen):

1. **node `li-port-zhangjiagang`** — `type:"port"`, China, tier 2, lat **31.96800** / lon
   **120.42050** (de satelliet-gelegde kade; valt samen met aansluiting `li-zjg-kade`, net als bij
   Bunbury — het is een echte kade, dus samenvallen mag).
2. **node `li-ref-jiangsu`** — 天齐锂业（江苏）/ Tianqi Lithium (Jiangsu), Zhangjiagang,
   `type:"refinery"`, tier 2. ⚠️ **Stadsniveau-coördinaat volstaat en dit is NIET geblokkeerd op
   de satellietpass**: het register draagt de plek op wereldschaal, de aansluiting op
   straatniveau (§6.1-besluit van dezelfde dag). De poort 东新路 5 wordt pas de **aansluiting**
   `li-zjg-tianqi` zodra hij gelegd is. Zet die keuze **mét reden in de node-`note`**.
3. **nieuwe flow** `li-greenbushes → li-ref-jiangsu`: `value: 17`, `mode:"ship"`, `stage:"erts"`,
   `via: ["li-port-bunbury","wp-lombok","wp-makassar","wp-scs","wp-taiwan","li-port-zhangjiagang"]`.
   *Waarom 17:* 110 kt × 6,0 % Li2O = 6,6 kt Li2O × 2,473 = **16,3 kt LCE**, en de brief noemt
   zelf 17 kt Li2CO3 uit — Li2CO3 ís de LCE-eenheid. Beide wegen geven ~17.
4. **bestaande flow** `li-greenbushes → li-ref-sichuan`: `value: 55` → **38**.
   *Waarom Sichuan en niet Jiangxi:* het Albemarle-deel gaat naar Xinyu (Jiangxi), dus
   `li-ref-jiangxi` blijft ongemoeid; de Sichuan-flow draagt vandaag de héle Tianqi-helft en zijn
   `note` zegt letterlijk "via Tianqi's eigen raffinaderijen". De Tianqi-helft blijft in totaal
   even groot: 55 = 38 + 17.

Na uitvoering: §6 punt 4 op ✅, §6b inkorten tot besluit + de eenheden-les.

## 🟠 2026-07-30 — de lithiumketen afmaken (✅ punt 1 opgelost 2026-08-05: beide adressen gevonden, zie het recept in v2/design/zoek-chinees-adres-recept.md — benen 5–8 zijn nu te bakken)

1. **Twee Chinese fabrieksadressen geocoderen — Lars zoekt ze op.** 东新路 5 号 (Tianqi
   Jiangsu, Zhangjiagang) en 锡梅路 167 号 (乐友新能源材料 / LG Chem–Huayou, Wuxi). OSM heeft
   ze niet: een volledige scan over de china-extract vond ze niet, terwijl hij de LG-cluster
   in Nanjing wél vond. Zodra de coördinaten er zijn: **z16-pass** per punt, dan **benen 5–8
   bakken** (Zhangjiagang-kade → Tianqi → Wuxi → Nanjing → Giga Shanghai).
2. **Shed 8-8 in Bunbury vraagt een andere bron dan Esri.** De nieuwste Wayback-release
   (2026-06-30) is identiek aan de live laag, dus de loods staat op geen enkele Esri-capture.
   Sentinel-2 of een havenplattegrond van Southern Ports.
3. **Welke van de 16 Zhangjiagang-ligplaatsen déze lading krijgt** is niet gepubliceerd. Voor
   de kaart niet nodig — het anker ligt op een satelliet-gelegde bulkkade van dezelfde
   operator; alleen noteren als open punt in §5.

## 🔴 NIEUW 2026-07-29 (laatst) — na de 1-op-1-omzetting

1. **De laatste omkering bij Guixi** (28.3429/117.1975). Daar ligt een tweede spoor
   6–16 m naast de hoofdlijn over ~5,3 km; met straf 100 springt de router er één keer
   op over. Zelfde klasse als Ningbo was, maar nu mét correcte topologie — dus dit is
   een tie-break-vraag, geen graafvraag.
2. **De 11 overgebleven omkeringen zitten NIET in het spoor** maar in zee-, rivier- en
   truckbenen (MARNET, AIS-tracks, wegcorridors). Eigen ronde, eigen bronnen. De
   grootste: 180° op het grafiet-truckbeen bij −14.9147/40.2954 en vier op het zeebeen
   Southwest Pass → New Orleans. `toets_knikken.py` telt ze.
3. **De bak-commando's van de vier stromen vastleggen.** `hecht_marnet route` is
   been-gestuurd, maar welke vlaggen er per stroom zijn gebruikt leeft alleen in een
   shell-historie. Dezelfde klasse als de generator-drift van `cu-guixi-spoor` (741 m):
   een gegenereerd bestand waarvan het recept niet is vastgelegd loopt stil uit de pas.
   Zet ze als scriptje naast de routebrieven — vóór de volgende herbake.
4. **`hecht_marnet` zelf op het 1-op-1-net laten routeren.** Nu draait alléén het losse
   spoorbeen erop (via `toets_spoorroute.mjs` + `vervang_spoorbeen.py`); de baker
   gebruikt nog zijn eigen graaf. Zolang dat zo is moet elk nieuw spoorbeen handmatig
   door dezelfde twee stappen.
5. **Overweeg de oude machinerie te schrappen** zodra 1-op-1 het volledig overneemt:
   `dedup_parallel`, de heal-passes, `vind_omweg_connectoren` en hun guards bestaan
   alléén om schade te repareren die de oude volgorde aanrichtte. ⚠️ Niet doen vóór de
   baker zelf op 1-op-1 draait — anders staat er niets meer onder.

## 🟠 2026-07-29 (eerder) — na de junctie-fix

1. **De twee scorefouten in `toets_ankers.py`.** De zelftoets is eerlijk gezakt en de
   diagnose staat er al bij:
   - de **spoor/weg-snap wordt gescoord alsof die netten overal dekkend zijn** —
     Collahuasi 49 km en Balama 178 km naar spoor zijn meetresultaten (daar ís geen
     spoor), geen fouten. Dezelfde nuance die voor de zee-snap al gold, doortrekken.
   - **"geen OSM-object binnen de straal" telt als verdenking**, wat een dunne kaart
     straft (Mozambique, de batture bij Vidalia) in plaats van het anker.
   ⚠️ Wat *niet* repareerbaar is: Waalhaven en Coloso waren **semantisch** fout, niet
   geometrisch (OSM vindt daar water op 3 m en een haven-object op 0 m). Voor die klasse
   is de productvraag het enige gereedschap — niet nóg een meetkundige toets.
2. **`toets_ankers.py --bron js` over alle 510 `data/*.js`-knopen** — dat is de
   eigenlijke oogst; alle 510 vallen in een extract dat al op schijf staat (108 passes).
3. **De junctie-telling als vaste regressietoets** naast de km-ijking zetten. Zie de
   waarschuwing hieronder: lengte meet niet of het net nog een *net* is.
4. **Overweeg `landnet.bin` lazy te laden** zoals `aistracks` — hij is 9,9 MB (laden
   342 ms). ⚠️ Níet de simplify-tolerantie terugdraaien; dan is de bocht weer een
   veelhoek en verdwijnen de flauwe Z'en opnieuw.

> [!warning] De km-ijking is blind voor junctieverlies
> Nederland (−3,7% tegen ProRail) en Polen (+1,2% tegen PKP-PLK) zijn precies de twee
> regio's waarop onze meetlat klopt — terwijl daar 86-88% van de topologie weg was.
> Kilometers meten niet of het net nog een NET is. De junctie-telling draait in 35 s
> (OSM-refs met graad ≥3 uit de scan-cache tegen de gebakken geojson) en hoort vanaf nu
> naast de lengte-ijking in elke landnet-run.

## 🔴 NIEUW 2026-07-29 (eerder) — na de routebrief-omzetting naar mijn→eindproduct

1. **z16-satellietpasses voor de nieuwe fase D/E-ankers** — per brief gelijst in §5.
   O.a.: 铜冠铜箔-foliefabriek (Tongling 经开区) · JCC-walsdraadfabriek (Guixi-complex) ·
   Deutsche Giessdraht Emmerich (OSM-terrein 51.82811, 6.26387) · Panasonic De Soto
   (38.93815, -95.00240) · Lucid AMP-1 Casa Grande (32.85685, -111.77844) · de
   tk-terreinankers (Werkshafen/Kokerei/hoogovens/OSW 1). Statussen zijn nu eerlijk
   bevestigd/aannemelijk — pas na de pass worden het ankers.
2. **Route-toets voor de D/E-benen op de bol** zodra die stromen gebakken worden —
   checklist §8 dekt A–E, maar dekking/verklikker zijn voor de nieuwe benen nog niet
   gedraaid (de stromen op de bol eindigen nu nog bij de smelter).
3. **Kolen vóór de Cerrejón→Ruhr-stroom:** de vier kolen-ankers satelliet-leggen (de
   brief noteert eerlijk nul satelliet-gelegd) én de **cokesblend-bron** uitzoeken —
   de gedocumenteerde Cerrejón→DE-stroom is krachtwerkkool (zie `bugs-and-risks.md`).
4. **Lobito fase D:** de Deutsche Giessdraht-koppeling documenteren, of de
   twee-varianten-vorm (Ruhrort-entrepot vs rechtstreeks Emmerich) bewust laten staan
   — de brief tekent hem nu terecht niet.

## ✅ AFGEROND 2026-07-29 — sjabloon + werkwijze A–E + vijf brieven omgezet

Werkwijze §1a/§1b/§2a/§2b + `_template.md` (commit `a54f0c9`); 12-agent-workflow zette
alle vijf brieven om mét fase D/E-research (commit `2ba6d55`). Details:
`session-summaries.md` en de vault-samenvatting
[[2026-07-29-grondstoffen-atlas-routebrieven-mijn-tot-eindproduct]].

## ✅ AFGEROND 2026-07-28 (laatst) — de zeven correcties + de herbake + de opruiming

1. **Coördinaten gewisseld** — de zes koper-ankers in `v2/tools/maak_aansluitingen.py`
   (de redactionele lijst = bron van waarheid) en daaruit `v2/data/aansluitingen.json`
   opnieuw gegenereerd mét verse snap-metingen; `gr-port-neworleans` in
   `data/graphite.js`. Onderweg een **drift** gevonden en hersteld: `cu-guixi-spoor`
   stond in de uitvoer al goed maar in de generator nog 741 m ernaast.
2. **Grafietketen herbakken** (`?v=098`) — zeeschip SWP → New Orleans 193,2 → **191,1
   km**, barge-start verhuist mee, keten 18.072,3 → **18.070,3 km**. De overslagmarker
   ligt nu 56 m van het geroutete overslagpunt in plaats van ~490 m.
3. **De kijklaag opgeruimd** — `ankercheck.json` terug tot de **drie open ligplaatsen**,
   HUD-sectie heet "Open ligplaatsen (3)". Het proefwerk van de beoordelingsronde staat
   bevroren in `v2/design/ankercheck-2026-07-28.json`.
4. **`toets_ankers.py` gebouwd** (zie hieronder) + de drie routebrieven bijgewerkt met
   wat er is doorgevoerd en wat open blijft.

## ✅ AFGEROND 2026-07-28 (laatst) — VIER STROMEN OP DE EXACTE KADES (`?v=099`)

De hele reden voor de anker-check: stromen die vertrekken en aankomen op een
satelliet-gelegde kade. Ze staan er, elk met een eigen bestand, eigen groep en
eigen knop (`STROMEN` in `main.js`).

| stroom | keten | totaal |
|---|---|---|
| grafiet Balama → Vidalia | truck 504 → zee 17.162 → barge 404 → last mile | 18.070 km |
| koper Escondida → Guixi | leiding 154 (stippel) → zee 19.104 → **trein 551** | 19.809 km |
| koper Collahuasi → Tongling | leiding **193 (echte OSM-geometrie)** → zee 18.590 → Yangtze 517 | 19.299 km |
| koper Lobito → Duisburg | zee 9.705 → Rijn 216 (echte AIS-tracks, Wesel gestippeld) | 9.920 km |

**Twee nieuwe stukken gereedschap** die dit mogelijk maakten:
* **`maak_rivierbeen.py`** — een rivierbeen als TEKENGEOMETRIE uit de
  MARNET-bulklaag (Yangtze Shanghai → Tongling, 516,6 km over 72 edges). De
  Yangtze heeft geen AIS-dekking (Tongling 0 berichten), dus tracks kunnen dit
  been niet leveren. ⚠️ Het pad wordt éénmalig gezocht en als GeoJSON
  weggeschreven; de routeergraaf van `hecht_marnet route` blijft per constructie
  ongewijzigd, dus geen enkele zeeroute kan stiekem een rivier-sluipweg nemen
  (de Donau-ring-fout).
* de slurryleiding Collahuasi → Patache uit `pijpleidingen.json` als
  `--been-geojson` — 192,4 km echte OSM-geometrie in plaats van een rechte lijn.

**Kleur = modaliteit, en spoor + leiding kregen een eigen kleur** (`spoor`
deelde amber met truck zolang geen stroom een spoorbeen had; nu wel).
Gestippeld betekent nu twee dingen die allebei eerlijk zijn: schematische
verbinding (haven-aanloop, last mile) **of een gedocumenteerd gat** — het
Wesel-vak, 0 van 35.237 tracks, structureel gemeten.

**Volgende stromen:** kolen Cerrejón → Ruhr (brief bestaat al) — maar **eerst de
vier kolen-ankers satelliet-leggen**, die zijn nooit gecheckt.

## 🔵 HET LANDNET IS OP 10 m SIMPLIFY HERBAKT — wat je daarvan moet weten

Lars, kijkend op straatniveau: *"een ronde bocht is echt hoekig van dichtbij, dat is
overal op de wereld zo."* Terecht, en het is de **simplify-tolerantie**, niet de bron.

`KETEN_SIMPLIFY_KM` in `fetch_landnet.py` stond op **0,10 km**. Die tolerantie ÍS de
maximale afwijking van de echte lijn, dus op een boog van straal R krijg je koorden van
`sqrt(8·R·t)`: bij R = 500 m en t = 100 m is dat **630 m** — één rechte streep door de
hele bocht. Gemeten op China: mediaan segment **1.095 m**, 0,70 punten/km.

Op **0,010 km** (10 m): mediaan segment **305 m**, 1,68 punten/km, en de netlengte gaat
186.876 → 187.560 km (+0,37%) omdat de bochten hun echte lengte terugkrijgen.

⚠️ **Dit kost GEEN nieuwe pass over de 74 GB extracts.** De ruwe osmium-scan zit in
`build-cache/land/` (1,8 GB, 550 bestanden) en de simplify-tolerantie zit bewust niet in
die vingerafdruk — alleen vouwen, dedup, heal en simplify draaien opnieuw. De hele wereld
is daarmee ~25 minuten in plaats van uren. Nieuwe vlag: `--simplify-km`.

⚠️ **De prijs is bestandsgrootte** (~2,4× de punten). Als `landnet.bin` daarmee te zwaar
wordt voor de telefoon is de volgende stap hem LAZY te laden zoals `aistracks` — níet de
tolerantie weer omhoog, want dan is de bocht weer een veelhoek.

## 🟠 `toets_ankers.py` — de verdachtenlijst STAAT; wat er nog mee moet gebeuren

Vier toetsen per ankerpunt (Lars' eigen lijst): **T1** afstand tot de waterrand + water
of land · **T2** afstand tot pier/kade/haven-object · **T3** wat er ónder het punt ligt
(een kade ligt nooit in een woonwijk, een laadplek hoort in het industrie-/mijnvlak) ·
**T4** snap naar het eigen net. Score = rangorde, mét de reden per punt.

⚠️ **Twee ontwerpkeuzes die je moet kennen voor je eraan draait:**
* **De zee-snap wordt gemeten maar NIET gescoord.** MARNET is grof en houdt op bij de
  kust (Patache 78 km, Coloso 85 km); daar is ver een meetresultaat, geen fout. Binnen,
  spoor en weg zijn wél dekkend en tellen dus wél mee.
* **De bron is de LOKALE Geofabrik-extract, niet Overpass** — omgekeerd aan
  `verken_terminals.py`, en met reden: de kosten stijgen met het aantal LANDEN in plaats
  van het aantal punten, en de publieke Overpass-mirrors gaven op de bouwdag 504's en
  daarna 429. Wat de extract-pass mist zijn multipolygoon-relaties (`--osm overpass` als
  controle op één punt). De regiokeuze gaat via de echte Geofabrik-regiopolygonen, niet
  via de bestands-bbox — op de bbox koos hij voor Puerto Coloso het Argentijnse extract.

**Volgende stappen:** `--bron js` over alle `data/*.js`-knopen draaien (dat is de eigenlijke
oogst: honderden punten) · de kop van die lijst satelliet-leggen · drempels bijstellen als
de zelftoets erom vraagt.

## 🟡 DE DRIE OPEN LIGPLAATSEN — productvraag beantwoord, kade nog niet

De productvraag heeft voor alle drie de **operator en de terminal** opgeleverd (details in
`memory/bugs-and-risks.md` en in de routebrieven):
- **Port Allen** — SEACOR AMH op de Inland Rivers Marine Terminal van de Port of Greater
  Baton Rouge: bargekanaal langs de GIWW, 200 ft bargekade, 9 acre containeryard.
- **Lobito** — de mineralenterminal van Porto do Lobito onder de LAR-concessie
  (Trafigura/Mota-Engil/Vecturis); kathode gaat er **gecontaineriseerd** weg (MSC SAMU,
  22-08-2024). Geen bron noemt een kade; Angola heeft nul havens met varend AIS-verkeer.
- **Vidalia** — mijl 359, 12 ft; bestaande fase = cargo ramp (aggregaat) + t-dock met
  transportband (droge bulk). ⚠️ Dat lost geen containers, terwijl deze stroom
  containervormig is — een vraag aan de brief, niet aan de satelliet.

**→ Volgende stap voor Port Allen en Vidalia is het DOK-BEWIJS uit de AIS-trackuiteinden,
niet opnieuw inzoomen.** Beide liggen binnen de bbox van de track-graaf, en die toets
vond bij de Syrah-kade al 55 eindigende tracks. Lobito blijft vermoedelijk open.

Ook nog: **de productvraag promoveren** van de Lobito-brief naar `routebrief-werkwijze.md`
zelf — hij hoort bij elke kade, niet bij één stroom.

## ✅ AFGEROND 2026-07-28 — ROUTEBRIEF GRAFIET + KETEN MIJN→FABRIEK (`?v=092`→`?v=094`, GO LARS)

Brief: `v2/design/routebrieven/grafiet-balama-vidalia.md` (~60 punten, DOE/EA-2181).
Kaart brief-gestuurd: zeeschip via Southwest Pass · barge belading Port Allen · los
Port of Vidalia mijl 359 · gestippelde last mile · **spoorbeen geschrapt (bestaat
niet — uitgaand is truck)**. graphite.js: 4 centroïdes → kades/fabriek (het
New Orleans-kade-punt hieronder is daarmee afgewerkt), rail→road, volumes EA-regime.

**✅ Zelfde dag afgewerkt (`?v=093`):** het Mozambique-truckbeen ligt er met échte
N380/N1-geometrie (`maak_stroombeen_weg.py`, +2,0% t.o.v. de brief) en het
MARNET-startgat is een gestippelde haven-aanloop — **de keten begint bij de mijn.**

**Nieuwe open punten uit de brief:**
- **Uitgaand been tekenen?** Pas als er een gedocumenteerde bestemming is
  (Tesla-locatie onbekend; Lucid→Panasonic De Soto KS is het meest aannemelijk).
- **Ankerstukjes plant/kade** (3,8 + 2,6 km recht): geen OSM-weg binnen 0,2 km
  van de ankers — evt. later verfijnen met satelliet-gelegde punten.
- **Golf-toegang** (Yucatán vs Straat Florida) blijft onzeker in de brief.
- Volgende stromen: per stroom eerst een brief (werkwijze bevestigd), dan de
  MARKER_NAAM/OVERSLAG_NAAM-tabel in `hecht_marnet.py` aanvullen.

## ✅ AFGEROND 2026-07-27 (avond) — DE EERSTE ECHTE STROOMTESTS

Vier tests, alle geslaagd (zie `session-summaries.md`): Nacala→Vidalia 17.371,5 km
(16.936 MARNET + 1 connector + 435 km tracks, Kaap-route) · Newcastle AU→Vidalia
17.488 km (Panama) · New Orleans→Baton Rouge vóór==ná byte-identiek · spoor
Vidalia→battery belt 1.036 km + Long Beach→Fort Worth 2.312 km (nieuw tool
`toets_spoorroute.mjs`). **De grafietketen Balama→battery belt is meetbaar over drie
netten.** Marnet-extractie staat klaar in `build-cache/marnet-preais/`.

## 🔴 START HIER — de losse eindjes

**M28 fase 1-3 is af en staat live op `?v=090`** (gepusht `c0c2b73..ed24837`). De
track-graaf staat (`bouw_trackgraaf.py`), MARNET hecht erop (`hecht_marnet.py`), en de
bol draagt vijf bronnen. Wat nu openstaat:

0. ~~**De stroom zichtbaar maken op de bol**~~ — **GEDAAN (2026-07-27, avond, `?v=091`,
   commit `e1811de`):** HUD-laag "Stroom: grafiet Balama → VS (preview)", standaard aan —
   `hecht_marnet.py route` bakt de benen + overslagmarkers naar
   `v2/data/stroomroute-pilot.json`, `stroomroute.js` tekent kleur-per-modaliteit.
   ⚠️ Twee CDP-lessen in de file-kop: renderOrder 7,5 bóven het landnet (het spoorbeen
   volgt exact een landnet-lijn) en toneMapped uit (ACES bleekte de legenda-kleuren).
   Vervolgkandidaten: meer stromen bakken (de MARKER_NAAM/OVERSLAG_NAAM-tabel in
   hecht_marnet.py per stroom aanvullen) · wacht op Lars' visuele check.
   Klein bijpunt uit de tests: `regressie` rapporteert een VOOR-pad ook na een snap van
   26.881 km — de snap-afstand ontmaskert het, maar een snap-maximum zou eerlijker zijn.

1. ~~**Visuele check van Lars op `?v=090`**~~ — **GEDAAN, go binnen** (2026-07-27):
   *"ziet er goed uit zo, we hebben veel kustgebieden, goeie haven-aansluitingen nu."*
   Geen fixes uit voortgekomen. De twee bekende schoonheidspunten blijven staan en zijn
   geen bug: in de Deense straten en de Mississippi-delta verzadigt de bundel naar
   crème-wit (prijs van 0,55 opacity bij die dichtheid), en Australië oogt grover door
   AMSA's eigen korrel van 21 km per stap.
2. **De New Orleans-coördinaat is een stadscentroïde, geen kade** — daardoor faalt de
   snap-eis (0,726 tegen ≤0,5 km) terwijl geen enkele van 510.752 tracks daar binnen
   0,5 km komt. De echte loskade van het Balama-vlok opzoeken en `gr-port-neworleans` in
   `data/graphite.js` vervangen. Zelfde klasse als de eerdere `data/*.js`-datafouten.
3. **Terminal-nodes (LAR-531)** uit de track-eindpunten — het dok-bewijs ligt er al:
   119 tracks eindigen en 133 beginnen binnen 3 km van de Syrah-kade, en elke
   track-uiteinde-cel is al een knoop in de graaf.
4. **GFW uitwerken voor de nul-dekking-corridors** (Chili/koperbeen, Hormuz, Lobito,
   Suez, Constanța). Token staat in `~/.claude/grondstoffen-atlas.env` en is getoetst
   (rooktest 200; presence-rapport Patache–Antofagasta 3.577 rijen / 27.741
   aanwezigheidsuren). ⚠️ Korrel is 1 positie/uur → corridorlaag, geen geul; en gebruik
   `datasets%5B0%5D=` in de URL, want bash leest `[0]` als glob.
5. **De EuRIS-vaarweglaag verwerken** — 7.122 secties met CEMT **én max diepgang** van de
   beheerder zelf, al anoniem binnengehaald in `build-cache/ais/euris/`. Dat is de echte
   diepgang-meting die LAR-514 eiste. De Donau valt in 8 componenten uiteen met gaten van
   3 m tot 2 km = de bekende LAR-520-klasse; de bestaande twee-traps heal volstaat.
6. **Overweeg een VPS-endpoint voor de tracks-laag** — `aistracks-pilot.json` ging van
   21,4 naar 39,5 MB en groeit met elke bron. Voor de pings-laag is die keuze al gemaakt
   (*"geen databestanden in de git-history"*); hier komt hetzelfde punt in zicht.
7. **De graaf op de andere corridors draaien** — nu bewezen op Mississippi en Rijn.
   Let op: connectors zijn corridor-gebonden, dus elke nieuwe corridor vraagt een eigen
   `hecht`-run. Globale bovengrens al gemeten: 1.211 van 9.633 MARNET-zeeknopen hebben
   over alle bronnen een trackpunt binnen 0,5 km.
8. **Collector blijft aandikken** — wekelijks `haal_ais_data.py` + `bouw_tracks.py --bron`.
   VPS-schijf: 21 GB vrij, ~844 MB/dag = ~24 dagen marge.

## Ouder (deels vervallen) — het oorspronkelijke LAR-530-plan

**Het plan staat in Linear** (milestone *"M28 · AIS-tracknet"*, LAR-528 t/m LAR-535) —
niet in de oude gloed/density-notities hieronder. De collector draait al op **13 vensters**
en verzamelt; er is dus dagelijks meer materiaal, en wachten kost niets.

**Eerst even dit, kost vijf minuten:**

* **Schijfritme is nu routine, geen luxe.** De collector staat op een wereldabonnement met
  live gzip: ~1 GB/dag gegzipt tegen ~22 GB vrij = **~20 dagen marge**. Loop
  `df -h /` + `ls -la /var/lib/ais-collector/ais/` na en draai
  `python v2/tools/haal_ais_data.py --opruimen` als er afgesloten dagen liggen.
  ⚠️ De harde ondergrens (2 GB) stopt alleen het schrijven, niet de stream — dat valt pas op
  in `journalctl`.
* **~~Wesel hermeten~~ — GEDAAN (2026-07-26):** op 12,5 uur is lon 6,5 nog steeds **0** en
  6,6 slechts 5 berichten in één uurvak, tegen 509 op 6,3 en 14.118 op 6,7. **Structureel**,
  zie `bugs-and-risks.md`. De pilot-corridor krijgt dus een gedocumenteerd gat.
* **Optioneel: tweede wereldscan op een ander tijdstip.** `python v2/tools/ais_wereldscan.py
  --minuten 60` (op de VPS) + `analyseer_wereldscan.py`. Scheidt de twijfelgevallen: "0 in dit
  uur" bewijst geen afwezigheid van dekking, terwijl wat binnenkwam wél hard bewijs van
  aanwezigheid is. Vooral zinnig voor havens met weinig bewegingen per dag.
* **Aanbod dat openstaat** (Lars nog niet op geantwoord): een dekkingsrapport per
  corridor-segment dat toont wélk aandeel van de uren dekking had — dan zie je in één blik
  welke gaten dichtlopen en welke echt leeg blijven. Volgt uit Lars' Starlink-punt: dekking
  is statistisch, niet binair. **Nu goedkoper dan eerst**, want het wereldabonnement levert
  elke corridor al aan.

* **LAR-530 · track-naar-graaf**, de kern. Stappen uit het issue:
  1. tracks per MMSI (sorteren op tijd, splitsen bij tijdsprong > X min of onrealistische
     sprongafstand — vangt meteen stream-uitval van de collector af);
  2. varend/stilliggend knippen (SOG < ~0,5 kn → apart, dat is LAR-531-materiaal);
  3. opschonen per track (max plausibele snelheid tussen punten, Douglas-Peucker + lichte
     smoothing);
  4. **track-bundeling** — meerdere doorvaarten middelen tot één centerline per vaarbaan.
     ⚠️ Bundel-afstand **kleiner dan de eiland-schaal**, anders smelten twee geulen om een
     eiland samen tot één lijn (de Tongling-les, ook al is Tongling zelf nu ongedekt);
     **⚠️ VERVALLEN MÉT stap 4 — sleep deze waarschuwing NIET mee naar de track-graaf.**
     Hij ging over *middelen tot één middellijn* over de héle lengte. In de track-graaf is de
     eis het omgekeerde: twee geulen om een eiland zijn twee eigen edges die **boven en onder
     het eiland juist wél in één gedeelde knoop samenkomen** — precies de vorm die Lars bij
     Tongling goedkeurde (zuid-junctie → kade → noord-junctie op exacte vertices). Zonder die
     samenkomst heb je twee losse parallelle netwerken en kan er niets langs routeren.
     (Correctie Lars, 2026-07-27, nadat deze zin ten onrechte als ontwerpeis was doorgegeven.)
  5. naar graafformaat: nodes op splitsingen/samenkomsten, edges met lengte.
* **Pilot = Rotterdam-Rijnmonding** (Tongling valt af wegens dekking). Eerst één corridor
  end-to-end vóór het generiek maken.
* **Integriteits-metrics per run loggen**, geen screenshot-vergelijking als primaire check:
  aantal losse componenten · edges/nodes · bereikbaarheid van havens/terminal-nodes vanuit
  de hoofdcomponent · verdeling snap-afstanden.
* **LAR-531 · terminal-nodes** uit de ligplaats-clusters (DBSCAN ε ~50–100 m), verrijkt met
  scheepstype uit `ShipStaticData` — dat komt al binnen, dus dit kan zodra stap 2 draait.
  Let op het onderscheid ankerplaats vs kade (afstand tot land / laad-context).
* **Collector-hygiëne:** af en toe `journalctl -u ais-collector | grep health` — blijft een
  venster op 0/min staan terwijl de verbinding er is, dan is dat dekking, geen storing.
  Schijf: dagbestanden gzippen automatisch, ondergrens 2 GB (VPS had 22,8 GB vrij).
* **Kandidaat-vensters zodra het recept staat:** de VS-binnenwateren (Mississippi/Ohio/
  Illinois/Seaway — Memphis, Cincinnati, Baton Rouge uit de routebrieven) zijn volgens de
  stationskaart gedekt, en dat zijn precies de corridors met de meeste OSM-topologiegaten.
* **Open, meeliften bij gelegenheid:** de reboot-overleving van `ais-collector.service` is
  mechanisch geborgd (`enabled` + `Restart=always`) maar niet live bevestigd — bevestigen
  bij de eerstvolgende geplande VPS-reboot (Hermes/Traefik/form4app draaien mee).
* *Herinnering:* de water-toetsen (`toets_routes.mjs`, `toets_stromen_14.mjs`) heffen hun
  parkering zelf op zodra er weer een waternet-bake ligt — verwachtingen dan herijken op het
  AIS-net (de oude 30/30-stand leeft op tag `pre-ais-net`).

## ⏸️ INGEHAALD DOOR M28 — de graaf-stap op de rug-lijnen

De onderstaande M27-acties (gloed-check, graaf-stap op de rug-lijnen, convergentie-filter)
zijn **geen route meer**. De gloed blijft als visuele laag, `bake_aisnet.py` als fallback
voor ongedekte corridors. Bewaard als context, niet als werklijst.

## ✅ AFGEROND 2026-07-25 (laat) — RUG-RECEPT VERVANGT DREMPEL+VERDUNNEN (live `?v=085`, commit `9576dea`)

Lars keurde v084 af (hoekig, gaten in oostgeul + Rijn, te dun) → tweede recept i.p.v.
fix. `bake_aisnet.py` herschreven: Steger-rug-NMS op het continue log-veld (2 schalen,
σ²-genormaliseerd) + hysteresis (zwak-maar-aaneengesloten loopt door → gaten dicht) +
geijkte bezettingstoets (oostgeul ≥0,53 vs drijfzone ≤0,40 + groot-component) +
kruimel-snoei + gladstrijken. 2.369 lijnen / 245 KB (was 9.631 / 770). Beide
Tongling-geulen doorlopend · NL glad tot de grens · Patache één corridor. Gemeten en
verworpen in de file-header: NMS-tolerantie, vlak-bezetting, max-filter-bezetting.
Het aparte "open-zee-recept" is hiermee opgegaan in de grove σ 3,5-schaal.

## ✅ AFGEROND 2026-07-25 — AIS-PILOT OP DE BOL (live `?v=084`, commit `9ddd96f`)

`verken_ais.py` (kijk-eerst: density-PNG's bewezen de bron) + `bake_aisnet.py` (drempel
100k → adaptief verdunnen → glad log-veld → confetti-filter → skelet + spur-snoei) +
`aisnet.js` (één LineSegments, HUD-knop). Tongling's beide geulen komen rechtstreeks uit
de data; binnenvaart-NL compleet. Les: heel NL-water is één verbonden component —
per-component herdrempelen sloopte de rivieren; brede vlakken lokaal uitsnijden.

## ✅ AFGEROND 2026-07-24 — SCHONE BOL: WATERNET ERUIT (live `?v=083`, commit `960ad15`)

Besluit Lars: alles nat weg (zee + binnenvaart), clean slate voor de AIS-graaf. Backup tag
`pre-ais-net` + branch `backup/pre-ais-net` (`?v=082`, 30/30). Bol = tegels + vectorwereld +
landnet + havens-als-ankers; marnet.bin/json verwijderd; HUD-secties Zeeroutes/route-test/
stromen weg; water-toetsen geparkeerd (zelfopheffende guard), land-toets draait door.
AIS-bron gedownload (Commercial 458 MB, gratis/CC-BY) + rasterio/scikit-image geïnstalleerd.
* **Optioneel: de 22 grove AFGEKNIPT-sites breder uitrollen.** De last-mile-pass draait nu op de
  15 aangewezen aansluitingen; de brede detector (`toets_spoor_aansluiting.mjs`) vond nog **22
  AFGEKNIPT** industriële nodes (Fresnillo, Kalgoorlie, Norilsk, Hunan-Ag…) — dat zijn de grove
  `data/*.js`-coördinaten, niet de aansluitingen. Uitrollen = per site een precieze coördinaat
  opzoeken (veel zijn stad-centroïdes) en `PUNT_EXTRACT` in `fetch_service_lastmile.py` uitbreiden;
  de heal + drop + wees-opruiming werken dan generiek mee.

## ✅ AFGEROND 2026-07-24 — ROUTEBRIEF-WERKWIJZE + EERSTE BRIEF (commit `a595095`, gepusht)

Besluit Lars: per stroom een **routebrief** die de échte corridor vastlegt — elk dorp/
splitsing/sluis in volgorde, per punt bron + status (bevestigd/aannemelijk/onzeker),
negatieve ankers, tweezijdige toets (dekking + verklikker), routeren via-punt→via-punt,
**simulator alleen op zee**. Spec: `v2/design/routebrief-werkwijze.md`. Eerste brief kolen
Cerrejón→Ruhr: spoorbeen 37 punten (laadlus→Muelle Carbonífero) + Rijnbeen 93 punten mét
operator-bron (thyssenkrupp Veerhaven: Hartelkanaal→Oude Maas→Merwede→Waal→Rijn, 240 km,
sluisvrij) — de toets ving meteen de **Beerkanaal-fout** en bevestigde de Oude Maas-keuze.
AIS-richting: corridor-first met World Bank-density als geul-bewijs (idee Lars, geverifieerd).

## ✅ AFGEROND 2026-07-24 — TONGLING: BEIDE GEULEN ALS GRAAF (live `?v=077`, Lars' go, commits `6327707`→`5428001`)

De oostgeul (waar de schepen echt varen) als échte graaf-tak **naast de hoofdgeul**: 18
punten, zuid-junctie → kade → noord-junctie, beide uiteinden op exacte vertices van
hoofdgeul-way 226556520 → gedeelde knopen. **Werkwijze-doorbraak:** OSM's watervlak bleek
geen waarheid (elke afleiding gaf de 27 km-lus) → Esri-tegels lokaal gestitcht (z14,
0,01°-grid) en elk punt visueel in het geul-midden gelegd — voortaan de standaard voor
handmatige vaarweglijnen. Onderweg het `knipWayId`-mechanisme gebouwd
(`bake_marnet.bulklaag`, extra-vaarwegen-feature = knip-instructie, guard ≤1 km); de
v076-knip van de west-arm was een **misinterpretatie** en is in v077 teruggedraaid — het
mechanisme blijft voor echt foute armen. Kleur = grondstof: bevestigd besloten. Toets
30/30 elke ronde; zee-invarianten exact. Lars: *"top helemaal goed — zo lang beide geulen
een simpele graaf, dat was alles."*
* **Realiteitsronde** (Lars' eigen volgorde: "eerst de rail beter verbinden, dan de realiteit"):
  per dragende site checken of het product écht per trein/truck vertrekt (bedrijfsrapporten) —
  nu is er een stuk minder te vullen omdat de last-mile-sidings al hechten.
* **Echte OSM-gaten** (blijven `onbekend`): EU-spoor rond Krefeld/Kempen (daar ligt écht niets)
  en de Escondida-slurryleiding (geen `substance=slurry` richting Coloso).

## ✅ AFGEROND 2026-07-24 — INDUSTRIEEL LAST-MILE-SPOOR GEHEELD (live `?v=072`, commit `6266aba`)

Vervolg op de heal-ronde: is er meer spoor/riviergraaf dat we missen? Twee detectoren
(`toets_stromen_14.mjs` → riviernet solide, 0 gaten; `toets_spoor_aansluiting.mjs` → 22 AFGEKNIPT).
Wortel: het M25-filter dropt álle `service=`-rail — juist het last-mile-spoor. Fix:
`fetch_service_lastmile.py` (service=spur/siding/yard binnen 7 km van de aansluitingen) +
transitieve vertex-op-vertex heal in `bake_landnet` (smelter→tussennet→hoofdnet ≤200 m) +
`drop_onverbonden` (weg + wees-knoop-opruiming, anti-regressie). Tongling/Beilun/Guixi/Duisburg
aan het hoofdnet; toets_routes 30/30; marnet/ports byte-identiek; Lars' visuele go.

## ✅ AFGEROND 2026-07-24 — DE HEAL-RONDE (de spoor+riviernet-heal van hieronder)

Live `?v=071` (commit `0eaff4b`). De diagnose draaide de opdracht om: niet het net healen,
maar de pijplijn laten ophouden met knippen — de bron was op elk breukpunt al verbonden
(raw-experiment, ook onder het service-filter).

- **Heal verlengt i.p.v. verplaatst** → EMO-flip-flop weg; Cerrejón→Ruhr **0 gaten**.
- **Riviersnap relatief naar doorgaand component** → Manaus→Amazone; Saldanha→Manaus routeert.
- **Dedup-connectiviteitsguard** → spoor 3.140 → **638 componenten**, grootste 402.845 →
  **664.313 km**; Beilun↔Guixi trein 883 km; Antwerpen↔Duisburg één component (EU 96%).
- toets_routes 30/30; zee-invarianten exact. Gemeten en verworpen: snipper verlagen alléén.

## ✅ AFGEROND 2026-07-23 (avond) — GROENE STROOM (COLLAHUASI→TONGLING) VERFIJND

Live `?v=066` → `070` (commits `8d2842e` · `7afc0e1` · `5e6fcd5` · `d14c602` · `a0b5959`).

- **Yangtze-heal in de bake:** `snij_bulk()` neemt nu alleen kop/staart weg, nooit een gat in
  het midden → de rivier blijft in de graaf één stuk. Been 616 → 540 km; 59 lijnen / ~282 km
  wereldwijd heel gehouden.
- **Overslag-markers:** `transparent:true` op het merk (zat in de opaque pass, tegels
  schilderden eroverheen) + maat gehalveerd.
- **Tongling-kade** naar de nieuwe TNMG-kopersmelter (`117,7718/30,98656`); oostgeul afgeleid
  met `middellijn_uit_vlakken.py` op 167 m, water-constrained, **alleen noordaanvaart** (met
  óók de zuidkant maakte de router een lus om het eiland).
- **Nieuw:** bake-optie `--extra-vaarwegen` + gecommit `data/vaarwegen-handmatig.geojson`
  (reproduceerbaar via `tools/maak_tongling_oostgeul.py`); `BAKE_SUFFIX` in `laad_headless.mjs`.

## ⚪ AANSLUITINGEN VERFIJNEN (Lars: "we laten het hierbij, verfijnen kan later")

* **Puerto Patache — de espesadores.** Collahuasi's eigen video geeft de keten ná de leiding:
  espesadores → planta de molibdeno → planta de filtro → stockpile → embarque. De leiding
  mondt uit bij de **indikkers**, niet bij de pier. Nu doet `cu-patache-kade` twee dingen
  tegelijk (eind van de leiding én begin van het zeebeen) terwijl dat twee plekken zijn met
  vier verwerkingsstappen ertussen. Eerlijke opzet: leiding → espesadores · terminalverwerking
  als *eigen verbinding* · zeebeen vanaf de pier. **Blokkade:** de espesadores staan niet in
  OSM (binnen 1,8 km kent de kaart vijf objecten, geen tank) → één coördinaat van Lars nodig.
* **Shanghai/Luojing** — nu de Baogang-bulkpier; concentraat voor de Yangtze-smelters lost in
  werkelijkheid vaak verder stroomopwaarts (Zhangjiagang/Jiangyin) of aan de eigen kade van
  de smelter.
* **Tongling** — de pier ligt 1,5 km van het smelterterrein; de smelter zelf heeft geen
  kade-tag in OSM.
* **Rotterdam/Duisburg** — OSM tagt bij géén van de gekozen kades wát er wordt overgeslagen;
  de toewijzing leunt op de buren binnen 1 km (ArcelorMittal Staalhandel / Metaalhandel
  Ketting bij de Waalhaven; Kokerei + Erzlager bij Schwelgern). Staat per aansluiting in de
  `noot`.

## ⚪ OPENSTAAND ONTWERPBESLUIT

* **Blijft "kleur = grondstof"?** De LOD-ontwerpbrief zegt van wel, maar de koperkleur
  (#E0965A) is op de Atacama en de Chinese kust onleesbaar — zandkleur op zandkleur. De pilot
  draait nu op vier contrastkleuren (Lars' eigen schets). Of de regel grondstof-gebonden
  blijft of per stroom mag verschillen hoort bij de rest van M26. Staat als `kleurnoot` in
  `v2/data/stromen-pilot.json`.
* **Pijpleidingen ooit tóch een net?** Voor slurry: nee (Lars' criterium — één product, twee
  punten, nooit een keuze). Voor **olie en gas ligt het anders**: Droezjba of Power of Siberia
  ís gedeelde infrastructuur waar een blokkade een echte herrouteringsvraag oplevert, en
  `data/*.js` heeft 36 pijpleidingstromen. Dán een eigen milestone, niet nu.

## ✅ AFGEROND 2026-07-23 — M26.1 · DE STROMEN OP STRAATNIVEAU

Live `?v=065` (commits `d5b2204` · `d8e86fd` · `0f4ba0b` · `5bc5997` · `4d1581e` · `17b5ac2` ·
`34f7a3a`). Vier werkelijke stromen, twee grondstoffen, been voor been over de gekoppelde netten.

- **`v2/data/aansluitingen.json`** — 15 aansluitingen per grondstof, coördinaten uit OSM (ODbL)
  via de nieuwe scout **`v2/tools/verken_terminals.py`**, gemeten door
  **`v2/tools/maak_aansluitingen.py`**.
- **`v2/src/stromen.js`** (three-vrij) + **`v2/src/stroomlaag.js`** (tekenen) — zelfde splitsing
  als `router.js`, zodat het routeren headless narekenbaar blijft.
- **`v2/data/pijpleidingen.json`** + **`v2/tools/fetch_pijpleidingen.py`** — de slurryleiding
  Collahuasi→Patache als tekengeometrie, 1.363 punten, 192,4 km (−3,8%).
- **`v2/design/stroom-aansluiting.md`** — het ontwerp, incl. §4a met Lars' net-criterium.
- `globe.js` kreeg **`vliegNaar(lon, lat, hoogteKm)`**; `keten.js` meet nu ook de componenten
  van land- én waternet zodat "geen pad" op elk net zijn reden draagt.
- **`toets_routes.mjs` 15/15 → 30/30 groen**; zee-invarianten onveranderd (19.610 / 89).

## ⚪ OUDER OPEN GELATEN

* **Drie wegcorridors zonder pad:** `bx-boke-katougouma`, `li-atacama-lanegra`,
  `ree-mountweld-leonora`.
* **89 atlas-plaatsen op een spoorcomponent <1.000 km** (New York op 0 km, Amsterdam op 87).
* **In "egaal" (tegellaag uit) blijft de vectorlaag onzichtbaar** — daar ís de bol het
  oppervlak, dus hij schrijft diepte en wint opnieuw.
* **Manaus→Rotterdam = "geen pad"** — Amazone-fragment raakt Macapá niet.
* **Drie datafouten in `data/*.js`** (zie `bugs-and-risks.md`), plus de nieuwe bevinding dat
  de via-havens daar te grofkorrelig zijn voor straatniveau.
