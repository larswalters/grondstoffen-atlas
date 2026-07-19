# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-19 (LAR-505 Maas + delta uitgevoerd; NU = LAR-493 Main -> LAR-494 Donau)*

## 👀 EERST: Lars' gevoelscheck op het slepen

Het slepen over de bol is vervangen door **grijpen-en-meenemen** (het punt dat je vastpakt blijft
onder de cursor). De oude wet was gemeten 3,52× te snel op élke zoom. Live op `?v=024`.
**Headless niet te beoordelen** — in de Browser-pane is het venster 1×1 en staat de framelus stil,
dus alleen Lars kan zeggen of het nu goed voelt. Voelt het nog steeds mis, kijk dan eerst naar het
tempo van `zoomBy` (factor 1,08 per wheel-tik) — dat is nooit tegen de meetkunde geijkt.

## ✅ AFGEROND: [LAR-506] Mosel — de eerste echte aftakking (2026-07-19)

Koblenz → Neuves-Maisons 392,0 km (officieel ~394, −0,5%), aansluiting 0,13 km `aftakking:rijn`.
Daarmee is LAR-504 end-to-end bewezen. Nieuwe les: **bevaarbaar ≠ bevaarbaar op commercieel
gabarit** — zie `decisions.md`. Nieuwe extracts `fr-lorraine` + `luxemburg`.

## ✅ AFGEROND (op de visuele go na): [LAR-505] Maas + Benelux-delta (2026-07-19)

Vier systemen: `maas` **278,1 km** (Werkendam → Luik, `aftakking:waal` op 0,00 km) · `maas-boven`
64,2 (Luik → Namen) · `albertkanaal` 127,5 (`aftakking:maas`) · `amsterdam-rijnkanaal` 73,3.
Live t/m `ba8c287` (`?v=025`). **[LAR-504] is nu ook end-to-end bewezen**: Nijmegen→Luik 353 km
loopt dwars *door* een aftakking.

Nieuw mechanisme **`sluitAan`** — een keten hecht aan **beide** kanten. Zie `decisions.md`.

## 👀 OOK OPEN: Lars' visuele go op de Maas

Kijken op https://larswalters.github.io/grondstoffen-atlas/v2/ : de Maas van de Biesbosch tot Luik,
en **Amsterdam→Nijmegen dat nu binnendoor gaat** (263 → 105 km) in plaats van om via zee.
Daarna [LAR-505] op Done.

## ➡️ NU: [LAR-493] Main + Main-Donaukanaal, daarna [LAR-494] Donau

Samen maken die de as **Rotterdam → Zwarte Zee** compleet. De Main takt bij Mainz **30 km ín
`rijn-boven`** aan — dat is precies waar [LAR-504] voor gebouwd is, en het patroon is nu twee keer
gelopen (Mosel, Maas), dus dit zou een vaste-werkwijze-klus moeten zijn.

⚠️ Verwacht bij de Donau de **gecombineerde grensnamen** die de survey al vond: `Dunaj / Duna` en
`Dunărea - Дунав`. Zonder allebei knipt de keten bij elke grens door.
⚠️ Verwacht ook de **CEMT-clause-val** opnieuw (Mosel + Maas allebei) — begin met
`cemt_insluiten=False` tenzij er een reden is om 'm aan te zetten.

## ➡️ DAARNA: [LAR-495] Schelde / Seine / Rhône

Extra reden sinds LAR-505: **Rotterdam→Antwerpen staat nu op 500 km** omdat de route om moet via
Maas + Albertkanaal. Het **Schelde-Rijnkanaal** (22,1 km, al gemeten) brengt dat terug naar ~110 km.
Franse regio's: Geofabrik gebruikt de **pre-2016** indeling (`alsace`, `basse-normandie`,
`rhone-alpes` bestaan; `normandie` niet — die geeft **0 bytes** i.p.v. een 404).

## ✅ AFGEROND: [LAR-492] Rijn + [LAR-504] aftakmechanisme (2026-07-19)

Live t/m `b402fc5` (`?v=022`), visuele go van Lars (*"Rotterdam Kehl ziet er goed uit"*).
`rijn` Nijmegen→Bingen 355,0 km · `rijn-boven` Bingen→Basel 360,6 km, beide binnen 1% van de
officiële Rijnkilometers; twaalf searoute-havens vallen op de lijn. Gesplitst bij Bingen op de
**verstoring** (Kaub-laagwater 2018/2022), niet op de zeevaartgrens — die klopte niet omdat `waal`
stroomafwaarts al binnenvaart is. Nieuw gereedschap `v2/tools/survey_vaarwegen.py`; nieuwe extract
`fr-alsace` (zonder die extract een gat van 72,9 km in de Elzas).

## ✅ AFGEROND: de M24-pilotreeks (2026-07-19)

Alle drie de pilots zijn Done na Lars' visuele go (*"ik heb even gekeken naar die test routes dat
ziet er wel goed uit mooi over de rivier"*). Daarmee zijn de drie controle-situaties bewezen:
twee onafhankelijke bronnen (NL/LAR-486) · officiële meetlat (VS/LAR-487) · géén scheidsrechter
(China/LAR-488). Live t/m `919b046` (`?v=018`).

## 🛤️ DAARNA: M25 · landroutes — bronnenplan staat, wachten op de uitrol ([LAR-491])

Bewuste volgorde van Lars: **eerst M24's uitrol afmaken, dán pas wegen en sporen.** Het bronnenplan is
al vastgelegd zodat een verse sessie meteen kan bouwen; niets ervan hoeft opnieuw onderzocht.

Beslist: **compleet hoofdspoornet** (niet corridor-scope) · spoor = OSM/Geofabrik met NARN als meetlat ·
pijpleiding = OSM + GEM's openbare GitHub-repo · weg bewust klein (geen scheidsrechter).

**Eerste werk zodra M25 begint, in deze volgorde:**
1. **Dedup van parallelle sporen** — móét vóór pilot 1, anders meet de lengtetoets 2,4× te veel waar
   dubbelspoor ligt en jaag je een niet-bestaande bug.
2. **Connected-components-pass** — M24's snoeiregel transfereert: een spoorcomponent die niet aan een
   haven of andere component hangt kan nooit een stroom dragen. Goedkoop, en de kandidaat om de
   1,9–2,4M km-schatting fors te drukken vóór er iets naar de browser gaat.
3. **Pilotkeuze vastleggen** (nog open) — voorstel: VS (NARN = meetlat én tweede bron in één) · EU (RINF
   kent alleen de lengte, niet de vorm) · Mongolië/Gashuunsukhait 233,6 km of Copperbelt→Lobito 1.739 km
   (géén scheidsrechter). Eerste ijkpunt bij voorkeur enkelsporig (Sishen–Saldanha 861 km).
4. **Knoopafstand 5 of 10 km** beslissen op de dedup-meting.
5. **GEM-licentie vastzetten** vóór er iets live gaat (repo heeft geen LICENSE-bestand).

Gereedschap staat al: `v2/tools/meet_spoor.py` (filter + budget per regio), het Geofabrik-fetchpad en
`strak_trekken()` uit M24.

## ➡️ NU: de uitrol uitvoeren — staat klaar in Linear

De go/no-go is beslist (Lars: doen, en *"uitgebreid"*). Bron en gereedschap staan; dit is uitvoeren.

**6 milestones, 12 issues** — elk issue is zelfstandig leesbaar mét de geverifieerde OSM-namen, de
benodigde extracts (allemaal al binnen), de meetlat en de acceptatie:

| milestone | issues |
|---|---|
| M24.0 · fundament + restpunten | [LAR-503] · **[LAR-504] aftakken op elk punt ✅ Done** |
| M24.1 · Europa (Rijn-Donau-as) | **[LAR-492] Rijn ✅ Done** · **[LAR-505] Maas + delta ⬅️ NU** · [LAR-493] Main+MD-kanaal · [LAR-494] Donau · [LAR-495] Schelde/Seine/Rhône |
| M24.2 · Noord-Amerika | [LAR-496] Ohio (kolen!) · [LAR-497] Upper Mississippi + Illinois |
| M24.3 · Zuid-Amerika | [LAR-498] Amazonebekken compleet · [LAR-499] Hidrovía + Orinoco |
| M24.4 · Azië | [LAR-500] Grand Canal/Parelrivier/Chongqing · [LAR-501] Mekong + Hooghly |
| M24.5 · Rusland | [LAR-502] Wolga + Wolga-Don + Wolga-Baltisch |

**Aanbevolen volgorde:** M24.1 (grootste tonnage én de enige regio met een officiële meetlat naast
de VS) → M24.2 (Ohio = kolen, direct nodig bij M26) → de rest.

**Vaste werkwijze per systeem** (drie keer bewezen in de pilots):
1. **Namen opzoeken in de extract** — niet raden. Zie `decisions.md`.
2. **Ankers verifiëren tegen waar MARNET wérkelijk ophoudt** — alle drie de pilots eindigden ergens
   anders dan hun zone-naam suggereerde.
