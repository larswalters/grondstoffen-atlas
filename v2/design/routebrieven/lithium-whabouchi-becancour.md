# Routebrief (licht) · Lithium — Van → Via → Naar (land)

**stroom-id:** `lithium-whabouchi-becancour` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** spodumeenconcentraat van Nemaska Lithiums Whabouchi-mijn (Eeyou Istchee James Bay,
Quebec) gaat per b-double truck 405 km over Route du Nord en de Route Billy-Diamond (James Bay Road) naar het
spoor-overslagpunt in Matagami, en vandaar per trein 900 km naar de eigen Bécancour-conversiefabriek —
beide bronopgaven van Nemaska Lithium zelf.
**Welke as van het verhaal:** *project-as: beide knopen (mijn én conversiefabriek) hebben de bouw sinds eind
2025/maart 2026 opgeschort (Rio Tinto)* — **niet** "de eerste Noord-Amerikaanse lithiumas" als actieve claim.
De fysieke route (405 km truck + 900 km spoor, bevestigd via nemaskalithium.com) is wél echt en bron-gelegd;
het jaarvolume over déze as is **onzeker, mogelijk nul, met risico op verdere stopzetting** (§7). Vergelijkbaar
precedent, maar zwakker: `lithium-greenbushes-kemerton.md` (daar draait de mijn wél, staat alleen de eigen
raffinaderij stil; hier zijn beide knopen onvoltooide bouwplaatsen).

## 1 · Ketenkaart
```
Whabouchi-mijn/concentrator `li-wh-laadplek` ──(b1 truck · Route du Nord → Route Billy-Diamond
(James Bay Road) zuidwaarts · 405 km, bron: nemaskalithium.com)──► Matagami-overslagpunt
`li-mg-overslag` (truck→spoor, intermodaal) ──(b2 spoor · lijn niet bij naam gebrond · 900 km,
bron: nemaskalithium.com)──► Bécancour-conversiefabriek `li-bc-fabriek`
⏹ stoppunt (Nemaska Lithium/Rio Tinto — mijnbouw én fabrieksbouw beide opgeschort sinds eind 2025/maart 2026)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (spodumeenconcentraat) | `li-wh-laadplek` → `li-mg-overslag` | mijnweg → Route du Nord (aansluiting op Route Billy-Diamond ≈ km 276) → Route Billy-Diamond (James Bay Road) zuidwaarts naar Matagami, all-weather b-double weg | **405 km** — expliciet bedrijfscijfer (nemaskalithium.com/en/the-whabouchi-mine/: *"transported 405km by truck on an all weather road using b-double trucks to the established railyard in Matagami"*) [1] | maak_stroombeen_weg (extract `canada`, nieuw profiel) | nee |
| b2 | B | spoor (spodumeenconcentraat) | `li-mg-overslag` → `li-bc-fabriek` | spoorlijn Matagami zuidwaarts naar Bécancour — **exacte lijn/maatschappij niet bij naam genoemd** in de bron (*"railed to Bécancour"*, *"railcars"*); bij het bakken te bepalen met `BAKE_SUFFIX=-raw` op de canada-extract (toets_spoorroute.mjs, kop→staart, geen via-corridorkeuze gedocumenteerd) | **900 km** — expliciet bedrijfscijfer (nemaskalithium.com/en/the-whabouchi-mine/: *"will travel 900km to Bécancour"*) [1] | toets_spoorroute (BAKE_SUFFIX=-raw) | nee |

Totaal gedocumenteerde route: 1.305 km (1.305 km bron-cijfer, geen eigen schatting nodig — beide benen zijn
letterlijke bedrijfsopgaven).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-wh-laadplek` | mijn / laadplek | Whabouchi-mijn/concentrator (Nemaska Lithium) | 51.6878, -75.8952 | **hergebruik letterlijk** `w-li-whabouchi` uit `v2/design/lithium-sitelaag.json`/`.md` [2] | **bron-gelegd** (sitelaag: z14, "kruis op gerooide/opgehoogde industriezone aan een meer") |
| `li-mg-overslag` | overslag (truck→spoor, intermodaal) | Matagami-railyard ("established facility... used by numerous companies including the surrounding mines and Hydro Québec") [1] | 49.75833, -77.62194 | Wikipedia-centroïde van de plaats Matagami [3]; **geen** onafhankelijke satellietbevestiging van de exacte rail-yard mogelijk binnen deze ronde (§7) | **onzeker** — sat_check op z13–z16 rond dit punt toont waterzuiveringsbekkens en woonbebouwing, geen herkenbare rangeersporen/wagons; de echte yard ligt vermoedelijk elders in de plaats. Coördinaat blijft de plaats-centroïde tot een OSM-`railway=yard`-tag of een luchtfoto met zichtbare sporen hem vervangt. |
| `li-bc-fabriek` | conversiefabriek (losplek, stoppunt) | Bécancour-conversiefabriek (Nemaska Lithium) | 46.3583, -72.3938 | **hergebruik letterlijk** `w-li-becancour` uit `v2/design/lithium-sitelaag.json`/`.md` [2] | **bron-gelegd** (sitelaag: z14, "kruis direct op het fabriekscomplex in het industriepark, langs de Saint-Laurent") |

