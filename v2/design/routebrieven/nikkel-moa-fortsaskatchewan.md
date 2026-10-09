# Routebrief (licht) · nikkel — Moa Bay (Cuba) → Halifax → Fort Saskatchewan (Canada)

**stroom-id:** `nikkel-moa-fortsaskatchewan` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** nikkel (als mixed-sulphide-neerslag, MSP, in zakken, samen met kobalt) van de Moa-JV-plant (Sherritt/General Nickel Company) in Cuba per **zeeschip** om de VS heen naar Halifax en per **spoor** over de CN-hoofdlijn (Moncton, Québec, Winnipeg, Saskatoon, Edmonton) naar de Sherritt-raffinaderij in Fort Saskatchewan, Alberta [1][5]. **Stilgevallen sinds 2026:** Moa-mijn grotendeels stil sinds feb 2026 (brandstof), VS-sanctie op Moa Nickel S.A. 7 mei 2026, raffinaderij gesloten 22 jun 2026 (MSP-voorraad op) [3][4]. De lijn toont infrastructuur, geen actieve lading.
**Welke as van het verhaal:** *Cuba naar Canada*, het enige westerse class-1-nikkeltraject uit een gesanctioneerd land. Volume: **25,24 kt afgewerkt nikkel in 2025** (100%-basis, Moa-JV-feed, tegen 31–33 kt oorspronkelijke guidance) [2]; capaciteit Fort Saskatchewan 38,2 kt Ni+Co (100%) [1]. Eenheid kt Ni/j, peiljaar 2025 (sitelaag: 33 kt Ni, nameplate-schatting). **Geometrie = letterlijke kopie van `kobalt-moa-fortsaskatchewan`** (zelfde MSP-lading, andere grondstof; precedent `nikkel-norilsk-monchegorsk` / `kobalt-norilsk-monchegorsk`) [6].

## 1 · Ketenkaart
```
Moa-laadkade `ni-moa-laad` ──(b1 zee, STIPPEL · haven-aanloop · 70,9 km)──► MARNET-zeeknoop 8163 (21.1135,-74.4068)
 ──(b2 zee · Caribische Zee → Atlantische Oceaan, om de VS heen · 2.943,5 km)──► Halifax-kade `ni-halifax-kade` (aannemelijk)
 ──(b3 spoor · CN via Moncton/Québec/Winnipeg/Saskatoon/Edmonton · 4.839,8 km, zes stukken)──► Fort Saskatchewan `ni-fortsask-raffinaderij`
 ⏹ stoppunt (gesloten raffinaderij)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee (haven-aanloop) | `ni-moa-laad` → zeeknoop 8163 | — | 70,9 gemeten (rechte lijn 70,5; tool-snap 75,7) [6] | KOPIE geojson `kobalt-moa-fortsaskatchewan-aanloop-moa` | **ja**: MARNET reikt niet tot de kade (> 25 km) |
| b2 | B | zee | zeeknoop 8163 → `ni-halifax-kade` | Caribische Zee → Atlantische Oceaan, bewust niet langs de VS-kust | 2.943,5 gemeten, 38 MARNET-edges (indicatief ~2.900, geen gepubliceerde lengte) [6] | MARNET `--been` | nee |
| b3 | C | spoor | `ni-halifax-kade` → `ni-fortsask-raffinaderij` | CN: Halifax–Moncton–Québec–Winnipeg–Saskatoon–Edmonton | 4.839,8 gemeten in zes stukken (297,8 · 704,6 · 2.477,7 · 766,7 · 520,0 · 73,0); ontwerp ~5.000 indicatief (−3,2%), hemelsbreed 3.659; **geen gepubliceerde lengte** [6] | KOPIE van zes `spoorroute-kobalt-moa-fortsaskatchewan-*.geojson` | nee |

Totaal 7.854,2 km. Geen fase A (mijn → laadkade): de plant ligt ~1,6 km van de kade en valt onder "geen last-mile-been" (de laadplek is zelf onzeker, §7). Fase D/E vervallen (§6).

## 3 · Ankers (één per site en per overslag, letterlijk hergebruikt uit `kobalt-moa-fortsaskatchewan` [6])
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-moa-laad` | laadplek (plant aan zee) | Punta Gorda-aanlegsteiger, Bahía de Moa (Moa-JV, plant ~1,6 km landinwaarts) | 20.6372, -74.8549 | [1][6][8] | **onzeker** (z15 gezien, eigen beeld `sat-nikkel-moa-fortsaskatchewan-moa-laad.png`: kaap met kleine steiger en dorpje; het plantcomplex met tankpark ligt ~2 km west; geen bulkkraan of laadbrug te zien) |
| `ni-halifax-kade` | overslag zee → spoor | Richmond Terminals, Halifax (multipurpose, kade-eigen spoor) | 44.6735, -63.6032 | [1][5][6][9] | **aannemelijk** (z15 gezien, `sat-nikkel-moa-fortsaskatchewan-halifax-kade.png`: kruis op de kade met spoorbundel en een schip aan de noordoever van het schiereiland). Halifax als haven is nu **primair gebrond door Sherritt** [1]; de kade zelf (Richmond) blijft één bron |
| `ni-fortsask-raffinaderij` | losplek / raffinaderij | Sherritt Metals Facility, Fort Saskatchewan | 53.7198, -113.1904 | [1][6] | **bron-gelegd** (z15 gezien, `sat-nikkel-moa-fortsaskatchewan-fortsask-raffinaderij.png`: complex met bolvormige tanks, rood-oranje tailingsvijver en spooraansluiting; kruis op de zuidrand van het terrein) |

