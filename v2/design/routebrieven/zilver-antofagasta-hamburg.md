# Zilver · Chileens koperconcentraat (herkomstmijn onbekend) → Brunsbüttel → Aurubis Hamburg (Duitsland)

**stroom-id:** `zilver-antofagasta-hamburg` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) ·
**status:** gebakken
**Keten in één zin:** zilver in Chileens koperconcentraat (herkomstmijn onbekend; Puerto Antofagasta/ATI als laadhaven,
**aannemelijk: één bron**) per **bulkcarrier** via Panama naar de Elbehafen Brunsbüttel, daar overgeslagen en voorgemengd,
per **binnenschip-shuttle** (Schramm) ~76 km de Elbe op naar de concentraatkade van **Aurubis Hamburg, Werk Ost**; in de
Rohhütte/elektrolyse blijft het zilver in het anodeslijk achter en wordt het in de Edelhütte van Aurubis Hamburg als
verkoopproduct afgescheiden — stoppunt: de concentraatkade (geen eigen been naar de Edelhütte, zie §6).
**Welke as van het verhaal:** Zuid-Amerikaans koperconcentraat met zilverbijproduct naar Europa's grootste primaire
koperzmelter. Volume: Aurubis **groep** verkocht **930 t Ag in FY2024/25** (921 t in FY2023/24) [1], inclusief recycling
(Aurubis-zilver 56% recycled content, 2021/22 [2]); aandeel Hamburg, aandeel Chili en Ag-gehalte van het concentraat zijn
**niet gepubliceerd**. Hamburg zet 0,9–1,3 Mt concentraat/j in [6]. De 800 t Ag/j uit de sitelaag is niet herbevestigd en
wordt hier niet als ketenvolume gebruikt.

## 1 · Ketenkaart
```
Puerto Antofagasta, molo/ATI `ag-antofagasta-molo`  (herkomstmijn onbekend, Codelco-district aannemelijk)
  ──(b1 haven-aanloop 97,1 stip · b2 zee ~13.596 km via Panama, aannemelijk: één bron · b3 haven-aanloop 4,0 stip)──►
Elbehafen Brunsbüttel, droge-bulkkade `ag-brunsbuettel-kade`  (overslag + voormenging)
  ──(b4 stip 4,0 · b5 binnenvaart Unterelbe/Norderelbe ~63,8 · b6 stip 8,2)──►
Aurubis Hamburg, concentraatkade Müggenburger Kanal `ag-hamburg-konzentratkade`
  ── (op het terrein, geen been) Werk Ost `ag-hamburg-werkost`: Rohhütte → elektrolyse → anodeslijk → Edelhütte (Werk Nord) ── stoppunt
```

