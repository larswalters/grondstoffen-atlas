# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-24 (routebrief-werkwijze + eerste brief Cerrejón→Ruhr, commit `a595095`)*

## 🔴 START HIER

* **Routebrief-vervolg (werkwijze staat, besluit Lars — zie `v2/design/routebrief-werkwijze.md`):**
  (a) **Beerkanaal-fix**: het Rijnbeen van de kolenstroom via-punt→via-punt langs de brief
  routeren — EMO → Suurhoffbrug → Hartelkanaal (níet het Beerkanaal), eindpunt Schwelgern
  Rijn-km 790,20; brief: `v2/design/routebrieven/kolen-cerrejon-ruhr.md` (§Toets).
  (b) **World Bank "Global Shipping Traffic Density"** downloaden (Data Catalog 0037580,
  GeoTIFF ~500 m, gratis) → eerste zelfgelegde knopen van het corridor-first natte net rond
  de Maasvlakte (pilot). Empirisch toetsen hoe helder Rijn/Yangtze in het raster staan.
  (c) **Routebrieven voor de andere drie pilotstromen** — Beilun→Guixi (China-spoor) is de
  zware (grootste kans op een verkeerde corridor).
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
