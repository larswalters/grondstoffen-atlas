# Routebrief (licht) · PGM — Mimosa → Zimplats SMC Selous (Zimbabwe), tolsmelt-aandeel onbekend

**stroom-id:** `pgm-mimosa-selous` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) ·
**status:** gebakken
**Keten in één zin:** PGM-concentraat van de **Mimosa-mijn en -concentrator** (Sibanye-Stillwater/Implats 50:50, Zvishavane/Bannockburn, Great Dyke) per **truck**
over Zvishavane, Shurugwi en de **A5** (Gweru, Kwekwe, Kadoma, Chegutu) naar de **Zimplats Selous Metallurgical Complex (SMC)**, waar Mimosa een deel van zijn concentraat
in tol laat smelten tot matte voor export; één landbeen, geen zee, geen luchtbeen, geen fase D/E (waar de matte heen gaat is niet gebrond).
**Welke as van het verhaal:** de Zimbabwaanse omslag naar lokale beneficiatie (exportheffing 3% op concentraat, 2,5% op matte): Mimosa-concentraat dat niet meer alleen
de grens over gaat (`pgm-mimosa-springs`) maar deels in eigen land wordt gesmolten. **Het aandeel dat naar Selous gaat is niet gepubliceerd.**
Volume: **bovengrens 7,3 t 4E/j** = 2 × 117.019 oz 4E (Sibanye-aandeel 50%, FY2025; 4E = Pt+Pd+Rh+Au) ÷ 32,15 [1]; 2024: 2 × 123 koz = 7,7 t; wat daarvan in tol bij SMC smelt is onbekend.

## 1 · Ketenkaart
```
Mimosa-mijn/concentrator `pgm-mimosa-mijn` ──(b1 truck · Zvishavane → Shurugwi → A5 Gweru–Kwekwe–Kadoma–Chegutu → Selous-rotonde → SMC · gemeten ~353 km,
  hemelsbreed 262 km, geen wegkm · aannemelijk: één bron voor de tolsmelt)──► Zimplats SMC `pgm-zimplats-smc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-mimosa-mijn` → `pgm-zimplats-smc` | Zvishavane–Shurugwi-weg → A5 Gweru–Kwekwe–Kadoma–Chegutu → Selous-rotonde → servicewegen SMC; aannemelijk: één bron voor de tolsmelt [1][2] | **hemelsbreed 262 km, geen wegkm**; indicatie som van wegdelen 32 + 121 + 200 = 353 [3][4][5]; OSRM 356,6 (toets); proefmeting 353,1 (−1% t.o.v. som) | maak_stroombeen_weg (extract zimbabwe) | nee |

Geen zee-, spoor-, binnenvaart-, leiding- of luchtbeen; geen fase B/C/D/E. Niet gekozen: Mvuma/Harare-variant (A5 blijft aan de A5; de proef zit 65 km van Mvuma). De ±15%-toets is hier een indicatie: er is geen doorgaande bronopgave voor de rit.

## 3 · Ankers (één per site; beide letterlijk hergebruikt)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-mimosa-mijn` | mijn + concentrator (laadplek) | Mimosa Mine, Zvishavane/Bannockburn — letterlijk uit `pgm-mimosa-springs.md` | -20.3179, 29.8368 | [1][6][9] | bron-gelegd (hergebruikt; eigen z15-blik: kruis op de oostrand van de grote lichte tailingsdam met vijver, mijnwegen en een steenstort noordoost, het hallencomplex ligt ~1,7 km ZW; de weg ligt 0,11 km van het anker) |
| `pgm-zimplats-smc` | smelter (concentrator, boogoven, converter) | Zimplats Selous Metallurgical Complex — letterlijk uit `pgm-ngezi-selous.md` / `pgm-zimplats-springs.md` | -18.0328, 30.4334 | [2][8][10] | bron-gelegd (z15 opnieuw bekeken: kruis op de procesgebouwen met rookpluim, vijfhoekige tailingsdam oost, blauwgroene vijvers, zonnepark west) |

