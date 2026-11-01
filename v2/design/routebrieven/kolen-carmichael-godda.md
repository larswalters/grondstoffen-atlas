# Routebrief (licht) · Kolen · Carmichael → Abbot Point → Dhamra → Godda (India)

**stroom-id:** `kolen-carmichael-godda` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** thermische kolen van de Carmichael-mijn (Bravus/Adani, Queensland) per **spoor** 368 km naar NQXT Abbot Point (letterlijke kopie van
`kolen-carmichael-abbotpoint`), per **zeeschip** ~8.900 km door de Koraalzee, de Indonesische archipel en de Golf van Bengalen naar Dhamra Port (Adani, Odisha),
per **spoor** ~699 km via Bhadrak, Kharagpur, de Howrah-regio, Bardhaman, Rampurhat, Dumka en Hansdiha naar de Adani Godda-centrale (1.600 MW, Jharkhand) — stoppunt.
**Aannemelijk: één bron** voor de koppeling Carmichael → Godda (IEEFA 2018 en wat daarvan is overgenomen; de EIA noemt ook Indonesië en Zuid-Afrika) [2][3][4].
**Welke as van het verhaal:** *Australische kool voor Bangladesh* — Godda draait op ingevoerde kool en exporteert alle stroom naar Bangladesh; 7–9 Mt kolen per jaar bij
vol bedrijf (EIA 2017, via GEM, projectie, geen gemeten lading) [2]; Carmichael produceerde 12,9 Mt in FY2024/25 [14]. Het Carmichael-aandeel in Godda is niet gepubliceerd.

## 1 · Ketenkaart
```
Carmichael CHPP + laadlus `kolen-carmichael-laad`
   ──(b1 spoor · Carmichael Rail → Newlands → Collinsville → Merinda → Kaili · 368,4 km, kopie)──►
NQXT kolenopslag, Abbot Point `kolen-abbotpoint-terminal`
   ──(b2 stippel 46 km kade → Reef-corridor · b3 zee MARNET ~8.729 km · b4 haven-aanloop Dhamra stippel 113 km, kopie)──►
Dhamra Port `kolen-dhamra-losplaats`
   ──(b5 spoor · Dhamra–Bhadrak → Kharagpur → Howrah-regio → Bardhaman → Rampurhat → Dumka → Hansdiha · ~699 km)──►
Adani Godda Power Plant `kolen-godda-centrale` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Carmichael-laadlus → NQXT kolenopslag | Carmichael Rail → Newlands/GAP-lijn → Collinsville → Merinda → Kaili (LETTERLIJKE KOPIE van `kolen-carmichael-abbotpoint`) | 368,4 gemeten; ~371 gepubliceerd [8] | kopie `spoorroute-kolen-carmichael-abbotpoint-carmichael-abbotpoint.geojson` | nee |
| b2 | B | zee | NQXT-kade → punt in de Reef-corridor (-19.5523,148.3180) | uitvaart Abbot Point | 46 (hemelsbreed) | rechte lijn | **ja**: kade 146 km van zeeknoop 9023, haven-aanloop hangt, rechte lijn naar 9023 is 64% land |
| b3 | B | zee | Reef-corridor → zeeknoop 2373 (21.0,88.0) | Koraalzee → Indonesische archipel (MARNET kiest) → Golf van Bengalen (aannemelijk: één bron) | 8.729,2 (MARNET, afgeleid) | `maak_zeebeen_kolen_carmichael_godda.py` | nee |
| b4 | B | zee | zeeknoop 2373 → Dhamra-losplaats | haven-aanloop Dhamra (kade 109,7 km van de zeeknoop) | 113,3 (kopie) | kopie `kolen-goonyella-kalinganagar-aanloop-dhamra.geojson` | **ja**: MARNET reikt niet tot Dhamra |
| b5 | C | spoor | Dhamra-losplaats → Godda-centrale | Dhamra–Bhadrak (62 km, 2011) → Kharagpur → Santragachi/Howrah-regio → Bardhaman → Rampurhat → Dumka → Hansdiha → Godda (namen afgeleid uit het OSM-pad) | 698,7 gemeten (router 694,9) tegen ~700 gepubliceerd (IEEFA 2018): −0,2% [3][4] | toets_spoorroute (india.geojson), zonder via-punten | nee; 0,6 km spoor-naar-anker < 2 km |

Het zeebeen heet in de bake "zeeschip NQXT Abbot Point → Dhamra-zeeknoop (MARNET, Koraalzee → Indonesië → Golf van Bengalen, aannemelijk: één bron)". Het eerste stuk van de MARNET-lijn is knoop 9009 (-20.8152,150.1694) tot vertex 24; dat stuk ligt in open zee buiten de kade en wordt niet getekend.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-carmichael-laad` | mijn / laadlus | Carmichael: wasserij, kolenopslag en treinlaadlus | -22.0215, 146.4088 | HERGEBRUIK letterlijk uit `kolen-carmichael-abbotpoint` [8] | bron-gelegd (z16 daar gezien: wasserij en kolenopslag, spoorlus 40 m van het punt) |
| `kolen-abbotpoint-terminal` | overslag spoor → zee | NQXT kolenopslag, zuidkop, Abbot Point | -19.8999, 148.0774 | HERGEBRUIK letterlijk uit `kolen-carmichael-abbotpoint` [8] | bron-gelegd (z15/z16 daar gezien: stockyards, spoorlus, pier noordwaarts) |
| `kolen-dhamra-losplaats` | losplek zee / laadplek spoor | Dhamra Port, kolenstockyard + jetty | 20.8280, 86.9600 | HERGEBRUIK letterlijk uit `kolen-goonyella-kalinganagar` [10][9] | bron-gelegd (z15 daar gezien: ovale stockyard met spoorlus, conveyor naar jetty met twee schepen) |
| `kolen-godda-centrale` | afnemer / centrale | Adani Godda Power Plant (2×800 MW), Motia, Godda | 24.8141, 87.1355 | GEM [2] (Wikipedia 24.8175, 87.1361 [1], ~0,4 km noordelijker) | bron-gelegd (z15 gezien: bebouwd complex met grote hallen en ketelgebouwen, ruime vlakte (kolenpark/asdam) ten NO, spoorbundel loopt vanuit het NO het terrein op; punt ligt op de westrand van het hallencomplex) |

