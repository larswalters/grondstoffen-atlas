---
type: werkorder
datum: 2026-08-04
stroom: grafiet-balama-vs
status: in uitvoering
---

# Werkorder — de grafietketen van mijn tot eindproduct

*Uitkomst van de ankerronde van 2026-08-04 (9 agents): vijf ankers gelegd, twee truckcorridors
afgeleid uit vrachtnetdata, en het bestaande deel doorgemeten. Besluit Lars dezelfde dag: fase D/E
worden getekend hoewel het volume vandaag nul is.*

# WERKORDER — grafietketen Balama → Casa Grande op de bol

**Project:** `C:\automation\Projects\General\grondstoffen-atlas` · **stroom-id:** `grafiet-balama-vs` · **brief:** `v2\design\routebrieven\grafiet-balama-vidalia.md` · **datum:** 2026-08-04

**Uitgangspunt:** de fasen D en E worden getekend hoewel het volume vandaag nul is (besluit projecteigenaar). Dat besluit hoort in de **node-note en de brief**, niet in de lijnstijl: D/E liggen op echt wegnet, dus **doorgetrokken**, niet gestippeld. Stippel betekent in dit project precies één ding — hier reikt het net niet (werkwijze §7) — en dat vervagen zou de enige eerlijke conventie kapotmaken die de kaart heeft.

⚠️ **Vóór je begint:** de working tree heeft `data/lithium.js` gewijzigd en twee untracked design-bestanden. Commit/stash die eerst; stage bij elke commit hieronder **alleen je eigen bestanden** (sectie J van de project-`CLAUDE.md`).

---

## A · Ankerlijst

lat,lon in decimale graden, 5 decimalen, WGS-84. "aansl." = `v2/data/aansluitingen.json`, en die wordt **gegenereerd** — je bewerkt `v2/tools/maak_aansluitingen.py` (de redactionele lijst is de bron van waarheid).

| id | omschrijving | lat, lon | status | landt in |
|---|---|---|---|---|
| `gr-balama-laadplek` | Balama-plant, bagging + truckbelading (Twigg/Syrah) | **-13.31000, 38.66000** | satelliet-gelegd (ankercheck 2026-07-28) | aansl. (nieuw) + `data/graphite.js` `gr-mozambique` (staat er al) |
| `gr-nacala-kade` | Porto de Nacala, containerterminal oostoever | **-14.53830, 40.66730** | satelliet-gelegd (z16, 2026-07-28) | aansl. (nieuw) + `graphite.js` `gr-port-nacala` (staat er al) |
| — | Grindrod Cross Dock Facility (aankomstanker O1) | — | **niet gevonden** | niets — blijft §5.1 |
| — | Durban DCT, beide ligplaatsen (O2) | — | **niet gevonden** | niets — blijft §5.2 |
| `gr-nola-napoleon` | Napoleon Avenue Container Terminal, containerkade | **29.91230, -90.11200** | satelliet-gelegd (z16, 2026-07-28) | aansl. (nieuw) + `graphite.js` `gr-port-neworleans` (staat er al) |
| `gr-portallen-kade` | IRMT — 200-ft bargekade, noordoever **Slack Water Canal** (aankomst b3 **én** vertrek b4: één ligplaats) | **30.43313, -91.24383** | **satelliet-gelegd** (z19, 2026-08-04; kadefront 59 m ≈ gepubliceerde 200 ft; AIS 51 pings <50 m) | aansl. (nieuw) |
| ↳ routeerpunt | vaargeulpunt in het zijkanaal, 22 m voor de kade | **30.43293, -91.24385** | echt AIS-trackpunt | bakprofiel + brief |
| `gr-portallen-lock` | Port Allen Lock, kolkmidden (OSM way 1465620640) | **30.43085, -91.20823** | satelliet-gelegd (z18) + OSM + 876 AIS-pings <50 m | brief (passage) + marker in `stroomroute-pilot.json` |
| `gr-vidalia-kade` | Port of Vidalia — verharde apron/keerplaats achter de cargo ramp | **31.53645, -91.48255** | **satelliet-gelegd** (Wayback 22252, wolkenvrij) — ±20 m beeldaflezing | aansl. (nieuw) |
| ↳ routeerpunt | kop van de ramp/transportband in de rivier | **31.53530, -91.48090** | satelliet-gelegd | bakprofiel + brief |
| `gr-vidalia-fabriek` | Syrah AAM-fabriek Vidalia, terreinanker | **31.54660, -91.48870** | satelliet-gelegd + EA-2181 Fig. 1 "Project Center" 31.54653, -91.48868 (8 m) | aansl. (nieuw) + `graphite.js` `gr-ref-vidalia` (staat er al) |
| ↳ routeerpunt | fabriekspoort / front gate aan D.A. Biglane Road | **31.54796, -91.48743** | satelliet-gelegd + EA-2181 Fig. 1 + OSM-knoop (6 m) | bakprofiel + brief (géén aansluiting: het is een poort, geen laadplek) |
| — | uitgaand **AAM-laaddock** Vidalia | — | **niet gevonden** (z19 = fijnste Esri; geen perron zichtbaar) | niets — §5.9 blijft open |
| `gr-ferriday-us84` | Ferriday, E. Wallace Blvd × Louisiana Ave (US-84 × US-425/LA-15/LA-568), OSM-knoop 115186261 | **31.62988, -91.55496** | satelliet-gelegd (z17+z18) | brief + bakprofiel (via-punt) |
| `gr-fab-desoto` | Panasonic Energy Kansas, De Soto — **TERREIN/GEBOUW**-anker (OSM way 1201758396) | **38.93815, -95.00240** | satelliet-gelegd **als terreinanker**; docks **niet gelegd** (opname = bouwfase) | `graphite.js` (nieuwe node) — **NIET** in aansl. (aansluiting op een ongelegd dock = Waalhaven-klasse) |
| ↳ routeerpunt | rotonde Energy Way × Astra Parkway | **38.94196, -95.00748** | OSM + z17 | bakprofiel + brief |
| — | inkomend dock (b7) en uitgaand dock (b8) De Soto | — | **niet gevonden** | niets — §5.12 blijft open |
| `gr-lucid-amp1` | Lucid AMP-1, **inkomende dockrij westgevel** (midden van ~330 m gevel) | **32.85724, -111.78008** | **satelliet-gelegd** (z19; rij opleggers kont-aan-gevel + truck-apron) | `graphite.js` (nieuwe node) + aansl. (nieuw) |
| ↳ routeerpunt | westelijke fabriekspoort aan West Selma Highway | **32.85035, -111.78238** | satelliet-gelegd (z19) | bakprofiel + brief |
| *negatief* | `gr-mkt-us` battery-belt-centroïde | 36.50000, -86.60000 | **markt-centroïde, géén anker** — verbodsstraal 150 km | blijft in `graphite.js` als markt; de Vidalia-flow mag er niet meer heen |