## 4 · Via-punten (landbeen; volgorde van reizen, alle op de doorgaande weg, geen stadscentra)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Zvishavane–Shurugwi-weg, ~14 km NW van Zvishavane | -20.2035, 29.9526 | pint de noordelijke afslag richting Shurugwi i.p.v. de A9 naar Masvingo (snap 0,01 km) |
| b1 | 2 | Shurugwi-noord, ~5 km voorbij het stadje | -19.6224, 29.9609 | houdt de weg naar Gweru aan de oostkant van de Great Dyke (snap 0,00) |
| b1 | 3 | A5 ~21 km ten noorden van Gweru | -19.2641, 29.7885 | pint de A5 naar Kwekwe; sluit de oostelijke omweg via Mvuma/Harare uit (snap 0,00) |
| b1 | 4 | A5 ~10 km ten noorden van Kwekwe | -18.8389, 29.8004 | bevestigt de A5 voorbij Kwekwe (snap 0,00) |
| b1 | 5 | A5 vlak vóór Kadoma | -18.3954, 29.8336 | bevestigt de A5 naar Chegutu (snap 0,00) |
| b1 | 6 | A5 ~5 km oost van Chegutu | -18.1229, 30.1903 | pint de A5 naar de Selous-rotonde (snap 0,00) |
| b1 | 7 | Selous-rotonde (A5, "Halfway") — letterlijk uit `pgm-ngezi-selous.md` | -18.0795, 30.4276 | hier takt de weg naar SMC af; Wikipedia 18°04'46"S 30°25'39"E [5] (snap 0,01) |
Geofabrik-regio: `zimbabwe`. Via-punten 1–6 komen uit de OSRM-controle van de haalbaarheidstoets (indicatie, geen bron), punt 7 uit de Ngezi-brief; alle zeven zijn met een proefrun
op de weg bevestigd (snaps 0,00–0,21 km, 8 deelstukken 46,0 + 75,1 + 49,9 + 50,1 + 50,3 + 49,7 + 26,3 + 5,5 km). Profielwaarden (lon, lat) voor de bak-agent: anker mijn (29.8368, -20.3179) ·
(29.9526, -20.2035) · (29.9609, -19.6224) · (29.7885, -19.2641) · (29.8004, -18.8389) · (29.8336, -18.3954) · (30.1903, -18.1229) · (30.4276, -18.0795) · SMC (30.4334, -18.0328); `refs` leeg,
`vensterKm` 50, `gepubliceerdKm` 375 als indicatie. De A5-stuk Gweru–Chegutu deelt de lijn met `lithium-kamativi-zhangjiagang` b1, maar begin en eind verschillen: geen letterlijke kopie.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Mimosa-concentrator | Mimosa Investments (Sibanye-Stillwater 50% / Implats 50%) | Great Dyke-erts → PGM-concentraat (4E-winning 80,6%); concentraat "primarily by road" naar Implats in Zuid-Afrika, een deel nu in tol bij Zimplats | 117 koz 4E (50%-aandeel) FY2025 | [1][6] |
| SMC (Zimplats) | Zimplats (Implats 87%) | Zimplats-concentraat + tolconcentraat van derden → matte; uitgebreide smelter met tolcapaciteit (tijdens FY2024 begonnen, hoger zwavelgehalte in derdenconcentraat FY2026) | 646 koz 6E in matte FY2024 (heel Zimplats), derdenaandeel niet gepubliceerd | [2][8][10] |

## 6 · Stoppunt
Bij de SMC-poort: Sibanye zegt dat Mimosa een lokale tolsmelt heeft "to produce PGM-enriched matte for export", maar geen bron noemt de bestemming van die matte; de brief tekent daarom geen fase D/E.

## 7 · Open punten
- **Één bron voor de tolsmelt:** het 20-F FY2025 [1] zegt dat Mimosa "has begun toll processing some of its concentrates at the Zimplats smelter" en een lokaal tolsmeltcontract heeft voor export-matte; Zimplats FY2026 [2] noemt tolsmelting van derdenconcentraat zonder naam. Aandeel en startdatum onbekend: kan een dunne stroom zijn (beennaam: aannemelijk, één bron).
- **Volume:** 7,3 t 4E/j is de bovengrens (2 × Sibanye-aandeel); wat bij SMC smelt is niet gepubliceerd.
- **Bestemming van de matte** (Springs of elders) ongebrond: niet getekend.
- **Modaliteit:** het 20-F zegt "transported by road" voor het concentraat naar Zuid-Afrika; voor het stuk naar Selous noemt geen bron truck of spoor (er is een spoorlijn Zvishavane–Gweru). Truck is een aanname uit de bestaande Zimbabwaanse PGM-brieven.
- **Km:** geen doorgaande wegkm-bron; de som 32 (mijn–Zvishavane, `pgm-mimosa-springs`) + 121 [3] + 200 (Gweru–Harare 275 [4] min Selous–Harare 75 [5]) is een samengestelde indicatie.
- **Mijn-anker:** het hergebruikte punt ligt op de rand van de tailingsdam, het hallencomplex ~1,7 km ZW; centraal te beoordelen (ook voor `pgm-mimosa-springs`), niet door mij gewijzigd.
- **Exportheffing** (3% concentraat, 2,5% matte) kan de route wijzigen [1]; actueel tarief bij Zimplats niet nagelopen; equityaxis [7] niet zelf gelezen.

