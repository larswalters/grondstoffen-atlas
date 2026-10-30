# Routebrief (licht) · goud — Fekola-mijn → Bamako (BKO) → OR Tambo (JNB) → Rand Refinery (Mali → Zuid-Afrika)

**stroom-id:** `goud-fekola-randrefinery` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) ·
**status:** gebakken
**Keten in één zin:** doré van de Fekola-mijn (B2Gold, Kéniéba, West-Mali) per truck over de Millennium Highway naar
de vrachtterminal van Bamako-Sénou (BKO), per vrachtvlucht (grootcirkel, aannemelijk) naar de vrachtterminal van OR Tambo
(JNB), en per truck over de R21/N12 naar Rand Refinery in Germiston.
**Welke as van het verhaal:** West-Afrikaanse doré naar de Rand (tweede speler in Mali naast Barrick-Loulo). Fekola Complex
**530.769 oz in 2025 = 16,5 t Au/j** (100%-basis, B2Gold 80%; koz ÷ 32,15) [1]; 2024 392.946 oz = 12,2 t [2]; guidance 2026
410–460 koz = 12,8–14,3 t [1]. Afnemer: "Doré produced is exported to Rand Refining in South Africa" [1][2] (één bron-type, herhaald).

## 1 · Ketenkaart
```
Fekola-verwerkingscomplex `au-fekola-plant`
  ──(b1 truck · 40-50 km onverhard naar Kéniéba, dan Millennium Highway via Kita · 520 gepubliceerd)──►
Bamako-Sénou vrachtterminal (BKO) `au-bamako-vrachtterminal` (hergebruikt uit goud-loulo-ticino)
  ──(b2 lucht · vlucht BKO → JNB, grootcirkel, aannemelijk: geen bron voor de vlucht · 5.814 km)──►
OR Tambo vrachtterminal (JNB) `au-jnb-vracht` (hergebruikt uit goud-mponeng-londen)
  ──(b3 truck · R21/N12 · 25,7 km, letterlijke kopie van goud-kibali-randrefinery b4)──►
Rand Refinery, Germiston `au-randrefinery` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Fekola-plant → Bamako-Sénou vrachtterminal | mijnweg 40 km onverhard → Kéniéba → Millennium Highway via Kita → Bamako | 520 = 480 Bamako-Kéniéba + 40 onverhard [1]; test-OSM 490,9 (−5,6%) | maak_stroombeen_weg (extract mali, eigen profiel) | nee |
| b2 | B | lucht | Bamako (BKO) → OR Tambo (JNB) | vlucht BKO → JNB (grootcirkel; **aannemelijk: geen bron voor de vlucht**) | 5.814 grootcirkel [berekend] | maak_luchtbeen | nee, doorgetrokken |
| b3 | C | truck | OR Tambo-vrachtterminal → Rand Refinery | R21/N12 (aannemelijk: één bron voor de afnemer) | 25,7 [10] | LETTERLIJKE KOPIE van goud-kibali-randrefinery-weg-jnb-randrefinery.geojson | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-fekola-plant` | mijn / laadplek | Fekola-verwerkingscomplex (B2Gold) | 12.5331, -11.3575 | [5] | bron-gelegd (z15 gezien: verwerkingscomplex met hallen, molen en leidingwerk, ten Z van een groen TSF-bekken, pit W, zonneparken ZO en O; OSM-punt van de Fekola-centrale 12.5330732, -11.3574792 ligt op dit terrein) |
| `au-bamako-vrachtterminal` | overslag truck→lucht | Bamako-Sénou (BKO), vrachtterminal | 12.5353, -7.9488 | [8][6] | hergebruikt letterlijk uit goud-loulo-ticino.md; **onzeker op pandniveau**: op z15 ligt het punt op de zuidwestelijke baan, apron en terminalgebouwen liggen N van de baan (zie §7) |
| `au-jnb-vracht` | overslag lucht→truck | OR Tambo vrachtterminal | -26.1440, 28.2295 | [9] | hergebruikt letterlijk uit goud-mponeng-londen.md (bron-gelegd z16, vrachtloodsen en widebodies) |
| `au-randrefinery` | raffinaderij / stoppunt | Rand Refinery, Germiston | -26.2189, 28.1550 | [7][9] | hergebruikt letterlijk uit goud-mponeng-londen.md; Wikipedia noemt 26,22 S / 28,155 O |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Fekola-plant (anker) | 12.5331, -11.3575 | start op het complex, niet op de pit-haulroads W |
| b1 | 2 | Kéniéba (OSM-knoop; de hoofdweg ligt 0,8 km ernaast) | 12.8407, -11.2322 | de mijnweg komt hier op de Millennium Highway; sluit Dakar-route en Kayes-omweg uit (50,1 km plant-Kéniéba, getest) |
| b1 | 3 | Kita (corridorknoop) | 13.0408, -9.4890 | de corridor buigt hier oostwaarts naar Bamako |
| b1 | 4 | BKO-anker | 12.5353, -7.9488 | eind: laatste 0,3 km via service-wegen binnen het terrein, zoals goud-loulo-ticino b1 |
| b3 | — | geen: kopie draagt de via-punten van goud-mponeng-londen b2 | — | niet opnieuw routeren |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Fekola Complex | B2Gold 80% / staat Mali 20% | erts → doré | 530.769 oz Au in 2025 (16,5 t) | [1] |
| Rand Refinery (Germiston) | Rand Refinery (Pty) Ltd | doré → LBMA-baren | capaciteit niet gebrond | [7] |

