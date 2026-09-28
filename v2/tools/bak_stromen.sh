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

# ── diamant · Alrosa Mirny-mijn (Rusland) → Sheremetyevo-Cargo (Moskou) → CSMIA (Mumbai) → Bharat Diamond Bourse
# Routebrief: v2/design/routebrieven/diamant-mirny-mumbai.md (lichte werkwijze M31 golf 3, §2 Lucht — eerste
# lucht-bake van dit project, letterlijk volgens bakhandleiding-licht.md §2 "Lucht").
# ⚠️ Twee luchtbenen (b2 MJZ→SVO 4.150,4 km · b3 SVO→BOM 5.049,0 km), beide DOORGETROKKEN
#    grootcirkels tussen satelliet-gelegde vrachtterminals (geen bron noemt een tussenlanding/hub
#    → één directe vlucht per etappe, aanname in brief §7). Geen gepubliceerde vluchtlengte
#    (per definitie berekend, is de bron zelf).
# ⚠️ Twee truckbenen (b1 mijn→MJZ, b4 BOM→BDB), BEIDE doorgetrokken (geen stippel — geen
#    airside/privéterrein-uitzondering nodig, beide eindigen op de vrachtterminal resp. beginnen
#    erop via de openbare weg). Geen gepubliceerde km voor beide (brief geeft alleen hemelsbreed-
#    schattingen); de gebakken weggeometrie valt BUITEN ±15% van die hemelsbreed-schattingen
#    (b1 3,5 km tegen ~2,2 km hemelsbreed/+59% — ~3 km wegschatting uit het ontwerp geeft +17%;
#    b4 8,4 km tegen ~3,9 km hemelsbreed/+114%) — dat is geen fout, hemelsbreed is nooit een
#    wegtoets; blijft staan als bevinding in §9, niet dichtgetrokken.
# ⚠️ Geen zee-, spoor- of leidingbeen; geen haven-aanloop nodig (geen zeebeen in deze keten).
# ⚠️ dia-bom-cargo is op OSM-POI-niveau gelegd (parking van het vrachtcomplex, geen los
#    vrachtgebouw op z15 te onderscheiden — brief §7); dia-bdb is een hergebruikt anker uit een
#    eerdere keten van deze golf (Bandra-Kurla Complex).
# ⚠️ Geen fase D/E: de brief stopt bij de beurs (§6) — Bharat Diamond Bourse is een
#    beurs-/exportgebouw, geen slijperij; geen bron koppelt Mirny-rough aan een specifieke
#    vervolgfabriek (vermoedelijk Surat, buiten deze keten).
bak_diamant_mirny_mumbai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Mir-mijn/sorteercentrum → Mirny Airport MJZ (stadsweg Mirny)|$BEEN/diamant-mirny-mumbai-weg-mijn-mjz.geojson" \
    --been-geojson "lucht|vlucht MJZ → SVO (vrachtvlucht, grootcirkel)|$BEEN/diamant-mirny-mumbai-lucht-mjz-svo.geojson" \
    --been-geojson "lucht|vlucht SVO → BOM (vrachtvlucht, grootcirkel)|$BEEN/diamant-mirny-mumbai-lucht-svo-bom.geojson" \
    --been-geojson "truck|vrachtwagen CSMIA Air Cargo Complex → Bharat Diamond Bourse (Airport Road/BKC-connector)|$BEEN/diamant-mirny-mumbai-weg-bom-bdb.geojson" \
    --marker "dia-mirny-mijn — Alrosa Mir-mijn/sorteercentrum, Mirny — mijn/laadplek, bron-gelegd|62.5258,113.9842" \
    --marker "dia-mirny-mjz — Mirny Airport (MJZ), vrachtterminal (Alrosa Mirny Air Enterprise) — vertrek luchtvracht, bron-gelegd|62.5344,114.0222" \
    --marker "dia-svo-cargo — Sheremetyevo-Cargo, Moskou — vrachtterminal aankomst+vertrek (Alrosa verkooporganisatie), bron-gelegd|55.9696,37.4362" \
    --marker "dia-bom-cargo — CSMIA Air Cargo Complex, Sahar, Mumbai — vrachtterminal aankomst, aannemelijk (OSM-POI-niveau)|19.0994,72.8673" \
    --marker "dia-bdb — Bharat Diamond Bourse, BKC, Mumbai — beursgebouw/bestemming, stoppunt, bron-gelegd (hergebruikt anker)|19.0641,72.8646" \
    --routebrief v2/design/routebrieven/diamant-mirny-mumbai.md \
    --uit    v2/data/stroomroute-diamant-mirny-mumbai.json \
    --stroom diamant-mirny-mumbai \
    --titel  "Diamant · Mirny (Rusland) → Moskou (Sheremetyevo-Cargo) → Mumbai (CSMIA/BDB)"
}

# ── pgm · Stillwater Mine (Nye, Montana) → Columbus Metallurgical Complex
# Routebrief: v2/design/routebrieven/pgm-stillwater-columbus.md (lichte werkwijze M31 golf 3)
# ⚠️ Eén been (fase A truck), geen zee/spoor/lucht: fase B/C/D/E vervallen —
#    Sibanye-Stillwater's eigen 20-F noemt de afnemer van de PGM-rijke filter
#    cake alleen als "a third-party refiner", zonder naam of locatie (brief §6,
#    stoppunt bij de smelterpoort; bindende haalbaarheidstoets — geen
#    vertakking naar een plausibele raffinaderij).
# ⚠️ Geen stippel: beide uiteinden liggen op het bestaande wegnet — mijn heeft
#    een verharde toegangsweg naar CR-419 bij Nye, smelterterrein grenst direct
#    aan Pike Avenue in Columbus (brief §2; gecontroleerd tijdens het bakken,
#    snap ≤ 2 km op beide ankers).
# ⚠️ Toetswaarde 64 km (40 mi, Encyclopedia.com [7]), niet de ontwerp-indicatie
#    van ~50 km (brief §7) — venster 54–74 km (±15%).
bak_pgm_stillwater_columbus() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Stillwater Mine → Columbus Metallurgical Complex (Nye Road/CR-419 → MT-78)|$BEEN/pgm-stillwater-columbus-weg-stillwater-columbus.geojson" \
    --marker "pgm-stillwater-laad — Stillwater Mine (Sibanye-Stillwater), Nye, Stillwater County — mijn/concentrator, bron-gelegd|45.3880,-109.8920" \
    --marker "pgm-columbus-smelter — Columbus Metallurgical Complex (Sibanye-Stillwater) — smelter + base metal refinery, stoppunt, bron-gelegd|45.6330,-109.2400" \
    --routebrief v2/design/routebrieven/pgm-stillwater-columbus.md \
    --uit    v2/data/stroomroute-pgm-stillwater-columbus.json \
    --stroom pgm-stillwater-columbus \
    --titel  "PGM · Stillwater Mine → Columbus"
}

# ── diamant · Ekati-mijnvliegveld → Yellowknife (splitsing) → Brussels Brucargo → Antwerpen AWDC
# Routebrief: v2/design/routebrieven/diamant-ekati-antwerpen.md (LICHTE werkwijze M31 golf 3,
# EERSTE bake met een luchtbeen — v2/design/bakhandleiding-licht.md §2 "Lucht").
# ⚠️ ⚠️ EKATI IS SINDS 14-07-2026 IN RECEIVERSHIP (brief §7, bron [12][13]): de mijn wordt
#    binnen enkele weken daarna afgebouwd/gereclameerd. Deze keten beschrijft de historische/
#    ontworpen as, niet aantoonbaar de actuele operatie op 28-09-2026 — gemeld, niet
#    stilzwijgend gebakken.
# ⚠️ b1+b2 (lucht): DOORGETROKKEN, geen stippel — grootcirkel tussen twee vrachtterminals,
#    ankers satelliet-gelegd (brief §3/§9 sat_check.py). Gemeten grootcirkel b1 = 311,4 km
#    (brief noemde 312,4; Wikipedia publiceert ~310 km — binnen norm). b2 YZF→BRU = 6.316,8 km
#    gemeten (brief noemde 6.319,2; ontwerp-schatting was ~6.700 km, niet gebruikt) — geen
#    tussenlanding gebrond, één directe vlucht (§7 van de brief).
# ⚠️ dia-yzf-splitsing blijft AANNEMELIJK: bronnen noemen alleen "een metaal-beklede loods
#    bij het vliegveld" zonder adres/operator; het anker staat op het GA-vrachtplatform
#    oostzijde YZF (bron-gelegd voor het terrein, niet voor het specifieke pand).
# ⚠️ b3 (truck, Brucargo → AWDC, E19): 44,5 km tegen ~40 km ontwerp = +11,3% — buiten ±10%
#    maar binnen de ±15%-norm, bevinding, niet dichtgetrokken. Beide anker-verbindingen zijn
#    triviaal klein (0,05 / 0,09 km) → GEEN stippel nodig, geen last-mile-gat.
# ⚠️ Geen zeebeen, dus geen MARNET/haven-aanloop. Fase D/E vervallen (brief §6, stoppunt AWDC).
bak_diamant_ekati_antwerpen() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "lucht|vlucht Ekati-strip → YZF (vrachtvlucht, grootcirkel)|$BEEN/diamant-ekati-antwerpen-lucht-ekati-yzf.geojson" \
    --been-geojson "lucht|vlucht YZF → BRU (vrachtvlucht, grootcirkel)|$BEEN/diamant-ekati-antwerpen-lucht-yzf-bru.geojson" \
    --been-geojson "truck|Brucargo → AWDC Antwerpen (E19)|$BEEN/diamant-ekati-antwerpen-weg-brucargo-awdc.geojson" \
    --marker "dia-ekati-strip — Ekati Airport (mijnstrip, geen permanente weg) — vertrekpunt lucht, bron-gelegd|64.69891,-110.61439" \
    --marker "dia-yzf-splitsing — vrachtapron/GA-terrein oostzijde Yellowknife Airport — overslag lucht→lucht, aannemelijk|62.46850,-114.42500" \
    --marker "dia-brucargo — Brucargo, Brussels Airport — vrachtterminal, overslag lucht→truck, bron-gelegd|50.90628,4.45584" \
    --marker "dia-awdc — AWDC/Diamond Office, Hoveniersstraat, Antwerpen — handels-/certificeringshub, stoppunt, bron-gelegd|51.21520,4.41870" \
    --routebrief v2/design/routebrieven/diamant-ekati-antwerpen.md \
    --uit    v2/data/stroomroute-diamant-ekati-antwerpen.json \
    --stroom diamant-ekati-antwerpen \
    --titel  "Diamant · Ekati (Canada) → Yellowknife → Brussel (Brucargo) → Antwerpen (AWDC)"
}

# ── pgm · Copper Cliff-smelter (Vale, Sudbury, ON) → Port Colborne-raffinaderij (Vale, ON)
# Routebrief: v2/design/routebrieven/pgm-sudbury-actonuk.md (LICHTE werkwijze M31 golf 3)
# ⚠️ ALLEEN been b1 (fase A, spoor) gebakken: b2 (exporthaven Canada — Montreal
#    of Halifax, geen bron kiest), b3 (zeeoversteek) en b4 (VK-haven → Acton)
#    zijn NIET getekend — drie ankers staan open (brief §7), geen coördinaat
#    verzonnen. De brief eindigt bij Vale Europe's Acton-raffinaderij in tekst;
#    de getekende lijn stopt bij Port Colborne (brief §6, stoppunt).
# ⚠️ Geen lucht: geen bron noemt luchtvracht/beveiligde koerier voor deze as
#    (bron_voor_luchtvracht: n.v.t. in het ontwerp) — golf 3's "lucht"-
#    tooling is voor déze keten niet van toepassing.
# ⚠️ b1 is VIER RUNS op het 1-op-1-spoornet (BAKE_SUFFIX=-raw, "3260717
#    spoor-edges" bevestigd), kop → via MacTier → via Hamilton/CPKC Kinnear
#    Yard → via Welland → staart: 233,0 + 266,2 + 68,0 + 35,6 = 602,8 km.
#    Geen gepubliceerde lengte om tegen te toetsen (de ~700 km in de brief is
#    een webcheck-schatting, geen harde norm, brief §2/§7) — 602,8 km is de
#    gemeten vervanging.
# ⚠️ TWEE OMKERINGEN blijven staan, beide vlak bij het Port Colborne-eind van
#    de reis (Hamilton→Welland-run: 178,9°, boogstraal ~171 m, 42,96070/
#    -79,27110; Welland→Port Colborne-run: 180,0°, boogstraal ~55 m,
#    42,96850/-79,20050) — zelfde klasse als de kopmaak-omkeringen bij
#    nikkel-sudbury-kristiansand/nikkel-norilsk-monchegorsk: reëel op een
#    emplacement/industrieel spoor bij een raffinaderij, niet dichtgetrokken
#    (werkwijze §5: buiten de norm = bevinding).
# ⚠️ Geen haven-aanloop: geen zeebeen in dit stuk (brief §2/bak_aanwijzingen).
# ⚠️ `pgm-coppercliff-smelter` en `pgm-portcolborne-refinery` zijn beide
#    bron-gelegd op z15/z16 (brief §3, satcheck-PNG's in de brief-bronnenlijst).
bak_pgm_sudbury_actonuk() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Copper Cliff-smelter → MacTier (CP Parry Sound Subdivision — trekt de route zuidwaarts richting Toronto/Zuid-Ontario)|$BEEN/spoorroute-pgm-sudbury-actonuk-coppercliff-mactier.geojson" \
    --been-geojson "spoor|trein MacTier → Hamilton/CPKC Kinnear Yard (CP-hoofdlijn, grootste rangeerknoop in de Golden Horseshoe)|$BEEN/spoorroute-pgm-sudbury-actonuk-mactier-hamilton.geojson" \
    --been-geojson "spoor|trein Hamilton/CPKC Kinnear Yard → Welland (Welland-corridor, route buigt hier zuidwaarts naar Port Colborne)|$BEEN/spoorroute-pgm-sudbury-actonuk-hamilton-welland.geojson" \
    --been-geojson "spoor|trein Welland → Port Colborne-raffinaderij (Welland-corridor, doorgaande tak)|$BEEN/spoorroute-pgm-sudbury-actonuk-welland-portcolborne.geojson" \
    --marker "pgm-coppercliff-smelter — Vale Copper Cliff Complex, smelter, Sudbury, ON — kop van het spoor, bron-gelegd|46.47860,-81.05473" \
    --marker "pgm-portcolborne-refinery — Vale Port Colborne Refinery, Ontario — tussenraffinaderij (PGM/Au/Ag-intermediair + elektro-kobalt), stoppunt, bron-gelegd|42.88350,-79.24300" \
    --routebrief v2/design/routebrieven/pgm-sudbury-actonuk.md \
    --uit    v2/data/stroomroute-pgm-sudbury-actonuk.json \
    --stroom pgm-sudbury-actonuk \
    --titel  "PGM · Copper Cliff (Sudbury) → Port Colborne (Ontario)"
}

# ── pgm · Zimplats SMC (Zimbabwe) → Beitbridge → Rustenburg PMR (Zuid-Afrika, matte over land)
# Routebrief: v2/design/routebrieven/pgm-zimplats-rustenburg.md (LICHTE werkwijze M31 golf 3)
# ⚠️ Geen luchtbeen in deze as (brief §6/§7): de PGM-matte reist volledig over
#    land; alleen het geraffineerde metaal ná Rustenburg PMR vliegt, en dat is
#    hier bewust niet getekend (geen bron noemt een vervolgzending).
# ⚠️ b1 (Zimplats SMC → Beitbridge) is +47,3% BOVEN het ketenontwerp (663,0 km
#    tegen ~450 km) — buiten ±15%, bevinding uit de brief zelf (§7): de
#    ketenontwerp-indicatie lag al duidelijk onder de eigen via-puntensom
#    (~600-650 km geschat, 663,0 km gemeten). Geen via-punt geschrapt; mogelijk
#    bestaat een kortere Harare-bypass die niet gevonden is.
# ⚠️ b2 (Beitbridge → Rustenburg PMR) is +16,4% BOVEN het ketenontwerp
#    (582,1 km tegen ~500 km) — de eigen via-puntensom (~526 km) lag binnen
#    ±15%, maar de gemeten weggeometrie (met keerlussen/first-last-mile) komt
#    er net buiten. Bevinding, niet dichtgetrokken.
# ⚠️ Beitbridge-anker (pgm-beitbridge-grens, -22.2244,29.9865) is IDENTIEK aan
#    het bestaande anker in koper-kolwezi-durban.md — bewust hergebruikt.
#    Harare/Masvingo/Polokwane-via-punten eveneens uit die brief hergebruikt.
bak_pgm_zimplats_rustenburg() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|matte Zimplats SMC → Chegutu → Harare → Beatrice → Chivhu → Masvingo → Beitbridge (A5 → A4/A1)|$BEEN/pgm-zimplats-rustenburg-weg-smc-beitbridge.geojson" \
    --been-geojson "truck|matte Beitbridge → Musina → Polokwane → Pretoria → Rustenburg PMR (N1 → N4)|$BEEN/pgm-zimplats-rustenburg-weg-beitbridge-rustenburg.geojson" \
    --marker "pgm-zimplats-smc — Zimplats Selous Metallurgical Complex, mijn/smelter, bron-gelegd|-18.0328,30.4334" \
    --marker "pgm-beitbridge-grens — Beitbridge grensovergang (Limpopo-brug), overslag tussen twee truckcorridors, bron-gelegd, gedeeld anker|-22.2244,29.9865" \
    --marker "pgm-rustenburg-pmr — Rustenburg PMR (Waterval-complex, Valterra Platinum), eindraffinaderij, stoppunt, bron-gelegd|-25.6838,27.3272" \
    --routebrief v2/design/routebrieven/pgm-zimplats-rustenburg.md \
    --uit    v2/data/stroomroute-pgm-zimplats-rustenburg.json \
    --stroom pgm-zimplats-rustenburg \
    --titel  "PGM · Zimplats SMC (Zimbabwe) → Beitbridge → Rustenburg PMR (Zuid-Afrika)"
}

# ── diamant · Jwaneng-mijn (Botswana) → Gaborone DTP → GBE-vrachtapron → Brucargo (BRU) → Antwerpen (AWDC)
# Routebrief: v2/design/routebrieven/diamant-jwaneng-antwerpen.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# Vier benen, ALLE DOORGETROKKEN, geen stippels.
# ⚠️ b3 (lucht) is een GROOTCIRKEL GBE → BRU (maak_luchtbeen.py), 8.651,7 km —
#    binnen de verwachte 8.650-8.660 km (eigen sferische berekening 8.652 km;
#    ontwerp noemde ~8.850 km). Doorgetrokken: een vlucht tussen twee gelegde
#    vrachtterminals is geen "net reikt niet"-geval. Geen bron voor een
#    tussenlanding → één directe vlucht aangenomen (brief §7).
# ⚠️ dia-gbe-cargo (GBE-vrachtapron) is AANNEMELIJK: geen OSM-gebouw met
#    "Cargo" in de naam, anker = hangaar/apron-cluster naast de terminal
#    (satellietbeeld z17, brief §3).
# ⚠️ dia-gaborone-dtp gebruikt de "Diamond Technology Park"-polygoon in de
#    Diamond Hub SEZ (sinds 2017) i.p.v. het exacte DBGSS-gebouw, dat niet met
#    naam is gevonden in OSM/Nominatim/Photon (brief §7).
bak_diamant_jwaneng_antwerpen() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|ruwe diamant Jwaneng-mijn → Gaborone Diamond Technology Park (Trans-Kalahari Corridor/A2 via Sese–Kanye–Moshupa–Gabane)|$BEEN/diamant-jwaneng-antwerpen-weg-jwaneng-gaborone.geojson" \
    --been-geojson "truck|ruwe diamant Gaborone DTP → GBE-vrachtapron (Airport Road)|$BEEN/diamant-jwaneng-antwerpen-weg-gaborone-gbe.geojson" \
    --been-geojson "lucht|vlucht GBE → BRU (vrachtvlucht, grootcirkel)|$BEEN/diamant-jwaneng-antwerpen-lucht-gbe-bru.geojson" \
    --been-geojson "truck|ruwe diamant Brucargo → AWDC/Diamond Office Antwerpen (E19 via Mechelen)|$BEEN/diamant-jwaneng-antwerpen-weg-brucargo-antwerpen.geojson" \
    --marker "dia-jwaneng-mill — Jwaneng-mijn concentrator-/fabriekscomplex (Debswana), laadplek, bron-gelegd|-24.5303,24.7083" \
    --marker "dia-gaborone-dtp — Diamond Technology Park, Gaborone (De Beers/DBGSS sight-aggregatie, Diamond Hub SEZ), bron-gelegd|-24.5899,25.9149" \
    --marker "dia-gbe-cargo — Sir Seretse Khama Int'l Airport, vrachtapron/hangaar, aannemelijk|-24.5576,25.9242" \
    --marker "dia-bru-cargo — Brucargo, Brussels Airport, bron-gelegd|50.9056,4.4576" \
    --marker "dia-antwerp-awdc — AWDC/Diamond Office, Hoveniersstraat 22 Antwerpen, stoppunt, bron-gelegd|51.2154,4.4185" \
    --routebrief v2/design/routebrieven/diamant-jwaneng-antwerpen.md \
    --uit    v2/data/stroomroute-diamant-jwaneng-antwerpen.json \
    --stroom diamant-jwaneng-antwerpen \
    --titel  "Diamant · Jwaneng → Gaborone/Brussels Airport → Antwerpen"
}

# ── diamant · Namdeb Oranjemund (Namibië) → NDTC Windhoek → Hosea Kutako (WDH) → Brussels Airport (BRU) → Antwerpen (AWDC)
# Routebrief: v2/design/routebrieven/diamant-namdeb-gaborone.md (LICHTE werkwijze M31 golf 3)
# ⚠️ Bestemming Gaborone VERVANGEN door Antwerpen (brief kop/§1, bindend uit de
#    haalbaarheidstoets): geen bron dat Namibische rough naar Botswana
#    doorvliegt; NDTC is een eigen 50/50-JV die zelf in Windhoek sights houdt.
# ⚠️ Grootste open punt (brief §7, NIET getekend): de fysieke aanvoer van
#    marien naar de wal is een helikoptersprong (Debmarine-schip → Oranjemund,
#    3×/week, De Beers Group 2022) — het scheeppunt is varend en dus niet te
#    pinnen zonder een coördinaat te verzinnen; de keten begint bij het
#    Namdeb-terrein, niet bij het schip.
# ⚠️ b1 (truck, Oranjemund → Windhoek): 975,4 km tegen ~900 ontwerp = +8,4%
#    [binnen ±15%]. dia-namdeb-oranjemund blijft AANNEMELIJK: kantoorpand
#    (OSM office=company "MRM Namdeb"), niet aantoonbaar het exacte
#    helikopter-landingsterrein (brief §7).
# ⚠️ b2 (truck, Windhoek → WDH): 44,6 km tegen 45 (Wikipedia) = -1,0% [OK].
#    dia-wdh-cargo blijft AANNEMELIJK: terminal-/vrachtapron van een kleine
#    regionale internationale luchthaven, geen apart Cargo-gebouw te
#    onderscheiden op z16-z17 (brief §7).
# ⚠️ b3 (lucht, WDH → BRU): DOORGETROKKEN, geen stippel — grootcirkel tussen
#    twee vrachtterminals, ankers satelliet-gelegd/hergebruikt (brief §3/§9).
#    Gemeten grootcirkel 8.260,1 km (brief noemde 8.259,7 — binnen norm). Geen
#    tussenlanding gebrond, één directe vlucht (brief §7).
# ⚠️ b4 (truck, Brucargo → AWDC): LETTERLIJKE HERGEBRUIK van het gebakken
#    geojson van diamant-ekati-antwerpen b3 (identieke Brucargo→AWDC/E19-
#    route, zelfde twee ankers dia-brucargo/dia-awdc) — geen tweede
#    weg-scan/profiel. 44,5 km tegen ~40 ontwerp (uit die zusterbrief).
# ⚠️ Windhoek → Antwerpen (na WDH) is AANNEMELIJK, niet per zending gebrond
#    voor Namibische rough specifiek — hergebruikt patroon van de andere
#    diamantketens in deze golf (brief §7).
bak_diamant_namdeb_gaborone() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|ruwe diamant Namdeb-terrein Oranjemund → NDTC/Namdeb-sortering Windhoek (B4 → B1 via Rosh Pinah–Aus–Keetmanshoop–Mariental–Rehoboth)|$BEEN/diamant-namdeb-gaborone-weg-oranjemund-windhoek.geojson" \
    --been-geojson "truck|ruwe diamant NDTC/Namdeb-sortering Windhoek → Hosea Kutako Airport WDH-vrachtapron (B6)|$BEEN/diamant-namdeb-gaborone-weg-windhoek-wdh.geojson" \
    --been-geojson "lucht|vlucht WDH → BRU (vrachtvlucht, grootcirkel)|$BEEN/diamant-namdeb-gaborone-lucht-wdh-bru.geojson" \
    --been-geojson "truck|ruwe diamant Brucargo → AWDC Antwerpen (E19, letterlijk hergebruikt uit diamant-ekati-antwerpen b3)|$BEEN/diamant-ekati-antwerpen-weg-brucargo-awdc.geojson" \
    --marker "dia-namdeb-oranjemund — Namdeb-kantoor/terrein, Oranjemund — laadplek (marien, helikopterlanding), aannemelijk|-28.55284,16.42375" \
    --marker "dia-ndtc-windhoek — NDTC/Namdeb-kantoor, Frans Indongo Street, Windhoek Central — overslag/verwerkingsknoop (sortering/sight), bron-gelegd|-22.56482,17.08384" \
    --marker "dia-wdh-cargo — Hosea Kutako International Airport (WDH), terminal-/vrachtapron — vrachtterminal, overslag truck→lucht, aannemelijk|-22.4863,17.4643" \
    --marker "dia-brucargo — Brucargo, Brussels Airport — vrachtterminal, overslag lucht→truck, bron-gelegd (hergebruikt anker)|50.90628,4.45584" \
    --marker "dia-awdc — AWDC/Diamond Office, Hoveniersstraat, Antwerpen — handels-/certificeringshub, stoppunt, bron-gelegd (hergebruikt anker)|51.21520,4.41870" \
    --routebrief v2/design/routebrieven/diamant-namdeb-gaborone.md \
    --uit    v2/data/stroomroute-diamant-namdeb-gaborone.json \
    --stroom diamant-namdeb-gaborone \
    --titel  "Diamant · Namdeb Oranjemund (Namibië) → Windhoek → Brussel (Brucargo) → Antwerpen (AWDC)"
}

# ── pgm · Rustenburg PMR (Valterra Platinum, Zuid-Afrika) → OR Tambo (JNB) → Shanghai Pudong (PVG, China)
# Routebrief: v2/design/routebrieven/pgm-rustenburg-shanghai.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ Eerste luchtbeen-bake in dit project (bakhandleiding §2): grootcirkel JNB→PVG
#    via maak_luchtbeen.py, 11.787,1 km — DOORGETROKKEN, geen stippel (een vlucht
#    tussen twee gelegde vrachtterminals is geen gat). Geen tussenlanding aangenomen
#    (geen bron noemt een hub, routebrief §7).
# ⚠️ b1 (truck, eindToegangPrivaat) — het wegprofiel geeft 178,0 km tegen het
#    ~120 km-ontwerpcijfer uit de brief (+48,4%, buiten ±15%). Dit is de gemeten
#    N4 (Rustenburg–Brits–Pretoria) → N1/R21 (Pretoria–Midrand–Kempton Park), niet
#    dichtgetrokken (bakhandleiding §5/§6: het ontwerpcijfer was indicatief, de
#    bake-uitvoer is de echte controle) — bevinding, zie §9 van de brief.
# ⚠️ Geen stippel nodig: beide ankers liggen aan openbare industrie-/luchthaven-
#    terreinwegen (snap 0,17/0,04 km); `eindToegangPrivaat` liet de laatste km bij
#    het JNB-vrachtplatform over kleine wegklassen toe zonder een aparte stippel.
# ⚠️ Geen fase C/D (brief §6, bindende haalbaarheidstoets): geen met naam genoemde
#    Chinese eindfabriek/-entrepot gevonden — de stroom eindigt op de PVG-vracht-
#    terminal.
bak_pgm_rustenburg_shanghai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Rustenburg PMR → OR Tambo vrachtterminal (N4/N1/R21)|$BEEN/pgm-rustenburg-shanghai-weg-rustenburg-jnb.geojson" \
    --been-geojson "lucht|vlucht JNB → PVG (vrachtvlucht, grootcirkel)|$BEEN/pgm-rustenburg-shanghai-lucht-jnb-pvg.geojson" \
    --marker "pgm-rustenburg-pmr — Rustenburg PMR + Waterval-smelter-/RBMR-complex (Valterra Platinum), laadplek, bron-gelegd|-25.6750,27.3180" \
    --marker "pgm-jnb-cargo — O.R. Tambo International Airport, vrachtplatform/-loodsen, overslag truck → lucht, bron-gelegd|-26.1380,28.2270" \
    --marker "pgm-pvg-cargo — Shanghai Pudong International Airport, vrachtplatform/-loodsen, stoppunt, bron-gelegd|31.1335,121.8025" \
    --routebrief v2/design/routebrieven/pgm-rustenburg-shanghai.md \
    --uit    v2/data/stroomroute-pgm-rustenburg-shanghai.json \
    --stroom pgm-rustenburg-shanghai \
    --titel  "PGM · Rustenburg PMR (Zuid-Afrika) → OR Tambo (JNB) → Shanghai Pudong (PVG)"
}

# ── pgm · Impala Rustenburg-mijnencluster → Impala Springs Refinery → OR Tambo-vrachtterminal → (vlucht) → Zürich Airport → edelmetaalkluis Kloten
# Routebrief: v2/design/routebrieven/pgm-springs-zurich.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, NIET stippel) is +59,8% BOVEN de eigen schatting (255,7 km tegen
#    ~160 km "uit het ketenontwerp, geen aparte bron" — brief §2). Buiten ±15%,
#    bevinding, niet dichtgetrokken: de N4→N1→N12-corridor via Centurion en
#    Johannesburg is een reële omweg t.o.v. de hemelsbrede schatting, en er is
#    geen gepubliceerde bronlengte om tegen te toetsen. Via-punten (Marikana/
#    Centurion/Johannesburg N1-N12-knoop/Germiston) komen uit de brief zelf.
# ⚠️ b2 (truck, NIET stippel): 41,3 km tegen ~40 km (+3,2%) [OK].
# ⚠️ b3 (lucht, DOORGETROKKEN — geen stippel, bakhandleiding §2): vlucht
#    JNB → ZRH als grootcirkel, 8.417,1 km. Geen tussenlanding gebrond (brief
#    §7: geen bron noemt een hub) → één directe vrachtvlucht, aangenomen als
#    industriestandaard voor ZA-PGM-luchtvracht (brief §8[1]/[4]/[5]). Beide
#    vrachtterminal-ankers zijn satelliet-gelegd (bron-gelegd, brief §3).
# ⚠️ b4 (truck) is een STIPPEL, GEEN gewoon wegbeen: `maak_stroombeen_weg.py`
#    vond GEEN wegpad tussen het Zürich Airport-vrachtplatform en de Kloten-
#    kluis, ook niet met `eindToegangPrivaat: True` (twee scans, beide
#    "corridor niet gerouteerd: geen wegpad tussen punt 0 en 1" — de graaf in
#    dit venster verbindt de twee ankers niet, geen classificatieprobleem).
#    Conform de bak-aanwijzing in de opdracht: "tenzij het wegtool geen route
#    vindt binnen het privéterrein van de kluis, dan --stippel ... met reden."
#    Dit is dus geen "aannemelijk"-kwestie maar een net-reikt-niet-geval.
# ⚠️ `pgm-zurich-kluis` (Loomis Schweiz AG, Steinackerstrasse Kloten) staat op
#    status AANNEMELIJK (brief §3/§7: één indirecte bron, geen bevestigd
#    huisnummer) — dit been mag gewoon doorgetrokken/gestippeld gebakken
#    worden (het is een brongeschil over de exacte locatie, geen "net reikt
#    niet"-geval voor het ANKER zelf); vermeld hier voor de keuring: dit anker
#    hoort in een latere ronde geverifieerd te worden tegen een primaire
#    Loomis-bron (brief §7).
# ⚠️ Geen fase D/E (brief §6): de brief stopt bewust bij de Kloten-kluis, geen
#    bron noemt een specifieke Zwitserse afnemer/verwerker van déze partij.
bak_pgm_springs_zurich() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Impala Rustenburg-mijnencluster → Impala Springs Refinery (N4 → N1 → N12)|$BEEN/pgm-springs-zurich-weg-rustenburg-springs.geojson" \
    --been-geojson "truck|vrachtwagen Impala Springs Refinery → OR Tambo-vrachtterminal (N12 → N3/R21)|$BEEN/pgm-springs-zurich-weg-springs-ortambo.geojson" \
    --been-geojson "lucht|vlucht JNB → ZRH (vrachtvlucht, grootcirkel, aannemelijk: industriestandaard)|$BEEN/pgm-springs-zurich-lucht-jnb-zrh.geojson" \
    --stippel      "truck|Zürich Airport vrachtplatform → edelmetaalkluis Kloten (schematisch — geen wegpad gevonden in het OSM-net tussen vrachtplatform en kluis, ook niet met eindToegangPrivaat; last mile Zürich-Kloten)|47.4647,8.5492|47.4474,8.6046" \
    --marker "pgm-rustenburg-mijn — Impala Platinum Rustenburg-mijnencluster — mijn/laadplek, bron-gelegd|-25.5535,27.2176" \
    --marker "pgm-springs-raffinaderij — Impala Refining Services, Springs (Implats) — overslag/raffinaderij, bron-gelegd|-26.2227,28.4437" \
    --marker "pgm-ortambo-vrachtterminal — OR Tambo-vrachtterminal (Swissport/Menzies Cargo, Northern Perimeter Road) — overslag/lucht, bron-gelegd|-26.1211,28.2472" \
    --marker "pgm-zrh-vrachtterminal — Zürich Airport vrachtplatform — overslag/lucht, bron-gelegd|47.4647,8.5492" \
    --marker "pgm-zurich-kluis — Edelmetaalkluis Loomis Schweiz AG, Steinackerstrasse, Kloten — losplek/kluis, stoppunt, aannemelijk|47.4474,8.6046" \
    --routebrief v2/design/routebrieven/pgm-springs-zurich.md \
    --uit    v2/data/stroomroute-pgm-springs-zurich.json \
    --stroom pgm-springs-zurich \
    --titel  "PGM · Impala Rustenburg → Springs → OR Tambo (JNB) → vrachtvlucht → Zürich (ZRH) → Kloten-kluis"
}

