# Routebrief (licht) · olie — Hardisty (Alberta, Canada) → Steele City (Nebraska) → Cushing (Oklahoma, VS)

**stroom-id:** `olie-hardisty-cushing` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken (2026-09-28)
**Keten in één zin:** Canadese oliezandcrude vanaf de Hardisty-tankopslaghub (Alberta) per **pijpleiding** —
de Keystone-hoofdleiding (Fase 1, via Saskatchewan → Manitoba → Noord-Dakota → Zuid-Dakota → Nebraska) tot
het Steele City-knooppunt, en vandaar de **Keystone-Cushing Extension** (Fase 2, via Kansas) — naar de
Cushing-opslag-/handelshub in Oklahoma, de WTI-prijsbenchmarkknoop.
**Welke as van het verhaal:** het Noord-Amerikaanse **binnenlandse** pijpleidingnet — vult het Midwest/
inland-net aan dat `olie-westridge-ulsan` (kustexport via Vancouver) niet dekt. Jaarvolume: mainline-
capaciteit ≥590 kb/d (2013-cijfer, twee onafhankelijke Wikipedia-pagina's); South Bow (eigenaar sinds
okt. 2024) meldt in 2026 een open season voor ~450 kb/d extra vaste capaciteit Hardisty→Cushing/Golfkust
(Prairie Connector Project) — recentere totale systeemcapaciteit niet dit keer apart bevestigd.

## 1 · Ketenkaart
```
Hardisty-tankopslaghub `ol-hardisty-terminal` (Alberta, Canada)
  ──(b1 leiding · Keystone-hoofdleiding Fase 1, via Saskatchewan → Manitoba → Noord-Dakota →
      Zuid-Dakota → Nebraska · ordegrootte ~2.150 km, niet apart bevestigd)──►
   Steele City-knooppunt (Nebraska, 40.0369/-97.0231 — vaste splitsing Keystone-hoofdlijn:
   been B hieronder vs. Wood River/Patoka IL, buiten deze keten; geen overslag, geen anker)
  ──(b2 leiding · Keystone-Cushing Extension Fase 2, via Kansas · 468 km [Wikipedia])──►
   Cushing-oliehub `ol-cushing-hub` (Payne County, Oklahoma) ── stoppunt (opslag-/handelsknoop)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Hardisty-terminal → Steele City-knooppunt | Keystone-hoofdleiding (Fase 1), via Saskatchewan → Manitoba → Noord-Dakota → Zuid-Dakota → Nebraska | ordegrootte ~2.150 km [ontwerp-schatting]; Wikipedia geeft alleen fase-1-totaal Hardisty→Patoka IL (3.456 km [1]) en de Canadese deelsom (1.237 km [1]), geen apart Hardisty–Steele City-cijfer; eigen grootcirkel Hardisty↔Steele City = 1.768 km — niet dit keer op een exacte deeltraject-bron bevestigd | OSM-pipeline ("Keystone Pipeline", pyosmium/Overpass bij bake) | onbekend — bij bake bepalen; toets meldt hoge verwachte OSM-dekking in alle vijf extracts |
| b2 | B | leiding | Steele City-knooppunt → Cushing-oliehub | Keystone-Cushing Extension (Fase 2), via Kansas | 468 km (291 mi) [Wikipedia, Route-sectie: gebouwd 2010, operationeel feb. 2011][1] | OSM-pipeline ("Keystone Pipeline", pyosmium/Overpass bij bake) | onbekend — bij bake bepalen |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-hardisty-terminal` | kop van de leiding / tankopslaghub | Hardisty-tankopslaghub (Keystone-corridor, multi-operator tankenparkgebied) | 52.6437, -111.2800 | [1][2][6][7] | bron-gelegd (z17 gezien: tankbatterij van zes ronde tanks in een 2×3-opstelling met verbindend leidingnet, direct langs een pijplijn-/spoorcorridor net ten zuiden van het dorp Hardisty, met meerdere aangrenzende tankenparken van andere operators in dezelfde hub — exacte perceelsgrens van het Keystone-tankenpark niet los te onderscheiden op dit beeld) |
| `ol-cushing-hub` | losplek / opslag-handelsknoop (stoppunt) | Cushing-oliehub (WTI-leverpunt, "Pipeline Crossroads of the World") | 35.9472, -96.7565 | [3][4][7] | bron-gelegd (z16 gezien: aaneengesloten complex van tientallen ronde olietanks in rijen en clusters, zuidwest van downtown Cushing — exact het gebied dat de bron beschrijft als de Cushing-tankenparken; het perceel van één specifieke operator (Magellan/Plains/Enbridge/Energy Transfer) is op dit beeld niet te onderscheiden) |

