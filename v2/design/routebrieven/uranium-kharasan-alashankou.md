# Routebrief (licht) · uranium — Kharasan (Kazachstan) → Alashankou (China)

**stroom-id:** `uranium-kharasan-alashankou` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** yellowcake van de Kharasan-ISR-mijn (Uranium One-JV — sinds 2013 Rosatom-dochter — 60/40
met Kazatomprom, Zuid-Kazachstan) per **truck** naar het spoorstation Zhanakorgan, dan per **spoor** via de
Trans-Aral-lijn en de Turksib-corridor (Shymkent–Taraz–Almaty–Aktogay) naar de grensovergang Dostyk–Alashankou
— Kazatomprom's leverpunt voor de contracten met SNURDC/SPIC en CNUC, stoppunt.
**Welke as van het verhaal:** *Kazachstan → China per spoor, de daadwerkelijk grootste afnemer.* Kazachstan
leverde in 2023 twee derde van het door China ingevoerde natuurlijk uranium (Carnegie Endowment, 2024-07);
NucNet (5-3-2024) bevestigt lopende onderhandelingen over een oostwaartse transitroute via Alashankou naar
Shanghai. Vierde, onafhankelijke Kazachstan→China-as naast de drie eerder gebouwde Inkai-stromen.

## 1 · Ketenkaart
```
Kharasan-mijn `u-kharasan-plant` ──(b1 truck · steppepiste → Zhanakorgan-station · ~31 km hemelsbreed,
   aannemelijk: eigen verbinding, geen bron)──►
Zhanakorgan-spoorstation `u-zhanakorgan-station` ──(b2 spoor · Trans-Aral-lijn zuidwaarts → Turksib oostwaarts
   (Shymkent–Taraz–Almaty–Aktogay) → Dostyk–Alashankou-grensovergang · geen gepubliceerde spoorkm,
   aannemelijk: geografische afleiding)──►
Alashankou-spoorstation `u-alashankou-station` ── stoppunt (leverpunt SNURDC/SPIC/CNUC, geen Chinese
   verwerker na Alashankou gedocumenteerd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Kharasan-mijn → Zhanakorgan-station | steppepiste/toegangsweg, geen bron voor exact traject | ~31 [eigen berekening, hemelsbreed, geen wegkm] | maak_stroombeen_weg (extract kazachstan) | nee — *aannemelijk: eigen verbinding, geen bron*; vindt de scanner geen doorgaand pad, dan alsnog stippel |
| b2 | A | spoor | Zhanakorgan-station → Alashankou-station | Trans-Aral-lijn (Zhanakorgan → Turkestan → Arys) → Turksib oostwaarts (Shymkent–Taraz–Almaty) → tak naar Aktogay–Dostyk–Alashankou | geen gepubliceerd [via-punten hemelsbreed-som ~1.850 km, eigen berekening] | toets_spoorroute (BAKE_SUFFIX=-raw, extracts kazachstan + china) | nee — *aannemelijk: geografische afleiding* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-kharasan-plant` | mijn / ISR-verwerkingscomplex (laadplek) | Kharasan ISR-complex (Uranium One-JV/Rosatom, Zuid-Kazachstan-regio) | 43.8427, 66.8640 | [3][4][sat] | bron-gelegd (z16 gezien: gebouwencomplex met tanks en lijnvormige procesbekkens direct ZO van het Wikipedia-punt 43.8400/66.8600, dat slechts 2 decimalen droeg — hier verschoven naar het zichtbare complex) |
| `u-zhanakorgan-station` | overslag truck → spoor | Zhanakorgan-spoorstation, Kyzylorda-oblast | 43.9005, 67.2467 | [6][sat] | bron-gelegd (z15 gezien: stationsgebouw + spoorbundel aan de rand van de stad Zhanakorgan, aan de Trans-Aral-lijn, tegenover een zoutmeer) |
| `u-alashankou-station` | overslag spoor (stoppunt) | Alashankou-spoorstation (阿拉山口站), Xinjiang | 45.1703, 82.5705 | [5][6][sat] | bron-gelegd (z15 gezien: uitgebreid emplacement met meerdere sporen, rangeeryard en grote vrachtloodsen direct aan de grensovergang met Dostyk) |

