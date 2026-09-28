# Routebrief (licht) · Grafiet · Van → Via → Naar (land)

**stroom-id:** `grafiet-molo-duisburg` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** Madagaskar SuperFlake-vlokgrafiet van de NextSource Molo-mijn (Zuid-Madagaskar) per
**truck** naar de Toliara-kade, per **zeeschip** (haven-aanloop + MARNET, Mozambiquekanaal/Kaap of
Malakka/Suez) naar Rotterdam RHB, per **binnenvaart** de Rijn op naar Duisburg-Ruhrort Becken A — de
niet-Chinese afnemer-as met thyssenkrupp Materials Trading (Duitsland) als contractuele afnemer.
**Welke as van het verhaal:** enige gemeten grafietketen naar een Europese handelspartij buiten China;
17 kt vlokconcentraat/j nameplate, feitelijk sinds mei 2025 "campaign production" op ~11 kt/j (NextSource
Q3-update 2025 [3]); thyssenkrupp-offtake contractueel tot 35 kt/j (2021, 10 jaar) [5][6].

## 1 · Ketenkaart
```
Molo-mijn `gr-molo-mijn` ──(b1 truck · via Fotadrevo/Ampanihy → RN10 → Andranovory → RN7 ·
hemelsbreed ~165 km, geen wegkm)──► Toliara-kade `gr-toliara-kade`
  ──(b2 zee · haven-aanloop, stippel, ~111,16 km, kade ligt >25 km van de MARNET-zeeknoop)──►
  zeeknoop 5303 (-22,85720, 42,73680)
  ──(b3 zee · MARNET, Mozambiquekanaal/Kaap óf Malakka/Suez — router kiest · orde duizenden km,
  niet vooraf geschat)──► Rotterdam RHB `gr-rotterdam-rhb` (hergebruikt anker)
  ──(b4-b6 binnenvaart · Rijn, letterlijke kopie van `koper-lobito-duisburg` benen 5-7 · 235,0 km)──►
  Duisburg-Ruhrort Becken A `gr-duisburg-beckena` (hergebruikt anker) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-molo-mijn` → `gr-toliara-kade` | regionale weg Fotadrevo → Ampanihy (RN10-aansluiting) → Betioky Atsimo → Andranovory (RN10/RN7-kruispunt) → Toliara | hemelsbreed ~165 km, geen gepubliceerde wegkm [7] | maak_stroombeen_weg (extract `madagaskar`) | nee, tenzij het net hier niet aaneengesloten blijkt |
