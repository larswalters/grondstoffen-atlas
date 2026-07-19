#!/usr/bin/env python3
"""
fetch_waterways.py — bevaarbare-vaarweg-middellijnen per systeem (M24, LAR-486).

Drie bronnen; de bake-off van LAR-486 vergeleek de eerste twee op hetzelfde traject:
  osm        Overpass API — waterway=river|canal|fairway met een CEMT-tag of een
             naam uit de whitelist, binnen de systeem-bbox.
             Licentie: ODbL — "© OpenStreetMap contributors" hoort in de HUD.
  geofabrik  DEZELFDE OSM-data, maar uit een lokale regio-extract (.osm.pbf)
             i.p.v. via de API. Zelfde licentie, zelfde filters, zelfde stitcher.
  unece      het E-waterway-netwerk uit de UNECE Blue Book database
             (gis.unece.org, ArcGIS Feature Service / shapefile-export).

Waarom `geofabrik` naast `osm`: de publieke Overpass-mirrors zijn de traagste en
broosste stap van de hele pijplijn gebleken (~25 min voor 6 systemen tegen ~1 min
bakken, met 504's op queries die minuten eerder slaagden). Een regio-extract haalt
~45 MB/s en is daarna offline en herhaalbaar — wat de wereldwijde uitrol met
tientallen systemen pas praktisch maakt. `osm` blijft bestaan als kruiscontrole:
beide paden horen dezelfde middellijn op te leveren.

De extractie is bron-agnostisch: uit de ruwe segmenten wordt het KORTSTE
WATERPAD gestitcht van anker-zee naar anker-binnen (dijkstra over de
segment-geometrie; uiteinden binnen de stitch-tolerantie gelden als
verbonden). Zelfde ankers + andere bron = zelfde traject, vergelijkbaar.

Uitvoer: v2/build-cache/vaarwegen_<bron>.geojson — één LineString per systeem,
coördinaten beginnen ALTIJD aan de zeezijde. bake_marnet.py leest dit via
--vaarwegen en hangt de ketens aan het MARNET-netwerk.

Draaien:  python v2/tools/fetch_waterways.py osm
          python v2/tools/fetch_waterways.py geofabrik [--download]
          python v2/tools/fetch_waterways.py unece --bestand <pad .geojson/.shp>
"""

import argparse
import hashlib
import heapq
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
CACHE = os.path.join(V2, "build-cache")

OVERPASS_URLS = [
    "https://overpass.private.coffee/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass-api.de/api/interpreter",
]
# De publieke mirrors geven onder belasting 504's — óók op queries die minuten
# eerder gewoon slaagden. Eén ronde langs de lijst is dus te weinig; met een
# pauze ertussen komt hij er wel door. Elke geslaagde query gaat de cache in,
# dus een herstart begint nooit opnieuw.
OVERPASS_RONDES = 4
OVERPASS_PAUZE_S = 30
# Twee verschillende klokken, bewust uit elkaar gehouden: de server mag lang
# rekenen, maar wij moeten SNEL kunnen doorschakelen naar een andere mirror.
# Eén gedeelde waarde van 600 s liet een overbelaste mirror de hele run tien
# minuten gijzelen; een zware bbox-query duurt gemeten ~75 s.
OVERPASS_SERVER_S = 300   # [timeout:] in de query zelf
OVERPASS_CLIENT_S = 180   # urllib — daarna de volgende mirror

R_AARDE = 6371.0

# Stitch-tolerantie per bron: OSM-ways delen exacte knopen (kleine marge voor
# fairway->rivier-overgangen); officiële netten hebben grovere segmentatie.
STITCH_KM = {"osm": 0.06, "geofabrik": 0.06, "unece": 0.8}
ANKER_TOL_KM = 6.0    # anker moet binnen deze afstand van de geometrie liggen
SIMPLIFY_KM = 0.025   # Douglas-Peucker ~25 m: bochten blijven, ruis verdwijnt