3. Segmenteren met `volgtOp` — sinds [LAR-504] mag een systeem **overal** op zijn voorganger
   aanhaken, niet alleen op het uiteinde. Splits waar een échte **verstoring** zit (Kaub), niet
   op de zeevaart/binnenvaart-grens: die vlag is alleen metadata en zegt niets over routering.
4. **Lengte tegen de officiële vaarafstand** = de beslissende controle, niet de puntafstand.
5. Regressie: 6818→9654 **19.610** en 6391→6818 **8.031** moeten exact blijven.

**Geblokkeerd:** [LAR-501] deels, op de Indiase Geofabrik-regio-namen (zie [LAR-503]).
**Niet meer geblokkeerd:** [LAR-495] — Geofabrik gebruikt de **pre-2016** Franse indeling;
`alsace`, `basse-normandie` en `rhone-alpes` bestaan wél, `normandie` niet (die geeft **0 bytes**
in plaats van een 404 — controleer dus de bestandsgrootte, niet de HTTP-status).

## 🔭 Later (ná M25): [LAR-490] LOD-systeem — het M26-startpunt

Spec = **`v2/design/lod-ontwerpbrief.md`** (commit `08f2341`; referentiebeelden in
`v2/design/referenties/` + als bijlage op het issue). Kern: semantische zoom ~4–5 banden op
`getAltitude()` · hiërarchisch nodemodel (`level`+`parent`, build-time geaggregeerd) · glow-bollen
(géén pilaren) · lijndikte hybride (meters op volume + pixel-minimum → ribbon/`Line2`) ·
data-ambitie C (koper-pilot top-±15–30 échte sites) · night-side testen in de pilot. **M25 is een
harde afhankelijkheid** (regionaal/lokaal = land-transport). Niet eerder oppakken dan M25-af.

## ✅ LAR-486 NL-pilot uitgevoerd (2026-07-19) — de M24-pipeline staat

`fetch_waterways.py` (bron-agnostische stitcher; OSM via Overpass, UNECE via de Blue Book
ArcGIS-laag — achter Cloudflare, via de Browser-pane) → `EXTRA_VAARWEGEN` in `bake_marnet.py`
(ketens `soort=1` + passage-labels `noordzeekanaal`/`waal` + zeevaart-vlag; corridor-toets ≤ 250 m;
zee-overgang NE-water óf waterweg-zone) → verzoening-cache (35 min → 1 min) → `?vaarwegbron`-toggle
+ ODbL/UNECE-attributie. Tests: zeenet exact (19.610/8.031 op de oude knopen), Amsterdam via
IJmuiden (−131 km), R'dam→Nijmegen 172 km, snaps 0,8/2,1/3,8 km. Commit `d9a9e0f`, live op Pages.

## 📋 Vorige stand (bronnenplan, 2026-07-19 — uitgevoerd)

**Het bronnenplan is besloten (2026-07-19, plansessie zonder code).** Kerninzicht: de **corridor-toets vervangt
de vlak-toets** — rivieren/kanalen bestaan niet als water in de NE-polygonen, dus elke binnenwater-edge wordt
getoetst als "elk ~2 km-monster ≤ ε van een bevaarbare-vaarweg-middellijn"; de polygoon-toets blijft alleen op
de zee-overgang gelden (mondings-knoop op een MARNET-knoop in NE-water). Besluiten + context in LAR-485.

1. **[LAR-486] NL-pilot (High)** — NZK + Waal (R'dam→Nijmegen) **twee keer** bouwen: uit **OSM** (Overpass,
   `waterway=canal|river` + CEMT-tags) én uit de **UNECE E-waterway-shapefile** (Blue Book) → het
   vergelijkingsrapport beslist de definitieve bron-rolverdeling. Bouwt meteen de hele pipeline:
   `v2/tools/fetch_waterways.py` (cache in `v2/build-cache/`) → `EXTRA_VAARWEGEN`-stap in `bake_marnet.py`
   (edges `soort=1` + systeemlabel + zeevaart-vlag, lon-normalisatie) → `ports.json` her-snappen
   (Amsterdam→NZK-knoop, Nijmegen→Waal-knoop). **Acceptatie: Amsterdam vaart via IJmuiden uit** (het
   screenshot-bewijsstuk), Nijmegen-snap 79 km → <5 km, regressie Duluth→R'dam 8.031 / R'dam→Shanghai
   19.610 onveranderd. ODbL-attributie ("© OpenStreetMap contributors") in de HUD meenemen.
2. **[LAR-487] VS-pilot** (blocked by 486) — Mississippi stroomopwaarts (zone → Memphis/St. Louis) × **USACE
   NWN als onafhankelijke meetlat** (inland filteren); relevant voor kolen-binnenvaart in M26.
3. **[LAR-488] China-pilot** (blocked by 486) — Yangtze-verdieping (zone → Wuhan, evt. Chongqing); zeevaart-vlag
   t/m Nanjing; **géén scheidsrechter** = bewust de zwaarste controle-situatie; valideert de wereldwijde uitrol.
4. **Daarna: uitrol + restpunten uit [LAR-485]** — het complete commercieel bevaarbare net (EU CEMT ≥ IV, VS
   USACE-net, elders de commerciële systemen: Paraná/Amazon/Wolga incl. Kaspische dekking-check/Mekong/
   Irrawaddy/Congo/Grand Canal), Yangon/Moulmein-stubs → echte riviergeometrie, en de 2 restedges
   (Södertälje-archipel, Channel Islands-koorde). Beleid is al besloten: **labels bij de bake** (passage-label
   per systeem + zeevaart-vlag); router blijft permissief, filteren = M26/M21 via `vermijd`.

## ✅ M23 AFGEROND op visuele go na (2026-07-18) — LAR-483 uitgevoerd

- `v2/tools/bake_marnet.py`: netwerk **één keer** verzoend met de 1:10M-wereld — 9.686 knopen / 15.933
  edges, 148/150 landsnijders omgelegd, 93 binnenwater-edges (29 zones), 2 onopgelost. Meren = water.
