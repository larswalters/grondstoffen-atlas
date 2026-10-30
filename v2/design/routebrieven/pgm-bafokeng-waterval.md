# Routebrief (licht) · PGM — Impala Bafokeng-concentrator → R565/N4 → Waterval-smelter (Zuid-Afrika)

**stroom-id:** `pgm-bafokeng-waterval` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** PGM-concentraat (6E: Pt, Pd, Rh, Ru, Ir, Au) van de Impala Bafokeng-mijnen (Styldrift en BRPM, ~37 km NW van Rustenburg; Implats, ex-RBPlat) per **truck** (aannemelijk: één bron voor de bestemming) over R565, Ottoman Highway (P115-1), N4 en R24 naar het Waterval-smelterscomplex van Valterra Platinum (ex-Amplats) bij Rustenburg; stoppunt = de smelter.
**Welke as van het verhaal:** Bushveld-westrand: Impala Bafokeng verkoopt zijn concentraat aan Valterra, dus aan een concurrent als smelter ("disposal of concentrate agreement" met Amplats via RPM [1]). Volume: **15,0 t 6E/j** (483.000 oz 6E in concentraat, FY2024 [1]; koz ÷ 32,15). Eén anker voor twee concentrators.

## 1 · Ketenkaart
```
Impala Bafokeng Styldrift `pgm-bafokeng-styldrift` ──(b1 truck · Z546/Z527 → R565 → Ottoman Highway (P115-1) → N4 → R24 · meer dan 65 km [2], eigen OSRM 57 km · aannemelijk: één bron)──►
  Waterval-smelter (Valterra) `pgm-rustenburg-pmr` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Styldrift → Waterval-smelter (aannemelijk: één bron) | Z546/Z527 → R565 (Boshoek–Phokeng) → Ottoman Highway (P115-1) → N4 → R24 | meer dan 65 km (RBPlat 2013, erts naar Waterval, openbare weg [2]); hemelsbreed 37 km, geen wegkm; eigen OSRM 57,0 km [9] | maak_stroombeen_weg (nieuw profiel) | nee, doorgetrokken |

Geen zee-, spoor-, lucht-, leiding- of binnenvaartbeen; geen fase B/C/D/E. Waarom truck: Valterra beschrijft dat concentraat van eigen, JV- en derde-partij-concentrators per truck naar de smelters gaat [3]; Mining Technology zegt dit specifiek voor Styldrift ("trucked to the RPM smelting and refining operations" [4]). Geen bron noemt de route (§7).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-bafokeng-styldrift` | mijn + concentrator (laadplek) | Styldrift I (Impala Bafokeng), Chaneng/Rasimone, ~37 km NW van Rustenburg | -25.3977, 27.1084 | [1][5][6] | bron-gelegd (z15 gezien: schachtcomplex met hijsgebouwen, zonnepanelen en twee bezinkvijvers, kruis erop; OSM way 804634901 "Styldrift", centrum -25.39767/27.10838; toegangsweg zuidwaarts, dorp Chaneng 1,5 km oost) |
| `pgm-rustenburg-pmr` | smelter (losplek, stoppunt) | Waterval-complex, Valterra Platinum, ~7 km ONO van Rustenburg-centrum — **hergebruikt letterlijk** uit `pgm-rustenburg-shanghai.md` §3 en `pgm-amandelbult-iselin.md` §3 (de smelterstrook) | -25.6750, 27.3180 | [3][7][10] | bron-gelegd (opnieuw z15 gezien: smelterstrook met schoorstenen en ovengebouwen, slakveld/tailings-dam 1–2 km NW, raffinage-/BMR-deel met blauwe bezinkput ~1,3 km ZO) |

**Verschil tussen de twee Waterval-waarden:** -25.6750/27.3180 (smelterstrook, gekozen) en -25.6838/27.3272 (raffinagedeel, gebruikt door `pgm-unki-rustenburg`/`modikwa`/`mototolo`/`zimplats`) liggen 1,34 km uit elkaar, beide binnen het complex; b1 is een smelterbeen, dus de smelterstrook.

## 4 · Via-punten (b1, reisvolgorde; coördinaten op de weg, geen stadscentrum; refs door Nominatim gecontroleerd)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | R565 bij Boshoek (Nominatim: R565 `secondary`) | -25.4762, 27.0867 | pint de R565 zuidwaarts (via Z546/Z527 vanaf de site) i.p.v. een lokale weg langs Rasimone; hier loopt ook het BRPM-verkeer |
| b1 | 2 | Ottoman Highway (P115-1) tussen Phokeng en de N4 (Nominatim: `secondary`) | -25.6107, 27.1494 | corridorkeuze: Phokeng → N4-bypass i.p.v. R565/R104 dwars door Rustenburg-centrum (OSRM: 50 km door de stad, 57 km via de N4) |
| b1 | 3 | N4 ten zuiden van Rustenburg (Nominatim: `trunk` N4) | -25.6900, 27.2264 | houdt de N4 langs de zuidkant van de stad |
| b1 | 4 | N4/R24-kruising Rustenburg — **hergebruikt** uit `pgm-zimplats-rustenburg.md` §4 | -25.7031, 27.2572 | laatste punt vóór het Waterval-complex; pint R24 noordwaarts naar het complex |

