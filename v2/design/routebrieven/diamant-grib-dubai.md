# Routebrief (licht) · diamant — Grib-mijn → Talagi (ARH) → Dubai (DMCC) (Rusland → VAE)

**stroom-id:** `diamant-grib-dubai` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Ruwe diamant uit de Grib-mijn (AGD Diamonds, Arkhangelsk oblast; Lukoil verkocht de mijn in 2017) gaat per truck over secondary-weg, 11K-723 en M-8 naar Talagi Airport (ARH), vliegt als vrachtvlucht (grootcirkel) naar het DXB-vrachtcomplex en gaat per truck naar DMCC / Dubai Diamond Exchange (Almas Tower, JLT); aannemelijk: één bron voor Dubai-veilingen (2022), geen bron voor mijn → luchthaven of voor de vlucht.
**Welke as van het verhaal:** *De niet-Alrosa-diamant van Arkhangelsk na de verschuiving van Antwerpen naar Dubai.* Volume **4,2 Mct in 2025** (AGD Diamonds, Russisch persbericht via www1.ru [8]); vermelde capaciteit 3,62 Mct/j [1]; 4,4 Mct verwacht voor 2017 [3], 4,5 Mct in 2016 [5]; sitelaag `w-grib` 3,2 Mct staat op een verkeerde plek (65.0333, 43.85): centraal corrigeren. Aandeel via Dubai niet gebrond. Waarde per karaat niet gevonden in de gelezen bronnen. Eenheid Mct/j.

## BINDENDE aanpassing (haalbaarheidstoets)
Lukoil is niet de eigenaar (verkocht 2017, 1,45 mld USD [5]); sancties: OFAC op AGD Diamonds en Grib Diamonds 14-9-2023 [4]. Dubai alleen gebrond tot sept 2022 [2]. b1 eigen profiel, eindigt op de laatste openbare weg (M-8 bij Talagi); b1b letterlijke kopie Lomonosov-airside-stippel; b2 een vlucht ARH → DXB (aannemelijk); b3 letterlijke kopie `diamant-mbujimayi-dubai` b4. Overlap met Lomonosov b1 melden (§7).

## 1 · Ketenkaart
```
Grib-mijn (AGD Diamonds) `dia-grib-mijn` ──(b1 truck · mijnweg → secondary/tertiary → 11K-723 → M-8 · hemelsbreed 107 km, geen wegkm; gemeten 132,5)──►
laatste openbare weg M-8 bij Talagi ──(b1b stippel · airside last mile · 0,38 km, kopie Lomonosov)──►
Talagi Airport (ARH), vrachtplatform `dia-arh-vrachtplatform` ──(b2 lucht · vlucht ARH → DXB, grootcirkel, aannemelijk · 4.499,3 km)──►
DXB Cargo Village `dia-dxb-vracht` ──(b3 truck · letterlijke kopie diamant-mbujimayi-dubai b4 · 31,2 km)──►
DMCC / Almas Tower, JLT `dia-dmcc-almas` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Grib-mijn → M-8 bij Talagi | mijnweg → ongenummerde secondary/tertiary → 11K-723 → 11PK-744 → М-8 [9] | hemelsbreed 107 km, geen wegkm; gemeten 132,0 (+0,5 km aanloop) is indicatie; Barents Observer 2016: mijn ca 115 km ONO van Arkhangelsk (geen wegkm) [6] | maak_stroombeen_weg (profiel `diamant-grib-dubai-mijn-arh`, rusland-noordwest) | nee |
| b1b | A | truck | M-8-vertex → ARH-vrachtplatform | airside, geen wegpad | 0,38 (hemelsbreed, kopie `diamant-lomonosov-moskou` b1b) | `--stippel` | **ja** — airside/privéterrein zonder aansluiting op het openbare net |
| b2 | B | lucht | ARH → DXB | vlucht ARH → DXB (vrachtvlucht, grootcirkel; aannemelijk: geen bron voor de vlucht, geen tussenlanding) | 4.499,3 (berekend) | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | DXB-vrachtterminal → DMCC / Almas Tower | Airport Road → Sheikh Zayed Road / Al Ittihad Road | 31,2 (gebakken; geen gepubliceerde wegkm) | LETTERLIJKE KOPIE `diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson` | nee |

Fase D en E vervallen (geen bron voor een slijper of fabriek na Dubai).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-grib-mijn` | mijn / laadplek | Grib-pijp, open pit (AGD Diamonds) | 65.5078, 41.4226 | [1][9][10] | bron-gelegd (z15 gezien: ronde terrasvormige open pit van ca 1,5 km, het kruis ligt in de blauwgroene pitbodem; Wikipedia 65.5075, 41.4228 ligt 0,03 km ernaast) |
| `dia-arh-vrachtplatform` | vrachtplatform / vertrek lucht | Talagi Airport (ARH), platform | 64.5970, 40.7090 | **hergebruikt** `diamant-lomonosov-moskou.md` [11] | **onzeker** (z15 opnieuw gezien: verhard platform met ca 10 toestellen en terminal; apart vrachtgebouw niet te onderscheiden) [12] |
| `dia-dxb-vracht` | vrachtterminal / aankomst lucht | DXB Cargo Village, Al Garhoud | 25.2574524, 55.3405972 | **hergebruikt** `diamant-udachny-dubai.md` [13] | bron-gelegd (daar z14–15: loodsenrij en apron) |
| `dia-dmcc-almas` | handelshub / eindpunt | DMCC / Dubai Diamond Exchange, Almas Tower, JLT | 25.0689, 55.1412 | **hergebruikt** [13] | aannemelijk (één bron voor Dubai-veilingen [2]; toren daar op z15 gezien, 0,05 km van de lijn) |

