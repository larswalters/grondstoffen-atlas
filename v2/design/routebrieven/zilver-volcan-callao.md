# Zilver · Chungar (Volcan) → PE-20A via Canta → Callao (Peru)

**stroom-id:** `zilver-volcan-callao` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) ·
**status:** gebakken
**Keten in één zin:** Pb-Zn-Ag-concentraat van het Chungar-complex (Volcan, plant Animón, Huayllay, Pasco) per **truck**
over de PE-20A (Carretera Vencedores de Sángrar: Huayllay, Abra La Viuda, Canta, Yangas, Punchauca, Av. Túpac Amaru) naar
de mineraalterminal van Transportadora Callao (TCSA) in de haven van Callao (aannemelijk: één bron, oud). Stoppunt Callao.
**Welke as van het verhaal:** Peru-hoogland, Volcan-eenheid zonder eigen keten. Chungar 1,7 Moz Ag in 2024 = ca. 52,9 t Ag/j
(peiljaar 2024, jaarverslag [1]); heel Volcan 13,9 Moz = ca. 432 t Ag/j (2024, [1][2]), 2025 13,5 Moz [2]. Eigenaar sinds mei 2024
Transition Metals (Integra Capital), eerder Glencore [1][3].

## 1 · Ketenkaart
```
Chungar-complex/Animón `ag-chungar-mijn` ──(b1 truck · PE-20A Huayllay–Canta–Yangas–Túpac Amaru · hemelsbreed ~137 km,
   geen wegkm; Lima–Chungar 219 km [1])──► Transportadora Callao-terminal `ag-callao-tcsa` ── stoppunt
```
Eenheid Yauli (Junín) bewust niet gekozen: San Cristóbal-Carahuacra en Ticlio lagen maart-april 2024 stil [2]; Chungar is het
sterkere, bron-gelegde anker. Geen spoorbeen: het Volcan-spoor/FCCA staat in [6] alleen als algemene route, niet voor Chungar.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Chungar/Animón → TCSA-terminal Callao | PE-20A: Huayllay, Abra La Viuda, Canta, Yangas, Punchauca, Av. Túpac Amaru, dan Naranjal/Canta-Callao [3][4][5] | hemelsbreed ~137 km, geen wegkm; indicatie 219 km Lima–Chungar [1] (Callao komt erbij); proeftoets 206,2 km = −5,8% | maak_stroombeen_weg (extract `peru`) | nee |

