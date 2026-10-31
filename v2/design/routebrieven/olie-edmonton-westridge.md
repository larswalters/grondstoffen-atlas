# Routebrief (licht) · Olie · Edmonton → Trans Mountain Pipeline → Westridge Marine Terminal (Canada)

**stroom-id:** `olie-edmonton-westridge` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** Canadese ruwe olie (oliezand-crude) per **pijpleiding** (Trans Mountain Pipeline, TMPL plus de TMX-uitbreiding van mei 2024)
van de Edmonton-kant (Strathcona County, Alberta) over de Anchor Loop bij Jasper, Blue River, Kamloops en Hope naar de **Westridge Marine Terminal**
in Burnaby (BC). De keten eindigt bewust bij de terminal: de lading gaat daarvandaan per tanker naar de VS-westkust en Azië (zie `olie-westridge-ulsan`).
**Welke as van het verhaal:** de bronkant van `olie-westridge-ulsan` (Alberta → Pacifische kust). Volume: **761 kb/d** gemiddelde doorvoer in 2025
(86% van de 890 kb/d ontwerpcapaciteit; 2024: 555 kb/d), Trans Mountain [2], peiljaar 2025; dat is doorvoer van het hele systeem, ook raffinaderijproducten.

## 1 · Ketenkaart
```
Edmonton Terminal (Trans Mountain, Strathcona County) -- NIET gelegd: tankenpark niet in OSM, lijn begint bij het OSM-pijpeinde
OSM-pijpeinde Edmonton `ol-edmonton-pijpeinde` (53.4976, -113.4187, onzeker)
  ──(b1 leiding · TMPL + TMX via Gainford, Anchor Loop (Jasper), Blue River, Kamloops, Hope · 1.143,1 km OSM-gestikt,
      tegen 1.180 km gepubliceerd [2], -3,1%)──►
pijpeinde Westridge (49.2908, -122.9503) ──(b2 leiding, stippel · last mile 0,5 km, steiger/trestle niet gekarteerd)──►
Westridge Marine Terminal `ol-westridge-term` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | OSM-pijpeinde Edmonton → pijpeinde Westridge | Trans Mountain Pipeline (TMPL) en TMX; Anchor Loop bij Jasper | 1.143,1 km OSM-gestikt; gepubliceerd "meer dan 1.180 km" [2], Wikipedia 1.150 km [1] (hemelsbreed 809 km; leidinglengte, geen wegkm) | OSM-pipeline, 29 ways, Dijkstra (`maak_leidingbeen_olie_edmonton_westridge.py`) | nee (twee bruggen 0,54 en 0,68 km) |
| b2 | A | leiding | pijpeinde Westridge → Westridge-kade-anker | — | 0,49 km (gemeten) | rechte lijn | ja: last mile, steiger en trestle niet gekarteerd |

Aannemelijk-status: geen. Dat deze leiding Edmonton met Westridge verbindt staat bij meerdere bronnen gelijk [1][2][3]; onzeker is alleen de exacte Edmonton-kop (§3).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-edmonton-pijpeinde` | kop van de leiding (vervangt de Edmonton Terminal) | OSM-pijpeinde van Trans Mountain Pipeline (way 352856671) in Edmonton | 53.4976, -113.4187 | OSM [7]; haalbaarheidstoets | **onzeker** (z15 gezien: industriegebied met loodsen langs een spoor-/verbindingsbaan, geen tankenpark; de Edmonton Terminal zelf ligt ca. 7 km verder NO in Strathcona County, niet gelegd) |
| `ol-westridge-term` | stoppunt / zeeterminus | Westridge Marine Terminal, Burrard Inlet, Burnaby BC | 49.2932, -122.9560 | **hergebruikt** letterlijk uit `olie-westridge-ulsan.md` §3 [4][8] | bron-gelegd (daar z17; hier herbevestigd op z16: twee tankers aan twee dolfijnen-berths, trestle naar de wal) |