# ── diamant · Mbuji-Mayi (DR Congo) → Kinshasa (N'djili, CEEC) → Dubai (DXB) → DMCC
# Routebrief: v2/design/routebrieven/diamant-mbujimayi-dubai.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ Vier benen, alle DOORGETROKKEN — geen enkele stippel (bakhandleiding §2):
#    b1/b4 zijn gewone openbare stadswegen boven de "korter dan ~2 km / airside
#    zonder openbare weg"-stippeldrempel; b2/b3 zijn luchtbenen (per definitie
#    doorgetrokken, "grootcirkel" staat in de beennaam).
# ⚠️ b2 (lucht, DOORGETROKKEN): vlucht MJM → FIH als grootcirkel, 919,2 km —
#    BINNENLANDSE verzamelvlucht binnen DR Congo (geen internationale grens);
#    aangenomen op één zin in design/diamant.md §4a, niet apart bevestigd op
#    cargo-niveau (brief §7, open punt).
# ⚠️ b3 (lucht, DOORGETROKKEN): vlucht FIH → DXB als grootcirkel, 5.421,3 km.
#    Géén tussenlanding gebrond (brief §7: geen bron noemt een hub) → één
#    directe vrachtvlucht, aanname staat in de brief.
# ⚠️ b1 (truck, geen stippel): het wegprofiel geeft 4,2 km tegen het
#    ~5 km-ontwerpcijfer (-15,7%, net buiten de ±10%-toolwaarschuwing maar
#    binnen de ±15%-norm van de brief) — geen betrouwbare gepubliceerde
#    wegreferentie beschikbaar (bakhandleiding §5/§6), bevinding, niet
#    dichtgetrokken.
# ⚠️ b4 (truck, geen stippel, door de haalbaarheidstoets toegevoegd): 31,0 km
#    tegen ~34 km (hemelsbreed 29,0 km + verwachte omweg) = -8,9% [OK].
# ⚠️ dia-mbm-miba is een stadscentrum-anker (aannemelijk, brief §3/§7): géén
#    apart MIBA-omheind terrein of pit te onderscheiden op z14. dia-fih-term is
#    het luchthaventerrein, niet het CEEC-kantoor zelf (CEEC-locatie niet
#    adresseerbaar binnen budget, brief §7).
# ⚠️ Geen fase D/E (brief §6, bindende haalbaarheidstoets): de brief stopt
#    bewust bij DMCC/Almas Tower — geen bron koppelt de rough aan een
#    specifieke vervolgbestemming (bv. een slijperij in Surat).
bak_diamant_mbujimayi_dubai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|MIBA-terrein/exportkantoor, Mbuji-Mayi → Mbuji-Mayi Airport (MJM) (Avenue Inga, stadsverbinding)|$BEEN/diamant-mbujimayi-dubai-weg-miba-mjm.geojson" \
    --been-geojson "lucht|vlucht MJM → FIH (binnenlandse verzamelvlucht, grootcirkel)|$BEEN/diamant-mbujimayi-dubai-lucht-mjm-fih.geojson" \
    --been-geojson "lucht|vlucht FIH → DXB (vrachtvlucht, grootcirkel)|$BEEN/diamant-mbujimayi-dubai-lucht-fih-dxb.geojson" \
    --been-geojson "truck|DXB-vrachtterminal → DMCC/Almas Tower (Airport Road → Sheikh Zayed Road/Al Ittihad Road)|$BEEN/diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson" \
    --marker "dia-mbm-miba — MIBA-terrein/exportkantoor, Mbuji-Mayi — mijn/laadplek, aannemelijk|-6.1300,23.6000" \
    --marker "dia-mbm-mjm — Mbuji-Mayi Airport (MJM) — vrachtterminal, overslag truck → lucht, bron-gelegd|-6.1188177,23.5682265" \
    --marker "dia-fih-term — N'djili International Airport (FIH), Kinshasa — vrachtterminal + CEEC-certificering, overslag lucht → lucht, bron-gelegd|-4.3840685,15.4508775" \
    --marker "dia-dxb-cargo — Dubai Intl Airport (DXB), vrachtcomplex (Emirates SkyCargo/Cargo Village) — overslag lucht → truck, bron-gelegd|25.2574524,55.3405972" \
    --marker "dia-dmcc — DMCC / Almas Tower, Jumeirah Lake Towers, Dubai — handels-/beurshub, stoppunt, bron-gelegd|25.0690625,55.1411656" \
    --routebrief v2/design/routebrieven/diamant-mbujimayi-dubai.md \
    --uit    v2/data/stroomroute-diamant-mbujimayi-dubai.json \
    --stroom diamant-mbujimayi-dubai \
    --titel  "Diamant · Mbuji-Mayi (DR Congo) → Kinshasa (N'djili) → Dubai (DXB) → DMCC"
}

# ── pgm · Rustenburg PMR → OR Tambo-vrachtterminal → (vlucht) → Narita-vrachtterminal → Tanaka Kikinzoku Kogyo, Tokio
# Routebrief: v2/design/routebrieven/pgm-rustenburg-tokio.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ `pgm-rustenburg-pmr` GECORRIGEERD t.o.v. de eigen brief (§7 open punt): het
#    v1-registercoördinaat -25,9500/27,3000 bleek op z14 landbouwgrond met
#    center-pivot-irrigatie, geen raffinaderij. Hergebruikt het satelliet-
#    gelegde Waterval-smelter/RBMR/PMR-complex-anker (-25,6750/27,3180) uit de
#    zusterbrieven van dezelfde golf/grondstof: pgm-rustenburg-shanghai.md
#    (bron-gelegd, z16-z17) + pgm-zimplats-rustenburg.md + pgm-mogalakwena-
#    londen.md ("hergebruikt anker" + eigen z16-bevestiging). Brief-tekst zelf
#    NIET gewijzigd (conform de instructie); de correctie staat hier + in §9.
# ⚠️ b1 (truck, NIET stippel) is +48,3% BOVEN de ~120 km uit het ketenontwerp
#    (178,0 km gemeten over N4→N1→R21 via Kroondal/Brits/Pretoria-West/
#    Allandale) — buiten ±15%, bevinding, niet dichtgetrokken: dezelfde
#    corridor gaf in de zusterbrief pgm-mogalakwena-londen al een eigen
#    OSRM-check van 166 km tegen hetzelfde ~120 km-ontwerpcijfer; de
#    N4/N1/R21-corridor is structureel langer dan de hemelsbrede schatting.
#    `eindToegangPrivaat`/`eindKlassen` gezet voor de OR Tambo-vrachtterminal-
#    kant (luchthaventerrein deels airside/privé) — de scan vond desondanks een
#    doorgaand pad, dus geen stippel nodig.
# ⚠️ b2 (lucht, DOORGETROKKEN — geen stippel, bakhandleiding §2): vlucht
#    JNB → NRT als grootcirkel, 13.582,6 km — de langste luchtafstand van de
#    negen PGM/goud/diamant-ketens van deze golf (brief §0/§1). Geen
#    tussenlanding gebrond (brief §7: geen bron noemt een hub) → één directe
#    vrachtvlucht, aangenomen als industriestandaard voor ZA-PGM-luchtvracht
#    (brief §8). Beide vrachtterminal-ankers zijn satelliet-gelegd
#    (bron-gelegd, brief §3).
# ⚠️ b3 (truck, NIET stippel) is +14,6% BOVEN de ~65 km uit het ketenontwerp
#    (74,5 km gemeten over Higashi-Kanto Jidoshado → Keiyo-weg → Wangan-route)
#    — net BUITEN de ±10%-tool-waarschuwing maar BINNEN de ±15%-norm van de
#    brief [OK].
# ⚠️ `pgm-tanaka-tokio` is het Tanaka-HOOFDKANTOOR/handelsadres in Chuo-ku,
#    Tokio, geen bevestigd fabrieksterrein (Tanaka's fabrieken liggen in
#    Hiratsuka/Isehara, Kanagawa) — status AANNEMELIJK, expliciet open punt
#    voor Lars in de brief §7, hier ongewijzigd doorgezet als stoppunt.
# ⚠️ Geen fase D/E (brief §6): de brief stopt bewust bij Tanaka's hoofdkantoor,
#    géén bron noemt een fabriek/afnemer ná deze ontvangst.
bak_pgm_rustenburg_tokio() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Rustenburg PMR → OR Tambo vrachtterminal (N4/N1/R21)|$BEEN/pgm-rustenburg-tokio-weg-rustenburg-jnb.geojson" \
    --been-geojson "lucht|vlucht JNB → NRT (vrachtvlucht, grootcirkel)|$BEEN/pgm-rustenburg-tokio-lucht-jnb-nrt.geojson" \
    --been-geojson "truck|Narita vrachtterminal → Tanaka Kikinzoku Kogyo, Tokio (Higashi-Kanto → Keiyo → Wangan)|$BEEN/pgm-rustenburg-tokio-weg-narita-tanaka.geojson" \
    --marker "pgm-rustenburg-pmr — Rustenburg PMR + Waterval-smelter-/RBMR-complex (Valterra Platinum), laadplek, bron-gelegd (hergebruikt+gecorrigeerd, zie kop)|-25.6750,27.3180" \
    --marker "pgm-jnb-vracht — O.R. Tambo Cargo Terminal, Kempton Park (JNB), overslag truck → lucht, bron-gelegd|-26.1400,28.2300" \
    --marker "pgm-nrt-vracht — Narita Cargo Area (NRT), overslag lucht → truck, bron-gelegd|35.7743,140.3797" \
    --marker "pgm-tanaka-tokio — Tanaka Kikinzoku Kogyo K.K., hoofdkantoor Nihonbashi-Kayabacho, Chuo-ku, Tokio, stoppunt, aannemelijk|35.6816,139.7756" \
    --routebrief v2/design/routebrieven/pgm-rustenburg-tokio.md \
    --uit    v2/data/stroomroute-pgm-rustenburg-tokio.json \
    --stroom pgm-rustenburg-tokio \
    --titel  "PGM · Rustenburg PMR (Zuid-Afrika) → OR Tambo (JNB) → Narita (NRT) → Tanaka Kikinzoku Kogyo, Tokio"
}

# ── pgm · Nadezhda-smelter (Norilsk) → Alykel (NSK) → Yemelyanovo (KJA) → Krastsvetmet-raffinaderij (Krasnojarsk)
# Routebrief: v2/design/routebrieven/pgm-norilsk-krasnojarsk.md (LICHTE werkwijze M31 golf 3, §2 Lucht).
# ⚠️ b1 (spoor, Norilsk-industrienet) is GEMETEN, geen stippel: beide uiteinden snappen op
#    hetzelfde geïsoleerde component van 253 km (Nadezhda-knoop 0,73 km / Alykel-knoop 6,17 km),
#    exact het component uit nikkel-norilsk-monchegorsk.md — de kandidaat-stippel uit de brief
#    ("component-mismatch") deed zich dus niet voor. 27,3 km over 32 edges, verhouding 1,12.
# ⚠️ De 6,17 km-snap bij Alykel is een STIPPEL (spoor|…): OSM kent geen doorgaand zijspoor tot op
#    het vrachtplatform — consistent met de al onzekere Alykel-vrachtterminal-status (brief §3/§7,
#    geen bron voor een aparte cargo-faciliteit). Naad > 5 km, bakhandleiding §2 "Emplacementen…
#    missen vaak" — niet dichtgetrokken.
# ⚠️ b2 (lucht NSK → KJA) is DOORGETROKKEN grootcirkel, 1.484,3 km — gemotiveerd met Norilsk's
#    aantoonbare isolatie (geen weg/doorgaande spoorverbinding met het nationale net), niet met een
#    PGM-specifieke bron; bindende aanpassing van de haalbaarheidstoets (brief §7/§8[8]).
# ⚠️ b3 (truck Yemelyanovo → Krastsvetmet): Overpass was onbereikbaar bij het schrijven van de
#    brief; via-punten hier zelf gepind met pyosmium op de lokale rusland-siberie-extract. De brief
#    vermoedde "R257 zuidwaarts" — dat bleek de VERKEERDE kant van de stad (R257/Predmostnaya loopt
#    juist zuidwestwaarts naar Abakan); de echte luchthavenweg is R-255 "Sibir" → Северное шоссе/
#    Енисейский тракт → Октябрьский мост (Jenisej-oversteek) → Krastsvetmet-terrein. Gemeten
#    weglengte 53,2 km tegen de herziene toetswaarde ~40 km = +32,9% — BUITEN ±15%, bevinding, niet
#    dichtgetrokken (een reële stadsroute via twee ringwegen is nu eenmaal langer dan een
#    hemelsbreed-keten van vier via-punten; 04А-300/R-255/04К-044 zijn niet-hemelsbrede stadswegen).
#    Eerste 0,76 km (vrachtterminal-anker → eerste primary-knoop 04А-300) is een STIPPEL: het hele
#    kleine-klasse-wegennet rond de cargoterminal bestaat in OSM uit eilandjes van 4-7 knopen zonder
#    gedeelde knoop met het doorgaande net (component-scan, zelfde klasse als cu-beilun-laadspoor).
# ⚠️ pgm-alykel-vrachtterminal blijft ONZEKER (brief §3): satellietbeeld z17 toont geen apart
#    vrachtplatform/loods; mogelijk gaat PGM als bijvracht mee, geen aparte cargo-bron gevonden.
# ⚠️ Geen zeebeen, dus geen haven-aanloop.
bak_pgm_norilsk_krasnojarsk() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Nadezhda-smelter → Alykel-vrachtplatform (Norilsk Railway — geïsoleerd industrieel net, ~253 km-component)|$BEEN/spoorroute-pgm-norilsk-krasnojarsk-nadezhda-alykel.geojson" \
    --stippel      "spoor|laatste zijspoor naar het Alykel-vrachtplatform ontbreekt in OSM (geen doorgaand net tot op het platform — Alykel-status al onzeker, brief §3/§7)|69.3796,87.3598|69.3252,87.3290" \
    --been-geojson "lucht|vlucht NSK → KJA (vrachtvlucht, grootcirkel)|$BEEN/pgm-norilsk-krasnojarsk-lucht-alykel-yemelyanovo.geojson" \
    --stippel      "truck|Yemelyanovo-vrachtterminal → doorgaand wegnet 04А-300 (OSM-topologiebreuk — kleine-klasse-wegennet rond de cargoterminal is een los eilandje, geen zijspoor van meer dan 2 km)|56.1785,92.5250|56.1718,92.5275" \
    --been-geojson "truck|vrachtwagen Yemelyanovo-vrachtterminal → Krastsvetmet-raffinaderij (R-255 \"Sibir\" → Северное шоссе/Енисейский тракт → Октябрьский мост)|$BEEN/pgm-norilsk-krasnojarsk-weg-yemelyanovo-krastsvetmet.geojson" \
    --marker "pgm-nadezhda-fabriek — Nadezhda Metallurgical Plant, Norilsk (Nornickel Polar Division), mijn/smelter (kop spoor), bron-gelegd (hergebruikt anker ni-nadezhda-fabriek)|69.3275,87.9521" \
    --marker "pgm-alykel-vrachtterminal — Alykel International Airport (NSK), Norilsk, vrachtplatform (kop lucht), onzeker (geen aparte cargo-bron)|69.3252,87.3290" \
    --marker "pgm-yemelyanovo-vrachtterminal — Krasnoyarsk International Airport / Yemelyanovo (KJA), vrachtplatform (losplek lucht), bron-gelegd|56.1785,92.5250" \
    --marker "pgm-krastsvetmet-raffinaderij — Krastsvetmet (Krasnoyarsk Non-Ferrous Metals Plant), Транспортный проезд 1, Krasnojarsk, raffinaderij, stoppunt, bron-gelegd|56.0160,92.9998" \
    --routebrief v2/design/routebrieven/pgm-norilsk-krasnojarsk.md \
    --uit    v2/data/stroomroute-pgm-norilsk-krasnojarsk.json \
    --stroom pgm-norilsk-krasnojarsk \
    --titel  "PGM · Norilsk (Rusland) → Alykel (NSK) → Krasnojarsk (KJA) → Krastsvetmet"
}

# ── pgm · Mogalakwena-concentrator (Valterra Platinum, Zuid-Afrika) → Rustenburg PMR → OR Tambo (JNB) → (vlucht) → Heathrow (LHR) → Johnson Matthey Royston (Verenigd Koninkrijk)
# Routebrief: v2/design/routebrieven/pgm-mogalakwena-londen.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, NIET stippel): Mogalakwena-concentrator → Rustenburg PMR, N1 →
#    R24 "Platinum Highway". 336,4 km tegen het werkcijfer 341 km (eigen OSRM-
#    meting, geen operator-bron) = -1,3% [OK]. Ontwerpcijfer ~180 km was fors
#    onderschat (routebrief §7, bevinding, niet dichtgetrokken).
# ⚠️ b2 (truck, NIET stippel) — GEDEELD BEEN, LETTERLIJK HERGEBRUIKT: Rustenburg
#    PMR → OR Tambo is dezelfde corridor als in pgm-rustenburg-shanghai.md
#    (zelfde golf 3); dit been hergebruikt het al gebakken geojson
#    `pgm-rustenburg-shanghai-weg-rustenburg-jnb.geojson` (ankers identiek:
#    -25.6750,27.3180 → -26.1380,28.2270) i.p.v. het een derde keer te bakken
#    (routebrief §7, bak-aanwijzing).
# ⚠️ b3 (lucht, DOORGETROKKEN — geen stippel, bakhandleiding §2): vlucht
#    JNB → LHR als grootcirkel, 9.071,9 km, reeds gegenereerd met
#    maak_luchtbeen.py. Geen tussenlanding gebrond (brief §7) → één directe
#    vrachtvlucht, aannemelijk analoog aan de goud-/Rand Refinery-luchtvracht-
#    praktijk vanuit Zuid-Afrika (geen PGM-specifieke bron voor déze vlucht
#    gevonden binnen het budget).
# ⚠️ b4 (truck, NIET stippel, eindToegangPrivaat): Heathrow World Cargo Centre
#    → Johnson Matthey Royston, M4 → M25 → A1(M) → A505. 101,9 km tegen 97
#    (+5,0% [OK]) — BINDEND-tekst noemde ~50 km via M25/A10/A505; de A1(M) is
#    hier het functionele equivalent van de genoemde A10 (routebrief §7).
#    `eindToegangPrivaat` nodig: zonder die vlag vond het wegtool geen pad
#    tussen Baldock Bypass en het JM Royston-terrein.
# ⚠️ Geen fase D/E (brief §6, bindende haalbaarheidstoets): Johnson Matthey
#    Royston is de BINDEND aangewezen eindraffinage (LPPM good-delivery), geen
#    bron noemt een vervolgzending naar een specifieke afnemer/fabriek.
bak_pgm_mogalakwena_londen() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Mogalakwena-concentrator → Rustenburg PMR (N1 → R24 \"Platinum Highway\")|$BEEN/pgm-mogalakwena-londen-weg-mogalakwena-rustenburg.geojson" \
    --been-geojson "truck|Rustenburg PMR → OR Tambo vrachtterminal (N4/N1/R21, gedeeld been uit pgm-rustenburg-shanghai)|$BEEN/pgm-rustenburg-shanghai-weg-rustenburg-jnb.geojson" \
    --been-geojson "lucht|vlucht JNB → LHR (vrachtvlucht, grootcirkel)|$BEEN/pgm-mogalakwena-londen-lucht-jnb-lhr.geojson" \
    --been-geojson "truck|Heathrow World Cargo Centre → Johnson Matthey Royston (M4 → M25 → A1(M) → A505)|$BEEN/pgm-mogalakwena-londen-weg-heathrow-royston.geojson" \
    --marker "pgm-mogalakwena-mijn — Mogalakwena-concentrator, Valterra Platinum, Mokopane, Limpopo, laadplek, bron-gelegd|-23.9805,28.9160" \
    --marker "pgm-rustenburg-pmr — Rustenburg PMR (Waterval-smelter/RBMR/PMR-complex), Valterra Platinum, overslag, bron-gelegd (hergebruikt anker)|-25.6750,27.3180" \
    --marker "pgm-jnb-cargo — OR Tambo (JNB) vrachtplatform/-loodsen, Kempton Park, overslag truck → lucht, bron-gelegd (hergebruikt anker)|-26.1380,28.2270" \
    --marker "pgm-lhr-cargo — Heathrow (LHR) World Cargo Centre, overslag lucht → truck, bron-gelegd|51.4703,-0.4195" \
    --marker "pgm-jm-royston — Johnson Matthey Royston PGM-raffinaderij, Orchard Road Industrial Estate, Royston, Hertfordshire, stoppunt, bron-gelegd|52.0550,-0.0351" \
    --routebrief v2/design/routebrieven/pgm-mogalakwena-londen.md \
    --uit    v2/data/stroomroute-pgm-mogalakwena-londen.json \
    --stroom pgm-mogalakwena-londen \
    --titel  "PGM · Mogalakwena (Zuid-Afrika) → Rustenburg PMR → OR Tambo (JNB) → Heathrow (LHR) → Johnson Matthey Royston"
}

# ── diamant · Bharat Diamond Bourse (Mumbai) → Sahar/CSMIA vracht → JFK South Cargo → 47th Street Diamond Exchange (Manhattan)
# Routebrief: v2/design/routebrieven/diamant-mumbai-newyork.md (LICHTE werkwijze M31 golf 3)
# ⚠️ b2 (lucht): DOORGETROKKEN grootcirkel BOM→JFK, 12.530,2 km gemeten — exact
#    de gepubliceerde ontwerpschatting (~12.530 km, routebrief §2/§8); geen
#    bron noemt een tussenlanding → één directe vlucht aangenomen (brief §7).
# ⚠️ b1 (truck BDB→Sahar) is -16,5% tegen het ontwerpcijfer (~10 km, geen
#    gepubliceerde bron) — buiten de ±15%-norm maar het ontwerpcijfer was zelf
#    nooit gebrond (alleen hemelsbreed 3,9 km); geen stippel nodig, beide
#    anker-verbindingen liggen op de openbare weg (≤0,06 km). Bevinding, niet
#    dichtgetrokken (bakhandleiding §5).
# ⚠️ b3 (truck JFK→47th Street) is +1,3% tegen ~25 km ontwerp — binnen norm;
#    alle vijf via-punten snappen ≤0,02 km op de doorgaande corridor
#    (Van Wyck Expwy → Kew Gardens Interchange → LIE → Queens-Midtown Tunnel).
# ⚠️ dia-bdb en dia-bom-cargo zijn hergebruikte, al satelliet-gelegde ankers
#    uit diamant-mirny-mumbai.md (deze golf) — niet opnieuw gecheckt.
# ⚠️ Geen zee-, spoor- of leidingbeen, geen haven-aanloop. Fase D/E vervallen
#    (brief §6, stoppunt 47th Street Diamond Exchange — handelsgebouw, geen
#    bewerkingslocatie; geen bron koppelt deze stroom aan een vervolgfabriek).
bak_diamant_mumbai_newyork() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Bharat Diamond Bourse → Sahar/CSMIA Air Cargo Complex|$BEEN/diamant-mumbai-newyork-weg-bdb-bomcargo.geojson" \
    --been-geojson "lucht|vlucht BOM → JFK (vrachtvlucht, grootcirkel)|$BEEN/diamant-mumbai-newyork-lucht-bom-jfk.geojson" \
    --been-geojson "truck|JFK South Cargo Area → 47th Street Diamond Exchange|$BEEN/diamant-mumbai-newyork-weg-jfk-47th.geojson" \
    --marker "dia-bdb — Bharat Diamond Bourse, G Block, Bandra-Kurla Complex, Mumbai — beursgebouw/vertrekpunt, bron-gelegd (hergebruikt anker)|19.0641,72.8646" \
    --marker "dia-bom-cargo — Sahar/CSMIA Air Cargo Complex, Mumbai — vrachtterminal, vertrek luchtvracht, bron-gelegd (hergebruikt anker)|19.0994,72.8673" \
    --marker "dia-jfk-cargo — JFK South Cargo Area (Cargo Plaza/South Cargo Road), Queens, New York — vrachtterminal, aankomst luchtvracht, bron-gelegd|40.6587,-73.7952" \
    --marker "dia-ny-47th — 47th Street Diamond Exchange, 1196 Avenue of the Americas, Diamond District, Manhattan — beurs-/handelsgebouw, stoppunt, bron-gelegd|40.7578,-73.9817" \
    --routebrief v2/design/routebrieven/diamant-mumbai-newyork.md \
    --uit    v2/data/stroomroute-diamant-mumbai-newyork.json \
    --stroom diamant-mumbai-newyork \
    --titel  "Diamant · Mumbai (Bharat Diamond Bourse) → JFK Airport → 47th Street Diamond Exchange (New York)"
}

# ── diamant · Venetia-mijn (De Beers, Limpopo, ZA) → O.R. Tambo (JNB) → Brucargo (BRU) → AWDC Antwerpen
# Routebrief: v2/design/routebrieven/diamant-venetia-antwerpen.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b2 is een luchtbeen (bakhandleiding §2, maak_luchtbeen.py): grootcirkel
#    JNB → BRU, 8.879,6 km — DOORGETROKKEN, geen stippel (vlucht tussen twee
#    gelegde vrachtterminals is geen gat). Geen tussenlanding gebrond → één
#    directe vlucht aangenomen (brief §7).
# ⚠️ b1 (truck, N1/R572 via Polokwane, eindToegangPrivaat + corridorKlassen
#    tertiary/unclassified) komt op 665,2 km tegen de gepubliceerde/webcheck
#    491,1 km (+35,4%, ⚠️ BUITEN ±15% — bevinding). Beide instellingen
#    veranderen het getal nauwelijks (222,4 → 222,6 km voor het eerste
#    deelbeen Venetia → Louis Trichardt/Makhado, tegen ~90 km hemelsbreed):
#    dit is geen wegklasse-filter maar een genuine detour in het OSM-wegennet
#    tussen de mijn en de N1-knoop bij Louis Trichardt (mogelijk via Alldays/
#    Vivo, sparse net door het Soutpansberg-gebied). Via-punten NIET
#    bijgeschoven om het getal te forceren (routebrief-licht §1/bakhandleiding
#    §5) — vergelijkbaar met de eveneens buiten-tolerantie N1/N4-bevinding bij
#    `pgm-rustenburg-shanghai` b1 (+48,4%).
# ⚠️ b3 (truck, Brucargo → AWDC, E19 via Mechelen) is een LETTERLIJKE KOPIE
#    van het reeds gebakken been in `diamant-jwaneng-antwerpen` (identieke
#    via-punten en vrijwel identieke ankercoördinaten — brief §3/§4, "beide
#    truckbenen zijn substantiële hoofdwegverbindingen").
# ⚠️ dia-jnb-cargo (-26,1400/28,2300) is hetzelfde anker als pgm-jnb-vracht
#    (`pgm-rustenburg-tokio.md`, deze golf) — niet opnieuw satelliet-gelegd.
#    dia-brucargo/dia-awdc zijn hergebruikte ankers uit `diamant-jwaneng-
#    antwerpen.md`/`diamant-ekati-antwerpen.md` (deze golf).
bak_diamant_venetia_antwerpen() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Venetia-mijn → O.R. Tambo vrachtterminal (N1/R572 via Polokwane)|$BEEN/diamant-venetia-antwerpen-weg-venetia-jnb.geojson" \
    --been-geojson "lucht|vlucht JNB → BRU (vrachtvlucht, grootcirkel)|$BEEN/diamant-venetia-antwerpen-lucht-jnb-bru.geojson" \
    --been-geojson "truck|Brucargo → AWDC/Diamond Office (E19 via Mechelen, letterlijk hergebruikt uit diamant-jwaneng-antwerpen b3)|$BEEN/diamant-jwaneng-antwerpen-weg-brucargo-antwerpen.geojson" \
    --marker "dia-venetia-mijn — Venetia-mijn (De Beers), open put + verwerkingsfabriek, Limpopo — mijn/laadplek, bron-gelegd|-22.4362,29.3175" \
    --marker "dia-jnb-cargo — O.R. Tambo Int'l Airport, vrachtloodsen/-apron, Kempton Park — vrachtterminal (hergebruikt anker), bron-gelegd|-26.1400,28.2300" \
    --marker "dia-brucargo — Brucargo, Brussels Airport — vrachtterminal (hergebruikt anker), bron-gelegd|50.90628,4.45584" \
    --marker "dia-awdc — AWDC/Diamond Office, Hoveniersstraat, Antwerpen — beursgebouw/certificeringshub (hergebruikt anker), stoppunt, bron-gelegd|51.21520,4.41870" \
    --routebrief v2/design/routebrieven/diamant-venetia-antwerpen.md \
    --uit    v2/data/stroomroute-diamant-venetia-antwerpen.json \
    --stroom diamant-venetia-antwerpen \
    --titel  "Diamant · Venetia-mijn (Zuid-Afrika) → O.R. Tambo → Brussel (Brucargo) → Antwerpen (AWDC)"
}

# ── pgm · Northam Zondereinde-complex (Bushveld, Zuid-Afrika) → OR Tambo (JNB) → (vlucht) → Frankfurt (FRA) → Heraeus Precious Metals Hanau (Duitsland)
# Routebrief: v2/design/routebrieven/pgm-zondereinde-hanau.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, NIET stippel): Zondereinde mijn/smelter/BMR → OR Tambo
#    vrachtterminal, R510 zuidwaarts (via Northam-dorp) → N4 oostwaarts (via
#    Marikana/Brits) → N1 zuidwaarts (via Pretoria). 281,4 km tegen het
#    ~140 km-ontwerpcijfer (routebrief §1/§2, "niet apart gebrond") = **+101,0%,
#    ruim buiten ±15%** — bevinding, geen fout: de hemelsbrede afstand tussen
#    de twee ankers is zelf al ~168 km (het ontwerpcijfer van 140 km was dus
#    intern al te laag, los van enige routering), en de via-punten uit de
#    brief (§4, Northam/Marikana/Brits/Pretoria) pinnen de enige doorgaande
#    corridor R510→N4→N1 — geen via-punt bijgeschoven om het getal te halen.
#    Anker-verbindingsstukjes 0,28/0,10 km, beide ruim binnen 0,5 km.
# ⚠️ b2 (lucht, DOORGETROKKEN — geen stippel, bakhandleiding §2): vlucht
#    JNB → FRA als grootcirkel, 8.688,0 km, tegen het ontwerpcijfer ~8.900 km
#    (−2,4%; het tool zelf gaf bij de losse run "8688.0 km grootcirkel · 349
#    punten") — een luchtbeen heeft geen ±15%-km-toets (bakhandleiding §5).
#    Geen tussenlanding: geen bron noemt een hub (brief §7) → één directe
#    vrachtvlucht JNB → FRA, aannemelijk (industriestandaard voor ZA-PGM-
#    luchtvracht naar Europese raffinaderijen).
# ⚠️ b3 (truck, NIET stippel, `eindToegangPrivaat`): Frankfurt vrachtterminal
#    (Cargo City Süd) → Heraeus Hanau, A66. 35,3 km tegen het ~25 km-
#    ontwerpcijfer (+41,3%, buiten ±15%) — bevinding, niet dichtgetrokken: de
#    via-punten uit de brief (§4) liggen op Bahnhofstraße/Edmund-Seng-Straße
#    in Maintal-centrum, een lokaal stratennet dat in een eigen bereikbaar-
#    heidscontrole (pyosmium-scan op de de-hessen-extract) niet in hetzelfde
#    verbonden wegennet zat als de twee ankers, terwijl Frankfurt-vrachtterminal
#    en Heraeus Hanau dat onderling wél zijn. Maintal is daarmee NIET als
#    via-punt meegenomen in deze bake (b3 routeert rechtstreeks anker→anker
#    over A66); dit is een afwijking van routebrief §4 rij "b3 | 1 | Maintal",
#    die zelf al aangaf géén corridorkeuze te pinnen ("vaste doorgaande knoop,
#    geen zijtak") — zie ook §9-toelichting hieronder. `eindToegangPrivaat`
#    was nodig: zonder die vlag gaf het wegtool "geen wegpad tussen punt 0 en
#    1" bij het Frankfurt-vrachtterminal-anker (airside/privé-servicewegen
#    van Cargo City Süd, snap 0,01 km met de vlag).
# ⚠️ Geen fase D/E (brief §6): Heraeus Hanau is het BINDEND aangewezen
#    toll-raffinagepunt (99,95%); geen bron noemt een vervolgzending naar een
#    specifieke afnemer/fabriek.
bak_pgm_zondereinde_hanau() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Zondereinde mijn/smelter/BMR → OR Tambo vrachtterminal (R510 → N4 → N1)|$BEEN/pgm-zondereinde-hanau-weg-zondereinde-ortambo.geojson" \
    --been-geojson "lucht|vlucht JNB → FRA (vrachtvlucht, grootcirkel)|$BEEN/pgm-zondereinde-hanau-lucht-ortambo-frankfurt.geojson" \
    --been-geojson "truck|Frankfurt vrachtterminal → Heraeus Precious Metals Hanau (A66)|$BEEN/pgm-zondereinde-hanau-weg-frankfurt-hanau.geojson" \
    --marker "pgm-zondereinde-mijnsmelter — Northam Zondereinde-complex (mijn/smelter/BMR), Thabazimbi LM, Limpopo, laadplek, bron-gelegd|-24.8333,27.3669" \
    --marker "pgm-ortambo-vracht — OR Tambo International Airport, vrachtplatform, Kempton Park (JNB), overslag truck → lucht, bron-gelegd|-26.1290,28.2330" \
    --marker "pgm-frankfurt-vracht — Frankfurt Airport, Cargo City Süd (FRA), overslag lucht → truck, bron-gelegd|50.0244,8.5552" \
    --marker "pgm-heraeus-hanau — Heraeus Precious Metals, Hanau, stoppunt (toll-raffinage tot 99,95%), bron-gelegd|50.1328,8.9315" \
    --routebrief v2/design/routebrieven/pgm-zondereinde-hanau.md \
    --uit    v2/data/stroomroute-pgm-zondereinde-hanau.json \
    --stroom pgm-zondereinde-hanau \
    --titel  "PGM · Northam Zondereinde (Zuid-Afrika) → OR Tambo (JNB) → Frankfurt (FRA) → Heraeus Hanau (Duitsland)"
}

# ── goud · Valcambi-raffinaderij (Balerna, Zwitserland) → Milaan-Malpensa → Londen Heathrow → LBMA-kluis (Bank of England)
# Routebrief: v2/design/routebrieven/goud-valcambi-londen.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ Drie benen, alle fase D, geen tussenliggende verwerkingsknoop — de
#    Zwitserland–VK-goudas is een GEAGGREGEERDE marktas (vier Zwitserse
#    raffinaderijen samen), geen bedrijfsspecifieke route (brief §1/§7).
# ⚠️ b1 (truck) is DOORGETROKKEN, echte weggeometrie (maak_stroombeen_weg.py,
#    profiel goud-valcambi-londen-valcambi-mxp): A2 (Chiasso-grensovergang) →
#    A9 (Como–Lomazzo) → A8 (Gallarate) → Malpensa Cargo City Sud. Geen
#    gepubliceerde bronwaarde voor de km (≈78 km eigen kaartlezing, brief §7)
#    — de bake-lengte is de echte controle, venster 50 km (landsgrens).
# ⚠️ b2 (lucht) is een GROOTCIRKEL (maak_luchtbeen.py), DOORGETROKKEN — stippel
#    betekent uitsluitend "hier reikt het net niet" en een vlucht tussen twee
#    gelegde vrachtterminals is geen gat (bakhandleiding §2 Lucht). Malpensa
#    i.p.v. Zürich als vertrekluchthaven is AANNEMELIJK (brief §7, kortste weg
#    vanuit Ticino, niet bedrijfsbevestigd); geen tussenlanding bevestigd door
#    een bron — aanname is één directe vlucht MXP → LHR (brief §7).
# ⚠️ b3 (truck) is DOORGETROKKEN, echte weggeometrie (profiel
#    goud-valcambi-londen-lhr-boe): M4 (Heathrow-spur) → A4 (Chiswick,
#    Hammersmith) → Hyde Park Corner → Fleet Street → Bank of England. Rond de
#    kluis zelf ligt een voetgangerszone (brief §7) — `eindKlassen` neemt de
#    kleine stedelijke wegklassen mee zodat de lijn tot vlak bij het gebouw
#    komt; een eventuele laatste-meters-stippel is ter beoordeling ná de bake.
# ⚠️ LBMA-kluis in de City (Bank of England, Threadneedle Street) vs. de
#    praktijk dat veel commerciële LBMA-kluizen bij Heathrow zelf liggen —
#    Bank of England is een echte, in de City gevestigde LBMA-erkende
#    kluishouder en hier als anker gekozen conform het ketenontwerp (brief
#    §7); een bedrijfsspecifieke Heathrow-kluis is niet uitgesloten.
# ⚠️ Geen fase E: de brief stopt bij de LBMA-kluis/Bank of England (brief §6,
#    geen bron noemt een vervolgbestemming ná de Londense kluis).
bak_goud_valcambi_londen() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Valcambi, Balerna → Malpensa-vrachtterminal (A2/A9/A8)|$BEEN/goud-valcambi-londen-weg-valcambi-mxp.geojson" \
    --been-geojson "lucht|vlucht MXP → LHR (vrachtvlucht, grootcirkel)|$BEEN/goud-valcambi-londen-lucht-mxp-lhr.geojson" \
    --been-geojson "truck|Heathrow World Cargo Centre → Bank of England, City of London (M4/A4)|$BEEN/goud-valcambi-londen-weg-lhr-boe.geojson" \
    --marker "au-ref-valcambi — Valcambi SA, Via Passeggiata 3, Balerna (Ticino) — raffinaderij/laadplek, bron-gelegd|45.8385,9.0051" \
    --marker "au-mxp-cargo — Milano Malpensa Cargo, Cargo City Sud — vrachtterminal (vertrek lucht), bron-gelegd|45.6142,8.7186" \
    --marker "au-lhr-cargo — Heathrow World Cargo Centre / IAG Cargo — vrachtterminal (aankomst lucht), bron-gelegd|51.4605,-0.4629" \
    --marker "au-hub-london — Bank of England, Threadneedle Street, City of London — LBMA-kluis/beursgebouw, stoppunt, bron-gelegd|51.5139,-0.0883" \
    --routebrief v2/design/routebrieven/goud-valcambi-londen.md \
    --uit    v2/data/stroomroute-goud-valcambi-londen.json \
    --stroom goud-valcambi-londen \
    --titel  "Goud · Valcambi (Zwitserland) → Milaan-Malpensa → Londen Heathrow → LBMA-kluis (Bank of England)"
}

