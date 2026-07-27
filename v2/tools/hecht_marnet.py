# hecht_marnet.py — DE ZEEKANT VAN DE TRACK-GRAAF (M28, vervolg op LAR-530).
#
# Besluit Lars (M28): **open zee blijft definitief MARNET**; kust, riviermonding,
# binnenwater en havens komen uit echte AIS-tracks. Dan moet er één plek zijn
# waar die twee elkaar raken. Dit bestand bouwt die aanhechting — en niets meer.
#
# ── WAT ER NIET GEBEURT ────────────────────────────────────────────────────
# * marnet.bin / marnet.json worden NIET aangeraakt en NIET teruggezet in
#   v2/data/ (de "schone bol"-beslissing van M27 blijft staan). Ze worden van
#   de backup-tag gelezen:
#       git show pre-ais-net:v2/data/marnet.json > <map>/marnet.json
#       git show pre-ais-net:v2/data/marnet.bin  > <map>/marnet.bin
# * Er wordt GEEN MARNET-edge geknipt, geen MARNET-knoop verplaatst, geen
#   MARNET-id verschoven.
# * Er wordt GEEN trackpunt verplaatst. De aanhechting is een EXTRA edge naast
#   twee onveranderde netten.
#
# ── DE OVERLAPZONE IS GEMETEN, NIET AANGENOMEN (subcommando `overlap`) ─────
# De spec noemt "40-80 km de zee op". Dat klopt voor geen enkele bron: het
# verschilt met een factor 100. Gemeten over alle 119,1 mln trackpunten (134 s):
#
#   bron               zeepunten   max zee-km per track      tracks > 40 km
#                                  p50    p90    p99    max
#   vs-landelijk        51,2%      6,2  120,7  589,9  2045,3     71.823
#   dk-landelijk        86,4%      7,2   50,0  186,3   388,8     21.535
#   no-corridors        56,6%      3,3    8,7   20,0    20,8          0
#   wereld-collector    58,1%      7,2   51,8  224,9   851,6      3.628
#
# Dus: MarineCadastre loopt tot 2.045 km de oceaan op (11.298 tracks verder dan
# 300 km), DMA tot 389 km, de collector tot 852 km — en Kystdatahuset komt
# NERGENS verder dan 20,8 km uit de kust. Er is geen enkele "de" overlapzone;
# per bron is hij anders, en voor NO is hij er praktisch niet.
#
# Wat dat voor de aanhechting betekent, en dat is de eigenlijke uitkomst:
# ver de zee op lopen levert niets op als MARNET daar geen KNOOP heeft.
# Afstand van een zeetrackpunt tot MARNET-zee, mediaan:
#   bron              tot de LIJN   tot een VERTEX   tot een KNOOP
#   vs-landelijk         5,98 km        6,5 km         16,3 km
#   dk-landelijk         5,67           6,3            16,7
#   no-corridors         1,22           3,0             5,1
#   wereld-collector     4,09           4,9            13,5
# Aandeel zeepunten binnen 0,5 km van de MARNET-LIJN: VS 11,0% · DK 5,9% ·
# NO 27,1% · collector 10,5%. De overlap is dus reëel maar dun, en hij zit bij
# de kust — niet 40-80 km uit de wal, maar daar waar MARNET zijn haven- en
# aanloopknopen heeft.
#
# ── DE REGEL: RAAKPUNT, GEEN SNAP ──────────────────────────────────────────
# Een MARNET-ZEE-KNOOP wordt een knoop in het gecombineerde net als er een
# knoop van de track-graaf binnen EPS van hem ligt. De verbinding is één
# connector-edge tussen die twee ECHTE coördinaten, met de gemeten afstand als
# lengte. Meer niet. Geen kandidaat -> geen aanhechting.
#
# Waarom deze regel geen verbinding maakt die er niet is — vier gronden, elk
# apart weerlegbaar:
#
# 1. ER IS GEEN TERUGVAL. Er bestaat geen "en anders de dichtstbijzijnde knoop,
#    hoe ver ook". Dat is precies de schuine snap over 50 km die de opdracht
#    verbiedt, en het is dezelfde fout als de absolute havensnap die
#    Whitby/Rostock 58 km wegteleporteerde (Karlsruhe-klasse, 2026-07-24).
#    Een MARNET-knoop zonder trackdekking blijft onaangehecht en wordt als
#    zodanig gerapporteerd — zoals het Wesel-gat open blijft.
#
# 2. EPS LIGT ONDER DE EIGEN RAAK-TOLERANTIE VAN DE GRAAF. De track-graaf noemt
#    twee tracks "rakend" als ze dezelfde ~200 m-cel delen; twee zulke punten
#    liggen tot ~0,28 km uit elkaar. EPS = 0,5 km is dus nauwelijks meer dan
#    wat de graaf intern al als één plek telt, en kleiner dan de kortste edge
#    die de graaf maakt (--min-seg-km 0,5). Het bewijs onder de connector is
#    een ECHTE scheepspositie: daar voer een schip, en MARNET zegt dat daar een
#    vaarlaan-knoop ligt.
#
# 3. VERLENGEN, NIET VERPLAATSEN. De landnet-heal leerde dat een uiteinde
#    verplaatsen samenvallende punten lostrekt (de EMO-flip-flop: dezelfde naad
#    zes rondes gelegd en losgetrokken, eindstand los). Hier verschuift niets:
#    beide coördinaten blijven exact staan en er komt een edge bij. De
#    aanhechting is daarmee per constructie idempotent — nog een keer draaien
#    geeft dezelfde connectors.
#
# 4. DE CONNECTOR WORDT OP LAND GETOETST. Een connector die de kustlijn
#    (ne_10m_land + ne_10m_minor_islands, dezelfde 1:10M-wereld die de bol
#    tekent) snijdt gaat weg. Bij 0,5 km is dat zeldzaam — en juist daarom is
#    het een toets die iets kan weerleggen in plaats van een geruststelling.
#
# En de RELATIEVE weging, op de twee plekken waar hij hoort (les 2026-07-24):
#   * connector: van de graafknopen binnen EPS wint een knoop in de HOOFD-
#     component, mits die niet meer dan 2x + 0,1 km verder ligt dan de absoluut
#     dichtste. Anders hangt MARNET aan een snipper van twee tracks.
#   * havensnap: een haven snapt naar de dichtstbijzijnde halte in de
#     hoofdcomponent onder dezelfde relatieve regel, nooit absoluut.
#
# ── DE OVERSTAP TRACK -> MARNET KOST WAT EEN TRACK-WISSEL KOST ─────────────
# Een aanhechting die gratis is, is niet neutraal. Gemeten op Houston -> Mobile
# (894,5 km echte trackgeometrie beschikbaar, MARNET-laan ernaast):
#
#   boete 0    km -> 944,6 km · 19 MARNET-edges · dijkstra 969,3   <- MARNET
#   boete 0,1  km -> 944,6 km · 19 MARNET-edges · dijkstra 969,5   <- MARNET
#   boete 0,25 km -> 894,5 km ·  0 MARNET-edges · dijkstra 969,5   <- tracks
#   boete 0,5 / 1 / 2 / 5 / 10 / 25 / 100 / 1000 -> 894,5 km, exact dezelfde route
#
# Zonder prijs wint dus een route die 50,1 km LANGER is in echte geometrie, en
# hij wint met 0,2 km op een dijkstra-kost van 969 — 0,02%, een muntworp. De
# oorzaak is structureel: een track-wissel kost 25 km boete (die curve is in
# bouw_trackgraaf gemeten), een MARNET-laan kost niets, dus 822 km modellijn
# verslaat 894 km waargenomen lijn zodra er drie wissels in zitten.
#
# De default is daarom OVERSTAP_BOETE (25 km) — niet als afregeling maar als de
# CONSISTENTE prijs: de boete drukt uit dat een gestitchte route zwakker bewijs
# is dan één doorvaart, en een MARNET-laan is een gemodelleerde lijn, dus
# zwakker bewijs dan een waargenomen doorvaart. Het plateau loopt van 0,25 tot
# >= 1000 km (factor 4.000); 25 ligt daar diep in. ⚠️ Hermeet deze curve als de
# tracksets of de overstap-boete veranderen — het is één commando per punt.
# Wat de boete NIET doet: hij verandert geen enkele gerapporteerde lengte (die
# blijft de lengte van de getekende lijn) en hij sluit MARNET nergens af — waar
# geen trackalternatief is (New Orleans -> Rotterdam) verandert er niets.
#
# ── WAAROM AAN KNOPEN EN NIET AAN DE MARNET-LIJN ───────────────────────────
# Gemeten: MARNET-zee heeft 9.633 knopen en 289.568 geometrie-vertices op
# 2.656.757 km — 9,17 km per vertex. Die tussenvertices zijn GROOTCIRKEL-
# VERDICHTING uit de M23-bake (edges zijn op 10 km verdicht), dus berekende
# punten, geen waargenomen geometrie. Aanhechten daaraan zou "op echte
# geometrie hechten" heten terwijl het op interpolatie hecht. De knopen zijn
# het enige in MARNET dat uit de bron komt: het zijn de laan-juncties.
# Prijs die we daarvoor betalen, en die eerlijk in de uitslag staat: de mediane
# afstand van een zeetrackpunt tot de MARNET-LIJN is 4-6 km maar tot een
# MARNET-KNOOP 13-17 km, dus we hechten op minder plekken dan theoretisch kan.
#
# ── DRAAIEN ────────────────────────────────────────────────────────────────
#   python v2/tools/hecht_marnet.py hecht --graaf .../mississippi \
#       --marnet <map met marnet.bin/json> --eps 0.5
#   python v2/tools/hecht_marnet.py havens --graaf .../mississippi --marnet <map>
#   python v2/tools/hecht_marnet.py regressie --graaf .../mississippi \
#       --marnet <map> --van neworleans --naar vidalia
#   python v2/tools/hecht_marnet.py overlap --tracks *.jsonl.gz --marnet <map> \
#       --ne v2/build-cache --uit v2/build-cache/ais/graaf/overlapzone.json
#
# ── UITKOMST OP DE TWEE ACCEPTATIECORRIDORS (eps 0,5 km) ───────────────────
#                                        Mississippi        Rijn
#   aangehechte MARNET-knopen                    99          18
#   connector-lengte  p50 / max          0,095/0,452  0,111/0,458 km
#   totaal connector-geometrie                13,13        2,77 km
#   MARNET-knopen bereikbaar vanaf de kade  9.630/9.679 (99,5%) — beide
#   componenten voor -> na                   89 -> 90    45 -> 46
#   havensnap VERPLAATST door de aanhechting   0/115       0/74
#   havens die MARNET bereiken via tracks      87/115      58/74
#   havens dichter aan het net dan voor        72/115      39/74
#     mediane snap voor (MARNET) -> na (track) 17,13 -> 0,747   15,40 -> 0,505 km
#
# REGRESSIE (de eis): New Orleans -> Vidalia is voor én na
#   645 edges · 1.363 punten · 432,311 km — EDGE-reeks identiek, PUNTEN-reeks
#   identiek, verschil +0,000000 km, en 1.363/1.363 punten nog steeds letterlijk
#   gelijk aan het brontrackpunt. Ook bij eps 1/2/5/10 km ongewijzigd, en dat is
#   geen verdienste van eps maar structureel: MARNET-zee reikt in deze corridor
#   tot lat 30,295 (Mississippi Sound) en de rivier erboven zit in de BULKLAAG,
#   die per definitie buiten dit net valt.
#   Beide geulen om Profit Island: voor en na identiek — geul 1 12,90 km, geul 2
#   11,69 km, gedeelde knopen 153306 (beneden) en 153708 (boven). GESLAAGD.
#   Wesel blijft open: EMO -> Schwelgern geeft voor én na GEEN PAD.
#
# NIET-VACUÜM-CONTROLE (anders bewijst die regressie niets):
#   New Orleans -> Rotterdam: VOOR geen pad · NA 8.968,1 km = 30,1 km echte
#     trackgeometrie + 0,036 km connector + 8.937,8 km MARNET.
#   EMO (Maasvlakte) -> Shanghai: VOOR geen pad · NA 19.606,0 km = 19,1 km track
#     + 0,055 km connector + 19.586,2 km MARNET. De vastgelegde invariant van
#     het project is R'dam -> Shanghai 19.610 km: **-0,02%**, vanaf een ándere
#     kade en dwars door de aanhechting heen. Dat is de scherpste controle dat
#     de keten track -> connector -> MARNET klopt.

