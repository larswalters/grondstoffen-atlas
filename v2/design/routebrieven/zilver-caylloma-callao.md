# Zilver · Caylloma (Bateas) → Panamericana Sur → Callao (Peru)

**stroom-id:** `zilver-caylloma-callao` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) ·
**status:** gebakken
**Keten in één zin:** lood-zilverconcentraat van Caylloma (Minera Bateas, Fortuna, Arequipa) per **truck** over
Chivay, Yura, Camana, Chala, Nazca, Ica en Cañete (Panamericana Sur) naar de mineraalterminal van Transportadora
Callao (TCSA) in de haven van Callao (aannemelijk: één bron, Trafigura-afname). Stoppunt Callao.
**Welke as van het verhaal:** Zuid-Peru, kleine zilvermijn naar de exporthaven. Volume 911 koz Ag in 2018 = ca. 28 t Ag/j
(peiljaar 2018, technisch rapport 2019 [1]); recenter Caylloma-cijfer niet gevonden, het Fortuna-concern geeft voor 2026
alleen 0,8-1,0 Moz Ag over alle mijnen [3]. Lood-zilverconcentraat apart is niet gekwantificeerd.

## 1 · Ketenkaart
```
Caylloma/Bateas-plant `ag-caylloma-mijn` ──(b1 truck · Chivay-Yura-Camana-Chala-Nazca-Ica-Cañete · PE-1S ·
   ~1.235 km, som 225 + 1.009)──► Transportadora Callao-terminal `ag-callao-tcsa` ── stoppunt
```
Zinkconcentraat gaat naar Matarani en hoort niet in deze keten [2]. Alleen het lood-zilverconcentraat naar Callao.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Bateas-plant (Caylloma) → TCSA-terminal Callao | Chivay → Yura → Camana → Chala → Nazca → Ica → Cañete, PE-1S en PE-1N [6] | 1.235 (225 mijn-Arequipa [1][2] + 1.009 Arequipa-Lima [5]; som, geen enkele bron) | maak_stroombeen_weg (peru) | nee |