# bbox = (lat_min, lon_min, lat_max, lon_max) — Overpass-volgorde (Z,W,N,O).
# Ankers als (lon, lat); zeezijde eerst. Havens (searoute): Amsterdam
# (4.904, 52.375) · Nijmegen (5.867, 51.833) · Rotterdam (4.442, 51.904).
#
# `volgt_op` (LAR-487/488): dit systeem hangt niet aan MARNET maar aan het
# binneneinde van dat eerdere systeem — zo draagt één rivier twee labels met
# elk een eigen zeevaart-vlag (Mississippi zeevaarbaar t/m Baton Rouge, de
# Yangtze t/m Nanjing; daarboven binnenvaart). Het vervolgsysteem moet dus
# LATER in deze lijst staan en zijn anker_zee gelijk hebben aan het
# anker_binnen van zijn voorganger.
SYSTEMEN = [
    dict(
        label="noordzeekanaal",
        zeevaart=True,
        cemt="VIb",
        extracts=["nederland"],
        bbox=(52.34, 4.50, 52.52, 5.02),
        namen=["Noordzeekanaal", "Het IJ", "Afgesloten IJ", "Buiten-IJ",
               "Voorzaan", "Zijkanaal G", "Buitenhaven", "IJmuiden"],
        anker_zee=(4.565, 52.463),      # havenmond IJmuiden (vóór de sluizen)
        anker_binnen=(4.904, 52.383),   # Het IJ t.h.v. de haven van Amsterdam
    ),
    dict(
        label="waal",
        zeevaart=False,
        cemt="VIc",
        extracts=["nederland"],
        bbox=(51.70, 3.95, 52.05, 6.00),
        namen=["Nieuwe Waterweg", "Het Scheur", "Scheur", "Nieuwe Maas",
               "Noord", "Beneden-Merwede", "Beneden Merwede",
               "Boven-Merwede", "Boven Merwede", "Waal",
               "Oude Maas", "Dordtsche Kil", "Maasmond", "Calandkanaal"],
        anker_zee=(4.060, 51.985),      # Maasmond / Hoek van Holland
        anker_binnen=(5.860, 51.852),   # Waal t.h.v. Nijmegen (Waalkade)
    ),
    # ---- Rijn (LAR-492) — vervolg op `waal`: Nijmegen -> Basel, het kopeinde
    # van de scheepvaart. Alle searoute-Rijnhavens snappen nu op knoop 9697 (het
    # binneneinde van `waal`), van Duisburg 75,8 km tot Kehl 389,4 km — het
    # Nijmegen/Memphis-patroon over de hele as.
    # Namen OPGEZOCHT met survey_vaarwegen.py, niet geraden; twee vondsten die
    # de keten anders stil hadden doorgeknipt:
    #   `Boven-Rijn` (4,3 km, mét koppelteken) overbrugt Bijlandsch Kanaal ->
    #   `Rhein`, en `Le Rhin / Rhein` is de GECOMBINEERDE grensnaam op het
    #   Frans-Duitse traject (Basel-Karlsruhe) — de `Dunaj / Duna`-valkuil.
    # Bewust NIET in de whitelist: `Pannerdensch Kanaal` (tak naar Nederrijn/
    # IJssel) en `Vieux Rhin / Altrhein` (de Restrhein — wél water, géén
    # bevaarbare geul; die zou een korter maar onvaarbaar pad opleveren).
    # Gesplitst bij BINGEN (rkm 528), het bovenstroomse eind van de
    # Gebirgsstrecke. Besluit van Lars: het splitspunt moet een echte
    # verstoring modelleren, niet de zeevaart/binnenvaart-grens (die klopt hier
    # sowieso niet — `waal` stroomafwaarts is al binnenvaart). Bij Kaub, midden
    # in die bergstrecke, legde het laagwater van 2018 en 2022 de hele as stil;
    # `rijn-boven` in `vermijd` zetten reproduceert precies dat: Basel,
    # Ludwigshafen en Karlsruhe onbereikbaar, Duisburg en Keulen niet.
    dict(
        label="rijn",
        zeevaart=False,         # sluit aan op `waal`, dat ook binnenvaart is
        cemt="VIb",
        volgt_op="waal",
        extracts=["nederland", "de-nrw", "de-rheinland-pfalz"],
        bbox=(49.85, 5.75, 52.05, 8.10),
        namen=["Waal", "Bijlandsch Kanaal", "Boven-Rijn", "Rhein"],
        anker_zee=(5.860, 51.852),      # = anker_binnen van 'waal' (Waalkade)
        anker_binnen=(7.8868, 49.9729),  # Binger Loch, bovenkant Gebirgsstrecke
    ),
    dict(
        label="rijn-boven",
        zeevaart=False,
        cemt="VIb",
        volgt_op="rijn",
        # fr-alsace is hier NIET optioneel: tussen Basel en Straatsburg ligt de
        # vaargeul in het Grand Canal d'Alsace, volledig op Frans grondgebied.
        # Zonder die extract knipt de keten met een gat van 72,9 km.
        extracts=["de-rheinland-pfalz", "de-baden-wuerttemberg",
                  "fr-alsace", "zwitserland"],
        bbox=(47.40, 7.30, 50.10, 8.70),
        # `Le Rhin / Rhein` is de GECOMBINEERDE grensnaam op het Frans-Duitse
        # traject — de `Dunaj / Duna`-valkuil. De Écluse-namen zijn de sluizen
        # van de Elzas-kanalen; die dragen de keten door de omleidingskanalen.
        # Bewust NIET: `Vieux Rhin / Altrhein` (de Restrhein) — dat is wél water
        # maar géén bevaarbare geul, en zou een korter, onvaarbaar pad geven.
        namen=["Rhein", "Le Rhin / Rhein", "Canal d'Alsace",
               "Grand Canal d'Alsace", "Écluse de Kembs",
               "Écluse No", "Écluse No 2", "Écluse No 3"],
        anker_zee=(7.8868, 49.9729),    # = anker_binnen van 'rijn'
        anker_binnen=(7.590, 47.575),   # Rijn bij Basel (Kleinhüningen)
    ),
    # ---- Mosel (LAR-504-bewijs) — de eerste ECHTE aftakking: dit systeem hangt
    # niet aan het einde van `rijn` maar middenin, bij de monding in Koblenz
    # (Rijn-rkm 592, ruim binnen `rijn` dat van Nijmegen 884,6 tot Bingen 528
    # loopt). Daarmee is `volgtOp` geen ketting meer maar een boom.
    # Naam wisselt op de grens: `Mosel` (DE/LU) -> `La Moselle` (FR), met
    # overlap tussen lat 49,47 en 49,67 — hetzelfde patroon als Maas/La Meuse
    # en Le Rhin / Rhein. Kopeinde Neuves-Maisons: dáár stopt de Grande
    # Canalisation, niet bij de landsgrens (vandaar `fr-lorraine` + `luxemburg`).
    dict(
        label="mosel",
        zeevaart=False,
        cemt="Vb",
        # ⚠️ CEMT-clause UIT: die haalt élke geklasseerde vaarweg in de bbox
        # binnen, en bij Nancy liggen Freycinet-kanalen van klasse I (350 t)
        # die als kortste pad wonnen van de Moezel zelf — 18 km te kort én de
        # verkeerde vaarweg. Bulkschepen varen daar niet; de namenlijst is hier
        # dus de scherpere filter dan de tag.
        cemt_insluiten=False,
        volgt_op="rijn",
        extracts=["de-rheinland-pfalz", "luxemburg", "fr-lorraine"],
        bbox=(48.55, 5.85, 50.45, 7.70),
        namen=["Mosel", "La Moselle", "La Moselle Canalisée",
               "Canal de la Moselle", "Canal des Mines de Fer de la Moselle",
               "Dérivations de Pagny-sur-Moselle", "Dérivation de Custines",
               "Dérivation de Pompey"],
        anker_zee=(7.6065, 50.3645),    # Moselmonding bij Koblenz (Deutsches Eck)
        anker_binnen=(6.102, 48.617),   # Neuves-Maisons, kopeinde van de vaart
    ),
    # ---- Maas + Benelux-delta (LAR-505) — Lars: "we moeten nog wel meer mappen
    # dan alleen de rijn, de maas en stukken biesbosch". De `waal`-keten legt
    # één lijn door de delta; in werkelijkheid is het een NET, en de Maas
    # ontbrak volledig.
    # Dit systeem takt middenin `waal` af, bij Werkendam waar de Nieuwe Merwede
    # (de Biesbosch-verbinding) van de Boven-Merwede afsplitst — het tweede
    # bewijs van LAR-504, en de eerste keer dat een route DWARS DOOR een
    # aftakking heen moet.
    # Namen opgezocht met survey_vaarwegen.py; `Amer` (12,5 km, lon
    # 4,672…4,847) is de derde stille ketenbreuk die de survey vóór het stitchen
    # ving — zonder die naam gaapt er een gat tussen het Hollandsch Diep (eindigt
    # op 4,672) en de Bergsche Maas (begint op 4,847), net als `Boven-Rijn` en
    # `Le Rhin / Rhein`. Naamwissel op de taalgrens: `Maas` -> `La Meuse` op
    # exact lat 50,762 (de Mosel/Moselle-val).
    # ⚠️ CEMT-clause UIT, om dezelfde reden als bij de Mosel maar met een andere
    # dader: de Zuid-Willemsvaart (klasse II) loopt kaarsrecht parallel aan de
    # meanderende Maas van 's-Hertogenbosch tot Maastricht en zou als kortste
    # pad winnen. Ook de Wilhelminakanaal/Kanaal Wessem-Nederweert-takken komen
    # via de tag binnen. De namenlijst is hier scherper dan de klasse.
    dict(
        label="maas",
        zeevaart=False,
        cemt="Vb",
        cemt_insluiten=False,
        volgt_op="waal",
        extracts=["nederland", "belgie"],
        bbox=(50.55, 4.35, 51.90, 6.10),
        namen=["Nieuwe Merwede", "Hollandsch Diep", "Amer", "Bergsche Maas",
               "Maas", "Julianakanaal", "La Meuse"],
        anker_zee=(4.894, 51.821),      # Werkendam: splitsing Nieuwe Merwede
        anker_binnen=(5.573, 50.645),   # Maas bij Luik (searoute-haven `Liege`)
    ),
    # Kopeinde stroomopwaarts van Luik. Apart label = een eigen `vermijd`-knop
    # én de plek waar de afbakening uit het issue valt: bóven Namen is de Franse
    # Meuse klasse I-II en valt hij onder Lars' snoeiregel.
    dict(
        label="maas-boven",
        zeevaart=False,
        cemt="Va",
        cemt_insluiten=False,
        volgt_op="maas",
        extracts=["belgie"],
        bbox=(50.35, 4.75, 50.80, 5.65),
        namen=["La Meuse"],
        anker_zee=(5.573, 50.645),      # = anker_binnen van 'maas'
        anker_binnen=(4.867, 50.462),   # Meuse bij Namen
    ),
    # Het Albertkanaal is de commerciële hoofdader Luik -> Antwerpen (klasse
    # VIb) en verbindt het Maas-net met de Schelde uit LAR-495. Draagt ZIJN
    # EIGEN grensnaam-val: bij Luik heet hij `Canal Albert` (18,7 km, lat
    # 50,653…50,806), daarboven `Albertkanaal` — zonder allebei knipt de keten
    # bij Ternaaien door.
    dict(
        label="albertkanaal",
        zeevaart=False,
        cemt="VIb",
        cemt_insluiten=False,
        volgt_op="maas",
        extracts=["belgie"],
        bbox=(50.58, 4.35, 51.30, 5.75),
        # `Canal de Monsin` (1,0 km) is de schakel: de Meuse komt bij Luik niet
        # rechtstreeks op het kanaal uit maar via het Monsin-eiland. Zonder die
        # naam vindt de stitcher géén doorlopend pad (gemeten, niet gegokt).
        # ⚠️ DERDE VERSCHIJNING VAN "welk schip past erdoor" — nu op SLUISNIVEAU.
        # Het Albertkanaal viel uiteen in zes losse componenten met gaten van
        # ~150 m: bij elk van de vier sluiscomplexen liggen DRIE parallelle
        # kolken als aparte benoemde canal-ways (`duwvaartsas` / `middensas` /
        # `noordersas`), en de doorgaande `Albertkanaal`-way stopt ervóór.
        # Alleen de **duwvaartsas** is de kolk voor commerciële duwvaart; door
        # uitsluitend die te whitelisten kiest de keten per constructie de
        # grootgabarit-doorgang in plaats van de kortste kolk.
        # Bewust NIET `La Dérivation`: dat is de Maas-omleiding dwars door Luik,
        # die hoort bij `maas`. Hij ligt 841 m van het kanaal en vormde een
        # eigen eilandje — waar het anker vervolgens op snapte, zodat de
        # stitcher geen pad vond terwijl de keten zelf al heel was.
        namen=["Albertkanaal", "Canal Albert", "Canal de Monsin",
               "Canal de Lanaye",
               "Diepenbeek duwvaartsas", "Hasselt duwvaartsas",
               "Kwaadmechelen duwvaartsas", "Olen duwvaartsas"],
        # Het aftakpunt is het ZUIDEINDE van `Canal Albert` in Luik, niet de
        # Canal de Monsin: die bestaat uit twee stukjes met 130 m ertussen, en
        # het anker snapte op het losse fragment terwijl de keten zelf al heel
        # was — de stitcher meldde dan "geen doorlopend waterpad", wat naar de
        # ketting wees in plaats van naar het anker. Dit punt ligt MIDDENIN de
        # `maas`-keten (die van Maastricht naar Luik loopt en hier langskomt),
        # dus dit is de tweede echte mid-keten-aftakking.
        anker_zee=(5.6165, 50.6527),    # Canal Albert verlaat de Maas bij Luik
        anker_binnen=(4.428, 51.238),   # Albertkanaal bij Antwerpen
    ),
    # Het Amsterdam-Rijnkanaal takt bij Tiel middenin de Waal af en loopt door
    # tot het IJ. Dit is het eerste systeem dat aan BEIDE kanten aan een
    # bestaande keten hangt: `volgt_op` hecht de Tiel-kant aan `waal`,
    # `sluit_aan` hecht de Amsterdam-kant aan `noordzeekanaal`. Zonder die
    # tweede hechting is het kanaal een doodlopende tak van 73 km waar nooit
    # een route overheen kan — gemeten: Amsterdam->Nijmegen bleef 263 km, mét
    # én zonder het kanaal. Dít is waar een lijnennet een NET wordt: Amsterdam
    # kan nu de Rijn op zonder eerst naar zee.
    # ⚠️ De laatste ~3 km over het IJ, tussen het noordeinde van het kanaal
    # (4,950) en het binneneinde van `noordzeekanaal` (4,904), ligt in OSM niet
    # als benoemde doorgaande lijn (gecontroleerd: geen `Het IJ` in dat venster).
    # Die overbrugt `sluit_aan` expliciet als één sluitedge over het IJ — echt
    # water, en zichtbaar in de bake-uitvoer in plaats van stilzwijgend gladgestreken.
    dict(
        label="amsterdam-rijnkanaal",
        zeevaart=False,
        cemt="VIb",
        cemt_insluiten=False,
        volgt_op="waal",
        sluit_aan="noordzeekanaal",
        extracts=["nederland"],
        bbox=(51.85, 4.88, 52.42, 5.52),
        namen=["Amsterdam-Rijnkanaal"],
        anker_zee=(5.440, 51.890),      # Waal bij Tiel
        anker_binnen=(4.950, 52.380),   # noordeinde van het kanaal, in het IJ
    ),
    # ---- VS (LAR-487) — MARNET's mississippi-tak eindigt bij New Orleans en
    # loopt daar dood in het Pontchartrainmeer; alles stroomopwaarts ontbreekt.
    # Baton Rouge is het kopeinde van de diepzeevaart (~370 km binnenland),
    # daarboven is het duwbakgebied → tweede label zónder zeevaart-vlag.
    dict(
        label="mississippi",
        zeevaart=True,
        cemt="",
        extracts=["us-louisiana", "us-mississippi"],
        bbox=(29.85, -91.35, 30.60, -89.90),
        namen=["Mississippi River", "Mississippi"],
        anker_zee=(-90.055, 29.935),    # rivier bij New Orleans (Algiers Point)
        anker_binnen=(-91.190, 30.445),  # haven van Baton Rouge
    ),
    dict(
        label="mississippi-boven",
        zeevaart=False,
        cemt="",
        volgt_op="mississippi",
        extracts=["us-louisiana", "us-mississippi", "us-arkansas", "us-tennessee"],
        bbox=(30.30, -92.00, 35.35, -89.60),
        namen=["Mississippi River", "Mississippi"],
        anker_zee=(-91.190, 30.445),    # = anker_binnen van 'mississippi'
        anker_binnen=(-90.125, 35.125),  # rivier bij Memphis
    ),
    # ---- China (LAR-488) — géén officiële tweede bron; MARNET houdt op bij
    # Zhenjiang (knoop 9668), 78 km vóór Nanjing. Zeeschepen varen echt tot
    # Nanjing (12,5 m-diepwaterkanaal), daarboven binnenvaart.
    dict(
        label="yangtze",
        zeevaart=True,
        cemt="",
        extracts=["china"],
        bbox=(31.90, 118.55, 32.45, 119.70),
        namen=["长江", "扬子江", "Yangtze River", "Yangtze"],
        anker_zee=(119.545, 32.195),    # MARNET-uiteinde bij Zhenjiang
        anker_binnen=(118.735, 32.095),  # haven van Nanjing
    ),
    dict(
        label="yangtze-boven",
        zeevaart=False,
        cemt="",
        volgt_op="yangtze",
        extracts=["china"],
        bbox=(29.50, 113.90, 32.30, 118.85),
        namen=["长江", "扬子江", "Yangtze River", "Yangtze"],
        anker_zee=(118.735, 32.095),    # = anker_binnen van 'yangtze'
        anker_binnen=(114.300, 30.590),  # haven van Wuhan
    ),
    # ---- Myanmar (LAR-485 restpunt) — MARNET eindigt 21 km voor Yangon in een
    # doodlopende knoop 5358; de haven snapt daardoor 21,8 km weg en de route
    # eindigt als rechte stub over land. Namen komen uit de extract zelf
    # (het OSM-hoofdlabel is Birmaans; de Engelse naam staat in name:en).
    dict(
        label="yangon",
        zeevaart=True,
        cemt="",
        extracts=["myanmar"],
        bbox=(16.45, 95.95, 16.90, 96.45),
        namen=["ရန်ကုန်မြစ်",
               "လှိုင်မြစ်"],
        anker_zee=(96.250, 16.595),     # MARNET-uiteinde knoop 5358
        anker_binnen=(96.168, 16.775),  # haven van Yangon
    ),
    # ---- Amazone (uitrol) — GEEN benoemde middellijn in OSM: tussen Manaus en
    # de monding is de rivier >10 km breed en als watervlak gemapt. Dit systeem
    # wordt daarom AFGELEID uit de vlakken i.p.v. gestitcht uit lijnen.
    # MARNET loopt dood bij Macapa (knoop 5067); Manaus snapte 1.084 km weg --
    # het grootste gat van alle systemen tot nu toe.
    dict(
        label="amazone",
        zeevaart=True,          # zeeschepen varen tot Manaus, 1.300 km landinwaarts
        cemt="",
        extracts=["brazilie"],
        vlakken=dict(cel=0.004, min_klaring=0.15),
        bbox=(-4.0, -60.5, 1.0, -49.8),
        namen=[],               # niet van toepassing: afgeleid uit vlakken
        anker_zee=(-50.823, 0.132),     # MARNET-uiteinde bij Macapa
        anker_binnen=(-60.020, -3.130),  # haven van Manaus
    ),
]


