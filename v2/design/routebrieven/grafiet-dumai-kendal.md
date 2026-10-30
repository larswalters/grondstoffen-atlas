# Routebrief (licht) · grafiet — Dumai → Tanjung Emas → Kendal (Indonesië)

**stroom-id:** `grafiet-dumai-kendal` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** **groene petroleumcokes (green coke)**, geen kunstgrafiet, uit de cokeseenheid (Delayed Coker) van Pertamina Refinery Unit II Dumai (Riau) gaat per **schip** (aanname) via de Rupatstraat, Malakkastraat, Singapore- en Karimata-/Javazee-route naar Tanjung Emas (Semarang; losplek aannemelijk) en per **truck** ~31 km over de Pantura naar PT Indonesia BTR New Energy Material (anodefabriek) in Kendal SEZ.
**Welke as van het verhaal:** *Indonesische grondstof naar de grootste ex-China anodefabriek, binnen één land.* Cokes is het feedstock voor synthetisch anodemateriaal; wat BTR er daarna mee doet (calcineren, grafitiseren) is niet gedocumenteerd. **Volume: 100 kt green coke/j, toezegging (MoU 16-11-2023), peiljaar 2023** [1]; Dumai maakte 244,4 kt in 2024 [3]. Gerealiseerde leveringen niet gepubliceerd. Eenheid kt green coke/j (geen grafiet-equivalent; de grafiet-sitelaag telt kt AAM/grafiet).

## 1 · Ketenkaart
```
Pertamina RU II Dumai (kokerij) ──(site → steiger: eigen terrein, geen been)──► cokes-/productsteiger `gr-dumai-steiger` (aannemelijk)
  ──(b1 haven-aanloop Dumai 4,1 km rechte stippel)──► zeeknoop 5370 (1.6765, 101.5192)
  ──(b2 zee · Rupatstraat → Malakka → Singapore → Karimata/Javazee · 1.552,6 km MARNET, aannemelijk)──► zeeknoop 5470 (-6.8337, 110.4071)
  ──(b3 haven-aanloop Semarang 12,7 km stippel, KOPIE balama-kendal b5)──► Tanjung Emas, Dermaga Samudera 2 `gr-semarang-kade` (aannemelijk)
  ──(b4 truck · Pantura Jl Arteri · 31,3 km, KOPIE balama-kendal b6, aannemelijk)──► BTR Kendal `gr-btr-kendal` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | zee (aanloop) | `gr-dumai-steiger` → zeeknoop 5370 | Dumai-baai (Rupatstraat, oostwaarts) | 4,1 hemelsbreed (steiger < 5 km van de knoop, toch aanloop: anders begint de lijn 4 km vóór het anker) | rechte stippel (maak_havenaanloop.py gaf binnen 300 s geen pad; geen tweede poging) | ja — MARNET reikt niet tot de steiger |
| b2 | B | zee (bulk/breakbulk, aannemelijk) | zeeknoop 5370 → zeeknoop 5470 | Rupatstraat → Malakkastraat → Singaporestraat → Karimata/Javazee (router kiest) | 1.552,6 gemeten MARNET (14 edges); hemelsbreed 1.366,9; geen gepubliceerde zeelengte | MARNET `--been zee` | nee — *aannemelijk: één bron voor de bestemming, geen bron voor het schip* |
| b3 | B | zee (aanloop) | zeeknoop 5470 → `gr-semarang-kade` | havenmond Tanjung Emas; **letterlijke kopie** van `grafiet-balama-kendal-aanloop-semarang.geojson` (been 5 van `grafiet-balama-kendal`) | 12,7 gemeten (12,4 hemelsbreed) | `--stippel-geojson`, kopie | ja — MARNET reikt niet tot de kade (> 5 km) |
| b4 | C | truck | `gr-semarang-kade` → `gr-btr-kendal` | Pantura, Jl Raya Arteri; **letterlijke kopie** van `grafiet-balama-kendal-weg-semarang-kendal.geojson` (been 6) | 31,3 gemeten (31,2 weg); **25 gepubliceerd** (Tanjung Emas → KIP, parkopgave [7]) | `--been-geojson`, kopie | nee — +25% t.o.v. 25: indicatie, geen norm |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-dumai-steiger` | kokerij + overslag land → zee | Pertamina RU II Dumai, noordoostelijke steiger bij de cokes-/tankopslag | 1.6838, 101.4826 | [1][3][5] noemen Dumai als herkomst, geen bron noemt een steiger; OSM way 945327609 "Marine Pertamina" [8] | **aannemelijk** (z15–z17 gezien [10]: raffinaderij 1,7 km breed met tankparken en units; aan de NO-hoek een zwarte open stapelplaats met transportband en trestle naar een T-kop-steiger met tanker; de cokessteiger zelf niet aan te wijzen, ook de tankersteigers bij 1.6877/101.4703 en 1.6866/101.4772 kunnen het zijn) |
| `gr-semarang-kade` | losplek zee / overslag | Tanjung Emas, Dermaga Samudera 2 | -6.9442, 110.4240 | hergebruik letterlijk uit `routebrieven/grafiet-balama-kendal.md` §3 (OSM way 1430916358) | aannemelijk — hergebruik (z15 gezien in die brief: containerschiereiland met kraanrij) |
| `gr-btr-kendal` | fabriek | PT Indonesia BTR New Energy Material, Kendal SEZ | -6.9237, 110.2685 | hergebruik letterlijk uit `grafiet-balama-kendal` §3 en sitelaag `w-btr-kendal` [6][9] | bron-gelegd — hergebruik (blauwdak-fabriekscomplex in het park) |

