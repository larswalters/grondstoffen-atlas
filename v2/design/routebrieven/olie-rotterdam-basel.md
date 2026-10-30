# Routebrief (licht) · olie — Botlek (Rotterdam) → Rijn → tanklager Birsfelden (Basel, Zwitserland)

**stroom-id:** `olie-rotterdam-basel` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** aardolieproducten (diesel, stookolie, benzine) uit de ARA-producthub, geladen bij de Botlek Tank
Terminal in de Rotterdamse Botlek, per tankbinnenvaartschip ca. 860 km stroomopwaarts over Oude Maas, Merwede, Waal en Rijn
naar de tanklagers in het Hafen Birsfelden (Schweizerische Rheinhäfen, bij Basel) — de Zwitserse aanvoerslagader voor brandstof.
**Welke as van het verhaal:** *Rijn-binnenvaart als Zwitserse energielijn* — 2,64 Mt mineraalolieproducten via de Zwitserse
Rijnhavens in 2024 (≈ 54 kb/d bij 7,5 vat/t, eigen omrekening) [1]; 2025: import −22%, ca. 2,02 Mt (≈ 41 kb/d) [2].
Herkomst Rotterdam en de terminal zijn **aannemelijk: één bron voor het geheel** (geen bron koppelt Botlek aan Birsfelden).

## 1 · Ketenkaart
```
Botlek Tank Terminal `ol-botlek-btt` (Rotterdam)
  ──(b1 binnenvaart · Oude Maas → Merwede → Waal → Boven-Rijn → Midden-Rijn → Oberrhein · ~861 km, AIS-graaf + bulklaag;
      aannemelijk: één bron voor herkomst en terminal)──► Tanklager Hafen Birsfelden `ol-birsfelden-tank` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | B | binnenvaart | Botlek Tank Terminal → Groothoofd (Dordrecht) | Oude Maas → Beneden-Merwede, Noord niet nemen | ~37 (gemeten proef) | AIS-graaf rijn | nee |
| b1b | B | binnenvaart | Groothoofd → Werkendam → Loevestein → Pannerdensche Kop | Merwede → Boven-Merwede → Waal, 3 AIS-benen, **letterlijke kopie** van `kolen-cerrejon-ruhr` (117,3 km) | 117,3 (gemeten) | AIS-graaf rijn (kopie) | nee |
| b1c | B | binnenvaart | Pannerdensche Kop → Birsfelden | Waal/Rijn via Köln, Mainz, Strasbourg tot Rijn-km ca. 164 | ~703 (Rijn-km 867 → 164, eigen kennis); gemeten 706,7 | maak_rivierbeen over bulklaag | nee |

Totaal proef: **861 km**, naad ca. 0,5 km (haalbaarheidstoets 0,47), 0 stippel. Gepubliceerde totaalafstand niet gevonden; ontwerp-indicatie ca. 830 km
(eigen schatting) → +3,7%: indicatie, geen norm. Geen last-mile-benen: beide ankers liggen aan de kade (< 0,25 km van het water).
Geen zee, geen haven-aanloop (geen zeebeen), geen leiding, spoor of lucht.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-botlek-btt` | laadplek / tankterminal | Botlek Tank Terminal (Botlekhaven, Rotterdam) | 51.8793, 4.2653 | [5][6] | **onzeker** (z15 gezien: tankenpark van tientallen witte tanks vlak aan het havenbekken met binnenvaartschepen langs de kade; geen bron noemt déze terminal voor Basel-lading) |
| `ol-birsfelden-tank` | losplek / tanklager | Tanklager Hafen Birsfelden (Schweizerische Rheinhäfen) | 47.5560, 7.6385 | [2][4][6] | **bron-gelegd** (z15 gezien: tankenpark van tientallen tanks op de landtong tussen haven en Rijn, tankers aan de kade; SRH 2025 noemt "Tanklager im Hafen Birsfelden" [2]) |

