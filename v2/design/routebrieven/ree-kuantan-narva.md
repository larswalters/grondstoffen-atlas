# Routebrief (licht) · Zeldzame aardmetalen · Lynas Gebeng → Port Klang → Muuga → Neo Narva (Estland)

**stroom-id:** `ree-kuantan-narva` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · LAMP Gebeng (Lynas) → Westports → Muuga → Neo Narva (Estland; aannemelijk: Lynas upstream-bron volgens trade-pers, bestemming Silmet of Narva niet gebronnen)
**Keten in één zin:** Lynas-oxide (NdPr) van de LAMP in Gebeng gaat per **truck** (E8/Karak Highway, 336,5 km) naar Westports in Port Klang, per **zeeschip** (MARNET: Malakka, Suez, Gibraltar, Noordzee, Oostzee) naar de Finse Golf, over een stippel-haven-aanloop naar de containerterminal van Muuga en per **truck** over weg 1/E20 naar de Neo-magneetfabriek in het Kulgu-industriepark, Narva. Stoppunt bij de fabriekspoort.
**Welke as van het verhaal:** Maleisië naar Europa, Lynas-oxide in Europa's eerste NdFeB-magneetfabriek. Lynas NdPr-verkoop **7,3 kt per jaar** (FY2026, kt REO) [7]; Narva fase 1A **2 kt NdFeB per jaar**, fase 2 5 kt [3][4]. Het Lynas-aandeel in Narva is niet gepubliceerd; Narva staat per Rare Earth Exchanges (15-09-2026) in commerciële levering [1], per Neo-pagina en Fastmarkets sinds 19-09-2025 geopend [2][4].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** alleen als reserve; beennaam en titel "aannemelijk"; Muuga-anker 59.4915, 24.9675 en letterlijke kopie van de Muuga-stippel (hier in omgekeerde richting: knoop 1970 → kade); truck Muuga → Narva met 5 via-punten (ontwerp: 0-2). Eindpunt blijft Narva zoals het id belooft.