Vervallen coördinaten die je actief moet vervangen: **30.432, -91.222** (IRMT, 2,10 km fout) · **30.4415, -91.2075** (sluis, 1,19 km fout, ligt op de I-10-knoop) · **31.538, -91.485** (Vidalia-haven, staat in batture-bos).

---

## B · Reparaties aan het bestaande deel

### B1 — het binnenvaartbeen knippen (en de geometrie echt naar de kade brengen)

**Nu:** één been `binnenvaart` "containerbarge → Port of Vidalia", 404,2 km / 2.256 punten, van `-90.11204, 29.91179` naar `-91.48251, 31.53262`. Geen overslag, geen Port Allen in de geometrie; de marker hangt 2,08 km naast de lijn.

**Wordt:** twee benen. **Niet** chirurgisch knippen op index 1166 — dat punt ligt op de mainstem en de barge zou nog steeds nooit het zijkanaal in gaan. Herbakken met het IRMT-routeerpunt als tussenpunt:

- b3 `binnenvaart` — *containerbarge New Orleans → Port Allen (IRMT)* : `29.91230,-90.11200` → `30.43293,-91.24385`
- b4 `binnenvaart` — *containerbarge Port Allen → Port of Vidalia* : `30.43293,-91.24385` → `31.53645,-91.48255`

**Dit kan, en dat is gemeten** (2026-08-04, `v2/build-cache/ais/graaf/mississippi.npz`): de dichtstbijzijnde graafknoop bij de IRMT-kade ligt op **69 m** (knoop 152086, `30.43252,-91.24368`), de sluis op **52 m** (knoop 152068), en NOLA, sluis, IRMT en Vidalia zitten **alle vier in dezelfde component** (id 18, 153.931 knopen). Het openstaande punt uit het ankeronderzoek ("loopt het zijkanaal door in de graaf?") is hiermee **dicht: ja**. Een ruwe Dijkstra NOLA→IRMT loopt **door de sluis** en komt uit op 176 km; `hecht_marnet` routeert over haltes met overstapboete en komt hoger uit — meet dat na de bake, neem dit getal niet over.

**Controle na de bake:**
```bash
python - <<'PY'
import json,math
d=json.load(open('v2/data/stroomroute-pilot.json',encoding='utf-8'))
def km(a,b):
    R=6371.0088;la1,lo1=math.radians(a[1]),math.radians(a[0]);la2,lo2=math.radians(b[1]),math.radians(b[0])
    h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
for i,b in enumerate(d['benen']):
    print(i,b['modaliteit'],round(b['km'],1),len(b['punten']),b['punten'][0],b['punten'][-1])
for i in range(len(d['benen'])-1):
    g=km(d['benen'][i]['punten'][-1],d['benen'][i+1]['punten'][0])
    print(f'gat {i}->{i+1}: {g*1000:.0f} m')
b=[x for x in d['benen'] if 'Port Allen' in x['naam']][0]
print('laatste 6 punten b3:',b['punten'][-6:])
PY
```
Eisen: (1) b3 eindigt ≤0,10 km van `30.43293,-91.24385`; (2) de **laatste ~4 km van b3 liggen in het zijkanaal** — d.w.z. de laatste punten hebben lon < −91,235 bij lat ≈ 30,433, en er zit een knik bij de aftakking rond `30.4363,-91.2500`; (3) b3 passeert de sluis binnen 0,15 km van `30.43085,-91.20823`; (4) b3 ≈ 200–215 km, b4 ≈ 200–215 km (brief: 207 + 210); (5) gat b3→b4 = 0 m.

### B2 — Port Allen als twee ankers

De IRMT heeft **één** bargeligplaats; aankomst (b3) en vertrek (b4) vallen daarom fysiek samen op `30.43313, -91.24383`. Dat is géén compromis-coördinaat maar een gemeten feit, en dat moet er expliciet bij staan (werkwijze §2b). **Voorwaarde:** het geldt alleen in de barge-variant; blijft de modus NOLA→Port Allen truck (§5.5), dan is het aankomstanker de landpoort — en die is **niet gelegd**.

Markers in het gebakken bestand: vervang `Port Allen (IRMT) — barge-belading | -91.222, 30.432` door **`Port Allen (IRMT) — bargekade | 30.43313, -91.24383`** en voeg **`Port Allen Lock (sluis) | 30.43085, -91.20823`** toe. Controle: afstand marker → dichtstbijzijnde punt op b3 ≤ 0,10 km (was 2,08 km).

### B3 — de sluis als punt

Brief been 3 punt 8 en been 4 punt 2 dragen `30.4415, -91.2075`. Vervangen door **`30.43085, -91.20823`**. Controle: OSM way 1465620640 centroïde = dit punt; deur-tot-deur `30.43175,-91.20992` ↔ `30.42994,-91.20654` = 382 m ≈ de gepubliceerde kolk van 1.200 ft; de gebakken b3 komt er binnen 0,15 km langs. De sluis is een **passage**, geen aansluiting — geen entry in `aansluitingen.json`.

### B4 — b5 (last mile) hermeten

**Nu:** `--stippel truck`, 2 punten, 1,02 km, van `-91.485, 31.538` (bos) naar `-91.4887, 31.5466`.

**Wordt:** doorgetrokken been op echte weggeometrie, apron → grindtoegangsweg → LA-131 → D.A. Biglane Road → fabrieksinrit, **2,3–2,7 km**. Het net reikt hier wél, dus de stippel vervalt — dat is een statuswijziging die je in §7 van de brief moet verantwoorden.

⚠️ **Blokkade die je eerst moet opheffen:** het beslissende eerste stuk (1.197 m havengrindweg) is in OSM `highway=track`, en `EIND_KLASSEN` in `maak_stroombeen_weg.py` (regel 167) kent die klasse niet. Fix **per profiel**, niet globaal:

```python
EIND_KLASSEN = ("residential", "service", "tertiary", "unclassified")   # ongewijzigd = default
```
→ in `_kies_profiel()` een override lezen: `CORRIDOR["eindKlassen"] = p.get("eindKlassen", EIND_KLASSEN)` en overal waar nu de module-constante wordt gebruikt (regels ~282, ~330–338, ~450) die profielwaarde nemen. Reden voor per-profiel: het corridor-id dat de scan ziet hasht de eindklassen mee (regel 268), dus de default-tuple ongewijzigd laten garandeert dat de twee bestaande profielen **byte-identiek** blijven. Dat is meteen je regressietoets (zie E, stap 1).

**Controle:** lengte 2,2–2,8 km · ≥100 punten · `kmAanloopVan` ≤ 0,10 km (apron) · `kmAanloopNaar` ≤ 0,20 km (fabriek) · `snoei_keerlussen` rapporteert geen 180°-keerpunt. De EA-waarde "~4 km" is **niet reproduceerbaar** en wordt in de brief een bevinding, geen doel.