## 4 · Via-punten (alleen b3; letterlijk uit `kobalt-moa-fortsaskatchewan` §4, de lijn is al gebakken)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b3 | 1 | Moncton, CN-junctie | 46.0833, -64.7861 | Maritimes-omweg i.p.v. de Maine-VS-doorsteek; markers 177 m van de lijn |
| b3 | 2 | Québec, Gare du Palais | 46.8178, -71.2139 | oeversprong Saint-Laurent; marker 507 m van de lijn |
| b3 | 3 | Winnipeg, Union Station | 49.8889, -97.1343 | oost/west-knoop CN-hoofdlijn; 123 m |
| b3 | 4 | Saskatoon, CN Chappell Yard | 52.1052, -106.7505 | rangeerknoop Prairies; 144 m |
| b3 | 5 | Edmonton, CN-knoop | 53.5462, -113.4912 | laatste keuze vóór de aftakking; **marker 3.352 m van de lijn** (bevinding uit de kobalt-bake, niet bijgeschoven) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Moa-JV-plant, Moa (HPAL, MSP) | Sherritt 50% / General Nickel Company 50%; sinds 7 mei 2026 gesanctioneerd | lateriet → MSP (Ni+Co) | MSP 2026-guidance 30–32 kt (100%); 2025 MSP-aandeel Sherritt 12,65 kt Ni+Co | [2][3] |
| Fort Saskatchewan-raffinaderij | Sherritt (100%) | MSP → afgewerkt nikkel (briketten/poeder) + kobalt | 38,2 kt Ni+Co/j; 2025 afgewerkt Ni 25,24 kt; sinds 22 jun 2026 in care and maintenance | [1][2][3] |

## 6 · Stoppunt
De brief stopt bij Fort Saskatchewan: afgewerkt class-1-nikkel is het eindproduct en de raffinaderij ligt sinds 22 jun 2026 stil; geen bron noemt een volgende fabriek of afnemer, dus fase D/E vervallen.

## 7 · Open punten
- **`ni-moa-laad` onzeker:** geen bron noemt het laadpunt van de MSP-schepen; de Punta Gorda-steiger is op z15 klein en toont geen bulkinstallatie. Coördinaat niet verzonnen.
- **Halifax-kade:** Sherritt noemt Halifax, niet de terminal [1]; Richmond Terminals is de plausibele breakbulk+rail-kade. Resource World spreekt van MSP "in zakken" naar Halifax [5] (secundaire bron, niet zelf geopend).
- **Geen Moa-specifiek Ni-volume** in een bron; 25,24 kt is het afgewerkte nikkel van de JV-keten (100%), niet per leg. Q2 2026: slechts 934 t MSP tegen 3.238 t een jaar eerder, raffinage tot 22 jun op voorraad [7] (via zoekresultaat, niet zelf geopend).
- **Geen gepubliceerde totaallengte** voor spoor of zee; ±15% is hier een indicatie (spoor −3,2% tegen ~5.000 km ontwerp).
- **Heropening onbekend:** Sherritt wil de JV ontbinden (aug 2026) [4]; de kaart tekent een niet-actieve as.
- **Bevindingen uit de gekopieerde bake:** vier terugloops in b3.3 (Québec → Winnipeg, o.a. 48.2392/-79.0305; eigenschap van het 1-op-1-OSM-net, niet van een via-punt); grootste naad 4,75 km (zee → spoor Halifax, onder de 5 km-norm); marker Edmonton 3,35 km van de lijn.
- **Sitelaag:** `w-fortsaskatchewan-sherritt` (53.7128, -113.2133, stadscentrum) ligt 1,7 km van dit bron-gelegde anker; centraal gelijktrekken. Moa staat niet in de sitelaag.

