# Routebrief (licht) · gas — Wheatstone LNG (Onslow, Australië) → Futtsu (Japan)

**stroom-id:** `gas-wheatstone-kawagoe` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** LNG uit Chevron's Wheatstone-plant bij Ashburton North (12 km west van Onslow, WA) wordt aan de exportsteiger geladen en vaart per LNG-tanker via de Straat Lombok, Makassar, de Celebeszee en de Filipijnenzee naar de Futtsu LNG-terminal (JERA/Tokyo Electric) in Tokiobaai.
**Afwijking van het ontwerp:** het id noemt Kawagoe (Chubu, eigen aanname, geen bron); het werkelijke eindpunt is **Futtsu**, want de eerste Wheatstone-lading (12-11-2017, tanker Asia Venture) kwam daar aan [2][3]. Het id blijft, de titel noemt Futtsu.
**Welke as van het verhaal:** Australië (West-Australië) als derde LNG-bron naar Japan; JERA is de grootste koper van Wheatstone: 4,1 + 0,4 Mtpa volgens Chevron-contractlijst [4], 5,2 Mtpa volgens een persbericht-samenvatting [3] = ca. **6,1–7,1 bcm/j** contractvolume (plant 8,9 Mtpa ≈ 12,1 bcm/j) [1][4].

## 1 · Ketenkaart
```
Wheatstone LNG-plant `gas-wh-plant` (Ashburton North, -21.6895/115.0063; sitelaag w-wheatstone)
   ──(plant → steiger: 1,5 km eigen terrein langs de steiger, geen eigen been)──►
Wheatstone LNG-steigerkop `gas-wh-kade` (-21.6760/115.0060)
   ──(b1 haven-aanloop · 95,5 km kade → MARNET-zeeknoop 4120, stippel)──►
   ──(b2 zee · Indische Oceaan → Straat Lombok → Makassar → Celebeszee → Filipijnenzee → Oost-Chinese Zee
       → Tokiobaai · ~7.400 km, MARNET zeeknoop → zeeknoop)──►
   ──(b3 haven-aanloop Futtsu · 14,8 km, LETTERLIJKE KOPIE)──►
Futtsu LNG-terminal `w-futtsu` (JERA/Tokyo Electric, Tokiobaai) — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `gas-wh-kade` → zeeknoop 4120 (-21.62770/114.08300) | haven-aanloop Wheatstone (schematisch, over water — MARNET reikt niet) | 95,5 hemelsbreed; aanloop gemeten 96,7 (94 punten, 0 km over land) | `maak_havenaanloop.py` SLAAGDE (cel 0,005°, 2026-10-30) → `gas-wheatstone-kawagoe-aanloop-wheatstone.geojson` | ja — hier reikt het net niet |
| b2 | B | zee | zeeknoop 4120 → zeeknoop 9066 (35.23890/139.79280) | Lombok → Makassar → Celebeszee → Filipijnenzee → Oost-Chinese Zee → Tokiobaai (aannemelijk: één bron voor de bestemming, geen Kaap-omweg) | ~7.400 (toets); hemelsbreed 6.880; geen gepubliceerde vaarkm | MARNET (zeeknoop → zeeknoop) | nee |
| b3 | B | zee | zeeknoop 9066 → `w-futtsu` | haven-aanloop Futtsu, LETTERLIJKE KOPIE uit `gas-cautionbay-futtsu` | 14,8 (die stroom) | `gas-cautionbay-futtsu-aanloop-futtsu.geojson` | ja — kade 12,1 km van de zeeknoop |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-wh-plant` | site / liquefactie | Wheatstone LNG-plant (Chevron) | -21.6895, 115.0063 | sitelaag `w-wheatstone` (Wikidata Q7991977) [1][7] | bron-gelegd (z15 gezien: twee LNG-tanks, procestrains en een steiger die vanaf het terrein noordwaarts de zee in loopt; het punt ligt op het fabrieksterrein) |
| `gas-wh-kade` | overslag plant → zee / LNG-steigerkop | Wheatstone export-steiger, laadkop | -21.6760, 115.0060 | [5][7] | bron-gelegd (z16 gezien: ~1,4 km lange steiger met pijpbrug, aan de kop een LNG-tanker langszij; de stippel uit het ontwerp (-21.6745/115.0035) lag in open water, 0,3 km westelijk, daarom verlegd) |
| `w-futtsu` | losplek / regas-terminal + centrale | Futtsu LNG-terminal (JERA/Tokyo Electric) | 35.3424, 139.8322 | LETTERLIJK uit `gas-cautionbay-futtsu` / sitelaag `w-futtsu` [2][3][8] | aannemelijk (z15 gezien: LNG-tanks noordwest, centrale in het midden en een LNG-carrier langs de westelijke steiger op ~35.3415/139.8218, ~1 km van het marker-punt; gelaten zoals gekopieerd) |

