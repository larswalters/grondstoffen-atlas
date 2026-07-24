# Session summaries — Grondstoffen Atlas
*Newest first.*

## 2026-07-24 - Industrieel last-mile-spoor geheeld, live ?v=072
Vervolg op de heal-ronde: is er meer spoor/riviergraaf dat we missen? Twee detectoren gebouwd
i.p.v. één handmatige reparatie. `toets_stromen_14.mjs` (per grondstof één teststroom, havenniveau):
het riviernet is solide — 10 riviersstromen (diepe Yangtze→Chongqing, Mississippi, Seaway, Donau,
Rijn) routeren 0 gaten, geen Manaus/Tongling-siblings. `toets_spoor_aansluiting.mjs` (579
industriële nodes): VERBONDEN 258 · LANGE SPUR 180 · GEEN SPOOR 119 · **AFGEKNIPT 22** (siding
≤3 km bij de plant, los van het net). **Wortel:** het M25-filter dropt álle `service=`-rail — juist
de siding/spur die een smelter aan de hoofdlijn knoopt (china-extract Tongling: `service=spur`
0,9 km + 89× `service=yard`). **Lars had gelijk** (*"je ziet ze gewoon liggen op de kaart"*): OSM
tekende de ways maar knoopte de junctie-knopen niet — de smelter hangt via een 107 m-gaatje aan een
179 km-net, dat via 16 m aan het volgende (de LAR-520-klasse). **Fix:** `fetch_service_lastmile.py`
sluit `service=spur/siding/yard` binnen 7 km van de aansluitingen in (globaal insluiten blies M25
+22% op → alléén lokaal); `bake_landnet` heelt transitief vertex-op-vertex (smelter→179 km→hoofdnet,
≤200 m, bestaande-vertex-connectoren + herbake); `drop_onverbonden` gooit onverbonden rail weg +
ruimt wees-knopen op. **Twee bugs onderweg (beide Cerrejón→Bolívar-regressie):** edge-split gaf een
hoofdlijn-splithelft het spoor-heal-label → drop wierp het weg; en de drop liet wees-knopen achter
→ Bolívar snapte op een 0 km-wees. Opgelost via vertex-connectoren + wees-opruiming. **Resultaat:**
Tongling/Beilun/Guixi/Duisburg aan het hoofdnet, uitgaand kathode-per-trein over de échte siding;
toets_routes 30/30, marnet/ports byte-identiek, grootste 664.151→671.829 km. Live `?v=072`
(commit `6266aba`), Lars' visuele go: *"mooi tot in de haven en bij de grote fabrieken een lijntje
aangesloten op het grote net, zo moet het."* Open: 22 grove AFGEKNIPT-sites = aparte bredere uitrol.

## 2026-07-24 - De heal-ronde: de pijplijn verbreekt niets meer, live ?v=071
Diagnose eerst (meet-workflow, 8 agents incl. tegenspraak): een raw-experiment op de OSM-topologie
bewees dat de bron op elk breukpunt al verbonden was — Antwerpen-Duisburg en Beilun-Guixi zijn ook
onder ons service-filter een component. De breuken waren dus eigen maaksel. Drie fixes:

1. **De heal VERLENGT een uiteinde i.p.v. het te verplaatsen** (bake_marnet, tier-1 en tier-2).
   Verplaatsen trok samenvallende tweeling-eindpunten los en tier-2 snapte ze terug: de
   EMO-flip-flop (zelfde 15 m-naad zes rondes gelegd en losgetrokken). Nu convergeert de heal;
   Cerrejon->Ruhr 0 gaten (was 1). Bijvangst: R'dam->Cincinnati 11.199 -> 9.591 km via Chicago.
2. **De haven-riviersnap verkiest een doorgaand component (>=100 km), relatief gewogen**
   (hooguit 2x+1 km verder; absolute drempel verworpen — teleporteerde Whitby/Rostock 58 km).
   Manaus van 4-cellen-sliver naar de echte Amazone; Saldanha->Manaus routeert (Macapa, 1.299 km).
3. **Dedup-connectiviteitsguard** (herstel_verbindingen in fetch_landnet): niets wegvouwen dat
   >=2 componenten verbond; terug via het kortste stukkenpad. Wereld: 1.185 stukken / 3.468 km
   terug (0,3%) -> componenten 3.140 -> 638, grootste 402.845 -> 664.313 km. Beilun-Guixi rijdt
   (trein 883 km), Antwerpen-Duisburg een component (EU 96%).

Gemeten en verworpen: snipper 0,30->0,15 alleen maakt het NIET beter (grootste component kromp).
toets_routes 30/30 (verwachtingen mee: cerrejon 1->0, escondida 2->1, Cincinnati->Chicago, Manaus
gepind); zee-invarianten exact (19.610 / 89; zee-snaps byte-identiek). Commit 0eaff4b, ?v=071.
Open: Tongling-vlecht (brongeometrie), Escondida-leiding onbekend, echte OSM-gaten Krefeld/Kempen.

## 2026-07-23 - M26.1: de stromen op straatniveau, live ?v=065
Vier werkelijke stromen staan been voor been op de bol, twee grondstoffen. Nieuwe entiteit: de
**aansluiting per grondstof** (`v2/data/aansluitingen.json`, 15 stuks, coordinaten uit OSM/ODbL via
de nieuwe scout `v2/tools/verken_terminals.py`, gemeten door `maak_aansluitingen.py`).
`knooppunten.json` heeft een aanhechting per modaliteit voor alle lading en kan op straatniveau
geen twee lijnen in dezelfde havenmond dragen.

- **Collahuasi -> Tongling** 19.406 km, 0 gaten, 2x overslag (leiding -> zee -> Yangtze)
- **Escondida -> Guixi** 19.239 km, 2 gaten (leiding onbekend + treinbeen zonder pad)
- **Lobito -> Duisburg** 9.946 km, **0 gaten** - de eerste keten die volledig doorloopt
- **Cerrejon -> Ruhr** 8.377 km, 1 gat; spoorbeen 146 km over Cerrejons eigen kolenlijn (~150
  gepubliceerd), zee 8.231, Rijnbeen faalt

