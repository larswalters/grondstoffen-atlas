# Routebrief (licht) · uranium — Elemash Elektrostal (Rusland) → Zabaikalsk/Manzhouli → CFR-600, Xiapu (China, peiljaar 2022)

**stroom-id:** `uranium-elektrostal-xiapu` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) ·
**status:** gebakken
**Keten in één zin:** splijtstof voor de snelle reactor CFR-600 gaat in drie zendingen (sept., nov., dec. 2022) per **spoor** uit de
TVEL-fabriek Elemash in Elektrostal (aannemelijk: oostwaarts via Kazan naar Jekaterinenburg, dan Trans-Sib tot Borzya en de grens
Zabaikalsk/Manzhouli, dan door China via Tianjin en Hangzhou over de Wenfu-lijn naar Xiapu) en over een korte weg naar de reactor
op Changbiao-eiland — **stoppunt**: de reactor. Regelstaven gingen per vliegtuig (niet getekend).
**Welke as van het verhaal:** *Russische splijtstof voor een Chinese snelle reactor: de Rusland-China-nucleaire as buiten het VVER-verhaal.*
Volume: **onbekend**. Eenmalig, drie spoorzendingen met de eerste kern plus de eerste herlading [1][2]; geen tonnage gepubliceerd [3][4].
Derde-partij-indicatie 7,6 t U in de kern (BN-600-analogie, geen bron, niet bevestigd) [4]. Eenheid t U, peiljaar 2022.

