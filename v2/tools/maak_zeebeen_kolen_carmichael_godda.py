"""Zeebeen voor kolen-carmichael-godda: MARNET-pad van zeeknoop 9009 naar zeeknoop 2373 (21.0, 88.0),
geknipt vanaf vertex 24 (-19.5523, 148.3180, in de Great Barrier Reef-corridor, 46 km van de NQXT-kade).

Waarom dit tool: de kade NQXT Abbot Point ligt 146 km van de dichtstbijzijnde zeeknoop (9023) en
haven-aanloop daarheen hangt; de rechte stippel kade -> zeeknoop loopt 64% over land. Het MARNET-pad
vanaf knoop 9009 passeert op vertex 24 een punt op 46 km van de kade (3,7% land); alleen dat stuk
wordt een stippel, de rest is doorgetrokken MARNET-geometrie.

Gebruik (repo-root):  python v2/tools/maak_zeebeen_kolen_carmichael_godda.py
Uitvoer: v2/build-cache/ais/graaf/kolen-carmichael-godda-zee-marnet.geojson (FeatureCollection, [lon, lat]).
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

sys.path.insert(0, "v2/tools")
import hecht_marnet as H  # noqa: E402

VAN_ID, NAAR_ID, KNIP_VANAF = 9009, 2373, 24
UIT = Path("v2/build-cache/ais/graaf/kolen-carmichael-godda-zee-marnet.geojson")

m = H.lees_marnet("v2/build-cache/marnet-preais")
z = H.marnet_zee(m)
n = len(z["knoop_id"])
a, b = int(z["her"][VAN_ID]), int(z["her"][NAAR_ID])
M = csr_matrix((np.r_[z["km"], z["km"]], (np.r_[z["a"], z["b"]], np.r_[z["b"], z["a"]])), shape=(n, n))
dist, pred = dijkstra(M, directed=False, indices=a, return_predecessors=True)
pad = [b]
while pad[-1] != a:
    pad.append(int(pred[pad[-1]]))
pad = pad[::-1]
lookup = {}
for k, e in enumerate(z["edge"]):
    lookup.setdefault((int(z["a"][k]), int(z["b"][k])), []).append(int(e))
    lookup.setdefault((int(z["b"][k]), int(z["a"][k])), []).append(int(e))
punten = []
for u, v in zip(pad[:-1], pad[1:]):
    best = min(lookup[(u, v)], key=lambda e: m["edge_km"][e])
    g0, g1 = int(m["geom_start"][best]), int(m["geom_start"][best + 1])
    seq = list(range(g0, g1))
    if int(z["her"][int(m["edge_a"][best])]) != u:
        seq = seq[::-1]
    for gi in seq:
        p = (float(m["geom_lat"][gi]), float(m["geom_lon"][gi]))
        if not punten or punten[-1] != p:
            punten.append(p)
print(f"MARNET-pad {VAN_ID} -> {NAAR_ID}: {dist[b]:.1f} km, {len(punten)} punten")
punten = punten[KNIP_VANAF:]
la = np.array([p[0] for p in punten])
lo = np.array([p[1] for p in punten])
km = float(H.seg_km_wrap(la, lo).sum())
print(f"geknipt vanaf vertex {KNIP_VANAF}: {km:.1f} km, {len(punten)} punten, "
      f"begin {punten[0]}, eind {punten[-1]}")
fc = {"type": "FeatureCollection", "features": [{
    "type": "Feature",
    "properties": {"naam": "zeeschip NQXT Abbot Point naar Dhamra-zeeknoop (MARNET, geknipt vanaf vertex 24)",
                   "km": round(km, 1), "knoop_van": VAN_ID, "knoop_naar": NAAR_ID, "knip_vertex": KNIP_VANAF},
    "geometry": {"type": "LineString", "coordinates": [[p[1], p[0]] for p in punten]}}]}
UIT.write_text(json.dumps(fc), encoding="utf-8")
print("geschreven:", UIT)