import argparse
import gzip
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.spatial import cKDTree

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bouw_trackgraaf as G                                   # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

R_AARDE = 6371.0088
EPS_KM = 0.5              # raak-tolerantie; zie grond 2 in de kop
REL_FACTOR = 2.0          # relatieve voorkeur hoofdcomponent (bak_havens-patroon)
REL_MARGE = 0.1


# ── MARNET lezen ───────────────────────────────────────────────────────────
# Formaat afgelezen uit v2/src/marnet.js op tag pre-ais-net:
#   blok 1 knopen (delta lon/lat, zigzag-varint / schaal)
#   blok 2 per edge: a, b (delta t.o.v. vorige), lengte(0,1 km), soort,
#          aantal punten, gabarietvlag (1 -> vier extra varints)
#   blok 3 per edge de geometrie als delta's; punt 1 = knoop a

def lees_marnet(map_pad):
    map_pad = Path(map_pad)
    meta = json.loads((map_pad / "marnet.json").read_text(encoding="utf-8"))
    buf = (map_pad / "marnet.bin").read_bytes()
    p = 0

    def nxt():
        nonlocal p
        res, factor = 0, 1
        while True:
            b = buf[p]
            p += 1
            res += (b & 0x7F) * factor
            if not (b & 0x80):
                break
            factor *= 128
        half = res // 2
        return half if res % 2 == 0 else -half - 1

    schaal = meta["schaal"]
    nk, ne = meta["knopen"], meta["edges"]
    knoop_lon = np.empty(nk)
    knoop_lat = np.empty(nk)
    x = y = 0
    for i in range(nk):
        x += nxt()
        y += nxt()
        knoop_lon[i] = x / schaal
        knoop_lat[i] = y / schaal
    e_a = np.empty(ne, np.int64)
    e_b = np.empty(ne, np.int64)
    e_km = np.empty(ne)
    e_soort = np.empty(ne, np.uint8)
    e_n = np.empty(ne, np.int64)
    a = b = 0
    for i in range(ne):
        a += nxt()
        b += nxt()
        e_a[i], e_b[i] = a, b
        e_km[i] = nxt() / 10.0
        e_soort[i] = nxt()
        e_n[i] = nxt()
        if nxt() == 1:
            for _ in range(4):
                nxt()
    npt = meta["punten"]
    g_lon = np.empty(npt)
    g_lat = np.empty(npt)
    g_start = np.empty(ne + 1, np.int64)
    pi = 0
    for e in range(ne):
        g_start[e] = pi
        gx = round(knoop_lon[e_a[e]] * schaal)
        gy = round(knoop_lat[e_a[e]] * schaal)
        for k in range(e_n[e]):
            if k > 0:
                gx += nxt()
                gy += nxt()
            g_lon[pi] = gx / schaal
            g_lat[pi] = gy / schaal
            pi += 1
    g_start[ne] = pi
    return {"meta": meta, "knoop_lon": knoop_lon, "knoop_lat": knoop_lat,
            "edge_a": e_a, "edge_b": e_b, "edge_km": e_km,
            "edge_soort": e_soort, "edge_n": e_n,
            "geom_lon": g_lon, "geom_lat": g_lat, "geom_start": g_start}


def marnet_zee(m, vermijd=("northwest",)):
    """Het ZEENET van MARNET = alles BEHALVE de bulk-rivierlaag.

    ⚠️ NIET "soort == 0", en dat is gemeten in plaats van aangenomen. Van de
    60.293 soort-1-edges horen er 60.200 (407.870 km) bij de BULKLAAG — de
    mechanisch gefilterde rivierlaag van LAR-515, en precies wat M28 door
    tracks vervangt. De overige 93 (3.546 km) zijn de binnenwater-ZONES die
    M23 als-is bewaarde: Panama (2), Suez (3 van de 5 canal-edges!),
    Saint-Laurent/Seaway, Wolga-Don, Mississippi-delta, Elbe, Gironde, Severn,
    Hooghly, Paraná, Congo, Columbia, Maracaibo. Die zijn geen binnenvaart maar
    ZEEROUTE-infrastructuur.
    Met een kale "soort == 0"-filter knip je Suez en Panama doormidden, en dat
    zie je niet aan een foutmelding maar aan een lengte: Rotterdam -> Shanghai
    kwam uit op 25.020 km (om Kaap de Goede Hoop) i.p.v. de vastgelegde 19.610.
    Dat getal IS de toets — zie ijk_marnet.py: met deze definitie reproduceert
    de lezer 19.610 km en Duluth -> Rotterdam 8.031 km, beide op 0,00%.

    `vermijd` = de passage-restricties uit M23. Default `northwest`, exact
    zoals de browser-router (v2/src/router.js) en searoute zelf: zonder die
    restrictie is het kortste graafpad niet de commerciële route en kiest
    Rotterdam -> Shanghai de Noordwest-Passage."""
    meta = m["meta"]
    bulk = np.zeros(len(m["edge_km"]), bool)
    for v in (meta.get("vaarwegen") or {}).values():
        if v.get("bulk"):
            for e in v.get("edges", ()):
                if e < len(bulk):
                    bulk[e] = True
    zee = ~bulk
    pas = meta.get("passages", {})
    if vermijd:
        vermijd = set(vermijd)
        dicht = np.array([int(k) for k, v in pas.items() if v in vermijd],
                         dtype=np.int64)
        if len(dicht):
            zee[dicht[dicht < len(zee)]] = False
    ids = np.unique(np.concatenate([m["edge_a"][zee], m["edge_b"][zee]]))
    her = -np.ones(len(m["knoop_lat"]), np.int64)
    her[ids] = np.arange(len(ids))
    e = np.flatnonzero(zee)
    z = {"knoop_id": ids, "her": her,
         "lat": m["knoop_lat"][ids], "lon": m["knoop_lon"][ids],
         "edge": e, "a": her[m["edge_a"][e]], "b": her[m["edge_b"][e]],
         "km": m["edge_km"][e]}
    n = len(ids)
    M = csr_matrix((np.r_[z["km"], z["km"]],
                    (np.r_[z["a"], z["b"]], np.r_[z["b"], z["a"]])), shape=(n, n))
    nc, lab = connected_components(M, directed=False)
    z["componenten"], z["label"] = nc, lab
    z["hoofd"] = int(np.argmax(np.bincount(lab)))
    return z


# ── meetkunde ──────────────────────────────────────────────────────────────

def seg_km_wrap(la, lo):
    """Segmentlengtes langs een puntenreeks, met het lengteverschil gewikkeld
    naar [-180, 180].

    ⚠️ Nodig zodra MARNET meedoet, en dat is gemeten: twee zee-edges lopen over
    de datumgrens (edge 32 op lat 70,0 en edge 3160 op lat 59,6-62,1, allebei
    lon -180,00..179,85). Met een kaal lengteverschil leest edge 3160 als
    19.492 km terwijl hij 761,6 km is, en werd Rotterdam -> Shanghai 47.938 km
    i.p.v. ~19.600. De track-kant kan dit niet hebben (tracks zijn kort), dus
    bouw_trackgraaf.seg_km_np heeft het terecht niet — hier wel."""
    dlat = np.radians(la[1:] - la[:-1])
    dlon_deg = (lo[1:] - lo[:-1] + 180.0) % 360.0 - 180.0
    dlon = np.radians(dlon_deg) * np.cos(np.radians((la[1:] + la[:-1]) * 0.5))
    return 6371.0 * np.hypot(dlat, dlon)


def xyz(lat, lon):
    la, lo = np.radians(np.asarray(lat, float)), np.radians(np.asarray(lon, float))
    c = np.cos(la)
    return np.column_stack([c * np.cos(lo), c * np.sin(lo), np.sin(la)])


def boog_km(koorde):
    return 2.0 * R_AARDE * np.arcsin(np.clip(koorde, 0.0, 2.0) / 2.0)


def _ringen(pad):
    d = json.loads(Path(pad).read_text(encoding="utf-8"))
    uit = []
    for ft in d["features"]:
        g = ft["geometry"]
        polys = (g["coordinates"] if g["type"] == "MultiPolygon"
                 else [g["coordinates"]])
        for pl in polys:
            uit.append(pl)
    return uit


_LAND_CACHE = {}


def landtoets(paden, connectors, knoop_ll, marnet_ll):
    """Snijdt een connector de kustlijn? Zo ja: weg — MAAR alleen als de toets
    daar iets kán zeggen. (grond 4 in de kop)

    ⚠️ DE EERSTE VERSIE VAN DEZE TOETS VERWIERP PRECIES DE JUISTE CONNECTORS,
    en dat is gemeten, niet vermoed. Op de Rijn viel 10 van de 18 kandidaten af,
    op de Mississippi 39 van de 89. In ELK van die gevallen lagen BEIDE
    uiteinden binnen de landpolygoon: het havenbekken van Rotterdam, de passen
    van de Mississippi-delta, het Houston Ship Channel, Calcasieu. De 1:10M-kust
    kent die vaarwegen simpelweg niet — dezelfde vondst die in M24 de vlak-toets
    door de corridor-toets liet vervangen ("rivieren/kanalen bestaan niet als
    water in de NE-polygonen") en die M23 al opving met de aanloop-klasse
    (<= 5 km van een knoop = dokbekken/riviermond, geldig).

    Dus: de toets VERWERPT alleen als beide uiteinden aantoonbaar in water
    liggen en de lijn ertussen tóch land raakt — dat is de echte foutmodus, een
    connector dwars over een landtong. Ligt een uiteinde in de landpolygoon, dan
    ONTHOUDT de toets zich en zegt dat ook: daar is de 1:10M-kust te grof om
    iets te weerleggen, terwijl twee onafhankelijke bronnen (een MARNET-
    laanknoop én een echte scheepspositie) zeggen dat er water is.
    Onthouden wordt geteld en gerapporteerd, niet stilzwijgend als 'geslaagd'.
    """
    from shapely.geometry import LineString, Point, Polygon
    from shapely import STRtree
    sleutel = tuple(str(p) for p in paden)
    if sleutel not in _LAND_CACHE:                 # de eps-reeks draait 8x
        polys = []
        for pad in paden:
            for pl in _ringen(pad):
                try:
                    polys.append(Polygon(pl[0], pl[1:]))
                except Exception:
                    pass
        _LAND_CACHE[sleutel] = (polys, STRtree(polys))
    polys, boom = _LAND_CACHE[sleutel]

    def in_land(pt):
        return any(polys[j].contains(pt) for j in boom.query(pt))

    weg, onthouden = [], []
    for i, (mk, gk, d) in enumerate(connectors):
        pm = Point(marnet_ll[mk][1], marnet_ll[mk][0])
        pg = Point(knoop_ll[gk][1], knoop_ll[gk][0])
        if in_land(pm) or in_land(pg):
            onthouden.append(i)
            continue
        ln = LineString([pm, pg])
        for j in boom.query(ln):
            if polys[j].intersects(ln):
                weg.append(i)
                break
    return set(weg), set(onthouden)


# ── de aanhechting ─────────────────────────────────────────────────────────

