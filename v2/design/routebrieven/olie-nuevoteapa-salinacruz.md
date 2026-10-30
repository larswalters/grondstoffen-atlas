# Routebrief (licht) · olie — Nuevo Teapa (Veracruz) → Oleoducto Nuevo Teapa–Salina Cruz → Salina Cruz (Mexico)

**stroom-id:** `olie-nuevoteapa-salinacruz` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** Ruwe olie uit het Pemex-pompstation Nuevo Teapa (Veracruz, Golfzijde) per **leiding** (Oleoducto Nuevo Teapa–Salina Cruz, 48 inch, Pemex Logística, sinds 1979) over de Isthmus van Tehuantepec naar de raffinaderij Ing. Antonio Dovalí Jaime in Salina Cruz (Oaxaca, Pacific-zijde); daar eindigt het bewijs.
**Welke as van het verhaal:** *de trans-isthmus-leiding: Golf-crude naar de Pacific-raffinage* (reserve-as). Leidingcapaciteit 500 kb/d (48 inch) [1]; werkelijke leidingdoorzet niet gebrond. Raffinaderij: capaciteit 330 kb/d [4][6] (360 kb/d ontwerp [3]), doorzet gem. ~208 kb/d jan–apr 2025 [5] en 207 kb/d in april 2026 [4]. Volume-eenheid kb/d.

## 1 · Ketenkaart
```
Nuevo Teapa-pompstation `ol-teapa-kop` (Moloacán, Veracruz)
   ──(b1 leiding · Oleoducto Nuevo Teapa–Salina Cruz 48", via Minatitlán-zone, Matías Romero, Isthmus ·
       265,0 km OSM-som, 7 ways, doorgetrokken, 0 stippel)──►
   OSM-einde / pomp-klepstation `ol-salinacruz-eind` (NW-rand van het raffinaderijcomplex)
   ··· 1,3 km, geen been (anker ≠ routeerpunt) ··· ► raffinaderij Salina Cruz `ol-salinacruz-ref` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Nuevo Teapa-pompstation → OSM-einde bij raffinaderij Salina Cruz | Oleoducto Nuevo Teapa–Salina Cruz (48", lijn 2; 30"-tweeling ligt parallel en wordt niet getekend) | eigen OSM-som 265,0; gepubliceerd 267 (GEM, lijn 2) [1] = −0,7%; hemelsbreed kop–eind 225 km | 7 OSM-ways, `man_made=pipeline` `substance=oil` `diameter=48"` `operator=Pemex Logística`, gestikt met `maak_leidingbeen_olie_nuevoteapa_salinacruz.py`, doorgetrokken | nee — geen enkel stuk stippel |
