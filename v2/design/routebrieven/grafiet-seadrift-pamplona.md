# Routebrief (licht) · grafiet — Seadrift (Texas) → Corpus Christi → Bilbao → Pamplona (Spanje)

**stroom-id:** `grafiet-seadrift-pamplona` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** gecalcineerde petroleum-naaldcokes uit de eigen cokesfabriek van GrafTech (Seadrift Coke LP, Calhoun County TX) gaat per **spoor** (werkaanname) ~150 km naar de kade in Corpus Christi Inner Harbor, per **zeeschip** (MARNET, ~9.390 km, Golf van Mexico → Straat van Florida → Atlantische Oceaan → Golf van Biskaje) naar Bilbao (Santurtzi-kade) en per **truck** ~190 km (AP-68, A-1, A-10) naar de elektrodefabriek GrafTech Iberica in Ororbia bij Pamplona; stoppunt = elektrodefabriek.
**Welke as van het verhaal:** *de transatlantische voeding van de Europese elektrodefabriek*, en de opvolger van de uitdovende Monterrey-stroom (sluit Q2 2027; pinstock verhuist naar Pamplona) [1][2][5]. Seadrift: nameplate ~140 kt/j gecalcineerde naaldcokes, "de meerderheid" van GrafTechs behoefte [1]. **Aandeel Pamplona niet gepubliceerd**; geen volume voor deze lijn. Eenheid kt naaldcokes per jaar, peiljaar 2025. **Aannemelijk: één bron** — geen bron noemt vervoer, haven of leveringen Seadrift → Pamplona; alleen dat Seadrift de cokes van GrafTech levert [1][4] en Pamplona een GrafTech-fabriek is [4]. De eerder afgewezen `grafiet-seadrift-calais` had dezelfde zwakte; de onzekerheid staat in de beennamen.

