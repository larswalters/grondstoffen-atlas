# Routebrief (licht) · kolen — EMO-terminal (Rotterdam) → Rijn → Grosskraftwerk Mannheim (Duitsland)

**stroom-id:** `kolen-rotterdam-mannheim` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** steenkool die via de EMO-terminal op de Maasvlakte binnenkomt gaat per duwstel/binnenschip ca. 620 km stroomopwaarts (Nieuwe Maas, Merwede, Waal, Boven-Rijn, Midden-Rijn tot de Oberrhein bij Mannheim) naar de eigen kolenkade van het Grosskraftwerk Mannheim (GKM, Rijn-oever Neckarau).
**Welke as van het verhaal:** *Importkant Duitsland, de Boven-Rijn op naar de Zuid-Duitse kolencentrale* — GKM (1.958 MW netto) is de grootste energielocatie van Baden-Württemberg [1]; een groot deel van wat de Mannheimer havens overslaan is steenkool voor het GKM [2] (havens totaal ca. 8 Mt/j, 8,1 Mt in 2015 [4]). Volume GKM-kolen: **geen bron-tonnage**; indicatie ca. 2,7 Mt/j (peiljaar 2010: 6,5 Mt CO2 volgens PRTR [1] gedeeld door aangenomen 2,4 t CO2 per t steenkool — eigen afleiding). Herkomst EMO is **aannemelijk: één bron** (zie §7).

## 1 · Ketenkaart
```
EMO-kolenkade, Maasvlakte `kolen-emo-kade` (hergebruik)
  ──(b1-b4 binnenvaart · Oude Maas/Merwede/Waal tot Pannerdensche Kop · 172,3 km · letterlijke kopie kolen-cerrejon-ruhr)──►
Pannerdensche Kop ──(b5 binnenvaart · Waal/Boven-Rijn/Midden-Rijn, Duisburg-Keulen-Mainz-Worms · 446,8 km · bulklaag)──►
Rijn-knoop 2,6-4,3 km voor de kade ──(b5a stippel · kade-aanloop GKM · ca. 4,3 km hemelsbreed)──► GKM-kolenkade `kolen-gkm-kade` ⏹
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | binnenvaart | EMO-oostzijde → Groothoofd | Oude Maas, Noord NIET nemen; **kopie** kolen-cerrejon-ruhr | 55,0 (gemeten) | AIS-graaf rijn | nee |
| b2 | C | binnenvaart | Groothoofd → Werkendam | Nieuwe Merwede NIET nemen; **kopie** | 22,6 | AIS-graaf rijn | nee |
| b3 | C | binnenvaart | Werkendam → Loevestein | monding Afgedamde Maas; **kopie** | 9,5 | AIS-graaf rijn | nee |
| b4 | C | binnenvaart | Loevestein → Pannerdensche Kop | Pannerdensch Kanaal NIET nemen; **kopie** | 85,2 | AIS-graaf rijn | nee |
| b5 | C | binnenvaart | Pannerdensche Kop → Rijn-knoop bij Mannheim | Waal, Boven-Rijn, Midden-Rijn via Duisburg, Keulen, Koblenz, Mainz, Worms | 446,8 gemeten (71 edges); Rijn-km 867 → ca. 425 = ca. 442 (ontwerp, geen bronwaarde) | maak_rivierbeen (bulklaag) | nee |
| b5a | C | binnenvaart | Rijn-knoop (49.4451, 8.4505) → GKM-kade | kade-aanloop langs de Rijn-oever | ca. 4,3 hemelsbreed | rechte stippel | **ja**: bulklaag-edge niet doorsneden |

Totaal ca. 623 km (172,3 + 446,8 + ca. 4,3). Tegen ontwerp ca. 600 km / Rijn-km 442: +2% voor b5; geen gepubliceerde totaalafstand: ±15% is indicatie, geen norm.
Geen AIS-tracks boven Duisburg (collector dekt de Rijn tot Duisburg): b5 zegt waar het water ligt, niet dat een schip er gezien is. Geen zee, spoor, weg, leiding, lucht, haven-aanloop (geen zeebeen) of last-mile-been.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-emo-kade` | overslag / laadplek | EMO-kolenterminal, Mississippihaven, Maasvlakte (HERGEBRUIKT als `coal-rotterdam-kade`) | 51.9411, 4.0535 | [7][8] | bron-gelegd (anker van kolen-cerrejon-ruhr, sitelaag `w-rotterdam`, niet opnieuw gelegd); routeerpunt b1 51.937, 4.060 ligt ca. 0,6 km ernaast: anker ≠ routeerpunt |
| `kolen-gkm-kade` | losplek / eigen kolenkade GKM | Kolenkade Block 9 (kranen, kolenpark erachter) op de oostelijke Rijn-oever, Mannheim-Neckarau/Rheinau | 49.4390, 8.5097 | [3][5][9] | bron-gelegd (z17 gezien: ca. 500 m kade met kraanrails langs de Rijn, groot zwart kolenpark erachter, kolenschip aan de kade, transportband naar Block 9; OSM noemt dit terrein "Großkraftwerk Mannheim") |

