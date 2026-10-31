# Routebrief (licht) · PGM — Tharisa Mine → R104 → Waterval/PMR (Zuid-Afrika)

**stroom-id:** `pgm-tharisa-waterval` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) ·
**status:** gebakken
**Keten in één zin:** PGM-concentraat (derde partij, bijproduct van chroom) van de Tharisa Mine bij Marikana/Mooinooi per **truck** over Marikana Road (D1325), Karee Road (D108) en de onbenoemde tertiary-corridor westwaarts (R104-richting, niet de N4) naar het Waterval-/PMR-complex van Valterra Platinum (Rustenburg Platinum Mines), Rustenburg; stoppunt = smelter/raffinaderij. **Aannemelijk: één bron** (koper en ingangsdatum zijn bron-gelegd, het leveringspunt Waterval is aanname).
**Welke as van het verhaal:** de Westelijke-Bushveld-concentraatruil: vanaf 1-1-2027 gaat 50% van het Tharisa-PGM-concentraat van Sibanye-Stillwater naar Valterra (Northam houdt de andere 50%) — derde-partij-concentraat dat Valterra's eigen smelterpark voedt. Volume: 153,7 koz 6E FY2026 = 4,78 t 6E/j; de helft = **~2,4 t 6E/j** [1][2].

## 1 · Ketenkaart
```
Tharisa Mine (plant) `pgm-tharisa-plant` ──(b1 truck · Marikana Rd D1325 → Karee Rd D108 → R104-corridor west ·
   hemelsbreed 18,3 km, geen wegkm; OSRM-indicatie 24,2 km · aannemelijk: één bron)──►
Waterval-/PMR-complex Valterra `pgm-rustenburg-pmr` ── stoppunt (smelter/raffinage)
```
Niet getekend: de andere 50% naar Northam (Zondereinde; eigen keten `pgm-zondereinde-*`), en Karo-concentraat (Zimbabwe, vanaf eind 2027, andere keten).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-tharisa-plant` → `pgm-rustenburg-pmr` | Marikana Road D1325 → Karee Road D108 → onbenoemde tertiary west (R104-corridor); NIET de N4 | hemelsbreed 18,3 km, geen wegkm; OSRM-indicatie 24,2 km [9] (geen norm) | maak_stroombeen_weg | nee |

Geen zee-, spoor-, lucht- of leidingbeen; geen haven-aanloop. Naam van het been bevat "(aannemelijk: één bron)". Geen fase D/E: de bron noemt alleen de koper.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-tharisa-plant` | mijn + verwerkingsplant / vertrek | Tharisa Mine Processing Plants, Mooinooi/Marikana (Tharisa Minerals) | -25.7421, 27.4978 | [1][2][8] | bron-gelegd (z15 gezien: plantcomplex met procesgebouwen, bekkens en blauwgroene tailings/bezinkvijvers op het kruis, dagbouwpit direct noordelijk, N4 ~1 km zuidelijk) |
| `pgm-rustenburg-pmr` | losplek / smelter + raffinage, stoppunt | Waterval-/PMR-complex, Valterra Platinum (Rustenburg Platinum Mines) — **hergebruikt letterlijk** uit `pgm-zimplats-rustenburg.md` en `pgm-unki-rustenburg.md` | -25.6838, 27.3272 | [5][6] | bron-gelegd (z15 opnieuw gezien: industrieel procescomplex met hoge gebouwen, tanks en bezinkbekkens op het kruis; smelterstrook met schoorstenen en slakveld ligt ~1,3 km NW) |

Het leveringspunt binnen het complex (smelterstrook `-25.6750, 27.3180` of PMR-deel) noemt geen bron; site-niveau, geen tweede anker.

## 4 · Via-punten (in reisvolgorde, alle op de doorgaande weg, niet in een stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kruising Marikana Road D1325 / Karee Road D108 | -25.6971, 27.4888 | pint de noordelijke uitgang van de plant; sluit de N4-variant (75-88% overlap met bestaande lijnen) uit |
| b1 | 2 | R104-corridor, onbenoemde tertiary | -25.6887, 27.4551 | bindend uit de toets; houdt de lijn op de tertiary i.p.v. een zijtak (OSRM-snap 35 m) |
| b1 | 3 | R104-corridor, onbenoemde tertiary | -25.6803, 27.3860 | bindend uit de toets; pint de westelijke doorgaande weg (OSRM-snap 38 m) |
| b1 | 4 | Afslag naar het Waterval-complex | -25.6739, 27.3333 | pint de aanloop vanuit het noordoosten i.p.v. via Rustenburg-centrum (OSRM-snap 2 m) |