Haalbaarheidstoets (proefrun profiel `zilver-volcan-callao-chungar-tcsa`): 206,2 km, 5.466 punten, alle snaps ≤ 0,18 km, 1 keerpunt
(151°, Canta-westrand). Geen zeebeen: Callao is stoppunt (TCSA-kade ligt 60,7 km van MARNET-zeeknoop 394, relevant bij een latere fase B).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-chungar-mijn` | mijn / laadplek | Chungar-complex met plant Animón (Volcan), Huayllay, Pasco | -11.0307, -76.4237 | [1][5][8] | bron-gelegd (z14 en z15 gezien: kruis op de verwerkingshallen met blauwe daken, direct ten NW van een grote lichtgrijze tailingsdam met turkoois bekken; mijnwegen, groene meren en dagbouw-achtige gronden noordelijk; geen leeg terrein) |
| `ag-callao-tcsa` | overslag / exportpunt (stoppunt) | Transportadora Callao S.A., mineraalterminal (muelle centro), Callao | -12.0499, -77.1446 | [7][9] | bron-gelegd, letterlijk hergebruikt uit `zilver-uchucchacua-callao.md` (z18 daar: bulkcarriers aan eigen kade tussen twee containerterminals) |

## 4 · Via-punten (b1, landbeen met corridorkeuze, lat, lon)
Allemaal vertices van PE-20A-ways in OSM (Overpass), niet in een stadscentrum. Als (lon, lat) al in het profiel gezet.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | PE-20A bij Chungar/Huayllay | -11.0423, -76.4004 | 2,85 km van het anker; pint de Canta-corridor in plaats van Cerro de Pasco naar de Carretera Central/La Oroya [3][4] |
| b1 | 2 | PE-20A bij Canta (westrand) | -11.4779, -76.6370 | Carretera Vencedores de Sángrar langs, niet door het centrum (Av. 26 de Junio, eenrichting) [4][5] |
| b1 | 3 | PE-20A bij Yangas | -11.6558, -76.7864 | Chillón-vallei richting Santa Rosa de Quives [4] |
| b1 | 4 | PE-20A bij Punchauca | -11.7172, -76.9493 | laatste punt vóór de Lima-agglomeratie [4] |
| b1 | 5 | Av. Túpac Amaru | -11.8399, -76.9992 | pint het oude PE-20A-tracé Túpac Amaru, Naranjal en Canta-Callao in plaats van Chimpu Ocllo/Trapiche naar PE-1N (refs PE-20A, PE-20, PE-1N) [4] |
Geofabrik-regio: `peru`. In het profiel `corridorKlassen` tertiary + unclassified en `eindToegangPrivaat` (havenzone, zoals uchucchacua/caylloma).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Planta Animón (Chungar) | Volcan Compañía Minera | erts Animón (1,0 Mt in 2024, 1,9 oz Ag/t) → Zn-, Pb-, Cu-concentraat | 5.200 tpd (ampliatie 2013); 2024 gemiddeld 2.800 tpd gemaakt | [1] |

## 6 · Stoppunt
Callao-TCSA is de exportkade; geen bron noemt de overzeese smelter of afnemer van het Chungar-concentraat, dus de lijn eindigt waar
het bewijs eindigt (vergelijkbaar met `zilver-uchucchacua-callao` en `zilver-caylloma-callao`).

## 7 · Open punten
- **Bestemming Callao: één oude bron.** [6] zegt dat Volcan force majeure declareerde omdat regen vervoer van concentraten per spoor en weg naar Callao stopte (zoekresultaat, pagina gaf 403, datum niet gelezen, naar schatting 2017). Het jaarverslag 2024 noemt wel concentraattransport per hermetische truck en wagon [1] maar geen haven. Dus aannemelijk, niet bevestigd; staat in de beennaam.
- **Km:** geen Callao-wegkilometer gepubliceerd. 219 km is Lima–Chungar (jaarverslag), de proefrun meet 206,2 km en volgt de Canta-route; de 219 kan de Carretera Central-route zijn. Dit is dus een indicatie, geen norm.
- **Volume per concentraat:** het Chungar-zilver (52,9 t Ag/j) zit verdeeld over Zn-, Pb-, Cu-concentraat; welk deel naar Callao gaat, is onbekend. 2024 was door een stop van Animón (fataal ongeval maart, ramp-up april) en Islay een laag jaar: Chungar-zilver −22,6% [1][2].
- **Sitelaag mist Volcan/Chungar:** `zilver-sitelaag.json` en `data/silver.js` hebben geen Volcan-rij; centraal een site `-11.0307, -76.4237` (53 t Ag/j, 2024) toevoegen. Niets gewijzigd.
- **Corridor 2022:** de truck met 30 t zinkconcentraat die in de Río Chillón viel (Canta-Huayllay-Cerro de Pasco) bevestigt dat de PE-20A met concentraat bereden wordt [3].
- **Mijnweg:** 6,5 km van het anker naar de PE-20A (anker-snap 0,18 km); het eerste stuk loopt over een mijnweg, geen last mile-stippel nodig.
- **Eindpunt Callao** ligt in de afgesloten havenzone (`eindToegangPrivaat`, 0,48 km last mile over service/unclassified).

## 8 · Bronnen
[1] Volcan Compañía Minera, Memoria Anual 2024: Chungar 219 km ten oosten van Lima, 1,7 Moz Ag en 1,0 Mt erts in 2024 (p. 39-40), plant Animón 5.200 tpd (p. 13), concentraat per hermetische truck en wagon, transportkosten US$14,5 MM (p. 109, 233), Transition Metals (p. 5, 14). https://minedocs.com/28/Volcan-AR-2024.pdf
[2] Volcan, Análisis y Discusión de la Gerencia 4T24: 13,9 MM Oz Ag in 2024 (15,2 in 2023), Chungar-zilver −22,6%, stilstand San Cristóbal, Ticlio en Animón in 1S24. https://proactivo.com.pe/wp-content/uploads/2025/02/Analisis-y-discusion-de-la-gerencia-4T24.pdf
[3] es.wikipedia, Volcan Compañía Minera: eigendom (Transition Metals 55% Klasse A, mei 2024), eenheden Chungar/Yauli, truckongeval 2022 in de Río Chillón. https://es.wikipedia.org/wiki/Volcan_Compa%C3%B1%C3%ADa_Minera
[4] es.wikipedia, Ruta nacional PE-20 A (Carretera Vencedores de Sángrar): 257 km, tracé Trapiche, Túpac Amaru, Carabayllo, Punchauca, Yangas, Canta, Abra La Viuda, Huayllay, Cochamarca, Villa de Pasco. https://es.wikipedia.org/wiki/Ruta_nacional_PE-20_A
[5] OpenStreetMap (ODbL) via Overpass (191 ways ref PE-20A) en Nominatim ("Mina Chungar" -11,0307/-76,4237; Huayllay; Canta). https://www.openstreetmap.org
[6] RumboMinero, "Volcan declara que no podrá cumplir con despachos de minerales" (force majeure, regen, concentraat naar Callao per spoor en weg; alleen als zoekresultaat gelezen). https://www.rumbominero.com/peru/noticias/mineria/volcan-declara-que-no-podra-cumplir-con-despachos-de-minerales/
[7] PortalPortuario, TCSA concentreert vracht uit Junín, Pasco, Ayacucho, Huancavelica en Lima-noord (via `zilver-uchucchacua-callao.md` [7]). https://portalportuario.cl/en-puerto-de-el-callao-se-construye-el-mayor-deposito-de-minerales-del-mundo/
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14, z15, live): `v2/build-cache/satcheck/sat-zilver-volcan-callao-chungar-z14.png`, `sat-zilver-volcan-callao-chungar-z15.png`.
[9] Hergebruikt anker Callao-TCSA: `v2/design/routebrieven/zilver-uchucchacua-callao.md` (z18), ook in `zilver-caylloma-callao.md`.
[v1] `data/silver.js` en `v2/design/zilver-sitelaag.json`: geen Volcan-site (gecontroleerd, niet gewijzigd).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Bestand:** `v2/data/stroomroute-zilver-volcan-callao.json` (117,0 KB, contract versie 2, punt_formaat lonlat). Functie `bak_zilver_volcan_callao` in `v2/tools/bak_stromen.sh`, profiel `zilver-volcan-callao-chungar-tcsa` in `maak_stroombeen_weg.py`.
| been | modaliteit | km gemeten | punten | brief | afwijking |
|---|---|---|---|---|---|
| b1 truck Chungar/Animón → TCSA Callao (PE-20A, aannemelijk: één bron) | truck (doorgetrokken) | 206,5 | 5.466 | 219 km Lima–Chungar (indicatie, geen Callao-wegkm) | −5,7% (indicatie, niet norm) |
Totaal 206,5 km, 2 markers (`ag-chungar-mijn`, `ag-callao-tcsa`), geen stippel, geen zeebeen, geen aanloop, geen lucht, geen kopie.
**Recept:** `wegscan_puur.py --profiel zilver-volcan-callao-chungar-tcsa` (extract peru) leverde `v2/build-cache/ais/graaf/zilver-volcan-callao-weg-chungar-tcsa.geojson` (FeatureCollection, 1 LineString); daarna `bash v2/tools/bak_stromen.sh zilver-volcan-callao` (zwaar-slot) met één `--been-geojson truck|…` en twee markers. Via-punten 5 op PE-20A-vertices: segmenten 6,5 / 95,9 / 31,0 / 23,7 / 16,2 / 34,5 km, alle snaps ≤ 0,18 km (laatste 0,05 km in de havenzone).
**Toets:** geen naad (één been); beide markers 0,0 km van de lijn; `toets_knikken`: 21 knikken ≥ 60 gr, 0 omkeringen, 0 terugloop (alle spikes op 7–64 m, wegbochten bij Animón en in Callao); `toets_rechte_benen --min-km 5`: geen recht been; json.load ok (versie 2, lonlat, modaliteit truck, 5.466 punten).
**Toelichting:** geen stippel nodig; mijnweg 6,5 km van het anker naar de PE-20A is gewone weg (geen last mile). Eindpunt Callao ligt in de afgesloten havenzone (0,48 km over service/unclassified). Geen haven-aanloop: er is geen zeebeen (TCSA 60,7 km van MARNET-knoop 394).
**Lessen / open:** (1) de 206,5 km is de gemeten Canta-route; de 219 km uit het jaarverslag is Lima–Chungar en kan de Carretera Central-route zijn, dus geen harde norm. (2) Sitelaag en `silver.js` missen Volcan/Chungar: centraal een site toevoegen (-11.0307, -76.4237, 53 t Ag/j, 2024). (3) Bestemming Callao blijft aannemelijk (één oude bron). Niets in sitelaag, register of bundel gewijzigd.
