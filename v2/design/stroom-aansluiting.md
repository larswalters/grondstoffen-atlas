# De stroom-aansluiting — ontwerpbesluit (M26.1)

*Vastgelegd 2026-07-23, na Lars' schets: twee grondstoffen die in dezelfde havenmond elk hun
eigen lijn van het zeenet naar het riviernet trekken. Voortbouwend op
`overslag-ontwerp.md` (het koppelen, `?v=058`) en `lod-ontwerpbrief.md` (M26, koper-pilot).*

---

## 1 · Wat er ontbreekt

Het koppelen staat: vier netten, één zoekruimte, overstap op een aangewezen punt uit
`knooppunten.json`. Maar dat register heeft **één aanhechting per modaliteit per plaats** — één
zee-coördinaat voor heel Shanghai, één binnen-coördinaat, één spoor-coördinaat. Dat is genoeg om
te bewijzen dát de netten verbonden zijn, en het is precies genoeg voor een wereldbol.

Op straatniveau is het onwaar. Koperconcentraat wordt in Shanghai niet gelost waar containers
worden gelost; kathode weer ergens anders; en de ertspier in Beilun is een ander bouwwerk dan
het kolenfront ernaast. **Eén stip per haven kan geen twee lijnen dragen** — en twee lijnen is
exact wat Lars getekend heeft.

Dus: naast het register (welke plaatsen kunnen overslaan) een tweede, fijnere laag — **welke
plek raakt het net voor déze grondstof**.

## 2 · Het model

Een **aansluiting** is de plek waar één grondstof(-fase) het net raakt: een kade, een laadspoor,
een losplek. Eigen entiteit, eigen id, in `v2/data/aansluitingen.json`:

```json
{ "id": "cu-shanghai-concentraat",
  "grondstof": "copper",
  "fase": "erts",
  "naam": "Luojing — bulkkade aan de Yangtze",
  "knooppunt": "shanghai",
  "rol": "overslag",
  "plek": [121.4900, 31.4200],
  "aanhechting": { "zee": [121.48, 31.43], "binnen": [121.49, 31.41] },
  "bron": "OSM way/… (ODbL)" }
```

- **`plek` is de waarheid** (straatniveau, ~50 m, uit OSM), `aanhechting` is de aanloop naar het
  km-nauwkeurige net. De lader snapt elke aanhechting op zijn eigen net en **rapporteert de
  snap-afstand** — zelfde rolverdeling als het register: de machine meet, de redacteur oordeelt.
- **`knooppunt`** hangt de aansluiting op aan een aangewezen overslagpunt. Optioneel: een
  laadplek bij een mijn hoort bij geen enkele haven.
- **`rol`**: `laadplek` (vertrek) · `overslag` (van net naar net) · `losplek` (aankomst).
- **`fase`** volgt `data/*.js` (`erts` / `raffinaat` / `product`): concentraat en kathode
  verlaten dezelfde haven via verschillende kades, en dát is de reden dat de laag bestaat.

### Vier regels, elk met een al bewezen doodsoorzaak van het alternatief

1. **De aansluiting is AANGEWEZEN, niet gemeten.** Geen enkele afstandsdrempel kan zeggen welke
   kade bij welke grondstof hoort — dezelfde lege-interval-bevinding als bij de havens
   (`overslag-ontwerp.md` §2.2). De tool meet de snap en niets anders.
2. **De last mile wordt GETEKEND, niet verzwegen.** Tussen kade en netknoop zit een gat van
   honderden meters tot kilometers. Verzwijgen is precies de bug die bij de overslag-connector al
   is opgelost: de lijn "mist" dan een stuk en stopt schijnbaar in het niets.
3. **Een aansluiting VERVANGT het register niet, hij VERFIJNT het.** Zonder aansluiting valt een
   stroom terug op de generieke aanhechting van het knooppunt. Zo kan de laag grondstof voor
   grondstof groeien zonder dat er ooit iets breekt — het bewezen M5–M17-patroon.
4. **Een been mengt nooit netten.** Ongewijzigd; het is een constructie-eigenschap van de graaf.

## 3 · De router: de data kent de keten al

