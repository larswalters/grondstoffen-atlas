# Zeldzame aardmetalen · Northern RE-scheiding Baotou → Tianjin → Rotterdam → Vacuumschmelze, Hanau (Duitsland)

**stroom-id:** `ree-baotou-hanau` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** gescheiden NdPr-oxide van de Northern Rare Earth-scheiding (Huamei, Baotou) gaat (aannemelijk: één
bron) per **truck** over de G6 en Beijing's zesde ring naar het containerterminalgebied van Tianjin (Beijiang), per
**zeeschip** (MARNET: Gele Zee → Malakka → Suez → Noordzee) naar Rotterdam RHB en per **truck** (A15 → A12 → A3) naar
Vacuumschmelze (VAC) in Hanau, de enige Europese NdFeB-magneetfabriek van schaal.
**Welke as van het verhaal:** reserve-as 4 — de Europese magneet-flessenhals langs het *oxide*-spoor (v1-register:
"Chinees NdPr-oxide → VAC via Tianjin en Suez"). As 1 (`ree-ganzhou-hanau`) is inmiddels een JL MAG-magneetstroom naar
Schijndel; dit is de VAC-koppeling. Volume: Huamei 106,661 kt REO/j bedrijfsbreed (fase 1, okt 2024) [3]; VAC Hanau
~1,0 kt NdFeB/j [6]; niets per bestemming gepubliceerd. **Geen bron noemt een Baotou→VAC-levering** — zie §7.

## 0 · Toets en ontwerp verwerkt
Bindend: **haven-aanloop-stippel bij Tianjin** (kade 14,92 km van zeeknoop 9649 op 38,8910/117,8503, eigen meting; toets 14,81).
Het ontwerp noemde b1 "hemelsbreed ~550 km"; gemeten is **697 km** — het getal in het ontwerp klopte niet. Rolverdeling
as 1/as 4 uit het niet-bindende advies staat hierboven. **b3 is géén kopie van as 1:** die eindigt in Schijndel
(`ree-ganzhou-hanau-rhb-schijndel`), dus Rotterdam → Hanau krijgt een eigen profiel.

## 1 · Ketenkaart
```
Northern RE-scheiding (Huamei) `ree-baotou-scheiding` ──(b1 truck · G6 → Beijing 6e ring → 京津塘 · hemelsbreed 697 km)──►
Tianjin, containerterminal Beijiang `ree-tianjin-kade` ──(stippel · haven-aanloop 30,8 km)──► zeeknoop 9649
──(b2 zee · MARNET · ~20.600 km)──► Rotterdam RHB `ree-rotterdam-rhb`
──(b3 truck · A15 → A12 → A3 · hemelsbreed 369 km)──► Vacuumschmelze `ree-hanau-vac` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck (aannemelijk: modaliteit niet gepubliceerd) | `ree-baotou-scheiding` → `ree-tianjin-kade` | G6 (呼包 → 呼集 → 京张) → 北六环 → 东六环 → 京津塘 → G103 | hemelsbreed 697 km, geen wegkm; indicatie ~800 (G6 Baotou–Beijing ~629 volgens kilometertabel [4], niet bevestigd, + Beijing→haven) | maak_stroombeen_weg (china) | nee |
| — | C | zee | `ree-tianjin-kade` → zeeknoop 9649 | haven-aanloop Tianjin (kade > 5 km van zeeknoop, LAR-586) | 30,8 km pad over water, 22 punten [gemeten] | maak_havenaanloop (geslaagd, 300 s niet gehaald) | **ja** |
| b2 | C | zee (aannemelijk: één bron) | zeeknoop 9649 → `ree-rotterdam-rhb` | Bohai → Gele Zee → Malakka → Indische Oceaan → Suez → Noordzee | 20.638 km [MARNET-proef] tegen ~19.500 [ontwerp, indicatief] | MARNET | aanloop: ja (vorige rij) |
| b3 | C | truck (aannemelijk) | `ree-rotterdam-rhb` → `ree-hanau-vac` | A15 → A12 → A3 (Emmerich–Köln–Montabaur–Offenbacher Kreuz) | hemelsbreed 369 km, geen wegkm; indicatie ~470 | maak_stroombeen_weg (nederland, de-nrw, de-rheinland-pfalz, de-hessen) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-baotou-scheiding` | scheiding / van-site | Northern RE 冶炼分公司 / Huamei, 稀土高新区 — hergebruikt letterlijk uit `ree-bayanobo-baotou.md` | 40.5884, 109.8741 | [2][3] | bron-gelegd (hergebruikt; z15 nogmaals gezien: ommuurd industrieterrein met hallen aan de stadsrand tussen akkers; sitelaag `w-baotou-huamei` ligt er 0,35 km naast) |
| `ree-tianjin-kade` | overslag / containerterminal | Tianjin Port, Beijiang-haven, oostkade (exploitant niet vastgesteld) | 39.0100, 117.7705 | [7][9] | bron-gelegd (z16 gezien: kadekranen langs de oostkade, containerstapels op het terminal-yard, kruis op de apron; Wikipedia-havencentroïde 38,9758/117,7875 niet gebruikt) |
| `ree-rotterdam-rhb` | overslag / losplek | RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4 — hergebruikt letterlijk uit `routebrief-licht.md` §1 | 51.8935, 4.4585 | [8] | bron-gelegd (hergebruikt; zeeknoop 6818 op 0,73 km, geen aanloop) |
| `ree-hanau-vac` | magneetfabriek / naar-site | Vacuumschmelze (VAC), Grüner Weg 37, Hanau (Südost) | 50.1308, 8.9305 | [5][10] | bron-gelegd (z17 gezien: uitgestrekt industrieterrein met witte hallen aan Leipziger Straße, werkbrandweer van VAC in OSM op 0,3 km; OSM-landuse "Vacuumschmelze" op 50,1307/8,9301 en 50,1316/8,9318) |