Alternatief niet gekozen: het oudere kolenpark west van Block 8 met kade/lossers 49.4452, 8.4958 (z17: zwart kolenpark direct aan de Rijn). Welke van de twee kades de lading ontvangt is niet gebronnen. Het ontwerp-punt GKM-centrum 49.4457, 8.4904 ligt op de ketelhuizen, geen kade. De ontwerp-kandidaten 49.4412, 8.5069 (conveyor) en 49.4383, 8.5124 (kolenopslag) liggen op dezelfde Block 9-strook; 49.4390, 8.5097 is het midden van de kade.

## 4 · Via-punten
Geen eigen via-punten. De corridorkeuzes (Noord, Nieuwe Merwede, Pannerdensch Kanaal NIET nemen) zitten in de 4 AIS-benen b1-b4 (kopie). Boven de Pannerdensche Kop is er één Rijn: b5 is het kortste pad over de bulklaag, van 51.874, 6.038 naar knoop 49.4451, 8.4505 (4,33 km voor de kade).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Grosskraftwerk Mannheim (Blokken 1-9) | RWE Generation 40%, EnBW 32%, MVV RHE 28% | steenkool → stroom (50 Hz + bahnstroom) en fernwarme | 1.958 MW netto (Block 9 in bedrijf 2015); 2010: ca. 6,5 Mt CO2 | [1][3] |
| Mannheimer havens | Hafen Mannheim | scheepsgoederen; groot deel steenkool voor GKM | ca. 8 Mt/j totaal (8,1 Mt in 2015) | [2][4] |

## 6 · Stoppunt
De brief stopt bij de kolenkade van het GKM: de kool wordt verbrand tot stroom, warmte en bahnstroom, er is geen volgende fysieke locatie van de lading (transportband op eigen terrein is geen been). Fase D/E vervallen.

## 7 · Open punten
- **Alleen één bron voor de aanvoer:** Rheinpfalz (2019) zegt dat de Mannheimer havens grotendeels steenkool voor het GKM overslaan [2]; geen bron noemt Rotterdam of EMO als laadhaven en geen bron noemt het herkomstland. De bewering "per schip uit overzee" (ontwerp) kon ik niet terugvinden: de heidelberg24-pagina gaf 404. DB Cargo levert volgens de haalbaarheidstoets [6] ook per spoor, en [3] zegt "auf dem Wasser und Schienenweg". Daarom **aannemelijk: één bron voor GKM-aanvoer per schip; laadhaven EMO aangenomen**.
- **Tonnage GKM niet gevonden** (staat niet op gkm.de); de 2,7 Mt/j is een eigen afleiding uit PRTR-CO2 2010 en kan nu lager liggen.
- **Welke kade** (Block 9 oost of het oude kolenpark west) ontvangt de schepen is niet gebronnen; ontwerp-punt "GKM-centrum" is geen kade.
- **Ontwerp-aanname "zijwater" klopt niet:** GKM ligt aan de Rijn zelf; het router-eindpunt valt 4,3 km vóór de kade omdat het watersegment één lange bulklaag-edge is (b5a stippel, reden in de beennaam).
- **Geen gepubliceerde vaarafstand** EMO-GKM; Rijn-km 425 voor de kade is ontwerp, niet gelezen in een bron.
- Laagwater (Kaub) beperkt de beladingsgraad; volume blijft indicatief [2].