Haalbaarheidstoets: gemeten route 1.286,6 km = +3,8% op 1.235 (Wood Mackenzie noemt 1.460 km). Geen zeebeen: Callao is
het stoppunt, dus geen haven-aanloop nodig (TCSA-kade ligt 60,7 km van MARNET-zeeknoop 394, relevant als later een zeebeen volgt).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-caylloma-mijn` | mijn / laadplek | Bateas-plant, Caylloma-mijn (Fortuna), Arequipa | -15.2035, -71.8645 | [4][10] | bron-gelegd (z16 gezien: verwerkingsgebouwen en kantoren ca. 200 m oostelijk, tailings-bekken direct zuidelijk, toegangsweg langs het westelijk plantrand waar het kruis ligt; geen leeg terrein) |
| `ag-callao-tcsa` | overslag / exportpunt (stoppunt) | Transportadora Callao S.A., mineraalterminal (muelle centro) | -12.0499, -77.1446 | [7][8] | bron-gelegd, letterlijk hergebruikt uit `zilver-uchucchacua-callao.md` (z18 daar: bulkcarriers aan eigen kade tussen twee containerterminals) |

## 4 · Via-punten (b1, landbeen met corridorkeuze, lat, lon)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Chivay | -15.6381, -71.6009 | Colca-vallei: de weg van Caylloma naar Arequipa loopt via Chivay (toets) |
| b1 | 2 | Yura | -16.2506, -71.6786 | doorgaande weg Chivay-Arequipa langs de vulkaan; bovenlangs Arequipa-stad, niet door het centrum |
| b1 | 3 | Camaná | -16.6236, -72.7104 | Arequipa naar de kust: pint de PE-1S-kustcorridor in plaats van de route via Moquegua [6] |
| b1 | 4 | Chala | -15.8553, -74.2496 | kustweg PE-1S door de woestijn: sluit de Andes-route via Puquio uit [6] |
| b1 | 5 | Nazca | -14.8284, -74.9395 | PE-1S, enige doorgaande weg naar Ica [6] |
| b1 | 6 | Ica | -14.0678, -75.7283 | PE-1S, knoop Ica-vallei richting Lima |
| b1 | 7 | Cañete | -13.0783, -76.3906 | laatste punt op PE-1S vóór de Lima-agglomeratie; Lima zelf geen via-punt (router kiest de stadsdoorgang naar Callao) |
Via-punten komen uit de haalbaarheidstoets, die er een route van 1.286,6 km mee mat; in het profiel staan ze als (lon, lat).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Bateas-plant (Caylloma) | Minera Bateas / Fortuna Mining | erts → lood-, zink- (en koper-)concentraat | 2026-guidance ca. 550 kt erts, ca. 61 g/t Ag (toets-bron, zelf niet heropend) | [2][3] |

## 6 · Stoppunt
Callao-TCSA is de exportkade; geen bron noemt de overzeese smelter van het lood-zilverconcentraat (afname sinds 2018 door
Trafigura Peru volgens het technisch rapport 2023, concentraatcontracten zijn vertrouwelijk [1][2]), dus de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **Afnemer:** de lood-zilverconcentraten gaan sinds 2018 naar Trafigura Peru (TR 2019 en 2023), niet naar Glencore/AYSSA (dat is 2008). TCSA is deels van
  Trafigura-dochter Impala Peru; Callao-TCSA blijft dus aannemelijk, niet bevestigd: één bron [2], de TR 2019-passage over de afnemer [1] noemt hem niet (vertrouwelijk).
- **Km:** hier 1.235 als som van twee bronnen, geen enkele bron; de 225 km Arequipa-mijn staat in [1] (sec 1.2/5.1), de 1.009 km Arequipa-Lima is een kilometerteller-cijfer van een routesite [5] (de toets noemt Wikipedia, dat zelf alleen 1.234,52 km voor PE-1S Lima-Chili geeft [6]).
- **Volume:** peiljaar 2018, dus 7 jaar oud; zilverinhoud van alleen het Callao-deel onbekend (het zinkconcentraat, dat ook zilver draagt, gaat naar Matarani).
- **Huidige logistiek (2026)** niet bevestigd; Callao is al het stoppunt van `zilver-uchucchacua-callao` (geen overzeese bestemming).
- **Mijn-anker:** de UTM uit het technisch rapport 2023 (-15,1652, -71,8636) lag op z15 op leeg Andes-terrein; vervangen door OSM Minera Bateas (-15,2036, -71,8622) en de plantgebouwen op z16. Sitelaag niet gewijzigd.
- **Stadsdoorgang Lima:** geen via-punt; het wegtool kiest de doorgang van Cañete naar Callao.
- **Callao-eindpunt** ligt in de afgesloten havenzone: het wegbeen van `zilver-uchucchacua-callao` had daar eindToegangPrivaat nodig.

## 8 · Bronnen
[1] Fortuna Silver Mines, NI 43-101 technical report Caylloma Mine, 2019: 911 koz Ag in 2018 (tabel 6.3), 225 weg-km naar Arequipa, concentraat verkocht aan de open markt, contracten vertrouwelijk.
    https://www.sec.gov/Archives/edgar/data/1341335/000127956919000739/tv517002_ex99-1.htm
[2] Caylloma technical report 31-12-2023 (secties 17.2.3, 18, 19: Trafigura-afname, lood-zilver naar Callao, zink naar Matarani; via de haalbaarheidstoets, PDF te groot om te openen).
    https://minedocs.com/26/Caylloma-TR-12312023.pdf
[3] Fortuna Mining, mines and projects: 2026E zilver 0,8-1,0 Moz, concern totaal. https://fortunamining.com/mines-and-projects/
[4] OpenStreetMap (ODbL), Minera Bateas -15,2036/-71,8622 (via de toets) + Esri World Imagery z15/z16.
[5] Afstand Arequipa-Lima ca. 1.009,7 km. https://distancebetween2.com/arequipa/lima
[6] Wikipedia (ES), Ruta nacional PE-1S: Lima-Chili 1.234,52 km, secties Lima 175,5 · Ica 343,24 · Camaná/Arequipa 428,20 km.
    https://es.wikipedia.org/wiki/Ruta_nacional_PE-1S
[7] `v2/design/routebrieven/zilver-uchucchacua-callao.md`: anker `ag-callao-tcsa`, z18-blik, Wikipedia "Port of Callao" (muelle centro), PortalPortuario, Rumbo Minero.
[8] Wikipedia (EN), Port of Callao: terminal voor mineralenconcentraat van Transportadora Callao. https://en.wikipedia.org/wiki/Port_of_Callao
[9] Ketenontwerp en haalbaarheidstoets M31 golf 12 (workflow-invoer; risico: klein volume, bron uit 2019).
[10] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-zilver-caylloma-callao-bateas.png` (z15), `sat-zilver-caylloma-callao-bateas-z16.png` (z16), `sat-zilver-caylloma-callao-mijn.png` (eerdere UTM-poging).
[v1] `data/silver.js` en `design/zilver.md` bevatten geen Caylloma-record; sitelaag `zilver-sitelaag.json` niet gewijzigd.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
**Bestand:** `v2/data/stroomroute-zilver-caylloma-callao.json` (390,8 KB, versie 2, lonlat) · **recept:** `bash v2/tools/bak_stromen.sh zilver-caylloma-callao`
(functie `bak_zilver_caylloma_callao`, profiel `zilver-caylloma-callao-mijn-tcsa` in `maak_stroombeen_weg.py`, wegscan via `wegscan_puur.py`, extract peru).

