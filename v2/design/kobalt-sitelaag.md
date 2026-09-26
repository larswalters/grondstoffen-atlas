# Kobalt-sitelaag wereldwijd — lichte ronde (LAR-56x)

*Gemaakt 2026-09-26 · werkwijze: licht (M29, `routebrief-licht.md` §1/§4) · status: concept, nog niet in een `gloednodes-kobalt.json` verwerkt (voeg_sites_toe.py mist nog een `--grondstof`-parameter en main.js een tweede laadpad — zie het ontwerpbestand `sitelaag-co.json` §3).*

## Doel

Eén coördinaat op **site-niveau** (mijnterrein/plant/raffinaderij/terminal) plus een **capaciteit in kt Co-inhoud per jaar mét bron** voor de belangrijkste kobaltsites wereldwijd. Grondslag: het v1-register `data/cobalt.js` (23 knopen, 40 stromen, centroïdes ~1 km) aangevuld met evident ontbrekende grote sites — de zes Indonesische HPAL-fabrieken, de Chinese raffinagesites, en de niet-gebakken assen uit het ontwerp (`sitelaag-co.json`). Er waren nog geen kobalt-routebrieven geschreven op het moment van deze ronde (`v2/design/routebrieven/kobalt-*.md` bestaat niet), dus er waren geen ankers om letterlijk te hergebruiken buiten de al bestaande, in de vaste-regels-lijst genoemde punten (TFM-plant, Kasumbalesa, Durban DCT Pier 2, Kamoa, KCC Kolwezi).

**Eenheid: kt Co-inhoud per jaar** — bindend uit het ontwerp. Kobalt reist bijna nooit als zuiver metaal vanaf de mijn: Congolese mijnen leveren hydroxide (30–40% Co) of MHP (4–5% Co), Indonesische HPAL-fabrieken leveren MHP. Zonder deze eenheid zijn Congo en Indonesië niet optelbaar — precies de reden dat de opdracht hem bindend maakt.

## Werkwijze

- **Coördinaten** (WGS-84, lat, lon met decimale punt, 4 decimalen): Wikipedia-geohack (MediaWiki-API `prop=coordinates`), benoemde OSM-objecten via Nominatim/Photon, bedrijfsdocumenten. Firecrawl (web-tool) raakte tijdens deze ronde zijn creditlimiet kwijt na een handvol calls — het overgrote deel van dit werk liep via de generieke `WebSearch`/`WebFetch`-tools plus rechtstreekse Nominatim/Photon-calls.
- **Chinese sites via het MEE-emissievergunningregister**: **niet gelukt deze ronde.** Het register is — zoals de opdracht al waarschuwde — recent verhuisd en vraagt kennelijk een interactieve sessie/cookie-flow die met de beschikbare tools niet is af te dwingen. Voor Huayou Quzhou, GEM Jingmen en Jinchuan is daarom uitgeweken naar Wikipedia/OSM/bedrijfsdocumenten. Voor Huayou Quzhou en GEM Jingmen leverde dat alleen een **straatadres** op (resp. "Nianxin Road 18, Hi-tech Industrial Park (Phase II), Quzhou" en "Jingmen, Hubei") dat met Nominatim/Photon niet naar een bruikbaar punt te geocoderen was — beide blijven daarom **buiten scope** met het adres in de tekst, in plaats van een verzonnen coördinaat. Twee Chinese sites uit het v1-register (GEM Ganzhou, Jinchuan Jinchang) zijn als "aannemelijk" overgenomen op hun bestaande ~1 km-centroïde; voor Jinchuan is expliciet vastgelegd dat het bewijs van deze ronde naar Lanzhou wijst als de eigenlijke kobaltraffinaderij, niet Jinchang.
- **Congolese en overige mijnen/plants** via Wikipedia-geohack (de meeste DRC-mijnen hebben een eigen, goed onderhouden Wikipedia-pagina met coördinaat) en benoemde OSM-objecten (Bou Azzer, Ambatovy-plant, CDM Lubumbashi, Umicore Olen, Sherritt Fort Saskatchewan, Eagle Mine kwamen alle vijf naar voren als **exact benoemd OSM-object** — landuse=industrial of landuse=quarry met de bedrijfsnaam erop — en zijn op dat punt bron-gelegd verklaard).
- **Satellietblik** (`python v2/tools/sat_check.py`, Esri z13–z15, beelden in `v2/build-cache/satcheck/` met prefix `sitelaag-kobalt-`) voor de top-6 mijnen (TFM, Kisanfu, KCC, Mutanda, Metalkol RTR, Deziwa) en een deel van de top-6 verwerkers (Huayou Quzhou-gok — bleek geen bruikbare coördinaat, Jinchuan, Nikkelverk, Kokkola, Niihama, Vale Long Harbour). Ligt het kruis op het terrein → **bron-gelegd**; anders verschoven naar wat te zien is (genoteerd in `coord_bron`) → eveneens **bron-gelegd** als het zichtbare complex ondubbelzinnig bij de site hoort, anders **aannemelijk**; niet gezien of geen bruikbaar punt → **aannemelijk** of **buiten scope**.
- **Capaciteit**: kt Co-inhoud per jaar — mijnproductie 2024/2025 (laatste volledige jaar gevonden) of nameplate voor raffinaderijen/HPAL-fabrieken. Bronvermeldingen `[Bn]` verwijzen naar de bronnenlijst. Voor Congolese mijnen is het **Cobalt Institute Market Report 2024** de scherpste bron: die splitst Glencore's gecombineerde KCC+Mutanda-cijfer alsnog uit (27 kt resp. 8 kt), wat Glencore's eigen jaarverslag niet doet.
- **Bewust NIET gedraaid**: `v2/tools/voeg_sites_toe.py` (gebeurt centraal, zoals de opdracht voorschrijft).

