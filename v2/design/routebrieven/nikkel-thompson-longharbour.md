# Routebrief (licht) · nikkel — Thompson → Trois-Rivières → Long Harbour (Canada)

**stroom-id:** `nikkel-thompson-longharbour` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) · **status:** gebakken
**Keten in één zin:** nikkelconcentraat van de Thompson-concentrator (Manitoba) gaat per **spoor** (~3.921 km: Hudson Bay Railway → Winnipeg → Hornepayne → Capreol → Sudbury → Toronto → Montréal → Trois-Rivières) naar de haven van Trois-Rivières (Québec), ligt daar opgeslagen en gaat per **zeeschip** (~1.799 km, Saint-Laurent → Cabotstraat → Placentia Bay) naar Vale's Long Harbour-raffinaderij (Newfoundland). De bestemming Trois-Rivières is aannemelijk (één bron: Vale 20-F), de spoorcorridor en de kade zijn eigen afleiding [1][2].
**Welke as van het verhaal:** Vale's Thompson → Long Harbour-reserveketen: sinds H2 2021 gaat het meeste Thompson-concentraat naar Long Harbour, de rest naar Sudbury [1][2]. **7,9 kt Ni/j** finished nickel uit Thompson-erts (2023; 9,9 in 2022), Vale 20-F FY2023 [2]; het aandeel dat via Trois-Rivières gaat is niet gepubliceerd. Eenheid: kt Ni per jaar.

