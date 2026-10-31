# Routebrief (licht) · Zeldzame aardmetalen · Korean Metals Plant Ochang → Busan → Muuga → Neo Narva (Zuid-Korea → Estland)

**stroom-id:** `ree-ochang-narva` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · Korean Metals Plant Ochang → Busan → Muuga → Neo Narva (Zuid-Korea → Estland; aannemelijk: één bron voor de bestemming)
**Keten in één zin:** Dy-/Tb-metaal (en NdPr-metaal/NdFeB-legering) van ASM's Korean Metals Plant in Ochang gaat per truck naar Busan New Port, per containerschip (MARNET: Malakka, Suez, Gibraltar, Kanaal, Noordzee, Oostzee) naar de Finse Golf, over een stippel-haven-aanloop naar Muuga en per truck over weg 1/E20 naar Neo's magneetfabriek in Narva. Stoppunt bij de fabriekspoort.
**Welke as van het verhaal:** Korea als metaalhub naar Europa's eerste sintermagneetfabriek. Geen jaarvolume. Enige bestemmingsbron: 2 kg Tb + 2 kg Dy-metaal, jul 2025, "naar Neo's magneetfabriek in Estland" [1]. KMP 1,3 kt NdFeB-legering/j, doel 3,6 kt/j (kt legering, geen REO; peiljaar 2026) [2]; Narva fase 1 2 kt NdFeB/j [3][4].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** zeebeen exact als bewezen (knoop 5621 → 1970, 22.199,0 km, via Suez); vier benen zijn LETTERLIJKE KOPIEEN; beennamen "aannemelijk: een bron voor de bestemming"; de 19 t NdPr (Magnequench, dec 2024) heeft op [1] geen bestemming en wordt NIET aan Narva toegeschreven; volume = 2 kg + 2 kg, geen jaarcijfer. Eindpunt Narva klopt met het id.

