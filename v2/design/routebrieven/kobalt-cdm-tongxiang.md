# Routebrief (licht) · kobalt — Kobalt · CDM (Lubumbashi) → Durban → Tongxiang (China)

**stroom-id:** `kobalt-cdm-tongxiang` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) · **status:** gebakken
**Keten in één zin:** ruw kobalthydroxide van Huayou's eigen Congolese plant CDM (Lubumbashi) gaat per **truck** over de Copperbelt-zuidroute (RN1 → Kasumbalesa → T3/T2 → Chirundu → A1/A4 → Beitbridge → N1/N3) naar de containerkade **Durban DCT Pier 2**, per **zeeschip** via Malakka naar **Ningbo Beilun**, en per **truck** (G60/G92) naar de Huayou-hoofdraffinaderij in **Tongxiang** — aannemelijk: één bron (Huayou-eigen DRC-hydroxide; CDM geschorst sinds 2025-11-06, herstart onbevestigd).
**Welke as van het verhaal:** *de eigen mijn naast de eigen raffinaderij* — Huayou's rapport zegt dat Zhejiang Huayou (Tongxiang) zijn kobalt "mainly" uit ruw DRC-hydroxide haalt, over land naar Durban en per schip naar Zhapu/Ningbo [1]. Geen CDM-cijfer gepubliceerd; context: DRC-quotum 2026 = 96.600 t Co (87.000 basis + 9.600 strategisch) [7]; Reuters noemde 77,4 kt (discrepantie, niet opgelost).

## 1 · Ketenkaart
```
CDM Lubumbashi `co-cdm-lubumbashi` ──(b1 truck · RN1/T3/T2/A1/A4/N1/N3 · ~2.750 km, aannemelijk)──► Durban DCT Pier 2 `cu-durban-kade`
  ──(b1a zee-aanloop 17,8 km, kopie)──► zeeknoop Durban ──(b2 zee · Malakka · ~12.800 km)──► zeeknoop Ningbo
  ──(b2a zee-aanloop 11,6 km, kopie)──► Ningbo Beilun `co-ningbo-kade`
  ──(b3 truck · G60/G92 · 192,2 km, kopie, aannemelijk)──► Huayou Tongxiang `co-tongxiang-raffinaderij` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-cdm-lubumbashi` → `cu-durban-kade` | RN1 → Kasumbalesa → T3/T2 → Chirundu → A1/A4 → Beitbridge → N1/N3 (aannemelijk: één bron, CDM geschorst) | **hemelsbreed 2.075 km, geen wegkm**; eigen afleiding weg ~2.780 (tfm-durban 2.982 min ~200); de bestaande KCC-bake geeft vanaf Lubumbashi-RN1 2.727 km + ~20 km CDM→RN1 | `maak_stroombeen_weg.py`, nieuw profiel `kobalt-cdm-durban` | nee |
| b1a | A | zee (haven-aanloop) | `cu-durban-kade` → Durban-zeeknoop | — | 17,8 (bestaand) | **letterlijke kopie** `aanloop-durban.geojson` | ja — MARNET reikt niet tot de kade |
| b2 | B | zee | Durban-zeeknoop (-29.8168, 31.1737) → Ningbo-zeeknoop 5850 (29.9758, 121.9736) | Indische Oceaan → Malakka → Zuid-Chinese Zee → Oost-Chinese Zee | 12.792,0 (gebakken in tfm-quzhou b2) | MARNET, zelfde `--been` als `kobalt-tfm-quzhou` | nee |
| b2a | B | zee (haven-aanloop) | Ningbo-zeeknoop → `co-ningbo-kade` | Beilun-containerzone | 11,6 (bestaand) | **letterlijke kopie** `kobalt-tfm-quzhou-aanloop-ningbo.geojson` | ja — kade 11,6 km van de zeeknoop |
| b3 | C | truck | `co-ningbo-kade` → `co-tongxiang-raffinaderij` | G60/G92 Ningbo–Tongxiang (aannemelijk: Huayou-eigendom + rapport [1]) | 192,2 (gebakken) | **letterlijke kopie** `kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson` (functie `bak_kobalt_murrinmurrin_kwinana`) | nee |

