# Routebrief (licht) · nikkel — Ramu NiCo (Papoea-Nieuw-Guinea) → Basamuk → Caofeidian (China)

**stroom-id:** `nikkel-ramu-caofeidian` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** nikkel-kobalt-ertsslurry van de Kurumbukari-mijn per **leiding** (135 km, niet in OSM → stippel) naar de
Basamuk-HPAL-plant aan de kust, daar MHP (mixed hydroxide precipitate), per **zeeschip** door de Bismarckzee, Filipijnenzee,
Luzon-/Taiwanstraat en Gele Zee naar de MCC Ruimu-nikkelsulfaat/precursor-fabriek (MCC Ramu New Energy) in Caofeidian, Tangshan.
**Welke as van het verhaal:** de eerste nikkel-slurryleiding en de Chinese MCC-integratie — MHP uit een Chinees-eigen PNG-mijn
(MCC 67 %) naar een Chinese eigen raffinaderij. Jaarvolume: **34,3 kt Ni in MHP (2022, [1])**; doel 2026 **33,1 kt Ni** (Q2 2026:
8,2 kt Ni) [7]. Alleen een DEEL van de MHP gaat naar Caofeidian [2]: aandeel niet gebrond → leg geen tonnage op het been.

## 1 · Ketenkaart
```
Kurumbukari-mijn `ni-ramu-mijn` ──(b1 leiding · Ramu-slurryleiding · 135 km gepubliceerd, hemelsbreed 105 · stippel, geen OSM-way)──►
 Basamuk-plant `ni-ramu-basamuk` / pier `ni-ramu-basamuk-pier` ──(b2 zee · haven-aanloop · 126 km · stippel)──► zeeknoop 2643
 ──(b3 zee · Bismarckzee → Filipijnenzee → Taiwanstraat → Gele Zee → Bohai · 6.021,8 km, MARNET)──► zeeknoop 9649 (Bohai-baai)
 ──(b4 zee · haven-aanloop · 54,5 km · stippel)──► Caofeidian-kade `ni-caofeidian-kade`
 ──(b5 truck · last mile · 2,0 km · stippel)──► MCC Ruimu `ni-ruimu-fabriek` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `ni-ramu-mijn` → `ni-ramu-basamuk` | Ramu-slurryleiding Kurumbukari → Basamuk | 135 gepubliceerd [1]; hemelsbreed 104,6, geen wegkm | `--stippel "leiding\|…"` (geen man_made=pipeline in het papoea-extract) | ja — net reikt niet |
| b2 | B | zee | `ni-ramu-basamuk-pier` → zeeknoop 2643 (-4.8000,147.0000) | haven-aanloop Basamuk-baai (kade > 5 km van de zeeknoop) | 125,9 gemeten | rechte stippel (maak_havenaanloop: time-out 300 s) | ja |
| b3 | B | zee | zeeknoop 2643 → zeeknoop 9649 (38.8910,117.8503) | Bismarckzee → Filipijnenzee → Taiwanstraat → Gele Zee → Bohai | 6.021,8 gemeten (ontwerp 6.300-6.800 was te hoog) | MARNET | nee |
| b4 | B | zee | zeeknoop 9649 → `ni-caofeidian-kade` | haven-aanloop Bohai (kade 54,5 km van de knoop) | 54,5 gemeten | rechte stippel (maak_havenaanloop: time-out 300 s; landtoets 0 km) | ja |
| b5 | C | truck | `ni-caofeidian-kade` → `ni-ruimu-fabriek` | Caofeidian-industriezone, kade → fabriek | 2,0 hemelsbreed, geen wegkm | `--stippel "truck\|…"` (last mile, geen net op deze korrel) | ja |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-ramu-mijn` | mijn + beneficiatie (kop van de leiding) | Kurumbukari (Ramu NiCo) | -5.5819, 145.1947 | [1][8][10] OSM-way 793535755 | aannemelijk (z14 gezien: punt aan de westrand van het kale mijn-/terrasterrein, ~0,4 km buiten de ontgonnen grond) |
| `ni-ramu-basamuk` | HPAL-plant / MHP (voet van de leiding) | Basamuk Refinery, Basamuk Bay | -5.5422, 146.1388 | [1][10] OSM-way 672034115 | bron-gelegd (z15 gezien: procesplant met tankenpark en loodsen op de kustvlakte, punt op de oostrand) |
| `ni-ramu-basamuk-pier` | overslag leiding/plant → zee | Basamuk-pier | -5.5397, 146.1395 | [10] OSM-pier 893594415 | bron-gelegd (z15 gezien: noordoostpunt van het plantterrein aan het water; de pier zelf is op 4,8 m/px niet los te zien) |
| `ni-caofeidian-kade` | overslag zee → land | Caofeidian-kade, Tangshan Port | 38.9851, 118.4682 | [9] | aannemelijk (z15 gezien: kadefront met bulkschepen aan de westrand van het terminalterrein; welke steiger de MHP lost is niet gebrond; ontwerp-punt 38.9851,118.4743 lag 0,6 km landinwaarts in het terminal-emplacement) |
| `ni-ruimu-fabriek` | fase C-knoop (nikkelsulfaat/precursor) | MCC Ruimu / MCC Ramu New Energy, Caofeidian | 38.9896, 118.4909 | [3][5][6][10] | bron-gelegd (z15 gezien: industrieel complex met lange blauwe loodsen, tankkoepels en havenspoor; Nominatim-punt van 中冶瑞木新能源) |

