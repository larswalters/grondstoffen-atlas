# Routebrief (licht) · Lithium · Gwanda → Beitbridge → Maputo (Zimbabwe → Mozambique)

**stroom-id:** `lithium-gwanda-maputo` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van Tsingshans Gwanda-lithiummijn (Dinson Mining Investments) gaat per truck naar het nieuwe BBR-opstelspoor bij West Nicholson en daar per **spoor** (BBR → NRZ via Beitbridge en Rutenga → grens Sango/Chicualacuala → CFM Limpopo-lijn) naar de haven van Maputo; de kade is *aannemelijk: één bron, terminal niet genoemd*. Het zeebeen naar China is niet gedocumenteerd en is **geschrapt** (haalbaarheidstoets).
**Welke as van het verhaal:** as 2 (M31 golf 8) — Zimbabwes tweede uitgang naast de Beira-wegritten: een proeflading van 1.000 t concentraat (juli 2026, ≈ 0,15 kt LCE — **eigen omrekening**, 6 % Li2O × 2,473), geen jaarvolume of contract [1][2][3]. Context: Zimbabwe voerde in 2025 1,13 Mt concentraat uit naar China (douane) [3]; concentraatverbod 2027, bevriezing feb. 2026 kunnen de stroom stoppen.

## 1 · Ketenkaart
```
Gwanda-mijn (Tsingshan/Dinson, Mandihongola; coördinaat NIET gepubliceerd)  ··truck, niet getekend··►
West Nicholson-opstelspoor `li-wnicholson-siding` (BBR, nieuw; aannemelijk)
  ──(b1 spoor · Beitbridge Bulawayo Railway · 152,2 km)──► Beitbridge-emplacement `li-beitbridge-emplacement` (kopmaken)
  ──(b2 spoor · NRZ via Rutenga (kopmaken) en Sango · 282,0 km)──► grens `li-chicualacuala-grens`
  ──(b3 spoor · CFM Limpopo-lijn via Mabalane en Chókwè · 521,0 km)──► Maputo-kade `li-maputo-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `li-wnicholson-siding` → `li-beitbridge-emplacement` | BBR-lijn West Nicholson–Beitbridge | 152,2 gemeten; bron "Gwanda–Beitbridge ca. 180" [1][2] = **−15,4 %**, maar de bron meet vanaf Gwanda (station: 200,8 km, +11 %), het siding ligt 49 km dichterbij — indicatie, geen norm | toets_spoorroute (1-op-1-net) | nee |
| b2 | A | spoor | `li-beitbridge-emplacement` → `li-chicualacuala-grens` | NRZ Beitbridge–Rutenga–Sango–Chicualacuala | 282,0 gemeten; bron "ca. 300" [1][2] = **−6,0 %** | toets_spoorroute | nee |
| b3 | A | spoor | `li-chicualacuala-grens` → `li-maputo-kade` | CFM Linha do Limpopo | 521,0 gemeten; bron 522 [1][2] = **−0,2 %** | toets_spoorroute | nee |

