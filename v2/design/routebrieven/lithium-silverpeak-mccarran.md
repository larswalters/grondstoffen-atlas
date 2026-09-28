# Routebrief (licht) · lithium — Van → Via → Naar (land)

**stroom-id:** `lithium-silverpeak-mccarran` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** lithiumcarbonaat van Albemarle's Silver Peak-brineoperatie (Clayton Valley, Esmeralda
County, Nevada — de enige actieve Amerikaanse lithiummijn) gaat per truck ~300–330 km over US-95 noordwaarts
en US-95A/I-80 naar de Tahoe-Reno Industrial Center bij Sparks, waar Tesla's Gigafactory Nevada (met Panasonic
als celfabricage-partner op hetzelfde terrein) staat — de enige volledig binnenlandse as van de atlas: geen
zee, geen grens, kleinste volume van de vijf nieuwe M31-golf-2-ketens.
**Welke as van het verhaal:** *het IRA-onshoring-verhaal in het klein.* Amerikaanse lithiummijn → Amerikaanse
batterijfabriek, ~255 km hemelsbreed, binnen één staat. Volume klein (≈5 kt LCE/j, v1-register) en de
specifieke levering aan Gigafactory Nevada is **niet bevestigd** — dit is de kortste, meest voor de hand
liggende regionale stroom, geen gedocumenteerd offtake-contract.

## 1 · Ketenkaart
```
Silver Peak-plant `li-silverpeak-plant` ──(b1 truck · US-95 N → US-95A → I-80 W ·
via Tonopah/Mina/Hawthorne/Schurz/Silver Springs/Fernley · ~300–330 km, aannemelijke bestemming)──►
Gigafactory Nevada / Tesla Gigafactory 1 `li-gigafactory-fabriek` ⏹ stoppunt (Panasonic celfabricage
op hetzelfde terrein)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (lithiumcarbonaat) | `li-silverpeak-plant` → `li-gigafactory-fabriek` | NV-265 → US-95 N (Tonopah–Mina–Hawthorne–Schurz) → US-95A (Silver Springs–Fernley) → I-80 W (USA Parkway/Exit 46) → TRIC | niet gepubliceerd; ontwerpschatting 300–330 [ontwerp]; hemelsbreed-som via-punten 330,8 [eigen berekening, §8] | maak_stroombeen_weg (extract us-nevada) | nee — **aannemelijke bestemming**: geen bron koppelt Silver Peak-carbonaat specifiek aan Gigafactory Nevada; de weg zelf is een gewone doorgaande verharde route |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-silverpeak-plant` | mijn / brineplant (laadplek) | Albemarle Silver Peak — Clayton Valley-brineoperatie, Esmeralda County | 37.7693, -117.5768 | [5][6] hergebruik anker `w-li-silverpeak` uit `lithium-sitelaag.json` | **bron-gelegd** (z15 gezien: kruis midden op het verdampingsvijverveld — turkooise/groene bekkens, klassiek brine-operatiebeeld; eigen herbevestiging op dezelfde korrel, [7]) |
| `li-gigafactory-fabriek` | fabriek (losplek, fase C-eind) | Tesla Gigafactory 1 / Gigafactory Nevada, Tahoe-Reno Industrial Center, Storey County (1 Electric Avenue) | 39.5403926, -119.4390524 | [1][3][8] OSM-object "Tesla Gigafactory 1" + haalbaarheidstoets-webcheck | **bron-gelegd** (z15 gezien: langwerpig fabrieksgebouw met zonnepanelen op het dak, omringd door grote parkeer-/vrachtwagenterreinen, temidden van het TRIC-industriepark [7]; Panasonic is celfabricage-partner op datzelfde terrein, geen aparte site [1][8]) |

## 4 · Via-punten (b1 — enige landbeen, corridorkeuzes)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Tonopah (junctie US-6/US-95) | 38.1001, -117.2251 | hier komt de weg vanaf Silver Peak (NV-265) op de doorgaande US-95 noordwaarts |
| b1 | 2 | Mina (junctie US-95/SR-359) | 38.3905, -118.1087 | vervolg van de enige noordwaartse corridor, geen alternatief |
| b1 | 3 | Hawthorne (US-95 langs Walker Lake) | 38.5254, -118.6270 | grootste plaats onderweg, doorgaande route pint de richting westelijker langs het meer |
| b1 | 4 | Schurz (splitsing US-95 door naar Fallon vs. US-95A oostwaarts) | 38.9762, -118.8385 | corridorkeuze: hier neemt de route **US-95A** i.p.v. door te rijden op US-95 naar Fallon/I-80 verderop noordelijk |
| b1 | 5 | Silver Springs (junctie US-95A/US-50 ALT) | 39.3736, -119.2267 | pint de doorgaande US-95A-route richting Fernley i.p.v. afslag naar Fallon/Carson City |
| b1 | 6 | Fernley (junctie met I-80) | 39.6079, -119.2506 | hier gaat de corridor over op **I-80 westwaarts** naar de TRIC-afslag (Exit 46/USA Parkway) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Silver Peak-plant | Albemarle | brine (Clayton Valley) → lithiumcarbonaat | ≈5 kt LCE/j (niet apart geverifieerd voor deze as) | [5][6] |
| Gigafactory Nevada — celproductie | Tesla / Panasonic (celfabricage-partner op hetzelfde terrein) | lithiumcarbonaat/-hydroxide (herkomst gemengd, niet exclusief Silver Peak) → batterijcellen | niet gepubliceerd in Li-eenheden voor dit specifieke aandeel | [1][8] |