Naad-ankers zonder site: zeeknoop 5370 (1.6765, 101.5192, water, 4,1 km van de steiger; op z13 gezien: open water van de Dumai-baai) en zeeknoop 5470 (-6.8337, 110.4071).

## 4 · Via-punten
Geen. Het enige landbeen (b4) is een letterlijke kopie; er is geen corridorkeuze op land. Geen profiel en geen extract nodig.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kokerij (Delayed Coker) Dumai | Pertamina Kilang Pertamina Internasional (KPI); verkoop via Pertamina Patra Niaga / Pertachem | zware residu → green coke (S 0,5%, as 0,1%) | 244,4 kt green coke 2024; Q1 2025 49,6 kt; enige KPI-unit op industriële schaal | [3][4] |
| BTR Indonesia, Kendal | BTR New Energy Material | green coke + natuurlijk vlok → anodemateriaal | 80 kt/j fase 1 (aug 2024) + 80 kt fase 2 = 160 kt/j anode; coke-afname 100 kt/j (MoU) | [1][2][6] |

## 6 · Stoppunt
De brief stopt bij de BTR-fabriek in Kendal: de enige afnemer met naam in alle bronnen; waar cokes tot kunstgrafiet wordt (calcineren, grafitiseren, in Kendal of elders) is niet gedocumenteerd, dus fase D/E vervallen.

## 7 · Open punten
- **Productbenaming:** Jokowi spreekt van "artificial graphite" uit Pertamina's Riau-raffinaderij [6]; Kemenko Marves (Seto) zegt kunstgrafiet uit *petroleum coke* van Dumai [5]; contract en Pertachem-akkoord zeggen **green coke** [1][2]. Geen bron noemt een calciner in Dumai of een grafitiseringsstap in Indonesië; de keten tekent daarom green coke, niet kunstgrafiet.
- **Steiger niet bron-gelegd:** de cokesverscheping vanaf Dumai staat in geen bron; de gekozen T-kop-steiger is de dichtstbijzijnde bij de zwarte stapelplaats met transportband (aannemelijk). Een tankersteiger kan het zijn; vervoer als bulklading is niet aangetoond.
- **Zeevervoer en losplek Semarang zijn aanname** (geen bron noemt schip, haven of Tanjung Emas); Pertachem-BTR-akkoord zelf niet gelezen (rm.id 403). Daarom b2–b4 aannemelijk.
- **Volume:** 100 kt/j is een toezegging; gerealiseerde leveringen niet gepubliceerd. Dumai 244,4 kt (2024) is productie, geen export naar BTR.
- **Sungai Pakning** (andere Pertamina-unit in Riau) is niet uitgesloten als herkomst van "Riau"-materiaal; Dumai is door KPI als enige coke-unit genoemd [3].
- **MARNET-route** gaat oostwaarts uit de Dumai-baai (Selat Bengkalis); of schepen de westelijke Rupatstraat nemen is niet gemeten. Geen gepubliceerde zeelengte.
- Truck-kopie +25% t.o.v. 25 km: parkopgave, geen wegmeting (indicatie).

