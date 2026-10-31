# Routebrief (licht) · Zilver — Salares Norte → Santiago (SCL) → Zürich (ZRH) → MKS PAMP (Zwitserland, aannemelijk)

**stroom-id:** `zilver-salaresnorte-pamp` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** zilverdoré (zilver-doréstaven) van de Salares Norte-plant (Gold Fields, 4.200–4.700 m, Atacama) per truck via
C-167/Diego de Almagro/C-17/Ruta 31-30/Ruta 5 naar de vrachtterminal van Santiago (SCL), per vrachtvlucht (grootcirkel) naar de
vrachtterminal van Zürich (ZRH) en per truck over de A2/Gotthard naar de LBMA-raffinaderij MKS PAMP, Castel San Pietro. Eindpunt
Zwitserland is **aannemelijk** (20-F: "India of Zwitserland").
**Welke as van het verhaal:** doré naar de raffinaderij, de rol die zilver op de bol nog mist: zilver als gekoppeld product van een
goudmijn, zonder eigen concentraat. Volume **70,5 t Ag/j** = 2.268.179 oz zilver verkocht in 2025 (1 oz = 31,1035 g) [1]; peiljaar 2025
is het eerste jaar met commerciële productie (vanaf 31-08-2025), 2026-guidance 525–550 koz Au-eq [1]. Zilverdoré en gouddoré zijn beide
doré die naar dezelfde raffinaderij gaan [1]; geometrie is bewust een letterlijke kopie van `goud-salaresnorte-pamp` (§7).

## 1 · Ketenkaart
```
Salares Norte-plant `ag-salaresnorte-plant`
  ──(b1 truck · C-167 → Diego de Almagro → C-17 → Ruta 31/30 → Ruta 5 → Vespucio Norte · 1.137,9 km gemeten, kopie goud b1)──►
Santiago vrachtterminal (SCL) `ag-scl-vrachtterminal`  ──(b2 stippel · last mile airside 0,15 km)──►
  ──(b3 lucht · SCL → ZRH, grootcirkel, aannemelijk · 11.957,6 km, kopie goud b3)──►
Zürich vrachtplatform (ZRH) `ag-zrh-vrachtterminal`  ──(b4 stippel · last mile airside 0,91 km)──►
  ──(b5 truck · A1/A4 Knonaueramt → A14 → A2 Gotthard · 263,3 km, kopie goud b5)──► MKS PAMP `ag-pamp-raffinaderij` ── stoppunt
```

## 2 · Benen (alle vijf: LETTERLIJKE KOPIE van de benen van `goud-salaresnorte-pamp`, bestand/regel genoemd)
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Salares Norte-plant → openbare weg bij SCL (aannemelijk: één bron) | C-13/C-173/C-167 → Diego de Almagro → C-17 → Ruta 31/30 → Ruta 5 (bypass Copiapó) → Vespucio Norte | 183 mijn → Diego de Almagro [1]; verder geen wegkm-bron; hemelsbreed 842 km, geen wegkm; gemeten 1.137,9 (goud b1) | kopie `goud-salaresnorte-pamp-weg-plant-scl.geojson` | nee |
| b2 | A | truck | openbare weg (Osvaldo Croquevielle) → SCL-vrachtterminal | last mile airside | 0,15 hemelsbreed [goud b2] | stippel (kopie goud-regel) | **ja**: airside/privéterrein |
| b3 | B | lucht | SCL → ZRH (aannemelijk: één bron noemt Zwitserland of India) | vrachtvlucht, grootcirkel | 11.957,6 [goud b3, berekend] | kopie `goud-salaresnorte-pamp-lucht-scl-zrh.geojson` | nee, doorgetrokken |
| b4 | B | truck | ZRH-vrachtplatform → openbare weg (47,4721, 8,5545) | last mile airside | 0,91 [goud b4 = goud-pamp-shanghai] | stippel (kopie goud-regel) | **ja**: airside |
| b5 | C | truck | openbare weg ZRH → MKS PAMP | A1/A4 Knonaueramt → A14 → A2 Gotthard | 263,3 gemeten [goud b5] | kopie `goud-salaresnorte-pamp-weg-zrh-pamp.geojson` (ligt al ZRH → PAMP; NIET opnieuw omkeren) | nee |

