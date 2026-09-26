# Routebrief (licht) · nikkel — Norilsk → Moermansk → Monchegorsk (Rusland)

**stroom-id:** `nikkel-norilsk-monchegorsk` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** converter-matte van de Talnakh-mijnen en de Nadezhda-smelter (Norilsk, Nornickel Polar Division) gaat per **spoor** over het geïsoleerde Norilsk-industrienet naar Dudinka aan de Jenisej, per **binnenvaart** (bulklaag) de rivier af naar de Jenisej-golf, dan per **zee** met de eigen Arctische ijsbrekervloot (jaarrond, door Karskiye Vorota) naar Moermansk, en vandaar per **spoor** naar Severonickel in Monchegorsk voor elektrolytische raffinage tot nikkel — met een **optionele, niet-gebakken vertakking** per spoor via de Finse grens (Vainikkala) naar de raffinaderij Harjavalta.
**Welke as van het verhaal:** de enige Arctische class-1-keten van de atlas, en de enige route zonder één gedeelde zeehaven onderweg (eigen ijsbrekervloot, eigen spoor). Nornickel produceerde 205 kt Ni in 2024 (guidance 2025: 204–211 kt) [3]; Kola-raffinage (Severonickel, Monchegorsk) is opgevoerd van 120 naar 145 kt/j [4][9]; Harjavalta (Finland) verwerkt een deel van dezelfde matte, 65 kt nu → 100 kt gepland 2026 [10]. v1 had deze stroom fout als "rail Norilsk→Kola" — dat bestaat niet (geen spoorbrug van Norilsk naar het vasteland); gecorrigeerd naar spoor–binnenvaart–zee–spoor.

## 1 · Ketenkaart
```
Nadezhda-fabriek `ni-nadezhda-fabriek` ──(b1 spoor · Norilsk-industrienet, geïsoleerd · 77,7 km)──► Dudinka-kade `ni-dudinka-kade`
   ──(b2 binnenvaart · Jenisej, bulklaag · 429,8 km)──► Jenisej-golf-zeeknoop (MARNET 2338, 71.9829,82.4669)
   ──(b2b zee, stippel · naad rivier↔zeeknoop · ~20,2 km)──► idem
   ──(b3 zee · Karazee → Karskiye Vorota → Barentszzee, Arctische vloot · 2.124,5 km)──► Moermansk-terminal `ni-moermansk-terminal`
   ──(b4 spoor · Oktoberspoorweg Kola–Olenegorsk · 142,1 km)──► Severonickel Monchegorsk `ni-monchegorsk-severonickel`
   ──(b4b spoor, stippel · terreinspoor smelter · ~3 km)──► idem ⏹ stoppunt (elektrolytisch nikkel)
   ╎ vertakking (optioneel, niet gebakken): b5 spoor Monchegorsk → Vainikkala-grens (60.86,28.62) → Harjavalta `ni-harjavalta-raffinaderij` (Finland)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Nadezhda-fabriek → Dudinka-kade | Norilsk-industriespoor Norilsk → Kajerkan → Dudinka (geïsoleerd net) | 77,7 (gemeten) [16] | `BAKE_SUFFIX=-raw toets_spoorroute.mjs --hoofd-km=50 --max-snap=10` (rusland-siberie) | nee |
| b2 | B | binnenvaart | Dudinka-kade → Jenisej-golf (bulk-knoop) | Jenisej stroomafwaarts (bulklaag; geen bevaarbaarheidsbewijs, ligging van het water) | 429,8 (gemeten) [16] | `maak_rivierbeen.py` over de bulklaag (bulk-ru) | nee |
| b2b | B | zee | bulk-knoop → zeeknoop 2338 (Jenisej-golf) | naad rivier↔MARNET (bulk-knoop 1,8 km van de kade, 20,2 km van zeeknoop 2338) | ~20,2 (gemeten, naad > 5 km-norm) [16] | rechte stippel of rivierbeen eindigen op dichtstbijzijnde bulk-knoop bij 2338 | ja — net/naad reikt niet exact |
| b3 | B | zee | zeeknoop 2338 → Moermansk-terminal | Karazee → Karskiye Vorota (niet om Nova Zembla) → Barentszzee; jaarrond met 5 eigen Arc7-ijsbrekende schepen | 2.124,5 (gemeten, MARNET) [16] | `--been "zee\|…\|71.9829,82.4669\|68.9737,33.0658"` | nee |
| b4 | C | spoor | Moermansk-terminal → Severonickel Monchegorsk | Oktoberspoorweg Moermansk → Kola → Olenegorsk → Monchegorsk | 142,1 (gemeten, 1 spike) [16] | `toets_spoorroute.mjs` (rusland-noordwest) | nee |
| b4b | C | spoor | Severonickel-terrein | terreinspoor smelter (ontbreekt in OSM) | ~3 (gemeten snap) [16] | stippel "spoor\|terreinaansluiting Severonickel (geen net op deze korrel)" | ja — terreinspoor niet gekarteerd |
| b5 | C′ | spoor | Monchegorsk → Harjavalta (optioneel, **niet gebakken tenzij besloten**) | Kola → Kandalaksja → Petrozavodsk → **Vainikkala**-grens → Harjavalta | ~1.700 (ongemeten; vrije Dijkstra 1.732 km liep fout via Oulu) [16] | twee runs: Monchegorsk→Vainikkala + Vainikkala→Harjavalta | optioneel — anders weglaten |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-nadezhda-fabriek` | mijn/smelter (kop spoor) | Nadezhda Metallurgical Plant, Norilsk (Nornickel Polar Division) | 69.3275, 87.9521 | [2][17], hergebruikt uit koper-sitelaag.md | bron-gelegd (z15 gezien: groot fabriekscomplex met rookpluim, tankinstallaties en spoorbundel direct ten westen) |
| `ni-dudinka-kade` | overslag spoor→binnenvaart | Dudinka-havenkade, Jenisej | 69.4030, 86.1680 | [6][8][17] | bron-gelegd (z17 gezien: rij rood-oranje kadekranen evenwijdig aan de rivieroever, spoor direct erlangs) |
| `ni-moermansk-terminal` | overslag zee→spoor | Nornickel Murmansk Transport Division, Портовый проезд 31/1 | 68.9737, 33.0658 | [11][17] | **aannemelijk** (adres via bedrijvenregister; z17 gezien: kade met spoorbundel en loodsen aan de zuidkant van de Kolabaai, maar geen naambord/logo op het beeld te onderscheiden van het naastgelegen scheepsreparatiebedrijf) |
| `ni-monchegorsk-severonickel` | losplek/raffinaderij | Severonickel-fabriek (Kola MMC), Monchegorsk | 67.9195, 32.8320 | [4][9][17] | bron-gelegd (z16 gezien: smelterhallen, tanks en schoorstenen van het Severonickel-complex, spoorbundel aan de oostzijde) |
| `ni-harjavalta-raffinaderij` | raffinaderij (optionele vertakking) | Norilsk Nickel Harjavalta Oy, Teollisuuskatu 1 | 61.3188, 22.1225 | [10][15] | aannemelijk (bedrijvenregister/adres; geen satellietblik — optioneel, alleen bij bakken van b5) |

