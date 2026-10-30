# Routebrief (licht) · kolen — Bogdanka (LW Bogdanka) → Elektrownia Kozienice (Polen)

**stroom-id:** `kolen-bogdanka-kozienice` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** energiekool (steenkool, Lublin-bekken) uit de ondergrondse mijn LW Bogdanka gaat per **spoor** (mijnaansluiting naar Jaszczów, lijn 7 via
Lublin en Puławy naar Dęblin, lijn 26 tot Bąkowiec, lijn 76 naar de centrale) naar Elektrownia Kozienice (Enea Wytwarzanie, 4.000 MW) — stoppunt: de kool wordt
daar verstookt. Eén gemeten spoorbeen, geen zee. De ketenkoppeling is **bron-gelegd**: PKP Cargo kreeg twee aanbestedingen voor precies dit traject [1][3]
(het ontwerp noemde dit de zwakste bron; dat klopt niet), en Enea is sinds 2015 meerderheidsaandeelhouder van Bogdanka [6].
**Welke as van het verhaal:** *Poolse energiekool voor Polens tweede centrale — een keten binnen één concern (Enea).* Jaarvolume **≈ 4,5 Mt kolen/j**
(afgeleid uit het contract van 24-05-2017: 5,3 Mt in 14 maanden [1]; contract 2016: >5 Mt in 15 maanden = >4,0 Mt/j [3]). Indicatie 2025: Enea Wytwarzanie nam
64% van de Bogdanka-omzet af [13] bij 7,654 Mt kolenverkoop [12] — omzetaandeel is geen volumeaandeel, dus ≈ 4,9 Mt/j alleen als orde (afgeleid).
Bogdanka won 9,2 Mt in 2014 [5], 11,6 Mt brutto en 7,6 Mt netto in 2025 [12].

## 1 · Ketenkaart
```
LW Bogdanka-mijn (schachten, spoorplein, kolenopslag) `kolen-bogdanka-laad`
   ──(b1 spoor · mijnaansluiting → Jaszczów → lijn 7 → Lublin → Puławy → Dęblin → lijn 26 → Bąkowiec → lijn 76 → Kozienice · router 154,1 km,
       bron-gelegd: PKP Cargo/Enea-contracten 2016 en 2017)──► Elektrownia Kozienice (kolenopslag + ketelhuizen) `kolen-kozienice-centrale` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A+C | spoor | `kolen-bogdanka-laad` → `kolen-kozienice-centrale` | bocznica Bogdanka–Jaszczów [11] → lijn 7 Jaszczów (km 201,8) – Lublin Gł (km 175,0) – Puławy (km 126,8) – Dęblin (km 103,3) [9][11] → lijn 26 Dęblin–Bąkowiec [10] → lijn 76 Bąkowiec–Kozienice (aansluiting op de centrale) [7][8] | hemelsbreed 113,0 km, geen gepubliceerde totale spoorkm; router 154,1 km / 156,9 km over de 461 punten (verhouding 1,36–1,39, 0 bochten ≥60°). Deelstukken: Jaszczów–Lublin Gł 25,5 km route tegen 26,8 gepubliceerd (−5%), Lublin Gł–Puławy 48,4 tegen 48,2 (+0,4%). De ±15%-toets is indicatie | toets_spoorroute (1-op-1-net), één run, geen via | nee — volledig in het 1-op-1-net |

Fase C (last mile) vervalt: beide ankers liggen op het terrein (snap kop 0,25 km, staart 0,28 km). Geen zee, weg, leiding, lucht, haven-aanloop of kopie. Geen D/E:
de kool gaat in de ketels (E vervalt).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-bogdanka-laad` | mijn / laadplek | LW Bogdanka (KWK Bogdanka), Puchaczów — mijncomplex met spoorplein | 51.3286, 23.0052 | [5][6][15] | bron-gelegd (z15 gezien: schachtgebouwen met hijstorens, spoorbundel langs de westzijde die zuidwaarts het terrein verlaat, donkere kolenopslag ten noordoosten, twee ronde bezinkvijvers, grote hal ten zuidwesten; het kruis ligt op de schachten). Het wiki-punt 51.3289, 23.0047 [6] ligt 55 m ernaast op hetzelfde terrein |
| `kolen-kozienice-centrale` | verbruiker / losplek | Elektrownia Kozienice (Enea Wytwarzanie), Świerże Górne — ketelhuizen en kolenparken | 51.6653, 21.4644 | [7][15] | bron-gelegd (z15 gezien: centrale met koeltoren en ketelhuizen, vijf donkere kolenstapels langs het aanvoerspoor dat van het zuiden komt, schakelstation ernaast, de Wisła direct ten oosten). Wiki-punt [7] 51°39′55″N 21°27′52″E; het kruis ligt tussen ketelhuis en turbinehal, 0,3 km van de kolenparken |

Hergebruik: geen bestaand anker (geen eerdere keten met Bogdanka of Kozienice; `kolen-sitelaag.json` en de eerdere brieven noemen ze niet).

