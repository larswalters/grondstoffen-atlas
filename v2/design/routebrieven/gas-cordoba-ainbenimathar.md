# Routebrief (licht) · gas — Córdoba (Spanje) → GME omgekeerd → Ain Beni Mathar (Marokko)

**stroom-id:** `gas-cordoba-ainbenimathar` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** Spaans, uit LNG hervergast net-gas (Enagás) gaat sinds juni 2022 in omgekeerde richting door de Maghreb-Europe-gasleiding
(GME): vanaf de Enagás-aansluiting bij Córdoba via Al-Andalus naar Tarifa, onder de Straat van Gibraltar en door Marokko (Pedro Durán Farell) naar de
ONEE-gascentrale Ain Beni Mathar (ISCC 472 MW); één doorgetrokken OSM-leidingbeen van 753,9 km plus een korte stippel last mile.
**Welke as van het verhaal:** de Maghreb-Europa-leiding omgekeerd: Spanje levert nu Marokko, waar tot 31-10-2021 Algerijns transitgas stroomde [1][2].
Jaarvolume **ca. 1,0 bcm/j** = 10.375 GWh in 2025 (Enagás-cijfer via de pers, +7%; eigen omrekening ca. 10,5-11 TWh per bcm; peiljaar 2025) [6];
jan-jul 2026 4,95 TWh (-13,7%) [3]; Tarifa-exportplafond 32 GWh/d [3]; jaarcapaciteit ca. 11.500 GWh [6]. De bol toont de route, niet de herkomst van de lading.

## 1 · Ketenkaart
```
Spaans LNG-net (Enagás, hervergast; herkomst per lading niet gebrond) ──► Córdoba-aansluiting `gas-cordoba-gme`
   ──(b1 leiding · Al-Andalus Tarifa-Córdoba 274,6 km · GME-Straat 35,7 km · Pedro Durán Farell Marokko ca. 443 km · OSM 12 ways · 753,9 km)──►
leidingeinde bij Ain Beni Mathar (34.0471,-2.1158) ──(b2 leiding · last mile 2,8 km, stippel)──► ONEE-centrale `gas-ainbenimathar-centrale` ⏹ stoppunt
(Tahaddart bij Tanger, 384 MW, 17,6 km van de lijn: onderweg afgenomen, niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-cordoba-gme` → leidingeinde Ain Beni Mathar | Gasoducto Al-Ándalus (Tarifa-Córdoba, Enagás) · GME-Straat (underwater) · Pedro Durán Farell (Marokko) | gemeten OSM 753,9; gepubliceerd Spanje 269 + Straat 45 + Marokko 522 tot de Algerijnse grens = 836 [1]; geen leidingkm tot ABM, dus indicatie (-9,8%) | OSM-ways gestikt, `maak_leidingbeen_gas_cordoba_ainbenimathar.py`, naden 0 m | nee: doorgetrokken |
| b2 | C | leiding | leidingeinde → `gas-ainbenimathar-centrale` | aansluitleiding (Wikipedia: 12,6 km pijp op de GME [4]) | 2,8 hemelsbreed | rechte stippel | ja: last mile, geen OSM-way |

