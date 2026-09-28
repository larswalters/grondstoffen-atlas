# Routebrief (licht) · olie — Ras Tanura (Saoedi-Arabië) → Ain Sokhna → Sidi Kerir (Egypte)

**stroom-id:** `olie-rastanura-sidikerir` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) · **status:** gebakken
**Keten in één zin:** Golf-crude die door zijn omvang (VLCC) het Suezkanaal niet volgeladen door kan en daarom via
Bab-el-Mandeb en de Rode Zee naar de **Ain Sokhna-terminal** vaart, daar deels wordt gelicht, en via de **SUMED-pijpleiding**
(twin 42", Arab Petroleum Pipelines Co.) over land naar de **Sidi Kerir-terminal** bij Alexandrië wordt gepompt —
de fysieke Suez-bypass, sinds de Rode Zee-omleiding van 2023/2026 op maximale capaciteit.
**Welke as van het verhaal:** *de Rode Zee/Suez-bypass.* SUMED draait sinds de Iraanse-conflict-escalatie van begin 2026
op zijn nameplate-maximum van **2,5 mln vpd** (was 1,0 mln vpd in februari 2026, +150%) — een directe graadmeter van hoeveel
Golf-crude de Straat van Hormuz mijdt via de Rode Zee in plaats van het Suezkanaal [1][2][3].

## 1 · Ketenkaart
```
Ras Tanura-exportterminal `ol-rastanura-term` (Perzische Golf, Saoedi-Arabië)
  ──(b1 zee · haven-aanloop + Perzische Golf → Hormuz → Arabische Zee → Bab-el-Mandeb → Rode Zee ·
      ~5.700 km, MARNET, aannemelijk: één bron)──►
   Ain Sokhna-terminal `ol-sokhna-term` (Golf van Suez, Egypte)
  ──(b2 leiding · SUMED-hoofdleiding via Dahshour-boosterstation · 320 km gepubliceerd)──►
   Sidi Kerir-terminal `ol-sidikerir-term` (Middellandse-Zeekust bij Alexandrië) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | zee | Ras Tanura-exportterminal → Ain Sokhna-terminal (aannemelijk: één bron) | Perzische Golf → Straat Hormuz → Arabische Zee → Bab-el-Mandeb → Rode Zee | ~5.700 [ontwerp-schatting; MARNET meet exact] | MARNET (kade → kade), haven-aanloop beide zijden (zie §9-aanwijzingen) | ja, alleen de haven-aanloop-stukken |
| b2 | B | leiding | Ain Sokhna-terminal → Sidi Kerir-terminal | SUMED-hoofdleiding (twin 42", via Dahshour-boosterstation) | 320 [sumed.org] · eigen OSM-meting 318,3 (6 waysegmenten + 1 gat) = **−0,5%** [6] | OSM-way (`sumed 1..5,7`, `man_made=pipeline`, `substance=oil`, egypte-extract) — grotendeels doorgetrokken, één stippel over een kaarteringsgat | gedeeltelijk — één stippel van 17,5 km tussen `sumed 5` en `sumed 7` (ontbrekende "sumed 6") |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-rastanura-term` | laadplek / exportterminal | Ras Tanura-exportterminal (Saudi Aramco) | 26.6540, 50.1648 | [8] | **bron-gelegd** — letterlijk hergebruikt van `olie-rastanura-zhoushan` §3 (z16 gezien: tankenpark + T-vormige steiger + Sea Island-fingerpier; niet opnieuw sat-gecheckt) |
| `ol-sokhna-term` | overslag zee → leiding (kop van de leiding) | Ain Sokhna-terminal (SUMED, Arab Petroleum Pipelines Co.) | 29.6002, 32.3227 | [3][4][6][7] | **bron-gelegd** (z15 gezien: langgerekt tankenpark van ~25 ronde opslagtanks in nette rijen direct naast de kustweg, met een pijpleidingtracé/servicepad dat noordwestwaarts het binnenland in loopt; ~700 m NO een tweede, los ogend tankencomplex — vermoedelijk een naburige olie-installatie, niet SUMED zelf) |
| `ol-sidikerir-term` | losplek / terminal (leiding → zee, reshipment); stoppunt | Sidi Kerir-terminal (SUMED), noord-Alexandrië | 31.0486, 29.6738 | [3][5][6][7] | **bron-gelegd** (z15 gezien: tankenpark direct aan het strand, ingeklemd tussen kustweg en de bebouwing van Alexandrië, met een korte havendam/pier de zee in aan de noordkant — matcht sumed.org's beschrijving van het Sidi Kerir-tankfarm met vijf SBM's voor de kust) |

## 4 · Via-punten (alleen b2 — de OSM-waysegmentgrenzen van de leiding)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | einde `sumed 1` / begin `sumed 2` | 29.7906, 31.3523 | eerste gekarteerde segmentgrens, corridor buigt bij nadering Dahshour [6] |
| b2 | 2 | einde `sumed 2` / begin `sumed 3` (Dahshour-zone) | 29.8382, 31.1640 | segmentgrens in de zone waar sumed.org de Dahshour-boosterstation-passage noemt [3][6] |
| b2 | 3 | einde `sumed 3` / begin `sumed 4` | 29.9962, 30.9603 | volgende gekarteerde segmentgrens [6] |
| b2 | 4 | einde `sumed 4` / begin `sumed 5` | 30.2005, 30.6737 | laatste segmentgrens vóór het kaarteringsgat [6] |
| b2 | 5 | einde `sumed 5` (vóór het gat) | 30.8462, 29.8727 | laatste gekarteerde punt van het trunk-tracé vóór de ~17,5 km-onderbreking [6] |
| b2 | 6 | hervatting `sumed 7` (na het gat, gereverseerd) | 30.9665, 29.7536 | eerste gekarteerde punt ná het gat, richting Sidi Kerir [6] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Dahshour-boosterstation | Arab Petroleum Pipelines Co. (SUMED) | drukverhoging op de doorgaande leiding (geen in-/uitsplitsing) | zes gasturbine-pompen van 26 MW elk | [3] |

## 6 · Stoppunt
De brief stopt bij de poort van de Sidi Kerir-terminal: dat is exact het ontwerp-eindpunt (SUMED-bestemming), en geen bron
koppelt de Ras Tanura-crude na Sidi Kerir aan één benoemde afnemer of fabriek — het bronmateriaal noemt alleen dat crude bij
Sidi Kerir op kleinere tankers wordt herladen richting "Europa en Amerika" (aggregaat-niveau, geen benoemde bestemming) [2].
Fase D/E vervallen.

## 7 · Open punten
- **Ras Tanura als specifieke herkomst blijft aannemelijk: één bron** — SUMED-doorvoer is een aggregaat van meerdere
  Golf-oorsprongen (Saoedi-Arabië, Irak, Koeweit); geen cargo-niveau bron koppelt specifiek Ras Tanura aan Ain Sokhna
  (zoals de haalbaarheidstoets al aangaf). Vandaar "(aannemelijk: één bron)" in de beennaam van b1.
- **17,5 km OSM-kaarteringsgat tussen `sumed 5` en `sumed 7`** ("sumed 6" ontbreekt in de egypte-extract) — niet
  onafhankelijk bevestigd als échte fysieke onderbreking, kan een kartering-omissie zijn; blijft daarom een stippel.
- **Sidi Kerir-zeeknoopafstand: eigen meting 18,76 km** (zeeknoop 3824, 31.2025/29.7545) — hoger dan de 10,8 km die de
  haalbaarheidstoets noemt (vermoedelijk een ander referentiepunt/afronding). Niet bakkritisch in déze brief (Sidi Kerir
  heeft hier geen eigen zee-leg, het is het stoppunt), maar relevant zodra Sidi Kerir ooit het vertrekpunt van een
  vervolgketen wordt.
- **`sumed 8.1`/`8.2`/`8.3`** (drie korte ways van 8-10 km bij Sidi Kerir, 31.05/29.6-29.67) niet meegenomen in b2 —
  lijken offshore SBM-aansluitleidingen/spuien van het terminal zelf, geen deel van de doorgaande trunk.
- **Volume is sterk oorlogs-/Rode Zee-crisisgedreven** — het huidige 2,5 mln vpd-niveau (was 1,0 mln vpd vóór
  februari 2026) kan bij een geopolitieke ommekeer weer zakken.
- **Twee haven-aanloop-stippels aan de b1-zijden** (Ras Tanura 11,1 km / Ain Sokhna 29,0 km tot hun zeeknoop, eigen
  meting) zijn conform de haalbaarheidstoets verplicht bij het bakken — zie de bak-aanwijzingen.

## 8 · Bronnen
[1] Wikipedia, "Sumed pipeline" — Ain Sokhna → offshore Sidi Kerir, Suez-alternatief. https://en.wikipedia.org/wiki/Sumed_pipeline
[2] Egypt Independent / Asharq Business, 02-04-2026 — "Egypt's SUMED oil flows jump 150% on Red Sea trade rerouting": 2,5 mln vpd max capaciteit (was 1,0 mln vpd vóór februari 2026), VLCC-lichtering bij Ain Sokhna, herladen bij Sidi Kerir. https://www.egyptindependent.com/egypts-sumed-oil-flows-jump-150-on-red-sea-trade-rerouting/
[3] SUMED (Arab Petroleum Pipelines Co.), "Our Facilities" — Ain Sukhna 3 SBM's + 24 tanks (2,9 mln m³), twin 42" pijpleiding 320 km via Dahshour-boosterstation (6× 26 MW), Sidi Kerir 28 tanks (3,1 mln m³) + 5 SBM's. https://www.sumed.org/?p=facilities
[4] OpenStreetMap/Nominatim (ODbL) — landuse "محطة نهائية لأنابيب سوميد" (SUMED-pijpleidingterminal), Ain Sokhna, way/92907652, 29.6002/32.3227. https://www.openstreetmap.org
[5] OpenStreetMap/Nominatim (ODbL) — landuse "Sidi Kerir tanker facility", way/93602398, 31.0486/29.6738. https://www.openstreetmap.org
[6] OpenStreetMap/Geofabrik egypte-extract (ODbL), eigen pyosmium-scan (2026-09-28) — 9 ways `man_made=pipeline` `substance=oil` genaamd "sumed 1"–"sumed 8.3" (ids 97801692/802304836/107701168/293024229/802304835/97808606/802491218-220); trunk `sumed 1..5,7` gestikt op eindpunt-nabijheid, som 300,7 km + gat 17,5 km = 318,3 km tegen gepubliceerd 320 km (−0,5%); Ain Sokhna-anker 0,77 km van `sumed 1`-start, Sidi Kerir-anker 0,87 km van `sumed 7`-eind. https://www.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `sat-olie-rastanura-sidikerir-sokhna-term.png`, `sat-olie-rastanura-sidikerir-sidikerir-term.png`.
[8] Routebrief `olie-rastanura-zhoushan.md` §3 — hergebruikt Ras Tanura-anker `ol-rastanura-term` (26.6540, 50.1648), zelf gebrond op Wikipedia + OSM + satelliet.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Stroom `olie-rastanura-sidikerir`** → `v2/data/stroomroute-olie-rastanura-sidikerir.json` — 6 benen, **6.139,1 km**,
903 punten, 3 markers (2 stippel-geojson + 1 stippel).
Recept: `bak_stromen.sh` (functie `bak_olie_rastanura_sidikerir`), `--max-snap 30` (zie ⚠️ hieronder).

**b1 (zee, MARNET-route, kade → kade, aannemelijk: één bron):** `--been "zee|VLCC Ras Tanura-exportterminal →
Ain Sokhna-terminal|26.6540,50.1648|29.6002,32.3227"`. **5.776,8 km**, 594 punten (lengte-invariant: getekende lijn
5.776,761 vs som edge-km 5.777,000 = −0,239 km, dat zijn de interne naden — geen bevinding). Tegen de
ontwerp-schatting ~5.700 km hemelsbreed/vaarafstand uit de brief = **+1,3%**, ruim binnen de indicatie (de brief
geeft zelf geen harde wegkm, dus de ±15%-toets is hier indicatief). Beide zijden lagen > 5 km van hun
MARNET-zeeknoop (LAR-586): twee haven-aanloop-stippels zijn ervoor gebouwd (zie hieronder), en het onderliggende
zeebeen snapt zelf óók nog op de zeeknoop — Ras Tanura 11,139 km (binnen de default 25 km), **Ain Sokhna 29,004 km
(boven de default 25 km)**. Daarom draait deze bake met **`--max-snap 30`**, met de reden in het kopcommentaar:
zonder die verhoging weigert de bake volledig ("SNAP TE VER... niets gebakken"), en 29,0 km is een gemeten,
verwachte snap (bak-aanwijzingen noemden hem vooraf), geen IJsselmeer-klasse toevalstreffer.

**Haven-aanloop Ras Tanura** (`maak_havenaanloop.py`, timeout 300, geslaagd): rechte lijn 11,14 km, pad over water
**11,8 km · 6 punten · 0% over land**, omwegfactor 1,055. `--stippel-geojson "zee|haven-aanloop Ras Tanura
(schematisch, over water — kade 11,1 km van de MARNET-zeeknoop)|…-aanloop-rastanura.geojson"`, vóór b1 in de
reisvolgorde (van de kade naar de zeeknoop, vertrek).

**Haven-aanloop Ain Sokhna** (`maak_havenaanloop.py`, timeout 300, geslaagd): rechte lijn 29,0 km, pad over water
**32,1 km · 53 punten · 1,21 km over land** (uitsluitend aan het kade-uiteinde — een kade ligt op de 1:10M-kustlijn
per definitie óp land, dat is de korrel van het tool, geen landkruising MÍDDEN op de lijn: 0,00 km), omwegfactor
1,108. Het tool is aangeroepen als kade→zeeknoop (net als Ras Tanura) en de resulterende geojson is daarna
**programmatisch omgekeerd** (zeeknoop→kade) zodat de reisvolgorde bij aankomst klopt. `--stippel-geojson
"zee|haven-aanloop Ain Sokhna (schematisch, over water — kade 29,0 km van de MARNET-zeeknoop)|…-aanloop-sokhna.geojson"`,
ná b1.

**b2 (leiding, SUMED-hoofdleiding, via Dahshour-boosterstation):** nieuw gereedschap
`v2/tools/maak_leidingbeen_olie_sumed.py` — één pyosmium-pass op `v2/build-cache/geofabrik/egypte-latest.osm.pbf`
haalt de zes benoemde ways letterlijk op (`man_made=pipeline substance=oil`, ids 97801692/802304836/107701168/
293024229/802304835 = "sumed 1".."sumed 5", en 97808606 = "sumed 7"; "sumed 6" ontbreekt in deze extract — het
kaarteringsgat uit de brief). Gemeten lengtes: sumed 1 99,80 km · sumed 2 20,96 km · sumed 3 26,63 km · sumed 4
35,73 km · sumed 5 105,84 km · sumed 7 11,76 km.
- **Segment 1** = sumed 1+2+3+4+5, gestikt in reisvolgorde op exacte OSM-nodecoördinaten (aansluiting tussen elk
  paar ways ≤ 1 km, geen enkele waarschuwing) → **289,0 km · 210 punten**, kop 29,60699/32,32140 (0,765 km van het
  Ain Sokhna-anker) tot eind 30,84618/29,87265.
- **Stippel** over het kaarteringsgat: 30,8462,29,8727 → 30,9665,29,7536, **17,6 km** (niet onafhankelijk bevestigd
  als échte fysieke onderbreking — kan een OSM-karteringsomissie zijn, brief §7).
- **Segment 2** = sumed 7, **IN OMGEKEERDE RICHTING** (deze way loopt in OSM van Sidi Kerir terug naar het gat) →
  **11,8 km · 38 punten**, kop 30,96645/29,75364 tot eind 31,05101/29,68250 (0,871 km van het Sidi Kerir-anker).
- sumed 8.1/8.2/8.3 (offshore-aansluitleidingen bij Sidi Kerir) bewust **niet** meegenomen (brief §7).
- **Totaal leiding: 289,0 + 17,6 + 11,8 = 318,3 km** tegen gepubliceerd **320 km** (sumed.org, [3]) = **−0,5%**,
  ruim binnen ±15%. Bevestigt de brief's eigen OSM-meting (318,3 km) exact.

**Naden** (`hecht_marnet route` + eigen script): alle zes benen ≤ 0,77 km — b1-aanloop→b1 0,000 km · b1→b1-aanloop
0,000 km · aanloop-Sokhna→leiding-segment1 **0,765 km** (= "Ain Sokhna-anker 0,77 km van sumed1-start" uit de
brief) · segment1→gat-stippel 0,005 km · gat-stippel→segment2 0,007 km. **Geen naad > 5 km.**

**Markers:** Ras Tanura (0,0 m van de lijn) · Ain Sokhna (0,0 m) · Sidi Kerir (**871 m** — anker ≠ routeerpunt,
exact de 0,87 km die de brief zelf al noemt voor het gereverseerde sumed-7-eindpunt; geen extra last-mile-stippel
nodig, conform de bak-aanwijzingen).

**Toets:** `toets_knikken.py` — 4 knikken ≥60° (twee op het zeebeen bij 26,805/50,243 en 22,700/60,400, twee
"spike"-punten van 78,1°/71,7° op de leiding-geometrie bij ~29,807/31,259, R 56-60 m — echte OSM-pijpleidinggeometrie,
geen routeerartefact), **0 omkeringen ≥150°, 0 terugloop** — geen bevinding. `toets_rechte_benen.py --min-km 5` —
alleen de bewuste 17,6 km-gapstippel (omwegfactor 1,003) staat op de lijst: correct, dat is een rechte stippellijn
per constructie, geen bevinding op zichzelf. json geldig: versie 2, punt_formaat lonlat, modaliteiten `zee`/`leiding`
(toegestane set), elk been ≥2 punten (min. 2, max. 594), bestandsgrootte **17,7 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- `--max-snap` in `hecht_marnet.py route` is een GLOBALE vlag voor de hele bake, niet per been — een snap boven
  de default (25 km) op één enkel been-uiteinde dwingt de vlag voor de hele stroom, en de reden hoort dan in het
  kopcommentaar te staan (waarom dít geen IJsselmeer-klasse is): hier omdat de bak-aanwijzingen de 29 km-snap al
  vooraf voorspelden op basis van een eigen meting, niet een verdwaalde coördinaat.
- Een `maak_havenaanloop.py`-aanroep met `--van <kade> --naar <zeeknoop>` schrijft de geojson-coördinaten LETTERLIJK
  in die volgorde (kade→zeeknoop); voor een AANKOMENDE haven-aanloop (zeeknoop→kade, aan het einde van een zeebeen)
  moet die volgorde na het schrijven programmatisch omgekeerd worden — `hecht_marnet.py` leest `--stippel-geojson`
  puur letterlijk en routeert niet, dus een verkeerde richting geeft een stille, foute reisvolgorde in plaats van
  een fout.
- Eén pyosmium-pass (`osmium.FileProcessor` met `.with_locations()`) op een lijst bekende way-ids is genoeg om een
  brief die de exacte OSM-ids al heeft uitgezocht letterlijk te bakken — geen component-graaf/Dijkstra nodig zoals
  bij een brief die alleen namen/coördinaten geeft (vergelijk `maak_leidingbeen_gas_hassirmel_arzew.py`).
