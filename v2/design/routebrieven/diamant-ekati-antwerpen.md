# Routebrief (licht) · diamant — Ekati → Antwerpen (AWDC)

**stroom-id:** `diamant-ekati-antwerpen` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** ruwe diamant van de Ekati-mijn (Northwest Territories, geen permanente weg — alleen
winterijsweg) vliegt eerst naar de sorteer-/splitsingsfaciliteit bij Yellowknife Airport, dan met een
tweede, interncontinentale vlucht naar Brucargo op Brussels Airport, en tot slot per truck naar de
AWDC/Diamond Office in de Antwerpse Diamantwijk voor handel en G7-certificering.
**Welke as van het verhaal:** *het "conflictvrije" premium-Canadese anker* — twee luchtbenen achter elkaar
omdat er geen wegnet naar de mijn is; Canada levert ~14% van het wereldvolume (~16 Mct/j, Diavik+Ekati+
Gahcho Kué samen) [1][10]. ⚠️ **Ekati zelf is sinds medio 2026 niet meer in normale productie** (zie §7) —
dit is een as die op het moment van schrijven al aan het uitdoven is, niet een stabiele huidige stroom.

## 1 · Ketenkaart
```
Ekati-mijnvliegveld `dia-ekati-strip` ──(b1 lucht · grootcirkel · ~312 km)──► Yellowknife Airport
   `dia-yzf-splitsing` (sorteer-/splitsingsfaciliteit, aannemelijk: één bron)
   ──(b2 lucht · grootcirkel · ~6.320 km)──► Brussels Airport Brucargo `dia-brucargo`
   ──(b3 truck · E19 · ~40 km)──► Antwerpen AWDC/Diamond Office `dia-awdc` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | lucht | Ekati-mijnvliegveld → Yellowknife Airport (YZF) | grootcirkel | ~310 [2] / grootcirkel 312,4 (gemeten) | maak_luchtbeen.py | nee (lucht = doorgetrokken) |
| b2 | B | lucht | Yellowknife Airport (YZF) → Brussels Airport (BRU) Brucargo | grootcirkel, geen tussenlanding gebrond | grootcirkel 6.319,2 (gemeten); design-schatting ~6.700 [ontwerp] | maak_luchtbeen.py | nee |
| b3 | C | truck | Brucargo (BRU) → Antwerpen AWDC/Diamond Office | E19 (Zaventem/Machelen → Vilvoorde → Mechelen → Antwerpen-Zuid) | ~40 [ontwerp]; hemelsbreed 35,2 | maak_stroombeen_weg.py | nee — korter dan 2 km-stukjes aan beide zijden mogen stippel worden als het net niet reikt (zie §7) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-ekati-strip` | mijnvliegveld (vertrekpunt lucht) | Ekati Airport (mijnstrip, geen IATA — privé) | 64.69891, -110.61439 | [3][9][11] | bron-gelegd (z15 gezien: duidelijke start-/landingsbaan met klein apron/gebouwtje aan het noordelijke uiteinde, 64.7075/-110.617; OSM-node "Ekati Airport" 64.69891/-110.61439) |
| `dia-yzf-splitsing` | overslag lucht→lucht (sorteer-/splitsingsfaciliteit) | vrachtapron/GA-terrein oostzijde Yellowknife Airport | 62.46850, -114.42500 | [4][5][6][9] | **aannemelijk** (bron noemt alleen "een metaal-beklede loods bij het vliegveld" zonder adres; z15 gezien: hangaars + kleine vrachttoestellen op het GA-platform aan de oostzijde, dicht bij de stad — exact pand niet aangewezen binnen budget) |
| `dia-brucargo` | vrachtterminal lucht (aankomst B, vertrek truck) | Brucargo, Brussels Airport | 50.90628, 4.45584 | [7][9] | bron-gelegd (z15 gezien: vrachttoestellen op het platform direct naast loodsen, tussen de passagiersterminal en de zuidelijke cargozone; OSM-landuse "Brucargo", Machelen) |
| `dia-awdc` | handels-/certificeringshub (eindpunt) | AWDC / Diamond Office, Hoveniersstraat, Antwerpen | 51.21520, 4.41870 | [8][9] | bron-gelegd (z15 gezien: dicht stedelijk bouwblok in de Diamantwijk vlak bij Antwerpen-Centraal, past bij "in het hart van Antwerpen, Hoveniersstraat"; geen apart terrein te onderscheiden — typisch voor een kantoor-/handelsdistrict) |

