# Bak-handleiding (licht) — één keten bakken zonder voorkennis

*2026-09-26, voor de bak-agenten van de lichte werkwijze (M29+). Dit beschrijft het GEREEDSCHAP; het recept
per stroom blijft een functie in `v2/tools/bak_stromen.sh`. Lees vóóraf `v2/design/routebrief-licht.md`, één
lichte brief incl. §9 (`routebrieven/koper-oyutolgoi-china.md` of `koper-grasberg-manyar.md`) en de functies
`bak_koper_oyutolgoi` / `bak_koper_grasberg`. Alles draait vanuit de repo-root
(`C:/automation/Projects/General/grondstoffen-atlas`) in Git Bash met `export PYTHONIOENCODING=utf-8`.*

## 0 · Werkafspraken voor parallelle agenten (eerst lezen)

1. **Jij bakt precies één stroom-id** (`<grondstof>-<van>-<naar>`). Je raakt géén bestaande
   `stroomroute-*.json`, geen andere functie/profiel en geen uitvoer van een andere agent.
2. **Eigen bestandsnamen in `v2/build-cache/ais/graaf/`, altijd met je stroom-id als prefix:** `<stroom-id>-weg-<van>-<naar>.geojson`
   · `spoorroute-<stroom-id>-<van>-<naar>.geojson` (de `--naam=` van de spoorrouter) · `<stroom-id>-aanloop-<haven>.geojson` ·
   `<stroom-id>-rivier-….geojson`. `build-cache/` is gitignored; de scan-caches in `build-cache/land/` zijn per extract + profiel gehasht.
3. **Gedeelde bestanden alleen via één kleine edit met een stabiel anker** (bestand vlak vóór de edit
   opnieuw lezen): profiel in `v2/tools/maak_stroombeen_weg.py` **direct ná de regel `PROFIELEN = {`**
   (sleutel `"<stroom-id>-<van>-<naar>"`); functie `bak_<grondstof>_<slug>()` + kopcommentaar in
   `v2/tools/bak_stromen.sh` **direct vóór de regel `case "${1:-}" in`** (functienaam = argument met `-` → `_`);
   je bak-noot in §9 van je eigen brief `v2/design/routebrieven/<stroom-id>.md`.
4. **Centraal (orkestrator), niet door de bak-agent:** de `STROMEN`-lijst in `v2/src/main.js` én het
   data-versieliteral `laadStroomroute(VECTOR_R, "121", …)` daar, de `?v=`-bump in `v2/index.html`, een kleur in
   `GRONDSTOF_KLEUR` (`v2/src/stroomstijl.js`; koper, lithium, grafiet, kobalt, nikkel, goud, zilver, uranium,
   rare-earths, pgm, olie, gas, diamant, kolen bestaan al), nieuwe extracts (§3), de dispatch (§4), git.
   Lever in je eindrapport de registerregel: `{ sleutel: "<kort>", bestand: "stroomroute-<stroom-id>.json", aan: true }`.
5. Geen herbakes, geen `git add -A`, geen commit. Geen coördinaat verzinnen; bestaande ankers hergebruiken
   (`routebrief-licht.md` §1, Durban DCT Pier 2 en Lobito in de brieven).

## 1 · De vaste kop van `bak_stromen.sh` — waar de netten staan

| variabele | pad | inhoud |
|---|---|---|
| `GRAAF` | `v2/build-cache/ais/graaf/mississippi` | AIS-track-graaf (`mississippi.json`+`.npz`); `…/rijn` is het alternatief. Alleen relevant voor `--been "binnenvaart|…"` op die rivieren; anders laten staan (alle koperfuncties doen dat). |
| `MARNET` | `v2/build-cache/marnet-preais` | `marnet.bin` + `marnet.json` (zeenet, git-tag `pre-ais-net`). Nooit `v2/data/`. |
| `NE` | `v2/build-cache` | `ne_10m_land/minor_islands/lakes.geojson` — de landtoets. |
| `BEEN` | `v2/build-cache/ais/graaf` | alle vooraf gebakken benen (`--been-geojson` / `--stippel-geojson`). |

`hecht_marnet.py route` laadt dit in ~12 s en drukt per been km, punten en snaps af. De volgorde van
`--been/--stippel/--been-geojson/--stippel-geojson` IS de reisvolgorde; zodra er één `--marker` staat vervangt
die lijst de automatische afleiding (dus álle markers opgeven). Modaliteiten die de bol kent: `zee` ·
`binnenvaart` · `truck` · `spoor` · `leiding` (niet `weg`!).