## 3 · Ankers (hergebruikt uit `goud-salaresnorte-pamp`; id-prefix `ag-`, coördinaten letterlijk gelijk aan het goud-anker)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-salaresnorte-plant` | mijn / laadplek | Salares Norte, verwerkingsplant (Gold Fields) | -26.0220, -68.8917 | [1][2][3] | bron-gelegd (z15 opnieuw gezien 2026-10-31: molen-/tankcluster ZO van de dagbouw, kampmodules ten NW; het 20-F-punt -26.0117, -68.8931 ligt in de put; `sat-zilver-salaresnorte-pamp-plant.png`) |
| `ag-scl-vrachtterminal` | overslag / lucht | Santiago (SCL), internationale vrachtzone, loods aan het platform | -33.4105, -70.7874 | [3][7] | bron-gelegd, pand **onzeker** (z15 gezien: grote witte loods met docks ten Z van de passagiersterminal, kruis erop; `sat-zilver-salaresnorte-pamp-scl-cargo.png`) |
| `ag-zrh-vrachtterminal` | overslag / lucht | Zürich Airport vrachtplatform (hergebruikt goud-pamp-shanghai) | 47.4647, 8.5492 | [4] | bron-gelegd (daar gezien) |
| `ag-pamp-raffinaderij` | raffinaderij | MKS PAMP SA, Via alle Zocche 1, Castel San Pietro (hergebruikt) | 45.8546, 9.0025 | [4] | bron-gelegd (daar gezien); afnemer aannemelijk, geen India-alternatief getekend |