## 4 · Via-punten
Geen: b2 is een zeebeen zonder corridorkeuze; b1 en b3 zijn haven-aanlopen. Geen landbeen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Wheatstone LNG | Chevron 72% (Woodside 13%, KUFPEC 7%, Shell 6,4%, Kyushu 1,6%) | gas (trunkline ca. 225 km vanaf het offshore-platform) → LNG | 2 treinen 8,9 Mtpa ≈ **12,1 bcm/j** (Wikipedia noemt 15 Mtpa als totaalontwerp) | [1][4][6] |
| Futtsu LNG-terminal | JERA (Tokyo Electric/Chubu) | LNG → hervergast gas, centrale | ~10 Mt/j ontvangst ≈ 13,6 bcm/j (sitelaag; nameplate 22,9 Mtpa) | sitelaag [8] |

## 6 · Stoppunt
De brief stopt bij de Futtsu-terminal: de eerste lading en het JERA-contract (4,5–5,2 Mtpa) noemen deze terminal, maar geen bron noemt een vervolgtraject of fabriek. Fase D/E vervalt. Kawagoe (Chubu) en Shin-Sendai (Tohoku) zijn niet getekend: geen bron koppelt Wheatstone-lading aan die terminals.

## 7 · Open punten
- **Bestemming = "aannemelijk: één bron".** Twee bronnen [2][3] dekken één lading (nov 2017) plus het JERA-contract, geen routinematige leveringen; Chubu (1 Mtpa) en Tohoku (0,9–1 Mtpa) krijgen hun lading op onbekende terminals.
- **JERA-volume verschilt per bron:** 5,2 Mtpa [3] tegen 4,1 + 0,4 Mtpa [4]; hier beide genoemd, geen keuze gemaakt. Per-lading volume onbekend (~70 kt, Asia Venture [2]).
- **Kade ligt 95,5 km van zeeknoop 4120:** de aanloop (b1) is al geprobeerd en slaagde binnen de timeout (96,7 km, 0 km over land, ca. 1,3% van de keten); de MARNET-zeeknoop zelf ligt ver westelijk bij de Pilbara, niet bij Onslow.
- **Zeeafstand geen gepubliceerde waarde:** ~7.400 km is een eigen routeschatting (ontwerp 6.500–7.000), dus de ±15%-toets is alleen een indicatie.
- **Uitval 2026:** Wikipedia meldt Wheatstone en Gorgon eind maart 2026 offline na schade door cycloon Narelle [1]; de huidige stand is niet nagecheckt.
- **Futtsu-berth:** de losplek ligt volgens het beeld ~1 km westelijk van het marker-punt; de aanloop is letterlijk gekopieerd en eindigt op het marker-punt (naad 0).
- **Pijpleiding platform → plant (225 km, subzee)** niet getekend: geen coördinaat van het platform gevonden, niet verzonnen.

