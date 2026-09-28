# Routebrief (licht) · olie — Primorsk → Jamnagar (India)

**stroom-id:** `olie-primorsk-jamnagar` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** Russische Oostzee-ruwe olie van de Primorsk-exportterminal (Baltic Pipeline System-terminus,
Transneft) per **zeeschip** rond Europa via Gibraltar-Suez-Bab-el-Mandeb naar de Reliance-marineterminal bij
Sikka (jetty/SPM, Golf van Kutch), en via een **eigen crude-pijpleiding** (stippel — niet in OSM gekarteerd) naar
het Jamnagar-raffinaderijcomplex (Reliance, SEZ-exporteenheid + DTA-binnenlandeenheid) — stoppunt bij de
raffinaderij, geen productexport meegebakken.
**Welke as van het verhaal:** de Rusland-omleiding sinds 2022 (Oostzee-crude naar India). India importeerde in
2024 gemiddeld ~1,8 mln vaten/dag Russische ruwe olie (piek juli 2024: 2,08 mln vaten/dag), overwegend via de
Primorsk/Ust-Luga ↔ Jamnagar/Kandla-route, peiljaar 2024–2026 [13][15]. ⚠️ Sinds 20-11-2025 stopte de
SEZ-eenheid van Jamnagar met Russische crude (EU-sanctiepakket op Rosneft/Lukoil); binnenkomende Russische
olie ging naar de DTA-eenheid op hetzelfde complex, hervat januari 2026, +14% m-o-m in mei 2026 [9][10][11][12].

