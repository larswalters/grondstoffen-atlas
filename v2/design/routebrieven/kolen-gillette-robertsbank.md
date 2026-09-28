# Kolen · Gillette (Wyoming, VS) → Montana-grensovergang → Roberts Bank, Delta (Canada)

**stroom-id:** `kolen-gillette-robertsbank` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken
**Keten in één zin:** Powder River Basin-thermische kolen per lange unit train (BNSF door Wyoming/Montana,
overdracht aan Canadese spoor bij de grens, dan CP/CN over de Robert's Bank Rail Corridor) naar Westshore
Terminals op de Roberts Bank Superport (Delta, BC) — de enige westkust-route voor Amerikaanse PRB-kolen naar
Azië, want geen VS-westkustterminal accepteert kolenexport. Geen zeebeen: geen bron noemt een specifieke
Aziatische eindkoper per lading, dus de brief stopt bij de exportkade.
**Welke as van het verhaal:** reserve-as van golf 2 (M31), gekozen om de enige westkust-uitgang voor
Amerikaanse thermische kolen te tonen. Westshore verscheept >20 Mt/jaar exportkolen, capaciteit ~29 Mt/jaar
sinds de upgrade van 2010 [2]; het PRB-aandeel daarin specifiek is niet gepubliceerd (§7).

## 1 · Ketenkaart
```
North Antelope Rochelle-mijn (PRB, Wyoming) `coal-gillette-narm-laad`
   ──(b1 spoor · BNSF Wyoming/Montana → grensovergang (aannemelijk: één bron) → CP/CN
       Robert's Bank Rail Corridor (BC) · ~2.200–2.500 km)──►
Westshore Terminals, Roberts Bank `coal-gillette-westshore-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `coal-gillette-narm-laad` → `coal-gillette-westshore-kade` | BNSF (Wyoming → Montana, aannemelijk: één bron) → grensovergang → CP/CN Robert's Bank Rail Corridor (BC) [2][3] | ~2.200–2.500 [schatting, geen gepubliceerde spoorlengte; hemelsbreed 1.497 km, geen wegkm] | toets_spoorroute (`BAKE_SUFFIX=-raw`) | nee |

Geen via-punten: er is geen gepubliceerde bron voor de exacte BNSF↔CP/CN-overdrachtsplaats in Montana, dus
er wordt geen corridorpunt verzonnen — de router zoekt de kortste weg over het 1-op-1-spoornet tussen de twee
ankers (§7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `coal-gillette-narm-laad` | mijn / laadspoor | North Antelope Rochelle Mine (Peabody Energy), Campbell County, Wyoming | 43.5589, -105.2883 | [1][4][5] | bron-gelegd (z15 gezien: mijncomplex met dagbouwputten, overslaghopen en een spoorlus/laadspoor direct bij het punt — zie `sat-kolen-gillette-robertsbank-narm.png`) |
| `coal-gillette-westshore-kade` | overslag spoor → zeeschip (losplek/exportterminal) | Westshore Terminals Coal Port, Roberts Bank, Delta, British Columbia | 49.0184, -123.1661 | [2][4][5] | bron-gelegd (z15 gezien: bulkkolenterminal met donkere stockpiles, laadinstallatie en scheepsligplaatsen aan de zuidkant van de pier, duidelijk gescheiden van de containerterminal (Deltaport) oostelijk ervan — zie `sat-kolen-gillette-robertsbank-westshore.png`) |

## 4 · Via-punten
Geen — zie §2 (geen gepubliceerde corridorkeuze om te pinnen; één doorgaande spoorcorridor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Westshore Terminals | Westar Group (Westshore Terminals Investment Corp.) | ongewassen thermische kolen (spoor) → bulklading (zeeschip) | >20 Mt/j export, capaciteit ~29 Mt/j sinds 2010-upgrade | [2] |

Geen bewerking: kolen wordt bij Westshore ongewassen overgeslagen van trein naar schip (opslag + laden), geen
raffinage-/verwerkingsstap.

## 6 · Stoppunt
De brief stopt bij de Westshore-kade: geen bron noemt een specifieke Aziatische eindkoper of -haven per
lading (fase D/E vervallen), en de originele ontwerp-as noemt dit zelf al expliciet als stoppunt.

## 7 · Open punten
- **De exacte BNSF↔CP/CN-overdrachtsplaats** in Montana (bv. Sweetgrass/Coutts of een andere grensovergang)
  is niet onafhankelijk gebrond — alleen de algemene claim "BNSF/CP-interchange door Montana" uit het eigen
  ontwerp-item. Geen via-punt verzonnen; de bak-agent laat de router de kortste weg over het 1-op-1-net vinden
  en meldt zelf of dat een plausibele lijn oplevert (geen omweg via een ver gelegen knoop).
- **Welke PRB-mijn** exact de Westshore-bound kolen levert is niet gebrond — Roberts Bank ontvangt kolen van
  meerdere PRB-producenten via gebundelde unit trains; North Antelope Rochelle (Peabody, 's werelds grootste
  kolenmijn) is als representatief anker gekozen op basis van het eigen ontwerp-item, niet op een bron die
  specifiek déze mijn aan déze kade koppelt (vandaar "aannemelijk: één bron" bij de beennaam).
- **Het PRB-aandeel in Westshore's totale doorvoer** (>20 Mt/j, capaciteit ~29 Mt/j) is niet apart gepubliceerd
  — een deel van Westshore's volume is Canadese metallurgische kolen uit British Columbia (Teck Resources).
- **Geen zeebeen getekend:** geen bron noemt een specifieke Aziatische eindkoper per lading (conform de
  ontwerp-as, die dit zelf al als stoppunt aanmerkt).
- **Recente context (niet in deze keten verwerkt):** Peabody's North Antelope Rochelle-mijn exporteert sinds
  september 2026 ook via een nieuwe Mexico-route (Union Pacific → Ferromex → Port of Guaymas, eerste lading
  naar Vietnam) — genoemd in de haalbaarheidstoets van dit item, geen aparte bron in deze ronde geraadpleegd
  (webbudget); kandidaat voor een aparte as bij een volgende golf.

## 8 · Bronnen
[1] Wikipedia, "North Antelope Rochelle Mine" — coördinaten 43.55889,-105.28833; 's werelds grootste kolenmijn, Peabody Energy, Campbell County WY, 85,3 Mt in 2019. https://en.wikipedia.org/wiki/North_Antelope_Rochelle_Mine
[2] Wikipedia, "Roberts Bank Superport" — Westshore Terminals als enige tenant sinds 1970, >20 Mt/j exportkolen, capaciteit 24→29 Mt/j na de upgrade van 2010, coördinaten 49.01944,-123.16056, "the Roberts Bank Superport is the only way for coal producers in the Powder River Basin to export coal to Asia" (VS-westkustterminals politiek geblokkeerd), Robert's Bank Rail Corridor bedient CN Rail/CP Rail/BNSF Railway. https://en.wikipedia.org/wiki/Roberts_Bank_Superport
[3] Wikipedia, "Powder River Basin" — gezamenlijke BNSF Railway/Union Pacific Railroad-spoorlijn door het zuidelijke PRB, 50–100 kolentreinen/dag (2016–2019). https://en.wikipedia.org/wiki/Powder_River_Basin
[4] OpenStreetMap/Nominatim (ODbL) — "Westshore Terminals Coal Port", Delta BC (49.0183716,-123.1660999); "Black Thunder Mine", Campbell County WY (alternatieve PRB-mijn, niet als anker gekozen). https://www.openstreetmap.org
[5] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-kolen-gillette-robertsbank-narm.png`, `sat-kolen-gillette-robertsbank-westshore.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Benen:** 2 (1 stippel + 1 gemeten) · **totaal 2.355,9 km** · 5.660 punten · 2 markers ·
bestand 110,4 KB.

| # | modaliteit | km | naad | stippel | naam |
|---|---|---|---|---|---|
| 1 | spoor | 6,3 | 0,00 km | ja | North Antelope Rochelle Mine — laadspoor/mijnaansluiting (geen net op deze korrel) |
| 2 | spoor | 2.349,6 | 0,00 km | nee | trein North Antelope Rochelle Mine → Westshore Terminals (BNSF Wyoming/Montana → grensovergang, aannemelijk: één bron → CP/CN Robert's Bank Rail Corridor) |

**Recept:**
```bash
BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=43.5589,-105.2883" \
  "--naar=49.0184,-123.1661" "--naam=kolen-gillette-robertsbank-narm-westshore" \
  --hoofd-km=1000 --max-snap=60 --keerstraf=25
bash v2/tools/bak_stromen.sh kolen-gillette-robertsbank
```
Functie `bak_kolen_gillette_robertsbank()` in `v2/tools/bak_stromen.sh`. Geen profiel nodig
(geen wegbeen in deze keten).

**Toelichting per stippel/aanloop/vlucht:**
- **b1 (stippel, spoor, 6,3 km):** het laadspoor/emplacement bij North Antelope Rochelle Mine
  is niet in OSM gekarteerd — de 1-op-1-router snapt 6,27 km van het punt op het hoofdnet
  (knoop 3441064). >2 km zonder duidelijke reden = korte stippel met reden, conform de
  bak-instructies; geen doorgetrokken lijn de dagbouwput in.
- **b2 (gemeten, spoor):** geen via-punten opgegeven (§2/§7 van de brief: geen gepubliceerde
  bron voor de exacte BNSF↔CP/CN-overdrachtsplaats in Montana). De kale 1-op-1-Dijkstra tussen
  de twee ankers gaf een plausibele lijn — géén Cerrejón-Cuba-precedent (geen omweg naar een
  ver gelegen component, verhouding route/grootcirkel 1,56, wat normaal is voor een
  spoorcorridor die niet in een rechte lijn ligt). Staart bij Westshore snapt 0,23 km —
  normale meting, geen stippel nodig.
- **Geen zeebeen, geen haven-aanloop:** de keten stopt bewust bij de Westshore-kade (brief §6)
  — geen bron noemt een Aziatische eindkoper per lading.
- **Geen lucht, geen binnenvaart, geen leiding:** niet van toepassing op deze keten.

**Km-toets:** gemeten 2.349,6 km (b2) tegen de brief-schatting ~2.200–2.500 km (hemelsbreed
1.497,2 km, geen gepubliceerde spoorlengte). De gemeten waarde valt **binnen** de
brief-schatting. Zoals de brief zelf al aangeeft (§2, geen gepubliceerde referentie): de
±15%-toets geldt hier als indicatie, niet als harde norm — in dit geval was hij niet nodig
omdat de brief-schatting zelf al klopte.

**Overige toetsen:** `toets_knikken.py` → 0 knikken ≥60°, 0 omkeringen, 0 terugloop.
`toets_rechte_benen.py --min-km 5` → been 1 (stippel, 6,3 km) heeft omwegfactor 1,006
(bijna recht) — verwacht en correct voor een stippel, geen bevinding. JSON: `versie` 2,
`punt_formaat` `lonlat`, beide benen modaliteit `spoor`, elk been ≥2 punten, laadt zonder
fouten.

**Lessen / bevindingen:**
- De eerdere claim dat `us-montana` als extract ontbreekt was inderdaad feitelijk onjuist
  (bevestigd: `v2/build-cache/raw1op1/us-montana.geojson` stond al op schijf, net als
  `us-wyoming` en `canada`). Geen centraal werk nodig geweest aan `fetch_landnet.py`.
- Deze keten is de eerste kolen-as VS→Canada; geen overlap met de negen bestaande
  kolen-stromen, dus geen gedeeld been nodig.
