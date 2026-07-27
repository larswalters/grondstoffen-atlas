# bouw_trackgraaf.py — DE TRACK-GRAAF (LAR-530): het vaarnet IS de verzameling
# gevaren lijnen. Twee lagen, geen enkele herrekende geometrie.
#
# ── WAAROM DEZE VORM — de Vidalia-toets besliste het ────────────────────────
# Voor New Orleans -> Syrah Vidalia (~431 km Mississippi) gaf een graaf op
# CELCENTRA **-7,4%** lengte en volgens Lars "onrealistisch hoekig"; de ÉCHTE
# gevaren lijn van één duwboot gaf **-0,1%** (430,6 km). Elke stap die
# geometrie hérrekent — een raster, een skelet, een centerline, een gemiddelde —
# kost lengte én vorm. Dus rekenen we hier nergens geometrie uit. We knippen
# bestaande punten­reeksen, en dat is alles.
#
# ── ER WORDT NIET GEBUNDELD. NERGENS. (besluit Lars, 2026-07-27) ────────────
# Lars: *"veel tracks is juist de bedoeling ... als er hele tracks vanaf de
# juiste zeehaven naar de juiste fabriekshaven liggen gebruiken we die specifiek
# voor die route, dat is het mooiste ... bundelen is dus niet nodig maar wel
# langs beide geulen moeten sporen lopen."* Dus: geen representant per bundel,
# geen dedup van "dezelfde" doorvaart, geen middeling. Elke doorvaart blijft een
# eigen echte lijn. Dat is per constructie ook de beste bescherming tegen
# foutmodus (a) — twee geulen om een eiland die tot één lijn samensmelten:
# zolang niets wordt gemiddeld kan een arm niet verdwijnen.
#
# ── LAAG 1 · DE HELE-TRACK-MATCH (primair, "het mooiste") ───────────────────
# Vraag: is er een track die zélf al van bij A naar bij B loopt? Zo ja, dán IS
# die track de route: de echte gevaren lijn van één schip, kade tot kade, op
# GPS-precisie. Geen graaf, geen stitching, geen keuze-artefact. De Vidalia-
# meting die dit ontwerp besliste was precies dat. Laag 1 rapporteert de HELE
# verdeling (hoeveel doorvaarten, welke lengtes, welke snaps) — meerdere echte
# doorvaarten van dezelfde route is het doel, niet ruis.
#
# ── LAAG 2 · DE GRAAF OP RAAKPUNTEN (voor wat laag 1 niet dekt) ─────────────
# Knoop = een ~200 m-cel die door >= 2 VERSCHILLENDE tracks wordt geraakt (een
# raakpunt), plus elke track-uiteinde-cel (dat is het dok-materiaal van
# LAR-531). Een route is een keten van track-SEGMENTEN: bij een raakpunt stap je
# van de ene track op de andere. Uitsluitend echte gevaren geometrie.
#
# ── EEN EDGE IS EEN VERWIJZING, GEEN GEKOPIEERDE GEOMETRIE ──────────────────
# edge = (trackset-index, REGELNUMMER, begin-index, eind-index) + knoop_a,
# knoop_b + echte km. De geometrie bestaat dus exact één keer, in de trackset.
# Gevolg: "niet bundelen" kost geen opslag-explosie, en het is per constructie
# ONMOGELIJK dat er een gemiddelde of een celcentrum in een edge sluipt — er is
# geen plek waar zoiets zou kunnen staan.
# **Track-id = <bestandsstam>#<regelnummer>** (0-gebaseerd, regel in het
# .jsonl.gz). mmsi alléén is níet uniek: één schip heeft tientallen tracks.
# Knoop-coördinaten zijn óók echte trackpunten (het eerste punt dat de cel
# claimde), nooit een celcentrum — de cel is alleen de sleutel waarop twee
# tracks elkaar herkennen.
#
# ── DE VALKUIL DIE HIERIN ZIT (lees dit voor je een parameter draait) ───────
# 1. **Kortste-pad over een bundel echte banen KORT DE ROUTE SYSTEMATISCH AF —
#    en dat is hier gemeten, niet bedacht.** Zonder tegenwicht springt het
#    kortste pad bij elke bocht over op de track die net iets binnendoor lag;
#    elke sprong wint een paar meter en samen kost dat procenten. Daarom een
#    OVERSTAP-BOETE per track-wissel.
#    Gemeten op New Orleans -> Vidalia, op de HERBOUWDE tracksets van
#    2026-07-27 (referentie 431 km; laag 1 geeft 432,0 km met één hele track):
#      boete  0 km -> 397,6 km (-7,8%) · 346 wissels over 321 tracks  <- kapot
#             2 km -> 416,5 km (-3,4%) ·   7 wissels
#             5 km -> 421,3 km (-2,2%) ·   5 wissels
#            10 km -> 421,3 km (-2,2%) ·   5 wissels
#          **12 km -> 432,3 km (+0,3%) ·   4 wissels**
#            15/20/30/40/80/160/320 km -> 432,3 km, exact dezelfde route
#    Het plateau loopt dus van 12 tot minstens 320 km: over een factor 26 in de
#    parameter verandert er geen meter. Default 25 km ligt daar ruim in.
#    ⚠️ De vorige default (10) kwam van de curve op de tracksets van vóór de
#    knip-fix, waar het plateau bij 10-20 lag. Na de herbouw ligt de knik tussen
#    10 en 12 — de oude default stond dus precies op de rand, de enige plek waar
#    een parameter niet hoort te staan. Hermeet deze curve als de tracksets
#    opnieuw worden gebouwd; het is één commando per punt (`route
#    --overstap-boete`) en het is de enige parameter hier die iets kan verbergen.
#    Onafhankelijke bevestiging dat 432 de juiste orde is: laag 1 kent GEEN
#    boete (het is één ongewijzigde track) en komt op 432,0 km — 0,07% van wat
#    laag 2 op het plateau geeft.
#    ⚠️ De boete is GEEN geometrie en verandert de gerapporteerde lengte niet —
#    die blijft de lengte van de getekende lijn. Hij drukt uit wat Lars ook zegt:
#    liever wat verder op dezelfde échte gevaren lijn dan een baanwissel voor
#    marginale winst; een gestitchte route is zwakker bewijs dan één doorvaart.
#    Twee guards op de geometrie zelf:
#      * `--min-seg-km` — minimum edge-lengte, dus geen baanwissel elke 200 m;
#      * `--max-stap-km` — een edge met twee opeenvolgende trackpunten verder dan
#        dit uit elkaar gaat WEG. Zo'n stap is een ONGEOBSERVEERDE koorde
#        (bouw_tracks knipt pas bij een gat > 30 min, dus een rechte lijn over
#        een bocht kan blijven staan). Effect gemeten op de tracksets van vóór de
#        knip-fix: klein (2,0 -> 0,4 km scheelde 0,8 procentpunt), dus de koorden
#        waren daar NIET de oorzaak van de verkorting — de bundel was het.
#        ⚠️ Niet hermeten na de herbouw; de default 2,0 km wierp op de
#        Mississippi-corridor 19.847 edges weg (0,7% van 2,80 mln).
#    Wat er ná de boete overblijft is echt: laag 2 mag een kortere, óók echt
#    gevaren zijgeul nemen die de referentiedoorvaart niet nam. Laag 2 is
#    daarmee een ONDERGRENS voor een werkelijke reis, geen schatting ervan —
#    en dat is precies waarom laag 1 primair is.
# 2. **Op-/afvaart mag GEEN eigen knoop-ruimte krijgen.** Verleidelijk (het zijn
#    eigen banen) maar fataal: dan liggen er twee parallelle netwerken die nooit
#    samenkomen en kan er niets langs routeren — foutmodus (b), die het
#    gevaarlijkst is omdat de graaf compleet lijkt. Richting is hier daarom een
#    LABEL op de edge (eigen banen, eigen geometrie, eigen km) op ÉÉN gedeelde
#    knoop-ruimte. `eiland` toetst dat de twee geulen om een eiland boven en
#    onder een knoop-id delen, en noemt die ids.
# 3. Cellen worden in de lengte cos(lat)-gecorrigeerd, dus ~200 m in beide
#    richtingen op elke breedte. Zonder dat is een cel op de Rijn 38% smaller
#    dan op de Mississippi en verschuift de knoopdichtheid met de breedtegraad.
#
# ── UITVOER (formaat dat fase 3 kan bakken) ─────────────────────────────────
#   <uit>.json         manifest: parameters, tracksets, metrics, array-uitleg
#   <uit>.npz          de graaf zelf: knoop_lat/knoop_lon + edge_* arrays
#   <uit>-tracks.npz   geometrie-cache: de gebruikte tracks als platte arrays
#                      (afgeleid, byte-voor-byte de waarden uit de trackset;
#                       de trackset blijft de bron — `bewijs` leest die terug)
# Zelfde tweedeling als marnet.bin + marnet.json: binair payload, JSON meta.
#
# ── DRAAIEN ────────────────────────────────────────────────────────────────
#   # laag 1 — hele-track-match (streamt de trackset, geen graaf nodig)
#   python v2/tools/bouw_trackgraaf.py laag1 \
#       --tracks v2/build-cache/ais/tracks/vs-landelijk.jsonl.gz \
#       --van neworleans --naar vidalia --snap 0.5
#
#   # laag 2 — graaf bouwen (cache + graaf in één keer)
#   python v2/tools/bouw_trackgraaf.py graaf \
#       --tracks .../vs-landelijk.jsonl.gz --bbox 29.4,-92.2,32.2,-89.4 \
#       --uit v2/build-cache/ais/graaf/mississippi
#
#   # de acceptatietoets: beide lagen + geometrie-bewijs
#   python v2/tools/bouw_trackgraaf.py toets --graaf .../mississippi \
#       --van neworleans --naar vidalia --snap 0.5 --verwacht-km 431
#
#   # eiland — eerst kandidaten zoeken, dan toetsen MET --via in de andere arm
#   python v2/tools/bouw_trackgraaf.py eiland --graaf .../mississippi --zoek \
#       --bbox 29.9,-91.7,31.7,-89.9 --min-sep 0.8 --max-sep 4.0
#   python v2/tools/bouw_trackgraaf.py eiland --graaf .../mississippi \
#       --van 30.560,-91.245 --naar 30.620,-91.293 --via 30.585,-91.271
#
#   python v2/tools/bouw_trackgraaf.py diagnose --graaf .../rijn \
#       --van emo --naar schwelgern --corridor-as lon
#
# ── SCHAAL (gemeten 2026-07-27, deze machine) ───────────────────────────────
# Eén streaming-pass over ALLE VIER de bronnen (725.841 tracks / 119,1 mln
# punten): **72 s**. De graaf is bewust CORRIDOR-scoped via --bbox, en dat is
# geen luxe: de Mississippi-corridor (43.544 tracks / 8,17 mln punten ->
# 2,80 mln edges) piekt op **1,94 GB** en 69 s totaal. Lineair doorgetrokken
# naar alles-in-één-graaf (~41 mln edges, ~161 mln bogen) is dat ~28 GB — dat
# past niet. Wil je ooit één wereldgraaf, dan is de router de post die het kost
# (b_from/b_to/b_w/b_eid + de lexsort-kopieën), niet de graaf zelf.
# ⚠️ --bbox filtert op OVERLAP van de track-bounding-box en knipt tracks NIET:
# een doorgaande track die de bbox raakt gaat in zijn geheel mee. Dat is nodig
# (laag 1 wil de hele lijn) maar het betekent dat de cache veel groter kan zijn
# dan de corridor — gemeten: een bbox van 0,02° in Deens water hield 4.346
# tracks / 7,10 mln punten vast.

