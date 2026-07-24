#!/usr/bin/env python3
"""
run_landnet_wereld.py — draait fetch_landnet per bulk-regio over álle extracts.

Per regio in plaats van in één keer: het vouwen en de dedup houden de hele regio
in geheugen, en de wereld in één keer is meerdere GB. Regiogrenzen zijn
continentaal, dus doorgaande ketens worden er nauwelijks door geknipt — en wat
er wél op een grens ligt, hecht in de bake alsnog aan elkaar (gedeelde cel).

Draaien:  python v2/tools/run_landnet_wereld.py
"""

import os
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fetch_landnet as fl  # noqa: E402

REGIOS = ["oc", "af", "sa", "na", "as", "cn", "ru", "eu"]   # klein → groot


def main():
    alles = fl.alle_sleutels()
    per_regio = {}
    for s in alles:
        per_regio.setdefault(fl.regio_van(s), []).append(s)
    print(f"{len(alles)} extracts over {len(per_regio)} regio's")

    t0 = time.time()
    totaal_km = totaal_ketens = 0
    for regio in REGIOS:
        sleutels = sorted(per_regio.get(regio, []))
        if not sleutels:
            continue
        print(f"\n{'=' * 74}\nREGIO {regio.upper()} — {len(sleutels)} extracts\n{'=' * 74}",
              flush=True)
        t1 = time.time()
        fl.land_scan(sleutels, "spoor")
        ways = fl.land_laad(sleutels, "spoor")
        ketens = fl.vouw_ketens(ways)
        fl.keten_invariant(ways, ketens)
        del ways
        ketens, rap = fl.dedup_parallel(ketens)
        ketens = fl.heel_naden(ketens)
        ketens = fl.herstel_verbindingen(ketens, rap["verwijderd"])
        ketens = fl.snoei_componenten(ketens)
        fl.schrijf_geojson(ketens, "spoor", f"-{regio}")
        km = sum(k["km"] for k in ketens)
        totaal_km += km
        totaal_ketens += len(ketens)
        print(f"  REGIO {regio.upper()} KLAAR: {km:,.0f} km · {len(ketens):,} ketens "
              f"in {time.time() - t1:,.0f}s", flush=True)

    print(f"\n{'=' * 74}\nWERELD: {totaal_km:,.0f} km · {totaal_ketens:,} ketens "
          f"in {time.time() - t0:,.0f}s\n{'=' * 74}")


if __name__ == "__main__":
    main()
