# Routebrief (licht) · kolen — Elkview-mijn (Elk Valley, Canada) → Neptune Terminals, North Vancouver (Canada)

**stroom-id:** `kolen-elkview-neptune` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** metallurgische cokeskool van de Elkview-mijn (Elk Valley, BC) gaat per lange
unit train over het CPKC-net door British Columbia naar Neptune Terminals in North Vancouver — de
tweede, complementaire Canadese westkust-exportroute naast `kolen-gillette-robertsbank` (andere mijn,
andere spoorcorridor zonder grensovergang, andere kade, ~15–20 km verderop in dezelfde haven-regio).
**Welke as van het verhaal:** cokeskool (i.p.v. thermische kolen) rechtstreeks uit Canada naar
Aziatisch staal. Elkview-mijn ~9,0 Mt/jaar (Wood Mackenzie/mediaschatting 2024, `kolen-sitelaag.json`,
anker `w-elkview`); Neptune Terminals verwerkte in 2023 **59 %** van Teck's totale steenkoolverkoop-
volume via Teck's **46 %-belang** en is sinds september 2021 Teck's **primaire** cokeskoolexport-
terminal met exclusieve kolencapaciteit voor die divisie (Teck Resources Form 40-F, SEC-jaarverslag) —
sterker gebrond dan het ontwerp zelf aangaf.

## 1 · Ketenkaart
```
Elkview-mijn, Elk Valley (Elk Valley Resources — Glencore 77 %/Nippon Steel 20 %/POSCO 3 %), BC
`kolen-elkview-laad`
   ──(b1 spoor · CPKC (voorheen CP Rail), corridor door British Columbia, exacte lijnkeuze niet
       gepubliceerd · ~592 km hemelsbreed, indicatief 950–1.100 km werkelijke spoorlengte, geen
       gepubliceerde spoorkm)──►
Neptune Terminals, North Vancouver `kolen-neptune-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-elkview-laad` → `kolen-neptune-kade` | CPKC door British Columbia (geen gepubliceerde exacte lijnkeuze; ontwerp noemt Crowsnest-lijn → Thompson-/Fraser Canyon, niet onafhankelijk bevestigd) [3] | ~592 [hemelsbreed, geen wegkm/spoorkm gepubliceerd; indicatief 950–1.100 km werkelijke CPKC-route, niet bevestigd — de ±15 %-toets is hier dus geen norm, alleen een indicatie] | toets_spoorroute (`BAKE_SUFFIX=-raw`) | nee |

Geen via-punten: er is geen gepubliceerde bron voor de exacte CPKC-lijnkeuze door British Columbia
(Crowsnest Pass vs. een andere route naar de Kamloops/Fraser Canyon-hoofdlijn), dus wordt er geen
corridorpunt verzonnen — zie §7 voor bak-aanwijzingen als de kale Dijkstra een implausibele omweg geeft.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-elkview-laad` | mijn / laadspoor | Elkview-mijn (Elk Valley Resources — Glencore 77 %/Nippon Steel 20 %/POSCO 3 %), Elk Valley, British Columbia | 49.7522, -114.8772 | [1][2] | bron-gelegd (z15 gezien: actieve dagbouwmijn met zwarte kolenstockpiles/terrassen, een pitmeer/afvalbekken direct zuidelijk en een spoorlus/laadspoor direct ten oosten van het punt, langs de rivier bij Sparwood — coördinaat hergebruikt uit `kolen-sitelaag.json` (anker `w-elkview`), in deze ronde zelf satelliet-gecheckt: `v2/build-cache/satcheck/sat-kolen-elkview-neptune-elkview.png`) |
| `kolen-neptune-kade` | overslag spoor → zeeschip (losplek/exportterminal) | Neptune Terminals, North Vancouver (Teck 46 %-belang; steenkolen + potas) | 49.3054, -123.0506 | [4][5][6] | bron-gelegd (z15 gezien: bulkterminal met zwarte kolenstockpiles direct aan het spoor, laadinstallatie en meerdere scheepsligplaatsen aan de waterkant, duidelijk gescheiden van de aangrenzende stadswijk/rangeerterrein — coördinaat onafhankelijk bevestigd door OSM Nominatim-reverse ("Neptune Terminals", industrial landuse, Moodyville, North Vancouver) en dit sat_check-beeld: `v2/build-cache/satcheck/sat-kolen-elkview-neptune-neptune.png`) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen — zie §2. Er is geen gepubliceerde bron die één specifieke CPKC-doorgaande lijn (Crowsnest Pass
vs. een noordelijkere corridor via Golden) tussen Elkview en Neptune aanwijst.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Neptune Terminals | Teck Resources (46 %-belang; cost-of-service shiploading) | cokeskool (spoor) → bulklading (zeeschip) | 59 % van Teck's steenkoolverkoopvolume in 2023; primaire terminal sinds 2021, kolencapaciteit exclusief voor Teck's Steelmaking Coal Operations | [5] |

Geen bewerking: cokeskool wordt bij Neptune ongewassen overgeslagen van trein naar schip (opslag +
laden), geen raffinage-/verwerkingsstap.