**Beennaam b1:** "Tanger-Taza als OSM-ligging indicatief": way 578918617 (Tanger-Taza, 253 km, note=fixme, slechts 4 knopen: rechte koorden van 99,6 en 148,4 km) ligt tientallen km naast de werkelijke
tracé-route via Sidi Kacem en Fès; de leidinglengte is bruikbaar, de ligging niet. **Richting:** OSM kent geen stromingsrichting; de lijn is Córdoba → Marokko, de huidige richting.
Ways in volgorde (Spanje 274,6 km): 305990340, 777461438, 331405426, 331373354, 266007641, 331370590, 266354518, 264885392; Straat 265033883 (35,7); Marokko 265033635 (3,1), 578918617 (253,2), 229290151 (178,2) (geknipt op vertex 34.0471,-2.1158).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-cordoba-gme` | kop: aansluiting GME op het Enagás-net | Córdoba-aansluiting (Enagás-complex, 17 km ten oosten van de stad) | 37.9141, -4.5775 | [1][9] | bron-gelegd (z15 gezien: omheind installatieterrein met leidingwerk/afsluiters midden in olijf- en akkerland, aan een veldweg; punt = OSM-leidinguiteinde, geen operatordocument dat dit perceel de GME-aansluiting noemt) |
| `gas-ainbenimathar-centrale` | afnemer, stoppunt | ONEE-gascentrale Ain Beni Mathar (ISCC: 2 gasturbines 300 MW + stoom 172 MW + 20 MW zon, 2011) | 34.0706, -2.1038 | [4][9] | bron-gelegd (z15 gezien: omheind blok met krachtcentrale, koeltorens en een veld parabolische trogkollectoren van ca. 1 km breed, het kruis ligt op het machinehuis; Wikipedia 34.0683,-2.1047 ligt 0,3 km zuidwestelijk, in het zonneveld) |
| (routeerpunt) | leidingeinde b1 | OSM-uiteinde Pedro Durán Farell, woestijn zonder bebouwing | 34.0471, -2.1158 | [9] | geen anker: z15 gezien: open steppe, onverharde baan, droge rivierbedding; 2,8 km ZZW van de centrale |

Hergebruik: geen; Córdoba, Tarifa, Tahaddart en Ain Beni Mathar staan niet in `gas-sitelaag.json` of in andere gas-brieven.

## 4 · Via-punten
Niet van toepassing: leidingbeen uit aaneengestikte OSM-ways, geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Spaanse regasificatie en Tarifa-interconnectie | Enagás | LNG-ladingen (door Marokko gekocht) → net-gas, 29-31 GWh/d export, plafond 32 GWh/d | ca. 11.500 GWh/j; 2025: 10.375 GWh | [3][6][7] |
| Ain Beni Mathar (en Tahaddart) | ONEE | gas → stroom (ABM 472 MW; Tahaddart 384 MW, Tanger, Endesa/ONEE) | ABM gem. 3.538 GWh/j netto stroom | [2][4][5] |

## 6 · Stoppunt
De brief stopt bij de ONEE-centrale Ain Beni Mathar: de enige gedocumenteerde afnemer aan het Marokkaanse leidingeinde; verder is het stroom. Fase A (LNG naar Spaanse terminal) vervalt: de lading wordt per bron niet aan één terminal gebonden; fase D, E vervallen.

## 7 · Open punten
- **Ligging Tanger → Taza onbetrouwbaar:** way 578918617 (fixme, 4 knopen, koorden 99,6 en 148,4 km); de lijn wijkt tientallen km af van de echte route. Geen vervangende geometrie verzonnen.
- **Richting en herkomst:** OSM kent geen richting; invoeding kan via Tarifa uit meerdere Spaanse leidingen komen, Córdoba is een gekozen kop. LNG-herkomst (VS, Rusland, Shell) niet gebrond.
- **Volume is indicatie:** 10.375 GWh komt uit persberichten die Enagás citeren (Enagás zelf niet geraadpleegd); S&P Global-artikel [8] gaf HTTP 403. De bcm-omrekening is eigen.
- **Last mile b2 schematisch:** Wikipedia noemt een 12,6 km aansluitleiding [4]; geen OSM-way, werkelijke aftakking niet gevonden.
- **Tahaddart (35.5894,-5.9875)** ligt 17,6 km van de lijn en is niet getekend; Wikipedia-lijst noemt geen coördinaat; geen satellietblik.
- **Córdoba-anker** niet door een operatordocument bevestigd; **Wikipedia-coördinaat ABM** (list-pagina 36°N) is een typefout.
- **Sitelaag mist** Córdoba, ABM, Tarifa en Tahaddart (centraal aanvullen).

## 8 · Bronnen
[1] Wikipedia (EN), "Maghreb-Europe Gas Pipeline": 1.620 km; Marokko 522, Straat 45, Andalusië 269; 2021-stop; omkering juni 2022. https://en.wikipedia.org/wiki/Maghreb%E2%80%93Europe_Gas_Pipeline
[2] North Africa Post, "Algeria blocks Maghreb-Europe pipeline revival": ONEE koopt LNG, GME omgekeerd naar Tahaddart en Ain Beni Mathar; jan-aug 2025 6,73 TWh; transit gestopt 31-10-2021. https://northafricapost.com/92504-algeria-blocks-maghreb-europe-pipeline-revival-despite-european-pressure.html
[3] Morocco World News, aug 2026, "Gas flows from Spain to Morocco fall": jan-jul 2026 4,95 TWh (-13,7%), 20-31 GWh/d, plafond Tarifa 32 GWh/d. https://www.moroccoworldnews.com/2026/08/335911/gas-flows-from-spain-to-morocco-fall-nearly-a-third-since-last-week/
[4] Wikipedia (EN), "Ain Beni Mathar Integrated Thermo Solar Combined Cycle Power Plant": 472 MW, ONE, 2011, 12,6 km pijp op de GME, 34.06833,-2.10472. https://en.wikipedia.org/wiki/Ain_Beni_Mathar_Integrated_Thermo_Solar_Combined_Cycle_Power_Plant
[5] Wikipedia (EN), "List of power stations in Morocco": Tahaddart 384 MW, 2005, Tanger, Endesa/ONEE. https://en.wikipedia.org/wiki/List_of_power_stations_in_Morocco
[6] Spaanse/Engelse pers op Enagás-data (websearch): Marokko ontving 10.375 GWh in 2025 (+7%), 2024 9.703, 2023 9.471, capaciteit ca. 11.500 GWh/j. https://northafricapost.com/?p=94427
[7] H24info, 29-6-2022: eerste Spaanse levering 28-6-2022 naar Tahaddart en Ain Béni Mathar, via Tarifa, LNG door Marokko gekocht. https://h24info.ma/?p=594492
[8] S&P Global, 29-6-2022, "Spain begins gas re-exports to Morocco via GME" (HTTP 403, niet gelezen). https://spglobal.com/commodity-insights/en/news-research/latest-news/natural-gas/062922-spain-begins-gas-re-exports-to-morocco-via-gme-pipeline-enagas
[9] OpenStreetMap-bijdragers (ODbL), OSM-API 2026-10-31: de 12 ways; https://www.openstreetmap.org/way/265033883. Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-gas-cordoba-ainbenimathar-cordoba.png`, `-abm.png`, `-abmeind.png`.
[10] Hespress, "Spanish gas exports to Morocco through GME": 2022 1.430 GWh, Q1 2023 2.036 GWh, Enagás. https://en.hespress.com/62299-62299.html

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
`bash v2/tools/bak_stromen.sh gas-cordoba-ainbenimathar` (functie `bak_gas_cordoba_ainbenimathar`) -> `v2/data/stroomroute-gas-cordoba-ainbenimathar.json`, 12,8 KB, contract versie 2, punt_formaat lonlat.

