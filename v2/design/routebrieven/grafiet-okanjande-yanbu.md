# Routebrief (licht) · Grafiet · Okanjande (Namibië) → Walvis Bay → Yanbu King Fahd Industrial Port (Saoedi-Arabië)

**stroom-id:** `grafiet-okanjande-yanbu` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) ·
**status:** gebakken
**Keten in één zin:** Grafietvlok-concentraat van de Okanjande-mijn (Northern Graphite, bij Otjiwarongo) gaat per **truck** (zandweg → D2515 → B1 → C33 → B2) naar de
Walvis Bay-kade, per **zeeschip** (haven-aanloop + MARNET, Kaap, Bab-el-Mandeb, Rode Zee) naar Yanbu en via een tweede aanloop naar de algemene-ladingkade van
King Fahd Industrial Port, voor de geplande BAM-fabriek in Yanbu Industrial City (aannemelijk: één bron noemt de stad, geen bron de haven of kade).
**Welke as van het verhaal:** Namibische vlok naar een Saoedische anodefabriek (Obeikan 51 % / Northern 49 %). Volume: 0 kt vandaag (Okanjande ligt stil,
pre-FID); plan 31 kt/j vlok vanaf herstart eind 2027 [1]; Yanbu-term sheet tot 50 kt/j concentraat, BAM 25 kt/j, start 2028 [2][3]. Peiljaar 2026; eenheid kt grafiet per jaar.

## 1 · Ketenkaart
```
Okanjande-put `gr-okanjande-mijn` ──(b1a truck · zandweg naar D2515, STIPPEL last mile · 2,2 km)──► D2515-aansluiting (-20.6005, 16.6018)
  ──(b1b truck · D2515 → B1 → Otjiwarongo · ~21 km)──► Otjiwarongo B1 (-20.4619, 16.6510)
  ──(b1c truck · C33 Kalkfeld/Omaruru → B2, KOPIE kobalt-mutanda-walvisbay b4 vanaf vertex 4058 · 417,5 km)──► Walvis Bay-kade `gr-walvisbay-kade`
  ──(b2 zee · haven-aanloop WB, STIPPEL · 12,9 km)──► zeeknoop 8084 (-22.8344, 14.4759)
  ──(b3 zee · MARNET, Kaap → Bab-el-Mandeb → Rode Zee · 10.657,0 km gemeten)──► zeeknoop 5931 (24.0364, 37.9358)
  ──(b4 zee · haven-aanloop KFIP, STIPPEL · 28,4 km hemelsbreed, 30,6 km over water)──► KFIP-kade `gr-yanbu-kade` ⏹ stoppunt (BAM-fabriek in Yanbu Industrial City niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | A | truck | `gr-okanjande-mijn` → D2515-aansluiting | zandspoor naar de D2515, 2,2 km | hemelsbreed 2,2 km, geen wegkm | `--stippel "truck|last mile (geen net op deze korrel)|…"` | ja: `track` komt de wegscan niet door, site 2,2 km van het net |
| b1b | A | truck | D2515-aansluiting → Otjiwarongo (B1) | D2515 (secundair) → B1 → Hage Geingob Street | OSRM-indicatie 21,3 km (geen publicatie) [9][10] | `maak_stroombeen_weg` nieuw profiel, extract `namibie` | nee |
| b1c | A | truck | Otjiwarongo → `gr-walvisbay-kade` | B1 → C33 (Kalkfeld, Omaruru) → B2 (Karibib, Usakos, Swakopmund) → Walvis Bay | 417,5 km uit het gebakken bestand; hele b1: hemelsbreed 342 km, geen wegkm; bedrijfsopgave 288 km [1] (PEA 2022: 388 km) onverenigbaar met de kaart; OSRM 445,6 km | LETTERLIJKE KOPIE van de staart van `kobalt-mutanda-walvisbay-weg-katimamulilo-walvisbay.geojson` (vertex 4058 t/m eind, al gesneden: `$BEEN/grafiet-okanjande-yanbu-weg-otjiwarongo-walvisbay.geojson`, 2.532 punten) | nee |
| b2 | B | zee | `gr-walvisbay-kade` → zeeknoop 8084 | haven-aanloop Walvis Bay | 12,9 hemelsbreed (kade > 5 km van de knoop) | rechte `--stippel` (maak_havenaanloop gaf hier eerder twee keer time-out) | ja: 1:10M-kust kent de haven niet |
| b3 | B | zee | zeeknoop 8084 → zeeknoop 5931 | MARNET: Kaap, Bab-el-Mandeb, Rode Zee | 10.657,0 (proefrun hecht_marnet, 1.085 punten); geen gepubliceerde routelengte | `--been "zee|…|-22.8344,14.4759|24.0364,37.9358"` | nee |
| b4 | B | zee | zeeknoop 5931 → `gr-yanbu-kade` | haven-aanloop KFIP (kade 28,4 km van de knoop) | 28,4 hemelsbreed; 30,6 over water (14 punten, omweg 1,078, al gerekend) | `--stippel-geojson` met `$BEEN/grafiet-okanjande-yanbu-aanloop-yanbu-rev.geojson` (omgekeerd: knoop → kade) | ja: aanloop |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-okanjande-mijn` | mijn + vlokplant (kop) | Okanjande-put, 20 km (bron 14 km) ten zuiden van Otjiwarongo | -20.5999, 16.6230 | [1][5][13] | aannemelijk (z15 gezien: kleine put met afgebakend erf, zandweg oost-west langs de put, kleine bebouwing 450 m westelijk; OSM kent geen object, terreinnaam niet bevestigd) |
| `gr-walvisbay-kade` | overslag (zeekade) | Walvis Bay-containerterminal, gereclameerd havenhoofd — hergebruikt uit `kobalt-mutanda-walvisbay` | -22.9500, 14.4860 | [12] | bron-gelegd (letterlijk hergebruikt: containerstapels en portaalkranen op het havenhoofd); welke kade grafiet gebruikt is niet gebrond |
| `gr-yanbu-kade` | overslag/losplek (algemene lading) | King Fahd Industrial Port, algemene-ladingkade met loodsen, Yanbu | 23.9637, 38.2036 | [2][7][11] | aannemelijk (z16 gezien: kadeapron met drie transitloodsen en schepen langszij, containerstapels/autopark 1 km NW; haven en kade in geen bron voor deze lading genoemd) |