`data/*.js` draagt per stroom **de keten** (`via: [...]`) én **de modus per been** (`mode:
ship|rail|road|pipeline`). Dat is niet toevallig — het is het antwoord op de landbrug-vraag die
in `overslag-ontwerp.md` §5.2 is opgeschreven:

> *De atlas hoeft de modal split niet te raden — de flows-data draagt al `mode` per been. De
> simulator routeert bekende stromen langs hun opgegeven ketens; hij verzint geen vervoerskeuze.*

Dit is de niet-simulator-kant: **werkelijke stromen tonen, geen keuzes verzinnen.** Dus:

- een stroom = een rij aansluitingen: `laadplek → kade → kade → losplek`;
- per been **één net**, gezocht met de bestaande `zoekKeten` op `netten: [dat ene net]` en
  `maxOverstap: 0`, gezaaid op de aansluiting-coördinaten;
- **de overslag is geen zoekactie meer maar een feit**: twee opeenvolgende benen liggen op
  verschillende netten, op dezelfde plek. De witte ring komt op de aansluiting te staan, niet op
  de generieke havenknoop.

Waarom niet één `zoekKeten` over de hele reis: die zóekt de keten (lexicografisch minste
overslagen, dan km) terwijl de data hem al kent. Dat is de simulator, en die komt later.
`zoekKeten` blijft ongewijzigd staan voor de vrije haven→haven-vraag in de HUD.

## 4 · Wat je hieraan gaat zien (en dat is het punt)

Op straatniveau valt elk gat meteen op — Lars' werkregel: *"we moeten het vooral meemaken waar
iets ontbreekt."* Wat de pilot naar verwachting blootlegt:

- **De via-havens in `data/*.js` zijn grofkorrelig.** `cu-collahuasi` vaart daar via
  *Antofagasta*, terwijl de eigen `note` van die node al "Patache/Collahuasi-haven" zegt — en
  Collahuasi heeft daar een eigen terminal. Idem `cu-port-shanghai` = *Yangshan*: een
  containerhaven op eilanden voor de kust, geen concentraatkade en niet aan de Yangtze.
- **De aanloop wordt meetbaar.** Een aansluiting met een snap van 40 km zegt: hier houdt het net
  op, niet de werkelijkheid.
- **De geometrie-LOD.** Routes zijn op ~2 km gesampled; onder 5 km hoogte worden dat hoeken
  (`lod-ontwerpbrief.md`). Op de kade zelf zie je dat meteen.

## 5 · Wat dit bewust NIET doet

1. **Geen modale economie** — de modus komt uit de data, niet uit een kostenmodel.
2. **Geen aggregatie/hotspot-LOD, geen glow** — dat is de rest van M26 (`lod-ontwerpbrief.md`);
   deze stap gaat over positionele waarheid, niet over de look.
3. **Geen dikte-op-volume** — komt met de `Line2`-ribbon uit de LOD-brief.
4. **Geen nieuwe overslagmechaniek** — `zoekKeten` en `knooppunten.json` blijven exact zoals ze
   zijn; de bestaande invarianten (R'dam→Shanghai 19.610, Duluth→R'dam 8.031) mogen niet bewegen.

## 6 · De pilot (Lars' keuze, 2026-07-23)

Twee koperstromen, zodat **beide overslagsoorten** naast elkaar te bekijken zijn, en de hele
keten op straatniveau (mijn → kade → kade → fabriek):

| | stroom A — zee → rivier | stroom B — zee → spoor |
|---|---|---|
| bron | Collahuasi (Chili) | Escondida (Chili) |
| kade uit | Puerto Patache | Puerto Coloso |
| zeebeen | Stille Oceaan | Stille Oceaan |
| kade in | Shanghai, Yangtze-bulkkade | Ningbo-Zhoushan, Beilun |
| landbeen | Yangtze (binnenvaart) | spoor |
| bestemming | smelter Tongling | Jiangxi Copper, Guixi |

**Acceptatie:** de twee lijnen komen in hun eigen kade aan, op z17 ligt de lijn in het juiste
bekken, de last mile is zichtbaar, en de bestaande invarianten zijn onveranderd.