### B5 — het gat van 643 m

Verdwijnt niet, en dat is correct. b4 eindigt op een **graafknoop in de rivier** (de dichtstbijzijnde bij de apron ligt op 444 m), b5 begint op de **kade**. Dat is precies `anker ≠ routeerpunt` (§2b), zoals Napoleon Ave 154 m. Acceptatie: **gat ≤ 0,5 km**, marker staat op het anker, en de afstand staat als "max snap" in het b4-blok van de brief. Wat wél moet verdwijnen is het gat dat uit een fout anker kwam: het oude `31.538,-91.485` bestond niet als haveninfrastructuur.

### B6 — `aansluitingen.json` (via de generator)

Voeg in `v2/tools/maak_aansluitingen.py` een blok toe. `plek` is **[lon, lat]**. Draai eerst **zonder** `--schrijf` en diff tegen het bestaande bestand: de 18 bestaande aansluitingen moeten op 0,0 m gelijk blijven (de `cu-guixi-spoor`-drift van 741 m).

```python
# ======================================================================
# STROOM E — grafiet Balama → Vidalia → De Soto → Casa Grande
# ======================================================================
dict(id="gr-balama-laadplek", grondstof="graphite", fase="erts", rol="laadplek",
     naam="Balama — bagging + truckbelading op de plant",
     plek=[38.66000, -13.31000], modi=["weg"],
     bron="SATELLIET-GELEGD Esri z16 2026-07-28 (ankercheck) + OSM industrieterrein/pits (ODbL)"),
dict(id="gr-nacala-kade", grondstof="graphite", fase="erts", rol="overslag",
     naam="Porto de Nacala — containerterminal oostoever",
     plek=[40.66730, -14.53830], modi=["zee", "weg"],
     bron="SATELLIET-GELEGD Esri z16 2026-07-28",
     noot="⚠️ het onderzoekspunt -14.531/40.652 lag in het water bij de kolen-jetty op de WESToever"),
dict(id="gr-nola-napoleon", grondstof="graphite", fase="erts", rol="overslag",
     naam="Port of New Orleans — Napoleon Avenue Container Terminal",
     plek=[-90.11200, 29.91230], modi=["zee", "binnen"],
     bron="SATELLIET-GELEGD Esri z16 2026-07-28 (489 m verplaatst)"),
dict(id="gr-portallen-kade", grondstof="graphite", fase="erts", rol="overslag",
     naam="Port Allen — IRMT 200-ft bargekade (Slack Water Canal)",
     plek=[-91.24383, 30.43313], modi=["binnen"],
     bron="SATELLIET-GELEGD Esri z19 2026-08-04 + portgbr IRMT-Map.pdf + MarineCadastre "
          "(51 pings <50 m); OSM way 1465620640 = Port Allen Lock ter oriëntatie",
     noot="⚠️ DE IRMT LIGT NIET AAN DE DOORGAANDE GIWW maar aan een doodlopend zijkanaal "
          "('Slack Water Canal') dat op ~30.4363/-91.2500 zuidwaarts aftakt. Elke zoekpoging "
          "langs de GIWW moest mislukken — dat verklaart de mislukte ankercheck van 2026-07-28. "
          "Aankomst b3 en vertrek b4 vallen hier fysiek samen: er is precies één bargeligplaats. "
          "Routeerpunt (vaargeul) 30.43293/-91.24385, 22 m; max snap 0,05 km."),
dict(id="gr-vidalia-kade", grondstof="graphite", fase="erts", rol="overslag",
     naam="Port of Vidalia — apron achter de cargo ramp (mijl 359)",
     plek=[-91.48255, 31.53645], modi=["binnen", "weg"],
     bron="SATELLIET-GELEGD Esri Wayback 22252 (2026-01-29) 2026-08-04",
     noot="⚠️ het oude briefpunt 31.538/-91.485 ligt in batture-bos: geen kade, geen ramp, "
          "geen verharding. De ramp-/transportbandkop ligt op 31.53530/-91.48090 = het "
          "routeerpunt; max snap 0,45 km (graafknoop 444 m). Slip in aanbouw: 31.53788/-91.48535."),
dict(id="gr-vidalia-fabriek", grondstof="graphite", fase="raffinaat", rol="losplek",
     naam="Syrah Technologies — AAM-fabriek Vidalia",
     plek=[-91.48870, 31.54660], modi=["weg"],
     bron="SATELLIET-GELEGD 2026-07-28 (ankercheck) + DOE/EA-2181 Fig. 1 'Project Center' "
          "31.54653/-91.48868 (8 m, onafhankelijke tweede bron)",
     noot="Routeerpunt = de fabriekspoort 31.54796/-91.48743 (EA-2181 'Front Gate' + OSM-knoop "
          "31.54800/-91.48739, 6 m). ⚠️ Het terrein grenst aan D.A. BIGLANE ROAD, niet aan "
          "LA-131. Het uitgaande AAM-laaddock is NIET gelegd — z19 toont geen perron."),
dict(id="gr-amp1-dock", grondstof="graphite", fase="product", rol="losplek",
     naam="Lucid AMP-1 Casa Grande — inkomende dockrij westgevel",
     plek=[-111.78008, 32.85724], modi=["weg"],
     bron="SATELLIET-GELEGD Esri z19 2026-08-04 (rij opleggers kont-aan-gevel over ~330 m + "
          "truck-apron OSM way 1254718550) — Wayback 32246 identiek aan live",
     noot="Anker = MIDDEN van een dockrij van ~330 m, geen aangewezen deur. Routeerpunt = "
          "westpoort West Selma Highway 32.85035/-111.78238 (797 m). UITGESLOTEN: de "
          "autoparking zuid (~32.85160/-111.77980) is de uitgaande kant; oostgevel is "
          "personeelsparking; noordblok nog in aanbouw. Geen spoor op het terrein."),
```
**Bewust géén entry** voor De Soto (dock niet gelegd), Grindrod Cross Dock, Durban.

### B7 — `data/graphite.js`