## 4 · Via-punten
*Geen corridorkeuze op beide benen — een pijpleiding volgt een vaste, al aangelegde buis (geen alternatieve
route zoals bij een weg/spoorbeen). Eén informatief punt voor de bake-agent, geen anker en geen via-punt in
de zin van §4-methodiek:*

| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1/b2-grens | — | Steele City-knooppunt | 40.0369, -97.0231 | vaste fysieke splitsing van de Keystone-hoofdlijn (Wikipedia [1][5]): hier gaat de hoofdlijn door naar Wood River/Patoka (IL, buiten deze keten) en takt de Keystone-Cushing Extension af naar Cushing — de grens tussen been A en been B, geen corridorkeuze |

## 5 · Verwerkingsknopen
*Geen aparte verwerkingsknoop — Cushing is zelf de opslag-/handelsknoop en tevens het stoppunt (§6); geen
tussenliggende raffinaderij of smelter op deze twee benen.*

## 6 · Stoppunt
De brief stopt bij de Cushing-oliehub: Cushing is bewust een **opslag-/handelsknoop zonder één vaste
eindraffinaderij** (zelfde patroon als `olie-tengiz-novorossiysk`) — geen bron koppelt deze specifieke
Hardisty-lading aan één met naam genoemde raffinaderij. Vanaf Cushing loopt de crude via afzonderlijke
leidingen verder (Fase 3a MarketLink naar Nederland/Port Arthur TX, Fase 3b Houston Lateral, en talrijke
andere Cushing-pijpleidingen [4]) — dat valt buiten deze as en kan in een latere ronde een eigen
vervolgketen worden. Fase C/D/E vervallen: geen bron noemt een specifieke eindafnemer voor déze lading.

## 7 · Open punten
- **Geen apart gepubliceerd kilometercijfer voor het Hardisty→Steele City-deeltraject.** Wikipedia geeft
  alleen het totaal van Fase 1 tot Patoka, Illinois (3.456 km) en de Canadese deelsom (1.237 km); de
  ~2.150 km uit het ontwerp is een ordegrootte-schatting, niet onafhankelijk bevestigd op een exacte
  deeltraject-bron. Eigen grootcirkelcontrole (1.768 km) ligt lager — het verschil past bij een tracé dat
  via Saskatchewan én Manitoba loopt (niet in een rechte lijn naar Steele City), maar is niet gemeten.
- **Recentere systeemcapaciteit niet apart bevestigd.** South Bow (eigenaar sinds okt. 2024) meldt in 2026
  een open season voor ~450 kb/d nieuwe vaste capaciteit Hardisty→Cushing/Golfkust (Prairie Connector
  Project) [6] — dit bevestigt dat het systeem actief uitbreidt, maar geen bron uit deze ronde geeft de
  huidige totale mainline-capaciteit als opvolger van het 2013-cijfer (590 kb/d).
- **OSM-dekking van de pijpleiding niet dit keer met Overpass geverifieerd** (publieke mirrors onbereikbaar
  vanaf deze sessie) — de haalbaarheidstoets schat een hoge kans op complete dekking in alle vijf
  extracts (Canada, us-north-dakota, us-south-dakota, us-nebraska, us-kansas, us-oklahoma); te bevestigen
  bij bake met een lokale pyosmium-scan (zoals bij `olie-habshan-chiba`, waar dit zonder Overpass lukte).
- **Exacte perceelsgrenzen van de Keystone-specifieke tankenparken bij Hardisty en Cushing** niet te
  onderscheiden van naburige operators op dit satellietbeeld — beide ankers blijven op hub-/siteniveau.