def bouw_connectors(graaf, router, z, eps_km, ne_map=None, stil=False):
    """Voor elke MARNET-zee-knoop: de graafknoop binnen eps, relatief gewogen
    naar de hoofdcomponent. Geen kandidaat -> geen aanhechting."""
    gk_lat, gk_lon = graaf["knoop_lat"], graaf["knoop_lon"]
    boom = cKDTree(xyz(gk_lat, gk_lon))
    # component-label per GRAAFKNOOP (uit de halte-componenten van de router)
    nc, lab_h = connected_components(router["M"], directed=False)
    maten = np.bincount(lab_h)
    hoofd_h = int(np.argmax(maten))
    knoop_hoofd = np.zeros(len(gk_lat), bool)
    knoop_hoofd[router["h_knoop"][lab_h == hoofd_h]] = True

    P = xyz(z["lat"], z["lon"])
    straal = 2.0 * np.sin(min(eps_km, 500.0) / (2 * R_AARDE))    # koorde
    buren = boom.query_ball_point(P, r=straal, workers=-1)
    ruw = []
    for mi, lijst in enumerate(buren):
        if not lijst:
            continue
        idx = np.asarray(lijst, np.int64)
        d = boog_km(np.linalg.norm(xyz(gk_lat[idx], gk_lon[idx]) - P[mi], axis=1))
        j_dicht = int(np.argmin(d))
        keus, dkeus = int(idx[j_dicht]), float(d[j_dicht])
        # RELATIEVE voorkeur voor de hoofdcomponent
        in_hoofd = knoop_hoofd[idx]
        if not knoop_hoofd[keus] and in_hoofd.any():
            kand = np.flatnonzero(in_hoofd)
            j2 = kand[int(np.argmin(d[kand]))]
            if d[j2] <= REL_FACTOR * dkeus + REL_MARGE:
                keus, dkeus = int(idx[j2]), float(d[j2])
        ruw.append((mi, keus, dkeus))

    verworpen_land, onthouden = set(), set()
    if ne_map and ruw:
        ne_map = Path(ne_map)
        verworpen_land, onthouden = landtoets(
            [ne_map / "ne_10m_land.geojson",
             ne_map / "ne_10m_minor_islands.geojson"],
            ruw, list(zip(gk_lat, gk_lon)), list(zip(z["lat"], z["lon"])))
    conn = [c for i, c in enumerate(ruw) if i not in verworpen_land]
    if not stil:
        print(f"  kandidaten binnen {eps_km} km: {len(ruw):,} van "
              f"{len(z['lat']):,} MARNET-zee-knopen")
        print(f"  landtoets: {len(ruw)-len(verworpen_land)-len(onthouden)} "
              f"getoetst en goed · {len(verworpen_land)} VERWORPEN (kruist land "
              f"terwijl beide uiteinden in water liggen) · {len(onthouden)} "
              f"onthouden (een uiteinde ligt binnen de 1:10M-landpolygoon — "
              f"havenbekken/deltapas; daar kan deze toets niets weerleggen)")
    return conn, knoop_hoofd, {"verworpen": verworpen_land,
                               "onthouden": onthouden}


# ── gecombineerde router ───────────────────────────────────────────────────
# haltes 0..n_track-1     = de track-haltes van bouw_trackgraaf.bouw_router
# haltes n_track..        = de MARNET-zee-knopen
# boog-eid:  >= 0  track-edge · -1 track-overstapspaak
#            -2-k  MARNET-boog k (in mar_arc: ('marnet', edge_ix) of
#                  ('connector', mi, gk, km))

def bouw_gecombineerd(graaf, cache, router, z, conn, boete_connector=0.0,
                      stil=True):
    t0 = time.monotonic()
    n_t = router["n_h"]
    n_m = len(z["lat"])
    n = n_t + n_m
    h_lat = np.concatenate([router["h_lat"], z["lat"]])
    h_lon = np.concatenate([router["h_lon"], z["lon"]])

    # bestaande bogen overnemen
    b_from = router["boog_sleutel"] // router["n_h"]
    b_to = router["boog_sleutel"] % router["n_h"]
    b_w = router["boog_w"].copy()
    b_eid = router["boog_eid"].copy()

    mar_arc = []
    mf, mt, mw, me = [], [], [], []
    for k, e in enumerate(z["edge"]):
        # de zee-index van knoop a wordt meegegeven: de geometrie van een
        # MARNET-edge begint per formaat bij knoop a, dus daarmee staat de
        # looprichting EXACT vast (zie route_geometrie_comb)
        mar_arc.append(("marnet", int(e), int(z["a"][k])))
        mf += [n_t + int(z["a"][k]), n_t + int(z["b"][k])]
        mt += [n_t + int(z["b"][k]), n_t + int(z["a"][k])]
        mw += [float(z["km"][k])] * 2
        me += [-2 - (len(mar_arc) - 1)] * 2
    halte_van_knoop = {}
    for mi, gk, d in conn:
        h = G.halte_van_knoop(router, gk)
        if h is None:
            continue
        halte_van_knoop[gk] = h
        mar_arc.append(("connector", int(mi), int(gk), float(d)))
        eid = -2 - (len(mar_arc) - 1)
        mf += [int(h), n_t + int(mi)]
        mt += [n_t + int(mi), int(h)]
        mw += [float(d) + boete_connector] * 2
        me += [eid, eid]

    b_from = np.concatenate([b_from, np.array(mf, np.int64)])
    b_to = np.concatenate([b_to, np.array(mt, np.int64)])
    b_w = np.concatenate([b_w, np.array(mw, float)])
    b_eid = np.concatenate([b_eid, np.array(me, np.int64)])

    sleutel = b_from * np.int64(n) + b_to
    ordr = np.lexsort((b_w, sleutel))
    sleutel, b_from, b_to = sleutel[ordr], b_from[ordr], b_to[ordr]
    b_w, b_eid = b_w[ordr], b_eid[ordr]
    eerste = np.r_[True, sleutel[1:] != sleutel[:-1]]
    sleutel, b_from, b_to = sleutel[eerste], b_from[eerste], b_to[eerste]
    b_w, b_eid = b_w[eerste], b_eid[eerste]
    M = csr_matrix((np.maximum(b_w, 1e-9), (b_from, b_to)), shape=(n, n))
    comb = dict(router)
    comb.update({"M": M, "n_h": n, "n_track": n_t, "h_lat": h_lat,
                 "h_lon": h_lon, "boog_sleutel": sleutel, "boog_eid": b_eid,
                 "boog_w": b_w, "mar_arc": mar_arc,
                 "h_knoop": np.concatenate(
                     [router["h_knoop"],
                      -1 - np.arange(n_m, dtype=np.int64)]),
                 "n_connector": len(conn)})
    if not stil:
        print(f"  gecombineerd: {n:,} haltes ({n_t:,} track + {n_m:,} MARNET) · "
              f"{len(b_from):,} bogen · {len(conn):,} connectors · "
              f"{time.monotonic()-t0:.0f}s")
    return comb


def route_geometrie_comb(graaf, cache, m, comb, halte_pad):
    """Punten + herkomst voor een pad dat over beide netten kan lopen.

    Het track-deel is regel voor regel hetzelfde als
    bouw_trackgraaf.route_geometrie — inclusief `vooruit = h_idx[u] == i0`, en
    dat is geen detail: zonder die richtingsbepaling emitteer je elke edge van
    i0 naar i1 ongeacht welke kant je hem inloopt, en dan zigzagt de lijn. Eerst
    fout gedaan en meteen gezien: dezelfde 645 edges gaven 2.001 punten en
    1.280 km i.p.v. 1.363 punten en 432 km, terwijl de som van de edge-km wél
    klopte (431,995). De lengte van de GETEKENDE lijn is dus de toets, niet de
    som van de edge-km — die laatste dekt een richtingsfout af."""
    punten, herkomst, edges = [], [], []
    km_track = km_marnet = km_conn = 0.0
    n_over = n_marnet_edge = n_conn = 0

    def voeg(p, herk):
        if punten and punten[-1] == p:
            return
        punten.append(p)
        herkomst.append(herk)

    for u, v in zip(halte_pad[:-1], halte_pad[1:]):
        eid, w = G.boog_eid(comb, u, v)
        if eid is None:
            raise RuntimeError(f"boog {u}->{v} niet gevonden")
        if eid == -1:                                  # overstap binnen tracks
            n_over += 1
            tix, idx = int(comb["h_tix"][v]), int(comb["h_idx"][v])
            s0 = int(cache["start"][tix])
            voeg((float(cache["lat"][s0 + idx]), float(cache["lon"][s0 + idx])),
                 (int(cache["set"][tix]), int(cache["regel"][tix]), idx))
        elif eid >= 0:                                 # track-edge
            edges.append(eid)
            tix = int(graaf["edge_tix"][eid])
            i0, i1 = int(graaf["edge_i0"][eid]), int(graaf["edge_i1"][eid])
            s0 = int(cache["start"][tix])
            vooruit = int(comb["h_idx"][u]) == i0
            rng = range(i0, i1 + 1) if vooruit else range(i1, i0 - 1, -1)
            for k in rng:
                voeg((float(cache["lat"][s0 + k]), float(cache["lon"][s0 + k])),
                     (int(cache["set"][tix]), int(cache["regel"][tix]), k))
            km_track += float(graaf["edge_km"][eid])
        else:
            soort = comb["mar_arc"][-2 - eid]
            if soort[0] == "marnet":                   # MARNET-zee-edge
                n_marnet_edge += 1
                e, zee_a = soort[1], soort[2]
                g0, g1 = int(m["geom_start"][e]), int(m["geom_start"][e + 1])
                seq = list(range(g0, g1))
                # ⚠️ Richting op KNOOP-ID, niet op coördinaat-afstand. De eerste
                # versie vergeleek |dlat|+|dlon| van beide edge-uiteinden met de
                # halte u; dat is fout zodra een edge lang is of de datumgrens
                # kruist, en het bleef verborgen omdat de som van de edge-km
                # gewoon klopte. Gemeten op Rotterdam -> Shanghai: getekende
                # lijn 47.938 km tegen 15.541 km aan edge-km — de lijn liep elke
                # edge de verkeerde kant op en weer terug. Vandaar de
                # LENGTE-INVARIANT hieronder: die kan dit niet missen.
                if (u - comb["n_track"]) != zee_a:
                    seq = seq[::-1]
                for gi in seq:
                    voeg((float(m["geom_lat"][gi]), float(m["geom_lon"][gi])),
                         ("MARNET", e, gi))
                km_marnet += float(m["edge_km"][e])
            else:                                      # connector
                n_conn += 1
                km_conn += soort[3]
                voeg((float(comb["h_lat"][v]), float(comb["h_lon"][v])),
                     ("CONNECTOR", soort[1], soort[2]))
    la = np.array([p[0] for p in punten])
    lo = np.array([p[1] for p in punten])
    seg = seg_km_wrap(la, lo) if len(la) > 1 else np.zeros(1)
    return {"punten": punten, "herkomst": herkomst, "edges": edges,
            "km": float(seg.sum()), "km_track": km_track,
            "km_marnet": km_marnet, "km_connector": km_conn,
            "n_overstap": n_over, "n_marnet_edge": n_marnet_edge,
            "n_connector": n_conn,
            # LENGTE-INVARIANT: de getekende lijn hoort de som van de gebruikte
            # edge-lengtes te zijn plus de naden van de overstappen. Wijkt dat
            # meer dan een paar honderd meter af, dan loopt er een edge de
            # verkeerde kant op — precies de fout hierboven, die de som van de
            # edge-km NIET liet zien.
            "km_edges": km_track + km_marnet + km_conn,
            "max_stap_km": float(seg.max()) if len(seg) else 0.0}


# ── relatieve havensnap ────────────────────────────────────────────────────

def snap_relatief(router, boom, lat, lon, in_hoofd, k=32):
    """Dichtstbijzijnde halte; maar een halte in de HOOFDcomponent wint als hij
    niet meer dan 2x + 0,1 km verder ligt. Nooit absoluut teleporteren."""
    d, idx = boom.query(xyz([lat], [lon]), k=k, workers=-1)
    d = boog_km(d)[0]
    idx = idx[0]
    j = 0
    if not in_hoofd[idx[0]]:
        kand = np.flatnonzero(in_hoofd[idx])
        if len(kand) and d[kand[0]] <= REL_FACTOR * d[0] + REL_MARGE:
            j = int(kand[0])
    return int(idx[j]), float(d[j]), float(d[0]), bool(in_hoofd[idx[j]])


