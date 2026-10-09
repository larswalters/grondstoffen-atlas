# Routebrief (licht) · gas — Temane (Mozambique) → Ressano Garcia/Komatipoort → Secunda (leidingeinde ROMPCO, Zuid-Afrika)

**stroom-id:** `gas-temane-secunda` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Pijpgas uit de Pande- en Temane-velden gaat via de centrale gasverwerking (CPF) bij Temane in de 865 km lange
Mozambique–Secunda-leiding (ROMPCO, operator Sasol), kruist de grens bij Ressano Garcia/Komatipoort en eindigt bij het Sasol-terrein in
Secunda (Mpumalanga). Eén doorlopende OSM-leiding, geen zee, geen weg. **Titel noemt het leidingeinde**, niet elk molecuul: Sasol gebruikt
het gas in eigen bedrijf, ROMPCO-gas gaat ook naar Sasolburg en circa 700 derden [1][5].
**Welke as van het verhaal:** de enige grote gasleiding Mozambique → Zuid-Afrika — 212 PJ/j capaciteit na de loop lines (peiljaar 2025) [1],
ruwweg 5,5 bcm/j (eigen omrekening, 38 PJ per bcm) en dus capaciteit, geen gemeten doorzet. Sasol levert extern 42 PJ/j aardgas (± 1,1 bcm/j,
2025) [5]; hoeveel er Secunda zelf in gaat is niet gebrond. Pande/Temane daalt volgens [3] vanaf 2026, volgens [4] na 2028.

## 1 · Ketenkaart
```
Pande/Temane-velden (niet getekend) ──► Temane CPF `gas-temane-cpf`
   ──(b1 leiding · ROMPCO Mozambique–Secunda Pipeline · 858,0 km OSM, 865 gepubliceerd; grens bij Ressano Garcia/Komatipoort)──►
Secunda leidingeinde `gas-secunda-leidingeinde` (NE-hoek Sasol-terrein, Polymers Road) ═══ stoppunt ═══
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-temane-cpf` → `gas-secunda-leidingeinde` | ROMPCO / Mozambique–Secunda Pipeline; Temane → Panda-zone → Ressano Garcia/Komatipoort → Mbombela-zone → Secunda | 865 gepubliceerd [1][2][3] → **858,0 OSM (−0,8%)** | OSM-way 248950177 (man_made=pipeline, operator Sasol, substance=gas, location=underground): 989 punten, één way, omgekeerd tot Temane → Secunda; grootste vertexafstand 7,9 km (rechte stukken, geen gat) | nee |