Zeeknopen (MARNET, `marnet_zee`): 8084 op 12,9 km van de Walvis Bay-kade; 5931 op 28,4 km van `gr-yanbu-kade`. Beelden: `v2/build-cache/satcheck/sat-grafiet-okanjande-yanbu-gr-okanjande-mijn.png`, `-okanjande-nipdb.png`, `-gr-yanbu-kade.png`, `-gr-yanbu-kade-z14.png`, `-gr-yanbu-kade-z16.png`.

## 4 · Via-punten (alleen b1b; b1c is kopie)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1b | 1 | D2515-aansluiting — begin profiel (anker) | -20.6005, 16.6018 | OSM-way 22794070 (D2515, secundair); eerste punt waar de put aan het net komt [9][10] |
| b1b | 2 | D2515 → B1 | -20.5109, 16.6841 | OSRM-afslag; pint B1 noordwaarts i.p.v. een omweg langs de farmwegen |
| b1b | 3 | Otjiwarongo B1 — einde profiel (anker) | -20.4619, 16.6510 | = vertex 4058 van de kopie (16.650971, -20.461853): naad 0 m |
Vensterbreedte 40 km, refs `["D2515","B1"]`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Okanjande vlokplant (in juni 2026 van Okorusu naar de mijn verhuisd) | Northern Graphite | erts → vlokconcentraat | 31 kt/j plan; herstart eind 2027, capex US$34,4 mln, nog te financieren | [1][4] |
| BAM-fabriek, Yanbu Industrial City (niet gebouwd) | JVCo: Obeikan 51 % / Northern 49 % | vlokconcentraat → battery anode material | BAM 25 kt/j initieel, concentraat tot 50 kt/j; start 2028 onder voorbehoud | [2][3] |