**De premisse is gemeten, niet beweerd:** Waalhaven hecht op binnenknoop 40927, EMO op 40904 - 30 km
uit elkaar, dus koper en kolen komen echt op verschillende plekken de Rijn op. Duisburg idem:
kathode naar Ruhrort (Becken A), cokeskool 7 km noordelijker naar de Schwelgern-pier bij
ThyssenKrupp. Aansluitingen maken **geen overstap** aan, dus de zoekruimte beweegt niet
(R'dam-Shanghai 19.610 / 89 overstappen, getoetst voor en na).

**Besluit van Lars dat een indeling van mij corrigeerde:** een NET is productonafhankelijk, een
EIGEN VERBINDING niet. Een slurryleiding vervoert een product tussen twee punten en levert als graaf
niets op - dus geen net, en daarmee ook **geen gat**. Drie categorieen: `ok` / `eigen` / `onbekend`.
Gevolg: gestippeld betekent voortaan uitsluitend "geraden", doorgetrokken "we weten waar hij ligt".

**Vier gaten gevonden door te routeren** (Lars' werkregel): Beilun-havenspoor los van het Chinese
hoofdnet (1.823 vs 402.762 km) - EMO-kade op een losstaand havenbekken van 4 km, terwijl koper 30 km
verderop wel doorloopt - zeenet grof langs Chili (78-85 km last mile) - de via-havens in `data/*.js`
te grofkorrelig (Antofagasta i.p.v. Patache, Yangshan i.p.v. rivierkade, Guixi 3,8 km mis).

**Vijf fouten van mij, alle door Lars' oog gevonden, drie met een wortel: maten als vaste fractie
van de bolstraal.** Markers 19,1 km met depthTest:false; lijnen zwevend op 3,8-10,2 km (parallax);
geel op de Atacama onleesbaar. Plus: snoeien op knoopniveau doet per definitie niets - de
overvaar-lus zit in de lijngeometrie tussen knopen (nu per vertex: Shanghai 10,7 -> 4,5 km). En de
pijpleiding werd gezaaid op een vertex middenin zichzelf, waardoor hij uit het niets begon; zaaien
op graad-1-uiteinden gaf 186,5 -> 192,4 km en -6,8% -> -3,8%.

**De slurryleiding ligt erop** (`fetch_pijpleidingen.py`): Collahuasi->Patache gestikt uit 14
OSM-ways met `substance=slurry`, 1.363 punten. 7 van de 14 ways dragen tegelijk `highway=track` +
`surface=dirt` - de pijp ligt begraven onder zijn eigen onderhoudsweg, en dat is de zandweg die Lars
op de satellietfoto zag: de beste bevestiging dat het tracee klopt. Escondida->Coloso lukt niet
(nul `substance=slurry`; geen van de 76 pijpleidingen komt dichter dan 16,5 km bij Coloso) -> blijft
een rechte stippellijn met die reden. Nagerekend: `Canaleta de Relaves` (tailings) zit met 0/283
punten niet in ons pad.

**Collahuasi's eigen video** gaf de keten na de leiding bij Puerto Patache: espesadores ->
planta de molibdeno -> planta de filtro -> stockpile -> embarque. Daarmee bevestigd dat de twee
ronde tanks die Lars aanwees de indikkers zijn, en dus het echte uitmondingspunt. Bewust niet
gemodelleerd ("we laten het hierbij, verfijnen kan later").

**Bijvangst-besluit:** bake-versie losgekoppeld van codeversie - data meebumpen zonder rebake kostte
elke bezoeker ~14 MB bit-identieke binaries. `toets_routes.mjs` 15/15 -> **30/30 groen**; de
verwachte gaten per stroom staan in de test met hun reden (omlaag = vooruitgang, omhoog = regressie).

Commits: `d5b2204` (pilot) - `d8e86fd` (schermgebonden maten + snoeien) - `0f4ba0b` (twee stromen
erbij) - `5bc5997` (slurryleiding) - `4d1581e` (net vs eigen verbinding) - `17b5ac2` (zaaien op
uiteinde) - `34f7a3a` (ongekarteerd laatste stuk gestippeld). Alle gepusht, live op Pages.

## 2026-07-23 — Het koppelen: de keten-router over álle vier de netten (LAR-518), live ?v=058
De vier netten (zee · binnenwater · spoor · weg) gekoppeld via een aangewezen register
(`v2/data/knooppunten.json`, 49 overslagpunten met coördinaat per modaliteit + expliciet knopenpaar
per overstap; `maak_knooppunten.py` meet de snap) en een keten-router (`zoekKeten`): een been mengt
nooit netten, overstap = toestandssprong op een aangewezen punt (+1 laag), **lexicografisch minste
overslagen → minste km** (het slot op de Donau-ring). `router.js` losgemaakt van three zodat de
**eerste uitvoerbare test van de repo** (`toets_routes.mjs`, 15/15 groen) exact dezelfde code draait
als de browser; bounds-assert op de heap. Drie bugronden, elk gevonden door te routeren: (1) een
niet-aangewezen haven zaait op zijn **dichtste** net i.p.v. beide (Karlsruhe tekende anders een
zeeschip dat 360 km landinwaarts begon → de lijn stopte in zee); (2) het **spoornet was nergens in
gebruik** doordat register-punten op **rangeersporen** snapten (hoofdnet 5 km verderop) → hoofdlijn-
snap (component-drempel spoor 1.000 / weg 30 km, cap 60 km) → Shanghai→Chongqing = trein 2.299 km;
knop *spoor+weg meenemen* + ◆-knooppunten kiesbaar; (3) HUD op mobiel buiten beeld → scrollbaar +
inklapbaar. Echt gat: **EU-spoor gefragmenteerd** (Antwerpen↔Duisburg op losse componenten). Zee-
invarianten onveranderd (19.610 / 8.031); marnet/ports/landnet-bins onaangeraakt. Lars: *"ziet er al
redelijk goed uit."* Volgende = de stromen routeren (M26).

## 2026-07-22 · Vier netten op de bol — en de vectorlaag die niemand kon zien (?v=053)

**TL;DR:** Lars kon het spoornet niet controleren, en dat bleek geen kwestie van kijken: zodra
de satelliettegels geladen waren leverden **alle** vectorlagen 0 pixels. Opgelost, en daarna
liggen de **wegcorridors** erop — 17 corridors, 17.635 km, negen binnen de tolerantie van hun
gepubliceerde lengte. Daarmee vier netten: zee · binnenwater · spoor · weg.

**De onzichtbare vectorlaag.** Gemeten op 1 km hoogte mét tegels: kustlijn 0 (zonder dieptetest
20.057), zeenet+riviernet 0 (84.477), landnet 0 (30.509). De dader is de **bol en alleen de
bol** — bol verbergen gaf 29.368 spoorpixels, `depthWrite: false` 29.308, tegels verbergen 0,
atmosfeer verbergen 0. Hij dekt af terwijl hij 12,7 km ónder de lijnen ligt, wat alleen kan
doordat `logarithmicDepthBuffer` een mesh via `gl_FragDepth` laat schrijven en een
`LineBasicMaterial` niet. Fix: `depthTest: false` + renderOrder boven de tegels + een
`THREE.Plane` op de horizon tegen doorschijnen. Gemeten op 419 km: Frankfurt landnet 64.476
(zonder klem 68.153), Nederland 49.641 (52.942), zeenet 86.034 → 14.262.

**⚠️ Drie meetfouten van mij in één avond.** (1) Mijn pixelmaat telde "pixels met de kleur van
de laag" en werd vertekend doordat een lijn over een lichte satellietfoto vervaagt — de juiste
maat is *hoeveel pixels veranderen als je de laag uitzet*. (2) De eerste fix hing aan een
hoogtedrempel van 1.500 km, buiten het bereik waarop Lars kijkt, dus voor hem veranderde er
niets. (3) Ik heb de horizonklem drie keer "kapot" verklaard terwijl ik boven **open water**
mat — de camera staat standaard op lat 0 / lon 0. Lars' screenshot wees de oorzaak aan: hij
noemde het *"zweven door de lucht en anders draaien"*, en dat is exact de achterkant van de bol
van binnenuit gezien.

**De wegcorridors.** Uit 20 nagelopen definities routeerden er 17. Fresnillo→Torreón −0,2% ·
Kasumbalesa −0,8% · **Copperbelt→Durban 3.068,8 tegen 3.000 (+2,3%)** · Dar es Salaam +2,9% ·
Kemerton −3,1% · Tavan Tolgoi −3,2% · Las Bambas −4,8% · Goulamina +6,9% · Walvis Bay +7,9% ·
Oyu Tolgoi +8,7% · Beira +12,5%. Durban loopt via Kasumbalesa, Chirundu, Harare, Beitbridge en
Johannesburg, elk tussenpunt <110 m van de weg; het anker is Bayhead Road (truck-aanvoer), niet
de kade. De vijf die in ronde 1 faalden wezen zichzelf aan mét coördinaat: drie doordat de
scanvensters uit de definities niet meekwamen, en Mountain Pass met *"punt (−115,1372 / 36,175)
ligt >25 km van elke weg"* — Las Vegas, want `us-nevada` ontbrak in de registry.

**Besloten:** gaten vind je door de stromen te routeren, niet vooraf. Daarom blijven de drie
corridorgaten en de 89 plaatsen op een klein spoorcomponent staan.

**Volgende:** het koppelen — `knooppunten.json` + de keten-router over álle vier de netten.


## 2026-07-22 · De simplify knipte het spoornet door — heal ernà (live ?v=046)

**TL;DR:** op weg naar de wegcorridors bleek het spoornet dat gisteren live ging structureel kapot.
De Douglas-Peucker-simplify in `schrijf_geojson` brak precies de naden open die de heal er net had
ingelegd. Herstel = dezelfde heal nóg een keer, ná de simplify — grootste component
**356.682 → 402.845 km**, roze havens op het wereldnet **23 → 45** van de 200.

**De diagnose, en twee doodlopende sporen die eerst gemeten moesten worden.** Polen met de
bake-regel (de knoopregel die de bake écht gebruikt): zonder simplify 77 componenten / grootste
15.341 km (79,3%), mét de simplify 91 / 8.673 km (45,1%). De twee helften raakten elkaar daarna op
**75 plekken**, waarvan zes binnen 22 m en één op **0,7 meter** — dat is geen geografie. Weerlegd
onderweg: (1) het `service=*`-filter zou het weefsel bij emplacementen slopen → met
`service=spur|siding|crossover|yard` erbij springt de PKP-PLK-ijking van +1,3% naar **+22,1%** en
gaan de componenten *omhoog* (109 → 271); (2) rastermismatch tussen de bescherming (1e-5) en de
knoopcel (`BULK_QUANT`) → beide standen exact 91 componenten / 8.673 km.

**⚠️ En een meetfout van mezelf, want die hoort erbij.** `landnet-aanhecht.json` meet plaats →
dichtstbijzijnde **KNOOP**, en knopen liggen op uiteinden/kruisingen + elke 10 km. Een stub van 1 km
heeft per definitie een knoop vlakbij; een doorgaande hoofdlijn die er rakelings langs loopt kan
zijn dichtstbijzijnde knoop 5 km verderop hebben. Mijn eerste conclusie ("het net valt uit elkaar op
de emplacementen") steunde daarop en was deels artefact — tegen de **lijngeometrie** hermeten
verschoof het oordeel voor 11 van de 497 plaatsen. Zelfde familie als de CEMT-diepgangkolom en de
vaargeul-projectdiepte: een getal dat X beschrijft begrenst Y niet.

**Lars' eis en hoe die is uitgevoerd.** Harde scheiding tussen modaliteiten: alleen rail-rail, alleen
echte gebroken naden, geen kruisingen/viaducten/tunnels zonder gedeelde spoorknoop, nooit
automatisch spoor↔weg/rivier/zee, multimodaal alleen via expliciete overslagnodes, rapporteren per
afstandsklasse. Uitgevoerd als **constructie-eigenschap in plaats van guard**: een naad mag alleen
tussen ketens die vóór de simplify in hetzelfde component zaten en er ná in verschillende, dus de
heal kan per constructie geen verbinding *maken* die de brongeometrie niet had. Plus gelijke
spoorwijdte, richtingsguard 30°, modus-assert. Controle: **0** componenten voegen ketens uit
verschillende pre-simplify-componenten samen. Naden: EU 84 (71 <1 m), CN 38, RU 14, rest 5-8;
**geen naad boven 75 m**. `marnet.bin`/`marnet.json`/`ports.json` sha256-identiek; `-t` byte-identiek.

**De wegcorridorronde.** 105 `mode:"road"`-legs → 24 kandidaten, elk onderzocht en door twee
sceptici aangevallen (74 agents, nul fouten): 8 bouwbaar, 6 stranden op een centroïde, 3 zijn een
andere modus, 6 twijfel — plus **12 corridors die de lijst helemaal miste** (Las Bambas→Pillones,
Tavan Tolgoi→Gashuunsukhait, Oyu Tolgoi, Kathleen Valley, Salar de Atacama, Boké, Mount Weld).
Twee besluiten van Lars corrigeren het bronnenplan: de **tussenpunten worden de acceptatietoets**
(voor weg bestaat geen scheidsrechter; OSRM is OSM-afgeleid en dus dezelfde bron) en het **filter
">150 km" vervalt** (omgekeerd gecorreleerd met wegrelevantie). Derde ontwerpfout: het scanvenster
zou om de grootcirkel liggen, maar Kolwezi→Durban loopt via Lusaka (155 km van die lijn) en Harare
(362 km) — het venster ligt nu om anker → tussenpunten → anker.

**Ook opgeleverd:** de wegmachinerie (`weg_houden()`, corridorvenster, `corridor_keten()` met
Dijkstra per been, `refs` als zachte voorkeur factor 3, `--modus weg` als eigen pijplijn), de
cachevingerafdruk die nu óók het wegfilter en de corridorvensters dekt, en een cache-index-sidecar
nadat elke worker bij een cache-hit het hele scanbestand parseerde voor twee getallen (MemoryError
halverwege een wereldrun).

**Volgende:** corridordefinities afmaken → `CORRIDORS` vullen → routeren → bakken. `us-new-mexico`
ontbreekt en is nodig voor Mountain Pass→Fort Worth.


## 2026-07-22 — M25: het landnet (spoor) op de bol, 1.154.090 km (LIVE ?v=045, visuele go)

**Lars draaide de volgorde om:** *"eerst het spoor en een aantal snelwegen neerleggen en dan pas
met connecten beginnen."* Verkenning + ontwerp via een multi-agent ronde (5 lezers → 4
architecturen → 12 aanvallers → synthese); alle vier kozen onafhankelijk een **eigen bestand**
naast `marnet.bin`.

**Gebouwd:** `audit_landdekking.py` (dekking aan de vraagkant; **79 van 497 plaatsen buiten de
brondata**, waarvan 43 alleen schijnbaar gedekt — een bbox-treffer bewijst niets over de inhoud:
Mongolië ligt in China's bbox) · `fetch_landnet.py` (eigen extract-registry, parallelle scan,
**ketenvouwen**, **dedup**, **heal**, component-snoei) · `bake_landnet.py` · `run_landnet_wereld.py`
· `v2/src/landnet.js` + HUD.

**Resultaat:** 1.154.090 km · 237.944 knopen · 236.728 edges · `landnet.bin` **4,4 MB** (budget 8)
· laden 466 ms · grootste component 356.682 km · 359/497 atlas-plaatsen ≤25 km van het spoor.
Labelverdeling klopt zonder sturing (`na-1435` 264.816 · `ru-1520` 89.677 · `as-1676` 82.755 ·
`af-1067` 44.160); China conventioneel 125.606 tegen 109.767 Wereldbank (+14,4%).

**Dedup GEIJKT op twee meetlatten, tweezijdig:** NL 3.103 tegen ProRail 3.223 (−3,7%) · Polen
19.534 tegen PKP-PLK ~19.300 (+1,2%) · enkelspoor blijft (Zambia −0,4% · Cambodja −0,2%) ·
Sishen–Saldanha 882 tegen 861.

**⚠️ De bake legde zijn eigen fout bloot** doordat hij componenten print: 31.737 componenten met
de grootste op 3.102 km. Oorzaak 1 — de simplify sneed juist de **aanhechtpunten** weg (die liggen
per definitie vlak bij de rechte lijn, dus DP verwijdert ze als eerste). Oorzaak 2 — de dedup liet
**snijranden** achter op ~4 m van de houder. Fix: simplify die knipt op aanhechtpunten + de
riviernet-heal cross-component ≤150 m.

**Besloten:** landbrug — het standaardprofiel sluit `land`, modus per been uit de flows-data ·
extracts uitgebreid met 23 stuks (3,6 GB, niet de geschatte 15-20) in een **eigen registry** ·
eigen bestand met **lokale** knoop-ids (een gebakken offset verloopt stil bij een marnet-rebake).
Guards: marnet/ports sha256-identiek vóór en ná. Commits `3aae346` · `f2cd1b7` · `f2578ed` ·
`d3fae84`. **Volgende: snelwegcorridors, dan koppelen over alle vier de netten.**

## 2026-07-21 (avond) — stap 2 havens: WPI-verrijking + 1.014 posities geschoond (?v=043/?v=044)

**Zelfde sessie als de riviernet-afronding hieronder.** De WPI-blokkade bleek een
user-agent-kwestie: de officiële NGA-API levert 2.951 havens (publiek domein). Nieuw
`v2/tools/fetch_wpi.py`; LOCODE-join in `bak_havens` → `wpiMaat`/`wpiSpoor`/`wpiVracht` (alleen
expliciete Y — WPI zet massaal "U", zelfs Rotterdam; onbekend ≠ geen vracht)/`wpiAfstandKm`/
`posBron`. **Roze = zee + rivier + spoor bevestigd: 200 kandidaten** (Rosario, Zeebrugge,
Santos…); **Saldanha Bay toegevoegd** (het gat in de 15 bulkhavens); NGA-attributie in de HUD.

**Posities** (na Lars: *"roze plekken liggen nog niet accuraat"*): **1.014 havens naar de
haven-georiënteerde WPI-plek** (mediaan 2,6 km) met twee poortwachters — watertoets (nieuwe plek
aan water, anders blijft de centroïde) en naamtoets >200 km (generieke woorden als "puerto"
tellen niet). Terechte megareparaties: **Portland Oregon→Maine 4.083 km**, Everett 3.982,
Crockett 3.415, Yawata 862; **zeven verkeerde LOCODE-identiteiten geweigerd** (Grays
Harbor↔"Greenwich", Penticton↔"Pangnirtung", Puerto Morelos↔"Puerto Morro Redondo"…).
Rivier-snap ≤1 km 167→190 · 27 extra havens door de waterpoort · zeenet ongemoeid.
Commits `d7e5ca4` · `d772477`. **Volgende: stap 3 aansluiten** (knooppunten.json + keten-router).

## 2026-07-21 — riviernet geknoopt: volg het water (bruggen + meer-oversteken; LAR-520 DONE, ?v=042)

**Werkwijze-correctie van Lars** (*"het viel me op dat je vooral veel ging meten en uitrekenen
voordat we iets gingen maken… we willen gewoon een lijntje door heel het rivierennet leggen"*) →
route-test als gap-detector geschrapt (kortste-pad rijdt om een gat heen), en gebouwd:
`v2/tools/knoop_riviernet.py`. (a) **Bruggen:** Dijkstra over óngetagde `waterway=river|canal`-ways
vanaf elk doodlopend uiteinde tot een ander component (OSM deelt de knoop exact waar de tags
knippen); 159 extracts / 70 GB / ~10 min → **1.828 bruggen / 29.961 km** (de Fly 245 km — Lars'
eigen screenshot-rivier; Congobekken 79; GB-kanalen 553). (b) **Meer-oversteek** (`--meren`):
koorde door `natural=water`-vlakken met shapely-`covers`-bewijs → **75 oversteken / 744 km**
(Hongze 48,6 km = het LAR-509-gat, Peipus 67, Mweru 109, Markermeer/IJsselmeer/Zeeland). Guards:
eerst dezelfde heal als de bake, waterval/dam blokkeert, kortste per componentpaar,
zelfde-component per constructie uit.

**Resultaat:** componenten **3.490 → 1.772**; **Ohio-Cairo + Waal-tak dicht via écht water** (de
geplande lengtetoets-naden vervielen); zeenet in elke stap byte-ongemoeid (0 zee↔rivier, -t ==
live); live `?v=041` → `?v=042` (commits `b4ab8c2` · `aecefa1`). **LAR-520 Done na Lars' go**
(*"er ligt nu wel veel in — anders kijken we later of we iets missen als we de stromen
uitwerken"*). Zijn ZH-cirkels (Kaag/Braassem/Westeinder) bleken al één component — de boezem
verbindt om de plassen heen; open aanbod: zelfde-component-koordes door plassen.
**Volgende: stap 2 — havens op de juiste plek** (WPI/posities/Saldanha), dan aansluiten, dan wegen.

## 2026-07-21 — LAR-520 riviernet stitchen: twee-traps over-water heal (LIVE ?v=040)

**Live t/m `f477668` (`?v=040`); LAR-520 blijft In Progress.** Lars' visuele check op mobiel binnen
(net staat verbonden, R'dam→Duisburg berekent 420 km / aanloop 153 km — `de router werkt nog niet`,
verwacht).

**Diagnose eerst** (geen shotgun-naadradius). Nieuw `v2/tools/diagnose_riviernet.py` parset de echte
bake (`marnet.bin`, varint) en reproduceert het overslag-panel **onafhankelijk**: 10.669 componenten,
mediaan 4,80 km, naadradius 2 km→2.551 / 5 km→1.666, Cincinnati 16 km/6 knopen, New Orleans 222 km/26.
De gatverdeling (mediaan uiteinde-gat 0,80 km) toonde dat een uniforme radius het doel niet haalt (10 km
→ nog 1.413) én eerst gevaarlijk wordt. Doel herijkt met Lars: **haven-dragende corridors heel** (maar
749 van de 10.669 dragen een haven). Projectie-analyse wees de oorzaak aan: **gemiste confluenties**
(binnenwaternet knoopt alleen op lijn-uiteinden; 4.067 uiteinden projecteren binnen 100 m op een ander
component).

**Mechanisme** (in `binnenwaternet()`, achter `--heal-km 0.25 --corridor-km 2.0`, default 0 = oud
gedrag, geïtereerd tot convergentie ≤6 rondes): **tier-1** cross-component confluentie-heal (uiteinde →
op de lijn van een ander component, over water per constructie, 4.837 naden ≤250 m; cross-component
sluit de meander-sluipweg per constructie uit); **tier-2** collineaire corridor-heal (uiteinde↔uiteinde
≤2 km mét richtingsguard ≤45°, 2.922 naden).

**Resultaat:** componenten **10.669 → 3.490**; **Mississippi** (New Orleans+Baton Rouge+Memphis,
11.124 km) én **Rijn** (Rotterdam↔Duisburg, 5.220 km) elk één component; **zeenet byte-identiek**
(15.840 zee-edges + 9.633 zeeknoop-coörd. ongewijzigd → 19.610 / 8.031 exact); **0 edges zee↔rivier**
(assert). Veilig gewerkt: naar suffix `-t` gebakken + byte-vergeleken vóór live (deterministisch,
rebake ~30 s dankzij de verzoening-cache). Twee AskUserQuestion-checkpoints (doel + tier-2-guard).

**Nog open (volgende sessie):** de router — `toets_routes.py` (elf invarianten headless, incl.
R'dam→Nijmegen ~172 km over de graaf, verifieert de route-acceptatie pas écht) + `knooppunten.json` +
`zoekKeten`. En de twee angled confluenties **Ohio-Cairo** (2,4 km) + **Waal-tak Nijmegen** (1,4 km)
met de **lengtetoets** (geen bredere radius). Zie `v2/design/overslag-ontwerp.md` §6.

## 2026-07-20 (sessie 38) — ÉÉN binnenwaternet: riviernet in de graaf, amber eruit

**Visuele go van Lars** (*"ziet er goed uit en ik zie de amber lijnen zijn weg"*). Live `?v=036`.

**De bulklaag is hét binnenwaternet geworden**: 374.342 km als 53.922 edges op 64.255 knopen, ín
de routeergraaf, met de maten als eigenschap van de lijn. 7.333 edges dragen een gabariet uit het
OSM-signaal. Acht regio's erbij (Niger, de Fly bij Ok Tedi, Ubangi/Ogooué/Chari, Volta, Mexico) en
de 36 handgemaakte ketens eruit.

**Het riviernet hangt bewust niet aan MARNET** — zee↔rivier gaat via overslag. Dat ruimt het
ankerwerk op dat de uitrol onhaalbaar maakte én laat de Donau-ring-fout structureel verdwijnen.

**Bijvangst die ik niet had bedacht:** de VS-duwkonvooi-maten (3×3 jumbo hoppers, 105 × 585 ft,
9 ft) passen als sleutel op slot in de USACE-kolk (110 × 600 ft, 9 ft) — de Amerikaanse vloot is
op de sluis ontworpen, en dat bevestigt de kolkmaten van de vorige sessie onafhankelijk.

**⚠️ WERKWIJZE — Lars corrigeerde me vier keer, en telkens terecht.** Dit hoort in het geheugen,
want het is een patroon en geen incident:
1. **Ik loste het verkeerde probleem op.** Op de Ohio-blokkade stelde ik een extra scheepsklasse
   voor; zijn vraag was *"wat gebeurt er in het echt?"* Met die klasse erin zei het model
   vervolgens dat een Ohio-duwbak vanuit Rotterdam vaart — net zo onwaar. De echte fout zat in de
   vraag die de router stelt.
2. **Ik gaf advies dat bij een doel paste dat hij niet had.** Ik adviseerde de 250 m-gaten te laten
   staan "omdat een dicht net connectiviteit zou suggereren die er niet is" — terwijl hij juist
   controleert *óf* ze aansluiten. Ik hield het signaal in stand waar hij op kijkt.
3. **Ik bleef meten in plaats van bouwen.** Drie keer achter elkaar een meting als poort vóór het
   bouwen; de laatste was zelfs rekenwerk (349.312 km ÷ 15 km) en geen meting.
4. **Ik hield twee lagen in stand waar één net hoorde.**

*"Wat ben je anders aan het maken??"* — de correctie die de architectuur rechtzette.

**Gemeten:** zeeroutes exact (19.610 / 8.031). Bewust anders: A'dam→Shanghai 19.794, havens >50 km
1.473 — teruggedraaide verbeteringen die met de overslag terugkomen. Netwerk 10.773 → 73.941
knopen, `marnet.bin` 1,24 → 5,86 MB, verwerken 197 ms, geen console-fouten.
Commits `afcabff` · `fde5336` · `049e5a9`. **Volgende: de overslaghavens.**

## 2026-07-20 (sessie 37) — LAR-514 GEBOUWD: het gabariet-veld + de 14 niet-CEMT-maten

**Het veld staat.** Vier maten per edge in `marnet.bin` (diepgang · breedte · lengte ·
doorvaarthoogte, **decimeter, 0 = onbekend = géén grens**) achter een vlagbyte die drie bytes
scheelt op elke ongemeten edge. De router filtert via `opties.schip` op exact dezelfde plek en van
dezelfde soort als `vermijd` — vóór de relaxatie, dus de grootcirkel-heuristiek blijft toelaatbaar.
HUD kreeg een scheepsklasse-keuze. `?v=032`.

**Werkwijze:** het bronnenonderzoek (de blokkade uit de vorige sessie) is als **achtergrond-
workflow** gestart terwijl ik het mechanisme bouwde. Dat kon omdat de twee onafhankelijk zijn:
zonder maten staat alles op onbekend en sluit het veld per constructie niets af. 43 agents
(14 onderzoekers, elk aangevallen door **twee** skeptici met verschillende lens — een algemene
weerlegger en een *poort-jager* die uitsluitend naar gemiste strengere poorten zocht — plus een
synthese), nul fouten, ~2,5M tokens.

**⚠️ DEZELFDE DENKFOUT TWEE KEER, IN VERSCHILLENDE VERMOMMING.** Een getal dat de **vaarweg**
beschrijft is geen getal dat het **schip** begrenst. Eerst bij de CEMT-presets: ik vulde ook
diepgang, waarna `waal` (VIc → 4,00 m) sloot voor een gewoon klasse Va-Rijnschip (4,50 m) en
R'dam→Nijmegen van 172 km naar **9.405 km** sprong. Het bewijs bleek **meetbaar** in plaats van
beredeneerd: lengte en breedte lopen monotoon op met de klasse, diepgang niet (VIb 4,50 → VIc
4,00). Daarna dook dezelfde fout op in het onderzoek: **vaargeul-projectdiepte is een garantie,
geen maximum** — Mississippi 9 ft project terwijl de USCG 10-10,5 ft toestond.

**Gemeten:** `marnet.bin` 1.249.034 → 1.271.236 byte (+20 KB, +1,6%) · knopen 10.773 / edges
17.024 ongewijzigd · `ports.json` byte-identiek · **alle elf regressieroutes exact** · van de
16.153 edges zónder maat gaat er **0** dicht · R'dam→Luik **375 km voor Vb, DICHT voor VIb** ·
zeeroutes bij elke klasse onaangetast.

**Eigen meetfout, eerlijk vastgelegd:** mijn eerste regressierun toonde alle elf routes fout met
een consistente kleine plus (+2 tot +16). Dat was de **meting**, niet de code — de invarianten zijn
knoop→knoop vastgelegd en ik telde de haven-aanloop mee. De **vorm** van de afwijking wees dat aan:
een pure zeeroute als R'dam→Shanghai kan onmogelijk door een binnenwater-veld geraakt worden.

**Vier vondsten die geen CEMT-klasse ooit had gevangen:** `ohio` 2,7432 m is écht scheepsdiepgang
(USACE: *"vessels drafting up to nine feet"*; de geul is 12 ft) → de Ohio sluit voor **élke**
CEMT-klasse, want zelfs klasse IV steekt 2,80 m, dus **Cincinnati en Louisville zijn onbereikbaar
voor de hele Europese vloot** · de 600 ft-kolken (182,88 m) sluiten een Vb-duwstel van 185 m ·
de **Nanjing-brug (1968, 24 m)** is het fysieke mechanisme waardoor zeeschepen niet boven Nanjing
komen · **kabels liggen stelselmatig lager dan bruggen** en werden 3 van de 4 keer vergeten
(Harahan 145 ft is lager dan élke brug op dat vak).

7 van de 14 systemen ingevuld, 7 bewust leeg. Commits `23d993e` · `b68f1e3` · `f9a5459` · `5cbebc0`.
**Open:** visuele go van Lars · zes edges splitsen/pinnen · vier bronverificaties · overweging om
een Amerikaanse duwbak-klasse aan de HUD toe te voegen.

## 2026-07-20 (sessie 36) — LAR-514 voorbereid: drie ontwerpbesluiten + de CEMT-presettabel

**Korte sessie, géén code** — afgebroken op Lars' verzoek (*"ik wil zo stoppen, sluit anders even
af, gaan we volgende keer verder"*). Wel is alles vastgelegd in **`v2/design/gabarit-veld.md`**
zodat de bouwsessie meteen kan starten.

**De drie open vragen uit [LAR-514] zijn beslist door Lars:**

1. **Vorm C — vier maten per edge** (diepgang · breedte · lengte · doorvaarthoogte), niet
   klasse-enum (A) of tonnage (B). Alleen vier maten vangen álle vijf regimes: Erie faalt op
   **hoogte** (4,7 m), Seaway op **lengte/breedte**, Poe Lock op **lengte** (366 m), Cape Cod op
   **konvooivorm** — geen daarvan ís een CEMT-klasse. CEMT blijft een **afgeleid** HUD-label.
2. **Per edge, geërfd van het systeem** — de Seaway-beperking zit in enkele sluis-edges binnen een
   systeem van 306 km, en de 16 labelloze graad-1-stubs uit [LAR-507] kunnen niets erven.
3. **Zee-edges (Panama/Suez/Kiel) apart** — eerst bewijzen op binnenwater, waar de regimes elkaar
   aantoonbaar tegenspreken (Freycinet 350 t naast CEMT VIb).

**Presettabel gesourcet en geverifieerd:** ECMT Resolution No. 92/2 (12 juni 1992), de officiële
classificatie — niet geschat. Leesregel: bovenkant van elk lengtebereik (Va 110×11,4 ·
Vb 185×11,4 · VIb 195×22,8 · VII 285×34,2), consistent met wat het issue zelf voorstelde.

**⚠️ De doorvaarthoogte komt níet uit de klasse.** De tabel geeft *alternatieven* (5,25 óf 7,00 óf
9,10 m); de beheerder kiest. Een gekozen waarde zou een verzinsel zijn — te laag sluit routes stil
af, te hoog laat een te hoog schip door. Voorstel: hoogte blijft **onbekend**, alleen gevuld waar
echt gemeten. Draagprincipe: **bekende maat = harde grens, onbekende maat = géén grens.**

**Nuttige vondst:** `cemt` bestaat al als veld per systeem en reist al door de hele pijplijn tot in
de browser — het wordt alleen **nergens gelezen**. 22 van de 36 systemen dragen een klasse.

**⚠️ Open blokkade:** de **14 systemen zónder CEMT** zijn niet onderzocht — die ronde strandde op
een API-sessielimiet, dus er zijn geen resultaten en er mag niets verzonnen worden. Bronnen die het
project al kent staan in `next-actions.md` en in de designnotitie.

**Volgende sessie:** eerst die 14 maten, dan bouwen (schrijver → lezer + `opties.schip` → HUD) →
bake. Acceptatie ligt vast: elf regressieroutes exact **én** zonder `schip` gaat geen enkele edge
dicht (aantoonbaar, niet aangenomen).

## 2026-07-20 (sessie 35) — de bulklaag: scope verbreed, wereldwijd gebouwd, live bevestigd (LAR-515)

Lars zag het gat in de Yangtze-delta en vroeg om eerst de scope vast te stellen voordat er iets
gebouwd werd. Scope-onderzoek (8 regio's, onderzoeker + criticus per regio) vond **375 ontbrekende
systemen / ~128.600 km** onder het oude CEMT≥IV-criterium — rapport in `v2/design/binnenwater-scope.md`.

Lars verbreedde de criteria tweemaal: (1) ondergrens van CEMT≥IV naar **"alles wat bevaarbaar is"**
(*"liever een kanaal mappen dat niet gebruikt wordt dan straks extra werk omdat er spoorwegen
uitkomen op plekken waar geen water ligt"*) — gemeten **428.428 km wereldwijd** met het nieuwe
`v2/tools/meet_vaarwegen.py`; (2) van gefaseerde golven naar **één bulkbake** (*"als fundament
gewoon alles mappen lijkt me de beste stap"*).

Een ontwerpronde + onafhankelijke risicoanalyse (workflow, 4 agents) vóór het bouwen vond dat
junction-stitching zoals de 36 bestaande systemen **fataal** zou zijn: op Nederland alleen al
23.189 knopen, meer dan het hele netwerk. **Besluit: de bulklaag is pure tekengeometrie, geen
onderdeel van de routeergraaf** — geen ankers, geen stitchen, geen Dijkstra. Bewezen met `git diff`
(leeg) op `marnet.bin`/`marnet.json`/`ports.json`. Bleek ook drastisch sneller: wereldwijde
scan+bake in ~16 minuten, geen VPS nodig.

**Resultaat: 349.312 km over 8 regio's** (bulk-ru 79.302 · bulk-sa 59.965 · bulk-eu 54.164 ·
bulk-as 48.180 · bulk-cn 42.048 · bulk-na 33.835 · bulk-af 29.464 · bulk-oc 2.354), 16.149 km
weggenomen door een 250m-STRtree-uitsluiting tegen de verhalende laag. Kleur eerst gedempt amber
(bleek onzichtbaar), toen **fel rood** (`0xff1a1a` @ 0,85) na Lars' feedback.

**Live gepusht in twee commits** (`f2ede13` China-proefbake, `d848344` wereldwijd, `0e06dda`
kleurfix), GitHub Pages cache-val herbevestigd (`index.html` cachet zelf 600s). **Lars' visuele go
ontvangen** op mobiel: dichtheid en positie kloppen op "egaal"-ondergrond; satelliet-zichtbaarheid
bewust uitgesteld ("daar gaat het niet om als ze we maar in liggen voor het fundament").

Nieuwe Linear-milestones: Fundament / Verbindingen (was Golf 1) / Promotie. Acht nieuwe issues
(LAR-510 t/m LAR-517). Volgende sessie: LAR-514 (gabarit-veld per edge) → LAR-513 (fantoomknopen) →
de Verbindingen-milestone.

## 2026-07-19 (sessie 34) — vijf issues parallel: 16 systemen in één bake (20 → 36)

Op Lars' vraag *"kan je er meerdere tegelijk laten lopen?"* vijf M24-issues tegelijk door
parallelle agents laten onderzoeken, centraal geïntegreerd en **één keer** gebakken.
**LAR-495/496/497/500/502 → Done.** Live t/m `06384e7` (`?v=029`).

`schelde` 92,1 · `schelde-rijnkanaal` 79,5 · `seine` 115,9 · `seine-boven` 239,9 · `rhone` 234,9 ·
`rhone-boven` 95,6 · `mississippi-upper` 1.728,7 · `illinois` 467,3 · `chicago-kanaal` 62,3 ·
`ohio` 1.555,8 · `yangtze-chongqing` 1.261,4 · `grand-canal-zuid` 321,9 · `parelrivier` 72,7 ·
`xijiang` 317,6 · `wolga` 2.546,4 · `wolga-don` 541,1 km.

**R'dam→Antwerpen 500 → 210 km.** Netwerk 10.152 → **10.773** knopen, 16.401 → **17.024** edges;
havens >50 km 1.410 → **1.358**; corridor 0 m; **alle negen regressies exact**.

**Nieuwe foutcategorie:** het `waterway`-TYPE fout gemapt (de Seine als `stream`). Filter aangepast,
bewezen veilig doordat alle 30 bestaande ketens identiek bleven. Zie `decisions.md`.

**Lars' visuele check leverde twee echte vondsten op** → [LAR-507] (doodlopende MARNET-stubs) en
[LAR-508] (Noord-Duitsland). Twee systemen bewust niet geleverd → [LAR-509].

## 2026-07-19 (sessie 33) — de Donau (LAR-494): Rotterdam→Zwarte Zee compleet

`donau-zeekanaal` **73,0 km** (Constanța → Cernavodă, zee-overgang) · `donau` **632,6**
(→ IJzeren Poort) · `donau-boven` **1.466,6** (→ Kelheim, **ringsluiting op
`main-donau-kanaal`** op 0,24 km). Geknipt bij de **IJzeren Poort** — twee sluiscomplexen,
dus splits op de verstoring (Kaub-redenering).

**Acceptatie: R'dam → Constanța 3.291 km over de rivieren tegen 6.285 over zee.** De stub uit
LAR-493 is weg: `Regensburg` **19,0 → 3,0 km**; Wenen 5,4 · Boedapest 3,7 · Neurenberg 6,2.

**De Donau komt niet via zijn eigen monding binnen** — MARNET reikt niet tot de delta (Sulina
123 km van een zeeknoop), dus werd het **Donau-Zwarte Zeekanaal** de zee-overgang. Bewust
geaccepteerd: deltahavens blijven slecht snappen (Sulina 124,8 · Brăila 100,8 · Tulcea 110,9).

**Zes naamvormen**, twee die het issue niet had: `Дунав/Dunărea` (Cyrillisch eerst) en
`Dunav/Dunărea` (Latijn eerst) dekken *aangrenzende* stukken; `Donau / Dunaj` overbrugt 6,8 km
bij Bratislava. Nieuw: **per-systeem `stitch_km`** (1,5 km op alleen het kanaal, waar OSM bij
de sluis van Cernavodă en de havenmond van Agigea onbenoemd laat; hiaat 1.192 m gemeten).

**Validatie, de scherpste tot nu toe:** elke stad binnen **±4 km** van haar officiële
Donau-kilometer over 1.467 km; totaal 2.099 tegen 2.114 (−0,7%); kanaal 64,3 tegen 64,4.

**⚠️ Kerninzicht:** dit is de **eerste binnenvaartverbinding die twee zeeën koppelt**. Zie
`decisions.md` en `bugs-and-risks.md` — de default is een openstaande keuze voor Lars.

Commit `ac86d98`, live `?v=027`. Netwerk 10.013 → **10.152** knopen, 16.261 → **16.401** edges.
**Ook: LAR-493 op Done** na Lars' visuele go.

## 2026-07-19 (sessie 32) — Main + Main-Donau-Kanaal (LAR-493)

`main` **391,3 km** (Mainz → Bamberg, `aftakking:rijn-boven` op **0,00 km**) ·
`main-donau-kanaal` **168,4 km** (Bamberg → Kelheim). **Acceptatie: Rotterdam → Kelheim
1.119 km** over `rijn`+`rijn-boven`+`main`+`main-donau-kanaal`; elk label los schakelbaar.

**Drie vondsten vóór het bouwen.** (a) **`de-hessen` ontbrak als extract** — de Main loopt ~100 km
door Hessen; de `fr-alsace`-les voor de tweede keer. (b) **`Ludwig-Donau-Main-Kanal`** (1846,
buiten gebruik sinds 1950) ligt met bijna dezelfde strekking náást het MDK → bewust niet
gewhitelist. (c) Het MDK viel uiteen in **zeventien componenten**: elke sluis is een eigen
`Schleuse <plaats>`-way, plus de **naamvariant `Main-Donau-Kanal (RMD)`** bij Kelheim (32 van
1.763 knopen bleven anders los).

**Kernles — de VORM van een lengte-afwijking is de diagnose, niet de grootte.** De Main komt op
+1,9% uit, maar die afwijking *wandelt* over negen punten (Frankfurt −2,5 · **Würzburg +0,2** ·
Bamberg +7,3) = meander-vs-sluiskanaal. Spiegelbeeld van LAR-505, waar juist de *constantheid*
het Julianakanaal bewees. MDK bevestigt zichzelf met `CEMT-tags gezien: Vb`.

**Nieuw gereedschap** `v2/tools/diagnose_keten.py` (commit `2591015`).

Regressie exact (19.610 · 8.031 · Nijmegen 172 · Luik 375 · A'dam→Nijmegen 105 · Shanghai 19.677 ·
Memphis 10.000 · Wuhan 20.626 · Kehl 757). Netwerk 9.975 → **10.013** knopen, 16.223 → **16.261**
edges. Commit `c353dfa`, live `?v=026`. **Ook: LAR-505 op Done** na Lars' visuele go.

**Open:** visuele go op LAR-493.

## 2026-07-19 (sessie 31) — Maas + Benelux-delta (LAR-505) + de eerste ringsluiting

**Vier systemen:** `maas` **278,1 km** (Werkendam → Luik, `aftakking:waal` op **0,00 km**) ·
`maas-boven` 64,2 (Luik → Namen) · `albertkanaal` 127,5 (`aftakking:maas`, 0,00 km) ·
`amsterdam-rijnkanaal` 73,3.

**Nieuw mechanisme `sluitAan` — hechten aan BEIDE kanten.** LAR-504 hecht alleen het *begin* van
een keten; voor een verbindingskanaal is dat de helft. Het ARK hing wel aan de Waal bij Tiel maar
bungelde in Amsterdam. **Meetbaar bewijs:** Amsterdam→Nijmegen bleef **263 km mét én zonder** het
kanaal — 73 km geometrie die nul routes droeg. Met de sluiting op `noordzeekanaal` (3,02 km over
het IJ, waar OSM geen doorgaande benoemde lijn heeft): **263 → 105 km**.

**Drie stille ketenbreuken gevangen:** `Amer` (12,5 km) overbrugt Hollandsch Diep → Bergsche Maas ·
`Canal Albert` is de grensnaam bij Luik · **elk sluiscomplex ligt als drie parallelle kolken**
(`duwvaartsas`/`middensas`/`noordersas`) → alleen de duwvaartsas gewhitelist.

**Twee vallen vermeden:** CEMT-clause uit (de Zuid-Willemsvaart, klasse II, won als kortste pad) en
de keten kiest uit zichzelf het **Julianakanaal** i.p.v. de Grensmaas — tekort t.o.v. de
rivierkilometrage is **constant ~22 km vanaf Maasbracht**, dus kanaal-vs-rivier en geen sluipweg.

**LAR-504 nu end-to-end bewezen:** Nijmegen→Luik **353 km** dwars door een aftakking.
Regressie exact (19.610 · 8.031 · Nijmegen 172 · A'dam→Shanghai 19.677 · Memphis 10.000 ·
Wuhan 20.626). Snaps `Liege` **102,2→2,7** · `Born` 90,2→10,1 · `Antwerpen` 17,6→5,0 km.
Netwerk 9.937 → **9.975** knopen, 16.184 → **16.223** edges. Commit `ba8c287`, live `?v=025`.

**Open:** Lars' visuele go. Bewust open: R'dam→Luik 375 km (havenknoop-overhead, niet de ~230 uit
het issue) en R'dam→Antwerpen 500 km tot het Schelde-Rijnkanaal er is ([LAR-495]).

## 2026-07-19 (sessie 30) — Mosel als eerste echte aftakking (LAR-506) + slepen gefixt

**Mosel** Koblenz → Neuves-Maisons **392,0 km** (officieel ~394, −0,5%), aansluiting knoop 9745 op
**0,13 km** als `aftakking:rijn`. Eerste systeem dat middenin een keten aanhaakt → `volgtOp` is nu
een boom, en LAR-504 is end-to-end bewezen: R'dam → Neuves-Maisons **856 km** over `waal+rijn+mosel`.
`mosel` in `vermijd` → kop weg, **Kehl blijft 758 km**; `rijn` dicht → Mosel valt ook weg.

**Nieuwe foutcategorie: bevaarbaar ≠ bevaarbaar op commercieel gabarit.** Eerste poging 18 km te
kort; zes officiële Moselkilometers wezen de plek aan (tot Frouard klopte alles, daarna liep de
keten via Freycinet-kanalen van klasse I bij Nancy, binnengekomen via de CEMT-clause). Fix:
`cemt_insluiten=False` → 640 → 310 segmenten, pad 15,5 km lánger, alle ways klasse Vb.

**Slepen over de bol** vervangen door grijpen-en-meenemen. Gemeten vóór het aanpassen: de oude wet
was **3,52× te snel op elke zoom** en negeerde de vensterhoogte; ook met de juiste gain glijdt het
gegrepen punt weg als je niet in het midden grijpt. Solver op 200.000 gevallen gevalideerd
(1,6·10⁻¹⁴). `dragSpeed`/`dragRefAltitude` verwijderd.

**Regressie exact:** 19.610 · 8.031 · Nijmegen 172 · Kehl 758 · A'dam→Shanghai 19.677. Netwerk
9.910 → 9.937 knopen, 16.157 → 16.184 edges. Commits `2ef7601` + `2ea5f42`, live `?v=024`.

**Open:** Lars' gevoelscheck op het slepen (headless niet te meten: venster 1×1, framelus stil).

## 2026-07-19 (sessie 29) — M24.1 gestart: de Rijn (LAR-492) + aftakken op elk punt (LAR-504)

**Gebouwd.** De Rijn als twee ketens met `volgtOp`: `rijn` Nijmegen→Bingen **355,0 km** (officieel
rkm 884,6−528 = 356,6 → −0,4%) en `rijn-boven` Bingen→Basel **360,6 km** (358,1 → +0,7%). Aanleiding:
álle searoute-Rijnhavens snapten op knoop 9697, het binneneinde van `waal`, van Duisburg 75,8 km tot
Kehl 389,4 — het Nijmegen/Memphis-patroon over een hele as.

**Het splitspunt uit het issue klopte niet.** Voorgesteld was `zeevaart=True`→`False` bij Keulen,
maar `waal` stroomafwaarts is al binnenvaart, en de vlag blijkt alleen metadata (de browser leest er
enkel `bron` uit). Lars koos splitsen op de **verstoring**: bij Kaub legde het laagwater van 2018/2022
de as stil. Reproduceert exact — met `rijn-boven` in `vermijd` blijven Duisburg 281 km en Keulen
373 km bereikbaar, vallen Mainz/Karlsruhe/Kehl weg.

**Bewijs.** Haventoets (searoute = andere bron dan OSM), snap vóór→na: Duisburg 75,8→**1,5** ·
Koblenz 207,3→**0,7** · Keulen 130,1→**1,1** · Mainz 266,1→**1,4** · Karlsruhe 360,3→**1,9** ·
Kehl 389,4→5,6 · Straatsburg 388,0→9,4 km (die laatste twee liggen in een zijbekken). Havens >50 km
1.449→**1.430**. Corridor-toets 0 m, beide aansluitingen 0,00 km. Regressie exact: 6818→9654
**19.610**, 6391→6818 **8.031**, R'dam→Nijmegen 172, A'dam→Shanghai 19.677, R'dam→Memphis 10.000,
R'dam→Wuhan 20.626. Netwerk 9.863→**9.910** knopen, 16.110→**16.157** edges.

**Lars' vervolgvraag legde een ontwerpfout bloot** (*"we moeten nog wel meer mappen dan alleen de
rijn, de maas en stukken biesbosch"*): M24 bakte **lijnen** — een vervolgsysteem hing aan
`keten_eind`, dus alleen aan het ketenuiteinde — terwijl een riviernet **aftakkingen** heeft. Bijt op
zes plekken (Main bij Mainz, Ohio bij Cairo, Illinois bij Grafton, Nieuwe Merwede, Bergsche Maas,
Amsterdam-Rijnkanaal). **[LAR-504]:** `hecht_aan_keten()` knipt de moederedge door op een **bestaande
geometrie-vertex**, dus zonder één coördinaat te verplaatsen. Bewijs dat het niets sloopt:
`marnet.bin`/`marnet.json`/`ports.json` komen **byte-identiek** uit de bake. Positief getest met een
synthetische zijtak op punt 283 van de 566 in `rijn` (hecht als `aftakking:rijn` op 0,00 km, `rijn`
23→24 edges, lengte blijft 355,0 km).

**Drie lessen.** (a) De namen-survey is nu gereedschap — `v2/tools/survey_vaarwegen.py` rangschikt op
**lengte** mét lon/lat-strekking; ving `Boven-Rijn` (mét koppelteken) en `Le Rhin / Rhein` (de
gecombineerde grensnaam). (b) Een extract kan buiten de oeverlanden liggen — tussen Basel en
Straatsburg ligt de geul in het **Grand Canal d'Alsace** op Frans grondgebied; zonder `fr-alsace`
een gat van 72,9 km. (c) Water ≠ vaarweg — `Vieux Rhin / Altrhein` bewust niet gewhitelist.

**Bijvangst.** Geofabrik gebruikt de pre-2016 Franse regionamen (`normandie` bestaat niet en geeft
0 bytes i.p.v. een 404) → open punt uit de uitrol-brief beantwoord. En de acht bestaande systemen
zijn coördinaat voor coördinaat identiek via het Geofabrik-pad, dus de bronwissel is herbevestigd.
Gecorrigeerd in `now.md`: daar stond 9.877/16.124 terwijl `marnet.json` op 9.863/16.110 staat.

**Linear.** LAR-492 + LAR-504 Done; nieuw **LAR-505** (Maas + Benelux-delta, M24.1) omdat de Maas in
geen van de vier oorspronkelijke M24.1-issues stond. Commits `1d26a24` + `b402fc5`, gepusht, live
`?v=022`.

**Volgende:** LAR-505 — de eerste échte aftakking is meteen het end-to-end bewijs van LAR-504.

## 2026-07-19 (sessie 28) — M25-bronnenplan landroutes: compleet spoornet gekozen, bronnen per modus gemeten
- **Plansessie zonder code, wél gemeten.** Lars wilde vóór de bouw eerst de bron bespreken, net als bij M24.
- **Context die het gesprek kantelde:** land is de **grootste** groep, niet de kleinste — 275 landstromen
  (134 spoor + 105 weg + 36 pijpleiding) tegen 223 zeestromen, en nul geometrie in `v2/`.
- **Besluit: compleet hoofdspoornet, géén corridor-scope** (*"complete spoor is wel beter zeker voor de
  simulator"*). Gelaagd zoals water: compleet spoor = MARNET-rol, verhalende corridors = `EXTRA_VAARWEGEN`-rol.
- **Bron per modus:** spoor = OSM/Geofabrik met NARN als meetlat · pijpleiding = OSM waar goed + GEM's
  **openbare** GitHub-repo · weg = klein houden, want als enige zónder scheidsrechter.
- **Filter gevalideerd door uitsluiting:** Cambodja 652 km (~650), Myanmar 6.643 (6.207,6 ministerie, +7%).
  40–43% van de spoor-ways heeft geen `usage`-tag → `usage=main` eisen sloopt Afrika/Zuidoost-Azië.
- **⚠️ Nieuwe stap die M24 niet had:** parallelle sporen samenvouwen. China +142% (266.146 vs 109.767 route-km)
  omdat dubbelspoor als twéé lijnen gemapt is. Rivieren komen niet in paren.
- **Budget:** routeergraaf 190–240k knopen @10 km past; ruwe tekengeometrie ~11M punten ≈ 36 MB niet →
  vorm ≠ routering, `strak_trekken()` is de kandidaat.
- **De eerlijke route bleek de betere:** Lars opperde een verzonnen naam voor GEM's downloadformulier; niet
  gedaan, en overbodig — de geometrie staat openbaar op GitHub. Centraal-Azië–China 0,3% van CNPC's cijfer.
- **Afgevallen mét bewijs:** NE spoor+wegen, GRIP4, gROADS, OGIM, HIFLD, ENTSOG, HDX. RINF blijft meetlat
  (géén geometrie).
- **Vastgelegd:** [LAR-491] (High, Todo) + comment op de M25-milestone + erfenis-comment. Meetscript
  `v2/tools/meet_spoor.py` (`55d6c5a`). **Volgende: eerst M24's uitrol, dán M25.**

## 2026-07-19 (sessie 27) — Geofabrik-bron, middellijn uit watervlakken, Yangon + Amazone, uitrol opgezet
- **Twee capabilities die de uitrol pas praktisch maken** (live t/m `45a21eb`, `?v=021`).
- **Geofabrik i.p.v. Overpass:** 40 regio's / 17 GB in ~6 min; gevalideerd coördinaat-voor-coördinaat
  identiek (0,000 m). Overpass blijft kruiscontrole. Shapefile viel af (Brazilië/Rusland = 0 bytes).
- **`middellijn_uit_vlakken.py`:** klaring-raster + Dijkstra + `strak_trekken()`. Klaring ≥150 m
  encodeert commerciële bevaarbaarheid in de geometrie zelf.
- **`yangon`** 23,2 km (LAR-485-stub weg, snap 21,8 → **1,3 km**) · **`amazone`** 1.261,9 km
  (snap Manaus 1.084 → **0,9 km**, Rotterdam→Manaus 9.268 km; Óbidos 3,15 km van de lijn).
- **Regressie exact:** 6818→9654 19.610, 6391→6818 8.031; Mississippi 1.032, Yangtze 1.016.
  Netwerk 9.877 knopen / 16.124 edges; havens >50 km 1.471 → **1.449**.
- **Lars ving twee dingen die ik miste:** de hoekigheid op de bol (rasterartefact → `strak_trekken()`,
  ook 4,4% te lang) en dat Brazilië meer draagt dan één rivier (uitrolplan te grof → schaal
  bijgesteld naar 40–50 systemen).
- **Twee eigen fouten, gemeten:** Overpass-timeout 600 s liet één mirror de run 10 min gijzelen
  (query duurt 74 s); vlakken-v1 verzamelde alle polygonen + `union_all` → 5,5 GB (van 289.365
  watervlakken raken er 1.241 het venster).
- **Linear:** 6 milestones M24.0–M24.5 + 12 issues LAR-492…LAR-503, per regio met issues per systeem.

## 2026-07-19 (sessie 26) — LAR-487 + LAR-488: de VS- en China-binnenvaartpilot gebouwd + gemeten
- **Beide resterende M24-pilots staan** (commit `919b046`, `?v=018`, live). De pilotreeks NL→VS→China
  is compleet op Lars' visuele go na.
- **Beide zones eindigden anders dan hun naam suggereert.** MARNET's `mississippi`-tak gaat vanaf New
  Orleans niet de rivier op maar het **Pontchartrainmeer** in en loopt dood (knoop 113); de
  `yangtze`-zone ("Nanjing-Jiangyin") eindigt bij **Zhenjiang** (knoop 9668), 78 km voor Nanjing.
  Vooraf snapte Memphis **532,7 km** weg (fictieve route 303 km) en Wuhan **528,4 km** (240 km).
- **Nieuw `volgtOp`-mechanisme** (zie `decisions.md`): ketens `mississippi` 218,8 km (zeevaart) →
  `mississippi-boven` 813,1 · `yangtze` 92,7 (zeevaart) → `yangtze-boven` 683,6. Beide
  vervolgsegmenten hechtten op **0,00 km**, corridor-toets 0 m op alle zes systemen.
- **USACE-meetlat** (`v2/tools/toets_usace.py`, nieuw): mediaan **76 m** / p95 409 m over 760 punten
  (NL-bake-off ~80 m). Staart (3,8% >500 m, max 1.889 m) = **OSM-vs-USACE kanaalverschil, niet onze
  simplify** — de ruwe 801-punts lijn heeft dezelfde max; geconcentreerd op de oxbow-stretch
  lon -91,15..-91,49. **Lengte 1.028,2 km = 638,9 river miles vs officieel 641 → 0,3%.**
- **China zonder scheidsrechter:** negen searoute-havens vallen vanzelf op de keten (Wuhan 0,7 ·
  Jiangyin 1,2 · Wuhu 1,9 · Nanjing 2,5 · Anqing 2,9 · Zhenjiang 5,2 · Jiujiang 7,1 km).
- **Acceptatie:** New Orleans→Memphis **1.032 km** (officieel 641 river miles = 1.032) · Shanghai→Wuhan
  **1.016** · R'dam→Wuhan 20.626 · R'dam→Memphis 10.000 · beide labels in `vermijd` → geen route.
  **Regressie exact:** 6818→9654 **19.610**, 6391→6818 **8.031**; Amsterdam→Shanghai 19.677.
  Snaps Memphis 532,7→**5,9** · Wuhan 528,4→**0,7** · Baton Rouge 87,6→**3,1** · Nanjing 77,9→**2,5**.
  Netwerk 9.698→**9.812** knopen / 15.945→**16.059** edges, bin 1.165→**1.170 KB**, >50 km 1.471→**1.452**.
- **Grootste tijdvreter + eigen fout:** Overpass-mirrors lagen er deels uit (504's). Ik diagnosticeerde
  eerst verkeerd — "query te zwaar" → timeout op 600 s, waardoor een overbelaste mirror de run tien
  minuten gijzelde voor failover, terwijl de query gemeten **74 s** duurt. Daarna gericht gefixt:
  client- los van server-timeout, exacte tag-match, conditionele CEMT-clause, retry-rondes,
  query-inhoud-cache, `overpass.osm.jp` eruit (kapot certificaat).
- **Twee stille-data-vallen gevangen:** `AMILE`/`BMILE` zijn niet overal gevuld (twee links op 0.0 zien
  eruit als een gat van 45 mijl terwijl de geometrie er is), en `exceededTransferLimit` zit bij
  `f=geojson` genest onder `properties` → op de top-level sleutel checken truncateert stil op 2.000.
- **Linear:** LAR-487 + LAR-488 → **Done** na Lars' visuele go (*"ik heb even gekeken naar die test
  routes dat ziet er wel goed uit mooi over de rivier"*), met uitgebreide meet- en slot-comments.
  Daarmee is de M24-pilotreeks compleet en zijn alle drie de controle-situaties bewezen.

## 2026-07-19 (sessie 24) — LAR-486 NL-pilot uitgevoerd: bake-off OSM vs UNECE, alle tests groen, live
- **Pipeline gebouwd + bewezen** (commit `d9a9e0f`, `?v=016`, live op Pages): `fetch_waterways.py`
  (bron-agnostische stitcher: kortste waterpad anker→anker; OSM via Overpass, UNECE via de Blue Book
  ArcGIS-laag — achter Cloudflare, via de Browser-pane; NL-extract in build-cache) →
  `EXTRA_VAARWEGEN`-stap (ketens `soort=1`, knoop per ~15 km, passage-labels + zeevaart-vlag;
  **corridor-toets** ≤ 250 m i.p.v. vlak-toets; zee-overgang NE-water óf zone) →
  **verzoening-cache** (35 min → 1 min) → `?vaarwegbron=unece`-toggle + ODbL/UNECE-attributie.
- **Tests groen op beide varianten:** zeenet exact onaangetast (19.610/8.031 tussen de óúde
  knoop-ids — regressie in 2 lagen, aangescherpt door Lars); **Amsterdam via IJmuiden** (−131 km,
  visueel bevestigd); R'dam→Nijmegen 172 km over `waal`; snaps Amsterdam 0,8 / Nijmegen 2,1 /
  Dordrecht 3,8 km; netwerk +12 knopen/+12 edges, bin 1.165 KB.
- **Bake-off:** bronnen mediaal ~80 m eens; OSM gedetailleerder + scriptbaar, UNECE officiële
  CEMT-klassen maar handwerk + EU-only. Advies: OSM-geometrie + UNECE/USACE-meetlat.
- **Hobbels:** 2× ~40 min bake gestrand op te strenge zee-overgang-check (Maasmond = NE-land →
  zone-vrijstelling gebouwd); argparse `--suffix=-unece`; winst-meting via de oude Markermeer-knoop.
- **Linear:** resultaat-comment op LAR-486 (In Progress tot keuze); LAR-489 (AIS-realisme-check,
  backlog) vastgelegd. **Open: Lars vergelijkt de twee live-URL's en kiest de bron.**

## 2026-07-19 (sessie 23) — M24-bronnenplan: bake-off OSM vs UNECE, pilots per regio (planning, géén code)
- Lars wilde vóór de M24-bouw eerst de **bron** bespreken (zee had de vector-kustlijn als controlepunt; voor
  binnenwater bestaat zoiets niet vanzelf).
- **Kerninzicht:** de **corridor-toets vervangt de vlak-toets** — rivieren/kanalen bestaan niet als water in de
  NE-polygonen; controle wordt "elk ~2 km-monster ≤ ε van een bevaarbare-vaarweg-middellijn"; de polygoon-toets
  blijft op de zee-overgang (mondings-knoop op een MARNET-knoop in NE-water).
- **Bronnenveld (websearch):** een wereldwijde kant-en-klare dataset bestaat niet. OSM = enige wereldwijde bron
  mét kanálen (+ CEMT-tags EU); UNECE E-waterway-shapefile = officieel EU-net; USACE NWN = officieel VS-net;
  NE-rivers (géén kanalen — geen NZK) en HydroRIVERS (DEM-afgeleid) afgevallen.
- **Besluiten Lars:** bake-off in de NL-pilot beslist de bron (NZK + Waal uit OSM én UNECE) · pilots per regio
  NL→VS→China (elk één controle-situatie; China zónder scheidsrechter = zwaarste test) · einddoel = het complete
  commercieel bevaarbare net (EU CEMT ≥ IV / VS USACE / elders commerciële systemen) · labels nú meebakken
  (passage-label + zeevaart-vlag; router permissief, filteren = M26/M21 via `vermijd`).
- **Linear:** LAR-486 (NL-pilot, High) + LAR-487 (Mississippi × USACE) + LAR-488 (Yangtze) aangemaakt, 487/488
  blocked by 486; besluiten-sectie toegevoegd aan LAR-485. Geen issue naar Done (milestone loopt).
- **Volgende:** LAR-486 in een verse sessie. Vault: [[2026-07-19-grondstoffen-atlas-m24-bronnenplan]].

## 2026-07-18 (sessie 22) — M23 KLAAR: MARNET verzoend, haven→haven werkt, go binnen (LAR-483 Done)
- **Nagekomen: pc-scherpte-reeks** (`990765c`+`61d7388`+`1a724b8`, `?v=014`): tegel-zoom ~1 texel/schermpixel +
  budget ×breedte²×aspect · dekking via straal-bol-snijding (H/V apart) · **middenring z−2** voor de schermhoeken
  (LOD: shell z3 → ring → patch). 1080p/portret ~100 tegels goed; ultrawide-restje geaccepteerd ("we laten het
  zo") — zie bugs-and-risks punt 0.
- **Afronding zelfde dag — Lars' go:** *"het zee gedeelte lijkt klaar te zijn, het ziet er realistisch uit."*
  → LAR-483 Done. Zijn test-vondst (Amsterdam vaart uit via IJsselmeer/Den Helder i.p.v. het Noordzeekanaal)
  gemeten verklaard: **MARNET heeft geen Noordzeekanaal-edge**; Amsterdam snapt op de Markermeer-knoop (15,1 km).
  Besluit: geen quick-fix → **M24-milestone + [LAR-485]** aangemaakt (EXTRA_VAARWEGEN, rivierhaven-stubs,
  2 restedges, binnenvaart-beleid).
- **Lars:** *"kan je beginnen met de marnet routes op de nieuwe kaart zetten… dan kunnen we daarna van zee
  haven naar zee haven testen"* → LAR-483 exact uitgevoerd, tegen de **1:10M-vectorwereld** (vector = waarheid).
  Live t/m `b6867f7`; **rest = visuele go van Lars** (LAR-483 In Progress met volledig resultaat-comment).
- **`v2/tools/bake_marnet.py`:** graaf 9.686 knopen / 15.933 edges (lon genormaliseerd), grootcirkel-verdicht
  (10 km), getoetst op ~2 km (shapely; **meren = water**), classificatie aanloop / binnenwater (93 edges, 29
  zones) / kapot (150) → **148/150 omgelegd** (A* 0,02°→0,01°, mét/zonder kustbuffer; eindtolerantie per
  uiteinde uit de oorspronkelijke koorde), 2 onopgelost. Uitvoer `marnet.bin/json` (1,17 MB varint) +
  `ports.json` (3.962 havens → knoop).
- **`v2/src/marnet.js`:** één LineSegments (blauw=zee, amber=binnenwater) + **A\*-router ~3 ms** met
  passage-restricties (default `northwest` dicht = searoute's default) + HUD-toggle + route-test-UI (datalist).
- **Twee structurele bugs gevangen door de eerste test:** Noordwest-Passage als kortste pad (→ restrictie,
  meteen het M21-mechanisme) en **15 dubbele ±180-knopen** die de trans-Pacific doorknipten (Yokohama→LA
  rekende 32.000 km via Suez+Panama → lon-normalisatie).
- **Gemeten:** R'dam→Shanghai **19.610** via gibraltar+suez+babalmandab+malacca · Antofagasta→Shanghai
  **18.915** op de 50°N-lane (searoute 18.880 = M18-benchmark; v1 dwong 19.970 af) · Yokohama→LA **9.111** ·
  Hamburg→NY 6.480 · Montreal→R'dam 5.852 · Duluth→R'dam **8.031** door Meren+Seaway · Novorossiysk→Shanghai
  15.792 via bosporus+dardanelles+suez · Valparaíso→Shanghai 19.220 deterministisch. Daarmee bundeling/dedupe/
  determinisme van LAR-483 structureel binnen.
- **Open → M24:** rivierhaven-stubs (Yangon ~30 km recht over land — rivier zit niet in de polygonen), de 2
  restedges, binnenvaart-beleid. Parallelle sessie fixte de root-atlas tegelscherpte (`c714297`, alleen v1).

## 2026-07-18 (sessie 21) — M22 UITGEVOERD: v2 staat, vectorwereld = bron van waarheid, tegels tot ~1 km
- **Lars' visuele go:** *"dit is echt goed… nu kunnen we die vectorlijnen als bron van waarheid gebruiken en
  de view opties zijn top zo."* → **LAR-484 Done, M22 af.** Live op `…/grondstoffen-atlas/v2/` t/m `4dd48d5`.
  **Buiten `v2/` is niets aangeraakt.**
- **Techniekkeuze vooraf besproken:** géén globe-library (globe.gl/Cesium/deck.gl) maar Three met onze eigen
  bol — de library bepaalt de schoonheid niet, en Cesium zou een **vierde wereldmodel** toevoegen. Lars koos
  expliciet voor écht upgraden (r128 → **r185**), met als bewuste prijs dat **M26 deels herbouw** wordt:
  `markers.js`/`flows.js`/`voyages.js` draaien op r128-API's die weg zijn. WebGPU bewust overgeslagen
  (koopt doorvoer, geen schoonheid; onze scene is geometrie-gebonden).
- **Volgorde gehanteerd:** kleur → waarheid → schoonheid → routes. De beeldpijplijn eerst omdat die de
  *kalibratie van het meetinstrument* is (Lars' rol = visuele check); de echte shaders hangen aan de
  definitieve geometrie, dus eerder bouwen = twee keer bouwen.
- **Gebouwd in `v2/`:** `src/globe.js` (scene, hoogte-gebaseerde zoom/sleep, ACES, log-diepte) ·
  `src/world.js` (decoder + opbouw) · `src/tiles.js` (Esri/OSM, shell + detailpatch, invaden) ·
  `tools/measure_world.py` + `tools/bake_world.py` · `data/world-10m.{bin,json}`.
- **De vectorwereld:** Natural Earth **1:10M**, 446.175 punten land + 35.512 kleine eilanden. Mediane
  puntafstand **7,7 → 1,5 km**, grootste gat **628 → 55 km**. Japan 16×, Hormuz 94×, Baja 11×, Malakka 7×
  meer detail. Gebakken tot **1,64 MB** (was 11,5 MB ruw): quantiseren op 1e-4° (~11 m) + delta-codering +
  zigzag-varint = **3,3 byte/punt**. Eén draw call voor 472.042 lijnstukken.
- **Waarom "van dichtbij geen upgrade" geen instelling was:** 4096 px voor de hele aarde = **9,8 km per
  textuurpixel**; bij 1,3 km/schermpixel wordt één textuurpixel over ~7 schermpixels uitgesmeerd. Gemeten op
  Malakka bij maximale zoom: vectorwereld contrastsprong **166/255** met 21 harde randen, satelliettextuur
  **5** en nul randen.
- **Daarna op Lars' verzoek de tegellaag** (hij wees op earth3dmap.com): de zoom-rem zat in **onze eigen
  code**, niet in de bron — camerabodem ~930 km (zoom rekende in **afstand tot het middelpunt** i.p.v.
  hoogte), nabij-vlak vast op 0,1 (= 265 km), kustlijn zwevend op 9,5 km. Alle drie gefixt +
  `logarithmicDepthBuffer`. Nu tot **~1 km hoogte**, tegels tot **z19**. Gemeten op 1,95 km boven Rotterdam:
  met tegels 3,74 detail/pixel, zonder tegels **0,00** — de oude textuur bevat daar geen informatie meer.
- **Bronnen-nuance:** earth3dmap draait bovenin op **Esri** (onze bron) maar geeft het bij straatniveau over
  aan een **ingesloten Google Maps** (zichtbaar aan de bronregel + Street View-poppetje). Google-tegels mogen
  niet in een eigen 3D-bol; Esri gaat zelf tot z19 (~30 cm/px bewoond gebied) mét verplichte bronvermelding.
- **Drie bugs die het waard zijn te onthouden:**
  1. **Vectorlaag lag 90° verdraaid** — `x = cos(lat)·sin(lon)` i.p.v. v1's `x = cos(lat)·cos(lon)`,
     `z = −cos(lat)·sin(lon)`. Kustlijnen klopten onderling maar lagen los van de bol (Lars: *"die kustlijnen
     zijn top, alleen de ligging klopt niks van"*). Moet **tegelijk** kloppen met de UV-afbeelding van
     `THREE.SphereGeometry` (lon 0 op +X) **én** met de markers/routes die in M26 uit v1 komen.
     Geverifieerd met `earth-water.png` als **onafhankelijke scheidsrechter**: 80–83% van de kustpunten op
     een land/water-grens vs 4,8% voor willekeurige punten; met de oude formule 8% (= willekeur-bodem).
  2. **Lege tegels schilderden over de bol** — bij het overzetten uit v1 ging `opacity: 0` + invaden verloren
     → horizontale banden en een ruitjespatroon boven de pool zolang tegels onderweg waren.
  3. **Bijna verkeerd geverifieerd door cache** — na de uitlijn-fix gaf de meting onzin; de browser had
     `?v=002` geladen omdat **de `index.html` zelf** in de Pages-cache zat.
- **Beeldpijplijn-correctie op mezelf:** ik beweerde eerst te stellig dat v1 "in het verkeerde kleurdomein"
  rendert — v1 zette `outputEncoding` wél goed. De winst zit in tone mapping + de fysieke belichting van
  r155+. En ACES aanzetten zónder de belichting mee te verhogen maakt het beeld juist **donkerder**.
- **→ Volgende: M23 · MARNET-zeeroutes** over de vectorwereld; kern blijft **LAR-483**.

## 2026-07-18 (sessie 20b, slotdeel) — Fundament-plan M22→M26 vastgesteld, atlas bevroren, v2/ als locatie
- **Lars' besluit** na de ontkoppelings-sessie: huidige atlas **bevriezen** (*"wat we nu hebben vind ik al
  wel erg mooi om te zien, alleen zitten er wel veel schoonheidsfoutjes in"*), alle M18-issues on hold, en
  de kaartlaag opnieuw opbouwen in fasen — met zijn heuristiek als drijfveer: *"fixes die na 2/3× niet
  lukken worden meestal niet beter."*
- **Vijf milestones aangemaakt:** M22 vector-wereldmodel (start **LAR-484**, Urgent) → M23 MARNET-zee
  haven→haven (kern LAR-483) → M24 binnenwater → M25 land/spoor → M26 grondstoffen terugzetten.
- **Kerndiagnose achter M22:** drie botsende wereldmodellen (satelliet · LAND_POLYS 1:50M · MARNET-kustlijn)
  → Lars en ik zagen verschillende waarheden. Zijn oplossing: een gegenereerde **vectorwereld** wordt de
  waarheid (scherp op elke zoom, ondubbelzinnig), satelliet wordt een skin.
- **Budget doorgerekend op zijn scepsis** ("alle routes in 300 KB?"): we slaan de **kaart** op, niet de
  routes. MARNET ~310 KB tekst; 5 km-hersampling → ~260k knopen ~1,2 MB, zoeken ~0,1 s. Dichtheid is geen
  beperking — maar **dichtheid ≠ gladheid** (trapjes-les).
- **Locatie besloten: `v2/` in deze repo** — Pages deployt mee (`…/grondstoffen-atlas/v2/`), gereedschap
  ernaast, M26 triviaal. **Harde regel: buiten `v2/` niets aanraken.** Lars kijkt mee via die URL; v2
  krijgt vanaf dag één `index.html` + cache-busting.
- **Overdracht geverifieerd** alsof een verse sessie start (now.md → Linear → CLAUDE.md → next-actions);
  twee gaten gedicht (code-locatie + dirty-tree-instructie: terug naar `9444fcb`, klem niet afmaken).
- **Startzin nieuwe sessie:** *"we gaan verder aan de nieuwe 3D-wereldbol met routes voor de grondstoffen atlas."*

## 2026-07-18 (sessie 20) — Patch-spiraal doorbroken: vorm/snelheid/klem ontkoppeld + netwerk-diagnose (LAR-483)
- **Startpunt:** besluit dat **MARNET de router blijft** (Lars overwoog 3 maanden AIS-data; AIS toont schepen,
  geen lading, en gratis wereldwijde historie bestaat praktisch niet). Zijn idee "echte schepen op de bol met
  een knop" → **LAR-482** als losse dichtheidslaag ná M18.
- **Vier visuele klachten van Lars**, alle vier terecht: band vaarbanen over Japan · band door de lege zuidelijke
  Stille Oceaan · *"rare knik naast Amerika waar alle paden over elkaar gaan en de balletjes raar doen"* (Baja,
  plus Vogelkop en Malakka) · *"soms gaan ze heel snel en dan ineens afremmen"* + lijnen die samenkomen waar dat
  niet hoeft én uit elkaar gaan terwijl ze dezelfde bestemming hebben.
- **De grootste tijdvreter was CACHE, niet routing.** `index.html` laadde assets zónder versie terwijl Pages
  `max-age=600` stuurt → Lars zag **drie fixes lang "geen verschil"** terwijl alles wél live stond. Opgelost met
  `tools/stamp_assets.js` (inhouds-hash per asset). Pas daarna zag hij verandering: *"nu pas zie ik dat het goed gaat."*
- **Methodologische fout van mijn kant:** de eerste Japan-verificatie testte **alleen de middelste vaarbaan** en
  verklaarde het probleem opgelost, terwijl de klacht juist over de **buitenste** banen ging. Les vastgelegd.
- **Het keerpunt:** Lars concludeerde *"ik krijg steeds meer het idee dat we dat niet echt kunnen fixen want anders
  blijven we heen en weer gaan zonder echt een fix"* — en had gelijk. Eén puntenlijst droeg tegelijk de vorm van de
  lijn, de vaarsnelheid en de baan-klem, met tegenstrijdige eisen. Na **ontkoppeling** verbeterde alles tegelijk:
  snelheidsvariatie **15,9× → 1,27×** (slechtste 47× → 2,3×), landtreffers **406 → 108**, Japan **8 → 0**,
  Baja-knikken **21 → 0**, Malakka **9 → 0**, geometrie 3.710 → 817 punten.
- **Onderweg gefixt:** trans-Pacific corridors consistent op 50°N (met de les dat een stabilisator op een *dicht*
  stuk netwerk moet liggen — via 50°N/180° ontstond een kaarsrechte interpolatie door leeg water; via −10°/−80°
  deelt Valparaíso nu 95 van 100 punten met de zusterlane) · trapje-opruiming in de baker (694 trapjes) · een
  nieuwe landkruising bij de Channel Islands die `check_corridors` ving en die door fijner bemonsteren verdween.
- **MARNET doorgemeten:** 4.109 features / 15.840 segmenten / 9.646 knopen; segmentlengte mediaan 83 km,
  **max 3.611 km** → een **grove graaf, geen waterkaart**. Lars' idee "netwerk over de bol laden" voorkomt
  land-treffers dus niet vanzelf; de bruikbare vorm is het netwerk **één keer** verzoenen met onze landpolygonen.
- **Bewust NIET doorgepatcht** (sessie zat op 500k tokens; Lars: *"leg het duidelijk vast zodat een nieuwe sessie
  niet weer het wiel hoeft uit te vinden"*) → **LAR-483** (High, Todo), zelfstandig leesbaar.
- **Commits t/m `9444fcb` gepusht.** Asymmetrische klem (links/rechts, `SIDE_SIGN = 1` empirisch bevestigd) staat
  **in uitvoering en is niet gepusht**: Baja-spreiding hersteld (143 km) maar Japan 0 → 52; waaier ±60° ongemeten.
- **LAR-474 blijft In Progress** — visuele go/no-go van Lars ontbreekt.

## 2026-07-17 (sessie 19) — Drie weergave-fixes, visueel bevestigd (LAR-479 + LAR-481) — pilot bewust gepauzeerd
- **Lars' prioritering:** *"we waren bezig met het verbeteren van de zee routes middels een pilot op koper, echter
  denk ik dat we eerst prioriteit moeten stellen aan het fixen van de globe tegels laadprobleem… als we dat eerst
  fixen voordat we de routes doen lijkt me beter."* LAR-474 blijft In Progress; deze sessie ging alleen over weergave.
- **LAR-479 · tegel-afkap — twee oorzaken, niet één.** (1) `maxTiles: 40` was **kleiner dan één patch** (42–72 tegels)
  terwijl `updateDetail` rij voor rij van **noord naar zuid** vulde → de zuidelijke rijen kregen structureel niets;
  de grens bewoog mee omdat de bbox rond `viewCentre()` ligt → **er was geen sweet spot**, je zag alleen de bovenkant
  van de bug. (2) `detailZoomFor()` miste **`cos(lat)`** → hoge breedten vroegen méér tegels voor dezelfde scherpte
  (Noorwegen 33%/0%, veel erger dan China). *Correctie op de vorige sessie: de "camZ 4,0/5,6/6,5 zijn gekapt, de rest
  niet"-analyse was te optimistisch — door oorzaak 2 is vrijwel élke view gekapt.* Fix: `cos(lat)` + budget 96 +
  midden-naar-buiten.
- **Zoom-evenredig draaien.** `rotation += dx * 0.005` was zoom-onafhankelijk (volle zoom 9× te gevoelig). Schaalt nu
  met de camera-afstand, **geankerd op de standaardzoom** (28,65°/100px identiek aan oud; volle zoom 3,13°; ratio
  **0,109** = exact de ratio zichtbare wereld).
- **LAR-481 · de marker-LOD vuurde AVERECHTS.** Lars zag Norilsk pas bij inzoomen. Dat léék tier-by-design (staat zo
  in de kop-comment) maar was het omgekeerde: `forced` overrulet tier voor **57/63** koper-nodes → de tier-regel raakte
  **alléén de 6 context-mijnen zónder stroom**. Chuquicamata (1,6) pop-in vs. Los Pelambres (1,6, wél stroom) altijd
  zichtbaar. Lars koos uit 3 opties: markers verdwijnen niet meer op tier, **`tier` = alleen labels**; `tierZoom` +
  `forced`/`usedNodeIds` verwijderd. Bewust ná M18: stromen ook tieren (raakt `flows.js` = pilot-code).
- **Verificatie (412×915, headless).** Tegels via raycast-grid ("ligt hier een geverfde detailtegel?"), met de **oude
  code echt teruggezet** (`git stash` + schone origin op 8733): 3 van de 4 oude views **exact op de cap van 40**
  (maximale zoom 100%/**50%**, Noorwegen **33%/0%**); nieuw **100%/100% op alle 7 views**, piek 72 tegels. Draaien via
  echte pointer-events. Markers: constant over z 8,0→2,75, labels gefaseerd (0 → 12 → 29), **regressie 14 grondstoffen:
  pop-in 0**, geen console-errors, build schoon.
- **Lars' bevestiging (mobiel, Pages):** *"top echt goeie upgrades/fixes ze werken zoals het hoort nu, k zie de mijnen
  en de kaart is scherp en heen en weer over een ingezoomde bol werkt goed."*
- **Methodisch:** de tegenproef ís het bewijs — de oude code echt terugzetten i.p.v. redeneren leverde het beslissende
  getal (3/4 exact op de cap). En: een gemelde bug kan een feature zijn die **omgekeerd in werking** is (LAR-481 had ik
  als "by design" kunnen afdoen). Gotcha's hielden stand: pane cachet script-tags → tweede server-instance;
  `document.hidden` → rAF pauzeert → tick pompen via `GLOBE.start()`; WebGL-screenshot hangt headless → Lars bevestigt.
- **Commits** `297016f` (tegels + draaien) + `8dda38e` (markers), Claude-trailer, alléén eigen bestanden, **gepusht →
  live**. Linear **LAR-479 + LAR-481 Done** (481 nieuw aangemaakt). `CLAUDE.md` sectie I gecorrigeerd (usedNodeIds-gate
  bestaat niet meer). **Volgende:** terug naar LAR-474 — de ondergrond is nu scherp, wat de routes makkelijker
  beoordeelbaar maakt.

## 2026-07-17 (sessie 18) — M18 koper-pilot GEBOUWD + 2 diepe bugs gefixt — IN TEST, morgen verder
- **Stand: MIDDEN IN DE PILOT** (LAR-474 In Progress). Koper vaart volledig op gebakken MARNET-routes, 3× live op
  Pages (`5af8fe0`→`3c801a0`), maar **geen go**: Lars ziet op mobiel nog routes over Japan (stale-cache-hypothese,
  morgen incognito verifiëren) én wil de **wereldbal-weergave duidelijker** vóór de uitrol (open idee, verkennen).
- **LAR-473 Done:** spec `design/zeeroutes.md`, alles gemeten (987 legs → 381 corridors, dedup 61%; 357 KB @ 3 dec;
  (a)-vs-(b) scheelt 11% → omvang geen argument). Lars: **(a) opruimen** → aangescherpt tot **"MARNET beslist"**
  (óók echte knelpunten niet afdwingen; `wp-taiwan` stond in ketens waar het niet hoort, +1.497 km).
- **Diagnose-correctie:** de "1.090 km-omweg" bestond niet — 93% antipodaal, echte delta 231 km (route-A-fout, die
  ik eerst zélf reproduceerde). Herijkte winst: zeereizen −9,3% (1,203→1,091), trapjes 37→25, A\* uit runtime, M21.
- **Gebouwd:** `tools/extract_corridors.js` + `bake_searoutes.py` → `_searoutes.js` (22 corridors, 26 KB,
  deterministisch, passages, hard falen) · `flows.js` cache-lookup + **geometrische knelpunt-detectie** (Dover-ring
  verscheen vanzelf; Lombok verdween terecht — Townsville=oostkust) · 61 wp's uit `copper.js` · koper 84 legs /
  0 kapot / 24 hits · regressie 13 andere 0 kapot/0 hits.
- **Lars' mobiele feedback → 2 diepe fixes:** (1) baker: de-zigzag (Yangtze-knik) + A\*-landomleiding+kustbuffer
  (Vogelkop 399 km, Guadalupe) + checker `check_corridors.js`; (2) **curve-sampling `util.js`**: uniform 1/~75 km
  sloeg kustpunten over → spline over land ("niet alle nodes pakken de paden" — letterlijk). Adaptief gemaakt;
  geverifieerd op de **gétekende** curve: 22/22 op water.
- **searoute-empirie:** suez dicht → +73% om de Kaap; ormuz dicht → `length: 0` + warning = *isolatie, nooit 0 km
  in een teller*; `traversed_passages` = M21-query; MARNET dekt óók Saint-Laurent + Kaspisch (getoetst).
- **Infra:** GitHub-egress flaky → achtergrond-retry-loops duwden alle 3 pushes erdoor. Correctie: "repo lokaal-only"
  was verouderd — Pages-deploy bestaat sinds 15-07.

## 2026-07-17 (sessie 17) — M18 · Realistische zeeroutes vastgelegd + feature-trio hernummerd + zoom-bug bewezen (GEEN code)
- **Context:** Lars drukte per ongeluk **rewind** → het gesprek was weg uit mijn context (schijf intact). Zijn eerder besproken features stonden wél in Linear, maar als **milestones** (0 issues) — ik zocht alleen op `list_issues` en concludeerde ten onrechte "niets vastgelegd". **Les: milestones ≠ issues.** Oude sessie via telefoon-screenshots gereconstrueerd (claude.ai `/code/session_…`-link = privé app-URL → 403, ook na "public"; alleen een echte `/share/`-link zou werken).
- **Aanleiding:** de atlas is inhoudelijk compleet (14 grondstoffen, backlog leeg) → de volgende stap werd **niet** een 15e grondstof maar **route-kwaliteit**. Lars: *"er zijn wel een aantal plekken waar routes bewust langs knelpunten gaan terwijl dat niet echt realistisch is … een boot zou nooit er zo doorheen varen."*
- **Diagnose (3 oorzaken in `searoute.js`):** `openRadiusDeg: 1.2` = ~130 km geforceerd water rond élk knelpunt → A\* vaart dwars over land/eilandjes (hoofdboosdoener) · 8-richtingen-A\* → trapjes (Golf→Rotterdam **33 richtingswissels**) · grof 0,25°-raster + `heuristicWeight: 1.35` + **géén echte vaarlanen** → het vindt het kortste *watertraject*, niet de lane die schepen varen.
- **Lars' "route A" legde een kapotte pilot bloot:** *"ik zie op onze wereldbol niets dat route A neemt."* Klopte — de pilot van 16 juli rekende **kaal origin→dest, zónder `via`-ketens**, terwijl elke Chili/Peru→China-koperstroom verplicht via `wp-pac-zuid` → `wp-pac-west` → `wp-taiwan` loopt. Route A (noordelijk over 43°N) tekent de bol nergens → vergelijking ongeldig. **Nieuwe harde regel:** vergelijk altijd tegen wat `flows.js` werkelijk rendert.
- **Maar de uitkomst draaide om (het scherpste bewijs voor M18):** Antofagasta→Shanghai = grote-cirkel **18.526 km** · searoute (echte lanen, noordelijk tot 50,7°N — passeert Australië niet) **18.880 km (+2%)** · **onze bol (zuidelijk via `wp-pac-zuid` op 26°Z) 19.970 km (+8%)** → **~1.090 km omweg** (~een week varen). Niet de pilot maar **onze bol** was hier onrealistisch. Nuance eerlijk vastgelegd: Antofagasta ligt bijna-antipodaal t.o.v. Zuid-China → noord/zuid schelen relatief weinig; 6% is niettemin geen ruis.
- **Besloten:** **M18 · Realistische zeeroutes (searoute)** = de fundering; trio hernummerd **M19** (stress) / **M20** (meta-view) / **M21** (simulator). Architectuur: precompute at build-time, **gededupliceerd per haven-paar**, netwerk bewaren voor M21 (*edge eruit → herrouteren*), **alleen zee-legs**, `searoute` = build-dependency, runtime blijft pure JS. **M21's aanpak herijkt** (raster-masker is niet meer de juiste vorm). **Open besluit (Lars, bij de pilot):** via-punten op zee-legs opruimen (a) of behouden als hint (b).
- **Zoom-bug bewezen (LAR-479, High):** `updateDetail` (`tiles.js`) breekt af zodra `maxTiles: 40` op is → onderste rijen alleen de grove shell = de kaarsrechte rand op Lars' screenshot. camZ 4,0/5,6/6,5 willen 64–80 tegels → gekapt (**5,6 = startzoom**); elders 36 → niet. Dát zijn de "sweetspots". Twee valse sporen uitgesloten: de "stilstaande tick-loop" was een artefact van de verborgen pane (`document.hidden` → rAF pauzeert; workaround `GLOBE.start()` handmatig), en de patch-centrering klopt wél. **Zonder Lars' screenshot had ik het verkeerde gefixt** (mijn eerste hypothese — mislukte tegels herstellen nooit — is een echte zwakte maar niet de oorzaak; vastgelegd als bijvangst).
- **Linear:** milestone **M18** + **LAR-473..478** (473 spec → **474 pilot koper** → 475 cache-generator → 476 engine → 477 uitrol+via-punten → 478 verificatie) + **LAR-479** (High, tegel-bug) + **LAR-480** (Low, markers-contrast: het is contrast niet schaal — `exp: 0.85` → markers worden bij inzoomen zelfs iets gróter; richting = halo/outline, bewust ná M18+479).
- **Uitkomst:** **géén code gewijzigd** — diagnose/audit + Linear + docs. `searoute` 1.6.0 geïnstalleerd; pilot-artefacten overleefden de rewind (`…/ec6b9a39-…/scratchpad/`). **Volgende sessie = de koper-pilot (LAR-474)**, Lars: *"dan begin ik in een nieuwe sessie met het uitwerken van de eerste grondstof als pilot met de exacte routes."*

## 2026-07-16 (sessie 16) — Backlog leeggewerkt: LAR-471 lab-grown-toggle + LAR-447 recycle-tooltip + LAR-448 PGM-beursvoorraden
- **Taak (Lars):** "kan je even kijken wat er nog in de backlog staat voor de grondstoffen atlas... eerst LAR 471 dan doen we daarna 447 en 448 voordat we iets nieuws oppakken." De backlog bleek klein: **niets meer In Progress/Todo** (alle visuele-bevestiging-issues M8–M17 al op Done), alleen 3 backlog-issues over.
- **LAR-471 · lab-grown-toggle (diamant)** — de bij M16 uitgestelde 6e optionele-laag (na goud-CB/koper-beurs/REE-recycle/olie-reserve/uranium-military). Het `layer:"labgrown"`-patroon (zoals recycle, niet dedicated type): 3 productie-nodes `type:"labgrown"` (China/Henan HPHT, India/Surat CVD, VS/Washington premium-CVD Diamond Foundry) + 6 flows die vooral de **VS-verlovingsringmarkt** ondergraven. 5 engine-plekken (config marker-size / main showLabGrown+hasLabGrown()+usedNodeIds / flows-gate / markers-gate + **violette octaëder-marker** 0xB98BE0 / ui-chip "lab-grown" + TYPE_LABEL). Default uit, chip alleen bij diamant; de `dia-t-labgrown`-tension wijst nu naar de echte lab-grown nodes/flows.
- **LAR-447 · recycle-tooltip per-grondstof** — de gedeelde chip-tooltip was hard-coded REE-bewoord ("magneetschroot, <5%"), fout voor PGM (~25% autokat) en grafiet. Fix via een `recycleHint`-veld op de resource + `main.recycleHint()` + generieke fallback in `ui.js`. Hints op REE/PGM/grafiet.
- **LAR-448 · PGM-beursvoorraden-laag (Lars akkoord)** — PGM's **tweede** optionele toggle naast recycling; pure data, 0 engine-wijziging (hergebruik exchange-toggle). 3 kluis-nodes (LPPM/NYMEX/TOCOM) + 3 `layer:"exchange"`-bufferflows naar de autokat-markten. PGM = eerste grondstof met twee toggles naast elkaar. De issue pleitte er zelf tegen ("één toggle per grondstof") maar Lars koos toch bouwen (Pt/Pd zijn feitelijk beursverhandeld).
- **Verificatie (headless, poort 8732 + verse load 8733):** diamant **41 legs (31 air+10 road) / 0 kapot / 0 straight / 0 degenerate**; lab-grown-toggle uit=35/25 aan=41/28 (+34 scene-meshes). PGM **52 legs / 0 kapot**; exchange-toggle +3/+3; **beide chips (recycling + beursvoorraden) alleen bij PGM**; recycle-tooltip per grondstof correct. Regressievrij (`totalBroken=0`), 0 console-errors. **Cache-gotcha:** de Browser-pane cachet script-tag-files hardnekkig (geen no-cache op python http.server) → engine gevalideerd via in-memory injectie + een tweede server-instance op 8733 (schone origin). `build-standalone.py` +4 checks, `atlas-standalone.html` geregenereerd.
- **Commit + push:** `f6c95f6` (feat 471) + `9feb8f2` (fix 447+448), Claude-trailer, alléén eigen bestanden — **gepusht** (`5d4d469..9feb8f2`) → live op Pages. Linear LAR-471/447/448 → Done. **Backlog nu leeg.**
- **Open:** visuele eindbevestiging op de live URL/mobiel = Lars. Ook gecorrigeerd: stale `next-actions.md`-notitie "M17 kolen nog niet gepusht" (`coal.js` staat al op origin/main).

## 2026-07-16 (sessie 15) — M15 · Gas uitgevoerd (data/gas.js, aardgas/LNG) — de nieuwe 12e grondstof
- **Taak (Lars):** "kan je beginnen met het uitwerken van gas zoals de rest, volgens hetzelfde patroon; als er dingen anders moeten maak daar aparte issues van — eerst oriënteren, de brief volgens template, dan in Linear, dan helemaal uitwerken. Je werkt tegelijk met andere sessies, dus let op." Gas zit **niet in de basis-10** → nieuwe grondstof (zoals zilver/diamant/kolen). Milestones t/m M14 → gas = **M15** (kolen koos aanvankelijk óók M15 → hernummerd Gas=M15/Diamant=M16/Kolen=M17).
- **De vorm (het aha) = de natuurkunde: gas is nauwelijks te verplaatsen.** Twee gescheiden leversystemen op de kaart: lage donkere **pijpleiding-arcs** (captive/regionaal — Rusland↔Europa was, Power of Siberia→China, Turkmenistan→China captive, Noorwegen→EU #1-ná-Rusland, Zuidelijke Gascorridor) náást heldere **LNG-oceaan-arcs** (globaal). **De liquefactie-stap is de trechter** (institutioneel/kapitaal, geen zeestraat): pas ná vloeibaarmaking (−162 °C) is een molecuul een omleidbare wereldgrondstof; capaciteit bij **drie polen VS-Golfkust/Qatar/Australië**. Gas' equivalent van de China-raffinage bij lithium.
- **Techniek:** stages als leversysteem-onderscheid: `erts` = veldgas + pijpleidinggas (blijft erts tot de markt) → `raffinaat` = **LNG** (de oceaan-arcs = het verhaal) → `product` = hervergast/geleverd. Liquefactie=`refinery`, regas=`port`, opslag=`reserve` → **géén nieuwe marker-types/render-modus/chokepoint** (4e na nikkel/olie/zilver op de bestaande routekaart). Schip + `pipeline` (beide bestaan). 6 tensions: Hormuz-afhankelijkheid (scherper dan olie — géén Yanbu/Fujairah-bypass), liquefactie-flessenhals, Europa-pivot 2022 (Nord Stream→LNG+FSRU's, TTF-piek), Russische oost-pivot (Power of Siberia + Arctisch LNG), drie prijszones (Henry Hub«TTF«JKM), Panama-LNG-knelpunt. Iran = reserves≠export (zelfde veld als Qatar).
- **Opslag-laag = hergebruik van de olie-SPR-`reserve`-toggle met 0 engine-wijziging** (`hasReserves()` generiek op `n.type==="reserve"`, `src/main.js:23`): 4 reserve-nodes (EU Rehden/Bergermeer, Oekraïne-caverns, US Henry Hub, China) + 5 vul-flows; EU-winter-vulgraad (90%-mandaat) = gas' geopolitieke metric na 2022.
- **Verificatie (headless, eigen server poort 8736):** gas **97 legs / 0 kapot / 0 straight (>200km) / 0 onbekende via-ids / 0 bad-refs**, regressievrij (0 kapot over alle 14 grondstoffen). **Géén route-bugs** — de 2 Arctische Yamal-routes (Barentszzee 107 pts + Noordelijke Zeeroute 255 pts), de Med-crossing (Arzew→Spanje) en de lange captive-pijpleidingen routeren allemaal correct zonder nieuw vaarpunt (empirisch bevestigd). Reserve-toggle-data correct; geen console-warnings; gas activeert als UI-band. Build groen (5 gas-checks OK).
- **Coördinatie (sectie J — 4 parallelle sessies grafiet/kolen/diamant/gas):** **git-index-race** — tussen mijn `git add` en `git commit` stagede de diamant-sessie háár bestanden in de gedeelde index → mijn eerste commit veegde `diamond.js`+`diamant.md` mee. Teruggedraaid (`reset --soft` + `restore --staged` + **`commit --only`**) → diamant's bestanden terug naar untracked, mijn commit alléén gas. **Les:** bij een gedeelde working tree is `git commit <paths>`/`--only` veiliger dan `git add` + kale `commit`. Commits `040d2b7` (gas.js+gas.md) + `a8378ef` (build-checks), **gepusht → live op Pages**.
- **Open:** visuele bevestiging op de live URL/mobiel (LAR-465, Lars).

## 2026-07-16 (sessie 14) — M16 · Diamant uitgevoerd (data/diamond.js, de scherpste downstream-trechter) — de nieuwe 12e grondstof
- **Taak (Lars):** "kan je beginnen met het uitwerken van diamant zoals de rest, volgens hetzelfde patroon; als er dingen anders moeten maak daar aparte issues van — eerst oriënteren, de brief volgens template, dan in Linear, dan helemaal uitwerken. Je werkt tegelijk met andere sessies, dus let op." Diamant zit **niet in de basis-10** → nieuwe grondstof (zoals zilver/gas). M15 was door gas bezet → diamant = **M16**.
- **De vorm (het aha):** **de scherpste DOWNSTREAM-trechter van de atlas.** Winning verspreid (Rusland/Alrosa #1 op **volume**, Botswana/Debswana #1 op **waarde**, Canada, Angola, Zuid-Afrika, Zimbabwe, Namibië-marien, Lesotho; **Argyle gesloten 2020** = schaarste-verhaal), maar **~90-95% van álle diamant geslepen/gepolijst in één stad: Surat (Gujarat)** — scherper nog dan de China-raffinage of Ganzhou-scheiding. **Antwerpen** = het verplichte **G7-certificeringsknooppunt** (sanctie op Russische/Alrosa diamant, maart 2024) → fysieke omweg mijn→Antwerpen→Surat, terwijl de **Alrosa-rough zichtbaar om Antwerpen heen buigt** via Dubai/direct India. De Beers-sights via Gaborone.
- **Techniek:** diamant **vlíégt** → **hergebruik van de goud/PGM air-mode** (`mode:"air"`), **0 engine-wijziging, géén nieuw chokepoint, géén nieuwe marker-types** (`hub`=handelshubs, `refinery`=slijperij). Korte hops binnen een land = `road`. Keten 3 stages (erts=rough → raffinaat=polished bij Surat → product=sieraad; VS #1 ~50%). 6 tensions: Surat-trechter, De Beers/Alrosa-duopolie, Antwerpen-certificering, Alrosa/G7-sanctie, lab-grown-ontwrichting, waarde-vs-volume + Botswana-beneficiation.
- **Twee "anders"-punten → aparte issues:** LAR-470 (nieuwe-12e-grondstof-plumbing, zoals zilvers LAR-436) + de **lab-grown-toggle** (LAR-471, `layer:"labgrown"`, 5 engine-bestanden) **bewust in de backlog** i.v.m. de parallelle sessies (zoals uranium's LAR-414 / olie's LAR-432); in v1 leeft lab-grown als `tension`.
- **Verificatie (headless, poort 8734):** diamant **35 legs (27 air + 8 road) / 0 kapot / 0 straight / 0 degenerate**, 0 warnings; blurb + 6 tensions renderen; regressievrij (0 engine-wijziging). 1 kust-artefact-landhop (Dubai→Golf) → `air` voor 0 straight. Build groen (4 diamant-checks OK).
- **Coördinatie (sectie J — 4 parallelle sessies grafiet/kolen/gas/diamant):** race geraakt (mijn gestagede bestanden éénmaal meegeveegd in gas' brede `git add`, daarna bij rebase M15→M17 weer untracked; inhoud intact, geen historie herschreven). Toen Lars zei "je kan hem helemaal afmaken, de sessies wachten": twee schone commits `72d134c` (feat) + `7d06a0c` (build; de meeliftende gas.js-tag verwees al naar de gecommitte gas.js → consistent). **Gepusht** (`8497f24..7d06a0c`, fast-forward, alléén eigen commits) → live op Pages.
- **Open:** visuele bevestiging op de live URL/mobiel (LAR-472, Lars) + de uitgestelde lab-grown-toggle (LAR-471) zodra de engine-tree schoon is.

## 2026-07-16 (sessie 13) — M17 · Kolen uitgevoerd (data/coal.js, de binnenlands-grondstof) — de nieuwe 14e grondstof
- **Taak (Lars):** "kan je beginnen met het uitwerken van kolen zoals de rest, volgens hetzelfde patroon; als er dingen anders moeten maak daar aparte issues van — eerst oriënteren, de brief volgens template, dan in Linear, dan helemaal uitwerken. Je werkt tegelijk met andere sessies, dus let op." Kolen zit **niet in de basis-10** → net als zilver (M13) een **nieuwe grondstof**. Milestones liepen t/m M14 → kolen = **M17**.
- **De vorm (het aha):** **de binnenlandsheid, géén trechter.** Waar elke andere grondstof ergens knijpt (raffinage/Zwitserland/verrijking/zeestraten-net/bijproduct-vraag), heeft kolen **géén enkele mondiale flessenhals** omdat het overweldigend binnenlands is: ~85% wordt verbrand waar gedolven (China ~50% van de wereld, India, VS, Rusland delven+verstoken thuis), slechts ~15% van de ~8.700 Mt gaat over zee. De kaart: grote binnenlandse blokken (mijn→centrale) tegenover een dunnere, geopolitiek beladen zeehandelslaag. **China = swing-koper** (grootste producent én importeur). **Twee kolen:** thermisch→stroom vs. cokeskool→staal.
- **Gebouwd:** nieuw `data/coal.js` (34 nodes / 33 flows / 6 tensions) + brief `design/kolen.md` + `<script src="data/coal.js">` in `index.html` + `grens-gashuunsukhait` (Mongolië-Gobi) in `_chokepoints.js` + 5 kolen-checks in `build-standalone.py`. Stages als ketenpositie: `erts` = mijn→haven/centrale · `raffinaat` = de internationaal verhandelde bulk (de zeekruisingen + de landcorridor, waar élk ban/her-routeringsverhaal leeft) · `product` = stroom/staal. Zo leest binnenlandse kolen (alleen erts+product) visueel anders dan verhandelde (mét de heldere raffinaat-zeeboog). Drie her-routeringen als tensions: China-Australië-ban (2020-2023), Rusland-oost-draai (2022→), Mongolië-Gobi-corridor.
- **Maximaal hergebruik, 0 engine-wijziging:** schip+land, **géén nieuwe render-modus, géén nieuwe marker-types** (alleen mine/port/market), **géén optionele toggle-laag** (kolen heeft geen zinvol CB/beurs/recycling-equivalent). Het grondstof-eigen "nieuwe element" = **één LANDknelpunt** `grens-gashuunsukhait` (Tavan-Tolgoi-cokeskool over de Gobi → Chinees staal), exact het Kasumbalesa/Ruili-patroon. Kolen = 4e grondstof (na nikkel/olie/zilver) zonder nieuw ZEE-knelpunt.
- **Verificatie (headless, poort 8735 = eigen `-4`-server):** kolen **111 legs / 0 kapot / 0 straight / 0 degen / 0 unresolved via**; regressie schoon (alle 12 grondstoffen op baseline). Route-bug empirisch gefixt (zilver-Tacoma→Astoria-precedent): de 2 kapotte legs zaten op de Canadese haven — **Roberts Bank ligt ingesloten in de Salish Sea** (valt dicht in het grove raster, robertsbank→open zee = null) → verplaatst naar **Ridley/Prince Rupert** (open kust; feitelijk óók dé Canadese cokeskool-exporthaven). `atlas-standalone.html` geregenereerd (5 kolen-checks OK). WebGL-screenshot hangt headless → visuele bevestiging = Lars.
- **Coördinatie (sectie J — het scherpst tot nu toe, 3 parallelle sessies):** naast grafiet (mid-wrapup) bleken óók **diamant** (`data/diamond.js`) en **gas** (`design/gas.md`+`data/gas.js`) actief. Alléén eigen bestanden gecommit (`75c3483`): `data/coal.js`, `design/kolen.md`, `data/_chokepoints.js` (eigen COAL-blok), `build-standalone.py` (eigen checks), + **alléén de coal-regel** uit de gedeelde `index.html` (drie sessies voegden daar diamond/coal/gas toe in één hunk → gerichte `git apply --cached`-patch die alleen mijn regel staged; werkboom intact, diamant/gas-regels ongestaged). `launch.json` + de untracked diamant/gas-bestanden ongemoeid.
- **Afgerond:** Linear **M17 · Kolen** + LAR-455..459, 461 (455/456 research + 457 plumbing + 458 chokepoint + 459 data = Done; 461 verificatie ✅ + visuele bevestiging = In Progress). De atlas telt nu **14 grondstoffen** (basis-10 + zilver + gas M15 + diamant M16 + kolen M17; gas/diamant lopen parallel).

## 2026-07-15 (sessie 12) — M14 · Grafiet uitgevoerd (data/graphite.js, de anode-verwerkingstrechter) — het LAATSTE basis-10-bestand
- **Taak (Lars):** "kan je grafiet uitwerken van de grondstoffen atlas" — met de heads-up dat **parallelle sessies andere grondstoffen uitwerken** (opletten bij committen, "ging de vorige keer ook goed") en dat er "een korte omschrijving is van hoe je te werk gaat" = het runbook (sectie I) + de parallel-regels (sectie J) in de project-`CLAUDE.md`.
- **De vorm (het aha):** een **REE-achtige verwerkingstrechter met TWEE feedstocks**. Grafiet is HET anodemateriaal in Li-ionbatterijen (grootste celcomponent naar massa, ~1 kg/kWh). **Natuurlijk vlokgrafiet** (China #1 ~65%, Balama/Mozambique, Molo/Madagascar, Minas Gerais/Brazilië, Mahenge/Tanzania, + Skaland/Noorwegen, Zavallya/Oekraïne, Sri Lanka vein) én **synthetisch grafiet** (uit petroleum-**naaldcokes**, gegrafitiseerd bij ~3000 °C) convergeren op de anode-verwerking die **~90%+ in China** zit — Shandong (natuurlijk) + Binnen-Mongolië (synthetisch). **Zelfs ex-China vlok vaart naar China.** Levende geopolitiek: de **China-exportvergunningen op grafiet (dec 2023)**.
- **Gebouwd:** `data/graphite.js` van "basis" (10/3) → **uitgewerkt** (31 nodes / 26 flows / 6 tensions) + brief `design/grafiet.md` + 5 grafiet-checks in `build-standalone.py`. Keten `erts` (vlok + naaldcokes) → `raffinaat` (gecoat sferisch/gegrafitiseerd anodepoeder, de China-trechter) → `product` (batterijcellen/gigafabrieken). Dunne ex-China buildout: Syrah Vidalia (Louisiana, uit Balama-vlok, IRA-FEOC) + Talga/Novonix/NMG/POSCO. Grafiet was het **laatste basis-10-bestand** (bestond al + stond al in `index.html` → basis→uitgewerkt, géén nieuwe script-tag, anders dan zilver/M13).
- **Maximaal hergebruik, 0 engine-wijziging:** schip+land, **géén nieuwe render-modus, géén nieuw chokepoint** (4e na nikkel/olie/zilver op de bestaande routekaart). **Recycling-toggle** (`layer:"recycle"`, default uit, bescheiden) = hergebruik van het REE/PGM-patroon met 0 engine-wijziging; chip via `hasRecycle()` verschijnt automatisch.
- **Verificatie (headless, poort 8735 — eigen `-4`-server naast de parallelle sessies):** grafiet **77 legs (57 zee + 20 land) / 0 kapot / 0 straight / 0 warnings**; toggle aan = 80 legs (+3 recycle); regressie schoon (0 kapot over álle grondstoffen). De verse schijf-data via synchrone fetch + `REGISTER`-capture door de exacte `flows.js`-routing gehaald (de Browser-pane cachete de oude `graphite.js` hardnekkig — pane-cache, geen codeprobleem); live app: blurb + recycling-chip + 6 tensions renderen, geen console-warnings. Route-bug gefixt: `gr-ref-japan→gr-mkt-korea-japan` road→ship (Japan→Korea over de Straat van Korea). `atlas-standalone.html` geregenereerd (5 grafiet-checks OK).
- **Coördinatie (sectie J):** werktree schoon bij start én vóór commit; grafiet raakt de engine niet (0 engine-wijziging) → alléén eigen bestanden gestaged (`data/graphite.js`, `design/grafiet.md`, `build-standalone.py`, `.claude/launch.json`). **Discrepantie gecorrigeerd:** de docs zeiden "repo lokaal-only", maar de repo is sinds M13 live op GitHub Pages → deze sessie **wél gepusht** (code `34b1ed4` + docs).
- **Afgerond:** Linear **M14 · Grafiet** + LAR-449..454 (449–453 Done, 454 In Progress = visuele bevestiging Lars). **Grafiet was het laatste basis-10-bestand → alle 11 grondstoffen nu uitgewerkt; de atlas is inhoudelijk compleet.**

## 2026-07-15 (sessie 11) — M12 · PGM uitgevoerd (data/pgm.js, twee landen/twee metalen + luchtvracht)
- **Taak (Lars):** "begin met het uitwerken van PMG voor de grondstoffen atlas zoals de rest ook is uitgewerkt en volgens hetzelfde patroon … als er dingen anders moeten maak daar dan aparte issues van." PMG = **PGM** (platinagroepmetalen); runbook sectie I gevolgd, **goud** als model (luchtvracht).
- **De vorm (het aha):** de scherpste twee-landen-concentratie van de atlas, gesplitst over **twee metalen**: **Zuid-Afrika/Bushveld** (~70% Pt + ~80% Rh, dichte kluwen schachtmijnen bij Rustenburg + Noord-/Oostrand) en **Rusland/Norilsk** (~40% Pd, Ni-Cu-bijproduct). Een schok in het ene land raakt een *ander* metaal dan een schok in het andere.
- **Gebouwd:** `data/pgm.js` van "basis" (9/3) → **uitgewerkt** (38 nodes / 41 flows / 6 tensions) + brief `design/pgm.md`. Keten `erts` (concentraat/matte, land) → `raffinaat` (geraffineerd metaal, **lucht**) → `product` (autokat/brandstofcel/sieraad/industrie). 6 tensions: twee-landen-concentratie, autokat-leiband + Pt↔Pd-substitutie, rodium-spof (~$29k/oz 2021), palladium/Rusland-sanctie, waterstof-hedge (Pt/Ir PEM-elektrolyse), Eskom-stroomcrisis.
- **Maximaal hergebruik, 0 engine-wijziging:** PGM **vliegt** (per kilo even waardevol als goud) → hergebruik van de **goud-air-mode** (`mode:"air"`, JNB-gateway; tijdlijn toont automatisch "✈ vluchten" via `activeHasAir()`); concentraat/matte over land. **Géén nieuw chokepoint** (derde na koper/nikkel). **Recycling** (~25%, autokat via dezelfde westerse huizen JM/BASF/Umicore/Heraeus/Tanaka) als **optionele toggle** (`layer:"recycle"`, hergebruik van het REE-patroon, 0 engine-wijziging; chip via `hasRecycle()`).
- **Verificatie (headless, poort 8732):** pgm **49 legs / 0 kapot / 0 straight / 0 degenerate arcs**, regressievrij; de lange risico-legs (Zimbabwe→ZA via Beitbridge, Norilsk→Krasnoyarsk, Kevitsa→Umicore om de Oostzee, VK→EU via de Kanaaltunnel) routeren correct; één SAMECELL-collision (Japan-recycler in Tokyo Bay → snapte naar Tanaka's cel) gefixt door de node naar Kanagawa te verplaatsen. Recycle-toggle (36→41 flows) + air-voyage-noun bevestigd.
- **Afwijkingen → aparte issues (op Lars' verzoek):** LAR-446 (single-file build + `atlas-standalone.html` regenereren, tijdelijk uitgesteld i.v.m. de parallelle zilver-sessie → **nu Done**), LAR-447 (recycling-chip-tooltip nog REE-bewoord "<5%", onjuist voor PGM ~25%, raakt `ui.js`), LAR-448 (optionele Pt/Pd-exchange-laag — pure data, bewust niet gebouwd; één toggle per grondstof).
- **Coördinatie (sectie J):** gebouwd náást de parallelle **M13-zilver-sessie** (+ een uranium-toggle-sessie) die de gedeelde `build-standalone.py`/`index.html`/`config.js` dirty hadden. PGM raakt geen engine-bestanden → alleen `data/pgm.js` + `design/pgm.md` gecommit (`2c4b668`); de build + `now.md`/project-sync bewust uitgesteld tot de tree schoon was, daarna afgemaakt.
- **Afgerond:** Linear **M12 · PGM** + LAR-440..448 (5 Done + 445 In Progress = visuele bevestiging Lars; 446 Done na de build; 447/448 Backlog). Vault-wrapup gepusht (`278dddd` conflictvrije delen + deze sync). **Rest = visuele bevestiging Netlify/mobiel (LAR-445, Lars).**

## 2026-07-15 (sessie 10) — M13 · Zilver uitgevoerd (data/silver.js, de eerste écht nieuwe grondstof)
- **Taak (Lars):** "begin met het uitwerken van zilver voor de grondstoffen atlas zoals de rest, volgens hetzelfde patroon; als er dingen anders moeten maak daar aparte issues van — oriënteren, de brief, milestone in Linear, daarna uitvoeren." Runbook sectie I gevolgd; in één sessie gebouwd + geverifieerd + wrapup.
- **Het grote verschil:** zilver is de **eerste écht nieuwe grondstof** sinds de basis-10 (niet basis→uitgewerkt). Nieuw `data/silver.js` (42 nodes / 37 flows / 6 tensions) + brief `design/zilver.md` + `<script src="data/silver.js">` in `index.html` + 5 zilver-checks in `build-standalone.py`. Dit "anders"-punt bewust als eigen Linear-issue (LAR-436).
- **De vorm (het aha) — fundamenteel anders:** zilver heeft géén enkel geografisch knelpunt. De knijp is tweezijdig en structureel: (1) **aanbod-inelasticiteit** — ~70-75% is **bijproduct** van zink/lood/koper/goud (Mexico #1, Peru, China, KGHM-koper Polen, Chili, Australië, Bolivia, Kazachstan; mijn-nodes = eigenlijk andermans mijnen); (2) **vraagconcentratie** — de energietransitie trekt zilver naar de **Chinese zonnepanelen-industrie** (fotovoltaïsch = grootste + snelst groeiende toepassing). Resultaat: meerjarig **structureel tekort** dat de kluisvoorraden (LBMA/COMEX/SGE) aftapt.
- **Gebouwd:** keten erts(mijn-doré/concentraat)→raffinaat(good-delivery baar)→product(solar/elektronica/sieraad); schip+land, **géén nieuw chokepoint** (derde na nikkel/olie), géén nieuwe marker-types/render-modus. Mexico als winning+raffinage-anker (Fresnillo grootste primaire producent + Peñoles/Torreón grootste raffinaderij). 6 tensions: bijproduct-paradox, solar-pull, structureel tekort, Mexico-anker, COMEX/LBMA registered-vs-eligible + 2021-squeeze, "geen winnings-knelpunt maar een vraagconcentratie".
- **Kluis-/beursvoorraden-laag** = hergebruik van de bestaande exchange-toggle met **0 engine-wijziging** (nikkel-patroon, 2e datagedreven hergebruik): 3 exchange-nodes (LBMA/COMEX/SGE) + 3 `layer:"exchange"`-aftap-flows. Recycling always-on (~15-18%).
- **Verificatie (headless, eigen server poort 8734):** zilver **85 legs / 0 kapot / 0 straight / 0 warnings**; regressie schoon (andere uitgewerkte grondstoffen 0/0). 2 route-bugs empirisch gefixt (VS-raffinage Tacoma→Astoria open kust; China-solar Suzhou-binnenland→Jiangsu-kust). Exchange-chip "beursvoorraden" verschijnt + blurb + 6 tensions renderen. `atlas-standalone.html` geregenereerd (5 zilver-checks OK; gitignored).
- **Coördinatie (sectie J):** gebouwd náást een parallelle sessie die aan uranium's engine-laag werkte op de gedeelde bestanden (`config.js`/`src/{flows,main,markers,ui}.js`/`data/uranium.js`, dirty). Zilver raakt de engine niet (0 engine-wijziging) → alléén eigen bestanden gestaged; ik wrapte als eerste (de uranium-sessie was nog niet gewrapt).
- **Afgerond:** code-commit `e091848` (Claude-trailer, alleen eigen bestanden). Linear **M13 · Zilver** + LAR-434..439 (434–438 Done, 439 In Progress = visuele bevestiging Lars). M12 bleek al PGM (parallelle sessie) → zilver werd M13. Pinecone-gist opgeslagen. Rest = visuele bevestiging Netlify/mobiel (Lars).

## 2026-07-15 (sessie 9, vervolg) — M11 · Olie compleet: SPR-voorraden-toggle gebouwd
- **Trigger (Lars):** "nikkel is klaar dus jij kan hem afmaken … en de voorraden bij olie is een goed idee" → de bewust uitgestelde SPR-toggle (LAR-432) alsnog gebouwd nu de gedeelde engine-bestanden vrij zijn.
- **Gebouwd:** het **vierde** optionele-laag-patroon (`layer:"reserve"` / `type:"reserve"`, `filters.showReserves`), exact het koper-`exchange`-patroon op 5 plekken (config/main/flows/markers/ui) + een olie-amber tank-marker. `data/oil.js`: 5 SPR-nodes (US Gulf ~350 / China Dalian ~300 / Japan Kiire ~130 / India Mangalore ~40 / IEA-EU Le Havre ~90 mln vaten) + 5 vul-flows + tension `oil-t-spr`.
- **Geverifieerd (headless, poort 8734):** olie **232 legs (incl. reserve) / 0 kapot / 0 straight**; toggle uit=45 nodes/46 flows, aan=50/51 (exact +5/+5); chip "voorraden" verschijnt alleen bij olie en toggelt schoon (uit→aan→uit, 0 console-errors); `hasReserves()` alleen true voor olie; regressie ongewijzigd. `atlas-standalone.html` geregenereerd (+ 2 reserve-checks, groen) + zelf geverifieerd.
- **Afgerond:** commit `86c8c1f` (Claude-trailer, alleen eigen 7 bestanden). **Linear LAR-432 → Done.** Olie is nu volledig compleet (data + optionele laag), gelijk aan goud/koper/REE. Rest = visuele bevestiging Netlify/mobiel (LAR-433, Lars).

## 2026-07-15 (sessie 9) — M11 · Olie uitgevoerd (data/oil.js, het knelpunten-netwerk licht op)
- **Taak (Lars):** "begin met het uitwerken van olie voor de grondstoffen atlas zoals we de rest ook gedaan hebben" → runbook sectie I gevolgd (uranium/koper = dichtstbijzijnde modellen). In één sessie gebouwd + geverifieerd + wrapup.
- **Gebouwd:** `data/oil.js` van "basis" (18 nodes/15 flows) → **uitgewerkt** (45 nodes / 46 flows / 6 tensions) + brief `design/olie.md` + 4 olie-sanity-checks in `build-standalone.py`. 14 mijnen + 14 export-terminals + 9 raffinaderijen + 8 markten (4 verbruik + 4 petrochemie). Stages: 35 erts (crude) / 6 raffinaat (product-trade) / 5 product (petrochemie). Modi: 41 tanker + 5 pijpleiding.
- **De vorm van olie (het aha):** bewust anders dan alle eerdere — geen enkele trechter maar het **hele knelpunten-netwerk dat tegelijk oplicht**. Data bevestigt: Hormuz #1 (15 stromen), Malakka (14), Taiwan (12), + Gibraltar/Suez/Bab/Kaap/Bosporus/Deense-Straten = 10 knelpunten. Daarom **géén nieuw chokepoint**; wel 3 olie-only navigatie-vaarpunten (`wp-golf-mexico`/`wp-florida`/`wp-caribisch`).
- **Drie levende verhalen:** Hormuz-bypass-pijpleidingen (Yanbu/Fujairah), Rusland-omleiding 2022→ (Primorsk/Novorossiysk/ESPO-Kozmino/Druzhba → India/China), Amerikaanse schalie-ommekeer (Corpus Christi export). Schip+pijpleiding, géén nieuwe render-modus. Kust-raffinaderijen `coastal:true`.
- **Verificatie (headless, eigen server poort 8734):** olie **210 legs / 0 kapot / 0 straight**; regressie schoon (globale baseline 5 = lithium 4 + goud 1, olie voegt 0 toe). Statische Node-check vooraf (id-resolutie) + browser-legs-check (Routing.sea/land) + zelf-check op de standalone-build. `atlas-standalone.html` geregenereerd (1608 KB, alle checks groen).
- **SPR-voorraden-toggle bewust uitgesteld** (LAR-432 Backlog): raakt de gedeelde engine-bestanden terwijl een **parallelle M10-nikkel-sessie** live was (dev-servers op 8732/8733 + concurrent vault-/memory-writes). Sectie J regel 5 gevolgd: op nikkel's wrapup gewacht vóór de eigen vault/memory-sync, om niets te clobberen.
- **Afgerond:** code-commit `1d4ece5` (Claude-trailer, alleen eigen bestanden). Linear **M11 · Olie** + LAR-428..433 (4 Done, 432 Backlog, 433 In Progress). Pinecone-gist opgeslagen. Rest = visuele bevestiging Netlify/mobiel (Lars).

## 2026-07-15 (sessie 8) — M10 · Nikkel uitgevoerd (data/nickel.js, Indonesië-onshoring-trechter)
- **Taak (Lars):** "werk nikkel uit voor de grondstoffen atlas zoals de rest, volgens hetzelfde patroon" → runbook sectie I gevolgd (koper = dichtstbijzijnde model). In één sessie gebouwd + geverifieerd + wrapup.
- **Gebouwd:** `data/nickel.js` van "basis" (13 nodes/4 flows) → **uitgewerkt** (50 nodes / 46 flows / 6 tensions) + brief `design/nikkel.md` + 3 nikkel-sanity-checks in `build-standalone.py`. Stages erts (ruw lateriet/sulfide) → raffinaat (NPI/ferronikkel/matte/MHP/class-1/sulfaat) → product (roestvrij staal + batterijkathode); schip+land, géén nieuwe render-modus.
- **De nikkel-"aha" — de trechter staat op z'n kop t.o.v. koper:** waar koper/lithium breed graven en in China raffineren, heeft **Indonesië in tien jaar de mijn ÉN de raffinage** naar zich toe getrokken via de **exportban op ruw erts** (2014 deels, 2020 volledig), met Chinees kapitaal (Tsingshan/Huayou) in de parken IMIP (Morowali) en IWIP (Weda Bay). Het erts blíjft in het land: korte hops mijn→smelter, pas als NPI/matte/MHP de zee op.
- **Vier tensions dragen het verhaal:** (1) Indonesië-onshoring (mijn+raffinage); (2) twee nikkels — class-1 (batterij/sulfaat) vs class-2 (roestvrij/NPI), met HPAL→MHP en matte als brug; (3) prijscrash-shakeout (BHP Nickel West stilgelegd 2024 = node als project/stilgelegd zonder exportstroom, Nieuw-Caledonië in crisis); (4) LME-nuance (alleen class-1 leverbaar → prijs los van de fysieke markt, de 2022-squeeze). Het contrast: de Filipijnen exporteren nog wél ruw lateriet naar China (geen ban).
- **Géén nieuw chokepoint** (tweede na koper die volledig op de bestaande routekaart draait): Makassar/Lombok/SCS/Taiwan, Deense Straten, Panama + Pacific-vaarpunten, de Saint-Laurent-keten. **Beursvoorraden-laag (LME)** hergebruikt de bestaande exchange-toggle van koper met **0 engine-wijziging** (bevestigd generiek: `hasExchangeStocks()` + gate + marker + chip op `type/layer==="exchange"`); 4 LME-nodes + 5 `layer:"exchange"`-flows, alleen class-1-bronnen leveren erin. Recycling always-on (koper-patroon). Coastal-markten (koper-fix) zodat elke ship-leg op een kustpunt landt.
- **Verificatie headless** (draaiende atlas, eigen server poort 8733 want de parallelle olie-sessie bezette 8732): nikkel **91 legs (63 zee + 18 land + 10 korte cluster-hops) / 0 kapot / 0 straight**. De 10 "korte hops" = intra-cluster mijn→smelter-legs (~30–65 km, endpoints-only) — dezelfde categorie die de runbook bij koper(7)/REE(6) als "0 kapot" telt; met afstandsdrempel (>1,2°) getoetst: 0 echt-kapot. Regressie schoon: 0 kapot over álle grondstoffen (`broken:[]`); de 21 resterende straight zitten volledig in grafiet/PGM/olie (nog op basis), nikkel voegt 0 toe. Geen REGISTER-warnings; exchange-toggle vuurt generiek. `atlas-standalone.html` geregenereerd (nikkel-checks OK). WebGL-screenshot lukt niet headless → visueel = Lars.
- **Parallelle sessie:** een andere chat werkte aan olie (`data/oil.js`/`design/olie.md`/`_chokepoints.js` dirty). Per sectie J alleen mijn eigen 3 bestanden gestaged (nooit `git add -A`). **Commit `08aa4f5`** (repo `main`, lokaal-only, Claude-trailer).
- **Linear:** milestone M10 · Nikkel + LAR-422..427 aangemaakt (422/423 research, 424 data-file, 425 beursvoorraden=hergebruik exchange-toggle, 426 verificatie+build → Done; 427 visuele bevestiging Netlify/mobiel → In Progress).
- **Status:** M10 gebouwd + geverifieerd + gecommit. **Open:** visuele bevestiging Netlify/mobiel (LAR-427, Lars) + vault-push (faalde op netwerkfout, lokaal gecommit). Volgende grondstof: grafiet, PGM (olie parallel).

## 2026-07-15 (sessie 7) — M8 · Zeldzame aardmetalen (magneet-REE) uitgevoerd (data/rare-earths.js + grens-ruili + recycling-toggle)
- **Taak (Lars):** "waar waren we?" op de atlas → M8 was de openstaande bouwklus (alleen op papier voorbereid; uranium M9 al af). Opdracht: M8 **helemaal uitwerken + afronden met wrapup**, "vraag bij twijfel". Geen blokkerende twijfels → in één sessie gebouwd + geverifieerd.
- **Gebouwd:** `data/rare-earths.js` van "basis" (9/5) → **uitgewerkt** (41 nodes / 38 flows / 6 tensions), **magneet-REE-framing** (optie 2 uit het skelet): `id` blijft `rare-earths`, `name` "Zeldzame aardmetalen (magneet-REE)", `symbol` `NdPr`, `unit` "kt magneet-REO/jaar". Stages erts (concentraat/ionklei) → raffinaat (NdPr/Dy-oxide) → product (NdFeB-magneet); schip+land, géén nieuwe render-modus.
- **Vier kern-aha's renderen:** (1) **Ganzhou-scheidingstrechter** ~85–90% Zuid-China (ionklei + Kachin + Mountain-Pass-concentraat convergeren) = de REE-Ticino, extreemste trechter van de atlas; (2) **Dy/Tb-landstroom Myanmar→China** over de nieuwe grenscorridor `grens-ruili` (Kachin → Ganzhou); (3) **Mountain-Pass-rondreis** (concentraat heen over de Stille Oceaan, oxide terug naar Fort Worth, gepland); (4) **NdFeB-magneet-waaier** vanuit Ningbo naar EU (Suez)/VS (Pacific)/Japan/Korea/China = de 2025-exporthefboom. Plus het dunne niet-Chinese Lynas-draadje (Mount Weld→Kuantan→Japan/VAC) + EU-draadje (Silmet/La Rochelle→VAC).
- **Nieuwe grenscorridor `grens-ruili`** (24.02, 97.85; Myanmar→China) in `_chokepoints.js`, `kind:"grensovergang"` = exact het Kasumbalesa-patroon (landpunt, houdt de landkaart open). Enige nieuwe knelpunt; alleen REE gebruikt het.
- **Recycling-toggle** (`layer:"recycle"`, default uit) = het **derde optionele-laag-patroon** (goud=CB, koper=beurs, REE=recycling). Bewust via `layer:"recycle"` op flows **én** recycler-nodes: node-gate op `node.layer==="recycle"` (niet op `type==="recycler"`) + `hasRecycle()` op `f.layer==="recycle"`, zodat **koper's always-on recyclers** (geen `layer`) ongemoeid blijven en alleen REE de chip krijgt. 5 plekken: config/main/flows/markers/ui.
- **5 co-located nodes ~30–45 km verschoven** (Baotou/Ganzhou ref+mag, MP mijn+scheiding, La Rochelle ref+recycler, Fort Worth mag+recycler): zaten in dezelfde 0,25°-rastercel → 1-punts route (`degDist:0`, onzichtbare arc). Verschoven binnen dezelfde stad zodat de lokale scheiding→magneet-arcs zichtbaar renderen én de teller schoon op 0 komt.
- **Verificatie headless** (draaiende atlas, poort 8732): rare-earths **90 legs (39 land + 51 zee) / 0 kapot / 0 straight**. Structuur groen (41/38/6, geen dubbele ids, geen onbekende endpoints, `grens-ruili` resolvet). Regressie schoon: globaal 5 kapot = bekende `degDist:0` lithium(4)+goud(1)-baseline (0 nieuw), 25 straight = de basis-grondstoffen. Toggle-test: aan → +3 recycle-flows + 3 recycler-nodes; uit → weg; 4e (MP, project) extra project-gated; cb/beurs blijven weg. Visueel in de browser-pane bevestigd (Ganzhou-trechter/NdFeB-waaier/Mountain-Pass-route/EU-Suez renderen). WebGL-full-screenshot lukt niet headless → visueel = Lars (LAR-421).
- **build-standalone.py** uitgebreid met REE-sanity-checks; `atlas-standalone.html` geregenereerd (alle checks OK).
- **Linear:** LAR-416..420 → Done, LAR-421 → In Progress (headless done, Netlify/mobiel = Lars), zoals uranium LAR-415.
- **Commit:** repo lokaal-only (geen remote), branch `main`, Claude-trailer (code + wrapup-docs).
- **Status:** M8 gebouwd + geverifieerd. **Open:** visuele bevestiging Netlify/mobiel (LAR-421, Lars). Volgende grondstof: nikkel (runner-up), grafiet, PGM, olie.

## 2026-07-15 (sessie 6) — M9 · Uranium uitgevoerd (data/uranium.js + Kaspische oversteek)
- **Taak (Lars):** nieuwe grondstof voorbereiden + committen "in dezelfde stijl", keuze aan mij → daarna ook echt uitwerken (data-file) + Linear-milestone/issues + wrapup.
- **Gekozen: uranium** (niet nikkel, de runner-up). Reden: de meest *distinctieve nieuwe vorm* — een **4-staps kernbrandstofketen** met de knijp twee stappen downstream in een vijandige staat + twee landlocked-routes, i.p.v. nóg een China-processing-trechter. Eerst het ontwerp-skelet `design/uranium.md` (commit `d016ab8`), daarna de bouw.
- **Gebouwd:** `data/uranium.js` van "basis" (9/2) → **uitgewerkt** (38 nodes / 36 flows / 6 tensions). De 4 stappen op de 3 bestaande stages: `erts` = winning + conversie (feed) · `raffinaat` = **verrijking (de flessenhals, ~44% Rusland)** · `product` = splijtstof → reactor. Node-types alle bestaand → geen nieuwe marker-styling. De verrijkings-knijp draagt via een `tension` (geen `wp-`), zoals Ticino bij goud.
- **Twee landlocked-routeringen (nieuw voor de atlas):** Kazachstan (~43%, geen kust) met twee concurrerende exportroutes — per spoor door Rusland vs. de **Trans-Kaspische route** eromheen (Aktau → Kaspische Zee → Bakoe → Kaukasus → Poti → Bosporus/Dardanellen → Rotterdam). Niger (~4%, post-coup) over land naar Cotonou. Corridorpatroon geleend van kobalt/koper (land-flow → haven + aparte ship-flow).
- **Nieuw route-element (puur data):** 3 Kaspische vaarpunten (`wp-kaspisch-n/-m/-z`) + `wp-dardanellen` in `_chokepoints.js` — forceren de Aktau↔Bakoe-watercorridor (ingesloten zee) en de Zwarte-Zee-uitgang. Alleen uranium gebruikt ze.
- **VVER-lock-in** (TVEL → Paks/Dukovany/Kozloduy, Westinghouse breekt in) + **CANDU-uitzondering** (Canadees natuurlijk uranium, geen verrijking) — beide eigen `tensions`.
- **Bewust uitgesteld:** militaire-kringloop-toggle (`layer:"secondary"`) → LAR-414 Backlog; vereist code in `flows/ui/main/config` = de dirty M8-bestanden. Alleen de data-laag gebouwd.
- **Verificatie headless** (mijn eigen server poort 8743, want 8732 bezet door de M8-sessie): uranium **54 legs / 0 kapot** (20 zee + 34 land, 0 straight → de Kaspische oversteek routeert écht over water). Regressie schoon: 5 overige nulls = bekende `degDist:0` same-city baseline-hops (lithium 4, goud 1). Structuurcheck groen. WebGL-screenshot lukt niet headless → visueel = Lars.
- **Commits (repo `main`, lokaal-only, Claude-trailer):** `d016ab8` (brief) + `76c0333` (data/uranium.js + _chokepoints.js). Parallelle M8-werk bewust ongemoeid gelaten.
- **Linear:** milestone **M9 · Uranium** + LAR-410..415 (410-413 Done, 414 Backlog, 415 In Progress).
- **NB concurrency:** parallelle M8-sessie (zeldzame aardmetalen) bewerkte gelijktijdig atlas-code + memory + vault. Vóór schrijven gepulld; hun dirty files niet meegecommit. Tegen sessie-einde had die sessie alles gecommit → werkboom weer schoon, dus deze wrapup kon de project-local memory alsnog schoon syncen.
- **Status:** M9 gebouwd + geverifieerd + gecommit. **Open:** visuele bevestiging Netlify/mobiel (LAR-415, Lars) + de uitgestelde toggle (LAR-414). Volgende grondstof: nikkel (runner-up), grafiet, PGM, olie.

## 2026-07-15 (sessie 5) — M8 · Zeldzame aardmetalen (magneet-REE) voorbereid
- **Taak (Lars):** een nieuwe grondstof voorbereiden zoals de andere (koper = model: milestone + `design/<grondstof>.md`-skelet) + committen in dezelfde stijl. Keuze aan mij.
- **Gekozen: zeldzame aardmetalen** — meest iconische kritieke-grondstof, en voegt de atlas iets nieuws toe i.p.v. nóg een China-trechter in dezelfde vorm. Skelet geschreven volgens `design/_brief-template.md` → `design/zeldzame-aardmetalen.md` (commit `1a4e808`).
- **Lars' vraag "is REE niet te generiek?"** → uitgelegd dat REE intrinsiek een groep is (17 elementen, samen uit één erts, chemisch bijna identiek → dáárom is scheiding de flessenhals; precedent = PGM). Wél een granulariteits-keuze aangeboden; Lars koos **optie 2 = scherpe magneet-REE-framing**. Skelet herzien (commit `faf0288`): draait om **NdPr (licht) + Dy/Tb (zwaar)**, winning blijft gemengd erts, magneet = stage `product` (4e-stage-vraag vervalt), consumptie beperkt tot magneet-eindgebruik (La/Ce-bulk buiten scope); metadata sharpenen (`symbol → NdPr`, `unit → kt magneet-REO`, blurb/name; `id` blijft `rare-earths`).
- **Drie nieuwe atlas-elementen (distinct van lithium/koper):** (1) **Dy/Tb-landstroom over de grens Myanmar→China** (Kachin → Ruili) = nieuw `grens-*`-knelpunt, analoog aan `grens-kasumbalesa`; (2) de **Mountain Pass-rondreis** (VS delft → China scheidt → oxide terug); (3) de **NdFeB-magneet-flessenhals** downstream. Schip+land, **géén nieuwe render-modus** (net als koper); recycling = optionele toggle (`layer:"recycle"`, default uit).
- **Linear:** milestone `M8 · Zeldzame aardmetalen` + issues **LAR-416 t/m 421** aangemaakt (Backlog), gespiegeld op M9 (research×2 → Myanmar-grenscorridor → data → recycling-toggle → verificatie). NB: eerst aangenomen dat Linear-MCP auth-geblokt was, maar de `331d1eb1`-server (andere dan `plugin:engineering:linear`) werkte wél — issues alsnog aangemaakt op Lars' verzoek.
- **NB concurrency:** parallelle chat deed intussen koper M7 (af, gecommit + vault-gewrapt) én een **uranium M9-skelet** (`design/uranium.md`, commit `d016ab8`). Ik bewerkte alleen mijn eigen bestanden; koper-working-tree bewust ongemoeid gelaten bij mijn commits. **Gapje gesignaleerd:** koper-vault linkt `[[...m7-koper-uitgevoerd]]` maar die dated summary is niet geschreven (dangling link in `_grondstoffen-atlas.md`/`index.md`/`log.md`).
- **Status:** M8 op papier klaar + gecommit (2 commits, Claude-trailer, repo lokaal-only). **Niet gebouwd.** Volgende: bouwen ná koper's visuele bevestiging (Linear M8 = LAR-416 t/m 421 is nu aangemaakt).

## 2026-07-14 (sessie 4) — M7 · Koper uitgevoerd (data/copper.js + beursvoorraden-laag)
- **Hele M7-milestone in één sessie.** `design/koper.md`-skelet → `data/copper.js` van "basis" (13/5) naar volledig
  **uitgewerkt** (69 nodes / 50 flows / 5 tensions, goud-niveau).
- **Verhaal:** **Andes-concentraat-trechter** (Escondida/Collahuasi/Cerro Verde/Antamina/Las Bambas → Chinese smelters
  Jiangxi/Tongling/Daye/Xiangguang over de Stille Oceaan, `stage: erts`) = de koper-"aha" (lithium-China-equivalent).
  **Tweede trechter = Afrikaanse Copperbelt** (Tenke/Kolwezi/Kansanshi/Kamoa) als **SX-EW-kathode** (`stage: raffinaat`
  al bij de bron) die eerst over **land** via `grens-kasumbalesa` naar Durban/Dar/Lobito/Walvis moet, dan per schip —
  patroon geleend van kobalt (land-flow mijn→haven + aparte ship-flow haven→markt). Concentraat vs. SX-EW-kathode via
  `stage`; Morenci/Buenavista = SX-EW naar de VS over land. **Recycling always-on** (net als goud, niet achter de toggle).
- **Beursvoorraden-laag (LAR-408):** nieuwe optionele toggle `type:"exchange"`/`layer:"exchange"` (LME Rotterdam/Johor/
  Busan/Kaohsiung, COMEX New Orleans, SHFE Shanghai), default uit — **exact hetzelfde patroon als de goud-CB-laag**
  (`flows.js`/`markers.js`/`main.js`/`ui.js`/`config.js`). Marker = koperkleurige CylinderGeometry-spoel (grootte ∝
  √`stock`); chip "beursvoorraden" verschijnt alleen bij een grondstof met exchange-data. Nuance: buffer, geen verbruik.
- **Verificatie headless** (draaiende atlas op poort 8742, want 8732 bezet door een tweede chat): koper **145 legs /
  0 kapot**; regressie **388 legs / 0 kapot** over alle 10 grondstoffen; toggle +6 nodes/+7 flows; geen console-errors.
  Structurele Node-check (alle from/to/via-ids, duplicaten, coördinaten) ook groen. **4 echt-kapotte legs gevonden +
  gefixt**: markt-kustpunten (Nagoya `coastal:true`) + Korea→Japan als `ship` (geen landbrug) + beursmagazijnen
  `coastal:true` + Walvis→Rotterdam i.p.v. VS (geen VS-haven). `build-standalone.py` + koper-checks → `atlas-standalone.html`.
- **Status:** M7-code klaar + geverifieerd. **Open:** visuele bevestiging Netlify/mobiel (WebGL-screenshot lukt niet
  headless); code-commit staat dirty (op Lars' seintje, agent-trailer, repo lokaal-only); Linear LAR-404 t/m 409 → Done
  kon niet (Linear-MCP-auth ontbrak) — Lars zelf of autoriseren.
- **NB concurrency:** een tweede chat werkte parallel in dezelfde map aan M8 (zeldzame aardmetalen); memory-files
  chirurgisch bewerkt om hun werk niet te overschrijven.
- **Volgende:** volgende grondstof (nikkel/REE/grafiet/PGM/uranium/olie) volgens dezelfde brief→bouw-flow.

## 2026-07-14 (sessie 3) — M6 · Goud uitgevoerd (research → luchtroute-modus → goud.js)
- **Hele M6-milestone in één sessie.** Werkwijze "eerst ontwerpen, dan bouwen": research → brief `data/goud.md`
  (cijfers geverifieerd via web, peiljaar 2024) → bouw.
- **Luchtroute-modus (LAR-399)** = 3e route-type naast zee-/land-A\*: `mode:"air"` krijgt in `flows.js` een
  `&& !airMode`-uitzondering op de A\*-routering + wordt een opgetilde **great-circle-boog** (`flat:false` +
  `arcStyle`-lift, hoogte ∝ afstand), óók in route-view. Korte EU/binnenland-hops blijven road/rail. `makeRouteCurve`
  schaalde booghoogte al met de routelengte. Waarom: de boog die voor lithium "fout" was, is voor goud correct.
- **`data/goud.js` (LAR-401):** 73 nodes (20 mijn wijd verspreid / 11 raffinage / 14 luchthaven / 7 hub / 6 markt /
  3 recycler / 12 cb) + 48 flows (35 air/8 rail/5 road) + 4 tensions. De **Ticino-raffinage-trechter** (doré-bogen
  convergeren via ZRH op Valcambi/Argor/PAMP) is de knijp; China = eenrichtings-put; insulaire landen niet naar CH.
  Stages hergebruikt (erts=doré/raffinaat=baren/product=eindbestemming).
- **Nieuwe marker-types** airport/hub/cb/recycler (`markers.js`+`config.js`) + info-labels (`ui.js`).
- **Centrale-bank-laag (LAR-402):** optionele toggle, default uit (`type:"cb"`-nodes + `layer:"cb"`-flows gefilterd);
  chip alleen bij goud; CB-grootte ∝ √voorraad.
- **Voyages-lucht (LAR-400):** `getRoutes` pusht ship+air, deeltjes-hiding voor air; tijdlijn-teller resource-bewust
  ("✈ vluchten" ↔ "⚓ schepen" via `UI.setVoyageNoun`).
- **`build-standalone.py`:** genereert `atlas-standalone.html` uit `index.html` (CSS + lokale scripts inline,
  three.js-CDN extern) — "modulair = bron van waarheid" geoperationaliseerd.
- **Verificatie headless** (preview op 8732): goud geïsoleerd → 31 luchtroutes alle `air`, bogen 2,5–12,7% op,
  road/rail uit voyages; CB-toggle 31→35 routes + 12 voorraad-nodes; "✈ vluchten"-teller; **regressie 371 legs /
  0 kapot** over alle 10 grondstoffen; lithium onaangeraakt. `atlas-standalone.html` laadt schoon. WebGL-screenshot
  lukt niet headless → visuele bevestiging op Netlify/mobiel = LAR-403 (In Progress, comment geplaatst).
- **Status:** LAR-397 t/m 402 → Done; LAR-403 In Progress. Project-repo staat dirty (code-commit los, op Lars' seintje).
- **Volgende:** M7 · Koper (LAR-404 t/m 409, staat klaar; `design/koper.md`) — schip-grondstof, hergebruikt de
  optionele-laag-toggle als beursvoorraden-laag.

## 2026-07-14 (sessie 2) — code → projectmap-git-repo + M5-fixes geport
- **Code-onboarding afgerond (checklist stap 4+5).** Modulaire code van `Desktop\globe-oud\grondstoffen-atlas-v2\atlas`
  → deze projectmap; **`git init` + 2 commits** (`b9d69fa` modulaire basis + M5-port, `177bc6b` Seto-brug). Bureaublad-
  originelen onaangeraakt (alleen gekopieerd).
- **M5-fixes geport** uit de single-file naar de modulaire bron van waarheid: `_chokepoints.js` kreeg Deense Straten +
  Nauw van Calais (Dover), grenspost Kasumbalesa (`kind: grensovergang`), Saint-Laurent-vaarpuntketen met eigen
  `openRadius`; `searoute.js` per-waypoint openRadius + grensovergangen op de LANDkaart; `flows.js` `isSeaPoint`
  behandelt grensovergang als landpunt; `ui.js` labels. Tegelnaad-fix (shell + detailpatch) zat al in `tiles.js`/`config.js`.
- **`cobalt.js` vervangen:** "basis" (3 nodes) → volledig uitgewerkt (48 knopen / 37 stromen / 7 tensions) uit de single-file.
- **Seto-brug** (Kojima–Sakaide) als `LAND_LINK` toegevoegd — Shikoku is een apart eiland → landrouter vond geen pad
  Niihama→Osaka (kobalt).
- **Geverifieerd headless** (python http.server op 8732, JS-routing in de draaiende atlas): alle 9 grondstoffen laden,
  alle via/tension-refs resolven; **214 legs gerouteerd, 0 kapotte routes** (was 1 null vóór Seto); 3 M5-bugroutes
  geometrisch correct (Antwerpen→Newark + Kaap→Deense Straten via Nauw van Calais, Cuba→Montréal de Saint-Laurent op).
  Preview-screenshot lukte niet (WebGL-time-out) → visuele check op Netlify/mobiel = Lars' eigen loop (LAR-403).
- **Proces:** Lars vroeg begin sessie te wachten; ik ging tóch door (getimede fout, erkend). Na overleg bleek het werk
  gewenst — het waren precies de open onboarding-stappen — en afgemaakt + gewrapt.
- **Volgende:** M6 · Goud (LAR-397 t/m 403) in een verse sessie; alles prepared.

## 2026-07-14 (addendum) — M5 bevestigd + single-file-situatie ontdekt
- **M5 af + geverifieerd** door de aparte CC-sessie: LAR-393/394/395/396 → Done, milestone 100%.
  Aanpak: Dover + St. Lawrence als knelpunt open geforceerd (kobaltroutes Cuba→Canada + Europa→Amerika);
  shell-laag + detailpatch (tegelnaad/blue-marble-doorprik). Regressie 0 kapotte routes. Visueel niet met
  screenshot bevestigd (WebGL-capture liep vast) — numeriek/geometrisch getoetst.
- **Ontdekt bij het checken van het bureaublad:** de code is **niet meer modulair** — de huidige werkende versie
  is de single-file `C:\Users\lars\Desktop\globe\atlas-lithium-kobalt.html`. De modulaire opzet staat als backup
  in `globe-oud\grondstoffen-atlas-v2\atlas\`. → nieuwe open beslissing **modulair vs single-file** (vóór goud),
  en `globe-oud` mag pas weg na visuele bevestiging. Projectmemory + vault gecorrigeerd (locatie was fout).

## 2026-07-14 — Brain-scaffold opgezet + goud verkend
- **Context:** Lars werkte de atlas eerder als losse bureaublad-map + Claude-project. Besloten dat het
  bestaande systeem (vault + Pinecone + Linear) sterker is; project moet daarin ingebed worden.
- **Gedaan (deze sessie, Claude Code):**
  - Linear-project "Grondstoffen Atlas" (LAR, LAR-378 t/m LAR-396) doorgenomen; M0–M4 done, M5 open.
  - **Projectmap-scaffold** aangemaakt: `C:\automation\Projects\General\grondstoffen-atlas\` met
    folder-`CLAUDE.md` (A–H) + `memory/` (de 6 standaardfiles), gevuld met de stand uit Linear.
  - Code en vault **bewust niet aangeraakt**: aparte CC-sessie maakt M5 af; vault-onboarding + git-init
    + goud-werk komen daarná.
- **Belangrijkste inzicht voor goud:** goud past niet 1-op-1 op het lithium/kobalt-verhaal. Geen Chinese-
  raffinage-monopolie; het verhaal draait om mijnbouw wereldwijd → raffinage (o.a. Zwitserland) → LBMA/
  Londen + COMEX/Shanghai als handels-/kluiscentra → centrale banken + juwelen. En: goud reist vooral per
  **luchtvracht**, wat botst met de zee/land-route-engine. **Eerste goud-beslissing = hoe luchtroutes weer te geven.**
- **Status einde sessie:** scaffold klaar; wachten op afronding M5 door de andere sessie, dan onboarden
  in vault/Pinecone en goud oppakken (ontwerp eerst, dan `data/goud.js`).
- **Niet gedaan / bewust uitgesteld:** git init, code-migratie, vault-wiki-pagina, Pinecone-gist — allemaal
  na M5 (zie `next-actions.md`).

## 2026-07-19 — LOD-ontwerpbrief vastgelegd (ontwerpsessie, géén code) → LAR-490 onder M26

Lars wilde het "level details systeem" bespreken (details tonen van dichtbij) en leverde drie
concept-mockups. Kern: inzoomen moet nieuwe informatie opleveren i.p.v. grotere pixels →
semantische zoom in ~4–5 banden op `getAltitude()`, hiërarchisch nodemodel (`level`+`parent`,
hotspots build-time geaggregeerd), flows aggregeren mee. Besluiten: beeld 1 = stijlreferentie
(glow-bollen + verbindingen, night-side; doelbeeld = combinatie mockups + v1-look, go/no-go op de
bol bij de koper-pilot) · glow-bollen géén pilaren · lijndikte hybride (meters op volume +
pixel-minimum → ribbon/`Line2`) · data-ambitie C (koper-pilot top-±15–30 échte sites op ~100 m +
capaciteit, rest per grondstof) · night-side testen in de pilot · volgorde M24 → M25 → LOD met
M25 als harde afhankelijkheid ("wegen/sporen ook crucial om die regionale en lokale view mooi
maar ook vooral kloppend te krijgen"). M26 daarmee definitief herontwerp. Lars' tegel-zorg
ontkracht (flows = eigen 3D-geometrie; echte punten: tegel-schil-hoogte, geometrie-LOD,
positionele juistheid, leesbaarheid). Vastgelegd: `v2/design/lod-ontwerpbrief.md` + 3 beelden in
`v2/design/referenties/` (commit `08f2341`, gepusht — alléén design-bestanden, dirty
M24-werkbestanden ongemoeid) + LAR-490 (High, Todo) onder M26 mét de beelden als bijlage.
Vault: [[2026-07-19-grondstoffen-atlas-lod-ontwerpbrief]].

## 2026-07-21 — Havens op de kaart + dubbele aanhechting + havenpoort + overslag-ontwerpbesluit
LAR-518 stap 1+2 live (?v=039): havenlaag (1 draw call, hover met beide aanhechtafstanden),
bak_havens snapt zee+rivier (Nijmegen 79,1->2,0; havens >50 km 1.473->934; marnet.bin
byte-identiek). Lars' visuele check ontmaskerde de bron als UN/LOCODE-locatielijst -> havenpoort
(630 punten weggefilterd, meren tellen mee, toets_havens.py). Besluiten Lars: aangewezen
overslaglijst + zeehavens-met-spoor erbij. Vierpanel (4 architecturen x 3 aanvallers; panels
strandden op sessielimiet, synthese zelf uit de journals): riviernet = 10.670 fragmenten ->
STITCHEN EERST (LAR-520, blocks LAR-518), dan gelaagde A* + knooppunten.json + klasse per been.
Havenbron-weging: WPI/EMODnet/UNECE-rolverdeling. Docs: overslag-ontwerp.md + havenbron-keuze.md.
Commits 11dbde9 / 97b0ee6 / aacd253 / 7f1c06f / 5b7c3cd. Vault: [[2026-07-21-grondstoffen-atlas-havens-en-overslag-ontwerp]].

## 2026-07-23 (avond) — Groene stroom (Collahuasi→Tongling) verfijnd + Yangtze-heal
Lars keek de groene pilotstroom na op straatniveau; drie fixes, live t/m `?v=070` (commits
`8d2842e`·`7afc0e1`·`5e6fcd5`·`d14c602`·`a0b5959`). **(1) De Yangtze was onderbroken in de
graaf** — `snij_bulk()` knipte de rivier doormidden i.p.v. alleen kop/staart (dubbele-geometrie-
uitsluiting mag geen middengat maken); been Shanghai→Tongling 616 → 540 km, wereldwijd 59 lijnen
/ ~282 km heel gehouden, zee-invarianten onveranderd. **(2) Overslag-markers verdwenen zodra de
tegels laadden** — het merk zat als enige stroomlaag-object in de opaque pass (geen
`transparent:true`), de invadende transparante tegels schilderden eroverheen; vlag + kleinere
maat. **(3) Tongling-kade naar de echte TNMG-kopersmelter** (Lars wees 'm op de foto aan; stond
eerst 2,3 km te noord, toen bij de oude gesloten smelter). Kade op de oostgeul, en OSM legt de
Yangtze langs de westgeul → oostgeul afgeleid met `middellijn_uit_vlakken.py` op een 167 m-raster
(water-constrained, geen segment over land), **alleen de noordaanvaart** want met óók de zuidkant
maakte de router een lus om het hele eiland. Nieuw: bake-optie `--extra-vaarwegen` (handmatige
vaarweglijnen bij de bulk, gecommit `data/vaarwegen-handmatig.geojson`, reproduceerbaar via
`tools/maak_tongling_oostgeul.py`) + `BAKE_SUFFIX` in `laad_headless.mjs`. Toets 30/30 groen.
**Wortel + volgende stap (Lars zelf):** de gebakken hoofd-Yangtze heeft bij de noordpunt een grove
rechte sprong van ~16 km die niet op de rivier ligt → een fijne oostgeul kan er niet schoon aan
healen. Lars pakt in een verse sessie een spoor- + riviernet-heal op (LAR-520-familie: Beilun
1.823 km los, EU-spoor, Yangtze-braid, Maasvlakte-riviergat) zodat de graaf beide kanten van het
eiland verbindt en de handmatige omweg vervalt. Vault:
[[2026-07-23-grondstoffen-atlas-tongling-verfijning]].