## Sites (35)

| id | naam | land | rol | lat, lon | capaciteit kt Co-inhoud/j | bron | coord-bron | status | notitie |
|---|---|---|---|---|---|---|---|---|---|
| `w-tfm` | Tenke Fungurume (TFM) | DR Congo | mijn+plant | -10.5684, 26.1956 | 55 (schatting) | CMOC 2025: TFM+KFM samen 117,5 kt Co; TFM-aandeel niet uitgesplitst [B1][B2] | Wikipedia-geohack; satelliet z15: kruis op de SX-EW/hydroxide-plant | **bron-gelegd** | CMOC (China) 80%; grootste kobaltcomplex ter wereld. |
| `w-kisanfu` | Kisanfu (KFM) | DR Congo | mijn+plant | -10.7090, 25.9560 | 55 (schatting) | CMOC 2025: TFM+KFM samen 117,5 kt Co [B1][B2] | mindat-punt verschoven ~2,3 km ZO naar het zichtbare fabriekscomplex | **bron-gelegd** | CMOC 71,25%/CATL 23,75%/staat 5%. Ligt ZW van TFM (ontwerpcorrectie). |
| `w-kcc-pit` | Kamoto/KOV (KCC) — putten | DR Congo | mijn | -10.7148, 25.3855 | 27 | Cobalt Institute Market Report 2024 [B3] | Wikipedia-geohack; satelliet z15: kruis op het pitcomplex | **aannemelijk** | Glencore 75%/Gécamines 25%. |
| `w-kcc-luilu` | Luilu-plant (KCC) | DR Congo | plant | -10.7205, 25.3705 | — (open) | geen apart cijfer gevonden | satelliet-schatting op zichtbaar complex, geen benoemd object | **aannemelijk** | Verwerkt KCC-erts; capaciteit zit in het putcijfer. |
| `w-mutanda` | Mutanda | DR Congo | mijn+plant | -10.7858, 25.8082 | 8 | Cobalt Institute Market Report 2024 [B3] | Wikipedia-geohack; satelliet z15: kruis in de put | **bron-gelegd** | Glencore 100%. Was ooit 's werelds grootste kobaltmijn. |
| `w-metalkol-rtr` | Metalkol RTR | DR Congo | tailingsverwerking | -10.7116, 25.3966 | 5,7 (werkelijk; nameplate 23) | ERG nameplate + Cobalt Institute/Fastmarkets werkelijke output 2025 [B4][B5] | Wikipedia; satelliet z15: tailings-/uitloogvlakte zichtbaar, plantgebouw niet ondubbelzinnig | **aannemelijk** | ⚠️ Werkelijke output ver onder nameplate — 23 kt zou RTR onterecht als top-3-site laten gloeien. |
| `w-deziwa` | Deziwa | DR Congo | mijn+plant | -10.7970, 25.8010 | 11,6 (schatting, 4% wereldproductie) | Afgeleid, geen primaire bron [B6] | Wikipedia-geohack verschoven ~1,8 km OZO naar zichtbaar complex | **aannemelijk** | CNMC 51%/Gécamines 49%. |
| `w-sicomines` | Sicomines | DR Congo | mijn+plant | -10.7333, 25.3708 | — (open) | geen Co-cijfer gevonden | bedrijfsdocument, niet satelliet-geverifieerd | **aannemelijk** | Sinohydro/CREC 68%/Gécamines 32%. |
| `w-kinsevere` | Kinsevere | DR Congo | mijn+plant (gestopt) | -11.3635, 27.5640 | — (open, plant stil sinds dec. 2024) | MMG/Cobalt Institute [B7][B8] | Wikipedia-geohack, niet satelliet-geverifieerd | **aannemelijk** | MMG (China). Status "gestopt". |
| `w-ruashi` | Ruashi | DR Congo | mijn+plant | -11.6167, 27.5500 | 1 (historisch, 2008) | Verouderd cijfer [B9] | Wikipedia-geohack, niet satelliet-geverifieerd | **aannemelijk** | Jinchuan 75%/Gécamines 25%. |
| `w-chemaf-mutoshi` | Mutoshi (Chemaf) | DR Congo | mijn | -10.6778, 25.5353 | — (open) | geen recent cijfer | Wikipedia-geohack, niet satelliet-geverifieerd | **aannemelijk** | Chemaf, financieel wankel. |
| `w-boss-mining` | Boss Mining (Kakanda/Luita) | DR Congo | mijn | -10.87, 26.68 | — (open) | geen recent cijfer | v1-register-centroïde, niet herbevestigd | **aannemelijk** | ERG. |
| `w-cdm-lubumbashi` | Congo DongFang Mining (CDM) | DR Congo | plant (geschorst) | -11.5165, 27.4291 | — (open) | geen capaciteitscijfer | OSM-named object "Congo DongFang International Mining (CDM)" | **bron-gelegd** | Huayou-dochter. ⚠️ Geschorst sinds 6-11-2025 na dambreuk/gifspill in Lubumbashi. |
| `w-huayue-morowali` | Huayue Nickel Cobalt HPAL | Indonesië | HPAL | -2.8300, 122.1600 | 7,8 | Wood Mackenzie/brancherapporten [B12][B13] | IMIP-parkcentroïde, geen apart gebouw gevonden | **aannemelijk** | MBMA/Huayou/Tsingshan. Grootste operationele HPAL wereldwijd. |
| `w-qmb-morowali` | PT QMB New Energy Materials | Indonesië | HPAL | -2.8300, 122.1600 | 8 (herleid) | GEM Indonesia 9M-2025-cijfer geannualiseerd [B14] | IMIP-parkcentroïde | **aannemelijk** | GEM 55%/Tsingshan 10%/Brunp-CATL 10%/Ecopro 9%/Hanwa 8%/Yibin Libao 8%. |
| `w-huafei-wedabay` | Huafei Nickel Cobalt HPAL | Indonesië | HPAL | 0.4783, 127.9836 | 15 | Nameplate 120 kt Ni + 15 kt Co [B15] | IWIP-parkcentroïde | **aannemelijk** | Huayou/Tsingshan/EVE Energy. Zit op IWIP (Weda Bay), niet IMIP (ontwerpcorrectie). |
| `w-harita-obi` | Harita HPL/ONC (Obi) | Indonesië | HPAL | -1.42, 127.55 | — (open) | 120 kt Ni gecombineerd, geen los Co-cijfer | v1-register-centroïde, geen OSM-object gevonden | **aannemelijk** | Harita Group + Ningbo Lygend. |
| `w-murrin-murrin` | Murrin Murrin | Australië | mijn+HPAL | -28.7675, 121.8939 | 2,1 | Glencore productiecijfer 2023 [B16] | Wikipedia-geohack, niet satelliet-geverifieerd | **aannemelijk** | Glencore 100%. |
| `w-moa-puntagorda` | Moa/Punta Gorda | Cuba | mijn+plant | 20.6308, -74.8569 | 3,4 | Sherritt/GNC-productiecijfer 2022 [B17] | OSM-plaatsnaam "Punta Gorda" | **aannemelijk** | Sherritt 50%/GNC (Cuba) 50%. |
| `w-ambatovy-mijn` | Ambatovy-mijn | Madagaskar | mijn | -18.845, 48.307 | — (zie plant) | n.v.t. | Wikipedia-geohack, niet satelliet-geverifieerd | **aannemelijk** | Sumitomo-consortium. |
| `w-ambatovy-toamasina` | Ambatovy-plant (Toamasina) | Madagaskar | raffinaderij | -18.2002, 49.3604 | 2,5 (2024; nameplate 4) | mining.com/CNBC Africa 2026, Skillings 2026 [B18][B19] | OSM-named object "Ambatovy Plant Site" | **bron-gelegd** | Zelfde consortium als de mijn; 220 km-slurryleiding ertussen. |
| `w-bouazzer` | Bou Azzer | Marokko | mijn | 30.5184, -6.9134 | — (open) | geen recent officieel cijfer | OSM-named object "Mine Bou Azzer" | **bron-gelegd** | Managem/CTT. Enige mijn ter wereld met kobalt als hoofdproduct. |
| `w-umicore-kokkola` | Umicore Kokkola | Finland | raffinaderij | 63.8595, 23.0528 | 15 | Umicore/brancherapporten (indicatief) [B20] | OSM landuse=industrial "Suurteollisuusalue"; satelliet z14: industriepark gezien, Umicore-gebouw niet apart onderscheiden | **aannemelijk** | Umicore. Grootste kobaltraffinaderij buiten China. |
| `w-nikkelverk` | Glencore Nikkelverk | Noorwegen | raffinaderij | 58.1392, 7.9723 | 5 | Nikkelverk "At a glance" [B21] | Bedrijfsopgave; satelliet z16: kruis op het complex | **bron-gelegd** | Glencore. |
| `w-umicore-olen` | Umicore Olen | België | raffinaderij (afbouwend) | 51.1822, 4.8928 | 1,5 | USGS Belgium 2019 (schatting) [B22] | OSM-named object "Umicore Olen" | **bron-gelegd** | ⚠️ Kobaltraffinage verhuist naar Kokkola. |
| `w-niihama` | Niihama-raffinaderij | Japan | raffinaderij | 33.9496, 133.2316 | — (open) | geen apart cijfer | Bedrijfsadres | **bron-gelegd** | Sumitomo Metal Mining. Enige Japanse producent van elektrolytisch kobalt. |
| `w-longharbour` | Vale Long Harbour | Canada | raffinaderij | 47.4242, -53.8167 | 2,5 | Vale nameplate [B24] | Wikipedia-geohack | **bron-gelegd** | Vale Base Metals. |
| `w-fortsaskatchewan` | Sherritt Fort Saskatchewan | Canada | raffinaderij (gestopt) | 53.7237, -113.1875 | — (open; hist. ~3,8) | CBC 2026, Sherritt-jaarverslagen [B25][B26] | OSM-named object "Sherritt" | **bron-gelegd** | ⚠️ Gestopt in 2026 wegens uitgeputte Cubaanse feed. |
| `w-talvivaara-sotkamo` | Talvivaara/Terrafame Sotkamo | Finland | mijn+plant | 63.9672, 28.0169 | 7,4 kt kobaltsulfaat/j (product, niet herrekend naar Co-inhoud) | Terrafame nameplate [B27] | Wikipedia-geohack | **bron-gelegd** | Terrafame (Finse staat). Eenheid wijkt af — zie notitie. |
| `w-norilsk` | Norilsk (mijn/smelter) | Rusland | mijn | 69.35, 88.20 | 3 (Kola-raffinagecircuit, niet het ertsaandeel) | Nornickel 2025 [B28] | v1-register-centroïde, niet herbevestigd | **aannemelijk** | Nornickel. Raffinage grotendeels op Kola (Severonickel) — niet gelokaliseerd. |
| `w-eagle-mine` | Eagle Mine | VS | mijn | 46.7474, -87.8819 | — (open) | geen apart cijfer | OSM-named object "Eagle Mine" | **bron-gelegd** | Lundin Mining. Kobalt is klein bijproduct. |
| `w-gem-ganzhou` | GEM Ganzhou | China | raffinaderij+recycling | 25.83, 114.93 | — (open, alleen groepscijfer) | GEM 9M-2025 groepscijfer [B29] | v1-register-centroïde, niet herbevestigd | **aannemelijk** | GEM Co. Ltd. |
| `w-jinchuan-jinchang` | Jinchuan Jinchang | China | raffinaderij | 38.50, 102.19 | — (open; groep ~17) | Jinchuan-groepscijfer [B30][B31] | v1-register-centroïde, niet herbevestigd | **onzeker** | ⚠️ Bewijs wijst naar Lanzhou als echte kobalt-vestiging, niet Jinchang. |
| `w-idaho-cobalt` | Idaho Cobalt Operations | VS | mijn (project, stil) | 45.30, -114.25 | 2 (ontworpen) | Jervois Global (v1-cijfer) [B32] | v1-register-centroïde, niet herbevestigd | **aannemelijk** | Enige Amerikaanse primaire kobaltmijn — stilgelegd. |
| `w-kabanga` | Kabanga | Tanzania | mijn (project) | -2.95, 30.45 | — (nog geen productie) | Lifezone/BHP (v1-notitie) [B33] | v1-register-centroïde, niet herbevestigd | **aannemelijk** | Westers alternatief, nog niet in productie. |

