# Routebrief (licht) · Kolen · Goonyella Riverside → Hay Point → Dhamra → Kalinganagar (India)

**stroom-id:** `kolen-goonyella-kalinganagar` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** cokeskool (metallurgisch) per **spoor** ~199 km van het Goonyella Riverside-laadstation (BMA =
BHP/Mitsubishi, aannemelijk: blend uit vijf mijnen) via de junctie Coppabella naar Hay Point Coal Terminal, per
**Capesize-zeeschip** ~9.500–10.500 km over de Koraalzee en de Golf van Bengalen naar Dhamra Port (Adani, Odisha),
per **spoor** ~114 km via Bhadrak en Jakhapura naar de cokerij/hoogovens van Tata Steel Kalinganagar — stoppunt.
**Welke as van het verhaal:** *Zeehandel cokeskool Australië → India* — Bowen Basin is de grootste cokeskool-
exporteur ter wereld, India de grootste importeur (56,9 Mt in 2024, waarvan 25,8 Mt Australisch [1]); Dhamra
ontving in 2025 een recordlading van 165.283 t cokeskool "uit Queensland" voor Tata Steel [2][3]. Kalinganagar
fase II (blast furnace 2, 5.870 m³) is in 2024/2025 ingehuldigd, 3 → 8 Mt staal/j [4][5].

## 1 · Ketenkaart
```
Goonyella Riverside-laadstation `kolen-goonyella-laad` (aannemelijk: blend uit 5 BMA-mijnen)
   ──(b1 spoor · Goonyella-systeem via Coppabella · ~199 km)──► Hay Point Coal Terminal `kolen-haypoint-kade`
   ──(b2 zee · Koraalzee → Golf van Bengalen · ~9.500–10.500 km, MARNET + haven-aanloop)──► Dhamra Port `kolen-dhamra-losplaats`
   ──(b3 spoor · Dhamra-Bhadrak-lijn → Howrah-Chennai-hoofdlijn → Daitari-Jakhapura-lijn · ~114 km)──► Tata Steel
     Kalinganagar cokerij/hoogovens `kolen-kalinganagar-cokerij` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Goonyella Riverside laadstation → Hay Point Coal Terminal | Goonyella-spoorsysteem (Aurizon, geëlektrificeerd) via junctie Coppabella (GAP-lijn naar Abbot Point uitsluiten) en de HPCT/DBCT-terminalsplitsing | 199,0 (gemeten, 1-op-1-net) [7][8] | toets_spoorroute (australie.geojson) | nee — loadout-spur en HPCT-kade-aansluiting (~1,2 km) blijven korte stippels |
| b2 | B | zee | Hay Point Coal Terminal (BMA-kade, verkoop aan GIP aangekondigd 2025) → Dhamra Port losligplaats | Koraalzee → noord-om-PNG of Torres-straat (diepgangkeuze, MARNET kent geen diepgang) → Golf van Bengalen | ~9.500–10.500 (afgeleid; geen operator-cijfer) | MARNET; Dhamra ligt 109,5 km van de dichtstbijzijnde zeeknoop → haven-aanloop | aanloop: ja, ~110 km (Dhamra staat niet in ports.json) |
| b3 | C | spoor | Dhamra Port losplaats → Tata Steel Kalinganagar (cokerij/hoogovens) | Dhamra–Bhadrak-lijn (62 km, 2011) → Howrah–Chennai-hoofdlijn zuid → Jakhapura → Daitari–Jakhapura-lijn / Tata-siding | 114,2 (gemeten: 65,4 + 48,8) tegen ~140 EC-rapport (−18%, ruwe ankers) [9][10] | toets_spoorroute (india.geojson); via-punten Bhadrak + Jakhapura pinnen de corridor | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-goonyella-laad` | mijn / laadstation | Goonyella Riverside train loadout (BMA = BHP/Mitsubishi 50:50), 30 km N van Moranbah | -21.7923, 147.9620 | [6][7] | bron-gelegd (z15 gezien: open dagbouwput met teal-gekleurd waswater, afvalbergen, kolenstockpiles en een laad-/verwerkingscomplex direct naast een haulroad — punt ligt op de rand van de stockpile bij het laadstation) |
| `kolen-haypoint-kade` | overslag zee (BMA-kade, verkoop aan GIP aangekondigd 2025) | Hay Point Coal Terminal, offshore trestle + 2 berths | -21.2700, 149.2900 | [1][11] | bron-gelegd (z15 gezien: kilometerslange kolenstockyards aan land, conveyorlijnen naar een offshore trestle, twee bulkcarriers gemeerd aan de berths; anker ligt op de trestle, ~0,3 km vóór de kade zelf — anker ≠ routeerpunt) |
| `kolen-dhamra-losplaats` | losplek zee / laadplek spoor | Dhamra Port, kolenstockyard + jetty | 20.8280, 86.9600 | [2][3] | bron-gelegd (z15 gezien: ovale stockyard met rail-lus, kolenstapels, conveyor oostwaarts naar een jetty met twee gemeerde schepen; Dhamra staat niet in ports.json — dichtstbijzijnde vermelde haven is Paradip, 162 km) |
| `kolen-kalinganagar-cokerij` | verwerkingsknoop / fabriek | Tata Steel Kalinganagar (cokerij + hoogovens), Jajpur, Odisha | 20.9704, 86.0152 | [4][12] | bron-gelegd (z15 gezien: geïntegreerd staalcomplex met rail-emplacement, grondstofstockyards en oven-/hoogovenstructuren) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Coppabella-junctie | -21.9408, 148.2744 | knooppunt van het Goonyella-systeem (Peak Downs/Saraji/Norwich Park/Lake Vermont/German Creek/Oaky Creek komen hier samen); sluit de GAP-lijn naar Abbot Point uit [8] |
| b3 | 1 | Bhadrak-junctie | 21.0600, 86.5000 | waar de Dhamra-Bhadrak-havenlijn (62 km) aansluit op de Howrah-Chennai-hoofdlijn [9] |
| b3 | 2 | Jakhapura-junctie | 20.9163, 86.0645 | waar de Daitari-Jakhapura-lijn van de hoofdlijn aftakt naar de Tata-siding Kalinganagar [10] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tata Steel Kalinganagar cokerij + hoogovens | Tata Steel | cokeskool (deels import via Dhamra) → cokes → ruwijzer → 8 Mt staal/j (fase II) | BF 2 5.870 m³; behoefte 3,0 Mt cokeskool/j voor de 6 Mt-fase [4][5] | [4][5] |

