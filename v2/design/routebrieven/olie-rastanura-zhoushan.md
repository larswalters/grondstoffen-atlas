# Routebrief (licht) · olie — Ras Tanura (Saoedi-Arabië) → Zhoushan (China)

**stroom-id:** `olie-rastanura-zhoushan` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31) · **status:** gebakken
**Keten in één zin:** Arabische ruwe olie uit het Ghawar/Abqaiq-veldencomplex, via Aramco's interne gatheringleidingen
naar de Ras Tanura-exportterminal, per **VLCC** over de Perzische Golf → Straat van Hormuz → Arabische Zee →
Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee naar de kade van Zhejiang Petroleum & Chemical (ZPC,
Rongsheng-affiliate) op Dayushan-eiland, Zhoushan Green Petrochemical Base — de dikste enkele stroom van alle
grondstoffen in dit atlas.
**Welke as van het verhaal:** *de Golf → Azië-bundel (Hormuz + Malakka).* Termcontract van **480.000 vaten/dag**
Arabische ruwe olie aan het 800.000 vpd-ZPC-complex, gekoppeld aan Aramco's **$3,4 mrd/10%-aandeleninstap** in
Rongsheng Petrochemical (afgerond 21-07-2023) [1][2][3]; peiljaar 2024, nog actueel in 2026, geen tegenbericht
gevonden.

