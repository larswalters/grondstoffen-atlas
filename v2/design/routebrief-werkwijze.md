# De routebrief — werkwijze (M26)

*Vastgelegd 2026-07-24, op voorstel van Lars na de M26.1-lessen: de router koos corridors
zonder kennis van de werkelijkheid, en álle controle hing op zijn ogen (Honshu, het schip
voorbij de haven, vier fouten per sessie). Zijn formulering: "wat is de echte route die ze
in het echt maken, met elk dorp, regio of stad waar die doorheen rijdt — zodat je zelf
doorhebt dat het goed of fout is."*

*Aangescherpt 2026-07-28 na de eerste volledige keten (grafiet Balama→Vidalia). De brief
droeg de corridor goed — de fouten zaten in **kop en staart**. Toegevoegd: de status
**satelliet-gelegd** (§2), de last mile als eigen been (§3.4) en de stippellijn-conventie
waar het net niet reikt (§7).*

*Uitgebreid 2026-07-28 (besluit Lars): een brief loopt van de **mijn tot het eindproduct**,
niet tot kathode of raffinaat — na de raffinaderij komt de fabriek, en daarna wat daar nog
op volgt (§1a). Daarbij: **één brief = één streng** met expliciete samenvloeiingen en
vertakkingen (§1b), de **productvraag als vindmethode** voor elke kade (§2a), en **een
overslag is twee ankers** (§2b). Leeg sjabloon: `routebrieven/_template.md`.
Na tegenspraak dezelfde dag aangescherpt op toetsbaarheid: vaste coördinaatnotatie en
been-ids (§2), negatieve ankers mét verbodsstraal en het reële alternatief als eigen
klasse (§2), drager-wissel = overslag óók zonder modaliteitswissel + routeerpunt naast
anker (§2b), en de toets-marge per punt instelbaar (§4).*

---

## 1 · Wat een routebrief is

Per stroom één brief die de **werkelijke corridor** vastlegt als een geordende lijst
controleerbare punten: de exacte laadplek, elke plaats/splitsing/sluis/rivierstad die de
lading in werkelijkheid passeert, en de exacte overslag- en losplek. De brief wordt
geschreven **vóór** (of los van) de getekende lijn, uit bronnen — en de lijn wordt er
daarna tegen getoetst. Daarmee kan de maker van de route zélf zien dat iets fout is, in
plaats van dat de fout pas bij Lars' visuele check bovenkomt.

**Het doel is zelfverificatie.** De maker van de brief doet ook de satellietpass zelf:
*satelliet-gelegd* betekent "ik heb op de stitch gekeken en het punt ligt zichtbaar goed"
— niet "Lars moet er nog naar kijken". Bewijs dat dit werkt: bij de ankercheck van
2026-07-28 vond de agent zelf 10 van de 16 kop/staart-fouten op de stitches; Lars keurde
alleen de correctievoorstellen goed. Lars' visuele check is een realisme-blik achteraf;
het enige dat expliciet bij hem terugkomt is de openstaande-puntenlijst (§ openstaande
punten in de brief) — punten die ook op z16/z18 niet te beslissen zijn.

- Locatie: `v2/design/routebrieven/<grondstof>-<van>-<naar>.md`
- Leeg sjabloon: `v2/design/routebrieven/_template.md`
- Kop en staart van elk been = de **aansluiting per grondstof** (~50 m, `aansluitingen.json`)
- De corridor bij naam waar die bestaat (ertslijnen, vaarwegen en leidingen zijn vaak
  benoemde, gedocumenteerde trajecten met een eigen lengte — die lengte is meteen een toets)

## 1a · De reikwijdte: mijn → eindproduct

Een brief houdt **niet** op bij de kade van de smelter of bij de kathode. Na het raffinaat
volgt de fabriek die er een halffabricaat van maakt, en daarna wat daar nog op volgt — met
exact dezelfde bewijslast: laadplek, elke plaats onderweg, de exacte overslag, de losplek.
De keten is opgedeeld in vijf fasen met **doorlopend genummerde benen**:

| fase | van → naar | typische modaliteit |
|---|---|---|
| A | laadplek mijn → zeehaven (incl. last mile en poort) | truck · spoor · leiding · band |
| B | zee | zeeschip (vrij geroutet, §6) |
| C | aanlanding → smelter/raffinaderij (incl. last mile) | binnenvaart · spoor · weg |
| D | raffinaat (bv. kathode) → fabriek | spoor · weg · zee |
| E | fabriek → eindproduct / markt | weg · spoor |

De brief stopt waar het product als eindproduct de markt op gaat, óf waar er geen
gedocumenteerde volgende locatie meer is. **Dat stoppunt wordt beargumenteerd**, niet
stilzwijgend gekozen; een markt-centroïde is expliciet een centroïde en dus géén anker.

## 1b · Eén brief = één streng

Een keten vertakt (een deel van de kathode gaat naar een andere fabriek) en vloeit samen
(twee mijnen leveren aan dezelfde raffinaderij; twee halffabricaten komen in één fabriek
binnen). De brief beschrijft **één streng** van begin tot eind en noteert de kruispunten:

- **Samenvloeiing** — een been dat twee strengen delen wordt in **één** brief volledig
  uitgeschreven; de andere brief verwijst ernaar en herhaalt de puntenlijst niet. Anders
  lopen twee versies van dezelfde corridor stil uit elkaar.
- **Vertakking** — het afsplitsende deel krijgt een eigen `stroom-id` en een eigen brief; de
  moederbrief noemt het been, het aandeel en de brief waar het verder gaat.
- **Verwerkingsknoop** — elke smelter/raffinaderij/fabriek krijgt in de brief een blok met
  het anker-id, wie de **eigenaar** van dat anker is, wat er in- en uitgaat (product +
  volume), welke andere strengen er binnenkomen en waar het bijproduct heen gaat. Zo is
  achteraf controleerbaar of de volumes over de knoop heen kloppen.

## 2 · Het puntenformat

| # | km | punt | type | lat, lon | bron | status |

- **Notatie is een harde regel:** coördinaten altijd in de volgorde **lat, lon**, met
  **decimale punt**, ankers op **5 decimalen** (~1 m), passages op 2–4. Eén schrijfwijze
  door het hele document, ook in het proza. Reden: de toets-tools lezen de tabellen
  direct, en de eerste Collahuasi-versie had in dezelfde kolom lat,lon- én
  lon,lat-regels — daar struikelt elke controle over, machine én mens.
- **Elk been draagt een been-id** (`<stroom-id>-b<n>`) en elk anker het id uit
  `aansluitingen.json` waar dat bestaat. Stroomroute-JSON's en markertabellen verwijzen
  naar diezelfde ids, zodat brief ↔ bol 1:1 koppelbaar is zonder mensenwerk.
- **km** = afstand langs de corridor vanaf het laadpunt (waar meetbaar, bv. OSM-chainage
  of officiële kilometrering). Maakt volgorde-fouten meetbaar.
- **type**: laadplek · poort · passage · station · kruising · rivierkruising · passeerspoor ·
  sluis/kering · vaarweg-overgang · overslag · opslag/stockpile · verwerkingsstap · losplek ·
  **referentie (niet aan lijn)** · **alternatief (reëel, met aandeel)** ·
  **negatief anker (met verbodsstraal)**.
- **status**, met vaste betekenis:
  - **satelliet-gelegd** — het punt is visueel gecontroleerd op een gestitchte
    satellietoverlay (Esri World Imagery, **z16** met 0,01°-grid) en zo nodig verschoven.
    **Verplicht voor elk punt van het type laadplek, overslag of losplek**: zo'n punt is
    pas een anker ná deze stap, hoeveel bronnen er ook achter staan.
  - **bevestigd** — twee onafhankelijke bronnen, of OSM + één bron;
  - **aannemelijk** — één bron;
  - **onzeker** — genoteerd, nog niet gestaafd.