## 8 · Bronnen
[1] Indonesia Business Post, 17-11-2023: Pertamina Patra Niaga + PT Indonesia BTR New Energy Material, MoU 16-11-2023, 100.000 MT green petroleum coke per jaar, geproduceerd door KPI in Dumai. https://indonesiabusinesspost.com/1839/business-and-investment/pertamina-patra-niaga-signs-mou-with-btr-new-energy-material-to-supply-raw-materials-for-anodes
[2] Medcom.id, 18-04-2025: Pertachem tekent green-coke-verkoopakkoord met BTR; DCU; Refinery Unit II Dumai. https://www.medcom.id/ekonomi/sustainability/Rb1D6GlN-bahan-baku-baterai-ini-jadi-andalan-indonesia-menuju-swasembada-energi
[3] Tanahair.net: Dumai raffinaderij 244,4 kt green coke in 2024, 49,6 kt Q1 2025, enige KPI-unit op industriële schaal. https://tanahair.net/dumai-refinery-leads-national-green-coke-production/
[4] Warta Ekonomi: Delayed Coker, specificaties, toepassingen; geen kopers of transport genoemd. https://wartaekonomi.co.id/read573535/dari-limbah-jadi-uang-green-coke-kpi-tembus-industri-strategis
[5] Detik Finance, 07-08-2024: Kemenko Marves (S. H. Seto): anodegrondstof uit kunstgrafiet van petroleum coke van Pertamina Dumai. https://finance.detik.com/energi/d-7477997/pabrik-anoda-yang-diresmikan-jokowi-di-kendal-pakai-limbah-pertamina/amp
[6] Jakarta Globe, 07-08-2024: BTR Kendal 80 kt anodemateriaal/j, fase 2 tot 160; "artificial graphite ... Pertamina's Riau refinery". https://jakartaglobe.id/business/chinas-btr-launches-lithium-battery-anode-plant-in-central-java
[7] Kendal Industrial Park: PT Indonesia BTR New Energy Material, Tanjung Emas 25 km. https://www.kendalindustrialpark.co.id/post/index/612/pt-indonesia-btr-new-energy-material-is-ready-to-become-the-2nd-largest-anode-manufacturer-factory-in-the-world
[8] OpenStreetMap (ODbL) via Nominatim: way 945327609 "Marine Pertamina, Pertamina Refinery Unit II Dumai" (1.6776, 101.4610), node 2962728956 (1.6776, 101.4634). https://www.openstreetmap.org/way/945327609
[9] Atlas: `routebrieven/grafiet-balama-kendal.md` §3/§9 en `v2/design/grafiet-sitelaag.json` (`w-btr-kendal`).
[10] Esri World Imagery via `sat_check.py` (live, 2026-10-30): `v2/build-cache/satcheck/sat-grafiet-dumai-kendal-{dumai-marine,dumai-ruim,dumai-kilang,dumai-steiger,dumai-ne-steiger,dumai-steiger-z17,zeeknoop5370,rupat-regio}.png`.
[11] Interne meting 2026-10-30: `hecht_marnet route` zeeknoop 5370 → 5470, 1.552,6 km, 14 edges, landtoets 0 km (1:10M).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Bestand:** `v2/data/stroomroute-grafiet-dumai-kendal.json` (19,8 KB, versie 2, lonlat) · **functie:** `bak_grafiet_dumai_kendal()` in `v2/tools/bak_stromen.sh` · **geen profiel, geen extract, geen via-punt.** Totaal 1.600,7 km, 919 punten, 3 markers.

