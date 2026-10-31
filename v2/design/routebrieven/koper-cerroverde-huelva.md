# Routebrief (licht) · koper — Cerro Verde → Matarani → Huelva (Spanje)

**stroom-id:** `koper-cerroverde-huelva` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** koperconcentraat van de Cerro Verde-concentrator (SMCV, Arequipa, Peru; Freeport 55,1 %) per **truck** over de mijnweg langs de Quebrada San José naar het PeruRail-station La Joya, per **spoor** naar Matarani en de Tisur-pier Muelle F, per **zeeschip** door Panama over de Atlantische Oceaan naar **Puerto de Huelva** (Puerto Exterior, losplek niet gebrond), daarna per **truck** naar de **Atlantic Copper-smelter** (Punta del Sebo, Huelva) — daar stopt deze brief. **Eindpunt = aannemelijk: één bron** (Atlantic Copper koopt 15 % van zijn concentraat bij FCX Zuid-Amerika; de mijn Cerro Verde en de losplek zijn afgeleid).
**Welke as van het verhaal:** Zuid-Amerikaans concentraat naar de Spaanse smelter van dezelfde eigenaar (Atlantische route). **Volume: geen kt-cijfer gepubliceerd.** FCX 10-K 2024: Atlantic Copper kocht 15 % van zijn concentraat bij FCX' Zuid-Amerika-operaties (13 % Indonesië, 2 % Noord-Amerika, 70 % derden) [1]. Peiljaar 2024. Een omrekening naar kt Cu (15 % van 247,6 kt anode ≈ 37 kt) is een eigen rekensom op een inkoopaandeel en wordt niet als volume gebruikt.