## 6 · Stoppunt
De brief stopt aan de poort van Gigafactory Nevada / Tesla Gigafactory 1: dat is het enige stroomafwaartse
punt dat de haalbaarheidstoets aanwijst, en Panasonic zit als celfabricage-partner op datzelfde terrein in
plaats van als aparte site. Geen bron noemt welk celtype of welke klant specifiek Silver Peak-carbonaat
verwerkt — fase D vervalt (haalbaarheidstoets §"aanpassing"; ontwerp-§"risico").

## 7 · Open punten
- **Geen bevestigde leveringsrelatie Silver Peak → Gigafactory Nevada.** Dit is een plausibele regionale
  stroom (kortste route, zelfde staat, batterijvraag vlakbij) — géén gepubliceerd offtake-contract. Het hele
  been b1 draagt daarom het label *aannemelijke bestemming* in plaats van *bevestigd*, ook al is de
  wegcorridor zelf een gewone doorgaande route zonder bijzonderheden.
- **Gepubliceerde weg-km ontbreekt volledig** voor b1: alleen een ontwerpschatting (300–330 km) en de eigen
  hemelsbreed-som over de zes via-punten (330,8 km, §8) zijn beschikbaar. De bake-lengtetoets loopt dus tegen
  de kaartafstand, niet tegen een gepubliceerd getal.
- **Fase D (celtype/klant) vervalt** — Panasonic produceert cellen op hetzelfde terrein maar geen bron
  koppelt specifiek Silver Peak-carbonaat aan een celtype of eindklant.
- **Jaarvolume (~5 kt LCE/j) komt uit v1-register/Albemarle-bedrijfsinformatie**, niet apart geverifieerd of
  van een peiljaar voorzien voor deze specifieke as (§ ontwerp-invoer "jaarvolume_en_bron").
- **Welk aandeel van Silver Peak's productie (indien enige) daadwerkelijk richting Gigafactory Nevada gaat**
  tegenover andere klanten van Albemarle's battery-grade lithiumcarbonaat is niet gedocumenteerd.

## 8 · Bronnen
[1] Wikipedia (en), "Gigafactory Nevada" — locatie Tahoe Reno Industrial Center/Storey County, Panasonic als
celfabricage-partner (basisovereenkomst 2014, investering ~US$1,6 mld), Tesla-eigendom. https://en.wikipedia.org/wiki/Gigafactory_Nevada
[2] Wikipedia (en), "Silver Peak, Nevada" — CDP aan State Route 265, Esmeralda County, coördinaat van de
gemeenschap (37.755, -117.6347; afwijkend van het bron-gelegde plant-anker verderop op de salarwerken). https://en.wikipedia.org/wiki/Silver_Peak,_Nevada
[3] OpenStreetMap (ODbL) via Nominatim — "Tesla Gigafactory 1", 1 Electric Avenue, Storey County, Nevada,
39.5403926/-119.4390524. https://nominatim.openstreetmap.org
[4] OpenStreetMap (ODbL) via Nominatim — plaatscoördinaten Tonopah/Mina/Hawthorne/Schurz/Silver
Springs/Fernley/Tahoe Reno Industrial Center. https://nominatim.openstreetmap.org
[5] `v2/design/lithium-sitelaag.json`/`.md` — anker `w-li-silverpeak` (Albemarle Silver Peak), 37.7693/-117.5768,
bron-gelegd, capaciteit ≈5 kt LCE/j, hergebruikt voor dit document.
[6] `data/lithium.js` (v1-register), `li-silver-peak` — "enige actieve Amerikaanse lithiummijn — en klein: zo'n
5 kt LCE per jaar", share 1%, USGS-afgeleid.
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15, 2026-09-28) —
`v2/build-cache/satcheck/sat-lithium-silverpeak-mccarran-silverpeak.png`,
`sat-lithium-silverpeak-mccarran-gigafactory.png`.
[8] Haalbaarheidstoets M31 golf 2 (orkestrator-invoer, 2026-09-28) — webcheck OSM Nominatim "Gigafactory
Nevada Sparks" → Tesla Gigafactory 1, 39.5403926/-119.4390524; bindende aanpassing: eindanker vastgelegd op
dit OSM-object, Panasonic als celfabricage-partner op hetzelfde terrein i.p.v. aparte site.
[9] Geofabrik, `us-nevada-latest.osm.pbf` — lokaal aanwezig in `v2/build-cache/geofabrik/`, wegnet-extract
voor de bak-agent (`maak_stroombeen_weg.py`).
[10] Eigen berekening (grootcirkel) op de in dit document gelegde ankers en via-punten — hemelsbreed-som
330,8 km over de zes via-punten; directe hemelsbreed-afstand plant→fabriek 254,8 km.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `lithium-silverpeak-mccarran`** → `v2/data/stroomroute-lithium-silverpeak-mccarran.json` — **1 been,
346,5 km**, 2.483 punten, 2 markers. truck 346,5 km. Recept: `bak_stromen.sh` (functie
`bak_lithium_silverpeak_mccarran`).

