# Routebrief (licht) · olie — Sangachal Terminal (Azerbeidzjan) → Ceyhan-exportterminal (Turkije)

**stroom-id:** `olie-sangachal-ceyhan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** Azerbeidzjaanse (en Kazachse/Turkmeense) Azeri-Chirag-Guneshli-ruwe olie vanaf het
Sangachal-verzamelterminal aan de Kaspische Zee, per **leiding** — de Baku-Tbilisi-Ceyhan (BTC)-hoofdleiding, via
Tbilisi (Georgië) en de Erzurum-regio (Turkije) — rechtstreeks naar de Ceyhan-exportterminal aan de Middellandse Zee.
**Welke as van het verhaal:** *de Kaukasus/Bosporus-bypass* — het enige fysieke Hormuz-analoge bypass-verhaal
(naast Habshan-Fujairah) dat nog niet op de bol stond: 1.768 km leiding omzeilt zowel de Straat van Hormuz als de
Bosporus/Dardanellen (die laatste eliminatie is expliciet genoemd bron [2]: 350 tankervaarten/jaar minder). Sinds
1 juli 2026 beheert SOCAR Midstream Operations (SMO) de Azerbeidzjaanse en Georgische secties, BOTAŞ International
Limited (BIL) de Turkse sectie — een recente operatorswissel van BP naar de regionale staatsbedrijven [2][4].

## 1 · Ketenkaart
```
Sangachal Terminal `ol-sangachal-kop` ──(b1 leiding · Baku-Tbilisi-Ceyhan (BTC) hoofdleiding,
    via Tbilisi/Gardabani (Georgië) en de Erzurum-regio (Turkije) · 1.768 km gepubliceerd,
    eigen OSM-som 1.741,3 km · doorgetrokken)──►
   Ceyhan-exportterminal `ol-ceyhan-term` (Haydar Aliyev Terminal, Middellandse Zee) ── stoppunt
   (haven-aanloop over water naar de MARNET-zeeknoop, zie §9)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Sangachal Terminal → Ceyhan-exportterminal | Baku-Tbilisi-Ceyhan (BTC) hoofdleiding, via Tbilisi/Gardabani (Georgië) en Erzurum-regio (Turkije) | 1.768 [2][4] (443 AZ + 249 GE + 1.076 TR); eigen OSM-som 1.741,3 km over 67 ways = **−1,5%** [6] | OSM-way's (`man_made=pipeline`, `substance=oil`, naam ~ "Bakı-Tbilisi-Ceyhan"/"ბაქო-თბილისი-ჯეიჰანის"/"Bakü-Tiflis-Ceyhan", operator BTC Co/BOTAŞ) — pyosmium-scan op drie lokale extracts, **doorlopend gekarteerd** (zie §9) | nee — vrijwel volledige OSM-dekking bevestigd vóór het bakken (dit was het bindende risico uit de haalbaarheidstoets, nu weerlegd) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-sangachal-kop` | kop van de leiding / verzamelterminal (ACG-olie + Kazachse/Turkmeense aanvoer) | Sangachal Terminal (Azerbeidzjan) | 40.2013, 49.4813 | [3][6] | bron-gelegd (z15 gezien: groot industrieel complex met tankparken, procesinstallaties en pijpleidingracks, 45 km zuid van Baku aan de Kaspische kust — exact zoals de bron beschrijft; de eerste OSM-pijplijnsegmentgrens ligt ~4,9 km verderop bij een kruispunt van weg/spoor/pijpleidingcorridor, zie §7) |
| `ol-ceyhan-term` | overslag leiding → zee (exportterminal, BTC-terminus) | Ceyhan-exportterminal (Haydar Aliyev Terminal, BTC) — **hergebruikt anker** `w-ceyhan-btc`, ongewijzigd uit `v2/design/olie-sitelaag.md`/`.json` | 36.8500, 35.9333 | [10] | bron-gelegd (overgenomen; niet opnieuw gelegd — status in de sitelaag zelf al "onzeker", geen satellietblik die ronde; zie §7 voor een eigen OSM-bevinding over dit punt) |