## 1 · Ketenkaart
```
Thompson-emplacement `ni-thompson-emplacement` ──(b1-b5 spoor · HBRY → The Pas → Winnipeg → Hornepayne → Foleyet → Capreol · 2.658 km, KOPIE thompson-sudbury)──►
Capreol ──(b6 spoor · CN Bala Sub · 43 km)──► Sudbury ──(b7 spoor · Sudbury → MacMillan Yard, Toronto · 466 km, KOPIE sudbury-kristiansand)──►
MacMillan ──(b8 spoor · CN Kingston Sub · 541 km, KOPIE sudbury-kristiansand)──► Taschereau Yard, Montréal
──(b9 spoor · Joliette → Garneau-keerpunt Shawinigan → Trois-Rivières · 213 km, aannemelijk: één bron)──► Trois-Rivières-kade `ni-troisrivieres-kade`
──(b10 zee · haven-aanloop 26 km, stippel)──► zeeknoop 6352 ──(b11 zee · MARNET · 1.578,5 km)──► zeeknoop 703
──(b12 zee · haven-aanloop 194 km, stippel)──► Long Harbour-kade `ni-longharbour-kade` ──(b13 truck · eigen terrein 1,6 km, stippel, KOPIE voiseysbay)──► Long Harbour-fabriek `ni-longharbour-fabriek` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1-b5 | A | spoor | `ni-thompson-emplacement` → Capreol | HBRY, Winnipeg-lijn, CN Hornepayne/Foleyet: **LETTERLIJKE KOPIE van de vijf runs `spoorroute-nikkel-thompson-sudbury-{thompson-thepas,thepas-winnipeg,winnipeg-hornepayne,hornepayne-foleyet,foleyet-capreol}`** | 369,7 + 795,6 + 1.016,4 + 237,5 + 238,9 = **2.658,1** (OSM-graaf; geen gepubliceerde lengte) [5] | kopie bestaande geojsons | nee |
| b6 | A | spoor | Capreol → Sudbury | CN Bala Sub, 50 edges, snap 0,27/0,16 km | **43,4** (OSM-graaf; hemelsbreed 16,9) | toets_spoorroute (eigen run) | nee |
| b7 | A | spoor | Sudbury → MacMillan Yard | CN Bala Sub: **KOPIE `spoorroute-nikkel-sudbury-kristiansand-sudbury-macmillan`** | **465,7** [6] | kopie | nee |
| b8 | A | spoor | MacMillan → Taschereau Yard | CN Kingston Sub: **KOPIE `spoorroute-nikkel-sudbury-kristiansand-macmillan-taschereau`** | **541,0** [6] | kopie | nee |
| b9 | A | spoor | Taschereau → `ni-troisrivieres-kade` | CN via Joliette, Garneau-knoop Shawinigan, Garneau Sub naar Trois-Rivières; lijn/vervoerder niet gebrond (aannemelijk: één bron) | **212,6** (OSM-graaf, 361 edges; hemelsbreed 130; snap 0,11/0,23 km) | toets_spoorroute (eigen run) | nee |
| b10 | B | zee | `ni-troisrivieres-kade` → zeeknoop 6352 (46.4321, -72.2818) | haven-aanloop **26,2 km**: kade ligt 23,3 km van de zeeknoop (> 5 km) | maak_havenaanloop (cel 0,02° kaal), 0,00 km over land | stippel-geojson | ja (MARNET reikt niet) |
| b11 | B | zee | zeeknoop 6352 → zeeknoop 703 (46.1000, -54.0000) | Saint-Laurent → Cabotstraat → ten zuiden van Newfoundland | **1.578,5** MARNET (hemelsbreed 1.403; geen gepubliceerde zeelengte; ontwerp ~2.000 indicatief) | MARNET | nee |
| b12 | B | zee | zeeknoop 703 → `ni-longharbour-kade` | haven-aanloop **193,8 km** via twee waterpunten (46.9, -54.7) en (47.3, -54.2); kade 147,7 km van 703 en 103,9 km van knoop 762 | handmatig, landtoets ne_10m: 0 km land behalve ~0,9 km aan de kade | stippel-geojson | ja (MARNET reikt niet) |
| b13 | C | truck | `ni-longharbour-kade` → `ni-longharbour-fabriek` | eigen terrein/conveyor, geen openbaar net: **KOPIE van de stippelregel in `bak_nikkel_voiseysbay_longharbour`** | **1,6** [7] | stippel | ja (last mile, geen net op deze korrel) |
Totaal **5.720,9 km** (spoor 3.920,8 · zee 1.798,5 · truck 1,6) over 13 benen, proefbake 2026-10-29 in de scratchpad (niet in `v2/data`). Naden 0,00 km behalve zee-kade 0,23 km. Spoor heeft geen gepubliceerde lengte: de ±15%-toets is een indicatie; zee 1.798,5 (aanloop + MARNET + aanloop) tegen ~2.000 indicatief = −10%.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-thompson-emplacement` | concentrator-load-out / kop spoor | Thompson-emplacement (Vale-concentraat) | 55.7407, -97.8300 | hergebruikt letterlijk uit `nikkel-thompson-sudbury` §3 [5] | aannemelijk (daar z15 gezien: groot emplacement met tientallen sporen en loodsen zuidoost van de stad; load-out niet te onderscheiden) |
| `ni-troisrivieres-kade` | overslag spoor → zee, opslag | Port de Trois-Rivières, bulkkade zuidwestelijk van de stadskade | 46.3302, -72.5466 | [1][2]; plek eigen z16/z17-blik | aannemelijk (z16/z17 gezien: kade met een gemeerd rood bulkschip, korenzuil/-silo, lange witte opslagloodsen, tankenpark en havensporen; welke loods nikkelconcentraat opslaat is niet te zien. Het Wikipedia-punt 46.3405, -72.5394 ligt aan de cruisekade en is niet gebruikt) |
| `ni-longharbour-kade` | overslag zee → land | Long Harbour-kade (Vale) | 47.4230, -53.8230 | hergebruikt letterlijk uit `nikkel-voiseysbay-longharbour` §3 [7] | bron-gelegd (daar z17: wharf met laadconveyor-overkapping, bulkloods, gemeerd schip) |
| `ni-longharbour-fabriek` | raffinaderij (hydromet) | Long Harbour Processing Plant (Vale) | 47.4101, -53.8133 | idem [7] | bron-gelegd (daar z16: procescomplex ~1,6 km zuid van de kade) |

