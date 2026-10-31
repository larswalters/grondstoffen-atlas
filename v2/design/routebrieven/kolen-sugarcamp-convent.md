# Kolen · Sugar Camp (Illinois) → Memphis → Convent Marine Terminal (Louisiana, VS)

**stroom-id:** `kolen-sugarcamp-convent` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) · **status:** gebakken
**Keten in één zin:** thermische kolen uit de ondergrondse Sugar Camp-mijn (MC 1, Franklin County, Illinois) per Canadian National-spoor (ex-Illinois Central) via
Fulton (Kentucky), Memphis, Grenada, Jackson en McComb naar de Convent Marine Terminal (SunCoke) aan de oostoever van de Mississippi in St. James Parish, Louisiana,
de Golfkust-exportkade. Eén spoorbeen van ca. 1.070 km, geen zeebeen (geen bron noemt een loshaven), geen weg, geen fase D/E.
**Welke as van het verhaal:** reserve-as, Illinois-bekken naar de Amerikaanse Golfkust. Sugar Camp 4,88 Mt ROM in 2025, 5,79 Mt in 2023 (GEM [1]); terminal 15 Mst/j
capaciteit (SunCoke [4]). **Eenheid: Mt kolen per jaar.** Aannemelijk: één bron voor de koppeling mijn-terminal (CN-contract 2011 voor vier Illinois-mijnen [2][3], Sugar Camp niet bij naam).

## 1 · Ketenkaart
```
Sugar Camp-mijn (Franklin Co., IL) `kolen-sugarcamp-laad`
   ──(b1a spoor · CN via Metropolis en Fulton · ~398 km)──► Memphis (tussenpunt)
   ──(b1b · CN Grenada Sub via Batesville · ~157 km)──► Grenada
   ──(b1c · CN via Jackson, McComb, Hammond, New Orleans-zijde, LaPlace, Gramercy · ~520 km)──► Convent Marine Terminal `kolen-convent-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | A | spoor | `kolen-sugarcamp-laad` → Memphis (35.0730, -90.0740) | CN ex-Illinois Central, route-uitkomst (Metropolis, Fulton) | hemelsbreed 348 km, geen gepubliceerde spoorkm; proef 396,2 | toets_spoorroute (BAKE_SUFFIX=-raw) | nee (snap 0,85 km) |
| b1b | A | spoor | Memphis → Grenada (33.7693, -89.8035) | CN Grenada Sub, route-uitkomst | hemelsbreed 147 km, geen gepubliceerde spoorkm; proef 156,0 | toets_spoorroute | nee |
| b1c | A | spoor | Grenada → `kolen-convent-kade` | CN via Jackson, McComb, Hammond en de oostoever-lijn naar Gramercy, route-uitkomst | hemelsbreed 425 km, geen gepubliceerde spoorkm; proef 515,4 | toets_spoorroute | nee (snap 0,29 km) |

