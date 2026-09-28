# Routebrief (licht) · koper — Van → Via → Naar (land)

**stroom-id:** `koper-aktogay-jinchuan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** Kazachs koperconcentraat van de Aktogay-mijn (KAZ Minerals, Abai-regio) reist over de
historische Turksib-spoorlijn en de grensovergang Dostyk/Alashankou (1990, breukspoor 1520↔1435 mm) naar een
Chinese smelter — aannemelijk Jinchuan in Jinchang (Gansu) via de Lanzhou-Xinjiang-spoorlijn (Tweede
Euraziatische Landbrug) — een pure spoorketen zonder zee, net als Oyu Tolgoi→Feishang.
**Welke as van het verhaal:** Tweede Centraal-Aziatische spoor-as naast Oyu Tolgoi–Feishang. Aktogay produceerde
in 2024 **229 kt Cu totaal** (KAZ Minerals Q4 2024-productierapport), waarvan ≈18 kt als SX-EW-kathode en
**≈211 kt als concentraat** uit de sulfide-concentrator — hier gemodelleerd op de dominante concentraatstroom.

## 1 · Ketenkaart
Aktogay-mijn/concentrator `cu-aktogay-laad` ──(b1 spoor · Turksib-hoofdlijn · ~250 km hemelsbreed)──►
Dostyk-grensstation `cu-aktogay-grens` (KZ) ──(grensdoorlaat Dostyk/Alashankou, 1990)──►
Alashankou (CN, via-punt) ──(b2 spoor · Lanzhou-Xinjiang-lijn via Jinghe–Ürümqi–Hami–Wuwei · geen gepubliceerde km)──►
smelter Jinchuan, Jinchang `cu-jinchuan-smelter` (aannemelijk: smelterkeuze niet cargo-specifiek gebrond, Xinjiang-
alternatief afgewogen) ⏹ stoppunt

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `cu-aktogay-laad` → `cu-aktogay-grens` | Turksib-hoofdlijn (Aktogay = historisch Turksib-spoorknooppunt; de aftak naar Dostyk is in 1959 aangelegd op Sovjet-Chinese afspraken uit 1956) [2] | ~250 hemelsbreed [1]; geen aparte gepubliceerde spoor-km | toets_spoorroute (BAKE_SUFFIX=-raw, extract kazachstan) | nee |
| b2 | A | spoor | `cu-aktogay-grens` → `cu-jinchuan-smelter` | grensdoorlaat Dostyk/Alashankou (verbonden 1990, "Ürümqi–Dostyk–Aktogay–Sayak–Balqash–Moyynty"-brug [2]) → Lanzhou-Xinjiang-spoorlijn (Lanxin, Tweede Euraziatische Landbrug) via Jinghe–Ürümqi–Hami–Wuwei | geen gepubliceerde spoor-km voor dit traject; ~1.780 km hemelsbreed (berekend, Alashankou→Jinchang) | toets_spoorroute (BAKE_SUFFIX=-raw, extract china; meerdere runs kop→via→via…→staart vanwege de landsgrens en de netextractie, patroon uranium-inkai-poti / koper-oyutolgoi-feishang) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-aktogay-laad` | mijn/concentrator (laadplek) | Aktogay-mijn + concentrator (KAZ Minerals), Abai-regio | 46.9570, 79.9263 | Nominatim "ГОК Актогай" [webcheck haalbaarheidstoets], getoetst tegen `v2/build-cache/raw1op1/kazachstan.geojson` (0,24 km van het spoor) | bron-gelegd (z15 gezien: complex met blauwe loodsdaken, opslagterrein en wegverharding direct naast de spoorlijn — bevestigt de gemeten 0,24 km spoorafstand; verfijning t.o.v. de bestaande sitelaag-entry 46.95/79.86, die op de grovere Wikipedia-geohack steunt) |
| `cu-aktogay-grens` | grensovergang / breukspoorterminal (KZ) | Dostyk-spoorstation, Jetisu-regio | 45.2540, 82.4855 | Wikipedia "Dostyk railway station" [3] | bron-gelegd (z14 gezien: rangeeremplacement met meerdere evenwijdige sporen, stationsgebouw en de bebouwde kom Dostyk aan weerszijden van de lijn; de Chinese poort Alashankou ligt ~9 km ZO) |
| `cu-jinchuan-smelter` | losplek / smelter (stoppunt) | Jinchuan Group, Jinchang (Gansu) | 38.5210, 102.1850 | Wikipedia "Jinchang" [8]; komt overeen met `cu-ref-jinchuan` in `data/copper.js` en `w-jinchuan-jinchang` in `v2/design/nikkel-sitelaag.json` | aannemelijk (z13 gezien: stedelijk gebied met spoorwegemplacement en industriebebouwing ten oosten van de kern; het exacte fabrieksterrein is op dit schaalniveau niet af te bakenen — zelfde beperking als al vastgesteld in de nikkel-sitelaag) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Alashankou-grensstation (CN) | 45.1703, 82.5703 | pint de grensdoorgang/breukspoorterminal aan Chinese zijde, direct na Dostyk |
| b2 | 2 | Jinghe (spoorstation op de Lanxin-lijn) | 44.6000, 82.9000 | pint de Lanxin-hoofdlijn oostwaarts i.p.v. een lokale aftakking bij de grens |
| b2 | 3 | Ürümqi (spoorknoop) | 43.8225, 87.6125 | pint de doorgaande Lanxin-lijn i.p.v. de Zuid-Xinjiang-lijn naar Korla/Kashgar |
| b2 | 4 | Hami-spoorstation | 42.8484, 93.5045 | pint de ingang van de Hexi-corridor (Gansu) i.p.v. een zuidelijker tracé |
| b2 | 5 | Wuwei (spoorstad, ~50 km NW van Jinchang) | 37.9290, 102.6380 | laatste corridorpunt vóór de aftakking naar Jinchang op de Lanxin-hoofdlijn |

