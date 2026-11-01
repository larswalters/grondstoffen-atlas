# Routebrief (licht) · Zeldzame aardmetalen · White Mesa → Houston → Muuga → Silmet (Estland)

**stroom-id:** `ree-whitemesa-sillamae` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · White Mesa Mill (Utah) → Houston → Muuga → Silmet Sillamäe (VS → Estland; peiljaar 2023, stroom gestopt 2024; aannemelijk: haven en modaliteit niet gebronnen)
**Keten in één zin:** Gemengd REE-carbonaat (MREC) uit monazietzand van de White Mesa Mill (Energy Fuels, Blanding, Utah) gaat in containers per **truck** over US-191/160/64/550, I-40, US-84 en TX-6 naar Barbours Cut (Houston), per **zeeschip** (MARNET, Golf van Mexico, Atlantische Oceaan, Kanaal, Oostzee) naar de Finse Golf, over een stippel-haven-aanloop naar Muuga en per **truck** over weg 1/E20 naar NPM Silmet in Sillamäe, waar Neo het MREC scheidt in NdPr-oxide en een zwaar-REE-carbonaat. Stoppunt aan de poort van Silmet.
**Welke as van het verhaal:** de eerste Amerikaanse monaziet-keten naar Europese scheiding (2021-2023). Jaarvolume: Eurostat Estland-import uit de VS, CN 2846 (REE-verbindingen): 254,5 t (2021), 196,0 t (2022), **331,6 t (2023)**, 2024 en 2025 ca. 0 [1]. Productgewicht; met REO ca. 70% is 2023 ca. **0,23 kt REO per jaar** (indicatie, eigen omrekening). Peiljaar 2023; sinds 2024 scheidt Energy Fuels zelf [2].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** wegkm niet 1.892 maar 2.056-2.073 km (OSRM met via-punten; us-colorado ontbreekt, dus langs Kayenta en Shiprock); zee gemeten 10.746,1 km (ontwerp 11.000); titel "peiljaar 2023, stroom gestopt 2024" en "aannemelijk: haven en modaliteit niet gebronnen"; Albuquerque-via (Central Avenue, stad) vervangen door US-550 en I-40 oost van de stad. Eindpunt blijft Silmet zoals het id belooft.

## 1 · Ketenkaart
```
White Mesa Mill, Blanding (Utah) `ree-whitemesa-mill` (hergebruikt anker, ree-georgia-whitemesa)
  ──(b1 truck · US-191 → US-160/163 Kayenta → US-64 Shiprock → US-550 → I-25/I-40 → US-84 Lubbock/Post → TX-6 · hemelsbreed 1.599,5 km, geen wegkm; OSRM 2.056-2.073 km, aannemelijk)──►
Barbours Cut, Houston `ree-houston-kade` (hergebruikt anker, ree-larochelle-sanmarcos)
  ──(b2 zee · Golf van Mexico, Florida-straat, Atlantische Oceaan, Kanaal, Oostzee · 10.746,1 km, MARNET, aannemelijk)──► zeeknoop 1970 (59.8, 24.7, Finse Golf)
  ╌╌(b3 zee-stippel · haven-aanloop Muuga · 37,5 km, LETTERLIJKE KOPIE ree-kuantan-narva b3)╌╌► Muuga-containerterminal `ree-muuga-ct`
  ──(b4 truck · weg 1/E20 + weg 94 · ~176 km, KOPIE ree-sillamae-newark b1, omgekeerd)──► NPM Silmet `ree-silmet-scheiding` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-whitemesa-mill` → `ree-houston-kade` | US-191 → US-160/163 (Kayenta) → US-64 (Shiprock) → US-550 → I-25/I-40 → US-84 (Lubbock, Post) → TX-6 (Hico, Bryan) | hemelsbreed 1.599,5 km, geen wegkm; OSRM 2.055,5 km met de via-punten van §4, 2.073 km met de ontwerppunten [8]; de ±15%-toets is een indicatie | maak_stroombeen_weg (us-utah, us-arizona, us-new-mexico, us-texas) | nee — *aannemelijk: haven en modaliteit niet gebronnen* |
