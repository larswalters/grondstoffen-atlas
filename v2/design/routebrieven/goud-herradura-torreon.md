# Routebrief (licht) · Goud · Herradura-mijn (Sonora) → MEX 2 / MEX 45D / MEX 49D → Met-Mex Peñoles Torreón (Mexico)

**stroom-id:** `goud-herradura-torreon` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) ·
**status:** gebakken
**Keten in één zin:** goud-doré van de Herradura-mijn (Penmont, Fresnillo plc, Caborca, Sonora) per **truck** over een
noordelijke corridor (MEX 2 → MEX 10/CHIH 56D-7D → MEX 45D Chihuahua → MEX 49D) naar het Met-Mex Peñoles-complex in
Torreón (Coahuila) — **aannemelijk: één bron voor de relatie, route en vervoerswijze over de lange afstand niet gebronnen**.
**Welke as van het verhaal:** *Mexico binnenlands, goud* — 's lands grootste goudmijn naar het Peñoles-raffinagecomplex;
jaarvolume **≈ 11 t Au/j** (Herradura-omzet US$ 883,6 mln in 2024 [1]; ÷ ≈ 2.390 USD/oz ≈ 370 koz ≈ 11,5 t; kruiscontrole
57% van ≈ 632 koz [4] ≈ 11,2 t).

## 1 · Ketenkaart
```
Herradura-plant `au-herradura-plant` ──(b1 truck · MEX 2 → MEX 10/CHIH 56D-7D → MEX 45D → MEX 49D ·
   OSRM 1.413 km, geen wegkm; hemelsbreed 1.112 km)──► Met-Mex Peñoles Torreón `au-penoles-torreon` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Herradura-plant → Met-Mex Peñoles Torreón | SON-weg (plant → MEX 2) → MEX 2 (Santa Ana–Cananea–Agua Prieta) → MEX 10 (Janos–Buenaventura) → CHIH 56D/7D → MEX 45/45D (Chihuahua-oost) → MEX 49D/49 (Jiménez–Torreón) | OSRM-routeplanner 1.413 [6] (alternatief 1.756), **geen wegkm** (geen bedrijfs-/overheidsopgave); hemelsbreed 1.112, via de punten 1.261 — ±15%-toets is indicatie | maak_stroombeen_weg (extract `mexico`) | nee — doorgetrokken, aannemelijk: route niet gebronnen |

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-herradura-plant` | mijn / plant (laad) | Herradura-plant (CIL-tanks, verdikkers), Minera Penmont | 31.1458, -112.8482 | [1][2][10] | bron-gelegd (z16 gezien: groene CIL-tanks en twee verdikkerkoepels NO van de open put, procesgebouwen en wegen; het OSM-puntje 31.1493,-112.8732 ligt op de westrand van de put, niet op de plant) |
| `au-penoles-torreon` | raffinaderij / smelter (los, stoppunt) | Met-Mex Peñoles-complex, Torreón | 25.5278, -103.4417 | [1][5] | bron-gelegd — letterlijk hergebruikt uit `zilver-fresnillo-torreon.md` §3 (`ag-penoles-torreon`; z16 gezien: industrieel complex met tanks, bezinkvijver en spooraansluiting; OSM way 116771096) |

## 4 · Via-punten (b1 — corridorkeuze noordroute, nooit in een stad; elk punt ligt op de genoemde weg, OSRM-nearest ≤ 6 m)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | MEX 2 Sonoyta–Santa Ana (SON-weg-aansluiting) | 31.3310, -112.5795 | MEX 2 oostwaarts, niet zuid naar Hermosillo/MEX 15 [2][6] |
| b1 | 2 | Libramiento Magdalena de Kino (MEX 2/15D) | 30.6189, -110.9948 | bypass buiten het stadscentrum; MEX 2 naar Cananea, niet MEX 15 naar Nogales [6] |
| b1 | 3 | MEX 2 Cananea–Agua Prieta | 31.1865, -109.9368 | noordelijke grensstrook; pint de Agua Prieta-corridor, niet de Sinaloa-/Durango-zuidroute [6] |
| b1 | 4 | MEX 2 Agua Prieta–Ascensión | 31.0307, -108.3864 | doorgaande MEX 2 richting Janos, voor de overgang naar MEX 10 [6][7] |
| b1 | 5 | CHIH 56D (Ricardo Flores Magón–Galeana) | 30.1167, -107.5116 | tolweg i.p.v. libre MEX 10 via Ricardo Flores Magón [6][7] |
| b1 | 6 | CHIH 7D (El Álamo–Ricardo Flores Magón) | 29.8125, -106.8162 | tolweg naar Chihuahua, naast de libre MEX 45 [6] |
| b1 | 7 | Libramiento Oriente Chihuahua (MEX 45D) | 28.5919, -105.9488 | Chihuahua-stad omzeild, MEX 45D zuidwaarts [6][8] |
| b1 | 8 | MEX 49D Jiménez–Torreón | 26.4850, -103.9927 | pint de MEX 49D-noordaanvoer naar La Laguna (zilverstroom komt van het zuiden: geen gedeeld been) [6][9] |

