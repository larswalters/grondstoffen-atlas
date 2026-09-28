# Routebrief (licht) · Zilver · Garpenberg → Gävle → Rönnskär (land)

**stroom-id:** `zilver-garpenberg-ronnskar` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** zink/lood-concentraat (met het zilver als bijproduct) van de Boliden Garpenberg-mijn
(Dalarna) per **truck** naar de Boliden-terminal in de haven van Gävle, en per **zeeschip** over de Botnische
Golf naar de Rönnskär-smelter (Boliden, Skelleftehamn) — stoppunt bij de smelter.
**Welke as van het verhaal:** *Zweeds binnenlands truck+zee-patroon, geen spoor* — de haalbaarheidstoets
verving het ontworpen ene spoorbeen door dit truck+zee-patroon op basis van Boliden's eigen bronnen; ≈260 t
Ag/j uit het Garpenberg-concentraat (Boliden jaarverslag 2024, via `v2/design/zilver-sitelaag.md`).

## 1 · Ketenkaart
```
Garpenberg-mijn (Boliden, Dalarna) `ag-garpenberg-mijn`
   ──(b1 truck · Gästrikland via Hofors–Storvik–Sandviken · hemelsbreed ~70 km)──►
Gävle-haven, Fredriksskans-terminal `ag-gavle-kade`
   ──(b2 zee · Botnische Golf · MARNET, haven-aanloop bij Gävle)──►
Rönnskär-smelter (Boliden, Skelleftehamn) `ag-ronnskar-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ag-garpenberg-mijn` → `ag-gavle-kade` | Gästrikland, via Hofors–Storvik–Sandviken (geografische afleiding — consistente noordwaartse boog t.o.v. de hemelsbrede lijn, geen gepubliceerde routebron) | hemelsbreed 69,8 km, geen wegkm binnen budget | `maak_stroombeen_weg.py` | nee |
| b2 | B | zee | `ag-gavle-kade` → `ag-ronnskar-kade` | Botnische Golf, MARNET kade→kade | geen brief-schatting (webbudget op) | MARNET (`--been "zee|..."`) | aanloop: **ja** bij Gävle (kade 19,2 km van zeeknoop, > 5 km-drempel) / **nee** bij Rönnskär (1,5 km van zeeknoop) |

Modaliteit is **BINDEND gecorrigeerd** t.o.v. het ketenontwerp (dat één onbevestigd spoorbeen veronderstelde):
Boliden's eigen NI 43-101-rapport zegt letterlijk — *"The zinc and lead concentrates are transported by truck
to Gävle port and from there by ship to Boliden's smelters in Finland, Sweden and Norway. The copper and
gravimetric concentrates are trucked, the copper concentrate later being reloaded to rail, for onward
transport to the Boliden Rönnskär smelter"* [1]. Alleen het **koper**concentraat gaat dus per spoor naar
Rönnskär; het Zn/Pb-concentraat (met het zilver) gaat per truck+zee. `spoornet_nodig` = **false**.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-garpenberg-mijn` | mijn (zink/lood, kop van het wegbeen) | Boliden Garpenberg, Dalarna | 60.3129, 16.1933 | [2][4][7] | bron-gelegd (z15 gezien: industrieel mijncomplex met hallen, opslagterrein en toegangswegen direct ZO van het dorp Garpenberg; OSM `landuse=industrial "Boliden"` 0 m van het punt) — wijkt ~600 m af van het bestaande sitelaag-anker `w-garpenberg` (60.3158,16.1983, dorpscentroïde); zie §7 |
| `ag-gavle-kade` | overslag truck → zee (tank-/bulkterminal) | Gävle Hamn, Fredriksskans-terminal | 60.6922, 17.2103 | [1][9] | bron-gelegd (z14 gezien: tankenpark + kade met kraanopstelling en loodsen op de Fredriksskans-landtong, water aan drie zijden — de bulkterminal van de haven van Gävle) |
| `ag-ronnskar-kade` | smelter/losplek (stoppunt) | Boliden Rönnskär, Skelleftehamn | 64.6704, 21.2699 | [3][8][11] | bron-gelegd (z15 gezien: smeltercomplex met schoorstenen, tankenpark en kade op het schiereiland Rönnskär; OSM `landuse=industrial "Rönnskärsverken"` 0 m van het punt) — **hergebruikt anker** (`zilver-sitelaag.md` `w-ref-ronnskar`), coördinaat onafhankelijk bevestigd via OSM (0 m verschil) en satellietblik → status opgewaardeerd van aannemelijk naar bron-gelegd |

