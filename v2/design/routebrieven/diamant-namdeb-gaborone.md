# Routebrief (licht) · diamant — Namdeb/Debmarine (Namibië) → Windhoek → Antwerpen (België)

**stroom-id:** `diamant-namdeb-gaborone` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** Namibische mariene ruwe diamant (Debmarine Namibia, recovery-schepen voor de Sperrgebiet-kust) komt per helikopter aan land bij Namdeb in Oranjemund, gaat per truck ~900 km naar de NDTC/Namdeb-sortering in Windhoek, vandaar per truck naar Hosea Kutako Airport (WDH), vliegt als vrachtvlucht (grootcirkel) naar Sheremetyevo-achtige G7-poort Brussels Airport (BRU, Brucargo) en tot slot per truck naar AWDC Antwerpen voor G7-certificering en handel.
**Welke as van het verhaal:** *Namibië (Namdeb/Debmarine, marien) → Windhoek → hoogste waarde/karaat ter wereld.* **Afwijking van het ketenontwerp, bindend uit de haalbaarheidstoets**: de oorspronkelijke bestemming Gaborone is **vervangen door Antwerpen** — er is geen bron gevonden dat Namibische rough standaard naar Botswana doorvliegt (zie §7); NDTC is een eigen 50/50-JV die in Windhoek zelf sights houdt (Wikipedia, bevestigd bij het schrijven). Antwerpen/AWDC is het hergebruikte anker uit `diamant-ekati-antwerpen.md`. Jaarvolume: **~2 Mct/jr ruw** (Namdeb/Debmarine, ~2% wereldvolume) maar de **hoogste $/karaat van alle grote producenten** — design/diamant.md §3a.

## 1 · Ketenkaart
```
Debmarine-schepen (Sperrgebiet-kust, geen vast punt) ┄(helikopter, 3×/week, niet getekend — zie §7)┄►
Namdeb-terrein `dia-namdeb-oranjemund` ──(b1 truck · B4/B1 via Rosh Pinah–Aus–Keetmanshoop–Mariental–Rehoboth · ~900 km)──►
NDTC/Namdeb-sortering `dia-ndtc-windhoek` ──(b2 truck · B6 · ~40 km)──►
Hosea Kutako Airport (WDH) `dia-wdh-cargo` ──(b3 lucht · vlucht WDH → BRU, grootcirkel · ~8.260 km)──►
Brussels Airport Brucargo `dia-brucargo` ──(b4 truck · E19 · ~35 km)──►
Antwerpen AWDC/Diamond Office `dia-awdc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Namdeb-terrein Oranjemund → NDTC/Namdeb-sortering Windhoek | B4 (Oranjemund-omgeving → Rosh Pinah → Aus → Keetmanshoop) → B1 (Keetmanshoop → Mariental → Rehoboth → Windhoek) | ~900 hemelsbreed via de via-keten (gemeten, §4); ontwerp noemt ~900 [ontwerp] | maak_stroombeen_weg | nee |
| b2 | A | truck | NDTC/Namdeb-sortering Windhoek → Hosea Kutako Airport (WDH) | B6, oostwaarts uit Windhoek | ~40 hemelsbreed (gemeten); Wikipedia noemt de luchthaven "45 km ten oosten van de stad" [6] | maak_stroombeen_weg | nee |
| b3 | B | lucht | Hosea Kutako Airport (WDH) → Brussels Airport (BRU) Brucargo | vlucht WDH → BRU, grootcirkel, geen tussenlanding gebrond | 8.259,7 (gemeten, grootcirkel) | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | Brucargo (BRU) → Antwerpen AWDC/Diamond Office | E19 (Zaventem/Machelen → Vilvoorde → Mechelen → Antwerpen-Zuid) — zelfde corridor als `diamant-ekati-antwerpen` | ~35 hemelsbreed (gemeten); ~40 in de zusterbrief [7] | maak_stroombeen_weg | nee |