## 1 · Ketenkaart
```
Primorsk-exportterminal `ol-primorsk-kade` (Transneft, BPS-terminus, Leningrad Oblast)
   ──(b1 zee · Oostzee → Deense Straten → Noordzee → Golf van Biskaje → Straat van Gibraltar →
       Middellandse Zee → Suezkanaal → Rode Zee → Bab-el-Mandeb → Arabische Zee ·
       ~11.500 km [ontwerp-schatting; MARNET meet de exacte lengte] · alternatief bij sanctie-/
       diepgangdruk op Suez: om de Kaap, niet getekend)──► Sikka Marine Terminal `ol-sikka-terminal`
       (Reliance/SPTL, jetty + SPM's, Golf van Kutch)
   ──(b2 leiding · eigen crude-pijpleiding SPM-terminal → raffinaderij, stippel · ~17 km [webcheck;
       ontwerp noemde ~50 km, niet bevestigd])──► Jamnagar-raffinaderijcomplex `ol-jamnagar-raffinaderij`
       (Reliance, SEZ-exportraffinaderij + DTA-binnenlandraffinaderij op één complex) ── stoppunt
```
Risiconoot: G7-prijsplafond en EU-sanctiepakketten kunnen de stroom snel doen omslaan naar de Kaap-route of
andere afnemers; schaduwvloot-tankers (ship-to-ship overslag) maken AIS-gebaseerde routebevestiging
onbetrouwbaar [design-invoer]. Sinds 20-11-2025 is de routering genuanceerder: de SEZ-raffinaderij (exportgericht)
verwerkt sindsdien geen Russische crude meer; de DTA-eenheid op hetzelfde Jamnagar-complex wél, met een
onderbreking en hervatting (zie boven) [9][10][11][12]. De lichte werkwijze onderscheidt geen SEZ/DTA-subankers —
het anker blijft het raffinaderijcomplex op site-niveau.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ol-primorsk-kade` → `ol-sikka-terminal` | Oostzee–Deense Straten–Noordzee–Biskaje–Gibraltar–Middellandse Zee–Suez–Rode Zee–Bab-el-Mandeb–Arabische Zee | ~11.500 [ontwerp; MARNET meet de exacte lengte] | MARNET | nee |
| b2 | C | leiding | `ol-sikka-terminal` → `ol-jamnagar-raffinaderij` | eigen crude-pijpleiding SPM-terminal–raffinaderij | ~17 [webcheck: hemelsbreed 16,4 km tussen de twee ankers; ontwerp noemde ~50 km, in geen bron teruggevonden] | stippel "leiding" — Overpass rond Sikka–Jamnagar geeft 0 × `man_made=pipeline` op dit tracé [16] | ja — eigen pijpleiding, niet verwacht en niet gevonden in OSM |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-primorsk-kade` | laadplek / kade | Primorsk-exportterminal (Transneft, BPS-terminus), Leningrad Oblast | 60.3340, 28.7090 | [1][2][8] | bron-gelegd (z15 gezien: tankenpark van tientallen grote ronde crude-tanks ~700 m landinwaarts, twee laadsteigers de baai in; een rode ruwe-olietanker ligt aan de zuidsteiger) |
| `ol-sikka-terminal` | overslag zee → leiding | Reliance/SPTL Marine Terminal Sikka (jetty + SPM's), Golf van Kutch, Gujarat | 22.4990, 69.8330 | [3][4][5][8] | bron-gelegd (z16 gezien: trestle-steiger ~5,5 km de zee in vanaf de Sikka-tankfarm, T-vormige laadkop met vier getankerde schepen — waaronder een rood-rompige ruwe-olietanker — langszij) |
| `ol-jamnagar-raffinaderij` | losplek / raffinaderij | Jamnagar-raffinaderijcomplex (Reliance Industries: SEZ + DTA) | 22.3500, 69.8500 | [6][8] (v1-checklist, hergebruikt — geen coördinaatwijziging) | bron-gelegd (z14 gezien: rijen cilindrische opslagtanks en procesinstallaties over meerdere km², reeds bevestigd in v1; het complex loopt satelliet-zichtbaar door tot de kust-tankfarm bij Sikka, ~22.43/69.87) |

## 4 · Via-punten
Geen — b1 is een zeeleg (MARNET routeert kade→kade zonder handmatige via-punten; de genoemde zeestraten
liggen al in de routeergraaf) en b2 is een rechte stippel tussen twee ankers (eigen leiding, geen corridorkeuze).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Jamnagar-raffinaderijcomplex | Reliance Industries | ruwe olie (incl. Russische mix) → benzine/diesel/nafta/petrochemie | wereldgrootste single-site raffinaderijcomplex, gecombineerd SEZ (exportgericht) + DTA (binnenlandse markt); SEZ-eenheid stopte Russische crude-inname 20-11-2025, DTA-eenheid nam het over | [6][9][10][11] |

## 6 · Stoppunt
De brief stopt bij het Jamnagar-raffinaderijcomplex: dit is de bestemming uit het ketenontwerp, en fase D/E
(productexport van benzine/diesel vanaf Jamnagar) is een aparte keten met eigen bestemmingen en valt buiten
deze brief — geen bron in deze ronde koppelt een specifieke Russische-crude-lading aan een specifieke
productstroom naar een specifiek exportland.

## 7 · Open punten
- **Welke van de vijf jetty-berths / vijf SPM's van SPTL** de Russische ruwe olie feitelijk ontvangt, is niet per
  lading gebrond — `ol-sikka-terminal` is het jetty/SPM-complex als geheel, satelliet bevestigt tankers aan de
  steigerkop maar niet welke SPM specifiek.
- **Pijpleidingtracé Sikka → Jamnagar niet in OSM gekarteerd** (0 × `man_made=pipeline` in een Overpass-check
  rond de bbox 22,30–22,50 / 69,75–69,95) → stippel over de hemelsbrede afstand (16,4 km tussen de ankers);
  het ontwerp noemde ~50 km maar dat cijfer is in geen geraadpleegde bron teruggevonden — mogelijk een eerdere
  schatting die het hele complex (kust-tankfarm tot de zuidelijke procesunits, ~15 km) plus marge meerekende.
- **SEZ/DTA-nuance (nov 2025–heden)** staat in de tekst maar wordt niet als apart anker of been getekend —
  conform de bindende aanpassing uit de haalbaarheidstoets (de lichte werkwijze onderscheidt geen subankers
  binnen één complex).
- **Schaduwvloot-tankers (ship-to-ship-overslag)** maken een AIS-gebaseerde bevestiging van de exacte route
  onbetrouwbaar (uit het ketenontwerp); dit raakt de bake-verificatie van been b1 (MARNET tekent de kortste
  legale route, niet per se de werkelijk gevaren route van een schaduwvloot-schip).
- **Jaarvolume in oorspronkelijke eenheid:** ~1,8 mln vaten/dag (2024-gemiddelde), piek 2,08 mln vaten/dag
  (juli 2024) [13][15]. Omgerekend naar Mt/jaar: 1,8 mb/d × 365 dagen ≈ 657 mln vaten/jaar; bij ~7,3 vaten/tonne
  (typische dichtheid Oeral-mix) ≈ **90 Mt/jaar** — indicatief, de werkelijke dichtheid van de geleverde crude-mix
  is niet per lading gebrond.

## 8 · Bronnen
[1] Wikipedia, "Port of Primorsk" — coördinaten 60°20'00"N 28°43'00"E, terminal van Transneft, BPS-terminus, 9 dokken. https://en.wikipedia.org/wiki/Port_of_Primorsk
[2] Wikipedia, "Baltic Pipeline System" — Primorsk als westelijk eindpunt van de BPS, crude uit West-Siberië/Timan-Pechora. https://en.wikipedia.org/wiki/Baltic_Pipeline_System
[3] Shipnext, "Sikka Port Data & Shipping Insights" — Sikka op de zuidkust van de Golf van Kutch, geëxploiteerd door Reliance; Jamnagar Marine Terminal 10 berths (5 tankerberths + 5 SPM's). https://shipnext.com/port/sikka-insik-iot
[4] Sikka Ports & Terminals Limited (SPTL), officiële site — captive havenfaciliteit voor RIL Jamnagar: SPM's, jettyberths, crude-/productopslagtanks en onderzeese/onshore-pijpleidingen tussen SPM's, jetty en Marine Tank Farm. https://www.sptl.co.in/business.html
[5] CARE Ratings, persbericht Sikka Ports & Terminals Limited (2024) — SPTL als BOMT-havenfaciliteit met 10 captive jetty's, licentie Gujarat Maritime Board. https://www.careratings.com/upload/CompanyFiles/PR/202407130748_Sikka_Ports_&_Terminals_Limited.pdf
[6] Wikipedia, "Jamnagar refinery" — Reliance Industries, Motikhavdi/Jamnagar, Gujarat, coördinaten 22°20'53"N 69°52'08"E, wereldgrootste single-site raffinaderijcomplex (SEZ + DTA). https://en.wikipedia.org/wiki/Jamnagar_refinery
[7] v1-checklist, `data/oil.js` + `design/olie.md` — anker `oil-ref-jamnagar` 22.35, 69.85 (hergebruikt, geen coördinaatwijziging conform de haalbaarheidstoets).
[8] Esri World Imagery via `v2/tools/sat_check.py` (z13–z16, live) — `v2/build-cache/satcheck/sat-olie-primorsk-jamnagar-primorsk-overview.png`, `sat-olie-primorsk-jamnagar-primorsk-berth.png`, `sat-olie-primorsk-jamnagar-sikka-mtf.png`, `sat-olie-primorsk-jamnagar-sikka-jetty-full.png`, `sat-olie-primorsk-jamnagar-sikka-jettyhead.png`, `sat-olie-primorsk-jamnagar-refinery-overview.png`, `sat-olie-primorsk-jamnagar-refinery-zoom.png`, `sat-olie-primorsk-jamnagar-sikka-tankfarm.png`.
[9] Business Standard, 20-11-2025 — "Reliance stops import of Russian crude oil into Jamnagar's SEZ refinery" (VS-sancties Rosneft/Lukoil, 21-11-2025). https://www.business-standard.com/industry/news/reliance-stops-import-of-russian-crude-oil-into-jamnagar-s-sez-refinery-125112001129_1.html
[10] BusinessToday, 21-11-2025 — "Reliance just pulled the plug on Russian oil at its Jamnagar export refinery" — DTA-eenheid neemt binnenkomende Russische crude over. https://www.businesstoday.in/latest/corporate/story/reliance-just-pulled-the-plug-on-russian-oil-at-its-jamnagar-export-refinery-503092-2025-11-21
[11] Outlook Business — "Reliance Halts Russian Oil Imports at Jamnagar Refinery to Comply with Sanctions". https://www.outlookbusiness.com/corporate/reliance-halts-russian-oil-imports-at-jamnagar-refinery-to-comply-with-sanctions
[12] DiscoveryAlert — "India Russian oil imports rise May 2026" (hervatting + 14% m-o-m). https://discoveryalert.com.au/news/india-russian-oil-imports-rise-may-2026/
[13] TheePrint, "How Russian oil makes its way to India: two key routes, a backup, a sanctions hack". https://theprint.in/economy/how-russian-oil-makes-its-way-to-india-two-key-routes-a-backup-a-sanctions-hack/2893853/
[14] Energy and Clean Air, "June 2026 monthly analysis of Russian fossil fuel exports and sanctions". https://energyandcleanair.org/june-2026-monthly-analysis-of-russian-fossil-fuel-exports-and-sanctions/
[15] Al Jazeera, 22-08-2025 — "Behind India's massive Russian oil imports". https://www.aljazeera.com/economy/2025/8/22/behind-indias-massive-russian-oil-imports-asias-richest-man
[16] OpenStreetMap (ODbL) via Overpass — `overpass-api.de`, query op landuse=industrial/man_made=pipeline/pier/storage_tank en naam~"Sikka" in bbox 22,30–22,50 / 69,75–70,10 (2026-09-27); vond o.a. way "Reliance Refinery" (landuse=industrial, center 22.3368/69.8666), Sikka Port-knoop (22.4325/69.8358), diverse piers, 0 × `man_made=pipeline` op het Sikka–Jamnagar-tracé. https://www.openstreetmap.org


## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `olie-primorsk-jamnagar`** → `v2/data/stroomroute-olie-primorsk-jamnagar.json` — 4 benen, **14.111,6 km**, 1.552 punten, 3 markers. zee 31,0 (stippel) + 14.020,4 + 43,5 (stippel) = 14.094,9 km · leiding 16,7 km (stippel).
Recept: `bak_stromen.sh` (functie `bak_olie_primorsk_jamnagar`).

**b1 (zee):** beide ankers liggen BUITEN de 25 km-norm van een MARNET-zeeknoop (Primorsk 31,041 km tot zeeknoop 6850 op 60,59370/28,50130; Sikka 40,7 km tot zeeknoop 5321 op 22,57340/69,44460) — dus twee haven-aanlopen in plaats van een directe kade→kade-snap:
- Primorsk-aanloop: `maak_havenaanloop.py` liep vast op `timeout 300` (exit 124) — geen tweede poging, direct een rechte stippel (31,0 km, 2 punten).
- Sikka-aanloop: gelukt op de eerste poging (trap 0,005° gebufferd, 43,5 km over 79 punten, omwegfactor 1,068, 0,00 km over land midden op de lijn) → `--stippel-geojson`.
- Hoofdzeebeen (zeeknoop → zeeknoop, MARNET, `northwest` dicht/default): **14.020,4 km over 129 MARNET-edges, 1.469 punten** (lengte-invariant: getekende lijn 14.020,408 vs som edge-km 14.020,600 = −0,192 km, de naden).

⚠️ **Buiten de ±15%-norm, bevinding i.p.v. bijgeschoven:** de volledige b1 (aanloop + hoofdbeen + aanloop) komt op **14.094,9 km tegen de ontwerp-schatting ~11.500 km uit de brief = +22,6%.** De brief noemt dit cijfer zelf expliciet "ontwerp-schatting, geen gepubliceerde lengte; MARNET meet exact" — dat is precies wat hier is gebeurd: MARNET routeert via Oostzee → Deense Straten → Noordzee → Golf van Biskaje → Gibraltar → Middellandse Zee → Suez → Rode Zee → Bab-el-Mandeb → Arabische Zee (129 edges, geen enkel handmatig via-punt nodig — de route komt uit de graaf zelf) en de gemeten lengte is 22,6% langer dan de eerdere schatting. Niet dichtgetrokken: de brief waarschuwde hier al voor.

**b2 (leiding, stippel):** rechte lijn Sikka-terminal (22,4990/69,8330) → Jamnagar-raffinaderij (22,3500/69,8500), **16,660 km** tegen de webcheck-schatting van 16,4 km hemelsbreed uit de brief = +1,6%, ruim binnen ±15%. Geen OSM `man_made=pipeline` gevonden op dit tracé (bevestigt brief §7/§8[16]); het ontwerp-cijfer ~50 km is in geen bron of meting terugvonden.

**Toets:** naden tussen alle vier opeenvolgende benen **0,00 km** (elk been begint exact waar het vorige eindigt — Primorsk-stippel → hoofdzeebeen → Sikka-aanloop-geojson → leiding-stippel, elke overgang op de letterlijke coördinaat van de vorige). `toets_knikken.py`: **3 knikken ≥60° (77,7°/76,8°/64,3°, boogstralen 6,2–8,7 km, bij 24,3/66,6 · 55,3/12,7 · 36,8/−9,25 — respectievelijk de Arabische Zee-nadering/Straat van Hormuz-corridor, de Deense Straten en de Straat van Gibraltar), 0 omkeringen ≥150°, 0 TERUGLOOP.** `toets_rechte_benen.py --min-km 5`: beide stippelbenen (31,0 km, omwegfactor 0,999; 16,7 km, omwegfactor 1,002) staan correct als stippel — geen doorgetrokken been met omwegfactor 1,000. json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {zee, leiding}, elk been ≥2 punten, bestandsgrootte **27,9 KB** (ruim < 300 KB, richtwaarde). Markers: alle drie op 0,00 m van hun been — elk anker is zelf het letterlijke eindpunt van het aangrenzende been-segment (geen anker≠routeerpunt-afwijking).

**Gereedschapslessen:**
- `marnet_zee()` gaf voor beide ankers een snap > 25 km (Primorsk 31,0 · Sikka 40,7 km) — bij twee zulke ankers in één stroom loont het de check vóóraf voor beide uiteinden te draaien in plaats van na een mislukte bake terug te moeten.
- `maak_havenaanloop.py` faalde op de Primorsk-kant binnen 300 s en slaagde op de Sikka-kant meteen — dezelfde tool geeft bij twee vergelijkbare ankers geen gegarandeerd gelijk resultaat; een losse tweede aanroep in de tegengestelde richting op de Sikka-aanloop liep bij toeval opnieuw tegen de timeout aan, dus is de al geslaagde geojson achteraf met een simpele puntenreeks-omkering (geen nieuwe routeerpoging, alleen de volgorde in het bestand) in reisvolgorde gezet.
- Een ontwerp-schatting die zichzelf al "geen gepubliceerde lengte, MARNET meet exact" noemt, is een uitnodiging tot een bevinding, niet tot bijschuiven: de +22,6% hier is precies wat de brief voorspelde dat kon gebeuren.
