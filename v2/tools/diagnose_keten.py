#!/usr/bin/env python3
"""
diagnose_keten.py — waarom vindt de stitcher geen doorlopend waterpad? (M24)

Ontstaan bij [LAR-505] (Albertkanaal) en meteen terugverdiend bij [LAR-493] (het
Main-Donau-Kanaal). De les die het bestaan van dit script rechtvaardigt:

  `RuntimeError: geen doorlopend waterpad tussen de ankers` KLINKT als een gat in
  de ketting, en de reflex is namen bijgokken. Bij het Albertkanaal was de keten
  al heel — 136,3 km in één component — en snapte het ANKER op een geïsoleerd
  fragment van 4 punten. De melding beschreef het symptoom, niet de oorzaak.

Even belangrijk: bouw de diagnose op de ÉCHTE stitcher-graaf. Een eigen
benadering die alleen segment-uiteinden koppelt verbindt anders dan
`kortste_waterpad()` zelf, en wijst je dus de verkeerde kant op.

Uitvoer: waar de ankers landen, hoeveel knopen vanaf de start bereikbaar zijn,
en — als het doel onbereikbaar is — de kleinste gaten tussen de start-/
doelcomponent en hun buren, mét de NAMEN aan weerszijden. Dat laatste is wat je
nodig hebt: bij Kelheim wees het direct de naamvariant `Main-Donau-Kanal (RMD)`
aan in plaats van één van de zestien sluizen.

Draaien:
  python v2/tools/diagnose_keten.py main-donau-kanaal
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_waterways import SYSTEMEN, segmenten_geofabrik, km, STITCH_KM  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

label = sys.argv[1]
s = [x for x in SYSTEMEN if x["label"] == label][0]
segs, _ = segmenten_geofabrik(s)
stitch = STITCH_KM["geofabrik"]

knopen, kid, buren, naam_van = [], {}, [], {}


def nid(p):
    k = (round(p[0], 6), round(p[1], 6))
    if k not in kid:
        kid[k] = len(knopen)
        knopen.append(k)
        buren.append([])
    return kid[k]


uiteinden = []
for pts, naam in segs:
    v = None
    for j, p in enumerate(pts):
        k = nid(p)
        naam_van.setdefault(k, naam)
        if v is not None and v != k:
            buren[v].append(k)
            buren[k].append(v)
        if j == 0 or j == len(pts) - 1:
            uiteinden.append(k)
        v = k

cel = max(stitch / 70.0, 1e-4)
grid = {}
for i, (lo, la) in enumerate(knopen):
    grid.setdefault((int(lo / cel), int(la / cel)), []).append(i)
for i in set(uiteinden):
    lo, la = knopen[i]
    cx, cy = int(lo / cel), int(la / cel)
    r = max(1, int(stitch / (cel * 70.0)) + 1)
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            for j in grid.get((cx + dx, cy + dy), ()):
                if j != i and km(knopen[i], knopen[j]) <= stitch:
                    buren[i].append(j)
                    buren[j].append(i)


def near(a):
    b, bd = -1, 1e18
    for i, p in enumerate(knopen):
        d = km(a, p)
        if d < bd:
            b, bd = i, d
    return b, bd


def bereik(x):
    seen, stk = {x}, [x]
    while stk:
        u = stk.pop()
        for v in buren[u]:
            if v not in seen:
                seen.add(v)
                stk.append(v)
    return seen


st, ds = near(s["anker_zee"])
dl, dd = near(s["anker_binnen"])
print(f"start {st} op {ds:.3f} km ({naam_van[st]}) {knopen[st]}")
print(f"doel  {dl} op {dd:.3f} km ({naam_van[dl]}) {knopen[dl]}")
bs, bd = bereik(st), bereik(dl)
print(f"bereikbaar vanaf start: {len(bs)}/{len(knopen)} · doel bereikbaar: {dl in bs}")
if dl in bs:
    raise SystemExit("keten is heel — de fout zit elders")

# kleinste gat tussen de startcomponent en ELKE andere component
seen, comps = set(), []
for i in range(len(knopen)):
    if i in seen:
        continue
    c = bereik(i)
    seen |= c
    comps.append(c)
comps.sort(key=len, reverse=True)
print(f"componenten: {len(comps)}")

for bron, naam in ((bs, "START"), (bd, "DOEL")):
    beste = []
    for c in comps:
        if c is bron or not (c - bron):
            continue
        d, pa, pb = min(
            ((km(knopen[i], knopen[j]), i, j) for i in bron for j in c),
            key=lambda t: t[0])
        beste.append((d, pa, pb, c))
    beste.sort()
    print(f"\n{naam}-component ({len(bron)} knopen) — 3 dichtstbijzijnde buren:")
    for d, pa, pb, c in beste[:3]:
        print(f"  {d * 1000:7.0f} m  {knopen[pa]} ({naam_van[pa]})"
              f"  ->  {knopen[pb]} ({naam_van[pb]})  [component n={len(c)}]")