**b1 (truck, nieuw profiel `lithium-silverpeak-mccarran-silverpeak-gigafactory`, extract us-nevada):**
via-punten Albemarle Silver Peak (anker) → Tonopah → Mina → Hawthorne → Schurz → Silver Springs → Fernley →
Tesla Gigafactory Nevada (anker). **346,5 km, 2.483 punten**, snaps 0,11–1,36 km (alle ruim onder de 5 km-norm),
15 keerlussen gesnoeid (462,2 → 346,3 km, dubbel gereden stukken bij vier van de zes junctiepunten). Tegen de
ontwerpschatting van 315 km (middenwaarde van de gepubliceerde 300-330 km) is dit **+9,9% [OK]**, ruim binnen
±15%; ook tegen de eigen hemelsbreed-som van de via-punten (330,8 km, brief §8) is de omwegfactor 1,05 —
plausibel voor een grotendeels rechtdoorgaande hoofdweg. `corridorKlassen: tertiary/unclassified` was nodig
voor NV-265 bij Silver Peak zelf (tweebaans landelijke staatsweg); `eindKlassen` verruimd met track/residential/
service liet 38,15 km first-mile en 5,86 km last-mile over kleine klassen toe (geen "geen wegpad"-fout).

**Geen zee/spoor/leiding/binnenvaart, geen haven-aanloop:** enige volledig binnenlandse as van de atlas (brief
§1), geen kade in deze keten.

**Geen stippel:** dit is de enige doorgaande verharde route tussen de twee sites (design-noot, brief §2
bevestigt dit); het been draagt wél het label *aannemelijke bestemming* in de beennaam (geen offtake-contract),
niet omdat het net ontbreekt — conform werkwijze §7 staat "aannemelijk" alleen in de naam, niet in de lijnstijl.

**Geen fase D/E:** conform brief §6 — Panasonic produceert cellen op hetzelfde TRIC-terrein als
celfabricage-partner, geen aparte site; geen bron koppelt een celtype/eindklant specifiek aan
Silver Peak-carbonaat.

**Toets:** naad **0,00 km** (enige been, geen voorganger). `toets_knikken.py`: **17 knikken ≥60° totaal, 3
omkeringen ≥150°, 0 TERUGLOOP** — niets te repareren; de drie scherpe bochten (180,0°/163,4°/150,9°) liggen op
echte OSM-junctieknopen (Schurz-splitsing, Fernley/I-80-aansluiting, Silver Peak-toegangsweg) en zijn
"scherpe bocht, echt" volgens het tool, geen artefact. `toets_rechte_benen.py --min-km 5`: **geen regel voor
deze stroom** (geen been ≥5 km met omwegfactor 1,000). json geldig: versie 2, punt_formaat lonlat, modaliteit
uitsluitend {truck}, het ene been ≥2 punten, **bestandsgrootte 53,6 KB** (ruim onder de ~300 KB-richtwaarde).
Beide markers liggen op **0,0 m** van de lijn (marker = been-uiteinde).

**Gereedschapslessen:**
- **Bij een enkel truckbeen zonder haven/spoor is de bake-stap triviaal** (`--been-geojson` neemt de
  vooraf gescande lijn letterlijk over) — de enige inhoudelijke stap zit in het wegprofiel en de
  `corridorKlassen`/`eindKlassen`-keuze bij de wegscan.
- **Een via-puntenketen met "geen alternatief"-corridorkeuzes (brief §4: elk via-punt pint een keuze zonder
  reëel alternatief) geeft een lage omwegfactor (1,05) en dus een betrouwbare lengtetoets zelfs zonder
  gepubliceerde bron-km** — de eigen hemelsbreed-som en de gemeten weggeometrie bevestigen elkaar.