Alternatieven die **niet** gekozen zijn: Chane Terminal Botlek (51.8789, 4.3158; OSM W144149689, z15: groot tankenpark op de oostelijke
landtong, door [5] als ARA-laadplek van Rijn-vrachttarieven genoemd) en Auhafen Muttenz TAU (47.5446, 7.6558; z15: tankenpark aan de
Rijn-oever, het ontwerp-eindpunt). Beide zijn echte tankterminals; welke de Basel-lading precies laadt/lost is niet gebronnen.

## 4 · Via-punten
Geen eigen via-punten: de corridorkeuzes (Noord niet nemen, Nieuwe Merwede niet nemen, Pannerdensch Kanaal niet nemen)
zitten in de 4 AIS-benen b1a/b1b, waarvan 3 een letterlijke kopie zijn van `kolen-cerrejon-ruhr` (Groothoofd 51.820,4.670 ·
Werkendam 51.821,4.894 · Loevestein 51.821,5.002 · Pannerdensche Kop 51.874,6.038). Boven Pannerdensche Kop is er geen keuze
(één Rijn): b1c is het kortste pad over de bulklaag, gecontroleerd langs Köln, Koblenz, Mainz, Maxau, Strasbourg en Breisach (0,1–2,3 km).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tanklagers Hafen Birsfelden (en Auhafen Muttenz) | meerdere tanklager-exploitanten (niet gebronnen) | producten per schip → Zwitserse binnenlandse distributie / raffinaderij Cressier-wisselwerking | totaal SRH 2,64 Mt (2024) | [1][2] |

## 6 · Stoppunt
De brief stopt bij het tanklager in Hafen Birsfelden: de bron noemt de tanklagers daar als importpunt, maar geen bron noemt een
volgende locatie voor déze lading; fase D/E vervallen. Raffinaderij Cressier (NE) is alleen als wisselwerking genoemd [2], niet als bestemming per lading.

## 7 · Open punten
- **Geen bron koppelt Rotterdam/Botlek aan Birsfelden per lading.** SRH geeft alleen volume per goedergroep; ARA-herkomst volgt uit
  Rijn-vrachttarieven ARA → Basel [5] en algemene kennis. Een deel kan uit de Duitse binnenlandse raffinaderij Karlsruhe komen [5].
- **Welke Botlek-terminal** laadt is open (BTT onzeker; Chane Terminal Botlek is de alternatieve kandidaat, [5] noemt beide).
- **Welke Birsfelden-exploitant** (en of Auhafen Muttenz meedoet) is niet gebronnen; SRH 2024: ook Auhafen Muttenz (+4,6%) en Kleinhüningen (+5,1%) groeien [1].
- **Geen gepubliceerde vaarafstand Botlek → Birsfelden**; 861 km gemeten, 830 km ontwerp-indicatie. Rijn-km-verschil Basel (166,6) → Rijnmonding (ca. 1.032) is ca. 866 km: niet zelf gelezen in een bron.
- Laagwater kan de route dichtknijpen (Kaub, lente 2025 [2], zomer 2026 [7]); tankers varen dan deellading of niet: volume per jaar blijft indicatief.
- Volume: 2,64 Mt is alle mineraalolieproducten via de drie havens (incl. export), geen Rotterdam-aandeel; import alleen 2,59 Mt (bulletin 2024) [1].

