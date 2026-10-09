# Routebrief (licht) · kobalt — Raglan → Deception Bay → Québec → Sudbury (Canada)

**stroom-id:** `kobalt-raglan-sudbury` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** nikkel-koper-kobaltconcentraat van de Raglan-mijn en -concentrator (Glencore, Katinniq, Nunavik) per **truck** over de grindweg naar Glencore's eigen kade in Deception Bay, per **ijsklasse-schip** (MV Arvik-1) door de Hudsonstraat, langs Labrador en over de Saint-Laurent naar de Glencore-terminal in de haven van Québec, dan per **spoor** (CN, via Montréal en Toronto) naar de Glencore Sudbury Smelter. Seizoensvaart, circa 8 maanden per jaar [1][4]. Stoppunt Sudbury; de matte-keten daarna staat in `kobalt-sudbury-kristiansand`.
**Welke as van het verhaal:** de Arctische voeder van de Canadese nikkel-kobaltketen. **Jaarvolume: 0,822 kt Co/jaar** (822 t kobalt, productie 2025, Glencore Raglan "our mining activity") [1]; vervoerd als ~240.000 t concentraat in ~8 reizen [3]. Eenheid: kt Co per jaar. Het kobalt zit in het concentraat (naast 39,9 kt Ni) [1][2]; het is een bijproduct, geen eigen mijnbouwstroom. Het ontwerp (Wikipedia: 200 t Co, ontwerpcijfer zonder peiljaar [4]) is achterhaald; de haalbaarheidstoets (geen Co-cijfer) is door deze bron achterhaald.