| # | modaliteit | km | punten | naad | stippel |
|---|---|---|---|---|---|
| b1 | truck (doorgetrokken) | 1.286,7 | 18.335 | n.v.t. | nee |

- **Lengtetoets:** 1.286,6 km tegen 1.235 = **+4,2%** (binnen +-15%, maar de 1.235 is een som van twee bronnen, geen enkele bron: indicatie, geen harde norm). Segmenten: mijn-Chivay 112,5 · Chivay-Yura 121,8 · Yura-Camana 186,2 · Camana-Chala 222,4 · Chala-Nazca 171,1 · Nazca-Ica 148,3 · Ica-Canete 160,4 · Canete-Callao 165,1.
- **Snaps** van de via-punten 0,02-0,36 km (nooit > 5 km); geen via-punt verplaatst of verwijderd, geen omweg. Kleine-klasse-aanloop: 6,09 km first mile (service, tertiary), 2,05 km last mile (service, tertiary, unclassified); anker-verbindingen 0,02 en 0,05 km.
- **Markers:** 2 (`ag-caylloma-mijn` -15.2035,-71.8645 en `ag-callao-tcsa` -12.0499,-77.1446), beide 0,0 km van de lijn. Geen naden (een been).
- **Knikken:** 107 >= 60 graden, vrijwel allemaal spikes/haarspeldbochten in de Andes (Arequipa-Yura, Colca); 2 omkeringen (-13.1625,-76.3671 en -12.0328,-77.0545), beide "scherpe bocht, echt", 0 terugloop. `toets_rechte_benen`: geen treffer voor deze stroom.
- **Geen stippel, geen haven-aanloop, geen kopie:** een truckbeen, Callao is het stoppunt (TCSA-kade 60,7 km van MARNET-zeeknoop 394, pas relevant bij een later zeebeen).
- **Recept-afwijking t.o.v. de bak-aanwijzing:** `corridorKlassen ["tertiary"]` en `refs ["PE-1S","PE-1N"]` zoals voorgesteld; `eindKlassen` incl. track en `eindToegangPrivaat True` (kamp en afgesloten havenzone); venster 40 km. Scan 105 s.
- **Lessen:** (1) bestandsgrootte 391 KB ligt boven de ~300 KB-richtlijn (18.335 punten over 1.287 km), net als andere lange truckbenen: centrale bundel kan dit verdichten. (2) Open punten uit §7 blijven gelden (afnemer een bron, km een som, volume uit 2018, sitelaag niet gewijzigd).
