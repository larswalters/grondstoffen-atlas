# Routebrief (licht) · olie — Heglig (Nile Blend) → Bashayer (Port Sudan) → Fujairah (VAE)

**stroom-id:** `olie-heglig-fujairah` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** Nile Blend (Heglig + Unity, Zuid-Soedanese en Soedanese crude) per **Greater Nile-leiding** (GNPOC, 1.476 km OSM)
van het Heglig-complex naar het Bashayer-exportterminal bij Port Sudan, per **tanker** (Aframax/Suezmax) over de Rode Zee, Bab-el-Mandeb en
de Arabische Zee naar de Fujairah-exportterminal (VAE); de bestemming Fujairah rust op één bron.
**Welke as van het verhaal:** *landlocked export onder oorlog* — Zuid-Soedan heeft geen kust en exporteert via Soedans leiding en haven.
Bashayer is het enige exportpunt voor ~170 kb/d Dar+Nile Blend [3]; gemiddeld 130 kb/d in 2023 (Kpler via Argus) [5]; in 2025 stilstand en
herstart (leidingreparaties, drones op Heglig). Het Nile Blend-aandeel is niet los gepubliceerd. Peiljaar 2023–2025, sterk schommelend [2][3][5].
Fujairah nam 41% van de Bashayer-bestemmingen [2] (vijf jaar eerder ~44% [3]); het Fujairah-deel in kb/d is eigen rekensom (~50–70 kb/d).

## 1 · Ketenkaart
```
Heglig-leidingkop `ol-heglig-kop` (OSM-begin, ~32 km N van de CPF) ──(b1 leiding · Greater Nile Oil Pipeline · 1.475,8 km OSM
  / ~1.600 gepubliceerd; langs El Obeid, Khartoum, Shendi, Atbara, Haiya)──► Bashayer-tankpark `ol-bashayer-tankpark`
──(b2 stippel leiding · 2,1 km)──► Bashayer-steiger `ol-bashayer-steiger` ──(b3 stippel zee · haven-aanloop · 28,6 km)──► zeeknoop 5930
──(b4 zee · Rode Zee → Bab-el-Mandeb → Golf van Aden → Arabische Zee · 3.911 km · aannemelijk: één bron)──► zeeknoop 8407
──(b5 stippel zee · haven-aanloop Fujairah · 12,2 km)──► Fujairah-exportterminal `ol-fujairah-term` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Heglig-leidingkop → Bashayer-tankpark | Greater Nile Oil Pipeline (GNPOC) | 1.475,8 OSM-meting; ~1.600 gepubliceerd [1] (-7,8%) | OSM-way 199993060 (1 way, 1.050 pt) als FeatureCollection; `maak_leidingbeen_olie_heglig_fujairah.py` | nee |
| b2 | A | leiding | Bashayer-tankpark → steiger | laadleiding (niet gekarteerd) | 2,1 (eigen meting) | rechte lijn | ja: geen OSM-leiding |
| b3 | B | zee | steiger → MARNET-zeeknoop 5930 (19.5908, 37.4963) | haven-aanloop Bashayer | 28,6 (maak_havenaanloop) | `olie-heglig-fujairah-aanloop-bashayer.geojson` | ja: MARNET reikt niet tot de kade (28,5 km) |
| b4 | B | zee | zeeknoop 5930 → Fujairah (aannemelijk: één bron) | Rode Zee → Bab-el-Mandeb → Golf van Aden → Golf van Oman | 3.911 MARNET (geen gepubliceerde zeekm; de ontwerpschatting 3.400 vervalt) | MARNET | nee |
| b5 | B | zee | zeeknoop 8407 (25.1378, 56.4038) → Fujairah-kade | haven-aanloop Fujairah | 12,2 | LETTERLIJKE KOPIE, omgekeerd, van `olie-habshan-chiba-aanloop-fujairah.geojson` | ja: kade 10,5 km van de zeeknoop |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-heglig-kop` | kop van de leiding | Greater Nile-leidingbegin (OSM) | 10.2945, 29.3546 | [4][8] | **onzeker** (z14 gezien: kaal bushland met paden, geen installatie; de Heglig-CPF ligt ~32 km zuidelijker, zie §7) |
| `ol-bashayer-tankpark` | overslag leiding → steiger | Bashayer-tankpark (GNPOC-leidingeinde) | 19.3984, 37.2885 | [4][5] | bron-gelegd (z15 gezien: tankenpark met 9 tanks, OSM-leiding eindigt aan de westrand; 2e tankpark met 6 tanks 1,5 km zuidelijker, niet gebruikt) |
| `ol-bashayer-steiger` | overslag steiger → tanker | Bashayer-steiger (OSM man_made=pier, way 689616227) | 19.4085, 37.3052 | [4] | aannemelijk (z15: T-steiger met weg naar het noordelijke tankpark; geen bron noemt deze steiger bij naam) |
| `ol-fujairah-term` | losplek / stoppunt | Fujairah-exportterminal (FOIZ-tankenpark) | 25.2135, 56.3419 | hergebruik `olie-habshan-chiba.md` §3 | bron-gelegd (daar z15: tankenpark tegen de bergvoet, kade op ~1 km) |