def km(a, b):
    """Haversine tussen (lon,lat)-paren."""
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R_AARDE * math.asin(min(1.0, math.sqrt(h)))


# ---------------------------------------------------------------- bron: OSM

def overpass(query):
    """Overpass-antwoord, met een schijf-cache op de query-hash.

    De cache maakt herhalen goedkoop: ankers/simplify aanpassen hoeft niet
    opnieuw over de lijn (dezelfde les als de verzoening-cache in
    bake_marnet.py — bewaarpunt éérst bij dure pijplijnen). De bbox en de
    namen zitten ín de query, dus de sleutel vervalt vanzelf zodra die
    veranderen.
    """
    # Sleutel op de INHOUD van de query (bbox + namen), niet op de
    # instellingenregel: aan een timeout draaien mag nooit opgehaalde data
    # weggooien.
    kern = "\n".join(r for r in query.splitlines() if not r.startswith("[out:"))
    sleutel = hashlib.sha1(kern.encode()).hexdigest()[:16]
    cache_map = os.path.join(CACHE, "overpass")
    cache_pad = os.path.join(cache_map, f"{sleutel}.json")
    if os.path.exists(cache_pad):
        print(f"  overpass uit cache ({sleutel})")
        with open(cache_pad, encoding="utf-8") as f:
            return json.load(f)

    data = urllib.parse.urlencode({"data": query}).encode()
    fout = None
    for ronde in range(OVERPASS_RONDES):
        if ronde:
            print(f"  alle mirrors bezet — ronde {ronde + 1}/{OVERPASS_RONDES} "
                  f"na {OVERPASS_PAUZE_S}s")
            time.sleep(OVERPASS_PAUZE_S)
        for url in OVERPASS_URLS:
            try:
                req = urllib.request.Request(url, data=data, headers={
                    "User-Agent": "grondstoffen-atlas/M24 (github.com/larswalters/grondstoffen-atlas)"})
                with urllib.request.urlopen(req, timeout=OVERPASS_CLIENT_S) as r:
                    antwoord = json.load(r)
                os.makedirs(cache_map, exist_ok=True)
                with open(cache_pad, "w", encoding="utf-8") as f:
                    json.dump(antwoord, f)
                return antwoord
            except Exception as e:  # noqa: BLE001 — mirror proberen, dan pas falen
                fout = e
                print(f"  overpass-mirror faalde ({url.split('/')[2]}): {e}")
    raise RuntimeError(f"alle Overpass-mirrors faalden na {OVERPASS_RONDES} rondes: {fout}")


