#!/usr/bin/env python3
"""maak_leidingbeen_olie_doba_kribi.py - b1 van olie-doba-kribi.

Brief: v2/design/routebrieven/olie-doba-kribi.md (b1). Tsjaad-Kameroen-leiding (TOTCO/COTCO)
van het Kome-CPF tot het OSM-einde van de onderzeese buis bij Kribi: drie vaste OSM-ways
(man_made=pipeline, substance=oil) uit de lokale Geofabrik-extracts tsjaad en kameroen,
op way-id, in reisvolgorde, gestikt op 0 m. Dubbele mapping (197953902, 198082553,
1189390159, 198081296) wordt NIET gebruikt.

pyosmium is op deze machine geblokkeerd: dit script leest de pbf met de pure-Python lezer uit
wegscan_puur.py (blobs/prim/fields; nodes eerst, dan ways).

Uitvoer: v2/build-cache/ais/graaf/olie-doba-kribi-leiding-chad-cameroon.geojson (FeatureCollection,
een LineString, [lon,lat]).

Draaien:  python v2/tools/maak_leidingbeen_olie_doba_kribi.py --schrijf
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import wegscan_puur as W  # noqa: E402

WORTEL = os.path.dirname(HIER)  # .../v2
GEOFABRIK = os.path.join(WORTEL, "build-cache", "geofabrik")
UIT = os.path.join(WORTEL, "build-cache", "ais", "graaf", "olie-doba-kribi-leiding-chad-cameroon.geojson")

# (extract, way-id) in reisvolgorde
KETEN = [("tsjaad", 926239436), ("kameroen", 199342881), ("kameroen", 257189942)]
KOME = (16.7958, 8.5304)   # (lon, lat)
R = 6371.0088


def km(a, b):
    la1, lo1 = math.radians(a[1]), math.radians(a[0])
    la2, lo2 = math.radians(b[1]), math.radians(b[0])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * R * math.asin(math.sqrt(h))


def lees_ways(pbf, wanted):
    """Geeft {way_id: [(lon,lat),...]} voor de gevraagde way-id's (pure-Python pbf)."""
    # pas 1: ways (refs + tags)
    gevonden = {}
    for typ, raw in W.blobs(pbf):
        if typ != "OSMData":
            continue
        st, groups, gran, la, lo = W.prim(raw)
        for g in groups:
            for fn, wmsg in W.fields(g):
                if fn != 3:
                    continue
                wid = None
                refs = None
                ks = vs = None
                for f2, v in W.fields(wmsg):
                    if f2 == 1:
                        wid = v
                    elif f2 == 2:
                        ks = W.packed_varints(v)
                    elif f2 == 3:
                        vs = W.packed_varints(v)
                    elif f2 == 8:
                        refs = v
                if wid in wanted and refs:
                    tags = {st[k].decode(): st[x].decode("utf-8", "replace") for k, x in zip(ks or [], vs or [])}
                    gevonden[wid] = (tags, np.cumsum(W.np_sint(refs)))
    print(f"  {os.path.basename(pbf)}: {len(gevonden)}/{len(wanted)} ways gevonden", flush=True)
    for wid, (tags, r) in gevonden.items():
        print(f"    way {wid}: {len(r)} nodes; man_made={tags.get('man_made')} substance={tags.get('substance')} "
              f"operator={tags.get('operator')} name={tags.get('name')}", flush=True)
    if not gevonden:
        return {}
    nodig = np.unique(np.concatenate([r for _, r in gevonden.values()]))
    # pas 2: node-coordinaten
    cid, clat, clon = [], [], []
    for typ, raw in W.blobs(pbf):
        if typ != "OSMData":
            continue
        st, groups, gran, la, lo = W.prim(raw)
        for g in groups:
            for fn, msg in W.fields(g):
                if fn == 2:
                    ids = lats = lons = None
                    for f2, v in W.fields(msg):
                        if f2 == 1:
                            ids = np.cumsum(W.np_sint(v))
                        elif f2 == 8:
                            lats = np.cumsum(W.np_sint(v))
                        elif f2 == 9:
                            lons = np.cumsum(W.np_sint(v))
                    mk = np.isin(ids, nodig)
                    if mk.any():
                        cid.append(ids[mk])
                        clat.append(((la + gran * lats[mk]) * 1e-9))
                        clon.append(((lo + gran * lons[mk]) * 1e-9))
    cid = np.concatenate(cid)
    clat = np.concatenate(clat)
    clon = np.concatenate(clon)
    o = np.argsort(cid)
    cid, clat, clon = cid[o], clat[o], clon[o]
    uit = {}
    for wid, (tags, r) in gevonden.items():
        ix = np.searchsorted(cid, r).clip(0, len(cid) - 1)
        if not (cid[ix] == r).all():
            raise SystemExit(f"way {wid}: {(cid[ix] != r).sum()} nodes ontbreken")
        uit[wid] = [(float(clon[i]), float(clat[i])) for i in ix]
    return uit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schrijf", action="store_true")
    args = ap.parse_args()

    per_extract = {}
    for ext, wid in KETEN:
        per_extract.setdefault(ext, set()).add(wid)
    geo = {}
    for ext, wanted in per_extract.items():
        pbf = os.path.join(GEOFABRIK, f"{ext}-latest.osm.pbf")
        geo.update(lees_ways(pbf, wanted))
    lijn = []
    for ext, wid in KETEN:
        p = geo[wid]
        if lijn:
            if km(lijn[-1], p[0]) > km(lijn[-1], p[-1]):
                p = p[::-1]
        else:
            if km(KOME, p[0]) > km(KOME, p[-1]):
                p = p[::-1]
        if lijn:
            naad = km(lijn[-1], p[0])
            print(f"  naad voor way {wid}: {naad * 1000:.1f} m")
            if naad > 0.001:
                raise SystemExit(f"naad {naad:.3f} km > 1 m bij way {wid}")
            p = p[1:]
        lijn.extend(p)
        print(f"  way {wid}: {len(p)} punten, begin {p[0][1]:.4f},{p[0][0]:.4f}")
    totaal = sum(km(lijn[i], lijn[i + 1]) for i in range(len(lijn) - 1))
    print(f"gestikt: {len(lijn)} punten, {totaal:.1f} km; kop {lijn[0][1]:.5f},{lijn[0][0]:.5f} ({km(lijn[0], KOME):.2f} km van Kome-anker); "
          f"staart {lijn[-1][1]:.5f},{lijn[-1][0]:.5f}")
    if args.schrijf:
        coords = [[round(x, 5), round(y, 5)] for x, y in lijn]
        doc = {"type": "FeatureCollection", "features": [{
            "type": "Feature",
            "properties": {
                "naam": "Tsjaad-Kameroen-leiding (TOTCO/COTCO), Kome-CPF - onderzeese buis Kribi",
                "km": round(totaal, 2), "punten": len(coords),
                "bron": "OpenStreetMap-bijdragers (ODbL), extracts tsjaad+kameroen, ways 926239436+199342881+257189942",
                "gereedschap": "maak_leidingbeen_olie_doba_kribi.py",
            },
            "geometry": {"type": "LineString", "coordinates": coords},
        }]}
        os.makedirs(os.path.dirname(UIT), exist_ok=True)
        with open(UIT, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False)
        print(f"geschreven: {UIT} ({os.path.getsize(UIT) / 1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