- **Geen cargo- of afnemersniveau bewijs voorbij Cushing** — bewust, want dat is precies waarom de brief
  bij Cushing stopt (§6).

## 8 · Bronnen
[1] Wikipedia, "Keystone Pipeline" — eigenaar South Bow (sinds okt. 2024, afgesplitst van TC Energy),
Route-sectie: Fase 1 (Hardisty→Steele City-knooppunt→Wood River/Patoka IL) 3.456 km, Canadese deelsom
864+373=1.237 km, Amerikaanse deelsom 2.219 km (via ND/SD/NE/KS/MO/IL); Fase 2 "Keystone-Cushing
pipeline phase" Steele City→Cushing 468 km, gebouwd 2010, operationeel feb. 2011; capaciteit Fase 1+2
590.000 vpd (2013-cijfer). https://en.wikipedia.org/wiki/Keystone_Pipeline
[2] Wikipedia, "Hardisty, Alberta" — coördinaat 52.67506/-111.30344 (dorpscentrum, geen anker), "pivotal
petroleum industry hub", Western Canada Select-handel. https://en.wikipedia.org/wiki/Hardisty,_Alberta
[3] Wikipedia, "Cushing, Oklahoma" — coördinaat 35.97972/-96.76083 (stadscentrum, geen anker), WTI-
leverpunt, "Pipeline Crossroads of the World". https://en.wikipedia.org/wiki/Cushing,_Oklahoma
[4] Wikipedia, "Oil industry in Cushing, Oklahoma" — tankopslag ~91 mln vaten totale capaciteit,
tankparkeigenaren (Magellan/Enbridge/Enterprise/Plains/Energy Transfer), Keystone-pijpleiding "operated
by TransCanada, flows from Hardisty, Alberta... to an intermediary hub in Cushing to Port Arthur, Texas.
Maximum capacity of 590,000 barrels per day". https://en.wikipedia.org/wiki/Oil_industry_in_Cushing,_Oklahoma
[5] Wikipedia, "Steele City, Nebraska" — coördinaat 40.03694/-97.02306 (dorpscentrum), Jefferson County,
bevolking 47 (census 2020). https://en.wikipedia.org/wiki/Steele_City,_Nebraska
[6] South Bow (huidige eigenaar/operator, officiële pagina) — systeemlengte 4.327 km (Hardisty–Cushing–
Houston/Port Arthur totaal), terminals te Hardisty AB/Cushing OK/Houston-Port Arthur TX, 3,9+ mrd vaten
vervoerd sinds 2010; 2026 open season "Prairie Connector Project" ~450.000 vpd nieuwe capaciteit
Hardisty→Cushing/Golfkust. https://www.southbow.com/operations/keystone-pipeline-system
[7] Esri World Imagery via `v2/tools/sat_check.py` (z13/z16/z17) —
`sat-olie-hardisty-cushing-hardisty-wide.png`, `sat-olie-hardisty-cushing-hardisty-tanks1.png`,
`sat-olie-hardisty-cushing-hardisty-terminal.png` (anker Hardisty), `sat-olie-hardisty-cushing-cushing-wide.png`,
`sat-olie-hardisty-cushing-cushing-tanks1.png` (anker Cushing).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Stroom `olie-hardisty-cushing`** → `v2/data/stroomroute-olie-hardisty-cushing.json` — 7 benen, **2.744,5 km**,
3.171 punten, 2 markers (1 stippel been). Recept: `bak_stromen.sh` (functie `bak_olie_hardisty_cushing`).
Nieuw gereedschap: `v2/tools/maak_leidingbeen_keystone.py` (pyosmium-scan per Geofabrik-extract op
`man_made=pipeline` met naam~"keystone", component-graaf op gedeelde OSM-nodes, plus een `--knip`-optie om een
component op een interior-punt in twee helften te splitsen).

