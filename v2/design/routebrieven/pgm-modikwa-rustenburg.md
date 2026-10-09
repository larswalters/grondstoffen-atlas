# Routebrief (licht) · PGM — Modikwa via Polokwane-smelter naar ACP Rustenburg (Zuid-Afrika)

**stroom-id:** `pgm-modikwa-rustenburg` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) ·
**status:** gebakken
**Keten in één zin:** PGM-concentraat van de Modikwa-concentrator (JV Valterra/ARM, Eastern Limb, Limpopo/Mpumalanga)
per **truck** over de R37 naar de **Valterra Polokwane-smelter** [1][3]; de matte per **truck** (aannemelijk: één bron,
modaliteit niet in de bron) via de R37/N1-aansluiting en de N1/N4 naar het **Anglo Converter Plant (ACP)** in het
Waterval-complex bij Rustenburg [3] — hetzelfde eindanker als `pgm-rustenburg-pmr`.
**Welke as van het verhaal:** de Oostelijke-rand-JV die al zijn metaal-in-concentraat aan Valterra levert [2] en via
Polokwane (niet Mortimer, dat stilstaat) in de Rustenburg-converting loopt. ~8,8 t 6E/j (ARM F2025, zie §7).

## 1 · Ketenkaart
```
Modikwa-concentrator `pgm-modikwa-mijn` ──(b1 truck · lokale weg → R37 Maandagshoek–Mecklenburg–Lebowakgomo ·
  hemelsbreed 99 km, geen wegkm)──► Polokwane-smelter `pgm-polokwane-smelter`
  ──(b2a truck · R37 noordwaarts · hemelsbreed ~10 km, geen wegkm, aannemelijk)──► R37/N1-aansluiting
  ──(b2b truck · N1 → N4 · 359,9 km, LETTERLIJKE KOPIE pgm-zimplats-rustenburg b2 vanaf vertex 2050, aannemelijk)──►
  Rustenburg ACP/PMR `pgm-rustenburg-pmr` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-modikwa-mijn` → `pgm-polokwane-smelter` | R37 (Burgersfort-Polokwane) | hemelsbreed 99 km, geen wegkm; indicatie ~113 km tot Polokwane + smelter [5][6], eigen scan 126,1 km [12] | maak_stroombeen_weg | nee |
| b2a | A | truck | smelter → R37/N1-aansluiting (-23.9431, 29.4439) | R37 noord, Polokwane-zuid (aannemelijk) | hemelsbreed ~10 km, geen wegkm; eigen scan 12,7 km [12] | maak_stroombeen_weg | nee |
| b2b | A | truck | R37/N1-aansluiting → `pgm-rustenburg-pmr` | N1 Polokwane–Pretoria → N4 (aannemelijk: één bron) — LETTERLIJKE KOPIE van `pgm-zimplats-rustenburg` b2, vertex 2050 t/m einde | 359,9 (kopie) [11] | kopie geojson, nieuw bestand | nee |

