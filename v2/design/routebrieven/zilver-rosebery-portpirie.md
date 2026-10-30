# Zilver · Rosebery → Burnie → Port Pirie (Australië)

**stroom-id:** `zilver-rosebery-portpirie` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Zn-Pb-Cu-Ag-concentraat van de MMG-Rosebery-fabriek (Tasmanië) per **spoor** (Melba Line, TasRail) naar de Port of Burnie, per **zeeschip** door Bass Strait en Spencer Gulf naar de Nyrstar-loodsmelter in Port Pirie (Zuid-Australië), die zilver raffineert — bewust **stoppunt** bij de smelter, geen fase D/E.
**Welke as van het verhaal:** Tasmaniës enige grote zilver-bijproduct-mijn naar Australiës loodsmelter; deelt de eindsmelter met `zilver-brokenhill-portpirie`. **Jaarvolume:** Rosebery produceerde in 2023 2.583.418 oz Ag in concentraten = **80,4 t Ag/j** (payable in verkocht product 2.206.577 oz = 68,6 t Ag/j) [2]. Aandeel dat naar Port Pirie gaat (lood- en edelmetaalconcentraat) versus Hobart (zinkconcentraat) is niet gepubliceerd [1].

## 1 · Ketenkaart
```
Rosebery-mijn/fabriek `ag-rosebery-mijn` ──(b1 spoor · Melba Line (TasRail, ex-Emu Bay Railway) · 108,2 km gemeten, geen bronkm [3][4])──►
   Port of Burnie `ag-burnie-haven` ──(b2 zee · Bass Strait → Spencer Gulf · 1.497 km MARNET + haven-aanloop 42,0 en 33,4 km)──►
   Port Pirie-smelterkade `ag-portpirie-kade` ── (0,4 km) ── Nyrstar-smelter `ag-portpirie-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ag-rosebery-mijn` → `ag-burnie-haven` | Melba Line Rosebery–Guildford Jn–Burnie (TasRail; "concentrate travels by rail to the Port of Burnie" [1]) | hemelsbreed 86 km, geen spoorkm gepubliceerd; lijn Burnie–Melba Flats ~130 km [3] (indicatie) | toets_spoorroute (extract `australie`, `--max-snap=60 --hoofd-km=50 --keerstraf=100`) = 108,2 km, snap 0,66 / 0,28 km | nee |
| b2a | B | zee | `ag-burnie-haven` → MARNET-zeeknoop 6029 (-41.1280, 146.3612) | haven-aanloop Burnie, kade 38,6 km van de knoop (> 5 km) | 42,0 km gemeten | maak_havenaanloop (gelukt, 4 s) | **ja** (aanloop, schematisch over water) |
| b2 | B | zee | zeeknoop 6029 → zeeknoop 6044 (-33.1927, 137.7356) | Bass Strait, ten zuiden langs Kangaroo Island, Spencer Gulf | 1.496,7 km MARNET; hemelsbreed kade-kade ~1.125 km; vaarweg ~1.400 km (eigen inschatting, geen bron) | MARNET | nee |
| b2c | B | zee | knoop 6044 → `ag-portpirie-kade` | haven-aanloop Port Pirie, kade 25,9 km van de knoop (> 25 km snap én > 5 km) | 33,4 km gemeten | maak_havenaanloop (gelukt, 4 min) | **ja** (aanloop, schematisch) |

"Aannemelijk: één bron" geldt voor de bestemming van het lood-zilverconcentraat (MMG noemt Port Pirie zonder volume), niet voor de lijnstijl: b1 en b2 zijn doorgetrokken. Geen last-mile-been: de fabriek staat op ~0,7 km van de Melba Line (snap 0,66 km) en de smelter ligt 0,4 km van de kade. De zeeroute loopt ~85 km heen-en-terug door de knoop bij Devonport (aanloop Burnie gaat 38 km oostwaarts, de route daarna westwaarts weer langs Burnie): cosmetisch, MARNET heeft geen knoop westelijker dan 115 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-rosebery-mijn` | mijn + fabriek, laadplek (kop b1) | MMG Rosebery Mine, Rosebery | -41.7754, 145.5385 | [1][10] | bron-gelegd (z15 gezien: verwerkingscomplex met dakvlakken en opslag midden in het dorp, tailingsdam 1,2 km zuidelijk) |
| `ag-burnie-haven` | overslag spoor → schip | Port of Burnie, kade bij No 6/7 Berth | -41.0537, 145.9116 | [1][6][7][10] | aannemelijk (z16 gezien: diepwaterkade met emplacement en schuren; welk berth het concentraat laadt is niet gevonden — TasRail noemt alleen een "Bulk Mineral Export Facility" met shiploader) |
| `ag-portpirie-kade` | losplek schip | Nyrstar-smelterkade, Port Pirie | -33.1710, 138.0129 | [8][9][11] | bron-gelegd (z16 gezien: vrachtschip afgemeerd aan de kade langs de smelterwerken, spoor en loods op de kade) |
| `ag-portpirie-smelter` | smelter (stoppunt) | Nyrstar Port Pirie-smelter | -33.1684, 138.0095 | [8][9] | bron-gelegd (letterlijk hergebruikt uit `zilver-brokenhill-portpirie`, z15 daar en hier gezien: hallen, stapels en sporen aan de rivierarm) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen. De Melba Line is de enige spoorlijn tussen Rosebery en Burnie (de Murchison Highway, sinds 1963 de weg, is geen spoorkeuze [5]); een vrije run gaf 108,2 km. Bij `--keerstraf=25` kwam één 174°-omkering (91 m straal) op het Burnie-emplacement; bij `--keerstraf=100` is die weg (alleen een zigzag-punt geschrapt).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Rosebery-fabriek | MMG | erts (ondergronds) → zink-, lood-, koper- en edelmetaalconcentraat | zink in concentraat 45.000–55.000 t/j; Ag 2,58 Moz (80,4 t) in 2023 | [1][2] |
| Nyrstar Port Pirie-smelter | Nyrstar | lood-zilverconcentraat → lood, zilver, koper, goud, zuur | geen vers jaarcijfer (zie `zilver-brokenhill-portpirie`) | [8][9] |