## 4 · Via-punten (alleen spoor; elk pint een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1/b2 | 1 | The Pas | 53.8245, -101.2506 | zie `nikkel-thompson-sudbury` §4 (kopie, geen eigen keuze) |
| b2/b3 | 2 | Winnipeg, Symington Yard (westkant) | 49.8688, -97.0480 | idem |
| b3/b4 | 3 | Hornepayne | 49.2205, -84.7758 | idem; houdt de route op de CN-lijn naar Foleyet/Capreol |
| b4/b5 | 4 | Foleyet | 48.2439, -82.4397 | idem |
| b5/b6 | 5 | Capreol | 46.7058, -80.9214 | begin van de Bala Sub; opent b6 |
| b6/b7 | 6 | Sudbury (CN Bala Sub) | 46.5786, -80.7993 | begin van de gekopieerde run b7 (zonder dit punt een omkering bij MacMillan, 43.667, -79.465, in een vrije Capreol–MacMillan-run) |
| b7/b8 | 7 | MacMillan Yard (CN, Vaughan) | 43.8119, -79.5111 | houdt de route om Toronto-lakeshore; gekopieerd uit [6] |
| b8/b9 | 8 | Taschereau Yard (CN, Montréal) | 45.4686, -73.6861 | pint de Kingston Sub door Montréal; gekopieerd uit [6] |
Geen via-punt op b9: de vrije run Taschereau → kade is stabiel (zelfde lijn als de Val-d'Or–Trois-Rivières-run in [8]). Geen stadscentra: alle punten zijn spoorknopen of -terreinen.
Omkeringen (`toets_knikken`, proefbake): 4 TERUGLOOP, alle verklaard: twee uit de gekopieerde runs (MacMillan 43.6673/-79.4652 en 43.8263/-79.5153, bekend uit `nikkel-sudbury-kristiansand` §9), één in het Taschereau-rangeerterrein (45.4651/-73.6834: de router maakt daar een lus van ~12 km tussen aankomst en vertrek), één bij de Garneau-/Shawinigan-knoop (46.5595/-72.7307: mogelijk een echte wye, ook in [8] gevonden, niet bevestigd). Eén krappe zeebocht (61°, R 5,3 km) bij 46.84/-71.18 (Saint-Laurent). Geen reparatie.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Thompson (mijn + concentrator) | Vale Canada tot 16 okt 2026, daarna Exiro Nickel (Vale 18,9%, meerjarige offtake) | erts → nikkelconcentraat | 7,9 kt Ni/j (2023) | [2][4] |
| Trois-Rivières | haven (opslag) | concentraat per trein → opslag → schip | niet gepubliceerd | [1][2] |
| Long Harbour Processing Plant | Vale Base Metals | Ni-sulfideconcentraat (Voisey's Bay + Thompson) → afgewerkt nikkel | nameplate 50 kt Ni/j | [7] |

## 6 · Stoppunt
De brief stopt bij de Long Harbour Processing Plant: dat is het eindproduct (afgewerkt nikkel) en geen bron noemt een vervolgzending van Thompson-nikkel specifiek; fase D/E vervalt zoals in `nikkel-voiseysbay-longharbour`.

## 7 · Open punten
- **Spoorcorridor is eigen afleiding.** Vale noemt alleen "rail naar Trois-Rivières" [1][2]. De getekende lijn volgt de bindende toetsaanpassing (via Capreol, Toronto en Montréal). De OSM-router vindt Hornepayne → Trois-Rivières ook via Cochrane, Taschereau (QC), La Tuque en Garneau in **1.329 km** (vrije run, 2026-10-29), tegen **1.739 km** via Capreol; welke lijn Vale gebruikt staat nergens. Alleen b1-b9 zouden wijzigen.
- **Kade en opslag in Trois-Rivières niet gebrond:** welke terminal/loods het concentraat opslaat is onbekend; `ni-troisrivieres-kade` is een bulkkade met gemeerd schip, geen bevestigde nikkelkade.
- **Verdeling Sudbury / Trois-Rivières / Long Harbour** niet gepubliceerd; 7,9 kt Ni/j is voor heel Thompson. Winnipeg wordt in de bron als alternatieve overslag genoemd, niet getekend [1][2].
- **Eigenaarswissel Thompson:** Vale verkocht het Thompson Mine Complex per 16 okt 2026 aan Exiro Nickel (81,1%), houdt 18,9% en een meerjarige offtake voor het concentraat; waar dat concentraat daarna verwerkt wordt noemt de 6-K niet [4]. De ketenjaren 2021-2023 blijven de bronbasis.
- **Zeebeen:** Cabotstraat en winterijs niet gemodelleerd; zeenet reikt niet tot de kade (twee haven-aanlopen, b10 en b12). Aanloop b12 volgt twee door de toets aangewezen waterpunten, geen bevaren geul.
- **Thompson, Trois-Rivières ontbreken in `nikkel-sitelaag.json`**; centraal toe te voegen. Het 6-K-fragment van mei 2022 over de overslag in Trois-Rivières kwam alleen via een zoekfragment binnen, niet zelf gelezen.

## 8 · Bronnen
[1] Vale S.A., Form 20-F FY2022: Thompson-concentraat per truck/trein naar Winnipeg of direct per trein naar Sudbury of Trois-Rivières, opslag in de haven en per schip naar Long Harbour (fragment via zoekresultaat, passage niet volledig gelezen). https://www.sec.gov/Archives/edgar/data/917851/000129281423001516/valeform20f_2022.htm
[2] Vale S.A., Form 20-F FY2023: idem; sinds H2 2021 meeste Thompson-concentraat naar Long Harbour; Thompson 7,9 kt Ni (2023), 9,9 (2022). https://www.sec.gov/Archives/edgar/data/917851/000129281424001463/valeform20f_2023.htm
[3] Vale S.A., Form 6-K mei 2022 (zoekfragment; niet zelf gelezen). https://www.sec.gov/Archives/edgar/data/917851/000129281422002601/vale20220531_6k.htm
[4] Vale S.A., Form 6-K 2026-10-16: Exiro Nickel nieuwe eigenaar Thompson Mine Complex (Vale 18,9%), meerjarige offtake voor concentraat (gelezen). https://www.sec.gov/Archives/edgar/data/0000917851/000129281426004942/vale20261016_6k.htm
[5] Routebrief `nikkel-thompson-sudbury` §2-§4 en §9: emplacement-anker, vijf spoorruns b1-b5 (`v2/design/routebrieven/nikkel-thompson-sudbury.md`).
[6] Routebrief `nikkel-sudbury-kristiansand` §9: Sudbury → MacMillan → Taschereau, bekende TERUGLOOP bij MacMillan; ook gebruikt in `nikkel-raglan-sudbury`.
[7] Routebrief `nikkel-voiseysbay-longharbour` §3 en bake-functie `bak_nikkel_voiseysbay_longharbour`: Long Harbour-kade (47.4230, -53.8230), fabriek (47.4101, -53.8133), stippel kade → fabriek.
[8] Routebrief `lithium-nal-quebec` §7: spoor Val-d'Or → Trois-Rivières, keerpunt bij Shawinigan (46.5595, -72.7307).
[9] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-nikkel-thompson-longharbour-troisrivieres-{haven,kade,kade-z17}.png` (z14, z16, z17, 2026-10-29).
[10] OSM 1-op-1-spoornet via `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`) en MARNET-router (`v2/build-cache/marnet-preais`), runs 2026-10-29; `maak_havenaanloop.py` voor b10.
[11] BNN Bloomberg, 2026-02-19, "Vale to form new consortium to invest in Thompson mine complex" (alleen titel uit zoekresultaat). https://www.bnnbloomberg.ca/business/2026/02/19/vale-to-form-new-consortium-to-invest-in-thompson-mine-complex/

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
**Recept:** `bash v2/tools/bak_stromen.sh nikkel-thompson-longharbour` (functie `bak_nikkel_thompson_longharbour`). Uitvoer `v2/data/stroomroute-nikkel-thompson-longharbour.json`, 159 KB, 13 benen, 12 markers, 5.720,9 km (spoor 3.920,9 · zee 1.798,5 · truck 1,6), versie 2, lonlat. Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen); geen extract nodig.

| # | modaliteit | km gebakken | brief | stippel | geometrie |
|---|---|---|---|---|---|
| 1-5 | spoor | 369,7 + 795,6 + 1.016,4 + 237,5 + 238,9 = 2.658,1 | 2.658,1 | nee | letterlijke kopie `spoorroute-nikkel-thompson-sudbury-*` |
| 6 | spoor | 43,4 | 43,4 | nee | eigen run `spoorroute-nikkel-thompson-longharbour-capreol-sudbury` |
| 7 | spoor | 465,7 | 465,7 | nee | kopie `…sudbury-kristiansand-sudbury-macmillan` |
| 8 | spoor | 541,0 | 541,0 | nee | kopie `…sudbury-kristiansand-macmillan-taschereau` |
| 9 | spoor | 212,6 | 212,6 | nee | eigen run `…taschereau-troisrivieres` (console 210,0 vóór spike-schoonmaak; lijn 212,6 gemeten) |
| 10 | zee | 26,2 | 26,2 | ja | haven-aanloop Trois-Rivières |
| 11 | zee | 1.578,5 | 1.578,5 | nee | MARNET 6352 → 703 |
| 12 | zee | 193,8 | 193,8 | ja | haven-aanloop Long Harbour (twee waterpunten) |
| 13 | truck | 1,6 | 1,6 | ja | stippel kade → fabriek |

**Toets:** alle gemeten benen gelijk aan de brief (0%); naden 0,00 km behalve zee-kade 0,23 km (procesgat, blijft staan); markers 0,00–0,27 km van hun lijn; geen gepubliceerde spoorkm, dus de ±15%-toets is een indicatie. `toets_knikken`: 4 TERUGLOOP (MacMillan 43.6673/-79.4652 en 43.8263/-79.5153 in de gekopieerde runs; Taschereau-rangeerterrein 45.4651/-73.6834; Garneau-/Shawinigan-knoop 46.5595/-72.7307), alle vier verklaard in §4; één spike 46.4859/-80.8324 in de gekopieerde Sudbury-run; één krappe zeebocht (61°, R 5,3 km) bij 46.84/-71.18. Niet gerepareerd. `toets_rechte_benen`: alleen de stippelbenen zijn recht (aanlopen volgen een berekend waterpad, de truckstippel is 1,6 km).

**Stippels (alle drie "hier reikt het net niet"):** b10 Trois-Rivières-kade ligt 23,3 km van MARNET-zeeknoop 6352 (LAR-586, aanloop 26,2 km, 0 km over land); b12 Long Harbour-kade ligt 147,7 km van knoop 703 (aanloop 193,8 km via waterpunten 46.9/-54.7 en 47.3/-54.2, geen bevaren geul); b13 eigen terrein, kopie van de regel in `bak_nikkel_voiseysbay_longharbour`. Geen lucht, leiding, weg of binnenvaart. "Aannemelijk: één bron" (bestemming Trois-Rivières, Vale 20-F) staat in de beennamen van b6 en b9 en van het zeebeen; de lijnen zijn doorgetrokken.

**Hergebruikte ankers:** Thompson-emplacement uit `nikkel-thompson-sudbury`; Long Harbour-kade en -fabriek uit `nikkel-voiseysbay-longharbour`; MacMillan en Taschereau uit `nikkel-sudbury-kristiansand`. Nieuw: `ni-troisrivieres-kade` (aannemelijk, z16/z17 gezien in de brief; geen nieuwe satellietrun).

**Lessen:** (1) de aanloop-geojsons en spoorruns uit de proefbake bleven bruikbaar; de bake draaide ongewijzigd na de proefmaten van de brief. (2) De vrije run Hornepayne → Trois-Rivières via Cochrane en La Tuque (1.329 km, 410 km korter) blijft een open alternatief; alleen b1-b9 zouden wijzigen. (3) Centraal: register (`ni-tl`), sitelaag voor Thompson en Trois-Rivières, bundel.