Totaal 955,2 km tegen bron "ca. 1.000" (−4,5 %). Aannemelijk-een-bron staat in de ankers en in de ketennaam, niet in de lijnstijl; **geen stippel**, het net reikt overal (OSM-spoorcomponent 47.640 km, geen naad). Geen zeebeen: de zeeknoop van de kade ligt 6,7 km weg (-25.9951,32.6060, knoop 5197) — bij een later zeebeen hoort er een haven-aanloop (> 5 km).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-wnicholson-siding` | laadplek spoor | West Nicholson, BBR-siding (US$ 1,5 mln, nieuw) | -21.0662, 29.3668 | [1][4][5] | aannemelijk (z16 gezien: spoorwaaier met zijsporen bij de wegbrug, geen laadinstallatie aan te wijzen; ligt 0,3 km van het spoor; Wikipedia-plaats -21.0644/29.365) |
| `li-beitbridge-emplacement` | kopmaakplek | Beitbridge, rangeeremplacement oost van de stad | -22.1906, 30.0136 | [8] | bron-gelegd (z15 gezien: spoorwaaier met meerdere sporen, bij het vliegveldje) |
| `li-chicualacuala-grens` | grensovergang | Sango (ZW) / Chicualacuala (MZ), grensemplacement | -22.0801, 31.6834 | [6][7] | bron-gelegd (z15 gezien: langgerekt emplacement met meerdere sporen en een keerlus; Wikipedia -22.0833/31.6833) |
| `li-maputo-kade` | losplek (stoppunt) | Haven van Maputo, kade met bulkcarriers en mineraalopslag | -25.9635, 32.5495 | [1][9] | aannemelijk (z16 gezien: twee bulkcarriers aan de kade, zwarte/grijze opslaghopen en sporen direct erachter; bron noemt geen terminal) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1–b3 | — | **geen** | — | enkelsporige lijn zonder tweede corridor; de drie runs lopen van emplacement tot emplacement (naad 0,00 km). Een vrije Dijkstra vindt dezelfde lijn: Rutenga ligt 2,9 km, Beitbridge 2,1 km, Mabalane 0,2 km en Chókwè 3,3 km van de gemeten lijn |

Keerpunten die `toets_knikken` zal melden (geen fout, kopmaken of driehoek): Beitbridge -22.1918,30.0110 (180°) en Rutenga -21.2534,30.7452 (178,8°) — beide in de haalbaarheidstoets genoemd; plus Maputo -25.9338,32.5232 (177°, straal ~150 m), niet vooraf bekend: de lijn loopt langs de stad voorbij de havenaftakking en keert terug, vermoedelijk een driehoek bij Maputo-west.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Gwanda-mijn (Mandihongola, voormalige tinmijn) | Tsingshan / Dinson Mining Investments | erts → concentraat (op site) | niet gepubliceerd; eerste lading 1.000 t | [1][10] |

Geen verdere knoop: het concentraat gaat ongewijzigd naar de haven.

## 6 · Stoppunt
De brief stopt op de kade van Maputo: geen bron noemt een terminal, een schip, een afnemer of een bestemming ná Maputo [1][2][3]; het optionele zeebeen naar de Yangtze is aanname en vervalt (fase C/D/E vervallen).

## 7 · Open punten
- **Mijncoördinaat ongepubliceerd:** de tracker [10] geeft -20.9389/29.0186, maar dat is het centrum van Gwanda-stad en spreekt de eigen tekst ("15 km NW van Kafusi", Kafusi -21.60/28.77) tegen; niet gebruikt. Het truckstuk mijn → siding is niet getekend, de lijn begint waar het bewijs begint (het siding).
- **Laadpunt: West Nicholson, niet Gwanda-station.** [4] (en bijschrift [1]) noemen het nieuwe BBR-siding West Nicholson als laadplek; de haalbaarheidstoets koos nog Gwanda-station (-20.9401,29.0073) omdat de bronnen "Gwanda" zeggen. Het siding zelf is niet exact aan te wijzen; ankerpunt = het spoor bij de plaats.
- **Maputo-terminal onbekend** [1][2][3][9]; kadepunt is een bulkkade, geen bevestigde terminal. De toets stelde -25.9625/32.5475 voor; dat punt ligt 200 m van de kade bij de containerzijde, verschoven naar de bulkkade.
- **Geen jaarvolume** en geen bewijs van regelmaat (proeflading); volume in LCE is eigen omrekening.
- **Mapai** (Nominatim -22.62/32.48) ligt 44 km van de gemeten lijn: de plaatscoördinaat is waarschijnlijk niet het station; totaal 521 km tegen 522 bevestigt de lijn.
- Kopmaakpunten Rutenga en Maputo-west zijn niet satelliet-bekeken.
- Gwanda-mijn staat niet in `lithium-sitelaag` (geen coördinaat, geen capaciteit): geen gloedknoop; sitelaag niet aangeraakt.

## 8 · Bronnen
[1] ZimLive, 23-07-2026 — "Zimbabwe adds freight rail option to lithium export gateway": eerste 1.000 t concentraat, Tsingshan Gwanda, Gwanda–Beitbridge 180 / –Chicualacuala 300 / –Maputo 522 km, BBR-siding West Nicholson (bijschrift), geen terminal. https://www.zimlive.com/zimbabwe-adds-freight-rail-option-to-lithium-export-gateway/
[2] SMM, 22-07-2026 — "Zimbabwe opens rail route to Maputo": zelfde trajecten, "logistiek proef", geen afnemer. https://news.metal.com/newscontent/104019049-smm-analysis-zimbabwe-opens-rail-route-to-maputo-easing-lithium-export-logistics-constraints
[3] Equity Axis, 07-2026 — haven-concurrentie, 1,13 Mt concentraat 2025, geen terminal. https://equityaxis.net/post/19275/2026/7/zimbabwe-s-lithium-rail-service-intensifies-regional-port-competition
[4] Freight News (ZA), 07-2026 — "Rail corridor opens new export route for Zim lithium": trein geladen op het nieuwe BBR West Nicholson-siding; Port of Maputo. https://www.freightnews.co.za/article/rail-corridor-opens-new-export-route-for-zim-lithium
[5] Wikipedia, "West Nicholson" — -21,0644/29,365. https://en.wikipedia.org/wiki/West_Nicholson
[6] Wikipedia, "Chicualacuala" — -22,0833/31,6833, grensplaats tegenover Sango. https://en.wikipedia.org/wiki/Chicualacuala
[7] Wikipedia, "Sango, Zimbabwe" — -22,0697/31,6803, grenspost. https://en.wikipedia.org/wiki/Sango,_Zimbabwe
[8] Wikipedia, "Beitbridge Bulawayo Railway" — BBR Bulawayo–Beitbridge 317 km, Cape-spoor 1.067 mm. https://en.wikipedia.org/wiki/Beitbridge_Bulawayo_Railway
[9] Wikipedia, "Port of Maputo" — havencomplex Maputo-Matola, exploitant MPDC (CFM/DP World/Grindrod). https://en.wikipedia.org/wiki/Port_of_Maputo
[10] China Global South Project, "Gwanda Lithium" — Dinson Mining Investments (Tsingshan), Mandihongola, Gwanda District, actief sinds 2022 (coördinaat van de tracker niet gebruikt). https://africamining.chinaglobalsouth.com/projects/gwanda-lithium
[11] Discovery Alert, 07-2026 — siding West Nicholson als overslag truck → trein; geen terminal, geen jaarvolume. https://discoveryalert.com/zimbabwe-lithium-export-rail-maputo-port-corridor-2026/

## 9 · Bak-noot
**Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)** — `bash v2/tools/bak_stromen.sh lithium-gwanda-maputo` → `v2/data/stroomroute-lithium-gwanda-maputo.json` (17,4 KB, contract versie 2, lonlat).

| # | modaliteit | been | km gebakken | km brief | afwijking |
|---|---|---|---|---|---|
| b1 | spoor | West Nicholson BBR-siding → Beitbridge | 152,8 | ca. 180 (bron vanaf Gwanda) | −15,1 % (indicatie, zie §2) |
| b2 | spoor | Beitbridge → Rutenga → Sango/Chicualacuala | 283,1 | ca. 300 | −5,6 % |
| b3 | spoor | Chicualacuala → Mabalane → Chókwè → Maputo | 522,1 | 522 | +0,0 % |

Totaal 958,0 km (de bake telt de polylijn; toets_spoorroute meldde 955,2 km routeKm), 880 punten, 4 markers, naden 0,000 km. **Recept:** drie runs `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (hoofd-km 1000, max-snap 60, geen via-punten), geojson in `v2/build-cache/ais/graaf/spoorroute-lithium-gwanda-maputo-{westnicholson-beitbridge,beitbridge-chicualacuala,chicualacuala-maputo}.geojson`, daarna `bak_lithium_gwanda_maputo` (drie `--been-geojson spoor`, vier `--marker`, geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen kopie).

