# Routebrief (licht) · grafiet — Balama → Nacala → Saemangeum (Zuid-Korea)

**stroom-id:** `grafiet-balama-saemangeum` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** Mozambikaans vlokgrafiet van de Balama-plant (Syrah Resources) reist per truck (kopie van been 1
`grafiet-balama-vs`) naar de containerterminal Nacala, per **zeeschip** (aannemelijke haven, geen tweede bron) naar
Gunsan New Port bij het Saemangeum-complex, per truck naar de nog in aanbouw zijnde spheronisatiefabriek van
Future Graph (POSCO Future M, oplevering 2027) in Saemangeum, en — op één bron, niet in het offtake-contract zelf —
door naar de bestaande POSCO Future M-anodefabriek in Sejong. **Volume is vandaag nul**: geen bron bevestigt dat er
al Balama-vlok in Zuid-Korea is gelost.
**Welke as van het verhaal:** het Aziatische ex-China-alternatief — Korea haalt vandaag ~93 % van zijn anodemateriaal
uit China [6]; Syrah–POSCO Future M tekenden maart 2024 een offtake (tot 24 kt jaar 1, 60 kt/j vanaf jaar 2, zes
jaar, levering in Zuid-Korea) [1][7], en Saemangeum moet de Chinese spheronisatiestap vervangen die daar tot 2027
nog altijd voor nodig is.

## 1 · Ketenkaart
```
Balama-plant `gr-balama-mill` ──(b1 truck · N380/N1, kopie been 1 grafiet-balama-vs · 498 km)──► Nacala-terminal `gr-nacala-kade`
   ──(b2 zee · Indische Oceaan–Malakka–Oost-Chinese Zee–Gele Zee, aannemelijk (één bron) · ~11.000 km, MARNET)──► Gunsan-kade `gr-gunsan-kade`
   ──(b3 truck · haven → industrieterrein, ~4 km, onzeker anker)──► Future Graph Saemangeum `gr-saemangeum-fabriek` (SPG, 2027)
   ──(b4 truck · Seohaean Expwy 15 → Iksan JC → Nonsan JC → Nonsan-Cheonan Expwy 25, aannemelijk (één bron) · ~180 km)──► POSCO Future M Sejong `gr-sejong-fabriek` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Balama-plant → Nacala-containerterminal | N380/N1 — **letterlijke kopie van been 1 (+ last mile) `grafiet-balama-vs`**, `stroomroute-pilot.json` | 497,9 [8] | kopie uit `stroomroute-pilot.json` | nee |
| b2 | B | zee (volume nul: leveringen aan POSCO niet gepubliceerd) | Nacala-kade → Gunsan-kade | Indische Oceaan → Malakka → Zuid-Chinese Zee → Oost-Chinese Zee → Gele Zee | ~11.000, geen publicatie | MARNET | nee — de haven zelf is aannemelijk, de route niet |
| b3 | C | truck | Gunsan-kade → Future Graph Saemangeum | binnen het Saemangeum/Gunsan-industriecomplex (Osikdo-dong) | ~4, geen publicatie | maak_stroombeen_weg (of stippel als het net de fabriek niet dekt) | mogelijk — plant-anker is *onzeker* |
| b4 | C | truck (volume nul: leveringen aan POSCO niet gepubliceerd) | Future Graph Saemangeum → POSCO Future M Sejong | Route 21 → Seohaean Expwy (15) → Iksan JC → Nonsan JC → Nonsan-Cheonan Expwy (25) → Jeonui-industriepark | ~180, geen publicatie | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-balama-mill` | mijn / laadplek | Balama-plant (Syrah Resources), Mozambique | -13.310, 38.660 | [8] (hergebruik `grafiet-balama-vs`) | bron-gelegd (hergebruikt anker, eerder satelliet-gelegd) |
| `gr-nacala-kade` | overslag | Nacala-containerterminal, oostoever | -14.5383, 40.6673 | [8] (hergebruik `grafiet-balama-vs`) | bron-gelegd (hergebruikt anker, eerder satelliet-gelegd) |
| `gr-gunsan-kade` | losplek zee | Gunsan (New) Port, Osikdo-dong, bij het Saemangeum-complex | 35.9770, 126.5830 | [9] geen bron noemt de haven expliciet | **aannemelijk** (z16 gezien: functionerende diepwaterkade met twee tankers/vrachtschepen langszij en een RoRo/auto-opstelterrein ernaast [12]; Busan en Pyeongtaek zijn even goed bereikbare alternatieven als een latere bron een andere haven noemt) |
| `gr-saemangeum-fabriek` | verwerkingsknoop (SPG) | Future Graph — POSCO Future M, Saemangeum Nationaal Industriecomplex blok 6, Osikdo-dong, Gunsan | 35.9680, 126.5480 | [2][3][4] | **onzeker** (z16 gezien: dicht bebouwd industrieterrein zonder onderscheidend bord; bouw begon begin 2026 [4] en is op deze opname niet van de buurpercelen te scheiden [12]) |
| `gr-sejong-fabriek` | fabriek (AAM) | POSCO Future M — Sejong natuurlijk-grafiet-anodefabriek 1 | 36.7059, 127.2203 | [11] officieel adres 세종특별자치시 산단길 22-64 | **aannemelijk** (z16 gezien: druk industrieterrein in het Jeonui-industriepark; het POSCO Future M-pand is op deze opname niet te onderscheiden van een naastgelegen KCC-fabriek [12]) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b4 | 1 | Dong-Gunsan IC (op de Seohaean Expwy) | 35.9452, 126.8342 | pint de instap op de kustsnelweg (15) i.p.v. de lokale N-wegen om de Saemangeum-baai |
| b4 | 2 | Iksan-knooppunt | 35.9504, 127.0971 | corridorkeuze: hier kan de route naar de Honam-as of oostwaarts richting Nonsan afbuigen |
| b4 | 3 | Nonsan-knooppunt (start Nonsan-Cheonan Expwy 25) | 36.0834, 127.0998 | pint de overstap van de kustcorridor naar de noord-zuidas 25 die naar Sejong loopt |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Future Graph Saemangeum (SPG) | POSCO Future M (dochter Future Graph) | vlokgrafiet → sferisch grafiet (SPG) | 37 kt SPG/j nameplate, oplevering Q3 2027, opstart Q4 2027, KRW 436 mrd | [2][4] |
| POSCO Future M Sejong (plant 1 + 2) | POSCO Future M | SPG → natuurlijk-grafiet-anodemateriaal (AAM) | plant 1 + 2 samen ca. 74 kt/j-orde AAM (bedrijfscijfer, niet per site gesplitst) | [11] |