def segmenten_osm(systeem):
    la0, lo0, la1, lo1 = systeem["bbox"]
    bbox = f"({la0},{lo0},{la1},{lo1})"
    delen = []
    # De CEMT-clause heeft géén naamfilter en scant dus élke waterway in de
    # bbox. Buiten Europa bestaat de tag niet, dus daar is dat pure kosten:
    # de Mississippi-delta (bayous!) liep er op beide mirrors in een timeout.
    # Alleen meenemen als het systeem zelf een CEMT-klasse draagt.
    if systeem.get("cemt") and systeem.get("cemt_insluiten", True):
        delen.append(f'  way["waterway"~"^(river|canal|fairway)$"]["CEMT"]{bbox};')
    for naam in systeem["namen"]:
        # Exacte tag-match i.p.v. één naam-regex: Overpass indexeert key=value,
        # terwijl een regex een scan over alle waterways in de bbox afdwingt.
        # De oude regex was ^(...)$-geankerd, dus dit selecteert hetzelfde.
        delen.append(f'  way["waterway"~"^(river|canal|fairway)$"]["name"="{naam}"]{bbox};')
    query = ("[out:json][timeout:%d];\n(\n%s\n);\nout geom;\n"
             % (OVERPASS_SERVER_S, "\n".join(delen)))
    antwoord = overpass(query)
    segs = []
    cemt_gezien = {}
    for el in antwoord.get("elements", []):
        geom = el.get("geometry") or []
        if el.get("type") != "way" or len(geom) < 2:
            continue
        tags = el.get("tags") or {}
        pts = [(p["lon"], p["lat"]) for p in geom]
        naam = tags.get("name", "")
        segs.append((pts, naam))
        if tags.get("CEMT"):
            cemt_gezien[naam or f"way/{el.get('id')}"] = tags["CEMT"]
    return segs, cemt_gezien