## 1 · Ketenkaart
```
KMP Ochang `ree-ksm-fabriek` ──(b1 truck · Jungbu 35 → Gyeongbu 1 → 30 → Jungbu Naeryuk 45 → Changwon · hemelsbreed 222 km, kopie gemeten 279,4 km)──►
Busan New Port `ree-busan-kade` ╌╌(b2a haven-aanloop, STIPPEL · 10,8 km)╌╌► zeeknoop 5621 ──(b2b zee · MARNET · 22.199,0 km)──► zeeknoop 1970 (Finse Golf)
╌╌(b3 haven-aanloop Muuga, STIPPEL · 37,5 km)╌╌► Muuga-terminal `ree-muuga-ct` ──(b4 truck · Muuga sadama tee → weg 1/E20 · hemelsbreed 180,4 km, kopie 202,7 km)──►
Neo Narva `ree-narva-magneetfabriek` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck (aannemelijk: een bron) | `ree-ksm-fabriek` → `ree-busan-kade` | Jungbu Expwy 35 → Gyeongbu 1 → Seosan-Yeongdeok 30 → Jungbu Naeryuk 45 → Changwon | hemelsbreed 222 km, geen wegkm; kopie 279,4 (OSRM 279, OSM-afgeleid) [9] | KOPIE b1 ree-cheongju-sanmarcos (maak_stroombeen_weg, zuid-korea) | nee |
| b2a | C | zee (haven-aanloop) | `ree-busan-kade` → zeeknoop 5621 (35.0485, 128.7268) | Busan New Port-aanloop, kade 10,1 km van de knoop (> 5 km, LAR-586) | 10,8 (kopie) [9] | KOPIE b2a ree-cheongju-sanmarcos (stippel-geojson) | **ja** — MARNET reikt niet tot de kade |
| b2b | C | zee (aannemelijk: een bron) | zeeknoop 5621 → zeeknoop 1970 (59.8000, 24.7000) | Malakka, Rode Zee/Suez, Gibraltar, Kanaal, Noordzee, Oostzee (MARNET kiest) | 22.199,0 (eigen MARNET-proef 2026-10-31, 182 edges, snaps 0,000) [10] | MARNET | nee |
| b3 | C | zee (haven-aanloop) | zeeknoop 1970 → `ree-muuga-ct` | over water tussen Viimsi-punt en Prangli, kade 37,5 km van de knoop | 37,5 (rechte lijn, kopie) [8] | KOPIE b3 ree-kuantan-narva (`--stippel`-regel) | **ja** — hier reikt het net niet |
| b4 | D | truck (aannemelijk: bestemming Narva alleen via [1]) | `ree-muuga-ct` → `ree-narva-magneetfabriek` | Muuga sadama tee → Peterburi tee → weg 1/E20 Tallinn–Narva mnt → Kulgu-tööstuspark | hemelsbreed 180,4 km, geen wegkm; kopie 202,7 (OSRM 206,3); weg 1 = 212 km Tallinn–Narva [6] | KOPIE b4 ree-kuantan-narva (maak_stroombeen_weg, estland) | nee |

Beennaam b2b: "… (aannemelijk: een bron voor de bestemming; haven en zeeroute niet gebronnen)". Geen luchtbeen: geen bron zegt dat deze 4 kg vliegt (zie §7). b1, b2a, b3 en b4 zijn bestandskopieen (§9 voor de bak-agent), geen tweede versie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-ksm-fabriek` | metaal-/legeringsfabriek (kop b1) | Korean Metals Plant (KSM Metals/KSMM, ASM → Energy Fuels), Gwahaksaneop 4-ro, Cheongju | 36.7009, 127.4147 | hergebruikt letterlijk uit `ree-cheongju-sanmarcos.md` §3 [1][2][7] | **onzeker** (z15 gezien, `sat-ree-ochang-narva-kmp.png`: dicht industriecomplex met hallen en een groot parkeerterrein, plantgebouw niet aanwijsbaar; bron plaatst KMP in de Ochang Foreign Investment Zone, B/L in Oksan-myeon) |
| `ree-busan-kade` | overslag truck → zee | Busan New Port, containerterminal | 35.0731, 128.8338 | hergebruikt letterlijk uit `ree-cheongju-sanmarcos.md` §3 (daar uit `kobalt-huayou-gunsan.md`) [9] | bron-gelegd in die briefs; hier z15 gezien (`sat-ree-ochang-narva-busan.png`): containeropslag en kadeapron aan het bekken oost van de portaalkranen; terminal voor deze lading niet gebronnen |
| `ree-muuga-ct` | overslag zee → truck | Muuga-containerterminal (HHLA TK Estonia), Muuga sadam | 59.4915, 24.9675 | hergebruikt letterlijk uit `ree-sillamae-newark.md` §3 / `ree-kuantan-narva.md` §3 [8] | bron-gelegd in die briefs; hier z15 gezien (`sat-ree-ochang-narva-muuga.png`): kade met portaalkranen, schip en containerstapels; haven voor deze lading = aanname |
| `ree-narva-magneetfabriek` | magneetfabriek (losplek, stoppunt) | Neo Performance Materials, NPM Narva OÜ, Kulgu-tööstuspark | 59.3618, 28.1478 | hergebruikt letterlijk uit `ree-sillamae-narva.md` §3 [5] | bron-gelegd in die brief; hier z15 gezien (`sat-ree-ochang-narva-narva.png`): gebouwencluster met opslagterrein aan de doorgaande weg tussen twee meren |

Zeeknoop 5621 (35.0485, 128.7268) en 1970 (59.8000, 24.7000) zijn MARNET-knopen, geen ankers. Geen last-mile-benen: beide fabrieken liggen aan het net.

## 4 · Via-punten (alleen landbenen; beide zijn kopieen)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1-6 | zes punten op Jungbu 35, Seosan-Yeongdeok 30, Jungbu Naeryuk 45, Changwon, Jinhae Sanup-ro | zie `ree-cheongju-sanmarcos.md` §4 (36.5228,127.5311 · 36.3586,128.2365 · 36.0244,128.2675 · 35.4901,128.5107 · 35.2836,128.5102 · 35.1590,128.7150) | pint de route west van Daegu en Changwon i.p.v. Busan-stad |
| b4 | 1-5 | vijf punten op weg 1 (Kuusalu, NW Rakvere, W Jõhvi, Vaivara, afslag Kulgu) | zie `ree-kuantan-narva.md` §4 (59.4440,25.3533 · 59.4267,26.2455 · 59.4064,27.0591 · 59.4010,28.0131 · 59.3767,28.1541) | houdt de route op weg 1, niet door Sillamäe of Narva-centrum |