## 6 · Stoppunt
De brief stopt bij de Nyrstar-smelter in Port Pirie: dat is de plek waar het zilver uit het loodconcentraat tot metaal wordt, en geen bron noemt een gedocumenteerde vervolgzending van het geraffineerde zilver.

## 7 · Open punten
- **Aandeel van Rosebery-zilver naar Port Pirie** onbekend: MMG noemt Nyrstar Hobart (zink) én Port Pirie [1]; 2023-zilver (80,4 t) zit verdeeld over lood- en edelmetaalconcentraat. Volume op de kaart = bovengrens.
- **Peiljaar:** 2023 (MDA 2023); 2024/2025-zilver niet gevonden. Q2 2026: zinkconcentraat 9.500 t, -25% j-o-j [12].
- **Spoorkm b1** geen bron; 108,2 km is een meting. Melba Line ~130 km tot Melba Flats [3] en Burnie–Zeehan 131 km [4] geven alleen een bovengrens; Rosebery ligt ruim ervoor (tot ~25 km).
- **Burnie-berth** voor concentraat niet gevonden (OSM kent alleen berth-nodes 4–7, TasPorts als bron); `ag-burnie-haven` is dus aannemelijk. Port Pirie-kade is niet door een bron als "concentraatkade" benoemd; punt is op de afgemeerde schepen gelegd.
- **Zeeafstand** is MARNET-grof (1.497 km vs ~1.400 km eigen schatting); geen gepubliceerde vaarafstand.
- Port Pirie-aanloop (33,4 km, 2,8 km "over land" aan de kade-kant) en Burnie-aanloop (42,0 km, 0,8 km) zijn schematisch, 1:10M-kust kent de havens niet.

