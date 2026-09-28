# Routebrief (licht) · olie — Bonny (Nigeria) → Vadinar (India)

**stroom-id:** `olie-bonny-vadinar` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** Nigeriaanse lichte zoete ruwe olie (Bonny Light) per **zeeschip** vanaf de Bonny-exportterminal
(Shell/SPDC/NNPC), om Kaap de Goede Hoop (geen Suez), naar de Vadinar SPM van Nayara Energy in de Golf van Kutch,
en van daar per **eigen crude-pijpleiding** (~15 km) naar de Vadinar-raffinaderij (Gujarat) voor binnenlandse
raffinage — géén gedocumenteerde vervolgzending per lading, dus geen fase D.
**Welke as van het verhaal:** *West-Afrika → Azië via de Kaap.* Nigeria exporteert ~1,3–1,4 mln vaten/dag totaal
(peiljaar 2024) [12]; India is wereldwijd de grootste afnemer van Bonny Light (404 zendingen [11]) en de
snelst groeiende exportmarkt voor Nigeriaanse ruwe olie (+$1,14 mrd 2023→2024). Vadinar-raffinaderij verwerkt
20 Mt/j (≈405 kb/d) [6][7] en staat sinds 18-07-2025 onder EU-sancties wegens het 49,13%-belang van Rosneft [8][9]
— relevant voor deze as, geen showstopper voor de crude-invoer zelf (zie §7).