| b2 | A/B | zee | `gr-toliara-kade` → zeeknoop 5303 (-22,85720, 42,73680) | haven-aanloop — MARNET reikt hier niet (>25 km) | ~111,16 [haalbaarheidstoets 2026-09-26, `hecht_marnet.marnet_zee`] | `maak_havenaanloop.py` (timeout 300); terugval: rechte stippel | ja — haven-aanloop, "hier reikt het net niet" |
| b3 | B | zee (MARNET) | zeeknoop 5303 → `gr-rotterdam-rhb` | Mozambiquekanaal/Kaap óf Malakka/Suez — MARNET kiest | orde duizenden km, niet vooraf geschat | `--been "zee|…|-22.8572,42.7368|51.8935,4.4585"` | nee |
| b4 | C | binnenvaart | `gr-rotterdam-rhb` → Emmerich-vak (51,754, 6,366) | Rijn — letterlijke kopie `koper-lobito-duisburg` been 5 (AIS-graaf) | 161,1 [13] | `--been` (AIS-graaf `rijn`) | nee |
| b5 | C | binnenvaart | Emmerich-vak → Wesel-vak (51,39985, 6,74535) | Rijn — letterlijke kopie been 6, geen AIS-dekking, echte OSM-loop | 66,6 [13] | `--been-geojson` (`rivierbeen-wesel.geojson`, hergebruikt bestand) | nee |
| b6 | C | binnenvaart | Wesel-vak → `gr-duisburg-beckena` | Rijn — letterlijke kopie been 7 (AIS-graaf) | 7,3 [13] | `--been` (AIS-graaf `rijn`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-molo-mijn` | mijn (kop) | NextSource Molo-mijn (SuperFlake-vlokgrafiet), Fotadrevo/Ampanihy, Zuid-Madagaskar — hergebruikt sitelaag-anker `w-nextsource-molo` | -24,0045, 45,1244 | [1][2][3][12], sitelaag `v2/design/grafiet-sitelaag.json` | bron-gelegd (z14 gezien, sitelaag-satellietblik hergebruikt: kruis op/vlak bij kleine gebouwen in droog savannegebied; OSM bevestigt deze ronde onafhankelijk landuse=quarry "Molo Graphite Mine" op -24,00675/45,12447, ~250 m van het sitelaag-punt [7]) |
| `gr-toliara-kade` | overslag (zeekade) | Port de Tuléar, Toliara, Zuid-Madagaskar | -23,3778, 43,6648 | [1][2][7] OSM way/119493486 (landuse=harbour) | bron-gelegd (z15 gezien, `sat-grafiet-molo-duisburg-toliara-kade.png`: smalle pier met een T-vormige aanlegsteiger die ver de baai in steekt, met een klein platform/gebouwtje aan het uiteinde — geen zichtbare kranen/bulkband op deze zoom, dus alleen de aanwezigheid van een kade bevestigd, niet de overslagcapaciteit) |
| `gr-rotterdam-rhb` | overslag (binnenvaart-entrepot) | RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4, Rotterdam — hergebruikt canoniek anker uit `routebrief-licht.md` §1 | 51,8935, 4,4585 | [13], eerder satelliet-gelegd (`koper-lobito-duisburg`) | bron-gelegd (letterlijk hergebruikt, dit onderzoeksbudget niet opnieuw gecheckt) |
| `gr-duisburg-beckena` | losplek (entrepot/stoppunt) | Duisburg-Ruhrort, Becken A — hergebruikt canoniek anker uit `routebrief-licht.md` §1 | 51,4518, 6,7565 | [13], eerder satelliet-gelegd (`koper-lobito-duisburg`) | bron-gelegd (letterlijk hergebruikt, dit onderzoeksbudget niet opnieuw gecheckt) |

## 4 · Via-punten (alleen b1 — corridorkeuze rond de RN10/RN7-aansluiting)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ampanihy (RN10-aansluiting vanaf de regionale weg Fotadrevo) | -24,6927, 44,7464 | hier komt de regionale weg vanaf de mijn/Fotadrevo op de RN10 — RN10 loopt hier al gekarteerd, bevestigd door Wikipedia als "gekruist door Ampanihy" [8] |
| b1 | 2 | Betioky Atsimo (RN10-waypoint) | -23,6897, 44,4212 | doorgaande RN10 tussen Ampanihy en het RN7-kruispunt bij Andranovory, geen zijtak |
| b1 | 3 | Andranovory (RN10 → RN7-kruispunt) | -23,5420, 44,8053 | RN10 eindigt hier op de RN7, die westwaarts naar Toliara loopt [8][9] — de enige corridorkeuze richting de kade |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Molo-mijn (vlotatie/wascircuit) | NextSource Materials Inc. | grafieterts → SuperFlake-vlokconcentraat (94-97% C) | nameplate 17 kt/j; feitelijk ~11 kt/j door maal-/vlotatiebeperkingen, sinds mei 2025 "campaign production" (kapitaalbehoud richting Fase 2) | [1][2][3] |

## 6 · Stoppunt
De brief stopt bij Duisburg-Ruhrort Becken A (entrepot): thyssenkrupp Materials Trading is een
bevestigde, contractuele afnemer (offtake 2021, 10 jaar, tot 35 kt/j) [5][6], maar geen bron noemt het
exacte vestigingsadres of de kade in Duisburg — een eigen fase-D-anker zou een coördinaat verzinnen.
Zelfde patroon als `koper-lobito-duisburg`: de brief eindigt bij het entrepot als het fase-D-vertrek
onzeker blijft.

## 7 · Open punten
- **thyssenkrupp Materials Trading — exacte Duisburg-vestiging/kade niet gevonden** dit onderzoeksbudget
  (geen adres of terreinnaam in de drie startbronnen of het OSM-naamzoeken); fase D vervalt daarom.
- **Toliara-kade toont geen bulk-overslaginfrastructuur op de z15-satellietblik** — alleen een pier/
  aanlegsteiger; welke exacte ligplaats de containerlading van NextSource gebruikt is niet bevestigd.
- **Fase A (Molo-mijn → Toliara) nog niet met `maak_stroombeen_weg.py` doorgerekend** — alleen een
  hemelsbrede schatting (~165 km); de corridor maakt via Ampanihy een zuidelijke omweg vóór hij weer
  noordwaarts naar Toliara buigt, dus de werkelijke wegkm ligt vermoedelijk ruim boven 165 km — de
  ±15%-toets geldt hier dus niet als norm.
- **Haven-aanloop Toliara (~111 km) is het grootste precedent tot nu toe** (groter dan Fujairah 10,5 /
  Ras Tanura 11,1 / Aktau 7,4 km uit golf 1, en groter dan Skaland-Noorwegen 27,3 km) — de
  haalbaarheidstoets kreeg binnen >7 min geen uitvoer van `maak_havenaanloop.py`; bakken met `timeout 300`
  en bij het uitblijven van een pad de rechte stippel als eindvorm.
- **Molo Fase 1 draait sinds mei 2025 op "campaign production"** (NextSource zelf: kapitaalbehoud,
  prioriteit naar Fase 2) [3] — de aanvoer is waarschijnlijk intermitterend, ook al is het
  thyssenkrupp-contract bindend en langlopend.
- **Een niet bij naam genoemde Japanse technische partner** (uit de persberichten 2024-2025) is bewust
  niet getekend — geen tonnage/bestemming per afnemer gepubliceerd; deze brief volgt alleen de
  thyssenkrupp-as.
- **WEBBUDGET:** 2 van 3 WebSearch-aanroepen gebruikt (offtake-condities + campaign-productiestatus);
  verder alleen Nominatim + curl op de drie startbronnen.

## 8 · Bronnen
[1] MINING.COM, "NextSource ships first Madagascar graphite to global markets", 2024-10-24 — export via Port of Tulear naar Duitsland/VS, 17.000 tpa capaciteit. https://www.mining.com/nextsource-ships-first-madagascar-graphite-to-global-markets/
[2] NextSource Materials / ACCESS Newswire, "Molo Mine Update; Begins Transporting SuperFlake Graphite Concentrate to Port for Export", 2024-08-07 — transport Molo-mijn → Port of Tulear. https://www.accessnewswire.com/newsroom/en/metals-and-mining/nextsource-materials-provides-molo-mine-update-begins-transporting-superflaker-gra-897247
[3] NextSource Materials / ACCESS Newswire, "Quarterly Update … Molo Mine Expansion Study", 2025-05-15 — "campaign production", plantcapaciteit c. 11.000 tpa, eerste commerciële zendingen okt. 2024 naar Duitsland/VS, aankomst jan. 2025, ~2.500 t voorraad. https://www.accessnewswire.com/newsroom/en/metals-and-mining/nextsource-materials-provides-quarterly-update-and-announces-progress-on-molo-min-1028248
[4] Mining Magazine, "NextSource secures offtake agreement with thyssenkrupp". https://miningmagazine.com/processing/news-articles/1410909/nextsource-secures-offtake-agreement-thyssenkrupp
[5] Mining Weekly, "Thyssenkrupp Materials Trading, NextSource sign offtake agreement", 2021-05-25 — 10 jaar, tot 35.000 t/j, Fase 1 min. 7.300 t/j. https://www.miningweekly.com/article/thyssenkrupp-materials-trading-nextsource-sign-offtake-agreement-2021-05-25/rep_id:3650
[6] NextSource Materials, persbericht offtake thyssenkrupp Materials Trading. https://www.nextsourcematerials.com/nextsource-materials-secures-offtake-agreement-with-thyssenkrupp-materials-trading/
[7] OpenStreetMap/Nominatim (ODbL) — Molo Graphite Mine (landuse=quarry, -24,00675/45,12447); Port de Tuléar (landuse=harbour, way/119493486, -23,3778126/43,6647555); Fotadrevo, Ampanihy, Betioky Atsimo, Andranovory (place-nodes). https://www.openstreetmap.org
[8] Wikipedia (EN), "Route nationale 10 (Madagascar)" — 512 km onverharde secundaire weg, Andranovory → Ambovombe, kruist Ampanihy. https://en.wikipedia.org/wiki/Route_nationale_10_(Madagascar)
[9] Wikipedia (EN), "Toliara" — havenstad Zuid-Madagaskar, hoofdstad Atsimo-Andrefana, import/export-knooppunt. https://en.wikipedia.org/wiki/Toliara
[10] Wikipedia (EN), "Ampanihy" — dorp/gemeente, gekruist door RN10. https://en.wikipedia.org/wiki/Ampanihy
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-grafiet-molo-duisburg-toliara-kade.png`.
[12] v2/design/grafiet-sitelaag.json — anker `w-nextsource-molo` (hergebruikt, bron-gelegd).
[13] v2/design/routebrieven/koper-lobito-duisburg.md + `v2/tools/bak_stromen.sh` (functie `bak_koper_lobito`, benen 5-7) — Rijn-geometrie Waalhaven → Emmerich-vak (161,1 km, AIS-graaf) → Wesel-vak (66,6 km, `rivierbeen-wesel.geojson`) → Duisburg Becken A (7,3 km, AIS-graaf), 235,0 km totaal, letterlijk gekopieerd; ook bron voor de canonieke Rotterdam RHB- en Duisburg Becken A-ankers.
[14] Haalbaarheidstoets `grafiet-molo-duisburg`, 2026-09-26 — zeeknoop 5303 (-22,85720/42,73680), 111,16 km van de Toliara-kade (`hecht_marnet.marnet_zee`).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Stroom `grafiet-molo-duisburg`** → `v2/data/stroomroute-grafiet-molo-duisburg.json` — 6 benen,
**14.373,9 km**, 4 markers: truck 378,5 km · zee 111,2 (stippel) + 13.649,2 km · binnenvaart 161,1 + 66,6 +
7,3 km. Bestand 128,1 KB. Recept: `bak_stromen.sh` (functie `bak_grafiet_molo_duisburg`), profiel
`grafiet-molo-duisburg-molo-toliara` in `maak_stroombeen_weg.py`.

Toelichting per leg:
- **b1 (truck, doorgetrokken):** `maak_stroombeen_weg.py --profiel grafiet-molo-duisburg-molo-toliara`
  (extract `madagaskar`, venster 75 km). Eerste poging (WEG_HOUD kaal, t/m `secondary`) gaf **"corridor niet
  gerouteerd: punt (44.8053, -23.542) ligt >25 km van elke weg"** — RN10 is in Wikipedia zelf een "onverharde
  secundaire weg" en draagt in OSM geen `highway=secondary`-tag. `corridorKlassen`
  tertiary/unclassified/residential/service toegevoegd (+ `eindKlassen` voor de uiteinden) → doorgaand pad
  gevonden. Ruwe lijn 516,8 km, na het snoeien van **6 keerlussen** (dubbel gereden stukken, o.a. 129,6 km bij
  Andranovory en 8,8 km bij Betioky Atsimo) → **378,5 km gebakken**. Tegen hemelsbreed ~165 km uit de brief
  is dat **+129%** — GEEN norm-overschrijding: de brief zegt zelf al dat de brief geen gepubliceerde wegkm
  heeft en dat de werkelijke wegkm door de zuidelijke omweg over Ampanihy "ruim boven 165 km" ligt, en dat de
  ±15%-toets hier niet als norm geldt (brief §2/§7). Via-snaps: Ampanihy 0,01–0,08 km · Betioky Atsimo 2,68 km
  (binnen de norm, geen wegklasse-correctie nodig) · Andranovory 0,01 km.
- **b2 (zee, stippel):** `timeout 300 python v2/tools/maak_havenaanloop.py` vond bij trap "cel 0,005° kaal"
  al een pad met **0% over land** (93 punten, 118,6 km) maar werd door de timeout afgekapt vóór het bestand
  geschreven was (exit 124, geen geojson op schijf) — exact het beeld uit de haalbaarheidstoets ("binnen
  >7 min geen uitvoer"). Conform bakhandleiding §2: geen tweede poging, rechte stippel
  (111,165 km, brief noemt 111,16 km — komt overeen). Zeeknoop 5303 (-22,8572/42,7368) is bindend uit de
  haalbaarheidstoets en niet herrekend.
- **b3 (zee, MARNET, doorgetrokken):** kade → kade, router snapt 0,000 km op Toliara en 0,107 km op
  Waalhaven; **13.649,2 km** (orde duizenden km, niet vooraf geschat — brief §2). MARNET koos zelf de route
  om Afrika (Kaap), niet Suez.
- **b4-b6 (binnenvaart, doorgetrokken, LETTERLIJKE KOPIE):** exact de drie Rijn-benen uit `bak_koper_lobito`
  hierboven (zelfde `GRAAF_RIJN`, zelfde `rivierbeen-wesel.geojson`, geen eigen versie gebakken) —
  Waalhaven → Emmerich-vak **161,1 km** (AIS-graaf) · Emmerich-vak → Wesel-vak **66,6 km**
  (`rivierbeen-wesel.geojson`, geen AIS-dekking) · Wesel-vak → Duisport Ruhrort **7,3 km** (AIS-graaf).
  Rijn-segment totaal **235,0 km** — komt exact overeen met de brief (§2, been b4/b5/b6).
- Alle 4 markers uit §3 zijn meegenomen; geen fase D/E (thyssenkrupp Materials Trading heeft geen gevonden
  vestigingscoördinaat — brief §6/§7, brief en bake stoppen bij Duisburg-Ruhrort Becken A).

**Toets-bevindingen (bakhandleiding §5):**
- **Naden tussen alle 6 benen ≤ 0,0654 km** — ruim binnen de ≤5 km-norm (grootste naad tussen b4↔b5, bij
  Emmerich-vak).
- **`toets_knikken.py`: 56 knikken ≥60°, 4 omkeringen (≥150°), 0 TERUGLOOP** (de enige categorie die
  reparatie zou vragen) — rc=0. De 36 spikes op b1 zijn OSM-zigzag op kleine wegklassen (klein
  boogstraal, geen echte knik); de vier omkeringen op de binnenvaartbenen (Wesel-vak-uiteinden, Duisport
  Ruhrort-uiteinde) staan gemarkeerd als "scherpe/krappe bocht, echt" — dezelfde geometrie als in
  `koper-lobito-duisburg` (letterlijke kopie), niet iets dat deze bake heeft geïntroduceerd.
- **`toets_rechte_benen.py --min-km 5`:** alleen b2 (de haven-aanloop-stippel, 111,2 km, omwegfactor 1,000)
  staat in de wereldwijde verdachtenlijst — verwacht en correct: een rechte stippel met reden is precies de
  norm (bakhandleiding §2/§6).
- **Marker-afstand tot de lijn:** Molo-mijn 0,0 m (anker = beginpunt) · Toliara-kade 0,0 m (anker =
  overslagpunt) · Rotterdam 107 m (binnen de ~0,5 km-norm) · Duisburg 2.153 m (**anker ≠ routeerpunt** — de
  eindsnap van de laatste binnenvaartleg "51.4,6.745 → 51.4518,6.7565" komt letterlijk uit
  `bak_koper_lobito`, dus deze afwijking is géén nieuw artefact van deze bake maar een eigenschap van het
  gedeelde been dat hier bewust ongewijzigd is overgenomen).
- **JSON-vormtoets:** `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, zee, binnenvaart} (alle
  toegestaan), elk been ≥2 punten, bestand 128,1 KB (< 300 KB) — allemaal in orde.

**Open bevinding buiten deze bake (gemeld, niet aangeraakt — "JE RAAKT ALLEEN JE EIGEN BESTANDEN"):**
het bestaande `v2/data/stroomroute-koper-lobito-duisburg.json` op schijf komt bij de laatste
binnenvaartleg niet overeen met de huidige tekst van `bak_koper_lobito()` (json toont een leg van 0,624 km
tussen 6,25845/51,82385 en 6,2624/51,8289; de functie specificeert "binnenvaart|…Wesel-vak →
Duisport Ruhrort|51.4,6.745|51.4518,6.7565"). Voor déze bake maakt dat niets uit — de literal copy is
gebaseerd op de FUNCTIETEKST, niet op het json-bestand, en de zelfstandig gebakken uitkomst (161,1/66,6/7,3
km) klopt exact met de brief — maar het is een signaal dat `koper-lobito-duisburg.json` mogelijk stale is
ten opzichte van zijn eigen recept.