Beide knopen draaien vandaag grotendeels op Chinees vooraf-gespheroniseerd of Chinees ingekocht grafiet; Saemangeum
moet die stap pas vanaf 2027 overnemen — tot dan is niet gepubliceerd wáár Balama-vlok tussentijds wordt bewerkt [3][4].

## 6 · Stoppunt
De brief stopt bij de Sejong-anodefabriek: dat is het eindproduct (AAM) en de enige plek waar één bron ondubbelzinnig
zegt dat Saemangeum-SPG naartoe gaat [3][4]; de afnemende batterijcellenfabrieken (LG Energy Solution, SK On,
Samsung SDI, Panasonic, en een niet-genoemde Japanse en Amerikaanse klant [6][11]) zijn niet één fabriek — fase D
vervalt.

## 7 · Open punten
- **Geen leveringsbewijs:** het offtake-contract (maart 2024, 24→60 kt/j) staat vast [1][7], maar geen bron bevestigt
  dat er in 2025/2026 al Balama-vlok in Zuid-Korea is aangekomen; Syrah's eigen kwartaalrapporten noemen POSCO niet
  en leggen de 55 kt ex-China-verkoop 2025 bij Indonesië en de VS [10]. Beide truck- en zeebenen dragen daarom
  "volume nul" in de naam.
- **Koreaanse loshaven niet gepubliceerd:** Gunsan is aannemelijk (naast het Saemangeum-complex, 8–11 km van de
  dichtstbijzijnde MARNET-zeeknoop [9][12]), maar geen bron noemt een haven met naam; Busan en Pyeongtaek zijn
  reële alternatieven.
- **Tussenstap vóór 2027 onbekend:** tot Saemangeum draait wordt Balama-vlok ergens anders gespheroniseerd
  (mogelijk China) — niet gepubliceerd, dus niet getekend.
- **Saemangeum-perceel niet scherp:** blok 6 van het Saemangeum-industriecomplex ligt in hetzelfde dichtbebouwde
  Osikdo-dong-gebied als de bestaande Gunsan-industriehavens; op deze satellietopname is het Future Graph-perceel
  niet te onderscheiden van de buren — bouw begon pas begin 2026 [4].
- **Sejong-pand niet scherp:** het officiële adres (산단길 22-64) ligt in een druk industriepark waar op deze opname
  een naastgelegen KCC-pand net zo goed past; niet verder ingezoomd (z16 is de lichte-werkwijze-limiet).
- **km b3/b4 niet gepubliceerd:** beide zijn OSRM/wegnet-schattingen; de bake-toets is de eerste echte meting.