Totaal gemeten proef 1.067,6 km (geojson-lengte 1.075 km, andere afstandsformule) tegen hemelsbreed 907 km (verhouding 1,18); geen gepubliceerde spoorlengte: de
±15%-toets geldt als indicatie, niet als norm. Het ontwerp noemde 1.047 km met vier via-punten; vrij routeren geeft 1.079,6 km (+3,1%). De beennaam draagt
"(aannemelijk: één bron)". De drie stukken sluiten met naad 0 m op elkaar.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-sugarcamp-laad` | mijn / laadlus | Sugar Camp-mijn (MC 1, M-Class Mining / Viking Mine), Macedonia, Franklin County | 38.0264, -88.7679 | [1][8] | bron-gelegd (z15 gezien: bereidingsinstallatie met kolenstapel, silo en transportband bij het kruis, slibbekken ervoor, een spoorlus ~1,1 km oostelijker; router snapt op 0,85 km) |
| `kolen-convent-kade` | overslag spoor → zeeschip/schuit | Convent Marine Terminal (SunCoke, ex-IC RailMarine), Milepost 161, oostoever | 30.0483, -90.8328 | [2][4][5][8] | bron-gelegd (z14 gezien: kolenstapel met dok aan de oostoever van de rivier; GEM: oostoever Milepost 161; Convent-dorp 30.0208, -90.8297 ligt ~3 km zuidelijker en is geen anker) |

## 4 · Via-punten (alleen spoorbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1a/b1b | 1 | Memphis, op de CN-lijn (westzijde stad) | 35.0730, -90.0740 | snap 0,03 km; scheidt het noordelijke stuk van de keuze Grenada Sub of Delta-lijn |
| b1b/b1c | 2 | Grenada, op de CN-hoofdlijn | 33.7693, -89.8035 | snap 0,31 km; pint de Grenada Sub (via Batesville, Winona, Canton). Zonder dit punt kiest de router een Delta-route via Tunica, Greenwood en Yazoo City (Grenada 37 km ernaast), 1.079,6 km |
Vervallen uit het ontwerp: Fulton (36.6125, -88.8493) en Amite-zijde (30.8236, -90.5104) liggen al op de vrije route; Memphis-noord (35.4646, -89.7501) snapte 3,0 km ernaast en
(32.8589, -89.997) 3,0 km, die gaven een omkering. Het geojson raakt Fulton 0,2 km, Jackson 0,6, McComb 0,3, Hammond 0,1, LaPlace 0,8 en Gramercy 0,7 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sugar Camp (MC 1) | M-Class Mining LLC en Viking Mine LLC, ex-Foresight (huidige eigenaar niet bevestigd) | steenkool → gewassen thermische kolen | 4,88 Mt ROM in 2025; reserves 1.179 Mt | [1] |
| Convent Marine Terminal | SunCoke Energy (gekocht 2015, 412 mln dollar) | trein → zeeschip en schuit | 15 Mst/j (13,6 Mt) na shiploader 2016 | [2][4] |

## 6 · Stoppunt
De brief stopt bij de CMT-kade: geen bron noemt voor Sugar Camp-kolen een loshaven of afnemer (GEM: export vooral naar Europa), dus geen zeebeen en geen fase D/E.

## 7 · Open punten
- **Sugar Camp niet bij naam bij CMT.** Alleen het CN-contract van 2011 (Savatran, vier Illinois-mijnen naar Convent [2][3]) en 2019 ca. 5 Mst Foresight via CMT van 6,5 Mst totaal [6] (via zoeksamenvatting); aandeel van Sugar Camp niet gepubliceerd.
- **Eigenaar en huidige stroom:** na het Foresight-faillissement (maart 2020 [7], via zoeksamenvatting) is de huidige eigenaar niet gevonden; of er nu kolen van Sugar Camp naar Convent gaan is onbevestigd; het CN-contract was 10 jaar vanaf 2011.
- **Mijnaansluiting op het CN-net:** het eerste stuk (Sugar Camp tot Fulton, ~160 km) loopt via Metropolis en de Ohio; dat is een route-uitkomst, de bron die de aansluiting noemt is niet gevonden en het laadspoor ligt 0,85 km van het punt.
- **Corridor Memphis-Jackson:** Grenada Sub gekozen (hoofdlijn, +0 via-keuze); de Delta-variant is 12 km langer en niet uitgesloten.
- **Route langs New Orleans:** het pad Hammond naar Gramercy loopt via de oostzijde van New Orleans (max. 19 km van het centrum) en volgt dan de oostoever; bron voor deze keuze niet gevonden.
- **Spoorkm:** geen gepubliceerde lengte (hemelsbreed 907 km); proef 1.067,6 km.
- **Zee:** MARNET-zeeknoop 56,8 km van de kade (zou een haven-aanloop vragen); niet getekend omdat er geen zeebeen is.
- **Sitelaag en v1:** Sugar Camp ontbreekt in `kolen-sitelaag.json`, `data/coal.js` en `design/kolen.md` hebben geen Illinois-stroom; centrale beslissing.

## 8 · Bronnen
[1] Global Energy Monitor, Sugar Camp Mine: eigenaar M-Class Mining, 38.0264/-88.7679, ROM 2017-2025 (4,88 Mt 2025; 5,79 Mt 2023). https://www.gem.wiki/Sugar_Camp_Mine
[2] Global Energy Monitor, Convent Marine Terminal: SunCoke, 2015 gekocht voor 412 mln dollar, 15 Mst na 2016, Milepost 161 oostoever, CN-contract 2011. https://www.gem.wiki/Convent_Marine_Terminal
[3] Global Energy Monitor, Foresight Reserves: Sugar Camp als Cline-mijn; CN verkocht IC RailMarine in 2011; 10-jarig contract voor vier Illinois-mijnen. https://www.gem.wiki/Foresight_Reserves
[4] SunCoke Energy, Logistics: CMT 15 miljoen ton per jaar. https://www.suncoke.com/en/our-business/industrial-services/logistics
[5] Wikipedia, Convent, Louisiana: oostoever, 30.0208/-90.8297. https://en.wikipedia.org/wiki/Convent,_Louisiana
[6] SunCoke Energy Partners Q3 2019 earnings call (via zoeksamenvatting, niet geopend): CMT 2019 ca. 6,5 Mst waarvan 5 Mst Foresight. https://www.fool.com/earnings/call-transcripts/2019/11/06/suncoke-energy-partners-sxcp-q3-2019-earnings-call.aspx
[7] KFVS12, Foresight Energy declares Chapter 11 (2020-03-11, via zoeksamenvatting). https://www.kfvs12.com/2020/03/11/foresight-energy-declares-chapter-bankruptcy/
[8] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-kolen-sugarcamp-convent-mijn.png` (z15), `…-cmt.png` (z14).
[9] Eigen routerruns `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs … --hoofd-km=1000 --max-snap=60` (3.260.717 spoor-edges): vrij 1.079,6 km; stukken mijn-memphis 396,2 · memphis-grenada 156,0 · grenada-convent 515,4 km; 0 bochten ≥ 60 graden.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Bestand:** `v2/data/stroomroute-kolen-sugarcamp-convent.json` (32,6 KB, contract versie 2, lonlat) · **functie:** `bak_kolen_sugarcamp_convent` in `v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh kolen-sugarcamp-convent` (20 s).