Refs b1 ["35","1","30","45"], venster 40 km; refs b4 ["1","E20","94"], venster 40 km, eindToegangPrivaat. Geen nieuwe scan: de geojson's bestaan al.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Korean Metals Plant, Ochang | ASM, sinds 2026-08 Energy Fuels | oxide → NdPr-metaal, NdFeB-legering, Dy/Tb-metaal | 1,3 kt NdFeB-legering/j, naar 3,6 kt/j (kt legering); Q2 2026 ca. 45 t uitgeleverd | [1][2] |
| Neo Narva (Kulgu-park) | Neo Performance Materials | metaal/legering + oxide (Silmet-lijn) → gesinterd NdFeB | 2 kt NdFeB/j fase 1, 5 kt/j daarna; geopend 2025-09-19 | [3][4] |

## 6 · Stoppunt
Bij de fabriekspoort van Neo Narva: de enige in [1] genoemde bestemming ("Neo's magneetfabriek in Estland"); fase E vervalt, geen gedocumenteerde klant erna.

## 7 · Open punten
- **Bestemming alleen via [1].** ASM noemt "Neo's facility in Estonia", geen plaatsnaam en geen leveringsroute; Neo noemt zelf geen KMP-levering [3][4]. Narva is de enige Neo-magneetfabriek in Estland, vandaar "aannemelijk: een bron".
- **19 t NdPr (Magnequench, dec 2024) niet aan Narva toegeschreven:** op [1] geen bestemming (Magnequench Korat in Thailand, Silmet of China zijn alternatieven).
- **Volume is monsterschaal:** 2 kg Tb + 2 kg Dy (jul 2025), geen jaarcijfer; een zending van 4 kg gaat realistisch per koerier/lucht, maar geen bron zegt dat, dus geen luchtbeen. Container via Busan en Muuga is een aanname, evenals Muuga boven Hamburg/Rotterdam + truck.
- **KMP-kopanker onzeker:** straatniveau Gwahaksaneop 4-ro (B/L: Oksan-myeon; ASM/Segye: Ochang-eup), plantgebouw niet gezien.
- **Km:** geen gepubliceerde wegkm voor b1/b4; de ±15%-toets is een indicatie op OSM-afgeleide lengtes. Zeebeen 22.199,0 km is eigen MARNET-proef; de Kaaproute is niet gemodelleerd.
- **Stoppunt Narva en Silmet-vertakking:** of het metaal eerst naar Silmet (Sillamäe) gaat is niet gebronnen en niet getekend.

## 8 · Bronnen
[1] ASM, KMP-geschiedenis: NdPr Magnequench 19 t (dec 2024, eerste 5 t), 2 kg Tb + 2 kg Dy naar Neo's magneetfabriek in Estland (jul 2025), Ochang Foreign Investment Zone. https://asm-au.com/metals/korean-metals-plant/kmp-history/
[2] Investornews, 2026-09: KMP Ochang/Cheongju, 1,3 kt/j NdFeB-legering, 3,6 kt/j gepland, ca. 45 t uitgeleverd Q2 2026, Energy Fuels-eigenaar. https://investornews.com/critical-minerals-rare-earths/rare-earth-metal-and-alloy-capability-outside-of-china-in-september-2026/
[3] Benchmark Minerals, interview Neo-CEO Suleman: Narva geopend 2025-09-19, sample-fase, fase 1 2.000 t, daarna 5.000 t/j; oxide lokaal van Silmet; Lynas als upstream. https://source.benchmarkminerals.com/article/in-conversation-with-neo-performance-materials-ceo-and-president-rahim-suleman
[4] Neo Performance Materials, Estonia: grand opening Narva 2025-09-19, geen leverancierslijst. https://www.neomaterials.com/estonia/
[5] `v2/design/routebrieven/ree-sillamae-narva.md` §3/§4: Kulgu-anker en wegpunten (Invest in Estonia, Neo-fabriek Narva).
[6] Wikipedia, Estonian national road 1: Tallinn–Narva 212 km, onderdeel van E20. https://en.wikipedia.org/wiki/Estonian_national_road_1
[7] `v2/design/routebrieven/ree-cheongju-sanmarcos.md` §3/§4/§9: KMP-anker, Busan-anker, b1-kopie en Busan-aanloop (ImportGenius-B/L KSM Metals, Segye Ilbo 2022-05-12).
[8] `v2/design/routebrieven/ree-kuantan-narva.md` §3/§4/§9 en `ree-sillamae-newark.md`: Muuga-anker, Muuga-stippel 37,5 km, b4-kopie (Wikipedia Muuga Harbour, OSRM 206,3 km).
[9] OSRM demo-router (OSM-afgeleid, indicatie), Cheongju → Busan 279 km (via [7]); hemelsbreed eigen haversine 221,6 km (KMP-anker → Busan-kade).
[10] MARNET `hecht_marnet.py route`, eigen proef 2026-10-31: knoop 5621 → 1970 = 22.199,0 km, 182 edges, 2.313 punten, snaps 0,000, via Suez en Gibraltar.
Satellietblikken: `v2/build-cache/satcheck/sat-ree-ochang-narva-{kmp,busan,muuga,narva}.png` (Esri z15, 2026-10-31).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
`bash v2/tools/bak_stromen.sh ree-ochang-narva` (functie `bak_ree_ochang_narva`) → `v2/data/stroomroute-ree-ochang-narva.json` (137,4 KB, contract versie 2, lonlat, 5 benen, 4 markers, 22.729,4 km). Geen nieuwe scan, geen profiel, geen lucht, geen last mile; zware run 18 s in zwaar-slot2.