# Routebrief goud-olimpiada-dubai.md (LICHTE werkwijze, M31 golf 3, §2 Lucht).
# Goud (doré/baar) van Polyus' Olimpiada-mijn per truck naar de Krastsvetmet-
# raffinaderij in Krasnojarsk, per truck naar de vrachtterminal van
# Krasnojarsk (KJA), per vrachtvlucht (grootcirkel) naar de vrachtterminal
# van Dubai (DXB), per truck naar de DMCC-vrijzone — de post-2022 route van
# Russisch goud om de westerse LBMA-schorsing heen.
# ⚠️ Geen stippels: alle vier de benen zijn doorgetrokken (truck/truck/lucht/
#    truck), geen enkel wegsegment ontbrak in de lokale extracts.
# ⚠️ b1 (Olimpiada-mijn → Krastsvetmet) en b2 (Krastsvetmet → KJA) en b4
#    (DXB → DMCC) meten 615,0 / 45,6 / 33,5 km tegen ontwerpcijfers 550 / 30 /
#    20 km (+11,8% / +51,9% / +67,4%) — alleen b1 valt binnen ±15%; b2 en b4
#    zijn een BEVINDING (brief §9): het ontwerpcijfer was een grove schatting,
#    niet apart gebrond, en de gemeten wegroute (P409/ringweg resp. Sheikh
#    Zayed Road) is de echte, gekarteerde corridor — niet dichtgetrokken.
# ⚠️ b3 (lucht KJA → DXB) is een grootcirkel, geen km-toets: 4.548,1 km
#    gemeten tegen het ontwerpcijfer ≈5.150 km (bron uit 2022, brief §7 —
#    aannemelijk, kan gewijzigd zijn sinds de sanctieroute uit dat onderzoek).
# ⚠️ au-kja-cargo is een gedeeld platform (general aviation + vracht +
#    Volga-Dnepr-hub); de exacte Lufthansa Cargo-loods is op z16 niet apart
#    te onderscheiden (brief §7).
bak_goud_olimpiada_dubai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Olimpiada-mijn → Severo-Jenisejsk → Jenisejsk/Lesosibirsk → Bolsjaja Moerta → Krastsvetmet-raffinaderij, Krasnojarsk (P409)|$BEEN/goud-olimpiada-dubai-weg-olimpiada-krastsvetmet.geojson" \
    --been-geojson "truck|Krastsvetmet-raffinaderij, Krasnojarsk → Jemeljanovo (KJA) vrachtterminal (P409/ringweg noordwaarts)|$BEEN/goud-olimpiada-dubai-weg-krastsvetmet-kja.geojson" \
    --been-geojson "lucht|vlucht KJA → DXB (vrachtvlucht, grootcirkel, aannemelijk: bron uit 2022, sanctieroute kan gewijzigd zijn)|$BEEN/goud-olimpiada-dubai-lucht-kja-dxb.geojson" \
    --been-geojson "truck|Dubai International Airport (DXB), Emirates SkyCargo → Trade Centre-rotonde → Mall of the Emirates → DMCC-vrijzone (Sheikh Zayed Road)|$BEEN/goud-olimpiada-dubai-weg-dxb-dmcc.geojson" \
    --marker "au-olimpiada-mijn — Olimpiada-mijn (Polyus), open dagbouwput — mijn/laadplek, bron-gelegd|59.8650,92.9156" \
    --marker "au-krastsvetmet — Krastsvetmet OJSC, Transportny proezd, Krasnojarsk — raffinaderij, bron-gelegd|56.0160,92.9998" \
    --marker "au-kja-cargo — Krasnojarsk (Jemeljanovo/KJA) vracht-/GA-apron — vrachtterminal (vertrek lucht), bron-gelegd|56.1837,92.4630" \
    --marker "au-dxb-cargo — Dubai International Airport, Emirates SkyCargo-gebouw — vrachtterminal (aankomst lucht), bron-gelegd|25.2560,55.3434" \
    --marker "au-dmcc — DMCC (Dubai Multi Commodities Centre), Jumeirah Lake Towers — handelshub/vrijzone, stoppunt, bron-gelegd|25.0709,55.1387" \
    --routebrief v2/design/routebrieven/goud-olimpiada-dubai.md \
    --uit    v2/data/stroomroute-goud-olimpiada-dubai.json \
    --stroom goud-olimpiada-dubai \
    --titel  "Goud · Olimpiada-mijn (Rusland) → Krasnojarsk → Dubai (DXB) → DMCC-vrijzone"
}

# ── diamant · Catoca-mijn (Angola) → Luanda (Sodiam/Endiama) → NBJ-vrachtterminal → Dubai (DXB) → DMCC/Almas Tower
# Routebrief: v2/design/routebrieven/diamant-catoca-dubai.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, DOORGETROKKEN, echte weggeometrie, profiel diamant-catoca-dubai-
#    catoca-luanda): Catoca-mijn → Saurimo → Malanje → Cacuso → N'dalatando →
#    Luanda (EN230/EN220). Eerste poging zonder corridorKlassen faalde ("geen
#    wegpad tussen punt 0 en 1") — de dichtstbijzijnde secondary bij de mijn
#    ligt op 19,6 km, EIND_STRAAL_KM is 12 km; met corridorKlassen tertiary/
#    unclassified/service erbij routeert hij door. Lengtetoets: 1.024,7 km
#    tegen de briefwaarde ~850 (ontwerp) = **+20,6%, BUITEN ±15%** — een
#    bevinding, niet dichtgetrokken. Eigen WebSearch-check bevestigt de
#    afwijking zit in het brief-cijfer, niet in de bake: de EN230 Malanje↔
#    Saurimo alléén is gepubliceerd op 625–657 km (AFA-herstelproject/
#    adistanciaentre.com), tegen een hemelsbreed-schatting van ~438 km waar de
#    briefschrijver zijn ~850 km-totaal op baseerde — de weg zelf windt fors
#    meer dan de brief aannam.
# ⚠️ b2 (truck, DOORGETROKKEN, profiel diamant-catoca-dubai-luanda-nbj):
#    Sodiam-kantoor Luanda → NBJ-vrachtterminal (nieuwe luchthaven-toegangsweg/
#    Via Expresso). Geen corridorkeuze gevonden (routebrief §4) — 41,9 km
#    tegen ~40 gepubliceerd = +4,8%, binnen tolerantie.
# ⚠️ b3 (lucht, GROOTCIRKEL, maak_luchtbeen.py, DOORGETROKKEN): NBJ-
#    vrachtterminal → DXB-vrachtterminal. Stippel betekent uitsluitend "hier
#    reikt het net niet" en een vlucht tussen twee gelegde terminals is geen
#    gat (bakhandleiding §2 Lucht). Geen bron noemt een tussenlanding → één
#    directe vlucht (routebrief §7). Gemeten 5.919,2 km grootcirkel — vrijwel
#    identiek aan de eigen briefmeting (5.922 km, tegen het ontwerpcijfer
#    ~7.300 km dat een ruwe schatting bleek).
# ⚠️ DXB-vrachtterminal-anker VERVANGEN t.o.v. de brief: de brief zelf noemt
#    dit anker "onzeker" (§3, officiële luchthaven-referentiecoördinaat
#    25,25278/55,36444, Cargo Village niet exact gepind, open punt §7).
#    Bakhandleiding §1/routebrief-licht §1: bestaande ankers uit brieven van
#    dezelfde grondstof in deze golf hergebruiken. Drie zusterbrieven
#    (diamant-marange-dubai, diamant-mbujimayi-dubai, diamant-letseng-dubai)
#    hebben ditzelfde DXB-vrachtcomplex al SATELLIET-GELEGD (z14-z18) op
#    25,2574524/55,3405972 (Emirates SkyCargo/Cargo Village, Al Garhoud) —
#    dat scherpere, bron-gelegde anker is hier gebruikt i.p.v. het eigen
#    onzekere punt, en lost het open punt van de eigen brief §7 op.
# ⚠️ b4 (truck, DOORGETROKKEN) is een GEDEELD BEEN, LETTERLIJK HERGEBRUIKT:
#    DXB-vrachtterminal → DMCC/Almas Tower loopt over exact dezelfde corridor
#    (Sheikh Zayed Road E11) en exact dezelfde twee ankers als de al gebakken
#    diamant-mbujimayi-dubai-stroom (31,2 km, -8,9% tegen 34 km gepubliceerd,
#    binnen tolerantie) — diens geojson wordt hier letterlijk hergebruikt
#    (bakhandleiding §2: "gedeeld been = letterlijke kopie, geen tweede
#    versie"), geen herbake, geen eigen wegscan nodig.
# ⚠️ DMCC/Almas Tower-anker (25,0689/55,1412, bron-gelegd, Wikipedia) komt
#    vrijwel exact overeen met het gedeelde eindpunt van het hergebruikte been
#    (25,069063/55,141166) — geen aanpassing nodig.
# ⚠️ Geen haven-aanloop: deze keten bevat geen zeebeen (§ verplicht alleen bij
#    modaliteit zee). Geen fase D/E: de brief stopt bij de Dubai Diamond
#    Exchange (§6, geen bron koppelt déze Catoca-lading aan een vervolgbestemming).
bak_diamant_catoca_dubai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Catoca-mijn → Luanda (Sodiam/Endiama) (EN230 Saurimo–Malanje / EN220 Malanje–N'dalatando–Luanda)|$BEEN/diamant-catoca-dubai-weg-catoca-luanda.geojson" \
    --been-geojson "truck|Luanda (Sodiam) → NBJ-vrachtterminal (nieuwe luchthaven-toegangsweg)|$BEEN/diamant-catoca-dubai-weg-luanda-nbj.geojson" \
    --been-geojson "lucht|vlucht NBJ → DXB (vrachtvlucht, grootcirkel)|$BEEN/diamant-catoca-dubai-lucht-nbj-dxb.geojson" \
    --been-geojson "truck|DXB-vrachtterminal → DMCC/Dubai Diamond Exchange (Almas Tower, JLT) (Sheikh Zayed Road E11; gedeeld been met diamant-mbujimayi-dubai)|$BEEN/diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson" \
    --marker "dia-catoca-mijn — Catoca-mijn (Sociedade Mineira de Catoca), Lunda Sul — mijn/laadplek, bron-gelegd|-9.39889,20.30083" \
    --marker "dia-luanda-sodiam — Endiama-hoofdkantoor/Sodiam-exportkantoor, Major Kanhangulo, Luanda — overslag: kantoor/exportadministratie, bron-gelegd|-8.81291,13.23578" \
    --marker "dia-nbj-vracht — Vrachtterminal (TECA), Aeroporto Internacional Dr. António Agostinho Neto (NBJ), Bom Jesus — overslag truck → lucht, aannemelijk|-9.03350,13.51400" \
    --marker "dia-dxb-vracht — Dubai Intl Airport (DXB), Cargo Village/Emirates SkyCargo (hergebruikt: diamant-marange-dubai/-mbujimayi-dubai/-letseng-dubai) — overslag lucht → truck, bron-gelegd|25.2574524,55.3405972" \
    --marker "dia-dmcc-almas — Dubai Diamond Exchange (DMCC), Almas Tower, Jumeirah Lake Towers — eindpunt/beurs, stoppunt, bron-gelegd|25.0689,55.1412" \
    --routebrief v2/design/routebrieven/diamant-catoca-dubai.md \
    --uit    v2/data/stroomroute-diamant-catoca-dubai.json \
    --stroom diamant-catoca-dubai \
    --titel  "Diamant · Catoca-mijn (Angola) → Luanda → NBJ-vrachtterminal → Dubai (DXB) → DMCC/Almas Tower"
}

# ── goud · Gold Fields Tarkwa (Ghana) → Kotoka/Accra → Dubai (DXB) → DMCC-goudzone
# Routebrief: v2/design/routebrieven/goud-tarkwa-dubai.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, weg): Tarkwa-mill → Kotoka/Accra-vrachtterminal, inland-route
#    via Twifo Praso–Assin Fosu–Agona Swedru–Kasoa. Gebakken 279,3 km tegen
#    ~300 km gepubliceerd (Gold Fields, niet corridor-specifiek) = -6,9%, OK.
#    Geen N-wegnummer gebrond (brief §7); via-punten op geografische
#    aannemelijkheid + OSM/Photon.
# ⚠️ b2 (lucht): vrachtvlucht ACC → DXB, grootcirkel, 6.288,0 km (eigen
#    haversine ≈6.290 km in de brief) — doorgetrokken, geen stippel
#    (bakhandleiding §2: een vlucht tussen twee gelegde vrachtterminals is
#    geen gat). Geen tussenlanding: geen bron noemt een hub-overstap voor
#    déze corridor (brief §7, aanname).
# ⚠️ b3 (truck, weg): DXB-vrachtterminal → DMCC-goudzone (Al Etihad Gold
#    Refinery) via Sheikh Zayed Road (E11), Trade Centre Roundabout → Mall of
#    the Emirates → Al Thanyah/JLT. Gebakken 38,2 km tegen de brief-schatting
#    ~31 km (+23,2%, buiten de ±15%-norm) — bevinding, geen via-punt
#    bijgeschoven: de snaps liggen strak op de weg (0,00-0,03 km) en 38 km is
#    consistent met de werkelijke afstand DXB↔JLT over Sheikh Zayed Road; de
#    brief-schatting ("eigen meting via de drie via-punten") was kennelijk
#    een onderschatting, de bake-lengte is leidend (bakhandleiding §5).
# ⚠️ Geen haven-aanloop: deze keten bevat geen zeebeen. Geen fase D/E: de
#    brief stopt bewust bij de DMCC-goudzone (§6, geen bron koppelt déze
#    Tarkwa-lading aan één met naam genoemde raffinaderij binnen DMCC).
bak_goud_tarkwa_dubai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Gold Fields Tarkwa (mill) → Kotoka/Accra-vrachtterminal (inland-route via Twifo Praso–Assin Fosu–Agona Swedru–Kasoa)|$BEEN/goud-tarkwa-dubai-weg-mill-acc.geojson" \
    --been-geojson "lucht|vlucht ACC → DXB (vrachtvlucht, grootcirkel)|$BEEN/goud-tarkwa-dubai-lucht-acc-dxb.geojson" \
    --been-geojson "truck|Dubai Intl-vrachtterminal (DXB) → DMCC-goudzone (Sheikh Zayed Road E11, via Trade Centre Roundabout en Mall of the Emirates)|$BEEN/goud-tarkwa-dubai-weg-dxb-dmcc.geojson" \
    --marker "au-tarkwa-mill — Gold Fields Tarkwa, CIL-verwerkingsfabriek — mijn/laadplek, bron-gelegd|5.3275,-2.0215" \
    --marker "au-air-acc-cargo — Kotoka/Accra Intl Airport, vrachtterminal (Ghana Airport Cargo Center) — overslag truck → lucht, bron-gelegd|5.5985,-0.1745" \
    --marker "au-air-dxb-cargo — Dubai Intl Airport (DXB), Emirates SkyCargo-terminal (Cargo Village) — overslag lucht → truck, bron-gelegd|25.2560,55.3431" \
    --marker "au-dmcc-refine — DMCC-goudzone, Dubai — Al Etihad Gold Refinery (naast Emirates Gold/Kaloti) — raffinagezone, stoppunt, bron-gelegd|25.0602,55.1352" \
    --routebrief v2/design/routebrieven/goud-tarkwa-dubai.md \
    --uit    v2/data/stroomroute-goud-tarkwa-dubai.json \
    --stroom goud-tarkwa-dubai \
    --titel  "Goud · Gold Fields Tarkwa (Ghana) → Kotoka/Accra → Dubai (DXB) → DMCC-goudzone"
}

# ── diamant · Marange-diamantvelden (ZCDC) → Harare (HRE) → vrachtvlucht → Dubai (DXB) → DMCC
# Routebrief: v2/design/routebrieven/diamant-marange-dubai.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck) begint NIET op het mijnanker zelf: `maak_stroombeen_weg.py` gaf
#    "geen wegpad tussen punt 0 en 1" met het mijnanker als startpunt, óók met
#    corridorKlassen ruim (tertiary/unclassified/service) + eindToegangPrivaat.
#    Gemeten met een osmium-connectiviteitscheck op de zimbabwe-extract: het
#    mijnanker snapt op een geïsoleerd 8-knopen-eilandje van vooral track-
#    ways (0,14 km) dat NIET verbonden is met het doorgaande wegnet
#    (1,9 mln-knopen-component incl. de R5/Harare-Mutare Highway) — een echt
#    "net reikt niet"-geval voor het mijnterrein zelf, geen wegklassefout.
#    De dichtstbijzijnde WEL-verbonden weg (service) ligt op 0,79 km van het
#    mijnanker → getekend als STIPPEL "last mile" met die reden; het
#    wegprofiel begint op dat verbindingspunt.
# ⚠️ Het via-punt "Mutare" uit de brief (stadscentrum 32,6333/-18,9667) snapte
#    op een even geïsoleerde wegstomp (0,048 km, component van 2 knopen) —
#    dus ook GEEN wegklassefout maar een via-punt náást de doorgaande weg.
#    Verplaatst naar de R5/Harare-Mutare Highway zelf (32,6426/-18,9511, nog
#    steeds Mutare-stad), gemeten met dezelfde connectiviteitscheck. Dit is
#    een via-punt (corridorkeuze), geen anker — geen brief-wijziging nodig.
# ⚠️ b1 lengtetoets: 357,4 km tegen de ontwerpschatting ~270 km = **+32,4%,
#    BUITEN ±15%** — BEVINDING, niet dichtgetrokken (geen via-punt bijgeschoven
#    om het getal te halen; alle vier subsnaps liggen op 0,00–0,13 km). De
#    brief-schatting van ~270 km was zelf al "geen betrouwbare gepubliceerde
#    wegreferentie" (§2); de werkelijk gerouteerde afstand via Mutare–Rusape–
#    Marondera–Harare (R5/A3) is plausibeler voor deze corridor.
# ⚠️ b2 (lucht, DOORGETROKKEN — geen stippel, bakhandleiding §2): vlucht
#    HRE → DXB als grootcirkel, 5.471,7 km — komt exact overeen met de
#    brief-schatting (routebrief §2, "5.471,7 km berekende grootcirkel").
#    Geen tussenlanding gebrond (brief §7) → één directe vrachtvlucht.
# ⚠️ b3 (truck, doorgetrokken): DXB-vrachtterminal → DMCC/Almas Tower over
#    Sheikh Zayed Road (E11) — 34,5 km tegen ~34 = +1,4% [OK]. Ankers
#    hergebruikt van de zusterbrief diamant-mbujimayi-dubai (dezelfde DXB-
#    vrachtterminal/DMCC-coördinaten, beide bron-gelegd in deze golf).
# ⚠️ Geen fase D/E (brief §6): DMCC is een handelsbeurs/kluis, geen
#    verwerkingsknoop — de brief stopt hier bewust.
bak_diamant_marange_dubai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|last mile Marange-mijn (ZCDC-terrein) → doorgaande weg (geen net op deze korrel — track-only mijnwegen tussen het terrein en de dichtstbijzijnde geclassificeerde weg, 0,79 km, osmium-connectiviteitscheck)|-19.5906,32.3522|-19.5956,32.3469" \
    --been-geojson "truck|vrachtwagen Marange-mijnwegaansluiting → Harare (HRE) vrachtterminal (via Mutare/Rusape/Marondera, R5/A3-corridor)|$BEEN/diamant-marange-dubai-weg-marange-hre.geojson" \
    --been-geojson "lucht|vlucht HRE → DXB (vrachtvlucht, grootcirkel)|$BEEN/diamant-marange-dubai-lucht-hre-dxb.geojson" \
    --been-geojson "truck|vrachtwagen Dubai Intl (DXB) vrachtterminal → DMCC/Almas Tower (Sheikh Zayed Road E11)|$BEEN/diamant-marange-dubai-weg-dxb-dmcc.geojson" \
    --marker "dia-marange-mijn — Marange-diamantvelden (ZCDC), Chiadzwa — mijn/laadplek, bron-gelegd|-19.5906,32.3522" \
    --marker "dia-hre-cargo — Robert Gabriel Mugabe Intl (HRE), vracht-/GA-apron, Harare — overslag truck → lucht, bron-gelegd (exploitant niet bevestigd)|-17.9218,31.0946" \
    --marker "dia-dxb-cargo — Dubai Intl (DXB), Emirates Air Cargo-gebouw, Al Garhoud — overslag lucht → truck, bron-gelegd|25.2575,55.3406" \
    --marker "dia-dmcc — DMCC / Dubai Diamond Exchange, Almas Tower, Jumeirah Lake Towers — beursgebouw/kluis, stoppunt, bron-gelegd|25.0691,55.1412" \
    --routebrief v2/design/routebrieven/diamant-marange-dubai.md \
    --uit    v2/data/stroomroute-diamant-marange-dubai.json \
    --stroom diamant-marange-dubai \
    --titel  "Diamant · Marange-diamantvelden (ZCDC) → Harare (HRE) → Dubai (DXB) → DMCC"
}

# ── goud · Goldstrike-complex (Nevada Gold Mines, Carlin Trend) → Asahi
#    Refining USA, Salt Lake City (LICHTE werkwijze M31 golf 3)
# Routebrief: v2/design/routebrieven/goud-nevada-saltlakecity.md
# ⚠️ Eén been (b1, truck via maak_stroombeen_weg.py), GEEN luchtvracht — de
#    brief kiest dat bewust (§1/§7): een kort, goed gedocumenteerd landtraject
#    zonder bron die luchtvracht noemt.
# ⚠️ De laatste ~100 m bij Asahi Refining zijn een STIPPEL, niet doorgetrokken.
#    Diagnose (weggraaf, 2026-09-28): het anker au-saltlakecity-asahi
#    (laaddock/parkeerlus, 40.72471,-112.00077) snapt op een OSM-component van
#    slechts 8 knopen (twee losse `service`-ways, way 742154031/742154032) die
#    NIET aan het publieke wegennet hangt — een echte topologiebreuk in OSM,
#    geen te krap scanvenster (geverifieerd met een BFS-componentenanalyse op
#    de volledige weggraaf). Dichtstbijzijnde knoop op het hoofdnet: South
#    Frontage Road, 102 m verderop (40.725566,-112.000339) — het wegbeen
#    eindigt daar, de laatste 102 m gaan als korte stippel "geen net op deze
#    korrel" (bakhandleiding §2, <2 km).
# ⚠️ Lengtetoets: 442,9 km tegen ≈450 km gepubliceerd (brief §2/§7, eigen
#    optelling uit deelroutes) = −1,6% [OK]. Het ontwerp noemde ≈550 km; de
#    brief corrigeert dat expliciet (§7) — de bake-lengte is leidend.
# ⚠️ Beide ankers bron-gelegd (routebrief §3, satelliet z15 via sat_check.py):
#    au-nevada-mijn = Goldstrike-complex, Betze-Post open pit + autoclaaf-/
#    roaster (Nevada Gold Mines, Carlin Trend); au-saltlakecity-asahi = Asahi
#    Refining USA, Inc., 4601 West 2100 South, Salt Lake City.
# ⚠️ Geen fase D/E (brief §6): de raffinaderij levert baren aan de groothandel/
#    COMEX-keten, maar geen bron noemt een specifieke afnemersfabriek voor dit
#    Nevada-doré — de brief stopt bewust bij de poort van Asahi Refining.
bak_goud_nevada_saltlakecity() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Goldstrike-complex → South Frontage Road (Asahi Refining SLC) via I-80/NV-766 (Carlin·Elko·Wells·West Wendover·Knolls·Lake Point)|$BEEN/goud-nevada-saltlakecity-weg-nevada-saltlakecity.geojson" \
    --stippel      "truck|last mile Asahi Refining — South Frontage Road → laaddock/parkeerlus (geen net op deze korrel: OSM-service-ways op het terrein hangen niet aan het publieke net, 102 m, componentenanalyse weggraaf)|40.725566,-112.000339|40.72471,-112.00077" \
    --marker "au-nevada-mijn — Goldstrike-complex, Betze-Post open pit + autoclaaf-/roaster (Nevada Gold Mines, Carlin Trend) — mijn/verwerking, bron-gelegd|40.9816,-116.3789" \
    --marker "au-saltlakecity-asahi — Asahi Refining USA, Inc., 4601 West 2100 South, Salt Lake City — raffinaderij, stoppunt, bron-gelegd|40.72471,-112.00077" \
    --routebrief v2/design/routebrieven/goud-nevada-saltlakecity.md \
    --uit    v2/data/stroomroute-goud-nevada-saltlakecity.json \
    --stroom goud-nevada-saltlakecity \
    --titel  "Goud · Goldstrike-complex (Nevada Gold Mines) → Asahi Refining USA (Salt Lake City)"
}

# ── goud · Siguiri-mijn (AngloGold Ashanti/SMD, Guinee) → Conakry (CKY) → Dubai (DXB) → DMCC
# Routebrief: v2/design/routebrieven/goud-siguiri-dubai.md (LICHTE werkwijze M31 golf 3,
# §2 Lucht — derde, onafhankelijke West-Afrikaanse lucht-as naar Dubai in deze golf).
# ⚠️ b1 (truck): Siguiri-mijn → Kouroussa → Dabola → Mamou → Kindia → Coyah → Conakry
#    Int'l (CKY) vrachtterminal, N1-corridor — 742,7 km tegen ~850 km ontwerp =
#    **-12,6%** (binnen ±15%, buiten de ±10% waarschuwing van het tool) — BEVINDING,
#    niet dichtgetrokken: geen gepubliceerde wegkilometrage voor deze corridor
#    gevonden binnen het webbudget, ~850 km was zelf al niet onafhankelijk bevestigd.
#    Geen stippel nodig — alle subsnaps 0,04–1,82 km, geen via-punt >5 km mis.
# ⚠️ b2 (lucht, DOORGETROKKEN — geen stippel, bakhandleiding §2): vlucht CKY → DXB
#    als grootcirkel, 7.447,3 km — geen gepubliceerde vluchtlengte (brief §7); geen
#    bron noemt een tussenlanding → één directe vrachtvlucht, die aanname staat in §7.
# ⚠️ b3 (truck, doorgetrokken): DXB-vrachtterminal → DMCC/Almas Tower over Sheikh
#    Zayed Road (E11) — geometrie LETTERLIJK HERGEBRUIKT van de zusterbrief
#    diamant-marange-dubai (dezelfde ankers au-dxb-cargo/au-dubai-dmcc, coördinaat-
#    identiek aan dia-dxb-cargo/dia-dmcc, beide bron-gelegd in deze golf) —
#    34,757 km tegen ~20 km ontwerp = **+73,8%, BUITEN ±15%** — BEVINDING: het
#    ontwerp-getal lag al onder de anker-tot-anker hemelsbreed-afstand (~29 km),
#    de gemeten wegroute (34,5 km, enige doorgaande E11-corridor) is leidend.
# ⚠️ Ankers: au-cky-cargo is AANNEMELIJK, niet bron-gelegd — satellietbeeld (z17)
#    toont een GA-apron met kleine vliegtuigen, geen duidelijke vrachtloodsen; de
#    luchthaven bouwt volgens 2025-nieuws een nieuwe, aparte vrachtterminal, dus dit
#    beeld kan gedateerd zijn (brief §3/§7). Overige drie ankers bron-gelegd.
# ⚠️ Geen fase D/E (brief §6): de brief stopt bewust bij de DMCC-raffinagezone
#    (Emirates Gold/Kaloti) — geen bron noemt een vervolgbestemming.
# ⚠️ Zwakste bronbasis van de golf (brief §7): geen bedrijfsbron koppelt de
#    Siguiri-mijn specifiek aan een Dubai-luchtvrachtstroom — alleen de regionale
#    Swissaid/OECD-bevinding dat West-Afrikaans goud overwegend per lucht naar
#    Dubai gaat, niet mijn-specifiek.
bak_goud_siguiri_dubai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Siguiri-mijn → Conakry Int'l (CKY) vrachtterminal (N1 via Kouroussa–Dabola–Mamou–Kindia–Coyah)|$BEEN/goud-siguiri-dubai-weg-siguiri-cky.geojson" \
    --been-geojson "lucht|vlucht CKY → DXB (vrachtvlucht, grootcirkel)|$BEEN/goud-siguiri-dubai-lucht-cky-dxb.geojson" \
    --been-geojson "truck|vrachtwagen Dubai Intl (DXB) vrachtterminal → DMCC/Almas Tower (Sheikh Zayed Road E11)|$BEEN/goud-siguiri-dubai-weg-dxb-dmcc.geojson" \
    --marker "au-siguiri-mijn — Siguiri-mijn (AngloGold Ashanti/SMD), Kintinian, Boure-gebied — mijn/laadplek, bron-gelegd|11.5695,-9.3567" \
    --marker "au-cky-cargo — Conakry Int'l (Ahmed Sékou Touré, CKY), vracht-/GA-apron — overslag truck → lucht, aannemelijk (nieuwe vrachtterminal in aanbouw, 2025-nieuws)|9.5748,-13.6205" \
    --marker "au-dxb-cargo — Dubai Intl (DXB), Emirates Air Cargo-gebouw, Al Garhoud — overslag lucht → truck, bron-gelegd (hergebruikt anker)|25.2575,55.3406" \
    --marker "au-dubai-dmcc — DMCC / Emirates Gold-Kaloti, Almas Tower, Jumeirah Lake Towers — raffinage-/handelszone, stoppunt, bron-gelegd (hergebruikt anker)|25.0691,55.1412" \
    --routebrief v2/design/routebrieven/goud-siguiri-dubai.md \
    --uit    v2/data/stroomroute-goud-siguiri-dubai.json \
    --stroom goud-siguiri-dubai \
    --titel  "Goud · Siguiri-mijn (Guinee) → Conakry (CKY) → Dubai (DXB) → DMCC"
}

# ── goud · Yanacocha-mijn (Peru) → Lima (LIM) → vrachtvlucht → Zürich (ZRH) →
#    Valcambi-raffinaderij, Balerna (Ticino) — doré per truck/lucht/truck
# Routebrief: v2/design/routebrieven/goud-yanacocha-ticino.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b2 is het EERSTE luchtbeen van de atlas (maak_luchtbeen.py, §2 van de
#    bakhandleiding): grootcirkel LIM → ZRH, 10.667,8 km, DOORGETROKKEN (lucht
#    is nooit stippel — de onzekerheid over één directe vlucht i.p.v. via
#    Miami staat in de beennaam/brief §7, niet in de lijnstijl). Bron voor de
#    modaliteit: Zwitserland raffineert ~70% van 's werelds goud en Valcambi
#    verwerkte naar verluidt ~70% van het Yanacocha-goud (brief §8, bron [8]).
# ⚠️ ÉÉN STIPPEL: het Zürich-vrachtplatform (au-zrh-vrachtterminal) snapt op
#    een geïsoleerde apron-service-way (gemeten: component-grootte 2) —
#    airside/privéterrein zonder aansluiting op het openbare net, ook niet met
#    eindToegangPrivaat (zelfde bevinding als pgm-springs-zurich, ZRH→Kloten-
#    kluis). Been b3 is daarom gescand vanaf het dichtstbijzijnde punt op het
#    openbare wegennet (0,91 km van het platform, gemeten) en de tussenliggende
#    0,91 km is hier een korte stippel "last mile" (airside/privé, §2 Lucht).
# ⚠️ b1 (Yanacocha → Lima) is DOORGETROKKEN: geen deel ligt op privéterrein of
#    <2 km airside (anker-verbindingen 0,41/0,12 km, beide binnen de norm).
# ⚠️ b3-LENGTETOETS BUITEN ±15% (267,1 km tegen ~200 km ontwerpcijfer, +33,5%):
#    bevinding, niet dichtgetrokken — het brief-ontwerpcijfer is een grove
#    schatting van de A4/A2-Gotthard-as; de gemeten route volgt de weg via de
#    Gotthard Base Tunnel-as (Erstfeld) en heeft geen rechte-lijn-afsnijding of
#    lusartefact (521 gesnoeide keerlusmeters uitgezonderd, al verrekend).
bak_goud_yanacocha_ticino() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Yanacocha-mijn → Lima Cargo City (LIM) (Carretera Panamericana Norte)|$BEEN/goud-yanacocha-ticino-weg-yanacocha-lim.geojson" \
    --been-geojson "lucht|vlucht LIM → ZRH (vrachtvlucht, grootcirkel, aannemelijk: één directe vlucht i.p.v. via Miami-hub, §7)|$BEEN/goud-yanacocha-ticino-lucht-lim-zrh.geojson" \
    --stippel      "truck|last mile Zürich Airport vrachtplatform → openbare weg (airside/privéterrein, geen OSM-wegpad tot het platform)|47.4647,8.5492|47.472087,8.554523" \
    --been-geojson "truck|vrachtwagen Zürich Airport vrachtplatform → Valcambi-raffinaderij, Balerna (A4 → A2/Gotthard-as)|$BEEN/goud-yanacocha-ticino-weg-zrh-valcambi.geojson" \
    --marker "au-yanacocha-mijn — Minera Yanacocha (Newmont, 100%), Cajamarca — mijn/laadplek, bron-gelegd|-6.9858,-78.5099" \
    --marker "au-lim-vrachtterminal — Lima Cargo City, Jorge Chávez Int'l (LIM), Callao — overslag/lucht, bron-gelegd|-12.0289,-77.1039" \
    --marker "au-zrh-vrachtterminal — Zürich Airport vrachtplatform — overslag/lucht, bron-gelegd (hergebruikt anker, pgm-springs-zurich)|47.4647,8.5492" \
    --marker "au-valcambi-raffinaderij — Valcambi SA, Balerna (Ticino) — losplek/raffinaderij, stoppunt, bron-gelegd|45.8385,9.0051" \
    --routebrief v2/design/routebrieven/goud-yanacocha-ticino.md \
    --uit    v2/data/stroomroute-goud-yanacocha-ticino.json \
    --stroom goud-yanacocha-ticino \
    --titel  "Goud · Yanacocha-mijn (Peru) → Lima (LIM) → vrachtvlucht → Zürich (ZRH) → Valcambi-raffinaderij (Ticino)"
}

# ── diamant · Letšeng-mijn (Lesotho) → O.R. Tambo (JNB) → vrachtvlucht → Dubai (DXB) → DMCC/Almas Tower
# Routebrief: v2/design/routebrieven/diamant-letseng-dubai.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, Letšeng-mijn → JNB) is +16,2% BOVEN de ontwerp-indicatie (523,1 km
#    tegen ~450 km, routebrief §2/§7) — buiten ±15%, bevinding, niet dichtgetrokken.
#    GIA/G&G bevestigt alleen de $3,7 mln-bergweg en Letšeng↔Maseru 214 km, niet de
#    exacte km naar Johannesburg; het ontwerpcijfer was zelf al "niet apart
#    geverifieerd". `eindToegangPrivaat`+`eindKlassen` (incl. `track`) nodig: zonder
#    die twee vond de scanner GEEN wegpad tussen de mijn en het eerste via-punt
#    Oxbow (33 km) — de eigen bergwegtoegang bij de mijn draagt in OSM een kleine
#    klasse (`track`). Geen stippel: na die uitbreiding routeert de hele corridor
#    door, ankers snappen op 0,04/0,09 km.
# ⚠️ b2 (lucht) is een GROOTCIRKEL JNB → DXB (maak_luchtbeen.py), 6.415,6 km —
#    DOORGETROKKEN, geen stippel (bakhandleiding §2: een vlucht tussen twee gelegde
#    vrachtterminals is geen "net reikt niet"-geval). Dicht bij de ontwerp-indicatie
#    (6.432,4 km, routebrief §2). Geen bron voor een tussenlanding → één directe
#    vlucht aangenomen (routebrief §7).
# ⚠️ b3 (truck, DXB → DMCC) is 37,6 km — binnen de eigen verwachting van de brief
#    ("wegafstand naar verwachting 35-40 km", §2), ondanks +21,3% tegen de
#    hemelsbreed-toetswaarde (31 km) die als vervanger diende omdat er geen
#    gepubliceerd getal bestaat. `dia-dxb-cargo` van DEZE brief (25,2644/55,3661,
#    eigen sat_check.py-anker, routebrief §3) ligt ~2,7 km van het `dia-dxb-cargo`-
#    anker dat de zusterbrieven diamant-marange-dubai/diamant-mbujimayi-dubai
#    gebruiken (andere kandidaat-loods binnen hetzelfde Dubai Cargo Village-complex)
#    — bewust NIET hergebruikt, eigen wegscan met het eigen anker (geen coördinaat
#    verzonnen, wel een tweede onafhankelijke DXB↔DMCC-lijn in de graaf-cache).
# ⚠️ Geen zeebeen (truck + lucht + truck) → geen MARNET/haven-aanloop. Fase D/E
#    vervallen (routebrief §6, stoppunt DMCC/Almas Tower — handels-/
#    certificeringshub, geen fysieke bewerking).
# ⚠️ dia-letseng-mijn/dia-jnb-cargo/dia-dxb-cargo/dia-dmcc-almas zijn alle vier
#    bron-gelegd (satelliet, routebrief §3/§9); de zes via-punten van b1 zijn
#    indicatief (bergpas-/grensroute zonder zinnig alternatief), niet zelf
#    satelliet-gelegd (routebrief §4).
bak_diamant_letseng_dubai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Letšeng-mijn → O.R. Tambo vrachtapron (JNB) (eigen bergweg → Oxbow/Tlaeeng-Moteng-pas → Butha-Buthe → Caledonspoort → Fouriesburg → Bethlehem → Villiers)|$BEEN/diamant-letseng-dubai-weg-letseng-jnb.geojson" \
    --been-geojson "lucht|vlucht JNB → DXB (vrachtvlucht, grootcirkel)|$BEEN/diamant-letseng-dubai-lucht-jnb-dxb.geojson" \
    --been-geojson "truck|vrachtwagen DXB-vrachtterminal → DMCC/Almas Tower (Al Garhoud → Sheikh Zayed Road E11 → JLT)|$BEEN/diamant-letseng-dubai-weg-dxb-dmcc.geojson" \
    --marker "dia-letseng-mijn — Letšeng-mijn (Gem Diamonds + regering Lesotho), 3.100 m — mijn/laadplek, bron-gelegd|-29.00028,28.86194" \
    --marker "dia-jnb-cargo — O.R. Tambo vrachtapron (Golf/Whiskey), Kempton Park — overslag truck→lucht, bron-gelegd|-26.14300,28.22700" \
    --marker "dia-dxb-cargo — Dubai Cargo Village/Cargo Gateway, Al Garhoud — overslag lucht→truck, bron-gelegd|25.26440,55.36610" \
    --marker "dia-dmcc-almas — DMCC/Almas Tower, Jumeirah Lake Towers — handels-/certificeringshub, stoppunt, bron-gelegd|25.06890,55.14120" \
    --routebrief v2/design/routebrieven/diamant-letseng-dubai.md \
    --uit    v2/data/stroomroute-diamant-letseng-dubai.json \
    --stroom diamant-letseng-dubai \
    --titel  "Diamant · Letšeng-mijn (Lesotho) → Johannesburg (JNB) → Dubai (DXB) → DMCC/Almas Tower"
}