## 2 · Per modaliteit: het exacte commando

**Zee (router, kade → kade)** — elk uiteinde snapt op de dichtstbijzijnde ZEE-knoop (`--max-snap` 25 km):
```bash
--been "zee|zeeschip <haven> → <haven>|<lat>,<lon>|<lat>,<lon>"
```
Ligt de kade verder dan ~25 km van een zeeknoop (San Antonio 74 km, Matarani 72, Mejillones 136), dan eindigt
het zeebeen op die zeeknoop met een haven-aanloop ervoor/erachter. De zeeknoop vind je zo:
```bash
python - <<'EOF'
import sys, numpy as np; sys.path.insert(0, "v2/tools"); import hecht_marnet as H
lat, lon = -33.5885, -71.6170                                   # jouw kade
z = H.marnet_zee(H.lees_marnet("v2/build-cache/marnet-preais"))  # zeeknopen, niet havenknopen
d = 6371.0088*np.arccos(np.clip(np.sin(np.radians(lat))*np.sin(np.radians(z["lat"]))+np.cos(np.radians(lat))*np.cos(np.radians(z["lat"]))*np.cos(np.radians(lon-z["lon"])),-1,1))
i = int(np.argmin(d)); print(f"zeeknoop {z['knoop_id'][i]}: {z['lat'][i]:.5f},{z['lon'][i]:.5f} op {d[i]:.1f} km")
EOF
```

**Haven-aanloop (kortste pad over water, blijft stippel)** — hangt op havens die de 1:10M-kust niet kent
(Hamburg: 20 min op 99% CPU, geen time-out in het tool). Altijd met wrapper:
```bash
timeout 300 python v2/tools/maak_havenaanloop.py --naam <stroom-id>-<haven> \
  --van <kade lat,lon> --naar <zeeknoop lat,lon> --uit "$BEEN/<stroom-id>-aanloop-<haven>.geojson"
# exit 124 of "geen pad" → terugval, rechte stippel in de functie:
--stippel "zee|haven-aanloop <haven> (schematisch — 1:10M-kust kent de haven niet)|<kade>|<zeeknoop>"
# gelukt →
--stippel-geojson "zee|haven-aanloop <haven> (schematisch, over water — MARNET reikt niet)|$BEEN/<stroom-id>-aanloop-<haven>.geojson"
```

**Spoor (1-op-1-OSM-net, via-punt → via-punt)** — ⚠️ `BAKE_SUFFIX=-raw` kiest het 1-op-1-net
(`v2/data/landnet-raw.bin`, 3.260.717 spoor-edges); zonder die var routeert het tool over het tekennet
(470.543 edges) en krijg je andere lijnen. Controleer de eerste consoleregel.
```bash
BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=LAT,LON" "--naar=LAT,LON" \
  "--naam=<stroom-id>-<van>-<naar>" [--hoofd-km=1000] [--max-snap=60] [--keerstraf=25]
# → v2/build-cache/ais/graaf/spoorroute-<naam>.geojson; console: km, snap per uiteinde, omkeringen
```
Er is geen `--via`: run kop→via en via→staart apart en zet de stukken in reisvolgorde als aparte
`--been-geojson "spoor|…|…"` (Hamburg→Emmerich = 4 runs). Een vrije Dijkstra kiest anders een omweg
(Hamburg–Bremen via Soltau 160 km; met via Rotenburg 113). `--hoofd-km` omlaag (bv. 100) voor een klein
nationaal net (Colombia 156 km, Peru 854). Dekking = de 184 extracts van §3 (`v2/build-cache/raw1op1/<extract>.geojson`);
`landnet_spoor-{af,as,cn,eu,na,oc,ru,sa}.geojson` is het tekennet per bulkregio, niet de router-bron.
Emplacementen/havensporen missen vaak (Chuqui 9 km, Pillones 3,4, Matarani 1,7) → `--stippel "spoor|…"`.