## 4 · Via-punten
Geen: geen wegbeen, geen spoorbeen. De leiding is één rechte stippel mijn → plant; zee loopt via de router.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kurumbukari + Basamuk | MCC Ramu NiCo (MCC 67,02 %, Nickel 28 8,56 %) | lateriet-erts → slurry → MHP | 34,3 kt Ni (2022); doel 2026 33,1 kt Ni | [1][7][8] |
| MCC Ruimu (Caofeidian) | MCC Ramu New Energy (MCC 51 %, Gotion 30 %, BYD 10 %) | MHP → nikkelsulfaat + NCM-precursor | fase I+II: 100 kt nikkelsulfaat, 50 kt precursor per jaar; 2021 ~51 kt sulfaat | [3][5][6] |

## 6 · Stoppunt
De brief stopt bij de poort van MCC Ruimu: de fabriek is de beargumenteerde afnemer (WoodMac: MCC bouwde de raffinaderij voor een deel van de Ramu-MHP [2]);
verder (precursor naar batterijfabrieken) is niet per zending gebrond, fase D/E vervallen.

## 7 · Open punten
- **Aandeel MHP naar Caofeidian**: alleen WoodMac noemt dat een DEEL erheen gaat; rest-afnemers en zendingen niet gebrond. Eén bron → "aannemelijk" in de beennaam van b3.
- **Fabriek-identiteit**: Ruimu = Ramu bevestigd via WoodMac-assetpagina [3] (feed uit de MCC Ramu-mijn) en 36kr-bedrijfsregister [6]; geen tweede bron over MHP-routing zelf.
- **Slurryleiding niet gekarteerd** in OSM: tracé onbekend, getekend als rechte stippel (hemelsbreed 104,6 km tegen 135 km gepubliceerd); een satelliet-tracé zou kunnen maar is niet gedaan (licht).
- **Welke Caofeidian-steiger** de MHP lost is onbekend; kade-punt staat aan het kadefront op site-niveau.
- **Zeeknoop 9649 ligt 47 km voorbij de kade**: de zeelijn passeert Caofeidian op ~29 km en overschiet; de aanloop wijkt dus terug. Bewust zo gelaten (binding voor de keten).
- **Productie 2026**: Ramu draait (Q2 2026: 8.234 t Ni) [7], maar HPAL-treinen hebben stops; een PNG-havenban voor ladingen vertraagde in 2020 MHP-zendingen [4].

