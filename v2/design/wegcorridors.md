# De wegcorridors — de lijst om één keer door te lopen

*M25 / [LAR-491] · opgesteld 2026-07-22 · status: **wacht op de redactieronde met Lars***

Dit is het stuk waar `memory/next-actions.md` naar verwijst met *"lijst één keer met Lars
doorlopen ná dit spoorwerk"*. Het bevat de afleiding, wat het bronnenonderzoek ervan
overliet, en de drie besluiten die aan Lars zijn.

---

## 1 · Waar de lijst vandaan komt

De atlas-data draagt **105 legs met `mode: "road"`** verdeeld over veertien grondstoffen.
Daarop zijn de drie filters uit het bronnenplan losgelaten:

| stap | over | eruit |
|---|---|---|
| alle `mode:"road"`-legs | 105 | |
| endpoint-type ≠ `market`/`exchange`/`hub` | 61 | 44 |
| > 150 km hemelsbreed | 37 | 24 |
| ontdubbeld op nabijheid (≤200 km herkomst, ≤100 km bestemming) | **24** | 13 |

24 corridors — precies de band van 20–40 die het plan voorspelde. Elk is daarna
onderzocht en door **twee sceptici met verschillende lens** aangevallen (modaliteit;
route-en-lengte): 24 onderzoekers + 48 weerleggers, geen fouten.

---

## 2 · Twee structurele bevindingen die vóór de lijst komen

### 2a · De meetlat bestaat grotendeels niet

Het bronnenplan gaat uit van *"elk één gelabelde polyline tussen twee ankers met een
gepubliceerde lengte ernaast"*. Van de 24 corridors leverden er **vijf** een gepubliceerde
weglengte op:

| corridor | gepubliceerd |
|---|---|
| Copperbelt → Durban | ~3.000 km |
| Lubumbashi → Dar es Salaam | 2.081 km |
| Boss Mining → Beira | 1.595 km |
| Arlit → Cotonou | ~1.600 km |
| Greenbushes → Kwinana | 250 km |

Voor de rest is er niets onafhankelijks. De onderzoekers vonden wél OSRM-afstanden en
**wezen die zelf af** met het juiste argument: OSRM routeert op OpenStreetMap, dus dat is
dezelfde bron als onze extract en dus geen scheidsrechter — precies het probleem dat de
wegmodus per definitie heeft. Spoor had NARN/RINF, water had USACE/CEMT; weg heeft niets.

> **Voorstel: de tussenpunten worden de toets.** Loopt de geroute lijn aantoonbaar via
> Kasumbalesa, Lusaka, Harare en Beitbridge, dán is het die corridor — ook zonder
> kilometergetal. Een topologische controle in plaats van een metrische. Waar wél een
> gepubliceerde lengte bestaat blijft die de tweede, hardere toets.

### 2b · Het filter ">150 km" is omgekeerd gecorreleerd met wegrelevantie

Dit kwam uit de kritiekronde en het klopt. Lange wegcorridors zijn meestal een *symptoom*
van ontbrekende infrastructuur (DRC, Niger). **Korte hauls zijn juist waar de weg
structureel de enige optie is** — mijn → spoorkop, mijn → grenspost — en juist daar
publiceert de operator vaak wél een afstand.

Slachtoffers van het filter, met naam:

* **Oyu Tolgoi → Gashuun Sukhait, 80 km** (bron: Rio Tinto zelf) — de enige exportroute
  van een van de grootste koperprojecten ter wereld.
* **Boké (SMB) → Katougouma, 27 km** — de grootste bauxietstroom ter wereld begint op een
  truckweg van 27 km, en sluit daarna aan op ons binnenwaternet.
* **Mount Weld → Leonora railhead, ~120 km** — de niet-Chinese tegenhanger van
  Mountain Pass, en een schoolvoorbeeld van de modusvraag (weg tot Leonora, spoor daarna).
* **Salar de Atacama → La Negra** — 100% tankwagen, geen pijpleiding, geen spoor.
* **Greenbushes → Kemerton, ~90–110 km** — valt weg terwijl Greenbushes → Kwinana (250 km)
  blijft; de dubbelnaam "Kwinana / Kemerton" maskeert dat het er twéé zijn.

En het scherpste geval: **Bingham Canyon**. Het concentraat gaat **27 km door een
pijpleiding** naar de smelter bij Magna, Utah. De atlas heeft daar dus twee fouten (modus
én bestemming), en *zodra je ze herstelt is de corridor 27 km en vermoordt het filter hem
alsnog*. Correctheid en overleven staan tegenover elkaar — dat is een ontwerpfout.