import argparse
import gzip
import heapq
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

R_AARDE = 6371.0
CEL_KM = 0.2                      # ~200 m — de raakpunt-korrel
CEL_GRADEN = CEL_KM / 111.32
MIN_SEG_KM = 0.5                  # minimum edge-lengte (zie valkuil 1)
MAX_STAP_KM = 2.0                 # stap tussen twee trackpunten = ongeobserveerd
SNAP_KM = 0.5                     # acceptatie-eis van de Vidalia-toets
KAND_KM = 3.0                     # tot hier zoekt laag 1 kandidaten (dok-bewijs 3 km)
OVERSTAP_BOETE = 25.0             # km-opslag per track-wissel — GEMETEN, zie de kop
                                  # (plateau 12..>=320 km; 25 ligt er ruim in)

# Referentiepunten. Coördinaten NIET hier bedacht — herkomst per punt.
PUNTEN = {
    "neworleans":  (29.95, -90.07,
                    "gr-port-neworleans, data/graphite.js"),
    "vidalia":     (31.57, -91.42,
                    "gr-ref-vidalia (Syrah-anodefabriek), data/graphite.js"),
    "batonrouge":  (30.4396, -91.1983,
                    "knooppunten.json baton-rouge, aanhechting 'binnen'"),
    "no-binnen":   (29.953, -90.0286,
                    "knooppunten.json new-orleans, aanhechting 'binnen'"),
    "emo":         (51.94109, 4.05354,
                    "coal-rotterdam-kade (EMO Maasvlakte), v2/data/aansluitingen.json"),
    "schwelgern":  (51.51321, 6.72347,
                    "coal-duisburg-kade (Schwelgern-pier), v2/data/aansluitingen.json"),
    "waalhaven":   (51.89369, 4.39341,
                    "cu-rotterdam-kade (Waalhaven), v2/data/aansluitingen.json"),
    "ruhrort":     (51.45187, 6.7559,
                    "cu-duisburg-kade (Duisport Ruhrort), v2/data/aansluitingen.json"),
    "wesel":       (51.65, 6.55,
                    "midden van het gemeten Wesel-gat (memory/bugs-and-risks.md)"),
}


# ── afstand ────────────────────────────────────────────────────────────────
# Zelfde equirectangular formule als bouw_tracks.py, zodat km hier en km in de
# trackset dezelfde grootheid zijn (de 430,6 km-referentie is zo gemeten).

def km(lat1, lon1, lat2, lon2):
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1) * math.cos(math.radians((lat1 + lat2) / 2))
    return R_AARDE * math.hypot(dlat, dlon)


def km_np(la, lo, lat0, lon0):
    dlat = np.radians(la - lat0)
    dlon = np.radians(lo - lon0) * np.cos(np.radians((la + lat0) * 0.5))
    return R_AARDE * np.hypot(dlat, dlon)


def seg_km_np(la, lo):
    """Lengte per segment langs een puntenreeks (n-1 waarden)."""
    dlat = np.radians(la[1:] - la[:-1])
    dlon = (np.radians(lo[1:] - lo[:-1])
            * np.cos(np.radians((la[1:] + la[:-1]) * 0.5)))
    return R_AARDE * np.hypot(dlat, dlon)


def cel_sleutels(la, lo):
    """~200 m-cel, in de lengte cos(lat)-gecorrigeerd. Deterministisch."""
    iy = np.floor(la / CEL_GRADEN).astype(np.int64)
    cosr = np.cos(np.radians(iy * CEL_GRADEN))
    ix = np.floor(lo * cosr / CEL_GRADEN).astype(np.int64)
    return (iy + 1_000_000) * 4_000_003 + (ix + 2_000_000)


def parse_punt(spec):
    if spec in PUNTEN:
        lat, lon, bron = PUNTEN[spec]
        return lat, lon, spec, bron
    lat, lon = (float(x) for x in spec.split(","))
    return lat, lon, spec, "handmatig meegegeven"


def pct(v, q):
    return float(np.percentile(np.asarray(v, dtype=float), q)) if len(v) else float("nan")


# ── inlezen: één streaming pass over de tracksets ──────────────────────────

def lees_tracksets(paden, bbox=None, doelen=(), kand_km=KAND_KM,
                   max_regels=None, stil=False):
    """Streamt alle tracksets één keer.

    Geeft (cache, doelmeting):
      cache      – de tracks BINNEN bbox als platte arrays (bbox=None: alles)
      doelmeting – per track die binnen kand_km van >= 1 doelpunt komt:
                   de snap-afstanden en de puntindices. Dit is de grondstof
                   voor laag 1 en die kijkt NIET naar de bbox: een hele-track-
                   match mag onderweg overal komen.
    """
    z = w = n_ = o = None
    if bbox:
        z, w, n_, o = bbox
    lat_d = np.array([d[0] for d in doelen], dtype=np.float64)
    lon_d = np.array([d[1] for d in doelen], dtype=np.float64)

    c_lat, c_lon, c_t = [], [], []
    c_start, c_regel, c_set, c_op, c_kmbron = [0], [], [], [], []
    tracksets = []
    doelmeting = {}                      # (set_ix, regel) -> record
    n_gezien = n_in_bbox = 0
    kmbron_ratio = []
    t0 = time.monotonic()

    for set_ix, pad in enumerate(paden):
        pad = Path(pad)
        n_regels = 0
        with gzip.open(pad, "rt", encoding="utf-8") as fh:
            for regel_nr, regel in enumerate(fh):
                if max_regels and regel_nr >= max_regels:
                    break
                n_regels = regel_nr + 1
                t = json.loads(regel)
                n_gezien += 1
                arr = np.asarray(t["punten"], dtype=np.float64)
                la, lo = arr[:, 0], arr[:, 1]
                seg = seg_km_np(la, lo)
                cum = np.empty(len(la))
                cum[0] = 0.0
                np.cumsum(seg, out=cum[1:])

                # laag 1: hoe dicht komt deze track bij de doelpunten?
                if len(doelen):
                    dmin, iarg = [], []
                    treffers = []
                    for k in range(len(doelen)):
                        d = km_np(la, lo, lat_d[k], lon_d[k])
                        j = int(np.argmin(d))
                        dmin.append(float(d[j]))
                        iarg.append(j)
                        treffers.append(np.flatnonzero(d <= kand_km)
                                        if d[j] <= kand_km else None)
                    if min(dmin) <= kand_km:
                        doelmeting[(set_ix, regel_nr)] = {
                            "mmsi": t["mmsi"], "km_bron": t["km"],
                            "dmin": dmin, "iarg": iarg, "treffers": treffers,
                            "cum": cum, "la": la, "lo": lo,
                            "n": len(la),
                        }

                if bbox and not (la.max() >= z and la.min() <= n_
                                 and lo.max() >= w and lo.min() <= o):
                    continue
                n_in_bbox += 1
                c_lat.append(la)
                c_lon.append(lo)
                c_t.append(arr[:, 2].astype(np.int32))
                c_start.append(c_start[-1] + len(la))
                c_regel.append(regel_nr)
                c_set.append(set_ix)
                dl, dlo = t["dlat"], t["dlon"]
                dominant = dl if abs(dl) >= abs(dlo) else dlo
                c_op.append(1 if dominant > 0 else 0)
                c_kmbron.append(t["km"])
                if t["km"] > 5:
                    kmbron_ratio.append(cum[-1] / t["km"])

        tracksets.append({"stam": pad.stem.replace(".jsonl", ""),
                          "pad": str(pad), "regels": n_regels})
        if not stil:
            print(f"  {pad.name}: {n_regels:,} tracks gelezen "
                  f"({time.monotonic()-t0:.0f}s)", flush=True)

    cache = {
        "lat": np.concatenate(c_lat) if c_lat else np.zeros(0),
        "lon": np.concatenate(c_lon) if c_lon else np.zeros(0),
        "t": np.concatenate(c_t) if c_t else np.zeros(0, np.int32),
        "start": np.array(c_start, dtype=np.int64),
        "regel": np.array(c_regel, dtype=np.int64),
        "set": np.array(c_set, dtype=np.int16),
        "op": np.array(c_op, dtype=np.uint8),
        "km_bron": np.array(c_kmbron, dtype=np.float64),
        "tracksets": tracksets,
        "bbox": list(bbox) if bbox else None,
    }
    if not stil:
        print(f"gelezen: {n_gezien:,} tracks · {n_in_bbox:,} binnen bbox · "
              f"{len(cache['lat']):,} punten · {time.monotonic()-t0:.0f}s")
        if kmbron_ratio:
            r = np.array(kmbron_ratio)
            print(f"  ijking km-formule tegen 'km' in de trackset: "
                  f"mediaan {np.median(r):.5f} (1,0 = identiek)")
    return cache, doelmeting


def bewaar_cache(pad: Path, cache):
    np.savez(pad, lat=cache["lat"], lon=cache["lon"], t=cache["t"],
             start=cache["start"], regel=cache["regel"], set=cache["set"],
             op=cache["op"], km_bron=cache["km_bron"])
    (pad.parent / (pad.name + ".meta.json")).write_text(
        json.dumps({"tracksets": cache["tracksets"], "bbox": cache["bbox"]},
                   ensure_ascii=False, indent=1), encoding="utf-8")