## 6 · Stoppunt
De brief stopt bij de Neptune-kade (conform het ontwerp, expliciet als STOPPUNT gemarkeerd): Teck's
steelmaking-coal-export via Neptune gaat overwegend naar de Asia-Pacific-regio (China, India, Japan,
Korea), zonder onderverdeling naar één specifieke afnemer of haven per lading — dezelfde reden waarom
`kolen-gillette-robertsbank` (andere mijn, andere corridor, andere kade ~15–20 km verderop op Roberts
Bank) daar ook stopt.

## 7 · Open punten
- **De exacte CPKC-lijnkeuze door British Columbia** (Crowsnest Pass-corridor vs. een route via Golden
  naar de Kamloops/Thompson-/Fraser Canyon-hoofdlijn) is niet onafhankelijk gebrond — alleen de
  algemene claim uit het eigen ontwerp-item. Geen via-punt verzonnen. **Bak-aanwijzing:** draai eerst
  één kale run tussen de twee ankers; geeft die een plausibele lijn (verhouding gemeten/hemelsbreed in
  de orde van de indicatieve 950–1.100 km, geen omweg naar een ver gelegen component), gebruik die.
  Geeft de Dijkstra een implausibele omweg, dan zijn `Sparwood-emplacement` (49.7333, -114.8858) en/of
  de doorgang bij `Crowsnest Pass` (49.6409, -114.6710) mogelijke correctiepunten voor een gesplitste
  run (kop→punt, punt→staart) — géén bevestigde via-punten, alleen kandidaat-coördinaten voor de bake.
- **Rail-km is alleen hemelsbreed te onderbouwen** (~592 km) tegen een geschatte werkelijke CPKC-route
  van 950–1.100 km (niet bevestigd) — geen gepubliceerde spoorlengte gevonden binnen het webbudget; de
  ±15 %-toets geldt hier dus als indicatie, niet als harde norm (zoals het ontwerp zelf al aangaf).