## 8 · Bronnen
[1] Sherritt, "Metals Operations": MSP per schip naar Halifax, dan trein naar Fort Saskatchewan; 38.200 t Ni+Co/j (100%). https://sherritt.com/Operations/Metals/
[2] Sherritt, persbericht Q4/FY2025 (feb 2026): 25.240 t afgewerkt Ni en 2.728 t Co (100%); MSP 12.650 t contained Ni+Co (2025, Sherritt-aandeel) tegen 15.847 t (2024); 2026-guidance Ni 26–28 kt. https://sherritt.com/?p=15099
[3] Skillings, sluiting Fort Saskatchewan 22-06-2026; OFAC-sanctie 7 mei 2026 op GAESA en Moa Nickel S.A.; Moa-mijn gestopt. https://www.skillings.net/?p=95781
[4] Metalnomist, 24-08-2026: Moa-stop feb 2026, sanctie 7 mei, Sherritt wil de JV ontbinden. https://www.metalnomist.com/2026/08/sherritt-moa-jv-dissolution-marks-break.html
[5] Resource World, "Sherritt tables production update, cuts Canadian staff by 10%": MSP in zakken naar Halifax, dan trein (via zoekresultaat). https://resourceworld.com/sherritt-tables-production-update-cuts-canadian-staff-by-10/
[6] Eigen brief `v2/design/routebrieven/kobalt-moa-fortsaskatchewan.md` (ankers, via-punten, bake-uitkomsten §9, 2026-09-28) en `v2/data/stroomroute-kobalt-moa-fortsaskatchewan.json`.
[7] Engineering News, 13-08-2026, "Sherritt posts first losses from Cuba disruptions" (Q2 2026 MSP-cijfers; via zoekresultaat). https://www.engineeringnews.co.za/article/sherritt-posts-first-losses-from-cuba-disruptions-2026-08-13
[8] Havendata Punta Gorda (offshore-terminal Moa-regio, LOA 134 m) via [6]: https://www.bansarchina.com/largest-cuba-ports/
[9] Port of Halifax, Richmond Terminals (kade-eigen CN-spoor) via [6]: https://www.porthalifax.ca/facilities/hpa-facilities/richmond-terminals/
[10] Esri World Imagery via `sat_check.py` (z15): `v2/build-cache/satcheck/sat-nikkel-moa-fortsaskatchewan-{moa-laad,halifax-kade,fortsask-raffinaderij}.png`; eerdere beelden `sat-kobalt-moa-fortsaskatchewan-*.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-nikkel-moa-fortsaskatchewan.json` (175,8 KB, contract versie 2, lonlat). **Recept:** `bash v2/tools/bak_stromen.sh nikkel-moa-fortsaskatchewan` (functie `bak_nikkel_moa_fortsaskatchewan`, LF). Alle benen zijn letterlijke kopieën van `bak_kobalt_moa_fortsaskatchewan`; geen eigen scan, geen tweede aanloop- of spoorrun.

| # | modaliteit | been | km | punten | opmerking |
|---|---|---|---|---|---|
| b1 | zee, **stippel** | haven-aanloop Moa Bay | 70,9 | 49 | MARNET reikt niet tot de kade; schematisch over water |
| b2 | zee | Moa Bay → Halifax (MARNET) | 2.943,5 | 314 | 38 edges, om de VS heen |
| b3.1 | spoor | Halifax → Moncton | 297,8 | 812 | |
| b3.2 | spoor | Moncton → Québec | 704,6 | 1.509 | |
| b3.3 | spoor | Québec → Winnipeg | 2.477,7 | 5.169 | 4 terugloops (zie lessen) |
| b3.4 | spoor | Winnipeg → Saskatoon | 766,7 | 681 | |
| b3.5 | spoor | Saskatoon → Edmonton | 520,0 | 643 | |
| b3.6 | spoor | Edmonton → Fort Saskatchewan | 73,0 | 209 | kopse aansluiting |

**Totaal 7.854,2 km, 9.386 punten, 8 benen, 8 markers** (precies de verwachting). Spoor totaal 4.839,8 km tegen ontwerp ~5.000 (−3,2%, indicatie; geen gepubliceerde lengte).

**Toelichting.** Stippel alleen b1 (MARNET reikt niet). Geen vlucht, geen leiding, geen weg. "Stilgevallen/gesanctioneerd" staat in titel en beennamen, niet in de lijnstijl.

**Toets.** Naden: alle 0 m behalve zee → spoor Halifax 4,75 km (onder de 5 km-norm; kade-kruis en eerste spoorpunt liggen daar uit elkaar). Markers tot de lijn: Moa 0, Halifax 1,02 km, Moncton 0,18, Québec 0,51, Winnipeg 0,12, Saskatoon 0,14, **Edmonton 3,35 km** (bevinding, niet bijgeschoven), Fort Saskatchewan 0,23. `toets_knikken`: 7 knikken, 5 omkeringen, 4 terugloops, allemaal in b3.3 (zelfde als kobalt). `toets_rechte_benen`: geen doorgetrokken been is recht. json.load: versie 2, lonlat, modaliteiten {zee, spoor}, elk been >= 2 punten.

**Lessen.** (1) Een gedeelde lading met een andere grondstof kost met de kopieermethode 17 s en geen enkele scan. (2) De 4 terugloops in b3.3 en de Edmonton-marker van 3,35 km zijn eigenschappen van het gedeelde kobalt-been; repareren gebeurt bij `kobalt-moa-fortsaskatchewan` zodat beide stromen mee verbeteren. (3) Sitelaag `w-fortsaskatchewan-sherritt` ligt 1,7 km van het bron-gelegde anker: centraal gelijktrekken.