def laad_cache(pad: Path):
    d = np.load(str(pad) if str(pad).endswith(".npz") else str(pad) + ".npz")
    meta = json.loads((pad.parent / (pad.name + ".meta.json")).read_text(
        encoding="utf-8")) if (pad.parent / (pad.name + ".meta.json")).exists() \
        else json.loads(Path(str(pad) + ".meta.json").read_text(encoding="utf-8"))
    cache = {k: d[k] for k in d.files}
    cache["tracksets"] = meta["tracksets"]
    cache["bbox"] = meta["bbox"]
    return cache


# ── LAAG 1 · hele-track-match ──────────────────────────────────────────────

def laag1_kandidaten(doelmeting, ia, ib, snap_km):
    """Tracks die binnen snap_km bij doel ia EN doel ib komen.

    Per kandidaat het indexpaar dat de KORTSTE gevaren afstand tussen de twee
    aanlegpunten geeft (een track kan A meerdere keren passeren; het minimum is
    de doorvaart, niet een rondje).
    """
    uit = []
    for (set_ix, regel), rec in doelmeting.items():
        if rec["dmin"][ia] > snap_km or rec["dmin"][ib] > snap_km:
            continue
        ta, tb = rec["treffers"][ia], rec["treffers"][ib]
        if ta is None or tb is None or not len(ta) or not len(tb):
            continue
        cum = rec["cum"]
        beste = None
        # twee-pointer over gesorteerde indexlijsten
        for i in ta:
            j = tb[np.argmin(np.abs(cum[tb] - cum[i]))]
            d = abs(float(cum[j] - cum[i]))
            if beste is None or d < beste[0]:
                beste = (d, int(i), int(j))
        if beste is None:
            continue
        d, i, j = beste
        uit.append({
            "set": set_ix, "regel": regel, "mmsi": rec["mmsi"],
            "snap_a": rec["dmin"][ia], "snap_b": rec["dmin"][ib],
            "i_a": i, "i_b": j, "km": d, "n_punten": rec["n"],
            "richting_ab": "voorwaarts" if j > i else "achterwaarts",
            "km_hele_track": float(cum[-1]),
        })
    uit.sort(key=lambda k: k["km"])
    return uit


def kies_route(kandidaten, wijze="mediaan"):
    """Welke kandidaat geven we terug als 'de' route?

    'mediaan' (default) — de kandidaat met de MEDIAAN gevaren km. Motivatie:
      het blijft één échte, ongewijzigde track (geen middeling), en de mediaan
      is robuust tegen de twee bekende uitschieters aan weerszijden: een track
      die over een datagat een bocht heeft afgesneden (te kort) en een track die
      onderweg een havenarm in is gevaren of heeft gedraaid (te lang).
    'kort'  — de kortste; 'snap' — de kleinste max-snap.
    De rest blijft opvraagbaar (--alle).
    """
    if not kandidaten:
        return None
    if wijze == "kort":
        return kandidaten[0]
    if wijze == "snap":
        return min(kandidaten, key=lambda k: max(k["snap_a"], k["snap_b"]))
    return kandidaten[len(kandidaten) // 2]


def rapport_laag1(kandidaten, naam_a, naam_b, snap_km, wijze="mediaan"):
    print(f"\n── LAAG 1 · hele-track-match {naam_a} -> {naam_b} "
          f"(snap <= {snap_km} km) ──")
    if not kandidaten:
        print("  GEEN enkele track dekt deze route in zijn geheel.")
        return None
    kms = [k["km"] for k in kandidaten]
    print(f"  {len(kandidaten)} hele tracks dekken de route")
    print(f"  gevaren km : min {min(kms):.1f} · p10 {pct(kms,10):.1f} · "
          f"mediaan {pct(kms,50):.1f} · p90 {pct(kms,90):.1f} · max {max(kms):.1f}")
    print(f"  snap A     : min {min(k['snap_a'] for k in kandidaten):.3f} · "
          f"mediaan {pct([k['snap_a'] for k in kandidaten],50):.3f} km")
    print(f"  snap B     : min {min(k['snap_b'] for k in kandidaten):.3f} · "
          f"mediaan {pct([k['snap_b'] for k in kandidaten],50):.3f} km")
    vw = sum(1 for k in kandidaten if k["richting_ab"] == "voorwaarts")
    print(f"  richting   : {vw} voorwaarts (A->B) · {len(kandidaten)-vw} achterwaarts")
    keus = kies_route(kandidaten, wijze)
    print(f"  GEKOZEN ({wijze}): track-id {stam_van(keus)}  mmsi {keus['mmsi']} · "
          f"{keus['km']:.1f} km · snap {keus['snap_a']:.3f}/{keus['snap_b']:.3f} km · "
          f"punten {keus['i_a']}..{keus['i_b']} van {keus['n_punten']}")
    return keus


def stam_van(k):
    return f"set{k['set']}#{k['regel']}"


# ── LAAG 2 · de graaf ──────────────────────────────────────────────────────

def bouw_graaf(cache, min_seg_km=MIN_SEG_KM, max_stap_km=MAX_STAP_KM, stil=False):
    """Knopen op raakpunten, edges als verwijzing in een track."""
    t0 = time.monotonic()
    lat, lon, start = cache["lat"], cache["lon"], cache["start"]
    n_tracks = len(start) - 1
    sleutels = cel_sleutels(lat, lon)

    # ── knoop-cellen: geraakt door >= 2 VERSCHILLENDE tracks ──
    # per track de UNIEKE cellen (anders telt een schip dat stilligt zichzelf
    # tot knoop), daarna over alle tracks tellen.
    uniek_per_track = []
    for i in range(n_tracks):
        uniek_per_track.append(np.unique(sleutels[start[i]:start[i + 1]]))
    alle = np.concatenate(uniek_per_track) if n_tracks else np.zeros(0, np.int64)
    cellen, tellen = np.unique(alle, return_counts=True)
    knoopcel = cellen[tellen >= 2]

    # uiteinde-cellen zijn altijd knoop (dok-materiaal LAR-531, en zonder dit
    # hangt een unieke track met beide benen in de lucht)
    eind_ix = np.concatenate([start[:-1], start[1:] - 1]) if n_tracks else \
        np.zeros(0, np.int64)
    knoopcel = np.union1d(knoopcel, np.unique(sleutels[eind_ix]))
    knoopcel.sort()

    # knoop-coördinaat = het EERSTE ECHTE TRACKPUNT in die cel (nooit een
    # celcentrum). np.searchsorted geeft per punt zijn knoop-id of -1.
    pos = np.searchsorted(knoopcel, sleutels)
    pos[pos >= len(knoopcel)] = 0
    is_knoop = knoopcel[pos] == sleutels
    knoop_id_per_punt = np.where(is_knoop, pos, -1)
    knoop_lat = np.zeros(len(knoopcel))
    knoop_lon = np.zeros(len(knoopcel))
    ix = np.flatnonzero(is_knoop)
    # laatste toewijzing wint; om "eerste" te krijgen omgekeerd doorlopen
    knoop_lat[knoop_id_per_punt[ix[::-1]]] = lat[ix[::-1]]
    knoop_lon[knoop_id_per_punt[ix[::-1]]] = lon[ix[::-1]]

    # ── edges: knip elke track bij zijn knoop-indices ──
    e_set, e_regel, e_i0, e_i1, e_a, e_b, e_km, e_op = [], [], [], [], [], [], [], []
    e_tix = []
    n_verworpen_stap = n_verworpen_zelf = 0
    for i in range(n_tracks):
        s, e = start[i], start[i + 1]
        la, lo = lat[s:e], lon[s:e]
        seg = seg_km_np(la, lo)
        cum = np.empty(len(la))
        cum[0] = 0.0
        np.cumsum(seg, out=cum[1:])
        kn = knoop_id_per_punt[s:e]
        kandidaat = np.flatnonzero(kn >= 0)
        if len(kandidaat) < 2:
            continue
        # greedy knippen: min. lengte tussen twee knippen, uiteinden altijd mee
        knip = [int(kandidaat[0])]
        for j in kandidaat[1:]:
            if kn[j] == kn[knip[-1]]:
                continue
            if cum[j] - cum[knip[-1]] >= min_seg_km or j == kandidaat[-1]:
                knip.append(int(j))
        for a_ix, b_ix in zip(knip[:-1], knip[1:]):
            ka, kb = int(kn[a_ix]), int(kn[b_ix])
            if ka == kb:
                n_verworpen_zelf += 1
                continue
            if seg[a_ix:b_ix].max() > max_stap_km:
                n_verworpen_stap += 1      # ongeobserveerde koorde — zie valkuil 1
                continue
            e_tix.append(i)
            e_set.append(int(cache["set"][i]))
            e_regel.append(int(cache["regel"][i]))
            e_i0.append(a_ix)
            e_i1.append(b_ix)
            e_a.append(ka)
            e_b.append(kb)
            e_km.append(max(float(cum[b_ix] - cum[a_ix]), 1e-6))
            e_op.append(int(cache["op"][i]))

    graaf = {
        "knoop_lat": knoop_lat, "knoop_lon": knoop_lon,
        "edge_tix": np.array(e_tix, dtype=np.int64),
        "edge_set": np.array(e_set, dtype=np.int16),
        "edge_regel": np.array(e_regel, dtype=np.int64),
        "edge_i0": np.array(e_i0, dtype=np.int32),
        "edge_i1": np.array(e_i1, dtype=np.int32),
        "edge_a": np.array(e_a, dtype=np.int64),
        "edge_b": np.array(e_b, dtype=np.int64),
        "edge_km": np.array(e_km, dtype=np.float64),
        "edge_op": np.array(e_op, dtype=np.uint8),
        "cel_graden": CEL_GRADEN, "cel_km": CEL_KM,
        "min_seg_km": min_seg_km, "max_stap_km": max_stap_km,
        "tracksets": cache["tracksets"], "bbox": cache["bbox"],
        "verworpen_stap": n_verworpen_stap, "verworpen_zelf": n_verworpen_zelf,
        "bouwtijd_s": time.monotonic() - t0,
    }
    if not stil:
        print(f"\ngraaf: {len(knoop_lat):,} knopen · {len(e_km):,} edges · "
              f"{sum(e_km):,.0f} edge-km · {graaf['bouwtijd_s']:.0f}s")
        print(f"  verworpen: {n_verworpen_stap:,} edges met een stap > "
              f"{max_stap_km} km (ongeobserveerde koorde) · "
              f"{n_verworpen_zelf:,} zelf-lussen")
    return graaf


def bewaar_graaf(pad: Path, graaf, metrics):
    pad.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        str(pad) + ".npz",
        knoop_lat=graaf["knoop_lat"], knoop_lon=graaf["knoop_lon"],
        edge_tix=graaf["edge_tix"],
        edge_set=graaf["edge_set"], edge_regel=graaf["edge_regel"],
        edge_i0=graaf["edge_i0"], edge_i1=graaf["edge_i1"],
        edge_a=graaf["edge_a"], edge_b=graaf["edge_b"],
        edge_km=graaf["edge_km"], edge_op=graaf["edge_op"])
    manifest = {
        "versie": 1, "type": "trackgraaf",
        "gemaakt": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "bron": "echte AIS-scheepstracks (bouw_tracks.py); GEEN bundeling, "
                "GEEN centerline, GEEN celcentra — edge = verwijzing in een track",
        "cel_graden": graaf["cel_graden"], "cel_km": graaf["cel_km"],
        "min_seg_km": graaf["min_seg_km"], "max_stap_km": graaf["max_stap_km"],
        "bbox_zwno": graaf["bbox"],
        "tracksets": graaf["tracksets"],
        "knopen": int(len(graaf["knoop_lat"])),
        "edges": int(len(graaf["edge_km"])),
        "edge_km_totaal": float(graaf["edge_km"].sum()),
        "arrays": {
            "knoop_lat/knoop_lon": "f8 — ECHT trackpunt in de cel, geen celcentrum",
            "edge_tix": "index in de track-cache <uit>-tracks.npz "
                        "(gemak; volgt uit edge_set+edge_regel)",
            "edge_set": "index in tracksets",
            "edge_regel": "0-gebaseerd regelnummer in dat .jsonl.gz "
                          "(track-id = <stam>#<regel>)",
            "edge_i0/edge_i1": "begin- en eindindex in track['punten'] — "
                               "de geometrie is die punten, niets anders",
            "edge_a/edge_b": "knoop-ids (index in knoop_lat/knoop_lon)",
            "edge_km": "f8 — echte lengte langs de puntenreeks",
            "edge_op": "u1 — 1 = opvaart, 0 = afvaart (baan-label; de "
                       "knoop-ruimte is GEDEELD, zie valkuil 2 in de kop)",
        },
        "bakken": "fase 3: stream de trackset één keer, en resolve per regel de "
                  "edges die ernaar verwijzen (punten[i0:i1+1]). Geen enkele "
                  "geometrie staat in dit bestand — dat is het punt.",
        "metrics": metrics,
    }
    Path(str(pad) + ".json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"geschreven: {pad}.npz "
          f"({Path(str(pad)+'.npz').stat().st_size/1e6:.1f} MB) + {pad}.json")


