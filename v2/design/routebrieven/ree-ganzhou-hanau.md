# Zeldzame aardmetalen · JL MAG Ganzhou → Yantian/Rotterdam → JL MAG Europe, Schijndel (Nederland)

**stroom-id:** `ree-ganzhou-hanau` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) · **status:** gebakken
**Keten in één zin:** NdFeB-magneten van JL MAG's hoofdfabriek in Ganzhou per **truck** naar de Yantian-
containerterminal (Shenzhen), per **zeeschip** (MARNET, Zuid-Chinese Zee → Malakka → Indische Oceaan → Suez →
Rotterdam) naar Rotterdam, en per **truck** naar JL MAG's eigen Europese distributievestiging in Schijndel (NL).
**Welke as van het verhaal:** de Chinese NdFeB-magneetexport-flessenhals richting Europa, nu als **intra-company**
stroom (moederbedrijf → eigen EU-vestiging) i.p.v. een aangenomen relatie met een concurrent (zie §7).
JL MAG-groep 38,0 kt NdFeB/j bedrijfsbreed (Ganzhou+Baotou+Ningbo, 2024) [7]; wereld-NdFeB-productie >90% in
China (v1-ontwerp); zending-/factuurniveau volume voor déze as niet gepubliceerd.

## 1 · Ketenkaart
```
JL MAG Rare-Earth, Ganzhou `ree-ganzhou-jlmag` (hergebruikt `w-jlmag-ganzhou`)
  ──(b1 truck · Ganzhou–Shenzhen-corridor (G4511/惠河) via Longnan–Heyuan–Huizhou ·
     hemelsbreed ~367 km, aannemelijk: ~450-500 km over de weg, geen gepubliceerde wegkm)──►
Yantian International Container Terminals, Shenzhen `ree-yantian-kade`
  ──(zee, stippel · haven-aanloop Yantian (schematisch, over water) · ~6,6 km)──►
  ──(b2 zee · MARNET · Zuid-Chinese Zee → Straat Malakka → Indische Oceaan → Suez → Middellandse Zee →
     Gibraltar → Noordzee · ~19.000 km indicatief)──►
Rotterdam RHB (hergebruikt anker, `routebrief-licht.md` §1) `ree-rotterdam-rhb`
  ──(b3 truck · A15 → Gorinchem → A27/A59 → 's-Hertogenbosch → Schijndel, aannemelijk: geen publicatie
     voor déze zending · hemelsbreed ~76 km, aannemelijk ~100-110 km over de weg)──►
JLMAG Rare-earth Co (Europe) B.V., Schijndel `ree-schijndel-jlmageu` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | `ree-ganzhou-jlmag` → `ree-yantian-kade` | Ganzhou–Shenzhen-corridor (G4511 粤赣高速 via Longnan → 惠河高速 via Heyuan/Huizhou), aannemelijk: modaliteit/route niet gepubliceerd | hemelsbreed 367 km [berekend]; aannemelijk ~450-500 km over de weg, geen gepubliceerde wegkm | maak_stroombeen_weg (extract `china`) | nee |
| — | D | zee | `ree-yantian-kade` → zeeknoop 4553 | haven-aanloop Yantian (schematisch, over water — MARNET reikt niet tot de kade; kade > 5 km van de zeeknoop, LAR-586) | 6,6 km [gemeten, marnet_zee] | maak_havenaanloop | **ja** |
| b2 | D | zee | zeeknoop 4553 → `ree-rotterdam-rhb` | Zuid-Chinese Zee → Straat Malakka → Indische Oceaan → Suez → Middellandse Zee → Gibraltar → Noordzee (standaard Asia–NW-Europa containerlijn), aannemelijk: geen tracking-bron voor déze specifieke lading | ~19.000 km indicatief [ontwerp]; MARNET bepaalt het exacte tracé | MARNET (`--been "zee|…"`) | nee |
| b3 | D | truck | `ree-rotterdam-rhb` → `ree-schijndel-jlmageu` | A15 (Rotterdam → Gorinchem) → A27/A59 ('s-Hertogenbosch → Schijndel), aannemelijk: geen publicatie voor déze zending | hemelsbreed 76 km [berekend]; aannemelijk ~100-110 km over de weg | maak_stroombeen_weg (extract `nederland`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-ganzhou-jlmag` | fabriek (van-site) | JL MAG Rare-Earth, Ganzhou — hergebruikt letterlijk anker `w-jlmag-ganzhou` | 25,8406, 114,8663 | [7] REE-sitelaag, al satelliet-gelegd | bron-gelegd (hergebruikt, dit onderzoeksbudget niet opnieuw gecheckt) |
| `ree-yantian-kade` | overslag / containerterminal | Yantian International Container Terminals, Shenzhen | 22,5734, 114,2741 | [1][2] | bron-gelegd (z15 gezien: rijen gestapelde containers en kadekranen op het volle schiereiland-terminal in de Yantian-baai — kruis staat middenin het containerpark) |
| `ree-rotterdam-rhb` | overslag / containerterminal (canoniek Rotterdam-aanlandpunt) | RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4, Rotterdam — hergebruikt letterlijk anker uit `routebrief-licht.md` §1 | 51,8935, 4,4585 | [3] | bron-gelegd (letterlijk hergebruikt, dit onderzoeksbudget niet opnieuw gecheckt) |
| `ree-schijndel-jlmageu` | distributievestiging (naar-site) | JLMAG Rare-earth Co (Europe) B.V., Madame Curieweg 15, 5482 TL Schijndel | 51,6078, 5,4676 | [4][5][6] | bron-gelegd (z16 gezien: bedrijfspand op het moderne bedrijventerrein Duin 2, Schijndel — adrescoördinaat is een OSM-huisnummer-match op straat + postcode) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Longnan (Jiangxi, county-stad op de provinciegrens) | 24,9047, 114,7998 | pint de zuidelijke G4511-corridor (粤赣高速) vanaf Ganzhou, sluit een oostelijkere omweg via Xunwu uit |
| b1 | 2 | Heyuan (Guangdong) | 23,7443, 114,7002 | knooppunt op de aansluitende 惠河高速 (Huizhou–Heyuan-expressway), sluit een westelijkere route via Guangzhou uit |
| b1 | 3 | Huizhou (Guangdong) | 23,1120, 114,4160 | laatste grote stad vóór Shenzhen op deze corridor, pint de directe zuidoostelijke aanloop naar Yantian |
| b3 | 1 | Gorinchem (A15-corridor) | 51,8422, 4,9746 | doorgaande A15 oostwaarts vanaf Rotterdam, sluit een zuidelijkere route via Breda/Tilburg (A16/A58) uit |
| b3 | 2 | 's-Hertogenbosch (A59-aansluiting) | 51,6889, 5,3031 | laatste knoop vóór de A59-afslag naar Schijndel, pint de noordelijke in plaats van een oostelijke nadering |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| JL MAG Europe, Schijndel | JLMAG Rare-earth Co (Europe) B.V. (dochter JL MAG Rare-Earth Co., Ltd) | NdFeB-magneten (bulk, uit Ganzhou) → levering aan Europese klanten (automotive, halfgeleiders, duurzame energie, consumentenelektronica, robotica) | geen tonnage gepubliceerd (verkoop-/distributievestiging, geen productie) | [4] |