**Weg (`maak_stroombeen_weg.py`)** — één profiel per been in `PROFIELEN`; ⚠️ coördinaten daar zijn
`(lon, lat)`, eerste en laatste via-punt zijn de ankers. Licht voorbeeld (M29, ingekort):
```python
    "koper-oyutolgoi-feishang": {
        "via": [
            ("Oyu Tolgoi — concentrator",        (106.8360, 43.0480)),   # anker (lon, lat)
            ("OT-betonweg (2)",                  (107.3890, 42.7729)),   # alleen waar een corridorkeuze bestaat
            ("Gashuun Sukhait — grenspost",      (107.5692, 42.4146)),
            ("Bayannur Feishang — smelter",      (106.8530, 40.9694)),   # anker
        ],
        "id": "cu-oyutolgoi-feishang",  "naam": "Oyu Tolgoi → … → Feishang (OT-weg → G242 → G335)",
        "extracts": ["mongolia", "china"],       # Geofabrik-slugs, zie §3
        "refs": ["G242", "G335"],                # zachte voorkeur (factor 3), mag leeg
        "gepubliceerdKm": 310, "bronnoot": "OT-weg 105 km (OT LLC) + …",
        "vensterKm": 40,                         # venster om anker→via→anker; 75 bij grote uitbuigingen
        "corridorKlassen": ["tertiary"],         # optioneel: kleine klasse corridor-breed toelaten
        "uit": "<stroom-id>-weg-oyutolgoi-feishang.geojson",
    },
```
Optioneel verder: `eindKlassen` (kleine klassen binnen 12 km van de ankers; default residential/service/
tertiary/unclassified — `track` komt de scanner NIET door), `eindToegangPrivaat: True` (private/permit in de
eindzone, Codelco-klasse), `trimStaart: True` (knip overschiet op de ankerprojectie).
```bash
python v2/tools/maak_stroombeen_weg.py --profiel <sleutel> [--bron geofabrik|overpass]
# → v2/build-cache/ais/graaf/<uit>; console: "lengtetoets (weggeometrie): X km tegen gepubliceerd Y",
#   per been "snap van → naar (km)", "plant → weg … km", "keerlussen gesnoeid", "geschreven: …"
```
`geofabrik` (default) scant de lokale pbf met pyosmium (werkt hier); `overpass` is de terugval (in M29 waren
alle spiegels de hele dag onbereikbaar). Een via-punt dat > 5 km snapt is fout gelegd (wegklasse of naast de
doorgaande weg), niet "ongeveer goed". In de functie: `--been-geojson "truck|<naam>|$BEEN/<uit>"`.

**Binnenvaart** — Rijn/Mississippi: `--been "binnenvaart|…|lat,lon|lat,lon"` over de AIS-graaf (`GRAAF` op
`…/rijn` resp. `…/mississippi`; kade-anker ≤ 0,5 km van een track, anders "geen pad"). Elders over de bulklaag:
```bash
python v2/tools/maak_rivierbeen.py --marnet v2/build-cache/marnet-preais --van LAT,LON --naar LAT,LON \
  --naam "<naam>" --uit "$BEEN/<stroom-id>-rivier-<van>-<naar>.geojson"   # → --been-geojson "binnenvaart|…"
```
Gedeeld been met een bestaande stroom (Yangtze-monding → Tongling): letterlijk hetzelfde geojson/been
hergebruiken (`rivierbeen-yangtze-tongling-gedeeld.geojson`), geen tweede versie.

**Leiding / band** — OSM `man_made=pipeline` gestikt tot een LineString → `--been-geojson "leiding|…"` (voorbeeld
`leidingbeen-collahuasi-patache.geojson`); niet gekarteerd → `--stippel "leiding|<naam> (schematisch — geen OSM-way)|lat,lon|lat,lon"`.

**Vertakking / aanhechten achteraf** — aftakking halverwege een bestaand been, of fase D na de bake:
```bash
python v2/tools/voeg_been_toe.py --stroom v2/data/stroomroute-<stroom-id>.json \
  --been "truck|<naam>|$BEEN/<geojson>" [--stippel "…|lat,lon|lat,lon"] --marker "<naam>|lat,lon" \
  --vertakt-van <N> --droog    # N = 1-gebaseerd moederbeen; naad wordt gemeten, niet dichtgetrokken; --droog = rapport
```
Binnen één bake volstaat een gewone `--stippel`-regel voor een korte vertakking (PT Smelting-patroon).