## 4 · Via-punten (alleen b5 — de enige corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b5 | 1 | Vainikkala-grensovergang | 60.86, 28.62 | Global Witness noemt Vainikkala expliciet als grensovergang voor de matte-containers [1]; een vrije Dijkstra kiest zonder dit punt de verkeerde grensroute via Oulu (Vartius/Tornio) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nadezhda Metallurgical Plant, Norilsk | Nornickel Polar Division | erts/concentraat Talnakh-mijnen → converter-matte | onderdeel van groepscijfer 205 kt Ni (2024) | [3][17] |
| Severonickel, Monchegorsk (Kola MMC) | Nornickel | converter-matte (Dudinka via Moermansk) → elektrolytisch nikkel, Tank Houses #1/#2 | 120 → 145 kt/j (chloor-uitloging-upgrade) | [4][9] |
| Harjavalta (optioneel, niet getekend) | Nornickel Harjavalta Oy | matte → nikkelsulfaat | 65 kt/j → 100 kt/j gepland 2026 | [10] |

## 6 · Stoppunt
De brief stopt bij Severonickel: elektrolytisch nikkel/nikkelkathode is het eindproduct, verkocht op de wereldmarkt (LME-leverbaar voor class-1) — geen bron noemt een specifieke volgende fabriek per afnemer, dus fase D/E vervalt. Sanctie-/China-afzet (Potanin: deels richting China, NSR) is context in de bronnen, geen gedocumenteerde keten.

