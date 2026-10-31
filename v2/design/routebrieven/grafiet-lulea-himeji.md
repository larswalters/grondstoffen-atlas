# Routebrief (licht) · Grafiet · Luleå → Zee (Suez) → Himeji (Japan)

**stroom-id:** `grafiet-lulea-himeji` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) ·
**status:** gebakken
**Keten in één zin:** Talnode-C-anodemateriaal (natuurlijk grafiet, gecoat) van Talga's geplande Talnode-fabriek op
Hertsöfältet in Luleå per **zeeschip** door de Botnische Golf, Öresund, Kanaal, Gibraltar, Suez, Bab-el-Mandeb, Malakka en
de Seto-binnenzee naar Dainen Materials in Himeji (Shikama, Hyogo), Japan. Eén zeebeen, geen last-mile; stoppunt Dainen.
**Welke as van het verhaal:** de eerste Japanse as van Talga: Zweedse anode naar een Japanse trader/anodepartij die aan
Japanse batterijklanten levert (Baltische/Suez-corridor). Volume: tot **2 kt/j** Talnode-C gereserveerd (5 jaar, start
verwacht eind 2027) [1][2], peiljaar 2026-10; **vandaag 0 kt**, fabriek niet gebouwd.

## 1 · Ketenkaart
```
Talnode-kavel Hertsöfältet, Luleå `gr-lulea-talnode` ──(naad 3,8 km, geen last-mile)──► MARNET-zeeknoop 8829
  ──(b1 zee · Botnische Golf → Öresund → Kanaal → Gibraltar → Suez → Bab-el-Mandeb → Malakka → Straat Taiwan → Bungo → Seto ·
      ~23.156 km gemeten, aannemelijk: havens niet gebronnet, EXW)──►
MARNET-zeeknoop 5815 ──(naad 4,2 km)──► Dainen Materials, Nakashima, Shikama, Himeji `gr-himeji-dainen` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `gr-lulea-talnode` → `gr-himeji-dainen` | zeeschip Luleå → Himeji (Botnische Golf, Öresund, Kanaal, Gibraltar, Suez, Bab-el-Mandeb, Malakka, Straat Taiwan, Bungo, Seto-binnenzee); aannemelijk: havens niet gebronnet, EXW | 23.156,5 [13] (MARNET, 200 edges, 2.417 punten); geen gepubliceerde lengte, ±15%-toets n.v.t. | MARNET `--been` kade-anker → kade-anker | nee |

Fase A (Hertsön → Luleå-kade) en D (Shikama-kade → Dainen) vervallen (haalbaarheidstoets): geen Luleå-kade en geen
Himeji-kade gevonden, dus geen verzonnen landbeen. De naden zijn 3,8 km (Luleå) en 4,2 km (Himeji), beide < 5 km:
geen haven-aanloop.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-lulea-talnode` | losplek / anodefabriek | Talga Talnode, Hertsöfältet, Luleå Industripark — **letterlijk hergebruikt** uit `grafiet-vittangi-lulea.md` | 65.5670, 22.2840 | [3][11] | **onzeker** (z15 opnieuw gezien: gegrade kavel met grindwegen in naaldbos, ontgravingsplek W erbij, loods en onderstation ZO; geen fabriek; welke kavel Talnode is staat in geen bron; NIET 65.58, 22.15 = marina) |
| `gr-himeji-dainen` | losplek / afnemer | Dainen Materials Co. Ltd., 2985-19 Nakashima, Shikama-ku, Himeji 672-8035 (anodemateriaal, recycling) | 34.7808, 134.6712 | [5][7][14] | **aannemelijk** (adres bevestigd op bedrijfspagina [5]; punt = OSM-weg in postcode 672-8035 uit de haalbaarheidstoets; z15/z17 gezien: zwaar industrieterrein met lange staalhallen en coilopslag naast een havenkanaal, Dainens eigen pand (2018) niet aanwijsbaar) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen: b1 is een MARNET-zeebeen zonder via-punten (de router kiest de Suez-corridor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Talnode-fabriek, Luleå (gepland) + EVA-pilot | Talga Group | Vittangi-grafiet → Talnode-C anode | EVA 50 t/j (sinds 2022); plan 5 kt/j 2027–28, 19,5 kt/j 2028–29; FID niet genomen | [3][4] |
| Dainen Materials, Himeji | Dainen Materials Co. Ltd. | Talnode-C → anodemateriaal voor Japanse batterijklanten (eigen R&D, productie, QC; ook recycling) | niet gepubliceerd | [2][5] |

## 6 · Stoppunt
De brief stopt bij Dainen in Himeji: het term sheet noemt Dainen als koper "of zijn klanten" en de klanten zijn niet met naam
genoemd [1][2]; geen bron geeft een volgende locatie. Fase E vervalt.

## 7 · Open punten
- **BINDEND VERWERKT (haalbaarheidstoets):** fase A en D geschrapt; één zeebeen MARNET tussen de twee site-ankers; beennaam
  "aannemelijk: havens niet gebronnet, EXW"; naden 3,8 en 4,2 km hier vastgelegd; Dainen-anker aannemelijk, Talnode-anker onzeker.
- **Fabriek niet gebouwd:** pilot EVA 50 t/j, raffinaderij pre-FID, 2028–29 voor volle schaal [3][4]; actueel volume 0. Het term sheet
  bindt alleen de capaciteitsreservering; definitieve MSA streefdatum maart 2027 [1][2].
- **Eindpunt Himeji is niet gebronnet:** de persberichten zeggen "Dainen of zijn klanten" en noemen geen leverplaats [1][2]; Himeji is
  het adres van Dainens hoofdkantoor [5]. De klantfabrieken kunnen elders in Japan liggen.
- **EXW** (Dainen regelt het vervoer) staat in het ontwerp, niet in de persberichten die ik kon lezen [1][2]; havens, schip en route zijn
  aannames. Het Talga-ASX-bericht zelf [14] kon ik niet openen.
- **Himeji-kade onbekend.** Mogelijke kade: de Nakashima-container-terminal van Himeji Port (internationale containerlijn sinds 2000 [6],
  warehouse 34.7699, 134.6632 [7]); niet getekend. **Luleå-kade onbekend:** havenlocatie (Svartön/Södra hamn) staat in geen Talga-bron.
- **Winterijs** in de Botnische Golf [9]: één jaarronde lijn, seizoen en ijsbreker-afhankelijkheid niet gemodelleerd.
- **Suez/Bab-el-Mandeb:** de router kiest Suez; containerlijnen keren terug (Alphaliner 21-10-2026: 63% van Far East-Europe) maar
  beveiligingsrisico's blijven [8]. De Kaaproute is niet getekend.
- **Andere Luleå-coördinaat:** `grafiet-skaland-lulea` heeft `gr-lulea-talnode` op 65.58, 22.15 (marina, ~9 km van dit anker); centraal
  gelijktrekken, hier niet aangepast. Sitelaag `w-talga-lulea` staat op dezelfde marina.
- **Marker-afstand:** beide ankers liggen 3,8 en 4,2 km van het eind van de lijn (naad); de bak-agent moet dit als bekend vlaggen.

## 8 · Bronnen
[1] Yahoo Finance, 28-10-2026 — Talga signeert bindend term sheet met Dainen Materials: tot 2.000 tpa Talnode-C, 5 jaar, start eind 2027, MSA streefdatum maart 2027. https://finance.yahoo.com/news/talga-supply-swedish-anode-material-125237231.html
[2] Grafa, 2026 — Talga/Dainen: bindend term sheet, floor-prijs plus premium, opvolger van LOI juli 2026, Japanse klanten niet genoemd. https://grafa.com/en/news/australia/talga-signs-binding-graphite-deal-with-dainen-materials
[3] Talga Group, Luleå-pagina — Anode Refinery in Luleå Industrial Park, EVA 50 t/j sinds 2022, geen haven genoemd. https://www.talgagroup.com/our-operations/lulea/
[4] FilingReader, 15-05-2026 — Talga: 5.000 tpa 2027–28, 19.500 tpa 2028–29, geen FID, EU-subsidie EUR 70 mln. https://filingreader.com/news-wire/sydney/2026-05-15/talga-group-targets-2028-anode-production-with-70m-eu-grant
[5] Dainen Materials, bedrijfspagina — hoofdkantoor 2985-19 Nakashima, Shikama, Himeji, Hyogo 672-8035; anodematerialen en recycling. https://www.dainenmaterials.com/company
[6] ja.wikipedia, 姫路港 — Himeji Port (Shikama-, Hirohata-, Aboshi-havengebied), internationale containerlijn op Nakashima-wharf sinds 2000; coordinaat 34.78486, 134.6629. https://ja.wikipedia.org/wiki/%E5%A7%AB%E8%B7%AF%E6%B8%AF
[7] Photon (OSM) — plaats 飾磨区中島 672-8035 op 34.7855, 134.6741; 姫路港運 Nakashima-loods 34.7699, 134.6632. https://photon.komoot.io/api/?q=飾磨区中島
[8] Ship & Bunker, 21-10-2026 — Alphaliner: 63% van Far East-Europe-capaciteit terug op Suez; beveiligingsrisico's blijven. https://shipandbunker.com/news/emea/932812-container-lines-shift-63-of-far-east-europe-capacity-back-to-suez-canal-alphaliner
[9] Sjöfartsverket, vintersjöfart 2025/26 (ijsbrekerdienst Botnische Golf). https://sjofartsverket.se/globalassets/tjanster/isbrytning/pdf-vintersjofart/vintersjofart_svenska_2025_web11.pdf
[10] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-grafiet-lulea-himeji-talnode.png`, `-dainen.png`, `-dainen17.png`.
[11] `v2/design/routebrieven/grafiet-vittangi-lulea.md` — anker `gr-lulea-talnode` 65.5670, 22.2840 (onzeker).
[12] `v2/design/routebrieven/grafiet-skaland-lulea.md` — zeeknoop 8830 Luleå-zijde, marina-coördinaat 65.58, 22.15.
[13] Eigen meting `hecht_marnet.py route`, 2026-10-31 — snaps 3,771 km (knoop 8829, 65.5340, 22.3029) en 4,170 km (knoop 5815, 34.7433, 134.6704); 23.156,5 km.
[14] Haalbaarheidstoets keten `grafiet-lulea-himeji` (workflow) — Dainen-adres, OSM-weg 34.7808, 134.6712, Talga-ASX 28-10-2026 (company-announcements.afr.com niet bereikbaar).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
Functie `bak_grafiet_lulea_himeji` in `v2/tools/bak_stromen.sh`; `bash v2/tools/bak_stromen.sh grafiet-lulea-himeji` -> `v2/data/stroomroute-grafiet-lulea-himeji.json` (42,3 KB, versie 2, lonlat, 2.417 punten). Geen profiel, geen extract, geen spoor/vlucht/leiding.

| # | modaliteit | been | km gemeten | km brief | stippel |
|---|---|---|---|---|---|
| b1 | zee | zeeschip Luleå -> Himeji (aannemelijk: havens niet gebronnet, EXW) | 23.156,5 (MARNET 200 edges, 2.417 punten) | geen gepubliceerde lengte; 23.156,5 indicatie | nee (doorgetrokken) |

Totaal 23.156,5 km. Eén been, dus geen naden tussen benen. Markers: `gr-lulea-talnode` (65.5670, 22.2840, onzeker) en `gr-himeji-dainen` (34.7808, 134.6712, aannemelijk); ze liggen 3,77 en 4,17 km van de lijneinden (zeeknoop 8829 en 5815). Dat is de bewuste naad uit §3/§7: onder de 5 km, dus geen haven-aanloop en geen last-mile-stippel; de lijn eindigt waar het net eindigt.
Recept: `hecht_marnet.py route --been "zee|...|65.5670,22.2840|34.7808,134.6712"` plus twee `--marker`. Router kiest Suez/Bab-el-Mandeb; Kaaproute en winterijs niet gemodelleerd.
Toets: `toets_knikken.py` 6 knikken >= 60 gr (Seto-binnenzee, Öresund, Straat Gibraltar-zone, Botnische Golf; allemaal 1:10M-kustnet, 0 omkeringen, 0 terugloop); `toets_rechte_benen.py` geen melding; json.load ok.
Lessen: (1) bij twee kade-ankers op 3-5 km van de zeeknoop is het markerverschil een bewuste naad en geen fout; (2) het Luleå-anker verschilt 9 km van de marina-coördinaat in `grafiet-skaland-lulea` en sitelaag `w-talga-lulea`: centraal gelijktrekken.