`cu-aktogay-laad → cu-aktogay-grens` (b1) heeft geen via-punten: de lijn is een enkele historische aftakking
(1959, geen gedocumenteerd alternatief tracé).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Jinchuan-smelter, Jinchang | Jinchuan Group | koperconcentraat → ruwkoper/kathode (aannemelijk) | geen onafhankelijk gepubliceerde koper-smeltcapaciteit gevonden (Jinchuan is vooral bekend als nikkelproducent; `data/copper.js` noemt de site alleen kwalitatief) | [8][9][10] |

## 6 · Stoppunt
De brief stopt bij de Jinchuan-smelter in Jinchang: die is de enige in de bestaande koperlaag (`data/copper.js`)
die al Centraal-Aziatisch/Mongools materiaal over land verwerkt, maar geen bron noemt Jinchuan specifiek als
koper van Aktogay-concentraat — dit blijft dus expliciet **aannemelijk**, conform de haalbaarheidstoets. Fase D
(afzet van het Jinchuan-product) vervalt: geen bron noemt een specifieke volgende fabriek.

## 7 · Open punten
- **Smelterkeuze niet cargo-specifiek gebrond.** KAZ Minerals noemt alleen "China is main sales market" en
  "transport by rail" [1]; een Xinjiang-smelter dichter bij de grens (bijv. in de Ürümqi- of Hami-industriezone)
  is een reëel alternatief dat bij het bakken gecheckt moet worden (haalbaarheidstoets-risico).
- **Geen gepubliceerde spoor-km voor b2.** Het Alashankou–Jinchang-traject (~1.780 km hemelsbreed) heeft geen
  onafhankelijk gepubliceerde lengte; de bake-toets loopt tegen het 1-op-1-net.
- **Breukspoor-terminal niet exact gelokaliseerd.** Dostyk/Alashankou is de bekende 1520↔1435 mm-overslag
  (bogiewissel of overlading), maar geen bron geeft een precieze coördinaat van de overslaghal zelf — het anker
  staat op het Dostyk-spoorstation.
- **Twee productvormen in de 229 kt.** Concentraat (≈211 kt) en SX-EW-kathode (≈18 kt) lopen door elkaar in de
  KAZ Minerals-cijfers; deze brief modelleert bewust alleen de dominante concentraatstroom.
- **Jinchuan-koper-capaciteit onbekend.** Geen bron geeft een koper-smeltcapaciteit voor de Jinchang-site
  (Jinchuan is vooral een nikkelproducent); §5 blijft daarom leeg op dit punt.

