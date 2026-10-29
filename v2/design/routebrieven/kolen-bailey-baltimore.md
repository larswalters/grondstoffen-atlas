# Kolen · Pennsylvania Mining Complex → CONSOL Marine Terminal, Baltimore (VS)

**stroom-id:** `kolen-bailey-baltimore` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Keten in één zin:** thermische kolen uit het Pennsylvania Mining Complex (Bailey, Enlow Fork, Harvey; Core Natural Resources,
Greene County PA) gaan vanaf de centrale wasserij met dubbel laadstation per spoor (CSX/B&O via Connellsville en Cumberland) naar
de kolenkade van de CONSOL Marine Terminal in Curtis Bay, Baltimore. Eén spoorbeen, geen zee, geen fase D/E.
**Welke as van het verhaal:** Noord-Appalachen thermische kolen naar de Baltimore-exportkade over Class-I-spoor. PAMC 25,7 Mt (2024;
Bailey 10,8, Enlow Fork 9,2, Harvey 5,7) [1]; terminal 17,0 Mt verscheept in 2024, ~84% PAMC, dus ~14 Mt (afgeleid) [1].
**Eenheid: Mt kolen per jaar.** Bailey alleen is niet apart gekoppeld: de wasserij is gedeeld, dit is de PAMC-keten (§7).

## 1 · Ketenkaart
```
PAMC-wasserij + laadlus `kolen-bailey-laad` ─(b1a spoor · mijnlijn langs de Monongahela · 129,7 km)─► Connellsville (via)
─(b1b spoor · CSX/B&O via Cumberland, Hancock, Martinsburg, Brunswick · 431,6 km)─► CONSOL Marine Terminal `kolen-consol-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | A | spoor | `kolen-bailey-laad` → Connellsville | route-uitkomst over het 1-op-1-net, via Charleroi (zie §7) | hemelsbreed 70,3 km, geen spoorkm; proef 129,7 | toets_spoorroute (`BAKE_SUFFIX=-raw`) | nee (snap 0,15 km) |
| b1b | A | spoor | Connellsville → `kolen-consol-kade` | CSX/B&O-hoofdlijn via Cumberland [1][6] | hemelsbreed 272,3 km, geen spoorkm; proef 431,6 | toets_spoorroute (`BAKE_SUFFIX=-raw`) | nee (snap 0,07 km) |