## 4 · Via-punten
Geen: b1 is een gestikte OSM-way, geen corridorkeuze. Dichtste punten van de lijn: El Obeid 5,9 km · Khartoum 16,1 km · Shendi 7,3 km · Atbara 23,1 km · Haiya 1,9 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Heglig (PETCO-meetstation/CPF) | PETCO/GNPOC | Zuid-Soedanese crude uit Blok 5A → Nile Blend in de leiding | Heglig-veld ~20 kb/d; Zuid-Soedan ~110 kb/d export [6] | [5][6] |
| Greater Nile-leiding | GNPOC (CNPC/PipeChina 40%, Petronas 30%, ONGC 25%, Sudapet 5%) | Nile Blend → Bashayer | 250 kb/d (GEM) tot 450 kb/d (ontwerp) [5][7] | [5][7] |
| Bashayer-terminal | Soedan | tankpark → steiger → Aframax/Suezmax | 53% van Soedans exportvolume (PLOC 35%) [2] | [2] |
| Fujairah-terminal | FOIZ/diverse tenants | tanker → opslag | zie `olie-habshan-chiba.md` | — |

## 6 · Stoppunt
De brief stopt bij de Fujairah-exportterminal: geen bron noemt welke raffinaderij of koper achter Fujairah de Nile Blend neemt (Maleisië 24% [2] valt buiten deze keten); fase D/E vervallen.

## 7 · Open punten
- **Begin van de leiding niet gekarteerd:** OSM begint 32,3 km N van de Heglig-CPF (z15: complex met vliegveld rond 10.0075, 29.3985, niet als anker gelegd). Geen stippel naar de CPF verzonnen; de lijn begint waar het bewijs begint.
- **Dar Blend hoort niet bij deze leiding:** Dar komt uit Blok 3/7 [5] en loopt via Petrodar/PLOC (OSM-way 312828553, ook als "Greater Nile" getagd, buiten deze keten); titel en ketenomschrijving gaan over Nile Blend. De Petrodar-koppeling is niet in een bron gelezen.
- **Bestemming Fujairah = één bron** (41% van Bashayer, niet cargo-specifiek [2]). Aug 2025: de VAE schorsten vaarvergunningen naar Port Sudan en een Nile Blend-lading lag stil voor Fujairah (S&P via zoekresultaat, pagina niet gelezen) [3]; de VAE-leg is politiek onzeker.
- **Steiger** niet bij naam bevestigd; een tweede pier (OSM-way 689616028, 19.3849, 37.3123) hoort bij het zuidelijke tankpark en is niet gekozen. Tankers laden mogelijk ook via een boei (schip op z15 rond 19.388, 37.318).
- Leidingcapaciteit 250 (GEM) of 450 kb/d (energynews); gepubliceerde zeekm ontbreekt (3.911 km is een MARNET-uitkomst).
- OSM-leiding is 7,8% korter dan ~1.600 km: past bij het ontbrekende beginstuk (~32 km) plus afronding.