# ── subcommando's ──────────────────────────────────────────────────────────

def _laad(args):
    pad = Path(args.graaf)
    graaf = G.laad_graaf(pad)
    cache = G.laad_cache(Path(str(pad) + "-tracks"))
    m = lees_marnet(args.marnet)
    z = marnet_zee(m, vermijd=tuple(args.vermijd))
    print(f"MARNET-zee (alles behalve de bulk-rivierlaag; vermijd "
          f"{list(args.vermijd)}): {len(z['lat']):,} knopen · "
          f"{len(z['edge']):,} edges · {z['km'].sum():,.0f} km · "
          f"{z['componenten']} componenten "
          f"(hoofd {np.bincount(z['label']).max():,} knopen)")
    print(f"track-graaf: {len(graaf['knoop_lat']):,} knopen · "
          f"{len(graaf['edge_km']):,} edges · "
          f"{graaf['edge_km'].sum():,.0f} km · bbox {graaf['bbox']}")
    return graaf, cache, m, z


def cmd_hecht(args):
    graaf, cache, m, z = _laad(args)
    router = G.bouw_router(graaf, cache, overstap_boete=args.overstap_boete,
                           stil=False)
    print(f"\n═══ AANHECHTING · EPS = {args.eps} km ═══")
    conn, knoop_hoofd, weg = bouw_connectors(graaf, router, z, args.eps,
                                             ne_map=args.ne)
    print(f"  AANGEHECHT: {len(conn):,} MARNET-zee-knopen "
          f"({len(conn)/len(z['lat'])*100:.1f}% van MARNET-zee wereldwijd)")
    if conn:
        d = np.array([c[2] for c in conn])
        print(f"  connector-lengte (km): min {d.min():.3f} · p50 "
              f"{np.median(d):.3f} · p90 {np.percentile(d,90):.3f} · "
              f"max {d.max():.3f} · som {d.sum():.2f}")
        in_h = np.array([knoop_hoofd[c[1]] for c in conn])
        print(f"  graafknoop in de hoofdcomponent: {in_h.sum()} van {len(conn)}")
        mh = np.array([z["label"][c[0]] == z["hoofd"] for c in conn])
        print(f"  MARNET-knoop in de MARNET-hoofdcomponent: {mh.sum()} van "
              f"{len(conn)}")

    # gevoeligheid: wat koopt eps, en kan de landtoets überhaupt iets weerleggen?
    print("\n── GEVOELIGHEID VAN EPS ──")
    print("  (de landtoets draait bij elke stap mee: als hij bij GEEN enkele "
          "eps\n   iets verwerpt, is hij decoratie en hoort dat er te staan)")
    rijen = []
    for e in args.eps_reeks:
        c2, _, w2 = bouw_connectors(graaf, router, z, e, ne_map=args.ne,
                                    stil=True)
        d2 = np.array([c[2] for c in c2]) if c2 else np.zeros(0)
        rijen.append((e, len(c2), float(d2.sum()) if len(d2) else 0.0,
                      float(d2.max()) if len(d2) else 0.0,
                      len(w2["verworpen"]), len(w2["onthouden"])))
        print(f"  eps {e:>5} km -> {len(c2):>5} connectors · "
              f"som {rijen[-1][2]:8.2f} km · langste {rijen[-1][3]:6.3f} km · "
              f"landtoets verwerpt {len(w2['verworpen'])} · onthoudt "
              f"{len(w2['onthouden'])}")

    comb = bouw_gecombineerd(graaf, cache, router, z, conn,
                             boete_connector=args.boete_connector, stil=False)
    print("\n── INTEGRITEITS-METRICS NA AANHECHTING ──")
    rap = metrics_na(graaf, cache, m, z, router, comb, conn, args)

    uit = Path(str(args.graaf) + "-marnet.json")
    doc = {
        "versie": 1, "type": "marnet-aanhechting",
        "gemaakt": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "graaf": str(args.graaf),
        "marnet": {"bron": "tag pre-ais-net, v2/data/marnet.{bin,json} — NIET "
                           "teruggezet in v2/data/",
                   "zee_knopen": int(len(z["lat"])),
                   "zee_edges": int(len(z["edge"])),
                   "zee_km": float(z["km"].sum())},
        "regel": "MARNET-zee-KNOOP <-> track-graaf-KNOOP binnen eps; geen "
                 "terugval, geen coördinaat verplaatst, geen MARNET-edge "
                 "geknipt; connector getoetst op landkruising; relatieve "
                 "voorkeur voor de hoofdcomponent",
        "eps_km": args.eps, "boete_connector_km": args.boete_connector,
        "landtoets": {"verworpen": len(weg["verworpen"]),
                      "onthouden": len(weg["onthouden"]),
                      "uitleg": "verworpen = kruist land terwijl beide "
                                "uiteinden in water liggen; onthouden = een "
                                "uiteinde ligt binnen de 1:10M-landpolygoon "
                                "(havenbekken/deltapas), daar kan de toets "
                                "niets weerleggen"},
        "eps_gevoeligheid": [{"eps_km": r[0], "connectors": r[1],
                              "som_km": r[2], "langste_km": r[3],
                              "land_verworpen": r[4], "land_onthouden": r[5]}
                             for r in rijen],
        "connectors": [{"marnet_knoop": int(z["knoop_id"][c[0]]),
                        "marnet_zee_ix": int(c[0]),
                        "marnet_lat": float(z["lat"][c[0]]),
                        "marnet_lon": float(z["lon"][c[0]]),
                        "graaf_knoop": int(c[1]),
                        "graaf_lat": float(graaf["knoop_lat"][c[1]]),
                        "graaf_lon": float(graaf["knoop_lon"][c[1]]),
                        "km": round(float(c[2]), 4)} for c in conn],
        "metrics": rap,
    }
    uit.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\ngeschreven: {uit}")


def metrics_na(graaf, cache, m, z, router, comb, conn, args):
    nc0, lab0 = connected_components(router["M"], directed=False)
    nc1, lab1 = connected_components(comb["M"], directed=False)
    m0 = np.bincount(lab0)
    m1 = np.bincount(lab1)
    h0, h1 = int(np.argmax(m0)), int(np.argmax(m1))
    # hoeveel MARNET-zee-knopen hangen nu aan de track-hoofdcomponent?
    n_t = comb["n_track"]
    mar_in_hoofd = int((lab1[n_t:] == h1).sum())
    trk_in_hoofd = int((lab1[:n_t] == h1).sum())
    graad = np.bincount(router["h_knoop"], minlength=len(graaf["knoop_lat"]))
    rap = {
        "voor": {"componenten": int(nc0), "hoofd_haltes": int(m0[h0]),
                 "hoofd_aandeel": float(m0[h0] / len(lab0))},
        "na": {"componenten": int(nc1), "hoofd_haltes": int(m1[h1]),
               "hoofd_aandeel": float(m1[h1] / len(lab1)),
               "marnet_knopen_in_hoofd": mar_in_hoofd,
               "track_haltes_in_hoofd": trk_in_hoofd},
        "knopen": int(len(graaf["knoop_lat"])),
        "dode_knopen": int((graad == 0).sum()),
        "edges": int(len(graaf["edge_km"])),
        "edge_km": float(graaf["edge_km"].sum()),
        "haltes_track": int(router["n_h"]),
        "haltes_totaal": int(comb["n_h"]),
        "connectors": len(conn),
        "connector_km": float(sum(c[2] for c in conn)),
    }
    print(f"  componenten        : {nc0:,} -> {nc1:,}")
    print(f"  hoofdcomponent     : {m0[h0]:,} haltes ({m0[h0]/len(lab0)*100:.1f}%)"
          f" -> {m1[h1]:,} ({m1[h1]/len(lab1)*100:.1f}%)")
    print(f"  MARNET-zee-knopen in de hoofdcomponent: {mar_in_hoofd:,} van "
          f"{len(z['lat']):,}  ({mar_in_hoofd/len(z['lat'])*100:.1f}% — dat is "
          f"het HELE zeenet dat nu vanaf de kade bereikbaar is)")
    print(f"  knopen / edges     : {rap['knopen']:,} / {rap['edges']:,} "
          f"({rap['edge_km']:,.0f} edge-km) · dode knopen "
          f"{rap['dode_knopen']:,} ({rap['dode_knopen']/rap['knopen']*100:.1f}%)")
    print(f"  knoop-bezetting    : 1 halte={int((graad==1).sum()):,} · "
          f"2={int((graad==2).sum()):,} · 3+={int((graad>=3).sum()):,} · "
          f"0 (dood)={rap['dode_knopen']:,}")
    print(f"  haltes             : {router['n_h']:,} track + {len(z['lat']):,} "
          f"MARNET = {comb['n_h']:,} · connectors {len(conn):,} "
          f"({rap['connector_km']:.2f} km totaal aan connector-geometrie)")
    return rap


def _havenlijst(args, graaf, cache):
    """Havens uit v2/data/ports.json + aansluitingen.json binnen de extent van
    de graaf-cache (daar kan een track überhaupt iets betekenen)."""
    d = Path(args.data)
    p = json.loads((d / "ports.json").read_text(encoding="utf-8"))
    ll = np.asarray(p["ll"], float).reshape(-1, 2)
    la, lo = cache["lat"], cache["lon"]
    z, w, n_, o = la.min(), lo.min(), la.max(), lo.max()
    sel = np.flatnonzero((ll[:, 1] >= z) & (ll[:, 1] <= n_)
                         & (ll[:, 0] >= w) & (ll[:, 0] <= o))
    havens = [{"naam": p["namen"][i], "land": p["landen"][i],
               "locode": p["locodes"][i], "lat": float(ll[i, 1]),
               "lon": float(ll[i, 0]), "bron": "ports.json",
               "marnet_knoop_oud": int(p["knoop"][i]),
               "marnet_km_oud": float(p["afstandKm"][i])} for i in sel]
    a = json.loads((d / "aansluitingen.json").read_text(encoding="utf-8"))
    for s in a["aansluitingen"]:
        lon_, lat_ = s["plek"]
        if z <= lat_ <= n_ and w <= lon_ <= o:
            havens.append({"naam": s["id"], "land": s.get("grondstof", ""),
                           "locode": "", "lat": lat_, "lon": lon_,
                           "bron": "aansluitingen.json",
                           "marnet_knoop_oud": -1, "marnet_km_oud": float("nan")})
    for naam, (lat_, lon_, herk) in G.PUNTEN.items():
        if z <= lat_ <= n_ and w <= lon_ <= o:
            havens.append({"naam": naam, "land": "", "locode": "",
                           "lat": lat_, "lon": lon_, "bron": "PUNTEN",
                           "marnet_knoop_oud": -1, "marnet_km_oud": float("nan")})
    return havens