## 1 · Ketenkaart
```
LAMP Gebeng `ree-lamp-gebeng` (hergebruikt anker)
  ──(b1 truck · E8 Pantai Timur → Karak Highway → KL–Klang · 336,5 km, LETTERLIJKE KOPIE ree-kuantan-japan b1)──►
Westports, Port Klang `ree-kuantan-japan-westport-kade` (hergebruikt anker)
  ──(b2 zee · Malakka → Suez → Gibraltar → Noordzee → Oostzee · 17.175,0 km, MARNET, aannemelijk)──► zeeknoop 1970 (59.8, 24.7, Finse Golf)
  ╌╌(b3 zee-stippel · haven-aanloop Muuga · 37,5 km, LETTERLIJKE KOPIE ree-sillamae-newark b2, omgekeerd)╌╌► Muuga-containerterminal `ree-muuga-ct`
  ──(b4 truck · weg 1/E20 Tallinn–Narva mnt · hemelsbreed 180,4 km, OSRM 206,3 km)──► Neo-magneetfabriek Narva `ree-narva-magneetfabriek` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `ree-lamp-gebeng` → `ree-kuantan-japan-westport-kade` | Lebuhraya Pantai Timur (E8) → Karak Highway (E8/E9) → KL–Klang-corridor | 336,5 getekend; hemelsbreed 258 km, geen wegkm [8][11] | KOPIE `ree-kuantan-japan-weg-gebeng-westport.geojson` (bak_ree_kuantan_japan / bak_ree_kuantan_pasadena) | nee |
| b2 | C | zee | `ree-kuantan-japan-westport-kade` → zeeknoop 1970 | Malakka, Rode Zee/Suez, Gibraltar, Kanaal, Noordzee, Oostzee (MARNET kiest) — *aannemelijk: één bron, Lynas upstream-bron* | 17.175,0 (eigen MARNET-meting [12]; snap Westports 2,34 km, knoop 0,0 km) | MARNET | nee; Westports < 5 km, geen aanloop |
| b3 | C | zee | zeeknoop 1970 → `ree-muuga-ct` | haven-aanloop Muuga, over water tussen Viimsi-punt en Prangli | 37,5 (rechte lijn, ree-sillamae-newark b2) | LETTERLIJKE KOPIE van de `--stippel`-regel in `bak_ree_sillamae_newark`, richting omgedraaid | **ja — hier reikt het net niet** (kade 37,5 km van zeeknoop) |
| b4 | D | truck | `ree-muuga-ct` → `ree-narva-magneetfabriek` | Muuga sadama tee (94) → Peterburi tee → weg 1 (E20, Tallinn–Narva mnt) | hemelsbreed 180,4 km, geen wegkm; OSRM 206,3 km [11]; weg 1 zelf 212 km Tallinn–Narva [6] | maak_stroombeen_weg (extract estland) | nee — *aannemelijk: bestemming Narva niet gebronnen* |

Het b4-eindstuk (Vaivara → afslag Kulgu → fabriek) komt overeen met het slot van `ree-sillamae-narva` b1; de E20 tussen Jõhvi en Muuga loopt vrijwel dubbel met `ree-sillamae-newark` b1 (geen letterlijke kopie: andere richting en andere uiteinden).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-lamp-gebeng` | fabriek (start) | Lynas Advanced Materials Plant (LAMP), Gebeng | 4.0034, 103.3775 | hergebruik `ree-kuantan-japan.md` §3 / `ree-mtweld-kuantan.md` | bron-gelegd (in die brief z15: plantcomplex met procesgebouwen en tanks) |
| `ree-kuantan-japan-westport-kade` | overslag truck → zee | Westports Malaysia, Pulau Indah, Port Klang | 2.9498, 101.3076 | hergebruik `ree-kuantan-japan.md` §3 [9] | bron-gelegd (z14 in die brief: kadelijn, containerstapels, tankopslag) |
| `ree-muuga-ct` | overslag zee → truck | Muuga-containerterminal (HHLA TK Estonia), Muuga sadam | 59.4915, 24.9675 | hergebruik `ree-sillamae-newark.md` §3 [5] | bron-gelegd (in die brief z16: portaalkranen en containerstapels op de kade met schip; haven en terminal voor deze lading = aanname) |
| `ree-narva-magneetfabriek` | magneetfabriek (losplek, stoppunt) | Neo Performance Materials, NPM Narva OÜ, Kulgu-tööstuspark | 59.3618, 28.1478 | hergebruik `ree-sillamae-narva.md` §3 [10] | bron-gelegd (in die brief z16: gebouwencluster met opslagterrein aan de doorgaande weg tussen twee moerasmeren; hal niet van buren te onderscheiden) |

Zeeknoop 1970 (59.8000, 24.7000) is een MARNET-knoop, geen anker. Geen last-mile-been: de site ligt aan de weg (het wegbeen eindigt op het anker). Er is niets nieuw gelegd, dus geen nieuwe satellietblik.

## 4 · Via-punten (alleen b4; b1 = kopie van `ree-kuantan-japan.md` §4)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b4 | 1 | weg 1 ten oosten van Tallinn (Kuusalu-streek) | 59.4440, 25.3533 | pint de uitgang van de Tallinn-ring op weg 1 i.p.v. kustwegen (uit `ree-sillamae-newark` §4, OSRM nearest 5 m) |
| b4 | 2 | weg 1 NW van Rakvere | 59.4267, 26.2455 | doorgaande weg langs Rakvere, niet door de stad (OSRM nearest 1 m) |
| b4 | 3 | weg 1 westelijk van Kohtla-Järve/Jõhvi | 59.4064, 27.0591 | houdt de route op weg 1 i.p.v. de binnenwegen (OSRM nearest 0 m) |
| b4 | 4 | weg 1/E20 ter hoogte van Vaivara | 59.4010, 28.0131 | kustcorridor i.p.v. binnenlandse afsnijding; Sillamäe-centrum blijft buiten beeld (uit `ree-sillamae-narva` §4) |
| b4 | 5 | afslag weg 1 → Kulgu-tööstuspark | 59.3767, 28.1541 | afslag zuidwaarts naar het park i.p.v. rechtdoor Narva-centrum in (uit `ree-sillamae-narva` §4) |