## 8 · Bronnen
[1] Wikipedia, "Mining in Papua New Guinea" (leiding 135 km, Basamuk, 34.302 t Ni 2022). https://en.wikipedia.org/wiki/Mining_in_Papua_New_Guinea
[2] Wood Mackenzie, "Ramu nickel operation" ("dedicated refinery … at Caofeidian"). https://www.woodmac.com/reports/metals-ramu-nickel-operation-15932037
[3] Wood Mackenzie, "Caofeidian, MCC Ramu nickel sulphate refinery" (eigenaar, feed, 51,3 kt sulfaat 2021). https://www.woodmac.com/reports/metals-caofeidian-mcc-ramu-nickel-sulphate-refinery-150003965/
[4] SMM/Metal.com, Chinese nickel sulphate producers and PNG vessel ban (MHP 2019: 32.766 t Ni). https://news.metal.com/en/newscontent/101056352-chinese-nickel-sulphate-producers-facing-raw-material-supply-woes-as-papua-new-guinea-bans-vessels-at-ports
[5] Mysteel, "MCC Ramu New Energy phase II commences operation", 2026-01-27 (Caofeidian, 100 kt sulfaat). https://www.mysteel.net/news/5111559-flash-mcc-ramu-new-energy-phase-ii-commences-operation
[6] 36kr PitchHub, 中冶瑞木新能源科技有限公司 (adres Caofeidian, aandeelhouders). https://pitchhub.36kr.com/project/2001603690012804
[7] Nickel 28, Ramu Q2 2026 operating performance (8.234 t Ni, doel 33.100 t). https://nickel28.com/_resources/news/nr-20260810.pdf
[8] Wikipedia, "Ramu Nickel Mine" (MCC 67,02 %, Nickel 28 8,56 %). https://en.wikipedia.org/wiki/Ramu_Nickel_Mine
[9] Wikipedia, "Port of Tangshan" (Caofeidian-havengebied). https://en.wikipedia.org/wiki/Port_of_Tangshan
[10] OpenStreetMap/Nominatim (ODbL): 中冶瑞木 = 38.9896,118.4909; Basamuk Refinery = -5.5419,146.1354. https://nominatim.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-nikkel-ramu-caofeidian-{mijn,basamuk,basamuk-pier,kade,ruimu}.png` (z14-z15).
[12] Asian Metal, "MCC new material project comes on stream" (fase I Caofeidian, 2018-12; alleen via zoekresultaat, pagina niet geladen). https://www.asianmetal.com/news/1465207/MCC-new-material-project-comes-on-stream-

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
`bash v2/tools/bak_stromen.sh nikkel-ramu-caofeidian` → `v2/data/stroomroute-nikkel-ramu-caofeidian.json` (13,0 KB, versie 2, lonlat).
Functie `bak_nikkel_ramu_caofeidian`; geen profiel in `maak_stroombeen_weg.py` (geen weg- of spoorbeen), geen via-punten, geen kopie.

| # | modaliteit | km | naad | stippel | been |
|---|---|---|---|---|---|
| 1 | leiding | 104,6 | – | ja | Ramu-slurryleiding Kurumbukari → Basamuk (hemelsbreed; 135 km gepubliceerd) |
| 2 | zee | 125,9 | 0,29 | ja | haven-aanloop Basamuk-baai (pier → zeeknoop 2643) |
| 3 | zee | 6.021,8 | 0,00 | nee | MARNET zeeknoop 2643 → zeeknoop 9649 (aannemelijk: één bron voor de bestemming) |
| 4 | zee | 54,5 | 0,00 | ja | haven-aanloop Caofeidian-kade (zeeknoop 9649 → kade) |
| 5 | truck | 2,0 | 0,00 | ja | last mile kade → MCC Ruimu |

Totaal 6.308,8 km · 625 punten · 4 markers (mijn, Basamuk-plant, Caofeidian-kade, Ruimu), alle op de lijn (0,0 km).
**Toets.** Zee b3 6.021,8 km = de gemeten waarde uit de brief. Grootste naad 0,29 km (plant → pier, procesgat, blijft staan). `toets_knikken`: 3 bochten >= 60 gr bij Okinawa/Ryukyu (25,98-26,40 N, 127,4-127,8 E; echte straatpassage), 0 omkeringen. `toets_rechte_benen`: b1, b2 en b4 zijn rechte stippels met reden.
**Stippels.** b1 leiding niet in OSM (rechte lijn 104,6 tegen 135 km gepubliceerd: de ±15%-toets geldt niet, geen wegkm). b2/b4 haven-aanloop als rechte lijn omdat `maak_havenaanloop.py` in de briefronde na 300 s geen resultaat gaf (geen tweede poging); b2 loopt 2,1 km over land bij het pier-uiteinde. b5 last mile 2,0 km hemelsbreed, geen net op deze korrel.
**Bevinding.** Zeeknoop 9649 ligt 47 km voorbij de kade: b3 overschiet Caofeidian en b4 wijkt terug (zichtbare hoek in de lijn, bewust gelaten). De Caofeidian-steiger is niet gebrond. Aandeel MHP naar Caofeidian alleen WoodMac. Geen ankerverschuiving.
**Lessen.** Een keten zonder landbeen met profiel bakt in een enkele run (~1 minuut); een leiding die niet in OSM staat blijft een eerlijke stippel, de keten blijft overwegend doorgetrokken op de zeeroute.