**Sites (gloedlaag)** — invoer `v2/design/koper-sitelaag.json`: `{"sites": [{"id","naam","land","rol"
(mijn|smelter|raffinaderij|smelter+raffinaderij),"lat","lon","capaciteit_kt","capaciteit_bron","coord_bron",
"status","notitie"}], "china_capaciteiten": [{"naam_zoekstring","capaciteit_kt","bron"}]}`.
`python v2/tools/voeg_sites_toe.py` rapporteert, `--schrijf` merget idempotent in `v2/data/gloednodes-koper.json`.
⚠️ Paden en `grondstof: ["koper"]` zijn hard-coded: een andere grondstof vraagt eerst een parameter (centraal).

## 3 · Geofabrik-extracts

184 extracts (70 GB) in `v2/build-cache/geofabrik/<slug>-latest.osm.pbf`; `ls` daar is de lijst. Slugs zijn
Nederlands (`chili`, `peru`, `zuid-afrika`, `congo-drc`, `mongolia`, `indonesie`, `australie`), DE/FR/RU/VS per
deelstaat (`de-nrw`, `fr-alsace`, `rusland-oeral`, `us-arizona`). Ontbrekend: o.a. taiwan, kenia, ethiopie,
tunesie, libie, jordanie, israel, kirgizie, tadzjikistan, Midden-Amerika, jamaica, dominicaanse-republiek, brunei,
oost-timor, us-colorado, us-hawaii, de NE-staten van de VS. Een ontbrekende extract is **centraal werk**: slug in `LAND_EXTRA_REGIOS` (+ `EXTRA_REGIO`,
bulkregio af/as/eu/na/oc/sa) in `v2/tools/fetch_landnet.py`, dan `python v2/tools/fetch_landnet.py --download`
(patroon `https://download.geofabrik.de/<continent>/<land>-latest.osm.pbf`; controleer de grootte — 0 byte is een
redirect). Een los gecurld bestand zonder registerregel stopt in `land_laad` op "staat niet in GEOFABRIK_REGIOS".

**Looptijd en geheugen (M29, `workers=1` per profiel):** ~1–2 min scan per GB pbf (Congo-DRC 414 MB ≈ 20 s,
Chili ≈ 25 s, Zuid-Afrika ≈ 2 min, China 1,56 GB ≈ 3 min) plus seconden tot minuten Dijkstra; de scan-cache in
`build-cache/land/` is 1–370 MB JSON per extract (groeit met het venster) en kost bij laden ruwweg 5–10× dat in
RAM (Zuid-Afrika op 75 km ≈ 2–4 GB). Machine: 16 cores, 31 GB. **Advies: maximaal 4 wegscans tegelijk, hooguit
2 op een reus** (china, india, indonesie, japan, brazilie, canada, italie, groot-brittannie, australie, de-bayern,
us-california/-texas). `hecht_marnet route` (12 s) en de spoorrouter (seconden) mogen onbeperkt naast elkaar.

## 4 · De functie in `bak_stromen.sh` en de dispatch

Kop: 3–8 regels commentaar (`# ── <grondstof> · <van> → <naar>`, routebrief, de ⚠️-keuzes: welke stippels en
waarom, welke ankers onzeker). Dan één `python v2/tools/hecht_marnet.py route --graaf "$GRAAF" --marnet "$MARNET"
--ne "$NE" …` met de benen in reisvolgorde, alle markers, `--routebrief v2/design/routebrieven/<stroom-id>.md
--uit v2/data/stroomroute-<stroom-id>.json --stroom <stroom-id> --titel "…"`. Draaien: `bash v2/tools/bak_stromen.sh <stroom-id>`.

De `case … esac` onderaan is een handmatige lijst (usage-regel noemt nog vier stromen). Elke regel is al
`<naam>) bak_<naam met _>`, dus de dispatch kan generiek zonder gedragswijziging (**centraal doorvoeren**):
```bash
naam="bak_${1//-/_}"
if [ -n "${1:-}" ] && declare -F "$naam" >/dev/null; then "$naam"
else echo "gebruik: bash v2/tools/bak_stromen.sh <stroom>; bekend:" >&2
     declare -F | sed -n 's/^declare -f bak_//p' | tr '_' '-' >&2; exit 2; fi
```

## 5 · De toets ná het bakken

