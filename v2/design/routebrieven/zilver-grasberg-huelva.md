# Routebrief (licht) · Zilver · Grasberg → Portsite → Atlantic Copper Huelva (Spanje)

**stroom-id:** `zilver-grasberg-huelva` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** Cu-Au-Ag-concentraat van de Grasberg-mill (PT Freeport Indonesia, Papoea) als slurry door de **leiding** (3 x 115 km, schematische stippel) naar Portsite/Amamapare, per **zeeschip** (Arafurazee, Banda, Indische Oceaan, Rode Zee/Suez, Middellandse Zee, Gibraltar) naar Puerto de Huelva, daarna per **truck** naar de Atlantic Copper-smelter, waar het zilver in de anodeslijmen belandt. **Eindpunt = aannemelijk: een bron** (FCX 10-K: 13 procent van Atlantic Coppers concentraat komt uit Indonesie; de losplek is afgeleid).
**Welke as van het verhaal:** *Papoea-concentraat naar de Freeport-smelter in Spanje.* Grasberg 190 t Ag in 2023 [1]; het deel naar Huelva is niet gepubliceerd, alleen het inkoopaandeel (13 procent van het Atlantic Copper-concentraat, 2024) [2]. Peiljaar 2023 (Ag) resp. 2024 (aandeel); 2026 lager na de modderstroom van sept 2025 [3].

## 1 · Ketenkaart
```
Grasberg-mill `ag-grasberg-mill` ──(b1 leiding · HEAT-corridor via Tembagapura/Timika · 115 km gepubliceerd, 89,6 km stippel)──►
Portsite/Amamapare `ag-portsite-kade` ──(b2 zee · haven-aanloop 53,2 km stippel)──► zeeknoop 7877 (-4.9278,136.4009)
──(b3 zee · MARNET · 16.998,6 km via Suez · aannemelijk: een bron voor de bestemming)──► Huelva-zeeknoop 8016 (37.0872,-6.8478)
──(b4 zee · haven-aanloop 7,8 km stippel)──► Puerto Exterior `ag-huelva-terminal` ──(b5 truck · N-442/H-30 · aannemelijk)──►
Atlantic Copper-smelter `ag-atlanticcopper-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `ag-grasberg-mill` → `ag-portsite-kade` | slurryleiding langs de HEAT-corridor; **letterlijke kopie koper-grasberg-manyar b1** | 115 gepubliceerd [1][4]; gebakken stippel 89,6 hemelsbreed over 6 punten | kopie `leidingbeen-grasberg-portsite-schematisch.geojson` | **ja** - OSM heeft geen `man_made=pipeline` in de Grasberg-bbox (Overpass 2026-06, koper-brief) |
| b2 | B | zee | Portsite-kade → zeeknoop 7877 | haven-aanloop Amamapare, kade 49,9 km van de knoop (> 5 km); **kopie koper-grasberg-manyar b2** | 53,2 over water | kopie `aanloop-portsite.geojson` | **ja** - MARNET reikt niet |
| b3 | B | zee | zeeknoop 7877 → Huelva-zeeknoop 8016 - **aannemelijk: een bron voor de bestemming** | Arafura - Banda - Indische Oceaan - Bab el-Mandeb - Suez - Gibraltar (router kiest Suez, gemeten) | MARNET **16.998,6** (90 edges; geen gepubliceerde routelengte) | MARNET `--been zee` | nee |
| b4 | B | zee | zeeknoop 8016 → `ag-huelva-terminal` | haven-aanloop Puerto de Huelva, kade 7,8 km van de knoop; **kopie koper-cerroverde-huelva b6** | 7,8 hemelsbreed | `--stippel` 37.0872,-6.8478 → 37.1535,-6.8768 | **ja** - schematisch, MARNET reikt niet |
| b5 | D | truck | `ag-huelva-terminal` → `ag-atlanticcopper-smelter` | N-442, H-30, Av. Francisco Montenegro; **kopie zilver-matsa-huelva b2** (aannemelijk) | hemelsbreed 10,5, geen wegkm; OSM-pad 11,9; gebakken 12,7 | kopie `zilver-matsa-huelva-weg-terminal-smelter.geojson` | nee |

**Stippel = 150,6 km van ca. 17.161,9 km = 0,9 procent van de lijn** (b1 89,6 + b2 53,2 + b4 7,8); het zeebeen is 99,1 procent en doorgetrokken. Alle benen behalve b3 zijn kopieen; nieuw is alleen het zeebeen Portsite → Huelva. Het zeebeen is **aannemelijk: een bron voor de bestemming** (FCX 10-K, via koper-cerroverde-huelva): dat staat in de beennaam, de lijn blijft doorgetrokken. Suez of Kaap: MARNET kiest Suez; de scheepsroute zelf is niet gebrond.