## 1 · Ketenkaart
```
Elemash, Elektrostal `u-elemash` ──(b1 spoor · oostwaarts via Kazan, niet via Kirov/Perm · router 1.618 km, hemelsbreed 1.365 ·
   aannemelijk: bron noemt alleen "per spoor uit Elektrostal")──► Jekaterinenburg-knoop
──(b2-b9 spoor · Trans-Sib Tyumen–Omsk–Novosibirsk–Krasnoyarsk–Irkutsk–Ulan-Ude–Chita–Borzya · 4.673 km router · letterlijke kopieën)──►
Borzya ──(b10 spoor · 126 km)──► Zabaikalsk/Manzhouli-emplacement `u-manzhouli-overslag` (spoorwijdteovergang 1520 → 1435 mm)
──(b11 spoor · Hailar–Jinzhou–Tianjin–Hangzhou–Wenzhou–Fuding · 3.537 km router, aannemelijk)──► Xiapu-station `u-xiapu-station`
──(b12 truck, stippel 17,5 km · last mile)──► CFR-600, Changbiao `u-cfr600` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | spoor | Elemash → Jekaterinenburg-knoop | Kazan (6 km), Izjevsk-streek (33 km); router rijdt NIET via Moskou, Kirov of Perm | hemelsbreed 1.365, geen spoorkm; router 1.618,0 | toets_spoorroute (1 run, -raw) | nee — *aannemelijk: één bron* |
| b2 | D | spoor | Jekaterinenburg → Tyumen | Trans-Sib noordroute | router 316 | kopie tricastin-seversk | nee |
| b3 | D | spoor | Tyumen → Omsk | idem | router 567,6 | kopie tricastin-seversk | nee |
| b4 | D | spoor | Omsk → Novosibirsk | idem | router 617,5 | kopie tricastin-seversk | nee |
| b5-b9 | D | spoor | Novosibirsk → Krasnoyarsk → Irkutsk → Ulan-Ude → Chita → Borzya | Trans-Sib om het Baikalmeer; **omgekeerd** van priargunsky-seversk | router 758,9 + 1.075,8 + 451,4 + 544,9 + 340,5 | kopie priargunsky-seversk, omgekeerd | nee |
| b10 | D | spoor | Borzya → Manzhouli-emplacement | Borzya–Zabaikalsk–Manzhouli; router passeert Zabaikalsk op 0,3 km | router 126,2 (hemelsbreed 110) | toets_spoorroute (-raw) | nee — *aannemelijk: grensovergang niet genoemd* |
| b11 | D | spoor | Manzhouli → Xiapu-station | Hailar, Jinzhou, Tianjin, Hangzhou, Wenzhou, Fuding; niet via Harbin, Shenyang of Beijing (97-288 km ernaast) | hemelsbreed 2.530, geen spoorkm; router 3.536,9 | toets_spoorroute (1 run, -raw) | nee — *aannemelijk: Chinees traject niet genoemd* |
| b12 | D | truck | Xiapu-station → CFR-600 | last mile, geen net op deze korrel (dam naar het eiland, geen OSM-pad gemeten) | hemelsbreed 17,5; geen wegkm | stippel | **ja — net reikt niet** |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-elemash` | fabriek (kop) | TVEL Elemash Machine-Building Plant, Elektrostal | 55.7875, 38.4875 | letterlijk uit `uranium-elektrostal-paks.md` [8] | bron-gelegd (z15 gezien: ommuurd industrieterrein met een grote fabriekshal en bijgebouwen in bos, rondom een hekwerk; welke hal splijtstof maakt niet te zien). Sitelaag `w-tvel-elektrostal` ligt 3,4 km westelijker |
| `u-manzhouli-overslag` | grensovergang, spoorwijdtewissel | Manzhouli-emplacement (routepunt, Zabaikalsk-zijde 14 km noordwest) | 49.5829, 117.4165 | eigen router-eindpunt; stad 49°35'53"N 117°22'44"E [6] | bron-gelegd (z16 gezien: groot spoorcomplex met meerdere rangeersporen, lange loodsen, kranen en containerstapels; 0,64 km van het ontwerppunt 49.5774, 117.4193). De wijzigingsoverslag zelf ligt volgens [5][6] aan de Russische kant, Zabaikalsk (49.6514, 117.3269), niet apart gelegd |
| `u-xiapu-station` | overslag spoor → weg | Xiapu-station (霞浦站), Fujian | 26.9127, 120.0282 | OSM-station (Nominatim) [7] | bron-gelegd (z15/z16 gezien: tweesporige lijn met lange perrons oostelijk en een stationsplein met parkeerterrein; router-eind 0,45 km west op de lijn, 26.9137, 120.0238). Of dit het spoorhoofd van de bron is, noemt geen bron |
| `u-cfr600` | reactor (eindpunt) | CFR-600, Changbiao-eiland, Xiapu | 26.8036, 120.1550 | Wikipedia 26°48'13"N 120°09'18"E [9] | bron-gelegd (z15 gezien: compact complex met witte hallen en bijgebouwen op een door dijken omgeven eiland, een dam met weg naar het vasteland in het zuidwesten) |

## 4 · Via-punten (router-knopen; alleen waar een corridorkeuze bestaat)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | – | geen via-punt; eindpunt Jekaterinenburg-knoop | 56.8381, 60.6344 | de router kiest zelf de Kazan-corridor (1.618 km); een via-punt zou terug door Moskou sturen. Twee router-omkeringen 55.7334, 38.4704 en 55.7609, 38.9723 (niet bijgeschoven) |
| b2-b9 | – | knopen van de kopieën: Tyumen 57.1455, 65.5221 · Omsk 54.9396, 73.3866 · Novosibirsk 55.0186, 82.9207 · Krasnoyarsk 56.0134, 92.8351 · Irkutsk 52.2897, 104.2599 · Ulan-Ude 51.8309, 107.5957 · Chita 52.0371, 113.4539 · Borzya 50.3828, 116.5197 | – | letterlijk uit de kopiebestanden; Tyumen-noordroute i.p.v. Kurgan–Petropavl (Kazachstan) is daar al vastgelegd |
| b10, b11 | – | geen via-punten | – | één run per been; b11 mijdt Beijing en Harbin vanzelf; splitsen alleen als de bake een omkering of een omweg toont |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Elemash | TVEL / Rosatom | uraniumoxide → splijtstofassemblages (voor CFR-600 uranium-, geen MOX-brandstof geleverd [4]) | ≈ 1.200 t HM/j, indicatie sitelaag alle TVEL-klanten | [3][8] |
| CFR-600 | CNNC | splijtstof → 600 MWe snelle reactor, eerste herladingen onder het contract | 600 MWe; contract dekt eerste kern en herladingen eerste zeven jaar [1] | [1][9] |