## 6 · Stoppunt
Rand Refinery: de bron (B2Gold-AIF) zegt alleen "exported to Rand Refining" en stopt daar; de verdere afzet van de baren is
niet gebrond. Fase D vervalt, E vervalt.

## 7 · Open punten
- **Geen bron voor de vlucht BKO → JNB of voor BKO als overslag.** De AIF noemt alleen de export naar Rand Refining; twee zoekacties
  (toets en deze brief) vonden geen doré-vervoer per lucht. De mijn heeft een eigen gravel-airstrip met "regularly scheduled flights from Bamako
  to the mine site" [1]: een vlucht rechtstreeks vanaf de mijn is even denkbaar. Gekozen volgens de toets: truck naar BKO, vlucht BKO → JNB,
  beide "aannemelijk". De mijnairstrip is niet getekend (geen coördinaat gebrond).
- **BKO-anker ligt op de baan.** Op z15 valt het hergebruikte punt 12.5353, -7.9488 op de baanrichting 06/24 [6]; de apron met toestellen en
  de terminalgebouwen liggen N van de baan (~12.5405-12.5415, -7.9455 tot -7.9505) en hangars W (~12.5395, -7.9565). Niet verplaatst (letterlijk
  hergebruik, gedeeld met goud-loulo-ticino); in goud-loulo-ticino b1 loopt de weg via service-wegen langs de apron tot 0,07 km van het anker.
  Welk pand vracht afhandelt blijft onzeker.
- **Kéniéba-via kan een terugloop geven:** de Kita-weg verlaat Kéniéba naar het ZO en de plant ligt ZW van Kéniéba. Bij een omkering in
  `toets_knikken`: via op de hoofdweg projecteren (-11.2267, 12.8459, vertex van goud-loulo-ticino b1) in plaats van de stadsknoop.
- **Wegbeen 88% gelijk aan goud-loulo-ticino b1** (alleen Fekola-Kéniéba is nieuw): bewust geen kopie, eigen profiel via Kéniéba (toets).
- **Kayes-regio onder druk (blokkades 2025):** B2Gold meldde in nov 2025 dat de operatie ongestoord doorloopt [3]; Mali-productie H1 2026 +30%,
  Fekola 8,85 t [4]. Niet verder onderzocht.
- **Russisch-gesteunde goudraffinaderij bij Bamako-Senou in aanbouw** [11]: kan op termijn de export van doré naar Rand beperken; geen datum.
- Volume 16,5 t is een 100%-cijfer; het B2Gold-aandeel is 13,2 t. Plantpunt is het centrale-/complexpunt (site-niveau), geen aparte poort.

## 8 · Bronnen
[1] B2Gold Annual Information Form 2026 (EDGAR, Fekola Complex: 530.769 oz 2025; "Doré produced is exported to Rand Refining in South Africa"; 480 km + 40 km unsealed; gravel airstrip met geregelde vluchten Bamako-mijn; guidance 2026 410.000-460.000 oz; B2Gold 80%): https://www.sec.gov/Archives/edgar/data/1429937/000110465926026310/tm266740d1_ex99-1.htm
[2] B2Gold Annual Information Form 2025 (EDGAR; zelfde Rand-Refining-zin, 392.946 oz in 2024, airstrip): https://www.sec.gov/Archives/edgar/data/1429937/000106299325006466/exhibit99-1.htm
[3] Mining Weekly, 04-11-2025, "B2Gold says Mali operations continue uninterrupted" (alleen via zoekresultaat, pagina 403): https://www.miningweekly.com/article/b2gold-says-mali-operations-continue-uninterrupted-2025-11-04
[4] Engineering News, 18-08-2026, "Mali gold output jumps 30% in first half" (Fekola 8,85 t H1 2026; alleen via zoeksamenvatting, pagina 403): https://www.engineeringnews.co.za/article/mali-gold-output-jumps-30-in-first-half-beating-forecasts-2026-08-18
[5] OpenStreetMap (ODbL) via Nominatim: "Fekola Mine power station" way 1303591053, 12.5330732, -11.3574792: https://www.openstreetmap.org/way/1303591053
[6] Wikipedia, "Bamako-Sénou International Airport" (12°32′16″N 7°56′35″W, baan 06/24, 2.706 m): https://en.wikipedia.org/wiki/Bamako%E2%80%93S%C3%A9nou_International_Airport
[7] Wikipedia, "Rand Refinery" (Germiston, ~26,22 S / 28,155 O): https://en.wikipedia.org/wiki/Rand_Refinery
[8] `v2/design/routebrieven/goud-loulo-ticino.md` (au-bamako-vrachtterminal, via-punten Kéniéba/Kita, b1 479,9 km; geojson `goud-loulo-ticino-weg-loulo-bamako.geojson`).
[9] `v2/design/routebrieven/goud-mponeng-londen.md` §3 (au-jnb-vracht, au-randrefinery, b2 25,7 km).
[10] `v2/design/routebrieven/goud-kibali-randrefinery.md` §2/§9 (b4 = JNB → Rand, 25,717 km; `goud-kibali-randrefinery-weg-jnb-randrefinery.geojson`, 381 punten, begint op 28.2295,-26.144).
[11] Mining Technology / Miningmx, "Mali starts work on Russia-backed gold refinery" (Senou, bij Bamako; alleen via zoekresultaat): https://www.mining-technology.com/news/mali-russia-gold-refinery-bamako
Satellietblik: `v2/build-cache/satcheck/sat-goud-fekola-randrefinery-plant.png`, `sat-goud-fekola-randrefinery-bko.png` (Esri z15, 2026-10-30; Fekola eerder gezien op `sat-gtoets-fekola-plant.png`, z14).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
`v2/data/stroomroute-goud-fekola-randrefinery.json`, 155,0 KB, contract versie 2, lonlat, 3 benen, 4 markers, totaal 6.330,8 km. Alle benen doorgetrokken, geen stippel.

