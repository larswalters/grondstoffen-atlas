# Routebrief (licht) · nikkel — Sudbury → Québec → Kristiansand (Noorwegen)

**stroom-id:** `nikkel-sudbury-kristiansand` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** sulfide-matte (~60 % Ni) van de Glencore Sudbury Smelter (Falconbridge, Ontario) per **spoor**
via Toronto en Montréal naar de Glencore-terminal in de haven van Québec, per **zeeschip** over de Saint-Laurent,
de Cabotstraat en het Skagerrak naar de Nikkelverk-kade in Kristiansand — de LME-leverbare eindraffinage van
Glencore's Atlantische class-1-as. Geen fase D: geen bron dekt een vervolgzending naar Rotterdam per lading.
**Welke as van het verhaal:** de Atlantische class-1-keten naar Europa — Canadese sulfide-matte naar Nikkelverk,
het LME-leverbare nikkel voor de EU-markt. 22 scheepsladingen/jaar, ~140 kt matte, Québec → Kristiansand [2];
Nikkelverk raffineert ~92 kt Ni/j (Glencore) [4][8].

## 1 · Ketenkaart
```
Sudbury Smelter `ni-sudbury-smelter` ──(b0 spoor · eigen emplacement, stippel · ~2 km)──► spoornet
   ──(b1 spoor · CN Bala Sub Sudbury→Toronto → CN Kingston Sub Toronto→Montréal→Québec,
       via MacMillan Yard + Taschereau Yard · ~1.230 km)──► Québec-kade `ni-quebec-kade` (secteur Beauport)
   ──(b2 zee · Saint-Laurent–benedenloop → Cabotstraat → Skagerrak · ~5.452 km, MARNET)──► Nikkelverk-kade
       `ni-nikkelverk-kade` (Kolsdalen, Kristiansand) ── stoppunt
```
Vertakking niet getekend: Raglan-concentraat (Deception Bay, Nunavik) komt via Québec het spoor óp in
tegenrichting naar Sudbury — zou het spoorbeen dupliceren in de verkeerde richting [3][5].

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b0 | A | spoor | `ni-sudbury-smelter` → spoornet | Falconbridge-emplacement/rangeerspoor | ~2 [webcheck: snap 2,22 km] | stippel — net reikt niet | ja |
| b1 | A | spoor | spoornet → `ni-quebec-kade` | CN Bala Sub (Sudbury→Toronto, via MacMillan Yard) → CN Kingston Sub (Toronto→Montréal, via Taschereau Yard→Québec) | ~1.230 [webcheck; geen gepubliceerde lengte, CN Alderdale Sub via Ottawa bestaat niet meer sinds 1996 [6]] | toets_spoorroute (drie/vier runs via de twee via-punten) | nee |
| b2 | B | zee | `ni-quebec-kade` → `ni-nikkelverk-kade` | Saint-Laurent-benedenloop → Cabotstraat → Noord-Atlantische Oceaan → Skagerrak | ~5.452 [webcheck; 22 schepen/j, 140 kt matte/j gebrond [2]] | MARNET | nee (beide kades <25 km van een zeeknoop — Québec 0,6 km, Kristiansand 6,2 km) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-sudbury-smelter` | mijn/smelter (kop van het spoor) | Glencore Sudbury Smelter (Falconbridge), Sudbury INO | 46.5786, -80.7993 | [3][5][12][13] | bron-gelegd (z15 gezien: industrieel complex met hoge gebouwen/schoorsteen aan de oostrand van Falconbridge, adres 6 Edison Rd) |
| `ni-quebec-kade` | overslag spoor → zee | Glencore-terminal, Port of Québec, secteur Beauport | 46.8330, -71.2035 | [2][12][13] | aannemelijk (z15 gezien: tankenpark + industrieel havenfront met steiger en schip in secteur Beauport; welke exacte steiger Glencore's matte-terminal is, is niet te onderscheiden — Glencore noemt géén kade/sector) |
| `ni-nikkelverk-kade` | losplek + raffinaderij (site-anker, geen apart kade-been — eigen terrein) | Nikkelverk (Glencore), Kolsdalen, Kristiansand | 58.1388, 7.9713 | [4][8][10][13] | bron-gelegd (z15 gezien: industrieterrein met kade/pier direct aan de Kristiansandsfjord, adres Vesterveien 31) |

## 4 · Via-punten (alleen b1 — corridorkeuze rond Toronto/Montréal)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | MacMillan Yard (CN, Vaughan/Toronto-noord) | 43.8119, -79.5111 | trekt de route om Toronto-lakeshore heen — zonder dit via-punt geeft een vrije Dijkstra een 180°-omkering bij 43.667,-79.465 (Toronto-west) [webcheck] |
| b1 | 2 | Taschereau Yard (CN, Saint-Laurent/Montréal) | 45.4686, -73.6861 | pint de CN Kingston Sub door Montréal in plaats van een sluipweg eromheen |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sudbury Smelter (Falconbridge) | Glencore Sudbury INO | nikkel-koperconcentraat (Nickel Rim South/Fraser + custom feed + Raglan-concentraat) → matte ~60 % Ni | matte-export ~140 kt/j naar Québec [2][3] | [2][3][5] |
| Nikkelverk | Glencore | matte → 99,99 % nikkel (chloorloog-raffinage) + kobalt | ~92 kt Ni/j | [4][8] |

## 6 · Stoppunt
De brief stopt bij Nikkelverk: geen bron documenteert een vervolgzending naar Rotterdam RHB of enig ander
LME-entrepot per lading — de afzet naar de EU/LME-markt is alleen in algemene termen genoemd, niet per zending.

## 7 · Open punten
- **Welke steiger in secteur Beauport** Glencore's matte-terminal is, staat in geen bron (kade/sector niet genoemd
  door Glencore Canada); `ni-quebec-kade` blijft *aannemelijk*.
- **Spoorbedrijf/lijn niet met naam genoemd** door Glencore — de CN Bala/Kingston-route volgt uit de weerlegging
  van de Ottawa-vallei-corridor (CN Alderdale Subdivision, opgebroken na 1996 [6]) en is niet zelf gebrond.
- **Fase D (Rotterdam RHB)** vervalt: geen bron koppelt Nikkelverk-productie aan een specifieke LME-entrepotzending.
- **Raglan-vertakking** (Deception Bay → Québec → Sudbury) bewust niet getekend — zou het spoorbeen in
  tegenrichting dupliceren.
- **Vale's parallelle keten** (Sudbury → Copper Cliff; Voisey's Bay → Long Harbour) is het reële binnenlandse
  alternatief maar hoort niet in deze brief (andere eigenaar, ander eindpunt).
- **b0-lengte (~2 km)** is een schatting uit de haalbaarheidstoets, geen gepubliceerde waarde.

## 8 · Bronnen
[1] Glencore, "The journey of nickel". https://www.glencore.com/what-we-do/metals-and-minerals/nickel/the-journey-of-nickel
[2] Glencore Canada, "Facilities at Port of Quebec" — matte per spoor Sudbury Smelter → Port of Québec, ~22 schepen/j, 140.000 t naar Kristiansand. https://www.glencore.ca/en/our-assets/facilities-at-port-of-quebec
[3] Glencore Canada, Sudbury INO "At a glance" — Fraser Mine, Strathcona Mill, Sudbury Smelter, Raglan-custom feed. https://www.glencore.ca/en/sudburyino/who-we-are/at-a-glance
[4] Glencore, Nickel overview — Nikkelverk als raffinaderij van de Canadese matte. https://www.glencore.com/what-we-do/metals-and-minerals/nickel
[5] Glencore Canada, "Smelting and recycling" — adres 6 Edison Rd, Falconbridge, ON; matte naar Québec/Nikkelverk. https://www.glencore.ca/en/sudburyino/what-we-do/smelting-and-recycling
[6] Wikipedia, "CN Alderdale Subdivision" — Capreol–North Bay–Ottawa-lijn afgestoten, sporen verwijderd na 1996. https://en.wikipedia.org/wiki/CN_Alderdale_Subdivision
[7] Wikipedia, "MacMillan Yard" — CN-rangeerterrein Vaughan/Toronto-noord. https://en.wikipedia.org/wiki/MacMillan_Yard
[8] Nikkelverk (Glencore), officiële site — grootste nikkelraffinaderij van het westen, Kristiansand. https://www.nikkelverk.no/en
[9] Glencore, "Nikkelverk Public Responsible Supply Chain Due Diligence Report" 2024 (PDF). https://www.glencore.com/.rest/api/v1/documents/static/51d9a58f-6979-45d8-8936-c8e411dea4d1/2024+Nikkelverk+Public+Responsible+Supply+Chain+Due+Diligence+Report.pdf
[10] Wikipedia, "Kolsdalen" — locatie van Nikkelverk binnen Kristiansand. https://en.wikipedia.org/wiki/Kolsdalen
[11] Wikidata, "Glencore Nikkelverk" (Q17776423). https://www.wikidata.org/wiki/Q17776423
[12] OpenStreetMap/Nominatim (ODbL) — adrespunten Edison Road/Falconbridge, "Port de Québec - Secteur Beauport" (railway yard), Vesterveien 31/Glencore Nikkelverk. https://www.openstreetmap.org
[13] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-nikkel-sudbury-kristiansand-smelter.png`, `sat-nikkel-sudbury-kristiansand-quebec-kade.png`, `sat-nikkel-sudbury-kristiansand-nikkelverk.png`.


## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `nikkel-sudbury-kristiansand`** → `v2/data/stroomroute-nikkel-sudbury-kristiansand.json` — 5 benen, **6.746,2 km**, 3.562 punten, 5 markers. spoor 0,2 (stippel) + 465,7 + 541,0 + 286,9 = 1.293,8 km · zee 5.452,4 km.
Recept: `bak_stromen.sh` (functie `bak_nikkel_sudbury_kristiansand`).

**b0 (spoor, stippel):** Falconbridge-emplacement → spoornet, gemeten via de snap uit run 1 hieronder (`BAKE_SUFFIX=-raw`, hoofdnet-knoop 248525 op **0,161 km**) — ruim onder de haalbaarheidsschatting van 2,22 km uit de brief; de échte meting vervangt de schatting (wie meet wint van wie redeneert).

**b1 (spoor, drie runs op het 1-op-1-net, console bevestigt "3260717 spoor-edges"):**
1. Sudbury-emplacement → MacMillan Yard (`--van=46.5786,-80.7993 --naar=43.8119,-79.5111`): **465,7 km over 545 edges** (grootcirkel 323,8 km, verhouding 1,43).
2. MacMillan Yard → Taschereau Yard (`--van=43.8119,-79.5111 --naar=45.4686,-73.6861`): **541,0 km over 571 edges** (grootcirkel 496,2 km, verhouding 1,08).
3. Taschereau Yard → Québec-kade (`--van=45.4686,-73.6861 --naar=46.8330,-71.2035`): **286,9 km over 421 edges** (grootcirkel 244,1 km, verhouding 1,16).

