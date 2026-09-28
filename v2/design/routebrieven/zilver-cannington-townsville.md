# Zilver · Van → Via → Naar (land)

**stroom-id:** `zilver-cannington-townsville` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** lood/zilverconcentraat van de Cannington-mijn (South32, Queensland) per **roadtrain** (Linfox, 180 km, 24/7) naar de Yurbi rail-overslagfacility bij Cloncurry, dan per **spoor** (Great Northern Railway / Mount Isa-lijn) naar de kade van Townsville — bewust **stoppunt** bij de haven, geen gedocumenteerde overzeese smelter-bestemming.
**Welke as van het verhaal:** Cannington is 's werelds grootste zilver- en loodmijn (~3,3 Mt erts/j); > 500.000 t concentraat/jaar gaat over deze roadtrain-route naar Yurbi (South32 / Industry Queensland, recent, geen peiljaar). Prioriteit 4 van M31 golf 2.

## 1 · Ketenkaart
```
Cannington-mill `ag-cannington-mill` ──(b1 truck · roadtrain Cannington–Cloncurry via McKinlay (Linfox, 24/7) · 180 km)──► Yurbi-overslag `ag-yurbi-overslag`
   ──(b2 spoor · Great Northern Railway / Mount Isa-spoorlijn · spoorrouter meet)──► Haven van Townsville, Berth 11 `ag-townsville-haven` (South32-concentraatlader) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Cannington-mill → Yurbi-overslag | roadtrain-route Cannington–Cloncurry via McKinlay (Linfox, 24/7-operatie) | 180 [1][2] | maak_stroombeen_weg (extract `australie`) | nee |
| b2 | A | spoor | Yurbi-overslag → Townsville-haven (Berth 11) | Great Northern Railway / Mount Isa-spoorlijn | geen gepubliceerde deellengte voor dit traject — spoorrouter meet het | toets_spoorroute (`BAKE_SUFFIX=-raw`, extract `australie`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-cannington-mill` | mijn / verwerkingsfabriek (kop van b1) | Cannington-mijn en verwerkingsfabriek (South32) | -21.8595, 140.9155 | [1][8] | bron-gelegd (z17 gezien: verwerkingsfabriek met conveyors, tanks en gebouwen, tailingsdammen ernaast, open pit ~400 m zuidelijker met een headframe/schacht) |
| `ag-yurbi-overslag` | overslag truck → spoor | Yurbi rail-overslagfacility, 15 km oost van Cloncurry | -20.7389, 140.6557 | [3][6][8] | bron-gelegd (z15 gezien: kleine industriële faciliteit met opslagloods/stockpile aan een spoorzijspoor naast de Landsborough Highway) |
| `ag-townsville-haven` | losplek spoor / laadplek zee (stoppunt) | Haven van Townsville, Berth 11 (South32-concentraatlader) | -19.2441, 146.8358 | [4][5][8] | bron-gelegd (z19 gezien: geïsoleerde jetty aan de havenmond met een laadplatform/laderstructuur, duidelijk anders dan de eenvoudige enkelpunts-meerboei van Berth 1 ernaast; volgens de officiële berth-tabel is dit de dedicated South32-concentraatlader) |

## 4 · Via-punten (alleen b1 — de enige landbeen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | McKinlay (aansluiting mijntoegangsweg → Landsborough Highway) | -21.2713, 141.2902 | Wikipedia: "the mine site is serviced by road from McKinlay" — hier verlaat de roadtrain de mijnweg en gaat de doorgaande Landsborough Highway op [1][7] |
| b1 | 2 | Cloncurry (Landsborough Highway passeert de stad, corridor buigt oostwaarts naar Yurbi) | -20.7047, 140.5053 | de route loopt via/langs Cloncurry voordat de laatste ~15 km oostwaarts naar Yurbi volgt [2][3][7] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| — | — | — | — | geen tussenliggende verwerkingsknoop: het erts wordt al op de mijn (Cannington-mill) tot lood/zilverconcentraat verwerkt; er is geen smelter of raffinaderij in deze keten getekend |