## 4 · Via-punten
Geen. De vrije route volgt zonder via de bronlijnen; gemeten langs de 461 punten: Jaszczów op 0,41 km (route-km 25,2), Lublin Gł op 0,04 km (50,7), Puławy op 0,26 km (99,1),
Dęblin (noordpunt route-km 119,2), Bąkowiec op 0,27 km (129,2), Janików op 0,54 km (140,3). Garbatka-Letnisko ligt op lijn 26 voorbij Bąkowiec en is niet nodig: lijn 76 takt in
Bąkowiec af [10] (het ontwerp noemde Garbatka als corridor). Een via op een station zou alleen een bocht kunnen afdwingen. De enige corridorkeuze is Lublin → Dęblin: via Puławy
(lijn 7, hier gevolgd) of via lijn 30 Lublin Płn–Łuków (107,7 km [14]) en lijn 26. Die laatste was in 2017 een **tijdelijke omleiding** wegens modernisering van het traject [1] en is geen
corridorkeuze die een via-punt rechtvaardigt.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LW Bogdanka | Enea (65% sinds 2015; beursgenoteerd) | steenkool, ondergronds → spoor (eigen vervoerslicentie, LBW) | 11,6 Mt brutto / 7,6 Mt netto (2025); 9,2 Mt (2014) | [6][12] |
| Elektrownia Kozienice | Enea Wytwarzanie (100% Enea) | steenkool → elektriciteit en warmte; kolenaanvoer per eigen aansluiting op lijn 76 | 4.000 MW; 266 MW warmte | [7] |

## 6 · Stoppunt
De brief stopt bij de centrale van Kozienice: de kool houdt daar op als grondstof (verbranding), er is geen volgende fysieke goederenstroom.

## 7 · Open punten
- **Spoorlengte:** geen gepubliceerde totale spoorkm; alleen lijn 7 per km-positie [9][11] is nagerekend, de rest (bocznica Bogdanka–Jaszczów, Dęblin–Bąkowiec, lijn 76) niet.
- **Lijn 82 Bąkowiec–Puławy Azoty** staat in de bron als aanwezige lijn [10]; de router neemt de omweg via Dęblin (Puławy–Bąkowiec 29,3 km). Of lijn 82 voor kolen openstaat is niet gevonden.
- **Volume per jaar niet rechtstreeks gebrond:** afgeleid uit twee contracten (2016, 2017) en het omzetaandeel 2025; geen jaarcijfer voor deze stroom. Recent jaarverslag-aandeel in tonnen niet gevonden.
- **Vervoerder nu:** de contracten 2016/2017 gaan naar PKP Cargo, de eerste (2007) naar Freightliner PL [4]; wie nu rijdt is niet gevonden (Bogdanka heeft zelf een vervoerslicentie [6]).
- **Wiki-aandeel:** Bogdanka levert ook aan Enea Elektrownia Połaniec (16% omzet) [13]; die stroom is niet getekend.
- **Sitelaag:** `kolen-sitelaag.json` heeft geen Poolse sites; Bogdanka en Kozienice kunnen centraal als sites met productie/capaciteit erbij.