## 4 · Via-punten (alleen b3 — de enige landcorridor)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Vilvoorde, E19-knoop | 50.933, 4.434 | de corridor verlaat de luchthavenzone hier naar de doorgaande E19 noordwaarts (indicatief; bake-agent snapt op de echte rijbaan) |
| b3 | 2 | Mechelen, E19 westzijde | 51.020, 4.460 | E19 passeert Mechelen aan de westkant — enige doorgaande corridor tussen Brussel en Antwerpen, geen alternatieve routekeuze |
| b3 | 3 | Antwerpen-Zuid, R1/E19-knoop | 51.190, 4.400 | overgang van de E19 op de Antwerpse ring naar de binnenstad/Diamantwijk |

Dit is één ondubbelzinnige motorwegcorridor (E19); een `refs: ["E19"]`-voorkeur in het wegprofiel volstaat,
de drie punten hierboven zijn indicatief en niet zelf satelliet-gelegd (geen overslag, geen corridorkeuze
tussen twee gelijkwaardige wegen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Yellowknife-splitsing | (niet gebrond welke operator) | ruwe diamant Ekati/Diavik/Gahcho Kué → gesorteerd/gesplitst, klaar voor internationale verkoop | onbekend | [4][5][6] |
| Antwerpen AWDC/Diamond Office | AWDC (overheid + sector) | rough/polished diamant → geïmporteerd/geëxporteerd, G7-conflictcertificering | ~1.800 handelaren aangesloten [8] | [8][10] |

Beide knopen zijn **administratief/handel**, geen fysieke bewerking (slijpen gebeurt niet in Antwerpen maar
overwegend in Surat, India — buiten de scope van deze keten, zie stoppunt).

## 6 · Stoppunt
De brief stopt bij AWDC/Diamond Office in Antwerpen: dat is het opgegeven eindpunt van de keten
(certificering + handel), en geen bron noemt een specifieke vervolgbestemming (slijperij) voor Ekati-rough
specifiek — fase D vervalt.

## 7 · Open punten
- **⚠️ Belangrijkste bevinding, niet in het ontwerp/de haalbaarheidstoets:** Ekati is sinds mei 2026 onder
  CCAA-schuldeisersbescherming en is op 14-07-2026 door een rechtbank in **receivership** geplaatst; de
  NWT-overheid vroeg dit aan nadat een verkoopronde met 140 benaderde partijen nul biedingen opleverde. PwC
  is aangesteld als curator om de mijn binnen ~5 weken **af te bouwen en te reclameren** [12][13]. Op het
  moment van schrijven (28-09-2026, ruim 10 weken na de receivership-order) is onduidelijk of er nog
  reguliere winning/verscheping van ruwe diamant plaatsvindt — de keten in deze brief beschrijft de
  **historische/ontworpen** as, niet aantoonbaar de actuele operatie. Dit weegt zwaarder dan het door de
  haalbaarheidstoets bevestigde Diavik-risico.
- **Yellowknife-splitsingsgebouw niet adresseerbaar binnen budget:** meerdere bronnen noemen "een
  metaal-beklede loods bij het vliegveld" zonder naam/adres/operator; het anker staat op het GA-vrachtplatform
  aan de oostzijde van YZF (bron-gelegd voor het terrein, niet voor het specifieke pand).
- **Geen bron voor een tussenlanding** op b2 (bv. via Calgary/Toronto/een Europese hub) — één directe vlucht
  YZF→BRU aangenomen, zoals de bakhandleiding voorschrijft bij het ontbreken van een hub-bron.
- **Ekati-specifiek jaarvolume niet apart gebrond** — alleen het Canada-totaal (Diavik+Ekati+Gahcho Kué)
  is gevonden; met Diavik gesloten (maart 2026 [ontwerp/webcheck]) en Ekati in afbouw ligt het actuele
  Canadese volume waarschijnlijk (fors) onder de ~16 Mct/j uit design/diamant.md §3a.
- **km b2 is een schatting** (ontwerp noemt ~6.700 km, de gemeten grootcirkel tussen de gekozen
  luchthavenankers is 6.319,2 km) — de bak-agent rekent het exacte getal uit met `maak_luchtbeen.py`.
- **b3-via-punten zijn indicatief**, niet satelliet-gelegd; E19 is de enige zinnige corridor dus het risico
  op een verkeerd wegprofiel is laag.

## 8 · Bronnen
[1] design/diamant.md §3a — Canada (Diavik/Ekati/Gahcho Kué) ~16 Mct/j, 14% wereldvolume (intern ontwerpdocument).
[2] Wikipedia, "Ekati Diamond Mine" — "located 310 km (190 mi) north-east of Yellowknife". https://en.wikipedia.org/wiki/Ekati_Diamond_Mine
[3] OpenStreetMap (ODbL) via Photon — node "Ekati Airport", aeroway=aerodrome, 64.69891/-110.61439. https://www.openstreetmap.org
[4] GIA, Gems & Gemology, Summer 2016, "Mining Diamonds in the Canadian Arctic: The Diavik Mine" — rough diamonds gaan naar een sorteerfaciliteit bij Yellowknife. https://www.gia.edu/gems-gemology/summer-2016-diamonds-canadian-arctic-diavik-mine
[5] CBC News, "Warrant reveals details of alleged diamond theft" — sorteer-/splitsingsgebouwen bij Yellowknife Airport, Diavik/Gahcho Kué in het ene gebouw, Ekati in een ander. https://www.cbc.ca/news/canada/north/diamond-theft-search-warrant-1.4620826
[6] The Walrus, "How to Close a Diamond Mine in the Northwest Territories" — sorteerproces diamant NWT (achtergrond, geen adresdetail). https://thewalrus.ca/how-to-close-a-diamond-mine-in-the-northwest-territories/
[7] OpenStreetMap (ODbL) via Photon — landuse "Brucargo", Machelen, 50.9063/4.4558. https://www.openstreetmap.org
[8] Wikipedia, "Antwerp World Diamond Centre" — AWDC/Diamond Office, Hoveniersstraat, Antwerpen; ~1.800 diamanthandelaren. https://en.wikipedia.org/wiki/Antwerp_World_Diamond_Centre
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14–z15, live) — `v2/build-cache/satcheck/sat-diamant-ekati-antwerpen-{ekati-strip2,yzf-apronoost,brucargo2,awdc}.png`.
[10] design/diamant.md §2/§3c — Antwerpen als G7-certificeringsknooppunt (sinds maart 2024, sanctie op Russische/Alrosa-diamant); ruw vliegt naar Antwerpen voor certificering + handel (intern ontwerpdocument).
[11] Wikipedia, "Ekati Diamond Mine" §Transportation — "Mine workers fly-in fly-out through Ekati Airport." https://en.wikipedia.org/wiki/Ekati_Diamond_Mine
[12] Wikipedia, "Ekati Diamond Mine" §History — CCAA-bescherming mei 2026, receivership 14-07-2026, PwC als curator, $325M reclamatiezekerheid. https://en.wikipedia.org/wiki/Ekati_Diamond_Mine (bronverwijzing naar Cabin Radio, zie [13])
[13] Cabin Radio, 14-07-2026, "Ekati enters receivership and will be shut down, ending an era" — rechtbank plaatst Ekati in receivership op verzoek van de NWT-overheid na een mislukte verkoopronde (140 benaderde partijen, nul biedingen); afbouw mijnbouw binnen ~5 weken, dan reclamatie. https://cabinradio.ca/300594/news/economy/mining/ekati-enters-receivership-and-will-be-shut-down-ending-an-era/

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**⚠️ Vóór het bakken gemeld, niet stilzwijgend genegeerd:** Ekati is sinds 14-07-2026 in receivership en wordt
binnen enkele weken daarna afgebouwd/gereclameerd (§7, bron [12][13]). Op het moment van bakken (28-09-2026,
ruim 10 weken na de receivership-order) is onduidelijk of er nog reguliere winning/verscheping van ruwe diamant
plaatsvindt — deze keten is **historisch/ontworpen**, niet aantoonbaar de actuele operatie. Gebakken zoals
opgedragen, met dit voorbehoud expliciet in het rapport aan Lars.