1. **Twee nodes erbij** (achter `gr-ref-vidalia`), met de reden in de `note` — anders wordt het anker later stil "gecorrigeerd" (de Greenbushes-les):
```js
{ id: "gr-fab-desoto", type: "refinery", name: "Panasonic Energy Kansas — De Soto", country: "VS (Kansas)",
  lat: 38.93815, lon: -95.00240, tier: 2, operator: "Panasonic Energy",
  capacity: "≈ 32 GWh/j (2170-cellen)",
  note: "Celfabriek in Astra Enterprise Park (ex-Sunflower AAP); massaproductie sinds 14-07-2025. ⚠️ DIT IS EEN TERREIN-/GEBOUWANKER (OSM way 1201758396, satelliet-gelegd op het dak), GEEN DOCK: op de nieuwste Esri-opname (= Wayback 32246, bouwfase) is geen dockdeur of marshalling-yard aanwijsbaar. Niet promoveren tot laad-/losplek zonder een opname van ná 14-07-2025. Routeerpunt = rotonde Energy Way × Astra Parkway 38.94196/-95.00748. Adresconflict: OSM 10301 vs KDHE 10701 Astra Parkway. ⚠️ VOLUME VANDAAG NUL — Syrah leverde t/m Q2 2026 alleen ~150 t kwalificatiemonsters." },
{ id: "gr-lucid-amp1", type: "market", name: "Lucid AMP-1 — Casa Grande", country: "VS (Arizona)",
  lat: 32.85724, lon: -111.78008, tier: 2, operator: "Lucid Motors",
  note: "Voertuig-/packfabriek, keten-eind. ⚠️ HET ANKER IS DE INKOMENDE DOCKRIJ AAN DE WESTGEVEL (satelliet-gelegd z19), NIET de gebouwcentroïde — die ligt 159 m oostelijker. De uitgaande autoparking (~32.85160/-111.77980) is bewust GEEN anker. ⚠️ VOLUME VANDAAG NUL: de weg is echt, de lading nog niet." },
```
2. **De uitgaande flow herrichten.** `gr-ref-vidalia → gr-mkt-us` (mode road, value 11) wijst nu naar de coördinaat die de brief zelf als negatief anker met 150 km verbodsstraal voert. Vervangen door:
   - `gr-ref-vidalia → gr-fab-desoto`, mode `road`, waarde ≈ **2,3** (Lucid ~7 kt / 3 jaar), note met de nul-volume-notitie en de Tesla-streng als beargumenteerd stoppunt;
   - `gr-fab-desoto → gr-lucid-amp1`, mode `road`, cellen, zelfde nul-volume-notitie.
   `gr-mkt-us` blijft bestaan als markt voor de flows uit Novonix/Québec — die zijn niet van deze streng.
3. `gr-ref-vidalia.note`: "laatste ~4 km per truck" → **~2,3 km over grindweg → LA-131 → D.A. Biglane Road**; en de emballage is **supersacks** (EA-2181 §2.2), niet "niet gedocumenteerd".

### B8 — cache-busting

`stroomroute-pilot.json` is een browser-asset. In `v2/index.html` regel 7 + 250: `?v=105` → `?v=106`. In `v2/src/main.js` (~regel 257): `laadStroomroute(VECTOR_R, "103", …)` → `"104"`. Dat herlaadt alle vijf stroombestanden (< 300 KB elk) — acceptabel, en het is de enige plek waar de data-versie leeft.

---

## C · Nieuwe benen — de bak-recepten

⚠️ **Dit is meteen de invulling van het openstaande projectpunt "de bak-commando's staan nergens".** Leg het complete commando vast in **`v2/tools/bak_stromen.sh`** (uitvoerbaar, één functie per stroom) en verwijs er in §7 van de routebrief naar. Een recept in een shell-historie is een generator die uit de pas gaat lopen — de `cu-guixi-spoor`-klasse.

Alle vier de nieuwe benen zijn wegbenen en gaan door `maak_stroombeen_weg.py`. **Zet ze in de `PROFIELEN`-dict van dat bestand** (regel 96) — nadrukkelijk niet in een kopie. Coördinaten daar zijn **(lon, lat)**.

### Extracts — alles staat al op schijf, niets downloaden

Gecontroleerd in `v2/build-cache/geofabrik/`: `us-louisiana` · `us-arkansas` · `us-missouri` · `us-kansas` · `us-oklahoma` · `us-texas` · `us-new-mexico` · `us-arizona` · `mozambique`. `us-colorado` ontbreekt en is **niet nodig** (alleen een I-70-variant zou hem vragen).

### C1 · profiel `grafiet-vidalia-lastmile` (b5, inkomende last mile)

```python
"grafiet-vidalia-lastmile": {
    "via": [
        ("Port of Vidalia — apron/cargo ramp", (-91.48255, 31.53645)),
        ("Syrah AAM-fabriek",                  (-91.48870, 31.54660)),
    ],
    "id": "gr-vidalia-lastmile",
    "naam": "Port of Vidalia → Syrah AAM-fabriek (haventoegangsweg → LA-131 → D.A. Biglane Rd)",
    "extracts": ["us-louisiana"],
    "refs": ["131"],
    "eindKlassen": ("track", "residential", "service", "tertiary", "unclassified"),
    "gepubliceerdKm": 2.34,
    "bronnoot": "eigen Dijkstra over us-louisiana (2026-08-04); de EA-waarde ~4 km is niet reproduceerbaar",
    "vensterKm": 8,
    "uit": "stroombeen-vidalia-lastmile.geojson",
},
```
```bash
python v2/tools/maak_stroombeen_weg.py --profiel grafiet-vidalia-lastmile
```

### C2 · profiel `grafiet-vidalia-us84` (b6, uitgaande last mile)

Kop = de **fabriekspoort**, niet het laaddock: dat dock is niet gevonden en wordt niet verzonnen.

```python
"grafiet-vidalia-us84": {
    "via": [
        ("Syrah fabriekspoort (front gate)", (-91.48743, 31.54796)),
        ("D.A. Biglane Rd × LA-131",         (-91.48503, 31.54530)),
        ("LA-131 × US-84, Vidalia",          (-91.42737, 31.56647)),
    ],
    "id": "gr-vidalia-us84",
    "naam": "Syrah-poort → D.A. Biglane Rd → LA-131 → US-84 (Vidalia)",
    "extracts": ["us-louisiana"],
    "refs": ["131", "84", "425"],
    "gepubliceerdKm": 6.98,
    "bronnoot": "gemeten over de OSM-geometrie 2026-08-04; de brief-waarde '~3 km' klopt op geen enkele route",
    "vensterKm": 10,
    "uit": "stroombeen-vidalia-us84.geojson",
},
```
```bash
python v2/tools/maak_stroombeen_weg.py --profiel grafiet-vidalia-us84
```
⚠️ Alternatief dat je **niet** kiest zonder bron: Airport Road × US-84 op `31.58728, -91.49884` is 5,46 km en dus korter, maar over `tertiary`. Welke een 15-meter-trekker rijdt is onbekend → openstaand punt, geen stille keuze.

### C3 · profiel `grafiet-vidalia-desoto` (b7)