## 4 · Via-punten (alleen b1 — OSM-waysegmentgrenzen langs de leiding, geen alternatieve corridor)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | eerste OSM-waysegmentgrens | 40.1774, 49.4326 | pijplijn verlaat het Sangachal-terminalcomplex, corridor buigt naar het binnenland [6] |
| b1 | 2 | AZ/GE-grensregio | 41.4128, 45.1726 | laatste gedeelde waysegmentgrens vóór Georgië [6] |
| b1 | 3 | Gardabani-pompstationregio | 41.5838, 45.0847 | nabij het Georgische pompstation bij Gardabani (41,4608/45,0894 [8]), ingehuldigd 12-10-2005 [2] |
| b1 | 4 | GE/TR-grensregio | 41.4569, 42.7173 | laatste gedeelde waysegmentgrens vóór Turkije [6] |
| b1 | 5 | Erzurum-regio | 39.9670, 41.4176 | corridor loopt hier ~10 km noordwestelijk van Erzurum (39,9086/41,2769 [9]), parallel aan de South Caucasus Gas Pipeline [2] |
| b1 | 6 | nadering Ceyhan-kust | 37.4603, 36.3374 | laatste grote segmentgrens vóór het BOTAŞ-slotstuk naar het terminalcomplex [6] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ceyhan-exportterminal (Haydar Aliyev Terminal) | BTC Co (consortium, beheer BOTAŞ International Ltd sinds 01-07-2026) | pijplijn-Murban/ACG-ruwe olie → tankopslag → VLCC/Suezmax-lading | nameplate 1,2 mln vpd sinds 2009; 2025 daadwerkelijk **207 mln vaten (~27 Mt, 283 tankerladingen) geladen** (≈567 kb/d gemiddeld) [5]; cumulatief sinds 2006 ~632 Mt / 4,75 mrd vaten tot 30-06-2026 [4] | [2][4][5] |

## 6 · Stoppunt
De brief stopt bij de Ceyhan-exportterminal: BTC-ruwe olie wordt breed verkocht op de Middellandse Zee-markt en
geen bron koppelt één specifieke lading aan één eindbestemming/raffinaderij — zelfde stoppunt-logica als
olie-tengiz-novorossiysk en olie-corpuschristi-rotterdam.

## 7 · Open punten
- **Coördinaat-bevinding, niet gewijzigd (mag alleen gerapporteerd worden):** het hergebruikte anker
  `ol-ceyhan-term`/`w-ceyhan-btc` (36,8500/35,9333) ligt **6,0–6,1 km** van het dichtstbijzijnde punt waar de eigen
  OSM-scan het BTC-pijpleiding-eind + een dicht cluster BOTAŞ-eigen interne terminalleidingen vindt
  (~36,89–36,91/35,91–35,93) — de sitelaag noemt dit punt zelf al "onzeker, geen satellietblik deze ronde". Dit is
  een bevinding voor een latere ankercheck-ronde op de sitelaag, geen wijziging in deze brief (werkregel: andermans
  bestanden niet aanraken, fout melden).
- **Sangachal-kop ligt ~4,9 km van het dichtstbijzijnde OSM-pijplijnsegment** — de terminal zelf is een groot
  complex (satellietbeeld toont meerdere km aan tankparken); de eerste gekarteerde way begint aan de rand van het
  bredere terminal-/corridorgebied, niet exact op het satelliet-gelegde middelpunt.
- **De 67 unieke OSM-ways zijn nog niet end-to-end op knoop-niveau gestikt tot één LineString** — de eigen scan
  bevestigt naam/substance/lengte (67 ways, 1.741,3 km, −1,5% t.o.v. 1.768 km gepubliceerd) en een vrijwel
  monotone lat/lon-voortgang AZ→GE→TR, maar niet elke naad tussen opeenvolgende ways is met een exacte
  coördinaat-match geverifieerd (zie §9 voor het gedetailleerde stiklint per land). Bij het bakken kan dit een klein
  aantal korte stippel-stukjes opleveren; geen reden om de as als stippel te behandelen.