Alle punten liggen buiten stadscentra en op weg 1. Het begin Muuga sadama tee (59.4526, 24.9828) uit `ree-sillamae-newark` is bewust NIET gebruikt: OSRM-ketens Muuga → Narva kregen door dat punt ca. 6 km omweg (richtingsgevoelig). OSRM-ketens met meerdere via-punten gaven 231–242 km tegen 206,3 km direct (richtingsgevoelige snaps); de wegscan (ongerichte graaf) moet de lengte bepalen, verwacht ca. 200–210 km. Refs voor het profiel: `["1", "E20", "94"]`; profiel-coördinaten zijn (lon, lat).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LAMP Gebeng | Lynas | Mt Weld-concentraat → NdPr-oxide, Dy, Tb | nameplate 10.500 t NdPr/j; FY2026-verkoop 7.337 t | [7] |
| Muuga-containerterminal | HHLA TK Estonia (Port of Tallinn) | feeder → truck | 267.752 TEU in 2022 | [5] |
| Neo Narva (Kulgu-park) | Neo Performance Materials | REE-oxide (Silmet-lijn + upstream) → gesinterd NdFeB | 2 kt/j fase 1A, 5 kt/j fase 2; commercieel volgens [1], sample volgens oudere bronnen | [1][2][3][4] |

## 6 · Stoppunt
De brief stopt bij de fabriekspoort van Neo Narva: dat is de enige gedocumenteerde afnemer in Europa van het Neo-systeem waarin Lynas als upstream-bron wordt genoemd; of de lading eerst naar Silmet (Sillamäe, 30 km van Narva) gaat is niet gebronnen. Fase D/E (motorfabrikant) vervalt.

## 7 · Open punten
- **Lynas als bron is zwak.** Alleen Benchmark Minerals (Neo-CEO) noemt Lynas onder "a wide variety of global upstream sources" [3]; het REX-artikel noemt Lynas alleen in een waarderingsvergelijking en noemt geen oxideleveranciers [1]; neomaterials.com/estonia en Fastmarkets noemen Lynas niet [2][4]. Geen contract, volume of datum gevonden. Vandaar "aannemelijk" in b2 en de titel.
- **Bestemming Silmet of Narva niet gebronnen.** Benchmark zegt dat Narva zijn oxide lokaal van Silmet krijgt [3]; Lynas-oxide kan dus eerst naar Silmet (Sillamäe, anker in `ree-sillamae-narva`). We tekenen de rit naar Narva zoals het ontwerp vraagt; een vertakking naar Silmet staat niet op de kaart.
- **Haven Muuga en feeder-route zijn aannames**, evenals de Westports-route voor deze lading (zelfde aanname als `ree-kuantan-japan`). Zelfde begin en zeestraat als `ree-kuantan-pasadena`.
- **b1 is niet gebrond als route van deze lading**; geen wegkm gepubliceerd (336,5 km getekend, +16% op de kaartschatting 290).
- **Zeeroute via Suez** is wat MARNET kiest (Gulf of Suez en Gibraltar in het spoor); of schepen via de Kaap varen is niet gemodelleerd.
- **b4 heeft alleen een hemelsbreed getal (180,4 km) en een OSRM-meting (206,3 km)**: de ±15%-toets is een indicatie.
- **Volumestatus Narva loopt uiteen**: sample production (Neo-berichten 2025, brief `ree-sillamae-narva`) tegen commerciële levering (REX, 15-09-2026) [1]; het Lynas-deel van de 2 kt NdFeB per jaar is onbekend.
- **Muuga-aanloop is schematisch**: rechte stippel van 37,5 km, `maak_havenaanloop` liep eerder vast op 300 s (zie `ree-sillamae-newark`).