## 7 · Open punten
- Naad tussen het Jenisej-rivierbeen (bulklaag) en MARNET-zeeknoop 2338: 20,2 km, boven de 5 km-norm — blijft een korte stippel of het rivierbeen wordt ingekort tot de dichtstbijzijnde bulk-knoop.
- `ni-moermansk-terminal` is **aannemelijk**, niet bron-gelegd: het adres (Портовый проезд 31/1) komt uit een bedrijvenregister [11], maar op het satellietbeeld is geen Nornickel-specifiek kenmerk (logo, naambord) te onderscheiden van het naastgelegen scheepsreparatiebedrijf — een niet-Esri-bron (bv. Yandex-panorama) kan dit sluitend maken.
- Severonickel-terreinspoor (~3 km) ontbreekt in OSM → stippel "geen net op deze korrel".
- Nornickel publiceert geen matte-tonnage per deelroute; het jaarvolume is het groepscijfer (205 kt Ni, 2024) [3].
- b5 (Harjavalta-vertakking) is optioneel en **niet gebakken** in deze ronde — alleen tekenen als de bak-agent tijd heeft voor de twee spoorruns via Vainikkala; anders weglaten (aanpassing toets).
- Sanctie-/China-afzet is genoemd in de bronnen maar niet tot een tekenbare keten te herleiden (geen gedocumenteerde Chinese fabriek).

## 8 · Bronnen
[1] Global Witness, "Sanctions gap lets Russian-mined nickel flow to Western markets" — matte per schip Dudinka→Moermansk, dan spoor naar Monchegorsk; containers over de Finse grens bij Vainikkala naar Harjavalta. https://globalwitness.org/en/campaigns/transition-minerals/sanctions-gap-lets-russian-mined-nickel-flow-to-western-markets/
[2] Nornickel, Kola Site — bedrijfsprofiel Kola-divisie. https://nornickel.com/business/assets/kola-division-russia/
[3] Nornickel, persbericht 27-01-2025 — geconsolideerde productieresultaten 2024: 205 kt Ni, guidance 2025 204–211 kt. https://nornickel.com/news-and-media/press-releases-and-news/nornickel-announces-consolidated-production-results-for-2024/
[4] Nornickel Factsheet (corporate PDF) — Kola-raffinage 120 → 145 kt/j, Tank House #1/#2 chloor-uitloging. https://nornickel.com/files/en/corporate_documents/company/profile/Nornickel_Factsheet.pdf
[5] Nornickel, AR2023 — Logistics & sales of goods: eigen Moermansk-terminal ontvangt converter-matte uit Dudinka, verzendt per spoor naar Kola Division. https://ar2023.nornickel.com/business-overview/logistics-sales-of-goods
[6] Nornickel, AR2024 — Transport and logistics assets (PDF): Dudinka Transport Division, Dudinka-haven als hoofdlading-haven van Taimyr. https://ar2024.nornickel.com/pdf/ar/en/business-overview_transport-logistics-assets.pdf
[7] International Mining, 21-01-2022 — nieuwe ijsbreker breidt Nornickels transportcapaciteit Dudinka–Moermansk uit; thuishaven Moermansk. https://im-mining.com/2022/01/21/new-icebreaker-expand-nornickels-metal-concentrate-transportation-capacity-arctic-route-dudinka-murmansk/
[8] Nornickel ESG, "The only port in the world that goes under water every May" — Dudinka-havenbeschrijving, ijsgang Jenisej. https://esg.nornickel.com/practice/tpost/b92i5m0i41-the-only-port-in-the-world-that-goes-und
[9] Nornickel Annual Report — Tank-house #2 Severonickel: 145 kt/j elektrolytisch nikkel na chloor-uitloging-upgrade (via zoekindex, geciteerd in [4]).
[10] IndustryAbout, Harjavalta Nickel Refinery (Nornickel Harjavalta Oy) — adres Teollisuuskatu 1, 29200 Harjavalta; verwerkt matte uit Monchegorsk + Boliden-materiaal, nikkelsulfaat sinds 2002. https://www.industryabout.com/country-territories-3/2745-finland/nickel-mining/42868-nornickel-harjavalta-nickel-refinery
[11] 2GIS — "Норильский никель, горно-металлургическая компания", Портовый проезд, 31/1, Мурманск. https://2gis.ru/murmansk/firm/70000001024889816
[12] Nornickel, persbericht 19-12-2011 — "MMC Norilsk Nickel develops Murmansk cargo terminal". https://nornickel.com/news-and-media/press-releases-and-news/mmc-norilsk-nickel-develops-murmansk-cargo-terminal-/
[13] OpenStreetMap (ODbL) via Nominatim — geocodering Дудинка (69.4061,86.1751) en Портовый проезд, Мурманск (adresbasis voor [11]). https://www.openstreetmap.org
[14] Volza/Panjiva — bedrijfsadres Norilsk Nickel Harjavalta Oy, Teollisuuskatu, Harjavalta (bevestiging van [10]). https://www.volza.com/company-profile/norilsk-nickel-harjavalta-oy-teollisuuskatu-77689114/
[15] Nornickel — coördinaat Harjavalta-raffinaderij, 61.318792, 22.122454 (afgeleid via [10]/[14], niet zelf satelliet-gelegd — optionele vertakking).
[16] Interne haalbaarheidstoets `nikkel-norilsk-monchegorsk` (ontwerp-JSON, 2026-09-26): proefroutes via `toets_spoorroute.mjs`/`maak_rivierbeen.py`/MARNET, km/snaps zoals in §2 vermeld.
[17] Esri World Imagery via `v2/tools/sat_check.py` (z13–z17) — `v2/build-cache/satcheck/sat-nikkel-norilsk-monchegorsk-*.png` (dudinka-overzicht, dudinka-haven, dudinka-kade, dudinka-kade2, murmansk-overzicht, murmansk-zeleny-mys, murmansk-portoviy31, nadezhda, severonickel, severonickel2, severonickel3).

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `nikkel-norilsk-monchegorsk`** → `v2/data/stroomroute-nikkel-norilsk-monchegorsk.json` — 5 benen, **2.798,6 km**, 3.144 punten, 6 markers. spoor 78,0 + 145,7 = 223,7 km · binnenvaart 430,2 km · zee 20,2 (stippel) + 2.124,5 = 2.144,7 km.
Recept: `bak_stromen.sh` (functie `bak_nikkel_norilsk_monchegorsk`).

