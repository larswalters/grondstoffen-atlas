# Routebrief (licht) · PGM — Zimplats SMC → Beitbridge → Impala Springs (Zimbabwe → Zuid-Afrika)

**stroom-id:** `pgm-zimplats-springs` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) ·
**status:** gebakken
**Keten in één zin:** PGM-matte van de Zimplats Selous Metallurgical Complex (Great Dyke, Zimbabwe) per **truck**
over A5/A4 naar de grens **Beitbridge**, en per **truck** over de N1 (Musina–Polokwane–Pretoria–Johannesburg) en
de N12 naar de raffinaderij van **Impala Refining Services (IRS) in Springs** — de bestemming die Implats zelf
noemt (life-of-mine-akkoord); geen luchtbeen, geen zee, geen fase D/E.
**Welke as van het verhaal:** Zimbabwaanse matte die in Zuid-Afrika wordt afgeraffineerd, nu met de bron-
bestemming (Springs) in plaats van het ongebronde Rustenburg van `pgm-zimplats-rustenburg`. Volume: 646.000 oz 6E in
matte (FY2024) = **20,1 t 6E/j** (646.000 ÷ 32,15; mix 6E = Pt+Pd+Rh+Au+Ru+Ir) [1].

## 1 · Ketenkaart
```
Zimplats SMC `pgm-zimplats-smc` ──(b1 truck · A5 Chegutu–Harare → A4 Harare–Masvingo–Beitbridge · hemelsbreed
  468 km, geen wegkm · LETTERLIJKE KOPIE pgm-zimplats-rustenburg b1, gebakken 663 km)──► Beitbridge-grens
  `pgm-beitbridge-grens` ──(b2 truck · N1 Musina–Polokwane–Pretoria–Johannesburg → N12 Germiston–Springs · hemelsbreed
  471 km, geen wegkm; indicatie ~570 km)──► Impala Refining Services Springs `pgm-springs-raffinaderij` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-zimplats-smc` → `pgm-beitbridge-grens` | A5 (Chegutu–Harare) → A4/R1 (Harare–Masvingo–Beitbridge) — LETTERLIJKE KOPIE `pgm-zimplats-rustenburg` b1 | hemelsbreed 468 km, geen wegkm; gebakken 663,0 [6] | kopie geojson | nee |
| b2 | A | truck | `pgm-beitbridge-grens` → `pgm-springs-raffinaderij` | N1 (Musina–Polokwane–Pretoria–Centurion–Johannesburg) → N12 (Germiston–Springs) | hemelsbreed 471 km, geen wegkm; indicatie ~570 = 521 (Beitbridge–Johannesburg) + ~50 (Johannesburg–Springs) [3][4] | maak_stroombeen_weg (nieuw profiel) | nee |

Geen zee-, spoor-, binnenvaart-, leiding- of luchtbeen; geen fase D/E (geen bron noemt een afnemer van het
geraffineerde metaal in déze as — §6). De ±15%-toets is voor b1 én b2 een indicatie, geen norm (geen wegkm-bron).