**Stroom `diamant-ekati-antwerpen`** → `v2/data/stroomroute-diamant-ekati-antwerpen.json` — 3 benen (lucht ·
lucht · truck, fase A → C → stoppunt), **6.672,9 km**, 1.055 punten, 4 markers, 21,0 KB. Recept: `bak_stromen.sh`
(functie `bak_diamant_ekati_antwerpen`); nieuw wegprofiel `diamant-ekati-antwerpen-brucargo-awdc` in
`maak_stroombeen_weg.py`. **Eerste bake van deze golf (en van het project) met een luchtbeen** — twee stuks,
achter elkaar, conform `bakhandleiding-licht.md` §2 "Lucht".

**b1 (lucht, grootcirkel, Ekati-strip → YZF):** `maak_luchtbeen.py --van "Ekati-strip|64.69891,-110.61439" --naar
"Yellowknife YZF|62.46850,-114.42500"` — **311,4 km** gemeten grootcirkel (brief noemde 312,4; Wikipedia publiceert
~310 km — binnen norm, geen aparte km-toets voor een luchtbeen). 14 punten. Doorgetrokken, geen stippel: een vlucht
tussen twee gelegde vrachtterminals is geen gat. Ankers ongewijzigd bron-gelegd overgenomen uit de opdracht
(Ekati-mijnstrip z15 duidelijke start-/landingsbaan met apron; Yellowknife GA-vrachtplatform aannemelijk — geen
adres voor het specifieke sorteergebouw gevonden).

