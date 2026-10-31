# Routebrief (licht) · lithium — Sabi Star → Beira → Morowali (Zimbabwe → Indonesië)

**stroom-id:** `lithium-sabistar-morowali` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van de Sabi Star-mijn (Max Minds Investments / Chengxin Lithium, Buhera) gaat per **truck** over een naamloze mijnweg naar de R5/A3 bij Odzi, door Mutare naar de Forbes/Machipanda-grens en over de EN6 naar de Beira-kade, per **bulkcarrier** (Mozambiquekanaal, Indische Oceaan, Straat Sunda) naar de IMIP-kade bij Morowali, waar Chengxin zelf een lithiumzoutfabriek (ChengTok, 60 kt/j) heeft — bestemming **aannemelijk: één bron** (afgeleid, geen bron noemt deze mijn bij Morowali).
**Welke as van het verhaal:** de Chinese converter die zijn Afrikaanse erts op Sulawesi verwerkt, naast Australisch erts. BPS: Zimbabwe leverde 9 % van de 293 kt spodumeen die in 8M-26 bij Morowali/Bahodopi binnenkwam [3] = ca. 26 kt concentraat in 8 maanden ≈ 40 kt/j ≈ **5,4 kt LCE/j** (eigen omrekening: 40 kt SC × 0,136 bij 5,5 % Li2O; peiljaar 2026, geannualiseerd). De naamplaat van Sabi Star (ca. 290 kt SC/j [2][5]) is dus niet het volume van deze keten: Zimbabwe schorste export feb–apr 2026 en gaf daarna quota's [6][7].