## 4 · Via-punten (b1 — corridorkeuzes op Route Billy-Diamond/James Bay Road)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Route du Nord × Route Billy-Diamond, junctie ≈ km 276/278 | 51.5082, -77.2785 | corridorkeuze: hier verlaat de as de oost-westverbinding (Route du Nord, mijn-uitgang) en slaat zuidwaarts af op de doorgaande James Bay Road — OSM-naam `Route du Nord` bevestigd op exact dit punt [4]; km-positie (≈276) sluit nagenoeg aan bij de "mijnkm ~276" van het ontwerp |
| b1 | 2 | Halte des Cascades de la Rivière Rupert, km 257, Route Billy-Diamond | 51.3532, -77.4202 | vaste doorgaande route (geen alternatief), rivierkruising Rupert; OSM-benoemd knooppunt met kilometerbord, bevestigt de doorgaande corridor zuidwaarts [4] |
| b1 | 3 | km 232, Route Billy-Diamond (mijlpaal) | 51.1835, -77.4657 | zelfde doorgaande corridor, tussenpunt dat de rechte OSRM/OSM-lijn zuidwaarts pint [4] |
| b1 | 4 | Halte de la route de la Baie-James, km 6, Route Billy-Diamond | 49.7723, -77.5759 | laatste punt van de doorgaande James Bay Road vóór Matagami — hier komt de as de plaats binnen [4] |

Geen via-punten voor b2 (spoor): de bron noemt geen tussenstation of corridorkeuze ("railed to Bécancour"),
en volgens de bakhandleiding krijgt spoor zonder gedocumenteerde vertakking één kop→staart-run op het
1-op-1-net (`BAKE_SUFFIX=-raw`).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Bécancour-conversiefabriek | Nemaska Lithium (Rio Tinto meerderheidsbelang sinds feb 2026 + Québec-overheid) | spodumeenconcentraat (SC5,5%) → lithiumhydroxide (LiOH·H2O) | contractvolume Ford-overeenkomst 2023: tot 100 kt SC5,5%/j → **13 kt LiOH·H2O/j ≈ 11 kt LCE/j** (13 × 0,88 wateraftrek-equivalent) [5]; sitelaag noemt daarnaast een eerste-fase-nameplate van 6 kt LCE-equivalent [2]; **bouw van de fabriek zelf is sinds maart 2026 vertraagd/"lever le pied"** — actuele/toekomstige productie onzeker [6][7] | [5][6][7] |

