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

# ── NIEUWE STROOMFUNCTIES HIERBOVEN INVOEGEN (vóór de dispatch) ──
# Generieke dispatch (2026-09-26): het argument `<grondstof>-<slug>` wordt de
# functie `bak_<grondstof>_<slug>` (streepje → underscore). Een nieuwe stroom
# vraagt dus alleen een functie hierboven, geen regel hier.
arg="${1:-}"; naam="bak_${arg//-/_}"   # ${1:-} eerst: zonder argument geeft set -u anders "unbound variable"
if [ -n "${1:-}" ] && declare -F "$naam" >/dev/null; then "$naam"
else echo "gebruik: bash v2/tools/bak_stromen.sh <stroom>; bekend:" >&2
     declare -F | sed -n 's/^declare -f bak_//p' | tr '_' '-' >&2; exit 2; fi