Sitelaag `w-vac-hanau` (50.1300, 8.9284) is een straatmidden en ligt 0,17 km westelijk van dit satelliet-gelegde punt — centraal gelijktrekken.

## 4 · Via-punten (alleen landbenen met een corridorkeuze; allemaal op motorway/trunk, niet in een centrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | G6;G7 呼包高速, Hohhot-west | 40.7443, 111.3055 | Baotou–Hohhot over de G6-autosnelweg i.p.v. G110, vóór de Hohhot-ring (way/161787162) |
| b1 | 2 | G6 呼集高速, Jining | 40.9647, 113.0838 | G6 Hohhot–Jining i.p.v. de G55/G208-takken (way/211357904) |
| b1 | 3 | G6 京张高速, Xuanhua | 40.6323, 115.0147 | G6 via Zhangjiakou/Xuanhua naar Beijing i.p.v. de G110 (way/53588040) |
| b1 | 4 | G4501 北六环, Changping | 40.1693, 116.2271 | trucks de zesde ring op i.p.v. door Beijing's binnenringen (way/157838596) |
| b1 | 5 | G4501 东六环, Tongzhou | 39.8143, 116.6487 | ring doorgereden tot oost (geen sprong door het centrum) (way/29131831) |
| b1 | 6 | 京津塘高速, Wuqing | 39.4151, 117.0475 | Beijing–Tianjin–Tanggu-corridor i.p.v. de S15 naar Tianjin-stad (way/187504470) |
| b1 | 7 | G103 京滨线, havenaanloop | 39.0273, 117.6627 | laatste doorgaande weg naar de Beijiang-terminal (way/350468599) |
| b3 | 1 | A15, Betuwe | 51.9199, 5.5715 | A15 → A12 over Zevenaar i.p.v. de noordelijke A12 via Utrecht (way/509618594) |
| b3 | 2 | A3, Emmerich | 51.8862, 6.1782 | grensovergang Elten/Emmerich i.p.v. Venlo (A61) (way/27838928) |
| b3 | 3 | A3, Köln-Porz | 50.9179, 7.0943 | A3 oostelijk om Köln (way/310361284) |
| b3 | 4 | A3, Montabaur | 50.4510, 7.9012 | A3 Köln–Frankfurt i.p.v. A61 langs de Rijn (way/37386469) |
| b3 | 5 | A3, Offenbacher Kreuz | 50.0676, 8.7990 | laatste knoop vóór Hanau; daarna A3/A66 naar de terreinweg (way/1412537196) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Northern RE-scheiding (Huamei), Baotou | China Northern Rare Earth | REE-concentraat → gescheiden oxiden/carbonaat | 106,661 kt REO/j (fase 1, okt 2024) | [3] |
| VAC, Hanau | Vacuumschmelze (overname door Energy Fuels aangekondigd juni 2026) | gescheiden metalen/legeringen → NdFeB-magneten | ~1,0 kt magneten/j Hanau [6]; Sumter (VS) 2 kt/j | [1][6] |