## 8 · Bronnen
[1] Wikipedia (en), "Aktogay mine": KAZ Minerals, open pit + concentrator, Abai-regio, "approximately 250 km from Kazakhstan-China border" — https://en.wikipedia.org/wiki/Aktogay_mine
[2] Wikipedia (en), "Aktogay, East Kazakhstan Region": "major railway hub of Turkestan-Siberian Railway"; spoorlijn naar Dostyk gebouwd 1959 op de Sovjet-Chinese accoorden van 1956; verbinding met China bij de Alataw-pas in 1990, brug "Ürümqi–Dostyk–Aktogay–Sayak–Balqash–Moyynty" — https://en.wikipedia.org/wiki/Aktogay,_East_Kazakhstan_Region
[3] Wikipedia (en), "Dostyk railway station": coördinaat 45.253978/82.48548, grensstation KZ-CN — https://en.wikipedia.org/wiki/Dostyk_railway_station
[4] Wikipedia (en), "Dostyk": stad aan de grens met Xinjiang, coördinaat 45.25333/82.48444 — https://en.wikipedia.org/wiki/Dostyk
[5] Wikipedia (en), "Alashankou railway station": coördinaat 45.17028/82.57028 — https://en.wikipedia.org/wiki/Alashankou_railway_station
[6] Wikipedia (en), "Alashankou": grensstad, poort van zowel spoor als weg vanuit Kazachstan, onderdeel Eurasian Land Bridge — https://en.wikipedia.org/wiki/Alashankou
[7] Wikipedia (en), "Turkestan–Siberia Railway": beschrijving van de Turksib-hoofdlijn (Arys–Shymkent–Taraz–Almaty–Semey–Novosibirsk) — https://en.wikipedia.org/wiki/Turkestan%E2%80%93Siberia_Railway
[8] Wikipedia (en), "Jinchang": prefecture-level stad in Gansu, coördinaat 38.5214/102.188 — https://en.wikipedia.org/wiki/Jinchang
[9] `v2/data/copper.js`, node `cu-ref-jinchuan`: "Jinchuan (Jinchang), Gansu; verwerkt o.a. het Mongoolse Oyu Tolgoi-concentraat over land", lat 38.50/lon 102.19 — intern projectbestand
[10] `v2/design/nikkel-sitelaag.json`, site `w-jinchuan-jinchang`: coördinaat 38.521/102.185, status "aannemelijk" met noot dat het feitelijke mijn-/smeltercomplex in de oostelijke industriezone ligt — intern projectbestand
[11] `v2/design/koper-sitelaag.json`, site `w-aktogay`: 229 kt Cu 2024 (waarvan 18 kt SX-EW-kathode), bron "KAZ Minerals Q4 2024 production report" — intern projectbestand
[12] Wikipedia (en), "Ürümqi": coördinaat 43.8225/87.6125 — https://en.wikipedia.org/wiki/%C3%9Cr%C3%BCmqi
[13] Wikipedia (en), "Hami railway station": coördinaat 42.84836/93.5045 — https://en.wikipedia.org/wiki/Hami_railway_station
[14] Wikipedia (en), "Wuwei, Gansu": coördinaat 37.929/102.638 — https://en.wikipedia.org/wiki/Wuwei,_Gansu
[15] Wikipedia (en), "Jinghe County": coördinaat 44.60/82.90 — https://en.wikipedia.org/wiki/Jinghe_County

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `koper-aktogay-jinchuan`** → `v2/data/stroomroute-koper-aktogay-jinchuan.json` — 7 benen, **2.538,2 km**,
3.674 punten, 3 markers, uitsluitend spoor. Recept: `bak_stromen.sh` (functie `bak_koper_aktogay_jinchuan`).

**b1 (spoor, Aktogay-mijn → Dostyk-grensstation, KZ, Turksib-hoofdlijn):**
`BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=46.9570,79.9263 --naar=45.2540,82.4855
--naam=koper-aktogay-jinchuan-aktogay-dostyk` (1-op-1-net, console bevestigt "3260717 spoor-edges", geen
via-punt — enkele historische aftakking uit 1959). **332,1 km over 150 edges, grootcirkel 273,4 km, verhouding
1,21.** Geen gepubliceerde spoor-km om tegen te toetsen (brief §7, alleen ~250 km hemelsbreed) — dit is nieuwe
informatie, geen normtoets. Twee spike-punten opgeruimd (OSM-zigzag); **2 bochten ≥60° na de keerstraf**, beide
vlak bij de laadplek (46,96/79,69, ~18 km ten westen van het Aktogay-anker) — plausibel een spur/keerlus bij het
mijncomplex vóórdat de trein op de doorgaande Turksib-lijn oostwaarts naar Dostyk gaat.