## 2 · Benen
Geometrie = **letterlijke kopie** van benen 1–6 van `koper-aurubis-hamburg` (`bak_koper_aurubis()`); alleen de beennamen krijgen
"aannemelijk: één bron" op de zeetak. Totaal **13.773,1 km** (het ontwerp noemde 13.680; de gebakken koper-benen tellen 13.773).
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ag-antofagasta-molo` → MARNET-zeeknoop 4664 (-23.8, -71.3) | haven-aanloop Antofagasta | 97,1 (kade-zeeknoop hemelsbreed 92,2) | `aanloop-antofagasta.geojson` (kopie koper b1) | ja: MARNET reikt niet |
| b2 | B | zee | zeeknoop 4664 → zeeknoop Elbemonding (53.8771, 9.2273) | Panamakanaal, bulkcarrier (aannemelijk: één bron) | ~13.596 (searoute-referentie, geen gepubliceerde afstand) | MARNET (kopie koper b2) | nee |
| b3 | B | zee | zeeknoop → `ag-brunsbuettel-kade` | haven-aanloop Elbehafen Brunsbüttel | 4,0 (zeeknoop-kade 3,7) | `aanloop-brunsbuettel-aankomst.geojson` (kopie b3) | ja: schematisch |
| b4 | C | binnenvaart | `ag-brunsbuettel-kade` → zeeknoop | vertrek Schramm-shuttle | 4,0 | `aanloop-brunsbuettel.geojson` (kopie b4) | ja: schematisch |
| b5 | C | binnenvaart | (53.8771, 9.2273) → (53.5451, 9.9273) | Unterelbe → Norderelbe, zeevaarweg in MARNET | 63,8 gebakken; Elbe-km 695 → 618,4 = 76,6 gepubliceerd [7] | MARNET (kopie b5) | nee |
| b6 | C | binnenvaart | Norderelbe → `ag-hamburg-konzentratkade` | Müggenburger Kanal | 8,2 | rechte stippel (kopie b6) | ja: 1:10M-kust kent de haven niet |
Haven-aanloop-regel (§2 handleiding): Antofagasta-kade ligt 92,2 km van de zeeknoop en Brunsbüttel-kade 3,7 km — beide aanlopen zitten
al in de benen (b1 en b3/b4); er is geen extra aanloop nodig. Toets: Elbe 63,8 + 4,0 + 8,2 = 76,0 km tegen 76,6 gepubliceerd (−0,8%).

## 3 · Ankers (allen hergebruikt letterlijk uit `koper-aurubis-hamburg`, lat, lon, 4 decimalen)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-antofagasta-molo` | laadkade (herkomst) | Puerto Antofagasta, frente 2 (ATI, sitios 4–7), molo-binnenzijde | -23.6500, -70.4088 | [8][9] | bron-gelegd; z15 opnieuw gezien: lange molo met afgemeerd schip aan de binnenzijde, containerstapels en loodsen op de wal; welk sitio het concentraat laadt is open |
| `ag-brunsbuettel-kade` | overslag zee → binnenschip | Elbehafen Brunsbüttel, droge-bulkkade | 53.8878, 9.1740 | [6][7] | bron-gelegd (koper-brief z16: kademuur met havenkranen, zeeschip aan de kade, stockpiles en loodsen erachter) |
| `ag-hamburg-konzentratkade` | losplek concentraat | Aurubis Werk Ost, kade Müggenburger Kanal | 53.5163, 10.0418 | [6] | bron-gelegd (koper-brief z17: verharde kade met kraanachtige structuur aan de Werk-Ost-oever) |
| `ag-hamburg-werkost` | smelter + elektrolyse (anodeslijk) | Aurubis Hamburg, Werk Ost (Rohhütte Werk Ost, Elektrolyse) | 53.5140, 10.0400 | [3] | bron-gelegd (z15 gezien: hüttecomplex met schoorsteen, zuurfabriek en rangeerterrein op de Veddel-landtong tussen Kanaal en Elbe) |
Niet gelegd: de **Edelhütte** (Werk Nord, [3]) — geen coördinaat gevonden, dus geen anker en geen been (§7). Het sitelaag-punt `w-ref-aurubis-hh`
(53.5186, 10.0408, aannemelijk) ligt ~0,5 km noordelijker en wordt niet gebruikt.

## 4 · Via-punten
Geen: alle benen zijn zee, binnenvaart of stippel; er is geen land-been, geen spoor en geen weg-km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Elbehafen Brunsbüttel (overslag, opslag, voormenging) | Brunsbüttel Ports / Schramm | zeeschip-concentraat → gemengd concentraat op binnenschip | >11 Mt cumulatief 2007–2017 | [6][7] |
| Aurubis Hamburg: Rohhütte + elektrolyse (Werk Ost) → Edelhütte (Werk Nord) | Aurubis AG | concentraat → kathode + anodeslijk; anodeslijk + edelmetaalrijke tussenproducten → Ag, Au, PGM | concern 930 t Ag/j verkocht (Hamburg-deel onbekend); nieuwe Precious Metals Refinery (~300 Mio. EUR) gepland eind 2026 | [1][3][4] |

## 6 · Stoppunt
De brief stopt op de concentraatkade: de Edelhütte ligt op hetzelfde terrein (Werk Nord) en heeft geen gepubliceerde coördinaat, en een intern been zou een
last-mile-been zijn; één bron (de Umweltbericht) noemt de procesketen Rohhütte → elektrolyse → Edelhütte, geen bron noemt een afnemer van het zilver zelf (fase D/E vervalt).