| # | modaliteit | been | km | toets |
|---|---|---|---|---|
| b1 | truck | Fekola-plant → BKO-vrachtterminal (mijnweg, Kéniéba, Millennium Highway via Kita) | 490,9 (7.162 punten) | 520 gepubliceerd (480 + 40 onverhard) = -5,6%, binnen ±15% |
| b2 | lucht | vlucht BKO → JNB (vrachtvlucht, grootcirkel, aannemelijk) | 5.814,2 (234 punten) | berekend 5.814,16; geen km-toets voor lucht |
| b3 | truck | JNB-vrachtterminal → Rand Refinery (letterlijke kopie goud-kibali-randrefinery b4) | 25,7 (381 punten) | 25,7 = bron |

Naden 0,00 km; markers 0,00 km van hun lijn; bestand < 300 KB.

**Recept.** b1: profiel `goud-fekola-randrefinery-plant-bamako` in `maak_stroombeen_weg.py` (extract mali, via plant · Kéniéba · Kita · BKO, `eindToegangPrivaat`, venster 40 km), `python v2/tools/wegscan_puur.py --profiel …` → `goud-fekola-randrefinery-weg-plant-bamako.geojson`. b2: `maak_luchtbeen.py` BKO → JNB. b3: `cp` van `goud-kibali-randrefinery-weg-jnb-randrefinery.geojson` naar `goud-fekola-randrefinery-weg-jnb-randrefinery.geojson`. Functie `bak_goud_fekola_randrefinery()` in `bak_stromen.sh`.

**Toelichting per been**
- **Geen stippel, geen haven-aanloop, geen leiding.** Het wegbeen eindigt 0,07 km van het BKO-anker (precedent goud-loulo-ticino), dus geen airside-stippel nodig.
- **Vlucht.** Aannemelijk: geen bron noemt de vlucht of BKO als overslag; staat in de beennaam, de lijn is doorgetrokken. BKO-anker ligt op de baan (pand onzeker, niet verschoven).
- **Kopie.** b3 is byte-gelijk aan b4 van de Kibali-stroom (begint 28.2295,-26.144, eindigt 28.155,-26.2189).

**Bevindingen**
- ⚠ **Terugloop bij Kéniéba (toets_knikken):** de route gaat via een Y-knoop ten N van de stad (12.8639, -11.2336, 159°, boogstraal 14 m) en keert terug door Kéniéba; ongeveer 4,4 km extra. Het via-punt is eerst van de stadsknoop (-11.2322, 12.8407) naar de hoofdweg (-11.2267, 12.8459) geprojecteerd, zoals de brief voorschreef; de geometrie bleef identiek, dus het is de OSM-topologie (de enige verbinding), niet het via-punt. Niet verder bijgeschoven.
- Overige knikken in b1 zijn spikes < 100 m bij erf- en servicewegen rond BKO en de plant (geen terugloop); in b3 twee echte scherpe bochten (kopie van Kibali).
- b1 is voor 88% gelijk aan goud-loulo-ticino b1 (alleen Fekola-Kéniéba, 50,1 km, is nieuw); bewust geen kopie.

**Lessen**
- Een via-punt op een stadsknoop kan een terugloop geven; projecteren op de hoofdweg lost het niet op als de OSM-verbinding zelf een Y-knoop buiten de stad is.
- Tijdens de tweede bake meldde `bak_stromen.sh` eenmalig een regel-fout in andermans functie (gelijktijdige edit, daarna weer in orde); mijn functie bakte correct.
- Register en bundel zijn niet gedraaid (centraal).