## 6 · Stoppunt
De brief stopt bij VAC Hanau: dat is de naam-en-adres-afnemer in het ontwerp en de enige Europese magneetmaker met eigen
Hanau-fabriek; wat VAC met de magneten doet (auto/wind/defensie) staat niet per zending in een bron — fase D/E vervalt.

## 7 · Open punten
- **Geen enkele bron legt Baotou-oxide bij VAC.** Het enige spoor is ons eigen v1-register [11]; VAC zelf meldt juist diversificatie
  (Torngat, Pensana, Ucore: niet-Chinese oxide) [12] en zegt "separated rare earth metals and alloys" te kopen [1]. Reserve-as,
  aannemelijk op macro-niveau, **geen zending- of contractbewijs** — zo staat het in de beennaam.
- **Product:** de scheiding levert oxide; VAC koopt volgens [1] metaal/legering. De oxide→metaal-stap (strip casting) zit tussen en is niet getekend.
- **b1-modaliteit** is aangenomen. Spoor bestaat (Jingbao 833 km Baotou–Beijing [4], plus Beijing–Tianjin) maar is niet gekozen;
  geen wegkm gepubliceerd — de ±15%-toets (680–920 km) is een indicatie.
- Containerterminal-exploitant en kade (Beijiang vs Dongjiang) niet vast te stellen op site-niveau; Esri toont containerkranen, geen operator.
- **Tooling 2026-10-09:** pyosmium is geblokkeerd (app-control), dus `--bron geofabrik` faalt; Overpass-mirrors: alleen maps.mail.ru
  antwoordt (overpass-api.de reset, kumi/private.coffee 500); Wikipedia-API gaf 429. Via-punten zijn daarom via maps.mail.ru gevonden.
- b2 is 20.638 km tegen ~19.500 in het ontwerp (+5,8%); de MARNET-router bepaalt, geen publicatie.