> **Voorstel: vervang de lengtedrempel door een rol-toets.** Houd de corridor als de weg de
> enige oppervlaktelink is tussen twee ankers van verschillend type (mijn→plant,
> mijn→spoorkop, plant→haven). Lengte wordt een **weergegeven attribuut, nooit een filter**.

### 2c · Het venster om de grootcirkel klopt niet — al gefixt

Het plan zei: *scanvenster = buffer van 50 km rond de grootcirkel tussen de ankers*. De
echte truckroute Kolwezi → Durban loopt via **Lusaka (155 km van die rechte lijn)** en
**Harare (362 km)**. Een buffer van 50 km mist de corridor volledig. Het venster ligt nu om
de lijn **anker → tussenpunten → anker** (`corridor_punten()` in `fetch_landnet.py`).

---

## 3 · De 24 kandidaten met hun oordeel

`weerlegd` = hoeveel van de twee sceptici de claim onderuithaalden.

### Bouwbaar als wegcorridor (8)

| # | corridor | modus | gepub. | weerlegd | opmerking |
|---|---|---|---|---|---|
| 2 | Copperbelt → Durban | weg | ~3.000 km | 0/2 | dé corridor van de atlas; **Kasumbalesa en Beitbridge horen als tussenanker** |
| 6 | Lubumbashi → Dar es Salaam | weg | 2.081 km | 0/2 | schoon; beste meetlat van de lijst |
| 7 | Boss Mining → Beira | weg | 1.595 km | 0/2 | schoon; Kasumbalesa als tussenanker |
| 5 | Arlit → Cotonou | gemengd | ~1.600 km | 2/2 | ⚠️ deels spoor; sinds de coup grotendeels stilgevallen |
| 3 | Mountain Pass → Fort Worth | weg | — | 1/2 | route klopt op de meeste knopen, lengte niet |
| 4 | Kachin → Ganzhou | weg | — | 1/2 | grenspost Ruili; wegroute is 2–3× de rechte lijn |
| 21 | Fresnillo → Torreón | weg | — | 1/2 | |
| 23 | Peñasquito → Torreón | weg | — | 1/2 | |
| 24 | Greenbushes → Kwinana | weg | 250 km | 1/2 | **hoort te splitsen in Kwinana én Kemerton** |

### Strandt op een centroïde (6) — er is geen punt om een lijn aan te hangen

| # | corridor | waarom |
|---|---|---|
| 9 | Bingham Canyon → "VS-raffinage (PNW)" | bestemming is een verzonnen aggregaat; in werkelijkheid 27 km **pijpleiding** naar Magna, Utah |
| 12 | Hunan-cluster → oostkust-smelters | beide uiteinden zijn clustercentroïdes |
| 13 | Zimbabwe-PGM → Springs | herkomst voegt Zimplats, Unki én Mimosa in één punt |
| 15 | Japan (schroot) → Toyo | herkomst is een landcentroïde; de route gaat over water |
| 18 | China (magneetschroot) → Ganzhou | herkomst is een regiocentroïde |
| 20 | Japan (urban mining) → Mitsubishi/Dowa | ⚠️ **draagt een lengte van 610,7 km tussen twee aggregaten** — een getal dat niets meet maar op bewijs lijkt. Moet op `null`. "Mitsubishi / Dowa" zijn niet eens twee plaatsen maar twee bedríjven |

### Is in werkelijkheid een andere modus (3)

| # | corridor | werkelijkheid |
|---|---|---|
| 8 | Lai Chau → Ganzhou | modus niet vast te stellen; geen wegcorridor |
| 10 | Barro Alto/Onça Puma → Vitória | gemengd weg-spoor; bevestigd door IBRAM. Bovendien voegt de herkomst twee mijnen samen die ~700 km uit elkaar liggen (Goiás vs Pará) |
| 16 | Garpenberg → Rönnskär | gemengd weg-spoor; 2/2 weerlegd |

### Twijfel (6) — mijn advies staat erbij

| # | corridor | advies |
|---|---|---|
| 1 | Redwood NV → Novonix TN | **niet bouwen.** Geen enkele bron beschrijft deze stroom: Novonix maakt synthetisch grafiet uit needle coke van Phillips 66 (Lake Charles), Redwood's anodeproduct is koperfolie. De lading bestaat niet |
| 11 | Naaldcokes → Novonix | herkomst voegt Lake Charles en Seadrift samen; kies Lake Charles |
| 14 | HyProMag → Hanau | kruist het Kanaal; geen pure wegcorridor. Eén scepticus vond bovendien een harde routefout |
| 17 | Umicore → Aurubis | modus niet vastgesteld |
| 19 | Arezzo → Valcambi | 0/2 weerlegd, maar herkomst voegt Arezzo en Vicenza samen (~250 km uit elkaar) |
| 22 | Bushveld → Rustenburg | hoge zekerheid maar dubbelnaam; Amandelbult valt mogelijk onder 150 km |