## 6 · Stoppunt
De lijn stopt op de KFIP-kade: de fabrieksplek in Yanbu Industrial City is niet genoemd (alleen de stad [2]), dus een fase-D-anker zou een verzonnen coördinaat zijn; geen bron noemt KFIP of
Yanbu Commercial Port voor deze lading. Fase D en E vervallen.

## 7 · Open punten
- **Terrein niet bron-gelegd:** de put is zichtbaar op z15, maar geen bron geeft een coördinaat. De coördinaat -20.587, 16.628 uit de haalbaarheidstoets (nipdb) kon ik in de pdf niet terugvinden; op z15 ligt daar open bosveld 1,5 km NNO van de put.
- **Afstand tegenstrijdig:** bedrijfswebsite 288 km tot Walvis Bay [1], PEA-publicatie 388 km, kaart 342 km hemelsbreed en 446 km over de weg. De 288 is niet gebruikt.
- **Haven aangenomen:** KFIP (algemene lading en containers, bedoeld voor industrie [7]) is gekozen omdat Yanbu Industrial City eraan ligt; Yanbu Commercial Port (24.0803, 38.0659) ligt ca. 30 km noordwestelijker en is het alternatief.
- **Volume nul, pre-FID:** term sheet 14 jan 2026 niet-bindend; offtake tot 50 kt/j niet gesloten, Okanjande-herstart afhankelijk van financiering [1][3].
- **Rode Zee:** de MARNET-route is de structurele route via Bab-el-Mandeb; actuele beschikbaarheid niet onderzocht.
- **Last mile:** zandspoor 2,2 km als stippel; dat het in OSM als `track` staat is niet nagelopen met een scan.

## 8 · Bronnen
[1] Northern Graphite, Okanjande Mine (31 kt/j, herstart eind 2027, plant juni 2026 naar de mijn, capex US$34,4 mln, 288 km tot Walvis Bay). https://northerngraphite.com/okanjande-mine
[2] Northern Graphite, Yanbu BAM project (Obeikan 51 / Northern 49, 25 kt/j, 2028, Yanbu Industrial City, offtake tot 50 kt/j Okanjande). https://northerngraphite.com/yanbu-plant
[3] Northern Graphite persbericht 14 jan 2026, term sheet BAM-JV (US$200 mln, niet-bindend). https://www.northerngraphite.com/wp-content/uploads/2026/01/Northern-Inks-BAM-Joint-Venture-with-KSAs-Obeikan_Jan14_2026_.pdf
[4] Northern Graphite, processing plant relocation Okanjande, juni 2026. https://www.nasdaq.com/press-release/northern-graphite-completes-processing-plant-relocation-advance-okanjande-mine
[5] Republikein/Windhoek Express, "Okanjande set for 2027 restart" (ca. 20 km ten zuiden van Otjiwarongo, volgens zoekresultaat). https://www.we.com.na/mw-main/okanjande-set-for-2027-restart-NMH013523-3015-16685
[6] Northern Miner, PEA Okanjande 2022 (14 km / 388 km volgens zoekresultaat, niet zelf gelezen). https://northernminer.com/news/northern-graphite-completes-pea-on-namibian-operation-forecasts-restart-by-mid-2023/1003843756
[7] Wikipedia, "King Fahd Industrial Port (Yanbu)" (General Cargo and Containers Terminal, bulk, crude; volgens zoekresultaat). https://en.wikipedia.org/wiki/King_Fahd_Industrial_Port_(Yanbu)
[8] Wikipedia, "Yanbu" (twee havens, Yanbu Industrial City zuid van de stad, 24°5′22″N 38°3′43″E). https://en.wikipedia.org/wiki/Yanbu
[9] OpenStreetMap via Nominatim (ODbL), way 22794070 D2515 secondary bij -20.6006, 16.6018. https://nominatim.openstreetmap.org
[10] OSRM-demo (OSM-gegevens): put → Otjiwarongo 23,5 km via D2515/B1; put → Walvis Bay-kade 445,6 km via C33/B2. https://router.project-osrm.org
[11] Esri World Imagery via `v2/tools/sat_check.py` — `sat-grafiet-okanjande-yanbu-*.png`.
[12] `v2/design/routebrieven/kobalt-mutanda-walvisbay.md` (anker Walvis Bay, b4-kopie), `uranium-walvisbay-malvesi.md` (zeeknoop 8084, aanloop-stippel).
[13] Haalbaarheidstoets `grafiet-okanjande-yanbu` (2026-10-31, bindend): eindanker KFIP, 10.657 km MARNET, nipdb-coördinaat.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
Bestand `v2/data/stroomroute-grafiet-okanjande-yanbu.json` (75,2 KB, versie 2, lonlat, 6 benen, 3.752 punten, 3 markers), functie `bak_grafiet_okanjande_yanbu` in `v2/tools/bak_stromen.sh`, profiel `grafiet-okanjande-yanbu-okanjande-otjiwarongo` in `v2/tools/maak_stroombeen_weg.py`.