| b2 | B | zee | `ree-houston-kade` → zeeknoop 1970 | Golf van Mexico, Straat van Florida, Atlantische Oceaan, Kanaal, Oostzee (MARNET kiest) | 10.746,1 (eigen MARNET-dry-run [12]; snap Barbours Cut 0,02 km op track, zeeknoop 6228 op 1,6 km, knoop 1970 0,0 km) | MARNET | nee; < 5 km, geen aanloop — *aannemelijk: één bron voor de bestemming Silmet, route niet gebronnen* |
| b3 | B | zee | zeeknoop 1970 → `ree-muuga-ct` | haven-aanloop Muuga, over water tussen Viimsi-punt en Prangli | 37,5 (rechte lijn) | LETTERLIJKE KOPIE van de `--stippel`-regel in `bak_ree_kuantan_narva` (knoop 1970 → kade) | **ja — hier reikt het net niet** (kade 37,5 km van de zeeknoop) |
| b4 | C | truck | `ree-muuga-ct` → `ree-silmet-scheiding` | Muuga sadama tee (94) → Peterburi tee → weg 1 (E20, Tallinn–Narva mnt) → Sillamäe | hemelsbreed 157,1 km, geen wegkm; OSRM 178,4 km; getekend 176,3 (bestaande kopie) [9][10] | KOPIE van `ree-sillamae-newark-weg-silmet-muuga.geojson`, coördinaten omgekeerd | nee |

