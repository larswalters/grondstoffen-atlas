# Routebrief (licht) · goud — Gold Fields Tarkwa (Ghana) → Accra (ACC) → Delhi (DEL) → MKS PAMP India (Rojka Meo)

**stroom-id:** `goud-tarkwa-mkspampindia` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** doré/baar uit de Gold Fields Tarkwa-fabriek per **truck** (letterlijke kopie goud-tarkwa-dubai b1) naar de
vrachtterminal van Accra/Kotoka, per **vrachtvlucht** (grootcirkel, aannemelijk: één bron) naar het Delhi Air Cargo Complex, en per **truck**
(letterlijke kopie goud-dubai-delhi b3) naar de MKS PAMP-raffinaderij in India, Rojka Meo (Sohna/Nuh, Haryana).
**Welke as van het verhaal:** *Ghana → India: het contractuele standaardpad van Tarkwa-goud* — Gold Fields 20-F 2025: de MKS-raffinageovereenkomst
(3-6-2021) laat MKS het goud ophalen bij de goudkamer van Tarkwa en vervoeren naar de Zwitserse of de Indiase raffinaderij; **India is de
standaard** tenzij een partij kennisgeeft [1]. Volume: Tarkwa verkocht in 2025 **474.200 oz = 14,7 t Au/j** (474.200 ÷ 32,15) [1]; het aandeel dat
naar India gaat is niet gepubliceerd. Haalbaarheidstoets: haalbaar, BINDEND: b1 en b3 letterlijke kopie, b2 aannemelijk.

## 1 · Ketenkaart
```
Gold Fields Tarkwa-fabriek `au-tarkwa-mill`
   ──(b1 truck · Twifo Praso–Assin Fosu–Agona Swedru–Kasoa · 279,4 km gemeten, letterlijke kopie goud-tarkwa-dubai b1)──►
   Accra/Kotoka vrachtterminal `au-air-acc-cargo`
   ──(b2 lucht · vrachtvlucht ACC → DEL, grootcirkel · 8.468,7 km eigen berekening, aannemelijk: één bron)──►
   Delhi Air Cargo Complex `au-air-del`
   ──(b3 truck · NH48 Delhi–Gurugram → Sohna Road · 45,4 km gemeten, letterlijke kopie goud-dubai-delhi b3)──►
   MKS PAMP India, Rojka Meo `au-ref-mmtc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `au-tarkwa-mill` → `au-air-acc-cargo` | Twifo Praso, Assin Fosu, Agona Swedru, Kasoa (letterlijke kopie goud-tarkwa-dubai b1) | 279,4 gebakken; Gold Fields: "approximately 300 kilometres by road" naar Accra/Tema [2][3] | kopie goud-tarkwa-dubai-weg-mill-acc.geojson | nee |
| b2 | B | lucht | `au-air-acc-cargo` → `au-air-del` | vrachtvlucht ACC → DEL, grootcirkel (aannemelijk: één bron voor het vervoer, luchthaven niet genoemd) | 8.468,7 [eigen berekening, maak_luchtbeen] | maak_luchtbeen | nee, doorgetrokken |
| b3 | C | truck | `au-air-del` → `au-ref-mmtc` | NH48 Delhi–Gurugram, Sohna Road (letterlijke kopie goud-dubai-delhi b3) | 45,4 gebakken; brief dubai-delhi: ca 50–55 hemelsbreed+omweg [3] | kopie goud-dubai-delhi-weg-del-mmtc.geojson | nee |

Totaal ca 8.793 km. Geen zeebeen, dus geen haven-aanloop. Geen tussenlanding: geen bron noemt een hub, één directe vlucht aangenomen.

## 3 · Ankers (alle vier hergebruikt, letterlijk; geen nieuwe satellietblik nodig)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-tarkwa-mill` | mijn/fabriek (kop b1) | Gold Fields Tarkwa, CIL-verwerkingsfabriek | 5.3275, -2.0215 | brief goud-tarkwa-dubai [1][5] | bron-gelegd (z17 daar gezien: procesgebouwen, slibindikker, conveyor) |
| `au-air-acc-cargo` | vrachtterminal (truck → lucht) | Accra/Kotoka Intl, vrachtterminal (Ghana Airport Cargo Center) | 5.5985, -0.1745 | brief goud-tarkwa-dubai [5] | bron-gelegd (z18 daar gezien: vrachtloods aan het platform, vrachttoestel ervoor) |
| `au-air-del` | vrachtterminal (lucht → truck) | Delhi Air Cargo Complex, IGI Airport (bij Terminal 3) | 28.5570, 77.1000 | brief goud-dubai-delhi [6] | bron-gelegd met voorbehoud (z16 daar gezien: loodsen + platform; grens naast onderhoudshangar niet scherp) |
| `au-ref-mmtc` | raffinaderij (stoppunt) | MKS PAMP India (juridisch MMTC-PAMP India Pvt Ltd), Rojka-Meo Industrial Estate, Nuh | 28.2140, 77.0611 | brief goud-dubai-delhi [4][6] | bron-gelegd (z15 daar gezien: industrieel complex met blauw/witte hallen; OSM-gebouw "MMTC PAMP ROJKA MEO") |