Geen zee-, spoor-, binnenvaart-, leiding- of luchtbeen; geen haven-aanloop; geen fase D/E (geen bron noemt een afnemer ná ACP in deze as).
b2a+b2b = smelter → ACP; het eindpunt is niet "Rustenburg PMR" als raffinaderij maar de converting-stap op hetzelfde Waterval-complex.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-modikwa-mijn` | mijn + concentrator | Modikwa Platinum Mine, concentrator (JV Valterra 50 / ARM 41,5 / gemeenschappen 8,5), Maandagshoek, Limpopo | -24.6565, 30.1675 | [1][7][13] | aannemelijk (z15 gezien: schachtgebouwen en grijze steenbergen, een grote tailings-dam ~3 km NW met bezinkvijvers; bron zegt 15 km N van Steelpoort, anker ligt 9,2 km — site wel zichtbaar) |
| `pgm-polokwane-smelter` | smelter (elektrische oven, SO2-installatie) | Valterra Polokwane-smelter, OSM way 804571574, ~14 km ten zuiden van Polokwane | -24.0281, 29.4694 | [1][3][8] | bron-gelegd (z15 gezien: ovengebouw met schoorstenen en rookpluim, donkere slakdam 1 km ZW, R37 op ~1 km westelijk) |
| `pgm-rustenburg-pmr` | losplek / converting (ACP) | Waterval-complex, Valterra, Rustenburg — **hergebruikt letterlijk** uit `pgm-unki-rustenburg.md` | -25.6838, 27.3272 | [3][11] | bron-gelegd (overgenomen; z15 gezien bij die brief) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; lat, lon; alle op de R37)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | R37 bij Maandagshoek | -24.5878, 30.1591 | waar de plantweg op de R37 uitkomt; pint de R37 i.p.v. de zuidelijke Burgersfort-zijde |
| b1 | 2 | R37 bij Mecklenburg | -24.3803, 30.0659 | houdt de R37 noordwaarts i.p.v. een binnenweg via Steelpoort/Ohrigstad |
| b1 | 3 | R37 bij Olifants/Ga-Makgoba | -24.2600, 29.8207 | pint de Orrie Baragwanath-passage en de Olifants-rivierkruising [5] |
| b1 | 4 | R37 ten noorden van Lebowakgomo | -24.1829, 29.4842 | houdt de R37 vast naar Polokwane, niet de R518 het stadje in; buiten de stadskern |
| b2a | 1 | R37 zuidrand Polokwane | -24.0357, 29.4591 | pint de R37 noordwaarts vanaf de smelter-aansluiting (de oven ligt zelf aan een kleine weg) |
| b2b | — | via-punten van de bron (Polokwane, Pretoria N1/N4, Rustenburg N4/R24) | zie `pgm-zimplats-rustenburg.md` §4 | ongewijzigd overgenomen, geen tweede versie van dezelfde corridor |

Geofabrik-regio: `zuid-afrika` (alle benen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Modikwa-concentrator | Modikwa JV (Valterra/ARM) | 2,49 Mt erts gemalen (2025) → PGM-concentraat | 277 koz 6E (100%, 2025) | [1] |
| Polokwane-smelter | Valterra Platinum | concentraat (o.a. Mogalakwena, Modikwa) → ovenmatte; zes-in-lijn-oven + SO2-installatie sinds 2021 | niet in t/j gepubliceerd | [3] |
| Anglo Converter Plant (Waterval) | Valterra Platinum | ovenmatte → converter-matte | niet in t/j gepubliceerd | [3] |

## 6 · Stoppunt
De brief stopt bij ACP Rustenburg (Waterval-complex, hetzelfde anker als de PMR): geen bron in dit onderzoek noemt een
gedocumenteerde volgende locatie of vervoerswijze voor de converter-matte.

## 7 · Open punten
- **Wegkm niet gepubliceerd.** Alleen hemelsbreed (b1 99 km, b2a ~10 km). Indicaties: Wikipedia R37 Polokwane–Burgersfort ~139 km (som van segmenten) min 25,9 km Modikwa–Burgersfort [5][6] ≈ 113 km; eigen OSM-scan b1 126,1 km, b2a 12,7 km — de ±15%-toets is een indicatie.
- **Matte-modaliteit** Polokwane → ACP staat niet in de bron ("transported", [3]); truck is aanname — daarom "aannemelijk" in b2a/b2b.
- **b2a loopt eerst ~10 km noordwaarts** naar de N1-aansluiting om dan terug zuidwest op de N1 te gaan; een directere lokale verbinding is niet onderzocht (bindende haalbaarheidstoets).
- **Sitelaag `w-modikwa`** (-24.68, 30.23) ligt ~6,8 km ten oosten van de hier gelegde concentrator; centraal gelijktrekken naar -24.6565, 30.1675 (niet door mij aangepast).
- **Afstand tot Steelpoort:** bron 15 km N [1], gemeten 9,2 km; een zoekresultaat meldt voor Valterra IAR 2025 "25 km W van Burgersfort" — de ligging is dus aannemelijk, niet bron-gelegd.
- **Volume:** ARM F2025 (jul 2024–jun 2025) 281.638 oz 6E ÷ 32,15 = 8,8 t 6E/j (Pt 120 koz, Pd 102 koz, Rh 20 koz); Valterra MRMR 2025 geeft 277 koz 6E (100%) = 8,6 t; IAR 2025 138,4 koz bij 50% [2][1][4]. Sitelaag noemt 5,6 t 4E (oud). Mix = 6E.
- **Overlap:** b2b is 100% gedeeld met `pgm-zimplats-rustenburg` b2 (vanaf Polokwane) en `pgm-unki-rustenburg` b2; eigen geometrie b1+b2a ~140 km (28%). Lijkt op de afgewezen `pgm-derbrochen-rustenburg`; verschil: Polokwane-knoop, JV-rol, eigen R37-corridor.

## 8 · Bronnen
[1] Valterra Platinum, Ore Reserves and Mineral Resources report 2025, p.91–94 (Modikwa: 15 km N Steelpoort, JV, concentraat naar Polokwane-smelter, productietabel), https://www.valterraplatinum.com/wp-content/uploads/2026/05/ore-reserves-and-mineral-resources-report-2025.pdf
[2] ARM, Operational review Platinum F2025 (281.638 oz 6E), https://arm.co.za/wp-content/uploads/2025/10/Ops-review_Platinum.pdf
[3] SAIMM, Snodgrass e.a., Pyrometallurgy 2024 (concentraat per truck naar de smelters; ovenmatte naar het ACP), https://www.saimm.co.za/Conferences/files/pyrometallurgy-2024/16_646-Snodgrass.pdf
[4] Valterra Integrated report 2025 (Modikwa 138,4 koz bij 50%, Mortimer in care and maintenance) — via de haalbaarheidstoets, niet opnieuw geopend, https://www.valterraplatinum.com/wp-content/uploads/2026/05/integrated-report-2025.pdf
[5] Wikipedia, R37 road (South Africa) (304 km; Polokwane–Lebowakgomo–Burgersfort), https://en.wikipedia.org/wiki/R37_(South_Africa)
[6] Engineering News, National Road R37 Section 1 Modikwa mine to Burgersfort (25,87 km; via zoekresultaat, pagina 403), https://engineeringnews.co.za/article/national-road-r37-section-1-modikwa-mine-to-burgersfort-road-improvement-south-africa-2021-06-25
[7] Wikipedia, Modikwa mine (NW van Burgersfort, 50/50-JV), https://en.wikipedia.org/wiki/Modikwa_mine
[8] OpenStreetMap-contributors (ODbL) via Nominatim: Steelpoort (-24.7316, 30.2056), Burgersfort (-24.6736, 30.3283), Mecklenburg/R37; smelter = OSM way 804571574 (haalbaarheidstoets)
[9] Mining Technology, Modikwa Platinum (concentraat naar Polokwane-smelter; via zoekresultaat), https://www.mining-technology.com/projects/modikwa-platinum/
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-pgm-modikwa-rustenburg-modikwa.png`, `…-polokwane-smelter.png`
[11] `v2/design/routebrieven/pgm-zimplats-rustenburg.md` (b2, geojson `pgm-zimplats-rustenburg-weg-beitbridge-rustenburg.geojson`) en `pgm-unki-rustenburg.md` (anker PMR)
[12] Eigen OSM-wegscan (`v2/tools/wegscan_puur.py`, zuid-afrika-extract, 2026-10-09): b1 126,1 km, b2a 12,7 km, snaps ≤ 0,32 km
[13] `v2/design/pgm-sitelaag.json` w-modikwa (-24.68, 30.23; aannemelijk, niet satelliet-bevestigd)

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)