## 8 · Bronnen
[1] Rare Earth Exchanges, Neo Performance Materials Estonia NdFeB magnets (15-09-2026, deels betaalmuur) — Narva levert gekwalificeerde magneten, fase 1A ca. 2.000 t/j, geen oxideleveranciers genoemd, Lynas alleen in valuatievergelijking. https://rareearthexchanges.com/news/neo-performance-materials-estonia-ndfeb-magnets/
[2] Neo Performance Materials, Estonia — grand opening Narva 19-09-2025, geen tonnages, geen Lynas/Maleisië. https://www.neomaterials.com/estonia/
[3] Benchmark Minerals, interview Neo-CEO Rahim Suleman — "wide variety of global upstream sources, including Lynas"; Narva-oxide lokaal van Silmet; 2.000 t Q2 2026 dan 5.000 t/j (magneten). https://source.benchmarkminerals.com/article/in-conversation-with-neo-performance-materials-ceo-and-president-rahim-suleman
[4] Fastmarkets, Neo adds heavy rare earth line, opens EV motor magnet plant (22-09-2025) — Narva 2.000 t/j NdFeB, ambitie 5.000 t/j; Silmet 2.000 t/j licht REE, ca. 30 km van Narva; geen Lynas. https://www.fastmarkets.com/insights/neo-adds-heavy-rare-earth-line-opens-ev-motor-magnet-plant/
[5] Wikipedia, Muuga Harbour — HHLA-terminal, 267.752 TEU in 2022, 59°29′30″N 24°57′30″E. https://en.wikipedia.org/wiki/Muuga_Harbour
[6] Wikipedia, Estonian national road 1 — Tallinn–Narva 212 km, onderdeel van E20. https://en.wikipedia.org/wiki/Estonian_national_road_1
[7] Lynas Rare Earths (LAMP, Kuantan) en Discovery Alert FY26 (NdPr-verkoop 7.337 t, nameplate 10.500 t), via `ree-kuantan-japan.md` [1][2]. https://lynasrareearths.com/kuantan-malaysia-2/
[8] Time.com, The Sobering Truth About Rare Earths (apr 2026) — truckcorridor Gebeng → Port Klang, via `ree-kuantan-japan.md` [3].
[9] Wikipedia, West Port, Malaysia — Westports, Pulau Indah. https://en.wikipedia.org/wiki/West_Port,_Malaysia
[10] Invest in Estonia, Neo EUR 100M magnet factory in Narva — Kulgu-tööstuspark. https://investinestonia.com/neo/
[11] OSRM (router.project-osrm.org), eigen meting 2026-10-30 — Muuga-anker → Narva-anker 206,3 km; hemelsbreed 180,4 km (haversine).
[12] Eigen MARNET-dry-run (`hecht_marnet.py route`, scratch): Westports → knoop 1970 17.175,0 km, 144 MARNET-edges, 1.790 punten, snap 2,336 / 0,000 km, via Suez en Gibraltar.
[13] Asian Metal, interview Lynas (2017) — afzet aan klanten in Japan, China, Europa, Noord-Amerika (oud, noemt geen Europese koper). https://www.asianmetal.com/metal_cron/2017/index_lunshi_malloch_en.shtml
[14] Briefs `ree-kuantan-japan`, `ree-kuantan-pasadena`, `ree-sillamae-newark`, `ree-sillamae-narva`, `ree-mtweld-kuantan` — ankers, kopie-benen, Muuga-stippel en satellietblikken (v2/build-cache/satcheck/sat-ree-sillamae-newark-*, sat-ree-sillamae-narva-*).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)