## 8 · Bronnen
[1] Benchmark Minerals — Syrah–POSCO Future M offtake highlights appetite for ex-China flake graphite (maart 2024). https://source.benchmarkminerals.com/article/syrah-posco-offtake-agreement-highlights-appetite-for-ex-china-flake-graphite
[2] Korea Herald — Posco Future M invests W436b for new anode material plant in Saemangeum, 37 kt SPG/j, oplevering 2027 (2025). https://www.koreaherald.com/article/10503706
[3] EBN News — 포스코퓨처엠, 새만금 투자 속도…구형흑연 공급망 핵심 거점으로: "새만금에서 생산된 구형흑연을 세종 음극재 공장에 공급" (2026-06-16). https://www.ebn.co.kr/news/articleView.html?idxno=1712708
[4] THE ELEC — 포스코퓨처엠, '흑연 자립' 풀악셀… 새만금 공장 2027년 가동: bouw gestart, Q3 2027 oplevering, Q4 2027 opstart, Syrah Mozambique-contract tot 60 kt/j (2025-12-23). https://www.thelec.kr/news/articleView.html?idxno=50114
[5] KEDGlobal — POSCO Future M FID april 2025 voor Carbon New Materials Co. (spherical graphite, KRW 396 mrd) + $470m anode-contract met Amerikaanse autobouwer (2025). https://www.kedglobal.com/batteries/newsView/ked202504230002 · https://www.kedglobal.com/batteries/newsView/ked202510150003
[6] HKTDC Research — Zuid-Korea haalt ~93 % van zijn anodemateriaal uit China. https://research.hktdc.com/en/article/MTUzNTc1NTU0Mw
[7] mining.com.au — Syrah signs another ex-China offtake partner: 24 kt jaar 1 / 60 kt vanaf jaar 2, zes jaar. https://mining.com.au/syrah-signs-another-ex-china-offtake-partner/
[8] Interne atlasbron — `v2/data/stroomroute-pilot.json` + brief `grafiet-balama-vidalia.md` (been 1 Balama-plant → Nacala-containerterminal, 497,9 km, satelliet-gelegde ankers `gr-balama-mill`/`gr-nacala-kade`, ongewijzigd hergebruikt).
[9] Interne toets (ontwerpronde M29, 2026-09) — MARNET-zeeknoop 5638 (36,018, 126,4719) op 8,3 km van Gunsan New Port; Busan (5621, 9,8 km) en Pyeongtaek (5632, 10,4 km) even goed bereikbaar.
[10] Syrah Resources — September 2025 quarterly activities and cashflow report: breakbulk-verkoop 2025 naar Indonesië en de VS, POSCO niet genoemd. https://www.listcorp.com/asx/syr/syrah-resources-limited/news/september-2025-quarterly-activities-and-cashflow-report-3266566.html
[11] POSCO Future M — 회사소개/주요사업장: officiële adressen Sejong plant 1 (세종특별자치시 산단길 22-64) en plant 2 (세종특별자치시 소정면 매실로294). https://www.poscofuturem.com/introduce/directions.do
[12] OpenStreetMap (ODbL) via Nominatim (Osikdo-dong, Dong-Gunsan IC, Iksan-knooppunt, Nonsan-knooppunt) + Esri World Imagery via `v2/tools/sat_check.py` (z14–z16) — `v2/build-cache/satcheck/sat-grafiet-balama-saemangeum-gunsanport-overzicht.png`, `-gunsanport-detail.png`, `-gunsanport-kade.png`, `-blok56-overzicht.png`, `-blok6-west.png`, `-sejong-plant1.png`.


## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `grafiet-balama-saemangeum`** → `v2/data/stroomroute-grafiet-balama-saemangeum.json` — 6 benen, 13.397,1 km, 6.650 punten, 5 markers: truck 497,9 km · zee (stippel, aanloop Nacala) 152,1 km · zee 12.562,1 km · zee (stippel, aanloop Gunsan) 11,5 km · truck 3,9 km · truck 169,6 km.
Recept: `bak_stromen.sh` (functie `bak_grafiet_balama_saemangeum`). Profielen `grafiet-balama-saemangeum-gunsan-saemangeum` en `grafiet-balama-saemangeum-saemangeum-sejong` in `maak_stroombeen_weg.py`.

**b1 (truck, Balama → Nacala):** letterlijke kopie van been 1 `grafiet-balama-vs` (`stroombeen-balama-nacala.geojson`, 497,9 km, ongewijzigd) — geen nieuwe bake.

