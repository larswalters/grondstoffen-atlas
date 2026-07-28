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

---

## 1 · Wat een routebrief is

Per stroom één brief die de **werkelijke corridor** vastlegt als een geordende lijst
controleerbare punten: de exacte laadplek, elke plaats/splitsing/sluis/rivierstad die de
lading in werkelijkheid passeert, en de exacte overslag- en losplek. De brief wordt
geschreven **vóór** (of los van) de getekende lijn, uit bronnen — en de lijn wordt er
daarna tegen getoetst. Daarmee kan de maker van de route zélf zien dat iets fout is, in
plaats van dat de fout pas bij Lars' visuele check bovenkomt.

- Locatie: `v2/design/routebrieven/<grondstof>-<van>-<naar>.md`
- Kop en staart van elk been = de **aansluiting per grondstof** (~50 m, `aansluitingen.json`)
- De corridor bij naam waar die bestaat (ertslijnen, vaarwegen en leidingen zijn vaak
  benoemde, gedocumenteerde trajecten met een eigen lengte — die lengte is meteen een toets)

## 2 · Het puntenformat

| # | km | punt | type | lat, lon | bron | status |

- **km** = afstand langs de corridor vanaf het laadpunt (waar meetbaar, bv. OSM-chainage
  of officiële kilometrering). Maakt volgorde-fouten meetbaar.
- **type**: laadplek · passage · station · kruising · rivierkruising · passeerspoor ·
  sluis/kering · vaarweg-overgang · overslag · losplek · **referentie (niet aan lijn)**.
- **status**, met vaste betekenis:
  - **satelliet-gelegd** — het punt is visueel gecontroleerd op een gestitchte
    satellietoverlay (Esri World Imagery, **z16** met 0,01°-grid) en zo nodig verschoven.
    **Verplicht voor elk punt van het type laadplek, overslag of losplek**: zo'n punt is
    pas een anker ná deze stap, hoeveel bronnen er ook achter staan.
  - **bevestigd** — twee onafhankelijke bronnen, of OSM + één bron;
  - **aannemelijk** — één bron;
  - **onzeker** — genoteerd, nog niet gestaafd.

- **Negatieve ankers zijn ook feiten.** Een plaats waar de route juist NIET langskomt
  terwijl bronnen dat suggereren (wegbeschrijvingen noemen vaak knooppunten die 3 km naast
  het spoor liggen) krijgt een eigen regel als *referentie (niet aan lijn)*. De getekende
  lijn mag zo'n punt niet raken.

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

## 3 · Kalibratie — welke punten erin horen

Niet elk gehucht. Wél:

1. **Elk punt waar je fout kunt afslaan** — elke splitsing/aftakking/rivierarm, plus het
   eerstvolgende bevestigde punt ná de splitsing (dat punt pint de gekozen tak).
2. Om de **±25–50 km een genoemd anker**, zodat er maar één plausibel pad door de punten past.
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
   Marge: ~2 km op spoor/rivier-passages, ~100 m op kop en staart. Een gemist
   aannemelijk/onzeker punt is een vraag; een gemist bevestigd punt is een fout.
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