**b2 (spoor, Dostyk → Jinchuan-smelter, CN, Lanxin-hoofdlijn, 6 aparte runs kop→via→via…→staart):**
Zelfde tool/vlaggen per stuk (extract `china`, geen via-vlag op de spoorrouter — patroon
koper-oyutolgoi-feishang / uranium-inkai-poti):

| run | van → naar | km | edges | grootcirkel | verhouding |
|---|---|---|---|---|---|
| Dostyk → Alashankou-grensstation | 45.2540,82.4855 → 45.1703,82.5703 | 13,3 | 24 | 11,4 | 1,16 |
| Alashankou-grensstation → Jinghe | 45.1703,82.5703 → 44.6000,82.9000 | 115,5 | 125 | 68,5 | 1,67 |
| Jinghe → Ürümqi | 44.6000,82.9000 → 43.8225,87.6125 | 410,7 | 380 | 385,4 | 1,06 |
| Ürümqi → Hami-spoorstation | 43.8225,87.6125 → 42.8484,93.5045 | 540,6 | 303 | 488,6 | 1,10 |
| Hami-spoorstation → Wuwei | 42.8484,93.5045 → 37.9290,102.6380 | 1.021,4 | 639 | 946,5 | 1,08 |
| Wuwei → Jinchuan-smelter | 37.9290,102.6380 → 38.5210,102.1850 | 104,6 | 140 | 76,8 | 1,34 |

b2-totaal **2.206,1 km** tegen ~1.780 km hemelsbreed Alashankou→Jinchang (brief §7) = **+24,0%**, buiten ±15% —
**bevinding, niet dichtgetrokken**: er is geen gepubliceerde spoor-km voor dit traject (alleen een hemelsbreed-
schatting tegen een reëel gebogen 1-op-1-spoortracé door de Hexi-corridor), dus de norm is hier zwak (conform de
bak-aanwijzing in de opdracht: "vooral op geen-naad->5-km letten"). De Dostyk→Alashankou- en
Alashankou→Jinghe-runs delen dezelfde 166,8°/171,4°/174,0°-omkeerpunten rond de grensdoorlaat (zie
`toets_knikken.py` hieronder) — dat is de breukspoor-overslag zelf, geen routeerfout.

**Toets naden (alle 7 benen, kop→staart in reisvolgorde):** elke opeenvolgende snap komt op exact dezelfde
knoop-id met exact dezelfde snap-afstand uit (bv. Ürümqi-knoop 531352 op 3,89 km in zowel de staart van
`jinghe-urumqi` als de kop van `urumqi-hami`; Wuwei-knoop 700565 op 3,11 km in beide aangrenzende runs) —
**alle 6 naden 0,000 km** (python-naadscript uit de handleiding §5). Geen enkele naad > 5 km, dus geen
haven-aanloop of ander lapmiddel nodig — dit is een pure spoorketen zonder zee (brief, `bak_aanwijzingen`).