Naam van het been: "Oleoducto Nuevo Teapa–Salina Cruz (Pemex Logística, 48 inch) … (7 OSM-ways, gemeten, aannemelijk: geen leiding-in-bedrijf-bron, 30-inch-tweeling niet getekend)". Geen zeebeen: geen bron koppelt een lading of afnemer aan de marine terminal (§7).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-teapa-kop` | kop van de leiding (pompstation) | Nuevo Teapa-station, Pemex Logística | 18.0745, -94.3275 | [2] OSM-begin way 1284967366; substation-punt 18.0755,-94.3288 (way 1191523913, Pemex Logística); [7] dorp Nuevo Teapa 18.0750,-94.3197 | bron-gelegd (z16 gezien: Pemex-compound langs de snelweg met twee witte tanks en leidingmanifolds, het OSM-begin ligt aan de rand ervan, ~100 m) |
| `ol-salinacruz-eind` | einde van de leiding (pomp-/klepstation) | OSM-einde 48"-reeks, NW-rand raffinaderij Salina Cruz | 16.2201, -95.1845 | [2] OSM-einde way 1284967360 | aannemelijk (z16 gezien: punt ligt op de Transístmica-weg; 300 m ten zuiden een klein compound met vier witte tanks, daarachter tankenpark; geen eigen terrein op het punt zelf) |
| `ol-salinacruz-ref` | afnemer / raffinaderij | Raffinaderij Ing. Antonio Dovalí Jaime (Pemex), Salina Cruz | 16.2164, -95.1730 | [3][6]; eigen z14-blik | bron-gelegd (z14 gezien: dicht tankenpark met witte tanks en procesunits met rookpluim direct oostelijk van het kanaal; 767 ha complex [3]) |

## 4 · Via-punten (b1 is een gestikte OSM-lijn: geen routering, alleen controlepunten op de lijn)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | waygrens 1 (ketenkm 45,7) | 18.0045, -94.7360 | naad tussen way 1284967366 en 1284967364, kruising met het Cenagas-gasleidingtracé [2] |
| b1 | 2 | waygrens 2 (ketenkm 94,5) | 17.6526, -94.9902 | naad 1284967364 / 1378921297 (naad 13 m) [2] |
| b1 | 3 | waygrens 3 (ketenkm 119,0) | 17.4338, -95.0173 | korte koppelway 1378921298, stationspunt 17.4336/-95.0173 [2] |
| b1 | 4 | waygrens 4 (ketenkm 144,6) | 17.2114, -95.0471 | station (way 1284967363), naad 19 m [2] |
| b1 | 5 | waygrens 5 (ketenkm 199,9) | 16.7522, -95.0040 | station (way 1284967361) ten noorden van de laatste 65 km [2] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nuevo Teapa-pompstation | Pemex Logística | crude uit het Golfsysteem → leiding naar Salina Cruz | leiding 48" 500 kb/d (30"-lijn 240 kb/d) | [1] |
| Raffinaderij Salina Cruz | Pemex | crude → brandstoffen en stookolie (Pacific-kust); export crude en stookolie via de marine terminal, bronvermelding ontbreekt | 330 kb/d (360 ontwerp); ~208 kb/d jan–apr 2025; 207 kb/d april 2026; 124 kb/d mei 2026 (brand) | [3][4][5][6][9] |

## 6 · Stoppunt
De brief stopt bij de raffinaderij: de leiding heeft haar afnemer in de raffinaderij zelf, en geen bron koppelt een lading van de marine terminal aan één bestemming (alleen een algemene "Japan, VS, Singapore"-opgave zonder bron [3]); fase D en E vervallen, geen zeebeen.

## 7 · Open punten
- **Marine terminal (havenopslag, Terminal Marítima) niet gelegd:** OSM-leidingen en tanks bij 16.167,-95.203 (ca. 6 km ZW van de raffinaderij) horen daar waarschijnlijk bij; geen bron voor kade of lading, dus geen anker en geen been. Het ontwerp-eindpunt 16.167,-95.203 was deze havenopslag, niet de raffinaderij.
- **Leiding in bedrijf niet onafhankelijk bevestigd:** GEM noemt de status "operating", gebaseerd op een CRE-vergunning van 2015 [1]; OSM geeft alleen start_date 1979. Een zoekresultaat meldt een ruptuur op de lijn in februari 2026 bij Loma Larga (Oaxaca) [10] (alleen de samenvatting gelezen, niet de bron). Werkelijke doorzet en bron van de crude (Isthmus/Maya) zijn niet gebrond.
- **Twee parallelle lijnen (30" en 48")**: alleen de 48"-reeks is getekend; de 30"-reeks (ways 1284967367/59/69/70/68, 1378921299/1378921300) loopt in dezelfde corridor.
- **OSM-geometrie grof op stukken:** langste koorde 6,4 km; de lengtetoets (−0,7% tegen GEM) is de enige controle.
- **Leidingeinde ≠ raffinaderij-anker:** 1,3 km, binnen het complex dat deels aan weerszijden van een kanaal ligt; geen OSM-leiding voor dat stuk, geen stippel (korter dan 2 km).
- **Annualisering:** de doorzet van 208 kb/d is een partiële periode (jan–apr 2025) uit een nieuwsbericht, geen jaargemiddelde; een Pemex-jaarverslag is niet gevonden.
- v1-checklist en `olie-sitelaag.json` bevatten geen Salina Cruz of Nuevo Teapa: geen coördinaat om te hergebruiken.

## 8 · Bronnen
[1] Global Energy Monitor, "Nuevo Teapa-Salina Cruz Oil Pipeline" — lijn 1: 30", 267 km, 240 kb/d; lijn 2: 48", 267 km, 500 kb/d; beide 1979, operating, Pemex Logística; bron CRE-vergunning 2015-12-31. https://www.gem.wiki/Nuevo_Teapa-Salina_Cruz_Oil_Pipeline
[2] OpenStreetMap (ODbL), lokale Geofabrik-extract mexico, eigen pure-Python pbf-scan 2026-10-30: 7 ways van de 48"-reeks (`man_made=pipeline`, `substance=oil`, `operator=Pemex Logística`, `start_date=1979`), som 265,0 km, 466 punten; stationspunten (`pipeline=substation`). https://www.openstreetmap.org/way/1284967360
[3] es.wikipedia, "Refinería Ing. Antonio Dovalí Jaime" — start 1979, 767 ha, 56 procesgebieden, capaciteit 360 kb/d (werkelijk 260 kb/d), marine terminal exporteert (cita requerida). https://es.wikipedia.org/?curid=9955180
[4] OPIS, 2026-05-27, "Pemex Tula Boosts April Processing Runs…" — Salina Cruz 207.311 b/d (april 2026), 202.347 (maart 2026), 188.412 (april 2025), capaciteit 330.000 b/d. https://www.opis.com/resources/energy-market-news-from-opis/pemex-tula-boosts-april-processing-runs-while-dos-bocas-falls-to-43-capacity/
[5] SDP Noticias — Salina Cruz hoogste doorzet van de Pemex-raffinaderijen, 208.192 b/d jan–apr 2025. https://www.sdpnoticias.com/mexico/esta-es-la-refineria-que-mas-produce-en-mexico/
[6] Grupo Animal, 2026-02-03 — capaciteit Salina Cruz 330.000 b/d. https://grupoanimal.mx/explicaciones/refineria-dos-bocas-capacidad
[7] Nominatim (OSM), 2026-10-30 — dorp Nuevo Teapa, Moloacán 18.0750/-94.3197. https://nominatim.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16): `sat-olie-nuevoteapa-salinacruz-teapa-kop(-z16).png`, `…-salinacruz-eind(-z16).png`, `…-salinacruz-ref.png`.
[9] El Financiero, 2026-07-06 — Salina Cruz 123,9 kb/d in mei 2026 (−40,2%). https://www.elfinanciero.com.mx/nacional/2026/07/06/pemex-rompe-racha-refinacion-de-crudo-cae-por-debajo-del-millon-de-barriles-diarios-en-mayo/
[10] N+, 2026-02-10 — explosie en brand op een Pemex-leiding in Oaxaca (samenvatting via zoekresultaat). https://www.nmas.com.mx/nacional/seguridad/explosion-ducto-pemex-hoy-10-de-febrero-2026-muertos-heridos-oaxaca-que-paso/

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-olie-nuevoteapa-salinacruz.json` (10,7 KB, versie 2, lonlat) · **1 been · 265,0 km · 466 punten · 3 markers** · naden n.v.t. (één been).
Recept: `bak_olie_nuevoteapa_salinacruz()` in `v2/tools/bak_stromen.sh` (één `--been-geojson leiding`, 3 markers, geen zee/MARNET-routering, geen aanloop, geen stippel); geometrie vooraf gestikt met `python v2/tools/maak_leidingbeen_olie_nuevoteapa_salinacruz.py --schrijf` (7 OSM-ways uit de extract mexico) naar `v2/build-cache/ais/graaf/olie-nuevoteapa-salinacruz-leiding-isthmus.geojson` (FeatureCollection, één LineString).
| # | modaliteit | km gemeten | km brief | afwijking | stijl |
|---|---|---|---|---|---|
| b1 | leiding (48 inch, Pemex Logística) | 265,0 | 267 (GEM lijn 2) | -0,7% | doorgetrokken |
Markers: `ol-teapa-kop` (18.0745, -94.3275; 6 m van de lijn), `ol-salinacruz-eind` (16.2201, -95.1845; 7 m) en `ol-salinacruz-ref` (16.2164, -95.1730; 1,30 km van het leidingeinde: anker ongelijk routeerpunt, bewust geen last-mile-been, korter dan 2 km).
**Toelichting:** het hele been is een OSM-leiding (`man_made=pipeline`), dus doorgetrokken; geen stippel, geen haven-aanloop, geen vlucht, geen via-punten (de vijf waygrenzen in §4 zijn controlepunten, geen routering), geen gedeeld been, geen wegscan. Het werkelijke eindpunt is het OSM-einde bij de raffinaderij Salina Cruz (zoals het id belooft); de havenopslag uit het ontwerp is niet gelegd. De 30-inch-tweeling is niet getekend. Status aannemelijk: geen leiding-in-bedrijf-bron.
**Toetsen:** km -0,7% tegen GEM; `toets_knikken.py` 0 knikken, 0 omkeringen, 0 terugloop; `toets_rechte_benen.py` meldt dit been niet; json.load ok, versie 2, punt_formaat lonlat, modaliteit leiding, 466 punten, 10,7 KB; `bak_stromen.sh` blijft LF (0 CRLF), `bash -n` ok.
**Lessen:** een OSM-leiding van 7 ways is in één script te stikken en daarna zonder routering te bakken (nybro- en IGB-patroon); een leidingeinde dat 1,3 km van het afnemer-anker ligt blijft zonder last-mile-been, met de afstand in de markernaam en §9 benoemd.