b4 deelt zijn geometrie bewust met `ree-sillamae-newark` b1 (andere richting) en met een eventueel gelijktijdig gebakken `ree-serraverde-sillamae`; b3 is dezelfde kopie als in `ree-kuantan-narva`. b1 deelt het stuk Kayenta-Shiprock-White Mesa met `ree-georgia-whitemesa` b1 (andere richting, geen kopie).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-whitemesa-mill` | scheiding/verwerking (laadplek) | White Mesa Mill (Energy Fuels), Blanding, Utah | 37.5323, -109.5098 | hergebruik letterlijk `ree-sitelaag.json` (id `w-whitemesa`) en `ree-georgia-whitemesa.md` §3 | bron-gelegd (z15 hier gezien: kruis op kaal terrein tussen twee tailingbekkens, gebouwencluster van de mill ca. 0,5 km NO, toegangsweg naar de weg oostelijk; laadpunt binnen het millterrein) |
| `ree-houston-kade` | overslag truck → zee | Barbours Cut Container Terminal, La Porte (Houston) | 29.6819, -94.9983 | hergebruik `ree-larochelle-sanmarcos.md` §3 / `ree-kuantan-pasadena.md` [7] | aannemelijk (z15 hier gezien: kadefront met portaalkranen, containerstapels, schip aan de kade; haven = aanname, geen bron noemt Houston voor deze lading) |
| `ree-muuga-ct` | overslag zee → truck | Muuga-containerterminal (HHLA TK Estonia), Muuga sadam | 59.4915, 24.9675 | hergebruik `ree-sillamae-newark.md` §3 [9] | bron-gelegd (in die brief z16: portaalkranen en containerstapels aan de kade; haven en terminal voor deze lading = aanname) |
| `ree-silmet-scheiding` | scheidingsfabriek (losplek, stoppunt) | NPM Silmet OÜ, Sillamäe | 59.4031, 27.7421 | hergebruik letterlijk `ree-sillamae-narva.md` §3 | bron-gelegd (in die brief z15: industrieterrein met tankenpark en spooraansluiting; OSM-landuse "Silmet" op 41 m) |

Zeeknoop 1970 (59.8000, 24.7000) is een MARNET-knoop, geen anker. Geen last-mile-been: beide landbenen eindigen op het site-anker (White Mesa 0,36 km van de weg in de Georgia-bake; Silmet 0,07 km in de Newark-bake). Alle ankers zijn hergebruikt; de twee Amerikaanse zijn opnieuw bekeken (`v2/build-cache/satcheck/sat-ree-whitemesa-sillamae-{whitemesa,barbours}.png`, Esri z15).

## 4 · Via-punten (alleen b1; b4 = kopie, geen eigen via-punten)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kayenta, knoop US-160/US-163 | 36.7278, -110.2568 | pint de westelijke omweg via Arizona; us-colorado ontbreekt, dus niet via Cortez (OSRM nearest 29 m; scan-snap in Georgia-bake 0,27 km) |
| b1 | 2 | Shiprock, knoop US-64/US-491 | 36.7856, -108.6871 | pint US-64 oostwaarts naar Farmington/US-550 i.p.v. door naar Gallup en I-40 (OSRM 15 m; Georgia-bake 0,15 km) |
| b1 | 3 | US-550 bij Cuba (NM) | 36.0213, -106.9590 | houdt de route op US-550 naar Albuquerque (OSRM 1 m) |
| b1 | 4 | I-40, ca. 100 km oost van Albuquerque (Clines Corners) | 35.0088, -105.6746 | pint I-40 oostwaarts; vervangt het ontwerppunt Albuquerque (Central Avenue = stad), de route passeert Albuquerque toch via I-25 (OSRM 3 m) |
| b1 | 5 | US-84 bij Post (TX) | 33.1780, -101.3700 | pint US-84 over Lubbock i.p.v. I-40 naar Amarillo en Dallas (OSRM 0 m) |
| b1 | 6 | TX-6 ten oosten van Hico | 31.9786, -97.8427 | pint TX-6 naar Waco i.p.v. US-84/I-45; bewust buiten Hico (ontwerppunt 31.982,-98.031 ligt in een straat van het dorp; OSRM 5 m) |
| b1 | 7 | TX-6/US-190 bij Bryan (bypass) | 30.6653, -96.3299 | pint de TX-6-corridor naar Houston i.p.v. I-35/I-45 (OSRM 1 m, snelweg buiten het centrum) |

Alle punten liggen op de doorgaande weg, buiten stadscentra. Refs voor het profiel: `["US 191","US 160","US 64","US 550","I 25","I 40","US 84","TX 6","US 190"]`; profiel-coördinaten zijn (lon, lat); eerste en laatste punt zijn de ankers. `vensterKm` 60, `eindKlassen` en `eindToegangPrivaat: True` als `ree-georgia-whitemesa-ga-utah`, `gepubliceerdKm` null met bronnoot "hemelsbreed 1.599,5 km en OSRM 2.056 km via Kayenta/Shiprock vanwege ontbrekend Colorado, geen wegkm". OSRM met precies deze zeven punten: 2.055,5 km (legs 152, 160, 208, 218, 488, 402, 232, 196). Slechts één wegscan tegelijk met Texas (710 MB).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| White Mesa Mill | Energy Fuels | monazietzand (Chemours, Georgia) → REE-carbonaat (MREC) + uranium | contract monaziet min. 2.500 t/j (2020) | [2][3][5] |
| Muuga-containerterminal | HHLA TK Estonia (Port of Tallinn) | feeder/containerschip → truck | 267.752 TEU in 2022 | [9] |
| Silmet Sillamäe | Neo Performance Materials | MREC → NdPr-oxide + zwaar-REE-carbonaat | 2 kt/j licht REE; geen zware scheiding bij de start | [2][5][6] |

## 6 · Stoppunt
De brief stopt bij de poort van Silmet: daar scheidt Neo het MREC; wat met de oxiden verder gebeurt (o.a. Narva, zie `ree-sillamae-narva`) is een andere stroom. Fase D/E vervalt.

## 7 · Open punten
- **Historische stroom.** Eurostat: 2021-2023 254,5/196,0/331,6 t, 2024 en 2025 ca. 0 [1]; de 10-K 2025 beschrijft dat Energy Fuels nu zelf scheidt [2]. Peiljaar 2023.
- **Geen bron noemt route, haven of modaliteit.** Artikelen noemen alleen containers (eerste container ca. 20 t van een verwachte 15, 7 juli 2021) en White Mesa → Silmet [3][4][5]. Houston/Barbours Cut, de 2.000 km truck en de Estse aanvoerhaven Muuga zijn aannames; alternatief was Port Newark (3.560 km truck).
- **Geen gepubliceerde wegkilometer.** b1 heeft hemelsbreed 1.599,5 km en OSRM 2.056 km; de ±15%-toets is een indicatie. Het ontwerp noemde 1.892 km (zonder Kayenta-omweg).
- **Zee:** zeker niet direct Houston → Muuga; feeder via Rotterdam, Bremerhaven of Gdańsk is waarschijnlijk. MARNET kiest de kortste route; hoeveel overslagen er zijn is niet gemodelleerd.
- **b4 komt uit een andere stroom** (`ree-sillamae-newark`, 176,3 km, andere richting). Bestaat `ree-serraverde-sillamae` tegen de bake, hergebruik dan diens b4-bestand (zelfde weg); anders omgekeerde kopie.
- **Muuga-aanloop is schematisch:** rechte stippel van 37,5 km (maak_havenaanloop liep eerder vast).
- **Volume:** REO-aandeel (ca. 70%) is een aanname; CN 2846 bevat ook andere REE-verbindingen, dus 0,23 kt REO is een bovengrens-indicatie voor deze stroom.
- **Geen Colorado-extract:** de directe route via Cortez (US-491) is korter maar niet te scannen.

## 8 · Bronnen
[1] Eurostat Comext DS-045409, Estland import uit VS, CN 2846 (x100 kg): 2021 2.545, 2022 1.960, 2023 3.316, 2024 0,26; eigen opvraging 2026-11-01. https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/ds-045409?freq=A&reporter=EE&partner=US&product=2846&flow=1
[2] Energy Fuels, Form 10-K FY2025 (MREC 2021-2023 verkocht aan Neo voor scheiding bij Silmet; daarna eigen scheiding). https://www.sec.gov/Archives/edgar/data/1385849/000138584926000009/efr-20251231.htm
[3] North American Mining, Energy Fuels' White Mesa sends rare earths to Estonia (27-09-2021): ca. 20 t RE-carbonaat, 7 juli, White Mesa → Silmet, geen route. https://northamericanmining.com/index.php/2021/09/27/energy-fuels-white-mesa-sends-rare-earths-to-estonia/
[4] Magnetics Business & Technology, Neo Performance Materials and Energy Fuels Begin Shipments (15-07-2021): eerste container onderweg naar Silmet; route, haven, modaliteit niet genoemd. https://magneticsmag.com/neo-performance-materials-and-energy-fuels-begin-shipments-to-launch-us-to-europe-rare-earth-supply-chain/
[5] Energy Fuels, Form 10-Q (30-06-2022): eerste container (ca. 20 t) van een verwachte 15; driejaarscontract, alle MREC naar Silmet. https://www.sec.gov/Archives/edgar/data/1385849/000138584922000037/efr-20220630.htm
[6] Fastmarkets, Neo adds heavy rare earth line, opens EV motor magnet plant (22-09-2025): Silmet 2.000 t/j licht REE, geen zware scheiding. https://www.fastmarkets.com/insights/neo-adds-heavy-rare-earth-line-opens-ev-motor-magnet-plant/
[7] Wikipedia, Barbours Cut Terminal — 29°40′55″N 94°59′54″W (via `ree-larochelle-sanmarcos.md`). https://en.wikipedia.org/wiki/Barbours_Cut_Terminal
[8] OSRM demo-router (OSM), eigen meting 2026-11-01: White Mesa → Barbours Cut via Kayenta/Shiprock/Albuquerque 2.073 km; met de zeven via-punten van §4 2.055,5 km; nearest-snaps per punt. https://router.project-osrm.org/
[9] Wikipedia, Muuga Harbour — HHLA-terminal, 267.752 TEU in 2022; en `ree-sillamae-newark.md` (Muuga-anker, b1-kopie). https://en.wikipedia.org/wiki/Muuga_Harbour
[10] Wikipedia, Estonian national road 1 — Tallinn–Narva 212 km, onderdeel van E20. https://en.wikipedia.org/wiki/Estonian_national_road_1
[11] Briefs `ree-georgia-whitemesa`, `ree-larochelle-sanmarcos`, `ree-kuantan-narva`, `ree-kuantan-pasadena`, `ree-sillamae-newark`, `ree-sillamae-narva` — ankers, kopie-benen, via-punten Kayenta/Shiprock; `v2/design/ree-sitelaag.json`.
[12] Eigen MARNET-dry-run (`hecht_marnet.py route`, scratch): Barbours Cut → knoop 1970 10.746,1 km, 140 MARNET-edges, 1.196 punten, snap 0,019 / 0,000 km; zeeknoop bij Barbours Cut 6228 op 1,6 km.
[13] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-ree-whitemesa-sillamae-{whitemesa,barbours}.png` (z15, 2026-11-01).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
Functie `bak_ree_whitemesa_sillamae` in `v2/tools/bak_stromen.sh`, profiel `ree-whitemesa-sillamae-whitemesa-houston` in `v2/tools/maak_stroombeen_weg.py`; uitvoer `v2/data/stroomroute-ree-whitemesa-sillamae.json` (356,4 KB, versie 2, lonlat). Totaal 12.925,0 km, 4 benen, 17.258 punten, 4 markers.