# ------------------------------------------------------------ bron: Geofabrik
#
# Zelfde OSM-data als het Overpass-pad, maar uit een lokale regio-extract. De
# filters hieronder spiegelen de Overpass-query exact (waterway-type, naam uit de
# whitelist, CEMT alleen als het systeem een CEMT-klasse draagt), zodat beide
# bronnen vergelijkbaar blijven — dat is de kruiscontrole.

GEOFABRIK = os.path.join(CACHE, "geofabrik")
GEOFABRIK_BASIS = "https://download.geofabrik.de/"

# Geofabrik levert géén free-shapefile voor de grootste regio's (Brazilië,
# Rusland geven 0 bytes), dus .osm.pbf is het enige formaat dat overal bestaat.
# Rusland staat als federale districten in de lijst: de Wolga heeft er drie
# nodig (~1,9 GB) i.p.v. het hele land (~3,9 GB).
GEOFABRIK_REGIOS = {
    "myanmar": "asia/myanmar",
    "china": "asia/china",
    "vietnam": "asia/vietnam",
    "cambodia": "asia/cambodia",
    "argentina": "south-america/argentina",
    "paraguay": "south-america/paraguay",
    "congo-drc": "africa/congo-democratic-republic",
    "rusland-centraal": "russia/central-fed-district",
    "rusland-wolga": "russia/volga-fed-district",
    "rusland-zuid": "russia/south-fed-district",
    "nederland": "europe/netherlands",
    # de Mississippi vormt staatsgrenzen -> beide oevers nodig
    "us-louisiana": "north-america/us/louisiana",
    "us-mississippi": "north-america/us/mississippi",
    "us-arkansas": "north-america/us/arkansas",
    "us-tennessee": "north-america/us/tennessee",
    # --- uitrol: Ohio (kolen!) + Upper Mississippi/Illinois (graan, naar de Meren)
    "us-kentucky": "north-america/us/kentucky",
    "us-ohio": "north-america/us/ohio",
    "us-pennsylvania": "north-america/us/pennsylvania",
    "us-west-virginia": "north-america/us/west-virginia",
    "us-indiana": "north-america/us/indiana",
    "us-illinois": "north-america/us/illinois",
    "us-missouri": "north-america/us/missouri",
    "us-iowa": "north-america/us/iowa",
    "us-wisconsin": "north-america/us/wisconsin",
    "us-minnesota": "north-america/us/minnesota",
    # --- uitrol: Rijn/Main/Donau — de drukste binnenvaartas van Europa,
    # Rotterdam tot Constanta over de Main-Donau-Kanaal-verbinding
    "de-nrw": "europe/germany/nordrhein-westfalen",
    "de-rheinland-pfalz": "europe/germany/rheinland-pfalz",
    "de-baden-wuerttemberg": "europe/germany/baden-wuerttemberg",
    "de-bayern": "europe/germany/bayern",
    "de-niedersachsen": "europe/germany/niedersachsen",
    "de-hamburg": "europe/germany/hamburg",
    "zwitserland": "europe/switzerland",
    # Frankrijk staat bij Geofabrik nog in de PRE-2016 regio-indeling: `alsace`
    # bestaat, `normandie` niet (dat is basse-/haute-normandie) — die geeft een
    # bestand van 0 bytes i.p.v. een 404, dezelfde val als de Brazilië-shapefile.
    # Alsace is niet optioneel voor de Rijn: tussen Basel en Straatsburg loopt de
    # vaargeul door het Grand Canal d'Alsace, volledig op Frans grondgebied.
    "fr-alsace": "europe/france/alsace",
    # de Mosel is boven Apach volledig Frans en vormt daaronder de Duits-
    # Luxemburgse grens — beide nodig om tot het kopeinde bij Neuves-Maisons
    # te komen i.p.v. bij de landsgrens af te kappen
    "fr-lorraine": "europe/france/lorraine",
    "luxemburg": "europe/luxembourg",
    "belgie": "europe/belgium",
    "oostenrijk": "europe/austria",
    "slowakije": "europe/slovakia",
    "hongarije": "europe/hungary",
    "kroatie": "europe/croatia",
    "servie": "europe/serbia",
    "roemenie": "europe/romania",
    "bulgarije": "europe/bulgaria",
    # --- uitrol: Zuid-Amerika — de Amazone draagt zeeschepen tot Manaus
    "brazilie": "south-america/brazil",
    "venezuela": "south-america/venezuela",
}