## 7 · Open punten
- **Herkomst onbekend:** geen bron koppelt Chileens concentraat aan Aurubis Hamburg per mijn of haven; Aurubis noemt alleen "Chile, Peru, Brasilien" en Codelco als partner [1], en Codelco is 48% van de concentraatverschepingen in Antofagasta (2013) [8]. Antofagasta is dus aannemelijk, niet gedocumenteerd.
- **Zilvervolume voor Hamburg of Chili ontbreekt;** alleen groepscijfer inclusief recycling. 921 t verschijnt zowel als FY2022/23 (Metzler [2]) als FY2023/24 (GB [1], verkoopvolumes) — verschil productie/verkoop of afrondingsvraag, niet opgelost.
- **Zilver in dit concentraat is een procesredenering,** geen gemeten gehalte: Aurubis noemt zilver als bijproduct van koper [1][3]; het enige Fraunhofer-procesdiagram uit het onderzoeksontwerp [5] is een scan en niet machineleesbaar, dus niet gecontroleerd.
- **Edelhütte niet gelegd** (Werk Nord, geen coördinaat): geen anker, geen marker.
- **Zeeafstand 13.596 km** is een searoute/MARNET-referentie, geen gepubliceerde havenafstand (geen onafhankelijke toets).
- **Gaan er óók schepen rechtstreeks naar Hamburg?** Aurubis zegt "vornehmlich" via Brunsbüttel [1]; het rechtstreekse aandeel is niet gevonden en wordt niet getekend.
- **Kathode-benen naar Emmerich** zijn bewust niet meegenomen (zilver verlaat Hamburg niet als kathode).

## 8 · Bronnen
[1] Aurubis, Geschäftsbericht 2024/25, Lagebericht (p. 4: Konzentrate vornehmlich auf dem Seeweg, Hafenterminal Brunsbüttel, Vormischung; Chile/Peru/Brasilien; Codelco-samenwerking 2024; Wirtschaftsbericht ~p. 90: Verkaufsmengen Silber 930 t 2024/25, 921 t 2023/24), https://geschaeftsbericht2024-25.aurubis.com/fileadmin/static/pdf_de/Aurubis-GB-24-25-Lagebericht.pdf
[2] Aurubis, Metzler Roadshow 2024-08-27 (p. 4: Silber 921 t +1%, concentrate processing 2.319.000 t FY22/23; p. 5: Aurubis Silver 56% recycled; p. 26: nieuwe precious metal plant Hamburg), https://aurubis.com/en/dam/jcr:457653c0-0f4c-4b3e-a84e-89a0149cc24f/20240827_%20Aurubis_%20Metzler_Roadshow.pdf
[3] Aurubis, Umweltbericht 2024 (Standort Hamburg: Werk Nord met Edelmetallproduktion, Werk Ost met Rohhütte + Elektrolyse; Edelhütte scheidt Silber, Gold, PGM hydrometallurgisch; Treibkonverter verwerkt eigen Anodenschlämme), https://aurubis.com/dam/jcr:13846db9-30b0-4eeb-b6a8-0555fd00eb23/2024_Umweltbericht_DE.pdf
[4] Aurubis, persbericht 2023-12-12, 330 Mio. EUR Hamburg, Precious Metals Refinery (~300 Mio., in bedrijf eind 2026), https://www.presseportal.de/download/document/65782f7f270000fd2cb97f54-aurubis-pressemittei-schutz-20231212.pdf
[5] Fraunhofer UMSICHT, Nolte, DGAW 2018 (procesdiagram Aurubis; PDF is een scan, niet te lezen), https://www.umsicht-suro.fraunhofer.de/content/dam/umsicht-suro/de/images/pressemitteilungen/2018/DGAW/6_Nolte.pdf
[6] Routebrief `koper-aurubis-hamburg.md` (bronnen [1]–[5], [14], [17], [18] daar: Hafen Hamburg 2017, THB 2016, Umwelterklärung 2022/2025 met input Hamburg 0,9–1,3 Mt, Schramm), v2/design/routebrieven/koper-aurubis-hamburg.md
[7] Hafen Hamburg, 2017-04-03, ">5.000 Binnenschiffe mit Kupfererzkonzentrat beladen" (>11 Mt 2007–2017), https://www.hafen-hamburg.de/de/presse/news/ueber-5000-binnenschiffe-mit-kupfererzkonzentrat-beladen-35163/ · Elbe-km: https://gewaesser.rudern.de/norderelbe
[8] MundoMaritimo, 2014-05-09, "48% de los embarques de concentrados son de Codelco en Puerto Antofagasta", https://www.mundomaritimo.cl/noticias/48-de-los-embarques-de-concentrados-son-de-codelco-en-puerto-antofagasta
[9] Hanseatic Global Terminals, ATI (sitios 4–7, frente de atraque 2), https://latinamerica.hanseaticglobalterminals.com/business-area-section/port-terminals/ati/
Satelliet (Esri z15): `v2/build-cache/satcheck/sat-zilver-antofagasta-hamburg-antofagasta-molo.png`, `sat-zilver-antofagasta-hamburg-aurubis-complex.png`; eerdere z16/z17-beelden in de koper-brief.

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)

