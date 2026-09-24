# De lichte routebrief — werkwijze én sjabloon (M29)

*Vastgelegd 2026-09-24 op besluit van Lars (2026-09-22/24): de gemeten routes zijn de vorm, nu
koper **verhaal-compleet** maken — één gemeten keten per handelsas plus een wereldwijde sitelaag.
Zijn randvoorwaarde: "elke stroom met dezelfde hoeveelheid aandacht als die we nu hebben vereist
veel te veel; we moeten iets sneller zodat het visuele plaatje sneller in beeld komt." Dit is die
snellere werkwijze. De volledige werkwijze (`routebrief-werkwijze.md`) blijft de norm voor de zes
bestaande brieven en voor elke keten die later alsnog een ankercheck-ronde krijgt.*

## 1 · Wat er verandert, en wat niet

Doel: per as één gemeten keten op de bol, in **één werkblok per keten** (brief ± een halve dag,
bake + bol ± een halve dag). Het verhaal — waar het koper vandaan komt, waar het overgaat, waar
het heen gaat — is het product. De 100 m-precisie van kop en staart is dat niet meer.

| | volledig (werkwijze 2026-07-24/28) | licht (M29) |
|---|---|---|
| brief | 600–1.100 regels; elke plaats onderweg; productvraag-ladder per kade; negatieve ankers | **≤ ~100 regels**: ketenkaart, benen-tabel, ankers, knopen, stoppunt, open punten |
| ankers | satelliet-gelegd op z16–z19 (grid-stitch), 5 decimalen, twee ankers per overslag | **site-niveau**: 4 decimalen, één anker per overslag, één satellietblik (Esri z14–z15) om te zien dat het punt op het terrein/de kade ligt — geen grid-pass, geen verschuiven op de meter |
| via-punten | elke plaats waar de corridor doorheen gaat | **alleen waar een corridorkeuze bestaat** (splitsing, grensovergang, spoortak): 3–8 per landbeen |
| last mile | eigen been, eigen ankers, kleine wegklassen tot 12 km | **geen eigen been**: het landbeen eindigt op het site-anker; ligt de site > ~2 km van het net → stippel "last mile (geen net op deze korrel)" |
| fase D/E | verplicht tot eindproduct, bewijslast per fabriek | **D alleen als één bron de fabriek noemt**; E vervalt tenzij hij in één zin gegeven is; stoppunt in één zin beargumenteerd |
| toets | ankercheck-ronde (`toets_ankers.py`), dekking + verklikker | **de bake-uitvoer**: km per been binnen ±15% van de gepubliceerde lengte, geen naad > 5 km tussen benen, plus één blik op de bol |
| status-vocabulaire | satelliet-gelegd · bevestigd · aannemelijk · onzeker | **bron-gelegd** (één bron + satellietblik) · **aannemelijk** (één bron, niet gezien) · **onzeker** |

**Wat niet verandert — dit zijn de eerlijkheidsregels van de kaart, geen precisieregels:**

- **Stippel betekent nog steeds precies één ding: hier reikt het net niet** (werkwijze §7). Een
  gemeten been blijft doorgetrokken; een "aannemelijk" been (één bron voor de *bestemming*) wordt
  gewoon gemeten en doorgetrokken getekend — de onzekerheid zit in de brief en in de beennaam
  (`… (aannemelijk: één bron)`), niet in de lijnstijl.
- **Zee = router; spoor, weg, leiding en binnenvaart = via-punt → via-punt** (werkwijze §5/§6).
- **Coördinaten altijd lat, lon met decimale punt** (werkwijze §2).
- **Geen coördinaat verzinnen.** Een punt dat niet gevonden is blijft open, en de lijn eindigt
  waar het bewijs eindigt. Een markt-centroïde is geen anker.
- **Bakken via `bak_stromen.sh`** (één functie per stroom, in dezelfde commit als het json).
  Geen herbakes van bestaande stromen; extra velden gaan in een los metadatabestand.
- **Ankers die al bestaan worden hergebruikt**, niet opnieuw gelegd: Rotterdam RHB
  (51.8935, 4.4585), Tongling-kade (30.98656, 117.7718), Beilun-losberth (29.9364, 121.883),
  Yangtze-monding (31.42704, 121.47618), Duisburg Becken A (51.4518, 6.7565), Kamoa (-10.76, 25.28).