## 6 · Stoppunt
De brief stopt bij de cokerij/hoogovens van Kalinganagar: dat is al de eindverwerking (kolen → cokes → ruwijzer op
één terrein) en geen bron noemt een aparte fabriek stroomafwaarts van het staal zelf — fase D bestaat bij kolen
alleen voor een staalfabriek en die staat híer al aan het einde van fase C.

## 7 · Open punten
- **Mijnkeuze blijft "aannemelijk":** BMA verkoopt cokeskool per blend uit vijf mijnen (Goonyella Riverside, Peak
  Downs, Saraji, Norwich Park/Daunia, Caval Ridge); geen bron legt een specifieke Dhamra-lading bij Goonyella
  Riverside alleen — bronnen zeggen "Queensland"/"BMA" [1][2][3].
- **Terminalsplitsing HPCT/DBCT niet gepind:** de exacte splitsing tussen Hay Point Coal Terminal (BMA) en het
  aangrenzende Dalrymple Bay Coal Terminal is geometrisch niet apart via-gelegd; de gemeten 199,0 km eindigt op
  het BMA-anker.
- **Zeebeen-afstand niet gepubliceerd:** ~9.500–10.500 km is afgeleid (geen operator-cijfer); de bake meet het exact.
- **Dhamra-aanloop:** haven staat niet in ports.json → ~110 km stippel of `maak_havenaanloop.py`-uitkomst over de
  Golf van Bengalen; visueel zwak maar eerlijk (werkwijze §7).
- **Diepgangkeuze Torres-straat vs. noord-om-Papoea-Nieuw-Guinea** is een echte corridorkeuze voor een beladen
  Capesize; MARNET kent geen diepgang en kiest zelf een route — niet apart afgedwongen.