## 1 · Ketenkaart
```
Cerro Verde-concentrator ──(b1 truck · mijnweg Quebrada San José · OSM-pad 47 km)──► La Joya-station
  `cu-cerroverde-laad`                                                               `cu-lajoya-overslag`
──(b2 spoor · Ferrocarril del Sur · 59 km)──► spooreinde ──(b3 stippel 1,7 km)──► Muelle F `cu-matarani-kade`
──(b4 stippel haven-aanloop 72,1 km)──► zeeknoop 489 ──(b5 zee · MARNET · 11.451 km, via Panama)──► Huelva-zeeknoop 8016
──(b6 stippel haven-aanloop 7,8 km)──► Puerto Exterior `cu-huelva-terminal` ──(b7 truck · N-442/H-30 · aannemelijk)──► Atlantic Copper `cu-atlanticcopper-smelter` ⏹
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | concentrator → La Joya-station | mijnweg Quebrada San José, openbare-wegbenadering van de 40 km privéweg; **letterlijke kopie koper-cerroverde-toyo b1** [2] | hemelsbreed 36 km, geen wegkm; OSM-pad 47,0 km | kopie `koper-cerroverde-toyo-weg-cerroverde-lajoya.geojson` | nee |
| b2 | A | spoor | La Joya → spooreinde Matarani | Ferrocarril del Sur (PeruRail); **kopie cerroverde-toyo b2** | ca. 60 (MINEM), gemeten 59,2; FCX: ca. 70 mijl truck plus spoor [1] | kopie `spoorroute-koper-cerroverde-toyo-lajoya-matarani.geojson` | nee |
| b3 | A | spoor | spooreinde → Muelle F | havenspoor, geen net; **kopie cerroverde-toyo b3** | 1,7 hemelsbreed | stippel (kopie) | **ja** — haventerrein, geen net |
| b4 | B | zee | Muelle F → zeeknoop 489 (-17.3000,-72.7000) | haven-aanloop; **kopie `aanloop-matarani.geojson`** | 72,1 (kade 70,6 km van de knoop) | stippel-geojson (kopie) | **ja** — MARNET reikt niet |
| b5 | B | zee | zeeknoop 489 → Huelva-zeeknoop 8016 (37.0872,-6.8478) — **aannemelijk: één bron voor de bestemming** | Stille Oceaan → Panamakanaal → Atlantische Oceaan, route door MARNET | MARNET gemeten **11.451,1** (proefrun, 88 edges, 31 punten in Panama-zone; geen gepubliceerde routelengte) | MARNET (`--been zee`) | nee |
| b6 | B | zee | zeeknoop 8016 → Puerto Exterior-anker (37.1535,-6.8768) | haven-aanloop Puerto de Huelva; kade 7,8 km van de knoop (> 5 km) | 7,8 hemelsbreed | rechte stippel (aanloop-tool time-out 2x, zie §7) | **ja** — schematisch, MARNET reikt niet |
| b7 | D | truck | Puerto Exterior → Atlantic Copper-smelter | N-442, H-30, Av. Francisco Montenegro; **kopie zilver-matsa-huelva b2** (aannemelijk: één bron) | hemelsbreed 10,5 km, geen wegkm; OSM-pad 11,9 | kopie `zilver-matsa-huelva-weg-terminal-smelter.geojson` | nee |

Landbenen b1–b4 + b7 zijn kopieën (samen ca. 192 km = 1,6 % van ca. 11.650 km). Het zeebeen is 98 % van de km: de ±15 %-toets op de landbenen is hier van weinig belang. Geen luchtbeen, geen leiding.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-cerroverde-laad` | mijn / concentrator | Cerro Verde, concentrator Uchumayo/Yarabamba | -16.5170, -71.5966 | koper-cerroverde-toyo §3 | bestaand — hergebruikt (bron-gelegd) |
| `cu-lajoya-overslag` | overslag truck→spoor | PeruRail-station La Joya | -16.7245, -71.8598 | koper-cerroverde-toyo §3 | bestaand — hergebruikt (aannemelijk) |
| `cu-matarani-spooreinde` | spooreinde | Matarani, spooreinde | -17.0049, -72.0964 | koper-lasbambas-matarani §3 | bestaand — hergebruikt |
| `cu-matarani-kade` | overslag spoor→zee | Tisur Muelle F, concentraatpier | -17.0044, -72.1124 | koper-cerroverde-toyo §3 | bestaand — hergebruikt (bron-gelegd) |
| `cu-huelva-terminal` | losplek / overslag zee→truck | Puerto de Huelva, Puerto Exterior, Muelle Ingeniero Juan Gonzalo (zuidzijde) — **losplek niet gebrond** | 37.1535, -6.8768 | [3][4]; = `ag-huelva-terminal` uit zilver-matsa-huelva §3 | aannemelijk (z15 gezien, 2026-10-31: witte opslagloods in de zuiduitbreiding van de Muelle Sur naast de containerkade met portaalkranen, een bulkschip op de rede; dit is Impala's MATSA-exportterminal, geen bewezen importkade van Atlantic Copper) |
| `cu-atlanticcopper-smelter` | smelter (stoppunt) | Atlantic Copper, Complejo Metalúrgico, Punta del Sebo | 37.2287, -6.9482 | [3][5]; = `ag-atlanticcopper-smelter` | bron-gelegd (z15 gezien, 2026-10-31: smeltergebouwen met schoorstenen, grondstofstapels, twee steigers aan de Odiel; 0 m van OSM-object) |
| `cu-huelva-zeeknoop` | zee-knoop | MARNET-zeeknoop 8016 | 37.0872, -6.8478 | `hecht_marnet`-meting | knoop, niet de lijn |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen nieuwe via-punten: alle landbenen zijn letterlijke kopieën. b1 behoudt de drie via-punten van cerroverde-toyo §4 (-16.5681,-71.6494 · -16.5958,-71.7226 · -16.6591,-71.7874, alle op OSM way 286975126); b7 die van zilver-matsa-huelva §4 (N-442-via 37.1958,-6.9253). b2 heeft geen via nodig.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Cerro Verde-concentrator | SMCV (Freeport 55,1 %) | erts → Cu-concentraat | 430,5 kt Cu/j in concentraat plus kathode (2024) | koper-cerroverde-toyo [8] |
| Atlantic Copper | Freeport-McMoRan | Cu-concentraat → anodes → kathode | anode 247,6 kt in 2024 (smelter 330 kt, raffinaderij 285 kt) | [1][5] |

## 6 · Stoppunt
Bij de Atlantic Copper-smelter: daar eindigt het concentraat; de afzet van de kathode is niet gepubliceerd per stroom. Fase E vervalt. Zou b7 niet houden, dan is het Puerto de Huelva-anker het stoppunt.

## 7 · Open punten
1. **Cerro Verde niet bij naam bevestigd.** Het 10-K noemt "South America operations" (p. 27, 98, 173); El Abra levert alleen SX/EW-kathode (p. 22), dus Cerro Verde is de enige concentraatbron daar. Afleiding, geen bronnaam: de bestemming staat in de beennaam b5.
2. **Losplek in Huelva niet gebrond.** Atlantic Copper: grondstof wordt ontvangen in Puerto de Huelva, daarna truck naar de smelter; geen kade genoemd [3]. Het anker is de MATSA-exportterminal van Impala en alleen een plausibele plek. De BOE-concessie van Atlantic Copper (tot 2027) omvat een bulkterminal en een "pantalán" op Punta del Sebo [4]; de twee steigers die op z15 bij de smelter aan de Odiel liggen kunnen de eigen losplek zijn. Dan vervalt b6+b7 voor een waterpad de Odiel op (ca. 18 km van knoop 8016). Niet getekend: geen bron legt deze lading op een kade.
3. **Haven-aanloop b6:** `maak_havenaanloop` (anker → knoop 8016) gaf bij de toets én bij een tweede poging (2026-10-31, machine belast door parallelle aanloop-runs) exit 124 na 300 s: b6 is een rechte stippel, zonder kustpad.
4. **Volume:** alleen 15 % van de concentraatinkoop (2024); geen kt Cu, geen tonnage concentraat gepubliceerd. Volgorde "15 % = Cerro Verde" is aanname.
5. **Route Panama** is door MARNET gekozen (geen scheepsbron); alternatief via Kaap Hoorn/Suez niet beproefd.
6. **Sitelaag:** koper-sitelaag kent Atlantic Copper (smelter Huelva, ca. 330 kt anode) niet; melding aan de orchestrator.

## 8 · Bronnen
[1] Freeport-McMoRan, Form 10-K 2024 — p. 27 en 173: Atlantic Copper 2024 concentraat 15 % uit FCX Zuid-Amerika, 13 % Indonesië, 2 % Noord-Amerika; p. 27: anode 247.600 t; p. 98: Zuid-Amerika verkoopt een deel van het concentraat aan Atlantic Copper; p. 20: Cerro Verde-productie ca. 70 mijl per truck en spoor naar Matarani; p. 22: El Abra alleen SX/EW. https://s22.q4cdn.com/529358580/files/doc_financials/10-K/10_k2024.pdf
[2] v2/design/routebrieven/koper-cerroverde-toyo.md (b1–b4, ankers, bronnen [3][4][6][8][11] daarin)
[3] Atlantic Copper, "Materias primas" — concentraat vooral per schip, ook over de weg uit Huelva; "se recibe en el Puerto de Huelva", daarna truck; geen kade genoemd (gelezen 2026-10-31). https://atlantic-copper.es/como-lo-hacemos/materias-primas/
[4] BOE-B-2010-3850, Autoridad Portuaria de Huelva — concessie Atlantic Copper: smelter/raffinaderij, bulkterminal en pantalán op Punta del Sebo, 395.975 m², tot 22-10-2027, minimaal 750.000 t concentraat per jaar via de haven (gelezen 2026-10-31). https://www.boe.es/diario_boe/txt.php?id=BOE-B-2010-3850
[5] Atlantic Copper, "Complejo Metalúrgico" — 60 ha, 330 kt anode, 285 kt kathode. https://atlantic-copper.es/como-lo-hacemos/complejo-metalurgico/
[6] v2/design/routebrieven/zilver-matsa-huelva.md — ankers `ag-huelva-terminal` en `ag-atlanticcopper-smelter` (bronnen [3]–[9], [11], [12] daarin), b2 truck Terminal → smelter
[7] v2/design/routebrieven/koper-lasbambas-matarani.md — Matarani-spooreinde, Muelle F, haven-aanloop Matarani
[8] v1 `data/copper.js` en `design/koper.md` — checklist (Panama als Pacific→Atlantic-chokepoint)
Satellietblik (Esri live, 2026-10-31, `v2/build-cache/satcheck/`): `sat-koper-cerroverde-huelva-cu-huelva-terminal.png` (z15) · `-cu-atlanticcopper-smelter.png` (z15) · `-cu-havenzone.png` (z14). Proefrun b5: MARNET 489 → 8016 = 11.451,1 km (88 edges).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
Recept: `bash v2/tools/bak_stromen.sh koper-cerroverde-huelva` (functie `bak_koper_cerroverde_huelva`) → `v2/data/stroomroute-koper-cerroverde-huelva.json` (51,6 KB). Geen nieuw profiel, geen wegscan, geen aanloop-run: alle landbenen zijn letterlijke kopieën, het zeebeen is één MARNET-run.

| # | modaliteit | km | naad | herkomst |
|---|---|---|---|---|
| b1 | truck | 47,0 | – | kopie koper-cerroverde-toyo (mijnweg, OSM-pad; brief: hemelsbreed 36, geen wegkm) |
| b2 | spoor | 59,2 | 0,13 | kopie cerroverde-toyo (MINEM ca. 60: −1,3 %) |
| b3 | spoor, stippel | 1,7 | 0,00 | havenspoor, geen net |
| b4 | zee, stippel | 72,1 | 0,00 | kopie aanloop-matarani.geojson |
| b5 | zee | 11.451,1 | 0,00 | MARNET 489 → 8016, 88 edges, via Panama (= proefrun) |
| b6 | zee, stippel | 7,8 | 0,00 | rechte stippel knoop 8016 → Puerto Exterior |
| b7 | truck | 12,7 | 0,00 | kopie zilver-matsa-huelva b2 (brief: OSM-pad 11,9; 12,7 is het kopie-getal) |

Totaal 11.651,6 km · 2.561 punten · 5 markers (Cerro Verde, La Joya, Muelle F, Puerto de Huelva, Atlantic Copper), alle ≤ 0,04 km van de lijn. Grootste naad 0,13 km (b1→b2, geërfd van de toyo-stroom). Stippel = 3 benen (b3, b4, b6), alle "hier reikt het net niet" / eigen verbinding.
- **b6 rechte stippel:** MARNET reikt niet over de 7,8 km tussen zeeknoop 8016 en Puerto Exterior; maak_havenaanloop gaf in het ontwerp 2x exit 124, dus geen derde poging (toets_rechte_benen meldt hem, zoals bedoeld).
- **Geen vlucht, geen leiding.** b5 is aannemelijk (één bron, FCX 10-K); de losplek in Huelva is niet gebrond (open punt 2).
- **toets_knikken:** 19 knikken ≥ 60°, 3 omkeringen, 0 terugloop; de spikes bij 37,153,-6,875 en 37,228,-6,952 zitten in de gekopieerde b7 (haventerrein/smelterstraten) en zijn niet aangeraakt.
- **Les:** een keten van louter kopieën plus één MARNET-run is in één bake klaar (geen slot voor de wegscan nodig); de ±15 %-toets is hier van weinig belang (landbenen 1,6 % van de km).