## 8 · Bronnen
[1] MMG, "Rosebery" — concentraat per spoor naar Port of Burnie, verscheept naar Nyrstar Hobart en Port Pirie; zink 45.000–55.000 t/j; geen Ag-cijfer. https://www.mmg.com/operations/rosebery/
[2] MMG, Rosebery MD&A 2023 — Ag 2.583.418 oz (2022: 2.178.998), payable 2.206.577 oz, Au 30.096 oz. https://www.mmg.com/wp-content/uploads/2024/04/MDA_ROS.pdf
[3] Wikipedia, "Melba Line" — ~130 km, Burnie–Melba Flats, TasRail, 1.067 mm. https://en.wikipedia.org/wiki/Melba_Line
[4] Wikipedia, "Emu Bay Railway" — Burnie–Rouse's Camp 71 km + 60 km naar Zeehan; Rosebery–Melba Flats heropend 1970 (EZ). https://en.wikipedia.org/wiki/Emu_Bay_Railway
[5] Wikipedia, "Rosebery, Tasmania" — mijn sinds 1936 door EZ/…/MMG; Emu Bay Railway tot de Murchison Highway (1963). https://en.wikipedia.org/wiki/Rosebery,_Tasmania
[6] TasPorts, "Burnie Gateway" projectbrief — Port of Burnie, bulkmineralenexport, mineralenopslag en shiploader. https://tasports.com.au/volumes/documents/Major-Projects/Burnie-Gateway/Infrastructure-Project-Brief_Burnie-Gateway.pdf
[7] Infrastructure Minister, "Port of Burnie shiploader complete, doubling capacity" (TasRail Bulk Mineral Export Facility; alleen via zoekresultaat). https://minister.infrastructure.gov.au/c-king/media-release/port-burnie-shiploader-complete-doubling-capacity
[8] Nyrstar Port Pirie operations-pagina (via brief `zilver-brokenhill-portpirie` [8]). https://www.nyrstar.com/operations/metals-processing/nyrstar-port-pirie
[9] Wikipedia, "Port Pirie" (via brief `zilver-brokenhill-portpirie` [3]). https://en.wikipedia.org/wiki/Port_Pirie
[10] OpenStreetMap (ODbL), Nominatim/Overpass — "MMG Rosebery Mine" (way 408998641), "Burnie Port" (way 911186976), berth-nodes 12128751855 e.v. (No 4–7, bron TasPorts). https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-zilver-rosebery-portpirie-{mijn,burnie,burnie16,smelter,kade16}.png`.
[12] Metal.com, "MMG Q2 2026 … Rosebery Falls 25%" — 9.500 t zinkconcentraat. https://news.metal.com/newscontent/104029162-mmg-q2-2026-zinc-production-down-1-yoy-dugald-river-up-6-rosebery-falls-25
[13] Metingen: `toets_spoorroute.mjs`, `maak_havenaanloop.py`, `hecht_marnet.py route` (droge run, 2026-10-30).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Bestand:** `v2/data/stroomroute-zilver-rosebery-portpirie.json` (19,5 KB, versie 2, lonlat) · functie `bak_zilver_rosebery_portpirie` in `v2/tools/bak_stromen.sh` · 4 benen, 937 punten, 4 markers, totaal 1.680,5 km.

| # | modaliteit | km | naad | stippel | been |
|---|---|---|---|---|---|
| 1 | spoor | 108,4 | 0 | nee | trein Rosebery-fabriek → Port of Burnie (Melba Line, 1-op-1-net) |
| 2 | zee | 42,0 | 0,28 | ja | haven-aanloop Burnie (kade 38,6 km van knoop 6029) |
| 3 | zee | 1.496,7 | 0 | nee | zeeschip knoop 6029 → knoop 6044 (MARNET, bestemming aannemelijk: een bron) |
| 4 | zee | 33,4 | 0 | ja | haven-aanloop Port Pirie (kade 25,9 km van knoop 6044) |

**Recept:** b1 `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=-41.7754,145.5385 --naar=-41.0537,145.9116 --naam=zilver-rosebery-portpirie-rosebery-burnie --max-snap=60 --hoofd-km=50 --keerstraf=100`; aanlopen met `maak_havenaanloop.py` (Burnie 42,0 km, Port Pirie 33,4 km); b2 MARNET over de twee zeeknopen zonder snap. Alle tussenuitvoer stond al op schijf (prefix `zilver-rosebery-portpirie-`); alleen de functie is nieuw. Markers: ag-rosebery-mijn, ag-burnie-haven, ag-portpirie-kade, ag-portpirie-smelter.

**Toets:** b1 108,4 km tegen 108,2 gemeten in de brief (geen gepubliceerde spoorkm, indicatie ~130 km lijn tot Melba Flats); geen naad > 5 km (grootste 0,28 km bij het begin van de Burnie-aanloop); markers 0,0 / 0,0 / 0,43 / 0,66 km van de lijn (mijn-anker ligt 0,66 km van het spoor = de snap van b1, smelter 0,43 km van de kade, beide bewust anker ≠ routeerpunt). `toets_knikken`: 1 krappe bocht van 97,9 graden in het MARNET-zeebeen bij -35,50 135,67 (zee, geen omkering of terugloop); `toets_rechte_benen`: niets voor deze stroom.

**Stippels:** beide zeeaanlopen zijn schematisch over water omdat de 1:10M-kust Burnie en Port Pirie niet kent; b1 en b2 zijn doorgetrokken (het ene gemeten, het andere MARNET). De bestemming Port Pirie versus Hobart blijft "aannemelijk: een bron" (in beennaam b3), niet in de lijnstijl.

**Lessen:** de zeeroute loopt cosmetisch ~85 km heen-en-terug bij Devonport (aanloop Burnie gaat 38 km oostwaarts, MARNET-route daarna westwaarts); geen echte fout, MARNET heeft geen knoop westelijker dan 115 km. Tijdens het bakken gaf bak_stromen.sh eenmalig een syntaxfout op regel ~14015 in andermans functie (gas-mnazibay-dares-salaam, gelijktijdige edit); een herhaalde `bash -n` was schoon.