- **Negatieve ankers zijn ook feiten — en ze zijn pas toetsbaar mét coördinaat en
  verbodsstraal.** Een plaats waar de route juist NIET langskomt terwijl bronnen dat
  suggereren krijgt een eigen regel: naam, lat/lon, straal ("de lijn mag niet binnen
  X km komen") en de reden. "Niet via Yangshan" zonder coördinaat kan de machine niet
  meten; mét wordt het één afstandscheck.
- **Het reële alternatief is een eigen klasse, geen referentie.** Een plek waar een déél
  van de stroom in werkelijkheid wél heengaat (Zhangjiagang/Jiangyin voor
  Yangtze-concentraat) is geen negatief anker en geen oriëntatiepunt: noteer hem als
  *alternatief* met het (geschatte) aandeel. Wordt dat aandeel substantieel, dan is het
  een vertakking → eigen streng (§1b). Zonder deze klasse tekent de bol een
  plausibele-maar-verkeerde route zonder dat de toets piept.

> ⚠️ **Waarom de satellietregel er staat: twee "bevestigde" onderzoekspunten bleken
> visueel fout.** De New Orleans-"kade" was een stadscentroïde (van 510.752 VS-tracks
> kwam er géén binnen 0,5 km), en het Nacala-kadepunt −14,531 / 40,652 lag in open water
> bij de **kólen**-jetty op de **wéstoever** — terwijl de containerterminal waar de trucks
> aankomen op de oostoever ligt (−14,5383 / 40,6673). Beide werden gevonden door Lars' oog
> op de bol, niet door de brief. Een bron- of OSM-coördinaat is dus een *kandidaat*, geen
> anker. Werkwijze (Tongling-ronde): tegels stitchen met PIL uit
> `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}`,
> grid + kandidaatpunt erover tekenen, schuiven tot het zichtbaar op de kade/laadplek ligt.
> Route-uiteinden vragen z16 — een haven of fabriek is kleiner dan de z13-korrel.

## 2a · De productvraag — het gereedschap dat de kade vindt

*"Welk product is dat, dan kun je toch checken waar ze dat verwerken of overslaan"* (Lars).
Dat bleek de snelste en betrouwbaarste manier om een kade te vinden — sneller dan zoeken op
havennaam en sneller dan inzoomen. Daarom hoort hij **verplicht bij elke laad-, overslag- en
losplek** in de brief, als ingevulde ladder, zodat de keuze navolgbaar is en een fout in
stap 2 niet stil doorwerkt in stap 6:

| stap | vraag |
|---|---|
| 1 | Welk product, in welke fysieke vorm (bulk, bundels, containers, vloeibaar, slurry)? |
| 2 | Welke **soort** faciliteit hoort daarbij? |
| 3 | Welke partijen doen dat op deze plek? |
| 4 | Welke daarvan hoort bij déze stroom (operator, afnemer, concessiehouder) — en waarom? |
| 5 | Welke kade / welk adres / welk laadspoor? |
| 6 | Coördinaat + satellietbevestiging (z16) — wat is er zichtbaar: kranen, wagons, stapels? |

**Gewerkt voorbeeld (Rotterdam):** kathode = LME-leverbaar metaal → dus een LME-erkend
entrepot → Rotterdam heeft daar een handvol partijen voor (Steinweg, RHB, Metaal Transport,
Access World) → **RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4** (1.060 m kade,
non-ferro, LME-kwaliteit) → kade satelliet-gelegd op 51,8935 / 4,4585. Het oude anker lag
4,5 km verderop op de dijk bij de woonwijk Heijplaat, en was *geometrisch* plausibel:
OSM vond daar water op 3 m en een haven-object op 0 m. **Geen meetkundige toets vangt die
klasse fout — alleen de productvraag doet dat.**

**Noteer ook de uitsluitingen.** Wat de productvorm onmogelijk maakt is vaak sterker bewijs
dan wat hij toestaat, en het levert meteen de negatieve ankers: containervormig product lost
niet aan een bulk-t-dock met transportband; slurry eindigt bij de indikkers en niet aan de
pier; concentraat voor de Yangtze-smelters komt niet binnen op een containerhaven op eilanden
voor de kust.

## 2b · Een overslag is twee ankers

**Een overslag is elke drager-wissel** — een modaliteitswissel, maar óók een wissel binnen
dezelfde modaliteit: container-transshipment (deepsea → feeder, de kathode-op-MSC-SAMU-
klasse in fase D/E) en lightering (groot zeeschip → kleiner rivierschip, wat bij
Zhangjiagang/Jiangyin werkelijk gebeurt). "Het blijft een schip" is geen reden om de
overslag weg te laten.

Elke overslag krijgt **minstens twee ankers** — waar been N aankomt en waar been N+1
vertrekt — plus de terreinstappen ertussen (opslag, indikker, filterinstallatie, stockpile,
silo, rangeerbundel). Eén coördinaat kan niet tegelijk het einde van de leiding en het begin
van het zeebeen zijn; wordt dat toch afgedwongen, dan hoort er een **tweede aansluiting** te
komen, geen compromis-coördinaat tussen beide in.

Daarbij hoort de tweede helft van dezelfde regel: **anker ≠ routeerpunt**. Een schip vaart in
de geul en niet tegen de kade, een trein rijdt over het doorgaande spoor en niet in de
losbunker. Noteer bij elk been-uiteinde op water of spoor **beide** punten plus de maximaal
verwachte snap-afstand ertussen — anders kan de toets een goede snap niet van een foute
onderscheiden. Twee gemeten voorbeelden: bij New Orleans schoof het anker 490 m terwijl het
routeerpunt maar 154 m meebewoog; bij Beilun ligt de berth in het water en eindigt het
havenspoor bij het ertsveld, dus is een spoor-snap van 1,3 km dáár correct, geen fout.

## 3 · Kalibratie — welke punten erin horen

Niet elk gehucht. Wél:

1. **Elk punt waar je fout kunt afslaan** — elke splitsing/aftakking/rivierarm, plus het
   eerstvolgende bevestigde punt ná de splitsing (dat punt pint de gekozen tak).
2. **Op land: elke plaats waar de corridor doorheen of langs gaat** — dorp, stad,
   grensovergang, station. Dat is het niveau waarop de route met het blote oog te
   verifiëren is ("rijdt hij echt door X?"), en het is strenger dan de oude regel *om de
   ±25–50 km een anker*. Op water: elke rivierstad, sluis, kering en armsplitsing. Op zee
   volstaan de zeestraten en kapen als sanity-anker (§6). Vuistregel blijft: er mag maar
   **één plausibel pad** door de punten passen.
3. De **exacte kop en staart** (kade, laadspoor, pier) op ~50 m.
4. **De last mile aan beide uiteinden, als eigen been.** Niet alleen "de mijn" en "de
   kade", maar: laadplek op het terrein → poort → de openbare weg waar de corridor begint,
   en aan de andere kant: kade/losspoor → havenstraat → fabriekspoort → losplek. Dit is
   waar de grafietketen zijn laatste correctie kreeg — door kleine wegklassen
   (`residential`/`service`/`tertiary`/`unclassified`) mee te nemen binnen 12 km van plant
   en kade krompen de rechte ankerstukjes van **3,8 / 2,6 km naar 0,39 / 0,12 km**. Een
   rechte stub naar het dichtstbijzijnde net is geen last mile.

## 4 · De toets is tweezijdig

1. **Dekking** — de getekende/gerouteerde lijn raakt alle *bevestigde* punten in volgorde.
   Marge: default ~2 km op spoor/rivier-passages, ~100 m op kop en staart, **per punt
   instelbaar** — een stadspunt ligt zelden óp het spoor. De geslaagde Beilun→Guixi-toets
   raakte de corridorpunten op 0,8–6,4 km; een vaste 2 km had die correcte route
   afgekeurd. Een gemist aannemelijk/onzeker punt is een vraag; een gemist bevestigd punt
   is een fout.
2. **Verklikker** — elke plaats die de lijn wél raakt maar die níet in de brief staat is
   een rood vlaggetje: opzoeken (en aan de brief toevoegen) of de lijn corrigeren.

## 5 · Routeren mét de brief: via-punt → via-punt

Een been wordt niet meer in één vrije Dijkstra van kop naar staart gezocht, maar van
brief-punt naar brief-punt. Twee gevolgen:

- de router **kán** geen andere corridor meer kiezen dan de brief zegt;
- een netgat wordt **lokaal** zichtbaar ("tussen punt 7 en 8 geen pad") in plaats van als
  bizarre-maar-geldige omweg — dezelfde eerlijkheid als "geen pad mét reden".

## 6 · De modaliteits-afspraak (besluit Lars, 2026-07-24)

- **Zee = router.** In de brief staan alleen kade→kade (en desgewenst een enkel
  sanity-anker zoals een zeestraat). Het zeenet is bewezen (R'dam→Shanghai-invarianten).
- **Spoor, leiding en binnenvaart = brief-gestuurd.** Die netten zijn te fragiel om er vrij
  overheen te routeren; de brief bepaalt de corridor, het net levert alleen de geometrie
  tussen de brief-punten.

## 7 · Waar het net niet reikt: de stippellijn (besluit Lars, 2026-07-28)

Niet elke laad- of losplek hangt aan een net. Waar geen havenspoor, geen kade-aansluiting
en geen tracks liggen, wordt dat stuk **gestippeld getekend mét de reden erbij** — het
wordt niet dichtgemaakt met geleende of beredeneerde geometrie. De stippellijn betekent
precies één ding: *hier reikt het net niet.*

- Zo staan in de grafietketen de **haven-aanloop van Nacala** (~122 km: MARNET-knopen dun
  bij Mozambique, geen AIS-tracks) en de **last mile Port of Vidalia → Syrah-fabriek**
  (~1 km, geen net) erin.
- **Reken erop dat dit terugkomt.** Gemeten over de hele wereldscan hebben Chili
  (Patache/Antofagasta = het koperbeen), Lobito, Hormuz, Suez en Constanța **nul havens
  met varend AIS-verkeer**. Voor die stromen is de stippellijn de **eindvorm**, geen
  tussenstand — daar hoeft niet op gewacht of voor gebouwd te worden.
- De brief noteert bij zo'n been de **reden** en, waar bekend, de werkelijke modaliteit
  (short-haul truck, sleepboot, transportband, pijp). Daarmee blijft de kaart eerlijk over
  wat gemeten is en wat geraden — dezelfde regel als "geen pad mét reden".
- Doorgetrokken = we weten waar de lijn ligt. Gestippeld = eigen verbinding of geen net.
  Die twee betekenissen mogen niet vervagen.

## 8 · Relatie met het komende AIS-net (corridor-first)

Voor het natte deel (havenaanloop + binnenwater) wordt de graaf niet langer uit
dataset-verzoening opgebouwd maar **corridor-first**: de brief zegt *welke plekken in welke
volgorde*, AIS-vaardichtheid (EMODnet e.d.) of de satellietgeul zegt *waar de geul echt
ligt*, en de knopen worden zelf gelegd en verbonden. Nuance t.o.v. het eerdere
AIS-besluit (2026-07-18, LAR-482): AIS toont schepen, geen lading — hier gebruiken we het
uitsluitend als **geul-bewijs** voor de graaf, niet als bron voor stromen. Het open-zeenet
blijft staan zolang het werkt; het AIS-net begint bij aanloop + binnenwater.