Geofabrik-regio's: `zuid-afrika`. OSRM met deze vier via-punten: 24,2 km, identiek aan de vrije route [9].

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tharisa Mine (concentrator, chroom + PGM) | Tharisa plc | reef (5,5 Mt gemalen FY2026) → PGM-concentraat (+ chroomconcentraat 1,56 Mt) | 153,7 koz 6E/j FY2026; guidance FY2027 150-170 koz | [2] |
| Waterval smelter / PMR | Valterra Platinum | derde-partij-concentraat (o.a. Tharisa, vanaf 2027) → matte → Pt/Pd/Rh | capaciteit niet gevonden | [1][5][10] |

## 6 · Stoppunt
De brief stopt bij het Waterval-/PMR-complex: dat is de bij naam gecontracteerde afnemer (Rustenburg Platinum Mines) en de bestaande Valterra-verwerking; geen bron noemt een vervolgbestemming van deze lading, en een leveringspunt noemt geen bron.

## 7 · Open punten
- **Leveringspunt onbevestigd:** SENS en Mining-technology noemen koper en ingangsdatum, geen leveringsplaats [1][3]. Waterval is aanname (derde-partij-voeding van de Waterval-smelter volgens een zoekresultaat-snippet van Polity [10], volledig artikel niet gelezen: HTTP 403). Alternatief zou Polokwane zijn (verwerkt vooral Mogalakwena-concentraat) — niet onderzocht.
- **Ingang 1-1-2027:** de keten loopt tot dan via Sibanye (Marikana-smelter); deze lijn is toekomstig, bindend maar nog niet gelopen.
- **Wegkm onbekend:** geen bron voor een echte wegkilometer; 24,2 km is alleen een OSRM-indicatie, de ±15%-toets is een indicatie. De 14 km onbenoemde tertiary heeft in OSRM geen ref; "R104" komt uit het ketenontwerp en is niet in OSM gezien.
- **Overlap bewaakt:** de N4-variant liggt 75-88% op de lijnen van `pgm-zondereinde-hanau` b1 (golf 16 wees `tharisa-zondereinde` daarom af); de gekozen R104-corridor overlapt 2% [toets].
- **Sitelaag `w-tharisa`** (-25.63, 27.63, aannemelijk) ligt 18,2 km ONO van de plant; hier niet aangepast (sitelagen zijn niet van deze brief), centraal gelijktrekken naar `pgm-tharisa-plant`.
- **Kleine wegklasse:** Marikana Road is OSM-`tertiary`: het wegprofiel heeft `corridorKlassen: ["tertiary"]` nodig.
- **Volumemix:** 6E (Pt+Pd+Rh+Au+Ru+Ir); de 50% is een aandeel van het concentraat, geen gemeten ritvolume; koz ÷ 32,15 = t.