Gemeten op de lijn (eigen berekening, indicatief): Mozambique ± 522 km, Zuid-Afrika ± 336 km; de lijn passeert de grens op ± 1,5–1,7 km van
Komatipoort en Ressano Garcia. Beennaam voor de bake: *ROMPCO Mozambique-Secunda Pipeline Temane naar Secunda (Mozambique, Zuid-Afrika; OSM-way 248950177)*.
De OSM-lijn volgt de hoofdleiding, niet de loop lines (die liggen parallel: loop 1 CPF–scraper station 1, 128 km; loop 2, 127 km [2]).
Géén last-mile-been (bindende toets): het eindanker is het leidingeinde; de hoofdinstallatie Secunda CTL (Wikipedia 26.5537 S, 29.1658 O) ligt 2,7 km westelijker
en is niet getekend (zie §7).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-temane-cpf` | leiding-kop / gasverwerking | Temane CPF (Sasol), Inhassoro, Inhambane | -21.7479, 35.0583 | [6][8][9] | bron-gelegd (z15 gezien: groot omheind complex met procestreinen, tanks en gebouwen in bos, met sandwegen; het punt ligt op de westrand van het terrein; een tweede installatie ± 2 km NO) |
| `gas-secunda-leidingeinde` | leidingeinde / stoppunt | Secunda, NE-hoek Sasol-terrein (Polymers Road) | -26.5516, 29.1933 | [6][9][10] | bron-gelegd (z15 gezien: rand van een industrieterrein met witte loods en procesinstallaties, dat 0,3 km ten westen van het punt ligt, open veld en mijnstort verder oostelijk; hoofdcomplex met koeltorens ± 2,7 km W) |

Hergebruik: geen — `gas-sitelaag.json` en eerdere brieven kennen Temane/Secunda niet; beide ankers zijn de OSM-uiteinden (0,00 km van de lijn).
Beelden: `v2/build-cache/satcheck/sat-gas-temane-secunda-temane-cpf.png`, `sat-gas-temane-secunda-secunda-eind.png`, `sat-gas-temane-secunda-secunda-ctl.png` (controlebeeld, geen anker) [8].
GEM-veldcoördinaat Pande/Temane (-21.7045, 35.1664) is een veld-centroïde, geen installatie en geen anker.

## 4 · Via-punten
Niet van toepassing: één leidingbeen uit één OSM-way (geen corridorkeuze, geen weg of spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Temane CPF | Sasol (veld: Sasol/ENH/IFC) [11] | veldgas → droog verkoopgas | niet gevonden | [3][11] |
| ROMPCO-leiding | ROMPCO (Sasol, CMG, iGas) [1][2] | CPF → Secunda, verderop Sasolburg en derden | 212 PJ/j (≈ 5,5 bcm/j) [1] | [1][2] |
| Secunda (Sasol) | Sasol | aardgas → eigen bedrijf; 42 PJ/j aardgas extern [5] | verbruik Secunda niet gebrond | [5] |

## 6 · Stoppunt
De brief stopt bij het leidingeinde in Secunda: waar de OSM-leiding het Sasol-terrein bereikt. Wat daarna in het interne gasnet gebeurt (reformers, gasturbines,
doorlevering naar Sasolburg en derden) is geen gedocumenteerde keten van één molecuul. Stroomopwaarts is niet getekend: het veldnet Pande/Temane staat niet in OSM.

## 7 · Open punten
- **Secunda is leidingeinde, niet elk molecuul:** ROMPCO-gas gaat ook naar Sasolburg (Gauteng) en circa 700 klanten [1][5]; de Sasolburg-aftakking staat niet in OSM en is niet getekend.
- **CTL-anker (26.5537 S, 29.1658 O) niet getekend:** de OSM-leiding eindigt 2,7 km oostelijk. In OSM liggen binnen het terrein gasleidingen (o.a. ways 590523662, 590523663,
  `produce=gas`, laag 1/2, zonder substance- of operator-tag) op ≥ 1,8 km van het leidingeinde, niet aangesloten; niet gebruikt als doorgetrokken lijn (bindende toets: geen last mile).
- **Geen kalenderjaar-doorzet:** 212 PJ/j is capaciteit (impliciet, [1]); Sasol-extern 42 PJ/j is een deelcijfer [5]. Secunda-eigen gasverbruik niet gevonden.
- **Aflopende levering:** Sasol zou eind juni 2026 stoppen met gas aan derden; Pande/Temane daalt vanaf 2026 [3], volgens een bericht van juli 2026 pas na 2028 [4]. Wat er in juni 2026 feitelijk gebeurde is niet bevestigd.
- **OSM-way heeft geen name- of ref-tag**, alleen operator Sasol en substance gas; herkomst bronnen `Bing aerial 23-05-18`. Het tweede (NO) complex bij Temane is niet geïdentificeerd.
- **Sitelaag mist Temane en Secunda** — centrale aanvulling nodig voor de gloed (gewicht 212 PJ/j capaciteit, eenheid PJ, niet bcm).

## 8 · Bronnen
[1] World Pipelines, 18-08-2025, "ROMPCO driving regional energy security in Southern Africa" — 865 km, 212 → 400 PJ/j (plan), ~700 gebruikers. https://www.worldpipelines.com/project-news/18082025/rompco-driving-regional-energy-security-in-southern-africa/
[2] Engineering News, 30-11-2015, "$210m Moz-to-SA gas pipeline expansion moves ahead" — CPF Temane → Secunda 865 km, loop lines, eigenaren Sasol/CMG/iGas. https://www.engineeringnews.co.za/article/210m-moz-to-sa-gas-pipeline-expansion-moves-ahead-2015-11-30
[3] Engineering News, 20-09-2024, "Depleting gas reserves threaten future gas security" — 865 km, daling vanaf 2026, derden-stop eind juni 2026, Pande 2004 / Temane 2009. https://www.engineeringnews.co.za/article/depleting-gas-reserves-threaten-future-gas-security-2024-09-20
[4] Wits/Polity, 22-07-2026, "A sharp fall in gas supplies in 2028…" (alleen via zoekresultaat gelezen: daling na 2028). https://www.polity.org.za/article/a-sharp-fall-in-gas-supplies-in-2028-threatens-south-africas-economy-how-to-manage-the-fallout-2026-07-22
[5] Sasol, "Sasol Gas fact sheet" (2025) — ~65 PJ/j totaal, 42 PJ/j aardgas + 23 PJ/j methane-rich gas extern. https://www.sasol.com/sites/default/files/2025-07/Sasol%20Fact%20Sheet%20_%20Sasol%20Gas.pdf
[6] OpenStreetMap-bijdragers (ODbL), api.openstreetmap.org, way 248950177 (989 nodes, v29, 2026-10-09). https://www.openstreetmap.org/way/248950177
[7] Wikipedia (EN), "Secunda CTL" — coördinaat 26.5537 S, 29.1658 O (controle, geen anker). https://en.wikipedia.org/wiki/Secunda_CTL
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15, live, 2026-10-09).
[9] Nominatim reverse (2026-10-09): Temane-eind → Magungumete, Inhassoro, Inhambane; Secunda-eind → Polymers Road, Secunda. https://nominatim.openstreetmap.org
[10] OpenStreetMap-bijdragers, map-bbox 29.14–29.23 / -26.58…-26.52 (2026-10-09): ways 590523662/-63 (gas), power=plant "Sasol Power Station East" 280 MW gas. https://www.openstreetmap.org
[11] Wikipedia (EN), "Sasol" — Mozambique-gas JV Sasol/ENH/IFC. https://en.wikipedia.org/wiki/Sasol

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-gas-temane-secunda.json` (20,8 KB, versie 2, punt_formaat lonlat) · **functie:** `bak_gas_temane_secunda` in `v2/tools/bak_stromen.sh` · **totaal 858,0 km, 1 been, 2 markers.**