## 4 · Via-punten (b1, reisvolgorde, lat, lon, vertices OP de doorgaande weg, snap ≤ 0,01 km [9])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | tertiary/secondary Grib → Arkhangelsk, km 30 | 65.3172, 41.1838 | houdt de route op de doorgaande weg van de GOK i.p.v. een zijtak |
| b1 | 2 | secondary, km 50 (aansluiting corridor Lomonosov) | 65.1479, 41.1394 | vanaf hier dezelfde secondary als Lomonosov b1 |
| b1 | 3 | secondary, midden (hergebruik Lomonosov-via) | 64.9112, 41.0312 | zelfde punt als `diamant-lomonosov-moskou` |
| b1 | 4 | begin 11K-723 (hergebruik) | 64.7159, 40.7631 | overgang naar de genummerde regionale weg vóór de stad |
| b1 | 5 | 11PK-744 × M-8 (hergebruik) | 64.6020, 40.6292 | knoop waar de rondweg de M-8 bereikt; stadscentrum blijft ongemoeid |
| b1 | eind | M-8 Talazhskoe shosse bij Talagi | 64.5951, 40.7024 | laatste openbare weg (b1b-stippel sluit af) |

Segmenten (km, [9]): mijn → 1 30,1 · → 2 20,2 · → 3 31,0 · → 4 32,7 · → 5 14,4 · → eind 3,6 (som 132,0; plus 0,5 km pit-stub). Zonder `corridorKlassen: tertiary` vindt de weg-tool geen pad: ca 36 km staartstuk is highway=tertiary zonder naam of ref.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Grib-GOK (V. Grib-erts verwerking) | AGD Diamonds (Grib Diamonds, Antwerpen, verkoop) | erts → ruwe diamant | 3,62 Mct/j capaciteit; 4,2 Mct gedolven in 2025 | [1][7][8] |
| Grib Diamonds-veilingen | Grib Diamonds (Belgisch, AGD) | ruw → veiling (10 reguliere + 2 speciale per jaar, 2017; sinds 2022 meerdere in Dubai) | niet gevonden | [2][3] |

## 6 · Stoppunt
De brief stopt bij DMCC/Almas Tower: het enige gebronde afzetadres van Grib-ruw buiten Antwerpen is Dubai ("several auctions this year", 2022 [2]); geen bron noemt een vervolgafnemer, dus fase D en E vervallen.

