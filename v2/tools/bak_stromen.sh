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
# Draaien vanuit de repo-root:
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

# ⚠️ OPENSTAAND: de recepten van de twee ANDERE stromen (koper Collahuasi→
# Tongling, lithium) staan hier nog NIET. Die zijn
# gebakken vóór dit bestand bestond en hun vlaggen leven nog in een
# shell-historie. Reconstrueer ze bij de eerstvolgende herbake van elk — en
# herbak ze niet zonder eerst de huidige uitvoer te bewaren, want net als bij
# Balama→Nacala kan het gereedschap intussen veranderd zijn.
#
# ⚠️ REPRODUCEERBAARHEID IS BEGRENSD DOOR v2/.gitignore (build-cache/): $GRAAF,
# $MARNET, $NE en alle --been-geojson-bestanden zijn ONGETRACKT. Op een verse
# clone draait geen van deze recepten. Geldt even hard voor bak_grafiet.

case "${1:-}" in
  grafiet)         bak_grafiet ;;
  koper-escondida) bak_koper_escondida ;;
  koper-lobito)    bak_koper_lobito ;;
  *) echo "gebruik: bash v2/tools/bak_stromen.sh {grafiet|koper-escondida|koper-lobito}" >&2; exit 2 ;;
esac
