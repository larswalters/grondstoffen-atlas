# Next actions — Grondstoffen Atlas
*Last updated: 2026-07-23 (M26.1 live `?v=065`: vier werkelijke stromen op straatniveau; volgende = healen + aansluitingen verfijnen)*

## 🔴 START HIER — DE TWEE NETGATEN HELEN

Het routeren van de stromen heeft ze aangewezen; ze zijn nu allebei exact benoemd mét getal,
en `verklaarGeenPad()` in `stromen.js` meldt ze uit zichzelf zodra iemand de stroom bekijkt.

* **Beilun-havenspoor** ligt op een eigen spoorcomponent van **1.823 km**, los van het
  Chinese hoofdnet (**402.762 km**) → `cu-escondida-guixi` krijgt geen treinpad. Vraagt een
  cross-component-heal op `landnet.bin`, dezelfde soort als het riviernet in [LAR-520].
  Hetzelfde geldt voor het al eerder gevonden **gefragmenteerde EU-spoor** (Antwerpen↔
  Duisburg) — één heal-ronde kan beide dekken.
* **Maasvlakte-riviergat:** de EMO-kade hecht op een **losstaand havenbekken van 4 km**,
  terwijl Duisburg op de doorgaande Rijn (**24.517 km**) zit → het kolen-Rijnbeen faalt
  terwijl koper 30 km verderop (Waalhaven) dezelfde reis wél maakt. Riviernet-fragmentatie,
  patroon van [LAR-520].

## ⚪ AANSLUITINGEN VERFIJNEN (Lars: "we laten het hierbij, verfijnen kan later")

* **Puerto Patache — de espesadores.** Collahuasi's eigen video geeft de keten ná de leiding:
  espesadores → planta de molibdeno → planta de filtro → stockpile → embarque. De leiding
  mondt uit bij de **indikkers**, niet bij de pier. Nu doet `cu-patache-kade` twee dingen
  tegelijk (eind van de leiding én begin van het zeebeen) terwijl dat twee plekken zijn met
  vier verwerkingsstappen ertussen. Eerlijke opzet: leiding → espesadores · terminalverwerking
  als *eigen verbinding* · zeebeen vanaf de pier. **Blokkade:** de espesadores staan niet in
  OSM (binnen 1,8 km kent de kaart vijf objecten, geen tank) → één coördinaat van Lars nodig.
* **Shanghai/Luojing** — nu de Baogang-bulkpier; concentraat voor de Yangtze-smelters lost in
  werkelijkheid vaak verder stroomopwaarts (Zhangjiagang/Jiangyin) of aan de eigen kade van
  de smelter.
* **Tongling** — de pier ligt 1,5 km van het smelterterrein; de smelter zelf heeft geen
  kade-tag in OSM.
* **Rotterdam/Duisburg** — OSM tagt bij géén van de gekozen kades wát er wordt overgeslagen;
  de toewijzing leunt op de buren binnen 1 km (ArcelorMittal Staalhandel / Metaalhandel
  Ketting bij de Waalhaven; Kokerei + Erzlager bij Schwelgern). Staat per aansluiting in de
  `noot`.

## ⚪ OPENSTAAND ONTWERPBESLUIT

* **Blijft "kleur = grondstof"?** De LOD-ontwerpbrief zegt van wel, maar de koperkleur
  (#E0965A) is op de Atacama en de Chinese kust onleesbaar — zandkleur op zandkleur. De pilot
  draait nu op vier contrastkleuren (Lars' eigen schets). Of de regel grondstof-gebonden
  blijft of per stroom mag verschillen hoort bij de rest van M26. Staat als `kleurnoot` in
  `v2/data/stromen-pilot.json`.
* **Pijpleidingen ooit tóch een net?** Voor slurry: nee (Lars' criterium — één product, twee
  punten, nooit een keuze). Voor **olie en gas ligt het anders**: Droezjba of Power of Siberia
  ís gedeelde infrastructuur waar een blokkade een echte herrouteringsvraag oplevert, en
  `data/*.js` heeft 36 pijpleidingstromen. Dán een eigen milestone, niet nu.

## ✅ AFGEROND 2026-07-23 — M26.1 · DE STROMEN OP STRAATNIVEAU

Live `?v=065` (commits `d5b2204` · `d8e86fd` · `0f4ba0b` · `5bc5997` · `4d1581e` · `17b5ac2` ·
`34f7a3a`). Vier werkelijke stromen, twee grondstoffen, been voor been over de gekoppelde netten.

- **`v2/data/aansluitingen.json`** — 15 aansluitingen per grondstof, coördinaten uit OSM (ODbL)
  via de nieuwe scout **`v2/tools/verken_terminals.py`**, gemeten door
  **`v2/tools/maak_aansluitingen.py`**.
- **`v2/src/stromen.js`** (three-vrij) + **`v2/src/stroomlaag.js`** (tekenen) — zelfde splitsing
  als `router.js`, zodat het routeren headless narekenbaar blijft.
- **`v2/data/pijpleidingen.json`** + **`v2/tools/fetch_pijpleidingen.py`** — de slurryleiding
  Collahuasi→Patache als tekengeometrie, 1.363 punten, 192,4 km (−3,8%).
- **`v2/design/stroom-aansluiting.md`** — het ontwerp, incl. §4a met Lars' net-criterium.
- `globe.js` kreeg **`vliegNaar(lon, lat, hoogteKm)`**; `keten.js` meet nu ook de componenten
  van land- én waternet zodat "geen pad" op elk net zijn reden draagt.
- **`toets_routes.mjs` 15/15 → 30/30 groen**; zee-invarianten onveranderd (19.610 / 89).

## ⚪ OUDER OPEN GELATEN

* **Drie wegcorridors zonder pad:** `bx-boke-katougouma`, `li-atacama-lanegra`,
  `ree-mountweld-leonora`.
* **89 atlas-plaatsen op een spoorcomponent <1.000 km** (New York op 0 km, Amsterdam op 87).
* **In "egaal" (tegellaag uit) blijft de vectorlaag onzichtbaar** — daar ís de bol het
  oppervlak, dus hij schrijft diepte en wint opnieuw.
* **Manaus→Rotterdam = "geen pad"** — Amazone-fragment raakt Macapá niet.
* **Drie datafouten in `data/*.js`** (zie `bugs-and-risks.md`), plus de nieuwe bevinding dat
  de via-havens daar te grofkorrelig zijn voor straatniveau.