**⚠️ GEEN kaarteringsgaten — beter dan de brief verwachtte (§7).** Zes extracts gescand (canada · us-north-
dakota · us-south-dakota · us-nebraska · us-kansas · us-oklahoma); elke land-/staatsgrens wordt overgestoken
door een **way die Geofabrik heel in beide buur-extracts opneemt** (dezelfde OSM-node-refs, dus bevestigd met
`osmium` op exact dezelfde 43/82/213 punten in beide bestanden): Canada/Noord-Dakota op way/627805181
(49,06759/-98,00642), Noord-Dakota/Zuid-Dakota op way/138279021 (45,95288/-97,90692), Zuid-Dakota/Nebraska op
way/138364295 (42,63538/-97,33771), en de Kansas/Oklahoma-overlap op way/166440274 (37,36092/-97,05471). Elke
grens is daardoor **geen stippel maar een knip** in een dubbel-gebakken segment: de ene extract-helft wordt tot
het gedeelde punt gebruikt, de andere ná — zo blijft de km-som eenmalig geteld (niet verdubbeld, geen gat).

**b1 (leiding, 4 been-geojson-segmenten, Hardisty → Steele City):**
- segment 1 Hardisty-terminal → Canada/Noord-Dakota-grens: **1.225,1 km**, 1.151 punten — één doorlopend
  OSM-component over heel Alberta+Saskatchewan+Manitoba (edge-som vóór het knippen 1.264,5 km; 39,4 km
  bij de grens weggeknipt om dubbeltelling met segment 2 te voorkomen).
- segment 2 Canada/Noord-Dakota-grens → Noord-Dakota/Zuid-Dakota-grens: **357,0 km**, 436 punten (Noord-Dakota-
  component 432,2 km vóór het knippen; 75,3 km aan de zuidkant afgeknipt, want die 75,3 km is exact
  way/138279021 en telt al mee in segment 3).
- segment 3 Noord-Dakota/Zuid-Dakota-grens → Zuid-Dakota/Nebraska-grens: **383,5 km**, 339 punten — het volledige
  Zuid-Dakota-component, ongeknipt.
- segment 4 Zuid-Dakota/Nebraska-grens → Steele City-knooppunt: **297,5 km**, 315 punten (Nebraska-component
  374,96 km vóór het knippen; 77,4 km aan de noordkant afgeknipt, al geteld in segment 3).

⚠️ **Lengtetoets b1:** 1.225,1+357,0+383,5+297,5 = **2.263,1 km** tegen de brief-schatting "ordegrootte
~2.150 km" (niet onafhankelijk bevestigd, §7) = **+5,3%**. Ruim binnen de marge die de brief zelf toestaat voor
een ordegrootte-schatting. Eigen grootcirkel Hardisty↔Steele City uit de brief was 1.768 km; de gemeten
pijpleidingroute is 28,0% langer, consistent met een tracé dat via Saskatchewan én Manitoba omslingert i.p.v.
recht naar het zuidoosten te lopen.

**⚠️ Bewuste uitsluiting bij Steele City (brief §1, informatief punt):** in OSM splitst de naam "Keystone
Pipeline" bij Steele City in twee takken — de hoofdlijn door naar Wood River/Patoka (Illinois, way/468901503
e.a., component met uiteinde 39,67200/-94,86878, gevonden in zowel de Nebraska- als de Kansas-extract) en de
Cushing Extension. De Wood River-tak is **niet gebruikt**: die hoort bij een andere, hier niet gebakken keten
(brief §1, "buiten deze keten"). b1 eindigt daarom op een Nebraska-eigen punt (40,03920/-96,99993, 1,99 km van
het Steele City-referentiepunt 40,0369/-97,0231); b2 begint op een apart Kansas-punt 150 m verderop
(40,03786/-96,99986) — de kleine naad daartussen (zie hieronder) is de fysieke splitsing van de twee takken,
geen meetfout.

**b2 (leiding, 2 been-geojson-segmenten, Steele City → Cushing):**
- segment 1 Steele City-knooppunt → knooppunt 37,36092/-97,05471 (Kansas): **302,6 km**, 532 punten
  (Kansas-component 389,83 km vóór het knippen; 87,2 km aan de zuidkant afgeknipt, al geteld in segment 2).