# ── goud · Canadian Malartic-mijn (Agnico Eagle, Québec) → Royal Canadian Mint (Ottawa)
# Routebrief: v2/design/routebrieven/goud-malartic-ottawa.md (LICHTE werkwijze M31 golf 3)
# ⚠️ Eén enkel wegbeen (b1), doorgetrokken — geen zee/spoor/lucht (brief §7
#    bevestigt: truck-only, bakhandleiding §2 "Lucht" niet van toepassing).
# ⚠️ Geen gepubliceerde route-km: 451,6 km gebakken tegen de ontwerp-schatting
#    480 km (-5,9%, [OK]) — de brief zegt zelf dat de toets tegen een schatting
#    staat, niet een harde bron (via-puntensom hemelsbreed 398,0 km).
# ⚠️ Geen stippels: het hele traject (Route 117 → Route 105 → Autoroute 5) ligt
#    op doorgaande wegen tot aan het RCM-terrein; de anker-verbindingsstukjes
#    (plant → weg 0,08 km · weg → kade 0,05 km) zijn ruim binnen de norm.
# ⚠️ Geen fase D/E: de brief stopt bij de RCM-raffinaderij (§6, geen bron
#    documenteert een specifieke vervolgzending per lading).
bak_goud_malartic_ottawa() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Canadian Malartic-mijn → Royal Canadian Mint Ottawa (Route 117 → Route 105 → Autoroute 5)|$BEEN/goud-malartic-ottawa-weg-malartic-ottawa.geojson" \
    --marker "au-malartic-mijn — Canadian Malartic Mine (Agnico Eagle), Malartic, Québec — mijn/laadplek, bron-gelegd|48.1176,-78.0942" \
    --marker "au-rcm-ottawa — Royal Canadian Mint, 320 Sussex Drive, Ottawa — raffinaderij/muntslag, stoppunt, bron-gelegd|45.4315,-75.6993" \
    --routebrief v2/design/routebrieven/goud-malartic-ottawa.md \
    --uit    v2/data/stroomroute-goud-malartic-ottawa.json \
    --stroom goud-malartic-ottawa \
    --titel  "Goud · Canadian Malartic-mijn (Québec) → Royal Canadian Mint (Ottawa)"
}

# ── goud · Loulo-Gounkoto-mijncomplex (Mali) → Bamako-Sénou → Zürich (ZRH) → Valcambi (Balerna, Ticino)
# Routebrief: v2/design/routebrieven/goud-loulo-ticino.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, DOORGETROKKEN): Loulo-mijn → Bamako-Sénou vrachtterminal via
#    Kéniéba–Kita. Gebakken 479,7 km tegen ~380 (ontwerp) = +26,2%, BUITEN de
#    ±15%-norm — bevinding, niet dichtgetrokken (de brief noemt de via-punten
#    zelf als "indicatief, niet OSM-wegvertex-geverifieerd binnen het
#    webbudget"; het echte OSM-wegnet loopt kennelijk verder om dan de
#    hemelsbrede via-som suggereert).
# ⚠️ b2 (lucht, DOORGETROKKEN, §2 "Lucht" letterlijk gevolgd): vlucht
#    BKO → ZRH als grootcirkel, 4.176,8 km — sluit vrijwel exact aan op de
#    brief-schatting (~4.180 km). Aannemelijk (geen bron voor déze specifieke
#    lading, West-Afrikaanse doré-export naar Zwitserse raffinaderijen is
#    industriestandaard, brief §7); geen tussenlanding gebrond → één directe
#    vlucht.
# ⚠️ b3 (truck, DOORGETROKKEN): Zürich Airport vrachtplatform → Valcambi
#    Balerna via A4 (Zug–Luzern) → A2/Gotthard-as (Bellinzona–Lugano–Chiasso).
#    Het vrachtplatform-anker zelf (au-zrh-vrachtterminal, 47,4647/8,5492)
#    snapt op een geïsoleerde airside-apron-way zonder aansluiting op het
#    openbare net (twee mislukte pogingen: "geen wegpad tussen punt 0 en 1",
#    ook mét eindToegangPrivaat) — exact dezelfde bevinding als het analoge
#    been in goud-yanacocha-ticino-valcambi (zelfde ZRH-anker, zelfde golf).
#    Profiel start op het dichtstbijzijnde punt van het openbare wegennet
#    (47,472087/8,554523, 0,91 km van het platform); de korte tussenliggende
#    stippel hieronder draagt die 0,91 km airside/privéterrein. Gebakken
#    268,4 km tegen ~200 (ontwerp) = +34,2%, BUITEN de ±15%-norm — bevinding
#    (géén betrouwbare alternatieve wegreferentie; via-punten volgen de
#    A4/A2-Gotthard-as letterlijk, het OSM-wegnet incl. klaverbladlussen bij
#    Zug/Luzern/Bellinzona maakt de rit langer dan de hemelsbrede schatting).
# ⚠️ Geen fase D/E: de brief stopt bij Valcambi (§6, geen bron koppelt déze
#    Mali-doré aan een specifieke vervolgbestemming).
bak_goud_loulo_ticino() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Loulo-Gounkoto-mijncomplex → Bamako-Sénou vrachtterminal (BKO) (Kéniéba–Kita-corridor)|$BEEN/goud-loulo-ticino-weg-loulo-bamako.geojson" \
    --been-geojson "lucht|vlucht BKO → ZRH (vrachtvlucht, grootcirkel)|$BEEN/goud-loulo-ticino-lucht-bko-zrh.geojson" \
    --stippel      "truck|ZRH-vrachtplatform last mile (schematisch — airside/privéterrein zonder aansluiting op het openbare net)|47.4647,8.5492|47.472087,8.554523" \
    --been-geojson "truck|vrachtwagen Zürich Airport vrachtplatform → Valcambi-raffinaderij, Balerna (A4 Zug-Luzern → A2/Gotthard-as via Bellinzona–Lugano–Chiasso)|$BEEN/goud-loulo-ticino-weg-zrh-valcambi.geojson" \
    --marker "au-loulo-mijn — Loulo-Gounkoto-mijncomplex, verwerkingsinstallatie (Barrick) — mijn/laadplek, bron-gelegd|13.0868,-11.4118" \
    --marker "au-bamako-vrachtterminal — Bamako-Sénou Int'l (BKO), terreincluster W van de startbaan — overslag truck → lucht, bron-gelegd (pand onzeker)|12.5353,-7.9488" \
    --marker "au-zrh-vrachtterminal — Zürich Airport vrachtplatform (hergebruikt anker uit pgm-springs-zurich.md) — overslag lucht → truck, bron-gelegd|47.4647,8.5492" \
    --marker "au-ref-valcambi — Valcambi SA, Via Passeggiata 3, Balerna — raffinaderij, stoppunt, bron-gelegd|45.8385,9.0051" \
    --routebrief v2/design/routebrieven/goud-loulo-ticino.md \
    --uit    v2/data/stroomroute-goud-loulo-ticino.json \
    --stroom goud-loulo-ticino \
    --titel  "Goud · Loulo-Gounkoto (Mali) → Bamako-Sénou → Zürich (ZRH) → Valcambi (Balerna, Ticino)"
}

# ── goud · Kalgoorlie Super Pit → Perth Mint → Perth Airport (PER) → vrachtvlucht → Singapore Changi (SIN) → GoldSilver Central
# Routebrief: v2/design/routebrieven/goud-kalgoorlie-singapore.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b3 is een LUCHTBEEN (maak_luchtbeen.py, §2 van de bakhandleiding): grootcirkel
#    PER → SIN, 3.914,5 km, DOORGETROKKEN — een vlucht tussen twee gelegde
#    vrachtterminals is geen gat. Geen bron voor een tussenlanding → één
#    rechtstreekse vlucht aangenomen (brief §7).
# ⚠️ b4 IS EEN STIPPEL, EN DAT IS CENTRAAL WERK, GEEN BAKFOUT: de
#    'singapore'-Geofabrik-extract ontbreekt lokaal (alleen 'maleisie' staat
#    er, bevestigd bij het schrijven van de brief én opnieuw bij het bakken) —
#    "geen net op deze korrel" (bakhandleiding §2). De via-punten liggen al
#    klaar in de brief §4 voor zodra de extract gedownload is (centraal werk).
# ⚠️ b2 (Perth Mint → PER-vrachtterminal) is +23,5% BOVEN de ontwerp-schatting
#    van ~12 km (gemeten 14,8 km) — bevinding, niet dichtgetrokken: 12 km was
#    een hemelsbreed-afgeleide ontwerpschatting, geen gepubliceerde
#    wegbeheerder-lengte (brief §2/§8[1]).
# ⚠️ au-per-cargo (Qantas Freight Int'l Terminal) draagt geen "Cargo"-naam-tag
#    in OSM; geen bron bevestigt specifiek dat Perth Mint-baren via déze
#    terminal (i.p.v. dnata) worden verzonden (brief §7).
bak_goud_kalgoorlie_singapore() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Kalgoorlie Super Pit/Fimiston-mill → Perth Mint, East Perth (Great Eastern Highway)|$BEEN/goud-kalgoorlie-singapore-weg-kalgoorlie-perth.geojson" \
    --been-geojson "truck|vrachtwagen Perth Mint, East Perth → Perth Airport (PER) vrachtterminal (Great Eastern Hwy → Tonkin Hwy)|$BEEN/goud-kalgoorlie-singapore-weg-perth-percargo.geojson" \
    --been-geojson "lucht|vlucht PER → SIN (vrachtvlucht, grootcirkel, aannemelijk: één directe vlucht, geen tussenlanding gebrond, §7)|$BEEN/goud-kalgoorlie-singapore-lucht-per-sin.geojson" \
    --stippel      "truck|geen net op deze korrel (Geofabrik-extract 'singapore' ontbreekt, centraal werk — bakhandleiding §3)|1.37753,103.9976|1.275755,103.8459" \
    --marker "au-kalgoorlie-mill — Kalgoorlie Super Pit / KCGM Fimiston-mill-complex, Boulder — mijn/laadplek, bron-gelegd|-30.7897,121.4990" \
    --marker "au-ref-perth — The Perth Mint, East Perth — raffinaderij/verwerkingsknoop, bron-gelegd|-31.9550,115.8700" \
    --marker "au-per-cargo — Qantas Freight International Terminal, Affleck Road, Ascot (Perth Airport) — overslag truck → lucht, bron-gelegd|-31.9460,115.9764" \
    --marker "au-sin-cargo — Changi Airfreight Centre / SATS Airfreight Terminal, Singapore Changi Airport — overslag lucht → truck, bron-gelegd|1.37753,103.9976" \
    --marker "au-sin-vault — GoldSilver Central, #23-16 International Plaza, 10 Anson Road, Singapore — kluis-/handelsgebouw, stoppunt, bron-gelegd|1.275755,103.8459" \
    --routebrief v2/design/routebrieven/goud-kalgoorlie-singapore.md \
    --uit    v2/data/stroomroute-goud-kalgoorlie-singapore.json \
    --stroom goud-kalgoorlie-singapore \
    --titel  "Goud · Kalgoorlie Super Pit → Perth Mint → Perth (PER) → Singapore (SIN) → GoldSilver Central"
}

# ── goud · Mponeng-mijn (Harmony, Witwatersrand) → Rand Refinery → OR Tambo (JNB) → Heathrow (LHR) → LBMA-kluis (Londen)
# Routebrief: v2/design/routebrieven/goud-mponeng-londen.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ Vier benen, alle DOORGETROKKEN — geen enkele stippel in deze keten (geen
#    zeebeen, geen ontbrekend net).
# ⚠️ b1 (truck, profiel goud-mponeng-londen-mponeng-randrefinery) via
#    Westonaria → Soweto (N12/R28-industriecorridor): 85,8 km tegen een eigen
#    schatting van ≈77 km (+11,2%). Geen gepubliceerde bron (brief §7); de
#    ±15%-toets is soepel toegepast conform het bak-aanwijzingen-advies (een
#    uitkomst tussen 76 en ~100 km is plausibel) — 85,8 km valt daarbinnen.
# ⚠️ b2 (truck, profiel goud-mponeng-londen-randrefinery-jnb) Rand Refinery →
#    OR Tambo-vrachtterminal: 25,6 km tegen de redactionele schatting van
#    ≈15 km (+70,8%, BUITEN ±15% — bevinding, niet dichtgetrokken). De brief
#    noemt die 15 km zelf al als "niet hard" (rechte afstand is al 11,2 km);
#    de gemeten R21/N12-route is de echte controle. Eerste poging faalde op
#    "geen wegpad" (JNB-vrachtapron is airside/deels privéterrein, zoals het
#    dia-jnb-cargo-anker elders in dit bestand) → eindToegangPrivaat +
#    eindKlassen incl. track toegevoegd aan het profiel, tweede poging slaagde.
# ⚠️ b3 (lucht, maak_luchtbeen.py) is een GROOTCIRKEL tussen twee vracht-
#    terminals, DOORGETROKKEN — stippel betekent uitsluitend "hier reikt het
#    net niet" en een vlucht tussen twee gelegde vrachtterminals is geen gat
#    (bakhandleiding §2 Lucht). 9.074,3 km, tegen de gepubliceerde ≈9.070 km
#    (brief §2/§8[1]) — geen km-toets voor een luchtbeen (§5 van de
#    handleiding). Aanname: één directe vlucht JNB → LHR, geen tussenlanding
#    (brief §7, geen bron noemt een hub); bron voor de modaliteit is
#    markt-niveau (LBMA/WGC), niet Rand Refinery-specifiek — vandaar
#    "aannemelijk: één bron" in de beennaam.
# ⚠️ b4 (truck, profiel goud-mponeng-londen-lhr-lbma) via Hounslow → Chiswick
#    → Hammersmith (M4/A4): 30,9 km tegen een eigen schatting van ≈27 km
#    (+14,4%, binnen ±15%).
# ⚠️ au-lbma-kluis (51,514/-0,088) is hergebruikt van v1 (au-hub-london uit
#    `data/goud.js`) — een generiek City-anker (Bank of England-omgeving),
#    geen specifiek kluisadres van Brink's/Malca-Amit/Loomis (brief §3/§7).
# ⚠️ Geen fase D/E: de brief stopt bij de LBMA-kluis (brief §6, geen bron
#    noemt een vervolgbestemming ná de Londense kluis).
bak_goud_mponeng_londen() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Mponeng-mijn → Westonaria → Soweto → Rand Refinery, Germiston (N12/R28)|$BEEN/goud-mponeng-londen-weg-mponeng-randrefinery.geojson" \
    --been-geojson "truck|Rand Refinery, Germiston → OR Tambo (JNB) vrachtterminal (R21/N12)|$BEEN/goud-mponeng-londen-weg-randrefinery-jnb.geojson" \
    --been-geojson "lucht|vlucht JNB → LHR (vrachtvlucht, grootcirkel, aannemelijk: één bron)|$BEEN/goud-mponeng-londen-lucht-jnb-lhr.geojson" \
    --been-geojson "truck|Heathrow-vrachtterminal → Hounslow → Chiswick → Hammersmith → LBMA-kluis City of London (M4/A4)|$BEEN/goud-mponeng-londen-weg-lhr-lbma.geojson" \
    --marker "au-mponeng-mijn — Mponeng Gold Mine, Harmony Gold, Witwatersrand — mijn/laadplek, bron-gelegd|-26.4361,27.4306" \
    --marker "au-randrefinery — Rand Refinery (Pty) Ltd, Germiston — raffinaderij (overslag truck→truck), bron-gelegd|-26.2189,28.1550" \
    --marker "au-jnb-vracht — OR Tambo (JNB) vrachtterminal, zuid van de passagiersterminal — overslag truck→lucht, bron-gelegd|-26.1440,28.2295" \
    --marker "au-lhr-vracht — Heathrow Cargo Centre, Sandringham Road — overslag lucht→truck, bron-gelegd|51.4605,-0.4680" \
    --marker "au-lbma-kluis — LBMA/Bank of England-omgeving, City of London — losplek/stoppunt, bron-gelegd (hergebruik au-hub-london)|51.5140,-0.0880" \
    --routebrief v2/design/routebrieven/goud-mponeng-londen.md \
    --uit    v2/data/stroomroute-goud-mponeng-londen.json \
    --stroom goud-mponeng-londen \
    --titel  "Goud · Mponeng-mijn (Zuid-Afrika) → Rand Refinery → OR Tambo (JNB) → Heathrow (LHR) → LBMA-kluis (Londen)"
}

# ── diamant · Surat Diamond Bourse (India) → Bharat Diamond Bourse (BKC) → CSMIA (BOM) → (vlucht) → Cathay Pacific Cargo Terminal (HKG) → Hong Kong Diamond Exchange Building
# Routebrief: v2/design/routebrieven/diamant-surat-hongkong.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, KORTE STIPPEL + been-geojson): DREAM City (Surat Diamond Bourse) heeft
#    een EIGEN wegenstelsel dat in OSM een geïsoleerd component van 57 knopen vormt —
#    een echt topologiegat, geen access-filter (`eindToegangPrivaat` loste dit dus niet
#    op). Gemeten (BFS op de india-scan): component vanaf het anker 57 knopen tegen
#    1.780.308 vanaf Navsari; dichtstbijzijnde publieke-netpunt 17 m van dat interne
#    component, 0,33 km hemelsbreed vanaf het anker. Korte stippel anker → routeerpunt
#    (bakhandleiding §2, "korter dan ~2 km"), dan de gemeten weg vanaf het routeerpunt:
#    279,5 km tegen ~280 km ontwerp = -0,2% [OK].
# ⚠️ b2 (truck, BDB → CSMIA) is een GESPIEGELDE KOPIE van diamant-mirny-mumbai b4
#    (CSMIA → BDB, omgekeerde richting): fysiek hetzelfde Airport Road/BKC-connector-
#    been, geen tweede scan gedraaid (bakhandleiding: hergebruik i.p.v. opnieuw
#    scannen). Coördinaten gespiegeld, geen enkel punt herberekend.
# ⚠️ b3 (lucht) DOORGETROKKEN, geen stippel: grootcirkel BOM → HKG, 4.272,8 km — exact
#    de berekende grootcirkel uit de brief. Geen tussenlanding gebrond (brief §7) → één
#    directe vlucht.
# ⚠️ b4 (truck, eindToegangPrivaat) op de china-extract: Cathay Pacific Cargo Terminal
#    (Chek Lap Kok) ligt airside/op luchthaventerrein, dus de eerste km loopt over
#    kleine wegklassen (eindToegangPrivaat) zonder aparte stippel. Geen harde
#    gepubliceerde km (brief §2); via-punten-som 32,4 km, gemeten 40,7 km = +25,8%
#    [BUITEN ±15% — bevinding, niet dichtgetrokken: HK-tunnels/bruggen maken een
#    reële omweg t.o.v. de rechte via-keten].
# ⚠️ dia-bdb en dia-bom-cargo zijn HERGEBRUIKTE ankers uit diamant-mirny-mumbai.md
#    (deze golf, al satelliet-gelegd) — hier opnieuw als marker opgegeven zodat deze
#    stroom zelfstandig markers draagt, geen dubbele registratie bedoeld.
# ⚠️ Geen haven-aanloop nodig: geen zeebenen in deze keten (alleen truck + lucht).
# ⚠️ Geen fase D/E (brief §6): geen bron koppelt déze stroom aan een vervolgbestemming
#    ná het Hong Kong Diamond Exchange Building.
bak_diamant_surat_hongkong() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "truck|DREAM City interne toegangsweg → NH48-aansluiting (schematisch — OSM-topologiegat tussen het eigen wegenstelsel van de bourse en het publieke net, 0,33 km hemelsbreed)|21.1099,72.7954|21.112178,72.79343" \
    --been-geojson "truck|vrachtwagen NH48-aansluiting → Bharat Diamond Bourse (NH48 Surat–Mumbai)|$BEEN/diamant-surat-hongkong-weg-surat-bdb.geojson" \
    --been-geojson "truck|vrachtwagen Bharat Diamond Bourse → CSMIA Air Cargo Complex (Airport Road/BKC-connector, gespiegeld hergebruikt van diamant-mirny-mumbai b4)|$BEEN/diamant-surat-hongkong-weg-bdb-bomcargo.geojson" \
    --been-geojson "lucht|vlucht BOM → HKG (vrachtvlucht, grootcirkel)|$BEEN/diamant-surat-hongkong-lucht-bom-hkg.geojson" \
    --been-geojson "truck|vrachtwagen Cathay Pacific Cargo Terminal (HKG) → Hong Kong Diamond Exchange Building (North Lantau Hwy → Tsing Ma Bridge → Kwai Chung → Western Harbour Crossing)|$BEEN/diamant-surat-hongkong-weg-hkgcargo-hkexchange.geojson" \
    --marker "dia-surat-bourse — Surat Diamond Bourse, DREAM City, Surat, Gujarat — beursgebouw/vertrekpunt (slijperij-omgeving), laadplek, bron-gelegd|21.1099,72.7954" \
    --marker "dia-bdb — Bharat Diamond Bourse, BKC, Mumbai — beursgebouw/doorvoerpunt, bron-gelegd (hergebruikt anker)|19.0641,72.8646" \
    --marker "dia-bom-cargo — CSMIA Air Cargo Complex, Sahar, Mumbai — vrachtterminal, vertrek luchtvracht, bron-gelegd (hergebruikt anker)|19.0994,72.8673" \
    --marker "dia-hkg-cargo — Cathay Pacific Cargo Terminal, Chek Lap Kok, Hong Kong — vrachtterminal, aankomst luchtvracht, bron-gelegd|22.2975,113.9247" \
    --marker "dia-hk-exchange — Hong Kong Diamond Exchange Building, 20 Ice House Street, Central — beurs-/handelsgebouw, stoppunt, bron-gelegd|22.2797,114.1570" \
    --routebrief v2/design/routebrieven/diamant-surat-hongkong.md \
    --uit    v2/data/stroomroute-diamant-surat-hongkong.json \
    --stroom diamant-surat-hongkong \
    --titel  "Diamant · Surat Diamond Bourse (India) → Mumbai (CSMIA) → Hong Kong (Cathay Pacific Cargo/HK Diamond Exchange)"
}

# ── diamant · Gaborone (DTCB/DBGSS) → GBE-vrachtapron → CSMIA Air Cargo Complex (BOM) → Surat Diamond Bourse
# Routebrief: v2/design/routebrieven/diamant-gaborone-surat.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# Drie benen doorgetrokken + één korte stippel op het eind — geen zeebeen, dus geen haven-aanloop.
# ⚠️ b2 (lucht) is een GROOTCIRKEL GBE → BOM (maak_luchtbeen.py), 7.027,6 km — komt exact
#    overeen met de brief-schatting. Geen bron voor een tussenlanding (JNB/DXB) → één directe
#    vlucht aangenomen (brief §7).
# ⚠️ b3 (BOM → Surat Diamond Bourse-omgeving, fase C NIEUW t.o.v. het oorspronkelijke STV-
#    ontwerp) is ZELF GELEGD — géén bestaand spiegelbeen gevonden (keten diamant-surat-hongkong
#    bestaat wel in deze golf en deelt hetzelfde SDB-anker, maar is een ANDERE as: Surat→Hongkong
#    langs de NH48 rícht Mumbai, niet BOM→Surat). Eigen NH48-corridorkeuze met 6 via-punten
#    (Manor–Talasari–Vapi–Valsad–Navsari–Sachin), 273,3 km tegen ~280 km (haalbaarheidstoets) =
#    -2,4% [OK]. Twee via-punt-correcties tijdens het bakken (geen km-toets-manipulatie, beide
#    "geen wegpad"-fouten):
#    · Valsad: het briefpunt (72,9260/20,6100, Wikipedia-stadscentroïde) snapte op 113 m naar een
#      geïsoleerd stompje van 3 knopen — de échte NH48 (trunk) omzeilt de stad ~3 km zuidwestelijker
#      (bypass). Via-punt verplaatst naar een vertex ÓP de NH48-trunk (72,9512/20,5968).
#    · Surat Diamond Bourse: het ANKER zelf (dia-sdb, 21,1097/72,7953, satelliet-gelegd) snapt op
#      134 m naar een geïsoleerd DREAM City-wegennet van 57 knopen; het doorgaande publieke net ligt
#      287 m verderop. Weg-profiel eindigt op dat ROUTEERPUNT (anker ≠ routeerpunt, staand
#      projectpatroon); de resterende 0,29 km is hieronder een expliciete korte stippel — dezelfde
#      OSM-topologiegat-klasse die diamant-surat-hongkong (deze golf) voor hetzelfde DREAM
#      City-terrein al meldt (daar 0,33 km, aan de Mumbai-zijde van het complex).
# ⚠️ dia-gbe-cargo AANNEMELIJK op naam ("Cargo" niet in OSM), maar SATELLIET-GELEGD (z18: loodsen
#    + apron met vrachttoestellen, los van de passagiersterminal) — status bron-gelegd volgens de
#    brief. Een zusterstroom in deze golf (diamant-jwaneng-antwerpen) legt hetzelfde GBE-vrachtapron
#    ~500 m verderop (-24,5576/25,9242, "aannemelijk") — niet overgenomen: dit stroom-eigen anker
#    komt uit de eigen z18-satellietpas van déze brief (dia-gbe-cargo, -24,5550/25,9286,
#    "bron-gelegd") en blijft leidend voor déze stroom (gemeld, niet stilzwijgend samengevoegd).
# ⚠️ dia-bom-cargo is een HERGEBRUIKT anker (ongewijzigd uit diamant-mirny-mumbai.md, zelfde golf).
bak_diamant_gaborone_surat() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen DTCB/DBGSS-diamanthub → GBE-vrachtapron (A1/Western Bypass Road)|$BEEN/diamant-gaborone-surat-weg-dtc-gbe.geojson" \
    --been-geojson "lucht|vlucht GBE → BOM (vrachtvlucht, grootcirkel)|$BEEN/diamant-gaborone-surat-lucht-gbe-bom.geojson" \
    --been-geojson "truck|ruwe diamant CSMIA Air Cargo Complex (BOM) → Surat Diamond Bourse-omgeving (NH48 Mumbai–Ahmedabad Highway → routeerpunt)|$BEEN/diamant-gaborone-surat-weg-bom-sdb.geojson" \
    --stippel      "truck|DREAM City interne toegangsweg → NH48-omgeving (schematisch — OSM-topologiegat tussen het eigen wegenstelsel van de bourse en het publieke net, 0,29 km)|21.107445,72.796653|21.1097,72.7953" \
    --marker "dia-gaborone-dtc — DTCB/DBGSS-diamanthub, Gaborone — mijn/sight-aggregatie, laadplek, bron-gelegd|-24.5859,25.9144" \
    --marker "dia-gbe-cargo — GBE-vrachtapron, Sir Seretse Khama Intl Airport — vrachtterminal, vertrek luchtvracht, bron-gelegd|-24.5550,25.9286" \
    --marker "dia-bom-cargo — CSMIA Air Cargo Complex, Sahar, Mumbai — vrachtterminal, aankomst luchtvracht, hergebruikt anker, bron-gelegd|19.0994,72.8673" \
    --marker "dia-sdb — Surat Diamond Bourse, DREAM City, Surat — beursgebouw + slijperij-cluster, stoppunt, bron-gelegd|21.1097,72.7953" \
    --routebrief v2/design/routebrieven/diamant-gaborone-surat.md \
    --uit    v2/data/stroomroute-diamant-gaborone-surat.json \
    --stroom diamant-gaborone-surat \
    --titel  "Diamant · Gaborone (DTCB/DBGSS) → GBE → BOM → Surat Diamond Bourse"
}

# ── goud · DMCC-raffinagezone (Dubai) → DXB-vrachtterminal → vrachtvlucht → DEL-vrachtterminal → MMTC-PAMP (Rojka Meo, Sohna)
# Routebrief: v2/design/routebrieven/goud-dubai-delhi.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b2 is een LUCHTBEEN (maak_luchtbeen.py, §2 van de bakhandleiding): grootcirkel
#    DXB → DEL, 2.185,2 km, DOORGETROKKEN — geen bron noemt een tussenlanding →
#    één rechtstreekse vlucht aangenomen (brief §7). Bron voor de modaliteit is
#    marktniveau (decennialang gerapporteerde Dubai–India-bullioncorridor,
#    WGC/RBI/DGFT-importstatistieken), geen vluchtnummer-/AWB-bevestiging.
# ⚠️ b1 (truck, DMCC-raffinagezone → DXB-vrachtterminal): 22,9 km tegen ≈20 km
#    eigen meting (+14,5% — binnen ±15%, geen bevinding).
# ⚠️ b3 (truck, DEL-vrachtterminal → MMTC-PAMP Rojka Meo): 45,3 km tegen ≈50–55 km
#    eigen meting (-13,0% — binnen ±15%, geen bevinding). ⚠️ "Manesar" in de
#    ketennaam ≠ de plaats Manesar (28,3553/76,9327, andere corridor via NH48
#    richting Jaipur) — route/anker volgen het satelliet-bevestigde Rojka Meo-
#    punt (brief §7).
# ⚠️ au-air-del (Delhi Air Cargo Complex) blijft "bron-gelegd, met voorbehoud":
#    cargo-warehouse en een naastgelegen hangaarcomplex liggen dicht tegen elkaar
#    op het satellietbeeld (brief §3/§7; beheerwissel Celebi → GMR, mei 2025).
# ⚠️ Geen fase E: de Delhi-sieradenmarkt is niet als apart been getekend (geen
#    gebronde vervolgzending, brief §6). Geen haven-aanloop, geen zeebeen.
bak_goud_dubai_delhi() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen DMCC-raffinagezone (Gold & Diamond Park, Al Quoz 3) → DXB-vrachtterminal (Emirates SkyCargo) (Sheikh Zayed Rd → Al Rebat St/Cargo Village Rd)|$BEEN/goud-dubai-delhi-weg-dmcc-dxb.geojson" \
    --been-geojson "lucht|vlucht DXB → DEL (vrachtvlucht, grootcirkel, aannemelijk: één directe vlucht, geen tussenlanding gebrond, §7)|$BEEN/goud-dubai-delhi-lucht-dxb-del.geojson" \
    --been-geojson "truck|vrachtwagen DEL-vrachtterminal (Delhi Air Cargo Complex) → MMTC-PAMP-raffinaderij, Rojka Meo, Sohna (NH48 Delhi–Gurugram Expwy → Sohna Road)|$BEEN/goud-dubai-delhi-weg-del-mmtc.geojson" \
    --marker "au-dmcc-refine — Gold & Diamond Park, Al Quoz Industrial 3, Dubai (DMCC-vergunde precious-metals-zone) — laadplek (raffinage/handelszone), bron-gelegd|25.1261,55.2089" \
    --marker "au-air-dxb — DXB-vrachtterminal (Emirates SkyCargo) — overslag truck → lucht, bron-gelegd|25.2560,55.3434" \
    --marker "au-air-del — Delhi Air Cargo Complex, IGI Airport (bij Terminal 3) — overslag lucht → truck, bron-gelegd met voorbehoud|28.5570,77.1000" \
    --marker "au-ref-mmtc — MMTC-PAMP India Pvt Ltd, Rojka Meo, Sohna (Gurugram/Nuh-district) — raffinaderij, stoppunt, bron-gelegd|28.2140,77.0611" \
    --routebrief v2/design/routebrieven/goud-dubai-delhi.md \
    --uit    v2/data/stroomroute-goud-dubai-delhi.json \
    --stroom goud-dubai-delhi \
    --titel  "Goud · Dubai (DMCC) → DXB → DEL → MMTC-PAMP (Rojka Meo, Sohna)"
}

# ── goud · Argor-Heraeus, Mendrisio (Zwitserland) → Milaan-Malpensa (MXP) → vrachtvlucht → Mumbai (BOM) → Zaveri Bazaar
# Routebrief: v2/design/routebrieven/goud-argor-mumbai.md (LICHTE werkwijze M31 golf 3, §2 Lucht)
# ⚠️ b1 (truck, doorgetrokken, profiel goud-argor-mumbai-argor-mxp, extracts
#    zwitserland+italie): Argor-Heraeus, Mendrisio → A2 (CH) → Chiasso-grens
#    → A9/A8 (IT) → Malpensa-vrachtterminal. 75,9 km tegen ~70 km
#    (ontwerpschatting, geen officiële wegbeheerder-lengte gevonden voor een
#    grensoverschrijdend CH→IT-traject) = +8,4%, binnen ±15%. Anker-
#    verbindingen 0,02/0,09 km — geen stippel nodig. 235 keerlussen
#    gesnoeid (79,5 → 75,9 km).
# ⚠️ b2 (lucht, doorgetrokken, maak_luchtbeen.py): grootcirkel Milaan-
#    Malpensa (MXP) → Mumbai (BOM), **6.508,5 km, 262 punten** — exact de
#    gemeten waarde uit de brief. Geen km-toets (een luchtbeen ís de
#    grootcirkel per constructie). Geen tussenlanding gebrond (brief §7) →
#    één directe vlucht.
# ⚠️ KORTE STIPPEL vóór b3: het anker au-air-bom (Mumbai Air Cargo Complex,
#    Sahar, 19,0954/72,8660) snapt op een GEÏSOLEERD airside-wegcomponent —
#    gemeten met een BFS over de india-scan: componentgrootte 9 vanaf het
#    anker tegen 178.739 op het publieke net, dichtstbijzijnde publieke-
#    netknoop 0,117 km van de anker-snap. `eindToegangPrivaat` lost dit niet
#    op (COMPONENT-scheiding, geen ACCESS-filter — zelfde klasse als
#    au-zrh-vrachtterminal in goud-yanacocha-ticino en dia-surat-bourse in
#    diamant-surat-hongkong). Eerste via-punt van b3 is daarom het
#    routeerpunt op het publieke net (72,865345/19,096391, 0,13 km van het
#    anker); de korte stippel tekent anker → routeerpunt.
# ⚠️ b3 (truck, doorgetrokken vanaf het routeerpunt, profiel
#    goud-argor-mumbai-bom-zaveri, extract india): BOM-vrachtterminal
#    (routeerpunt) → Vile Parle (Western Express Highway) → Bandra West →
#    Mahim → Worli (Dr. Annie Besant Road) → Crawford Market → Zaveri
#    Bazaar. 26,3 km tegen ~25 km (ontwerpschatting) = +5,4%, binnen ±15%.
#    De brief hield rekening met een mogelijke korte stippel bij Kalbadevi
#    (smalle marktstraten) — bleek niet nodig: `trimStaart` knipte 1 punt
#    overschiet-en-terug (26,36 → 26,34 km) en de lijn eindigt gewoon op het
#    au-mkt-zaveri-anker, 0,01 km snap.
# ⚠️ Zaveri Bazaar-anker blijft "aannemelijk" (brief §3/§7): een marktwijk
#    zonder los aan te wijzen gebouw, coördinaat = het Wikipedia-punt van de
#    bazaar — dat verschijnt in de brief/§7, niet in de lijnstijl (doorgetrokken).
# ⚠️ Geen fase D/E (brief §6): de brief stopt bewust bij Zaveri Bazaar als
#    groothandelsschakel; geen bron noemt een specifieke juwelier/beursgebouw
#    erna.
bak_goud_argor_mumbai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Argor-Heraeus, Mendrisio → Milaan-Malpensa (MXP) vrachtterminal (A2 CH → grens Chiasso → A9/A8 IT)|$BEEN/goud-argor-mumbai-weg-argor-mxp.geojson" \
    --been-geojson "lucht|vlucht MXP → BOM (vrachtvlucht, grootcirkel)|$BEEN/goud-argor-mumbai-lucht-mxp-bom.geojson" \
    --stippel      "truck|BOM-vrachtterminal (Sahar) → openbare-wegaansluiting (schematisch — OSM-topologiegat: airside-wegcomponent van 9 knopen, geen aansluiting op het publieke net binnen het venster)|19.0954,72.8660|19.096391,72.865345" \
    --been-geojson "truck|vrachtwagen openbare-wegaansluiting bij BOM → Zaveri Bazaar-sieradenmarkt (Western Express Highway → S.V. Road → Dr. Annie Besant Road)|$BEEN/goud-argor-mumbai-weg-bom-zaveri.geojson" \
    --marker "au-ref-argor — Argor-Heraeus SA, Mendrisio (Ticino) — raffinaderij/laadplek, bron-gelegd|45.8749,8.9818" \
    --marker "au-air-mxp — Milano Malpensa Cargo, Cargo City Sud (MXP) — overslag truck → lucht, bron-gelegd|45.6142,8.7186" \
    --marker "au-air-bom — Mumbai Air Cargo Complex, Sahar (CSMIA/BOM) — overslag lucht → truck, bron-gelegd|19.0954,72.8660" \
    --marker "au-mkt-zaveri — Zaveri Bazaar-sieradenmarkt, Mumbai — groothandelsmarkt, stoppunt, aannemelijk|18.9518,72.8307" \
    --routebrief v2/design/routebrieven/goud-argor-mumbai.md \
    --uit    v2/data/stroomroute-goud-argor-mumbai.json \
    --stroom goud-argor-mumbai \
    --titel  "Goud · Argor-Heraeus (Mendrisio) → Malpensa (MXP) → Mumbai (BOM) → Zaveri Bazaar"
}

