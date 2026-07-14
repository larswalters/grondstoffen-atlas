# Grondstoffen-atlas — v2

## Starten

**Aanbevolen — via een lokale server** (dan werken ook de lokale textures):

```bash
cd atlas
python3 -m http.server 8000
# open http://localhost:8000
```

**Of gewoon dubbelklikken op `index.html`.** Dat werkt ook: `config.js` staat op
`basemap.source: "cdn"`, dus de aardbol-textures komen van jsDelivr. Zonder
internet valt hij automatisch terug op de zelfgetekende vectorkaart.

> Waarom een server? Browsers blokkeren `file://`-afbeeldingen in WebGL
> (CORS/tainted textures). Wil je de textures uit de map `textures/` gebruiken,
> zet dan `source: "local"` **én** draai een server.

## Structuur

```
config.js            alle knoppen: kleuren, groottes, snelheden, kaartstijl
geo-data.js          achtergrondkaart (Natural Earth, ongewijzigd)
textures/            4 aardbol-textures (satelliet, nacht, donker, reliëf, water)

data/_registry.js    het schema + REGISTER()
data/lithium.js      ← volledig uitgewerkt, gebruik dit als voorbeeld
data/cobalt.js       ← automatisch overgezet, nog "basis"
data/…               één bestand per grondstof

src/util.js          geometrie-hulpjes
src/globe-core.js    scene, camera, slepen/zoomen, renderloop  (weet niets van data)
src/basemap.js       het aardoppervlak: textuur + reliëf + scherpe grenzen
src/markers.js       de locaties
src/flows.js         de stromen
src/ui.js            knoppen en panelen
src/main.js          knoopt alles aan elkaar
```

Elk onderdeel is los te vervangen. Wil je een andere aardbol? Alleen
`basemap.js` + `config.js`. Andere markers? Alleen `markers.js`.

## Wat er nieuw is aan de aardbol

- **Echte satelliettextuur** van 4096×2048 in plaats van een getekende kaart.
- **Reliëf** (bump map) en een **watermasker**, zodat alleen de zee glimt.
- **Kustlijnen en grenzen als 3D-lijnen** bovenop de textuur — die blijven
  haarscherp als je inzoomt, terwijl een textuur wazig wordt.
- Vier stijlen, schakelbaar rechtsboven: satelliet · nacht · donker · vector.

## Een grondstof uitwerken

Open het bestand in `data/`, en breid `nodes` en `flows` uit. Het schema staat
bovenaan `data/_registry.js`; `data/lithium.js` laat zien hoe het eruit ziet als
het af is.

Een node:

```js
{ id: "li-greenbushes", type: "mine", name: "Greenbushes", country: "Australië",
  lat: -33.86, lon: 116.06, share: 30, operator: "Talison", status: "actief",
  capacity: "±1.500 kt/j", note: "Grootste hardrock-lithiummijn ter wereld." }
```

- `type`: `mine` (bol, grootte = `share`) · `refinery` (ruit) · `port` (kubus) ·
  `market` (ring)
- `status`: `actief` · `project` · `gepland` (projecten worden halftransparant)

Een stroom:

```js
{ from: "li-greenbushes", to: "li-ref-jiangxi", value: 60, mode: "ship",
  note: "De dikste lithiumstroom ter wereld." }
```

- `value` bepaalt de **dikte** van de boog en het aantal deeltjes, relatief aan
  de grootste stroom van diezelfde grondstof.
- `mode`: `ship` (doorgetrokken) · `pipeline` / `rail` / `road` (gestreept)

Zet `detail: "uitgewerkt"` zodra een grondstof af is — dan krijgt de knop een
"detail"-label.

## Volgorde van aanpak

1. ✅ lithium — af
2. kobalt, koper, nikkel, zeldzame aardmetalen, grafiet, PGM, uranium, aardolie
   — staan in het nieuwe format maar hebben nog de oude, grove data
   (mijnen op landniveau, stromen alleen mijn→dichtstbijzijnde raffinaderij).

Per grondstof herhalen we dezelfde stap: echte mijnen en fabrieken met naam en
coördinaat, en de werkelijke handelsroutes met volume en transportmodus.

## Bronnen / betrouwbaarheid

De cijfers zijn indicatief en afgerond, gebaseerd op openbare bronnen (USGS
Mineral Commodity Summaries, IEA, jaarverslagen van producenten). Ze tonen
verhoudingen, geen handelsstatistiek. Bij elke grondstof staat bovenaan het
databestand waar de getallen vandaan komen en hoe ze gelezen moeten worden.