## 1 · Ketenkaart
```
Seadrift Coke LP `gr-seadrift-cokes` ──(b1 spoor · UP-aansluiting Placedo → Odem/Robstown-zijde → Corpus Christi · router 149,5 km, hemelsbreed 98 km · aannemelijk: één bron)──►
Corpus Christi Inner Harbor, kade `gr-corpuschristi-kade` ──(b2 zee · MARNET · 9.390 km · aannemelijk: één bron; stippel-haven-aanloop aan beide kanten, zie §2)──►
Bilbao, Santurtzi-kade `gr-bilbao-kade` ──(b3 truck · AP-68 → A-1 → A-10 → PA-30 · 190,5 km)──►
GrafTech Iberica, Ororbia `gr-pamplona-fabriek` (naaldcokes → grafietelektroden + pins) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor (werkaanname; truck is reserve) | `gr-seadrift-cokes` → `gr-corpuschristi-kade` | UP Calhoun-spoor via Placedo-wye (zelfde eerste ~100 km als seadrift-monterrey, géén kopie: andere staart) → Corpus Christi | hemelsbreed 98 km, router 149,5 km, geen spoorkm [12] | `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`), 153 edges | nee |
| b2a | B | zee (haven-aanloop) | `gr-corpuschristi-kade` → zeeknoop 4842 (27.8603,-97.4384) | — | 6,4 km kade ↔ zeeknoop | `maak_havenaanloop.py` haalde 300 s niet → rechte stippel | **ja** (MARNET reikt niet tot de kade) |
| b2 | B | zee | zeeknoop CC → zeeknoop 3523 (43.4074,-3.0657) | MARNET | ~9.390 km (router, kade→kade getest 9.389,6) [13] | MARNET `--been "zee|…"` | nee |
| b2b | B | zee (haven-aanloop) | zeeknoop 3523 → `gr-bilbao-kade` | — | 8,2 km | idem: rechte stippel | **ja** |
| b3 | C | truck | `gr-bilbao-kade` → `gr-pamplona-fabriek` | AP-68 → A-1 → A-10 → PA-30 | **geen gepubliceerde wegkm**; eigen OSM-meting 190,5 km (+0,2% tegen schatting 190) [14] | `maak_stroombeen_weg.py` (profiel `grafiet-seadrift-pamplona-bilbao-ororbia`, extract `spanje`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-seadrift-cokes` | feedstock / laadplek | Seadrift Coke LP, 8618 State Hwy 185 N, Port Lavaca TX — **hergebruikt uit `grafiet-seadrift-monterrey.md`** | 28.5134, -96.7946 | [4][6][7][11] | bron-gelegd (z15 opnieuw gezien: compact industriecomplex met tankbatterij en groen bassin in kreek- en weidegebied; spoor binnen 0,15 km). Sitelaagwaarde `w-seadrift-graftech` ligt 21,5 km te ver (centraal) |
| `gr-corpuschristi-kade` | overslag / zee | Corpus Christi Inner Harbor, zuidoever net W van de Harbor Bridge, bij groot wit magazijn — **hergebruikt uit `lithium-kathleenvalley-robstown.md`** | 27.8112, -97.4045 | [15][11] | aannemelijk (z15 gezien: kade met schip naast wit magazijn; terminalnaam niet vastgesteld; spoor binnen 0,04 km) |
| `gr-bilbao-kade` | overslag / zee | Puerto de Bilbao, Santurtzi, kade met magazijnlinten aan het binnenbekken (zone Muelle Reina Victoria / Princesa de España, terminal niet vastgesteld) | 43.3363, -3.0396 | [9][10][11] | aannemelijk (z15 gezien: lange kade met loodsen en schepen tegen de zuidoever van het havenbekken; geen bron koppelt déze kade aan GrafTech) |
| `gr-pamplona-fabriek` | verwerkingsknoop + losplek | GrafTech Iberica SL, Carretera de Astrain, Ororbia (Navarra) | 42.8134, -1.7435 | [4][8][11] | bron-gelegd (z15 gezien: fabrieksterrein met meerdere hallen in een rivierbocht ten zuidoosten van Ororbia; adres uit [4], punt = OSM `man_made=works`) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b3 | 1 | AP-68 zuid van Bilbao | 43.2378, -2.9503 | kiest de AP-68 (tolweg) i.p.v. de N-625/Basauri-route; op de doorgaande rijbaan (snap 0,00 km) |
| b3 | 2 | A-1/AP-1 oost van Vitoria-Gasteiz | 42.8725, -2.4872 | pint de ring om Vitoria-Gasteiz; niet in het centrum |
| b3 | 3 | A-10 bij Altsasu-Etxarri | 42.8951, -2.0849 | pint de Sakana-corridor (A-10) naar Pamplona i.p.v. de AP-15/N-121-route; snap 0,00 km |
Het spoorbeen b1 heeft geen via-punten: de router kiest zonder punten één corridor (Placedo-wye 28.6459,-96.8939 → Robstown-zijde ~27.94,-97.58 → Corpus Christi-West), net als in seadrift-monterrey.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Seadrift Coke LP | GrafTech | decant oil → gecalcineerde naaldcokes | nameplate ~140 kt/j | [1][4] |
| GrafTech Iberica, Ororbia | GrafTech | naaldcokes → grafietelektroden; neemt de pinstock van Monterrey over | capaciteit niet in de bronnen; −16 kt/j elektroden aangekondigd (productmix) [5] | [4][5] |

## 6 · Stoppunt
Elektrodefabriek Ororbia: fase D (staalfabrieken) wordt door geen bron aan deze fabriek gekoppeld; E vervalt. De keten stopt waar het bewijs stopt.