| # | modaliteit | km | naad | stippel | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 1.965,1 | 0 | nee | eigen wegscan (wegscan_puur, us-utah/-arizona/-new-mexico/-texas), 14.479 punten |
| b2 | zee | 10.746,1 | 0,02 | nee | MARNET Barbours Cut → zeeknoop 1970, snap 0,019 / 0,000 km, geen aanloop |
| b3 | zee | 37,5 | 0,00 | **ja** | rechte schematische stippel, letterlijke kopie van de regel in bak_ree_kuantan_narva |
| b4 | truck | 176,3 | 0,00 | nee | letterlijke kopie van `ree-serraverde-sillamae-weg-muuga-silmet.geojson` (= omgekeerde `ree-sillamae-newark` b1; coordinaten identiek aan de omgekeerde newark-lijn) |

**Toets.** b1 1.965,1 km tegen OSRM 2.056 km (−4,4%) en hemelsbreed 1.599,5 km (ratio 1,23); geen gepubliceerde wegkm, dus de ±15% is een indicatie en ligt erbinnen. b4 176,3 tegen OSRM 178,4 (−1,2%). Grootste naad 0,02 km (zee-snap). Markers 0,0 km van hun lijn. toets_knikken: b1 1 omkering (165,6 graden bij 32.7074, -99.4274, echte bocht, ratio 1,4, geen terugloop); de spikes zitten aan de haven- en fabrieksuiteinden. toets_rechte_benen: alleen de stippel b3 (met reden).

