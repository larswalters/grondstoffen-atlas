#!/usr/bin/env python3
"""
knoop_riviernet.py — knoopt het riviernet aan elkaar door het WATER ZELF te volgen.

Waarom dit bestaat (Lars, 2026-07-21): op veel plekken houdt de graaf op terwijl
je vanuit de ruimte de rivier gewoon ziet doorlopen. De oorzaak is de bron, niet
de rivier: het bevaarbaarheidssignaal (CEMT/ship/boat/draft) stopt halverwege,
dus de bulkscan knipte de lijn daar af. Zulke stukken horen aan elkaar — nog
vóór de havens en de overslag.

Aanpak — het water is de gids, geen zoekradius:
  1. laad vaarwegen_bulk.geojson en draai EERST dezelfde twee-traps heal als de
     bake. Anders zoekt dit gereedschap bruggen voor naden die de heal al legt,
     en vindt een walk een omweg van kilometers waar de heal 30 m nodig heeft.
  2. elk DOODLOPEND uiteinde van het geheelde net is een zoekpunt.
  3. per extract: volg vanaf elk zoekpunt de óngetagde waterway=river|canal-
     geometrie in de pbf. OSM knipt een way precies waar de tags veranderen,
     dus het ongetagde vervolg deelt zijn knoop-coördinaat exact met ons
     uiteinde. De walk (Dijkstra over de ongetagde ways) stopt zodra hij een
     ANDER component van het net raakt — dat pad is het verbindingsstuk.
  4. kortste verbinding per componentpaar wint (progressieve union, zoals de
     heal); zelfde-component-treffers zijn per constructie uitgesloten — een
     ongetagd zijkanaal terug het eigen net in is precies de meander-sluipweg.

Uitvoer: build-cache/vaarwegen_bruggen.geojson met signaal "brug" per lijn.
"brug" draagt géén gabariet → onbekende maat = géén grens (het draagprincipe);
de bake bakt ze mee via --bruggen en de heal hecht daar de laatste meters.

Guards:
  * ways die een waterway=waterfall|dam-punt raken zijn onbegaanbaar — een
    waterval of dam zónder sluis is een GOEDE reden om los te blijven. (Stuwen
    met een sluis liggen als apart sluiskanaal in OSM; de walk neemt dan
    vanzelf dat kanaal.)
  * getagde snippers < BULK_MIN_KM (uit het net gefilterd) doen wél mee als
    wandelgeometrie — het is water, alleen te kort voor een eigen lijn.
  * begrensd op --max-km per brug en een relaxatie-plafond per zoekpunt, zodat
    een vlechtende delta de scan niet opeet. Wat wegvalt wordt geteld en
    gemeld — geen stille aftopping.

Draaien:  python v2/tools/knoop_riviernet.py                        (alles)
          python v2/tools/knoop_riviernet.py --extracts nederland,us-illinois
"""

import argparse
import hashlib
import heapq
import json
import math
import os
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fetch_waterways as fw  # noqa: E402 — extract-registry, filter, simplify

CACHE = fw.CACHE
BRUG_CACHE = os.path.join(CACHE, "bruggen")
BULK_GEOJSON = os.path.join(CACHE, "vaarwegen_bulk.geojson")
UIT_GEOJSON = os.path.join(CACHE, "vaarwegen_bruggen.geojson")

KNOOP_VERSIE = 1
BRUG_SOORT = {"river", "canal"}    # stream/ditch/drain bewust niet: een kreek
                                   # is geen "rivier die zichtbaar doorloopt"
BLOKKEER_SOORT = {"waterfall", "dam"}
FIJN = 1e-5                        # = bake_marnet.BULK_QUANT (assert in prep)
DOEL_CEL = 0.0008                  # ~90 m: raakvlak met het getagde net; de
                                   # sprong naar de exacte vertex blijft daarmee
                                   # in de tier-1-klasse (≤ ~250 m)
RELAX_CAP = 30_000                 # plafond per zoekpunt (vlechtende delta's)


def q_fijn(p):
    return (round(p[0] / FIJN), round(p[1] / FIJN))


def q_doel(p):
    return (round(p[0] / DOEL_CEL), round(p[1] / DOEL_CEL))


# ---------------------------------------------------------------- voorbereiding