## 8 · Bronnen
[1] Schweizerische Rheinhäfen / SVS, medienmitteilung 26-02-2025, "Umschlag Schweizerische Rheinhäfen 2024": 5,39 Mt totaal, Mineralölprodukte 2,64 Mt (+6,8%), Hafen Birsfelden +14,4%, Auhafen Muttenz +4,6%, Kleinhüningen +5,1%; Monatsbulletin Dez. 2024: Zufuhr Mineralölerzeugnisse 2.589.510 t. https://port-of-switzerland.ch/wp-content/uploads/2025/02/Medien_SRH_SVS_Jahreszahlen_2024.pdf
[2] Schweizerische Rheinhäfen, medienmitteilung 27-02-2026, "Umschlag 2025": 4,7 Mt (−11,3%), Mineralöl-/Energieimport −22% (ca. 570.000 t), "Import über die Tanklager im Hafen Birsfelden"; Bulletin: Zufuhr Mineralölerzeugnisse 2.019.653 t; Niedrigwasser im Frühling. https://port-of-switzerland.ch/wp-content/uploads/2026/03/MM-SRH-Umschlagszahlen-2025.pdf
[3] Eigen omrekening: 2,64 Mt × 7,5 vat/t / 365 = ca. 54 kb/d; 2,02 Mt → ca. 41 kb/d.
[4] Wikipedia (DE) "Schweizerische Rheinhäfen": Hafen Birsfelden (1937-40) is gespecialiseerd in vloeibare brand- en brandstoffen; in 2023 30% van de Zwitserse mineraalolie-import via de drie Rijnhavens; coördinaat 47,588/7,590. https://de.wikipedia.org/wiki/Schweizerische_Rheinh%C3%A4fen
[5] tankterminals.com, 29-04-2026, "Rhine Freight Market: Falling Water Levels Jolt Rates": noemt Basel als Rijn-tariefbestemming, ARA-terminals, Chane Terminal Botlek, Evos Amsterdam East en de Karlsruhe-raffinaderij als herkomsten (geen tarief- of volumecijfers). https://tankterminals.com/news/rhine-freight-market-falling-water-levels-jolt-rates-mid-week-before-market-settles/
[6] OpenStreetMap (ODbL) via Photon: landuse Botlek Tank Terminal W150118003 (51,8793/4,2653); Chane Terminal Botlek B.V. W144149689 (51,8789/4,3158); coördinaat Birsfelden uit de haalbaarheidstoets (47,5560/7,6385).
[7] Samenvattingen in zoekresultaten (S&P Global, Argus, aug. 2026) over recordlaagwater bij Kaub en ARA-Basel-vrachttarieven; paginatekst niet leesbaar (403/leeg), alleen als context. https://www.spglobal.com/energy/en/news-research/latest-news/crude-oil/082126-rhine-water-levels-rebound-easing-barge-shipping-strain
[8] Routebrief `kolen-cerrejon-ruhr` (2026-07-24/09-26): AIS-benen Groothoofd → Pannerdensche Kop en corridorkeuzes; bake-functie `bak_kolen_cerrejon_ruhr` in `v2/tools/bak_stromen.sh`.
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-olie-rotterdam-basel-botlek-btt.png`, `-botlek-chane.png`, `-birsfelden.png`, `-muttenz-auhafen.png`.
[10] Eigen proef 2026-10-30: `hecht_marnet.py route` + `maak_rivierbeen.py` (Pannerdensche Kop → Birsfelden: 706,2 km over 134 bulk-edges, bulk-knoop 0,23 km van het anker) → 861,1 km, 0 stippel, naad ca. 0,5 km.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

**Bestand:** `v2/data/stroomroute-olie-rotterdam-basel.json` (67,2 KB, versie 2, punt_formaat lonlat, 4.005 punten, 2 markers).
**Recept:** `bash v2/tools/bak_stromen.sh olie-rotterdam-basel` (functie `bak_olie_rotterdam_basel`, graaf `v2/build-cache/ais/graaf/rijn`; ~5 s).
Titel: "Olie · Botlek (Rotterdam) → Rijn → Birsfelden (Basel, Zwitserland)". Het eindpunt komt overeen met het stroom-id.

| # | modaliteit | been | km gemeten | punten | doorgetrokken/stippel |
|---|---|---|---|---|---|
| 1 | binnenvaart | Botlek Tank Terminal → Groothoofd (Noord NIET nemen) | 37,1 | 82 | doorgetrokken (AIS-graaf, snap 0,113/0,017 km) |
| 2 | binnenvaart | Groothoofd → Werkendam (kopie kolen-cerrejon-ruhr) | 22,6 | 36 | doorgetrokken |
| 3 | binnenvaart | Werkendam → Loevestein (kopie kolen-cerrejon-ruhr) | 9,5 | 19 | doorgetrokken |
| 4 | binnenvaart | Loevestein → Pannerdensche Kop (kopie kolen-cerrejon-ruhr) | 85,2 | 161 | doorgetrokken |
| 5 | binnenvaart | Pannerdensche Kop → Birsfelden (bulklaag, vooraf gebakken FeatureCollection) | 706,7 | 3.707 | doorgetrokken |

Totaal **861,1 km** (b1b = benen 2-4 samen 117,3 km). Markers: `ol-botlek-btt` (onzeker, 0,113 km van de lijn) en `ol-birsfelden-tank`
(bron-gelegd, 0,235 km van de lijn: de bulk-knoop). Geen zee, geen haven-aanloop, geen stippel, geen leiding, geen vlucht, geen last mile,
geen via-punten, geen extracts. Er is geen gepubliceerde vaarafstand: 861,1 km tegen de ontwerp-indicatie 830 km (eigen schatting) is +3,7%,
indicatie en geen norm; Rijn-km 867 naar 164 (ca. 703, eigen kennis) tegen gemeten 706,7 km (+0,5%).

**Kopie:** de benen 2-4 zijn letterlijk dezelfde punten als in `stroomroute-kolen-cerrejon-ruhr.json` (puntlijst per been gelijk gecontroleerd).
De Rijn-vervolgstukken lopen over de bulklaag (`maak_rivierbeen.py`, 706,2 km, 134 bulk-edges); dat been zegt waar het water ligt,
niet dat er een schip gezien is. Herbouwcommando staat in het kopcommentaar van de functie.

**Toets:** naden 0,00 / 0,00 / 0,00 / 0,47 km (max 0,47 km; geen zee-snap, dus geen haven-aanloop nodig). `toets_rechte_benen.py --min-km 5`:
geen regel voor deze stroom. `toets_knikken.py`: 17 knikken >= 60 gr, 5 omkeringen >= 150 gr, 2 daarvan TERUGLOOP; alle in de gekopieerde benen
2-4 (Groothoofd-Werkendam bij 51,8284/4,9404; Loevestein-Pannerdensche Kop bij 51,8747/6,0385), dus erfgoed van de cerrejon-AIS-benen en
hier niet bijgewerkt (andermans recept). Bulkbeen: 3 krappe bochten (Oberrhein bij 48,02/7,58; R 300-350 m), echte rivierbochten.
json.load: versie 2, punt_formaat lonlat, modaliteiten {binnenvaart}, elk been >= 2 punten.

**Bevindingen:**
- De twee TERUGLOOP-spijkers in de gekopieerde AIS-benen (zie hierboven) zijn niet bijgeschoven: een kopie blijft letterlijk, een reparatie hoort bij `kolen-cerrejon-ruhr`.
- Het AIS-stuk begint bij `ol-botlek-btt` met een korte spijker rond 51,8209/4,6780 (Groothoofd-aansluiting, 99 gr, R 36 m); klein, niet gerepareerd.
- Herkomst ARA/Botlek en de terminal blijven aannemelijk (een bron voor het geheel); de open punten van §7 zijn ongewijzigd.

**Gereedschapslessen:**
- **Een keten van alleen binnenvaart over de AIS-graaf vraagt `--graaf "v2/build-cache/ais/graaf/rijn"` in de functie**; de default in de kop is mississippi.
- **Een vooraf gebakken bulkbeen uit de haalbaarheidstoets (FeatureCollection) is direct bruikbaar als `--been-geojson`**: de bake duurde 5 s, geen wegscan of slot-rekenwerk nodig.