```python
"grafiet-vidalia-desoto": {
    "via": [
        ("LA-131 × US-84 Vidalia",      (-91.42737, 31.56647)),
        ("Ferriday US-84 × US-425",     (-91.55496, 31.62988)),
        ("Clayton US-425 × US-65",      (-91.53933, 31.71575)),
        ("Winnsboro LA",                (-91.72011, 32.16365)),
        ("US-425 × I-20 (Rayville)",    (-91.75873, 32.45759)),
        ("Bastrop LA",                  (-91.91330, 32.77830)),
        ("grens LA/AR op US-425",       (-91.85428, 33.01773)),
        ("Hamburg AR US-425 × US-82",   (-91.79763, 33.22426)),
        ("Monticello AR",               (-91.80229, 33.62908)),
        ("Pine Bluff AR — US-425→I-530",(-91.97206, 34.19938)),
        ("Little Rock I-530 × I-30",    (-92.26239, 34.75377)),
        ("N. Little Rock I-30 → I-40",  (-92.25570, 34.77778)),
        ("Conway AR I-40 × US-65",      (-92.43278, 35.10847)),
        ("Russellville AR",             (-93.13381, 35.30431)),
        ("Alma AR I-40 × I-49",         (-94.22110, 35.48987)),
        ("Fayetteville AR",             (-94.20248, 36.07410)),
        ("I-49 Bella Vista Bypass",     (-94.31479, 36.42399)),
        ("grens AR/MO op I-49",         (-94.38238, 36.49919)),
        ("Joplin MO I-49 × I-44",       (-94.42085, 37.06340)),
        ("Nevada MO",                   (-94.32405, 37.83875)),
        ("Harrisonville MO I-49 × MO-7",(-94.35536, 38.63849)),
        ("Kansas City I-49 → I-435",    (-94.52622, 38.87285)),
        ("grens MO/KS op I-435",        (-94.60790, 38.93691)),
        ("Lenexa KS I-435 × K-10",      (-94.77430, 38.95192)),
        ("De Soto K-10 × Lexington Ave",(-94.96651, 38.96023)),
        ("Astra Parkway — rotonde",     (-95.00748, 38.94196)),
        ("Panasonic De Soto — terrein", (-95.00240, 38.93815)),
    ],
    "id": "gr-vidalia-desoto",
    "naam": "Syrah Vidalia → Panasonic De Soto (US-84/US-425 → I-530 → I-40 → I-49 → I-435 → K-10)",
    "extracts": ["us-louisiana", "us-arkansas", "us-missouri", "us-kansas"],
    # ⚠️ "71" bewust NIET: die trok de eerste run 26 km over het oude US-71-tracé
    #    door Bella Vista i.p.v. de I-49-bypass (geopend 01-10-2021).
    "refs": ["84", "425", "15", "530", "30", "40", "49", "435", "10"],
    "gepubliceerdKm": 1160,
    "bronnoot": "eigen corridormeting over de vier extracts 2026-08-04 (1.150,8 km net + last miles); "
                "geen bron documenteert deze rit",
    "vensterKm": 40,
    "uit": "stroombeen-vidalia-desoto.geojson",
},
```
```bash
python v2/tools/maak_stroombeen_weg.py --profiel grafiet-vidalia-desoto
```
**Verklikker direct na deze run:** raakt de lijn `36.48, -94.27` binnen 4 km (oude US-71 door Bella Vista), dan is de ref-voorkeur alsnog de fout in getrapt → via-punt op de bypass verzwaren. En de lijn mag Oklahoma niet raken.

### C4 · profiel `grafiet-desoto-casagrande` (b8)

```python
"grafiet-desoto-casagrande": {
    "via": [
        ("Panasonic De Soto — terrein", (-95.00240, 38.93815)),
        ("K-10 bij Astra Enterprise Pk",(-95.00128, 38.96127)),
        ("K-10 × K-7",                  (-94.85289, 38.94101)),
        ("K-7 × I-35 Olathe",           (-94.81556, 38.85570)),
        ("Ottawa KS",                   (-95.23252, 38.61673)),
        ("Emporia KS",                  (-96.17126, 38.41520)),
        ("El Dorado KS",                (-96.88661, 37.83253)),
        ("Wichita I-35 × I-135",        (-97.25057, 37.66449)),
        ("grens KS/OK op I-35",         (-97.34227, 36.99998)),
        ("Oklahoma City I-35 × I-40",   (-97.47233, 35.46346)),
        ("El Reno OK",                  (-97.95474, 35.50142)),
        ("Elk City OK",                 (-99.38886, 35.40230)),
        ("grens OK/TX (Texola)",        (-100.00030, 35.22709)),
        ("Amarillo TX",                 (-101.84663, 35.19435)),
        ("grens TX/NM (Glenrio)",       (-103.04184, 35.18275)),
        ("Tucumcari NM",                (-103.72533, 35.15164)),
        ("Santa Rosa NM",               (-104.67828, 34.94713)),
        ("Albuquerque — the Big I",     (-106.62715, 35.10581)),
        ("Grants NM",                   (-107.85370, 35.14434)),
        ("Gallup NM",                   (-108.74265, 35.53078)),
        ("grens NM/AZ (Lupton)",        (-109.04522, 35.36509)),
        ("Holbrook AZ",                 (-110.15960, 34.91178)),
        ("Winslow AZ",                  (-110.68421, 35.02900)),
        ("Flagstaff I-40 × I-17",       (-111.66233, 35.17225)),
        ("Camp Verde AZ",               (-111.88437, 34.57713)),
        ("Cordes Junction AZ",          (-112.12685, 34.30821)),
        ("Black Canyon City AZ",        (-112.14221, 34.06746)),
        ("Phoenix — the Split I-17×I-10",(-112.04809, 33.42724)),
        ("I-10 × I-8",                  (-111.68375, 32.81949)),
        ("I-8 afrit 172 Thornton Road", (-111.77458, 32.82817)),
        ("Lucid AMP-1 — westpoort",     (-111.78238, 32.85035)),
        ("Lucid AMP-1 — dockrij",       (-111.78008, 32.85724)),
    ],
    "id": "gr-desoto-casagrande",
    "naam": "Panasonic De Soto → Lucid AMP-1 (K-10/K-7 → I-35 → I-40 → I-17 → I-10 → I-8)",
    "extracts": ["us-kansas", "us-oklahoma", "us-texas", "us-new-mexico", "us-arizona"],
    "refs": ["10", "7", "35", "40", "17", "8"],
    "gepubliceerdKm": 2230,
    "bronnoot": "eigen corridormeting 2026-08-04 (grootcirkelsom 2.147 km over 31 punten + ~4%); "
                "geen bron documenteert de vervoerswijze — truck is werkaanname",
    "vensterKm": 40,
    "uit": "stroombeen-desoto-casagrande.geojson",
},
```
```bash
python v2/tools/maak_stroombeen_weg.py --profiel grafiet-desoto-casagrande
```
⚠️ Twee dingen om te lezen in de uitvoer: (1) `refs` bevat zowel `10` (K-10) als `10` (I-10) — het is een zachte voorkeur (factor 3), maar als de lijn ergens raar afbuigt is dit de eerste verdachte; (2) het laatste via-punt is de **dockrij**, en die zit achter `service`-ways — komt de route daar niet, laat dan het dock-via weg en eindig op de poort, met de reststub gerapporteerd als `kmAanloopNaar`. Niet gladstrijken.

### C5 · de stroom herbakken — het volledige commando