| been | modaliteit | km | punten | geometrie |
|---|---|---|---|---|
| b1 | leiding, doorgetrokken | 753,9 | 604 | `--been-geojson` uit `maak_leidingbeen_gas_cordoba_ainbenimathar.py` (12 OSM-ways, FeatureCollection, naden 0 m) |
| b2 | leiding, stippel | 2,8 | 2 | `--stippel`, rechte lijn leidingeinde 34.0471,-2.1158 -> centrale 34.0706,-2.1038 |
Totaal 756,7 km, 606 punten, 2 markers.

**Markers:** `gas-cordoba-gme` 37.9141,-4.5775 (6 m van de lijn) en `gas-ainbenimathar-centrale` 34.0706,-2.1038 (0 m, eindpunt van b2). Het leidingeinde is routeerpunt, geen marker.

**Toets:** b1 753,9 km tegen 836 gepubliceerd (Spanje 269 + Straat 45 + Marokko 522 tot de Algerijnse grens) = -9,8%; dat getal reikt tot de grens, niet tot Ain Beni Mathar, dus een indicatie en geen ±15%-norm. Naad b1 -> b2 2,4 m. `toets_knikken.py`: 1 knik (62,4 gr, R 346 m, 34.2861,-3.1960), 0 omkeringen, 0 terugloop. Elk been >= 2 punten, modaliteiten {leiding}.

**Leiding:** b1 is geheel OSM (`man_made=pipeline`), geen eigen tekenwerk. Geen MARNET-zee, haven-aanloop, weg, via-punten, kopie of vlucht. De Straat (35,7 km) is een OSM-way over zee en dus doorgetrokken.

**Stippel b2:** hier reikt het net niet: geen OSM-way tussen leidingeinde en centrale; Wikipedia noemt een 12,6 km aansluitleiding, de 2,8 km is schematisch hemelsbreed.

**Bevindingen:**
- Way 578918617 (Tanger-Taza, fixme) heeft 4 knopen: rechte koorden van 148,4 km (vanaf 34.9621,-5.3008) en 99,6 km (vanaf 35.7422,-5.9377). De ligging wijkt tientallen km af van de werkelijke route via Sidi Kacem en Fes; de beennaam zegt "OSM-ligging indicatief". Geen vervangende geometrie verzonnen.
- Grootste segment daarna 21,7 km (Straat, 36.0046,-5.8832).
- `toets_rechte_benen.py` toont deze stroom pas nadat hij in het register staat.

**Lessen:** de functie stond al klaar uit een eerdere poging; de commandoregel was bij het opslaan tot een lange regel samengeklapt (geldig bash, onleesbaar) en is herschreven naar regels met backslash-voortzetting. LF, `bash -n` ok.