- **Bestaande fout in andermans bestand (niet hier gewijzigd):** de notitie bij anker `w-elkview` in
  `v2/design/kolen-sitelaag.json` ("per spoor naar Westshore/Ridley → Aziatisch staal") is verouderd en
  spreekt deze keten tegen. Diezelfde entry noemt het eigenaarschap onvolledig ("Glencore, sinds juli
  2024; voorheen Teck Coal"). **Correctie voor het rapport:** Elkview is sinds de Glencore-acquisitie
  van Teck's steelmaking-coal-business eigendom van **Glencore 77 % / Nippon Steel 20 % / POSCO 3 %**
  (Wikipedia "Elkview coal mine", 2024) — **niet** "Glencore 77 %/Teck 23 %" zoals het ontwerp-item
  stelde; Teck houdt zelf geen belang meer in de mijn. Niet gewijzigd in `kolen-sitelaag.json` (eigen-
  bestanden-regel) — gemeld voor centrale correctie.
- **Coördinaat Elkview-mijn** komt uit `kolen-sitelaag.json`, onafhankelijk bevestigd via Wikipedia's
  infobox-coördinaat (49.752273, -114.877327 — 4 decimalen identiek) en een eigen satellietblik.
- **Geen zeebeen getekend:** conform de ontwerp-as en §6 stopt de keten bewust bij de Neptune-kade.

## 8 · Bronnen
[1] Wikipedia, "Elkview coal mine" — coördinaten 49.752273,-114.877327; eigendom Glencore 77,0 %/
Nippon Steel 20,0 %/POSCO 3,0 % (stand 2024); capaciteit 4,19 Mt/jaar volgens een dataset uit 2012
("Coal in British Columbia", mining.bc.ca) — deze capaciteit is verouderd tegenover de recentere
~9,0 Mt/jaar-schatting in [2]. https://en.wikipedia.org/wiki/Elkview_coal_mine
[2] `v2/design/kolen-sitelaag.json`, anker `w-elkview` — Elkview 49.7522,-114.8772, ~9,0 Mt/jaar
(Wood Mackenzie/mediaschatting 2024, Baldy Ridge Extension-project), status aannemelijk, coördinaatbron
Wikipedia-geohack "Elkview coal mine".
[3] Glencore, persbericht "Acquisition of a 77 percent interest in Teck's steelmaking coal business for
US$6.93 bn" — bevestigt de Glencore-overname van Teck's steelmaking-coal-divisie (Elk Valley Resources).
https://www.glencore.com/media-and-insights/news/acquisition-of-a-77-percent-interest-in-tecks-steelmaking-coal-business-for-USd6-93-bn
[4] OpenStreetMap/Nominatim (ODbL) — "Neptune Terminals" (industrial landuse, way/564571990),
49.3054214,-123.0506419, "Neptune Terminals, 1001, Moodyville, North Vancouver, Metro Vancouver
Regional District, British Columbia, Canada" — reverse-geocode bevestigt de locatie. https://www.openstreetmap.org
[5] Teck Resources Ltd, Form 40-F (jaarverslag, SEC EDGAR), MD&A-bijlage — "Neptune became our primary
terminal in 2021"; "46 % ownership interest in Neptune"; "Neptune handled 59 % of our sales volumes in
2023"; "coal capacity at Neptune is exclusive to [Teck's Steelmaking Coal Operations]"; afzetmarkten
overwegend Asia-Pacific, aanvullend Europa/Amerika's.
https://www.sec.gov/Archives/edgar/data/886986/000088698624000003/teck-20231231xexx993mda.htm
[6] Neptune Terminals, eigen website — "Connecting Canadian commodities to world markets from the
North Shore for more than 50 years"; verscheept "steelmaking coal, potash and other terminal assets".
https://www.neptuneterminals.com/
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-kolen-elkview-neptune-elkview.png`,
`v2/build-cache/satcheck/sat-kolen-elkview-neptune-neptune.png`.

## 9 · Bakresultaat (2026-09-28, lichte werkwijze, M31 golf 6)

**Eén been, doorgetrokken, geen stippel.** Kale kop→staart-run over het 1-op-1-spoornet
(`BAKE_SUFFIX=-raw`, extract `canada` uit `raw1op1`, al aanwezig):

```
BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=49.7522,-114.8772" \
  "--naar=49.3054,-123.0506" "--naam=kolen-elkview-neptune-elkview-neptune" \
  --hoofd-km=1000 --max-snap=60 --keerstraf=25
```

Console: `3260717 spoor-edges` (bevestigt het 1-op-1-net, geen tekennet) · snap Elkview
0,04 km / snap Neptune 0,18 km, beide op de grootste component (392.614 km — hetzelfde
hoofdnetwerk aan beide kanten) · 7 spike-punten opgeruimd (OSM-zigzag, geen bocht) ·
**0 bochten ≥60° na de keerstraf** · **route 1.108,8 km over 914 edges** (kale meting,
vóór het hechten aan de zeenet-graaf in de bake) → **1.114,6 km / 3.692 punten** in het
gebakken bestand (klein verschil door de vecto­risatie van `hecht_marnet.py route`).

**Km-toets (indicatief, zoals de brief zelf al aangeeft):**
- Tegen de hemelsbrede 591,7 km: verhouding **1,88** (route/hemelsbreed) — plausibel voor
  een spoorlijn door de Rocky Mountains/Coast Mountains (geen rechte corridor).
- Tegen de indicatieve werkelijke CPKC-lengte van 950–1.100 km (brief §2/§7, niet
  bevestigd): **1.108,8–1.114,6 km ligt net iets bóven de bovenkant van die indicatie**
  (+1–1,3%). Geen gepubliceerde spoorkm gevonden binnen het webbudget, dus de ±15%-toets
  geldt hier niet als harde norm — de uitkomst is in dezelfde orde als de indicatie en
  wordt niet als afwijking gerapporteerd, conform de brief.
- De kale run gaf **0 bochten ≥60° na de keerstraf** en geen implausibele omweg naar een
  ver gelegen component → de kandidaat-junctiepunten uit §7 (Sparwood-emplacement,
  Crowsnest Pass) waren niet nodig; de enkele run is gebruikt zoals hij uit de router
  kwam.

**Naden:** 0,00 km (één been, geen aansluitend been). **Markers:** beide binnen 0,2 km
van hun eigen been-uiteinde (anker = routeerpunt op dit korrelniveau).

**Toets_knikken:** 0 knikken ≥60°, 0 omkeringen (incl. 0 terugloop) — een schone lijn.
**Toets_rechte_benen:** het been staat niet in de "rechte lijn ≥5 km"-verdachtenlijst
(1.114,6 km over 3.692 punten, geen enkelvoudige koorde) — verwacht voor een geroutete
spoorlijn, geen bevinding.
**Contract:** `versie: 2`, `punt_formaat: "lonlat"`, modaliteit `spoor` (geldig), 1 been
met 3.692 punten (≥2), bestand 72,2 KB (ruim onder de ~300 KB-norm).

**Lessen / bevindingen:**
- Geen via-punten nodig gebleken: de kale Dijkstra over het 1-op-1-net koos zelf een
  plausibele lijn binnen de indicatieve lengte-orde, zonder omweg naar een ver component
  (de Cerrejón-Cuba-klasse trad niet op).
- Complementair aan `kolen-gillette-robertsbank` bevestigd: geen been-overlap, geen
  gedeelde geometrie — andere mijn (Elkview vs. North Antelope Rochelle), andere
  spoorcorridor (CPKC door BC zonder grensovergang vs. BNSF Wyoming/Montana → grens →
  CP/CN Robert's Bank Rail Corridor), andere kade (Neptune Terminals North Vancouver vs.
  Westshore Terminals Roberts Bank, ~15–20 km verderop in dezelfde havenregio).
- Openstaande punten uit §7 (exacte CPKC-lijnkeuze, ontbrekende gepubliceerde spoorkm,
  de eigenaarschapscorrectie op `w-elkview` in `kolen-sitelaag.json`) blijven ongewijzigd
  open — niet hier opgelost, gemeld voor centrale correctie.