Er bestaat geen "voeg één been toe": `vervang_spoorbeen.py` kan alleen vervangen en matcht op modaliteit (bij deze stroom raakt `truck` straks 5 benen). Dus altijd de hele stroom in één keer. Dit hoort letterlijk in `v2/tools/bak_stromen.sh`:

```bash
python v2/tools/hecht_marnet.py route \
  --graaf  v2/build-cache/ais/graaf/mississippi \
  --marnet v2/build-cache/marnet-preais \
  --ne     v2/build-cache \
  --been-geojson "truck|vrachtwagen Balama → Nacala (N380/N1)|v2/build-cache/ais/graaf/stroombeen-balama-nacala.geojson" \
  --stippel      "zee|haven-aanloop Nacala (schematisch — MARNET reikt hier niet)|-14.5383,40.6673|-15.0,41.7" \
  --been         "zee|zeeschip Nacala → Southwest Pass|-15.0,41.7|28.91,-89.43014" \
  --been         "zee|zeeschip Southwest Pass → New Orleans|28.91,-89.43014|29.91230,-90.11200" \
  --been         "binnenvaart|containerbarge New Orleans → Port Allen (IRMT)|29.91230,-90.11200|30.43293,-91.24385" \
  --been         "binnenvaart|containerbarge Port Allen → Port of Vidalia|30.43293,-91.24385|31.53645,-91.48255" \
  --been-geojson "truck|last mile haven → Syrah-fabriek|v2/build-cache/ais/graaf/stroombeen-vidalia-lastmile.geojson" \
  --been-geojson "truck|uitgaand: fabriekspoort → US-84 (Vidalia)|v2/build-cache/ais/graaf/stroombeen-vidalia-us84.geojson" \
  --been-geojson "truck|AAM → Panasonic De Soto (KS)|v2/build-cache/ais/graaf/stroombeen-vidalia-desoto.geojson" \
  --been-geojson "truck|2170-cellen → Lucid AMP-1 (AZ)|v2/build-cache/ais/graaf/stroombeen-desoto-casagrande.geojson" \
  --marker "Balama — mijn/plant|-13.31000,38.66000" \
  --marker "Nacala — containerterminal|-14.53830,40.66730" \
  --marker "Port of New Orleans — Napoleon Ave|29.91230,-90.11200" \
  --marker "Port Allen (IRMT) — bargekade|30.43313,-91.24383" \
  --marker "Port Allen Lock (sluis)|30.43085,-91.20823" \
  --marker "Port of Vidalia — apron (mijl 359)|31.53645,-91.48255" \
  --marker "Syrah AAM-fabriek Vidalia|31.54660,-91.48870" \
  --marker "Panasonic Energy Kansas — De Soto (volume nul)|38.93815,-95.00240" \
  --marker "Lucid AMP-1 — Casa Grande (volume nul)|32.85724,-111.78008" \
  --routebrief v2/design/routebrieven/grafiet-balama-vidalia.md \
  --uit    v2/data/stroomroute-pilot.json \
  --stroom grafiet-balama-vs \
  --titel  "Grafiet · Balama → Vidalia → De Soto → Casa Grande"
```

Aandachtspunten die je niet mag verschuiven: `--marnet` wijst naar `build-cache/marnet-preais`, **nooit** naar `v2/data/` (de bol mag het waternet niet laden). Zodra er één `--marker` staat vervangt de lijst de automatische afleiding volledig — dus alle negen moeten erin. `--vermijd` default `northwest` laten staan. De volgorde van `--been`/`--stippel`/`--been-geojson` **is** de reisvolgorde (één gedeelde lijst).

Resultaat: **10 benen**, HUD-regel wordt `truck … · zeeschip … · binnenschip …` (de HUD telt per modaliteit op, dus de vijf truckbenen worden één regel — dat is bestaand gedrag, geen bug).

---

## D · Wijzigingen in `grafiet-balama-vidalia.md`