# ── goud · MKS PAMP (Castel San Pietro) → Zürich (ZRH) → vrachtvlucht → Shanghai Pudong (PVG) → SGE-kluiszone Lujiazui
# Routebrief: v2/design/routebrieven/goud-pamp-shanghai.md (lichte werkwijze M31 golf 3, §2 Lucht)
# ⚠️ CENTRAAL AFGEBAKKEN (2026-09-28): de bak-agent haalde alleen het luchtbeen en
#    de twee profielen binnen de sessie (wegscans op het gedeelde slot). Twee
#    profielcorrecties: (1) het wegbeen eindigt op de openbare weg bij het
#    vrachtplatform (airside, "geen wegpad" — zelfde bevinding als
#    goud-loulo-ticino/goud-yanacocha-ticino), afgesloten met een stippel van
#    0,91 km; (2) via-punt Zug verwijderd (lag in de stad, de A4 gaat door het
#    Knonaueramt) — 266,7 → 263,3 km. Tegen de ~200 km uit de brief is dat +32%:
#    de brief-km was hemelsbreed; Castel San Pietro → Zürich Airport over de
#    Gotthard is realistisch ~250 km. Bevinding, geen via-punt bijgeschoven.
# ⚠️ Het eindanker au-sge-kluiszone is een ZONE (Lujiazui/Yincheng-corridor):
#    het SGEI-kluispand wordt door geen bron met een adres genoemd → onzeker, en
#    dat staat in de markernaam.
bak_goud_pamp_shanghai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen MKS PAMP → Zürich Airport (A2 Gotthard → A14/A4 Knonaueramt → A1)|$BEEN/goud-pamp-shanghai-weg-pamp-zrh.geojson" \
    --stippel      "truck|ZRH-vrachtplatform last mile (schematisch — airside/privéterrein zonder aansluiting op het openbare net)|47.472087,8.554523|47.4647,8.5492" \
    --been-geojson "lucht|vlucht ZRH → PVG (vrachtvlucht, grootcirkel)|$BEEN/goud-pamp-shanghai-lucht-zrh-pvg.geojson" \
    --been-geojson "truck|vrachtwagen Shanghai Pudong vrachtterminal → SGE-kluiszone Lujiazui (aannemelijk: kluispand niet gepubliceerd)|$BEEN/goud-pamp-shanghai-weg-pvg-sge.geojson" \
    --marker "au-pamp-raffinaderij — MKS PAMP SA, Via alle Zocche 1, Castel San Pietro — raffinaderij/laadplek, bron-gelegd|45.8546,9.0025" \
    --marker "au-zrh-vrachtterminal — Zürich Airport vrachtplatform (hergebruikt anker) — overslag truck → lucht, bron-gelegd|47.4647,8.5492" \
    --marker "au-pvg-vrachtterminal — Shanghai Pudong vrachtplatform (hergebruikt anker) — overslag lucht → truck, bron-gelegd|31.1335,121.8025" \
    --marker "au-sge-kluiszone — Lujiazui/Yincheng-corridor, SGE International Board-kluiszone — stoppunt, onzeker (zone)|31.2355,121.5008" \
    --routebrief v2/design/routebrieven/goud-pamp-shanghai.md \
    --uit    v2/data/stroomroute-goud-pamp-shanghai.json \
    --stroom goud-pamp-shanghai \
    --titel  "Goud · MKS PAMP (Ticino) → Zürich (ZRH) → Shanghai Pudong (PVG) → SGE-kluiszone"
}

# ── gas · North Field (Qatar, offshore) → Ras Laffan LNG-laadkade → Gate terminal (Rotterdam, de Suez-as)
# Routebrief: v2/design/routebrieven/gas-raslaffan-rotterdam.md (lichte werkwijze M31 golf 4)
# Reserve-as naast gas-raslaffan-chiba (as 2, Japan) — b1 en b2a zijn LETTERLIJKE
# KOPIEËN van as 2, geen nieuwe geometrie gezocht/gebakken.
# ⚠️ b1 (leiding, STIPPEL) = letterlijk dezelfde --stippel-regel als
#    bak_gas_raslaffan_chiba (geen site-anker aan de kop: North Field is een
#    offshore veld van >6.000 km², brief §7 — gedeeld open punt met as 2).
# ⚠️ b2a (zee, haven-aanloop, STIPPEL-GEOJSON) = hergebruikt letterlijk het
#    bestaande geojson van as 2 (gas-raslaffan-chiba-aanloop-raslaffan.geojson,
#    41,6 km) — Ras Laffan-kade ligt 41,5 km van de MARNET-zeeknoop (LAR-586).
#    maak_havenaanloop.py NIET opnieuw gedraaid.
# ⚠️ b2b (zee, MARNET, hoofdbeen) is het ENIGE nieuwe been van deze as: kade
#    → kade tussen dezelfde zeeknoop als as 2 en de Gate-kade Rotterdam.
#    MARNET routeert zelf kortste-pad (verwacht via Hormuz/Suez); geen
#    Kaap-omweg geforceerd — de Rode-Zee-crisis-risicotekst in de brief (§7)
#    is documentair, geen routeer-instructie. Gate-kade ligt 1,836 km van een
#    zeeknoop (gemeten in as 1, gas-sabinepass-rotterdam) — ruim binnen de
#    5 km-norm, geen tweede haven-aanloop nodig. km-toets zacht: brief geeft
#    alleen een ~11.000–12.000 km ontwerp-indicatie, geen gepubliceerde
#    ladingroute-lengte.
# ⚠️ Fase C (Gate-regas → GTS-net) vervalt, conform as 1 (gas-sabinepass-
#    rotterdam §2) — geen OSM-pijpleiding-way, geen tweede coördinaat gebrond.
#    Geen fase D/E (brief §6): geen bron koppelt één specifieke Ras Laffan-
#    lading aan Rotterdam.
bak_gas_raslaffan_rotterdam() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "leiding|offshore verzamelleiding North Field → Ras Laffan-kade (schematisch — subsea, niet gekarteerd; gedeeld been met gas-raslaffan-chiba)|26.6191,51.9500|25.9265,51.5955" \
    --stippel-geojson "zee|haven-aanloop Ras Laffan (schematisch, over water — kade 41,5 km van de MARNET-zeeknoop; gedeeld been met gas-raslaffan-chiba)|$BEEN/gas-raslaffan-chiba-aanloop-raslaffan.geojson" \
    --been         "zee|LNG-tanker Ras Laffan → Rotterdam Gate (Perzische Golf → Straat van Hormuz → Arabische Zee → Bab-el-Mandeb → Rode Zee → Suezkanaal → Middellandse Zee → Straat van Gibraltar → Atlantische kust/Noordzee)|26.30000,51.60000|51.97110,4.06890" \
    --marker "gas-raslaffan-kade — Ras Laffan LNG-laadsteiger (QatarEnergy LNG-complex), overslag leiding → zee, bron-gelegd (hergebruikt anker)|25.9265,51.5955" \
    --marker "gas-gate-kade — Gate terminal (Vopak/Gasunie), Maasvlakte Rotterdam, losplek/LNG-importterminal, stoppunt, aannemelijk (hergebruikt anker)|51.97110,4.06890" \
    --routebrief v2/design/routebrieven/gas-raslaffan-rotterdam.md \
    --uit    v2/data/stroomroute-gas-raslaffan-rotterdam.json \
    --stroom gas-raslaffan-rotterdam \
    --titel  "Gas · Ras Laffan (Qatar) → Rotterdam (Nederland)"
}

# ── kolen · North Antelope Rochelle Mine (Wyoming) → Westshore Terminals (Roberts Bank, BC) — PRB-kolen naar de enige westkust-exportkade
# Routebrief: v2/design/routebrieven/kolen-gillette-robertsbank.md (lichte werkwijze M31 golf 4, reserve-as)
# ⚠️ Eén been (spoor, BNSF Wyoming/Montana → grensovergang aannemelijk → CP/CN
#    Robert's Bank Rail Corridor): geen gepubliceerde bron voor de exacte
#    BNSF↔CP/CN-overdrachtsplaats in Montana, dus geen via-punt verzonnen — de
#    1-op-1-router zoekt zelf de kortste weg. Gemeten 2.333,3 km tegen de
#    brief-schatting ~2.200–2.500 km (geen gepubliceerde spoorlengte bestaat;
#    hemelsbreed 1.497,2 km) — binnen de schatting; de ±15%-toets geldt hier
#    als indicatie, niet als norm (brief §2).
# ⚠️ Kop-stippel: het laadspoor bij North Antelope Rochelle Mine snapt 6,27 km
#    van het 1-op-1-hoofdnet (mijn-eigen railaansluiting niet in OSM
#    gekarteerd) — korte stippel met reden, geen doorgetrokken lijn de
#    dagbouwput in.
# ⚠️ Staart bij Westshore Terminals snapt 0,23 km — normale meting, geen
#    stippel nodig.
# ⚠️ Geen zeebeen, geen haven-aanloop: de keten stopt bij de Westshore-kade
#    (brief §6) — geen bron noemt een Aziatische eindkoper per lading.
bak_kolen_gillette_robertsbank() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "spoor|North Antelope Rochelle Mine — laadspoor/mijnaansluiting (geen net op deze korrel)|43.5589,-105.2883|43.5057,-105.2627" \
    --been-geojson "spoor|trein North Antelope Rochelle Mine → Westshore Terminals (BNSF Wyoming/Montana → grensovergang, aannemelijk: één bron → CP/CN Robert's Bank Rail Corridor)|$BEEN/spoorroute-kolen-gillette-robertsbank-narm-westshore.geojson" \
    --marker "coal-gillette-narm-laad — North Antelope Rochelle Mine (Peabody Energy), Campbell County, Wyoming — mijn/laadspoor, bron-gelegd|43.5589,-105.2883" \
    --marker "coal-gillette-westshore-kade — Westshore Terminals Coal Port, Roberts Bank, Delta, British Columbia — overslag spoor → zeeschip, bron-gelegd|49.0184,-123.1661" \
    --routebrief v2/design/routebrieven/kolen-gillette-robertsbank.md \
    --uit    v2/data/stroomroute-kolen-gillette-robertsbank.json \
    --stroom kolen-gillette-robertsbank \
    --titel  "Kolen · North Antelope Rochelle Mine (Wyoming) → Westshore Terminals, Roberts Bank (Canada)"
}

# ── koper · Bingham Canyon Mine → Copperton-concentrator → Garfield-smelter/raffinaderij (VS, binnenlandse mijn-tot-kathode-lus)
# Routebrief: v2/design/routebrieven/koper-binghamcanyon-garfield.md (lichte werkwijze, M31 golf 4)
# ⚠️ Eén been (fase A, leiding), volledig gestippeld: transportband
#    Bingham Canyon Mine → Copperton-concentrator + 17-mijl (~27 km)
#    Kennecott-slurrypijpleiding Copperton → Garfield-smelter. Particuliere
#    mijninfrastructuur op eigen terrein (Rio Tinto/Kennecott), geen publieke
#    weg/spoor/leiding-kartering die het tracé doorlopend draagt (routebrief §7).
# ⚠️ Geen zee (volledig binnenlandse VS-keten), geen via-punten (geen
#    corridorkeuze op privéterrein), geen haven-aanloop, geen fase D/E (§6:
#    stoppunt bij de kathode, bewust een gesloten mijn-tot-raffinaderij-lus
#    zonder gedocumenteerde afnemersfabriek).
bak_koper_binghamcanyon_garfield() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel "leiding|Kennecott slurry-pijpleiding + transportband Bingham Canyon Mine → Copperton-concentrator → Garfield-smelter (schematisch — particuliere mijninfrastructuur, geen doorlopend publiek net; gepubliceerd 17 mijl/~27 km leidingdeel Copperton→Garfield, mijn→Copperton per transportband, lengte niet gevonden)|40.5230,-112.1510|40.7231,-112.2000" \
    --marker "cu-bingham-mijn — Bingham Canyon Mine (Rio Tinto/Kennecott Utah Copper)|40.5230,-112.1510" \
    --marker "cu-garfield-smelter — Kennecott Garfield-smelter/raffinaderij (Magna, UT)|40.7231,-112.2000" \
    --routebrief v2/design/routebrieven/koper-binghamcanyon-garfield.md \
    --uit    v2/data/stroomroute-koper-binghamcanyon-garfield.json \
    --stroom koper-binghamcanyon-garfield \
    --titel  "Koper: Bingham Canyon -> Garfield (VS)"
}

# ── diamant · Gahcho Kué Aerodrome (NWT, Canada) → Yellowknife (YZF) → Gaborone (GBE) → DTCB/DBGSS-campus
# Routebrief: v2/design/routebrieven/diamant-gahchokue-gaborone.md (LICHTE werkwijze M31 golf 4)
# Drie benen, alle DOORGETROKKEN — geen zeebeen, dus geen haven-aanloop.
# ⚠️ b1 (lucht, maak_luchtbeen.py) Gahcho Kué Aerodrome → YZF: 287,7 km grootcirkel,
#    tegen Wikipedia "approximately 280 km" [brief §2/§8[3]] — geen km-toets voor een
#    luchtbeen (bakhandleiding §5).
# ⚠️ b2 (lucht) YZF → GBE: 14.878,7 km grootcirkel — ZEER LANG, ver voorbij het
#    realistische bereik van een vrachtvliegtuig zonder tussenstop (747-8F/777F ≈
#    9.000-9.200 km). Geen bron noemt een specifieke tussenlandingshub → ÉÉN DIRECTE
#    VLUCHT aangenomen conform bakhandleiding §2 ("Lucht"), die aanname is expliciet
#    gedocumenteerd in de brief §7. dia-yzf-splitsing is een HERGEBRUIKT anker (uit
#    diamant-ekati-antwerpen.md, deze golf al satelliet-gelegd); dia-gbe-cargo en
#    dia-gaborone-dtc zijn hergebruikte ankers uit diamant-gaborone-surat.md.
# ⚠️ b3 (truck, fase C — NIEUW t.o.v. het oorspronkelijke ontwerp, per de bindende
#    aanpassing van de haalbaarheidstoets) is een LETTERLIJKE KOPIE, OMGEKEERDE
#    RICHTING, van diamant-gaborone-surat-weg-dtc-gbe.geojson (stroom
#    diamant-gaborone-surat, been b1, functie bak_diamant_gaborone_surat) — geen
#    nieuwe wegscan/profiel, puntenvolgorde omgedraaid
#    (diamant-gahchokue-gaborone-truck-gbe-dtc.geojson). 4,253 km (kmWeg 4,1 km) tegen
#    3,7 km hemelsbreed gemeten voor dít ankerpaar — geen nieuwe km-toets nodig, het
#    origineel is al getoetst in zijn eigen brief. Geen via-punten, geen stippel
#    (zelfde stadsweg zonder corridorkeuze als het origineel).
# ⚠️ Geen fase D/E (brief §6): de brief stopt bewust bij de DTCB/DBGSS-campus, want de
#    aansluiting Gaborone → Surat-slijperij is al getekend in stroom
#    diamant-gaborone-surat (dubbeling vermeden).
bak_diamant_gahchokue_gaborone() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "lucht|vlucht Gahcho Kue Aerodrome → YZF (vrachtvlucht, grootcirkel)|$BEEN/diamant-gahchokue-gaborone-lucht-gahchokue-yzf.geojson" \
    --been-geojson "lucht|vlucht YZF → GBE (vrachtvlucht, grootcirkel, zeer lang, geen tussenlanding gebrond, §7)|$BEEN/diamant-gahchokue-gaborone-lucht-yzf-gbe.geojson" \
    --been-geojson "truck|GBE-vrachtapron → DTCB/DBGSS-campus (A1/Western Bypass, letterlijke kopie omgekeerd van diamant-gaborone-surat b1)|$BEEN/diamant-gahchokue-gaborone-truck-gbe-dtc.geojson" \
    --marker "dia-gahchokue-strip — Gahcho Kue Aerodrome (grind-/ijsbaan naast het mijncomplex, Kennady Lake) — mijnvliegveld, vertrekpunt lucht, bron-gelegd|63.43534,-109.14478" \
    --marker "dia-yzf-splitsing — GA-vrachtplatform oostzijde Yellowknife Airport — overslag lucht→lucht, hergebruikt anker, bron-gelegd|62.46850,-114.42500" \
    --marker "dia-gbe-cargo — GBE-vrachtapron, Sir Seretse Khama Intl Airport — vrachtterminal, aankomst lucht/vertrek truck, hergebruikt anker, bron-gelegd|-24.55500,25.92860" \
    --marker "dia-gaborone-dtc — DTCB/DBGSS-campus, Gaborone — handels-/aggregatiehub, stoppunt, hergebruikt anker, bron-gelegd|-24.58590,25.91440" \
    --routebrief v2/design/routebrieven/diamant-gahchokue-gaborone.md \
    --uit    v2/data/stroomroute-diamant-gahchokue-gaborone.json \
    --stroom diamant-gahchokue-gaborone \
    --titel  "Diamant · Gahcho Kué (NWT, Canada) → Yellowknife (YZF) → Gaborone (GBE) → DTCB/DBGSS"
}

# ── goud · Metalor-raffinaderij (Marin-Epagnier) → Zürich Airport (ZRH) → Istanbul Airport (IST) → Kuyumcukent (Yenibosna)
# Routebrief: v2/design/routebrieven/goud-metalor-istanbul.md (LICHTE werkwijze M31 golf 4, reserve-as uit golf 3, nu geactiveerd)
# Drie benen, alle FASE D en alle DOORGETROKKEN — geen enkel been is een stippel
# (behalve de korte ZRH-airside-last-mile, zoals goud-loulo-ticino / goud-pamp-shanghai).
# ⚠️ b1 (truck, profiel goud-metalor-istanbul-marin-zrh) Metalor → Biel/Bienne →
#    Solothurn → ZRH-vrachtplatform-openbare-wegpunt: 152,6 km. ⚠️ Centraal
#    gecorrigeerd (2026-09-28): het via-punt Bern dwong een omweg af (195,2 km,
#    1,53× hemelsbreed); verwijderd, zie §9 van de brief. Het ZRH-platform zelf (47.4647,8.5492) is
#    airside/privéterrein zonder aansluiting op het openbare net (hergebruikt
#    anker uit pgm-springs-zurich.md) — het wegbeen eindigt op het bekende
#    openbare-wegpunt 47.472087,8.554523 en een korte --stippel sluit de
#    airside-laatste-honderden-meters af, letterlijk hetzelfde patroon en
#    dezelfde coördinaten als goud-loulo-ticino / goud-pamp-shanghai
#    (bakhandleiding §2 Lucht).
# ⚠️ b2 (lucht, maak_luchtbeen.py) vlucht ZRH → IST: 1.738,9 km grootcirkel,
#    tegen de brief-schatting ≈1.739 km hemelsbreed (brief §2/§8) — geen
#    km-toets voor een luchtbeen (handleiding §5). Doorgetrokken, geen
#    stippel: een vlucht tussen twee gelegde vrachtterminals is geen gat.
#    Aannemelijk: industriestandaard voor edelmetaal, geen bron bevestigt
#    déze specifieke lading of een tussenlanding (brief §7).
# ⚠️ b3 (truck, profiel goud-metalor-istanbul-ist-kuyumcukent) IST-vrachtterminal
#    → Kuyumcukent: 37,1 km tegen ontwerp ≈30 km (+23,6%, BUITEN ±15% —
#    bevinding, niet dichtgetrokken; geen gepubliceerde wegbeheerder-lengte,
#    alleen een ontwerpschatting, brief §2). Het IST-vrachtterminalanker bleek
#    NIET airside-geïsoleerd (anders dan de brief als terugval voorzag,
#    §"bak_aanwijzingen"): de wegscan snapte direct (0,03 km) zonder
#    "geen wegpad" — geen stippel nodig, geen zelf toegevoegde via-punten.
# ⚠️ Geen haven-aanloop (geen zeebeen), geen gedeeld been (alle drie ankers
#    zijn óf nieuw satelliet-gelegd óf letterlijk hergebruikt van
#    pgm-springs-zurich.md, zonder eigen geometrie).
bak_goud_metalor_istanbul() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Metalor Marin-Epagnier → Biel/Bienne → Solothurn → Zürich Airport-vrachtplatform (A5 → A1)|$BEEN/goud-metalor-istanbul-weg-marin-zrh.geojson" \
    --stippel      "truck|ZRH-vrachtplatform last mile (schematisch — airside/privéterrein zonder aansluiting op het openbare net)|47.472087,8.554523|47.4647,8.5492" \
    --been-geojson "lucht|vlucht ZRH → IST (vrachtvlucht, grootcirkel, aannemelijk: industriestandaard, geen bron voor déze specifieke lading)|$BEEN/goud-metalor-istanbul-lucht-zrh-ist.geojson" \
    --been-geojson "truck|vrachtwagen Istanbul Airport (IST) vrachtterminal → Kuyumcukent-complex, Yenibosna (TEM-otoyolu/Basın Ekspress Yolu)|$BEEN/goud-metalor-istanbul-weg-ist-kuyumcukent.geojson" \
    --marker "au-ref-metalor — Metalor SA, Marin-Epagnier (Neuchâtel) — raffinaderij/laadplek, bron-gelegd|47.0107,7.0112" \
    --marker "au-zrh-vrachtterminal — Zürich Airport vrachtplatform (hergebruikt anker uit pgm-springs-zurich.md) — overslag truck → lucht, bron-gelegd|47.4647,8.5492" \
    --marker "au-ist-vrachtterminal — Istanbul Airport (iGA) vrachtterminal, Tayakadın/Arnavutköy — overslag lucht → truck, bron-gelegd|41.25528,28.71278" \
    --marker "au-kuyumcukent — Kuyumcukent-goud-/sieradencomplex, Yenibosna — losplek/markt, stoppunt, bron-gelegd|41.0035,28.8148" \
    --routebrief v2/design/routebrieven/goud-metalor-istanbul.md \
    --uit    v2/data/stroomroute-goud-metalor-istanbul.json \
    --stroom goud-metalor-istanbul \
    --titel  "Goud · Metalor (Marin-Epagnier) → Zürich (ZRH) → Istanbul (IST) → Kuyumcukent (Yenibosna)"
}

# ── goud · Ity-mijn (Endeavour Mining, Ivoorkust) → Abidjan (ABJ) → Zürich (ZRH) → Valcambi (Balerna, Ticino)
# Routebrief: v2/design/routebrieven/goud-ity-ticino.md (LICHTE werkwijze M31 golf 4, reserve-as)
# ⚠️ b1 (truck, profiel goud-ity-ticino-ity-abidjan, extract ivoorkust): Ity-mijn →
#    Zouan-Hounien → Man → Daloa → Yamoussoukro → Abidjan (ABJ) vrachtterminal.
#    695,0 km tegen de venster-referentie ~600 km (+15,8%) — GEEN harde ±15%-toets:
#    de brief geeft geen gepubliceerde wegkm, alleen een ontwerp-schatting/hemelsbreed-
#    som (routebrief §2/§7); de via-punten zijn indicatieve corridorsteden, niet zelf
#    OSM-wegvertex-geverifieerd, dus de router bepaalt de exacte ligging. Bevinding,
#    geen via-punt bijgeschoven.
# ⚠️ b2 (lucht, maak_luchtbeen.py): grootcirkel ABJ → ZRH, 4.841,6 km — komt vrijwel
#    exact overeen met de brief (≈4.840 km berekend). Doorgetrokken, geen stippel:
#    een vlucht tussen twee gelegde vrachtterminals is geen gat (bakhandleiding §2
#    Lucht). Aannemelijk, niet chain-specifiek bevestigd (routebrief §7): West-
#    Afrikaanse doré-export naar Zwitserse raffinaderijen is industriestandaard
#    (zelfde redenering als goud-loulo-ticino.md) en Abidjan heeft bevestigde directe
#    luchtvrachtverbindingen richting Zürich. Geen tussenlanding gebrond → één
#    directe vlucht.
# ⚠️ b3-stippel + b3 (truck, ZRH-vrachtplatform → Valcambi) zijn een LETTERLIJKE KOPIE
#    van het bestaande been in goud-loulo-ticino (identieke ankers 47,4647/8,5492 →
#    45,8385/9,0051, identieke A2/Gotthard-corridor via Bellinzona–Lugano–Chiasso):
#    het geojson is 1-op-1 gekopieerd naar goud-ity-ticino-weg-zrh-valcambi.geojson
#    (géén tweede scan gedraaid, bakhandleiding "gedeeld been = letterlijke kopie");
#    de airside-last-mile-stippel (ZRH-platform → openbare-wegpunt, 0,914 km) is
#    dezelfde geometrie als in bak_goud_loulo_ticino().
# ⚠️ au-zrh-vrachtterminal en au-ref-valcambi zijn HERGEBRUIKTE ankers uit
#    goud-loulo-ticino.md/goud-pamp-shanghai.md (geen nieuwe satellietpas nodig).
# ⚠️ Geen haven-aanloop (geen zeebeen), geen spoornet, geen fase D/E (routebrief §6:
#    Valcambi levert aan een brede, niet-herleidbare afname — stoppunt).
bak_goud_ity_ticino() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Ity-mijn → Abidjan (ABJ) vrachtterminal (Zouan-Hounien–Man–Daloa–Yamoussoukro)|$BEEN/goud-ity-ticino-weg-ity-abidjan.geojson" \
    --been-geojson "lucht|vlucht ABJ → ZRH (vrachtvlucht, grootcirkel, aannemelijk: industriestandaard, zie goud-loulo-ticino.md)|$BEEN/goud-ity-ticino-lucht-abj-zrh.geojson" \
    --stippel      "truck|ZRH-vrachtplatform last mile (schematisch — airside/privéterrein, identiek aan goud-loulo-ticino)|47.4647,8.5492|47.472087,8.554523" \
    --been-geojson "truck|vrachtwagen Zürich Airport vrachtplatform → Valcambi-raffinaderij, Balerna (A2/Gotthard-as via Bellinzona–Lugano–Chiasso, letterlijke kopie van goud-loulo-ticino)|$BEEN/goud-ity-ticino-weg-zrh-valcambi.geojson" \
    --marker "au-ity-mijn — Ity-mijn, verwerkingsinstallatie (Endeavour Mining, Zouan-Hounien Department, Tonkpi) — mijn/laadplek, bron-gelegd|6.8830,-8.1195" \
    --marker "au-abidjan-vrachtterminal — Abidjan Félix-Houphouët-Boigny Int'l (ABJ), cargo-apron W van de startbaan — overslag truck → lucht, bron-gelegd (pand onzeker)|5.2628,-3.9298" \
    --marker "au-zrh-vrachtterminal — Zürich Airport vrachtplatform (hergebruikt anker uit goud-loulo-ticino.md) — overslag lucht → truck, bron-gelegd|47.4647,8.5492" \
    --marker "au-ref-valcambi — Valcambi SA, Via Passeggiata 3, Balerna (hergebruikt anker) — raffinaderij, stoppunt, bron-gelegd|45.8385,9.0051" \
    --routebrief v2/design/routebrieven/goud-ity-ticino.md \
    --uit    v2/data/stroomroute-goud-ity-ticino.json \
    --stroom goud-ity-ticino \
    --titel  "Goud · Ity-mijn (Ivoorkust) → Abidjan (ABJ) → Zürich (ZRH) → Valcambi (Balerna, Ticino)"
}

# ── olie · Westridge Marine Terminal (Trans Mountain, Canada) → Ulsan-raffinagecomplex (SK Energy, Zuid-Korea)
# Routebrief: v2/design/routebrieven/olie-westridge-ulsan.md (lichte werkwijze, M31 golf 4, reserve-as)
# ⚠️ Eén been (b1, zee, MARNET kade → kade): Canadese oliezandcrude (Cold Lake-type) van de
#    TMX-zeeterminus in Burnaby BC naar het SK Energy Ulsan-complex, Straat van Georgia/Juan de
#    Fuca → Noord-Pacific grote cirkel — bestemming "aannemelijk: één bron" (brief §7: de zwakste
#    van de zes olie-assen uit golf 2 — SK Energy's 550.000-vatencargo (sept 2024, via Unipec) is
#    de enige directe koppeling, maar geen bron bevestigt Ulsan als losplek t.o.v. het sterker
#    onderbouwde alternatief Yeosu/GS Caltex; olie-westridge-yeosu is kandidaat voor een latere as).
# ⚠️ Westridge snapt 1,43 km op zeeknoop 7820 — ruim onder de 5 km-norm, geen haven-aanloop nodig.
# ⚠️ Haven-aanloop Ulsan (LAR-586, 2026-09-28): de kade snapt op 5,38 km van zeeknoop 5629 — boven
#    de 5 km-grens ondanks ruim binnen de 25 km-snapgrens, dus VERPLICHT. maak_havenaanloop.py
#    liep op `timeout 300` vast (exit 124, zelfde uitkomst als bij Onsan/Manzanillo) → rechte
#    stippel, geen tweede poging, zoals de bak-aanwijzing voorschrijft.
bak_olie_westridge_ulsan() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been         "zee|zeeschip Westridge Marine Terminal → Ulsan-raffinagecomplex (SK Energy) (aannemelijk: één bron)|49.2932,-122.9560|35.43317,129.3429" \
    --stippel      "zee|haven-aanloop Ulsan (schematisch — 1:10M-kust kent de kade niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|35.46180,129.39080|35.43317,129.3429" \
    --marker "ol-westridge-term — Westridge Marine Terminal (Trans Mountain Corporation), Burrard Inlet, Burnaby BC — laadplek/exportterminal, bron-gelegd|49.2932,-122.9560" \
    --marker "ol-ulsan-sk — SK Energy Ulsan-raffinagecomplex (Ulsan Complex) — losplek/raffinaderij, stoppunt, bron-gelegd (bestemming aannemelijk: één bron)|35.43317,129.3429" \
    --routebrief v2/design/routebrieven/olie-westridge-ulsan.md \
    --uit    v2/data/stroomroute-olie-westridge-ulsan.json \
    --stroom olie-westridge-ulsan \
    --titel  "Olie · Westridge Marine Terminal (Canada) → Ulsan (Zuid-Korea)"
}

# ── gas · Yamal LNG-complex Sabetta (Rusland) → Fluxys LNG-terminal Zeebrugge (België)
# Routebrief: v2/design/routebrieven/gas-sabetta-zeebrugge.md (lichte werkwijze M31 golf 4)
# ⚠️ b1a (zee, haven-aanloop Sabetta, NIEUW): anders dan de vergelijkbare
#    Bonny/Zeebrugge-aanlopen in gas-bonny-zeebrugge (beide exit 124) SLAAGDE
#    maak_havenaanloop.py hier wél (cel 0,005° kaal, minste land midden op de
#    lijn) → 17,7 km over water, 63 punten, 2,43 km over land uitsluitend aan
#    het kade-uiteinde (0,00 km MIDDEN op de lijn = de 1:10M-kustkorrel, geen
#    landkruising) → --stippel-geojson i.p.v. een rechte stippel. Kade 14,4 km
#    hemelsbreed van zeeknoop 4711.
# ⚠️ b1 (zee, MARNET, kade→kade wordt knoop→knoop): zeeknoop 4711
#    (71,34710/72,40350) → zeeknoop 1629 (51,50000/3,40000, identiek aan de
#    knoop die gas-bonny-zeebrugge al gebruikt voor Zeebrugge) — Karische Zee
#    → Barentszzee-kust (69-73°N) → Noorse kust zuidwaarts (66°N→54°N) →
#    Noordzee, lokaal vooraf getest op ~4.844,9 km / 503 punten (0/54 edges
#    afgekeurd wegens landkruising); zie §9 voor de echte bake-uitkomst.
# ⚠️ b1b (zee, haven-aanloop Zeebrugge): óók geslaagd (cel 0,01° kaal) →
#    21,4 km over water, 19 punten, 0,00 km over land — geen enkele
#    landkruising → --stippel-geojson. Kade 20,5 km hemelsbreed van
#    zeeknoop 1629 (identiek grensgeval aan gas-bonny-zeebrugge b1b, die daar
#    wél op timeout vastliep; hier niet).
# ⚠️ b2 (leiding, Zeebrugge-terrein, stippel, LETTERLIJKE KOPIE uit
#    gas-bonny-zeebrugge b2): 4,98 km — het OSM-pijpleidingnet is daar al
#    getoetst (topologische component-analyse: LNG-terminal en IUK-poort op
#    twee NIET-verbonden componenten); hier niet opnieuw gecheckt.
# ⚠️ Fase A vervalt: geen coördinaat voor het South Tambey-gasveld — verspreide
#    putlocaties, geen enkelvoudig traceerbaar tracé (brief §7). Geen fase
#    D/E: geen enkelvoudige fabriek/afnemer, het gas verdwijnt in het
#    Belgisch/NW-Europese net of gaat als transshipment verder (brief §6).
bak_gas_sabetta_zeebrugge() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel-geojson "zee|haven-aanloop Sabetta (schematisch, over water — kade 14,4 km van de MARNET-zeeknoop 4711)|$BEEN/gas-sabetta-zeebrugge-aanloop-sabetta.geojson" \
    --been         "zee|LNG-tanker Sabetta → Zeebrugge (Karische Zee → Barentszzee-kust (69-73°N) → Noorse kust zuidwaarts (66°N→54°N) → Noordzee — westelijke, niet-Arctische route)|71.34710,72.40350|51.50000,3.40000" \
    --stippel-geojson "zee|haven-aanloop Zeebrugge (schematisch, over water — kade 20,5 km van de MARNET-zeeknoop 1629)|$BEEN/gas-sabetta-zeebrugge-aanloop-zeebrugge.geojson" \
    --stippel      "leiding|korte terreinleiding Zeebrugge naar het net (schematisch — geen bevestigde OSM-way; twee losse pijpleidingcomponenten in de belgie-extract, niet verbonden — letterlijke kopie uit gas-bonny-zeebrugge b2)|51.3537,3.2200|51.3156,3.1822" \
    --marker "gas-sabetta-lng — Yamal LNG, Sabetta (Novatek) — productie + laadkade (LNG-complex), bron-gelegd|71.2733,72.0725" \
    --marker "gas-zeebrugge-lng — Fluxys LNG Zeebrugge — losplek + regasterminal + transshipment-hub, bron-gelegd (anker letterlijk hergebruikt uit gas-bonny-zeebrugge)|51.3537,3.2200" \
    --marker "gas-zeebrugge-iuk — UK Gas Interconnector Terminal-terrein (Fluxys-gaszone), Zeebrugge — netinvoedingspunt, stoppunt, aannemelijk (anker letterlijk hergebruikt uit gas-bonny-zeebrugge)|51.3156,3.1822" \
    --routebrief v2/design/routebrieven/gas-sabetta-zeebrugge.md \
    --uit    v2/data/stroomroute-gas-sabetta-zeebrugge.json \
    --stroom gas-sabetta-zeebrugge \
    --titel  "Gas · Sabetta (Rusland) → Zeebrugge (België)"
}