Last mile CDM: het anker ligt 2,1 km van de gebakken RN1-lijn (gemeten op de KCC-bake); geen eigen been, het wegprofiel (eindKlassen) legt de plant-stub; blijkt dat een snap > 5 km, dan stippel `last mile (geen net op deze korrel)`.

## 3 · Ankers
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-cdm-lubumbashi` | mijn/plant (laadplek) | Congo DongFang International Mining (CDM, Huayou), Likasi Road, Lubumbashi | -11.5165, 27.4291 | [1][8], OSM landuse=industrial | **bron-gelegd** (z15 gezien: blauwe hallen, tankparken en vijvers naast een dagbouwput; het kruis ligt op de plant) [12] |
| `cu-durban-kade` | overslag truck → zee | Durban Container Terminal Pier 2 (Bayhead) | -29.8790, 31.0160 | `koper-kolwezi-durban.md` §3 | hergebruikt, bron-gelegd |
| `co-ningbo-kade` | overslag zee → truck | Beilun Container Terminal Phase 2 | 29.9353, 121.8695 | `kobalt-tfm-quzhou.md` §3 | hergebruikt, bron-gelegd |
| `co-tongxiang-raffinaderij` | raffinaderij ⏹ | Zhejiang Huayou Cobalt, Wuzhen East Road 18, Tongxiang | 30.6167, 120.5629 | `kobalt-huayou-gunsan.md` §3, adres [1] | hergebruikt, bron-gelegd; open conflict campus versus raffinaderij (§7) |

## 4 · Via-punten (b1, lat, lon, letterlijk uit `koper-kolwezi-durban.md` §4 / profiel `kobalt-kcc-durban`)
| # | punt | lat, lon | waarom hier |
|---|---|---|---|
| 1 | Lubumbashi RN1 | -11.6642, 27.4827 | pint RN1 zuidwaarts, geen Likasi-omweg |
| 2 | Kasumbalesa (grens DRC/ZM) | -12.2658, 27.7959 | enige grensovergang |
| 3 | Ndola T3 | -12.9688, 28.6367 | Copperbelt-keuze T3 |
| 4 | Kabwe T2 | -14.4426, 28.4400 | T3 → T2 |
| 5 | Lusaka T2 | -15.4163, 28.2817 | Lusaka-bypass T2 |
| 6 | Chirundu (grens ZM/ZW) | -16.0338, 28.8471 | grensbrug |
| 7 | Harare A1→A4 | -17.8362, 31.0467 | A1/A4-splitsing |
| 8 | Masvingo A4 | -20.0745, 30.8332 | A4 zuidwaarts |
| 9 | Beitbridge (grens ZW/ZA) | -22.2244, 29.9865 | grensovergang |
| 10 | Polokwane N1-bypass | -23.9218, 29.4803 | N1-bypass |
| 11 | Buccleuch N1/N3 | -26.0493, 28.1004 | N1/N3-splitsing naar Durban |

Elf punten (boven de 3–8): bindend hergebruik van de bestaande bake-corridor, geen nieuwe punten. Refs: RN1 N1 T3 T2 A1 A4 N3. Extracts: congo-drc, zambia, zimbabwe, zuid-afrika. Venster 75 km, corridorKlassen tertiary.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| CDM, Lubumbashi | Zhejiang Huayou Cobalt (dochter, sinds 2006 verwerker, daarna mijn) | erts → ruw kobalthydroxide (+ koper, grootste omzet) | geen Co-cijfer gepubliceerd; omzet 2024 $1,1 mld | [3][6] |
| Zhejiang Huayou, Tongxiang | Zhejiang Huayou Cobalt | DRC-hydroxide → kobaltchemicaliën | geen cijfer gebrond | [1] |

## 6 · Stoppunt
De lijn stopt bij Huayou Tongxiang: het rapport noemt deze vestiging als afnemer van DRC-hydroxide via Durban en Zhapu/Ningbo [1]; geen bron noemt een volgende fabriek, dus fase D/E vervallen.

## 7 · Open punten
- **CDM niet genoemd als leverancier:** het rapport noemt CDM alleen als contactadres (Likasi Road, Lubumbashi) [1]; herkomst CDM = eigendomsinferentie, naam "aannemelijk: één bron".
- **CDM geschorst:** drie maanden vanaf 2025-11-06 na dambreuk [2][3][5]; 2026-02-13 stelde het ministerie herstartvoorwaarden voor Joli-Site [4]; geen herstartbericht gevonden. Lijn = gedocumenteerd patroon, geen actuele lading.
- **Zhapu niet gelegd:** het rapport noemt "Zhapu/Ningbo"; Ningbo gekozen, Zhapu-kade ontbreekt.
- **Wegkm b1:** geen gepubliceerde wegkm; 2.780 is eigen afleiding, ±15% geldt als indicatie.
- **Tongxiang-anker:** open conflict in `kobalt-sitelaag.json` (campus versus smelterij op bijna dezelfde plek); niet hier opgelost.
- **Quotum:** 96,6 kt [7] tegen 77,4 kt (Reuters) onopgelost; CDM-aandeel onbekend.
- **Rapport [1]:** Zhejiang Huayou (Tongxiang) staat in [1] als ontvanger van DRC-hydroxide; Quzhou als ontvanger van een deel. Het ontwerp-stoppunt Tongxiang wordt dus beter gedekt dan voor tfm-quzhou.

## 8 · Bronnen
[1] Huayou Cobalt, 2024 Mineral Supply Chain Due Diligence Report (pdf, doc-pagina's 10–11, 14, 19: Zhejiang Huayou Tongxiang, DRC-hydroxide naar Durban en Zhapu/Ningbo; CDM-adres Likasi Road) https://www.huayou.com/Public/Uploads/uploadfile/files/20250422/2024-Mineral-Supply-Chain-Due-Diligence-Report.pdf
[2] BHRRC, DRC Huayou subsidiary suspended after dam failure, 2025-11 https://www.business-humanrights.org/en/latest-news/drc-huayou-cobalt-subsidiary-suspended-operation-after-dam-failure-spilled-toxic-water-into-lubumbashi-incl-company-non-response/
[3] AFP/Yahoo, DR Congo suspends Chinese cobalt miner after chemical spill (CDM = Huayou-dochter, 2006, omzet 2024) https://www.yahoo.com/news/articles/dr-congo-suspends-chinese-cobalt-122913889.html
[4] Bankable, DRC sets strict conditions for CDM's return, 2026-02-13 https://bankable.africa/en/news/1302-2407-drc-sets-strict-conditions-for-cdms-return-after-environmental-incident
[5] Reuters via Engineering News, Congo suspends activities at Chinese mine after spill, 2025-11-07 https://www.engineeringnews.co.za/article/congo-suspends-activities-at-chinese-mine-after-spill-2025-11-07
[6] Wikipedia, Zhejiang Huayou Cobalt (hoofdkantoor Tongxiang Economic Development Zone) https://en.wikipedia.org/wiki/Zhejiang_Huayou_Cobalt
[7] Benchmark, DRC to lift cobalt export ban and impose quotas through 2027 (96.600 t in 2026) https://source.benchmarkminerals.com/article/drc-to-lift-cobalt-export-ban-and-impose-quotas-through-2027
[8] `v2/design/kobalt-sitelaag.json`, `w-cdm-lubumbashi` (OSM-benoemd, -11.5165 27.4291)
[9] `v2/design/routebrieven/kobalt-tfm-quzhou.md` §3/§9 (Durban-aanloop, MARNET-been, Ningbo-aanloop)
[10] `v2/design/routebrieven/kobalt-wedabay-tongxiang.md` en `kobalt-huayou-gunsan.md` (anker Tongxiang, b3-kopie)
[11] `v2/tools/maak_stroombeen_weg.py` profiel `kobalt-kcc-durban` en `kobalt-kcc-kokkola.md` §4
[12] Esri World Imagery via `sat_check.py` z15: `v2/build-cache/satcheck/sat-kobalt-cdm-tongxiang-cdm-lubumbashi.png`, 2026-10-28

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
`bash v2/tools/bak_stromen.sh kobalt-cdm-tongxiang` → `v2/data/stroomroute-kobalt-cdm-tongxiang.json` (588 KB, 29.076 punten, 4 markers, 15.764,1 km). Functie `bak_kobalt_cdm_tongxiang`, profiel `kobalt-cdm-tongxiang-cdm-durban` in `maak_stroombeen_weg.py`.

| # | modaliteit | km gemeten | km brief | naad | stippel |
|---|---|---|---|---|---|
| b1 | truck CDM → Durban DCT Pier 2 | 2.750,5 | ~2.780 (eigen afleiding) | – | nee |
| b1a | zee haven-aanloop Durban (kopie) | 17,8 | 17,8 | 0,00 | ja |
| b2 | zee Durban → Ningbo (MARNET) | 12.792,0 | 12.792,0 | 0,04 | nee |
| b2a | zee haven-aanloop Ningbo Beilun (kopie) | 11,6 | 11,6 | 0,00 | ja |
| b3 | truck Ningbo-kade → Tongxiang (kopie) | 192,2 | 192,2 | 0,00 | nee |

**Markers (4, alle 0,0 km van de lijn):** CDM Lubumbashi (-11.5165, 27.4291), Durban DCT Pier 2 (-29.8790, 31.0160), Ningbo Beilun (29.9353, 121.8695), Tongxiang (30.6167, 120.5629).

**Recept:** b1 `wegscan_puur.py --profiel kobalt-cdm-tongxiang-cdm-durban` (extracts congo-drc, zambia, zimbabwe, zuid-afrika; refs RN1 N1 T3 T2 A1 A4 N3; venster 75 km; corridorKlassen tertiary), elf via-punten letterlijk uit `kobalt-kcc-durban` plus het CDM-anker; alle via-snaps 0,00-0,09 km, geen punt verschoven. b1a, b2a en b3 zijn letterlijke kopieën van bestaande geojson (`aanloop-durban`, `kobalt-tfm-quzhou-aanloop-ningbo`, `kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang`); b2 is dezelfde MARNET-`--been` tussen de zeeknopen als `kobalt-tfm-quzhou`.

**Toelichting.**
- b1: 2.750,5 km is -1,1% tegen de eigen afleiding 2.780; omdat er geen gepubliceerde wegkm bestaat (hemelsbreed 2.075 km) is dit een indicatie, geen norm. Eerste stuk plant → RN1 is 23,8 km (verwacht ~20 km), eerste-mile 2,97 km over unclassified, laatste mile 7,41 km (service/tertiary/unclassified) in Durban.
- Stippels b1a en b2a: MARNET reikt niet tot de kade (Durban 17,8 km, Ningbo 11,6 km); stippel betekent alleen dat, de keten blijft "aannemelijk: één bron" in de beennaam.
- Geen vlucht, spoor of leiding. Geen last-mile-been: het CDM-anker ligt op de gebakken lijn (plant → weg 0,05 km).
- toets_knikken: 67 knikken, 0 terugloop; de ene omkering zit in de gedeelde Ningbo → Tongxiang-kopie (b3, niet van deze bake). toets_rechte_benen toont geen been van deze stroom.

**Lessen / bevindingen.** Bestandsgrootte 588 KB is boven de ~300 KB-richtlijn door de 26.871 punten van b1 (volle OSM-resolutie, zoals de KCC-bake); de bundel verdicht dit. Zhapu-kade blijft ongelegd, het Tongxiang-anker (campus versus smelterij) is niet hier opgelost, en CDM is geschorst sinds 2025-11-06 (§7).