## 8 · Bronnen
[1] Enea (ir.enea.pl), 24-05-2017, PKP Cargo with a large contract for coal transports for Enea Group — 5,3 Mt Bogdanka → Kozienice, 14 maanden, omleiding via lijn 30. https://ir.enea.pl/en/pr/356768/pkp-cargo-with-a-large-contract-for-coal-transports-for-enea-group
[2] money.pl, 24-05-2017, PKP Cargo ma umowę na przewóz 5,3 mln t węgla (idem). https://www.money.pl/gielda/wiadomosci/artykul/pkp-cargo-ma-umowe-na-przewoz-5-3-mln-t-wegla,98,0,2324578.html
[3] PKP Cargo, persbericht 16-05-2016, PKP CARGO przewiezie ponad 5 mln ton węgla dla Enei za 54 mln zł — Bogdanka → Kozienice, 15 maanden. https://pkpcargo.com/wp-content/uploads/2023/10/pkpcargoobsluzyprzewozywegladlaeneakomunikatprasowy16052016.pdf
[4] en.wikipedia, Freightliner Group — Freightliner PL, eerste kolencontract Bogdanka → Kozienice, vanaf september 2007. https://en.wikipedia.org/wiki/Freightliner_Group
[5] en.wikipedia, Bogdanka Coal Mine — 51°19′44″N 23°00′17″E, productietabel 2007–2014 (9,191 Mt in 2014). https://en.wikipedia.org/wiki/Bogdanka_Coal_Mine
[6] pl.wikipedia, Lubelski Węgiel „Bogdanka” — 51.3289, 23.0047, Enea 65% sinds 2015, vervoerslicentie LBW. https://pl.wikipedia.org/wiki/Lubelski_W%C4%99giel_%E2%80%9EBogdanka%E2%80%9D
[7] pl.wikipedia, Elektrownia Kozienice — 51°39′55″N 21°27′52″E, 4.000 MW, kolen per spoor, aansluiting op lijn 76, leveranciers incl. Bogdanka. https://pl.wikipedia.org/wiki/Elektrownia_Kozienice
[8] pl.wikipedia, Linia kolejowa nr 76 Bąkowiec – Kozienice (enkelspoor, geëlektrificeerd). https://pl.wikipedia.org/wiki/Linia_kolejowa_nr_76
[9] pl.wikipedia, Linia kolejowa nr 7 — km-posities Dęblin 103,285 · Puławy 126,777 · Lublin Główny 174,973. https://pl.wikipedia.org/wiki/Linia_kolejowa_nr_7
[10] pl.wikipedia, Bąkowiec (stacja kolejowa) — 51°31′03″N 21°43′25″E; lijnen 26, 76 en 82. https://pl.wikipedia.org/wiki/B%C4%85kowiec_(stacja_kolejowa)
[11] pl.wikipedia, Jaszczów (stacja kolejowa) — lijn 7 km 201,784, bocznica naar LW Bogdanka. https://pl.wikipedia.org/wiki/Jaszcz%C3%B3w_(stacja_kolejowa)
[12] LW Bogdanka, presentatie jaarcijfers 2025 — verkoop 7.654 kt, productie netto 7.569 kt, brutto 11.556 kt. https://ri.lw.com.pl/pobierz/7384/przedstawienie-wynikow-finansowych-lw-bogdanka-s-a-za-2025-r-pdf
[13] Parkiet, 2026, Coraz trudniej utrzymać Bogdance chętnych na węgiel — Enea Wytwarzanie 64% en Połaniec 16% van de omzet 2025; contracten verlengd tot 2036. https://www.parkiet.com/surowce-i-paliwa/art44136461-coraz-trudniej-utrzymac-bogdance-chetnych-na-wegiel
[14] pl.wikipedia, Linia kolejowa nr 30 Łuków – Lublin Północny (107,723 km) en nr 26 Łuków – Radom Główny. https://pl.wikipedia.org/wiki/Linia_kolejowa_nr_30
[15] Esri World Imagery via `v2/tools/sat_check.py`; OSM-spoornet via `toets_spoorroute.mjs` (2026-10-30) — `v2/build-cache/satcheck/sat-kolen-bogdanka-kozienice-mijn.png`, `-centrale.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
**Bestand:** `v2/data/stroomroute-kolen-bogdanka-kozienice.json` (8,7 KB; versie 2, punt_formaat lonlat) · functie `bak_kolen_bogdanka_kozienice` in `v2/tools/bak_stromen.sh` · titel *Kolen · Bogdanka (Lublin-bekken) → Elektrownia Kozienice (Polen)*.
**Benen (1):** b1 spoor "trein Bogdanka → Elektrownia Kozienice (via Jaszczów, Lublin, Puławy, Dęblin en Bąkowiec; lijn 7 → 26 → 76)", **156,9 km, 461 punten**, doorgetrokken (geen stippel). Totaal 156,9 km, 2 markers.
**Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=51.3286,23.0052 --naar=51.6653,21.4644 --naam=kolen-bogdanka-kozienice-bogdanka-kozienice --hoofd-km=200` (1-op-1-net, één run, geen via); de FeatureCollection `v2/build-cache/ais/graaf/spoorroute-kolen-bogdanka-kozienice-bogdanka-kozienice.geojson` is ongewijzigd als `--been-geojson "spoor|…"` gebruikt. Daarna `bash v2/tools/bak_stromen.sh kolen-bogdanka-kozienice` (zwaar-slot, 40 s).
**Markers:** `kolen-bogdanka-laad` 51.3286, 23.0052 (0,25 km van de lijn) en `kolen-kozienice-centrale` 51.6653, 21.4644 (0,28 km van de lijn) — beide ≪ 0,5 km.
**Toets (handleiding §5):** km-toets is indicatie (geen gepubliceerde totale spoorkm): 156,9 gemeten tegen hemelsbreed 113,0 (verhouding 1,39) en eerder nagerekende deelstukken (Jaszczów–Lublin Gł −5%, Lublin Gł–Puławy +0,4%). Eén been, dus geen naden. `toets_knikken.py`: 0 knikken ≥ 60°, 0 omkeringen. `toets_rechte_benen.py --min-km 5`: het been staat niet in de lijst (geen rechte lijn); grootste puntafstand 5,1 km op een recht baanvak ten westen van Lublin (punt 212), geen gat. json.load: versie 2, modaliteit {spoor}, 461 punten.
**Geen:** stippel, haven-aanloop, vlucht, leiding, kopie of via-punt; geen extract gebruikt voor weg (Polen niet gescand).
**Lessen:** de tussenuitvoer van de brief-fase bleek direct bruikbaar; het 1-op-1-net levert voor een nationaal spoorbeen zonder via-punten een nette, knikvrije lijn (lijn 7 → 26 → 76). Open punten uit §7 blijven staan (lijn 82, totale spoorkm, volume, vervoerder).