## 6 · Stoppunt
De brief stopt bewust bij de kade van Townsville (Berth 11): geen enkele bron noemt een specifieke overzeese smelter-bestemming ("loaded onto ships for export to customers around the world" is het meest concrete dat gevonden is) — de lijn eindigt waar het bewijs eindigt, conform de regel dat een haven-eindpunt geen smelter-gok is.

## 7 · Open punten
- Geen gepubliceerde deellengte voor het spoorbeen Yurbi→Townsville (Great Northern Railway / Mount Isa-lijn); de spoorrouter meet de werkelijke lengte tijdens het bakken.
- De identificatie van `ag-townsville-haven` als **Berth 11** (i.p.v. het ernaast liggende Berth 1) berust op de officiële berth-tabel (South32/concentraten/scheepslader) gecombineerd met het satellietbeeld (laderstructuur vs. enkelvoudige meerboei voor vloeibare bulk) — geen naam-tag op de kaart zelf bevestigt dit direct.
- De exacte naam/het wegnummer van de mijntoegangsweg Cannington→McKinlay is niet gevonden (Overpass onbereikbaar tijdens dit onderzoek); de corridor steunt op Wikipedia's aanwijzing "serviced by road from McKinlay" + de gepubliceerde 180 km totaal.
- Geen bron noemt een specifieke overzeese smelter-bestemming vanaf Townsville — vandaar het bewuste stoppunt in §6.
- MARNET-zeeknoopcheck uit de haalbaarheidstoets (niet getekend, buiten scope): Townsville-kade ligt 4,2 km van de dichtstbijzijnde zeeknoop, ruim onder de 5 km-grens van de haven-aanloop-regel (LAR-586) — relevant pas als deze keten later met een zeebeen wordt doorgetrokken.
- South32 target voor mijnlevensduur-extensie tot minstens 2032 (Wikipedia, bevestigd bij de haalbaarheidstoets) — geen sluitingsrisico op korte termijn, niet verder onderzocht.