Bak-profiel (voor de bak-agent): `corridorKlassen ["tertiary","unclassified"]` (plant → SON-weg is een lokale weg, ≈ 28–35 km);
`vensterKm` 40; refs `MEX 2`, `MEX 10`, `CHIH 56D`, `CHIH 7D`, `MEX 45`, `MEX 45D`, `MEX 49D`, `MEX 49`; `gepubliceerdKm` 1413.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Herradura-plant | Minera Penmont (Fresnillo plc) | erts → goud-doré (CIL) | Herradura-omzet US$ 883,6 mln (2024) ≈ 11 t Au/j | [1][4] |
| Met-Mex Peñoles-complex Torreón | Industrias Peñoles | doré → raffinaat (goud/zilver) | 99,6% van de Fresnillo-productie gaat naar Met-Mex (2024) | [1][5] |

## 6 · Stoppunt
Stop bij het Met-Mex-complex: het ketenontwerp noemt geen vervolgstap, geen bron legt de raffinaat-afnemers van deze
doré met naam en adres; fase D/E vervalt.

## 7 · Open punten
- **Vervoerswijze en route Sonora → Coahuila zijn niet gebronnen** (AR24 bewijst de verkoop aan Met-Mex, niet het vervoer).
  Wél bewezen: doré gaat per beveiligde truck (SEPSA) over de weg Caborca–Sonoyta [2]. De noordroute is OSRM-afgeleid.
- **Geen wegkm uit een bedrijfs-/overheidsopgave**: 1.413 km is OSRM (alternatief 1.756 via een andere corridor); hemelsbreed 1.112 km.
- **Herradura-volume is afgeleid** uit omzet ÷ goudprijs (370 koz ≈ 11,5 t); geen gepubliceerd Herradura-ounces cijfer gezien (AJ Bell-pagina gaf 404).
- **Plant → eerste weg** (≈ 28–35 km tot MEX 2) is op OSM een lokale weg; ligt de plant op privéterrein dan stippel "last mile (geen net op deze korrel)".
- **Torreón-aankomst via de stad** (MEX 49 → La Laguna): het eindanker ligt in de bebouwde kom, de weg erheen is niet apart gecontroleerd.
- **Gevonden bij Wikipedia-check:** geen artikel voor de Herradura-mijn; ankers dus uit satelliet en OSM.

