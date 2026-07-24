# De routebrief — werkwijze (M26)

*Vastgelegd 2026-07-24, op voorstel van Lars na de M26.1-lessen: de router koos corridors
zonder kennis van de werkelijkheid, en álle controle hing op zijn ogen (Honshu, het schip
voorbij de haven, vier fouten per sessie). Zijn formulering: "wat is de echte route die ze
in het echt maken, met elk dorp, regio of stad waar die doorheen rijdt — zodat je zelf
doorhebt dat het goed of fout is."*

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
  - **bevestigd** — twee onafhankelijke bronnen, of OSM + één bron;
  - **aannemelijk** — één bron;
  - **onzeker** — genoteerd, nog niet gestaafd.
- **Negatieve ankers zijn ook feiten.** Een plaats waar de route juist NIET langskomt
  terwijl bronnen dat suggereren (wegbeschrijvingen noemen vaak knooppunten die 3 km naast
  het spoor liggen) krijgt een eigen regel als *referentie (niet aan lijn)*. De getekende
  lijn mag zo'n punt niet raken.

## 3 · Kalibratie — welke punten erin horen

Niet elk gehucht. Wél:

1. **Elk punt waar je fout kunt afslaan** — elke splitsing/aftakking/rivierarm, plus het
   eerstvolgende bevestigde punt ná de splitsing (dat punt pint de gekozen tak).
2. Om de **±25–50 km een genoemd anker**, zodat er maar één plausibel pad door de punten past.
3. De **exacte kop en staart** (kade, laadspoor, pier) op ~50 m.

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

## 7 · Relatie met het komende AIS-net (corridor-first)

Voor het natte deel (havenaanloop + binnenwater) wordt de graaf niet langer uit
dataset-verzoening opgebouwd maar **corridor-first**: de brief zegt *welke plekken in welke
volgorde*, AIS-vaardichtheid (EMODnet e.d.) of de satellietgeul zegt *waar de geul echt
ligt*, en de knopen worden zelf gelegd en verbonden. Nuance t.o.v. het eerdere
AIS-besluit (2026-07-18, LAR-482): AIS toont schepen, geen lading — hier gebruiken we het
uitsluitend als **geul-bewijs** voor de graaf, niet als bron voor stromen. Het open-zeenet
blijft staan zolang het werkt; het AIS-net begint bij aanloop + binnenwater.
