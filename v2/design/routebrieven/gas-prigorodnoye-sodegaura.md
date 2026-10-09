# Routebrief (licht) · gas — Prigorodnoje (Sachalin-2, Rusland) → Sodegaura (Tokiobaai, Japan)

**stroom-id:** `gas-prigorodnoye-sodegaura` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** Het Sachalin-2-LNG-complex bij Prigorodnoje (Aniva-baai, Zuid-Sachalin) laadt LNG via een
805 m-jetty op tankers, die over MARNET via de Okhotskzee en de Kurilen-passage langs de Pacifische kust van
Hokkaido en Honshu naar de Sodegaura-terminal in Tokiobaai varen (Tokyo Gas/TEPCO-JERA-terminal).
**Welke as van het verhaal:** *Russisch LNG dat Japan bewust blijft afnemen onder sancties* — 10,3 Mt LNG in 2025
(= ~14,0 bcm/j) [5], waarvan 58% naar Japan [6]; Sachalin-2 is voor Japan de enige Russische LNG-bron met een
sanctie-uitzondering, en Sodegaura is er sinds de allereerste lading (maart 2009) de gedocumenteerde ontvanger [2][3].

## 1 · Ketenkaart
```
Sachalin-2 LNG-plant Prigorodnoje `gas-prigorodnoye-plant` (Sakhalin Energy)
  ──(b1 leiding · jetty-leiding plant → pier · 0,8 km, stippel)──►
LNG-jetty, kop `gas-prigorodnoye-kade` (overslag leiding → tanker)
  ──(b2 zee · haven-aanloop kade → zeeknoop 5683 · ~21,5 km, stippel over water)──►
zeeknoop Aniva-baai (46.4303, 142.8992)
  ──(b3 zee · Aniva-baai → Okhotskzee → Kurilen-passage → Pacifische kust Hokkaido/Honshu · ~1.762 km, MARNET)──►
Sodegaura LNG-terminal `gas-sodegaura-term` (Tokiobaai)
  ──(b4 leiding · terreinleiding, letterlijke kopie gas-raslaffan-chiba b4 · 0,4 km, stippel)──►
stoppunt: invoedingspunt Kanto-gasnet/centrale
```
Fase A (offshore Piltun/Lunskoje + ~800 km onshore noord-zuid) vervalt (haalbaarheidstoets, bindend).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | plant → jetty-kop | LNG-leiding op het onderdek van de jetty | ~0,8 (hemelsbreed gemeten op z16; jetty 805 m [1]) | stippel (rechte lijn) | ja — jetty-leiding niet als OSM-way gekarteerd/geverifieerd; eigen verbinding zonder net |
| b2 | B | zee | jetty-kop → zeeknoop 5683 | haven-aanloop Aniva-baai | 21,5 (gemeten, 36 punten; geojson staat klaar) | maak_havenaanloop | ja — MARNET reikt niet (kade 21,1 km hemelsbreed van de knoop) |
| b3 | B | zee | zeeknoop 5683 → Sodegaura-kade | Okhotskzee → Kurilen-passage → Pacifische kust (router, niet La Pérouse/Tsugaru) | 1.762,2 (router; eigen schatting ontwerp 1.900–2.300, geen bron) | MARNET | nee |
| b4 | C | leiding | Sodegaura-kade → centrale | terreinleiding, **kopie gas-raslaffan-chiba b4** | 0,4 | stippel (kopie) | ja — last mile op eigen terrein, geen net op deze korrel |