## 8 · Bronnen
[1] Fresnillo plc, Annual Report 2024 (financial statements): 99,6% van de productie naar Met-Mex (2023: 99,9%); segmenttabel Herradura third-party omzet US$ 883.571 k; Met-Mex hoofdklant. https://www.fresnilloplc.com/media/gf3fqvci/fresnillo-financial-statements-ar24-web.pdf
[2] El Universal, robbery of a Sepsa vehicle with 47 doré bars (Penmont/Noche Buena, Carretera Internacional Caborca–Sonoyta km 157) en de maart-overval op weg mijn → Fed. 2. https://www.eluniversal.com.mx/estados/robo-de-lingotes-de-oro-en-sonora-es-de-hasta-8-mdd-penmont/ · https://www.eluniversal.com.mx/english/criminals-steal-gold-silver-bars-mexican-mine/
[3] Fresnillo plc RNS 20-05-2009: force majeure Met-Mex voor doré en precipitaat van Herradura en Ciénega opgeheven. https://investegate.co.uk/announcement/rns/fresnillo--fres/pe-oles-lead-precious-metals-refinery-lifts-fo-/2114453
[4] AJ Bell, Fresnillo 2024 (Herradura 57% van het goud) — via het ketenontwerp, niet zelf kunnen openen (404); Fresnillo FY24 attributable goud ≈ 631,6 koz volgens BMV-/Sharecast-samenvatting. https://www.ajbell.co.uk/news/articles/fresnillo-shares-expects-profit-and-revenue-surge-for-2024
[5] Wikipedia, Peñoles: Met-Mex-complex (loodsmelter, zinkraffinaderij) in Torreón. https://en.wikipedia.org/wiki/Pe%C3%B1oles
[6] OSRM (router.project-osrm.org), route 31.1458,-112.8482 → 25.5278,-103.4417: 1.413,4 km, stappen en wegnamen (MEX 2, 10, CHIH 56D/7D, MEX 45/45D, MEX 49D/49); via-punten gesampled en met /nearest op de wegnaam gecontroleerd.
[7] Wikipedia, Mexican Federal Highway 10 en 2: MEX 10 Janos–Nuevo Casas Grandes–Buenaventura; MEX 2 grenscorridor (1.343 km westdeel). https://en.wikipedia.org/wiki/Mexican_Federal_Highway_10
[8] Wikipedia, Mexican Federal Highway 45 (45D = tolweg parallel aan de libre MEX 45). https://en.wikipedia.org/wiki/Mexican_Federal_Highway_45
[9] Wikipedia, Mexican Federal Highway 49 (Ciudad Jiménez – Fresnillo, co-signed met MEX 40 Gómez Palacio–Cuencamé). https://en.wikipedia.org/wiki/Mexican_Federal_Highway_49
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14 en z16): `v2/build-cache/satcheck/sat-goud-herradura-torreon-plant.png`, `sat-goud-herradura-torreon-plant-z14.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Bestand:** `v2/data/stroomroute-goud-herradura-torreon.json` (281,2 KB, contract v2, lonlat) · recept `bak_goud_herradura_torreon()` in `v2/tools/bak_stromen.sh` · profiel `goud-herradura-torreon-herradura-torreon` in `v2/tools/maak_stroombeen_weg.py` (scan via `wegscan_puur.py`, extract `mexico`, 331 s, 13.186 punten).

| # | modaliteit | been | km gemeten | km brief | afwijking | naad |
|---|---|---|---|---|---|---|
| 1 | truck (doorgetrokken) | Herradura-plant → MEX 2 → CHIH 56D/7D → MEX 45D → MEX 49D → Met-Mex Peñoles Torreón | 1.434,7 | 1.413 (OSRM, geen wegkm) | +1,5% (indicatie) | n.v.t. |

Totaal 1.434,7 km · 2 markers (plant 0,0 km en Peñoles 0,0 km van de lijn) · geen stippel, geen haven-aanloop, geen lucht, geen kopie.
**Toelichting.** Plant → MEX 2 is een lokale weg van 34,8 km die de scan over de kleine klassen (tertiary/unclassified) volledig vond: doorgetrokken, plant → weg 0,28 km en weg → kade 0,31 km (eindzone), dus geen last-mile-stippel. Alle 8 via-punten snapten op ≤ 0,01 km; geen enkel segment een omweg (segment 2 Sonoyta → Magdalena: 235 km op ≈ 170 hemelsbreed, bergweg, geen lus). 15 keerlussen gesnoeid (1.436,9 → 1.434,1 km). `toets_knikken`: 54 knikken ≥ 60 gr (rotondes/knooppunten), 0 omkeringen, 0 terugloop; `toets_rechte_benen`: geen treffer.
**Aannemelijk, niet gebronnen:** vervoerswijze en noordroute Sonora → Coahuila (AR24 bewijst alleen de verkoop aan Met-Mex); de ±15%-toets is hier indicatie omdat 1.413 km OSRM is en geen wegkm. Torreón-aankomst via de bebouwde kom komt uit op het anker (0,31 km weg → kade).
**Lessen.** Alle vier weg-slots waren bezet (≈ 4 min wachten); een eenbenige 1.400 km-truckketen door één extract is in ≈ 6 min gescand en volledig doorgetrokken.