## 7 · Open punten
- **Geen bron voor het vervoer mijn → ARH noch voor de vlucht ARH → DXB.** Het been is aannemelijk; ARH is de enige luchthaven op bereik, een airstrip bij de mijn is niet gevonden (OSM-scan haalbaarheidstoets: wel helipads op 1,4–1,5 km). De werkelijke route kan via Moskou (SVO) lopen, of per weg of trein naar Arkhangelsk met sortering ter plaatse.
- **Dubai dun gebrond:** alleen Rapaport 21-9-2022 noemt Dubai-veilingen (traditioneel Antwerpen; Grib Diamonds is Belgisch) [2]; Rapaport 2017 noemt 95% export naar Antwerpen en 5% in Rusland [3]. Na OFAC 2023 geen bron over Dubai [4]; DMCC als adres is aannemelijk, niet gebrond.
- **OVERLAP met `diamant-lomonosov-moskou` b1:** ca 86 van 132 km (65%) van het wegbeen is dezelfde OSM-corridor vanaf km 45; b1b en b3 zijn kopieën; alleen mijnanker, ca 45 km staartstuk en de vlucht zijn nieuw.
- **Wegkm niet gebrond:** alleen hemelsbreed 107 km; gemeten 132,0 km is een indicatie (de ±15%-toets geldt niet als norm). Een Lukoil-persbericht noemt 130 km van de stad Arkhangelsk (via haalbaarheidstoets, zelf niet gelezen; geen wegkm naar Talagi).
- **ARH-vrachtplatform onzeker**; airside-stippel schematisch.
- **Mijn draait** (4,2 Mct in 2025, 228,62 ct-steen 13-2-2026 [7][8]); geen stilstandsbericht. Sancties: OFAC 14-9-2023 op AGD en Grib Diamonds [4]; Lukoil is niet de eigenaar. Status Dubai-veilingen na de sancties niet bevestigd.
- **Sitelaag `w-grib`:** 65.0333, 43.85 en 3,2 Mct kloppen niet (pit 65.5078, 41.4226; 4,2 Mct in 2025): centraal corrigeren.
- Eigenaar in 2017 werd Otkritie Holding genoemd [3], de Barents Observer noemt Open Holding [5], Rapaport 2022 AGD Diamonds [2]: dezelfde keten van eigenaren, naam wisselt per bron.