**b1 (spoor, nieuwe scan):** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=69.3275,87.9521 --naar=69.4030,86.1680 --naam=nikkel-norilsk-monchegorsk-nadezhda-dudinka --hoofd-km=50 --max-snap=10`, op het 1-op-1-net ("3260717 spoor-edges" bevestigd). Snap 0,73 km (Nadezhda-fabriek) / 1,92 km (Dudinka-kade), beide op hetzelfde geïsoleerde component (253 km — het Norilsk-industrienet). Resultaat **77,7 km over 68 edges tegen 70,4 km hemelsbreed (verhouding 1,10)** — EXACT de gepubliceerde 77,7 km uit de brief. 0 knikken ≥60°.

**b2 (binnenvaart, bulklaag):** `python v2/tools/maak_rivierbeen.py --marnet v2/build-cache/marnet-preais --van 69.4030,86.1680 --naar 71.82880,82.77830`, over de bulklaag (60.200 van 76.133 edges, 407.870 km). Snap 1,26 km (Dudinka-kade) / 0,00 km (bulk-knoop 58275, gevonden als dichtstbijzijnde bulk-knoop bij MARNET-zeeknoop 2338 via `H.marnet_zee`). Resultaat **429,8 km over 49 edges** — EXACT de gepubliceerde 429,8 km. Beennaam draagt de clausule "bulklaag: ligging van het water, geen bevaarbaarheidsbewijs" zoals de bak-aanwijzing vroeg. Naad b1→b2: **3,08 km** (kop river-been op 69,4052/86,1363 tegen staart spoorbeen op 69,3915/86,2046) — < 5 km, procesgat op het overslagpunt spoor→binnenvaart in Dudinka.

**b2b (zee, stippel, naad):** rechte `--stippel` van de bulk-knoop (71,82880/82,77830) naar MARNET-zeeknoop 2338 (71,9829/82,4669), **20,23 km** — gemeten met dezelfde zoekfunctie als de brief (`hecht_marnet.marnet_zee` → dichtstbijzijnde bulk-knoop op 20,23 km van zeeknoop 2338), dus geen kortere naad gevonden en het rivierbeen is al zo dicht mogelijk ingekort. Boven de 5 km-norm → stippel gehouden, niet dichtgetrokken (brief §7, open punt 1).

**b3 (zee, geroutet):** `--been "zee|…|71.9829,82.4669|68.9737,33.0658"`, MARNET zelf laten routeren (geen via-punt afgedwongen, `northwest`-passage dicht op de default). Snap 0,000 km (Jenisej-golf-zeeknoop) / 1,159 km (Moermansk). Resultaat **2.124,5 km over 227 punten** — EXACT de gepubliceerde 2.124,5 km; de route loopt via Karskiye Vorota zoals verwacht (geen Noordwest-Passage-sluipweg, want die passage blijft dicht).

**b4 (spoor, nieuwe scan):** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=68.9737,33.0658 --naar=67.9195,32.8320 --naam=nikkel-norilsk-monchegorsk-moermansk-severonickel`, op het hoofdnet (1.144.150 km-component, geen `--hoofd-km` nodig). Snap 0,04 km (Moermansk-terminal) / 0,23 km (Severonickel). Resultaat **145,1 km over 127 edges tegen 117,6 km hemelsbreed (verhouding 1,23)** tegen de gepubliceerde 142,1 km (**+2,1%**, ruim binnen ±15%). Eén spike-punt automatisch weggesnoeid (OSM-zigzag); 2 scherpe bochten (178,0°/165,7°, boogstralen 27–57 m) vlak bij Moermansk-terminal — komt overeen met de "1 spike" die de brief noemt, en past bij rangeerbewegingen op het havenemplacement. Naad b3→b4: **1,20 km** (staart zeebeen bij Moermansk tegen kop spoorbeen) — < 5 km.