| sectie | wat er moet gebeuren |
|---|---|
| **kop / statusregel** | "fase D–E concept (prospectief)" → **"fase D–E getekend, volume nul"**, met de datum en de naam van het besluit (projecteigenaar, 2026-08-04) |
| **nieuw blok direct onder de kop** | *De nul-volume-notitie*: Balama ligt stil, "Graphite Shipped to Vidalia" 2025 = 0, t/m Q2 2026 alleen ~150 t kwalificatiemonsters. **De weg is echt, de lading nog niet.** Expliciet: D/E worden **doorgetrokken** getekend omdat ze op echt wegnet liggen; stippel blijft voorbehouden aan "hier reikt het net niet" |
| **§1 ketenkaart** | b3/b4 splitsen met de echte IRMT-kade; b5 van "~1–4 km stippel" naar "2,3 km doorgetrokken"; b6/b7/b8 met hun gemeten lengtes; het ASCII-schema bijwerken |
| **§2 fase D** | emballage: "niet gedocumenteerd" → **supersacks/bigbags** (EA-2181 §2.2), tot 11.200 t/j, 45–55 trailers/maand |
| **§3 kernfeit 4** | het redactionele besluit erbij: tekenen ondanks nul volume, met de reden |
| **been 3 punt 8 · been 4 punt 2** | sluis `30.4415,-91.2075` → **`30.43085, -91.20823`**, status satelliet-gelegd + OSM way 1465620640 + AIS |
| **overslag O4 + been 3 punt 9 + been 4 punt 1 + §5.6** | IRMT `30.432,-91.222` → **`30.43313, -91.24383`**, routeerpunt `30.43293,-91.24385`, max snap 0,05 km. Nieuwe alinea over de **geografische vergissing**: de IRMT ligt aan het doodlopende Slack Water Canal, niet aan de doorgaande GIWW — daarom faalde de ankercheck. Been 4 krijgt er ~4,5 km bij (kade → zijkanaal → aftakking ~30.4363/-91.2500 → GIWW → sluis → rivier). Aankomst- en vertrekanker vallen samen (één ligplaats), mét het voorbehoud van §5.5 |
| **overslag O5 + been 4 punt 8 + been 5** | Vidalia `31.538,-91.485` → **`31.53645, -91.48255`** (apron), ramp-kop `31.53530,-91.48090` als routeerpunt; het oude punt staat in batture-bos. Been 5: lengte **2,34 km gemeten** over grindweg → LA-131 → D.A. Biglane Rd → inrit; stippel → doorgetrokken, mét de reden; "~4 km" wordt een bevinding |
| **been 6** | punt 2 corrigeren: "fabriekspoort → LA-131" klopt niet — het terrein grenst aan **D.A. Biglane Road**. Keten wordt: laaddock (open) → terreinweg → **poort 31.54796, -91.48743** → 0,37 km ZO → **LA-131 31.54530, -91.48503** → US-84. Punt 3 "~3 km" vervangen door **6,98 km naar 31.56647, -91.42737** (of 5,46 km via Airport Road `31.58728,-91.49884` — welke van de twee is open) |
| **been 7** | volledige puntentabel (28 punten uit C3) met status per punt; Ferriday-naam corrigeren: **US-84 × US-425 (+LA-15/LA-568)**, niet US-65 — US-65 begint 9,85 km noordelijker bij Clayton `31.71606,-91.53875`; km "~10" → **13,1** (kortste route) resp. 14,8 (vanaf LA-131); lengte "~1.100 km" → **~1.160 km**; negatieve ankers mét straal (Natchez-brug 1,5 km · Jackson 25 · battery belt 150 · Memphis 100 · Lake Providence/Tallulah 30 · Crossett 8 · Monroe 30 · Shreveport 75 · Tulsa 100 · oude US-71 Bella Vista 4); **het reële alternatief als eigen klasse**: US-65 Ozarks + MO-13/MO-7, 1.084 km = 6% **korter**, verworpen op NHFN-aanwijzing + wegvorm + reistijd. Vermeld dat km 0–473 en 1.070–1.156 in beide varianten identiek zijn |
| **been 8** | volledige puntentabel (31 punten uit C4); lengte "~1.900 (indicatief)" → **~2.230 km** (ondergrens 2.147 over 31 punten); modaliteit blijft open (truck = werkaanname, intermodaal spoor niet uitgesloten); lading is **UN3480 klasse 9** maar zonder plakkaatplicht binnenlands wegvervoer → geen routeplicht; negatieve ankers incl. het BNSF-Transcon-tracé (Wellington/Clovis/Belen, 25 km) als verklikker voor een per ongeluk gebakken spoorlijn |
| **verwerkingsknoop De Soto** | anker-id `gr-fab-desoto` = **terreinanker**, docks open; adresconflict 10301 vs 10701; geen actief spoor op het terrein |
| **nieuwe verwerkingsknoop AMP-1** | anker `gr-lucid-amp1` = inkomende dockrij westgevel; uitsluitingen (autoparking zuid = uitgaand, oostgevel = personeel, noordblok in aanbouw, geen spoorstomp op het terrein); adresconflict 317 W Selma Highway vs 317 South Thornton Road |
| **§5 openstaande punten** | **sluiten:** 6 (IRMT-kade) · 7 (Vidalia-kade) · 8 (last-mile-lengte + poort) · 12 gedeeltelijk (terrein De Soto gelegd, docks open) · 15 gedeeltelijk (AMP-1-dock gelegd, modaliteit open). **Verkleinen, niet sluiten:** 10 (corridor b7 afgeleid; alleen het middenstuk Conway–Harrisonville hangt aan de keuze). **Toevoegen:** westelijke ingang Syrah niet gelokaliseerd · "Daul Drive" niet te geocoderen (vrachtpoort De Soto) · adresconflicten · US-54/NM-status ("qualifying federal aid primary"?) · vrachtroute-/gewichtsbeperking door Ferriday-kern · welke van de twee US-84-aansluitingen · Kansas Turnpike als tolgevoelige afwijking |
| **§6 afwerklijst** | rij 10 (`aansluitingen.json`) en 11 (fase-D/E-ankers) op **doorgevoerd**; drie rijen erbij voor de sluis-, IRMT- en Vidalia-correctie |
| **§7 wat de kaart tekent** | 10 benen; punt 4 ("géén spoorbeen, uitgaand niet tekenen") herschrijven naar het nieuwe besluit; punt 6 (fase E pas bij fysieke leveringen) vervangen; nieuwe ketenstand invullen ná de meting |
| **§8 checklist** | afvinken wat nu klopt; de regels over satelliet-gelegde laad-/los-/overslagplekken blijven **onafgevinkt** voor de drie niet-gevonden docks |
| **§9 bronnen** | erbij: EA-2181 Fig. 1 (Front Gate + Project Center) · portgbr `IRMT-Map.pdf` · MarineCadastre `vs-landelijk.jsonl.gz` · Overpass 2026-08-04 · KDHE/Kansas Register 50871 + 52452 · FHWA NHFN 2022 · 23 CFR 658 App. A · SSOE · Esri Wayback 22252/32246 |

---

## E · Volgorde en controlepunten

**0 · Nulmeting (vóór je iets aanraakt).**
```bash
python v2/tools/toets_knikken.py > /tmp/knikken-voor.txt
sha256sum v2/build-cache/ais/graaf/stroombeen-*.geojson v2/data/stroomroute-pilot.json
python v2/tools/maak_aansluitingen.py          # zonder --schrijf: generator↔uitvoer moet 18/18 op 0,0 m
```
Leg de huidige benen/km/punten van alle vijf stromen vast. Zonder deze regel weet je straks niet of iets verschoof of altijd al zo stond.

**1 · Gereedschapsfix (B4) — en meteen de regressietoets.** `eindKlassen` per profiel. Draai daarna **beide bestaande profielen** opnieuw:
```bash
python v2/tools/maak_stroombeen_weg.py --profiel grafiet-balama-nacala
python v2/tools/maak_stroombeen_weg.py --profiel lithium-greenbushes-bunbury
sha256sum v2/build-cache/ais/graaf/stroombeen-*.geojson   # moet identiek zijn aan stap 0
```
**Eis: byte-identiek.** Niet identiek = de default-tuple is toch geraakt → terug, want dan is de cachevingerafdruk veranderd en drijft de lithiumstroom mee.

**2 · De vier nieuwe wegbenen bakken (C1→C4), één voor één.** Per been meteen lezen: lengte t.o.v. `gepubliceerdKm` (±10%), `kmAanloopVan/Naar`, en het `snoei_keerlussen`-rapport. Een 180°-keerpunt betekent dat een via-punt op een zijtak ligt → projecteer het op de dichtstbijzijnde trunk/primary-vertex (de Balingup-les), verplaats het niet op gevoel. Buiten de tolerantie = **een bevinding die blijft staan**, geen via-punt bijschuiven om het getal te halen.

**3 · Verklikkers per been, vóór het herbakken.** Meet voor elk nieuw geojson de afstand tot elk negatief anker uit D. Eisen: b7 raakt Oklahoma niet, komt niet binnen 4 km van `36.48,-94.27` (oude US-71) en niet binnen 1,5 km van het oostelijke landhoofd van de Natchez-brug `31.56430,-91.39790`; b8 komt nergens boven 39,0°N en niet binnen 60 km van `33.80009,-110.50003` (Salt River Canyon).

**4 · Stroom herbakken (C5)** en het commando in `v2/tools/bak_stromen.sh` zetten. Dat script is vanaf nu de generator; het gebakken json is de uitvoer. Commit ze in één commit — als ze uit elkaar lopen is het de `cu-guixi-spoor`-klasse.