## 8 · Bronnen
[1] en.wikipedia — "Grib diamond mine": 65.5075/41.4228, reserves 98,5 Mct, capaciteit 3,62 Mct/j. https://en.wikipedia.org/wiki/Grib_diamond_mine
[2] Rapaport, 21-9-2022 — "Grib Cancels Auction Amid Payment Block": AGD Diamonds kocht Grib in 2017 van Lukoil (1,45 mld USD), Grib Diamonds (Belgisch) verkoopt, meerdere veilingen in Dubai in 2022 (traditioneel Antwerpen), correspondentbank blokkeerde betalingen. https://rapaport.com/news/grib-cancels-auction-amid-payment-block/
[3] Rapaport, 2017 — "Grib Mine Projects Higher Sales in 2017": 4,4 Mct verwacht (3,8 in 2016), Otkritie Holdings kocht van Lukoil, 10 reguliere + 2 speciale veilingen, ca 5% in Rusland, rest naar Antwerpen. https://rapaport.com/news/grib-mine-projects-higher-sales-in-2017/
[4] JCK, 15-9-2023 — "U.S. Treasury Sanctions Grib": OFAC-sancties op AGD Diamonds (14-9-2023), Grib ca 10% van de Russische diamantproductie. https://www.jckonline.com/editorial-article/u-s-treasury-sanctions-grib/
[5] The Barents Observer, 12-2016 — "Lukoil changes Arkhangelsk diamonds for cash": Lukoil verkoopt Arkhangelskgeoldobycha aan Open Holding voor 1,45 mld USD, Grib 4,5 Mct in 2016. https://thebarentsobserver.com/en/industry-and-energy/2016/12/lukoil-changes-arkhangelsk-diamonds-cash
[6] The Barents Observer — mijn ca 115 km ONO van Arkhangelsk, < 50 km van Lomonosov. https://thebarentsobserver.com/en/node/24966
[7] Interfax, 20-2-2026 — 228,62-carat diamant bij Grib, Mezen-district, AGD Diamonds. https://interfax.com/newsroom/top-stories/116273/
[8] www1.ru, 21-2-2026 — AGD Diamonds produceerde 4,2 Mct in 2025, Grib-GOK. https://www1.ru/news/2026/02/21/unikalnyi-almaz-iuvelirnogo-kacestva-vesom-228-karat-dobyli-v-arxangelskoi-oblasti.html
[9] OSM (ODbL), Geofabrik `rusland-noordwest`, eigen PBF-scan (`maak_stroombeen_weg.py`, profiel `diamant-grib-dubai-mijn-arh`): 132,0 km, 132,5 km getekende lijn.
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-diamant-grib-dubai-grib-mijn.png`.
[11] `v2/design/routebrieven/diamant-lomonosov-moskou.md` (ankers `dia-arh-vrachtplatform`, via-punten, b1b-stippel).
[12] Esri World Imagery (z15): `v2/build-cache/satcheck/sat-diamant-grib-dubai-arh-platform.png`.
[13] `v2/design/routebrieven/diamant-udachny-dubai.md` en `diamant-mbujimayi-dubai.md` (ankers DXB/DMCC, b3-geojson).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Bestand:** `v2/data/stroomroute-diamant-grib-dubai.json` (36,8 KB, versie 2, lonlat), 4 benen, 4.663,4 km, 1.824 punten, 4 markers. Functie `bak_diamant_grib_dubai()` in `v2/tools/bak_stromen.sh`; profiel `diamant-grib-dubai-mijn-arh` in `maak_stroombeen_weg.py` (wegscan_puur, rusland-noordwest).

| # | modaliteit | km | punten | opmerking |
|---|---|---|---|---|
| b1 | truck | 132,5 | 1.235 | mijn tot M-8 bij Talagi; geen gepubliceerde wegkm (hemelsbreed 107), indicatie, geen +-15%-norm |
| b1b | truck, stippel | 0,38 | 2 | ARH-vrachtplatform last mile, airside zonder wegpad (letterlijk als Lomonosov) |
| b2 | lucht | 4.499,3 | 181 | grootcirkel ARH naar DXB, doorgetrokken, aannemelijk |
| b3 | truck | 31,2 | 406 | letterlijke kopie `diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson` |

**Toets:** naden 0,00 km overal (max 0,00); markers 0,0 / 0,0 / 0,0 / 0,018 km van de lijn; toets_knikken 0 omkeringen, 0 terugloop (b1: spikes bij 64.6020,40.6292 en 65.2493,41.1216 zijn OSM-bochten/via-knoop, geen keerpunt); toets_rechte_benen geen treffer voor deze stroom.

**Recept:** wegscan_puur.py --profiel diamant-grib-dubai-mijn-arh; maak_luchtbeen.py ARH-vrachtplatform naar DXB Cargo Village; hecht_marnet.py route met drie `--been-geojson`, een `--stippel` en vier `--marker` (functie in bak_stromen.sh).

**Toelichting:** stippel = alleen b1b (airside, geen net). De vlucht is doorgetrokken: aannemelijk, geen bron voor mijn naar ARH of voor ARH naar DXB (kan via Moskou lopen); dat staat in de beennaam. Geen zee, haven-aanloop, leiding of spoor. Overlap 65% met `diamant-lomonosov-moskou` b1 (eigen profiel, geen kopie). Dubai alleen gebrond via Rapaport 2022.

**Lessen / voor centraal:** sitelaag `w-grib` staat op 65.0333,43.85 met 3,2 Mct: corrigeren naar 65.5078,41.4226 en 4,2 Mct (ca 140 km verschil). Registerlabel Grib-mijn → Dubai (DMCC). Geen afwijking van het ontwerp: id en eindpunt (DMCC) komen overeen.