## 2 · Het gereedschap per modaliteit — bestaand, geen nieuw tool

| modaliteit | hoe de geometrie ontstaat | in `bak_stromen.sh` |
|---|---|---|
| zee | MARNET routeert kade → kade | `--been "zee\|naam\|lat,lon\|lat,lon"` |
| zee, waar MARNET niet tot de kade reikt | `maak_havenaanloop.py --van … --naar …` (kortste pad over water) | `--stippel-geojson "zee\|haven-aanloop …\|…geojson"` |
| spoor | `node v2/tools/toets_spoorroute.mjs --van=… --naar=… --naam=…` over het 1-op-1-spoornet; corridorkeuze = meerdere runs kop→via, via→staart en de stukken achter elkaar | `--been-geojson "spoor\|naam\|…geojson"` |
| weg | profiel in `maak_stroombeen_weg.py` (extracts, via-punten, refs, gepubliceerdKm, vensterKm) | `--been-geojson "truck\|naam\|…geojson"` |
| binnenvaart | Rijn/Mississippi: `--been` over de AIS-graaf; elders `maak_rivierbeen.py` over de bulklaag | `--been` resp. `--been-geojson "binnenvaart\|…"` |
| leiding / band | OSM-way (`man_made=pipeline`) waar hij gekarteerd is, anders stippel | `--been-geojson "leiding\|…"` resp. `--stippel "leiding\|…"` |
| eigen terrein / last mile zonder net | rechte lijn, gestippeld, reden in de naam | `--stippel "truck\|last mile … (geen net)\|…\|…"` |

De **markers** zijn de ankers uit §3 van de brief — één per site en per overslag. Die worden
vanzelf gloedhotspots (`gloed.js`), dus de sitelaag en de stroom lichten op dezelfde plek op.

## 3 · Sjabloon

```markdown
# Routebrief (licht) · koper — <van> → <naar>

**stroom-id:** `koper-<van>-<naar>` · **geschreven:** <datum> · **werkwijze:** licht (M29) ·
**status:** concept | gebakken | op de bol
**Keten in één zin:** <product, modaliteiten, corridors, eindpunt>
**Welke as van het verhaal:** <bv. "Andes-concentraat naar Chinese smelters" — jaarvolume + bron>

## 1 · Ketenkaart
<mijn> ──(b1 <modaliteit> · <corridor> · ~<km>)──► <haven> ──(b2 zee · ~<km>)──► <haven>
──(b3 <modaliteit>)──► <smelter> ──(b4 <modaliteit>, aannemelijk)──► <fabriek>

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | <mijn> → <haven> | <N-weg / spoorlijn / leiding> | <km> [n] | maak_stroombeen_weg | nee |
| b2 | B | zee | <haven> → <haven> | — | <km> | MARNET | aanloop: ja/nee |
| b3 | C | spoor | <haven> → <smelter> | <lijn> | <km> [n] | toets_spoorroute | nee |
| b4 | D | truck | <smelter> → <fabriek> | | <km> | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-<x>-laad` | mijn / laadplek | | | [n] | bron-gelegd (z15 gezien: <wat je zag>) |
| `cu-<x>-kade` | overslag | | | [n] | |
| `cu-<x>-smelter` | losplek / smelter | | | [n] | |
| `cu-<x>-fabriek` | fabriek | | | [n] | aannemelijk |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|

## 6 · Stoppunt
<één zin: waar de brief ophoudt en waarom (eindproduct, of geen gedocumenteerde volgende locatie)>

## 7 · Open punten
- <wat niet gevonden is en dus niet getekend wordt>

## 8 · Bronnen
[1] <bron, jaar, url>
```

## 4 · De satellietblik in de praktijk

`python v2/tools/sat_check.py` stitcht Esri World Imagery rond een punt (zie de docstring voor
de vlaggen). Voor de lichte brief volstaat **één beeld op z14–z15 per anker**: ligt het punt op
het terrein, de kade of het emplacement dat de bron noemt? Ja → status *bron-gelegd*, noteer in
één zin wat je zag (kranen, stapels, pit, rookpluim). Nee → verschuif naar wat je wél ziet én
schrijf dat op; twijfel → *onzeker* en open punt. Niet doorzoomen tot z18, niet meten op de meter.