## 8 · Bronnen
[1] Wikipedia, Greater Nile Oil Pipeline (1.600 km, 1999, GNPOC/CNPC 40%). https://en.wikipedia.org/wiki/Greater_Nile_Oil_Pipeline
[2] Breakwave Advisors, 4-7-2025, Sudan crude exports via Bashayer (Dar/Nile Blend, VAE 41% Fujairah, Maleisië 24%, Bashayer 53%, PLOC 35%). https://www.breakwaveadvisors.com/insights/2025/7/4/sudan-crude-oil-exports-via-bashayer
[3] WebSearch-samenvatting van S&P Global 27-8-2025 (170 kb/d, VAE ~44%, vergunningen geschorst; S&P gaf 403). https://www.spglobal.com/energy/en/news-research/latest-news/crude-oil/082725-tanker-with-crude-cargo-from-sudan-idles-off-uae-as-bilateral-ties-sour
[4] OpenStreetMap (ODbL), Overpass/API 2026-10-30: way 199993060 (1.475,8 km, begin 10.2945/29.3546, eind 19.3984/37.2885), tankpark way 312824703, pier 689616227. https://www.openstreetmap.org/way/199993060
[5] energynews.pro, 1-9-2025, Heglig-evacuatiewaarschuwing (Nile Blend, 450 kb/d, Bashayer, Kpler 130 kb/d in 2023, Dar Blend Blok 3/7). https://energynews.pro/en/sudan-warns-of-heglig-evacuation-after-new-drone-strikes
[6] The EastAfrican, 1-9-2025, Juba faces ruin (Heglig CPF, 20 kb/d, 110 kb/d export). https://www.theeastafrican.co.ke/tea/news/east-africa/juba-faces-ruin-after-sudan-shuts-oil-pipeline-5175318
[7] GEM.wiki, Greater Nile Oil Pipeline (250 kb/d, eigenaren). https://www.gem.wiki/Greater_Nile_Oil_Pipeline
[8] Esri World Imagery via `sat_check.py` (z14–z15): `v2/build-cache/satcheck/sat-olie-heglig-fujairah-heglig-kop.png`, `-heglig-stad.png`, `-heglig-cpf.png`, `-bashayer-tank.png`, `-bashayer-steiger.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)

`bash v2/tools/bak_stromen.sh olie-heglig-fujairah` (functie `bak_olie_heglig_fujairah`) geeft `v2/data/stroomroute-olie-heglig-fujairah.json`:
**5.429,7 km · 1.480 punten · 5 benen · 4 markers · 29,5 KB · naden 0,00 km**; contract versie 2, punt_formaat lonlat, modaliteiten {leiding, zee}.

| # | modaliteit | km | stippel | naam |
|---|---|---|---|---|
| b1 | leiding | 1.475,8 | nee | Greater Nile Oil Pipeline (OSM-way 199993060), Heglig-leidingkop → Bashayer-tankpark |
| b2 | leiding | 2,1 | ja | laadleiding tankpark → steiger (geen OSM-leiding) |
| b3 | zee | 28,6 | ja | haven-aanloop Bashayer (kade 28,5 km van zeeknoop 5930) |
| b4 | zee | 3.911,0 | nee | MARNET zeeknoop 5930 → Fujairah (aannemelijk: één bron) |
| b5 | zee | 12,2 | ja | haven-aanloop Fujairah, omgekeerde kopie van olie-habshan-chiba |

Stippel in totaal 42,9 km = 0,8% van de keten.

**Recept.** b1: `python v2/tools/maak_leidingbeen_olie_heglig_fujairah.py` (één OSM-way als FeatureCollection, `olie-heglig-fujairah-leiding-heglig-bashayer.geojson`). b3: `maak_havenaanloop.py` van 19.4085,37.3052 naar 19.5908,37.4963 (`olie-heglig-fujairah-aanloop-bashayer.geojson`). b4: MARNET-router, snap begin 0,000 km, snap Fujairah 10,472 km op zeeknoop 8407. b5: letterlijke omgekeerde kopie van `olie-habshan-chiba-aanloop-fujairah.geojson` (`olie-heglig-fujairah-aanloop-fujairah.geojson`). Geen profiel, geen extract, geen via-punt, geen vlucht, geen fase D/E.

**Toets.**
- b1: OSM 1.475,8 km tegen ~1.600 gepubliceerd (Wikipedia) = -7,8%, binnen de 15%; het verschil past bij het ontbrekende beginstuk (~32 km) en afronding.
- b4: geen gepubliceerde zeekm; 3.911 is een MARNET-uitkomst (de ontwerpschatting 3.400 vervalt).
- Naden: alle 0,00 km. Markers: alle op 0,00 tot 0,01 km van hun lijn.
- `toets_knikken.py`: zee-been 3 knikken, geen omkering of terugloop; de knikken in b1 liggen op de OSM-geometrie (spikes van 100-140 m bij Heglig en in de Rode-Zee-kuststrook, de leiding volgt het terrein). `toets_rechte_benen.py`: alleen de stippels b2 en b3 hebben omwegfactor 1,00 en dat is bedoeld (stippel met reden).

**Toelichting per stippel/aanloop/leiding.**
- b2 is een korte rechte stippel: de laadleiding van tankpark naar steiger staat niet in OSM.
- b3 is een haven-aanloop: MARNET reikt niet tot de Bashayer-kade (zeeknoop 5930 ligt 28,5 km buiten de steiger); het pad over water is 28,6 km.
- b5 is een haven-aanloop: de Fujairah-kade ligt 10,5 km van zeeknoop 8407; letterlijke kopie, geen tweede versie.
- b1 is doorgetrokken want OSM heeft de leiding (man_made=pipeline). De lijn begint waar het bewijs begint (OSM-begin 10.2945,29.3546, ~32 km N van de Heglig-CPF); er is geen stippel naar de CPF verzonnen.

**Afwijkingen van het ontwerp.** Geen: het eindpunt is Fujairah, zoals het id belooft. Bestemming Fujairah blijft een bron (aannemelijk), dat staat in de beennaam b4.

**Lessen.** (1) Tijdens een eerdere bake gaf `bak_stromen.sh` een syntaxfout op regel 13160 van een andermans functie; bij de herbake van deze stroom slaagt `bash -n` (0) en telt het bestand 0 CRLF. (2) Een leiding die in OSM een eindig beginstuk mist (hier ~32 km) wordt niet met een stippel aangevuld: de kaart toont wat gemeten is. (3) Zee-snap Fujairah (10,5 km) kost een omgekeerde aanloop-kopie, geen nieuwe berekening.