## 7 · Open punten
- **Geen bron noemt het vervoer** Seadrift → Pamplona (haven, schip, spoor/truck). Alle drie de modaliteiten en beide havens zijn aannames; Pamplona is wel de fabriek die na de Monterrey-sluiting de pinstock krijgt [2][5].
- **Spoor is werkaanname** (geleasete railcars, geen route [1]); reserve: truck Seadrift → Corpus Christi (~160 km). **Omkeringen** op b1 (toets_spoorroute): 168,5° Placedo-wye 28.6459,-96.8939 (gedeeld met seadrift-monterrey), 162,6° aansluitspoor 28.5184,-96.7859, 155,1° kadeeinde 27.8113,-97.4034 — OSM-topologie, na de bake met `toets_knikken.py` beoordelen.
- **Haven-aanlopen zijn schematisch:** `maak_havenaanloop.py` haalde 300 s niet (beide havens); rechte stippel over 6,4 resp. 8,2 km kruist hier en daar land (havenbekken niet in de 1:10M-kust). De router snapt los op 1,43 km (CC, via AIS-track) en 8,18 km (Bilbao).
- **Bilbao-terminal onbekend:** Santurtzi heeft meerdere concessiekades voor stukgoed en vaste bulk [10]; de gekozen kade is een satellietkeuze, geen bron. Alternatief Zierbena (buitenhaven) niet onderzocht.
- **Corpus Christi of Houston** als gulfhaven is een aanname (CC gekozen: dichtst bij Seadrift, kade al gelegd).
- Jaarvolume voor déze lijn niet gepubliceerd; Pamplona-aandeel van de 140 kt onbekend. Geen coördinaat verzonnen.

## 8 · Bronnen
[1] GrafTech, Form 10-K FY2025 — Seadrift ~140 kt, "majority" van de behoefte; capaciteit 178 kt; railcars geleast. https://www.sec.gov/Archives/edgar/data/931148/000093114826000017/gti-20251231.htm
[2] Argus Media, "GrafTech to shutter Monterrey electrode plant", 2026-09-01 — pinstock naar Pamplona. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2872327-graftech-to-shutter-monterrey-electrode-plant
[3] Engineering News, 2026-09-01 — zelfde aankondiging. https://engineeringnews.co.za/article/graphite-electrode-manufacturer-graftech-shuts-mexican-plant-2026-09-01
[4] GrafTech, "About us" — GrafTech Iberica SL, Carretera de Astrain S/N, Ororbia (Navarra); Seadrift = "one of the world's only standalone petroleum needle coke plants". https://www.graftech.com/about-us
[5] Steel Market Update, 2026-09-02 — −51 kt capaciteit: 35 kt Monterrey + 16 kt Pamplona (productmix). https://www.steelmarketupdate.com/2026/09/02/graftech-to-permanently-close-monterrey-electrode-plant/
[6] TCEQ, plain-language summary NSR 70898 (Seadrift Coke LP, Port Lavaca). https://www.tceq.texas.gov/downloads/permitting/air/bilingual/pending-permit-notices/70898-pls-english.pdf
[7] GrafTech Holdings, Form S-4/A 2010 — adres Seadrift Coke LP. https://www.sec.gov/Archives/edgar/data/0001492849/000119312510193073/ds4a.htm
[8] OpenStreetMap (ODbL), Geofabrik-extract `spanje` — Ororbia-fabriek (`man_made=works`) en wegen AP-68/A-1/A-10. https://download.geofabrik.de/europe/spain.html
[9] Wikipedia, "Port of Bilbao" — havencomplex in Santurtzi en Zierbena, ~15 km west van Bilbao. https://en.wikipedia.org/wiki/Port_of_Bilbao
[10] BOE-B-2019-560, concessie vaste bulk Muelle Princesa de España, Santurtzi. https://www.boe.es/boe/dias/2019/01/09/pdfs/BOE-B-2019-560.pdf
[11] Esri World Imagery via `v2/tools/sat_check.py` (2026-10-29, z15) — `v2/build-cache/satcheck/sat-grafiet-seadrift-pamplona-{seadrift,cc-kade,bilbao-kade,pamplona-fabriek}.png`.
[12] OSM-spoor 1-op-1 + `toets_spoorroute.mjs` — 149,5 km / 153 edges, snap 0,15/0,04 km (`spoorroute-grafiet-seadrift-pamplona-seadrift-cc.geojson`).
[13] `hecht_marnet.py route` (proefrun, niet geschreven naar v2/data) — zee kade→kade 9.389,6 km, snaps 1,43/8,18 km.
[14] `maak_stroombeen_weg.py --profiel grafiet-seadrift-pamplona-bilbao-ororbia` — 190,5 km, 3.085 punten, snaps ≤0,07 km.
[15] `v2/design/routebrieven/lithium-kathleenvalley-robstown.md` — Corpus Christi-kade 27.8112,-97.4045 (§3).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`bash v2/tools/bak_stromen.sh grafiet-seadrift-pamplona` (functie `bak_grafiet_seadrift_pamplona`) → `v2/data/stroomroute-grafiet-seadrift-pamplona.json`, 85 KB, versie 2, lonlat, 5 benen, 4 markers, totaal 9.615,4 km.