## Capaciteiten voor Chinese registersites

Geen enkele Chinese site is deze ronde via het MEE-emissieregister gelegd — het endpoint bleek (zoals verwacht) niet zonder interactieve sessie bereikbaar. Eén bekend groepscijfer, zonder vestigingscoördinaat, staat apart in `kobalt-sitelaag.json` onder `china_capaciteiten`:

| naam_zoekstring | site | capaciteit kt Co-inhoud/j | bron |
|---|---|---|---|
| `华友钴业` | Huayou Cobalt (Quzhou-terrein, coördinaat niet gevonden) | 22 | Wood Mackenzie 2021: 3,0 kt sulfaat + 19,1 kt tetroxide (Co-inhoud), grootste kobaltraffinaderij ter wereld [B34] |

## Buiten scope

Sites die evident groot/relevant zijn maar deze ronde geen bruikbare coördinaat kregen — geen coördinaat verzonnen, de lijn eindigt waar het bewijs eindigt:

- **Huayou Quzhou (kobaltraffinaderij, 22 kt Co-inhoud/j, 's werelds grootste)** — adres bekend ("No. 18 Nianxin Road, Hi-tech Industrial Park (Phase II), Quzhou, Zhejiang"), niet geocodeerbaar met Nominatim/Photon deze ronde; het MEE-register (de bedoelde bron) was niet zonder interactieve sessie bereikbaar. Het v1-registerpunt "Tongxiang" (30.63, 120.56) hoort niet bij deze raffinaderij — dat is Huayou's hoofdkantoor/nieuwe-energiecampus, een andere stad, en is daarom bewust *niet* als vervangend site-punt gebruikt (dat zou misleidend zijn geweest).
- **GEM Jingmen (Ni/Co-recyclingfabriek, 100 kt/j nameplate, Hubei)** — locatie alleen op stadsniveau bekend ("Jingmen, geografisch centrum van China, 100 km van de Drieklovendam"); geen straatadres of OSM-object gevonden.
- **Guangdong Brunp/CATL (kobaltsulfaat-recycling, Foshan)** — adres bekend ("Zhixin Avenue 6, Leping Town, Sanshui District, Foshan"), niet geocodeerbaar.
- **Ganzhou Tengyuan Cobalt (3 kt Co-metaal/j nameplate)** — adres bekend ("No. 9, Xijin Avenue, Ganzhou High-tech Industrial Development Zone, Ganxian District"), niet geocodeerbaar tot op siteniveau (alleen het 800 km²-district).
- **CNGR Tongren (precursorbasis, 60 kt precursor/j — geen los Co-cijfer)** — alleen stadsniveau gevonden.
- **Guemassa (Managem, nieuwe kobaltsulfaatfabriek, 5.000–6.000 t/j)** — project, pas voorzien voor 2026; geen coördinaat gevonden voor het bestaande of het geplande complex bij Marrakech.
- **Kola/Severonickel-raffinagecircuit (Monchegorsk, Nornickel, 3 kt Co/j nameplate)** — alleen de stad Monchegorsk gevonden (een markt-/stadscentroïde is geen anker, expliciet uitgesloten door de vaste regels); het specifieke Severonickel-complex niet als benoemd object gevonden.
- **Kisanfu, Deziwa, Sicomines, KCC-Luilu**: coördinaten zijn wél opgenomen (zie tabel) maar op **satelliet-schatting of secundaire bron**, niet op een benoemd object — bij een volgende ronde met méér tijd voor Nominatim-varianten of Amap/Baidu-navraag te verscherpen.

## Open punten

- Voor 15 van de 35 sites ontbreekt een bruikbaar, actueel Co-capaciteitscijfer (kolom "—" in de tabel) — met name kleinere DRC-mijnen (Sicomines, Chemaf, Boss Mining, Ruashi) en enkele raffinaderijen (Luilu, Niihama, Jinchuan) publiceren geen los kobaltcijfer.
- Het onderscheid "productie 2025" vs. "quotum/exportcijfer 2026" (Congo's ARECOMS-quotum sinds februari 2025) is bewust NIET in de capaciteitskolom verwerkt — de kaart tekent de weg, niet het volume, zoals de opdracht voorschrijft; waar bekend staat het wel in de notitie (Metalkol RTR).
- Talvivaara/Terrafame Sotkamo's capaciteitscijfer (7,4 kt/j) is in kobaltSULFAAT, niet in Co-inhoud — bewust niet herrekend omdat onduidelijk is of de bron zelf al op contained-metal-basis rapporteert; een volgende ronde moet dit met een Terrafame-jaarverslag verifiëren.
- De vier Chinese registersites die evident groot zijn (Huayou Quzhou, GEM Jingmen, Brunp Foshan, Tengyuan Ganzhou) staan met bekend adres maar zonder coördinaat — het MEE-register deblokkeren (interactieve sessie) is de aangewezen vervolgstap, precies zoals het ontwerp voorspelde.
- `w-kcc-luilu` (Luilu-plant) is een satelliet-schatting zonder benoemd object — de minst zekere coördinaat in de lijst; nader te bevestigen.
- De centrale ingrepen die nodig zijn voordat deze laag op de bol kan (een `--grondstof`-parameter in `voeg_sites_toe.py` + een tweede gloednodes-laadpad in `main.js`) zijn — zoals het ontwerpbestand al vaststelde — nog niet uitgevoerd; buiten scope van deze sitelaag-ronde.

## Bronnen

- **[B1]** CMOC Group, 2025 jaarresultaten/persberichten (TFM+KFM 117,5 kt Co in 2025) — https://en.cmoc.com/
- **[B2]** Reuters/Fastmarkets-coverage van CMOC's 2025-cijfers en het DRC-exportquotum — https://www.fastmarkets.com/
- **[B3]** Cobalt Institute, Cobalt Market Report 2024 (KCC 27 kt, Mutanda 8 kt) — https://cobaltinstitute.org/
- **[B4]** ERG Africa, Metalkol RTR — https://www.ergafrica.com/cobalt-copper-division/metalkol-rtr/
- **[B5]** Fastmarkets, African copper-cobalt logistics chain — https://www.fastmarkets.com/insights/african-copper-cobalt-logistics-chain-under-pressure-as-truckers-avoid-drc/
- **[B6]** Afgeleide schatting (4% van ~290 kt wereldproductie 2025) uit het ontwerpbestand `sitelaag-co.json`, geen primaire bron
- **[B7]** MMG, Kinsevere — https://www.mmg.com/operations/kinsevere/
- **[B8]** Mining Weekly, "China's MMG halts new Congo plant after one year on cobalt slump" (2025-03-06) — https://www.miningweekly.com/article/chinas-mmg-halts-new-congo-plant-after-one-year-on-cobalt-slump-2025-03-06
- **[B9]** Wikipedia, "Ruashi mine" (historisch 2008-cijfer) — https://en.wikipedia.org/wiki/Ruashi_mine
- **[B10]** Business & Human Rights Resource Centre, CDM-dambreuk Lubumbashi (nov. 2025) — https://www.business-humanrights.org/en/latest-news/drc-huayou-cobalt-subsidiary-suspended-operation-after-dam-failure-spilled-toxic-water-into-lubumbashi-incl-company-non-response/
- **[B11]** Semafor, "DRC suspends Chinese cobalt miner after Lubumbashi chemical spill" — https://www.semafor.com/article/11/10/2025/dr-congo-suspends-chinese-cobalt-miner-after-chemical-spill
- **[B12]** Wood Mackenzie, Huayue Nickel and Cobalt HPAL — https://www.woodmac.com/reports/metals-huayue-nickel-and-cobalt-hpal-cobalt-project-150012468/
- **[B13]** IDNFinancials, MBMA/Huayue HPAL — https://www.idnfinancials.com/news/52718/mbma-partners-with-huayue-nickel-cobalt-to-build-hpal-plant
- **[B14]** Mining Technology, "New project launches and ramp-ups set to lift Indonesia's cobalt output in 2026" — https://www.mining-technology.com/analyst-comment/new-project-launches-ramp-ups-lift-indonesia-cobalt-output-2026/
- **[B15]** Mysteel/SMM, Weda Bay Industrial Park veldbezoek 2025 — https://www.mysteel.net/news/5088234-flash-mysteel-visits-indonesias-weda-bay-industrial-park-iwip
- **[B16]** Glencore, productiecijfers 2023 (Murrin Murrin) — https://www.glencore.com.au/operations-and-projects/minara
- **[B17]** Sherritt International, Moa JV / Major Mines & Projects — https://miningdataonline.com/property/999/Moa-Mine.aspx
- **[B18]** mining.com, Ambatovy cycloonschade 2026 — https://www.mining.com/web/madagascan-miner-ambatovys-operations-hit-by-cyclone-traders-say/
- **[B19]** Skillings, Ambatovy-herstart 2026 — https://skillings.net/
- **[B20]** Umicore/eerdere sitelaag-ronden — https://www.umicore.fi/en/our-sites/
- **[B21]** Nikkelverk, "At a glance" — https://www.nikkelverk.no/en/who-we-are/at-a-glance
- **[B22]** USGS, Mineral Industry of Belgium 2019 — https://pubs.usgs.gov/myb/vol3/2019/myb3-2019-belgium.pdf
- **[B23]** Sumitomo Metal Mining, Niihama Nickel Refinery — https://www.smm.co.jp/en/corp_info/location/domestic/nickel/
- **[B24]** Vale, Long Harbour Nickel Processing Plant — https://en.wikipedia.org/wiki/Long_Harbour_Nickel_Processing_Plant
- **[B25]** CBC News, "Sherritt shutting down Fort Saskatchewan refinery" (2026) — https://www.cbc.ca/news/canada/edmonton/sherritt-fort-sask-refinery-9.7250254
- **[B26]** Sherritt International, jaarverslagen 2024/2025 — https://sherritt.com/operations/metals/
- **[B27]** Terrafame, battery chemicals plant Sotkamo — https://www.terrafame.com/newsroom/media-releases/terrafame-ltd.-plans-nickel-and-cobalt-chemicals-production-for-battery-applications.html
- **[B28]** Interfax/Nornickel, Kola-cobaltcircuit herstart 2025 — https://interfax.com/newsroom/top-stories/109943/
- **[B29]** GEM Co. Ltd, 9M-2025 resultaten (persberichten) — http://en.gemindonesia.com/
- **[B30]** Wood Mackenzie, Jinchuan Lanzhou Cobalt Refinery — https://www.woodmac.com/reports/metals-jinchuan-lanzhou-cobalt-refinery-150024053/
- **[B31]** Jinchuan Group — https://en.jnmc.com/
- **[B32]** Jervois Global, Idaho Cobalt Operations (v1-registerbron)
- **[B33]** Lifezone Metals / BHP, Kabanga-project (v1-registerbron)
- **[B34]** Wood Mackenzie, Huayou Quzhou-raffinage-samenvatting (3,0 kt sulfaat + 19,1 kt tetroxide) — https://www.woodmac.com/

Coördinaatbronnen: Wikipedia (geohack via de MediaWiki-API `prop=coordinates`, en/fr-taalversies), OpenStreetMap via Nominatim (https://nominatim.openstreetmap.org) en Photon (https://photon.komoot.io) — © OpenStreetMap contributors, ODbL; Esri World Imagery via `v2/tools/sat_check.py`; mindat.org voor één satellietpunt (Kisanfu).