## 6 · Stoppunt
De brief stopt bij de poort van Bécancour: dit is Nemaska Lithiums eigen conversiefabriek en er is geen
gedocumenteerde volgende locatie op déze as (fase D vervalt — geen bron noemt een specifieke afnemersfabriek
voor het LiOH·H2O van Whabouchi/Bécancour; alleen de generieke vermelding "delivered to global markets via
the Port of Montréal" [1], onvoldoende voor een fase D-anker).

## 7 · Open punten
- **Beide knopen zijn NU bouw-opgeschort, niet slechts "partially built".** Whabouchi-mijnbouw staat "op het
  ijs" sinds december 2025 [8]; de Bécancour-conversiefabriek-**bouw** zelf is sinds maart 2026 vertraagd
  ("Nemaska Lithium doit lever le pied à Bécancour") [6], met doorlopende ontslagrondes (april/juli/september
  2026, inmiddels ~30% van het personeel) [9][10]. Eerste productie bij Bécancour wordt nu voorzien voor 2028,
  niet eerder [7].
- **Rio Tinto overweegt een overstap naar de Galaxy-afzetting (~100 km ten oosten van Whabouchi) in plaats van
  verder bouwen op Whabouchi.** Sinds de meerderheidsovername (feb 2026, $1,2 mrd publieke/Québec-financiering)
  evalueert Rio Tinto beide bronnen voor de spodumeenvoeding van Bécancour; een beslissing wordt nu verwacht in
  H2 2026 (eerder H1 2026) [7]. **Bij een keuze voor Galaxy vervalt dit ankerpaar (`li-wh-laadplek` +
  het hele b1-been) voor déze as, en moet de as vóór het bakken heroverwogen worden.**
- **Spoorlijn-identiteit Matagami → Bécancour blijft ongebrond.** De bron noemt alleen "railed"/"railcars",
  geen maatschappij of lijnnaam. Bij het bakken: `BAKE_SUFFIX=-raw` op de `canada`-extract, kop→staart-run met
  `toets_spoorroute.mjs`; als de router een 900 km-pad binnen ±15% vindt is dat voldoende bevestiging, een
  grotere afwijking is een eigen bevinding voor §9.
- **Matagami-overslagpunt staat op de plaats-centroïde, niet satellietgecheckt op de daadwerkelijke rail-yard**
  (§3). Twee sat_check-passes (z13/z15/z16, `lithium-whabouchi-becancour-matagami-*`) toonden geen herkenbare
  rangeersporen binnen de kern van Matagami — mogelijk ligt de yard buiten de gescande cirkels, of is hij op
  deze resolutie niet van gewone bedrijventerreinen te onderscheiden. Bij het bakken: zoek eerst op een
  OSM-`railway=yard`/`railway=station`-tag in de `canada`-extract rond Matagami; vind je die, gebruik dat punt
  i.p.v. de centroïde.
- **Geen fase D/E**: geen bron noemt een specifieke afnemersfabriek voor het Bécancour-hydroxide (§6).
- Dit is qua bewijsstatus vergelijkbaar met `lithium-greenbushes-kemerton.md`
  (aannemelijk/onzeker volume, doorgetrokken lijnen) maar **zwakker** dan het door het ontwerp aangehaalde
  `lithium-greenbushes-kemerton`/`lithium-greenbushes-zhangjiagang`-precedent: daar draait de mijn zelf wél,
  hier zijn beide knopen onvoltooide bouwplaatsen zonder bevestigde herstartdatum.

## 8 · Bronnen
[1] Nemaska Lithium, "The Whabouchi Mine" — https://nemaskalithium.com/en/the-whabouchi-mine/ (opgevraagd
2026-09-28 via directe curl-fetch; bevestigt letterlijk "405km by truck ... to the established railyard in
Matagami" en "900km to Bécancour", en "The mine is partially built and will continue to be constructed at the
right time to bring online with the conversion facility").
[2] `v2/design/lithium-sitelaag.json`/`.md` — ankers `w-li-whabouchi` (51.6878, -75.8952, bron-gelegd) en
`w-li-becancour` (46.3583, -72.3938, bron-gelegd), beide letterlijk hergebruikt (§3).
[3] Wikipedia (via de MediaWiki-API), "Matagami" — https://en.wikipedia.org/wiki/Matagami — coördinaat
49.75833,-77.62194 (plaats-centroïde, geen rail-yard-bevestiging; zie §7).
[4] OpenStreetMap (ODbL) via Nominatim — "Route du Nord" (way 1044057021, 51.5082,-77.2785); "Halte des
Cascades de la Rivière Rupert, km 257" (node 6001112215, 51.35338,-77.42041) en het bijbehorende
"km 257"-mijlpaalnode (547520079, 51.35145,-77.41465); "km 232" (node 5010435952, 51.18350,-77.46568); "Halte
de la route de la Baie-James, km 6" (way 172058388, 49.77232,-77.57586); "Route Billy-Diamond" als officiële
huidige naam van de James Bay Road. https://nominatim.openstreetmap.org (opgevraagd 2026-09-28).
[5] SEC EDGAR, Nemaska Lithium / Arcadium/Livent-gerelateerd technisch rapport, Exhibit 96-1 —
https://www.sec.gov/Archives/edgar/data/1742924/000114036123045135/ny20009544x3_ex96-1.htm — Ford-
leveringsovereenkomst 2023: tot 100 kt SC5,5%/j spodumeenconcentraat → 13 kt LiOH·H2O/j.
[6] La Presse, "Projet phare de la filière des batteries | Nemaska Lithium doit lever le pied à Bécancour"
(2026-03-13) — https://www.lapresse.ca/affaires/2026-03-13/projet-phare-de-la-filiere-des-batteries/nemaska-lithium-doit-lever-le-pied-a-becancour.php
[7] Rio Tinto, persbericht "Rio Tinto assumes majority interest and management responsibilities at Nemaska
Lithium" (feb 2026) — https://www.riotinto.com/en/news/releases/2026/rio-tinto-assumes-majority-interest-and-management-responsibilities-at-nemaska-lithium
— bevestigt de evaluatie Whabouchi vs. Galaxy-afzetting voor de spodumeenvoeding van Bécancour, beslissing nu
verwacht H2 2026, eerste productie Bécancour 2028.
[8] La Presse, "Filière québécoise des batteries | Nemaska Lithium met son volet minier sur la glace"
(2025-12-05) — https://www.lapresse.ca/affaires/2025-12-05/filiere-quebecoise-des-batteries/nemaska-lithium-met-son-volet-minier-sur-la-glace.php
[9] La Presse, "Ralentissement chez Nemaska Lithium | Près de 10% de l'effectif mis à pied" (2026-04-04) —
https://www.lapresse.ca/affaires/entreprises/2026-04-04/ralentissement-chez-nemaska-lithium/pres-de-10-de-l-effectif-mis-a-pied.php
[10] La Presse, "Projet phare de la filière batterie | Les licenciements s'accumulent chez Nemaska Lithium"
(2026-09-02) — https://www.lapresse.ca/affaires/entreprises/2026-09-02/projet-phare-de-la-filiere-batterie/les-licenciements-s-accumulent-chez-nemaska-lithium.php
[11] Geofabrik, `canada-latest.osm.pbf` — lokaal in `v2/build-cache/geofabrik/`, wegnet- en spoornet-extract
voor de bak-agent (`maak_stroombeen_weg.py --bron geofabrik`; `toets_spoorroute.mjs` met `BAKE_SUFFIX=-raw`).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Stroom:** `lithium-whabouchi-becancour` · **bestand:** `v2/data/stroomroute-lithium-whabouchi-becancour.json` (95,0 KB) ·
**recept:** `bak_lithium_whabouchi_becancour()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh lithium-whabouchi-becancour`).