Totaal **1.293,6 km tegen ~1.230 km (webcheck 1.231,4) uit de brief = +5,1%, ruim binnen ±15%.**

⚠️ **Twee TERUGLOOPS (`toets_knikken.py`) blijven staan, gemeten maar niet dichtgetrokken:** 180° bij 43,6673/-79,4652 (boogstraal ~36 m, run 1, verhouding pad/hemelsbreed v=99,0) en 180° bij 43,8263/-79,5153 (boogstraal ~0 m, run 2, v=12,9) — allebei net aan weerszijden van de MacMillan-yardcluster. Onderzocht met vier alternatieve via-vertices (0,00–2,26 km van het opgegeven punt, incl. de dichtstbijzijnde vertex 43,8352/-79,5304 op 0,00 km) en met `--keerstraf` tot 1000 (40× de default, ruim boven wat de bak-aanwijzing suggereerde): de lus verandert niet van plek en verdwijnt niet. Netmeting verklaart waarom: de yardcluster is een lokaal subnet van ~1,4 km met knopen 0,000–0,100 km uit elkaar (een dichte laddertrack van korte wissel-edges — knopen 188507/188510/188511 onderzocht); de dichtstbijzijnde knoop daarbuiten ligt op ≥29,9 km. Élk via-punt in of rond de yard bereikt de rest van het net dus via dezelfde brongeometrie — de omkering zit in de brongeometrie zelf, niet in de gekozen via-coördinaat. Bevinding, niet dichtgetrokken (werkwijze §5: buiten de norm = bevinding).