def laad_graaf(pad: Path):
    d = np.load(str(pad) + ".npz")
    graaf = {k: d[k] for k in d.files}
    m = json.loads(Path(str(pad) + ".json").read_text(encoding="utf-8"))
    graaf.update({"cel_graden": m["cel_graden"], "cel_km": m["cel_km"],
                  "min_seg_km": m["min_seg_km"], "max_stap_km": m["max_stap_km"],
                  "tracksets": m["tracksets"], "bbox": m["bbox_zwno"]})
    return graaf


# ── routeren over de graaf: HALTES ─────────────────────────────────────────
# ⚠️ Waarom dit niet gewoon een Dijkstra over knoop-cellen is — gemeten, niet
# bedacht. Een knoop is een CEL van ~200 m; twee tracks die die cel raken liggen
# er tot ~280 m van elkaar in. Met de knoop-cel als routeer-knoop is overstappen
# GRATIS en telt niemand die naad mee: eerste meting New Orleans -> Vidalia gaf
# 583 edges, **560 track-wissels**, som van de edge-km 346,7 maar de werkelijk
# getekende lijn 425,3 km — **78,6 km aan naden = 18% onverantwoord**, en een
# schijnbare -19,6% lengtefout. Precies de verkorting waar de kop voor waarschuwt.
#
# De gerichte fix: klap elke knoop-cel bij het ROUTEREN open in HALTES — één per
# knip-punt van één track. Doorvaren op dezelfde track is dan gratis (dezelfde
# halte, hetzelfde punt), en overstappen kost de ÉCHTE meters die je moet
# oversteken. Per knoop-cel één representant-halte (een echt trackpunt: de halte
# die het dichtst bij het midden van de cel-haltes ligt); overstappen loopt via
# die representant, dus de kosten zijn O(haltes) i.p.v. O(haltes**2).
# Gevolg: de dijkstra-afstand IS de lengte van de getekende lijn, punt voor punt,
# en elk punt blijft een echt trackpunt. De OPSLAG verandert niet — die blijft
# (track-id, i0, i1) + knoop-ids, precies zoals gespecificeerd; haltes zijn een
# routeer-constructie die uit de graaf volgt.

HALTE_SCH = 1 << 17          # max punten per track in de halte-sleutel


def bouw_router(graaf, cache, alleen_op=None, verboden_knopen=None,
                overstap_boete=0.0, stil=True):
    from scipy.sparse import csr_matrix
    t0 = time.monotonic()
    tix = graaf["edge_tix"].astype(np.int64)
    key_a = tix * HALTE_SCH + graaf["edge_i0"].astype(np.int64)
    key_b = tix * HALTE_SCH + graaf["edge_i1"].astype(np.int64)
    haltes = np.unique(np.concatenate([key_a, key_b]))
    ha = np.searchsorted(haltes, key_a)
    hb = np.searchsorted(haltes, key_b)
    n_h = len(haltes)
    h_knoop = np.zeros(n_h, dtype=np.int64)
    h_knoop[ha] = graaf["edge_a"]
    h_knoop[hb] = graaf["edge_b"]
    h_tix = haltes // HALTE_SCH
    h_idx = haltes % HALTE_SCH
    pos = cache["start"][h_tix] + h_idx
    h_lat = cache["lat"][pos]
    h_lon = cache["lon"][pos]

    houd = np.ones(len(graaf["edge_km"]), dtype=bool)
    if alleen_op is not None:
        houd &= graaf["edge_op"] == (1 if alleen_op else 0)
    vb_h = np.zeros(n_h, dtype=bool)
    if verboden_knopen:
        vbk = np.zeros(int(h_knoop.max()) + 2, dtype=bool)
        vbk[list(verboden_knopen)] = True
        vb_h = vbk[h_knoop]
        houd &= ~(vb_h[ha] | vb_h[hb])

    a_from, a_to = ha[houd], hb[houd]
    a_w = graaf["edge_km"][houd]
    a_eid = np.flatnonzero(houd).astype(np.int64)

    # overstap-spaken per knoop-cel
    orde = np.argsort(h_knoop, kind="stable")
    kn_s = h_knoop[orde]
    grens = np.flatnonzero(np.r_[True, kn_s[1:] != kn_s[:-1]])
    grenzen = np.r_[grens, len(kn_s)]
    s_from, s_to, s_w = [], [], []
    for gi in range(len(grens)):
        leden = orde[grenzen[gi]:grenzen[gi + 1]]
        if verboden_knopen:
            leden = leden[~vb_h[leden]]
        if len(leden) < 2:
            continue
        la, lo = h_lat[leden], h_lon[leden]
        d = km_np(la, lo, la.mean(), lo.mean())
        r = leden[int(np.argmin(d))]
        rest = leden[leden != r]
        s_from.append(rest)
        s_to.append(np.full(len(rest), r, dtype=np.int64))
        s_w.append(km_np(h_lat[rest], h_lon[rest], h_lat[r], h_lon[r])
                   + overstap_boete)
    if s_from:
        sf = np.concatenate(s_from)
        st = np.concatenate(s_to)
        sw = np.concatenate(s_w)
    else:
        sf = st = np.zeros(0, np.int64)
        sw = np.zeros(0)

    # alle bogen, beide richtingen (een baan is een label, niet een verbod)
    b_from = np.concatenate([a_from, a_to, sf, st])
    b_to = np.concatenate([a_to, a_from, st, sf])
    b_w = np.concatenate([a_w, a_w, sw, sw])
    b_eid = np.concatenate([a_eid, a_eid,
                            np.full(len(sf), -1, np.int64),
                            np.full(len(st), -1, np.int64)])
    # dubbele (van,naar) samenvouwen op de KORTSTE — meer dan één kortste boog
    # tussen twee haltes bestaat niet; alle edges blijven in de graaf staan.
    sleutel = b_from * np.int64(n_h) + b_to
    ordr = np.lexsort((b_w, sleutel))
    sleutel, b_from, b_to, b_w, b_eid = (sleutel[ordr], b_from[ordr],
                                         b_to[ordr], b_w[ordr], b_eid[ordr])
    eerste = np.r_[True, sleutel[1:] != sleutel[:-1]]
    sleutel, b_from, b_to = sleutel[eerste], b_from[eerste], b_to[eerste]
    b_w, b_eid = b_w[eerste], b_eid[eerste]
    M = csr_matrix((np.maximum(b_w, 1e-9), (b_from, b_to)), shape=(n_h, n_h))
    router = {"M": M, "haltes": haltes, "h_knoop": h_knoop, "h_lat": h_lat,
              "h_lon": h_lon, "h_tix": h_tix, "h_idx": h_idx,
              "boog_sleutel": sleutel, "boog_eid": b_eid, "boog_w": b_w,
              "n_h": n_h, "n_overstap": int(len(sf)),
              "boete": float(overstap_boete)}
    if not stil:
        print(f"  router: {n_h:,} haltes · {len(b_from):,} bogen "
              f"({len(sf):,} overstap-spaken) · {time.monotonic()-t0:.0f}s")
    return router


def boog_eid(router, u, v):
    s = u * router["n_h"] + v
    j = int(np.searchsorted(router["boog_sleutel"], s))
    if j >= len(router["boog_sleutel"]) or router["boog_sleutel"][j] != s:
        return None, float("nan")
    return int(router["boog_eid"][j]), float(router["boog_w"][j])


def snap_halte(router, lat, lon):
    d = km_np(router["h_lat"], router["h_lon"], lat, lon)
    j = int(np.argmin(d))
    return j, float(d[j]), int(router["h_knoop"][j])


def halte_van_knoop(router, knoop_id):
    """De best verbonden halte VAN een knoop-id, exact.

    ⚠️ Niet vervangen door snap_halte op de knoop-coördinaat. Die coördinaat is
    het eerste trackpunt in de cel en hoeft zelf helemaal geen halte te zijn
    (haltes liggen op knip-punten), dus de dichtstbijzijnde halte kan bij een
    BUURCEL horen — en dan zoekt de eiland-toets vanaf de verkeerde knoop of
    breekt hij af met 'uiteinde-knoop verdween'. Gemeten: bij probes vlak bij de
    junctie (snap 0,010 en 0,392 km) gebeurde precies dat."""
    ix = np.flatnonzero(router["h_knoop"] == knoop_id)
    if not len(ix):
        return None
    graad = np.diff(router["M"].indptr)[ix]
    return int(ix[int(np.argmax(graad))])