| # | modaliteit | km (gemeten) | proef router | punten | stippel | naam |
|---|---|---|---|---|---|---|
| 1 | spoor | 398,6 | 396,2 | 601 | nee | deel 1/3 mijn → Memphis (Metropolis, Fulton) |
| 2 | spoor | 156,6 | 156,0 | 293 | nee | deel 2/3 Memphis → Grenada (CN Grenada Sub) |
| 3 | spoor | 520,1 | 515,4 | 816 | nee | deel 3/3 Grenada → Convent (Jackson, McComb, Hammond, New Orleans-oostzijde) |

Totaal 1.075,3 km, 1.710 punten, naden 0 m, 0 knikken >= 60 graden, 0 omkeringen. Markers: `kolen-sugarcamp-laad` (0,85 km van de lijn: het laadspoor ligt ~1,1 km oostelijker, snap
zoals in §3) en `kolen-convent-kade` (0,29 km). Geen gepubliceerde spoorkm: de +-15%-toets is een indicatie (geojson-lengte wijkt 0,6% af van de routerproef, andere afstandsformule).

**Recept:** drie `--been-geojson "spoor|…"` in reisvolgorde, de router-uitvoer van `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs … --hoofd-km=1000 --max-snap=60`
(`spoorroute-kolen-sugarcamp-convent-{mijn-memphis,memphis-grenada,grenada-convent}.geojson`, niet opnieuw gerund), twee markers, geen zee/weg/leiding/lucht, geen stippel, geen haven-aanloop, geen kopie.
**Toelichting:** geen stippel nodig (het net reikt tot 0,85 km van de mijn en 0,29 km van de kade); geen haven-aanloop omdat er geen zeebeen is (zeeknoop 56,8 km van de kade).
Aannemelijk (een bron) staat in de beennaam. **Lessen:** de Grenada-pin is nodig, vrij routeren geeft de Delta-route 1.079,6 km; 3 stukken met naad 0 m voorkomen een stippel op de naad.