**b2 (zee, MARNET, geen aanloop nodig):** `--been "zee|...|46.8330,-71.2035|58.1388,7.9713"` — snap Québec-kade 1,617 km (brief-schatting 0,6 km) en Kristiansand 6,475 km (brief-schatting 6,2 km), beide ruim binnen `--max-snap` 25 km, dus inderdaad geen aparte haven-aanloop nodig zoals de bak-aanwijzing al zei. Resultaat **5.452,4 km over 46 MARNET-edges** (574 punten) — nagenoeg exact de webcheck-schatting uit de brief (5.452,4 km). Lengte-invariant: getekende lijn 5.452,360 km vs som edge-km 5.452,100 km = +0,260 km (de naden).

**Toets:** naden tussen alle vijf opeenvolgende benen **0,00 km** op de eerste vier overgangen en **1,51 km** tussen b1 (Taschereau→Québec-kade) en b2 (zee) — het zeebeen begint op zijn eigen MARNET-zeeknoop-snap (46,8371/-71,1831), niet op het exacte spoor-eindpunt; ruim binnen de norm van ≤5 km. `toets_knikken.py`: **4 knikken ≥60°, 2 omkeringen ≥150°, beide TERUGLOOP** (zie b1 hierboven) plus 1 "krappe bocht" (92,9°, straal 5.733 m) op het zeebeen bij de Noorse kust (57,95/8,05) — een gewone kustbocht, geen terugloop. `toets_rechte_benen.py --min-km 5`: geen been van deze stroom gevonden (b0 is de enige rechte stippel, 0,161 km, ruim onder de 5 km-drempel). json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {spoor, zee}, elk been ≥2 punten, bestandsgrootte 66,7 KB (< 300 KB). Markers: smelter 0 m · MacMillan Yard 87,6 m · Taschereau Yard 109,7 m · Québec-kade 122,1 m · **Nikkelverk-kade 6.474,6 m** (anker ≠ routeerpunt — het zeebeen eindigt op MARNET-zeeknoop 58,0993/8,0523, 6,475 km van de kade-anker; conform de bak-aanwijzing, die hier bewust geen haven-aanloop bouwt omdat de snap ruim onder 25 km blijft).

**Gereedschapslessen:**
- Een gemeten spoorsnap kan ver onder een haalbaarheidsschatting uitkomen (hier 0,161 tegen geschat 2,22 km) — de schatting was een webcheck-benadering zonder de 1-op-1-graaf; de meting met `BAKE_SUFFIX=-raw` is de echte waarde en vervangt de schatting, niet andersom.
- Niet elke TERUGLOOP is oplosbaar door het via-punt te verschuiven: als het hele lokale subnet rond een via-punt maar op één manier aansluit op het grote net (hier: een yardcluster van 1,4 km die pas op ≥29,9 km weer aansluit), routeert élke keuze binnen die cluster over dezelfde brongeometrie. `--keerstraf` tot 40× de default veranderde hier niets — het bewijs dat de omkering een vaste eigenschap van de graaf is, geen discretionaire routekeuze. Zoek in zo'n geval eerst de netconnectiviteit rond het via-punt (dichtstbijzijnde knoop buiten de lokale cluster) vóórdat je meer via-vertices probeert.
- MARNET-zeeknopen kunnen een paar honderd meter tot een paar kilometer van de brief-schatting afwijken (Québec 0,6→1,617 km, Kristiansand 6,2→6,475 km) zonder dat er iets mis is — beide blijven ruim onder `--max-snap` 25 km en de bak-aanwijzing "geen aparte haven-aanloop nodig" klopte voor allebei.