## 3 · Ankers (alle hergebruikt; eigen z15-blik 2026-11-01, `v2/build-cache/satcheck/sat-zilver-grasberg-huelva-<anker>.png`)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-grasberg-mill` | mill / kop van de leiding | Grasberg mill- en concentratorcomplex (PTFI) | -4.0905, 137.1155 | koper-grasberg-manyar §3 `cu-grasberg-mill` | bron-gelegd (z15 gezien: gebouwencluster met hallen en indikker in het dal onder de put, mijnweg slingert noordwaarts) |
| `ag-portsite-kade` | overslag leiding → zee | Portsite / Amamapare, PTFI | -4.8290, 136.8405 | koper-grasberg-manyar §3 `cu-portsite-kade` | bron-gelegd (z15 gezien: kadefront aan de rivier aan de zuidzijde van de terreinplaat tussen loods en filtergebouwen, schepen langszij) |
| `ag-huelva-terminal` | losplek / overslag zee → truck | Puerto Exterior, Muelle Ingeniero Juan Gonzalo (zuidzijde) - **losplek niet gebrond** | 37.1535, -6.8768 | zilver-matsa-huelva §3; koper-cerroverde-huelva §3 | aannemelijk (z15 gezien: witte opslagloods naast de containerkade met portaalkranen, bulkschip op de rede; Impala's MATSA-exportterminal, geen bewezen importkade van Atlantic Copper) |
| `ag-atlanticcopper-smelter` | smelter (stoppunt) | Atlantic Copper, Punta del Sebo, Huelva | 37.2287, -6.9482 | zilver-matsa-huelva §3 | bron-gelegd (z15 gezien: smeltergebouwen met schoorstenen, concentraatstapels en drie steigers langs de Odiel) |

Knopen (geen ankers): MARNET-zeeknoop 7877 (-4.9278, 136.4009) en 8016 (37.0872, -6.8478).

## 4 · Via-punten
Geen nieuwe via-punten: alle landbenen zijn letterlijke kopieen. b1 volgt de 4 via-punten van koper-grasberg-manyar §4 (Tembagapura -4.1424,137.0907 · -4.4349,136.9001 · Timika -4.5389,136.8956 · -4.8130,136.8465); b5 die van zilver-matsa-huelva §4 (N-442 37.1958,-6.9253).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Grasberg-mill | PT Freeport Indonesia | erts → Cu-Au-Ag-concentraat | Ag 190 t in 2023 (mijn) | [1] |
| Portsite-ontwatering | PTFI | slurry → concentraat | 3 vacuumfilters, loods 135.000 t | [4] |
| Atlantic Copper | Freeport-McMoRan | Cu-concentraat → anode → kathode; anodeslijmen met typisch 8,5 procent Ag | smelter 330 kt anode/j; 247,6 kt anode in 2024 | [2][5][6] |

## 6 · Stoppunt
Bij de Atlantic Copper-smelter: daar eindigt het concentraat en gaat het zilver in de anodeslijmen naar gespecialiseerde raffinaderijen zonder genoemde afnemer [6]; fase E vervalt. Zou b5 niet houden, dan is het Huelva-anker het stoppunt.

## 7 · Open punten
- **Zilver naar Huelva niet gepubliceerd:** 190 t Ag is de mijnproductie van heel Grasberg; Atlantic Copper koopt 13 procent van zijn concentraat in Indonesie (tonnage en Ag-gehalte niet gepubliceerd). Geen volume te berekenen; het cijfer is context, geen stroomvolume.
- **Indonesische bron niet bij naam:** het 10-K noemt Indonesie, niet Grasberg; Grasberg is de grote concentraatexporteur van het land (afleiding).
- **Losplek Huelva niet gebrond:** het anker is Impala's MATSA-terminal; Atlantic Coppers eigen pantalan (BOE-concessie) kan de echte plek zijn (zie koper-cerroverde-huelva §7).
- **Route Suez/Kaap onbekend:** MARNET kiest Suez (16.998,6 km); een scheepsbron ontbreekt.
- **Leiding niet in OSM:** gebakken stippel 89,6 km hemelsbreed tegen 115 km gepubliceerd; geen +-15 procent-norm hier. Aanloop-stippels geen geometrie van de vaargeul.
- **Grasberg-productie 2026 lager** (modderstroom 08-09-2025); peiljaar 2023.
- **Grasberg ontbreekt in de zilver-sitelaag** (190 t Ag): centraal toevoegen.
- Het Indische alternatief (Hindalco Dahej) is niet onderzocht: geen bron voor de concentraatherkomst.

## 8 · Bronnen
[1] Wikipedia, "Grasberg mine" - 9 t Au en 190 t Ag in 2023; drie pijpleidingen naar Amamapare; concentraat naar smelters wereldwijd. https://en.wikipedia.org/wiki/Grasberg_mine
[2] Freeport-McMoRan, Form 10-K 2024 (via koper-cerroverde-huelva [1]) - Atlantic Copper 2024: 13 procent van het concentraat uit Indonesie, 15 procent Zuid-Amerika; anode 247.600 t. https://s22.q4cdn.com/529358580/files/doc_financials/10-K/10_k2024.pdf
[3] Freeport-McMoRan, update herstart Grasberg (2025) (via koper-grasberg-manyar [8]). https://investors.fcx.com/investors/news-releases/news-release-details/2025/Freeport-Provides-Update-on-Restart-Plans-for-Grasberg-Minerals-District/default.aspx
[4] PT Freeport Indonesia, Drying & Shipping - filters, loods 135.000 t, Sea Buoy A. https://ptfi.co.id/en/drying-and-shipping
[5] Atlantic Copper, "Materias primas" - concentraat per schip en weg, ontvangst in Puerto de Huelva. https://atlantic-copper.es/como-lo-hacemos/materias-primas/
[6] Atlantic Copper, "Metales preciosos" - anodeslijmen met typisch 8,5 procent Ag. https://atlantic-copper.es/que-hacemos/metales-preciosos/
[7] Interne briefs: koper-grasberg-manyar (b1, b2, ankers), koper-cerroverde-huelva (b6, Huelva-zeeknoop, anker-status), zilver-matsa-huelva (b2, ankers).
[8] MARNET-proefrun 2026-11-01 (hecht_marnet route): -4.9278,136.4009 → 37.0872,-6.8478 = 16.998,6 km, 90 edges, passeert Suez (3 km) en Gibraltar (6 km), niet de Kaap (5.688 km ernaast). Esri World Imagery via `sat_check.py`: `sat-zilver-grasberg-huelva-ag-grasberg-mill.png` · `-ag-portsite-kade.png` · `-ag-huelva-terminal.png` · `-ag-atlanticcopper-smelter.png` (z15).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-zilver-grasberg-huelva.json` (versie 2, lonlat, 35,9 KB, 5 benen, 4 markers) · **recept:** `bak_zilver_grasberg_huelva` in `v2/tools/bak_stromen.sh` · **titel:** Zilver · Grasberg → Portsite → Atlantic Copper Huelva (Spanje). Geen nieuw profiel, geen wegscan, geen aanloop-run: alle benen behalve het zeebeen zijn letterlijke kopieen.

| # | modaliteit | km | punten | stippel | herkomst |
|---|---|---|---|---|---|
| b1 | leiding | 89,6 | 6 | ja | kopie koper-grasberg-manyar b1 (`leidingbeen-grasberg-portsite-schematisch.geojson`) |
| b2 | zee | 53,2 | 21 | ja | kopie koper-grasberg-manyar b2 (`aanloop-portsite.geojson`) |
| b3 | zee | 16.998,6 | 1.744 | nee | MARNET `--been`, 90 edges, via Suez; snap 0,025 km / 0,000 km |
| b4 | zee | 7,8 | 2 | ja | rechte `--stippel`, kopie koper-cerroverde-huelva b6 |
| b5 | truck | 12,7 | 179 | nee | kopie zilver-matsa-huelva b2 (`zilver-matsa-huelva-weg-terminal-smelter.geojson`) |

**Totaal 17.161,9 km; stippel 150,6 km (0,9 procent).** Naden: max 0,02 km (b2 → b3, de snap); overige 0,00 km. Markers (4) liggen 0,0 km van hun lijn. Deze run bevestigt de proefrun uit de brief (16.998,6 km, 90 edges).

**Toelichting per stippel.** b1 slurryleiding: OSM heeft geen `man_made=pipeline` in de Grasberg-bbox; 89,6 km hemelsbreed over 6 punten tegen 115 km gepubliceerd, dus geen +-15 procent-norm. b2 haven-aanloop Amamapare: kade 49,9 km van zeeknoop 7877, MARNET reikt niet; kortste pad over water, geen waargenomen vaargeul. b4 haven-aanloop Puerto de Huelva: kade 7,8 km van zeeknoop 8016, rechte lijn, schematisch.

**Toets (handleiding §5).** json.load goed, versie 2, punt_formaat lonlat, modaliteiten {leiding, zee, truck}, elk been >= 2 punten. b5 (12,7 km) tegen hemelsbreed 10,5 en OSM-pad 11,9 uit de brief: geen gepubliceerde wegkm, kopie van een eerder getoetst been. `toets_knikken.py`: 8 knikken >= 60 graden, 2 omkeringen, 0 terugloop; alle liggen in b5 (de gekopieerde stadsweg bij Puerto Exterior en Punta del Sebo, o.a. de bocht 37,1956,-6,9252) en zijn dus erfenis van zilver-matsa-huelva, geen nieuwe fout. `toets_rechte_benen.py --min-km 5`: alleen b4 (stippel met reden).

**Lessen.** (1) Een keten met drie kopieen en een MARNET-been bakt in een minuut zonder wegscan. (2) De zee-snap is 0,025 km, dus de naad b2 → b3 is verwaarloosbaar; de aanloop is nodig omdat de kade 49,9 km van de knoop ligt. (3) Eindpunt klopt met het id (Huelva); niets afgeweken. (4) Centraal: sitelaag mist Grasberg (190 t Ag); registerregel `ag-gh`.