## 4 · Via-punten (alleen b2 — corridorkeuzes op de Trans-Aral/Turksib-route)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Turkestan-spoorstation | 43.2857, 68.2130 | op de Trans-Aral-lijn, waar de route zuidwaarts naar de Arys-knoop buigt i.p.v. noordwaarts langs de Syrdarja te blijven |
| b2 | 2 | Shymkent-spoorstation | 42.2987, 69.6103 | bij de Arys-knoop splitst de Trans-Aral-lijn naar Tasjkent (Oezbekistan); dit punt pint de Turksib-tak oostwaarts |
| b2 | 3 | Taraz-spoorstation | 42.8697, 71.3789 | doorgaand knooppunt op de Turksib-lijn tussen Shymkent en Almaty |
| b2 | 4 | Almaty-2-spoorstation | 43.2738, 76.9391 | bij Almaty verlaat de route de Turksib-hoofdlijn (die verder noordwaarts naar Semey/Rusland loopt) voor de tak naar Aktogay–Dostyk |
| b2 | 5 | Aktogay (spoorknoop) | 46.9570, 79.9263 | hier splitst de lijn naar Dostyk/China van de doorgaande lijn naar Ayagoz/Semey — zonder dit punt kan een vrije Dijkstra de Ayagoz-tak nemen. ⚠️ coördinaat bij benadering: geen los OSM-stationspunt gevonden binnen het webbudget, positie is die van de bekende Aktogay-nederzetting (kopermijn-GOK) in dezelfde plaats — snap > 5 km bij het bakken is een signaal om na te kijken |
| b2 | 6 | Dostyk-spoorstation (grensovergang) | 45.2529, 82.4867 | laatste Kazachse station vóór de grensovergang naar Alashankou; hier vindt de bogiewissel plaats (1520 mm → 1435 mm) |

## 5 · Verwerkingsknopen
*(geen — deze stroom bevat geen conversie/verrijking; Alashankou is een zuiver grensovergangs-/overslagpunt, geen verwerkingsknoop)*

## 6 · Stoppunt
De brief stopt bij het Alashankou-spoorstation: dit is het opgedragen keten-eindpunt en het leverpunt dat
Kazatomprom's contracten met SNURDC/SPIC en CNUC noemen (NucNet, 5-3-2024, "to the Alashankou railway
station"). Geen bron noemt een specifieke Chinese verwerker of vervolgbestemming ná Alashankou — fase D
vervalt conform de haalbaarheidstoets.

## 7 · Open punten
- **Kharasan als bronmijn is niet bevestigd voor déze leveringen** (aannemelijk: de gevonden contracten
  koppelen aan Kazatomprom als staatsexporteur, niet aan Kharasan individueel) — deze disclaimer staat hier
  expliciet, conform de bindende aanpassing uit de haalbaarheidstoets, en de onzekerheid zit in de tekst, niet
  in de lijnstijl.
- **Kharasan-coördinaat verfijnd** van de 2-decimalen Wikipedia-waarde (43.84, 66.86) naar 4 decimalen via
  satellietblik op het zichtbare ISR-complex (§3); geen Kazatomprom/Uranium One NI 43-101-rapport gevonden
  binnen het webbudget om dit onafhankelijk te bevestigen.
- **Fase A (mijn → Zhanakorgan) heeft geen gepubliceerde km, corridor of exact traject** — bij het bakken de
  daadwerkelijke toegangsweg zoeken via osmium op de `kazachstan`-extract; vindt de scanner geen doorgaand
  pad over de ~31 km steppe (zoals bij `uranium-inkai-poti` b1 gebeurde op een veel langere afstand), dan
  stippel "last mile (geen net op deze korrel)".
- **Spoorcorridor Trans-Aral→Turksib→Aktogay→Dostyk is "aannemelijk: geografische afleiding"** — geen bron
  noemt de tussenstations; het Aktogay-via-punt is zelf een benadering (§4) en de werkelijke gebakken lengte
  kan flink afwijken van de indicatieve ~1.850 km hemelsbreed-som.