Geofabrik-regio: `zuid-afrika` (hele been). Refs: R565, P115-1, N4, R24. Eerste 8,5 km (Z546, Z527) en laatste ~10 km (R24, D108, lokaal) zijn lagere wegklassen: `corridorKlassen` tertiary en unclassified waarschijnlijk nodig.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Impala Bafokeng-concentrators (twee: BRPM en Styldrift I) | Implats (87%, sinds 2023) | 4,24 Mt erts gemalen (FY2024) → PGM-concentraat | 483.000 oz 6E in concentraat (FY2024) | [1] |
| Waterval-smelter + ACP | Valterra Platinum | concentraat → ovenmatte (twee zes-in-lijn-ovens, twee converters, slakreiniging) → converter-matte | niet in t/j gepubliceerd | [3] |

## 6 · Stoppunt
De brief stopt bij de Waterval-smelter: Impala Bafokeng noemt alleen de afnameovereenkomst met Amplats/RPM [1], geen vervolg; wat daarna met de matte gebeurt is al getekend in de bestaande Valterra-ketens vanaf hetzelfde anker (`pgm-rustenburg-shanghai`, `pgm-rustenburg-tokio`); geen fase D.

## 7 · Open punten
- **Smelter aannemelijk, niet gebrond (één bron).** De factsheet [1] noemt het contract met Amplats via RPM maar geen fysieke plant; Miningmx 2020 [8] zegt dat RBR al zijn concentraat aan RPM verkoopt en dat de force majeure van Amplats "technical problems at Waterval" betrof, Mining Technology [4] noemt de RPM-smelter. Dat is aannemelijk voor Waterval, maar geen bron zegt "Styldrift-concentraat naar de Waterval-smelter". Sinds de Implats-overname (2023) kan het contract verschuiven naar Impala Rustenburg (niet onderzocht; een eigen Implats-smelter bestaat daar).
- **Km-spreiding.** ">65 km" [2] is een RBPlat-planning uit 2013 voor het ertstransport naar de Waterval-*concentrator* (225 ritten/dag, 45 trucks), geen concentraat naar de smelter; mijn eigen OSRM (publieke demo, geen bron) geeft 57,0 km via de N4 en 50,0 km door Rustenburg-centrum [9]. De ±15%-toets is dus een indicatie: 57 tegen 65 is -12%.
- **Twee concentrators, één anker.** BRPM (Boschkoppie 104 JQ) is niet apart gelegd: ik vond geen coördinaat [1]; op z14 ligt langs de R565 bij -25.42/27.085 een procescomplex met een zeshoekige tailingsdam, vermoedelijk BRPM, niet bevestigd. De 15 t geldt voor beide; BRPM gebruikt dezelfde R565-corridor.
- Of de Styldrift-concentrator op dit anker staat of enkele honderden meters verder is op z15 niet apart herkend (site-niveau).
- Sitelaag `w-bafokeng-styldrift` (-25.45/27.10, 10,0 t, aannemelijk) ligt ~5,9 km zuid van dit anker en is volumeverouderd (15,0 t tegen 10,0 t); niet aangepast (sitelagen zijn niet van deze brief).
- FY2025-cijfer niet opgezocht (peiljaar FY2024); de SEC-rapport [6]-vermelding bevat geen Waterval-smelter-tekst in de gelezen 100.000 tekens: alleen "tolling agreement with Valterra Platinum" voor Sibanye Rustenburg, dus niet gebruikt als bewijs voor deze keten.
- SENS 2020-04-29 (JSE) gaf HTTP 403 en is niet herlezen; de force-majeure-inhoud komt uit Miningmx [8].