Zeeknoop Dhamra: 2373 (21.0,88.0), 109,7 km uit de kade (> 5 km: haven-aanloop, zie b4). Zeeknoop bij Abbot Point: 9023 (-19.2619,146.8584), 146 km: niet gebruikt (zie b2).

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen via-punten. Het vrije kortste pad over het 1-op-1-spoornet (Dhamra → Godda) is 694,9 km, 0 bochten ≥ 60° na de keerstraf, −0,7% tegen ~700 km [4]; de vrije route
raakt de corridorplaatsen zonder dat er een punt nodig is. Gemeten afstand van de lijn tot: Balasore 1,7 km, Santragachi 0,4, Howrah 2,2, Bardhaman 1,8, Rampurhat 0,7,
Dumka 2,3, Hansdiha 0,2, Godda 1,9 km. Bhadrak 3,6 km en Kharagpur Jn (22.339, 87.320) 0,2 km.
Het enige echte alternatief (via Adra/Dhanbad) zou ~100 km omlopen en staat niet in een bron.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Carmichael CHPP + laadlus | Bravus (Adani) | ruwe kolen → thermisch product | 12,9 Mt FY2024/25 (nameplate 15 Mtpa) | [14][8] |
| NQXT Abbot Point | NQXT, Adani-beheer | trein → stockyard → pier | niet gevonden | [8] |
| Dhamra Port | Adani Ports & SEZ | zee → stockyard → spoor | 43 Mt cargo in 2023-24 (haven totaal, alle ladingen) | [9] |
| Adani Godda Power Plant | Adani Power Jharkhand | kolen → stroom voor Bangladesh | 1.600 MW (2×800 MW); kolenbehoefte 7–9 Mt/j (projectie) | [1][2][13] |

## 6 · Stoppunt
De brief stopt bij de Godda-centrale: de kolen worden daar verstookt en de stroom gaat per hoogspanningslijn via Farakka naar Bangladesh [1]; er is geen kolenstroom naar een volgende fysieke locatie.
Fase D (de stroomexport naar Bangladesh) is geen goederenstroom van kolen en wordt niet getekend.