| # | modaliteit | km gemeten | km brief | naad | opmerking |
|---|---|---|---|---|---|
| b1a | truck, stippel | 2,2 | hemelsbreed 2,2 | 0 | last mile zandspoor, geen net op deze korrel |
| b1b | truck | 21,3 | OSRM 21,3 | 0 | wegscan namibie, 117 punten, +1,7% tegen 21 |
| b1c | truck | 417,5 | 417,5 (kopie) | 0 | letterlijke kopie staart kobalt-mutanda-walvisbay b4, 2.532 punten |
| b2 | zee, stippel | 12,9 | 12,9 | 0 | rechte haven-aanloop Walvis Bay |
| b3 | zee | 10.657,0 | 10.657,0 | 0 | MARNET 8084 naar 5931, 1.085 punten |
| b4 | zee, stippel | 30,6 | 30,6 | 0 | haven-aanloop KFIP, omgekeerde kopie van het gerekende bestand |

Totaal 11.141,5 km; hele b1 441,0 km (hemelsbreed 342, OSRM 445,6: binnen 1%). Markers gr-okanjande-mijn, gr-walvisbay-kade, gr-yanbu-kade liggen 0,0 km van hun lijn; geen naad boven 0 m.

**Recept.** b1a `--stippel truck`; b1b profiel met via (lon,lat) 16.6018,-20.6005 / 16.6841,-20.5109 / 16.650971,-20.461853, extract namibie, refs D2515 B1, gepubliceerdKm 21, vensterKm 40, trimStaart, via `wegscan_puur.py`; b1c `--been-geojson` op het al gesneden bestand; b2 rechte `--stippel`; b3 `--been zee`; b4 `--stippel-geojson` op `grafiet-okanjande-yanbu-aanloop-yanbu-rev.geojson`.

**Toelichting stippels.** b1a: het zandspoor staat als track buiten de wegscan, site 2,2 km van het net. b2: de 1:10M-kust kent de haven Walvis Bay niet, maak_havenaanloop gaf eerder time-out, dus recht. b4: MARNET reikt niet tot de KFIP-kade (28,4 km hemelsbreed van knoop 5931), aanloop over water 30,6 km.

**Toetsen.** toets_knikken: b1b heeft een omkering van 166 graden op 1 m bij het begin (het anker ligt 1 m naast de weg, procesgat), de overige knikken zijn spikes van enkele meters in de kopie bij de Walvis Bay-haven en MARNET-bochten op open zee; geen terugloop. toets_rechte_benen: alleen de stippel b2 heeft omwegfactor 1,000 (met reden). Geen naad boven 0 m.

**Lessen.** Een tussentijdse `bash -n`-fout in bak_stromen.sh na de bake kwam van een gelijktijdige edit door een andere agent; daarna was het bestand schoon en LF. De brief bleef gelijk aan de bake: geen afwijking van het ontwerp.