# ── koper · Antamina-mijn (Peru) → Huarmey/Punta Lobitos → Yangtze → Huangshi (China, reserve-as)
# Routebrief: v2/design/routebrieven/koper-antamina-daye.md (lichte werkwijze, M31 golf 4)
# ⚠️ b1 leiding = STIPPEL: Antamina-concentraatpijpleiding (~302 km, hooglandtracé Ancash-kust,
#    bedrijfscijfer). Vóór het bakken nagegaan (pyosmium, peru-extract, bbox Antamina-Huarmey):
#    geen enkele man_made=pipeline-way met substance=slurry op dit tracé — bevestigt de eerdere
#    Nominatim-toets uit de brief, dus bindend gestippeld.
# ⚠️ b2a haven-aanloop Huarmey → zeeknoop 166 (-10.0000,-80.0000): gemeten 199,7 km recht,
#    maak_havenaanloop.py (timeout 300, GESLAAGD, geen fallback nodig) → 202,1 km / 183 punten,
#    0,41 km over land grenst aan het kade-uiteinde zelf (korrel van de 1:10M-kustlijn, geen fout).
#    Blijft stippel-geojson: kortste pad over water, geen waargenomen vaargeul.
# ⚠️ b3 binnenvaart Yangtze-monding → Tongling-kade = GEDEELD been, LETTERLIJKE KOPIE (zelfde
#    geojson-bestand als koper-lasbambas-matarani/koper-chuquicamata-china, niet opnieuw gebakken):
#    $BEEN/rivierbeen-yangtze-tongling-gedeeld.geojson, 516,6 km.
# ⚠️ b4 binnenvaart Tongling → Huangshi = NIEUW, MARNET-bulklaag (Yangtze heeft geen AIS-dekking
#    boven Tongling): maak_rivierbeen.py → 401,0 km / 48 edges / 2.082 punten (schatting in de
#    brief ~390 km o.b.v. omwegfactor — binnen de indicatieve marge, geen gepubliceerde rivier-km).
#    Het "naar"-uiteinde snapt op 3,19 km van het brief-anker cu-huangshi-kade (bulk-knoop 21597) —
#    geen precieze routeerknoop op die stedelijke oever; PROCESGAT, niet het punt verschoven.
# ⚠️ cu-huangshi-kade blijft ONZEKER (algemene havenzone Huangshi, geen bedrijfskade van Daye
#    Nonferrous Metals gevonden binnen het webbudget) — de brief stopt hier bewust (§6): geen bron
#    noemt Daye als naam-afnemer van déze lading.
bak_koper_antamina_daye() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel        "leiding|Antamina-concentraatpijpleiding (schematisch — geen OSM-way verwacht op dit Andes-tracé, geverifieerd: pyosmium peru-extract geen substance=slurry-way)|-9.5372,-77.0611|-10.1035,-78.1788" \
    --stippel-geojson "zee|haven-aanloop Huarmey (schematisch, over water — MARNET reikt niet tot de kade: 199,7 km tot zeeknoop 166)|$BEEN/koper-antamina-daye-aanloop-huarmey.geojson" \
    --been           "zee|zeeschip Huarmey → Yangtze-monding|-10.0000,-80.0000|31.42704,121.47618" \
    --been-geojson   "binnenvaart|Yangtze-monding → Tongling-kade (Yangtze, oostgeul — gedeeld been met koper-collahuasi-tongling/lasbambas/chuqui)|$BEEN/rivierbeen-yangtze-tongling-gedeeld.geojson" \
    --been-geojson   "binnenvaart|Tongling → Huangshi (Yangtze, stroomopwaarts, MARNET-bulklaag)|$BEEN/koper-antamina-daye-rivier-tongling-huangshi.geojson" \
    --marker "cu-antamina-laad — Antamina-mijn (open pit + concentrator), Ancash, Peru (BHP/Glencore/Teck/Mitsubishi) — mijn/laadplek, bron-gelegd|-9.5372,-77.0611" \
    --marker "cu-antamina-huarmey-kade — Puerto Punta Lobitos – Antamina, Huarmey, Peru — overslag (laadkade), bron-gelegd|-10.1035,-78.1788" \
    --marker "cu-huangshi-kade — Yangtze-oeverfront Huangshi, Hubei (havenzone bij Daye Nonferrous Metals) — losplek, stoppunt, ONZEKER (algemene havenzone, geen bedrijfskade)|30.2100,115.0750" \
    --routebrief v2/design/routebrieven/koper-antamina-daye.md \
    --uit    v2/data/stroomroute-koper-antamina-daye.json \
    --stroom koper-antamina-daye \
    --titel  "Koper · Antamina (Peru) → Huarmey → Yangtze → Huangshi (China)"
}

# ── pgm · Amandelbult-mijn (Noord-Bushveld, Zuid-Afrika) → Rustenburg PMR → OR Tambo (JNB) → (vlucht) → JFK (New York) → Metivo/BASF ECMS, Iselin NJ
# Routebrief: v2/design/routebrieven/pgm-amandelbult-iselin.md (lichte werkwijze, M31 golf 4)
# Vier benen; geen zeebeen/haven-aanloop in deze keten; geen ongebronde stippels.
# ⚠️ b1 (truck, NIET stippel): Amandelbult → Rustenburg PMR over de R510 via
#    Northam. Geen gepubliceerde wegkm gevonden (brief §7) → getoetst tegen de
#    hemelsbrede afstand (96,6 km) als indicatie, niet als norm. Gebakken
#    111,4 km (+15,3% t.o.v. de hemelsbrede indicatie) — bevinding, geen fout
#    (de R510 maakt een reële bocht om Northam/Thabazimbi-omgeving heen).
#    Anker-verbinding plant→weg 1,46 km [⚠️ >0,5 km, bevinding: Amandelbult is
#    een uitgestrekt mijnterrein, het OSM-wegnet raakt het terrein niet exact].
# ⚠️ b2 (truck, NIET stippel) is een LETTERLIJKE KOPIE van pgm-rustenburg-
#    shanghai been b1 (Rustenburg PMR → OR Tambo (JNB), N4/N1/R21, 178,0 km) —
#    hergebruikt geojson, niet opnieuw gebakken (werkwijze-regel routebrief §7).
#    Via-punten identiek: Brits · Pretoria (N4/N1-knoop) · Midrand · Kempton Park.
# ⚠️ b3 (lucht, maak_luchtbeen.py): vlucht JNB → JFK, grootcirkel, 12.831,5 km —
#    DOORGETROKKEN, geen stippel (bakhandleiding §2). Niet apart gebrond voor
#    déze as; aangenomen als industriestandaard (PGM als beveiligde luchtvracht),
#    zelfde aanname als de andere golf-3-PGM-luchtbenen (brief §7). Geen
#    tussenlanding aangenomen.
# ⚠️ b4 (truck, NIET stippel): JFK South Cargo Area → Metivo/BASF ECMS, Iselin
#    NJ. Brief noemde alleen het extract us-new-jersey als aanwezig, maar het
#    JFK-anker ligt in Queens (New York) — zonder het extract us-new-york snapte
#    de "plant"-kant 19,31 km weg (JFK niet gedekt door us-new-jersey alleen).
#    Extract us-new-york toegevoegd (al aanwezig op schijf, geen download) →
#    snap 0,01/0,03 km, beide OK. Gebakken 55,5 km tegen de routeplanner-
#    schatting ~69 km (Travelmath, geen officiële opgave) = −19,5%, bevinding,
#    geen fout — de bake-uitvoer is hier de echte controle (brief §7).
bak_pgm_amandelbult_iselin() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Amandelbult-mijn → Rustenburg PMR (R510 via Northam)|$BEEN/pgm-amandelbult-iselin-weg-amandelbult-rustenburg.geojson" \
    --been-geojson "truck|Rustenburg PMR → OR Tambo (JNB) vrachtterminal, letterlijke kopie pgm-rustenburg-shanghai b1 (N4/N1/R21)|$BEEN/pgm-rustenburg-shanghai-weg-rustenburg-jnb.geojson" \
    --been-geojson "lucht|vlucht JNB → JFK (vrachtvlucht, grootcirkel)|$BEEN/pgm-amandelbult-iselin-lucht-jnb-jfk.geojson" \
    --been-geojson "truck|JFK South Cargo Area vrachtterminal → Metivo/BASF ECMS, Iselin NJ (NJ Turnpike/I-95)|$BEEN/pgm-amandelbult-iselin-weg-jfk-iselin.geojson" \
    --marker "pgm-amandelbult — Amandelbult-mijn (Anglo American Platinum / Valterra Platinum), Noordrand Bushveld, laadplek, bron-gelegd|-24.8080,27.2650" \
    --marker "pgm-rustenburg-pmr — Rustenburg PMR + Waterval-smelter-/RBMR-complex (Valterra Platinum), overslag naar weg, bron-gelegd|-25.6750,27.3180" \
    --marker "pgm-jnb-cargo — O.R. Tambo International Airport, vrachtplatform/-loodsen, overslag truck → lucht, bron-gelegd|-26.1380,28.2270" \
    --marker "pgm-jfk-cargo — JFK South Cargo Area (Cargo Plaza/South Cargo Road), Queens, New York, overslag lucht → truck, bron-gelegd|40.6587,-73.7952" \
    --marker "pgm-basf-ecms-iselin — Metivo (voorheen BASF Environmental Catalyst and Metal Solutions), 33 Wood Ave South, Iselin NJ 08830, stoppunt, bron-gelegd|40.5650,-74.3288" \
    --routebrief v2/design/routebrieven/pgm-amandelbult-iselin.md \
    --uit    v2/data/stroomroute-pgm-amandelbult-iselin.json \
    --stroom pgm-amandelbult-iselin \
    --titel  "PGM · Amandelbult (Zuid-Afrika) → Rustenburg PMR → OR Tambo (JNB) → JFK (New York) → Metivo/BASF ECMS, Iselin NJ"
}

# ── kobalt · Kawasi HPAL-complex (Obi Island, Indonesië) → Xiamen Haicang (containerkade, China)
# Routebrief: v2/design/routebrieven/kobalt-obi-ganzhou.md (lichte werkwijze M31 golf 4)
# Drie zeebenen, geen truck-/spoorbenen.
# ⚠️ b1 (zee, haven-aanloop, LETTERLIJKE KOPIE) = exact
#    v2/build-cache/ais/graaf/nikkel-obi-ningbo-aanloop-kawasi.geojson
#    (gebakken in bak_nikkel_obi_ningbo: 84,9 km, 32 punten) — zelfde fysieke
#    jetty en hetzelfde pad als nikkel-obi-ningbo b1, geen nieuwe
#    maak_havenaanloop.py-run.
# ⚠️ b2 (zee, MARNET, nieuw, GEEN stippel): zeeknoop 9031 → zeeknoop 5576.
#    Geen gepubliceerde lengte voor deze corridor naar Xiamen — de brief geeft
#    alleen een analogie met de gebakken nikkel-obi-ningbo-corridor naar
#    Ningbo (4.202,5 km); de console-km hieronder is de enige referentie,
#    geen ±15%-harde toets mogelijk (brief §7).
# ⚠️ b3 (zee, haven-aanloop, nieuw): de Xiamen Haicang-kade ligt 5,7 km van
#    zeeknoop 5576, boven de 5 km-drempel (LAR-586, bakhandleiding §2) — dus
#    VERPLICHT een haven-aanloop, ook al ligt de kade ruim binnen de 25 km-
#    snap. `maak_havenaanloop.py` onder timeout 300 vond GEEN pad binnen de
#    tijd (exit 124) → terugval rechte stippel, geen tweede poging.
# ⚠️ Geen been C (Xiamen → GEM Ganzhou): GEM's Ganzhou-vestiging heeft geen
#    site-niveau coördinaat gevonden deze sessie (brief §6/§7 — zelfde
#    patroon als de Huayou Quzhou-knoop in kobalt-morowali-quzhou.md). Geen
#    lijn, geen stippel, geen marker voor die knoop.
bak_kobalt_obi_ganzhou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel-geojson "zee|haven-aanloop Kawasi (schematisch, over water — MARNET reikt niet; letterlijke kopie nikkel-obi-ningbo b1)|$BEEN/nikkel-obi-ningbo-aanloop-kawasi.geojson" \
    --been         "zee|zeeschip Obi/Kawasi → Xiamen/Haicang (MHP/nikkelsulfaat, Co als bijproduct; Molukse Zee → Straat Makassar/Lombok → Zuid-Chinese Zee → Straat Taiwan)|-1.1099,127.9122|24.4515,117.9163" \
    --stippel      "zee|haven-aanloop Xiamen Haicang (schematisch — kade 5,7 km van de MARNET-zeeknoop; maak_havenaanloop.py-timeout, geen tweede poging)|24.4515,117.9163|24.4585,117.9720" \
    --marker "co-obi-kawasi — Kawasi HPAL-complex, Obi Island (PT Halmahera Persada Lygend / PT Obi Nickel Cobalt) — mijn + HPAL + eigen exportjetty, hergebruikt anker|-1.5361,127.4160" \
    --marker "co-xiamen-haicang — Xiamen Haicang Container Terminal, Fujian — overslag zeeschip → onbekend vervolg, stoppunt, bron-gelegd|24.4585,117.9720" \
    --routebrief v2/design/routebrieven/kobalt-obi-ganzhou.md \
    --uit    v2/data/stroomroute-kobalt-obi-ganzhou.json \
    --stroom kobalt-obi-ganzhou \
    --titel  "Kobalt · Obi (Kawasi) → Xiamen Haicang (China)"
}

# ── kobalt · Murrin Murrin (Australië) → Leonora → Kwinana → Ningbo → Tongxiang (China)
# Routebrief: v2/design/routebrieven/kobalt-murrinmurrin-kwinana.md (lichte werkwijze M31 golf 4, reserve-as)
# ⚠️ b1 (truck, NIEUW profiel): scan vond een doorgaand pad, 65,4 km tegen de
#    hemelsbrede brief-schatting van 56,4 km (+16,0%) — de brief geeft "geen
#    wegkm" dus dit is een indicatie, geen harde ±15%-toets (bakhandleiding §5).
# ⚠️ b2 (spoor, NIEUW, BAKE_SUFFIX=-raw): ÉÉN directe Dijkstra-run
#    Leonora→Kalgoorlie geeft 260,4 km tegen 259 km gepubliceerd (Wikipedia
#    "Leonora railway line", +0,5%) — de brief-via-punten Malcolm/Menzies
#    bleken NIET nodig: de vrije Dijkstra volgde hier al vanzelf de juiste
#    lijn (geen omweg/geen tweede route gevonden om te vergelijken), dus geen
#    aparte kop→via/via→staart-runs.
# ⚠️ b3 (spoor, NIEUW, 4 losse runs): Broad Arrow is BEWUST NIET als via-punt
#    gebruikt — Wikipedia-coördinaatcheck (en.wikipedia.org/wiki/Broad_Arrow,
#    _Western_Australia) bevestigt dat de plaats 38 km NOORD van Kalgoorlie
#    ligt, aan de Kalgoorlie–Leonora-weg (dus op de b2-corridor, een ZIJTAK
#    van de Eastern Goldfields Railway naar Perth, niet erop). Met Broad
#    Arrow als via-punt gaf het eerste deelsegment een sanity-fout (route
#    34,3 km < grootcirkel 35,6 km) en samen met het tweede segment 319,3 km
#    Kalgoorlie→Southern Cross tegen 251,3 km voor de directe run — een
#    echte omweg (bakhandleiding: "een via-punt dat een omweg geeft
#    verwijder of verplaats je, met een ⚠️-noot"). Gebruikt: Kalgoorlie →
#    Southern Cross (direct, 251,3 km) → Merredin (118,9 km) → Northam
#    (163,2 km) → Kwinana-kade (157,5 km) = 690,9 km tegen de indicatieve
#    webcheck-schatting ~642 km uit de brief (+7,6%, indicatie, geen harde
#    norm — brief §7/bak_aanwijzingen).
# ⚠️ b4 (zee-haven-aanloop, NIEUW, STIPPEL — LAR-586): Kwinana-kade ligt
#    20,9 km van zeeknoop 8982 (>5 km, dus verplicht ondanks <25 km
#    max-snap). `maak_havenaanloop.py` vond een pad over water: 22,5 km,
#    38 punten, 1,24 km "over land" ligt op het uiteinde (kade op de
#    1:10M-kustlijn, geen echte landkruising midden op de lijn).
# ⚠️ b5 (zee, NIEUW): MARNET-route zeeknoop 8982 → Ningbo Beilun-kade
#    (Ningbo snapt al <5 km, geen aparte aanloop aan de Chinese kant nodig).
#    Indicatief ~7.300 km in de brief (hemelsbreed 6.925 km); console-km
#    hieronder is de gemeten MARNET-afstand.
# ⚠️ b6 (truck, LETTERLIJKE KOPIE, OMGEKEERDE RICHTING): puntenvolgorde
#    omgedraaid t.o.v. kobalt-huayou-gunsan-weg-tongxiang-ningbo.geojson
#    (stroom kobalt-huayou-gunsan, been b1, functie bak_kobalt_huayou_gunsan)
#    — geen nieuwe wegscan, 192,2 km, al getoetst in de eigen brief van die
#    stroom (kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson).
# ⚠️ Kalgoorlie is bewust GEEN apart anker/overslag (geen modaliteitswissel,
#    blijft spoor→spoor) — alleen knoop in de spoorroute-runs (brief §3/§4).
# ⚠️ Open punten (brief §7): rol Kwinana-kade als exporthaven voor
#    nikkel/kobalt is aannemelijk, niet primair gebrond; b1-wegkm en
#    b3-spoorkm zijn hemelsbreed resp. webcheck-schattingen; uitgaande
#    modaliteit spoor niet apart gebrond (Wikipedia noemt vooral inkomend
#    zwavel/ammoniak); zeeroute-lengte indicatief; aandeel van deze route in
#    Murrin Murrin's totale kobaltproductie niet gebrond.
bak_kobalt_murrinmurrin_kwinana() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|briketten Murrin Murrin HPAL-plant → Leonora-spoorhoofd (eigen toegangsweg → Goldfields Highway)|$BEEN/kobalt-murrinmurrin-kwinana-weg-plant-leonora.geojson" \
    --been-geojson "spoor|trein Leonora-spoorhoofd → Kalgoorlie (Kalgoorlie–Leonora-lijn, directe run — Malcolm/Menzies niet nodig)|$BEEN/spoorroute-kobalt-murrinmurrin-kwinana-leonora-kalgoorlie.geojson" \
    --been-geojson "spoor|trein Kalgoorlie → Southern Cross (Eastern Goldfields Railway, direct — Broad Arrow ligt op de b2-zijtak, niet op deze corridor)|$BEEN/spoorroute-kobalt-murrinmurrin-kwinana-kalgoorlie-southerncross.geojson" \
    --been-geojson "spoor|trein Southern Cross → Merredin (Eastern Goldfields Railway)|$BEEN/spoorroute-kobalt-murrinmurrin-kwinana-southerncross-merredin.geojson" \
    --been-geojson "spoor|trein Merredin → Northam (Eastern Goldfields Railway)|$BEEN/spoorroute-kobalt-murrinmurrin-kwinana-merredin-northam.geojson" \
    --been-geojson "spoor|trein Northam → Kwinana-kade (Eastern Goldfields Railway → Kwinana-industriespoor)|$BEEN/spoorroute-kobalt-murrinmurrin-kwinana-northam-kwinana.geojson" \
    --stippel-geojson "zee|haven-aanloop Kwinana (schematisch, over water — kade 20,9 km van de MARNET-zeeknoop, LAR-586)|$BEEN/kobalt-murrinmurrin-kwinana-aanloop-kwinana.geojson" \
    --been         "zee|zeeschip Kwinana → Ningbo Beilun-kade (Indische Oceaan → Lombok/Makassar-straat → Zuid-Chinese Zee → Oost-Chinese Zee, v1-patroon)|-32.0565,115.7160|29.9353,121.8695" \
    --been-geojson "truck|kobalttetroxide/-sulfaat Ningbo Beilun-kade → Huayou Tongxiang-raffinaderij (G60/G92 Tongxiang–Ningbo, letterlijke kopie omgekeerd van kobalt-huayou-gunsan b1)|$BEEN/kobalt-murrinmurrin-kwinana-weg-ningbo-tongxiang.geojson" \
    --marker "co-murrinmurrin-plant — Murrin Murrin HPAL nikkel-kobaltplant (Glencore/Minara Resources), Laverton Shire, WA (bron-gelegd)|-28.7680,121.8940" \
    --marker "co-leonora-spoorhoofd — Leonora, railhead Kalgoorlie–Leonora-lijn (aannemelijk)|-28.8845,121.3308" \
    --marker "co-kwinana-kade — Kwinana Bulk Jetty (Fremantle Ports) (bron-gelegd)|-32.2414,115.7576" \
    --marker "co-ningbo-kade — Beilun Container Terminal Phase 2, Ningbo-Zhoushan (hergebruikt anker, bron-gelegd)|29.9353,121.8695" \
    --marker "co-tongxiang-raffinaderij — Zhejiang Huayou Cobalt nikkel-kobaltsmelterij, Tongxiang Economic Development Zone (hergebruikt anker, stoppunt, bron-gelegd)|30.6167,120.5629" \
    --routebrief v2/design/routebrieven/kobalt-murrinmurrin-kwinana.md \
    --uit    v2/data/stroomroute-kobalt-murrinmurrin-kwinana.json \
    --stroom kobalt-murrinmurrin-kwinana \
    --titel  "Kobalt · Murrin Murrin (Australië) → Kwinana → Ningbo → Tongxiang (China)"
}

# ── zilver · Broken Hill Mine (Rasp-mijn, NSW) → Crystal Brook-knooppunt → Nyrstar Port Pirie-smelter (Zuid-Australië)
# Routebrief: v2/design/routebrieven/zilver-brokenhill-portpirie.md (lichte werkwijze M31 golf 5)
# ⚠️ Twee spoorbenen, geen zee/weg — de keten stopt bij de smelter (brief §6,
#    geen fase D/E). Geen last-mile-been mijn→spoor: het gefilterde
#    concentraat gaat "trucked less than a kilometre to the Rasp rail siding"
#    (bron [7]), ruim onder de 2 km-drempel — b1 begint direct op het
#    site-anker.
# ⚠️ b1 (ag-brokenhill-mijn → ag-crystal-brook-knoop, BAKE_SUFFIX=-raw):
#    gemeten 370,0 km (verhouding 1,07 t.o.v. de grootcirkel, 0 omkeringen na
#    de keerstraf). De brief geeft zelf een discrepantie aan: 394,2 km uit een
#    stations-afstandstabel tegen Wikipedia's 371 km voor de hele lijn. De
#    gemeten 370,0 km ligt vrijwel op het Wikipedia-getal (−0,3%) en 6,1%
#    onder de brief-tabel — bevestigt het eigen open punt van het ontwerp,
#    geen fout van deze bake (brief §7).
# ⚠️ b2 (ag-crystal-brook-knoop → ag-portpirie-smelter): gemeten 28,6 km
#    (verhouding 1,06 t.o.v. de grootcirkel van 27,0 km) tegen de
#    hemelsbreed-schatting uit de brief (~27,5 km, geen wegkm/spoorkm
#    gepubliceerd) — indicatie, geen ±15%-norm (brief zegt dat expliciet).
# ⚠️ Geen via-punten (brief §4: geen gedocumenteerde corridorkeuze op b1;
#    b2 is een kort feederspoor). Geen haven-aanloop (geen zeebeen). Geen
#    stippels — beide benen zijn doorgetrokken, gemeten spoorroutes.
bak_zilver_brokenhill_portpirie() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Broken Hill Mine (Rasp-mijn) → Crystal Brook-knooppunt (Crystal Brook–Broken Hill railway line, ARTC-net, ex-Silverton Tramway-tracé)|$BEEN/spoorroute-zilver-brokenhill-portpirie-brokenhill-crystalbrook.geojson" \
    --been-geojson "spoor|trein Crystal Brook-knooppunt → Nyrstar Port Pirie-smelter (Bowmans Rail-vrachtlijn)|$BEEN/spoorroute-zilver-brokenhill-portpirie-crystalbrook-portpirie.geojson" \
    --marker "ag-brokenhill-mijn — Broken Hill Mine (Rasp-mijn, Broken Hill Mines/Coolabah Metals sinds okt. 2024) — mijn/verwerkingsfabriek, kop van het spoor|-31.9486,141.4852" \
    --marker "ag-crystal-brook-knoop — Crystal Brook, spoorzone rond Railway Terrace — spoorknooppunt, splitsing ARTC-hoofdlijn/Bowmans Rail-vrachtlijn (aannemelijk)|-33.3497,138.2020" \
    --marker "ag-portpirie-smelter — Nyrstar Port Pirie-smelter — losplek/smelter, stoppunt|-33.1684,138.0095" \
    --routebrief v2/design/routebrieven/zilver-brokenhill-portpirie.md \
    --uit    v2/data/stroomroute-zilver-brokenhill-portpirie.json \
    --stroom zilver-brokenhill-portpirie \
    --titel  "Zilver · Broken Hill (NSW) → Crystal Brook → Port Pirie (Zuid-Australië)"
}

# ── zilver · Uchucchacua-mijnkamp (Buenaventura, Oyón) → Transportadora Callao-mineraalterminal (Callao-haven)
# Routebrief: v2/design/routebrieven/zilver-uchucchacua-callao.md (lichte werkwijze M31 golf 5)
# ⚠️ Eén been (b1, truck), géén zeebeen — de keten stopt BEWUST bij het
#    exportpunt: geen bron bevestigt dat Uchucchacua-concentraat specifiek
#    naar Callao/Transportadora Callao gaat versus een eigen Buenaventura-
#    verwerkingsfabriek elders in Peru (brief §6/§7, bindend uit de
#    haalbaarheidstoets — Cannington-precedent). Geen fase B/C/D/E.
# ⚠️ Geen gepubliceerde wegkm binnen budget (brief §7): gepubliceerdKm =
#    hemelsbreed via-punten-som 243,2 km, expliciet géén ±15%-harde-norm
#    (Andes-traject Oyón→Sayán, 2-3× de directe hemelsbrede 160 km). Gemeten
#    wegkm (`maak_stroombeen_weg.py`, extract peru): **305,4 km** — +25,6% t.o.v.
#    de 243,2 km-indicatie, buiten ±15% maar VERWACHT en GEEN bevinding zoals
#    de brief het bedoelt (de indicatie is zelf al erkend zwak); zie §9.
# ⚠️ Mijn-anker AFWIJKEND van de sitelaag-v1-centroïde `w-uchucchacua`
#    (-10.6200,-76.9200 in v2/design/zilver-sitelaag.json) — die ligt op leeg
#    Andes-terrein zonder mijninfrastructuur, 25 km WNW van het hier gebruikte,
#    satelliet-bevestigde mijnkamp-anker (brief §7). Sitelaag zelf NIET
#    aangeraakt — alleen gemeld (eigen bestanden, zie werkwijze).
# ⚠️ Callao-anker verscherpt van de generieke havencentroïde `ag-port-callao`
#    (data/silver.js, -12.05,-77.15) naar de satelliet-bevestigde Transportadora
#    Callao-mineraalterminal (muelle centro) — vier bulkcarrier-ligplaatsen
#    naast elkaar tussen de APM- en DP World-containerterminals (brief §3).
#    `data/silver.js` zelf niet aangeraakt.
# ⚠️ Geen haven-aanloop: er is geen zeebeen in deze brief. Ter info (brief §7):
#    de TCSA-kade ligt 60,7 km van de dichtstbijzijnde MARNET-zeeknoop (knoop
#    394, -12.00000,-77.70000) — ruim boven de 5 km-drempel, dus zou bij een
#    latere fase B een haven-aanloop-stippel vragen.
# ⚠️ Geen stippels in b1 — doorgetrokken, gemeten wegcorridor (eindKlassen
#    ruim + eindToegangPrivaat True voor het mijnkamp- en het havenzone-
#    uiteinde, profielsleutel zilver-uchucchacua-callao-mijn-tcsa).
bak_zilver_uchucchacua_callao() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|truck lood/zink-zilverconcentraat Uchucchacua-mijnkamp → Transportadora Callao-mineraalterminal (Oyón–Churín–Sayán–Huacho–Chancay, Panamericana Norte)|$BEEN/zilver-uchucchacua-callao-weg-mijn-tcsa.geojson" \
    --marker "ag-uchucchacua-mijn — Uchucchacua-mijnkamp (Buenaventura), Oyón, Lima-regio — mijn/laadplek, bron-gelegd|-10.6335,-76.6895" \
    --marker "ag-callao-tcsa — Transportadora Callao S.A. mineraalterminal (muelle centro), Callao-haven — overslag/exportpunt, stoppunt, bron-gelegd|-12.0499,-77.1446" \
    --routebrief v2/design/routebrieven/zilver-uchucchacua-callao.md \
    --uit    v2/data/stroomroute-zilver-uchucchacua-callao.json \
    --stroom zilver-uchucchacua-callao \
    --titel  "Zilver · Uchucchacua-mijnkamp (Peru) → Callao (mineraalterminal, stoppunt)"
}

# ── zilver · Fresnillo/Saucito-mijnencomplex (Fresnillo plc) → Met-Mex Peñoles-raffinaderij Torreón (Mexico, binnenlands)
# Routebrief: v2/design/routebrieven/zilver-fresnillo-torreon.md (lichte werkwijze M31 golf 5)
# ⚠️ Eén been, één tool (maak_stroombeen_weg.py, profiel zilver-fresnillo-torreon-
#    fresnillo-torreon): truck MEX 45/45D (Fresnillo-Río Grande) → MEX 40D/49D
#    (Cuencamé-Ciudad Lerdo-Torreón), 100% binnenlands, geen zeebeen.
# ⚠️ Geen bedrijfs-/overheidsopgave van de wegkilometer binnen budget (brief §7):
#    enige cijfers zijn hemelsbreed 270 km en een route-planner-webcheck van
#    331 km (mejoresrutas.com). De ±15%-toets tegen 331 km geldt hier als
#    INDICATIE, niet als harde norm (brief §7, profiel-bronnoot).
# ⚠️ Geen fase D/E: de raffinaderij is het stoppunt van deze as (brief §6).
bak_zilver_fresnillo_torreon() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|zilverdoré/-concentraat Fresnillo/Saucito-mijnencomplex → Río Grande → Cuencamé → Ciudad Lerdo → Met-Mex Peñoles-raffinaderij Torreón (MEX 45/45D → 40D/49D)|$BEEN/zilver-fresnillo-torreon-weg-fresnillo-torreon.geojson" \
    --marker "ag-fresnillo-mijn — Fresnillo/Saucito-mijnencomplex (Fresnillo plc, Zacatecas) — mijn/plant (laad)|23.1580,-102.8600" \
    --marker "Río Grande (Zacatecas) — via-punt corridorkeuze (MEX 45/45D vs. lokale zijwegen)|23.8269,-103.0338" \
    --marker "Cuencamé (Durango) — via-punt corridorkeuze (overgang naar MEX 40D/49D)|24.8700,-103.6978" \
    --marker "Ciudad Lerdo (Durango) — via-punt corridorkeuze (La Laguna-conurbatie)|25.5366,-103.5252" \
    --marker "ag-penoles-torreon — Met-Mex Peñoles-raffinaderij (Industrias Peñoles, Torreón, Coahuila) — raffinaderij (los, stoppunt)|25.5278,-103.4417" \
    --routebrief v2/design/routebrieven/zilver-fresnillo-torreon.md \
    --uit    v2/data/stroomroute-zilver-fresnillo-torreon.json \
    --stroom zilver-fresnillo-torreon \
    --titel  "Zilver · Fresnillo/Saucito (Fresnillo plc) → Met-Mex Peñoles Torreón (Mexico)"
}

# ── uranium · Smith Ranch-Highland ISR-mijn (Wyoming) → Metropolis Works (Illinois)
# Routebrief: v2/design/routebrieven/uranium-smithranch-metropolis.md (lichte werkwijze M31 golf 5)
# Eén been (b1, fase A, truck): I-25 zuid (Douglas–Cheyenne) → I-80 oost (Nebraska–Iowa)
# → I-80/I-39-knik bij LaSalle-Peru/Utica → I-39/I-74/I-57 zuid door Illinois naar
# Metropolis Works. Bewust om Colorado heen (extract ontbreekt daar, brief §7).
# ⚠️ gepubliceerdKm = ~2.090 km is een ALGEMENE Wyoming-brede claim ("over 1.300
#    miles", Cowboy State Daily sept. 2025), niet route-specifiek — de ±15%-toets
#    geldt hier als INDICATIE, geen harde norm (brief §2/§7). Gemeten: 2.161,8 km
#    weggeometrie (+3,4% t.o.v. de indicatie) — binnen elke redelijke marge.
# ⚠️ Geen last-mile-stippel nodig aan beide kanten: de scan (eindKlassen default,
#    12 km-zone) vond een doorlopend wegpad tot op het mijnterrein (plant → weg
#    0,06 km) en tot aan de fabriekspoort (weg → kade 0,03 km) — beide ruim onder
#    de "> ~2 km = last mile"-drempel van de vaste regels van de kaart.
# ⚠️ SITELAAG-DISCREPANTIE (voor de orkestrator, niet hier gewijzigd): het
#    bestaande sitelaag-anker `w-metropolis` in v2/design/uranium-sitelaag.json
#    (37.1500,-88.7333, status "aannemelijk") ligt ~3,2 km ZO van de echte
#    fabriek — een stadspunt in Metropolis zelf. Deze stroom gebruikt daarom de
#    Wikipedia-infobox-/satellietbevestigde coördinaat (37.1718,-88.7570) als
#    eigen anker `u-metropolis-conversie`; de sitelaag zelf is niet aangepast
#    (brief §3/§7).
bak_uranium_smithranch_metropolis() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|yellowcake Smith Ranch-Highland ISR-mijn → Metropolis Works (I-25 zuid → I-80 oost → I-39/I-74/I-57 zuid door Illinois)|$BEEN/uranium-smithranch-metropolis-weg-smithranch-metropolis.geojson" \
    --marker "u-smithranch-mijn — Smith Ranch-Highland ISR-mijn (Cameco Resources), Converse County, Wyoming — mijn (laadplek), bron-gelegd|43.0537,-105.6851" \
    --marker "u-metropolis-conversie — Honeywell/ConverDyn Metropolis Works, Metropolis, Illinois — conversiefabriek (U3O8 → UF6), stoppunt, bron-gelegd|37.1718,-88.7570" \
    --routebrief v2/design/routebrieven/uranium-smithranch-metropolis.md \
    --uit    v2/data/stroomroute-uranium-smithranch-metropolis.json \
    --stroom uranium-smithranch-metropolis \
    --titel  "Uranium · Smith Ranch-Highland (Wyoming) → Metropolis Works (Illinois)"
}