| # | modaliteit | km | punten | naad | stippel | toets |
|---|---|---|---|---|---|---|
| b1 | leiding | 858,0 | 989 | n.v.t. (enig been) | nee, doorgetrokken | 865 gepubliceerd, -0,8% (norm ±15%: goed) |

**Recept:** geen wegscan, geen zeerouter, geen profiel, geen extract. Het been is OSM-way 248950177 (man_made=pipeline, operator Sasol, substance=gas) omgekeerd tot Temane naar Secunda en als FeatureCollection weggeschreven in `v2/build-cache/ais/graaf/gas-temane-secunda-leiding-rompco.geojson` (herbouwen kan uit `gas-temane-secunda-way.json`, api.openstreetmap.org way full). Dan `hecht_marnet.py route --been-geojson "leiding|…"` met twee `--marker`; geen stippel, geen haven-aanloop, geen via-punten.
**Markers:** gas-temane-cpf (-21.7479, 35.0583) 0,004 km van de lijn; gas-secunda-leidingeinde (-26.5516, 29.1933) 0,002 km van de lijn.
**Toetsen:** `toets_knikken.py`: 42 knikken >= 60 graden, 0 omkeringen, 0 terugloop (spikes van 50-200 m in de OSM-leiding, bv. -25.45182,31.95977; leidingtekening, geen route-fout). `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom. Geen naad (één been).
**Lessen / bevindingen:** (1) Een eerdere afgebroken poging had de functie en het geojson al compleet; hergebruikt, niet dubbel ingevoegd. (2) De functie staat op één regel met spaties in plaats van backslash-vervolgregels; werkt, puur cosmetisch. (3) Tijdens de run gaf bash eenmalig "ga: command not found" op regel 9423: een gelijktijdige edit van een andere agent aan bak_stromen.sh; daarna `bash -n` ok en 0 CRLF. (4) Open punten uit §7 blijven staan (Sasolburg-aftakking en CTL-anker niet getekend; sitelaag mist Temane en Secunda, centraal).