## 8 · Bronnen
[1] Wikipedia, "Cannington Mine" — coördinaat (-21.8564, 140.907, deposit/tailings), eigendom South32 sinds 19-08-2014 (BHP-afsplitsing), "serviced by road from McKinlay", productiegeschiedenis, mine-life-extensie tot ≥2032. https://en.wikipedia.org/wiki/Cannington_Mine
[2] Industry Queensland, "Road trip with a difference" — Linfox-roadtrainroute Cannington→Yurbi, 180 km, 24/7-operatie, 5 quad-roadtrains, > 500.000 t concentraat/jaar. https://industryqld.com.au/road-trip-with-a-difference/
[3] Queensland Government, ministerial statement 28-11-1997 (nr. 1026) — Yurbi "2,5 km balloon loop" op de Mount Isa–Townsville-spoorlijn; "McIver brings the product from the Cannington mine in impressive road trains to Yurbi, where it's transferred for Queensland Rail haulage to Townsville"; 1997-productiecijfers (1,5 Mt erts, 375 kt concentraat). https://statements.qld.gov.au/statements/1026
[4] Wikipedia, "Port of Townsville" — "In 1997, BHP built Berth 11 to handle mineral concentrates from the Cannington Mine"; haven is nr. 1 van Australië voor export van koper/zink/lood; algemene havencoördinaat -19,24910/146,83661. https://en.wikipedia.org/wiki/Port_of_Townsville
[5] Port of Townsville, officiële berth-informatie (PDF) — Berth 11: operator South32, cargo "Concentrates", faciliteit "Ship loader", geen bunkerbrandstof, berth pocket 240 m, max. vessel LOA 225 m, design depth 12,2 m LAT; Berth 2 (Glencore, ander concentraat) ter vergelijking. https://s3-ap-southeast-2.amazonaws.com/os-data-2/port-townsville/documents/berth_information_website_final.pdf
[6] OpenStreetMap (ODbL) via Photon — landuse "Yurbi Rail Loading Facility" (-20,7389/140,6557) + knoop "Yurbi" (railway=yard, -20,7396/140,6535), Landsborough Highway, Cloncurry. https://www.openstreetmap.org
[7] Wikipedia — coördinaten McKinlay (-21,2713/141,2902) en Cloncurry (-20,7047/140,5053), gebruikt als via-punten op de Landsborough Highway-corridor. https://en.wikipedia.org/wiki/McKinlay,_Queensland · https://en.wikipedia.org/wiki/Cloncurry,_Queensland
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15–z19, live) — `v2/build-cache/satcheck/sat-zilver-cannington-townsville-mijn-zoom.png` (z17, mill+pit) · `sat-zilver-cannington-townsville-yurbi.png` (z15, overslagfacility) · `sat-zilver-cannington-townsville-jetty-detail.png` + `sat-zilver-cannington-townsville-loader.png` (z19, Townsville-jetty's).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `zilver-cannington-townsville`** → `v2/data/stroomroute-zilver-cannington-townsville.json` — 2 benen,
**946,8 km**, 1.820 punten, 3 markers. truck 181,2 km + spoor 765,6 km. Recept: `bak_stromen.sh` (functie
`bak_zilver_cannington_townsville`).

**b1 (truck, roadtrain Cannington-mill → McKinlay → Cloncurry → Yurbi-overslag):**
`maak_stroombeen_weg.py --profiel zilver-cannington-townsville-mill-yurbi --bron geofabrik` (extract `australie`).
Niet-monotone lijn (mijn → McKinlay noordoostwaarts, dan terug naar Cloncurry noordwestwaarts, dan oostwaarts
naar Yurbi) met `vensterKm: 55` — geen omweg/lus-afkeuring, de knik bij McKinlay is een echte corridorkeuze.
⚠️ Twee scans faalden op `"geen wegpad tussen punt 2 en 3"` (Cloncurry → Yurbi): eerst `WEG_HOUD` kaal, toen met
`corridorKlassen: [tertiary, unclassified]` — pas met `eindKlassen` verruimd naar `[residential, service,
tertiary, unclassified, track]` + `eindToegangPrivaat: True` routeerde de scanner door (Yurbi is een private
rail-overslagfacility met een toegangsweg op een kleinere klasse dan de standaard-eindzone dekt; een
verhard/berijdbaar tracé is aannemelijk voor een bemande, dagelijkse 24/7-roadtrainroute). Resultaat **181,2 km
tegen gepubliceerd 180 km (Industry Queensland + Qld-ministerieel statement) = +0,7%, ruim binnen ±15%**. Vier
keerlussen gesnoeid (210,1 → 181,1 km) — dubbel-gereden stukjes bij Cloncurry, geen route-artefact in de
lengtetoets zelf.

**b2 (spoor, 1-op-1-net, console bevestigt "3260717 spoor-edges", `BAKE_SUFFIX=-raw`):**
`node v2/tools/toets_spoorroute.mjs --van=-20.7389,140.6557 --naar=-19.2441,146.8358
--naam=zilver-cannington-townsville-yurbi-townsville` (extract `australie`, geen via-punt, enkelvoudige lijn
zonder corridorkeuze). **765,6 km over 551 edges, grootcirkel 666,8 km, verhouding 1,15.** Geen gepubliceerde
deellengte om tegen te toetsen (brief §7) — dit is nieuwe informatie. Twee spike-punten opgeruimd (OSM-zigzag,
knik >60° maar <25 m uit de lijn), **0 bochten ≥60° na de keerstraf (25 km)**.

**Toets naden:** b1 → b2 (truck → spoor, bij Yurbi): **0,22 km** — de truck-lijn eindigt exact op het
Yurbi-marker-anker, de spoorrouter snapt zijn kopeinde op een apart hoofdnet-knooppunt 0,22 km verderop; ruim
binnen de ≤5 km-norm (bakhandleiding §5), geen haven-aanloop-achtige tussenstap nodig.

**`toets_knikken.py`:** 8 knikken ≥60° op het truckbeen, waarvan **1 omkering** (180,0° bij McKinlay,
-21,27068/141,28995, straal ~0 m, door het tool zelf als *"scherpe bocht, echt"* geclassificeerd — verhouding
pad/hemelsbreed 1,5, dus geen terugloop) — precies de bewust niet-monotone knik uit het ontwerp (§ opdracht
hierboven), **0 terugloop**. Zeven overige knikken zijn spikes (OSM-zigzags <90 m straal) rond McKinlay en Yurbi
— kopmaak/zijweg-precisie op de eindzones, geen fout. Het spoorbeen: **0 knikken, 0 omkeringen**.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, spoor} (binnen de toegestane
set), elk been ≥2 punten (minimum 646), bestandsgrootte **37,4 KB** (ruim < 300 KB-richtwaarde).