# ── uranium · Orano Malvési (Comurhex I, Narbonne) → Orano Tricastin (Comurhex II + Georges Besse II, Pierrelatte)
# Routebrief: v2/design/routebrieven/uranium-malvesi-tricastin.md (lichte werkwijze M31 golf 5)
# ⚠️ Modaliteit-correctie t.o.v. het ketenontwerp: SPOOR, niet truck — Wikipedia (fr)
#    documenteert de overschakeling naar spoor in 2014 na de blokkade-actie van
#    12-09-2013, met een gedateerd 2017-cijfer (320 t U/week); een tegensprekende
#    bron (homonuclearus.fr, 2020) noemt 3-5 vrachtwagens voor dezelfde route
#    (brief §7). `spoornet_nodig: false` uit het ketenontwerp is hiermee achterhaald.
# ⚠️ Vier losse runs in reisvolgorde i.p.v. één via-keten (bakhandleiding §2, spoor):
#    een vrije Dijkstra tussen de site-ankers koos anders een omweg; de drie
#    via-punten (Gare de Narbonne/Nîmes/Avignon-Centre, brief §4) pinnen de
#    hoofdcorridor Béziers–Montpellier–Nîmes–Avignon–Pierrelatte. Been 2
#    (Narbonne→Nîmes) met `--keerstraf=150` (default 25 gaf een extra
#    terugloop-lus bij 43.8138,4.5126 zonder kortere route; 150 haalt hem weg
#    op exact dezelfde lengte, 168,0 km). Been 4 blijft op de default 25 —
#    150 gaf daar juist een omweg (110,9 i.p.v. 67,3 km).
# ⚠️ Geen gepubliceerde spoorkm om tegen te toetsen (alleen de hemelsbrede 187 km
#    uit het ontwerp) — gemeten totaal 291,9 km (+56,1% t.o.v. hemelsbreed);
#    indicatie zoals de brief zelf voorschrijft, geen ±15%-norm.
# ⚠️ Eén terugloop-lus blijft staan op been 1+2 bij de Narbonne-Malvési-
#    aftakking (43.187,3.0011, ~55 m boogstraal) — onafhankelijk van keerstraf
#    (25 én 150 geven 'm) en op precies hetzelfde punt in twee los geroutete
#    benen: aannemelijk een echte kop-maak-junctie waar de private aftakking
#    op de hoofdlijn aansluit, geen routeerartefact. Niet weggeschoven (§9).
# ⚠️ Geen stippel: beide site-ankers liggen op het fabrieksterrein/emplacement
#    zelf (geen haven-aanloop, geen zee-been, geen last-mile). Géén fase D —
#    Tricastin → Framatome Romans-sur-Isère is vervallen (brief §6/§7).
bak_uranium_malvesi_tricastin() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "spoor|trein Orano Malvési → Gare de Narbonne (private Malvési-aftakking, 4,9 km, vernieuwd 2020)|$BEEN/spoorroute-uranium-malvesi-tricastin-malvesi-narbonne.geojson" \
    --been-geojson "spoor|trein Gare de Narbonne → Gare de Nîmes (hoofdlijn Béziers–Montpellier, corridorkeuze i.p.v. Perpignan/Toulouse)|$BEEN/spoorroute-uranium-malvesi-tricastin-narbonne-nimes.geojson" \
    --been-geojson "spoor|trein Gare de Nîmes → Gare d'Avignon-Centre (corridorkeuze i.p.v. de aftakking Alès/Le Grau-du-Roi)|$BEEN/spoorroute-uranium-malvesi-tricastin-nimes-avignon.geojson" \
    --been-geojson "spoor|trein Gare d'Avignon-Centre → Orano Tricastin (Rhônevallei noordwaarts, corridorkeuze i.p.v. de lijn naar Marseille)|$BEEN/spoorroute-uranium-malvesi-tricastin-avignon-tricastin.geojson" \
    --marker "u-malvesi — Orano Malvési, Comurhex I (conversie U3O8→UF4), Narbonne — laadplek, kop van het spoor|43.2074,2.9812" \
    --marker "u-tricastin — Orano Tricastin, Comurhex II (UF4→UF6) + Georges Besse II-verrijking, Pierrelatte — losplek, stoppunt|44.3250,4.7167" \
    --routebrief v2/design/routebrieven/uranium-malvesi-tricastin.md \
    --uit    v2/data/stroomroute-uranium-malvesi-tricastin.json \
    --stroom uranium-malvesi-tricastin \
    --titel  "Uranium · Orano Malvési (Narbonne) → Orano Tricastin (Pierrelatte)"
}

# ── zilver · Rampura Agucha-mijn (Hindustan Zinc, Bhilwara) → Chanderiya Lead-Zinc Smelter (Chittorgarh)
# Routebrief: v2/design/routebrieven/zilver-rampuraagucha-pantnagar.md (lichte werkwijze M31 golf 5)
# ⚠️ EENBENIGE KETEN, BINDEND INGEKORT (brief §6): het tweede, zwak onderbouwde spoorbeen naar
#    Pantnagar (Uttarakhand) en `spoornet_nodig` zijn na de haalbaarheidstoets vervallen — Wikipedia
#    (Hindustan Zinc) bevestigt alleen dat Pantnagar "initially intended" was voor zilversmelt, niet
#    dat er vandaag een zilverstroom loopt. Chanderiya (produceert zelf al "zinc, lead, cadmium and
#    other precious metals") is het sterker gedocumenteerde stoppunt.
# ⚠️ b1 (truck, geofabrik india-extract) is GEMETEN en doorgetrokken, geen stippel, geen via-punt
#    bijgeschoven. Geen gepubliceerde wegkm binnen budget (brief §7/§8[8]): gepubliceerdKm = hemelsbreed
#    98,0 km tussen de satelliet-gelegde ankers, toets-bindend als indicatie (geen harde ±15%-norm); een
#    niet-officiële OSRM-schatting over dezelfde NH48-corridor gaf ~119,4 km. Gemeten: 126,5 km over de
#    NH48 via Gulabpura → Bhilwara-bypass → Chittorgarh → Chanderiya-afslag (+29,1% tegen de indicatieve
#    98,0 km — buiten de ±10%-tool-waarschuwing maar dicht bij de eigen OSRM-indicatie van 119,4 km,
#    dus binnen de vooraf verwachte orde van grootte; bevinding, geen via-punt bijgeschoven).
# ⚠️ Anker→weg-verbinding bij de mijn 0,51 km (net > de 0,5 km-norm, bevinding, geen tweede poging) —
#    de mijn/concentrator ligt op een klein-klasse toegangsweg vlak naast de doorgaande NH48-aftakking.
bak_zilver_rampuraagucha_pantnagar() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|truck Rampura Agucha-mijn/concentrator (Hindustan Zinc) → Chanderiya Lead-Zinc Smelter, NH48 via Gulabpura, Bhilwara-bypass, Chittorgarh|$BEEN/zilver-rampuraagucha-pantnagar-weg-rampuraagucha-chanderiya.geojson" \
    --marker "ag-rampuraagucha-mijn — Rampura Agucha-mijn en concentrator (Hindustan Zinc), Bhilwara — laadplek, bron-gelegd|25.8416,74.7332" \
    --marker "ag-chanderiya-smelter — Chanderiya Lead-Zinc Smelter Complex (Hindustan Zinc), Chittorgarh — losplek, stoppunt, bron-gelegd|24.9632,74.6580" \
    --routebrief v2/design/routebrieven/zilver-rampuraagucha-pantnagar.md \
    --uit    v2/data/stroomroute-zilver-rampuraagucha-pantnagar.json \
    --stroom zilver-rampuraagucha-pantnagar \
    --titel  "Zilver · Rampura Agucha-mijn (Hindustan Zinc) → Chanderiya Lead-Zinc Smelter (Chittorgarh)"
}

# ── uranium · Kharasan ISR-complex (Zuid-Kazachstan) → Zhanakorgan-station → Alashankou-station (grensovergang China)
# Routebrief: v2/design/routebrieven/uranium-kharasan-alashankou.md (lichte werkwijze M31 golf 5)
# ⚠️ b1 (truck) is GEEN stippel: de scanner vond wél een doorgaand wegpad
#    (34,3 km, kleine wegklassen tot 12 km van plant/kade mee) tegen ~31 km
#    hemelsbreed in de brief (+10,8% — buiten ±10% maar de brief geeft geen
#    echte wegkm, dus dit is indicatie, geen norm; brief §2/§7).
# ⚠️ b2 (spoor) is ZEVEN aparte segmenten in reisvolgorde (geen --via bestaat
#    in de spoorrouter, uranium-inkai-poti-patroon): Zhanakorgan → Turkestan
#    → Shymkent → Taraz → Almaty-2 → Aktogay (via-punt bij benadering, brief
#    §4) → Dostyk (grensovergang, bogiewissel 1520→1435mm) → Alashankou.
#    Route 1.967,0 km tegen ~1.850 km hemelsbreed-som via-punten (brief, geen
#    gepubliceerde spoorkm) = +6,3% — indicatie, geen harde norm (brief §2/§7,
#    "het gemeten getal wordt de nieuwe waarheid"). Het laatste stukje
#    Dostyk→Alashankou (17,1 km) is apart gehouden zoals de brief voorstelt
#    voor de gauge-breuk, al liep de router er zonder blokkade doorheen (OSM-
#    topologie is gauge-onafhankelijk; de wissel zelf is niet als apart been
#    gemodelleerd, brief §7).
# ⚠️ Geen zeebenen, geen leiding, geen lucht in deze keten (brief §1/§6).
#    Geen fase D/E: de brief stopt bij het Alashankou-spoorstation (§6),
#    geen verwerkingsknoop na de grensovergang.
# ⚠️ Open punten (brief §7): Kharasan als bronmijn niet individueel bevestigd
#    voor de SNURDC/SPIC/CNUC-contracten (alleen Kazatomprom als staats-
#    exporteur); Kharasan-coördinaat verfijnd van 2 naar 4 decimalen via
#    satellietblik, geen NI 43-101-rapport gevonden; spoorcorridor Trans-
#    Aral→Turksib→Aktogay→Dostyk is geografisch afgeleid (geen bron noemt de
#    tussenstations); Aktogay-via-punt is zelf een benadering.
bak_uranium_kharasan_alashankou() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|yellowcake Kharasan ISR-complex → Zhanakorgan-spoorstation (steppepiste/toegangsweg, geen bron voor exact traject)|$BEEN/uranium-kharasan-alashankou-weg-kharasan-zhanakorgan.geojson" \
    --been-geojson "spoor|trein Zhanakorgan-station → Turkestan-station (Trans-Aral-lijn zuidwaarts)|$BEEN/spoorroute-uranium-kharasan-alashankou-zhanakorgan-turkestan.geojson" \
    --been-geojson "spoor|trein Turkestan-station → Shymkent-station (Trans-Aral-lijn, naar de Arys-knoop)|$BEEN/spoorroute-uranium-kharasan-alashankou-turkestan-shymkent.geojson" \
    --been-geojson "spoor|trein Shymkent-station → Taraz-station (Turksib-lijn oostwaarts)|$BEEN/spoorroute-uranium-kharasan-alashankou-shymkent-taraz.geojson" \
    --been-geojson "spoor|trein Taraz-station → Almaty-2-station (Turksib-lijn oostwaarts)|$BEEN/spoorroute-uranium-kharasan-alashankou-taraz-almaty2.geojson" \
    --been-geojson "spoor|trein Almaty-2-station → Aktogay (spoorknoop, tak naar Dostyk/China, via-punt bij benadering)|$BEEN/spoorroute-uranium-kharasan-alashankou-almaty2-aktogay.geojson" \
    --been-geojson "spoor|trein Aktogay → Dostyk-station (grensovergang, laatste Kazachse station vóór de bogiewissel)|$BEEN/spoorroute-uranium-kharasan-alashankou-aktogay-dostyk.geojson" \
    --been-geojson "spoor|trein Dostyk-station → Alashankou-station (grensovergang, bogiewissel 1520→1435mm, stoppunt)|$BEEN/spoorroute-uranium-kharasan-alashankou-dostyk-alashankou.geojson" \
    --marker "u-kharasan-plant — Kharasan ISR-complex, Uranium One-JV/Rosatom (Kazatomprom, Zuid-Kazachstan-regio) — mijn/verwerkingscomplex (laadplek, bron-gelegd)|43.8427,66.8640" \
    --marker "u-zhanakorgan-station — Zhanakorgan-spoorstation, Kyzylorda-oblast — overslag truck → spoor (bron-gelegd)|43.9005,67.2467" \
    --marker "u-alashankou-station — Alashankou-spoorstation (阿拉山口站), Xinjiang — overslag spoor, grensovergang (stoppunt, bron-gelegd)|45.1703,82.5705" \
    --routebrief v2/design/routebrieven/uranium-kharasan-alashankou.md \
    --uit    v2/data/stroomroute-uranium-kharasan-alashankou.json \
    --stroom uranium-kharasan-alashankou \
    --titel  "Uranium · Kharasan (Kazachstan) → Zhanakorgan → Alashankou (grensovergang China)"
}

# ── ree · Chavara → Aluva (India, Zuid-Azië-reserve-as naast As1 OSCOM→Aluva)
# Routebrief: v2/design/routebrieven/ree-chavara-aluva.md (lichte werkwijze M31 golf 5).
# EÉN wegbeen (b1, truck): monaziet-houdend mineraalconcentraat IREL Chavara
# Mineral Division (Mannumala-mijnsite, Kollam) → IREL Rare Earths Division
# (RED), Udyogamandal/Edayar, Aluva — NH-66 kustweg → NH-544. Geen zee/spoor/
# leiding/overslag; fase D/E vervallen (brief §6: geen bron voor een specifieke
# magneetfabriek/afnemer voor déze corridor).
# ⚠️ Geen gepubliceerde wegkm (brief §7): hemelsbreed 124,3 km tussen de
#    site-ankers, via-puntensom 129,1 km. Gemeten wegkm = 143,0 km (ratio 1,15
#    tegen hemelsbreed — binnen de typische wegfactor 1,1-1,3x); de ±15%-toets
#    geldt hier als indicatie, niet als harde norm (brief §2/§7). Geen stippel:
#    beide ankers snappen <0,12 km op het wegnet (industrieterrein met normale
#    toegangswegen), 5 keerlussen gesnoeid (146,4 → 143,0 km).
# ⚠️ ree-aluva-red (10,08133/76,29761) ligt 190 m van het onafhankelijk
#    satellietgelegde `udyogamandal`-anker van de parallelle keten
#    ree-oscom-aluva (10,08300/76,29800, zelfde naar-site) — brief §7 beveelt
#    aan de twee bij het bakken/de sitelaag gelijk te trekken; hier bewust
#    NIET gedaan (raakt andermans brief/anker niet) — gemeld in het eindrapport.
# Deze keten wordt per ontwerp NIET gelijktijdig met ree-oscom-aluva gebakken
# (zelfde naar-site, zou een schijn-duplicaat zijn) — alleen inzetten als As1 vastloopt.
bak_ree_chavara_aluva() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Chavara -> RED Aluva (NH-66 -> NH-544)|$BEEN/ree-chavara-aluva-weg-chavara-aluva.geojson" \
    --marker "ree-chavara-scheiding|8.98583,76.52485" \
    --marker "ree-aluva-red|10.08133,76.29761" \
    --routebrief v2/design/routebrieven/ree-chavara-aluva.md \
    --uit    v2/data/stroomroute-ree-chavara-aluva.json \
    --stroom ree-chavara-aluva \
    --titel  "Zeldzame aardmetalen · Chavara -> Aluva (India)"
}

# ── uranium · Jaduguda-mijn (UCIL, Jharkhand) → NFC Hyderabad (India, binnenlandse splijtstofroute, zonder verrijking)
# Routebrief: v2/design/routebrieven/uranium-jaduguda-hyderabad.md (LICHTE werkwijze M31 golf 5)
# EEN BEEN, TRUCK, DOORGETROKKEN — geen zee/spoor in deze keten (India's eigen
# winningsland, tweede "geen-verrijking"-uitzondering naast Canada's CANDU).
# ⚠️ Eindanker u-nfc-hyderabad-stop is de ECIL X-Roads-kruising, GEEN
# fabriekspoort — NFC's eigen site-coördinaat is niet gevonden (Wikipedia
# zonder {{coord}}, Wikidata Q7067950 zonder P625, Nominatim/Photon/Overpass
# 0 hits; brief §6/§7). Geen last-mile-stippel naar de poort: er is geen
# tweede coördinaat om naartoe te stippelen.
# ⚠️ De zes via-punten zijn OSRM-routepunten met Nominatim-naambevestiging,
# geen gepubliceerd NH-tracé per segment (brief §4/§7) — de wegscan koos een
# vergelijkbaar maar niet per-se identiek tracé; alle snaps ≤0,04 km.
# ⚠️ De gemeten weglijn (1.295,7 km) wijkt −3,2% af van de gepubliceerde
# OSRM-wegroute (1.339 km, ECHTE wegkm) en ruim onder Wikipedia's indicatieve
# "~1.200 km" — binnen de ±15%-toets, die hier als indicatie geldt (brief §7).
bak_uranium_jaduguda_hyderabad() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|geel-koek Jaduguda-mijn (UCIL) → Hat Gamharia → Deogarh → Bolangir → Jagdalpur (Bastar) → Hanamkonda/Warangal → Bhongir → ECIL X-Roads, Hyderabad (India's binnenlandse splijtstofroute, zonder verrijking)|$BEEN/uranium-jaduguda-hyderabad-weg-jaduguda-hyderabad.geojson" \
    --marker "Jaduguda-mijn (UCIL), Purbi Singhbhum, Jharkhand — mijn/molen (laadplek, geel-koek)|22.6533,86.3466" \
    --marker "ECIL X-Roads-kruising, Kapra, Hyderabad — net-uiteinde bij NFC (GEEN poort, fabriekssite niet gevonden)|17.4733,78.5708" \
    --routebrief v2/design/routebrieven/uranium-jaduguda-hyderabad.md \
    --uit    v2/data/stroomroute-uranium-jaduguda-hyderabad.json \
    --stroom uranium-jaduguda-hyderabad \
    --titel  "Uranium · Jaduguda-mijn → Hyderabad (NFC, India — binnenlandse splijtstofroute)"
}

# ── zilver · Boliden Garpenberg (Dalarna) → Gävle-haven → Rönnskär-smelter (Skelleftehamn, Zweden)
# Routebrief: v2/design/routebrieven/zilver-garpenberg-ronnskar.md (LICHTE werkwijze M31 golf 5)
# Modaliteit BINDEND gecorrigeerd (brief §2): geen spoor zoals het ketenontwerp
# veronderstelde — Boliden's eigen NI 43-101-rapport zegt letterlijk dat het
# Zn/Pb-concentraat (met het zilver) per truck naar Gävle-haven gaat en per
# schip naar de smelters in Finland/Zweden/Noorwegen; alleen het koperconcentraat
# gaat per spoor naar Rönnskär. spoornet_nodig = false.
# ⚠️ b1 (truck): Hofors–Storvik–Sandviken is een geografische afleiding (brief
#    §4/§7, NIET gebrond met een bron). Gemeten wegkm 105,7 km tegen hemelsbreed
#    69,8 km (+51,5%) — BUITEN de ±15%-toets, maar die geldt hier bindend alleen
#    als indicatie (geen gepubliceerde wegkm, brief §2/§8[9]): een reële weg via
#    drie tussenplaatsen is langer dan de rechte lijn, bevinding, niet dichtgetrokken.
#    eindKlassen bewust ZONDER "unclassified" (zie kop van het profiel in
#    maak_stroombeen_weg.py): met "unclassified" erbij snapt de Gävle-kade op een
#    geïsoleerde stub-way (component van 5 knopen, geen pad naar Sandviken) i.p.v.
#    het doorgaande net — gemeten, niet aangenomen. Beide ankers liggen ≤0,45 km
#    van het net (OK, geen last-mile-stippel nodig).
# ⚠️ b2 (zee): kade Gävle ligt 19,2 km van zeeknoop 8841 (60.74660,17.54600) —
#    ruim boven de 5 km-drempel (LAR-586), dus haven-aanloop VERPLICHT óók al
#    snapt de router binnen de 25 km (bakhandleiding §2). maak_havenaanloop.py
#    slaagde (cel 0,005° kaal, 22,2 km, omwegfactor 1,155, 0,19 km over land —
#    uitsluitend aan het kade-uiteinde, geen landkruising midden op de lijn) →
#    --stippel-geojson; het hoofd-zeebeen begint daarom op de zeeknoop, niet op
#    de kade. Rönnskär-zijde GEEN aanloop nodig: kade 1,5 km van zeeknoop 8833
#    (64.66680,21.30040), ruim binnen de 5 km-drempel.
# ⚠️ Geen fase D/E (brief §6): geen bron noemt een fabriek/afnemer na Rönnskär
#    voor dit specifieke Garpenberg-concentraat — stoppunt bij de smelterkade.
# ⚠️ Geen gedeelde benen: eerste stroom die Garpenberg, Gävle of Rönnskär raakt.
bak_zilver_garpenberg_ronnskar() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|Garpenberg → Gävle-haven (Gästrikland via Hofors–Storvik–Sandviken, aannemelijk: geografische corridor)|$BEEN/zilver-garpenberg-ronnskar-weg-garpenberg-gavle.geojson" \
    --stippel-geojson "zee|haven-aanloop Gävle (schematisch, over water — MARNET reikt niet: kade 19,2 km van de zeeknoop)|$BEEN/zilver-garpenberg-ronnskar-aanloop-gavle.geojson" \
    --been         "zee|zeeschip Gävle-zeeknoop → Rönnskär-kade (Botnische Golf)|60.74660,17.54600|64.6704,21.2699" \
    --marker "ag-garpenberg-mijn — Boliden Garpenberg, Dalarna (mijn, zink/lood-bijproduct, kop wegbeen)|60.3129,16.1933" \
    --marker "ag-gavle-kade — Gävle Hamn, Fredriksskans-terminal (overslag truck → zee)|60.6922,17.2103" \
    --marker "ag-ronnskar-kade — Boliden Rönnskär, Skelleftehamn (smelter/losplek, stoppunt)|64.6704,21.2699" \
    --routebrief v2/design/routebrieven/zilver-garpenberg-ronnskar.md \
    --uit    v2/data/stroomroute-zilver-garpenberg-ronnskar.json \
    --stroom zilver-garpenberg-ronnskar \
    --titel  "Zilver · Garpenberg (Boliden) → Gävle → Rönnskär (Skelleftehamn, Zweden)"
}

# ── grafiet · Molo (Madagaskar) → Toliara → Rotterdam → Duisburg
# Routebrief: v2/design/routebrieven/grafiet-molo-duisburg.md (LICHTE werkwijze M31 golf 5).
# b1 (truck, doorgetrokken): profiel "grafiet-molo-duisburg-molo-toliara" in
#    maak_stroombeen_weg.py — regionale weg Fotadrevo → Ampanihy (RN10-
#    aansluiting) → Betioky Atsimo → Andranovory (RN10/RN7-kruispunt) → RN7
#    naar Toliara. Geen gepubliceerde wegkm (brief §2/§7); corridorKlassen
#    tertiary/unclassified/residential/service nodig — WEG_HOUD kaal (t/m
#    secondary) lag >25 km van Andranovory (RN10 is een onverharde
#    secundaire weg, geen OSM `secondary`). Gebakken: 378,4 km (na het
#    snoeien van 6 keerlussen, 516,8 → 378,4 km) tegen hemelsbreed ~165 km —
#    +129% is GEEN norm-overschrijding: de brief zegt zelf dat de werkelijke
#    wegkm door de zuidelijke omweg over Ampanihy "ruim boven 165 km" ligt en
#    dat de ±15%-toets hier niet geldt.
# ⚠️ b2 (zee, stippel): `maak_havenaanloop.py` (timeout 300) vond bij 0,005°
#    kaal al een 0%-over-land-pad (118,6 km) maar werd bij het schrijven
#    door de timeout afgekapt (exit 124, geen bestand op schijf) — exact het
#    beeld uit de haalbaarheidstoets (>7 min, geen uitvoer). Geen tweede
#    poging (bakhandleiding §2): rechte stippel, reden "1:10M-kust kent de
#    haven niet". Zeeknoop 5303 is bindend uit de haalbaarheidstoets
#    (hecht_marnet.marnet_zee), 111,16 km van de kade.
# b3 (zee, MARNET, doorgetrokken): kade → kade, router kiest zelf
#    Mozambiquekanaal/Kaap of Malakka/Suez (geen vooraf geschatte km).
# b4-b6 (binnenvaart, doorgetrokken, LETTERLIJKE KOPIE van koper-lobito-
#    duisburg benen 5-7 in bak_koper_lobito() hierboven — zelfde GRAAF_RIJN,
#    zelfde geojson-bestand (`rivierbeen-wesel.geojson`), geen eigen versie
#    gebakken): Waalhaven → Emmerich-vak (161,1 km, AIS-graaf rijn) →
#    Wesel-vak (66,6 km, echte OSM-loop, geen AIS-dekking) → Duisport
#    Ruhrort (7,3 km, AIS-graaf rijn) = 235,0 km Rijn-segment.
# Geen fase D/E: thyssenkrupp Materials Trading heeft geen eigen coördinaat/
#    adres gevonden (brief §6/§7) — de brief en deze bake stoppen bij
#    Duisburg-Ruhrort Becken A (entrepot, stoppunt).
bak_grafiet_molo_duisburg() {
  # ⚠️ eigen graaf: deze stroom vaart de Rijn, niet de Mississippi (koper-lobito-patroon).
  local GRAAF_RIJN="v2/build-cache/ais/graaf/rijn"
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF_RIJN" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|SuperFlake-vlokgrafiet Molo-mijn → Toliara-kade (RN10 → RN7)|$BEEN/grafiet-molo-duisburg-weg-molo-toliara.geojson" \
    --stippel      "zee|haven-aanloop Toliara (schematisch — 1:10M-kust kent de haven niet)|-23.3778,43.6648|-22.8572,42.7368" \
    --been         "zee|zeeschip Toliara-kade → Rotterdam (Waalhaven) (Mozambiquekanaal/Kaap óf Malakka/Suez — MARNET kiest)|-22.8572,42.7368|51.8935,4.4585" \
    --been         "binnenvaart|containerbinnenschip Waalhaven → Emmerich-vak|51.8935,4.4585|51.754,6.366" \
    --been-geojson "binnenvaart|Wesel-vak — echte Rijnloop uit OSM (geen AIS-dekking: 0 van 35.237 tracks)|$BEEN/rivierbeen-wesel.geojson" \
    --been         "binnenvaart|containerbinnenschip Wesel-vak → Duisport Ruhrort|51.4,6.745|51.4518,6.7565" \
    --marker "Molo-mijn (NextSource) — SuperFlake-vlokgrafiet, mijn/laadplek|-24.0045,45.1244" \
    --marker "Toliara-kade — Port de Tuléar, overslag truck → zee|-23.3778,43.6648" \
    --marker "Rotterdam — RHB, Waalhaven Noordzijde 4 (gedeeld anker)|51.8935,4.4585" \
    --marker "Duisburg — Duisport Ruhrort, Becken A (gedeeld anker, stoppunt)|51.4518,6.7565" \
    --routebrief v2/design/routebrieven/grafiet-molo-duisburg.md \
    --uit    v2/data/stroomroute-grafiet-molo-duisburg.json \
    --stroom grafiet-molo-duisburg \
    --titel  "Grafiet · Molo (Madagaskar) → Toliara → Rotterdam → Duisburg"
}

# ── ree · OSCOM REEP (Chatrapur, Odisha) → RED Aluva (Udyogamandal, Kerala), India
# Routebrief: v2/design/routebrieven/ree-oscom-aluva.md (lichte werkwijze M31 golf 5)
# EÉN wegbeen (b1, truck, doorgetrokken, geen stippel): mixed rare earth chloride
# (MRCL) van de OSCOM-monazietextractie naar de RED Aluva-scheidingsfabriek, over
# NH-16 (Oostkust, via Vijayawada) → NH-544 (Salem-Kochi, via de Palakkad-gap) →
# NH-66 (Kerala-kust). Modaliteit truck is AANNEMELIJK (geen bron bevestigt hoe
# MRCL reist, brief §7); geen zee/spoor/leiding/lucht, geen fase D/E (brief §6:
# geen bron voor een afnemer van RED Aluva's HPRE-oxiden).
# ⚠️ Geen gepubliceerde wegkm (brief §7): hemelsbreed 1.386 km — de ±15%-toets
#    geldt hier alleen als INDICATIE, geen harde norm. Gemeten wegkm = 1.717,6 km
#    (+23,9% t.o.v. de indicatie, buiten zowel ±10% als ±15% — een BEVINDING, geen
#    fout: de brief voorzag zelf al 1.700-2.100 km voor de omweg door de Palakkad-
#    gap, en 1.717,6 valt daarbinnen).
# ⚠️ RED Aluva-anker gecorrigeerd bij het bakken (brief §3): de parallelle keten
#    ree-chavara-aluva (andere agent, zelfde M31 golf 5) legde onafhankelijk
#    hetzelfde IREL RED-terrein satelliet-gelegd op 10.08133/76.29761 — 190 m van
#    dit brief's oorspronkelijke, onzekere punt. Letterlijk hergebruikt (niet
#    stilzwijgend in het json, wél gedocumenteerd in de brief §3).
# ⚠️ Beide ankersnaps ruim binnen norm (plant→weg 0,00 km, weg→kade 0,11 km) —
#    geen last-mile-stippel nodig, ondanks de brief's verwachting dat er één zou
#    komen (OSCOM in bosrijk terrein, RED Aluva in dichte industriezone).
bak_ree_oscom_aluva() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|MRCL OSCOM REEP → RED Aluva (NH-16 → NH-544 → NH-66, via Vijayawada/Chengalpattu/Salem/Coimbatore/Walayar; aannemelijk: modaliteit ongedocumenteerd)|$BEEN/ree-oscom-aluva-weg-oscom-aluva.geojson" \
    --marker "ree-oscom-reep — OSCOM REEP, Chatrapur, Ganjam-district, Odisha — mijn/extractiefabriek (laadplek, bron-gelegd)|19.3261,84.9449" \
    --marker "ree-red-aluva — RED Aluva, Udyogamandal, Periyar-rivier, Kerala — scheidingsfabriek (losplek, stoppunt, bron-gelegd)|10.08133,76.29761" \
    --routebrief v2/design/routebrieven/ree-oscom-aluva.md \
    --uit    v2/data/stroomroute-ree-oscom-aluva.json \
    --stroom ree-oscom-aluva \
    --titel  "Zeldzame aardmetalen · OSCOM REEP (Odisha) → RED Aluva (Kerala, India)"
}

# ── zeldzame aardmetalen · Chemours Mission Mine (Georgia) → White Mesa Mill (Blanding, Utah)
# Routebrief: v2/design/routebrieven/ree-georgia-whitemesa.md (lichte werkwijze M31 golf 5)
# ⚠️ Eén been (b1, fase A, truck, aannemelijke modaliteit — brief §7: geen bron
#    bevestigt hoe déze 2.600+ km-rit precies verloopt). Geen gepubliceerde
#    wegkm (brief §2/§7): alleen hemelsbreed 2.620,4 km tussen de site-ankers.
#    Gemeten weggeometrie 3.518,0 km (+34,3% t.o.v. de hemelsbrede indicatie,
#    logisch voor een 2.600+ km I-40/US-corridor die niet de grootcirkel volgt)
#    — de lengtetoets is hier referentie, geen ±15%-norm (brief §2/§7).
# ⚠️ Profiel `ree-georgia-whitemesa-ga-utah` (maak_stroombeen_weg.py) draagt
#    TWEE via-punten die NIET in de brief-tabel (§4, 8 punten) staan: Shiprock
#    NM en Kayenta AZ, om het laatste stuk Gallup→White Mesa (~400 km, buiten
#    het 8-punten-budget van de brief) op US-491/US-160/163/191 te pinnen —
#    zie de kopnoot in het profiel + open punt 1 van bak_aanwijzingen. De brief
#    zelf is ONGEWIJZIGD gelaten (§4-tabel blijft 8 punten).
# ⚠️ Beide ankersnaps ruim binnen norm (plant→weg 0,07 km, weg→kade 0,36 km,
#    open punt 2 van bak_aanwijzingen) — GEEN last-mile-stippel nodig bij
#    Mission Mine, ondanks de brief's vermoeden dat de mijn "continu meebeweegt
#    met het ertslichaam" (§7). First mile 6,95 km over kleine wegklassen
#    (service/tertiary/track), last mile 1,67 km (service) — vandaar
#    eindKlassen incl. track + eindToegangPrivaat in het profiel.
# ⚠️ w-whitemesa is LETTERLIJK HERGEBRUIKT uit v2/design/ree-sitelaag.json —
#    niet opnieuw satelliet-gecheckt (brief §3).
bak_ree_georgia_whitemesa() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|monazietzand Chemours Mission Mine → White Mesa Mill (I-40 → US 491 → US 160/163 → US 191, hemelsbreed 2.620,4 km, geen wegkm; aannemelijk: modaliteit)|$BEEN/ree-georgia-whitemesa-weg-ga-utah.geojson" \
    --marker "ree-ga-mijn — Chemours Mission Mine, heavy-mineral-sand-mijn (Charlton County, Georgia) — mijn/laadplek, bron-gelegd|31.0276,-81.9772" \
    --marker "w-whitemesa — White Mesa Mill (Energy Fuels), Blanding, Utah — raffinaderij/losplek, stoppunt, bron-gelegd (hergebruikt anker)|37.5323,-109.5098" \
    --routebrief v2/design/routebrieven/ree-georgia-whitemesa.md \
    --uit    v2/data/stroomroute-ree-georgia-whitemesa.json \
    --stroom ree-georgia-whitemesa \
    --titel  "Zeldzame aardmetalen · Chemours Mission Mine (Georgia) → White Mesa Mill (Blanding, Utah)"
}

# ── lithium · Salar de Atacama → Carmen → Antofagasta → Daesan (Zuid-Korea, SK On/Seosan)
# Routebrief: v2/design/routebrieven/lithium-carmen-pohang.md (LICHTE werkwijze M31 golf 5)
# ⚠️ b1/b2 (truck) ZIJN LETTERLIJKE KOPIEËN van been 1/2 uit
#    stroomroute-lithium-atacama-antofagasta.json (profielen lithium-atacama-carmen /
#    lithium-carmen-antofagasta in maak_stroombeen_weg.py) — GEEN eigen wegscan,
#    zelfde geojson, geen tweede versie (brief §2 b1/b2, bakhandleiding §0.4).
# ⚠️ b3 (zee, haven-aanloop Antofagasta) IS OOK EEN LETTERLIJKE KOPIE — hetzelfde
#    gedeelde bestand als lithium-atacama-antofagasta/koper-aurubis-hamburg
#    (aanloop-antofagasta.geojson, 97,1 km, MARNET reikt hier niet tot de kade).
# ⚠️ b4 (zee, MARNET, NIEUW): Antofagasta-zeeknoop → Daesan-zeeknoop, andere lane
#    dan de bestaande Antofagasta→Yangtze-as (Stille Oceaan, geen zeestraat) —
#    hemelsbreed 17.827 km stond in de brief als schatting; MARNET bepaalt de
#    echte lane/km bij het bakken (bevinding, geen venster om dicht te trekken —
#    zie lithium-pilgangoora-gwangyang §9 voor het precedent).
# ⚠️ b5 (zee, haven-aanloop Daesan, NIEUW): Daesan-havenfront ligt 17,1 km van de
#    dichtstbijzijnde MARNET-zeeknoop (>5 km ⇒ verplichte haven-aanloop per
#    bakhandleiding §2/LAR-586, ook al zou de router binnen 25 km snappen).
#    maak_havenaanloop.py vond een pad over water (17,4 km, 16 punten, 0,00 km
#    over land, omwegfactor 1,017) — geen terugval-stippel nodig. De punten
#    van dat bestand zijn ná het bakken van de aanloop OMGEDRAAID (het tool
#    bouwt altijd kade→zeeknoop; deze keten reist zeeknoop→kade) zodat de lijn
#    in reisvolgorde ligt en de naadmeting niet vals uitslaat.
# ⚠️ GEEN fase D/E: de keten stopt bij li-daesan-kade — geen bron zegt dat SQM's
#    lading specifiek in Daesan wordt gelost of van daar naar Seosan rijdt
#    (bindende uitkomst van de haalbaarheidstoets, brief §6/§7 — het
#    oorspronkelijke Pohang-fabrieksanker is geschrapt).
bak_lithium_carmen_pohang() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|tankwagens SQM Salar de Atacama → PQL Carmen (plantweg → Ruta B-39 → Baquedano → Ruta 5) — LETTERLIJKE KOPIE lithium-atacama-antofagasta been b1|$BEEN/lithium-carmen-pohang-weg-atacama-carmen.geojson" \
    --been-geojson "truck|carbonaat/hydroxide (containers) PQL Carmen → Puerto Antofagasta ATI (Ruta 5 → Ruta 26 → Av. Salvador Allende) — LETTERLIJKE KOPIE lithium-atacama-antofagasta been b2|$BEEN/lithium-carmen-pohang-weg-carmen-antofagasta.geojson" \
    --stippel-geojson "zee|haven-aanloop Antofagasta (schematisch, over water — MARNET reikt hier niet: 97 km; gedeeld met lithium-atacama-antofagasta/koper-aurubis-hamburg — LETTERLIJKE KOPIE)|$BEEN/lithium-carmen-pohang-aanloop-antofagasta.geojson" \
    --been         "zee|zeeschip Antofagasta → Daesan (Stille Oceaan, andere lane dan de bestaande Antofagasta→Yangtze-as; hemelsbreed-schatting 17.827 km, MARNET bepaalt de echte lane)|-23.80,-71.30|37.16690,126.41420" \
    --stippel-geojson "zee|haven-aanloop Daesan (schematisch, over water — Daesan-havenfront ligt 17,1 km van de MARNET-zeeknoop, >5 km ⇒ verplichte haven-aanloop LAR-586)|$BEEN/lithium-carmen-pohang-aanloop-daesan.geojson" \
    --marker "SQM Salar de Atacama — lithiumplant (laadplek tankwagens, hergebruikt anker)|-23.5675,-68.4000" \
    --marker "SQM Planta Química de Litio Carmen — verwerkingsknoop (LiCl → Li2CO3/LiOH, hergebruikt anker)|-23.6335,-70.2600" \
    --marker "Puerto Antofagasta, ATI — kade (containers, hergebruikt anker)|-23.6500,-70.4088" \
    --marker "Daesan-havenfront, Seosan — algemene-vracht-/containerterminal (nieuw anker, satelliet-gecheckt), stoppunt|37.0131,126.4243" \
    --routebrief v2/design/routebrieven/lithium-carmen-pohang.md \
    --uit    v2/data/stroomroute-lithium-carmen-pohang.json \
    --stroom lithium-carmen-pohang \
    --titel  "Lithium · Salar de Atacama → Antofagasta → Daesan (Zuid-Korea)"
}