**Stroom `zilver-antofagasta-hamburg`** → `v2/data/stroomroute-zilver-antofagasta-hamburg.json` (28,4 KB, versie 2, lonlat) — 6 benen, **13.773,1 km**, 4 markers.
| # | modaliteit | km | stippel | naam (kort) |
|---|---|---|---|---|
| b1 | zee | 97,1 | ja | haven-aanloop Antofagasta (kopie koper b1) |
| b2 | zee | 13.596,0 | nee | MARNET zeeknoop -23,8/-71,3 → Elbemonding, via Panama (herkomst aannemelijk: één bron) |
| b3 | zee | 4,0 | ja | haven-aanloop Brunsbüttel aankomst (kopie koper b3) |
| b4 | binnenvaart | 4,0 | ja | vertrek Schramm-shuttle (kopie koper b4) |
| b5 | binnenvaart | 63,8 | nee | MARNET Unterelbe → Norderelbe |
| b6 | binnenvaart | 8,2 | ja | Norderelbe → Müggenburger Kanal, concentraatkade |
Markers: Antofagasta molo/ATI (-23,6500, -70,4088) · Brunsbüttel Elbehafen (53,8878, 9,1740) · Hamburg concentraatkade (53,5163, 10,0418) · Werk Ost (53,5140, 10,0400).
Recept: `bak_stromen.sh` (functie `bak_zilver_antofagasta_hamburg`, nieuwe stroom-id zonder eigen scan). Toelichting: benen b1, b3 en b4 zijn letterlijke kopieën van de `aanloop-*.geojson` van `koper-aurubis-hamburg`; b2, b5 en b6 zijn dezelfde MARNET-/stippelregels. Er is geen wegscan, geen spoor, geen vlucht en geen leiding. De zes benen geven exact dezelfde km als de koper-benen 1-6 (13.773,1 km).
Stippels: alle vier de stippels betekenen "hier reikt het net niet" (Antofagasta 97 km buiten MARNET, Brunsbüttel-kade 3,7 km van de zeeknoop, Hamburg 1:10M-kust kent de haven niet); de gemeten zee- en Elbebenen zijn doorgetrokken, ook al is de herkomst aannemelijk (staat in de beennaam).
Haven-aanloop: Antofagasta-kade 92,2 km van de zeeknoop en Brunsbüttel-kade 3,7 km — beide aanlopen zitten al in de benen; geen extra aanloop nodig.
Toets: Elbe 63,8 + 4,0 + 8,2 = 76,0 km tegen 76,6 gepubliceerd (-0,8%). Naden tussen opeenvolgende benen 0,00 km. Markers 0,0 km van hun lijn, behalve Werk Ost (0,3 km van de kade; terreinanker). `toets_knikken.py`: 4 knikken >= 60 graden, 0 omkeringen, 0 terugloop (twee spikes in het Kanaal bij 50,3375/-0,7643 en twee krappe bochten bij Panama, MARNET-geometrie, identiek aan de koper-stroom). `toets_rechte_benen.py --min-km 5`: alleen de stippel b6 (8,2 km, bewust). json geldig (versie 2, punt_formaat lonlat, modaliteiten in {zee, binnenvaart}, elk been >= 2 punten).
Open: herkomst en zilvervolume blijven ongedocumenteerd (§7); de Edelhütte is niet gelegd en heeft geen marker.

**Gereedschapslessen:**
- Een stroom die dezelfde benen deelt met een bestaande stroom bakt in ~16 s zonder slot-pool van weg/reus: alleen het zwaar-slot en een functie met letterlijke kopieën (geen herberekening, geen tweede versie).
- Bij het kopiëren van een koper-functie: laat de spoorstippels en de Emmerich-regels weg, anders krijgt het zilver een spoorstuk dat niet in de keten zit.