## 6 · Stoppunt
De brief stopt bij JL MAG Europe in Schijndel: dit is het (via de haalbaarheidstoets aangepaste) eindpunt van de
as — een intra-company distributievestiging, geen extern geïdentificeerde eindklant. Fase E (welke Europese
fabriek koopt hier concreet magneten) is niet in één zin te onderbouwen — JL MAG Europe noemt alleen brede
sectoren, geen naam-en-adres-klant — en vervalt.

## 7 · Open punten
- **BINDEND VERWERKT (haalbaarheidstoets):** het oorspronkelijke eindpunt Vacuumschmelze Hanau is vervangen door
  JL MAG Europe, Schijndel — VAC is zelf een concurrerende magneetfabriek en geen bron noemt JL MAG als
  leverancier van VAC; het enige aangehaalde bewijs voor een Hanau-relatie (v1-register "Chinees NdPr-oxide →
  VAC via Tianjin en Suez") betreft een ander product (oxide, geen magneten) en een ander knooppunt
  (Baotou/Tianjin) en hoort bij een andere as (`ree-baotou-*` / een toekomstige oxide-as), niet bij deze.
- **BINDEND VERWERKT (haalbaarheidstoets):** vóór b2 is een haven-aanloop-stippel bij Yantian toegevoegd — de
  kade ligt 6,6 km van de dichtstbijzijnde MARNET-zeeknoop (eigen meting, knoop 4553 op 22,55820/114,33610;
  de haalbaarheidstoets zelf mat 7,12 km met een net iets ander kandidaatpunt — beide ruim boven de 5 km-drempel
  uit LAR-586, dus de aanloop is nodig ongeacht welk exact punt op de terminal wordt gekozen).
- **Nog altijd geen zending- of contractniveau-bewijs** voor déze specifieke stroom Ganzhou → Schijndel: de as
  verbindt twee reële, gedocumenteerde JL MAG-vestigingen (grootste NdFeB-fabriek ↔ eigen EU-distributiekantoor)
  via de generieke, macro-gedocumenteerde stroom "Chinese NdFeB-export naar Europa" en de brede
  2025-exportvergunning-berichtgeving, maar geen aangetoonde individuele zending. Dit is nu wel een aannemelijke
  interne bedrijfsstroom in plaats van een verzonnen relatie met een concurrent.
- **b1 en b3 hebben geen gepubliceerde wegkilometer** — alleen hemelsbreed berekend + corridor-aanname; de
  bakstap moet dit met een echte wegscan vaststellen (±15%-toets geldt dan als indicatie, niet als harde norm,
  conform de vaste regel bij een hemelsbreed-schatting).
- **Modaliteit van b1 en b3 zelf is aangenomen** (truck) — geen bron noemt expliciet hoe JL MAG zijn eigen
  fabrieks-naar-haven- en haven-naar-vestiging-transport regelt; truck is de enige plausibele modaliteit over
  deze korte binnenlandse afstanden (geen spoorverbinding tussen deze exacte punten gepubliceerd).
- **Jaarvolume specifiek voor déze as ontbreekt** — alleen JL MAG's bedrijfsbrede 38,0 kt NdFeB/j (Ganzhou +
  Baotou + Ningbo, niet per vestiging of exportbestemming uitgesplitst) [7].