def _laad_lijnen(pad):
    gj = json.load(open(pad, encoding="utf-8"))
    per = {}
    for f in gj["features"]:
        p = f["properties"]
        pts = [(lo, la) for lo, la in f["geometry"]["coordinates"]]
        if len(pts) > 1:
            per.setdefault(p["label"], []).append((p.get("signaal") or "?", pts))
    return per


def prep_hash(heal_km, corridor_km):
    st = os.stat(BULK_GEOJSON)
    ruw = repr((KNOOP_VERSIE, st.st_size, int(st.st_mtime), heal_km, corridor_km,
                DOEL_CEL, sorted(BRUG_SOORT)))
    return hashlib.sha1(ruw.encode()).hexdigest()[:16]


def prep(heal_km, corridor_km):
    """Heal → componenten → zoekpunten + doelcellen, gecached op de geojson.

    De heavy imports (bake_marnet trekt shapely/numpy/searoute binnen) staan
    bewust HIER: de workers hebben ze niet nodig.
    """
    import numpy as np
    ph = prep_hash(heal_km, corridor_km)
    basis = os.path.join(BRUG_CACHE, f"prep-{ph}")
    if os.path.exists(basis + ".npz") and os.path.exists(basis + "-zoekpunten.json"):
        z = json.load(open(basis + "-zoekpunten.json", encoding="utf-8"))
        print(f"voorbereiding uit cache ({ph}): {len(z):,} zoekpunten")
        return ph

    import bake_marnet as bm
    assert bm.BULK_QUANT == FIJN, "FIJN loopt uit de pas met bake_marnet.BULK_QUANT"

    per = _laad_lijnen(BULK_GEOJSON)
    n_lijnen = sum(len(v) for v in per.values())
    print(f"geladen: {n_lijnen:,} lijnen uit {os.path.basename(BULK_GEOJSON)}")

    # Zelfde heal als de bake, geïtereerd tot convergentie (max 6 rondes).
    t0 = time.time()
    for ronde in range(6):
        n1 = n2 = 0
        if heal_km > 0:
            n1, _, _ = bm._heal_riviernet(per, heal_km)
        if corridor_km > 0:
            n2, _, _ = bm._heal_corridors(per, corridor_km)
        if n1 + n2 == 0:
            break
    comp, idx = bm._lijn_componenten(per)
    wortels = {}
    for gi in range(len(idx)):
        wortels.setdefault(comp[gi], len(wortels))
    comp = [wortels[c] for c in comp]
    print(f"heal + componenten in {time.time() - t0:,.0f} s: "
          f"{len(wortels):,} componenten (zelfde parameters als de bake: "
          f"--heal-km {heal_km} --corridor-km {corridor_km})")

    # Doodlopende uiteinden: endpoint-cel die geen enkele ANDERE lijn raakt.
    vcell = {}
    for gi, (regio, li) in enumerate(idx):
        for p in per[regio][li][1]:
            c = q_fijn(p)
            oud = vcell.get(c)
            if oud is None:
                vcell[c] = gi
            elif oud != gi:
                vcell[c] = -1          # gedeeld met een andere lijn
    zoekpunten = []
    for gi, (regio, li) in enumerate(idx):
        pts = per[regio][li][1]
        for e in (0, -1):
            if vcell.get(q_fijn(pts[e])) == gi:
                zoekpunten.append([round(pts[e][0], 6), round(pts[e][1], 6),
                                   comp[gi], regio])

    # Doelcellen: elk vertex van het net, één exact coördinaat per (cel, comp).
    doel = {}
    for gi, (regio, li) in enumerate(idx):
        for p in per[regio][li][1]:
            sleutel = (*q_doel(p), comp[gi])
            if sleutel not in doel:
                doel[sleutel] = (round(p[0], 6), round(p[1], 6))
    cx = np.fromiter((k[0] for k in doel), dtype=np.int64, count=len(doel))
    cy = np.fromiter((k[1] for k in doel), dtype=np.int64, count=len(doel))
    cc = np.fromiter((k[2] for k in doel), dtype=np.int64, count=len(doel))
    lon = np.fromiter((v[0] for v in doel.values()), dtype=np.float64, count=len(doel))
    lat = np.fromiter((v[1] for v in doel.values()), dtype=np.float64, count=len(doel))

    os.makedirs(BRUG_CACHE, exist_ok=True)
    np.savez_compressed(basis + ".npz", cx=cx, cy=cy, comp=cc, lon=lon, lat=lat)
    with open(basis + "-zoekpunten.json", "w", encoding="utf-8") as f:
        json.dump(zoekpunten, f)
    print(f"voorbereiding klaar: {len(zoekpunten):,} zoekpunten · "
          f"{len(doel):,} doelcellen → prep-{ph}")
    return ph