## 1 · Ketenkaart
```
Sabi Star-mijn + plant `li-sabistar-plant` (Buhera, Manicaland)
  ──(b1 truck · naamloze mijnweg → Odzi R5/A3 → Mutare → Forbes · 112,1 km gemeten, geen gepubliceerde wegkm)──►
Forbes/Machipanda-grens `li-forbes-grens` (hergebruikt)
  ──(b2 truck · EN6 via Manica–Chimoio–Inchope–Dondo · 286,9 km — letterlijke kopie lithium-arcadia-beira b2)──►
Beira-kade `li-beira-kade` (hergebruikt) ──(b3 terreinstippel 1,8 km · b4 haven-aanloop 7,8 km — kopie)──►
zeeknoop Beira ──(b5 zee · MARNET · 10.822 km)──► zeeknoop 5491 ──(b6 haven-aanloop 95,6 km, stippel — kopie, omgekeerd)──►
IMIP-kade `li-imip-kade` (hergebruikt) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-sabistar-plant` → `li-forbes-grens` | mijnweg (ca. 67 km naamloos) → R5/A3 Odzi → Mutare (A3/N6) → Forbes | 112,1 gemeten; **geen gepubliceerde wegkm**, hemelsbreed 81 km; OSRM-toets 113 km [11] | maak_stroombeen_weg, extract zimbabwe, corridorKlassen tertiary+unclassified | nee |
| b2 | A | truck | `li-forbes-grens` → `li-beira-kade` | EN6 — **letterlijke kopie** lithium-arcadia-beira b2 | 286,9 (Mozambique Expert 289) [10] | `lithium-arcadia-beira-weg-forbes-beira.geojson` | nee |
| b3 | A | truck | havenweg-inrit → `li-beira-kade` | eigen terrein Beira — kopie | 1,8 | stippel | ja — eigen terrein |
| b4 | B | zee | `li-beira-kade` → zeeknoop Beira | haven-aanloop — kopie (kade 7,8 km van de zeeknoop > 5 km) | 7,8 | rechte stippel | ja — MARNET reikt niet tot de kade |
| b5 | B | zee | zeeknoop Beira → zeeknoop 5491 | Mozambiquekanaal → Indische Oceaan → Straat Sunda → Java/Banda-zee (MARNET beslist) | 10.822,1 gemeten; hemelsbreed 9.622 vanaf de zeeknoop, geen zeekm | MARNET | nee |
| b6 | B | zee | zeeknoop 5491 → `li-imip-kade` | haven-aanloop IMIP — **omgekeerde letterlijke kopie** nikkel-morowali-quzhou-aanloop-imip (92,9 km hemelsbreed > 5 km) | 95,6 | `lithium-sabistar-morowali-aanloop-imip.geojson` | ja — 1:10M-kust kent de haven niet |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-sabistar-plant` | mijn + concentratorplant / laadplek | Sabi Star-mijn (Max Minds Investments / Chengxin Lithium), Buhera | -19.1983, 31.9658 | [1][2][8] | **bron-gelegd** (z15 gezien: kruis op de blauwdaks-procesgebouwen, tailingsdam ca. 1 km NW, twee lichte open pits W/ZW, mijnweg verlaat het terrein naar NO) — `sat-lithium-sabistar-morowali-mijn.png`, `-mijn-wide.png` |
| `li-forbes-grens` | grensovergang | Forbes (ZW) / Machipanda (MZ), N6 | -19.0052, 32.7123 | [10] | hergebruik letterlijk, bron-gelegd (lithium-bikita-zhangjiagang / lithium-arcadia-beira) |
| `li-beira-kade` | overslag truck → zee | Beira, general-cargo-terminal Cornelder; zeeknoop -19.8701, 34.7882 | -19.8150, 34.8340 | [10] | hergebruik letterlijk, bron-gelegd (lithium-arcadia-beira) |
| `li-imip-kade` | losplek (stoppunt) | IMIP-exporthaven, oostpunt van het complex, Bahodopi (Morowali); zeeknoop 5491 -2.0357, 122.0017 | -2.8480, 122.1980 | [4][10] | hergebruik letterlijk (nikkel-morowali-quzhou `ni-imip-jetty`; zelfde punt als lithium-pilgangoora-morowali); z15 opnieuw gezien: landtong met pier, schepen langszij, loodsen en terreinstapels — bestemming **aannemelijk: één bron** |

## 4 · Via-punten (alleen b1; b2–b6 zijn kopieën of MARNET)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Odzi, R5/A3 (ten oosten van het dorp, buiten Mutare) | -18.9199, 32.4158 | pint de route via de R5/A3 Harare–Mutare (snap 0,00 km) i.p.v. een zuidelijker sluipweg naar Mutare; dit is de enige corridorkeuze. Mutare zelf krijgt géén via-punt: de A3 loopt er per definitie doorheen (0,18 km van het centrum, geen ringweg) en een via-punt in het centrum kost omweg. |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sabi Star-concentrator | Max Minds Investments (Chengxin Lithium, meerderheid sinds 2021) | erts 1,98 % Li2O → spodumeenconcentraat | 990 kt erts/j → ca. 290 kt SC/j naamplaat; productie sinds mei 2023 | [1][2][5] |
| ChengTok Lithium Indonesia (IMIP) | Chengxin 65 % / Tsingshan-dochter 35 % | spodumeenconcentraat → Li2CO3/LiOH | 60 kt zout/j; proefproductie juni 2024; "volle productie" volgens [5] | [4][5] — **fabrieksperceel niet gelegd**, niet getekend |

## 6 · Stoppunt
De brief stopt op de IMIP-kade: [4] noemt de ChengTok-fabriek binnen IMIP en dat Chengxin concentraat uit eigen mijnen in China en Zimbabwe betrekt, maar geen bron koppelt Sabi Star-concentraat aan een lading naar Morowali, en het fabrieksperceel is niet gevonden — dus geen fase C/D; fase D vervalt (geen fabriek met één bron + coördinaat), fase E vervalt.

## 7 · Open punten
- **Bestemming Morowali is afgeleid** (twee losse feiten: BPS Zimbabwe 9 % bij Morowali [3]; Chengxin eigenaar van mijn én ChengTok [4]). Climate Change News [1] zegt alleen "naar China". Terugval bij weerlegging: Yangtze-monding (conventie).
- **Ligplaats in Beira ongebrond** (zoals in lithium-arcadia-beira); **ligplaats in IMIP** niet gedocumenteerd (meerdere private steigers; anker = de exportkade die op z15 zichtbaar is).
- **Geen gepubliceerde wegkm voor b1**: de ±15 %-toets is een indicatie (gemeten 112,1 tegen OSRM 113 = -0,8 %); Chengxin geeft 360 km road mijn–Beira [2]; gemeten b1+b2 = 399 km (+11 %, naamloze weg + door Mutare).
- **Naamloze mijnweg** (ca. 67 km, tertiary/unclassified): geen `track` nodig gebleken; plant → eerste weg 1,0 km, doorgetrokken (< 2 km).
- **Chengxin geeft Sabi Star "180 km NW van Harare"** [2]; de OSM-/satellietlocatie ligt 180 km hemelsbreed ZO van Harare (240 km weg klopt) — de richting in de bron is fout, de plek op de satelliet is een plant met pits en tailings.
- **Volume**: 5,4 kt LCE/j is een eigen omrekening; Zimbabwe-aandeel (9 %) is van het hele Morowali/Bahodopi-complex, niet alleen Chengxin. Quota en concentraatverbod vanaf jan. 2027 [6] maken het jaar-op-jaar onzeker; sulfaatplan Buhera (75 kt/j, aangekondigd 24-08-2026) [5] niet getekend.
- **Haalbaarheidstoets**: Mukwasi-corridor uit het ontwerp is vervallen (Mukwasi ligt in Gutu); route via Odzi zoals de toets aanwees.

## 8 · Bronnen
[1] Climate Change News, 26-01-2024, trucks vanaf Sabi Star via Mukwasi en Mutare naar Beira, schip naar China; 900 kt erts/j, 300 kt concentraat/j, productie sinds mei. https://www.climatechangenews.com/2024/01/26/cef-project-zimbabwe-lithium-mining-china-ev-battery-supply-chain/
[2] Chengxin Lithium, Sabi Star-productpagina: 40 claims, 1,98 % Li2O, 990 kt erts/j, ca. 290 kt SC/j, Beira 300 km hemelsbreed / 360 km weg, productie mei 2023. https://en.cxlithium.com/product/45.html
[3] Dewan Ekonomi Nasional (BPS-douanedata), p. 45: 8M-26 spodumeen bij Morowali en Bahodopi 293 kt, Australië 91 %, "Zimbabwe supplied 9% of 2026 ore". https://www.dewanekonomi.go.id/public/storage/event-materials/01M5BNCV5NQGV1M3Z2Y9SG4Q1T.pdf
[4] Petromindo, 01-04-2025, ChengTok-fabriek in IMIP, 60 kt/j, proefproductie juni 2024, concentraat uit mijnen in China en Zimbabwe. https://www.petromindo.com/news/article/chengxin-strives-for-full-capacity-at-indonesian-lithium-chemical-plant
[5] Energytrend, 25-08-2026, Sabi Star 990 kt erts / 290 kt SC per jaar, 60 kt-lithiumzoutproject Indonesië op volle productie, sulfaatplan Buhera. https://www.energytrend.com/news/20260825-52016.html
[6] Mining Weekly (Reuters), 08-04-2026, Zimbabwe: exportquota's, 10 % exportbelasting, sulfaatfabrieken vóór 01-01-2027. https://www.miningweekly.com/article/zimbabwe-to-introduce-lithium-export-quotas-sets-conditions-for-resumption-of-shipments-2026-04-08
[7] Miningmx, 13-04-2026, Zimbabwe geeft Chinese mijnbouwers (o.a. Chengxin) lithiumquota. https://miningmx.com/news/battery-minerals/2026-04-13-zimbabwe-grants-chinese-miners-lithium-export-quotas
[8] OSM via Photon (haalbaarheidstoets): "Sabi Star Mine" -19.1983, 31.9658, industrial; Nominatim: Odzi (dorp) -18.9603, 32.3894.
[9] Esri World Imagery via `v2/tools/sat_check.py`, z14/z15: `v2/build-cache/satcheck/sat-lithium-sabistar-morowali-mijn.png`, `-mijn-wide.png`, `-imip.png`.
[10] Eigen briefs: `lithium-arcadia-beira.md` (Forbes, Beira, EN6, terreinstippel), `lithium-bikita-zhangjiagang.md`, `nikkel-morowali-quzhou.md` (IMIP-kade, aanloop 92,9 km); zie ook `lithium-pilgangoora-morowali` (zelfde IMIP-anker).
[11] OSRM/OSM-route Sabi Star → Odzi → Forbes 113 km (haalbaarheidstoets 2026-10-31), geen publicatie.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)

`v2/data/stroomroute-lithium-sabistar-morowali.json` · 118,9 KB · versie 2, lonlat · 6 benen, 11.327,4 km, 5.874 punten, 4 markers (alle 0,0 km van de lijn) · naden 0-0,006 km · 0 terugloop.
Recept: `bash v2/tools/bak_stromen.sh lithium-sabistar-morowali` (functie `bak_lithium_sabistar_morowali`; profiel `lithium-sabistar-morowali-plant-forbes`, wegscan_puur.py, extract zimbabwe).

| # | modaliteit | km | geometrie |
|---|---|---|---|
| b1 | truck | 113,2 getekend (112,1 gescand + 1,0 plant naar weg) | wegscan, via-punt Odzi (snap 0,00 km), eerste 9,95 km unclassified; indicatie tegen OSRM 113 km: +0,2 %, geen gepubliceerde wegkm |
| b2 | truck | 286,9 | letterlijke kopie lithium-arcadia-beira b2 (EN6) |
| b3 | truck, stippel | 1,8 | kopie terreinstippel Beira |
| b4 | zee, stippel | 7,8 | kopie haven-aanloop Beira (rechte stippel, kade 7,8 km van de zeeknoop) |
| b5 | zee | 10.822,1 | MARNET zeeknoop Beira naar zeeknoop 5491 (via Straat Sunda); geen zeekm gepubliceerd, geen toets |
| b6 | zee, stippel | 95,6 | omgekeerde letterlijke kopie nikkel-morowali-quzhou-aanloop-imip (zeeknoop 5491 naar IMIP-kade) |

**Toelichting stippels:** b3 en b4 zijn kopieen uit lithium-arcadia-beira (eigen terrein en MARNET-gat Beira); b6 is de haven-aanloop IMIP omdat de kade 92,9 km van de zeeknoop ligt en de 1:10M-kust de haven niet kent. Geen lucht-, spoor- of leidingbeen; fase C/D/E vervallen (stoppunt IMIP-kade).
**Toets:** toets_knikken: 10 knikken in b1, allemaal spikes van enkele tot tientallen meters (snaps bij plant, Odzi, Forbes-grens), 0 terugloop; b2 1 omkering (kopie, reeds beoordeeld in lithium-arcadia-beira); toets_rechte_benen markeert alleen de kopie-stippel Beira.
**Lessen:** de beennaam van b1 noemde eerst 112,1 km (scan) terwijl de bak 113,2 getekend rapporteert (plant-naar-weg-stuk 1,0 km erbij): noem in de beennaam het getekende getal. Mutare krijgt geen via-punt (A3 loopt erdoor, geen ringweg); Odzi alleen pint de R5/A3.