Het OSM-pijpeinde van b1 aan de Westridge-kant (49.2908, -122.9503) ligt op z16 op de kop van de wal-pier naast de trestle, 0,49 km van het anker [8].
Niet gebruikt: Westridge Lateral (Pembina, ca. 1 km, andere leiding) en de Puget Sound-tak "Border to Burlington" (VS).

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
*Geen via-punten: een pijpleiding volgt een aangelegde buis, en de lijn is OSM-geometrie. Controlepunten (afstand tot de gestikte lijn, km vanaf de kop) uit OSM-pompstations [7]:*
Gainford 0,17 km (km 92) · Anchor Loop west (Jasper-zijde) 0,10 km (km 366) · Yellowhead 0,06 km (km 400) · Hargreaves 0,03 km (km 461) · Blue River 0,05 km (km 581) ·
Kamloops-terminal 0,23 km (km 815) · Kingsvale 0,04 km (km 916) · Sumas-tankpark 0,45 km (km 1.077) · Burnaby-terminal 0,20 km (km 1.140). Parallelle lijnen (TMPL, TMX, Anchor Loop) liggen in dezelfde corridor; de lijn kiest per stuk de kortste way.

## 5 · Verwerkingsknopen
*Geen eigen knoop: de Edmonton Terminal (20 gereguleerde tanks van 2,9 mln vat plus 15 handelstanks van 5,1 mln vat [5]) en het Kamloops- en Sumas-tankpark zijn tank- en pompknopen op dezelfde leiding, geen overslag naar een andere drager; de Westridge Marine Terminal is het stoppunt.*

## 6 · Stoppunt
De brief stopt bij Westridge: daar gaat de olie van pijpleiding naar tanker, en de bestemming per lading (VS-westkust of Azië) staat in `olie-westridge-ulsan`; Fase C/D/E vervallen.

## 7 · Open punten
- **Edmonton Terminal niet gelegd.** Trans Mountain noemt hem "Strathcona County, bij Edmonton" [5]; OSM heeft de tanks niet en het OSM-pijpeinde (53.4976, -113.4187) ligt in industriegebied zonder tankenpark. Er is geen coördinaat voor de terminal gevonden (transmountain.com gaf 403), dus de lijn eindigt waar OSM eindigt: de eerste ca. 7 km richting de terminal ontbreken (indicatie, niet gemeten). Een latere ronde kan het tankenpark leggen (Refinery Row, ca. 53.55, -113.36, ongelegd).
- **Geen wegkilometer-toets mogelijk**: de lengte is leidinglengte; 1.143,1 km OSM tegen 1.180 km (Trans Mountain [2]) en 1.150 km (Wikipedia [1]); de verschillen komen uit het ontbrekende Edmonton-stuk en uit kortere ways.
- **Parallelle lijnen**: de gestikte lijn is de corridor, niet bewezen de buis TMX of TMPL zelf; in OSM wisselen naam en operator ("Corperation", Midway/Midwest Pipelines als aannemer, naamloze ways 98238972 en 200617517).
- **Volume is systeemdoorvoer**: 761 kb/d in 2025 omvat ook producten; nominale capaciteit 890 kb/d [2]; Westridge laadt hooguit 630 kb/d [3].
- **Alleen een deel van de Westridge-lading gaat naar Azië**: 67% van de in 2025 geladen schepen ging naar Azië volgens Trans Mountain [2][6]; de rest naar de VS-westkust.