## 8 · Bronnen
[1] rare-earth-mining.com, "Vacuumschmelze (VAC): Essential Magnet Maker Profile" — Hanau, zet gescheiden metalen/legeringen om in magneten; Sumter 2.000 tpa → 12.000. https://rare-earth-mining.com/vacuumschmelze/
[2] `v2/design/routebrieven/ree-bayanobo-baotou.md` — anker `ree-baotou-scheiding` (OSM-landuse Huamei, z15).
[3] Metalnomist 2024-11 via `ree-sitelaag.json` [B4] — Huamei fase 1: 106.661 t REO/j. https://www.metalnomist.com/2024/11/china-launches-worlds-largest-rare.html
[4] Wikipedia (EN), "Beijing–Baotou railway" (833–834 km) en "G6 Beijing–Lhasa Expressway" (kilometertabel, Baotou-vak ~629 vanaf Beijing, niet bevestigd). https://en.wikipedia.org/wiki/Beijing–Baotou_railway
[5] OSM via Photon-geocoder — Grüner Weg Hanau, landuse "Vacuumschmelze" 50,1307/8,9301 en 50,1316/8,9318, brandweer 50,1290/8,9295. https://photon.komoot.io
[6] t-online, 2026-04-28, "Rohstoffkonflikt mit China…" — Hanau ~1.000 t magneten/j, ~€400 mln omzet. https://www.t-online.de/finanzen/aktuelles/wirtschaft/id_101230912/rohstoffkonflikt-mit-china-trump-setzt-auf-weltmarktfuehrer-aus-deutschland.html
[7] Wikipedia (EN), "Port of Tianjin" — havencentroïde 38,9758/117,7875, Xingang = hoofdhaven. https://en.wikipedia.org/wiki/Port_of_Tianjin
[8] `v2/design/routebrief-licht.md` §1 + `routebrieven/ree-ganzhou-hanau.md` — anker Rotterdam RHB, zeeknoop 6818 op 0,73 km.
[9] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-ree-baotou-hanau-{baotou-scheiding,tianjin-verken,tianjin-kade,tianjin-kade2,vac,vac-b}.png`.
[10] Esri-controle VAC (z17) + Photon/Nominatim-adres "Grüner Weg 37, Hanau"; `ree-sitelaag.json` `w-vac-hanau`, [B23][B24].
[11] `data/rare-earths.js` — flow `ree-ref-baotou` → `ree-mag-vac` via `ree-port-tianjin` (v1, eigen aanname).
[12] ANSA/Mining Weekly 2025-08 — VAC–Torngat-MoU (niet-Chinese oxide); Pensana, Ucore. https://www.ansa.it/pressrelease/english/2025/08/26/vac-and-torngat-metals-announce-strategic-partnership-to-strengthen-rare-earth_0b1852a4-84f0-41b0-802b-c4982fbd0c6a.html
[13] OSM-ways via Overpass-spiegel maps.mail.ru (2026-10-09), way-id's in §4. · `maak_havenaanloop.py` en `hecht_marnet.py` (zeeknoop 9649, 20.638,1 km).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-ree-baotou-hanau.json` · 257,7 KB · versie 2, `punt_formaat` lonlat · 4 benen · 21.999,4 km · 13.202 punten · 4 markers.
Recept: `bash v2/tools/bak_stromen.sh ree-baotou-hanau` (functie `bak_ree_baotou_hanau`); profielen `ree-baotou-hanau-baotou-tianjin` en
`ree-baotou-hanau-rhb-hanau` in `maak_stroombeen_weg.py`. Registersleutel (centraal): `ree-bh`.

| # | modaliteit | km | tegen brief | naad naar vorige | punten | opmerking |
|---|---|---|---|---|---|---|
| b1 | truck | 848,2 | indicatie ~800 / hemelsbreed 697: **+6,0%** (band 680–920, geen wegkm → indicatie) | — | 5.343 | G6 → 6e ring → G103 → 京津塘; snaps ≤ 0,02 km |
| aanloop | zee, **stippel** | 30,8 | 30,8 gemeten (22 punten, omwegfactor 2,06) | 0,00 km | 22 | haven-aanloop Tianjin, kade 14,9 km van zeeknoop 9649 (LAR-586) |
| b2 | zee (MARNET) | 20.638,1 | ontwerp ~19.500 (indicatief): +5,8% — MARNET beslist | 0,00 km | 2.150 | 162 MARNET-edges; Rotterdam snapt op 0,73 km (zeeknoop 6818) |
| b3 | truck | 482,3 | indicatie ~470 / hemelsbreed 369: **+2,6%** (band 400–540, indicatie) | 0,73 km (= de zee-snap) | 5.687 | A15 → A12 → A3 → Hanau; snaps ≤ 0,13 km |

Markers: alle vier op 0 m van de lijn. `toets_knikken`: zee 0 omkeringen; b3 1 omkering (165,8°, 15 m straal, v = 1,2 = echte bocht, knooppunt vóór Hanau);
b1 6 omkeringen waarvan 3 "terugloop" van 100–200 m (Hohhot 40.7435/111.3258, Xuanhua 40.6252/115.0731, 6e ring NO 40.1133/116.6206) — dat zijn
haarspeldlussen op knooppunten in de OSM-geometrie (de graaf is ongericht; geen via-punt ligt daar), niet hersteld; samen < 1 km op 848 km.
`toets_rechte_benen --min-km 5`: geen enkel doorgetrokken been van deze stroom is recht; de aanloop is stippel met reden.