# ── lithium · Greenbushes-mijn (WA) → Kemerton lithium hydroxide plant (Albemarle)
# Routebrief: v2/design/routebrieven/lithium-greenbushes-kemerton.md (LICHTE werkwijze M31 golf 5).
# Eén enkel truckbeen (fase A), zoals lithium-silverpeak-mccarran — geen zee,
# geen haven-aanloop, geen spoor/leiding/binnenvaart. Deelt alleen het START-
# ANKER met lithium-greenbushes-bunbury (116.05505,-33.86495); ander eindpunt,
# dus GEEN gedeeld-been-kopie (het is een nieuw profiel, ~66 km overlapt
# corridormatig met de Bunbury-as maar dat is geen letterlijke kopie).
# ⚠️ Beennaam draagt "(aannemelijk: eigendomsrelatie, geen brondocument)" —
#    geen bron koppelt Greenbushes-concentraat specifiek aan Kemerton; de as
#    steunt uitsluitend op gedeeld eigendom (Albemarle 49% Greenbushes + 100%
#    Kemerton), zie brief §7. Kemerton's hydroxidetrein staat grotendeels
#    stil sinds 2026 (Albemarle-persbericht) — actueel volume onzeker/laag.
# ⚠️ Kemerton-coördinaat is de GEHARMONISEERDE waarde uit de sitelaag
#    (-33.2050,115.7604, brief §3) — 0,5 km van de negatieve-ankerwaarde in
#    lithium-greenbushes-zhangjiagang.md §2a-2, bewust niet die laatste.
# ⚠️ Geen gepubliceerde wegkm (brief §2): OSRM-routering 100,7 km als
#    werk-doelwaarde; de bake geeft 101,6 km getekend (102,1 km incl. de twee
#    korte anker-verbindingen plant→weg 0,06 km en weg→kade 0,45 km) — binnen
#    1,4% van de OSRM-waarde. ±15%-toets hier indicatie, geen norm.
bak_lithium_greenbushes_kemerton() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|spodumeenconcentraat Greenbushes-mijn → Kemerton lithium hydroxide plant (South Western Hwy N → Wilman Wadandi Hwy (Bunbury-omleiding) → Forrest Hwy N → Marriott Rd; aannemelijk: eigendomsrelatie, geen brondocument)|$BEEN/lithium-greenbushes-kemerton-weg-greenbushes-kemerton.geojson" \
    --marker "li-gb-laadplek — Greenbushes-concentraatloods (Talison: Tianqi/IGO 51% · Albemarle 49%), laadplek — hergebruikt anker|-33.86495,116.05505" \
    --marker "li-kemerton-fabriek — Kemerton lithium hydroxide plant (Albemarle 100%), stoppunt (hydroxidetrein grotendeels stilgelegd sinds 2026)|-33.2050,115.7604" \
    --routebrief v2/design/routebrieven/lithium-greenbushes-kemerton.md \
    --uit    v2/data/stroomroute-lithium-greenbushes-kemerton.json \
    --stroom lithium-greenbushes-kemerton \
    --titel  "Lithium · Greenbushes-mijn → Kemerton lithium hydroxide plant (West-Australië)"
}

# ── grafiet · Bogala-mijn (Sri Lanka) → Colombo → Hamburg → Hauzenberg (Duitsland)
# Routebrief: v2/design/routebrieven/grafiet-bogala-hauzenberg.md (LICHTE werkwijze M31 golf 5)
# b1 (truck, weg-geojson): Bogala-mijn → Jaya Container Terminal Colombo, lokale
#    weg → A1 via Kegalle-Warakapola-Nittambuwa-Kadawatha. 93,2 km gebakken
#    (geen gepubliceerde wegkm — hemelsbreed 54,0 km, alleen referentie).
# b2a (zee, STIPPEL, VERPLICHTE haven-aanloop LAR-586): de kade ligt 8,89 km van
#    MARNET-zeeknoop 5328, boven de 5 km-drempel, óók al snapt de router ruim
#    binnen 25 km. `maak_havenaanloop.py` liep vast op timeout 300 (exit 124) →
#    per bakhandleiding §2 GEEN tweede poging, terugval op een rechte stippel.
# b2b (zee, MARNET, geen stippel): Colombo → Hamburg, kade-coördinaten — de
#    router snapt zelf op zeeknoop 5328 (Colombo, 8,89 km, via de aanloop
#    hierboven overbrugd) resp. 3944 (Hamburg, 1,41 km, geen aanloop nodig).
# b3 (truck, weg-geojson): Hamburg Burchardkai → Graphit Kropfmühl Hauzenberg,
#    A7 → A3 → B12/lokale weg. 851,8 km gebakken (orde ~830-850 km verwacht).
# ⚠️ Anker-verbinding Hamburg-kant 0,62 km (> 0,5 km-norm, bevinding): het
#    dichtstbijzijnde OSM-punt bij Container Terminal Burchardkai (0,31 km) is
#    een geïsoleerd eiland van 20 terminal-service-knopen (2 ways, 0 verbinding
#    met het publieke wegnet) — gemeten met een BFS-componenttoets op de
#    gebakken graaf. Profiel-eindKlassen laat daarom bewust 'service' weg
#    (alleen residential/tertiary/unclassified); het anker snapt dan op 0,62 km
#    op een knoop in het hoofdcomponent (868.157 knopen) i.p.v. op het eiland.
# ⚠️ Geen fase D/E (brief §6): geen bron voor de afzet ná Hauzenberg-verwerking.
bak_grafiet_bogala_hauzenberg() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen Bogala-mijn → Jaya Container Terminal Colombo (lokale weg → A1 via Kegalle-Warakapola-Nittambuwa-Kadawatha)|$BEEN/grafiet-bogala-hauzenberg-weg-bogala-colombo.geojson" \
    --stippel      "zee|haven-aanloop Colombo (schematisch — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300/exit 124, geen tweede poging)|6.9449,79.8527|6.99460,79.78960" \
    --been         "zee|zeeschip Colombo → Hamburg (Indische Oceaan → Arabische Zee → Rode Zee → Suez → Middellandse Zee → Straat van Gibraltar → Golf van Biskaje → Het Kanaal → Noordzee → Elbe-estuarium)|6.9449,79.8527|53.5328,9.9223" \
    --been-geojson "truck|vrachtwagen Container Terminal Burchardkai → Graphit Kropfmühl GmbH Hauzenberg (A7 → A3 → B12/lokale weg; anker-verbinding Hamburg-kant 0,62 km, zie ⚠️-noot)|$BEEN/grafiet-bogala-hauzenberg-weg-hamburg-hauzenberg.geojson" \
    --marker "Bogala-mijn, Aruggammana, Kegalle District — ondergrondse ader-/klompgrafietmijn|7.1164,80.3106" \
    --marker "Jaya Container Terminal, Colombo — overslag truck → zee|6.9449,79.8527" \
    --marker "Container Terminal Burchardkai, Waltershof, Hamburg — overslag zee → truck|53.5328,9.9223" \
    --marker "Graphit Kropfmühl GmbH, Hauzenberg (Kropfmühl) — losplek/verwerker, stoppunt (Asbury Carbons Inc.)|48.6218,13.6599" \
    --routebrief v2/design/routebrieven/grafiet-bogala-hauzenberg.md \
    --uit    v2/data/stroomroute-grafiet-bogala-hauzenberg.json \
    --stroom grafiet-bogala-hauzenberg \
    --titel  "Grafiet · Bogala-mijn (Sri Lanka) → Colombo → Hamburg → Hauzenberg (Duitsland)"
}

# ── lithium · AMG Mibra-mijn/concentrator (Nazareno, Brazilië) → Porto de Vitória → Hamburg → AMG Lithium Bitterfeld-Wolfen (Duitsland)
# Routebrief: v2/design/routebrieven/lithium-mibra-bitterfeld.md (LICHTE werkwijze M31 golf 5)
# b1 (truck, weg-geojson): AMG Mibra-mijn/concentrator/chem.-conversieterrein
#    (Nazareno, MG) → BR-265 → MG-285/MG-447 → BR-356 → RJ-186 → ES-297 →
#    BR-101 → Porto de Vitória. 654,6 km gebakken tegen OSRM-wegreferentie
#    619,2 km (+5,8%, binnen ±10% — refs uitgebreid met RJ-186/ES-297 t.o.v.
#    de bak-aanwijzingen, anders koos de scanner zonder soft-preference op die
#    staatswegen een omweg van 742,4 km/+19,9% tussen Itaperuna en Itapemirim).
# ⚠️ b2 (zee, STIPPEL) is een LETTERLIJKE KOPIE van been b2 uit de gebakken
#    stroom lithium-cirilo-vitoria (functie bak_lithium_cirilo_vitoria,
#    102,7 km haven-aanloop Porto de Vitória → zeeknoop 900) — hetzelfde
#    geojson-bestand ($BEEN/lithium-cirilo-vitoria-aanloop-vitoria.geojson)
#    wordt hier rechtstreeks hergebruikt, GEEN nieuwe maak_havenaanloop.py-run.
# b3 (zee, MARNET, geen stippel): zeeknoop 900 (-20,00000/-39,50000) →
#    Hamburg CTB-kade. Geen tweede haven-aanloop nodig aan de Duitse kant: de
#    kade snapt op zeeknoop 3944 op 1,8 km (ruim < 5 km-drempel, bak-
#    aanwijzingen §"Zeeknoop-check gedaan").
# b4 (truck, weg-geojson): Hamburg CTB → A7 → A2 → A14 → B6/B185 → B183 →
#    AMG Lithium Bitterfeld-Wolfen (Areal A). 356,2 km gebakken tegen OSRM-
#    wegreferentie 362,7 km (-1,9%, binnen ±10%). `eindToegangPrivaat` nodig
#    aan de Hamburg-kop (containerterminal-toegangswegen, anders "geen
#    wegpad tussen punt 0 en 1" — airside/privéterrein-klasse, bakhandleiding §2).
# ⚠️ Geen fase D/E (brief §6): geen bron noemt een specifieke Europese
#    batterijfabriek als vaste afnemer van dit ronde; de brief stopt bij
#    battery-grade LiOH·H2O in Bitterfeld.
# ⚠️ Belangrijkste open punt (brief §7, GEEN bak-blokkade): een Fastmarkets-
#    citaat van AMG-CEO Fabiano Costa (juli 2025) suggereert dat de vandaag
#    werkelijk gevaren route mogelijk via China (tolling) loopt i.p.v.
#    rechtstreeks Mibra→Bitterfeld — deze brief tekent bewust de door de
#    haalbaarheidstoets opgedragen directe Atlantische as (geplande
#    eindketen); een vervolgronde zou een aparte keten lithium-mibra-china
#    moeten uitzoeken.
bak_lithium_mibra_bitterfeld() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "truck|vrachtwagen AMG Mibra-mijn/concentrator → São João del-Rei → Barbacena → Mercês → Cataguases → Muriaé → Itaperuna → Itapemirim → Porto de Vitória (LMG-841 → BR-265 → MG-285/MG-447 → BR-356 → RJ-186 → ES-297 → BR-101)|$BEEN/lithium-mibra-bitterfeld-weg-mibra-vitoria.geojson" \
    --stippel-geojson "zee|haven-aanloop Porto de Vitória (schematisch, over water — letterlijke kopie van been b2 uit lithium-cirilo-vitoria, 102,7 km, geen nieuwe run)|$BEEN/lithium-cirilo-vitoria-aanloop-vitoria.geojson" \
    --been         "zee|zeeschip Vitória → Hamburg (Zuid-Atlantische Oceaan → Noordzee, MARNET beslist; hemelsbreed ~9.446 km tussen de zeeknopen, geen zeekm-citaat)|-20.00000,-39.50000|53.5290,9.9278" \
    --been-geojson "truck|vrachtwagen HHLA Container Terminal Burchardkai → Wedemark → Lehrte → Peine → Hohe Börde → Bernburg → Südliches Anhalt → AMG Lithium Bitterfeld-Wolfen (A7 → A2 → A14 → B6/B185 → B183)|$BEEN/lithium-mibra-bitterfeld-weg-hamburg-bitterfeld.geojson" \
    --marker "li-mibra-plant — AMG Brasil, Mina/Complexo Volta Grande (Mibra), Nazareno MG — mijn + concentrator + chem.-conversieterrein|-21.0834,-44.5893" \
    --marker "li-vitoria-kade — Porto de Vitória, Vila Rubim/Cais Comercial (hergebruikt anker uit lithium-cirilo-vitoria)|-20.3238,-40.3477" \
    --marker "li-hamburg-ctb-kade — HHLA Container Terminal Burchardkai, Waltershofer Hafen, Hamburg|53.5290,9.9278" \
    --marker "li-bitterfeld-plant — AMG Lithium GmbH, Liebigstraße 10, Chemiepark Bitterfeld-Wolfen Areal A, stoppunt (battery-grade LiOH·H2O)|51.6522,12.2580" \
    --routebrief v2/design/routebrieven/lithium-mibra-bitterfeld.md \
    --uit    v2/data/stroomroute-lithium-mibra-bitterfeld.json \
    --stroom lithium-mibra-bitterfeld \
    --titel  "Lithium · AMG Mibra-mijn (Brazilië) → Porto de Vitória → Hamburg → AMG Lithium Bitterfeld-Wolfen (Duitsland)"
}

# ── gas · Kårstø (Noorwegen) → Dornum (Duitsland) ──────────────────────────
# Routebrief: v2/design/routebrieven/gas-karsto-dornum.md (M31 golf 5, lichte
# werkwijze). Eén been (fase B, leiding): Noors Noordzeegas wordt bij Kårstø
# behandeld en gaat via Europipe II naar de Gasempfangsanlage bij Dornum/Nesse
# (Duits invoedingspunt). Fase A (diffuus Statpipe-verzamelnet) vervalt bewust
# — geen enkelvoudig tracé, zoals de Amerikaanse schaliegasvelden elders.
#
# b1 — leiding, Kårstø → Dornum (Europipe II), DOORGETROKKEN, GEEN STIPPEL:
# ⚠️ De brief vroeg dit als open punt te verifiëren ("offshore-continuïteit
# NIET geverifieerd deze sessie") — pyosmium-scan op de extracts noorwegen +
# de-niedersachsen (extract-naam is `noorwegen`, niet `norwegen` zoals de
# brief schreef) vond een DOORLOPENDE keten van 7 exact aaneensluitende OSM-
# ways (gedeelde eindpunt-coördinaten, geen enkel gat): 1117764491 →
# 1117764494 → 1117764490 → 1117764492 → 523930562 → 174152562 (de lange
# offshore-hoofdway, 70 nodes, NO-landing → DE-landing) → 795944175. Alle
# dragen `man_made=pipeline`+`substance=gas`, vijf met naam-tag "Europipe II";
# 795944175 heeft geen eigen naam-tag maar sluit exact aan op 174152562 (zelfde
# coördinaat) en ligt tussen de DE-landing en de Dornum-aansluiting. Het
# OUDERE "Europipe" (I, way 174152545 + 1167437586, begint bij Draupner) is
# NIET meegenomen — aparte way-ids, geen overlap met de II-keten.
# Gestikte lengte: 655,77 km (181 punten) — tegen ~670 km (Engelse Wikipedia,
# 13+642+15) is dat −2,1%, tegen de Duitse Wikipedia's ruwe "~660 km" −0,6%;
# beide binnen de indicatieve marge (de brief noemt ±15% hier indicatief, geen
# harde norm, gezien de vooraf onbevestigde offshore-continuïteit — die is nu
# alsnog bevestigd). Marge kop-anker → eerste stitch-punt 0,94 km, staart-
# anker → laatste stitch-punt 0,16 km — beide < 5 km, dus geen losse stippel
# nodig (anker ≠ routeerpunt, bakhandleiding §5).
# Eén marker-paar: gas-karsto-plant (kop) en gas-dornum-netra (staart,
# stoppunt). Geen zee/haven-aanloop (geen zeebeen), geen luchtbeen, geen
# gedeeld been (geen andere stroom deelt dit tracé).
bak_gas_karsto_dornum() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "leiding|Europipe II Kårstø → Dornum (13 km onshore NO + ~642 km offshore NO/DK/DE-sector + 15 km onshore DE, gestikt uit 7 aaneensluitende OSM-ways man_made=pipeline)|$BEEN/gas-karsto-dornum-leiding-karsto-dornum.geojson" \
    --marker "gas-karsto-plant — Kårstø-gasbehandelingsanlegg (Equinor/Gassco), Tysvær|59.2774,5.5247" \
    --marker "gas-dornum-netra — Gasempfangsanlage/Heizhaus Europipe (Open Grid Europe/Gasunie Deutschland), Dornum/Nesse — stoppunt|53.6564,7.4039" \
    --routebrief v2/design/routebrieven/gas-karsto-dornum.md \
    --uit    v2/data/stroomroute-gas-karsto-dornum.json \
    --stroom gas-karsto-dornum \
    --titel  "Gas · Kårstø (Noorwegen) → Dornum (Duitsland) — Europipe II"
}

# ── gas · Hides Gas Conditioning Plant (Papoea-Nieuw-Guinea) → PNG LNG-plant Caution Bay → Futtsu LNG-terminal (Japan)
# Routebrief: v2/design/routebrieven/gas-cautionbay-futtsu.md (lichte werkwijze M31 golf 5) — de
# eerste keten van de atlas in Papoea-Nieuw-Guinea.
# ⚠️ b1 (leiding, STIPPEL, rechte lijn) heeft GEEN geometrie-bewijs voor het
#    tracé zelf — de PNG-Geofabrik-extract is gescand in de haalbaarheidstoets
#    (bindend): 112 man_made=pipeline-ways totaal, precies 1 (3 nodes,
#    ongenoemd) met substance=gas — het ~700 km-tracé Hides→Caution Bay
#    (ExxonMobil corporate: "approximately 700-kilometers of onshore and
#    offshore pipeline"; onafhankelijke bron 292 km onshore + 407 km offshore
#    = 699 km, brief §8[6][9]) is in OSM vrijwel niet gekarteerd. Alleen kop
#    (gas-cbf-hides) en staart (gas-cbf-plant) zijn bron-gelegd; de stippel is
#    een rechte koorde en ligt daarmee fors korter dan de werkelijke offshore-
#    boog door de Golf van Papoea — dat is INHERENT aan een schematische
#    stippel (kop-staart, geen geometrie-bewijs) en géén fout. Dit ene been
#    maakt de keten als geheel niet grotendeels-stippel: de zeeroute is
#    verreweg het grootste deel van de totale lengte (vergelijk Bingham
#    Canyon → Garfield, golf 4, dat wél 100% stippel werd en is afgewezen).
# ⚠️ b2 (zee, MARNET kade → kade) draagt een VERPLICHTE haven-aanloop op BEIDE
#    uiteinden (LAR-586, eigen meting): Caution Bay ligt 39,3 km van zeeknoop
#    5906 (-9,60080/147,26620) — buiten het 25 km-snapbereik —
#    `maak_havenaanloop.py` SLAAGDE (cel 0,01° kaal: 48,2 km · 34 punten ·
#    2,46 km over land, alle bij het kade-uiteinde — een kade ligt per
#    definitie óp de 1:10M-kustlijn, geen fout). Futtsu ligt 12,1 km van
#    zeeknoop 9066 (35,23890/139,79280) — binnen 25 km maar boven de 5 km-
#    drempel, dus ook hier verplicht; SLAAGDE eveneens (cel 0,01° gebufferd:
#    14,8 km · 12 punten · 0,90 km over land). Hoofdzeebeen tussen de twee
#    zeeknopen: Golf van Papoea → Coral Sea/Bismarckzee → Filipijnenzee
#    (langs Luzon/Taiwan) → Oost-Chinese Zee → Tokiobaai, geen Kaap-omweg.
#    Km-indicatie hemelsbreed ~5.026 km, geen gepubliceerde scheepvaart-
#    kilometrage gevonden (brief §2/§7) — geen harde ±15%-toets, alleen ter
#    indicatie (zelfde klasse als gas-raslaffan-chiba).
# ⚠️ Geen fase D/E: geen bron benoemt een specifieke fabriek/afnemer
#    stroomafwaarts van Futtsu (brief §6/§7). Futtsu blijft "aannemelijk: één
#    bron" — de 2010-afnemerscontracten noemen JERA/Tokyo Electric Power
#    Company en Osaka Gas als afnemers van PNG LNG in het algemeen, geen bron
#    koppelt een specifieke lading aan specifiek Futtsu. Het w-futtsu-anker is
#    letterlijk hergebruikt uit `v2/design/gas-sitelaag.json` (status daar al
#    aannemelijk, geen eigen satellietronde deze sessie).
# ⚠️ Geen luchtbeen, geen via-punten, geen gedeeld been met een bestaande
#    gas-keten (beide benen zijn nieuw voor deze stroom).
bak_gas_cautionbay_futtsu() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "leiding|Hides→Caution Bay pijpleiding (schematisch — geen doorlopende OSM-way; PNG-extract: 112 pipeline-ways, 1 met substance=gas)|-6.0050,142.8100|-9.3417,147.0231" \
    --stippel-geojson "zee|haven-aanloop Caution Bay (schematisch, over water — kade 39,3 km van de MARNET-zeeknoop)|$BEEN/gas-cautionbay-futtsu-aanloop-cautionbay.geojson" \
    --been         "zee|LNG-tanker Caution Bay → Futtsu (Golf van Papoea → Coral Sea/Bismarckzee → Filipijnenzee (Luzon/Taiwan) → Oost-Chinese Zee → Tokiobaai)|-9.60080,147.26620|35.23890,139.79280" \
    --stippel-geojson "zee|haven-aanloop Futtsu (schematisch, over water — kade 12,1 km van de MARNET-zeeknoop)|$BEEN/gas-cautionbay-futtsu-aanloop-futtsu.geojson" \
    --marker "gas-cbf-hides — Hides Gas Conditioning Plant, Southern Highlands (ExxonMobil PNG LNG) — laadplek/kop leiding, bron-gelegd|-6.0050,142.8100" \
    --marker "gas-cbf-plant — PNG LNG-plant, Caution Bay (ExxonMobil PNG Limited) — overslag leiding → zee, bron-gelegd|-9.3417,147.0231" \
    --marker "w-futtsu — Futtsu LNG-terminal (JERA/Tokyo Electric) — losplek zee, regasificatie + invoeding, stoppunt, aannemelijk|35.3424,139.8322" \
    --routebrief v2/design/routebrieven/gas-cautionbay-futtsu.md \
    --uit    v2/data/stroomroute-gas-cautionbay-futtsu.json \
    --stroom gas-cautionbay-futtsu \
    --titel  "Gas · Hides (Papoea-Nieuw-Guinea) → Caution Bay → Futtsu (Japan)"
}

# ── gas · Hassi R'Mel-gasveld (Algerije) → Arzew LNG-complex → Barcelona (Spanje)
# Routebrief: v2/design/routebrieven/gas-arzew-barcelona.md (lichte werkwijze M31 golf 5) —
# de eerste korte Middellandse-Zee-as van de kaart.
# ⚠️ b1 (leiding, fase A, GROTENDEELS DOORGETROKKEN) is gebouwd met een
#    TOPOLOGISCHE COMPONENT-GRAAF over ALLE 794 man_made=pipeline
#    substance=gas-ways in de lokale algerije-extract (pyosmium, gedeelde
#    OSM-node-refs — zelfde methode als bak_gas_bonny_zeebrugge b2, maar hier
#    WEL verbonden; gereedschap: v2/tools/maak_leidingbeen_gas_hassirmel_arzew.py).
#    Krechba-In Salah (way 391023450) en GALSI (ways 225282712/379118070/
#    1393655399) zijn hard uitgesloten op way-id (brief §7, bewezen verkeerde
#    corridor). De grootste component die BEIDE ankers benadert (775 vertices,
#    namen "Houd El Hamra"/"LZ2") ligt 7,3 km van Hassi R'Mel en 1,5 km van
#    Arzew — de Dijkstra daarbinnen geeft een doorlopend pad van 496,0 km
#    (288 punten, omwegfactor 1,112 t.o.v. de hemelsbrede 446,2 km; brief-
#    schatting was ~400 km hemelsbreed — indicatie, geen harde norm, brief
#    §7). GK3-Borg Chegga (ways 469395884/469395885/485487144) ligt NIET op
#    het gevonden pad (script-uitvoer bevestigt dit expliciet) — de
#    oostwaartse richting die de brief al vermoedde, dus terecht niet
#    meegenomen. De twee resterende gaten (veldterrein Hassi R'Mel 7,3 km;
#    complexterrein Arzew 1,5 km) hebben geen OSM-way en worden gestippeld
#    met reden — b1 is dus ~98% doorgetrokken, niet de 100%-stippel-klasse
#    van Bingham Canyon → Garfield (golf 4, afgewezen).
# ⚠️ b2a/b2b (zee, haven-aanlopen, LAR-586 — beide kades > 5 km van hun
#    zeeknoop): Arzew (10,35 km van zeeknoop 9074) — `maak_havenaanloop.py`
#    SLAAGDE (cel 0,005° kaal: 11,6 km · 21 punten · 0,80 km over land, geheel
#    bij het kade-uiteinde — een kade ligt per definitie óp de 1:10M-kustlijn).
#    Barcelona (5,09 km van zeeknoop 3723) — `maak_havenaanloop.py` liep vast
#    op `timeout 300` (exit 124), geen tweede poging (bakhandleiding §2) →
#    rechte stippel.
# ⚠️ b2 (zee, MARNET knoop→knoop) is de doorgetrokken hoofdroute zeeknoop 9074
#    → zeeknoop 3723 door de westelijke Middellandse Zee, rechtstreeks (geen
#    zeestraat); geen gepubliceerde routelengte, hemelsbreed ~650 km uit het
#    ontwerp is de enige referentie (indicatie, geen harde norm).
# ⚠️ Geen fase C/D/E (brief §6): geen bron bevestigt welke van Spanje's zeven
#    regasterminals het Arzew-volume daadwerkelijk ontvangt — Barcelona is het
#    enige Algerije-relevante sitelaag-anker in Spanje en blijft "aannemelijk:
#    één bron" (stoppunt). Geen luchtbeen, geen via-punten, geen gedeeld been
#    met een bestaande stroom.
bak_gas_arzew_barcelona() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --stippel      "leiding|gasveld-verzamelnet Hassi R'Mel → trunkleiding (schematisch — geen OSM-way op het veldterrein, 7,3 km)|32.94722,3.17056|32.94554,3.24879" \
    --been-geojson "leiding|Houd El Hamra-trunkleiding Hassi R'Mel → Arzew (aannemelijk: exacte way-keten bake-werk, component-graaf op gedeelde OSM-nodes, 496,0 km)|$BEEN/gas-arzew-barcelona-leiding-hassirmel-arzew.geojson" \
    --stippel      "leiding|trunkleiding → Arzew LNG-complex (schematisch — geen OSM-way op het complexterrein, 1,5 km)|35.79427,-0.24124|35.80780,-0.23950" \
    --stippel-geojson "zee|haven-aanloop Arzew (schematisch, over water — kade 10,35 km van de MARNET-zeeknoop)|$BEEN/gas-arzew-barcelona-aanloop-arzew.geojson" \
    --been         "zee|LNG-carrier Arzew → Barcelona (westelijke Middellandse Zee, rechtstreeks)|35.85230,-0.13870|41.31220,2.20940" \
    --stippel      "zee|haven-aanloop Barcelona (schematisch — 1:10M-kust kent de haven niet; maak_havenaanloop.py timeout 300 s, geen tweede poging)|41.31220,2.20940|41.34050,2.16150" \
    --marker "gas-hassirmel-veld — Hassi R'Mel-gasveld (Sonatrach) — gasveld/kop leiding, bron-gelegd|32.94722,3.17056" \
    --marker "gas-arzew-laad — Arzew LNG-complex (GL1Z/GL2Z/GL3Z, Sonatrach) — laadplek/LNG-liquefactie, bron-gelegd|35.80780,-0.23950" \
    --marker "gas-barcelona-los — Planta de Barcelona (Enagás), Zona Franca — losplek/LNG-regasificatie, stoppunt, aannemelijk|41.34050,2.16150" \
    --routebrief v2/design/routebrieven/gas-arzew-barcelona.md \
    --uit    v2/data/stroomroute-gas-arzew-barcelona.json \
    --stroom gas-arzew-barcelona \
    --titel  "Gas · Hassi R'Mel (Algerije) → Arzew → Barcelona (Spanje)"
}

# ── gas · Chajanda-gasveld (Jakoetië, Rusland) → Сила Сибири → RU/CN-grens → 中俄东线 → Nantong (China)
# Routebrief: v2/design/routebrieven/gas-chayanda-shanghai.md (LICHTE werkwijze M31 golf 5)
# Eerste volledig-leiding gas-keten zonder zee-leg — 3 benen, alle modaliteit leiding.
# ⚠️ b1 (fase A, DOORGETROKKEN): OSM-pipeline way-stitch, extract rusland-verrehoosten,
#    "Сила Сибири", 10 aaneengeschakelde ways (van de 14 kandidaat-way-id's uit de
#    brief bleken 4 korte parallel-/spurstukken bij compressorstations te zijn, niet
#    nodig voor een doorlopende keten — pyosmium-graaf op endpoint-matching bevestigt
#    een sluitende, gatloze verbinding zonder die 4). Veld → RU-grensstation, 2.153,8 km
#    (was in de brief 2.168,2 km met alle 14) — bevinding, geen via-punt-gesleep. Tegen
#    "±3.000 km algemeen bekend" (Gazprom, ongemeten) blijft dit −28,2%: OSM-geometrie is
#    een volledige gesloten keten van veld tot grensstation, dus vertrouwd. Naad met het
#    veld-anker 2,7 km (binnen de norm, geen actie).
# ⚠️ b2 (fase B, STIPPEL, ~3,2 km): Amoer-onderdoorgang, dubbele tunnel gereed 2019 —
#    geen doorlopende OSM-way over de rivier binnen het webbudget, ondanks gedocumenteerde
#    fysieke tunnel (Wikipedia). Rechte lijn tussen de twee OSM-way-eindpunten.
# ⚠️ b3 (fase C, China): 6 benoemde clusters, DOORGETROKKEN, 1.062,4 km samen, met 5
#    tussenliggende stippels (gaten 141,7 · 85,0 · 317,4 · 524,4 · 331,3 km — verdeeld
#    over de gap-zones, GEEN grote rechte stippel voor de hele 5.111 km, conform het
#    gas-karsto-dornum-patroon). Vóór het stikken een BREDERE pyosmium-scan zonder
#    naamfilter gedraaid (bakhandleiding §2 optie a): dat vond 3 extra benoemde
#    "中俄东线"-ways (1328499370/376/377) die de Qinhuangdao/Tangshan-cluster en de
#    losse 1336781081-cluster tot ÉÉN doorlopende cluster van 160,8 km samensmeden
#    (naden 0,66–1,22 km) — een echte verbetering t.o.v. de brief, geen aanname.
#    De aftakking 长岭-长春支线 (way 1328499381) is NIET meegenomen (expliciet een
#    zijtak, eigen naam-tag). Way 1328499383 (tiny, 2,3–2,8 km van de Changchun-cluster)
#    is een losse afsluiter-stub, geen brug over het gat — niet meegenomen.
#    Cluster "shenyang" en "nantong" zijn omgekeerd t.o.v. hun OSM-node-volgorde om
#    Noord→Zuid te lopen; "nantong" eindigt exact op het Nantong-anker (stoppunt).
# ⚠️ Haalbaarheid (§0 in de brief): b3 alléén is 43,1% doorgetrokken / 56,9% stippel,
#    maar de HELE keten (b1+b2+b3 samen) is 69,6% doorgetrokken / 30,4% stippel — dus
#    NIET de Bingham-Garfield-klasse (100% stippel); haalbaar.
# Geen via-punten (leiding volgt de exacte OSM-geometrie), geen fase D/E (brief §6: de
# brief stopt bewust bij het Nantong-anker, geen bron voor een Shanghai-invoedpunt).
bak_gas_chayanda_shanghai() {
  python v2/tools/hecht_marnet.py route \
    --graaf  "$GRAAF" \
    --marnet "$MARNET" \
    --ne     "$NE" \
    --been-geojson "leiding|Сила Сибири Chajanda-veld → RU-grensstation (10 aaneengeschakelde OSM-ways, 2.153,8 km)|$BEEN/gas-chayanda-shanghai-leiding-chayanda-rugrens.geojson" \
    --stippel      "leiding|Amoer-onderdoorgang (dubbele tunnel, gereed 2019, schematisch — geen doorlopende OSM-way over de rivier)|50.3116,127.3921|50.2926,127.3573" \
    --been-geojson "leiding|中俄东线, cluster CN-grens → Changchun-omgeving (2 ways, 571,7 km)|$BEEN/gas-chayanda-shanghai-leiding-cn-cn-grens-changchun.geojson" \
    --stippel      "leiding|中俄东线, tussenstuk Changchun-omgeving → Changchun-Shenyang-cluster (schematisch — geen doorlopende naam-tag)|45.7437,124.9734|44.5561,124.3182" \
    --been-geojson "leiding|中俄东线, cluster Changchun → Shenyang-omgeving (140,7 km)|$BEEN/gas-chayanda-shanghai-leiding-cn-changchun-shenyang.geojson" \
    --stippel      "leiding|中俄东线, tussenstuk Shenyang-omgeving (schematisch — geen doorlopende naam-tag)|43.4515,123.6469|42.6992,123.4625" \
    --been-geojson "leiding|中俄东线, cluster Shenyang-omgeving (27,1 km)|$BEEN/gas-chayanda-shanghai-leiding-cn-shenyang-cluster.geojson" \
    --stippel      "leiding|中俄东线, tussenstuk Shenyang → Qinhuangdao/Tangshan (schematisch — geen doorlopende naam-tag, 317,4 km)|42.4974,123.3092|40.5257,120.5529" \
    --been-geojson "leiding|中俄东线, cluster Qinhuangdao/Tangshan (7 ways incl. 3 extra uit de brede scan, 160,8 km)|$BEEN/gas-chayanda-shanghai-leiding-cn-qinhuangdao-tangshan.geojson" \
    --stippel      "leiding|中俄东线, tussenstuk Qinhuangdao/Tangshan → Linyi/Rizhao (schematisch — geen doorlopende naam-tag, 524,4 km)|39.9265,119.1499|35.2410,118.4750" \
    --been-geojson "leiding|中俄东线, cluster Linyi/Rizhao (6 ways, 136,8 km)|$BEEN/gas-chayanda-shanghai-leiding-cn-linyi-rizhao.geojson" \
    --stippel      "leiding|中俄东线, tussenstuk Linyi/Rizhao → Nantong (schematisch — geen doorlopende naam-tag, 331,3 km)|34.3931,119.0752|31.9325,121.0831" \
    --been-geojson "leiding|中俄东线, cluster Nantong-eindpunt (5 ways, 25,4 km, eindigt op het stoppunt)|$BEEN/gas-chayanda-shanghai-leiding-cn-nantong.geojson" \
    --marker "gas-chayanda-veld — Chajanda-gasveld, centrale gasbehandelingsinstallatie (Gazprom) — veld/kop leiding, bron-gelegd|60.3545,111.7086" \
    --marker "gas-ru-grensstation — compressor-/afsluiterstation aan de Amoer, Amoergebied (~20 km NW van Blagovesjtsjensk) — grensovergang RU-zijde, bron-gelegd|50.3116,127.3921" \
    --marker "gas-cn-grensstation — leidingstation aan de Amoeroever tegenover Blagovesjtsjensk, Heilongjiang — grensovergang CN-zijde, bron-gelegd|50.2926,127.3573" \
    --marker "gas-nantong-eindpunt — laatste benoemde leidingpunt 中俄东线, Nantong-gebied, Jiangsu — stoppunt, bron-gelegd|31.7231,121.0591" \
    --routebrief v2/design/routebrieven/gas-chayanda-shanghai.md \
    --uit    v2/data/stroomroute-gas-chayanda-shanghai.json \
    --stroom gas-chayanda-shanghai \
    --titel  "Gas · Chajanda-gasveld (Jakoetië) → Сила Сибири → 中俄东线 → Nantong (China)"
}

# ── NIEUWE STROOMFUNCTIES HIERBOVEN INVOEGEN (vóór de dispatch) ──
# Generieke dispatch (2026-09-26): het argument `<grondstof>-<slug>` wordt de
# functie `bak_<grondstof>_<slug>` (streepje → underscore). Een nieuwe stroom
# vraagt dus alleen een functie hierboven, geen regel hier.
arg="${1:-}"; naam="bak_${arg//-/_}"   # ${1:-} eerst: zonder argument geeft set -u anders "unbound variable"
if [ -n "${1:-}" ] && declare -F "$naam" >/dev/null; then "$naam"
else echo "gebruik: bash v2/tools/bak_stromen.sh <stroom>; bekend:" >&2
     declare -F | sed -n 's/^declare -f bak_//p' | tr '_' '-' >&2; exit 2; fi