## 4 · Via-punten (alleen b1 — corridorkeuze Dalarna→Gästrikland)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Hofors | 60.5455, 16.2855 | pint de corridor noordwaarts door Gästrikland i.p.v. de hemelsbrede lijn (die door meer landelijk gebied zonder duidelijke hoofdweg zou snijden); geografische afleiding, niet gebrond |
| b1 | 2 | Storvik | 60.5853, 16.5350 | vervolgpunt op dezelfde noordwaartse boog, tussen Hofors en Sandviken |
| b1 | 3 | Sandviken | 60.6219, 16.7760 | grootste tussenliggende plaats vóór Gävle, waarschijnlijke corridor via een doorgaande weg (route 80-richting) |

Alle drie liggen op een consistente noordwaartse boog t.o.v. de rechte lijn Garpenberg→Gävle (10–22 km
uitwijking, afnemend richting Gävle) — geen losse zijsprong, maar geen van de drie is gebrond met een bron;
zie open punt in §7.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Garpenberg-mijn | Boliden | ruw erts → zink/lood-concentraat (met Ag/Au-bijproduct) | ≈260 t Ag/j uit het Garpenberg-concentraat, jaarverslag 2024 | [2][11] |
| Rönnskär-smelter | Boliden | koper- en loodconcentraat → koper/lood + edelmetalen (Ag/Au) | smelter verwerkt eigen + extern concentraat; geen apart Garpenberg-specifiek Ag-cijfer bij Rönnskär gevonden binnen budget | [3] |

## 6 · Stoppunt
De brief stopt bij de Rönnskär-smelter: geen bron noemt een fabriek of afnemer na de raffinage bij Rönnskär
voor dit specifieke Garpenberg-concentraat — fase D vervalt.

## 7 · Open punten
- **Wegcorridor Garpenberg→Gävle niet gebrond** — Hofors–Storvik–Sandviken is een geografische afleiding
  (consistente boog, geen gepubliceerde routebron); bij het bakken moet `maak_stroombeen_weg.py` de
  werkelijke doorgaande weg vinden/bevestigen. Geen echte wegkilometer gevonden binnen budget (alleen
  hemelsbreed 69,8 km).
- **Welk concentraat exact het zilver naar Rönnskär draagt is niet uitgesplitst** — Rönnskär verwerkt zelf
  alleen koper- én loodconcentraat [3]; het zinkconcentraat gaat vermoedelijk naar Kokkola (Finland) of Odda
  (Noorwegen) [1]. Aannemelijk dat het **lood**concentraat (met Ag) de Rönnskär-tak draagt, niet apart
  gebrond binnen budget.
- **`ag-garpenberg-mijn` wijkt ~600 m af van het bestaande sitelaag-anker** `w-garpenberg` (60.3158,16.1983,
  OSM-dorpscentroïde, status aannemelijk in `zilver-sitelaag.md`) — deze brief gebruikt een preciezere,
  satelliet-bevestigde coördinaat op het industriële mijncomplex zelf. Centrale sync met de sitelaag wordt
  aanbevolen (niet zelf gedaan — sitelaag is niet mijn bestand).
- **Haven-aanloop bij Gävle nog niet gebakken** — kade ligt ~19,2 km van de dichtstbijzijnde MARNET-zeeknoop
  (8841, 60.74660/17.54600); ruim boven de 5 km-drempel (LAR-586), dus een haven-aanloop is verplicht.
- **Jaarvolume is het Garpenberg-totaal (bijproduct), niet uitgesplitst naar deze specifieke tak** — 260 t
  Ag/j is de mijn-brede schatting uit het ketenontwerp/sitelaag, niet een Rönnskär-specifiek cijfer.