- **De Yantian-kade is site-niveau, niet berth-niveau** — het satellietbeeld toont het volle terminal-schiereiland;
  welke specifieke berth NdFeB-ladingen (in reguliere containers, geen bulk) verlaat is niet uit een bron af te
  leiden en ook niet relevant op dit detailniveau.

## 8 · Bronnen
[1] Wikipedia (EN), "Yantian International Container Terminals" — coördinaat 22,5734/114,2741. https://en.wikipedia.org/wiki/Yantian_International_Container_Terminals
[2] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-ree-ganzhou-hanau-yantian.png`.
[3] `v2/design/routebrief-licht.md` §1 + `v2/design/routebrieven/koper-lobito-duisburg.md` — canoniek anker Rotterdam RHB (Waalhaven Noordzijde 4), 51,8935/4,4585, eerder satelliet-gelegd.
[4] jlmag.eu (bedrijfswebsite, JSON-LD schema.org Organization-blok) — JLMAG Rare-earth Co (Europe) B.V., Madame Curieweg 15, 5482 TL Schijndel, NL; dochter van JL MAG Rare-Earth Co., Ltd; klanten in automotive/halfgeleiders/duurzame energie/consumentenelektronica/robotica. https://jlmag.eu/
[5] OpenStreetMap (ODbL) via Photon-geocoder — huisnummer-match Madame Curieweg 15, Schijndel, 51,6078123/5,4675948. https://photon.komoot.io
[6] Esri World Imagery via `v2/tools/sat_check.py` (z16, live) — `v2/build-cache/satcheck/sat-ree-ganzhou-hanau-schijndel.png`.
[7] `v2/design/ree-sitelaag.json`, anker `w-jlmag-ganzhou` — JL MAG Rare-Earth Ganzhou, 25,8406/114,8663, capaciteit 38,0 kt NdFeB/j bedrijfsbreed (bron SMM/JL MAG-jaarverslag 2024, [B19][B20] in de sitelaag).
[8] Bloomberg, 2026-09-21, "World's Top Rare-Earth Magnet Maker Gives Xi Leverage Over US" (aangehaald in de haalbaarheidstoets-webcheck van deze opdracht) — bevestigt JL MAG als wereldwijd grootste magneetmaker en de geopolitieke-hefboom-framing van deze as.
[9] news.metal.com, "JL MAG Rare-Earth Sets New Highs with Over 90% Capacity Utilization in 2024". https://news.metal.com/newscontent/103258207/JL-MAG-Rare-Earth-Sets-New-Highs-with-Over-90-Capacity-Utilization-in-2024
[10] forcedistancetimes.com, "The week that's done: a US rare-earth magnet factory's China ties" — achtergrond VAC/Wolong-aandeelhouderschap, gebruikt in de oorspronkelijke as-analyse (§7). https://forcedistancetimes.com/the-week-thats-done-a-us-rare-earth-magnet-factorys-china-ties/
[11] Wikipedia (EN), "Heyuan" — 23,7443/114,7002. https://en.wikipedia.org/wiki/Heyuan
[12] Wikipedia (EN), "Huizhou" — 23,112/114,416. https://en.wikipedia.org/wiki/Huizhou
[13] OpenStreetMap (ODbL) via Photon-geocoder — Longnan-stad (Jiangxi) 24,9047/114,7998 · Gorinchem 51,8422/4,9746 · 's-Hertogenbosch 51,6889/5,3031. https://photon.komoot.io
[14] `v2/tools/hecht_marnet.py` (`marnet_zee`) — eigen zeeknoop-afstandsmeting: Yantian 6,58 km tot knoop 4553 (22,55820/114,33610) · Rotterdam RHB 0,73 km tot knoop 6818 (51,90000/4,45740), geen aanloop nodig bij Rotterdam.
[15] Haalbaarheidstoets M31 golf 6 voor `ree-ganzhou-hanau` (workflow-invoer bij deze opdracht) — verwierp het oorspronkelijke eindpunt Vacuumschmelze Hanau (product-/entiteitsmismatch met bron [10]) en wees JL MAG Europe Schijndel aan als vervangend, beter onderbouwd eindpunt.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Functie:** `bak_ree_ganzhou_hanau()` in `v2/tools/bak_stromen.sh` · **json:** `v2/data/stroomroute-ree-ganzhou-hanau.json`
(133,8 KB) · **draaien:** `bash v2/tools/bak_stromen.sh ree-ganzhou-hanau`.

| # | modaliteit | km | punten | stippel | recept |
|---|---|---|---|---|---|
| b1 | truck | 424,2 | 3.659 | nee | `maak_stroombeen_weg.py --profiel ree-ganzhou-hanau-ganzhou-yantian` (extract china) |
| b1-aanloop | zee | 6,6 | 2 | **ja** | rechte stippel (`maak_havenaanloop.py` exit 124, geen tweede poging) |
| b2 | zee | 18.214,5 | 1.896 | nee | MARNET-router, zeeknoop 4553 → Rotterdam RHB |
| b3 | truck | 95,2 | 1.387 | nee | `maak_stroombeen_weg.py --profiel ree-ganzhou-hanau-rhb-schijndel` (extract nederland) |
| **totaal** | | **18.740,5** | **6.944** | | 4 markers |

**Toelichting per been:**
- **b1 (truck, Ganzhou → Yantian):** geen gepubliceerde wegkm (brief §2/§7) — getekend 424,2 km tegen hemelsbreed
  367 km (ratio 1,16) en de brief-aanname ~450-500 km over de expressway; de ±15%-toets gold als indicatie, niet
  als norm, en de gemeten waarde valt binnen de aannemelijke bandbreedte. Alle drie via-snaps (Longnan/Heyuan/
  Huizhou) ≤ 0,12 km, ankersnaps 0,01/0,18 km — geen wegklasse-correctie nodig, `corridorKlassen`
  (tertiary/unclassified) volstond zonder terugval.
- **b1-aanloop (zee, stippel, Yantian):** `maak_havenaanloop.py` liep vast op `timeout 300` (exit 124) → conform
  de vaste regel geen tweede poging, terugval op de rechte stippel uit de brief (6,6 km, kade > 5 km van
  zeeknoop 4553, LAR-586).
- **b2 (zee, MARNET):** zeeknoop 4553 → Rotterdam RHB, 18.214,5 km. Rotterdam zelf snapt op 0,73 km van
  zeeknoop 6818 — dat is de naad tussen b2 en b3, ruim binnen de 5 km-norm, geen tweede haven-aanloop nodig
  aan de Rotterdamse kant.
- **b3 (truck, Rotterdam RHB → Schijndel):** geen gepubliceerde wegkm — getekend 95,2 km tegen hemelsbreed 76 km
  (ratio 1,25), iets onder de brief-aanname van ~100-110 km maar binnen de indicatieve bandbreedte (geen bron,
  dus geen harde ±15%-norm). Alle snaps ≤ 0,50 km, geen airside/privéterrein-stippel nodig (gewoon
  bedrijventerrein Duin 2 met openbare weg tot vlak bij het pand, zoals verwacht).

**Toets (bakhandleiding §5):**
- Naden tussen opeenvolgende benen: 0,00 / 0,00 / 0,73 km — geen naad > 5 km.
- `toets_knikken.py`: 52 knikken ≥ 60°, 2 omkeringen (waarvan 1 terugloop). De terugloop (152,5°, straal 11 m,
  23,74469/114,70083) valt exact op het Heyuan-via-punt (23,7443/114,7002) — een klein overschiet-en-terug-
  snapartefact op het via-punt zelf, geen omweg (verwaarloosbare km-impact op 424 km). Niet gerepareerd door
  het via-punt te verschuiven (dat zou de km-toets sturen in plaats van de corridorkeuze te volgen); staat hier
  als bevinding.
- `toets_rechte_benen.py --min-km 5`: alleen de b1-aanloop-stippel (2 punten, omwegfactor 1,002) komt boven de
  5 km-drempel uit — dat is precies de rechte stippel die hij zou moeten zijn, geen bevinding.
- JSON-contract: `versie` 2, `punt_formaat` "lonlat", modaliteiten {truck, zee} (beide in de toegestane set),
  elk been ≥ 2 punten, bestandsgrootte 133,8 KB.

**Gedeelde bestanden aangepast:** `PROFIELEN`-sleutels `ree-ganzhou-hanau-ganzhou-yantian` en
`ree-ganzhou-hanau-rhb-schijndel` in `v2/tools/maak_stroombeen_weg.py` · functie `bak_ree_ganzhou_hanau()` in
`v2/tools/bak_stromen.sh`. Beide alleen toegevoegd (nieuwe sleutels/functie), geen bestaande sleutel/functie
gewijzigd.

**Lessen:** de Heyuan-terugloop bevestigt opnieuw de "overschiet-en-terug op een via-punt"-klasse uit de
bakhandleiding, hier op een schaal (11 m) die geen ingreep rechtvaardigt — een via-punt pas verschuiven bij een
échte omweg (segment-km ≫ hemelsbreed), niet bij een knik van enkele meters.