**b2 (zee, Nacala → Gunsan):** Nacala-kade snapt op 122,3 km van het zeenet — de bestaande `aanloop-nacala.geojson` (152,1 km, over water, hergebruikt uit `bak_grafiet`) is ervóór gezet, dezelfde als bij `grafiet-balama-laixi`. Aan de Koreaanse kant ligt de dichtstbijzijnde MARNET-zeeknoop (5643, 35,9991/126,6991) op 10,7 km van het Gunsan-anker — ruim binnen de 25 km-vrijstelling van de handleiding, maar boven de 5-10 km die de brief zelf als drempel noemde. Daarom is met `maak_havenaanloop.py` een korte haven-aanloop gebakken: 11,5 km over water, **0,00 km over land**, omwegfactor 1,074 — gekozen boven zeeknoop 5638 (10,99 km) omdat 5643 net iets dichterbij ligt. Beide aanlopen blijven gestippeld. Het hoofdzeebeen zelf is 12.562,1 km tegen de brief-schatting "~11.000 km, geen publicatie" (+14%) — geen harde toets (geen bron), maar wel een bevinding: de MARNET-route via de Straat Malakka en de Gele Zee loopt kennelijk ruimer dan de hemelsbrede aanname in de brief.

**b3 (truck, Gunsan-kade → Future Graph Saemangeum):** wegscan zonder via-punten (extract `zuid-korea`, profiel-lengtetoets 3,7 km tegen ~4 gepubliceerd = **−7,5%**, ruim binnen ±15%). Beide anker-verbindingen ≤ 0,12 km. De scanner vond een doorgaand pad over kleine wegklassen (residential/service/tertiary/unclassified, `eindToegangPrivaat`) — het perceel van blok 6 is dus (nog) niet volledig van het net afgesneden, ondanks dat de bouw pas begin 2026 startte; het been is **doorgetrokken**, niet gestippeld. De status van het eindanker blijft **onzeker** (brief §3) ongeacht deze geometrie.

**b4 (truck, Future Graph Saemangeum → POSCO Future M Sejong):** wegscan met de drie brief-via-punten (Dong-Gunsan IC → Iksan-knooppunt → Nonsan-knooppunt), extract `zuid-korea`, refs `15`/`25`/`21` als zachte voorkeur. Lengte 169,5 km getekende weggeometrie tegen de brief-schatting 180 km (zelf geen onafhankelijke bron) = **−5,9%**. Alle vier via-snaps 0,00–0,03 km — geen enkel via-punt lag naast de bedoelde weg. 18 keerlussen gesnoeid (dubbel gereden stukjes, netto 0,0 km verschil).

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **Geen enkele naad > 5 km** — alle 6 opeenvolgende benen sluiten op 0,000 km aan (inclusief beide haven-aanlopen).
- **Alle 5 markers liggen exact op hun lijn** (0,0 m) — elk anker uit §3 is ook het begin- of eindpunt van het bijbehorende been.
- **2 terugloop-punten** (`toets_knikken.py`) op been b4, allebei rond het Dong-Gunsan IC-via-punt (35,9452/126,8342 — TERUGLOOP op 35,94520/126,83419 en 35,94864/126,83455, v-verhouding 6,1–7,3). Dit is het bekende overschiet-en-terug-patroon van een via-punt op een knooppunt (`decisions.md`, "een knooppunt-via ligt ná de afslag, niet op het kruis"): de scanner snapt op de dichtstbijzijnde rijbaanvertex bij de op-/afrit, niet op de doorgaande hoofdrijbaan. Niet gerepareerd door het via-punt te verschuiven (zou de km-toets kunnen laten "slagen" zonder de oorzaak weg te nemen) — blijft staan als bevinding. Overige knikken op b4 (23 totaal, 1 "scherpe bocht, echt" bij Iksan) zijn OSM-spikes op kleine wegklassen, geen sluipweg.
- **b2 is 14% langer dan de brief-schatting** (zie hierboven) — geen harde toets omdat de brief zelf geen publicatie heeft, maar het verschil is groot genoeg om te noteren.
- `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom in de verdachtenlijst (geen rechte lijn ≥5 km met omwegfactor ≈1,000) — ook de nieuwe Gunsan-aanloop (omwegfactor 1,074, 7 punten) claimt terecht geen rechte kennis.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, zee} (beide toegestaan), elk been ≥ 2 punten, bestand 133,1 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:** de dichtstbijzijnde MARNET-zeeknoop bij een kade kán binnen de 25 km-vrijstelling vallen en toch een eigen (korte) haven-aanloop verdienen als de brief zelf een strengere drempel noemt (hier 5-10 km) — de 25 km uit de handleiding is een bovengrens, geen vrijbrief om een aanloop van 10-11 km over te slaan. Verder: twee haven-aanlopen in één stroom (Nacala hergebruikt, Gunsan nieuw) zijn probleemloos te combineren in reisvolgorde zonder dat de naad-toets iets bijzonders laat zien.
