# bake_searoutes.py — bakt de zee-corridors met searoute (MARNET) en schrijft
# data/_searoutes.js. De build-time kant van M18 (design/zeeroutes.md §3).
#
#   python tools/bake_searoutes.py copper          # pilot: alleen koper
#   python tools/bake_searoutes.py                 # alle grondstoffen
#
# Principes (spec §3–§4):
#   - MARNET beslist: corridors kaal haven→haven, geen via-dwang.
#   - Determinisme: gesorteerde sleutels, 3 decimalen, geen tijdstempels.
#   - Fouten hard: een corridor die niet routeert = build FAALT (exit 1) met de
#     coördinaten erbij. Dat zijn de nodes die een handmatig duwtje nodig hebben.
#   - traversed_passages per corridor meegeschreven (M21-query + kruiscontrole).

import json
import math
import subprocess
import sys
import warnings
from pathlib import Path

import searoute as sr

warnings.filterwarnings("ignore")  # de no-path-warning vangen we zelf, hard

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "_searoutes.js"
PRECISION = 3  # ~110 m; vastgelegd in design/zeeroutes.md §3


def gc_km(a, b):
    lo1, la1, lo2, la2 = map(math.radians, [a["lon"], a["lat"], b["lon"], b["lat"]])
    return 6371 * 2 * math.asin(math.sqrt(
        math.sin((la2 - la1) / 2) ** 2
        + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2))


def bake(corridor):
    """searoute over één corridor -> (polyline [[lat,lon],...], passages, km) of None."""
    a, b = corridor["a"], corridor["b"]
    r = sr.searoute([a["lon"], a["lat"]], [b["lon"], b["lat"]], units="km",
                    append_orig_dest=True, return_passages=True)
    km = r["properties"]["length"]
    if not km or km <= 0:
        return None
    pts, seen = [], None
    for lon, lat in r["geometry"]["coordinates"]:
        p = [round(lat, PRECISION), round(lon, PRECISION)]
        if p != seen:
            pts.append(p)
            seen = p
    passages = sorted(r["properties"].get("traversed_passages") or [])
    return pts, passages, km


def main():
    resources = sys.argv[1:]
    raw = subprocess.run(
        ["node", str(ROOT / "tools" / "extract_corridors.js"), *resources],
        capture_output=True, text=True, check=True).stdout
    corridors = json.loads(raw)
    print(f"corridors te bakken: {len(corridors)}"
          f" ({', '.join(resources) if resources else 'alle grondstoffen'})")

    entries, failures, total_pts = [], [], 0
    for c in corridors:
        try:
            res = bake(c)
        except Exception as e:  # searoute kan ook exceptions gooien (punt buiten net)
            res = None
            c["err"] = str(e)
        if res is None:
            failures.append(c)
            continue
        pts, passages, km = res
        total_pts += len(pts)
        ratio = km / max(gc_km(c["a"], c["b"]), 1e-9)
        entries.append((c["key"], pts, passages, c, round(km), round(ratio, 3)))

    # FOUTEN HARD (spec §4): niet stil doorgaan.
    if failures:
        print(f"\nBUILD FAALT — {len(failures)} corridor(s) niet routeerbaar:")
        for c in failures:
            print(f"  {c['a']['id']} ({c['a']['lat']},{c['a']['lon']}) -> "
                  f"{c['b']['id']} ({c['b']['lat']},{c['b']['lon']})"
                  + (f"  [{c['err']}]" if c.get("err") else ""))
        sys.exit(1)

    # sanity-checks (build-standalone.py-stijl)
    assert entries, "sanity: 0 corridors gebakken"
    suspects = [(k, c, r) for k, _p, pas, c, _km, r in entries
                if r > 1.15 and not pas]
    if suspects:
        print(f"\nLET OP — {len(suspects)} corridor(s) >15% boven grote-cirkel "
              f"zonder doorgang (spec §9, handmatig beoordelen):")
        for k, c, r in suspects:
            print(f"  {c['a']['id']} -> {c['b']['id']}  ratio {r}")

    entries.sort(key=lambda e: e[0])  # determinisme
    lines = [
        "// _searoutes.js — GEGENEREERD door tools/bake_searoutes.py — NIET met de hand bewerken.",
        "//",
        "// Corridor-cache: echte zeeroutes over MARNET (searoute), gebakken at build-time.",
        "// Sleutel: \"lat,lon|lat,lon\" (3 decimalen, paar gesorteerd — richtingsonafhankelijk).",
        "// Waarde: { pts: [[lat,lon],...] van a naar b zoals geëxtraheerd,",
        "//           passages: doorgangen die de route passeert (traversed_passages) }.",
        "// Zie design/zeeroutes.md. flows.js keert de polyline om als de leg andersom loopt.",
        "const SEAROUTES = {",
    ]
    for key, pts, passages, c, km, ratio in entries:
        pts_js = ",".join(f"[{la},{lo}]" for la, lo in pts)
        pas_js = ",".join(f'"{p}"' for p in passages)
        lines.append(
            f'  "{key}": {{ pts: [{pts_js}], passages: [{pas_js}] }},'
            f' // {c["a"]["id"]} -> {c["b"]["id"]}  {km} km  x{ratio}')
    lines.append("};")
    lines.append("")
    lines.append("// Grondstoffen die volledig op de cache draaien (ontbrekende corridor = kapot,")
    lines.append("// nooit stil terugvallen op A*). Andere grondstoffen gebruiken nog Routing.sea.")
    baked = sorted(set(r for _k, _p, _pas, c, _km, _r in entries for r in c["resources"]))
    lines.append("const SEAROUTES_BAKED = { " + ", ".join(f'"{r}": true' for r in baked) + " };")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    kb = OUT.stat().st_size / 1024
    print(f"\nOK: {len(entries)} corridors, {total_pts} punten "
          f"-> {OUT.name} ({kb:.0f} KB)")
    print(f"gedekte grondstoffen: {', '.join(baked)}")


if __name__ == "__main__":
    main()