def snap_trackpunt(cache, lat, lon):
    """Wat het BESTE is dat de data kan: de dichtstbijzijnde echte ping."""
    d = km_np(cache["lat"], cache["lon"], lat, lon)
    j = int(np.argmin(d))
    return float(d[j])


def zoek_route(router, h_start, h_doel):
    from scipy.sparse.csgraph import dijkstra
    d, pred = dijkstra(router["M"], directed=True, indices=h_start,
                       return_predecessors=True)
    if not np.isfinite(d[h_doel]):
        return None, float("inf")
    pad = [int(h_doel)]
    while pad[-1] != h_start:
        p = int(pred[pad[-1]])
        if p < 0:
            return None, float("inf")
        pad.append(p)
    pad.reverse()
    return pad, float(d[h_doel])


def route_geometrie(graaf, cache, router, halte_pad):
    """Punten + herkomst + lengte. De lengte is de lengte van de GETEKENDE lijn
    (inclusief de overstap-naden).

    ⚠️ Invariant, en let op de exacte vorm: getekende lijn == dijkstra-afstand
    MINUS n_overstap * overstap-boete. De boete is namelijk geen geometrie maar
    een routeer-voorkeur, dus hij zit wél in het dijkstra-gewicht en NIET in de
    lijn. Wie de twee kaal vergelijkt krijgt een 'verschil' dat exact het aantal
    overstappen maal de boete is (gemeten: 471,344 - 421,344 = 5 x 10 km) en
    denkt ten onrechte dat er km zoekraken. Na aftrek hoort het verschil 0 te
    zijn — en dán toetst deze controle wat hij moet toetsen: dat er geen naad
    onverantwoord blijft."""
    punten, herkomst, edges = [], [], []
    n_overstap = 0
    overstap_km = 0.0
    for u, v in zip(halte_pad[:-1], halte_pad[1:]):
        eid, w = boog_eid(router, u, v)
        if eid is None:
            raise RuntimeError(f"boog {u}->{v} niet gevonden")
        if eid < 0:                       # overstap-spaak: één echt punt erbij
            n_overstap += 1
            tix, idx = int(router["h_tix"][v]), int(router["h_idx"][v])
            s0 = int(cache["start"][tix])
            vorig = punten[-1] if punten else None
            _voeg_toe(punten, herkomst, cache, tix, s0, idx)
            if vorig and punten[-1] != vorig:
                # ECHTE naad-afstand, niet het boog-gewicht (dat de boete bevat)
                overstap_km += km(vorig[0], vorig[1], punten[-1][0], punten[-1][1])
            continue
        edges.append(eid)
        tix = int(graaf["edge_tix"][eid])
        i0, i1 = int(graaf["edge_i0"][eid]), int(graaf["edge_i1"][eid])
        s0 = int(cache["start"][tix])
        vooruit = int(router["h_idx"][u]) == i0
        rng = range(i0, i1 + 1) if vooruit else range(i1, i0 - 1, -1)
        for k in rng:
            _voeg_toe(punten, herkomst, cache, tix, s0, k)
    la = np.array([p[0] for p in punten])
    lo = np.array([p[1] for p in punten])
    seg = seg_km_np(la, lo) if len(la) > 1 else np.zeros(1)
    return {"punten": punten, "herkomst": herkomst, "edges": edges,
            "km": float(seg.sum()), "n_overstap": n_overstap,
            "overstap_km": overstap_km, "max_stap_km": float(seg.max()),
            "n_tracks": len({(h[0], h[1]) for h in herkomst})}


def _voeg_toe(punten, herkomst, cache, tix, s0, k):
    p = (float(cache["lat"][s0 + k]), float(cache["lon"][s0 + k]))
    if punten and punten[-1] == p:
        return
    punten.append(p)
    herkomst.append((int(cache["set"][tix]), int(cache["regel"][tix]), k))


def bewijs_route(graaf, punten, herkomst):
    """HARD BEWIJS: lees de brontrackset terug en vergelijk punt voor punt.
    'identiek' betekent hier letterlijk gelijk, niet 'dichtbij'."""
    nodig = {}
    for idx, (s, r, k) in enumerate(herkomst):
        nodig.setdefault(s, {}).setdefault(r, []).append((k, idx))
    identiek = anders = 0
    voorbeeld = []
    for s, regels in nodig.items():
        pad = Path(graaf["tracksets"][s]["pad"])
        with gzip.open(pad, "rt", encoding="utf-8") as fh:
            for nr, regel in enumerate(fh):
                if nr not in regels:
                    continue
                pts = json.loads(regel)["punten"]
                for k, idx in regels[nr]:
                    bron = (pts[k][0], pts[k][1])
                    if bron == punten[idx]:
                        identiek += 1
                        if len(voorbeeld) < 3:
                            voorbeeld.append(
                                (f"{graaf['tracksets'][s]['stam']}#{nr}[{k}]",
                                 bron, punten[idx]))
                    else:
                        anders += 1
                        if len(voorbeeld) < 8:
                            voorbeeld.append(
                                ("AFWIJKEND "
                                 f"{graaf['tracksets'][s]['stam']}#{nr}[{k}]",
                                 bron, punten[idx]))
    return identiek, anders, voorbeeld


# ── integriteits-metrics (elke run) ────────────────────────────────────────

def metrics(graaf, cache, router, punten_namen, laag1_paren=None, stil=False):
    from scipy.sparse.csgraph import connected_components
    n_comp, label = connected_components(router["M"], directed=False)
    maten = np.bincount(label)
    hoofd = int(np.argmax(maten))
    e_label = label[np.searchsorted(
        router["haltes"],
        graaf["edge_tix"].astype(np.int64) * HALTE_SCH
        + graaf["edge_i0"].astype(np.int64))]
    km_per_comp = np.bincount(e_label, weights=graaf["edge_km"],
                              minlength=n_comp)
    graad = np.bincount(router["h_knoop"], minlength=len(graaf["knoop_lat"]))

    snaps, bereik, snaps_ping = {}, {}, {}
    for naam in punten_namen:
        lat, lon, _, _ = parse_punt(naam)
        j, d, kn = snap_halte(router, lat, lon)
        snaps[naam] = d
        snaps_ping[naam] = snap_trackpunt(cache, lat, lon)
        bereik[naam] = bool(label[j] == hoofd)

    m = {
        "knopen": int(len(graaf["knoop_lat"])),
        "edges": int(len(graaf["edge_km"])),
        "haltes": int(router["n_h"]),
        "overstap_spaken": int(router["n_overstap"]),
        "edge_km": float(graaf["edge_km"].sum()),
        "componenten": int(n_comp),
        "hoofdcomponent_haltes": int(maten[hoofd]),
        "hoofdcomponent_aandeel": float(maten[hoofd] / len(label)),
        "hoofdcomponent_km": float(km_per_comp[hoofd]),
        "knoop_bezetting": {"1": int((graad == 1).sum()),
                            "2": int((graad == 2).sum()),
                            "3+": int((graad >= 3).sum())},
        "op_edges": int((graaf["edge_op"] == 1).sum()),
        "af_edges": int((graaf["edge_op"] == 0).sum()),
        "snap_km_naar_graaf": {k: round(v, 3) for k, v in snaps.items()},
        "snap_km_naar_ping": {k: round(v, 3) for k, v in snaps_ping.items()},
        "in_hoofdcomponent": bereik,
    }
    if snaps:
        v = list(snaps.values())
        m["snap_verdeling_km"] = {"min": round(min(v), 3),
                                  "mediaan": round(pct(v, 50), 3),
                                  "max": round(max(v), 3)}
    if laag1_paren is not None:
        m["laag1_opgelost"] = laag1_paren
    if not stil:
        print("\n── INTEGRITEITS-METRICS ──")
        print(f"  knopen / edges     : {m['knopen']:,} / {m['edges']:,} "
              f"({m['edge_km']:,.0f} edge-km · op {m['op_edges']:,} / "
              f"af {m['af_edges']:,})")
        print(f"  haltes / overstap  : {m['haltes']:,} / "
              f"{m['overstap_spaken']:,} spaken")
        print(f"  losse componenten  : {m['componenten']:,}  "
              f"(hoofdcomponent {m['hoofdcomponent_haltes']:,} haltes = "
              f"{m['hoofdcomponent_aandeel']*100:.1f}% · "
              f"{m['hoofdcomponent_km']:,.0f} km)")
        print(f"  knoop-bezetting    : 1 halte={m['knoop_bezetting']['1']:,} · "
              f"2={m['knoop_bezetting']['2']:,} · "
              f"3+={m['knoop_bezetting']['3+']:,}")
        for naam in punten_namen:
            print(f"  {naam:<12}: snap {snaps[naam]:.3f} km naar de graaf "
                  f"({snaps_ping[naam]:.3f} km naar de dichtstbijzijnde ping) · "
                  f"{'IN hoofdcomponent' if bereik[naam] else 'LOS van hoofdcomponent'}")
        if laag1_paren is not None:
            print(f"  laag 1 lost op     : {laag1_paren['opgelost']} van "
                  f"{laag1_paren['paren']} paren "
                  f"(snap {laag1_paren['snap_km']} km)")
    return m, label, hoofd


# ── subcommando's ──────────────────────────────────────────────────────────

def cmd_laag1(args):
    namen_in = list(args.punten or [])
    if args.van and args.van not in namen_in:
        namen_in.insert(0, args.van)
    if args.naar and args.naar not in namen_in:
        namen_in.insert(1, args.naar)
    doelen = [parse_punt(n) for n in namen_in]
    namen = [d[2] for d in doelen]
    print(f"laag 1 over {len(args.tracks)} trackset(s) · doelpunten: "
          + ", ".join(f"{d[2]} ({d[0]},{d[1]})" for d in doelen))
    _, dm = lees_tracksets(args.tracks, bbox=None, doelen=doelen,
                           kand_km=args.kand_km, max_regels=args.max_regels)
    print(f"\ntracks binnen {args.kand_km} km van minstens één doelpunt: {len(dm):,}")
    for k, naam in enumerate(namen):
        n = sum(1 for r in dm.values() if r["dmin"][k] <= args.kand_km)
        n_snap = sum(1 for r in dm.values() if r["dmin"][k] <= args.snap)
        print(f"  {naam:<12}: {n:,} tracks binnen {args.kand_km} km · "
              f"{n_snap:,} binnen {args.snap} km")
    opgelost = paren = 0
    for i in range(len(namen)):
        for j in range(len(namen)):
            if i == j:
                continue
            paren += 1
            kand = laag1_kandidaten(dm, i, j, args.snap)
            if kand:
                opgelost += 1
            if (i, j) == (0, 1) or args.alle_paren:
                rapport_laag1(kand, namen[i], namen[j], args.snap, args.kies)
    print(f"\nlaag 1 lost {opgelost} van de {paren} geordende paren volledig op "
          f"(snap {args.snap} km)")