def cmd_havens(args):
    graaf, cache, m, z = _laad(args)
    router = G.bouw_router(graaf, cache, overstap_boete=args.overstap_boete,
                           stil=False)
    conn, knoop_hoofd, _ = bouw_connectors(graaf, router, z, args.eps,
                                           ne_map=args.ne)
    comb = bouw_gecombineerd(graaf, cache, router, z, conn,
                             boete_connector=args.boete_connector, stil=False)
    havens = _havenlijst(args, graaf, cache)
    print(f"\n═══ HAVENS · {len(havens)} binnen de extent van de graaf-cache ═══")

    zboom = cKDTree(xyz(z["lat"], z["lon"]))
    tboom = cKDTree(xyz(router["h_lat"], router["h_lon"]))
    nc1, lab1 = connected_components(comb["M"], directed=False)
    h1 = int(np.argmax(np.bincount(lab1)))
    in_hoofd_t = lab1[:comb["n_track"]] == h1
    nc0, lab0 = connected_components(router["M"], directed=False)
    h0 = int(np.argmax(np.bincount(lab0)))
    in_hoofd_t0 = lab0 == h0
    # bereikt de MARNET-hoofdcomponent?
    mar_hoofd = np.flatnonzero((z["label"] == z["hoofd"]))
    mar_in_h1 = set(np.flatnonzero(lab1[comb["n_track"]:] == h1).tolist())

    rijen = []
    for h in havens:
        dz, _ = zboom.query(xyz([h["lat"]], [h["lon"]]))
        dz = float(boog_km(dz)[0])
        j0, d0, d0abs, ok0 = snap_relatief(router, tboom, h["lat"], h["lon"],
                                           in_hoofd_t0)
        j1, d1, d1abs, ok1 = snap_relatief(router, tboom, h["lat"], h["lon"],
                                           in_hoofd_t)
        # bereikt deze haven na aanhechting het MARNET-hoofdnet?
        bereikt = bool(ok1 and len(mar_in_h1) > 0)
        # VOOR = wat de haven had vóór het AIS-werk: hij hing aan MARNET-zee.
        # NA  = hij hangt aan echte trackgeometrie EN bereikt MARNET nog steeds.
        wint = d1 < dz and bereikt
        rijen.append({**h, "marnet_zee_km": round(dz, 3),
                      "track_km_voor": round(d0, 3),
                      "track_km_na": round(d1, 3),
                      "in_hoofd_voor": bool(ok0), "in_hoofd_na": bool(ok1),
                      "bereikt_marnet": bereikt,
                      "winst_km": round(dz - d1, 3) if wint else 0.0,
                      "beter_dan_marnet": bool(wint)})
    rijen.sort(key=lambda r: (-r["beter_dan_marnet"], -r["winst_km"],
                              r["track_km_na"]))
    print("  VOOR = snap naar MARNET-zee (de enige optie vóór het AIS-werk)")
    print("  NA   = snap naar ECHTE trackgeometrie, mét MARNET nog bereikbaar")
    print("  'track voor/na' zijn de snap naar de track-graaf zónder en mét de")
    print("  aanhechting — die horen gelijk te zijn: de aanhechting voegt toe,")
    print("  ze verplaatst niets.\n")
    print(f"{'haven':<32}{'VOOR (MARNET)':>14}{'NA (track)':>11}"
          f"{'winst':>9}{'hoofd':>7}  MARNET bereikbaar")
    for r in rijen:
        w = f"{r['winst_km']:>9.2f}" if r["beter_dan_marnet"] else "        -"
        print(f"{r['naam'][:31]:<32}{r['marnet_zee_km']:>14.2f}"
              f"{r['track_km_na']:>11.3f}{w}"
              f"{('ja' if r['in_hoofd_na'] else 'NEE'):>7}  "
              f"{'JA' if r['bereikt_marnet'] else 'nee'}")
    n_ok = sum(1 for r in rijen if r["bereikt_marnet"])
    n_beter = sum(1 for r in rijen if r["beter_dan_marnet"])
    dz = np.array([r["marnet_zee_km"] for r in rijen])
    dt = np.array([r["track_km_na"] for r in rijen])
    dv = np.array([r["track_km_voor"] for r in rijen])
    print(f"\n  havensnap verplaatst door de aanhechting: "
          f"{int((dv != dt).sum())} van {len(rijen)} "
          f"(hoort 0 te zijn — verlengen, niet verplaatsen)")
    print(f"  {n_ok} van {len(rijen)} havens bereiken na aanhechting het "
          f"MARNET-zeenet over echte trackgeometrie")
    print(f"  {n_beter} van {len(rijen)} havens hangen NA dichter aan het net "
          f"dan VOOR (en houden MARNET)")
    sel = np.array([r["beter_dan_marnet"] for r in rijen])
    if sel.any():
        print(f"    van die {n_beter}: MARNET-snap p50 {np.median(dz[sel]):.2f} km "
              f"-> track-snap p50 {np.median(dt[sel]):.3f} km · "
              f"mediane winst {np.median(dz[sel]-dt[sel]):.2f} km")
    print("\n  ── WAAR DE AANHECHTING NIETS OPLEVERT (even informatief) ──")
    for r in rijen:
        if r["beter_dan_marnet"]:
            continue
        if not r["bereikt_marnet"] and r["track_km_na"] < 5:
            reden = ("dicht bij tracks maar LOS van de hoofdcomponent — geen "
                     "doorgaand spoor naar zee (dataschaarste, geen graaffout)")
        elif not r["bereikt_marnet"]:
            reden = "geen tracks in de buurt én los van de hoofdcomponent"
        else:
            reden = (f"MARNET ligt dichterbij ({r['marnet_zee_km']:.2f} km) dan "
                     f"de tracks ({r['track_km_na']:.1f} km) — buiten het "
                     f"dekkingsgebied van deze corridor")
        print(f"    {r['naam'][:31]:<32} {reden}")
    uit = Path(str(args.graaf) + "-havens.json")
    uit.write_text(json.dumps({"eps_km": args.eps, "havens": rijen},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\ngeschreven: {uit}")


def cmd_regressie(args):
    graaf, cache, m, z = _laad(args)
    router = G.bouw_router(graaf, cache, overstap_boete=args.overstap_boete,
                           stil=False)
    conn, knoop_hoofd, _ = bouw_connectors(graaf, router, z, args.eps,
                                           ne_map=args.ne)
    comb = bouw_gecombineerd(graaf, cache, router, z, conn,
                             boete_connector=args.boete_connector, stil=False)

    lat_a, lon_a, na, _ = G.parse_punt(args.van)
    lat_b, lon_b, nb, _ = G.parse_punt(args.naar)
    print(f"\n═══ REGRESSIE {na} -> {nb} ═══")
    ha, da, ka = G.snap_halte(router, lat_a, lon_a)
    hb, db, kb = G.snap_halte(router, lat_b, lon_b)
    pad0, d0 = G.zoek_route(router, ha, hb)
    r0 = G.route_geometrie(graaf, cache, router, pad0) if pad0 else None
    ha2, da2, _ = G.snap_halte(comb, lat_a, lon_a)
    hb2, db2, _ = G.snap_halte(comb, lat_b, lon_b)
    pad1, d1 = G.zoek_route(comb, ha2, hb2)
    r1 = route_geometrie_comb(graaf, cache, m, comb, pad1) if pad1 else None

    print(f"  snap A: {da:.3f} km (voor) / {da2:.3f} km (na) · "
          f"snap B: {db:.3f} / {db2:.3f} km")
    if r0 is None:
        print("  VOOR: GEEN PAD over de track-graaf alleen")
    if r1 is None:
        print("  NA  : GEEN PAD over het gecombineerde net")
    if r1 is not None and r0 is None:
        print(f"  NA  : {len(r1['edges'])} track-edges · "
              f"{r1['n_marnet_edge']} MARNET-edges · {r1['n_connector']} "
              f"connectors · {len(r1['punten'])} punten · {r1['km']:.1f} km "
              f"(track {r1['km_track']:.1f} · MARNET {r1['km_marnet']:.1f} · "
              f"connector {r1['km_connector']:.3f})")
        print(f"  lengte-invariant: getekende lijn {r1['km']:.3f} km vs som "
              f"edge-km {r1['km_edges']:.3f} km · verschil "
              f"{r1['km']-r1['km_edges']:+.3f} km "
              f"(= de naden; groot verschil = een edge loopt verkeerd om)")
        print("  -> de aanhechting maakt een reis mogelijk die er zonder haar "
              "NIET was. Dit is de niet-vacuüm-controle bij de Vidalia-"
              "regressie: dezelfde connectors die daar niets veranderen, "
              "openen hier het hele zeenet.")
    if r0 is None or r1 is None:
        print("\n── INTEGRITEITS-METRICS NA AANHECHTING ──")
        metrics_na(graaf, cache, m, z, router, comb, conn, args)
        return
    print(f"  VOOR: {len(r0['edges'])} edges uit {r0['n_tracks']} tracks · "
          f"{r0['n_overstap']} track-wissels · {len(r0['punten'])} punten · "
          f"{r0['km']:.3f} km  (dijkstra {d0:.1f} = {r0['km']:.1f} + "
          f"{r0['n_overstap']}x{args.overstap_boete:g} km boete)")
    print(f"  NA  : {len(r1['edges'])} track-edges · {r1['n_marnet_edge']} "
          f"MARNET-edges · {r1['n_connector']} connectors · "
          f"{len(r1['punten'])} punten · {r1['km']:.3f} km "
          f"(track {r1['km_track']:.3f} · MARNET {r1['km_marnet']:.3f} · "
          f"connector {r1['km_connector']:.3f})  (dijkstra {d1:.1f})")
    print(f"  lengte-invariant NA: getekende lijn {r1['km']:.3f} km vs som "
          f"edge-km {r1['km_edges']:.3f} km · verschil "
          f"{r1['km']-r1['km_edges']:+.3f} km (= de naden)")
    gelijk = (len(r0["punten"]) == len(r1["punten"])
              and all(p == q for p, q in zip(r0["punten"], r1["punten"])))
    zelfde_edges = r0["edges"] == r1["edges"]
    print(f"  lengteverschil: {r1['km']-r0['km']:+.6f} km "
          f"({(r1['km']-r0['km'])/max(r0['km'],1e-9)*100:+.4f}%)")
    print(f"  EDGE-REEKS identiek : {'JA' if zelfde_edges else 'NEE'}")
    print(f"  PUNTENREEKS identiek: {'JA' if gelijk else 'NEE'}"
          + ("" if gelijk else "  <- de aanhechting verschuift de route"))
    if not gelijk:
        n_mar = sum(1 for h in r1["herkomst"] if h[0] == "MARNET")
        print(f"    routepunten uit MARNET: {n_mar} van {len(r1['punten'])}")
    # HARD BEWIJS: lees de brontrackset terug voor de route NA aanhechting
    ix = [i for i, h in enumerate(r1["herkomst"]) if isinstance(h[0], int)]
    ident, anders, vb = G.bewijs_route(
        graaf, [r1["punten"][i] for i in ix], [r1["herkomst"][i] for i in ix])
    print(f"  geometrie-bewijs NA: {ident:,} van {len(ix):,} track-routepunten "
          f"IDENTIEK aan het brontrackpunt · {anders} afwijkend · "
          f"{len(r1['punten'])-len(ix)} punten niet uit een track "
          f"(MARNET/connector)")
    if args.verwacht_km:
        for naam, v in (("voor", r0["km"]), ("na", r1["km"])):
            afw = (v - args.verwacht_km) / args.verwacht_km * 100
            print(f"  {naam} tegen referentie {args.verwacht_km} km: {v:.1f} km "
                  f"= {afw:+.2f}%  {'BINNEN' if abs(afw) <= 2 else 'BUITEN'} ±2%")

    # ── de tweede eis: beide geulen om het eiland blijven bereikbaar ──
    if args.eiland_van:
        print("\n═══ EILAND-TOETS NA AANHECHTING ═══")
        eiland_toets(graaf, cache, m, z, conn, args)

    print("\n── INTEGRITEITS-METRICS NA AANHECHTING ──")
    metrics_na(graaf, cache, m, z, router, comb, conn, args)


def eiland_toets(graaf, cache, m, z, conn, args):
    """Zelfde toets als bouw_trackgraaf.cmd_eiland, maar op het GECOMBINEERDE
    net: twee knoop-disjuncte geulen die boven én onder één knoop delen.
    Foutmodus (a) = één arm weg · (b) = twee losse parallelle netwerken."""
    lat_a, lon_a, na, _ = G.parse_punt(args.eiland_van)
    lat_b, lon_b, nb, _ = G.parse_punt(args.eiland_naar)
    for fase in ("voor", "na"):
        router = G.bouw_router(graaf, cache, overstap_boete=args.overstap_boete,
                              stil=True)
        R1 = (router if fase == "voor" else
              bouw_gecombineerd(graaf, cache, router, z,
                                conn if fase == "na" else [],
                                boete_connector=args.boete_connector))
        ha, da, ka = G.snap_halte(R1, lat_a, lon_a)
        hb, db, kb = G.snap_halte(R1, lat_b, lon_b)
        pad1, _ = G.zoek_route(R1, ha, hb)
        if pad1 is None:
            print(f"  [{fase}] GEEN PAD")
            continue
        g1 = (G.route_geometrie(graaf, cache, R1, pad1) if fase == "voor"
              else route_geometrie_comb(graaf, cache, m, R1, pad1))
        kn1 = [int(R1["h_knoop"][h]) for h in pad1]
        verboden = set(k for k in kn1[1:-1] if k >= 0) - {ka, kb}
        r2 = G.bouw_router(graaf, cache, verboden_knopen=verboden,
                           overstap_boete=args.overstap_boete, stil=True)
        R2 = (r2 if fase == "voor" else
              bouw_gecombineerd(graaf, cache, r2, z, conn,
                                boete_connector=args.boete_connector))
        ha2 = G.halte_van_knoop(R2, ka)
        hb2 = G.halte_van_knoop(R2, kb)
        if ha2 is None or hb2 is None:
            print(f"  [{fase}] uiteinde-knoop bestaat niet in de tweede graaf")
            continue
        lat_v, lon_v, nv, _ = G.parse_punt(args.eiland_via)
        hv, dv, kv = G.snap_halte(R2, lat_v, lon_v)
        pa, _ = G.zoek_route(R2, ha2, hv)
        pb, _ = G.zoek_route(R2, hv, hb2)
        if pa is None or pb is None:
            print(f"  [{fase}] GEEN PAD via {nv} — die arm hangt niet aan "
                  f"beide juncties")
            continue
        pad2 = pa + pb[1:]
        g2 = (G.route_geometrie(graaf, cache, R2, pad2) if fase == "voor"
              else route_geometrie_comb(graaf, cache, m, R2, pad2))
        kn2 = [int(R2["h_knoop"][h]) for h in pad2]
        gedeeld = sorted(set(kn1) & set(kn2))
        goed = ka in gedeeld and kb in gedeeld
        print(f"  [{fase}] geul 1 {g1['km']:.2f} km · geul 2 {g2['km']:.2f} km "
              f"· gedeelde knopen {len(gedeeld)} · beneden-junctie {ka} "
              f"({graaf['knoop_lat'][ka]:.5f}, {graaf['knoop_lon'][ka]:.5f}) · "
              f"boven-junctie {kb} ({graaf['knoop_lat'][kb]:.5f}, "
              f"{graaf['knoop_lon'][kb]:.5f}) -> "
              f"{'GESLAAGD' if goed else 'TWIJFEL'}")


# ── subcommando `route`: één stroom bakken tot statisch databestand ───────
# De bol tekent (nog) geen MARNET, geen connectors en geen geroutete stroom —
# daarom wordt de eerste zichtbare stroom BUILD-TIME gebakken tot een klein
# JSON-contract (versie 2): punten [lon, lat] op 5 decimalen (de ruwe
# AIS-korrel), benen in reisvolgorde, markers op de aangewezen punten. De
# route komt uit exact dezelfde laad- en routeerroutines als `regressie`
# (NA-kant).
#
# TWEE MODI:
#   * BEEN-GESTUURD (--been/--stippel/--marker) — de standaard sinds de
#     routebrief grafiet-balama-vidalia. Elk been wordt APART geroutet tussen
#     zijn eigen, uit de routebrief aangewezen eindpunten; de modaliteit komt
#     uit de vlag. Zie de docstring van cmd_route voor het waarom (de
#     Leeville-les).
#   * VRIJ (--van/--naar zonder --been) — één route over het hele
#     gecombineerde net; benen afgeleid uit de herkomst (MARNET = zee,
#     track = binnenvaart). Blijft bestaan voor verkenning: hij laat zien wat
#     de graaf ZELF zou kiezen, en dat verschil met de routebrief is
#     informatie (zo werd Leeville überhaupt gevonden).
#
# Een spoorbeen komt niet uit deze graaf maar uit een aangeleverde GeoJSON
# (toets_spoorroute.mjs) en wordt als los been achteraan gezet.

# Weergavenamen voor de markers — ALLEEN gebruikt in de vrije modus (in de
# been-modus vervangt --marker de afleiding volledig). De router kent alleen
# coördinaten en PUNTEN-sleutels (bouw_trackgraaf.PUNTEN zegt "vidalia", de
# bol wil "Vidalia (Syrah)"); dat is redactie, geen meting — vandaar een
# expliciete tabel i.p.v. iets afleiden. Sleutel = de --van/--naar-spec zoals
# meegegeven; onbekende specs vallen terug op de parse_punt-naam.
MARKER_NAAM = {
    "-14.54,40.67": "Nacala",      # uitvoerhaven van Balama-grafiet (Mozambique)
    "vidalia": "Vidalia (Syrah)",  # gr-ref-vidalia, data/graphite.js
}
# Naam van het overslagpunt zee <-> binnenvaart, per stroom (het connectorpunt
# wordt pas tijdens het routeren gevonden, dus zijn naam kan nergens anders
# vandaan komen dan uit deze redactietabel).
OVERSLAG_NAAM = {
    "grafiet-balama-vs": "New Orleans-delta",
}
# Hoe een modaliteit in de overslag-markertekst heet ("overslag zee → barge").
OVERSLAG_WOORD = {"zee": "zee", "binnenvaart": "barge"}


def _spoor_been(pad):
    """Het spoorbeen uit een GeoJSON (LineString/MultiLineString, coördinaten
    al [lon, lat]). km = som van de segmentlengtes PER DEEL, zodat een gat
    tussen twee MultiLineString-delen niet als gevaren afstand meetelt."""
    d = json.loads(Path(pad).read_text(encoding="utf-8"))
    delen = []
    for ft in d["features"]:
        g = ft["geometry"]
        if g["type"] == "LineString":
            delen.append(g["coordinates"])
        elif g["type"] == "MultiLineString":
            delen.extend(g["coordinates"])
    punten, km_tot = [], 0.0
    for deel in delen:
        arr = np.asarray(deel, dtype=np.float64)
        if len(arr) > 1:
            km_tot += float(seg_km_wrap(arr[:, 1], arr[:, 0]).sum())
        punten.extend((float(lo), float(la)) for lo, la in arr)
    return punten, km_tot


def _parse_been_spec(spec):
    """'MODALITEIT|NAAM|VAN_LAT,VAN_LON|NAAR_LAT,NAAR_LON' → 4 velden.
    VAN/NAAR mogen ook een PUNTEN-sleutel zijn (G.parse_punt regelt beide)."""
    delen = [d.strip() for d in spec.split("|")]
    if len(delen) != 4 or not all(delen):
        sys.exit(f"--been/--stippel verwacht 'MODALITEIT|NAAM|VAN_LAT,VAN_LON|"
                 f"NAAR_LAT,NAAR_LON', kreeg: {spec!r}")
    return delen[0], delen[1], delen[2], delen[3]


def _parse_marker_spec(spec):
    """'NAAM|LAT,LON' → (naam, lat, lon)."""
    delen = [d.strip() for d in spec.split("|")]
    if len(delen) != 2 or not all(delen):
        sys.exit(f"--marker verwacht 'NAAM|LAT,LON', kreeg: {spec!r}")
    try:
        lat, lon = (float(x) for x in delen[1].split(","))
    except ValueError:
        sys.exit(f"--marker: coördinaat niet leesbaar in {spec!r}")
    return delen[0], lat, lon


def _marker(naam, lat, lon):
    return {"naam": naam, "lon": round(lon, 5), "lat": round(lat, 5)}


def _route_been(args, graaf, cache, m, comb, mod, naam, van, naar):
    """Eén been apart routeren over het gecombineerde net. De modaliteit komt
    uit de vlag; de km-uitsplitsing (track/MARNET/connector) en de
    snap-afstanden gaan naar de console — dat blijft de eerlijkheid van het
    gereedschap: de vlag bepaalt hoe het been HEET, de uitsplitsing laat zien
    waar de geometrie werkelijk vandaan komt."""
    lat_a, lon_a, na, _ = G.parse_punt(van)
    lat_b, lon_b, nb, _ = G.parse_punt(naar)
    ha, da, _ = G.snap_halte(comb, lat_a, lon_a)
    hb, db, _ = G.snap_halte(comb, lat_b, lon_b)
    print(f"\n═══ BEEN [{mod}] {naam} ═══")
    print(f"  van {na} · snap {da:.3f} km — naar {nb} · snap {db:.3f} km")
    pad, _ = G.zoek_route(comb, ha, hb)
    if pad is None:
        sys.exit(f"GEEN PAD voor been '{naam}' ({na} -> {nb}) — niets gebakken")
    r = route_geometrie_comb(graaf, cache, m, comb, pad)
    print(f"  {len(r['edges'])} track-edges · {r['n_marnet_edge']} "
          f"MARNET-edges · {r['n_connector']} connectors · "
          f"{len(r['punten'])} punten")
    print(f"  km-uitsplitsing: totaal {r['km']:.1f} = track {r['km_track']:.1f}"
          f" · MARNET {r['km_marnet']:.1f} · connector {r['km_connector']:.3f}")
    print(f"  lengte-invariant: getekende lijn {r['km']:.3f} vs som edge-km "
          f"{r['km_edges']:.3f} = {r['km']-r['km_edges']:+.3f} km (= de naden)")
    return {"modaliteit": mod, "naam": naam, "km": r["km"],
            "punten": r["punten"]}


def _stippel_been(mod, naam, van, naar):
    """Een been dat NIET geroutet wordt: een eigen verbinding (zoals de last
    mile kade → fabriek) als rechte lijn van precies twee punten,
    "stippel": true in de uitvoer."""
    lat_a, lon_a, na, _ = G.parse_punt(van)
    lat_b, lon_b, nb, _ = G.parse_punt(naar)
    km = float(seg_km_wrap(np.array([lat_a, lat_b]),
                           np.array([lon_a, lon_b])).sum())
    print(f"\n═══ STIPPEL [{mod}] {naam} ═══")
    print(f"  {na} -> {nb} · rechte lijn (eigen verbinding, niet geroutet) · "
          f"{km:.3f} km · 2 punten")
    return {"modaliteit": mod, "naam": naam, "stippel": True, "km": km,
            "punten": [(lat_a, lon_a), (lat_b, lon_b)]}


def _route_vrij(args, graaf, cache, m, comb, conn_km):
    """De oude vrije modus: één route --van → --naar, benen afgeleid uit de
    HERKOMST van de punten (MARNET = zee, track = binnenvaart). Retourneert
    (benen, auto_markers)."""
    lat_a, lon_a, na, _ = G.parse_punt(args.van)
    lat_b, lon_b, nb, _ = G.parse_punt(args.naar)
    ha, da, _ = G.snap_halte(comb, lat_a, lon_a)
    hb, db, _ = G.snap_halte(comb, lat_b, lon_b)
    print(f"\n═══ ROUTE (vrij) {na} -> {nb} ═══")
    print(f"  snap A: {da:.3f} km · snap B: {db:.3f} km")
    pad, _ = G.zoek_route(comb, ha, hb)
    if pad is None:
        sys.exit("GEEN PAD over het gecombineerde net — niets gebakken")
    r = route_geometrie_comb(graaf, cache, m, comb, pad)
    print(f"  {len(r['edges'])} track-edges · {r['n_marnet_edge']} "
          f"MARNET-edges · {r['n_connector']} connectors · "
          f"{len(r['punten'])} punten · {r['km']:.1f} km "
          f"(track {r['km_track']:.1f} · MARNET {r['km_marnet']:.1f} · "
          f"connector {r['km_connector']:.3f})")
    print(f"  lengte-invariant: getekende lijn {r['km']:.3f} vs som edge-km "
          f"{r['km_edges']:.3f} = {r['km']-r['km_edges']:+.3f} km (= de naden)")

    # ── opdelen in benen; punten intern (lat, lon) zoals de router ze geeft ─
    benen, overslagen = [], []
    huidig, huidig_mod = [], None
    for p, h in zip(r["punten"], r["herkomst"]):
        if h[0] == "CONNECTOR":
            if huidig:
                huidig.append(p)
                benen.append({"modaliteit": huidig_mod, "punten": huidig})
            overslagen.append((p, conn_km.get((h[1], h[2]), 0.0),
                               len(benen) - 1))
            huidig, huidig_mod = [p], None
            continue
        mod = "zee" if h[0] == "MARNET" else "binnenvaart"
        if huidig_mod is None:
            huidig_mod = mod
        elif mod != huidig_mod:
            # hoort niet voor te komen (elke wissel loopt over een connector);
            # als het tóch gebeurt: eerlijk splitsen i.p.v. stil doorplakken
            print(f"  ⚠️ modaliteitswissel zonder connector bij punt "
                  f"({p[0]:.5f}, {p[1]:.5f})")
            benen.append({"modaliteit": huidig_mod, "punten": huidig})
            huidig = [huidig[-1]]
            huidig_mod = mod
        huidig.append(p)
    if huidig:
        benen.append({"modaliteit": huidig_mod, "punten": huidig})
    for b in benen:
        la = np.array([q[0] for q in b["punten"]])
        lo = np.array([q[1] for q in b["punten"]])
        b["km"] = float(seg_km_wrap(la, lo).sum()) if len(la) > 1 else 0.0
        b["naam"] = f"{b['modaliteit']} (afgeleid uit herkomst)"

    # ── markers: start zeebeen · elk connectorpunt · einde laatste been ────
    van_naam = MARKER_NAAM.get(args.van, na)
    naar_naam = MARKER_NAAM.get(args.naar, nb)
    overslag_naam = OVERSLAG_NAAM.get(args.stroom, "overslag")
    p0 = benen[0]["punten"][0]
    markers = [_marker(f"{van_naam} — start zeebeen (MARNET-knoop)",
                       p0[0], p0[1])]
    for p, dkm, ix in overslagen:
        mv = benen[ix]["modaliteit"] if 0 <= ix < len(benen) else "?"
        mn = (benen[ix + 1]["modaliteit"] if ix + 1 < len(benen) else "?")
        markers.append(_marker(
            f"{overslag_naam} — overslag {OVERSLAG_WOORD.get(mv, mv)} → "
            f"{OVERSLAG_WOORD.get(mn, mn)} (connector "
            f"{f'{dkm:.2f}'.replace('.', ',')} km)", p[0], p[1]))
    p_eind = benen[-1]["punten"][-1]
    markers.append(_marker(
        f"{naar_naam} — overslag naar spoor" if args.spoor_geojson
        else naar_naam, p_eind[0], p_eind[1]))
    return benen, markers


def cmd_route(args):
    """Bak één stroom als benen + markers naar een statisch databestand voor
    de bol (contract versie 2).

    ── WAAROM DE BEEN-MODUS ERBIJ IS GEKOMEN (de Leeville-les) ──
    De vrije modus routeert één pad --van → --naar en leidt de benen af uit de
    HERKOMST van de punten (MARNET = zee, track = binnenvaart). De overslag
    ligt daarmee per constructie op het eerste GRATIS raakpunt tussen de twee
    netten — en dat is een graaf-eigenschap, geen haven. Bij grafiet
    Balama → Vidalia legde de vrije modus de zee→barge-overslag zo bij
    Leeville (Bayou Lafourche): Belle Pass is 23-27 ft, gebouwd voor
    offshore-supplyvaart naar Port Fourchon — daar komt geen containerschip
    voor NOLA doorheen (routebrief grafiet-balama-vidalia, negatieve ankers
    been 2 [Z15]). De routebrief zegt: overslag hoort op AANGEWEZEN punten
    (zeeschip-eind Napoleon Ave · barge-belading Port Allen · losplek Port of
    Vidalia mijl 359), niet waar de netten elkaar toevallig het eerst raken.

    Daarom de been-modus: elk --been wordt APART geroutet over het
    gecombineerde net (eigen snap van/naar, eigen zoek_route +
    route_geometrie_comb) en de modaliteit komt uit de vlag, niet uit de
    herkomst — het zeeschip vaart immers óók het 50-ft-channel de rivier op
    tot mijl 100, en dat stuk hoort bij het zeebeen. Per been blijft de
    km-uitsplitsing (track/MARNET/connector) en de snap-afstand op de console
    staan: de vlag bepaalt de naam, de meting blijft zichtbaar.
    --stippel = een eigen verbinding (last mile kade → fabriek): niet
    geroutet, rechte lijn, "stippel": true. --marker vervangt de automatische
    marker-afleiding volledig zodra er één is opgegeven.

    De km per been is de lengte van de GETEKENDE lijn (seg_km_wrap over de
    beenpunten), dezelfde grootheid als overal in dit bestand — niet de som
    van edge-km, want die dekt een richtingsfout af (zie
    route_geometrie_comb)."""
    if not args.keten and not (args.van and args.naar):
        sys.exit("geef óf --been/--stippel (been-gestuurd) óf --van én --naar "
                 "(vrije modus)")
    graaf, cache, m, z = _laad(args)
    router = G.bouw_router(graaf, cache, overstap_boete=args.overstap_boete,
                           stil=False)
    conn, _, _ = bouw_connectors(graaf, router, z, args.eps, ne_map=args.ne)
    comb = bouw_gecombineerd(graaf, cache, router, z, conn,
                             boete_connector=args.boete_connector, stil=False)
    conn_km = {(mi, gk): d for mi, gk, d in conn}

    auto_markers = []
    if args.keten:
        # ── been-gestuurd: elk been apart, in de volgorde van de vlaggen ──
        if args.van or args.naar:
            print("  (--van/--naar worden in de been-modus genegeerd)")
        benen = []
        for soort, spec in args.keten:
            mod, naam, van, naar = _parse_been_spec(spec)
            if soort == "been":
                benen.append(_route_been(args, graaf, cache, m, comb,
                                         mod, naam, van, naar))
            else:
                benen.append(_stippel_been(mod, naam, van, naar))
        # terugval-markers (alleen gebruikt zónder --marker): eindpunten
        p0 = benen[0]["punten"][0]
        auto_markers = [_marker(f"start · {benen[0]['naam']}", p0[0], p0[1])]
        for b in benen:
            pe = b["punten"][-1]
            auto_markers.append(_marker(f"eind · {b['naam']}", pe[0], pe[1]))
    else:
        benen, auto_markers = _route_vrij(args, graaf, cache, m, comb, conn_km)

    # ── markers: expliciet (--marker) vervangt de afleiding volledig ──────
    if args.marker:
        markers = [_marker(naam, lat, lon)
                   for naam, lat, lon in map(_parse_marker_spec, args.marker)]
    else:
        markers = auto_markers

    # ── uitvoer volgens het contract (versie 2): [lon, lat], 5 decimalen ──
    uit_benen = []
    for b in benen:
        d = {"modaliteit": b["modaliteit"], "naam": b["naam"]}
        if b.get("stippel"):
            d["stippel"] = True
        d["km"] = round(b["km"], 1)
        d["punten"] = [[round(q[1], 5), round(q[0], 5)] for q in b["punten"]]
        uit_benen.append(d)
    if args.spoor_geojson:
        sp_punten, sp_km = _spoor_been(args.spoor_geojson)
        uit_benen.append({"modaliteit": "spoor", "naam": args.spoor_naam,
                          "km": round(sp_km, 1),
                          "punten": [[round(lo, 5), round(la, 5)]
                                     for lo, la in sp_punten]})
        if not args.marker:
            markers.append(_marker(args.spoor_naam,
                                   sp_punten[-1][1], sp_punten[-1][0]))

    doc = {"versie": 2, "stroom": args.stroom, "titel": args.titel}
    if args.routebrief:
        doc["routebrief"] = args.routebrief
    doc.update({"gemaakt": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "punt_formaat": "lonlat", "benen": uit_benen,
                "markers": markers})
    uit = Path(args.uit)
    uit.parent.mkdir(parents=True, exist_ok=True)
    uit.write_text(json.dumps(doc, ensure_ascii=False,
                              separators=(",", ":")), encoding="utf-8")

    print("\n── STROOMROUTE GEBAKKEN (contract versie 2) ──")
    for b in uit_benen:
        stip = " · stippel" if b.get("stippel") else ""
        print(f"  {b['modaliteit']:<12} {b['km']:>9,.1f} km · "
              f"{len(b['punten']):>5,} punten{stip} · {b['naam']}")
    print(f"  totaal       {sum(b['km'] for b in uit_benen):>9,.1f} km · "
          f"{sum(len(b['punten']) for b in uit_benen):,} punten · "
          f"{len(markers)} markers")
    for mk in markers:
        print(f"  marker: {mk['naam']}  ({mk['lat']}, {mk['lon']})")
    print(f"geschreven: {uit} · {uit.stat().st_size/1024:.1f} KB")


# ── STAP 1 · de overlapzone MÉTEN i.p.v. aannemen ──────────────────────────

def _ringen_uit(paden):
    uit = []
    for pad in paden:
        for pl in _ringen(pad):
            for r in pl:
                uit.append(np.asarray(r, dtype=np.float64))
    return uit


def cmd_overlap(args):
    """Hoe ver lopen de tracks werkelijk de zee op, per bron?

    ZEE     = buiten ne_10m_land + minor_islands + lakes op een 0,02°-raster
              (~2,2 km). Een Mississippi-punt bij Memphis valt in een landcel
              (de rivier is smaller dan de cel) en telt dus NIET als zee —
              precies de bedoeling, anders leest 600 km landinwaarts als
              '600 km de zee op'. Meren tellen als niet-zee, anders wordt de
              Seaway een oceaan.
    ZEE-KM  = grootcirkel tot de dichtstbijzijnde kustlijn-vertex van dezelfde
              1:10M-wereld die de bol tekent (puntafstand ~1,5 km, dus de
              meetfout is < 1 km — ruim onder de 40-80 km uit de spec).
    """
    from PIL import Image, ImageDraw
    ne = Path(args.ne)
    t0 = time.monotonic()
    res = args.raster
    nx, ny = int(round(360 / res)), int(round(180 / res))
    img = Image.new("1", (nx, ny), 0)
    dr = ImageDraw.Draw(img)
    for f in ("ne_10m_land.geojson", "ne_10m_minor_islands.geojson",
              "ne_10m_lakes.geojson"):
        for r in _ringen_uit([ne / f]):
            dr.polygon(list(zip(((r[:, 0] + 180.0) / res).tolist(),
                                ((r[:, 1] + 90.0) / res).tolist())), fill=1)
    masker = np.array(img, dtype=bool)
    kust = np.concatenate(_ringen_uit([ne / "ne_10m_land.geojson",
                                       ne / "ne_10m_minor_islands.geojson"]))
    kust_boom = cKDTree(xyz(kust[:, 1], kust[:, 0]))
    print(f"landmasker {nx}x{ny} · {masker.mean()*100:.1f}% niet-zee · "
          f"{len(kust):,} kustlijn-vertices · {time.monotonic()-t0:.0f}s")

    m = lees_marnet(args.marnet)
    z = marnet_zee(m, vermijd=())
    knoop_boom = cKDTree(xyz(z["lat"], z["lon"]))
    g_ix = np.concatenate([np.arange(m["geom_start"][e], m["geom_start"][e + 1])
                           for e in z["edge"]])
    gxyz = xyz(m["geom_lat"][g_ix], m["geom_lon"][g_ix])
    vert_boom = cKDTree(gxyz)
    edge_van_vertex = np.repeat(np.arange(len(z["edge"])), m["edge_n"][z["edge"]])
    print(f"MARNET-zee: {len(z['edge']):,} edges · {z['km'].sum():,.0f} km · "
          f"{len(z['lat']):,} knopen · {len(g_ix):,} geometrie-vertices "
          f"({z['km'].sum()/len(g_ix):.2f} km per vertex)")

    def lijn_km(P, kand):
        """Afstand tot het dichtstbijzijnde MARNET-LIJNSTUK (niet vertex)."""
        best = np.full(len(P), np.inf)
        for kk in range(kand.shape[1]):
            j = kand[:, kk]
            for buur in (-1, 1):
                jb = np.clip(j + buur, 0, len(gxyz) - 1)
                geldig = (edge_van_vertex[jb] == edge_van_vertex[j]) & (jb != j)
                A, B = gxyz[j], gxyz[jb]
                AB = B - A
                l2 = np.maximum(np.einsum("ij,ij->i", AB, AB), 1e-30)
                t = np.clip(np.einsum("ij,ij->i", P - A, AB) / l2, 0.0, 1.0)
                d = np.linalg.norm(P - (A + t[:, None] * AB), axis=1)
                best = np.minimum(best, np.where(geldig, d, np.inf))
        return boog_km(best)

    uitslag = {}
    for pad in args.tracks:
        pad = Path(pad)
        naam = pad.stem.replace(".jsonl", "")
        t1 = time.monotonic()
        n_regels = sum(1 for _ in gzip.open(pad, "rt", encoding="utf-8"))
        tmax = np.zeros(n_regels)
        n_pt = n_zee = 0
        dl_s, dk_s, dv_s = [], [], []
        buf_la, buf_lo, buf_id = [], [], []

        def verwerk():
            nonlocal n_zee
            if not buf_la:
                return
            la = np.concatenate(buf_la)
            lo = np.concatenate(buf_lo)
            tid = np.concatenate(buf_id)
            buf_la.clear(); buf_lo.clear(); buf_id.clear()
            iy = np.clip(((la + 90.0) / res).astype(np.int64), 0, ny - 1)
            ix = np.clip(((lo + 180.0) / res).astype(np.int64), 0, nx - 1)
            zeep = ~masker[iy, ix]
            if not zeep.any():
                return
            la, lo, tid = la[zeep], lo[zeep], tid[zeep]
            P = xyz(la, lo)
            zkm = boog_km(kust_boom.query(P, workers=-1)[0])
            n_zee += len(zkm)
            np.maximum.at(tmax, tid, zkm)
            houd = np.arange(0, len(zkm), max(1, len(zkm) // 40000))
            dk_s.append(boog_km(knoop_boom.query(P[houd], workers=-1)[0])
                        .astype(np.float32))
            dv, vi = vert_boom.query(P[houd], k=3, workers=-1)
            dv_s.append(boog_km(dv[:, 0]).astype(np.float32))
            dl_s.append(lijn_km(P[houd], vi).astype(np.float32))

        with gzip.open(pad, "rt", encoding="utf-8") as fh:
            for nr, regel in enumerate(fh):
                arr = np.asarray(json.loads(regel)["punten"], dtype=np.float64)
                n_pt += len(arr)
                buf_la.append(arr[:, 0])
                buf_lo.append(arr[:, 1])
                buf_id.append(np.full(len(arr), nr, dtype=np.int64))
                if sum(len(a) for a in buf_la) >= 400_000:
                    verwerk()
        verwerk()

        def q(a, p):
            a = np.concatenate(a) if isinstance(a, list) and a else a
            return float(np.percentile(a, p)) if len(a) else float("nan")
        dl = np.concatenate(dl_s) if dl_s else np.zeros(0, np.float32)
        pos = tmax[tmax > 0]
        u = {"tracks": n_regels, "punten": n_pt, "zee_punten": int(n_zee),
             "zee_aandeel": round(n_zee / max(n_pt, 1), 4),
             "tracks_met_zeepunt": int((tmax > 0).sum()),
             "zee_km_per_track": {"p50": q(pos, 50), "p90": q(pos, 90),
                                  "p99": q(pos, 99), "max": float(tmax.max())},
             "tracks_verder_dan_km": {str(g): int((tmax > g).sum())
                                      for g in (10, 20, 40, 80, 150, 300)},
             "zeepunt_tot_marnet_km": {
                 "knoop_p50": q(dk_s, 50), "vertex_p50": q(dv_s, 50),
                 "lijn_p50": q(dl_s, 50),
                 "aandeel_lijn_binnen": {str(g): round(float((dl <= g).mean()), 4)
                                         for g in (0.5, 1, 2, 5, 10)}},
             "seconden": round(time.monotonic() - t1, 1)}
        uitslag[naam] = u
        print(f"\n=== {naam} ===")
        print(f"  {n_regels:,} tracks · {n_pt:,} punten · {n_zee:,} op zee "
              f"({u['zee_aandeel']*100:.1f}%) · {u['seconden']}s")
        print(f"  max zee-km per track: p50 {u['zee_km_per_track']['p50']:.1f} · "
              f"p90 {u['zee_km_per_track']['p90']:.1f} · "
              f"p99 {u['zee_km_per_track']['p99']:.1f} · "
              f"max {u['zee_km_per_track']['max']:.1f}")
        print("  tracks verder dan: " + " · ".join(
            f"{g} km {n:,}" for g, n in u["tracks_verder_dan_km"].items()))
        print(f"  zeepunt -> MARNET: knoop p50 "
              f"{u['zeepunt_tot_marnet_km']['knoop_p50']:.1f} km · vertex p50 "
              f"{u['zeepunt_tot_marnet_km']['vertex_p50']:.1f} · LIJN p50 "
              f"{u['zeepunt_tot_marnet_km']['lijn_p50']:.2f}")
        print("  aandeel zeepunten binnen X km van de MARNET-lijn: " + " · ".join(
            f"{g} km {v*100:.1f}%" for g, v in
            u["zeepunt_tot_marnet_km"]["aandeel_lijn_binnen"].items()))
    Path(args.uit).write_text(json.dumps(
        {"definities": {"zee": f"buiten land+eilanden+meren op {res}-raster",
                        "zee_km": "grootcirkel tot dichtstbijzijnde "
                                  "kustlijn-vertex (1:10M)"},
         "marnet_zee": {"edges": int(len(z["edge"])),
                        "km": float(z["km"].sum()),
                        "knopen": int(len(z["lat"])),
                        "geom_vertices": int(len(g_ix))},
         "per_bron": uitslag}, indent=1), encoding="utf-8")
    print(f"\ngeschreven: {args.uit} · totaal {time.monotonic()-t0:.0f}s")


class _KetenActie(argparse.Action):
    """--been en --stippel delen ÉÉN lijst (dest='keten'), in de volgorde van
    de commandoregel — want de benen-volgorde in de uitvoer ís de
    reisvolgorde, en met twee losse append-lijsten zou een stippel-been
    (last mile) nooit tússen twee geroutete benen kunnen liggen."""

    def __call__(self, parser, namespace, values, option_string=None):
        lst = getattr(namespace, self.dest, None) or []
        lst.append(("stippel" if option_string == "--stippel" else "been",
                    values))
        setattr(namespace, self.dest, lst)


def main():
    ap = argparse.ArgumentParser(description="MARNET-aanhechting op echte "
                                             "trackgeometrie")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def gedeeld(s):
        s.add_argument("--graaf", required=True)
        s.add_argument("--marnet", required=True,
                       help="map met marnet.bin + marnet.json (van tag "
                            "pre-ais-net; NIET v2/data/)")
        s.add_argument("--eps", type=float, default=EPS_KM)
        s.add_argument("--overstap-boete", type=float, default=G.OVERSTAP_BOETE)
        s.add_argument("--boete-connector", type=float,
                       default=G.OVERSTAP_BOETE, help="prijs van één overstap "
                       "track <-> MARNET; zie de boete-curve in de kop")
        s.add_argument("--ne", default=None,
                       help="map met ne_10m_land.geojson + "
                            "ne_10m_minor_islands.geojson (landtoets)")
        s.add_argument("--vermijd", nargs="*", default=["northwest"],
                       help="MARNET-passages die dicht zijn (M23-default: "
                            "northwest); geef leeg voor alles open")
        s.add_argument("--data", default=str(Path(__file__).resolve()
                                             .parent.parent / "data"))

    s = sub.add_parser("hecht", help="connectors berekenen + wegschrijven")
    gedeeld(s)
    s.add_argument("--eps-reeks", type=float, nargs="+",
                   default=[0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])
    s.set_defaults(fn=cmd_hecht)

    s = sub.add_parser("havens", help="snap per haven voor en na")
    gedeeld(s)
    s.set_defaults(fn=cmd_havens)

    s = sub.add_parser("overlap", help="hoe ver lopen de tracks de zee op?")
    s.add_argument("--tracks", nargs="+", required=True)
    s.add_argument("--marnet", required=True)
    s.add_argument("--ne", required=True)
    s.add_argument("--raster", type=float, default=0.02)
    s.add_argument("--uit", default="overlap.json")
    s.set_defaults(fn=cmd_overlap)

    s = sub.add_parser("regressie", help="route voor/na + eiland + metrics")
    gedeeld(s)
    s.add_argument("--van", required=True)
    s.add_argument("--naar", required=True)
    s.add_argument("--verwacht-km", type=float, default=None)
    s.add_argument("--eiland-van", default=None,
                   help="probe beneden het eiland (lat,lon)")
    s.add_argument("--eiland-naar", default=None, help="probe boven het eiland")
    s.add_argument("--eiland-via", default=None,
                   help="punt in de ANDERE arm — zonder dit vindt de toets een "
                        "parallelle doorvaart in dezelfde geul")
    s.set_defaults(fn=cmd_regressie)

    s = sub.add_parser("route", help="één stroom bakken tot een statisch "
                                     "databestand voor de bol")
    gedeeld(s)
    s.add_argument("--van", default=None,
                   help="vrije modus (alleen zonder --been): startpunt")
    s.add_argument("--naar", default=None,
                   help="vrije modus (alleen zonder --been): eindpunt")
    s.add_argument("--been", dest="keten", action=_KetenActie, default=None,
                   metavar="MOD|NAAM|VAN_LAT,VAN_LON|NAAR_LAT,NAAR_LON",
                   help="herhaalbaar: één been, APART geroutet over het "
                        "gecombineerde net; modaliteit uit de vlag (routebrief-"
                        "modus — overslag op aangewezen punten)")
    s.add_argument("--stippel", dest="keten", action=_KetenActie,
                   metavar="MOD|NAAM|VAN_LAT,VAN_LON|NAAR_LAT,NAAR_LON",
                   help="herhaalbaar: been dat NIET geroutet wordt — rechte "
                        "lijn tussen de twee punten, 'stippel': true (eigen "
                        "verbinding, zoals de last mile kade → fabriek)")
    s.add_argument("--marker", action="append", default=None,
                   metavar="NAAM|LAT,LON",
                   help="herhaalbaar: expliciete marker; zodra er één is "
                        "opgegeven vervangt de lijst de automatische "
                        "afleiding volledig")
    s.add_argument("--routebrief", default=None,
                   help="pad van de routebrief die deze keten voorschrijft; "
                        "gaat als veld het contract in")
    s.add_argument("--uit", required=True, help="uitvoerpad (JSON-contract)")
    s.add_argument("--stroom", required=True, help="stroom-id, bv. "
                                                   "grafiet-balama-vs")
    s.add_argument("--titel", required=True)
    s.add_argument("--spoor-geojson", default=None,
                   help="GeoJSON met een LineString/MultiLineString van het "
                        "spoorbeen ([lon,lat]; uit toets_spoorroute.mjs) — "
                        "wordt als los been 'spoor' achteraan gezet")
    s.add_argument("--spoor-naam", default="spoor-eindpunt",
                   help="markernaam voor het eindpunt van het spoorbeen")
    s.set_defaults(fn=cmd_route)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