**b2 (lucht, grootcirkel, YZF → BRU):** `maak_luchtbeen.py --van "Yellowknife YZF|62.46850,-114.42500" --naar
"Brussels BRU Brucargo|50.90628,4.45584"` — **6.316,8 km** gemeten grootcirkel (brief noemde 6.319,2; de eerdere
ontwerp-schatting van ~6.700 km is **niet gebruikt**, zoals de opdracht voorschreef — het gemeten getal vervangt
de schatting). 254 punten. Doorgetrokken. Geen tussenlanding gebrond (geen bron noemt een hub tussen Yellowknife en
Brussel) → één directe vlucht, conform §7 van de brief en de bakhandleiding.

**b3 (truck, nieuw profiel `diamant-ekati-antwerpen-brucargo-awdc`, extract `belgie`, vensterKm 40):**
`maak_stroombeen_weg.py --profiel diamant-ekati-antwerpen-brucargo-awdc --bron geofabrik` — **44,5 km** geroute
(getekende lijn 44,7 km incl. anker-verbindingsstukjes) over de drie indicatieve via-punten uit de opdracht
(Vilvoorde → Mechelen-west → Antwerpen-Zuid), de router volgt de E19 exact zoals verwacht — geen alternatieve
corridor. Anker-verbindingsstukjes Brucargo → weg 0,05 km en weg → AWDC 0,09 km (beide ruim binnen 0,5 km, dus
**geen stippel nodig** op de uiteinden — de airside-/voetgangerszone-zorgen uit de opdracht bleken in de praktijk
niet nodig). 43 kleine keerlussen gesnoeid (48,3 → 44,5 km, dubbel gereden stukjes op stadswegen rond Vilvoorde/
Mechelen/Antwerpen-Zuid/AWDC). First mile 0,24 km + last mile 0,63 km over kleine wegklassen (service/
unclassified/tertiary/residential), beide binnen de 12 km-marge.

**⚠️ Lengtetoets net BUITEN ±10%, BINNEN de ±15%-norm:** 44,5 km (getekend 44,7 km) tegen de toetswaarde 40 km
(ontwerp, geen gepubliceerde km) = **+11,3% resp. +11,75%**. Bevinding, geen fout: de drie via-punten zijn
indicatief (brief §4/§7, niet satelliet-gelegd) en de E19 is de enige doorgaande motorwegcorridor Brussel–
Antwerpen — geen via-punt bijgeschoven om het getal te halen.

**Toetsen:** `toets_knikken.py` — lucht-benen 0 knikken/0 omkeringen (per constructie recht); truckbeen 17 knikken
≥60° (spikes bij kruispunten van de E19-op-/afritten en stadswegen rond Vilvoorde/Mechelen/Antwerpen-Zuid, straal
2–56 m), **0 omkeringen ≥150°, 0 terugloop** — geen actie nodig. `toets_rechte_benen.py --min-km 5` — geen melding
voor deze stroom (lucht-benen worden per constructie overgeslagen; het truckbeen is geen rechte lijn). `json.load`
slaagt: versie 2, `punt_formaat` lonlat, modaliteiten `lucht`/`lucht`/`truck` ∈ toegestane set, elk been ≥ 2 punten
(14/254/787), bestandsgrootte 21,0 KB (ruim onder ~300 KB). Naden tussen de drie benen: **0,000 km** op alle twee
overgangen (b1→b2 op de YZF-splitsing, b2→b3 op Brucargo). Markers: alle vier op 0,0 km van hun been (elk anker is
tegelijk het routeerpunt/been-uiteinde).

**Toelichting stippels/haven-aanlopen/vluchten:** twee vluchten, beide doorgetrokken (geen stippel, zie boven).
Geen zeebeen in deze keten → geen MARNET, geen haven-aanloop. Geen stippel op b3: beide anker-verbindingen zijn
triviaal klein (0,05/0,09 km), dus geen airside- of voetgangerszone-probleem zoals de opdracht als mogelijkheid
noemde. Fase D/E vervallen (brief §6, stoppunt bij AWDC/Diamond Office).

**Gereedschapslessen:** `maak_luchtbeen.py` werkte zonder aanpassing voor beide vluchten, inclusief de lange
interncontinentale (6.316,8 km, 254 punten binnen de default `--stap-km 25`). Het luchtbeen-been-geojson-patroon
uit `bakhandleiding-licht.md` §2 ("lucht|vlucht <van> → <naar> (vrachtvlucht, grootcirkel)|pad") sluit naadloos aan
op `hecht_marnet.py route --been-geojson`, net als een truck-been-geojson — geen tool-aanpassing nodig voor de
eerste luchtbeen-bake van het project. Kleine correctie op de opdracht: de beennaam in `--been-geojson` draagt
hier geen IATA-code ("vlucht Ekati-strip → YZF"/"vlucht YZF → BRU") omdat de Ekati-mijnstrip geen IATA/ICAO-code
heeft (brief §7, laatste open punt) — conform de brief zelf, die dit al voorzag.