Ankers staan ook letterlijk in `v2/data/stroomroute-goud-tarkwa-dubai.json` en `-dubai-delhi.json` en in goud-sitelaag.json (w-tarkwa, w-ref-mmtcpamp).

## 4 · Via-punten (alleen in de kopie-benen; ongewijzigd uit de bronbrieven)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Twifo Praso | 5.6116, -1.5497 | pint de inland-route i.p.v. de kustroute via Takoradi |
| b1 | 2 | Assin Fosu | 5.7005, -1.2769 | doorgaande knoop op dezelfde corridor |
| b1 | 3 | Agona Swedru | 5.5345, -0.7008 | corridor buigt naar Kasoa i.p.v. Cape Coast |
| b1 | 4 | Kasoa | 5.5326, -0.4375 | laatste grote knoop vóór Accra/Kotoka |
| b3 | 1 | Rajokri, NH48 | 28.5031, 77.1111 | Delhi/Haryana-grens, begin Delhi–Gurugram Expressway |
| b3 | 2 | Gurugram, Sohna Road-afslag | 28.4560, 77.0290 | corridor verlaat NH48 |
| b3 | 3 | Sohna | 28.2500, 77.0700 | laatste grote plaats vóór Rojka Meo |
Extracts: b1 ghana; b3 india. Er is geen nieuw wegprofiel nodig: beide geojsons bestaan al.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tarkwa-fabriek | Gold Fields Ghana Ltd | erts → doré/baar (goudkamer = leveringsplaats) | 474.200 oz verkocht in 2025 (14,7 t) | [1] |
| MKS PAMP India (MMTC-PAMP India Pvt Ltd) | MKS PAMP-groep / MMTC (JV) | doré → LBMA-baren | sitelaag: nameplate ca 200 t/j, niet onafhankelijk herbevestigd | [4] |

## 6 · Stoppunt
De brief stopt aan de poort van de Indiase raffinaderij: het 20-F noemt de raffinaderij als eindbestemming ("gold is then refined"); geen bron noemt een
volgende afnemer van de baren. Fase D/E vervallen.

## 7 · Open punten
- **b2 is aannemelijk (één bron):** het 20-F zegt dat MKS het goud ophaalt en naar India of Zwitserland brengt, maar noemt geen luchtvracht, geen
  Accra en geen Delhi. Vlucht ACC → DEL en de keuze van het Delhi Air Cargo Complex zijn een aanname (beennaam draagt "aannemelijk").
- **Zwitserland is het alternatief:** MKS mag per zending naar Zwitserland kennisgeven (feestdag in India/zwakke vraag, of gewijzigde importregels) [1].
  Blijkt het vaker Zwitserland, dan hoort er een Ticino-variant bij (b2 ACC naar ZRH, zie goud-loulo-ticino); hier is India getekend.
- **Naam:** het 20-F noemt alleen "MKS refinery in India". Dat dit de MMTC-PAMP-vestiging in Rojka Meo is, is afgeleid: MKS PAMP presenteert MMTC-PAMP als
  groepsentiteit en de bedrijfssite noemt MMTC-PAMP India Pvt Ltd, Rojka-Meo Industrial Estate, Nuh [4]. Geen bron voor een formele naamswijziging naar "MKS PAMP India"; titel
  en beennamen gebruiken "MKS PAMP India" op besluit van de haalbaarheidstoets, de legale naam staat in §3.
- **Overlap:** b1 en b3 zijn kopieën en de grootcirkel ACC–DEL ligt ca 129 km van het bestaande ACC–DXB–DEL: visueel bijna dezelfde lijn als goud-tarkwa-dubai plus
  goud-dubai-delhi. De Dubai-ketens zijn mogelijk achterhaald (20-F: India is standaard); centraal opmerken, niet hier oplossen.
- **Volume:** 14,7 t is Tarkwa-verkoop 2025 totaal [1]; het aandeel naar India is niet gepubliceerd. Het v1-register (ca 17 t/j) is niet gebruikt.
- **Risico:** Tarkwa-leases (vijf) verlopen april 2027, verlenging aangevraagd [1]; status onbekend. Ghana verschuift beleid naar lokale raffinage (GoldBod) [7].
- **Last mile:** geen airside-stippel nodig: b1 en b3 zijn kopieën die zonder stippel zijn gebakken (anker 0,01–0,2 km van het net).
- **Km:** b1 en b3 zijn gebakken wegkilometers (kopie); de gepubliceerde ~300 km voor b1 is een bedrijfsopgave naar Accra/Tema, niet corridor-specifiek (-6,9% daar).

