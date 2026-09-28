# Routebrief (licht) · koper — Antamina → Huarmey → Huangshi (China)

**stroom-id:** `koper-antamina-daye` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken
**Keten in één zin:** koperconcentraat uit de Antamina-mijn (Ancash, Peru; BHP/Glencore/Teck/Mitsubishi-jv)
per **slurryleiding** (~302 km, eigen infrastructuur) naar de kade Puerto Punta Lobitos bij Huarmey, per
**zeeschip** (via een lange haven-aanloop naar MARNET-zeeknoop 166) naar de Yangtze-monding, en per
**binnenvaart** stroomopwaarts — het eerste stuk gedeeld met `koper-collahuasi-tongling` — tot de
Yangtze-oeverzone bij **Huangshi (Hubei)**, waar 大冶有色金属集团 (Daye Nonferrous Metals, een van
China's grootste koperhutten) zetelt; de brief stopt op de kade, want geen bron noemt Daye als
naam-afnemer van déze lading.
**Welke as van het verhaal:** reserve-as (golf 2) — tweede Peru-as los van Las Bambas, met een eigen
kusthaven (Huarmey) en een Chinese bestemming ten westen van de al drie keer gebruikte Tongling/Guixi-kant.
Jaarvolume: **≈410 kt koperconcentraat/jaar** (Wikipedia "Antamina mine", peiljaar 2024).

## 1 · Ketenkaart
Antamina-mijn ──(b1 leiding · stippel · ~302 km)──► Huarmey/Punta Lobitos-kade
  ──(b2a haven-aanloop · stippel · ~200 km)──► MARNET-zeeknoop 166
  ──(b2b zee · MARNET · ~17.800 km)──► Yangtze-monding
  ──(b3 binnenvaart · GEDEELD `koper-collahuasi-tongling`-b3 · 516,6 km)──► Tongling-rivierpunt
  ──(b4 binnenvaart · NIEUW · ~390 km, schatting)──► Huangshi-kade (stoppunt, onzeker)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Antamina-mijn → Huarmey-kade | Antamina-concentraatpijpleiding (eigen infrastructuur, hooglandtracé Ancash–kust) | ~302 [1] | stippel | **ja** — schematisch, geen OSM-way verwacht op dit Andes-tracé (bindend uit de toets; twee gerichte Nominatim-pogingen leverden niets op) |
| b2a | B | zee (haven-aanloop) | Huarmey-kade → zeeknoop 166 (-10,0000/-80,0000) | kortste pad over water, MARNET reikt niet tot de kade | ~200 [2] | maak_havenaanloop.py, timeout 300 | **ja** — kade ligt 199,7 km van de dichtstbijzijnde zeeknoop (toets, bindend); bij timeout: rechte stippel-terugval |
| b2b | B | zee | zeeknoop 166 → Yangtze-monding (31,42704, 121,47618) | Stille Oceaan-oversteek, zelfde patroon als bestaande Peru/Chili→China-stromen | ~17.800 (schatting, te bakken) [3] | MARNET | nee |
| b3 | C | binnenvaart | Yangtze-monding → Tongling-rivierpunt (30,98656, 117,7718) | Yangtze, **GEDEELD been = `koper-collahuasi-tongling`-b3**, letterlijke kopie | 516,6 (gebakken, [4]) | maak_rivierbeen.py (bestaand geojson hergebruiken) | nee |
| b4 | C | binnenvaart | Tongling-rivierpunt → Huangshi-kade (30,2100, 115,0750) | Yangtze, stroomopwaarts voorbij Tongling, **NIEUW** stuk | ~390 (schatting o.b.v. omwegfactor 1,45× van hemelsbreed 272,2 km — dezelfde factor als het gedeelde b3-stuk; geen gepubliceerde rivier-km gevonden) [5] | maak_rivierbeen.py (MARNET-bulklaag — Yangtze heeft geen AIS-dekking) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-antamina-laad` | mijn / laadplek | Antamina-mijn (open pit + concentrator), Ancash | -9,5372, -77,0611 | [6] + satelliet (z15, 2026-09-28: open pit met concentrische afgravingsringen, wegennet naar concentrator-terras rond het middelpunt) | bron-gelegd |
| `cu-antamina-huarmey-kade` | overslag | Puerto Punta Lobitos – Antamina, Huarmey | -10,1035, -78,1788 | [7] + satelliet (z15, 2026-09-28: pier met aangemeerd schip, industrieterrein direct landinwaarts — bevestigt de Nominatim-treffer uit de toets) | bron-gelegd |
| `cu-huangshi-kade` | losplek (stoppunt) | Yangtze-oeverfront Huangshi, Hubei (bij Daye Nonferrous) | 30,2100, 115,0750 | [8] + satelliet (z14/z15, 2026-09-28: stedelijke rivieroever met aanlegsteigers/vaartuigen op de Yangtze, geen specifiek 大冶有色-dok herkenbaar) | **onzeker** — algemene havenzone van de stad, niet de exacte kade van de kopersmelter (open punt §7) |

## 4 · Via-punten
*(geen — deze keten heeft geen wegbeen met een corridorkeuze; leiding en binnenvaart routeren via-punt→via-punt binnen hun eigen tool)*

## 5 · Verwerkingsknopen
*(geen — de brief stopt op de kade, vóór de smelter; zie §6)*

## 6 · Stoppunt
De brief stopt op de Huangshi-kade: 大冶有色金属集团 (Daye Nonferrous Metals, "'s werelds grootste TSL-smelter"
in Huangshi/Hubei, WebSearch [8]) is een reële, van Tongling/Guixi onderscheiden koperhut aan de Yangtze die
volgens Chinese bronnen geïmporteerd koperconcentraat via de Huangshi-havenzone ontvangt, maar geen bron
noemt Antamina/Peru-concentraat als naam-lading naar déze specifieke hut — fase D (kade→fabriekspoort) zou
zonder die bron verzonnen zijn.

## 7 · Open punten
- Fase A (pijpleiding, ~302 km) is bij voorbaat als stippel behandeld, conform de bindende toets; blijkt het
  bakken toch een OSM-way op te leveren, dan wordt dat been doorgetrokken.
- De haven-aanloop Huarmey→zeeknoop 166 (~200 km) is een reëel timeoutrisico (300 s-limiet); bij mislukking
  is de rechte stippel-terugval de eindvorm, niet een tweede poging.
- **`cu-huangshi-kade` is een algemene havenzone, geen bedrijfskade.** Binnen het webbudget van deze sessie
  (max. 3 WebSearch, geen firecrawl — credits op) is geen OSM-object of registerpunt voor 大冶有色's eigen
  losdok gevonden; de gekozen coördinaat ligt in de stedelijke havenzone van Huangshi (黄石港区) waar Chinese
  bronnen "geïmporteerd ijzererts, koperconcentraat, schroot" als vrachtsoort noemen, niet op het exacte
  terrein van de smelter. Een vervolgronde met een Chinees registerpunt (MEE-emissieregister o.i.d., het
  recept uit `zoek-chinees-adres-recept.md`) kan dit naar bron-gelegd optillen.
- **Bewuste diversiteitskeuze, niet stilzwijgend:** drie bestaande koperketens (Chuquicamata, Collahuasi,
  Las Bambas) eindigen al op de Tongling-kade. Deze brief kiest doelbewust Huangshi (een andere Chinese
  koperhut, ~270 km stroomopwaarts van Tongling) om die convergentie niet nog verder op te stapelen — precies
  de afweging die de toets openliet. Wordt bij het bakken alsnog gekozen voor hergebruik van de Tongling-kade
  (bijv. omdat Huangshi niet haalbaar blijkt), dan is dat een resultaat, geen stille terugval.
- Geen cargo-specifieke bron koppelt Antamina aan één met-naam-genoemde Chinese smelter (zelfde patroon als
  bij Las Bambas/Collahuasi) — de aanname "naar China" steunt op het algemene Peru-concentraatpatroon.
- Rivier-km Tongling→Huangshi (~390 km) is een schatting op basis van de omwegfactor van het gedeelde
  Yangtze-monding→Tongling-stuk; geen gepubliceerde vaarwegkilometrering voor dit traject gevonden.
- Antamina's levensduur: sluiting rond 2028 met een investeringsscenario tot 2036 (Wikipedia) — geen
  blokkade voor een huidige-stand-atlas.

## 8 · Bronnen
[1] Antamina-concentraatpijpleiding, ~300–302 km, Ancash-hoogland → Puerto Punta Lobitos/Huarmey —
    bedrijfscijfer, zoals eerder vastgelegd in `data/copper.js` (v1) en bevestigd door het algemene publieke
    beeld van deze pijpleiding als een van de langste concentraatleidingen ter wereld.
[2] Gemeten zeeknoop-afstand Huarmey-kade → MARNET-zeeknoop 166 (-10,0000/-80,0000): 199,7 km — uit de
    haalbaarheidstoets van deze as (`golf4-assen.json`, veld `toets.webcheck`).
[3] Schatting op basis van vergelijkbare Peru/Chili→China-zeeroutes in deze atlas (Escondida→Guixi,
    Collahuasi→Tongling, Las Bambas→Matarani-Tongling: 17.000–19.800 km totaal); exacte km volgt uit de bake.
[4] `v2/design/routebrieven/koper-collahuasi-tongling.md`, been b3 (Yangtze-monding → Tongling-kade, oostgeul,
    516,6 km gebakken) — letterlijk te hergebruiken geojson/beenregel.
[5] Eigen berekening (haversine) op de coördinaten van `cu-tongling-kade` (30,98656, 117,7718, bestaand anker)
    en `cu-huangshi-kade` (30,2100, 115,0750): hemelsbreed 272,2 km; omwegfactor 1,45 afgeleid uit hetzelfde
    stuk Yangtze-monding→Tongling (hemelsbreed 355,7 km tegen 516,6 km gebakken).
[6] Wikipedia, "Antamina mine" (geraadpleegd 2026-09-28): coördinaat -9,5372/-77,0611, 410.000 t
    koperconcentraat in 2024, jv Teck/BHP/Glencore/Mitsubishi Corporation, open pit op 4.300 m hoogte.
[7] Nominatim (OpenStreetMap, ODbL): "Puerto Punta Lobitos - Antamina", -10,1035/-78,1788, industrieterrein —
    zelfde treffer als in de haalbaarheidstoets van deze as; satelliet z15 (2026-09-28) bevestigt pier +
    aangemeerd vaartuig.
[8] WebSearch (2026-09-28), o.a. Bloomberg-bedrijfsprofiel "Daye Nonferrous Metals Group Holdings", Britannica
    "Daye", Metso-case study "DAYE copper smelter": Daye Nonferrous Metals/China Daye Non-Ferrous Metals
    Mining (HK:661) heeft zijn belangrijkste kopersmelter ("'s werelds grootste TSL-smelter") in Huangshi,
    Hubei, aan de Yangtze, ~90 km ten zuidoosten van Wuhan; Chinese bronnen (黄石市港航局-documentatie, via
    WebSearch) noemen geïmporteerd ijzererts/koperconcentraat/schroot als de belangrijkste vrachtsoorten van
    de Huangshi-havenzone. Geen van beide bronnen noemt Antamina/Peru als herkomst.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Bestand:** `v2/data/stroomroute-koper-antamina-daye.json` (124,3 KB, contract versie 2, `punt_formaat`
`lonlat`) · **5 benen · 18.203,8 km · 6.679 punten · 3 markers**.

| # | modaliteit | km | punten | stippel | naad met vorige been |
|---|---|---|---|---|---|
| b1 | leiding | 137,7 km (rechte lijn — het gepubliceerde tracé is ~302 km) | 2 | ja | — (eerste been) |
| b2a | zee (haven-aanloop) | 202,1 km | 183 | ja | 0,00 km |
| b2b | zee (MARNET) | 16.946,4 km | 1.738 | nee | 0,00 km |
| b3 | binnenvaart (gedeeld) | 516,5 km | 2.674 | nee | 1,82 km |
| b4 | binnenvaart (nieuw) | 401,1 km | 2.082 | nee | 0,00 km |

**Recept:** `bash v2/tools/bak_stromen.sh koper-antamina-daye` → functie `bak_koper_antamina_daye()`
in `v2/tools/bak_stromen.sh` (ingevoegd vóór de dispatch-anker). Geen wegbeen in deze keten, dus
`v2/tools/maak_stroombeen_weg.py` (PROFIELEN) is niet aangeraakt.

**Toelichting per stippel/aanloop/gedeeld been:**
- **b1 (leiding, stippel).** Vóór het bakken geverifieerd met `pyosmium` op het lokale
  `peru-latest.osm.pbf`: 349 `man_made=pipeline`-ways in heel Peru, waarvan 9 binnen de
  Antamina–Huarmey-bbox — geen daarvan draagt `substance=slurry` of vormt een doorlopend tracé over
  het Andes-hoogland (de 2 treffers vlak bij de kade zijn korte havenleidingen, niet de mijnleiding).
  Bevestigt de bindende aanname uit de brief. De 137,7 km die de bake toont is de **rechte
  hemelsbrede lijn** tussen de twee ankers (het tool tekent een stippelbeen ongerouteerd) — dat is
  geen tegenspraak met het gepubliceerde ~302 km-tracé (bedrijfscijfer, hooglandtracé met
  bochten); de ±15%-toets is hier niet van toepassing (geen gerouteerd been).
- **b2a (haven-aanloop Huarmey, stippel-geojson).** `maak_havenaanloop.py --naam
  koper-antamina-daye-huarmey`, binnen `timeout 300`, **geslaagd op de eerste poging** (geen
  fallback nodig): 202,1 km / 183 punten, omwegfactor 1,012 t.o.v. de rechte lijn (199,7 km, exact
  de in de brief genoemde zeeknoop-afstand). 0,41 km van de 1:10M-kustlijn ligt "over land" en
  grenst aan het kade-uiteinde zelf — dat is de korrel van de kustlijn (een kade ligt per definitie
  óp de 1:10M-landrand), geen fout.
- **b2b (zee, MARNET, doorgetrokken).** Zeeknoop 166 → Yangtze-monding, 16.946,4 km over 76
  MARNET-edges. Snap aan het Yangtze-monding-uiteinde 10,715 km — dat is de bestaande situatie van
  dit gedeelde ankerpunt (elke andere koper→Tongling-stroom in dit project routeert naar exact
  dezelfde 31.42704,121.47618 met dezelfde ordegrootte snap); niet dit bak-recept aangepast.
- **b3 (binnenvaart, GEDEELD, letterlijke kopie).** `--been-geojson` verwijst naar het **bestaande**
  `$BEEN/rivierbeen-yangtze-tongling-gedeeld.geojson` (Yangtze-monding → Tongling-kade, oostgeul,
  516,5 km / 2.674 punten) — exact hetzelfde bestand dat `koper-lasbambas-matarani` en
  `koper-chuquicamata-china` al gebruiken. Niet opnieuw gebakken, geen tweede versie. Naad met b2b
  1,82 km — dezelfde vaste kop-naad die deze gedeelde rivierlijn ook in de andere twee stromen
  draagt (de zee-marker en het begin van de gedeelde rivierlijn liggen niet op exact hetzelfde
  punt); binnen de norm van ≤ 5 km.
- **b4 (binnenvaart, NIEUW, MARNET-bulklaag).** `maak_rivierbeen.py --marnet
  v2/build-cache/marnet-preais --van 30.98656,117.7718 --naar 30.2100,115.0750`: 401,1 km over 48
  bulklaag-edges, 2.082 punten. Tegen de schatting uit de brief (~390 km, o.b.v. omwegfactor 1,45×
  hemelsbreed 272,2 km) is dat **+2,8%** — ruim binnen zelfs de indicatieve marge, hoewel die marge
  hier geen norm is (geen gepubliceerde rivier-km, zie brief §7/[5]). **Procesgat:** het
  "naar"-uiteinde van de bulklaag snapt op bulk-knoop 21597, **3,19 km** van het exacte brief-anker
  `cu-huangshi-kade` (30,2100/115,0750) — er ligt geen precieze routeerknoop op die stedelijke
  Yangtze-oever. Conform de instructie in de bak-aanwijzing is dat punt **niet verschoven of
  verzonnen**; de 3,19 km is een gerapporteerd procesgat, samenhangend met de ONZEKERE status van
  het anker zelf (§3/§7 van de brief).

**Toets (§5 bakhandleiding-licht):**
- Km + naden: alle naden tussen opeenvolgende benen ≤ 5 km (grootste 1,82 km, b2b→b3); geen zee-snap
  > 5 km die om een nieuwe haven-aanloop vraagt.
- `toets_knikken.py --bestand v2/data/stroomroute-koper-antamina-daye.json`: 3 knikken ≥ 60°, waarvan
  1 omkering (**1 TERUGLOOP**) op been b4 (31.10910,117.76960, 173,2° over 88 m straal) — een
  MARNET-bulklaag-Dijkstra-artefact op de rivier boven Tongling, dezelfde soort punt als de
  al-bestaande "krappe bocht" op het gedeelde b3-been (31.17450,118.00110, 61,2°, 0 omkeringen
  daar). Dit been heeft geen via-punten (binnenvaart routeert kop→staart via de bulklaag zonder
  tussenstops), dus er is in de lichte werkwijze geen aangrijpingspunt om de bocht te verleggen
  zonder het punt te verzinnen — **bevinding, niet gerepareerd** (bakhandleiding §5: "andere
  afwijkingen = bevinding").
- `toets_rechte_benen.py --min-km 5`: alleen b1 (leiding, 137,7 km, omwegfactor 1,000) komt naar
  voren — dat hoort bij een stippelbeen en is geen bevinding.
- Contract: `versie` 2, `punt_formaat` `lonlat`, alle 5 modaliteiten in {zee, binnenvaart} (subset
  van de geldige set), elk been ≥ 2 punten, bestand 124,3 KB (< 300 KB-richtlijn).

**Lessen:**
- De pyosmium-pipeline-toets op de lokale peru-extract was in enkele seconden te draaien en gaf een
  hardere bevestiging dan de eerdere Nominatim-pogingen uit de brief — voor een volgende
  Andes-pijpleiding-stippel is dat de snellere eerste stap.
- Een gedeeld been (`--been-geojson` naar een bestaand bestand van een andere stroom) draagt zijn
  eigen historische naad mee; die naad hoeft niet opnieuw verklaard te worden per nieuwe stroom die
  hem hergebruikt, zolang hij binnen de norm blijft.
- Een MARNET-bulklaag-rivierbeen zonder via-punten kan een terugloop bevatten die de lichte
  werkwijze niet kan repareren (geen corridorkeuze om een via-punt op te zetten); dat hoort als
  bevinding in de brief, niet als blokkade voor het bakken.