## 8 · Bronnen
[1] Boliden, "Garpenberg NI 43-101 Technical Report" (Mineral Resources and Mineral Reserves, 2022-12-31,
via minedocs.com) — expliciete transportbeschrijving: Zn/Pb-concentraat per truck naar Gävle-haven en per
schip naar Boliden-smelters in Finland/Zweden/Noorwegen; Cu- en gravimetrisch concentraat per truck +
spoor naar Rönnskär. https://minedocs.com/24/Garpenberg-MR-12312022.pdf
[2] Boliden, "Boliden Garpenberg" (operations-pagina) — 2025: ≈3,6 Mton erts verwerkt tot Zn/Cu/Pb/Au/Ag-
concentraten. https://www.boliden.com/operations/mines/boliden-garpenberg/
[3] Boliden, "Boliden Rönnskär" (operations-pagina) — smelter ontvangt koper- en loodconcentraat van eigen
mijnen en externe leveranciers; locatiekeuze Skelleftehamn destijds mede vanwege haven + spoor.
https://www.boliden.com/operations/smelters/boliden-ronnskar/
[4] Boliden Garpenberg, "Biodiversity GRI Report 2021" (PDF) — dieselverbruikstabel noemt expliciet
"transport to Gävle and Smedjebacken" als onderdeel van het vervoer vanaf de mine.
https://www.boliden.com/48e71e/globalassets/sustainability/sustainability-2/biodiversity-and-reclamation/gri-reports/boliden-garpenberg-gri-report-2022-03-30.pdf
[5] Skillings.net, "Boliden Garpenberg Investment: SEK 5.5B Expansion" — SEK 4 mrd hijssysteem Garpenberg,
productiecijfers (4,5 Mton erts/j na uitbreiding); geen transportdetails. https://skillings.net/boliden-garpenberg-investment-sek/
[6] Ketenontwerp + haalbaarheidstoets (workflow-invoer, M31 golf 5) — jaarvolume ≈260 t Ag/j, bindende
correctie van spoor naar truck+zee, webcheck-aanwijzing (boliden.com/operations, miningweekly.com).
[7] OpenStreetMap (ODbL) via Nominatim — `landuse=industrial "Boliden"`, Finnhyttan/Garpenberg, Hedemora
kommun, 60.31293/16.19332. https://www.openstreetmap.org
[8] OpenStreetMap (ODbL) via Nominatim — `landuse=industrial "Rönnskärsverken"`, Skelleftehamn, Skellefteå
kommun, 64.67039/21.26993. https://www.openstreetmap.org
[9] OpenStreetMap (ODbL) via Nominatim — "Gävle Hamn" / Fredriksskans, Källhagen, Gävle kommun (haven- en
industriezone aan de Gävlefjärden). https://www.openstreetmap.org
[10] OpenStreetMap (ODbL) via Nominatim — plaatscoördinaten Hofors (60.54545/16.28552), Storvik
(60.58534/16.53503), Sandviken (60.62187/16.77600) — gebruikt voor de via-punten van been b1.
https://www.openstreetmap.org
[11] `v2/design/zilver-sitelaag.md` (M31 golf 2) — bestaande ankers `w-garpenberg` (60.3158,16.1983,
aannemelijk) en `w-ref-ronnskar` (64.6704,21.2699, aannemelijk), capaciteitsbron Boliden jaarverslag 2024.
[12] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15) —
`sat-zilver-garpenberg-ronnskar-mijn.png`, `sat-zilver-garpenberg-ronnskar-gavle-b.png`,
`sat-zilver-garpenberg-ronnskar-smelter.png` in `v2/build-cache/satcheck/`.
[13] Interne meting (`hecht_marnet.marnet_zee`, MARNET-preais) — dichtstbijzijnde zeeknoop per kade:
Gävle-kade → knoop 8841 (60.74660,17.54600) op 19,2 km; Rönnskär-kade → knoop 8833 (64.66680,21.30040) op
1,5 km.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**3 benen · 691,0 km · 1.783 punten · 3 markers.** Recept: `bash v2/tools/bak_stromen.sh
zilver-garpenberg-ronnskar` → `bak_zilver_garpenberg_ronnskar()` in `v2/tools/bak_stromen.sh`.

| # | modaliteit | km | punten | stippel? | naam |
|---|---|---|---|---|---|
| b1 | truck | 106,4 | 1.654 | nee | Garpenberg → Gävle-haven (Gästrikland via Hofors–Storvik–Sandviken) |
| b2 | zee | 22,2 | 69 | **ja** | haven-aanloop Gävle (schematisch, over water) |
| b3 | zee | 562,4 | 60 | nee | zeeschip Gävle-zeeknoop → Rönnskär-kade (Botnische Golf) |

**Naden tussen de benen: 0,00 km overal** (b1→b2 en b2→b3 sluiten exact aan — b2 begint waar b1
eindigt, op de Gävle-kade; b3 begint waar b2 eindigt, op zeeknoop 8841). Markers ag-garpenberg-mijn
en ag-gavle-kade liggen op 0,0 m van hun lijn; ag-ronnskar-kade op **1.505 m** — dat is *anker ≠
routeerpunt*, geen naad: de Rönnskär-kade zelf ligt 1,5 km van haar dichtstbijzijnde zeeknoop (8833,
binnen de 5 km-drempel, dus geen haven-aanloop verplicht per §2), en het zeebeen eindigt op die
zeeknoop, niet op de literaire kadecoördinaat.

**Profiel/functie:** nieuw profiel `zilver-garpenberg-ronnskar-garpenberg-gavle` in
`v2/tools/maak_stroombeen_weg.py` (extract `zweden`, reeds op schijf) + nieuwe functie
`bak_zilver_garpenberg_ronnskar()` in `v2/tools/bak_stromen.sh`. Geen letterlijke kopieën nodig —
eerste stroom die Garpenberg, Gävle of Rönnskär raakt.