**Toets.** Markers van hun lijn: siding 301 m (anker is het spoor bij de plaats, snap 0,3 km), Beitbridge 34 m, Sango/Chicualacuala 66 m, Maputo-kade 15 m. `toets_knikken`: 4 omkeringen, 0 terugloop, precies de voorspelde kopmaakpunten (Beitbridge 180° op b1-eind en b2-begin, Rutenga 178,8°, Maputo-west 177°). `toets_rechte_benen`: geen rechte been voor deze stroom. `json.load` ok, versie 2, punt_formaat lonlat, modaliteit alleen spoor.

**Toelichting.** Geen stippel, geen haven-aanloop (geen zeebeen: zeeknoop van de kade ligt 6,7 km weg, pas relevant bij een later zeebeen), geen luchtbeen, geen leiding. Het truckstuk mijn → siding is niet getekend (mijncoördinaat ongepubliceerd). Km-afwijking b1 komt door de bron, die vanaf Gwanda-station meet (nu 200,8 km); tegen de afstand vanaf het siding klopt het.

**Lessen.** De drie vooraf gebakken spoorgeojsons uit de brief-fase waren compleet en zijn ongewijzigd hergebruikt (de bake routeert ze niet opnieuw). De hecht_marnet-km komt ~0,3 % hoger uit dan de routeKm van het spoortool (polylijn tegen padlengte).