**Aanloop en stippel.** b2 snapt 0,02 km op een track bij Barbours Cut en 0,0 km op zeeknoop 1970: geen haven-aanloop nodig. b3 (stippel, hier reikt het net niet): Muuga-kade ligt 37,5 km van de zeeknoop; maak_havenaanloop is niet opnieuw geprobeerd omdat hij daar eerder op 300 s vastliep (kopie van het bestaande besluit). Geen lucht, leiding, spoor of last mile.

**Recept.** Profiel b1 met 9 via-punten: de 7 uit §4 plus twee toegevoegde (zie hieronder); b2 `--been zee`; b3 `--stippel`; b4 `--been-geojson`. Scans op weg-slot en reus-slot (Texas 445 s), bake op zwaar-slot.

**Afwijkingen van de brief.**
- Twee via-punten toegevoegd t.o.v. §4 (de brief blijft ongewijzigd): `I-20/TX-6 bij Eastland` (32.3758, -98.8308) en `Beltway 8 Noord, Sam Houston Pkwy` (29.9377, -95.4364); beide zijn OSRM-stapcoordinaten op de weg, buiten stadscentra. Reden, gemeten: de eerste scan (zonder, 2.006,7 km) liep de laatste 245 km zuidelijk om Houston via TX-6 en Alvin (tot 42 km naast het OSRM-pad; leg Bryan → Barbours 244,5 km tegen OSRM 196). Met de twee punten is dat tot 26 km naast het OSRM-pad (andere route door Houston) en 1.965,1 km. Dit is geen via-punt om de km-toets te halen: die lag al binnen de norm.
- Open: tussen Abilene en Eastland maakt de scan nog een uitstap via Albany (US-283/US-180, tot 36 km naast het OSRM-pad, 165-graden-bocht bij 32.7074, -99.4274); niet verder bijgesteld (geen tweede via-punt). Gevolg: leg Post → Eastland 325 km tegen ca. 289 bij OSRM.
- b4: brief zei omgekeerde kopie van newark; omdat `ree-serraverde-sillamae-weg-muuga-silmet.geojson` bij het bakken bestond (zelfde coordinaten, hetzelfde 176,3 km) is die gekopieerd naar `ree-whitemesa-sillamae-weg-muuga-silmet.geojson`.

**Lessen.** (1) Vergelijk een wegbeen na de eerste scan met het volledige OSRM-pad (overview=full), niet alleen met de totaallengte: de totaalkm lag in beide scans binnen −2,4% en −4,4%, terwijl de lijn lokaal 42 km uitweek. (2) De ref-voorkeur voor TX 6 trekt de lijn bij Houston zuidwaarts tot voorbij Alvin; een via-punt op Beltway 8 stuurt dat bij. (3) Tijd: wegscan us-texas kost 7,5 min op een reus-slot; een tweede scan met een gewijzigd profiel scant opnieuw (cache is per profielhash).