| # | modaliteit | km | naad | stippel | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 279,4 | 0 | nee | byte-kopie `ree-cheongju-sanmarcos-weg-ksm-busan.geojson` (nu `ree-ochang-narva-weg-ksm-busan.geojson`) |
| b2a | zee (haven-aanloop Busan) | 10,8 | 0 | ja | byte-kopie `ree-cheongju-sanmarcos-aanloop-busan.geojson` (kade → knoop 5621) |
| b2b | zee (MARNET) | 22.199,0 | 0 | nee | zeeknoop 5621 → 1970, 182 edges, 2.313 punten, snaps 0,000; gelijk aan de proef in §2 |
| b3 | zee (haven-aanloop Muuga) | 37,5 | 0 | ja | `--stippel`-regel uit `bak_ree_kuantan_narva` (rechte lijn knoop 1970 → kade) |
| b4 | truck | 202,7 | 0 | nee | byte-kopie `ree-kuantan-narva-weg-muuga-narva.geojson` (nu `ree-ochang-narva-weg-muuga-narva.geojson`) |

**Markers (4):** ree-ksm-fabriek, ree-busan-kade, ree-muuga-ct, ree-narva-magneetfabriek; alle 0,0 km van hun lijn, alle naden 0,000 km.
**Km-toets:** b1 279,4 tegen OSRM-indicatie 279 (+0,2%; geen gepubliceerde wegkm, hemelsbreed 222 km); b4 202,7 tegen OSRM 206,3 (-1,7%; geen gepubliceerde wegkm, hemelsbreed 180,4 km); b2b gelijk aan MARNET-proef 22.199,0. De ±15%-toets is voor b1 en b4 een indicatie.
**Stippels met reden:** b2a: MARNET reikt niet tot de Busan-kade (10,1 km van knoop 5621, LAR-586), omgekeerde kopie van de aanloop uit ree-cheongju-sanmarcos. b3: Muuga-kade 37,5 km van knoop 1970 (hier reikt het net niet), rechte stippel; `maak_havenaanloop` liep daar eerder vast op de timeout, dus geen tweede poging.
**Knikken:** 50 (36 op b1, 11 op b4, 3 op b2b), 3 omkeringen, 0 terugloop: allemaal erfenis van de gekopieerde wegbenen (spikes in de laatste meters bij de ankers, patroon van de bronstromen); niets gerepareerd. `toets_rechte_benen` meldt alleen de Muuga-stippel (bedoeld).
**Recept:** 3 byte-kopieën in `v2/build-cache/ais/graaf/` met prefix `ree-ochang-narva-`; functievolgorde: been-geojson truck · stippel-geojson zee · been zee · stippel zee · been-geojson truck.
**Lessen:** een volledig uit kopieën opgebouwde keten (alleen het zeebeen is nieuw) bakt in 18 s zonder slotconflict; b3 hergebruiken als `--stippel`-regel is genoeg, een geojson is niet nodig. Let op: een gelijktijdige edit van een andere agent in `bak_stromen.sh` gaf één keer een tijdelijke syntaxfout na de bake (daarna `bash -n` schoon).
