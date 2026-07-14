# Grondstof-brief — TEMPLATE

*Kopieer dit bestand naar `data/<grondstof>.md` (naast `data/<grondstof>.js`) en vul het in
**vóór** je de `.js` schrijft. Dit is de "eerst ontwerpen"-stap: alle nodes + stromen op een rij,
zodat het coderen daarna alleen nog invullen is. Voorbeeld volledig ingevuld: `data/lithium.md`.*

> **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje
> vertelt zichzelf. Zoek dus eerst de **echte vorm** van deze grondstof: waar zit de flessenhals/
> het knelpunt (geografisch of institutioneel), en wat zou de kaart automatisch moeten laten zien?

---

## 0. Metadata (→ `REGISTER({...})` in de `.js`)

| veld | waarde | toelichting |
|---|---|---|
| `id` | `<grondstof>` | kleine letters, = bestandsnaam |
| `name` | | NL-naam |
| `symbol` | | scheikundig symbool of afkorting |
| `color` | `#______` | grondstofkleur (volle `raffinaat`-kleur) |
| `unit` | | eenheid waarin álle volumes staan, bijv. `kt LCE/jaar` of `t/jaar` — hele keten optelbaar |
| `detail` | `basis` → `uitgewerkt` | niveau na invullen |
| `blurb` | | 1–2 zinnen: de kern + waar de flessenhals zit |

## 1. Het verhaal in 3 zinnen
*(Wat komt er automatisch uit het plaatje als het klopt? Waar zit de trechter?)*
1.
2.
3.

## 2. De keten & stages (→ `stage`-codes + booghoogte/kleur)
De stages bepalen kleur + booghoogte op de kaart (ruw = laag/gedempt, eindproduct = hoog/licht).
Standaard drie; pas de codes aan de grondstof aan (moet matchen met de stage-styling in de code).

| stap | `stage`-code | kleur | booghoogte | eenheid |
|---|---|---|---|---|
| 1. winning → ruw | `erts` | donker/gedempt | laag (kruipt over oppervlak) | |
| 2. raffinage → bewerkt | `raffinaat` | volle grondstofkleur | midden | |
| 3. eindproduct/cel | `product` | licht, bijna wit | hoog | |

## 3. Nodes (locaties)
*Velden per node (→ `nodes: [...]`):*
`id` · `type` (mine/refinery/port/plant/hub/vault/cb/airport/recycler…) · `name` · `country` ·
`lat` · `lon` (**west = negatief, dubbelcheck!**) · `share` (% wereldproductie, actieve bronnen) **óf**
`potential` (voor projecten, géén share) · `tier` (1 = draagt het verhaal/altijd zichtbaar,
2 = havens & middelgroot/bij inzoomen, 3 = detail) · `operator` · `status` (actief/project) ·
`capacity` · `note` · optioneel `coastal: true` (fabriek pal aan de kade → mag zelf de zee op).

> ⚠️ Nieuwe `type`-waarden (bijv. `airport`, `vault`, `cb` voor goud) moeten een marker-stijl krijgen
> in de rendering-laag — noteer dat als bouw-TODO.

### 3a. Winning / bron (actief — met `share`)
| id | naam | land | lat | lon | share | tier | operator | capacity | note |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

### 3b. Winning / bron (projecten — met `potential`, geen share)
| id | naam | land | lat | lon | potential | status | note |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### 3c. Raffinage / bewerking
| id | naam | land | lat | lon | share/capacity | tier | operator | note |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

### 3d. Havens / gateways / knooppunten
*(havens `*-port-*`; voor luchtvracht-grondstoffen zoals goud: luchthavens.)*
| id | naam | land | lat | lon | rol |
|---|---|---|---|---|---|
| | | | | | |

### 3e. Eindbestemming / consumptie
| id | naam | land | lat | lon | tier | note |
|---|---|---|---|---|---|---|
| | | | | | | |

### 3f. Extra lagen (optioneel — bijv. centrale banken, recycling)
| id | naam | type | land | lat | lon | note |
|---|---|---|---|---|---|---|
| | | | | | | |

## 4. Stromen (flows)
*Velden per stroom (→ `flows: [...]`):* `from` · `to` (node-`id`'s) · `value` (in de `unit`) ·
`mode` (`ship`/`road`/`rail`/`pipeline`/`air`) · `stage` · `via: [...]` (ids van havens/luchthavens +
knelpunten `wp-*` uit `_chokepoints.js`, in volgorde) · optioneel `note`/`label`.

> Zonder `via`-punten trekt de atlas de kortste lijn over de bol — dwars over land. Zet de echte
> route via de juiste havens/knelpunten.

| from | to | value | mode | stage | via (havens + wp-knelpunten) | note |
|---|---|---|---|---|---|---|
| | | | | | | |

## 5. Knelpunten & vaarpunten
Welke bestaande `wp-*` uit `_chokepoints.js` gebruikt deze grondstof? Nieuwe nodig (dan toevoegen +
evt. `openRadiusDeg`)? Voor lucht/institutioneel: welke "knijp" draagt het verhaal (bijv. Zwitserse
raffinage voor goud)?
-

## 6. Emergent plaatje-check (verificatie)
*(Wat moet je zien als het klopt? Dit is de lat bij oplevering.)*
-

## 7. Bronnen
*(Peiljaar + waar de cijfers vandaan komen — USGS, WGC, IEA, LBMA, bedrijfsrapportages, …)*
-

## 8. Open vragen / research-TODO
-

---

### Veld-referentie (samenvatting van het `.js`-schema)
- **node:** `{ id, type, name, country, lat, lon, share|potential, tier, operator, status, capacity, note, coastal? }`
- **flow:** `{ from, to, value, mode, stage, via: [ids], note? }`
- **tiers:** 1 = verhaal (altijd), 2 = havens/middelgroot (inzoomen), 3 = detail (dichtbij)
- **stages:** kleur + booghoogte; `erts` laag/donker → `raffinaat` midden/vol → `product` hoog/licht
- **modes:** `ship` (zee-A\*), `road`/`rail`/`pipeline` (land-A\*), `air` (great-circle — nieuw voor goud)
- Registreer de module in `data/_registry.js`.