1. **Km per been en naden** — de bake-console geeft ze al; uit het json:
```bash
python - <<'EOF'
import json, math
d = json.load(open("v2/data/stroomroute-<stroom-id>.json", encoding="utf-8")); B = d["benen"]
gc = lambda a, b: 6371.0088*math.acos(min(1, math.sin(math.radians(a[1]))*math.sin(math.radians(b[1]))+math.cos(math.radians(a[1]))*math.cos(math.radians(b[1]))*math.cos(math.radians(a[0]-b[0]))))
for i, b in enumerate(B):
    v = b.get("vertakt_van"); p0 = b["punten"][0]
    naad = 0 if i == 0 else (min(gc(p, p0) for p in B[v-1]["punten"]) if v else gc(B[i-1]["punten"][-1], p0))
    print(f"{i+1:2} {b['modaliteit']:<12}{b['km']:>9.1f} km  naad {naad:6.2f} km  {'stippel' if b.get('stippel') else '':8} {b['naam'][:70]}")
print("totaal", round(sum(b["km"] for b in B), 1), "km ·", len(d["markers"]), "markers")
EOF
```
   Norm (`routebrief-licht.md` §1): elk gemeten been binnen **±15%** van de km in je benen-tabel (het wegtool
   waarschuwt al bij ±10%); **geen naad > 5 km** tussen opeenvolgende benen (honderden meters = procesgat, blijft
   staan en komt in §9); markers ≤ ~0,5 km van hun lijn tenzij anker ≠ routeerpunt. Buiten de norm = bevinding
   in §9, geen via-punt bijschuiven om het getal te halen.
2. **Rijdbaarheid en rechte lijnen:** `python v2/tools/toets_knikken.py --bestand v2/data/stroomroute-<stroom-id>.json`
   (op weg/water is een lus soms echt) en `python v2/tools/toets_rechte_benen.py --min-km 5` (elk been met
   omwegfactor 1,000 hoort een stippel met reden te zijn).
3. **Laadt het json?** Er is géén node-toets voor stroomroutes (`toets_stromen_14.mjs` is geparkeerd op `marnet.bin`,
   `laad_headless.mjs` heeft geen stroomroute-lezer). Wat wél telt: `json.load` slaagt, `versie == 2`, `punt_formaat ==
   "lonlat"`, elke `modaliteit` in {zee, binnenvaart, truck, spoor, leiding}, elk been ≥ 2 punten, bestand < ~300 KB.
   De blik op de bol (0 console-fouten, atlasmodus per grondstof + donker) gebeurt centraal ná register en `?v=`-bump.

## 6 · Valkuilen-checklist (M29, brieven §9 + sessiesamenvatting)

- [ ] `PYTHONIOENCODING=utf-8`; coördinaten `lat,lon` met punt — behalve in `PROFIELEN` (`(lon, lat)`).
- [ ] Modaliteit heet `truck`, nooit `weg` (onbekende sleutel wordt wit op de bol).
- [ ] Spoor met `BAKE_SUFFIX=-raw`; console zegt `3260717 spoor-edges`. Corridorkeuze = meerdere runs met via-punt.
- [ ] Zee snapt op een ZEE-knoop, niet op de dichtstbijzijnde havenknoop (San Antonio: haven 3 km, zee 74 km).
- [ ] `maak_havenaanloop.py` altijd onder `timeout 300`; hangt → rechte stippel, geen tweede poging.
- [ ] Corridor in OSM `tertiary`/`unclassified`/`permit`? → `corridorKlassen` / `eindToegangPrivaat` (OT week 129 km
      westwaarts; Carretera del Cobre "geen wegpad"). `track` en `proposed` komen er nooit door → knippen + stippel.
- [ ] Via-punten óp de doorgaande weg, niet in een centrum of op een zijtak (Rancagua "geen wegpad"; zijtak = 180°-keerpunt);
      snap > 5 km op een via-punt = eerst de wegklasse nakijken, dan pas de km-toets geloven.
- [ ] Emplacementen, havensporen, steigers en bekkens zonder AIS-oversteek (Emmerich) zitten niet in de netten → korte stippel mét reden.
- [ ] Gedeeld been = letterlijke kopie; aftakking = `vertakt_van`. Stippel betekent alleen "hier reikt het net niet";
      "aannemelijk" en "onzeker" staan in de beennaam/markernaam en in §3/§7 van de brief, niet in de lijnstijl.
- [ ] Extract ontbreekt of Overpass valt weg → melden; niet zelf het register aanpassen, `--bron geofabrik` is de default.
- [ ] Eindrapport: benen + km + naden, de registerregel voor `main.js`, welke shared-file-edits (profiel, functie), open punten.