Fase C (b4) is het ontbrekende laatste been dat de haalbaarheidstoets eist (geen keten die op de luchthaven zelf eindigt) — letterlijk hergebruikt van `diamant-ekati-antwerpen.md` b3.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-namdeb-oranjemund` | mijn/aanvoerpunt (marien, helikopterlanding) | Namdeb-kantoor/terrein, Oranjemund | -28.55284, 16.42375 | [1][8][10] | aannemelijk (z15 gezien: kantoorpand middenin het woon-/bedrijvenweefsel van Oranjemund, OSM `office=company` "MRM Namdeb"; het exacte helikopter-landingsterrein voor de mariene lading is niet gebrond, zie §7) |
| `dia-ndtc-windhoek` | verwerkingsknoop (sortering/sight) | NDTC/Namdeb-kantoor, Frans Indongo Street, Windhoek Central | -22.56482, 17.08384 | [2][9][10] | bron-gelegd (z15 gezien: kantoorpand in het centrale zakendistrict van Windhoek, past bij "in Windhoek zelf sights houdt" [2]; OSM-building "Namdeb") |
| `dia-wdh-cargo` | vrachtterminal (vertrek lucht) | Hosea Kutako International Airport (WDH), terminal-/vrachtapron | -22.4863, 17.4643 | [3][10] | aannemelijk (z16-z17 gezien: platform met meerdere breedromptoestellen naast het terminalgebouw; een apart vrachtgebouw is op deze kleine luchthaven niet los van de passagiersapron te onderscheiden, zie §7) |
| `dia-brucargo` | vrachtterminal (aankomst B, vertrek truck) | Brucargo, Brussels Airport | 50.90628, 4.45584 | [4][7] | bron-gelegd (hergebruikt anker uit `diamant-ekati-antwerpen.md`: z15 gezien, vrachttoestellen op het platform naast loodsen, OSM-landuse "Brucargo") |
| `dia-awdc` | handels-/certificeringshub (eindpunt) | AWDC / Diamond Office, Hoveniersstraat, Antwerpen | 51.21520, 4.41870 | [5][7] | bron-gelegd (hergebruikt anker uit `diamant-ekati-antwerpen.md`: z15 gezien, dicht stedelijk bouwblok in de Diamantwijk) |

## 4 · Via-punten (alleen b1 — de enige lange landcorridor met een aantoonbare route)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Rosh Pinah | -27.9650, 16.7600 | mijnstadje waar de lokale weg vanuit Oranjemund op de doorgaande B4 aansluit (OSM-plaats) |
| b1 | 2 | Aus | -26.6667, 16.2667 | de B4 buigt hier van zuidwest naar oost richting Keetmanshoop (OSM-plaats, spoorwegknoop) |
| b1 | 3 | Keetmanshoop | -26.5786, 18.1333 | wisselpunt B4 → B1: enige doorgaande noord-zuidcorridor in Zuid-Namibië (OSM-plaats) |
| b1 | 4 | Mariental | -24.6333, 17.9667 | de B1 passeert hier de enige stad tussen Keetmanshoop en Windhoek (OSM-plaats) |
| b1 | 5 | Rehoboth | -23.3167, 17.0833 | laatste doorgaande plaats vóór Windhoek op de B1 (OSM-plaats) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| NDTC/Namdeb-sortering, Windhoek | NDTC (50/50 Namibië/De Beers-DTC) | ruwe (mariene + land-)diamant → gesorteerd/gewaardeerd, sight-allocaties aan sightholders | ~2 Mct/jr (Namdeb/Debmarine totaal) [2][9] | [2][9] |
| AWDC/Diamond Office, Antwerpen | AWDC (overheid + sector) | rough/polished diamant → import/export, G7-certificering | ~1.800 aangesloten handelaren [5] | [5] |

Beide knopen zijn **administratief/sortering**, geen fysieke slijperij (die zit overwegend in Surat, India — buiten deze keten, zie stoppunt).

## 6 · Stoppunt
De brief stopt bij AWDC/Diamond Office in Antwerpen: dit is het G7-certificerings-/handelsknooppunt waar de haalbaarheidstoets naartoe stuurt bij gebrek aan een Gaborone-bron, en er is geen bron die een specifieke vervolgbestemming (slijperij) aan Namdeb/Debmarine-rough koppelt — fase D vervalt.

## 7 · Open punten
- **Grootste open punt (ongewijzigd uit het ontwerp): de fysieke aanvoer van marien naar het vasteland is niet gebrond op de meter.** Wél nieuw gevonden (De Beers Group, 2022 [8]): Debmarine's recovery-schepen verzegelen het diamantconcentraat in kleine containers die **drie keer per week per helikopter** van het schip naar de wal worden gevlogen — geen tankwagen via Walvis Bay dus, wél een schip-naar-wal-helikoptervlucht. Het exacte landingsterrein (bij Oranjemund) is niet geadresseerd gevonden; het scheepspunt zelf is per definitie niet vast te leggen (varend) → **deze helikoptersprong is bewust niet getekend** (geen coördinaat verzonnen), de brief begint bij het Namdeb-terrein in Oranjemund.
- **`dia-namdeb-oranjemund` is een kantoorpand, niet aantoonbaar het helikopter-landingsterrein** — de OSM-node (`office=company`, "MRM Namdeb") is de enige gevonden Namdeb-locatie in Oranjemund binnen het webbudget; status blijft *aannemelijk*.
- **`dia-wdh-cargo` is de terminalapron, geen apart vrachtgebouw** — Hosea Kutako is een kleine regionale internationale luchthaven; op z16-z17 is geen los `Cargo`-gebouw te onderscheiden van het passagiersplatform (Overpass geen resultaat binnen budget).
- **Windhoek → Antwerpen is aannemelijk, niet per zending gebrond**: NDTC-sightholders verhandelen/exporteren via internationale hubs, en het patroon "niet-Russische/niet-Botswaanse rough via Antwerpen" is hergebruikt van de andere ketens in deze golf; er is geen Namibië-specifieke bron voor déze exacte route gevonden (webbudget uitgeput op dit punt).
- **Geen tussenlanding gebrond op b3** (bv. via Johannesburg, zoals historische passagiersvluchten Windhoek deden) → één directe vlucht aangenomen, zoals de bakhandleiding voorschrijft.
- b1-via-punten zijn OSM-plaatscentra (geen satellietpas); de bak-agent snapt op de echte doorgaande B4/B1-rijbaan.

## 8 · Bronnen
[1] OpenStreetMap (ODbL) via Photon — office=company "MRM Namdeb", 6th Avenue, Oranjemund, -28.5528357/16.423751. https://photon.komoot.io
[2] Wikipedia — "Namibia Diamond Trading Company": 50/50 joint venture Republiek Namibië / DTC (De Beers); "houdt zelf sights"; geen vermelding van doorvoer naar Botswana (webcheck uit de haalbaarheidstoets, bevestigd). https://en.wikipedia.org/wiki/Namibia_Diamond_Trading_Company
[3] OpenStreetMap (ODbL) via Photon — aeroway=aerodrome "Hosea Kutako International Airport", -22.4822/17.4720. https://www.openstreetmap.org
[4] OpenStreetMap (ODbL) via Photon — landuse "Brucargo", Machelen, 50.9063/4.4558 (hergebruikt uit `diamant-ekati-antwerpen.md`). https://www.openstreetmap.org
[5] Wikipedia — "Antwerp World Diamond Centre": AWDC/Diamond Office, Hoveniersstraat, Antwerpen; ~1.800 handelaren (hergebruikt anker). https://en.wikipedia.org/wiki/Antwerp_World_Diamond_Centre
[6] Wikipedia — "Hosea Kutako International Airport": "Located 45 km (28 mi) to the east of the city [Windhoek]". https://en.wikipedia.org/wiki/Hosea_Kutako_International_Airport
[7] `v2/design/routebrieven/diamant-ekati-antwerpen.md` — hergebruikte ankers Brucargo (50.90628/4.45584) en AWDC (51.21520/4.41870), E19-corridor.
[8] De Beers Group, 2022 — "World's most advanced diamond recovery vessel to start operating in Namibia": diamantconcentraat verzegeld in containers, drie keer per week per helikopter van schip naar wal gevlogen; Debmarine-productie gaat naar Namdeb Holdings, die verkoopt aan NDTC. https://www.debeersgroup.com/news-insights/business-market/2022/worlds-most-advanced-diamond-recovery-vessel-to-start-operating-in-namibia
[9] design/diamant.md §3a — jaarvolume Namdeb/Debmarine ~2 Mct/jr, ~2% wereldvolume, hoogste $/karaat van de grote producenten (intern ontwerpdocument).
[10] Esri World Imagery via `v2/tools/sat_check.py` (z13-z17, live) — `v2/build-cache/satcheck/sat-diamant-namdeb-gaborone-{oranjemund,windhoek,wdh-wide,wdh-terminal,wdh-close}.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `diamant-namdeb-gaborone`** → `v2/data/stroomroute-diamant-namdeb-gaborone.json` — 4 benen (truck ·
truck · lucht · truck, fase A → A → B → C), **9.324,8 km**, 7.703 punten, 5 markers, 156,0 KB. Recept:
`bak_stromen.sh` (functie `bak_diamant_namdeb_gaborone`); twee nieuwe wegprofielen
`diamant-namdeb-gaborone-oranjemund-windhoek` en `diamant-namdeb-gaborone-windhoek-wdh` in
`maak_stroombeen_weg.py`; het luchtbeen via `maak_luchtbeen.py`; b4 is géén nieuw wegprofiel maar een
**letterlijke hergebruik** van het gebakken geojson van `diamant-ekati-antwerpen` b3.