| # | modaliteit | km | brief | naad | beschrijving |
|---|---|---|---|---|---|
| 1 | spoor | 150,7 | router 149,5 (geen spoorkm) | 0 | Seadrift → CC-kade, voorgebakken `spoorroute-…-seadrift-cc.geojson`, 235 punten |
| 2 | zee, stippel | 6,4 | 6,4 | 0,04 | haven-aanloop CC, rechte stippel (schematisch) |
| 3 | zee | 9.259,5 | ~9.390 (kade-kade proefrun) | 0,00 | MARNET zeeknoop 4842 → 3523, 87 edges, 967 punten, snaps 0,000 km |
| 4 | zee, stippel | 8,2 | 8,2 | 0,00 | haven-aanloop Bilbao, rechte stippel (schematisch) |
| 5 | truck | 190,6 | eigen OSM-meting 190,5 | 0,00 | profiel `grafiet-seadrift-pamplona-bilbao-ororbia`, extract spanje, 3.085 punten |

**Markers** (4): Seadrift 0,15 km van de spoorlijn (spoorbegin ligt aan het sporennet, anker = site; binnen de norm), de drie andere 0,00 km.
**Recept:** b1 = voorgebakken spoor (raw1op1, zonder via-punten); b2a/b2b = rechte `--stippel` omdat `maak_havenaanloop.py` 300 s niet haalde (beide kades > 5 km van hun zeeknoop); b2 = `--been zee` tussen de zeeknopen, geen kade-kade zodat de naden dicht blijven; b3 = voorgebakken weg (3 via-punten, geen omweg). Geen lucht, leiding, kopie, last mile; geen fase D/E.
**Toelichting zee:** de zee-km (9.259,5) ligt 1,4% onder de proefrun kade-kade (9.389,6): die telde de snaps van 1,43 en 8,18 km mee; samen met de aanlopen 9.274 km. Geen gepubliceerde zee-km, dus geen norm.
**Toelichting stippels:** beide aanlopen zijn rechte schematische lijnen en kruisen deels land (havenbekken niet in de 1:10M-kust); het zeebeen begint en eindigt op de MARNET-zeeknoop.
**Toets:** naden max 0,04 km; json.load ok; modaliteiten {spoor, zee, truck}; `toets_rechte_benen`: alleen de twee stippels (terecht). `toets_knikken`: spoor 3 omkeringen (168,5 / 162,7 / 155,0 gr, OSM-topologie, geen terugloop), truck 0 omkeringen maar 10 knikken, alle spikes (63-107 gr, R 4-95 m) rond de fabriek bij 42,813-42,856 / -1,73 tot -1,75 (Ororbia, eindzone), zee 4 krappe bochten R 5-7 km (Bahama-kanaal, Biskaje).
**Bevindingen/open:** zie §7; daarnaast de knikken-cluster bij Ororbia (niet gerepareerd, geen terugloop) en de 0,15 km Seadrift-afstand tot het spoor.
**Lessen:** een voorgebakken weg- en spoorbeen uit de ontwerpfase hergebruiken scheelt de scans; zeebeen tussen zeeknopen (niet kade-kade) houdt de naden met stippelaanloop onder 0,05 km.