| # | modaliteit | km gemeten | km brief | naad | lijn |
|---|---|---|---|---|---|
| b1 | zee (haven-aanloop Dumai) | 4,1 | 4,1 hemelsbreed | 0,00 | stippel, rechte lijn (2 punten) |
| b2 | zee (MARNET 5370 → 5470) | 1.552,6 | 1.552,6 gemeten (geen publicatie) | 0,00 | doorgetrokken, 165 punten, 14 edges |
| b3 | zee (haven-aanloop Semarang) | 12,7 | 12,7 | 0,00 | stippel, KOPIE `grafiet-balama-kendal` b5 |
| b4 | truck (Tanjung Emas → BTR Kendal) | 31,3 | 25 parkopgave / 31,3 kopie | 0,00 | doorgetrokken, 746 punten, KOPIE `grafiet-balama-kendal` b6 |

**Markers (3):** `gr-dumai-steiger` 1.6838,101.4826 (aannemelijk) · Tanjung Emas Dermaga Samudera 2 -6.9442,110.4240 (aannemelijk, hergebruikt) · BTR Kendal -6.9237,110.2685 (bron-gelegd, hergebruikt); alle drie 0,0 km van hun lijn.

**Recept:** b1 `--stippel` rechte lijn · b2 `--been zee` kade → kade (de zeeknopen 5370 en 5470 als uiteinden, snap 0,000 km) · b3 `--stippel-geojson` en b4 `--been-geojson` letterlijk uit `grafiet-balama-kendal-aanloop-semarang.geojson` en `-weg-semarang-kendal.geojson`. Bake 17 s via `bash v2/tools/bak_stromen.sh grafiet-dumai-kendal`.

**Toelichting per stippel/aanloop:**
- **b1 stippel:** MARNET heeft geen knoop bij de steiger; `maak_havenaanloop.py` gaf binnen 300 s geen pad (brief-stap, geen tweede poging), dus een rechte lijn van 4,1 km. De steiger zelf is aannemelijk (z15-z17: T-kop met tanker bij de zwarte stapelplaats), niet bron-gelegd.
- **b3 stippel:** kade 12,4 km van zeeknoop 5470, dus haven-aanloop (kopie van balama-kendal, over water, 0 km land).
- **b2 aannemelijk:** één bron voor de bestemming (MoU), geen bron voor het schip; staat in de beennaam, de lijn is doorgetrokken.

**Toets (§5):** naden 0,00 km overal (max 0); geen km-afwijking van betekenis (b2 en b3 gelijk aan de brief; b4 = 31,3 tegen de 25 km van de parkopgave, +25%: indicatie, geen norm, identiek aan balama-kendal); `toets_knikken`: 12 knikken >= 60 graden, 1 omkering, 0 terugloop; 11 daarvan op de truckkopie (spikes in de Kendal-wegtoegang, hetzelfde als balama-kendal) en 1 krappe bocht (83 graden, R 6,7 km) in de Straat van Singapore (MARNET); `toets_rechte_benen --min-km 5`: geen melding voor deze stroom; json.load OK, modaliteiten {zee, truck}, elk been >= 2 punten.

**Lessen:** (1) een stroom die twee benen letterlijk kopieert is in één bake van 17 s klaar: de zeeknopen 5370/5470 komen uit de brief-meting en zijn het uiteinde van het zeebeen, dus geen snap. (2) De cokessteiger is de zwakste schakel: een aannemelijke ankerlegging op een satellietblik zonder bron voor de verscheping. (3) Het id noemt Kendal als eindpunt en de lijn eindigt daar.