**b1 (truck, nieuw profiel `diamant-namdeb-gaborone-oranjemund-windhoek`, extract `namibie`, vensterKm 75):**
`maak_stroombeen_weg.py --profiel diamant-namdeb-gaborone-oranjemund-windhoek --bron geofabrik` — **975,4 km**
geroute over de B4 (Oranjemund-omgeving → Rosh Pinah → Aus → Keetmanshoop) → B1 (Keetmanshoop → Mariental →
Rehoboth → Windhoek), zonder refs (B4/B1 zijn de enige doorgaande noord-zuidcorridor in Zuid-Namibië, geen
alternatieve routekeuze). Alle vijf via-snaps ≤ 0,93 km. Anker-verbindingsstukjes Namdeb-terrein → weg 0,01 km
en weg → NDTC 0,02 km (ruim binnen 0,5 km, geen stippel nodig).

**b2 (truck, nieuw profiel `diamant-namdeb-gaborone-windhoek-wdh`, extract `namibie`, vensterKm 40):**
`maak_stroombeen_weg.py --profiel diamant-namdeb-gaborone-windhoek-wdh --bron geofabrik` — **44,6 km** geroute
over de B6 oostwaarts uit Windhoek, geen via-punten nodig (<50 km, B6 eenduidig). Anker-verbindingsstukjes
NDTC → weg 0,02 km en weg → WDH-vrachtapron 0,04 km (geen stippel nodig).

