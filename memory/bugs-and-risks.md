# Bugs & risks — Grondstoffen Atlas
*Last updated: 2026-07-21 (LAR-520: 2 angled confluenties open; router nog niet gebouwd)*

## ⚠️ OPEN — twee angled confluenties nog niet gestitcht (2026-07-21, LAR-520)

Na de twee-traps heal (`?v=040`) zijn Mississippi en Rijn-mainstem verenigd, maar twee ankergaten
blijven bewust open: **Ohio-Cairo** (Cincinnati-component 2,4 km van de Mississippi) en de **Waal-tak
bij Nijmegen** (1,4 km). Beide zijn confluenties/vertakkingen **onder een hoek**, dus de collineaire
tier-2-guard wijst ze (terecht) af en tier-1 reikt niet zo ver. **Niet met een bredere naadradius
dichten** — gemeten dat dat parallelkanalen/dode voorlopers aanhaakt (valkuil 3). Ze vragen de
**lengtetoets** per corridor of een aangewezen naad in `knooppunten.json`; hoort bij het router-werk.

## ⚠️ OPEN — de router geeft nog niet het realistische getal (2026-07-21, LAR-520)

`de router werkt nog niet` (Lars). De huidige `zoekRoute` gaf R'dam→Duisburg **420 km / aanloop 153 km**
i.p.v. het realistische ~230 km — het stitchen maakt het net routeerbaar, maar `zoekKeten` (gelaagde
A*/overslag) + `toets_routes.py` (die R'dam→Nijmegen **~172 km over de graaf** narekent) moeten nog
gebouwd worden vóór de route-acceptatie van LAR-520 hard is.

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