- **Geen gepubliceerd jaarvolume specifiek voor Kharasan of voor de Alashankou-leveringen** — context:
  Kazachstan leverde in 2023 twee derde van China's ingevoerde natuurlijk uranium (Carnegie Endowment, 2024).
- **Uranium One (JV-partner van Kazatomprom in Kharasan) is sinds 2013 volledig eigendom van Rosatom**
  (Wikipedia) — een tweede gelaagdheid die het ketenontwerp niet noemde: een Russisch-Kazachse JV levert aan
  China.
- **Gauge-wissel bij Dostyk (1520 mm → 1435 mm)** is bekend (bogiewisseldepot) maar hier niet als apart been
  gemodelleerd — de bak-agent kan het spoorbeen desgewenst op de grens splitsen.

## 8 · Bronnen
[1] NucNet, 5-3-2024, "Talks continuing with China on eastward transit route for uranium exports" — Kazatomprom
onderhandelt over een landroute via Alashankou naar Shanghai, om Rusland te vermijden. https://www.nucnet.org/news/talks-continuing-with-china-on-eastward-transit-route-for-uranium-exports-5-3-2024
[2] Carnegie Endowment, 2024-07, "To Secure Kazakhstan's Uranium, Chinese Players Were Compelled to
Accommodate Local Partners" — Kazachstan leverde 2023 twee derde van China's ingevoerde natuurlijk uranium;
CGN-belangen in Semizbay-U en Ortalyk (niet Kharasan); Kazatomprom behoudt wettelijk ≥50% in elke JV.
https://carnegieendowment.org/posts/2024/07/to-secure-kazakhstans-uranium-chinese-players-were-compelled-to-accommodate-local-partners
[3] Wikipedia, "Kharasan mine" — ISR-mijn, Zuid-Kazachstan-regio, coördinaat 43.84/66.86 (2 decimalen), 59,3
Mt erts à 0,074% U. https://en.wikipedia.org/wiki/Kharasan_mine
[4] Wikipedia, "Uranium One" — bezit Akdala/South Inkai/Karatau/Akbastau/Kharasan in Kazachstan; sinds
oktober 2013 volledig eigendom van Rosatom (ARMZ nam de resterende aandelen over). https://en.wikipedia.org/wiki/Uranium_One
[5] Wikipedia, "Alashankou" — grensstad Xinjiang, spoor- en wegpoort met Kazachstan, Eurasian Land Bridge;
westelijke poort van de pas is Dostyk. https://en.wikipedia.org/wiki/Alashankou
[6] Wikipedia, "Dostyk" — grensstation/-stad op de grens met Xinjiang, spoorlink 1959 (Sovjetzijde) / voltooid
12-9-1990, bogiewisseldepot 1520↔1435 mm; poort aan Chinese zijde is Alashankou.
https://en.wikipedia.org/wiki/Dostyk · OSM/Nominatim (ODbL) — stationspunten Zhanakorgan (43.90050/67.24670),
Turkestan (43.28570/68.21300), Shymkent (42.29870/69.61030), Taraz (42.86970/71.37890), Almaty-2
(43.27380/76.93910), Dostyk (45.25290/82.48670), Aktogay-nederzetting (46.95700/79.92630).
https://www.openstreetmap.org
[7] Wikipedia, "Trans-Aral Railway" — 1520 mm-lijn Kinel–Tasjkent (1906), loopt door Kyzylorda-oblast waar
Zhanakorgan aan ligt. https://en.wikipedia.org/wiki/Trans-Aral_Railway
[8] Wikipedia, "Turkestan–Siberia Railway" (Turksib) — Arys (afsplitsing Trans-Aral) → Shymkent → Taraz →
Almaty → noordwaarts naar Semey/Rusland; de tak naar Aktogay/Dostyk/China vertakt bij Almaty-omgeving.
https://en.wikipedia.org/wiki/Turkestan%E2%80%93Siberia_Railway
[9] Wikipedia, "Kazatomprom" — Ulba-fabriek fabriceert sinds 2021 splijtstofbundels voor CGNPC (China);
algemene China-samenwerkingscontext, geen Alashankou-specifieke passage gevonden binnen het webbudget.
https://en.wikipedia.org/wiki/Kazatomprom
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live) —
`v2/build-cache/satcheck/sat-uranium-kharasan-alashankou-mine-cand.png`,
`sat-uranium-kharasan-alashankou-mine-refine.png`, `sat-uranium-kharasan-alashankou-zhanakorgan-station.png`,
`sat-uranium-kharasan-alashankou-alashankou-station.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Stroom `uranium-kharasan-alashankou`** → `v2/data/stroomroute-uranium-kharasan-alashankou.json` — 8 benen,
**2.013,9 km**, 3 markers: truck 34,7 km · spoor 106,8 + 185,8 + 203,4 + 546,5 + 586,8 + 332,3 + 17,6 km
(spoor-totaal 1.979,2 km). Bestand 66,7 KB. Geen stippels, geen zeebenen, geen leiding, geen lucht (conform
brief §1/§6). Recept: `bak_stromen.sh` (functie `bak_uranium_kharasan_alashankou`).

Toelichting per leg:
- **b1 (truck):** `maak_stroombeen_weg.py --profiel uranium-kharasan-alashankou-kharasan-zhanakorgan`
  (venster 60 km, extract `kazachstan`, geen via-punten) vond wél een doorgaand pad — anders dan de brief
  als mogelijke uitkomst opende ("vindt de scanner geen doorgaand pad, dan alsnog stippel"). 34,3 km ruwe
  weggeometrie (34,7 km gebakken met anker-stubs), tegen ~31 km hemelsbreed uit de brief = **+10,8%** —
  buiten de informele ±10%-waarschuwing van het tool, maar de brief geeft zelf geen echte wegkm (alleen
  een hemelsbrede schatting), dus dit is een indicatie, geen harde norm (brief §2/§7). Eerste en laatste
  ~7,4/0,1 km lopen over kleine wegklassen (`service`) binnen 12 km van plant/kade.
- **b2 (spoor, 1-op-1-net, ZEVEN aparte segmenten in reisvolgorde, geen `--via` bestaat):**
  `BAKE_SUFFIX=-raw toets_spoorroute.mjs --hoofd-km=1000` per deelstuk, telkens snap ≤0,3 km op het
  hoofdnet (grootste component 1.144.150 km):
  - Zhanakorgan → Turkestan: 106,8 km (tool 106,2, grootcirkel 103,6, verhouding 1,03).
  - Turkestan → Shymkent: 185,8 km (tool 184,5, grootcirkel 158,3, verhouding 1,17).
  - Shymkent → Taraz: 203,4 km (tool 201,5, grootcirkel 158,1, verhouding 1,27).
  - Taraz → Almaty-2: 546,5 km (tool 542,1, grootcirkel 453,8, verhouding 1,19).
  - Almaty-2 → Aktogay: 586,8 km (tool 584,1, grootcirkel 471,8, verhouding 1,24).
  - Aktogay → Dostyk: 332,3 km (tool 331,5, grootcirkel 273,6, verhouding 1,21).
  - Dostyk → Alashankou: 17,6 km (tool 17,1, grootcirkel 11,3, verhouding 1,51 — kort stuk, absolute
    afwijking klein).
  Totaal spoor 1.979,2 km tegen ~1.850 km hemelsbreed-som via-punten uit de brief (geen gepubliceerde
  spoorkm) = **+6,98%** — indicatie, geen harde norm (brief §2/§7, "het gemeten getal wordt de nieuwe
  waarheid"). De gauge-breuk bij Dostyk/Alashankou (1520→1435 mm) blokkeerde de router niet (OSM-topologie
  is gauge-onafhankelijk); het laatste stukje is wél als apart been gehouden zoals de brief voorstelde,
  zodat de wissel zelf zichtbaar blijft als eigen segment (niet apart gemodelleerd als eigen modaliteit).
- Alle 3 markers uit §3 zijn meegenomen; geen fase D/E (Alashankou-spoorstation is het opgedragen
  keten-eindpunt, brief §5/§6).

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **Naden tussen alle 8 benen ≤ 0,024 km** — ruim binnen de ≤5 km-norm; de acht segmenten sluiten
  vloeiend op elkaar aan (de reisvolgorde is de aaneenschakeling, geen los te trekken punt).
- **`toets_knikken.py`: 16 knikken ≥60°, waarvan 9 omkeringen (≥150°), waarvan 6 TERUGLOOP** (de enige
  categorie die reparatie zou vragen):
  - b1 (truck) draagt 7 spikes <60 m boogstraal — OSM-zigzag op de scan, geen echte knik (het tool noemt
    dit zelf "spike", geen terugloop).
  - Twee TERUGLOOP-punten bij **43,282–43,290 / 68,204–68,219** (grens been b2↔b3, bij Turkestan) — een
    kort overschiet-en-terug op de naad tussen twee onafhankelijk gebakken spoorsegmenten die elk apart
    op de dichtstbijzijnde hoofdnet-knoop bij het Turkestan-via-punt snappen (er bestaat geen `--via` in
    de spoorrouter, dus de twee runs raken elkaar niet perfect op de doorgaande as). Niet dichtgetrokken
    door het via-punt te verschuiven (dat zou de km-toets sturen in plaats van meten); staat hier als
    bevinding.
  - Vier TERUGLOOP/scherpe-bocht-punten bij **46,958–46,964 / 79,685–79,693** (grens been b6↔b7, bij
    Aktogay) — dezelfde klasse, en verwacht: de brief noemt het Aktogay-via-punt zelf al als
    "bij benadering, geen los OSM-stationspunt gevonden" (§4/§7); de snap zelf is met 0,27 km ruim binnen
    de norm, maar de doorgaande hoofdlijn maakt hier een lokale bocht/vertakking die de twee los gebakken
    segmenten elk net iets anders aandoen. Niet dichtgetrokken, staat als bevinding conform brief §7.
  - De overige 3 segmenten (Shymkent→Taraz, Taraz→Almaty-2, en de rest van Almaty-2→Aktogay) hebben
    **0 omkeringen**.
- **`toets_rechte_benen.py --min-km 5`:** geen enkel been van deze stroom staat in de wereldwijde
  verdachtenlijst (alle 8 benen zijn echte, meerpuntige geometrie — geen rechte stippels in deze keten).
- **Marker-afstand tot de lijn:** Kharasan-plant 0,0 m · Zhanakorgan-station 0,0 m ·
  Alashankou-station 335,8 m (anker ≠ exact routeerpunt op het emplacement — binnen de ~0,5 km-norm).
- **JSON-vormtoets:** `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, spoor} (beide toegestaan),
  elk been ≥2 punten, bestand 66,7 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:**