- **Eigenaarswissel Hay Point:** BMA kondigde in 2025 de verkoop van Hay Point Coal Terminal aan GIP aan [11] —
  de kade-eigenaar in de beennaam is dus een momentopname.
- **b3-lengte 114 km tegen ~140 km EC-rapport (−18%):** de eigen ankers (Dhamra-losplaats, Tata-siding) zijn ruw
  (snaps enkele km); met scherpere ankers komt de bake dichter bij 140 km, of de "140 km" is een wegafstand.

## 8 · Bronnen
[1] The Coal Trader, status van BHP's BMA — cokeskool-aandeel India (>40%), verkoop Hay Point Coal Terminal aan GIP. https://thecoaltrader.com/status-of-bhps-bma/
[2] Maritime Gateway, Dhamra Port dry-bulk record. https://www.maritimegateway.com/dhamra-port-dry-bulk-record/
[3] LinkedIn (Ramprasad Ravi B), Dhamra Port nationaal record — 165.283 t cokeskool uit Queensland voor Tata Steel. https://www.linkedin.com/posts/ramprasad-ravi-b901273_dhamra-port-in-odisha-has-set-a-new-national-activity-7479773790982266880-cBUd
[4] Tata Steel, persbericht — inhuldiging fase II-uitbreiding Kalinganagar (BF 2, 5.870 m³, 3 → 8 Mt/j). https://www.tatasteel.com/newsroom/press-releases/india/2025/tata-steel-inaugurates-phase-ii-expansion-of-kalinganagar-operations/
[5] Global Energy Monitor, Tata Steel Kalinganagar steel plant — coördinaten 20.970411,86.015211, capaciteit 8 Mt/j. https://www.gem.wiki/Tata_Steel_Kalinganagar_steel_plant
[6] Global Energy Monitor, Goonyella-Riverside Coal Mine — coördinaten -21.792321,147.962045, eigenaar BMA, 16,7 Mt/j (2025). https://www.gem.wiki/Goonyella-Riverside_Coal_Mine
[7] BHP, Goonyella Riverside mine — "coal is exported on the Goonyella railway line to Hay Point". https://www.bhp.com/what-we-do/global-locations/australia/queensland/goonyella-riverside
[8] Wikipedia, Goonyella railway line — 477 km, Coppabella-junctie (145,551 km) verbindt Peak Downs/Saraji/Norwich Park/Lake Vermont/German Creek/Oaky Creek. https://en.wikipedia.org/wiki/Goonyella_railway_line
[9] Wikipedia, Bhadrak railway station — Dhamra Port 62 km via de Dhamra–Bhadrak/Ranital-lijn op de Howrah-Chennai-hoofdlijn. https://en.wikipedia.org/wiki/Bhadrak_railway_station
[10] Wikipedia, Jakhapura Junction railway station — coördinaten 20.916344,86.064475; Daitari-Jakhapura-lijn gecommissioneerd 1981. https://en.wikipedia.org/wiki/Jakhapura_Junction_railway_station
[11] Wikipedia, Hay Point, Queensland — HPCT (BMA) en Dalrymple Bay Coal Terminal (Dalrymple Bay Infrastructure), gezamenlijk 97 Mt geëxporteerd 2021-22. https://en.wikipedia.org/wiki/Hay_Point,_Queensland
[12] Global Energy Monitor, Hay Point Coal Terminal — eigenaar BMA, capaciteit 55 Mt/j na Stage 3 (2015). https://www.gem.wiki/Hay_Point_Coal_Terminal
[13] Global Energy Monitor, Goonyella Rail System. https://www.gem.wiki/Goonyella_Rail_System
[14] Wikipedia, Dhamra Port — coördinaten 20.82333,86.96278, eigenaar Adani Ports & SEZ, 25 → 80 Mt/j capaciteit. https://en.wikipedia.org/wiki/Dhamra_Port
[15] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15) — `v2/build-cache/satcheck/sat-kolen-goonyella-kalinganagar-goonyella-laad.png`, `sat-kolen-goonyella-kalinganagar-haypoint-kade.png`, `sat-kolen-goonyella-kalinganagar-dhamra-kade.png`, `sat-kolen-goonyella-kalinganagar-tata-cokerij.png`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kolen-goonyella-kalinganagar`** → `v2/data/stroomroute-kolen-goonyella-kalinganagar.json` — 9 benen. 9.512,9 km. 4 markers: spoor (stippel) 2,4 km · spoor 324,3 km · zee 9.072,9 km · zee (stippel) 113,3 km.
Recept: `bak_stromen.sh` (functie `bak_kolen_goonyella_kalinganagar`). Toelichting: b1 (Goonyella Riverside → Hay Point) is twee spoorruns op het 1-op-1-net via de Coppabella-junctie (`toets_spoorroute.mjs`, `BAKE_SUFFIX=-raw`, extract australie) — 42,6 + 155,0 = 197,6 km gemeten been, plus twee korte stippels van 1,2 km elk (loadout-spur bij de mijn, HPCT-kade-aansluiting) voor het stuk dat niet op het net staat; totaal b1 = 200,0 km tegen de brief-schatting 199,0 km (+0,5%). b2 (zee) snapt aan de Hay Point-kant direct op zeeknoop 9022 (5,6 km, geen aanloop nodig); aan de Dhamra-kant ligt de haven 109,7 km van zeeknoop 2373 (21,0/88,0) — `maak_havenaanloop.py` gaf een schoon pad van 113,3 km (0% over land, omwegfactor 1,033) als stippel. Het gemeten zeebeen is 9.072,9 km, onder de brief-schatting van 9.500–10.500 km (afgeleid, geen operatorcijfer — de bake meet het exacte getal, dus dit is geen afwijking om dicht te trekken). b3 (Dhamra → Kalinganagar) is drie spoorruns (Dhamra→Bhadrak-junctie 66,6 km, Bhadrak→Jakhapura-junctie 46,6 km, Jakhapura→Tata-siding 13,5 km — de derde run was nodig, de router liet Jakhapura niet direct op de Tata-siding uitkomen); totaal 126,7 km tegen de brief-schatting 114,2 km (+11,0%, binnen de lichte ±15%-band, zoals de brief zelf al voorzag met "−18% t.o.v. het EC-rapport" als bekende ruwe-ankers-afwijking).

Stippels: (1) loadout-spur Goonyella Riverside → hoofdspoor (1,2 km, mijnemplacement niet in het 1-op-1-net) · (2) hoofdspoor → HPCT-kade-aansluiting (1,2 km, kade ligt 1,2 km van het net) · (3) haven-aanloop Dhamra Port (113,3 km, MARNET/ports.json kent de haven niet). Alle overige benen zijn gemeten en doorgetrokken.

Gereedschapslessen: (a) de zee-snap bij Hay Point (5,6 km, < 25 km max-snap) laat een eigen naad van 5,60 km tussen de HPCT-kade-stippel en het eerste getekende zeepunt — de snap zelf wordt niet als aparte lijn getekend (dezelfde klasse als de 5,6 km-snap bij QQCT/Qingdao in `bak_grafiet_balama_laixi`), licht boven de 5 km-norm en hier genoteerd, niet dichtgetrokken. (b) het derde spoorsegment (Jakhapura→Kalinganagar) draagt één omkering (175°, ~50 m boogstraal, `toets_knikken.py`: TERUGLOOP) vlak vóór de Tata-siding — een kopmaak op het fabrieksterrein, dezelfde klasse als Chuqui/Matarani (emplacement niet in het 1-op-1-net), geen via-punt bijgeschoven. (c) `toets_spoorroute.mjs` meldde op datzelfde derde segment "sanity FOUT — route korter dan de grootcirkel": een bekende bug in het meetgereedschap (de grootcirkel wordt tussen de ongesnapte invoerpunten berekend, de route tussen de gesnapte hoofdnet-knopen die dichter bij elkaar liggen) — geen routeerfout, de route zelf (13,5 km over 20 edges, 1 kopmaak) is plausibel voor de laatste kilometers naar een siding. Toetsen geslaagd: `toets_knikken.py` (1 terugloop, verwacht en toegelicht) · `toets_rechte_benen.py --min-km 5` (geen treffers) · json.load/versie 2/punt_formaat lonlat/modaliteiten {spoor, zee}/elk been ≥2 punten/bestand 32,9 KB, allemaal binnen de norm.