def cmd_graaf(args):
    doelen = [parse_punt(n) for n in args.punten] if args.punten else []
    bbox = tuple(float(x) for x in args.bbox.split(",")) if args.bbox else None
    print(f"graaf bouwen · bbox {bbox} · cel {CEL_KM*1000:.0f} m · "
          f"min-seg {args.min_seg_km} km · max-stap {args.max_stap_km} km")
    cache, dm = lees_tracksets(args.tracks, bbox=bbox, doelen=doelen,
                               kand_km=args.kand_km, max_regels=args.max_regels)
    uit = Path(args.uit)
    uit.parent.mkdir(parents=True, exist_ok=True)
    bewaar_cache(Path(str(uit) + "-tracks"), cache)
    graaf = bouw_graaf(cache, args.min_seg_km, args.max_stap_km)
    router = bouw_router(graaf, cache, alleen_op=_richting(args),
                         overstap_boete=args.overstap_boete, stil=False)
    l1 = None
    if len(doelen) >= 2:
        opgelost = paren = 0
        for i in range(len(doelen)):
            for j in range(len(doelen)):
                if i == j:
                    continue
                paren += 1
                if laag1_kandidaten(dm, i, j, args.snap):
                    opgelost += 1
        l1 = {"paren": paren, "opgelost": opgelost, "snap_km": args.snap}
    m, _, _ = metrics(graaf, cache, router, [d[2] for d in doelen], l1)
    bewaar_graaf(uit, graaf, m)


def _richting(args):
    r = getattr(args, "richting", "beide")
    return None if r == "beide" else (r == "op")


def _laad(args):
    pad = Path(args.graaf)
    graaf = laad_graaf(pad)
    cache = laad_cache(Path(str(pad) + "-tracks"))
    return graaf, cache


def _laag2(graaf, cache, router, lat_a, lon_a, lat_b, lon_b):
    ha, da, ka = snap_halte(router, lat_a, lon_a)
    hb, db, kb = snap_halte(router, lat_b, lon_b)
    pad, d = zoek_route(router, ha, hb)
    if pad is None:
        return None, (da, db, ka, kb), d
    r = route_geometrie(graaf, cache, router, pad)
    r["dijkstra_km"] = d
    r["halte_pad"] = pad
    r["knoop_pad"] = [int(router["h_knoop"][h]) for h in pad]
    return r, (da, db, ka, kb), d


def cmd_route(args):
    graaf, cache = _laad(args)
    router = bouw_router(graaf, cache, alleen_op=_richting(args),
                         overstap_boete=args.overstap_boete, stil=False)
    lat_a, lon_a, na, _ = parse_punt(args.van)
    lat_b, lon_b, nb, _ = parse_punt(args.naar)
    r, (da, db, ka, kb), d = _laag2(graaf, cache, router,
                                    lat_a, lon_a, lat_b, lon_b)
    print(f"snap {na}: knoop {ka} op {da:.3f} km · {nb}: knoop {kb} op {db:.3f} km")
    if r is None:
        print("GEEN PAD")
    else:
        print(f"route: {len(r['edges'])} edges uit {r['n_tracks']} tracks · "
              f"{len(r['punten'])} punten · {r['km']:.1f} km "
              f"(dijkstra {d:.1f} incl. {r['n_overstap']}x"
              f"{router['boete']:.0f} km boete) · {r['n_overstap']} "
              f"overstappen = {r['overstap_km']:.2f} km naad")
    metrics(graaf, cache, router, [na, nb])


def cmd_toets(args):
    """De acceptatietoets: laag 1 en laag 2 op dezelfde route + hard bewijs."""
    graaf, cache = _laad(args)
    lat_a, lon_a, na, bron_a = parse_punt(args.van)
    lat_b, lon_b, nb, bron_b = parse_punt(args.naar)
    print(f"═══ TOETS {na} -> {nb} ═══")
    print(f"  A {na}: {lat_a}, {lon_a}   [{bron_a}]")
    print(f"  B {nb}: {lat_b}, {lon_b}   [{bron_b}]")

    # ── laag 1, over de VOLLEDIGE tracksets (niet de bbox: een hele-track-match
    #    mag onderweg overal komen) ──
    keus = None
    if not args.geen_laag1:
        doelen = [(lat_a, lon_a, na, bron_a), (lat_b, lon_b, nb, bron_b)]
        paden = args.tracks or [t["pad"] for t in graaf["tracksets"]]
        _, dm = lees_tracksets(paden, bbox=None, doelen=doelen,
                               kand_km=args.kand_km, max_regels=args.max_regels)
        for k, naam in enumerate((na, nb)):
            n3 = sum(1 for r_ in dm.values() if r_["dmin"][k] <= args.kand_km)
            ns = sum(1 for r_ in dm.values() if r_["dmin"][k] <= args.snap)
            print(f"  {naam:<12}: {n3:,} tracks binnen {args.kand_km} km · "
                  f"{ns:,} binnen {args.snap} km")
        kand = laag1_kandidaten(dm, 0, 1, args.snap)
        keus = rapport_laag1(kand, na, nb, args.snap, args.kies)
        for w in ("kort", "snap"):
            alt = kies_route(kand, w)
            if alt:
                print(f"    (bij --kies {w}: {alt['km']:.1f} km, "
                      f"snap {alt['snap_a']:.3f}/{alt['snap_b']:.3f})")
        if args.alle and kand:
            print("  alle kandidaten (track-id · km · snapA · snapB):")
            for k_ in kand:
                stam = graaf["tracksets"][k_["set"]]["stam"]
                print(f"    {stam}#{k_['regel']:<7} mmsi {k_['mmsi']} · "
                      f"{k_['km']:7.1f} km · {k_['snap_a']:.3f} · {k_['snap_b']:.3f}")

    # ── laag 2 ──
    print("\n── LAAG 2 · de graaf ──")
    router = bouw_router(graaf, cache, alleen_op=_richting(args),
                         overstap_boete=args.overstap_boete, stil=False)
    r, (da, db, ka, kb), d = _laag2(graaf, cache, router,
                                    lat_a, lon_a, lat_b, lon_b)
    print(f"  snap A: knoop {ka} op {da:.3f} km · snap B: knoop {kb} op "
          f"{db:.3f} km  (eis <= {args.snap} km: "
          f"{'GEHAALD' if max(da, db) <= args.snap else 'GEFAALD'})")
    if r is None:
        print("  GEEN PAD over de graaf")
    else:
        n_op = sum(1 for e in r["edges"] if graaf["edge_op"][e] == 1)
        print(f"  route : {len(r['edges'])} edges uit {r['n_tracks']} "
              f"verschillende tracks · {len(r['punten'])} punten · "
              f"{r['km']:.1f} km")
        print(f"  banen : {n_op} op-edges · {len(r['edges'])-n_op} af-edges")
        print(f"  overstappen: {r['n_overstap']} · {r['overstap_km']:.2f} km "
              f"({r['overstap_km']/max(r['km'],1e-9)*100:.2f}% van de route) · "
              f"grootste stap in de lijn {r['max_stap_km']:.3f} km")
        d_geo = d - r["n_overstap"] * router["boete"]
        print(f"  controle: dijkstra {d:.3f} km − {r['n_overstap']}x"
              f"{router['boete']:.0f} km boete = {d_geo:.3f} km == getekende "
              f"lijn {r['km']:.3f} km  (verschil {abs(d_geo-r['km']):.6f} km "
              f"— hoort 0 te zijn: geen onverantwoorde naad)")
        if graaf["bbox"]:
            z, w_, n_, o = graaf["bbox"]
            la = np.array([p[0] for p in r["punten"]])
            lo = np.array([p[1] for p in r["punten"]])
            rand = min(np.abs(la - z).min(), np.abs(la - n_).min(),
                       np.abs(lo - w_).min(), np.abs(lo - o).min()) * 111.32
            print(f"  bbox-rand: route komt tot {rand:.1f} km van de bbox-rand "
                  f"({'ruim' if rand > 5 else 'LET OP — mogelijk afgekapt'})")
        ident, anders, vb = bewijs_route(graaf, r["punten"], r["herkomst"])
        print("\n  GEOMETRIE-BEWIJS (teruggelezen uit de brontrackset):")
        print(f"    {ident:,} van {len(r['punten']):,} routepunten IDENTIEK aan "
              f"het brontrackpunt · {anders} afwijkend")
        for naam, bronp, routep in vb[:3]:
            print(f"      {naam}: bron {bronp} == route {routep}")

    # ── vergelijking + verdict ──
    print("\n── VERGELIJKING ──")
    if keus:
        print(f"  laag 1: {keus['km']:.1f} km  (één echte track: "
              f"{graaf['tracksets'][keus['set']]['stam']}#{keus['regel']}, "
              f"mmsi {keus['mmsi']})")
    if r is not None:
        print(f"  laag 2: {r['km']:.1f} km")
    if keus and r is not None:
        afw = (r["km"] - keus["km"]) / keus["km"] * 100
        print(f"  verschil laag2 - laag1: {afw:+.2f}%")
    if args.verwacht_km:
        for naam, v in (("laag 1", keus["km"] if keus else None),
                        ("laag 2", r["km"] if r is not None else None)):
            if v is None or not np.isfinite(v):
                print(f"  {naam} tegen referentie: geen route")
                continue
            afw = (v - args.verwacht_km) / args.verwacht_km * 100
            print(f"  {naam} tegen referentie {args.verwacht_km} km: "
                  f"{v:.1f} km = {afw:+.2f}%  "
                  f"{'BINNEN' if abs(afw) <= 2 else 'BUITEN'} ±2%")
    metrics(graaf, cache, router, [na, nb])