# ------------------------------------------------------------------- de walk

def _reconstrueer(prev, ways, cel):
    """Pad van het zoekpunt tot `cel`, als puntenreeks."""
    stukken = []
    while cel in prev:
        wi, van = prev[cel]
        pts = ways[wi][0]
        stukken.append(pts if q_fijn(pts[0]) == van else pts[::-1])
        cel = van
    pad = []
    for stuk in reversed(stukken):
        pad.extend(stuk if not pad else stuk[1:])
    return pad


def brug_scan_extract(args):
    """Worker: één extract — pbf scannen, walks draaien, bruggen cachen."""
    sleutel, ph, max_km = args
    st = os.stat(fw.extract_pad(sleutel))
    ruw = repr((KNOOP_VERSIE, sleutel, st.st_size, int(st.st_mtime), ph, max_km,
                RELAX_CAP))
    fp_hash = hashlib.sha1(ruw.encode()).hexdigest()[:16]
    cpad = os.path.join(BRUG_CACHE, f"{sleutel}-{fp_hash}.json")
    if os.path.exists(cpad):
        c = json.load(open(cpad, encoding="utf-8"))
        return sleutel, c, True

    import numpy as np
    import osmium

    # 1 · pbf → wandelgeometrie (ongetagd water) + blokkadepunten
    blok_cellen = set()
    ways = []                       # (pts, km)
    proc = (osmium.FileProcessor(fw.extract_pad(sleutel))
            .with_locations()
            .with_filter(osmium.filter.EntityFilter(osmium.osm.NODE | osmium.osm.WAY))
            .with_filter(osmium.filter.KeyFilter("waterway")))
    for obj in proc:
        soort = obj.tags.get("waterway") or ""
        if obj.is_node():
            if soort in BLOKKEER_SOORT:
                blok_cellen.add(q_fijn((obj.location.lon, obj.location.lat)))
            continue
        if soort in BLOKKEER_SOORT:
            for n in obj.nodes:
                if n.location.valid():
                    blok_cellen.add(q_fijn((n.location.lon, n.location.lat)))
            continue
        if soort not in BRUG_SOORT:
            continue
        pts = [(n.location.lon, n.location.lat) for n in obj.nodes
               if n.location.valid()]
        if len(pts) < 2:
            continue
        pts = fw.simplify(pts, fw.BULK_SIMPLIFY_KM)
        cum = [0.0]
        for i in range(1, len(pts)):
            cum.append(cum[-1] + fw.km(pts[i - 1], pts[i]))
        L = cum[-1]
        if L <= 0:
            continue
        code, _ = fw.bulk_signaal(obj.tags)
        if code is not None and L >= fw.BULK_MIN_KM:
            continue                # zit al in het net — dat is een DOEL, geen pad
        ways.append(([(round(lo, 6), round(la, 6)) for lo, la in pts], L, cum))

    if not ways:
        uit = {"bruggen": [], "zoekpunten": 0, "geplafonneerd": 0, "ways": 0}
        os.makedirs(BRUG_CACHE, exist_ok=True)
        json.dump(uit, open(cpad, "w", encoding="utf-8"))
        return sleutel, uit, False

    # bbox van de wandelgeometrie bepaalt welke zoekpunten/doelen meedoen
    lo0 = min(p[0] for pts, _L, _c in ways for p in (pts[0], pts[-1]))
    lo1 = max(p[0] for pts, _L, _c in ways for p in (pts[0], pts[-1]))
    la0 = min(p[1] for pts, _L, _c in ways for p in (pts[0], pts[-1]))
    la1 = max(p[1] for pts, _L, _c in ways for p in (pts[0], pts[-1]))
    marge = 0.05

    # 2 · adjacency op endpoint-cellen; geblokkeerde ways vervallen als geheel
    adj = {}
    for wi, (pts, _L, _c) in enumerate(ways):
        if any(q_fijn(p) in blok_cellen for p in pts):
            continue
        for e in (0, -1):
            adj.setdefault(q_fijn(pts[e]), []).append((wi, e))

    # 3 · doelcellen binnen de bbox, opgeblazen naar 3×3 (dekt de simplify-drift)
    basis = os.path.join(BRUG_CACHE, f"prep-{ph}")
    d = np.load(basis + ".npz")
    m = ((d["lon"] >= lo0 - marge) & (d["lon"] <= lo1 + marge) &
         (d["lat"] >= la0 - marge) & (d["lat"] <= la1 + marge))
    doel = {}
    for cxi, cyi, ci, lo, la in zip(d["cx"][m], d["cy"][m], d["comp"][m],
                                    d["lon"][m], d["lat"][m]):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                doel.setdefault((int(cxi) + dx, int(cyi) + dy), []).append(
                    (int(ci), float(lo), float(la)))

    zoekpunten = [z for z in json.load(open(basis + "-zoekpunten.json",
                                            encoding="utf-8"))
                  if lo0 - marge <= z[0] <= lo1 + marge
                  and la0 - marge <= z[1] <= la1 + marge]

    # 4 · Dijkstra per zoekpunt over de ongetagde ways
    bruggen, geplafonneerd = [], 0
    for zlon, zlat, zcomp, regio in zoekpunten:
        start = q_fijn((zlon, zlat))
        if start not in adj:
            continue                # geen ongetagd vervolg op dit uiteinde
        dist, prev = {start: 0.0}, {}
        heap = [(0.0, start)]
        relax, klaar = 0, None
        while heap and klaar is None:
            dcur, cel = heapq.heappop(heap)
            if dcur > dist.get(cel, 1e18) + 1e-9 or dcur >= max_km:
                continue
            for wi, e in adj.get(cel, ()):  # e: uiteinde dat op deze cel ligt
                relax += 1
                if relax > RELAX_CAP:
                    geplafonneerd += 1
                    klaar = False
                    break
                pts, L, cum = ways[wi]
                volg = pts if e == 0 else pts[::-1]
                for i in range(1, len(volg)):
                    acc = dcur + (cum[i] if e == 0 else L - cum[len(pts) - 1 - i])
                    if acc > max_km:
                        break
                    for ct, tlon, tlat in doel.get(q_doel(volg[i]), ()):
                        if ct != zcomp:
                            pad = _reconstrueer(prev, ways, cel) or [(zlon, zlat)]
                            if pad[-1] == volg[0]:
                                pad = pad + list(volg[1:i + 1])
                            else:
                                pad = pad + list(volg[:i + 1])
                            if fw.km(pad[-1], (tlon, tlat)) > 1e-4:
                                pad.append((tlon, tlat))
                            bruggen.append({
                                "km": round(acc, 2), "van": zcomp, "naar": ct,
                                "regio": regio,
                                "pts": [[round(lo, 6), round(la, 6)]
                                        for lo, la in pad],
                            })
                            klaar = True
                            break
                    if klaar:
                        break
                if klaar:
                    break
                ander = q_fijn(volg[-1])
                nd = dcur + L
                if nd < dist.get(ander, 1e18) - 1e-9 and nd < max_km:
                    dist[ander] = nd
                    prev[ander] = (wi, cel)
                    heapq.heappush(heap, (nd, ander))

    uit = {"bruggen": bruggen, "zoekpunten": len(zoekpunten),
           "geplafonneerd": geplafonneerd, "ways": len(ways)}
    os.makedirs(BRUG_CACHE, exist_ok=True)
    tijdelijk = cpad + ".deel"
    json.dump(uit, open(tijdelijk, "w", encoding="utf-8"))
    os.replace(tijdelijk, cpad)
    return sleutel, uit, False