## 4 · Via-punten (alleen b1; de acht van de gekopieerde wegscan, lat, lon, geen stadscentrum, geen nieuwe scan nodig)
| # | punt | lat, lon | waarom hier |
|---|---|---|---|
| 1 | C-167, W van de C-173-aansluiting | -26.4043, -69.8901 | mijnweg bereikt Diego de Almagro alleen via C-167 |
| 2 | C-17 ten Z van Inca de Oro | -26.8938, -69.9199 | binnenlandroute C-17/Ruta 31 boven C-13 west/Ruta 5 kust |
| 3 | Ruta 30, W van Tierra Amarilla | -27.5015, -70.4088 | Copiapó-vallei in zonder stadscentrum |
| 4 | Ruta 5 Norte, bypass Copiapó zuidkop | -27.5060, -70.4491 | Ruta 5 zuidwaarts |
| 5 | Ruta 5 Norte, N van La Serena | -29.8174, -71.2746 | Ruta 5, geen kustweg |
| 6 | Ruta 5 Norte, N van Los Vilos | -31.8403, -71.5156 | kustvariant van Ruta 5 |
| 7 | Ruta 5 Norte bij Tiltil | -32.9352, -70.8138 | Ruta 5, niet Ruta 68 |
| 8 | Autopista Vespucio Norte (ref 70) | -33.4053, -70.7821 | ring naar Autopista Aeropuerto, niet door het centrum |
Eindpunt wegprofiel: Osvaldo Croquevielle (service) -33.4108, -70.7890. Extracts: b1 chili, b5 zwitserland (beide al gescand in goud-salaresnorte-pamp; de bak-agent hoeft niet te scannen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Salares Norte | Gold Fields | erts → goud- en zilverdoré (de plant maakt "silver doré bars") | 2.268.179 oz Ag + 363.573 oz Au verkocht 2025 (396,5 koz Au-eq) | [1] |
| MKS PAMP | MKS PAMP SA | doré → LBMA-baren | niet Salares-specifiek; offtake tot 31-12-2026, verlenging mogelijk | [1] |

## 6 · Stoppunt
Stoppunt MKS PAMP: het 20-F noemt de raffinaderij als afnemer (FCA, via MKS-agent, "India of Zwitserland") en geen bron noemt een volgende bestemming van het zilver. Fase D/E vervallen.

## 7 · Open punten
- **BINDEND:** Zwitserland is een keuze: het 20-F noemt India óf Zwitserland (MKS-raffinaderijen), vervoerswijze en luchthaven zijn niet gebrond. Beennamen b1 en b3 dragen "aannemelijk"; blijkt het India, dan wijzigt het eindpunt in de titel.
- MKS-raffinage- en offtake-overeenkomst loopt tot 31-12-2026 (verlenging mogelijk) [1]: over twee maanden verlopen; de brief tekent de situatie van peiljaar 2025.
- **Geometrie 100% gelijk aan `goud-salaresnorte-pamp`** (zelfde doré, zelfde raffinaderij): bewuste keuze van de ontwerptoets (reserve-as), geen tweede onderzoek. Zilver-doré en goud-doré kunnen in dezelfde zending zitten; het 20-F scheidt de transportstroom niet.
- Het zilveraandeel per staaf doré is niet gebrond; 70,5 t Ag/j is de verkochte hoeveelheid (alle zilver, ook als gemengd doré), geen apart staafvolume.
- Geen directe vrachtvlucht SCL → ZRH gevonden: één grootcirkel is de tekenaanname (tussenlanding in een hub niet gebrond).
- b1: wegkm niet gebrond (hemelsbreed 842 km, geen wegkm; 183 km mijn → Diego de Almagro [1]); de 1.137,9 km is gebakken OSM-meting, geen ±15%-norm.
- SCL-loods niet pandgenaamd; ZRH-platform airside (patroon b4 = goud-pamp-shanghai).

## 8 · Bronnen
[1] Gold Fields, Form 20-F FY2025: 2.268.179 oz zilver + 363.573 oz goud verkocht 2025; "Salares Norte also produces silver doré bars"; doré naar MKS PAMP, FCA, raffinaderijen in India of Zwitserland; overeenkomst tot 31-12-2026 (gelezen 2026-10-31). https://www.sec.gov/Archives/edgar/data/1172724/000162828026021904/gfi-20251231.htm
[2] Gold Fields, Technical Report Summary Salares Norte 2024 (UTM 510481 E, 7123125 N). https://www.sec.gov/Archives/edgar/data/1172724/000117272425000010/a964-technicalreportsummar.htm
[3] Routebrief goud-salaresnorte-pamp.md (ankers, via-punten, gebakken benen, 1.137,9 km) — `v2/design/routebrieven/goud-salaresnorte-pamp.md`.
[4] Routebrief goud-pamp-shanghai.md (ZRH- en PAMP-anker, b1 263,3 km, ZRH-stippel 0,91 km).
[5] OEC, Gold exports of Chile (Zwitserland grootste bestemming; indirect, via [3]). https://www.oec.world/profile/bilateral-product/gold/reporter/chl
[6] Wikipedia, Copiapó (ca. 800 km ten noorden van Santiago; via [3]). https://en.wikipedia.org/wiki/Copiap%C3%B3
[7] OpenStreetMap (ODbL): wegvertices en vrachtobjecten SCL (via [3]). https://www.openstreetmap.org
Satellietblik (Esri z15, 2026-10-31): `v2/build-cache/satcheck/sat-zilver-salaresnorte-pamp-plant.png`, `sat-zilver-salaresnorte-pamp-scl-cargo.png`; ZRH en PAMP daar gezien (zie [3][4]).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
Stroom `zilver-salaresnorte-pamp` gebakken via `bash v2/tools/bak_stromen.sh zilver-salaresnorte-pamp` (functie `bak_zilver_salaresnorte_pamp`), uitvoer `v2/data/stroomroute-zilver-salaresnorte-pamp.json` (467,5 KB, 22.761 punten, 5 benen, 4 markers, 13.359,9 km). Geen nieuwe scan, geen profiel, geen nieuwe geojson: alle vijf benen zijn letterlijke kopieën van `goud-salaresnorte-pamp`.

| # | modaliteit | km gebakken | brief | opmerking |
|---|---|---|---|---|
| b1 | truck, doorgetrokken | 1.137,9 | hemelsbreed 842, geen wegkm: indicatie, geen ±15%-norm | kopie `goud-salaresnorte-pamp-weg-plant-scl.geojson`, 16.123 punten |
| b2 | truck, STIPPEL | 0,15 | 0,15 | SCL-vrachtplatform last mile, airside |
| b3 | lucht, doorgetrokken | 11.957,6 | 11.957,6 | kopie `goud-salaresnorte-pamp-lucht-scl-zrh.geojson`, 480 punten, grootcirkel |
| b4 | truck, STIPPEL | 0,91 | 0,91 | ZRH-vrachtplatform last mile, airside |
| b5 | truck, doorgetrokken | 263,3 | 263,3 | kopie `goud-salaresnorte-pamp-weg-zrh-pamp.geojson`, ligt al ZRH naar PAMP, niet omgekeerd |

Naden alle 0,00 km; markers alle 0,0 km van hun lijn; geen zee, haven-aanloop of leiding.
**Recept:** functie in `bak_stromen.sh` = `bak_goud_salaresnorte_pamp` met stroom-id, titel, marker-prefix `ag-` en brief-pad aangepast; geen slot-scan nodig (alleen de bake).
**Toelichting stippels:** b2 en b4 zijn "hier reikt het net niet": een vrachtplatform ligt airside/privéterrein zonder wegpad. De vlucht is doorgetrokken; "aannemelijk: Zwitserland of India" staat in de beennaam, niet in de lijnstijl.
**Bevindingen:** (1) Geometrie 100% gelijk aan het goudstroom-bestand: zilver en goud worden op de bol twee identieke lijnen op elkaar (bewuste reserve-as); het volume (70,5 t Ag/j) is het enige verschil. (2) bestand 467 KB > ~300 KB-richtlijn door de 16.123 punten van b1; niet herbakken, de bundel simplificeert. (3) toets_knikken: 60 knikken, 4 omkeringen, 1 TERUGLOOP op -26,4045/-69,5906 (zijspoor ~40 m bij Diego de Almagro), identiek aan goud-salaresnorte-pamp; geen spikes die een ander gedrag tonen. (4) Open punten uit §7 blijven staan (India mogelijk, offtake tot 31-12-2026, geen directe vrachtvlucht SCL-ZRH).
**Lessen:** een stroom die geometrie 1-op-1 deelt kost 18 s bakken; bij een gedeeld been kopieer je de function-regel, niet de geojson.