## 1 · Ketenkaart
```
Raglan-mijn/concentrator `co-raglan-mijn` ──(b1 truck · Route Baie Déception–Katinniq, grind · 95,9 OSM-km, bedrijfsopgave 100)──►
Deception Bay-kade `co-deceptionbay-kade` ──(b2a zee-haven-aanloop, STIPPEL · 119,8 km)──► MARNET-zeeknoop 471 (63.2000, -75.0000)
   ──(b2 zee · Hudsonstraat → Labradorzee → Belle Isle/Cabot (router) → Golf → Saint-Laurent · 3.224,8 km, MARNET)──►
Québec-kade `co-quebec-kade` ──(b3 spoor · CN Kingston Sub → Taschereau Yard → MacMillan Yard → CN Bala Sub · 1.293,6 km)──►
Sudbury Smelter `co-sudbury-smelter` ── stoppunt
```
**Alle benen zijn letterlijke kopieën van `nikkel-raglan-sudbury`** (zelfde geojsons en zelfde MARNET-invoer, zie §2 en `bak_nikkel_raglan_sudbury` in `v2/tools/bak_stromen.sh`); alleen de ankernamen (co-), beennamen en titel zijn nieuw. Seizoen: de kade is ~8 maanden per jaar bereikbaar [1][4]; de lijn is een jaargemiddelde.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-raglan-mijn` → `co-deceptionbay-kade` | Route Baie Déception–Katinniq (OSM tertiary, grind), 11 ways, geen zijtak | **gebakken 95,9** (OSM-ketensom); bedrijfsopgave **100 km** (Glencore) [1] → −4,1% | kopie `nikkel-raglan-sudbury-weg-raglan-deceptionbay-osmketen.geojson` | nee |
| b2a | B | zee | `co-deceptionbay-kade` → zeeknoop 471 | haven-aanloop over water | 118,3 hemelsbreed; kopie **119,8** | kopie `nikkel-raglan-sudbury-aanloop-deceptionbay.geojson` | **ja** (net reikt niet; kade 118,3 km van de zeeknoop, ruim > 5 km en > 25 km snap) |
| b2 | B | zee | zeeknoop 471 → `co-quebec-kade` | MARNET kiest (Hudsonstraat, Belle Isle, Saint-Laurent) | **3.224,8** gebakken; Glencore noemt 2.600 km voor de vaart zelf [1] (b2a + b2 = 3.344,6, +28,6%; geen norm, MARNET-aanloop en Hudsonstraat-route) | MARNET, invoer 63.2000,-75.0000 → 46.8330,-71.2035 | nee (Québec-kade 1,62 km van zijn zeeknoop) |
| b3 | C | spoor | `co-quebec-kade` → `co-sudbury-smelter` | CN Kingston Sub + CN Bala Sub, via Taschereau Yard en MacMillan Yard | kopie **1.293,6** (286,9 + 541,0 + 465,7); webcheck ~1.230 (+5,2%, binnen ±15%) | kopie drie `spoorroute-nikkel-raglan-sudbury-{quebec-taschereau,taschereau-macmillan,macmillan-sudbury}.geojson` + slot b0 | alleen slot-emplacement 0,16 km |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-raglan-mijn` | mijn + concentrator | Raglan Mine, Katinniq (Glencore) | 61.6876, -73.6750 | hergebruikt letterlijk `ni-raglan-mijn` uit `nikkel-raglan-sudbury` §3 [1][6] | bron-gelegd (z15 opnieuw gezien: groot industrieel complex met molengebouw en transportband, tailingsmeer, kampvleugels, open pit ernaast) |
| `co-deceptionbay-kade` | overslag truck → zee | Deception Bay-kade (Glencore, pier uit 1971) | 62.1458, -74.6933 | hergebruikt letterlijk `ni-deceptionbay-kade` [1][6] | bron-gelegd (z15 opnieuw gezien: kruis op de pier met kadedek; ~300 m ten zuiden de grote koepelloods, passend bij "stored in a dome" [1]) |
| `co-quebec-kade` | overslag zee → spoor | Glencore-terminal, Port de Québec, Beauport | 46.8330, -71.2035 | hergebruikt letterlijk `ni-quebec-kade` / `co-quebec-kade` uit `kobalt-sudbury-kristiansand` [3][7] | aannemelijk (z15 opnieuw gezien: tankenpark en bulkkades in Beauport; welke steiger Glencore's terminal is, is niet te zien) |
| `co-sudbury-smelter` | losplek / smelter | Glencore Sudbury Smelter (Falconbridge) | 46.5786, -80.7993 | hergebruikt letterlijk `co-sudbury-smelter` uit `kobalt-sudbury-kristiansand` [7] | bron-gelegd (z15 opnieuw gezien: smelterconcern met schoorsteen en rangeeremplacement) |
Zeeknoop 471 is een routeerpunt, geen anker. Beelden: `v2/build-cache/satcheck/sat-kobalt-raglan-sudbury-{mijn,deceptionbay,quebec-kade,smelter}.png`.

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | wegknoop OSM-ways 587588827/949525173 | 62.0987, -74.5456 | kopie uit `nikkel-raglan-sudbury` §4; op de doorgaande weg, stabiliseert tegen service-sporen bij de haven |
| b1 | 2 | wegknoop 949525174/517305879 | 62.0952, -74.3177 | idem, begin van de 64 km-lange hoofdway |
| b1 | 3 | wegknoop 517305879/1266330307 | 61.7176, -73.7173 | idem, laatste 8 km naar de concentrator |
| b3 | 4 | MacMillan Yard (CN, Vaughan) | 43.8119, -79.5111 | in de gekopieerde geometrie; houdt de route om Toronto-lakeshore |
| b3 | 5 | Taschereau Yard (CN, Montréal) | 45.4686, -73.6861 | in de gekopieerde geometrie; pint de Kingston Sub door Montréal |
Er worden geen nieuwe via-punten gelegd en geen nieuw wegprofiel gedraaid; de vijf punten komen mee in de kopie. Geen stadscentra.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Raglan concentrator (Katinniq) | Glencore | ~1,5 Mt erts/j → Ni-Cu-Co-concentraat | 39,9 kt Ni, 9,988 kt Cu, **0,822 kt Co** (2025) | [1][2] |
| Sudbury Smelter | Glencore Sudbury INO | concentraat (o.a. Raglan, ~240 kt/j) → matte | zie `kobalt-sudbury-kristiansand` §5; INO eigen kobalt 0,4 kt Co/j totaal (Sudbury + Raglan + Nikkelverk, andere basis) | [3][5] |

## 6 · Stoppunt
De brief stopt bij de Sudbury Smelter: Glencore noemt die zelf als bestemming van het Raglan-concentraat [3]; de matte-keten daarna (Sudbury → Québec → Nikkelverk) is al getekend in `kobalt-sudbury-kristiansand` en `nikkel-sudbury-kristiansand`. Fase D/E vervalt, geen tweede bron.

## 7 · Open punten
- **Kobaltcijfer**: 822 t Co (2025) staat op de Glencore-pagina als "production results" zonder te zeggen of het contained Co in concentraat of Co-metaal is [1]. Het verschilt van het INO-cijfer van 0,4 kt eigen kobaltmetaal (Sudbury + Raglan + Nikkelverk) in het productierapport [5]; waarschijnlijk contained versus gewonnen metaal, niet bevestigd. Eén peiljaar, niet gemiddeld. De lijn toont de fysieke route, niet dat al dit kobalt in Nikkelverk-kobalt terechtkomt.
- **Welke pier** in Deception Bay is Raglan's: noordpier gekozen (OSM-weg eindigt er); bronvermelding mét coördinaat ontbreekt. De zuidoostpier is vermoedelijk CRI/Nunavik Nickel [9].
- **Km b1** is deels bedrijfsopgave (100 km, afgerond, ook "afstand" zonder routebasis) en 95,9 is de OSM-ketensom; −4,1% ligt ruim binnen ±15%.
- **Zeekm**: Glencore noemt 2.600 km voor de zeereis [1]; de kopie meet 3.344,6 (aanloop + MARNET), +28,6%. De aanloop is schematisch (echte vaarlijn volgt de zuidoever van de Hudsonstraat) en MARNET kiest zijn eigen corridor; de afwijking is niet gerepareerd, wel gemeld. Geen ±15%-norm voor zee zonder gepubliceerde routelengte.
- **Aanloop b2a is schematisch** (rechte route over water, 119,8 km); het zeebeen begint op knoop 471.
- **Spoor is een kopie** met de twee bekende TERUGLOOP-omkeringen bij MacMillan Yard (`nikkel-sudbury-kristiansand` §9); geen eigen spoorrun.
- **Québec-kade** blijft aannemelijk (Glencore noemt geen kade).
- **Dubbeling**: geometrisch 100% gelijk aan `nikkel-raglan-sudbury`; op de bol liggen beide lijnen op elkaar (twee grondstofkleuren). Centraal beslissen of dat gewenst is; het kobaltverhaal is hier de zwakste claim van de keten (bijproduct, klein volume).

## 8 · Bronnen
[1] Glencore Canada, Raglan "our mining activity": 2025 productie 39.900 t Ni, 9.988 t Cu, **822 t Co**; 100 km per truck naar Deception Bay, opslag in een koepel, 2.600 km vaart naar Québec aan boord van de MV Arvik-1 (ijsbreker, 27.000 t). https://www.glencore.ca/en/raglan/what-we-do/our-mining-activity
[2] Glencore Canada, Raglan "At a glance": 39,9 kt Ni (2025), wegen naar de seaport. https://www.glencore.ca/en/raglan/who-we-are/at-a-glance
[3] Glencore Canada, "Facilities at Port of Quebec": concentraat Raglan via Deception Bay naar Québec, ~8 reizen/j, ~240.000 t, per spoor naar de smelter in Sudbury; terminal op door de haven verhuurd land. https://www.glencore.ca/en/our-assets/facilities-at-port-of-quebec
[4] Wikipedia, "Raglan Mine" (61.6875, -73.6781): ontwerp 130.000 t concentraat met o.a. 200 t Co; 100 km truck; haven 8 maanden bereikbaar met ijsbreker. https://en.wikipedia.org/wiki/Raglan_Mine
[5] Glencore, Full Year 2025 Production Report: INO kobaltmetaal 0,4 kt eigen bronnen, 3,0 kt totaal incl. third-party (via brief `kobalt-sudbury-kristiansand` [1]). https://www.glencore.com/.rest/api/v1/documents/static/a8114247-02e8-4bd8-bc04-81f411ba631c/GLEN_2025-FY-Production-Report.pdf
[6] Brief `nikkel-raglan-sudbury` (ankers, via-punten, bronnen [4]-[10], §9 bake): `v2/design/routebrieven/nikkel-raglan-sudbury.md`.
[7] Brief `kobalt-sudbury-kristiansand` (Québec- en Sudbury-anker, spoorkopie): `v2/design/routebrieven/kobalt-sudbury-kristiansand.md`.
[8] Glencore Raglan, Sivumut-ESIA-samenvatting 2017 (kaart Deception Bay: seaport, loading pipe, warehouse). https://minedocs.com/24/Reglan(Sivumut)-ProjectDescription-012017.pdf
[9] Federal Review Panel North, CRI/Nunavik Nickel Deception Bay, aanbevelingsrapport (bestaande Glencore-kade). https://www.canada.ca/content/dam/iaac-acei/documents/jbnqa/deception-bay/recommendation_report_frp-north.pdf
[10] OpenStreetMap (ODbL), ketens en ways via de bake van `nikkel-raglan-sudbury` (ways 1266330306 e.a., brief [7] daar). https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15, 2026-10-09), `v2/build-cache/satcheck/sat-kobalt-raglan-sudbury-*.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-kobalt-raglan-sudbury.json` (77,9 KB, versie 2, lonlat). **4.734,3 km · 7 benen · 4.071 punten · 6 markers.** Functie `bak_kobalt_raglan_sudbury` in `v2/tools/bak_stromen.sh` (LF, 0 CRLF), direct vóór de ankerregel; geen nieuw wegprofiel, geen nieuwe tool-run, geen slot-run buiten de bake.
**Recept:** letterlijke kopie van `bak_nikkel_raglan_sudbury`: dezelfde vier geojsons (`nikkel-raglan-sudbury-weg-…-osmketen`, `…-aanloop-deceptionbay`, drie `spoorroute-nikkel-raglan-sudbury-*`), hetzelfde zee `--been` 63.2000,-75.0000 → 46.8330,-71.2035 en dezelfde slot-`--stippel`. Gemeten: de punten van alle 7 benen zijn identiek aan die van `stroomroute-nikkel-raglan-sudbury.json`.
| # | modaliteit | km | punten | naad naar vorige | stippel |
|---|---|---|---|---|---|
| 1 | truck Raglan → Deception Bay | 95,9 | 644 | – | nee |
| 2 | zee haven-aanloop Deception Bay → knoop 471 | 119,8 | 108 | 0,00 | **ja** |
| 3 | zee knoop 471 → Québec (MARNET) | 3.224,8 | 331 | 0,00 | nee |
| 4 | spoor Québec → Taschereau | 286,9 | 595 | 1,51 | nee |
| 5 | spoor Taschereau → MacMillan | 541,0 | 993 | 0,00 | nee |
| 6 | spoor MacMillan → Sudbury | 465,7 | 1.398 | 0,00 | nee |
| 7 | spoor slot-emplacement → smelter | 0,2 | 2 | 0,00 | **ja** |
**Toets:** b1 95,9 tegen 100 (Glencore) = −4,1% (binnen ±15%); b3 spoor 1.293,6 tegen ~1.230 webcheck = +5,2%; zee 3.344,6 (aanloop + MARNET) tegen Glencore 2.600 = +28,6%, geen norm zonder gepubliceerde routelengte (aanloop schematisch). Grootste naad 1,51 km (zee-snap Québec-kade 1,62 km, onder de 5 km-norm; kade → spoor, procesgat in de havenkom). Markers 0,0–0,14 km van de lijn. `toets_knikken`: 5 knikken, 3 omkeringen, waarvan 2 TERUGLOOP (beide bij MacMillan Yard, bekend uit de bron-stroom; geen eigen reparatie, kopie). `toets_rechte_benen`: geen bevinding voor deze stroom.
**Stippel (2):** (b2) haven-aanloop, kade 118,3 km van MARNET-zeeknoop 471, "net reikt niet"; (b7) 0,16 km slot-emplacement naar de smelterdeur, "net reikt niet". "Aannemelijk: één bron" voor de Québec-kade staat in de beennaam van b3, niet in de lijnstijl.
**Lessen / open:** (1) de stroom is geometrisch 100% gelijk aan `nikkel-raglan-sudbury`: op de bol liggen beide lijnen op elkaar (kobaltkleur over nikkelkleur); centraal beslissen of de dubbeling gewenst is. (2) Kobaltcijfer (0,822 kt Co, contained of metaal) blijft onzeker, zie §7. (3) Bij een bake in dezelfde minuut als een edit van een andere agent in `bak_stromen.sh` gaf bash één keer `ga: command not found` (regel 9423, een halve edit van een ander, exit 127 na afloop van de functie); de stroomroute was dan al compleet geschreven en de syntaxis van het bestand is nu schoon.