- segment 2 knooppunt 37,36092/-97,05471 → Cushing-oliehub (Oklahoma): **176,5 km**, 396 punten — het
  Oklahoma-component dat al vanaf de grens tot bijna aan de Cushing-hub doorloopt, ongeknipt.

⚠️ **Lengtetoets b2:** 302,6+176,5 = **479,1 km** tegen 468 km [Wikipedia, sterke bron] = **+2,4%**, ruim binnen
de ±15%-norm die hier als echte norm geldt (brief §2). De Oklahoma-extract had een tweede, groter component
(301,7 km, naar 33,52/-95,64 in Zuid-Oklahoma) — dat is Fase 3/MarketLink verder stroomafwaarts van Cushing,
buiten deze keten (brief §6) — bewust niet gebruikt.

**Naad b1→b2 (Steele City):** 149 m tussen segment 4 (Nebraska-eind, 40,03920/-96,99993) en b2-segment 1
(Kansas-begin, 40,03786/-96,99986) — ruim binnen de 5 km-norm, en zoals boven uitgelegd de fysieke afstand
tussen de twee OSM-takken bij de junctie, geen procesgat.

**Cushing-hub last mile (stippel):** de pijpleiding (b2-segment 2) eindigt op 35,92671/-96,75128, **2,33 km**
van het `ol-cushing-hub`-ankerpunt (35,9472/-96,7565) — net over de ~2 km-richtlijn voor "geen last-mile-benen",
dus als korte stippel getekend ("geen net op deze korrel"), **2,3 km**, geen verzonnen coördinaat.
**Hardisty-kant:** het leidingbegin (52,64627/-111,26543) ligt al op **1,02 km** van het ankerpunt (52,6437/
-111,2800) — ruim binnen de 2 km-marge, dus geen extra stippel (anker ≠ routeerpunt, zoals elders in de atlas).

**Markers:** `ol-hardisty-terminal` (kop, 1,02 km van het routeerpunt) · `ol-cushing-hub` (stoppunt, 2,33 km van
het routeerpunt, gedekt door de last-mile-stippel). Steele City draagt bewust geen marker (informatief
splitsingspunt, geen overslag — geen modaliteitswissel).

**Toets:** `toets_knikken.py` — 43 knikken ≥60°, waarvan **0 omkeringen ≥150° en 0 terugloop** (de enige klasse
die reparatie verdient); de knikken zijn OSM-waysegmentgrenzen/valve-station-spikes in de bronleiding zelf
(vergelijkbaar met olie-habshan-chiba), geen routeerfout — er wordt hier immers niets geroutet.
`toets_rechte_benen.py --min-km 5` — geen bevindingen voor deze stroom (geen been ≥5 km met omwegfactor 1,000).
json geldig: versie 2, punt_formaat lonlat, modaliteit uitsluitend `leiding` (toegestane set), elk been ≥2
punten (1.151/436/339/315/532/396/2), bestandsgrootte **66,8 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- Een grensoverschrijdende OSM-way wordt door Geofabrik **heel** in beide buur-extracts opgenomen, met
  identieke node-refs — dat maakt een grens een knip-op-gedeeld-punt in plaats van een stippel-met-reden, en
  het is met `osmium` in enkele seconden te bevestigen (zelfde node-ref, zelfde coördinaten tot 7 decimalen).
- Zonder die knip-stap zou de km-som van elke grens dubbel geteld zijn (of, bij een verkeerde helft, een gat
  ontstaan waar er geen is) — een dubbel-gebakken segment is een aparte foutklasse naast het bekende
  kaarteringsgat, en verdient een eigen check (osmium-scan op gedeelde way-ids tussen twee buur-extracts)
  vóórdat een "gat" wordt gerapporteerd.
- Bij een naam-tag die bij een fysieke splitsing (Steele City) in twee takken uiteenvalt, moet de niet-bedoelde
  tak eerst herkend worden aan zijn richting/bestemming (Wood River/Illinois, oostwaarts) vóórdat hij wordt
  uitgesloten — een blinde naamfilter alleen was hier niet genoeg, de brief (§1) was wel genoeg.