def cmd_eiland(args):
    """Beide geulen om een eiland bereikbaar? Foutmodus (a) = één arm weg;
    (b) = twee losse parallelle netwerken die nergens samenkomen."""
    graaf, cache = _laad(args)
    if args.zoek:
        zoek_eilanden(graaf, args)
        return
    router = bouw_router(graaf, cache, alleen_op=_richting(args),
                         overstap_boete=args.overstap_boete, stil=False)
    lat_a, lon_a, na, _ = parse_punt(args.van)
    lat_b, lon_b, nb, _ = parse_punt(args.naar)
    ha, da, ka = snap_halte(router, lat_a, lon_a)
    hb, db, kb = snap_halte(router, lat_b, lon_b)
    print(f"═══ EILAND-TOETS ═══")
    print(f"  probe beneden {na} -> knoop {ka} ({da:.3f} km) · "
          f"probe boven {nb} -> knoop {kb} ({db:.3f} km)")
    pad1, d1 = zoek_route(router, ha, hb)
    if pad1 is None:
        print("  GEEN PAD — geen van de geulen bereikbaar")
        return
    r1 = route_geometrie(graaf, cache, router, pad1)
    kn1 = [int(router["h_knoop"][h]) for h in pad1]
    print(f"  geul 1: {len(r1['edges'])} edges uit {r1['n_tracks']} tracks · "
          f"{r1['km']:.2f} km · {len(set(kn1))} knopen")
    # tweede geul: alle KNOPEN van geul 1 behalve de twee uiteinden verboden
    verboden = set(kn1[1:-1]) - {ka, kb}
    router2 = bouw_router(graaf, cache, verboden_knopen=verboden,
                          alleen_op=_richting(args),
                          overstap_boete=args.overstap_boete, stil=True)
    ha2 = halte_van_knoop(router2, ka)
    hb2 = halte_van_knoop(router2, kb)
    if ha2 is None or hb2 is None:
        print("  (uiteinde-knoop bestaat niet in de tweede graaf — afgebroken)")
        return
    if args.via:
        # ⚠️ Waarom --via bestaat, gemeten op Profit Island. Zonder via zoekt de
        # toets het KORTSTE knoop-disjuncte pad, en op een drukke rivier is dat
        # bijna nooit de andere arm: het is een parallelle doorvaart in dezelfde
        # geul, 160 m ernaast (gemeten: 12,78 km, max scheiding 0,308 km, 0 km
        # echt los). Dat is een geldig tweede pad maar het antwoordt niet op
        # Lars' vraag. Met --via in de andere arm dwing je de toets die arm in en
        # bewijs je wat er bewezen moet worden: dat er langs BEIDE geulen sporen
        # lopen en dat ze boven en onder dezelfde knoop delen.
        lat_v, lon_v, nv, _ = parse_punt(args.via)
        hv, dv, kv = snap_halte(router2, lat_v, lon_v)
        print(f"  via {nv} -> knoop {kv} ({dv:.3f} km)")
        pad_a, d_a = zoek_route(router2, ha2, hv)
        pad_b, d_b = zoek_route(router2, hv, hb2)
        if pad_a is None or pad_b is None:
            print(f"  GEEN PAD via {nv} — die arm hangt niet aan beide juncties.")
            return
        pad2, d2 = pad_a + pad_b[1:], d_a + d_b
    else:
        pad2, d2 = zoek_route(router2, ha2, hb2)
    if pad2 is None:
        print("  GEEN TWEEDE, KNOOP-DISJUNCTE GEUL — foutmodus (a): één arm.")
        return
    r2 = route_geometrie(graaf, cache, router2, pad2)
    kn2 = [int(router2["h_knoop"][h]) for h in pad2]
    print(f"  geul 2: {len(r2['edges'])} edges uit {r2['n_tracks']} tracks · "
          f"{r2['km']:.2f} km · {len(set(kn2))} knopen")
    la1 = np.array([p[0] for p in r1["punten"]])
    lo1 = np.array([p[1] for p in r1["punten"]])
    la2 = np.array([p[0] for p in r2["punten"]])
    lo2 = np.array([p[1] for p in r2["punten"]])

    def los_km(laA, loA, laB, loB):
        """Hoeveel km van baan A loopt verder dan min_sep van baan B?

        ⚠️ Dit is de eigenlijke toets, en 'max scheiding' is dat NIET. Op een
        drukke rivier liggen honderden doorvaarten in dezelfde geul, dus een
        tweede KNOOP-DISJUNCT pad is triviaal te vinden: pak een andere track in
        hetzelfde water. Zo'n pad haalt een max-scheiding-drempel al door ergens
        even uit te wijken. Wat een eiland onderscheidt is dat er een aaneen-
        gesloten LENGTE bestaat waarover de twee banen niet samenvallen — en
        die lengte is hier de maat."""
        sep = np.array([km_np(laB, loB, laA[i], loA[i]).min()
                        for i in range(len(laA))])
        seg = seg_km_np(laA, loA) if len(laA) > 1 else np.zeros(0)
        ver = (sep[:-1] > args.min_sep) & (sep[1:] > args.min_sep)
        return sep, float(seg[ver].sum())

    sep2, los2 = los_km(la2, lo2, la1, lo1)
    sep1, los1 = los_km(la1, lo1, la2, lo2)
    print(f"  scheiding geul2 t.o.v. geul1: mediaan {np.median(sep2):.3f} km · "
          f"max {sep2.max():.3f} km")
    print(f"  ECHT LOS (> {args.min_sep} km uit elkaar): "
          f"{los2:.2f} km van geul 2 ({los2/max(r2['km'],1e-9)*100:.0f}%) · "
          f"{los1:.2f} km van geul 1 ({los1/max(r1['km'],1e-9)*100:.0f}%)")
    gedeeld = sorted(set(kn1) & set(kn2))
    print(f"  GEDEELDE KNOPEN: {len(gedeeld)}")
    print(f"    beneden-junctie  knoop {ka}: {graaf['knoop_lat'][ka]:.5f}, "
          f"{graaf['knoop_lon'][ka]:.5f}")
    print(f"    boven-junctie    knoop {kb}: {graaf['knoop_lat'][kb]:.5f}, "
          f"{graaf['knoop_lon'][kb]:.5f}")
    if gedeeld:
        print(f"    alle gedeelde knoop-ids: "
              f"{gedeeld if len(gedeeld) <= 20 else str(gedeeld[:20]) + ' …'}")
    # Eis is de LOSSE LENGTE (zie los_km), niet de max-scheiding, plus een
    # gedeelde knoop boven én onder — foutmodus (b) is twee parallelle
    # netwerken die nergens samenkomen, en die lijkt compleet tot je routeert.
    goed = (los2 >= args.min_lengte and ka in set(kn1) & set(kn2)
            and kb in set(kn1) & set(kn2))
    print(f"  {'GESLAAGD' if goed else 'TWIJFEL'}: twee knoop-disjuncte geulen "
          f"({r1['km']:.2f} en {r2['km']:.2f} km) waarvan {los2:.2f} km echt "
          f"los loopt (eis >= {args.min_lengte} km), maximale scheiding "
          f"{sep2.max():.2f} km, en ze delen boven én onder een knoop.")
    metrics(graaf, cache, router, [na, nb])


def zoek_eilanden(graaf, args):
    """Zoek data-gestuurd naar twee parallelle geulen: latitude-banden waar de
    knopen in >= 2 lon-clusters uiteenvallen die boven en onder weer samenkomen.
    Geen aangenomen geografie."""
    lat, lon = graaf["knoop_lat"], graaf["knoop_lon"]
    z, w, n_, o = (tuple(float(x) for x in args.bbox.split(","))
                   if args.bbox else (lat.min(), lon.min(), lat.max(), lon.max()))
    sel = (lat >= z) & (lat <= n_) & (lon >= w) & (lon <= o)
    print(f"eiland-scan in bbox {z},{w},{n_},{o}: {sel.sum():,} knopen")
    band = 0.01
    la_sel, lo_sel = lat[sel], lon[sel]
    iy = np.floor(la_sel / band).astype(np.int64)
    banden = {}
    for y in np.unique(iy):
        v = np.sort(lo_sel[iy == y])
        if len(v) < 4:
            continue
        km_per_graad = 111.32 * math.cos(math.radians(y * band))
        d = np.diff(v) * km_per_graad
        # ⚠️ Een bovengrens is GEEN kosmetiek. Zonder hem is de sterkste
        # "kandidaat" op de Mississippi-graaf een scheiding van 629 km: dat is
        # de Golf van Mexico tegenover de rivier in dezelfde latitude-band, en
        # verderop de meanders (de rivier kruist dezelfde band meermaals, tien
        # km uit elkaar). Een eiland is hooguit een paar km breed, dus alles
        # daarboven is per definitie geen tweede geul om hetzelfde eiland.
        gaten = np.flatnonzero((d > args.min_sep) & (d <= args.max_sep))
        if len(gaten):
            banden[int(y)] = float(d[gaten].max())
    ys = sorted(banden)
    reeksen, huidig = [], []
    for y in ys:
        if huidig and y == huidig[-1] + 1:
            huidig.append(y)
        else:
            if huidig:
                reeksen.append(huidig)
            huidig = [y]
    if huidig:
        reeksen.append(huidig)
    kandidaten = []
    for rs in reeksen:
        lengte = len(rs) * band * 111.32
        sep = max(banden[y] for y in rs)
        if lengte >= args.min_lengte:
            kandidaten.append((sep * lengte, lengte, sep, rs[0] * band,
                               (rs[-1] + 1) * band))
    kandidaten.sort(reverse=True)
    print(f"  {len(kandidaten)} kandidaten (>= {args.min_lengte} km lang, "
          f"scheiding >= {args.min_sep} km) — sterkste eerst:")
    for score, lengte, sep, y0, y1 in kandidaten[:12]:
        band_sel = (la_sel >= y0) & (la_sel <= y1)
        lonm = float(np.median(lo_sel[band_sel]))
        print(f"    lat {y0:.3f}..{y1:.3f} ({lengte:.1f} km) · scheiding "
              f"{sep:.2f} km · lon ≈ {lonm:.3f}   probes: "
              f"--van {y0-0.04:.3f},{lonm:.3f} --naar {y1+0.04:.3f},{lonm:.3f}")