## 6 · Stoppunt
De brief stopt bij de reactor: één bron noemt zowel de fabriek (Elemash) als de afnemer (CFR-600) en de modaliteit spoor [1][2]. Fase E vervalt.
Fase D is hier de hele keten; geen bron noemt een vervolgbestemming van de brandstof.

## 7 · Open punten
- **Alleen paar, spoor en jaar zijn bron-gelegd:** grensovergang (Zabaikalsk/Manzhouli, Alashankou mogelijk), Chinese corridor en Xiapu-spoorhoofd zijn aannemelijk [1][2][5].
- **Corridor Rusland:** de ontwerpcorridor (Jaroslavl–Kirov–Perm) liep terug door Moskou; de router kiest de zuidelijke lijn via Kazan, 1.618 km. De haalbaarheidstoets noemt Nizjni Novgorod, maar de lijn passeert die stad op 88 km.
- **Geen spoorkm gepubliceerd:** de ±15%-toets is indicatie. Router: b1 1.618, b10 126, b11 3.537, kopieën 4.673 km; totaal ≈ 9.954 km spoor, ≈ 53% nieuw.
- **Chinese corridor wijkt af van het ontwerp:** niet Harbin–Shenyang–Beijing maar Hailar–Jinzhou–Tianjin–Hangzhou; Wenfu-lijn Wenzhou–Fuding–Xiapu. Geen bron noemt een van beide.
- **Last mile 17,5 km hemelsbreed (stippel), geen wegkm;** een weg over de dam naar Changbiao is op de satelliet te zien, maar niet als openbare weg gemeten.
- **Spoorwijdteovergang** ligt volgens Wikipedia aan de Russische kant (Zabaikalsk) [5]; de keten kruist de grens ongesplitst, het overslagpunt is niet apart gelegd.
- **Regelstaven per vliegtuig** [1]: luchthavens niet genoemd, dus niet getekend.
- **Sitelaag:** `w-tvel-elektrostal` (55.7833, 38.4333) ligt 3,4 km van `u-elemash`; centraal gelijktrekken. Een CFR-600-site staat niet in de sitelaag.
- **Volume:** geen tonnage; de 7,6 t U is een BN-600-analogie van een derde partij [4], geen levering.