def extract_pad(sleutel):
    return os.path.join(GEOFABRIK, f"{sleutel}-latest.osm.pbf")


def download_extracts(sleutels):
    """Haalt ontbrekende regio-extracts op (~45 MB/s gemeten)."""
    os.makedirs(GEOFABRIK, exist_ok=True)
    for sleutel in sleutels:
        pad = extract_pad(sleutel)
        if os.path.exists(pad):
            print(f"  {sleutel:18s} al aanwezig ({os.path.getsize(pad) / 1048576:,.0f} MB)")
            continue
        if sleutel not in GEOFABRIK_REGIOS:
            raise SystemExit(f"onbekende regio '{sleutel}' — vul GEOFABRIK_REGIOS aan")
        url = f"{GEOFABRIK_BASIS}{GEOFABRIK_REGIOS[sleutel]}-latest.osm.pbf"
        t0 = time.time()
        req = urllib.request.Request(url, headers={
            "User-Agent": "grondstoffen-atlas/M24 (github.com/larswalters/grondstoffen-atlas)"})
        tijdelijk = pad + ".deel"
        with urllib.request.urlopen(req, timeout=180) as r, open(tijdelijk, "wb") as f:
            while True:
                blok = r.read(1 << 20)
                if not blok:
                    break
                f.write(blok)
        os.replace(tijdelijk, pad)   # pas hernoemen als hij compleet is
        mb = os.path.getsize(pad) / 1048576
        print(f"  {sleutel:18s} {mb:7,.0f} MB in {time.time() - t0:4.0f}s")


def segmenten_geofabrik(systeem):
    import osmium  # alleen dit pad heeft het nodig; Overpass draait zonder

    la0, lo0, la1, lo1 = systeem["bbox"]
    marge = 0.15
    wit = set(systeem["namen"])
    cemt_clause = bool(systeem.get("cemt")) and systeem.get("cemt_insluiten", True)
    segs, cemt_gezien = [], {}
    for sleutel in systeem["extracts"]:
        pad = extract_pad(sleutel)
        if not os.path.exists(pad):
            raise SystemExit(f"ontbreekt: {pad}\n  haal 'm op met: "
                             f"python v2/tools/fetch_waterways.py geofabrik --download")
        fp = (osmium.FileProcessor(pad)
              .with_locations()
              .with_filter(osmium.filter.EntityFilter(osmium.osm.WAY))
              .with_filter(osmium.filter.KeyFilter("waterway")))
        for obj in fp:
            tags = obj.tags
            if tags.get("waterway") not in ("river", "canal", "fairway"):
                continue
            naam = tags.get("name", "")
            # spiegelt de twee Overpass-clauses: naam uit de whitelist, of een
            # CEMT-tag maar alléén bij een systeem dat zelf een CEMT-klasse draagt.
            # `cemt_insluiten=False` houdt de klasse als metadata maar zet de
            # clause uit — nodig zodra er kleinere vaarwegen in de bbox liggen
            # die de stitcher als sluiproute kan pakken (de Mosel liep zo bij
            # Nancy door Freycinet-kanalen van klasse I).
            if naam not in wit and not (cemt_clause and tags.get("CEMT")):
                continue
            pts = [(n.location.lon, n.location.lat) for n in obj.nodes
                   if n.location.valid()]
            if len(pts) < 2:
                continue
            if not any(lo0 - marge <= lo <= lo1 + marge and la0 - marge <= la <= la1 + marge
                       for lo, la in pts):
                continue
            segs.append((pts, naam))
            if tags.get("CEMT"):
                cemt_gezien[naam or f"way/{obj.id}"] = tags["CEMT"]
    return segs, cemt_gezien


# ---------------------------------------------------------------- bron: UNECE

