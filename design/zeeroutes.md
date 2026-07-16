# Ontwerp — Realistische zeeroutes (M18)

*Spec vóór code, conform runbook sectie I stap 2. Hoort bij Linear **LAR-473**; de bouw-issues
(LAR-474 pilot · LAR-475 build-stap · LAR-476 engine · LAR-477 uitrol · LAR-478 verificatie) bouwen
hiertegen. Geschreven 2026-07-17.*

> **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje
> vertelt zichzelf. Een route die 1.090 km omvaart is geen cosmetisch probleem: het is een onwaarheid
> in de kaart, en de features van M19–M21 (impact-teller, disruptie-simulator) staan erop.

---

## 1. De diagnose — waarom de zee-A\* eruit gaat

De zee-routing is aantoonbaar onrealistisch. Drie samenwerkende oorzaken in `src/searoute.js`
(let op de naam: dat is **onze eigen A\***, niet de gelijknamige Python-library):

| # | oorzaak | gevolg |
|---|---|---|
| 1 | **`openRadiusDeg: 1.2`** (`config.js:252`) — een schijf van ~130 km geforceerd water rond élk knelpunt. Nodig omdat de Straat van Lombok (~35 km) dichtslibt in een 0,25°-raster (~28 km/cel). | Zet óók **land** op "water" → A\* vaart vlak bij een knelpunt dwars over schiereilanden en eilandjes. **Hoofdboosdoener.** |
| 2 | **8-richtingen-A\*** | Trapjes. Golf→Rotterdam = **33 richtingswissels**. |
| 3 | **Grof raster + `heuristicWeight: 1.35` + géén vaarlanen** | Het vindt het kortste **watertraject**, niet de lane die schepen varen → kaarsrechte runs langs een breedtegraad. |

**Het bewijs (Antofagasta→Shanghai):**

| | afstand | t.o.v. grote cirkel |
|---|---|---|
| grote cirkel | 18.526 km | — |
| searoute (MARNET, echte lanen) | 18.880 km | **+2%** |
| **onze bol** (zuidelijk via `wp-pac-zuid` op 26°Z) | **19.970 km** | **+8%** |

Het handgeplaatste vaarpunt `wp-pac-zuid` (−26,00 / −125,00) dwingt **~1.090 km omweg** af — ongeveer
een week varen. Conservatief gemeten (via-keten als kale grote-cirkels; het echte A\*-pad mét trapjes
is langer).

## 2. Wat er voor in de plaats komt

Geen beter raster — een **ander soort ding**. De Python-library `searoute` (1.6.0, al geïnstalleerd)
doet Dijkstra over **MARNET**: een echt scheepvaartnetwerk (`marnet_searoute.geojson`, 729 KB +
`ports.geojson`, 721 KB).