## 8 · Bronnen
[1] Wikipedia, "Wheatstone LNG": locatie 12 km west van Onslow, operator Chevron, eigenaren, 15 Mtpa totaal, afnemers (Tokyo Electric 3,1; KOGAS 1,5; Tohoku 1; Chubu 1; Kyushu 0,3 Mtpa), cycloonschade maart 2026. https://en.wikipedia.org/wiki/Wheatstone_LNG
[2] LNG Industry, 13-11-2017, "JERA imports first LNG cargo shipped from Wheatstone": aankomst op Futtsu LNG-terminal, tanker Asia Venture, ~70.000 t. https://www.lngindustry.com/lng-shipping/13112017/jera-imports-first-lng-cargo-shipped-from-wheatstone
[3] SAFETY4SEA, "JERA receives first LNG cargo from Wheatstone project" (12-11-2017 aankomst, TEPCO Futtsu terminal, JERA-contract 5,2 Mtpa). https://safety4sea.com/jera-receives-first-lng-cargo-from-wheatstone-project
[4] NS Energy, "Wheatstone LNG Project": 2 treinen 8,9 Mtpa, trunkline ~225 km, export-steiger, JERA 4,1 + 0,4 Mtpa, Tohoku 0,9, Kyushu 0,7 Mtpa. https://www.nsenergybusiness.com/projects/wheatstone-lng-project-australia
[5] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16): `sat-gas-wheatstone-kawagoe-plant.png`, `…-steiger.png`, `…-kade.png`.
[6] Chevron Australia, Wheatstone project (de pagina en het overzichts-pdf gaven HTTP 403, niet gelezen; gelezen via zoekresultaat-samenvatting).
[7] `v2/design/gas-sitelaag.json`, anker `w-wheatstone` (-21.6895/115.0063), capaciteit 12,1 bcm/j.
[8] `v2/design/routebrieven/gas-cautionbay-futtsu.md` en `v2/data/stroomroute-gas-cautionbay-futtsu.json`: Futtsu-marker, aanloop-geojson, zeeknoop 9066 (sat: `sat-gas-wheatstone-kawagoe-futtsu.png`).
[9] Ketenontwerp en haalbaarheidstoets M31 golf 15 (workflow-invoer): zeeknoop 4120 op 95,7 km, aanpassing Futtsu.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Recept:** `bash v2/tools/bak_stromen.sh gas-wheatstone-kawagoe` (functie `bak_gas_wheatstone_kawagoe`) → `v2/data/stroomroute-gas-wheatstone-kawagoe.json` (17,2 KB). Eén `hecht_marnet.py route` met drie benen in reisvolgorde, 2 markers (`gas-wh-kade`, `w-futtsu`); geen wegprofiel, geen extract, geen via-punt.

| # | modaliteit | been | km | punten | stippel | naad |
|---|---|---|---|---|---|---|
| 1 | zee | haven-aanloop Wheatstone (kade → zeeknoop 4120) | 96,7 (brief 95,5 hemelsbreed) | 94 | ja | start |
| 2 | zee | LNG-tanker Wheatstone → Futtsu (MARNET 4120 → 9066, aannemelijk: één bron) | 7.399,8 (brief ca. 7.400, eigen schatting) | 755 | nee | 0,0 km |
| 3 | zee | haven-aanloop Futtsu (zeeknoop 9066 → kade, LETTERLIJKE KOPIE uit gas-cautionbay-futtsu) | 14,8 | 12 | ja | 0,0 km |

Totaal 7.511,3 km · 861 punten · 2 markers (0,0 km van de lijn) · alle naden 0 · 1,5% stippel.

**Toets:** zeebeen +0,0% tegen de schatting van ca. 7.400 km (indicatie, geen gepubliceerde vaarkm). `toets_knikken`: 1 knik van 75,5 graden (R 7.988 m, -20.1880/116.6645, krappe bocht op open zee), 0 omkeringen. `json.load` ok, versie 2, punt_formaat lonlat, alleen modaliteit zee. `bak_stromen.sh` 0 CRLF.
**Corridor:** de lijn passeert Lombok op 3 km, Makassar op 79 km en de Celebeszee op 7 km (hemelsbreed tot een controlepunt), en houdt Luzon op ca. 750 km; geen Kaap-omweg.
**Toelichting stippel/aanloop:** b1 is een haven-aanloop (kade 95,5 km van MARNET-zeeknoop 4120, ver buiten de 25 km-snap): `maak_havenaanloop.py` slaagde (96,7 km, 0 km over land), doorgezet als `--stippel-geojson`. b3 is de bestaande aanloop van `gas-cautionbay-futtsu`, ongewijzigd gekopieerd (kade 12,1 km van zeeknoop 9066).
**Lessen/bevindingen:** (1) de MARNET-zeeknoop 4120 ligt westelijk bij de Pilbara terwijl de steiger bij Onslow oostelijker ligt: de aanloop loopt dus eerst ca. 95 km west en de tanker keert daarna oostwaarts naar Lombok (een uitholling door de knoopkeuze, geen echte vaarroute; `toets_knikken` meldt geen omkering). (2) Het eindpunt is Futtsu, niet Kawagoe: het id blijft, de titel noemt Futtsu. (3) Niet gemeten: de huidige stand van de plant na cycloon Narelle (maart 2026).