- Een steppe-/woestijnverbinding zonder gebronde corridor (b1) kan tóch een doorgaand OSM-wegpad
  opleveren — de brief hield rekening met "geen wegpad" als uitkomst, maar hier vond de scanner een
  reëel pad van 34,3 km, wat de brief-schatting van ~31 km hemelsbreed als redelijk bevestigt (+10,8%,
  binnen de orde van grootte van een niet-rechtlijnige toegangsweg over 31 km hemelsbreed).
- Zeven aparte `toets_spoorroute.mjs`-runs zonder `--via` aan elkaar zetten (het `uranium-inkai-poti`-
  patroon) werkt hier over een grensoverschrijdende corridor van bijna 2.000 km, inclusief een
  gauge-breuk die de router niet blokkeert — de OSM-topologie kent geen spoorwijdte, dus de wissel bij
  Dostyk/Alashankou is puur een geografisch/operationeel feit, geen routeerbelemmering.
- De enige twee TERUGLOOP-clusters liggen precies op de twee via-punten die de brief zelf al als
  "aannemelijk"/"bij benadering" markeerde (Turkestan als corridorkeuze zonder eigen brontwijfel, en
  vooral Aktogay met een expliciete disclaimer) — een aanwijzing dat een naad-overschot in
  `toets_knikken.py` een nuttige, goedkope secundaire indicator is voor een via-punt dat zelf al onzeker
  was, zonder dat het de km-toets zou hebben opgemerkt.