**2 benen · 1.539,0 km · 4.882 punten · 3 markers**, beide DOORGETROKKEN (geen enkele stippel):

| # | fase | modaliteit | km | naad met vorig been | km-toets |
|---|---|---|---|---|---|
| b1 | A | truck | 401,1 | — (start) | 405 km bron → **−1,0%** [OK] |
| b2 | B | spoor | 1.137,9 | **7,28 km** | 900 km bron → **+25,7%** [BUITEN ±15% — bevinding] |

**Toelichting per been (bevindingen §5/§6 van de bakhandleiding):**
- **b1 (truck, profiel `lithium-whabouchi-becancour-whabouchi-matagami`, extract `canada`):** venster 70 km,
  `corridorKlassen: [tertiary, unclassified]` (Route du Nord en de James Bay Road zijn deels lager
  geklasseerd in OSM, zoals de bak-aanwijzing voorspelde). Scan gaf **401,0–401,1 km** tegen het bedrijfscijfer
  405 km = **−1,0%**, ruim binnen ±15%. Eén keerlus gesnoeid (0,23 km dubbel gereden stuk bij het Matagami-
  eind). Alle vijf via-punten uit §4 van de brief zijn in reisvolgorde meegenomen; het eindanker Matagami
  blijft de **plaats-centroïde** (zie hieronder) — géén `railway=yard`/`station`-tag dichterbij gevonden in de
  `canada`-extract tijdens deze scan.