| | nu (`src/searoute.js`) | straks (Python `searoute`) |
|---|---|---|
| model | A\* over **raster** (0,25°/cel) | Dijkstra over **graaf** |
| data | landpolygonen op canvas | MARNET-lanen + havens |
| zoekt | kortste **watertraject** | kortste pad over **echte vaarlanen** |
| knelpunt is | een gat in een landmasker | een **edge** (→ M21 kan 'm verwijderen) |
| draait | runtime, elke sessie | **build-time, één keer** |

De kern is dat een zeestraat een **edge** wordt in plaats van een verzameling rastercellen. Dat is wat
M21 (knelpunt blokkeren = edge eruit → herrouteren) pas echt mogelijk maakt — en waarom M21's oude
raster-masker-aanpak hiermee herijkt is.

### Empirisch geverifieerd (2026-07-17, deze sessie)

De `restrictions`-parameter doet precies wat M21 nodig heeft. Golf (Ras Tanura) → Rotterdam:

| scenario | afstand | uitkomst |
|---|---|---|
| normaal | **12.066 km** | door Suez |
| `restrictions=['suez']` | **20.924 km** | automatisch om **Kaap de Goede Hoop** — **+73%** |
| `restrictions=['ormuz']` | **0 km** ⚠️ | *"No path found"* — zie §6 |

Beschikbare restricties: `suez` · `panama` · `ormuz` · `malacca` · `bosporus` · `babalmandab` ·
`gibraltar` · `sunda` · `bering` · `northwest` · `chili` · `south_africa`.

Daarnaast geeft `return_passages=True` een veld **`traversed_passages`** — de router vertelt zélf
welke doorgangen een route gebruikt (Golf→Rotterdam: `['suez','babalmandab','gibraltar','ormuz']`).
**Waarde:** "welke stromen raakt Hormuz?" wordt een **query op de cache** in plaats van handmatige
annotatie — en het is een gratis **kruiscontrole** op onze eigen `via`-ketens en `tensions`.

## 3. Datamodel — `data/_searoutes.js`

Eén gedeelde corridor-cache over alle 14 grondstoffen, gededupliceerd per haven-paar.
Lars' observatie *"voor veel grondstoffen zijn de routes vrijwel hetzelfde"* is gemeten en klopt:

```
987 zee-legs  →  381 unieke corridors     (dedup-winst 61%)
```

### Gemeten bestandsgrootte (steekproef 12 representatieve corridors, geëxtrapoleerd naar 381)

| precisie | ≈ nauwkeurigheid | raming totaal |
|---|---|---|
| 2 decimalen | ~1,1 km | 319 KB |
| **3 decimalen** | **~110 m** | **357 KB** |
| 4 decimalen | ~11 m | 397 KB |
| 5 decimalen | ~1 m | 429 KB |

**→ Besluit: 3 decimalen.** Reden: 110 m is ruim sub-pixel op een wereldbol bij elke zoom die de
atlas toelaat, en de 38 KB boven 2 decimalen is goedkope verzekering tegen zichtbare knikken bij
sterk inzoomen. Netlify serveert gzipped, dus de effectieve kosten liggen lager. Gemiddeld ~61 punten
per corridor; **geen extra decimatie** (Douglas-Peucker) in M18 — pas overwegen als de standalone-build
in de praktijk te zwaar blijkt. *(Referentie: `atlas-standalone.html` is nu ~1.809 KB → +357 KB ≈ +20%,
waar de A\*-rasteropbouw van ~46 ms + alle runtime-A\*-runs tegenover verdwijnen.)*

### Sleutelformaat

**→ Besluit: coördinaat-paar, genormaliseerd en gesorteerd.**

```js
// data/_searoutes.js
const SEAROUTES = {
  // sleutel: "<lat>,<lon>|<lat>,<lon>" — beide punten op 3 decimalen, paar gesorteerd (A|B == B|A)
  "-23.650,-70.400|31.230,121.800": [[-23.65,-70.40], [-20.23,-70.63], /* … */ [31.23,121.80]],
};
```

Reden voor coördinaat i.p.v. node-id: **robuust bij hernoemde nodes** (en de atlas hernoemt: zie de
Roberts Bank→Ridley-verplaatsing bij M17), en het maakt de cache **grondstof-agnostisch** — precies
wat de dedup nodig heeft, want Antofagasta→Ningbo is voor koper/zilver/nikkel letterlijk dezelfde
sleutel. Kosten: minder leesbaar bij handmatig debuggen. Mitigatie: schrijf de node-ids als commentaar
achter elke corridor (kost niets in gzip, en de build genereert het toch).

**Sorteren van het paar** maakt de cache richtingsonafhankelijk (heen = terug omgekeerd). De generator
draait dus per corridor één searoute-run, en `flows.js` keert de polyline om als de leg andersom loopt.

### Determinisme

Gesorteerde sleutels, vaste afronding, geen tijdstempel in het bestand. Zelfde input → byte-identieke
output, anders geeft elke build een dirty diff.

## 4. Hoe `flows.js` het gebruikt

De leg-logica (`src/flows.js:180-195`) blijft structureel intact. Eén tak verandert:

```js
if (shipMode && seaA && seaB) {
  leg = Routing.sea(a, b);        // NU:     live A*
  leg = SeaCache.lookup(a, b);    // STRAKS: lookup in _searoutes.js
}
```

**Ongemoeid — geen regel wijzigen, de regressie moet het bewijzen:**
- **Land** (`road` / `rail` / `pipeline`) → `Routing.land` blijft precies zoals het is.
- **Lucht** (`air`) → great-circle, blijft zoals het is (goud/PGM/diamant zijn volledig air-mode).
- **Vaarbanen** (`laneShape` in `util.js`) → zie de waarschuwing in §5.

### Fallback bij een ontbrekende corridor

**→ Besluit: hard falen, zichtbaar.** Geen stille terugval naar de oude A\*.

Reden: een stille fallback is precies hoe je een kapotte route jarenlang niet ziet. Concreet:
`console.warn` met de exacte coördinaten + de leg wordt **niet gerenderd** (niet als rechte lijn —
dan lijkt het te werken). De headless legs-check telt ze als **kapot** → de bestaande
verificatie-lat (0 kapot) vangt het automatisch af. De ontbrekende corridors zijn per definitie
build-time bekend, dus dit hoort in de praktijk nooit te vuren; als het vuurt is de build stuk.

**Bijbehorende regel in de generator (LAR-475):** een corridor die searoute niet kan routeren, faalt
de build. Niet loggen-en-doorgaan. Dat zijn exact de coördinaten die een handmatig duwtje nodig
hebben (het M13/M17-patroon: kandidaat-coördinaat empirisch toetsen, dán de node verplaatsen).

## 5. ⚠️ De subtielste regressie-val — `laneShape`

`flows.js` zet een **anker** op elke tussenstop:

```js
if (i < stops.length - 2) anchors.push(routePts.length - 1);   // flows.js
```

`laneShape` maakt de zijwaartse verschuiving **nul bij elk anker** en maximaal ertussenin. Dat is het
kernbeeld van de atlas (M3): parallelle stromen waaieren uit en **knijpen samen bij een knelpunt**.

**Gevolg dat verder gaat dan een regressie:** zolang `wp-pac-zuid` in de via-keten staat, knijpen álle
Chili/Peru→China-koperstromen samen op **26°Z / 125°W** — midden op de open Stille Oceaan, waar niets
is. Dat is niet alleen een omweg, het is een **visuele leugen**: de kaart tekent een flessenhals die
niet bestaat. Zie §6.

Bij oplevering (LAR-478) **expliciet checken** dat de waaier bij de échte knelpunten nog samenknijpt.

## 6. ⚠️ "Geen route" is een geldige uitkomst — en de interessantste

Hormuz dicht gaf **`length: 0` + een `UserWarning`** — geen exception. Ras Tanura ligt *binnen* de
Golf: Hormuz dicht betekent niet "een langere route", maar **geen route**.

Dat is fysiek correct en het is precies het verhaal dat de atlas vertelt: **Suez dicht is duur
(+73%), Hormuz dicht is: het houdt op.**

**Regel:** `length == 0` / no-path **nooit** als getal doorgeven. Als M21 dat niet afvangt verschijnt
er "0 km" in een impact-teller — de sneakiest bug denkbaar, en exact het soort stille fallback dat §4
verbiedt. Een geblokkeerde corridor moet als **geïsoleerd** gerenderd/geteld worden, niet als nul.

## 7. Netwerk bewaren voor M21 — de keuze

De restricties draaien in **Python, build-time**. De atlas draait **pure JS** met gebakken polylines.
Voor M21 (disruptie-simulator) zijn er dus twee wegen:

| | aanpak | voor | tegen |
|---|---|---|---|
| **(a)** | **Scenario's vooraf bakken** — per knelpunt een set corridors (~12 restricties × 381 corridors) | Runtime blijft dom en snel; geen router in JS | Alleen vooraf bedachte scenario's; **combinaties** (Suez *én* Hormuz) exploderen; bestand groeit fors |
| **(b)** | **MARNET meesturen** (729 KB geojson) + Dijkstra in JS | Élke edge live weghaalbaar, ook combinaties; gebruiker mag zelf klikken | +729 KB; je bouwt de router deels na in JS |

**→ Besluit voor M18: geen van beide nu bouwen.** M18 hoeft alleen de routes goed te krijgen. Wat M18
wél moet doen om (b) later niet onmogelijk te maken:

1. **`traversed_passages` per corridor meeschrijven** in `_searoutes.js`. Kost een paar bytes, en het
   geeft M21 gratis "welke stromen raakt knelpunt X?" — óók in variant (a).
2. **De generator parametriseerbaar houden** op `restrictions`, zodat (a) later een build-vlag is en
   geen herschrijving.

De (a)/(b)-keuze valt bij **M21 zelf**, met de dan gemeten bestandsgrootte erbij. Niet nu vooruitbouwen
aan iets dat drie milestones verderop ligt.

## 8. 🔴 Het open besluit (Lars) — via-punten op zee-legs

**Dit is de scharnierbeslissing van de milestone.** Zie `data/_chokepoints.js`: de data maakt het
onderscheid **al** via `marker`.

**Blijven hoe dan ook — echte fysieke doorgangen** (`marker: true`; searoute volgt ze by-design, en ze
zijn `tension`-ankers voor `laneShape`):
`wp-malakka` · `wp-lombok` · `wp-makassar` · `wp-taiwan` · `wp-suez` · `wp-bab` · `wp-hormuz` ·
`wp-panama` · `wp-kaap` · `wp-gibraltar` · `wp-bosporus` · `wp-deense-straten` · `wp-dover`.
`grens-*` blijft sowieso (landkaart, raakt zee-legs niet).

**Kandidaat om te sneuvelen — navigatie-hulpjes** (`marker: false`; bestonden alleen om het kale A\*
te sturen), met gemeten gebruik:

| vaarpunt | gebruikt in | | vaarpunt | gebruikt in |
|---|---|---|---|---|
| `wp-rode-zee` | 15 stromen | | `wp-atl-west` | 3 |
| `wp-moz-noord` | 10 | | `wp-dardanellen` | 3 |
| `wp-pac-noord` | 10 | | `wp-cabot` | 1 |
| `wp-florida` | 9 | | `wp-st-laurent-1…4`, `-2b` | 1 elk |
| `wp-atl-brazilie` | 6 | | `wp-kaspisch-n/-m/-z` | 1 elk |
| `wp-golf-mexico` | 6 | | `wp-aceh`, `wp-singapore`, `wp-scs`, | |
| `wp-caribisch` | 5 | | `wp-pac-zuid`, `wp-pac-west`, `wp-zuid-australie` | |

### De twee opties

- **(a) Opruimen** — navigatie-hulpjes uit de via-ketens slopen. Antofagasta→Ningbo wordt gewoon
  haven→haven; searoute doet de rest.
- **(b) Behouden als hint** — laten staan en searoute er doorheen dwingen.

### Gemeten: bestandsgrootte is géén argument

```
(b) via-punten behouden : 987 legs → 381 unieke corridors
(a) navigatie-hulpjes weg: 698 legs → 340 unieke corridors
→ 41 corridors minder (11% kleiner)
```

De dedup vangt het meeste al weg. **De keuze moet dus puur op realisme, niet op omvang.**

### Aanbeveling: (a) — opruimen

Drie redenen:
1. **De omweg verdwijnt.** `wp-pac-zuid` kost ~1.090 km die er niet hoort te zijn.
2. **De valse flessenhals verdwijnt** (§5). Zolang het punt een anker is, tekent `laneShape` een
   knijppunt op open oceaan. Opruimen fixt de route én het plaatje.
3. **Je geeft searoute geen boeimarkering die er niet hoort.** MARNET wéét waar schepen varen; een
   handgeprikt punt uit het A\*-tijdperk kan die kennis alleen maar overrulen.

**Nuance / uitzonderingen die apart bekeken moeten:** de `wp-st-laurent-*`-keten en `wp-kaspisch-*`
zijn géén gewone navigatie-hulpjes — ze forceren een **ingesloten watercorridor** (Saint-Laurent-rivier;
de Kaspische Zee is een gesloten zee die MARNET mogelijk niet dekt). Die vallen waarschijnlijk buiten
searoute's netwerk en moeten in de pilot **empirisch** getoetst worden vóór ze sneuvelen. Zelfde geldt
voor `wp-dardanellen`.

> ### ✅ BESLIST (Lars, 2026-07-17): **(a) opruimen — mét de ingesloten-water-nuance**
>
> De navigatie-hulpjes op **open water** gaan uit de via-ketens. De **ingesloten-water-ketens**
> (`wp-st-laurent-1…4` + `-2b`, `wp-kaspisch-n/-m/-z`, en `wp-dardanellen`) worden **individueel
> empirisch getoetst** vóór ze sneuvelen — eerst door searoute halen, dán pas slopen. Dat is het
> M13/M17-patroon: kandidaat toetsen, niet gokken.
>
> Reden: (1) de ~1.090 km omweg van `wp-pac-zuid` verdwijnt; (2) de **valse flessenhals** verdwijnt —
> `laneShape` tekent nu een knijppunt op 26°Z/125°W waar niets is (§5); (3) een handgeprikt punt uit
> het A\*-tijdperk kan MARNET's lane-kennis alleen maar overrulen. Omvang speelde géén rol in de keuze
> (11%, zie boven) — dit is puur een realisme-besluit.

## 9. Verificatie-criterium — wat is "goed"?

De bestaande lat blijft: **per grondstof X legs / 0 kapot / 0 straight / 0 degenerate / 0 onbekende
via-ids**, geen console-warnings.

**Nieuw, wat M18 pas mogelijk maakt — de realisme-check:** per zee-leg de verhouding
**routelengte ÷ grote-cirkelafstand**.

**→ Drempel: Y = 15%.** Elke corridor die >15% boven z'n grote cirkel ligt moet een **aanwijsbare
reden** hebben, en die reden is opvraagbaar via `traversed_passages`. Legitiem: Kaap/Suez/Panama-omwegen,
en alles wat om een continent heen moet (Golf→Rotterdam via Suez = +73% t.o.v. de grote cirkel en is
volstrekt correct — een grote cirkel gaat daar dwars over Arabië). **Verdacht:** een corridor over open
water met >15% en géén doorgang in `traversed_passages`. Dat is precies de `wp-pac-zuid`-signatuur.

De check is dus niet "afwijking >15% = fout", maar "**afwijking >15% zonder doorgang = fout**".

## 10. Harde regels voor deze milestone

1. **Vergelijk nooit tegen een kale `Routing.sea(o, d)` / `searoute(o, d)`-run.** De pilot van
   2026-07-16 deed dat, zónder `via`-ketens, en produceerde "route A": een noordelijk pad over 43°N
   dat de bol **nergens tekent**. Lars zag het onmiddellijk: *"ik zie op onze wereldbol niets dat
   route A neemt."* De vergelijking was daardoor ongeldig.
   *Deze fout is op 2026-07-17 gereproduceerd bij het schrijven van deze spec: een kale
   Antofagasta→Shanghai-run gaf 18.864 km over **50,7°N** — dezelfde spookroute. Het is een makkelijke
   fout om te maken; vandaar dat 'ie hier bovenaan staat.*
   **→ Vergelijk altijd tegen het pad dat `flows.js` daadwerkelijk rendert** (mét via-keten).
2. **Browser-pane cachet script-tag-files hardnekkig** (geen no-cache op python `http.server`).
   Valideren via in-memory injectie of een tweede server-instance op een andere poort (schone origin) —
   **niet** via `reload()`.
3. **Sectie J (parallel werk):** dit raakt gedeelde bestanden (`build-standalone.py`, `src/flows.js`,
   `config.js`, nieuwe `data/_searoutes.js`). Draait er een parallelle grondstof-sessie? Stage alléén
   eigen bestanden, nooit `git add -A`.

## 11. Openstaand — te beslissen door Lars

| # | besluit | status |
|---|---|---|
| 1 | **Via-punten: (a) opruimen of (b) hint?** (§8) | ✅ **(a) opruimen** — beslist door Lars 2026-07-17; ingesloten-water-ketens individueel empirisch getoetst |
| 2 | Sleutelformaat: coördinaat-paar | ✅ voorstel vastgelegd (§3) |
| 3 | Precisie/decimatie: 3 decimalen, geen extra decimatie | ✅ voorstel vastgelegd (§3) |
| 4 | Fallback: hard falen | ✅ voorstel vastgelegd (§4) |
| 5 | Netwerk voor M21: nu niet bouwen, wél `traversed_passages` meeschrijven | ✅ voorstel vastgelegd (§7) |
| 6 | Realisme-drempel Y = 15% zónder doorgang | ✅ voorstel vastgelegd (§9) |

## 12. Bronnen

- `searoute` 1.6.0 (Python), data: `marnet_searoute.geojson` (729 KB) + `ports.geojson` (721 KB) —
  MARNET, EMODnet/Eurostat-lijn.
- Alle cijfers in §1–§3 en §8 zijn **gemeten op deze repo** op 2026-07-17 (14 grondstoffen geladen uit
  `data/`, zee-legs geteld zoals `flows.js` ze routeert: `from` + `via` + `to`).
- Diagnose + Antofagasta-bewijs: `memory/decisions.md` (2026-07-17), `CLAUDE.md` §diagnose.
