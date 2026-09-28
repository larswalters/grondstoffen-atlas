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
    # Routebrief kobalt-murrinmurrin-kwinana, been b1 (LICHTE werkwijze M31 golf 4,
    # reserve-as). Truck Murrin Murrin HPAL-plant (Glencore, Laverton Shire, WA) →
    # Leonora-spoorhoofd (railhead Kalgoorlie–Leonora-lijn), over de eigen
    # toegangsweg → Goldfields Highway. Geen gepubliceerde wegkm gevonden (brief
    # §2/§8[10]); gepubliceerdKm = de hemelsbrede afstand tussen de twee ankers
    # (56,4 km, "geen wegkm" — toets-bindend als indicatie, geen harde ±15%-norm).
    # Geen via-punten: enige toegangsweg, geen corridorkeuze gevonden.
    "kobalt-murrinmurrin-kwinana-plant-leonora": {
        "via": [
            ("Murrin Murrin HPAL-plant (Glencore/Minara Resources) (anker, co-murrinmurrin-plant)", (121.8940, -28.7680)),
            ("Leonora-spoorhoofd (railhead Kalgoorlie–Leonora-lijn) (anker, co-leonora-spoorhoofd)", (121.3308, -28.8845)),
        ],
        "id": "co-murrinmurrin-leonora-weg",
        "naam": "Murrin Murrin HPAL-plant → Leonora-spoorhoofd (eigen toegangsweg → Goldfields Highway)",
        "extracts": ["australie"],
        "refs": [],
        "gepubliceerdKm": 56.4,
        "bronnoot": "geen gepubliceerde wegkm gevonden; 56,4 km is de hemelsbrede afstand "
                    "tussen de twee ankers (routebrief §2/§8[1][10]) — 'geen wegkm', "
                    "toets-bindend als indicatie, geen harde ±15%-norm.",
        "vensterKm": 40,
        "uit": "kobalt-murrinmurrin-kwinana-weg-plant-leonora.geojson",
    },
    # Routebrief pgm-amandelbult-iselin, been b1 (LICHTE werkwijze M31 golf 4).
    # Truck Amandelbult-mijn (Anglo American Platinum / Valterra Platinum, Noord-Bushveld)
    # → Rustenburg PMR (Waterval-smelter-/RBMR-complex), via Northam op de R510
    # (Rustenburg–Northam–Thabazimbi). Geen gepubliceerde wegkm gevonden binnen het
    # webbudget (routebrief §2/§7) → gepubliceerdKm = de hemelsbrede afstand tussen de
    # twee ankers (96,6 km, toets-bindend "geen wegkm"); de scan hieronder levert de
    # echte routekm. Northam is het enige gevonden corridorpunt op de R510.
    "pgm-amandelbult-iselin-amandelbult-rustenburg": {
        "via": [
            ("Amandelbult-mijn (Anglo American Platinum / Valterra Platinum) (anker, pgm-amandelbult)", (27.2650, -24.8080)),
            ("Northam (R510-doorgangsplaats)", (27.2660, -24.9500)),
            ("Rustenburg PMR — Waterval-smelter-/RBMR-complex (anker, pgm-rustenburg-pmr)", (27.3180, -25.6750)),
        ],
        "id": "pgm-amandelbult-rustenburg-weg",
        "naam": "Amandelbult-mijn → Northam → Rustenburg PMR (R510)",
        "extracts": ["zuid-afrika"],
        "refs": ["R510"],
        "gepubliceerdKm": 96.6,
        "bronnoot": "geen gepubliceerde wegkm gevonden binnen het webbudget; 96,6 km is de "
                    "hemelsbrede afstand tussen de twee ankers (Major Mines & Projects noemt "
                    "'94 km north from Rustenburg', routebrief §2/§8[2]) — 'geen wegkm', "
                    "toets-bindend totdat deze scan een echte routekm geeft.",
        "vensterKm": 40,
        "uit": "pgm-amandelbult-iselin-weg-amandelbult-rustenburg.geojson",
    },
    # Routebrief pgm-amandelbult-iselin, been b4 (LICHTE werkwijze M31 golf 4).
    # Truck JFK South Cargo Area vrachtterminal (Queens, New York) → Metivo (voorheen BASF
    # ECMS), 33 Wood Avenue South, Iselin NJ, via NJ Turnpike/I-95. Gepubliceerd 43 mijl /
    # ~69 km (travelmath.com routeplanner) — geen officiële overheids-/bedrijfsopgave, dus
    # de bake-uitvoer is de echte controle tegen de ±15%-indicatie (routebrief §2/§7).
    "pgm-amandelbult-iselin-jfk-iselin": {
        "via": [
            ("JFK South Cargo Area vrachtterminal (anker, pgm-jfk-cargo)", (-73.7952, 40.6587)),
            ("Metivo (voorheen BASF ECMS), 33 Wood Ave South, Iselin NJ (anker, pgm-basf-ecms-iselin)", (-74.3288, 40.5650)),
        ],
        "id": "pgm-jfk-iselin-weg",
        "naam": "JFK South Cargo Area vrachtterminal → Metivo/BASF ECMS, Iselin NJ (NJ Turnpike/I-95)",
        "extracts": ["us-new-york", "us-new-jersey"],
        "refs": [],
        "gepubliceerdKm": 69,
        "bronnoot": "Travelmath.com, 'Driving Distance from JFK to Iselin, NJ' — 43 mijl / "
                    "~69 km, ~55 min (routebrief §2/§8[4]) — schatting uit een routeplanner, "
                    "geen officiële overheids-/bedrijfsopgave; de bake-uitvoer is de echte "
                    "controle tegen de ±15%-indicatie.",
        "vensterKm": 25,
        "uit": "pgm-amandelbult-iselin-weg-jfk-iselin.geojson",
    },
    # Routebrief goud-ity-ticino, been b1 (LICHTE werkwijze M31 golf 4, reserve-as).
    # Truck Ity-mijn (Endeavour Mining, West-Ivoorkust) → Abidjan (ABJ) vrachtterminal,
    # via Zouan-Hounien → Man → Daloa → Yamoussoukro (routebrief §2/§4). Geen gepubliceerde
    # wegkm gevonden binnen het webbudget; brief gebruikt hemelsbreed via-punten-som
    # (≈594 km) + ontwerp (≈600 km) puur als venster-referentie, geen harde ±15%-toets.
    # vensterKm ruim (75) want de via-punten zijn indicatieve corridorsteden, niet zelf
    # OSM-wegvertex-geverifieerd (routebrief §7).
    "goud-ity-ticino-ity-abidjan": {
        "via": [
            ("Ity-mijn, verwerkingsinstallatie (Endeavour Mining) (anker, au-ity-mijn)", (-8.1195, 6.8830)),
            ("Zouan-Hounien (departementshoofdstad, ~15 km van Ity)", (-8.2089, 6.9198)),
            ("Man (regionale corridorknoop, Tonkpi/Montagnes)", (-7.5504, 7.4103)),
            ("Daloa (corridorknoop, Haut-Sassandra)", (-6.4530, 6.8869)),
            ("Yamoussoukro (hoofdstad, corridorknoop naar Abidjan)", (-5.2776, 6.8200)),
            ("Abidjan (ABJ) vrachtterminal (anker, au-abidjan-vrachtterminal)", (-3.9298, 5.2628)),
        ],
        "id": "au-ity-abidjan-weg",
        "naam": "Ity-mijn → Zouan-Hounien → Man → Daloa → Yamoussoukro → Abidjan (ABJ) vrachtterminal",
        "extracts": ["ivoorkust"],
        "refs": [],
        "gepubliceerdKm": 600,
        "bronnoot": "geen wegkm gevonden binnen het webbudget; ontwerp ≈600 km, hemelsbreed "
                    "via-punten-som ≈594 km (routebrief §2/§7) — beide zijn een indicatie, geen "
                    "harde bron, dus de ±15%-toets geldt hier niet als norm.",
        "vensterKm": 75,
        "uit": "goud-ity-ticino-weg-ity-abidjan.geojson",
    },
    # Routebrief goud-metalor-istanbul, been b1 (LICHTE werkwijze M31 golf 4, reserve-as).
    # Truck Metalor-raffinaderij, Marin-Epagnier → Zürich Airport vrachtplatform, via
    # Biel/Bienne (A5/A6-knoop) en Bern (A6/A1-knoop) — A5 → A6/A1. Been eindigt op het
    # openbare-wegpunt vlak bij het ZRH-vrachtplatform (47.472087,8.554523), niet op het
    # platform zelf: het platform is airside/privéterrein zonder aansluiting op het
    # openbare net (zelfde patroon als goud-loulo-ticino / goud-pamp-shanghai) — de
    # bak-functie sluit af met een korte --stippel naar 47.4647,8.5492.
    "goud-metalor-istanbul-marin-zrh": {
        "via": [
            ("Metalor SA, Marin-Epagnier (anker, au-ref-metalor)", (7.0112, 47.0107)),
            ("Biel/Bienne (A5/A6-knoop)", (7.2439, 47.1402)),
            # ⚠️ Centraal verwijderd (2026-09-28): via-punt "Bern (A6/A1-knoop)" (7.4522,
            #    46.9485) ligt niet op de doorgaande route Biel → Zürich (A5 langs
            #    Solothurn → A1 bij Luterbach); het dwong een omweg van ~35 km af
            #    (been 195 km, 1,53× hemelsbreed). Zelfde klasse als Zug in golf 3.
            ("ZRH-vrachtplatform, openbare-wegpunt (anker, au-zrh-vrachtterminal, last mile)", (8.554523, 47.472087)),
        ],
        "id": "au-marin-zrh-weg",
        "naam": "Metalor Marin-Epagnier → Biel/Bienne → Solothurn → Zürich Airport vrachtplatform (A5 → A1)",
        "extracts": ["zwitserland"],
        "refs": ["A5", "A6", "A1"],
        "gepubliceerdKm": 180,
        "bronnoot": "ontwerp ≈180 km (routebrief §2); hemelsbreed 126,6 km berekend — grote afwijking is "
                    "normaal, de corridor via Bern maakt een boog.",
        "vensterKm": 40,
        "uit": "goud-metalor-istanbul-weg-marin-zrh.geojson",
    },
    # Routebrief goud-metalor-istanbul, been b3 (LICHTE werkwijze M31 golf 4, reserve-as).
    # Truck Istanbul Airport (IST) vrachtterminal → Kuyumcukent-complex, Yenibosna —
    # binnenstedelijke corridor over TEM-otoyolu/Basın Ekspress Yolu. Geen via-punten in
    # de brief (korte, ondubbelzinnige corridor); de router mag zelf 1-2 via-punten
    # toevoegen als een omweg/lus optreedt (brief §4, werkregel uit goud-loulo-ticino.md).
    "goud-metalor-istanbul-ist-kuyumcukent": {
        "via": [
            ("IST-vrachtterminal (iGA), Tayakadın (anker, au-ist-vrachtterminal)", (28.71278, 41.25528)),
            ("Kuyumcukent-goud-/sieradencomplex, Yenibosna (anker, au-kuyumcukent)", (28.8148, 41.0035)),
        ],
        "id": "au-ist-kuyumcukent-weg",
        "naam": "Istanbul Airport (IST) vrachtterminal → Kuyumcukent-complex, Yenibosna (TEM-otoyolu/Basın Ekspress Yolu)",
        "extracts": ["turkije"],
        "refs": [],
        "gepubliceerdKm": 30,
        "bronnoot": "ontwerp ≈30 km (routebrief §2); hemelsbreed 29,3 km berekend.",
        "vensterKm": 40,
        "uit": "goud-metalor-istanbul-weg-ist-kuyumcukent.geojson",
    },
    # Routebrief goud-dubai-delhi, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck DMCC-raffinagezone (Gold & Diamond Park, Al Quoz 3) → DXB-vrachtterminal
    # (Emirates SkyCargo) — Sheikh Zayed Rd → Al Rebat St/Cargo Village Rd. Gepubliceerd
    # ≈20 km (eigen meting, hemelsbreed 19,8 km); geen officiële wegbeheerder-lengte.
    "goud-dubai-delhi-dmcc-dxb": {
        "via": [
            ("DMCC-raffinagezone, Gold & Diamond Park, Al Quoz 3 (anker, au-dmcc-refine)", (55.2089, 25.1261)),
            ("Trade Centre-kruispunt (Sheikh Zayed Rd × Financial Centre Rd)", (55.2867, 25.2225)),
            ("Al Garhoud-kruising, nadering DXB", (55.3364, 25.2436)),
            ("DXB-vrachtterminal (Emirates SkyCargo) (anker, au-air-dxb)", (55.3434, 25.2560)),
        ],
        "id": "au-dmcc-dxb-weg",
        "naam": "DMCC-raffinagezone → Trade Centre-kruispunt → Al Garhoud → DXB-vrachtterminal (Sheikh Zayed Rd → Al Rebat St)",
        "extracts": ["gcc-staten"],
        "refs": [],
        "gepubliceerdKm": 20,
        "bronnoot": "≈20 km eigen meting, hemelsbreed 19,8 km (routebrief §2/§8); geen officiële "
                    "wegbeheerder-lengte gepubliceerd.",
        "vensterKm": 40,
        "uit": "goud-dubai-delhi-weg-dmcc-dxb.geojson",
    },
    # Routebrief goud-dubai-delhi, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck DEL-vrachtterminal (Delhi Air Cargo Complex) → MMTC-PAMP-raffinaderij
    # (Rojka Meo, Sohna) — NH48 (Delhi–Gurugram Expwy) → Sohna Road → Rojka Meo.
    # Gepubliceerd ≈50–55 km (eigen meting, hemelsbreed 38,3 km + corridoromweg via
    # Gurugram/Sohna); ⚠️ "Manesar" in de ketennaam ≠ de plaats Manesar (28,3553/76,9327,
    # andere corridor) — route volgt Rojka Meo/Sohna (routebrief §7).
    "goud-dubai-delhi-del-mmtc": {
        "via": [
            ("DEL-vrachtterminal, Delhi Air Cargo Complex (anker, au-air-del)", (77.1000, 28.5570)),
            ("Rajokri, NH48-kruising Delhi/Haryana-grens", (77.1111, 28.5031)),
            ("Gurugram, Sohna Road-afslag", (77.0290, 28.4560)),
            ("Sohna", (77.0700, 28.2500)),
            ("MMTC-PAMP-raffinaderij, Rojka Meo, Sohna (anker, au-ref-mmtc)", (77.0611, 28.2140)),
        ],
        "id": "au-del-mmtc-weg",
        "naam": "DEL-vrachtterminal → Rajokri → Gurugram/Sohna Road → Sohna → MMTC-PAMP Rojka Meo (NH48 → Sohna Road)",
        "extracts": ["india"],
        "refs": [],
        "gepubliceerdKm": 52,
        "bronnoot": "≈50–55 km eigen meting, hemelsbreed 38,3 km + corridoromweg via Gurugram/Sohna "
                    "(routebrief §2/§8); geen officiële bronlengte voor dit exacte traject.",
        "vensterKm": 45,
        "uit": "goud-dubai-delhi-weg-del-mmtc.geojson",
    },
    # Routebrief goud-pamp-shanghai, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck MKS PAMP-raffinaderij (Castel San Pietro, Ticino) → Zürich Airport
    # vrachtterminal (ZRH) — A2 Ticino → Gotthard → A2/A4 Zürich. Vijf via-punten
    # pinnen de doorgaande A2/A4-corridor (routebrief §4): Bellinzona (A2-knoop) →
    # Göschenen (noordportaal Gotthard, vaste doorgang) → Erstfeld (Reuss-dal) →
    # Rotkreuz (A2/A4-knoop) → Zug (A4-corridor). Gepubliceerd ~200 km (ontwerp),
    # ~198 km hemelsbreed via de punten (routebrief §2). ZRH-anker hergebruikt uit
    # pgm-springs-zurich/goud-loulo-ticino/goud-yanacocha-ticino (47.4647,8.5492).
    "goud-pamp-shanghai-pamp-zrh": {
        "via": [
            ("MKS PAMP SA, succursale Ticino — Via alle Zocche 1, Castel San Pietro (anker, au-pamp-raffinaderij)", (9.0025, 45.8546)),
            ("Bellinzona (A2-knoop) — vóór de Gotthard-klim", (9.0297, 46.1954)),
            ("Göschenen (noordportaal Gotthard) — vaste doorgang, geen alternatieve vrachtcorridor", (8.5887, 46.6676)),
            ("Erstfeld (Reuss-dal, Uri)", (8.6500, 46.8215)),
            ("Rotkreuz (A2/A4-knoop)", (8.4313, 47.1408)),
            # ⚠️ Centraal verwijderd (2026-09-28): via-punt "Zug (A4-corridor)" (8.5169,
            #    47.1681) lag in de stad; de A4 Rotkreuz → Zürich gaat door het
            #    Knonaueramt en niet door Zug. Gemeten: Rotkreuz → Zug 31,2 km voor
            #    6,5 km hemelsbreed, heel been 266,7 km (+33%).
            # ⚠️ Centraal hersteld (2026-09-28): het vrachtplatform zelf (8.5492,47.4647)
            #    ligt airside en gaf "geen wegpad tussen punt 5 en 6" — dezelfde
            #    bevinding als goud-loulo-ticino/goud-yanacocha-ticino. Het wegbeen
            #    eindigt op de openbare weg (0,91 km); de bake sluit af met een stippel.
            ("Openbare weg bij Zürich Airport vrachtplatform (last-mile-aansluiting)", (8.554523, 47.472087)),
        ],
        "id": "au-pamp-zrh-weg",
        "naam": "MKS PAMP → Bellinzona → Göschenen → Erstfeld → Rotkreuz → Zug → Zürich Airport vrachtterminal (A2 Gotthard → A4)",
        "extracts": ["zwitserland"],
        "refs": ["A2", "A4"],
        "gepubliceerdKm": 200,
        "bronnoot": "~200 km (ontwerp) · ~198 km hemelsbreed via de vijf punten (routebrief §2).",
        "vensterKm": 40,
        "uit": "goud-pamp-shanghai-weg-pamp-zrh.geojson",
    },
    # Routebrief goud-pamp-shanghai, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Shanghai Pudong (PVG) vrachtterminal → SGE-kluiszone Lujiazui (Bank of
    # Communications) — binnenstedelijk Pudong, S1/A20-type expressway-corridor.
    # Geen via-punten (routebrief §4): geen aanwijsbare corridorkeuze binnen het
    # webbudget, laat de router de kortste plausibele weg kiezen. Eindanker is een
    # ZONE (financiële wijk, geen kluispand gepubliceerd) → grotere marge acceptabel.
    "goud-pamp-shanghai-pvg-sge": {
        "via": [
            ("Shanghai Pudong International Airport vrachtplatform (PVG) (anker, au-pvg-vrachtterminal)", (121.8025, 31.1335)),
            ("Lujiazui financiële wijk / SGE-kluiszone (Bank of Communications), Yincheng-corridor (anker, au-sge-kluiszone)", (121.5008, 31.2355)),
        ],
        "id": "au-pvg-sge-weg",
        "naam": "Shanghai Pudong vrachtterminal → SGE-kluiszone Lujiazui (binnenstedelijk Pudong)",
        "extracts": ["china"],
        "refs": [],
        "gepubliceerdKm": 35,
        "bronnoot": "~35 km (ontwerp, hemelsbreed) — geen gepubliceerd getal, verwachte "
                    "uitkomst rond de 25-35 km (routebrief §2/§7).",
        "vensterKm": 30,
        "uit": "goud-pamp-shanghai-weg-pvg-sge.geojson",
    },
    # Routebrief goud-kalgoorlie-singapore, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Kalgoorlie Super Pit/Fimiston-mill (KCGM) → Perth Mint, East Perth —
    # Great Eastern Highway via Coolgardie–Southern Cross–Merredin–Cunderdin–
    # Northam–Midland (routebrief §2/§4). Gepubliceerd 590 km (Wikipedia);
    # hemelsbreed 549,8 km berekend (ratio 1,07).
    "goud-kalgoorlie-singapore-kalgoorlie-perth": {
        "via": [
            ("Kalgoorlie Super Pit / KCGM Fimiston-mill (anker, au-kalgoorlie-mill)", (121.4990, -30.7897)),
            ("Coolgardie — eerste stad op de Great Eastern Highway, corridor buigt hier af", (121.1640, -30.9530)),
            ("Southern Cross — doorgaande corridorstad, geen zijtak", (119.3278, -31.2306)),
            ("Merredin — regionale hub op de corridor", (118.2790, -31.4820)),
            ("Cunderdin — doorgaande corridorstad in de Wheatbelt", (117.2400, -31.6600)),
            ("Northam — hier voegt de Great Southern Highway aan, corridor buigt de Avon-vallei in", (116.6661, -31.6531)),
            ("Midland — rand van de Perth-agglomeratie, overgang naar stedelijke wegen", (116.0100, -31.8880)),
            ("The Perth Mint, East Perth (anker, au-ref-perth)", (115.8700, -31.9550)),
        ],
        "id": "au-kalgoorlie-perth-weg",
        "naam": "Kalgoorlie Super Pit → Coolgardie → Southern Cross → Merredin → Cunderdin → Northam → Midland → Perth Mint (Great Eastern Highway)",
        "extracts": ["australie"],
        "refs": [],
        "gepubliceerdKm": 590,
        "bronnoot": "590 km gepubliceerd (Wikipedia, Great Eastern Highway); hemelsbreed 549,8 km "
                    "berekend (ratio 1,07), routebrief §2/§8[10].",
        "vensterKm": 45,
        "uit": "goud-kalgoorlie-singapore-weg-kalgoorlie-perth.geojson",
    },
    # Routebrief goud-kalgoorlie-singapore, been b2 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Perth Mint, East Perth → Perth Airport (PER), vrachtterminal
    # (Qantas Freight Int'l Terminal, Affleck Road, Ascot) — binnenstedelijk
    # Perth, Great Eastern Highway → Tonkin Highway (routebrief §2/§4). Geen
    # via-punten nodig: <15 km, één voor de hand liggende route.
    "goud-kalgoorlie-singapore-perth-percargo": {
        "via": [
            ("The Perth Mint, East Perth (anker, au-ref-perth)", (115.8700, -31.9550)),
            ("Perth Airport (PER), Qantas Freight Int'l Terminal, Affleck Road, Ascot (anker, au-per-cargo)", (115.9764, -31.9460)),
        ],
        "id": "au-perth-percargo-weg",
        "naam": "Perth Mint, East Perth → Perth Airport (PER) vrachtterminal (Great Eastern Hwy → Tonkin Hwy)",
        "extracts": ["australie"],
        "refs": [],
        "gepubliceerdKm": 12,
        "bronnoot": "hemelsbreed 10,1 km berekend; ontwerp ≈12 km (routebrief §2/§8[1]), geen aparte "
                    "gepubliceerde wegbeheerder-lengte.",
        "vensterKm": 20,
        "eindKlassen": ["residential", "service", "tertiary", "unclassified"],
        "eindToegangPrivaat": True,
        "uit": "goud-kalgoorlie-singapore-weg-perth-percargo.geojson",
    },
    # Routebrief goud-argor-mumbai, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck Argor-Heraeus SA, Mendrisio (Ticino) → Milaan-Malpensa (MXP)
    # vrachtterminal — A2 (CH) → grens Chiasso → A9/A8 (IT) (routebrief §2/§4).
    # gepubliceerdKm 70 is een ontwerp-schatting (geen officiële wegbeheerder-
    # bron, grensoverschrijdend CH→IT); via-puntensom hemelsbreed 64,1 km ligt
    # daar logisch onder.
    "goud-argor-mumbai-argor-mxp": {
        "via": [
            ("Argor-Heraeus SA, Mendrisio (Ticino) (anker, au-ref-argor)", (8.9818, 45.8749)),
            ("Chiasso — grenspost CH/IT", (9.0333, 45.8333)),
            ("San Fermo della Battaglia (Como-tunnels A9)", (9.0486, 45.8084)),
            ("Fino Mornasco", (9.0476, 45.7429)),
            ("Lainate — A9/A8-knooppunt", (9.0317, 45.5632)),
            ("Busto Arsizio (A8)", (8.8518, 45.6119)),
            ("Cardano al Campo (A8-afslag Malpensa)", (8.7725, 45.6457)),
            ("Milano Malpensa Cargo, Cargo City Sud (MXP) (anker, au-air-mxp)", (8.7186, 45.6142)),
        ],
        "id": "au-argor-mxp-weg",
        "naam": "Argor-Heraeus Mendrisio → A2 → Chiasso → A9 → A8 → Malpensa-vrachtterminal",
        "extracts": ["zwitserland", "italie"],
        "refs": ["A2", "A9", "A8"],
        "gepubliceerdKm": 70,
        "bronnoot": "geen officiële wegbeheerder-lengte gevonden (grensoverschrijdend CH→IT); "
                    "70 km is een ontwerp-schatting, via-puntensom hemelsbreed 64,1 km (brief §2).",
        "vensterKm": 45,
        "uit": "goud-argor-mumbai-weg-argor-mxp.geojson",
    },
    # Routebrief goud-argor-mumbai, been b3 (LICHTE werkwijze M31 golf 3).
    # Truck Mumbai (BOM) vrachtterminal → Zaveri Bazaar-sieradenmarkt —
    # Western Express Highway → S.V. Road → Dr. Annie Besant Road (§2/§4).
    # Zaveri Bazaar ligt in nauwe marktstraten van Kalbadevi; kleine
    # wegklassen binnen 12 km toegelaten, laatste meters evt. korte stippel.
    # ⚠️ Het anker au-air-bom (72.8660,19.0954) snapt op een geïsoleerd
    # airside-wegcomponent (BFS op de india-scan: componentgrootte 9 tegen
    # 178.739 op het publieke net) — geen COMPONENT-toegang, dus
    # eindToegangPrivaat lost dit niet op. Eerste via-punt is daarom het
    # dichtstbijzijnde routeerpunt op het publieke net (72.865345,19.096391,
    # 0,13 km van het anker); de bake tekent anker → routeerpunt als korte
    # stippel (bakhandleiding §2 Lucht: "korter dan ~2 km").
    "goud-argor-mumbai-bom-zaveri": {
        "via": [
            ("Openbare-wegaansluiting bij BOM-vrachtterminal (routeerpunt; anker au-air-bom ligt 0,13 km verderop op het airside-net)", (72.865345, 19.096391)),
            ("Vile Parle (Western Express Highway)", (72.8440, 19.0999)),
            ("Bandra West", (72.8303, 19.0583)),
            ("Mahim", (72.8398, 19.0423)),
            ("Worli (Dr. Annie Besant Road)", (72.8157, 19.0308)),
            ("Crawford Market", (72.8345, 18.9473)),
            ("Zaveri Bazaar-sieradenmarkt, Mumbai (anker, au-mkt-zaveri)", (72.8307, 18.9518)),
        ],
        "id": "au-bom-zaveri-weg",
        "naam": "BOM-vrachtterminal → Western Express Highway → S.V. Road → Dr. Annie Besant Road → Zaveri Bazaar",
        "extracts": ["india"],
        "refs": [],
        "gepubliceerdKm": 25,
        "bronnoot": "geen officiële wegbeheerder-lengte gevonden; 25 km is een ontwerp-schatting, "
                    "via-puntensom hemelsbreed 22,2 km (brief §2).",
        "vensterKm": 20,
        "eindKlassen": ["residential", "service", "tertiary", "unclassified"],
        "trimStaart": True,
        "uit": "goud-argor-mumbai-weg-bom-zaveri.geojson",
    },
    # Routebrief goud-malartic-ottawa, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck Canadian Malartic-mijn (Agnico Eagle, Québec) → Royal Canadian Mint
    # Ottawa — Route 117 → Route 105 → Autoroute 5 (routebrief §2/§4/§7).
    # ⚠️ Geen gepubliceerde route-km (brief §7): ontwerp-schatting ≈480 km tegen
    # een via-puntensom hemelsbreed van 398,0 km (+21% bochtopslag, plausibel
    # voor het ~250 km rechte La Vérendrye-reservaat-stuk + twee regionale
    # wegen). vensterKm ruim (60) i.v.m. het lange rechte reservaat-traject.
    "goud-malartic-ottawa-malartic-ottawa": {
        "via": [
            ("Canadian Malartic-mijn (Agnico Eagle), Malartic, Québec (anker, au-malartic-mijn)", (-78.0942, 48.1176)),
            ("Route 117 bij Louvicourt (oostzijde Val-d'Or)", (-77.3779, 48.0657)),
            ("Route 117 door de Réserve faunique La Vérendrye", (-77.1100, 47.3300)),
            ("Grand-Remous — knooppunt Route 117 / Route 105", (-75.9158, 46.6192)),
            ("Route 105 bij Kazabazua", (-76.0226, 45.9074)),
            ("Route 105 bij Low", (-75.9526, 45.8117)),
            ("Wakefield — noordelijk eindpunt Autoroute 5 / aansluiting Route 105", (-75.9293, 45.6400)),
            ("Macdonald-Cartier Bridge (grens Québec/Ontario)", (-75.7030, 45.4370)),
            ("Royal Canadian Mint, 320 Sussex Drive, Ottawa (anker, au-rcm-ottawa)", (-75.6993, 45.4315)),
        ],
        "id": "au-malartic-ottawa-weg",
        "naam": "Canadian Malartic-mijn → Route 117 → Route 105 → Autoroute 5 → Royal Canadian Mint Ottawa",
        "extracts": ["canada"],
        "refs": ["117", "105", "5"],
        "gepubliceerdKm": 480,
        "bronnoot": "geen gepubliceerde route-km gevonden voor Malartic→Ottawa over de weg; "
                    "480 km is een ontwerp-schatting, via-puntensom hemelsbreed 398,0 km "
                    "(+21% bochtopslag) — de lengtetoets (±15%) staat dus tegen een schatting, "
                    "niet een harde bron (brief §7).",
        "vensterKm": 60,
        "uit": "goud-malartic-ottawa-weg-malartic-ottawa.geojson",
    },
    # Routebrief goud-siguiri-dubai, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Siguiri-mijn (AngloGold Ashanti/SMD, Kintinian) → Conakry Int'l (CKY)
    # vrachtterminal — N1-corridor via Kouroussa–Dabola–Mamou–Kindia–Coyah
    # (routebrief §2/§4/§7). Lange corridor (~850 km ontwerp, som via-punten
    # hemelsbreed ≈557 km — typisch 30-50% korter dan de wegafstand) → venster ruim.
    "goud-siguiri-dubai-siguiri-cky": {
        "via": [
            ("Siguiri-mijn — AngloGold Ashanti/SMD, Kintinian, Boure-gebied (anker, au-siguiri-mijn)", (-9.3567, 11.5695)),
            ("Kouroussa — eerste stadsknoop op de N1", (-9.8810, 10.6514)),
            ("Dabola — tussenstad op de N1, enige doorgaande route naar Mamou", (-11.1065, 10.7422)),
            ("Mamou — knooppuntstad waar de N1 richting kust ombuigt", (-12.0836, 10.3741)),
            ("Kindia — laatste grote tussenstad vóór de kustregio", (-12.8260, 10.0368)),
            ("Coyah — laatste knoop vóór de Conakry-stadsrand/luchthavenweg", (-13.3890, 9.7090)),
            ("Conakry Int'l (CKY), vracht-/GA-apron (anker, au-cky-cargo)", (-13.6205, 9.5748)),
        ],
        "id": "au-siguiri-cky-weg",
        "naam": "Siguiri-mijn → Kouroussa → Dabola → Mamou → Kindia → Coyah → Conakry Int'l (CKY) (N1)",
        "extracts": ["guinee"],
        "refs": ["N1"],
        "gepubliceerdKm": 850,
        "bronnoot": "~850 km ontwerp (routebrief §2/§7) — geen gepubliceerde wegkilometrage voor de "
                    "N1 Siguiri–Conakry-corridor gevonden binnen het webbudget; som via-punten "
                    "hemelsbreed ≈557 km, niet onafhankelijk bevestigd.",
        "vensterKm": 60,
        "uit": "goud-siguiri-dubai-weg-siguiri-cky.geojson",
    },
    # Routebrief goud-siguiri-dubai, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Dubai Intl (DXB) vrachtterminal → DMCC-raffinagezone (Emirates Gold/
    # Kaloti, Almas Tower) — Sheikh Zayed Road (E11), enige doorgaande corridor
    # (routebrief §2/§4/§7). Zelfde fysieke corridor als diamant-marange-dubai
    # (DXB-cargo → DMCC/Almas Tower) — die geometrie is letterlijk hergebruikt
    # (zie bak_stromen.sh, geen tweede scan). Dit profiel staat voor de volledigheid.
    "goud-siguiri-dubai-dxb-dmcc": {
        "via": [
            ("Dubai Intl (DXB), Emirates Air Cargo-gebouw, Al Garhoud (anker, au-dxb-cargo)", (55.3406, 25.2575)),
            ("Dubai World Trade Centre-interchange — enige doorgaande snelweg (E11) tussen DXB en JLT", (55.2888, 25.2276)),
            ("Mall of the Emirates-interchange — tweede vaste interchange, vlak vóór JLT/DMCC", (55.2006, 25.1181)),
            ("DMCC, Almas Tower, Jumeirah Lake Towers (anker, au-dubai-dmcc)", (55.1412, 25.0691)),
        ],
        "id": "au-dxb-dmcc-weg",
        "naam": "Dubai Intl (DXB) vrachtterminal → DMCC/Almas Tower (Sheikh Zayed Road E11)",
        "extracts": ["gcc-staten"],
        "refs": ["E11"],
        "gepubliceerdKm": 20,
        "bronnoot": "~20 km ontwerp (routebrief §2/§7); anker-tot-anker hemelsbreed ≈29 km — ligt onder "
                    "de gemeten wegroute, verwacht bij de lengtetoets een afwijking ruim boven +15% "
                    "(bevinding, geen bijschuiven). Zelfde E11-corridor als diamant-marange-dubai, "
                    "waar dit been al eerder gebakken werd (geometrie hergebruikt, zie bak_stromen.sh).",
        "vensterKm": 20,
        "uit": "goud-siguiri-dubai-weg-dxb-dmcc.geojson",
    },
    # Routebrief goud-mponeng-londen, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Mponeng-mijn (Harmony Gold) → Rand Refinery Germiston — N12/R28-
    # industriecorridor Witwatersrand via Westonaria → Soweto (routebrief §2/§4/§7).
    # Geen harde gepubliceerde km; eigen berekening ≈77 km (rechte afstand
    # 76,2 km), corridor N12 vs R28 niet bevonden → venster ruim.
    "goud-mponeng-londen-mponeng-randrefinery": {
        "via": [
            ("Mponeng-mijn — schacht + oppervlaktecomplex (anker, au-mponeng-mijn)", (27.4306, -26.4361)),
            ("Westonaria — West-Rand-mijngordel, pint de N12/R28-corridor", (27.6506, -26.3178)),
            ("Soweto — op de rechte lijn Westonaria→Germiston, pint de N12-route", (27.8585, -26.2678)),
            ("Rand Refinery, Germiston (anker, au-randrefinery)", (28.1550, -26.2189)),
        ],
        "id": "au-mponeng-randrefinery-weg",
        "naam": "Mponeng-mijn → Westonaria → Soweto → Rand Refinery, Germiston (N12/R28)",
        "extracts": ["zuid-afrika"],
        "refs": ["N12", "R28"],
        "gepubliceerdKm": 77,
        "bronnoot": "≈77 km eigen berekening (routebrief §2/§7; rechte afstand 76,2 km) — "
                    "geen gepubliceerde bron; corridor N12 vs R28 niet bevonden, ±15%-toets soepel.",
        "vensterKm": 45,
        "uit": "goud-mponeng-londen-weg-mponeng-randrefinery.geojson",
    },
    # Routebrief goud-mponeng-londen, been b2 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Rand Refinery Germiston → OR Tambo (JNB) vrachtterminal — R21/N12,
    # korte stadsleg (routebrief §2/§4). Geen via-punten nodig. Gepubliceerd
    # ≈15 km (redactionele schatting ontwerp, niet hard); rechte afstand 11,2 km.
    # ⚠️ Eerste poging (geen eindToegangPrivaat) faalde op "geen wegpad" — het
    # JNB-vrachtapron is airside/deels privéterrein (zoals dia-jnb-cargo elders
    # in dit bestand, 28.227/-26.143, hetzelfde patroon); eindToegangPrivaat +
    # bredere eindKlassen erbij.
    "goud-mponeng-londen-randrefinery-jnb": {
        "via": [
            ("Rand Refinery, Germiston (anker, au-randrefinery)", (28.1550, -26.2189)),
            ("OR Tambo (JNB) vrachtterminal (anker, au-jnb-vracht)", (28.2295, -26.1440)),
        ],
        "id": "au-randrefinery-jnb-weg",
        "naam": "Rand Refinery, Germiston → OR Tambo (JNB) vrachtterminal (R21/N12)",
        "extracts": ["zuid-afrika"],
        "refs": ["R21", "N12"],
        "gepubliceerdKm": 15,
        "bronnoot": "≈15 km redactionele schatting uit het ontwerp (routebrief §2/§7), geen aparte "
                    "bron; rechte afstand 11,2 km.",
        "vensterKm": 25,
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "eindToegangPrivaat": True,
        "uit": "goud-mponeng-londen-weg-randrefinery-jnb.geojson",
    },
    # Routebrief goud-mponeng-londen, been b4 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Heathrow-vrachtterminal → LBMA-kluis City of London — M4/A4 via
    # Hounslow → Chiswick → Hammersmith (routebrief §2/§4). Gepubliceerd ≈27 km
    # (eigen berekening; ontwerp noemde ≈25 km via M4). Stedelijk eindstuk:
    # standaard-eindklassen eerst proberen, verruimen als de City-straten niet
    # gevonden worden.
    "goud-mponeng-londen-lhr-lbma": {
        "via": [
            ("Heathrow-vrachtterminal (anker, au-lhr-vracht)", (-0.4680, 51.4605)),
            ("Hounslow — eerste grote plaats op de M4/A4-corridor", (-0.3750, 51.4668)),
            ("Chiswick — A4 vóór de overgang naar centraal Londen", (-0.2600, 51.4900)),
            ("Hammersmith — bekend knooppunt (Hammersmith flyover) op de A4", (-0.2228, 51.4933)),
            ("LBMA-kluis, City of London (anker, au-lbma-kluis)", (-0.0880, 51.5140)),
        ],
        "id": "au-lhr-lbma-weg",
        "naam": "Heathrow-vrachtterminal → Hounslow → Chiswick → Hammersmith → LBMA-kluis City of London (M4/A4)",
        "extracts": ["groot-brittannie"],
        "refs": ["M4", "A4"],
        "gepubliceerdKm": 27,
        "bronnoot": "≈27 km eigen berekening (routebrief §2/§7; ontwerp noemde ≈25 km via M4) — "
                    "vrijwel gelijk aan de rechte afstand (27,0 km).",
        "vensterKm": 25,
        "uit": "goud-mponeng-londen-weg-lhr-lbma.geojson",
    },
    # Routebrief goud-tarkwa-dubai, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Gold Fields Tarkwa — CIL-verwerkingsfabriek (mijn/mill, anker
    # au-tarkwa-mill) → Kotoka/Accra Intl vrachtterminal (anker au-air-acc-
    # cargo) — inland-corridor via Twifo Praso → Assin Fosu → Agona Swedru →
    # Kasoa → Accra (routebrief §2/§4/§7). N-wegnummer niet onafhankelijk
    # gebrond; via-punten op geografische aannemelijkheid + OSM/Photon-
    # coördinaten. Gepubliceerd ≈300 km (Gold Fields: "approximately 300
    # kilometres by road" naar Tema/Accra); ruim venster want lange landelijke
    # corridor. Geen refs (geen N-wegnummer gebrond).
    "goud-tarkwa-dubai-mill-acc": {
        "via": [
            ("Gold Fields Tarkwa — CIL-verwerkingsfabriek (anker, au-tarkwa-mill)", (-2.0215, 5.3275)),
            ("Twifo Praso — pint de inland-route naar Kasoa/Accra i.p.v. de kustomweg", (-1.5497, 5.6116)),
            ("Assin Fosu — doorgaande knoop op dezelfde inland-corridor", (-1.2769, 5.7005)),
            ("Agona Swedru — corridor buigt hier zuidoostwaarts naar Kasoa", (-0.7008, 5.5345)),
            ("Kasoa — laatste grote knoop vóór Accra/Kotoka", (-0.4375, 5.5326)),
            ("Kotoka/Accra Intl vrachtterminal (anker, au-air-acc-cargo)", (-0.1745, 5.5985)),
        ],
        "id": "au-tarkwa-acc-weg",
        "naam": "Gold Fields Tarkwa (mill) → Twifo Praso → Assin Fosu → Agona Swedru → Kasoa → Kotoka/Accra Intl vrachtterminal (inland-route)",
        "extracts": ["ghana"],
        "refs": [],
        "gepubliceerdKm": 300,
        "bronnoot": "Gold Fields: ~300 km naar Tema/Accra; via-punten niet individueel "
                    "gebrond, zie routebrief §7.",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "goud-tarkwa-dubai-weg-mill-acc.geojson",
    },
    # Routebrief goud-tarkwa-dubai, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Dubai Intl vrachtterminal (Emirates SkyCargo, anker au-air-dxb-
    # cargo) → DMCC-goudzone/Al Etihad Gold Refinery (anker au-dmcc-refine) —
    # Sheikh Zayed Road (E11) via Trade Centre Roundabout (kn. 1) → Mall of
    # the Emirates-knoop (kn. 4) → Interchange bij Al Thanyah/JLT (routebrief
    # §2/§4). Gepubliceerd ≈31 km (eigen meting via de drie via-punten, ná
    # satellietcheck van beide ankers).
    "goud-tarkwa-dubai-dxb-dmcc": {
        "via": [
            ("Dubai Intl vrachtterminal (Emirates SkyCargo, anker, au-air-dxb-cargo)", (55.3431, 25.2560)),
            ("Trade Centre Roundabout (Interchange 1, Sheikh Zayed Rd)", (55.2909, 25.2294)),
            ("Mall of the Emirates-knoop (Interchange 4)", (55.1997, 25.1202)),
            ("Interchange bij Al Thanyah/JLT (nabij DMCC)", (55.1410, 25.0680)),
            ("DMCC-goudzone, Dubai — Al Etihad Gold Refinery (anker, au-dmcc-refine)", (55.1352, 25.0602)),
        ],
        "id": "au-dxb-dmcc-weg",
        "naam": "Dubai Intl vrachtterminal (DXB) → Trade Centre Roundabout → Mall of the Emirates → Al Thanyah/JLT → DMCC-goudzone (Sheikh Zayed Road)",
        "extracts": ["gcc-staten"],
        "refs": ["Sheikh Zayed Road", "E11"],
        "gepubliceerdKm": 31,
        "bronnoot": "Eigen meting via de drie via-punten, ná satellietcheck van beide "
                    "ankers (routebrief §2/§7); ontwerp noemde ≈20 km, hier gecorrigeerd.",
        "vensterKm": 30,
        "eindKlassen": ["residential", "service", "tertiary", "unclassified"],
        "uit": "goud-tarkwa-dubai-weg-dxb-dmcc.geojson",
    },
    # Routebrief goud-valcambi-londen, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Valcambi-raffinaderij (Balerna, Ticino) → Milaan-Malpensa
    # Cargo City Sud-vrachtterminal — A2 (Chiasso-grensovergang) → A9
    # (Como–Lomazzo) → A8 (Gallarate) → laatste stuk naar Malpensa (routebrief
    # §2/§4). Gepubliceerd ≈78 km (eigen kaartlezing, ontwerp-indicatie ≈75 km,
    # geen aparte gepubliceerde bron) — de bake-lengte is de echte controle.
    "goud-valcambi-londen-valcambi-mxp": {
        "via": [
            ("Valcambi SA, Balerna (anker, au-ref-valcambi)", (9.0051, 45.8385)),
            ("Chiasso — grensovergang CH–IT (A2)", (9.0333, 45.8333)),
            ("Como — A9 langs het Comomeer", (9.0833, 45.8167)),
            ("Lomazzo — A9/A8-knooppunt, tak naar Malpensa", (9.0333, 45.7000)),
            ("Gallarate — A8, laatste plaats vóór de afslag naar Malpensa", (8.7932, 45.6599)),
            ("Milano Malpensa Cargo, Cargo City Sud (anker, au-mxp-cargo)", (8.7186, 45.6142)),
        ],
        "id": "au-valcambi-mxp-weg",
        "naam": "Valcambi, Balerna → Chiasso → Como → Lomazzo → Gallarate → Malpensa Cargo City Sud (A2/A9/A8)",
        "extracts": ["zwitserland", "italie"],
        "refs": ["A2", "A9", "A8", "SS336"],
        "gepubliceerdKm": 78,
        "bronnoot": "≈78 km eigen kaartlezing (routebrief §2/§7, ontwerp-indicatie ≈75 km) — "
                    "geen aparte gepubliceerde bronwaarde.",
        "vensterKm": 50,
        "uit": "goud-valcambi-londen-weg-valcambi-mxp.geojson",
    },
    # Routebrief goud-valcambi-londen, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Heathrow World Cargo Centre-vrachtterminal → LBMA-kluis / Bank of
    # England, City of London — M4 (Heathrow-spur) → A4 (Chiswick,
    # Hammersmith) → Hyde Park Corner → Fleet Street (routebrief §2/§4).
    # Gepubliceerd ≈25 km (eigen kaartlezing, geen aparte gepubliceerde bron).
    # Stedelijke eindnadering: rond de Bank of England ligt een voetgangerszone
    # (routebrief §7) — het laatste stukje kan een korte last-mile-stippel
    # vragen, ter beoordeling ná de bake.
    "goud-valcambi-londen-lhr-boe": {
        "via": [
            ("Heathrow World Cargo Centre / IAG Cargo (anker, au-lhr-cargo)", (-0.4629, 51.4605)),
            ("M4 J4/J4b — Heathrow-spur naar het Londense hoofdnet", (-0.4595, 51.4870)),
            ("Chiswick Roundabout — overgang M4 → A4", (-0.2814, 51.4911)),
            ("Hammersmith Flyover — doorgaande A4-tak", (-0.2240, 51.4912)),
            ("Hyde Park Corner — corridor buigt naar de City", (-0.1543, 51.5027)),
            ("Fleet Street — laatste doorgaande straat vóór de City", (-0.1119, 51.5137)),
            ("Bank of England, Threadneedle Street (anker, au-hub-london)", (-0.0883, 51.5139)),
        ],
        "id": "au-lhr-boe-weg",
        "naam": "Heathrow World Cargo Centre → M4 → Chiswick → Hammersmith → Hyde Park Corner → Fleet Street → Bank of England",
        "extracts": ["groot-brittannie"],
        "refs": ["M4", "A4"],
        "gepubliceerdKm": 25,
        "bronnoot": "≈25 km eigen kaartlezing (routebrief §2/§7) — geen aparte gepubliceerde bronwaarde.",
        "vensterKm": 40,
        "eindKlassen": ["tertiary", "unclassified", "residential", "service"],
        "uit": "goud-valcambi-londen-weg-lhr-boe.geojson",
    },
    # Routebrief goud-olimpiada-dubai, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Olimpiada-mijn (Polyus, Severo-Jenisejsk-district) → Krastsvetmet-
    # raffinaderij, Krasnojarsk — regionale weg eerst noordwaarts naar de
    # districtshoofdplaats Severo-Jenisejsk (vóór het doorgaande wegennet
    # zuidwaarts begint), dan zuidwaarts via Jenisejsk/Lesosibirsk (Jenisej-
    # oversteek, begin van de P409) → Bolsjaja Moerta → Krasnojarsk (routebrief
    # §2/§4). Gepubliceerd ≈550 km (ontwerpcijfer, niet apart gebrond — de
    # bake-lengte is de echte controle). Langste/onzekerste been van de keten
    # (routebrief §7): aannemelijke corridor uit nederzettingsgeografie, geen
    # gepubliceerde routebeschrijving; dunbevolkt taigagebied rond
    # Severo-Jenisejsk kan OSM-gaten hebben.
    "goud-olimpiada-dubai-olimpiada-krastsvetmet": {
        "via": [
            ("Olimpiada-mijn (Polyus), open dagbouwput (anker, au-olimpiada-mijn)", (92.9156, 59.8650)),
            ("Severo-Jenisejsk — districtshoofdplaats, mijnweg buigt hier eerst noordwaarts", (93.0330, 60.3747)),
            ("Jenisejsk / Lesosibirsk — Jenisej-oversteek, begin doorgaande P409 zuidwaarts", (92.1333, 58.4667)),
            ("Bolsjaja Moerta — vaste tussenstop op de P409-corridor", (93.1393, 56.9093)),
            ("Krastsvetmet OJSC, Krasnojarsk (anker, au-krastsvetmet)", (92.9998, 56.0160)),
        ],
        "id": "au-olimpiada-krastsvetmet-weg",
        "naam": "Olimpiada-mijn → Severo-Jenisejsk → Jenisejsk/Lesosibirsk → Bolsjaja Moerta → Krastsvetmet, Krasnojarsk (P409)",
        "extracts": ["rusland-siberie"],
        "refs": ["P409"],
        "gepubliceerdKm": 550,
        "bronnoot": "≈550 km (ontwerpcijfer, routebrief §2/§7) — geen gepubliceerde "
                    "routebeschrijving, aannemelijke corridor uit nederzettingsgeografie.",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "goud-olimpiada-dubai-weg-olimpiada-krastsvetmet.geojson",
    },
    # Routebrief goud-olimpiada-dubai, been b2 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Krastsvetmet-raffinaderij, Krasnojarsk → Jemeljanovo (KJA)
    # vrachtterminal — stadsrand Krasnojarsk, P409/ringweg noordwaarts naar het
    # vliegveld (routebrief §2/§4). Korte stadsrand-corridor, geen aparte
    # via-punten nodig. Gepubliceerd ≈30 km (ontwerpcijfer).
    "goud-olimpiada-dubai-krastsvetmet-kja": {
        "via": [
            ("Krastsvetmet OJSC, Krasnojarsk (anker, au-krastsvetmet)", (92.9998, 56.0160)),
            ("Jemeljanovo (KJA) vrachtterminal (anker, au-kja-cargo)", (92.4630, 56.1837)),
        ],
        "id": "au-krastsvetmet-kja-weg",
        "naam": "Krastsvetmet, Krasnojarsk → Jemeljanovo (KJA) vrachtterminal (P409/ringweg noordwaarts)",
        "extracts": ["rusland-siberie"],
        "refs": ["P409"],
        "gepubliceerdKm": 30,
        "bronnoot": "≈30 km (ontwerpcijfer, routebrief §2/§7).",
        "vensterKm": 40,
        "corridorKlassen": ["tertiary", "unclassified", "residential", "service"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "eindToegangPrivaat": True,
        "uit": "goud-olimpiada-dubai-weg-krastsvetmet-kja.geojson",
    },
    # Routebrief goud-olimpiada-dubai, been b4 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Dubai International Airport (DXB) — Emirates SkyCargo-vrachtterminal
    # → DMCC-vrijzone, Jumeirah Lake Towers — Sheikh Zayed Road via de Trade
    # Centre-rotonde → Mall of the Emirates/Interchange 4 (routebrief §2/§4).
    # Grote, goed gekarteerde snelweg-corridor, geen stippel verwacht.
    # Gepubliceerd ≈20 km (ontwerpcijfer).
    "goud-olimpiada-dubai-dxb-dmcc": {
        "via": [
            ("Dubai International Airport (DXB) — Emirates SkyCargo (anker, au-dxb-cargo)", (55.3434, 25.2560)),
            ("Trade Centre-rotonde — begin doorgaande Sheikh Zayed Road-corridor", (55.2888, 25.2276)),
            ("Mall of the Emirates (Interchange 4) — laatste keuzepunt vóór JLT/DMCC", (55.2004, 25.1180)),
            ("DMCC (Dubai Multi Commodities Centre), Jumeirah Lake Towers (anker, au-dmcc)", (55.1387, 25.0709)),
        ],
        "id": "au-dxb-dmcc-weg",
        "naam": "Dubai International Airport (DXB, Emirates SkyCargo) → Trade Centre → Mall of the Emirates → DMCC-vrijzone (Sheikh Zayed Road)",
        "extracts": ["gcc-staten"],
        "refs": ["Sheikh Zayed Road", "E11"],
        "gepubliceerdKm": 20,
        "bronnoot": "≈20 km (ontwerpcijfer, routebrief §2/§7).",
        "vensterKm": 40,
        "trimStaart": True,
        "uit": "goud-olimpiada-dubai-weg-dxb-dmcc.geojson",
    },
    # Routebrief goud-nevada-saltlakecity, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck Goldstrike-complex (Nevada Gold Mines, Carlin Trend, Barrick 61,5%/Newmont
    # 38,5%) → Asahi Refining USA, Salt Lake City — I-80 via de eigen mijnweg NV-766
    # (Goldstrike → Carlin) → Elko → Wells → West Wendover → Knolls → Lake Point.
    # Bewust GEEN luchtvracht (routebrief §1/§7): één doorgaand truckbeen. Gepubliceerd
    # ≈450 km (brief meet dit uit gepubliceerde deeltrajecten; ontwerp noemde ≈550 km,
    # zie brief §7 — de bake-lengte is leidend, norm ±15%). corridorKlassen niet gezet:
    # I-80 en NV-766 zijn beide doorgaande, publiek gekarteerde wegen; bij "geen wegpad"
    # eerst checken of NV-766 als tertiary/unclassified in het us-nevada-extract zit.
    "goud-nevada-saltlakecity-nevada-saltlakecity": {
        "via": [
            ("Goldstrike-complex, Betze-Post open pit + autoclaaf-/roaster (Nevada Gold Mines, anker au-nevada-mijn)", (-116.3789, 40.9816)),
            ("Carlin, NV — mijnweg NV-766/Boone Springs Road sluit hier aan op I-80", (-116.1071, 40.7131)),
            ("Elko, NV — I-80/US-93-knooppunt", (-115.74028, 40.83889)),
            ("Wells, NV — I-80/US-93-splitsing", (-114.96722, 41.12)),
            ("West Wendover, NV — staatsgrens Nevada/Utah op I-80", (-114.07517, 40.74097)),
            ("Knolls, UT — I-80-afrit rand Bonneville Salt Flats", (-113.28971, 40.72299)),
            ("Lake Point, UT — I-80 langs zuidoever Great Salt Lake (op de doorgaande I-80-lijn, niet het dorp)", (-112.2617, 40.6957)),
            ("South Frontage Road vóór Asahi Refining (routeerpunt — het anker au-saltlakecity-asahi/laaddock ligt ~100 m verder op een OSM-geïsoleerde parkeerlus, niet aangesloten op het net)", (-112.000339, 40.725566)),
        ],
        "id": "au-nevada-saltlakecity-weg",
        "naam": "Goldstrike-complex → Carlin → Elko → Wells → West Wendover → Knolls → Lake Point → South Frontage Road (Asahi Refining SLC, I-80/NV-766)",
        "extracts": ["us-nevada", "us-utah"],
        "refs": ["I-80", "NV-766"],
        "gepubliceerdKm": 450,
        "bronnoot": "≈450 km (routebrief-eigen optelling: Elko→Salt Lake City 370 km via "
                    "I-80 [DistanceCalc] + Carlin→Elko ≈39 km + mijnweg Goldstrike→Carlin "
                    "≈30 km over NV-766); ontwerp noemde ≈550 km, zie brief §7 — de bake "
                    "geldt als leidend. ⚠️ Diagnose (weggraaf, 2026-09-28): het "
                    "au-saltlakecity-asahi-anker (laaddock/parkeerlus, 40.72471,-112.00077) "
                    "snapt op een OSM-component van slechts 8 knopen (twee losse "
                    "'service'-ways, way 742154031/742154032) die niet aan het publieke net "
                    "hangt — een echte topologiebreuk, geen te ruim venster. Dichtstbijzijnde "
                    "knoop op het hoofdnet: South Frontage Road, 102 m verderop "
                    "(40.725566,-112.000339). Wegbeen eindigt daar; de laatste ~100 m gaat als "
                    "korte stippel in de bake (bakhandleiding §2, <2 km).",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "goud-nevada-saltlakecity-weg-nevada-saltlakecity.geojson",
    },
    # Routebrief goud-loulo-ticino, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Loulo-Gounkoto-mijncomplex (Barrick, West-Mali) → Bamako-Sénou
    # vrachtterminal (BKO) — mijnweg → Kéniéba (RN-verbindingsweg) → Kita
    # (corridorknoop, buigt oostwaarts naar Bamako) → Bamako (routebrief §2/§4).
    # Gepubliceerd ≈380 km (ontwerp); hemelsbreed 380,5 km (berekend).
    # eindToegangPrivaat: het BKO-terreincluster is airside/deels militair
    # terrein (routebrief §7) — korte eindstukjes evt. stippel bij het bakken.
    "goud-loulo-ticino-loulo-bamako": {
        "via": [
            ("Loulo-Gounkoto-mijncomplex (anker, au-loulo-mijn)", (-11.4118, 13.0868)),
            ("Kéniéba — RN-verbindingsweg (Dakar-Bamako-corridor)", (-11.232153, 12.8407105)),
            ("Kita — corridorknoop, buigt oostwaarts naar Bamako", (-9.4889798, 13.0408383)),
            ("Bamako-Sénou vrachtterminal, BKO (anker, au-bamako-vrachtterminal)", (-7.9488, 12.5353)),
        ],
        "id": "au-loulo-bamako-weg",
        "naam": "Loulo-Gounkoto-mijncomplex → Bamako-Sénou vrachtterminal (BKO) (Kéniéba–Kita–Bamako-corridor)",
        "extracts": ["mali"],
        "refs": [],
        "gepubliceerdKm": 380,
        "bronnoot": "≈380 km (ontwerp); eigen hemelsbreed berekend 380,5 km (routebrief §2).",
        "vensterKm": 40,
        "eindToegangPrivaat": True,
        "uit": "goud-loulo-ticino-weg-loulo-bamako.geojson",
    },
    # Routebrief goud-loulo-ticino, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Zürich Airport vrachtplatform (ZRH) → Valcambi-raffinaderij, Balerna
    # (Ticino) — A4 (Zürich-Zug-Luzern, verplichte aansluiting op de A2-as) →
    # A2/Gotthard-as via Bellinzona → Lugano → Chiasso (routebrief §2/§4).
    # Gepubliceerd ≈200 km (ontwerp); hemelsbreed 184,1 km (berekend).
    # ⚠️ Twee mislukte pogingen ("geen wegpad tussen punt 0 en 1", ook mét Zug/
    #    Luzern en eindToegangPrivaat): het vrachtplatform zelf (8.5492,47.4647)
    #    snapt op een geïsoleerde apron-service-way (airside/privéterrein zonder
    #    aansluiting op het openbare net) — exact dezelfde bevinding als het
    #    analoge been in goud-yanacocha-ticino-valcambi (zelfde ZRH-anker,
    #    zelfde golf). Profiel start daarom op het dichtstbijzijnde punt van het
    #    openbare wegennet (8.554523,47.472087, 0,91 km van het platform, komt
    #    uit dat andere profiel); de bak-functie sluit dat stukje af met een
    #    korte stippel "last mile" (airside/privé).
    "goud-loulo-ticino-zrh-valcambi": {
        "via": [
            ("Openbare weg bij Zürich Airport vrachtplatform (last-mile-aansluiting)", (8.554523, 47.472087)),
            ("Zug — A4 vanaf Zürich Airport, verplichte aansluiting richting Luzern", (8.5174, 47.1680)),
            ("Luzern — A4 sluit hier aan op de A2 zuidwaarts (Gotthard-as)", (8.3000, 47.0500)),
            ("Bellinzona — A2 komt hier het Ticino-dal in (na de Gotthard-tunnel)", (9.0205888, 46.1920538)),
            ("Lugano — doorgaande A2-corridor tussen Bellinzona en Chiasso", (8.9512275, 46.0038007)),
            ("Chiasso — grens, laatste punt vóór de afslag naar Balerna", (9.0290169, 45.8355209)),
            ("Valcambi SA, Balerna (anker, au-ref-valcambi)", (9.0051, 45.8385)),
        ],
        "id": "au-zrh-valcambi-loulo-weg",
        "naam": "Zürich Airport vrachtplatform → Valcambi-raffinaderij, Balerna (A4 Zug-Luzern → A2/Gotthard-as via Bellinzona–Lugano–Chiasso)",
        "extracts": ["zwitserland"],
        "refs": ["A4", "A2"],
        "gepubliceerdKm": 200,
        "bronnoot": "≈200 km (ontwerp); eigen hemelsbreed berekend 184,1 km (routebrief §2).",
        "vensterKm": 40,
        "eindToegangPrivaat": True,
        "uit": "goud-loulo-ticino-weg-zrh-valcambi.geojson",
    },
    # Routebrief diamant-letseng-dubai, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Letšeng-mijn (Gem Diamonds + regering Lesotho, 3.100 m) → O.R. Tambo
    # vrachtapron (JNB), eigen $3,7 mln-bergweg Mokhotlong → Oxbow/Tlaeeng-Moteng-pas
    # (A1) → Butha-Buthe → Caledonspoort-grens → Fouriesburg → Bethlehem (N5-knoop) →
    # Villiers (N3) → Johannesburg (routebrief §2/§4). Via-punten indicatief, niet
    # satelliet-gelegd (routebrief §4); alleen de twee ankers zijn dat (routebrief §3).
    # Gepubliceerd ~450 km (ontwerp; GIA bevestigt alleen Letšeng↔Maseru 214 km, niet
    # apart geverifieerd op JNB-afstand, routebrief §7). corridorKlassen ruim gezet:
    # een bergpascorridor in Lesotho en de Vrijstaat-grensstreek kan op tertiary/
    # unclassified vallen.
    "diamant-letseng-dubai-letseng-jnb": {
        "via": [
            ("Letšeng-mijn (Gem Diamonds + regering Lesotho), 3.100 m (anker, dia-letseng-mijn)", (28.86194, -29.00028)),
            ("Oxbow (Tlaeeng-/Moteng-pas) — enige doorgaande bergpas-corridor (A1)", (28.6396, -28.7712)),
            ("Butha-Buthe — laatste Lesothaanse plaats vóór de grens", (28.2333, -28.7833)),
            ("Caledonspoort-grensovergang Lesotho → Zuid-Afrika", (28.2338, -28.6949)),
            ("Fouriesburg (Zuid-Afrika) — eerste plaats na de grens", (28.2109, -28.6228)),
            ("Bethlehem (Zuid-Afrika) — knooppunt N5/N3 richting Johannesburg", (28.3110, -28.2240)),
            ("Villiers (Zuid-Afrika) — N3 tussen Free State en Gauteng", (28.6000, -27.0333)),
            ("O.R. Tambo vrachtapron (JNB), Kempton Park (anker, dia-jnb-cargo)", (28.22700, -26.14300)),
        ],
        "id": "dia-letseng-jnb-weg",
        "naam": "Letšeng-mijn → Oxbow → Butha-Buthe → Caledonspoort → Fouriesburg → Bethlehem → Villiers → O.R. Tambo vrachtapron (JNB)",
        "extracts": ["lesotho", "zuid-afrika"],
        "refs": ["A1", "N5", "N3"],
        "gepubliceerdKm": 450,
        "bronnoot": "~450 km (ontwerp, routebrief §2/§7); GIA/G&G bevestigt alleen de "
                    "$3,7 mln-bergweg en Letšeng↔Maseru 214 km, niet de exacte km naar "
                    "Johannesburg — niet apart geverifieerd.",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "eindToegangPrivaat": True,
        "uit": "diamant-letseng-dubai-weg-letseng-jnb.geojson",
    },
    # Routebrief diamant-letseng-dubai, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck DXB-vrachtterminal (Dubai Cargo Village/Cargo Gateway, Al Garhoud) →
    # DMCC/Almas Tower (JLT), Sheikh Zayed Road (E11) — enige zinnige doorgaande
    # corridor binnen Dubai, geen corridorkeuze (routebrief §2/§4/§7). Eigen anker
    # dia-dxb-cargo (25,2644/55,3661, satelliet-gelegd op de Dubai Cargo Village-
    # loodsenrij, routebrief §3) ligt ~2,7 km van het dia-dxb-cargo-anker van de
    # zusterbrieven diamant-marange-dubai/diamant-mbujimayi-dubai (andere kandidaat
    # binnen hetzelfde vrachtcomplex) — bewust NIET hergebruikt, eigen wegscan met
    # het eigen satelliet-gelegde anker.
    "diamant-letseng-dubai-dxb-dmcc": {
        "via": [
            ("DXB-vrachtterminal, Dubai Cargo Village/Cargo Gateway, Al Garhoud (anker, dia-dxb-cargo)", (55.36610, 25.26440)),
            ("DMCC / Almas Tower, Jumeirah Lake Towers (anker, dia-dmcc-almas)", (55.14120, 25.06890)),
        ],
        "id": "dia-letseng-dxb-dmcc-weg",
        "naam": "DXB-vrachtterminal → DMCC/Almas Tower (Al Garhoud → Sheikh Zayed Road E11 → JLT)",
        "extracts": ["gcc-staten"],
        "refs": ["Sheikh Zayed Road", "E11"],
        "gepubliceerdKm": 31,
        "bronnoot": "geen gepubliceerd getal; ~31 km hemelsbreed (routebrief §2), "
                    "wegafstand naar verwachting 35-40 km.",
        "vensterKm": 30,
        "uit": "diamant-letseng-dubai-weg-dxb-dmcc.geojson",
    },
    # Routebrief goud-yanacocha-ticino, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Minera Yanacocha (Newmont) → Lima Cargo City, Jorge Chávez Int'l (LIM) —
    # Carretera Panamericana Norte / Cajamarca-Lima-corridor, via Chilete (bergdal-afdaling)
    # → Pacasmayo (aansluiting doorgaande Panamericana Norte) → Trujillo → Chimbote →
    # Barranca → Huacho (laatste kustplaats vóór Lima). Gepubliceerd ~850 km (ontwerpcijfer,
    # wegafstand Cajamarca-Lima).
    "goud-yanacocha-ticino-lim": {
        "via": [
            ("Minera Yanacocha (Newmont) — mijn/laadplek (anker, au-yanacocha-mijn)", (-78.5099, -6.9858)),
            ("Chilete — afdaling bergdal naar de kust", (-78.8390, -7.2215)),
            ("Pacasmayo — aansluiting op de doorgaande Panamericana Norte", (-79.5685, -7.4029)),
            ("Trujillo — grote kustplaats op de Panamericana Norte", (-79.0288, -8.1120)),
            ("Chimbote — volgende kustplaats op de Panamericana Norte", (-78.5936, -9.0745)),
            ("Barranca — volgende kustplaats richting Lima", (-77.7609, -10.7541)),
            ("Huacho — laatste grote kustplaats vóór Lima", (-77.6050, -11.1067)),
            ("Lima Cargo City, LIM — vrachtterminal (anker, au-lim-vrachtterminal)", (-77.1039, -12.0289)),
        ],
        "id": "au-yanacocha-lim-weg",
        "naam": "Yanacocha-mijn → Lima Cargo City (LIM) (Carretera Panamericana Norte)",
        "extracts": ["peru"],
        "refs": ["Panamericana Norte", "PE-1N", "PE-3N"],
        "gepubliceerdKm": 850,
        "bronnoot": "~850 km (ontwerpcijfer, gepubliceerde wegafstand Cajamarca-Lima via de "
                    "Panamericana Norte).",
        "vensterKm": 40,
        "uit": "goud-yanacocha-ticino-weg-yanacocha-lim.geojson",
    },
    # Routebrief goud-yanacocha-ticino, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Zürich Airport vrachtplatform → Valcambi-raffinaderij, Balerna (Ticino) —
    # A4 (Zürich-Zug-Luzern) → A2/Gotthard-as (Luzern-Bellinzona-Chiasso). Gepubliceerd
    # ~200 km (ontwerpcijfer, A2/Gotthard-as).
    # ⚠️ Het vrachtplatform zelf (8.5492,47.4647) snapt op een geïsoleerde
    #    apron-service-way (component-grootte 2, gemeten) — airside/privéterrein
    #    zonder aansluiting op het openbare net, ook niet met eindToegangPrivaat
    #    (zelfde bevinding als pgm-springs-zurich, ZRH→Kloten-kluis). Het profiel
    #    start daarom op het dichtstbijzijnde punt van het openbare wegennet
    #    (8.554523,47.472087, 0,91 km van het platform, gemeten); de bak-functie
    #    sluit dat stukje af met een korte stippel "last mile" (airside/privé).
    "goud-yanacocha-ticino-valcambi": {
        "via": [
            ("Openbare weg bij Zürich Airport vrachtplatform (last-mile-aansluiting)", (8.554523, 47.472087)),
            ("Zug — A4 vanaf Zürich Airport, corridorkeuze richting Luzern", (8.5174, 47.1680)),
            ("Luzern — A4 sluit hier aan op de A2 zuidwaarts (Gotthard-as)", (8.3000, 47.0500)),
            ("Gotthard Base Tunnel-as — verplicht punt van de A2-Gotthard-corridor", (8.6465, 46.8359)),
            ("Bellinzona — de A2 komt hier het Ticino-dal in", (9.0297, 46.1954)),
            ("Chiasso — grenscorridor-punt vlak vóór de afslag naar Balerna", (9.0333, 45.8333)),
            ("Valcambi SA, Balerna — raffinaderij (anker, au-valcambi-raffinaderij)", (9.0051, 45.8385)),
        ],
        "id": "au-zrh-valcambi-weg",
        "naam": "Zürich Airport vrachtplatform → Valcambi-raffinaderij, Balerna (A4 → A2/Gotthard-as)",
        "extracts": ["zwitserland"],
        "refs": ["A4", "A2"],
        "gepubliceerdKm": 200,
        "bronnoot": "~200 km (ontwerpcijfer, A2/Gotthard-as).",
        "vensterKm": 40,
        "eindKlassen": ["residential", "service", "tertiary", "unclassified"],
        "eindToegangPrivaat": True,
        "uit": "goud-yanacocha-ticino-weg-zrh-valcambi.geojson",
    },
    # Routebrief diamant-catoca-dubai, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck ruwe diamant Catoca-mijn (Lunda Sul) → Sodiam/Endiama-exportkantoor
    # Luanda, EN230 Saurimo–Malanje + EN220 Malanje–N'dalatando–Luanda (routebrief
    # §2/§4). Via-punten uit de brief (Saurimo/Malanje/Cacuso/N'dalatando).
    # Gepubliceerd ~850 km (ontwerp); eigen hemelsbreed-som via de 4 via-punten
    # 826,6 km — komt goed overeen (routebrief §2).
    # ⚠️ corridorKlassen tertiary/unclassified/service: eerste poging (WEG_HOUD
    # kaal) gaf "geen wegpad tussen punt 0 en 1" — de dichtstbijzijnde secondary
    # bij de mijn ligt op 19,6 km, EIND_STRAAL_KM is 12 km, dus zonder corridor-
    # brede kleine klassen mist de scanner het stuk ertussen (nagemeten:
    # tertiary op 11,16 km, dan alleen unclassified/track tot de secondary).
    "diamant-catoca-dubai-catoca-luanda": {
        "via": [
            ("Catoca-mijn, Lunda Sul (anker, dia-catoca-mijn)", (20.30083, -9.39889)),
            ("Saurimo — knoop mijnweg/EN230", (20.39811, -9.65893)),
            ("Malanje — einde EN230, aansluiting EN220", (16.35000, -9.53333)),
            ("Cacuso — tussenplaats EN220", (15.74067, -9.42203)),
            ("N'dalatando — laatste knoop vóór Luanda", (14.91450, -9.29848)),
            ("Sodiam/Endiama-exportkantoor, Luanda (anker, dia-luanda-sodiam)", (13.23578, -8.81291)),
        ],
        "id": "diamant-catoca-dubai-catoca-luanda",
        "naam": "Catoca-mijn → Luanda (Sodiam/Endiama) — EN230 Saurimo–Malanje / EN220 Malanje–N'dalatando–Luanda",
        "extracts": ["angola"],
        "refs": ["EN230", "EN220"],
        "gepubliceerdKm": 850,
        "bronnoot": "~850 km (ontwerp); eigen hemelsbreed-som via de 4 via-punten 826,6 km (routebrief §2); lengtetoets ±15%.",
        "vensterKm": 40,
        "corridorKlassen": ["tertiary", "unclassified", "service"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "uit": "diamant-catoca-dubai-weg-catoca-luanda.geojson",
    },
    # Routebrief diamant-catoca-dubai, been b2 (LICHTE werkwijze M31 golf 3).
    # Truck Sodiam-kantoor Luanda → NBJ-vrachtterminal (nieuwe luchthaven Dr.
    # António Agostinho Neto, Bom Jesus/Ícolo e Bengo), nieuwe luchthaven-
    # toegangsweg/expresweg (routebrief §2/§4). Geen corridorkeuze binnen het
    # brief-onderzoek gevonden; geen via-punten in de brief, ruim venster.
    "diamant-catoca-dubai-luanda-nbj": {
        "via": [
            ("Sodiam/Endiama-exportkantoor, Luanda (anker, dia-luanda-sodiam)", (13.23578, -8.81291)),
            ("NBJ-vrachtterminal, Bom Jesus (anker, dia-nbj-vracht)", (13.51400, -9.03350)),
        ],
        "id": "diamant-catoca-dubai-luanda-nbj",
        "naam": "Luanda (Sodiam) → NBJ-vrachtterminal (nieuwe luchthaven-toegangsweg)",
        "extracts": ["angola"],
        "refs": [],
        "gepubliceerdKm": 40,
        "bronnoot": "~40 km (ontwerp/haalbaarheidstoets); eigen hemelsbreed 39,6 km (routebrief §2); lengtetoets ±15%.",
        "vensterKm": 40,
        "uit": "diamant-catoca-dubai-weg-luanda-nbj.geojson",
    },
    # Routebrief pgm-mogalakwena-londen, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Mogalakwena-concentrator (Valterra Platinum, Mokopane) → Rustenburg
    # PMR (Waterval-complex), N1 (Mokopane-Mookgophong-Bela-Bela-Pretoria-Noord)
    # → R24 "Platinum Highway" (Pretoria-Rustenburg). Geen operator-bron voor de
    # km; eigen OSRM-meting 341 km tegen het ontwerpcijfer ~180 km (routebrief
    # §7 — forse afwijking, bevinding, niet dichtgetrokken). Ruim venster om de
    # lange corridor.
    "pgm-mogalakwena-londen-mogalakwena-rustenburg": {
        "via": [
            ("Mogalakwena-concentrator (anker, pgm-mogalakwena-mijn)", (28.9160, -23.9805)),
            ("Mokopane (N1-aansluiting)", (29.0167, -24.1833)),
            ("Mookgophong (N1)", (28.7163, -24.5144)),
            ("Bela-Bela (N1)", (28.2905, -24.8806)),
            ("Akasia (N1 → R24 \"Platinum Highway\"-wissel)", (28.1136, -25.6548)),
            ("Rustenburg PMR — Waterval-complex (anker, pgm-rustenburg-pmr)", (27.3180, -25.6750)),
        ],
        "id": "pgm-mogalakwena-londen-mogalakwena-rustenburg",
        "naam": "Mogalakwena-concentrator → Rustenburg PMR (N1 → R24 Platinum Highway)",
        "extracts": ["zuid-afrika"],
        "refs": ["N1", "R24"],
        "gepubliceerdKm": 341,
        "bronnoot": "geen operator-bron; 341 km eigen OSRM-meting (routebrief pgm-mogalakwena-londen §7), werkcijfer tegen het ontwerpcijfer ~180 km.",
        "vensterKm": 50,
        "uit": "pgm-mogalakwena-londen-weg-mogalakwena-rustenburg.geojson",
    },
    # Routebrief pgm-mogalakwena-londen, been b4 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Heathrow (LHR) World Cargo Centre → Johnson Matthey Royston, M4 →
    # M25 (westring) → A1(M) → A505 Baldock-Royston. BINDEND-tekst noemt ~50 km
    # via M25/A10/A505; gemeten (OSRM) 97 km via M25/A1(M)/A505 — de A1(M) is
    # hier het functionele equivalent van de genoemde A10 (beide sluiten aan op
    # de A505 bij Baldock, routebrief §7).
    "pgm-mogalakwena-londen-heathrow-royston": {
        "via": [
            ("Heathrow (LHR) World Cargo Centre (anker, pgm-lhr-cargo)", (-0.4195, 51.4703)),
            ("Denham (M25-west)", (-0.5351, 51.5741)),
            ("Abbots Langley (M25-noord, Hertfordshire)", (-0.4059, 51.7131)),
            ("Welwyn (A1(M))", (-0.2285, 51.8100)),
            ("Baldock Bypass (A1(M) → A505-wissel)", (-0.1928, 51.9663)),
            ("Johnson Matthey Royston (anker, pgm-jm-royston)", (-0.0351, 52.0550)),
        ],
        "id": "pgm-mogalakwena-londen-heathrow-royston",
        "naam": "Heathrow World Cargo Centre → Johnson Matthey Royston (M4 → M25 → A1(M) → A505)",
        "extracts": ["groot-brittannie"],
        "refs": ["M4", "M25", "A1(M)", "A505"],
        "gepubliceerdKm": 97,
        "bronnoot": "BINDEND noemde ~50 km via M25/A10/A505; eigen OSRM-meting 97 km via M25/A1(M)/A505 (routebrief pgm-mogalakwena-londen §7).",
        "vensterKm": 30,
        "eindToegangPrivaat": True,
        "uit": "pgm-mogalakwena-londen-weg-heathrow-royston.geojson",
    },
    # Routebrief diamant-surat-hongkong, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Surat Diamond Bourse → Bharat Diamond Bourse (BKC), NH48 Surat–Mumbai via
    # Navsari/Vapi/Boisar/Vasai-Virar/Dahisar. Gepubliceerd ~280 km (ontwerp); via-punten-
    # som komt op 235,6 km — de NH48 maakt waarschijnlijk stadsomwegen in Surat/Mumbai die
    # de rechte via-keten niet meeneemt, dus een ruim venster.
    # ⚠️ DREAM City (Surat Diamond Bourse) heeft een EIGEN wegenstelsel dat in OSM een
    # geïsoleerd component van 57 knopen vormt — een echt topologiegat (gemeten
    # 2026-09-28 op de india-scan: `_wegen_graaf` + BFS geeft component-grootte 57 vanaf
    # de bourse-anchor tegen 1.780.308 vanaf Navsari; het dichtstbijzijnde punt op het
    # publieke net ligt 17 m van dat interne component, in totaal 0,325 km van het
    # ankerpunt). `eindToegangPrivaat` lost een ACCESS-filter op, geen COMPONENT-
    # scheiding, dus dat hielp niet. Eerste via-punt is daarom het routeerpunt op het
    # publieke net (NH48-zijstraat); de bake tekent het stukje anker → routeerpunt als
    # korte stippel (anker ≠ routeerpunt, bakhandleiding §2/§5).
    "diamant-surat-hongkong-surat-bdb": {
        "via": [
            ("NH48-aansluiting bij DREAM City (routeerpunt; anker dia-surat-bourse ligt 0,33 km verderop op het interne wegenstelsel)", (72.79343, 21.112178)),
            ("Navsari",                                            (72.9300, 20.9500)),
            ("Vapi",                                                (72.9170, 20.3720)),
            ("Boisar",                                              (72.7560, 19.8036)),
            ("Vasai-Virar",                                         (72.8000, 19.4700)),
            ("Dahisar (Mumbai-stadsgrens/toll naka)",               (72.859347, 19.250069)),
            ("Bharat Diamond Bourse, BKC (anker, dia-bdb)",         (72.8646, 19.0641)),
        ],
        "id": "dia-surat-bdb-weg",
        "naam": "Surat Diamond Bourse (NH48-aansluiting) → Bharat Diamond Bourse (NH48 Surat–Mumbai)",
        "extracts": ["india"],
        "refs": ["NH48"],
        "gepubliceerdKm": 280,
        "bronnoot": "~280 km (ontwerp); via-punten-som 235,6 km / hemelsbreed 227,6 km "
                    "(berekend) — de NH48 maakt waarschijnlijk stadsomwegen in Surat/Mumbai "
                    "die de rechte via-keten niet meeneemt.",
        "vensterKm": 75,
        "eindToegangPrivaat": True,
        "uit": "diamant-surat-hongkong-weg-surat-bdb.geojson",
    },
    # Routebrief diamant-surat-hongkong, been b4 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Cathay Pacific Cargo Terminal (HKG) → Hong Kong Diamond Exchange Building,
    # North Lantau Highway → Tsing Ma Bridge → Kwai Chung Interchange → Western Harbour
    # Crossing → Central. Geen harde bron; via-punten-som 32,4 km. Luchthaventerrein is
    # airside/privé, dus eindToegangPrivaat aan de kop.
    "diamant-surat-hongkong-hkgcargo-hkexchange": {
        "via": [
            ("Cathay Pacific Cargo Terminal, HKG (anker, dia-hkg-cargo)", (113.9247, 22.2975)),
            ("North Lantau Highway",                                      (113.9924, 22.3143)),
            ("Tsing Ma Bridge",                                            (114.07417, 22.35139)),
            ("Kwai Chung Interchange",                                     (114.1250, 22.36667)),
            ("Western Harbour Crossing (HK-portaal)",                      (114.15667, 22.30139)),
            ("Hong Kong Diamond Exchange Building, Central (anker, dia-hk-exchange)", (114.1570, 22.2797)),
        ],
        "id": "dia-hkgcargo-hkexchange-weg",
        "naam": "Cathay Pacific Cargo Terminal (HKG) → Hong Kong Diamond Exchange Building "
                "(North Lantau Hwy → Tsing Ma Bridge → Kwai Chung → Western Harbour Crossing)",
        "extracts": ["china"],
        "refs": [],
        "gepubliceerdKm": 32.4,
        "bronnoot": "geen harde bron; via-punten-som 32,4 km / hemelsbreed 24,0 km (berekend).",
        "vensterKm": 40,
        "eindToegangPrivaat": True,
        "uit": "diamant-surat-hongkong-weg-hkgcargo-hkexchange.geojson",
    },
    # Routebrief diamant-gaborone-surat, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck DTCB/DBGSS-sightaggregatie, Gaborone → GBE-vrachtapron (Sir Seretse Khama Intl
    # Airport) — binnen Gaborone, A1/Western Bypass Road, geen corridorkeuze, geen via-
    # punten (routebrief §2/§4). Hemelsbreed 3,7 km; ketenontwerp noemde ~15 km (afwijking
    # genoteerd in de brief §7, niet gecorrigeerd — venster ruim vanwege het verschil).
    "diamant-gaborone-surat-dtc-gbe": {
        "via": [
            ("DTCB/DBGSS-diamanthub, Gaborone (anker, dia-gaborone-dtc)", (25.9144, -24.5859)),
            ("GBE-vrachtapron, Sir Seretse Khama Intl Airport (anker, dia-gbe-cargo)", (25.9286, -24.5550)),
        ],
        "id": "diamant-gaborone-surat-dtc-gbe",
        "naam": "DTCB/DBGSS-diamanthub → GBE-vrachtapron (A1/Western Bypass Road)",
        "extracts": ["botswana"],
        "refs": [],
        "gepubliceerdKm": 3.7,
        "bronnoot": "3,7 km hemelsbreed gemeten (routebrief §2/§7); ketenontwerp noemde ~15 km, niet gecorrigeerd in het ontwerp.",
        "vensterKm": 15,
        "uit": "diamant-gaborone-surat-weg-dtc-gbe.geojson",
    },
    # Routebrief diamant-gaborone-surat, been b3 (LICHTE werkwijze M31 golf 3, haalbaar-
    # heidstoets-aanpassing — vervangt de oorspronkelijke STV-fase C). Truck CSMIA Air Cargo
    # Complex (BOM, Mumbai) → Surat Diamond Bourse (DREAM City) over de NH48 Mumbai–
    # Ahmedabad Highway, via Manor–Talasari–Vapi–Valsad–Navsari–Sachin (routebrief §2/§4).
    # Gepubliceerd ~280 km (haalbaarheidstoets); eigen via-puntensom hemelsbreed 231,1 km.
    # ⚠️ Eerste poging (WEG_HOUD kaal) gaf "geen wegpad tussen punt 6 en 7" (Navsari→Sachin,
    # het stuk waar de corridor van de NH48 afbuigt naar de Hajira-Sachin Bypass Road) →
    # corridorKlassen tertiary/unclassified toegevoegd (de Bypass Road is geen motorway/
    # secondary in OSM). Tweede poging (tertiary/unclassified(/service)) faalde daarna
    # tussen punt 3 en 4 (Vapi→Valsad) — gediagnosticeerd (component-scan op de gescande
    # graaf): het brief-punt "Valsad" (72,9260/20,6100, Wikipedia-centroïde) snapt op 113 m
    # naar een geïsoleerd stompje van 3 knopen, terwijl de échte doorgaande NH48 (trunk) ~3 km
    # zuidwestelijker loopt en de stad bewust omzeilt (bypass) — de brief-coördinaat is dus de
    # stadscentroïde, geen wegpunt. Via-punt verplaatst naar een vertex ÓP de NH48-trunk-way
    # (72,9512/20,5968) — bevinding, geen km-toets-manipulatie (werkwijze: via-punten op de
    # doorgaande weg, niet in een stadscentrum). Derde faal (tussen punt 6 en 7, Sachin→SDB):
    # het SDB-ANKER zelf (72,7953/21,1097, satelliet-gelegd) snapt op 134 m naar een
    # geïsoleerd DREAM City-interne-weg-stompje van 57 knopen; het doorgaande netwerk ligt
    # 287 m verderop (72,796653/21,107445, tertiary). Laatste via-punt is dat ROUTEERPUNT
    # (anker ≠ routeerpunt, staand projectpatroon — Napoleon Ave/RHB-klasse); de marker in de
    # bake blijft op het satelliet-gelegde ankerpunt, de resterende ~0,29 km last-mile-stub
    # komt in §9 als bevinding, niet als stippel (< 0,5 km toetsnorm).
    "diamant-gaborone-surat-bom-sdb": {
        "via": [
            ("CSMIA Air Cargo Complex, Mumbai/BOM (anker, dia-bom-cargo, hergebruikt)", (72.8673, 19.0994)),
            ("Manor (Palghar-district) — NH48-knooppunt", (72.9096, 19.7228)),
            ("Talasari — Maharashtra–Gujarat-grens, NH48-flyover", (72.9164, 20.1222)),
            ("Vapi — eerste grote Gujarat-industriestad op de NH48", (72.9170, 20.3720)),
            ("Valsad-bypass — NH48-trunk (verplaatst van de stadscentroïde 72,9260/20,6100, die 3 km van de weg ligt)", (72.9512158, 20.5967851)),
            ("Navsari — doorgaande NH48-stad vlak vóór Surat", (72.9300, 20.9500)),
            ("Sachin — hier buigt de corridor af naar de Hajira-Sachin Bypass Road", (72.8805, 21.0853)),
            ("Surat Diamond Bourse — routeerpunt op het doorgaande net (anker dia-sdb ligt 0,29 km verderop, geïsoleerd DREAM City-wegje)", (72.796653, 21.107445)),
        ],
        "id": "diamant-gaborone-surat-bom-sdb",
        "naam": "CSMIA Air Cargo Complex (BOM) → Manor → Talasari → Vapi → Valsad → Navsari → Sachin → Surat Diamond Bourse (NH48)",
        "extracts": ["india"],
        "refs": ["NH48"],
        "gepubliceerdKm": 280,
        "bronnoot": "~280 km (haalbaarheidstoets, NH48 Mumbai–Ahmedabad Highway); eigen via-puntensom 231,1 km hemelsbreed (routebrief §2/§7).",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified", "service"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified"],
        "uit": "diamant-gaborone-surat-weg-bom-sdb.geojson",
    },
    # Routebrief diamant-marange-dubai, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Marange-diamantvelden (ZCDC) → Harare (HRE) vrachtterminal, A9
    # Mutare–Harare via Mutare/Rusape/Marondera (routebrief §2/§4). Geen
    # gepubliceerde wegkm gevonden binnen het webbudget → ontwerp-schatting
    # ~270 km als gepubliceerdKm (som via-punten hemelsbreed 275,4 km),
    # ruim venster (40 km, standaardcorridor, geen bekende sterke uitbuiging).
    # ⚠️ Eerste poging (mijnanker als punt 0, corridorKlassen tertiary/
    #    unclassified/service + eindToegangPrivaat) faalde op "geen wegpad
    #    tussen punt 0 en 1" — gemeten (osmium-connectiviteitscheck op de
    #    zimbabwe-extract): het mijnanker snapt op een geïsoleerd 8-knopen-
    #    eilandje (0,14 km) van vooral `track`-ways, dat NIET verbonden is met
    #    de grote wegcomponent (2,25 mln knopen, incl. Mutare/de P4). De
    #    dichtstbijzijnde `service`-weg die WEL in die grote component zit ligt
    #    op 0,79 km van het mijnanker (-19,5956/32,3469) — dus via-punt hier
    #    ingevoegd als de echte start van het gescande wegbeen; de 0,79 km
    #    tussen het mijnanker en dit punt gaat als stippel "last mile (geen
    #    net op deze korrel — track-only mijnwegen)" in de bak-functie.
    "diamant-marange-dubai-marange-hre": {
        "via": [
            ("Marange-mijnweg — aansluiting doorgaand wegnet (0,79 km vanaf mijnanker dia-marange-mijn)", (32.3469, -19.5956)),
            ("Mutare — eerste stadsknoop op de A9 (op de R5/Harare-Mutare Highway, geprojecteerd vanaf het stadscentrum 32.6333/-18.9667 — dat punt snapt op een geïsoleerde wegstomp, gemeten met een osmium-connectiviteitscheck)", (32.6426, -18.9511)),
            ("Rusape — tussenstad op de A9", (32.1247, -18.5367)),
            ("Marondera — laatste tussenstad vóór Harare", (31.5467, -18.1897)),
            ("Robert Gabriel Mugabe Intl (HRE), vrachtterminal (anker, dia-hre-cargo)", (31.0946, -17.9218)),
        ],
        "id": "diamant-marange-dubai-marange-hre",
        "naam": "Marange-mijnweg-aansluiting → Harare (HRE) vrachtterminal (A9 Mutare–Harare)",
        "extracts": ["zimbabwe"],
        "refs": [],
        "gepubliceerdKm": 270,
        "bronnoot": "geen gepubliceerde wegkm gevonden; ~270 km ontwerpcijfer (routebrief §2), som via-punten hemelsbreed 275,4 km; lengtetoets ±15%.",
        "vensterKm": 40,
        "corridorKlassen": ["tertiary", "unclassified", "service"],
        "eindToegangPrivaat": True,
        "uit": "diamant-marange-dubai-weg-marange-hre.geojson",
    },
    # Routebrief diamant-marange-dubai, been b3 (LICHTE werkwijze M31 golf 3,
    # toegevoegd op de haalbaarheidstoets). Truck Dubai Intl (DXB) vrachtterminal
    # → DMCC/Almas Tower (JLT), Sheikh Zayed Road (E11) — enige doorgaande
    # corridor (routebrief §2/§4). Ankers hergebruikt van de zusterbrief
    # diamant-mbujimayi-dubai (dezelfde DXB-vrachtterminal en DMCC-coördinaten,
    # beide bron-gelegd in deze golf).
    "diamant-marange-dubai-dxb-dmcc": {
        "via": [
            ("Dubai Intl (DXB), vrachtterminal (anker, dia-dxb-cargo, hergebruikt)", (55.3406, 25.2575)),
            ("Dubai World Trade Centre-interchange — eerste vaste interchange op de E11", (55.2888, 25.2276)),
            ("Mall of the Emirates-interchange — tweede vaste interchange, vlak vóór JLT/DMCC", (55.2006, 25.1181)),
            ("DMCC / Almas Tower, Jumeirah Lake Towers (anker, dia-dmcc, hergebruikt)", (55.1412, 25.0691)),
        ],
        "id": "diamant-marange-dubai-dxb-dmcc",
        "naam": "Dubai Intl (DXB) vrachtterminal → DMCC/Almas Tower (Sheikh Zayed Road E11)",
        "extracts": ["gcc-staten"],
        "refs": ["Sheikh Zayed Road", "E11"],
        "gepubliceerdKm": 34,
        "bronnoot": "geen gepubliceerde wegkm; hemelsbreed 29,0 km (routebrief §2), verwacht ~32-38 km werkelijke wegafstand; lengtetoets ±15%.",
        "vensterKm": 20,
        "uit": "diamant-marange-dubai-weg-dxb-dmcc.geojson",
    },
    # Routebrief pgm-norilsk-krasnojarsk, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Yemelyanovo-vrachtplatform (KJA) → Krastsvetmet-raffinaderij, Krasnoyarsk.
    # Overpass was onbereikbaar bij het schrijven van de brief; via-punten hier
    # zelf gepind met pyosmium op de lokale rusland-siberie-extract (bbox-scan
    # op highway=trunk/primary rond Krasnoyarsk): R-255 "Sibir" (luchthavenweg,
    # geen R257 zoals de brief vermoedde — dat is de andere kant van de stad)
    # → Северное шоссе/Енисейский тракт-ringwegknoop → Октябрьский мост
    # (Jenisej-oversteek) → Krastsvetmet-terrein. Hemelsbreed-keten via deze
    # via-punten 37,5 km, tegen 34,5 km directe hemelsbreed-afstand — dicht bij
    # de door de briefschrijver herziene richtwaarde ~35-40 km (het ontwerp gaf
    # ten onrechte 25 km, gebaseerd op R257 i.p.v. de echte R-255/Северное
    # шоссе/Октябрьский мост-corridor).
    # ⚠️ Eerste via-punt is NIET de vrachtterminal-anker zelf: het hele kleine-
    # klasse-wegennet rond de cargoterminal bestaat uit OSM-eilandjes (4-7
    # knopen) die geen gedeelde knoop met het doorgaande net delen (component-
    # scan op de gescande graaf, zelfde klasse als Beilun-havenspoor/
    # cu-beilun-laadspoor) — de eerste PRIMARY-vertex van 04А-300 (0,8 km van
    # het anker) is wél in het hoofdcomponent; de bake-functie tekent dat
    # laatste stukje als korte stippel truck vanaf het echte anker.
    "pgm-norilsk-krasnojarsk-yemelyanovo-krastsvetmet": {
        "via": [
            ("04А-300 — eerste primary-knoop bij Yemelyanovo (0,8 km van het anker)", (92.5275, 56.1718)),
            ("R-255 \"Sibir\" — hoofdweg Yemelyanovo → Krasnojarsk", (92.7361, 56.1315)),
            ("Северное шоссе / Енисейский тракт — ringweg-knoop noord", (92.9345, 56.0807)),
            ("Октябрьский мост — Jenisej-oversteek", (92.9440, 56.0245)),
            ("Krastsvetmet-raffinaderij, Krasnojarsk (anker, pgm-krastsvetmet-raffinaderij)", (92.9998, 56.0160)),
        ],
        "id": "pgm-yemelyanovo-krastsvetmet-weg",
        "naam": "Yemelyanovo-vrachtterminal (KJA) → R-255 → Северное шоссе → Октябрьский мост → Krastsvetmet-raffinaderij",
        "extracts": ["rusland-siberie"],
        "refs": ["Р-255", "04К-044"],
        "gepubliceerdKm": 40,
        "bronnoot": "ontwerp gaf 25 km (R257-aanname); hemelsbreed gemeten 34,5 km, "
                    "eigen via-puntenketen 37,5 km → 40 km als toetswaarde "
                    "(brief §2/§7, herzien van de ontwerp-indicatie).",
        "vensterKm": 40,
        "corridorKlassen": ["tertiary", "unclassified"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified"],
        "uit": "pgm-norilsk-krasnojarsk-weg-yemelyanovo-krastsvetmet.geojson",
    },
    # Routebrief diamant-venetia-antwerpen, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck ruwe diamant Venetia-mijn (De Beers, Limpopo) → O.R. Tambo vrachtterminal
    # (JNB), N1/R572 via Louis Trichardt/Makhado, Polokwane, Mokopane, Bela-Bela,
    # Pretoria, Kempton Park N1/R21-knoop. Gepubliceerd ~440 km (ontwerp); webcheck
    # OSRM 491,1 km.
    "diamant-venetia-antwerpen-venetia-jnb": {
        "via": [
            ("Venetia-mijn (De Beers), open put (anker, dia-venetia-mijn)", (29.3175, -22.4362)),
            ("Louis Trichardt/Makhado — N1/R572-knoop", (29.9000, -23.0500)),
            ("Polokwane — N1", (29.4500, -23.9000)),
            ("Mokopane — N1", (29.0167, -24.1833)),
            ("Bela-Bela — N1", (28.2833, -24.8833)),
            ("Pretoria — N1-ring", (28.1881, -25.7461)),
            ("Kempton Park — N1/R21-knoop", (28.2333, -26.1000)),
            ("O.R. Tambo vrachtterminal, Kempton Park (anker, dia-jnb-cargo)", (28.2300, -26.1400)),
        ],
        "id": "dia-venetia-jnb-weg",
        "naam": "Venetia-mijn → O.R. Tambo vrachtterminal (N1/R572 via Polokwane)",
        "extracts": ["zuid-afrika"],
        "refs": ["N1", "R572", "R21"],
        "gepubliceerdKm": 491.1,
        "bronnoot": "~440 km (ontwerp); webcheck OSRM 491,1 km — leidend (bakhandleiding §2).",
        "vensterKm": 75,
        "eindToegangPrivaat": True,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "diamant-venetia-antwerpen-weg-venetia-jnb.geojson",
    },
    # Routebrief diamant-mbujimayi-dubai, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck MIBA-terrein/exportkantoor Mbuji-Mayi → Mbuji-Mayi Airport (MJM),
    # Avenue Inga — stadsverbinding, geen corridorkeuze, geen via-punten
    # (routebrief §2/§4). Geen betrouwbare wegreferentie → venster ruim.
    "diamant-mbujimayi-dubai-miba-mjm": {
        "via": [
            ("MIBA-terrein/exportkantoor, Mbuji-Mayi (anker, dia-mbm-miba)", (23.6000, -6.1300)),
            ("Mbuji-Mayi Airport (MJM) (anker, dia-mbm-mjm)", (23.5682265, -6.1188177)),
        ],
        "id": "diamant-mbujimayi-dubai-miba-mjm",
        "naam": "MIBA-terrein/exportkantoor → Mbuji-Mayi Airport (MJM)",
        "extracts": ["congo-drc"],
        "refs": [],
        "gepubliceerdKm": 5,
        "bronnoot": "~5 km ontwerpcijfer (routebrief §2), hemelsbreed 3,7 km; geen betrouwbare gepubliceerde wegreferentie.",
        "vensterKm": 15,
        "uit": "diamant-mbujimayi-dubai-weg-miba-mjm.geojson",
    },
    # Routebrief diamant-mbujimayi-dubai, been b4 (LICHTE werkwijze M31 golf 3,
    # toegevoegd door de haalbaarheidstoets). Truck DXB-vrachtterminal →
    # DMCC/Almas Tower, Airport Road → Sheikh Zayed Road/Al Ittihad Road —
    # binnen Dubai, geen corridorkeuze. Geen gepubliceerde wegkm.
    "diamant-mbujimayi-dubai-dxb-dmcc": {
        "via": [
            ("Dubai Intl Airport (DXB), vrachtcomplex (anker, dia-dxb-cargo)", (55.3405972, 25.2574524)),
            ("DMCC / Almas Tower, Dubai (anker, dia-dmcc)", (55.1411656, 25.0690625)),
        ],
        "id": "diamant-mbujimayi-dubai-dxb-dmcc",
        "naam": "DXB-vrachtterminal → DMCC/Almas Tower (Airport Road → Sheikh Zayed Road/Al Ittihad Road)",
        "extracts": ["gcc-staten"],
        "refs": ["Sheikh Zayed Road", "Airport Road", "Al Ittihad Road"],
        "gepubliceerdKm": 34,
        "bronnoot": "geen gepubliceerde wegkm; hemelsbreed 29,0 km, verwacht ~32-38 km werkelijke wegafstand.",
        "vensterKm": 30,
        "uit": "diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson",
    },
    # Routebrief diamant-mumbai-newyork, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck Bharat Diamond Bourse (BKC, Mumbai) → Sahar/CSMIA Air Cargo Complex
    # (BOM) — binnen Mumbai, <4 km hemelsbreed, geen corridorkeuze, geen
    # via-punten (routebrief §2/§4). Gepubliceerd ~10 km (ontwerp).
    "diamant-mumbai-newyork-bdb-bomcargo": {
        "via": [
            ("Bharat Diamond Bourse, BKC, Mumbai (anker, dia-bdb, hergebruikt)", (72.8646, 19.0641)),
            ("Sahar/CSMIA Air Cargo Complex, Mumbai (anker, dia-bom-cargo, hergebruikt)", (72.8673, 19.0994)),
        ],
        "id": "diamant-mumbai-newyork-bdb-bomcargo",
        "naam": "Bharat Diamond Bourse → Sahar/CSMIA Air Cargo Complex (BKC-connector/Airport Road)",
        "extracts": ["india"],
        "refs": [],
        "gepubliceerdKm": 10,
        "bronnoot": "geen gepubliceerde km; ~10 km ontwerpcijfer (routebrief §2), hemelsbreed 3,9 km; lengtetoets ±15%.",
        "vensterKm": 40,
        "uit": "diamant-mumbai-newyork-weg-bdb-bomcargo.geojson",
    },
    # Routebrief diamant-mumbai-newyork, been b3 (LICHTE werkwijze M31 golf 3).
    # Truck JFK South Cargo Area (JFK) → 47th Street Diamond Exchange,
    # Manhattan — Van Wyck Expressway (I-678) → Kew Gardens Interchange →
    # Long Island Expressway → Queens-Midtown Tunnel → Manhattan (routebrief §4).
    "diamant-mumbai-newyork-jfk-47th": {
        "via": [
            ("JFK South Cargo Area (anker, dia-jfk-cargo)", (-73.7952, 40.6587)),
            ("Van Wyck Expressway, nabij JFK", (-73.8051, 40.6504)),
            ("Van Wyck Expressway, ter hoogte van Kew Gardens", (-73.8166, 40.7033)),
            ("Kew Gardens Interchange", (-73.8279, 40.7165)),
            ("Queens-Midtown Tunnel, Queens-portaal (Long Island City)", (-73.9522, 40.7418)),
            ("Queens-Midtown Tunnel, Manhattan-portaal (Tudor City)", (-73.9719, 40.7463)),
            ("47th Street Diamond Exchange, Manhattan (anker, dia-ny-47th)", (-73.9817, 40.7578)),
        ],
        "id": "diamant-mumbai-newyork-jfk-47th",
        "naam": "JFK South Cargo Area → 47th Street Diamond Exchange (Van Wyck → Kew Gardens → LIE → Queens-Midtown Tunnel)",
        "extracts": ["us-new-york"],
        "refs": ["I-678", "I-495"],
        "gepubliceerdKm": 25,
        "bronnoot": "geen gepubliceerde km; ~25 km ontwerpcijfer (routebrief §2), hemelsbreed 19,2 km; lengtetoets ±15%.",
        "vensterKm": 40,
        "uit": "diamant-mumbai-newyork-weg-jfk-47th.geojson",
    },
    # Routebrief diamant-namdeb-gaborone, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck ruwe diamant Namdeb-terrein Oranjemund → NDTC/Namdeb-sortering
    # Windhoek: B4 (Oranjemund-omgeving → Rosh Pinah → Aus → Keetmanshoop) →
    # B1 (Keetmanshoop → Mariental → Rehoboth → Windhoek). Lange corridor met
    # een C13/B4-knik bij Rosh Pinah — venster ruim (75 km). Gepubliceerd
    # ~900 km (ontwerp/brief §2), refs leeg (B4/B1 zijn de enige doorgaande
    # noord-zuidcorridor in Zuid-Namibië, geen alternatieve routekeuze).
    "diamant-namdeb-gaborone-oranjemund-windhoek": {
        "via": [
            ("Namdeb-terrein, Oranjemund (anker, dia-namdeb-oranjemund)", (16.42375, -28.55284)),
            ("Rosh Pinah — B4-aansluiting", (16.7600, -27.9650)),
            ("Aus — B4-bocht naar oost", (16.2667, -26.6667)),
            ("Keetmanshoop — wisselpunt B4→B1", (18.1333, -26.5786)),
            ("Mariental — B1", (17.9667, -24.6333)),
            ("Rehoboth — B1, laatste plaats vóór Windhoek", (17.0833, -23.3167)),
            ("NDTC/Namdeb-sortering, Windhoek (anker, dia-ndtc-windhoek)", (17.08384, -22.56482)),
        ],
        "id": "diamant-namdeb-gaborone-oranjemund-windhoek",
        "naam": "Namdeb-terrein Oranjemund → NDTC/Namdeb-sortering Windhoek (B4 → B1)",
        "extracts": ["namibie"],
        "refs": [],
        "gepubliceerdKm": 900,
        "bronnoot": "geen gepubliceerde km; ~900 km ontwerpcijfer via de via-keten (routebrief §2), lengtetoets ±15%.",
        "vensterKm": 75,
        "uit": "diamant-namdeb-gaborone-weg-oranjemund-windhoek.geojson",
    },
    # Routebrief diamant-namdeb-gaborone, been b2 (LICHTE werkwijze M31 golf 3).
    # Truck NDTC/Namdeb-sortering Windhoek → Hosea Kutako Airport (WDH), B6
    # oostwaarts uit Windhoek — geen via-punten nodig (<50 km, B6 eenduidig).
    # Gepubliceerd 45 km (Wikipedia: "45 km ten oosten van de stad"); eigen
    # hemelsbreed-meting ~40 km.
    "diamant-namdeb-gaborone-windhoek-wdh": {
        "via": [
            ("NDTC/Namdeb-sortering, Windhoek (anker, dia-ndtc-windhoek)", (17.08384, -22.56482)),
            ("Hosea Kutako Airport WDH, vrachtapron (anker, dia-wdh-cargo)", (17.4643, -22.4863)),
        ],
        "id": "diamant-namdeb-gaborone-windhoek-wdh",
        "naam": "NDTC/Namdeb-sortering Windhoek → Hosea Kutako Airport WDH (B6)",
        "extracts": ["namibie"],
        "refs": ["B6"],
        "gepubliceerdKm": 45,
        "bronnoot": "Wikipedia: Hosea Kutako Airport '45 km ten oosten van' Windhoek; hemelsbreed ~40 km (routebrief §2).",
        "vensterKm": 40,
        "uit": "diamant-namdeb-gaborone-weg-windhoek-wdh.geojson",
    },
    # Routebrief pgm-rustenburg-tokio, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck geraffineerd PGM Rustenburg PMR (Valterra Platinum) → OR Tambo
    # vrachtterminal (JNB), N4 (Platinum Highway) via Kroondal → Brits →
    # N4/N1-knoop Pretoria-West → N1/R21-knoop Allandale → R21. ⚠️ PMR-anker
    # gecorrigeerd t.o.v. de eigen brief (open punt §7: -25,9500/27,3000 bleek
    # landbouwgrond): hergebruikt het satelliet-gelegde Waterval-smelter/RBMR/
    # PMR-complex-anker uit de zusterbrieven van dezelfde golf/grondstof
    # (pgm-rustenburg-shanghai.md / pgm-zimplats-rustenburg.md / pgm-
    # mogalakwena-londen.md, alle "bron-gelegd" op z15-z17), -25,6750/27,3180.
    # Gepubliceerd ~120 km (ontwerp, brief §2), lengtetoets ±15%.
    "pgm-rustenburg-tokio-rustenburg-jnb": {
        "via": [
            ("Rustenburg PMR — Waterval-complex (anker, pgm-rustenburg-pmr, hergebruikt+gecorrigeerd)", (27.3180, -25.6750)),
            ("Kroondal — R565/N4-oprit", (27.3078, -25.7253)),
            ("Brits — N4-kruispunt", (27.7814, -25.6350)),
            ("Pretoria-West — N4/N1-knoop (Proefplaas)", (28.1425, -25.7615)),
            ("Allandale — N1/R21-knoop", (28.1234, -25.9977)),
            ("OR Tambo vrachtterminal (anker, pgm-jnb-vracht)", (28.2300, -26.1400)),
        ],
        "id": "pgm-rustenburg-tokio-rustenburg-jnb",
        "naam": "Rustenburg PMR → OR Tambo vrachtterminal (N4/N1)",
        "extracts": ["zuid-afrika"],
        "refs": ["N4", "N1", "R21"],
        "gepubliceerdKm": 120,
        "bronnoot": "geen gepubliceerde km; ~120 km ontwerpcijfer (routebrief pgm-rustenburg-tokio §2), lengtetoets ±15%.",
        "vensterKm": 40,
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "eindToegangPrivaat": True,
        "uit": "pgm-rustenburg-tokio-weg-rustenburg-jnb.geojson",
    },
    # Routebrief pgm-rustenburg-tokio, been b3 (LICHTE werkwijze M31 golf 3).
    # Truck Narita vrachtterminal (NRT) → Tanaka Kikinzoku Kogyo, Tokio
    # (Nihonbashi-Kayabacho, Chuo-ku), Higashi-Kanto Jidoshado → Keiyo-weg →
    # Shuto-Wangan-route. Gepubliceerd ~65 km (ontwerp, brief §2).
    "pgm-rustenburg-tokio-narita-tanaka": {
        "via": [
            ("Narita vrachtterminal (anker, pgm-nrt-vracht)", (140.3797, 35.7743)),
            ("Narita-IC — Higashi-Kanto Jidoshado", (140.3183, 35.7767)),
            ("Chiba-kita IC — overgang naar de Keiyo-weg", (140.1064, 35.6073)),
            ("Ichikawa/Wangan-knoop", (139.8869, 35.6825)),
            ("Tanaka Kikinzoku Kogyo, Tokio (anker, pgm-tanaka-tokio)", (139.7756, 35.6816)),
        ],
        "id": "pgm-rustenburg-tokio-narita-tanaka",
        "naam": "Narita vrachtterminal → Tanaka Kikinzoku Kogyo, Tokio (Higashi-Kanto → Keiyo → Wangan)",
        "extracts": ["japan"],
        "refs": [],
        "gepubliceerdKm": 65,
        "bronnoot": "geen gepubliceerde km; ~65 km ontwerpcijfer (routebrief pgm-rustenburg-tokio §2), lengtetoets ±15%.",
        "vensterKm": 40,
        "uit": "pgm-rustenburg-tokio-weg-narita-tanaka.geojson",
    },
    # Routebrief diamant-jwaneng-antwerpen, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck ruwe diamant Jwaneng-mijn (Debswana) → Diamond Technology Park,
    # Gaborone (De Beers/DBGSS sight-aggregatie), Trans-Kalahari Corridor (A2)
    # via Sese–Kanye–Moshupa–Gabane. Gepubliceerd 170 km (Wikipedia); webcheck
    # OSRM 166,7 km. Vrijwel één hoofdweg — de vijf via-punten pinnen de
    # corridor, geen echte routekeuze (routebrief §7).
    "diamant-jwaneng-antwerpen-jwaneng-gaborone": {
        "via": [
            ("Jwaneng-mijn — concentrator/fabriekscomplex (anker, dia-jwaneng-mill)", (24.7083, -24.5303)),
            ("Sir Seretse Khama Ave / Trans-Kalahari-aansluiting", (24.7299, -24.5914)),
            ("Trans-Kalahari Corridor bij Sese", (25.0140, -24.8079)),
            ("Trans-Kalahari Corridor bij Kanye", (25.2955, -24.9502)),
            ("Moshupa, Thamaga Road-kruising", (25.4426, -24.7586)),
            ("Gabane, nabij Gaborone", (25.8030, -24.6531)),
            ("Diamond Technology Park, Gaborone (anker, dia-gaborone-dtp)", (25.9149, -24.5899)),
        ],
        "id": "dia-jwaneng-gaborone-weg",
        "naam": "Jwaneng-mijn → Gaborone Diamond Technology Park (Trans-Kalahari Corridor/A2)",
        "extracts": ["botswana"],
        "refs": [],
        "gepubliceerdKm": 170,
        "bronnoot": "170 km SW of Gaborone (Wikipedia, Jwaneng diamond mine); webcheck OSRM 166,7 km.",
        "vensterKm": 40,
        "uit": "diamant-jwaneng-antwerpen-weg-jwaneng-gaborone.geojson",
    },
    # Routebrief diamant-jwaneng-antwerpen, been b2 (LICHTE werkwijze M31 golf 3).
    # Truck Gaborone Diamond Technology Park → GBE-vrachtapron (Sir Seretse
    # Khama International Airport), Airport Road — korte stadsrand-hop binnen
    # de Diamond Hub SEZ. Webcheck OSRM 5,0 km (corrigeert het ontwerp-cijfer
    # van ~15 km).
    "diamant-jwaneng-antwerpen-gaborone-gbe": {
        "via": [
            ("Diamond Technology Park, Gaborone (anker, dia-gaborone-dtp)", (25.9149, -24.5899)),
            ("Airport Road, aftakking bij DTP", (25.9168, -24.5874)),
            ("Sir Seretse Khama Int'l Airport — vrachtapron/hangaar (anker, dia-gbe-cargo)", (25.9242, -24.5576)),
        ],
        "id": "dia-gaborone-gbe-weg",
        "naam": "Gaborone DTP → GBE-vrachtapron (Airport Road)",
        "extracts": ["botswana"],
        "refs": [],
        "gepubliceerdKm": 5,
        "bronnoot": "ontwerp ~15 km; webcheck OSRM 5,0 km (DTP ligt al in de Diamond Hub SEZ vlak bij de luchthaven) — gecorrigeerd cijfer.",
        "vensterKm": 15,
        "uit": "diamant-jwaneng-antwerpen-weg-gaborone-gbe.geojson",
    },
    # Routebrief diamant-jwaneng-antwerpen, been b4 (LICHTE werkwijze M31 golf 3).
    # Truck Brucargo (Brussels Airport) → AWDC/Diamond Office, Antwerpen, E19
    # via Mechelen. Gepubliceerd ~40 km (ontwerp); webcheck OSRM 37,7 km.
    "diamant-jwaneng-antwerpen-brucargo-antwerpen": {
        "via": [
            ("Brucargo, Brussels Airport (anker, dia-bru-cargo)", (4.4576, 50.9056)),
            ("E19 bij Mechelen", (4.4481, 51.0213)),
            ("E19/R1-knooppunt Antwerpen-Zuid (Wilrijk)", (4.4319, 51.1103)),
            ("AWDC / Diamond Office, Hoveniersstraat (anker, dia-antwerp-awdc)", (4.4185, 51.2154)),
        ],
        "id": "dia-brucargo-antwerpen-weg",
        "naam": "Brucargo → AWDC Antwerpen (E19 via Mechelen)",
        "extracts": ["belgie"],
        "refs": ["E19"],
        "gepubliceerdKm": 40,
        "bronnoot": "~40 km (ontwerp); webcheck OSRM 37,7 km.",
        "vensterKm": 20,
        "uit": "diamant-jwaneng-antwerpen-weg-brucargo-antwerpen.geojson",
    },
    # Routebrief pgm-rustenburg-shanghai, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck geraffineerd Pt/Pd/Rh Rustenburg PMR (Valterra Platinum, Waterval-
    # complex) → OR Tambo (JNB) vrachtterminal, N4 (Rustenburg-Brits-Pretoria)
    # → N1/R21 (Pretoria-Midrand-Kempton Park). Toetswaarde ~120 km
    # (ontwerpcijfer, indicatief — routebrief §7).
    "pgm-rustenburg-shanghai-rustenburg-jnb": {
        "via": [
            ("Rustenburg PMR — Waterval-complex (anker, pgm-rustenburg-pmr)", (27.3180, -25.6750)),
            ("Brits (N4-knoop)", (27.7811, -25.6344)),
            ("Pretoria (N4/N1-knoop, Proefplein-omgeving)", (28.1881, -25.7461)),
            ("Midrand (N1-corridor)", (28.1264, -25.9992)),
            ("Kempton Park (N1/R21-knoop)", (28.2333, -26.1000)),
            ("OR Tambo (JNB) vrachtterminal (anker, pgm-jnb-cargo)", (28.2270, -26.1380)),
        ],
        "id": "pgm-rustenburg-shanghai-rustenburg-jnb",
        "naam": "Rustenburg PMR → OR Tambo (JNB) vrachtterminal (N4 → N1/R21)",
        "extracts": ["zuid-afrika"],
        "refs": ["N4", "N1", "R21"],
        "gepubliceerdKm": 120,
        "bronnoot": "geen gepubliceerde km; ~120 km ontwerpcijfer (routebrief pgm-rustenburg-shanghai §2/§7), lengtetoets ±15%.",
        "vensterKm": 40,
        "eindToegangPrivaat": True,
        "uit": "pgm-rustenburg-shanghai-weg-rustenburg-jnb.geojson",
    },
    # Routebrief diamant-ekati-antwerpen, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Brucargo (Brussels Airport vrachtterminal) → AWDC/Diamond Office
    # Antwerpen, E19 (Vilvoorde → Mechelen-west → Antwerpen-Zuid/R1). De drie
    # via-punten zijn indicatief (brief §4/§7) — E19 is de enige doorgaande
    # motorwegcorridor Brussel–Antwerpen, geen alternatieve routekeuze.
    # Toetswaarde ~40 km (ontwerp); hemelsbreed 35,2 km.
    "diamant-ekati-antwerpen-brucargo-awdc": {
        "via": [
            ("Brucargo, Brussels Airport (anker, dia-brucargo)", (4.45584, 50.90628)),
            ("Vilvoorde — E19-knoop", (4.434, 50.933)),
            ("Mechelen — E19 westzijde", (4.460, 51.020)),
            ("Antwerpen-Zuid — R1/E19-knoop", (4.400, 51.190)),
            ("AWDC / Diamond Office, Hoveniersstraat (anker, dia-awdc)", (4.41870, 51.21520)),
        ],
        "id": "dia-brucargo-awdc-weg",
        "naam": "Brucargo → AWDC Antwerpen (E19)",
        "extracts": ["belgie"],
        "refs": ["E19"],
        "gepubliceerdKm": 40,
        "bronnoot": "geen gepubliceerde km; ~40 km uit het ketenontwerp, hemelsbreed 35,2 km.",
        "vensterKm": 40,
        "uit": "diamant-ekati-antwerpen-weg-brucargo-awdc.geojson",
    },
    # Routebrief pgm-zimplats-rustenburg, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck PGM-matte Zimplats Selous Metallurgical Complex (SMC) → grensovergang
    # Beitbridge, A5 (Chegutu-Harare) → A4/A1 (Harare-Beatrice-Chivhu-Masvingo-
    # Beitbridge). Gepubliceerd ~450 km (ketenontwerp); eigen via-puntensom komt
    # aanzienlijk hoger uit (~600-650 km) — venster ruim gezet, verwacht een
    # afwijking buiten ±15% (bevinding, zie routebrief §7, geen reden om
    # via-punten te schrappen).
    "pgm-zimplats-rustenburg-smc-beitbridge": {
        "via": [
            ("Zimplats SMC — smelter/concentrator (anker, pgm-zimplats-smc)", (30.4334, -18.0328)),
            ("Chegutu (A5-knooppunt)", (30.1460, -18.1305)),
            ("Harare (A5 → A4-wissel)", (31.0467, -17.8362)),
            ("Beatrice (begin A4 zuidwaarts)", (30.8544, -18.2581)),
            ("Chivhu (A4 tussenstop)", (30.8969, -19.0187)),
            ("Masvingo (A4 = R1)", (30.8332, -20.0745)),
            ("Beitbridge — grensovergang (anker, pgm-beitbridge-grens)", (29.9865, -22.2244)),
        ],
        "id": "pgm-zimplats-beitbridge-weg",
        "naam": "Zimplats SMC → Beitbridge (A5 → A4/A1)",
        "extracts": ["zimbabwe"],
        "refs": ["A5", "A4", "A1", "R1"],
        "gepubliceerdKm": 450,
        "bronnoot": "~450 km ketenontwerp; eigen via-puntensom ~600-650 km, buiten ±15% verwacht (routebrief §7).",
        "vensterKm": 90,
        "uit": "pgm-zimplats-rustenburg-weg-smc-beitbridge.geojson",
    },
    # Routebrief pgm-zimplats-rustenburg, been b2 (LICHTE werkwijze M31 golf 3).
    # Truck PGM-matte grensovergang Beitbridge → Rustenburg PMR (Valterra
    # Platinum), N1 (Musina-Polokwane-Pretoria) → N4 (Pretoria-Rustenburg).
    # Gepubliceerd ~500 km (ketenontwerp); eigen via-puntensom ~526 km, past
    # binnen ±15%.
    "pgm-zimplats-rustenburg-beitbridge-rustenburg": {
        "via": [
            ("Beitbridge — grensovergang (anker, pgm-beitbridge-grens)", (29.9865, -22.2244)),
            ("Musina (eerste stad na de grens)", (30.0269, -22.3454)),
            ("Polokwane (N1)", (29.4803, -23.9218)),
            ("Pretoria — N1/N4-wissel (N4-afslag Rustenburg)", (28.2761, -25.6357)),
            ("Rustenburg — N4/R24-kruising", (27.2572, -25.7031)),
            ("Rustenburg PMR — Waterval-complex (anker, pgm-rustenburg-pmr)", (27.3272, -25.6838)),
        ],
        "id": "pgm-beitbridge-rustenburg-weg",
        "naam": "Beitbridge → Rustenburg PMR (N1 → N4)",
        "extracts": ["zuid-afrika"],
        "refs": ["N1", "N4", "R24"],
        "gepubliceerdKm": 500,
        "bronnoot": "~500 km ketenontwerp; eigen via-puntensom ~526 km, sluit goed aan (binnen ±15%).",
        "vensterKm": 40,
        "uit": "pgm-zimplats-rustenburg-weg-beitbridge-rustenburg.geojson",
    },
    # Routebrief pgm-springs-zurich, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck PGM-erts/matte Impala Rustenburg-mijnencluster → Impala Springs
    # Refinery, N4 (Rustenburg-Centurion/Pretoria) → N1 (Pretoria-Johannesburg)
    # → N12 (Johannesburg-Germiston-Springs). Toetswaarde ~160 km (schatting uit
    # ketenontwerp, geen aparte bron — lengtetoets ±15%).
    "pgm-springs-zurich-rustenburg-springs": {
        "via": [
            ("Impala Rustenburg-mijnencluster (anker, pgm-rustenburg-mijn)", (27.2176, -25.5535)),
            ("Marikana (N4-corridor)", (27.4794, -25.7043)),
            ("Centurion (N4/N1-knoop, Pretoria)", (28.1894, -25.8603)),
            ("Johannesburg N1/N12-knoop", (28.0980, -26.0380)),
            ("Germiston (N12-corridor)", (28.1672, -26.2178)),
            ("Impala Refining Services, Springs (anker, pgm-springs-raffinaderij)", (28.4437, -26.2227)),
        ],
        "id": "pgm-springs-zurich-rustenburg-springs",
        "naam": "Impala Rustenburg-mijnencluster → Impala Springs Refinery (N4 → N1 → N12)",
        "extracts": ["zuid-afrika"],
        "refs": ["N4", "N1", "N12"],
        "gepubliceerdKm": 160,
        "bronnoot": "geen gepubliceerde km; ~160 km uit het ketenontwerp (routebrief pgm-springs-zurich §2), behandeld als schatting.",
        "vensterKm": 40,
        "uit": "pgm-springs-zurich-weg-rustenburg-springs.geojson",
    },
    # Routebrief pgm-springs-zurich, been b2 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck PGM (geraffineerd) Impala Springs Refinery → OR Tambo-vrachtterminal
    # (JNB), N12/N3 Springs–Johannesburg–Kempton Park. Toetswaarde ~40 km
    # (schatting uit ketenontwerp).
    "pgm-springs-zurich-springs-ortambo": {
        "via": [
            ("Impala Refining Services, Springs (anker, pgm-springs-raffinaderij)", (28.4437, -26.2227)),
            ("Boksburg (N12-corridor)", (28.2519, -26.2125)),
            ("Kempton Park (N3/R21-corridor)", (28.2321, -26.1020)),
            ("OR Tambo-vrachtterminal (anker, pgm-ortambo-vrachtterminal)", (28.2472, -26.1211)),
        ],
        "id": "pgm-springs-zurich-springs-ortambo",
        "naam": "Impala Springs Refinery → OR Tambo-vrachtterminal (N12 → N3/R21)",
        "extracts": ["zuid-afrika"],
        "refs": ["N12", "N3", "R21"],
        "gepubliceerdKm": 40,
        "bronnoot": "geen gepubliceerde km; ~40 km uit het ketenontwerp (routebrief pgm-springs-zurich §2), behandeld als schatting.",
        "vensterKm": 40,
        "uit": "pgm-springs-zurich-weg-springs-ortambo.geojson",
    },
    # Routebrief pgm-springs-zurich, been b4 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Zürich Airport vrachtplatform → edelmetaalkluis Kloten (Loomis
    # Schweiz, aannemelijk), binnenstedelijk Zürich-Kloten. Toetswaarde ~15 km
    # (schatting).
    "pgm-springs-zurich-zrh-kloten": {
        "via": [
            ("Zürich Airport vrachtplatform (anker, pgm-zrh-vrachtterminal)", (8.5492, 47.4647)),
            ("Edelmetaalkluis Loomis Schweiz, Kloten (anker, pgm-zurich-kluis, aannemelijk)", (8.6046, 47.4474)),
        ],
        "id": "pgm-springs-zurich-zrh-kloten",
        "naam": "Zürich Airport vrachtplatform → edelmetaalkluis Kloten (binnenstedelijk Zürich–Kloten)",
        "extracts": ["zwitserland"],
        "refs": [],
        "eindToegangPrivaat": True,
        "gepubliceerdKm": 15,
        "bronnoot": "geen gepubliceerde km; ~15 km schatting (routebrief pgm-springs-zurich §2/§7).",
        "vensterKm": 15,
        "uit": "pgm-springs-zurich-weg-zrh-kloten.geojson",
    },
    # Routebrief pgm-zondereinde-hanau, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Northam Zondereinde mijn/smelter/BMR → OR Tambo vrachtterminal (JNB),
    # R510 zuidwaarts → N4 oostwaarts → N1 zuidwaarts. Toetswaarde ~140 km
    # (ontwerp, niet apart gebrond).
    "pgm-zondereinde-hanau-zondereinde-ortambo": {
        "via": [
            ("Northam Zondereinde-complex (anker, pgm-zondereinde-mijnsmelter)", (27.3669, -24.8333)),
            ("Northam (dorp aan het R510-begin)", (27.2656, -24.9575)),
            ("Marikana (R510/N4-omgeving)", (27.4915, -25.6879)),
            ("Brits (N4)", (27.7842, -25.6297)),
            ("Pretoria (N4/N1-knoop)", (28.1881, -25.7461)),
            ("OR Tambo vrachtterminal (anker, pgm-ortambo-vracht)", (28.2330, -26.1290)),
        ],
        "id": "pgm-zondereinde-ortambo-weg",
        "naam": "Zondereinde mijn/smelter/BMR → OR Tambo vrachtterminal (R510 → N4 → N1)",
        "extracts": ["zuid-afrika"],
        "refs": ["R510", "N4", "N1"],
        "gepubliceerdKm": 140,
        "bronnoot": "geen gepubliceerde km; ~140 km uit het ketenontwerp, niet apart gebrond.",
        "vensterKm": 40,
        "uit": "pgm-zondereinde-hanau-weg-zondereinde-ortambo.geojson",
    },
    # Routebrief pgm-zondereinde-hanau, been b3 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Frankfurt vrachtterminal (Cargo City Süd) → Heraeus Precious Metals
    # Hanau, A66 Frankfurt–Hanau. Toetswaarde ~25 km (ontwerp).
    "pgm-zondereinde-hanau-frankfurt-hanau": {
        "via": [
            ("Frankfurt vrachtterminal (anker, pgm-frankfurt-vracht)", (8.5552, 50.0244)),
            ("Heraeus Precious Metals Hanau (anker, pgm-heraeus-hanau)", (8.9315, 50.1328)),
        ],
        "id": "pgm-frankfurt-hanau-weg",
        "naam": "Frankfurt vrachtterminal → Heraeus Hanau (A66)",
        "extracts": ["de-hessen"],
        "refs": ["A66"],
        "gepubliceerdKm": 25,
        "bronnoot": "geen gepubliceerde km; ~25 km uit het ketenontwerp, niet apart gebrond.",
        "vensterKm": 40,
        "eindToegangPrivaat": True,
        "uit": "pgm-zondereinde-hanau-weg-frankfurt-hanau.geojson",
    },
    # Routebrief diamant-mirny-mumbai, been b1 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck Alrosa Mirny-mijn/sorteercentrum → Mirny Airport (MJZ), stadsweg
    # binnen de Alrosa-bedrijfsstad Mirny, geen doorgaande corridorkeuze.
    # Toetswaarde ~2,2 km hemelsbreed uit de ankers (brief noemt indicatief
    # ~3 km wegafstand); geen refs (lokale stadswegen).
    "diamant-mirny-mumbai-mijn-mjz": {
        "via": [
            ("Alrosa Mir-mijn/sorteercentrum (anker, dia-mirny-mijn)", (113.9842, 62.5258)),
            ("Mirny Airport MJZ, vrachtterminal (anker, dia-mirny-mjz)", (114.0222, 62.5344)),
        ],
        "id": "dia-mirny-mjz-weg",
        "naam": "Mir-mijn/sorteercentrum → Mirny Airport (MJZ) (stadsweg Mirny)",
        "extracts": ["rusland-verrehoosten"],
        "refs": [],
        "gepubliceerdKm": 2.2,
        "bronnoot": "geen gepubliceerde km; ~2,2 km hemelsbreed uit de ankers, "
                    "ontwerp/brief noemt indicatief ~3 km wegafstand.",
        "vensterKm": 15,
        "uit": "diamant-mirny-mumbai-weg-mijn-mjz.geojson",
    },
    # Routebrief diamant-mirny-mumbai, been b4 (LICHTE werkwijze M31 golf 3, §2 Lucht).
    # Truck CSMIA Air Cargo Complex (BOM) → Bharat Diamond Bourse (BKC), Airport
    # Road → Western Express Highway/BKC-connector, binnen Mumbai, geen
    # corridorkeuze. Toetswaarde ~3,9 km hemelsbreed uit de ankers.
    "diamant-mirny-mumbai-bom-bdb": {
        "via": [
            ("CSMIA Air Cargo Complex, Sahar (anker, dia-bom-cargo)", (72.8673, 19.0994)),
            ("Bharat Diamond Bourse, BKC (anker, dia-bdb)", (72.8646, 19.0641)),
        ],
        "id": "dia-bdb-weg",
        "naam": "CSMIA Air Cargo Complex (BOM) → Bharat Diamond Bourse (Airport Road/BKC-connector)",
        "extracts": ["india"],
        "refs": [],
        "gepubliceerdKm": 3.9,
        "bronnoot": "geen gepubliceerde km; ~3,9 km hemelsbreed uit de ankers.",
        "vensterKm": 15,
        "uit": "diamant-mirny-mumbai-weg-bom-bdb.geojson",
    },
    # Routebrief pgm-stillwater-columbus, been b1 (LICHTE werkwijze M31 golf 3).
    # Truck PGM-erts (2E, Pd-dominant) Stillwater Mine (Sibanye-Stillwater, Nye,
    # Stillwater County) → Columbus Metallurgical Complex (smelter + base metal
    # refinery), over Nye Road/CR-419 (Stillwater River) → Absarokee → MT-78
    # noordwaarts naar Columbus. Toetswaarde 64 km (40 mi, Encyclopedia.com [7]);
    # ontwerp gaf indicatief ~50 km. Twee via-punten = eerlijk aan de geografie
    # (MT-78 is de enige verharde doorgaande corridor Absarokee→Columbus).
    "pgm-stillwater-columbus": {
        "via": [
            ("Stillwater Mine — concentrator/laadplek (anker, pgm-stillwater-laad)", (-109.8920, 45.3880)),
            ("Nye — mijnweg/Nye Road-knoop", (-109.8037, 45.4350)),
            ("Absarokee — aansluiting MT-78", (-109.4426, 45.5211)),
            ("Columbus Metallurgical Complex — smelter/refinery (anker, pgm-columbus-smelter)", (-109.2400, 45.6330)),
        ],
        "id": "pgm-stillwater-columbus",
        "naam": "Stillwater Mine → Nye → Absarokee (MT-78) → Columbus Metallurgical Complex",
        "extracts": ["us-montana"],
        "refs": ["MT-78"],
        "gepubliceerdKm": 64,
        "bronnoot": "40 miles (Encyclopedia.com [7]) tussen Stillwater Mine en Columbus-smelter; ontwerp gaf indicatief ~50 km — 64 km als toetswaarde.",
        "vensterKm": 40,
        "uit": "pgm-stillwater-columbus-weg-stillwater-columbus.geojson",
    },
    # Routebrief nikkel-sorowako-matsuzaka, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck nikkel-matte PT Vale Indonesia Sorowako-mijn/smelter (Danau Matano) →
    # rivierhaven Balantang bij Malili, over de Jalan Poros Malili-Soroako (OSM-
    # naam bevestigd). Geen gepubliceerde km — ~60 km indicatief (ketenontwerp,
    # brief §2 bron [2]); vensterKm ruim ivm bergterrein.
    "nikkel-sorowako-matsuzaka-sorowako-balantang": {
        "via": [
            ("PT Vale Indonesia — Sorowako-mijn/smelter (anker, ni-sorowako-plant)", (121.3575, -2.5203)),
            ("Asuli — junctie Jalan Poros Malili-Soroako", (121.3244, -2.5964)),
            ("Wasuponda", (121.2583, -2.5971)),
            ("Balambano — PT Vale-nederzetting", (121.2516, -2.6607)),
            ("Malili — doorgaande weg nabij centrum", (121.1163, -2.6191)),
            ("Pelabuhan Balantang — exportterminal (anker, ni-balantang-kade)", (121.0732, -2.6428)),
        ],
        "id": "ni-sorowako-balantang",
        "naam": "Sorowako-mijn/smelter → Asuli → Wasuponda → Balambano → Malili → Balantang-kade (Jalan Poros Malili-Soroako)",
        "extracts": ["indonesie"],
        "refs": ["Jalan Poros Malili - Soroako"],
        "gepubliceerdKm": 60,
        "bronnoot": "niet gepubliceerd; ~60 km indicatief (ketenontwerp M31 golf 2, "
                    "brief §2 bron [2]) — GEEN harde ±15%-toets ivm ontbrekende "
                    "operatorbron.",
        "vensterKm": 75,
        "uit": "nikkel-sorowako-matsuzaka-weg-sorowako-balantang.geojson",
    },
    # Routebrief grafiet-lindijumbo-qingdao, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck natuurlijk vlokgrafiet Lindi Jumbo-mijn (Ndovu Graphite Limited, bij
    # Matambarale/Ruangwa-district) → Dar es Salaam-containerkade: mijnweg →
    # Ruangwa → regionale weg Ruangwa-Nyangao-Lindi → T7 "Kilwa Road" (Lindi →
    # Nangurukuru → Kibiti → Mkuranga → Dar es Salaam). Geen gepubliceerde
    # totaallengte (brief §2/§7); eigen via-keten 477,9 km hemelsbreed. Venster
    # ruimer dan default (75 km) omdat de regionale weg Ruangwa-Lindi niet
    # gepubliceerd is.
    "grafiet-lindijumbo-qingdao-lindijumbo-daressalaam": {
        "via": [
            ("Lindi Jumbo-mijn (Ndovu Graphite Limited) — anker", (38.9160, -9.9135)),
            ("Ruangwa — wegsplitsing, aansluiting mijnweg op regionale weg", (38.9274, -10.0675)),
            ("Lindi — aansluiting regionale weg op T7", (39.7144, -9.9969)),
            ("Nangurukuru — T7-kruispunt, pint de kustweg", (39.3502, -8.7980)),
            ("Kibiti — T7, Rufiji-delta", (38.9365, -7.7214)),
            ("Mkuranga — laatste kruispunt vóór Dar es Salaam", (39.2115, -7.1199)),
            ("Dar es Salaam Port, general cargo-/containerkade (Kurasini-kanaal) — anker", (39.2870, -6.8280)),
        ],
        "id": "gr-lindijumbo-daressalaam",
        "naam": "Lindi Jumbo-mijn → Ruangwa → Lindi → Nangurukuru → Kibiti → Mkuranga → Dar es Salaam (T7 'Kilwa Road')",
        "extracts": ["tanzania"],
        "refs": ["T7"],
        "gepubliceerdKm": None,
        "bronnoot": "geen onafhankelijk gepubliceerde totaallengte — eigen via-puntenketen 477,9 km hemelsbreed (routebrief grafiet-lindijumbo-qingdao §2/§7)",
        "vensterKm": 75,
        "uit": "grafiet-lindijumbo-qingdao-weg-lindijumbo-daressalaam.geojson",
    },
    # Routebrief grafiet-itapecerica-vitoria, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck vlokgrafiet Nacional de Grafite Itapecerica-vestiging (Tejuco Preto-
    # mijn + concentratie, Minas Gerais) → Porto de Praia Mole-kade, Vitória
    # (Espírito Santo), over de BR-262-exportcorridor. Geen gepubliceerde km
    # (brief §2: ontwerpschatting ~570 km via-keten tegen hemelsbreed 510,5 km) —
    # ruimere venster/tolerantie omdat er alleen een corridor-redenering is,
    # geen bron voor de exacte route.
    "grafiet-itapecerica-vitoria-itapecerica-praiamole": {
        "via": [
            ("Nacional de Grafite Itapecerica — mijn/concentratie (kop, anker)", (-45.1300, -20.4420)),
            ("Nova Serrana — aansluiting lokale weg × BR-262", (-44.9842, -19.8758)),
            ("Belo Horizonte — BR-262 door de metropoolregio", (-43.4848, -19.9272)),
            ("São Domingos do Prata — BR-262, Rio Doce-regio", (-42.9658, -19.8671)),
            ("Manhuaçu — BR-262, grote kruising", (-42.0341, -20.2574)),
            ("Domingos Martins — BR-262, bergpas MG→ES", (-41.0591, -20.3733)),
            ("Viana — BR-262, nadering Vitória-metropool", (-40.4949, -20.3894)),
            ("Porto de Praia Mole — exportterminal (staart, anker)", (-40.2350, -20.28965)),
        ],
        "id": "gr-itapecerica-praiamole",
        "naam": "Itapecerica-vestiging → Porto de Praia Mole (BR-262)",
        "extracts": ["brazilie"],
        "refs": ["BR-262"],
        "gepubliceerdKm": 570,
        "bronnoot": "geen gepubliceerde km — ontwerpschatting (som via-keten) tegen hemelsbreed 510,5 km, routebrief grafiet-itapecerica-vitoria §2/§7",
        "vensterKm": 75,
        "uit": "grafiet-itapecerica-vitoria-weg-itapecerica-praiamole.geojson",
    },
    # Routebrief grafiet-skaland-lulea, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck vlokgrafiet Skaland Grafitverk-mijn/plant (Senja) → dorpskade Skaland
    # (Bergsfjorden), lokale dorpsweg, ~0,7 km eigen meting op satelliet, niet
    # gepubliceerd. Geen corridorkeuze (kort eigen terrein/dorpspad) dus geen
    # via-punten.
    "grafiet-skaland-lulea-skaland-mijn-skaland-kade": {
        "via": [
            ("Skaland Grafitverk — mijn/verwerkingsplant (kop, anker)", (17.3279, 69.4462)),
            ("Skaland fiskerihavn — dorpskade (staart, anker)", (17.3125, 69.4428)),
        ],
        "id": "gr-skaland-mijn-kade",
        "naam": "Skaland-mijn → Skaland-dorpskade (lokale dorpsweg)",
        "extracts": ["noorwegen"],
        "refs": [],
        "gepubliceerdKm": 0.7,
        "bronnoot": "eigen meting op satelliet, niet gepubliceerd — routebrief grafiet-skaland-lulea §2",
        "vensterKm": 10,
        "uit": "grafiet-skaland-lulea-weg-skaland-mijn-skaland-kade.geojson",
    },
    # Routebrief koper-olympicdam-portadelaide, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck koperkathode (+U/Au/Ag) Olympic Dam-mijn/smelter/raffinaderij (BHP) →
    # Aurizon-terminal Pimba, over de Olympic Dam Highway (brief §2/§8[1]) —
    # rechte weg door dunbevolkt gebied, geen corridorkeuze dus geen via-punten.
    "koper-olympicdam-portadelaide-olympicdam-pimba": {
        "via": [
            ("Olympic Dam mining/metallurgical complex (BHP, Roxby Downs) — anker", (136.8731, -30.4400)),
            ("Aurizon intermodale terminal, Pimba — anker", (136.7997, -31.2551)),
        ],
        "id": "cu-olympicdam-pimba",
        "naam": "Olympic Dam-mijn → Pimba-terminal (Olympic Dam Highway)",
        "extracts": ["australie"],
        "refs": ["B97"],
        "gepubliceerdKm": 92,
        "bronnoot": "Wikipedia, 'Olympic Dam Highway' — sealed 92 km, Stuart Highway (Pimba) → Olympic Dam — brief §8[1]",
        "vensterKm": 40,
        "eindToegangPrivaat": True,
        "uit": "koper-olympicdam-portadelaide-weg-olympicdam-pimba.geojson",
    },
    # Routebrief koper-sentinel-walvisbay, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck sulfide-concentraat Sentinel-mijn (Kalumbila, First Quantum) → grens
    # Katima Mulilo/Sesheke: Solwezi-uitvalsweg → Mutanda → Kasempa → Kaoma →
    # Mongu → Senanga → Sesheke → grensbrug (WCL-tracé, brief §2/§4). Venster
    # ruim (75 km) want Solwezi–Mutanda (~45 km) is een kaartschatting, geen bron.
    "koper-sentinel-walvisbay-sentinel-katimamulilo": {
        "via": [
            ("Sentinel-mijn (Kalumbila, First Quantum) — anker", (25.3025, -12.2600)),
            ("Solwezi — provinciehoofdstad, regionale wegknoop", (26.3858, -12.1833)),
            ("Mutanda — start WCL-upgradetracé", (26.2400, -12.4000)),
            ("Kasempa — op het WCL-tracé", (25.8350, -13.4550)),
            ("Kaoma — WCL-tracé, splitst van de noordroute af", (24.8000, -14.8000)),
            ("Mongu — M10 doorgaande weg (Wikipedia-centroïde 294 m ernaast landde op een geïsoleerde straatjesstomp)", (23.1344278, -15.2764746)),
            ("Senanga — laatste plaats vóór de Zambezi-vlakte", (23.2667, -16.1167)),
            ("Sesheke — Zambiaanse grensstad", (24.3000, -17.4667)),
            ("Grensovergang Katima Mulilo-brug (Zambezi) — anker", (24.2499, -17.4717)),
        ],
        "id": "cu-sentinel-katimamulilo",
        "naam": "Sentinel-mijn → Solwezi → Mutanda → Kasempa → Kaoma → Mongu → Senanga → Sesheke → grens Katima Mulilo",
        "extracts": ["zambia"],
        "refs": [],
        "gepubliceerdKm": 566,
        "bronnoot": "Sentinel–Solwezi 150 km gepubliceerd [1]; Mutanda–grens 371 km officieel (WCL) [3][4]; Solwezi–Mutanda ~45 km geschat — brief §2",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "koper-sentinel-walvisbay-weg-sentinel-katimamulilo.geojson",
    },
    # Routebrief koper-sentinel-walvisbay, been b2 (LICHTE werkwijze M31 golf 2).
    # Truck concentraat grens Katima Mulilo/Sesheke → Walvis Bay-kade: B8
    # (Katima Mulilo–Rundu–Otavi) → B1 (Otavi–Otjiwarongo–Karibib) → B2
    # (Karibib–Walvis Bay) — de Trans-Caprivi-corridor (brief §2/§4).
    "koper-sentinel-walvisbay-katimamulilo-walvisbay": {
        "via": [
            ("Grensovergang Katima Mulilo-brug (Zambezi) — anker", (24.2499, -17.4717)),
            ("Rundu — eerste grote Namibische stad op de B8", (19.7670, -17.9170)),
            ("Otavi — wisselpunt B8 → B1", (17.3306, -19.6642)),
            ("Otjiwarongo — vaste tussenstop op de B1", (16.6528, -20.4642)),
            ("Karibib — wisselpunt B1 → B2", (15.8544, -21.9381)),
            ("Walvis Bay-containerterminal — anker", (14.4860, -22.9500)),
        ],
        "id": "cu-katimamulilo-walvisbay",
        "naam": "Grens Katima Mulilo → Rundu → Otavi → Otjiwarongo → Karibib → Walvis Bay (B8 → B1 → B2)",
        "extracts": ["namibie"],
        "refs": ["B8", "B1", "B2"],
        "gepubliceerdKm": 1470,
        "bronnoot": "opgeteld uit Wikipedia-routebeschrijving (Katima Mulilo–Rundu 510 + Rundu–Otavi–Karibib–Walvis Bay ~960), niet stapsgewijs officieel — brief §2/§7",
        "vensterKm": 40,
        "uit": "koper-sentinel-walvisbay-weg-katimamulilo-walvisbay.geojson",
    },
    # Routebrief ree-longnan-ganzhou, been b1 (LICHTE werkwijze M31 golf 2). Truck
    # ionenklei-uitloogconcentraat uitloogput bij Guanxi (关西镇) → Longnan-
    # scheidingsfabriek: county-weg vanaf de put → provinciale weg S225 door
    # Longnan-stad naar de ontwikkelingszone. Geen gepubliceerde km (brief §7) —
    # hemelsbreed 15,5 km, aannemelijk ~20 km over de weg. Venster ruim
    # (bergterrein); het laatste stuk bij de put kan buiten tertiary/
    # unclassified vallen (mogelijk alleen track) → corridorKlassen/eindKlassen
    # verruimd zodat de scan het zelf toetst i.p.v. te falen.
    "ree-longnan-ganzhou-uitloogput-scheiding": {
        "via": [
            ("Longnan-uitloogput, Zudong-district (bij Guanxi 关西镇) — anker", (114.9660, 24.8685)),
            ("Guanxi-stad (关西镇) — county-weg → weg naar Longnan-stad", (114.9431, 24.8420)),
            ("赣州稀土（龙南）有色金属有限公司 — Longnan-scheidingsfabriek — anker", (114.81439, 24.84829)),
        ],
        "id": "ree-longnan-uitloogput-scheiding",
        "naam": "Longnan-uitloogput → Guanxi-stad → Longnan-scheidingsfabriek (county-weg → S225)",
        "extracts": ["china"],
        "refs": ["S225"],
        "gepubliceerdKm": None,
        "bronnoot": "geen publicatie; hemelsbreed 15,5 km, aannemelijk ~20 km over de weg (brief §7)",
        "vensterKm": 30,
        "corridorKlassen": ["tertiary", "unclassified"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "uit": "ree-longnan-ganzhou-weg-uitloogput-scheiding.geojson",
    },
    # Routebrief ree-longnan-ganzhou, been b2 (LICHTE werkwijze M31 golf 2). Truck
    # RE-oxiden Longnan-scheidingsfabriek → JL MAG Rare-Earth magneetfabriek,
    # Ganzhou: G106 / Longnan–Ganzhou-expressway (S32) via Xinfeng (信丰). Geen
    # gepubliceerde km (brief §7) — hemelsbreed 110,5 km, aannemelijk ~130-160 km
    # (ketenontwerp noemde ongebrond 180-220 km). Venster ruim voor bergpassen;
    # corridorKlassen laat ook tertiary/unclassified toe als de expressway-scan
    # geen volledige verbinding vindt.
    "ree-longnan-ganzhou-scheiding-ganzhou": {
        "via": [
            ("赣州稀土（龙南）有色金属有限公司 — Longnan-scheidingsfabriek — anker", (114.81439, 24.84829)),
            ("Xinfeng-stad (信丰) — pint de noordelijke Longnan–Ganzhou-corridor", (114.9721, 25.2784)),
            ("JL MAG Rare-Earth, Ganzhou (hergebruikt anker w-jlmag-ganzhou) — anker", (114.8663, 25.8406)),
        ],
        "id": "ree-longnan-ganzhou-jlmag",
        "naam": "Longnan-scheidingsfabriek → Xinfeng → JL MAG Ganzhou (G106/S32 Longnan–Ganzhou-expressway)",
        "extracts": ["china"],
        "refs": ["G106", "S32"],
        "gepubliceerdKm": None,
        "bronnoot": "geen publicatie; hemelsbreed 110,5 km, aannemelijk ~130-160 km — ketenontwerp noemde ongebrond 180-220 km (brief §7)",
        "vensterKm": 50,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "ree-longnan-ganzhou-weg-scheiding-ganzhou.geojson",
    },
    # Routebrief uranium-olympicdam-portadelaide, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck uraanoxideconcentraat (yellowcake) Olympic Dam-fabriek (BHP, Roxby
    # Downs) → Port Adelaide, Outer Harbor: Stuart Highway (Roxby Downs–Pimba–
    # Port Augusta) → Augusta Highway/Princes Highway (Port Augusta–Adelaide) —
    # enige verharde doorgaande route, geen alternatieve corridor. Geen
    # gepubliceerde km voor dit specifieke traject (brief §7) — ~700 km is een
    # webcheck-schatting (grootcirkel ~560 km × wegfactor), geen citaat-bron.
    "uranium-olympicdam-portadelaide": {
        "via": [
            ("Olympic Dam Operations (BHP, Roxby Downs) — anker", (136.8731, -30.4400)),
            ("Pimba — kruising Olympic Dam Highway × Stuart Highway", (136.8264, -31.1756)),
            ("Port Augusta — kruising Stuart Highway × Augusta Highway", (137.7663, -32.4925)),
            ("Port Wakefield — overgang Augusta Highway → Princes Highway/Port Wakefield Road", (138.1497, -34.1936)),
            ("Outer Harbor, Port of Adelaide — anker", (138.4920, -34.7694)),
        ],
        "id": "u-olympicdam-portadelaide",
        "naam": "Olympic Dam → Pimba → Port Augusta → Port Wakefield → Port Adelaide, Outer Harbor (Stuart Hwy → Augusta/Princes Hwy)",
        "extracts": ["australie"],
        "refs": ["A87", "A1", "B97"],
        "gepubliceerdKm": 700,
        "bronnoot": "webcheck-schatting (grootcirkel ~560 km × wegfactor), geen citaat-bron — brief §7; de ±15%-toets is zwak want de referentiewaarde zelf is zwak",
        "vensterKm": 40,
        "corridorKlassen": ["tertiary", "unclassified"],
        "eindToegangPrivaat": True,
        "uit": "uranium-olympicdam-portadelaide-weg-olympicdam-portadelaide.geojson",
    },
    # Routebrief zilver-cannington-townsville, been b1 (LICHTE werkwijze M31 golf 2).
    # Roadtrain (Linfox, 24/7) lood/zilverconcentraat Cannington-mill → Yurbi
    # rail-overslag: mijnweg → McKinlay (aansluiting op de Landsborough Highway,
    # Wikipedia) → weer noordwestwaarts via Cloncurry → laatste ~15 km oostwaarts
    # naar Yurbi. GEEN monotone lijn: de route gaat eerst naar McKinlay (noordoost)
    # en dan terug naar Cloncurry (noordwest) — venster ruim (55 km) zodat de knik
    # bij McKinlay niet als omweg/lus wordt afgekeurd. Gepubliceerd: 180 km
    # (Industry Queensland + Qld-ministerieel statement, brief §2/§8[1][2]).
    "zilver-cannington-townsville-mill-yurbi": {
        "via": [
            ("Cannington-mill (South32) — anker", (140.9155, -21.8595)),
            ("McKinlay (aansluiting mijnweg → Landsborough Highway)", (141.2902, -21.2713)),
            ("Cloncurry (Landsborough Highway passeert de stad)", (140.5053, -20.7047)),
            ("Yurbi rail-overslagfacility — anker", (140.6557, -20.7389)),
        ],
        "id": "ag-cannington-yurbi",
        "naam": "Cannington-mill → McKinlay → Cloncurry → Yurbi-overslag (roadtrain-route, 24/7)",
        "extracts": ["australie"],
        "refs": [],
        "gepubliceerdKm": 180,
        "bronnoot": "Industry Queensland 'Road trip with a difference' + Qld-ministerieel statement 1026 (brief §8[1][2])",
        "vensterKm": 55,
        # ⚠️ Eerste poging (WEG_HOUD kaal) + tweede poging (corridorKlassen
        # tertiary/unclassified) faalden allebei op "geen wegpad tussen punt 2
        # en 3" (Cloncurry → Yurbi-overslag, ~15 km) — dit is een bemande,
        # dagelijkse 24/7-roadtrainroute (Linfox), dus een verhard/berijdbaar
        # tracé is aannemelijk; de Yurbi-toegangsweg zelf is vermoedelijk
        # smaller (service/track) dan de standaard-eindzone dekt.
        "corridorKlassen": ["tertiary", "unclassified"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "eindToegangPrivaat": True,
        "uit": "zilver-cannington-townsville-weg-mill-yurbi.geojson",
    },
    # Routebrief uranium-porthope-almelo, been b3 (LICHTE werkwijze M31 golf 2).
    # Truck UF6/LEU Rotterdam RHB → Urenco Almelo-verrijkingsfabriek: A20 → A12
    # (Knp. Gouwe) → A27 (Knp. Lunetten) → A28 (Knp. Rijnsweerd) → A1 (Knp.
    # Hoevelaken) → A35 (Knp. Buren) → N349/Bornsestraat. Gepubliceerd: OSRM-
    # webcheck 188,8 km (brief §2/§8[8]); het ketenontwerp noemde ~150 km — de
    # kortste route schakelt via A27/A28 om Utrecht/Amersfoort i.p.v.
    # rechtstreeks A12→A1 (bekend open punt, niet dichtgetrokken).
    "uranium-porthope-almelo-rotterdam-almelo": {
        "via": [
            ("Rotterdam RHB Stevedoring & Warehousing — anker", (4.4585, 51.8935)),
            ("Knooppunt Gouwe (A20 × A12)", (4.6542, 52.0222)),
            ("Knooppunt Lunetten (A12 × A27)", (5.1444, 52.0550)),
            ("Knooppunt Rijnsweerd (A27 × A28)", (5.1611, 52.0919)),
            ("Knooppunt Hoevelaken (A28 × A1)", (5.4276, 52.1756)),
            ("Knooppunt Buren (A1 × A35)", (6.7432, 52.2855)),
            ("Urenco Almelo-verrijkingsfabriek — anker", (6.6922, 52.3391)),
        ],
        "id": "u-rotterdam-almelo",
        "naam": "Rotterdam RHB → Knp. Gouwe → Knp. Lunetten → Knp. Rijnsweerd → Knp. Hoevelaken → Knp. Buren → Urenco Almelo (A20/A12/A27/A28/A1/A35)",
        "extracts": ["nederland"],
        "refs": ["A20", "A12", "A27", "A28", "A1", "A35"],
        "gepubliceerdKm": 189,
        "bronnoot": "OSRM-webcheck (publieke demo-router), 188,8 km; ontwerp noemde ~150 km — bekend open punt, niet dichtgetrokken (brief §7)",
        "vensterKm": 40,
        "uit": "uranium-porthope-almelo-weg-rotterdam-almelo.geojson",
    },
    # Routebrief kobalt-huayou-gunsan, been b1 (LICHTE werkwijze M31 golf 2). Truck
    # kobalttetroxide/-sulfaat Huayou Tongxiang-raffinaderij → Ningbo Beilun-kade:
    # G60/G92 Tongxiang–Ningbo (Hangzhou-ringweg-corridor). Geen gepubliceerd exact
    # tracé (brief §7/8[2][3]) — alleen ~150 km ontwerp-webcheck; geen via-punten
    # (Wikipedia/Nominatim/Photon rate-limited deze sessie, brief §7) — de wegscan
    # levert zelf corridorpunten op via het china-extract.
    "kobalt-huayou-gunsan-tongxiang-ningbo": {
        "via": [
            ("Huayou Tongxiang-raffinaderij — anker", (120.5629, 30.6167)),
            ("Ningbo Beilun-containerkade — anker", (121.8695, 29.9353)),
        ],
        "id": "co-tongxiang-ningbo",
        "naam": "Huayou Tongxiang-raffinaderij → Ningbo Beilun-kade (G60/G92 Tongxiang–Ningbo)",
        "extracts": ["china"],
        "refs": ["G60", "G92"],
        "gepubliceerdKm": 150,
        "bronnoot": "ontwerp-webcheck, niet onafhankelijk geverifieerd; hemelsbreed 146,6 km",
        "vensterKm": 40,
        "uit": "kobalt-huayou-gunsan-weg-tongxiang-ningbo.geojson",
    },
    # Routebrief zilver-penasquito-onsan, been b1 (LICHTE werkwijze M31 golf 2). Truck
    # Zn/Pb-concentraat (met meegesleept zilver) Peñasquito-mijn → Manzanillo-terminal:
    # Fed 54D/200D-corridor via Fresnillo → Zacatecas → Guadalajara → Colima. Geen
    # gepubliceerd exact tracé (brief §7[3]) — Wood Mackenzie noemt alleen de afstand
    # (~800 km, webcheck); groot venster i.v.m. de lange afstand.
    "zilver-penasquito-onsan-mijn-manzanillo": {
        "via": [
            ("Peñasquito-mijn (Newmont) — anker", (-101.6982, 24.6377)),
            ("Fresnillo", (-102.8675, 23.1750)),
            ("Zacatecas (stad)", (-102.5736, 22.7736)),
            ("Guadalajara", (-103.3475, 20.6767)),
            ("Colima (stad)", (-103.7247, 19.2433)),
            ("Manzanillo-terminal (TIMSA/OCUPA-zone) — anker", (-104.2975, 19.0810)),
        ],
        "id": "ag-penasquito-manzanillo",
        "naam": "Peñasquito-mijn → Fresnillo → Zacatecas → Guadalajara → Colima → Manzanillo-terminal (Fed 54D/200D)",
        "extracts": ["mexico"],
        "refs": ["54D", "200D"],
        "gepubliceerdKm": 800,
        "bronnoot": "Wood Mackenzie webcheck, geen exact tracé (brief §7[3]); via-punten hemelsbreed 729 km",
        "vensterKm": 65,
        "uit": "zilver-penasquito-onsan-weg-mijn-manzanillo.geojson",
    },
    # Routebrief kobalt-bouazzer-guemassa, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck kobalterts/concentraat CTT Bou Azzer-mijn → CTT Guemassa-complex: N9
    # Ouarzazate-Marrakech (Tizi n'Tichka-pas) → binnenstedelijk Marrakech als
    # "Avenue Guemassa" → terrein. Geen gepubliceerde wegkm (brief §7/§8[8]) —
    # alleen het gemeten getal geldt, geen ±15%-referentie.
    # ⚠️ via4 (Marrakech-zuid/Avenue Guemassa, lat 31.5791) ligt noordelijker dan
    #    de eindbestemming (lat 31.3825) — de weg buigt na Marrakech weer
    #    zuidwaarts naar Guemassa.
    "kobalt-bouazzer-guemassa-bouazzer-guemassa": {
        "via": [
            ("Mine Bou Azzer (CTT, Managem) — anker", (-6.9134, 30.5184)),
            ("Ouarzazate — aansluiting mijnweg op de N9", (-6.9170, 30.9170)),
            ("Tizi n'Tichka-pas (2.260 m, Hoge Atlas)", (-7.3808, 31.2858)),
            ("Aït Ourir — N9 tussen pas en Marrakech", (-7.6628, 31.5644)),
            ("Marrakech-zuid, N8/Avenue Guemassa-aftakking", (-8.0583, 31.5791)),
            ("CTT Guemassa-complex (Managem) — anker", (-8.0635, 31.3825)),
        ],
        "id": "co-bouazzer-guemassa",
        "naam": "Bou Azzer-mijn → Ouarzazate → Tizi n'Tichka-pas → Aït Ourir → Marrakech-zuid → Guemassa-complex (N9/N8)",
        "extracts": ["marokko"],
        "refs": ["N9", "N8"],
        "gepubliceerdKm": None,
        "bronnoot": "geen gepubliceerde wegkilometers gevonden voor N9/R203 Ouarzazate-Marrakech "
                    "(brief §7[8]); ontwerpschatting ~280 km, geen referentiewaarde voor de ±15%-toets",
        "vensterKm": 40,
        "uit": "kobalt-bouazzer-guemassa-weg-bouazzer-guemassa.geojson",
    },
    # Routebrief ree-kuantan-japan, been b1 (LICHTE werkwijze M31 golf 2). Truck
    # NdPr-/Dy-/Tb-oxide LAMP Gebeng → Westport (Pulau Indah, Port Klang): Gebeng-
    # industrieweg → Lebuhraya Pantai Timur (E8) → Karak Highway (E8/E9) → KL–
    # Klang-corridor (KESAS/Federal Highway). Geen gepubliceerde km (brief §7,
    # Time.com noemt alleen de route zelf); ~290 km ontwerpschatting, vensterKm
    # ruim omdat de brief-km zelf al een schatting is.
    "ree-kuantan-japan-gebeng-westport": {
        "via": [
            ("Lynas Advanced Materials Plant (LAMP), Gebeng — anker (hergebruikt uit ree-mtweld-kuantan)", (103.3775, 4.0034)),
            ("Kuantan (aansluiting Gebeng-industrieweg → Lebuhraya Pantai Timur E8)", (103.3333, 3.8167)),
            ("Bentong (Karak Highway-interchange, richting Kuala Lumpur)", (101.9167, 3.5167)),
            ("Genting Sempah (bergpas/tunnel door de Titiwangsa-bergketen)", (101.7806, 3.3497)),
            ("Gombak-tolplein (einde Karak Highway, aansluiting KL-ringweg)", (101.7272, 3.2420)),
            ("Shah Alam (KESAS/Federal Highway richting Port Klang)", (101.5167, 3.0722)),
            ("Pulau Indah (oprit naar het Westport-schiereiland)", (101.3317, 2.9489)),
            ("Westports Malaysia, Pulau Indah — anker", (101.3076, 2.9498)),
        ],
        "id": "ree-kuantan-japan-westport-kade",
        "naam": "LAMP Gebeng → Westport (Lebuhraya Pantai Timur E8 → Karak Highway E8/E9 → KL–Klang-corridor)",
        "extracts": ["maleisie"],
        "refs": ["E8", "E9"],
        "gepubliceerdKm": 290,
        "bronnoot": "geen gepubliceerde kilometrage (brief §7, alleen Time.com noemt de route zelf); "
                    "~290 km kaartschatting op de beschreven corridor",
        "vensterKm": 70,
        "uit": "ree-kuantan-japan-weg-gebeng-westport.geojson",
    },
    # Routebrief lithium-hombremuerto-bessemercity, been b1 (LICHTE werkwijze M31
    # golf 2). Truck carbonaat Fénix-plant (Salar del Hombre Muerto) → grens
    # Paso de San Francisco: RN-43/provinciale hooggebergteweg via Antofagasta
    # de la Sierra en El Peñón. Ontwerpschatting 150-200 km (brief §2, niet
    # gepubliceerd op wegniveau).
    # ⚠️ Hooggebergte-secundaire wegen, zelfde risico als lithium-olaroz-naraha
    #    RN52 → corridorKlassen laat tertiary/unclassified toe, venster ruim
    #    (75 km) voor de Puna-omweg.
    "lithium-hombremuerto-bessemercity-hombremuerto-elpenon": {
        "via": [
            ("Fénix-plant (Arcadium Lithium/Rio Tinto), Salar del Hombre Muerto — anker", (-67.1415, -25.3508)),
            ("Antofagasta de la Sierra (aansluiting RN-40/RN-43)", (-67.4066, -26.0592)),
            ("El Peñón (laatste plaats vóór de grensklim) — anker (net eindigt hier)", (-67.2653, -26.4754)),
        ],
        "id": "li-hombremuerto-elpenon",
        "naam": "Fénix-plant → El Peñón (RN-43 via Antofagasta de la Sierra)",
        "extracts": ["argentina", "chili"],
        "refs": ["RN43", "43", "RN40", "40"],
        "gepubliceerdKm": 175,
        "bronnoot": "ontwerpschatting 150-200 km voor het hele been plant→grens (midden 175); "
                    "El Peñón→grens heeft geen doorlopende OSM-weg (zie stippel in de bake)",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "uit": "lithium-hombremuerto-bessemercity-weg-hombremuerto-elpenon.geojson",
    },
    # Routebrief lithium-hombremuerto-bessemercity, been b2 (LICHTE werkwijze M31
    # golf 2). Truck carbonaat grens Paso de San Francisco → Puerto Antofagasta
    # (ATI-kade, gedeeld anker): Ruta 31/Ruta 23 via Diego de Almagro en
    # Chañaral naar Ruta 5 noordwaarts. Ontwerpschatting 475-525 km (midden
    # 500); b1+b2 samen ≈675 km tegen Arcadium/Livent's eigen "675 km driving
    # distance via Route 5" (brief bron [1]).
    # ⚠️ NIEUW PROFIEL, GEEN HERGEBRUIK: Ruta 5 hier is de noordwaartse
    #    kustcorridor vanuit het zuiden — anders dan de bestaande
    #    lithium-atacama-antofagasta-profielen die van Baquedano/oosten komen.
    "lithium-hombremuerto-bessemercity-grens-antofagasta": {
        "via": [
            ("grens Paso de San Francisco — anker", (-68.3014, -26.8764)),
            ("Diego de Almagro (aansluiting op Ruta 5)", (-70.0459, -26.3911)),
            ("Chañaral (Ruta 5 kustcorridor)", (-70.6224, -26.3479)),
            ("Puerto Antofagasta, ATI-kade — anker (gedeeld met lithium-atacama-antofagasta)", (-70.4088, -23.6500)),
        ],
        "id": "li-grens-antofagasta",
        "naam": "grens Paso de San Francisco → Puerto Antofagasta (Ruta 31/23 via Diego de Almagro/Chañaral → Ruta 5 noordwaarts)",
        "extracts": ["chili"],
        "refs": ["Ruta 31", "31", "Ruta 23", "23", "Ruta 5", "5", "CH-5"],
        "gepubliceerdKm": 500,
        "bronnoot": "ontwerpschatting 475-525 km (midden 500); b1+b2 samen ≈675 km tegen "
                    "Arcadium/Livent's eigen 'driving distance via Route 5' van 675 km (brief bron [1])",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "lithium-hombremuerto-bessemercity-weg-grens-antofagasta.geojson",
    },
    # Routebrief lithium-hombremuerto-bessemercity, been b4 (LICHTE werkwijze M31
    # golf 2). Truck (containers) Charleston (Hugh K. Leatherman Terminal) →
    # Arcadium Bessemer City-fabriek: I-26 westwaarts via Columbia en
    # Spartanburg → I-85 noordwaarts via Gastonia. Kruist twee extracts
    # (SC → NC). Ontwerpschatting 530-560 km (midden 545).
    "lithium-hombremuerto-bessemercity-charleston-bessemer": {
        "via": [
            ("Hugh K. Leatherman Terminal, Charleston — anker", (-79.9352, 32.8392)),
            ("Columbia, SC (I-26 richting NW)", (-81.0352, 34.0008)),
            ("Spartanburg, SC (I-26 → I-85)", (-81.9320, 34.9498)),
            ("Gastonia, NC (I-85 → laatste stuk naar Bessemer City)", (-81.1838, 35.2623)),
            ("Arcadium Lithium Bessemer City — anker", (-81.3060, 35.2795)),
        ],
        "id": "li-charleston-bessemer",
        "naam": "Charleston (Hugh K. Leatherman Terminal) → Bessemer City (I-26 via Columbia/Spartanburg → I-85 via Gastonia)",
        "extracts": ["us-south-carolina", "us-north-carolina"],
        "refs": ["I-26", "26", "I-85", "85"],
        "gepubliceerdKm": 545,
        "bronnoot": "ontwerpschatting 530-560 km (midden 545), niet gepubliceerd op wegniveau",
        "vensterKm": 40,
        "uit": "lithium-hombremuerto-bessemercity-weg-charleston-bessemer.geojson",
    },
    # Routebrief lithium-cirilo-vitoria, been b1 (LICHTE werkwijze M31 golf 2).
    # ⚠️ Stroom-id is lithium-cirilo-vitoria, NIET lithium-cirilo-ilheus: de brief
    # §7 (haalbaarheidstoets, bindend) stelt vast dat Sigma Lithium 100% per truck
    # naar Vitória (Espírito Santo) vervoert — geen spoorcorridor via FCA/VLI naar
    # Porto Sul/Ilhéus (Bahia). Dat was alleen het destijds GEPLANDE exportkanaal in
    # het NI 43-101-technisch rapport, niet het uitgevoerde tracé.
    # Truck spodumeenconcentraat Grota do Cirilo (Sigma Lithium, Araçuaí, MG) → BR-367
    # → Itaobim → BR-116 → Governador Valadares → BR-259 → Colatina → João Neiva →
    # BR-101 → Porto de Vitória. Geen gepubliceerd truck-km: ontwerpschatting
    # ~650-700 km (via-keten hemelsbreed 558,6 km × 1,15-1,25 routefactor) — venster-
    # indicatie, geen harde ±15%-toets zonder gepubliceerd cijfer (bevinding in §9).
    "lithium-cirilo-vitoria-plant-kade": {
        "via": [
            ("Grota do Cirilo — DMS/flotatie-complex (Sigma Lithium)", (-41.8878, -16.7328)),   # anker
            ("Itaobim, BR-367 × BR-116",                                (-41.5025, -16.5619)),
            ("Governador Valadares, BR-116 × BR-259",                   (-41.9439, -18.8574)),
            ("Colatina, BR-259 (ES)",                                   (-40.7193, -19.4720)),
            ("João Neiva, BR-259 × BR-101",                             (-40.4338, -19.7272)),
            ("Porto de Vitória — Vila Rubim/Cais Comercial",            (-40.3477, -20.3238)),   # anker
        ],
        "id": "li-cirilo-vitoria-plant-kade",
        "naam": "Grota do Cirilo → Itaobim → Gov. Valadares → Colatina → João Neiva → Porto de Vitória (BR-367 → BR-116 → BR-259 → BR-101)",
        "extracts": ["brazilie"],
        "refs": ["BR-367", "BR-116", "BR-259", "BR-101"],
        "gepubliceerdKm": 675, "bronnoot": "geen harde bron — ontwerpschatting 650-700 km (via-keten hemelsbreed 558,6 km); venster, geen ±15%-toets afdwingen",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary"],
        "uit": "lithium-cirilo-vitoria-weg-plant-kade.geojson",
    },
    # Routebrief lithium-silverpeak-mccarran, been b1 (LICHTE werkwijze M31 golf 2).
    # Truck lithiumcarbonaat Albemarle Silver Peak-brineoperatie (Clayton
    # Valley) → NV-265 → US-95 N (Tonopah–Mina–Hawthorne–Schurz) → US-95A
    # (Silver Springs–Fernley) → I-80 W → Tesla Gigafactory Nevada (TRIC).
    # Enige been van de keten; geen zee/spoor/leiding/binnenvaart. Geen
    # gepubliceerde weg-km: ontwerpschatting 300-330 km (gebruikt als 315),
    # eigen hemelsbreed-som over de zes via-punten 330,8 km (brief §8).
    # ⚠️ Silver Peak zelf hangt aan NV-265, een tweebaans landelijke
    #    staatsweg; bij Tonopah/Mina/Hawthorne/Schurz loopt de route recht
    #    door de plaatsen (geen omleiding nodig — dit zijn de doorgaande
    #    wegen zelf) → corridorKlassen laat tertiary/unclassified toe.
    # ⚠️ eindKlassen verruimd met track/residential/service — de laatste
    #    ~1-2 km naar de brine-operatie kan een unclassified/track-
    #    toegangsweg zijn (patroon van lithium-olaroz-naraha/-bougouni-yangpu).
    "lithium-silverpeak-mccarran-silverpeak-gigafactory": {
        "via": [
            ("Albemarle Silver Peak — brineoperatie (laadplek, anker)", (-117.5768, 37.7693)),
            ("Tonopah (junctie US-6/US-95)", (-117.2251, 38.1001)),
            ("Mina (junctie US-95/SR-359)", (-118.1087, 38.3905)),
            ("Hawthorne (US-95 langs Walker Lake)", (-118.6270, 38.5254)),
            ("Schurz (splitsing US-95 → US-95A)", (-118.8385, 38.9762)),
            ("Silver Springs (junctie US-95A/US-50 ALT)", (-119.2267, 39.3736)),
            ("Fernley (junctie met I-80)", (-119.2506, 39.6079)),
            ("Tesla Gigafactory Nevada — TRIC (losplek, anker)", (-119.4390524, 39.5403926)),
        ],
        "id": "li-silverpeak-gigafactory",
        "naam": "Albemarle Silver Peak → Tesla Gigafactory Nevada (NV-265 → "
                "US-95 N → US-95A → I-80 W)",
        "extracts": ["us-nevada"],
        "refs": ["US 95", "US 95A", "I 80", "NV 265"],
        "gepubliceerdKm": 315,
        "bronnoot": "niet gepubliceerd; ontwerpschatting 300-330 km, gebruikt "
                    "als middenwaarde 315; eigen hemelsbreed-som over de "
                    "zes via-punten 330,8 km (brief §8)",
        "vensterKm": 40,
        "corridorKlassen": ["tertiary", "unclassified"],
        "eindKlassen": ["residential", "service", "tertiary", "unclassified", "track"],
        "uit": "lithium-silverpeak-mccarran-weg-silverpeak-gigafactory.geojson",
    },
    # Routebrief kobalt-kisanfu-daressalaam, been b1 (LICHTE werkwijze M31).
    # Truck kobalthydroxide KFM Kisanfu-plant → mijnweg → RN39 (bij
    # Kisanfu-dorp) → RN39/RN1 Likasi–Lubumbashi (gedeeld eerste stuk met
    # TFM/KCC, zie koper-kolwezi-durban.md §4) → Kasumbalesa-grens. Geen
    # gepubliceerde bronlengte specifiek voor dit traject; gepubliceerdKm =
    # eigen via-puntenketen (~290 km hemelsbreed), vensterKm ruim omdat de
    # exacte mijnweg-aansluiting nog niet gemeten is.
    "kobalt-kisanfu-daressalaam-kisanfu-kasumbalesa": {
        "via": [
            ("KFM Kisanfu-plant (anker, bron-gelegd)", (25.9983, -10.7630)),
            ("Kisanfu-dorp / RN39-aansluiting", (25.9404, -10.6881)),
            ("Likasi (RN39 → RN1, hergebruikt)", (26.7355, -10.9806)),
            ("Lubumbashi (RN1, hergebruikt)", (27.4827, -11.6642)),
            ("Kasumbalesa-grens (hergebruikt anker)", (27.7959, -12.2658)),
        ],
        "id": "co-kisanfu-kasumbalesa",
        "naam": "KFM Kisanfu-plant → Kasumbalesa (mijnweg → RN39 → RN39/RN1, "
                "gedeeld eerste stuk met TFM/KCC)",
        "extracts": ["congo-drc"],
        "refs": ["RN39", "RN1"],
        "gepubliceerdKm": 290,
        "bronnoot": "geen gepubliceerde bronlengte; eigen via-puntenketen "
                    "~289,7 km hemelsbreed (routebrief §7)",
        "vensterKm": 85,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "kobalt-kisanfu-daressalaam-weg-kisanfu-kasumbalesa.geojson",
    },
    # Routebrief kobalt-kisanfu-daressalaam, been b2 (LICHTE werkwijze M31).
    # Truck kobalthydroxide Kasumbalesa-grens (hergebruikt) → T2/Great North
    # Road: Ndola → Kapiri Mposhi (zuidwaartse T2-lus) → Mpika (wissel
    # Serenje/Chinsali) → Isoka → Nakonde/Tunduma-grens. gepubliceerdKm
    # ~1.750 (Ndola–Tunduma ≈1.900 minus Kasumbalesa–Ndola); eigen
    # hemelsbreed-keten 934,5 km ter controle (verwacht ratio ~1,8-1,9 gezien
    # de Kapiri Mposhi-lus).
    "kobalt-kisanfu-daressalaam-kasumbalesa-nakonde": {
        "via": [
            ("Kasumbalesa-grens (hergebruikt anker)", (27.7959, -12.2658)),
            ("Ndola (T3 → T2)", (28.6366, -12.9693)),
            ("Kapiri Mposhi (T2/T3-kruispunt)", (28.6786, -13.9699)),
            ("Mpika (T2, wissel Serenje/Chinsali)", (31.4555, -11.8432)),
            ("Isoka", (32.6369, -10.1535)),
            ("Nakonde/Tunduma-grens", (32.7612, -9.3208)),
        ],
        "id": "co-kasumbalesa-nakonde",
        "naam": "Kasumbalesa → Nakonde/Tunduma (T2/Great North Road via Ndola–"
                "Kapiri Mposhi–Mpika–Isoka)",
        "extracts": ["zambia"],
        "refs": ["T2", "T3", "Great North Road", "Tanzam"],
        "gepubliceerdKm": 1750,
        "bronnoot": "Ndola–Tunduma ≈1.900 km [3][4] minus Kasumbalesa–Ndola; "
                    "eigen hemelsbreed-keten 934,5 km",
        "vensterKm": 75,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "kobalt-kisanfu-daressalaam-weg-kasumbalesa-nakonde.geojson",
    },
    # Routebrief kobalt-kisanfu-daressalaam, been b3 (LICHTE werkwijze M31).
    # Truck kobalthydroxide Nakonde/Tunduma-grens → T1 Centraal Corridor/
    # TANZAM (A7): Mbeya (wissel TANZAM → Centraal Corridor) → Iringa →
    # Morogoro → Dar es Salaam CT2-kade. gepubliceerdKm ~950 [ontwerp]; eigen
    # hemelsbreed-keten 786,6 km ter controle (verwacht ratio ~1,2).
    # ⚠️ EINDIGT OP DE HAVENPOORT, NIET OP DE KADE: het interne wegennet van
    # Container Terminal II (34 knopen) is in OSM een geïsoleerd eiland — 0,355
    # km van het doorgaande wegnet, geen gedeelde vertex (gemeten: component
    # van de kade bevat 34 knopen, bereikt het hoofdnet niet). Kade → poort
    # wordt in de bake een korte stippel (emplacement/havenpoort, net reikt
    # hier niet — bakhandleiding §2 "Emplacementen...").
    "kobalt-kisanfu-daressalaam-nakonde-daressalaam": {
        "via": [
            ("Nakonde/Tunduma-grens", (32.7612, -9.3208)),
            ("Mbeya (A7/T1, wissel TANZAM → Centraal Corridor)", (33.4687, -8.9065)),
            ("Iringa (A7)", (35.6971, -7.7789)),
            ("Morogoro (A7, wissel richting Dar es Salaam)", (37.6694, -6.8162)),
            ("Dar es Salaam — havenpoort (doorgaand wegnet, 0,355 km van de kade)", (39.293780, -6.840496)),
        ],
        "id": "co-nakonde-daressalaam",
        "naam": "Nakonde/Tunduma → Dar es Salaam-havenpoort (T1 Centraal Corridor/TANZAM "
                "via Mbeya–Iringa–Morogoro)",
        "extracts": ["tanzania"],
        "refs": ["A7", "T1", "Tanzam"],
        "gepubliceerdKm": 950,
        "bronnoot": "~950 km [ontwerp]; eigen hemelsbreed-keten 786,6 km",
        "vensterKm": 100,
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "kobalt-kisanfu-daressalaam-weg-nakonde-daressalaam.geojson",
    },
    # Routebrief uranium-mcarthurriver-porthope, been b1 (LICHTE werkwijze M31).
    # Truck (uraanconcentraat) McArthur River-mijn → Key Lake-mill, eigen
    # mijnweg door het Athabasca-bekken. Géén via-punten (geen corridorkeuze).
    # corridorKlassen ruim gezet: een mijnweg in het boreale woud kan als
    # tertiary/unclassified/service gekarteerd zijn (nooit als track — die
    # klasse komt de scanner niet door, werkwijze §valkuilen).
    "uranium-mcarthurriver-porthope-mcarthurriver-keylake": {
        "via": [
            ("McArthur River-mijn (Cameco 70% / Orano 30%, anker, bron-gelegd)", (-105.0508, 57.7626)),
            ("Key Lake-mill (Cameco, anker, bron-gelegd)", (-105.6740, 57.2130)),
        ],
        "id": "u-mcarthurriver-keylake",
        "naam": "McArthur River-mijn → Key Lake-mill (eigen mijnweg, Athabasca-bekken)",
        "extracts": ["canada"],
        "refs": [],
        "gepubliceerdKm": 80,
        "bronnoot": "80 km eigen mijnweg (Cameco)",
        "vensterKm": 30,
        "corridorKlassen": ["tertiary", "unclassified", "service"],
        "uit": "uranium-mcarthurriver-porthope-weg-mcarthurriver-keylake.geojson",
    },
    # Routebrief uranium-mcarthurriver-porthope, been b2 (LICHTE werkwijze M31).
    # Truck Key Lake-mill → Blind River-raffinaderij, dwars door Canada via
    # Hwy 914→2→16 (Yellowhead) → Trans-Canada Hwy 1/17, langs via-punten
    # (knooppuntsteden, niet per snelwegstuk gebrond — brief §7). vensterKm
    # ruim (90) gezien de lengte (~3.000 km) en de onzekere corridor buiten
    # Saskatoon/Sault Ste. Marie.
    # ⚠️ CORRECTIE OP DE BRIEF (bak-aanwijzing): het brief-via-punt "Points
    # North Landing (Hwy 905/102-knooppunt)" (58.2689,-104.0800) heeft in OSM
    # GEEN wegverbinding met Hwy 914/Key Lake — eerste scanpoging gaf "geen
    # wegpad tussen punt 0 en 1" (ook met corridorKlassen ruim). Nagemeten:
    # Hwy 914 loopt in OSM van McArthur River/Key Lake ZUIDWAARTS tot
    # (-106.7898,55.2348), waar hij exact aansluit op Hwy 165 — bevestigd door
    # Wikipedia (Sask. Hwy 914: "begins at Highway 165 south of Pinehouse …
    # does not intersect with any provincially-owned highways between
    # Highway 165 and Key Lake Mine"). Points North Landing (Hwy 905, ~1,5°
    # verder noordoostelijk) ligt niet aan deze corridor. Via-punt vervangen
    # door de werkelijke Hwy 165/914-aansluiting ten zuiden van Pinehouse
    # (coördinaat = het gemeten OSM-knooppunt, geen schatting).
    # ⚠️ TWEEDE CORRECTIE: "geen wegpad tussen punt 7 en 8" (Thunder Bay →
    # Sault Ste. Marie) — de rechte lijn snijdt over Lake Superior, en de
    # échte Hwy 17 buigt langs de noordoever ruim buiten een 90 km-venster om
    # die rechte lijn. Wawa (Hwy 17-knooppunt, tussenstad, bron-gelegd via
    # Nominatim) toegevoegd als extra via-punt.
    # ⚠️ DERDE CORRECTIE (na toets_knikken.py): het Saskatoon-via-punt
    # (52.1318,-106.6608, stadscentrum) snapte op een doodlopende straat en gaf
    # één echte TERUGLOOP (179,4°, v=29,5) — de doorgaande Hwy 16 loopt hier als
    # Circle Drive (trunk, OSM ref "16") 2,6 km noordelijker. Via-punt verschoven
    # naar de gemeten Circle Drive-coördinaat, geen via-punt bijgeschoven om een
    # km-toets te halen (de lengtetoets stond al binnen norm).
    "uranium-mcarthurriver-porthope-keylake-blindriver": {
        "via": [
            ("Key Lake-mill (Cameco, anker, bron-gelegd)", (-105.6740, 57.2130)),
            ("Hwy 165/914-knooppunt, ten zuiden van Pinehouse (correctie op de "
             "brief — Points North Landing ligt niet aan deze corridor, zie boven)",
             (-106.7898, 55.2348)),
            ("La Ronge (Hwy 102/2-knooppunt)", (-105.2900, 55.1005)),
            ("Prince Albert (Hwy 2/55/3-knooppunt)", (-105.7559, 53.2020)),
            ("Saskatoon (Hwy 16/Circle Drive, gebronde overslagplaats — via-punt "
             "verschoven van het stadscentrum naar de doorgaande ringweg, zie kop)",
             (-106.6606, 52.1579)),
            ("Yorkton (Yellowhead Hwy 16)", (-102.4612, 51.2120)),
            ("Winnipeg (Hwy 1/17-knooppunt)", (-97.1385, 49.8955)),
            ("Thunder Bay (Hwy 17-knooppunt)", (-89.2598, 48.4064)),
            ("Wawa (Hwy 17-knooppunt, extra via-punt — Lake Superior-noordoever)",
             (-84.7740, 47.9929)),
            ("Sault Ste. Marie (Hwy 17-knooppunt)", (-84.3330, 46.5127)),
            ("Blind River Refinery (Cameco, anker, bron-gelegd)", (-83.0174, 46.1810)),
        ],
        "id": "u-keylake-blindriver",
        "naam": "Key Lake-mill → Blind River-raffinaderij (Hwy 914 → 165 → 2 → 16 "
                "(Yellowhead) → Trans-Canada Hwy 1/17, via Pinehouse–Saskatoon–"
                "Winnipeg–Wawa–Sault Ste. Marie)",
        "extracts": ["canada"],
        "refs": ["914", "165", "2", "16", "1", "17", "Yellowhead Highway", "Trans-Canada Highway"],
        "gepubliceerdKm": 3000,
        "bronnoot": "~3.000 km Saskatchewan→Ontario (Watershed Sentinel)",
        "vensterKm": 90,
        "uit": "uranium-mcarthurriver-porthope-weg-keylake-blindriver.geojson",
    },
    # Routebrief uranium-mcarthurriver-porthope, been b3 (LICHTE werkwijze M31).
    # Truck Blind River-raffinaderij → Port Hope Conversion Facility, Hwy 17
    # (Sault Ste. Marie–Sudbury) → Hwy 69 (Georgian Bay-route) → Hwy 400 →
    # Hwy 401, via Sudbury/Parry Sound/Barrie/Vaughan.
    "uranium-mcarthurriver-porthope-blindriver-porthope": {
        "via": [
            ("Blind River Refinery (Cameco, anker, bron-gelegd)", (-83.0174, 46.1810)),
            ("Sudbury (Hwy 17/69-knooppunt)", (-80.9912, 46.4927)),
            ("Parry Sound (Hwy 69/400-knooppunt)", (-80.0337, 45.3436)),
            ("Barrie (Hwy 400/11-knooppunt)", (-79.6901, 44.3893)),
            ("Vaughan (Hwy 400/401-knooppunt)", (-79.5268, 43.7942)),
            ("Port Hope Conversion Facility (Cameco, anker, bron-gelegd)", (-78.2955, 43.9437)),
        ],
        "id": "u-blindriver-porthope",
        "naam": "Blind River-raffinaderij → Port Hope Conversion Facility "
                "(Hwy 17, Sault Ste. Marie–Sudbury–Parry Sound–Barrie–Toronto-omleiding)",
        "extracts": ["canada"],
        "refs": ["17", "69", "400", "401", "Highway 17", "Highway 69", "Highway 400", "Highway 401"],
        "gepubliceerdKm": 600,
        "bronnoot": "600 km Blind River→Port Hope (Watershed Sentinel)",
        "vensterKm": 50,
        "uit": "uranium-mcarthurriver-porthope-weg-blindriver-porthope.geojson",
    },
    # Routebrief uranium-mcarthurriver-porthope, been b4 (LICHTE werkwijze M31).
    # Truck Port Hope Conversion Facility → BWXT Toronto (pelletpers), rechte
    # Hwy 401-corridor, geen via-punten nodig.
    "uranium-mcarthurriver-porthope-porthope-bwxttoronto": {
        "via": [
            ("Port Hope Conversion Facility (Cameco, anker, bron-gelegd)", (-78.2955, 43.9437)),
            ("BWXT Nuclear Energy Canada — Toronto (anker, bron-gelegd)", (-79.4466, 43.6679)),
        ],
        "id": "u-porthope-bwxttoronto",
        "naam": "Port Hope Conversion Facility → BWXT Toronto (pelletpers) (Hwy 401)",
        "extracts": ["canada"],
        "refs": ["401", "Highway 401"],
        "gepubliceerdKm": 112,
        "bronnoot": "~112 km (webcheck, grootcirkel 97 km × wegfactor)",
        "vensterKm": 30,
        "uit": "uranium-mcarthurriver-porthope-weg-porthope-bwxttoronto.geojson",
    },
    # Routebrief uranium-mcarthurriver-porthope, been b5 (LICHTE werkwijze M31).
    # Truck BWXT Toronto (pelletpers) → BWXT Peterborough (bundelfabriek),
    # Hwy 401 oost dan Hwy 115/7 noord. ⚠️ Dit been + b4 zijn een AFWIJKING op
    # het oorspronkelijke ontwerp (dat één been Port Hope→Peterborough gaf,
    # brief §1); Toronto ligt zuidwestelijk van beide, dus de lijn maakt een
    # zichtbare lus/driehoek — dat is correct, geen bakfout.
    "uranium-mcarthurriver-porthope-bwxttoronto-bwxtpeterborough": {
        "via": [
            ("BWXT Nuclear Energy Canada — Toronto (anker, bron-gelegd)", (-79.4466, 43.6679)),
            ("BWXT Nuclear Energy Canada — Peterborough (anker, bron-gelegd)", (-78.3308, 44.2955)),
        ],
        "id": "u-bwxttoronto-bwxtpeterborough",
        "naam": "BWXT Toronto (pelletpers) → BWXT Peterborough (bundelfabriek) "
                "(Hwy 401 → Hwy 115/7)",
        "extracts": ["canada"],
        "refs": ["401", "115", "7", "Highway 401", "Highway 115", "Highway 7"],
        "gepubliceerdKm": 145,
        "bronnoot": "~145 km (webcheck, grootcirkel 113 km × wegfactor)",
        "vensterKm": 30,
        "uit": "uranium-mcarthurriver-porthope-weg-bwxttoronto-bwxtpeterborough.geojson",
    },
    # Routebrief uranium-inkai-poti, been b1 (LICHTE werkwijze M31). Truck
    # (yellowcake) Inkai MPP (JV Inkai, Kazatomprom/Cameco) → Zhanatas-
    # spoorstation, woestijnsteppe Suzak-district → Zjambyl-oblast, geen
    # gepubliceerde wegroute (brief §7: "aannemelijk: één bron" voor het feit
    # van truckvervoer; de weg zelf komt uit OSM). Geen via-punten bekend →
    # ruim venster, laat de Dijkstra de kortste hoofdweg vinden.
    "uranium-inkai-poti-inkai-zhanatas": {
        "via": [
            ("Inkai MPP — hoofdverwerkingsfabriek (JV Inkai, anker, bron-gelegd)", (67.5255, 45.2855)),
            ("Zhanatas-spoorstation (anker, bron-gelegd)", (69.7260, 43.5610)),
        ],
        "id": "u-inkai-zhanatas",
        "naam": "Inkai MPP → Zhanatas-spoorstation (woestijnweg Suzak-district → "
                "Zjambyl-oblast, aannemelijk: één bron)",
        "extracts": ["kazachstan"],
        "refs": [],
        "gepubliceerdKm": 290,
        "bronnoot": "~290 km hemelsbreed (Cameco 2024 NI 43-101 §18.2: "
                    "\"shipments... delivered to the Zhanatas rail station\"); "
                    "geen gepubliceerde wegkm",
        "vensterKm": 75,
        "uit": "uranium-inkai-poti-weg-inkai-zhanatas.geojson",
    },
    # Routebrief uranium-rossing-walvisbay, been b1 (LICHTE werkwijze M31).
    # Truck (yellowcake-drums) Rössing-fabriek (Arandis) → Walvis Bay-haven,
    # over de B2 (enige gekarteerde hoofdweg, geen corridorkeuze — geen
    # via-punten). Modaliteit AANNEMELIJK (brief §7: analogie met Husab).
    "uranium-rossing-walvisbay": {
        "via": [
            ("Rössing-fabriek (Arandis, anker, bron-gelegd)", (15.0405, -22.4635)),
            ("Walvis Bay-haven, NamPort containerterminal (anker, bron-gelegd)", (14.4840, -22.9465)),
        ],
        "id": "u-rossing-walvisbay",
        "naam": "Rössing-fabriek (Arandis) → Walvis Bay-haven (B2, aannemelijk: "
                "analogie met Husab)",
        "extracts": ["namibie"],
        "refs": ["B2"],
        "gepubliceerdKm": 90,
        "bronnoot": "~90 km indicatief (afgeleid: Wikipedia 80 km hemelsbreed "
                    "NO + B2 Arandis–Walvis Bay 77 km, routebrief §2/§7)",
        "vensterKm": 40,
        "uit": "uranium-rossing-walvisbay-weg.geojson",
    },
    # Routebrief uranium-arlit-cotonou, been b1 (LICHTE werkwijze M31). Truck
    # (yellowcake-vaten) SOMAIR-mijn Arlit → Agadez → Tahoua → Niamey → Dosso →
    # brug Gaya/Malanville (RN1 Niger). Historische exportroute, operationeel
    # gestaakt sinds de grenssluiting van 26-07-2023 (statusfeit, geen stippel-
    # reden — het net bestaat en is gemeten, zie brief §2).
    # ⚠️ Km AANNEMELIJK: geen bron meet dit deelstuk apart; ~1.270 km is
    #    afgeleid (1.600 km totaal Arlit→Parakou (WNA) minus ~330 km Benin-
    #    been). Tolerantie ruim nemen.
    "uranium-arlit-cotonou-arlit-grens": {
        "via": [
            ("SOMAIR-mijn/verwerkingscomplex, Arlit (anker, bron-gelegd)",     (7.3443, 18.7731)),
            ("Agadez",                                                        (7.9907, 16.9726)),
            ("Tahoua",                                                        (5.2621, 14.8899)),
            ("Niamey",                                                        (2.1098, 13.5248)),
            ("Dosso",                                                         (3.1945, 13.0496)),
            ("Brug Gaya/Malanville (anker, grensovergang, bron-gelegd)",      (3.3961, 11.8807)),
        ],
        "id": "u-arlit-grens",
        "naam": "SOMAIR-mijn Arlit → Agadez → Tahoua → Niamey → Dosso → grens "
                "Gaya/Malanville (RN1 Niger, aannemelijk: één bron)",
        "extracts": ["niger"],
        "refs": ["RN1"],
        "gepubliceerdKm": 1270,
        "bronnoot": "afgeleid: 1.600 km totaal Arlit→Parakou (WNA) minus ~330 "
                    "km Benin-been (routebrief §2/§8[1][8]) — geen directe "
                    "bron voor dit deelstuk, tolerantie ruim nemen",
        "vensterKm": 40,
        # ⚠️ Eerste poging (WEG_HOUD kaal) faalde tussen Tahoua en Niamey:
        # "geen wegpad tussen punt 2 en 3" — de RN1 draagt daar kennelijk geen
        # motorway/trunk/primary/secondary-tag over het hele traject.
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "uranium-arlit-cotonou-weg-arlit-grens.geojson",
    },
    # Routebrief uranium-arlit-cotonou, been b2 (LICHTE werkwijze M31). Truck
    # (yellowcake-vaten) brug Gaya/Malanville → Kandi → Bembèrèkè → Parakou-
    # emplacement (RNIE2 Benin).
    # ⚠️ Parakou-anker is AANNEMELIJK (brief §3): OSM-punt "Gare" is een gebouw
    #    in de stad, geen apart vrachtemplacement satelliet-onderscheiden.
    "uranium-arlit-cotonou-grens-parakou": {
        "via": [
            ("Brug Gaya/Malanville (anker, grensovergang, bron-gelegd)",      (3.3961, 11.8807)),
            ("Kandi",                                                         (2.9322, 11.1311)),
            ("Bembèrèkè",                                                     (2.7507, 10.2540)),
            ("Spoorstation Gare, Parakou (anker, aannemelijk)",              (2.6099, 9.3487)),
        ],
        "id": "u-grens-parakou",
        "naam": "grens Gaya/Malanville → Kandi → Bembèrèkè → Parakou-"
                "emplacement (RNIE2 Benin)",
        "extracts": ["benin"],
        "refs": ["RNIE2"],
        "gepubliceerdKm": 330,
        "bronnoot": "RNIE2 Cotonou-grens 729 km minus spoorlijn 400 km ≈ 329; "
                    "kruisbevestigd Rome2Rio Malanville→Parakou ≈322 km "
                    "(routebrief §2/§8[2][9])",
        "vensterKm": 40,
        # ⚠️ Eerste poging (WEG_HOUD kaal) gaf een via-snap van 6,71 km bij
        # Bembèrèkè — de RNIE2 draagt daar geen primary/secondary-tag
        # (osmium-check: unclassified op 0,39 km, tertiary op 1,13 km, geen
        # grotere klasse binnen 8 km).
        "corridorKlassen": ["tertiary", "unclassified"],
        "uit": "uranium-arlit-cotonou-weg-grens-parakou.geojson",
    },
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