## 8 · Bronnen
[1] World Nuclear News, 2023-01-04, "Fuel load for Chinese fast reactor dispatched from Russia" — drie zendingen per spoor uit Elemash sinds eind september 2022, regelstaven per vliegtuig, contract eerste kern plus herladingen. https://www.world-nuclear-news.org/Articles/Fuel-for-Chinese-fast-reactor-dispatched-from-Russ
[2] WISE Uranium, Enrichment/fuel Russia — Rosatom-bericht 28-12-2022, TVEL alle zendingen voor 2022, drie partijen per spoor uit Elemash. https://www.wise-uranium.org/eopru.html
[3] WISE Uranium, id. — Elemash-capaciteit (2003-projectie), geen jaarcijfer. https://www.wise-uranium.org/eopru.html
[4] FFMSG/fissilematerials.org, 2022-12 — drie zendingen sept./nov./dec. 2022, uranium-brandstof, kernmassa ~7,6 t (analogie, geen bron). https://fissilematerials.org/blog/2022/12/russia_delivers_fuel_for_.html
[5] Wikipedia, "Zabaykalsk" — grenszone met Manzhouli, spoorwijdtewissel; 49°39'05"N 117°19'37"E. https://en.wikipedia.org/wiki/Zabaykalsk
[6] Wikipedia, "Manzhouli" — drukste landpoort van China, 49°35'53"N 117°22'44"E, 1435/1524 mm. https://en.wikipedia.org/wiki/Manzhouli
[7] OSM Nominatim — Xiapu railway station 26.9127474, 120.0282365 (ODbL). https://nominatim.openstreetmap.org/search?q=Xiapu+railway+station&format=json
[8] Eigen briefs: `uranium-elektrostal-paks.md` (u-elemash letterlijk, Elemash-capaciteit), `uranium-tricastin-seversk.md` (b2-b4 geojsons), `uranium-priargunsky-seversk.md` (b5-b9 geojsons, omgekeerd).
[9] Wikipedia, "CFR-600" — Changbiao-eiland, Xiapu, 26.8036, 120.1550, TVEL-contract 2019. https://en.wikipedia.org/wiki/CFR-600
[10] NucNet, 2022-10-07, "TVEL delivers first batch of fuel for China's CFR-600" — eerste batch, assemblages uit Elemash, brandstoftype niet gespecificeerd. https://www.nucnet.org/news/russia-s-tvel-delivers-first-batch-of-fuel-for-china-s-cfr-600-demonstrator-10-5-2022
[sat] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-uranium-elektrostal-xiapu-{elemash,manzhouli,manzhouli-yard,xiapu-station,xiapu-spoor,cfr600}.png`.
Routetoets (router, -raw): `v2/build-cache/ais/graaf/spoorroute-uranium-elektrostal-xiapu-{elemash-jekaterinenburg,borzya-manzhouli,manzhouli-xiapu}.geojson` en de vijf omgekeerde kopieën `…-{novosibirsk-krasnoyarsk,krasnoyarsk-irkutsk,irkutsk-ulanude,ulanude-chita,chita-borzya}-omgekeerd.geojson` (alle al aangemaakt).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)

**Stroom `uranium-elektrostal-xiapu`** → `v2/data/stroomroute-uranium-elektrostal-xiapu.json` (392,8 KB): 12 benen, 10.051,6 km, 21.821 punten, 4 markers. Spoor 10.033,7 km (11 doorgetrokken benen), truck-stippel 17,9 km. Alle 11 naden 0,000 km (gedeelde knoop-eindpunten); de stippel begint op het router-eind van b11.
Recept: `bak_stromen.sh`, functie `bak_uranium_elektrostal_xiapu` (geen wegprofiel, geen wegscan, geen zee, haven, vlucht of leiding). Alle spoorbenen zijn vooraf gebakken geojsons in `v2/build-cache/ais/graaf/` (toets_spoorroute, BAKE_SUFFIX=-raw) en gaan als `--been-geojson "spoor|…"` rechtstreeks de functie in. Bake in één run via het zwaar-slot.

Toelichting per been.
- **b1** (spoor): Elemash naar Jekaterinenburg-knoop, 1.632,9 km (router 1.618,0), 4.361 punten; router kiest zelf Kazan; geen gepubliceerde spoorkm, dus alleen indicatie. Doorgetrokken; "aannemelijk: één bron" staat in de beennaam.
- **b2-b4** (spoor): Jekaterinenburg - Tyumen - Omsk - Novosibirsk, 320,1 + 570,7 + 621,6 km, LETTERLIJKE KOPIEEN van de tricastin-seversk-geojsons.
- **b5-b9** (spoor): Novosibirsk - Krasnoyarsk - Irkutsk - Ulan-Ude - Chita - Borzya, 764,9 + 1.086,5 + 456,6 + 550,4 + 344,9 km; omgekeerde kopieen van priargunsky-seversk (beennaam noemt dat).
- **b10** (spoor): Borzya naar Manzhouli-emplacement via Zabaikalsk, 129,4 km (router 126,2; hemelsbreed 110).
- **b11** (spoor): Manzhouli naar Xiapu-station, 3.555,7 km (router 3.536,9; hemelsbreed 2.530), 5.243 punten; Hailar, Jinzhou, Tianjin, Hangzhou, Wenzhou, Fuding.
- **b12** (stippel, truck): last mile Xiapu-station naar CFR-600 Changbiao, 17,9 km rechte lijn (hemelsbreed 17,5 uit de brief; stippel start op het router-eind 26,9137/120,0238), 2 punten. Stippel = hier reikt het net niet; geen wegkm gemeten.
Gebakken km liggen 0,5-0,9 procent boven de router-km uit de brief (b1 +0,9, b11 +0,5): meetverschil router-lengte tegen punt-voor-punt haversine, geen afwijking.

**Markers** (4, uit §3): Elemash 0,12 km van de lijn · Manzhouli-emplacement 0,0 km · Xiapu-station 0,45 km (router-eind ligt 0,45 km west op de lijn) · CFR-600 0,0 km (stippel-eindpunt).

**Toets.** json.load: versie 2, punt_formaat lonlat, modaliteiten {spoor, truck}, elk been >= 2 punten, 392,8 KB. Naden 0,000 km. `toets_knikken.py`: 7 omkeringen >= 150 graden, waarvan 5 TERUGLOOP-gemarkeerd, allemaal router-snap-artefacten die de brief of de bron-stromen al kennen: b1 55,7609/38,9723 (v=99, 180 graden, R 0 m; brief noemt deze omkering, niet bijgeschoven) en 55,7334/38,4704 (scherpe bocht, echt); Krasnoyarsk 56,0086/92,8313 en 56,0220/92,8323 (priargunsky-kopie, ook in de bron-bake vermeld; 56,0220 telt dubbel doordat twee opeenvolgende benen hem delen); Irkutsk 52,2874/104,2597 (scherpe bocht); b10 49,5852/117,4366 vlak voor het Manzhouli-emplacement (v=2,2, kopmaak-boog bij het eindpunt). Niet gerepareerd, geen via-punt bijgeschoven. `toets_rechte_benen.py --min-km 5`: alleen de stippel b12 (17,9 km, MIDDEL, 2 punten; bedoeld); de stroom staat nog niet in de bundel, de tool leest dus de losse json.

**Open punten/bevindingen.**
- Geen spoorkm gepubliceerd: de +-15%-toets is niet toepasbaar; alleen paar, spoor en jaar zijn bron-gelegd, de rest is aannemelijk.
- b1: de router passeert Nizjni Novgorod op 88 km (de haalbaarheidstoets zei erdoorheen); twee omkeringen bij Elemash niet bijgeschoven.
- Spoorwijdtewissel ligt volgens Wikipedia in Zabaikalsk (Russische kant), niet apart gelegd.
- Sitelaag `w-tvel-elektrostal` ligt 3,4 km van `u-elemash`; geen CFR-600-site in de sitelaag: centraal gelijktrekken.
- Last mile is een stippel; dam naar Changbiao op de satelliet zichtbaar, niet als openbare weg gemeten.
- Registerregel (centraal): sleutel `u-ex`, bestand `stroomroute-uranium-elektrostal-xiapu.json`.

**Gereedschapslessen:**
- Zijn alle spoorstukken (kopieen en eigen runs) al in de build-cache aanwezig, dan is de bake een korte run van één functie: geen slot-wachttijd voor losse routerruns.
- Een omgekeerde kopie van een bestaand spoorbeen werkt zonder herrouten: beide uiteinden delen een knoop, naad 0,000 km.
- Bij het vergelijken van brief-km (router) en gebakken km rekent de bake haversine over de puntenketen: verwacht +0,5 tot +1 procent.