## 8 · Bronnen
[1] Gold Fields Ltd, Form 20-F 2025, "Refining and Marketing, Ghana" (MKS-overeenkomsten 3-6-2021, India standaard, goudkamer als leveringsplaats), Tarkwa gold sold 474.200 oz, leases april 2027.
https://www.sec.gov/Archives/edgar/data/1172724/000162828026021904/gfi-20251231.htm (gelezen: pagina's Refining and Marketing + Operating Results)
[2] Routebrief goud-tarkwa-dubai.md (b1, ankers; Gold Fields "approximately 300 kilometres by road") en `stroomroute-goud-tarkwa-dubai.json`.
[3] Routebrief goud-dubai-delhi.md (b3, ankers, via-punten Rajokri/Gurugram/Sohna) en `stroomroute-goud-dubai-delhi.json`.
[4] MMTC-PAMP India Pvt Ltd, bedrijfssite (contact: Rojka-Meo Industrial Estate, Nuh, Haryana 122103; "An MKS PAMP GROUP Company") https://www.mmtcpamp.com/ ·
Wikipedia "MKS PAMP" (groepsentiteiten incl. MMTC-PAMP) https://en.wikipedia.org/wiki/MKS_PAMP · BIS-raffinagelijst https://www.bis.gov.in/wp-content/uploads/2022/11/Refineries-latest-list.pdf
[5] Esri World Imagery via sat_check.py (hergebruik): `v2/build-cache/satcheck/sat-goud-tarkwa-dubai-mijn-plant4.png`, `sat-goud-tarkwa-dubai-kotoka-cargo3.png`.
[6] Esri World Imagery (hergebruik): `sat-goud-dubai-delhi-del-cargo-zoom1.png`, `sat-goud-dubai-delhi-mmtc-rojkameo.png`.
[7] Engineering News 9-3-2026, "Ghana looks to shift artisanal gold refining amid Dubai flight disruptions"
https://www.engineeringnews.co.za/article/ghana-looks-to-shift-artisanal-gold-refining-amid-dubai-flight-disruptions-say-sources-2026-03-09 ·
GNA, PMMC-assaycentrum op Kotoka (goud wordt via KIA geëxporteerd) https://gna.org.gh/?p=141448
[8] Eigen berekening ACC–DEL: `python v2/tools/maak_luchtbeen.py` droogloop, 8.468,7 km grootcirkel, 340 punten.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
`bash v2/tools/bak_stromen.sh goud-tarkwa-mkspampindia` → `v2/data/stroomroute-goud-tarkwa-mkspampindia.json` (109,7 KB, versie 2, lonlat), 3 benen, **8.793,5 km**, 5.850 punten, 4 markers.

| # | modaliteit | km gebakken | km brief | afwijking | naad | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | 279,4 | ca 300 (Gold Fields, naar Accra/Tema) | -6,9% | - | nee |
| b2 | lucht | 8.468,7 | 8.468,7 (eigen berekening) | 0% | 0,0 km | nee, doorgetrokken |
| b3 | truck | 45,4 | 50-55 (hemelsbreed+omweg, geen wegkm) | indicatie -9% | 0,0 km | nee |

**Recept:** b1 en b3 zijn letterlijke kopieën (`--been-geojson` verwijst naar `goud-tarkwa-dubai-weg-mill-acc.geojson` en `goud-dubai-delhi-weg-del-mmtc.geojson`, geen tweede versie); b2 via `python v2/tools/maak_luchtbeen.py --van "Accra vrachtterminal|5.5985,-0.1745" --naar "Delhi Air Cargo Complex|28.5570,77.1000" --uit v2/build-cache/ais/graaf/goud-tarkwa-mkspampindia-lucht-acc-del.geojson` (8468,7 km, 340 punten). Functie `bak_goud_tarkwa_mkspampindia()`. Geen wegprofiel, geen wegscan, geen zeebeen, geen haven-aanloop, geen stippel.

**Toets:** naden 0,0 km; vier markers 0,0 m van hun lijn (ankers zijn lijneinden); modaliteiten truck/lucht/truck; `toets_rechte_benen` geen treffer voor deze stroom. `toets_knikken`: de spikes en omkeringen zitten in de gekopieerde b3 (Delhi/Gurugram, wissel- en klaverbladlussen) en zijn bronstroom-eigenschappen, hier niet aangeraakt.

**Vlucht:** b2 is aannemelijk (één bron, geen luchtvracht in het 20-F genoemd); dat staat in de beennaam en in §7, niet in de lijnstijl. Geen tussenlanding.

**Lessen / meldingen:** de grootcirkel ACC-DEL ligt ca 129 km van ACC-DXB-DEL; visueel bijna dezelfde lijn als goud-tarkwa-dubai plus goud-dubai-delhi (centraal opmerken). b3 km is een gebakken wegkm, de brief-schatting is hemelsbreed+omweg.