## 8 · Bronnen
[1] Sibanye-Stillwater, Form 20-F FY2025 (Mimosa: toll processing at Zimplats smelter; local toll smelting for PGM-enriched matte; 2,5% matte-heffing; Mimosa 117 koz 4E 2025, 123 koz 2024), https://www.sec.gov/Archives/edgar/data/0001786909/000162828026026991/sbsw-20251231.htm
[2] Zimplats Holdings, Appendix 4E FY2026 (third-party toll-smelted concentrates; SO2 +35%), https://announcements.asx.com.au/asxpdf/20260828/pdf/073cg0z4l6mxdx.pdf
[3] Wikipedia, "Zvishavane" (Gweru 121 km noord), https://en.wikipedia.org/wiki/Zvishavane
[4] Wikipedia, "Gweru" (275 km van Harare), https://en.wikipedia.org/wiki/Gweru
[5] Wikipedia, "A5 road (Zimbabwe)" (Harare–Bulawayo 439 km; Selous-rotonde 75 km ZW van Harare, 18°04'46"S 30°25'39"E), https://en.wikipedia.org/wiki/A5_road_(Zimbabwe)
[6] Wikipedia, "Mimosa mine" (50:50 JV; concentraat per weg naar Implats), https://en.wikipedia.org/wiki/Mimosa_mine
[7] Equity Axis, "PGM sector shifts toward higher value beneficiation in 2025" (via de toets; niet zelf geopend), https://equityaxis.net/post/18761/2026/2/pgm-sector-shifts-toward-higher-value-beneficiation-in-2025
[8] Mining Weekly, "Implats commissions 35 MW solar project, expanded smelter at Zimplats" (uitgebreide smelter met tolcapaciteit; alleen via zoekresultaat, pagina gaf 403), https://www.miningweekly.com/article/implats-commissions-35-mw-solar-project-expanded-smelter-at-zimplats-2024-10-30
[9] `v2/design/routebrieven/pgm-mimosa-springs.md` (anker `pgm-mimosa-mijn`)
[10] `v2/design/routebrieven/pgm-ngezi-selous.md`, `pgm-zimplats-springs.md` (anker SMC, Selous-rotonde)
[11] `v2/design/routebrieven/lithium-kamativi-zhangjiagang.md` (A5-overlap), `v2/design/pgm-sitelaag.json` (`w-mimosa`)
[12] Esri World Imagery: `v2/build-cache/satcheck/sat-pgm-mimosa-selous-mijn.png`, `…-smc.png` (z15); wegproef: `v2/build-cache/ais/graaf/pgm-mimosa-selous-weg-mimosa-smc.geojson` (353,1 km, 2.827 punten, vervangbaar door de bak-agent)

## 9 · Gebakken
**Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)** — `v2/data/stroomroute-pgm-mimosa-selous.json`, 58,5 KB, contract versie 2, lonlat.

| been | modaliteit | km gemeten | km brief | stippel |
|---|---|---|---|---|
| b1 | truck | 353,1 (2.827 punten; wegscan 352,8) | indicatie 353 (som 32 + 121 + 200); hemelsbreed 262, geen wegkm; OSRM 356,6 | nee |

Totaal 353,1 km, één been, geen naden (enig been), 2 markers (`pgm-mimosa-mijn`, `pgm-zimplats-smc`), beide 0,0 km van de lijn (anker = lijnuiteinde).
**Recept:** profiel `pgm-mimosa-selous-mimosa-smc` in `maak_stroombeen_weg.py` (extract zimbabwe, refs leeg, vensterKm 50, `gepubliceerdKm` 375 als indicatie, 9 punten:
anker, 7 via-punten uit §4, anker); `python v2/tools/wegscan_puur.py --profiel pgm-mimosa-selous-mimosa-smc` → `pgm-mimosa-selous-weg-mimosa-smc.geojson`
(8 deelstukken 46,0 + 75,1 + 49,9 + 50,1 + 50,3 + 49,7 + 26,3 + 5,5 km; snaps 0,00–0,21 km; 4 keerlussen gesnoeid zonder lengteverlies); functie `bak_pgm_mimosa_selous` met één
`--been-geojson "truck|…"` en twee markers; `bash v2/tools/bak_stromen.sh pgm-mimosa-selous`.
**Toelichting:** geen stippel, geen haven-aanloop, geen kopie, geen vlucht, geen leiding. Het eerste stuk (19,9 km) en het laatste stuk (5,4 km) lopen over kleine klassen
(residential/service/unclassified): de mijn- en smelterwegen. De lengtetoets (−0,1% op de som 353) is een indicatie, geen norm: er bestaat geen doorgaande wegkm-bron.
Toetsen: `toets_knikken` 9 knikken ≥ 60° (alle korte spikes van 5–88 m op kruisingen/rotondes, 0 omkeringen, 0 terugloop); `toets_rechte_benen` meldt dit been niet.
**Bevindingen / lessen:** (1) het mijn-anker ligt op de rand van de tailingsdam (hallen 1,7 km ZW), centraal beoordelen samen met `pgm-mimosa-springs`;
(2) truck naar Selous is een aanname uit de bestaande Zimbabwaanse PGM-brieven (20-F noemt alleen road naar Zuid-Afrika); (3) volume 7,3 t 4E/j is bovengrens,
SMC-aandeel niet gepubliceerd: mogelijk een dunne stroom; (4) geen fase D/E, de bestemming van de matte is niet gebrond; (5) de brief-proef (353,1 km) reproduceerde exact in de bak.