Recept: `bash v2/tools/bak_stromen.sh ree-kuantan-narva` (functie `bak_ree_kuantan_narva`; wegprofiel `ree-kuantan-narva-muuga-narva` in `maak_stroombeen_weg.py`) → `v2/data/stroomroute-ree-kuantan-narva.json` (159,9 KB, versie 2, `lonlat`, 8.398 punten, 4 markers). Titel: *Zeldzame aardmetalen · LAMP Gebeng (Lynas) → Westports → Muuga → Neo Narva (Estland; aannemelijk: …)*; het eindpunt klopt met het id.

| # | modaliteit | km | naad naar vorig been | opmerking |
|---|---|---|---|---|
| b1 | truck | 336,5 | — | LETTERLIJKE KOPIE `ree-kuantan-japan-weg-gebeng-westport.geojson` (4.673 punten); geen gepubliceerde wegkm (hemelsbreed 258), dus geen ±15%-norm |
| b2 | zee | 17.175,0 | 2,34 km (Westports-snap op zeeknoop 5375, < 5 km) | MARNET Westports → zeeknoop 1970 (59.8000, 24.7000), via Suez en Gibraltar; 1.790 punten; km gelijk aan de dry-run in de brief |
| b3 | zee, STIPPEL | 37,5 | 0 | haven-aanloop Muuga, rechte lijn knoop 1970 → kade; omgekeerde kopie van de `--stippel`-regel in `bak_ree_sillamae_newark` |
| b4 | truck | 202,7 | 0 | wegscan `estland`, 1.933 punten, 5 via-punten op weg 1 |

Totaal 17.751,7 km, 4 markers (alle 0,0 km van hun lijn), grootste naad 2,34 km.

**Wegbeen b4.** `wegscan_puur.py`, extract `estland`, refs `1`, `E20`, `94`, `vensterKm` 40, `eindToegangPrivaat`; alle via-snaps 0,00-0,05 km. Deelstukken: Muuga → Kuusalu 26,3 · → NW Rakvere 51,5 · → W Jõhvi 53,5 · → Vaivara 59,3 · → afslag Kulgu 10,1 · → fabriek 1,8 km. Lengtetoets 202,6 km tegen OSRM-indicatie 206 = -1,6% (hemelsbreed 180,4; geen wegkm gepubliceerd, dus de toets is een indicatie; weg 1 Tallinn-Narva is 212 km volgens Wikipedia). Eerste mijl 1,81 km en laatste mijl 1,54 km over kleine klassen: geen last-mile-been. Geen omweg: het beginpunt Muuga sadama tee (59.4526, 24.9828) is niet gebruikt. Toets_knikken: 11 knikken op b4, 0 omkeringen, 0 terugloop (spikes bij de terminal en de Kulgu-afslag zijn terreinwegen).

**Toelichting stippel (b3).** Muuga-kade ligt 37,5 km van zeeknoop 1970: hier reikt het net niet. Zoals in `ree-sillamae-newark` is `maak_havenaanloop.py` niet opnieuw geprobeerd (liep eerder vast op 300 s); schematische rechte lijn (37,452 km, 2 punten) over water tussen Viimsi-punt en Prangli. Dit is de enige stippel; `toets_rechte_benen` meldt alleen dit been.

**Niet getekend / aannames.** Geen lucht, leiding, spoor, last mile of fase D/E. Lynas als bron, de Westports-route, Muuga als haven en Narva (boven Silmet) als bestemming zijn aannames (§7); "aannemelijk" staat in de beennamen en de titel. Silmet-vertakking staat niet op de kaart.

**Lessen.** (1) Twee kopieën van bestaande benen (b1, de Muuga-stippel) maakten dit een korte bake: één wegscan van 26 s op de Estland-extract. (2) Een tussentijdse edit van een andere agent in `bak_stromen.sh` (kolen-curragh-gladstone, een regel `n.` in een commentaarblok na een regelvervolg) geeft aan het eind van de bake `command not found`; het json was al geschreven. (3) De ongerichte wegscan gaf 202,6 km waar OSRM-ketens met dezelfde via-punten 231-242 km gaven (richtingsgevoelige snaps).