**Resultaat:** `v2/data/stroomroute-pgm-modikwa-rustenburg.json` (68,6 KB, versie 2, lonlat), 3 truckbenen, 499,6 km, 3 markers, geen stippel.
Recept: functie `bak_pgm_modikwa_rustenburg()` in `v2/tools/bak_stromen.sh`; profielen `pgm-modikwa-rustenburg-modikwa-polokwane` en
`pgm-modikwa-rustenburg-smelter-r37n1` in `v2/tools/maak_stroombeen_weg.py` (extract zuid-afrika, via `wegscan_puur.py`, scan-cache hergebruikt).

| # | modaliteit | been | km gemeten | km brief | afwijking | naad |
|---|---|---|---|---|---|---|
| 1 | truck | Modikwa-concentrator → Polokwane-smelter (R37) | 126,7 | hemelsbreed 99, indicatie ~113 (geen wegkm) | +12% op de indicatie, omwegfactor 1,28 | 0 |
| 2 | truck | Polokwane-smelter → R37/N1-aansluiting (aannemelijk) | 13,0 | hemelsbreed ~10 (geen wegkm), eigen scan 12,7 | indicatie | 0,00 km |
| 3 | truck | R37/N1-aansluiting → ACP Rustenburg (N1 → N4, aannemelijk) | 359,9 | 359,9 (kopie) | 0% | 0,00 km |

Markers: Modikwa-concentrator (-24.6565, 30.1675), Polokwane-smelter (-24.0281, 29.4694), Rustenburg ACP/PMR (-25.6838, 27.3272); alle op 0,0 km van de lijn.

**Toelichting.** Geen stippel, haven-aanloop, vlucht of leiding: de keten ligt volledig op de Zuid-Afrikaanse weg. De ±15%-toets is voor b1 en b2a een
indicatie (geen gepubliceerde wegkm); b1 valt er met +12% binnen. b2b is een letterlijke kopie (vertex 2050 t/m einde, 2004 punten) van het geojson van
`pgm-zimplats-rustenburg` b2, in de beennaam vermeld. De beennamen van b2a en b2b dragen "aannemelijk: één bron" (matte-modaliteit niet in de bron).

**Bevindingen en lessen.**
- b1: de eerste 7,4 km vanaf de concentrator lopen over kleine klassen (plantweg, residential/service/unclassified); daarna R37 zonder omweg (via-snaps ≤ 0,01 km).
- b2a: via-punt "R37 zuidrand Polokwane" geeft een kort spoor van ca. 0,13 km heen en terug (knik 171°, straal 3 m); bewust niet verplaatst om het getal te halen. b2a loopt ca. 10 km noordwaarts en dan terug op de N1; een directere verbinding is niet onderzocht.
- b2b: de letterlijke kopie bevat één terugloop-knik bij Rustenburg (-25.7046, 27.2558, 8 m radius) uit de bronstroom; niet hier aangepast (andermans geometrie), melden bij `pgm-zimplats-rustenburg`.
- De eerdere scan-geojsons droegen testnamen ("test", "test2"); door de profielen vast te leggen en `wegscan_puur.py` opnieuw te draaien (cache, seconden) staan de echte namen erin.
- Centraal nog te doen: register (sleutel `pgm-mr`), bundel, sitelaag `w-modikwa` 6,8 km naar het gelegde anker trekken.
