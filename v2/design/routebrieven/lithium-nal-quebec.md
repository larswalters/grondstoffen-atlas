# Routebrief (licht) · Lithium — North American Lithium → Val-d'Or → Port de Québec (Canada)

**stroom-id:** `lithium-nal-quebec` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** spodumeenconcentraat (~5,0% Li2O) van de North American Lithium-mijn (Elevra, voorheen Sayona; La Corne,
Abitibi, Québec) gaat per truck ~60 km over de Route du Lithium en Route 111 naar de transload van Solurail in Val-d'Or en
vandaar per CN-spoor ~763 km (via Senneterre, La Tuque, Shawinigan en Trois-Rivières) naar het Port de Québec (sector Beauport),
waar de lading FOB wordt verkocht; de afnemer is niet gepubliceerd, dus de lijn stopt in Québec.
**Welke as van het verhaal:** *Noord-Amerikaanse hardrock-as met een draaiende mijn* — NAL produceerde in FY26 (jul 2025–jun 2026)
197.967 dmt concentraat bij gemiddeld 5,0% (verkocht 181.494 dmt) ≈ **24 kt LCE/j** (197.967 × 5,0% × 2,473; verkocht ≈ 22 kt LCE) [1];
nominaal 184.511 t/j bij 5,82% Li2O [2]. De fysieke route is bronbevestigd tot "trein naar Port de Québec"; kade en sector niet.