## 3 · Ankers (één per site en per overslag; alle drie letterlijk hergebruikt)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-zimplats-smc` | smelter/concentrator (matte-productie) | Zimplats Selous Metallurgical Complex, Zimbabwe — uit `pgm-zimplats-rustenburg.md` | -18.0328, 30.4334 | [1][6] | bron-gelegd (z15 opnieuw bekeken: smelter-/procesgebouwen met rookpluim, grote vijfhoekige tailingsdam oost, blauwgroene vijvers, zonnepark west) |
| `pgm-beitbridge-grens` | grensovergang / overslag tussen twee truckcorridors | Beitbridge-grens, Limpopo-brug — uit `pgm-zimplats-rustenburg.md` | -22.2244, 29.9865 | [6][2] | bron-gelegd (zie die brief) |
| `pgm-springs-raffinaderij` | losplek / eindraffinaderij | Impala Refining Services, Springs (Rowhill/East Geduld) — uit `pgm-springs-zurich.md` | -26.2227, 28.4437 | [1][7] | bron-gelegd (z15 opnieuw bekeken: kruis op het complex met productiehallen met blauwe daken, tailingsbekkens en bezinkvijvers; woonwijken zuid en oost) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1–5 | Chegutu · Harare · Beatrice · Chivhu · Masvingo | zie `pgm-zimplats-rustenburg.md` §4 | niet opnieuw gelegd: b1 is een kopie van het gebakken geojson |
| b2 | 1 | Musina — uit `pgm-zimplats-rustenburg.md` | -22.3454, 30.0269 | pint de N1 direct na de grens |
| b2 | 2 | Polokwane (N1) — idem | -23.9218, 29.4803 | sluit binnenwegen door Limpopo uit |
| b2 | 3 | Pretoria, N1/N4-wissel — idem | -25.6357, 28.2761 | houdt de N1 zuidwaarts vast (niet de N4 naar Rustenburg) |
| b2 | 4 | Centurion (N1) — uit `pgm-springs-zurich.md` | -25.8603, 28.1894 | pint de N1 door Pretoria/Centurion naar Johannesburg |
| b2 | 5 | Johannesburg N1/N12-knoop — idem | -26.0380, 28.0980 | hier buigt de corridor van de N1 op de N12 oostwaarts |
| b2 | 6 | Germiston (N12) — idem | -26.2178, 28.1672 | pint de N12 richting Springs |
Bestaande lijn bevestigt dit: op de gebakken geojson's passeert b2 de wissel op 462,2 km (zuidelijk stuk Pretoria–
Springs 121,3 km) — samengesteld ~583,5 km, +2,4% op de indicatie ~570. Geofabrik-regio's: `zimbabwe` (b1), `zuid-afrika` (b1-staart + b2).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Zimplats SMC | Zimplats (87% Implats) | concentraat Ngezi + SMC → matte (boogoven, converter); nieuwe 38 MW-oven H1 FY2025 | 646.000 oz 6E in matte FY2024 (611.000 FY2023) | [1] |
| Impala Refining Services, Springs | Implats | matte → geraffineerd PGM; life-of-mine-akkoord met Zimplats | niet gepubliceerd per site | [1][7] |

## 6 · Stoppunt
Bij Springs: de factsheet noemt IRS als raffinage-eindpunt van de matte; geen bron in deze as noemt een vervolg-
zending van het geraffineerde metaal (het luchtbeen staat bij `pgm-springs-zurich`), dus geen fase D/E.

## 7 · Open punten
- **Modaliteit niet gebrond:** de factsheet zegt "dispatched to Impala's refinery in Springs", niet "per truck"; truck
  is de aanname uit `pgm-zimplats-rustenburg` (Beitbridge-corridor, enige doorgaande wegroute).
- **Km-bron b1/b2:** geen doorgaande wegkm-bron voor Zimplats→Beitbridge (ketenontwerp ~450 is hemelsbreed-achtig,
  gebakken 663). b2 ~570 is een optelling van twee Wikipedia-waarden, geen routelengte.
- **Rustenburg-eindpunt in `pgm-zimplats-rustenburg` heeft geen bron;** of die stroom vervalt beslist de orkestrator.
- **Gedeelde geometrie:** b1 is een kopie en b2 deelt ~462 km met `pgm-zimplats-rustenburg` b2 (andere bestemming).
- **Zimbabwaans exportbeleid** (verbod/heffing op onbewerkte PGM; Zimplats exporteert witte matte) kan dit been
  doen wegvallen; alleen een zoekresultaat [8], niet geopend of gedateerd na 2022.
- **Volume:** 646 koz is productie in matte (FY2024 = jul 2023–jun 2024), niet exact "verscheept naar Springs".

## 8 · Bronnen
[1] Implats, Zimplats Fact Sheet 2025 (PDF; matte naar Springs onder life-of-mine-akkoord met IRS; 646.000 oz 6E FY2024;
SMC 77 km ten noorden van de mijnen), https://implats.co.za/pdf/fact-sheets/2025/fact-sheet-zimplats.pdf
[2] Wikipedia, "Beitbridge" (N1: Pretoria 463 km, Johannesburg 521 km), https://en.wikipedia.org/wiki/Beitbridge
[3] Wikipedia, "Springs, Gauteng" (50 km ten oosten van Johannesburg), https://en.wikipedia.org/wiki/Springs,_Gauteng
[4] Wikipedia, "N12 (South Africa)" (N12/N1 Johannesburg Ring Road), https://en.wikipedia.org/wiki/N12_(South_Africa)
[5] Wikipedia, "A4 road (Zimbabwe)" (A4/R1 Beitbridge–Rutenga–Masvingo–Chivhu–Harare),
https://en.wikipedia.org/wiki/A4_road_(Zimbabwe)
[6] `v2/design/routebrieven/pgm-zimplats-rustenburg.md` (ankers, b1, gebakken 663,0 km; b2 582,1 km)
[7] `v2/design/routebrieven/pgm-springs-zurich.md` (Springs-anker; b1 Rustenburg → Springs 255,8 km, N1/N12-via-punten)
[8] Herald Zimbabwe, "Zimplats to process matte at Selous metal refinery" (zoekresultaat, niet geopend),
https://www.heraldonline.co.zw/zimplats-to-process-matte-at-selous-metal-refinery/
[9] Esri World Imagery z15: `v2/build-cache/satcheck/sat-pgm-zimplats-rustenburg-smc2.png`, `sat-pgm-springs-zurich-springs.png`
[10] `v2/design/pgm-sitelaag.json` (`w-impala-springs` en Springs-anker gelijkgetrokken; `w-zimplats-ngezi` mijn niet gebruikt)

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)