## 8 · Bronnen
[1] Implats, Impala Bafokeng fact sheet (feb 2025): 2 mijnen + 2 concentrators ~30 km NW van Rustenburg, 37 km NW volgens de locatietekst; FY2024 4.243 kt gemalen, 483.000 oz 6E in concentraat; disposal of concentrate agreement met Amplats via RPM. https://implats.co.za/pdf/fact-sheets/2025/fact-sheet-impala-bafokeng.pdf
[2] RBPlat Ore Processing Strategy, 12 nov 2013, dia 7: "Distance from Styldrift to Waterval > 65 km", openbare weg, 225 ritten/dag, 45 trucks (ertstransport; gelezen). https://implats.co.za/pdf/rbplats/presentations/conference-and-site-visits/2013/rbplat-ore-strategy-12112013.pdf
[3] SAIMM, Snodgrass e.a., Pyrometallurgy 2024: concentraat van AAP-, JV- en derde-partij-concentrators wordt per truck naar de smelters gebracht; Waterval-smelterscomplex in Rustenburg (twee ovens, twee converters, slakreiniging); ACP. https://www.saimm.co.za/Conferences/files/pyrometallurgy-2024/16_646-Snodgrass.pdf
[4] Mining Technology, Styldrift Platinum Project: concentraat wordt na de verdikker "trucked to the Rustenburg Platinum Mine's (RPM) smelting and refining operations". https://www.mining-technology.com/projects/styldrift-platinum-project/
[5] OpenStreetMap-contributors (ODbL), Nominatim 2026-10-30: Styldrift way 804634901 (-25.39767, 27.10838); Phokeng (-25.5754, 27.1565); Boshoek (-25.4801, 27.0963); refs R565, Ottoman Highway, N4 per reverse-lookup op de via-punten.
[6] SEC, Sibanye-Stillwater Rustenburg Operation technical report (gelezen tot teken 100.000): tolling agreement met Valterra; Waterval-faciliteiten van Sibanye (concentrators), geen smelterbewijs voor deze keten. https://www.sec.gov/Archives/edgar/data/1786909/000162828026026991/ssw_rustenburgxoperation.htm
[7] Routebrieven `pgm-rustenburg-shanghai.md` en `pgm-amandelbult-iselin.md` (anker -25.6750/27.3180), `pgm-zimplats-rustenburg.md` (via-punt N4/R24, eindanker -25.6838/27.3272).
[8] Miningmx 2020, "RBPlat to temporarily accede to Amplats force majeure": RBR verkoopt al zijn concentraat aan RPM; force majeure wegens technische problemen bij Waterval. https://www.miningmx.com/news/platinum/40635-rpplat-to-temporarily-accede-to-amplats-force-majeure-pending-outcome-of-discussions/
[9] OSRM public demo (router.project-osrm.org), 2026-10-30: Styldrift → Waterval 50,0 km (Z546, Z527, R565, R104 door Rustenburg, D108) en 57,0 km (R565, P115-1, N4, R24, D108); indicatie, geen publicatie.
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15, z14): `v2/build-cache/satcheck/sat-pgm-bafokeng-waterval-styldrift.png`, `…-waterval.png`, `…-waterval-b.png`, `…-brpm-zoek.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)

**Recept:** `bash v2/tools/bak_stromen.sh pgm-bafokeng-waterval` → `v2/data/stroomroute-pgm-bafokeng-waterval.json` (16,2 KB, contract versie 2, lonlat, 1 been, 757 punten, 2 markers).
Weg: profiel `pgm-bafokeng-waterval-styldrift-waterval` in `maak_stroombeen_weg.py` (extract `zuid-afrika`, refs R565/P115-1/N4/R24, `corridorKlassen` tertiary+unclassified, vensterKm 40), gescand met `wegscan_puur.py` → `v2/build-cache/ais/graaf/pgm-bafokeng-waterval-weg-styldrift-waterval.geojson`.

| # | modaliteit | been | km | stippel |
|---|---|---|---|---|
| b1 | truck | Styldrift (Impala Bafokeng) → Waterval-smelter, Valterra (aannemelijk: één bron; Z546/Z527, R565, Ottoman Highway, N4, R24) | 57,3 | nee, doorgetrokken |

Totaal 57,3 km. Markers (2): `pgm-bafokeng-styldrift` (-25.3977, 27.1084) en `pgm-rustenburg-pmr` (-25.6750, 27.3180), beide 0,0 km van de lijn.

- **Km-toets:** 57,1 km weggeometrie (57,3 km getekend) tegen ">65 km" (RBPlat 2013) = -12,2%; het wegtool meldt "buiten ±10%", binnen ±15%. Brief §7 noemt de toets al een indicatie: eigen OSRM gaf 57,0 km via de N4, dus de scan bevestigt die route, niet de 65. Segmenten 10,6 / 18,8 / 13,4 / 4,1 / 10,5 km; geen omweg (alle via-snaps 0,00 km, anker-snaps 0,02 en 0,17 km).
- **Naden:** één been, dus geen naad. Geen haven-aanloop, kopie, lucht of stippel (Styldrift en Waterval liggen aan de openbare weg).
- **Knikken:** `toets_knikken.py` 25 knikken ≥ 60°, waarvan één terugloop van 8 m (150°) bij -25.70456, 27.25575, de N4/R24-kruising (via-punt 4): een rotondelus bij het knooppunt, geen omweg. De overige zijn 3–59 m spikes op knooppunten en op de ankers. `toets_rechte_benen.py`: niet gemeld.
- **Aannemelijk:** de bestemming Waterval-smelter heeft één bron (§7); dat staat in de beennaam, de lijn is doorgetrokken.
- **Open (ongewijzigd uit §7):** BRPM niet apart gelegd (geen marker); sitelaag `w-bafokeng-styldrift` ligt 5,9 km van dit anker en is volumeverouderd, niet aangepast.
- **Lessen:** Zuid-Afrika-scan 151 s op één core; via-punt 4 uit `pgm-zimplats-rustenburg` pinde de R24-aanloop zonder gedoe. Het id belooft Waterval en dat is ook het eindpunt.