- **b2 (spoor, `BAKE_SUFFIX=-raw`, kop→staart, geen `--via`):** `toets_spoorroute.mjs` snapt op het
  canada-hoofdnetcomponent van 392.614 km aan beide uiteinden (Matagami-zijde **7,28 km**, Bécancour-zijde
  0,25 km) en volgt een reële lijn: zuidwaarts vanaf Matagami via Senneterre-omgeving en de La Tuque-corridor,
  dan naar het zuiden tot in de buurt van Montreal (~45,48°N/−73,69°O, het zuidelijkste punt van de route),
  en vandaar weer oostwaarts naar Bécancour. Route **1.131,1–1.137,9 km** (toets_spoorroute resp.
  hecht_marnet-uitvoer; klein verschil door de snap-stub) tegen grootcirkel 541,9 km (**ratio 2,09**) en tegen
  het bedrijfscijfer 900 km (**ratio 1,26, +25,7%**). Conform de bak-aanwijzing ("retry met `--hoofd-km` alleen
  bij ratio > 1,3 óf een pad dat zichtbaar niet richting Trois-Rivières/Bécancour loopt") is **niet** opnieuw
  gedraaid: de ratio blijft onder 1,3 en de lijn loopt wél degelijk naar Trois-Rivières/Bécancour, alleen via
  een forse omweg door het zuiden. **Dit is de eerste keer dat de spoorlijn-identiteit Matagami → Bécancour
  wordt vastgesteld** (de bron noemt alleen "railed"/"railcars", geen maatschappij of lijnnaam) — de +25,7%
  t.o.v. het bedrijfscijfer is dus een **geografische bevinding** (een reële, langere spooromweg via het
  zuiden van Quebec, geen ontbrekend net en geen routeerfout) en blijft als zodanig staan, niet dichtgetrokken.

**⚠️ Naad b1→b2 = 7,28 km, BUITEN de 5 km-norm (bakhandleiding §5).** Been 1 eindigt exact op het
`li-mg-overslag`-anker (de Matagami-plaats-centroïde, 49,75833/−77,62194); been 2 begint op de dichtstbijzijnde
spoor-hoofdnetknoop, 7,28 km daarvandaan (49,71910/−77,70310). Dit is **geen zee-snap** (waarvoor de
haven-aanloop-regel geldt) en geen via-punt-fout — het is het rechtstreekse gevolg van de in §3/§7 al erkende
onzekerheid van het Matagami-anker (plaats-centroïde, geen bevestigde rail-yard-locatie; twee sat_check-passes
vonden geen rangeersporen). Dichttrekken zou een verzonnen verbinding tekenen; de naad blijft daarom staan als
openstaand punt (zie hieronder), net als de eerdere procesgat-precedenten in dit project.

**Ankers, status t.o.v. §3:** `li-wh-laadplek` en `li-bc-fabriek` blijven **bron-gelegd** zoals in §3 (hergebruikt
uit de lithium-sitelaag, ongewijzigd). `li-mg-overslag` blijft **onzeker** — geen `railway=yard`/`station`-tag
gevonden in de `canada`-extract tijdens deze bake die dichter bij het werkelijke overslagpunt ligt; het anker
blijft op de plaats-centroïde staan conform de bak-aanwijzing.

**Toets (bakhandleiding §5):**
- Naad b1→b2: **7,28 km** — buiten de 5 km-norm, verklaard hierboven (Matagami-ankeronzekerheid), geen
  via-punt bijgeschoven om het getal te halen.
- `toets_knikken.py`: **5 knikken ≥60°** (allemaal kleine spikes <20 m straal bij de mijnpoort, de James
  Bay Road-junctie en het Matagami-eind — OSM-zigzag, geen echte bochten), **0 omkeringen**, **0 terugloop**
  (de enige klasse die gerepareerd hoort te worden).
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de uitslag (beide benen zijn reële
  gerouteerde geometrie, geen omwegfactor 1,000).
- Markers: `li-wh-laadplek` **0,000 km**, `li-mg-overslag` **0,000 km** (matcht been 1-eind; ligt 7,28 km van
  het been 2-begin, zie de naad hierboven), `li-bc-fabriek` **0,247 km** (anker ≠ exact routeerpunt, binnen
  norm).
- `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteiten ⊂ {truck, spoor}, elk been ≥ 2 punten,
  bestand 95,0 KB (ruim onder ~300 KB).

**Gereedschapslessen:**
- **Een ratio-drempel (1,3) is scherper dan een percentage-drempel (±15%) om te beslissen of een spoorpad
  moet worden overgedraaid.** Bij ratio 1,26 (net onder de 1,3-grens) bleek een handmatige blik op de
  routepunten (zuidwaarts via Senneterre/La Tuque, dan naar Montreal-hoogte, dan terug oostwaarts) een
  plausibele reële spooromweg, geen artefact — de bak-aanwijzing had dit correct voorzien.
- **Een naad kan ontstaan door ankeronzekerheid, niet alleen door een netgat.** Bij Matagami is er geen
  ontbrekend net (het spoor-hoofdnet ligt er wél), maar het overslagpunt zelf is niet exact gelokaliseerd —
  de 7,28 km-naad is daarmee een directe doorwerking van een al bekend open punt uit §3/§7, niet een nieuwe
  bevinding op zichzelf.
- Beide slots (`weg`/`zwaar`) waren tijdens deze bake bezet door parallelle agenten; de wegscan (canada,
  6,4 GB pbf) duurde 150 s en de spoor-toets + bake enkele seconden, dus geen van beide liep tegen een
  slot-timeout aan.

**Centraal hersteld (2026-09-28, integratie golf 6):** de naad van 7,3 km tussen het Matagami-anker (plaats-centroïde) en de spoorkop (49.7191,-77.7031) is gedicht met een stippel "overslag Matagami: weg → spoorkop". Het anker blijft staan tot de overslaglocatie bevestigd is. 3 benen, 1.546 km.