## 1 · Ketenkaart
```
NAL-concentrator La Corne `li-nal-plant` ──(b1 truck · Route du Lithium → Route 111 zuidwaarts · hemelsbreed 33 km, geen wegkm;
  indicatie 61 km)──► Solurail-transload Val-d'Or `li-nal-valdor` (truck→spoor, Rue Roland-Massé)
  ──(b2 spoor · CN Val-d'Or–Senneterre–La Tuque–Hervey-Jonction–Shawinigan–Trois-Rivières–Québec · eigen netmeting 763 km,
  aannemelijk)──► Port de Québec, sector Beauport `li-nal-quebec-kade` (aannemelijk)
⏹ stoppunt (afnemer onbekend; geen zeebeen)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (spodumeenconcentraat) | `li-nal-plant` → `li-nal-valdor` | mijnweg → Route du Lithium (12,8 km) → Route 111 (La Corne → Val-d'Or) → Chemin Sullivan/Bd Tétrault (R117) → Rue Roland-Massé | **hemelsbreed 33 km, geen wegkm** — TRS noemt het terrein "60 km to the north of the city of Val-d'Or" [2]; OSRM 61,0 km (OSM-routering, geen bron) — ±15%-toets = indicatie | maak_stroombeen_weg (extract `canada`) | nee |
| b2 | B | spoor (spodumeenconcentraat) | `li-nal-valdor` → `li-nal-quebec-kade` | CN Abitibi-/La Tuque-lijn → Hervey-Jonction → Shawinigan/Trois-Rivières → noordoever naar Québec/Beauport | **763,1 km eigen netmeting** (toets_spoorroute, 637 edges; hemelsbreed 514 km, verhouding 1,48); geen gepubliceerde spoorkm — alleen "by train to Port of Québec" [2] | toets_spoorroute (`BAKE_SUFFIX=-raw`) | nee |

Geen zeebeen, geen fase D/E (zie §6). Totaal indicatief ~824 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-nal-plant` | mijn/concentrator (laadplek) | NAL-procescomplex, La Corne | 48.4059, -77.8305 | [2] eigendomscentrum 48.4067,-77.8306 (TRS: "Property centered near 48°24'24"N, 77°49'50"W"); gelegd op satelliet | **bron-gelegd** (z15 gezien: kruis op het procescomplex met grote hal en erts-/opslagterrein, direct naast de tailingsdam in het zuiden en de pit in het noorden; Route du Lithium sluit aan in het westen) |
| `li-nal-valdor` | overslag truck→spoor | Solurail-transload, Rue Roland-Massé, Val-d'Or | 48.1101, -77.7734 | [3] Solurail: 49 Rue Roland-Massé (trucking, transloading); [4] Nominatim way 175294648 (straatpunt) | **aannemelijk** (z16 gezien: grindterrein met opslag en bedrijfsloodsen, spoorbundel met wagons ~100 m oostwaarts en hoofdspoor ~150 m zuidelijk; spoorsnap 0,20 km; het gebouw zelf en de transload voor lithium zijn niet apart gebrond) |
| `li-nal-quebec-kade` | losplek/stoppunt | Port de Québec, sector Beauport (bulkterminal) | 46.8330, -71.1985 | [5] "FOB Port of Québec"; [6] eerste lading AAL Moon vertrok uit Québec; [4] Nominatim: Rue du Ressac, Port de Québec – Secteur Beauport | **aannemelijk** (z15/z16 gezien: droge-bulkterminal met erts-/bulkhopen, hallen en schepen langs de kade; spoorsnap 0,19 km; welke terminal/kade NAL gebruikt is niet gepubliceerd — kruis staat op het terrein, kadefront ~280 m zuidoostwaarts) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Route du Lithium × Route 111 (Chemin des Collines-aansluiting) | 48.4154, -78.0035 | de mijnweg gaat eerst 14 km west en slaat daar zuidwaarts af op Route 111; sluit een route via Barraute/Route 386 uit (ontwerp noemde "Barraute", dat ligt niet op de route) [7] |
| b1 | 2 | Route 111 bij La Corne (zuid) | 48.3427, -77.9958 | pint de doorgaande Route 111 ten zuiden van de afslag (OSRM-geometrie) [7] |
| b1 | 3 | Route 111 tussen Saint-Mathieu en Val-d'Or | 48.2882, -77.9950 | zelfde corridor, houdt het been op de tweebaans Route 111 [7] |
| b1 | 4 | Route 111 noord van Chemin Sullivan | 48.1871, -77.8606 | laatste punt vóór de kruising met Route 117 (Bd Tétrault, ring westzijde Val-d'Or, geen stadscentrum) [7] |
| b2 | 1 | Hervey-Jonction | 46.8530, -72.4701 | corridorkeuze: hier komt de La Tuque-lijn bij de lijn Shawinigan/Rivière-à-Pierre; de router blijft via Shawinigan/Trois-Rivières (snap 0,23 km); optioneel splitsen, totaal blijft 763,1 km [8] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| NAL-concentrator (La Corne) | Elevra Lithium (voorheen Sayona) | erts (~1,06% Li2O voeding) → spodumeenconcentraat ~5,0% | ontwerp 184.511 t/j (5,82% Li2O); FY26 productie 197.967 dmt ≈ 24 kt LCE; uitbreiding fase 1 gestart (2026) | [1][2][9] |

## 6 · Stoppunt
De brief stopt bij Port de Québec (Beauport): geen bron noemt de afnemer of het bestemmingsland van de FOB-lading, dus er is geen zeebeen en fase D/E vervalt.

## 7 · Open punten
- **Kade/terminal in Port de Québec niet gepubliceerd.** Alleen "Port of Québec" [2][5]; de eerste lading (AAL Moon, 1 aug 2023) vertrok uit Québec [6], maar geen bron noemt Beauport of Anse-au-Foulon. Beauport is aannemelijk (bulkterminal met spoor), niet bevestigd.
- **Transload-locatie Val-d'Or** alleen genoemd in de TRS 2025 [2]; Solurail (contract C$43 mln, okt 2022) noemde toen Trois-Rivières als haven [10] — de route/haven kan verschillen per jaar; actuele praktijk = FOB Québec [5].
- **Spoor 763 km is eigen netmeting**; router maakt twee keerpunten bij Shawinigan (46.5595,-72.7307 en 46.5514,-72.7401): de directe lijn Rivière-à-Pierre → Québec zit niet in het OSM-net, dus loopt de route via Trois-Rivières. Mogelijk een wye/keerlus, niet bevestigd.
- **Overlap**: ~551 km van b2 (Val-d'Or–Trois-Rivières) ligt binnen 2 km van `lithium-whabouchi-becancour` b3; uniek zijn mijn, truckbeen, Trois-Rivières→Québec en het eindpunt. Geen aparte kopie nodig.
- **Wegkm niet gepubliceerd**; de 61 km (OSRM) en "60 km" (TRS) zijn indicaties. Het ontwerp noemde "Route 111 Barraute–Val-d'Or"; de echte route loopt via de Route du Lithium en Route 111 bij La Corne.
- Sitelaag `lithium-sitelaag.json` heeft **geen NAL-site**; centraal toevoegen (anker `li-nal-plant`, nominaal 184,5 kt SC ≈ 26,6 kt LCE; FY26 24,5 kt LCE).

## 8 · Bronnen
[1] Elevra Lithium, Form 6-K (Quarterly Activities Report juni 2026, FY26 NAL-cijfers) — https://www.sec.gov/Archives/edgar/data/1739016/000114036126029882/ef20078904_6k.htm
[2] S-K 1300 Technical Report Summary NAL Project (2025) — https://www.sec.gov/Archives/edgar/data/1728205/000172820525000047/ex963s-k1300nalproject.htm
[3] Solurail Logistique (adres Val-d'Or, transloading, trucking) — https://www.solurail.com
[4] OpenStreetMap/Nominatim (ODbL): way 175294648 Rue Roland-Massé (48.11006,-77.77341); Rue du Ressac, Port de Québec – Secteur Beauport (46.8321,-71.1994); Barraute, Val-d'Or — https://nominatim.openstreetmap.org
[5] Elevra 6-K (zie [1]): realised price "FOB Port of Québec" — idem
[6] Sayona marks first shipment from NAL, Engineering News 2023-08-02 (en nasdaq/Piedmont persbericht 2023-08-01) — https://www.engineeringnews.co.za/article/sayona-marks-first-shipment-from-nal-2023-08-02
[7] OSRM (OSM-routering), Route du Lithium → Route 111 → Val-d'Or, 60,96 km — https://router.project-osrm.org ; Wikipedia, "Quebec Route 111" — https://en.wikipedia.org/wiki/Quebec_Route_111
[8] Eigen netmeting `toets_spoorroute.mjs` (BAKE_SUFFIX=-raw), 2026-10-09; Wikipedia/Nominatim Hervey-Jonction 46.853,-72.470
[9] Elevra Lithium start stage 1 NAL-uitbreiding (Mining Weekly 2026-06-30) — https://www.miningweekly.com/article/elevra-starts-stage-1-of-north-american-lithium-mine-expansion-2026-06-30
[10] Sayona secures rail link for NAL spodumene, Engineering News 2022-10-18 — https://www.engineeringnews.co.za/article/sayona-secures-rail-link-for-nal-spodumene-2022-10-18 ; Kallanish (api.kallanish.com, 'Sayona signs rail contract to transport Quebec spodumene to port') noemt Trois-Rivières als haven
[11] Satellietblikken (Esri, z15/z16): `v2/build-cache/satcheck/sat-lithium-nal-quebec-{plant,valdor,beauport,valdor-z16,beauport-z16}.png`

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Recept:** `bash v2/tools/bak_stromen.sh lithium-nal-quebec` (functie `bak_lithium_nal_quebec`) → `v2/data/stroomroute-lithium-nal-quebec.json`, 48,9 KB, contract versie 2, lonlat, modaliteiten {truck, spoor}, 3 markers, geen stippels, geen zeebeen, geen haven-aanloop, geen luchtbeen, geen leiding.

| # | modaliteit | km gemeten | brief | naad | geometrie |
|---|---|---|---|---|---|
| b1 | truck | **60,8** (wegnet 60,7) | hemelsbreed 33, geen wegkm; OSRM 61,0 / TRS 60 = indicatie (+-0,3% t.o.v. OSRM) | 0 | profiel `lithium-nal-quebec-plant-valdor`, `wegscan_puur.py` (extract canada, 6,4 GB, 449 s scan, venster 25 km), 5 via-punten |
| b2 | spoor | **768,3** (router 763,1 over 637 edges; lengte over de punten +0,7%) | geen gepubliceerde spoorkm; eigen netmeting 763,1 | 0,20 km (spoorsnap) | `BAKE_SUFFIX=-raw toets_spoorroute.mjs`, snap 0,20 en 0,19 km, ongewijzigd tegenover de run uit de brief |
Totaal 829,1 km. Markers: `li-nal-plant` (0,00 km van de lijn), `li-nal-valdor` (0,00), `li-nal-quebec-kade` (0,19 km, spoorsnap).

**Toelichting.**
- **b1:** profielsleutel `lithium-nal-quebec-plant-valdor`, refs 111 en 117, `gepubliceerdKm` None, `corridorKlassen` tertiary+unclassified. Segmenten 14,9 / 8,2 / 6,1 / 18,2 / 13,4 km, snaps <= 0,09 km, geen omweg; Route du Lithium (eerste 14,9 km over service/tertiary/unclassified) loopt eerst west en slaat zuid op Route 111 (Barraute ligt niet op de route). Laatste 0,78 km over service/unclassified naar de transload. Wegbron: pyosmium geblokkeerd, dus de pure-Python PBF-lezer; geen Overpass.
- **b2:** de twee keerpunten bij Shawinigan (46.5595,-72.7307 en 46.5514,-72.7401) staan ook in `toets_knikken` als TERUGLOOP; niet bijgeschoven (directe lijn Rivière-à-Pierre → Québec zit niet in OSM). Optioneel via-punt Hervey-Jonction niet gebruikt: de vrije route gaat al langs de brief-corridor, totaal ongewijzigd.
- **Gedeeld:** ~551 km van b2 overlapt `lithium-whabouchi-becancour` b3 maar met een andere kop; geen letterlijke kopie.
- **Bevindingen:** geen naad > 5 km; markers <= 0,19 km; toets_knikken geeft op b1 5 knikken (spikes bij via-punt en transload, plus de mijnweg-keerlus 159 graden bij het procescomplex: echte keerlus op het terrein), op b2 de 2 bekende Shawinigan-omkeringen. `toets_rechte_benen`: geen regel voor deze stroom (geen stippel, omwegfactor niet 1,000).
- **Open (zie §7):** Beauport-terminal niet gepubliceerd, Val-d'Or-transload alleen TRS 2025, geen NAL-site in `lithium-sitelaag.json` (centraal toevoegen).

**Lessen.** (1) De spoorgeojson uit de brief-fase was bruikbaar; herdraaien gaf identiek 763,1 km (seconden). (2) Een canada-wegscan met venster 25 km duurt ~8 min (103 s nodes + 449 s ways) en is daarna gecachet. (3) De door `hecht_marnet` herberekende spoorlengte wijkt +0,7% af van de routerkm (puntlengte versus edgesom).