- `v2/data/marnet.bin/json` (1,17 MB varint) + `ports.json` (3.962 havens → dichtstbijzijnde knoop).
- `v2/src/marnet.js`: één LineSegments (blauw=zee, amber=binnenwater) + **A\*-router ~3 ms** met
  passage-restricties (default `northwest` dicht = searoute's default; meteen het M21-mechanisme) +
  HUD-toggle + route-test-UI.
- Gemeten: R'dam→Shanghai **19.610** via gibraltar+suez+babalmandab+malacca · Antofagasta→Shanghai
  **18.915** op de 50°N-lane (searoute 18.880 = M18-benchmark) · Yokohama→LA **9.111** · Duluth→R'dam
  **8.031** door Meren+Seaway.
- Twee structurele bugs gevangen: Noordwest-Passage als kortste pad (→ restrictie) en **15 dubbele
  ±180-knopen** die de trans-Pacific doorknipten (→ lon-normalisatie).

## ✅ M22 AFGEROND (2026-07-18) — LAR-484 Done

`v2/` staat en is live: https://larswalters.github.io/grondstoffen-atlas/v2/ (t/m `4dd48d5`).
Lars' go: *"dit is echt goed… nu kunnen we die vectorlijnen als bron van waarheid gebruiken en de view
opties zijn top zo."* **Buiten `v2/` is niets aangeraakt** — de oude atlas op de root staat onveranderd.

Wat er ligt om op verder te bouwen:
- `v2/src/globe.js` — scene, **hoogte-gebaseerde** zoom/sleep, ACES, `logarithmicDepthBuffer`
- `v2/src/world.js` — de vectorwereld (één `LineSegments`, 481.675 punten)
- `v2/src/tiles.js` — Esri/OSM-tegels tot z19, shell + detailpatch, invaden
- `v2/tools/measure_world.py` · `v2/tools/bake_world.py` · `v2/data/world-10m.{bin,json}`

## 📜 Het M23-plan zoals het vóór de uitvoering stond (uitgevoerd — ter referentie)

De opdracht is onveranderd sinds de diagnose van 18 juli, maar nu pas uitvoerbaar: **verzoen het
MARNET-netwerk ÉÉN keer met de kustlijn en routeer daarover**, in plaats van per haven-paar corridors te
bakken en elke kapotte edge apart te repareren.

Waarom het nú kan: MARNET is een **grove graaf** (15.840 segmenten, mediaan 83 km maar **max 3.611 km**) —
kaal over de bol leggen voorkomt landtreffers niet. Tegen 1:50M verzoenen had weinig zin (7,7 km puntafstand,
gaten tot 628 km). Tegen **1:10M** (1,5 km, grootste gat 55 km) is de verzoening wél betekenisvol.

Concrete eerste stappen:
1. MARNET in `v2/` laden en tegen de 1:10M-wereld leggen: **hoeveel** knopen/edges liggen op land?
2. Knopen die op land vallen naar het dichtstbijzijnde water verplaatsen; edges die land kruisen opknippen
   of herrouteren — **één keer**, in de baker, niet per route.
3. Het gerepareerde netwerk **meesturen naar de browser** (vastgelegd besluit: anders geen simulator — met
   kant-en-klare lijnen kun je niet herrouteren als M21 een knelpunt sluit).
4. Testen **haven→haven** zoals Lars vroeg, met zijn visuele check op realisme; de machine bewaakt de
   objectieve regels (nul landkruisingen over alle banen, bundeling, geen kaarsrechte stukken).

## 🎨 Uitgesteld, bewust: de schoonheidsslag
Echte Rayleigh/Mie-verstrooiing, oceaan-specular (zonneglinstering) en dag/nacht-terminator met stadslichten
(`earth-night.jpg` ligt klaar). Bewust ná de geometrie — deze shaders hangen aan de definitieve wereld.
**De landvulling is vervallen:** met tegels als oppervlak is er niets te vullen.

> **De belangrijkste les van 2026-07-18, lees dit eerst:** vier visuele klachten van Lars bleken symptomen
> van **één ontwerpfout**, niet vier bugs. Eén puntenlijst droeg tegelijk de **vorm** van de lijn (wil weinig
> punten), de **vaarsnelheid** (wil gelijkmatige afstand) en de **baan-klem** (wil juist veel punten in nauw
> water) — elke fix voor de één brak de ander. Na ontkoppeling verbeterde *alles tegelijk*. Merk je dat een
> fix iets anders breekt: **stop met patchen en zoek de koppeling.** Lars zelf: *"anders blijven we heen en
> weer gaan zonder echt een fix."*
>
> **Cijfers na de ontkoppeling:** snelheidsvariatie **15,9× → 1,27×** (slechtste 47× → 2,3×) · landtreffers
> **406 → 108** · Japan **8 → 0** · Baja **21 → 0** · Malakka **9 → 0** · geometrie 3.710 → 817 punten.
> Commits t/m `9444fcb` gepusht.

## 🛑 BESLUIT 2026-07-18 — huidige atlas BEVROREN, kaartlaag opnieuw in fasen

**De atlas die er nu staat blijft precies zoals hij is.** Live, ongemoeid, mét de schoonheidsfoutjes.
Lars: *"wat we nu hebben vind ik al wel erg mooi om te zien, alleen zitten er wel veel schoonheidsfoutjes in."*
**Alle M18-issues staan on hold** (LAR-474/475/476/477/478 → Backlog, `[ON HOLD]` in de titel).
Niet verder patchen aan de huidige routelaag.

### De nieuwe volgorde (Lars' eigen plan)

| fase | wat | status |
|---|---|---|
| **M22** | gedetailleerd **vector-wereldmodel** = de waarheid | ⬅️ **START: LAR-484 (Urgent)** |
| **M23** | **MARNET-zeeroutes** erop, testen haven→haven | LAR-483 |
| **M24** | **binnenwater** (Rijn/Yangtze/Saint-Laurent/Kaspisch) | ná go op M23 |
| **M25** | **land/spoor** — bewust laatst (OSM = gigabytes) | ná M24 |
| **M26** | **samenvoegen**: de 14 grondstoffen erop terugzetten | slot |

**Waarom M22 eerst:** er bestaan **drie wereldmodellen** die het niet eens zijn — satellietbeeld (wat Lars
ziet) · `LAND_POLYS` op 1:50M (waar ik tegen valideer) · MARNET's eigen kustlijn. Een route kan mijn test
doorstaan én er op zijn scherm fout uitzien. **Zolang dat zo is meten we langs elkaar heen** — dat verklaart
waarom sommige "fouten" bleven terugkomen. Lars' oplossing: een gegenereerde vectorwereld die scherp blijft
bij inzoomen wordt de waarheid; satelliet wordt een skin.

**Waarom M26 laatst kan:** de grondstoffendata staat **volledig los van routering**. Het is een verhuizing,
geen herbouw. Lars: *"het opzoeken van mijnlocaties en raffinages is peanuts vergeleken met zo'n kaart maken."*

### ⚠️ Bij de start van de nieuwe sessie eerst regelen (staat ook in LAR-484)

1. **✅ BESLOTEN: de nieuwe bol leeft in `v2/` binnen deze repo** (Lars, 2026-07-18). Waarom: Pages
   deployt 'm gratis mee (`…/grondstoffen-atlas/v2/` live bij elke push), gereedschap en data liggen
   ernaast zonder kopiëren, en M26 (samenvoegen) wordt triviaal. **Harde regel: buiten `v2/` wordt
   NIETS aangeraakt** — de oude atlas op de root blijft bevroren; elke overtreding is zichtbaar in de diff.
   **Lars kijkt mee via https://larswalters.github.io/grondstoffen-atlas/v2/** (bestaat pas na de eerste
   push van de map; tot die tijd 404). Zet er vanaf dag één een `index.html` + cache-busting in, zodat
   die link meteen iets toont en zijn feedbackloop werkt.
2. **De working tree is dirty** (`src/util.js`, `tools/lane_widths.js`, `data/_searoutes.js` = de
   half-afgemaakte asymmetrische klem). **Niet afmaken, niet committen** — terug naar `9444fcb` (of
   stashen) zodat `main` schoon matcht met wat live staat vóór `v2/` begint.

### Ontwerpkeuzes die al vastliggen

- **Netwerk mee naar de browser** — anders geen echte simulator (nu sturen we kant-en-klare lijnen mee waar
  je niet mee kunt rekenen; dan wordt M21 een diavoorstelling i.p.v. een berekening).
- **Dichtheid ≠ gladheid.** Meer punten koopt land-nauwkeurigheid, *niet* schoonheid — een kortste pad over
  een fijn raster geeft trapjes (precies wat `detour_around_land` deed). Gladheid = aparte opruimstap.
- **Budget is geen beperking:** MARNET ≈ 310 KB tekst (~100–130 KB gezipt); hersamplen op 5 km → ~260.000
  knopen ≈ 1,2 MB, route zoeken ≈ tiende seconde. De atlas bouwt nu al een raster van 1440×720 in **45 ms**.
- **Doel: ruim op PC, werkbaar op mobiel** (Honor Magic V5).
- **De machine bewaakt de objectieve regels** zodat Lars' visuele check over *realisme* gaat, niet over bugs.

---

## Referentie — de sessie die tot dit besluit leidde (LAR-483 blijft geldig als M23-kern)

De sessie van 18 juli liep op 500k tokens; Lars vroeg expliciet om over te dragen.
**[LAR-483] is zelfstandig leesbaar geschreven — begin daar, niet hier.**