- **Baku-Supsa-pijpleiding bewust uitgesloten** (de haalbaarheidstoets waarschuwde hiervoor): de scan filterde
  expliciet op de naamreeks "supsa"/"სუფსა" en trof 0 matches — geen vervuiling van de Baku-Supsa-lijn in de
  BTC-selectie.
- **Geen cargo-specifieke eindbestemming** — zie §6.
- **Jaarvolume-eenheid:** kb/d (duizend vaten per dag) als brongegeven; zie volume-notitie hieronder.

*Volume-notitie:* nameplate-capaciteit 1,2 mln vpd (sinds 2009, met drag-reducing agents); in 2025 daadwerkelijk
207 mln vaten bij Ceyhan geladen (~27 Mt, 283 tankerladingen) ≈ **~567 kb/d gemiddeld** [5]; bij ~7,3 vaten/ton voor
lichte Azeri-ruwe olie komt 27 Mt overeen met de 207 mln vaten (interne consistentiecheck geslaagd).

## 8 · Bronnen
[1] BP, "Baku-Tbilisi-Ceyhan pipeline" (operationele overzichtspagina, genoemd in het ketenontwerp; deze ronde niet
vers opgehaald — server gaf HTTP 403 op geautomatiseerde toegang). https://www.bp.com/en_az/azerbaijan/home/who-we-are/operationsprojects/pipelines/btc.html
[2] Wikipedia, "Baku–Tbilisi–Ceyhan pipeline" — lengte 1.768 km (443 AZ/249 GE/1.076 TR), operationeel sinds
28-05-2006, diameter 1.070→865 mm, 8 pompstations (2/2/4), operatorswissel BP→SOCAR (SMO) 01-07-2026, parallel aan
South Caucasus Gas Pipeline naar Erzurum, organische-chloride-incident juli 2025 (~200.000 t geraakt), 350
tankervaarten/jaar minder door Bosporus/Dardanellen. https://en.wikipedia.org/wiki/Baku%E2%80%93Tbilisi%E2%80%93Ceyhan_pipeline
[3] Wikipedia, "Sangachal Terminal" — 40,201262/49,481270, industrieel gas-/olieverwerkingscomplex, 45 km zuid van
Baku aan de Kaspische kust (woordelijk gelijk aan het ketenontwerp). https://en.wikipedia.org/wiki/Sangachal_Terminal
[4] SOCAR Midstream, "Baku-Tbilisi-Ceyhan" infrastructuurpagina — lengte per land (443/249/1.076 km), capaciteit
1,2 mln vpd, cumulatief geëxporteerd ~632 Mt (4,75 mrd vaten) tot 30-06-2026, operator SMO (AZ/GE) + BOTAŞ
International Limited (TR). https://socarmidstream.az/infrastruktur/baku-tbilisi-ceyhan/
[5] WebSearch-samenvatting (2026-09-28), o.a. Report.az — 2025-jaarcijfer 207 mln vaten (27 Mt) BTC-ruwe olie
geladen bij Ceyhan op 283 tankers; los bevestigd voor jan-aug 2025 met 127,9 mln vaten via Türkiye (Report.az).
https://report.az/en/energy/btc-pipeline-transports-127-9-million-barrels-of-oil-through-turkiye-in-january-august
[6] OpenStreetMap (ODbL) — eigen pyosmium-scan (2026-09-28) op de lokale Geofabrik-extracts `azerbeidzjan`,
`georgie`, `turkije`: filter `man_made=pipeline` + `substance=oil` + naam ~ btc/baku/bakı/tbilisi/tiflis/ceyhan
(Baku-Supsa expliciet uitgesloten op "supsa"/"სუფსა") — 3/35/52 matches per extract, **67 unieke ways na dedup van
grensoverschrijdende dubbels, 1.741,3 km totaal**, alle getagd `operator=BTC Co` of `operator=BOTAŞ`. Sangachal-
omgeving apart doorzocht op alle `man_made=pipeline`-ways binnen een bbox (geen naamfilter) — dichtstbijzijnde
naamloze `substance=oil`-ways lopen noordwaarts (vermoedelijk een andere export-lijn, niet meegenomen); Ceyhan-
omgeving apart doorzocht — bevestigt een dicht cluster BOTAŞ-eigen interne terminalleidingen rond 36,89–36,91/
35,91–35,93, zie §7. https://www.openstreetmap.org
[7] GEM.wiki, "Baku–Tbilisi–Ceyhan Pipeline" (achtergrond, genoemd in het ketenontwerp, deze ronde niet apart
opgehaald). https://www.gem.wiki/Baku%E2%80%93Tbilisi%E2%80%93Ceyhan_Pipeline
[8] Wikipedia, "Gardabani" — 41,46083/45,08944, Georgische stad nabij het GE-pompstation van de BTC-leiding.
https://en.wikipedia.org/wiki/Gardabani
[9] Wikipedia, "Erzurum" — 39,90861/41,27694, referentiepunt voor via-punt b1-5. https://en.wikipedia.org/wiki/Erzurum
[10] `v2/design/olie-sitelaag.json`/`.md` — anker `w-ceyhan-btc` (36,8500/35,9333), status "onzeker", letterlijk
hergebruikt, niet gewijzigd.
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15) —
`v2/build-cache/satcheck/sat-olie-sangachal-ceyhan-sangachal.png`,
`sat-olie-sangachal-ceyhan-pijpkop.png` (eerste OSM-waysegmentgrens, verificatiebeeld).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Benen (4, contract versie 2):**
| # | modaliteit | km | punten | stippel? | naam |
|---|---|---|---|---|---|
| 1 | leiding | 4,9 | 2 | ja | Sangachal Terminal → BTC-hoofdleiding (last mile, geen OSM-way op het terminalterrein) |
| 2 | leiding | 1.741,1 | 2.911 | nee | Baku-Tbilisi-Ceyhan (BTC) hoofdleiding, via Tbilisi/Gardabani (Georgië) en de Erzurum-regio (Turkije) |
| 3 | leiding | 6,1 | 2 | ja | BTC-hoofdleiding → Ceyhan-exportterminal (last mile, geen OSM-way op het terminalterrein) |
| 4 | zee | 7,7 | 2 | ja | haven-aanloop Ceyhan-exportterminal → MARNET-zeeknoop 3786 (LAR-586) |
| — | **totaal** | **1.759,8** | **2.917** | | 2 markers |