Totaal proef 561,3 km tegen hemelsbreed 338,9 km (verhouding 1,66); er is geen gepubliceerde spoorkm: de ±15%-toets geldt als
indicatie, niet als norm. De vrije run kop → staart (zonder via) geeft dezelfde 561,3 km: de via pint de corridor, hij verandert hem niet.
Aannemelijk: de bron noemt beide spoorwegen, niet welke deze lading rijdt (zie §7); de beennaam draagt dat.
Het ontwerp-been 'laatste emplacement → kade' vervalt: de kade snapt op 0,07 km, dus geen havenspoor-stippel.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-bailey-laad` | wasserij / laadlus | Central Preparation Plant PAMC (Bailey/Enlow Fork), Greene County PA | 39.9732, -80.4121 | [1][5] | bron-gelegd (z16 gezien: silo's, transportbanden en een spoorlus rond de wasserij; 10-K 39°58'23.7"N 80°24'43.6"W = 39.9732,-80.4121; net snapt op 0,15 km; `sat-kolen-bailey-baltimore-wasserij-z16.png`) |
| `kolen-consol-kade` | overslag spoor → zeeschip | CONSOL Marine Terminal, Curtis Bay, Baltimore MD | 39.2609, -76.5650 | [1][3][5] | bron-gelegd (z15 gezien: groot zwart kolenpark op een ovaal spoorlus-terrein met een bulkschip aan de pier; net snapt op 0,07 km; `sat-kolen-bailey-baltimore-kade.png`) |
Verworpen kandidaten: GEM-punt 39.8529,-80.4540 (z14: kaal bospad met een kleine pad, geen rails binnen 10 km; mijnterrein, geen laadplek)
en OSM-dagbouwpunt 39.9619,-80.3997 (dagbouw, geen laadlus). Rukert Terminals (39.2669,-76.5705) is een andere kade en geen anker.

## 4 · Via-punten (alleen benen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1a/b1b | 1 | Connellsville, op de B&O-lijn | 40.0180, -79.5890 | pint de CSX/B&O-corridor (Cumberland) tegen de Norfolk Southern-variant via Harrisburg; snap 0,28 km, op de doorgaande lijn, niet in het centrum |
Cumberland, Hancock, Martinsburg en Brunswick passeert de route vanzelf (geen via nodig).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Central Preparation Plant | Core Natural Resources | ruwe kolen → gewassen thermische kolen | 8.200 ruwe ton/uur; laadstation 9.000 ton/uur over 19,3 mijl spoor | [1] |
| CONSOL Marine Terminal | Core Natural Resources | trein → bulkschip | ~20 Mt/j doorvoer, 1,1 Mt opslag; de enige Oostkust-kolenterminal met twee Class I-spoorwegen (NS en CSX) | [1] |

## 6 · Stoppunt
De brief eindigt op de kade: geen bron noemt een bestemming per lading, dus geen zeebeen (bol-overgang naar de zee-kolenstromen ontbreekt bewust).

## 7 · Open punten
- **Welke spoorweg rijdt de lading is niet gepubliceerd:** de 10-K noemt NS én CSX voor mijn en terminal [1]. Gemeten alternatief NS via Rutherford
  (Harrisburg): 516,9 + 182,2 = 699,1 km (180° omkering bij 40.2677,-76.8797, yard-kopmaak); niet getekend, CSX is korter (561,3 km).
- **Omkering 169,6° bij 40.1472,-79.8984 (Charleroi) in b1a:** Brownsville → Connellsville heeft in OSM geen directe lijn, de router steekt bij Charleroi
  de Monongahela over (63,8 km tegen 25 km hemelsbreed). Waarschijnlijk wye of OSM-kopmaak; niet verder uitgezocht, spoorbeen blijft doorgetrokken.
- **Geen Bailey-alleen-aandeel:** Bailey 10,8 Mt is één van drie mijnen op dezelfde wasserij; de terminal-84% geldt PAMC-breed [1] (~14 Mt afgeleid).
- **Spoorkm niet gepubliceerd** (hemelsbreed 338,9 km); geen echte spoorkm gevonden.
- **Kadepier niet apart gelegd:** het anker staat op de pierkop van de kolenterminal; de exacte laadpositie per schip is niet bepaald.
- **Sitelaag:** `kolen-sitelaag.json` kent Bailey en de CONSOL-terminal niet; centrale beslissing (kandidaat-sites: dit wasserij- en kade-anker).

## 8 · Bronnen
[1] Core Natural Resources, Form 10-K FY2024 (SEC EDGAR) — PAMC bediend door NS en CSX; wasserij 39°58'23.7"N 80°24'43.6"W; laadstation 9.000 t/u; Bailey 10,8, Enlow Fork 9,2, Harvey 5,7 Mt; terminal ~17,0 Mt, ~84% PAMC, ~20 Mt/j capaciteit. https://www.sec.gov/Archives/edgar/data/1710366/000171036625000010/ceix-20241231.htm
[2] Global Energy Monitor, "Bailey Mine" — ondergrondse langwandmijn, Greene County PA, open sinds 1984; 7,94 Mt in 2025. https://www.gem.wiki/Bailey_Mine
[3] Wikipedia, "Curtis Bay, Baltimore" — kolenterminals in Curtis Bay. https://en.wikipedia.org/wiki/Curtis_Bay,_Baltimore
[4] Wikipedia, "Francis Scott Key Bridge collapse" — terminals van CSX Curtis Bay en CONSOL Energy geïsoleerd in 2024. https://en.wikipedia.org/wiki/Francis_Scott_Key_Bridge_collapse
[5] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16): `v2/build-cache/satcheck/sat-kolen-bailey-baltimore-{wasserij,wasserij-z16,kade,gem}.png`.
[6] Proefroutes `toets_spoorroute.mjs` over het 1-op-1-net (`BAKE_SUFFIX=-raw`, 3.260.717 spoor-edges): `v2/build-cache/ais/graaf/spoorroute-kolen-bailey-baltimore-{b1a-conn,b1b-conn,vrij,ns1,ns2}.geojson`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
Functie `bak_kolen_bailey_baltimore` in `v2/tools/bak_stromen.sh`; uitvoer `v2/data/stroomroute-kolen-bailey-baltimore.json` (48,4 KB, versie 2, lonlat).
Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen), geen haven-aanloop, geen stippel, geen kopie.

| # | modaliteit | km (bake) | km (brief) | naad | punten | recept |
|---|---|---|---|---|---|---|
| b1a | spoor | 129,9 | proef 129,7 (hemelsbreed 70,3; geen spoorkm) | 0 | 638 | `spoorroute-kolen-bailey-baltimore-b1a-conn.geojson`, 1-op-1-net (`BAKE_SUFFIX=-raw`), hergebruikt uit de brieffase |
| b1b | spoor | 438,0 | proef 431,6 (hemelsbreed 272,3; geen spoorkm) | 0,000 | 1.889 | `spoorroute-kolen-bailey-baltimore-b1b-conn.geojson`, idem |

Totaal 567,9 km (brief 561,3; +1,2%, het verschil is puntsom tegen routeKm). Markers: wasserij 39,9732,-80,4121 (0,155 km van de lijn) en
CONSOL-kade 39,2609,-76,5650 (0,065 km); beide binnen 0,5 km. Naad b1a naar b1b 0 km (zelfde knoop, Connellsville).

**Toelichting.** Geen stippel: beide ankers snappen binnen 0,2 km op het net (geen last-mile, geen havenspoor). Geen zeebeen: de brief eindigt op de kade
(§6). De +-15%-toets is een indicatie omdat er geen gepubliceerde spoorkm is; beide benen liggen binnen 1,5% van de proef.
**Toetsen:** `toets_knikken.py` meldt een omkering van 169,6 graden bij 40,1472,-79,8984 (Charleroi) in b1a: route-uitkomst van het OSM-net
(Brownsville-Connellsville mist een directe lijn, 63,8 km tegen 25 km hemelsbreed), niet getekend weg; blijft doorgetrokken en staat in §7.
`toets_rechte_benen.py` meldt niets voor deze stroom.
**Lessen.** (1) Spoorbenen die in de brieffase al op het 1-op-1-net zijn geroutet kunnen letterlijk als `--been-geojson` worden hergebruikt: de bake is dan
alleen stikken en toetsen. (2) De NS-variant (699,1 km) is niet getekend; welke spoorweg deze lading rijdt blijft een open punt.