## 8 · Bronnen
[1] Tharisa plc, SENS/RNS "Valterra Platinum to purchase 50% of Tharisa Mine PGM concentrate from 1 January 2027", 2026-10-15, https://www.tharisa.com/download/sens-rns-tharisa-valterra-offtake-and-chrome-collaboration-15oct26.pdf
[2] Tharisa plc, Q4 FY2026 production report (153,7 koz 6E, guidance FY2027 150-170 koz), 2026-10-13, https://www.tharisa.com/download/sens-rns-tharisa-q4-fy2026-production-report-13oct26.pdf
[3] Mining-technology, Tharisa/Valterra PGM offtake (50%, 1-1-2027, geen leveringsplaats), https://www.mining-technology.com/news/tharisa-pgm-offtake-valterra-platinum/
[4] Sibanye-Stillwater 20-F FY2025 (huidige afnemer; niet gelezen, alleen als startpunt), https://www.sec.gov/Archives/edgar/data/0001786909/000162828026026991/sbsw-20251231.htm
[5] `v2/design/routebrieven/pgm-zimplats-rustenburg.md` §3 (anker PMR -25.6838/27.3272, z15) en `pgm-unki-rustenburg.md` §3 (letterlijk hergebruikt).
[6] `v2/design/routebrieven/pgm-bafokeng-waterval.md` §3 en §8 [9] (smelterstrook -25.6750/27.3180, OSRM-corridorvergelijking).
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-pgm-tharisa-waterval-tharisa-z15.png` en `sat-pgm-tharisa-waterval-pmr-z15.png`.
[8] `v2/design/pgm-sitelaag.json`, `w-tharisa`: FY2023 ~155 koz 6E, PGM als bijproduct van chroom (coördinaat aannemelijk, niet gebruikt).
[9] OSRM public demo (router.project-osrm.org), 2026-10-31: plant -> PMR 24,24 km (Marikana Road D1325 5,2 km, Karee Road D108 1,3 km, ~14 km onbenoemd west); met de vier via-punten 24,24 km. Indicatie, geen publicatie.
[10] Polity/Engineering News, "Jameson cells saving Valterra Platinum R203m, keeping 3 000 trucks off road", 2026-09-23 (alleen zoekresultaat-snippet: Waterval krijgt UG2-voeding van derden, Amandelbult en Mototolo), https://polity.org.za/article/jameson-cells-saving-valterra-platinum-r203m-keeping-3-000-trucks-off-road-2026-09-23

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-pgm-tharisa-waterval.json` (9,2 KB, contract versie 2, lonlat) · **functie:** `bak_pgm_tharisa_waterval()` in `bak_stromen.sh` · **profiel:** `pgm-tharisa-waterval-tharisa-waterval` in `maak_stroombeen_weg.py` · tussenuitvoer `v2/build-cache/ais/graaf/pgm-tharisa-waterval-weg-tharisa-waterval.geojson`.

| # | modaliteit | been | km (gemeten) | punten | stippel |
|---|---|---|---|---|---|
| b1 | truck | Tharisa Mine → Marikana Road D1325 → Karee Road D108 → R104-corridor west → Waterval/PMR (aannemelijk: één bron) | 24,5 (weg 24,2 + ankerstukken 0,03 en 0,20) | 405 | nee |

Totaal 24,5 km, 2 markers (`pgm-tharisa-plant`, `pgm-rustenburg-pmr`), 0 naden (één been), beide markers 0,0 km van de lijn.

**Recept:** `wegscan_puur.py --profiel pgm-tharisa-waterval-tharisa-waterval` (extract zuid-afrika, 124 s scan, refs D1325 D108 R104, corridorKlassen tertiary + unclassified, vensterKm 20, 4 via-punten uit §4 ongewijzigd, snaps 0,00-0,05 km, eindsnap kade 0,20 km), daarna `bash v2/tools/bak_stromen.sh pgm-tharisa-waterval`. Geen haven-aanloop, stippel, lucht, leiding of kopie.

**Toets:** lengte 24,2 km tegen indicatie 24 (+0,9%) is een indicatie, geen norm (geen echte wegkm; hemelsbreed 18,3 km). Lijn gaat direct noordwaarts de plant uit via D1325 en komt niet op de N4 (zuidelijkste punt is de plant zelf; N4 ligt ~1 km zuidelijk). `toets_knikken`: 9 knikken >= 60 gr (alle hoekpunten van kruispunten, 9-34 m straal), 0 omkeringen, 0 terugloop. `toets_rechte_benen`: geen treffer.

**Open / aan de orkestrator:** (1) leveringspunt Waterval blijft aanname (brief §7); (2) sitelaag `w-tharisa` (-25.63, 27.63) ligt 18,2 km ONO van de plant: centraal gelijktrekken; (3) de lijn eindigt op het PMR-anker -25.6838/27.3272 (hergebruikt), niet op de smelterstrook 1,3 km NW; (4) lijn is toekomstig (vanaf 1-1-2027), huidige afnemer Sibanye.

**Lessen:** een korte tertiary-corridor (D1325 / D108 / onbenoemd) gaat er met `corridorKlassen` ["tertiary","unclassified"] en 4 via-punten schoon doorheen, geen wegklasse-probleem; Zuid-Afrika-scan kost ~2 min per nieuw profiel.