Sodegaura-kade ligt 1,6 km van zeeknoop 9067 (35.4819, 139.9720), onder de 5 km-drempel: de zeelijn eindigt direct op
de kade, **geen Sodegaura-aanloop** (de ontwerp-b3 "kopie raslaffan-chiba b2" bestond niet: dat is de 41,6 km Ras Laffan-aanloop).
Aannemelijk-vlag: een bron noemt de ontvangende **terminal** (Sodegaura) voor de eerste lading [2][3]; dat de lijn nu nog
dezelfde terminal volgt is één bron → "aannemelijk: één bron" staat in de titel/beennaam, niet in de lijnstijl.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-prigorodnoye-plant` | liquefactie-site | Sachalin-2 LNG-plant, Prigorodnoje | 46.6275, 142.9028 | [7][12] | bron-gelegd (z16 gezien: omheind procescomplex met twee witte LNG-tanks, twee treinen en fakkelterrein; punt ligt op het terrein bij de westelijke tanks. v1 `gas.js` heeft lon 143.40 = >40 km fout) |
| `gas-prigorodnoye-kade` | overslag leiding → tanker | LNG-jetty Prigorodnoje, kop | 46.6205, 142.8995 | [10] | bron-gelegd (z16 gezien: 805 m-jetty vanaf de plant het water in, LNG-tanker afgemeerd aan de kop; punt ligt aan de tanker-zijde van de kop, ~0,2 km ten noorden van het platform) |
| `gas-sodegaura-term` | losplek zee → leiding | Sodegaura LNG-terminal (Tokyo Gas/TEPCO-JERA), Tokiobaai | 35.4675, 139.9700 | [2][3][11] | bron-gelegd (**hergebruikt letterlijk** uit `gas-raslaffan-chiba.md`: z15 tankenpark + twee steigers). Terminal nu ook door een bron als bestemming van Sachalin-LNG genoemd |

## 4 · Via-punten
Geen — geen landbeen met corridorkeuze; b1/b4 zijn korte stippels, b2/b3 zeebenen (aanloop-tool resp. MARNET).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sachalin-2 LNG-plant, Prigorodnoje | Sakhalin Energy LLC (Gazprom 77,5% / Mitsui 12,5% / Mitsubishi 10% [7]) | gas (Lunskoje/Piltun, via Trans-Sachalin) → LNG | 2 treinen à 4,8 Mt = 9,6 Mtpa ontwerp [1][7]; productie 10,3 Mt in 2025 ≈ **14,0 bcm/j** (1 Mt LNG ≈ 1,36 bcm) [5] | [1][5][7] |
| Sodegaura LNG-terminal + centrale | Tokyo Gas / TEPCO-JERA | LNG → hervergast → Kanto-net/centrale | niet in deze brief gebrond (§7) | [2][11] |

## 6 · Stoppunt
De brief stopt bij het invoedingspunt van Sodegaura: Tokyo Gas (1,1 Mtpa-contract [1]) en TEPCO namen de eerste lading in 2009 [2][3],
maar geen bron legt de huidige cargo's per terminal vast. Fase D/E vervalt: geen bron noemt een fabriek/afnemer stroomafwaarts.

## 7 · Open punten
- **Sanctie-actualiteit (2026-10):** US-licentie GL 55F (tot 18-12-2026) dekt de Sachalin-2-**ruwe-olie/bijproducten** richting Japan, niet de LNG zelf [8]; de LNG-lading naar Japan/Zuid-Korea valt onder een UK-vergunning tot 31-3-2028 (contracten van vóór 17-6-2025) [8]. Dit verschilt van de toets-tekst ("GL 55F verlengt de Sachalin-2-uitzondering"). Het verhaal kan snel wisselen.
- **Capaciteit: bronkeuze.** Sitelaag noemt 11,6 Mtpa/15,8 bcm/j (niet gebrond); Wikipedia en GEM: 9,6 Mtpa ontwerp [1][7]; productie 2025 10,3 Mt [5]. Brief gebruikt 10,3 Mt (14,0 bcm/j).
- **Japan-aandeel 58% (2025)** komt uit een WebSearch-samenvatting van [6] (operatorcijfer); de pagina gaf bij fetch HTTP 403 — niet los geverifieerd. Eind 2020 was het ~51,6% (Offshore Energy, ontwerp).
- **Per-terminal-volume niet gebrond**: alleen Tokyo Gas-contract (1,1 Mtpa) en de eerste lading; Sodegaura blijft voor de huidige stroom "aannemelijk".
- **Jetty-leiding (b1)** niet in OSM geverifieerd (Overpass onbereikbaar op de bouwdag); stippel is de eerlijke vorm.
- **Zeebeen is een eigen router-uitkomst** (geen gepubliceerde route-lengte): 1.762 km via de Pacifische zijde; schepen kunnen ook via La Pérouse/Tsugaru varen. Noteer dat in de beennaam.
- Kade-anker ligt in het water naast de aangemeerde tanker, ~0,2 km van het jetty-platform; geen meters-precisie (licht).

## 8 · Bronnen
[1] Wikipedia, "Sakhalin-II" — LNG-plant Prigorodnoje (2×4,8 Mtpa, 9,6 Mtpa; jetty 805 m; eigenaren; Tokyo Gas 1,1 Mtpa, Toho Gas 0,5, Tohoku 0,42 e.a. contracten). https://en.wikipedia.org/wiki/Sakhalin-II
[2] NS Energy, 1-4-2009 — eerste Russische LNG-lading, Energy Frontier, Prigorodnoye → Sodegaura terminal, Tokiobaai, 145.000 m³, Tokyo Gas + Tokyo Electric. https://www.nsenergybusiness.com/news/newssakhalin_energy_dispatches_first_lng_consignment_to_japan_010409/
[3] Offshore magazine, 31-3-2009 — idem (vertrek 29 maart, bestemming Sodegaura). https://www.offshore-mag.com/production/article/16786681/first-lng-cargo-loaded-from-sakhalin-ii-plant
[4] LNG Industry, 26-8-2015 — 1000e lading, Tokyo Electric/Tokyo Gas; 72% van de Sachalin-LNG sinds 2009 naar Japan. https://www.lngindustry.com/lng-shipping/26082015/Sakhalin-Energy-hits-LNG-cargo-milestone-1197
[5] Interfax, 11-3-2026 — LNG-productie Sachalin-2 10,3 Mt in 2025 (+1%). https://interfax.com/newsroom/top-stories/116553/
[6] Gas Processing News, apr 2026, "Japan got bulk of Russian LNG from Sakhalin-2 in 2025" — Japan 58%, China 23,9%, Zuid-Korea 17,5% (via WebSearch-samenvatting; fetch 403). https://gasprocessingnews.com/news/2026/04/japan-got-bulk-of-russian-lng-from-sakhalin-2-in-2025/
[7] GEM.wiki, "Sakhalin II LNG Terminal" — 2 treinen operating 4,8 Mtpa, coördinaat 46.6288/142.9112, eigenaren. https://www.gem.wiki/Sakhalin_II_LNG_Terminal
[8] OFAC GL 55F (tot 18-12-2026, olie/bijproducten) en UK-LNG-vergunning tot 31-3-2028 — uit WebSearch-samenvatting (qcintel/Thompson Hine/energyintel), niet los gefetcht. https://www.qcintel.com/article/us-extends-japan-s-waiver-for-russian-oil-from-sakhalin-2-43213.html
[9] PortNews, 2009 — tweede lading (Cygnus Passage) naar het gezamenlijk geëxploiteerde Sodegaura (uit zoek-samenvatting; fetch ECONNRESET). https://en.portnews.ru/news/15786
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14/z16) — `sat-gas-prigorodnoye-sodegaura-overzicht.png`, `…-pier.png`, `…-plant.png`.
[11] `v2/design/routebrieven/gas-raslaffan-chiba.md` — anker `gas-sodegaura-term`, b4-stippel (§2/§9), Sodegaura zeeknoop 9067 op 1,6 km.
[12] `v2/design/gas-sitelaag.json` — site `w-sakhalin2` (46.6275/142.9028, status aannemelijk → hier bron-gelegd); v1 `data/gas.js` r.156 (lon 143.40, fout).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
`bash v2/tools/bak_stromen.sh gas-prigorodnoye-sodegaura` → `v2/data/stroomroute-gas-prigorodnoye-sodegaura.json`, 5,7 KB, versie 2, lonlat, modaliteiten {leiding, zee}, 4 benen, 229 punten, **1.784,9 km**, 3 markers.

| # | modaliteit | km | punten | stippel | naad naar vorig been | noot |
|---|---|---|---|---|---|---|
| b1 | leiding | 0,818 | 2 | ja | - | plant -> jetty-kop, rechte lijn (805 m jetty, brief 0,8) |
| b2 | zee | 21,5 | 36 | ja | 0,000 | haven-aanloop Prigorodnoje, vooraf gebakken geojson (niet opnieuw gedraaid), 1,42 km over land aan de kust = korrel 1:10M |
| b3 | zee | 1.762,2 | 189 | nee | 0,000 | MARNET knoop 5683 -> Sodegaura, snap 0,000 / 1,611 km, 19 MARNET-edges, exact de brief (1.762,2 / 189) |
| b4 | leiding | 0,389 | 2 | ja | 1,611 | letterlijke kopie gas-raslaffan-chiba b4 (zelfde twee coordinaten) |

**Recept:** `bak_gas_prigorodnoye_sodegaura()` in `bak_stromen.sh`: `--stippel leiding` + `--stippel-geojson` aanloop + `--been zee` (zeeknoop 5683 -> Sodegaura) + `--stippel leiding` (kopie). Geen profiel, geen extract, geen weg/spoor/lucht, geen slot behalve het zware slot voor de bake (18 s).

**Toelichting per stippel/aanloop/leiding:**
- b1 stippel: de jetty-leiding is niet in OSM geverifieerd (Overpass onbereikbaar op de bouwdag); eigen verbinding zonder net, eerlijke vorm.
- b2 aanloop: de kade ligt 21,1 km van MARNET-zeeknoop 5683 (boven de 5 km-drempel), dus een haven-aanloop; stippel = hier reikt het net niet.
- b4 stippel: terreinleiding op het Sodegaura-terrein, geen net op deze korrel; kopie, niet opnieuw getoetst.
- Naad 1,611 km voor b4: het zeebeen eindigt op de MARNET-snap bij Sodegaura (zeeknoop 9067 op 1,6 km, onder de 5 km-drempel, zelfde patroon als gas-raslaffan-chiba) en niet op de kade zelf; blijft staan als procesgat, geen Sodegaura-aanloop. Dit is de enige naad boven 0,5 km en blijft onder 5 km.

**Toets (handleiding 5):** naden 0,000 / 0,000 / 0,000 / 1,611 km (geen naad > 5 km). Markers alle drie op 0,0 km van de lijn. `toets_knikken.py`: 7 knikken >= 60 graden op de MARNET-kust (Kurilen-passage en Tokiobaai, krappe bochten van 64-88 graden), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom komt naar voren (de stippels zijn korter dan 5 km of een gekromde aanloop). Er is geen wegbeen, dus geen wegkm-toets; het zeebeen heeft geen gepubliceerde lengte (router-uitkomst).

**Afwijkingen van het ontwerp:** geen; stroom-id en eindpunt (Sodegaura) kloppen.

**Lessen:** (1) een vooraf gebakken `--stippel-geojson` wordt letterlijk overgenomen, richting kade -> zeeknoop klopt hier. (2) Een brief met alleen zee en korte stippels bakt in 18 s zonder wegscan. (3) Open punten uit 7 blijven open: GL 55F/UK-vergunning, Japan-aandeel 58%, per-terminal-volume, Pacifische tegenover La Perouse/Tsugaru, capaciteit sitelaag 11,6 Mtpa niet gebrond.