**Markers (2, §3):** `ol-sangachal-kop` (40,2013/49,4813) · `ol-ceyhan-term` (36,8500/35,9333) — beide exact op hun
been-uiteinde, 0 m naad.

**Recept:** `bash v2/tools/bak_stromen.sh olie-sangachal-ceyhan` → functie `bak_olie_sangachal_ceyhan()` in
`v2/tools/bak_stromen.sh`. De leiding-geometrie (been 2) komt uit een nieuw eigen script
`v2/tools/maak_leidingbeen_olie_sangachal_ceyhan.py` (pyosmium-scan op de drie lokale extracts
azerbeidzjan/georgie/turkije, `man_made=pipeline`+`substance=oil`+naamfilter, component-graaf over de
extractgrenzen heen — grensoverschrijdende OSM-ways staan in beide buurextracts met dezelfde node-refs, dus
samenvoegen op node-id stikt de grens vanzelf) → geschreven naar
`v2/build-cache/ais/graaf/olie-sangachal-ceyhan-leiding-btc.geojson`.

**Toelichting per stippel/aanloop:**
- **Been 1 (4,9 km) en been 3 (6,1 km)** — beide anker-terreinen (Sangachal-tankparkcomplex,
  Ceyhan-terminalcluster) zijn groter dan de precisie waarmee de OSM-pijplijnkartering het net begint/eindigt;
  gemeten, niet geraden, en exact zoals de brief §3 al aankondigde (~4,9 en ~6,0–6,1 km).