**`toets_knikken.py`:** 8 knikken ≥60° over de hele keten, waarvan 8 omkeringen ≥150°, waarvan **5 TERUGLOOP**
(pad/hemelsbreed-verhouding wijst op een lijn die ter plaatse blijft i.p.v. een echte bocht maakt) — bevinding,
niet gerepareerd (geen via-punt bijschuiven om dit weg te toetsen, bakhandleiding §5/§6):
- b1: 180,0° bij 46,9635/79,6897 (R~0 m) **TERUGLOOP** + 175,2° bij 46,9577/79,6852 (R~30 m, "scherpe bocht,
  echt") — beide bij de mijnzijde, ~18 km ten westen van het Aktogay-anker, plausibel het mijnspoor/de spur
  vóór de doorgaande Turksib-lijn.
- b2 dostyk→alashankou: 166,8° bij 45,1651/82,5720 (R~28 m, "scherpe bocht, echt") — de grensdoorlaat zelf.
- b2 alashankou→jinghe: 174,0° bij 44,6387/83,0133 (R~32 m) **TERUGLOOP** + 171,4° bij 45,2682/82,4693 (R~17 m)
  **TERUGLOOP**, dit laatste punt ligt vrijwel bovenop het Dostyk-anker (45,2540/82,4855) — de spoorrouter kiest
  hier een pad dat via de grensovergang terugschakelt, plausibel de breukspoor-overslag/rangeerbeweging
  (1520↔1435 mm bogiewissel) waar de brief zelf al op wijst (§2, "grensdoorlaat Dostyk/Alashankou") + 166,8°
  bij 45,1651/82,5720 (dezelfde grensdoorlaat-bocht als hierboven, "scherpe bocht, echt").
- b2 hami→wuwei: 180,0° bij 39,7682/98,2507 (R~0 m) **TERUGLOOP** + 178,2° bij 39,7188/98,3038 (R~51 m)
  **TERUGLOOP** — beide rond lon 98,25-98,30/lat 39,7, dat is de Jiayuguan-regio op de Hexi-corridor tussen Hami
  en Wuwei; plausibel een yard-/aansluitpunt op de Lanxin-hoofdlijn, niet nader onderzocht binnen deze lichte bake.
- b2 jinghe→ürümqi, ürümqi→hami, wuwei→jinchuan: **0 knikken, 0 omkeringen**.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — alle 7 benen zijn over het
1-op-1-net gerouteerd (geen stippel), dus er is geen "rechte lijn die kennis claimt die de kaart niet heeft".

**json geldig:** versie 2, punt_formaat lonlat, modaliteit uitsluitend {spoor} (binnen de toegestane set), elk
been ≥2 punten (minimum 39), bestandsgrootte **66,1 KB** (ruim < 300 KB-richtwaarde).

**Markers:** `cu-aktogay-laad` 0 m (exacte kop van b1) · `cu-aktogay-grens` 0 m (exacte naad tussen b1-staart en
de eerste b2-run — dezelfde snap-knoop aan beide kanten) · `cu-jinchuan-smelter` ~2,15 km (anker ≠ routeerpunt —
de laatste spoorrouter-run snapt op zijn dichtstbijzijnde hoofdnet-knoop 737187, 2,15 km van het Jinchuan-anker;
de smeltersite zelf ligt op stadsniveau, conform brief §3 "exact fabrieksterrein niet af te bakenen op dit
schaalniveau"). Ruim binnen de ~0,5 km-norm voor de eerste twee, de derde is expliciet *anker ≠ routeerpunt*.

**Geen zee, geen haven-aanloop:** deze keten is bewust een pure spoorketen (brief, `keten_in_een_zin`) — geen
zeebeen, dus de LAR-586-haven-aanloopregel is niet van toepassing.

**Open punten die blijven staan (zie ook §7):** de smelterkeuze Jinchuan blijft aannemelijk (geen bron noemt
Jinchuan specifiek als koperafnemer van Aktogay-concentraat — een Xinjiang-smelter dichter bij de grens is een
reëel alternatief, niet nader gecheckt binnen deze lichte bake); geen gepubliceerde spoor-km voor b1 of b2 (nu
vervangen door de gemeten 332,1 + 2.206,1 km); de breukspoor-terminal Dostyk/Alashankou is niet exact
gelokaliseerd op de overslaghal zelf; geen fase D/E (§6, geen bron noemt een vervolgfabriek of een
koper-smeltcapaciteit voor Jinchuan).

**Gereedschapslessen:**
- De `--been-geojson`-bestandsnaam die `toets_spoorroute.mjs` zelf schrijft is `spoorroute-<naam>.geojson`
  (de `--naam=`-vlag), NIET `<naam>.geojson` — de eerste bake-poging faalde op "bestand niet gevonden" omdat de
  functie in `bak_stromen.sh` de `spoorroute-`-prefix miste. Fix: `$BEEN/spoorroute-<stroom-id>-<van>-<naar>.geojson`
  in elke `--been-geojson`-regel, consistent met hoe de andere lichte brieven (uranium-inkai-poti,
  koper-elteniente) dit al doen.
- Een pure spoorketen zonder zee/weg is de eenvoudigste lichte bake: geen zeeknoop-lookup, geen haven-aanloop,
  geen wegprofiel in `maak_stroombeen_weg.py` — alleen de spoorrouter, per corridorkeuze een aparte run,
  kop→staart-naad geverifieerd via identieke snap-knoop-ids tussen opeenvolgende runs.
- `toets_knikken.py`'s TERUGLOOP/scherpe-bocht-onderscheid (pad/hemelsbreed-verhouding) is op een
  grensovergang met breukspoor bijzonder nuttig: de omkeringen bij Dostyk/Alashankou zijn plausibel de
  bogiewissel-rangeerbeweging zelf, niet een routeerfout — maar dat blijft een interpretatie, geen bewijs, en is
  daarom als bevinding opgeschreven in plaats van als opgelost.