1. [ ] **Routeer over één gerepareerd MARNET-netwerk i.p.v. per haven-paar.** Kern: corridors worden nu per
       paar gebakken → (a) routes naar dezelfde bestemming **bundelen niet** (Lars: *"lijnen gaan uit elkaar
       terwijl ze dezelfde bestemming hebben naar China"*), (b) dezelfde kapotte edge wordt **steeds opnieuw**
       gerepareerd (7 corridors deelden hetzelfde Baja-trapje), (c) antipodale paren kiezen willekeurig een
       halfrond. Fix: netwerk laden → **één keer** verzoenen met `geo-data.js` → daarover routeren.
       Hergebruik `seg_land_hit()` / `detour_around_land()` / `simplify_water()` uit de baker.
       **Gemeten:** MARNET = 15.840 segmenten / 9.646 knopen, segment mediaan 83 km maar **max 3.611 km** →
       een **grove graaf, geen waterkaart**; kaal over de bol leggen voorkomt land-treffers dus níet.
2. [ ] **Beslis eerst:** build-time bakken vanaf het gerepareerde netwerk (licht, past bij de spec) óf het
       netwerk naar de runtime (~300 KB, nodig voor M21). Advies: build-time, netwerk bewaren.

## ⚠️ Werkende boom — NIET gepusht

3. [ ] **Asymmetrische baan-klem** (links/rechts apart i.p.v. rondom), zodat één los eiland niet de hele
       waaier dichtknijpt — Lars: *"voor de westkust van Amerika komen de lijnen samen terwijl dat niet hoeft."*
       Stand: Baja-spreiding hersteld (**143 km**) maar Japan ging **0 → 52** treffers; laatste wijziging
       (waaier ±60° per zijde i.p.v. één straal) is **nog ongemeten**. `SIDE_SIGN = 1` is empirisch bevestigd
       (154 vs 1.571) — niet opnieuw uitzoeken. **Beslis of dit nog nodig is** als LAR-483 doorgaat; de klem
       kan van vorm veranderen. Ongecommit: `src/util.js`, `tools/lane_widths.js`, `data/_searoutes.js`.

## Daarna

4. [ ] **LAR-474 koper-pilot afronden** — blijft In Progress; de visuele go/no-go van Lars ontbreekt.
5. [ ] **LAR-477 uitrol 13 grondstoffen** (pipeline + checker staan klaar; MARNET dekt óók Saint-Laurent/Kaspisch).
6. [ ] **LAR-480 + weergave** — *"het lijkt erop alsof je het water niet echt goed kan onderscheiden op deze
       kaart"* + het openstaande punt "wereldbal-weergave duidelijker". **Geen routing** — bewust apart
       gehouden zodat de twee sporen niet weer door elkaar lopen.
7. [ ] **LAR-482** — AIS-dichtheidslaag ("echte schepen op de bol" met een knop), ná M18. Besloten 18 juli:
       MARNET blijft de router (AIS toont *schepen*, geen *lading*; geen gratis wereldwijde historie).
8. [ ] Klein cosmetisch (mag wachten): haven-uitvaart-bochtjes punt 1 (110–160°, onder de marker) ·
       Rotterdam→Duitsland laatste-mijl-waaier (4 ship-stromen over land; bestond al vóór de pilot).

## Vaste pipeline (volgorde telt)

```
python tools/bake_searoutes.py copper   # geometrie (vorm)
node tools/lane_widths.js               # klem-profiel wp (los van de geometrie)
node tools/check_corridors.js           # landkruisingen + scherpe bochten
node tools/stamp_assets.js              # CACHE-BUSTING — anders ziet Lars niets veranderen
python build-standalone.py              # 55 checks
```

## Valkuilen bij verifiëren (kostten 18 juli de meeste tijd)

- **Meet over ALLE 7 vaarbanen**, niet alleen de middellijn. De eerste Japan-verificatie testte alleen de
  middelste baan en verklaarde het probleem ten onrechte opgelost — terwijl de klacht juist over de
  **buitenste** banen ging.
- **Cache-busting is geen luxe.** `index.html` laadde assets zónder versie terwijl Pages `max-age=600` stuurt
  → Lars zag **drie fixes lang "geen verschil"** terwijl alles wél live stond. Dat was de bron van de meeste
  frustratie. `tools/stamp_assets.js` lost het op; draai 'm vóór elke commit die assets raakt.
- **De Browser-pane cachet script-tags** hardnekkig, óók op een nieuwe poort mét querystring. Verifieer via
  injectie: `fetch(url, {cache:'no-store'})` → `<script>`-element.
- `const SEAROUTES` kan **niet** opnieuw gedeclareerd worden → bij injectie `const SEAROUTES =` vervangen
  door `window.__SR2 =`.
- WebGL-screenshots hangen in een verborgen pane → **visuele bevestiging blijft Lars**.

## 🧭 M18 · Realistische zeeroutes (searoute) — LAR-473..478 · stand na de pilot-bouwsessie

- [x] **LAR-473 — spec + besluiten** ✅ Done (2026-07-17): `design/zeeroutes.md`, "MARNET beslist", datamodel,
      hard falen, drempel ">15% zonder doorgang".
- [~] **LAR-474 — PILOT koper** ⬅️ **gebouwd, in visuele test** (zie boven). 84 legs / 0 kapot / 24 cache-hits,
      regressie schoon, zeereizen −9,3%.
- [~] LAR-475/476 — generator + engine de facto gebouwd binnen de pilot (voor koper); blijven open tot de uitrol.

**De koers na "inhoudelijk compleet": niet een 15e grondstof, maar route-kwaliteit.** Lars: *"een boot zou daar
nooit zo varen."* De drie feature-milestones **staan** op route-nauwkeurigheid → M18 eerst.

**Waarom (bewezen 2026-07-17):** Antofagasta→Shanghai = grote-cirkel **18.526 km** · searoute (echte lanen)
**18.880 km (+2%)** · **onze bol 19.970 km (+8%)**. Het handgeplaatste vaarpunt **`wp-pac-zuid`** (26°Z) dwingt
**~1.090 km omweg** af. De `via`-ketens zijn grotendeels handmatige compensatie voor een slechte router.
Diagnose in `searoute.js`: `openRadiusDeg: 1.2` (~130 km geforceerd water rond élk knelpunt) + 8-richtingen-A\*
(trapjes; Golf→Rotterdam 33 richtingswissels) + grof raster/gretige heuristiek/**géén echte vaarlanen**.

- [ ] **LAR-473 — spec `design/zeeroutes.md`** (design-first): datamodel corridor-cache, hoe `flows.js` 'm gebruikt,
      fallback-gedrag, netwerk bewaren voor M21, verificatie-criterium (routelengte ÷ grote-cirkel), en **het open
      besluit**: via-punten op zee-legs **(a) opruimen** of **(b) behouden als hint** — **Lars beslist**.
- [ ] **LAR-474 — PILOT: koper volledig op searoute** ⬅️ **START VAN DE VOLGENDE SESSIE.** Baseline → corridors
      extraheren (**mét** `via`-keten!) → searoute draaien → vergelijken → renderen → **go/no-go Lars** vóór de andere 13.
      Koper = beste testcase (bewezen-foute Antofagasta-corridor + Andes-trechter + Copperbelt-**land**routes die
      ongemoeid moeten blijven).
- [ ] **LAR-475 — corridor-cache generator** (Python, build-time): unieke zee-corridors **gededupliceerd per haven-paar**
      over alle 14 → `data/_searoutes.js`. Fouten hard maken, determinisme, bestandsgrootte bewaken.
- [ ] **LAR-476 — engine**: `flows.js` rendert gebakken polylines i.p.v. live A\*; land/lucht ongemoeid; **`laneShape`
      (vaarbanen-waaier) expliciet checken** = de subtielste regressie-val; **netwerk bewaren voor M21**.
- [ ] **LAR-477 — uitrol 13 + via-punten opruimen** (ná pilot-go). Let op: uranium's Kaspische oversteek (ingesloten
      zee) heeft searoute waarschijnlijk niet → expliciet checken, niet stil laten wegvallen. Goud/PGM/diamant = `air`, niet aanraken.
- [ ] **LAR-478 — verificatie + build + visueel** (Lars). IJkpunt: Antofagasta→Shanghai 19.970 → ~18.880 km.

> ⚠️ **Harde regel:** vergelijk **nooit** tegen een kale origin→dest A\*-run. De pilot van 16 juli deed dat →
> "route A", een pad dat de bol nergens tekent (Lars zag het meteen: *"ik zie op onze wereldbol niets dat route A
> neemt"*). Vergelijk altijd tegen wat `flows.js` werkelijk rendert.

**Status:** `searoute` 1.6.0 geïnstalleerd. Pilot-artefacten (`astar_paths.json`, `zeeroutes_vergelijking.html`) in
`…/Temp/claude/C--automation/ec6b9a39-…/scratchpad/`.

**Volgorde daarna:** M19 (knelpunt-stress) → M20 (China-meta-view) → M21 (disruptie-simulator). ⚠️ M21's aanpak is
**herijkt**: knelpunt blokkeren = *edge uit het netwerk halen*, niet een raster-cel-masker.
⚠️ M18 staat in Linear ónder M21 gesorteerd (`sortOrder` niet zetbaar via MCP) — even slepen in de UI.

## 🐛 Losse issues (buiten M18)

- [x] **LAR-479 (High) — tegel-patch wordt afgekapt bij inzoomen** ✅ **Done (2026-07-17), bevestigd door Lars.**
      Twee oorzaken: budget < één patch (40 vs 42–72) mét noord→zuid-vulling, én een ontbrekende `cos(lat)` in
      `detailZoomFor()`. Fix: `cos(lat)` + budget 96 + midden-naar-buiten. Commit `297016f`.
- [x] **Zoom-evenredig draaien** ✅ **Done (2026-07-17), bevestigd door Lars.** Geen issue-nummer — kwam er tijdens
      dezelfde sessie bij (Lars: *"als je een stuk bent ingezoomd dan is het draaien super gevoelig"*). Commit `297016f`.
- [x] **LAR-481 — marker-LOD vuurde averechts** ✅ **Done (2026-07-17), bevestigd door Lars.** `forced` overrulet tier
      voor 57/63 nodes → de LOD raakte alléén de 6 context-mijnen zónder stroom. Markers verdwijnen niet meer op tier;
      `tier` = alleen labels. Commit `8dda38e`.
- [ ] **LAR-480 (Low) — markers-contrast bij inzoomen.** Het is contrast, niet schaal. Richting: halo/outline.
      **Nu relevanter:** de tegels zijn scherper (drukkere ondergrond) én er staan meer markers (LAR-481). Nog steeds
      ná M18 — de zeeroutes veranderen wat er ópstaat.
- [ ] **(Low, geen issue) — mislukte tegel wordt nooit opnieuw geprobeerd** (`ensureTile` early-return + alleen
      `console.warn` → permanent opacity 0). Bijvangst van LAR-479, apart defect. Iets relevanter met `maxTiles: 96`
      (meer gelijktijdige requests), maar niet waargenomen — zie `bugs-and-risks.md`.
- [ ] **(Na M18) — stromen ook tieren?** De tier-LOD is nu de facto uit voor markers. Wil je uitgezoomd écht
      ontdubbelen, dan moeten stromen mee — raakt `flows.js` (= pilot-code) en het beeld van alle 14. Alleen oppakken
      als Lars uitgezoomd te druk vindt (6 extra bolletjes bij koper).

---

## 🎉 Backlog was leeg (2026-07-16) — afgerond
Alle 3 resterende backlog-issues afgerond + gepusht → live op Pages. **Niets meer In Progress/Todo/Backlog in Linear.**
- **LAR-471 · lab-grown-toggle (diamant)** ✅ — het 6e optionele-laag-patroon (`layer:"labgrown"`): 3 productie-nodes
  (China/Henan HPHT, India/Surat CVD, VS/Washington premium-CVD) + 6 flows die de VS-verlovingsringmarkt ondergraven;
  5 engine-plekken + violette octaëder-marker + chip "lab-grown"; default uit, alleen bij diamant. Commit `f6c95f6`.
- **LAR-447 · recycle-tooltip per-grondstof** ✅ — `recycleHint`-veld op de resource + `main.recycleHint()` + generieke
  fallback in `ui.js`; hints op REE (<5% magneet) / PGM (~25% autokat) / grafiet (nascent). Commit `9feb8f2`.
- **LAR-448 · PGM-beursvoorraden-laag** ✅ — PGM's tweede optionele toggle naast recycling (LPPM/NYMEX/TOCOM, pure data,
  0 engine-wijziging, hergebruik exchange-toggle). PGM = eerste grondstof met twee toggles. Commit `9feb8f2`.
- Headless geverifieerd: diamant 41 legs/0 kapot, PGM 52 legs/0 kapot, beide toggles filteren correct, regressievrij.

**Enige open punt:** visuele eindbevestiging op de live URL/mobiel = Lars (violette lab-grown-arcs op de VS-markt bij
diamant + de LPPM/NYMEX/TOCOM-kluismarkers bij PGM). WebGL-screenshot hangt headless.

**Toekomstig werk** = alleen nog een nieuwe **15e grondstof** (zilver/kolen-patroon) óf losse verfijningen — geen
openstaande features meer. Losse hygiëne: bureaublad-originelen (`atlas-lithium-kobalt.html` + `globe-oud`) opruimen.

---


## 🎉 De basis-10 is compleet — nu uitbreiden met nieuwe grondstoffen (14 en groeiend)
Na M14 (grafiet) stond er geen enkele grondstof van de **basis-10** meer op "basis". Daarna komen de **nieuwe
grondstoffen** erbij (niet basis→uitgewerkt maar een nieuw `data/<x>.js` + script-tag + build-check, het zilver-patroon):
zilver (M13), gas (M15), diamant (M16), **kolen (M17)**. Volledig uitgewerkt nu: de basis-10 + zilver + gas + diamant +
kolen = **14** (gas M15 / diamant M16 / kolen M17 = de nieuwe batch, alle drie in parallelle sessies gebouwd + gepusht).
Het brief→bouw-runbook (sectie I) + het nieuwe-grondstof-plumbing-patroon (LAR-436/457/463) blijven de vaste flow.

## M15 · Gas ✅ uitgevoerd (2026-07-16) — LAR-460, 462, 463, 464, 465, 466
Nieuw `data/gas.js` (42 nodes / 51 flows / 6 tensions) + brief `design/gas.md` + `<script>`-tag in `index.html` + 5 gas-checks
in `build-standalone.py`. Aardgas/LNG: **gas is nauwelijks te verplaatsen** → captive pijpleidingen vs de LNG-liquefactie-
trechter (VS-Golfkust/Qatar/Australië); Europa-pivot 2022 + Russische oost-pivot; Qatar via Hormuz (géén bypass, scherper
dan olie). Schip+pipeline, **géén nieuw chokepoint/render-modus/marker-types**; opslag hergebruikt de olie-`reserve`-toggle
(0 engine-wijziging). Headless: **97 legs / 0 kapot / 0 straight**, regressievrij (2 Arctische Yamal-routes + captive-
pijpleidingen routeren correct zonder nieuw vaarpunt). Commits `040d2b7` (data) + `a8378ef` (build-checks), **gepusht → live
op Pages** (git-index-race met de diamant-sessie teruggedraaid met `reset`+`--only`, sectie J). LAR-460/462/463/464/466 Done.
- [ ] **LAR-465** — visuele bevestiging op de live URL/mobiel (https://larswalters.github.io/grondstoffen-atlas/) = **Lars**.
  Checken: de twee leversystemen (donkere pijpleiding-arcs vs. heldere LNG-oceaan-arcs), Hormuz als Qatar's enige uitgang,
  de VS-Golfkust-waaier (oost naar Europa + west via Panama), de gekrompen Rusland→EU-pijl + de dikke Power-of-Siberia→China,
  en de opslag-toggle ("voorraden", default uit).

## M16 · Diamant ✅ uitgevoerd (2026-07-16) — LAR-467 t/m 472
Nieuw `data/diamond.js` (25 nodes / 35 flows / 6 tensions) + brief `design/diamant.md` + `<script>`-tag in `index.html` +
4 diamant-checks in `build-standalone.py`. De scherpste downstream-trechter (Surat ~90-95%) + Antwerpen-G7-certificering +
Alrosa-herrouting; diamant **vliegt** (hergebruik goud/PGM air-mode, 0 engine-wijziging, géén nieuw chokepoint/marker-types).
Headless: 35 legs (27 air + 8 road) / 0 kapot / 0 straight / 0 degen, regressievrij. Commits `72d134c` (feat) + `7d06a0c`
(build), **gepusht → live op Pages**. LAR-467/468/469/470 Done.
- [ ] **LAR-472** — visuele bevestiging op de live URL/mobiel (https://larswalters.github.io/grondstoffen-atlas/) = **Lars**.
- [ ] **LAR-471 (Backlog) — lab-grown-toggle** bouwen zodra de gedeelde engine-tree schoon is: nieuwe optionele laag
  `layer:"labgrown"` + `showLabGrown` op 5 plekken (`config`/`main`/`flows`/`markers`/`ui`); 2-3 productie-nodes (China/Henan
  HPHT + India/Surat CVD) die de Surat-slijperij én de VS-markt ondergraven. Bewust uitgesteld i.v.m. de parallelle sessies
  (zoals uranium's LAR-414 / olie's LAR-432). In v1 leeft lab-grown als `tension`.

## M17 · Kolen ✅ uitgevoerd (2026-07-16) — LAR-455 t/m 459, 461
Nieuw `data/coal.js` (34 nodes / 33 flows / 6 tensions) + brief `design/kolen.md` + `<script>`-tag in `index.html` +
`grens-gashuunsukhait` (Mongolië-Gobi) in `_chokepoints.js` + 5 kolen-checks in `build-standalone.py`. De vorm = **de
binnenlandsheid, géén trechter** (~85% verstookt waar gedolven; ~15% zeehandel); China = swing-koper; twee kolen
(thermisch/cokeskool via note+tension); drie her-routeringen (China-Australië-ban, Rusland-oost-draai, Mongolië-Gobi-
corridor). Schip+land, géén render-modus/marker-types/toggle-laag.
- [x] Research upstream (winning) / downstream (verbruik + staal + zeehandel + her-routeringen) inline in `design/kolen.md` (LAR-455/456).
- [x] Nieuwe-grondstof-plumbing (LAR-457): `data/coal.js` + `<script src="data/coal.js">` in `index.html` + 5 kolen-checks in `build-standalone.py`.
- [x] Nieuw chokepoint `grens-gashuunsukhait` (LAR-458) in een eigen COAL-blok in `_chokepoints.js` (Kasumbalesa/Ruili-patroon).
- [x] `data/coal.js` uitgewerkt (LAR-459): mijnen (binnenlandse reuzen + exportmijnen), havens, markt-centrales/staalhubs, Mongolië-corridor; 6 tensions.
- [x] Verificatie headless (LAR-461, deel): **kolen 111 legs / 0 kapot / 0 straight / 0 degen / 0 unresolved via**, regressievrij. Route-bug gefixt (Roberts Bank ingesloten → Ridley/Prince Rupert). `build-standalone.py` (+5 kolen-checks) → `atlas-standalone.html` geregenereerd.
- [x] Code-commit `75c3483` (repo `main`, Claude-trailer) — **alléén eigen bestanden** gestaged (sectie J: 3 parallelle sessies grafiet/diamant/gas ongemoeid; alléén de coal-regel uit de gedeelde `index.html` via gerichte patch).

**Open (M17 afronden):**
- [ ] **Code-commit `75c3483` pushen** naar GitHub → live op Pages (repo is sinds M13 live). *(Nog niet gepusht — zie onder.)*
- [ ] **Visuele bevestiging op de live URL/mobiel** (LAR-461, In Progress) — alleen Lars (WebGL-screenshot hangt headless), via https://larswalters.github.io/grondstoffen-atlas/. Checken: de grote binnenlandse blokken (China/India/VS/Rusland, dof) vs. de zeehandelslaag; de twee kolen (thermisch→centrales, cokeskool→staalhubs); de Mongolië-Gobi-landcorridor; het naspel van de Australië-ban (export naar India/Japan/Korea).

## M14 · Grafiet ✅ uitgevoerd (2026-07-15) — LAR-449 t/m 454
`data/graphite.js` van "basis" (10/3) → volledig **uitgewerkt** (31 nodes / 26 flows / 6 tensions). De vorm = een
**REE-achtige verwerkingstrechter met TWEE feedstocks**: natuurlijk vlokgrafiet + synthetische naaldcokes convergeren
op de anode-verwerking die **~90%+ in China** zit (Shandong natuurlijk, Binnen-Mongolië synthetisch). Schip+land,
**géén nieuw chokepoint** (4e na nikkel/olie/zilver). Grafiet was het **laatste basis-10-bestand** (bestond al + stond
al in `index.html` → basis→uitgewerkt, géén nieuwe script-tag).
- [x] Research upstream (vlok + naaldcokes) / downstream (verwerkingstrechter + dec-2023 exportcontroles) inline in `design/grafiet.md` (LAR-449/450).
- [x] Ontwerp-brief `design/grafiet.md` (LAR-451): mijnen + naaldcokes-bronnen, anode-verwerkers, havens, gigafabrieken, recyclers, 6 tensions.
- [x] `data/graphite.js` uitgewerkt (LAR-452): 8 natuurlijke vlokmijnen (China #1, Balama/Mozambique, Madagascar, Brazilië, Tanzania, Noorwegen, Oekraïne, Sri Lanka vein) + 2 naaldcokes-bronnen (VS/China) + 8 anode-verwerkers (Shandong/Binnen-Mongolië-trechter + Japan/POSCO/Vidalia/Novonix/Talga/NMG) + 6 havens + 4 gigafabriek-markten + 3 recyclers. Keten erts(vlok+naaldcokes)→raffinaat(gecoat sferisch/gegrafitiseerd anodepoeder)→product(cellen).
- [x] **Recycling-toggle** (LAR-453) = hergebruik van het REE/PGM-`recycle`-patroon met **0 engine-wijziging** (`layer:"recycle"` op nodes én flows); bewust bescheiden (3 recyclers, batterijgrafiet-recycling nog nascent). Chip verschijnt automatisch.
- [x] Verificatie headless (LAR-454, deel): **grafiet 77 legs (57 zee + 20 land) / 0 kapot / 0 straight / 0 warnings**; toggle aan=80 (+3 recycle); regressie schoon (0 kapot over álle grondstoffen). Route-bug gefixt: `gr-ref-japan→gr-mkt-korea-japan` road→ship (Japan→Korea over de Straat van Korea). `build-standalone.py` (+5 grafiet-checks) → `atlas-standalone.html` geregenereerd.
- [x] Code-commit `34b1ed4` (repo `main`, Claude-trailer) — **alléén eigen bestanden** gestaged (`data/graphite.js`, `design/grafiet.md`, `build-standalone.py`, `.claude/launch.json`; sectie J). **Gepusht** naar GitHub → live op Pages.

**Open (M14 afronden):**
- [ ] **Visuele bevestiging op de live URL/mobiel** (LAR-454, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless), nu triviaal via https://larswalters.github.io/grondstoffen-atlas/. Checken: de twee feedstock-stromen (vlok + naaldcokes) die op China convergeren, het emblematische Balama→Vidalia-draadje rond de Kaap, de dunne ex-China buildout-waaier (Talga/Novonix/NMG/POSCO), en de recycling-toggle (default uit).

## M13 · Zilver ✅ uitgevoerd (2026-07-15) — LAR-434 t/m 439
**De eerste écht nieuwe grondstof sinds de basis-10** (niet basis→uitgewerkt maar een nieuw `data/silver.js`
(42 nodes / 37 flows / 6 tensions) + `<script>`-tag in `index.html` + zilver-checks in `build-standalone.py`).
De vorm is fundamenteel anders: **géén winnings-trechter** — ~70-75% bijproduct van zink/lood/koper/goud
(aanbod inelastisch), terwijl de concentratie **downstream** zit (Chinese zonnepanelen/PV) → structureel
tekort dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt. Schip+land, **géén nieuw chokepoint** (derde na nikkel/olie).
- [x] Research by-product-winning / solar-vraag inline in `design/zilver.md` (LAR-434/435).
- [x] **Zilver als 11e grondstof geregistreerd** (LAR-436): `data/silver.js` + `<script src="data/silver.js">` na `oil.js` in `index.html` + 5 zilver-sanity-checks in `build-standalone.py`.
- [x] `data/silver.js` uitgewerkt (LAR-437): by-product-mijn-nodes (elk met hoofdmetaal-`note`), convergentie op Peñoles(Mexico)/KGHM(Polen)/Korea/China, solar-pull SGE→Jiangsu, 6 tensions. Keten erts(doré)→raffinaat(good-delivery baar)→product(solar/elektronica/sieraad).
- [x] **Kluis-/beursvoorraden-laag** (LAR-438) = hergebruik van de bestaande exchange-toggle met **0 engine-wijziging** (nikkel-patroon); 3 exchange-nodes (LBMA/COMEX/SGE) + 3 `layer:"exchange"`-aftap-flows; COMEX registered-vs-eligible + 2021-squeeze-nuance. Recycling always-on.
- [x] Verificatie headless (LAR-439, deel): **zilver 85 legs / 0 kapot / 0 straight / 0 warnings**; regressie schoon (andere uitgewerkte grondstoffen 0/0). 2 route-bugs gefixt (VS-raffinage Tacoma→Astoria; China-solar Suzhou→Jiangsu-kust) na empirisch testen. Exchange-chip + blurb + 6 tensions renderen. `build-standalone.py` (+5 zilver-checks) → `atlas-standalone.html` geregenereerd.
- [x] Code-commit `e091848` (repo `main`, lokaal-only, Claude-trailer) — **alléén eigen bestanden** gestaged (parallelle uranium-toggle-sessie op de gedeelde engine-files ongemoeid, sectie J).

**Open (M13 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-439, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: de diffuse mijn-origin bovenop andermans mijnen (geen winnings-trechter), de convergentie op Peñoles/KGHM/Korea/China, de dikke `product`-boog SGE→Chinese zonnecel-industrie, de India-sieradenstroom, en de kluis-toggle (LBMA/COMEX/SGE) die de aftap onder het tekort toont.

## M12 · PGM ✅ uitgevoerd (2026-07-15) — LAR-440 t/m 448
`data/pgm.js` van "basis" (9/3) → volledig **uitgewerkt** (38 nodes / 41 flows / 6 tensions). De scherpste twee-landen-
concentratie van de atlas, gesplitst over twee metalen: **Zuid-Afrika/Bushveld** = Pt/Rh, **Rusland/Norilsk** = Pd. PGM
**vliegt** (hergebruik goud-air-mode); **géén nieuw chokepoint, géén engine-wijziging** (derde na koper/nikkel).
- [x] Research upstream/downstream inline in `design/pgm.md` (LAR-440/441): ZA ~60% 3E (Pt/Rh), Rusland ~25% (Pd), Zimbabwe/NA/Finland; raffinage (Rustenburg PMR/Springs/Krasnoyarsk/Columbus + westerse huizen JM/BASF/Umicore/Heraeus/Tanaka); autokat + waterstof + recycling.
- [x] **PGM = luchtvracht, géén nieuw chokepoint** (LAR-442): hergebruik van de goud-air-mode (`mode:"air"`, JNB-gateway; "✈ vluchten" via `activeHasAir()`), concentraat/matte over land (Beitbridge/Kanaaltunnel/Baltische bruggen). Het grondstof-eigen "nieuwe element" is bewust géén nieuw element.
- [x] `data/pgm.js` uitgewerkt (LAR-443): 16 mijnen (8 ZA-Bushveld + Norilsk + Zimbabwe + Noord-Amerika + Kevitsa) / 9 raffinage-nodes / JNB-gateway / 8 markten / 4 recyclers. 6 tensions (concentratie, autokat + Pt↔Pd, rodium-spof, palladium/Rusland, waterstof-hedge, Eskom).
- [x] **Recycling-toggle** (LAR-444) = hergebruik van het REE-patroon met **0 engine-wijziging**; 4 recycler-nodes + 5 `layer:"recycle"`-flows (~25% autokat-recycling via de westerse huizen); chip via `hasRecycle()`.
- [x] Verificatie headless (LAR-445, deel): **pgm 49 legs / 0 kapot / 0 straight / 0 degenerate arcs**, regressievrij; lange risico-legs routeren correct; SAMECELL-fix (Japan-recycler uit Tokyo Bay → Kanagawa). `build-standalone.py` (+ 4 PGM-checks) → `atlas-standalone.html` geregenereerd (LAR-446).
- [x] Code-commit `2c4b668` (repo `main`, lokaal-only, Claude-trailer) — **alléén eigen bestanden** gestaged (parallelle zilver-/uranium-toggle-sessie op de gedeelde build-bestanden ongemoeid, sectie J).

**Open (M12 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-445, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: de dichte Bushveld-kluwen + de zware Norilsk-punt (twee bronnen), de hoge **luchtbogen** (géén zeeroutes) naar de westerse huizen + Azië, de recycling-retourbogen met de toggle aan, het dunne waterstof-draadje naast de autokat-bundel, scheeps-… nee: **vlucht**-voyages voor PGM.
- [ ] **Afwijkingen (Backlog):** LAR-447 (recycling-chip-tooltip generiek maken, nu REE-bewoord — raakt gedeelde `ui.js`), LAR-448 (optionele Pt/Pd-exchange-laag — pure data, hergebruik exchange-toggle).

## M11 · Olie ✅ uitgevoerd (2026-07-15) — LAR-428 t/m 433
`data/oil.js` van "basis" (18/15) → volledig **uitgewerkt** (45 nodes / 46 flows / 6 tensions). Olie's vorm is bewust
ANDERS dan alle eerdere: geen enkele trechter maar het **hele knelpunten-netwerk dat tegelijk oplicht** — Hormuz #1
(15 stromen), Malakka, Taiwan, Suez/Bab, Bosporus, Panama, Kaap (10 knelpunten). **Géén nieuw chokepoint** = het eigen aha.
- [x] Research upstream/downstream inline in `design/olie.md` (LAR-428/429): producenten + reserves≠productie (OPEC+), raffinage/product-trade/petrochemie.
- [x] **3 olie-only navigatie-vaarpunten** (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`) in een gelabeld OIL-blok in `_chokepoints.js` (LAR-430) — houden de VS/Venezuela-routes op het water; geen nieuw knelpunt (olie hergebruikt het hele bestaande net).
- [x] `data/oil.js` uitgewerkt (LAR-431): crude (erts) → raffinage; producten (raffinaat) → markt; petrochemie (product). Drie levende verhalen: Hormuz-bypass-pijpleidingen (Yanbu/Fujairah), Rusland-omleiding 2022→ (Primorsk/Novorossiysk/ESPO-Kozmino/Druzhba → India/China), Amerikaanse schalie-ommekeer (Corpus Christi). Kust-raffinaderijen `coastal:true`.
- [x] Verificatie headless (LAR-433, deel): **olie 210 legs / 0 kapot / 0 straight**; regressie schoon (baseline 5 = lithium 4 + goud 1, olie voegt 0 toe). Knelpunt-gebruik bevestigt het plaatje: Hormuz #1 (15), Malakka (14), Taiwan (12). `build-standalone.py` (+ 4 olie-checks) → `atlas-standalone.html` geregenereerd + zelf geverifieerd (210/0/0).
- [x] Code-commit `1d4ece5` (repo `main`, lokaal-only, Claude-trailer) — alleen mijn eigen bestanden gestaged (parallelle nikkel-sessie ontzien).
- [x] **Optionele SPR-voorraden-toggle** (LAR-432, Done) — gebouwd zodra de nikkel-sessie klaar was en de engine-bestanden vrij waren. `layer:"reserve"` = het **vierde** optionele-laag-patroon (goud-CB, koper-beurs, REE-recycling, olie-reserve), exact het koper-`exchange`-patroon op 5 plekken (config/main/flows/markers/ui) + olie-amber tank-marker. 5 SPR-nodes (US Gulf/China Dalian/Japan Kiire/India Mangalore/IEA-EU Le Havre, `stock` in mln vaten) + 5 vul-flows + tension `oil-t-spr`. Headless: olie 232 legs / 0 kapot / 0 straight; toggle uit=45/46, aan=50/51 (+5/+5); chip "voorraden" alleen bij olie; regressievrij. Commit `86c8c1f`.

**Open (M11 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-433, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: gloeit Hormuz als dikste knoop, dan Malakka erachter?; de Golf→Azië-bundel als dikste stroom; de twee dunne bypass-pijpleidingen (Yanbu/Fujairah) om Hormuz heen; de dikke Rusland→India-omleiding náást de gekrompen Rusland→Europa-pijl; de VS-exportpijlen uit Corpus Christi; het dunne Venezuela-pijltje (reserves-paradox); de **voorraden-toggle** (SPR-tanks US/China/Japan/India/EU); scheeps-voyages voor olie.

## M10 · Nikkel ✅ uitgevoerd (2026-07-15) — LAR-422 t/m 427
`data/nickel.js` van "basis" (13/4) → volledig **uitgewerkt** (50 nodes / 46 flows / 6 tensions). Schip+land, géén nieuwe
render-modus, **géén nieuw chokepoint** (tweede na koper die volledig op de bestaande routekaart draait).
- [x] Research upstream/downstream inline in `design/nikkel.md` (LAR-422/423): Indonesië-onshoring + class-1/class-2 + shakeout + LME.
- [x] `data/nickel.js` uitgewerkt (LAR-424): Indonesië-onshoring-trechter (erts blijft in het land = korte mijn→smelter-hops), twee nikkels (class-1 batterij vs class-2 roestvrij, HPAL→MHP/matte als brug), prijscrash-shakeout (Nickel West stilgelegd 2024), Filipijns ruw-erts-contrast. Coastal-markten (koper-fix).
- [x] **Beursvoorraden-laag (LME)** = hergebruik van de bestaande exchange-toggle met **0 engine-wijziging** (LAR-425); 4 LME-nodes + 5 `layer:"exchange"`-flows; nuance: alleen class-1 leverbaar + de 2022-squeeze. Recycling always-on.
- [x] Verificatie headless (LAR-426): **nikkel 91 legs (63 zee + 18 land + 10 korte hops) / 0 kapot / 0 straight**; regressie schoon (0 kapot over alle grondstoffen). `build-standalone.py` (+ nikkel-checks) → `atlas-standalone.html` geregenereerd.
- [x] Code-commit `08aa4f5` (repo `main`, lokaal-only, Claude-trailer) — alleen mijn 3 bestanden gestaged (parallelle olie-sessie ontzien).

**Open (M10 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-427, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: de Indonesische korte-hops-kluwen, de twee waaiers naar China (roestvrij + batterij) door Makassar/Lombok, de Filipijnse ruw-erts-contrastboog, het dunnere "oude wereld"-class-1-web, de scheeps-voyages, en de beursvoorraden-toggle (LME) aan/uit.
- [ ] **Vault push** — de vault-`git pull`/`push` faalde op een netwerkfout; lokaal gecommit, push zodra de verbinding terug is.

## M8 · Zeldzame aardmetalen ✅ uitgevoerd (2026-07-15) — LAR-416 t/m 421
`data/rare-earths.js` van "basis" (9/5) → volledig **uitgewerkt** (41 nodes / 38 flows / 6 tensions), **magneet-REE-framing**
(NdPr + Dy/Tb; `symbol: NdPr`, `unit: kt magneet-REO/jaar`). Schip+land, géén nieuwe render-modus.
- [x] Research → skelet `design/zeldzame-aardmetalen.md` 1-op-1 omgezet (LAR-416/417).
- [x] **Nieuwe grenscorridor `grens-ruili`** (Myanmar→China, `kind:"grensovergang"`) in `_chokepoints.js` — draagt de Dy/Tb-landstroom Kachin→Ganzhou (LAR-418).
- [x] `data/rare-earths.js` uitgewerkt (LAR-419): Ganzhou-scheidingstrechter + Mountain-Pass-rondreis + NdFeB-waaier + Lynas-draadje + EU-draadje.
- [x] **Recycling-toggle** (`layer:"recycle"`, default uit) bedraad over config/main/flows/markers/ui (LAR-420) — het derde optionele-laag-patroon; via `layer` op flows én nodes zodat koper's always-on recyclers ongemoeid blijven.
- [x] Verificatie headless (LAR-421, deel): **rare-earths 90 legs (39 land + 51 zee) / 0 kapot / 0 straight**; regressie schoon (5 kapot = bekende lithium/goud-baseline); toggle-test bevestigd. `build-standalone.py` (+ REE-checks) → `atlas-standalone.html` geregenereerd.

**Open (M8 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-421, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: convergeren de scheidings-bogen op Zuid-China?, loopt de Dy/Tb-landstroom over Ruili?, zichtbaar de Mountain-Pass-rondreis VS↔China?, de NdFeB-waaier naar EV/wind/defensie?, scheeps-voyages voor REE?, recycling-toggle aan/uit.
- [ ] **Code-commit** — 7 gewijzigde bestanden (`data/rare-earths.js`, `data/_chokepoints.js`, `src/{flows,main,markers,ui}.js`, `build-standalone.py`) + de wrapup-docs; repo lokaal-only (geen remote), branch `main`, Claude-trailer.

## M6 · Goud ✅ uitgevoerd (2026-07-14)
- [x] Research → brief `data/goud.md` (LAR-397/398).
- [x] Luchtroute-modus: great-circle 3e route-type in `flows.js` + marker-types airport/hub/cb/recycler (LAR-399).
- [x] `voyages.js` uitgebreid naar lucht + resource-bewuste teller "✈ vluchten" (LAR-400).
- [x] `data/goud.js` (73 nodes/48 flows, Ticino-trechter) + registratie in `index.html` (LAR-401).
- [x] Centrale-bank-laag als optionele toggle, default uit (LAR-402).
- [x] Verificatie headless: 371 legs / 0 kapot over alle 10 grondstoffen, regressievrij (deel LAR-403).
- [x] `build-standalone.py` → `atlas-standalone.html` (gegenereerde single-file build).

## LAR-403 ✅ afgerond (2026-07-14) — M6 volledig af
- [x] **Visuele bevestiging** — Lars bekeek de build thuis in de browser: "ziet er cool uit, geen aanmerkingen".
      LAR-403 → Done; alle M6-issues (LAR-397 t/m 403) Done. Lars zet `atlas-standalone.html` zelf op Netlify.
- [ ] Nog te doen (klein): bureaublad-restanten opruimen (`atlas-lithium-kobalt.html`, `globe-oud`) — nu unblocked.

## Openstaand — project-hygiëne
- [ ] **Project-repo committen** — goud.js/goud.md/edits/build-standalone.py staan dirty. Code-commit los van de
      wrapup-docs, op Lars' seintje (agent-trailer). Overweeg `atlas-standalone.html` in `.gitignore` (gegenereerd, 1,4 MB).
- [ ] Optioneel: **GitHub-remote** voor de repo (nu lokaal-only).

## Optionele verfijningen goud (later, niet-blokkerend)
- [ ] Per-leg touch-down bij hubs i.p.v. één boog over de via-punten (nu bulge't de boog in het midden).
- [ ] Air-specifieke voyage-snelheid/`ktPerShipment` (nu ship-tempo uit `config.time`).
- [ ] Eigen CB voor Oezbekistan/Kazachstan; evt. meer mijn-/consumptie-nodes (Lars: "extra nodes kan altijd").

## M7 · Koper ✅ uitgevoerd (2026-07-14) — LAR-404 t/m 409
`data/copper.js` van "basis" (13/5) → volledig **uitgewerkt** (69 nodes / 50 flows / 5 tensions, goud-niveau).
- [x] Andes-concentraat-trechter (Escondida/Collahuasi/Cerro Verde/Antamina/Las Bambas → Chinese smelters over de Stille Oceaan, `stage: erts`) = de koper-"aha".
- [x] Copperbelt-**kathode** (Tenke/Kolwezi/Kansanshi/Kamoa, SX-EW `stage: raffinaat`) over land via `grens-kasumbalesa` → Durban/Dar/Lobito/Walvis, dan per schip (kobalt-patroon: land-flow mijn→haven + aparte ship-flow haven→markt).
- [x] Concentraat vs. SX-EW-kathode via `stage`; recycling **always-on** (niet achter de toggle).
- [x] **Beursvoorraden-laag** (LAR-408): optionele toggle `type:"exchange"`/`layer:"exchange"` (LME/SHFE/COMEX), default uit — zelfde patroon als de goud-CB-laag; chip "beursvoorraden", koperkleurige spoel-marker (grootte ∝ √voorraad).
- [x] Verificatie headless (LAR-409): koper **145 legs / 0 kapot**; regressie **388 legs / 0 kapot** over alle 10 grondstoffen; toggle +6 nodes/+7 flows; geen console-errors. 4 route-bugs onderweg gefixt (markt-kustpunten + Korea→Japan als ship + beursmagazijnen coastal). `build-standalone.py` (checks + koper) → `atlas-standalone.html` geregenereerd.

**Open (M7 afronden, niet-code):**
- [ ] **Visuele bevestiging op Netlify/mobiel** — alleen Lars (WebGL-screenshot lukt niet headless). Checken: Andes→China-concentraatbundel, Copperbelt-kathode over land, beursvoorraden-toggle + spoel-markers, scheeps-voyages voor koper. (= laatste open stuk van LAR-409.)
- [x] **Code-commit** — gecommit op `main` (lokaal-only): code `233b882` + wrapup-docs `7e46092` (twee aparte commits, Claude-trailer).
- [x] **Linear** LAR-404 t/m 409 → Done (via Linear-MCP).

**Herbruikbaar uit M6+M7:** de optionele-laag-toggle (CB bij goud, beursvoorraden bij koper) is een vast, herbruikbaar
`layer:"..."`-filterpatroon (vier filterplekken + config-size + ui-chip + marker-vorm); het landcorridor-patroon
(Kasumbalesa) = land-flow mijn→haven + aparte ship-flow. **Elke ship-leg moet op een kustpunt (`port`/`coastal`/`wp-`) landen.**

## M9 · Uranium ✅ uitgevoerd (2026-07-15) — LAR-410 t/m 415
`data/uranium.js` van "basis" (9/2) → volledig **uitgewerkt** (38 nodes / 36 flows / 6 tensions). Eerste grondstof met een
bewust *andere vorm*: een **4-staps kernbrandstofketen** (winning → conversie → verrijking → splijtstof → reactor), gemapt
op de 3 bestaande stages, met de **verrijking (~44% Rusland) als `raffinaat`-flessenhals**.
- [x] Ontwerp-skelet `design/uranium.md` (LAR-410/411 research) + commit `d016ab8`.
- [x] **Kaspische oversteek + Dardanellen** (LAR-412): 3 vaarpunten (`wp-kaspisch-n/-m/-z`) + `wp-dardanellen` in `_chokepoints.js` — forceren de Aktau↔Bakoe-watercorridor (ingesloten zee) + de Zwarte-Zee-uitgang. Alleen uranium gebruikt ze.
- [x] `data/uranium.js` (LAR-413): 4-staps keten + Trans-Kaspische route (om Rusland heen) + VVER-lock-in + CANDU-uitzondering. Commit `76c0333`.
- [x] Verificatie headless (LAR-415, deel): uranium **54 legs / 0 kapot** (20 zee + 34 land, 0 straight → de Kaspische oversteek routeert écht over water); regressievrij (5 nulls = bekende `degDist:0` baseline-hops); structuurcheck groen.

**Open (M9 afronden):**
- [ ] **Visuele bevestiging op Netlify/mobiel** (LAR-415, In Progress) — alleen Lars (WebGL-screenshot lukt niet headless). Checken: verrijkings-flessenhals (dun ringetje nodes, Rusland dikst), de twee Kazachstan-routes, de VVER-lock-in-lijn, de CANDU-uitzondering, scheeps-voyages voor uranium.
- [x] **Militaire-kringloop-toggle** (LAR-414, **Done** — commit `6a6d062`, 2026-07-15) — de uitgestelde backlog-toggle afgemaakt zodra de engine-bestanden schoon waren. Het **vijfde** optionele-laag-patroon (`type:"military"`/`layer:"secondary"`/`showMilitary`), exact het olie-reserve-patroon in 5 plekken. 4 military-nodes (down-blend Rosatom/HEU, tails, US DOE, US reserve) + 5 `secondary`-flows (o.a. Megatons-to-Megawatts Rusland→VS) + tension `u-t-military`. Headless: uranium 60 legs / 0 kapot / 0 straight; toggle uit→aan +4/+5; chip alleen bij uranium.

## Verderop — geen grondstoffen meer op "basis" (atlas inhoudelijk compleet)
**Alle 11 uitgewerkt** (lithium, kobalt, goud, koper, uranium, REE, nikkel, olie, PGM, zilver, grafiet). Het brief→bouw-
runbook (sectie I) is voor alle basis-10 + zilver doorlopen. Toekomstig grondstof-werk = alleen nog een *nieuwe 12e+*
grondstof (zoals zilver een nieuw bestand + script-tag + build-check vergt), niet meer een basis→uitgewerkt-upgrade.

**Nog open (niet-inhoudelijk):**
- [ ] **Visuele bevestigingen per milestone** (Lars, In Progress): LAR-415 (uranium), 421 (REE), 427 (nikkel), 433 (olie),
      439 (zilver), 445 (PGM), 454 (grafiet). Nu triviaal via de live GitHub-Pages-URL.
- [ ] **PGM-backlog-afwijkingen:** LAR-447 (recycle-chip-tooltip generiek maken — nu REE-bewoord in de gedeelde `ui.js`,
      raakt nu óók grafiet), LAR-448 (optionele Pt/Pd-exchange-laag — pure data).
- [ ] Bureaublad-originelen opruimen (`atlas-lithium-kobalt.html` + `globe-oud`) ná visuele bevestiging.

**Repo-status (gecorrigeerd 2026-07-15):** de repo is **niet** lokaal-only — hij staat op GitHub (`larswalters/grondstoffen-atlas`)
en draait **live op GitHub Pages** (https://larswalters.github.io/grondstoffen-atlas/); **elke `git push origin main` deployt**.
`atlas-standalone.html` blijft gitignored (gegenereerd). De "lokaal-only"-notities in oudere milestones zijn achterhaald.