**Geen b4b-stippel (afwijking van de bak-aanwijzing):** de brief verwachtte een los terreinspoor-stukje bij Severonickel (~3 km, "geen net op deze korrel", brief §2/§7). Gemeten snap bij het Severonickel-anker is echter **0,23 km** — het 1-op-1-spoornet reikt hier al tot vlak bij het anker, dus er is geen meetbaar gat om te stippelen. Geen lijn getekend voor b4b; de marker Severonickel (67,9195/32,8320) ligt 228 m van de gerouteerde lijn, binnen de ~0,5 km-tolerantie.

**Geen b5 (Harjavalta-vertakking, Finland):** conform de brief optioneel ("alleen tekenen als er tijd voor is, anders weglaten", brief §2/§7) — in deze bake weggelaten. Blijft open punt.

**Toets:** km-sommen per gemeten been binnen ±15% (b1 0,0%, b2 0,0%, b4 +2,1%; b3 0,0% tegen MARNET-eigen route). Naden **3,08 km** (b1→b2) en **1,20 km** (b3→b4), beide < 5 km-norm; b2→b2b en b2b→b3 naadloos (0,00 km, gedeeld eindpunt). `toets_knikken.py`: 7 knikken ≥60° totaal, waarvan **2 echte terugloop** — beide op b4 vlak bij Moermansk-terminal (178,1°/165,8°, boogstralen 20–57 m), en `toets_spoorroute.mjs` had ze zelf al als "OMKERING — alleen echt als hier kopgemaakt wordt" gemeld; geïnterpreteerd als rangeerbeweging op het havenemplacement, niet dichtgetrokken (bevinding, geen fix). `toets_rechte_benen.py --min-km 5`: **b2b (20,2 km, stippel, omwegfactor 0,999) wordt terecht als stippel gevonden** — geen ongeteste rechte lijn. json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {spoor, binnenvaart, zee}, elk been ≥2 punten, bestandsgrootte 57,7 KB (< 300 KB). Alle 6 markers liggen op hun been (0–1.264 m; Nadezhda 731 m en Dudinka-kade 1.264 m zijn anker≠routeerpunt — site- resp. overslagcentroïdes tegenover een spoor-/rivier-routeerpunt).

**Gereedschapslessen:**
- De gemeten b4b-verwachting uit de briefsamenvatting (~3 km terreinspoor-stippel) bleek bij het bakken niet nodig: het 1-op-1-spoornet snapt al op 0,23 km van het Severonickel-anker. De brief ging uit van een aanname ("ontbreekt in OSM"), het bakken uit een meting — de meting wint, en de stippel is bewust niet toegevoegd.
- `H.marnet_zee(H.lees_marnet(...))` gecombineerd met de bulk-knopenlijst (uit `meta.vaarwegen[*].bulk`) vindt in één klap de kortste naad tussen een rivierbeen en een MARNET-zeeknoop — dezelfde truc als de zeeknoop-zoeker uit de handleiding §2, alleen dan op bulk-knopen in plaats van zeeknopen.
- Twee `toets_spoorroute.mjs`-runs op hetzelfde geïsoleerde Norilsk-net (b1) en het hoofdnet (b4) laten zien dat `--hoofd-km` alleen nodig is als het component kleiner is dan de default-drempel (1.000 km) — hier 253 km resp. 1.144.150 km, dus alleen b1 vroeg de verlaagde drempel.