def segmenten_bestand(pad, bbox):
    """GeoJSON of shapefile → segmenten binnen de (ruime) bbox."""
    la0, lo0, la1, lo1 = bbox
    marge = 0.15

    def binnen(pts):
        return any(lo0 - marge <= lo <= lo1 + marge and
                   la0 - marge <= la <= la1 + marge for lo, la in pts)

    segs = []
    if pad.lower().endswith((".geojson", ".json")):
        gj = json.load(open(pad, encoding="utf-8"))
        for f in gj.get("features", []):
            g = f.get("geometry") or {}
            props = f.get("properties") or {}
            naam = str(props.get("name") or props.get("NAME") or
                       props.get("Name") or props.get("SECTION_NA") or
                       props.get("EWW") or "")
            delen = []
            if g.get("type") == "LineString":
                delen = [g["coordinates"]]
            elif g.get("type") == "MultiLineString":
                delen = g["coordinates"]
            for deel in delen:
                pts = [(p[0], p[1]) for p in deel]
                if len(pts) >= 2 and binnen(pts):
                    segs.append((pts, naam))
    else:
        import shapefile  # pyshp — alleen nodig voor het shapefile-pad
        sf = shapefile.Reader(pad)
        velden = [f[0] for f in sf.fields[1:]]
        naam_veld = next((v for v in velden if v.lower() in
                          ("name", "naam", "eww", "waterway", "river")), None)
        for sr in sf.iterShapeRecords():
            shp = sr.shape
            if shp.shapeTypeName not in ("POLYLINE", "POLYLINEZ", "POLYLINEM"):
                continue
            naam = str(sr.record[velden.index(naam_veld)]) if naam_veld else ""
            grenzen = list(shp.parts) + [len(shp.points)]
            for i in range(len(grenzen) - 1):
                pts = [(p[0], p[1]) for p in shp.points[grenzen[i]:grenzen[i + 1]]]
                if len(pts) >= 2 and binnen(pts):
                    segs.append((pts, naam))
    return segs


# ---------------------------------------------------------------- stitcher

def kortste_waterpad(segs, anker_zee, anker_binnen, stitch_km):
    """Dijkstra over de segment-geometrie: zeezijde -> binnenzijde.

    Elke vertex is een graaf-knoop; opeenvolgende vertices van een segment zijn
    verbonden. Segment-UITEINDEN worden daarnaast gehecht aan elke vertex
    binnen stitch_km (bronnen delen niet altijd exacte knopen). Het resultaat
    is de kortste route over écht getekende waterweg-geometrie — takken en
    parallelle armen vallen er vanzelf uit.
    """
    knopen = []          # (lon, lat)
    knoop_id = {}
    buren = []           # per knoop: list[(buur, km, segment-index)]

    def nid(p):
        sleutel = (round(p[0], 6), round(p[1], 6))
        if sleutel not in knoop_id:
            knoop_id[sleutel] = len(knopen)
            knopen.append(sleutel)
            buren.append([])
        return knoop_id[sleutel]

    uiteinden = []
    for si, (pts, _naam) in enumerate(segs):
        vorige = None
        for j, p in enumerate(pts):
            k = nid(p)
            if vorige is not None and vorige != k:
                d = km(knopen[vorige], knopen[k])
                buren[vorige].append((k, d, si))
                buren[k].append((vorige, d, si))
            if j == 0 or j == len(pts) - 1:
                uiteinden.append(k)
            vorige = k

    # uiteinden hechten aan nabije vertices (grid-hash, cel ~ stitch-tolerantie)
    cel_graden = max(stitch_km / 70.0, 1e-4)
    grid = {}
    for i, (lo, la) in enumerate(knopen):
        grid.setdefault((int(lo / cel_graden), int(la / cel_graden)), []).append(i)

    def dichtbij(i, straal_km):
        lo, la = knopen[i]
        cx, cy = int(lo / cel_graden), int(la / cel_graden)
        r = max(1, int(straal_km / (cel_graden * 70.0)) + 1)
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1):
                for j in grid.get((cx + dx, cy + dy), ()):
                    if j != i:
                        yield j

    for i in set(uiteinden):
        for j in dichtbij(i, stitch_km):
            d = km(knopen[i], knopen[j])
            if d <= stitch_km:
                buren[i].append((j, d, -1))
                buren[j].append((i, d, -1))

    def dichtstbij(anker):
        beste, beste_d = -1, 1e18
        for i, p in enumerate(knopen):
            d = km(anker, p)
            if d < beste_d:
                beste, beste_d = i, d
        return beste, beste_d

    start, d_start = dichtstbij(anker_zee)
    doel, d_doel = dichtstbij(anker_binnen)
    if d_start > ANKER_TOL_KM or d_doel > ANKER_TOL_KM:
        raise RuntimeError(
            f"anker te ver van de geometrie: zee {d_start:.1f} km, binnen {d_doel:.1f} km "
            f"(tolerantie {ANKER_TOL_KM} km) — bbox/namenlijst dekt het traject niet")

    afstand = {start: 0.0}
    vorige = {}
    via_seg = {}
    pq = [(0.0, start)]
    klaar = set()
    while pq:
        d, k = heapq.heappop(pq)
        if k in klaar:
            continue
        klaar.add(k)
        if k == doel:
            break
        for buur, dd, si in buren[k]:
            nd = d + dd
            if nd < afstand.get(buur, 1e18):
                afstand[buur] = nd
                vorige[buur] = k
                via_seg[buur] = si
                heapq.heappush(pq, (nd, buur))
    if doel not in klaar:
        raise RuntimeError("geen doorlopend waterpad tussen de ankers gevonden "
                           "(stitch-tolerantie of dekking te krap)")

    pad = [doel]
    seg_volgorde = []
    k = doel
    while k != start:
        seg_volgorde.append(via_seg.get(k, -1))
        k = vorige[k]
        pad.append(k)
    pad.reverse()
    seg_volgorde.reverse()

    coords = [knopen[k] for k in pad]
    namen = []
    for si in seg_volgorde:
        naam = segs[si][1] if si >= 0 else None
        if naam and (not namen or namen[-1] != naam):
            namen.append(naam)
    return coords, afstand[doel], namen, (d_start, d_doel)


# ---------------------------------------------------------------- simplify

def simplify(pts, tol_km=SIMPLIFY_KM):
    """Douglas-Peucker (vlakke benadering met cos(lat) — prima op NL-schaal)."""
    if len(pts) < 3:
        return list(pts)
    coslat = math.cos(math.radians(sum(p[1] for p in pts) / len(pts)))

    def afstand_lijn(p, a, b):
        ax, ay = (a[0] - p[0]) * coslat, a[1] - p[1]
        bx, by = (b[0] - p[0]) * coslat, b[1] - p[1]
        dx, dy = bx - ax, by - ay
        den = math.hypot(dx, dy)
        if den < 1e-12:
            return math.hypot(ax, ay) * 111.2
        return abs(ax * dy - ay * dx) / den * 111.2

    houd = [False] * len(pts)
    houd[0] = houd[-1] = True
    stapel = [(0, len(pts) - 1)]
    while stapel:
        i, j = stapel.pop()
        if j <= i + 1:
            continue
        verste, verste_d = -1, -1.0
        for k in range(i + 1, j):
            d = afstand_lijn(pts[k], pts[i], pts[j])
            if d > verste_d:
                verste, verste_d = k, d
        if verste_d > tol_km:
            houd[verste] = True
            stapel.append((i, verste))
            stapel.append((verste, j))
    return [p for p, h in zip(pts, houd) if h]