## 7 · Open punten
- **Koppeling is aannemelijk, niet gemeten:** alleen IEEFA 2018 (en bronnen die dat overnemen) koppelt Carmichael aan Godda [3][4][5]; EIA 2017 noemt Indonesië, Zuid-Afrika en Australië als bronnen [2][3]. Geen scheepsregister van een Carmichael-lading naar Dhamra gevonden. Het Dhamra-spoor naar Godda is wel een gedocumenteerde route [3].
- **Volume Carmichael → Godda niet gepubliceerd:** 7–9 Mt/j is de kolenbehoefte van de centrale bij vol bedrijf (projectie, 2017), geen werkelijke import uit Carmichael.
- **Godda draait onder capaciteit in 2026:** Adani meldt (2 september 2026) minder kool per spoor door "severe railway congestion and multiple loading restrictions"; Bangladesh ontving rond 900 MW van 1.600 [6][2].
- **Zeeroute door MARNET gekozen:** via de Indonesische archipel (Torres-straat of noord-om-PNG niet afgedwongen); 8.729 km is afgeleid, geen operatorcijfer.
- **Haven-aanloop NQXT niet te routeren:** 146 km tot zeeknoop 9023, `maak_havenaanloop.py` hangt (3 runs 200–300 s); b2 is een rechte stippel van 46 km naar de eerste MARNET-vertex in de Reef-corridor.
- **Spoor-km is vrije kortste-pad:** de Dhamra → Godda-lijn is niet via-punten bevestigd; namen van tussenstations zijn afgeleid uit de OSM-geometrie. Gepubliceerd is alleen "~700 km" [3][4].
- **Overlap met bestaande stromen is hoog (~90% van de km):** b1 is 100% kopie van `kolen-carmichael-abbotpoint`, de MARNET-zeelijn volgt na de Koraalzee dezelfde edges als `kolen-goonyella-kalinganagar`, en de Dhamra-aanloop en de eerste ~62 km spoor delen met Goonyella. Uniek zijn ~630 km spoor en de aanvaart.
- **Centrale-coördinaat:** GEM 24.8141, 87.1355 (gebruikt) versus Wikipedia 24.8175, 87.1361; verschil ~0,4 km, beide op het complex.