# ---------------------------------------------------------------- orkestratie

def hoofd():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extracts", help="komma-gescheiden extract-namen "
                                      "(default: alle aanwezige)")
    ap.add_argument("--workers", type=int)
    ap.add_argument("--max-km", type=float, default=300.0,
                    help="langste toegestane brug-walk (default 300)")
    ap.add_argument("--heal-km", type=float, default=0.25,
                    help="MOET gelijk zijn aan de bake (default 0.25)")
    ap.add_argument("--corridor-km", type=float, default=2.0,
                    help="MOET gelijk zijn aan de bake (default 2.0)")
    ap.add_argument("--alleen-prep", action="store_true")
    a = ap.parse_args()

    ph = prep(a.heal_km, a.corridor_km)
    if a.alleen_prep:
        return

    if a.extracts:
        sleutels = [s.strip() for s in a.extracts.split(",") if s.strip()]
    else:
        sleutels = sorted(s for s in fw.GEOFABRIK_REGIOS
                          if os.path.exists(fw.extract_pad(s)))
    ontbreekt = [s for s in sleutels if not os.path.exists(fw.extract_pad(s))]
    if ontbreekt:
        raise SystemExit("extracts ontbreken: " + ", ".join(ontbreekt))

    workers = a.workers or max(1, min(14, (os.cpu_count() or 2) - 2))
    gb = sum(os.path.getsize(fw.extract_pad(s)) for s in sleutels) / 1e9
    print(f"\nknoopscan: {len(sleutels)} extracts, {gb:,.1f} GB, "
          f"{workers} workers, max {a.max_km:,.0f} km per brug")

    t0 = time.time()
    taken = [(s, ph, a.max_km) for s in sleutels]
    if workers == 1 or len(sleutels) == 1:
        resultaten = (brug_scan_extract(t) for t in taken)
    else:
        import multiprocessing as mp
        pool = mp.Pool(workers)
        resultaten = pool.imap_unordered(brug_scan_extract, taken)

    alle, plafond = [], 0
    for i, (sleutel, uit, cache) in enumerate(resultaten, 1):
        alle.extend(uit["bruggen"])
        plafond += uit["geplafonneerd"]
        print(f"  [{i}/{len(sleutels)}] {sleutel:<26} "
              f"{len(uit['bruggen']):4,} bruggen · {uit['zoekpunten']:5,} zoekpunten"
              f" · {uit['ways']:7,} ongetagde ways"
              f"{' (cache)' if cache else ''}", flush=True)
    if workers > 1 and len(sleutels) > 1:
        pool.close()
        pool.join()

    # Kortste brug per componentpaar wint; de rest zijn dubbelgangers (beide
    # oevers van hetzelfde gat zoeken naar elkaar) of parallelle omwegen.
    alle.sort(key=lambda b: b["km"])
    cmap = {}

    def vind(x):
        while cmap.setdefault(x, x) != x:
            cmap[x] = cmap[cmap[x]]
            x = cmap[x]
        return x

    houd, dubbel = [], 0
    for b in alle:
        ra, rb = vind(b["van"]), vind(b["naar"])
        if ra == rb:
            dubbel += 1
            continue
        cmap[rb] = ra
        houd.append(b)

    features = [{
        "type": "Feature",
        "properties": {"label": b["regio"], "regio": b["regio"].replace("bulk-", ""),
                       "zeevaart": False, "signaal": "brug", "km": b["km"]},
        "geometry": {"type": "LineString", "coordinates": b["pts"]},
    } for b in houd]
    with open(UIT_GEOJSON, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection",
                   "bron": "OpenStreetMap contributors (ODbL) via Geofabrik-regio-extract",
                   "laag": "bruggen", "knoopVersie": KNOOP_VERSIE, "prep": ph,
                   "maxKm": a.max_km, "healKm": a.heal_km,
                   "corridorKm": a.corridor_km, "extracts": sleutels,
                   "features": features}, f, ensure_ascii=False)

    per_regio = {}
    for b in houd:
        per_regio[b["regio"]] = per_regio.get(b["regio"], 0.0) + b["km"]
    print(f"\nbruggen per regio (na ontdubbeling, {dubbel:,} dubbelgangers weg"
          f"{f' · {plafond} zoekpunten geplafonneerd' if plafond else ''}):")
    for regio, L in sorted(per_regio.items(), key=lambda kv: -kv[1]):
        print(f"  {regio:<10} {L:9,.1f} km")
    print(f"  TOTAAL     {sum(b['km'] for b in houd):9,.1f} km · {len(houd):,} bruggen")
    langste = sorted(houd, key=lambda b: -b["km"])[:15]
    if langste:
        print("\nlangste bruggen (kijk deze na op de bol):")
        for b in langste:
            mid = b["pts"][len(b["pts"]) // 2]
            print(f"  {b['km']:7,.1f} km · {b['regio']:<8} · rond "
                  f"({mid[1]:.3f}, {mid[0]:.3f})")
    print(f"\ngeschreven: {UIT_GEOJSON} "
          f"({os.path.getsize(UIT_GEOJSON) / 1024:,.0f} KB)")
    print(f"klaar in {time.time() - t0:,.0f} s — bak mee met: "
          f"bake_marnet.py --bulk ... --binnenwater --bruggen "
          f"build-cache/vaarwegen_bruggen.geojson")


if __name__ == "__main__":
    hoofd()
