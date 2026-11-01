# Routebrief (licht) · kolen — Seival Sul → Candiota-wasserij → Pampa Sul (Brazilië)

**stroom-id:** `kolen-seival-pampasul` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** Subbitumineuze thermische kool uit de dagbouw **Seival Sul** (Copelmi, Candiota, Rio Grande do Sul) gaat per **truck** over een ongeplaveide mijnweg (OSM, 3,45 km) naar de wasserij en vandaar per **overlandband** (OSM `goods_conveyor`, 4,14 km) naar de kolenontvangst van **UTE Pampa Sul** (345 MW, CFB) — mine-mouth, geen spoor, zee of binnenvaart; de centrale zet kool in één stap om in stroom.
**Welke as van het verhaal:** *de eerste Latijns-Amerikaanse kolenketen: Braziliaanse mijn-centralecluster* — Seival Sul **1,9 Mt kolen per jaar** (ROM, peiljaar 2023, Brasil Mineral via GEM [1]; GlobalData: 1,6 Mt), capaciteit 2,8 Mt per jaar; contract 160–230 kt per maand tot 2043 (= 1,9–2,8 Mt per jaar, GEM [1]). CREA: bijna 100 % van de Seival-kool gaat naar Pampa Sul [4].

## 1 · Ketenkaart
```
Seival Sul-put `kolen-seival-put`
   ──(b1 truck · ongeplaveide mijnweg, OSM-service-ways · 3,45 km)──► wasserij / bandkop `kolen-seival-wasserij`
   ──(b2 leiding/band · correia de carvão, UTE Pampa Sul · 4,14 km)──► Pampa Sul-kolenontvangst / centrale `kolen-pampasul-centrale` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `kolen-seival-put` → `kolen-seival-wasserij` | mijnweg Seival Sul, OSM `highway=service` `surface=unpaved`, ways 1096854442 + 1096854439 + 1096854440 (aaneengesloten) | OSM gestikt **3,45 km**; GEM noemt 4,5 km "van de fronten naar de wasserij" [1] (ander meetpunt, indicatie; ±15 %-toets geen norm) | vooraf gestikt FeatureCollection `v2/build-cache/ais/graaf/kolen-seival-pampasul-weg-mijnweg.geojson` (49 punten); geen `maak_stroombeen_weg` (OSM-service-ways zitten niet in de wegscan) | nee — doorgetrokken |
| b2 | B | leiding (band) | `kolen-seival-wasserij` → `kolen-pampasul-centrale` | OSM `man_made=goods_conveyor`, name "correia de carvão", operator UTE Pampa Sul, resource coal, way 1096854443 (v2, 2025-11) | OSM gestikt **4,14 km**, geen gepubliceerde bandlengte; hemelsbreed 3,9 | vooraf gestikt FeatureCollection `v2/build-cache/ais/graaf/kolen-seival-pampasul-leiding-band.geojson` (36 punten) | nee — doorgetrokken (OSM heeft de band) |

Naden: b1-eind (-31.46375, -53.73573) → b2-begin (-31.46475, -53.73595) = **0,11 km**, binnen het wasserijterrein (procesgat, geen stippel). b2-eind (-31.45198, -53.77395) ligt 0,3 km van het GEM-centralepunt; het marker-anker staat op de centrale zelf. Totaal ca. 7,6 km: net boven de 5 km-grens van de Mae Moh-afwijzing; de haalbaarheidstoets liet de keten toe.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-seival-put` | mijn / laadplek, begin b1 | Seival Sul-dagbouw (Copelmi), zuidkant van de put waar de mijnweg begint | -31.4546, -53.7077 | [1][5][7] | bron-gelegd (z15 gezien: grote dagbouwput met donkere kolenvloer en terrassen; mijnweg verlaat de put aan de zuidkant richting ZW) |
| `kolen-seival-wasserij` | overslag weg → band (wasserij/bandkop), eind b1 en begin b2 | begin van de kolenband bij de wasserij | -31.4648, -53.7359 | [1][5][7] | bron-gelegd (z15 gezien: industrieel complex met gebouwen, silo's en een bekken midden in akkerland; de band loopt vanaf hier naar het NW) |
| `kolen-pampasul-centrale` | afnemer, eind b2 | UTE Pampa Sul (Miroel Wolowski), kolenontvangst | -31.4506, -53.7769 | [2][5][7] | bron-gelegd (z15 gezien: centralecomplex met een witte hal en opslagterrein; een dunne lijn, de band, loopt vanuit het oosten het terrein op) |

Hergebruik: geen bestaand anker; de sitelaag `v2/design/kolen-sitelaag.json` en eerdere brieven kennen Candiota niet. GEM-coördinaten: mijn -31.449159, -53.707527 (op de put, 0,5 km N van het gekozen anker); centrale -31.4506, -53.77687.

## 4 · Via-punten
Geen: beide benen volgen één gekarteerd OSM-pad zonder corridorkeuze; er is geen zee-, spoor- of wegscan, geen MARNET, geen extract en geen haven-aanloop.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Seival Sul-mijn + wasserij (beneficiation) | Copelmi Mineração (Seival Sul Mineração; Eneva verkocht 30 % in 2019) | dagbouw-ROM → gewassen thermische kool | capaciteit 2,8 Mt per jaar; productie 1,9 Mt (2023) | [1][6] |
| UTE Pampa Sul (Usina Termelétrica Pampa Sul) | Perfin Space X 50 % + Starboard 50 % (overname van Engie, 2022); eerder Tractebel/Engie | kool → elektriciteit (CFB, 1 × 345 MW, bedrijf sinds 2019) | 345 MW; kooltoevoer contractueel 160–230 kt per maand tot 2043 | [2] |

## 6 · Stoppunt
De brief stopt bij de kolenontvangst van Pampa Sul: de centrale verbrandt de kool in één stap tot elektriciteit, dus er is geen fase D en E vervalt. Een tweede cluster-keten (Candiota-mijn → Candiota III) bestaat naast deze, maar is niet onderzocht.

## 7 · Open punten
- **Mijnweg is geen wegkilometer-bron:** 3,45 km komt uit OSM-ways (unpaved service); GEM noemt 4,5 km van de fronten naar de wasserij. Beide zijn indicatie, geen bedrijfsopgave van de wegkilometer.
- **Bandlengte:** geen gepubliceerde waarde; 4,14 km is OSM. Aparte, ongetagde bandstukken bij het mijncluster zijn niet getekend; het einde van way 1096854443 ligt 0,3 km van het GEM-centralepunt, geen stippel.
- **Anker mijn:** de put is groot (dagbouw, meerdere fronten); het anker is het begin van de mijnweg aan de zuidkant, niet het actieve front. GEM-mijnpunt ligt 0,5 km noordelijker.
- **Volume:** 1,9 Mt (2023) komt uit Brasil Mineral via GEM, niet rechtstreeks gezien; GlobalData noemt 1,6 Mt. Contract 160–230 kt per maand is een contractmaat. Geen peiljaar later dan 2023 gevonden.
- **Eigendom en looptijd:** Pampa Sul wisselde in 2022 van eigenaar (Engie naar Perfin/Starboard); de eigenaren willen vóór 2043 ontmantelen, de steenkoollobby wil verlenging; GEM meldt een levensduurstudie in december 2025.
- **Sitelaag:** `kolen-sitelaag.json` bevat geen Candiota-site; centraal toevoegen indien gewenst (niet door mij gewijzigd).

## 8 · Bronnen
[1] Global Energy Monitor, Seival Coal Mine: -31.449159/-53.707527, capaciteit 2,8 Mt per jaar, 2023-productie 1,9 Mt (Brasil Mineral) en 1,6 Mt (GlobalData), contract 160–230 kt per maand tot 2043, wasserij ca. 4,5 km van de fronten. https://www.gem.wiki/Seival_Coal_Mine
[2] Global Energy Monitor, Pampa Sul power station: -31.4506/-53.77687, 345 MW CFB, gevoed via transportband uit de Seival-mijn, overdracht aan Starboard/Perfin 2022. https://www.gem.wiki/Pampa_Sul_power_station
[3] IBRAM, "Power plant makes Seival mine (RS) viable", 2007 (Jornal do Comércio) — mijnreserves ca. 350 Mt, mijn afhankelijk van de TermoPampa-centrale. https://ibram.org.br/en/noticia/usina-viabiliza-mina-de-seival-rs/
[4] Centre for Research on Energy and Clean Air (CREA) / Instituto Arayara, Coal in Candiota, 2026 — bijna 100 % van de Seival Sul-kool naar Pampa Sul. https://energyandcleanair.org/publication/coal-in-candiota-health-impacts-of-a-coal-mining-and-power-generation-cluster-in-rio-grande-do-sul-brazil/
[5] OpenStreetMap (ODbL), ways 1096854442, 1096854439, 1096854440 (`highway=service`, `surface=unpaved`) en 1096854443 (`man_made=goods_conveyor`, "correia de carvão", operator UTE Pampa Sul, resource coal), via OSM-API 0.6 opgehaald 2026-11-01. https://www.openstreetmap.org/way/1096854443
[6] Global Energy Monitor, Seival Coal Mine, eigendom: Copelmi 100 %, Eneva-aandeel verkocht 2019 (zelfde pagina als [1], sectie Background).
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-kolen-seival-pampasul-put.png`, `sat-kolen-seival-pampasul-bandkop.png`, `sat-kolen-seival-pampasul-centrale.png`.

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-kolen-seival-pampasul.json` (2,65 kB, versie 2, punt_formaat lonlat) · **functie:** `bak_kolen_seival_pampasul` in `v2/tools/bak_stromen.sh` · **recept:** `bash v2/tools/bak_stromen.sh kolen-seival-pampasul`.

| been | modaliteit | km gebakken | km brief | punten | stippel |
|---|---|---|---|---|---|
| b1 mijnweg Seival Sul (put -> wasserij) | truck | 3,5 | OSM 3,45; GEM 4,5 (indicatie, geen wegkm) | 49 | nee |
| b2 overlandband correia de carvao (wasserij -> Pampa Sul) | leiding | 4,1 | OSM 4,14 (geen bandopgave) | 36 | nee |

Totaal 7,6 km, 85 punten, 3 markers. Beide benen zijn `--been-geojson` uit de vooraf gestikte OSM-FeatureCollections (`kolen-seival-pampasul-weg-mijnweg.geojson`, `kolen-seival-pampasul-leiding-band.geojson`); geen `maak_stroombeen_weg`, geen profiel, geen zee, geen MARNET-aanloop, geen via-punten, geen kopie, geen vlucht, geen stippel.

**Toets:** naad b1 -> b2 0,11 km (wasserijterrein, procesgat, geen stippel); markers put 0,003 km, wasserij 0,007 km, centrale 0,32 km van hun lijn (binnen ~0,5 km); `toets_knikken.py`: 0 knikken, 0 omkeringen; geen been >= 5 km recht (beide gekarteerd); km binnen 1,5 procent van OSM. De +-15%-toets is geen norm: de brief geeft geen echte wegkm (OSM 3,45 en GEM 4,5 zijn indicaties).

**Toelichting:** de band is doorgetrokken omdat OSM hem kent (`man_made=goods_conveyor`, operator UTE Pampa Sul); de mijnweg omdat OSM de service-ways kent. De bakker voegde niets toe aan de geometrie; het mijnanker is het wegbegin aan de zuidkant van de put, niet het actieve front.

**Lessen:** (1) een mine-mouth-keten van twee korte OSM-benen bakt in een paar seconden zonder slot-zware tools; de hecht_marnet-route laadt wel de MARNET- en AIS-graaf (ca. 12 s) voor niets. (2) Sitelaag kolen kent Candiota nog niet (centraal).