## 8 · Bronnen
[1] de.wikipedia, Grosskraftwerk Mannheim — Steinkohle, 1958 MW netto, eigenaren, Block 9 (2015), 2010 ca. 6,5 Mt CO2 (PRTR). https://de.wikipedia.org/wiki/Grosskraftwerk_Mannheim
[2] Rheinpfalz, Drehscheibe in die Welt (9-1-2019) — Mannheimer havens ca. 8 Mt/j en 8.000 schepen, een groot deel steenkool voor het Großkraftwerk, laagwater 2018. https://www.rheinpfalz.de/startseite_artikel,-drehscheibe-in-die-welt-_arid,1352964.html
[3] Implenia, referentie Grosskraftwerk Mannheim (Marguerrestr. 1) — steenkool per water en spoor, kolenlager, -lossing en kaimauer, 380 m lossectie met portaalkranen, bouw 2009-2015. https://implenia.com/de-at/referenzen/detail/ref/grosskraftwerk-mannheim
[4] en.wikipedia, Mannheim Harbour — waterzijdige overslag 8,1 Mt (2015), vier havengebieden. https://en.wikipedia.org/wiki/Mannheim_Harbour
[5] OSM via Nominatim reverse (2026-10-31) — terrein langs Kohlestraße en Hafenstraße is "Großkraftwerk Mannheim", ook bij 49.4412, 8.5069. https://nominatim.openstreetmap.org
[6] Haalbaarheidstoets kolen-rotterdam-mannheim (2026-10-31): maak_rivierbeen 446,8 km, 71 edges, eindknoop 49.4451, 8.4505; GKM-kade niet gelegd.
[7] `v2/design/routebrieven/kolen-cerrejon-ruhr.md` en `v2/tools/bak_stromen.sh` `bak_kolen_cerrejon_ruhr` — EMO-anker en de vier binnenvaartbenen. [8] `v2/design/kolen-sitelaag.json` site `w-rotterdam`.
[9] Esri World Imagery via `v2/tools/sat_check.py` (2026-10-31) — `v2/build-cache/satcheck/sat-kolen-rotterdam-mannheim-gkm-kade-blok9.png` (z17), `-gkm-kade-west.png` (z17), `-gkm-kohlelager.png` (z16), `-gkm-kade.png`, `-gkm-kraan.png`, `-gkm-conveyor.png`, `-gkm-blok9.png` (z15); route `v2/build-cache/ais/graaf/kolen-rotterdam-mannheim-rivier-pannerdensche-gkm.geojson`.
[10] olie-rotterdam-basel (brief + `bak_olie_rotterdam_basel`) — zelfde kopie van de vier AIS-benen en bulklaag-Rijn.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Recept:** `bash v2/tools/bak_stromen.sh kolen-rotterdam-mannheim` (functie `bak_kolen_rotterdam_mannheim`) → `v2/data/stroomroute-kolen-rotterdam-mannheim.json` (47,3 KB, versie 2, lonlat). Titel: Kolen · EMO (Rotterdam) → Rijn → Grosskraftwerk Mannheim. Register (centraal): sleutel `kolen-rm`, label EMO Rotterdam → Mannheim.

| # | modaliteit | km gebakken | punten | naad | opmerking |
|---|---|---|---|---|---|
| 1 | binnenvaart | 55,0 | 147 | 0 | kopie kolen-cerrejon-ruhr (AIS-graaf rijn), EMO-oostzijde → Groothoofd |
| 2 | binnenvaart | 22,6 | 36 | 0,00 | kopie, Groothoofd → Werkendam |
| 3 | binnenvaart | 9,5 | 19 | 0,00 | kopie, Werkendam → Loevestein |
| 4 | binnenvaart | 85,2 | 161 | 0,00 | kopie, Loevestein → Pannerdensche Kop |
| 5 | binnenvaart | 447,1 | 2390 | 0,47 | bulklaag (vooraf gebakken kolen-rotterdam-mannheim-rivier-pannerdensche-gkm.geojson) |
| 6 | binnenvaart, stippel | 4,3 | 2 | 0,00 | kade-aanloop GKM, rechte stippel |

Totaal 623,7 km · 2.755 punten · 2 markers (EMO-kade 51.94109,4.05354; GKM-kade 49.4390,8.5097). Grootste naad 0,47 km (b4 → b5, Pannerdensche Kop), ruim onder de 5 km.

**Toelichting.**
- **Kopie b1-b4:** de vier `--been`-regels zijn letterlijk overgenomen uit `bak_kolen_cerrejon_ruhr` (identiek aan `bak_olie_rotterdam_basel`); km 55,0 / 22,6 / 9,5 / 85,2 komen exact overeen met de brief (172,3 km).
- **b5 (bulklaag):** 447,1 km in de bake tegen 446,8 in de brief (maak_rivierbeen, 71 edges); geen gepubliceerde vaarafstand, dus de ±15%-toets is indicatie: ontwerp ca. 442 km (+1%). Boven Duisburg zijn geen AIS-tracks: dit been zegt waar het water ligt, niet dat een schip er gezien is.
- **Stippel b6 (kade-aanloop):** de router eindigt 4,33 km vóór de kade door één lange bulklaag-edge; rechte stippel 49.4451,8.4505 → 49.4390,8.5097 (4,334 km), schematisch. Geen haven-aanloop-tool (die hing eerder, geen tweede poging).
- **Marker EMO** ligt 0,61 km van de lijn (anker 51.94109,4.05354 ≠ routeerpunt 51.937,4.060: anker ≠ routeerpunt, zoals in kolen-cerrejon-ruhr); marker GKM-kade 0,0 km (het stippeleinde).
- **Aannemelijk: één bron** (Rheinpfalz 2019) staat in beennaam b1 en in de markernaam GKM; de lijnstijl is doorgetrokken.
- **toets_knikken:** knikken en één terugloop zitten in b1-b4 en zijn precies die van de bestaande kolen-cerrejon-ruhr en olie-rotterdam-basel (letterlijke kopie, niet aangeraakt); b5 heeft 0 knikken en 0 omkeringen. `toets_rechte_benen --min-km 5`: geen treffer voor deze stroom.
- **Lessen/open:** het rivierbeen was vooraf gebakken (haalbaarheidstoets), dus geen slot voor een rekenrun nodig buiten de bake zelf; GKM-kade Block 9 oost versus oud kolenpark west blijft niet gebronnen.