**Markers:** ag-cannington-mill 0 m (exacte kop van b1) · ag-yurbi-overslag 0 m tegen de staart van b1 (de 0,22
km-naad hierboven zit tussen b1-staart en b2-kop, niet tegen de marker zelf) · **ag-townsville-haven ~230 m**
(anker ≠ routeerpunt — het spoorbeen snapt op zijn dichtstbijzijnde hoofdnet-knoop 40669, 0,23 km van de
Berth-11-kade-anker; de spoorrouter-console bevestigt dezelfde 0,23 km). Alle drie ruim binnen de ~0,5 km-norm.

**Geen haven-aanloop, geen zeebeen:** de keten stopt bij de kade van Townsville (§6, bewust stoppunt — geen bron
noemt een overzeese smelterbestemming). Voor het archief blijft staan wat de bak-aanwijzing al meegaf: de
haalbaarheidstoets vond de Townsville-zeeknoop op 4,2 km van de kade (< 5 km-grens, LAR-586) — bij een latere
doortrekking met een zeebeen is dus geen haven-aanloop nodig.

**Open punten die blijven staan (zie ook §7):** geen gepubliceerde deellengte voor b2 (nu vervangen door de
gemeten 765,6 km); de Berth-11-identificatie en de mijntoegangsweg-naam blijven zoals in §7 beschreven — niet
verder onderzocht binnen deze lichte bake.

**Gereedschapslessen:**
- `"geen wegpad tussen punt X en Y"` op een kort eindstuk (hier 15 km, Cloncurry → Yurbi) hoeft geen ontbrekende
  corridor te betekenen — het kan de laatste meters naar een private overslagfacility zijn die op een kleinere
  wegklasse ligt dan de standaard-eindzone (residential/service/tertiary/unclassified) dekt. `eindKlassen` met
  `track` erbij + `eindToegangPrivaat: True` loste dit op zonder te stippelen, conform de bak-aanwijzing dat een
  bemande 24/7-roadtrainroute een verhard tracé aannemelijk maakt.
- Een niet-monotone wegcorridor (mijn → via1 → terug richting via2 in een andere richting) routeert prima door
  `maak_stroombeen_weg.py` zolang `vensterKm` ruim genoeg is om de hele anker→via→via→anker-lijn (niet de
  grootcirkel) te dekken — hier volstond 55 km voor een been van 181 km met een knik van ~100 km per stuk.
  `toets_knikken.py` bevestigt zelf dat zo'n knik een "echte" bocht is (verhouding pad/hemelsbreed >1) en geen
  terugloop, dus de bewuste niet-monotone opzet is ook objectief te onderscheiden van een routeerfout.