## 1 · Ketenkaart
```
Ghawar/Abqaiq-olievelden `ol-abqaiq` ──(b1 leiding · Aramco-gatheringnet, stippel · ~90 km)──►
   Ras Tanura-exportterminal `ol-rastanura-term`
   ──(b2 zee · Perzische Golf → Straat Hormuz → Arabische Zee → Straat Malakka → Zuid-Chinese Zee →
       Oost-Chinese Zee · ~11.800 km, MARNET)──►
   ZPC-kade `ol-zhoushan-zpc` (Zhejiang Petroleum & Chemical, Dayushan-eiland, Zhoushan) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Abqaiq-olievelden → Ras Tanura-exportterminal | Aramco interne gatheringpijpleidingen (geen gepubliceerde enkele lijn) | ~90 [webcheck, hemelsbreed; input-schatting ~80] | stippel — schematisch, Aramco-gatheringnet niet gekarteerd (gcc-staten-extract heeft naar verwachting geen `man_made=pipeline` op dit tracé) | ja — eigen interne infrastructuur, net reikt niet |
| b2 | B | zee | Ras Tanura-exportterminal → ZPC-kade Zhoushan | Perzische Golf → Hormuz → Arabische Zee → Malakka → Zuid-Chinese Zee → Oost-Chinese Zee | ~11.800 [ontwerp/webcheck] | MARNET (kade → kade) | nee — beide kades ruim binnen zeeknoop-bereik (Ras Tanura 10,8 km, Zhoushan 3,7 km; haalbaarheidstoets) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-abqaiq` | olieveld/stabilisatiecomplex (kop van de leiding) | Abqaiq Plants (Saudi Aramco), Ghawar/Abqaiq-veldencomplex | 25.9400, 49.6600 | [4][5][14] | aannemelijk (z14 gezien: industrieel complex met tanks/procesinstallaties direct naast de woonwijk Abqaiq — 's werelds grootste olieverwerkings-/stabilisatiefaciliteit; exacte stabilisatietoren niet op deze korrel te onderscheiden) |
| `ol-rastanura-term` | laadplek / exportterminal | Ras Tanura-exportterminal (Saudi Aramco) — tankenpark + steiger, incl. Sea Island-fingerpier | 26.6540, 50.1648 | [6][7][15] | bron-gelegd (z16 gezien: tankenpark aan de kust met een T-vormige steiger de Golf in en een tanker afgemeerd aan de kop; de langere Sea Island-fingerpier met een tweede tanker zichtbaar verderop in zee) |
| `ol-zhoushan-zpc` | losplek / raffinage- en kraakcomplex (fase C-knoop) | ZPC (Zhejiang Petroleum & Chemical, Rongsheng-affiliate), Zhoushan Green Petrochemical Base, Dayushan-eiland | 30.3180, 121.9600 | [8][9][16] | bron-gelegd (z14 gezien: volledig gereclameerd industrie-eiland met tankenpark en procesinstallaties, verbonden door een lange trestle/havendam de zee in; de exacte crude-loskade binnen het complex niet te onderscheiden — meerdere pieren zichtbaar) |

## 4 · Via-punten
Geen — b1 is een gestippelde eigen leiding zonder alternatieve route, b2 wordt door de MARNET-router zelf gelegd
(kade → kade over Hormuz/Malakka, geen corridorkeuze te benoemen op dit schaalniveau).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| ZPC-complex (Zhoushan) | Rongsheng Petrochemical (51%) + Juhua/Tongkun/Zhoushan Marine; Aramco als crude-leverancier (10% Rongsheng-aandeel) | ruwe olie → nafta/aromaten (benzeen, PX)/olefinen/producten | 800.000 vpd raffinage-in, 4,2 Mt/j ethyleen; contract-aandeel Aramco 480.000 vpd (+84,6% t.o.v. eerdere instroom) | [1][2][3][9] |

## 6 · Stoppunt
De brief stopt bij de poort van het ZPC-complex: dat is de contractueel benoemde bestemming (het termcontract loopt
tot ZPC, niet tot één specifieke downstream-fabriek), en geen bron noemt welk deel van de nafta/aromaten-uitstroom
naar welke met-naam-genoemde vervolgfabriek gaat — fase D/E vervallen.

## 7 · Open punten
- **Geen bron noemt de exacte kade binnen het ZPC-complex** — op z14 zijn meerdere pieren/steigers zichtbaar; het
  anker blijft terminal-niveau, zoals de haalbaarheidstoets al voorschreef.
- **Aramco's interne gatheringnet (Ghawar/Abqaiq → Ras Tanura) is niet gekarteerd** — geen gepubliceerde
  enkele pijplijn, geen OSM-way verwacht; b1 blijft een schematische stippel van ~90 km hemelsbreed.
- **Recente onderbreking van de B-corridor, drie maanden vóór deze brief:** Ras Tanura werd op 02-03 en 04-03-2026
  zelf geraakt door Iraanse raketten/drones (vergelding op VS-Israël-strikes tegen Iran vanaf 28-02-2026), tijdelijk
  stilgelegd en heropend op 13-03-2026; Aramco leidde de export daarna ~4 maanden om via Yanbu (Rode Zee) terwijl de
  Straat van Hormuz effectief verstoord was. Ladingen bij Ras Tanura hervat 26-06-2026, na een tussentijds
  VS-Iran-akkoord over Hormuz [10][11][12][13]. De B-corridor is dus een recent bewezen kwetsbare schakel, geen
  hypothetisch risico.
- **Contractstructuur kan nog verschuiven** — de haalbaarheidstoets noemt mogelijke aanvullende SASREF/Ningbo
  Zhongjin-deals binnen dezelfde Aramco-Rongsheng-aandelenruil; niet in deze brief verwerkt.
- **Jaarvolume-eenheid:** contract in vaten/dag; zie §0-notitie hieronder voor de omrekening naar Mt/j.

*Volume-notitie:* 480.000 vpd Arabische ruwe olie × 365 dagen ≈ 175,2 mln vaten/jaar; bij ~7,3 vaten/ton voor
Arabische ruwe olie ≈ **~24 Mt/j** (oorspronkelijke eenheid: vaten/dag, kb/d; peiljaar 2024, contract sinds de
aandelenruil van 2023).

## 8 · Bronnen
[1] Aramco, persbericht 27-03-2023 / afgerond 21-07-2023 — "Aramco to expand presence in China by acquiring 10% stake in Rongsheng Petrochemical", 480.000 vpd aan ZPC, ZPC-capaciteit 800.000 vpd. https://www.aramco.com/en/news-media/news/2023/aramco-to-expand-presence-in-china-by-acquiring-10-percent-stake-in-rongsheng-petrochemical
[2] The National, 21-07-2023 — "Aramco completes $3.4bn purchase of 10% stake in Rongsheng Petrochemical". https://www.thenationalnews.com/business/energy/2023/07/21/aramco-completes-34bn-purchase-of-10-stake-in-rongsheng-petrochemical/
[3] Gulf News — "Saudi Aramco locks up stake in China petrochemicals firm". https://gulfnews.com/business/energy/saudi-aramco-locks-up-stake-in-china-petrochemicals-firm-1.97099055
[4] Wikipedia, "Abqaiq" — 25°56′06″N 49°39′58″E, 60 km ZW van Dhahran, Aramco's grootste olieverwerkings-/stabilisatiefaciliteit. https://en.wikipedia.org/wiki/Abqaiq
[5] Offshore Technology, "Saudi Aramco Abqaiq Plants Facility" — 7 mln vpd stabilisatiecapaciteit, oil processing + NGL + utilities unit. https://www.offshore-technology.com/projects/abqaiq-aramco/
[6] Wikipedia, "Ras Tanura" — 26°38′N 50°09′E, "world's largest crude oil export terminal", artificial island (Sea Island) + North Pier + South Pier + Ju'aymah-terminal. https://en.wikipedia.org/wiki/Ras_Tanura
[7] Aramco, "Ports and Terminals". https://www.aramco.com/en/what-we-do/operations/ports-and-terminals
[8] NS Energy Business, "Zhoushan Green Petrochemical Base" — ZPC = joint venture Rongsheng/Juhua/Tongkun/Zhoushan Marine, locatie Yushan-eiland, Daishan county. https://www.nsenergybusiness.com/projects/zhoushan-green-petrochemical-base/
[9] PGJ Online, jan. 2024 — "Saudi Aramco, China's Rongsheng in advanced talks for mutual stake purchase in refining units". https://pgjonline.com/news/2024/january/saudi-aramco-chinas-rongsheng-in-advanced-talks-for-mutual-stake-purchase-in-refining-units
[10] Wikipedia, "2026 Aramco refinery attack" — Iraanse strikes op Ras Tanura 02-03 en 04-03-2026 (na VS-Israël-strikes op Iran vanaf 28-02-2026), stillegging tot 13-03-2026, omleiding via Yanbu. https://en.wikipedia.org/wiki/2026_Aramco_refinery_attack
[11] CNBC, 27-06-2026 — "Saudi Aramco resumes oil loading at Ras Tanura in boost to supply", hervatting na bijna 4 maanden, 2 VLCC's van Bahri geladen. https://www.cnbc.com/2026/06/27/saudi-aramco-resumes-oil-loading-at-ras-tanura-in-boost-to-supply.html
[12] US News, 25-06-2026 — "Saudi Aramco Resumes Oil Loading at Ras Tanura After 4-Month Halt, Data Shows". https://www.usnews.com/news/world/articles/2026-06-25/saudi-aramco-resumes-oil-loading-at-ras-tanura-after-4-month-halt-data-shows
[13] GlobalSecurity.org / RFE/RL, 27-06-2026 — "Saudi Aramco Resumes Crude Loading At Ras Tanura Terminal", context VS-Iran-tussenakkoord over Hormuz. https://www.globalsecurity.org/wmd/library/news/saudi/2026/saudi-260627-rferl01.htm
[14] OpenStreetMap/Nominatim (ODbL) — plaats بقيق/Abqaiq 25,93556/49,66833. https://www.openstreetmap.org
[15] OpenStreetMap/Nominatim (ODbL) — geen directe treffer voor "Ras Tanura Terminal"/"Sea Island"; ligging bevestigd via Wikipedia-coördinaat + satellietbeeld. https://www.openstreetmap.org
[16] OpenStreetMap/Nominatim (ODbL) — eiland 大鱼山岛 (Dayushan), 30,31791/121,95940, bbox 30,2906–30,3450/121,9168–121,9954. https://www.openstreetmap.org
[17] Esri World Imagery via `v2/tools/sat_check.py` (z14–z17) — `sat-olie-rastanura-zhoushan-abqaiq.png`, `sat-olie-rastanura-zhoushan-seaisland.png`, `sat-olie-rastanura-zhoushan-zhoushan-eiland.png`, `sat-olie-rastanura-zhoushan-pier-ne.png`, `sat-olie-rastanura-zhoushan-pier-e.png`, `sat-olie-rastanura-zhoushan-jettyhead.png`, `sat-olie-rastanura-zhoushan-jettytip.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze)

**Stroom `olie-rastanura-zhoushan`** → `v2/data/stroomroute-olie-rastanura-zhoushan.json` — 2 benen, **10.949,1 km**, 1.123 punten, 3 markers (1 stippel).
Recept: `bak_stromen.sh` (functie `bak_olie_rastanura_zhoushan`).

**b1 (leiding, stippel):** `--stippel "leiding|Aramco-gatheringnet Ghawar/Abqaiq → Ras Tanura (schematisch — interne infrastructuur, geen gepubliceerde enkele OSM man_made=pipeline-lijn)|25.9400,49.6600|26.6540,50.1648"` — rechte lijn tussen de twee ankers. **94,0 km** tegen de gepubliceerde ~90 km (webcheck, hemelsbreed) = **+4,4%**, ruim binnen ±15%.
⚠️ **De pyosmium-scan op `man_made=pipeline` (bbox 25,8–26,8/49,5–50,3, extract `gcc-staten`) gaf géén schone negatieve uitslag** — er liggen wél losse, grotendeels ongenaamde `substance=oil`-fragmenten in het gebied (o.a. ways 219942630/219942632/226435144, elk met een uiteinde op ~3 km van het Abqaiq-anker), maar geen enkele stitcht door tot binnen 5 km van het Ras Tanura-anker (dichtstbijzijnde fragment-uiteinde bleef ~37 km te kort) en geen enkele draagt een naam. Dat bevestigt de brief eerder dan dat het hem weerlegt: een fragmentarisch, ongekarteerd net, geen gepubliceerde enkele lijn — de rechte stippel blijft de eindvorm.

**b2 (zee, MARNET-route, kade → kade):** `--been "zee|zeeschip Ras Tanura-exportterminal → ZPC-kade Zhoushan (Perzische Golf → Straat Hormuz → Arabische Zee → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee)|26.6540,50.1648|30.3180,121.9600"` — snap Ras Tanura **11,14 km**, snap Zhoushan **7,79 km** (beide ruim binnen de 25 km-norm, geen haven-aanloop gebouwd, conform de bak-aanwijzing). **10.855,1 km**, 1.121 punten, tegen de gepubliceerde ~11.800 km (ontwerp/webcheck) = **−8,0%**, ruim binnen ±15%. Tussenpunten van de getekende lijn bevestigen de verwachte corridor: 56,9°O/26,0°N (Straat Hormuz) → 67–78°O langs de Arabische Zee/Indische Oceaan → 92–104°O (Straat Malakka) → 108–115°O (Zuid-Chinese Zee) → 119–122°O (Oost-Chinese Zee naar Zhoushan) — geen Kaap-omweg (verkeerde-tak-signaal expliciet gecontroleerd en niet aangetroffen).

**Markers:** `ol-abqaiq` (0,00 km van de lijn — kop van b1) · `ol-rastanura-term` (0,00 km van b1-staart, maar **11,14 km** van de b2-lijn — anker ≠ routeerpunt: de kade ligt landinwaarts van de dichtstbijzijnde MARNET-zeeknoop; iets hoger dan de haalbaarheidstoets' 10,8 km maar dezelfde orde en ruim binnen de 25 km-norm) · `ol-zhoushan-zpc` (**7,79 km** van de b2-lijn — zelfde categorie; haalbaarheidstoets gaf 3,7 km, hier iets hoger doordat de dichtstbijzijnde zeeknoop niet identiek is aan het punt van de eerdere toets, nog steeds ruim binnen de norm).

**Naad tussen b1 en b2: 11,14 km** — dit is uitsluitend de zee-been-snap op de dichtstbijzijnde MARNET-zeeknoop (geen los procesgat); boven de 5 km-vuistregel uit de bakhandleiding maar hier de directe consequentie van de bewust niet-gebouwde haven-aanloop (beide kades < 25 km), dus een **bevinding, niet dichtgetrokken**.

> **Bijgewerkt 2026-09-28 (LAR-586):** de naad is alsnog dichtgezet met een haven-aanloop Ras Tanura over water (`maak_havenaanloop.py`: 11,8 km, 6 punten, 0 km over land) als stippel tussen de gatheringstippel en het zeebeen. Keten nu 10.960,9 km in drie benen.

**Toets:** `toets_knikken.py` — 3 knikken ≥60° (101,6° bij 26,805/50,243 · 85,2° bij 29,624/122,653 · 76,8° bij 29,927/122,162, alle drie krappe bochten vlak bij de aankomst/vertrek-kust), **0 omkeringen ≥150°**, 0 terugloop — geen bevinding. `toets_rechte_benen.py --min-km 5` — b1 (94,0 km, omwegfactor 1,000) staat op de lijst als 🟠 GROOT (stippel): correct, het is een bewuste rechte stippellijn, geen bevinding op zichzelf. json geldig: versie 2, punt_formaat lonlat, modaliteiten `leiding`/`zee` (in de toegestane set), elk been ≥2 punten (2/1.121), bestandsgrootte **20,5 KB** (ruim < 300 KB).

**Gereedschapslessen:**
- Een pyosmium-scan op `man_made=pipeline` met alleen `w.tags` mist de geometrie; `w.nodes` levert pas geldige `lat`/`lon` op via `osmium.NodeLocationsForWays` + `osmium.index.create_map` (twee-pass read met een locatie-cache), anders komen alle afstandsberekeningen uit met absurde honderden-kilometers-waarden die op het eerste gezicht als "ver weg" lezen maar in werkelijkheid een lege/ongeldige locatie zijn.
- Een niet-schone (niet-nul) OSM-uitslag bij een "geen gepubliceerde lijn"-verwachting is geen automatische weerlegging: fragmentatie + naamloosheid + een gat van tientallen km tot het anker is zelf het bewijs van "geen gepubliceerde enkele lijn", niet het tegendeel. Onderscheid dat van een schone hit (één benoemde, doorlopende way die beide ankers binnen 5 km raakt) vóór je de stippel loslaat.
- Bij een zeebeen zonder haven-aanloop (beide kades < 25 km van een zeeknoop) is de snapafstand zelf de "naad" met het voorgaande been — de 5 km-vuistregel van de bakhandleiding is hier niet haalbaar zonder een aanloop te bouwen die de bak-aanwijzing juist expliciet afraadt; rapporteren als bevinding, niet als fout.