**5 · Meten aan het gebakken eindproduct** (niet aan de meetlat — de fout van 28-07):
- het snippet uit B1: 10 benen, gaten tussen opeenvolgende benen ≤ 0,5 km en elk gat verklaard als anker≠routeerpunt;
- lengte per been tegen de brief: b1 ≈ 503 · zee-aanloop 122 (stippel) · zee 16.849 · zee-opvaart 191 · b3 ≈ 200–215 · b4 ≈ 200–215 · b5 ≈ 2,3 · b6 ≈ 7,0 · b7 ≈ 1.150 · b8 ≈ 2.230; totaal ≈ **21.500 km** (was 18.070);
- `python v2/tools/toets_knikken.py` en **diff tegen `/tmp/knikken-voor.txt`** — de vier andere stromen moeten ongewijzigd zijn; nieuwe omkeringen in de grafietstroom zijn een bevinding, geen ruis;
- markers: elke marker ≤ 0,15 km van de lijn (Port Allen was 2,08 km).

**6 · `aansluitingen.json` regenereren** (`--schrijf`) en de gerapporteerde snaps lezen. Verwacht: Port Allen binnen ≈ 0,05 km · Vidalia-apron binnen ≈ 0,45 km · Nacala/Napoleon zoals bekend · AMP-1 weg ≈ 0,03 km (interne apron-way) of ~1,1 km (alleen openbaar wegnet). Een grote snap is hier een **meetresultaat**, geen fout — maar noteer hem in de brief als max snap.

**7 · `data/graphite.js`** (B7) en daarna een schone build/laadcheck: geen console-fouten, `stroomRegel` toont vijf modaliteitsregels.

**8 · `?v=`-bump** (B8) en de brief bijwerken (D). Pas dan pushen; stuur de klikbare Pages-URL mét het nieuwe `?v=` nummer mee.

**9 · Wrapup** volgens de Definition of Done — inclusief Linear en de vault; en zet in `memory/next-actions.md` dat de bak-commando's van de **vier andere** stromen nog steeds nergens staan (dit werk lost alleen de grafietstroom op).

⚠️ **Ontbrekend gereedschap:** `toets_corridor.py` bestaat niet in de repo (stond in een scratchpad en is verdwenen — precies de klasse fout die `sat_check.py` naar `v2/tools/` bracht). De dekkings-/verklikkertoets van stap 3 en 5 moet je dus opnieuw schrijven; doe dat als **`v2/tools/toets_corridor.py`** met een expliciete puntenlijst + verbodsstralen als invoer, zodat hij deze keer blijft bestaan.

---

## F · Wat NIET af komt

**Niet gevonden — geen coördinaat, geen anker, geen lijn:**

1. **Het uitgaande AAM-laaddock bij Syrah Vidalia.** Esri z19 (0,25 m/px) is de fijnste beschikbare opname en toont geen dockperron; met 45–55 trailers/maand (≈2 per werkdag) volstaat één overheaddeur op maaiveld, en die is op deze korrel niet van een gevelopening te onderscheiden. Dit is een uitsluiting van een **zichtbaar perron**, niet van een laadpunt. Been 6 begint daarom bij de **poort**. Vervolgweg: LDEQ Minor Source Air Permit (nov 2021) met plot plan, of een NAIP-/oblique-opname.
2. **Beide docks bij Panasonic De Soto** (inkomend b7 én uitgaand b8). Oorzaak is de **opnamedatum**, niet het zoekwerk: live Esri = Wayback 32246 (2026-06-30) en dat is de bouwfase, terwijl de fabriek sinds 14-07-2025 draait. Dit is de Shed 8-8-klasse. De knoop krijgt dus **één terreinanker en niet de twee ankers die §2b eist**; dat hoort zo in de brief te staan, niet weggepoetst. Kandidaatzone (vermoeden, géén coördinaat opgevoerd): het betonschort oost van de oostgevel.
3. **Grindrod Cross Dock Facility** (Nacala, aankomstanker O1) en **beide Durban-ligplaatsen** (O2) — ongewijzigd open.
4. **De westelijke ingang van het Syrah-terrein** (EA noemt "east and west ends"); de oostelijke is aannemelijk gelokaliseerd op `31.54584, -91.48547`, de westelijke niet.
5. **"Daul Drive"** — de trucks-only-ingang van De Soto uit de planningsberichtgeving bestaat niet in OSM en is niet te geocoderen. Het routeerpunt dat we gebruiken (rotonde Astra Parkway) is de **werknemersingang**; de vrachtingang ligt vermoedelijk oost. Niet hard genoeg om te leggen.

**Blijft onzeker — gaat als openstaand punt de brief in:**

6. **Modus b3** (New Orleans → Port Allen): COB-shuttle of truck. Zolang dat open staat is het samenvallen van aankomst- en vertrekanker bij de IRMT **voorwaardelijk**; bij truck is het aankomstanker de terminalpoort en die is niet gelegd.
7. **De corridorkeuze in het midden van b7** (Conway AR → Harrisonville MO, 597 km). Het reële alternatief is 6% **korter**; de keuze rust op NHFN-aanwijzing, wegvorm en reistijd, niet op een bron. Teken km 0–473 en 1.070–1.156 zonder voorbehoud, markeer het middenstuk als keuze.
8. **De modaliteit van b8.** Truck is werkaanname; intermodaal spoor is niet uitgesloten (BNSF bij De Soto, UP bij Casa Grande — twee maatschappijen, dus een interchange). Slaat dit om, dan vervangt het de héle lijn in plaats van hem te verschuiven. Ondersteunend negatief bewijs: geen spoorstomp komt het Lucid-terrein op (dichtstbijzijnde op 193 m ten noorden van de terreingrens).
9. **Welke dockdeuren in de AMP-1-westgevel inkomend zijn** — de gevel is hard, de deur niet.
10. **Welke US-84-aansluiting de trucks in Vidalia werkelijk gebruiken** (LA-131 6,98 km vs Airport Road 5,46 km), en of er een vrachtroute-/gewichtsbeperking door de kern van Ferriday geldt.
11. **Adresconflicten** (10301 vs 10701 Astra Parkway; 317 W Selma Highway vs 317 South Thornton Road) en de juridische status van US-54 in New Mexico.
12. **Golf-toegang** (Yucatán vs Straat Florida) — `wp-florida` blijft een gok (§5.3).

**Wat gestippeld blijft:** alleen de haven-aanloop van Nacala (~122 km, MARNET reikt daar niet — eindvorm, geen tussenstand). De last mile in Vidalia verliest zijn stippel omdat het net er wél reikt. Fase D en E worden **doorgetrokken** getekend: de weg is gemeten, alleen de lading ontbreekt, en dat verschil hoort in de tekst te staan — niet in de lijnstijl.

**Statuswaarschuwing bij de oplevering:** in de brief mag De Soto **niet** als "satelliet-gelegde losplek" komen te staan. Het is "terrein satelliet-gelegd, docks open". Een anker dat niet satelliet-gelegd is, is geen anker.
