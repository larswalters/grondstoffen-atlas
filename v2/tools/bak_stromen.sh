#!/usr/bin/env bash
# ============================================================================
# bak_stromen.sh — HET RECEPT VAN ELKE GEBAKKEN STROOM.
#
# WAAROM DIT BESTAAT. `hecht_marnet.py route` is been-gestuurd: welke benen,
# welke via-punten, welke markers en welke vlaggen een stroom kreeg, leefde tot
# 2026-08-04 uitsluitend in een shell-historie. Daarmee is een gebakken
# stroomroute-*.json een gegenereerd bestand ZONDER vindbaar recept — precies de
# driftklasse die dit project al drie keer heeft geraakt:
#   * cu-guixi-spoor stond 741 m fout in de generator terwijl de uitvoer al goed
#     was; regenereren had dat stil teruggedraaid;
#   * maak_aansluitingen.py las marnet uit een pad dat niet meer bestond;
#   * het wegbeen Balama→Nacala op schijf (28-07) bleek NIET meer te zijn wat
#     zijn eigen generator vandaag maakt — snoei_keerlussen kwam er op 30-07
#     bij en raakt ook dat been (502,7 → 497,9 km).
#
# WERKREGEL. Wie een stroom herbakt, doet dat via dit script. Verandert er iets
# aan een recept, dan verandert dit bestand mee IN DEZELFDE COMMIT als het
# gebakken json. Lopen ze uit elkaar, dan is de stroom niet meer reproduceerbaar.
#
# ⚠️ --marnet wijst naar build-cache/marnet-preais, NOOIT naar v2/data/: de bol
#    mag het waternet niet laden (schone-bol-bake 24-07).
# ⚠️ Zodra er één --marker staat vervangt die lijst de automatische afleiding
#    volledig. Alle markers van de stroom moeten er dus in.
# ⚠️ De volgorde van --been / --stippel / --been-geojson / --stippel-geojson IS
#    de reisvolgorde.
# ⚠️ --stippel-geojson = betere geometrie, ONGEWIJZIGDE kennisclaim. Een
#    haven-aanloop die als kortste pad over water is berekend kruist geen land
#    meer, maar is nog steeds geen waargenomen vaargeul — die houdt zijn stippel.
#    Doorgetrokken blijft voorbehouden aan "we weten waar de lijn ligt".
#
# ⚠️ SPOOR: het 1-op-1-OSM-spoornet (v2/data/landnet-raw.bin, 3.260.717 spoor-
#    edges) is in toets_spoorroute.mjs ALLEEN actief met `BAKE_SUFFIX=-raw`;
#    zonder die var routeert het tool over het tekennet (470.543 edges) en krijg
#    je andere lijnen. Controleer de eerste consoleregel. Zie
#    v2/design/bakhandleiding-licht.md §2 (spoor).
#
# Draaien vanuit de repo-root (zonder of met onbekend argument: lijst van de
# bekende stromen; elke functie bak_<naam met _> is via <naam met -> bereikbaar):
#   bash v2/tools/bak_stromen.sh grafiet
# ============================================================================
set -euo pipefail

GRAAF="v2/build-cache/ais/graaf/mississippi"
MARNET="v2/build-cache/marnet-preais"
NE="v2/build-cache"
BEEN="v2/build-cache/ais/graaf"

# ── grafiet · Balama → Nacala → New Orleans → Vidalia → De Soto → Casa Grande
# Routebrief: v2/design/routebrieven/grafiet-balama-vidalia.md (fasen A–E)
# ⚠️ Fase D en E worden getekend terwijl het VOLUME VANDAAG NUL is (besluit Lars
#    2026-08-04): de weg is gemeten, de lading nog niet. Doorgetrokken, niet
#    gestippeld — stippel betekent in dit project uitsluitend "hier reikt het
#    net niet" (werkwijze §7).
# ⚠️ De keten hecht bij De Soto aan op het ROUTEERPUNT (rotonde Astra Parkway),
#    niet op het fabrieksterrein: dat terrein is over de weg niet bereikbaar en
#    de docks zijn niet gelegd (de Esri-opname is nog de bouwfase).
bak_grafiet() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Balama → Nacala (N380/N1)|$BEEN/stroombeen-balama-nacala.geojson" \
    --stippel-geojson "zee|haven-aanloop Nacala (schematisch, over water — MARNET reikt hier niet)|$BEEN/aanloop-nacala.geojson" \
    --been         "zee|zeeschip Nacala → Southwest Pass|-15.0,41.7|28.91,-89.43014" \
    --been         "zee|zeeschip Southwest Pass → New Orleans|28.91,-89.43014|29.91230,-90.11200" \
    --been         "binnenvaart|containerbarge New Orleans → Port Allen (IRMT)|29.91230,-90.11200|30.43293,-91.24385" \
    --been         "binnenvaart|containerbarge Port Allen → Port of Vidalia|30.43293,-91.24385|31.53645,-91.48255" \
    --been-geojson "truck|last mile haven → Syrah-fabriek|$BEEN/stroombeen-vidalia-lastmile.geojson" \
    --been-geojson "truck|uitgaand: fabriekspoort → US-84 (Vidalia)|$BEEN/stroombeen-vidalia-us84.geojson" \
    --been-geojson "truck|AAM → Panasonic De Soto (KS)|$BEEN/stroombeen-vidalia-desoto.geojson" \
    --been-geojson "truck|2170-cellen → Lucid AMP-1 (AZ)|$BEEN/stroombeen-desoto-casagrande.geojson" \
    --marker "Balama — mijn/plant|-13.31000,38.66000" \
    --marker "Nacala — containerterminal|-14.53830,40.66730" \
    --marker "Port of New Orleans — Napoleon Ave|29.91230,-90.11200" \
    --marker "Port Allen (IRMT) — bargekade|30.43313,-91.24383" \
    --marker "Port Allen Lock (sluis)|30.43085,-91.20823" \
    --marker "Port of Vidalia — apron (mijl 359)|31.53645,-91.48255" \
    --marker "Syrah AAM-fabriek Vidalia|31.54660,-91.48870" \
    --marker "Panasonic Energy Kansas — De Soto (volume nul)|38.93815,-95.00240" \
    --marker "Lucid AMP-1 — Casa Grande (volume nul)|32.85724,-111.78008" \
    --routebrief v2/design/routebrieven/grafiet-balama-vidalia.md \
    --uit    v2/data/stroomroute-pilot.json \
    --stroom grafiet-balama-vs \
    --titel  "Grafiet · Balama → Vidalia → De Soto → Casa Grande"
}

# ── koper · Escondida → Puerto Coloso → Beilun → 贵溪 → walsdraadfabriek
# Routebrief: v2/design/routebrieven/koper-escondida-guixi.md (fasen A–D)
# Werkorder:  v2/design/werkorder-koper-guixi-de.md
#
# ⚠️ GERECONSTRUEERD 2026-08-05, NIET TERUGGEVONDEN. Dit commando REPRODUCEERT
#    de uitvoer van 29 juli; het is niet aantoonbaar hét commando van 29 juli.
#    Vier vrijheidsgraden geven een byte-identiek bestand (--graaf mississippi
#    of rijn · --spoor-geojson of --been-geojson · --naar op het anker of op
#    het routeerpunt · één stap of twee). Het bestand op schijf onderscheidt ze
#    niet. Het bewijs is "dit commando produceert dat artefact", nooit "dit was
#    het commando".
# ⚠️ ÉÉNSTAPS. Op 29 juli is eerst gebakken (01:43) en daarna het spoorbeen
#    vervangen met vervang_spoorbeen.py (16:49) — zichtbaar doordat het veld
#    `gemaakt` ouder is dan de bestandsdatum. Die tweetraps is niet nodig: het
#    spoorbeen komt hier rechtstreeks uit de OSM-1-op-1-route als --been-geojson.
#    ⚠️ vervang_spoorbeen.py NIET meer op deze stroom gebruiken: hij matcht op
#    MODALITEIT, en sinds 2026-08-05 heeft deze stroom drie `leiding`-benen.
# ⚠️ --been-geojson voor het spoorbeen en NIET --spoor-geojson: die vlag zet
#    zijn been altijd achteraan, en dan komt fase D vóór de trein te staan.
# ⚠️ FASE E ONTBREEKT, EN DAT IS EEN RESULTAAT: er is geen gedocumenteerde
#    afnemer van dit walsdraad (werkorder §F4/F5). De keten stopt beargumenteerd
#    bij de walsdraadfabriek.
# ⚠️ DE KOP VAN FASE D IS EEN SUBSTITUUT: het registerpunt van de smelter, niet
#    de kathode-expeditie (niet gevonden — Esri heeft bij Guixi geen z19).
#    Daarom blijft er bewust een PROCESGAT van 0,54 km tussen het spoorbeen en
#    fase D. Dat gat ís het ontbrekende anker en wordt niet dichtgetrokken.
# ⚠️ HET LEIDINGBEEN IS DRIE BENEN, EN DAT IS DE KERN VAN DE CORRECTIE VAN
#    2026-08-05. Het was één rechte stippel van 153,5 km; op de plek waar de
#    werkelijke leiding het verst van die lijn af ligt zat 15,4 km ertussen.
#    Nu: gestippeld waar niets is waargenomen (mijnterrein 4,8 km · La Negra →
#    Coloso 17,7 km), DOORGETROKKEN over het gevolgde tracé (137,8 km) —
#    dezelfde regel als de Collahuasi-leiding, die doorgetrokken staat waar de
#    kartering reikt en gestippeld op de laatste 736 m waar hij ophoudt.
#    Recept van de geometrie: v2/tools/maak_leidingbeen_escondida.py (de
#    puntenlijst staat in de broncode, dus dit been is op een verse clone
#    reproduceerbaar — anders dan de andere --been-geojson-benen).
bak_koper_escondida() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "leiding|slurryleiding op het mijnterrein — pijpenrekken door elkaar, niet te volgen (4,8 km)|-24.26200,-69.06000|-24.24800,-69.10500" \
    --been-geojson "leiding|slurryleiding Escondida → Coloso (gevolgd tracé, 137,8 km)|$BEEN/leidingbeen-escondida-coloso.geojson" \
    --stippel      "leiding|slurryleiding La Negra → Coloso — deels ingegraven + twee tunnels (17,7 km)|-23.76861,-70.29369|-23.75900,-70.46700" \
    --stippel "leiding|terminalverwerking Coloso (filterfabriek → laadsteiger)|-23.759,-70.467|-23.7569,-70.4652" \
    --stippel-geojson "zee|haven-aanloop Coloso (schematisch, over water — MARNET reikt hier niet)|$BEEN/aanloop-coloso.geojson" \
    --been    "zee|zeeschip Coloso → Beilun|-23.8,-71.3|29.9364,121.883" \
    --stippel "zee|haven-aanloop Beilun (MARNET-knoop ligt in de geul, het schip lost aan de berth)|29.9478,121.8837|29.9364,121.883" \
    --stippel "leiding|transportband losberth → landpunt/ertsveld (eigen terrein, geen net)|29.9364,121.883|29.92742,121.87573" \
    --stippel "leiding|ertsveld → laadspoor 北仑港站 (eigen terrein, geen net)|29.92742,121.87573|29.92653,121.87308" \
    --been-geojson "spoor|trein Beilun → Guixi (甬金-vrachtlijn)|$BEEN/spoorroute-nieuw-beilun-guixi.geojson" \
    --been-geojson "truck|kathode 贵冶 → walsdraadfabriek 铜材公司 (闪速大道)|$BEEN/stroombeen-guixi-fase-d.geojson" \
    --marker "Escondida — concentrator/indikkers|-24.26200,-69.06000" \
    --marker "Puerto Coloso — laadsteiger|-23.75690,-70.46520" \
    --marker "Beilun — ertsterminal, losberth|29.93640,121.88300" \
    --marker "北仑港站 — laadspoor|29.92653,121.87308" \
    --marker "Jiangxi Copper Guixi — ertslosbundel|28.32710,117.22600" \
    --marker "江西铜业铜材有限公司 — walsdraadfabriek (kathode-expeditie open)|28.33180,117.21919" \
    --routebrief v2/design/routebrieven/koper-escondida-guixi.md \
    --uit    v2/data/stroomroute-koper-escondida-guixi.json \
    --stroom koper-escondida-guixi \
    --titel  "Koper · Escondida → Guixi (China)"
}

# ── koper · Kamoa-Kakula → Lobito → Rotterdam → Duisburg (kathode)
# Routebrief: v2/design/routebrieven/koper-lobito-duisburg.md
#
# ⚠️ GERECONSTRUEERD 2026-08-05, NIET TERUGGEVONDEN — maar STRAKKER vastgelegd dan
#    bak_koper_escondida: dit commando reproduceert het bestand van 29-07 veld voor
#    veld (7 benen, 4 markers, alle 4.863 puntcoördinaten identiek, `gemaakt`
#    uitgezonderd), en drie van de vier vrijheidsgraden die daar open bleven zijn
#    hier DICHT gemeten:
#      * --graaf is NIET vrij: het moet `rijn` zijn. Met mississippi snapt het
#        Emmerich-punt 108,9 km weg en wordt het Rijnbeen 249,8 km over MARNET
#        dóór het IJsselmeer i.p.v. 161,1 km over tracks;
#      * het spoorbeen komt uit --been-geojson, niet --spoor-geojson: die vlag zet
#        zijn been altijd achteraan en hier staat spoor op plek 2;
#      * de spoor-GeoJSON is de OUDE spoorroute-kamoa-lobito.geojson, NIET de
#        `-nieuw-`-variant uit de 1-op-1-bake van 29-07: Kamoa→Lobito had al 0
#        omkeringen en is toen bewust niet vervangen (alleen Beilun→Guixi).
#    Vrij blijft: of de --been-uiteinden als anker of als routeerpunt zijn
#    opgegeven (beide snappen op dezelfde halte).
#
# ⚠️ HET WESEL-BEEN IS GEEN STIPPEL MEER — de tweede correctie van 2026-08-05.
#    Het was een rechte lijn van 47,3 km met 2 punten "want er is geen AIS-dekking"
#    (0 van 35.237 tracks raken lon 6,45-6,60, structureel gemeten over 12,5 uur).
#    Dat is de Escondida-denkfout op water: geen AIS zegt niets over of de
#    GEOMETRIE bestaat. De Rijn ligt daar volledig in OSM en de rechte lijn lag er
#    tot 7,26 km vanaf. Nu 66,64 km echte Rijnloop (164 punten, uiteinden op 87 en
#    36 m van de gevraagde punten). ⚠️ De AIS-meting blijft staan: dit been zegt
#    waar het WATER ligt, niet dat wij daar een schip gezien hebben.
#    Recept van de geometrie: v2/tools/maak_rivierbeen_wesel.py
bak_koper_lobito() {
  # ⚠️ eigen graaf: deze stroom vaart de Rijn, niet de Mississippi.
  local GRAAF_RIJN="v2/build-cache/ais/graaf/rijn"
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF_RIJN" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|aanvoer mijn → railhead Kamoa (geen spoor tot de poort)|-10.76,25.28|-10.6627,25.2873" \
    --been-geojson "spoor|trein Kamoa-Kakula → Lobito (Benguela-lijn)|$BEEN/spoorroute-kamoa-lobito.geojson" \
    --stippel      "zee|haven-aanloop Lobito (ligplaats nog niet vastgesteld)|-12.34709,13.549|-12.2702,13.5406" \
    --been         "zee|zeeschip Lobito → Rotterdam (Waalhaven)|-12.2702,13.5406|51.8935,4.4585" \
    --been         "binnenvaart|containerbinnenschip Waalhaven → Emmerich-vak|51.8935,4.4585|51.754,6.366" \
    --been-geojson "binnenvaart|Wesel-vak — echte Rijnloop uit OSM (geen AIS-dekking: 0 van 35.237 tracks)|$BEEN/rivierbeen-wesel.geojson" \
    --been         "binnenvaart|containerbinnenschip Wesel-vak → Duisport Ruhrort|51.4,6.745|51.4518,6.7565" \
    --marker "Kamoa-Kakula — mijn (Copperbelt)|-10.76,25.28" \
    --marker "Lobito — mineralenterminal (ligplaats open)|-12.34709,13.549" \
    --marker "Rotterdam — RHB, Waalhaven Noordzijde 4|51.8935,4.4585" \
    --marker "Duisburg — Duisport Ruhrort, Becken A|51.4518,6.7565" \
    --routebrief v2/design/routebrieven/koper-lobito-duisburg.md \
    --uit    v2/data/stroomroute-koper-lobito-duisburg.json \
    --stroom koper-lobito-duisburg \
    --titel  "Koper · Copperbelt → Lobito → Duisburg (kathode)"
}

# ── lithium · Greenbushes → Bunbury → zee → Yangtze → Zhangjiagang → Tianqi →
#    Wuxi → Nanjing → Tesla Giga Shanghai   (DE TWEEDE A–E-KETEN)
# Routebrief: v2/design/routebrieven/lithium-greenbushes-zhangjiagang.md
# Werkorder:  v2/design/werkorder-lithium-benen-5-8.md
#
# ⚠️ BENEN 1-4 GERECONSTRUEERD 2026-08-05, NIET TERUGGEVONDEN — maar strak: dit
#    commando reproduceerde het bestand van 30-07 TEKEN VOOR TEKEN (52.821 byte,
#    gelijke sha256 na normalisatie van `gemaakt`; 5 benen, 2.576 punten, 4
#    markers), twee keer onafhankelijk nagedraaid.
# ⚠️ DRIE VRIJHEIDSGRADEN, ALLE DRIE GEMETEN — en anders dan bij Lobito is
#    --graaf hier WÉL vrij: mississippi of rijn geeft hetzelfde bestand, want het
#    zeebeen rapporteert 0 track-edges / 46 MARNET-edges / 0 connectors en beide
#    track-graven liggen aan de andere kant van de wereld. Tóch gepind: een graaf
#    die deze route wél dekt kan het antwoord veranderen.
#
# ⚠️ TWEE ANKERS UIT DE BRIEF WAREN FOUT EN ZIJN VERVANGEN (werkorder A):
#    * de "Tesla-poort 3" 30.87390/121.76572 was het REKENKUNDIG MIDDEN VAN VIER
#      OSM-BUSHALTENODES — 1,0 m van een publieke straat, aan de westkant van het
#      kanaal, 60,9 m BUITEN de fabriekspolygoon. De echte poort ligt op
#      30.87423/121.76667, 18,2 m binnen way 635670279 (brug, wachtersgebouw).
#    * het Nanjing-anker 32.16300/118.87900 lag 21,4 m BUITEN het hek in beboste
#      helling. Het stond als "satelliet-gelegd op z16" — en z16 (2,0 m/px) kán
#      dat verschil niet zien. Nu 32.16111/118.87953, binnen het hek.
#
# ⚠️ DRIE PROCESGATEN BLIJVEN BEWUST ZICHTBAAR: de UITGAANDE laadplekken bij
#    Tianqi (219 m), Wuxi (310 m) en Nanjing (301 m) zijn niet gevonden, dus de
#    koppen van b6/b7/b8 zijn substituten. Die gaten ZIJN de ontbrekende ankers;
#    dichttrekken is de Waalhaven-klasse. Zelfde vorm als De Soto (grafiet) en
#    het procesgat bij 贵冶 (koper).
# ⚠️ HET GAT VAN 4.933 m TUSSEN BEEN 1 EN BEEN 2 BLIJFT OPEN, en het is het
#    grootste van alle vijf stromen. Het is GEEN fout uiteinde: -33.30640/
#    115.61330 is MARNET's eigen Bunbury-knoop en de eerstvolgende zeeknoop ligt
#    92,8 km verderop. ⚠️ EN maak_havenaanloop.py KAN HET HIER NIET OPLOSSEN: het
#    1:10M-landmasker is bij Bunbury LOKAAL OMGEKEERD (een varende bulkcarrier
#    staat als land, een barrièreduin als water — werkorder F2). Eerst de
#    vaargeul satelliet-leggen, dán een aanloop uit handmatige punten.
bak_lithium() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|truck Greenbushes → Bunbury Berth 8 (Maranup Ford Rd → South Western Hwy)|$BEEN/stroombeen-greenbushes-bunbury.geojson" \
    --been         "zee|zeeschip Bunbury → Yangtze-monding|-33.31995,115.66385|31.4074,121.4848" \
    --stippel      "zee|overgang zeenet → Yangtze-bulklaag (MARNET houdt hier op)|31.51,121.4187|31.4512,121.4769" \
    --been-geojson "binnenvaart|Yangtze-monding → Zhangjiagang, zuidgeul langs Shuangshan-eiland|$BEEN/rivierbeen-yangtze-zhangjiagang.geojson" \
    --stippel      "binnenvaart|aanloop naar de ligplaats (anker ≠ routeerpunt)|31.9733,120.4202|31.968,120.4205" \
    --been-geojson "truck|last mile kade → poort Tianqi (常金线 X301 → 长江北路 → 东新路)|$BEEN/stroombeen-zhangjiagang-lastmile.geojson" \
    --been-geojson "truck|carbonaat/hydroxide Tianqi → kathodefabriek Wuxi (S23 → G4221 → S19)|$BEEN/stroombeen-zhangjiagang-wuxi.geojson" \
    --been-geojson "truck|kathodepoeder Wuxi → LG ES Nanjing (G42 沪宁高速 → G2503 → 栖霞大道)|$BEEN/stroombeen-wuxi-nanjing.geojson" \
    --been-geojson "truck|2170-cellen Nanjing → Tesla Giga Shanghai poort 3 (G42 → G1503 上海绕城 → G228 → 江山路)|$BEEN/stroombeen-nanjing-giga-shanghai.geojson" \
    --marker "Greenbushes — concentraatloods (laadplek)|-33.86495,116.05505" \
    --marker "Bunbury — Berth 8, scheepslader|-33.31995,115.66385" \
    --marker "Yangtze-monding — overgang zeenet → rivier|31.45120,121.47690" \
    --marker "Zhangjiagang — kade Zhangjiagang Port Group (ertsen/hout/staal)|31.96800,120.42050" \
    --marker "天齐锂业（江苏）— poort 东新路 5 (uitgaande laadplek open)|32.01218,120.45771" \
    --marker "乐友新能源材料（无锡）— laaddock westgevel|31.52362,120.47518" \
    --marker "乐友新能源材料（无锡）— zuidpoort 锡梅路 (uitgaand, substituut)|31.52084,120.47492" \
    --marker "LG Energy Solution Nanjing — New Port-campus|32.16111,118.87953" \
    --marker "LG Energy Solution Nanjing — hoofdpoort 恒谊路 (uitgaand, substituut)|32.15840,118.87950" \
    --marker "Tesla Giga Shanghai — poort 3 (losplek binnen het terrein open)|30.87423,121.76667" \
    --routebrief v2/design/routebrieven/lithium-greenbushes-zhangjiagang.md \
    --uit    v2/data/stroomroute-lithium-greenbushes-zhangjiagang.json \
    --stroom lithium-greenbushes-zhangjiagang \
    --titel  "Lithium · Greenbushes → Zhangjiagang → Tesla Giga Shanghai (spodumeen SC6.0 → 2170-cel)"
}

# ⚠️ OPENSTAAND: het recept van de LAATSTE stroom (koper Collahuasi→Tongling)
# staat hier nog NIET. Die zijn
# gebakken vóór dit bestand bestond en hun vlaggen leven nog in een
# shell-historie. Reconstrueer ze bij de eerstvolgende herbake van elk — en
# herbak ze niet zonder eerst de huidige uitvoer te bewaren, want net als bij
# Balama→Nacala kan het gereedschap intussen veranderd zijn.
#
# ⚠️ REPRODUCEERBAARHEID IS BEGRENSD DOOR v2/.gitignore (build-cache/): $GRAAF,
# $MARNET, $NE en alle --been-geojson-bestanden zijn ONGETRACKT. Op een verse
# clone draait geen van deze recepten. Geldt even hard voor bak_grafiet.

# ── M29 · LICHTE WERKWIJZE (v2/design/routebrief-licht.md) ──────────────────
# Eén functie per keten, ankers op site-niveau, geen last-mile-benen; stippel
# betekent ook hier: hier reikt het net niet.

# ── koper · TFM (Fungurume) → Kasumbalesa → Durban → China (kathode, truck)
# Routebrief: v2/design/routebrieven/koper-kolwezi-durban.md (LAR-561)
# ⚠️ De aanlanding in China (Shanghai bonded zone) is aannemelijk en niet
#    getekend als been: het zeebeen eindigt op het bestaande anker Yangtze-monding.
bak_koper_durban() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --been-geojson "truck|kathode TFM-plant → Kasumbalesa → Lusaka → Chirundu → Harare → Beitbridge → Durban DCT (RN39/RN1 · T3/T2 · A1/A4 · N1/N3)|$BEEN/stroombeen-tfm-durban.geojson"     --stippel-geojson "zee|haven-aanloop Durban (schematisch, over water — MARNET-knoop 15 km buiten de haven)|$BEEN/aanloop-durban.geojson"     --been         "zee|zeeschip Durban → Yangtze-monding (kathode, aanlanding Shanghai bonded — aannemelijk)|-29.817,31.174|31.42704,121.47618"     --marker "Tenke Fungurume — TFM-plant, EW-hallen (CMOC)|-10.5685,26.1975"     --marker "Kasumbalesa — grens DRC/Zambia|-12.2658,27.7959"     --marker "Beitbridge — grens Zimbabwe/RSA|-22.2206,29.9858"     --marker "Durban — DCT Pier 2, noordkade (kathode in containers)|-29.8790,31.0160"     --marker "Shanghai/Luojing — Yangtze-monding (aanlanding bonded zone, aannemelijk)|31.42704,121.47618"     --routebrief v2/design/routebrieven/koper-kolwezi-durban.md     --uit    v2/data/stroomroute-koper-tfm-durban.json     --stroom koper-tfm-durban     --titel  "Koper · Tenke Fungurume → Durban → China (kathode)"
}

# ── koper · Las Bambas → Pillones → Matarani → Yangtze → Tongling (concentraat)
# Routebrief: v2/design/routebrieven/koper-lasbambas-matarani.md (LAR-559)
# ⚠️ Het Chinese deel is een GEDEELD been met koper-collahuasi-tongling (§1b):
#    het zeebeen eindigt op exact hetzelfde punt (31.51,121.4187) en het
#    rivierbeen is een letterlijke kopie van dat been 5 — geen tweede versie.
# ⚠️ Twee stippels rond het spoor: de spoorlus van de Pillones-loods en de
#    havensporen van Matarani zitten niet in het 1-op-1-net (3,4 en 1,7 km).
bak_koper_lasbambas() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --been-geojson "truck|concentraat Las Bambas → Pillones — corredor minero del sur (PE-3SF → PE-3SY Mara/Ccapacmarca/Velille → PE-3SG Yauri → PE-34E/34A)|$BEEN/stroombeen-lasbambas-pillones.geojson"     --stippel      "spoor|Pillones — overslagloods → hoofdspoor (spoorlus niet in het net)|-15.9842,-71.2184|-15.9723,-71.1888"     --been-geojson "spoor|trein Pillones → Matarani (PeruRail, Ferrocarril del Sur)|$BEEN/spoorroute-pillones-matarani.geojson"     --stippel      "spoor|spooreinde → Muelle F, shiploaderpier (haventerrein, geen net)|-17.0049,-72.0964|-17.0044,-72.1124"     --stippel-geojson "zee|haven-aanloop Matarani (schematisch, over water — MARNET reikt hier niet: 72 km)|$BEEN/aanloop-matarani.geojson"     --been         "zee|zeeschip Matarani → Yangtze-monding (concentraat; afnemer Tongling = samenvloeiingsaanname)|-17.300,-72.700|31.51,121.4187"     --been-geojson "binnenvaart|Yangtze-monding → Tongling-kade — gedeeld been met Collahuasi→Tongling|$BEEN/rivierbeen-yangtze-tongling-gedeeld.geojson"     --marker "Las Bambas — concentrator (MMG)|-14.0894,-72.3357"     --marker "Pillones — overslagstation weg → spoor|-15.9842,-71.2184"     --marker "Matarani — Muelle F, concentraatpier (Tisur)|-17.0044,-72.1124"     --marker "Shanghai/Luojing — Yangtze-monding|31.42704,121.47618"     --marker "Tongling Nonferrous — kade van de TNMG-smelter (gedeeld)|30.98656,117.7718"     --routebrief v2/design/routebrieven/koper-lasbambas-matarani.md     --uit    v2/data/stroomroute-koper-lasbambas-tongling.json     --stroom koper-lasbambas-tongling     --titel  "Koper · Las Bambas → Matarani → Tongling (China)"
}

# ── koper · Grasberg → Portsite/Amamapare → Manyar/Gresik (concentraat, Indonesische downstreaming)
# Routebrief: v2/design/routebrieven/koper-grasberg-manyar.md (LAR-557)
# ⚠️ De slurryleiding (3 × 115 km, FCX) is in OSM NIET gekarteerd: schematische
#    stippel langs de HEAT-corridor (Tembagapura → Timika → Portsite).
# ⚠️ De Manyar-loskade is ONZEKER (Esri-opname van vóór de oplevering); het
#    zeebeen eindigt op de MARNET-knoop bij Gresik, de aanloop is stippel.
# ⚠️ PT Smelting (1,3 Mt/j) is een reële vertakking op dezelfde aanloop —
#    als stippel getekend, de steigerkop is niet gelegd.
bak_koper_grasberg() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --stippel-geojson "leiding|slurryleiding Grasberg mill → Portsite (3 × 115 km, schematisch langs de HEAT-corridor — OSM heeft geen pipeline-way)|$BEEN/leidingbeen-grasberg-portsite-schematisch.geojson"     --stippel-geojson "zee|haven-aanloop Portsite/Amamapare (schematisch, over water — 12 km riviermonding, MARNET reikt niet)|$BEEN/aanloop-portsite.geojson"     --been         "zee|zeeschip Portsite → Gresik (Arafurazee → Bandazee → Straat Madura)|-4.928,136.401|-7.138,112.669"     --stippel-geojson "zee|haven-aanloop Manyar/JIIPE (schematisch — loskade onzeker: opname van vóór de oplevering)|$BEEN/aanloop-manyar-aankomst.geojson"     --stippel      "leiding|concentraat loskade → Manyar-smelter (eigen terrein, procesgat 2,6 km)|-7.0855,112.6500|-7.0890,112.6270"     --stippel      "truck|kathode Manyar → Hailiang-foliefabriek (fase D, aannemelijk: intentie 2024; estate-wegen niet gescand)|-7.0890,112.6270|-7.0740,112.6194"     --stippel      "zee|vertakking: PT Smelting Gresik (1,3 Mt/j) — steigerkop niet gelegd|-7.138,112.669|-7.1400,112.6400"     --marker "Grasberg — mill/concentrator (PTFI)|-4.0905,137.1155"     --marker "Portsite/Amamapare — concentraatkade|-4.8290,136.8405"     --marker "Manyar — loskade JIIPE (onzeker)|-7.0855,112.6500"     --marker "Manyar — Freeport-smelter (1,7 Mt concentraat/j)|-7.0890,112.6270"     --marker "PT Smelting Gresik (1,3 Mt/j, vertakking)|-7.1400,112.6400"     --marker "Hailiang Gresik — foliefabriek (fase D, aannemelijk)|-7.0740,112.6194"     --routebrief v2/design/routebrieven/koper-grasberg-manyar.md     --uit    v2/data/stroomroute-koper-grasberg-manyar.json     --stroom koper-grasberg-manyar     --titel  "Koper · Grasberg → Amamapare → Manyar/Gresik (Indonesië)"
}

# ── koper · Chuquicamata → FCAB → Mejillones (TGN) → Yangtze → Tongling (concentraat)
# Routebrief: v2/design/routebrieven/koper-chuquicamata-china.md (LAR-558)
# ⚠️ Drie stippels rond het spoor: het mijnemplacement van Chuquicamata (9 km
#    tot de eerste hoofdspoorknoop), de spur naar de TGN-rotainer-yard (2025,
#    niet in OSM, 2,9 km) en de band/shiploader naar de pierkop (1,3 km).
# ⚠️ Het Chinese deel is het GEDEELDE been met Collahuasi→Tongling (§1b); de
#    afnemer Tongling is "aannemelijk: één bron" (Beilun→Guixi is het alternatief).
bak_koper_chuqui() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --stippel      "spoor|laadspoor Chuquicamata-concentrator → hoofdspoor FCAB (mijnemplacement niet in het net)|-22.3050,-68.9140|-22.3508,-68.8418"     --been-geojson "spoor|trein Chuquicamata → Prat (empalme) → Mejillones (FCAB-meterspoor, rotainers)|$BEEN/spoorroute-chuqui-mejillones.geojson"     --stippel      "spoor|spur naar de TGN-rotainer-yard (terminal 2025, niet in OSM)|-23.0905,-70.3953|-23.0693,-70.3787"     --stippel      "leiding|transportband/shiploader TGN-pier → pierkop (eigen terrein)|-23.0693,-70.3787|-23.0580,-70.3802"     --stippel-geojson "zee|haven-aanloop Mejillones (schematisch, over water — MARNET reikt hier niet: 136 km)|$BEEN/aanloop-mejillones.geojson"     --been         "zee|zeeschip Mejillones → Yangtze-monding (concentraat; afnemer Tongling aannemelijk, één bron)|-23.800,-71.300|31.51,121.4187"     --been-geojson "binnenvaart|Yangtze-monding → Tongling-kade — gedeeld been met Collahuasi→Tongling|$BEEN/rivierbeen-yangtze-tongling-gedeeld.geojson"     --marker "Chuquicamata — concentrator/laadspoor (Codelco)|-22.3050,-68.9140"     --marker "Prat — empalme ramal Mejillones (FCAB)|-23.4727,-70.1714"     --marker "Mejillones — TGN-concentraatterminal, pierkop (Puerto Angamos)|-23.0580,-70.3802"     --marker "Shanghai/Luojing — Yangtze-monding|31.42704,121.47618"     --marker "Tongling Nonferrous — kade van de TNMG-smelter (gedeeld)|30.98656,117.7718"     --routebrief v2/design/routebrieven/koper-chuquicamata-china.md     --uit    v2/data/stroomroute-koper-chuqui-tongling.json     --stroom koper-chuqui-tongling     --titel  "Koper · Chuquicamata → Mejillones → Tongling (China)"
}

# ── koper · Antofagasta → Brunsbüttel → Aurubis Hamburg → DG Emmerich (Europese raffinage)
# Routebrief: v2/design/routebrieven/koper-aurubis-hamburg.md (LAR-563)
# ⚠️ Zeeschepen lossen in de Elbehafen Brunsbüttel (Aurubis-milieuverklaring);
#    twee Schramm-binnenschepen shuttlen het concentraat naar de Peute — dus een
#    extra overslag. De Elbe Brunsbüttel → Hamburg is een ZEEVAARWEG en zit in
#    MARNET; de bulklaag valt daar in losse componenten (maak_rivierbeen: geen
#    pad), dus het binnenvaartbeen loopt over MARNET (modaliteit uit de vlag).
# ⚠️ Herkomsthaven Antofagasta is AANNEMELIJK (Codelco 48% van de concentraat-
#    verschepingen daar; Aurubis publiceert zijn laadhaven niet).
# ⚠️ Hamburg-aanloop: de 1:10M-kust kent de haven niet (maak_havenaanloop liep
#    vast) → rechte stippel Norderelbe → Müggenburger Kanal, 8 km.
# ⚠️ Kathode Hamburg → Emmerich per spoor is AANNEMELIJK (infrastructuurbewijs:
#    DG heeft een spooraansluiting tot op de pier; de modaliteit zelf is nergens
#    gepubliceerd; alternatief truck 381 km).
bak_koper_aurubis() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --stippel-geojson "zee|haven-aanloop Antofagasta (schematisch, over water — MARNET reikt hier niet: 97 km)|$BEEN/aanloop-antofagasta.geojson"     --been         "zee|zeeschip Antofagasta → Brunsbüttel (concentraat, via Panama)|-23.800,-71.300|53.8771,9.2273"     --stippel-geojson "zee|haven-aanloop Elbehafen Brunsbüttel (schematisch)|$BEEN/aanloop-brunsbuettel-aankomst.geojson"     --stippel-geojson "binnenvaart|Schramm-binnenschip: vertrek Elbehafen Brunsbüttel (schematisch)|$BEEN/aanloop-brunsbuettel.geojson"     --been         "binnenvaart|Schramm-binnenschip Brunsbüttel → Hamburg (Unterelbe → Norderelbe; zeevaarweg in MARNET)|53.8771,9.2273|53.5451,9.9273"     --stippel      "binnenvaart|Norderelbe → Müggenburger Kanal, concentraatkade Werk Ost (schematisch — 1:10M-kust kent de haven niet)|53.5451,9.9273|53.5163,10.0418"     --stippel      "spoor|Aurubis Werk Ost → hoofdspoor (emplacement, niet in het net)|53.5140,10.0400|53.5199,10.0119"     --been-geojson "spoor|kathode Aurubis Hamburg → DG Emmerich (Rollbahn Rotenburg–Bremen–Osnabrück–Münster → Oberhausen → Hollandstrecke; aannemelijk: modaliteit ongedocumenteerd)|$BEEN/spoorroute-hamburg-emmerich.geojson"     --stippel      "spoor|spoor → Deutsche Giessdraht, kade/emplacement Industriehafen|51.8350,6.2494|51.8284,6.2630"     --marker "Antofagasta — molo/ATI, concentraatkade (herkomst aannemelijk)|-23.6500,-70.4088"     --marker "Brunsbüttel — Elbehafen, droge-bulkkade (zee → binnenschip)|53.8878,9.1740"     --marker "Aurubis Hamburg — concentraatkade Müggenburger Kanal|53.5163,10.0418"     --marker "Aurubis Hamburg — Werk Ost, smelter + raffinaderij (~400 kt kathode/j)|53.5140,10.0400"     --marker "Emmerich — Deutsche Giessdraht, gietwalsdraad (290 kt/j)|51.8284,6.2630"     --routebrief v2/design/routebrieven/koper-aurubis-hamburg.md     --uit    v2/data/stroomroute-koper-aurubis-hamburg.json     --stroom koper-aurubis-hamburg     --titel  "Koper · Antofagasta → Brunsbüttel → Aurubis Hamburg → Emmerich"
}

# ── koper · Oyu Tolgoi → Gashuun Sukhait/Ganqimaodu → bonded → Bayannur Feishang (concentraat, alleen land)
# Routebrief: v2/design/routebrieven/koper-oyutolgoi-china.md (LAR-562)
# ⚠️ Eén wegscan (profiel koper-oyutolgoi-feishang), gesplitst op het bonded-
#    anker: dezelfde Mongoolse trucks rijden door tot de bonded warehouse
#    (~7 km achter de grens, NI 43-101), daar neemt de klant af. De smelter
#    Feishang is de enige met een bron (158,2 kt OT-concentraat in 2022);
#    Jinchuan/Tongling/JCC zijn alleen intentieverklaringen → vertakking.
# ⚠️ De bonded-loods zelf is AANNEMELIJK (welke loods "Huafang" is, is niet
#    gebrond). Geen zee: de keten eindigt bij de smelter (anodes, stoppunt).
bak_koper_oyutolgoi() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --been-geojson "truck|concentraat Oyu Tolgoi → OT-betonweg → grenspost Gashuun Sukhait → Ganqimaodu → bonded warehouse (105 + 7 km)|$BEEN/stroombeen-ot-bonded.geojson"     --been-geojson "truck|concentraat bonded warehouse → G242 → G335 → Bayannur Feishang Copper (aannemelijk: één bron voor de afnemer)|$BEEN/stroombeen-bonded-feishang.geojson"     --marker "Oyu Tolgoi — concentrator/zakkenplant (Rio Tinto/Erdenes)|43.0480,106.8360"     --marker "Gashuun Sukhait — grenspost Mongolië/China|42.4146,107.5692"     --marker "Ganqimaodu — bonded warehouse (Huafang, aannemelijk)|42.3740,107.5990"     --marker "Bayannur Feishang Copper — smelter (100 kt/j ruwkoper)|40.9694,106.8530"     --routebrief v2/design/routebrieven/koper-oyutolgoi-china.md     --uit    v2/data/stroomroute-koper-oyutolgoi-feishang.json     --stroom koper-oyutolgoi-feishang     --titel  "Koper · Oyu Tolgoi → Ganqimaodu → Bayannur (over land)"
}

# ── koper · El Teniente → Caletones → Ventanas → San Antonio → Panama → Rotterdam (kathode naar Europa)
# Routebrief: v2/design/routebrieven/koper-elteniente-rotterdam.md (LAR-560)
# ⚠️ De Carretera del Cobre heeft in OSM twee gaten: Maitenes–Confluencia staat
#    alleen als geplande weg (2,8 km) en bij Coya ligt 5,6 km H-27 als track
#    (komt de scanner niet door) → drie gemeten wegstukken met twee stippels.
# ⚠️ ETEO-anker en San Antonio-kade zijn ONZEKER (brief §3); de pulpleiding
#    Colón → Caletones is aannemelijk (Codelco: "en forma de pulpa").
# ⚠️ Zeebeen via het Panamakanaal (MARNET kiest die zelf; 1,8 km van Gatún
#    bij de Aurubis-keten); San Antonio ligt 74 km van de dichtstbijzijnde
#    MARNET-zeeknoop → aanloop over water als stippel.
bak_koper_elteniente() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --stippel      "leiding|pulpleiding concentrator Colón → Caletones-smelter (~2 km, aannemelijk)|-34.0900,-70.4630|-34.1061,-70.4503"     --been-geojson "truck|anodes Caletones → Maitenes (Carretera del Cobre, oude weg; Codelco-privéwegen)|$BEEN/stroombeen-caletones-maitenes.geojson"     --stippel      "truck|Carretera del Cobre Maitenes–Confluencia (in OSM alleen als geplande weg gekarteerd)|-34.15062,-70.54925|-34.17568,-70.54976"     --been-geojson "truck|anodes Confluencia → Coya (Carretera del Cobre → H-27)|$BEEN/stroombeen-confluencia-coya.geojson"     --stippel      "truck|H-27 bij Coya (in OSM 5,6 km als track — komt de scanner niet door)|-34.19657,-70.57698|-34.19650,-70.61359"     --been-geojson "truck|anodes Coya → Rancagua → ETEO Los Lirios (H-27 → Ruta 5)|$BEEN/stroombeen-coya-eteo.geojson"     --stippel      "spoor|overslag ETEO — emplacement (anker onzeker)|-34.2118,-70.7748|-34.2099,-70.7710"     --been-geojson "spoor|anodes ETEO → Santiago → San Pedro → Ventanas (Fepasa, 850 t/dag)|$BEEN/spoorroute-eteo-ventanas.geojson"     --stippel      "spoor|spoor → Ventanas-raffinaderij (terrein)|-32.7540,-71.4789|-32.7596,-71.4816"     --been-geojson "truck|kathode Ventanas → Concón → Casablanca → Algarrobo → Puerto San Antonio (Codelco-corridor 2026)|$BEEN/stroombeen-ventanas-sanantonio.geojson"     --stippel-geojson "zee|haven-aanloop San Antonio (schematisch, over water — MARNET reikt hier niet: 80 km)|$BEEN/aanloop-sanantonio.geojson"     --been         "zee|zeeschip San Antonio → Rotterdam (kathode, via Panama)|-33.0,-72.0|51.8935,4.4585"     --marker "El Teniente — concentrator Colón (Codelco)|-34.0900,-70.4630"     --marker "Caletones — smelter (anodes)|-34.1061,-70.4503"     --marker "ETEO Los Lirios — overslag truck → spoor (onzeker)|-34.2118,-70.7748"     --marker "Ventanas — raffinaderij (kathode)|-32.7596,-71.4816"     --marker "San Antonio — espigón, kathodekade (onzeker)|-33.5885,-71.6170"     --marker "Rotterdam — RHB, Waalhaven Noordzijde 4|51.8935,4.4585"     --routebrief v2/design/routebrieven/koper-elteniente-rotterdam.md     --uit    v2/data/stroomroute-koper-elteniente-rotterdam.json     --stroom koper-elteniente-rotterdam     --titel  "Koper · El Teniente → Ventanas → San Antonio → Rotterdam (kathode)"
}

# ── lithium · Salar de Atacama (SQM) → Salar del Carmen → Antofagasta → China (carbonaat)
# Routebrief: v2/design/routebrieven/lithium-atacama-antofagasta.md
# ⚠️ Fase D/E vervallen (brief §6): geen bron noemt de Chinese fabriek/haven die
#    het SQM-carbonaat lost, dus de brief stopt op de Yangtze-monding
#    (aanlanding-aannemelijk, 72% van de Chileense export). "aannemelijk: één
#    bron" staat in de beennaam, niet in de lijnstijl.
# ⚠️ B1 IS TRUCK MET TANKWAGENS (LiCl-oplossing ~6% Li), GEEN PIJPLEIDING — de
#    v1-aanname `pipeline` was fout (brief §2). De plantweg (compacted service,
#    10,9-16 km) valt deels buiten de 12 km-eindzone: de anker→weg-aanloop van
#    7,61 km blijft als restje staan (getekend, geen stippel — de weg bestaat en
#    is gescand, alleen de eindzone-drempel snijdt hem af).
# ⚠️ B2 IS +15,4% BOVEN DE GEPUBLICEERDE ~19 KM (buiten ±15%, bevinding, niet
#    dichtgetrokken): de via-keten van de brief zelf gaf al 19 km hemelsbreed
#    tegen de bronzin "15 km west of the Salar del Carmen" — twee losse
#    schattingen die niet op elkaar aansluiten.
# ⚠️ ZEEBEEN: kade > 25 km van een zeeknoop → letterlijke kopie van de
#    bestaande haven-aanloop `aanloop-antofagasta.geojson` (koper-aurubis-
#    hamburg, cu-antofagasta-kade = li-antofagasta-kade, zelfde kade) + MARNET
#    zeeknoop -23.80,-71.30 → Yangtze-monding (bestaand anker, gedeeld met vier
#    koperstromen).
bak_lithium_atacama_antofagasta() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --been-geojson "truck|tankwagens SQM Salar de Atacama → PQL Carmen (plantweg → Ruta B-39 → Baquedano → Ruta 5)|$BEEN/stroombeen-atacama-carmen.geojson"     --been-geojson "truck|carbonaat/hydroxide (containers) PQL Carmen → Puerto Antofagasta ATI (Ruta 5 → Ruta 26 → Av. Salvador Allende)|$BEEN/stroombeen-carmen-antofagasta.geojson"     --stippel-geojson "zee|haven-aanloop Antofagasta (schematisch, over water — MARNET reikt hier niet: 97 km; gedeeld met koper-aurubis-hamburg)|$BEEN/aanloop-antofagasta.geojson"     --been         "zee|zeeschip Antofagasta → Yangtze-monding (containerschip, 50°N-lane; aannemelijk: één bron, 72% van de Chileense carbonaatexport)|-23.800,-71.300|31.42704,121.47618"     --marker "SQM Salar de Atacama — lithiumplant (laadplek tankwagens)|-23.5675,-68.4000"     --marker "SQM Planta Química de Litio Carmen — verwerkingsknoop (LiCl → Li2CO3/LiOH)|-23.6335,-70.2600"     --marker "Puerto Antofagasta, ATI — kade (containers, gedeeld anker)|-23.6500,-70.4088"     --marker "Yangtze-monding — aanlanding China (aannemelijk, gedeeld anker)|31.42704,121.47618"     --routebrief v2/design/routebrieven/lithium-atacama-antofagasta.md     --uit    v2/data/stroomroute-lithium-atacama-antofagasta.json     --stroom lithium-atacama-antofagasta     --titel  "Lithium · Salar de Atacama → Antofagasta → China (LiCl → carbonaat)"
}

# ── grafiet · Balama → Nacala → Qingdao (QQCT) → Laixi/Nanshu (Qingdao Shinestar, China)
# Routebrief: v2/design/routebrieven/grafiet-balama-laixi.md (LICHTE werkwijze M29)
# ⚠️ Been 1 (Balama→Nacala) EN de haven-aanloop Nacala zijn LETTERLIJKE KOPIEËN
#    van bak_grafiet (Balama→Vidalia) — géén tweede scan/aanloop-poging.
# ⚠️ Zeebeen (b2) heeft GEEN aanloop nodig: QQCT-kade (36.0124,120.2070) ligt
#    5,6 km van zeeknoop 5841 (< 25 km) en snapt automatisch.
# ⚠️ VOLUME = NUL (brief §1, Lars-besluit 2026-08-04-klasse): Syrah meldde voor
#    2025 géén natuurlijk-grafietverkoop aan Chinese anodeklanten. Doorgetrokken,
#    niet gestippeld — de weg is echt, de lading niet (werkwijze §7).
# ⚠️ QQCT-kade én de Qingdao→Laixi-corridor zijn *aannemelijk: één bron* (brief
#    §3/§7: contract Langruite 2018/2019) — dat staat in de been-/markernamen,
#    niet in de lijnstijl.
bak_grafiet_balama_laixi() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --been-geojson "truck|vrachtwagen Balama → Nacala (N380/N1) — LETTERLIJKE KOPIE bak_grafiet been 1|$BEEN/stroombeen-balama-nacala.geojson"     --stippel-geojson "zee|haven-aanloop Nacala (schematisch, over water — MARNET reikt hier niet, 152,1 km — LETTERLIJKE KOPIE bak_grafiet)|$BEEN/aanloop-nacala.geojson"     --been         "zee|zeeschip Nacala → Qingdao QQCT (Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Gele Zee; losplek aannemelijk, geen bron noemt de terminal)|-15.0,41.7|36.0124,120.2070"     --been-geojson "truck|vrachtwagen QQCT-kade → Qingdao Shinestar-fabriek Nanshu (S7602 → G22 → G15 om de Jiaozhou-baai → S214; aannemelijk: één bron, contract 2018)|$BEEN/stroombeen-qingdao-qqct-laixi-shinestar.geojson"     --marker "Balama-plant, bagging on-site (Syrah/Twigg)|-13.31000,38.66000"     --marker "Porto de Nacala — containerterminal oostoever|-14.53830,40.66730"     --marker "QQCT Qianwan-kade, Qingdao (aannemelijk)|36.01240,120.20700"     --marker "Qingdao Shinestar SPG-fabriek, Nanshu|37.02520,120.32240"     --routebrief v2/design/routebrieven/grafiet-balama-laixi.md     --uit    v2/data/stroomroute-grafiet-balama-laixi.json     --stroom grafiet-balama-laixi     --titel  "Grafiet · Balama → Nacala → Qingdao → Laixi (China)"
}

# ── grafiet · Jinzhou (CNPC-naaldcokes) → Zhangjiakou → Baotou Jiuyuan (Shanshan-AAM-basis)
# Routebrief: v2/design/routebrieven/grafiet-jinzhou-baotou.md (LICHTE werkwijze M29)
# ⚠️ Modaliteit spoor is een WERKAANNAME (brief §7): geen bron noemt expliciet
#    spoor voor dit traject; een wegalternatief (G1/G6, ~1.200 km) is niet
#    uitgesloten.
# ⚠️ Eén corridorkeuze op de Jingbao-lijn (via Shanhaiguan/Beijing-ring, niet de
#    Datong–Qinhuangdao-kolenlijn) → twee spoorrouter-runs, gesplitst bij
#    Zhangjiakou (geen --via-vlag op de spoorrouter). Kop→Zhangjiakou geraakt
#    2,4 km van Shanhaiguan-station; Zhangjiakou→staart geraakt 0,4 km van
#    Hohhot-station — beide bevestigen de Jingbao-hoofdlijn i.p.v. een omweg.
# ⚠️ "Aannemelijk: bedrijfsniveau" — geen bron noemt de ontvangende Shanshan-
#    fabriek met naam (kaderakkoord 2021 bewijst alleen de relatie CNPC↔Shanshan
#    op bedrijfsniveau). Doorgetrokken, niet gestippeld — dat staat in de
#    beennaam/markernaam, niet in de lijnstijl (werkwijze §valkuilen).
# ⚠️ Eén korte omkering (180°, ~30 m boogstraal) op 4,9 km van het Jinzhou-
#    anker — een kopmaak-plek bij het laademplacement, zelfde klasse als
#    Chuqui (9 km)/Matarani (1,7 km): geen bugreden, het emplacement zelf zit
#    niet in het 1-op-1-net. Snap Baotou-eind 1,22 km (anker ≠ routeerpunt,
#    het exacte Shanshan-perceel binnen Jiuyuan Industrial Park is niet
#    individueel bevestigd — brief §7).
# ⚠️ Fase D vervalt (brief §6): geen bron koppelt Shanshan Baotou aan één
#    celfabriek. Geen zee, geen MARNET — de keten is een pure landas.
bak_grafiet_jinzhou_baotou() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --been-geojson "spoor|trein Jinzhou → Zhangjiakou (Jingbao-lijn via Shanhaiguan; werkaanname)|$BEEN/spoorroute-grafiet-jinzhou-baotou-jinzhou-zhangjiakou.geojson"     --been-geojson "spoor|trein Zhangjiakou → Baotou Jiuyuan (Jingbao-lijn via Hohhot; werkaanname, aannemelijk: bedrijfsniveau)|$BEEN/spoorroute-grafiet-jinzhou-baotou-zhangjiakou-baotou.geojson"     --marker "CNPC Jinzhou Petrochemical — naaldcokesfabriek (kop)|41.13159,121.08583"     --marker "Shanshan Baotou Jiuyuan — grafitisatie-/AAM-basis (staart, aannemelijk)|40.60860,109.67826"     --routebrief v2/design/routebrieven/grafiet-jinzhou-baotou.md     --uit    v2/data/stroomroute-grafiet-jinzhou-baotou.json     --stroom grafiet-jinzhou-baotou     --titel  "Grafiet · Jinzhou → Zhangjiakou → Baotou (China)"
}

# ── grafiet · Lake Charles (P66, naaldcokes) → Novonix Riverside (Chattanooga)
#    → Panasonic Energy Kansas, De Soto (synthetisch AAM, geen zee)
# Routebrief: v2/design/routebrieven/grafiet-lakecharles-desoto.md (LICHTE werkwijze M29)
# ⚠️ BEIDE BENEN DRAGEN "aannemelijk: één bron; volume nul tot H2 2027" (brief
#    §1/§5): Novonix' 20-F noemt Phillips 66 als één van "a select few other
#    suppliers", geen bindende supply-overeenkomst; massaproductie voor
#    Panasonic start pas H2 2027. Doorgetrokken, niet gestippeld — de weg is
#    gemeten, de lading nog niet (werkwijze §7, dezelfde vorm als grafiet-
#    balama-vidalia/-laixi en lithium-atacama-antofagasta).
# ⚠️ MODALITEIT VAN BEIDE BENEN IS EEN WERKAANNAME (brief §7): cokes gaat in de
#    VS vaak per spoorhopper en beide sites liggen aan spoor; zonder bron voor
#    een gedocumenteerd spoorbeen is truck de getekende keuze.
# ⚠️ GEEN ZEE: dit is de eerste grafietketen van de atlas zonder MARNET-been —
#    beide fabrieken liggen landinwaarts en de brief stopt bij het De Soto-
#    routeerpunt (fase E is al been 10 van grafiet-balama-vs, niet opnieuw
#    getekend — brief §1/§6).
# ⚠️ BEEN 2 EINDIGT OP HET ROUTEERPUNT (rotonde Astra Parkway), NIET HET
#    TERREINANKER (38.93815,-95.00240) — hergebruik van hetzelfde De Soto-
#    anker/routeerpunt-paar als grafiet-balama-vidalia been 7/8: het terrein
#    is over de weg niet bereikbaar en de docks zijn niet gelegd. De marker
#    hieronder staat daarom op het terreinanker, ~480 m van de lijn
#    (anker ≠ routeerpunt, brief §3).
# ⚠️ KOP VAN BEEN 1 OP PRIVÉ-TERREINWEGEN (Phillips 66 Lake Charles Manufacturing
#    Complex, `access=private` binnen het terrein) → profiel
#    grafiet-lakecharles-desoto-lakecharles-riverside draait met
#    eindToegangPrivaat: True (v2/tools/maak_stroombeen_weg.py).
bak_grafiet_lakecharles_desoto() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen P66 Lake Charles — cokesveld → Novonix Riverside (I-10 → I-12 → I-59 → I-24; aannemelijk: één bron; volume nul tot H2 2027)|$BEEN/grafiet-lakecharles-desoto-weg-lakecharles-riverside.geojson" \
    --been-geojson "truck|vrachtwagen Novonix Riverside → De Soto-routeerpunt (I-24 → I-57 → I-64 → I-70 → I-435 → K-10; aannemelijk: één bron; volume nul tot H2 2027)|$BEEN/grafiet-lakecharles-desoto-weg-riverside-desoto.geojson" \
    --marker "Phillips 66 Lake Charles Manufacturing Complex — cokesveld/coker|30.24200,-93.27700" \
    --marker "Novonix Riverside — fabriek (Chattanooga, grafitisatie)|35.03880,-85.32430" \
    --marker "Panasonic Energy Kansas — De Soto (fase D, aannemelijk: één bron; volume nul)|38.93815,-95.00240" \
    --routebrief v2/design/routebrieven/grafiet-lakecharles-desoto.md \
    --uit    v2/data/stroomroute-grafiet-lakecharles-desoto.json \
    --stroom grafiet-lakecharles-desoto \
    --titel  "Grafiet · Lake Charles → Chattanooga → De Soto (VS)"
}

# ── lithium · Bikita (Zimbabwe) → Beira → Zhangjiagang (China) — spodumeenconcentraat/petaliet
# Routebrief: v2/design/routebrieven/lithium-bikita-zhangjiagang.md (LICHTE werkwijze M29)
# ⚠️ HAVENTERREIN BEIRA NIET IN HET NET (gemeten 2026-09-26): Cornelder's
#    havenstraten (`service`, geen access-tag) vormen in OSM een eigen, van
#    het doorgaande net LOSSTAAND clustertje (component van 2 knopen binnen
#    0,25 km van de kade) — precies de "haventerrein Beira alleen als OSM de
#    havenstraten mist"-uitzondering die de brief al noemt. Het truckbeen
#    (profiel lithium-bikita-zhangjiagang-bkplant-beira) eindigt daarom op de
#    laatste VERBONDEN knoop, de N6-havenweg-inrit bij Av. Samora Machel
#    (1,82 km van de kade — vrijwel exact de "1,8 km" die de brief bij
#    via-punt 8 zelf al noemt); de laatste 1,82 km is een stippel "eigen
#    terrein".
# ⚠️ ZEEBEEN "AANNEMELIJK: ÉÉN BRON" (SunSirs noemt Tianjin/Zhangjiagang als
#    aankomsthavens van de Bikita-ladingen) — de aanname staat in de
#    beennaam, niet in de lijnstijl (werkwijze §7); zeeknoop 7,8 km van de
#    kade, dus geen haven-aanloop nodig.
# ⚠️ b3/b4/b5 ZIJN EEN LETTERLIJKE KOPIE VAN bak_lithium (Greenbushes→
#    Zhangjiagang): dezelfde overgang zeenet→Yangtze-bulklaag, hetzelfde
#    Yangtze-rivierbeen (gedeeld bestand, geen tweede versie) en dezelfde
#    aanloop-stippel naar de kade (anker ≠ routeerpunt) — brief §2 b3-b5.
bak_lithium_bikita_zhangjiagang() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Bikita-plant → N6-havenweg-inrit Beira (A9/P4 Mutare-Masvingo Highway → Forbes/Machipanda-grens → N6/EN6 → Av. Samora Machel)|$BEEN/lithium-bikita-zhangjiagang-weg-bkplant-beira.geojson" \
    --stippel      "truck|haventerrein Beira (eigen terrein — OSM's havenstraten hangen niet aan het doorgaande net)|-19.823623,34.848737|-19.8150,34.8340" \
    --been         "zee|zeeschip Beira → Yangtze-monding (Mozambiquekanaal → Malakka → Zuid-Chinese Zee; bestemming aannemelijk: één bron)|-19.8150,34.8340|31.4074,121.4848" \
    --stippel      "zee|overgang zeenet → Yangtze-bulklaag (MARNET houdt hier op) — letterlijke kopie bak_lithium|31.51,121.4187|31.4512,121.4769" \
    --been-geojson "binnenvaart|Yangtze-monding → Zhangjiagang, zuidgeul langs Shuangshan-eiland — letterlijke kopie bak_lithium|$BEEN/rivierbeen-yangtze-zhangjiagang.geojson" \
    --stippel      "binnenvaart|aanloop naar de ligplaats (anker ≠ routeerpunt) — letterlijke kopie bak_lithium|31.9733,120.4202|31.968,120.4205" \
    --marker "Bikita Minerals — concentratorplant (Sinomine)|-19.9512,31.4245" \
    --marker "Forbes Border Post (ZW) / Machipanda (MZ), N6|-19.0052,32.7123" \
    --marker "Beira — general-cargo-terminal (Cornelder de Moçambique)|-19.8150,34.8340" \
    --marker "Yangtze-monding — overgang zee → rivier|31.42704,121.47618" \
    --marker "Zhangjiagang — kade Zhangjiagang Port Group (ertsen/hout/staal)|31.96800,120.42050" \
    --routebrief v2/design/routebrieven/lithium-bikita-zhangjiagang.md \
    --uit    v2/data/stroomroute-lithium-bikita-zhangjiagang.json \
    --stroom lithium-bikita-zhangjiagang \
    --titel  "Lithium · Bikita → Beira → Zhangjiagang (Zimbabwe → China)"
}

# ── grafiet · Balama (Mozambique) → Nacala → Saemangeum (Zuid-Korea) — vlokgrafiet → SPG → AAM
# Routebrief: v2/design/routebrieven/grafiet-balama-saemangeum.md (LICHTE werkwijze M29)
# ⚠️ b1 IS EEN LETTERLIJKE KOPIE VAN been 1 `grafiet-balama-vs` (497,9 km,
#    hergebruikte satelliet-gelegde ankers gr-balama-mill/gr-nacala-kade) —
#    géén nieuwe bake, geen tweede versie.
# ⚠️ TWEE HAVEN-AANLOPEN: Nacala snapt op 122,3 km van het zeenet (hergebruik
#    van de bestaande `aanloop-nacala.geojson`, dezelfde als bak_grafiet) en
#    Gunsan op 10,7-11,0 km (5643/5638) — een nieuwe korte aanloop gebakken
#    (`maak_havenaanloop.py`, 11,5 km over water, 0,00 km over land). Beide
#    blijven gestippeld (nog geen waargenomen vaargeul).
# ⚠️ b2/b3/b4 DRAGEN "VOLUME NUL" IN DE NAAM: geen bron bevestigt dat er in
#    2025/2026 al Balama-vlok in Zuid-Korea is aangekomen (brief §7). Dat
#    verschil hoort in de naam en de brief, NIET in de lijnstijl — alle drie
#    zijn DOORGETROKKEN.
# ⚠️ HET GUNSAN-ANKER EN HET SAEMANGEUM-FABRIEKSANKER ZIJN AANNEMELIJK RESP.
#    ONZEKER (brief §3): geen bron noemt de loshaven met naam, en blok 6 van
#    het Saemangeum-industriecomplex was op de satellietopname nog niet van
#    de buurpercelen te onderscheiden (bouw begon begin 2026). Doorgetrokken
#    geometrie, onzekere status blijft in de brief staan.
bak_grafiet_balama_saemangeum() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Balama-plant → Nacala-containerterminal (N380/N1) — LETTERLIJKE KOPIE been 1 grafiet-balama-vs|$BEEN/stroombeen-balama-nacala.geojson" \
    --stippel-geojson "zee|haven-aanloop Nacala (schematisch, over water — MARNET reikt hier niet, 152,1 km — hergebruik uit bak_grafiet)|$BEEN/aanloop-nacala.geojson" \
    --been         "zee|zeeschip Nacala → Gunsan New Port (Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee → Gele Zee; haven aannemelijk, geen bron noemt de losplek met naam; volume nul: leveringen aan POSCO niet gepubliceerd)|-15.0,41.7|35.9991,126.6991" \
    --stippel-geojson "zee|haven-aanloop Gunsan New Port (schematisch, over water — MARNET reikt niet tot de kade)|$BEEN/grafiet-balama-saemangeum-aanloop-gunsan.geojson" \
    --been-geojson "truck|vrachtwagen Gunsan New Port → Future Graph Saemangeum (Osikdo-dong-industrieterrein; plant-anker onzeker)|$BEEN/grafiet-balama-saemangeum-weg-gunsan-saemangeum.geojson" \
    --been-geojson "truck|vrachtwagen Future Graph Saemangeum → POSCO Future M Sejong (Route 21 → Seohaean Expwy 15 → Iksan JC → Nonsan JC → Expwy 25; volume nul: leveringen aan POSCO niet gepubliceerd)|$BEEN/grafiet-balama-saemangeum-weg-saemangeum-sejong.geojson" \
    --marker "Balama-plant (Syrah Resources), Mozambique|-13.31000,38.66000" \
    --marker "Nacala-containerterminal, oostoever|-14.53830,40.66730" \
    --marker "Gunsan (New) Port, Osikdo-dong (aannemelijk)|35.97700,126.58300" \
    --marker "Future Graph Saemangeum — POSCO Future M, blok 6 (onzeker)|35.96800,126.54800" \
    --marker "POSCO Future M — Sejong natuurlijk-grafiet-anodefabriek 1|36.70590,127.22030" \
    --routebrief v2/design/routebrieven/grafiet-balama-saemangeum.md \
    --uit    v2/data/stroomroute-grafiet-balama-saemangeum.json \
    --stroom grafiet-balama-saemangeum \
    --titel  "Grafiet · Balama → Nacala → Saemangeum (Zuid-Korea)"
}

# ── lithium · Bougouni (Kodal Minerals, Mali) → San Pedro (Ivoorkust) → Yangpu (Hainan, China)
# Routebrief: v2/design/routebrieven/lithium-bougouni-yangpu.md (LICHTE werkwijze M29)
# ⚠️ b1 (truck, Mali/Ivoorkust) IS +30,7% BOVEN DE GEPUBLICEERDE ~880 KM
#    (bevinding, niet dichtgetrokken — brief §7): het Ivoriaanse tracé is niet
#    gepubliceerd, alleen "één grensovergang, corridor via Sikasso"; de
#    via-keten gaf zelf al ~1.014 km hemelsbreed vóór het bakken.
# ⚠️ b2 (zee) — SAN PEDRO SNAPT BINNEN 1,58 KM (geen aanloop nodig, "been zee"
#    tekent zelf niet tot de kade, alleen tot de zeeknoop, maar 1,58 km blijft
#    onder de 5 km-naadnorm). YANGPU SNAPT OP 19,38 KM VAN DE DICHTSTBIJZIJNDE
#    ZEEKNOOP (< de 25 km --max-snap-afbreekgrens uit handleiding §2, maar wél
#    boven de 5 km-naadnorm van de toets) → CORRECTIE OP DE BRIEFSCHATTING VAN
#    ~25 km: de gemeten 19,38 km is kleiner, maar nog steeds een naad die een
#    aparte haven-aanloop vraagt (maak_havenaanloop.py, 20,4 km over water,
#    0 km landkruising, omwegfactor 1,054) van de zeeknoop naar de kade.
# ⚠️ b3 (truck, korte stippel-kandidaat) BLEEK GEEN STIPPEL NODIG: OSM heeft
#    wél een havenweg/estateweg tussen de twee onzekere ankers binnen de Yangpu
#    New Materials Industrial Park (9,4 km tegen een schatting van 5-10 km,
#    +17,5% — binnen de bandbreedte van de schatting zelf). Doorgetrokken, niet
#    gestippeld — "onzeker" staat in de ankernamen/marker, niet in de lijnstijl.
# ⚠️ BEIDE YANGPU-ANKERS ZIJN ONZEKER (brief §3): geen bron wijst een
#    specifieke berth of fabriekspoort aan; MEE-registerzoektocht (星之海/
#    兴之海) niet herhaald in deze bake (endpoint recent weer verhuisd).
bak_lithium_bougouni_yangpu() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Ngoualana-plant (Kodal Minerals) → San Pedro TIPSP (RN7 → grens Zégoua/Pogo → Ferkessédougou → Yamoussoukro → Soubré; +30,7% boven ~880 km, bevinding)|$BEEN/lithium-bougouni-yangpu-weg-plant-sanpedro.geojson" \
    --been         "zee|zeeschip San Pedro → Yangpu (Golf van Guinee → Kaap de Goede Hoop → Indische Oceaan → Straat Malakka → Zuid-Chinese Zee; San Pedro snapt binnen 1,58 km, geen aanloop nodig)|4.7490,-6.6180|19.8701,109.0009" \
    --stippel-geojson "zee|haven-aanloop Yangpu (schematisch, over water — MARNET-zeeknoop ligt 19,38 km van de kade, geen AIS-dekking op Hainan)|$BEEN/lithium-bougouni-yangpu-aanloop-yangpu.geojson" \
    --been-geojson "truck|vrachtwagen SDIC Yangpu-kade → Hainan Xingzhihai New Materials (havenweg/estateweg Yangpu New Materials Industrial Park; beide ankers onzeker)|$BEEN/lithium-bougouni-yangpu-weg-yangpu-xingzhihai.geojson" \
    --marker "Ngoualana open pit + Stage 1 DMS-plant (Kodal Minerals), Kola, Cercle de Bougouni|11.3413,-7.4886" \
    --marker "TIPSP San Pedro — bulkstockpile (Port Autonome de San Pedro)|4.7490,-6.6180" \
    --marker "SDIC Yangpu-havenzone — kade (onzeker)|19.7680,109.1510" \
    --marker "Hainan Xingzhihai New Materials — Yangpu New Materials Industrial Park (onzeker)|19.7180,109.1570" \
    --routebrief v2/design/routebrieven/lithium-bougouni-yangpu.md \
    --uit    v2/data/stroomroute-lithium-bougouni-yangpu.json \
    --stroom lithium-bougouni-yangpu \
    --titel  "Lithium · Bougouni (Mali) → San Pedro (Ivoorkust) → Yangpu (China)"
}

# ── lithium · Olaroz (Salar de Olaroz, Argentinië) → Buenos Aires → Onahama (Japan) → Naraha (Toyotsu Lithium)
# Routebrief: v2/design/routebrieven/lithium-olaroz-naraha.md (LICHTE werkwijze M29)
# ⚠️ b1 (truck, Argentinië) IS +19,6% BOVEN DE HEMELSBREED-SOM VAN DE VIA-PUNTEN
#    (~1.562 km — GEEN gepubliceerde weg-km, brief §7/§2), maar +6,7% t.o.v. de
#    ontwerpschatting uit de brief (~1.750 km) — bevinding, niet dichtgetrokken.
#    RN52 vlak bij Olaroz-plant loopt over `service`/`track`-mijnwegen op de
#    salarwerken (~3.900-4.200 m); zonder een corridor-brede `residential` én
#    een verruimde `eindKlassen` (mét `track`) meldde de scan "geen wegpad" —
#    zie het profiel in maak_stroombeen_weg.py. Anker-verbinding plant → weg
#    0,83 km (> 0,5 km, bevinding).
# ⚠️ b2 (zee) — BEIDE KADES LIGGEN TE VER VAN EEN ZEEKNOOP VOOR EEN DIRECT
#    "--been": Buenos Aires TRP snapt op 30,5 km, Onahama-kade op 44,9 km
#    (marnet_zee-snippet, bak-handleiding §2). Twee `maak_havenaanloop.py`-
#    aanlopen (32,3 km / 45,5 km, allebei geen landkruising) overbruggen dat;
#    het zeebeen zelf loopt tussen de twee ZEEKNOPEN en laat MARNET de
#    Kaap- of Panama-route kiezen (geen zeestraat op de heenweg, brief §2).
#    ⚠️ DE ONAHAMA-AANLOOP IS IN AANKOMSTRICHTING GEGENEREERD (zeeknoop → kade,
#    `--van`/`--naar` omgedraaid t.o.v. de kade→zeeknoop-vertrekconventie):
#    `--been-geojson`/`--stippel-geojson` tekenen de punten LETTERLIJK in
#    bestandsvolgorde (geen automatische omkering in hecht_marnet.py), dus de
#    reisvolgorde moet al in het bestand zitten.
# ⚠️ b3 (truck, Japan) IS +28,0% BOVEN DE GEPUBLICEERDE ~35 KM (Toyotsu
#    Onahama-havenseminar, brief bron [3]) — bevinding, niet dichtgetrokken:
#    geen tussenliggend via-punt (brief §7, geen corridorkeuze), dus de
#    gemeten 44,8 km is de kortste weg tussen de twee ankers over het net.
# ⚠️ NARAHA STAAT SINDS MEDIO 2025 OP CARE AND MAINTENANCE (brief §1/§5/[1][5])
#    — de weg is echt gevaren tot 2025, de lading ligt nu stil. Doorgetrokken,
#    niet gestippeld (werkwijze §7, zelfde behandeling als grafiet
#    Balama→Vidalia): het volume-nul hoort in de tekst, niet in de lijnstijl.
# ⚠️ FASE D VERVALT (brief §6): Toyotsu Lithium Naraha is zelf de conversieknoop
#    (carbonaat → hydroxide) en het stoppunt van deze brief.
bak_lithium_olaroz_naraha() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Olaroz-plant → Buenos Aires containerkade (RN52 → RN9 → RN34/RN9-splitsing → Rosario; +19,6% boven de hemelsbreed-som, geen gepubliceerde weg-km)|$BEEN/lithium-olaroz-naraha-weg-olaroz-baires.geojson" \
    --stippel-geojson "zee|haven-aanloop Buenos Aires TRP (schematisch, over water — MARNET reikt hier niet: 30,5 km)|$BEEN/lithium-olaroz-naraha-aanloop-baires.geojson" \
    --been         "zee|zeeschip Buenos Aires-zeeknoop → Onahama-zeeknoop (Atlantische Oceaan, geen zeestraat op de heenweg — MARNET beslist Kaap- of Panama-route)|-34.32530,-58.47060|36.90680,141.37350" \
    --stippel-geojson "zee|haven-aanloop Onahama, aankomstrichting (schematisch, over water — MARNET reikt hier niet: 44,9 km)|$BEEN/lithium-olaroz-naraha-aanloop-onahama-aankomst.geojson" \
    --been-geojson "truck|vrachtwagen Onahama-kade → Toyotsu Lithium Naraha (Jōban-snelweg/Route 6, geen corridorkeuze; +28,0% boven de gepubliceerde ~35 km)|$BEEN/lithium-olaroz-naraha-weg-onahama-naraha.geojson" \
    --marker "Sales de Jujuy — Olaroz-plant, Salar de Olaroz (~3.900 m)|-23.4629,-66.7025" \
    --marker "Buenos Aires — TRP, Terminales Río de la Plata (Puerto Nuevo)|-34.5847,-58.3631" \
    --marker "Onahama — Ōken-ふ頭 containerterminal (Iwaki, Fukushima)|36.9245,140.8695" \
    --marker "Toyotsu Lithium Naraha — hydroxidefabriek (care and maintenance, stoppunt)|37.2467,140.9954" \
    --routebrief v2/design/routebrieven/lithium-olaroz-naraha.md \
    --uit    v2/data/stroomroute-lithium-olaroz-naraha.json \
    --stroom lithium-olaroz-naraha \
    --titel  "Lithium · Olaroz (Argentinië) → Buenos Aires → Onahama → Naraha (Japan)"
}

# ── lithium · Pilgangoora (PLS) → Port Hedland/Utah Point → Gwangyang/Yulchon
#    (P-PLS-hydroxidefabriek → POSCO Future M-kathodefabriek, aannemelijk)
# Routebrief: v2/design/routebrieven/lithium-pilgangoora-gwangyang.md (LICHTE werkwijze M29)
# ⚠️ b1 IS TWEE WEGPROFIELEN MET EEN KORTE STIPPEL ERTUSSEN — GEMETEN OSM-
#    GRAAFGAT, GEEN WEGKLASSE-FOUT. De Great Northern Highway bij South
#    Hedland bestaat in OSM als twee componenten die geen knoop delen: het
#    doorgaande GNH-net (naar Marble Bar Rd/de mijn) en het stadsnet van Port
#    Hedland (Wilson St, Utah Road, de haven). Kleinste gemeten afstand tussen
#    beide componenten: 0,355 km — te klein om als "geen net op deze korrel"
#    weg te schrijven, groot genoeg om niet dicht te trekken. Zie de kop van
#    het profiel in maak_stroombeen_weg.py voor de meting.
# ⚠️ b2 (zee) heeft AAN BEIDE KANTEN een aanloop: de Port Hedland-zeeknoop ligt
#    79,7 km uit de kust (AU-binnenkant heeft geen MARNET-graaf) en de
#    Gwangyang-zeeknoop 29,7 km van Yulchon (op de grens van --max-snap 25 km)
#    — beide gehaald met maak_havenaanloop.py, geen terugval nodig.
# ⚠️ b3/b4 zijn allebei "eigen terrein"-stippels (§7): b3 kade → P-PLS-fabriek
#    (~1,3 km, geen net op deze korrel) en b4 P-PLS → POSCO Future M-
#    kathodefabriek (<1 km, "aannemelijk: één bron" — beide fabrieken op
#    hetzelfde Yulchon-complex, opeenvolgende straatadressen, geen bron geeft
#    het overgedragen volume). Fase D/E-onderscheid staat in de beennaam, niet
#    in de lijnstijl.
bak_lithium_pilgangoora_gwangyang() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|road train Pilgan-plant → GNH bij South Hedland (mijnweg → Marble Bar Rd → Great Northern Hwy)|$BEEN/lithium-pilgangoora-gwangyang-weg-plant-southhedland.geojson" \
    --stippel      "truck|OSM-graafgat in de Great Northern Highway bij South Hedland (twee GNH-componenten delen geen knoop, 0,355 km — geen net op deze korrel)|-20.377913,118.575136|-20.374731,118.574874" \
    --been-geojson "truck|road train GNH-stadsnet Port Hedland → Utah Point (Great Northern Hwy → Utah Road)|$BEEN/lithium-pilgangoora-gwangyang-weg-southhedland-utahpoint.geojson" \
    --stippel-geojson "zee|haven-aanloop Utah Point Bulk Handling Facility (schematisch, over water — MARNET reikt hier niet: 79,7 km)|$BEEN/lithium-pilgangoora-gwangyang-aanloop-utahpoint.geojson" \
    --been         "zee|zeeschip Utah Point → Yulchon/Gwangyang (bulkcarrier; Lombok/Makassar–Zuid-Chinese Zee–Taiwanstraat–Oost-Chinese Zee, MARNET beslist)|-19.60000,118.60000|34.71000,127.82040" \
    --stippel-geojson "zee|haven-aanloop Yulchon/Gwangyang, aankomstrichting (schematisch, over water — MARNET reikt hier niet: 29,7 km; kade-anker onzeker)|$BEEN/lithium-pilgangoora-gwangyang-aanloop-yulchon.geojson" \
    --stippel      "truck|havenweg Yulchon-kade → P-PLS-hydroxidefabriek (eigen terrein — geen net op deze korrel, ~1,3 km)|34.9075,127.6020|34.9008,127.5911" \
    --stippel      "truck|P-PLS → POSCO Future M-kathodefabriek (aannemelijk: één bron — eigen terrein, hetzelfde Yulchon-complex)|34.9008,127.5911|34.8985,127.5885" \
    --marker "Pilgan-plant, Pilgangoora Operation (PLS)|-21.0595,118.8956" \
    --marker "Utah Point Bulk Handling Facility, Port Hedland (Berth 4)|-20.3153,118.5585" \
    --marker "Yulchon-havenfront, Gwangyang (losplek onzeker)|34.9075,127.6020" \
    --marker "POSCO Pilbara Lithium Solution (P-PLS), Yulchon-industriecomplex|34.9008,127.5911" \
    --marker "POSCO Future M — kathodefabriek, Yulchon-industriecomplex (aannemelijk)|34.8985,127.5885" \
    --routebrief v2/design/routebrieven/lithium-pilgangoora-gwangyang.md \
    --uit    v2/data/stroomroute-lithium-pilgangoora-gwangyang.json \
    --stroom lithium-pilgangoora-gwangyang \
    --titel  "Lithium · Pilgangoora (Australië) → Port Hedland → Gwangyang (Zuid-Korea)"
}

# ── kobalt · Kolwezi-spoorstation → Kamoa-railhead → Lobito (Benguela-lijn)
# Routebrief: v2/design/routebrieven/kobalt-kolwezi-lobito.md (LICHTE werkwijze M29)
# ⚠️ b1 is NIEUW en op het 1-op-1-spoornet gescand (BAKE_SUFFIX=-raw,
#    "3260717 spoor-edges" bevestigd): 29,4 km over 36 edges tegen 22,2 km
#    hemelsbreed (verhouding 1,32) — één omkering vlak bij het beginpunt
#    (156,6°, boogstraal ~100 m) is kopmaken op het emplacement, geen fout.
# ⚠️ b2 EN de aanloop-stippel van b3 zijn LETTERLIJKE KOPIEËN van
#    bak_koper_lobito (koper-lobito-duisburg) — géén tweede scan/aanloop-
#    poging. b3 is daar zelf al een RECHTE --stippel (geen geojson-bestand),
#    dus die vorm is hier exact overgenomen, niet een stippel-geojson die niet
#    bestaat.
# ⚠️ GEEN b4 (zee naar een bestemmingshaven): geen bron noemt de koper/haven
#    van het kobalt na Lobito (brief §6/§7). De brief stopt bewust bij de
#    haven-nadering.
# ⚠️ co-kolwezi-laad is de CFB-spoorstation-fallback, status onzeker (brief
#    §3/§7): de echte EGC/LAR-laadlus in Kolwezi is nergens bij naam of
#    coördinaat gedocumenteerd.
bak_kobalt_kolwezi_lobito() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|Kolwezi-spoorstation → Kamoa-railhead (nieuw stuk, 1-op-1-net)|$BEEN/spoorroute-kobalt-kolwezi-lobito-kolwezi-railhead.geojson" \
    --been-geojson "spoor|trein Kamoa-Kakula → Lobito (Benguela-lijn, gedeeld met koper-lobito-duisburg)|v2/build-cache/ais/graaf/spoorroute-kamoa-lobito.geojson" \
    --stippel      "zee|haven-aanloop Lobito (schematisch, over water — MARNET reikt niet; ligplaats niet vastgesteld; gedeeld met koper-lobito-duisburg)|-12.34709,13.549|-12.2702,13.5406" \
    --marker "Kolwezi-spoorstation — Gare de Kolwezi/CFB-emplacement (laadplek, onzeker)|-10.71495,25.48365" \
    --marker "Kamoa-railhead — kop van spoorroute-kamoa-lobito.geojson (gedeeld anker)|-10.6627,25.2873" \
    --marker "Dilolo — Congolees grensstation (Benguela-lijn)|-10.69886,22.34423" \
    --marker "Luau — Angolees grensstation, start Benguela-kilometrering|-10.70491,22.22639" \
    --marker "Lobito — mineralenterminal (ligplaats open, gedeeld anker)|-12.34709,13.549" \
    --routebrief v2/design/routebrieven/kobalt-kolwezi-lobito.md \
    --uit    v2/data/stroomroute-kobalt-kolwezi-lobito.json \
    --stroom kobalt-kolwezi-lobito \
    --titel  "Kobalt · Kolwezi → Kamoa-railhead → Lobito (Benguela-lijn)"
}

# ── nikkel · Sudbury Smelter (Falconbridge) → Québec (CN-spoor) → Kristiansand/Nikkelverk (zee)
# Routebrief: v2/design/routebrieven/nikkel-sudbury-kristiansand.md (LICHTE werkwijze M29)
# ⚠️ b0 is een KORT emplacementsstuk (spoor reikt niet tot de smelterdeur):
#    gemeten snapgat 0,16 km (BAKE_SUFFIX=-raw, hoofdnet-knoop) — veel korter
#    dan de haalbaarheidsschatting van 2,22 km; de échte meting wint.
# ⚠️ b1 is DRIE RUNS op het 1-op-1-spoornet (BAKE_SUFFIX=-raw, "3260717
#    spoor-edges" bevestigd), via MacMillan Yard en Taschereau Yard:
#    463,9 + 535,5 + 283,8 = 1.283,2 km tegen de brief se ~1.230 km (+4,3%,
#    binnen ±15%). Eén 180°-omkering blijft staan bij 43,6673/-79,4652
#    (boogstraal ~36 m, in run 1): getest met vier alternatieve via-vertices
#    in en rond de MacMillan-yardcluster (0,00–2,26 km van het opgegeven
#    punt) én met keerstraf 150 — de omkering verandert niet van plek of
#    verdwijnt niet. De yardcluster is een lokaal subnet (~1,4 km) dat pas op
#    ≥29,9 km weer aansluit op het grote net, dus de omkering zit in de
#    brongeometrie zelf, niet in het gekozen via-punt. Bevinding, niet
#    dichtgetrokken (werkwijze §5: buiten de norm = bevinding).
# ⚠️ `ni-quebec-kade` is AANNEMELIJK (brief §3/§7: Glencore noemt geen kade/
#    sector in secteur Beauport); b2 heeft geen haven-aanloop nodig — beide
#    kades snappen <25 km van een zeeknoop (Québec 0,6 km, Kristiansand
#    6,2 km).
# ⚠️ Geen fase D: de brief stopt bewust bij Nikkelverk (§6) — geen bron
#    koppelt een Nikkelverk-zending aan een specifiek LME-entrepot.
bak_nikkel_sudbury_kristiansand() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "spoor|Falconbridge-emplacement → spoornet (schematisch — net reikt niet tot de smelterdeur, gemeten 0,16 km)|46.5786,-80.7993|46.5787,-80.7972" \
    --been-geojson "spoor|trein Sudbury-emplacement → MacMillan Yard (CN Bala Sub, via Barrie)|$BEEN/spoorroute-nikkel-sudbury-kristiansand-sudbury-macmillan.geojson" \
    --been-geojson "spoor|trein MacMillan Yard → Taschereau Yard (CN Kingston Sub, via Toronto-Montréal)|$BEEN/spoorroute-nikkel-sudbury-kristiansand-macmillan-taschereau.geojson" \
    --been-geojson "spoor|trein Taschereau Yard → Glencore-terminal Port of Québec (CN Kingston Sub, secteur Beauport aannemelijk)|$BEEN/spoorroute-nikkel-sudbury-kristiansand-taschereau-quebec.geojson" \
    --been         "zee|zeeschip Québec → Kristiansand (Saint-Laurent-benedenloop → Cabotstraat → Noord-Atlantische Oceaan → Skagerrak)|46.8330,-71.2035|58.1388,7.9713" \
    --marker "Glencore Sudbury Smelter (Falconbridge) — kop van het spoor|46.5786,-80.7993" \
    --marker "MacMillan Yard (CN, Vaughan/Toronto-noord) — via-punt corridorkeuze|43.8119,-79.5111" \
    --marker "Taschereau Yard (CN, Saint-Laurent/Montréal) — via-punt corridorkeuze|45.4686,-73.6861" \
    --marker "Glencore-terminal, Port of Québec, secteur Beauport (aannemelijk)|46.8330,-71.2035" \
    --marker "Nikkelverk (Glencore), Kolsdalen, Kristiansand — losplek + raffinaderij, stoppunt|58.1388,7.9713" \
    --routebrief v2/design/routebrieven/nikkel-sudbury-kristiansand.md \
    --uit    v2/data/stroomroute-nikkel-sudbury-kristiansand.json \
    --stroom nikkel-sudbury-kristiansand \
    --titel  "Nikkel · Sudbury → Québec → Kristiansand (Noorwegen)"
}

# ── nikkel · Norilsk (Nadezhda) → Dudinka → Jenisej → Moermansk (Arc7) → Monchegorsk (Severonickel)
# Routebrief: v2/design/routebrieven/nikkel-norilsk-monchegorsk.md (LICHTE werkwijze M29)
# ⚠️ b1 spoor (1-op-1-net, BAKE_SUFFIX=-raw): 77,7 km — EXACT de gepubliceerde
#    77,7 km uit de brief (rusland-siberie, geïsoleerd Norilsk-industrienet).
# ⚠️ b2 binnenvaart (bulklaag): 429,8 km — EXACT de gepubliceerde 429,8 km.
#    Beennaam noemt de clausule "bulklaag: ligging van het water, geen
#    bevaarbaarheidsbewijs" (brief §2, Nornickel Arc7-vloot).
# ⚠️ b2b IS EEN STIPPEL: de naad tussen de dichtstbijzijnde bulk-knoop
#    (71,82880/82,77830) en MARNET-zeeknoop 2338 (71.9829,82.4669) is
#    20,23 km — gemeten, boven de 5 km-norm, dus niet dichtgetrokken.
# ⚠️ b3 zee laat MARNET zelf via Karskiye Vorota routeren (geen via-punt
#    afgedwongen) — jaarrond Arc7-ijsbrekervloot, `northwest`-passage blijft
#    dicht (default), dus geen Noordwest-Passage-sluipweg.
# ⚠️ b4 spoor (rusland-noordwest): 145,1 km tegen gepubliceerd 142,1 km
#    (+2,1%, ruim binnen ±15%); 2 omkeringen vlak bij Moermansk-terminal
#    (178,0°/165,7°, boogstralen 27-57 m) = kopmaken op het emplacement,
#    geen fout — komt overeen met de "1 spike" uit de brief.
# ⚠️ GEEN b4b-stippel: de brief verwachtte een los terreinspoor-stukje
#    (~3 km, "geen net op deze korrel"), maar de gemeten snap bij Severonickel
#    is 0,23 km — het net reikt hier al tot het anker. Bevinding, niet
#    dichtgetrokken (§9).
# ⚠️ GEEN b5 (Harjavalta-vertakking, Finland): optioneel volgens de brief
#    ("alleen tekenen als er tijd voor is, anders weglaten") — in deze bake
#    weggelaten; blijft open punt.
# ⚠️ `ni-moermansk-terminal` is AANNEMELIJK (brief §3/§7: adres via
#    bedrijvenregister, geen Nornickel-specifiek kenmerk op het satellietbeeld
#    te onderscheiden van het naastgelegen scheepsreparatiebedrijf).
bak_nikkel_norilsk_monchegorsk() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Nadezhda-fabriek → Kajerkan → Dudinka-kade (geïsoleerd Norilsk-industrienet, 1-op-1-net)|$BEEN/spoorroute-nikkel-norilsk-monchegorsk-nadezhda-dudinka.geojson" \
    --been-geojson "binnenvaart|Jenisej stroomafwaarts Dudinka-kade → bulk-knoop bij zeeknoop 2338 (bulklaag: ligging van het water, geen bevaarbaarheidsbewijs; Nornickel Arc7-vloot)|$BEEN/nikkel-norilsk-monchegorsk-rivier-dudinka-bulkknoop.geojson" \
    --stippel      "zee|haven-aanloop Jenisej-golf (schematisch, naad rivier↔MARNET, 20,2 km > 5 km-norm)|71.82880,82.77830|71.9829,82.4669" \
    --been         "zee|zeeschip (Arc7-ijsbreker, jaarrond) Jenisej-golf → Moermansk (Karazee → Karskiye Vorota → Barentszzee)|71.9829,82.4669|68.9737,33.0658" \
    --been-geojson "spoor|trein Moermansk-terminal → Kola → Olenegorsk → Monchegorsk (Oktoberspoorweg, 1-op-1-net)|$BEEN/spoorroute-nikkel-norilsk-monchegorsk-moermansk-severonickel.geojson" \
    --marker "Nadezhda Metallurgical Plant, Norilsk (Nornickel Polar Division) — kop spoor|69.3275,87.9521" \
    --marker "Dudinka-havenkade, Jenisej — overslag spoor→binnenvaart|69.4030,86.1680" \
    --marker "Jenisej-golf — bulk-knoop (naad-eindpunt rivierbeen)|71.82880,82.77830" \
    --marker "Jenisej-golf — MARNET-zeeknoop 2338 (naad-eindpunt zeebeen)|71.9829,82.4669" \
    --marker "Nornickel Murmansk Transport Division, Портовый проезд 31/1 — overslag zee→spoor (aannemelijk)|68.9737,33.0658" \
    --marker "Severonickel-fabriek (Kola MMC), Monchegorsk — losplek/raffinaderij, stoppunt|67.9195,32.8320" \
    --routebrief v2/design/routebrieven/nikkel-norilsk-monchegorsk.md \
    --uit    v2/data/stroomroute-nikkel-norilsk-monchegorsk.json \
    --stroom nikkel-norilsk-monchegorsk \
    --titel  "Nikkel · Norilsk → Dudinka → Moermansk → Monchegorsk (Rusland)"
}

# ── kobalt · TFM (Fungurume) → Kasumbalesa → Durban → Ningbo (hydroxide, stopt bij de containerkade)
# Routebrief: v2/design/routebrieven/kobalt-tfm-quzhou.md (lichte werkwijze M29, LAR-563)
# ⚠️ b1 EN de Durban-aanloopstippel zijn LETTERLIJKE KOPIEËN van bak_koper_durban
#    (koper-tfm-durban): zelfde truck, zelfde Copperbelt-zuidroute
#    (RN39/RN1 → Kasumbalesa → T3/T2 → Chirundu → A1/A4 → Beitbridge → N1/N3,
#    2.982 km) — géén tweede wegscan, géén tweede aanloop-poging.
# ⚠️ b2 (zee Durban → Ningbo) is NIEUW over MARNET: de afnemer Huayou Quzhou
#    is een SAMENVLOEIING, aannemelijk — CMOC verkoopt via handelaar IXM, geen
#    bron koppelt dit hydroxide aan Quzhou specifiek (brief §6/§7).
# ⚠️ b2a (haven-aanloop Ningbo) is NIEUW: maak_havenaanloop.py vond een pad
#    over water, 11,6 km / 5 punten / 0,00 km over land — geen terugval nodig.
# ⚠️ GEEN been C (Ningbo → Huayou Quzhou, ~300 km truck): geen bron toont dat
#    dit specifieke hydroxide bij Quzhou aankomt (Huayou's eigen due-diligence-
#    rapport, de enige kandidaat, gaf een 403). De lijn stopt op de Ningbo-kade;
#    Huayou Quzhou blijft een ongeplaatste knoop (§5/§7, coördinaat niet
#    gevonden — niet verzonnen, dus ook geen marker).
bak_kobalt_tfm_quzhou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|kobalthydroxide TFM-plant → Durban DCT Pier 2 (Copperbelt-zuidroute, letterlijke kopie van koper-tfm-durban)|$BEEN/stroombeen-tfm-durban.geojson" \
    --stippel-geojson "zee|haven-aanloop Durban (schematisch, over water — MARNET reikt niet; letterlijke kopie van koper-tfm-durban)|$BEEN/aanloop-durban.geojson" \
    --been         "zee|zeeschip Durban → Ningbo (kobalthydroxide; afnemer Huayou Quzhou: samenvloeiing, aannemelijk)|-29.8168,31.1737|29.9758,121.9736" \
    --stippel-geojson "zee|haven-aanloop Ningbo Beilun (schematisch, over water — MARNET reikt niet tot de containerkade)|$BEEN/kobalt-tfm-quzhou-aanloop-ningbo.geojson" \
    --marker "TFM hydrometallurgische plant (CMOC/Gécamines), Kwatebala, Fungurume — laadplek (hergebruikt anker)|-10.5685,26.1975" \
    --marker "Durban — DCT Pier 2, noordkade (overslag truck → container → zeeschip, hergebruikt anker)|-29.8790,31.0160" \
    --marker "Ningbo Beilun Container Terminal Phase 2 — overslag zeeschip → onbekend vervolg (stoppunt)|29.9353,121.8695" \
    --routebrief v2/design/routebrieven/kobalt-tfm-quzhou.md \
    --uit    v2/data/stroomroute-kobalt-tfm-quzhou.json \
    --stroom kobalt-tfm-quzhou \
    --titel  "Kobalt · TFM (Fungurume) → Durban → Ningbo (hydroxide)"
}

# ── nikkel · Weda Bay-put → IWIP-ore-yard (eigen mijnweg, Indonesië)
# Routebrief: v2/design/routebrieven/nikkel-wedabay-iwip.md (LICHTE werkwijze M29)
# ⚠️ EEN LANDBEEN, GEEN ZEEBEEN — export naar Chinese roestvrijstaal-mills is
#    nergens op fabrieksniveau gebrond (brief §6), dus de keten stopt op het
#    IWIP-ore-yard-anker. GEEN fase-C-been binnen het park: de RKEF-smeltrijen
#    en de haven liggen 3-5 km oostelijker op hetzelfde terrein maar krijgen
#    geen eigen anker (werkwijze §1, één anker per site).
# ⚠️ GEEN gepubliceerde lengte voor de mijnweg — 3,6 km hemelsbreed
#    (satellietmeting) is een losse controle, geen hard toetsdoel. Gemeten pad:
#    7,4 km (+104% t.o.v. de hemelsbrede meting) — verwacht door het reliëf,
#    blijft als bevinding staan (brief §9), niet dichtgetrokken.
# ⚠️ Beide uiteinden snappen ruim binnen 0,5 km op de weg (0,12 / 0,39 km) —
#    de scan vond een doorgaand pad over unclassified/tertiary/service, dus
#    GEEN stippel-knip bij de put nodig (anders dan vooraf verwacht in de
#    bak-aanwijzing van het onderzoek).
# ⚠️ ni-iwip-jetty is een MARKER-ALLEEN (haven/kolenopslag verderop op
#    hetzelfde terrein) — geen been ernaartoe (werkwijze: geen last-mile-been).
bak_nikkel_wedabay_iwip() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|lateriet-erts actieve dagbouw-put WBN → IWIP-ore-yard (eigen mijnweg, unclassified/tertiary/service)|$BEEN/nikkel-wedabay-iwip-weg-pit-rkef.geojson" \
    --marker "Actieve dagbouw-put, WBN-contractgebied, Halmahera Tengah — mijn/laadfront|0.4930,127.9350" \
    --marker "IWIP-terrein Lelilef — ore-yard/eerste industriecluster (RKEF Tsingshan + Huafei-HPAL Huayou), stoppunt|0.4970,127.9670" \
    --marker "IWIP-havenbekken binnen de golfbreker — jetty (marker, geen been)|0.4745,128.0055" \
    --routebrief v2/design/routebrieven/nikkel-wedabay-iwip.md \
    --uit    v2/data/stroomroute-nikkel-wedabay-iwip.json \
    --stroom nikkel-wedabay-iwip \
    --titel  "Nikkel · Weda Bay-put → IWIP-ore-yard (Indonesië)"
}

# ── kobalt · Morowali (Huayue MHP-plant) → Labota-jetty → Ningbo (stopt bij de containerkade)
# Routebrief: v2/design/routebrieven/kobalt-morowali-quzhou.md (lichte werkwijze M29)
# ⚠️ b1 is een STIPPEL zonder wegscan: parkinterne IMIP-weg, geen net op deze
#    korrel (brief b1, ~3,5 km hemelsbreed).
# ⚠️ b2 (haven-aanloop Labota) is NIEUW via maak_havenaanloop.py: 100,9 km,
#    exit 0 (0.39 km land-restant zit op de kade-korrel zelf, geen fout) — de
#    zwaarste haven-aanloop van de zes kobaltassen, +8,5% t.o.v. de brief se
#    ~93 km, binnen ±15%.
# ⚠️ b3 (zee Golf van Tolo → zeeknoop bij Ningbo) is de MARNET-router tussen
#    twee al bestaande zeeknopen (5491 uit de ontwerptoets, 5850 uit
#    kobalt-tfm-quzhou.md b2) — geen snap-berekening nodig, geen stippel.
# ⚠️ b4 (haven-aanloop Ningbo Beilun) is een LETTERLIJKE KOPIE van
#    kobalt-tfm-quzhou.md's b2a-geojson (co-ningbo-kade = exact hetzelfde
#    punt in beide stromen) — géén tweede aanloop-poging.
# ⚠️ GEEN been C (Ningbo → Huayou Quzhou): geen coördinaat voor de
#    vervolgfabriek gevonden deze sessie (brief §6/§7, gedeeld open punt met
#    kobalt-tfm-quzhou.md); Huayou Quzhou blijft een ongeplaatste knoop,
#    geen marker.
bak_kobalt_morowali_quzhou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|parkintern Huayue → Labota-jetty (binnen estate, geen net op deze korrel)|-2.8371,122.1658|-2.8606,122.1871" \
    --stippel-geojson "zee|haven-aanloop Labota (schematisch, over water — MARNET reikt hier niet: 93 km, zwaarste aanloop van de zes kobaltassen)|$BEEN/kobalt-morowali-quzhou-aanloop-labota.geojson" \
    --been         "zee|zeeschip Labota → Ningbo (MHP, 4-5% Co; Golf van Tolo → Banda-/Molukse Zee → Filipijnenzee/Zuid-Chinese Zee → Oost-Chinese Zee)|-2.0357,122.0017|29.9758,121.9736" \
    --stippel-geojson "zee|haven-aanloop Ningbo Beilun (schematisch, over water — MARNET reikt niet tot de containerkade; letterlijke kopie van kobalt-tfm-quzhou)|v2/build-cache/ais/graaf/kobalt-tfm-quzhou-aanloop-ningbo.geojson" \
    --marker "PT Huayue Nickel Cobalt, Morowali Industrial Park (IMIP), Sulawesi — HPAL-plant, laadplek (aannemelijk)|-2.8371,122.1658" \
    --marker "Labota-jetty, IMIP-havenzone — overslag parkweg → zee (bron-gelegd)|-2.8606,122.1871" \
    --marker "Ningbo Beilun Container Terminal Phase 2 — overslag zeeschip → onbekend vervolg (stoppunt, hergebruikt anker)|29.9353,121.8695" \
    --routebrief v2/design/routebrieven/kobalt-morowali-quzhou.md \
    --uit    v2/data/stroomroute-kobalt-morowali-quzhou.json \
    --stroom kobalt-morowali-quzhou \
    --titel  "Kobalt · Morowali (IMIP) → Labota-jetty → Ningbo (MHP)"
}

# ── kobalt · KCC Luilu (Kolwezi) → Durban → Kokkola (Umicore-raffinaderij, Finland)
# Routebrief: v2/design/routebrieven/kobalt-kcc-kokkola.md (LICHTE werkwijze M29)
# ⚠️ Been 1 (truck) is een NIEUW profiel `kobalt-kcc-durban` — niet dezelfde
#    bestandskopie als koper-tfm-durban (ander beginpunt: Luilu i.p.v. TFM
#    Fungurume), wel dezelfde 12 via-punten vanaf Likasi. RN39 Kolwezi→Likasi
#    kreeg `corridorKlassen: ["tertiary"]` (Oyu Tolgoi-precedent): zonder die
#    klasse snapte het nieuwe via-punt 8,05 km, mét 3,65 km.
# ⚠️ Kop-aanloop Durban = LETTERLIJKE KOPIE van `aanloop-durban.geojson` (17,8 km,
#    uit koper-kolwezi-durban) — geen nieuwe scan. Staart-aanloop Kokkola is wél
#    nieuw: de Kokkola-zeeknoop (8821, 64.0369,22.7535) ligt 23,4 km van de kade
#    (binnen --max-snap 25 maar dicht bij de grens en over de Kvarken-scherenkust)
#    → `maak_havenaanloop.py` gedraaid, geslaagd (25,4 km, 0,00 km over land).
# ⚠️ Laadhaven Durban is AANNEMELIJK (branche-default, Fastmarkets — Glencore
#    publiceert geen haven); dat staat in de beennaam, niet in de lijnstijl.
# ⚠️ Fase C (kade → Umicore-raffinaderij, <3 km) krijgt GEEN eigen been (lichte
#    werkwijze) — alleen de marker `co-kip-umicore`. Fase D (raffinaderij →
#    precursorlijn, zelfde terrein) wordt niet getekend, alleen genoemd in §5
#    van de brief (één bron).
bak_kobalt_kcc_kokkola() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|kobalthydroxide KCC Luilu-plant, Kolwezi → Durban DCT Pier 2 (RN39 → RN1 → T3/T2 → A1/A4 → N1/N3)|$BEEN/kobalt-kcc-kokkola-weg-kcc-durban.geojson" \
    --stippel-geojson "zee|haven-aanloop Durban (schematisch, over water — MARNET-knoop 16,7 km buiten de haven; letterlijke kopie van koper-kolwezi-durban)|$BEEN/aanloop-durban.geojson" \
    --been         "zee|zeeschip Durban DCT Pier 2 → Port of Kokkola (kobalthydroxide, om de Kaap · Skagerrak · Kattegat · Oostzee · Botnische Golf; laadhaven Durban aannemelijk: branche-default, Glencore publiceert geen haven)|-29.8790,31.0160|63.8645,23.0270" \
    --stippel-geojson "zee|haven-aanloop Kokkola (schematisch, over water — zeeknoop 8821 ligt 23,4 km van de kade, Kvarken-scherenkust)|$BEEN/kobalt-kcc-kokkola-aanloop-kokkola.geojson" \
    --marker "KCC (Glencore 75%) Luilu hydrometallurgische plant, Kolwezi|-10.7205,25.3620" \
    --marker "Durban Container Terminal Pier 2 (Bayhead) — hergebruikt anker|-29.8790,31.0160" \
    --marker "Kokkolan syväsatama (Deep Port), Port of Kokkola|63.8645,23.0270" \
    --marker "Umicore Finland Oy, Kokkola Industrial Park — raffinaderij + precursorlijn (fase D, onzeker perceel)|63.8580,23.0490" \
    --routebrief v2/design/routebrieven/kobalt-kcc-kokkola.md \
    --uit    v2/data/stroomroute-kobalt-kcc-kokkola.json \
    --stroom kobalt-kcc-kokkola \
    --titel  "Kobalt · KCC Kolwezi → Durban → Kokkola (Umicore)"
}

# ── nikkel · Ouaco-mijnplateau → Téoudié-laadkade → Gwangyang (SNNC) → Pohang (POSCO)
# Routebrief: v2/design/routebrieven/nikkel-ouaco-gwangyang.md (LICHTE werkwijze M29)
# ⚠️ b1 IS EEN VERWACHTE-MISLUKKING-POGING: het profiel
#    nikkel-ouaco-gwangyang-ouaco-teoudie (nieuw-caledonie-extract) geeft "geen
#    wegpad" — de Ouaco-mijnweg "Mines" is in OSM vrijwel volledig `track`, en
#    track komt de scanner nooit door (ook niet via corridorKlassen). Rechte
#    stippel met de reden in de naam, geen tweede poging.
# ⚠️ b2/b3 ZIJN VOLLEDIG STIPPEL, ZONDER BETROUWBAAR TUSSENANKER: de rede/
#    ankerplaats Téoudié heeft geen gepubliceerde coördinaat (brief §7); het
#    redepunt (-20.760,164.375) is een schatting ~2-3 km uit de kust op het rif.
# ⚠️ b3/b5 ZIJN HAVEN-AANLOPEN VAN maak_havenaanloop.py (getekend, blijven
#    stippel): Ouaco 98,2 km (rif, geen landkruising midden op de lijn) tegen
#    ~102 km in de brief; Gwangyang 25,5 km tegen ~22,1 km — allebei binnen het
#    schematische karakter van een aanloop, geen gemeten been.
# ⚠️ GEEN EIGEN BEEN VOOR KADE → SNNC-FABRIEK: beide liggen op hetzelfde
#    Gwangyang-industrieterrein (~2,4 km) — korte stippel-`truck` als
#    procesgat, geen lijn dwars door het complex (Tongling/Manyar-klasse).
# ⚠️ b7 (SNNC → Pohang) IS AANNEMELIJK: ÉÉN BRON NOEMT POHANG ALS AFNEMER, GEEN
#    ENKELE NOEMT DE ROUTE. Vrije Dijkstra over het zuid-korea-extract
#    (WEG_HOUD, motorway t/m secondary): 239,8 km tegen de kaart-schatting van
#    ~250 km (-4,1%), geen publicatie om hard tegen te toetsen.
bak_nikkel_ouaco_gwangyang() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|vrachtwagen Ouaco-mijnplateau → Téoudié-laadkade (privé mijnweg \"Mines\", geen net op deze korrel)|-20.7400,164.4750|-20.7566,164.3822" \
    --stippel      "zee|bakken Téoudié-laadkade → rede (geen kade voor zeeschepen; bakken 250-330 t achter sleepboten)|-20.7566,164.3822|-20.760,164.375" \
    --stippel-geojson "zee|haven-aanloop Ouaco (schematisch, over het barrièrerif — MARNET reikt niet tot de rede)|$BEEN/nikkel-ouaco-gwangyang-aanloop-ouaco.geojson" \
    --been         "zee|zeeschip Ouaco-aanloop → Gwangyang-aanloop (Koraalzee → Salomonszee/Bismarckzee → Filipijnenzee → Oost-Chinese Zee)|-20.9000,163.5000|34.7100,127.8204" \
    --stippel-geojson "zee|haven-aanloop Gwangyang (schematisch, over water — MARNET-zeeknoop ligt buiten de 25 km-snap van de kade)|$BEEN/nikkel-ouaco-gwangyang-aanloop-gwangyang.geojson" \
    --stippel      "truck|kade → SNNC-terrein (zelfde Gwangyang-industriehaven, procesgat)|34.9095,127.7280|34.9295,127.7360" \
    --been-geojson "truck|ferronikkel SNNC Gwangyang → POSCO-staalfabriek Pohang (aannemelijk: één bron, geen gedocumenteerde corridor)|$BEEN/nikkel-ouaco-gwangyang-weg-snnc-pohang.geojson" \
    --marker "NMC-mijnplateau Ouaco (Kaala-Gomen)|-20.7400,164.4750" \
    --marker "Téoudié-laadkade, Cotransmine (Kaala-Gomen, westkust)|-20.7566,164.3822" \
    --marker "SNNC ferronikkelfabriek, Gwangyang Industrial Complex|34.9295,127.7360" \
    --marker "Bulkkade, POSCO Gwangyang-industriehaven|34.9095,127.7280" \
    --marker "POSCO geïntegreerd staalcomplex Pohang|36.0180,129.3820" \
    --routebrief v2/design/routebrieven/nikkel-ouaco-gwangyang.md \
    --uit    v2/data/stroomroute-nikkel-ouaco-gwangyang.json \
    --stroom nikkel-ouaco-gwangyang \
    --titel  "Nikkel · Ouaco → Téoudié → Gwangyang (SNNC) → Pohang (POSCO)"
}

# ── nikkel · IMIP Morowali (Huayue) → Ningbo (Beilun, hergebruikt anker) → Quzhou (Huayou)
# Routebrief: v2/design/routebrieven/nikkel-morowali-quzhou.md (LICHTE werkwijze M29)
# ⚠️ b1 (zee): IMIP-jetty ligt 92,9 km van de dichtstbijzijnde MARNET-zeeknoop
#    (5491, -2.03570,122.00170) — geen aanloop-tweede-poging nodig, de eerste
#    trap (0,01° gebufferd) vond een schoon pad (95,6 km, 0% over land) →
#    `maak_havenaanloop.py` als STIPPEL-GEOJSON; het zeebeen zelf begint op de
#    zeeknoop, niet op de kade. Beilun is het HERGEBRUIKTE anker uit de
#    koperketen en al aangesloten — geen tweede aanloop aan die kant.
# ⚠️ b2 (truck): het profiel `nikkel-morowali-quzhou-beilun-quzhou` in
#    maak_stroombeen_weg.py — beide via-punten (Shaoxing/Jinhua) zijn
#    Nominatim-stadscentroïdes, geprojecteerd op de doorgaande G60 door de
#    scanner (snap 0,00–0,16 km, ruim binnen 5 km). GEEN gepubliceerde km
#    (brief §7): de gescande 405,7 km tegen de ~300 km-corridorschatting over
#    de kaart is GEEN ±15%-toets, alleen een referentie voor later gebruik —
#    +35,2%, buiten de gebruikelijke ±10/15%-band, bewust niet dichtgetrokken.
#    Huayou Quzhou-fabriek blijft regio-niveau (perceel niet gelegd, brief §3/§7).
# ⚠️ SCM-mijn (Konawe) → IMIP-slurryleiding (~62 km, Huayou-persbericht) is
#    NIET getekend: het pompstation op het Routa-plateau heeft geen
#    gepubliceerde coördinaat en is deze sessie niet satelliet-gelegd (brief §7).
#    IMIP-processing (Huayue e.a.) → IMIP-jetty is eigen terrein en blijft
#    ongetekend (ketenkaart §1) — alleen de site-marker staat op de kaart.
# ⚠️ Fase D vervalt (brief §6): geen bron noemt de afnemer van Quzhou's
#    sulfaat/precursor.
bak_nikkel_morowali_quzhou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel-geojson "zee|haven-aanloop IMIP-jetty (Bahodopi) (schematisch, over water — MARNET reikt niet tot de kust: 92,9 km)|$BEEN/nikkel-morowali-quzhou-aanloop-imip.geojson" \
    --been         "zee|zeeschip IMIP (Bahodopi) → Ningbo/Beilun-losberth (hergebruikt anker, koperketen — MHP in containers/big bags)|-2.03570,122.00170|29.9364,121.883" \
    --max-snap 25 \
    --been-geojson "truck|MHP-container Ningbo/Beilun-losberth → Huayou Quzhou-fabriek (G60 via Shaoxing–Jinhua, aannemelijk: één bron voor de exacte afnemer)|$BEEN/nikkel-morowali-quzhou-weg-beilun-quzhou.geojson" \
    --marker "IMIP-verwerkingszone, Bahodopi, Morowali — Huayue Nickel Cobalt (HPAL/MHP, eigen terrein niet getekend)|-2.8250,122.1600" \
    --marker "IMIP-exporthaven, oostpunt van het complex, Bahodopi|-2.8480,122.1980" \
    --marker "Ningbo–Zhoushan, Beilun-losberth (hergebruikt anker, koperketen)|29.9364,121.8830" \
    --marker "Huayou New Energy Technology (Quzhou) — nikkelsulfaat-/precursorfabriek (regio-niveau, onzeker)|28.9020,118.8780" \
    --routebrief v2/design/routebrieven/nikkel-morowali-quzhou.md \
    --uit    v2/data/stroomroute-nikkel-morowali-quzhou.json \
    --stroom nikkel-morowali-quzhou \
    --titel  "Nikkel · Morowali (IMIP) → Ningbo (Beilun) → Quzhou (Huayou)"
}

# ── nikkel · Taganito (Claver) → THPAL → Niihama (Japan), met vertakking Hachinohe (DSO)
# Routebrief: v2/design/routebrieven/nikkel-taganito-niihama.md (LICHTE werkwijze M29)
# ⚠️ b1 is een NIEUWE wegscan (profiel nikkel-taganito-niihama-taganito-thpal,
#    corridorKlassen ruim + eindToegangPrivaat True, extract filipijnen): 1,8 km
#    tegen het brief-venster van 3-8 km (-67,1%, buiten ±10% — bevinding, geen
#    via-punt bijgeschoven; de twee terreinen liggen simpelweg dichter bij
#    elkaar dan het venster veronderstelde — hemelsbreed is al maar 1,2 km).
# ⚠️ THPAL-plant → THPAL-kade (~1,2 km) is GEEN eigen been (site-intern,
#    Portsite-patroon uit de Grasberg-brief) — de MS "verschijnt" op
#    ni-thpal-pier; dat procesgat blijft bewust staan (zie §9).
# ⚠️ Twee haven-aanlopen via maak_havenaanloop.py: Claver 65,9 km (brief
#    ~51-56, omwegfactor 1,089) en Niihama 25,7 km (brief ~24,8, snap net
#    onder de max-snap-grens) — beide zonder landkruising midden op de lijn.
# ⚠️ b3 is het enige GEMETEN zeebeen (MARNET-zeeknoop 8314 → 5746): doorgetrokken.
# ⚠️ Vertakking (DSO naar PAMCO Hachinohe, bedrijfsniveau gebrond) via
#    voeg_been_toe.py --vertakt-van, NA de hoofdbake in dezelfde functie:
#    b5 (zeeknoop 8314 → Hachinohe-zeeknoop 5690, doorgetrokken, NIET gemeten
#    in de brief-toets — console-km 4.004,9 is leidend, niet de schatting
#    3.300-3.800) en b6 (Hachinohe-zeeknoop → PAMCO Hachinohe, stippel: haven
#    reikt niet tot MARNET ÉN de kade-positie is onzeker — geen OSM-naam-tag
#    bevestigt welk perceel PAMCO is; dat is een aparte reden naast de
#    klassieke stippel-conventie, zie §9). Rechte stippellijn (10,3 km,
#    0% over land per maak_havenaanloop) i.p.v. een geojson: voeg_been_toe.py
#    kent geen geojson-stippel-optie (alleen hecht_marnet.py --stippel-geojson
#    heeft die), en op deze korte aanloop maakt dat geometrisch niets uit.
bak_nikkel_taganito_niihama() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Taganito-mijn (TMC) → THPAL-plant (eigen mijnweg, aangrenzend terrein)|$BEEN/nikkel-taganito-niihama-weg-taganito-thpal.geojson" \
    --stippel-geojson "zee|haven-aanloop Claver/THPAL-kade (schematisch, over water — MARNET reikt niet tot de kade: 65,9 km)|$BEEN/nikkel-taganito-niihama-aanloop-claver.geojson" \
    --been         "zee|zeeschip Claver/THPAL-kade → MARNET-zeeknoop 5746 (mixed sulfide naar Niihama; oostelijk om Kyushu, Bungo-kanaal in)|9.8356,125.3465|34.0720,133.0479" \
    --stippel-geojson "zee|haven-aanloop Niihama Nickel Refinery (schematisch, over water — MARNET reikt niet: 25,7 km, snap net onder de max-snap-grens)|$BEEN/nikkel-taganito-niihama-aanloop-niihama.geojson" \
    --marker "Taganito Mining Corporation (Nickel Asia), Brgy. Taganito, Claver — laadplek erts/DSO|9.5464,125.8193" \
    --marker "Taganito HPAL Nickel Corporation (THPAL) — plant|9.5395,125.8106" \
    --marker "Taganito/Claver-laadsteiger (TMC/THPAL) — overslagkade|9.5490,125.8160" \
    --marker "Niihama Nickel Refinery, Sumitomo Metal Mining — raffinaderij (stoppunt kathode)|33.9669,133.2658" \
    --routebrief v2/design/routebrieven/nikkel-taganito-niihama.md \
    --uit    v2/data/stroomroute-nikkel-taganito-niihama.json \
    --stroom nikkel-taganito-niihama \
    --titel  "Nikkel · Taganito (Claver) → THPAL → Niihama (Japan)"

  # Vertakking DSO → PAMCO Hachinohe: aangehecht ná de hoofdbake, geen herbake
  # van b1-b4 (besluit Lars 2026-08-06: bakken is geen deliverable).
  python v2/tools/voeg_been_toe.py \
    --stroom v2/data/stroomroute-nikkel-taganito-niihama.json \
    --been "zee|MARNET-zeeknoop 8314 → Hachinohe-zeeknoop (vertakt van b2, DSO naar PAMCO; niet gemeten in de brief-toets — console-km leidend)|$BEEN/nikkel-taganito-niihama-vertakking-hachinohe.geojson" \
    --vertakt-van 2

  python v2/tools/voeg_been_toe.py \
    --stroom v2/data/stroomroute-nikkel-taganito-niihama.json \
    --stippel "zee|haven-aanloop PAMCO Hachinohe, Kawaraki-havengebied (schematisch, over water — MARNET reikt niet + kade-positie onzeker: geen OSM-naam-tag bevestigt welk perceel PAMCO is)|40.62650,141.58630|40.578,141.482" \
    --marker "PAMCO (Pacific Metals Co.) Hachinohe — Kawaraki-havengebied (onzeker: geen naam-tag bevestigt het perceel)|40.578,141.482" \
    --vertakt-van 5
}

# ── kolen · Taldinsky-groeve (Kuzbass) → Taishet → Chita → Khabarovsk → Vostochny-laadkade
# Routebrief: v2/design/routebrieven/kolen-taldinsky-vostochny.md (LICHTE werkwijze M29)
# ⚠️ Vier opeenvolgende Trans-Siberische spoorbenen, 5.923,1 km — de langste
#    landcorridor van de atlas. Elk been apart geroutet onder BAKE_SUFFIX=-raw
#    (1-op-1-net); Taishet/Chita/Khabarovsk zijn VERPLICHTE via-punten (brief
#    §4) — zonder Chita neemt een vrije Dijkstra de Chinese Oost-spoorweg via
#    Harbin (ander spoorwijdte-net), gemeten 4.917,2 km met een omkering in
#    Harbin (zie build-cache/ais/graaf/spoorroute-diag-kolen-taldinsky-
#    vostochny.geojson, een eerdere diagnose-run zonder via's — géén onderdeel
#    van deze bake).
# ⚠️ Kop-stippel b1: het GEM-putpunt (54.1772,87.1906) ligt in de dagbouwput
#    zelf; de mijn-eigen railaansluiting op de Erunakovo-tak/het emplacement
#    ontbreekt in OSM. De router snapt 9,72 km verderop op het hoofdnet
#    (54.1140,87.0875) — korte stippel ertussen, geen doorgetrokken lijn de
#    put in.
# ⚠️ b4 (Khabarovsk → Vostochny) bevat één 180°-omkering bij 48.49890,135.0649
#    (boogstraal ~32 m) — een kopmaak-plek op het net, geen verzonnen sluiproute
#    (sanity OK, verhouding 1,38; km 904,8 klopt exact met de brief-tabel).
# ⚠️ Geen zeebeen: geen bron noemt een specifieke Aziatische loshaven (brief
#    §6/§7) — de keten stopt op de Vostochny-laadkade, bestemmingstype als
#    marker-noot (Japan/Korea/China/Taiwan/India/NL).
bak_kolen_taldinsky_vostochny() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "spoor|Taldinsky-put → hoofdspoor (mijn-eigen railaansluiting Erunakovo-tak/emplacement ontbreekt in OSM)|54.1772,87.1906|54.1140,87.0875" \
    --been-geojson "spoor|trein Taldinsky → Taishet (Kuzbass-net Artyshta/Novokuznetsk → Novosibirsk-zuid/Yurga → Krasnoyarsk → Taishet, boven de BAM-splitsing)|$BEEN/spoorroute-kolen-taldinsky-vostochny-taldinsky-taishet.geojson" \
    --been-geojson "spoor|trein Taishet → Chita (Trans-Sib hoofdlijn)|$BEEN/spoorroute-kolen-taldinsky-vostochny-taishet-chita.geojson" \
    --been-geojson "spoor|trein Chita → Khabarovsk (Trans-Sib hoofdlijn)|$BEEN/spoorroute-kolen-taldinsky-vostochny-chita-khabarovsk.geojson" \
    --been-geojson "spoor|trein Khabarovsk → Vostochny-laadkade (Trans-Sib/Ussuri-lijn → Nachodka-tak)|$BEEN/spoorroute-kolen-taldinsky-vostochny-khabarovsk-vostochny.geojson" \
    --marker "Taldinsky open pit (Kuzbassrazrezugol/UMMC), Prokopjevsk-district, Kemerovo — mijn/laadgebied|54.1772,87.1906" \
    --marker "Vostochny Port JSC kolenterminal, Wrangel-baai, Nachodka — laadkade (bestemming: Japan/Korea/China/Taiwan/India/NL, GEM)|42.7555,133.0680" \
    --routebrief v2/design/routebrieven/kolen-taldinsky-vostochny.md \
    --uit    v2/data/stroomroute-kolen-taldinsky-vostochny.json \
    --stroom kolen-taldinsky-vostochny \
    --titel  "Kolen · Taldinsky (Kuzbass) → Trans-Sib → Vostochny (Rusland)"
}

# ── zeldzame aardmetalen · NPM Silmet (Sillamäe) → Neo-magneetfabriek (Narva)
# Routebrief: v2/design/routebrieven/ree-sillamae-narva.md (LICHTE werkwijze M29)
# ⚠️ Eén been (truck, E20/Tallinn–Narva mnt, ~30 km): REE-oxide (NdPr/Dy/Tb),
#    modaliteit-en-afnemer "aannemelijk: één bron" — staat in de beennaam, niet
#    in de lijnstijl (doorgetrokken, geen net-reikt-niet).
# ⚠️ Upstream-oxide naar Silmet (Lynas + overige bronnen) bewust NIET getekend
#    (brief §7): geen laadhaven/aandeel per bron gebrond, geen coördinaat
#    verzonnen. Evenmin een zeebeen bij Port of Sillamäe (21,4 km van de
#    dichtstbijzijnde MARNET-zeeknoop): geen bron noemt zeevracht op deze as.
# ⚠️ Spoor bewust niet gebruikt ondanks dat het net er ligt (0,7/0,3 km bij
#    Sillamäe/Narva volgens het ontwerp) — geen bron noemt treinvervoer.
# ⚠️ Silmet hangt via `service`+`access=private`-terreinwegen aan de E20
#    (eindToegangPrivaat in het wegprofiel); geen last-mile-been, want beide
#    ankers zijn de site zelf.
bak_ree_sillamae_narva() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|NdPr/Dy/Tb-oxide NPM Silmet Sillamäe → Neo-magneetfabriek Narva (E20/Tallinn–Narva mnt; aannemelijk: één bron voor de oxidelevering)|$BEEN/ree-sillamae-narva-weg-silmet-narva.geojson" \
    --marker "NPM Silmet OÜ, Sillamäe — REE-scheidingsfabriek (laadplek)|59.4031,27.7421" \
    --marker "Neo Performance Materials — NPM Narva OÜ, Kulgu-tööstuspark (losplek, magneetfabriek)|59.3618,28.1478" \
    --routebrief v2/design/routebrieven/ree-sillamae-narva.md \
    --uit    v2/data/stroomroute-ree-sillamae-narva.json \
    --stroom ree-sillamae-narva \
    --titel  "Zeldzame aardmetalen · Sillamäe (Silmet) → Narva (Neo-magneetfabriek, Estland)"
}

# ── kolen · Datong-mijnstreek (Shanxi) → Qinhuangdao-kolenkade (Daqin-lijn) → Huaneng Haimen-centrale (Guangdong)
# Routebrief: v2/design/routebrieven/kolen-datong-haimen.md (LICHTE werkwijze M29)
# ⚠️ b1 (spoor) = 4 losse runs op het 1-op-1-net (kop→Yangyuan→Shacheng→
#    Zunhua-N→Qinhuangdao-kade), elk een eigen corridorkeuze uit de toets.
#    Som 635,8 km tegen gepubliceerd 653 km (−2,6 %, ruim binnen ±15 %) — de
#    ingekorte 3-via-lijst uit de brief volstond, de volledige 11-vertexlijst
#    was niet nodig.
# ⚠️ Kop-anker `kolen-datong-kop` is ONZEKER: de westelijkste OSM-vertex van de
#    Daqin-lijn bij Datong, geen bevestigde mijn met eigen laadstation (brief §7).
# ⚠️ b2 (zee, kustvaart binnenlands) is AANNEMELIJK: geen bron legt het havenpaar
#    Qinhuangdao→Haimen rechtstreeks (GEM tagt Haimen deels als "imported"); dat
#    staat in de beennaam, niet in de lijnstijl. Beide kades liggen <25 km van
#    een MARNET-zeeknoop (Qinhuangdao 19,7 km / zeeknoop 9650; Haimen 17,8 km /
#    zeeknoop 5570), maar de RECHTE snap laat een procesgat van 18-19 km staan
#    (hecht_marnet plakt geen automatische aanloopstukken — dat bleek pas ná de
#    eerste bake, toets §5). Twee `maak_havenaanloop.py`-runs (timeout 300,
#    beide binnen budget) sluiten het: Qinhuangdao kade→zeeknoop 19,5 km (0,43 km
#    aan het uiteinde, dat is de 1:10M-kustkorrel, geen fout); Haimen
#    zeeknoop→kade 41,8 km (rechte lijn liep 81% over land — Haimen ligt op een
#    schiereiland, de omweg is dus reëel, omwegfactor 2,30).
# ⚠️ b3 (leiding/band, ~1 km) is een STIPPEL: geen OSM-way voor de transportband
#    over het eigen Huaneng-terrein tussen terminal en ketelhuizen — net reikt
#    hier niet, geen gok naar een verzonnen tracé.
# ⚠️ Fase D/E vervallen (brief §6): de centrale zet kolen in één stap om in
#    stroom, geen smelter-/raffinaderijfase.
bak_kolen_datong_haimen() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Datong-kop → Yangyuan (Daqin-lijn 大秦铁路, mijnkop onzeker)|$BEEN/spoorroute-kolen-datong-haimen-kop-yangyuan.geojson" \
    --been-geojson "spoor|trein Yangyuan → Shacheng (Daqin-lijn)|$BEEN/spoorroute-kolen-datong-haimen-yangyuan-shacheng.geojson" \
    --been-geojson "spoor|trein Shacheng → Zunhua-N (Daqin-lijn)|$BEEN/spoorroute-kolen-datong-haimen-shacheng-zunhua.geojson" \
    --been-geojson "spoor|trein Zunhua-N → Qinhuangdao-kolenkade (Daqin-lijn, havenemplacement)|$BEEN/spoorroute-kolen-datong-haimen-zunhua-qhd.geojson" \
    --stippel-geojson "zee|haven-aanloop Qinhuangdao (schematisch, over water — kade ligt 19,7 km van de MARNET-zeeknoop)|$BEEN/kolen-datong-haimen-aanloop-qinhuangdao.geojson" \
    --been         "zee|kustvaart (binnenlands) Qinhuangdao → Haimen (Bohai–Gele Zee–Oost-Chinese Zee–Straat Taiwan; aannemelijk: geen bron voor dit havenpaar)|39.8014,119.7875|23.3438,116.6470" \
    --stippel-geojson "zee|haven-aanloop Haimen (schematisch, over water — kade ligt 17,8 km van de MARNET-zeeknoop, schiereiland-omweg)|$BEEN/kolen-datong-haimen-aanloop-haimen.geojson" \
    --stippel      "leiding|transportband Haimen-terminal → Huaneng Haimen-centrale (eigen terrein, geen net)|23.1810,116.6595|23.1899,116.6548" \
    --marker "Daqin-spoorkop bij Datong — mijn niet gebrond (onzeker)|39.9905,113.2324" \
    --marker "Qinhuangdao-kolenterminal, Port of Qinhuangdao — overslag spoor → zee|39.9290,119.6440" \
    --marker "Huaneng-kolenterminal Shantou-Haimen — losligplaats/coal transit base|23.1810,116.6595" \
    --marker "Huaneng Haimen Power Station, Shantou, Guangdong — stoppunt|23.1899,116.6548" \
    --routebrief v2/design/routebrieven/kolen-datong-haimen.md \
    --uit    v2/data/stroomroute-kolen-datong-haimen.json \
    --stroom kolen-datong-haimen \
    --titel  "Kolen · Datong → Qinhuangdao → Haimen (China)"
}

# ── zeldzame aardmetalen · Mountain Pass mijn+scheiding → Fort Worth (Independence, NdPr-metaal + NdFeB-magneten)
# Routebrief: v2/design/routebrieven/ree-mountainpass-fortworth.md (LICHTE werkwijze M29)
# ⚠️ Modaliteit AANNEMELIJK — nergens gepubliceerd welke drager MP Materials
#    gebruikt (10-K noemt alleen "immediately adjacent to Interstate 15 …
#    within a one-hour drive of a major railhead"); truck is de enige eerlijke
#    aanname, "aannemelijk" staat daarom in de beennaam en NIET in de lijnstijl
#    (doorgetrokken, geen stippel — werkwijze §7). Het gemeten spooralternatief
#    (2.312 km, M28) is niet getekend.
# ⚠️ Geen gepubliceerde km voor dit been (brief §7): de bake-toets loopt tegen
#    de eigen OSRM/wegscan-uitkomst (~2.026,5 km getekend), geen ±15%-toets
#    tegen een onafhankelijke bron.
# ⚠️ Fase D (NdPr-metaal → gesinterde NdFeB-magneten) is GEEN apart been —
#    zelfde perceel, 0 km, eigen terrein (brief §5/§6). Geen --been/--stippel-
#    regel; de fabrieksmarker op ree-fw-fabriek draagt beide rollen (losplek +
#    D-verwerkingsknoop).
# ⚠️ Bewust niet getekend (brief §5/§7/§8): de gestopte concentraat-rondreis
#    Mountain Pass ↔ China (2025-04-17) · de NdPr-oxide-exportstroom naar
#    Japan/Zuid-Korea via vermoedelijk LA/Long Beach (geen kade/afnemer met
#    naam+adres) · GM's eigen magneetafnamefabriek (Ultium-motoren, locatie
#    niet gepubliceerd) · de geplande 10X Northlake-magneetfabriek (niet op
#    adresniveau bevestigd).
bak_ree_mountainpass_fortworth() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|NdPr-oxide Mountain Pass → I-15 → I-40 → US-287 → Independence (aannemelijk: modaliteit niet gepubliceerd)|$BEEN/ree-mountainpass-fortworth-weg-mountainpass-fortworth.geojson" \
    --marker "Mountain Pass — mijn- en scheidingsfabriek (MP Materials, San Bernardino County, CA)|35.4786,-115.5325" \
    --marker "Independence, Fort Worth — NdPr-metaal → gesinterde NdFeB-magneten (MP Materials, D-knoop, eigen terrein)|32.9845,-97.2498" \
    --routebrief v2/design/routebrieven/ree-mountainpass-fortworth.md \
    --uit    v2/data/stroomroute-ree-mountainpass-fortworth.json \
    --stroom ree-mountainpass-fortworth \
    --titel  "Zeldzame aardmetalen · Mountain Pass → Fort Worth (VS)"
}

# ── ree · Bayan Obo-laadstation → Baogang-selectie (包白铁路, spoor) →
#    Northern Rare Earth-scheiding Huamei (truck, stedelijk Baotou)
# Routebrief: v2/design/routebrieven/ree-bayanobo-baotou.md (LICHTE werkwijze M29)
# ⚠️ b1 (spoor) SNAPT VEEL DICHTER OP DE ANKERS DAN VERWACHT (brief §2 zei
#    "verwacht ~1,3/2,8 km emplacement-stippel"): gemeten met BAKE_SUFFIX=-raw
#    op het 1-op-1-net (3.260.717 spoor-edges) is de snap 0,22 km bij Bayan Obo
#    en 0,25 km bij Baogang-selectie — ruim binnen de marker-norm (≤0,5 km),
#    dus GEEN aparte emplacement-stippelbeentjes nodig. 149,1 km tegen 159 km
#    gepubliceerd (包白铁路, zh.wikipedia) = −6,2%, binnen ±15%.
# ⚠️ b2 (truck) heeft GEEN gepubliceerde km (brief §2/§7): ~15 km hemelsbreed
#    is een schatting, geen operator-bron. Gemeten wegtracé 19,3 km = +28,3%
#    t.o.v. die schatting — buiten ±10%/±15% maar het is een INDICATIEVE
#    toets (geen derde-bron-publicatie om tegen te toetsen), dus bevinding in
#    §9, niet dichtgetrokken.
# ⚠️ b2 draagt "waarschijnlijk: Huamei-dochter" (brief §6/§7): geen bron
#    documenteert per rechtspersoon wie het concentraat als eerste ontvangt.
bak_ree_bayanobo_baotou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Bayan Obo-laadstation → Baogang-selectiecomplex (包白铁路, 1-op-1-net)|$BEEN/spoorroute-ree-bayanobo-baotou-laad-selectie.geojson" \
    --been-geojson "truck|vrachtwagen Baogang-selectiecomplex → Northern Rare Earth-scheiding Huamei (stedelijke wegen Baotou, aannemelijk: welke Northern-dochter)|$BEEN/ree-bayanobo-baotou-weg-baogang-scheiding.geojson" \
    --marker "Bayan Obo-spoorstation — mijn/laadstation (kop 包白铁路)|41.7712,109.9517" \
    --marker "Baogang-selectiecomplex — veredelingsfabriek (ijzer-REE-erts → REE-concentraat REO 50%)|40.6790,109.7550" \
    --marker "Northern Rare Earth-scheiding (Huamei), 稀土高新区 — stoppunt|40.5884,109.8741" \
    --routebrief v2/design/routebrieven/ree-bayanobo-baotou.md \
    --uit    v2/data/stroomroute-ree-bayanobo-baotou.json \
    --stroom ree-bayanobo-baotou \
    --titel  "Zeldzame aardmetalen · Bayan Obo → Baotou (China)"
}

# ── kolen · Cerrejón (spoor) → Puerto Bolívar → EMO Maasvlakte → Werkshafen
#    Schwelgern-loskade (Duisburg) — LICHTE WERKWIJZE, stoppunt bij Schwelgern
# Routebrief: v2/design/routebrieven/kolen-cerrejon-ruhr.md (§10, licht)
# ⚠️ Fase D vervalt: de Kokerei Schwelgern-brochure van thyssenkrupp zelf noemt
#    de kolenherkomst ("vooral Australië, Canada, VS, Afrika en deels Azië")
#    en Colombia staat er niet bij — geen been, alleen een marker met de noot.
# ⚠️ b1 (spoor) hergebruikt de toets-ronde van 2026-08-06 (BAKE_SUFFIX=-raw,
#    --hoofd-km=100): 150,6 km / 94 punten, 0 bochten ≥60°. Laatste ~1 km OSM-
#    gat bij de pierlus apart gestippeld (terminal-lus niet doorverbonden).
# ⚠️ b2 (zee): Puerto Bolívar-kade snapt op 36,4 km van de dichtstbijzijnde
#    zeeknoop (>25 km, geen AIS-dekking Colombia in de wereldscan) →
#    maak_havenaanloop.py (cel 0,005° gebufferd, 42,1 km, blijft stippel).
# ⚠️ b3 (binnenvaart): de kade-ankers `coal-rotterdam-kade` (1,07 km) en
#    `coal-duisburg-kade` (0,82 km) liggen boven de 0,5 km-raakpuntregel van
#    hecht_marnet → het routeerpunt ligt op een trackpunt (EMO-oostzijde
#    ≈51.937,4.060, niet de kade-centroïde) resp. op de loskade zelf
#    (51.50900,6.73000 — NIET de OSM-pier op 51.51321,6.72347). De vier
#    via-punten uit de brief (Groothoofd/Werkendam/Loevestein/Pannerdensche
#    Kop) staan als losse --been-segmenten in reisvolgorde.
# ⚠️ HET LAATSTE STUK (Pannerdensche Kop → Schwelgern) LIGT OVER DE AIS-
#    TRACKGAAF NIET TE ROUTEREN: 0 tracks bij Wesel (lon 6,45-6,60, dezelfde
#    dekkingsgeul als bij koper-lobito-duisburg) knipt de trackgraaf in twee
#    losse componenten (snap 4,5 km, "geen pad"). Net als bij Lobito de
#    bulklaag gebruikt (maak_rivierbeen.py, niet de AIS-tracks): 77,6 km /
#    423 punten — dit been zegt waar het water ligt, niet dat er een schip
#    gezien is.
bak_kolen_cerrejon_ruhr() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "v2/build-cache/ais/graaf/rijn" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Cerrejón-laadlus → Puerto Bolívar-pierlus (Vía Ferroviaria Albania – Puerto Bolívar)|$BEEN/spoorroute-kolen-cerrejon-ruhr-b1.geojson" \
    --stippel      "spoor|laatste km Puerto Bolívar (OSM-gat bij de pier, terminal-lus niet doorverbonden)|12.2391,-71.9739|12.23912,-71.97693" \
    --stippel-geojson "zee|haven-aanloop Puerto Bolívar (schematisch, over water — geen AIS-dekking Colombia)|$BEEN/kolen-cerrejon-ruhr-aanloop-bolivar.geojson" \
    --been         "zee|zeeschip Puerto Bolívar-aanloop → EMO Maasvlakte|12.44700,-72.23630|51.94109,4.05354" \
    --been         "binnenvaart|EMO-oostzijde → Groothoofd (Noord NIET nemen)|51.937,4.060|51.820,4.670" \
    --been         "binnenvaart|Groothoofd → Werkendam (Nieuwe Merwede NIET nemen)|51.820,4.670|51.821,4.894" \
    --been         "binnenvaart|Werkendam → Loevestein (monding Afgedamde Maas)|51.821,4.894|51.821,5.002" \
    --been         "binnenvaart|Loevestein → Pannerdensche Kop (Pannerdensch Kanaal NIET nemen)|51.821,5.002|51.874,6.038" \
    --been-geojson "binnenvaart|Pannerdensche Kop → Schwelgern-loskade (bulklaag: ligging van het water — AIS-dekking ontbreekt bij Wesel)|$BEEN/kolen-cerrejon-ruhr-rivier-pannerdensche-schwelgern.geojson" \
    --marker "Cerrejón laadlus — keerlus met laadsilo's|11.12600,-72.63500" \
    --marker "Puerto Bolívar-terminal (Terminal de Carbones del Cerrejón)|12.23912,-71.97693" \
    --marker "EMO-kolenkade, Mississippihaven, Maasvlakte|51.94109,4.05354" \
    --marker "Werkshafen Schwelgern-loskade|51.50900,6.73000" \
    --marker "thyssenkrupp Schwelgern (cokesblend: geen bron; gedocumenteerd: krachtwerkkool RWE/STEAG, ±31% DE-import)|51.50900,6.73000" \
    --routebrief v2/design/routebrieven/kolen-cerrejon-ruhr.md \
    --uit    v2/data/stroomroute-kolen-cerrejon-ruhr.json \
    --stroom kolen-cerrejon-ruhr \
    --titel  "Kolen · Cerrejón → Rotterdam → Schwelgern (Duisburg)"
}

# ── zeldzame aardmetalen · Pangwa (Kachin, Myanmar) → Diantan-douane (Tengchong, China)
# Routebrief: v2/design/routebrieven/ree-kachin-ganzhou.md (LICHTE werkwijze M29)
# ⚠️ ÉÉN BEEN (b1, truck): de brief stopt bewust bij de Diantan-douane — de
#    ~2.300 km naar de Ganzhou/Longnan-scheiding wordt NIET getekend (brief
#    §6: alleen groepsniveau gedocumenteerd, geen volledige coördinaat voor de
#    kandidaat-vestiging). De scheidingsfabriek gaat later naar de sitelaag
#    als gloednode (rol scheidingsfabriek), niet als lijn.
# ⚠️ GEEN GEPUBLICEERDE KM: hemelsbreed 57,5 km, "~60-110 km" in het ontwerp
#    was een ongebronde aanname. Eigen scan geeft 118,7 km weggeometrie
#    (118,8 km getekend incl. anker-stukjes) — ruim boven die aanname, wat bij
#    bergterrein met haarspeldbochten (243 keerlussen gesnoeid) niet
#    onaannemelijk is, maar zonder derde bron is dit referentie, geen ±15%-toets.
# ⚠️ GEEN VIA-PUNTEN (brief §4): geen gedocumenteerde corridorkeuze in het
#    nauwelijks gekarteerde Kachin-wegennet; corridorKlassen tertiary/
#    unclassified liet de scan het tracé zelf kiezen (venster 60 km).
bak_ree_kachin_ganzhou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Pangwa-mijngebied/grensdoorlaat → Diantan-douane, Tengchong (Kachin-bergweg → Chinese zijde, geen gepubliceerde wegnummers)|$BEEN/ree-kachin-ganzhou-weg-pangwa-diantan.geojson" \
    --marker "Pangwa (mijngebied + grensdoorlaat) — uitloogputtengebied, KIA-gebied|26.0153,98.6080" \
    --marker "Diantan-douane, Tengchong (Yunnan) — stoppunt, handover aan Chinese kopers|25.5292,98.4097" \
    --routebrief v2/design/routebrieven/ree-kachin-ganzhou.md \
    --uit    v2/data/stroomroute-ree-kachin-ganzhou.json \
    --stroom ree-kachin-ganzhou \
    --titel  "Zeldzame aardmetalen · Pangwa (Kachin) → Diantan-douane (Myanmar–China)"
}

# ── kolen · Goonyella Riverside (BMA) → Coppabella → Hay Point → Dhamra Port → Bhadrak → Jakhapura → Tata Steel Kalinganagar
# Routebrief: v2/design/routebrieven/kolen-goonyella-kalinganagar.md (LICHTE werkwijze M29)
# ⚠️ Kop-mijnkeuze IS AANNEMELIJK: BMA verkoopt cokeskool als blend uit vijf
#    mijnen (Goonyella Riverside, Peak Downs, Saraji, Norwich Park/Daunia,
#    Caval Ridge); geen bron legt één specifieke Dhamra-lading bij Goonyella
#    Riverside alleen — dat staat daarom letterlijk in de kop-markernaam, niet
#    in de lijnstijl (brief §7).
# ⚠️ b1 = TWEE spoorruns (kop→Coppabella-junctie, Coppabella→Hay Point) op het
#    1-op-1-net (BAKE_SUFFIX=-raw, 3.260.717 spoor-edges, extract australie):
#    42,5 + 153,8 = 196,3 km tegen de brief-schatting 199,0 km (−1,4%, binnen
#    ±15%). Snaps 1,19/2,50/1,18 km. Aan beide uiteinden een korte stippel
#    voor het stuk dat niet op het 1-op-1-net staat (loadout-spur bij de mijn,
#    HPCT-kade-aansluiting ~1,2 km) — de Chuqui/Matarani-klasse, geen bug.
#    Terminalsplitsing HPCT/DBCT is niet apart via-gepind (brief §7).
# ⚠️ b2 = zee. Hay Point snapt direct op zeeknoop 9022 (5,6 km, < 25 km
#    max-snap default — geen aanloop nodig). Dhamra ligt 109,7 km van
#    zeeknoop 2373 (21,0/88,0; Dhamra staat niet in ports.json) →
#    `maak_havenaanloop.py` gaf een schoon pad (113,3 km, 0% over land,
#    omwegfactor 1,033) als STIPPEL-GEOJSON. De diepgangkeuze Torres-straat
#    vs. noord-om-Papoea-Nieuw-Guinea staat in de beennaam, niet afgedwongen —
#    MARNET kent geen diepgang en kiest zelf. Zeebeen-afstand (~9.500–10.500 km
#    afgeleid) is niet getoetst tegen een operatorcijfer; de bake meet het exact.
# ⚠️ b3 = DRIE spoorruns (Dhamra→Bhadrak-junctie, Bhadrak→Jakhapura-junctie,
#    Jakhapura→Tata-siding — de derde was nodig, de router liet Jakhapura niet
#    direct op de Tata-siding uitkomen). 66,4 + 46,7 + 13,1 = 126,2 km tegen
#    de brief-schatting 114,2 km (+10,5%, binnen ±15%). Snaps 0,48/2,64/0,12/
#    0,26 km. Het derde segment draagt één OMKERING (175°, ~191 m boogstraal)
#    vlak vóór de Tata-siding — een kopmaak-plek op het fabrieksterrein, zelfde
#    klasse als Chuqui/Matarani (emplacement niet in het 1-op-1-net), geen
#    via-punt bijgeschoven. `toets_spoorroute.mjs` meldde op dit derde segment
#    óók "sanity FOUT — route korter dan de grootcirkel": een bekende bug in
#    het meetgereedschap zelf (grootcirkel wordt tussen de ONgesnapte
#    invoerpunten berekend, de route tussen de gesnapte) — geen routeerfout.
bak_kolen_goonyella_kalinganagar() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "spoor|loadout-spur Goonyella Riverside → hoofdspoor (mijnemplacement niet in het 1-op-1-net, ~1,2 km)|-21.7923,147.9620|-21.80120,147.95560" \
    --been-geojson "spoor|trein Goonyella Riverside → Coppabella-junctie (Goonyella-spoorsysteem, Aurizon)|$BEEN/spoorroute-kolen-goonyella-kalinganagar-goonyella-coppabella.geojson" \
    --been-geojson "spoor|trein Coppabella-junctie → Hay Point Coal Terminal (Goonyella-spoorsysteem, HPCT/DBCT-terminalsplitsing niet apart gepind)|$BEEN/spoorroute-kolen-goonyella-kalinganagar-coppabella-haypoint.geojson" \
    --stippel      "spoor|hoofdspoor → HPCT-kade-aansluiting (kade ligt 1,2 km van het 1-op-1-net, geen net op de laatste meters)|-21.28060,149.29000|-21.2700,149.2900" \
    --been         "zee|zeeschip Hay Point Coal Terminal → Dhamra-zeeknoop (Koraalzee → Torres-straat of noord-om-Papoea-Nieuw-Guinea, diepgang niet afgedwongen → Golf van Bengalen)|-21.2700,149.2900|21.0,88.0" \
    --stippel-geojson "zee|haven-aanloop Dhamra Port (schematisch, over water — MARNET/ports.json kent de haven niet, ~110 km)|$BEEN/kolen-goonyella-kalinganagar-aanloop-dhamra.geojson" \
    --been-geojson "spoor|trein Dhamra Port losplaats → Bhadrak-junctie (Dhamra–Bhadrak-havenlijn, 2011)|$BEEN/spoorroute-kolen-goonyella-kalinganagar-dhamra-bhadrak.geojson" \
    --been-geojson "spoor|trein Bhadrak-junctie → Jakhapura-junctie (Howrah–Chennai-hoofdlijn zuid)|$BEEN/spoorroute-kolen-goonyella-kalinganagar-bhadrak-jakhapura.geojson" \
    --been-geojson "spoor|trein Jakhapura-junctie → Tata Steel Kalinganagar (Daitari–Jakhapura-lijn/Tata-siding, kopmaak op het terrein)|$BEEN/spoorroute-kolen-goonyella-kalinganagar-jakhapura-kalinganagar.geojson" \
    --marker "Goonyella Riverside (BMA, aannemelijk: blend uit 5 mijnen)|-21.7923,147.9620" \
    --marker "Hay Point Coal Terminal — BMA-kade, offshore trestle (verkoop aan GIP aangekondigd 2025)|-21.2700,149.2900" \
    --marker "Dhamra Port — kolenstockyard + jetty (Adani)|20.8280,86.9600" \
    --marker "Tata Steel Kalinganagar — cokerij/hoogovens|20.9704,86.0152" \
    --routebrief v2/design/routebrieven/kolen-goonyella-kalinganagar.md \
    --uit    v2/data/stroomroute-kolen-goonyella-kalinganagar.json \
    --stroom kolen-goonyella-kalinganagar \
    --titel  "Kolen · Goonyella Riverside → Hay Point → Dhamra → Kalinganagar (India)"
}

# ── kolen · ETT-laadterminal Tavan Tolgoi → Gashuunsukhait → Ganqimaodu → Wanshuiquan-Zuid (Baotou) → Baotou Steel
# Routebrief: v2/design/routebrieven/kolen-tavantolgoi-baotou.md (LICHTE werkwijze M29)
# ⚠️ b1 = spoor (BAKE_SUFFIX=-raw, extract mongolia): 227,2 km tegen 233,6 km
#    gepubliceerd (−2,7%, binnen ±15%). Eén OMKERING vlak bij de laadterminal
#    (172,9°, ~32 m boogstraal) — kopmaak-plek op het opstelterrein, zelfde
#    klasse als Chuqui/Matarani (emplacement), geen via-punt bijgeschoven.
# ⚠️ b2 = truck (maak_stroombeen_weg, profiel kolen-tavantolgoi-baotou-tt-gs-
#    ganqimaodu, extracts mongolia+china): 13,6 km — geen gepubliceerde km
#    (brief: ~9-10 km afgeleid uit de ankers), lengtetoets is indicatief. Via
#    `cu-ot-grens` en "Chinese poort Ganqimaodu" LETTERLIJK HERGEBRUIKT uit
#    koper-oyutolgoi-china.md (zelfde coördinaten, geen nieuwe scan op die
#    punten). Dit been is een TIJDELIJKE TOESTAND: de grensspoorlijn (32,6 km)
#    vervangt het zodra hij klaar is (gepland 2027).
# ⚠️ b3 = spoor (BAKE_SUFFIX=-raw, extract china): 368,6 km tegen 366,9 km
#    gepubliceerd (+0,5%, ruim binnen ±15%).
# ⚠️ b4 = STIPPEL, geen bake-tool: Baotou Steel als afnemer rust op één bron
#    (sxcoal 2017); geen gekarteerde siding of weg tussen Wanshuiquan-Zuid en
#    Baogang. ~14 km hemelsbreed, last mile (geen net op deze korrel) EN
#    aannemelijk (één bron) — beide in de beennaam, niet in de lijnstijl.
bak_kolen_tavantolgoi_baotou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein ETT-laadterminal Tavan Tolgoi → Gashuunsukhait rail-yard (Tavantolgoi–Gashuunsukhait-spoorlijn, Bodi International, 1520 mm, open sinds 09-2022)|$BEEN/spoorroute-kolen-tavantolgoi-baotou-tt-gs.geojson" \
    --been-geojson "truck|vrachtwagen Gashuunsukhait-overslag → grenspost → Chinese poort → Ganqimaodu-opslag (grensoverslag; grensspoorlijn 32,6 km nog in aanbouw, gepland 2027)|$BEEN/kolen-tavantolgoi-baotou-weg-ttgs-ganqimaodu.geojson" \
    --been-geojson "spoor|trein Ganqimaodu-station → Wanshuiquan-Zuid, Baotou (甘泉铁路, Ganqimaodu → Baoshen-lijn, geëlektrificeerd enkelspoor, 2012)|$BEEN/spoorroute-kolen-tavantolgoi-baotou-ganqimaodu-baotou.geojson" \
    --stippel      "truck|last mile Baotou Steel (aannemelijk: één bron, sxcoal 2017) — geen gekarteerde siding|40.5775,109.89105|40.6549,109.7545" \
    --marker "ETT-laadterminal Tavan Tolgoi — automated loading logistics center (in bedrijf sinds mei 2024)|43.64336,105.58236" \
    --marker "Gashuunsukhait rail-yard (overslag spoor eind MN / truck-transfer)|42.44558,107.53063" \
    --marker "Gashuun Sukhait grenspost (MN) / Ganqimaodu (CN) — hergebruikt uit koper-oyutolgoi-china.md|42.4146,107.5692" \
    --marker "Ganqimaodu-station + opslagloodsen (kop van 甘泉铁路)|42.37414,107.60964" \
    --marker "Wanshuiquan-Zuid station, Baotou (spooreindpunt, stoppunt fase C)|40.5775,109.89105" \
    --marker "Baotou Steel (包钢), staalwerken — fase D, aannemelijk|40.6549,109.7545" \
    --routebrief v2/design/routebrieven/kolen-tavantolgoi-baotou.md \
    --uit    v2/data/stroomroute-kolen-tavantolgoi-baotou.json \
    --stroom kolen-tavantolgoi-baotou \
    --titel  "Kolen · Tavan Tolgoi → Gashuunsukhait/Ganqimaodu → Baotou (China)"
}

# ── zeldzame aardmetalen · Mt Weld-mijn → Kalgoorlie REPF → Fremantle → Kuantan Port → LAMP Gebeng (MREC → NdPr-oxide)
# Routebrief: v2/design/routebrieven/ree-mtweld-kuantan.md (LICHTE werkwijze M29)
# ⚠️ b1 (truck, maak_stroombeen_weg, profiel ree-mtweld-kuantan-mtweld-
#    kalgoorlie, extract australie): eerste poging faalde ("geen wegpad") —
#    de outback-mijnweg Mt Weld→Laverton zit niet in WEG_HOUD (motorway t/m
#    secondary) binnen het venster. Hergebruikt de al bestaande, geconnec-
#    teerde via-keten uit corridor `ree-mountweld-leonora`
#    (fetch_landnet.py CORRIDORS) voor het stuk Mt Weld→Leonora, verlengd via
#    Menzies (`corridorKlassen: tertiary/unclassified`). 401,0 km tegen
#    ~380 km gepubliceerd (+5,5%, binnen ±15%).
# ⚠️ b2 (spoor, BAKE_SUFFIX=-raw, TWEE runs, extract 1-op-1-net): Kalgoorlie
#    REPF → Kewdale 646,9 km (tegen 563 km gepubliceerd Kalgoorlie–Kewdale,
#    +14,9%, net binnen ±15%) · Kewdale → Fremantle North Quay 42,3 km (tegen
#    ~20 km schatting, +111%, BUITEN ±15% — bevinding, niet dichtgetrokken:
#    de gepubliceerde ~20 km was zelf al een schatting, geen operator-cijfer,
#    en Kewdale is bewust een spoorreferentiepunt zonder wegequivalent om een
#    Dijkstra-omweg via de goudlijn te vermijden). REPF-snap 0,47 km (ruim
#    onder de verwachte 1,9 km last-mile — geen aparte stippel nodig, de naad
#    tussen truck- en spoorbeen blijft binnen de norm); Fremantle-snap
#    0,51 km. Eén OMKERING bij elke run (170,5° resp. 169,3°, kopmaak-plekken
#    op het REPF-/Kewdale-emplacement, geen bugreden).
# ⚠️ b3 (zee, MARNET, --been zee Fremantle → Kuantan Port): Fremantle snapt
#    op 0,6 km (geen aanloop nodig). Kuantan ligt 22,8 km van de dichtst-
#    bijzijnde zeeknoop (binnen de default --max-snap 25) — de haven-aanloop
#    (maak_havenaanloop.py, geslaagd, 24,7 km over water, omwegfactor 1,085)
#    vervangt het laatste stuk als stippel-geojson zodat de lijn niet recht
#    over Tanjung Gelang snijdt.
# ⚠️ b4 (truck, maak_stroombeen_weg, profiel ree-mtweld-kuantan-kuantan-
#    lamp, extract maleisie): 13,1 km tegen een OSRM-schatting van 8-12 km
#    (geen harde publicatie — indicatief, geen ±15%-toets).
# ⚠️ Kalgoorlie REPF-anker is ONZEKER (brief §3/§7): satellietpas toont geen
#    ondubbelzinnig REPF-terrein op 70 Johns Rd, Yilkari — mogelijk jonger
#    dan de Esri-opname; adres uit vergunningdocumenten wel eenduidig.
bak_ree_mtweld_kuantan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Mt Weld-mijn/concentratieplant → Laverton → Leonora → Menzies → Lynas Kalgoorlie REPF (mijnweg → Great Central/Beadell Hwy → Goldfields Highway)|$BEEN/ree-mtweld-kuantan-weg-mtweld-kalgoorlie.geojson" \
    --been-geojson "spoor|trein Lynas Kalgoorlie REPF → Kewdale (Eastern Goldfields Railway, 1-op-1-net)|$BEEN/spoorroute-ree-mtweld-kuantan-kalgoorlie-kewdale.geojson" \
    --been-geojson "spoor|trein Kewdale → Fremantle North Quay (spoorreferentiepunt Kewdale splitst de run om een Dijkstra-omweg via de goudlijn te vermijden)|$BEEN/spoorroute-ree-mtweld-kuantan-kewdale-fremantle.geojson" \
    --been         "zee|zeeschip Fremantle North Quay → Kuantan Port (Indische Oceaan → Straat Sunda/Lombok → Straat Karimata → Zuid-Chinese Zee)|-32.0438,115.7449|3.9805,103.4242" \
    --stippel-geojson "zee|haven-aanloop Kuantan (schematisch, over water — MARNET reikt hier niet, 22,8 km)|$BEEN/ree-mtweld-kuantan-aanloop-kuantan.geojson" \
    --been-geojson "truck|vrachtwagen Kuantan Port → Jalan Gebeng → Lynas Advanced Materials Plant (LAMP), Gebeng-industriezone|$BEEN/ree-mtweld-kuantan-weg-kuantan-lamp.geojson" \
    --marker "Mt Weld-mijn en concentratieplant (Lynas), rotainer-laadplek|-28.8695,122.5392" \
    --marker "Lynas Kalgoorlie REPF, Johns Rd, Yilkari (cracking & leaching → MREC, onzeker)|-30.7883,121.4086" \
    --marker "Fremantle North Quay containerterminal (overslag spoor→zee)|-32.0438,115.7449" \
    --marker "Kuantan Port (Pelabuhan Kuantan), Tanjung Gelang (overslag zee→truck)|3.9805,103.4242" \
    --marker "Lynas Advanced Materials Plant (LAMP), Gebeng — scheiding tot NdPr-oxide|4.0034,103.3775" \
    --routebrief v2/design/routebrieven/ree-mtweld-kuantan.md \
    --uit    v2/data/stroomroute-ree-mtweld-kuantan.json \
    --stroom ree-mtweld-kuantan \
    --titel  "Zeldzame aardmetalen · Mt Weld → Kalgoorlie → Fremantle → Kuantan (Maleisië)"
}

# ── kolen · KPC-mijn Sangatta → Tanjung Bara Coal Terminal → Mundra UMPP (India, thermisch)
# Routebrief: v2/design/routebrieven/kolen-sangatta-mundra.md (lichte werkwijze M29)
# ⚠️ b1 (band Sangatta → TBCT) is een STIPPEL zonder wegscan, als DRIE losse
#    segmenten (het tool kent geen multi-punts --stippel; via-punten uit
#    brief §4 als eigen segmentgrenzen): de Indonesië-extract kent 137
#    goods_conveyor-ways maar geen enkele met een naam/operator-tag naar
#    KPC/Kaltim Prima/Tanjung Bara (bindende toets-uitkomst, brief §7).
#    Gepubliceerde km 13 (mining-technology.com); de stippelafstand komt
#    hoger uit (~24 km hemelsbreed) omdat het exacte laadpunt/wasserij binnen de
#    ~20 km-lange KPC-concessie niet vast te stellen is — bevinding, geen via-punt
#    bijgeschoven om het te laten kloppen.
# ⚠️ b2 (zee) snapt de TBCT-zijde automatisch op zeeknoop 5453 (21,8 km, binnen
#    25 km, geen aanloop nodig); aan de Mundra-kant reikt MARNET niet tot de
#    kolenjetty (jetty zelf niet satelliet-gelokaliseerd, brief §7) →
#    maak_havenaanloop.py van zeeknoop 5321 (22,5734/69,4446) naar het
#    CGPL-terreinanker, 30,0 km / 11 punten, 0,00 km land midden op de lijn
#    (geslaagd, geen terugval nodig).
# ⚠️ Eigen-keten-claim (Tata Power-belang in KPC sinds 2007 + CGPL-offtake 2011)
#    blijft AANNEMELIJK: geen bron noemt een specifieke scheepslading KPC → Mundra
#    in 2024/25 (brief §7) — staat in de beennaam, niet in de lijnstijl.
# ⚠️ Geen fase D/E: de keten stopt bij de kolenopslag van de centrale (brief §6,
#    kolen wordt daar in één stap verstookt).
bak_kolen_sangatta_mundra() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|band KPC-mijn → haalweg-knoop (schematisch — OSM kent geen goods_conveyor met KPC/TBCT-tag)|0.5810,117.4985|0.5820,117.5080" \
    --stippel      "truck|band haalweg-knoop → TBCT-landzijde (schematisch)|0.5820,117.5080|0.5400,117.6250" \
    --stippel      "truck|band TBCT-landzijde → Tanjung Bara-kade (schematisch)|0.5400,117.6250|0.5375,117.6595" \
    --been         "zee|zeeschip Tanjung Bara → Mundra (thermisch; centrale stil jul 2025–mrt 2026, weer in bedrijf 04-2026)|0.5375,117.6595|22.5734,69.4446" \
    --stippel-geojson "zee|haven-aanloop Mundra (schematisch, over water — MARNET reikt niet tot de kolenjetty)|$BEEN/kolen-sangatta-mundra-aanloop-mundra.geojson" \
    --marker "KPC open pit + naaste terreinen, Sangatta — mijn (kop van de band)|0.58100,117.49850" \
    --marker "Tanjung Bara Coal Terminal — laadponton aan kade-einde (band → zee)|0.53750,117.65950" \
    --marker "Coastal Gujarat Power Ltd, Mundra UMPP (Tata Power) — losplek + stoppunt|22.82007,69.51889" \
    --routebrief v2/design/routebrieven/kolen-sangatta-mundra.md \
    --uit    v2/data/stroomroute-kolen-sangatta-mundra.json \
    --stroom kolen-sangatta-mundra \
    --titel  "Kolen · Sangatta (KPC) → Tanjung Bara → Mundra (India)"
}

# ── uranium · Rössing-fabriek (Arandis) → Walvis Bay-haven (truck, B2)
# Routebrief: v2/design/routebrieven/uranium-rossing-walvisbay.md (LICHTE werkwijze M31)
# Eén been, geen corridorkeuze — B2 is de enige gekarteerde hoofdweg tussen
# Arandis en Walvis Bay, geen via-punten nodig.
# ⚠️ Modaliteit truck is AANNEMELIJK: geen Rössing-specifieke bron voor het
#    wegtransport van de yellowcake-drums zelf; analogie met de buurmijn Husab
#    (brief §7).
# ⚠️ Lengtetoets 106,3 km tegen ~90 km gepubliceerd = +18,1% — BUITEN ±15%
#    (bevinding, niet dichtgetrokken; geen enkele bron geeft een directe
#    km-waarde voor dit traject, ~90 is zelf al afgeleid uit twee losse
#    cijfers, brief §7).
# ⚠️ Fase B (zee) NIET getekend: geen gepubliceerd Chinees loshavenanker
#    (brief §6, bindende haalbaarheidstoets) — de keten stopt bij de haven.
bak_uranium_rossing_walvisbay() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Rössing → Walvis Bay (B2)|$BEEN/uranium-rossing-walvisbay-weg.geojson" \
    --marker "Rössing-fabriek|-22.4635,15.0405" \
    --marker "Walvis Bay-haven|-22.9465,14.4840" \
    --routebrief v2/design/routebrieven/uranium-rossing-walvisbay.md \
    --uit    v2/data/stroomroute-uranium-rossing-walvisbay.json \
    --stroom uranium-rossing-walvisbay \
    --titel  "Uranium · Rössing (Arandis) → Walvis Bay (Namibië)"
}

# ── uranium · SOMAIR-mijn Arlit → Parakou → Cotonou (Niger/Benin, exportroute GESTAAKT sinds 26-07-2023)
# Routebrief: v2/design/routebrieven/uranium-arlit-cotonou.md (LICHTE werkwijze M31)
# Drie benen, ALLE DOORGETROKKEN: het net bestaat en is gemeten, "gestaakt" is
# een statusfeit (brief §6), geen stippel-reden (werkwijze §7).
# ⚠️ b1 (RN1 Niger, extract niger) en b2 (RNIE2 Benin, extract benin) zijn
#    beide AANNEMELIJK op km (afgeleid uit WNA-totaal 1.600 km minus de
#    spoorlengte 400 km, brief §2/§7/§8[1][2][8][9]) — geen directe bron per
#    deelstuk. Beide profielen droegen `corridorKlassen: [tertiary,
#    unclassified]`: de RN1 (Tahoua–Niamey) en de RNIE2 bij Bembèrèkè dragen
#    geen primary/secondary-tag over het hele traject (osmium-check).
# ⚠️ b3 (spoor, OCBN-noordlijn) routeert op een GEÏSOLEERD net (component
#    455 km, dichtstbijzijnde hoofdnet 198-232 km weg > --max-snap 60) —
#    de terugval is hier de juiste uitkomst, geen fout: Benin's spoor hangt
#    aan geen ander land. 442,1 km over 73 edges tegen 400 km (WNA) / 437 km
#    lijnlengte incl. aftakkingen = binnen ±15% op beide referenties.
# ⚠️ u-parakou-emplacement is AANNEMELIJK (brief §3/§7): OSM-punt "Gare" is
#    een gebouw in de stad, geen apart vrachtemplacement satelliet-
#    onderscheiden op z15 — snap van de wegkant is desondanks 0,05 km.
# ⚠️ Géén fase D/E (brief §6): het toekomstige afzetkanaal (TSUMCO, mei 2026)
#    is niet gebrond en Orano/Frankrijk is niet gegarandeerd het vervolg.
bak_uranium_arlit_cotonou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen SOMAIR-mijn Arlit → Agadez → Tahoua → Niamey → Dosso → grens Gaya/Malanville (RN1 Niger, aannemelijk: één bron, historische route gestaakt sinds 26-07-2023)|$BEEN/uranium-arlit-cotonou-weg-arlit-grens.geojson" \
    --been-geojson "truck|vrachtwagen grens Gaya/Malanville → Kandi → Bembèrèkè → Parakou-emplacement (RNIE2 Benin)|$BEEN/uranium-arlit-cotonou-weg-grens-parakou.geojson" \
    --been-geojson "spoor|trein Parakou-emplacement → Cotonou-haven (OCBN-noordlijn, geïsoleerd Benins net, aangelegd t/m 1936)|$BEEN/spoorroute-uranium-arlit-cotonou-parakou-cotonou.geojson" \
    --marker "SOMAIR-mijn/verwerkingscomplex, Arlit — mijn (kop van b1)|18.7731,7.3443" \
    --marker "Brug Gaya/Malanville — grensovergang (b1→b2)|11.8807,3.3961" \
    --marker "Spoorstation Gare, Parakou — overslag truck→spoor (b2→b3), aannemelijk|9.3487,2.6099" \
    --marker "Port Autonome de Cotonou — loskade (einde b3)|6.3444,2.4187" \
    --routebrief v2/design/routebrieven/uranium-arlit-cotonou.md \
    --uit    v2/data/stroomroute-uranium-arlit-cotonou.json \
    --stroom uranium-arlit-cotonou \
    --titel  "Uranium · Arlit → Parakou → Cotonou (Benin) — gestaakt sinds 2023"
}

# ── kobalt · Ambatovy-mijn (Moramanga) → Ambatovy-plant (Toamasina) — slurrypijpleiding
# Routebrief: v2/design/routebrieven/kobalt-ambatovy-toamasina.md (LICHTE werkwijze M31)
# ⚠️ Enig been = een STIPPEL: de 220 km-slurrypijpleiding (Ausenco/EIB, schematisch,
#    ~1.000 m hoogteverschil, zwaartekracht-gedreven) is BEVESTIGD niet als
#    doorlopende OSM-way gekarteerd — directe pyosmium-scan van madagaskar-
#    latest.osm.pbf op man_made=pipeline gaf 35 ways, geen op deze corridor
#    (de enige benoemde ligt bij Vohipeno). Geen geometrie-tool nodig; rechte
#    stippellijn. Gepubliceerde km (220, vaste bron) blijft normaal toetsbaar
#    ondanks de stippel (werkwijze §5).
# ⚠️ Fase B (zee, plant → kade) wordt NIET getekend: geen bron noemt een naam-
#    en-adres-afnemer voor het geraffineerde nikkel/kobalt, alleen marktregio's
#    (Europa/Japan). De kade krijgt daarom alleen een LOSSE marker (geen
#    --been/--stippel-regel ernaartoe), zodat hij wel oplicht in de sitelaag/
#    gloed zonder een lijn te claimen die er niet is (brief §6).
# ⚠️ Fase C/D/E vervallen: mijn en plant zijn rechtstreeks door de pijpleiding
#    verbonden (geen tussenknoop) en er is geen tweede fabriek of afnemer
#    gebrond (brief §7).
# ⚠️ Eerste en enige Malagassische keten in de atlas — geen gedeelde geometrie
#    met een andere stroom mogelijk.
bak_kobalt_ambatovy_toamasina() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel "leiding|Ambatovy slurry-pijpleiding Moramanga → Toamasina (schematisch — geen OSM-way)|-18.8446,48.3077|-18.2002,49.3604" \
    --marker "co-ambatovy-moramanga — Ambatovy Mine, mijn/ertsvoorbereiding (kop)|-18.8446,48.3077" \
    --marker "co-ambatovy-plant — Ambatovy Plant Site, proces- en raffinaderijterrein (staart, stoppunt fase D)|-18.2002,49.3604" \
    --marker "co-toamasina-kade — Ambatovy Bulk Jetty Terminal / Port of Toamasina (marker, geen lijn — geen afnemer gebrond)|-18.1556,49.4278" \
    --routebrief v2/design/routebrieven/kobalt-ambatovy-toamasina.md \
    --uit    v2/data/stroomroute-kobalt-ambatovy-toamasina.json \
    --stroom kobalt-ambatovy-toamasina \
    --titel  "Kobalt · Ambatovy-mijn (Moramanga) → Ambatovy-plant (Toamasina)"
}

# ── olie · Bonny-exportterminal (Nigeria) → Vadinar SPM → Vadinar-raffinaderij (India)
# Routebrief: v2/design/routebrieven/olie-bonny-vadinar.md (LICHTE werkwijze M31)
# ⚠️ b1 (zee) is AANNEMELIJK — géén cargo-niveau bron koppelt Bonny-crude
#    specifiek aan Vadinar (Bonny Light gaat ook naar Jamnagar/Mangalore); staat
#    in de beennaam, niet in de lijnstijl.
# ⚠️ Vadinar SPM ligt op 26,7 km van de dichtstbijzijnde MARNET-zeeknoop (>25 km)
#    → haven-aanloop gebouwd (`maak_havenaanloop.py`, cel 0,02° gebufferd,
#    28,84 km, 0 km land midden op de lijn); het zeebeen eindigt op die
#    zeeknoop (22.5734,69.4446), de aanloop maakt de kade af.
# ⚠️ b2 (leiding) is een gestippelde eigen crude-pijpleiding SPM → tankfarm/
#    raffinaderij (~15 km, geen OSM-way verwacht op dit tracé) — géén tweede
#    poging, direct gestippeld per de bak-aanwijzing in de brief.
# ⚠️ Fase D vervalt (brief §6/§7): geen bron noemt een specifieke downstream-
#    bestemming van de Vadinar-producten per lading; de brief stopt bij de
#    poort van de raffinaderij.
bak_olie_bonny_vadinar() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been         "zee|zeeschip Bonny-exportterminal → Vadinar SPM (Golf van Guinee → Kaap de Goede Hoop → Indische Oceaan → Arabische Zee, geen Suez; aannemelijk: geen cargo-niveau bron)|4.4200,7.1600|22.5734,69.4446" \
    --stippel-geojson "zee|haven-aanloop Vadinar SPM (schematisch, over water — MARNET reikt niet: 26,7 km)|$BEEN/olie-bonny-vadinar-aanloop-vadinar-spm.geojson" \
    --stippel      "leiding|Vadinar SPM → Vadinar-raffinaderij (eigen crude-pijpleiding, schematisch — niet verwacht in OSM)|22.4528,69.6694|22.3317,69.7472" \
    --marker "Bonny Oil & Gas Terminal (Shell/SPDC/NNPC), Bonny Island — laadplek/exportterminal|4.4200,7.1600" \
    --marker "Vadinar SPM, Pathfinder Inlet (Nayara Energy) — overslag zee → leiding|22.4528,69.6694" \
    --marker "Vadinar-raffinaderij (Nayara Energy), Gujarat — raffinaderij, stoppunt|22.3317,69.7472" \
    --routebrief v2/design/routebrieven/olie-bonny-vadinar.md \
    --uit    v2/data/stroomroute-olie-bonny-vadinar.json \
    --stroom olie-bonny-vadinar \
    --titel  "Olie · Bonny (Nigeria) → Vadinar SPM → Vadinar-raffinaderij (India)"
}

# ── olie · Habshan (ADNOC-verzamelknooppunt) → Fujairah-exportterminal → Chiba-raffinaderij (ENEOS, Japan)
# Routebrief: v2/design/routebrieven/olie-habshan-chiba.md (LICHTE werkwijze M31)
# ⚠️ b1 (leiding) is gestikt uit 5 OSM-ways (man_made=pipeline, gcc-staten-
#    extract, ids 451508619/586125766/225206383/360437230/360499797) tot twee
#    LineStrings van resp. 236,9 en 165,1 km, met een stippel van 17,3 km over
#    het interne kaarteringsgat bij Sweihan/Al Ain (niet onafhankelijk bevestigd
#    als échte onderbreking — kan een OSM-omissie zijn, brief §7). Som 402,0 km
#    + gat 17,3 km = 419,3 km, tegen gepubliceerd 406 km (14 km offshore) →
#    binnen ±15%.
# ⚠️ Haven-aanloop Fujairah (LAR-586, 2026-09-28): de kade snapt binnen 25 km
#    op zeeknoop 8407, maar op 10,5 km — boven de naadnorm van 5 km
#    (bakhandleiding §5). maak_havenaanloop.py vond een pad over water (12,2 km,
#    2,2 km over land alleen aan de kadekant) → stippel-geojson tussen leiding
#    en zeebeen. Chiba snapt op 7,7 km / zeeknoop 9067 en eindigt de stroom
#    (geen volgend been, dus geen naad).
# ⚠️ Fase D/E vervallen (brief §6): geen bron koppelt één specifieke lading aan
#    de Chiba/ENEOS-raffinaderij (het "Japan 30%"-cijfer is een aggregaat over
#    heel ADNOC's Murban-export); de brief stopt bij de poort van de raffinaderij.
bak_olie_habshan_chiba() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "leiding|Habshan-Fujairah-pijpleiding (Hormuz-bypass), segment 1: Habshan → vóór het kaarteringsgat bij Sweihan|$BEEN/olie-habshan-chiba-leiding-habshan-sweihan.geojson" \
    --stippel      "leiding|Habshan-Fujairah-pijpleiding, schematisch — OSM-kaarteringsgat ~17 km bij Sweihan/Al Ain (brief §7)|24.5977,55.3998|24.5749,55.2302" \
    --been-geojson "leiding|Habshan-Fujairah-pijpleiding (Hormuz-bypass), segment 2: ná het kaarteringsgat → Fujairah-exportterminal|$BEEN/olie-habshan-chiba-leiding-sweihan-fujairah.geojson" \
    --stippel-geojson "zee|haven-aanloop Fujairah (schematisch, over water — kade 10,5 km van de MARNET-zeeknoop)|$BEEN/olie-habshan-chiba-aanloop-fujairah.geojson" \
    --been         "zee|VLCC Fujairah-exportterminal → Chiba-raffinaderij (Golf van Oman → Arabische Zee → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee)|25.2135,56.3419|35.5195,140.0430" \
    --marker "Habshan-pijplijnkop (Habshan–Fujairah-leiding, ADNOC Onshore/ADCO) — verzamelknooppunt, kop|23.8285,53.4915" \
    --marker "Fujairah-exportterminal (FOIZ-tankenpark, Habshan–Fujairah-pijplijneind) — overslag leiding → zee|25.2135,56.3419" \
    --marker "Chiba-raffinaderij (ENEOS), Chikusa-kaigan 1, Ichihara (Tokiobaai) — losplek, stoppunt|35.5195,140.0430" \
    --routebrief v2/design/routebrieven/olie-habshan-chiba.md \
    --uit    v2/data/stroomroute-olie-habshan-chiba.json \
    --stroom olie-habshan-chiba \
    --titel  "Olie · Habshan (ADNOC) → Fujairah (Hormuz-bypass) → Chiba (ENEOS)"
}

# ── olie · Ghawar/Abqaiq-olievelden → Ras Tanura-exportterminal → ZPC-kade Zhoushan (China)
# Routebrief: v2/design/routebrieven/olie-rastanura-zhoushan.md (LICHTE werkwijze M31)
# ⚠️ b1 (leiding) is een gestippelde schematische lijn: Aramco's interne
#    gatheringpijpleidingen tussen Ghawar/Abqaiq en Ras Tanura zijn nergens als
#    één gepubliceerde lijn te vinden. Eén pyosmium-scan op `man_made=pipeline`
#    in bbox 25,8–26,8/49,5–50,3 (gcc-staten-extract) gaf GEEN negatieve
#    uitslag: er liggen wél losse, grotendeels ongenaamde `substance=oil`-
#    fragmenten in dat gebied (o.a. way 219942630/219942632/226435144 met een
#    uiteinde op ~3 km van het Abqaiq-anker), maar geen enkele stitcht door tot
#    binnen 5 km van het Ras Tanura-anker (dichtstbijzijnde fragment-uiteinde
#    bleef ~37 km te kort) en geen enkele draagt een naam. Dat bevestigt de
#    brief eerder dan dat het hem weerlegt: een fragmentarisch, ongekarteerd
#    net, geen gepubliceerde enkele lijn — de rechte stippel blijft de eindvorm.
# ⚠️ b2 (zee) is de MARNET-route kade → kade; beide kades snappen binnen de
#    25 km-norm op een zeeknoop (Ras Tanura 11,1 km, Zhoushan 7,8 km). MARNET
#    routeert zelf via Hormuz + Malakka (`northwest`-passage blijft dicht).
# ⚠️ Haven-aanloop Ras Tanura (LAR-586, 2026-09-28): de 11,1 km-snap liet een
#    naad boven de 5 km-norm (bakhandleiding §5) tussen de gatheringstippel en
#    het zeebeen → maak_havenaanloop.py, pad over water (11,8 km, 0 km land).
#    Zhoushan eindigt de stroom (geen volgend been, dus geen naad).
# ⚠️ Geen fase D/E: geen bron benoemt welk deel van ZPC's nafta-/aromaten-
#    uitstroom naar welke met-naam-genoemde vervolgfabriek gaat (brief §6/§7).
bak_olie_rastanura_zhoushan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "leiding|Aramco-gatheringnet Ghawar/Abqaiq → Ras Tanura (schematisch — interne infrastructuur, geen gepubliceerde enkele OSM man_made=pipeline-lijn)|25.9400,49.6600|26.6540,50.1648" \
    --stippel-geojson "zee|haven-aanloop Ras Tanura (schematisch, over water — kade 11,1 km van de MARNET-zeeknoop)|$BEEN/olie-rastanura-zhoushan-aanloop-rastanura.geojson" \
    --been         "zee|zeeschip Ras Tanura-exportterminal → ZPC-kade Zhoushan (Perzische Golf → Straat Hormuz → Arabische Zee → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee)|26.6540,50.1648|30.3180,121.9600" \
    --marker "Abqaiq Plants (Saudi Aramco), Ghawar/Abqaiq-veldencomplex — olieveld/stabilisatiecomplex (kop van de leiding)|25.9400,49.6600" \
    --marker "Ras Tanura-exportterminal (Saudi Aramco) — tankenpark + T-steiger + Sea Island-fingerpier, laadplek|26.6540,50.1648" \
    --marker "ZPC (Zhejiang Petroleum & Chemical, Rongsheng-affiliate), Zhoushan Green Petrochemical Base, Dayushan-eiland — losplek/raffinage- en kraakcomplex, stoppunt|30.3180,121.9600" \
    --routebrief v2/design/routebrieven/olie-rastanura-zhoushan.md \
    --uit    v2/data/stroomroute-olie-rastanura-zhoushan.json \
    --stroom olie-rastanura-zhoushan \
    --titel  "Olie · Ras Tanura (Saoedi-Arabië) → Zhoushan (China)"
}

# ── olie · Corpus Christi-exportterminals (South Texas Gateway) → Maasvlakte Olie Terminal (Rotterdam)
# Routebrief: v2/design/routebrieven/olie-corpuschristi-rotterdam.md (LICHTE werkwijze M31)
# ⚠️ Eén been (zee): Amerikaanse schalie-ruwe olie (VLCC/Suezmax) rechtstreeks
#    kade → kade, Golf van Mexico → Straat van Florida → Noord-Atlantische
#    Oceaan → Nauw van Calais/Noordzee. Beide kades snappen ruim binnen de
#    25 km-norm op een MARNET-zeeknoop (Corpus Christi 4,87 km / zeeknoop
#    4843; Rotterdam 1,73 km / zeeknoop 6812) → geen haven-aanloop nodig.
# ⚠️ "Aannemelijk: aggregaatcijfers beide zijden, geen cargoniveau-bron" staat
#    in de beennaam/brief, niet in de lijnstijl — dit is een volledig gemeten
#    MARNET-zeebeen, geen stippel.
# ⚠️ Geen fase C/D/E (brief §6): geen bron benoemt welk deel van de MOT-aanvoer
#    specifiek uit Corpus Christi komt of welke raffinaderij (Pernis, …) de
#    Amerikaanse partij verwerkt — de brief stopt bij de poort van de MOT.
bak_olie_corpuschristi_rotterdam() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been         "zee|zeeschip Corpus Christi (South Texas Gateway) → Rotterdam (Maasvlakte Olie Terminal)|27.82677,-97.19447|51.97273,4.06243" \
    --marker "South Texas Gateway Terminal (Gibson Energy), Ingleside — exportterminal, representatief voor het Corpus Christi Ship Channel-complex, laadplek|27.82677,-97.19447" \
    --marker "Maasvlakte Olie Terminal (BP/Esso/Shell/TotalEnergies/Vopak/Aramco Overseas), Rotterdam — crude-importsteiger, losplek/stoppunt|51.97273,4.06243" \
    --routebrief v2/design/routebrieven/olie-corpuschristi-rotterdam.md \
    --uit    v2/data/stroomroute-olie-corpuschristi-rotterdam.json \
    --stroom olie-corpuschristi-rotterdam \
    --titel  "Olie · Corpus Christi (VS) → Rotterdam (Maasvlakte Olie Terminal)"
}

# ── kobalt · Moa Bay (Cuba) → Halifax → Fort Saskatchewan (mixed-sulfide, om de VS heen, niet actief)
# Routebrief: v2/design/routebrieven/kobalt-moa-fortsaskatchewan.md (lichte werkwijze M31)
# ⚠️ Eerste en enige Cubaans-Canadese as in de atlas — geen gedeelde geometrie
#    met een andere stroom mogelijk.
# ⚠️ b1 (zee, haven-aanloop Moa Bay) is een STIPPEL: de Punta Gorda-jetty ligt
#    75,7 km van de dichtstbijzijnde MARNET-zeeknoop, ruim boven de default
#    max-snap. `maak_havenaanloop.py` vond een pad over water (70,9 km, 49
#    punten, 0,00 km over land) — geen terugval nodig.
# ⚠️ b2 (zee) is de MARNET-route zeeknoop → kade, BEWUST OM DE VS HEEN
#    (sanctie-gevoelige route, brief §1/§2): Caribische Zee → Atlantische
#    Oceaan. Halifax-kade snapt binnen de default max-snap, dus geen tweede
#    haven-aanloop.
# ⚠️ b3 (spoor, 1-op-1-net, BAKE_SUFFIX=-raw) is de CN-hoofdlijn via Moncton —
#    bewust de Maritimes-omweg i.p.v. de kortere Maine-VS-kortsluiting
#    (sanctie-conform, brief §2/§4) — zes losse kop→via/via→staart-runs,
#    gesplitst op elke corridorkeuze (geen --via-vlag op de spoorrouter).
#    Som 4.821,1 km tegen de indicatieve ~5.000 km uit de brief (−3,6%, ruim
#    binnen ±15%); vier scherpe bochten (159,6–178,1°) op emplacementen/
#    rangeerknopen (Winnipeg-nadering, Edmonton-nadering) zijn kopmaak-plekken,
#    geen fout — komt overeen met de bochten die de handleiding op sporen
#    verwacht.
# ⚠️ `co-moa-laad` en `co-halifax-kade` zijn resp. ONZEKER/AANNEMELIJK (brief
#    §3/§7: geen bron bevestigt een laadbrug/kraan bij Punta Gorda, geen bron
#    noemt Richmond Terminals met naam voor Sherritt-lading) — dat staat in de
#    markernaam, niet in de lijnstijl.
# ⚠️ Geen fase D/E: de raffinaderij is het stoppunt (brief §6) — sinds
#    22-06-2026 gesloten, geen afzetmarkt gebrond voor toekomstige output.
bak_kobalt_moa_fortsaskatchewan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel-geojson "zee|haven-aanloop Moa Bay (schematisch, over water — MARNET reikt niet: 75,7 km)|$BEEN/kobalt-moa-fortsaskatchewan-aanloop-moa.geojson" \
    --been         "zee|zeeschip Moa Bay → Halifax (Caribische Zee → Atlantische Oceaan, bewust om de VS heen — sanctie-gevoelig)|21.1135,-74.4068|44.6735,-63.6032" \
    --been-geojson "spoor|trein Halifax → Moncton (CN-hoofdlijn/Intercolonial, kop van de Maritimes-omweg)|$BEEN/spoorroute-kobalt-moa-fortsaskatchewan-halifax-moncton.geojson" \
    --been-geojson "spoor|trein Moncton → Québec (CN-hoofdlijn, oeversprong Saint-Laurent bij Gare du Palais)|$BEEN/spoorroute-kobalt-moa-fortsaskatchewan-moncton-quebec.geojson" \
    --been-geojson "spoor|trein Québec → Winnipeg (CN-transcontinentale hoofdlijn, oostelijke → westelijke tak)|$BEEN/spoorroute-kobalt-moa-fortsaskatchewan-quebec-winnipeg.geojson" \
    --been-geojson "spoor|trein Winnipeg → Saskatoon (CN-hoofdlijn, CN Chappell Yard-rangeerknoop)|$BEEN/spoorroute-kobalt-moa-fortsaskatchewan-winnipeg-saskatoon.geojson" \
    --been-geojson "spoor|trein Saskatoon → Edmonton (CN-hoofdlijn, laatste corridorkeuze vóór de aftakking)|$BEEN/spoorroute-kobalt-moa-fortsaskatchewan-saskatoon-edmonton.geojson" \
    --been-geojson "spoor|trein Edmonton → Fort Saskatchewan-raffinaderij (kopse aansluiting, staart)|$BEEN/spoorroute-kobalt-moa-fortsaskatchewan-edmonton-fortsask.geojson" \
    --marker "co-moa-laad — Punta Gorda-aanlegsteiger, Bahía de Moa (Sherritt/GNC Moa JV, onzeker)|20.6372,-74.8549" \
    --marker "co-halifax-kade — Richmond Terminals, Halifax (overslag zee → spoor, aannemelijk)|44.6735,-63.6032" \
    --marker "Moncton — spoorstation/CN-junctie (via-punt corridorkeuze: Maritimes-omweg i.p.v. Maine-VS-kortsluiting)|46.0833,-64.7861" \
    --marker "Québec — Gare du Palais, oeversprong Saint-Laurent (via-punt corridorkeuze)|46.8178,-71.2139" \
    --marker "Winnipeg — Union Station (via-punt corridorkeuze, oost/west-splitsing)|49.8889,-97.1343" \
    --marker "Saskatoon — CN Chappell Yard (via-punt corridorkeuze, rangeerknoop)|52.1052,-106.7505" \
    --marker "Edmonton — CN-knoop vóór de aftakking (via-punt corridorkeuze)|53.5462,-113.4912" \
    --marker "co-fortsask-raffinaderij — Sherritt Metals Facility, Fort Saskatchewan (losplek/raffinaderij, gesloten, stoppunt)|53.7198,-113.1904" \
    --routebrief v2/design/routebrieven/kobalt-moa-fortsaskatchewan.md \
    --uit    v2/data/stroomroute-kobalt-moa-fortsaskatchewan.json \
    --stroom kobalt-moa-fortsaskatchewan \
    --titel  "Kobalt · Moa Bay (Cuba) → Halifax → Fort Saskatchewan (Canada)"
}

# ── uranium · Inkai (Kazachstan, ISR-mijn) → Zhanatas → Aktau → Alyat/Bakoe → Tbilisi → Poti (Georgië)
# Routebrief: v2/design/routebrieven/uranium-inkai-poti.md (LICHTE werkwijze M31)
# ⚠️ b1 (truck) is een STIPPEL: `maak_stroombeen_weg.py --profiel
#    uranium-inkai-poti-inkai-zhanatas` (venster 75 km, geen via-punten) gaf
#    "geen wegpad tussen punt 0 en 1" — geen doorlopende OSM-weg over de
#    ~290 km woestijnsteppe Suzak-district → Zjambyl-oblast. Rechte stippel,
#    geen tweede poging.
# ⚠️ b2 (spoor, 1-op-1-net, BAKE_SUFFIX=-raw) = 2.407,0 km, verhouding 1,62 —
#    GEEN gepubliceerde lengte om tegen te toetsen (brief §7), dus dit is
#    nieuwe informatie. Eén omkering (179,7°, boogstraal ~118 m) bij
#    47,8187/59,6491 = Shalkar, een echte spoorknoop op de Trans-Aral-lijn
#    (Aral → Shalkar → Beyneu) — kopmaak op het net, geen verzonnen sluiproute.
#    Het eerste deel van de route dipt zuidwaarts naar de Shu/Turkestan-
#    mainline vóór hij westwaarts langs Kyzylorda/Aral/Shalkar/Beyneu naar
#    Mangystau/Aktau buigt; geografisch aannemelijk, geen bron noemt de
#    tussenstations (brief §7).
# ⚠️ b3 (zee) = 468,1 km, al vooraf getoetst (hecht_marnet.py) — Aktau-kade
#    snapt op 7,4 km (< 25 km-norm, automatisch), Alyat-kade op 49,4 km
#    (> 25 km-norm) → het hoofdzeebeen eindigt op de MARNET-zeeknoop bij Alyat
#    (40,21240/49,93290), niet op de kade zelf.
# ⚠️ b2b (haven-aanloop Aktau, LAR-586, 2026-09-28) is een RECHTE STIPPEL: de
#    7,4 km-snap liet een naad van 6,8 km (boven de 5 km-norm, §5) tussen spoor
#    en zeebeen; `maak_havenaanloop.py` liep vast op `timeout 300` (exit 124) —
#    geen tweede poging, zoals bij Alyat.
# ⚠️ b3b (haven-aanloop Alyat) is een RECHTE STIPPEL: `maak_havenaanloop.py`
#    liep vast op `timeout 300` (exit 124) — geen tweede poging, direct
#    gestippeld per de bak-aanwijzing in de brief.
# ⚠️ b4 (spoor, 1-op-1-net) is TWEE RUNS met het Tbilisi-via-punt (geen --via-
#    vlag op de spoorrouter): Alyat/Bakoe → Tbilisi (465,1 km) + Tbilisi →
#    Poti (303,1 km) = 768,2 km tegen de TRACECA-schatting van 800 km
#    (Poti-Baku Container Block Train, −4,0%, ruim binnen ±15%). Zonder het
#    via-punt kan een vrije Dijkstra bij Tbilisi de Bakoe–Tbilisi–Kars-lijn
#    (Turkije) nemen i.p.v. de doorgaande lijn naar Poti.
# ⚠️ Geen fase D/E (brief §5/§6): Poti is een zuiver overslagpunt (spoor →
#    zee), geen verwerkingsknoop; het vervolg naar Montreal/Cameco Blind
#    River valt buiten deze stroom (brief §1/§6).
bak_uranium_inkai_poti() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|yellowcake Inkai MPP → Zhanatas-spoorstation (schematisch — geen doorlopende weg in OSM; woestijnweg Suzak-district → Zjambyl-oblast, aannemelijk: één bron)|45.2855,67.5255|43.5610,69.7260" \
    --been-geojson "spoor|trein Zhanatas-spoorstation → Aktau-kade (Trans-Kazachse lijn via Shu-knoop → Kyzylorda-regio → Aral → Shalkar → Beyneu → Mangystau-tak; 1-op-1-net, geen gepubliceerde lengte)|$BEEN/spoorroute-uranium-inkai-poti-zhanatas-aktau.geojson" \
    --stippel      "zee|haven-aanloop Aktau (schematisch — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|43.6005,51.2287|43.61220,51.13860" \
    --been         "zee|zeeschip Aktau-kade → Alyat/Bakoe (Kaspische Zee-oversteek, TITR/Middle Corridor)|43.6005,51.2287|40.21240,49.93290" \
    --stippel      "zee|haven-aanloop Alyat/Bakoe (schematisch, over water — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|40.21240,49.93290|39.9764,49.4408" \
    --been-geojson "spoor|trein Alyat/Bakoe-kade → Tbilisi (Bakoe–Tbilisi–Poti-lijn, via-punt corridorkeuze t.o.v. de Bakoe–Tbilisi–Kars-lijn)|$BEEN/spoorroute-uranium-inkai-poti-alat-tbilisi.geojson" \
    --been-geojson "spoor|trein Tbilisi → Poti-kade (Bakoe–Tbilisi–Poti-lijn, doorgaande tak na de Kars-splitsing)|$BEEN/spoorroute-uranium-inkai-poti-tbilisi-poti.geojson" \
    --marker "Inkai MPP — hoofdverwerkingsfabriek, JV Inkai (Kazatomprom 60%/Cameco 40%) — laadplek|45.2855,67.5255" \
    --marker "Zhanatas-spoorstation, Zjambyl-oblast — overslag truck → spoor|43.5610,69.7260" \
    --marker "Aktau-zeehaven (Kazmortransflot-terrein) — overslag spoor → zee|43.6005,51.2287" \
    --marker "Bakı Dəniz Ticarət Limanı, Alyat (Qaradağ) — overslag zee → spoor|39.9764,49.4408" \
    --marker "Poti Sea Port, Georgië — overslag spoor → zee, stoppunt|42.1550,41.6560" \
    --routebrief v2/design/routebrieven/uranium-inkai-poti.md \
    --uit    v2/data/stroomroute-uranium-inkai-poti.json \
    --stroom uranium-inkai-poti \
    --titel  "Uranium · Inkai (Kazachstan) → Aktau → Bakoe → Poti (Georgië)"
}

# ── olie · Primorsk (Rusland) → Sikka Marine Terminal → Jamnagar-raffinaderij (India, Rusland-omleiding)
# Routebrief: v2/design/routebrieven/olie-primorsk-jamnagar.md (LICHTE werkwijze M31)
# ⚠️ b1 (zee): beide uiteinden liggen BUITEN de 25 km-norm van een MARNET-
#    zeeknoop (Primorsk 31,0 km, Sikka 40,7 km) — twee haven-aanlopen nodig.
#    Primorsk-aanloop is een RECHTE STIPPEL: maak_havenaanloop.py liep vast op
#    timeout 300 (exit 124) — geen tweede poging. Sikka-aanloop lukte wél
#    (43,5 km over water, omwegfactor 1,068) → --stippel-geojson.
# ⚠️ b2 (leiding) is een RECHTE STIPPEL: geen enkele OSM man_made=pipeline op
#    het Sikka→Jamnagar-tracé (Overpass-check, brief §7/§8[16]) — hemelsbreed
#    16,4 km tussen de twee ankers; het ontwerp noemde ~50 km, in geen bron
#    terugvonden (bevinding, niet dichtgetrokken).
# ⚠️ Geen fase D/E (brief §6): de brief stopt bewust bij het Jamnagar-
#    raffinaderijcomplex; de SEZ/DTA-nuance (sinds 20-11-2025) staat alleen in
#    de tekst, geen apart anker (conform de lichte werkwijze).
bak_olie_primorsk_jamnagar() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "zee|haven-aanloop Primorsk-exportterminal (schematisch — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|60.3340,28.7090|60.59370,28.50130" \
    --been         "zee|zeeschip Primorsk-zeeknoop → Sikka-zeeknoop (Oostzee → Deense Straten → Noordzee → Golf van Biskaje → Gibraltar → Middellandse Zee → Suez → Rode Zee → Bab-el-Mandeb → Arabische Zee)|60.59370,28.50130|22.57340,69.44460" \
    --stippel-geojson "zee|haven-aanloop Sikka Marine Terminal (schematisch, over water — MARNET reikt hier niet: 40,7 km)|$BEEN/olie-primorsk-jamnagar-aanloop-sikka.geojson" \
    --stippel      "leiding|eigen crude-pijpleiding Sikka-terminal → Jamnagar-raffinaderij (schematisch — geen OSM-way, geen man_made=pipeline gevonden)|22.4990,69.8330|22.3500,69.8500" \
    --marker "Primorsk-exportterminal (Transneft, BPS-terminus) — laadplek/kade|60.3340,28.7090" \
    --marker "Reliance/SPTL Marine Terminal Sikka — overslag zee → leiding|22.4990,69.8330" \
    --marker "Jamnagar-raffinaderijcomplex (Reliance, SEZ+DTA) — losplek/raffinaderij, stoppunt|22.3500,69.8500" \
    --routebrief v2/design/routebrieven/olie-primorsk-jamnagar.md \
    --uit    v2/data/stroomroute-olie-primorsk-jamnagar.json \
    --stroom olie-primorsk-jamnagar \
    --titel  "Olie · Primorsk (Rusland) → Sikka → Jamnagar (India)"
}

# ── kobalt · KFM Kisanfu-plant → Kasumbalesa → Nakonde/Tunduma → Dar es Salaam → Ningbo (hydroxide, volledig truck)
# Routebrief: v2/design/routebrieven/kobalt-kisanfu-daressalaam.md (LICHTE werkwijze M31)
# ⚠️ Eigendom gecorrigeerd (brief §7): CMOC Group 71,25% / CATL 23,75% /
#    DRC-staat 5% (niet 75%/25% zoals het ontwerp noemde).
# ⚠️ b1 (Kisanfu → Kasumbalesa) is +24,2% BOVEN de eigen schatting (360,3 km
#    tegen ~290 km hemelsbreed-keten) — buiten ±15%, bevinding, niet
#    dichtgetrokken: een reële weg is altijd langer dan een hemelsbrede
#    via-puntenketen, en er is geen gepubliceerde bronlengte om tegen te
#    toetsen (brief §2). Via-punten Likasi/Lubumbashi/Kasumbalesa hergebruikt
#    uit koper-kolwezi-durban.md §3/§4.
# ⚠️ b2 (Kasumbalesa → Nakonde/Tunduma) is -38,6% ONDER de gepubliceerde
#    schatting (1.075,2 km tegen ~1.750 km) — buiten ±15%, bevinding: de eigen
#    hemelsbreed-keten (934,5 km) geeft een omwegfactor van 1,15, wat
#    plausibel is voor een hoofdweg; de "~1.750 km" uit de brief (afgeleid via
#    "Ndola–Tunduma ≈1.900 km minus Kasumbalesa–Ndola") lijkt de onjuiste
#    schatting, niet de gemeten weg. Niet dichtgetrokken.
# ⚠️ b3 (Nakonde/Tunduma → Dar es Salaam) EINDIGT OP EEN HAVENPOORT, NIET OP
#    DE KADE: het interne wegennet van Container Terminal II is in OSM een
#    geïsoleerd eiland van 34 knopen, 0,355 km van het doorgaande wegnet, geen
#    gedeelde vertex (gemeten met een component-scan op de gescande graaf).
#    Dat laatste stukje is hier een stippel (emplacement/havenpoort — net
#    reikt niet, bakhandleiding §2). 930,1 km tegen ~950 km = -2,1% [OK].
# ⚠️ b4 (zee): co-dar-kade snapt binnen de --max-snap-norm (zeeknoop 5310,
#    20,9 km < 25 km) maar hecht_marnet plakt géén stub — de eerste bake gaf
#    een naad van 20,9 km tussen de havenpoort-stippel en het zeebeen (buiten
#    de ≤5 km-norm). `maak_havenaanloop.py` liep vast op timeout 300 (exit
#    124) — geen tweede poging, terugval op een RECHTE stippel kade→zeeknoop.
#    De Ningbo-aanloop (zeeknoop → co-ningbo-kade, 11,64 km) is een LETTERLIJKE
#    KOPIE van kobalt-tfm-quzhou b2a — geen tweede zeeknoop-lookup/aanloop-run.
# ⚠️ `co-nakonde-tunduma-grens` blijft AANNEMELIJK (brief §3): geen los
#    aanwijsbaar grensgebouw op de satellietpas, alleen de doorgaande hoofdweg
#    door de tweelingstad. Bestemming Ningbo Beilun blijft AANNEMELIJK
#    (generieke China-bestemming, geen mijn-specifieke bron). Geen fase D/E
#    (brief §6): geen bron koppelt dit hydroxide aan een met naam genoemde
#    Chinese raffinaderij.
bak_kobalt_kisanfu_daressalaam() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|kobalthydroxide KFM Kisanfu-plant → Kasumbalesa (mijnweg → RN39 → RN39/RN1 Likasi–Lubumbashi, gedeeld eerste stuk met TFM/KCC)|$BEEN/kobalt-kisanfu-daressalaam-weg-kisanfu-kasumbalesa.geojson" \
    --been-geojson "truck|kobalthydroxide Kasumbalesa → Nakonde/Tunduma (T2/Great North Road via Ndola–Kapiri Mposhi–Mpika–Isoka)|$BEEN/kobalt-kisanfu-daressalaam-weg-kasumbalesa-nakonde.geojson" \
    --been-geojson "truck|kobalthydroxide Nakonde/Tunduma → Dar es Salaam-havenpoort (T1 Centraal Corridor/TANZAM via Mbeya–Iringa–Morogoro)|$BEEN/kobalt-kisanfu-daressalaam-weg-nakonde-daressalaam.geojson" \
    --stippel      "truck|havenpoort → Container Terminal II-kade (emplacement, intern havenwegennet niet in het net — gemeten 0,355 km)|-6.840496,39.293780|-6.8394,39.2968" \
    --stippel      "zee|haven-aanloop Dar es Salaam (schematisch — maak_havenaanloop.py timeout 300 s, geen tweede poging; rechte lijn kade→zeeknoop 5310, 20,9 km)|-6.8394,39.2968|-6.6537,39.3256" \
    --been         "zee|zeeschip Dar es Salaam → Ningbo (kobalthydroxide; bestemming Huayou/generieke China-markt, aannemelijk)|-6.8394,39.2968|29.9758,121.9736" \
    --stippel-geojson "zee|haven-aanloop Ningbo Beilun (schematisch, over water — MARNET reikt niet; letterlijke kopie van kobalt-tfm-quzhou b2a)|$BEEN/kobalt-tfm-quzhou-aanloop-ningbo.geojson" \
    --marker "KFM – Kisanfu Processing Plant (CMOC Kisanfu Mining SARL) — laadplek (anker, bron-gelegd)|-10.7630,25.9983" \
    --marker "Kasumbalesa grenspost — DRC/Zambia (hergebruikt anker)|-12.2658,27.7959" \
    --marker "Nakonde (ZM) / Tunduma (TZ) one-stop grenspost (aannemelijk)|-9.3208,32.7612" \
    --marker "Dar es Salaam Port, Container Terminal II (Berth 8-11), Kurasini — overslag truck → container → zeeschip|-6.8394,39.2968" \
    --marker "Beilun Container Terminal Phase 2, Ningbo-Zhoushan — overslag zeeschip → onbekend vervolg (stoppunt, hergebruikt anker)|29.9353,121.8695" \
    --routebrief v2/design/routebrieven/kobalt-kisanfu-daressalaam.md \
    --uit    v2/data/stroomroute-kobalt-kisanfu-daressalaam.json \
    --stroom kobalt-kisanfu-daressalaam \
    --titel  "Kobalt · KFM Kisanfu → Kasumbalesa → Dar es Salaam → Ningbo (hydroxide)"
}

# ── uranium · McArthur River-mijn/Key Lake-mill → Blind River → Port Hope → BWXT Toronto → BWXT Peterborough
# Routebrief: v2/design/routebrieven/uranium-mcarthurriver-porthope.md (LICHTE werkwijze M31)
# Vijf benen, alle truck, extract "canada" — de CANDU-uitzondering: natuurlijk
# (onverrijkt) uraan, geen verrijkingsstap.
# ⚠️ b4+b5 zijn een AFWIJKING op het oorspronkelijke ketenontwerp (dat één been
#    Port Hope → Peterborough gaf, "aannemelijk: één bron"). Onderzoek (drie
#    onafhankelijke bronnen, brief §1) toont een tussenstap via BWXT Toronto
#    (pelletpers); Toronto ligt zuidwestelijk van beide, dus de lijn maakt een
#    zichtbare lus/driehoek — dat is correct, geen bakfout.
# ⚠️ b2 CORRIGEERT DE BRIEF OP TWEE PUNTEN (bak-aanwijzing week af van de OSM-
#    werkelijkheid, geen coördinaat verzonnen — beide correcties op het
#    gemeten OSM-net/Wikipedia, zie de kop van het profiel in
#    maak_stroombeen_weg.py):
#    (1) het via-punt "Points North Landing" (Hwy 905, 58.27,-104.08) heeft
#        géén wegverbinding met Hwy 914/Key Lake — Sask. Hwy 914 loopt in OSM
#        van de mijnen zuidwaarts tot een knooppunt met Hwy 165 ten zuiden van
#        Pinehouse (Wikipedia bevestigt: "begins at Highway 165 south of
#        Pinehouse … does not intersect with any provincially-owned highways
#        between Highway 165 and Key Lake Mine"). Via-punt vervangen door dat
#        Hwy 165/914-knooppunt (55.2348,-106.7898, exact OSM-eindpunt).
#    (2) Thunder Bay → Sault Ste. Marie sneed over Lake Superior heen (geen
#        wegpad binnen het venster van 90 km om de rechte lijn); Wawa
#        (Hwy 17-knooppunt, Nominatim-gelegd) toegevoegd als extra via-punt.
# ⚠️ Geen stippels: alle vijf benen zijn eigen/openbare weg met een gepubliceerd
#    of goed beargumenteerd km-cijfer; het net reikt overal tot de zes ankers.
bak_uranium_mcarthurriver_porthope() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|uraanconcentraat McArthur River-mijn → Key Lake-mill (eigen mijnweg, Athabasca-bekken)|$BEEN/uranium-mcarthurriver-porthope-weg-mcarthurriver-keylake.geojson" \
    --been-geojson "truck|uraanconcentraat Key Lake-mill → Blind River-raffinaderij (Hwy 914 → 165 → 2 → 16 (Yellowhead) → Trans-Canada Hwy 1/17, via Pinehouse–Saskatoon–Winnipeg–Wawa–Sault Ste. Marie; correctie op de brief, zie kop)|$BEEN/uranium-mcarthurriver-porthope-weg-keylake-blindriver.geojson" \
    --been-geojson "truck|uraanconcentraat/UO3 Blind River-raffinaderij → Port Hope Conversion Facility (Hwy 17, Sault Ste. Marie–Sudbury–Parry Sound–Barrie–Toronto-omleiding)|$BEEN/uranium-mcarthurriver-porthope-weg-blindriver-porthope.geojson" \
    --been-geojson "truck|UO2-poeder Port Hope Conversion Facility → BWXT Toronto (pelletpers) (Hwy 401)|$BEEN/uranium-mcarthurriver-porthope-weg-porthope-bwxttoronto.geojson" \
    --been-geojson "truck|CANDU-pellets BWXT Toronto (pelletpers) → BWXT Peterborough (bundelfabriek) (Hwy 401 → Hwy 115/7; afwijking op het ontwerp, zie kop)|$BEEN/uranium-mcarthurriver-porthope-weg-bwxttoronto-bwxtpeterborough.geojson" \
    --marker "McArthur River-mijn (Cameco 70% / Orano 30%), Athabasca-bekken|57.7626,-105.0508" \
    --marker "Key Lake-mill (Cameco), Athabasca-bekken|57.2130,-105.6740" \
    --marker "Blind River Refinery (Cameco), 328 Eldorado Road|46.1810,-83.0174" \
    --marker "Port Hope Conversion Facility (Cameco), 1 Eldorado Place|43.9437,-78.2955" \
    --marker "BWXT Nuclear Energy Canada — Toronto, 1025 Lansdowne Avenue|43.6679,-79.4466" \
    --marker "BWXT Nuclear Energy Canada — Peterborough, 1160 Monaghan Road|44.2955,-78.3308" \
    --routebrief v2/design/routebrieven/uranium-mcarthurriver-porthope.md \
    --uit    v2/data/stroomroute-uranium-mcarthurriver-porthope.json \
    --stroom uranium-mcarthurriver-porthope \
    --titel  "Uranium · McArthur River/Key Lake → Blind River → Port Hope → BWXT Peterborough (Canada)"
}

# ── lithium · Albemarle Silver Peak (Clayton Valley, Nevada) → Tesla Gigafactory Nevada (TRIC)
# Routebrief: v2/design/routebrieven/lithium-silverpeak-mccarran.md (LICHTE werkwijze M31 golf 2)
# ⚠️ ÉÉN BEEN, ALLEEN TRUCK — geen zee/spoor/leiding/binnenvaart, geen
#    haven-aanloop nodig: dit is de enige volledig binnenlandse as van de
#    atlas (geen zee, geen grens).
# ⚠️ GEEN BEVESTIGDE LEVERRELATIE (brief §7/§1): geen bron koppelt Silver
#    Peak-carbonaat specifiek aan Gigafactory Nevada — "aannemelijke
#    bestemming" (kortste, meest voor de hand liggende regionale stroom),
#    niet een gedocumenteerd offtake-contract. De weg zelf is een gewone
#    doorgaande verharde route (US-95/US-95A/I-80), geen bijzonderheid.
#    Doorgetrokken, niet gestippeld (werkwijze §7: stippel betekent
#    uitsluitend "hier reikt het net niet").
# ⚠️ GEEN GEPUBLICEERDE WEG-KM: ontwerpschatting 300-330 km, gebruikt als
#    middenwaarde 315 voor de lengtetoets. Gemeten weggeometrie 346,3 km
#    (+9,9%, binnen ±15%).
# ⚠️ FASE D/E VERVALLEN (brief §6): Panasonic produceert cellen op hetzelfde
#    TRIC-terrein als celfabricage-partner, geen aparte site; geen bron
#    koppelt een celtype/eindklant specifiek aan Silver Peak-carbonaat.
bak_lithium_silverpeak_mccarran() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|lithiumcarbonaat Albemarle Silver Peak → Tesla Gigafactory Nevada (NV-265 → US-95 N via Tonopah/Mina/Hawthorne/Schurz → US-95A via Silver Springs/Fernley → I-80 W; aannemelijke bestemming, geen offtake-contract)|$BEEN/lithium-silverpeak-mccarran-weg-silverpeak-gigafactory.geojson" \
    --marker "Albemarle Silver Peak — Clayton Valley-brineoperatie, Esmeralda County (laadplek)|37.7693,-117.5768" \
    --marker "Tesla Gigafactory Nevada / Gigafactory 1, TRIC, Storey County (stoppunt, Panasonic celfabricage op hetzelfde terrein)|39.5403926,-119.4390524" \
    --routebrief v2/design/routebrieven/lithium-silverpeak-mccarran.md \
    --uit    v2/data/stroomroute-lithium-silverpeak-mccarran.json \
    --stroom lithium-silverpeak-mccarran \
    --titel  "Lithium · Albemarle Silver Peak → Tesla Gigafactory Nevada (Nevada, VS)"
}

# ── kolen · Kriel Colliery (Mpumalanga) → Ermelo → Vryheid → Empangeni → Richards Bay Coal Terminal → Port Qasim Power Project (Pakistan)
# Routebrief: v2/design/routebrieven/kolen-ermelo-portqasim.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (spoor, 1-op-1-net, BAKE_SUFFIX=-raw, extract zuid-afrika) is VIER
#    losse runs op de corridorkeuze uit de brief (kop→Ermelo→Vryheid→
#    Empangeni→RBCT-kade, geen --via-vlag op de spoorrouter): 137,4 + 228,4 +
#    215,7 + 37,0 = 618,5 km totaal. Ermelo→RBCT alleen (228,4+215,7+37,0 =
#    481,1 km) ligt -17,1% ONDER de gepubliceerde 580 km (Ermelo→Richards Bay,
#    Wikipedia Class 19E) — buiten de ±15%-norm. De brief verwachtte juist een
#    POSITIEF verschil (Kriel→Ermelo-stuk niet apart gepubliceerd, dus bovenop
#    de 580 km); de bake laat het omgekeerde zien op het Ermelo→RBCT-deel.
#    Bevinding, geen via-punt bijgeschoven om het getal te halen — zie §9.
# ⚠️ Kop-snap Kriel: 14,30 km tussen het mijnanker en het hoofdnet (component
#    47.640 km) — geen doorlopende OSM-spoorlijn tot in de dagbouwput zelf; de
#    brief noemt de mijn-eigen railaansluiting al als "buiten deze brief om"
#    (§4, via-punt 1). Geen kop-stippel toegevoegd: de brief geeft geen apart
#    mijnspoor-anker, het spoorbeen begint op de gesnapte hoofdnet-knoop.
# ⚠️ b2 (zee) = MARNET-route zeeknoop 5200 → zeeknoop 4085 — BEIDE kades
#    liggen ruim boven de 25 km max-snap én de 5 km-LAR-586-norm (RBCT
#    94,2 km, Port Qasim 40,0 km) → BEIDE zijden krijgen een haven-aanloop-
#    stippel (maak_havenaanloop.py, timeout 300, geen tweede poging nodig —
#    beide trappenreeksen gaven meteen een geslaagd pad):
#      - RBCT-aanloop: 101,5 km, omwegfactor 1,078, 0,89 km land (uitsluitend
#        aan het kade-uiteinde, geen landkruising midden op de lijn).
#      - Port Qasim-aanloop: 43,6 km, omwegfactor 1,089, 12,00 km land
#        (uitsluitend aan het kade-uiteinde — Port Qasim ligt landinwaarts in
#        een riviermonding, vandaar het hogere aandeel; geen landkruising
#        midden op de lijn).
#    maak_havenaanloop.py schrijft altijd in --van→--naar-volgorde; beide
#    geojson's zijn ná generatie handmatig op reisvolgorde gezet (RBCT-aanloop
#    kade→knoop, Port Qasim-aanloop knoop→kade — de coördinaten zelf zijn
#    ongewijzigd, alleen de puntvolgorde is omgedraaid).
bak_kolen_ermelo_portqasim() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Kriel Colliery → Ermelo (kop van de gepubliceerde Coalink-lijn)|$BEEN/spoorroute-kolen-ermelo-portqasim-kriel-ermelo.geojson" \
    --been-geojson "spoor|trein Ermelo → Vryheid (Coalink-lijn, geüpgraded segment)|$BEEN/spoorroute-kolen-ermelo-portqasim-ermelo-vryheid.geojson" \
    --been-geojson "spoor|trein Vryheid → Empangeni (Coalink-lijn, nieuwer segment, 210 km/10,5 km tunnels/67 bruggen)|$BEEN/spoorroute-kolen-ermelo-portqasim-vryheid-empangeni.geojson" \
    --been-geojson "spoor|trein Empangeni → Richards Bay Coal Terminal (laatste kusttak)|$BEEN/spoorroute-kolen-ermelo-portqasim-empangeni-rbct.geojson" \
    --stippel-geojson "zee|haven-aanloop RBCT (schematisch, over water — kade 94,2 km van de MARNET-zeeknoop)|$BEEN/kolen-ermelo-portqasim-aanloop-rbct.geojson" \
    --been         "zee|zeeschip Richards Bay → Port Qasim (Mozambiekkanaal → Indische Oceaan → Arabische Zee, geen Malakka)|-28.4494,32.9205|24.8174,66.9757" \
    --stippel-geojson "zee|haven-aanloop Port Qasim (schematisch, over water — kade 40,0 km van de MARNET-zeeknoop)|$BEEN/kolen-ermelo-portqasim-aanloop-portqasim.geojson" \
    --marker "Kriel Colliery, Seriti Coal (Pty) Ltd, open dagbouw bij Kriel, Mpumalanga (Coalink-cluster, representatief; mijnkeuze aannemelijk) — laadplek|-26.2258,29.1360" \
    --marker "Ermelo — kop van de gepubliceerde Coalink-lijn (via-punt corridorkeuze)|-26.5333,29.9833" \
    --marker "Vryheid — lijnknoop tussen de twee bouwsegmenten (via-punt corridorkeuze)|-27.7705,30.7886" \
    --marker "Empangeni — vóór de laatste kusttak naar RBCT (via-punt corridorkeuze)|-28.7461,31.8972" \
    --marker "Richards Bay Coal Terminal, laadkade/stockyard — overslag spoor → zee|-28.8187,32.0523" \
    --marker "Port Qasim Power Project (CPEC), kolenkade aan het centraleterrein — losplek/stoppunt|24.7808,67.3701" \
    --routebrief v2/design/routebrieven/kolen-ermelo-portqasim.md \
    --uit    v2/data/stroomroute-kolen-ermelo-portqasim.json \
    --stroom kolen-ermelo-portqasim \
    --titel  "Kolen · Mpumalanga (Kriel/Ermelo) → Richards Bay → Port Qasim (Pakistan)"
}

# ── kolen · Mount Arthur (Muswellbrook, Hunter Valley) → Newcastle → Hekinan (JERA, Japan)
# Routebrief: v2/design/routebrieven/kolen-muswellbrook-hekinan.md (lichte werkwijze M31 golf 2)
# ⚠️ Mijnkeuze is AANNEMELIJK (brief §7): Mount Arthur is de grootste NSW-mijn
#    met een bronvermeld spoorbeen naar Newcastle, maar geen bron legt één
#    specifieke Newcastle→Hekinan-lading bij deze mijn alleen vast
#    (blend-praktijk Hunter Valley Coal Chain) — dat staat in de kop-markernaam,
#    niet in de lijnstijl.
# ⚠️ b1 = VIER spoorruns op het 1-op-1-net (BAKE_SUFFIX=-raw, extract australie),
#    kop→via/via→via/via→staart: Mount Arthur → Muswellbrook 25,6 km +
#    Muswellbrook → Singleton 49,1 km + Singleton → Maitland-junctie 46,6 km +
#    Maitland-junctie → PWCS Kooragang Island 29,9 km = 151,2 km tegen de
#    brief-schatting ~140 km (+8,0%, binnen ±15%).
# ⚠️ Het eerste segment snapt 4,37 km van het Mount Arthur-anker (de mijn-
#    laadinfrastructuur ligt niet op het 1-op-1-net, Goonyella-klasse) →
#    stippel "laadspoor mijn → hoofdspoor". Datzelfde segment maakt een grote
#    lus (25,6 km over 32 edges tegen 8,2 km grootcirkel, verhouding 3,12) met
#    één OMKERING (175,7°, boogstraal ~102 m bij -32.34920,150.99260) — een
#    kopmaak-/marshalling-lus rond de kolenladingsfaciliteiten ten oosten van
#    de mijn, geen via-punt bijgeschoven om het getal te verlagen (bevinding,
#    niet dichtgetrokken). De PWCS-kade-aansluiting snapt 0,41 km — binnen de
#    marker-norm, geen aparte stippel nodig (anders dan Goonyella's HPCT).
# ⚠️ b2 = zee, BEIDE kanten een haven-aanloop (bakhandleiding §2, LAR-586
#    2026-09-28): Newcastle-kade ligt 46,5 km van zeeknoop 2707
#    (-33,00000/152,25000, > 25 km max-snap) → `--been zee` gebruikt de
#    ZEEKNOOP als beginpunt, `maak_havenaanloop.py` vond een pad over water
#    (49,8 km, 2,81 km over land aan het kade-uiteinde — de kustkorrel, geen
#    fout) als stippel-geojson vóór het zeebeen. Hekinan-kade ligt 23,6 km van
#    zeeknoop 5771 (34,64220/137,01940, < 25 km max-snap, dus binnen het
#    automatische snapbereik) → `--been zee` gebruikt de KADE rechtstreeks als
#    eindpunt, met een tweede stippel-geojson (24,9 km, 0,00 km over land) ná
#    het zeebeen om de resterende naad te dichten. MARNET kiest zelf de route
#    (Tasmanzee → westelijke Pacific, geen Zuid-Chinese-Zee-doorsteek
#    afgedwongen — corridornoot, geen via-punt).
# ⚠️ Geen fase D/E (brief §6): de kolen wordt bij Hekinan verstookt, geen
#    fysiek product om verder te volgen — stoppunt.
bak_kolen_muswellbrook_hekinan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "spoor|laadspoor Mount Arthur-mijn → hoofdspoor (mijnemplacement niet in het 1-op-1-net, ~4,4 km)|-32.3340,150.8530|-32.3344,150.8995" \
    --been-geojson "spoor|trein Mount Arthur-mijn → Muswellbrook (Main Northern-lijn, marshalling-lus bij de laadfaciliteiten)|$BEEN/spoorroute-kolen-muswellbrook-hekinan-arthur-muswellbrook.geojson" \
    --been-geojson "spoor|trein Muswellbrook → Singleton (Main Northern-lijn)|$BEEN/spoorroute-kolen-muswellbrook-hekinan-muswellbrook-singleton.geojson" \
    --been-geojson "spoor|trein Singleton → Maitland-junctie (Main Northern-lijn, splitst hier van de North Coast-lijn)|$BEEN/spoorroute-kolen-muswellbrook-hekinan-singleton-maitland.geojson" \
    --been-geojson "spoor|trein Maitland-junctie → PWCS Kooragang Island (Port of Newcastle)|$BEEN/spoorroute-kolen-muswellbrook-hekinan-maitland-newcastle.geojson" \
    --stippel-geojson "zee|haven-aanloop Newcastle (schematisch, over water — kade 46,5 km van de MARNET-zeeknoop)|$BEEN/kolen-muswellbrook-hekinan-aanloop-newcastle.geojson" \
    --been         "zee|zeeschip Newcastle-zeeknoop → Hekinan Thermal Power Station (Tasmanzee → westelijke Stille Oceaan, geen Zuid-Chinese-Zee-doorsteek)|-33.00000,152.25000|34.8478,136.9535" \
    --stippel-geojson "zee|haven-aanloop Hekinan (schematisch, over water — kade 23,6 km van de MARNET-zeeknoop)|$BEEN/kolen-muswellbrook-hekinan-aanloop-hekinan.geojson" \
    --marker "Mount Arthur coal mine (BHP), Muswellbrook — laadplek (aannemelijk: blend uit het Hunter Valley-cluster)|-32.3340,150.8530" \
    --marker "Port Waratah Coal Services, Kooragang Island, Port of Newcastle — overslag spoor → zee|-32.8785,151.7735" \
    --marker "Hekinan Thermal Power Station (JERA), kolenkade — losplek, stoppunt|34.8478,136.9535" \
    --routebrief v2/design/routebrieven/kolen-muswellbrook-hekinan.md \
    --uit    v2/data/stroomroute-kolen-muswellbrook-hekinan.json \
    --stroom kolen-muswellbrook-hekinan \
    --titel  "Kolen · Mount Arthur (Muswellbrook) → Newcastle → Hekinan (Japan)"
}

# ── zilver · Zakład Wzbogacania Rud "Polkowice" (KGHM) → Huta Miedzi "Głogów"-smelter (bijproduct-zilver)
# Routebrief: v2/design/routebrieven/zilver-lubin-glogow.md (lichte werkwijze M31 golf 2)
# ⚠️ Eén been (b1, fase A, spoor, 1-op-1-net BAKE_SUFFIX=-raw, extract polen,
#    --keerstraf=5): gemeten 59,5 km tegen hemelsbreed 23,1 km — verhouding
#    2,57, ver buiten ±15% maar bewust NIET dichtgetrokken (bevinding, zie
#    §9). GEEN routerfout: een onafhankelijke webbron (zoekopdracht "linia
#    kolejowa Polkowice Głogów KGHM Główny Ciąg Technologiczny", netTG.pl/
#    Rynek Kolejowy/Envirail) bevestigt dat het huidige KGHM-treinverkeer
#    Polkowice → Głogów alleen over de bestaande, tamelijk omslachtige route
#    via Lubin en Rudna Gwizdanów loopt (bevestigd: het traject snijdt
#    51,5291/16,2810 = Rudna Gwizdanów-station, Nominatim-gelegd); een
#    nieuwe rechtstreekse lijn (Lubin-Polkowice-Głogów incl. uitbreiding van
#    lijn 289 Legnica-Lubin-Rudna Gwizdanów) is pas in planfase, niet
#    aangelegd. De 23,2 km "Główny Ciąg Technologiczny" uit de brief is dus
#    de hemelsbrede afstand, niet de echte spoorcorridor.
# ⚠️ KEERSTRAF VERLAAGD VAN DE DEFAULT (25) NAAR 5, MET REDEN: op de default
#    (en ook op 100, dus geen straf-toeval) koos de vrije Dijkstra een
#    14 km-omweg voorbij Głogów naar een doodlopende stomp bij Bytom
#    Odrzański (51.7253,15.8257) en terug over DEZELFDE punten — een echte
#    TERUGLOOP (`toets_knikken.py`, R≈0 m, v=99), niet een aannemelijk
#    kopmaakpunt: Bytom Odrzański ligt ver buiten de KGHM-corridor en de
#    webbron noemt hem nergens. Getest op --keerstraf 1/2/3/5/10/15/20: ALLE
#    geven identiek 59,5 km/115 edges — pas bij 25 (default) springt de route
#    naar de 81,6 km-omweg. Dit is dus de echte kortste-padwissel van het
#    net, geen straftoeval; 5 is gekozen als ruime marge onder die drempel.
# ⚠️ ÉÉN KLEINE TERUGLOOP BLIJFT STAAN (open punt, niet gerepareerd): vlak
#    vóór de Głogów-smelter (51.68370,15.96940, R≈24-34 m, `toets_knikken`
#    v=2,2) toont het pad een korte in-en-teruglus. Op ELKE geteste keerstraf
#    1-20 blijft precies dít punt over — de enige manier om hem weg te
#    krijgen is de default-straf (25), die in ruil de 14 km-omweg naar Bytom
#    Odrzański terugbrengt (een veel grovere fout). Aannemelijke verklaring:
#    de KGHM-smelter heeft een eigen "spoorbundel het terrein op" (brief §1)
#    en het 1-op-1-net dwingt hier een korte kopmaakbeweging af om die
#    site-aansluiting vanuit de juiste richting te bereiken — maar dat is
#    NIET apart geverifieerd binnen het WEBBUDGET van deze bake. Niet
#    dichtgetrokken met een verzonnen via-punt; gemeld in §9.
# ⚠️ De Lubin-bocht (172,4° bij 51.4006,16.1955, ~exact op Lubin-station,
#    R≈51 m) blijft in elke geteste keerstraf ongewijzigd staan en wordt door
#    `toets_knikken.py` als "scherpe bocht, echt" geclassificeerd (geen
#    terugloop) — een aannemelijk rangeer-/richtingwisselpunt bij de
#    Lubin-aansluiting, niet gerepareerd.
# ⚠️ Geen via-punten toegevoegd (brief §4: geen gedocumenteerde
#    corridorkeuze) — de --keerstraf-aanpassing is een generiek tool-tunable,
#    geen coördinaat verzonnen of via-punt bijgeschoven.
# ⚠️ Geen haven-aanloop nodig (geen zeebeen). Geen fase D/E (brief §6, stopt
#    bij de Głogów-smelter/-raffinaderij).
bak_zilver_lubin_glogow() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Zakład Wzbogacania Rud \"Polkowice\" → Huta Miedzi \"Głogów\"-smelter (KGHM's interne \"Główny Ciąg Technologiczny\"; 1-op-1-net --keerstraf=5, echte route via Lubin/Rudna Gwizdanów — zie kop)|$BEEN/spoorroute-zilver-lubin-glogow-concentrator-smelter.geojson" \
    --marker "Zakład Wzbogacania Rud \"Polkowice\" (KGHM), Polkowice Dolne — concentrator, kop van het spoor|51.4863,16.0655" \
    --marker "Huta Miedzi \"Głogów\" (KGHM), Żukowice — smelter + zilver-/goudraffinaderij, stoppunt|51.6872,15.9778" \
    --routebrief v2/design/routebrieven/zilver-lubin-glogow.md \
    --uit    v2/data/stroomroute-zilver-lubin-glogow.json \
    --stroom zilver-lubin-glogow \
    --titel  "Zilver · Polkowice (KGHM) → Głogów-smelter (Polen)"
}

# ── zilver · San Cristóbal-concentrator (Bolivia) → Julaca → grens Ollagüe → Calama → Mejillones-kade (Chili)
# Routebrief: v2/design/routebrieven/zilver-sancristobal-antofagasta.md (lichte werkwijze M31 golf 2)
# ⚠️ Eén rail-keten, geen zeebeen — de keten stopt op de Mineral Concentrate
#    Terminal-kade in Puerto Mejillones (brief §6: smelterbestemming sinds de
#    2023-eigendomswissel niet meer gepubliceerd). Alle vier spoorruns via het
#    1-op-1-net (BAKE_SUFFIX=-raw), --hoofd-km=100 (klein/geïsoleerd net).
# ⚠️ b1 (San Cristóbal-concentrator → Julaca): 88,4 km tegen 65 km gepubliceerd
#    (+36,0%), BUITEN de ±15%-norm. Geen tweede poging/via-schuif: Julaca is
#    zelf al aannemelijk-niet-bevestigd (brief §7) en de 1-op-1-netgeometrie
#    kan een reële omweg zijn t.o.v. de gepubliceerde tak-lengte — bevinding,
#    niet dichtgetrokken (zie §9).
# ⚠️ b2 (Julaca → grens Avaroa/Ollagüe): geen gepubliceerde deellengte, alleen
#    de bake-uitkomst (76,2 km, verhouding 1,00 t.o.v. de grootcirkel — vrijwel
#    recht, zie toets_rechte_benen in §9). Snap op het grenspunt 9,20 km: de
#    brief noemt dit punt al als de dorpscoördinaat (Wikipedia-geohack), niet
#    de exacte spoorgrensmarkering (brief §7) — geen via-punt bijgeschoven.
# ⚠️ b3a (grens → Calama) en b3b (Calama → Mejillones-kade): twee losse runs
#    (kop→via, via→staart) zoals de brief voorschrijft, geen gepubliceerde
#    deellengte. b3b heeft één OMKERING (179,7°, boogstraal ~169 m) vlak bij
#    het startpunt Calama — een knooppunt met de Chuqui-mijntak, dus een
#    kopmaak-plek op het net, geen verzonnen sluiproute.
# ⚠️ Geen haven-aanloop gebouwd: de keten stopt op de kade, dus een MARNET-
#    zeeverbinding is hier niet relevant (bak-aanwijzing in de brief). Gemeten
#    met het hecht_marnet-snippet uit de handleiding: dichtstbijzijnde
#    zeeknoop 4664 op -23.80000,-71.30000, 124,9 km van de kade — bevestigt de
#    ~125 km uit brief §7 (Mejillones-136km-klasse), open punt/context.
# ⚠️ Geen last-mile-stippel bij Mejillones toegevoegd: de kade zelf is het
#    stoppunt van de hele keten (geen b4/b5), dus de laatste ~700 m
#    conveyor-strook is geen apart been in deze bake.
# ⚠️ Geen fase D/E (brief §6): de smelterbestemming is sinds 2023 niet meer
#    gepubliceerd — bewust niet getekend, stoppunt op de kade.
bak_zilver_sancristobal_antofagasta() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein San Cristóbal-concentrator → Julaca-aansluiting (MSC-tak, eigen lijn, spoorwijdte 1 m, 2005-2007)|$BEEN/spoorroute-zilver-sancristobal-antofagasta-b1.geojson" \
    --been-geojson "spoor|trein Julaca-aansluiting → grens Avaroa (BO)/Ollagüe (CL) (Ferrocarril Uyuni-Antofagasta/FCAB)|$BEEN/spoorroute-zilver-sancristobal-antofagasta-b2.geojson" \
    --been-geojson "spoor|trein grens Ollagüe → Calama (FCAB, via-punt corridorkeuze — knooppunt met de Chuquicamata-mijntak)|$BEEN/spoorroute-zilver-sancristobal-antofagasta-b3a.geojson" \
    --been-geojson "spoor|trein Calama → Mineral Concentrate Terminal, Puerto Mejillones (FCAB, doorgaande tak na Calama)|$BEEN/spoorroute-zilver-sancristobal-antofagasta-b3b.geojson" \
    --marker "ag-sancristobal-planta — Minera San Cristóbal, concentrator, Nor Lípez, Potosí — laadplek, kop van het spoor|-21.1266,-67.2098" \
    --marker "Julaca-aansluiting (Uyuni-Antofagasta-lijn) — via-punt corridorkeuze, aannemelijk (geen bron noemt de naam expliciet)|-20.9113,-67.5673" \
    --marker "grens Avaroa (BO)/Ollagüe (CL) — via-punt corridorkeuze, dorpscoördinaat (niet de exacte spoorgrensmarkering)|-21.2833,-68.1833" \
    --marker "Calama — via-punt corridorkeuze, knooppunt met de Chuquicamata-mijntak|-22.4624,-68.9272" \
    --marker "ag-mejillones-kade — Mineral Concentrate Terminal, Puerto Mejillones (Terminal de Graneles del Norte) — losplek, stoppunt|-23.0598,-70.3788" \
    --routebrief v2/design/routebrieven/zilver-sancristobal-antofagasta.md \
    --uit    v2/data/stroomroute-zilver-sancristobal-antofagasta.json \
    --stroom zilver-sancristobal-antofagasta \
    --titel  "Zilver · San Cristóbal (Bolivia) → Ollagüe/Calama → Mejillones (Chili)"
}

# ── kobalt · CTT Bou Azzer-mijn (Managem) → Tizi n'Tichka-pas → CTT Guemassa-complex (Marokko)
# Routebrief: v2/design/routebrieven/kobalt-bouazzer-guemassa.md (lichte werkwijze M31 golf 2)
# ⚠️ Eén been, één tool: profiel kobalt-bouazzer-guemassa-bouazzer-guemassa in
#    maak_stroombeen_weg.py (extract marokko). Geen gepubliceerde wegkm (brief
#    §7[8]) — alleen het gemeten getal (310,2 km) staat op de kaart, geen
#    ±15%-toets mogelijk.
# ⚠️ De weg buigt na Marrakech weer zuidwaarts: via4 (Marrakech-zuid/Avenue
#    Guemassa, lat 31,5791) ligt noordelijker dan de fabriek (lat 31,3825) —
#    elk been-segment is apart geroutet (kop→via/via→via), dus geen
#    noord-zuid-lus; het laatste segment (26,9 km) loopt gewoon zuidwaarts.
# ⚠️ Ankerverbinding "weg → kade" bij Guemassa is 0,63 km (> 0,5 km-norm) —
#    bevinding, niet dichtgetrokken (het satellietgelegde fabrieksanker ligt
#    net naast de dichtstbijzijnde OSM-wegvertex).
# ⚠️ Geen fase D/E: het hydrometallurgisch complex is het stoppunt (brief §6).
bak_kobalt_bouazzer_guemassa() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|erts/concentraat Bou Azzer-mijn → Ouarzazate → Tizi n'Tichka-pas → Aït Ourir → Marrakech-zuid → CTT Guemassa-complex (N9/N8)|$BEEN/kobalt-bouazzer-guemassa-weg-bouazzer-guemassa.geojson" \
    --marker "Mine Bou Azzer (CTT, Managem), Drâa-Tafilalet — mijn/laadplek|30.5184,-6.9134" \
    --marker "CTT Guemassa-complex (Managem), vijf eenheden (Co-kathodes, CuSO4, NiSO4, ZnO) — fabriek/losplek, stoppunt|31.3825,-8.0635" \
    --routebrief v2/design/routebrieven/kobalt-bouazzer-guemassa.md \
    --uit    v2/data/stroomroute-kobalt-bouazzer-guemassa.json \
    --stroom kobalt-bouazzer-guemassa \
    --titel  "Kobalt · Bou Azzer-mijn → Tizi n'Tichka-pas → Guemassa-complex (Marokko)"
}

# ── uranium · Inkai MPP (Kazachstan) → Zhanatas → Astana → Petropavl → Jekaterinenburg → Moskou → Sint-Petersburg (Rusland-route)
# Routebrief: v2/design/routebrieven/uranium-inkai-stpetersburg.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck) is een LETTERLIJKE KOPIE van uranium-inkai-poti b1: geen nieuwe
#    geometrie, dezelfde rechte stippel-regel (geen doorlopende OSM-weg over de
#    ~290 km woestijnsteppe Suzak-district → Zjambyl-oblast, brief §7/[1]).
# ⚠️ Geen anker voor "de grensovergang" (brief §3: "niet als apart anker
#    gelegd") — Petropavl (54.8833,69.1667, laatste KZ-knoop vóór de grens)
#    is daarom het praktische kop-/staartpunt van b2 én b3: de naad daar is
#    0,0 km (identieke coördinaat), dus de grensoversteek zelf zit "in" die
#    naad in plaats van op een eigen punt. b2 = 2 deelruns (Zhanatas→Astana,
#    Astana→Petropavl), b3 = 3 deelruns (Petropavl→Jekaterinenburg,
#    Jekaterinenburg→Moskou, Moskou→Sint-Petersburg-kade) — alle vijf
#    BAKE_SUFFIX=-raw toets_spoorroute.mjs op het 1-op-1-spoornet, doorgetrokken
#    (géén stippel): beide spoorbenen zijn "aannemelijk: geografische
#    afleiding" maar dat staat in de beennaam, niet in de lijnstijl (brief §2).
# ⚠️ Geen zee-been: de keten stopt bij de Sint-Petersburg-kade zelf (brief §6),
#    dus geen MARNET-zeeknoop-check/haven-aanloop nodig.
# ⚠️ u-inkai-plant en u-zhanatas-station zijn AL gelegde ankers uit
#    uranium-inkai-poti — hergebruikt, geen nieuwe satellietpas. u-stpetersburg-
#    kade (Petrolesport-containerterminal) is nieuw, satellietblik brief §3/[4]
#    — de algemene commerciële zeehaven, geen bevestigd nucleair-ladingpunt.
bak_uranium_inkai_stpetersburg() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|yellowcake Inkai MPP → Zhanatas-spoorstation (schematisch — geen doorlopende weg in OSM; woestijnweg Suzak-district → Zjambyl-oblast, aannemelijk: één bron — letterlijke kopie van b1 in uranium-inkai-poti)|45.2855,67.5255|43.5610,69.7260" \
    --been-geojson "spoor|trein Zhanatas-spoorstation → Astana (b2a, Trans-Kazachse hoofdlijn, aannemelijk: geografische afleiding)|$BEEN/spoorroute-uranium-inkai-stpetersburg-zhanatas-astana.geojson" \
    --been-geojson "spoor|trein Astana → Petropavl (b2b, laatste Kazachse knoop vóór de KZ–RU-grens, aannemelijk: geografische afleiding)|$BEEN/spoorroute-uranium-inkai-stpetersburg-astana-petropavl.geojson" \
    --been-geojson "spoor|trein Petropavl → Jekaterinenburg (b3a, KZ–RU-grensovergang zit in deze naad — geen apart anker in de brief, aannemelijk: geografische afleiding)|$BEEN/spoorroute-uranium-inkai-stpetersburg-petropavl-jekaterinenburg.geojson" \
    --been-geojson "spoor|trein Jekaterinenburg → Moskou (b3b, Oeral-lijn naar de Moskou-hoofdlijn, aannemelijk: geografische afleiding)|$BEEN/spoorroute-uranium-inkai-stpetersburg-jekaterinenburg-moskou.geojson" \
    --been-geojson "spoor|trein Moskou → Sint-Petersburg-kade (b3c, Moskou–Sint-Petersburg-hoofdlijn, stoppunt, aannemelijk: geografische afleiding)|$BEEN/spoorroute-uranium-inkai-stpetersburg-moskou-stpetersburg.geojson" \
    --marker "Inkai MPP — hoofdverwerkingsfabriek, JV Inkai (Kazatomprom 60%/Cameco 40%) — laadplek|45.2855,67.5255" \
    --marker "Zhanatas-spoorstation, Zjambyl-oblast — overslag truck → spoor|43.5610,69.7260" \
    --marker "Petrolesport-containerterminal, Groot-haven van Sint-Petersburg — overslag spoor → zee, stoppunt|59.8909,30.2376" \
    --routebrief v2/design/routebrieven/uranium-inkai-stpetersburg.md \
    --uit    v2/data/stroomroute-uranium-inkai-stpetersburg.json \
    --stroom uranium-inkai-stpetersburg \
    --titel  "Uranium · Inkai (Kazachstan) → Petropavl → Jekaterinenburg → Moskou → Sint-Petersburg (Rusland-route)"
}

# ── lithium · Salar del Hombre Muerto/Fénix (Argentinië) → Antofagasta → Charleston → Bessemer City (VS)
# Routebrief: v2/design/routebrieven/lithium-hombremuerto-bessemercity.md (LICHTE werkwijze M31 golf 2)
# ⚠️ b1 (truck) is GESPLITST op El Peñón: plant → El Peñón is een gemeten
#    weggeometrie (RN-43, 162,2 km); El Peñón → grens Paso de San Francisco is
#    een STIPPEL — `maak_stroombeen_weg.py` gaf tweemaal "geen wegpad tussen
#    punt 2 en 3" (eerst alleen extract argentina, toen ook chili erbij) —
#    geen doorlopende OSM-weg over de hooggebergteklim (~4.726 m), precies wat
#    de brief anticipeerde (§2: "geen stippel verwacht tenzij OSM geen wegpad
#    geeft op deze hoogte").
# ⚠️ b2 (truck, grens → Antofagasta-kade) meet 728,5 km tegen de
#    ontwerpschatting van ~500 km (+45,7%, buiten ±15%) — GEEN via-punt
#    bijgeschoven om het getal te halen (werkregel §5): de Diego de Almagro-
#    en Chañaral-segmenten liggen op de reële afstanden van de bergafdaling
#    resp. de Ruta 5-kustcorridor; Arcadium/Livent's "675 km via Route 5" dekt
#    vermoedelijk b1+b2 samen zonder de kustomweg via Chañaral, of is een
#    Google-Maps-punt-naar-punt-cijfer op een andere route. Blijft een
#    bevinding, geen fout.
# ⚠️ b3 (zee) hergebruikt de bestaande haven-aanloop Antofagasta
#    (aanloop-antofagasta.geojson, 97,1 km, gedeeld met
#    lithium-atacama-antofagasta/koper-aurubis-hamburg); Charleston-kant
#    GEEN aanloop (kade 1,67 km van zeeknoop 9371, eigen meting, ruim onder
#    de 5 km-norm van LAR-586) — direct been naar de kade-coördinaat.
# ⚠️ b4 (truck, Charleston → Bessemer City) meet 415,2 km tegen de
#    ontwerpschatting van ~545 km (−23,8%, buiten ±15%) — de gemeten
#    interstate-afstand (I-26 → I-85) is preciezer dan de ontwerpschatting;
#    geen fout, blijft een bevinding.
# ⚠️ Fénix-plant-anker is ONZEKER (brief §3/§7: sitelaag-hergebruik, alleen de
#    salarcentroïde zichtbaar op z13, geen fabrieksgebouw op deze korrel) —
#    dat staat in de markernaam, niet in de lijnstijl. Geen enkel been is
#    gedeeld met een bestaande stroom, alleen het Antofagasta-anker en de
#    haven-aanloop zijn letterlijke kopieën.
bak_lithium_hombremuerto_bessemercity() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|carbonaat Fénix-plant → El Peñón (RN-43 via Antofagasta de la Sierra)|$BEEN/lithium-hombremuerto-bessemercity-weg-hombremuerto-elpenon.geojson" \
    --stippel      "truck|El Peñón → grens Paso de San Francisco (schematisch — geen doorlopende OSM-weg over de hooggebergteklim, ~4.726 m, tweemaal getoetst)|-26.4754,-67.2653|-26.8764,-68.3014" \
    --been-geojson "truck|carbonaat grens Paso de San Francisco → Puerto Antofagasta (Ruta 31/23 via Diego de Almagro/Chañaral → Ruta 5 noordwaarts)|$BEEN/lithium-hombremuerto-bessemercity-weg-grens-antofagasta.geojson" \
    --stippel-geojson "zee|haven-aanloop Antofagasta (schematisch, over water — MARNET reikt hier niet: 97 km; gedeeld met lithium-atacama-antofagasta/koper-aurubis-hamburg)|$BEEN/aanloop-antofagasta.geojson" \
    --been         "zee|containerschip Antofagasta → Charleston, Hugh K. Leatherman Terminal (Stille Oceaan zuidwaarts → Panamakanaal → Atlantische Oceaan)|-23.800,-71.300|32.8392,-79.9352" \
    --been-geojson "truck|containers Charleston → Bessemer City (I-26 via Columbia/Spartanburg → I-85 via Gastonia)|$BEEN/lithium-hombremuerto-bessemercity-weg-charleston-bessemer.geojson" \
    --marker "li-hombremuerto-plant — Fénix-plant (Arcadium Lithium/Rio Tinto), Salar del Hombre Muerto — laadplek (onzeker)|-25.3508,-67.1415" \
    --marker "El Peñón — laatste plaats vóór de grensklim (grens tussen gemeten weg en stippel)|-26.4754,-67.2653" \
    --marker "grens Paso de San Francisco — landgrens Argentinië/Chili (via-punt corridorkeuze)|-26.8764,-68.3014" \
    --marker "li-antofagasta-kade — Puerto Antofagasta, ATI-kade (frente 2) — overslag truck → zee (bron-gelegd, gedeeld anker)|-23.6500,-70.4088" \
    --marker "li-charleston-kade — Hugh K. Leatherman Terminal, North Charleston — overslag zee → truck (bron-gelegd)|32.8392,-79.9352" \
    --marker "li-bessemer-fabriek — Arcadium Lithium (ex-Livent), Bessemer City NC — losplek/conversieknoop, stoppunt (bron-gelegd)|35.2795,-81.3060" \
    --routebrief v2/design/routebrieven/lithium-hombremuerto-bessemercity.md \
    --uit    v2/data/stroomroute-lithium-hombremuerto-bessemercity.json \
    --stroom lithium-hombremuerto-bessemercity \
    --titel  "Lithium · Salar del Hombre Muerto (Argentinië) → Antofagasta → Charleston → Bessemer City (VS)"
}

# ── lithium · Grota do Cirilo (Araçuaí, MG) → Porto de Vitória (ES) → China (spodumeenconcentraat)
# Routebrief: v2/design/routebrieven/lithium-cirilo-vitoria.md (LICHTE werkwijze M31 golf 2)
# ⚠️ STROOM-ID IS lithium-cirilo-vitoria, NIET lithium-cirilo-ilheus: de brief §7
#    (haalbaarheidstoets, bindend) sluit de oorspronkelijk ONTWORPEN spoorcorridor
#    via FCA/VLI naar Porto Sul/Ilhéus (Bahia) uit — Sigma Lithium vervoert 100%
#    per TRUCK naar Vitória (Espírito Santo), bevestigd door meerdere persberichten
#    2023-2025. Porto Sul/Ilhéus stond alleen in het NI 43-101-technisch rapport
#    als het destijds GEPLANDE exportkanaal, niet het uitgevoerde tracé. Eerste
#    Zuid-Amerikaanse Atlantische ertsroute van de atlas.
# ⚠️ b1 (truck, 712,3 km) ligt +5,5% boven de ontwerpschatting van 675 km — er is
#    geen gepubliceerd truck-km (brief §7/§2); de schatting was een venster op de
#    via-keten-hemelsbreedte (558,6 km), geen harde bron. Binnen het venster, geen
#    dwingende ±15%-toets zonder gepubliceerd cijfer (bevinding, geen fout).
# ⚠️ b2 (zee, haven-aanloop Vitória) is een STIPPEL: de Vila Rubim-kade ligt 95,5 km
#    van zeeknoop 900 (-20,00000,-39,50000), ver boven de 25 km-snapdrempel én de
#    5 km-haven-aanloopregel van 2026-09-28. `maak_havenaanloop.py` vond een pad
#    over water (102,7 km, 87 punten, 0,00 km over land) — geen terugval nodig.
# ⚠️ b3 (zee, MARNET) is GEEN stippel: bulkschip vanaf zeeknoop 900 (niet vanaf de
#    kade — die aanloop levert b2) naar de Yangtze-monding. Bestemming China is
#    "aannemelijk: één bron" (Yahua/Sichuan niet bevestigd, brief §6) — de aanname
#    staat in de beennaam, niet in de lijnstijl.
# ⚠️ li-yangtze-monding is een BESTAAND, HERGEBRUIKT anker (zelfde rol/coördinaat
#    als in lithium-atacama-antofagasta.md §3) — geen dubbele markerdefinitie.
bak_lithium_cirilo_vitoria() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Grota do Cirilo → Itaobim → Gov. Valadares → Colatina → João Neiva → Porto de Vitória (BR-367 → BR-116 → BR-259 → BR-101)|$BEEN/lithium-cirilo-vitoria-weg-plant-kade.geojson" \
    --stippel-geojson "zee|haven-aanloop Vitória (schematisch, over water — kade 95,5 km van de MARNET-zeeknoop)|$BEEN/lithium-cirilo-vitoria-aanloop-vitoria.geojson" \
    --been         "zee|bulkschip Vitória → Yangtze-monding (Zuid-Atlantische Oceaan, om Kaap de Goede Hoop of via Panama — MARNET beslist; bestemming aannemelijk, één bron)|-20.00000,-39.50000|31.42704,121.47618" \
    --marker "Grota do Cirilo — DMS/flotatie-complex (Sigma Lithium)|-16.7328,-41.8878" \
    --marker "Porto de Vitória — Vila Rubim/Cais Comercial|-20.3238,-40.3477" \
    --marker "Yangtze-monding (bestaand anker, hergebruikt uit lithium-atacama-antofagasta)|31.42704,121.47618" \
    --routebrief v2/design/routebrieven/lithium-cirilo-vitoria.md \
    --uit    v2/data/stroomroute-lithium-cirilo-vitoria.json \
    --stroom lithium-cirilo-vitoria \
    --titel  "Lithium · Grota do Cirilo (Araçuaí) → Porto de Vitória → China (Brazilië-Atlantische route)"
}

# ── zeldzame aardmetalen · JL MAG Baotou-fabriek (毛坯) → JL MAG Ningbo-fabriek (China, interne bedrijfsstroom)
# Routebrief: v2/design/routebrieven/ree-baotou-ningbo.md (LICHTE werkwijze M31 golf 2)
# ⚠️ Ontwerp herzien (brief §0): niet Northern RE-scheiding → naamloze Ningbo-
#    afnemer, maar JL MAG's EIGEN fabriek in Baotou (magneet-halffabricaten,
#    毛坯) → JL MAG's EIGEN fabriek in Ningbo (afwerking tot eindmagneten) —
#    één bedrijf, aannemelijk: één bron (SMM-artikel, brief §8 [1]).
# ⚠️ ÉÉN BEEN (b1, spoor): BAKE_SUFFIX=-raw toets_spoorroute.mjs op het
#    1-op-1-net (extract china, console bevestigt "3260717 spoor-edges"),
#    geen --via (geen gedocumenteerde corridorkeuze binnen budget, de router
#    kiest zelf het hoofdspoornet-tracé). Geen stippel — doorgetrokken,
#    "aannemelijk" staat in de beennaam, niet in de lijnstijl.
# ⚠️ Lengtetoets: 2.116,6 km gemeten tegen de ~2.150 km hemelsbreed-schatting
#    uit de brief (−1,6%) — geldt hier als referentie, niet als ±15%-toets,
#    want er is geen gepubliceerde enkelvoudige vrachtlijnlengte (brief §2/§7).
# ⚠️ Fase D NIET gebakken (Ningbo-emplacement → JL MAG Ningbo-fabriekspoort,
#    ~13 km truck): het adres (浦丰路666号, 慈城镇) is bevestigd maar geen
#    coördinaat gevonden binnen dit sessiebudget (OSM/Overpass leeg, Nominatim
#    429-rate-limited, MEE-register 302 naar error.jsp) — zie brief §6/§7.
# ⚠️ Beide ankers zijn zelf het been-uiteinde (geen losse marker-snap nodig):
#    JL MAG Baotou is een straatmatch (沼园路 bevestigd in OSM, geen
#    poortbevestiging op naam), Ningbo-noord-station is bron-gelegd (rode
#    perronoverkapping + rangeersporen op z14 duidelijk zichtbaar).
bak_ree_baotou_ningbo() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein JL MAG Baotou-fabriek → Ningbo-noord spoorstation (hoofdspoornet, geen gepubliceerde enkelvoudige vrachtlijn, aannemelijk: één bron voor de interne relatie)|$BEEN/spoorroute-ree-baotou-ningbo-baotou-ningbobei.geojson" \
    --marker "JL MAG (金力永磁) Baotou-fabriek — magneet-halffabricaten (毛坯), 稀土高新区 — laadplek (aannemelijk: straatmatch)|40.6115,109.8600" \
    --marker "Ningbo-noord spoorstation (宁波北站), Jiangbei — spoor-eindpunt, stoppunt van deze brief (bron-gelegd)|29.9517,121.5200" \
    --routebrief v2/design/routebrieven/ree-baotou-ningbo.md \
    --uit    v2/data/stroomroute-ree-baotou-ningbo.json \
    --stroom ree-baotou-ningbo \
    --titel  "Zeldzame aardmetalen · JL MAG Baotou → Ningbo (interne bedrijfsstroom, China)"
}

# ── kolen · AlamTri/Adaro Tutupan/Wara (Tabalong) → Kelanis → Taboneo-rede → Fangchenggang (Guangxi, China)
# Routebrief: v2/design/routebrieven/kolen-tabalong-fangchenggang.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck) is een RECHTE STIPPEL: Adaro's eigen haalweg (privéterrein,
#    geen publiek net, geen OSM-weg beschikbaar). Hemelsbreed 73,8 km tegen
#    gepubliceerd ~86 km (bron [2], MarineLink-havenprofiel) = -14,2%, binnen
#    ±15% (een niet-rechte privéweg is altijd langer dan de hemelsbrede lijn).
# ⚠️ b2 (binnenvaart, maak_rivierbeen.py over de bulklaag) meet 195,9 km tegen
#    gepubliceerd ~118,5 km (64 NM, bron [5]) = +65,4%, RUIM BUITEN ±15% —
#    bevinding, geen via-punt bijgeschoven. De hemelsbrede afstand Kelanis→
#    Taboneo is zelf al ~162,9 km (dus groter dan de gepubliceerde 118,5 km):
#    de brief-km lijkt een andere, kortere deelmeting te zijn (bijv. vanaf een
#    ander punt in de Barito-delta dan het Kelanis-anker) — Taboneo is bovendien
#    een gebied zonder vaste kade (brief §3/§7, ±enkele km-onzekerheid). De
#    "naar"-kant van de bulklaag snapte 18,51 km van het dichtstbijzijnde
#    bulk-knooppunt, want Taboneo ligt in open zee zuid van de delta-mond, niet
#    op de gekarteerde rivierlijn zelf → dat gaf een naad > 5 km (bakhandleiding
#    §5) tussen b2 en de Taboneo-haven-aanloop. Gedicht met een korte RECHTE
#    STIPPEL (binnenvaart, 18,5 km, "bulklaag reikt niet tot de open-zee
#    ankerplaats") — geen via-punt bijgeschoven, wel de vereiste naad-fix.
# ⚠️ b3 (zee) krijgt een haven-aanloop aan BEIDE zijden (bakhandleiding §2,
#    LAR-586): Taboneo ligt 19,54 km van zeeknoop 5483 (-3,52850,114,49950,
#    aanloop 20,8 km, omwegfactor 1,067) en Fangchenggang-kade ligt 28,63 km
#    van zeeknoop 5539 (21,57570,108,62050, aanloop 31,2 km, omwegfactor
#    1,091) — beide ruim boven de 5 km-norm en Fangchenggang zelfs boven de
#    25 km max-snap. Beide `maak_havenaanloop.py`-runs slaagden meteen (geen
#    terugval nodig); de Fangchenggang-aanloop is ná generatie op reisvolgorde
#    gezet (zeeknoop → kade — de coördinaten zelf zijn ongewijzigd, alleen de
#    puntvolgorde is omgedraaid, zoals bij kolen-ermelo-portqasim). Geen
#    gepubliceerde scheepsroute-km gevonden; het gemeten zeebeen wordt tegen
#    de ~2.890 km hemelsbreed uit de brief vergeleken in §9, geen via-punt
#    bijgeschoven (Straat Makassar/Karimata/SCS voegen normaal een
#    omwegfactor >1,05 toe — dat is hier ook wat er gebeurt).
# ⚠️ Geen fase D/E (brief §6): geen bron noemt de specifieke afnemende
#    centrale voor déze as (China is de swing-koper op de wereldkolenmarkt).
bak_kolen_tabalong_fangchenggang() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|haalweg Tutupan/Wara-mijncomplex → Kelanis-laadterminal (Adaro's eigen privéweg, geen publiek net)|-2.204484,115.527798|-2.293384,114.8703" \
    --been-geojson "binnenvaart|Kelanis → Taboneo (Barito-rivier + delta, bulklaag: ligging van het water)|$BEEN/kolen-tabalong-fangchenggang-rivier-kelanis-taboneo.geojson" \
    --stippel      "binnenvaart|Barito-delta → Taboneo-rede (bulklaag reikt niet tot de open-zee ankerplaats — rechte stippel, naad 18,5 km)|-3.5460,114.5234|-3.6994,114.4586" \
    --stippel-geojson "zee|haven-aanloop Taboneo-rede (schematisch, over water — kade 19,54 km van de MARNET-zeeknoop)|$BEEN/kolen-tabalong-fangchenggang-aanloop-taboneo.geojson" \
    --been         "zee|zeeschip Taboneo-rede → Fangchenggang-kolenterminal (thermisch; Javazee → Straat Makassar/Karimata → Zuid-Chinese Zee → Beibu-golf)|-3.52850,114.49950|21.57570,108.62050" \
    --stippel-geojson "zee|haven-aanloop Fangchenggang-kade (schematisch, over water — kade 28,63 km van de MARNET-zeeknoop)|$BEEN/kolen-tabalong-fangchenggang-aanloop-fcg.geojson" \
    --marker "AlamTri/Adaro Tutupan/Wara-mijncomplex, Tabalong (Zuid-Kalimantan)|-2.204484,115.527798" \
    --marker "Kelanis-laadterminal (PT Adaro Indonesia), Barito-rivier|-2.293384,114.8703" \
    --marker "Taboneo-ankerplaats (rede, geen vaste kade — transshipment, onzeker)|-3.6994,114.4586" \
    --marker "Fangchenggang-havencomplex (西湾港区), Guangxi (onzeker, geen specifieke kolenberth geïsoleerd)|21.592216,108.344216" \
    --routebrief v2/design/routebrieven/kolen-tabalong-fangchenggang.md \
    --uit    v2/data/stroomroute-kolen-tabalong-fangchenggang.json \
    --stroom kolen-tabalong-fangchenggang \
    --titel  "Kolen · Tabalong (AlamTri/Adaro) → Kelanis → Taboneo → Fangchenggang (China)"
}

# ── zilver · Yanacancha-concentrator (Antamina) → Puerto Punta Lobitos (Huarmey), mineroducto (Peru)
# Routebrief: v2/design/routebrieven/zilver-antamina-huarmey.md (LICHTE werkwijze M31 golf 2)
# ⚠️ Eén been (b1, fase A, modaliteit leiding) — geen zeebeen: de brief stopt
#    bewust bij de Huarmey-kade (§6, geen bron noemt een smelterbestemming
#    voor het concentraat), dus geen haven-aanloop-check nodig.
# ⚠️ b1 is VIJF STIPPEL-SEGMENTEN ACHTER ELKAAR (kop→via1→via2→via3→via4→
#    staart), want `--stippel` accepteert precies twee punten per aanroep —
#    geen meerpunts-vlag. Eigen Overpass-poging deze sessie: overpass-api.de
#    gaf HTTP 406, de kumi-mirror een timeout — beide onbereikbaar, precies
#    zoals de brief §7 al meldde. Niet vastgesteld of OSM man_made=pipeline
#    hier echt ontbreekt of alleen onbereikbaar was.
# ⚠️ De 4 via-punten (Aquia, Cajacay/Santa Rosa, Cochapeti, Huayan) zijn
#    gedocumenteerde corridorgemeenschappen (RPP/Antamina-nieuwspagina's),
#    geen gemeten pijplijntracé — de echte mineroducto heeft 4 klepstations
#    en een hoogste punt van 4.669 m die niet 1-op-1 op deze dorpen valt.
#    Gemeten hemelsbreed via de 5 segmenten: 187,7 km tegen de gepubliceerde
#    302 km (Wikipedia ES; Antamina.com noemt 304) = −37,9% — ver buiten de
#    ±15%-norm, maar dit is bewust een schematische stippel zonder gemeten
#    brongeometrie (brief §7: geen harde ±15%-eis hier). Bevinding voor §9,
#    niet dichtgetrokken.
bak_zilver_antamina_huarmey() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel "leiding|mineroducto Antamina-Huarmey, segment 1: Yanacancha-concentrator → Aquia (schematisch — geen OSM man_made=pipeline gevonden/bereikbaar)|-9.5615,-77.0400|-10.0745,-77.1447" \
    --stippel "leiding|mineroducto Antamina-Huarmey, segment 2: Aquia → Cajacay/Santa Rosa (schematisch — corridorgemeenschap, geen gemeten tracé)|-10.0745,-77.1447|-10.1747,-77.3355" \
    --stippel "leiding|mineroducto Antamina-Huarmey, segment 3: Cajacay/Santa Rosa → Cochapeti (schematisch — corridorgemeenschap, geen gemeten tracé)|-10.1747,-77.3355|-9.9801,-77.6958" \
    --stippel "leiding|mineroducto Antamina-Huarmey, segment 4: Cochapeti → Huayan (schematisch — corridorgemeenschap, geen gemeten tracé)|-9.9801,-77.6958|-9.9079,-77.7933" \
    --stippel "leiding|mineroducto Antamina-Huarmey, segment 5: Huayan → Puerto Punta Lobitos (schematisch — geen OSM man_made=pipeline gevonden/bereikbaar)|-9.9079,-77.7933|-10.1035,-78.1788" \
    --marker "Yanacancha-concentrator, Compañía Minera Antamina — mijn/concentrator, kop van de leiding|-9.5615,-77.0400" \
    --marker "Puerto Punta Lobitos, Huarmey — overslag leiding → zee (ontwatering/filtratie + laadsteiger), stoppunt|-10.1035,-78.1788" \
    --routebrief v2/design/routebrieven/zilver-antamina-huarmey.md \
    --uit    v2/data/stroomroute-zilver-antamina-huarmey.json \
    --stroom zilver-antamina-huarmey \
    --titel  "Zilver · Antamina (Yanacancha) → Puerto Punta Lobitos (Huarmey, Peru)"
}

# ── zeldzame aardmetalen · LAMP Gebeng (Lynas) → Westport (Port Klang) → Honmoku/Yokohama (Japan)
# Routebrief: v2/design/routebrieven/ree-kuantan-japan.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck, maak_stroombeen_weg.py, profiel ree-kuantan-japan-gebeng-westport,
#    extract maleisie): 336,5 km getekende weggeometrie tegen ~290 km
#    kaartschatting (geen gepubliceerde kilometrage, brief §7, alleen Time.com
#    noemt de route zelf) = **+16,0%, net buiten ±15%** — bevinding, niet
#    dichtgetrokken (de referentiewaarde is zelf al een schatting op de
#    beschreven corridor, geen operator-bron).
# ⚠️ b2 (zee, MARNET, kade → kade): Westport snapt op 2,3 km van zeeknoop 5375
#    — ruim binnen de 5 km-norm, geen haven-aanloop nodig. Honmoku ligt 7,8 km
#    van zeeknoop 9065 (> 5 km, LAR-586 §2) → haven-aanloop nodig. Poging via
#    maak_havenaanloop.py liep vast op de 300 s-timeout (exit 124) → GEEN
#    tweede poging (bakhandleiding §2), terugval op een rechte stippel
#    zeeknoop → kade. Honmoku is een AANKOMENDE haven (net als Kuantan in
#    ree-mtweld-kuantan.md §9) — het hoofd-zeebeen eindigt dus op de zeeknoop
#    en de stippel vervolgt zeeknoop → kade, niet andersom.
# ⚠️ Fase D niet getekend (brief §6): drie Japanse magneetfabrieken (Shin-Etsu
#    Fukui/Takefu, TDK Akita, Proterial Kumagaya) delen de markt, geen
#    offtake-koppeling per lading gevonden — de keten stopt bij de Japanse
#    invoerhaven, net als ree-bayanobo-baotou.
# ⚠️ LAMP Gebeng is een hergebruikt anker (ree-mtweld-kuantan.md §3, geen
#    nieuwe satellietpas); geen gedeelde geometrie met die stroom (Australië→
#    Fremantle→Kuantan versus Kuantan→Port Klang→Japan lopen niet samen).
bak_ree_kuantan_japan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen LAMP Gebeng → Westport, Pulau Indah (Lebuhraya Pantai Timur E8 → Karak Highway E8/E9 → KL–Klang-corridor)|$BEEN/ree-kuantan-japan-weg-gebeng-westport.geojson" \
    --been         "zee|zeeschip Westport (Port Klang) → Honmoku-zeeknoop, Yokohama (Straat Malakka → Zuid-Chinese Zee → Luzon-/Taiwanstraat → Filipijnse Zee)|2.9498,101.3076|35.36610,139.68570" \
    --stippel      "zee|haven-aanloop Honmoku/Yokohama (schematisch — 1:10M-kust kent de haven niet; maak_havenaanloop.py liep vast op de 300 s-timeout, geen tweede poging)|35.36610,139.68570|35.4356,139.6727" \
    --marker "Lynas Advanced Materials Plant (LAMP), Gebeng — scheiding tot NdPr-/Dy-/Tb-oxide (hergebruikt anker)|4.0034,103.3775" \
    --marker "Westports Malaysia, Pulau Indah, Port Klang — overslag truck → zee|2.9498,101.3076" \
    --marker "Honmoku Futo-containerterminal, Yokohama — voorgestelde Japanse invoerhaven, stoppunt|35.4356,139.6727" \
    --routebrief v2/design/routebrieven/ree-kuantan-japan.md \
    --uit    v2/data/stroomroute-ree-kuantan-japan.json \
    --stroom ree-kuantan-japan \
    --titel  "Zeldzame aardmetalen · LAMP Gebeng (Lynas) → Port Klang → Yokohama (Japan)"
}

# ── uranium · Port Hope Conversion Facility (Cameco, Ontario) → Rotterdam RHB → Urenco Almelo
# Routebrief: v2/design/routebrieven/uranium-porthope-almelo.md (LICHTE werkwijze M31 golf 2)
# ⚠️ b1 (zee, haven-aanloop, STIPPEL): Port Hope ligt 65,9 km van de
#    dichtstbijzijnde bruikbare MARNET-zeeknoop 4821 (Lake Ontario/Seaway-zone,
#    ruim buiten de 25 km-snap) — maak_havenaanloop.py lukte in één poging
#    (67,3 km, omwegfactor 1,022, 0 km over land); brief noemde ~66 km
#    (haalbaarheidstoets) → binnen tolerantie.
# ⚠️ b2 (zee, GEEN stippel): standaard MARNET-router zeeknoop 4821 → Rotterdam
#    RHB. Brief-schatting ~7.400 km was een EXTRAPOLATIE (grootcirkel ×
#    Duluth→Rotterdam-inflatiefactor), niet gemeten — getoetst tegen de echte
#    bake-uitvoer, zie §9.
# ⚠️ b3 (truck, GEEN stippel): profiel "uranium-porthope-almelo-rotterdam-
#    almelo" in maak_stroombeen_weg.py, extract nederland. Gemeten 191,6 km
#    tegen gepubliceerd 189 (OSRM-webcheck) = +1,4% [OK]; het ketenontwerp
#    noemde ~150 km (bekend open punt uit de brief, niet dichtgetrokken — de
#    kortste route schakelt via A27/A28 om Utrecht/Amersfoort).
# ⚠️ Bestemmingsclaim Almelo blijft aannemelijk op één bron uit 2013 (brief §7)
#    — niet aan te scherpen binnen het WEBBUDGET van deze bake.
# ⚠️ Geen fase D/E (brief §6): stopt bewust bij de Urenco-verrijkingsfabriek
#    (stoppunt, geen gedocumenteerde vervolgbestemming voor déze lading).
bak_uranium_porthope_almelo() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel-geojson "zee|haven-aanloop Port Hope (schematisch, over water — MARNET reikt niet: 65,9 km van zeeknoop 4821)|$BEEN/uranium-porthope-almelo-aanloop-porthope.geojson" \
    --been         "zee|zeeschip MARNET-knoop 4821 → Rotterdam RHB (Lake Ontario/Seaway → Atlantische oversteek)|43.4992,-78.8371|51.8935,4.4585" \
    --been-geojson "truck|UF6/LEU Rotterdam RHB → Urenco Almelo-verrijkingsfabriek (A20/A12/A27/A28/A1/A35 via Knp. Gouwe–Lunetten–Rijnsweerd–Hoevelaken–Buren)|$BEEN/uranium-porthope-almelo-weg-rotterdam-almelo.geojson" \
    --marker "Port Hope Conversion Facility (Cameco), 1 Eldorado Place — laadplek (anker, hergebruikt)|43.9437,-78.2955" \
    --marker "Rotterdam — RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4 — overslag zee → truck (hergebruikt anker)|51.8935,4.4585" \
    --marker "Urenco Nederland — verrijkingsfabriek, Drienemansweg, Almelo — stoppunt (anker, bron-gelegd)|52.3391,6.6922" \
    --routebrief v2/design/routebrieven/uranium-porthope-almelo.md \
    --uit    v2/data/stroomroute-uranium-porthope-almelo.json \
    --stroom uranium-porthope-almelo \
    --titel  "Uranium · Port Hope (Cameco) → Rotterdam RHB → Urenco Almelo"
}

# ── kobalt · Huayou Tongxiang-raffinaderij (China) → Ningbo Beilun-kade → Busan New Port (Zuid-Korea)
# Routebrief: v2/design/routebrieven/kobalt-huayou-gunsan.md (LICHTE werkwijze M31 golf 2)
# ⚠️ b1 (truck, weg-scan china-extract): 192,1 km tegen ~150 km ontwerp-webcheck
#    (brief §2, geen onafhankelijk geverifieerd exact tracé) = +28,0%, BUITEN de
#    ±15%-norm. Geen via-punten uit een bron (Wikipedia/Nominatim/Photon waren
#    rate-limited, brief §4/§7) — de wegscan koos zelf de G60/G92-corridor via
#    het china-extract; geen via-punt bijgeschoven om het getal te halen
#    (bakhandleiding §5). Blijft staan als bevinding in §9.
# ⚠️ b2a (zee) routeert kade → zeeknoop: Ningbo Beilun snapt op 1,95 km van zijn
#    zeeknoop (< 5 km, LAR-586) → geen haven-aanloop aan de Ningbo-kant nodig.
#    Zeeknoop 5621 = 35.0485,128.7268 (opgehaald met hecht_marnet.marnet_zee).
# ⚠️ b2b (zee, haven-aanloop Busan, LAR-586) is VERPLICHT: Busan New Port ligt
#    10,12 km van zeeknoop 5621 (> 5 km). maak_havenaanloop.py vond een pad over
#    water (10,8 km, 6 punten, 0,00 km over land) → --stippel-geojson.
# ⚠️ Been C (Busan → LG-Huayou precursor-JV, Saemangeum-blok 6, Gunsan) is NIET
#    getekend: geen coördinaat gevonden voor het perceel (brief §5/§7, Nominatim/
#    Photon/Overpass zonder treffer) — de fabriek staat als losse knoop in de
#    brief, geen marker, geen been. Busan New Port is het stoppunt.
bak_kobalt_huayou_gunsan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|kobalttetroxide/-sulfaat Huayou Tongxiang-raffinaderij → Ningbo Beilun-kade (G60/G92 Tongxiang–Ningbo)|$BEEN/kobalt-huayou-gunsan-weg-tongxiang-ningbo.geojson" \
    --been         "zee|zeeschip Ningbo Beilun-kade → zeeknoop 5621 (Oost-Chinese Zee → Korea-straat)|29.9353,121.8695|35.0485,128.7268" \
    --stippel-geojson "zee|haven-aanloop Busan New Port (schematisch, over water — kade 10,12 km van de MARNET-zeeknoop)|$BEEN/kobalt-huayou-gunsan-aanloop-busan.geojson" \
    --marker "co-tongxiang-raffinaderij — Huayou Tongxiang-raffinaderij, Jiaxing (镍钴冶炼)|30.6167,120.5629" \
    --marker "co-ningbo-kade — Beilun Container Terminal Phase 2, Ningbo-Zhoushan (hergebruikt anker)|29.9353,121.8695" \
    --marker "co-busan-newport — Busan New Port, containerterminal (stoppunt)|35.0731,128.8338" \
    --routebrief v2/design/routebrieven/kobalt-huayou-gunsan.md \
    --uit    v2/data/stroomroute-kobalt-huayou-gunsan.json \
    --stroom kobalt-huayou-gunsan \
    --titel  "Kobalt · Huayou Tongxiang (China) → Ningbo → Busan New Port (Zuid-Korea)"
}

# ── gas · Sabine Pass LNG Terminal (VS) → Gate terminal Rotterdam (Europa-pivot-corridor 2022)
# Routebrief: v2/design/routebrieven/gas-sabinepass-rotterdam.md (lichte werkwijze M31 golf 2)
# ⚠️ Eén been (zee, MARNET kade → kade): geen fase A (diffuus VS-schaliegasnet,
#    geen enkelvoudig anker) en geen fase C (Gate-regas → GTS-invoedingspunt,
#    <5 km terreinleiding, geen OSM-pijpleiding-way gevonden) — brief §2/§6.
# ⚠️ Beide kades snappen ruim binnen de 25 km-norm én de >5 km-haven-aanloop-
#    grens (LAR-586) op een MARNET-zeeknoop: Sabine Pass 1,40 km/knoop 6220,
#    Gate-kade 1,84 km/knoop 6812 (brief §7/bak_aanwijzingen) — GEEN haven-
#    aanloop nodig.
# ⚠️ `gas-gate-kade` blijft AANNEMELIJK (Wikipedia-coördinaat): een gerichte
#    z15-satellietpass (v2/build-cache/satcheck/sat-gas-sabinepass-rotterdam-
#    gate-{a,b,nijlhaven,wide}.png) bevestigt een reëel tank-/steigercomplex
#    met aangemeerde tankers op deze coördinaat, maar kan de Gate-steiger op
#    deze schaal niet scherp scheiden van de aangrenzende Maasvlakte Olie
#    Terminal (brief §3/§7) — geen upgrade naar bron-gelegd, coördinaat
#    ongewijzigd, dus de zeeknoop-afstand (1,84 km) blijft ruim onder de norm.
# ⚠️ Geen gepubliceerde routelengte (brief §7); ontwerpschatting ~8.500–9.000 km,
#    plausibiliteitscheck tegen de gebakken olie-corpuschristi-rotterdam
#    (9.589,8 km, vergelijkbare Golfkust-VS → Rotterdam-corridor).
bak_gas_sabinepass_rotterdam() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been         "zee|LNG-carrier Sabine Pass → Rotterdam Gate (Golf van Mexico → Straat van Florida → Atlantische Oceaan → Het Kanaal/Noordzee)|29.75410,-93.87410|51.97110,4.06890" \
    --marker "gas-sabinepass-laad — Sabine Pass LNG Terminal (Cheniere), Cameron Parish, Louisiana — laadplek/LNG-exportterminal, bron-gelegd|29.75410,-93.87410" \
    --marker "gas-gate-kade — Gate terminal (Vopak/Gasunie), Maasvlakte, Rotterdam — losplek/LNG-importterminal, stoppunt, aannemelijk|51.97110,4.06890" \
    --routebrief v2/design/routebrieven/gas-sabinepass-rotterdam.md \
    --uit    v2/data/stroomroute-gas-sabinepass-rotterdam.json \
    --stroom gas-sabinepass-rotterdam \
    --titel  "Gas · Sabine Pass (VS) → Rotterdam (Gate terminal)"
}

# ── zilver · Cannington-mill (South32) → Yurbi-overslag → Townsville-haven (Berth 11, stoppunt)
# Routebrief: v2/design/routebrieven/zilver-cannington-townsville.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck, roadtrain Linfox 24/7): geen monotone lijn — de route gaat van
#    de mijn NAAR McKinlay (noordoost) en dan terug NAAR Cloncurry (noordwest)
#    voordat hij oostwaarts naar Yurbi draait. Twee scans op WEG_HOUD kaal en
#    op corridorKlassen tertiary/unclassified faalden allebei op "geen wegpad
#    tussen punt 2 en 3" (Cloncurry → Yurbi); pas met eindKlassen +track en
#    eindToegangPrivaat routeerde de scanner door (dit is een bemande,
#    dagelijkse 24/7-roadtrainroute — een verhard/berijdbaar tracé is
#    aannemelijk). 181,1 km tegen gepubliceerd 180 km (+0,6%, ruim binnen ±15%).
# ⚠️ b2 (spoor, 1-op-1-net, BAKE_SUFFIX=-raw): geen gepubliceerde deellengte
#    (brief §7) — de spoorrouter meet 763,9 km over 551 edges, verhouding 1,15
#    op de grootcirkel, 0 omkeringen ≥60° na de keerstraf. Geen via-punt nodig
#    (enkelvoudige lijn, geen corridorkeuze).
# ⚠️ Geen haven-aanloop en geen zeebeen: deze keten stopt bewust bij de kade
#    van Townsville (Berth 11) — geen bron noemt een specifieke overzeese
#    smelterbestemming (brief §6, bewust stoppunt). De haalbaarheidstoets vond
#    de Townsville-zeeknoop op 4,2 km van de kade (< 5 km-grens, LAR-586) — bij
#    een latere doortrekking met een zeebeen is dus geen haven-aanloop nodig.
bak_zilver_cannington_townsville() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|roadtrain (Linfox, 24/7) Cannington-mill → McKinlay → Cloncurry → Yurbi-overslag|$BEEN/zilver-cannington-townsville-weg-mill-yurbi.geojson" \
    --been-geojson "spoor|trein Yurbi-overslag → Townsville-haven, Berth 11 (Great Northern Railway/Mount Isa-spoorlijn, 1-op-1-net)|$BEEN/spoorroute-zilver-cannington-townsville-yurbi-townsville.geojson" \
    --marker "ag-cannington-mill — Cannington-mijn en verwerkingsfabriek (South32), laadplek|-21.8595,140.9155" \
    --marker "ag-yurbi-overslag — Yurbi rail-overslagfacility, Cloncurry — overslag truck → spoor|-20.7389,140.6557" \
    --marker "ag-townsville-haven — Haven van Townsville, Berth 11 (South32-concentraatlader), stoppunt|-19.2441,146.8358" \
    --routebrief v2/design/routebrieven/zilver-cannington-townsville.md \
    --uit    v2/data/stroomroute-zilver-cannington-townsville.json \
    --stroom zilver-cannington-townsville \
    --titel  "Zilver · Cannington-mijn (South32) → Yurbi → Townsville-haven (Berth 11)"
}

# ── koper · Aktogay-mijn (KAZ Minerals, Kazachstan) → Dostyk/Alashankou → Jinchuan-smelter (Jinchang, Gansu)
# Routebrief: v2/design/routebrieven/koper-aktogay-jinchuan.md (lichte werkwijze M31 golf 2)
# ⚠️ Pure spoorketen zonder zee (net als koper-oyutolgoi-feishang): twee benen,
#    b1 KZ (Turksib-hoofdlijn, één historische aftakking, geen via-punten), b2
#    CN (Lanxin-hoofdlijn) in ZES aparte spoorrouter-runs kop→via→via…→staart
#    (patroon uranium-inkai-poti / koper-oyutolgoi-feishang), elk apart
#    --been-geojson in reisvolgorde: Dostyk→Alashankou-grensstation→Jinghe→
#    Ürümqi→Hami-spoorstation→Wuwei→Jinchuan-smelter.
# ⚠️ Geen gepubliceerde spoor-km voor beide benen (brief §7): b1 alleen
#    ~250 km hemelsbreed, b2 alleen ~1.780 km hemelsbreed Alashankou→Jinchang —
#    de lengtetoets is hier zwak, vooral op naad-tussen-benen letten.
#    Gemeten: b1 331,3 km (grootcirkel 273,4, verhouding 1,21); b2-stukken
#    13,3 + 114,3 + 407,9 + 537,6 + 1018,1 + 103,0 = 2.194,2 km. Totaal 2.525,5 km.
# ⚠️ b2 dostyk→alashankou en alashankou→jinghe delen dezelfde OSM-omkeerpunten
#    bij Dostyk/Alashankou (166,7°/171,4°/174,1°, boogstraal 36-48 m) — dit is
#    de grensdoorlaat/breukspoor-overslag zelf (1520↔1435 mm bogiewissel), geen
#    routerfout: de trein maakt daar letterlijk een rangeerbeweging.
# ⚠️ Smelterkeuze Jinchuan blijft AANNEMELIJK (brief §6/§7): geen bron noemt
#    Jinchuan specifiek als koper-afnemer van Aktogay-concentraat, staat in de
#    stroom-/beennaam. Geen fase D/E (brief §6): geen bron noemt een
#    vervolgfabriek of Jinchuan-koper-smeltcapaciteit.
bak_koper_aktogay_jinchuan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Aktogay-mijn/concentrator → Dostyk-grensstation (Turksib-hoofdlijn, aftak 1959, 1-op-1-net)|$BEEN/spoorroute-koper-aktogay-jinchuan-aktogay-dostyk.geojson" \
    --been-geojson "spoor|trein Dostyk-grensstation → Alashankou-grensstation (breukspoor 1520↔1435 mm, verbonden 1990)|$BEEN/spoorroute-koper-aktogay-jinchuan-dostyk-alashankou.geojson" \
    --been-geojson "spoor|trein Alashankou-grensstation → Jinghe (Lanxin-hoofdlijn oostwaarts)|$BEEN/spoorroute-koper-aktogay-jinchuan-alashankou-jinghe.geojson" \
    --been-geojson "spoor|trein Jinghe → Ürümqi (Lanxin-hoofdlijn, i.p.v. Zuid-Xinjiang-lijn)|$BEEN/spoorroute-koper-aktogay-jinchuan-jinghe-urumqi.geojson" \
    --been-geojson "spoor|trein Ürümqi → Hami-spoorstation (Lanxin-hoofdlijn, ingang Hexi-corridor)|$BEEN/spoorroute-koper-aktogay-jinchuan-urumqi-hami.geojson" \
    --been-geojson "spoor|trein Hami-spoorstation → Wuwei (Lanxin-hoofdlijn door de Hexi-corridor, Gansu)|$BEEN/spoorroute-koper-aktogay-jinchuan-hami-wuwei.geojson" \
    --been-geojson "spoor|trein Wuwei → Jinchuan-smelter, Jinchang (aftakking van de Lanxin-hoofdlijn; aannemelijk: smelterkeuze niet cargo-specifiek gebrond)|$BEEN/spoorroute-koper-aktogay-jinchuan-wuwei-jinchuan.geojson" \
    --marker "cu-aktogay-laad — Aktogay-mijn + concentrator (KAZ Minerals), Abai-regio — laadplek, bron-gelegd|46.9570,79.9263" \
    --marker "cu-aktogay-grens — Dostyk-spoorstation, Jetisu-regio — grensovergang/breukspoorterminal (KZ), bron-gelegd|45.2540,82.4855" \
    --marker "cu-jinchuan-smelter — Jinchuan Group, Jinchang (Gansu) — losplek/smelter, stoppunt, aannemelijk|38.5210,102.1850" \
    --routebrief v2/design/routebrieven/koper-aktogay-jinchuan.md \
    --uit    v2/data/stroomroute-koper-aktogay-jinchuan.json \
    --stroom koper-aktogay-jinchuan \
    --titel  "Koper · Aktogay (Kazachstan) → Dostyk/Alashankou → Jinchuan-smelter (Jinchang, China)"
}

# ── zilver · Peñasquito-mijn (Newmont, Zacatecas) → Manzanillo-terminal → Onsan-smelter (Korea Zinc, Ulsan)
# Routebrief: v2/design/routebrieven/zilver-penasquito-onsan.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck, geofabrik mexico-extract) is GEMETEN en doorgetrokken, geen
#    stippel — de corridor zelf is aannemelijk (Wood Mackenzie noemt alleen de
#    afstand ~800 km, geen exact tracé, brief §7[3]), maar de lijn wordt over
#    de doorgaande Fed 54D/200D-weg gemeten: 943,6 km tegen 800 = **+18,0%,
#    buiten ±15%** — bevinding, geen via-punt bijgeschoven om het getal te
#    halen (de via-punten liggen op de brief-corridor, hemelsbreed-som 729 km,
#    en snappen allemaal ≤0,43 km).
# ⚠️ b2 (zee, haven-aanloop Manzanillo) en b4 (zee, haven-aanloop Onsan) zijn
#    beide RECHTE STIPPELS: `maak_havenaanloop.py` liep op allebei vast op
#    `timeout 300` (exit 124) — geen tweede poging, precies zoals de brief
#    voorschrijft. Manzanillo-terminal ligt 154,2 km van zeeknoop 4859, de
#    Onsan-kade 5,6 km van de zeeknoop erbuiten (LAR-586: ook binnen 25 km een
#    aanloop nodig zodra de kade > 5 km van de zeeknoop ligt).
# ⚠️ b3 (zee) is de MARNET-route tussen twee al-zeeknopen (Manzanillo-zeeknoop
#    4859 → Onsan-zeeknoop), dus dit been snapt direct — grootcirkel-orde
#    11.878 km, MARNET-vaarafstand ligt hoger (verwacht op een transpacifische
#    oversteek).
# ⚠️ b5 (truck, stippel, eigen terrein) is de 0,9 km kade → smelter binnen de
#    2 km-last-mile-drempel van de lichte werkwijze — geen apart wegprofiel.
# ⚠️ Geen fase D/E: de brief stopt bewust bij de Korea Zinc Onsan-smelter
#    (brief §6, stoppunt) — de bestemming zelf blijft "aannemelijk: één bron"
#    (brief §7, deels verouderde Goldcorp 6-K, deels 2019-CRU-bevestigd).
bak_zilver_penasquito_onsan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Peñasquito-mijn → Manzanillo-terminal (Fed 54D/200D, aannemelijke corridor, gemeten en doorgetrokken)|$BEEN/zilver-penasquito-onsan-weg-mijn-manzanillo.geojson" \
    --stippel      "zee|haven-aanloop Manzanillo (schematisch, over water — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|19.0810,-104.2975|17.98400,-103.40330" \
    --been         "zee|zeeschip Manzanillo-zeeknoop → Onsan-zeeknoop (Grote Oceaan-oversteek, transpacifisch)|17.98400,-103.40330|35.46180,129.39080" \
    --stippel      "zee|haven-aanloop Onsan (schematisch, over water — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|35.46180,129.39080|35.4180,129.3600" \
    --stippel      "truck|Onsan-kade → Korea Zinc Onsan-smelter (eigen terrein, geen net op deze korrel)|35.4180,129.3600|35.4234,129.3525" \
    --marker "Peñasquito-mijn (Newmont), Mazapil, Zacatecas — laadplek, bron-gelegd|24.6377,-101.6982" \
    --marker "Manzanillo-terminal (TIMSA/OCUPA-zone), binnenhaven — overslag truck → zee, bron-gelegd|19.0810,-104.2975" \
    --marker "Onsan-havenkade nabij Korea Zinc-smelter, Ulsan — overslag zee → truck, bron-gelegd|35.4180,129.3600" \
    --marker "Korea Zinc Onsan-smelter (power station-blok) — losplek/smelter, stoppunt, bron-gelegd|35.4234,129.3525" \
    --routebrief v2/design/routebrieven/zilver-penasquito-onsan.md \
    --uit    v2/data/stroomroute-zilver-penasquito-onsan.json \
    --stroom zilver-penasquito-onsan \
    --titel  "Zilver · Peñasquito-mijn (Mexico) → Manzanillo → Onsan-smelter (Korea Zinc, Zuid-Korea)"
}

# ── gas · North Field (Qatar, offshore) → Ras Laffan LNG-laadkade → Sodegaura LNG-terminal (Japan, Hormuz-only)
# Routebrief: v2/design/routebrieven/gas-raslaffan-chiba.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (leiding, STIPPEL) heeft geen site-anker aan de kop: North Field/South
#    Pars is een offshore gasveld van >6.000 km² zonder installatie op één
#    punt (brief §7). Kop = een schematisch veldpunt (Wikipedia-referentie-
#    coördinaat 26,6191/52,0685 aangepast naar 51,9500 — het Qatarese deel,
#    niet richting Iran), staart = het satelliet-gelegde gas-raslaffan-kade-
#    anker. km-toets is zwak (~80 km ontwerp-indicatie, geen harde bron) —
#    geen alarm bij afwijking.
# ⚠️ b2 (zee, MARNET + VERPLICHTE haven-aanloop, LAR-586): Ras Laffan-kade
#    ligt 41,5 km van de dichtstbijzijnde MARNET-zeeknoop (zeeknoop 4090,
#    26,30000/51,60000) — ver boven zowel de 5 als de 25 km-norm.
#    `maak_havenaanloop.py` SLAAGDE (cel 0,02° gebufferd, 41,6 km · 20
#    punten · 0,00 km over land) — geen terugval nodig. Sodegaura-kant heeft
#    GEEN aanloop nodig: 1,61 km tot zeeknoop 9067 (35,48190/139,97200), ruim
#    binnen de 5 km-norm. Verwachte route: Hormuz + Malakka, geen Kaap-
#    omweg; lengtetoets tegen de zwakke ~11.000–12.000 km ontwerp-indicatie
#    (brief §7) — een afwijking is eerder een correctie van de schatting dan
#    een routefout (zelfde klasse als olie-Habshan-Chiba).
# ⚠️ b3 (leiding, STIPPEL, last mile) heeft kop en staart vrijwel samen
#    (zelfde terrein als de terminal): staart is een punt ~1 km landinwaarts
#    op het JERA-centraleterrein (35,4650/139,9670, zichtbaar op
#    sat-gas-raslaffan-chiba-sodegaura-wide.png) i.p.v. een nul-lengte-
#    stippel — geen gepubliceerde leidinglengte (brief §7).
# ⚠️ Geen fase D/E: geen bron benoemt een specifieke fabriek/afnemer
#    stroomafwaarts van de Sodegaura-centrale/het Kanto-net (brief §6/§7).
bak_gas_raslaffan_chiba() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "leiding|offshore verzamelleiding North Field → Ras Laffan-kade (schematisch — subsea, niet gekarteerd)|26.6191,51.9500|25.9265,51.5955" \
    --stippel-geojson "zee|haven-aanloop Ras Laffan (schematisch, over water — kade 41,5 km van de MARNET-zeeknoop)|$BEEN/gas-raslaffan-chiba-aanloop-raslaffan.geojson" \
    --been         "zee|LNG-tanker Ras Laffan → Sodegaura (Perzische Golf → Straat van Hormuz → Arabische Zee → Straat Malakka/Singapore → Zuid-Chinese Zee → Straat Taiwan → Oost-Chinese Zee)|26.30000,51.60000|35.4675,139.9700" \
    --stippel      "leiding|terreinleiding Sodegaura-terminal → Kanto-net/JERA-centrale (schematisch — geen net op deze korrel)|35.4675,139.9700|35.4650,139.9670" \
    --marker "gas-raslaffan-kade — Ras Laffan LNG-laadsteiger (QatarEnergy LNG-complex), overslag leiding → zee|25.9265,51.5955" \
    --marker "gas-sodegaura-term — Sodegaura LNG-terminal & gascentrale (JERA), Tokiobaai, overslag zee → leiding, stoppunt-nabijheid|35.4675,139.9700" \
    --routebrief v2/design/routebrieven/gas-raslaffan-chiba.md \
    --uit    v2/data/stroomroute-gas-raslaffan-chiba.json \
    --stroom gas-raslaffan-chiba \
    --titel  "Gas · Ras Laffan (Qatar) → Sodegaura (Japan)"
}

# ── gas · Pluto LNG (Karratha, Australië) → PetroChina Jiangsu LNG-terminal (Rudong)
# Routebrief: v2/design/routebrieven/gas-karratha-rudong.md (lichte werkwijze M31 golf 2)
# ⚠️ Slechts één been getekend (zee). b1 (leiding, Pluto-gasveld → Pluto LNG,
#    180 km/36″ subzee) en b3 (leiding, Rudong-eiland → Jiangsu-gasnet) zijn
#    OPEN PUNTEN — geen brongegeven platformcoördinaat resp. geen gebrond
#    vastelandeindpunt (de eiland↔vasteland-causeway bleek op satelliet >10 km,
#    niet de veronderstelde <5 km) — brief §2/§7. Geen fase D/E.
# ⚠️ Haven-aanloop BEIDE zijden (LAR-586, kade >5 km van de zeeknoop, óók
#    binnen de 25 km-snap): Karratha-zijde zeeknoop 3878 op 5,97 km, Rudong-
#    zijde zeeknoop 9669 op 33,02 km (brief §3/§7 — nog steeds boven de
#    >5 km-drempel dan het oude Wikipedia-infoboxpunt van Karratha).
# ⚠️ Karratha-aanloop is een RECHTE STIPPEL: `maak_havenaanloop.py` liep vast
#    op timeout 300 (exit 124) — geen tweede poging.
# ⚠️ Rudong-aanloop LUKTE: 36,3 km over water, 0,00 km over land (omwegfactor
#    1,10) — het sterk verslibde Jiangsu-getijdengebied gaf desondanks een pad
#    op de 1:10M-kustlijn (dezelfde klasse als de M31-golf-1-havenaanlopen bij
#    Fujairah/Ras Tanura/Aktau, maar hier wél succesvol).
# ⚠️ Geen gepubliceerde ladingroute-lengte om het hoofdzeebeen exact tegen te
#    toetsen — alleen de ontwerpschatting ~6.000-6.500 km / grote cirkel
#    5.927 km (brief §2/§7); de ±15%-norm is hier dus zacht.
bak_gas_karratha_rudong() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "zee|haven-aanloop Karratha/Pluto LNG (schematisch — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|-20.5905,116.7755|-20.62240,116.72940" \
    --been         "zee|LNG-carrier Pluto LNG (Karratha) → Rudong LNG-terminal (Yangguang eiland) (Indische Oceaan → Straat Lombok/Makassar → Celebeszee → Zuid-Chinese Zee → Straat Taiwan → Oost-Chinese Zee)|-20.62240,116.72940|32.63010,121.09680" \
    --stippel-geojson "zee|haven-aanloop Rudong (schematisch, over water — kade 33,02 km van de MARNET-zeeknoop)|$BEEN/gas-karratha-rudong-aanloop-rudong.geojson" \
    --marker "gas-kr-pluto — Pluto LNG (Woodside), Burrup Peninsula, Karratha — overslag leiding → zee / LNG-plant, kop, bron-gelegd|-20.5905,116.7755" \
    --marker "gas-rd-eiland — PetroChina Jiangsu LNG-terminal, Yangguang (Sunshine) Island, Rudong/Nantong — overslag zee → leiding, staart/stoppunt, bron-gelegd|32.528814,121.428128" \
    --routebrief v2/design/routebrieven/gas-karratha-rudong.md \
    --uit    v2/data/stroomroute-gas-karratha-rudong.json \
    --stroom gas-karratha-rudong \
    --titel  "Gas · Pluto LNG (Karratha, Australië) → Rudong (China)"
}

# ── koper · Sentinel-mijn (Kalumbila, Zambia) → Trans-Caprivi-corridor → Walvis Bay (Namibië)
# Routebrief: v2/design/routebrieven/koper-sentinel-walvisbay.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck, Zambia) is een BEVINDING op de km-toets: gemeten 985,8 km tegen
#    ~566 km uit de brief (+74,0%, ver buiten ±15%) — de "371 km"-bronvermelding
#    (WCL-persbericht, brief §2/[3][4]) is geometrisch niet houdbaar als
#    punt-tot-puntafstand Mutanda→grens (rechte lijn alleen al ~603 km), dus die
#    beschrijft vermoedelijk het specifieke wegverbeteringstraject en niet de
#    volledige routelengte via alle genoemde tussenplaatsen. Gemeten per been:
#    Sentinel→Solwezi 158,2 km (tegen 150 gepubliceerd, +5,5%) · Solwezi→Mutanda
#    33,4 km (tegen ~45 geschat) · Mutanda→Kasempa 147,3 · Kasempa→Kaoma 219,1 ·
#    Kaoma→Mongu 190,6 · Mongu→Senanga 103,6 · Senanga→Sesheke 206,4 ·
#    Sesheke→grens 5,9 km. Geen via-punt bijgeschoven om het getal te halen (de
#    werkregel) — dit is nieuwe informatie over de brief-bronnering, geen
#    routeerfout: 8 keerlussen zijn al gesnoeid (1.064,5 → 985,0 km) en elk
#    via-punt snapt <2,4 km op zijn corridor.
# ⚠️ corridorKlassen tertiary/unclassified nodig: zonder deze klassen corridor-
#    breed toegelaten gaf de scan "geen wegpad tussen punt 0 en 1" — de
#    Sentinel-mijn hangt alleen via lokale tertiary/unclassified-wegen aan het
#    net, ver buiten de 12 km-eindzone-straal.
# ⚠️ Via-punt Mongu VERSCHOVEN 294 m t.o.v. de Wikipedia-centroïde (23,1319/
#    -15,2775 → 23,1344278/-15,2764746): de centroïde snapte op een volledig
#    geïsoleerde straatjesstomp (10 knopen, geen verbinding met het net —
#    gemeten met een component-BFS), de nieuwe coördinaat ligt op de M10-
#    doorgaande weg zelf, 294 m verderop, en snapt <5 cm. Geen coördinaat
#    verzonnen — het is een reëel OSM-punt op de doorgaande weg, dezelfde
#    aanpak als de via-punt-projectie-klasse (M28: "punten 300–500 m vóóruit
#    leggen").
# ⚠️ b2 (truck, Namibië) = 1.421,2 km tegen ~1.470 opgeteld-Wikipedia-cijfer
#    (−3,3%, ruim binnen ±15%) — B8/B1/B2 zijn nationale hoofdwegen, geen
#    corridorKlassen nodig.
# ⚠️ Geen zee-been, geen haven-aanloop: de brief stopt bij de Walvis Bay-kade
#    (stoppunt, brief §6) — geen gedocumenteerde overzeese afnemer.
bak_koper_sentinel_walvisbay() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|concentraat Sentinel-mijn → Solwezi → Mutanda → Kasempa → Kaoma → Mongu → Senanga → Sesheke → grens Katima Mulilo (Trans-Caprivi-corridor, Zambisch deel; gemeten 985,8 km tegen ~566 gepubliceerd, bevinding — zie kopcommentaar)|$BEEN/koper-sentinel-walvisbay-weg-sentinel-katimamulilo.geojson" \
    --been-geojson "truck|concentraat grens Katima Mulilo → Rundu → Otavi → Otjiwarongo → Karibib → Walvis Bay-kade (B8 → B1 → B2, Trans-Caprivi-corridor, Namibisch deel)|$BEEN/koper-sentinel-walvisbay-weg-katimamulilo-walvisbay.geojson" \
    --marker "cu-sentinel-mijn — Sentinel-mijn (Kalumbila), First Quantum Minerals — laadplek|-12.2600,25.3025" \
    --marker "Grensovergang Katima Mulilo-brug (Zambezi) — Zambia/Namibië|-17.4717,24.2499" \
    --marker "cu-walvisbay-kade — Walvis Bay-containerterminal, gereclameerd havenhoofd — stoppunt|-22.9500,14.4860" \
    --routebrief v2/design/routebrieven/koper-sentinel-walvisbay.md \
    --uit    v2/data/stroomroute-koper-sentinel-walvisbay.json \
    --stroom koper-sentinel-walvisbay \
    --titel  "Koper · Sentinel-mijn (Zambia) → Trans-Caprivi-corridor → Walvis Bay (Namibië)"
}

# ── uranium · Olympic Dam-fabriek (BHP, Roxby Downs) → Port Adelaide, Outer Harbor (Australië, truck)
# Routebrief: v2/design/routebrieven/uranium-olympicdam-portadelaide.md (LICHTE werkwijze M31 golf 2)
# ⚠️ Modaliteit (truck) is een AANNAME, kort gecheckt vóór het bakken (webbudget):
#    Friends of the Earth Adelaide bevestigt onafhankelijk dat yellowcake per
#    truck van Olympic Dam naar de dokken bij Outer Harbor gaat (brief §7[7]).
#    De BHP-EIS-vondst over een dagelijkse vrachttrein met "copper cathodes and
#    uranium oxide concentrate" (chapter-22-traffic.pdf, brief §7[6]) blijkt bij
#    een gerichte zoekronde te horen bij de NOOIT GEBOUWDE Olympic Dam Expansion
#    (2009-2011 EIS: een voorgesteld spoortracé Pimba→Olympic Dam met 14
#    treinen/week, sinds 2012 geschrapt) — geen bron bevestigt dat spoor de
#    HUIDIGE praktijk is. Eén truckbeen gebakken, geen spoorsplitsing.
# ⚠️ b1 (truck) is DOORGETROKKEN, geen stippel — het hele tracé is gekarteerde
#    hoofdweg (Stuart Hwy B97/A87 → Augusta/Princes Hwy). De aansluitstukjes op
#    de plant (toegangsweg, access=private) en op de haventerminal zijn alleen
#    routeerbaar met `eindToegangPrivaat: True` in het wegprofiel — zonder die
#    vlag stond zowel de plant als Outer Harbor op een geïsoleerd wegfragment
#    (gemeten: component 2 resp. 24 knopen, geen pad naar het hoofdnet).
# ⚠️ Lengtetoets BUITEN ±15%: 581,8 km tegen de brief-schatting ~700 km
#    (-16,9%). Blijft staan als bevinding — de referentiewaarde zelf is een
#    zwakke webcheck-schatting (grootcirkel × wegfactor, geen citaat-bron;
#    brief §7), geen gemeten hoofd-corridor die is afgesneden.
# ⚠️ Geen zeebeen: de brief stopt bindend bij de haven (geen bestemmingsland
#    gedocumenteerd voor UOC-zendingen, zoals uranium-rossing-walvisbay) → geen
#    haven-aanloop nodig, ook al ligt Outer Harbor 16,6 km van zijn MARNET-
#    zeeknoop (brief §7, overgenomen uit de haalbaarheidstoets).
bak_uranium_olympicdam_portadelaide() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|yellowcake Olympic Dam-fabriek → Port Adelaide, Outer Harbor (Stuart Highway → Augusta Highway/Princes Highway)|$BEEN/uranium-olympicdam-portadelaide-weg-olympicdam-portadelaide.geojson" \
    --marker "u-olympicdam-plant — Olympic Dam Operations (BHP, Roxby Downs), metallurgische fabriek/laadplek|-30.4400,136.8731" \
    --marker "u-portadelaide-outerharbor — Outer Harbor container-/algemene-vrachtterminal, Port of Adelaide, stoppunt|-34.7694,138.4920" \
    --routebrief v2/design/routebrieven/uranium-olympicdam-portadelaide.md \
    --uit    v2/data/stroomroute-uranium-olympicdam-portadelaide.json \
    --stroom uranium-olympicdam-portadelaide \
    --titel  "Uranium · Olympic Dam (BHP, Australië) → Port Adelaide, Outer Harbor"
}

# ── zeldzame aardmetalen · Longnan-uitloogput → Longnan-scheidingsfabriek → JL MAG Ganzhou (China intern)
# Routebrief: v2/design/routebrieven/ree-longnan-ganzhou.md (lichte werkwijze M31 golf 2)
# ⚠️ Beide benen zijn truck-only, extract china (maak_stroombeen_weg.py); geen
#    zeebenen, dus geen haven-aanloop nodig. Geen gepubliceerde km voor beide
#    benen (brief §7) — alleen referentie, geen harde ±15%-toets.
# ⚠️ b1 (uitloogput → scheidingsfabriek): 24,5 km tegen aannemelijk ~20 km
#    (referentie, licht buiten de brief-marge — bevinding, niet dichtgetrokken).
#    Anker-verbindingsstukje put → weg 2,02 km (> 0,5 km, bevinding: bergterrein,
#    laatste stuk bij de put ligt verder van de doorgaande weg dan gebruikelijk).
# ⚠️ b2 (scheidingsfabriek → JL MAG Ganzhou): 145,7 km, binnen de aannemelijke
#    marge ~130-160 km uit de brief.
# ⚠️ Naad tussen b1 en b2 op het scheidingsfabriek-anker: 0,00 km (zelfde punt,
#    geen overslag — één rechtspersoon, truck rijdt door).
# ⚠️ Anker ree-ganzhou-jlmag is een LETTERLIJKE HERGEBRUIK van w-jlmag-ganzhou
#    (v2/design/ree-sitelaag.json) — niet opnieuw satelliet-gelegd.
bak_ree_longnan_ganzhou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen ionenklei-uitloogconcentraat Longnan-uitloogput → Guanxi-stad → Longnan-scheidingsfabriek (county-weg → S225)|$BEEN/ree-longnan-ganzhou-weg-uitloogput-scheiding.geojson" \
    --been-geojson "truck|vrachtwagen RE-oxiden Longnan-scheidingsfabriek → Xinfeng → JL MAG Ganzhou (G106/S32 Longnan–Ganzhou-expressway)|$BEEN/ree-longnan-ganzhou-weg-scheiding-ganzhou.geojson" \
    --marker "ree-longnan-uitloogput — uitloogput, Zudong-district bij Guanxi (关西镇), Longnan (mijn/uitloogput, bron-gelegd)|24.8685,114.9660" \
    --marker "ree-longnan-scheiding — 赣州稀土（龙南）有色金属有限公司, Longnan-ontwikkelingszone (scheidingsfabriek, bron-gelegd)|24.84829,114.81439" \
    --marker "ree-ganzhou-jlmag — JL MAG Rare-Earth, Ganzhou (magneetfabriek, stoppunt, hergebruikt anker w-jlmag-ganzhou)|25.8406,114.8663" \
    --routebrief v2/design/routebrieven/ree-longnan-ganzhou.md \
    --uit    v2/data/stroomroute-ree-longnan-ganzhou.json \
    --stroom ree-longnan-ganzhou \
    --titel  "Zeldzame aardmetalen · Longnan-uitloogput → Longnan-scheiding → JL MAG Ganzhou (China intern)"
}

# ── koper · Olympic Dam (BHP, geïntegreerde mijn/smelter/raffinaderij) → Pimba → Port Adelaide (Inner Harbour, stoppunt)
# Routebrief: v2/design/routebrieven/koper-olympicdam-portadelaide.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck, weg) = 98,7 km tegen gepubliceerd 92 km (+7,3%, ruim binnen
#    ±15%); `eindToegangPrivaat: True` nodig (BHP-terreinweg, gated site) —
#    zonder die vlag "geen wegpad tussen punt 0 en 1".
# ⚠️ b2 (spoor, 1-op-1-net, BAKE_SUFFIX=-raw) = DRIE runs, niet vier: Pimba →
#    Port Augusta (180,3 km) → Crystal Brook (113,8 km) → Port Adelaide-kade
#    (194,1 km, in één run). Het Gawler-via-punt uit de brief (§4) is BEWUST
#    LATEN VALLEN: Crystal Brook → Gawler gaf een omkering van 173,9° (boogstraal
#    ~117 m) op -34,8606/138,5785 — de Gawler-stationsknoop hangt aan het net via
#    een lus door de Islington-rangeerknoop, dus forceren op dat exacte punt
#    reed de lijn eerst voorbij Gawler naar de Adelaide-junctie en weer terug
#    (overschiet-en-terug op een via-punt, dezelfde klasse als een via op een
#    zijtak). Crystal Brook → Port Adelaide-kade in één ongebroken run raakt
#    dezelfde junctie zonder de dubbele passage: 0 omkeringen, verhouding 1,16
#    tegen 1,50 met de geforceerde Gawler-stop. Dry Creek-via-punt bleek
#    overbodig: de Dry Creek–Port Adelaide-havenlijn zit al in het 1-op-1-net en
#    de directe run snapt er vanzelf doorheen.
#    Som b2 = 180,3 + 113,8 + 194,1 = 488,2 km tegen ~500 km (Aurizon-
#    persbericht, "roughly 500 kilometres") = −2,4%, ruim binnen ±15%. Geen
#    per-segment bron (brief §7) — alleen het totaal is te toetsen.
# ⚠️ Geen zeebeen: geen bron noemt een overzeese smelter/raffinaderij/afnemer
#    voor dit kathodevolume — de keten stopt bewust bij de kade (brief §6);
#    fase D/E vervallen.
# ⚠️ `cu-pimba-terminal` en `cu-portadelaide-kade` blijven ONZEKER (brief §3):
#    de nieuwe Aurizon-terminal bij Pimba is niet scherp te onderscheiden van
#    bestaande roadhouse-bebouwing (opname mogelijk van vóór de bouw), en het
#    exacte Berth 29-kadefront is niet gevonden via OSM/Nominatim/Photon — het
#    anker blijft het generieke Inner Harbour-bulkprecinct
#    (sat_check.py-kandidaten cand1/cand2/cand3, z15, in build-cache/satcheck/;
#    cand2 = -34,83300/138,50750, de duidelijkste kade-/loodsstrook aan het
#    water, is als anker gekozen — geen van de drie kandidaten wijkt >1 km van
#    het brief-anker af, dus geen last-mile-stippel nodig).
bak_koper_olympicdam_portadelaide() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Olympic Dam-mijn → Pimba-terminal (Olympic Dam Highway)|$BEEN/koper-olympicdam-portadelaide-weg-olympicdam-pimba.geojson" \
    --been-geojson "spoor|trein Pimba-terminal → Port Augusta (Trans-Australian Railway)|$BEEN/spoorroute-koper-olympicdam-portadelaide-pimba-portaugusta.geojson" \
    --been-geojson "spoor|trein Port Augusta → Crystal Brook (Adelaide–Port Augusta-lijn)|$BEEN/spoorroute-koper-olympicdam-portadelaide-portaugusta-crystalbrook.geojson" \
    --been-geojson "spoor|trein Crystal Brook → Port Adelaide-kade (Adelaide–Port Augusta-lijn → Dry Creek–Port Adelaide-havenspoor, ongebroken run — Gawler-via-punt liet een omkering zien en is laten vallen)|$BEEN/spoorroute-koper-olympicdam-portadelaide-crystalbrook-portadelaide.geojson" \
    --marker "cu-olympicdam-mijn — Olympic Dam mining/metallurgical complex (BHP, Roxby Downs), mijn + geïntegreerde smelter/raffinaderij, bron-gelegd|-30.4400,136.8731" \
    --marker "cu-pimba-terminal — Aurizon intermodale vrachtterminal, Pimba, overslag truck → spoor, onzeker|-31.2551,136.7997" \
    --marker "cu-portadelaide-kade — Port Adelaide, Inner Harbour, bulkmineralenprecinct (Berth 29-omgeving), losplek, stoppunt, onzeker|-34.8330,138.5075" \
    --routebrief v2/design/routebrieven/koper-olympicdam-portadelaide.md \
    --uit    v2/data/stroomroute-koper-olympicdam-portadelaide.json \
    --stroom koper-olympicdam-portadelaide \
    --titel  "Koper · Olympic Dam (BHP, Australië) → Pimba → Port Adelaide (Inner Harbour)"
}

# ── gas · Corpus Christi LNG (Cheniere, VS) → Incheon LNG-basis (KOGAS, Zuid-Korea)
# Routebrief: v2/design/routebrieven/gas-corpuschristi-incheon.md (lichte werkwijze M31 golf 2)
# ⚠️ Drie benen, alle zee — geen landbenen, geen Geofabrik-extracts nodig. Beide
#    haven-aanlopen zijn VERPLICHT (LAR-586: kade > 5 km van de MARNET-zeeknoop,
#    óók onder de 25 km-max-snap), niet een keuze bij het bakken.
# ⚠️ b1 (haven-aanloop Corpus Christi) is een RECHTE STIPPEL: `maak_havenaanloop.py`
#    liep vast op `timeout 300` (exit 124) — geen tweede poging. Kade 7,98 km van
#    zeeknoop 4843 (> 5 km, LAR-586).
# ⚠️ b2 (zee, geroutet) is de MARNET-route zeeknoop → zeeknoop via Panama; de
#    brief-km (~16.500–17.500) is zelf al een ontwerp-/webcheck-schatting, geen
#    gepubliceerde ladingroute-lengte (olie-habshan-chiba-§9-klasse) — de gemeten
#    MARNET-km is de bevinding, geen via-punt bijgeschoven.
# ⚠️ b3 (haven-aanloop Incheon) is GEMETEN: `maak_havenaanloop.py` vond een pad
#    over water (24,2 km, 18 punten, 0,00 km over land) → --stippel-geojson. Kade
#    24,17 km van zeeknoop 5633, tegen de 25 km-max-snap aan (> 5 km, LAR-586).
# ⚠️ Geen fase A/D/E (brief §1/§6/§7): fase A (Eagle Ford/Permian-schaliegasnet)
#    vervalt — diffuus net, geen enkelvoudig anker; de brief stopt bij de KOGAS
#    Incheon-regasterminal (geen fase D/E-bron binnen het webbudget).
bak_gas_corpuschristi_incheon() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "zee|haven-aanloop Corpus Christi (schematisch — kade 7,98 km van de zeeknoop)|27.8797,-97.2645|27.81110,-97.24070" \
    --been         "zee|LNG-tanker Corpus Christi LNG → Incheon LNG-terminal (via Panama)|27.81110,-97.24070|37.16690,126.41420" \
    --stippel-geojson "zee|haven-aanloop Incheon (schematisch, over water — kade 24,17 km van de MARNET-zeeknoop, tegen de 25 km-max-snap)|$BEEN/gas-corpuschristi-incheon-aanloop-incheon.geojson" \
    --marker "Corpus Christi LNG (Cheniere)|27.8797,-97.2645" \
    --marker "Incheon LNG-terminal (KOGAS)|37.3377,126.5831" \
    --routebrief v2/design/routebrieven/gas-corpuschristi-incheon.md \
    --uit    v2/data/stroomroute-gas-corpuschristi-incheon.json \
    --stroom gas-corpuschristi-incheon \
    --titel  "Gas · Corpus Christi → Incheon"
}

# ── grafiet · Nacional de Grafite Itapecerica-vestiging (Minas Gerais) → Porto de
#    Praia Mole, Vitória (Espírito Santo) — vlokgrafiet, exportcorridor BR-262
# Routebrief: v2/design/routebrieven/grafiet-itapecerica-vitoria.md (LICHTE werkwijze M31 golf 2)
# ⚠️ EEN BEEN, TRUCK, GEEN ZEE (brief §1/§6): de brief stopt bewust bij de kade —
#    geen bron koppelt Nacional de Grafite aan Praia Mole of aan een met naam
#    genoemde buitenlandse afnemer, dus fase B is niet getekend (zelfde vorm als
#    grafiet-lakecharles-desoto: doorgetrokken been, geen fase erna).
# ⚠️ GEEN GEPUBLICEERDE KM (brief §2/§7): de brief geeft alleen een ontwerp-
#    schatting (~570 km via-keten) tegen een hemelsbrede afstand van 510,5 km.
#    De gemeten weggeometrie (`maak_stroombeen_weg.py --profiel
#    grafiet-itapecerica-vitoria-itapecerica-praiamole`) komt uit op 751,5 km
#    (+31,9% t.o.v. de ontwerpschatting) — BUITEN de norm, maar per de bak-
#    aanwijzing coulanter behandeld omdat er geen bron is, alleen een corridor-
#    redenering; blijft staan als bevinding in §9, geen via-punt bijgeschoven.
# ⚠️ GEEN LAST-MILE-STIPPEL: beide anker-verbindingsstukjes snappen ruim binnen
#    de norm (plant → weg 0,03 km, weg → kade 0,04 km — beide [OK] in de
#    scan-console), dus geen aparte "last mile (geen net op deze korrel)"-
#    stippel nodig.
# ⚠️ REGISTERREGEL VOOR DE SITELAAG (brief §"bak_aanwijzingen"): de 70 kt/j-
#    capaciteit is over drie mijnen samen (Tejuco Preto/Itapecerica, Paca,
#    Califórnia) — Itapecerica's eigen aandeel niet apart bekend. Niet in deze
#    functie toegekend; hoort bij een latere sitelaag-toevoeging als
#    "sites_zonder_gewicht" of met een expliciete aggregaat-noot, niet als
#    70 kt aan dit ene punt.
bak_grafiet_itapecerica_vitoria() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Itapecerica-vestiging → Porto de Praia Mole (BR-262 via Nova Serrana → Belo Horizonte → São Domingos do Prata → Manhuaçu → Domingos Martins → Viana; geen gepubliceerde km, ontwerpschatting ~570 km)|$BEEN/grafiet-itapecerica-vitoria-weg-itapecerica-praiamole.geojson" \
    --marker "gr-itapecerica-plant — Nacional de Grafite, Itapecerica-vestiging (Mina Tejuco Preto + concentratie), laadplek, bron-gelegd|-20.4420,-45.1300" \
    --marker "gr-praiamole-kade — Porto de Praia Mole, Vitória/Serra (ES), exportterminal, stoppunt, bron-gelegd|-20.28965,-40.23500" \
    --routebrief v2/design/routebrieven/grafiet-itapecerica-vitoria.md \
    --uit    v2/data/stroomroute-grafiet-itapecerica-vitoria.json \
    --stroom grafiet-itapecerica-vitoria \
    --titel  "Grafiet · Itapecerica → Porto de Praia Mole, Vitória (Brazilië)"
}

# ── gas · NLNG-complex Bonny Island (Nigeria) → Fluxys LNG-terminal Zeebrugge (België)
# Routebrief: v2/design/routebrieven/gas-bonny-zeebrugge.md (lichte werkwijze M31 golf 2)
# ⚠️ Twee benen, geen fase A: het Niger-delta gasverzamelsysteem (feedgas naar
#    NLNG) is diffuus en niet in één tracé te vangen — het structurele
#    sabotage-/force-majeure-risico van NLNG speelt hier, vóór de kade
#    (brief §7), niet in de zeeroute.
# ⚠️ b1 (zee) snapt op BEIDE zijden > 5 km van zijn MARNET-zeeknoop (LAR-586
#    §2, óók al snapt de router zelf binnen de 25 km-grens): Bonny-jetty
#    7,94 km / zeeknoop 5231 (4,39020/7,09580), Zeebrugge-terminal 20,50 km /
#    zeeknoop 1629 (51,50000/3,40000) — bevestigd met dezelfde zeeknoop-lookup
#    als de bak_aanwijzingen van de brief. Op BEIDE zijden dus een
#    haven-aanloop nodig.
# ⚠️ Beide haven-aanlopen zijn RECHTE STIPPELS: `maak_havenaanloop.py` liep op
#    zowel Bonny (`--van 4.41836,7.16157 --naar 4.39020,7.09580`) als
#    Zeebrugge (`--van 51.3537,3.2200 --naar 51.50000,3.40000`) vast op
#    `timeout 300` (exit 124) — geen tweede poging, zoals bij Karratha/Aktau/
#    Primorsk (bakhandleiding §2).
# ⚠️ b2 (leiding, Zeebrugge-terrein) is een STIPPEL, GECONTROLEERD: een
#    pyosmium-scan op `man_made=pipeline` in de belgie-Geofabrik-extract vond
#    73 leiding-ways rond Zeebrugge (incl. de "Interconnector"- en
#    "Zeepipe"-lijnen), maar het LNG-terminal-punt (51,3537/3,2200) en het
#    netinvoedingspunt-kandidaat `gas-zeebrugge-iuk` (51,3156/3,1822) liggen
#    op TWEE VERSCHILLENDE, NIET-VERBONDEN componenten van het volledige
#    Belgische pijpleidingnet (LNG-terminal-component 118 nodes, IUK-
#    component 7 nodes, 0 gedeelde knopen) — geen doorlopende OSM-way tussen
#    de twee ankers, dus blijft een rechte stippel van 4,98 km (brief §7: OSM
#    niet gecontroleerd binnen het webbudget — nu wél gecontroleerd, negatief).
# ⚠️ `gas-zeebrugge-iuk` blijft AANNEMELIJK (brief §3/§7): OSM-terreinnaam +
#    afstandsmatch, geen bron bevestigt expliciet dat dit de Fluxys-zendlijn is.
# ⚠️ Geen fase D/E (brief §6): stoppunt is het netinvoedingspunt, het gas gaat
#    het gemengde Belgisch/NW-Europese pijpleidingnet in — geen enkelvoudige
#    "fabriek" die dit gas als eindproduct ontvangt.
bak_gas_bonny_zeebrugge() {
  python v2/tools/hecht_marnet.py route     --graaf  "$GRAAF"     --marnet "$MARNET"     --ne     "$NE"     --stippel      "zee|haven-aanloop Bonny Island (schematisch — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|4.41836,7.16157|4.39020,7.09580"     --been         "zee|LNG-tanker Bonny Island → Zeebrugge (Golf van Guinee → Straat van Gibraltar → Golf van Biskaje → Het Kanaal/Noordzee)|4.39020,7.09580|51.50000,3.40000"     --stippel      "zee|haven-aanloop Zeebrugge (schematisch — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|51.50000,3.40000|51.3537,3.2200"     --stippel      "leiding|korte terreinleiding Zeebrugge naar het net (schematisch — geen bevestigde OSM-way; twee losse pijpleidingcomponenten in de belgie-extract, niet verbonden)|51.3537,3.2200|51.3156,3.1822"     --marker "gas-bonny-nlng — Nigeria LNG Ltd, Bonny Island — productie + laadkade (LNG-complex), bron-gelegd|4.41836,7.16157"     --marker "gas-zeebrugge-lng — Fluxys LNG Zeebrugge — losplek + regasterminal, bron-gelegd|51.3537,3.2200"     --marker "gas-zeebrugge-iuk — UK Gas Interconnector Terminal-terrein (Fluxys-gaszone), Zeebrugge — netinvoedingspunt, stoppunt, aannemelijk|51.3156,3.1822"     --routebrief v2/design/routebrieven/gas-bonny-zeebrugge.md     --uit    v2/data/stroomroute-gas-bonny-zeebrugge.json     --stroom gas-bonny-zeebrugge     --titel  "Gas · Bonny Island (Nigeria) → Zeebrugge (België)"
}

# ── grafiet · Skaland Grafitverk (Senja, Noorwegen) → dorpskade → Talga Talnode-anodefabriek (Luleå, Zweden)
# Routebrief: v2/design/routebrieven/grafiet-skaland-lulea.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck) is DOORGETROKKEN weggeometrie (maak_stroombeen_weg.py, profiel
#    grafiet-skaland-lulea-skaland-mijn-skaland-kade, extract noorwegen): 1,6 km
#    tegen de eigen ongepubliceerde meting van ~0,7 km = +123,4% — BUITEN ±15%,
#    maar de brief-km zelf is een schatting op satelliet, geen gepubliceerd
#    cijfer; bevinding, geen via-punt bijgeschoven om het getal te halen.
# ⚠️ b2 (zee, haven-aanloop Skaland) is een STIPPEL: de dorpskade ligt 27,3 km
#    van MARNET-zeeknoop 4723 — groter dan elk eerder precedent (Fujairah
#    10,5 / Ras Tanura 11,1 / Aktau 7,4 km, M31 golf 1). `maak_havenaanloop.py`
#    liep vast op `timeout 300` (exit 124) — geen tweede poging (bakhandleiding
#    §2) — dus een rechte stippel Skaland-kade → zeeknoop 4723.
# ⚠️ b3 (zee, MARNET) is de doorgetrokken zeeroute zeeknoop 4723 → Talga
#    Luleå-kade (Noorse Zee → Vestfjorden/Lofoten-omvaart → Skagerrak →
#    Kattegat → Botnische Golf); lengte niet gepubliceerd, geen lengtetoets
#    mogelijk. Luleå-kade snapt zelf op 2,06 km van zeeknoop 8830 — geen
#    aparte haven-aanloop nodig aan die kant.
# ⚠️ `gr-skaland-kade` blijft ONZEKER en `gr-lulea-talnode` AANNEMELIJK
#    (brief §3/§7): geen bron bevestigt een bulkexportfunctie bij de dorpskade,
#    en het Luleå-punt landt op de kleinbotenhaven, niet aantoonbaar op het
#    Talnode-terrein — dat staat in de markernaam, niet in de lijnstijl.
# ⚠️ Kernclaim niet bevestigd (brief §7, §9): Talga's eigen Luleå-pagina noemt
#    uitsluitend eigen Vittangi-erts als feedstock, geen Skaland/Noors vlok —
#    dit blijft reserve-as (prioriteit 4), niet dichtgetrokken.
bak_grafiet_skaland_lulea() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Skaland-mijn → Skaland-dorpskade (lokale dorpsweg Skaland, geen refs; ~0,7 km eigen meting, gebakken 1,6 km)|$BEEN/grafiet-skaland-lulea-weg-skaland-mijn-skaland-kade.geojson" \
    --stippel      "zee|haven-aanloop Skaland (schematisch — MARNET reikt hier niet: kade 27,3 km van zeeknoop 4723; maak_havenaanloop.py timeout 300 s, geen tweede poging)|69.4428,17.3125|69.4797,16.6204" \
    --been         "zee|zeeschip Skaland → Talga Luleå (Noorse Zee → Vestfjorden/Lofoten-omvaart → Skagerrak → Kattegat → Botnische Golf)|69.4797,16.6204|65.58,22.15" \
    --marker "gr-skaland-mijn — Skaland Grafitverk (Skaland Graphite AS/Norge Mining), Senja — mijn/verwerkingsplant, bron-gelegd|69.4462,17.3279" \
    --marker "gr-skaland-kade — Skaland fiskerihavn, dorpskade Bergsfjorden — lokale overslag, onzeker|69.4428,17.3125" \
    --marker "gr-lulea-talnode — Talga Talnode-anodefabriek/EVA Plant, Luleå Industripark — losplek + anodefabriek, stoppunt, aannemelijk|65.58,22.15" \
    --routebrief v2/design/routebrieven/grafiet-skaland-lulea.md \
    --uit    v2/data/stroomroute-grafiet-skaland-lulea.json \
    --stroom grafiet-skaland-lulea \
    --titel  "Grafiet · Skaland (Noorwegen) → Talga Luleå (Zweden)"
}

# ── nikkel · Kawasi HPAL-complex (Obi Island) → Ningbo (Beilun, hergebruikt anker)
# Routebrief: v2/design/routebrieven/nikkel-obi-ningbo.md (lichte werkwijze M31 golf 2)
# ⚠️ Eén been (zee), geen truck-/spoorbenen — geen bron noemt een specifieke
#    Chinese precursor-/batterijfabriek als afnemer van de Obi-MHP/-sulfaat
#    (brief §6/§7); Ningbo/Beilun is patroonanalogie met
#    `nikkel-morowali-quzhou`, geen Obi-specifiek bewijs.
# ⚠️ b1 (zee, VERPLICHTE haven-aanloop, LAR-586): de Kawasi-jetty ligt 72,7 km
#    van de dichtstbijzijnde MARNET-zeeknoop (9031, -1,1099/127,9122; top-3
#    kandidaten 9031 op 72,72 km · 9034 op 79,21 km · 9036 op 93,95 km — ruim
#    boven de 5 km-norm van bakhandleiding §2). `maak_havenaanloop.py`
#    SLAAGDE op de laatste trap (cel 0,02° kaal, minste land midden op de
#    lijn) → 84,9 km · 32 punten · 1,80 km over land, geheel aan het
#    kade-uiteinde (0,00 km midden op de lijn) — dat is de 1:10M-kustkorrel,
#    geen fout. Beilun-kant heeft GEEN aanloop nodig: hergebruikt anker,
#    al aangesloten (koper-/nikkelketens).
# ⚠️ Geen gepubliceerde km voor het zeebeen zelf (brief §7): ~3.900 km is een
#    corridorschatting naar analogie van `nikkel-morowali-quzhou` (dat
#    4.202,5 km gebakken werd tegen een grotecirkel-indicatie van ~3.650 km);
#    de console-km hieronder is leidend, geen ±15%-hard-toets.
# ⚠️ Geen fase D/E: geen bron benoemt een Chinese vervolgfabriek/afnemer
#    voor het Obi-MHP/-sulfaat (brief §6).
bak_nikkel_obi_ningbo() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel-geojson "zee|haven-aanloop Kawasi (schematisch, over water — kade 72,7 km van de MARNET-zeeknoop 9031)|$BEEN/nikkel-obi-ningbo-aanloop-kawasi.geojson" \
    --been         "zee|zeeschip Kawasi (Obi) → Ningbo/Beilun-losberth (hergebruikt anker, koper-/nikkelketens — MHP/nikkelsulfaat)|-1.1099,127.9122|29.9364,121.883" \
    --marker "ni-obi-kawasi — Kawasi HPAL-complex, Obi Island (PT Halmahera Persada Lygend / PT Obi Nickel Cobalt) — mijn + HPAL + eigen exportjetty, bron-gelegd|-1.5361,127.4160" \
    --marker "ni-beilun-losberth — Ningbo–Zhoushan, Beilun-losberth (hergebruikt anker)|29.9364,121.883" \
    --routebrief v2/design/routebrieven/nikkel-obi-ningbo.md \
    --uit    v2/data/stroomroute-nikkel-obi-ningbo.json \
    --stroom nikkel-obi-ningbo \
    --titel  "Nikkel · Obi (Kawasi) → Ningbo (Beilun)"
}

# ── olie · Kozmino-exportterminal (Rusland, ESPO-terminus) → Dalian-raffinagecluster (China)
# Routebrief: v2/design/routebrieven/olie-kozmino-dalian.md (lichte werkwijze M31 golf 2)
# ⚠️ Eén zeebeen (b1), MARNET-router. Dalian als specifieke bestemming is
#    AANNEMELIJK (één bron, niet op cargo-niveau bevestigd — Kozmino verscheept
#    ook naar Rizhao/Yantai/Ningbo/Huizhou e.a., brief §1/§7); dat staat in de
#    beennaam en de brief, niet in de lijnstijl (doorgetrokken).
# ⚠️ Haven-aanloop BEIDE zijden (LAR-586, kade >5 km van de zeeknoop):
#    Kozmino-kade 56,5 km tot zeeknoop 2596 (42,70000/133,70000) —
#    `maak_havenaanloop.py` lukte (60,5 km over water, 72 punten, 0,39 km
#    "land" alleen op het kade-uiteinde zelf = de 1:10M-kustkorrel, geen echte
#    landkruising midden op de lijn) → `--stippel-geojson`. Dalian-raffinaderij
#    8,33 km tot zeeknoop 5650 (38,94870/121,74220), binnen de 25 km-snap maar
#    boven de 5 km-drempel → `maak_havenaanloop.py` liep vast op de 300 s-
#    timeout (exit 124, net als Primorsk bij `olie-primorsk-jamnagar`) → rechte
#    stippel-aanloop, geen tweede poging.
# ⚠️ Geen fase C/D/E: de brief stopt bij het raffinagecluster (§6) — geen bron
#    koppelt een specifieke ESPO-lading aan een vervolgproductstroom.
bak_olie_kozmino_dalian() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel-geojson "zee|haven-aanloop Kozmino (schematisch, over water — kade 56,5 km van de MARNET-zeeknoop)|$BEEN/olie-kozmino-dalian-aanloop-kozmino.geojson" \
    --been         "zee|zeeschip Kozmino → Dalian (Japanse Zee – Straat van Korea/Tsushima – Gele Zee)|42.70000,133.70000|38.94870,121.74220" \
    --stippel      "zee|haven-aanloop Dalian (schematisch — kade 8,33 km van de MARNET-zeeknoop; maak_havenaanloop.py-timeout, geen tweede poging)|38.94870,121.74220|38.9788,121.6539" \
    --marker "ol-kozmino-kade — Kozmino-exportterminal (Transneft, ESPO-terminus), Nachodka-baai, Primorje — laadplek/kade, bron-gelegd|42.7185,133.0090" \
    --marker "ol-dalian-raffinaderij — PetroChina Dalian Petrochemical (Dalian Petrochemical Refinery, CNPC), Ganjingzi-district — losplek/raffinaderij, stoppunt, bron-gelegd|38.9788,121.6539" \
    --routebrief v2/design/routebrieven/olie-kozmino-dalian.md \
    --uit    v2/data/stroomroute-olie-kozmino-dalian.json \
    --stroom olie-kozmino-dalian \
    --titel  "Olie · Kozmino (Rusland) → via Japanse Zee/Straat van Korea/Tsushima/Gele Zee → Dalian (China)"
}

# ── olie · Tengiz-productiecomplex (Kazachstan) → CPC-hoofdleiding → CPC Marine Terminal Novorossiysk (Zwarte Zee)
# Routebrief: v2/design/routebrieven/olie-tengiz-novorossiysk.md (lichte werkwijze M31 golf 2)
# ⚠️ Eén been (b1, leiding), geen zeebeen: CPC Blend heeft geen gedocumenteerde
#    vaste eindafnemer (brief §6, stoppunt bij de kade) — anders dan de andere
#    olie-brieven die wél doorroutet naar een raffinaderij.
# ⚠️ Eigen pyosmium-scan (geen Overpass) op kazachstan + rusland-zuid pbf,
#    filter man_made=pipeline + naam/operator ~ cpc|caspian|тенгиз|новоросс|
#    кропотк: 5 target-ways in kazachstan (waaronder 1x gedeeld met rusland-
#    zuid), 16 in rusland-zuid — 13 ways gestikt in reisvolgorde, alle naden
#    tussen opeenvolgende ways EXACT 0,000 km (gedeelde OSM-nodes). Twee
#    parallelle/alternatieve taggingtakken bij de Kalmykia-knoop (319494061/
#    072/070 vs 274735428/295): de 319494061-tak gekozen — kleinste naad naar
#    het volgende via-punt (105 km tegen 332 km voor de andere tak, conform de
#    brief-aanwijzing "kies de tak met de kleinste eindpunt-naden").
# ⚠️ ÉÉN ECHT OSM-KAARTERINGSGAT van 105,0 km tussen way 319494070 (einde
#    45,6806/43,1034) en way 319565265 (begin 45,5504/41,7664) — een bredere
#    scan zonder naamfilter (man_made=pipeline, alle substances, tot 60 km van
#    beide uiteinden) vond geen enkele bruggende oliepijplijn-way, alleen twee
#    ongerelateerde gasleidingen. Dit is geen "enkele km"-naad (bakhandleiding
#    §9-voorbeeld) maar een echt gat in de OSM-dekking op dit stuk Stavropol
#    Krai — gestippeld met reden, niet dichtgetrokken. De totale lengte inclusief
#    dit gat (1.514,4 km) klopt wél nagenoeg exact met de gepubliceerde 1.510 km
#    (+0,3%), dus het tracé zelf is correct — alleen de kartering ontbreekt hier.
# ⚠️ De laatste way (802869201) eindigt op 44,6707/37,6533, ~22 m van het
#    terminalanker (44,6705/37,6533) — de drie korte slottakken naar de losse
#    mooring-aansluitingen (802869198/199/200) zijn NIET nodig voor de
#    hoofdlijn en blijven ongebruikt.
# ⚠️ Haven-aanloop CPC Marine Terminal (LAR-586, 2026-09-28): kade ligt 16,6 km
#    van MARNET-zeeknoop 2060 (44,5897/37,8295), binnen de 25 km-snapgrens maar
#    > 5 km → haven-aanloop verplicht. maak_havenaanloop.py: 19,2 km over water,
#    0,80 km "over land" grenst aan het kade-uiteinde (de 1:10M-kustkorrel, geen
#    fout — zelfde patroon als elke andere aanloop in dit project). Geen
#    vervolgbeen ná de terminal (brief §6, geen vaste eindafnemer) — dus geen
#    zeebeen, de haven-aanloop is het laatste stuk van de stroom.
bak_olie_tengiz_novorossiysk() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "leiding|CPC-hoofdleiding (Caspian Pipeline Consortium), segment 1: Tengiz-productiecomplex → vóór het kaarteringsgat in Stavropol Krai|$BEEN/olie-tengiz-novorossiysk-leiding-tengiz-gat.geojson" \
    --stippel      "leiding|CPC-hoofdleiding, schematisch — OSM-kaarteringsgat ~105 km in Stavropol Krai (geen bruggende pipeline-way gevonden, brede scan zonder naamfilter)|45.6806,43.1034|45.5504,41.7664" \
    --been-geojson "leiding|CPC-hoofdleiding, segment 2: ná het kaarteringsgat → CPC Marine Terminal Novorossiysk|$BEEN/olie-tengiz-novorossiysk-leiding-gat-terminal.geojson" \
    --stippel-geojson "zee|haven-aanloop CPC Marine Terminal (schematisch, over water — kade 16,6 km van de MARNET-zeeknoop)|$BEEN/olie-tengiz-novorossiysk-aanloop-novo.geojson" \
    --marker "ol-tengiz-kop — Tengiz-productiecomplex (Tengizchevroil), Atyrau-oblast, Kazachstan — kop van de leiding/productiecomplex, bron-gelegd|46.1778,53.4224" \
    --marker "ol-novo-terminal — CPC Marine Terminal (onshore tankenpark), Yuzhnaya Ozereyevka, Novorossiysk, Rusland — overslag leiding → zee, stoppunt, bron-gelegd|44.6705,37.6533" \
    --routebrief v2/design/routebrieven/olie-tengiz-novorossiysk.md \
    --uit    v2/data/stroomroute-olie-tengiz-novorossiysk.json \
    --stroom olie-tengiz-novorossiysk \
    --titel  "Olie · Tengiz (Kazachstan) → CPC-hoofdleiding → Novorossiysk (CPC Marine Terminal, Zwarte Zee)"
}

# ── olie · Kharg Island-exportterminal (Iran) → Dongjiakou-olieterminal (Qingdao Port, China)
# Routebrief: v2/design/routebrieven/olie-kharg-dongjiakou.md (LICHTE werkwijze M31 golf 2)
# ⚠️ Eén been (zee, kade → kade): Perzische Golf → Straat van Hormuz (sinds
#    28-02-2026 door Iran zelf verstoord, brief §0) → Arabische Zee → Straat
#    Malakka → Zuid-Chinese Zee → Oost-Chinese Zee/Gele Zee. GEEN Suez, GEEN
#    landbenen — schaduwvloot-tankers varen doelbewust met AIS uit, dus het
#    gebakken zeebeen is de structurele/gepubliceerde route tussen de twee
#    terminals, GEEN bevestigde AIS-track van één specifieke lading (brief
#    §0/§7 — niet als "bevestigde route" herschrijven).
# ⚠️ Kharg-kant: kade snapt op 4,03 km van zeeknoop 8039 (29,24720/50,36490) —
#    BINNEN de 5 km-norm (bakhandleiding §5), dus GEEN haven-aanloop nodig.
# ⚠️ Dongjiakou-kant: kade snapt op 9,37 km van zeeknoop 5835 (35,57580/
#    119,70290) — BOVEN de 5 km-norm (structureel dunne knopendichtheid in dat
#    stuk Gele Zee, drie kandidaatpunten getest, allemaal 9,3-9,7 km, geen
#    ankerfout) → haven-aanloop nodig. `maak_havenaanloop.py` liep vast op
#    `timeout 300` (exit 124) — GEEN tweede poging, rechte stippel.
# ⚠️ Geen fase D/E (brief §6): geen bron koppelt een specifieke Iraanse lading
#    aan één met naam genoemde Shandong-teapotraffinaderij achter de terminal.
bak_olie_kharg_dongjiakou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been         "zee|zeeschip Kharg-exportterminal → Dongjiakou-olieterminal (Perzische Golf → Straat van Hormuz (verstoord sinds 28-02-2026) → Arabische Zee → Straat Malakka → Zuid-Chinese Zee → Oost-Chinese Zee/Gele Zee)|29.2230,50.3340|35.5900,119.8050" \
    --stippel      "zee|haven-aanloop Dongjiakou (schematisch — 1:10M-kust kent de haven niet: kade 9,37 km van de MARNET-zeeknoop; maak_havenaanloop.py timeout 300 s, geen tweede poging)|35.57580,119.70290|35.5900,119.8050" \
    --marker "Kharg Island-exportterminal (NIOC), T-jetty/Sea Island-steigercomplex — laadplek/exportterminal, bron-gelegd|29.2230,50.3340" \
    --marker "Dongjiakou-olieterminal (crude oil-steiger, Dongjiakou-havenzone, Qingdao Port), Shandong — losplek/VLCC-diepwaterterminal, stoppunt, bron-gelegd|35.5900,119.8050" \
    --routebrief v2/design/routebrieven/olie-kharg-dongjiakou.md \
    --uit    v2/data/stroomroute-olie-kharg-dongjiakou.json \
    --stroom olie-kharg-dongjiakou \
    --titel  "Olie · Kharg Island (Iran) → Dongjiakou (Qingdao Port, China)"
}

# ── nikkel · Voisey's Bay (Labrador) → Long Harbour (Newfoundland) — Vale's tweede eigen Atlantisch-Canadese class-1-as
# Routebrief: v2/design/routebrieven/nikkel-voiseysbay-longharbour.md (lichte werkwijze M31 golf 2)
# ⚠️ Volledig nieuwe, eigen keten — geen gedeelde geometrie met een andere stroom.
# ⚠️ b1 (truck) is een STIPPEL: sitewegen, geen openbaar net (brief §2/§7).
#    Gepubliceerde km ontbreekt; de satellietschatting was ~8,6 km hemelsbreed
#    (het ketenontwerp noemde ten onrechte "<2 km site-intern") — de rechte
#    stippel komt daar automatisch op uit.
# ⚠️ b2 (zee, VERPLICHTE haven-aanloop AAN BEIDE ZIJDEN, LAR-586): de
#    kade-ankers liggen ver van hun MARNET-zeeknoop — Voisey's Bay-kade
#    177,3 km van zeeknoop 645 (57,8113/-60,6748), Long Harbour-kade 103,9 km
#    van zeeknoop 762 (47,7000/-52,5000) — ruim boven de 5 km-norm (§2) en ook
#    ver boven de 25 km-max-snap zelf. `maak_havenaanloop.py` gaf twee
#    verschillende uitkomsten: Voisey's Bay-kant liep vast op `timeout 300`
#    (exit 124, alle acht trappen) → RECHTE STIPPEL, geen tweede poging.
#    Long Harbour-kant SLAAGDE (cel 0,005° gebufferd) → 305,0 km · 285 punten ·
#    0,00 km over land → --stippel-geojson (punten achteraf omgekeerd naar
#    zeeknoop→kade, want maak_havenaanloop.py schrijft kade→zeeknoop en de
#    reisvolgorde vraagt de aankomstrichting). Middenstuk (zeeknoop → zeeknoop)
#    is een normaal MARNET-been, geen extra via-punten (haven → haven).
#    Gepubliceerde/indicatieve km voor het hele zeebeen ~1.700 km (brief §1,
#    kustvolgend, niet gemeten — geen harde ±15%-norm, bron zegt zelf
#    "indicatief"); console-km hieronder (aanloop+midden+aanloop) is leidend.
# ⚠️ Seizoensijs (Vale's winterprogramma 22 jan–6 apr, eigen ijstracks) is NIET
#    gemodelleerd — de gebakken zeelijn is bewust de standaard zomercorridor
#    via MARNET (brief §6).
# ⚠️ b3 (truck) is een STIPPEL: eigen terrein/transportband kade → fabriek,
#    geen openbaar net (brief §2/§7), ~1,6 km.
# ⚠️ Geen fase D/E: Long Harbour Processing Plant is het stoppunt (brief §6) —
#    geen bron documenteert een vervolgzending naar een LME-entrepot of derde
#    afnemer.
bak_nikkel_voiseysbay_longharbour() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|Voisey's Bay sitewegen mijn → kade (eigen terrein, geen openbaar net)|56.3347,-62.1031|56.4115,-62.0800" \
    --stippel      "zee|haven-aanloop Voisey's Bay (schematisch — MARNET reikt niet: kade 177,3 km van zeeknoop 645; maak_havenaanloop.py timeout 300 s op alle acht trappen, geen tweede poging)|56.4115,-62.0800|57.8113,-60.6748" \
    --been         "zee|zeeschip Voisey's Bay-zeeknoop → Long Harbour-zeeknoop (Labradorkust → Straat Belle Isle/Golf van Saint-Laurent → Placentia Bay, seizoensgebonden ijsvaart — standaard zomercorridor)|57.8113,-60.6748|47.7000,-52.5000" \
    --stippel-geojson "zee|haven-aanloop Long Harbour (schematisch, over water — kade 103,9 km van de MARNET-zeeknoop 762)|$BEEN/nikkel-voiseysbay-longharbour-aanloop-longharbour.geojson" \
    --stippel      "truck|Long Harbour eigen terrein/conveyor kade → fabriek (eigen terrein, geen openbaar net)|47.4230,-53.8230|47.4101,-53.8133" \
    --marker "ni-voiseysbay-mijn — Voisey's Bay Mine (Vale Base Metals), mijn/concentrator, bron-gelegd|56.3347,-62.1031" \
    --marker "ni-voiseysbay-kade — sitefaciliteit Anaktalak Bay (kandidaat Edward's Cove-cluster), laadplek/overslag, aannemelijk|56.4115,-62.0800" \
    --marker "ni-longharbour-kade — Long Harbour-kade (Vale), overslag zee → land, bron-gelegd|47.4230,-53.8230" \
    --marker "ni-longharbour-fabriek — Long Harbour Processing Plant (Vale), raffinaderij (hydromet), stoppunt, bron-gelegd|47.4101,-53.8133" \
    --routebrief v2/design/routebrieven/nikkel-voiseysbay-longharbour.md \
    --uit    v2/data/stroomroute-nikkel-voiseysbay-longharbour.json \
    --stroom nikkel-voiseysbay-longharbour \
    --titel  "Nikkel · Voisey's Bay (Labrador) → Long Harbour (Newfoundland)"
}

# ── olie · Al Başrah Oil Terminal (Irak) → IOCL-olietankenpark/South Oil Jetty Paradip (India)
# Routebrief: v2/design/routebrieven/olie-albasrah-paradip.md (LICHTE werkwijze M31 golf 2)
# ⚠️ b1 (zee) heeft TWEE haven-aanlopen — beide kades liggen > 5 km van hun
#    dichtstbijzijnde MARNET-zeeknoop (LAR-586, ook binnen de 25 km-snap):
#    ABOT-kant 13,47 km (zeeknoop 8050, 29,8055/48,7931) — maak_havenaanloop.py
#    lukte (13,8 km over water, 0 km over land) → --stippel-geojson.
#    Paradip-kant: dichtstbijzijnde MARNET-zeeknoop ligt op 164,2 km (zeeknoop
#    2373, 21,000/88,000) — een écht dekkingsgat van MARNET in de Golf van
#    Bengalen bij de Odisha-kust (drie onafhankelijke testpunten rond Paradip
#    Port gaven allemaal ~150-165 km, brief §7). `hecht_marnet.py route`
#    bevestigt dit zelf: geeft "SNAP TE VER" bij een directe kade→kade-poging
#    (geen kortere graafroute beschikbaar). `maak_havenaanloop.py` liep vast
#    op `timeout 300` (exit 124, geen output vóór de kill) — GEEN tweede
#    poging, rechte stippel met de reden in de beennaam (bak-aanwijzing brief).
# ⚠️ b2 (leiding) is een rechte stippel: interne IOCL-pijpleiding
#    jetty → raffinaderij, niet in OSM gekarteerd (geen scan binnen het
#    webbudget) — hemelsbreed tussen twee satelliet-bevestigde ankers.
# ⚠️ ol-albasrah-term blijft status ONZEKER (brief §3): een offshore
#    SPM-boeicluster is op z15 niet als vaste structuur te onderscheiden van
#    water — dat staat in de markernaam, niet in de lijnstijl (doorgetrokken,
#    want de bestemming is aannemelijk: één bron, geen ontbrekend net).
# ⚠️ Geen fase D/E (brief §6): de brief stopt bewust bij de poort van de
#    Paradip-raffinaderij, geen bron noemt een vervolgproduct/-locatie.
bak_olie_albasrah_paradip() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel-geojson "zee|haven-aanloop Al Başrah Oil Terminal (schematisch, over water — kade 13,47 km van de MARNET-zeeknoop)|$BEEN/olie-albasrah-paradip-aanloop-albasrah.geojson" \
    --been         "zee|VLCC Al Başrah Oil Terminal-zeeknoop → Paradip-zeeknoop (Perzische Golf → Straat van Hormuz → Arabische Zee → om Sri Lanka → Golf van Bengalen)|29.8055,48.7931|21.0000,88.0000" \
    --stippel      "zee|haven-aanloop Paradip (schematisch — MARNET reikt hier niet: zeeknoop 164,2 km uit de kust, dekkingsgat Golf van Bengalen bij Odisha; maak_havenaanloop.py timeout 300 s, geen tweede poging)|21.0000,88.0000|20.2585,86.6355" \
    --stippel      "leiding|IOCL interne pijpleiding jetty → raffinaderij (schematisch — geen publieke OSM-lijn verwacht)|20.2585,86.6355|20.24764,86.59819" \
    --marker "Al Başrah Oil Terminal (ABOT/BOT, ex-Mina al-Bakr), SOMO/South Oil Company — offshore SPM-boeicluster, laadplek, onzeker|29.6848,48.8052" \
    --marker "IOCL-olietankenpark / South Oil Jetty, Paradip Port — overslag zee → leiding, bron-gelegd|20.2585,86.6355" \
    --marker "Paradip-raffinaderij (Indian Oil Corporation) — losplek/raffinaderij, stoppunt|20.24764,86.59819" \
    --routebrief v2/design/routebrieven/olie-albasrah-paradip.md \
    --uit    v2/data/stroomroute-olie-albasrah-paradip.json \
    --stroom olie-albasrah-paradip \
    --titel  "Olie · Al Başrah (Irak) → Paradip (India)"
}

# ── grafiet · Lindi Jumbo-mijn (Tanzania) → Dar es Salaam → Qingdao (China)
# Routebrief: v2/design/routebrieven/grafiet-lindijumbo-qingdao.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck) geen gepubliceerde totaallengte om tegen te toetsen — 575,4 km
#    gemeten tegen 477,9 km eigen via-keten hemelsbreed (ratio 1,20, net boven
#    de verwachte 1,1-1,2-band uit de opdracht maar geen andere corridor: de
#    router volgt exact Ruangwa → Lindi → Nangurukuru → Kibiti → Mkuranga, geen
#    kortere afsplitsing gevonden). Anker-verbindingsstukje mijn → weg 1,87 km
#    (> 0,5 km, bevinding: geen open pit zichtbaar op het satellietbeeld, het
#    complex/de toegangsweg liggen iets terug van de doorgaande regionale weg).
# ⚠️ Haven-aanloop Dar es Salaam (LAR-586, kade 19,84 km van de zeeknoop):
#    maak_havenaanloop.py gelukt, 20,7 km over water, 0,00 km over land.
# ⚠️ Haven-aanloop Qingdao (LAR-586, kade 5,59 km van de zeeknoop, óók al
#    snapt de kade binnen 25 km): maak_havenaanloop.py exit 124 (timeout
#    300 s) — GEEN tweede poging (bakhandleiding §2) → rechte stippel met
#    reden. Zelfde Qingdao-anker als grafiet-balama-laixi.md (letterlijke
#    kopie van het punt), maar géén gedeeld been — die brief is vóór LAR-586
#    gebakken en heeft daar geen aanloop voor.
# ⚠️ Geen fase C/D/E (brief §6): de brief stopt bewust op de QQCT-kade — geen
#    bron lokaliseert de IMQG- of QRGT-fabriek, hoofdafzetmarkt is India, de
#    Chinese offtakes blijven aannemelijk.
bak_grafiet_lindijumbo_qingdao() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen natuurlijk vlokgrafiet Lindi Jumbo-mijn → Ruangwa → Lindi → Nangurukuru → Kibiti → Mkuranga → Dar es Salaam-kade (regionale weg → T7 'Kilwa Road')|$BEEN/grafiet-lindijumbo-qingdao-weg-lindijumbo-daressalaam.geojson" \
    --stippel-geojson "zee|haven-aanloop Dar es Salaam (schematisch, over water — kade 19,84 km van de MARNET-zeeknoop, LAR-586)|$BEEN/grafiet-lindijumbo-qingdao-aanloop-daressalaam.geojson" \
    --been         "zee|zeeschip Dar es Salaam → Qingdao (Indische Oceaan → Straat Malakka → Zuid-Chinese Zee → Gele Zee)|-6.6537,39.3256|36.0313,120.2646" \
    --stippel      "zee|haven-aanloop Qingdao (schematisch — kade 5,59 km van de MARNET-zeeknoop, LAR-586; maak_havenaanloop.py timeout 300 s, geen tweede poging)|36.0313,120.2646|36.0124,120.2070" \
    --marker "Lindi Jumbo-mijn (Ndovu Graphite Limited), bij Matambarale/Ruangwa-district — mijn/verwerkingsfabriek, laadplek, bron-gelegd|-9.9135,38.9160" \
    --marker "Dar es Salaam Port, general cargo-/containerkade (Kurasini-kanaal) — overslag truck → zee, bron-gelegd|-6.8280,39.2870" \
    --marker "Qingdao Qianwan Container Terminal (QQCT) — losplek zee, stoppunt, hergebruikt anker (letterlijke kopie uit grafiet-balama-laixi.md, aannemelijk)|36.0124,120.2070" \
    --routebrief v2/design/routebrieven/grafiet-lindijumbo-qingdao.md \
    --uit    v2/data/stroomroute-grafiet-lindijumbo-qingdao.json \
    --stroom grafiet-lindijumbo-qingdao \
    --titel  "Grafiet · Lindi Jumbo-mijn (Tanzania) → Dar es Salaam → Qingdao (China)"
}

# ── nikkel · Sorowako (PT Vale Indonesia) → Balantang → Matsusaka (Vale Base Metals/Tokyo Nickel Co.)
#    met vertakking Niihama (Sumitomo Metal Mining)
# Routebrief: v2/design/routebrieven/nikkel-sorowako-matsuzaka.md (lichte werkwijze M31 golf 2)
# ⚠️ b1 (truck) geen gepubliceerde km — 60,2 km gemeten tegen ~60 km indicatief
#    uit het ketenontwerp (+0,4%, geen harde ±15%-toets, brief §2).
# ⚠️ b2/b4/b6 zijn haven-aanlopen (LAR-586, kade > 5 km van de MARNET-zeeknoop,
#    óók binnen de 25 km-snap): Balantang 86,95 km hemelsbreed → 90,4 km over
#    water (omwegfactor 1,04); Matsusaka 11,87 km → 12,1 km (1,02); Niihama
#    23,24 km → 25,7 km (1,10, vergelijkbaar met de ~25,7 km-aanloop in
#    nikkel-taganito-niihama.md b4, apart opnieuw gegenereerd — geen bestaand
#    geojson om te hergebruiken). Alle drie `maak_havenaanloop.py` geslaagd,
#    geen terugval nodig.
# ⚠️ b3 (zee MARNET, Balantang-zeeknoop 6080 → Matsusaka-zeeknoop 5767) meet
#    5.584,3 km tegen de indicatieve ~3.200-3.500 km uit de brief — NIET hard
#    getoetst (brief zegt zelf "indicatief, niet gemeten"); MARNET routeert
#    kennelijk niet via de kortste Straat Makassar-corridor. Bevinding, niet
#    dichtgetrokken.
# ⚠️ Vertakking b5+b6 (~20% naar Niihama, SMM): AANGEHECHT ná de hoofdbake
#    met voeg_been_toe.py --vertakt-van 2 (been 2 = de Balantang-aanloop),
#    zelfde patroon als nikkel-taganito-niihama se DSO→Hachinohe-tak. b5 (zee
#    MARNET, Balantang-zeeknoop 6080 → Niihama-zeeknoop 5746) is vooraf
#    apart gerouteerd met hecht_marnet.py route naar een los geojson (géén
#    aparte tool voor één MARNET-been bestaat) — 5.310,9 km, óók niet hard
#    getoetst (brief: "~3.300 km, schatting, analoog b3"). b6 is de
#    Niihama-haven-aanloop (nieuw --stippel-geojson op voeg_been_toe.py,
#    hecht_marnet.py-equivalent voor post-hoc aanhechten — bestond nog niet).
bak_nikkel_sorowako_matsuzaka() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|nikkel-matte PT Vale Indonesia Sorowako-mijn/smelter → Asuli → Wasuponda → Balambano → Malili → Balantang-kade (Jalan Poros Malili-Soroako)|$BEEN/nikkel-sorowako-matsuzaka-weg-sorowako-balantang.geojson" \
    --stippel-geojson "zee|haven-aanloop Balantang (schematisch, over water — kade 86,95 km van de MARNET-zeeknoop, LAR-586)|$BEEN/nikkel-sorowako-matsuzaka-aanloop-balantang.geojson" \
    --been         "zee|zeeschip Balantang-zeeknoop 6080 → Matsusaka-zeeknoop 5767 (Straat Makassar → Molukkenzee/Filipijnenzee → Japan; ~80% hoofdstroom)|-3.3140,120.6714|34.71000,136.57520" \
    --stippel-geojson "zee|haven-aanloop Matsusaka (schematisch, over water — kade 11,87 km van de MARNET-zeeknoop, LAR-586)|$BEEN/nikkel-sorowako-matsuzaka-aanloop-matsusaka.geojson" \
    --marker "PT Vale Indonesia — Sorowako-mijn en co-located mattesmelter, Danau Matano|-2.5203,121.3575" \
    --marker "Pelabuhan Balantang, Desa Balantang, Kec. Malili — exportterminal|-2.6428,121.0732" \
    --marker "Vale Base Metals/Tokyo Nickel Co. — Matsusaka-fabriek (NOS/Tonimet, ~80% hoofdstroom, stoppunt)|34.6050,136.5520" \
    --routebrief v2/design/routebrieven/nikkel-sorowako-matsuzaka.md \
    --uit    v2/data/stroomroute-nikkel-sorowako-matsuzaka.json \
    --stroom nikkel-sorowako-matsuzaka \
    --titel  "Nikkel · Sorowako → Balantang → Matsusaka (Japan) / vertakking Niihama"

  # Vertakking naar Niihama (SMM, ~20%): aangehecht ná de hoofdbake, geen
  # herbake van b1-b4 (besluit Lars 2026-08-06: bakken is geen deliverable).
  python v2/tools/voeg_been_toe.py \
    --stroom v2/data/stroomroute-nikkel-sorowako-matsuzaka.json \
    --been "zee|zeeschip Balantang-zeeknoop 6080 → Niihama-zeeknoop 5746 (vertakt van b2, ~20% van het volume naar SMM Niihama; niet gemeten in de brief-toets — console-km leidend)|$BEEN/nikkel-sorowako-matsuzaka-vertakking-niihama.geojson" \
    --vertakt-van 2

  python v2/tools/voeg_been_toe.py \
    --stroom v2/data/stroomroute-nikkel-sorowako-matsuzaka.json \
    --stippel-geojson "zee|haven-aanloop Niihama Nickel Refinery (schematisch, over water — kade 23,24 km van de MARNET-zeeknoop, LAR-586; vergelijkbaar met het ~25 km-aanloop-precedent in nikkel-taganito-niihama.md b4)|$BEEN/nikkel-sorowako-matsuzaka-aanloop-niihama.geojson" \
    --marker "Niihama Nickel Refinery, Sumitomo Metal Mining — raffinaderij (stoppunt kathode, vertakking)|33.9669,133.2658" \
    --vertakt-van 5
}

# ── NIEUWE STROOMFUNCTIES HIERBOVEN INVOEGEN (vóór de dispatch) ──
# Generieke dispatch (2026-09-26): het argument `<grondstof>-<slug>` wordt de
# functie `bak_<grondstof>_<slug>` (streepje → underscore). Een nieuwe stroom
# vraagt dus alleen een functie hierboven, geen regel hier.
arg="${1:-}"; naam="bak_${arg//-/_}"   # ${1:-} eerst: zonder argument geeft set -u anders "unbound variable"
if [ -n "${1:-}" ] && declare -F "$naam" >/dev/null; then "$naam"
else echo "gebruik: bash v2/tools/bak_stromen.sh <stroom>; bekend:" >&2
     declare -F | sed -n 's/^declare -f bak_//p' | tr '_' '-' >&2; exit 2; fi