**Toelichting per been:**
- **b1 (truck, doorgetrokken):** de wegscan vond de doorgaande weg via Hofors–Storvik–Sandviken zoals
  het profiel voorschreef; gemeten **105,7 km weggeometrie** (106,4 km getekend incl. de twee
  ankerverbindingsstukjes van 0,21 en 0,45 km) tegen de hemelsbrede 69,8 km uit de brief = **+51,5%**,
  ⚠️ **BUITEN de ±15%-indicatie maar geen bevinding die dichtgetrokken hoort te worden** — de brief
  zelf schrijft voor dat de ±15%-toets hier alleen als indicatie geldt (geen gepubliceerde wegkm), en
  een reële weg via drie tussenplaatsen op een noordwaartse boog is per constructie langer dan de
  rechte lijn. `eindKlassen` is in het profiel bewust gezet op `["residential","service","tertiary"]`
  **zonder** `"unclassified"` (zie de ⚠️-noot in het profiel zelf): met de default-eindklassen (incl.
  unclassified) snapte de Gävle-kade op een geïsoleerde stub-way (OSM-way 1111961047, eigen component
  van 5 knopen, 0,10 km van het anker maar zonder pad naar Sandviken) — gemeten met een BFS-
  componenttoets, niet aangenomen. Zonder "unclassified" blijft de hele keten één component en snapt
  Garpenberg alsnog op 0,21 km (via residential/tertiary bij de mijntoegang). Beide ankers liggen
  ≤0,45 km van het net → geen last-mile-stippel nodig. 15 spikes ≤42 m (junctie-artefacten), 0
  omkeringen, 0 terugloop (`toets_knikken.py`).
- **b2 (zee, stippel, haven-aanloop Gävle):** kade ligt 19,2 km van zeeknoop 8841 — ruim boven de 5
  km-drempel (LAR-586), dus verplicht óók al snapt de router binnen de 25 km.
  `maak_havenaanloop.py` slaagde op de vierde trap (cel 0,005° kaal): 22,2 km over 69 punten,
  omwegfactor 1,155, 0,19 km over land — uitsluitend aan het kade-uiteinde (de 1:10M-kustlijn kent de
  kade per definitie als land, geen fout), 0,00 km midden op de lijn. Geen tweede poging nodig.
- **b3 (zee, doorgetrokken):** MARNET-route Gävle-zeeknoop → Rönnskär-kade over de Botnische Golf,
  562,4 km over 60 punten, snap 0,000 km aan de Gävle-zijde (begint exact op de zeeknoop) en 1,505 km
  aan de Rönnskär-zijde (anker ≠ routeerpunt, zie boven). Eén krappe bocht (103,6°, straal 5.605 m) —
  een echte MARNET-routekeuze in de Botnische Golf, geen artefact.

**Toets:** `toets_knikken.py` 0 omkeringen/0 terugloop op beide modaliteiten; `toets_rechte_benen.py
--min-km 5` toont geen been van deze stroom (het stippel-been b2 heeft omwegfactor 1,155 ≠ 1,000,
dus terecht niet als "verzonnen rechte lijn" gevlagd); json.load slaagt, `versie == 2`,
`punt_formaat == "lonlat"`, modaliteiten {truck, zee} ⊂ de toegestane set, elk been ≥ 2 punten,
bestand 35,3 KB.

**Lessen:**
- **De sitelaag-mismatch bij `ag-garpenberg-mijn` (~600 m t.o.v. `w-garpenberg`) is niet zelf
  gecorrigeerd** — centrale sync met `v2/design/zilver-sitelaag.json` aanbevolen (buiten scope van
  deze bak-agent, raakt andermans bestand).
- **Welk concentraat (Zn of Pb) het zilver naar Rönnskär draagt is niet uitgesplitst** (brief §7) —
  niet apart gebrond binnen het webbudget van deze bake.
- **Een `eindKlassen`-lijst zonder "unclassified" kan een verplichte fix zijn, niet alleen een
  keuze** — deze klasse hoort bij dezelfde familie als de bestaande "snap > 5 km → wegklasse
  controleren"-regel, maar hier was het probleem geen grote snap-afstand (0,10 km, ruim binnen de
  norm) maar een KLEINE, verkeerde snap op een topologisch geïsoleerde stub. Een BFS-componenttoets
  op de gesnapte ankers (vóór de Dijkstra) had dit eerder kunnen vangen dan de "geen wegpad"-fout
  van `corridor_keten` — nuttig voor een volgende agent die dezelfde foutmelding ziet.
