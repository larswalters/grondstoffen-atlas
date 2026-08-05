#!/usr/bin/env python3
"""
maak_stroombeen_weg.py — het TRUCKBEEN Balama-plant → Nacala-kade als échte
weggeometrie (N380/N1/N12) voor de stroomlaag.

WAT. Routebrief grafiet-balama-vidalia, been 1: de keten begint niet op zee
maar bij de mijn — "het begint niet echt bij de mijn — dat is wel belangrijk"
(Lars, 2026-07-28). Dit tool bakt dat been één keer als GeoJSON-LineString
([lon, lat]) zodat `hecht_marnet.py route --been-geojson` hem als
DOORGETROKKEN been in het stroomcontract opneemt (geen routering daar, geen
stippel — de geometrie komt letterlijk uit dit bestand).

HOE. Exact dezelfde machinerie als de M25-wegcorridors, geïmporteerd uit
fetch_landnet (niets gedupliceerd):
  * het wegfilter `weg_houden()`/WEG_HOUD via `land_scan(modus="weg")` —
    motorway t/m secondary, bewust ruim: de scope komt van het VENSTER,
    niet van de tag (highway=motorway is 0 km in half Afrika);
  * het corridorvenster om anker → via-punten → anker (⚠️ het venster ligt
    om de VIA-PUNTEN, niet om de grootcirkel — de corridor_punten()-les van
    Kolwezi→Durban); hier straal 40 km;
  * `corridor_keten()`: Dijkstra per been langs de via-punten uit de
    routebrief (in reisvolgorde), refs als záchte voorkeur (factor 3),
    anker-snap ≤ 25 km per punt.

⚠️ DIT IS TEKENGEOMETRIE VOOR DE STROOMLAAG, GEEN LANDNET. De lijn gaat naar
v2/build-cache/ais/graaf/ en wordt door hecht_marnet als been meegebakken;
hij komt NIET in landnet.bin en NIET in de CORRIDORS-lijst op schijf — de
runtime-vervanging hieronder raakt geen enkele bestaande bake of cache.
⚠️ CACHEVINGERAFDRUK: fetch_landnet hasht WEG_HOUD en de corridorlijst
(id + punten + vensterKm) mee, maar NIET een runtime-gepatchte weg_houden.
Daarom draagt het corridor-id dat de scan ziet een eigen
eindklassen-marker (zie main): de M25-caches blijven onaangeraakt én een
oudere cache van dit tool (ander filter of andere kade) kan nooit
stilzwijgend hergebruikt worden.

⚠️ LENGTETOETS = RAPPORTEREN, NIET GLADSTRIJKEN. De brief zegt ~485 km
(ESIA-som; gepubliceerd 490-515). Binnen ±10% is goed; erbuiten is een
bevinding die blijft staan — geen via-punt bijschuiven om het getal te halen.

⚠️ HET EERSTE VIA-PUNT IS DE PLANT, NIET HET DORP. Balama-dorp ligt ~9 km
WZW van de plant (briefpunt 2, "referentie — niet aan lijn"); de route start
op de site (-13.310, 38.660).

⚠️ HET LAATSTE VIA-PUNT IS DE CONTAINERTERMINAL OP DE OOSTOEVER (correctie
Lars, satelliet-check ?v=093). Het onderzoekspunt (-14.531, 40.652) bleek op
open water bij de kolen-jetty op de WESTOEVER te liggen — nota bene het
terminal dat in de routebrief als "hoort NIET bij deze stroom" staat. Het
nieuwe anker (-14.5383, 40.6673) is satelliet-gelegd op de containerkade
(Esri z16, 0,01-graden-grid — de Tongling-werkwijze).

⚠️ KLEINE WEGKLASSEN DOEN MEE, MAAR ALLEEN BIJ DE UITEINDEN. Gemeten in de
bron (2026-07-28): met alléén WEG_HOUD (motorway t/m secondary) eindigt de
weg 3,8 km van de plant (N14/N380 bij Balama) en blijft het laatste stuk een
rechte lijn dwars over het mijnterrein — "dat laatste stukje gaat niet over
de weg" (Lars). De echte toegangsweg bestaat wél in OSM maar draagt een
kleinere klasse: `unclassified` op 0,39 km van de plant, en bij Nacala liggen
de havenstraten als `service`/`residential`. Daarom accepteert deze run óók
EIND_KLASSEN (tertiary/unclassified/residential/service) — maar uitsluitend
binnen EIND_STRAAL_KM van de plant resp. de kade, NIET corridor-breed: anders
trekt elk dorpsspoor het venster in en kan een bush-track (zachte
ref-voorkeur is maar factor 3) de N1 aftroeven. De hoofdroute blijft zo op de
N-wegen; alleen de first/last mile pakt de echte toegangsweg. De resterende
anker-verbindingsstukjes (anker → dichtstbijzijnde wegvertex) horen daarmee
≤ ~0,5 km per kant te zijn; ze blijven apart gerapporteerd (`kmAanloopVan`/
`kmAanloopNaar`) en tellen NIET mee in de lengtetoets, die uitsluitend over
de weggeometrie gaat. Zelfde patroon als de slurryleiding waarvan de
kartering 736 m vóór het terminalvlak ophoudt: het restje is een getekende
verbinding, geen gemeten weg.

Bijvangst uit de meting: de N380 draagt in OSM tussen Balama en Montepuez de
ref `N14` (hernummering); die zit daarom in de zachte ref-voorkeur.

Draaien:
  python v2/tools/maak_stroombeen_weg.py
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fetch_landnet as fl  # noqa: E402 — weg_houden/venster/corridor_keten
import fetch_waterways as fw  # noqa: E402 — km()

# ── PROFIELEN ─────────────────────────────────────────────────────────────
# Eén profiel per truckbeen uit een routebrief. Kies met --profiel; de default
# is het oorspronkelijke grafietbeen, zodat een herbake daarvan onveranderd
# blijft. Coördinaten (lon, lat) zoals overal in fetch_landnet.CORRIDORS;
# namen alleen voor de rapportage. Zet een nieuw been HIER neer en niet in een
# kopie van dit bestand: een gekopieerd recept loopt stil uit de pas (de
# generator-driftles van cu-guixi-spoor, 741 m).
PROFIELEN = {
    "grafiet-balama-nacala": {
        "via": [
            ("Balama-plant",        (38.660,  -13.310)),
            ("Montepuez",           (39.0017, -13.1253)),
            ("Metoro (N380×N1)",    (39.873,  -13.104)),
            ("Ocua / Lúrio-brug",   (39.793,  -13.6451)),
            ("Namialo (N1×N12)",    (39.9882, -14.9231)),
            ("Monapo",              (40.2972, -14.9155)),
            # ⚠️ Satelliet-gelegd op de containerterminal-OOSToever (Esri z16,
            # 0,01°-grid) — correctie Lars: het onderzoekspunt (40.652,
            # -14.531) bleek in het water bij de kolen-jetty op de westoever te
            # liggen (het terminal dat per routebrief NIET bij deze stroom
            # hoort). Hier komen de trucks aan.
            ("Nacala-kade",         (40.6673, -14.5383)),
        ],
        "id": "gr-balama-nacala",
        "naam": "Balama-plant → Porto de Nacala (N380/N1/N12)",
        "extracts": ["mozambique"],
        # Zachte voorkeur (factor 3), géén filter: de brief noemt N380
        # (ex-EN242), N1 en EN8/N12; OSM-Mozambique wisselt tussen N- en
        # EN-schrijfwijzen en draagt op Balama–Montepuez de hernummerde ref N14.
        "refs": ["N380", "N14", "EN242", "N1", "EN1", "N12", "EN8", "N8"],
        "gepubliceerdKm": 485,
        "bronnoot": "ESIA-som; gepubliceerd 490-515",
        "vensterKm": 40,
        "uit": "stroombeen-balama-nacala.geojson",
    },
    # Routebrief lithium-greenbushes-zhangjiagang, benen 1 + 2. ⚠️ De trucks
    # gaan eerst NOORDWAARTS over Maranup Ford Road en Stanifer Street dwars
    # door het dorp Greenbushes; de South Western Highway loopt ÓÓSTELIJK langs
    # de mijn, niet westelijk (OSM way 850831840 e.v.). Dat komt overeen met
    # Talisons eigen routebeschrijving.
    "lithium-greenbushes-bunbury": {
        # ⚠️ DE DORPEN STAAN OP DE WEG GEPROJECTEERD, NIET OP HUN CENTRUM.
        # Met de plaatsknoop uit OSM (23-143 m náást de highway) rijdt de router
        # het dorp in en weer uit: gemeten in de eerste bake 180,0° keerpunten
        # bij Balingup en Picton. Ze helemaal weglaten kan ook niet — dan valt
        # de lijn van 88,2 naar 83,1 km omdat de Dijkstra een kortere sluipweg
        # pakt langs de N-weg. Dus: dezelfde dorpen, geprojecteerd op de
        # dichtstbijzijnde trunk/primary-vertex uit de eigen wegscan.
        # (Een dorp blijft in de brief een DEKKINGSpunt met marge; dit is de
        # tekenvariant ervan — de Taicang/Changshu-les, andere kant op.)
        "via": [
            ("Greenbushes concentraatloods", (116.05505, -33.86495)),
            ("Mijnpoort / Maranup Ford Rd",  (116.05413, -33.86376)),
            ("Stanifer St × South Western Hwy", (116.06491, -33.84210)),
            ("Balingup (op de highway)",     (115.98442, -33.78616)),
            ("Mullalyup (op de highway)",    (115.94523, -33.74287)),
            ("Kirup (op de highway)",        (115.89294, -33.70584)),
            ("Donnybrook (op de highway)",   (115.82594, -33.57660)),
            ("Boyanup (op de highway)",      (115.72791, -33.48365)),
            ("Picton (op de highway)",       (115.69414, -33.35121)),
            ("Willinge Drive (haventoegang)", (115.67423, -33.32799)),
            ("Bunbury Berth 8 — kade",       (115.66385, -33.31995)),
        ],
        "id": "li-greenbushes-bunbury",
        "naam": "Greenbushes-concentraatloods → Bunbury Berth 8 "
                "(Maranup Ford Rd → Stanifer St → South Western Hwy)",
        "extracts": ["australie"],
        "refs": ["1", "20"],           # South Western Highway draagt ref=1
        "gepubliceerdKm": 90,
        "bronnoot": "Talison/NS Energy: mijn ligt 90 km ZO van de haven",
        "vensterKm": 40,
        "uit": "stroombeen-greenbushes-bunbury.geojson",
    },

    # ── Routebrief grafiet-balama-vidalia, benen 5-8 (2026-08-04) ──────────
    # De keten van mijn tot eindproduct: last mile in Vidalia, en daarna fase
    # D en E over de weg naar Kansas en Arizona. ⚠️ Die twee lange benen
    # worden getekend terwijl het VOLUME VANDAAG NUL is (besluit Lars): de weg
    # is gemeten, de lading nog niet. Dat verschil hoort in de brief en de
    # node-note te staan, NIET in de lijnstijl — stippel betekent in dit
    # project precies één ding: hier reikt het net niet (werkwijze §7).
    "grafiet-vidalia-lastmile": {
        "via": [
            ("Port of Vidalia — apron/cargo ramp", (-91.48255, 31.53645)),
            ("Syrah AAM-fabriek",                  (-91.48870, 31.54660)),
        ],
        "id": "gr-vidalia-lastmile",
        "naam": "Port of Vidalia → Syrah AAM-fabriek (haventoegangsweg → LA-131 → D.A. Biglane Rd)",
        "extracts": ["us-louisiana"],
        "refs": ["131"],
        # ⚠️ `track` erbij: het beslissende eerste stuk (1,2 km havengrindweg)
        # draagt in OSM highway=track. Zonder deze klasse houdt het wegnet op
        # bij LA-131 en blijft er een rechte stub van ~800 m naar de kade over.
        "eindKlassen": ("track", "residential", "service", "tertiary", "unclassified"),
        "gepubliceerdKm": 2.34,
        "bronnoot": "eigen Dijkstra over us-louisiana (2026-08-04); de EA-waarde ~4 km "
                    "is niet reproduceerbaar — noch vanaf de kade, noch vanaf de apron",
        "vensterKm": 8,
        "uit": "stroombeen-vidalia-lastmile.geojson",
    },
    # ⚠️ Kop = de FABRIEKSPOORT, niet het laaddock. Dat uitgaande dock is op
    # z19 (de fijnste Esri-korrel) niet aanwijsbaar en wordt niet verzonnen.
    "grafiet-vidalia-us84": {
        "via": [
            ("Syrah fabriekspoort (front gate)", (-91.48743, 31.54796)),
            ("D.A. Biglane Rd × LA-131",         (-91.48503, 31.54530)),
            ("LA-131 × US-84, Vidalia",          (-91.42737, 31.56647)),
        ],
        "id": "gr-vidalia-us84",
        "naam": "Syrah-poort → D.A. Biglane Rd → LA-131 → US-84 (Vidalia)",
        "extracts": ["us-louisiana"],
        "refs": ["131", "84", "425"],
        "gepubliceerdKm": 6.98,
        "bronnoot": "gemeten over de OSM-geometrie 2026-08-04; de brief-waarde '~3 km' "
                    "klopt op geen enkele route. Alternatief Airport Road × US-84 "
                    "(-91.49884, 31.58728) is 5,46 km maar over tertiary — welke een "
                    "15-meter-trekker rijdt is onbekend (openstaand punt, geen stille keuze)",
        "vensterKm": 10,
        "uit": "stroombeen-vidalia-us84.geojson",
    },
    "grafiet-vidalia-desoto": {
        "via": [
            ("LA-131 × US-84 Vidalia",       (-91.42737, 31.56647)),
            ("Ferriday US-84 × US-425",      (-91.55496, 31.62988)),
            ("Clayton US-425 × US-65",       (-91.53933, 31.71575)),
            ("Winnsboro LA",                 (-91.72011, 32.16365)),
            ("US-425 × I-20 (Rayville)",     (-91.75873, 32.45759)),
            ("Bastrop LA",                   (-91.91330, 32.77830)),
            ("grens LA/AR op US-425",        (-91.85428, 33.01773)),
            ("Hamburg AR US-425 × US-82",    (-91.79763, 33.22426)),
            ("Monticello AR",                (-91.80229, 33.62908)),
            ("Pine Bluff AR — US-425→I-530", (-91.97206, 34.19938)),
            ("Little Rock I-530 × I-30",     (-92.26239, 34.75377)),
            ("N. Little Rock — I-40 ná I-30", (-92.25901, 34.77865)),
            ("Conway AR I-40 × US-65",       (-92.43278, 35.10847)),
            ("Russellville AR",              (-93.13381, 35.30431)),
            ("Alma AR I-40 × I-49",          (-94.22110, 35.48987)),
            ("Fayetteville AR",              (-94.20248, 36.07410)),
            ("I-49 Bella Vista Bypass",      (-94.31479, 36.42399)),
            ("grens AR/MO op I-49",          (-94.38238, 36.49919)),
            # ⚠️ KNOOPPUNT-VIA'S LIGGEN NÁ DE AFSLAG, NIET OP HET KRUIS.
            # Gemeten 2026-08-04: op het kruis zelf snapt de via op de
            # dichtstbijzijnde rijbaanvertex, en die kan ACHTER de reisrichting
            # liggen — de router rijdt er dan voorbij en keert om (Joplin
            # 177,1° · N. Little Rock 163,6° · Lenexa 163,4°). Geen afrit-fout
            # (`projecteer_viapunten.py` vond de rijbaan op 17-41 m) maar een
            # overschiet-en-terug. Punten daarom 300-500 m vóóruit gelegd op de
            # weg waarover de reis verdergaat.
            ("Joplin MO — I-49 ná I-44",     (-94.40691, 37.06809)),
            ("Nevada MO",                    (-94.32405, 37.83875)),
            ("Harrisonville MO I-49 × MO-7", (-94.35536, 38.63849)),
            ("Kansas City I-49 → I-435",     (-94.52622, 38.87285)),
            ("grens MO/KS op I-435",         (-94.60790, 38.93691)),
            ("Lenexa KS — K-10 ná I-435",    (-94.77794, 38.94231)),
            ("De Soto K-10 × Lexington Ave", (-94.96651, 38.96023)),
            # ⚠️ DE LIJN EINDIGT OP HET ROUTEERPUNT, NIET OP HET TERREINANKER.
            # Gemeten 2026-08-04: er is géén wegpad van deze rotonde naar
            # (-95.00240, 38.93815) — de terreinways liggen op een eigen
            # component achter het hek. Dat is geen tekortkoming maar de
            # anker≠routeerpunt-regel (§2b, zoals Napoleon Ave 154 m): het
            # De Soto-anker is een TERREINanker, want de docks zijn niet
            # gelegd (de Esri-opname is nog de bouwfase). Het reststukje van
            # ~0,4 km wordt als kmAanloopNaar gerapporteerd en NIET getekend.
            ("Astra Parkway — rotonde",      (-95.00748, 38.94196)),
        ],
        "id": "gr-vidalia-desoto",
        "naam": "Syrah Vidalia → Panasonic De Soto (US-84/US-425 → I-530 → I-40 → I-49 → I-435 → K-10)",
        "extracts": ["us-louisiana", "us-arkansas", "us-missouri", "us-kansas"],
        # ⚠️ "71" bewust NIET: die trok de eerste meetronde 26 km over het OUDE
        #    US-71-tracé door Bella Vista i.p.v. de I-49-bypass (open sinds
        #    01-10-2021). Verklikker na de bake: raakt de lijn (-94.27, 36.48)
        #    binnen 4 km, dan is de ref-voorkeur er alsnog ingetrapt.
        "refs": ["84", "425", "15", "530", "30", "40", "49", "435", "10"],
        "gepubliceerdKm": 1160,
        "bronnoot": "eigen corridormeting over de vier extracts 2026-08-04 (1.150,8 km net "
                    "+ last miles); GEEN bron documenteert deze rit. Het reële alternatief "
                    "(US-65 Ozarks + MO-13/MO-7, 1.084 km = 6% korter) is verworpen op "
                    "NHFN-aanwijzing, wegvorm en reistijd — niet op lengte",
        "vensterKm": 40,
        "uit": "stroombeen-vidalia-desoto.geojson",
    },
    "grafiet-desoto-casagrande": {
        "via": [
            # ⚠️ Begint op hetzelfde ROUTEERPUNT waar b7 eindigt (zie daar):
            # het terreinanker (-95.00240, 38.93815) is niet over de weg
            # bereikbaar, en de keten hoort aaneengesloten te zijn op de weg,
            # niet op de fabrieksstip.
            ("Astra Parkway — rotonde",       (-95.00748, 38.94196)),
            ("K-10 bij Astra Enterprise Pk",  (-95.00128, 38.96127)),
            # ⚠️ ná de afslag op K-7 zuidwaarts, zie de noot bij b7
            ("K-7 ná K-10 (zuidwaarts)",       (-94.85257, 38.93759)),
            ("K-7 × I-35 Olathe",             (-94.81556, 38.85570)),
            ("Ottawa KS",                     (-95.23252, 38.61673)),
            ("Emporia KS",                    (-96.17126, 38.41520)),
            ("El Dorado KS",                  (-96.88661, 37.83253)),
            ("Wichita I-35 × I-135",          (-97.25057, 37.66449)),
            ("grens KS/OK op I-35",           (-97.34227, 36.99998)),
            ("Oklahoma City I-35 × I-40",     (-97.47233, 35.46346)),
            ("El Reno OK",                    (-97.95474, 35.50142)),
            ("Elk City OK",                   (-99.38886, 35.40230)),
            ("grens OK/TX (Texola)",          (-100.00030, 35.22709)),
            ("Amarillo TX",                   (-101.84663, 35.19435)),
            ("grens TX/NM (Glenrio)",         (-103.04184, 35.18275)),
            ("Tucumcari NM",                  (-103.72533, 35.15164)),
            ("Santa Rosa NM",                 (-104.67828, 34.94713)),
            ("Albuquerque — the Big I",       (-106.62715, 35.10581)),
            ("Grants NM",                     (-107.85370, 35.14434)),
            ("Gallup NM",                     (-108.74265, 35.53078)),
            ("grens NM/AZ (Lupton)",          (-109.04522, 35.36509)),
            ("Holbrook AZ",                   (-110.15960, 34.91178)),
            ("Winslow AZ",                    (-110.68421, 35.02900)),
            ("Flagstaff I-40 × I-17",         (-111.66233, 35.17225)),
            ("Camp Verde AZ",                 (-111.88437, 34.57713)),
            ("Cordes Junction AZ",            (-112.12685, 34.30821)),
            ("Black Canyon City AZ",          (-112.14221, 34.06746)),
            ("Phoenix — the Split I-17×I-10", (-112.04809, 33.42724)),
            ("I-10 × I-8",                    (-111.68375, 32.81949)),
            ("I-8 afrit 172 Thornton Road",   (-111.77458, 32.82817)),
            ("Lucid AMP-1 — westpoort",       (-111.78238, 32.85035)),
            ("Lucid AMP-1 — dockrij",         (-111.78008, 32.85724)),
        ],
        "id": "gr-desoto-casagrande",
        "naam": "Panasonic De Soto → Lucid AMP-1 (K-10/K-7 → I-35 → I-40 → I-17 → I-10 → I-8)",
        "extracts": ["us-kansas", "us-oklahoma", "us-texas", "us-new-mexico", "us-arizona"],
        # ⚠️ "10" staat er twee keer in de werkelijkheid: K-10 in Kansas en I-10
        #    in Arizona. De ref-voorkeur is zacht (factor 3), maar buigt de lijn
        #    ergens raar af, dan is dit de eerste verdachte.
        "refs": ["10", "7", "35", "40", "17", "8"],
        "gepubliceerdKm": 2230,
        "bronnoot": "eigen corridormeting 2026-08-04 (grootcirkelsom 2.147 km over 31 punten "
                    "+ ~4%); geen bron documenteert de vervoerswijze — truck is werkaanname, "
                    "intermodaal spoor is niet uitgesloten",
        "vensterKm": 40,
        "uit": "stroombeen-desoto-casagrande.geojson",
    },

    # ── Routebrief koper-escondida-guixi, fase D (2026-08-05) ─────────────
    # De interne overbrenging van kathode naar de eigen walsdraadfabriek, over
    # de as die het officiële terreinplan (赣环监字（2017）第S007号, fig. 3-1)
    # als 物流主轴线 tekent: OSM way 1462532976, highway=service, 2.250 m,
    # géén access-tag. Onafhankelijk nagemeten 2026-08-05 (Overpass + lokale
    # extract): 43,1 m van het smelter-registerpunt, 8,0 m van het
    # walsdraad-registerpunt, 613 m tussen de twee projecties.
    # ⚠️ DE KOP IS EEN SUBSTITUUT. Het registerpunt van de smelter is NIET de
    #    kathode-expeditie; die is niet gevonden (brief §5.5) omdat Esri bij
    #    Guixi geen z19 heeft. Zodra ze gevonden is schuift dit via-punt
    #    daarheen en verdwijnt het procesgat van 0,54 km naar het spoorbeen.
    #    Dat gat IS het ontbrekende anker en wordt niet dichtgetrokken.
    # ⚠️ eindKlassen BEWUST NIET GEZET: de default-tuple bevat `service` al, en
    #    het corridor-id hasht de eindklassen mee — de default ongewijzigd
    #    laten garandeert dat de vier bestaande profielen byte-identiek blijven.
    "koper-guixi-fase-d": {
        "via": [
            ("贵溪冶炼厂 — registerpunt (substituut-kop)", (117.22545, 28.33227)),
            ("江西铜业铜材有限公司 — registerpunt",         (117.21919, 28.33180)),
        ],
        "id": "cu-guixi-fase-d",
        "naam": "kathode 贵冶 → walsdraadfabriek 铜材公司 (闪速大道 / 物流主轴线)",
        "extracts": ["china"],
        "refs": [],
        "gepubliceerdKm": 0.62,
        "bronnoot": "eigen meting 2026-08-05 over OSM way 1462532976 (highway=service, "
                    "2.250 m, geen access-tag, 8,0 m resp. 43,1 m van de twee "
                    "registerpunten); geen bron publiceert deze afstand",
        "vensterKm": 3,
        "uit": "stroombeen-guixi-fase-d.geojson",
    },

    # ── Routebrief lithium-greenbushes-zhangjiagang, been 5 (2026-08-05) ──
    # FASE C, last mile: van de publieke kade van 张家港港务集团 naar de poort van
    # 天齐锂业（江苏）, 东新路 5号 in het 扬子江国际化学工业园.
    #
    # ⚠️ DE BRIEF ZEGT ±3-5 KM EN DAT KAN NIET. Hemelsbreed liggen de twee ankers
    #    al 6,037 km uit elkaar: de weg moet zuidwaarts om de monding van het
    #    Zhangjiagang-kanaal en de zuidgeul heen. Gemeten 10,261 km over 51 punten
    #    — tweemaal onafhankelijk gereproduceerd (bevinding + weerlegger, tot op
    #    de meter gelijk).
    # ⚠️ DE EERSTE 0,555 KM IS HAVENTERREIN EN STAAT NIET IN OSM. In het vak
    #    lon 120,413-120,4275 x lat 31,9625-31,970 liggen 5 highway-ways, alle op
    #    lat <= 31,9641 (de zuidrand); boven 31,965 nul. De tool vlagt die aanloop
    #    als "> 0,5 km — bevinding"; dat is de JUISTE uitslag. Niet dichttrekken.
    # ⚠️ eindKlassen BEWUST NIET GEZET. Het beslissende eerste stuk is
    #    西五节桥街 = highway=service, en `service` zit AL in EIND_KLASSEN_DEFAULT
    #    ("residential", "service", "tertiary", "unclassified"). Zetten zou alleen
    #    de cachevingerafdruk veranderen (scan_corridor["id"] = eigen id + de
    #    eindklassen), niet de uitkomst.
    #    ⚠️ CORRECTIE OP DE KOPER-COMMENT: het argument "anders komen de bestaande
    #    profielen niet byte-identiek uit de bake" is ONJUIST — EIND_KLASSEN wordt
    #    per run in _kies_profiel gezet en de scan-id wordt uit het EIGEN id van
    #    elk profiel gebouwd, dus een eindKlassen-sleutel op een nieuw profiel kan
    #    een ander profiel per constructie niet raken. Het besluit klopt wel.
    # ⚠️ ALLE VIA-PUNTEN ZIJN ECHTE OSM-VERTICES uit de eigen wegscan (snap
    #    0-1 m), geen plaatsknopen — de Balingup-val (180,0 graden keerpunt, been
    #    2 van deze zelfde stroom) kan hier per constructie niet optreden.
    "lithium-zhangjiagang-lastmile": {
        "via": [
            ("Kade Zhangjiagang Port Group",            (120.42050, 31.96800)),
            ("中兴北路 × 常金线 X301",                     (120.42398, 31.95890)),
            ("常金线 X301 — vak zuid van 双山岛",           (120.43965, 31.96252)),
            ("常金线 X301 — vak langs het chemiepark",     (120.46944, 31.98062)),
            ("常金线 X301 × 长江北路",                     (120.47170, 31.99419)),
            ("长江北路 × 东新路",                          (120.46199, 32.01353)),
            ("Poort Tianqi Lithium (Jiangsu), 东新路 5",   (120.45771, 32.01218)),
        ],
        "id": "li-zjg-lastmile",
        "naam": "kade Zhangjiagang Port Group → poort Tianqi Lithium (Jiangsu) "
                "(西五节桥街 → 中兴北路 → 常金线 X301 → 长江北路 → 东新路)",
        "extracts": ["china"],
        # 常金线 draagt X301; 中兴北路/长江北路/东新路 zijn ongenummerd en krijgen
        # de zachte factor 3 — gemeten verandert dat de route niet.
        "refs": ["X301"],
        # ⚠️ TAUTOLOGISCH: dit is onze eigen meting, geen gepubliceerde waarde.
        #    De lengtetoets op dit been bewijst dus niets; de echte controle is de
        #    wegblokken-lijst en de verklikkers in sectie E van de werkorder.
        "gepubliceerdKm": 10.26,
        "bronnoot": "eigen Dijkstra over china-latest (2026-08-05) met exact de "
                    "regels van dit gereedschap, twee keer onafhankelijk "
                    "gereproduceerd; geen bron publiceert deze afstand. De "
                    "brief-waarde ±3-5 km is niet reproduceerbaar: de hemelsbrede "
                    "afstand kade→poort is al 6,037 km",
        "vensterKm": 5,
        "uit": "stroombeen-zhangjiagang-lastmile.geojson",
    },

    # ── Routebrief lithium-greenbushes-zhangjiagang, been 6 (2026-08-05) ──
    # FASE D: batterijkwaliteit hydroxide/carbonaat van 天齐锂业（江苏）naar de
    # kathodefabriek 乐友新能源材料（无锡）, 锡梅路 167号, Xinwu, Wuxi.
    #
    # DE CORRIDOR: 东新路 → 长江北路 → 常金线 X301 → 东海路 → S23 靖张高速
    #   (OSM name:en "Zhangjiagang Port Expressway") → G4221 沪武高速 →
    #   张家港枢纽立交 → S19 通锡高速 → afrit Xinwu → 新鸿路 X252.
    #
    # ⚠️ DE KOP IS DE POORT, NIET DE UITGAANDE LAADPLEK. Die laadplek is niet
    #    gevonden (werkorder F3); het procesgat van 218,9 m naar het terreinanker
    #    32.01050/120.45650 blijft daarom bewust bestaan en wordt NIET getekend.
    # ⚠️ DE CORRIDORKEUZE IS ROBUUSTER DAN EERST GEMELD, MAAR HET AANGEVOERDE
    #    BEWIJS KLOPTE NIET. De claim "zonder via-punten kiest de Dijkstra de
    #    S259-route van 61,0 km" is NIET reproduceerbaar: met de refs hieronder en
    #    NUL via-punten (venster 12 én 25 km) komt er exact 67,955 km uit, dezelfde
    #    408 punten. De 61,0 km verschijnt pas als je óók de refs leegmaakt. Wat de
    #    keuze wél draagt is een TIJD-optimale vrije Dijkstra (klassesnelheden,
    #    geen via-punten, geen refs, venster 25 km, dus met S228/S259/G2/G42/S48 in
    #    de zoekruimte): die kiest punt voor punt dezelfde lijn — 67,955 km /
    #    48,6 min tegen 61,3 km / 69,9 min voor S259. Drie onafhankelijke criteria
    #    (via-punten, ref-voorkeur, reistijd) geven dezelfde corridor.
    # ⚠️ S259 锡张线 IS EEN REËEL ALTERNATIEF (werkwijze §2), geen negatief anker:
    #    korter (61,0 km) maar trager, aandeel onbekend.
    # ⚠️ "G2 京沪高速 ligt minimaal 17,4 km van deze lijn" IS FOUT en mag niet in
    #    de brief. Ways met ref exact "G2" liggen 17,29 km weg, maar het
    #    concurrentievak met ref "G2;G42" — dat ÍS 京沪高速 — passeert op 2,02 km
    #    (bij 31,5073/120,4545). De conclusie (deze corridor is niet G2) blijft
    #    staan; het bewijs zat er 8,6x naast. _wegen_graaf matcht op ref.split(";").
    # ⚠️ DE TWEE KNOOPPUNT-VIAS LIGGEN NÁ DE INVOEGING (627 m op de G4221, 466 m
    #    op de S19), niet op het kruis — de overschiet-en-terug-regel.
    # ⚠️ eindKlassen BEWUST NIET GEZET: tertiary (东海路) en secondary zitten al in
    #    WEG_HOUD resp. EIND_KLASSEN_DEFAULT.
    "lithium-zhangjiagang-wuxi": {
        "via": [
            ("Poort Tianqi Lithium (Jiangsu), 东新路 5",    (120.45771, 32.01218)),
            ("长江北路 (Yangtze North Road)",                (120.46633, 32.00489)),
            ("常金线 X301 ná de aansluiting",               (120.47047, 31.98681)),
            ("东海路 → kop van de S23",                     (120.46599, 31.96594)),
            ("S23 靖张高速 ná de toerit",                    (120.47810, 31.95761)),
            ("S23 靖张高速 — middenvak",                     (120.49876, 31.89771)),
            ("S23 靖张高速 — vóór het knooppunt G4221",       (120.52082, 31.83047)),
            ("G4221 沪武高速 ná de invoeging",               (120.53242, 31.80877)),
            ("S19 通锡高速 ná 张家港枢纽立交",                  (120.58071, 31.78839)),
            ("S19 通锡高速 — middenvak west van Changshu",    (120.55646, 31.69145)),
            ("S19 通锡高速 — zuidvak oost van Wuxi",          (120.52141, 31.58316)),
            ("S19 通锡高速 — vóór de afrit Xinwu",            (120.48052, 31.52150)),
            ("新鸿路 X252 ná de afrit",                     (120.47346, 31.52318)),
            # ⚠️ STAART = HET LAADDOCK (z19: twee rode opleggers onder een
            #    laadluifel), NIET het EIA-anker 31.523573/120.475895. Reden is
            #    meetbaar: het EIA-anker ligt 186 m van de gerouteerde lijn en zou
            #    de marker-eis (<= 0,15 km punt-tot-segment) breken; het laaddock
            #    ligt op 126,3 m van 新鸿路. De 68,0 m ertussen zijn de correctie.
            #    Bijvangst: het EIA-anker was het enige anker in de brief met 6
            #    decimalen terwijl werkwijze §2 er 5 eist — dat probleem verdwijnt.
            ("Laaddock 乐友新能源材料（无锡）— westgevel",      (120.47518, 31.52362)),
        ],
        "id": "li-zjg-wuxi",
        "naam": "poort Tianqi (Jiangsu) → laaddock LG Chem/Huayou Wuxi "
                "(东新路 → 常金线 X301 → 东海路 → S23 靖张高速 → G4221 沪武高速 → "
                "张家港枢纽 → S19 通锡高速 → 新鸿路 X252)",
        "extracts": ["china"],
        # ⚠️ X301 BEWUST NIET IN refs: 锡甘线 bij Wuxi draagt dezelfde ref en zou
        #    het staartstuk naar zich toe trekken. (Gemeten: X301 er tóch bij
        #    zetten verandert exact niets — 67,955 km, identiek. De waarschuwing
        #    is dus overbodig maar onschadelijk.) De S19-ways met ref "S19;S58"
        #    matchen gewoon, want _wegen_graaf splitst op ";".
        "refs": ["S23", "G4221", "S19", "X252"],
        # De brief-waarde, NIET onze eigen meting — anders is de toets tautologisch.
        "gepubliceerdKm": 70,
        "bronnoot": "brief been 6 (±70 km) tegen een eigen Dijkstra over "
                    "china-latest (2026-08-05) langs de snelwegcorridor "
                    "S23 → G4221 → S19: 67,955 km = -2,9%. Twee keer onafhankelijk "
                    "gereproduceerd. Het afstand-optimale alternatief over de "
                    "provinciale S259 锡张线 is 61,0 km (-12,9%) — korter maar "
                    "trager (69,9 vs 48,6 min); reëel alternatief, aandeel onbekend",
        "vensterKm": 6,
        "uit": "stroombeen-zhangjiagang-wuxi.geojson",
    },

    # ── Routebrief lithium-greenbushes-zhangjiagang, been 7 (2026-08-05) ──
    # FASE E: NCM-kathodepoeder Wuxi → celfabriek LG Energy Solution Nanjing,
    # New Port-campus in de 南京经济技术开发区.
    #
    # DE CORRIDOR IS G42 沪宁高速. OSM draagt hem als ref "G2;G42" met naam
    # 京沪高速 tussen Shanghai en Wuxi, en als ref "G42" naam 沪蓉高速 verder
    # westwaarts — één weg, twee OSM-schrijfwijzen.
    #
    # ⚠️ HET "S38"-ALTERNATIEF IS GEMETEN EN VERWORPEN, twee keer. Wat in Jiangsu
    #    S38 常合高速 heet ligt in OSM als G4221 沪武高速 (805 ways met ref G4221;
    #    slechts 3 ways dragen S38, alle op lon 119,888-119,893 bij Changzhou —
    #    precies de gedeelde-tracé-claim). G4221 ligt op lon 120,4 op lat 31,814-
    #    31,819 (NOORD om Wuxi) en op lon 119,3 op lat 31,72, en nadert Nanjing van
    #    het ZUIDwesten — de verkeerde kant voor de NEDZ op lat 32,16. Gemeten
    #    312,3 km tegen 196,6 km via G42. Verworpen op VORM, niet alleen op lengte.
    # ⚠️ GEEN VIA OP S19 通锡高速. De fabriek ligt er 0,5 km vandaan en de Dijkstra
    #    pakt hem vanzelf. Een via ÓP S19 legde een 180,0-graden keerpunt neer: de
    #    oprit ligt noordelijk van de fabriek, de reis gaat zuidwaarts.
    # ⚠️ VIA-PUNT 8 LIGT BEWUST ÓÓST VAN HET G2503-KNOOPPUNT (dat zit op lon
    #    ≈118,938). Een punt wést ervan gaf 3 km overschiet-en-terug.
    # ⚠️ HET 栖霞大道-VIA LIGT 62 m VAN DE G2503-RIJBAAN, DUS ÓP HET KLAVERBLAD, en
    #    produceert een omkering van 173,6 graden met pad/hemelsbreed 2,08. Dat is
    #    een KNOOPPUNTLUS, geen terugloop (de band voor terugloop is 3,0-10,2), maar
    #    het is wel dezelfde knooppunt-via-regel die op been 8 juist wél is
    #    toegepast. Slaat toets_knikken.py erop aan: schuif dit punt verder
    #    noordwestwaarts ÓP 栖霞大道 en hermeet. Niet vooraf verschuiven — ongemeten.
    # ⚠️ DE KOP IS EEN SUBSTITUUT (de zuidpoort, 310,1 m van het laaddock): welk
    #    dock uitgaand is, is niet gedocumenteerd — b6-staart en b7-kop wezen
    #    anders op DEZELFDE apron en dan is §2b's twee-ankers-eis alleen nominaal
    #    vervuld. Een verzonnen verschil tussen twee docks zou erger zijn.
    #    ⚠️ DE EERSTE ~1 KM IS DAARDOOR NIET VOORGEMETEN: de meting van 196,6 km
    #    liep vanaf het fabrieksanker met een aanloop van 199 m. Verwacht
    #    锡梅路 → 新鸿路 → oprit → S19, dus +0,3 tot +0,6 km. HERMEET.
    # ⚠️ DE STAART IS VERVANGEN. Het briefpunt 32.16300/118.87900 ligt 21,4 m
    #    BUITEN way 621624910, in beboste helling — het was "satelliet-gelegd op
    #    z16" en op 2,0 m/px is dat verschil onzichtbaar. Nieuw: het bbox-midden
    #    van diezelfde way, binnen het hek, 216,0 m van het oude punt.
    "lithium-wuxi-nanjing": {
        "via": [
            ("Zuidpoort 乐友无锡, 锡梅路 (substituut-kop)",  (120.47492, 31.52084)),
            ("G2/G42 京沪高速 — knooppunt 硕放",             (120.45227, 31.50909)),
            ("G42 沪蓉高速 — Wuxi-west / Luoshe",           (120.19721, 31.70953)),
            ("G42 — Changzhou (noord van het centrum)",    (119.98628, 31.84207)),
            ("G42 — Danyang",                              (119.65600, 32.00444)),
            ("G42 — Zhenjiang",                            (119.44875, 32.05524)),
            ("G42 — Jurong 句容",                           (119.19980, 32.04512)),
            ("G42 — Nanjing-oost, vóór knooppunt G2503",   (118.97025, 32.06317)),
            ("G2503 南京绕城高速 — noordwaarts na het knooppunt", (118.95119, 32.10188)),
            ("栖霞大道 S338 — ná de afrit 栖霞",               (118.94392, 32.14829)),
            ("LG ES Nanjing — terreinanker New Port",      (118.87953, 32.16111)),
        ],
        "id": "li-wuxi-nanjing",
        "naam": "laaddock/zuidpoort LG Chem-Huayou Wuxi → LG Energy Solution "
                "Nanjing, New Port (S19 通锡 → G42 沪宁高速 → G2503 南京绕城 → "
                "栖霞大道 S338)",
        "extracts": ["china"],
        # G2 matcht het element "G2" in de OSM-ref "G2;G42"; G25 hoort bij G2503
        # (die ring draagt "G25;G2503"). Zachte voorkeur, factor 3.
        "refs": ["G42", "G2", "G2503", "G25", "S338"],
        "gepubliceerdKm": 180,
        "bronnoot": "brief been 7 (±180 km); onafhankelijk: gepubliceerde "
                    "wegafstanden Wuxi→Nanjing centrum-tot-centrum 174-185 km en "
                    "沪宁高速 is 274 km lang. Eigen corridormeting 196,6 km ruw / "
                    "196,3 na snoei = +9,1% — verklaarbaar doordat beide ankers "
                    "voorbij de stadscentra liggen (fabriek in Xinwu/硕放, campus "
                    "in de NEDZ aan de Yangtze). ⚠️ KRAP BINNEN ±10%: dit is het "
                    "eerste getal dat kantelt, en de kop IS verschoven — hermeet",
        "vensterKm": 40,
        "uit": "stroombeen-wuxi-nanjing.geojson",
    },

    # ── Routebrief lithium-greenbushes-zhangjiagang, been 8 (2026-08-05) ──
    # FASE E, slot: 2170-cellen van LG ES Nanjing naar Tesla Giga Shanghai,
    # poort 3, 江山路 5000号, 南汇新城镇, Lingang/Pudong. HET EINDE VAN DE KETEN.
    #
    # DE CORRIDOR: G42 沪宁高速 OOSTWAARTS TOT JIADING, DAARNA G1503 上海绕城高速
    # MET DE KLOK MEE OM SHANGHAI HEEN (Qingpu → Songjiang → Jinshan → Fengxian →
    # Lingang), en pas op het laatst 新四平公路 G228 → 江山路 → poort 3.
    #
    # ⚠️ ER GELDT EEN VRACHTVERBOD DOOR HET CENTRUM, EN DAT STUURT DE ROUTE.
    #    Blauwe-plaat vrachtwagens mogen de hele dag niet binnen de binnenring;
    #    sinds 15-10-2025 mogen diesel-vrachtwagens Euro-IV de hele dag niet
    #    binnen G1503, met S20 外环 als aanbevolen omleiding. Deze lijn blijft
    #    31,34 km van 人民广场 — gemeten. Ter vergelijking: een VRIJE Dijkstra
    #    komt op 14,7 km en gaat dus wél de verbodszone in, en is 30 km korter.
    #    Dát verbod is de reden dat we die kortere route niet nemen.
    # ⚠️ VIER ARCS GEMETEN vanaf het knooppunt G42 x G1503 (121,139/31,290):
    #    G1503-zuidwest 108,1 km · S32 申嘉湖 119,7 · S20 外环 + S2 沪芦 122,2 ·
    #    oostelijke arc via Pudong 131,0. De zuidwestarc wint op lengte, ligt het
    #    verst van de verbodszone en raakt als enige de brief-passage Songjiang.
    #    ⚠️ S20+S2 IS GEEN SCHOON ALTERNATIEF: die route komt op 10,9 km van
    #    人民广场 en ligt dus RUIM BINNEN G1503 — hij schendt precies het
    #    Euro-IV-verbod waarmee de gekozen arc wordt gerechtvaardigd. Noem hem in
    #    de brief alleen mét dat voorbehoud.
    # ⚠️ VIA-PUNT 17 LIGT OP 新四平公路 G228, NIET OP HET G1503-KNOOPPUNT 临海路.
    #    Gemeten: een via ÓP dat knooppunt (121.76188, 30.92297) legde een keerlus
    #    van 5,49 km over 41 punten neer. Ná de afslag → 0 keerlussen en het been
    #    381,9 → 376,1 km. Dezelfde les als Joplin/Lenexa.
    # ⚠️ VIA-PUNT 11 IS KUNSHAN EN NIET ANTING. G42 buigt tussen lon 121,14 en
    #    121,16 naar het zuiden; een via bij Anting (121,157/31,272) ligt in
    #    reisrichting VOORBIJ het G1503-knooppunt (121,139/31,290).
    # ⚠️ "G228" staat in refs voor de laatste 3,7 km, maar G228 loopt langs de hele
    #    Chinese kust en parallel aan G1503 tussen Jinshan en Lingang. Buigt de
    #    lijn daar raar af, dan is dit de eerste verdachte.
    # ⚠️ DE KOP IS EEN SUBSTITUUT (hoofdpoort 恒谊路, 301,4 m van het terreinanker):
    #    de uitgaande laadplek van de celfabriek is niet gevonden (werkorder F3).
    # ⚠️ DE STAART IS VERVANGEN EN DIT IS DE BELANGRIJKSTE CORRECTIE VAN DE HELE
    #    RONDE. Het briefpunt 30.87390/121.76572 is HET REKENKUNDIG MIDDEN VAN VIER
    #    OSM-BUSHALTENODES (12376922502..505, alle highway=bus_stop resp.
    #    public_transport=platform/stop_position, bus=yes; gemiddelde 30.873906/
    #    121.765716). Het ligt 1,0 m van de PUBLIEKE straat 正嘉路 op de WESToever
    #    van het kanaal en 60,9 m BUITEN way 635670279. Er is geen barrier=gate en
    #    geen entrance=* binnen 1,8 km. Elk "bewijs" dat dat punt goed snapt is
    #    CIRCULAIR: het meet het anker tegen één van de nodes waaruit het gemiddeld
    #    is. De echte poort ligt 97,8 m verderop, over de brug, 18,2 m BINNEN de
    #    fabriekspolygoon.
    # ⚠️ HET LAATSTE STUK IS NIET MEER GECONTROLEERD OP OVERSCHIET-EN-TERUG. Die
    #    controle liep op het oude (bushalte-)eindpunt. 正嘉路 (way 1338068671) heeft
    #    5 vertices over 869 m; de nieuwe staart hangt aan way 1229490502. CONTROLEER
    #    dit opnieuw — loopt het been over precies één benoemde way voorbij de poort,
    #    dan is knip_osm_been.py hier wél inzetbaar (anders dan bij been 5).
    "lithium-nanjing-shanghai": {
        "via": [
            ("Hoofdpoort LG ES Nanjing, 恒谊路 (substituut-kop)", (118.87950, 32.15840)),
            ("栖霞大道 S338 — vóór de oprit G2503",           (118.94392, 32.14829)),
            ("G2503 南京绕城高速 — zuidwaarts",                (118.95119, 32.10188)),
            ("G42 沪蓉高速 — Nanjing-oost (Qixia)",           (118.97025, 32.06317)),
            ("G42 — Jurong 句容",                            (119.19980, 32.04512)),
            ("G42 — Zhenjiang",                              (119.44875, 32.05524)),
            ("G42 — Danyang",                                (119.65600, 32.00444)),
            ("G42 — Changzhou",                              (119.98628, 31.84207)),
            ("G42 — Wuxi",                                   (120.19721, 31.70953)),
            ("G2/G42 京沪高速 — Suzhou",                       (120.59967, 31.35006)),
            ("G2/G42 — Kunshan (vóór knooppunt G1503)",      (120.99984, 31.33419)),
            ("G1503 上海绕城高速 — zuidwaarts na Jiading",      (121.14262, 31.24131)),
            ("G1503 — Qingpu",                               (121.13800, 31.14649)),
            ("G1503 — Songjiang",                            (121.14908, 31.01539)),
            ("G1503 — Jinshan / Fengxian (zuidkust)",        (121.29025, 30.87814)),
            ("G1503 — Fengxian-oost",                        (121.60383, 30.91048)),
            ("新四平公路 G228 — ná de afrit Lingang",          (121.73564, 30.88459)),
            ("江山路 — westzijde Tesla-terrein",               (121.75945, 30.87586)),
            ("Tesla Giga Shanghai — poort 3 (brug + wachtersgebouw)", (121.76667, 30.87423)),
        ],
        "id": "li-nanjing-shanghai",
        "naam": "LG Energy Solution Nanjing → Tesla Giga Shanghai poort 3 "
                "(G2503 → G42 沪宁高速 → G1503 上海绕城 → G228 新四平公路 → 江山路)",
        "extracts": ["china"],
        "refs": ["G42", "G2", "G2503", "G25", "G1503", "S338", "G228"],
        # ⚠️ DE BRIEF-WAARDE ±300 KM IS DE GROOTCIRKEL EN MOET UIT DE BRIEF:
        #    poort-tot-poort is hemelsbreed 308,68 km (nagerekend), dus een
        #    wegafstand van 300 km is onmogelijk.
        "gepubliceerdKm": 376,
        "bronnoot": "eigen corridormeting 2026-08-05 over china-latest.osm.pbf, "
                    "twee keer onafhankelijk gereproduceerd: 376,1 km ruw / 375,6 "
                    "na snoei. ⚠️ TAUTOLOGISCHE LENGTETOETS — er is geen bron die "
                    "deze rit documenteert. Onafhankelijke kruiscontrole: "
                    "gepubliceerd Nanjing→Shanghai-centrum 297-305 km, Lingang ligt "
                    "daar nog ~70 km voorbij, plus de ringomleiding → ~370-380 km. "
                    "De brief-waarde ±300 km is de GROOTCIRKEL (308,68 km "
                    "hemelsbreed poort-tot-poort)",
        "vensterKm": 40,
        "uit": "stroombeen-nanjing-giga-shanghai.geojson",
    },
}

# ⚠️ Kleine wegklassen: ALLEEN binnen EIND_STRAAL_KM van plant/kade (zie kop).
# weg_houden() krijgt alleen tags, dus de straal-beperking gebeurt geometrisch
# ná land_laad; de tag-verruiming zelf is een runtime-patch op fetch_landnet.
#
# ⚠️ PER PROFIEL OVERSCHRIJFBAAR via de sleutel "eindKlassen" (2026-08-04). Nodig
# omdat de last mile in Vidalia begint met 1,2 km havengrindweg die in OSM
# `highway=track` heet; zonder die klasse reikt het wegnet niet tot de kade en
# houd je een rechte stub van ~800 m over. De DEFAULT-tuple blijft ongewijzigd,
# en dat is geen netheid maar een vereiste: het corridor-id dat de scan ziet
# hasht de eindklassen mee (zie main()), dus een profiel zónder deze sleutel
# houdt exact dezelfde cachevingerafdruk en levert byte-identieke uitvoer.
EIND_KLASSEN_DEFAULT = ("residential", "service", "tertiary", "unclassified")
EIND_KLASSEN = EIND_KLASSEN_DEFAULT     # wordt per profiel gezet in _kies_profiel
EIND_STRAAL_KM = 12.0

TOLERANTIE = 0.10                   # de brief-toets: ±10%

# Worden in main() gezet uit het gekozen profiel.
VIA_PUNTEN = []
CORRIDOR = {}
UIT = ""


def snoei_keerlussen(pts, drempel_m=25.0):
    """Haal HEEN-EN-WEER-uitstapjes uit een gerouteerde lijn.

    ⚠️ WAAROM DIT NODIG IS. `corridor_keten` routeert van via-punt naar
    via-punt. Valt een via-punt op een ZIJTAK (een dorpsknoop naast de
    doorgaande weg, een rotonde-lus, een havenstraat die oostwaarts begint),
    dan rijdt de route die tak in en er weer uit — op de kaart een 180°-
    keerpunt dat een truck nooit maakt. Gemeten in de eerste lithium-bake:
    180,0° bij Balingup, Picton en de Willinge Drive-knoop.

    Een via-punt verplaatsen lost telkens één geval op en verschuift het
    probleem; en het via-punt wéglaten kost de corridor (83,1 i.p.v. 88,2 km,
    want dan pakt de Dijkstra een sluipweg). Daarom hier, ná het routeren, op
    de GETEKENDE lijn: waar de lijn zichzelf terugloopt, houd je één keer over.

    Werking: bij elk punt waar het pad terugkeert, groeit een palindroom-venster
    zolang de punten links en rechts binnen `drempel_m` van elkaar liggen; het
    heen-en-weer-stuk valt weg en het keerpunt zelf blijft staan als doorgang.
    Conservatief: raakt niets waar de lijn níet over zichzelf heen loopt (een
    echte haarspeldbocht in een bergweg heeft geen samenvallende armen).
    """
    if len(pts) < 5:
        return pts, []
    drempel = drempel_m / 1000.0
    weg = [False] * len(pts)
    gesnoeid = []
    i = 1
    while i < len(pts) - 1:
        if weg[i]:
            i += 1
            continue
        k = 1
        while (i - k >= 0 and i + k < len(pts)
               and fw.km(pts[i - k], pts[i + k]) <= drempel):
            k += 1
        k -= 1
        if k >= 2:                       # ≥2 punten aan weerszijden = uitstapje
            km_lus = sum(fw.km(pts[j], pts[j + 1]) for j in range(i - k, i + k))
            for j in range(i - k + 1, i + k):
                weg[j] = True
            gesnoeid.append((pts[i][0], pts[i][1], 2 * k - 1, km_lus))
            i += k
        else:
            i += 1
    return [p for p, w in zip(pts, weg) if not w], gesnoeid


def _kies_profiel(naam):
    """Zet de moduleglobals uit een profiel. Eén plek, zodat de rest van het
    bestand (en de bestaande grafiet-bake) letterlijk ongewijzigd blijft."""
    global VIA_PUNTEN, CORRIDOR, UIT, EIND_KLASSEN
    p = PROFIELEN[naam]
    VIA_PUNTEN = p["via"]
    EIND_KLASSEN = tuple(p.get("eindKlassen", EIND_KLASSEN_DEFAULT))
    CORRIDOR = {
        "id": p["id"],
        "naam": p["naam"],
        "van": VIA_PUNTEN[0][1],
        "naar": VIA_PUNTEN[-1][1],
        "via": [q for _, q in VIA_PUNTEN[1:-1]],
        "extracts": p["extracts"],
        "refs": p["refs"],
        "gepubliceerdKm": p["gepubliceerdKm"],
        "bronnoot": p.get("bronnoot", ""),
        "vensterKm": p["vensterKm"],
    }
    UIT = os.path.join(fl.CACHE, "ais", "graaf", p["uit"])


def main():
    import argparse
    ap = argparse.ArgumentParser(
        description="truckbeen uit een routebrief als GeoJSON-tekengeometrie")
    ap.add_argument("--profiel", default="grafiet-balama-nacala",
                    choices=sorted(PROFIELEN),
                    help="welk truckbeen uit welke routebrief")
    _kies_profiel(ap.parse_args().profiel)
    print(f"profiel: {CORRIDOR['id']} — {CORRIDOR['naam']}")

    # ⚠️ RUNTIME-ONLY (1/3): CORRIDORS wordt vervangen door alléén dit been,
    # zodat het scanvenster (en dus de graaf) niet ook de Beira-/Zimbabwe-
    # corridors door Mozambique meeneemt. Omdat we precies één extract scannen
    # draait land_scan in-proces (geen mp-spawn) — dat is een vereiste, want
    # een spawn-worker herimporteert fetch_landnet en zou geen van deze
    # patches zien. Het corridor-id dat de SCAN ziet draagt de eindklassen-
    # configuratie: _venster_sleutel hasht (id, punten, vensterKm), dus zo
    # krijgt deze filtervariant een eigen cachevingerafdruk — de M25-caches
    # blijven staan en de oude v093-cache (WEG_HOUD-only, oude kade) kan niet
    # stilletjes hergebruikt worden. corridor_keten krijgt gewoon CORRIDOR
    # (zelfde punten/venster), alleen de cache-sleutel verschilt.
    scan_corridor = dict(CORRIDOR)
    scan_corridor["id"] = (CORRIDOR["id"] + "+eind-" + ",".join(EIND_KLASSEN)
                           + f"@{EIND_STRAAL_KM:g}km")
    fl.CORRIDORS[:] = [scan_corridor]

    # ⚠️ RUNTIME-ONLY (2/3): weg_houden accepteert óók de kleine eindklassen
    # (zelfde access-uitsluiting). De 12-km-straal kan hier niet — weg_houden
    # krijgt alleen tags, geen geometrie — en volgt ná land_laad (zie onder).
    _weg_houden_orig = fl.weg_houden

    def _weg_houden_eind(tags):
        houd, reden = _weg_houden_orig(tags)
        if houd:
            return True, ""
        soort = (tags.get("highway") or "").strip()
        if (soort in EIND_KLASSEN
                and (tags.get("access") or "").strip() not in fl.WEG_ACCESS_WEG):
            return True, ""
        return houd, reden

    fl.weg_houden = _weg_houden_eind

    # ⚠️ RUNTIME-ONLY (3/3): snelle bbox-afwijzing vóór de segmentlus van
    # _raakt_venster. Met de kleine klassen erbij zou anders élke
    # residential-way van Maputo door zes segment-afstandsberekeningen per
    # vertex gaan. Gedrag identiek — de bbox is een ruime superset van het
    # corridorvenster (marge ruim boven vensterKm) — alleen sneller.
    lons = [p[0] for _, p in VIA_PUNTEN]
    lats = [p[1] for _, p in VIA_PUNTEN]
    marge = CORRIDOR["vensterKm"] / 100.0 + 0.25   # ° — ruim > 40 km op lat -14
    bb = (min(lons) - marge, max(lons) + marge,
          min(lats) - marge, max(lats) + marge)
    _raakt_orig = fl._raakt_venster

    def _raakt_venster_bbox(pts, vensters):
        for lo, la in pts:
            if bb[0] <= lo <= bb[1] and bb[2] <= la <= bb[3]:
                return _raakt_orig(pts, vensters)
        return False

    fl._raakt_venster = _raakt_venster_bbox

    # ⚠️ De extracts komen uit het PROFIEL, niet uit een vaste naam: de eerste
    # lithium-run scande stil Mozambique en meldde "geen wegen in het venster"
    # — een lege uitvoer zonder foutmelding, precies de klasse fout die dit
    # bestand elders bewaakt.
    extracts = CORRIDOR["extracts"]
    for naam in extracts:
        pad_extract = fl.extract_pad(naam)
        if not os.path.exists(pad_extract):
            raise SystemExit(f"extract ontbreekt: {pad_extract} — "
                             "haal hem met fetch_landnet.py --download")

    fl.land_scan(extracts, "weg", workers=1)
    ways = fl.land_laad(extracts, "weg")

    # ── de 12-km-beperking: kleine klassen ALLEEN bij plant en kade ────────
    # Corridor-breed zou elk dorpsspoor het venster in trekken; hier vallen
    # alle kleine-klasse-ways af die geen enkele vertex binnen EIND_STRAAL_KM
    # van een van de twee ankers hebben. De hoofdroute blijft op WEG_HOUD.
    plant, kade = CORRIDOR["van"], CORRIDOR["naar"]

    def _bij_eind(w):
        return any(fw.km((lo, la), plant) <= EIND_STRAAL_KM
                   or fw.km((lo, la), kade) <= EIND_STRAAL_KM
                   for lo, la in w["pts"])

    n_klein_tot = sum(1 for w in ways if w["soort"] in EIND_KLASSEN)
    ways = [w for w in ways if w["soort"] not in EIND_KLASSEN or _bij_eind(w)]
    n_klein_mee = sum(1 for w in ways if w["soort"] in EIND_KLASSEN)
    print(f"  eindklassen ({'/'.join(EIND_KLASSEN)}): {n_klein_mee:,} van "
          f"{n_klein_tot:,} kleine-klasse-ways binnen {EIND_STRAAL_KM:g} km "
          f"van plant/kade doen mee; {len(ways):,} ways totaal in de graaf")

    keten, rap = fl.corridor_keten(ways, CORRIDOR)
    if keten is None:
        raise SystemExit(f"⚠️ corridor niet gerouteerd: {rap.get('fout')}")

    # ⚠️ SNOEIEN VÓÓR ELKE METING. Zie snoei_keerlussen(): een via-punt op een
    # zijtak levert een heen-en-weer-uitstapje op, en dat telt zijn kilometers
    # twee keer mee. Meet het eindproduct, niet je meetlat.
    keten["pts"], gesnoeid = snoei_keerlussen(list(keten["pts"]))
    if gesnoeid:
        km_voor = rap["km"]
        rap["km"] = sum(fw.km(keten["pts"][i], keten["pts"][i + 1])
                        for i in range(len(keten["pts"]) - 1))
        print(f"  keerlussen gesnoeid: {len(gesnoeid)} · lengte "
              f"{km_voor:,.1f} → {rap['km']:,.1f} km (dubbel gereden stukken)")
        for lo, la, n, k in sorted(gesnoeid, key=lambda x: -x[3])[:5]:
            print(f"    {la:.5f},{lo:.5f} · {n} punten · {k:.2f} km")

    # ── wegklasse per vertex (voor de eindrapportage: waarover loopt de
    # first/last mile werkelijk?) — zelfde 6-decimalenkorrel als de graaf ────
    vertex_klassen = {}
    for w in ways:
        for lo, la in w["pts"]:
            vertex_klassen.setdefault((round(lo, 6), round(la, 6)),
                                      set()).add(w["soort"])

    def _klein_stuk(pts_keten, vanaf_start):
        """km + klassen vanaf het keten-uiteinde tot de eerste vertex die aan
        een WEG_HOUD-way ligt — het stuk dat over de kleine klassen loopt."""
        volgorde = pts_keten if vanaf_start else list(reversed(pts_keten))
        km_klein, klassen = 0.0, set()
        for i in range(len(volgorde) - 1):
            kl = vertex_klassen.get((round(volgorde[i][0], 6),
                                     round(volgorde[i][1], 6)), set())
            if kl & fl.WEG_HOUD:
                break
            klassen |= kl
            km_klein += fw.km(volgorde[i], volgorde[i + 1])
        return km_klein, sorted(klassen)

    # ── rapport per been: km + snap van beide via-punten naar de weg ──────
    print(f"\n  {CORRIDOR['naam']}")
    print(f"  {'been':<42} {'km':>8}  snap van → naar (km)")
    for i, been_km in enumerate(rap["benen"]):
        na, nb = VIA_PUNTEN[i][0], VIA_PUNTEN[i + 1][0]
        print(f"    {na + ' → ' + nb:<40} {been_km:>8,.1f}  "
              f"{rap['snapsKm'][i]:.2f} → {rap['snapsKm'][i + 1]:.2f}")

    # ── lengtetoets: rapporteren, niet gladstrijken — ALLEEN de weggeometrie
    afw = rap["km"] / CORRIDOR["gepubliceerdKm"] - 1.0
    vlag = "OK" if abs(afw) <= TOLERANTIE else "⚠️ BUITEN ±10% — bevinding"
    print(f"\n  lengtetoets (weggeometrie): {rap['km']:,.1f} km tegen "
          f"~{CORRIDOR['gepubliceerdKm']} ({CORRIDOR['bronnoot']}) "
          f"= {100 * afw:+.1f}%  [{vlag}]")

    # ── anker-verbindingsstukken (zie kop): plant → eerste wegpunt en laatste
    # wegpunt → kade, zodat het been exact op de briefankers begint en eindigt.
    # Met de eindklassen erbij horen deze stukjes ≤ ~0,5 km per kant te zijn —
    # rapporteren, niet gladstrijken: erboven is een bevinding die blijft staan.
    pts = list(keten["pts"])
    aanloop_van = fw.km(plant, pts[0])
    aanloop_naar = fw.km(pts[-1], kade)
    km_klein_van, kl_van = _klein_stuk(pts, True)
    km_klein_naar, kl_naar = _klein_stuk(pts, False)
    pts = ([(round(plant[0], 6), round(plant[1], 6))] + pts +
           [(round(kade[0], 6), round(kade[1], 6))])
    km_getekend = rap["km"] + aanloop_van + aanloop_naar
    v_van = "OK" if aanloop_van <= 0.5 else "⚠️ > 0,5 km — bevinding"
    v_naar = "OK" if aanloop_naar <= 0.5 else "⚠️ > 0,5 km — bevinding"
    print(f"  anker-verbindingen (rechte stukken, apart gerapporteerd, buiten "
          f"de lengtetoets):")
    print(f"    plant → weg {aanloop_van:.2f} km [{v_van}] · "
          f"weg → kade {aanloop_naar:.2f} km [{v_naar}]")
    print(f"  first mile over kleine klassen: {km_klein_van:.2f} km "
          f"({', '.join(kl_van) or 'geen — direct op WEG_HOUD'}) · "
          f"last mile: {km_klein_naar:.2f} km "
          f"({', '.join(kl_naar) or 'geen — direct op WEG_HOUD'})")
    print(f"  getekende lijn totaal: {km_getekend:,.1f} km · begint op de "
          f"plant en eindigt op de kade (continuïteit met de haven-aanloop "
          f"= 0,000 km)")

    # ── wegschrijven: [lon, lat], zelfde 6-decimalenkorrel als corridor_keten
    benen_props = []
    for i, been_km in enumerate(rap["benen"]):
        benen_props.append({
            "van": VIA_PUNTEN[i][0], "naar": VIA_PUNTEN[i + 1][0],
            "km": been_km,
            "snapVanKm": rap["snapsKm"][i],
            "snapNaarKm": rap["snapsKm"][i + 1],
        })
    doc = {
        "type": "FeatureCollection",
        "bron": "OpenStreetMap contributors (ODbL) via Geofabrik "
                "mozambique-latest; routebrief grafiet-balama-vidalia been 1",
        "laag": "stroombeen (tekengeometrie voor de stroomlaag — geen landnet)",
        "features": [{
            "type": "Feature",
            "properties": {
                "id": CORRIDOR["id"],
                "naam": CORRIDOR["naam"],
                "modaliteit": "truck",
                # km = de getekende lijn (incl. anker-verbindingen) — dit is
                # wat hecht_marnet uit de geometrie zal meten; kmWeg = de
                # lengtetoets-grootheid (alleen weggeometrie).
                "km": round(km_getekend, 3),
                "kmWeg": round(rap["km"], 3),
                "kmAanloopVan": round(aanloop_van, 3),
                "kmAanloopNaar": round(aanloop_naar, 3),
                # de first/last mile over de kleine eindklassen (zie kop):
                # echte weggeometrie, telt gewoon mee in kmWeg.
                "eindKlassen": list(EIND_KLASSEN),
                "eindStraalKm": EIND_STRAAL_KM,
                "kmKleinVan": round(km_klein_van, 3),
                "kmKleinNaar": round(km_klein_naar, 3),
                "klassenVan": kl_van,
                "klassenNaar": kl_naar,
                "gepubliceerdKm": CORRIDOR["gepubliceerdKm"],
                "afwijkingPct": round(100 * afw, 1),
                "binnenTolerantie": bool(abs(afw) <= TOLERANTIE),
                "vensterKm": CORRIDOR["vensterKm"],
                "benen": benen_props,
            },
            "geometry": {"type": "LineString",
                         "coordinates": [[lo, la] for lo, la in pts]},
        }],
    }
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False)
    print(f"\n  geschreven: {UIT} · {os.path.getsize(UIT) / 1024:.1f} KB · "
          f"{len(pts):,} punten")


if __name__ == "__main__":
    main()