## 1 · Ketenkaart
```
Bonny-exportterminal `ol-bonny-term` ──(b1 zee · Golf van Guinee → Kaap de Goede Hoop → Indische Oceaan
   → Arabische Zee (geen Suez) · ~11.500 km, MARNET, aannemelijk: geen cargo-niveau bron)──►
   Vadinar SPM `ol-vadinar-spm` (Pathfinder Inlet, Golf van Kutch)
   ──(b2 leiding · eigen crude-pijpleiding SPM–raffinaderij, stippel · ~15 km)──►
   Vadinar-raffinaderij `ol-vadinar-raf` (Nayara Energy, Gujarat) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Bonny-exportterminal → Vadinar SPM (aannemelijk: geen cargo-niveau bron) | Golf van Guinee → Kaap de Goede Hoop → Indische Oceaan → Arabische Zee — natuurlijke Kaap-route, geen Suez | ~11.500 [ontwerp/webcheck] | MARNET (kade → kade) | nee — beide kades binnen zeeknoop-bereik (Bonny 7,9 km [webcheck]) |
| b2 | C | leiding | Vadinar SPM → Vadinar-raffinaderij | eigen crude-pijpleiding SPM–tankfarm–raffinaderij | ~15 [ontwerp] | stippel — eigen verbinding zonder net | ja — eigen pijpleiding, niet verwacht in OSM (`man_made=pipeline` ontbreekt naar verwachting op dit tracé) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-bonny-term` | laadplek / exportterminal | Bonny Oil & Gas Terminal (Shell/SPDC/NNPC), Bonny Island, Nigeria | 4.4200, 7.1600 | [1][2][3] | bron-gelegd (z15 gezien: tankenpark, procesinstallatie en meerdere steigers/aanlopen de zee in; v1-anker `oil-term-bonny` hergebruikt) |
| `ol-vadinar-spm` | overslag zee → leiding | Vadinar SPM, Pathfinder Inlet (Nayara Energy), Golf van Kutch, India | 22.4528, 69.6694 | [4][5] | bron-gelegd (z15 gezien: trestle met SPM-kop de vaargeul in, tegenover de vaste jetty's van de raffinaderij aan de overkant) |
| `ol-vadinar-raf` | raffinaderij (fase C, site-anker) | Vadinar-raffinaderij (Nayara Energy), Gujarat, India | 22.3317, 69.7472 | [6][7] | bron-gelegd (z14 gezien: tankenpark en procesinstallaties van het raffinagecomplex, ~9 km landinwaarts van de SPM) |

## 4 · Via-punten
Geen — b1 wordt door de MARNET-router zelf gelegd (kade → kade, geen corridorkeuze te benoemen), b2 is een korte
gestippelde eigen leiding zonder alternatieve route.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Vadinar-raffinaderij | Nayara Energy (49,13% Rosneft, 24,50% Trafigura/UCP, 49,13%+ overig; EU-gesanctioneerd sinds 18-07-2025) | ruwe olie → diesel/benzine/kerosine/overige producten | 20 Mt/j ruwe olie ≈ 405 kb/d, complexiteit 11,8 (2e grootste single-site raffinaderij van India) | [6][7][8][9] |

## 6 · Stoppunt
De brief stopt bij de poort van de Vadinar-raffinaderij: de ruwe olie gaat in binnenlandse raffinage, geen bron
noemt een specifieke afnemer of exportbestemming per lading voor de resulterende producten (EU-export is sinds
18-07-2025 bovendien verboden) — fase D vervalt.

## 7 · Open punten
- **Geen cargo-niveau bron koppelt Bonny-crude specifiek aan Vadinar.** Bonny Light gaat naar meerdere Indiase
  raffinaderijen (Jamnagar, Vadinar, Mangalore) zonder vaste toewijzing per lading [11][12]; deze as is afgeleid
  uit geaggregeerde handelsdata (Nigeria→India-totaal + Bonny Light-bestemmingsspreiding), niet uit een bron die
  één specifieke tanker aan de Vadinar SPM koppelt.
- **EU-sancties op Nayara/Vadinar** (18-07-2025, 18e sanctiepakket, wegens het 49,13%-belang van Rosneft):
  productexportverbod naar de EU, tegoedenbevriezing, beperkte verzekerings-/bankdiensten [8][9]. De crude-invoer
  voor binnenlandse raffinage lijkt door te gaan — geen VS-sanctie, Nayara herstelde binnen ~2 maanden tot 75%
  capaciteit met Indiase staatssteun [9] — dat rechtvaardigt het aanhouden van deze as, maar is een blijvend risico.
- **Herhaalde force-majeure-onderbrekingen bij de Bonny-terminal** (2022–2023) maken het volume volatiel; geen
  actueel, aan deze specifieke as gekoppeld volumecijfer gevonden.
- **Fase D vervalt**: geen bron benoemt een specifieke downstream-bestemming voor de Vadinar-producten per lading
  (binnenlandse Indiase markt, geen aanwijsbare eindklant).

## 8 · Bronnen
[1] Findaport, "Port of Bonny Offshore Terminal, Nigeria" — BOGT, drie SPM's, afstand tot de kust. https://www.findaport.com/port-of-bonny-offshore-terminal
[2] TankTerminals, "Shell's 250,000bpd Bonny Export Terminal Restarts Operation". https://tankterminals.com/news/shells-250000bpd-bonny-export-terminal-restarts-operation/
[3] Premium Times Nigeria, "Shell resumes crude oil export operations at Bonny Terminal". https://www.premiumtimesng.com/business/business-news/587968-shell-resumes-crude-oil-export-operations-at-bonny-terminal.html
[4] MoEFCC (India), Brief Summary of the Project — Vadinar SPM-coördinaten 22°27'10"N 69°40'10"E. https://environmentclearance.nic.in/writereaddata/Online/TOR/01_Aug_2019_091210520PWAJ0Q8GAnnexure-BriefSummaryoftheProject.pdf
[5] Wikipedia, "Vadinar" — locatie Golf van Kutch, Devbhoomi Dwarka district. https://en.wikipedia.org/wiki/Vadinar
[6] Nayara Energy, officiële site — Vadinar-raffinaderij, 20 Mt/j, complexiteit 11,8. https://www.nayaraenergy.com/vadinar-refinery
[7] Wikipedia, "Vadinar Refinery" — coördinaten 22°19′54″N 69°44′50″E, capaciteit/complexiteit. https://en.wikipedia.org/wiki/Vadinar_Refinery
[8] Bloomberg, 20-07-2025, "EU Sanctions Against India's Nayara 'Unjustified,' Rosneft Says". https://www.bloomberg.com/news/articles/2025-07-20/eu-sanctions-against-india-s-nayara-unjustified-rosneft-says
[9] Euromaidan Press, 29-09-2025, "EU sanctions hit, but India's Russia-linked refiner bounces back in 60 days" — 75% capaciteit hersteld, geen VS-sanctie. https://euromaidanpress.com/2025/09/29/india-eu-us-sanctions-gap-nayara-rosneft/
[10] Rosneft, persbericht — reactie op de EU-sancties. https://www.rosneft.com/press/releases/item/222585/
[11] Volza, "Bonny Light Crude Oil / Nigerian Crude Oil" importdata — 404 zendingen naar India. https://www.volza.com/p/bonny-light-crude-oil-or-nigerian-crude-oil/import/
[12] EIA, Nigeria Country Analysis Brief 2025 (PDF) — exportvolume ~1,3–1,4 mln vaten/dag. https://www.eia.gov/international/content/analysis/countries_long/Nigeria/Nigeria-2025.pdf
[13] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15) — `sat-olie-bonny-vadinar-bonny-term.png`, `sat-olie-bonny-vadinar-vadinar-spm.png`, `sat-olie-bonny-vadinar-vadinar-raf.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `olie-bonny-vadinar`** → `v2/data/stroomroute-olie-bonny-vadinar.json` — 3 benen, **13.668,1 km**, 1.401 punten, 3 markers (2 stippel).
Recept: `bak_stromen.sh` (functie `bak_olie_bonny_vadinar`).

**b1 (zee, geroutet):** `--been "zee|zeeschip Bonny-exportterminal → Vadinar SPM (Golf van Guinee → Kaap de Goede Hoop → Indische Oceaan → Arabische Zee, geen Suez)|4.4200,7.1600|22.5734,69.4446"` — MARNET-route, kade Bonny (snap 7,85 km) tot de zeeknoop bij Vadinar (snap 0,00 km, want die knoop IS het eindpunt). **13.623,6 km**, 1.387 punten. De getekende route loopt zichtbaar via de Golf van Guinee, om de Kaap (−35,00/18,00) en dwars over de Indische Oceaan naar de Golf van Kutch — geen Suez, zoals de brief eist.

⚠️ **Lengtetoets buiten de norm, bevinding niet dichtgetrokken:** 13.623,6 km tegen de gepubliceerde ~11.500 km (ontwerp/webcheck) = **+18,5%**, buiten ±15%. De brief-schatting was zelf al gemerkt "geen gepubliceerde ladingroute-lengte" — de MARNET-router meet de daadwerkelijke Kaap-omvaart tussen de twee kades, en dat blijkt substantieel langer dan de webcheck-schatting. Geen via-punt bijgeschoven om het getal te halen; de gemeten km is de bevinding.

**b1-aanloop (zee, stippel-geojson):** Vadinar SPM ligt op **26,7 km** van de dichtstbijzijnde MARNET-zeeknoop (> 25 km, dus geen automatische snap) → `python v2/tools/maak_havenaanloop.py --naam olie-bonny-vadinar-vadinar-spm --van 22.4528,69.6694 --naar 22.5734,69.4446 --uit v2/build-cache/ais/graaf/olie-bonny-vadinar-aanloop-vadinar-spm.geojson`, gekozen trap **0,02° gebufferd**, **28,84 km**, 12 punten, 0,00 km land midden op de lijn (geen landkruising). De geojson-punten liggen in kade→zeeknoop-volgorde (toolconventie); voor de reisvolgorde (zeeknoop → kade, want Vadinar is hier de bestemming) is de puntenlijst vóór het bakken **omgekeerd** — dit is de enige aanpassing aan de tool-uitvoer. `--stippel-geojson "zee|haven-aanloop Vadinar SPM (schematisch, over water — MARNET reikt niet: 26,7 km)|$BEEN/olie-bonny-vadinar-aanloop-vadinar-spm.geojson"`.

**b2 (leiding, stippel):** `--stippel "leiding|Vadinar SPM → Vadinar-raffinaderij (eigen crude-pijpleiding, schematisch — niet verwacht in OSM)|22.4528,69.6694|22.3317,69.7472"` — rechte lijn tussen de twee ankers, geen OSM-way gezocht (brief: eigen bedrijfsleiding, geen gedeeld net). **15,7 km** tegen de gepubliceerde ~15 km (ontwerp) = **+4,4%**, ruim binnen ±15%.

**Markers:** `ol-bonny-term` (kop been 1, 7,85 km van het routeerpunt — anker ≠ routeerpunt: de kade ligt landinwaarts van de dichtstbijzijnde zeeknoop, verwacht en genoemd in de brief) · `ol-vadinar-spm` (0,00 km van de lijn — exact het startpunt van b2 én het eindpunt van de aanloop) · `ol-vadinar-raf` (0,00 km van de lijn — eindpunt van b2, stoppunt).

**Toets:** `toets_knikken.py` — 2 knikken ≥60° (112,4° bij 22,543/68,720 en 67,9° bij −35,00/18,00, beide krappe bochten op het zeenet — de eerste vlak vóór de aanloop-aansluiting, de tweede bij de Kaap-ronding), **0 omkeringen ≥150°**, 0 terugloop. `toets_rechte_benen.py --min-km 5` — 1 been gevonden (🟡 MIDDEL, stippel, omwegfactor 1,002, b2): correct geclassificeerd als stippel-met-reden, geen bevinding op zichzelf. Naad tussen b1→aanloop en aanloop→b2: **0,00 km** (beide punt-op-punt gedeeld). json geldig: versie 2, punt_formaat lonlat, modaliteiten `zee`/`leiding` (in de toegestane set), elk been ≥2 punten (1.387/12/2), bestandsgrootte **25,7 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- Een kade net over de 25 km-zeeknoop-grens (hier 26,7 km) is geen twijfelgeval: de handleiding trekt de lijn hard bij ~25 km, en `maak_havenaanloop.py` levert ook op een kleine overschrijding meteen een schone aanloop (0 km land midden op de lijn, eerste trap).
- Wanneer de verre kade de BESTEMMING is (niet het vertrekpunt zoals in de bestaande voorbeelden), moet de aanloop-geojson vóór het bakken worden omgekeerd: `maak_havenaanloop.py --van <kade> --naar <zeeknoop>` schrijft de punten altijd in die volgorde, terwijl de reisvolgorde hier zeeknoop → kade is. `_geojson_been()` in `hecht_marnet.py` leest de punten letterlijk, zonder auto-richting — de aanroeper is hiervoor verantwoordelijk.
- Een brief-km die zichzelf al markeert als "geen gepubliceerde ladingroute-lengte" (ontwerp/webcheck-schatting) is een zwakke meetlat; een afwijking van +18,5% op zo'n schatting is eerder een correctie van de schatting dan een routefout — vooral bij een lange Kaap-omvaart waar kleine koersverschillen zich over 13.000+ km opstapelen.