## 8 · Bronnen
[1] Wikipedia, "Trans Mountain pipeline" — 1.150 km, TMX operationeel 1 mei 2024, 300.000 → 890.000 vat/dag. https://en.wikipedia.org/wiki/Trans_Mountain_pipeline
[2] Trans Mountain, "Q4 2025 Financial Fact Sheet" — 761.000 vat/dag gemiddeld in 2025 (86%), 555.000 in 2024, 304 schepen geladen in 2025, meer dan 1.180 km leiding, drie berths. https://docs.transmountain.com/Corporate-Reports/Q4-2025-Financial-Fact-Sheet-EN.pdf
[3] Canada Energy Regulator, "Market Snapshot: Trans Mountain Expansion eases pipeline constraints…" (2025) — Westridge tot 630 kb/d, gemiddeld 23 schepen per maand, doorvoer 704 kb/d (juni 2024) en 793 kb/d (maart 2025). https://neb-one.gc.ca/en/data-analysis/energy-markets/market-snapshots/2025/market-snapshot-trans-mountain-expansion-eases-pipeline-constraints-and-increases-exports-to-overseas-markets.html
[4] `v2/design/routebrieven/olie-westridge-ulsan.md` §3 — Westridge-anker 49.2932, -122.9560, bron-gelegd z17.
[5] Trans Mountain, "Edmonton Terminal" (pagina niet te openen, 403; alleen via zoekresultaat gelezen) — terminal in zwaar-industrieel gebied in Strathcona County, 20 gereguleerde tanks (2,9 mln vat) plus 15 handelstanks (5,1 mln vat). https://www.transmountain.com/edmonton-terminal
[6] Trans Mountain, Q4 2025-presentatie (alleen via zoekresultaat gelezen) — 67% van de schepen naar Azië in 2025. https://docs.transmountain.com/Corporate-Reports/Q4-2025-Presentation.pdf
[7] OpenStreetMap-bijdragers (ODbL), Geofabrik-extract `canada` (2026-07-20), scan van man_made=pipeline substance=oil en Trans Mountain-benoemde objecten door `maak_leidingbeen_olie_edmonton_westridge.py`: 181 pijp-ways in de bbox, 29 op het pad. https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py`: `sat-olie-edmonton-westridge-edmonton.png` (z15, pijpeinde Edmonton), `sat-olie-edmonton-westridge-strathcona-ov.png` (z14, Refinery Row), `sat-olie-edmonton-westridge-westridge-pijpeinde.png` en `…-westridge-anker.png` (z16).
[9] Haalbaarheidstoets golf 18 (binnen deze run) — Dijkstra over 39 ways, 1.143,5 km; hier opnieuw uitgevoerd en bevestigd (1.143,1 km, 29 ways).

## 9 · Gebakken

**Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)** · `v2/data/stroomroute-olie-edmonton-westridge.json` (67,9 KB, versie 2, punt_formaat lonlat) · herbakken: `bash v2/tools/bak_stromen.sh olie-edmonton-westridge`.

| been | modaliteit | km | punten | lijnstijl |
|---|---|---|---|---|
| Trans Mountain Pipeline (TMPL plus TMX), Edmonton naar Westridge (OSM-gestikt) | leiding | 1143,1 | 3156 | doorgetrokken |
| last mile Westridge-kade (schematisch, steiger en trestle niet gekarteerd) | leiding | 0,5 | 2 | stippel |

Totaal 1143,6 km, 2 benen, 2 markers (`ol-edmonton-pijpeinde` 53.4976,-113.4187; `ol-westridge-term` 49.2932,-122.9560). Naad tussen de benen 0,00 km.

**Recept:** b1 uit `python v2/tools/maak_leidingbeen_olie_edmonton_westridge.py --schrijf` (OSM man_made=pipeline, 29 ways, Dijkstra, FeatureCollection `olie-edmonton-westridge-leiding-tmpl.geojson` in build-cache/ais/graaf); b2 als `--stippel` in `bak_olie_edmonton_westridge()`. Geen zee, haven-aanloop, weg, kopie of lucht.

**Toelichting stippel:** b2 is een rechte last mile van 0,49 km van het OSM-pijpeinde op de wal-pier naar het Westridge-anker; de steiger en trestle staan niet in OSM. Het gemeten leidingbeen b1 is doorgetrokken (twee bruggen van 0,54 en 0,68 km zitten er als OSM-geometrie in).

**Toets:** leidinglengte 1143,1 km tegen 1180 (Trans Mountain, -3,1%) en 1150 (Wikipedia, -0,6%); geen naad > 5 km; markers op de lijn (kop 0 km, terminal aan het stippeleinde); toets_knikken: 0 omkeringen en 0 terugloop, 47 knikken >= 60 gr (spikes op way-overgangen in OSM, geen reparatie nodig).

**Lessen:** (1) een lijn die begint waar OSM eindigt is eerlijker dan een verzonnen terminal: de Edmonton Terminal ontbreekt, ca. 7 km (indicatie); (2) parallelle lijnen (TMPL, TMX, Anchor Loop) zijn één corridor, niet één bewezen buis; (3) transmountain.com geeft 403, dus tankgegevens en 67% Azië komen alleen uit zoekresultaten.