def cmd_diagnose(args):
    """Eerlijke breuk-diagnose: hoe ver komt de graaf van elke kant, waar
    breekt hij, hoeveel componenten heeft de corridor?"""
    from scipy.sparse.csgraph import connected_components, dijkstra
    graaf, cache = _laad(args)
    router = bouw_router(graaf, cache, alleen_op=_richting(args),
                         overstap_boete=args.overstap_boete, stil=False)
    lat_a, lon_a, na, _ = parse_punt(args.van)
    lat_b, lon_b, nb, _ = parse_punt(args.naar)
    n_comp, label = connected_components(router["M"], directed=False)
    maten = np.bincount(label)
    ha, da, ka = snap_halte(router, lat_a, lon_a)
    hb, db, kb = snap_halte(router, lat_b, lon_b)
    print(f"═══ DIAGNOSE {na} -> {nb} ═══")
    print(f"  snap A: knoop {ka} ({da:.3f} km) · component {label[ha]} "
          f"({maten[label[ha]]:,} haltes)")
    print(f"  snap B: knoop {kb} ({db:.3f} km) · component {label[hb]} "
          f"({maten[label[hb]]:,} haltes)")
    if label[ha] == label[hb]:
        pad, d = zoek_route(router, ha, hb)
        print(f"  ZELFDE COMPONENT — er IS een pad: {d:.1f} km")
    else:
        print("  VERSCHILLENDE COMPONENTEN — geen pad. Dat is de breuk.")

    # ⚠️ Afstanden hier MOETEN boete-vrij zijn. "hoe ver komt hij" is een
    # geometrische vraag, en het routeer-gewicht bevat de overstap-boete: met de
    # default 25 km telt elke track-wissel 25 fantoom-km mee, en op een
    # gestitchte corridor zijn dat er tientallen. Gemeten op EMO -> stroomopwaarts
    # gaf dat 339,6 km waar de echte gevaren afstand 189,6 km is. De
    # halte-nummering hangt NIET van de boete af (die raakt alleen de
    # spaak-gewichten), dus ha/hb blijven geldig in deze tweede router.
    router0 = bouw_router(graaf, cache, alleen_op=_richting(args),
                          overstap_boete=0.0, stil=True)
    dA = dijkstra(router0["M"], directed=False, indices=ha)
    dB = dijkstra(router0["M"], directed=False, indices=hb)
    print("  (afstanden hieronder zijn ECHTE gevaren km — boete-vrij gemeten)")
    for naam, dist, doel in ((na, dA, (lat_b, lon_b)), (nb, dB, (lat_a, lon_a))):
        ber = np.isfinite(dist)
        print(f"\n  vanuit {naam}: {ber.sum():,} haltes bereikbaar · verst "
              f"{np.nanmax(np.where(ber, dist, np.nan)):.1f} km langs de graaf")
        hemel = km_np(router["h_lat"], router["h_lon"], doel[0], doel[1])
        j = int(np.argmin(np.where(ber, hemel, np.inf)))
        print(f"    verste bereikbare punt RICHTING de tegenpartij: "
              f"{router['h_lat'][j]:.5f}, {router['h_lon'][j]:.5f} "
              f"(knoop {router['h_knoop'][j]}) · {dist[j]:.1f} km langs de graaf "
              f"· nog {hemel[j]:.1f} km hemelsbreed te gaan")
    if label[ha] != label[hb]:
        # Exact, niet op een steekproef: een steekproef van elke 25e halte kan
        # juist het dichtste paar overslaan, en dít getal is de kern van de
        # diagnose ("hoe breed is het gat werkelijk"). cKDTree op dezelfde
        # equirectangulaire km-projectie die de rest van dit bestand gebruikt.
        from scipy.spatial import cKDTree
        ca = np.flatnonzero(np.isfinite(dA))
        cb = np.flatnonzero(np.isfinite(dB))
        lat0 = float(np.median(router["h_lat"]))
        f = math.cos(math.radians(lat0)) * 111.32

        def xy(ix):
            return np.c_[router["h_lon"][ix] * f, router["h_lat"][ix] * 111.32]

        boom = cKDTree(xy(cb))
        afst, welke = boom.query(xy(ca), k=1)
        i = int(np.argmin(afst))
        best = (float(afst[i]), int(ca[i]), int(cb[welke[i]]))
        print(f"\n  KLEINSTE GAT tussen de twee componenten: {best[0]:.2f} km "
              f"hemelsbreed (exact over {len(ca):,} x {len(cb):,} haltes)")
        for h in (best[1], best[2]):
            print(f"    {router['h_lat'][h]:.5f}, {router['h_lon'][h]:.5f} "
                  f"(knoop {router['h_knoop'][h]}, component {label[h]})")

    if args.corridor_as:
        as_ = args.corridor_as
        e_label = label[np.searchsorted(
            router["haltes"],
            graaf["edge_tix"].astype(np.int64) * HALTE_SCH
            + graaf["edge_i0"].astype(np.int64))]
        km_per_comp = np.bincount(e_label, weights=graaf["edge_km"],
                                  minlength=n_comp)
        groot = [c for c in range(n_comp) if km_per_comp[c] >= args.min_comp_km]
        print(f"\n  componenten met >= {args.min_comp_km} km, gesorteerd langs "
              f"{as_} ({len(groot)} van {n_comp}):")
        rijen = []
        for c in groot:
            h = np.flatnonzero(label == c)
            v = router["h_lon"][h] if as_ == "lon" else router["h_lat"][h]
            rijen.append((float(v.min()), float(v.max()), c, len(h),
                          float(km_per_comp[c])))
        rijen.sort()
        for lo_, hi_, c, nh, kmc in rijen[:args.max_comp]:
            print(f"    comp {c:<6} {as_} {lo_:.3f}..{hi_:.3f} · "
                  f"{nh:,} haltes · {kmc:,.0f} km")
        print(f"  breuken langs {as_} (leeg gat tussen opeenvolgende "
              f"componenten, >= {args.min_gat} km):")
        f_km = (111.32 * math.cos(math.radians(float(np.median(router["h_lat"]))))
                if as_ == "lon" else 111.32)
        vorige = None
        gaten = 0
        for lo_, hi_, c, nh, kmc in rijen:
            if vorige is not None and lo_ > vorige[1]:
                gat = (lo_ - vorige[1]) * f_km
                if gat >= args.min_gat:
                    gaten += 1
                    print(f"    {as_} {vorige[1]:.3f} -> {lo_:.3f} = "
                          f"{gat:.1f} km leeg (comp {vorige[2]} -> {c})")
            if vorige is None or hi_ > vorige[1]:
                vorige = (lo_, hi_, c)
        if not gaten:
            print("    (geen)")
    metrics(graaf, cache, router, [na, nb])


def main():
    p = argparse.ArgumentParser(
        description="Track-graaf: laag 1 (hele-track-match) + laag 2 (graaf op "
                    "raakpunten). Geen bundeling, geen herrekende geometrie.")
    sub = p.add_subparsers(dest="cmd", required=True)

    def gedeeld(sp, tracks_verplicht=False):
        sp.add_argument("--tracks", type=Path, nargs="+",
                        required=tracks_verplicht,
                        help="één of meer jsonl.gz van bouw_tracks.py")
        sp.add_argument("--snap", type=float, default=SNAP_KM)
        sp.add_argument("--kand-km", type=float, default=KAND_KM)
        sp.add_argument("--max-regels", type=int, default=None,
                        help="alleen voor proefdraaien")
        sp.add_argument("--kies", choices=("mediaan", "kort", "snap"),
                        default="mediaan")
        sp.add_argument("--richting", choices=("beide", "op", "af"),
                        default="beide",
                        help="routeer alleen over opvaart- of afvaart-banen. "
                             "beide = default; de knoop-ruimte is altijd "
                             "gedeeld (zie valkuil 2).")
        sp.add_argument("--overstap-boete", type=float, default=OVERSTAP_BOETE,
                        help="km-opslag per track-wissel bij het routeren. "
                             "GEEN geometrie: de gerapporteerde lengte blijft de "
                             "getekende lijn. Zie de kop — met 0 hugt het "
                             "kortste pad de binnenbocht van elke bocht.")

    s = sub.add_parser("laag1", help="hele-track-match (geen graaf nodig)")
    gedeeld(s, True)
    s.add_argument("--punten", nargs="*", default=[])
    s.add_argument("--van")
    s.add_argument("--naar")
    s.add_argument("--alle-paren", action="store_true")
    s.set_defaults(fn=cmd_laag1)

    s = sub.add_parser("graaf", help="graaf bouwen (+ track-cache)")
    gedeeld(s, True)
    s.add_argument("--bbox", help="z,w,n,o — beperkt de graaf tot een corridor")
    s.add_argument("--uit", required=True, help="pad zonder extensie")
    s.add_argument("--punten", nargs="*", default=[])
    s.add_argument("--min-seg-km", type=float, default=MIN_SEG_KM)
    s.add_argument("--max-stap-km", type=float, default=MAX_STAP_KM)
    s.set_defaults(fn=cmd_graaf)

    s = sub.add_parser("route", help="routeer over de graaf (laag 2)")
    gedeeld(s)
    s.add_argument("--graaf", required=True)
    s.add_argument("--van", required=True)
    s.add_argument("--naar", required=True)
    s.set_defaults(fn=cmd_route)

    s = sub.add_parser("toets", help="acceptatietoets: laag 1 + laag 2 + bewijs")
    gedeeld(s)
    s.add_argument("--graaf", required=True)
    s.add_argument("--van", required=True)
    s.add_argument("--naar", required=True)
    s.add_argument("--verwacht-km", type=float)
    s.add_argument("--alle", action="store_true")
    s.add_argument("--geen-laag1", action="store_true")
    s.set_defaults(fn=cmd_toets)

    s = sub.add_parser("eiland", help="beide geulen om een eiland bereikbaar?")
    gedeeld(s)
    s.add_argument("--graaf", required=True)
    s.add_argument("--van", default=None)
    s.add_argument("--naar", default=None)
    s.add_argument("--via", default=None,
                   help="lat,lon in de ANDERE arm — dwingt geul 2 die arm in. "
                        "Zonder dit vindt de toets het kortste knoop-disjuncte "
                        "pad, en dat is op een drukke rivier een parallelle "
                        "doorvaart in dezelfde geul.")
    s.add_argument("--zoek", action="store_true", help="scan naar kandidaten")
    s.add_argument("--bbox")
    s.add_argument("--min-sep", type=float, default=0.6, help="km")
    s.add_argument("--max-sep", type=float, default=5.0,
                   help="km — breder dan dit is geen eiland maar een meander "
                        "of een tweede waterlichaam in dezelfde lat-band")
    s.add_argument("--min-lengte", type=float, default=3.0, help="km")
    s.set_defaults(fn=cmd_eiland)

    s = sub.add_parser("diagnose", help="componenten/breuken tussen twee punten")
    gedeeld(s)
    s.add_argument("--graaf", required=True)
    s.add_argument("--van", required=True)
    s.add_argument("--naar", required=True)
    s.add_argument("--corridor-as", choices=("lon", "lat"), default=None)
    s.add_argument("--min-comp-km", type=float, default=5.0)
    s.add_argument("--min-gat", type=float, default=2.0)
    s.add_argument("--max-comp", type=int, default=40)
    s.set_defaults(fn=cmd_diagnose)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