- **Been 4 (haven-aanloop, 7,7 km)** — Ceyhan-anker ligt 7,7 km van MARNET-zeeknoop 3786 (36,89130/36,00220,
  gemeten met `hecht_marnet.py`'s eigen zeeknoop-snippet uit de bakhandleiding §2) — boven de 5 km-norm (LAR-586),
  dus een haven-aanloop óók al snapt de router zelf ruim binnen de 25 km. `maak_havenaanloop.py --naam
  olie-sangachal-ceyhan-ceyhan --van 36.8500,35.9333 --naar 36.89130,36.00220` liep vast op `timeout 300`
  (exit 124) → geen tweede poging, rechte stippel (bakhandleiding §2, exact de regel).
- **Been 2 (BTC-hoofdleiding, 1.741,1 km, doorgetrokken)** — geen enkele stippel-naad nodig: de eigen
  pyosmium-scan (86 matchende ways over drie extracts, 3.774 vertices) stikte in één keer tot ÉÉN aaneengesloten
  component van 2.911 vertices die zowel Sangachal (4,9 km) als Ceyhan (6,1 km) samen het dichtst benadert — de
  brief hield rekening met 0-3 korte stippelstukjes op ongestikte naden tussen opeenvolgende ways; dat bleek niet
  nodig, want het component-graaf-mechanisme (gedeelde OSM-node-refs, geen coördinaat-snap) stikt automatisch
  correct over de AZ/GE- en GE/TR-grens heen. Lengtetoets: 1.741,1 km tegen 1.768 km gepubliceerd (SOCAR
  Midstream/Wikipedia, 443 AZ+249 GE+1.076 TR) = **−1,5%**, ruim binnen de ±15%-norm.

**Toets (§5 bakhandleiding):**
- Km-toets: been 2 (het enige gemeten landbeen) **−1,5%** t.o.v. de gepubliceerde 1.768 km — binnen ±15%.
- Naden: alle vier de benen sluiten op **0,00 km** op elkaar aan.
- Markers: beide markers liggen exact (0 m) op hun been-uiteinde.
- `toets_knikken.py`: 34 knikken ≥60° langs de leiding (verwacht voor een pijpleiding die het terrein volgt),
  **0 omkeringen, 0 terugloop** — geen enkele reparatie nodig.
- `toets_rechte_benen.py --min-km 5`: vlagt de twee stippel-benen (been 3, 6,1 km) en de haven-aanloop-stippel
  (been 4, 7,7 km) als omwegfactor ≈1,00 — verwacht, want dat zijn per constructie rechte lijnen en al als
  stippel getekend; geen bevinding.
- `json.load`: `versie`=2, `punt_formaat`="lonlat", modaliteiten ⊂ {zee, leiding}, elk been ≥2 punten,
  bestand 57,7 KB (ruim onder de ~300 KB-richtlijn).

**Lessen:**
- Een component-graaf op gedeelde OSM-node-refs stikt een grensoverschrijdende pijpleiding automatisch over
  Geofabrik-extractgrenzen heen — geen los grens-stitchmechanisme nodig zolang de buurextracts de grensknoop
  allebei bevatten (wat hier voor AZ/GE en GE/TR het geval was).
- De brief-inschatting "0-3 korte stippel-naden" bleek pessimistisch: het gemeten resultaat (1 aaneengesloten
  component, 0 naden) is beter dan de brief voorspelde. Niet de brief-inschatting overnemen als vaststaand
  feit — het bakken zelf is de toets.

## 10 · Bak-aanwijzingen (oorspronkelijk, vóór het bakken)