## 8 · Bronnen
[1] Wikipedia, Godda Thermal Power Station: 2×800 MW, Adani Power, units 2023, kolen uit Australië (Carmichael) via Dhamra, 7–9 Mt/j, stroom naar Bangladesh via Farakka, 24°49′03″N 87°08′10″E. https://en.wikipedia.org/wiki/Godda_Thermal_Power_Station
[2] Global Energy Monitor, Adani Godda power station: 24.814107, 87.135465; operating 2023; EIA 2017 bronnen Indonesië/Zuid-Afrika/Australië; Dhamra; ~700 km spoor (IEEFA 2018); 7–9 Mtpa; kolenkrapte mid-aug 2026. https://www.gem.wiki/Adani_Godda_power_station
[3] BankTrack, Adani Godda Thermal Power Project: kolen uit Australië, Indonesië, Zuid-Afrika, "troubled Carmichael"; Dhamra; ~700 km spoor; 7–9 Mtpa. https://banktrack.org/project/adani_godda_thermal_power_project
[4] IEEFA, Adani Godda power project: too expensive, too late and too risky for Bangladesh (2018): kolen van Carmichael via Dhamra, ~700 km per spoor (gelezen via zoekresultaat en [2][3]; directe fetch gaf 403). https://ieefa.org/resources/adani-godda-power-project-too-expensive-too-late-and-too-risky-bangladesh
[5] IEEFA, Carmichael coal will add pressure for power tariff hikes in Bangladesh (zoekresultaat; Mundra als eerder beoogde afnemer van Carmichael-kool). https://ieefa.org/articles/carmichael-coal-will-add-pressure-power-tariff-hikes-bangladesh-not-reduce-poverty
[6] The Financial Express (BD), Adani cuts power supply to Bangladesh due to coal transport disruption (2 sept 2026): railcongestie, onder 900 MW. https://thefinancialexpress.com.bd/trade/adani-cuts-power-supply-to-bangladesh-due-to-coal-transport-disruption
[7] Wikipedia, Carmichael coal mine: 10 Mt/j (gedownsized van 60), eerste export 29-12-2021, Abbot Point; geen afnemers genoemd. https://en.wikipedia.org/wiki/Carmichael_coal_mine
[8] Eigen brief `kolen-carmichael-abbotpoint.md` (M31 golf 12): ankers Carmichael-laadlus en NQXT, 368,4 km spoor, bronnen daar [1]–[11]. `v2/design/routebrieven/kolen-carmichael-abbotpoint.md`
[9] Wikipedia, Dhamra Port: 20°49′24″N 86°57′46″E, Adani Ports & SEZ, 62 km spoor Dhamra–Bhadrak (2011), 43 Mt in 2023-24. https://en.wikipedia.org/wiki/Dhamra_Port
[10] Eigen brief `kolen-goonyella-kalinganagar.md`: anker Dhamra-losplaats, haven-aanloop 113,3 km, Bhadrak. `v2/design/routebrieven/kolen-goonyella-kalinganagar.md`
[11] OpenStreetMap (ODbL) via `v2/build-cache/raw1op1/india.geojson` en `toets_spoorroute.mjs`: `spoorroute-kolen-carmichael-godda-dhamra-godda.geojson` (698,7 km, 1.058 punten).
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-kolen-carmichael-godda-plant.png`.
[13] Adani Power, Godda Jharkhand (1.600 MW, 12 centrales, 18.110 MW thermisch). https://adanipower.com/operational-power-plants/Godda-Jharkhand
[14] Adani Enterprises annual report 2025 en Argus (Carmichael 12,9 Mt FY2024/25), overgenomen uit [8]. https://connect.adani.com/annual_report/2025/ael/commercial-mining-business.html

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
`bash v2/tools/bak_stromen.sh kolen-carmichael-godda` -> `v2/data/stroomroute-kolen-carmichael-godda.json` (63,2 KB, versie 2, lonlat, modaliteiten spoor en zee), functie `bak_kolen_carmichael_godda`. Geen profiel, geen extract, geen nieuwe spoorrun: alle vijf benen bestonden al in `v2/build-cache/ais/graaf/`.

| # | modaliteit | km | punten | naad naar vorige | geometrie |
|---|---|---|---|---|---|
| 1 | spoor | 368,4 | 1.239 | 0 | letterlijke kopie `spoorroute-kolen-carmichael-abbotpoint-carmichael-abbotpoint.geojson` (brief ~371 gepubliceerd, -0,7%) |
| 2 | zee, stippel | 46,1 | 2 | 0,20 | rechte uitvaart NQXT -> Reef-corridorpunt (-19.5523,148.3180) |
| 3 | zee | 8.729,2 | 892 | 0,00 | `kolen-carmichael-godda-zee-marnet.geojson` (MARNET, afgeleid) |
| 4 | zee, stippel | 113,3 | 53 | 0,00 | letterlijke kopie `kolen-goonyella-kalinganagar-aanloop-dhamra.geojson` |
| 5 | spoor | 698,7 | 1.058 | 0,48 | `spoorroute-kolen-carmichael-godda-dhamra-godda.geojson` (~700 gepubliceerd, -0,2%) |

Totaal 9.955,7 km, 3.244 punten, 4 markers (Carmichael-laadlus, NQXT, Dhamra, Godda-centrale; afstand tot de lijn 0,01 / 0,0 / 0,0 / 0,64 km). Grootste naad 0,48 km (Dhamra-losplaats naar het begin van het spoor, procesgat, < 5 km). Geen via-punten, geen extracts, geen weg- of luchtbeen.

**Stippels (zee).** b2: de NQXT-kade ligt 146 km van zeeknoop 9023 en `maak_havenaanloop.py` hangt; de rechte lijn is dus de stippel "hier reikt het net niet" en eindigt op het eerste punt van de MARNET-lijn in de Reef-corridor. b4: de Dhamra-kade ligt 109,7 km van zeeknoop 2373 (21.0,88.0); de bestaande aanloop van Goonyella wordt hergebruikt. Het gemeten zeebeen b3 is doorgetrokken; "aannemelijk: een bron" staat in de beennaam.

**Toetsen.** Km: b1 en b4 zijn kopieen, b5 -0,2% tegen ~700 km (binnen de +-15%). `toets_knikken.py`: 0 omkeringen, 3 knikken, allemaal in het MARNET-zeebeen b3 (61,4 gr bij -10.4499,143.0198 in de Torres-straat, twee spikes met 15 m boogstraal bij -4.5798,114.1001 in de Javazee); OSM- of MARNET-geometrie, geen reparatie. `toets_rechte_benen.py --min-km 5`: alleen b2, de bedoelde stippel. `json.load` slaagt.

**Recept.** b1 en b4 letterlijke kopieen (noem in de beennaam), b3 en b5 uit de eerdere tussenuitvoer van deze brief (zeebeen `maak_zeebeen_kolen_carmichael_godda.py`, spoor `toets_spoorroute.mjs` zonder via-punten met `BAKE_SUFFIX=-raw`). Ankers uit de brief, geen nieuwe satellietblik nodig (hergebruik + `sat-kolen-carmichael-godda-plant.png`).

**Lessen.** (1) Een keten van vijf bestaande bouwstenen bakt in een run: de hele klus is de functie met de juiste kopieen. (2) Het spoor Dhamra -> Godda zit niet in een bron per tussenstation; het is een vrij kortste pad, de Godda-koppeling blijft een bron (IEEFA 2018). (3) Een MARNET-spike in de Javazee en een krappe bocht in de Torres-straat zijn eigenschappen van het zeenet, niet van deze stroom.