---

## 4 · Wat er ontbreekt — 12 corridors die de lijst niet kon vinden

Gevonden door de completeness-agent. Gesorteerd op belang; lengtes alleen waar
gepubliceerd.

| corridor | lengte | waarom hij ertoe doet |
|---|---|---|
| **Las Bambas → Pillones** (Peru) | **435 km weg** (+ 295 km spoor naar Matarani) | 's werelds politiek beruchtste mijntruckcorridor. ⚠️ **eindigen bij Pillones, niet Matarani** |
| **Tavan Tolgoi → Gashuunsukhait** (Mongolië) | **239–250 km** | grootste kolentruck-haul ter wereld; 11–12.000 trucks, files tot 85 km |
| **Zambiaanse Copperbelt → Kasumbalesa** | — | de atlas heeft **geen enkele Zambiaanse koperstroom**; Kasumbalesa doet 500–900 trucks/dag |
| **Oyu Tolgoi → Gashuun Sukhait** | **80 km** (Rio Tinto zelf) | enige exportroute; beste bronkwaliteit van de lijst |
| **Kathleen Valley → Geraldton** (WA) | **700 km** (Liontown) | zelfde archetype als Greenbushes maar 3× zo lang, volledig weg |
| **Salar de Atacama → La Negra** (Chili) | — | kern van de lithiumketen, 100% tankwagen. Grootste inhoudelijke scheefstand |
| **Goulamina → Abidjan** (Mali/Ivoorkust) | 195 km tot Bamako | West-Afrika's eerste hardrock-lithiummijn |
| **Walvis Bay → Ndola/Lubumbashi** | 2.524 km ⚠️ zwakke bron | westelijke uitweg van de Copperbelt |
| **Zimbabwe-lithium → Machipanda → Beira** | — | volledig weg; beleidsgevoelig (exportverbod feb. 2026) |
| **Boké (SMB) → Katougouma** (Guinee) | **27 km** | grootste bauxietstroom ter wereld; sluit aan op ons binnenwaternet |
| **Mount Weld → Leonora railhead** (WA) | ~120 km | ⚠️ **stoppen bij Leonora**, daarna spoor |
| **Man Maw/Wa State → Muse–Ruili** (Myanmar) | — | de tinstroom; andere gate dan de REE-stroom van #4 |

**Expliciet getoetst en afgewezen:** de **Lobito-corridor** is spoor, geen weg.

---

## 5 · Drie besluiten voor Lars

1. **De acceptatietoets.** Tussenpunten in plaats van lengte (§2a)? Of alleen corridors
   bouwen die een gepubliceerde lengte hebben — dan blijven er vijf over.
2. **Het lengtefilter.** Vervangen door een rol-toets (§2b)? Dat haalt Oyu Tolgoi, Boké,
   Mount Weld, Atacama en Kemerton binnen, en het is de enige manier waarop Bingham Canyon
   correct én aanwezig kan zijn.
3. **De uiteindelijke lijst.** Mijn voorstel: de **8 bouwbare min #5 (Arlit, deels spoor)**
   = 7, plus de **7 sterkste ontbrekende** (Las Bambas, Tavan Tolgoi, Oyu Tolgoi, Kathleen
   Valley, Atacama, Boké, Mount Weld) = **14 corridors** om mee te beginnen. De
   centroïde-gevallen niet bouwen maar terugmelden aan de datalaag — dat zijn echte fouten
   in `data/*.js`, geen corridorprobleem.

---

## 6 · Wat er al staat om dit uit te voeren

In `v2/tools/fetch_landnet.py`:

* `weg_houden()` + `WEG_HOUD` (`motorway` t/m `secondary`) — ruim, omdat
  `highway=motorway` gemeten 0 km geeft in Zambia én DR Congo; de scope komt van het
  venster, niet van de tag
* `corridor_punten()` / `_vensters_voor()` / `_raakt_venster()` — het corridorvenster om
  anker → tussenpunten → anker
* de cachevingerafdruk dekt nu het wegfilter én de corridorvensters, zodat een gewijzigde
  lijst niet stilzwijgend het oude scanresultaat teruggeeft
* `CORRIDORS = []` — leeg tot dit stuk is doorgenomen

Nog te plakken (staat klaar): de routering zelf — vertex-graaf over de gescande wegen,
Dijkstra per been langs de tussenpunten, `refs` als zachte voorkeur (factor 3) in plaats
van een hard filter, en de lengtetoets waar een gepubliceerd getal bestaat.