**Stroom `pgm-zimplats-springs`** → `v2/data/stroomroute-pgm-zimplats-springs.json` — 2 benen (beide truck, fase A →
stoppunt), **1.246,6 km**, 10.353 punten, 3 markers, 211,2 KB. Recept: `bak_stromen.sh` (functie
`bak_pgm_zimplats_springs`); één nieuw wegprofiel `pgm-zimplats-springs-beitbridge-springs` in `maak_stroombeen_weg.py`.
Geen zee, spoor, binnenvaart, leiding, lucht, haven-aanloop of stippel: twee doorgetrokken truckbenen, naden 0,0 km.

| been | modaliteit | km (gemeten) | brief | geometrie |
|---|---|---|---|---|
| b1 Zimplats SMC → Beitbridge | truck | 663,2 | hemelsbreed 468, geen wegkm; gebakken kopie 663,0 | LETTERLIJKE KOPIE `pgm-zimplats-rustenburg-weg-smc-beitbridge.geojson` (bestand `pgm-zimplats-springs-weg-smc-beitbridge-gedeeld.geojson`, byte-gelijk) |
| b2 Beitbridge → Springs | truck | 583,4 | hemelsbreed 471, geen wegkm; indicatie ~570 | nieuw wegprofiel, `wegscan_puur.py` (extract `zuid-afrika`) |

**Markers (3, alle op de lijn, 0,0 km):** `pgm-zimplats-smc` (-18.0328, 30.4334), `pgm-beitbridge-grens` (-22.2244, 29.9865),
`pgm-springs-raffinaderij` (-26.2227, 28.4437); alle drie letterlijk hergebruikt (bron-gelegd).

**b1:** geen scan; letterlijke kopie van het geojson van `pgm-zimplats-rustenburg` b1 (663,0 km geroute, 663,2 km getekend).
**b2:** 583,3 km geroute (getekend 583,4) over de zes via-punten uit §4 (Musina, Polokwane, Pretoria-wissel, Centurion,
Johannesburg N1/N12, Germiston); snaps 0,00-0,71 km, 23 keerlussen gesnoeid (587,0 → 583,3 km). Lengtetoets tegen de
indicatie ~570 = +2,3% (indicatie, geen norm: geen wegkm-bron; de brief verwachtte ~583 uit de bestaande lijnen en dat
komt uit). Last mile 0,31 km (service/unclassified).

**Toetsen:** geen naad > 5 km (0,0 km); langste segment 4,8 km; `toets_knikken.py`: 29 knikken >= 60 gr, 0 terugloop
(alleen ankerspikes en op/afritten rond Johannesburg/Springs); `toets_rechte_benen.py --min-km 5`: geen treffer voor deze
stroom; json: versie 2, punt_formaat lonlat, modaliteiten {truck}, elk been >= 2 punten.

**Toelichting:** geen stippel, geen aanloop, geen vlucht, geen leiding. De b1/b2-kilometers zijn gemeten weggeometrie, geen
gepubliceerde wegkm; "aannemelijk: één bron" geldt voor de modaliteit (truck is aanname uit `pgm-zimplats-rustenburg`,
de factsheet zegt alleen dispatched naar Springs).

**Lessen / bevindingen:** (1) b1 en ~462 km van b2 zijn gedeeld met `pgm-zimplats-rustenburg`; het Rustenburg-eindpunt van
die stroom heeft geen bron, centraal beslissen of die vervalt. (2) Zimbabwaans exportbeleid voor onbewerkte PGM kan het
been doen wegvallen (alleen zoekresultaat). (3) Een wegscan op `zuid-afrika` duurt ~3,5 min (pure-Python pbf-lezer).