**b3 (lucht, grootcirkel, WDH → BRU):** `maak_luchtbeen.py --van "Hosea Kutako WDH|-22.4863,17.4643" --naar
"Brussels Airport BRU Brucargo|50.90628,4.45584"` — **8.260,1 km** gemeten grootcirkel (brief noemde 8.259,7 —
binnen norm, geen aparte km-toets voor een luchtbeen). 332 punten. Doorgetrokken, geen stippel: een vlucht
tussen twee gelegde vrachtterminals is geen gat. Geen tussenlanding gebrond (brief §7) → één directe vlucht,
conform de bakhandleiding.

**b4 (truck, letterlijke hergebruik van `diamant-ekati-antwerpen` b3):** geen nieuwe weg-scan/profiel — het
`--been-geojson` verwijst rechtstreeks naar `$BEEN/diamant-ekati-antwerpen-weg-brucargo-awdc.geojson` (identieke
Brucargo → AWDC/E19-route, zelfde twee ankers `dia-brucargo`/`dia-awdc`). Getekende lijn **44,7 km** (dat
zusterbake-been mat 44,5 km geroute + anker-verbindingsstukjes, samen 44,7 km getekend — zie
`diamant-ekati-antwerpen.md` §9 voor de volledige toelichting van dit been, hier ongewijzigd).

**Toetsen:** `toets_knikken.py` — truckbenen 5/17 knikken ≥60° (spikes op kruispunten, straal 2–56 m), lucht 0
knikken (per constructie recht); **0 omkeringen ≥150°, 0 terugloop op alle vier benen** — geen actie nodig.
`toets_rechte_benen.py --min-km 5` — geen melding voor deze stroom (lucht wordt per constructie overgeslagen;
geen van de drie truckbenen is een rechte lijn). `json.load` slaagt: versie 2, `punt_formaat` lonlat,
modaliteiten `truck`/`truck`/`lucht`/`truck` ∈ toegestane set, elk been ≥ 2 punten (6.028/556/332/787),
bestandsgrootte 156,0 KB (ruim onder ~300 KB). Naden tussen de vier benen: **0,000 km** op alle drie overgangen.
Markers: alle vijf op 0,0 km van hun been (elk anker is tegelijk het routeerpunt/been-uiteinde).

**Toelichting stippels/haven-aanlopen/vluchten:** géén stippels in deze keten — alle vier benen zijn
doorgetrokken. Geen zeebeen → geen MARNET, geen haven-aanloop. Eén vlucht (b3), doorgetrokken (zie boven).
Fase D/E vervallen (brief §6, stoppunt bij AWDC/Diamond Office).

**Lengtetoetsen:** b1 +8,4% (975,4 tegen ~900 ontwerp) en b2 -1,0% (44,6 tegen 45, Wikipedia) — beide binnen
±15%. b4 is geen nieuwe meting (letterlijke hergebruik van de zusterketen, die op +11,3%/+11,75% uitkwam — zie
`diamant-ekati-antwerpen.md` §9).

**Gereedschapslessen:** dit was de tweede bake van de golf met een luchtbeen (na `diamant-ekati-antwerpen`) en
de eerste met een **letterlijke geojson-hergebruik over stroomgrenzen heen** voor een truckbeen — het
`--been-geojson`-mechanisme van `hecht_marnet.py route` maakt geen onderscheid tussen "eigen" en "andermans"
gebakken geometrie in `$BEEN`, zolang de ankers exact overeenkomen (hier: `dia-brucargo`/`dia-awdc`, identieke
coördinaten in beide brieven). Geen tool-aanpassing nodig. De grootste onzekerheid in deze keten (de
helikoptersprong schip → wal, brief §7) blijft bewust ongetekend — geen coördinaat verzonnen voor een varend
scheeppunt.