# ---------------------------------------------------------------- hoofdflow

def _feature(systeem, bron, coords, lengte, route):
    """Uitvoer-feature; beide paden (lijn-stitch en vlak-afleiding) delen 'm."""
    return {
        "type": "Feature",
        "properties": {
            "label": systeem["label"],
            "zeevaart": systeem["zeevaart"],
            "cemt": systeem["cemt"],
            "volgtOp": systeem.get("volgt_op", ""),
            "sluitAan": systeem.get("sluit_aan", ""),
            "bron": bron,
            "km": round(lengte, 1),
            "route": route,
            "ankerZee": list(systeem["anker_zee"]),
            "ankerBinnen": list(systeem["anker_binnen"]),
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [[round(lo, 6), round(la, 6)] for lo, la in coords],
        },
    }


def haal(bron, bestand=None, alleen=None):
    features = []
    systemen = [s for s in SYSTEMEN if not alleen or s["label"] in alleen]
    if alleen:
        onbekend = set(alleen) - {s["label"] for s in SYSTEMEN}
        if onbekend:
            raise SystemExit(f"onbekende labels: {sorted(onbekend)}")
    for systeem in systemen:
        label = systeem["label"]
        print(f"\n[{label}] bron={bron}")
        # Brede rivieren hebben geen benoemde middellijn in OSM (de Amazone is
        # tussen Manaus en Belém >10 km breed en staat als wátervlak gemapt).
        # Zo'n systeem wordt niet gestitcht uit lijnen maar AFGELEID uit de
        # vlakken; de rest van de pijplijn merkt het verschil niet.
        if systeem.get("vlakken"):
            from middellijn_uit_vlakken import afleiden
            v = systeem["vlakken"]
            strak, lengte, klaringen = afleiden(
                v.get("extracts") or systeem["extracts"],
                systeem["bbox"], systeem["anker_zee"], systeem["anker_binnen"],
                cel_graden=v.get("cel", 0.004),
                min_klaring=v.get("min_klaring", 0.15),
                simplify_km=v.get("simplify_km", 0.25))
            kl = sorted(klaringen)
            # bron = altijd de extract, ongeacht de gekozen --bron: een
            # vlakken-systeem komt nooit via Overpass binnen (attributie!)
            features.append(_feature(systeem, "geofabrik", strak, lengte,
                                     f"afgeleid uit watervlakken (klaring mediaan "
                                     f"{kl[len(kl) // 2]:.2f} km, min {kl[0]:.2f})"))
            continue

        if bron == "osm":
            segs, cemt_gezien = segmenten_osm(systeem)
        elif bron == "geofabrik":
            if not systeem.get("extracts"):
                raise SystemExit(f"{label}: geen 'extracts' opgegeven — vul de regio('s) in")
            segs, cemt_gezien = segmenten_geofabrik(systeem)
        else:
            if not bestand:
                raise SystemExit("unece vereist --bestand <pad naar geojson/shapefile>")
            segs, cemt_gezien = segmenten_bestand(bestand, systeem["bbox"]), {}
        print(f"  segmenten: {len(segs)} · vertices: {sum(len(p) for p, _ in segs):,}")
        if not segs:
            raise RuntimeError(f"geen segmenten voor {label} — dekking/filters checken")

        coords, lengte, namen, anker_d = kortste_waterpad(
            segs, systeem["anker_zee"], systeem["anker_binnen"], STITCH_KM[bron])
        strak = simplify(coords)
        print(f"  pad: {lengte:.1f} km · {len(coords)} punten → {len(strak)} na simplify"
              f" · anker-afstanden zee {anker_d[0]:.2f} / binnen {anker_d[1]:.2f} km")
        if namen:
            print(f"  route: {' → '.join(namen[:12])}{' …' if len(namen) > 12 else ''}")
        if cemt_gezien:
            uniek = sorted(set(cemt_gezien.values()))
            print(f"  CEMT-tags gezien: {', '.join(uniek)}")

        features.append(_feature(systeem, bron, strak, lengte, " → ".join(namen)))

    os.makedirs(CACHE, exist_ok=True)
    achtervoegsel = f"_{'-'.join(sorted(alleen))}" if alleen else ""
    pad = os.path.join(CACHE, f"vaarwegen_{bron}{achtervoegsel}.geojson")
    bronvermelding = {
        "osm": "OpenStreetMap contributors (ODbL) via Overpass API",
        "geofabrik": "OpenStreetMap contributors (ODbL) via Geofabrik-regio-extract",
    }.get(bron, "UNECE Blue Book database — E-waterway network (gis.unece.org)")
    with open(pad, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection",
                   "bron": bronvermelding,
                   "features": features}, f, ensure_ascii=False)
    print(f"\ngeschreven: {pad} ({os.path.getsize(pad) / 1024:.0f} KB)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("bron", choices=["osm", "geofabrik", "unece"])
    ap.add_argument("--bestand", help="unece: pad naar geojson of shapefile")
    ap.add_argument("--download", action="store_true",
                    help="geofabrik: haal ontbrekende regio-extracts eerst op")
    ap.add_argument("--alleen", help="komma-gescheiden labels i.p.v. alle systemen "
                                     "(schrijft naar een eigen bestand — handig om te vergelijken)")
    args = ap.parse_args()
    alleen = [s.strip() for s in args.alleen.split(",")] if args.alleen else None
    if args.download:
        nodig = sorted({r for s in SYSTEMEN if not alleen or s["label"] in alleen
                        for r in s.get("extracts", [])})
        print(f"regio-extracts ophalen ({len(nodig)}):")
        download_extracts(nodig)
    haal(args.bron, args.bestand, alleen)