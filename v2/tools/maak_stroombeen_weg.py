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
    # ── NIEUWE PROFIELEN HIERONDER INVOEGEN (één per been; coördinaten (lon, lat)) ──
    # Routebrief kolen-tavantolgoi-baotou, been b2 (LICHTE werkwijze M29). Truck
    # (cokeskool, grensoverslag) Gashuunsukhait rail-yard (MN) → grenspost Gashuun
    # Sukhait → Chinese poort Ganqimaodu → Ganqimaodu-station/opslagloodsen (CN).
    # Geen gepubliceerde km (~9-10 km afgeleid uit de ankers); de grensspoorlijn
    # (32,6 km) is nog in aanbouw (gepland 2027), dus dit been is vandaag truck.
    # Via-punten `cu-ot-grens` en "Chinese poort Ganqimaodu" hergebruikt uit
    # koper-oyutolgoi-china.md §3/§4 (letterlijk dezelfde coördinaten).
    # ⚠️ Ruim venster (20 km) om de douanezone niet af te snijden; corridor kan
    #    tertiary/unclassified zijn in de poortzone.
    "kolen-tavantolgoi-baotou-tt-gs-ganqimaodu": {
        "via": [
            ("Gashuunsukhait rail-yard (anker, kolen-tt-gs)",              (107.53063, 42.44558)),
            ("Gashuun Sukhait grenspost (cu-ot-grens, hergebruikt)",       (107.5692, 42.4146)),
            ("Chinese poort Ganqimaodu (via-punt, hergebruikt)",          (107.5743, 42.4089)),
            ("Ganqimaodu-station + opslagloodsen (anker, kolen-ganqimaodu-opslag)", (107.60964, 42.37414)),
        ],
        "id": "kolen-tt-gs-ganqimaodu",
        "naam": "Gashuunsukhait-overslag → grenspost → Chinese poort → Ganqimaodu-opslag (grensoverslag, truck)",
        "extracts": ["mongolia", "china"],
        "refs": [],
        "gepubliceerdKm": None,
        "bronnoot": "geen publicatie; ~9-10 km afgeleid uit de ankers "
                    "(routebrief kolen-tavantolgoi-baotou.md b2) — lengtetoets is "
                    "indicatief, geen ±15%-toets tegen een derde bron",
        "vensterKm": 20,
        "uit": "kolen-tavantolgoi-baotou-weg-ttgs-ganqimaodu.geojson",
    },
    # Routebrief ree-mtweld-kuantan, been b1 (LICHTE werkwijze M29). Truck
    # (REE-concentraat in rotainers) Mt Weld-mijn/concentratieplant (Lynas) →
    # Laverton → Leonora → Menzies → Lynas Kalgoorlie Rare Earths Processing
    # Facility (Johns Rd, Yilkari) via de mijnweg → Great Central/Beadell Hwy →
    # Goldfields Highway. Drie via-punten pinnen de doorgaande corridor
    # (brief §4): Laverton = aansluiting mijnweg → Great Central Hwy (noord vs.
    # rechtstreeks zuid), Leonora = overgang naar de Goldfields Hwy (i.p.v. via
    # Cosmo Newbery), Menzies = Goldfields Hwy blijft doorgaand i.p.v. een
    # binnendoor-piste.
    # ⚠️ Kalgoorlie REPF-anker is ONZEKER (brief §3/§7): de satellietpas toont
    #    geen ondubbelzinnig REPF-terrein op 70 Johns Rd — mogelijk jonger dan
    #    de Esri-opname; adres uit vergunningdocumenten wel eenduidig.
    # ⚠️ Laatste toegang naar het REPF-terrein kan buiten het OSM-net vallen
    #    (Yilkari-terreininrit) — bij falen wordt dat een korte stippel in de bake.
    # ⚠️ Mt Weld → Laverton is een geen-wegpad zonder tussenpunten (eerste
    #    poging): het venster + WEG_HOUD (motorway t/m secondary) mist de
    #    outback-mijnweg. Hergebruikt de al bestaande, geconnecteerde via-keten
    #    uit corridor `ree-mountweld-leonora` (fetch_landnet.py CORRIDORS) voor
    #    het stuk Mt Weld→Leonora (bak_aanwijzingen), verlengd via Menzies naar
    #    Kalgoorlie REPF.
    "ree-mtweld-kuantan-mtweld-kalgoorlie": {
        "via": [
            ("Mt Weld-mijn/concentratieplant (anker, ree-mtweld-laad)",           (122.5392, -28.8695)),
            ("corridor-punt (ree-mountweld-leonora, hergebruikt)",                (122.460970, -28.838070)),
            ("corridor-punt (ree-mountweld-leonora, hergebruikt)",                (122.447140, -28.771820)),
            ("Laverton (corridor-punt, hergebruikt)",                            (122.400170, -28.625700)),
            ("corridor-punt (ree-mountweld-leonora, hergebruikt)",                (122.249690, -28.556980)),
            ("corridor-punt (ree-mountweld-leonora, hergebruikt)",                (121.859850, -28.829980)),
            ("corridor-punt (ree-mountweld-leonora, hergebruikt)",                (121.517600, -28.926250)),
            ("corridor-punt (ree-mountweld-leonora, hergebruikt)",                (121.334990, -28.885020)),
            ("Leonora (corridor-punt, hergebruikt)",                             (121.324050, -28.870100)),
            ("Menzies",                                                          (121.0291, -29.6924)),
            ("Lynas Kalgoorlie REPF, Johns Rd (anker, ree-kalgoorlie-repf, onzeker)", (121.4086, -30.7883)),
        ],
        "id": "ree-mtweld-kalgoorlie",
        "naam": "Mt Weld-mijn → Laverton → Leonora → Menzies → Lynas Kalgoorlie REPF (mijnweg → Goldfields Highway)",
        "extracts": ["australie"],
        "refs": [],
        "gepubliceerdKm": 380,
        "bronnoot": "~380 km, DWER/EPA-vergunningdocumenten (routebrief §2/§8[3][10])",
        "vensterKm": 50,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "ree-mtweld-kuantan-weg-mtweld-kalgoorlie.geojson",
    },
    # Routebrief ree-mtweld-kuantan, been b4 (LICHTE werkwijze M29). Truck
    # (MREC/rotainers) Kuantan Port (Tanjung Gelang) → havenweg → Jalan Gebeng
    # → Lynas Advanced Materials Plant (LAMP), Gebeng-industriezone. Geen
    # via-punten nodig (brief §4: korte havenweg → industrieweg, geen
    # gedocumenteerde corridorkeuze).
    # ⚠️ GEEN GEPUBLICEERDE KM (brief §2/§7): alleen een OSRM-schatting van
    #    8-12 km — de lengtetoets is hier indicatief, geen ±15%-toets tegen
    #    een derde bron.
    "ree-mtweld-kuantan-kuantan-lamp": {
        "via": [
            ("Kuantan Port, Tanjung Gelang (anker, ree-kuantan-kade)",  (103.4242, 3.9805)),
            ("Lynas Advanced Materials Plant, Gebeng (anker, ree-lamp-gebeng)", (103.3775, 4.0034)),
        ],
        "id": "ree-kuantan-lamp",
        "naam": "Kuantan Port → Jalan Gebeng → LAMP Gebeng (havenweg → industrieweg, geen gepubliceerde km)",
        "extracts": ["maleisie"],
        "refs": [],
        "gepubliceerdKm": None,
        "bronnoot": "geen publicatie; OSRM-schatting 8-12 km (routebrief §2/§7) "
                    "— lengtetoets is indicatief, geen ±15%-toets tegen een derde bron",
        "vensterKm": 40,
        "uit": "ree-mtweld-kuantan-weg-kuantan-lamp.geojson",
    },
    # Routebrief ree-bayanobo-baotou, been b2 (LICHTE werkwijze M29). Truck
    # (REE-concentraat, aannemelijk: Huamei-dochter ontvangt als eerste) van
    # het Baogang-selectiecomplex (Kundulun, 河西-industrie) naar de
    # scheidingsfabriek van Northern Rare Earth (waarschijnlijk 包头华美稀土高科,
    # 稀土高新区). Geen via-punten (brief §4: geen gedocumenteerde
    # corridorkeuze, ~15 km stedelijke hop over Baotou's doorgaande wegen).
    # ⚠️ GEEN GEPUBLICEERDE KM (brief §2/§7): ~15 km hemelsbreed is een
    #    schatting, geen operator-publicatie — de lengtetoets hierop is dus
    #    indicatief, geen ±15%-toets tegen een derde bron.
    "ree-bayanobo-baotou-baogang-scheiding": {
        "via": [
            ("Baogang-selectie (anker, ree-baogang-selectie)",             (109.7550, 40.6790)),
            ("Northern-scheiding Huamei (anker, ree-baotou-scheiding)",    (109.8741, 40.5884)),
        ],
        "id": "ree-baogang-scheiding",
        "naam": "Baogang-selectiecomplex → Northern Rare Earth-scheiding (Huamei), stedelijke wegen Baotou",
        "extracts": ["china"],
        "refs": [],
        "gepubliceerdKm": 15,
        "bronnoot": "geen publicatie; ~15 km hemelsbreed, geen officiële bron "
                    "(routebrief §2/§7) — lengtetoets is indicatief, geen "
                    "±15%-toets tegen een derde bron",
        "vensterKm": 25,
        "uit": "ree-bayanobo-baotou-weg-baogang-scheiding.geojson",
    },
    # Routebrief ree-kachin-ganzhou, been b1 (LICHTE werkwijze M29). Truck
    # (zware-REE-ionklei, RE-carbonaat/oxalaat in zakken) Pangwa-mijngebied +
    # grensdoorlaat (Kachin Special Region 1, Myanmar, KIA-gebied) → Diantan-
    # douane (滇滩镇), Tengchong, Yunnan. Geen via-punten (brief §4: geen
    # gedocumenteerde corridorkeuze in het nauwelijks gekarteerde Kachin-
    # wegennet) — het venster is ruim zodat de scan zelf het tracé door de
    # vallei kiest.
    # ⚠️ GEEN GEPUBLICEERDE KM (brief §2/§7): hemelsbreed 57,5 km, gepubliceerd
    #    "~60-110 km" is een ongebronde ontwerpaanname — lengtetoets is dus
    #    referentie, geen ±15%-toets tegen een derde bron.
    # ⚠️ CORRIDORKLASSEN OP TERTIARY/UNCLASSIFIED (geen `track`): de Kachin-kant
    #    hangt grotendeels aan `track` (in de eerdere scan 44 track tegen
    #    24 tertiary/10 secondary/4 primary/59 unclassified in de mijnbouw-
    #    bbox) — waar geen tertiary/unclassified-verbinding bestaat wordt het
    #    stuk een stippel met reden "hier reikt het net niet" (werkwijze §7),
    #    nooit dichtgetrokken via track.
    "ree-kachin-ganzhou-pangwa-diantan": {
        "via": [
            ("Pangwa — mijngebied + grensdoorlaat (anker, ree-pangwa-mijn)", (98.6080, 26.0153)),
            ("Diantan-douane, Tengchong (anker, ree-diantan-douane)",        (98.4097, 25.5292)),
        ],
        "id": "ree-pangwa-diantan",
        "naam": "Pangwa-mijngebied/grensdoorlaat → Diantan-douane, Tengchong (Kachin-bergweg → Chinese zijde, geen gepubliceerde wegnummers)",
        "extracts": ["myanmar", "china"],
        "refs": [],
        "gepubliceerdKm": None,
        "bronnoot": "geen publicatie; hemelsbreed 57,5 km, ontwerpaanname "
                    "\"~60-110 km\" zonder bron (routebrief §2/§7) — "
                    "lengtetoets is referentie, geen ±15%-toets",
        "vensterKm": 60,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "ree-kachin-ganzhou-weg-pangwa-diantan.geojson",
    },
    # Routebrief ree-sillamae-narva, been b1 (LICHTE werkwijze M29). Truck
    # (NdPr/Dy/Tb-oxide, aannemelijk: één bron) NPM Silmet OÜ, Sillamäe →
    # E20/Tallinn–Narva mnt (nationale weg 1) → Neo-magneetfabriek, Kulgu-
    # tööstuspark Narva. Drie via-punten pinnen de route op de doorgaande
    # kustcorridor i.p.v. de binnenweg door Sillamäe-centrum resp. een
    # binnenlandse afsnijding via Vaivara-Soldina resp. rechtdoor
    # Narva-centrum (brief §4, OSRM-tracé).
    # ⚠️ GEPUBLICEERDE KM = eigen OSRM-meting (30,3 km), geen onafhankelijke
    #    operator-publicatie (brief §2/§8[13]) — de lengtetoets loopt dus
    #    tegen de eigen referentie, geen ±15%-toets tegen een derde bron.
    # ⚠️ SILMET HANGT VIA `service`+`access=private`-terreinwegen AAN DE E20
    #    (gemeten op de ongefilterde OSM-graaf 2026-09-26; geen tertiary/
    #    unclassified binnen ~150 m van het anker) → eindToegangPrivaat, alleen
    #    binnen de 12-km-eindzone.
    "ree-sillamae-narva-silmet-narva": {
        "via": [
            ("NPM Silmet OÜ, Sillamäe (anker, ree-silmet-scheiding)",         (27.7421, 59.4031)),
            ("aansluiting Sillamäe op de Tallinn–Narva mnt",                  (27.7610, 59.3964)),
            ("doorgaande E20/weg 1 ter hoogte van Vaivara",                   (28.0131, 59.4010)),
            ("afslag Tallinn–Narva mnt → Kulgu-tööstuspark",                  (28.1541, 59.3767)),
            ("Neo-magneetfabriek, Kulgu-tööstuspark Narva (anker, ree-narva-magneetfabriek)", (28.1478, 59.3618)),
        ],
        "id": "ree-silmet-narva",
        "naam": "NPM Silmet Sillamäe → Neo-magneetfabriek Narva (E20/Tallinn–Narva mnt, kustcorridor)",
        "extracts": ["estland"],
        "refs": ["E20"],
        "gepubliceerdKm": 30,
        "bronnoot": "eigen OSRM-meting (routebrief §2/§8[13]), geen onafhankelijke "
                    "operator-publicatie — lengtetoets tegen de eigen referentie",
        "vensterKm": 20,
        "eindToegangPrivaat": True,
        "uit": "ree-sillamae-narva-weg-silmet-narva.geojson",
    },
    # Routebrief ree-mountainpass-fortworth, been b1 (LICHTE werkwijze M29). Truck
    # (NdPr-oxide, modaliteit aannemelijk — nergens gepubliceerd) Mountain Pass
    # mijn+scheiding → I-15 → US-93/I-11 → I-40 → US-287 → MP Materials
    # Independence (Fort Worth). Corridor + via-punten 1-op-1 hergebruikt uit de
    # bestaande definitie in fetch_landnet.CORRIDORS (id "ree-mountainpass-
    # fortworth"), alleen omgezet naar (lon, lat)-tuples voor dit profiel.
    # ⚠️ GEEN GEPUBLICEERDE KM (brief §7): de bake-toets loopt tegen de eigen
    #    OSRM/wegscan-uitkomst (~2.250 km indicatie), geen ±15%-toets tegen een
    #    onafhankelijke bron. Het gemeten spooralternatief (2.312 km, M28) is
    #    niet getekend.
    "ree-mountainpass-fortworth-mountainpass-fortworth": {
        "via": [
            ("Mountain Pass — mijn+scheiding (anker, ree-mp-laad)",        (-115.5325, 35.4786)),
            ("Las Vegas (I-15/US-93-knoop)",                               (-115.1372, 36.1750)),
            ("Boulder City-omgeving (US-93/I-11)",                        (-114.7414, 36.0125)),
            ("Kingman AZ (US-93/I-40-knoop)",                              (-114.0530, 35.1894)),
            ("Flagstaff AZ (op I-40)",                                     (-111.6513, 35.1983)),
            ("Albuquerque NM (op I-40)",                                   (-106.6504, 35.0844)),
            ("Amarillo TX (I-40/US-287-knoop)",                            (-101.8313, 35.2220)),
            ("Wichita Falls TX (op US-287)",                                (-98.4934, 33.9137)),
            ("Decatur/Justin-omgeving TX (US-287 laatste stuk)",           (-97.5861, 33.2343)),
            ("Independence Fort Worth — metaal-/magneetfabriek (anker, ree-fw-fabriek)", (-97.2498, 32.9845)),
        ],
        "id": "ree-mp-fortworth",
        "naam": "Mountain Pass → Las Vegas → Kingman → Flagstaff → Albuquerque → Amarillo → Fort Worth (I-15 → I-11/US-93 → I-40 → US-287)",
        "extracts": ["us-california", "us-nevada", "us-arizona", "us-new-mexico", "us-texas"],
        "refs": ["I 15", "I 11", "US 93", "I 40", "US 287"],
        "gepubliceerdKm": None,
        "bronnoot": "geen publicatie — bake-toets tegen de eigen OSRM/wegscan-"
                    "uitkomst (~2.250 km indicatie, routebrief §7); "
                    "spooralternatief 2.312 km (M28) niet getekend",
        "vensterKm": 50,
        "uit": "ree-mountainpass-fortworth-weg-mountainpass-fortworth.geojson",
    },
    # Routebrief nikkel-morowali-quzhou, been b2 (LICHTE werkwijze M29). Truck
    # (MHP in containers/big bags) Ningbo/Beilun-losberth (hergebruikt anker uit
    # de koperketen) → Huayou New Energy Technology Quzhou — nikkelsulfaat-/
    # precursorfabriek (aannemelijk: één bron voor de exacte afnemer). Corridor
    # G60 Shanghai–Kunming via Shaoxing–Jinhua.
    # ⚠️ BEIDE TUSSENPUNTEN ZIJN STADSCENTROÏDES UIT NOMINATIM, GEEN WEGVERTICES
    #    (brief §4): Overpass was onbereikbaar om de echte G60-op-/afritten te
    #    vinden. Ze moeten hier op de doorgaande G60 projecteren; >5 km snap =
    #    fout gelegd, dan eerst de wegklasse nakijken (corridorKlassen), niet
    #    het punt bijschuiven.
    # ⚠️ GEEN GEPUBLICEERDE KM (brief §7): ~300 km is een corridorschatting over
    #    de kaart (Ningbo–Shaoxing–Jinhua–Quzhou langs G60), geen bronopgave —
    #    de lengtetoets hierop is dus geen ±15%-toets, alleen een referentie.
    # ⚠️ Quzhou-eindpunt is regio-niveau (perceel niet gelegd, brief §3/§7).
    "nikkel-morowali-quzhou-beilun-quzhou": {
        "via": [
            ("Ningbo/Beilun-losberth (anker, hergebruikt)",                    (121.8830, 29.9364)),
            ("Shaoxing-omgeving (stadscentroïde, corridor-indicator — projecteer op G60)", (120.5769, 29.9992)),
            ("Jinhua-omgeving (stadscentroïde, corridor-indicator — projecteer op G60)",   (119.6486, 29.1080)),
            ("Huayou Quzhou-fabriek (regio-niveau, onzeker, anker)",           (118.8780, 28.9020)),
        ],
        "id": "ni-beilun-quzhou",
        "naam": "Ningbo/Beilun-losberth → Huayou Quzhou-fabriek (G60 via Shaoxing–Jinhua)",
        "extracts": ["china"],
        "refs": ["G60"],
        "gepubliceerdKm": 300,
        "bronnoot": "geen publicatie; corridorschatting over de kaart "
                    "(Ningbo–Shaoxing–Jinhua–Quzhou langs G60), geen bronopgave "
                    "(routebrief §7) — rapporteer als referentie, geen ±15%-toets",
        "vensterKm": 60,
        "uit": "nikkel-morowali-quzhou-weg-beilun-quzhou.geojson",
    },
    # Routebrief nikkel-ouaco-gwangyang, been b1 (LICHTE werkwijze M29). Truck
    # (lateriet-erts) NMC-mijnplateau Ouaco (Kaala-Gomen) → Téoudié-laadkade,
    # over de privé-mijnweg "Mines" (Cotransmine). OSM-bbox rond Ouaco is
    # overwegend track/unclassified (348× track, 73× unclassified, 60×
    # primary/RT1) — de doorgaande mijnweg zelf staat vrijwel zeker als
    # `track`, en dat komt de scanner NOOIT door, ook niet via corridorKlassen
    # (zie de opmerking bij regel 1368 hieronder). Dit profiel is daarom een
    # VERWACHTE-MISLUKKING-poging: als hij geen pad geeft, valt het been terug
    # op een rechte stippel (bak-aanwijzingen, orkestrator-opdracht).
    "nikkel-ouaco-gwangyang-ouaco-teoudie": {
        "via": [
            ("NMC-mijnplateau Ouaco (anker, ni-ouaco-mijn)", (164.4750, -20.7400)),
            ("Téoudié-laadkade (anker, ni-teoudie-kade)",    (164.3822, -20.7566)),
        ],
        "id": "ni-ouaco-teoudie",
        "naam": "Ouaco-mijnplateau → Téoudié-laadkade (mijnweg \"Mines\", privaat/track)",
        "extracts": ["nieuw-caledonie"],
        "refs": [],
        "gepubliceerdKm": None,
        "bronnoot": "geen publicatie; ~10 km hemelsbreed (routebrief §7) — losse "
                    "controle, geen hard toetsdoel",
        "vensterKm": 15,
        "corridorKlassen": ["unclassified", "tertiary"],
        "eindKlassen": ["unclassified", "tertiary", "service", "residential"],
        "eindToegangPrivaat": True,
        "uit": "nikkel-ouaco-gwangyang-weg-ouaco-teoudie.geojson",
    },
    # Routebrief nikkel-ouaco-gwangyang, been b7 (LICHTE werkwijze M29). Truck
    # (ferronikkel) SNNC-fabriek Gwangyang → POSCO-staalfabriek Pohang. Geen
    # bron noemt de weg of de lengte (aannemelijk: één bron voor de afnemer,
    # brief §6/§7); via-lijst = alleen de twee ankers, de Dijkstra routeert
    # vrij over het zuid-korea-extract op WEG_HOUD (motorway t/m secondary).
    "nikkel-ouaco-gwangyang-snnc-pohang": {
        "via": [
            ("SNNC-fabriek Gwangyang (anker, ni-snnc-fabriek)",       (127.7360, 34.9295)),
            ("POSCO-staalfabriek Pohang (anker, ni-pohang-mill)",     (129.3820, 36.0180)),
        ],
        "id": "ni-snnc-pohang",
        "naam": "SNNC Gwangyang → POSCO Pohang (aannemelijk: één bron, geen gedocumenteerde corridor)",
        "extracts": ["zuid-korea"],
        "refs": [],
        "gepubliceerdKm": 250,
        "bronnoot": "schatting op de kaart (routebrief §2/bak-aanwijzingen), geen "
                    "publicatie om ±15% tegen te toetsen",
        "vensterKm": 60,
        "uit": "nikkel-ouaco-gwangyang-weg-snnc-pohang.geojson",
    },
    # Routebrief nikkel-taganito-niihama, been b1 (LICHTE werkwijze M29). Truck
    # (limonieterts) Taganito Mining Corporation, laadplek (Nickel Asia, Claver)
    # → Taganito HPAL Nickel Corporation-plant, aangrenzend terrein — eigen
    # mijnweg, hemelsbreed maar 1,2 km. ⚠️ GEEN GEPUBLICEERDE WEG-KM (brief §2):
    # het venster 3-8 km is een ontwerpschatting, geen harde toets. De
    # OSM-bbox rond Claver is overwegend unclassified/service (access=private)
    # en track → corridorKlassen ruim + eindToegangPrivaat True; lukt geen
    # wegpad, dan valt dit been terug op een stippel "eigen terrein" in de
    # bake (geen tweede scanpoging). Negeer 8 korte ongelabelde pipeline-ways
    # rond 9.54,125.82 (THPAL-terrein) — dat is géén ertsleiding.
    "nikkel-taganito-niihama-taganito-thpal": {
        "via": [
            ("Taganito Mining Corporation — laadplek (anker, ni-taganito-laad)", (125.8193, 9.5464)),
            ("Taganito HPAL Nickel Corporation — plant (anker, ni-thpal-plant)", (125.8106, 9.5395)),
        ],
        "id": "ni-taganito-thpal",
        "naam": "Taganito-mijn (TMC) → THPAL-plant (eigen mijnweg, aangrenzend terrein)",
        "extracts": ["filipijnen"],
        "refs": [],
        "eindKlassen": ("tertiary", "unclassified", "residential", "service"),
        "eindToegangPrivaat": True,
        "gepubliceerdKm": 5.5,
        "bronnoot": "geen publicatie; routebrief geeft een venster van 3-8 km "
                    "(ontwerpschatting, geen harde toets), hemelsbreed 1,2 km",
        "vensterKm": 12,
        "corridorKlassen": ["tertiary", "unclassified", "service"],
        "uit": "nikkel-taganito-niihama-weg-taganito-thpal.geojson",
    },
    # Routebrief nikkel-wedabay-iwip, been b1 (LICHTE werkwijze M29). Truck
    # (lateriet-erts) actieve dagbouw-put WBN → IWIP-ore-yard, eigen mijnweg
    # (deels OSM unclassified/tertiary, deels track/service). Geen gepubliceerde
    # km — 3,6 km hemelsbreed (satellietmeting, dit document) is losse controle,
    # geen hard toetsdoel; vensterKm ruim (reliëf kan het pad fors verlengen).
    # ⚠️ Kop bij de put is vermoedelijk track/service (niet gekarteerd als
    # doorgaande weg) → als het laatste stuk daar niet doorkomt, knipt de bake
    # en wordt dat stuk gestippeld "eigen mijnweg (geen net op deze korrel)".
    "nikkel-wedabay-iwip-pit-rkef": {
        "via": [
            ("Actieve dagbouw-put WBN (anker, ni-wedabay-pit)",          (127.9350, 0.4930)),
            ("Knik mijnweg / erts-schermstation",                        (127.9430, 0.4880)),
            ("Eerste kruising IWIP-industrieweg",                        (127.9560, 0.4940)),
            ("IWIP-ore-yard, Lelilef (anker, ni-iwip-rkef)",             (127.9670, 0.4970)),
        ],
        "id": "ni-wedabay-iwip-pit-rkef",
        "naam": "Weda Bay-put → IWIP-ore-yard (eigen mijnweg, unclassified/tertiary)",
        "extracts": ["indonesie"],
        "refs": [],
        "gepubliceerdKm": 3.6,
        "bronnoot": "GEEN publicatie; 3,6 km hemelsbreed (satellietmeting, "
                    "routebrief §2) — losse controle, geen hard toetsdoel. Het "
                    "echte pad kan door het reliëf fors langer zijn; een "
                    "lengte-afwijking t.o.v. dit hemelsbrede getal is verwacht "
                    "en is een bevinding, geen fout.",
        "vensterKm": 20,
        # OSM-scan bbox toont 138 unclassified / 88 trunk / 55 track / 29
        # tertiary; benoemde mijnwegen staan als unclassified/service. Trunk
        # zit al in WEG_HOUD (default corridorklassen); service erbij als
        # kleine klasse (`track` komt de scanner sowieso niet door).
        "corridorKlassen": ["unclassified", "tertiary", "service"],
        # Zowel de put als het IWIP-ore-yard-terrein zijn vermoedelijk deels
        # private/permit-wegen (WBN-contractgebied resp. IWIP-industrieterrein).
        "eindToegangPrivaat": True,
        "uit": "nikkel-wedabay-iwip-weg-pit-rkef.geojson",
    },
    # Routebrief kobalt-kcc-kokkola, been b1 (LICHTE werkwijze M29). Truck
    # (kobalthydroxide) KCC Luilu-plant (Glencore, Kolwezi) → Durban DCT Pier 2 —
    # RN39 Kolwezi→Likasi (nieuw stuk, niet eerder gebakken), dan IDENTIEK aan
    # koper-tfm-durban §4 vanaf Likasi (RN1 → Kasumbalesa → T3/T2 → Chirundu →
    # A1/A4 → Beitbridge → N1/N3) — geen letterlijke bestandskopie (ander
    # beginpunt: Luilu i.p.v. TFM Fungurume), wel dezelfde 12 via-punten in
    # dezelfde volgorde. ⚠️ Venster 75 km (zoals koper-tfm-durban: RN39 buigt
    # ver uit de rechte lijn). ⚠️ RN39 Kolwezi–Likasi mogelijk lage OSM-wegklasse
    # (Oyu Tolgoi-precedent) — check corridorKlassen bij een snap > 5 km.
    "kobalt-kcc-durban": {
        "via": [
            ("KCC Luilu-plant, Kolwezi (anker, co-kcc-luilu)", (25.3620, -10.7205)),
            ("RN39 ZO van Kolwezi (nieuw stuk)",               (25.5300, -10.8600)),
            ("Likasi RN39→RN1",                                 (26.7355, -10.9806)),
            ("Lubumbashi RN1",                                  (27.4827, -11.6642)),
            ("Kasumbalesa (grens DRC/Zambia)",                  (27.7959, -12.2658)),
            ("Ndola T3",                                        (28.6367, -12.9688)),
            ("Kabwe T2",                                        (28.4400, -14.4426)),
            ("Lusaka T2",                                       (28.2817, -15.4163)),
            ("Chirundu (grens Zambia/Zimbabwe)",                (28.8471, -16.0338)),
            ("Harare A1→A4",                                    (31.0467, -17.8362)),
            ("Masvingo A4",                                     (30.8332, -20.0745)),
            ("Beitbridge (grens Zimbabwe/RSA)",                 (29.9865, -22.2244)),
            ("Polokwane N1-bypass",                             (29.4803, -23.9218)),
            ("Buccleuch N1/N3-splitsing",                       (28.1004, -26.0493)),
            ("Durban DCT Pier 2 (anker, cu-durban-kade)",       (31.0160, -29.8790)),
        ],
        "id": "co-kcc-durban",
        "naam": "KCC Luilu-plant, Kolwezi → Durban DCT Pier 2 (RN39 → RN1 → "
                "T3/T2 → A1/A4 → N1/N3)",
        "extracts": ["congo-drc", "zambia", "zimbabwe", "zuid-afrika"],
        "refs": ["RN39", "RN1", "N1", "T3", "T2", "A1", "A4", "N3"],
        "gepubliceerdKm": 3100,
        "bronnoot": "routebrief §2: ~3.100 km (400 Kolwezi–Kasumbalesa [7] + "
                    "rest = koper-tfm-durban b1, 2.982 km gebakken)",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary"],
        "uit": "kobalt-kcc-kokkola-weg-kcc-durban.geojson",
    },
    # Routebrief lithium-bougouni-yangpu, been b1 (LICHTE werkwijze M29). Truck
    # (spodumeenconcentraat) Ngoualana-plant (Kodal Minerals, Bougouni) → TIPSP
    # San Pedro, dwars over Mali/Ivoorkust: RN7 Bougouni–Sikasso → grens
    # Zégoua/Pogo → Ferkessédougou → Bouaké/Yamoussoukro → Soubré → San Pedro.
    # ⚠️ HET IVORIAANSE TRACÉ IS NIET GEPUBLICEERD (brief §7): alleen "~880 km,
    #    één grensovergang, gevestigde corridor via Sikasso"; de via-keten geeft
    #    hemelsbreed al ~1.014 km (boven de 880) — de lengtetoets op de GEVOLGDE
    #    weggeometrie is de echte controle, niet de via-punten-som.
    "lithium-bougouni-yangpu-plant-sanpedro": {
        "via": [
            ("Ngoualana-plant — Kodal Minerals DMS (laadplek)", (-7.4886, 11.3413)),  # anker
            ("Sikasso (RN7-knoop)",                             (-5.6778, 11.3166)),
            ("Grens Zégoua (ML) / Pogo (CI)",                   (-5.6531, 10.4828)),
            ("Ferkessédougou (A3/N1-knoop)",                    (-5.1976, 9.5940)),
            ("Yamoussoukro (N1/A3-knoop)",                      (-5.2776, 6.8200)),
            ("Soubré (aftakking naar San Pedro)",               (-6.5933, 5.7850)),
            ("TIPSP San Pedro — bulkstockpile",                 (-6.6180, 4.7490)),  # anker
        ],
        "id": "li-bougouni-sanpedro",
        "naam": "Ngoualana-plant → San Pedro TIPSP (RN7 → grens Zégoua/Pogo → Ferkessédougou → Yamoussoukro → Soubré)",
        "extracts": ["mali", "ivoorkust"],
        "refs": ["RN7", "N1", "A3", "N9"],
        "gepubliceerdKm": 880,
        "bronnoot": "Kodal Minerals: ~880 km, één grensovergang, gevestigde "
                    "corridor via Sikasso (brief §2/§7); via-keten hemelsbreed "
                    "~1.014 km, geen onafhankelijke bevestiging van het tracé",
        "vensterKm": 40,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "lithium-bougouni-yangpu-weg-plant-sanpedro.geojson",
    },
    # Routebrief lithium-bougouni-yangpu, been b3 (LICHTE werkwijze M29). Kort
    # truckbeen SDIC Yangpu-kade → Hainan Xingzhihai New Materials, binnen de
    # Yangpu Economic Development Zone / New Materials Industrial Park — geen
    # tussenliggend via-punt (brief §7: geen corridorkeuze, ~5-10 km schatting).
    # ⚠️ BEIDE ANKERS ONZEKER (brief §3): geen bron wijst een specifieke berth
    #    of fabriekspoort aan; kade- en fabriekscoördinaat zijn plaatsbepalingen
    #    binnen de havenzone resp. het industriepark.
    "lithium-bougouni-yangpu-yangpu-xingzhihai": {
        "via": [
            ("SDIC Yangpu-havenzone — kade (onzeker)",                (109.1510, 19.7680)),  # anker
            ("Hainan Xingzhihai New Materials — fabriekspoort (onzeker)", (109.1570, 19.7180)),  # anker
        ],
        "id": "li-yangpu-xingzhihai",
        "naam": "SDIC Yangpu-kade → Hainan Xingzhihai New Materials (havenweg/estateweg Yangpu EDZ)",
        "extracts": ["china"],
        "refs": [],
        "gepubliceerdKm": 8,
        "bronnoot": "geen publicatie; schatting 5-10 km binnen de Yangpu New "
                    "Materials Industrial Park (brief §2/§7)",
        "vensterKm": 15,
        "corridorKlassen": ["tertiary", "unclassified", "residential", "service"],
        "uit": "lithium-bougouni-yangpu-weg-yangpu-xingzhihai.geojson",
    },
    # Routebrief grafiet-balama-saemangeum, been b3 (LICHTE werkwijze M29). Kort been
    # (~4 km) binnen hetzelfde Osikdo-dong-industriecomplex bij Gunsan: van de
    # (aannemelijke) losplek Gunsan New Port naar het (onzekere) Future Graph
    # Saemangeum-perceel (blok 6). GEEN corridorkeuze — geen via-punten nodig, alleen
    # de twee ankers. ⚠️ Blok 6 is nog een bouwterrein (oplevering 2027); als de
    # scanner geen wegverbinding vindt hoort dit been een stippel te worden
    # ("eigen terrein / geen net op deze korrel"), niet een verzonnen lijn.
    "grafiet-balama-saemangeum-gunsan-saemangeum": {
        "via": [
            ("Gunsan (New) Port — losplek (aannemelijk)", (126.5830, 35.9770)),
            ("Future Graph Saemangeum — blok 6 (onzeker)", (126.5480, 35.9680)),
        ],
        "id": "gr-saemangeum-gunsan-fabriek",
        "naam": "Gunsan New Port → Future Graph Saemangeum (Osikdo-dong-industrieterrein)",
        "extracts": ["zuid-korea"],
        "refs": [],
        "eindKlassen": ("track", "residential", "service", "tertiary", "unclassified"),
        "eindToegangPrivaat": True,
        "gepubliceerdKm": 4,
        "bronnoot": "geen publicatie — brief-schatting o.b.v. nabijheid binnen het complex",
        "vensterKm": 12,
        "uit": "grafiet-balama-saemangeum-weg-gunsan-saemangeum.geojson",
    },
    # Routebrief grafiet-balama-saemangeum, been b4. Truck Future Graph Saemangeum →
    # POSCO Future M Sejong (~180 km, geen publicatie): Route 21 → Seohaean Expwy (15)
    # → Iksan-knooppunt → Nonsan-knooppunt → Nonsan-Cheonan Expwy (25) →
    # Jeonui-industriepark. Drie via-punten pinnen de corridorkeuze (kustsnelweg i.p.v.
    # lokale N-wegen, dan de overstap naar de noord-zuidas 25). Volume nul (geen bron
    # bevestigt geleverde Balama-vlok in Korea) — dat staat in de beennaam, niet hier.
    "grafiet-balama-saemangeum-saemangeum-sejong": {
        "via": [
            ("Future Graph Saemangeum — blok 6 (onzeker)", (126.5480, 35.9680)),
            ("Dong-Gunsan IC (Seohaean Expwy 15)",         (126.8342, 35.9452)),
            ("Iksan-knooppunt",                            (127.0971, 35.9504)),
            ("Nonsan-knooppunt (start Expwy 25)",          (127.0998, 36.0834)),
            ("POSCO Future M Sejong — anodefabriek 1",     (127.2203, 36.7059)),
        ],
        "id": "gr-saemangeum-sejong",
        "naam": "Future Graph Saemangeum → POSCO Future M Sejong "
                "(Route 21 → Seohaean Expwy 15 → Iksan JC → Nonsan JC → Expwy 25)",
        "extracts": ["zuid-korea"],
        "refs": ["15", "25", "21"],
        # ⚠️ GEEN GEPUBLICEERDE WEG-KM (brief §2/§7): 180 is de brief-schatting zelf
        # (hemelsbreed-achtige aanname, geen onafhankelijke bron) — dit is dus geen
        # echte lengtetoets, alleen een informatief getal; venster ruim gezet.
        "gepubliceerdKm": 180,
        "bronnoot": "geen publicatie — brief-schatting, geen onafhankelijke bron; "
                    "OSRM/wegnet bepaalt de echte km bij het bakken",
        "vensterKm": 60,
        "uit": "grafiet-balama-saemangeum-weg-saemangeum-sejong.geojson",
    },
    # Routebrief lithium-olaroz-naraha, been b1 (LICHTE werkwijze M29). Truck
    # (carbonaat in big bags) Olaroz-plant → Buenos Aires containerkade, dwars
    # over Argentinië: RN52 (Susques→Purmamarca) → RN9 (San Salvador de Jujuy)
    # → RN34/RN9-splitsing bij Tucumán → zuidwaarts via Rosario → Buenos Aires.
    # ⚠️ GEEN GEPUBLICEERDE WEG-KM (brief §7/§2): gepubliceerdKm hieronder is de
    #    hemelsbreed-som van de via-punten (~1.562 km, geen onafhankelijke
    #    bron) — venster ruim gezet, dit is geen echte lengtetoets.
    # ⚠️ RN52 BIJ OLAROZ LIGT OP ~3.900-4.200 M en kan in OSM lager geklasseerd
    #    zijn dan primary/trunk (brief §7) → corridorKlassen breed gezet.
    "lithium-olaroz-naraha-baires": {
        "via": [
            ("Olaroz-plant — Sales de Jujuy S.A. (Salar de Olaroz)", (-66.7025, -23.4629)),  # anker
            ("Purmamarca (RN52 → RN9-knoop)",                        (-65.4992, -23.7466)),
            ("San Salvador de Jujuy",                                (-65.2995, -24.1853)),
            ("Tucumán (RN34/RN9-splitsing)",                         (-65.2226, -26.8241)),
            ("Rosario",                                              (-60.6505, -32.9442)),
            ("Buenos Aires containerkade — TRP Puerto Nuevo",        (-58.3631, -34.5847)),  # anker
        ],
        "id": "li-olaroz-baires",
        "naam": "Olaroz-plant → Buenos Aires containerkade (RN52 → RN9 → RN34/RN9 → Rosario)",
        "extracts": ["argentina"],
        "refs": ["RN52", "52", "RN9", "9", "RN34", "34", "RN A008"],
        "gepubliceerdKm": 1562,
        "bronnoot": "niet gepubliceerd; hemelsbreed-som van de via-punten "
                    "(~1.562 km) als indirecte controle, geen onafhankelijke bron "
                    "(brief §7/§2)",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified", "residential"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "uit": "lithium-olaroz-naraha-weg-olaroz-baires.geojson",
    },
    # Routebrief lithium-olaroz-naraha, been b3 (LICHTE werkwijze M29). Truck
    # Onahama-kade → Toyotsu Lithium Naraha, Jōban-snelweg (E6)/Route 6
    # noordwaarts — geen tussenliggend via-punt (één doorgaande route, geen
    # corridorkeuze; brief §7).
    "lithium-olaroz-naraha-onahama-naraha": {
        "via": [
            ("Ōken-ふ頭 containerterminal, Onahama-haven",  (140.8695, 36.9245)),  # anker
            ("Toyotsu Lithium Naraha — hydroxidefabriek",  (140.9954, 37.2467)),  # anker
        ],
        "id": "li-onahama-naraha",
        "naam": "Onahama-kade → Toyotsu Lithium Naraha (Jōban-snelweg/Route 6)",
        "extracts": ["japan"],
        "refs": ["E6", "6", "Route 6"],
        "gepubliceerdKm": 35,
        "bronnoot": "Toyotsu Onahama-havenseminar 2024-02-02: kade↔extern "
                    "magazijn ~16 km/~30 min + resterend deel naar de fabriek, "
                    "~35 km totaal (brief bron [3])",
        "vensterKm": 20,
        "uit": "lithium-olaroz-naraha-weg-onahama-naraha.geojson",
    },
    # ── Routebrief lithium-pilgangoora-gwangyang, been b1 (LICHTE werkwijze M29) ──
    # Road trains Pilgan-plant (Pilgangoora, PLS) → Utah Point Bulk Handling
    # Facility, Port Hedland: mijnweg → Marble Bar Road → Great Northern
    # Highway → Utah Road. Via-punten = de vier corridorkeuzes uit de brief §4.
    # ⚠️ TWEE PROFIELEN, NIET ÉÉN — GEMETEN OSM-GRAAFBREUK BIJ SOUTH HEDLAND.
    #    De Dijkstra weigerde in één stuk: het GNH/stadsnet van Port Hedland
    #    (component met Utah Point, Wilson St, Great Northern Highway-tak de
    #    stad in) deelt GEEN knoop met het doorgaande GNH-net verderop zuid-
    #    waarts, ook niet met corridorKlassen erbij. Kleinste gemeten afstand
    #    tussen de twee componenten: 0,355 km (118.575136,-20.377913) ↔
    #    (118.574874,-20.374731) — een OSM-topologiegat, geen wegklasse-fout
    #    (beide zijden zijn zelf `trunk`/GNH). Dat gat wordt in bak_stromen.sh
    #    een korte `--stippel` tussen de twee scans; verder is niets aan de
    #    corridor bijgeschoven om dit te maskeren.
    #    Ook opgelost via `eindToegangPrivaat` (haulroad-vertakkingen bij de
    #    plant/Wodgina hangen als unclassified/service met access=private aan
    #    een eigen geïsoleerd netwerkje, comp. 247 knopen tot lon 118.909) en
    #    `corridorKlassen` (de kleine klassen tussen plant en Marble Bar Road,
    #    ~55 km hemelsbreed, liggen buiten de 12 km-eindzone van de ankers).
    "lithium-pilgangoora-gwangyang-plant-southhedland": {
        "via": [
            ("Pilgan-plant, Pilgangoora Operation (PLS)",     (118.8956, -21.0595)),  # anker
            ("mijnweg × Marble Bar Road",                     (118.92,   -21.00)),
            ("Strelley — Marble Bar Rd × Great Northern Hwy", (118.9512, -20.5162)),
            ("South Hedland (GNH-doorgang)",                  (118.5987, -20.4088)),
            ("GNH vóór het OSM-graafgat (zuidzijde)",         (118.575136, -20.377913)),
        ],
        "id": "li-pilgangoora-southhedland",
        "naam": "Pilgan-plant → GNH bij South Hedland (mijnweg → Marble Bar Rd → Great Northern Hwy)",
        "extracts": ["australie"],
        "refs": ["Great Northern Highway", "Marble Bar Road", "Utah Road", "1", "95"],
        "gepubliceerdKm": 105,
        "bronnoot": "geen eigen publicatie voor dit deelstuk; PLS geeft alleen het "
                    "totaal 'approximately 140 km SE of Port Hedland' [1] — de "
                    "toets van 130 km geldt de SOM van beide wegprofielen",
        "vensterKm": 40,
        "eindToegangPrivaat": True,
        "corridorKlassen": ["unclassified", "tertiary", "service", "residential"],
        "uit": "lithium-pilgangoora-gwangyang-weg-plant-southhedland.geojson",
    },
    "lithium-pilgangoora-gwangyang-southhedland-utahpoint": {
        "via": [
            ("GNH ná het OSM-graafgat (noordzijde, stadsnet)", (118.574874, -20.374731)),
            ("Utah Road-afslag vanaf GNH",                     (118.565,  -20.320)),
            ("Utah Point Bulk Handling Facility, Berth 4",     (118.5585, -20.3153)),  # anker
        ],
        "id": "li-southhedland-utahpoint",
        "naam": "GNH-stadsnet Port Hedland → Utah Point (Great Northern Hwy → Utah Road)",
        "extracts": ["australie"],
        "refs": ["Great Northern Highway", "Utah Road"],
        "gepubliceerdKm": 25,
        "bronnoot": "geen eigen publicatie voor dit deelstuk; zie de zusterprofiel-"
                    "noot — de toets van 130 km geldt de SOM van beide wegprofielen",
        "vensterKm": 40,
        "uit": "lithium-pilgangoora-gwangyang-weg-southhedland-utahpoint.geojson",
    },
    # ── Routebrief lithium-atacama-antofagasta (LICHTE werkwijze M29) ──
    # Been b1: LiCl-oplossing per tankwagen SQM Salar de Atacama → plantweg
    # (compacted, zuidpoort) → Ruta B-39 (in OSM: geen B-385, alléén B-39,
    # tertiary/chipseal) → Baquedano → Ruta 5 Norte zuidwest → PQL Carmen.
    # ⚠️ B-385 BESTAAT NIET IN OSM (brief §7): 0 ways met die ref op de
    # chili-extract; de weg heet er B-39. Zonder corridorKlassen tertiary
    # week de M25-fout ("geen wegpad") hierdoor af.
    # ⚠️ DE PLANTWEG (compacted `service`, 10,9-16 km) KAN BUITEN DE 12 KM-
    # EINDZONE VALLEN — dan blijft er een korte stippel over ("plantweg,
    # geen net op deze korrel"); niet dichtschuiven met een verzonnen via-punt.
    "lithium-atacama-carmen": {
        "via": [
            ("SQM Salar de Atacama — lithiumplant (laadplek)", (-68.4000, -23.5675)),
            ("plantweg, zuidpoort SQM-complex",                (-68.4060, -23.5700)),
            ("Ruta B-39 ná samenkomst van de twee plantwegen", (-68.5939, -23.6669)),
            ("Ruta B-39, knoop bij km ~64",                    (-68.8387, -23.5471)),
            ("Ruta B-39, bocht naar NW",                       (-69.4078, -23.4941)),
            ("Ruta B-39, vlak vóór Baquedano",                 (-69.7926, -23.3409)),
            ("Ruta 5 Norte, ZW van Baquedano",                 (-70.0523, -23.4488)),
            ("PQL Carmen — verwerkingsknoop (LiCl → Li2CO3)",  (-70.2600, -23.6335)),
        ],
        "id": "li-atacama-carmen",
        "naam": "SQM Salar de Atacama → PQL Carmen (plantweg → Ruta B-39 → Baquedano → Ruta 5)",
        "extracts": ["chili"],
        "refs": ["B-39", "5", "Ruta 5"],
        "gepubliceerdKm": 255,
        "bronnoot": "SQM 20-F: 'approximately 255 km from the Salar de Atacama'; "
                    "Antofagasta–salar via B-385 272 km; via-keten hemelsbreed 211",
        "vensterKm": 40,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "stroombeen-atacama-carmen.geojson",
    },
    # Been b2: carbonaat/hydroxide (big bags in containers) PQL Carmen →
    # ATI-kade Puerto Antofagasta, over Ruta 5 (3 km) → Ruta 26 / Av. Salvador
    # Allende → havenpoort.
    "lithium-carmen-antofagasta": {
        "via": [
            ("PQL Carmen — verwerkingsknoop",                  (-70.2600, -23.6335)),
            ("kruising Ruta 5 / Ruta 26",                      (-70.2685, -23.6047)),
            ("Ruta 26 op de Cuesta",                           (-70.3438, -23.6253)),
            ("Av. Salvador Allende (Ruta 26 in de stad)",      (-70.3960, -23.6287)),
            ("Puerto Antofagasta, ATI — kade (overslag naar zee)", (-70.4088, -23.6500)),
        ],
        "id": "li-carmen-antofagasta",
        "naam": "PQL Carmen → Puerto Antofagasta ATI (Ruta 5 → Ruta 26 → Av. Salvador Allende)",
        "extracts": ["chili"],
        "refs": ["5", "Ruta 5", "26", "Ruta 26"],
        "gepubliceerdKm": 19,
        "bronnoot": "SQM 20-F: 'ports of Antofagasta (15 km west of the Salar del "
                    "Carmen)'; plant '20 km east of Antofagasta'; via-keten 19",
        "vensterKm": 15,
        "uit": "stroombeen-carmen-antofagasta.geojson",
    },
    # Routebrief grafiet-lakecharles-desoto, been b1 (LICHTE werkwijze M29).
    # Truck (werkaanname) Lake Charles cokesveld → Novonix Riverside
    # (Chattanooga TN), I-10 → I-12 → I-59 → I-24. Via-punten = de zes
    # corridorkeuzes uit de brief §4 (b1).
    # ⚠️ KOP OP PRIVÉ-TERREINWEGEN: het cokesveld ligt binnen het Phillips 66
    #    Lake Charles-complex (`highway=service access=private`, 71 ways op
    #    het terrein, brief §3/[13]) → eindToegangPrivaat binnen de 12-km-zone.
    # ⚠️ GEEN GEPUBLICEERDE LENGTE (brief §2): 1.086 km is OSRM over OSM [15],
    #    dezelfde bron als deze extract — de lengtetoets loopt hier tegen
    #    zichzelf. Rapporteren, niet als onafhankelijke bevestiging lezen.
    "grafiet-lakecharles-desoto-lakecharles-riverside": {
        "via": [
            ("P66 Lake Charles — cokesveld/coker",       (-93.2770, 30.2420)),   # anker
            ("I-12 oost van Baton Rouge (Walker)",       (-90.8576, 30.4707)),
            ("I-59 noord van Slidell (Pearl River)",     (-89.7265, 30.4031)),
            ("I-59 noord van Hattiesburg",                (-89.3252, 31.3798)),
            ("I-20/59 oost van Meridian",                 (-88.5772, 32.3964)),
            ("I-59 NO van Birmingham (Trussville)",       (-86.6237, 33.6342)),
            ("I-24 Chattanooga, Lookout Valley",          (-85.3830, 35.0188)),
            ("Novonix Riverside — fabriek",               (-85.3243, 35.0388)),   # anker
        ],
        "id": "gr-lakecharles-riverside",
        "naam": "P66 Lake Charles — cokesveld → Novonix Riverside (I-10 → I-12 → I-59 → I-24)",
        "extracts": ["us-louisiana", "us-mississippi", "us-alabama", "us-tennessee"],
        "refs": ["I-10", "I-12", "I-59", "I-20", "I-24", "10", "12", "59", "20", "24"],
        "gepubliceerdKm": 1086,
        "bronnoot": "OSRM over OSM (routebrief §2/[15], 2026-09-26); geen gepubliceerde "
                    "lengte — de lengtetoets loopt tegen dezelfde bron als deze extract",
        "vensterKm": 40,
        "eindToegangPrivaat": True,
        "uit": "grafiet-lakecharles-desoto-weg-lakecharles-riverside.geojson",
    },
    # Routebrief grafiet-lakecharles-desoto, been b2 (LICHTE werkwijze M29).
    # Truck (werkaanname) Novonix Riverside → De Soto-routeerpunt (rotonde
    # Astra Parkway), I-24 → I-57 → I-64 → I-70 → I-435 → K-10. Via-punten =
    # de acht corridorkeuzes uit de brief §4 (b2). ⚠️ EINDIGT OP HET
    #    ROUTEERPUNT, NIET HET TERREINANKER — zelfde vorm als
    #    grafiet-vidalia-desoto/-desoto-casagrande in dit bestand: het
    #    fabrieksterrein (38.93815,-95.00240) is over de weg niet bereikbaar,
    #    de docks zijn niet gelegd (brief §3).
    "grafiet-lakecharles-desoto-riverside-desoto": {
        "via": [
            ("Novonix Riverside — fabriek",               (-85.3243, 35.0388)),   # anker
            ("I-24 W bij Kimball/Jasper",                 (-85.6740, 35.0424)),
            ("I-24 NW Nashville, ná I-65/I-40",           (-86.7805, 36.2293)),
            ("I-57 N ná het einde van I-24 (Pulleys Mill IL)", (-88.9763, 37.6474)),
            ("I-64 W ná I-57 (Mt Vernon IL)",             (-89.0286, 38.3621)),
            ("I-70 W Wentzville MO",                       (-90.8696, 38.8102)),
            ("I-435 Z ná I-70 (Kansas City)",             (-94.5006, 39.0306)),
            ("K-10 Lenexa, ná I-435",                      (-94.7779, 38.9423)),
            ("K-10 × Lexington Ave, De Soto",             (-94.9665, 38.9602)),
            ("Astra Parkway — rotonde (routeerpunt)",      (-95.00748, 38.94196)),  # routeerpunt
        ],
        "id": "gr-riverside-desoto",
        "naam": "Novonix Riverside → De Soto-routeerpunt (I-24 → I-57 → I-64 → I-70 → I-435 → K-10)",
        "extracts": ["us-tennessee", "us-kentucky", "us-illinois", "us-missouri", "us-kansas"],
        "refs": ["I-24", "I-57", "I-64", "I-70", "I-435", "K-10", "24", "57", "64", "70",
                 "435", "10"],
        "gepubliceerdKm": 1152,
        "bronnoot": "OSRM over OSM (routebrief §2/[15], 2026-09-26); geen gepubliceerde "
                    "lengte — de lengtetoets loopt tegen dezelfde bron als deze extract",
        "vensterKm": 40,
        "uit": "grafiet-lakecharles-desoto-weg-riverside-desoto.geojson",
    },
    # Routebrief grafiet-balama-laixi, been b3 (LICHTE werkwijze M29). Enige
    # weg-scan van deze stroom: b1 (Balama→Nacala) is een letterlijke kopie van
    # bak_grafiet been 1, b2 is de MARNET-zeerouter. Kop = QQCT Qianwan-kade
    # (aannemelijk, §3), staart = Qingdao Shinestar-fabriek in Nanshu
    # (bron-gelegd, MEE-vergunning). Vijf via-punten pinnen de corridorkeuze om
    # de Jiaozhou-baai (§4 van de brief): westelijke haven-uitvalsweg i.p.v.
    # de baaibrug, doorrijden op G15 i.p.v. G204/S202 door Jimo, afrit naar de
    # S214 i.p.v. Laixi-stad. ⚠️ Geen gepubliceerde km — brief-toets loopt tegen
    # OSRM (149,6 km, zelfde OSM-bron); *aannemelijk: één bron* (contract 2018).
    "grafiet-balama-laixi-qingdao-nanshu": {
        "via": [
            ("Qingdao Qianwan Container Terminal (QQCT) — kade",  (120.2070, 36.0124)),   # anker (aannemelijk)
            ("S7602 uitrit havengebied (2号疏港高速)",              (120.1528, 36.0449)),
            ("samenvloeiing G22 青兰高速 → G15 沈海高速",           (119.9736, 36.0573)),
            ("G15 ten noorden van Jiaozhou (splitsing)",           (120.0259, 36.3890)),
            ("afrit G15 → S214 南城路 (Laixi-west)",                (120.3366, 36.7634)),
            ("S214 aankomst Nanshu, afslag industriezone",         (120.3339, 37.0170)),
            ("Qingdao Shinestar SPG-fabriek, Nanshu",              (120.3224, 37.0252)),   # anker (bron-gelegd)
        ],
        "id": "gr-qingdao-qqct-laixi-shinestar",
        "naam": "QQCT Qianwan-kade → Qingdao Shinestar-fabriek, Nanshu "
                "(S7602 → G22 → G15 om de Jiaozhou-baai → S214)",
        "extracts": ["china"],
        "refs": ["S7602", "G22", "G15", "S214"],
        "gepubliceerdKm": 150,
        "bronnoot": "OSRM over OSM 149,6 km (geen onafhankelijke publicatie; "
                    "contract Langruite 2018/2019)",
        "vensterKm": 40,
        "uit": "stroombeen-qingdao-qqct-laixi-shinestar.geojson",
    },
    # Routebrief lithium-bikita-zhangjiagang, been b1. A9/P4 (Mutare-Masvingo
    # Highway, ZW) → Forbes/Machipanda-grens → EN6 (Beira-corridor, MZ).
    "lithium-bikita-zhangjiagang-bkplant-beira": {
        "via": [
            ("Bikita Minerals — concentratorplant",      (31.4245, -19.9512)),   # anker
            ("mijnafrit op de A9/P4",                     (31.4148, -19.9721)),
            ("Nyika, A9/P4",                               (31.5915, -20.0001)),
            ("Birchenough Bridge (Save-oversteek)",        (32.3460, -19.9614)),
            ("Wengezi, A9/P4",                             (32.5318, -19.5095)),
            ("Forbes Border Post, N6",                     (32.7123, -19.0052)),
            ("Chimoio, N6-doorgaande weg",                 (33.4838, -19.1283)),
            ("Inchope, EN6 × EN1",                         (33.9326, -19.2072)),
            ("Dondo, N6",                                  (34.7460, -19.6165)),
            # ⚠️ EINDIGT NIET OP DE KADE: gemeten (2026-09-26) dat Cornelder's
            # havenstraten (`service`, geen access-tag) in OSM een EIGEN, VAN
            # HET DOORGAANDE NET LOSSTAAND clustertje vormen (component van 2
            # knopen op ≤0,25 km van de kade) — precies de "OSM kent de
            # havenstraten niet"-uitzondering uit de brief. De laatste
            # connected knoop op het net ligt op de N6-havenweg-inrit (Av.
            # Samora Machel), 1,82 km van de kade — vrijwel exact de "1,8 km"
            # die de brief bij via-punt 8 al noemt. Vanaf hier een stippel.
            ("N6 — havenweg-inrit Beira (Av. Samora Machel)", (34.848737, -19.823623)),
        ],
        "id": "li-bkplant-beira",
        "naam": "Bikita — concentratorplant → Forbes/Machipanda → Beira, N6-havenweg-inrit (A9/P4 → N6/EN6)",
        "extracts": ["zimbabwe", "mozambique"],
        "refs": ["A9", "P4", "N6", "EN6"],
        "gepubliceerdKm": 525,
        "bronnoot": "som van deelstukken (Masvingo-Mutare ~70+298 km + Mutare-Forbes ~8 + EN6 289 km); geen bron geeft de rit als geheel; dit profiel meet tot 1,82 km vóór de kade (zie hierboven)",
        "vensterKm": 40,
        "uit": "lithium-bikita-zhangjiagang-weg-bkplant-beira.geojson",
    },
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

    # ── Routebrief koper-collahuasi-tongling, benen 4 en 5 (2026-08-06) ──────
    # FASE D: kathode verlaat het TNMG-smeltercomplex en gaat naar de
    # foliefabriek 铜冠铜箔, beide in de 铜陵经开区.
    #
    # ⚠️ DE KOP IS EEN SUBSTITUUT (besluit Lars, koperronde Guixi). De echte
    #    kathode-expeditie is NIET gevonden, en dat heeft twee gemeten oorzaken
    #    die elkaar niet vervangen: (a) het emissievergunningregister geeft één
    #    punt per vergunning — de vestiging, niet de deur; (b) Esri heeft hier
    #    GEEN z19 (z19 én z20 leveren op alle drie de punten exact 2.521 byte
    #    placeholder, terwijl z17/z18 16-18 kB echte tegels geven), dus z18 =
    #    0,51 m/px is de fijnste korrel en een laadperron van 10-15 m ligt op de
    #    resolutiegrens. Vijfde bevestigde zoomplafond na Guixi, Zhangjiagang,
    #    Tianqi en Chizhou. Het procesgat dat daardoor blijft staan (0-700 m, het
    #    金冠-perceel meet 98,5 ha) ÍS het ontbrekende anker — niet dichttrekken.
    # ⚠️ DE KOP IS 金冠铜业, NIET 金新铜业, en dat is een wijziging aan ladder 5
    #    van de brief. 金冠 is het bestaande 760 kt/a-blok dat de foliefabriek al
    #    levert sinds fase 1 in dec 2017 draaide; 金新 werd pas ontstoken op
    #    2025-03-26 en is principieel niet satelliet-te-leggen omdat de hele
    #    Tongling-scene één opname van 2019-04-05 is (identify-service SRC_DATE2)
    #    — daar staat nog rauw struweel. [D6] documenteert de interne levering op
    #    CONCERNniveau, dus 金冠 spreekt de bron niet tegen.
    # ⚠️ DE ZUIDPOORT IS GEKOZEN DOOR TE METEN, NIET DOOR TE KIEZEN: een Dijkstra
    #    vanaf het registerpunt naar de foliefabriek neemt vanzelf de zuidpoort
    #    (7,41 km) boven de noordpoort (8,70 km). Beide poorten zijn op z18
    #    gelegd (poortwachterspaar in een onderbroken haag-/muurlijn); komt er
    #    later een bron die de noordpoort aanwijst, dan verandert alleen dit been.
    "koper-tongling-lastmile": {
        "via": [
            ("金冠铜业分公司 — registerpunt (substituut-kop)", (117.78548, 30.99602)),
            ("terreinpoort zuid (翠湖六路-zijde)",              (117.78146, 30.99156)),
            ("aansluiting openbaar net (翠湖六路)",             (117.78147, 30.99058)),
        ],
        "id": "cu-tongling-lastmile",
        "naam": "kathode 金冠铜业 → poort → openbaar net (翠湖六路)",
        "extracts": ["china"],
        "refs": [],
        "gepubliceerdKm": 1.04,
        "bronnoot": "eigen meting 2026-08-06 over het interne servicenet van het "
                    "金冠-terrein (OSM service-ways 1247093604/1247093607/"
                    "1247093593); geen bron publiceert deze afstand. Identiteit "
                    "van het blok vastgelegd via het 四至 uit het gemeentelijke "
                    "verificatiebesluit over het 奥炉改造工程 van 金冠铜业分公司: "
                    "'西湖二路以南，翠湖六路以北'",
        "vensterKm": 3,
        "uit": "stroombeen-tongling-lastmile.geojson",
    },

    # ⚠️ DE STAART MOET GETRIMD WORDEN — overschiet-en-terug-klasse. De
    #    dichtstbijzijnde OSM-KNOOP ligt 50 m voorbij de projectie van het
    #    folie-anker op 翠湖二路; ongetrimd rijdt de lijn de poort voorbij en
    #    keert terug. Zelfde klasse als het Guixi-eindpunt (792 m voorbij) en de
    #    grafiet-via-punten. snoei_keerlussen vangt de lus; de lengte hoort ná de
    #    snoei gemeten te worden — meet het eindproduct, niet je meetlat.
    # ⚠️ HET STAARTANKER IS EEN VESTIGINGSPUNT, GEEN LOSDOCK. Drie officiële
    #    coördinaten liggen binnen 256 m op hetzelfde ommuurde perceel
    #    (MEE-register 30.96174/117.81059 · EIA 厂区中心 30.96330/117.81123 ·
    #    水土保持 30.96288/117.81292). Het procesgat naar het echte losdock
    #    (~150-300 m) blijft bewust staan.
    # ⚠️ GEBRUIK OSM-POLYGOON way/1247093617 NIET. Die draagt de naam-tag
    #    铜冠铜箔有限公司 maar omsluit in werkelijkheid 铜冠黄铜棒材 (翠湖二路
    #    2135号), 400 m westelijker — een armchair-edit, v1, geen source-tag.
    #    Dit is de gevaarlijke variant van de OSM-regel: niet een LEGE uitslag,
    #    maar een POSITIEVE en foute.
    "koper-tongling-folie": {
        "via": [
            ("aansluiting openbaar net (翠湖六路)",   (117.78147, 30.99058)),
            ("铜冠电子铜箔 — 翠湖二路西段789号",       (117.81051, 30.96137)),
        ],
        "id": "cu-tongling-folie",
        "naam": "kathode → 铜冠铜箔 basis Tongling (翠湖六路 / 长山大道 / 翠湖二路)",
        "extracts": ["china"],
        # Zachte voorkeur (factor 3): 五松山大道 draagt in OSM de ref S335. De
        # overige assen zijn benoemde stadswegen zonder ref.
        "refs": ["S335"],
        "gepubliceerdKm": 6.38,
        "bronnoot": "eigen meting 2026-08-06; geen bron publiceert deze "
                    "binnenzone-rit. Corridor gemeten als 翠湖六路 1.438 m → "
                    "长山大道 1.974 m → 五松山大道/S335 619 m → tertiary "
                    "479567771 1.276 m → 479567772 806 m → 翠湖二路 248 m",
        "vensterKm": 6,
        "trimStaart": True,
        "uit": "stroombeen-tongling-folie.geojson",
    },

    # ── Routebrief koper-kolwezi-durban (LICHTE werkwijze M29, 2026-09-24) ──
    # Been 1: SX-EW-kathode TFM-plant (CMOC, Fungurume) → Durban DCT Pier 2 —
    # de Copperbelt-truckcorridor (~3.000 km; de M25-bake cu-copperbelt-durban
    # kwam op 3.068,8 km). Via-punten = OSM-wegvertices uit die M25-corridor, in
    # reisvolgorde; de grensposten Kasumbalesa, Chirundu en Beitbridge zijn de
    # verplichte tussenankers (wegcorridors.md). ⚠️ Venster 75 km: RN39 buigt
    # bij Fungurume 53 km uit de rechte lijn. ⚠️ Buccleuch (N1/N3) komt uit een
    # bake die door het Johannesburg-centrum liep — toets dat de lijn erna de
    # N3 (Heidelberg) neemt en niet de M1/M2. Kop = plant-hart (EW-hallen op
    # z15); de kathode-expeditiehal is niet gevonden (brief §7).
    "koper-tfm-durban": {
        "via": [
            ("TFM-plant Fungurume (EW-hallen)",       (26.1975, -10.5685)),
            ("Likasi RN39→RN1",                        (26.7355, -10.9806)),
            ("Lubumbashi RN1",                         (27.4827, -11.6642)),
            ("Kasumbalesa (grens DRC/Zambia)",         (27.7959, -12.2658)),
            ("Ndola T3",                               (28.6367, -12.9688)),
            ("Kabwe T2",                               (28.4400, -14.4426)),
            ("Lusaka T2",                              (28.2835, -15.4278)),
            ("Chirundu (grens Zambia/Zimbabwe)",       (28.8471, -16.0338)),
            ("Harare A1→A4",                           (31.0467, -17.8362)),
            ("Masvingo A4",                            (30.8343, -20.0720)),
            ("Beitbridge (grens Zimbabwe/RSA)",        (29.9858, -22.2206)),
            ("Polokwane N1",                           (29.4813, -23.9215)),
            ("Buccleuch N1/N3-splitsing",              (28.0991, -26.0464)),
            ("Durban DCT Pier 2, noordkade",           (31.0160, -29.8790)),
        ],
        "id": "cu-tfm-durban",
        "naam": "TFM-plant Fungurume → Durban DCT Pier 2 (RN39/RN1 → T3/T2 → "
                "A1/A4 → N1/N3)",
        "extracts": ["congo-drc", "zambia", "zimbabwe", "zuid-afrika"],
        # Zachte voorkeur (factor 3): de refs per land; "N1" matcht zowel de
        # Congolese RN1-schrijfwijze N1 als de Zuid-Afrikaanse N1.
        "refs": ["RN39", "RN1", "N1", "T3", "T2", "A1", "A4", "N3"],
        "gepubliceerdKm": 3000,
        "bronnoot": "wegcorridors.md ~3.000 km (Copperbelt → Durban); "
                    "routeplanner 3.035; eigen M25-bake 3.068,8 km (+2,3%)",
        "vensterKm": 75,
        "uit": "stroombeen-tfm-durban.geojson",
    },

    # ── Routebrief koper-lasbambas-matarani (LICHTE werkwijze M29, 2026-09-24) ──
    # Been 1: concentraat Las Bambas (MMG) → overslagstation Pillones, de
    # "corredor minero del sur": PE-3SF → PE-3SY (RM 054-2019: Mara – Ccapacmarca
    # – Yavi Yavi – Velille) → PE-3SG (Velille–Yauri) → PE-34E/34J (Yauri–Imata)
    # → PE-34A. ⚠️ Het EIA-2011-tracé liep via Haquira–Santo Tomás; de 2e MEIA
    # en de blokkades (Mara, Ccapacmarca, Yavi Yavi) leggen de trucks op de
    # Mara-route — die is getekend. Via-punten = vertices van de M25-corridor
    # (landnet_weg.geojson), ~3 km ná elke afslag, dus per constructie op de weg.
    # Kop = concentrator (z15); de mijnweg naar PE-3SF (5–6 km) valt onder de
    # eindklassen mét 'track' (mijnwegen heten in OSM vaak zo).
    "koper-lasbambas-pillones": {
        "via": [
            ("Las Bambas — concentrator (laadplek)",   (-72.3357, -14.0894)),
            ("PE-3SF ná Challhuahuacho",               (-72.2319, -14.1014)),
            ("Mara",                                   (-72.1042, -14.0876)),
            ("Ccapacmarca",                            (-71.9957, -14.0059)),
            ("Yavi Yavi",                              (-71.9620, -14.1927)),
            ("PE-3SG oost van Velille",                (-71.8590, -14.5101)),
            ("PE-34E zuid van Yauri (Espinar)",        (-71.4165, -14.8222)),
            ("Condoroma",                              (-71.1384, -15.3000)),
            ("PE-34A ZW van Imata",                    (-71.1063, -15.8436)),
            ("Pillones — overslagstation (spoorlus)",  (-71.2184, -15.9842)),
        ],
        "id": "cu-lasbambas-pillones",
        "naam": "Las Bambas concentrator → Pillones (PE-3SF → PE-3SY → PE-3SG → "
                "PE-34E/34J → PE-34A)",
        "extracts": ["peru"],
        # Zachte voorkeur (factor 3); OSM-Peru schrijft de refs wisselend met en
        # zonder spatie/koppelteken.
        "refs": ["PE-3SF", "PE-3S F", "PE-3SY", "PE-3S Y", "PE-3SG", "PE-3S G",
                 "PE-34E", "PE-34J", "PE-34A", "3SF", "3SY", "3SG", "34E", "34A"],
        "gepubliceerdKm": 450,
        "bronnoot": "ProActivo 730 km totaal (weg+spoor) − ~285 spoor; fetch_landnet "
                    "450; wegcorridors.md 435; corridor Progreso→Pillones 482,2 "
                    "(RM); oude M25-bake 411,5 km vanaf PE-3SF",
        "vensterKm": 50,
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "uit": "stroombeen-lasbambas-pillones.geojson",
    },

    # ── Routebrief koper-elteniente-rotterdam (LICHTE werkwijze M29) ──
    # Been 2: anodes per truck Caletones-smelter → Estación de Transferencia
    # El Olivar/Los Lirios (ETEO) bij Rancagua, via de H-25 (Carretera del
    # Cobre). ⚠️ ETEO-anker is ONZEKER (emplacement 1,7 km NNO van station Los
    # Lirios); de km (±75) zijn afgeleid, H-25 = 63 km Rancagua→Caletones.
    "koper-caletones-eteo": {
        "via": [
            ("Caletones-smelter (anodes)",             (-70.4503, -34.1061)),
            ("Rancagua (H-25 → Ruta 5)",               (-70.7407, -34.1702)),
            ("ETEO — El Olivar/Los Lirios (overslag)", (-70.7748, -34.2118)),
        ],
        "id": "cu-caletones-eteo",
        "naam": "Caletones → ETEO Los Lirios (H-25 Carretera del Cobre → Ruta 5)",
        "extracts": ["chili"],
        "refs": ["H-25", "5", "Ruta 5", "H-10"],
        "gepubliceerdKm": 75,
        "bronnoot": "afgeleid: H-25 = 63 km Rancagua→Caletones/Sewell + ~12 km "
                    "Rancagua→ETEO; geen bron publiceert het geheel",
        "vensterKm": 25,
        # De Carretera del Cobre is in OSM `unclassified` (access=permit) over
        # ~60 km, met stukken `secondary`/`tertiary` (H-27/H-25): corridor-breed
        # toelaten, anders "geen wegpad tussen punt 0 en 1" (gemeten 2026-09-25).
        "corridorKlassen": ["unclassified", "tertiary"],
        # De smelter hangt via Codelco's privé-servicewegen (Tramo 3, Puente
        # Confluencia) aan de Carretera del Cobre — gemeten op de ongefilterde
        # OSM-graaf 2026-09-25. Alleen binnen de 12-km-eindzone.
        "eindToegangPrivaat": True,
        "uit": "stroombeen-caletones-eteo.geojson",
    },
    # ⚠️ BOVENSTAAND PROFIEL ROUTEERT NIET: OSM heeft in de Carretera del Cobre
    # een gat van 2,8 km tussen het einde van de oude weg (-34.15062,-70.54925)
    # en Confluencia (-34.17568,-70.54976) — de nieuwe weg Maitenes–Confluencia
    # staat er alleen als highway=proposed (gemeten op de ongefilterde graaf,
    # 2026-09-25). Daarom twee gemeten stukken + een stippel in de bake.
    "koper-caletones-maitenes": {
        "via": [
            ("Caletones-smelter (anodes)",                  (-70.4503, -34.1061)),
            ("Variante Caletones / Carretera del Cobre",    (-70.50305, -34.09862)),
            ("einde gekarteerde oude weg (vóór het gat)",   (-70.54925, -34.15062)),
        ],
        "id": "cu-caletones-maitenes",
        "naam": "Caletones → Maitenes (Carretera del Cobre, oude weg; privé-servicewegen Codelco)",
        "extracts": ["chili"],
        "refs": ["H-25", "H-27"],
        "gepubliceerdKm": 18.5,
        "bronnoot": "eigen meting op de ongefilterde OSM-graaf (2026-09-25): 18,5 km",
        "vensterKm": 15,
        "corridorKlassen": ["unclassified", "tertiary"],
        "eindToegangPrivaat": True,
        "uit": "stroombeen-caletones-maitenes.geojson",
    },
    # ⚠️ TWEEDE GAT (gemeten 2026-09-25): tussen Coya (-34.19657,-70.57698) en
    # (-34.19650,-70.61359) staat de H-27 in OSM 5,6 km als highway=track, en
    # track komt de scanner niet door — óók niet via corridorKlassen. Daarom
    # nog een knip: Confluencia → Coya gemeten, stippel over de track-strook,
    # Rancagua-rand → ETEO gemeten.
    "koper-confluencia-coya": {
        "via": [
            ("Confluencia — begin gekarteerde weg (ná het gat)", (-70.54976, -34.17568)),
            ("Coya — einde H-27 secondary (vóór de track-strook)", (-70.57698, -34.19657)),
        ],
        "id": "cu-confluencia-coya",
        "naam": "Confluencia → Coya (Carretera del Cobre, unclassified/permit → H-27)",
        "extracts": ["chili"],
        "refs": ["H-27", "H-25"],
        "gepubliceerdKm": 4.6,
        "bronnoot": "eigen meting op de ongefilterde OSM-graaf: 16,0 → 20,6 km = 4,6 km",
        "vensterKm": 10,
        "corridorKlassen": ["unclassified", "tertiary"],
        "uit": "stroombeen-confluencia-coya.geojson",
    },
    "koper-coya-eteo": {
        "via": [
            ("Carretera del Cobre H-27 — ná de track-strook", (-70.61359, -34.19650)),
            # ⚠️ Via-punt ÓP de doorgaande weg (Av. Miguel Ramírez, primary), niet
            # in het voetgangerscentrum: daar snapt het punt op een los stukje
            # unclassified en meldt de bake "geen wegpad" (gemeten 2026-09-25).
            ("Rancagua — Av. Miguel Ramírez (primary)",      (-70.70146, -34.17579)),
            ("ETEO — El Olivar/Los Lirios (overslag)",       (-70.7748, -34.2118)),
        ],
        "id": "cu-coya-eteo",
        "naam": "Coya-rand → Rancagua → ETEO (H-27 → Ruta 5)",
        "extracts": ["chili"],
        "refs": ["H-27", "5", "Ruta 5"],
        "gepubliceerdKm": 20,
        "bronnoot": "afgeleid: ongefilterde graaf 26,5 → 39,6 km Rancagua-centrum (13,1) + ~5 km naar ETEO",
        "vensterKm": 20,
        "corridorKlassen": ["unclassified", "tertiary"],
        "uit": "stroombeen-coya-eteo.geojson",
    },
    # Been 4: kathode per truck Ventanas-raffinaderij → Puerto San Antonio
    # (Codelco-pilot juli 2026: vaste truckcorridor, 130 km). Via Concón,
    # Casablanca (Ruta 68) en Algarrobo (F-90). ⚠️ San Antonio-kade ONZEKER
    # (westkade espigón DP World/Puerto Central; STI Molo Sur 400 m W).
    "koper-ventanas-sanantonio": {
        "via": [
            ("Ventanas-raffinaderij (kathode)",        (-71.4816, -32.7596)),
            ("Concón (F-30-E)",                        (-71.5160, -32.9220)),
            ("Casablanca (Ruta 68)",                   (-71.4101, -33.3206)),
            ("Algarrobo (F-90)",                       (-71.6681, -33.3692)),
            ("San Antonio — espigón (kathodekade)",    (-71.6170, -33.5885)),
        ],
        "id": "cu-ventanas-sanantonio",
        "naam": "Ventanas → Puerto San Antonio (F-30-E → Ruta 68 → F-90 → G-98-F)",
        "extracts": ["chili"],
        "refs": ["F-30-E", "F-30", "60", "68", "Ruta 68", "F-90", "G-98-F", "78"],
        "gepubliceerdKm": 130,
        "bronnoot": "Codelco-pilot 2026: truckcorridor Ventanas → San Antonio 130 km",
        "vensterKm": 30,
        "uit": "stroombeen-ventanas-sanantonio.geojson",
    },

    # ── Routebrief koper-oyutolgoi-china (LICHTE werkwijze M29) ──
    # Eén scan voor de hele landketen: concentraat per truck Oyu Tolgoi-
    # concentrator → OT-betonweg (105 km, OT LLC) → grenspost Gashuun Sukhait →
    # bonded warehouse ~7 km achter de grens (dezelfde Mongoolse trucks, geen
    # drager-wissel — NI 43-101) → G242 → G335 → Bayannur Feishang Copper
    # (Qingshan-industriepark; 158,2 kt OT-concentraat in 2022). ⚠️ Bij het
    # bakken wordt de lijn gesplitst op het bonded-anker (twee benen: OT →
    # bonded, bonded → smelter). De km-toets geldt het geheel: 105 + 7 + ~198
    # (OSRM) ≈ 310. ⚠️ De bonded-loods is AANNEMELIJK (welke loods "Huafang" is,
    # is niet gebrond).
    "koper-oyutolgoi-feishang": {
        "via": [
            ("Oyu Tolgoi — concentrator/zakkenplant",   (106.8360, 43.0480)),
            ("OT-betonweg (1)",                          (106.9657, 42.9945)),
            ("OT-betonweg (2)",                          (107.3890, 42.7729)),
            ("OT-betonweg (3) — vs. Tavan Tolgoi-kolenweg", (107.5437, 42.5785)),
            ("Gashuun Sukhait — grenspost",              (107.5692, 42.4146)),
            ("Ganqimaodu — Chinese poort/douanezone",    (107.5743, 42.4089)),
            ("bonded warehouse (Huafang, aannemelijk)",  (107.5990, 42.3740)),
            ("G242 zuid van Ganqimaodu",                 (107.5711, 42.3887)),
            ("afrit G242 → G335",                        (107.3697, 41.2704)),
            ("Bayan Baolige (G335)",                     (107.0729, 41.0790)),
            ("Bayannur Feishang Copper — smelter",       (106.8530, 40.9694)),
        ],
        "id": "cu-oyutolgoi-feishang",
        "naam": "Oyu Tolgoi → Gashuun Sukhait/Ganqimaodu → bonded → Feishang-smelter "
                "(OT-weg → G242 → G335)",
        "extracts": ["mongolia", "china"],
        "refs": ["G242", "G335", "S212"],
        "gepubliceerdKm": 310,
        "bronnoot": "OT-weg 105 km (OT LLC) + ~7 km grens→bonded (NI 43-101) + "
                    "~198 km bonded→Feishang (OSRM; geen publicatie)",
        "vensterKm": 40,
        # De OT-weg staat in OSM als 'Оюутолгой - Цагаанхад' (tertiary, asfalt)
        # + 'Цагаан хад - Гашуун сухайт' (primary): zonder tertiary corridor-breed
        # week de eerste bake (2026-09-25) uit naar het westen (129 km i.p.v. 105,
        # via-punt 2 op 14 km naast de weg).
        "corridorKlassen": ["tertiary"],
        "uit": "stroombeen-oyutolgoi-feishang.geojson",
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
# ⚠️ CORRIDOR-BREED TOEGELATEN KLEINE KLASSEN, per profiel via "corridorKlassen"
# (2026-09-25, lichte werkwijze M29). Nodig omdat sommige échte corridors in OSM
# geen WEG_HOUD-klasse dragen: de Carretera del Cobre (Caletones → Rancagua, de
# anodeweg van El Teniente) is `unclassified` + access=permit over ~60 km, en de
# OT-betonweg naar Gashuun Sukhait is een privé-mijnweg. Zonder deze sleutel
# vallen die ways buiten de 12-km-eindzone weg en meldt de bake "geen wegpad".
# Een klasse hoort óók in eindKlassen te staan (de tag-filter), anders komt hij
# de graaf nooit in. Bewust per profiel en niet globaal: corridor-breed
# `unclassified` trekt anders elk dorpsspoor het venster in.
CORRIDOR_KLASSEN = ()
# ⚠️ PRIVÉ-TOEGANG BINNEN DE EINDZONE, per profiel via "eindToegangPrivaat": True
# (2026-09-25). Codelco's Caletones-smelter hangt uitsluitend via
# `highway=service access=private`-wegen (Tramo 3, Puente Confluencia) aan de
# Carretera del Cobre; zonder deze sleutel is er "geen wegpad tussen punt 0 en
# 1". Geldt ALLEEN voor de kleine eindklassen (dus binnen EIND_STRAAL_KM van
# plant/kade) — de hoofdroute blijft de access-regel van fetch_landnet houden.
EIND_TOEGANG_PRIVAAT = False

TOLERANTIE = 0.10                   # de brief-toets: ±10%

# Worden in main() gezet uit het gekozen profiel.
VIA_PUNTEN = []
CORRIDOR = {}
BRON = "geofabrik"      # --bron; zie _ways_uit_overpass()
_PROFIEL_NAAM = ""      # --profiel; alleen voor de opt-in-sleutels
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


def _trim_staart(pts, anker):
    """Knip de gerouteerde lijn op de PROJECTIE van het staartanker, in plaats
    van er een stub naartoe terug te leggen.

    ⚠️ DE OVERSCHIET-EN-TERUG-KLASSE, NU OP HET BEEN-EINDE. `corridor_keten`
    eindigt op de dichtstbijzijnde graafKNOOP, en die kan vóórbij het anker
    liggen; main() plakt daarna het anker er als recht stukje achter. Het
    resultaat rijdt de poort voorbij en keert terug — precies wat bij Guixi
    792 m kostte en de lengtetoets op +29,0% zette (`knip_osm_been.py`, 05-08).
    `snoei_keerlussen` kan dit per constructie niet vangen: die draait vóór het
    aanplakken van het anker, dus de lus bestaat op dat moment nog niet.

    Werking: zolang de loodrechte projectie van het anker BINNEN het laatste
    segment valt (0 < t < 1), ligt het laatste punt voorbij het anker → weg
    ermee. Dat is dezelfde knip-op-de-projectie die knip_osm_been.py op één
    benoemde way doet, hier op de gerouteerde keten. Conservatief: valt de
    projectie buiten het segment, dan wordt er niets aangeraakt.

    ⚠️ OPT-IN PER PROFIEL (`"trimStaart": True`). De vier bestaande profielen
    blijven daarmee per constructie byte-identiek — en dat is hier geen luxe,
    want het Geofabrik-pad draait op deze machine niet meer (zie
    _ways_uit_overpass), dus een regressie op die profielen is nu niet te meten.
    Wat je niet kunt narekenen, moet je niet stilzwijgend veranderen.
    """
    weg = 0
    while len(pts) >= 2:
        a, b = pts[-2], pts[-1]
        vx, vy = b[0] - a[0], b[1] - a[1]
        nn = vx * vx + vy * vy
        if nn <= 0:
            break
        t = ((anker[0] - a[0]) * vx + (anker[1] - a[1]) * vy) / nn
        if not (0.0 < t < 1.0):
            break
        pts = pts[:-1]
        weg += 1
    return pts, weg


def _ways_uit_overpass(bb, timeout=180):
    """Het wegnet in het corridorvenster via OVERPASS in plaats van de
    Geofabrik-extract. Levert exact dezelfde way-vorm als `fl.land_laad`
    (`id`/`soort`/`ref`/`pts`), zodat álles stroomafwaarts — het eindklassen-
    filter, `corridor_keten`, de snoei, de lengtetoets — letterlijk ongewijzigd
    blijft. Geen tweede recept: alleen een tweede kraan op dezelfde leiding.

    WAAROM DIT BESTAAT. `pyosmium` kan op deze machine sinds 2026-08-06 zijn
    DLL niet meer laden — *"Dit bestand is geblokkeerd door een beleid voor
    toepassingsbeheer"* — waardoor het Geofabrik-pad hier niet draait. Dat is
    een machine-policy en geen codefout; hem omzeilen is niet aan dit script.
    Overpass was in dit project al de gedocumenteerde kruiscontrole op datzelfde
    pad, en die vergelijking is destijds hard gemaakt: hetzelfde systeem via
    beide paden gehaald kwam er COÖRDINAAT VOOR COÖRDINAAT identiek uit
    (0,000 m afwijking, M24). Daarom is dit een gelijkwaardige bron en geen
    noodgreep.

    ⚠️ HET FILTER MOET DEZELFDE ZIJN, ANDERS VERGELIJK JE TWEE DINGEN. We roepen
    `fl.weg_houden()` aan — dus inclusief de runtime-patch die de kleine
    eindklassen toelaat, en inclusief de access-uitsluiting. Overpass krijgt
    daarom bewust een ruime vraag (alle `highway`-ways in de bbox) en het
    schiften gebeurt hier, met exact de functie die het Geofabrik-pad ook
    gebruikt.
    ⚠️ GEEN CACHE. Het Geofabrik-pad hasht filter + corridorvenster in zijn
    vingerafdruk; een half-gecachte Overpass-uitslag zou die discipline stil
    ondermijnen. Elke run haalt vers op — het venster is klein genoeg.
    """
    import urllib.error
    import urllib.parse
    import urllib.request

    vraag = (f"[out:json][timeout:{timeout}];"
             f"way[\"highway\"]({bb[2]:.6f},{bb[0]:.6f},{bb[3]:.6f},{bb[1]:.6f});"
             f"out geom;")
    spiegels = ["https://overpass-api.de/api/interpreter",
                "https://overpass.kumi.systems/api/interpreter"]
    ruw = None
    for url in spiegels:
        try:
            req = urllib.request.Request(
                url, data=urllib.parse.urlencode({"data": vraag}).encode(),
                headers={"User-Agent": "grondstoffen-atlas/1.0 (stroombeen)"})
            with urllib.request.urlopen(req, timeout=timeout + 30) as r:
                ruw = json.loads(r.read().decode())
            print(f"  overpass: {url}")
            break
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            print(f"  overpass mislukt op {url}: {e}")
    if ruw is None:
        raise SystemExit("overpass: alle spiegels mislukt — geen wegnet opgehaald")

    ways, geweigerd = [], 0
    for el in ruw.get("elements", []):
        if el.get("type") != "way" or "geometry" not in el:
            continue
        tags = el.get("tags") or {}
        houd, _ = fl.weg_houden(tags)
        if not houd:
            geweigerd += 1
            continue
        pts = [[round(p["lon"], 7), round(p["lat"], 7)] for p in el["geometry"]]
        if len(pts) < 2:
            continue
        ways.append({
            "id": el["id"],
            "soort": (tags.get("highway") or "").strip(),
            "ref": (tags.get("ref") or "").strip(),
            "pts": pts,
            "regio": "overpass",
        })
    print(f"  overpass: {len(ways):,} ways gehouden, {geweigerd:,} geweigerd "
          f"door het wegfilter (zelfde weg_houden als het Geofabrik-pad)")
    if not ways:
        raise SystemExit("overpass: geen enkele way door het filter — "
                         "controleer het venster")
    return ways


def _kies_profiel(naam):
    """Zet de moduleglobals uit een profiel. Eén plek, zodat de rest van het
    bestand (en de bestaande grafiet-bake) letterlijk ongewijzigd blijft."""
    global VIA_PUNTEN, CORRIDOR, UIT, EIND_KLASSEN, CORRIDOR_KLASSEN
    p = PROFIELEN[naam]
    VIA_PUNTEN = p["via"]
    EIND_KLASSEN = tuple(p.get("eindKlassen", EIND_KLASSEN_DEFAULT))
    CORRIDOR_KLASSEN = tuple(p.get("corridorKlassen", ()))
    global EIND_TOEGANG_PRIVAAT
    EIND_TOEGANG_PRIVAAT = bool(p.get("eindToegangPrivaat", False))
    for k in CORRIDOR_KLASSEN:
        if k not in EIND_KLASSEN:
            raise SystemExit(f"profiel {naam}: corridorKlasse '{k}' staat niet in "
                             "eindKlassen — de tag-filter laat hem dan nooit door")
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
    ap.add_argument("--bron", default="geofabrik",
                    choices=("geofabrik", "overpass"),
                    help="waar het wegnet vandaan komt. 'geofabrik' (default) "
                         "scant de lokale pbf met pyosmium; 'overpass' haalt "
                         "hetzelfde venster live op en draait daarna door "
                         "exact dezelfde filters en Dijkstra. Nodig sinds "
                         "pyosmium op deze machine door een beleid voor "
                         "toepassingsbeheer geblokkeerd wordt")
    _args = ap.parse_args()
    global BRON, _PROFIEL_NAAM
    BRON = _args.bron
    _PROFIEL_NAAM = _args.profiel
    _kies_profiel(_args.profiel)
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
                           + f"@{EIND_STRAAL_KM:g}km"
                           + ("+privaat" if EIND_TOEGANG_PRIVAAT else ""))
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
        if soort in EIND_KLASSEN:
            toegang = (tags.get("access") or "").strip()
            if toegang not in fl.WEG_ACCESS_WEG:
                return True, ""
            # profiel-opt-in: privéwegen van het bedrijf zelf (eindzone)
            if EIND_TOEGANG_PRIVAAT and toegang == "private":
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
    if BRON == "overpass":
        # Zelfde venster, andere kraan — zie _ways_uit_overpass().
        ways = _ways_uit_overpass(bb)
    else:
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
    ways = [w for w in ways if w["soort"] not in EIND_KLASSEN
            or w["soort"] in CORRIDOR_KLASSEN or _bij_eind(w)]
    n_klein_mee = sum(1 for w in ways if w["soort"] in EIND_KLASSEN)
    if CORRIDOR_KLASSEN:
        print(f"  corridor-breed toegelaten (profiel): {'/'.join(CORRIDOR_KLASSEN)}")
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

    # ⚠️ TRIMMEN VÓÓR DE LENGTETOETS, om dezelfde reden als de snoei hierboven:
    # een toets die de ongesnoeide lijn meet, keurt de juiste lijn af. Dat is in
    # dit project al een keer misgegaan (lengtetoets 88,1 km terwijl de lijn
    # 82,9 was, lithium been 2).
    if PROFIELEN[_PROFIEL_NAAM].get("trimStaart"):
        keten["pts"], n_trim = _trim_staart(list(keten["pts"]), kade)
        if n_trim:
            km_voor = rap["km"]
            rap["km"] = sum(fw.km(keten["pts"][i], keten["pts"][i + 1])
                            for i in range(len(keten["pts"]) - 1))
            print(f"  staart getrimd op de ankerprojectie: {n_trim} punt(en) "
                  f"voorbij het anker weg · lengte {km_voor:,.2f} → "
                  f"{rap['km']:,.2f} km (overschiet-en-terug, zie _trim_staart)")

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
    # ⚠️ Zonder gepubliceerde km (CORRIDOR["gepubliceerdKm"] is None) is er geen
    # onafhankelijke bron om tegen te toetsen — rapporteer de eigen scanuitkomst
    # als referentie in plaats van tegen None te delen.
    if CORRIDOR["gepubliceerdKm"] is None:
        print(f"\n  lengtetoets (weggeometrie): {rap['km']:,.1f} km — geen "
              f"gepubliceerde lengte ({CORRIDOR['bronnoot']}); alleen "
              f"referentie, geen ±10%-toets")
    else:
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
                "afwijkingPct": (None if CORRIDOR["gepubliceerdKm"] is None
                                 else round(100 * afw, 1)),
                "binnenTolerantie": (None if CORRIDOR["gepubliceerdKm"] is None
                                     else bool(abs(afw) <= TOLERANTIE)),
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