**Toelichting per stippel/aanloop:** de enige stippel is de haven-aanloop Tianjin (zee): `maak_havenaanloop.py` slaagde (kortste pad over water, 0,96 km over land aan het
kade-uiteinde = 1:10M-korrel); stippel betekent hier "MARNET reikt niet tot de kade", niet "onzeker". Geen vlucht, geen spoor, geen leiding, geen last-mile-been.

**Wat anders uitviel dan de brief (afwijkingen_van_ontwerp):**
1. **b1-via's.** De drie via-punten van de brief rond Beijing gaven in de eerste bake een route door de STAD (Badaling-G6 → Deshengmen → Jingtong-G103, 71 km, 5 km van het centrum) in plaats van de
   6e ring: de NO-hoek van de ring heeft in OSM **geen `ref=G4501`** (alleen `name=六环/6th Ring Road`, `int_ref=AH3`), dus de ref-voorkeur (factor 3) bestrafte juist de ring.
   Opgelost met drie extra via-punten óp de ring (116.5974/40.1419 · 116.6183/40.0962 · 116.6550/40.0408; snap ≤ 7 m). De brief-via's Changping (116.2271/40.1693), Tongzhou
   (116.6487/39.8143) en Wuqing (117.0475/39.4151) gaven keerlussen van 3,1 / 15,2 / 5,4 km (zijtak resp. vóór de aansluiting waar de route de weg oprijdt): Changping is
   doorgeschoven naar 116.3506/40.1642, Tongzhou is vervallen, Wuqing staat nu op 117.1057/39.3881 (voorbij de G103-aansluiting). Eindstand: 25,9 km van het centrum van Beijing. De lijn passeert Tianjin-stad op 5,8 km (de 京津塘-expressway loopt langs de zuidrand naar Tanggu), Frankfurt op 5,4 km, Utrecht op 26,9 km.
2. **Tussen de 6e ring en Wuqing rijdt de router de G103 (Jingbin-weg)**, niet de 京津塘-expressway (die in OSM zonder `ref` staat); de expressway pakt hij vanaf Wuqing. Beide zijn legitieme vrachtroutes;
   de beennaam noemt beide.
3. **b3-refs.** Duitse wegnummers staan in OSM met spatie (`A 3`, `A 66`); de brief-refs `A3`/`A66` matchten in Duitsland niets, waardoor de eerste bake bij Frankfurt dwars door de stad
   (Westend → Hbf, 0,4 km van het centrum) reed. Profiel gebruikt nu `A 3`/`A 66` (NL: `A15`/`A12` zonder spatie). Lengte 475,3 → 482,3 km, route nu over de A3.
4. Het id belooft Hanau en de lijn eindigt in Hanau: geen afwijking tussen id en eindpunt.

**Recept/gereedschap:** wegscan via Overpass (pyosmium geblokkeerd) met een eigen tegelwrapper (0,5°-tegels, 3 threads, retry op `maps.mail.ru`; klassen motorway..secondary, de kleine eindklassen alleen bij de ankers;
b1 90 tegels, b3 42 tegels, ~55 min wandkloktijd doordat de enige werkende spiegel bijna steeds 504 gaf). Tegelcache en wrapper staan in het scratchpad (`ree_bh/`), niet in de repo.

**Lessen:** (a) controleer bij een stad-doorsnijdende ring de `ref`-tags van de ringways zelf, niet alleen de wegnummers uit de brief; (b) test refs per land (spaties in DE); (c) lees bij elke wegbake de afstand van de lijn tot het stadscentrum, niet alleen de km-toets:
beide eerste bakes zaten binnen de ±15%-band en waren toch fout; (d) een via-punt dat een keerlus > 1 km geeft ligt op een zijtak of vóór de oprit — verschuif of laat vervallen, schuif er niet bij.
